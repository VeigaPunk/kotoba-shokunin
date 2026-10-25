#!/bin/sh
# run6.sh <clone-dir> <rev> <outdir> -- the six frozen C3 battery commands.
# Each command capped at 300 s; exit code and wall time recorded per gate.
set -u
clone=$1; rev=$2; out=$3
mkdir -p "$out"
cd "$clone" || exit 9
run() {
  name=$1; shift
  start=$(date +%s)
  timeout 300 "$@" > "$out/$name.out" 2> "$out/$name.err"
  code=$?
  end=$(date +%s)
  printf '%s exit=%s wall=%ss\n' "$name" "$code" "$((end - start))" >> "$out/summary.txt"
}
: > "$out/summary.txt"
run check_gate_registry   python3 -B verifiers/check_gate_registry.py --rev "$rev"
run check_assertion_floors python3 -B verifiers/check_assertion_floors.py
run verify_skill_checklist python3 -B verifiers/verify_skill_checklist.py
run verify_corpus_integrity python3 -B verifiers/verify_corpus_integrity.py
run verify_corpus_independent python3 -B verifiers/verify_corpus_independent.py
run check_correction_sweep python3 -B verifiers/check_correction_sweep.py --root .
cat "$out/summary.txt"
