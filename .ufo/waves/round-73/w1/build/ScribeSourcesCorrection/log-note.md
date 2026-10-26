# LOG.md draft (r72 closure defect D4) — one-line note

## Proposed exact replacement for `corpus/knowledge/resident-index-and-rungs-round72.md:45`

```
- **Check the harness's house standard before the format's rules.**
```

## Proposed one-line LOG.md note (append after the Round 72 block, style of the existing `- <date> — round N:` lines)

```
- 2026-10-25 — round 73: repaired the r72 closure-defect D4 typo at `corpus/knowledge/resident-index-and-rungs-round72.md:45` — "before the format's,." → "before the format's rules." (the bullet's own continuation names those rules: F7's 60-char description cap and no-invented-commands clause; the wave-1 draft's dropped ", and let portability pick the middle rung" is not restored, because the landed F table ends at F7 and the entry carries no portability finding. Quotes and `verified-at` lines untouched.)
```

## Why this replacement, and not the others

- Evidence: the wave-1 draft bullet, `.ufo/waves/round-72/w1/build/ScribeEntryRung/resident-index-and-rungs-round72.md:64`, reads `- **Check the harness's house standard before the format's, and let portability pick the middle rung.**` — the landed `,.` is a truncation at that comma, not a stray keystroke.
- The draft's next line carries an F8 clause (`skills, not always-on files or prompts, are what travel between agents (F8)`); the landed entry's finding table ends at `| F7 |` and `grep -c -i portability` on the landed file prints `0`. The landing edit therefore dropped the portability/F8 half deliberately, so restoring that clause would be a claim edit, which plan line 37-38 forbids ("a lane-authored entry typo, not a claim edit").
- Deleting only the comma leaves an elliptical headline ("before the format's.") whose missing head noun the reader must supply; `rules` is the noun lines 46-47 enumerate.
