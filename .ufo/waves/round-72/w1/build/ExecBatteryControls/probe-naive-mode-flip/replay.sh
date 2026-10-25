#!/bin/sh
# replay.sh -- rebuild this control world in a throwaway fleet-shaped sandbox,
# run the six frozen C3 battery commands, and recompute the four counter
# guards. Nothing outside the sandbox is written.
#
#   sh replay.sh            (output goes to the sandbox, removed at the end)
#   KEEP=1 sh replay.sh     (keeps the sandbox and prints its path)
set -eu
here=$(cd "$(dirname "$0")" && pwd)
P=$(mktemp -d /tmp/k72w1-replay.XXXXXX)
applied=$(sh "$here/apply.sh" "$P")
rev=$(printf "%s\n" "$applied" | sed -n "s/^rev //p")
tree=$(printf "%s\n" "$applied" | sed -n "s/^tree //p")
echo "world revision: $rev (tree $tree)"
mkdir -p "$P/out"
sh "$here/run6.sh" "$P/kotoba-shokunin" "$rev" "$P/out"
echo "--- guards"
python3 -B "$here/guards.py" "$P/kotoba-shokunin" "$rev"
if [ "${KEEP:-0}" = 1 ]; then echo "sandbox kept: $P"; else rm -rf "$P"; fi
