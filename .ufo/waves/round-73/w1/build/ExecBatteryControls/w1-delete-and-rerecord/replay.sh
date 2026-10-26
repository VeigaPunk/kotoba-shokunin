#!/bin/sh
# replay.sh -- rebuild this control world in a fresh fleet-shaped sandbox and
# print the round-73 C3 counter's reading for it. Nothing outside the sandbox is
# written; the counter is read from the lane (read-only) and measures committed
# bytes only.
#
#   sh replay.sh            fresh sandbox, removed at the end
#   KEEP=1 sh replay.sh     keeps the sandbox and prints its path
#
# NOTE the counter is always given an ABSOLUTE --repo: with `--repo .` the
# counter's fleet default (verifiers/check_tip_battery.py:610, `repo.parent`)
# resolves to `.` itself and every `../` citation becomes unresolvable (M127).
# The reading recorded in counter.out was taken this way.
set -eu
here=$(cd "$(dirname "$0")" && pwd)
COUNTER=${COUNTER:-/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_tip_battery.py}
P=$(mktemp -d /tmp/k73w1-replay.XXXXXX)
applied=$(sh "$here/apply.sh" "$P")
rev=$(printf '%s\n' "$applied" | sed -n 's/^rev //p')
tree=$(printf '%s\n' "$applied" | sed -n 's/^tree //p')
echo "world revision: $rev (tree $tree)"
set +e
python3 -B "$COUNTER" --rev "$rev" --repo "$P/kotoba-shokunin" --fleet "$P"
rc=$?
set -e
echo "counter exit=$rc"
if [ "${KEEP:-0}" = 1 ]; then echo "sandbox kept: $P"; else rm -rf "$P"; fi
