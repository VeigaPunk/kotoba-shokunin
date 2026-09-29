---
name: command-sh-c-inner
description: >
  Fixture skill for the checker fixture world. Triggers:
  "fixture run". Anti-triggers: never use this for production
  skills, and do not use it outside the fixture tree.
---

# clean

Role statement for the fixture skill.


Verify the fixture world with `python3 -c 'print(1)'`.

```bash
sh -c 'cat corpus/absent-round16-shc.md'
```


## Fixture checklist

- [ ] First box text for this fixture.
      (executed: `trigger.line_budget`)
- [ ] Second box text for this fixture, with a continuation
      line to exercise multi-line box extraction.
