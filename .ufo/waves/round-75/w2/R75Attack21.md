# R75Attack21 — independent falsification of R75Facet21

## Verdict: survived, with a narrow actionable scope

The factual discrepancy survives inspection at the measured repository revision `65a5c7a`: the guide's strict “above” wording and S211's `>=` classify positive-query equality differently. The skill's current sentence is already carefully scoped as “guide advice level,” and explicitly tells the reader to name the comparator when reporting a boundary result. The facet's core concern is therefore not a demonstrated defect in the current sentence; its own report identifies an arithmetic guardrail and a useful test, but does not establish that the skill claims a complete calibration methodology.

## Evidence reopened

- `SKILL.md:193` says “Keep runs × threshold non-integral and query strings unique” and directly identifies the guides as advice-level, cites the source artifact, and instructs naming the comparator for a boundary result. This is not phrased as a normative universal prescription. (Full line is available via `read` selector `:raw:193-193`.)
- `.ufo/waves/round-70/snapshots/S210-optimizing-descriptions.md:90-93` recommends repeated runs and says positive queries pass “above” the threshold; negatives pass below. It calls 3 runs and 0.5 reasonable starting/default values.
- `.ufo/waves/round-70/snapshots/S211-run_eval.py.txt:213-234` groups outcomes by query string, computes per-string rate, uses `>=` for positives and `<` for negatives. `:266-267` gives defaults of 3 runs and threshold 0.5.
- `corpus/knowledge/skill-eval-artefacts-round70.md:13-16,58-72` explicitly treats sources as guides, not specification; it explains the equality gap, default 3-run limitation, duplicates, and arithmetic mitigation. Its `:71-72` action is consistent with the current skill sentence.
- S210 separately recommends fixed stratified train/validation partitions and held-out fresh queries (`:136-161,171-175`). Those are sound additional methodology, but their omission from this one operational bullet does not show it purports to be a complete calibration recipe; the facet itself describes the sentence as a compressed piece of “operational” advice.

## Attack and control assessment

The proposed equality fixture is non-vacuous as a source-level arithmetic check: 2 runs with one positive result yield rate 0.5, which passes S211 (`>=`) and fails S210's literal “above”; a negative equality case fails in both. With 3 runs and threshold 0.5, equality is unreachable for one query string, while duplicate strings aggregate outcomes under S211. This follows directly from the inspected implementation. No model invocation or external runner was executed; the proposed fixture's behavioral premise is established by source arithmetic, not an executed command.

The proposed broader validation/fresh-query controls are useful when evaluating an actual description change, but are not necessary to resolve this comparator discrepancy. No evidence supports elevating the non-integral guard to a claim of statistical sufficiency. Conversely, the report's “calibration risk” is a limitation of that guard, not evidence that the current skill sentence misleads: the bullet does not assert that the guard alone makes an evaluation adequate.

## Scope, evidence method, gaps

The measured revision was reported as `65a5c7a`. No source edits or live fetches were made. No LSP device was available in the tool inventory, so this review used literal committed source line evidence rather than semantic-navigation claims. The S211 command was not run; it invokes external client/model behavior, and source inspection plus the exact rate calculation suffices for the proposed boundary case. No actionable finding against the skill text remains established; the issue is an expressly bounded advice-level arithmetic caveat, with comparator disclosure already in the sentence.

## Report trailer

- Target: `.ufo/waves/round-75/w1/R75Facet21.md`.
- Verdict: equality discrepancy confirmed; no material defect in `SKILL.md:193` established.
- Evidence: `SKILL.md:193`; `.ufo/waves/round-70/snapshots/S210-optimizing-descriptions.md:90-93,136-161,171-175`; `.ufo/waves/round-70/snapshots/S211-run_eval.py.txt:213-234,266-267`; `corpus/knowledge/skill-eval-artefacts-round70.md:13-16,58-72`.
- Verification: source arithmetic only; no runner/model experiment or live fetch.
- Remaining risk: behavior of other clients/counters is outside this evidence and was not generalized.
