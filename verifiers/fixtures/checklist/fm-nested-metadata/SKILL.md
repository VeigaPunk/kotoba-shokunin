---
name: fm-nested-metadata
description: >
  Fixture skill whose frontmatter nests a metadata block, which is what the
  file's own metadata.requires box prescribes. Triggers: "fixture run".
  Anti-triggers: never use for production skills.
  and do not use it outside the fixture tree.
metadata:
  requires:
    bins: ["fixturebin"]
  owner: kotoba
---

# clean

Role statement for the fixture skill.


Verify the fixture world with `python3 -c 'print(1)'`.

```bash
ls -la
```


## Fixture checklist

- [ ] First box text for this fixture.
      (executed: `trigger.line_budget`)
- [ ] Second box text for this fixture, with a continuation
      line to exercise multi-line box extraction.
