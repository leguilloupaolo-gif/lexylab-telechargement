#!/usr/bin/env python3
"""Publie sur Instagram SANS Metricool, via l'API officielle de Meta (Instagram API with Instagram Login).

Tourne dans GitHub Actions (.github/workflows/instagram.yml) toutes les 15 minutes.
Lit la file d'attente agent-video/instagram/file.json, publie les posts dont l'heure est passée,
et note le résultat dans le même fichier.

Secrets GitHub nécessaires (jamais dans le dépôt, jamais dans un chat) :
  IG_ACCESS_TOKEN  : jeton d'accès Instagram longue durée (60 jours)
  IG_USER_ID       : identifiant du compte Instagram professionnel
  GH_SECRETS_PAT   : (facultatif) jeton GitHub avec droit « Secrets : écriture » sur ce dépôt, pour renouveler
                     automatiquement IG_ACCESS_TOKEN chaque semaine

Une entrée de file.json :
  {"id": "2026-11-18-quiz-courses", "quand": "2026-11-18T18:00:00+01:00", "type": "REEL" | "CARROUSEL",
   "media": ["https://raw.githubusercontent.com/.../video.mp4"]  (ou plusieurs images pour un carrousel),
   "legende": "texte du post", "statut": "a_publier"}
Le script ajoute : statut = "publie" | "erreur", media_id, publie_le, erreur.
"""
import json, os, sys, time, urllib.parse, urllib.request
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(HERE, "file.json")
API = "https://graph.instagram.com"
TOKEN = os.environ.get("IG_ACCESS_TOKEN", "")
USER = os.environ.get("IG_USER_ID", "")


def call(method, path, **params):
    params["access_token"] = TOKEN
    data = urllib.parse.urlencode(params).encode()
    url = f"{API}/{path}"
    if method == "GET":
        req = urllib.request.Request(url + "?" + data.decode())
    else:
        req = urllib.request.Request(url, data=data, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")
        raise RuntimeError(f"HTTP {e.code} sur {path} : {body.replace(TOKEN, '***')}")


def wait_ready(container, minutes=8):
    for _ in range(minutes * 4):
        st = call("GET", container, fields="status_code,status").get("status_code")
        if st == "FINISHED":
            return
        if st in ("ERROR", "EXPIRED"):
            raise RuntimeError(f"Instagram n'a pas pu traiter le média (statut {st})")
        time.sleep(15)
    raise RuntimeError("Instagram met trop de temps à traiter la vidéo")


def publish(entry):
    caption = entry.get("legende", "")
    if entry["type"] == "REEL":
        c = call("POST", f"{USER}/media", media_type="REELS", video_url=entry["media"][0], caption=caption, share_to_feed="true")["id"]
    elif entry["type"] == "CARROUSEL":
        kids = []
        for url in entry["media"][:10]:
            if url.lower().endswith((".mp4", ".mov")):
                k = call("POST", f"{USER}/media", media_type="VIDEO", video_url=url, is_carousel_item="true")["id"]
            else:
                k = call("POST", f"{USER}/media", image_url=url, is_carousel_item="true")["id"]
            wait_ready(k); kids.append(k)
        c = call("POST", f"{USER}/media", media_type="CAROUSEL", children=",".join(kids), caption=caption)["id"]
    else:
        raise RuntimeError(f"Type inconnu : {entry['type']}")
    wait_ready(c)
    return call("POST", f"{USER}/media_publish", creation_id=c)["id"]


def refresh_token():
    """Prolonge le jeton de 60 jours. Renvoie le nouveau jeton (ou None)."""
    r = call("GET", "refresh_access_token", grant_type="ig_refresh_token")
    return r.get("access_token")


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "publier"
    if not TOKEN or not USER:
        print("Secrets IG_ACCESS_TOKEN / IG_USER_ID pas encore ajoutés dans GitHub : rien à faire.")
        sys.exit(1 if mode == "test" else 0)
    if mode == "test":
        me = call("GET", "me", fields="user_id,username,account_type")
        print(f"OK : connecté au compte @{me.get('username')} ({me.get('account_type')})")
        lim = call("GET", f"{USER}/content_publishing_limit", fields="quota_usage,config")
        print("Quota de publication :", json.dumps(lim.get("data", lim)))
        return
    if mode == "renouveler":
        new = refresh_token()
        if new:
            print(f"::add-mask::{new}")
            out = os.environ.get("TOKEN_OUT")
            if out:
                with open(out, "w") as fh: fh.write(new)
            print("Jeton prolongé de 60 jours.")
        return
    queue = json.load(open(FILE, encoding="utf-8")) if os.path.exists(FILE) else []
    now = datetime.now(timezone.utc)
    changed = False
    for e in queue:
        if e.get("statut") != "a_publier":
            continue
        if datetime.fromisoformat(e["quand"]) > now:
            continue
        try:
            e["media_id"] = publish(e); e["statut"] = "publie"
            print(f"Publié : {e['id']} -> {e['media_id']}")
        except Exception as ex:
            e["statut"] = "erreur"; e["erreur"] = str(ex)[:500]
            print(f"ERREUR {e['id']} : {e['erreur']}")
        e["publie_le"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
        changed = True
    if changed:
        json.dump(queue, open(FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    else:
        print("Rien à publier maintenant.")


if __name__ == "__main__":
    main()
