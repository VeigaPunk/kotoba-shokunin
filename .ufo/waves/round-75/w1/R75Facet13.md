# R75Facet13 — sourced-depth/calibration candidate

## Finding (observed)

`corpus/lessons/round-74-verifier-spotcheck.md:127-130` calls **quality: improved**, citing (a) 15/20 stale pins at base, (b) 20/20 re-pinned rows, (c) 8/8 sampled quote locations, and (d) one corrected classification. It also explicitly notes the lane self-graded unchanged and that the outside re-check supplied verification. This is a concrete but bounded freshness/re-verification result; it is not direct evidence that the description is more factually accurate in general.

Relevant scope boundary: `corpus/knowledge/skill-eval-artefacts-round70.md:18-21,31-32` distinguishes machine-checkable output/trigger evaluations from judgments such as style and whether output “feels right,” reserved for human review. Thus a future description-audit claim should separate countable checks (source/quote/line, factual assertions mapped to evidence) from reviewer judgments; a counter alone cannot establish semantic truth.

A useful explicit boundary is in the historical plan `plans/round-74.md:98-100`: it says the C1 counter counts forms/sources/tokens but whether a rule sentence is true of the page is reviewer judgment, assigned to named non-author wave-2 seats. This is historical r74 design, not a frozen r75 claim. It provides a defensible pattern for a description audit: enumerate each factual clause, map it to source bytes/line, and have independent reviewers assess entailment and scope; report mechanical coverage separately from semantic verdict.

## Candidate check/control

Use a clause-level evidence matrix for one chosen description paragraph: split into atomic factual clauses; for every clause record source URL/committed snapshot hash, exact line/span and whether the source supports the same scope/modality. Include negative controls by replacing a supported clause with (1) a true quote from a sibling page, and (2) an over-broad paraphrase of the correct source. The mechanical check should reject the wrong-page citation/hash; named non-author reviewers judge entailment and scope. Score only that paragraph and those clauses, not whole-skill quality. This directly targets the distinction at `skill-eval-artefacts-round70.md:31-32` and plan precedent `round-74.md:98-100`.

## Calibration/risk

The r74 spot-check's 8/8 quote-location sample is explicitly a sample (`round-74-verifier-spotcheck.md:74`), not exhaustive semantic review. Do not generalize it to every row or to description truth. Also, the lesson's “quality” label at lines 127-130 aggregates pin freshness, quote location, and one classification correction; an r75 description audit should label its own measured construct (e.g. clause-level source entailment) rather than inheriting “quality improved.”

Confidence: high for the stated r74 observation and the cited methodological distinction; moderate for the proposed control as a suitable r75 design, since no r75 target paragraph/claim has been frozen in the examined files. Remaining unknown: which exact current description paragraph r75 intends to assess, and its source snapshot set.

## Evidence commands

- `read corpus/lessons/round-74-verifier-spotcheck.md:127-130`
- `read corpus/knowledge/skill-eval-artefacts-round70.md:18-21,31-32`
- `read plans/round-74.md:98-100`

Report: `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-75/w1/R75Facet13.md`
