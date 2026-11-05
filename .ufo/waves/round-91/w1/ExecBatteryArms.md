# ExecBatteryArms — r91-w1 C1 build report

Seat: ExecBatteryArms (executor). Claim: plans/round-91.md § C1 (battery guard arms, manifest rows,
third probe target). Base: 9af1a7af2adf0ab07cfd53f92affc1ed8d992262 (freeze commit). All work in the
scratch clone /fast/scratch/hyaku/kotoba-r91/ExecBatteryArms/repo (deleted after handoff); nothing
written in the lane except the files named below.

## Files written (lane)
- `.ufo/waves/round-91/w1/ExecBatteryArms/ExecBatteryArms.patch` — the C1 patch (10192 bytes, `git diff --binary` vs the freeze commit; `git apply --check` clean on a fresh base clone)
- `.ufo/waves/round-91/w1/ExecBatteryArms_READY` — content `N=25 rc=0`
- receipts: `ExecBatteryArms/{base-selftest,selftest-final,mutant-mb-m2,mutant-mb-m15,mutant-mb-m16,anchors,patch-applies}.txt`
- this report

## Files changed (inside the patch; the only two I own)
- `verifiers/check_mutation_battery.py`
  - `BAT = "verifiers/check_mutation_battery.py"` constant; third `PROBES` entry `BAT: (("bat-self-test", ["--self-test"], 0),)` — manifest targets == PROBES keys stays true
  - three new self-test arms (6 assertions, each named): G1 commit-check (full-hex non-commit `--rev` → exit 2 naming "is not a commit"), G1 clean-tree (scratch-clone `status --porcelain` interception returns dirt → exit 2 "not clean"), G2 restore read-back (`place` interception tampers only `restore `-labelled writes → exit 2 naming G2 copy integrity on the restore copy)
  - fixture world updated so it materializes a battery stub: `FX_BAT`, `FX_KILL_BAT` (fx-k10), `_eq_rows` gains the bat target, `build_fixture` writes `BAT: FX_BAT`; fixture predicate-line pins updated to 9 kills / 9 equivalents / 1 survivor (line_ok, line_broken 9-of-10, line_eq 8-of-9)
  - docstring: one added sentence naming the round-91 kill channel; exit ladder, predicate line, G1–G3, `--allow-unregistered` semantics untouched
- `verifiers/fixtures/mutation-battery/manifest.tsv` — exactly three appended kill rows (five columns, target `verifiers/check_mutation_battery.py`): `mb-m2-g1-commit-check-skipped`, `mb-m15-clean-tree-guard-off`, `mb-m16-restore-unverified`, recipes ported from r90 `MutTesterBattery/harness.py` MUTANTS with anchors re-verified against the final bytes. Class counts now 17 kill / 6 equivalent / 0 survivor → the frozen predicate sentence prints `mutation battery killed 17 of 17 kill-set; equivalents survived 6 of 6; disclosed survivors 0 of 0`.

## Evidence (observed)
- Base self-test (freeze bytes): `0 failure(s) over 19 assertions`, rc 0, 2778 ms.
- Final self-test (patch bytes): `0 failure(s) over 25 assertions`, rc 0, 3868 ms — N=25 ≥ 22, exit 0.
- Able-to-fail (each r90 mutant replayed on the final bytes; self-test of the mutated battery, standalone, TMPDIR-scratch only):
  - mb-m2 → rc 1, `1 failure(s) over 25 assertions`, FAIL `G1 commit check: the refusal says the revision is not a commit`
  - mb-m15 → rc 1, `2 failure(s) over 25 assertions`, FAIL both `G1 clean-tree guard: …` assertions
  - mb-m16 → rc 1, `2 failure(s) over 25 assertions`, FAIL both `G2 restore read-back: …` assertions
- Anchors: each mb-* anchor `findall` == 1 against the final bytes; every recipe `json.loads`-parses; 5 columns per row.
- Patch: `git apply --check` rc 0 on a fresh clone at 9af1a7af.

## Findings
1. **Manifest recipe JSON escaping (defect caught pre-landing).** My first draft wrote regex escapes as `\.` inside the recipe JSON; that is an invalid JSON escape (`Invalid \escape`) and `parse_manifest` would have made the LANDING battery run exit 2. The manifest convention (matching the existing fg-*/d5-* rows) is regex backslashes doubled in JSON (`\\.`), actual newlines/quotes as `\n`/`\"`. All three recipes now follow it; verified by json.loads + anchor counts. Anyone porting further r90 mutants into this manifest must double-escape.
2. **Fixture world must materialize every PROBES target.** Adding a third PROBES key silently broke every fixture world (`git show <rev>:verifiers/check_mutation_battery.py failed`, 12 self-test failures) until `build_fixture` wrote a battery stub. The target-set invariant (`manifest targets == PROBES keys`) reaches into fixture construction; any future probe target needs a fixture stub in the same change.
3. The new kill channel is the battery's own self-test probe: under each mutant the probe's exit/output differs from the clean baseline (`0 failure(s) over 25 assertions`, exit 0), so each mb-* kill-class row flips to killed without touching the two-sided equivalents rule (6 eq rows untouched, still measurement-time generated).

## Risks
- The landing run now runs the battery self-test probe 4× (baseline + three mb-* rows) plus all fg/d5 probes; measured self-test duration is ~3–4 s against PROBE_TIMEOUT 120 s, so per-probe headroom is large; total landing-run wall time grows by roughly a minute.
- My anchors bind only to battery bytes (edited by me alone). If ExecLadder's freeze-gate repair shifts any fg-* anchor line, that row's anchor miss would surface at the landing run — outside my file ownership, flagged for the L1/attack seats.
- No tool installs were performed (none needed); no pacman use; no kernel/host settings touched.

## Cleanup
Scratch dir /fast/scratch/hyaku/kotoba-r91/ExecBatteryArms (repo clone, prove clone, mutant copies,
mutcheck.py, base-battery.py) deleted after the receipts and patch were written to the wave dir.
