#!/bin/bash
# Fabrique les voix off de l'agent LexyLab avec la voix française du Mac, puis les envoie sur GitHub.
# À lancer sur le Mac de Paolo :  bash agent-video/voix/generer_voix.sh   (depuis le dossier lexylab-telechargement)
set -e
cd "$(dirname "$0")/../.."
git pull -q --rebase origin main
VOIX="${VOIX_MAC:-Thomas}"
if ! say -v '?' | grep -q "^$VOIX "; then
  VOIX=$(say -v '?' | grep -E "fr_FR|fr_BE" | head -1 | awk '{print $1}')
fi
echo "Voix utilisée : $VOIX"
n=0
FEMME="${VOIX_FEMME:-Amélie}"
if ! say -v '?' | grep -q "^$FEMME "; then
  FEMME=$(say -v '?' | grep -E "fr_FR|fr_BE|fr_CA" | grep -v "^$VOIX " | head -1 | awk '{print $1}')
  [ -z "$FEMME" ] && FEMME="$VOIX"
fi
while IFS='|' read -r fichier texte voixligne; do
  [ -z "$fichier" ] && continue
  case "$fichier" in \#*) continue;; esac
  cible="agent-video/$fichier"
  if [ ! -f "$cible" ]; then
    mkdir -p "$(dirname "$cible")"
    v="$VOIX"
    case "$voixligne" in Am*|am*|femme|Femme) v="$FEMME";; esac
    say -v "$v" -r 175 -o /tmp/lexy_voix.aiff "$texte"
    afconvert -f m4af -d aac /tmp/lexy_voix.aiff "$cible"
    echo "  ✓ $fichier"
    n=$((n+1))
  fi
done < agent-video/voix/a-generer.txt
if [ $n -gt 0 ]; then
  git add agent-video/voix
  git commit -q -m "Voix off : $n nouvelle(s) voix (Mac, $VOIX)"
  git push -q origin HEAD
  echo "$n voix envoyées à l'agent. Merci !"
else
  echo "Rien de nouveau à fabriquer."
fi
