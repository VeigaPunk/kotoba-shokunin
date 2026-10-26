# R75Attack30 — independent attack on R75Facet30

## Verdict
**Finding survived with a narrow calibration qualification; no material factual error found in the cited historical comparison.** The report properly limits the comparison to advice in a guide versus behavior of one reference implementation, not a normative specification or client behavior. The actionable risk is real only when an audit claims a particular pass rule or generalizes the reference comparator; the source itself already explicitly warns against that overstatement. The proposed equality arm is non-vacuous as a test of comparator behavior, though not evidence that any current audit has mis-scored a query.

## Independent evidence
At lane HEAD `65a5c7a663249e0522cc49e4a148424200d9ddfe`, the committed entry says S209/S210 are guides, not the specification, and numbers are advice (`corpus/knowledge/skill-eval-artefacts-round70.md:13-16`). It separately records S213's "above" wording and S211's `>=` (`:33-34`). The exact S210 snapshot says above at `.ufo/waves/round-70/snapshots/S210-optimizing-descriptions.md:90-93`; exact S211 snapshot computes rate at `:227-230` and uses `>=` for should-trigger and `<` for should-not-trigger at `:231-234`. Thus the entry's comparison is supported by pinned source bytes, not merely its own prose.

The reported safe controls target the actual edge: `:58-70` explains equality, and `:71-72` offers non-integral threshold×runs, unique query strings, or naming the applied rule. The implementation groups repeated identical query strings (`S211:214-225`) before scoring, so de-duplication addresses a real aggregation condition. The equality test is meaningful if an evaluator is being tested; odd runs at .5 avoid equality for a unique query, while duplicate aggregation or other thresholds can reintroduce it.

## Attack / qualification
The report's phrase “calibration overstatement” is a conditional risk, not an observed defect: the entry itself labels thresholds advisory (`:13-16`), calls 0.5 a suggested default (`:33`), and limits scope to guides plus one reference implementation (`:76-82`). It does not assert that a current description audit treated 0.5 or `>=` as universal. The proposed reporting fields (per-query rates, threshold, comparator) improve observability but cannot by themselves establish query-set representativeness or trigger-rate stability; the facet appropriately presents them as controls rather than proof of those properties. No concrete current misclassification is demonstrated.

Working-tree caveat: the knowledge entry is modified relative to HEAD (`git status --porcelain -- corpus/knowledge/skill-eval-artefacts-round70.md` prints ` M`), but `git show HEAD:<path>` hashes match the report's cited entry and snapshot hashes (entry `598655…`; S210 `7cc54f…`; S211 `43e3b8…`). Review above therefore uses pinned committed bytes, not the modified working-tree copy. LSP was unavailable (`read xd://lsp` returned “No such tool”); literal-source review only, not semantic reference analysis. No evaluator command was run: the control is a proposed test scenario, and executing the upstream snapshot was unnecessary to confirm the source comparison.

## Residual risk and verification gaps
No live upstream re-fetch; current upstream behavior beyond the recorded 2026-10-25 snapshots is unverified. No actual client or audit was exercised, so no present-day pass/fail consequence is established.

## Report trailer
- Facet: description-eval threshold calibration.
- Verdict: survived attack, scoped; conditional risk/control, no observed current defect.
- Paths: `corpus/knowledge/skill-eval-artefacts-round70.md`, `.ufo/waves/round-70/snapshots/S210-optimizing-descriptions.md`, `.ufo/waves/round-70/snapshots/S211-run_eval.py.txt`, `.ufo/waves/round-75/w1/R75Facet30.md`.
