#!/bin/sh
# round-87 base no-harm battery: captures each command's own exit status (Q65).
set -u
L=/home/vgpnk/Projects/shokunin/kotoba-shokunin
BASE=223ae62424f8ab1eb365d733eb648d6228ddd7e8
S=/fast/scratch/hyaku/kotoba-r87/l1
mkdir -p "$S"; export TMPDIR="$S"
OUT="$L/.ufo/waves/round-87/receipts/base-battery.txt"
: > "$OUT"
printf 'base %s\nhost %s\n' "$BASE" "$(uname -sr)" >> "$OUT"
run() {
  name=$1; shift
  printf -- '--- %s\n' "$name" >> "$OUT"
  ( cd "$L" && timeout 1200 "$@" ) >> "$OUT" 2>&1
  rc=$?
  printf 'exit=%s\n' "$rc" >> "$OUT"
}
run corpus_integrity python3 -B verifiers/verify_corpus_integrity.py
run corpus_independent python3 -B verifiers/verify_corpus_independent.py --json
run skill_checklist python3 -B verifiers/verify_skill_checklist.py
run gate_registry python3 -B verifiers/check_gate_registry.py --rev "$BASE"
run assertion_floors python3 -B verifiers/check_assertion_floors.py
run census bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba
run skill_lines wc -l SKILL.md
run skill_bytes wc -c SKILL.md
run q73_sweep grep -n 'differs from the base\|byte-identical' verifiers/check_tip_battery.py verifiers/check_province_core.py
echo done
