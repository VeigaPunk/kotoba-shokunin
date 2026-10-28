#!/usr/bin/env bash
# compute-combined-blob.sh <grammar-patch> [e04-patch]
#
# Kb80E04DeadPointer helper: prints the git blob sha1 of
# verifiers/verify_corpus_integrity.py AFTER both the E04 dead-pointer repair
# and a grammar-class patch are applied to the round-80 base.
#
# The E04 patch alone yields blob 051b8c5f8676cba5c8d6047c8c9f7fcb56cd8f9f
# (published at .ufo/waves/round-80/build/Kb80E04DeadPointer.blob).
# If the grammar-class patch also edits verifiers/verify_corpus_integrity.py,
# the TIP blob is the combined content and INSTRUMENT_PINS must carry THAT sha,
# not 051b8c5f... (the pin guard compares the blob AT the measured rev).
#
# Usage:
#   bash compute-combined-blob.sh <grammar-patch> [e04-patch]
# The order of application does not matter: measured both ways, the resulting
# blob is identical (see the seat report).
set -euo pipefail

GRAMMAR_PATCH=${1:?usage: compute-combined-blob.sh <grammar-patch> [e04-patch]}
E04_PATCH=${2:-/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E04DeadPointer.patch}
BASE=398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93
LANE=/home/vgpnk/Projects/shokunin/kotoba-shokunin

S=${TMPDIR:-/tmp}/kb80e04-blob-$$
mkdir -p "$S"
trap 'rm -rf -- "$S"' EXIT
git clone -q --shared "$LANE" "$S/clone"
git -C "$S/clone" checkout -q "$BASE"
test "$(git -C "$S/clone" rev-parse --show-toplevel)" = "$S/clone" || { echo SCRATCH-NOT-TOPLEVEL >&2; exit 2; }

git -C "$S/clone" apply "$E04_PATCH"
git -C "$S/clone" apply "$GRAMMAR_PATCH"

BLOB=$(git -C "$S/clone" hash-object verifiers/verify_corpus_integrity.py)
INDEP=$(git -C "$S/clone" hash-object verifiers/verify_corpus_independent.py)
NUMSTAT=$(git -C "$S/clone" diff --numstat 072048fa8e8a52c707d25f7079772fa317244eb7 -- \
  verifiers/check_gate_registry.py verifiers/check_assertion_floors.py \
  verifiers/verify_skill_checklist.py verifiers/verify_corpus_integrity.py \
  verifiers/verify_corpus_independent.py verifiers/check_correction_sweep.py)

echo "integrity blob (E04+grammar): $BLOB"
echo "independent blob (grammar)  : $INDEP"
echo "six-instrument numstat vs base 072048fa:"
echo "$NUMSTAT"
echo "--- remember: the tip-battery instrument-size guard sums the ADDED column;"
echo "--- the plan budgets 22 (at base) + 17 (E04) + grammar <= 60."
