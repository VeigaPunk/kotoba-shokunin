# ExecBatterySelfTest — round 94 C1 build (battery self-test kills k1, k2, k3)

Seat: ExecBatterySelfTest (executor). Owned file: `verifiers/check_mutation_battery.py` (C1 only).
Base: freeze commit `edc731a91a956f6df20c27a74fb981b286f6ba58`.
Scratch clone (removed after use): `/fast/scratch/hyaku/kotoba-r94/ExecBatterySelfTest/repo`. Candidate commit (scratch identity): `0be372b69e1c49c612b7631d5fdcc3c0a808bf4f` (diff vs freeze: 1 file, +26 lines).

## Change (self_test() section only; production evaluate()/kill_set_check()/main() unchanged)
Seven new behavioural assertions, 31 -> 38 total. Each new arm runs the instrument on a fixture or a live manifest and reads its exit code and output.
Anchors unchanged: `ok_pin, pin_detail = kill_set_check(committed, pinned)` 1x, `print("could-not-evaluate: %s" % exc)` 3x, `return n == want, "observed` 1x. Module pin capture/restore kept. No new occurrence of any anchor.

- k1 (working-tree read): `k1 working-tree read: the fixture's working-tree manifest is dirty (precondition)`;
  `k1 working-tree read: a kill row dropped in the working tree only exits 0 (committed bytes govern) without kill-set-size`
  (run_evaluate on a fixture whose committed manifest is honest and whose working tree drops kill row 0).
- k2 (label every CNE): `k2 label-every-cne: the G1 short-rev refusal is not labelled kill-set-size`;
  `k2 label-every-cne: the G1 commit-check refusal is not labelled kill-set-size`;
  `k2 label-every-cne (rev path): an anchor miss exits 2 without the kill-set-size label` (run_evaluate, pin 10).
- k3 (added rows): `arm kill-set-size (k3): the live manifest with one kill row appended is refused by the pin` (kill_set_check on live text + one row);
  `k3 added rows (rev path): a committed manifest with one kill row above the pin exits 2 naming kill-set-size` (run_evaluate, pin 9, 10 kill rows).

## Verification (observed)
- `python3 -B verifiers/check_mutation_battery.py --self-test` at candidate → `0 failure(s) over 38 assertions`, rc 0 (`receipts/selftest-candidate.txt`).
- Frozen counter `selftest-kills.py c1 0be372b6… <scratch repo>` (`receipts/counter-c1-candidate.txt`):
  honest rc 0; k1 KILLED (1 failure); k2 KILLED (3); k3 KILLED (2); positive k0 KILLED (4); decoys held 3 of 3.
  Tally: `C1 targets killed 3 of 3; positive killed 1 of 1; honest rc 0; decoys held 3 of 3` → `C1-PREDICATE-MET`, rc 0.
- Round-93 `c1-killpin-rev.sh 0be372b6… <scratch repo>` (`receipts/r93-c1-killpin-candidate.txt`):
  drop world rc 2 names kill-set-size yes; other world rc 2 names no; honest rc 0 names no → `C1-PREDICATE-MET`, rc 0.
- Round-92 `controls-run.sh`, run from inside the scratch clone (the ctl-*.sh scripts resolve REV from their own repo, so they were run against the candidate by placing the run in the clone; the lane was not touched) (`receipts/r92-controls-candidate.txt` + `.stderr`):
  `round-92 controls: shortcuts refused 2 of 2; honest held 2 of 2`, rc 0. C2-shortcut, C2-honest, C1-shortcut, C1-honest all met.
- Patch: `ExecBatterySelfTest/ExecBatterySelfTest.patch` = `git diff --binary edc731a9… 0be372b6… -- verifiers/check_mutation_battery.py`, 56 lines,
  sha256 `cbf44a34c6f99bf4ae3fb353c5e34fc34d4efc1567f67a1c3f29037991d04834`.
  Fresh clone at the freeze: `git apply --check` OK, `git apply`, then `--self-test` → `0 failure(s) over 38 assertions`. The fresh clone was removed.
- READY: `ExecBatterySelfTest_READY` (patch sha256 and one line).

## Findings
- The frozen counter, not the self-test, is the arbiter here. Against the base instrument the three targets were not killed (`redbefore-c1-base.txt`, pre-data). Against the candidate all three are killed and the decoys hold.
- F1 (round-93 m3, working-tree read): now killed by a behavioural arm (k1) that dirties the working tree of a fixture and reads the exit code at the committed head.
- F2 (round-93 added rows): now killed on both the live path and the rev path (k3).
- F4 (round-93 m6, label every CNE): now killed by two non-kill-set rc-2 arms (G1 short-rev, G1 commit-check) and one rev-path anchor-miss arm (k2).
- Not addressed (out of this claim): round-93 m5 (order-insensitive kill check, F3) is not in the frozen mutant table and was not targeted.

## Risks
- The k2 rev-path arm and the k3 rev-path arm call `evaluate()` on fixtures, which runs the probe subprocesses. Self-test runtime rose modestly (about 5 s on this host for the full self-test).
- A sniffer that skips comments (AST-aware) is outside the counter's decoy guard. The new arms observe behaviour, so this does not change the C1 verdict.

## Tooling
No installs. No host or kernel settings changed. No lane, fleet-root, sibling-lane, or git write in the lane. Scratch directory removed.

## Checks the main agent should run
- `python3 -B verifiers/check_mutation_battery.py --self-test` on the integrated tree (expect `0 failure(s) over 38 assertions`).
- `python3 -B verifiers/fixtures/round-94/selftest-kills.py c1 <landing rev>` (expect `C1-PREDICATE-MET`, decoys held 3 of 3).
