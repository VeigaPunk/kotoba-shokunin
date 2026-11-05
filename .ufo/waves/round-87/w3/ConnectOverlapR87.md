# ConnectOverlapR87 — staged-package and sibling-lane overlap (read-only)

Seat scope: overlap audit only. Everything below is read-only observation; no sibling,
staged package, or lane corpus file was written.

## 1. Staged package (`/home/vgpnk/Projects/shokuknow/merge/kotoba/`)

The round-87 report's "package absent" claim is **still true**: the package covers
rounds 1–16 (rows S203–S390 staged over the lane's S128 ceiling) and contains **no
round-87 material**.

- `MERGE-REPORT.md` § rows by round: `round1=11 … round16=14` — no round-87 (or any
  round >16) bucket.
- `SOURCES.append.md` top id is **S390**; every row cites rounds ≤16.
- `knowledge/` holds 88 entries; none named for omp loader semantics.
- Grep for `omp|skill.root|discovery|loader|plugin` over the whole package tree:
  only generic "discovery roots" language in vendor-facing entries
  (`chinese-client-skill-surfaces.md`, `spec-script-craft-rules.md`,
  `client-frontmatter-and-discovery-divergence.md`, `skill-paths-and-precedence.md`
  in the merge report's own table at line 46). No `omp`, `oh-my-pi`, `can1357`,
  `skill.?root`, `omp-plugins`, or `reader_quote` hit anywhere in the package.
- The only staged row numerically colliding with the lane's new S256 is staged
  `S256` = "Agent Skills — How to add skills support to your agent" (agentskills.io
  client-implementation page). The lane's own registry already holds that page as
  S002 and re-cites it as staged S256 for the **loading/validation/disclosure**
  sections (MERGE-REPORT line 60; lane corpus/SOURCES.md:252 records the
  round-72 screen of exactly this row). The lane's round-87 S256 is a *different
  source entirely*: the omp ELF / `discovery/omp-plugins.ts` reader. Same id,
  different row — an id-space collision the operator should know about at adopt
  time, not a duplicate claim.

**Package dates (mtimes, not git — the package tree has no VCS access here):**
`MERGE-REPORT.md`, `SOURCES.append.md`, and every `knowledge/` file carry mtime
`2026-10-24 23:33:20 -0300`. The lane's round-87 C1 landed at commit `e03f9e2`
`2026-11-04 21:13:02 -0300` (`git log -1 -- corpus/knowledge/omp-root-semantics-round87.md`).
The package predates the round by ~11 days, so "package absent" remains accurate —
it is not a stale observation.

## 2. Sibling lanes

Marker grep (`omp-skill-roots|reader_quote|discovery/omp-plugins`) across
`*/.ufo` and `*/corpus` outside this lane returned **no corpus hits** — only two
chousa-shokunin `.ufo` wave receipts that quote this lane's SCORECARD text, and
one kake-shokunin receipt quoting this lane's own SOURCES.md S255 row.

Broad omp/oh-my-pi sweep of sibling `corpus/SOURCES.md` + `corpus/knowledge/`:

- **kumitate-shokunin** — the only sibling with substantive oh-my-pi coverage:
  S001/S002/S003/S080 task-agent contract (`docs/task-agent-discovery.md`,
  `docs/tools/task.md`, `docs/agent-hub.md`); S024 `docs/mcp-config.md`; S053/S087
  `packages/utils/src/dirs.ts` agent-dir member census (incl. the
  `skill-descriptions.db` filename); S060 v18.12.6 agent-root member readers
  (discovery/builtin.ts reads `extensions/`, RULES.md, hooks); S068/S099–S104
  task-isolation / async-job internals; S224 `docs/lsp-config.md`; S226 dirs.ts
  re-grounded at v18.15.0. Its knowledge files `omp-agent-root.md`,
  `omp-task-contract.md`, `kimi-skills-plugins.md` cover agent-directory
  membership, task-agent discovery precedence, and Kimi's skill/plugin plane —
  **none grounds the skill-root loader semantics** (the 12 `root_pattern` rows,
  `{cwd}` walk-up bound, `reader_quote` joins, `~/.omp/plugins/node_modules/*/skills`).
  Adjacent but non-overlapping: kumitate's dirs.ts census names
  `skill-descriptions.db` as a *member* of `~/.omp/agent`; kotoba's round-86/87
  work grounds the *skill discovery providers* that feed that db. Different
  surface, same binary.
- **mori-shokunin** — oh-my-pi async-job internals only (S098–S104); no skill
  loader content.
- **chousa-shokunin, kagi-shokunin, kaidoku-shokunin, kama-shokunin,
  kotodama-shokunin, revenger-shokunin, tsukuroi-shokunin** — grep hits are
  unrelated (pathlib `parents`, folktale phylogenetics, OpenBao tokens, REA
  skills, boot repair). No omp skill-root or loader-quote content.

## 3. Cross-lane consequence

**Nothing contested; one adjacent lane worth noting.** kumitate-shokunin holds the
oh-my-pi *agent-directory* census (dirs.ts member names, writers, modes) while
kotoba-shokunin now holds the *skill discovery* semantics (which roots omp walks,
which code joins each path, precedence/bounds). The surfaces are complementary —
both cite `discovery/builtin.ts` and `dirs.ts` at overlapping tags (kumitate
v18.12.6/45c35e40 + v18.15.0/3fedf8d5; kotoba ELF sha256 6737ee24…/v18.15.0) —
but no row duplicates another. Watch item for future rounds: if kumitate ever
extends its census into `discovery/*.ts` skill providers it will collide with
S255/S256/round-87's ledger; today it does not.

## Overlap verdict

`overlap: package=none (rounds ≤16 only; staged S256 id collides with lane S256 but is a different source — agentskills.io page already held as lane S002), siblings=[kumitate-shokunin (adjacent omp census, no loader-semantics overlap)], consequence=none — no duplication to avoid, no contested scope; note the staged-vs-lane S256 id collision for the operator at adopt time`
