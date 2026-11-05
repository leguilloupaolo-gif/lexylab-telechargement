#!/usr/bin/env python3
"""Génère une vidéo LexyLab style bâton (1080x1920, 30 i/s, avec son).

Usage : python3 make_video.py <scenario_id> <sortie.mp4>
        python3 make_video.py --preview <scenario_id> <dossier>   (quelques images PNG pour vérifier)
Le scénario est lu dans scenarios.json (même dossier).
"""
import json, os, subprocess, sys, wave
import numpy as np
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
FPS = 30
SR = 44100


def load_scenario(sid):
    data = json.load(open(os.path.join(HERE, "scenarios.json"), encoding="utf-8"))
    for s in data:
        if s["id"] == sid:
            return s
    sys.exit(f"Scénario introuvable : {sid}")


# ---------------- son ----------------
def env(n, a=0.005, r=0.2):
    t = np.arange(n) / SR
    e = np.minimum(1, t / max(a, 1e-4)) * np.exp(-t / r)
    return e


def tone(f, d, a=0.005, r=0.2, kind="sine"):
    n = int(d * SR); t = np.arange(n) / SR
    w = np.sin(2 * np.pi * f * t)
    if kind == "tri":
        w = 2 / np.pi * np.arcsin(np.sin(2 * np.pi * f * t))
    return w * env(n, a, r)


def add(buf, sig, t0, g=1.0):
    i = int(t0 * SR)
    if i >= len(buf): return
    j = min(len(buf), i + len(sig))
    buf[i:j] += sig[: j - i] * g


def soundtrack(info, path):
    dur = info["duration"]; n = int(dur * SR)
    rng = np.random.default_rng(7)
    music = np.zeros(n); sfx = np.zeros(n)
    # fond musical doux (accords + arpège)
    chords = [[261.6, 329.6, 392.0, 493.9], [220.0, 261.6, 329.6, 392.0],
              [174.6, 220.0, 261.6, 329.6], [196.0, 246.9, 293.7, 329.6]]
    bar = 2.4; k = 0; t = 0.0
    while t < dur:
        ch = chords[k % 4]
        for f in ch:
            add(music, tone(f / 2, bar + 0.4, a=0.3, r=1.6), t, 0.05)
        for i, f in enumerate([ch[0], ch[2], ch[1], ch[3], ch[2], ch[1]]):
            add(music, tone(f, 0.5, a=0.004, r=0.18, kind="tri"), t + i * bar / 6, 0.06)
        add(music, tone(ch[0] / 4, 0.6, a=0.01, r=0.3), t, 0.12)
        t += bar; k += 1
    fade = np.ones(n); fo = int(1.5 * SR); fade[-fo:] = np.linspace(1, 0, fo)
    music *= fade
    # effets
    for e in info["events"]:
        tt, ty = e["t"], e["type"]
        if ty == "pop":
            d = 0.12; m = int(d * SR); x = np.arange(m) / SR
            f = 500 + 900 * x / d
            add(sfx, np.sin(2 * np.pi * np.cumsum(f) / SR) * env(m, 0.002, 0.04), tt, 0.5)
        elif ty == "whoosh":
            m = int(0.45 * SR); w = rng.standard_normal(m)
            w = np.convolve(w, np.ones(30) / 30, "same")
            add(sfx, w * np.sin(np.linspace(0, np.pi, m)) ** 2, tt, 0.6)
        elif ty == "buzz":
            add(sfx, tone(140, 0.35, a=0.01, r=0.2, kind="tri") + tone(147, 0.35, a=0.01, r=0.2, kind="tri"), tt, 0.25)
        elif ty == "ding":
            add(sfx, tone(1318.5, 0.6, r=0.25) + 0.5 * tone(1975.5, 0.6, r=0.18), tt, 0.25)
        elif ty == "steps":
            for i in range(4):
                m = int(0.06 * SR); w = rng.standard_normal(m) * env(m, 0.001, 0.015)
                add(sfx, np.convolve(w, np.ones(12) / 12, "same"), tt + i * 0.25, 0.9)
        elif ty == "chime":
            for i, f in enumerate([523.3, 659.3, 784.0, 1046.5]):
                add(sfx, tone(f, 1.2, r=0.5), tt + i * 0.09, 0.18)
    for a, b in info["typing"]:
        tt = a
        while tt < b:
            m = int(0.025 * SR); w = rng.standard_normal(m) * env(m, 0.0005, 0.006)
            add(sfx, w, tt, 0.35)
            tt += 0.06 + rng.random() * 0.07
    mix = music + sfx
    mix = mix / max(1e-6, np.abs(mix).max()) * 0.85
    pcm = (mix * 32767).astype(np.int16)
    with wave.open(path, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())


# ---------------- image ----------------
def open_page(p, sc):
    b = p.chromium.launch()
    page = b.new_page(viewport={"width": 1080, "height": 1920})
    page.goto("file://" + os.path.join(HERE, "template.html"))
    page.wait_for_load_state("networkidle")
    info = page.evaluate("sc => init(sc)", sc)
    page.evaluate("document.fonts.ready")
    return b, page, info


def main():
    if sys.argv[1] == "--preview":
        sid, outdir = sys.argv[2], sys.argv[3]
        os.makedirs(outdir, exist_ok=True)
        sc = load_scenario(sid)
        with sync_playwright() as p:
            b, page, info = open_page(p, sc)
            for t in [2, 6, 10.5, 11.6, 14, 18, 22.5, 26, 29, 31.5, 34, 37]:
                page.evaluate(f"render({t})")
                page.screenshot(path=os.path.join(outdir, f"t{t:05.1f}.png"))
            b.close()
        return
    sid, out = sys.argv[1], sys.argv[2]
    sc = load_scenario(sid)
    wav = out + ".wav"
    with sync_playwright() as p:
        b, page, info = open_page(p, sc)
        soundtrack(info, wav)
        nfr = int(info["duration"] * FPS)
        ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "image2pipe", "-framerate", str(FPS), "-i", "-",
                               "-i", wav, "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
                               "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", out],
                              stdin=subprocess.PIPE)
        for i in range(nfr):
            page.evaluate(f"render({i / FPS})")
            ff.stdin.write(page.screenshot(type="jpeg", quality=92))
            if i % 150 == 0:
                print(f"  image {i}/{nfr}", flush=True)
        ff.stdin.close(); ff.wait()
        b.close()
    os.remove(wav)
    print("OK ->", out)


if __name__ == "__main__":
    main()
