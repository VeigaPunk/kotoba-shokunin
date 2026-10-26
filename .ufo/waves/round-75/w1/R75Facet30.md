# Facet 30 — description-eval calibration

## Finding (observed)
At committed kotoba tip `65a5c7a663249e0522cc49e4a148424200d9ddfe`, `corpus/knowledge/skill-eval-artefacts-round70.md:13-16` explicitly says S209/S210 are guidance, not normative specification, and characterizes thresholds as advice. Yet `:33-34` records a tension: the guide's threshold wording says “above,” while the reference script accepts equality (`>=`). This is usefully falsifiable and narrowly sourced, but the source guide and implementation are distinct authorities; a description audit must not collapse the implementation detail into a specification requirement.

The entry cites S213 at its header (`:2, :6`) and S211 (`:3`), and states its verifier counts facts (`:23`). The opening split between output quality and trigger firing (`:18-21`) is a clear control design: measure task performance separately from routing. The specific concrete risk is calibration overstatement from treating the suggested 0.5 default / equality boundary as a universal pass rule, despite its own authority note.

## Concrete check/control
For each description-trigger audit, preserve separate `should_trigger` and `should_not_trigger` query sets and report observed per-query rate, threshold, and comparison operator. Include boundary cases whose repeated-run rate equals the threshold; test the documented guide interpretation and actual evaluator behavior separately. Label 0.5 as a chosen starting threshold, not normative truth. This directly checks whether a claimed trigger pass is supported at the boundary and prevents conflating guide prose with code behavior.

## Scope and confidence
High confidence in the quoted committed text and its internal calibration distinction. This is a source-supported control recommendation, not evidence that the current r75 claim or evaluator has been independently tested. R74 plan is historical per assignment and is not used as a frozen r75 claim.

## Evidence
- `corpus/knowledge/skill-eval-artefacts-round70.md:13-16` — authority caveat; advice, not normative rule.
- `corpus/knowledge/skill-eval-artefacts-round70.md:18-21` — separate output-quality and trigger questions.
- `corpus/knowledge/skill-eval-artefacts-round70.md:33-34` — suggested threshold wording versus implementation `>=` boundary.
- `corpus/knowledge/skill-eval-artefacts-round70.md:1-8` — S209–S213 source/snapshot/recheck provenance.
- Command: `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse HEAD` → `65a5c7a663249e0522cc49e4a148424200d9ddfe`; `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin ls-files --error-unmatch corpus/knowledge/skill-eval-artefacts-round70.md corpus/lessons/round-74-verifier-spotcheck.md plans/round-74.md SKILL.md corpus/QUALITY.md` → all five tracked.

## Report trailer
- Facet: description-eval threshold calibration.
- Status: scoped evidence and concrete check reported; no edits or tests performed.
- Paths: `corpus/knowledge/skill-eval-artefacts-round70.md`; `.ufo/waves/round-75/w1/R75Facet30.md`
