#!/usr/bin/env bash
# c2-pinkey (round 93, claim C2, frozen counting command; plans/round-93.md § C2).
# Usage: bash verifiers/fixtures/round-93/c2-pinkey.sh [REV] [REPO]
#   REV  full commit to measure (default: the tip of branch master of REPO)
#   REPO repository to clone REV from (default: this lane; a scratch repo for the forgery control)
# Runs the public tip battery `verifiers/check_tip_battery.py --rev REV --repo <clone> --fleet <fleet>`
# three times from a scratch clone checked out at REV; only the INSTRUMENT_PINS dict of the RUNNING
# checker differs between runs (working-tree edit, never committed):
#   honest  : unmodified -> holds iff the output has `guard instrument-pin PASS` AND `guards 5 of 5`
#   keydrop : the "verifiers/check_correction_sweep.py" key removed from INSTRUMENT_PINS
#             -> holds iff a `FAIL guard instrument-pin:` line names verifiers/check_correction_sweep.py
#                AND the tally reads `guards 4 of 5`
#   keyswap : the same key removed AND a junk key "verifiers/r93-junk-key.py" added (the key count is
#             unchanged) -> holds iff a `FAIL guard instrument-pin:` line names
#             verifiers/check_correction_sweep.py AND the tally reads `guards 4 of 5`
# Predicate (frozen): C2-PREDICATE-MET iff all three hold. Exit 0 met, 1 unmet, 2 could-not-evaluate.
# The tip battery's own exit code is not read (the lane's carried corpus reds hold it at 1 in every
# world); only the guard lines and the frozen tally line are. Scratch under
# ${HYAKU_SCRATCH:-/fast/scratch/hyaku}/kotoba-r93/c2-pinkey, removed on exit.
set -u
LANE="$(cd "$(dirname "$0")/../../.." && pwd)"
REPO="${2:-$LANE}"
FLEET="$(cd "$LANE/.." && pwd)"
REV="$(git -C "$REPO" rev-parse --verify -q "${1:-$(git -C "$REPO" rev-parse master)}^{commit}")" \
  || { echo "C2-NOT-EVALUATED: REV is not a commit of $REPO"; exit 2; }
ROOT="${HYAKU_SCRATCH:-/fast/scratch/hyaku}/kotoba-r93/c2-pinkey"
mkdir -p "$ROOT" && W="$(mktemp -d "$ROOT/run.XXXX")" || { echo "C2-NOT-EVALUATED: scratch unavailable"; exit 2; }
trap 'rm -rf -- "$W"' EXIT
export TMPDIR="$W"
echo "rev $REV repo $REPO fleet $FLEET"

S="$W/world/kotoba-shokunin"
mkdir -p "$W/world"
git clone -q --shared "$REPO" "$S" && git -C "$S" checkout -q "$REV" \
  || { echo "C2-NOT-EVALUATED: clone or checkout failed"; exit 2; }
TB="$S/verifiers/check_tip_battery.py"
cp -- "$TB" "$W/tb.orig" || { echo "C2-NOT-EVALUATED: copy failed"; exit 2; }

edit_pins() {  # mode (keydrop|keyswap): edit the working-tree INSTRUMENT_PINS of $TB
  python3 -B - "$TB" "$1" <<'PY'
import ast, sys
path, mode = sys.argv[1], sys.argv[2]
src = open(path, encoding="utf-8").read()
lines = src.splitlines(keepends=True)
KEY = "verifiers/check_correction_sweep.py"
for node in ast.parse(src).body:
    if (isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "INSTRUMENT_PINS"
                                             for t in node.targets)):
        d = node.value
        break
else:
    raise SystemExit("INSTRUMENT_PINS absent")
for k, v in zip(d.keys, d.values):
    if isinstance(k, ast.Constant) and k.value == KEY:
        start, end = k.lineno, v.end_lineno
        break
else:
    raise SystemExit("key absent")
new = [] if mode == "keydrop" else ['    "verifiers/r93-junk-key.py": ("%s",),\n' % ("0" * 40)]
lines[start - 1:end] = new
out = "".join(lines)
pins = None
for node in ast.parse(out).body:
    if (isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "INSTRUMENT_PINS"
                                             for t in node.targets)):
        pins = ast.literal_eval(node.value)
assert pins is not None and KEY not in pins, "edit did not remove the key"
open(path, "w", encoding="utf-8").write(out)
print("%s: INSTRUMENT_PINS keys %d" % (mode, len(pins)))
PY
}

tip() {  # label -> sets OUT
  OUT="$(cd "$S" && python3 -B verifiers/check_tip_battery.py --rev "$REV" --repo "$S" --fleet "$FLEET" 2>&1)"; TRC=$?
  printf '%s\n' "$OUT" | grep -E '^(guard instrument-pin|FAIL guard instrument-pin)' | sed "s/^/  $1: /"
  printf '%s\n' "$OUT" | tail -1 | sed "s/^/  $1 last (tip rc $TRC): /"
}

tip honest
h_ok=no
printf '%s\n' "$OUT" | grep -qxF 'guard instrument-pin PASS' && printf '%s\n' "$OUT" | tail -1 | grep -qF 'guards 5 of 5' && h_ok=yes

hit() {  # -> yes iff the frozen keydrop/keyswap condition holds on $OUT
  if printf '%s\n' "$OUT" | grep -E '^FAIL guard instrument-pin:' | grep -qF 'verifiers/check_correction_sweep.py' \
     && printf '%s\n' "$OUT" | tail -1 | grep -qF 'guards 4 of 5'; then echo yes; else echo no; fi
}

edit_pins keydrop || { echo "C2-NOT-EVALUATED: keydrop edit failed"; exit 2; }
tip keydrop; k_ok=$(hit)
cp -- "$W/tb.orig" "$TB"
edit_pins keyswap || { echo "C2-NOT-EVALUATED: keyswap edit failed"; exit 2; }
tip keyswap; s_ok=$(hit)
cp -- "$W/tb.orig" "$TB"

echo "honest world: instrument-pin PASS and guards 5 of 5: $h_ok"
echo "keydrop world: check_correction_sweep.py named and guards 4 of 5: $k_ok"
echo "keyswap world: check_correction_sweep.py named and guards 4 of 5: $s_ok"
if [ "$h_ok$k_ok$s_ok" = yesyesyes ]; then echo "C2-PREDICATE-MET"; exit 0; fi
echo "C2-PREDICATE-UNMET"; exit 1
