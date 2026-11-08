# Stratégie de communication LexyLab (document vivant)

> Tenu à jour par l'agent de communication. Chaque lundi, il relit les chiffres, met à jour les
> « Apprentissages » et ajuste le « Mix de la semaine ». Il ne supprime jamais l'historique.

## 1. Objectif
Faire connaître LexyLab (correcteur pensé pour la dyslexie, Mac et Windows, hors ligne) et amener des
gens à cliquer sur le lien en bio. À court terme, l'indicateur principal est l'**attention** : vues,
temps de visionnage, partages et sauvegardes. Les abonnés et les clics viendront ensuite.

## 2. Cibles (par ordre de priorité)
1. **Élèves et étudiants dys (15-25 ans)** : cours, examens, devoirs, mails aux profs, jobs étudiants. → TikTok surtout.
2. **Mamans (et parents) d'enfants dys** : cible **prioritaire sur Instagram**. Devoirs du soir, dictées, mots du prof,
   rendez-vous chez le logopède, peur pour l'avenir, fierté des progrès, culpabilité (« est-ce que j'en fais assez ? »).
   Ce qu'elles veulent : se sentir comprises, des astuces concrètes, un outil qui rend leur enfant plus autonome.
   Ton : doux, rassurant, complice (« entre mamans »), jamais culpabilisant. **Au moins 2 posts par semaine pour elles.**
3. **Adultes dys au travail** : mails, rapports, CV.
4. **Logopèdes et enseignants** : ils recommandent. Contenus éducatifs, sérieux, bienveillants.

## 3. Positionnement et messages
- Promesse : « Écris comme tu penses, LexyLab s'occupe de l'orthographe. »
- Preuves (on ne dit **que** ça) : pensé pour la dyslexie ; créé par un étudiant dys ; souligne en direct ;
  comprend les mots écrits comme on les entend ; explique certaines fautes ; hors ligne, textes privés ;
  Word, Gmail, Google Docs, Outlook, navigateur ; Mac et Windows.
- Ton : chaleureux, drôle, jamais moqueur, jamais culpabilisant. On parle aux dys **comme un pote dys**.

## 4. Piliers de contenu
| Pilier | Formats possibles | Rôle |
|---|---|---|
| **situations** : galères du quotidien | sketch (bâton), kinetic POV | identification, partage |
| **demo** : le produit en action | demo (maquette ou vraie capture) | conversion, preuve |
| **education** : comprendre la dyslexie, astuces | kinetic (mythe/réalité, astuces, chiffres sourcés) | sauvegardes, crédibilité, logopèdes |
| **emotion** : souvenirs d'école, remarques blessantes | kinetic sombre, sketch | commentaires, portée |
| **engagement** : jeux, quiz, questions | quiz, kinetic « commente » | commentaires, algorithme |
| **fondateur** : l'histoire derrière LexyLab (sans prénom) | kinetic | confiance, meilleur score TikTok |
| **mamans** : le quotidien des mamans d'enfants dys | sketch maman/enfant, kinetic « entre mamans », astuces devoirs, demo mot au prof | communauté, partages entre mamans |

## 5. Formats disponibles (dossier `formats/`)
**Règle n°1 (demande de Paolo) : priorité aux VRAIS visuels de LexyLab.** Dès qu'il y a des captures ou des
enregistrements d'écran dans `captures/`, le format `capture` devient le format principal pour le pilier demo
(au moins 3 posts par semaine), et la maquette `demo` n'est plus utilisée que si aucune vraie capture ne convient.
Les visuels dessinés (sketch, kinetic, quiz) restent possibles pour l'humour, l'éducation et l'engagement,
mais on ne fait jamais passer un dessin ou une maquette pour l'appli réelle.
- `presentation` : présentation produit premium (motion design sombre ou clair) ; existe aussi en **carrousel** (images à faire glisser).
- `capture` : montage de **vraies** captures ou vidéos d'écran de LexyLab, avec zoom, cadres rouges, sous-titres, musique et fin. Le badge « ● Vraie capture » s'affiche.
- `sketch` : sketch bâton (~39 s), 2 personnages, bulles, écran avec fautes puis correction.
- `demo` : fenêtre Word, Gmail, Docs ou Notes, frappe, soulignement, bulle LexyLab, clic, correction, sous-titres façon voix off (~20 s). Peut finir sur une **vraie capture** de `captures/`.
- `kinetic` : texte animé mot par mot, cartes « mythe / réalité », listes numérotées, POV (~15-30 s).
- `quiz` : « trouve les fautes » avec compte à rebours, puis révélation (~20 s).
- L'agent **peut créer un nouveau format** (nouveau fichier HTML qui respecte le contrat décrit dans `render.py`)
  quand une idée ne rentre dans aucun format. Il le teste toujours avec `--preview` avant de publier.

## 6. Règles d'expérimentation (test & learn)
- **70 / 20 / 10** : 70 % des posts reprennent ce qui marche le mieux, 20 % sont des variantes (nouvelle
  accroche, autre durée, autre pilier sur le format gagnant), 10 % sont des paris (nouveau format, nouvelle idée).
- Chaque post a **une hypothèse** écrite dans le journal (ex. « une accroche-question en 1re seconde augmente la rétention »).
- On compare après **au moins 3 jours** de vie d'un post, et sur au moins 2 posts du même type avant de conclure.
- Indicateurs : vues, portée, temps moyen, rétention ou taux vu en entier, partages, sauvegardes, commentaires.
  Score simple pour comparer : `vues + 10 × (partages + sauvegardes) + 5 × commentaires`.
- Pas plus de 2 jours de suite le même format. Varier les cibles dans la semaine.
- Les 2 premières secondes comptent le plus : accroche forte, texte gros, problème clair.

## 7. Apprentissages (mis à jour par l'agent)
**Point de départ, 5/11/2026** (chiffres du 15/10 au 30/10) :
- TikTok : la vidéo **fondateur** (« mes copies revenaient pleines de rouge ») est la meilleure (1 864 vues).
  Ensuite la **dictée** (862) et la **lettre de motivation** (740). Les sujets travail ou mail font environ 280 vues.
- Instagram : les sujets **école, parents, enfants** gagnent (« Tu dois faire plus attention » 616 vues, dictée 582).
  Les sujets adultes ou travail sont plus bas (mail 182, notes 184).
- Hypothèse de départ : **émotion + école + histoire vraie** > situations pro. À tester.
- Pas encore de données sur les formats demo, quiz, kinetic : à tester dans les 2 premières semaines.

## 8. Mix de la semaine (mis à jour chaque lundi)
Semaine du 6/11 : phase de découverte, chaque format testé au moins 2 fois.
Ordre conseillé : demo → kinetic mamans → sketch → quiz → kinetic émotion → sketch maman/enfant → kinetic fondateur.
Les posts « mamans » passent de préférence le soir (après les devoirs) ou le mercredi.
