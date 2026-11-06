#!/usr/bin/env python3
"""Moteur vidéo LexyLab : transforme une page HTML animée en MP4 vertical 1080x1920, 30 i/s, avec son.

Usage :
  python3 render.py <idee_id> <sortie.mp4>                 idée lue dans idees.json
  python3 render.py --json <fichier.json> <sortie.mp4>     idée lue dans un fichier (un objet)
  python3 render.py --preview <idee_id|fichier.json> <dossier>   12 images PNG pour vérifier

Une idée = {"id", "format", "params", "post_text", "tiktok_title", "pilier", "hypothese"}
"format" = nom d'un fichier de formats/ (capture, sketch, demo, kinetic, quiz, ... ou un nouveau format créé par l'agent).

Contrat d'une page de format (formats/<nom>.html) :
  window.init(params)  -> {duration: secondes, events: [{t, type}], typing: [[debut, fin], ...], music: "calme|joyeux|tension|aucune"}
  window.render(t)     -> dessine l'image au temps t (secondes)
  types de sons : pop, whoosh, buzz, ding, steps, chime, click, tick, boom, swoosh-up
  voix off : évènement {t, type:"voice", file:"voix/xxx.m4a"} ; la musique baisse automatiquement pendant la voix.
  params._voix_dur = {"voix/xxx.m4a": durée en s} est ajouté par render.py (seulement pour les fichiers qui existent).
"""
import json, os, subprocess, sys, tempfile, wave
import numpy as np
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
FPS = 30
SR = 44100


def load_idea(ref):
    if ref.endswith(".json") and os.path.exists(ref):
        return json.load(open(ref, encoding="utf-8"))
    for s in json.load(open(os.path.join(HERE, "idees.json"), encoding="utf-8")):
        if s["id"] == ref:
            return s
    sys.exit(f"Idée introuvable : {ref}")


# ---------------- son ----------------
def env(n, a=0.005, r=0.2):
    t = np.arange(n) / SR
    return np.minimum(1, t / max(a, 1e-4)) * np.exp(-t / r)


def tone(f, d, a=0.005, r=0.2, kind="sine"):
    n = int(d * SR); t = np.arange(n) / SR
    w = np.sin(2 * np.pi * f * t)
    if kind == "tri":
        w = 2 / np.pi * np.arcsin(np.sin(2 * np.pi * f * t))
    return w * env(n, a, r)


def add(buf, sig, t0, g=1.0):
    i = int(t0 * SR)
    if i >= len(buf) or i < 0: return
    j = min(len(buf), i + len(sig))
    buf[i:j] += sig[: j - i] * g


MOODS = {
    "calme": dict(chords=[[261.6, 329.6, 392.0, 493.9], [220.0, 261.6, 329.6, 392.0], [174.6, 220.0, 261.6, 329.6], [196.0, 246.9, 293.7, 329.6]], bar=2.4, arp=6, gain=1.0),
    "joyeux": dict(chords=[[261.6, 329.6, 392.0, 523.3], [196.0, 246.9, 293.7, 392.0], [220.0, 261.6, 329.6, 440.0], [174.6, 220.0, 261.6, 349.2]], bar=1.6, arp=8, gain=1.1),
    "tension": dict(chords=[[220.0, 261.6, 329.6, 415.3], [207.7, 246.9, 311.1, 392.0], [196.0, 233.1, 293.7, 349.2], [207.7, 246.9, 311.1, 392.0]], bar=2.0, arp=4, gain=0.9),
}


def decode_audio(path):
    if not os.path.exists(path):
        return None
    out = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"],
                         capture_output=True)
    if out.returncode != 0:
        return None
    return np.frombuffer(out.stdout, dtype=np.int16).astype(np.float64) / 32768


def audio_duration(path):
    a = decode_audio(path)
    return None if a is None else len(a) / SR


def voice_durations(obj, acc):
    """Cherche tous les chemins 'voix/...' dans les paramètres et mesure leur durée (s). Fichier absent = ignoré."""
    if isinstance(obj, dict):
        for v in obj.values(): voice_durations(v, acc)
    elif isinstance(obj, list):
        for v in obj: voice_durations(v, acc)
    elif isinstance(obj, str) and obj.startswith("voix/"):
        d = audio_duration(os.path.join(HERE, obj))
        if d: acc[obj] = round(d, 3)
    return acc


def soundtrack(info, path):
    dur = info["duration"]; n = int(dur * SR)
    rng = np.random.default_rng(7)
    music = np.zeros(n); sfx = np.zeros(n)
    mood = MOODS.get(info.get("music", "calme"))
    if mood:
        bar = mood["bar"]; k = 0; t = 0.0
        while t < dur:
            ch = mood["chords"][k % 4]
            for f in ch:
                add(music, tone(f / 2, bar + 0.4, a=0.3, r=1.6), t, 0.05)
            seq = [ch[0], ch[2], ch[1], ch[3], ch[2], ch[1], ch[3], ch[2]][: mood["arp"]]
            for i, f in enumerate(seq):
                add(music, tone(f, 0.5, a=0.004, r=0.18, kind="tri"), t + i * bar / len(seq), 0.06)
            add(music, tone(ch[0] / 4, 0.6, a=0.01, r=0.3), t, 0.12)
            if info.get("music") == "joyeux":
                for i in range(4):
                    m = int(0.03 * SR); add(music, rng.standard_normal(m) * env(m, 0.0005, 0.008), t + i * bar / 4 + bar / 8, 0.08)
            t += bar; k += 1
        music *= mood["gain"]
        fo = int(1.5 * SR); music[-fo:] *= np.linspace(1, 0, fo)
    for e in info.get("events", []):
        tt, ty = e["t"], e["type"]
        if ty == "pop":
            d = 0.12; m = int(d * SR); x = np.arange(m) / SR
            add(sfx, np.sin(2 * np.pi * np.cumsum(500 + 900 * x / d) / SR) * env(m, 0.002, 0.04), tt, 0.5)
        elif ty in ("whoosh", "swoosh-up"):
            m = int(0.45 * SR); w = np.convolve(rng.standard_normal(m), np.ones(30) / 30, "same")
            add(sfx, w * np.sin(np.linspace(0, np.pi, m)) ** 2, tt, 0.6)
        elif ty == "buzz":
            add(sfx, tone(140, 0.35, a=0.01, r=0.2, kind="tri") + tone(147, 0.35, a=0.01, r=0.2, kind="tri"), tt, 0.25)
        elif ty == "ding":
            add(sfx, tone(1318.5, 0.6, r=0.25) + 0.5 * tone(1975.5, 0.6, r=0.18), tt, 0.25)
        elif ty == "click":
            m = int(0.02 * SR); add(sfx, rng.standard_normal(m) * env(m, 0.0003, 0.004), tt, 0.6)
        elif ty == "tick":
            add(sfx, tone(1800, 0.05, a=0.001, r=0.015), tt, 0.35)
        elif ty == "boom":
            m = int(0.6 * SR); x = np.arange(m) / SR
            add(sfx, np.sin(2 * np.pi * np.cumsum(120 - 70 * x / 0.6) / SR) * env(m, 0.003, 0.25), tt, 0.7)
        elif ty == "steps":
            for i in range(4):
                m = int(0.06 * SR); w = rng.standard_normal(m) * env(m, 0.001, 0.015)
                add(sfx, np.convolve(w, np.ones(12) / 12, "same"), tt + i * 0.25, 0.9)
        elif ty == "chime":
            for i, f in enumerate([523.3, 659.3, 784.0, 1046.5]):
                add(sfx, tone(f, 1.2, r=0.5), tt + i * 0.09, 0.18)
    for a, b in info.get("typing", []):
        tt = a
        while tt < b:
            m = int(0.025 * SR); add(sfx, rng.standard_normal(m) * env(m, 0.0005, 0.006), tt, 0.35)
            tt += 0.06 + rng.random() * 0.07
    # voix off : fichiers audio (voix/*.m4a) placés par le format avec des évènements {t, type:"voice", file}
    voice = np.zeros(n)
    for e in info.get("events", []):
        if e.get("type") == "voice" and e.get("file"):
            v = decode_audio(os.path.join(HERE, e["file"]))
            if v is not None:
                add(voice, v, e["t"], 1.0)
    if np.abs(voice).max() > 0:
        voice = voice / np.abs(voice).max() * 0.95
        envv = np.convolve(np.abs(voice), np.ones(int(0.25 * SR)) / (0.25 * SR), "same")
        duck = 1 - 0.7 * np.clip(envv / max(1e-6, envv.max()) * 4, 0, 1)
        music *= duck; sfx *= (0.5 + 0.5 * duck)
    mix = music + sfx + voice * 0.9
    mix = mix / max(1e-6, np.abs(mix).max()) * 0.85
    with wave.open(path, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix * 32767).astype(np.int16).tobytes())


# ---------------- image ----------------
def prepare_videos(idea):
    """Pour le format capture : extrait les images des enregistrements d'écran (30 i/s)."""
    plans = idea.get("params", {}).get("plans", [])
    for i, pl in enumerate(plans):
        if pl.get("video"):
            src = os.path.join(HERE, pl["video"])
            if not os.path.exists(src):
                sys.exit(f"Vidéo introuvable : {src}")
            d = tempfile.mkdtemp(prefix=f"plan{i}_")
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(pl.get("start", 0)), "-i", src,
                            "-t", str(pl["end"] - pl.get("start", 0)), "-vf", f"fps={FPS},scale='min(1600,iw)':-2",
                            "-q:v", "3", os.path.join(d, "f%05d.jpg")], check=True)
            pl["_frames"] = "file://" + d
            pl["_count"] = len(os.listdir(d))
            pl["end"] = pl["end"] - pl.get("start", 0)  # les images commencent au début de l'extrait
            pl["start"] = 0
    if plans:
        idea["params"]["_fps"] = FPS


def open_page(p, idea):
    prepare_videos(idea)
    page_path = os.path.join(HERE, "formats", idea["format"] + ".html")
    if not os.path.exists(page_path):
        sys.exit(f"Format introuvable : {page_path}")
    b = p.chromium.launch()
    page = b.new_page(viewport={"width": 1080, "height": 1920})
    errors = []
    page.on("pageerror", lambda e: errors.append(str(e)))
    page.goto("file://" + page_path)
    page.wait_for_load_state("networkidle")
    idea["params"]["_voix_dur"] = voice_durations(idea["params"], {})
    info = page.evaluate("p => init(p)", idea["params"])
    page.evaluate("document.fonts.ready")
    page.evaluate("t => render(t)", 0)   # précharge la 1re image
    page.wait_for_timeout(500)
    if errors:
        sys.exit("Erreur JavaScript dans le format : " + " | ".join(errors))
    return b, page, info


def main():
    a = sys.argv[1:]
    if a[0] == "--preview":
        idea = load_idea(a[1]); outdir = a[2]; os.makedirs(outdir, exist_ok=True)
        with sync_playwright() as p:
            b, page, info = open_page(p, idea)
            d = info["duration"]
            for i in range(12):
                t = round(0.3 + i * (d - 0.6) / 11, 2)
                page.evaluate(f"render({t})")
                page.screenshot(path=os.path.join(outdir, f"t{t:05.1f}.png"))
            b.close()
        print(f"Aperçu : {outdir} (durée {info['duration']} s)")
        return
    if a[0] == "--json":
        idea = load_idea(a[1]); out = a[2]
    else:
        idea = load_idea(a[0]); out = a[1]
    wav = out + ".wav"
    with sync_playwright() as p:
        b, page, info = open_page(p, idea)
        soundtrack(info, wav)
        nfr = int(info["duration"] * FPS)
        ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "image2pipe", "-framerate", str(FPS), "-i", "-",
                               "-i", wav, "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
                               "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", out], stdin=subprocess.PIPE)
        for i in range(nfr):
            page.evaluate(f"render({i / FPS})")
            ff.stdin.write(page.screenshot(type="jpeg", quality=92))
            if i % 300 == 0:
                print(f"  image {i}/{nfr}", flush=True)
        ff.stdin.close(); ff.wait()
        b.close()
    os.remove(wav)
    print("OK ->", out)


if __name__ == "__main__":
    main()
