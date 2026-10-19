#!/usr/bin/env bash
# usage: battery.sh <commit> <outdir> -- runs the gate battery in the canonical-layout clone
set -u
P=$(/tmp/kotoba-r46-meas/meas-tree.sh "$1"); O=$2; mkdir -p "$O"
export PYTHONDONTWRITEBYTECODE=1
run(){ n=$1; shift; s=$(date -u +%FT%TZ); ( cd "$P" 2>/dev/null; builtin cd "$P"; "$@" ) >"$O/$n.stdout" 2>"$O/$n.stderr"; e=$?; echo "$n exit=$e start=$s end=$(date -u +%FT%TZ) stdout_sha256=$(sha256sum <"$O/$n.stdout"|cut -c1-64)" | tee -a "$O/summary.txt"; }
echo "commit=$(git -C "$P" rev-parse HEAD) tree=$(git -C "$P" rev-parse 'HEAD^{tree}') path=$P" > "$O/summary.txt"
run checklist python3 -B verifiers/verify_skill_checklist.py --repo "$P" --skill "$P/SKILL.md"
run corpus-integrity python3 -B verifiers/verify_corpus_integrity.py
run corpus-independent python3 -B verifiers/verify_corpus_independent.py
run surfaces python3 -B verifiers/verify_surfaces.py
run pins python3 -B verifiers/check_substrate_pins.py
run floors python3 -B verifiers/check_assertion_floors.py --repo "$P"
