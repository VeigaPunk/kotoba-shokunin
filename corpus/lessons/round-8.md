# Lessons — round 8

Round: 8. Evidence: commit `8c300ad` ("round-8 corpus entries (uncommitted on
fleet pause)", 2 files, 799 insertions), report
`/home/vgpnk/projects/shokunin/.ufo/reports/round-8/kotoba.md` (120 B, a respawn
marker), artifacts `knowledge/opencode-offer-trace-round8.md` and
`knowledge/sibling-description-rewrites-round8.md`. **No `LOG.md` round-8 entry
was written** and `SKILL.md` was not touched: the lane was retired mid-round by
the fleet pause, so the round's integration delta landed a round late (round 9).
Round 9 re-verified three of this round's mechanism sentences and corrected them
— see "Corrected in round 9" below; the artifact text is append-only and is not
rewritten.

## Worked

- **The opencode side finally has an offer measurement.** Round 6's "no
  opencode catalogue" result was a wrong-literal artifact: `<skills>` is omp's
  tag; opencode renders `<available_skills>` (`fmt(list,{verbose:true})`,
  upstream `packages/opencode/src/skill/index.ts:321-343`). Corrected, the probe
  found two traces that agree without a stored record — the discovery module's
  `message=init count=N` log line, and reconstruction of the offered name set
  from the global roots (17 on disk + 1 builtin `customize-opencode` = 18 = the
  last logged count, `2026-09-28T19:44:36.669Z`). Lesson: when a cross-harness
  search comes back empty, re-check the *literal* before concluding the surface
  is absent.
- **A model-choice gap, cleanly separated from an offer gap.** godspeed is
  offered in 387/387 attested opencode sessions (100%; 399/399 by
  reconstruction) and activated in 205/399 = 51.4% — so round 6's 51.5%
  "coverage" was never an offer hole, matching round 7's omp finding
  (3911/3911 offered). The same number means different things on the two
  harnesses; only the offer side belongs to craft.
- **Producer-ready beats advisory.** The sibling lane shipped drop-in
  `description:` YAML per sibling plus the H7s reproduction recipe and pinned
  md5s, so the fix needs no re-derivation by the upstream owner. Its §5 also
  names what it cannot claim (routing improvement unmeasurable — none of the 5
  is offered; the LLM-cache branch cannot be exercised for an unoffered skill).
- **Re-render caught a stale count.** kotoba's own render string is reproducible
  byte-for-byte but measures **94** chars, not the 104 the round-7 doc recorded:
  re-run the `h7s` recipe in `knowledge/sibling-description-rewrites-round8.md`
  §1 on this repo's frontmatter `description` and count the output (the printed
  string and the 94/104 discrepancy are both in that artifact's §1 validation
  table). Same signature as rounds 5–7: stored counts drift while the
  mechanism claim survives.

## Failed / weak

- **An artifact is not a landed lesson.** Round 8 produced 799 lines of
  evidence and zero integration: `git show 8c300ad --name-only` lists exactly
  two `knowledge/` files — no `SKILL.md` edit, no README rows, no
  `lessons/round-8.md`, no `LOG.md` entry. The fleet pause hit the handoff step,
  the one step a lane cannot do unattended. Round 9 re-did the index work and
  wrote both lesson files; the honest record is that round 8 *discovered* and
  round 9 *landed*.
- **The five sibling rewrites are still proposals.** Cross-domain writes were
  never dispatched, and the subjects remain outside every omp discovery root,
  so even a perfect description buys audit hygiene only.
- **The durable-file delta was invisible to the next session.** Because
  `SKILL.md` was not updated, the skill's own contract still described a
  one-harness router model for a full round after the two-harness evidence
  existed — the defect class round 9 names "harness-unscoped claims".

## Corrected in round 9 (round-8 artifact claims, re-verified against upstream dev)

- **Dedupe: "first-scanned copy wins" is wrong.** `skill/index.ts:125-139`
  logs the `duplicate skill name` warn and then assigns unconditionally, so the
  **last-parsed** copy wins, and `Effect.forEach(…, {concurrency:"unbounded"})`
  (`:240-242`) makes the parse order nondeterministic run-to-run. Live proof,
  same file set: `.claude/skills/<name>` is the early copy in 154 warn lines (13
  runs) and the late copy in 18 warn lines (5 runs) —
  `grep 'duplicate skill name' ~/.local/share/opencode/log/opencode.log |
  grep -c 'existing=/home/vgpnk/.claude'` → 154, `… | grep -c
  'duplicate=/home/vgpnk/.claude'` → 18. Offer verdict unaffected
  (one entry per name; the bailian duplicates are symlinks to one target;
  godspeed has 0 duplicate warns).
- **"name ≠ folder ⇒ not offered" is wrong for opencode.** The only frontmatter
  gate is `isSkillFrontmatter` (`skill/index.ts:123`, requires `name: string`);
  `NameMismatchError` (`:67`) is declared and never thrown — a `SKILL.md` in
  `…/foo/` declaring `name: bar` **is** offered as `bar`.
- **"The non-verbose render is also used by the TUI" is wrong.** The TUI reads
  `app.skills({})` and renders `skill.description?.replace(/\s+/g," ").trim()`
  (`packages/tui/src/component/dialog-skill.tsx:41`) — whitespace collapse
  only, never `fmt`; the `## Available Skills` branch (`skill/index.ts:340-345`)
  has no production caller. No code path in opencode dev truncates a skill
  description (repo-wide `Truncate` hits are tool-output/compaction only).

## New evidence (opinion-flagged where not provable)

- **opencode's offer gate is: `description` defined** (`skill/index.ts:322`
  filter) **and the `skill` permission not disabled** (`session/system.ts:108`,
  per-skill deny filtered at `skill/index.ts:314`) **and winning the by-name
  dedupe, which is nondeterministic** (see above). Frontmatter must parse with
  a `name:`; folder-name equality is not checked.
- **There is no verbatim offer record to be had** short of a code change: the
  catalogue is assembled inline in `prompt.ts` and discarded; the persistence
  hook (`session_context_epoch`) exists but this build's migrations wipe it.
- **Log↔db joins are corroborative only**: 61 log sessions are absent from
  opencode.db, so the 415-part count and the 471 permission-line count cannot be
  reconciled exactly.