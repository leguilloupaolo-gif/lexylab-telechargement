# Stratégie de communication LexyLab (document vivant)

> Tenu à jour par l'agent de communication. Chaque lundi, il relit les chiffres, met à jour les
> « Apprentissages » et ajuste le « Mix de la semaine ». Il ne supprime jamais l'historique.

## 1. Objectif
Faire connaître LexyLab (correcteur pensé pour la dyslexie, Mac et Windows, hors ligne) et amener des
gens à cliquer sur le lien en bio. À court terme, l'indicateur principal est l'**attention** : vues,
temps de visionnage, partages et sauvegardes. Les abonnés et les clics viendront ensuite.

## 2. Cibles (par ordre de priorité)
**Répartition décidée par Paolo (10/11) : 25 % des posts pour les mamans** (soit 2 à 3 posts sur 10 par semaine, républications comprises),
**75 % pour les autres cibles** : élèves et étudiants dys, adultes dys au travail, logopèdes et enseignants, et tous les dys en général
(fondateur, mythes, astuces, quiz). Répartis ces 75 % entre ces cibles, selon les stats. Les mamans ne doivent jamais dépasser 3 posts sur 10.
1. **Élèves et étudiants dys (15-25 ans)** : cours, examens, devoirs, mails aux profs, jobs étudiants. → TikTok surtout.
2. **Mamans (et parents) d'enfants dys** : cible prioritaire, mais **pas la seule**. Devoirs du soir, dictées, mots du prof,
   rendez-vous chez le logopède, peur pour l'avenir, fierté des progrès, culpabilité (« est-ce que j'en fais assez ? »).
   Ce qu'elles veulent : se sentir comprises, des astuces concrètes, un outil qui rend leur enfant plus autonome.
   Ton : doux, rassurant, complice (« entre mamans »), jamais culpabilisant.
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

**Analyse du 9/11/2026** (chiffres du 19/10 au 9/11 ; les posts du 7 et 8/11 ont moins de 3 jours, donc prudence) :
- TikTok : la nouvelle série monte nettement. Kinetic mamans 779 vues, sketch CV 755, demo mail au prof 690, contre environ 280 pour les sketchs bâton d'octobre. Le texte animé et la demo marchent aussi bien que les sketchs sur TikTok. À confirmer sur 2 posts de chaque.
- Instagram : tous les posts récents restent bas (150 à 237 vues), loin des posts école/émotion d'octobre (619 et 348). Le temps moyen de visionnage suit : environ 8 s pour les posts émotion, 3,5 à 5,5 s pour les nouveaux. Sur Instagram, l'émotion école garde l'avantage.
- Partages et sauvegardes presque nuls partout (seul « groupe de classe » a 5 partages sur Instagram). Il faut des contenus « à garder » : astuces, listes, carrousels. Le carrousel n'a pas encore été testé : priorité cette semaine.
- Heures : 10 h ou 18 h 30, pas de différence claire pour l'instant (le CV à 18 h 30 est le meilleur récent sur Instagram). Cette semaine, test des deux créneaux les jours à 2 posts.
- Toujours aucune vraie capture de LexyLab dans `captures/` : le format `capture` reste impossible.

## 8. Mix de la semaine (mis à jour chaque lundi)
**Rythme (décision de Paolo, 8/11) : 10 posts par semaine.** 2 posts le lundi, le mercredi et le vendredi, 1 post les autres jours. Toujours avec voix off (sauf carrousels).
Semaine du 6/11 : phase de découverte, chaque format testé au moins 2 fois.
Ordre conseillé : demo → kinetic mamans → sketch → quiz → kinetic émotion → sketch maman/enfant → kinetic fondateur.
Les posts « mamans » passent de préférence le soir (après les devoirs) ou le mercredi.

**Semaine du 9/11** (10 posts, toujours avec voix off sauf carrousels) :
- Lun 9 : 10 h kinetic fondateur (70 % : meilleur sujet TikTok) ; 18 h demo maman, mot au prof (70 % mamans + demo, le soir).
- Mar 10 : sketch maman/devoirs (rendu BD, décor chambre) : 70 % mamans.
  → Fait le 10/11 : kinetic POV dictée à 10 h à la place (déjà une republication sketch devoirs et une kinetic mamans ce jour-là). Sketch maman/devoirs reporté à sam 14 ou dim 15.
- Mer 11 : 10 h quiz (20 % : premier quiz, engagement) ; 18 h kinetic astuces devoirs mamans (70 %).
- Jeu 12 : présentation produit « correcteur classique vs LexyLab » (10 % pari) si ses voix sont prêtes, sinon kinetic mythes.
  → Fait le 12/11 : présentation classique vs LexyLab à 10 h (voix prêtes), IG + TikTok.
- Ven 13 : 10 h carrousel « 5 raisons » (10 % pari : sauvegardes) ; 18 h kinetic mythes dyslexie ou kinetic POV dictée (20 % émotion école, pour Instagram).
  → Fait le 13/11 : 10 h carrousel « 5 raisons » ; 18 h kinetic mythes dyslexie (thème clair), IG + TikTok.
- Sam 14 : sketch école ou étudiant (70 %). Dim 15 : kinetic émotion (POV dictée) ou sketch, selon les voix prêtes.
  → Mise à jour 10/11 (règle des 25 %) : cette semaine, les mamans ont déjà 3 posts (lun 18 h demo, mar 20 h 30 republication, mer 18 h astuces).
    Le sketch maman/devoirs est reporté à la semaine prochaine. Sam et dim : étudiants, travail ou tous les dys.
  → Fait le 11/11 : 10 h quiz-courses ; 18 h kinetic astuces relire (étudiants) à la place des astuces devoirs mamans (plafond de 3 posts mamans sur 7 jours atteint). Astuces devoirs mamans reportées à la semaine prochaine.
- Répartition visée : 7 posts « ce qui marche » (mamans, fondateur, école/émotion), 2 variantes (quiz, POV), 1 pari (carrousel ou présentation).
