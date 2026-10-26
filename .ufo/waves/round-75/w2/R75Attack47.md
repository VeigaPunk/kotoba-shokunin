# R75Attack47 — independent falsification

## Axes
Calibration; claim scope; material actionability; control non-vacuity.

## Verdict: finding survives, but is a bounded wording/sourcing defect

**Central claim:** `SKILL.md:23-25` claims that the frontmatter description is “the only part any router ingests,” while the offered evidence is only two observable harnesses and documentation for 11 clients. The proposed remedy is to scope the claim to observed/documented implementations or establish an exhaustive population.

**Independent evidence at stated lane revision.** Lane HEAD is `65a5c7a663249e0522cc49e4a148424200d9ddfe` (`.git/HEAD`). Reopened `SKILL.md:23-25`: it indeed says “only part any router ingests” and immediately qualifies the evidence as two observable harnesses plus 11 clients “mapped by documentation.” `SKILL.md:26-47` describes omp and opencode separately; lines 50-53 say the evidence base includes 16 production skill files and other instruction surfaces, not an exhaustive census of every router. Lines 54-56 explicitly advise re-verifying citations after drift. This supports the report's distinction between a universal assertion and bounded sources; it does not prove the universal assertion false.

**Counterevidence / calibration.** `corpus/lessons/round-74.md:72-76` records the prior intro change as an explicit considered suggestion: the intro previously contrasted “two harnesses here” while the lane mapped seven clients by documentation; it reports that the current clause names two observable harnesses and says 11 clients are mapped by documentation. Its count command counts distinct seven client-table names plus TRAE, CodeBuddy, Kimi Code, Zhipu (11). This confirms the text's evidence framing was intentionally made more precise, but it is not evidence that all 11 clients actually ingest description only, nor that the universe of routers is exhaustive. The count itself is a name-count, not an ingestion-behavior test.

**Cheap check / safety.** Reopened the cited committed lines; no live fetch or source mutation was needed. The proposed counterexample criterion is sound in principle: one in-scope router ingesting body/other fields would refute “only part any router ingests.” It is not a runnable check until the population and meaning of “router” are operationally specified. Requiring an “actual router/client population” without defining a closed population risks an impossible/vacuous demand. The current evidence does not establish any counterexample, so this is a calibration/source-coverage issue, not a demonstrated runtime defect.

**Impacted axes:** calibration (universal quantifier exceeds stated evidence); actionability (a bounded rewrite is readily actionable); control non-vacuity (enumeration helps only if scope is defined and membership evidence is checkable). No duplicate finding identified in the target itself.

**Smallest safe correction:** retain the accurate bounded basis in the sentence and avoid presenting the universal as verified; e.g. describe observed behavior for omp/opencode and separately state that the named additional clients are documented, with a citation/countable source set. If retaining “any router,” define an explicitly closed population and test each member's loaded fields. Do not claim falsity absent a counterexample.

## Sources
- Lane `SKILL.md:23-25,26-47,50-56`, revision `65a5c7a663249e0522cc49e4a148424200d9ddfe`.
- Lane `corpus/lessons/round-74.md:72-76`.
- Target `w1/R75Facet47.md:5-9,13-20`.
