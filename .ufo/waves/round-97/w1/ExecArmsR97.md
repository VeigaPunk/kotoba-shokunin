# ExecArmsR97 — C1 build: the dispatch-prompt self-test kills t01..t13

Seat: ExecArmsR97 (executor, wave r97-w1). Base: `148395bf42af97436b1b832a97a175515f981939`
(the round-97 freeze commit). Candidate commit (scratch clone only):
`ac7a00f5c570b8a21702a961667ade86eacbd1ab`.
Scratch clone: `/fast/scratch/hyaku/kotoba-r97/ExecArmsR97/repo` (clone of the lane, shared, at the
freeze commit; `git rev-parse --show-toplevel` = that directory).

## Scope actually changed

One file, one contiguous insertion: `verifiers/verify_dispatch_prompts.py`, +231 lines, single hunk
`@@ -1102,0 +1103,231 @@ def self_test() -> int:`. Nothing else in the candidate commit
(`git diff --name-only 148395bf..HEAD` → `verifiers/verify_dispatch_prompts.py`).

Byte-identity proven, not asserted (`production-identity.txt`): the candidate reconstructs exactly as
`base[:p] + insertion + base[-s:]` (`reconstructs exactly: True`), `base` is the candidate minus the
insertion (`True`), the insertion lies after `def self_test() -> int:` and before the self-test tail
`for f in failures:`, and the inserted text has **0** lines at column 0 (so it defines nothing at
module scope; the only new helper, `lane_case`, is nested inside `self_test()`). The module docstring
through `run_checks()` and `box_proof()`/`main()` are therefore unchanged.

## The arms (27 new `rec(...)` assertions; honest 78 → 105 assertions)

Every arm calls a production helper on a temporary fixture input and reads the observed result —
`evaluate_dispatch_04` / `evaluate_dispatch_08` / `report_paths` / `role_round` / `has_placeholder` /
`lane_kind` / `state_source`. No arm reads this file's source, so the anti-sniffing rule holds.

| frozen survivor | arm (observed behaviour) |
|---|---|
| t01-rstrip-dot | `report_paths("Write it at .ufo/reports/round-7/kote.md. Then stop.")` → `[(7,'kote')]`; the dispatch.04 stem conjunct PASS and the file PASS |
| t02-empty-baseline | an empty `<lane>.report-baseline` → `state_source` state `none`; `round_le_latest_dispatched` N/A; file not PASS |
| t03-fleetroot-stem-pass | fleet-root role (state file, no `<lane>-shokunin` repo), report stem `kote-summary` ≠ lane → `report_stem_is_lane_id` N/A; file not PASS |
| t04-fleetroot-no-baseline | `lane_kind` with only `kote.report-baseline` → `fleet-root-role`; `lane_identity_known` PASS |
| t05-placeholder-empty-angle | `has_placeholder("kote<>")` is True; a stem `kote<>` → `report_path_literal` FAIL |
| t06-sibling-file-as-lane | `kote-shokunin` is a plain **file** → `lane_kind` `fleet-root-role` (not `sibling-lane`); dispatch.04 file not PASS |
| t07-report-regex-noprefix | `report_paths(".ufo/reports/7/kote.md")` → `[]`; a prompt whose only path lacks `round-` has no report path, file not PASS |
| t08-role-regex-nospace | `role_round("… round7 of up to 1024.")` is None; `filename_role_round_equal` FAIL |
| t09-file-note-dropped | a file with no report path carries `note == "no report path found"` |
| t10-unreadable-as-baseline | a mode-000 baseline → `state_source` state `none`; `round_le_latest_dispatched` N/A (root runs record the arm instead of crashing) |
| t11-lane-kind-legacy-dropped | `lane_kind` with only legacy `kote.round` → `fleet-root-role`; `lane_identity_known` PASS |
| t12-finish-single-fail-na | one failing file beside one passing file → `evaluate_dispatch_08(...)["status"] == "FAIL"`, evaluated 2 |
| t13-noreport-08-pass | a file with no report path → dispatch.08 file verdict N/A and `filename_report_dir_round_equal` N/A |

The positive control `p00-md-not-stripped` stays killed by the pre-existing
`report_paths keeps an absolute report path` arm (and by the box-proof corpus arms).

## Retained evidence (commands and observed lines)

1. Honest self-test, candidate (`selftest.txt`):
   `python3 -B verifiers/verify_dispatch_prompts.py --self-test` → `0 failure(s) over 105 assertions`,
   rc 0.
2. Box proof, candidate (`boxproof.txt`): `python3 -B verifiers/verify_dispatch_prompts.py --box-proof`
   → `boxes proven 2`, rc 0.
3. Frozen anchors (`anchors.txt`): every anchor of `CLAIMS["c1"]` and `CLAIMS["r96c1"]` (targets and
   positive) matches exactly its expected count in the candidate — `anchor mismatches: 0`. So no new
   code contains an anchor text verbatim, and the mutated statements keep their line count.
4. Local differential sweep (`sweep.txt`, debug aid, not the authority): each of the thirteen mutants
   run from the candidate bytes in a repo-shaped copy → rc 1 with a `self-test FAIL: ` line naming its
   own arm (`t01-rstrip-dot` … `t13-noreport-08-pass`); `mutants without a reported failure: 0`.
5. Frozen v5 counter, c1 (`c1-counter.txt`): `C1 targets killed 13 of 13 (run errors 0); positive
   killed 1 of 1; honest CLEAN; comment decoys held 13 of 13; code decoys held 13 of 13`,
   `rules v5: honest runs CLEAN 3 of 3; mirror runs reported 14 of 14; seed 35748dccbbc61dd5`,
   `C1-PREDICATE-MET`, rc 0.
6. Positive controls on the same candidate (`r96c1-counter.txt`, `r95c1-counter.txt`):
   `R96C1 targets killed 11 of 11 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys
   held 11 of 11; code decoys held 11 of 11` / `R96C1-PREDICATE-MET` rc 0, and
   `R95C1 targets killed 3 of 3 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys
   held 3 of 3; code decoys held 3 of 3` / `R95C1-PREDICATE-MET` rc 0 — v5 does not refuse honest arms.
7. Patch (`ExecArmsR97.patch`, sha256 `22638a4e8a81cc8fabf1760660d5908ed40d8a0a5e4b9d09212d7c87d8973c80`,
   242 lines, one `diff --git`): `git -C <fresh clone at 148395bf> apply --check` → `APPLY-CHECK-OK`,
   and after applying, the file is byte-equal to the candidate (`APPLIED-BYTES-EQUAL`); the second
   clone was removed.

## Findings

**F1 (the claim, met).** The frozen v5 counter at the candidate commit reads, on `c1`:

```
mutant t01-rstrip-dot … t13-noreport-08-pass  blind REPORTED-FAILURE mirror REPORTED-FAILURE: KILLED
positive p00-md-not-stripped                  blind REPORTED-FAILURE mirror REPORTED-FAILURE: KILLED
C1 targets killed 13 of 13 (run errors 0); positive killed 1 of 1; honest CLEAN;
comment decoys held 13 of 13; code decoys held 13 of 13
rules v5: honest runs CLEAN 3 of 3; mirror runs reported 14 of 14; seed 35748dccbbc61dd5
C1-PREDICATE-MET
```

rc 0. Every target is a reported failure in **both** the source-blind and the mirror run (no
RUN-ERROR), all three honest runs read `0 failure(s) over 105 assertions`, and all 26 decoys hold
CLEAN — so the arms observe behaviour, not the file's text.

**F2 (the arms are per-survivor, as the claim scopes them).** Each arm is anchored on one frozen
mutant's input shape. Two mutants (`t03`, `t04`) also trip the `t06` lane-kind arm because they change
the same classifier; that is a reported failure either way and does not weaken the kill. The
neighbouring edge of each function stays unobserved — the round-96 F1 coverage bound applies unchanged.

**F3 (root-mode bound, disclosed).** `t10` needs a mode-000 baseline to be unreadable. As uid 1000 it
is; under a root run the arm is recorded as a passing assertion instead of crashing (the item's
instruction), which means that one arm would not kill `t10` there. The counter runs as the invoking
user, so the measured reading is unaffected.

**F4 (no production change).** The insertion is entirely inside `self_test()` (0 lines at column 0,
`production-identity.txt`), so the live-run verdicts over the fleet prompts cannot move: the patch
cannot reach `run_checks()`.

## Bounds and risks

- The arms are per-survivor, anchored on each frozen mutant's input shape, exactly as the plan's C1
  target specifies: the neighbouring edge of the same function stays unobserved (the round-96 F1
  coverage finding applies unchanged to this set).
- `t10` depends on the run not being root: as uid 1000 the mode-000 baseline is unreadable; under a
  root run the arm is recorded as a passing assertion instead of crashing, so the mutant would survive
  that one arm there. The counter runs as the invoking user (uid 1000 here).
- The `t03`/`t04` mutants also trip the `t06` arm (they change `lane_kind`'s classification); that is a
  reported failure either way and does not weaken the kill.
- No production behaviour changed, so the live-run verdicts over the fleet prompts are unchanged by
  construction (the patch cannot reach `run_checks()`).

## Tool installs

None. No package, binary or network access was needed.
