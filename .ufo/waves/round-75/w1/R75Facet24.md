# R75Facet24 — sourced-depth/calibration candidate

## Finding: SKILL.md trigger-evaluation advice is bounded, but its operational safeguard is not independently demonstrated

**Observed (committed source rows):** `SKILL.md:193` says trigger sets label about 20 queries, run about 3 times, and suggests unique query strings/non-integral threshold×runs to avoid disagreement between the guide's strict `above` wording and `run_eval.py`'s `>=`. The cited knowledge entry explicitly marks these as guide advice, not normative rules (`corpus/knowledge/skill-eval-artefacts-round70.md:11-21`); it records the guide/implementation discrepancy and its arithmetic, including duplicate strings being aggregated per query string (`:56-72`). Thus the recommendation is calibrated as an operational choice, not attributed as a universal spec requirement.

**Control weakness / inference:** the text presents uniqueness or non-integral threshold×runs as sufficient ways to avoid the specific equality disagreement, but there is no stated guard at this point that tests the actual query-set/run configuration or catches a later change to either. The source entry's fact table records the equality behavior (`:33-34`), while its action is prose (`:71-72`). This is a plausible description-audit target: the cited semantics are falsifiable, but the safeguard's continued applicability is not counter-enforced. The entry also says duplicate query strings aggregate (`:67-69`), so uniqueness matters even when default runs are three.

**Concrete check/control:** audit the pinned `run_eval.py` pass/fail branch and per-query denominator at the recorded commit (S211), then use a tiny committed control matrix: unique query with default 3 runs; duplicate query string yielding 6 observations; and an even run count with exactly half firing. Assert the reported pass/fail under both guide wording (`> threshold`) and implementation (`>= threshold`). Keep the resulting recommendation explicitly scoped to that implementation and chosen threshold/run count; do not treat the guide's suggested 0.5/20/3 values as normative. The knowledge entry already documents the source lines/logic and a 90-day recheck command (`corpus/knowledge/skill-eval-artefacts-round70.md:1-8,56-72`); no live fetch or runtime experiment was performed here.

**Unresolved:** I did not independently reopen the snapshot file or execute the verifier/implementation. The conclusion is grounded in the committed knowledge entry and `SKILL.md`, not a fresh source-byte reproduction. Confidence: moderate for identifying a candidate/control gap; source behavior itself remains to be independently rechecked.

## Report trailer

- Scope: one paragraph/rule, SKILL.md:193.
- No edits outside this report; no installs.
- Evidence paths are relative to kotoba-shokunin.