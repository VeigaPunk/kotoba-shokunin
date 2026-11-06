# ExecArmsR96 — C1 build: the dispatch-prompt self-test kills t01..t11

Seat: ExecArmsR96 (executor, wave r96-w1). Base: `679775abb9277a7b8d17f060b0f5b4ced2b127b6`.
Candidate commit (scratch clone only): `443430a6cd84b0c1c56a5c92cebfda22aab40f7f`.
Scratch clone: `/fast/scratch/hyaku/kotoba-r96/ExecArmsR96/repo` (clone of the lane, shared, at the freeze commit).

## Scope actually changed

One file, one contiguous insertion: `verifiers/verify_dispatch_prompts.py`, +128 lines, single hunk
`@@ -799,0 +800,128 @@ def self_test() -> int:`. Nothing else in the candidate commit
(`git diff --name-only 679775ab..HEAD` → `verifiers/verify_dispatch_prompts.py`).

Byte-identity proven, not asserted (`production-identity.txt`): the candidate reconstructs exactly as
`base[:i] + insertion + base[i:]` (`True`), prefix and suffix byte-identical (`True`), insertion point
after `run_checks()` (base line 564) and after `def self_test` (base line 679), before `box_proof()`
(base line 985). So the module docstring through `run_checks()` and `box_proof()`/`main()` are unchanged.

## The arms (22 new `rec(...)` assertions; honest 56 → 78 assertions)

Every arm calls `evaluate_dispatch_04` / `evaluate_dispatch_08` on a temporary fixture tree and reads
the observed verdict/conjunct status — no arm reads this file's source.

| frozen survivor | arm (observed behaviour) |
|---|---|
| t01-var-dropped | report path `/round-7/${LANE}.md` → `report_path_literal` FAIL, file FAIL |
| t02-var-brace-only | report path `/round-7/$LANE.md` → `report_path_literal` FAIL, file FAIL |
| t03-var-bare-only | report path `/round-7/${LANE}.md` → `report_path_literal` FAIL, file FAIL |
| t04-le-to-lt | baseline `7`, prompt round 7 → `round_le_latest_dispatched` PASS, file PASS |
| t05-finish-allna-pass | all-N/A `dispatch.08` (no state) → check status N/A (not PASS), evaluated 1; no-report-path `dispatch.04` → evaluated 1 |
| t06-role-whole-text | round token only on a later line (line 1 has none) → `filename_role_round_equal` FAIL, file FAIL |
| t07-dirs-subset | report paths in round-7 and round-6 → `filename_report_dir_round_equal` FAIL |
| t08-bad-first-only | two report paths, second carries `<lane>` → `report_path_literal` FAIL |
| t09-wrong-first-only | stems `kote` + `other` (sorts after) → `report_stem_is_lane_id` FAIL |
| t10-nonint-baseline | baseline first field `abc` → `round_le_latest_dispatched` N/A, file N/A, check N/A |
| t11-noreport-04-pass | no report path → file N/A, all three `dispatch.04` conjuncts N/A, check N/A |

Both POSIX parameter-expansion forms are exercised separately (POSIX.1-2024 XCU 2.6.2, braces
optional), which is what separates t02 from t03.

## Retained evidence (commands and observed lines)

1. Honest self-test, candidate (`selftest.txt`):
   `python3 -B verifiers/verify_dispatch_prompts.py --self-test` → `0 failure(s) over 78 assertions`, rc 0.
2. Box proof, candidate (`boxproof.txt`): `python3 -B verifiers/verify_dispatch_prompts.py --box-proof`
   → `boxes proven 2`, rc 0.
3. Frozen counter, c1 (`c1-counter.txt`):
   `HYAKU_SCRATCH=/fast/scratch/hyaku/kotoba-r96/ExecArmsR96 python3 -B verifiers/fixtures/round-96/selftest-kills.py c1 443430a6cd84b0c1c56a5c92cebfda22aab40f7f /fast/scratch/hyaku/kotoba-r96/ExecArmsR96/repo`
   → `honest rc 0 CLEAN: 0 failure(s) over 78 assertions`;
   `mutant t01..t11 rc 1 KILLED` (11 of 11, failure counts 2,1,1,2,3,2,1,1,1,3,5);
   `positive p00-md-not-stripped rc 1 KILLED: 5 failure(s) over 78 assertions`;
   `comment decoy <t> rc 0 HELD` and `code decoy <t> rc 0 HELD` for all 11;
   summary `C1 targets killed 11 of 11 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 11 of 11; code decoys held 11 of 11`, `C1-PREDICATE-MET`, rc 0.
4. Positive control r95c1, candidate (`r95c1-counter.txt`):
   `HYAKU_SCRATCH=... python3 -B verifiers/fixtures/round-96/selftest-kills.py r95c1 443430a6cd84b0c1c56a5c92cebfda22aab40f7f /fast/scratch/hyaku/kotoba-r96/ExecArmsR96/repo`
   → `honest rc 0 CLEAN`; `n1-manifest-at-head`, `n5-label-targets-cne`, `n11-accept-plus-two` and
   `n10-accept-plus-one` all `rc 1 KILLED`; every comment/code decoy `rc 0 HELD`;
   `R95C1 targets killed 3 of 3 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 3 of 3; code decoys held 3 of 3`, `R95C1-PREDICATE-MET`, rc 0.
5. Patch applies at the freeze commit on a second fresh clone (`git apply --check` → `APPLY-CHECK-OK`),
   and the patched clone reads `0 failure(s) over 78 assertions` and `boxes proven 2`; clone removed.
6. Anchors: each of the eleven frozen anchor texts matches exactly once in the candidate and zero
   times inside the insertion (`production-identity.txt`); every mutated statement is 1 line → 1 line.
7. Patch: `.ufo/waves/round-96/w1/ExecArmsR96/ExecArmsR96.patch`,
   sha256 `799bbaac9485587900baeaee0291db2bc5beca97978ab773e2a2d5b770b73088`, 139 lines.

## Findings

- The pre-freeze sweep's 11 survivors are all killed by behavioural arms; the honest run stays CLEAN
  and both decoys hold for every target (the code decoy for t05 exercises the v4 elif-chain climb).
- Assertion count rises 56 → 78; the floors registry entry `dispatch_prompts` floor 56 is a floor, so
  it still holds (not raised here — raising it is not claimed).
- No counter, plan, builder, forgery patch or frozen predicate was touched; no lane write beyond this
  seat's receipts, patch, READY file and report.

## Risks / bounds

- Killing this frozen set does not show every mutant is killed (the sweep's other survivors — sentence-
  final `.` on a report path, empty baseline, fleet-root stem — are not in the set and are not claimed).
- The v3 code-object-sniffer bound is unchanged: a mutant that inspects its own compiled code objects
  and proves the decoy guard dead is still not caught.
- `--box-proof`'s docstring still lists the unproven clauses (unsubstituted variable, `<=` at equality,
  legacy-state arm, non-digit round folder). Those clauses are now covered by the self-test, not by the
  box proof; the docstring is outside my writable region (production text) and was left byte-identical.

## Tool installs

None.
