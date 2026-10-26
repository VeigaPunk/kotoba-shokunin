#!/bin/sh
# apply.sh [parent-dir] -- build a fleet-shaped sandbox of the round-73 base
# (072048fa8e8a52c707d25f7079772fa317244eb7) and apply THIS control world's
# world.patch inside it. Prints the world revision and tree.
#
# The lane and the fleet repo are never written: every git write happens inside
# the sandbox clone. The parent also gets one symlink per fleet-root entry, so
# the lane gates that read `../` fleet-root paths resolve (a bare /tmp clone
# cannot run them).
#
#   parent-dir  default: a fresh mktemp -d /tmp/k73w1-world.XXXXXX
#               layout: <parent>/kotoba-shokunin + one symlink per fleet entry
set -eu
here=$(cd "$(dirname "$0")" && pwd)
BASE=072048fa8e8a52c707d25f7079772fa317244eb7
LANE=${LANE:-/home/vgpnk/Projects/shokunin/kotoba-shokunin}
FLEET=${FLEET:-/home/vgpnk/Projects/shokunin}
parent=${1:-$(mktemp -d /tmp/k73w1-world.XXXXXX)}
mkdir -p "$parent"
for e in "$FLEET"/* "$FLEET"/.[!.]*; do
  n=$(basename "$e")
  [ "$n" = kotoba-shokunin ] && continue
  [ -e "$parent/$n" ] || ln -s "$e" "$parent/$n"
done
clone=$parent/kotoba-shokunin
[ -d "$clone" ] || git clone --shared -q --no-checkout "$LANE" "$clone"
git -C "$clone" checkout -q "$BASE"
[ "$(git -C "$clone" rev-parse --show-toplevel)" = "$clone" ] || {
  echo "sandbox toplevel is not $clone" >&2; exit 9; }
git -C "$clone" apply --index "$here/world.patch"
git -C "$clone" -c user.name=control -c user.email=control@k73.invalid \
    -c commit.gpgsign=false commit -q -m "control world: $(basename "$here")"
echo "rev $(git -C "$clone" rev-parse HEAD)"
echo "tree $(git -C "$clone" rev-parse HEAD^{tree})"
