#!/usr/bin/env bash
# ctl-c2-honest (round 92, C1 honest world, calibration conjunct): at $1 (default: the lane tip) the
# committed bytes carry (a) SELF_TEST_TIMEOUT_S >= 2 x MEASURED_SELFTEST_S, (b) an INSTRUMENT_PINS
# admission for the check_assertion_floors.py blob at that revision, and (c) the public tip battery's
# instrument-pin guard reading PASS. Every reading is taken from `git show <rev>:<path>`, never the
# working tree. Exit 0 prints C2-PREDICATE-MET; 1 prints the unmet conjunct; 2 cannot evaluate.
set -u
LANE="$(cd "$(dirname "$0")/../../.." && pwd)"
ROOT="${HYAKU_SCRATCH:-/fast/scratch/hyaku}/kotoba-r92/ExecCtlWorlds"
mkdir -p "$ROOT" && W="$(mktemp -d "$ROOT/c2-honest.XXXX")" || { echo "C2-PREDICATE-UNMET: scratch unavailable"; exit 2; }
trap 'rm -rf -- "$W"' EXIT

REV="$(git -C "$LANE" rev-parse --verify -q "${1:-$(git -C "$LANE" rev-parse HEAD)}^{commit}")" \
  || { echo "C2-PREDICATE-UNMET: argument is not a commit of the lane"; exit 2; }
echo "rev $REV"

python3 -B - "$LANE" "$REV" <<'PY'
import ast
import subprocess
import sys

lane, rev = sys.argv[1], sys.argv[2]


def show(path):
    return subprocess.run(["git", "-C", lane, "show", rev + ":" + path],
                          capture_output=True, text=True, check=True).stdout


def const(src, name):
    for node in ast.parse(src).body:
        if isinstance(node, ast.Assign) and any(
                isinstance(t, ast.Name) and t.id == name for t in node.targets):
            return ast.literal_eval(node.value)
    raise SystemExit("constant %s absent at %s" % (name, rev))


floors_src = show("verifiers/check_assertion_floors.py")
cap = const(floors_src, "SELF_TEST_TIMEOUT_S")
measured = const(floors_src, "MEASURED_SELFTEST_S")
pins = const(show("verifiers/check_tip_battery.py"), "INSTRUMENT_PINS")
blob = subprocess.run(["git", "-C", lane, "rev-parse", rev + ":verifiers/check_assertion_floors.py"],
                      capture_output=True, text=True, check=True).stdout.strip()
admitted = blob in pins.get("verifiers/check_assertion_floors.py", ())
print("cap conjunct: SELF_TEST_TIMEOUT_S %s >= 2 x MEASURED_SELFTEST_S %s: %s"
      % (cap, measured, cap >= 2 * measured))
print("admission conjunct: floors blob %s in INSTRUMENT_PINS: %s" % (blob, admitted))
raise SystemExit(0 if (cap >= 2 * measured and admitted) else 1)
PY
conj=$?

out="$(cd "$LANE" && TMPDIR="$W" python3 -B verifiers/check_tip_battery.py --rev "$REV" 2>&1)"; trc=$?
echo "tip battery exit $trc (red corpus gates carry from base; only the pin guard is read here)"
printf '%s\n' "$out" | grep -E '^(guard instrument-pin|FAIL guard instrument-pin)' || true
pin=1
printf '%s\n' "$out" | grep -qE '^guard instrument-pin PASS$' && pin=0

if [ "$conj" = 0 ] && [ "$pin" = 0 ]; then
  echo "C2-PREDICATE-MET"
  exit 0
fi
echo "C2-PREDICATE-UNMET: cap+admission conjunct rc=$conj; tip battery pin guard unread-or-failing rc=$pin"
exit 1
