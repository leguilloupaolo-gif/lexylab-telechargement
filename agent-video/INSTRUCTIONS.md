# Agent de communication LexyLab : 1 vidéo par jour (Instagram + TikTok)

Chaque jour, l'agent :
1. choisit le prochain scénario pas encore publié,
2. génère la vidéo style bâton (1080x1920, ~39 s, avec son),
3. la met en ligne dans ce dépôt (`reseaux-sociaux/auto/`),
4. la programme sur Metricool, en **publication automatique**, sur Instagram (Reel) et TikTok, à la meilleure heure du jour,
5. note la publication dans `journal.json`.

## Fichiers
- `template.html` : la scène animée (personnages bâton, bulles, écran d'ordi, fin avec logo).
- `make_video.py` : génère la vidéo. `python3 make_video.py <id> <sortie.mp4>` (environ 3 min).
  Pour vérifier visuellement : `python3 make_video.py --preview <id> <dossier>` (12 images PNG).
- `scenarios.json` : la liste des scénarios.
- `journal.json` : ce qui a déjà été publié (`[{"date","id","fichier","instagram","tiktok"}]`).

## Format d'un scénario
```
id            identifiant court, unique (ex. "devoir-francais")
caption       petite phrase de contexte en haut (ex. "À la maison, 21h…")
hero_hair     curly | short | cap | long | bun | ponytail   (la personne dys, assise)
friend_hair   bun | ponytail | long | short | curly | cap     (l'ami(e) qui arrive)
p1, p2        2 bulles de la personne dys : le problème (max ~60 caractères chacune)
screen        le texte tapé à l'écran. Chaque faute s'écrit [faute|correction]
              ex. "Je vous [envoi|envoie] le [raport|rapport]." : 3 à 5 fautes, texte de 40 à 70 caractères
f1            l'ami(e) : « T'as pas *LexyLab* ? » (ou variante)
f2, f3        l'ami(e) explique LexyLab (max ~80 caractères)
p3            la personne dys, contente du résultat
f4            phrase de fin de l'ami(e)
post_text     légende du post Instagram/TikTok (avec hashtags)
```
`*mot*` = mot mis en vert dans une bulle.

## Règles de contenu (à respecter absolument)
- **Jamais le prénom de Paolo** (ni aucun vrai nom) dans les vidéos ou les légendes.
- Les fautes doivent être réalistes pour la dyslexie/dysorthographie : fautes phonétiques (« raport », « ojourdui »), lettres confondues, accents oubliés, mots collés. Pas de faute identique à la correction.
- Ce qu'on peut dire de LexyLab (rien d'autre, pas de prix inventé, pas de chiffre inventé) :
  correcteur pensé pour la dyslexie ; créé par un étudiant dys ; souligne les fautes en direct ;
  comprend les mots écrits comme on les entend ; fonctionne sans internet, les textes restent sur l'ordi ;
  marche dans Word, Gmail, Google Docs, Outlook, le navigateur ; disponible sur Mac et Windows.
- Ton : bienveillant, drôle, jamais moqueur envers les dys.
- Pas de nom de concurrent.
- Quand tous les scénarios sont publiés : écrire 10 nouveaux scénarios (situations variées : école, études, travail, vie quotidienne, famille), les ajouter à `scenarios.json`, et en vérifier au moins un avec `--preview`.

## Publication Metricool
- Marque (blogId) : `7384289`, fuseau `Europe/Brussels`.
- URL de la vidéo : `https://raw.githubusercontent.com/leguilloupaolo-gif/lexylab-telechargement/main/reseaux-sociaux/auto/<fichier>.mp4`
  (attendre ~1 min après le push. Le shell ne peut pas vérifier l'URL (proxy) : si Metricool renvoie une URL static.metricool.com dans `media`, c'est bon).
- Heure : `getBestTimeToPostByNetwork` pour le jour même ; prendre la meilleure heure entre maintenant + 1 h et 21 h.
  Instagram et TikTok peuvent avoir des heures différentes (2 posts séparés).
- Instagram : `providers:[{"network":"instagram"}]`, `instagramData: {"type":"REEL","showReelOnFeed":true}`, `autoPublish: true`.
- TikTok : `providers:[{"network":"tiktok"}]`, `tiktokData: {"privacyOption":"PUBLIC_TO_EVERYONE","commercialContentOwnBrand":true,"title":"<courte accroche>"}`, `autoPublish: true`.
- Ne jamais programmer 2 vidéos le même jour sur le même réseau (vérifier avec `getScheduledPosts`).
