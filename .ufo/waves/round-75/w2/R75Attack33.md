# R75Attack33 — independent falsification

## Axes
Factuality, calibration, operability.

## Verdict
**The omission is real and the proposed control is non-vacuous, but “material” is a judgment about the compact instruction’s intended completeness, not an observed defect in evaluations.** The target correctly distinguishes guide advice from normative specification and explicitly limits its inference. I found no counterexample to its factual claim that the held-out selection protocol is missing from the compact line. The strongest qualification is that the cited source itself calls its counts defaults and the skill line is deliberately compressed; this does not establish that any description tuning has overfit or leaked validation data.

## Evidence

- Independently reopened `R75Facet33.md`. Its central claim is that `SKILL.md:193` omits the source guide’s fixed held-out validation and best-iteration selection guidance, while its inference is only that omission weakens standalone prevention of overfitting.
- Confirmed measured revision is `65a5c7a663249e0522cc49e4a148424200d9ddfe`. Read the committed bytes (not just the working-copy file): `SKILL.md:193` says about 20 labeled queries, about 3 runs, the equality distinction, unique strings, and non-integral runs × threshold; it says nothing about splitting a held-out set or selecting iterations by validation pass rate.
- Committed `corpus/knowledge/skill-eval-artefacts-round70.md:48–54` records the omitted protocol: about 40% fixed validation queries that never guide edits and choosing the best iteration by validation pass rate. This is source-derived support, not independent corroboration: the entry explicitly says the guide and skill-creator describe the same loop, and that this protocol is stated twice rather than independently corroborated.
- Reopened the preserved `S210-optimizing-descriptions.md` snapshot: lines 136–147 describe the train/validation split, fixed split, and keeping validation out of edits; lines 151–163 say to choose the best iteration on validation pass rate. Thus the claim is supported by the cited source snapshot. The two guessed snapshot filenames in the facet are not present; the actual local snapshot is named `S210-optimizing-descriptions.md` (its substantive evidence is available and matches the knowledge entry).
- The proposed check has operative conditions: freeze validation inputs before edits, prohibit their use in wording changes, compare iterations on validation pass rate, and separately report train/validation results. Its boundary arm is also mathematically reachable: with threshold 0.5 and two runs, one firing gives rate 1/2, so strict “above” and `>=` disagree. This checks reporting/comparator behavior, not whether a model actually triggers reliably. No runtime or client behavior was tested.

## Smallest safe correction

Retain the scoped omission finding, but describe it as an optional depth/operability improvement to a compact guide line, not evidence of actual leakage or overfitting. If the line is expanded, add a short pointer to fixed held-out validation and best-iteration selection (or ensure its referenced knowledge entry is the deliberate destination); preserve the existing guide-advice/non-normative caveat. No lane-source changes made.

## Report

- `.ufo/waves/round-75/w2/R75Attack33.md`
