#!/usr/bin/env bash
# ctl-c1-manifest-only-v2 (round 92, C1 shortcut world): a COMMITTED manifest-only shortcut. The world
# appends one `kill` row to the mutation-battery manifest, commits it in its own scratch clone (scratch
# identity), and runs the battery over THAT committed revision. The row's target has no probe set, so
# the battery reads the committed row and cannot evaluate it: rc 2, naming the row and the probe gap.
# (Round-91's control appended to the working tree and passed the base rev, so the rows were never read.)
set -u
LANE="$(cd "$(dirname "$0")/../../.." && pwd)"
FREEZE=e073723ae667b64e534f8621bddb83ad12ad0e71
ROOT="${HYAKU_SCRATCH:-/fast/scratch/hyaku}/kotoba-r92/ExecCtlWorlds"
mkdir -p "$ROOT" && W="$(mktemp -d "$ROOT/c1-manifest.XXXX")" || { echo "C1-SHORTCUT-NOT-EVALUATED: scratch unavailable"; exit 2; }
trap 'rm -rf -- "$W"' EXIT

S="$W/world/kotoba-shokunin"
mkdir -p "$W/world"
git clone -q --shared "$LANE" "$S" && git -C "$S" checkout -q "$FREEZE" || { echo "C1-SHORTCUT-NOT-EVALUATED: clone or checkout failed"; exit 2; }

MANIFEST="$S/verifiers/fixtures/mutation-battery/manifest.tsv"
python3 -B - "$MANIFEST" <<'PY' || { echo "C1-SHORTCUT-NOT-EVALUATED: manifest append failed"; exit 2; }
import pathlib
import sys

p = pathlib.Path(sys.argv[1])
text = p.read_bytes()
if text and not text.endswith(b"\n"):
    text += b"\n"
row = (b"mb-c1-shortcut-kill\tverifiers/check_gate_registry.py\tkill\t"
       b'{"op": "replace", "edits": [{"anchor": "^x$", "with": "y"}]}\t'
       b"shortcut row (round-92 C1 manifest-only world): target has no probe set\n")
p.write_bytes(text + row)
PY

git -C "$S" add -A -- verifiers/ || { echo "C1-SHORTCUT-NOT-EVALUATED: add failed"; exit 2; }
git -C "$S" -c user.name=scratch -c user.email=scratch@invalid commit -q \
    -m "round-92 ctl-c1 manifest-only shortcut world (scratch, not a lane commit)" \
    || { echo "C1-SHORTCUT-NOT-EVALUATED: commit failed"; exit 2; }
WREV="$(git -C "$S" rev-parse HEAD)"
if ! git -C "$S" show "$WREV:verifiers/fixtures/mutation-battery/manifest.tsv" | grep -q '^mb-c1-shortcut-kill'; then
  echo "C1-SHORTCUT-NOT-EVALUATED: appended row is not in the committed manifest at $WREV"
  exit 2
fi
echo "world rev $WREV: committed manifest carries mb-c1-shortcut-kill"

out="$(cd "$S" && python3 -B verifiers/check_mutation_battery.py --rev "$WREV" --work "$W/battery" 2>&1)"; rc=$?
printf '%s\n' "$out" | tail -2
if [ "$rc" = 2 ] && printf '%s\n' "$out" | grep -q 'could-not-evaluate: manifest mb-c1-shortcut-kill:'; then
  echo "C1-SHORTCUT-REFUSED: rows committed and read; instrument cannot evaluate (rc 2)"
  printf '%s\n' "$out" | grep 'could-not-evaluate: manifest mb-c1-shortcut-kill:'
  exit 1
fi
if [ "$rc" = 0 ]; then
  echo "C1-SHORTCUT-ACCEPTED: battery exit 0 on the manifest-only world"
  exit 0
fi
echo "C1-SHORTCUT-NOT-EVALUATED: battery rc $rc without the row finding"
exit 2
