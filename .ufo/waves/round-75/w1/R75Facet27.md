# R75Facet27 — description-audit candidate

## Candidate: trigger-eval advice has a narrow but concrete boundary condition

**Observed (committed source text):** `SKILL.md:193` tells authors to keep trigger-query strings unique and runs × threshold non-integral, explaining that the guide says “above” while `run_eval.py` uses `>=`. The linked knowledge entry gives the underlying distinctions and caveats: `corpus/knowledge/skill-eval-artefacts-round70.md:58-72` identifies the boundary disagreement as one-way (the implementation passes, guide wording fails), states 3 runs at threshold .5 cannot yield equality for a singly listed query, and explains duplicate strings aggregate runs per string (`:67-72`). Its scope refusal is explicit: it makes no claim that clients natively run the artefact (`:76-82`).

**Assessment / inference:** The advice is well-scoped to the two cited sources and the measured implementation, and is falsifiable at a boundary value. But its wording compresses the condition: uniqueness alone does not eliminate equality at other threshold/run combinations; the adjacent “runs × threshold non-integral” condition does. The entry correctly exposes this nuance. The greater audit risk is provenance of the implementation fact: entry source row S211 is pinned to a Git tree and script lines (`:3`), whereas a description audit must re-open those committed bytes rather than treat the entry's line references as current facts. This is an audit candidate, not evidence of a defect.

**Concrete check/control:** From the report's pinned revision, inspect the committed S211 snapshot and its cited branch around lines 213–234 and defaults 266–267; run a tiny local truth-table over `rate = successes/runs` at the guide threshold to show `>` versus `>=` at equality. Include (a) 3 runs, .5 threshold, one occurrence (no equality), (b) 2 runs, .5 (one-half equality), and (c) duplicate query rows aggregated by `run_eval.py`. Freeze the exact source revision and inputs in the receipt; separately verify the advice's uniqueness/threshold condition against entry lines 62–72. This tests the stated boundary without asserting any client executes the format.

**Evidence pointers:** `SKILL.md:193`; `corpus/knowledge/skill-eval-artefacts-round70.md:3,58-72,76-82`. Source-derived statements above are observations of committed text; evaluation of audit risk and proposed control are inference.

Report trailer paths (relative to `kotoba-shokunin`): `.ufo/waves/round-75/w1/R75Facet27.md`
