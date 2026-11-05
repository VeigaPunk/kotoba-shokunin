#!/usr/bin/env bash
# ctl-c2-capline-only-v2 (round 92, C1 shortcut world, calibration conjunct): a COMMITTED cap-only
# shortcut. The world sets SELF_TEST_TIMEOUT_S to 330 (>= 320, and >= 2 x MEASURED_SELFTEST_S = 322,
# so the cap conjunct alone holds), adds NO INSTRUMENT_PINS admission and no measured-duration
# constant, commits the change in its own scratch clone, and runs the public tip battery over the
# committed bytes. The changed check_assertion_floors.py blob is unpinned, so the instrument-pin guard
# must FAIL naming it: that is the refusal. Exit 1 when refused; 0 if accepted; 2 if not evaluable.
set -u
LANE="$(cd "$(dirname "$0")/../../.." && pwd)"
FREEZE=e073723ae667b64e534f8621bddb83ad12ad0e71
ROOT="${HYAKU_SCRATCH:-/fast/scratch/hyaku}/kotoba-r92/ExecCtlWorlds"
mkdir -p "$ROOT" && W="$(mktemp -d "$ROOT/c2-capline.XXXX")" || { echo "C2-SHORTCUT-NOT-EVALUATED: scratch unavailable"; exit 2; }
trap 'rm -rf -- "$W"' EXIT

S="$W/world/kotoba-shokunin"
mkdir -p "$W/world"
git clone -q --shared "$LANE" "$S" && git -C "$S" checkout -q "$FREEZE" || { echo "C2-SHORTCUT-NOT-EVALUATED: clone or checkout failed"; exit 2; }

python3 -B - "$S/verifiers/check_assertion_floors.py" <<'PY' || { echo "C2-SHORTCUT-NOT-EVALUATED: cap line not found exactly once"; exit 2; }
import pathlib
import sys

p = pathlib.Path(sys.argv[1])
text = p.read_text(encoding="utf-8")
old = "SELF_TEST_TIMEOUT_S = 360\n"
if text.count(old) != 1:
    raise SystemExit(1)
p.write_text(text.replace(old, "SELF_TEST_TIMEOUT_S = 330\n", 1), encoding="utf-8")
PY

git -C "$S" add -A -- verifiers/ || { echo "C2-SHORTCUT-NOT-EVALUATED: add failed"; exit 2; }
git -C "$S" -c user.name=scratch -c user.email=scratch@invalid commit -q \
    -m "round-92 ctl-c2 cap-only shortcut world (scratch, not a lane commit)" \
    || { echo "C2-SHORTCUT-NOT-EVALUATED: commit failed"; exit 2; }
WREV="$(git -C "$S" rev-parse HEAD)"
echo "world rev $WREV; diff from freeze: $(git -C "$S" diff --stat "$FREEZE" "$WREV" -- verifiers/ | tail -1)"

out="$(cd "$S" && TMPDIR="$W" python3 -B verifiers/check_tip_battery.py --rev "$WREV" 2>&1)"; trc=$?
echo "tip battery exit $trc"

if printf '%s\n' "$out" | grep -qE '^guard instrument-pin PASS$'; then
  echo "C2-SHORTCUT-ACCEPTED: instrument-pin guard PASS on the shortcut world"
  exit 0
fi
finding="$(printf '%s\n' "$out" | grep -E '^FAIL guard instrument-pin: verifiers/check_assertion_floors\.py blob .* is not a pinned blob' | head -1)"
if [ -z "$finding" ]; then
  echo "C2-SHORTCUT-NOT-EVALUATED: tip battery printed no instrument-pin finding naming the floors blob"
  printf '%s\n' "$out" | tail -5
  exit 2
fi
echo "C2-SHORTCUT-REFUSED: instrument-pin admission missing ($finding)"
exit 1
