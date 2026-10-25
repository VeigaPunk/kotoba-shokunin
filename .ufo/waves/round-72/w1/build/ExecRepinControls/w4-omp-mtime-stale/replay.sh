#!/bin/sh
# replay.sh -- round-72 C2 shortcut control world 4 (omp.real pinned, but
# omp_binary_mtime left at the round-47 value). Rebuilds this world on a fresh
# --shared clone of the base c69711e inside a fleet-shaped sandbox, commits the
# overlay inside that clone, then runs the two existing instruments at their own
# default paths (no path flags) and records their exit codes and JSON. Every git
# write happens inside $P/kotoba-shokunin.
set -eu
L=/home/vgpnk/Projects/shokunin/kotoba-shokunin
BASE=c69711ee08279609374d895bb0f3c8c18ccf15c9
HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
P=$(mktemp -d /tmp/k72fleet-replay-w4.XXXXXX)
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
git -C "$C" add -A
git -C "$C" commit -q -m "w4-omp-mtime-stale: overlay on base $BASE (shortcut control)"
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
