# R75Attack38 — independent falsification of R75Facet38

## Verdict
Finding survives in the narrow form stated: the cited C2 row establishes a folded-frontmatter length and literal lane-name coverage, plus the counter's outcomes; it does not report semantic prompt-routing accuracy. However, the proposed additional semantic audit is not demonstrated necessary for the existing claim: this report finds no evidence that round 74 claimed sourced depth or calibration from C2. The proposal is actionable only as a future claim-specific requirement, not an identified defect in the measured result.

## Axes
- **Consistency:** survives narrowly. The C2 row is structural and not semantically calibrated evidence.
- **Operability:** proposal is implementable, but not yet an existing failure or directly load-bearing to C2's stated predicate.

## Independent evidence
At lane HEAD `65a5c7a663249e0522cc49e4a148424200d9ddfe`, reopened `corpus/lessons/round-74-verifier-spotcheck.md:76-77`: line 76 explicitly says the description was 1,021 chars under a 1,024 cap and names all ten non-`none` lanes; line 77 reports counter outcomes (`0 of 20` failed, `20 of 20` passed, carry-forward `20 of 20`, 47 assertions). These are directly observable structural/count and counter results, not a route-quality measure.

The nearby `:58-64` documents a distinct page-fidelity reviewer judgement for C1 and closes with “coverage `improved`”; it does not establish that semantic description routing was claimed. The cited `plans/round-74.md:121-131` defines C2 as an adjacent-lane census/re-pin predicate (row checks, commit ancestry, and diff recomputation), not the semantic audit proposed here. `SKILL.md:3-18` does contain triggers, anti-triggers, and sibling ownership boundaries, but those source bytes alone do not measure prompt classification outcomes.

The current worktree has uncommitted changes (including `SKILL.md`, round-75 corpus/plan and `.ufo`); I treated those as user evidence and made no lane changes. The cited revision matches HEAD; no live fetch or runtime check was needed.

## Attack on proposed control
The prompt-set and mutation test could be useful for a future claim specifically about route precision/recall. But the control is underspecified as a falsification of this report's current structural claim: it says detect a changed route **or failed criterion**, allowing a textual criterion failure to count without any changed observed route. It also gives no route implementation/oracle or fixed acceptance threshold; reviewers classify expected routes, while “observed routing” is not defined by the cited C2 counter. Without that binding, a small handpicked set can yield a passing audit without proving general quality, and the proposed bounded conclusion correctly must not generalize beyond the set.

Smallest safe correction: retain the conclusion as an evidence-boundary caveat, but require the semantic audit only before asserting semantic routing quality (not before making the already-measured C2 structural/freshness claim). Make the must-fail mutation criterion require a predetermined case's observed route/expected-route result to flip or fail, not merely a textual criterion change; name the router/oracle and freeze the acceptance rule before testing.

## Report trailer
Report path: `.ufo/waves/round-75/w2/R75Attack38.md`
