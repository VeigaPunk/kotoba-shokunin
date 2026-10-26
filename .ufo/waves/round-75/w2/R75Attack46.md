# R75Attack46 — independent falsification

Axes: factual support; falsifiability; scope; control weakness.

**Verdict: finding survives; control is non-vacuous as a proposed discriminating test, but not yet executed.** At measured master `65a5c7a663249e0522cc49e4a148424200d9ddfe`, `SKILL.md:237-242` explicitly labels `trigger.anti_trigger_clause` a vocabulary test and expressly states both false-pass and false-fail cases. Independent source inspection of `verifiers/verify_skill_checklist.py:93-103,1439-1456` confirms the contract and implementation: regex marker presence yields PASS; no marker yields FAIL. Thus this is not a mistaken inference from an opaque counter: the source and normative text agree, and the report does not falsely claim current semantic validation.

`SKILL.md:243-247` requires concrete sibling arbitration in frontmatter. The cited r74 spotcheck `corpus/lessons/round-74-verifier-spotcheck.md:75-77` records a count of ten named lanes and counter outputs; `:80-86` itself says the counter does not discriminate the judged change, and supplies separate line-level boundary reasoning. The report's narrow claim—that the census does not prove arbitration quality—is supported. The historical r74 evidence is explicitly scoped as historical in the facet, not passed off as an r75 frozen claim.

**Counter / qualification:** proposed paired controls (vacuous marker versus a legitimate unlisted exclusion; named sibling with generic split) would help distinguish lexical checks and census from semantic review, but would only establish behavior of whichever checker/reviewer is actually exercised. The facet expressly says it did not inspect fixtures and does not assert the controls are currently absent. Do not turn this bounded observation into a claim that the existing gate is defective beyond its disclosed ceiling, or that a particular future control is already a required product feature.

Evidence reopened: `SKILL.md:237-247`; `verifiers/verify_skill_checklist.py:93-103,1439-1456`; `corpus/lessons/round-74-verifier-spotcheck.md:75-86`; revision above.
