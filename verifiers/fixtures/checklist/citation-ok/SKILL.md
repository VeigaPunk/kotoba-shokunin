---
name: citation-ok
description: >
  Fixture skill for the checker fixture world. Triggers:
  "fixture run". Anti-triggers: never use this for production
  skills, and do not use it outside the fixture tree.
---

# citation-ok

Role statement for the fixture skill.

Every citation in this fixture resolves from the repo root: see
`corpus/knowledge/anatomy-and-compression.md` and
`verifiers/verify_skill_checklist.py` for the two live source documents.

No command surface at all in this fixture body (the command check reports N/A).


## Fixture checklist

- [ ] First box text for this fixture.
      (executed: `trigger.line_budget`)
- [ ] Second box text for this fixture, with a continuation
      line to exercise multi-line box extraction.
