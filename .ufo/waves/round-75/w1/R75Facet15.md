# R75Facet15 — anti-trigger checklist: lexical presence is not exclusion validity

## Finding (observed)

`SKILL.md:237-242` presents “at least one anti-trigger or exclusion clause” as a checklist item, but explicitly limits the executed check to a vocabulary test: a marker-bearing vacuous clause passes, while a genuine exclusion outside the vocabulary fails. The verifier confirms the boundary: its docstring says this at `verifiers/verify_skill_checklist.py:94-103`; `check_anti_trigger` strips quoted spans, searches `ANTI_TRIGGER_RE`, and returns PASS on any match (`:1439-1457`). Thus the box's PASS is evidence only of a recognized token outside quotes—not that the description actually excludes an intent or skill.

This is an acknowledged limitation, not an undisclosed counter defect. The live skill description itself has concrete exclusions at `SKILL.md:8-16` (e.g. general prompt engineering, runtime code changes, and named sibling ownership), so the current instance is stronger than a marker-only PASS. The check does not establish that fact.

## Assessment / bounded inference

For an audit candidate about description quality, this is a concrete calibration gap: a reader may interpret “PASS” as semantic compliance although the checker explicitly disclaims semantics. A falsifiable claim is available: “the anti-trigger gate accepts at least one description with a marker but no meaningful exclusion.” This is already stated as a known limit in the verifier docs and in the checklist itself; do not claim the round discovered it anew. [INFERENCE] A future description audit could measure false positives by adjudicating whether each passing description's exclusion identifies a meaningful out-of-scope intent, rather than treating marker presence as evidence of that property.

## Concrete control

Use a paired control against the same frozen checker: (1) a vacuous marker case such as `Never use this skill.` must demonstrate the current lexical PASS; (2) a semantically clear exclusion phrased without any listed marker must demonstrate the current lexical FAIL. Record both outcomes and keep the verdict wording bounded to “recognized exclusion marker present.” For any semantic-quality claim, separately have a named non-author reviewer assess the exclusion against the description's positive trigger/use case, with their cited text and disagreement recorded; do not promote the lexical check to a semantic gate without such a controlled instrument.

## Evidence and commands

- `SKILL.md:237-242` — checklist criterion and explicit caveat.
- `verifiers/verify_skill_checklist.py:94-103,1439-1457` — documented limitation and implementation.
- `verifiers/verify_skill_checklist.py:2053-2055` — self-test cases include absent-marker and quoted-negation cases; these do not, by themselves, assert semantic exclusion validity.
- Read-only literal search: `grep -n 'vacuous\|anti-trigger\|trigger.anti_trigger_clause' verifiers/verify_skill_checklist.py` (matches the cited docstring, implementation, and case names).

Confidence: high on the stated lexical boundary (source code and its own documentation agree); semantic evaluation of real descriptions remains reviewer judgment.
