#!/bin/sh
# replay.sh -- round-72 C2 shortcut control world 3b (COMPOSITE: world 3's stub
# at the pinned opencode path, its sha pinned, PLUS world 2's ledger of every
# opencode class). Not one of the four worlds the plan names; it exists because
# worlds 2 and 3 each defeat only one conjunct of the frozen predicate and the
# plan's kill rule is about a shortcut world reading exit 0 -- 3b is the world
# that would read exit 0 if the surfaces target were lowered to 5 (plan Q45).
# Rebuilds on a fresh --shared clone of the base c69711e inside a fleet-shaped
# sandbox, commits the overlay inside that clone, then runs the two existing
# instruments at their own default paths (no path flags) and records their exit
# codes and JSON. Every git write happens inside $P/kotoba-shokunin.
#
# The one world-specific step: the overlay's two path constants carry the
# literal placeholder __CLONE__, substituted here with this clone's absolute
# path so the stub at verifiers/fixtures/opencode-stub.bin is what both
# instruments read.
set -eu
L=/home/vgpnk/Projects/shokunin/kotoba-shokunin
BASE=c69711ee08279609374d895bb0f3c8c18ccf15c9
HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
P=$(mktemp -d /tmp/k72fleet-replay-w3b.XXXXXX)
cleanup() { [ "${KEEP:-0}" = 1 ] || rm -rf "$P"; }
trap cleanup EXIT INT TERM
for e in /home/vgpnk/Projects/shokunin/*; do
  n=$(basename "$e"); [ "$n" = kotoba-shokunin ] && continue
  ln -s "$e" "$P/$n"
done
git clone --shared -q "$L" "$P/kotoba-shokunin"
C=$P/kotoba-shokunin
git -C "$C" checkout -q --detach "$BASE"
[ "$(git -C "$C" rev-parse --show-toplevel)" = "$C" ] || { echo "not the clone toplevel" >&2; exit 1; }
git -C "$C" config user.name "round-72 C2 shortcut control"
git -C "$C" config user.email "control@example.invalid"
cp -R "$HERE/overlay/." "$C/"
for f in "$C/verifiers/check_substrate_pins.py" "$C/verifiers/verify_surfaces.py"; do
  sed -i "s|__CLONE__|$C|g" "$f"
done
grep -c "__CLONE__" "$C/verifiers/check_substrate_pins.py" "$C/verifiers/verify_surfaces.py" || true
git -C "$C" add -A
git -C "$C" commit -q -m "w3b-stub-full-ledger: overlay on base $BASE (shortcut control)"
echo "world commit: $(git -C "$C" rev-parse HEAD)"
cd "$C"
set +e
python3 -B verifiers/check_substrate_pins.py --json > "$HERE/observed-pins.json" 2>&1
echo "check_substrate_pins.py exit=$?"
python3 -B verifiers/verify_surfaces.py --json > "$HERE/observed-surfaces.json" 2>&1
echo "verify_surfaces.py exit=$?"
if [ -f "$L/verifiers/check_substrate_repin_v2.py" ]; then
  python3 -B "$L/verifiers/check_substrate_repin_v2.py" \
    --rev "$(git -C "$C" rev-parse HEAD)" --repo "$C" \
    > "$HERE/observed-counter.txt" 2>&1
  echo "check_substrate_repin_v2.py exit=$?"
else
  echo "check_substrate_repin_v2.py absent in the lane; counter not run"
fi
set -e
if [ "${KEEP:-0}" = 1 ]; then echo "sandbox kept at $P"; fi
