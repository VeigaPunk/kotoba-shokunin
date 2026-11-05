#!/bin/sh
set -u
L=/home/vgpnk/Projects/shokunin/kotoba-shokunin
S=/fast/scratch/hyaku/kotoba-r87/l1
mkdir -p "$S"; export TMPDIR="$S"
OUT="$L/.ufo/waves/round-87/receipts/after-battery.txt"
: > "$OUT"
TIP=$(git -C "$L" rev-parse master)
printf 'tip %s\nhost %s\n' "$TIP" "$(uname -sr)" >> "$OUT"
run() { name=$1; shift; printf -- '--- %s\n' "$name" >> "$OUT"; ( cd "$L" && timeout 1800 "$@" ) >> "$OUT" 2>&1; rc=$?; printf 'exit=%s\n' "$rc" >> "$OUT"; }
run corpus_integrity python3 -B verifiers/verify_corpus_integrity.py
run corpus_independent python3 -B verifiers/verify_corpus_independent.py
run skill_checklist python3 -B verifiers/verify_skill_checklist.py
run gate_registry python3 -B verifiers/check_gate_registry.py --rev "$TIP"
run assertion_floors python3 -B verifiers/check_assertion_floors.py
run census bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba
run skill_lines wc -l SKILL.md
run skill_bytes wc -c SKILL.md
run c1_root_semantics python3 -B verifiers/check_omp_root_semantics.py --rev "$TIP"
run c2_routed_repairs python3 -B verifiers/check_r86_routed_repairs.py --rev "$TIP"
run c1_selftest python3 -B verifiers/check_omp_root_semantics.py --self-test
run c2_selftest python3 -B verifiers/check_r86_routed_repairs.py --self-test
echo done
