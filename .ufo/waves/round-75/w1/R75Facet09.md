# R75Facet09 — sourced-depth candidate: skill description trigger evaluation

Axes examined: **depth** (whether an operator can apply the guidance) and **calibration/operability** (whether the advice is supported, bounded, and falsifiable).

## Finding

The distinct candidate is `SKILL.md:193`, specifically the trigger-set advice (“~20 queries”, “~3 runs”, threshold comparison, unique query strings). Its source pointer is `corpus/knowledge/skill-eval-artefacts-round70.md`, which explicitly distinguishes documentary guide advice from normative specification rules (`:13-16`), tabulates the trigger rule and reference implementation disagreement (`:33-34`), and scopes out native client execution claims (`:74-82`). The cited `S213` is the optimization guide; `S211` is the pinned `run_eval.py` implementation (artefact `:3,6`). This is a supported, bounded operational instruction rather than a claim that clients natively execute the artefact.

**Observed:** The local knowledge entry says the guide's should-trigger pass is strictly above threshold, while the reference code uses `>=`; it explains why the default three runs at threshold .5 cannot hit equality for one occurrence, and identifies duplicate-query and even-run/non-default-threshold cases (`skill-eval-artefacts-round70.md:56-72`). The SKILL instruction incorporates the mitigation (non-integral product, unique query strings) at `SKILL.md:193`. Round-74 plan and spotcheck do not independently validate this old rule: the plan declares C1/C2 on other surfaces (`plans/round-74.md:47-61`); the spotcheck lists its examined claims and axes at `round-74-verifier-spotcheck.md:44-64,96-108`.

**Inference:** The mitigation is falsifiable against the cited script's rate calculation and threshold branch, but it is configuration-sensitive: a single scalar rule does not itself establish that a future evaluator actually uses the cited defaults or deduplicates queries. This is a candidate for a description-audit claim only if framed as advice about the cited guide/reference pair, not as a universal client behavior or guaranteed audit outcome.

## Concrete control / check

Use committed bytes only. At a frozen revision, derive a tiny truth table directly from `S211`'s committed snapshot: one unique query with 3 runs and threshold .5 (rates 0, 1/3, 2/3, 1); two copies of the same query aggregated to 6 runs at .5 (3/6 equality); one unique query with 3 runs and threshold 1/3 (1/3 equality). Confirm expected pass/fail from the actual branch (`>=`) and compare with the guide's “above” wording in the committed S213 snapshot. Record the exact snapshot hash and source lines. A useful headline is limited to “the cited guide and cited reference implementation differ at equality”; do not claim the mitigation resolves arbitrary evaluator configurations without checking each configuration's run count, threshold, and duplicate aggregation.

## Evidence / confidence / gap

- `kotoba-shokunin/SKILL.md:193` — exact adopted advice and source pointer.
- `kotoba-shokunin/corpus/knowledge/skill-eval-artefacts-round70.md:13-16,33-34,56-72,74-82` — authority level, discrepancy, reasoning, and explicit scope boundary.
- `kotoba-shokunin/plans/round-74.md:47-61`; `kotoba-shokunin/corpus/lessons/round-74-verifier-spotcheck.md:44-64,96-108` — round-74 claims are distinct; do not treat that historical plan/spotcheck as a frozen r75 claim or corroboration of this paragraph.

Confidence: **high** for what the committed entry and SKILL paragraph state; **moderate** for the substantive discrepancy because this seat did not independently open the referenced snapshot/script bytes. Remaining gap: independently resolve S211/S213 snapshot paths and execute the truth-table derivation from those committed bytes before promoting this into a new claim.