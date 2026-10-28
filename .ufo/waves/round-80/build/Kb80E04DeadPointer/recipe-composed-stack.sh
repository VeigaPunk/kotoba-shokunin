set -u
S=/fast/scratch/hyaku/kotoba-r80/Kb80E04DeadPointer
export TMPDIR=$S/tmp
B=/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build
rm -rf "$S/clone3"
git clone -q --shared /home/vgpnk/Projects/shokunin/kotoba-shokunin "$S/clone3"
cd "$S/clone3" || exit 2
test "$(git rev-parse --show-toplevel)" = "$S/clone3" || { echo SCRATCH-NOT-TOPLEVEL; exit 2; }
git checkout -q 398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93
git apply "$B/Kb80Y01-simplified.patch" || { echo Y01-APPLY-FAILED; exit 2; }
git add -A
git -c user.name=scratch-r80 -c user.email=scratch@example.invalid commit -qm "r80 composed stack: E04 + grammar class (Y01 bytes)"
git rev-parse HEAD > "$S/y01-stack-rev.txt"
git rev-parse HEAD:verifiers/verify_corpus_integrity.py > "$S/y01-stack-integrity-blob.txt"
git rev-parse HEAD:verifiers/verify_corpus_independent.py > "$S/y01-stack-independent-blob.txt"
python3 -B verifiers/check_tip_battery.py --rev "$(cat "$S/y01-stack-rev.txt")" --repo "$S/clone3" --fleet /home/vgpnk/Projects/shokunin > "$S/tipbattery-y01-stack-abs.txt" 2>&1
rc=$?
echo "exit=$rc" >> "$S/tipbattery-y01-stack-abs.txt"
echo DONE
