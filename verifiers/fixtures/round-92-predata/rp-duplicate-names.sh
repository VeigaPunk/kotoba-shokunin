#!/usr/bin/env bash
# rp-duplicate-names (round 92 pre-data): two same-named controls, both passing. Round-91
# ExecLadder F1 re-derived (`ladder-defect.md:56,113-117`): the gate accepts duplicate control
# names as valid spec and reads `freeze gate: 2 control(s) held`. Observes exit 0 at base.
set -u
LANE="$(cd "$(dirname "$0")/../../.." && pwd)"
out="$(cd "$LANE" && python3 -B verifiers/check_freeze_gate.py --plan verifiers/fixtures/round-92-predata/fp-duplicate-names.md 2>&1)"; rc=$?
echo "$out" | tail -2
if [ "$rc" = 0 ] && echo "$out" | grep -q 'control(s) held'; then echo "rp-dup duplicate control names accepted as valid spec (defect observable)"; exit 0; fi
echo "rp-dup: gate refused (rc=$rc) — the defect is not observable at these bytes"; exit 1
