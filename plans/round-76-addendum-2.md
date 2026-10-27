# Round 76 — addendum 2 (pre-data integration corrections)

Date: 2026-10-27. Author: L1 `KotobaR76`. This addendum corrects evidence and implementation defects found in the settled w1 wave before any claim data is committed. It does not change C1/C2 targets or their 6/4 conjunct counts.

## 1. Corrected base-gate evidence

`plans/round-76.md` § Base battery and `.ufo/waves/round-76/base-battery/base-battery.txt` claim corpus-integrity and independent gates exit 0. That exit capture is **withdrawn**: the command pipeline recorded `tail`'s exit status, not the gate process status. A direct run against the committed r76 base `b7f13f4b39cbd43076a85568adca763a6f674e7a` returns exit 1 for both gates. The corpus integrity drift is explained by the r75 closure spot-check added at `b7f13f4` without its README index row or a baseline refresh. A corrected receipt `.ufo/waves/round-76/base-battery/base-gate-correction.txt` must carry each command's direct stdout and its actual exit status. The final no-harm requirement remains: both corpus gates are green at the measured final tip, and the baseline/index are re-recorded to observed committed bytes. No base pass is claimed.

## 2. R2 exact-tip correction (same C2 target)

C2 R2 is the committed no-harm receipt for the final measured tip. The current `check_r75_routed_repairs.py` accepts any ancestor at or after the r75 tip, so A05 demonstrated a stale-revision receipt scored as `4 of 4` by the core fixture check. Correct the implementation—not the target—to require the receipt's first-line revision to equal the normalized measured `--rev` (`Repo.rev`), and retain the actual corpus-gate re-run at that exact revision. Add a self-test arm with a stale ancestor receipt and run the exact shortcut against the corrected core; it must leave R2 open. This is required to implement the plan's existing `noharm-at-tip` wording.

## 3. Q73 pin caused by the required D4 floors bump

B01PlanConsistency found `check_tip_battery.py` pins the byte identity of `verifiers/check_assertion_floors.py`; D4's required bump changes that blob and makes `check_tip_battery.py --rev <rev>` fail its `instrument-pin` guard (5/5 to 4/5). The `check_tip_battery.py` pin table therefore joins the round-76 touch list, and the exact reviewed D4 blob must be added to `INSTRUMENT_PINS` in the same landing. Run its self-test and `--rev` against base and final tip. The Q73 sweep conclusion in the original plan is superseded: the sweep found multiple guards, including this pin, not only `check_province_core.py`.

## 4. Append-only S213 used-by compatibility

C1 requires the permitted S213 `used-by` append from `corpus/knowledge/skill-eval-artefacts-round70.md` to include `corpus/knowledge/description-craft-round76.md`. B17's control showed the existing `check_skill_evals_v2.py` rejects any S213 `used-by` value other than the single r70 path (F7 exact-match rule), so the required SOURCES change would make that existing gate fail. Correct that gate to accept the exact r70 path as one comma-delimited member while preserving exact member matching (no substring/negation), and add a positive multi-member self-test plus retain the old-path and substring must-fail arms. Run the gate self-test and live `--rev` at the final tip. This is compatibility with the append-only registry contract; no source row is removed or rewritten outside the allowed `used-by` cell.

## 5. Predicate sentence and wave record

The plan's canonical C1/C2 sentence remains the one under each claim; the counter docstrings must quote those sentences verbatim (including the full base hash and `K of 6` / `K of 4` forms), and the SCORECARD rows and receipt labels must cite the same string. The validated role topology and 64-seat role counts are in addendum 1; the original § Wave shape paragraph's `30 build + 34 attack`, `labrat`, and `sonic` estimate is stale and is superseded by that measured dispatch mix.

## Reason/evidence

Observed before claim data: B01PlanConsistency §§1–3, A05RevControls §§2–3, B17LessonScribe §§1.4 and 3. The initial shell pipeline (`eval "$g" | tail -3; echo "$?"`) did not preserve the gate's return code; the corrected receipt uses direct commands without a pipeline. These are implementation/evidence corrections, not a changed claim target or post-data re-score.