# R75Facet21 — threshold advice is not a complete calibration recipe

**Facet:** `SKILL.md:193`, the trigger-evaluation clause advising “keep runs × threshold non-integral and query strings unique.” Candidate axis: calibration/depth. This is a distinct rule-level audit, not a conclusion about the historical r74 plan or a frozen r75 claim.

## Observed

- `corpus/knowledge/skill-eval-artefacts-round70.md:13-16` explicitly scopes S212/S213 as authoring guides, not normative specification rules; lines 33-34 distinguish guide wording (“above”) from `run_eval.py`'s `>=` behavior. This is carefully qualified advice, not a vendor requirement.
- The committed S213 snapshot describes threshold behavior at `.ufo/waves/round-70/snapshots/S210-optimizing-descriptions.md:88-93`: repeated runs estimate a trigger rate; 3 is a “reasonable starting point”; threshold 0.5 is a “reasonable default”; should-trigger is above threshold and should-not-trigger below.
- Same snapshot recommends fixed train/validation partitions with proportional positive/negative mix (`:136-147`), only train failures guiding edits (`:151-160`), choosing by validation pass rate (`:161`), and fresh queries as an honest generalization check (`:171-175`).
- The S211 implementation groups results by query string before computing `sum(triggers) / len(triggers)`, then uses `>=` for positives and `<` for negatives (`.ufo/waves/round-70/snapshots/S211-run_eval.py.txt:213-234`). Defaults are 3 runs and threshold 0.5 (`:264-268`). Thus exact-threshold ambiguity exists for positive queries; the S213 wording and implementation differ at equality.
- The evidence entry gives a useful concrete explanation: with one unique query and 3 runs, rate 0.5 is impossible; duplicated strings can aggregate runs, and other thresholds can make equality reachable (`corpus/knowledge/skill-eval-artefacts-round70.md:58-72`). The duplication warning is evidence-specific to this implementation's grouping behavior, not a general client protocol.
- The current skill compresses the evidence into one operational sentence at `SKILL.md:193`; it does not state that the threshold convention itself is an implementation choice, nor mention validation/fresh-query protection in that same recommendation.

## Assessment / inference

**Supported and falsifiable, but narrowly scoped.** The equality discrepancy and recommended non-integral product have direct committed-source support. This is a good description-audit candidate because an auditor can test the exact boundary case, not merely judge whether prose sounds calibrated. It should remain explicitly advice about the cited guide/reference pair, not a universal prescription: clients may have different counters or boundary conventions. [INFERENCE] Treating unique query strings as a general description-eval quality requirement would overstate what these sources establish; the duplicate-string risk here follows from S211's grouping implementation.

**Calibration risk:** “keep runs × threshold non-integral” avoids the exact equality edge only for the relevant discrete scoring denominator and threshold. It does not establish that three runs are statistically adequate, that query labels are valid, that the chosen threshold is useful, or that a description generalizes. S213 itself cautions against overfitting and supplies validation/fresh-query controls. A calibration assessment should not score the arithmetic guard as a complete evaluation methodology.

## Concrete control

Use a source-pinned equality boundary fixture against the committed S211 implementation: one `should_trigger=true` query with an even run count and exactly half successful invocations must pass S211 (`>=`) while being classified as not passing under the guide's strict “above” wording; pair it with a negative query at equality, which must fail under both (`<`). Also test the one-query/3-run case (no equality possible) and repeated identical query strings (implementation aggregates by string). Record the two classifications separately; do not silently call one normative. For any claimed description improvement, additionally freeze a stratified train/validation split and reserve fresh held-out queries per S213 `:140-161,171-175`; report those results separately from the boundary-control result.

## Limits and evidence method

Observed bytes are the committed repository snapshots and files named above. No LSP device/server was available in the supplied tool inventory, so semantic navigation was unavailable; this report uses literal file/line evidence and direct source reading, not grep as semantic proof. No live fetch, experiments, or edits were performed. The r74 spot-check at `corpus/lessons/round-74-verifier-spotcheck.md:15-19` explicitly says r74 gates were not executed, and its axis table at `:96-108` marks calibration unchanged; the present finding is not a claim that r74 or r75 validated this control.

## Report trailer

- Facet: 21 — trigger threshold calibration guidance.
- Evidence: `SKILL.md:193`; `corpus/knowledge/skill-eval-artefacts-round70.md:13-16,33-34,58-72`; `.ufo/waves/round-70/snapshots/S210-optimizing-descriptions.md:88-93,136-161,171-175`; `.ufo/waves/round-70/snapshots/S211-run_eval.py.txt:213-234,264-268`; `corpus/lessons/round-74-verifier-spotcheck.md:15-19,96-108`.
- Check/control: equality boundary fixture plus stratified held-out validation/fresh query evaluation, as specified above.
- Remaining unknown: client-specific trigger counters outside S211 and whether a prospective r75 experiment would use the same implementation.
