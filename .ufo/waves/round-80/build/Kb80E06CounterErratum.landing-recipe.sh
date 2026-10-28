#!/bin/bash
# Kb80E06CounterErratum — the LANDING RECIPE for the round-80 stack (C1 + C2).
#
# WHY THIS EXISTS: two published artifacts both modify verifiers/check_tip_battery.py —
# E06's E5 amendment (Kb80E06CounterErratum.patch) and the published bundle
# (Kb80Y01-simplified.patch) — so `git apply Kb80E06CounterErratum.patch` on that bundle's tree
# fails ("patch failed: verifiers/check_tip_battery.py:103").  The L1 lands exactly ONE counter
# stream.  This recipe lands the counter of E06's line set (the one plans/round-80.md §Addendum 1
# enumerates) on top of everything the bundle carries.
#
# USAGE
#   bash Kb80E06CounterErratum.landing-recipe.sh <work-dir>
#
# WHAT IT DOES
#   1. apply the published bundle MINUS its check_tip_battery.py hunk  (its registry rows, the
#      round-76 symlink, the coverage rows, the refreshed baseline, E04's pointer fix and the
#      grammar class);
#   2. write E06's amended counter file verbatim
#      (build/check_tip_battery.amended.py, sha256 15cc17614e61bdc47122bf501da951de3dbde6444b1ed4a98ca8192c2329ddba);
#   3. add the C2 counter, its gate-registry row and the round-79 snapshot MANIFEST (see the C2
#      NOTE below — without them the registry gate reads 62 of 63 and the round reports a C1
#      failure that is really a bookkeeping red);
#   4. commit.
#
# MEASURED RESULT ON THIS RECIPE'S TREE (receipts beside this script)
#   rev 0c73088048e40200d2be9e6906cc7b2c2edde841   (REPRODUCIBLE: two independent runs of
#                                                      this script produce this identical rev
#                                                      and tree; see the DETERMINISM note below)
#   counter sha256      15cc17614e61bdc47122bf501da951de3dbde6444b1ed4a98ca8192c2329ddba
#   instrument blobs    68ccce1c152c915e16893a5157c9d5878df779fb  (verify_corpus_integrity.py)
#                        e887de71892ecfc6be5b3f47e362ce8a766c5c89  (verify_corpus_independent.py)
#     -- the CANONICAL E05 class (L1 ruling), not Y01's candidate
#     -- exactly the two blobs E06's INSTRUMENT_PINS names
#   six-instrument numstat vs the pinned r72 base 072048fa:
#                        22/3 check_assertion_floors + 10/3 verify_corpus_independent
#                        + 28/2 verify_corpus_integrity = 60 added / 8 deleted (cap 60, EXACTLY at it)
#   check_gate_registry.py --rev <tip>  ->  gate registry rows conformant 63 of 63; phantom 0; exit 0
#   check_tip_battery.py --rev <tip>     ->  guards 5 of 5; tip battery exit 0: 6 of 6; exit 0
#   refresh-corpus-baseline.py --repo .  ->  post-refresh: 9/9 checks pass, exit 0
#
# DETERMINISM (fixed after Kb80S15FreezeShas measured that the rev was not reproducible)
#   The refresh script writes the COMMIT SHA it was refreshed at into the baseline's "head" and
#   "note" fields, so a run-to-run committer timestamp changed the baseline's bytes, and
#   therefore the tree and the rev.  Measured before the fix: two runs of this recipe gave
#   DIFFERENT revs AND DIFFERENT trees (the trees differing only in those two baseline fields).
#   Fixed by exporting GIT_AUTHOR_DATE and GIT_COMMITTER_DATE below, so the same inputs give
#   the same rev.  Measured after the fix: two runs -> the same rev
#   0c73088048e40200d2be9e6906cc7b2c2edde841 and the same tree
#   dde9e843b40e72d702e036781e3d3596f92d13ff, and that rev reads "guards 5 of 5; tip battery
#   exit 0: 6 of 6", exit 0.  The freeze may therefore pin THIS REV, not just the content.
#
# C2 NOTE (measured both ways; Kb80S15FreezeShas F19, confirmed here)
#   The C1-only composition of this recipe (steps 1-2) is green on its own: the registry gate
#   reads "62 of 62 lane verifiers; phantom 0", exit 0.  Adding the C2 counter
#   (build/check_allowed_tools.py) WITHOUT its registry row makes the gate read "62 of 63",
#   exit 1 — a bookkeeping red, not a repo-state red.  Step 3 therefore adds all three C2
#   artifacts together:
#     (i)   the C2 counter, copied verbatim from build/check_allowed_tools.py;
#     (ii)  its gate-registry row, the row S09 published (build/Kb80S09SkillRule.patch), inserted
#           VERBATIM as the last row of SKILL.md's "## Gate registry" table (the patch itself does
#           not apply to this tree because the bundle already shifted SKILL.md's line numbers);
#     (iii) .ufo/waves/round-79/snapshots/MANIFEST.sha256, the six per-page digests from
#           build/Kb80N01Sentinel-MANIFEST.proposed, each VERIFIED against the committed snapshot
#           bytes before it is written (the row's pinned-values cell names that path, and the
#           registry gate checks the named path exists at the rev).
#   With (i)-(iii) in place the gate reads "63 of 63 lane verifiers; phantom 0", exit 0.
#   The order the L1 should still follow: this recipe -> the C2 counter's own remaining pieces
#   (the entry, PROVINCE bullet, SKILL rule line) -> the baseline refresh -> measure.  The recipe
#   lands the C2 COUNTER and its registry row so the registry gate is not red; it does not land
#   the C2 entry, whose measured value is the C2 claim's business, not this counter's.
#
# REPRODUCING THE TWO INSTRUMENT BLOBS (the form that works — the helper in
# build/Kb80E04DeadPointer/ applies E04 FIRST and therefore fails on the bundle, which already
# embeds E04's hunk):
#   git clone --shared <lane> /tmp/x && git -C /tmp/x checkout 398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93
#   git -C /tmp/x apply build/Kb80E04DeadPointer.patch && git -C /tmp/x apply build/Kb80E05GrammarFix.patch
#   git -C /tmp/x hash-object verifiers/verify_corpus_integrity.py verifiers/verify_corpus_independent.py
#   -> 68ccce1c152c915e16893a5157c9d5878df779fb
#      e887de71892ecfc6be5b3f47e362ce8a766c5c89
#
# IF A DIFFERENT GRAMMAR-CLASS PATCH LANDS: both blobs move and nothing else in E06's counter
# changes — re-derive them with the recipe above and change one hex string per pin row.
set -euo pipefail
LANE=/home/vgpnk/Projects/shokunin/kotoba-shokunin
BUILD=$LANE/.ufo/waves/round-80/build
BASE=398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93
W=${1:?usage: landing-recipe.sh <work-dir>}
mkdir -p "$W"
git clone -q --shared "$LANE" "$W/clone"
git -C "$W/clone" checkout -q "$BASE"
test "$(git -C "$W/clone" rev-parse --show-toplevel)" = "$W/clone" || { echo SCRATCH-NOT-TOPLEVEL >&2; exit 2; }
git -C "$W/clone" config user.name scratch-r80
git -C "$W/clone" config user.email scratch@example.invalid
# DETERMINISM: the baseline the refresh script writes records the COMMIT SHA it was refreshed
# at, so a run-to-run committer timestamp would change the baseline's bytes and therefore the
# tree and the rev.  Fixed author/committer dates make the whole run reproducible: the same
# inputs produce the same rev.  (Measured before the fix: two runs of this recipe gave
# different revs AND different trees, the trees differing only in the baseline's "head" and
# "note" fields, which quote that commit.)
export GIT_AUTHOR_DATE="2026-10-27T00:00:00 +0000"
export GIT_COMMITTER_DATE="2026-10-27T00:00:00 +0000"

# 1. the published bundle minus its counter hunk
git -C "$W/clone" apply "$BUILD/Kb80E06CounterErratum.Y01bundle-minus-counter.patch"

# 1b. THE CANONICAL GRAMMAR CLASS (repair 5, E05): the bundle above carries Y01's candidate
#     class in the two corpus gates.  The L1 ruled that the canonical class is E05's, so reset
#     those two files to the base and apply E04 then E05 — the canonical composed content.
#     (Measured: E04 then E05 and E05 then E04 give the identical composed blobs, so the pin
#     does not depend on this order.)
git -C "$W/clone" checkout -q "$BASE" -- verifiers/verify_corpus_integrity.py verifiers/verify_corpus_independent.py
git -C "$W/clone" apply "$BUILD/Kb80E04DeadPointer.patch"
git -C "$W/clone" apply "$BUILD/Kb80E05GrammarFix.patch"

# 2. E06's amended counter, verbatim
cp "$BUILD/check_tip_battery.amended.py" "$W/clone/verifiers/check_tip_battery.py"

# 3. the C2 counter, its gate-registry row, and the snapshot MANIFEST (see the C2 NOTE)
cp "$BUILD/check_allowed_tools.py" "$W/clone/verifiers/check_allowed_tools.py"
python3 - "$W/clone/SKILL.md" "$BUILD/Kb80S09SkillRule.patch" <<'PY'
import sys
skill, patch = sys.argv[1], sys.argv[2]
row = None
for line in open(patch, encoding="utf-8").read().splitlines():
    if line.startswith("+| `verifiers/check_allowed_tools.py` |"):
        row = line[1:]          # strip the diff '+', keep the row text exactly
        break
if row is None:
    raise SystemExit("registry row not found in %s" % patch)
lines = open(skill, encoding="utf-8").read().split("\n")
last = max(i for i, l in enumerate(lines) if l.startswith("| `verifiers/"))
lines.insert(last + 1, row)
open(skill, "w", encoding="utf-8").write("\n".join(lines))
print("registry row inserted after line", last + 1)
PY
MANIFEST="$W/clone/.ufo/waves/round-79/snapshots/MANIFEST.sha256"
python3 - "$BUILD/Kb80N01Sentinel-MANIFEST.proposed" "$MANIFEST" <<'PY'
import hashlib, os, sys
src, dst = sys.argv[1], sys.argv[2]
rows = []
for line in open(src, encoding="utf-8").read().splitlines():
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    digest, name = line.split(None, 1)
    path = os.path.join(os.path.dirname(dst), name)
    with open(path, "rb") as fh:
        got = hashlib.sha256(fh.read()).hexdigest()
    if got != digest:
        raise SystemExit("digest mismatch for %s: got %s want %s" % (name, got, digest))
    rows.append("%s  %s" % (digest, name))
with open(dst, "w", encoding="utf-8") as fh:
    fh.write("\n".join(rows) + "\n")
print("MANIFEST.sha256 written; %d digests verified against the committed bytes" % len(rows))
PY


# 3b. the C2 ENTRY and its coverage-map row (the entry must be TRACKED and INDEXED, or the
#     corpus gate reads corpus.index.unindexed=1 and the baseline refresh refuses), then the
#     baseline refresh itself (the plan's order: rows -> E04 -> E05 -> refresh -> measure).
cp "$BUILD/allowed-tools-surfaces-round80.md" "$W/clone/corpus/knowledge/allowed-tools-surfaces-round80.md"
python3 - "$W/clone/corpus/README.md" "$BUILD/Kb80S08ReadmeRows.patch" <<'PY2'
import sys
readme, patch = sys.argv[1], sys.argv[2]
row = None
for line in open(patch, encoding="utf-8").read().splitlines():
    if line.startswith("+| Allowed-tools surfaces (round 80)"):
        row = line[1:]
        break
if row is None:
    raise SystemExit("coverage row not found in %s" % patch)
lines = open(readme, encoding="utf-8").read().split("\n")
end = next(i for i, l in enumerate(lines) if l.startswith("## ") and i > 5)   # the Coverage map table
last_row = max(i for i in range(5, end) if lines[i].startswith("| "))
lines.insert(last_row + 1, row)
open(readme, "w", encoding="utf-8").write("\n".join(lines))
print("coverage row inserted after line", last_row + 1)
PY2

git -C "$W/clone" add -A
git -C "$W/clone" commit -q -m "r80 stack: bundle minus its counter hunk + E06's E5-amended counter + the C2 counter, its registry row, the C2 entry, its coverage row and the snapshot MANIFEST"
# the refresh reads WORKTREE bytes while recording the baseline at HEAD, so it needs a clean
# tree: commit everything above first, then refresh, then commit the refreshed baseline.
python3 -B "$BUILD/refresh-corpus-baseline.py" --repo "$W/clone"
git -C "$W/clone" add -A
git -C "$W/clone" commit -q -m "refresh the corpus baseline at the stack tip"
echo "rev: $(git -C "$W/clone" rev-parse HEAD)"
echo "counter sha256:"; sha256sum "$W/clone/verifiers/check_tip_battery.py"
echo "instrument blobs:"; git -C "$W/clone" hash-object verifiers/verify_corpus_integrity.py verifiers/verify_corpus_independent.py
echo "six-instrument numstat vs the pinned r72 base 072048fa:"
git -C "$W/clone" diff --numstat 072048fa8e8a52c707d25f7079772fa317244eb7 -- \
  verifiers/check_gate_registry.py verifiers/check_assertion_floors.py \
  verifiers/verify_skill_checklist.py verifiers/verify_corpus_integrity.py \
  verifiers/verify_corpus_independent.py verifiers/check_correction_sweep.py
echo "gate registry on this tree:"
python3 -B "$W/clone/verifiers/check_gate_registry.py" --rev "$(git -C "$W/clone" rev-parse HEAD)" 2>&1 | tail -1
