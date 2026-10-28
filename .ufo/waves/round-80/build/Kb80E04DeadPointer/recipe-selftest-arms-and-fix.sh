set -u
S=/fast/scratch/hyaku/kotoba-r80/Kb80E04DeadPointer
export TMPDIR=$S/tmp
cd "$S/clone2" || exit 2
git reset --hard -q 398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93
git apply "$S/arms-only.patch"
python3 -B verifiers/verify_corpus_integrity.py --self-test > "$S/selftest-arms-only.txt" 2>&1
rc=$?
echo "exit=$rc" >> "$S/selftest-arms-only.txt"
git reset --hard -q 398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93
git apply /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E04DeadPointer.patch
python3 -B verifiers/verify_corpus_integrity.py --self-test > "$S/selftest-postfix.txt" 2>&1
rc=$?
echo "exit=$rc" >> "$S/selftest-postfix.txt"
echo DONE
