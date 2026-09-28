# Lessons — round 4

Round: 4. Evidence: `LOG.md` round-4 entry, commit `round-4`,
report `/home/vgpnk/projects/shokunin/.ufo/reports/round-4/kotoba.md`.

## Worked

- **`uniq -c -w32` on region hashes for duplication claims.** `md5sum` over the
  sed-extracted preamble region across all 18 agent files collapsed "13
  identical, 4 absent, 1 doubled" into one pipeline — stronger than counting
  `grep` hits because it proves byte-identity, not just presence.
- **`grep -c` caught a merge artifact.** mutation-tester.md embeds the godspeed
  preamble twice in-file — invisible to "which files have the preamble"
  counting; only a per-file count exposes doubling. Duplication checks should
  count occurrences per file, not just file membership.
- **`wc -l`+`diff` before classifying.** Sizing `.ufo/prompts/` first split it
  cleanly into the 9–12-line spawn family and the 3–4-line round family; the
  `kake`/`kasegi` diff then proved the template varies in exactly two fields.
- **Gap list as queue, again.** Round-3's README filed "taxonomy generalizes
  from 3 observed classes only"; the host had exactly two unsurveyed classes
  (`agents/`, `command/`) plus a second dispatch mode hiding inside the
  already-surveyed prompt directory. The gap was real and bounded.

## Failed / weak

- **Two literal-hunk-header insertions.** `PUT`/`CUT` op lines emitted inside
  a body twice landed as file text (lines `PUT 67*=70*:` and `PUT 81.=85:`),
  each requiring a repair pass — the exact failure this repo's own round-3
  lesson warned about, recurred. Cause: one `edit` call carrying two ops where
  the second's header was misparsed. Mitigation applied mid-round: after every
  multi-op `edit`, `grep -n 'PUT \|CUT '` the file before proceeding — cheap
  and it caught both. This failure signature now belongs in the domain's
  anti-patterns as a tooling note, not just a personal lesson.
- **Section-order drift during repair.** Moving blocks left the wrap-up
  paragraph before the anatomy paragraph; caught only by re-reading the full
  section, not by the edit tool's echo. Structural order is a separate check
  from text correctness.

## New evidence (opinion-flagged where not provable)

- Frontmatter without a freshness mechanism accumulates stale claims:
  `ufo.md`'s `cascade_note` carries a `until 2026-08-29` deadline past at
  survey time. Prediction: any date-bearing frontmatter field is stale within
  ~1 quarter unless a status file owns the fact. Falsifiable by re-survey.
- The 5-class surface taxonomy on this host may still be incomplete:
  harness-injected system prompts exist but are not owned by any writable
  file — they are evidence of a sixth class with no surveyable artifact.
