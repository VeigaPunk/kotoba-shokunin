#!/usr/bin/env bash
# rp-exit127 (round 92 pre-data): a control that actually exits 127 and DECLARES `exit 127`.
# Round-91 A3/ExecLadder F2: the harness intercepts 126/127 as could-not-evaluate, so the declared
# 127 is never compared — the declaration is unobservable through the gate.
set -u
LANE="$(cd "$(dirname "$0")/../../.." && pwd)"
out="$(cd "$LANE" && python3 -B verifiers/check_freeze_gate.py --plan verifiers/fixtures/round-92-predata/fp-exit127.md 2>&1)"; rc=$?
echo "$out" | tail -2
if [ "$rc" = 2 ] && echo "$out" | grep -q 'one27'; then echo "rp-127 declared exit 127 never compared (could-not-evaluate rung intercepted; defect observable)"; exit 0; fi
echo "rp-127: unexpected reading (rc=$rc)"; exit 1
