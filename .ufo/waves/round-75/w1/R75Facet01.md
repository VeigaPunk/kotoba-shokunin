# R75Facet01 — skill-eval artefact claim: content-blind counter boundary

## Axes
Named round axes: depth, freshness, consistency, calibration, operability, adjacency (`.ufo/waves/round-75/w1-spec.json:1`). This facet bears on **depth** and **calibration** only; no asserted improvement or harm to other axes.

## Evidence (committed bytes; observation)
- `SKILL.md:193` presents testing a skill via authored `evals/evals.json`, with/without-skill comparison, mechanical scripting, and trigger guidance; it explicitly identifies the round-70 source entry and guide-level status.
- `corpus/knowledge/skill-eval-artefacts-round70.md:13-21` limits S209/S210 to authoring guides, says numbers are advice, splits output-quality and trigger questions, and reserves human review for uncapturable judgment. Lines 23-34 enumerate facts; F7/F8 record the guide/reference threshold difference. Lines 74-82 explicitly refuse a claim that clients natively run the artefact.
- The counter implementation `verifiers/check_skill_evals.py:125-175` checks fact-row count, extracts one source id and quote, checks token presence and quote membership in a pinned snapshot, registry row shape/status/used-by, source header linkage, and that SKILL.md merely contains the entry path (`skill_ok = ENTRY in skill`, lines 129-137, 163-174). It does not inspect the fact prose for entailment or verify that `SKILL.md:193` faithfully communicates those facts; this is a direct code observation, not an inference about the prose's truth.
- Historical independent evidence: `corpus/lessons/round-70.md:238-244` records 11/13 junk worlds achieving 8/8; a 13-line world used empty fact text, `x`-filled source rows, and a bare path in SKILL.md. It says fact text, row content and SKILL substance were unchecked. Lines 270-278 classify this as M119 and state the depth claim rests on non-author spot-check rather than the hollow counter.
- `corpus/lessons/round-74-verifier-spotcheck.md:102-105` says depth was unchanged in r74 and there was no declared depth claim; this is historical context, not an r75 frozen claim.

## Concrete control / bounded move
For any r75 candidate that reuses the r70 artefact, treat `8 of 8` strictly as quote/provenance linkage, never as evidence that the authored facts or SKILL guidance are semantically supported. Require an independent, non-author, row-by-row adjudication: each fact statement and each corresponding SKILL sentence is matched to the cited committed snapshot at the exact supported scope; record the supporting source lines and mark overreach/unsupported wording explicitly. Keep the counter and the semantic review as separate evidence, and do not claim depth improvement from the counter alone. This is an audit control, not an edit or a proposed change to the historical claim.

## Risks and verification
Risk: a reviewer may reproduce the same shallow token/quote heuristic or accept paraphrase scope too broadly. Mitigation: quote exact snapshot evidence, record each reviewed claim separately, and include at least one plausible near-miss/overclaim in the review protocol; disagreement must remain visible rather than averaged. Verify a future candidate against its pinned committed snapshots and report the counter output separately from the adjudication; no live fetch or model run is needed for this bounded check.

No repository files were edited; no checks were run and no tools installed.
