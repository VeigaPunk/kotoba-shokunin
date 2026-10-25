#!/bin/sh
# apply.sh [parent-dir] -- build the fleet-shaped sandbox for THIS control world
# and apply its world.patch. Prints the world revision (a commit inside the
# sandbox clone; the lane and the fleet repo are never written).
#
#   parent-dir  default: a fresh mktemp -d /tmp/k72w1-world.XXXXXX
#               layout: <parent>/kotoba-shokunin + one symlink per fleet entry
set -eu
here=$(cd "$(dirname "$0")" && pwd)
BASE=c69711ee08279609374d895bb0f3c8c18ccf15c9
LANE=${LANE:-/home/vgpnk/Projects/shokunin/kotoba-shokunin}
FLEET=${FLEET:-/home/vgpnk/Projects/shokunin}
parent=${1:-$(mktemp -d /tmp/k72w1-world.XXXXXX)}
mkdir -p "$parent"
for e in "$FLEET"/* "$FLEET"/.[!.]*; do
  n=$(basename "$e")
  [ "$n" = kotoba-shokunin ] && continue
  [ -e "$parent/$n" ] || ln -s "$e" "$parent/$n"
done
clone=$parent/kotoba-shokunin
[ -d "$clone" ] || git clone --shared -q "$LANE" "$clone"
git -C "$clone" checkout -q "$BASE"
[ "$(git -C "$clone" rev-parse --show-toplevel)" = "$clone" ] || {
  echo "sandbox toplevel is not $clone" >&2; exit 9; }
git -C "$clone" apply --index "$here/world.patch"
git -C "$clone" -c user.name=control -c user.email=control@k72.invalid \
    -c commit.gpgsign=false commit -q -m "control world: $(basename "$here")"
echo "rev $(git -C "$clone" rev-parse HEAD)"
echo "tree $(git -C "$clone" rev-parse HEAD^{tree})"
