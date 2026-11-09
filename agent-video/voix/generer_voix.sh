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
  for qual in "Premium" "Enhanced" "Améliorée" "Amélioré" ""; do
    for nom in $1; do
      ligne=$(echo "$LISTE" | grep -E "^$nom" | grep -E "fr_(FR|BE|CA|CH)" | { if [ -n "$qual" ]; then grep "($qual)"; else grep -v "("; fi; } | head -1)
      if [ -n "$ligne" ]; then echo "$ligne" | sed -E 's/ +fr_.*$//' | sed -E 's/ +$//'; return; fi
    done
  done
}
# Voix féminine : Audrey (la plus naturelle, haute qualité) puis Aurélie
FEMME=$(meilleure "Audrey Aurélie Amélie Marie Céline")
# Voix « homme » : une voix masculine améliorée si elle existe ; sinon on préfère une voix NATURELLE (Aurélie)
# à un Thomas robotique (demande de Paolo : la voix la moins robotique possible).
HOMME=$(echo "$LISTE" | grep -E "^(Thomas|Jacques|Daniel|Nicolas) \((Premium|Enhanced|Améliorée|Amélioré)\)" | grep fr_ | head -1 | sed -E 's/ +fr_.*$//')
if [ -z "$HOMME" ]; then
  for nom in "Aurélie" "Audrey"; do
    if echo "$LISTE" | grep -E "^$nom( |\()" | grep -q fr_ && [ "$(echo "$LISTE" | grep -E "^$nom" | head -1 | sed -E 's/ +fr_.*$//')" != "$FEMME" ]; then
      HOMME=$(echo "$LISTE" | grep -E "^$nom" | head -1 | sed -E 's/ +fr_.*$//'); break; fi
  done
fi
[ -z "$HOMME" ] && HOMME=$(meilleure "Thomas")
[ -z "$HOMME" ] && HOMME=$(echo "$LISTE" | grep -E "fr_FR" | head -1 | sed -E 's/ +fr_.*$//')
[ -z "$FEMME" ] && FEMME="$HOMME"
echo "Voix homme : $HOMME | Voix femme : $FEMME"

MANIF="agent-video/voix/voix-utilisees.txt"; touch "$MANIF"
n=0
while IFS='|' read -r fichier texte voixligne; do
  [ -z "$fichier" ] && continue
  case "$fichier" in \#*) continue;; esac
  texte="${texte%%|*}"   # sécurité : ne jamais lire le nom de la voix à voix haute
  v="$HOMME"; case "$voixligne" in Am*|am*|Au*|femme|Femme) v="$FEMME";; esac
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
  git commit -q -m "Voix off : $n voix (Mac : $HOMME / $FEMME)"
  git push -q origin HEAD
  echo "$n voix envoyées à l'agent."
else
  echo "Rien de nouveau à fabriquer."
fi
