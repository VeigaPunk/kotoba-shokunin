---
name: command-heredoc-tilde
description: >
  Fixture skill for the checker fixture world. Triggers:
  "fixture run". Anti-triggers: never use this for production
  skills, and do not use it outside the fixture tree.
---

# command-heredoc-tilde

Role statement for the fixture skill.

```bash
python3 - <<~EOF
false
nonexistent-binary-xyz
~EOF
cat corpus/knowledge/anatomy-and-compression.md
```


## Fixture checklist

- [ ] First box text for this fixture.
      (executed: `trigger.line_budget`)
- [ ] Second box text for this fixture, with a continuation
      line to exercise multi-line box extraction.
