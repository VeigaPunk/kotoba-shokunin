# R75Facet08 — calibration / operability

## Finding
**Axis:** calibration and falsifiability. **Candidate surface:** the round-74 closure's C1 page-fidelity row and the bounded coverage verdict. Evidence is strong for the *recorded measurement*, but not independently reproducible from this passage alone; the report explicitly separates evidence-verified counter behavior from judgement.

## Observations (committed source rows)
- `corpus/lessons/round-74-verifier-spotcheck.md:58` describes a manual fidelity review: approximately 44 located line pointers; rule groups 5/5 per three pages, table rows 3/3, zero overreach/unsupported. It also records scope hedges. This is a checkable claim, but its summary omits the reviewers' actual outputs and does not enumerate all ~44 pointers in this table cell (it uses ellipses for some locations).
- The distinction is properly calibrated at `:63-64`: rows, digests, live bytes, fidelity, and line count are said to be re-measured, while only the counter's 0/3→3/3 and self-test are called evidence-verified; verdict is specifically coverage `improved`, not a broad depth closure.
- `corpus/QUALITY.md:36-37` gives concrete controls: mutate claimed content and require counter/content-guard change (Q25); each headline clause must be measured by counter or falsifiable cited guard (Q26). These directly apply to any future audit claiming source fidelity or breadth.
- `corpus/knowledge/skill-eval-artefacts-round70.md:74-80` demonstrates scope discipline: it refuses to claim native client execution absent source support and distinguishes the documented opt-in plugin. This is a useful calibration control, not evidence for the separate r74 sources.

## Concrete control / check
For a description-audit claim, preserve the exact committed source snapshot hash and a reviewer artifact with one source locator per substantive description clause; have an independent reviewer mark each clause supported / overreach / unsupported and record outputs. Add a falsification arm that removes or alters a cited clause/source and demonstrates the content guard's exit/output changes (QUALITY Q25–Q26). Limit the headline to the tested source set and snapshot; do not infer client runtime behavior from documentation-only evidence.

## Limits and confidence
Confidence: medium-high that the *closure text* is calibrated (it bounds the verdict and labels reviewer judgement separately); medium that the summarized fidelity result is independently auditable from this report excerpt, because reviewer outputs and complete pointers are not reproduced here. No inference that fidelity is false. This is not a frozen r75 claim: `plans/round-74.md:3-17` labels its plan historical/frozen-before-wave and describes r74's two-wave design; do not carry it forward as an r75 assertion without fresh committed-byte checks. Read-only; no live fetch or experiments performed.