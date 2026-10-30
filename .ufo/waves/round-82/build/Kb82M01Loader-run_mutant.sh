#!/bin/bash
# usage: run_mutant.sh NAME  -- commits the working-tree mutant on top of the
# candidate in the scratch clone, runs the frozen counter twice, restores candidate.
set -u
NAME="$1"
C=/fast/scratch/hyaku/kotoba-r82/Kb82M01Loader/clone
T=/fast/scratch/hyaku/kotoba-r82/Kb82M01Loader/tmp
CAND=6f9e6d9443118b25ad07341f80b335b63c3cf92d
export TMPDIR=$T
[ "$(git -C "$C" rev-parse --show-toplevel)" = "$C" ] || { echo TOPLEVEL_MISMATCH; exit 9; }
[ "$(git -C "$C" rev-parse HEAD)" = "$CAND" ] || { echo HEAD_NOT_CANDIDATE; exit 8; }
git -C "$C" add -A verifiers || exit 7
if git -C "$C" diff --cached --quiet; then echo "NO_MUTATION_STAGED $NAME"; exit 6; fi
git -C "$C" -c user.name="Kb82M01Loader scratch" -c user.email="kb82m01loader@scratch.invalid" commit -q -m "mutant $NAME (scratch fixture)" || exit 5
M=$(git -C "$C" rev-parse HEAD)
git -C "$C" diff "$CAND" "$M" > "$T/mut_$NAME.patch"
echo "MUTANT=$NAME COMMIT=$M PATCH_SHA256=$(sha256sum "$T/mut_$NAME.patch" | cut -d' ' -f1)"
cd "$C"
s1=$(date +%s)
python3 -B verifiers/check_substrate_repin_v2.py --rev "$M" --repo "$C" > "$T/mut_$NAME.run1.out" 2> "$T/mut_$NAME.run1.err"; e1=$?
s2=$(date +%s)
python3 -B verifiers/check_substrate_repin_v2.py --rev "$M" --repo "$C" > "$T/mut_$NAME.run2.out" 2> "$T/mut_$NAME.run2.err"; e2=$?
e=$(date +%s)
echo "RUN1_EXIT=$e1 elapsed_s=$((s2-s1))"
echo "RUN2_EXIT=$e2 elapsed_s=$((e-s2))"
if cmp -s "$T/mut_$NAME.run1.out" "$T/mut_$NAME.run2.out" && cmp -s "$T/mut_$NAME.run1.err" "$T/mut_$NAME.run2.err"; then echo "STABLE=yes"; else echo "STABLE=no"; fi
echo "--- stdout run1:"; cat "$T/mut_$NAME.run1.out"
echo "--- stderr run1:"; head -c 1500 "$T/mut_$NAME.run1.err"; echo
git -C "$C" reset -q --hard "$CAND" || exit 4
echo "RESTORED_HEAD=$(git -C "$C" rev-parse HEAD) status_lines=$(git -C "$C" status --porcelain | wc -l)"
