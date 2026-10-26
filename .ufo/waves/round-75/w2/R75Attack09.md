# R75Attack09 — independent falsification of R75Facet09

## Verdict: finding survives; proposed control is non-vacuous for this cited implementation

Central claim in R75Facet09: the adopted SKILL paragraph at `SKILL.md:193` accurately describes a real equality-boundary discrepancy between the Agent Skills guide wording (“above”) and the pinned reference `run_eval.py` (`>=`). The report itself disclosed that it had not independently opened S211/S213. I reopened the committed bytes at current measured `HEAD 65a5c7a663249e0522cc49e4a148424200d9ddfe`.

Evidence:
- `SKILL.md:193` says trigger rate must be above per guide, reference uses `>=`, names the comparator for boundary results, and recommends non-integral runs × threshold and unique query strings.
- `.ufo/waves/round-70/snapshots/S211-run_eval.py.txt:213-229` groups results by query string and computes `sum(triggers) / len(triggers)`; `:231-234` accepts should-trigger when `trigger_rate >= trigger_threshold`, and the inverse case uses `<`.
- S211 defaults at `:266-267` are 3 runs and threshold 0.5. For unique-query 3-run rates, equality at .5 is impossible (integer successes over 3); for 2 runs it is possible. Duplicate strings are combined by the dict keyed on query (`:213-220`), so two entries with the same query and 6 results can yield 3/6=.5. Threshold 1/3 with 3 runs likewise yields equality. Thus the report's suggested truth-table checks distinguish behavior and its constraints target the actual identified equality conditions, not an empty/vacuous claim.
- `.ufo/waves/round-70/snapshots/S213-optimizing-descriptions.md` is the committed guide snapshot referenced by the knowledge entry; the guide statement is recorded in `corpus/knowledge/skill-eval-artefacts-round70.md:33-34`, with source mapping S213 and S211 at `:1-6`. That entry explicitly limits itself to guide advice rather than normative specification (`:13-16`).

Scope/calibration: This supports only the stated comparison of the pinned guide and reference implementation, not universal client behavior. The target report explicitly sets that boundary and does not overclaim. The actionable control is to test/report equality using the comparator actually applied; its mitigation (non-integral product and unique query strings) does avoid equality for the cited default configuration. One caveat: unique query strings alone are insufficient if a chosen run count/threshold allows equality (e.g. 3 runs, threshold 1/3); SKILL's separate product constraint covers that case.

No actionable counterfinding identified. Verification gap: I did not execute `run_eval.py` against live model calls; unnecessary and unsafe for this source-level deterministic branch check. LSP device was unavailable (`xd://lsp` returned no such tool); evidence was checked directly against the committed snapshots and cited source text. No lane source changed.

## Residual risk

Snapshot provenance is the knowledge entry's pinned upstream metadata, not independently re-fetched live upstream content; live-fetch was unnecessary for the assigned committed-byte falsification.