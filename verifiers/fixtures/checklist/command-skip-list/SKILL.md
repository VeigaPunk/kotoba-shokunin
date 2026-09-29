---
name: command-skip-list
description: >
  Fixture skill for the checker fixture world. Triggers:
  "fixture run". Anti-triggers: never use this for production
  skills, and do not use it outside the fixture tree.
---

# command-skip-list

Role statement for the fixture skill.

```bash
#!/usr/bin/env bash
# a comment line
FOO=bar
echo hello && cd /tmp
for f in a b; do echo $f; done
env FOO=bar ls /tmp
sudo ls /
command ls /tmp
VAR=x ls /tmp
xargs -n1 echo
```


## Fixture checklist

- [ ] First box text for this fixture.
      (executed: `trigger.line_budget`)
- [ ] Second box text for this fixture, with a continuation
      line to exercise multi-line box extraction.
