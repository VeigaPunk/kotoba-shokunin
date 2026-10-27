# R75Facet48 — Description evidence depth and control

## Finding
At committed HEAD `65a5c7a663249e0522cc49e4a148424200d9ddfe`, `SKILL.md:205-216` labels six body-craft rules by source and gives concrete author actions; this is sourced instructional content, not a measurement of description quality. For the description specifically, round-74 spotcheck `corpus/lessons/round-74-verifier-spotcheck.md:76-77` records a parsed 1,021-character description, ten lane names, and counter outcomes 0/20 to 20/20 plus a carry-forward 20/20. Those observations establish a size/name-presence predicate only. The same report states the counter cannot discriminate the judged carry-forward change (`:80-83`); it separately describes wave-2 falsification as undispatched (`:34-36`). These are concrete control limitations, not evidence that the description is actually misrouted.

The relevant sourced calibration material exists in `corpus/knowledge/skill-eval-artefacts-round70.md:48-54`: repeated labelled trigger/non-trigger query sets, a held-out validation split, and an explicit warning that skill-creator and the guide disagree at threshold equality (`:58-72`). Its scope refusal says no claim that clients natively run the eval artefact (`:74-82`). This offers a documented candidate control pattern, not proof that r75 has a frozen test corpus or observed route outcomes.

## Concrete check/control
For any r75 description claim, freeze a prompt set with source-grounded expected routes: positive examples for each asserted responsibility and negatives near each anti-trigger and named sibling boundary. Keep a held-out subset out of edits; run repeated trials, record expected/observed route and false-positive/false-negative cases, and have an independent reviewer adjudicate expectation disagreements against committed description and boundary bytes. State the threshold/equality convention explicitly. Retain the existing count as a structural check, not as the semantic verdict. A must-fail control should remove or falsify one boundary clause and show the semantic guard changes result. Bound claims to the tested prompt set and observed harness; don't infer universal routing behavior.

## Evidence, confidence, gaps
- Observed: `SKILL.md:205-216`; `corpus/lessons/round-74-verifier-spotcheck.md:34-36,76-83`; `corpus/knowledge/skill-eval-artefacts-round70.md:48-54,58-82`; `corpus/QUALITY.md:36-42` (counter/content, headline, and counter-description bounds).
- Inference: a character/lane-name predicate cannot establish precision, recall, or semantic boundary fidelity; those measurements are absent from the cited C2 rows.
- Confidence: high on the narrow distinction between recorded structural predicate and unreported semantic outcome; moderate on proposed control suitability, since no fixture or current runtime result was inspected.
- Unresolved: whether another committed fixture already measures description-trigger routes; this was a targeted facet read, not a repository-wide sweep. The r74 plan is historical and is not treated as r75's frozen claim.

## Commands / provenance
- `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse HEAD` → `65a5c7a663249e0522cc49e4a148424200d9ddfe`.
- Read the committed working-tree sections at the paths/lines cited above. No live fetch or runtime experiment performed; no edits outside this report.
- LSP device was unavailable in this environment; evidence is literal committed source text, not semantic LSP results.

Report path: `.ufo/waves/round-75/w1/R75Facet48.md`
