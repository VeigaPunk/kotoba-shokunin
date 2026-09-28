# Lessons — round 3

Round: 3 (no round-2 was run in this repo — numbering skipped 1→3 on operator
directive; LOG.md records the actual sequence, report written to
`.ufo/reports/round-3/kotoba.md`).

## Worked

- **Dogfooding the gap list.** The round-1 corpus README filed "no AGENTS.md
  corpus" as the top gap; picking it directly made the round self-evidently
  scoped. The corpus gap list functions as a work queue — keep it honest.
- **`diff` on sibling dispatch prompts** (`kagi-L1.md` vs `kotoba-L1.md`)
  isolated the template's variable fields in one command: role line, domain
  sentence, job stanza, round number. Faster and more reliable than reading
  files serially — template diffs are anatomy evidence.
- **`md5sum` for identity claims.** "Six AGENTS.md files are identical except
  the name" is falsifiable only with checksums; `cat` output alone would be
  assertion.

## Failed / weak

- **`edit` anchor drift cost two retries.** Mid-file inserts shifted line
  anchors between edits; one `PUT >N` mis-anchored into a wrong location and a
  `PUT N.=M` splice produced a duplicated line needing a repair edit. Lesson:
  after any mid-file insert, re-read the tail region before anchoring there —
  anchors below an insert are stale.
- **Round-number surprise discovered late.** The operator's "round-3" directive
  arrived while round-2 artifacts were still in flight mentally (bg job
  showed kagi's round-2 prompt). Check `git log` round labels against the
  incoming round number *before* planning report paths.

## New evidence (opinion-flagged where not provable)

- Round numbering is operator-driven and can skip; `LOG.md` is the record of
  what actually ran, not the counter. A lane should write to the round
  directory the operator names and note discrepancies rather than renumber.
