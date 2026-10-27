#!/usr/bin/env bash
# N01Sentinel.sweep.sh — read-only sentinel sweep for kotoba round 77 w1.
#
# Scope (round-77 w1 seat N01Sentinel):
#   .ufo/waves/round-76/build/, .ufo/waves/round-76/snapshots/,
#   .ufo/waves/round-77/build/, .ufo/waves/round-77/w1/,
#   .ufo/waves/round-77/receipts/
# Checks: credential material; /tmp citations; hardcoded /tmp roots in
# seat-written scripts; scratch trees left by finished seats under
# /fast/scratch/hyaku/kotoba-r77/; files written outside the lane repo
# (fleet status + sibling-lane scan); and the pinned input bytes.
#
# READ-ONLY: no writes, no git/jj mutation, no rm, no network, no mktemp.
# The sweep excludes its own files (N01Sentinel.*) from the citation grep so
# the script and its report do not count their own text as hits.
#
# Exit: 0 = every class empty; 1 = at least one finding class is non-empty.
set -u
LC_ALL=C
export LC_ALL

LANE=/home/vgpnk/Projects/shokunin/kotoba-shokunin
FLEET=/home/vgpnk/Projects/shokunin
SCRATCH=/fast/scratch/hyaku/kotoba-r77
SCOPE="$LANE/.ufo/waves/round-76/build $LANE/.ufo/waves/round-76/snapshots
$LANE/.ufo/waves/round-77/build $LANE/.ufo/waves/round-77/w1
$LANE/.ufo/waves/round-77/receipts"
SELF_RE='N01Sentinel\.(md|sweep\.sh|sweep-output\.txt)'
findings=0

hdr() { printf '\n== %s ==\n' "$1"; }

hdr 'A. credential material (r76 build+snapshots, r77 build+w1+receipts)'
A=$(grep -RInE 'op://[A-Za-z0-9]|gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY-----|Authorization: *Bearer [A-Za-z0-9]|xox[baprs]-[A-Za-z0-9-]{10,}|sk-[A-Za-z0-9]{32,}' $SCOPE 2>/dev/null)
if [ -n "$A" ]; then printf '%s\n' "$A"; findings=$((findings + 1)); fi
printf 'credential hits: %s\n' "$(printf '%s' "$A" | grep -c . )"

hdr 'B. /tmp citations (evidence paths under /tmp are not citable)'
B=$(grep -RIn '/tmp' $SCOPE 2>/dev/null \
    | grep -v 'w1-spec\.json\|w1-dispatch\.json' \
    | grep -vE "$SELF_RE")
if [ -n "$B" ]; then printf '%s\n' "$B"; findings=$((findings + 1)); fi
printf '/tmp mention lines: %s\n' "$(printf '%s' "$B" | grep -c . )"

hdr 'C. hardcoded /tmp roots in seat-written scripts'
C=$(grep -RInE 'mkdtemp\(dir *= *["'"'"']/tmp|/tmp/[A-Za-z0-9._-]*X{3,}|TMPDIR:-/tmp|\$\{TMPDIR:-/tmp\}' \
      "$LANE/.ufo/waves/round-77/build" "$LANE/.ufo/waves/round-76/build" 2>/dev/null \
    | grep -vE "$SELF_RE")
if [ -n "$C" ]; then printf '%s\n' "$C"; findings=$((findings + 1)); fi
printf 'hardcoded-/tmp lines: %s\n' "$(printf '%s' "$C" | grep -c . )"

hdr 'D. scratch trees left by finished seats (report file present)'
D=''
for d in "$SCRATCH"/*/; do
  s=$(basename "$d")
  if [ -f "$LANE/.ufo/waves/round-77/w1/$s.md" ]; then
    line=$(printf 'REPORT+SCRATCH %-24s %s' "$s" "$(du -sh "$d" 2>/dev/null | cut -f1)")
    D="$D$line
"
  fi
done
if [ -n "$D" ]; then printf '%s' "$D"; findings=$((findings + 1)); fi
printf 'finished-seat scratch trees: %s\n' "$(printf '%s' "$D" | grep -c . )"
printf 'loose files in scratch parent:\n'
find "$SCRATCH" -maxdepth 1 -type f -printf '  %s %f\n' 2>/dev/null

hdr 'E. files written outside the lane repo'
printf -- '-- fleet repo status --\n'
git -C "$FLEET" status --porcelain 2>/dev/null
printf -- '-- lane repo status --\n'
git -C "$LANE" status --porcelain 2>/dev/null
printf -- '-- sibling lanes with kotoba|round-77 status entries --\n'
for d in "$FLEET"/*/; do
  d=${d%/}
  [ -d "$d/.git" ] || continue
  [ "$d" = "$LANE" ] && continue
  hit=$(timeout 10 git -C "$d" status --porcelain 2>/dev/null | grep -iE 'kotoba|round-77' | head -3)
  [ -n "$hit" ] && printf '%s:\n%s\n' "$d" "$hit"
done
printf -- '-- end sibling scan --\n'

hdr 'F. pinned inputs'
sha256sum "$LANE/verifiers/check_desc_craft.py" "$LANE/verifiers/check_r75_routed_repairs.py"
( cd "$LANE/.ufo/waves/round-76/snapshots" && sha256sum -c MANIFEST.sha256 )
printf 'lane HEAD: %s\n' "$(git -C "$LANE" rev-parse HEAD)"

hdr 'G. kotoba-attributable /tmp entries (top level)'
ls -d /tmp/SC03-* /tmp/skill.*.md /tmp/r75base.md /tmp/r75head.md /tmp/sc01-page.md \
       /tmp/k72-tip-* /tmp/k76-* 2>/dev/null

printf '\nSWEEP FINDING CLASSES NON-EMPTY: %s\n' "$findings"
[ "$findings" -eq 0 ]
