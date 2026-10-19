#!/usr/bin/env bash
# usage: meas-tree.sh <commit>  -> prints path of a canonical-layout clone at <commit>
# Builds /tmp/kotoba-r46-meas/<commit>/ whose entries symlink to the fleet root (read-only),
# with kotoba-shokunin/ a shared clone checked out at <commit>, so '../X' citations resolve
# exactly as in the canonical lane checkout. Writes nothing outside /tmp.
set -euo pipefail
FLEET=/home/vgpnk/Projects/shokunin
WT=$FLEET/.tower/worktrees/kaika/kotoba-shokunin
C=$(git -C "$WT" rev-parse "$1")
D=/tmp/kotoba-r46-meas/$C
if [ ! -d "$D/kotoba-shokunin" ]; then
  mkdir -p "$D"
  for e in "$FLEET"/* "$FLEET"/.ufo "$FLEET"/.git; do
    b=$(basename "$e"); [ "$b" = kotoba-shokunin ] && continue
    ln -sfn "$e" "$D/$b"
  done
  git clone -q --shared --no-checkout "$WT" "$D/kotoba-shokunin"
  git -C "$D/kotoba-shokunin" -c advice.detachedHead=false checkout -q "$C"
fi
echo "$D/kotoba-shokunin"
