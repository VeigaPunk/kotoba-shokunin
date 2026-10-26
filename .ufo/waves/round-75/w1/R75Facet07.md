# R75Facet07 — description-audit candidate

## Axes
Depth (whether the audit measures sourced description quality) and calibration (whether its claims are bounded by the measurement/control). Candidate is specifically the trigger-evaluation rule in `SKILL.md` § Frontmatter craft, not a general audit of the skill.

## Evidence (committed working-tree bytes; no live fetch)

- `SKILL.md:193` prescribes about 20 labelled trigger queries, about three runs, ~40% validation never used to guide edits, and selection by validation pass rate. It also records a real threshold-boundary disagreement: guide uses `>` while `run_eval.py` uses `>=`; its recommendation is non-integral runs × threshold.
- `corpus/knowledge/skill-eval-artefacts-round70.md:48-54` gives the same protocol and explicitly says this is the same loop already held as S124, not independent corroboration. Its sources are identified at `:1-8` (S210/S213 optimization-guide source record; S211 script source record); the entry labels scope and refuses a native-client execution claim at `:74-82`.
- `plans/round-74.md:91-99` for the separate C1 claim illustrates a useful calibration pattern: do-nothing plus committed shortcut worlds, and explicitly labels truth of rule sentences as reviewer judgment rather than counter output. This is historical precedent only, not a frozen r75 claim.
- The historical plan says a falsify wave was required (`plans/round-74.md:14-17, 35`); the r74 spot-check records it was not dispatched (`corpus/lessons/round-74-verifier-spotcheck.md:34-37`). Do not treat r74's intended control plan as executed evidence.

## Assessment

The best bounded r75 candidate is not “description quality improved” or “the trigger loop is validated.” It is an audit of whether a *specific proposed description edit* beats its frozen baseline on a declared, held-out trigger-query set under the stated threshold semantics. The repository bytes support the protocol as documentary guidance and expose a concrete calibration hazard (`>` versus `>=`); they do not establish that any r75 description has been run, or that a score predicts general router behavior. Source depth is limited by the round-70 entry's own disclosure that S210 repeats S124 rather than independently corroborating it.

## Concrete control/check

Freeze the query set, `should_trigger` labels, threshold, iteration-selection rule, run count, and exact `>`/`>=` semantics before seeing candidate scores. Partition validation queries before edits and prohibit their use in choosing wording; report per-query rates and aggregate validation result, not only a pooled headline. Include boundary cases whose observed rates equal the threshold, so the `>`/`>=` disagreement changes an expected result. Add controls: baseline description and a deliberately overfit candidate that inserts training-query wording but should not improve held-out performance. Treat the result strictly as performance on this declared query population; a separate source-backed/manual review is needed for whether the description's scope and exclusions are factually accurate.

## Remaining unknowns

No r75 frozen claim, query population, score, committed receipt, or control execution was inspected/available in the cited paragraphs. The source snapshots/upstream bytes were not independently reopened in this leaf; findings concern committed lane descriptions of those sources, not fresh validation. No claim about present client runtime behavior follows.
