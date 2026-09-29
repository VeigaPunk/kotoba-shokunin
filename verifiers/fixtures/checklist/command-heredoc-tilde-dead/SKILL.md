---
name: command-heredoc-tilde-dead
description: >
  Fixture skill for the checker fixture world. Triggers:
  "fixture run". Anti-triggers: never use this for production
  skills, and do not use it outside the fixture tree.
---

# command-heredoc-tilde-dead

Role statement for the fixture skill.

```bash
python3 - <<~EOF
false
nonexistent-binary-xyz
~EOF
cat corpus/absent-round17.md
```


## Fixture checklist

- [ ] First box text for this fixture.
      (executed: `trigger.line_budget`)
- [ ] Second box text for this fixture, with a continuation
      line to exercise multi-line box extraction.
