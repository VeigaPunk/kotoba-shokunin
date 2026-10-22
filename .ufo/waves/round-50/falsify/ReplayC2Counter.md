# ReplayC2Counter — round-50 falsify, C2 operability replay

HOLDS — C2 as re-sized (`plans/round-50.md:31-39`): `killed 0 of 6` at `f3046466` and `killed 6 of 6` at
`542f5156` / `956ee167` reproduce via the committed driver, and the same 0 of 6 → 6 of 6 reproduces
independently (no driver): deleting each of the 6 must-fail cases in place from a 542f5156 scratch copy
makes `--box-proof` exit 1, while at f3046466 every deletion still exits 0.

## What I ran

All work in my scratch dir `/fast/scratch/hyaku/kotoba-r50/falsify/ReplayC2Counter/`
(`git clone` of the lane pinned to `956ee1676e4c18480bce8ac3993541462be76e11`; trees exported with
`git archive <rev> | tar -x` — the lane itself was never written). No tools installed.

### 1. Driver replay (committed counter)

`python3 -B verifiers/box_proof_case_deletion.py --rev <rev>` from the pinned clone:

- `--rev f30464660c675d1c1e2851a3bf0366a3aaffe5a8` → `killed 0 of 6`, **exit 1**. All six cases
  (`d04-placeholder, d04-stem, d04-unknown-lane, d08-role-round, d08-report-dir-round, d08-above-state`)
  `exit 0 survived`; control: `exit 0 boxes proven 2`; mode `--fixtures`.
- `--rev 542f515672306e1baefcb69ba79f1d4c18b6450e` → `killed 6 of 6`, **exit 0**. All six
  `exit 1 killed`; controls 2 of 2, na 1 of 1 also killed at this rev; control: `exit 0 boxes proven 2`.
- `--rev 956ee1676e4c18480bce8ac3993541462be76e11` → `killed 6 of 6`, **exit 0**. Identical per-case
  lines to 542f5156.

### 2. Independent, driver-free deletion (in-place manifest edit)

For each rev I exported the tree, then for each of the 6 must-fail cases copied the pristine export,
removed only that `cases[]` entry from `verifiers/fixtures/dispatch-prompts/manifest.json`
(9 → 8 entries; fixture directories untouched — the plan's re-sized "delete means removing a manifest
entry"), and ran exactly `python3 -B verifiers/verify_dispatch_prompts.py --box-proof --map
verifiers/checklist-baseline.json` (no `--fixtures` — the literal claim form).

At **542f5156** (intact control: exit 0, `boxes proven 2`, stderr empty), each single deletion:

| deleted case | exit | stdout | stderr line |
|---|---|---|---|
| d04-placeholder | 1 | `boxes proven 1` | `box-proof: dispatch.04: no isolated must-fail case for conjunct report_path_literal` |
| d04-stem | 1 | `boxes proven 1` | `box-proof: dispatch.04: no isolated must-fail case for conjunct report_stem_is_lane_id` |
| d04-unknown-lane | 1 | `boxes proven 1` | `box-proof: dispatch.04: no isolated must-fail case for conjunct lane_identity_known` |
| d08-role-round | 1 | `boxes proven 1` | `box-proof: dispatch.08: no isolated must-fail case for conjunct filename_role_round_equal` |
| d08-report-dir-round | 1 | `boxes proven 1` | `box-proof: dispatch.08: no isolated must-fail case for conjunct filename_report_dir_round_equal` |
| d08-above-state | 1 | `boxes proven 1` | `box-proof: dispatch.08: no isolated must-fail case for conjunct round_le_latest_dispatched` |

At **f3046466** (intact control: exit 0, `boxes proven 2`), every one of the same six deletions:
**exit 0**, stdout `boxes proven 2`, stderr empty — the coverage check simply is not there yet.
Independent 0 of 6.

So 0 of 6 → 6 of 6 reproduces **both ways** (driver and independent in-place deletion), at both
endpoints, and the records rev behaves like the claims rev.

## Findings

1. No defect found in C2's counter or statement within my scope. Q25 is satisfied: the counter is
   shown able to fail (exit 1, `killed 0 of 6` at base; independent base deletions all survive).
2. Q26 direction is safe: the driver's kill rule (exit exactly 1, stdout `boxes proven 1|0`, stderr
   naming the deleted case's conjunct) is strictly stricter than the statement's bare "exit 1", so
   `killed 6 of 6` cannot pass while the statement fails. My independent run confirmed all three
   kill conditions hold per case, and that the stderr names the conjunct from observed coverage.
3. The denominator is honest: the instrument itself pins the same six conjuncts in `CONJUNCTS`
   (`verifiers/verify_dispatch_prompts.py:122-127`, `ALLOWED_CO_FAIL` for the one co-failure pair,
   coverage read from observed statuses at lines 55-65), and the 542f5156 manifest holds exactly
   those six `expect_conjunct_status: FAIL` cases plus 2 controls and 1 N/A — matching the driver's
   pinned denominator rather than trusting the manifest (the re-sizing rule in
   `plans/round-50.md:80-84`).
4. The in-place form I used is stronger than the driver's `--fixtures` redirect and agrees with it:
   the instrument demonstrably reads the manifest from disk and fails the box when an entry is gone.
5. Residual (outside my scope, noted for the wave): at 542f5156 deleting a must-pass control
   (`d04-control`, `d08-control`) or the N/A case (`d08-missing-state`) also exits 1 (driver lines
   `control d04-control: exit 1 killed`, etc.) — coverage enforcement is whole-manifest, consistent
   with the manifest `note`; C2's statement does not cover those deletions and the driver scores them
   outside the six, so no over- or under-count enters `killed K of 6`.

## Evidence (commands → result)

- `python3 -B verifiers/box_proof_case_deletion.py --rev f3046466…` → stdout 12 lines ending
  `killed 0 of 6`, exit 1 (full transcript above, §1).
- `python3 -B verifiers/box_proof_case_deletion.py --rev 542f5156…` → `killed 6 of 6`, exit 0.
- `python3 -B verifiers/box_proof_case_deletion.py --rev 956ee167…` → `killed 6 of 6`, exit 0.
- `python3 -B ind/run_deletions.py` (542f5156 export, in-place deletions) → intact exit 0;
  6 deletions → 6 × exit 1, `boxes proven 1`, conjunct-named stderr; script exit 0.
- `python3 -B ind-base/run_deletions.py` (f3046466 export) → intact exit 0; 6 deletions → 6 × exit 0,
  `boxes proven 2`, empty stderr; script exit 0.
- Scratch harness and exports retained under `/fast/scratch/hyaku/kotoba-r50/falsify/ReplayC2Counter/`
  (`ind/pristine`, `ind-base/pristine`, `ind/del-<case>/`, `ind-base/del-<case>/`).
- No writes to the lane besides this Report file; no git/jj write commands; no tool installs.
