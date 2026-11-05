#!/usr/bin/env bash
# ctl-c1-manifest-only (round 91): a shortcut world that adds the three guard kill rows to the
# manifest but leaves the battery instrument at base. The manifest then names a target with no probe
# set, so the instrument cannot evaluate (exit 2) and the predicate is unmet.
set -u
LANE="$(cd "$(dirname "$0")/../../.." && pwd)"
ROOT="${HYAKU_SCRATCH:-/fast/scratch/hyaku}/kotoba-r91/ctl-c1-manifest-only"
mkdir -p "$ROOT" && W="$(mktemp -d "$ROOT/w.XXXX")" || { echo "C1-PREDICATE-UNMET: scratch unavailable"; exit 1; }
trap 'rm -rf -- "$W"' EXIT
S="$W/lane"; git clone -q --shared "$LANE" "$S" && git -C "$S" checkout -q 9264baaa823cdae3d009a4004e014639551e016f || { echo "C1-PREDICATE-UNMET: clone failed"; exit 1; }
printf '%s\tverifiers/check_mutation_battery.py\tkill\t{"op": "replace", "edits": []}\tshortcut row\n' >> "$S/verifiers/fixtures/mutation-battery/manifest.tsv"
out="$(cd "$S" && TMPDIR="$W" python3 -B verifiers/check_mutation_battery.py --rev "$(git -C "$S" rev-parse HEAD)" --work "$W" 2>&1)"; rc=$?
echo "$out" | tail -2
if [ "$rc" = 0 ] && echo "$out" | grep -q 'killed 17 of 17'; then echo "C1-PREDICATE-MET"; exit 0; fi
echo "C1-PREDICATE-UNMET"; exit 1
