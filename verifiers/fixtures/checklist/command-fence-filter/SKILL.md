---
name: command-fence-filter
description: >
  Fixture skill for the checker fixture world. Triggers:
  "fixture run". Anti-triggers: never use this for production
  skills, and do not use it outside the fixture tree.
---

# command-fence-filter

Role statement for the fixture skill.

```text
repo/
├── a
└── b
```

```python
import os
```

```yaml
name: not-a-command
```

```bash
ls -la
```


## Fixture checklist

- [ ] First box text for this fixture.
      (executed: `trigger.line_budget`)
- [ ] Second box text for this fixture, with a continuation
      line to exercise multi-line box extraction.
