#!/bin/bash
# Fabrique les voix off de l'agent LexyLab avec les voix françaises du Mac, puis les envoie sur GitHub.
# Lancé automatiquement par macOS (LaunchAgent eu.lexylab.voix) à 12h30 et 19h45.
# Choisit toujours la voix la PLUS NATURELLE installée : (Premium) > (Enhanced/Améliorée) > voix de base.
# Si une meilleure voix est installée plus tard, les anciennes voix sont refaites automatiquement.
set -e
cd "$(dirname "$0")/../.."
git pull -q --rebase origin main
LISTE=$(say -v '?')

meilleure() {  # $1 = liste de prénoms par ordre de préférence ; renvoie le nom exact de la meilleure voix fr installée
  for qual in "Premium" "premium" "Enhanced" "de qualité" "Améliorée" "Amélioré" ""; do
    for nom in $1; do
      ligne=$(echo "$LISTE" | grep -E "^$nom" | grep -E "fr_(FR|BE|CA|CH)" | { if [ -n "$qual" ]; then grep "($qual)"; else grep -v "("; fi; } | head -1)
      if [ -n "$ligne" ]; then echo "$ligne" | sed -E 's/ +fr_.*$//' | sed -E 's/ +$//'; return; fi
    done
  done
}
# Choix de Paolo (9/11) : voix PRINCIPALE = Aurélie (premium), partout.
# Voix SECONDE (seulement pour le 2e personnage des dialogues) = Audrey (premium).
PRINCIPALE=$(meilleure "Aurélie Audrey Amélie")
SECONDE=$(meilleure "Audrey Amélie Marie")
[ "$SECONDE" = "$PRINCIPALE" ] && SECONDE=$(meilleure "Audrey")
[ -z "$PRINCIPALE" ] && PRINCIPALE=$(echo "$LISTE" | grep -E "fr_FR" | head -1 | sed -E 's/ +fr_.*$//')
[ -z "$SECONDE" ] && SECONDE="$PRINCIPALE"
HOMME="$PRINCIPALE"; FEMME="$SECONDE"
echo "Voix principale : $PRINCIPALE | Voix seconde : $SECONDE"

MANIF="agent-video/voix/voix-utilisees.txt"; touch "$MANIF"
n=0
while IFS='|' read -r fichier texte voixligne; do
  [ -z "$fichier" ] && continue
  case "$fichier" in \#*) continue;; esac
  texte="${texte%%|*}"   # sécurité : ne jamais lire le nom de la voix à voix haute
  v="$PRINCIPALE"; case "$voixligne" in seconde|Seconde) v="$SECONDE";; esac
  cible="agent-video/$fichier"
  deja=$(grep -F "$fichier|" "$MANIF" | tail -1 | cut -d'|' -f2)
  # refaire si : fichier absent, ou fabriqué avec une autre voix, ou ancien fichier sans trace (avant le 9/11)
  if [ ! -f "$cible" ] || [ "$deja" != "$v" ]; then
    mkdir -p "$(dirname "$cible")"
    # petites pauses naturelles après les points et virgules
    t2=$(echo "$texte" | sed -E 's/([.!?…]) /\1 [[slnc 250]] /g; s/, /, [[slnc 120]] /g')
    say -v "$v" -o /tmp/lexy_voix.aiff "$t2"
    afconvert -f m4af -d aac /tmp/lexy_voix.aiff "$cible"
    grep -vF "$fichier|" "$MANIF" > "$MANIF.tmp" || true; mv "$MANIF.tmp" "$MANIF"; echo "$fichier|$v" >> "$MANIF"
    echo "  ✓ $fichier ($v)"
    n=$((n+1))
  fi
done < agent-video/voix/a-generer.txt
if [ $n -gt 0 ]; then
  git add agent-video/voix
  git commit -q -m "Voix off : $n voix (Mac)"
  git push -q origin HEAD
  echo "$n voix envoyées à l'agent."
else
  echo "Rien de nouveau à fabriquer."
fi
