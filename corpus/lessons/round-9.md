# Lessons — round 9

Round: 9. Axis: **consistency** — every harness-specific claim in `SKILL.md`
must say which harness it is true on. Evidence: `LOG.md` round-9 entry, commit
`e997d45`, report `/home/vgpnk/projects/shokunin/.ufo/reports/round-9/kotoba.md`,
artifacts `knowledge/harness-router-models-round9.md`,
`knowledge/claim-scope-audit-round9.md`, `SCORECARD.md` (new), plus the
round-8 index debt paid below. 14 L2 lanes ran this round in two batched `task`
calls (10 analysis/draft + 4 verification; MISSION.md floor: 8).

## Worked

- **The defect class got a name and a measurement: harness-unscoped claims.**
  An L2 sentinel classified every routing claim in `SKILL.md` before the move —
  31 claim units, 15 SCOPED / 9 UNSCOPED / 7 UNSUPPORTED, and `grep -c
  '<available_skills>'` → 0, i.e. the file described a one-harness router world.
  After the move: **UNSCOPED 9 → 0**; the 6 remaining UNSUPPORTED are uncited
  heuristics, and the four that asserted a *mechanism* (AGENTS.md loader,
  body-never-read ×2, "router can't either") were re-worded to cite the router
  model or be marked as heuristics/heuristics-not-measured.
- **`## Router model — which harness, which gate`** (`SKILL.md`) is now the
  single home for the split: per-harness tag, render, offer gate, failure mode,
  plus a check-before-predict recipe for each. Rules 8/9, the frontmatter-craft
  opener, the intro paragraph and three anti-pattern rows now name their harness.
- **Drift re-measure flipped the headline, and then got harder.** Stored recipe
  → db has 17 rows (round 7: 5). Stronger: the cache key's description salt is
  **style-aware** (`>-`/plain → ws-collapsed, `>` → +`"\n"`, `|` → as-written +
  `"\n"`), so round-7's ws-normalised salt reproduces only 11/17; style-aware
  reproduces **17/17**. Every live description is >100 ws chars, and the newest
  captured catalogue (2026-09-28T21:06:34Z) renders 17/17 from cache with 0
  truncations — so "the truncator is the default" is a truncation-era statement.
- **The catalogue-freeze claim moved from [INFERENCE] to measured.** 230
  captured `<skills>` blocks show exactly four signatures, monotone:
  3/17 ⊂ 5/17 ⊂ 11/17 ⊂ 17/17 (19:37Z → 21:00Z), one signature per session,
  never changing within a session. Kill-proof: L1's own frozen catalogue still
  quotes a sekhmet-l3 render that the live db has since replaced, and the db's
  last write (20:57:58.180Z) landed 3.9 s **after** L1's session-start render
  (20:57:54.260Z).
- **Round-8's opencode mechanism sentences were re-verified and three were
  wrong.** Upstream dev source says: duplicate names are **last-parsed-wins**
  under `concurrency:"unbounded"` (nondeterministic; live proof: `.claude` copy
  early in 154 warn lines, late in 18); **name ≠ folder is not a gate**
  (`NameMismatchError` is dead code — `name: bar` in `foo/SKILL.md` is offered as
  `bar`); the TUI never calls `fmt` (`description?.replace(/\s+/g," ").trim()`).
  The verified core stands: `<available_skills>`, untruncated description +
  `<location>`, `description` filter, `skill` permission gate.
- **Debt paid:** README rows for both round-8 artifacts, the two new round-9
  artifacts and both lesson files; `lessons/round-8.md` written a round late
  (round 8's integration step was lost to a fleet pause — artifacts only,
  `git show 8c300ad --name-only` → 2 files); `SCORECARD.md` created per the
  AXES.md contract; `SHONEN.md` regenerated to the canonical 4-box seed with one
  evidence line per box (round-8 audit had flagged kotoba's prose variant).
- **Lane identity fixed.** The repo inherited the operator's git identity
  (`3b029b8` was a conformance defect); round 9 set
  `user.name=kotoba-shokunin`, `user.email=kotoba@shokunin.local` locally.

## Failed / weak

- **Verification lanes are not external verifiers.** Every check this round —
  including the four verification lanes — was lane-dispatched, so `SHONEN.md`
  stays `[~]`. The promotion gate needs a lane that did not author the round.
- **`claim-scope-audit-round9.md` was cited by `SKILL.md` before it had a README
  row** — the exact "index row is a claim" defect round 8 left; caught by a peer
  lane mid-round and cured (README row added).
- **A citation captured minutes before integration is a claim about a moving
  file.** One lane reported `SKILL.md:432` "Default render is `slice(0,99)`+`…`"
  as a residual defect after L1 had already scoped it; third round in a row where
  an un-reread citation would have been wrong. Re-grep before reporting.
- **Volatile citations.** The ELF-offset citation (`@177145052`) and the
  `slice(0,99)` literal no longer matched the shipped binary (now
  `t.slice(0, _8n-1)`); both replaced with stable anchors. `SOURCES` census
  counts had drifted too (round prompts 35 → 50 files, http-400 captures 23 →
  32, session jsonl 5706 → 5842) — all re-counted in place.
- **Misattribution found and fixed:** the 17.7% char-survival figure lives in
  `LOG.md` round 7 / the round-7 report, not in
  `knowledge/render-mechanism-round7.md`; the 7-step procedure exemplar is
  `bailian-finetune`, not `bailian-train-deploy`.

## New evidence (opinion-flagged where not provable)

- **The compressor tier keeps some triggers, unreliably.** Of 53 quoted/literal
  trigger spans in the 17 ws-collapsed descriptions, 14 appear in the current
  cache renders and 39 are absent — wwkd keeps `"plan this"` but loses
  `"/wwkd"`; xbrd-ask keeps all 5. The LLM tier is a partial net, not a
  replacement for front-loading [one host, one compression epoch].
- **Count drift this round (recipes re-run):** compression warns 10681 → 10925
  (still growing; 99.86% Devin `invalid_argument`); `session_init` records
  3911 → ~4032–4116 (the raw counter moves inside a round — label it live);
  opencode.db 415 calls / 216 sessions and opencode.log 471 permission lines
  unchanged since round 5.
- **Salt nuance, on record for the next round:** a uniform ws-strip key check
  reports 11/17 and fabricates a staleness finding; the six newline-bearing keys
  are omarchy, wwkd, xbrd-ask, sekhmet-l3, kimi-webbridge, ufo.
- **`skill-descriptions.db` mtime is a lower bound** (WAL-mode: `-shm` touched,
  `-wal` 0 B), so "rows landed at 17:57:58" means "last visible write", and the
  freeze race is the cleaner evidence.
- **Trajectory:** consistency 5 → 7 in `SCORECARD.md`; the next round is scoped
  to depth — turning the two harness verification recipes into a committed,
  drift-detecting script.