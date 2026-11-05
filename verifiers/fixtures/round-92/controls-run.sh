#!/usr/bin/env bash
# controls-run (round 92): the frozen counting command for the C1 controls. Runs the four scripts in
# order, each exactly once, capturing rc and stdout. Stdout is the exact counting line and exit 0 iff
# both shortcut worlds exit 1 naming their missing conjunct AND both honest worlds exit 0. Any other
# combination prints the observed per-script lines to stdout and exits 1. Per-script stdout and rc
# are always written to stderr as the receipt.
set -u
D="$(cd "$(dirname "$0")" && pwd)"

LABELS=(); RCS=(); MET=()
step() {  # label script want_rc named_stdout_line
  local label="$1" script="$2" want="$3" named="$4" out rc met=no
  out="$(bash "$D/$script" 2>&1)"; rc=$?
  if [ "$rc" = "$want" ] && printf '%s\n' "$out" | grep -qF -- "$named"; then met=yes; fi
  printf -- '----- %s (%s) rc=%s met=%s\n%s\n' "$label" "$script" "$rc" "$met" "$out" >&2
  LABELS+=("$label"); RCS+=("$rc"); MET+=("$met")
}

step C2-shortcut ctl-c2-capline-only-v2.sh 1 "C2-SHORTCUT-REFUSED: instrument-pin admission missing"
step C2-honest   ctl-c2-honest.sh            0 "C2-PREDICATE-MET"
step C1-shortcut ctl-c1-manifest-only-v2.sh  1 "C1-SHORTCUT-REFUSED: rows committed and read; instrument cannot evaluate (rc 2)"
step C1-honest   ctl-c1-honest.sh            0 "C1-PREDICATE-MET"

refused=0; honest=0
[ "${MET[0]}" = yes ] && refused=$((refused + 1))
[ "${MET[2]}" = yes ] && refused=$((refused + 1))
[ "${MET[1]}" = yes ] && honest=$((honest + 1))
[ "${MET[3]}" = yes ] && honest=$((honest + 1))

if [ "$refused" = 2 ] && [ "$honest" = 2 ]; then
  echo "round-92 controls: shortcuts refused 2 of 2; honest held 2 of 2"
  exit 0
fi
for i in 0 1 2 3; do
  echo "${LABELS[$i]} rc=${RCS[$i]} met=${MET[$i]}"
done
echo "observed: shortcuts refused $refused of 2; honest held $honest of 2"
exit 1
