# R75Facet35 — calibration rule evidence

## Finding

**Observed:** `SKILL.md:193` compresses the guide/reference threshold disagreement into an operational instruction: keep `runs × threshold` non-integral and query strings unique. The cited entry explicitly grounds the distinction as documentary guidance, not a normative spec rule (`corpus/knowledge/skill-eval-artefacts-round70.md:11-16`), and records guide “above” versus implementation `>=` (`:33-34,58-72`). Its explanation says the default 3 runs at threshold 0.5 cannot yield exactly 0.5 for one unique query, but duplicate query strings aggregate to six runs and can (`:62-70`).

**Assessment:** This is a concrete, falsifiable calibration safeguard, but its stated arithmetic is only a sufficient condition and can be read too broadly. The entry correctly explains duplicate-string aggregation; the SKILL sentence's “keep runs × threshold non-integral and query strings unique” makes it actionable, but does not state that query deduplication is scoped to the trigger set as actually consumed by the implementation, nor that the threshold/run product must be evaluated after any per-query aggregation. It also covers only equality cases; it does not make guide and implementation semantics otherwise equivalent. The entry does distinguish the single direction of disagreement (`:70`) and gives the alternative of explicitly stating which rule the report applies (`:71-72`).

## Concrete check/control

For any proposed description-eval report relying on this rule, record the implementation's actual denominator per evaluated query string and its configured threshold; compute `threshold × denominator`. If integral, construct a real trigger set with that query's fire count equal to the product and show the guide-wording verdict (`rate > threshold`) beside the implementation verdict (`rate >= threshold`). Include both a unique-query case and a duplicate-string case (the entry's described 3-run/0.5 and aggregated 6-run/0.5 cases); require the report to declare which verdict it uses. This tests the calibration claim on actual aggregation semantics instead of treating the nominal CLI run count as denominator.

**Inference / risk:** If the implementation's aggregation or query deduplication differs from the described `run_eval.py` behaviour, the shortcut could be miscalibrated; no runtime experiment was performed for this facet. The cited entry claims source evidence from a pinned implementation and describes aggregation at `:67-70`, but the committed source bytes themselves were not independently re-opened here. Confidence: medium-high for what the committed prose asserts; medium for operational generalization beyond that cited implementation.

## Evidence boundary

Read-only source locations: `SKILL.md:193`; `corpus/knowledge/skill-eval-artefacts-round70.md:11-16,33-34,56-72`; historical plan `plans/round-74.md:63-99` explicitly assigns semantic truth to non-author judgment, and the closure says round-74 depth had no declared claim (`corpus/lessons/round-74-verifier-spotcheck.md:96-105`). The r74 plan is historical context, not evidence of a frozen r75 claim. No edits, installs, live fetches, or experiments.
