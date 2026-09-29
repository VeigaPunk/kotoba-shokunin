---
name: command-heredoc-cd
description: >
  Fixture skill for the checker fixture world. Triggers:
  "fixture run". Anti-triggers: never use this for production
  skills, and do not use it outside the fixture tree.
---

# command-heredoc-cd

Role statement for the fixture skill.

```bash
cd /tmp
python3 - <<PYEOF
PYEOF
print('heredoc body is not a command')
ls \
    -la /tmp
```


## Fixture checklist

- [ ] First box text for this fixture.
      (executed: `trigger.line_budget`)
- [ ] Second box text for this fixture, with a continuation
      line to exercise multi-line box extraction.
