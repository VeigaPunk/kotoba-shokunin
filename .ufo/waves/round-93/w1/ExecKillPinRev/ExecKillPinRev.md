# ExecKillPinRev — C1 build

## files_written
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-93/w1/ExecKillPinRev/ExecKillPinRev.patch
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-93/w1/ExecKillPinRev/ExecKillPinRev.md
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-93/w1/ExecKillPinRev_READY

## evidence
- python3 -B verifiers/check_mutation_battery.py --self-test (scratch clone D=/fast/scratch/hyaku/kotoba-r93/ExecKillPinRev/repo at 8c7fe6d963bbc2ef1c59c7ee952e6b89827e41fc): `0 failure(s) over 31 assertions`
- HYAKU_SCRATCH=/fast/scratch/hyaku/kotoba-r93/ExecKillPinRev bash verifiers/fixtures/round-93/c1-killpin-rev.sh 8c7fe6d963bbc2ef1c59c7ee952e6b89827e41fc "$D": `C1-PREDICATE-MET` (drop rc 2 names kill-set-size yes; other rc 2 names no; honest rc 0 names no)
- bash verifiers/fixtures/round-92/controls-run.sh (from clone at candidate): C1-honest `C1-PREDICATE-MET` (killed 17 of 17); C1-shortcut `C1-SHORTCUT-REFUSED ... could-not-evaluate: manifest mb-c1-shortcut-kill:`; full controls-run.sh exceeds 300s tool cap in this seat (timed out 2x) but its two C1 steps were run individually above and C2 steps are unaffected by this C1-only patch
- mb anchors: each of mb-m2-g1-commit-check-skipped, mb-m15-clean-tree-guard-off, mb-m16-restore-unverified anchor regex matches edited file exactly once (same as base)
- git apply --check on second fresh clone at 6d7eee0570912d9f3b9d3e3d0137f3c755451233: APPLY-OK; patch sha256 c88bd6aaddadab2fcb1321628fbb273f2c84033c564bd5d1f27047a2e1705f20

## findings
- evaluate() now runs kill_set_check() on committed manifest right after parse_manifest/target-set check and raises could-not-evaluate (rc 2) naming `kill-set-size` on mismatch; round-92 shortcut world still refused by existing `could-not-evaluate: manifest mb-c1-shortcut-kill:` line (target-set check first).
- kill_set_check/evaluate accept optional pinned param (default None → KILL_SET_PINNED=17, module pin unchanged) so self-test fixtures (9-10 kill rows) can drive rev path without altering the lane pen; live-manifest arm called with explicit 17.
- self_test arms (31 total, was 28): `kill-set-size rev path: matching pin exits 0 without naming`, `dropping a kill row exits 2 naming kill-set-size`, `unrelated baseline failure (dead kill row) does not name kill-set-size`. Fixture arms pin KILL_SET_PINNED locally (restored, never module-persisted).

## risks
- Self-test mutates module-global KILL_SET_PINNED within try/finally for fixture arms; probe processes are subprocesses reading file bytes so no cross-process leak, but a fork between set and restore could be tainted — restore is in finally, same process.
- evaluate() signature gained optional pinned kwarg (backwards compatible); frozen counter calls via CLI so default None preserves 17.
