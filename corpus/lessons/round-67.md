---
author: kotoba L1 (round 67, hyaku run 5)
date: 2026-10-24
round: 67
lane: kotoba
---

# Round 67 — lesson (kotoba, hyaku run 5)

## Gate

The round assimilated from the read-only campaign package
`/home/vgpnk/Projects/shokuknow/merge/kotoba/` on **one theme**: the instruction-authority
ladder and the boundary it draws around skill bodies. Nothing in that tree was written, committed
or executed; only its bytes were read.

**Admit (3 source rows, 1 knowledge entry).** Every cited source was re-opened by this round —
the campaign's own `opened` date and quote prove nothing about this lane (CORPUS.md rule 1).

- **S123 — OpenAI Model Spec (August 18, 2026)**, https://model-spec.openai.com/2026-08-18 —
  opened 2026-10-24 by the round-67 scout seat (`ScoutModelSpec`, session log
  `.ufo/waves/round-67/w1/logs/ScoutModelSpec.log`). Located under `# Instructions and levels of
  authority` -> `# The chain of command`; the located quote is: “Instructions with higher
  authority override those with lower authority.” (9 words). The earlier section lists Root,
  System, Developer, User, Guideline; the chain-of-command ordering adds **No Authority**. The
  page header renders `August 18, 2026`.
- **S124 — anthropics/skills, skill-creator/SKILL.md**, at tree `dbd4588`, opened 2026-10-24 by
  `ScoutSkillCreator` (log `.ufo/waves/round-67/w1/logs/ScoutSkillCreator.log`). Located under
  `# Description Optimization` -> `# Step 1: Generate trigger eval queries`; the located quote is:
  “Create 20 eval queries — a mix of should-trigger and should-not-trigger.” (12 words). The
  numbers live in `# How skill triggering works` and `# Step 3: Run the optimization loop`:
  “evaluates current description (running each query 3 times to get reliable trigger rate)”, a
  60/40 train/test split and up to 5 iterations. The tree pin is the same one the lane already
  holds for **S012** (same repo, same tree, a different file — S012's registered URL is the
  `tree/` form and its evidence is `scripts/quick_validate.py:79-81`), so this is a same-tree
  neighbour and **not** a duplicate-URL row.
- **S129 — Many-Tier Instruction Hierarchy in LLM Agents**, https://arxiv.org/abs/2604.09443 —
  opened 2026-10-24 by `ScoutArxiv` (log `.ufo/waves/round-67/w1/logs/ScoutArxiv.log`), record v4.
  Located in the abstract; the located quote is: “assumes a fixed, small set of privilege levels
  (typically fewer than five) defined by rigid role labels” (17 words). The abstract also states
  up to 12 levels of conflicting instructions, 853 agentic tasks (427 coding, 426
  instruction-following), 46 real-world agents, and about 40% accuracy for frontier models.

**Reject (1 part of a staged row).**

- **Refused — the staged S123 row's “document version 2026/08/18” claim.** The staged row
  (`/home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md`, row S123) asserts the
  document version as the literal string `2026/08/18`. Re-opened on 2026-10-24, the page's header
  renders `August 18, 2026` and the literal `2026/08/18` **does not appear in the fetched main
  text** (`ScoutModelSpec` log). The adopted row therefore cites the date as the page renders it
  and makes no version-string claim. **Flip condition:** the literal `2026/08/18` appears verbatim
  on a versioned permalink or in the page's own metadata; on that evidence the version claim may
  be admitted and the row's `anchor` cell corrected by an appended notice.
- **Refused — the staged rows as a class are not appended as-is.** The package's 164 rows carry
  campaign-schema cells (prose `recheck` cells such as “90d — re-fetch … (ran 2026-10-23)”) and
  the campaign's own `opened` date. Only the three rows the admitted entry cites were transformed
  into the lane's own 11-column schema and re-grounded with this round's access date
  (2026-10-24). The stripped prose from each `recheck` cell is recorded here: S123 — “re-fetch
  https://model-spec.openai.com/2026-08-18 and confirm the five levels and the override sentence
  are unchanged”; S124 — “re-fetch the pinned tree and confirm the 20-query, 60/40, 3-run,
  5-iteration numbers still read the same”; S129 — “re-check arXiv:2604.09443 for a v2”. Each
  row's `recheck` cell now holds the bare cadence `90d` and the condition lives in this Gate.
- **Not adopted (not a reject — out of theme).** The package's other 161 staged rows and 76
  entries are not this round's theme; they were neither screened nor admitted, and the lane
  adopts nothing from them.

**Id collision.** The lane registry held 120 rows (last id S122) and the staged set's first id is
S123, so the collision set is empty; the check ran in scratch with the census parser's 0-3-space
pattern (`.ufo/waves/round-67/w1/controls/reg-ids`, `staged-ids`, `collisions` — 120 / 164 / **0
collisions**). The guard was proved non-vacuous on a scratch fixture: a row with two leading
spaces (`  | S002 |`) is caught by the 0-3-space pattern and missed by a column-zero-only pattern.
No renumbering was needed and no adopted citation was re-pointed.

**Spot-check.** This L1 seat has no independent non-author reviewer; **no round-67 admit/reject
spot-check is claimed**. The r66 non-author verifier spot-check was read and its routed note (the
corpus-index omission below) is worked here.

## Mistakes

- **M104 — class: corpus-index omission by an external writer.** Evidence: the hyaku run card
  `/home/vgpnk/Projects/shokunin/.ufo/waves/hyaku/inline-run-20261023.md:181-185` records that
  kotoba r66's post-closure corpus-integrity observation is red at tip `2a8eba56` “because the
  closure spot-check is an unindexed corpus file”, and routes the issue to round 67 rather than
  applying it retroactively. The measured base control
  (`.ufo/waves/round-67/w1/controls/C1-base.txt`) shows the primary gate at `5/9 checks pass`,
  exit 1, with `unindexed: corpus/lessons/round-66-verifier-spotcheck.md` and three census DRIFT
  cells. Captured-by: `none` — no QUALITY criterion named the closure-authored spot-check as a
  corpus file that the coverage map must index, and the index census only counts what the
  coverage map already promises. Fix: index the r66 closure spot-check in the coverage map with
  the same shape as the r60/r61 rows, and re-record the census baseline from the gate's own
  measurement. Shown able to fail: the two half-repair control worlds (K2 index-row-only, K3
  baseline-only) each leave the gate red (`.ufo/waves/round-67/w1/controls/C1-half-controls.txt`).
- **M105 — class: an identifier asserted about a source that the source does not carry.** Evidence:
  the staged S123 row asserts the document version as the literal `2026/08/18`; the re-opened
  page renders `August 18, 2026` and the literal is absent from the fetched main text
  (`ScoutModelSpec` log). Captured-by: Q42/Q23 — a rule attributed to an authority carries a
  located quote from that authority, and a claim about an identifier must be read off the
  re-opened bytes. Fix: the adopted row cites the rendered date, the version-string claim is
  refused with a flip condition, and the lesson Gate carries the located quote and the access
  date. Shown able to fail: the counter's `verified-at`/`anchor` conjuncts reject an entry whose
  quote is not the row's, and the base control prints `0 of 1`.
- **M106 — class: a read-only seat's findings were produced but not written.** Evidence: the
  wave-1 scout seats (`ScoutModelSpec`, `ScoutSkillCreator`, `ScoutArxiv`, `ScoutQwen`,
  `ScoutConsiderthese`, `ScoutBaselineShape`) carry a read-only tool allowlist in their host
  profiles, so each seat reported in its session output and **no** seat report file was written
  (each log ends “Report not materialized: no write-capable tool is available to this
  read-only seat”). Captured-by: `none` — the wave item told the seat to write a report file
  without stating that the role profile denies the write tool. Fix: the seat's own findings are
  preserved verbatim in the committed session logs under `.ufo/waves/round-67/w1/logs/`, and the
  Gate quotes them; a future wave must either give the scout profile a write tool or accept
  session-output reports as the seat's artifact. Shown able to fail: the count of written seat
  reports (2 of 32) against the count of session logs carrying a findings section (32 of 32).

## Status changes

- S123, S124, S129: new rows written directly as `mined`; `opened` is this round's date
  2026-10-24; `recheck` is the bare cadence `90d` with the stripped condition in this Gate;
  `used-by` lists `corpus/knowledge/instruction-authority-ladder-round67.md` and
  `corpus/lessons/round-67.md`. **No existing row's `status`, `recheck` or `used-by` changed.**

## Evidence pins

- The claim freeze, the predicates and the do-nothing controls are in `plans/round-67.md`.
- The wave-1 spec is `.ufo/waves/round-67/w1-spec.json`; the validator's rendered task call and
  the seat results are `.ufo/waves/round-67/w1/seat-results.json` and
  `.ufo/waves/round-67/w1/logs/`.
- The C1 base control is `.ufo/waves/round-67/w1/controls/C1-base.txt`; the id-collision outputs are
  `.ufo/waves/round-67/w1/controls/{reg-ids,staged-ids,collisions}`; the pre-append census of the
  scratch mirror is `.ufo/waves/round-67/w1/controls/census-validate-append.txt`.
