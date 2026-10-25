#!/usr/bin/env bash
# replay.sh — rebuild one control world in a throwaway --shared clone and score it.
#
#   bash replay.sh honest
#   bash replay.sh w9-token-list
#
# The lane itself is only read (`git clone --shared`); every write happens inside the clone under
# /tmp, whose toplevel is asserted before the first commit.  The score comes from
# oracle_author_rules_literal.py — this seat's literal reading of the frozen predicate, NOT the
# lane counter (`verifiers/check_author_rules.py` did not exist when these worlds were built).
set -euo pipefail

world=${1:?usage: replay.sh <world>}
here=$(cd "$(dirname "$0")" && pwd)
lane=${LANE:-/home/vgpnk/Projects/shokunin/kotoba-shokunin}
base=${BASE:-c69711ee08279609374d895bb0f3c8c18ccf15c9}

D=$(mktemp -d /tmp/k72w1-ExecAuthorControls.replay.XXXXXX)
git clone --shared -q "$lane" "$D/kotoba-shokunin"
git -C "$D/kotoba-shokunin" checkout -q "$base"

top=$(git -C "$D/kotoba-shokunin" rev-parse --show-toplevel)
[ "$top" = "$D/kotoba-shokunin" ] || { echo "refusing: toplevel $top != $D/kotoba-shokunin" >&2; exit 2; }

cp -a "$here/carrier/." "$D/kotoba-shokunin/"
# the world's own overlay files (everything except the two meta files and empty dirs)
( cd "$here/$world" && find . -type f ! -name delta.patch ! -name README.md -print0 |
  while IFS= read -r -d '' f; do mkdir -p "$D/kotoba-shokunin/$(dirname "$f")"; cp -a "$f" "$D/kotoba-shokunin/$f"; done )
if [ -s "$here/$world/delta.patch" ]; then
  git -C "$D/kotoba-shokunin" apply --whitespace=nowarn "$here/$world/delta.patch"
fi

git -C "$D/kotoba-shokunin" -c user.name=k72-control -c user.email=k72-control@localhost add -A
git -C "$D/kotoba-shokunin" -c user.name=k72-control -c user.email=k72-control@localhost \
  commit -q -m "control world $world over $base"

echo "== $world  (sandbox $D/kotoba-shokunin)"
set +e
python3 -B "$here/oracle_author_rules_literal.py" --repo "$D/kotoba-shokunin" --rev HEAD
rc=$?
set -e
echo "exit=$rc"
