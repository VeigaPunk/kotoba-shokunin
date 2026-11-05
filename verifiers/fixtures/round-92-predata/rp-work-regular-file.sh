#!/usr/bin/env bash
# rp-work-regular-file (round 92 pre-data): `--work` under a regular file. Round-91 ExecLadder F4
# re-derived (`ladder-defect.md:57,124-125`): the freeze gate dies on an uncaught
# NotADirectoryError (os.makedirs in run_control) instead of reading could-not-evaluate.
set -u
LANE="$(cd "$(dirname "$0")/../../.." && pwd)"
W="$(mktemp -d "${HYAKU_SCRATCH:-/fast/scratch/hyaku}/kotoba-r92/l1-predata/rp-work.XXXXXX")" || exit 1
trap 'rm -rf -- "$W"' EXIT
touch "$W/notadir"
out="$(cd "$LANE" && python3 -B verifiers/check_freeze_gate.py --plan verifiers/fixtures/round-92-predata/fp-minimal.md --work "$W/notadir/sub" 2>&1)"; rc=$?
echo "$out" | tail -3
if [ "$rc" != 0 ] && echo "$out" | grep -q 'NotADirectoryError'; then echo "rp-work crash observed (rc=$rc, uncaught NotADirectoryError)"; exit 0; fi
echo "rp-work: no crash observed (rc=$rc)"; exit 1
