#!/usr/bin/env bash
# E11StrayAndMisroot.misroot_sweep.sh — read-only fleet-root misroot sweep.
#
# Round 77, seat E11StrayAndMisroot (R76-D1 follow-up).
#
# Purpose: round-77 wave-1 seats can write a lane-relative path while their
# cwd is the FLEET ROOT, which lands the file at
# /home/vgpnk/Projects/shokunin/<lane-relative-path> instead of inside the lane
# /home/vgpnk/Projects/shokunin/kotoba-shokunin/. That is how
#   kotoba-shokukin/.ufo/waves/round-76/w1/A18ScoutSnapshot.md   (commit 6ce2724)
#   kotoba-shokukin/.ufo/waves/round-75/w1/R75Facet48.md          (commit ac9f295)
# got committed. This script finds any *new* such spill before the L1 commits.
#
# READ-ONLY: one `git status` call. No add/commit/checkout/stash, no jj call,
# no rm, no writes anywhere.
#
# Usage:
#   bash .ufo/waves/round-77/build/E11StrayAndMisroot.misroot_sweep.sh
#       -> prints only untracked paths containing `kotoba` or `round-77`
#   bash .ufo/waves/round-77/build/E11StrayAndMisroot.misroot_sweep.sh --extra
#       -> additionally prints older `round-7x` spill (diagnostic only)
#
# Exit: 0 = no matching untracked path (clean); 1 = matching untracked path(s)
#       found (each printed on its own line); 2 = not a git work tree.
set -u

FLEET=/home/vgpnk/Projects/shokunin
EXTRA=0
case ${1:-} in
  --extra) EXTRA=1 ;;
  '') ;;
  *) echo "usage: $0 [--extra]" >&2; exit 64 ;;
esac

if ! top=$(git -C "$FLEET" rev-parse --show-toplevel 2>/dev/null); then
  echo "sweep: $FLEET is not a git work tree" >&2
  exit 2
fi
if [ "$top" != "$FLEET" ]; then
  echo "sweep: toplevel is $top, expected $FLEET" >&2
  exit 2
fi

# The required check: untracked entries whose path contains kotoba or round-77.
# A collapsed untracked directory (?? kotoba-shokukin/ or ?? .ufo/waves/round-77/)
# still matches, because the directory name carries the token.
status=$(git -C "$FLEET" status --porcelain 2>/dev/null) || {
  echo "sweep: git status failed" >&2; exit 2; }

hits=$(printf '%s\n' "$status" | sed -n 's/^?? //p' | LC_ALL=C grep -E 'kotoba|round-77' | LC_ALL=C sort -u)

if [ -z "$hits" ]; then
  echo "sweep: CLEAN — no untracked fleet-root path matching kotoba|round-77"
  rc=0
else
  echo "sweep: MISROOT RISK — untracked fleet-root path(s) matching kotoba|round-77:"
  printf '%s\n' "$hits" | sed 's/^/  /'
  echo "sweep: resolve by moving each path to the lane, e.g."
  echo "  mv -- \"$FLEET/<path>\" \"$FLEET/kotoba-shokunin/<path-without-the-typo-prefix>\""
  echo "  (then verify with cmp; never commit the fleet root)"
  rc=1
fi

if [ "$EXTRA" -eq 1 ]; then
  echo "sweep: --extra — untracked fleet-root paths matching round-7 (diagnostic):"
  printf '%s\n' "$status" | sed -n 's/^?? //p' | LC_ALL=C grep -E 'round-7|kotoba' | LC_ALL=C sort -u | sed 's/^/  /' || \
    echo "  (none)"
fi

exit "$rc"
