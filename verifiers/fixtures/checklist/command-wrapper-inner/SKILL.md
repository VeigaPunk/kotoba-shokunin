---
name: command-wrapper-inner
description: >
  Fixture skill for the checker fixture world. Triggers:
  "fixture run". Anti-triggers: never use this for production
  skills, and do not use it outside the fixture tree.
---

# command-wrapper-inner

Role statement for the fixture skill.

```bash
sudo definitely-missing-sudo run
FOO=1 definitely-missing-env run
env FOO=1 definitely-missing-env2 run
time definitely-missing-time run
sh -c 'definitely-missing-shc run'
```


## Fixture checklist

- [ ] First box text for this fixture.
      (executed: `trigger.line_budget`)
- [ ] Second box text for this fixture, with a continuation
      line to exercise multi-line box extraction.
