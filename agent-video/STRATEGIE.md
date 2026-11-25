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
- **Image de marque (Paolo, 13/11) : plus qualitative et plus corporate.** Visuels soignés (motion design, carrousels sobres, texte animé élégant),
  moins de bonshommes bâton (1 toutes les 2 semaines maximum), 1 sketch par semaine maximum (rendu flat ou cartoon).

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
- `sketch` : sketch (~39 s) ; **limité à 1 par semaine depuis le 13/11, bâton 1 toutes les 2 semaines max**, 2 personnages, bulles, écran avec fautes puis correction.
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

**Analyse du 16/11/2026** (chiffres du 26/10 au 16/11) :
- **Alerte : rien n'a été publié du 11 au 15/11.** Les 13 posts programmés (quiz, astuces relire, présentation classique vs LexyLab, carrousel 5 raisons, mythes, présentation pourquoi LexyLab, demo notes) sont tous en erreur dans Metricool : « You have reached your Metricool account limit ». Ce n'était pas un délai de remontée des chiffres. Les tests de la semaine dernière n'ont donc jamais été vus : aucune conclusion possible sur la présentation sombre, le carrousel, le quiz ni le mythe/réalité.
- TikTok (posts jusqu'au 10/11) : plateau stable de 650 à 790 vues quel que soit le format (kinetic mamans 785, demo maman 777, CV 764, kinetic fondateur 763, POV dictée 708, mail prof 699). Seul le sketch devoir du samedi 8/11 (305) décroche. Le sujet compte plus que le format.
- Instagram : toujours bas (145 à 247 vues). Meilleur temps de visionnage : demo maman (6,0 s) et sketch devoir (5,5 s) ; le texte animé mamans et fondateur retient moins (3,6 à 3,9 s). Montrer le produit en action retient mieux que du texte seul.
- Partages et sauvegardes : toujours presque nuls. Le carrousel et les astuces « à garder » restent à tester pour de vrai.
- Les voix off ne sont plus fabriquées depuis le 9/11 : les 4 présentations sombres du 13/11 n'ont pas leurs voix.

**Analyse du 23/11/2026** (chiffres du 2/11 au 23/11 ; Instagram seulement, TikTok n'a aucune donnée depuis le 10/11) :
- Instagram, période test « style 1re vidéo » (posts du 18 au 21/11) : les présentations sombres font 120 à 182 vues (moyenne ~151) et 2,3 à 4,9 s de temps moyen, contre ~174 vues et 3,6 à 6,0 s pour les kinetic, demos et sketchs du 5 au 10/11. Pas de gain d'attention à ce stade (à confirmer au bilan du 27/11).
- Ce qui retient le mieux sur Instagram : montrer le produit en action ou une scène vécue (demo maman 6,0 s, sketch devoir 5,5 s, POV dictée 5,3 s) et le quiz (173 vues, 4,8 s). Le texte seul retient moins (kinetic mamans/fondateur 3,6-3,9 s, présentations 3,6-4,9 s).
- Sujets : école/émotion et candidature (CV 248) restent devant ; la cible logopèdes/enseignants est la plus basse (120 vues, 2,3 s) : à ne refaire qu'en carrousel « à garder ».
- Partages et sauvegardes : toujours 0 sur tous les Reels ; seulement 3 commentaires en 3 semaines (demos mail prof et maman). Les questions en légende ne suffisent pas : tester un appel à commenter à l'écran (mot-clé, choix A/B).
- TikTok : toujours aucune publication depuis le 11/11 (limite du compte Metricool). Le 23/11, les deux posts sont acceptés en attente ; à vérifier demain.

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
  → **Changé le 13/11 (demande de Paolo : plus qualitatif, plus corporate, moins de bâton)** : sam 14 présentation produit « pourquoi LexyLab » (fondateur, thème sombre, voix prêtes) ;
    dim 15 voir ci-dessous. Pas de sketch ce week-end.
  → Fait le 14/11 : 10 h présentation « pourquoi LexyLab » (sombre, fondateur), IG + TikTok.
  → **Précision de Paolo (13/11) : style de la 1re vidéo du compte** (format `presentation` sombre, voir INSTRUCTIONS « Ligne visuelle »).
    Dim 15 : `pres-examen-fiches` (étudiants) si ses voix sont prêtes, sinon une demo. Nouvelles idées dans ce style : `pres-mail-travail`, `pres-examen-fiches`, `pres-mamans-autonomie`.
  → **Période de test : du 13/11 au 27/11** (2 semaines). Bilan chiffré avant/après envoyé au fondateur le 27/11. Tenir le cap sur toute la période pour que la comparaison soit juste.
  → Semaine du 16/11 : au moins 6 posts sur 10 dans le style de la 1re vidéo (présentation sombre ou carrousel sombre) ; en présentation, carrousel, kinetic sobre ou demo ; 1 sketch maximum (rendu flat ou cartoon, pas bâton).
  → Mise à jour 10/11 (règle des 25 %) : cette semaine, les mamans ont déjà 3 posts (lun 18 h demo, mar 20 h 30 republication, mer 18 h astuces).
    Le sketch maman/devoirs est reporté à la semaine prochaine. Sam et dim : étudiants, travail ou tous les dys.
  → Fait le 11/11 : 10 h quiz-courses ; 18 h kinetic astuces relire (étudiants) à la place des astuces devoirs mamans (plafond de 3 posts mamans sur 7 jours atteint). Astuces devoirs mamans reportées à la semaine prochaine.
- Répartition visée : 7 posts « ce qui marche » (mamans, fondateur, école/émotion), 2 variantes (quiz, POV), 1 pari (carrousel ou présentation).

**Semaine du 16/11** (10 posts ; la période de test du style 1re vidéo commence vraiment cette semaine, puisque rien n'est sorti du 11 au 15/11) :
- Priorité : **reprogrammer les posts jamais publiés** (ils comptent dans le quota, ce ne sont pas des republications), dès que la limite Metricool est levée.
- Lun 16 : 10 h présentation « pourquoi LexyLab » (sombre, fondateur, 70 %) ; 18 h kinetic astuces devoirs mamans (thème sombre, 70 % mamans le soir, « à garder »).
- Mar 17 : présentation classique vs LexyLab (sombre, jamais vue).
- Mer 18 : 10 h carrousel 5 raisons (sombre, 10 % pari sauvegardes) ; 18 h `pres-examen-fiches` si ses voix sont prêtes, sinon kinetic mythes dyslexie.
- Jeu 19 : `pres-mail-travail` si voix, sinon demo notes de cours (étudiants).
  → Fait le 19/11 : 10 h `pres-mail-travail` (voix 6/6). Instagram en direct (file.json) ; TikTok via Metricool, toujours bloqué par la limite du compte.
- Ven 20 : 10 h quiz courses (20 % engagement) ; 18 h `pres-mamans-autonomie` si voix, sinon kinetic astuces relire.
  → Fait le 20/11 : 10 h quiz courses ; 18 h `pres-mamans-autonomie` (voix 6/6). Instagram en direct, TikTok via Metricool. Nouvelles idées style 1re vidéo pour la semaine prochaine (voix demandées) : `pres-memoire-etudiant`, `pres-messages-quotidien`.
- Sam 21 : `pres-enseignants-logopedes` si voix, sinon un carrousel sombre (étudiants ou logopèdes).
  → Fait le 21/11 : 10 h `pres-enseignants-logopedes` (voix 6/6). Instagram en direct, TikTok via Metricool (toujours bloqué par la limite du compte). Nouvelle idée style 1re vidéo : `pres-dictee-rouge` (émotion école, voix demandées).
- Dim 22 : 1 sketch maximum (rendu flat ou cartoon) ou demo Word devoir.
  → Fait le 22/11 : 10 h demo Word devoir (voix 6/6), pour casser la série de 3 présentations sombres et parce que la demo garde le meilleur temps de visionnage sur IG. Nouvelle idée en thème clair pour la semaine prochaine : `pres-job-etudiant` (voix demandées).
- Mamans : 2 posts (lun 18 h, ven 18 h), plafond de 3 respecté. Au moins 6 posts sur 10 en présentation ou carrousel sombre.
- Répartition : 7 « ce qui marche » (fondateur, mamans, école, produit en action), 2 variantes (quiz, mythes), 1 pari (carrousel).

**Semaine du 23/11** (10 posts, voix off sur toutes les vidéos ; fin de la période de test le 27/11, donc au moins 6 posts dans le style 1re vidéo, mais plus de produit en action et d'émotion école d'après les chiffres) :
- Lun 23 : 10 h `pres-dictee-rouge` (émotion école, sombre, 70 %) ; 18 h `pres-job-etudiant` (thème clair, 20 % variante).
- Mar 24 : `quiz-message` (engagement, 70 % : le quiz égale le meilleur score récent sur IG).
- Mer 25 : 10 h `pres-memoire-etudiant` (sombre) ; 18 h `pres-mamans-mot-prof` (mamans, sujet du meilleur temps IG) si ses voix sont prêtes, sinon `sketch-maman-devoirs`.
  → Fait le 25/11 : 10 h `pres-memoire-etudiant` (sombre) ; 18 h `pres-mamans-mot-prof` en thème clair (variété, test clair vs sombre chez les mamans). Voix 6/6. IG en direct, TikTok via Metricool (toujours bloqué par la limite du compte). Nouvelle idée pour sam/dim : `kin-pov-lire-voix-haute` (thème bleu, appel à commenter à l'écran, voix demandées).
- Jeu 26 : `pres-messages-quotidien` (sombre, produit en action).
- Ven 27 : 10 h carrousel sombre « à garder » (astuces relire ou repères pour enseignants, 10 % pari sauvegardes) ; 18 h `sketch-maman-devoirs` (1 sketch max, rendu flat ou cartoon, pas bâton).
- Sam 28 / Dim 29 : une demo (Gmail ou Word) et un kinetic POV école (nouvelles idées, voix à demander mercredi).
- Mamans : 2 posts (mer 18 h, ven 18 h). Répartition : 7 « ce qui marche » (émotion école, produit en action, quiz, mamans), 2 variantes (thème clair, carrousel), 1 pari (appel à commenter à l'écran).
