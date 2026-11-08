#!/usr/bin/env python3
"""Prépare les textes de voix off d'une ou plusieurs idées et les ajoute à voix/a-generer.txt.

Usage : python3 voix/preparer_voix.py <idee_id> [<idee_id> ...]
        python3 voix/preparer_voix.py --a-venir        (toutes les idées pas encore publiées)
Le Mac fabrique ensuite les fichiers automatiquement (12h30 et 19h45).

Noms de fichiers (lus automatiquement par les formats) :
  kinetic : <id>-<n>       (n = numéro de carte, à partir de 0)
  sketch  : <id>-p1, -p2, -f1, -f2, -f3, -p3, -f4   (une voix par bulle ; personne dys = Thomas, ami(e)/maman = Amélie)
  demo    : <id>-hook, -s0 … -s4   (accroche + sous-titres)
  quiz    : <id>-q, -a, -c          (question, réponse, appel à commenter)
  capture : <id>-hook, -p<plan>-s<n>
  presentation (vidéo) : <id>-<n> (n = numéro de scène) ; les carrousels n'ont pas de voix
Format d'une ligne : voix/<fichier>.m4a|texte|voix (voix = Thomas ou Amélie ; vide = Thomas)
Tu peux ensuite retoucher les textes à la main dans a-generer.txt (prononciation, rythme).
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EMOJI = re.compile("[\U0001F000-\U0001FFFF☀-➿️‍⭐⬆↔-⇿✅❌✨]+")


def clean(t):
    t = (t or "").replace("\n", " ")
    t = re.sub(r"\[([^|\]]+)\|([^\]]+)\]", r"\2", t)
    t = t.replace("*", "").replace("_", "").replace("~", "").replace("«", "").replace("»", "")
    t = EMOJI.sub("", t)
    t = re.sub(r"\s+", " ", t).strip(" :")
    t = t.replace("POV", "Point de vue").replace("✓", "")
    t = t.replace(" · ", ", ")
    if t and t[-1] not in ".!?…":
        t += "."
    return t.replace("?.", "?").replace("!.", "!").strip()


def lines_for(idea):
    i, f, p = idea["id"], idea["format"], idea["params"]
    narr = "Amélie" if idea.get("pilier") == "mamans" else "Thomas"
    out = []
    if f == "kinetic":
        for n, s in enumerate(p["slides"]):
            if s.get("mythe"):
                txt = f"Idée fausse : {clean(s['mythe'])} Réalité : {clean(s['realite'])}"
            else:
                txt = " ".join(x for x in [clean(s.get("text")), clean(s.get("sub"))] if x)
            out.append((f"{i}-{n}", txt, narr))
    elif f == "sketch":
        for k in ["p1", "p2", "f1", "f2", "f3", "p3", "f4"]:
            if p.get(k):
                out.append((f"{i}-{k}", clean(p[k]), "Thomas" if k[0] == "p" else "Amélie"))
    elif f == "demo":
        out.append((f"{i}-hook", clean(p.get("hook")), narr))
        for n, s in enumerate(p.get("subs", [])):
            out.append((f"{i}-s{n}", clean(s), narr))
    elif f == "quiz":
        out += [(f"{i}-q", clean(p.get("question")), narr), (f"{i}-a", clean(p.get("answer") or "LexyLab les a toutes trouvées."), narr),
                (f"{i}-c", clean(p.get("cta") or "Tu en as trouvé combien ? Dis-le en commentaire."), narr)]
    elif f == "presentation" and idea.get("type") != "carrousel":
        for n, sc in enumerate(p.get("scenes", [])):
            parts = [" ".join(sc.get("lignes", [])), sc.get("titre", ""), sc.get("avant", ""), sc.get("sub", "")]
            if sc.get("type") == "logo": parts.append("LexyLab.")
            if sc.get("type") == "liste": parts += sc.get("items", [])
            if sc.get("type") == "duel": parts += [sc["ko"]["titre"] + " : " + sc["ko"]["texte"], sc["ok"]["titre"] + " : " + sc["ok"]["texte"]]
            if sc.get("type") == "editeur": parts.append(re.sub(r"\[([^|\]]+)\|([^\]]+)\]", r"\2", sc.get("ecran", "")))
            out.append((f"{i}-{n}", " ".join(re.sub(r"[.,;:]+$", "", clean(x)) + "." for x in parts if clean(x)).replace(",.", ",").replace("?.", "?").replace("!.", "!"), narr))
    elif f == "capture":
        out.append((f"{i}-hook", clean(p.get("hook")), narr))
        for a, pl in enumerate(p.get("plans", [])):
            for n, s in enumerate(pl.get("subs", [])):
                out.append((f"{i}-p{a}-s{n}", clean(s["text"]), narr))
    return [(n, t, v) for n, t, v in out if t and len(t) > 1]


def main():
    ideas = json.load(open(os.path.join(HERE, "idees.json"), encoding="utf-8"))
    if sys.argv[1:] == ["--a-venir"]:
        done = {j["id"] for j in json.load(open(os.path.join(HERE, "journal.json"), encoding="utf-8"))}
        sel = [x for x in ideas if x["id"] not in done]
    else:
        sel = [x for x in ideas if x["id"] in sys.argv[1:]]
    path = os.path.join(HERE, "voix", "a-generer.txt")
    existing = open(path, encoding="utf-8").read()
    have = {l.split("|")[0] for l in existing.splitlines() if "|" in l}
    new = []
    for idea in sel:
        for name, txt, voice in lines_for(idea):
            key = f"voix/{name}.m4a"
            if key not in have and not os.path.exists(os.path.join(HERE, key)):
                new.append(f"{key}|{txt}|{voice}")
    if new:
        with open(path, "a", encoding="utf-8") as fh:
            fh.write(("" if existing.endswith("\n") else "\n") + "\n".join(new) + "\n")
    print(f"{len(new)} voix ajoutées à a-generer.txt")


if __name__ == "__main__":
    main()
