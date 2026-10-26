# Attack 42 — trigger-eval calibration boundary

**Axes:** factual support, falsifiability, scope, control operability.

## Verdict

The central arithmetic distinction survives this attack as a bounded statement about the cited guide/reference implementation. I found no evidence here that it is a defect in a current description evaluation or that the proposed control has actually been run. The report correctly marks those limits; its actionable claim is only a candidate evaluation control, not measured performance.

## Independent evidence and countercheck

Reopened `corpus/knowledge/skill-eval-artefacts-round70.md:58-72`: it states guide `>` versus `run_eval.py >=` for should-trigger, `<` for should-not-trigger, the three-run default, and per-query-string denominator. Exact arithmetic supports the examples: 1/2 = 0.5, and a duplicated query receiving 3 fires out of 6 total runs also yields 0.5; for three runs, thresholds 1/3 and 2/3 are attainable. Thus the two should-trigger rules differ at equality, while should-not-trigger equality fails the strict-below condition. This is not evidence of a universal pass definition: the same entry explicitly limits scope to guides and one reference implementation (`:74-77`). The cited S210 snapshot independently says to hold the split fixed, exclude validation failures from edits, and select by validation pass rate (`.ufo/waves/round-70/snapshots/S210-optimizing-descriptions.md:142-161`).

No safe execution of `run_eval.py` was undertaken: the facet supplies no frozen description/query fixture or results, and this review did not locate/reopen the implementation source itself. Consequently the knowledge entry's attribution and implementation behavior are not independently source-verified in this attack; only its committed assertion and the arithmetic were checked. No specific skill's quality, overfitting, or observed disagreement is established.

## Control attack and smallest correction

The proposed equality test is discriminating if the stated rates are presented as inputs/results: at should-trigger rate 0.5, `>` rejects and `>=` accepts; at should-not-trigger equality, `<` rejects. But a duplicate query under 3 runs is only exact equality if the combined duplicate occurrences actually yield 3 firings in 6 runs; duplication alone does not guarantee it. Likewise, freezing test inputs is useful, but the report should not imply a performance claim absent an actual receipt. Smallest safe correction: retain the proposed control, explicitly construct and record the counts (1/2 or 3/6), and label it a rule-conformance check unless a frozen evaluation receipt exists. No lane-source edits made.

Report trailer: `Attack 42; independently reopened committed knowledge and S210 snapshot bytes; arithmetic checked, no runtime/source execution, live fetch, or source mutation.`