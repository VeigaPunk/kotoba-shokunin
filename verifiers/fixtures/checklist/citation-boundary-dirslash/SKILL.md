---
name: citation-boundary-dirslash
description: >
  Fixture skill for the checker fixture world. Triggers:
  "fixture run". Anti-triggers: never use this for production
  skills, and do not use it outside the fixture tree.
---

# citation-boundary-dirslash

Role statement for the fixture skill.

The knowledge base under `corpus/` holds every round document; this fixture
names the directory itself rather than one file inside it.

No command surface at all in this fixture body (the command check reports N/A).


## Fixture checklist

- [ ] First box text for this fixture.
      (executed: `trigger.line_budget`)
- [ ] Second box text for this fixture, with a continuation
      line to exercise multi-line box extraction.
