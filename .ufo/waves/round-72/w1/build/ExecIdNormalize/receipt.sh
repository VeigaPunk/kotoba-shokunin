#!/usr/bin/env bash
# receipt.sh -- reproduce the ExecIdNormalize validation receipt for round-72 wave 1.
#
#   ./receipt.sh [rev]            # default: the frozen plan's base c69711e
#
# Two admission states are validated, because the seat does not decide admission:
#   THEME  the plan's two-entry theme (skill-vs-always-on-boundary + context-rot-and-always-on-
#          context): 6 rows, and staged S255/S256 held back because neither entry cites them;
#   ALL    every candidate row, admitted by the campaign's own citation edges (the same two
#          entries plus client-frontmatter-and-discovery-divergence for S255/S256): 8 rows.
# Both assign the same ids (S214-S221); a held-back row keeps its id.
#
# Each run builds a throwaway mirror under /tmp/k72w1-ExecIdNormalize.mirror.XXXX with
# `git archive <rev> | tar -x`, inserts the normalized block, writes the candidate knowledge
# entries, and runs the fleet validator:
#   bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file <mirror>/corpus/SOURCES.md
# Read-only with respect to the lane: git archive and reads only, no writes outside /tmp.
set -u
LANE=/home/vgpnk/Projects/shokunin/kotoba-shokunin
HERE=$(cd -- "$(dirname -- "$0")" && pwd)
REV=${1:-c69711ee08279609374d895bb0f3c8c18ccf15c9}
CENSUS=/home/vgpnk/Projects/shokunin/scripts/sources-census.sh
THEME=("--entry" "corpus/knowledge/skill-vs-always-on-boundary.md"
       "--entry" "corpus/knowledge/context-rot-and-always-on-context.md")
ALL=("${THEME[@]}" "--entry" "corpus/knowledge/client-frontmatter-and-discovery-divergence.md")
ROOT=$(mktemp -d /tmp/k72w1-ExecIdNormalize.mirror.XXXX) || exit 2
trap 'rm -rf "$ROOT"' EXIT

echo "receipt: seat ExecIdNormalize, round-72 wave 1, lane kotoba"
echo "measured-rev: $REV"
echo "date: $(date -Iseconds)"
echo "mirror root: $ROOT (scratch, removed on exit)"
echo "validator: $CENSUS validate --file <mirror>/corpus/SOURCES.md"
echo

echo "== A. transform self-test (14 arms) =="
python3 -B "$HERE/normalize-staged-rows.py" --self-test
echo "exit=$?"
echo

echo "== B. THEME admission (the plan's two entries): 6 rows, S255/S256 held back =="
python3 -B "$HERE/normalize-staged-rows.py" "${THEME[@]}" --rev "$REV" --mirror "$ROOT/b"
echo "exit=$?"
echo

echo "== C. row count of mirror B under census mode =="
bash "$CENSUS" census --file "$ROOT/b/corpus/SOURCES.md"
echo "exit=$?"
echo

echo "== D. subset re-run: --only S262 (one row, fresh mirror, same id S215) =="
python3 -B "$HERE/normalize-staged-rows.py" "${THEME[@]}" --only S262 --rev "$REV" --mirror "$ROOT/d"
echo "exit=$?"
echo

echo "== E. ALL candidate rows (campaign citation edges): 8 rows, ids unchanged =="
python3 -B "$HERE/normalize-staged-rows.py" --blocks "$HERE/blocks-all.json" "${ALL[@]}" \
  --rev "$REV" --mirror "$ROOT/e"
echo "exit=$?"
echo

echo "== F. row count of mirror E under census mode =="
bash "$CENSUS" census --file "$ROOT/e/corpus/SOURCES.md"
echo "exit=$?"
echo

echo "== G. negative controls on mirror B (one row appended, then restored) =="
python3 -B "$HERE/normalize-staged-rows.py" "${THEME[@]}" --rev "$REV" --mirror "$ROOT/g" \
  --control pipe --control dup-id --control dup-url --control missing-usedby
echo "exit=$?"
echo

echo "== H. a second-seat entry's citation edge: the C1 A4 entry cites S214-S217 =="
A4_DRAFT=$LANE/.ufo/waves/round-72/w1/build/ScribeEntryRung/resident-index-and-rungs-round72.md
A4=corpus/knowledge/resident-index-and-rungs-round72.md
if [ -f "$A4_DRAFT" ]; then
  python3 -B "$HERE/normalize-staged-rows.py" --blocks "$HERE/blocks-all.json" "${ALL[@]}" \
    --entry "$A4" --cite "$A4=S214,S215,S216,S217" --entry-src "$A4=$A4_DRAFT" \
    --rev "$REV" --mirror "$ROOT/h"
  echo "exit=$?"
else
  echo "skipped: $A4_DRAFT not present (another seat's draft); --entry-src copies it, never authors it"
fi
echo
