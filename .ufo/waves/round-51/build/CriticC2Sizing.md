# CriticC2Sizing — round-51 C2 counter attack (build wave)

Result: **FAILS** — the C2 statement as worded, measured by the delivered counter
`verifiers/check_overlap_levers.py` (LeverGuard clone, sha256 `1545b256…be2b63`). Four constructed
worlds that each break a clause of the statement print `overlap levers backed 7 of 7 clients`, exit 0.
C2 becomes **HOLDS-BOUNDED** only with the re-sized statement and the script fixes F1–F6 below. A
prototype of those fixes rejects all four worlds (0 of 7, exit 1) and still passes an honest world
built from real vendor quotes (7 of 7, exit 0; `--fetch` 7 of 7).

Seat: KotobaR51.CriticC2Sizing (critic). Base `43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10`. Started
2026-10-22T14:18Z. No tools installed or updated. No lane files written except this report. Scratch:
`/fast/scratch/hyaku/kotoba-r51/build/CriticC2Sizing/` (`make_worlds.py`, `fixed_guard.py`, `worlds/`).

## Which clauses the counter turns on (Q26)

| # | Statement clause | Turned on by the offline counter? | By `--fetch`? |
|---|---|---|---|
| 1 | the table is in `SKILL.md` § Anti-patterns | no: the first line anywhere containing the marker | no |
| 2 | K of 7 pinned clients, one row each | yes: pinned `CLIENTS`, exact cell, duplicates rejected | — |
| 3 | the lever is "documented", meaning the client vendor's own docs | no: kind, tier, host and client are never read | no |
| 4 | the lever is "other than description wording" | partly: only the substring `description` in the key term | no |
| 5 | the lever stops one of two overlapping skills being chosen | **no**: nothing reads what the lever does | no |
| 6 | the key term is in the quote | yes, but as a raw substring (one letter is enough) | — |
| 7 | the quote is verbatim from the page | no | yes, but anywhere on today's page; the cited line is never checked |
| 8 | the quote cites a `mined` row | only the status cell; no access record is read | no |
| 9 | the row's `used-by` names the entry | substring of the stem `skill-overlap-levers-round51` | — |

## False-pass constructions (all run; each prints `backed 7 of 7`, exit 0, on the delivered script)

**A — one page backs all seven clients, and the table is in an HTML comment.** Every row cites S025
(the VS Code page) with key `disable-model-invocation` and the quote "Use the `user-invocable` and
`disable-model-invocation` frontmatter properties to control how each skill is accessed". The marker
and table sit inside `<!-- … -->`, and the file has no `## Anti-patterns` heading. Clauses 1 and 3
break, and `--fetch` would pass too, because the quote really is on the VS Code page. Caught by the
design: no. Fix F1 (section scope) and F2 (vendor identity).

**B — real vendor pages and real quotes, but none of them is an overlap lever.** All seven quotes
are on their live pages (`--fetch`: `quotes found on live pages 7 of 7`, exit 0):
- VS Code, `user-invocable`. The page says it hides the skill from the `/` menu "while still
  allowing the agent to load it automatically" (`agent-skills.md:150`), which is the opposite of the
  claim. Claude Code's `user-invocable: false` likewise means "Only Claude can invoke the skill"
  (`skills.md:551`). This is the most plausible honest mistake at build time.
- Claude Code, `when_to_use`. This is wording: it is "Appended to `description` in the skill
  listing" (`skills.md:390`). It passes because the description filter is a substring test on the key
  term only.
- Gemini CLI, `enabled`, quoting "injects the name and description of all enabled skills into the"
  (`skills.md:200`). The term is generic, the sentence describes discovery, and the quote contains
  the word "description".
- opencode, `disable`, quoting "Completely disable skills for agents that shouldn't use them". The
  term is generic, and the lever turns off the whole skill tool, not one of two skills
  (`opencode-skills.md:192-219`).
- Codex, `skills.max_context_tokens`. This sets the listing budget, not overlap.
- Copilot CLI, `enabledPlugins`, and Copilot SDK, `plugin`. Both act on plugins, and the SDK row
  cites the CLI plugin reference (S028), a different client's page.

Clauses 3, 4 and 5 break. Caught by the design: no, and `--fetch` cannot catch it either, because the
fault is in what the quote means, not where it comes from. Fix F3 (reviewed lever list) and F4 (code
span).

**C — a fabricated quote.** Same as B, but the Gemini quote is invented: "Set `skills.disabled` to
stop Gemini from choosing one of two overlapping skills". Offline: 7 of 7, exit 0. `--fetch`:
`quotes found on live pages 6 of 7`, exit 1. This is the only construction the design catches, and
only on the optional `--fetch` path, which the headline does not cite. Fix F5.

**D — provenance.** Seven rows of kind `own-work`, tier C, at `https://example.com/notes`, status
`mined`. Their used-by is `corpus/knowledge/skill-overlap-levers-round51-rejected.md`, there is no
lesson § Gate record, the key term is `e`, and the quote is "the quote says nothing". Clauses 3, 6,
8 and 9 break. Caught by the design: no. The census does not cover it either:
`scripts/sources-census.sh:24-33` gives only the warning W01 for a tier-C `mined` row, raises E11
only if the used-by path is missing on disk, and has no Gate rule. The SOURCES header says access
evidence "lives in … the round lesson's `## Gate`" (`corpus/SOURCES.md:5-8`), and the contract
defines `mined` only as "cited by ≥1 path in `used-by`" (`CORPUS.md:103`). Fix F2 and F6.

**Also from reading the code:**
- `parse_sources` keeps the last of two rows with the same id (`out[sid] = …`), so a queued
  duplicate could be shadowed by a mined one. The census rule E03 catches duplicate ids, but the
  counter does not cite the census.
- `QUOTE_CELL` accepts any length and any parenthesised location, including `()`, so the 25-word
  bound and the location are unchecked.
- The delivered `normalize` change removes anything between `<` and `>` from both the page and the
  quote, which makes matching on live pages looser.

## Q25: shown able to fail?

The plan's mutants (`plans/round-51.md:38-40`, the self-test at script lines 482-548) are all
structural: row removed, status, used-by, term absent, `description`, duplicate, wrong id, table
absent, unknown client. The self-test's own control world is 7 of 7 with `https://example.com/doc-N`
sources, key terms `term0` to `term6` and quotes "quote with term0 inside" (lines 440-480). No vendor,
lever or overlap appears in it. So on clauses 1, 3, 5, 8 and 9 the counter is a census observable in
Q25's sense: no mutant falsifies their content, and the exit code does not change when they are
falsified.

## Smallest safe correction

The script fixes, each prototyped in `fixed_guard.py`:
- **F1.** Look for the marker and table only inside the `## Anti-patterns` span (up to the next
  `## `), after removing HTML comments and fenced blocks.
- **F2.** Pin `CLIENT_URL_PREFIXES` per client:
  - Copilot SDK: `docs.github.com/en/copilot/how-tos/copilot-sdk/`
  - Copilot CLI: `…/how-tos/copilot-cli/` and `…/reference/copilot-cli-reference/`
  - VS Code: `code.visualstudio.com/docs/`
  - Claude Code: `code.claude.com/docs/`
  - opencode: `opencode.ai/docs/`
  - Gemini CLI: `geminicli.com/docs/`
  - Codex: `learn.chatgpt.com/docs/` and `developers.openai.com/codex/`

  Also require the row's kind to be `docs`, `code` or `spec`, and its tier to be `A`.
- **F3.** Pin `LEVER_TERMS` per client: the reviewed key terms that remove one named skill from model
  choice. The prototype set is `disabledSkills`/`disabled_skills`; `copilot skill`/`disabledSkills`/
  `/skills disable`; `disable-model-invocation`; `disable-model-invocation`/`skillOverrides`; `deny`;
  `/skills disable`; `allow_implicit_invocation`/`[[skills.config]]`.

  Tradeoff: this moves the semantic judgment into the instrument. The judgment belongs to the
  reviewer (ReviewOverlapRows and the Src seats) and is frozen in code, so the statement must say
  "from the reviewed list" and must not present it as a measurement. Without F3, clause 5 has to
  leave the counted statement.
- **F4.** The key term must occur inside a backticked code span of the quote. This blocks `e`,
  `enabled`, `disable` and `plugin` as bare words.
- **F5.** Reject quotes over 25 words. The statement cites a `--fetch` run (UTC, `J of K`, exit
  code) as the guard for clause 7. It is a check of today's page, not the mined bytes; an optional
  stronger form also checks the cited line of the `.md` bytes.
- **F6.** Split used-by on `[,;]` and require the exact item
  `corpus/knowledge/skill-overlap-levers-round51.md`. Require the row id in
  `corpus/lessons/round-51.md` § Gate, read at `--rev`. Treat a duplicate row id as UNBACKED.

New self-test mutants, one per fix: `user-invocable` swap; a cross-vendor URL; a generic key term not
in a code span; no Gate record; a comment-hidden table; a used-by that only shares the stem; a quote
over 25 words.

## Re-sized statement (HOLDS-BOUNDED with F1–F6)

> `SKILL.md` § Anti-patterns carries an "Overlap levers by client" table that names, for K of 7
> pinned clients, a key term from the instrument's reviewed per-client list of skill-removal levers
> (disable list, permission deny, model invocation off), shown as a code span in a quote of at most
> 25 words in `corpus/knowledge/skill-overlap-levers-round51.md`. The quote cites a tier-A
> vendor-documentation row of `corpus/SOURCES.md` whose URL is under that client's pinned docs
> prefix, whose status is `mined`, whose used-by names the entry path, and which has a round-51 Gate
> record: 0 of 7 → 7 of 7. `--fetch` at <UTC> found J of 7 quotes on the live pages. A listed lever
> removes one named skill from model choice; it is not a documented tie-break between two matching
> skills.

If F3 is not taken, drop "for stopping one of two overlapping skills" from the counted statement.
Write instead "a key term quoted from that client's vendor docs", and record lever semantics as a
cited reviewer judgment (ReviewOverlapRows), not as a counted clause.

## Evidence (commands run in the critic scratch; exit codes verbatim)

- `python3 -B delivered/check_overlap_levers.py --self-test` prints `0 failures`, `10 assertions`,
  exit 0. The delivered script's sha256 is `1545b256…`. I first tested the earlier draft `6853ae79…`;
  its offline logic is identical and the only diff is the HTML-tag strip in `normalize`.
- `python3 -B delivered/check_overlap_levers.py --root worlds/<W>`, last line and exit code:

  | World | Delivered counter | Prototype `fixed_guard.py worlds/<W>` |
  |---|---|---|
  | A | `backed 7 of 7`, exit 0 | 0 of 7, exit 1 |
  | B | `backed 7 of 7`, exit 0 | 0 of 7, exit 1 |
  | C | `backed 7 of 7`, exit 0 | 0 of 7, exit 1 |
  | D | `backed 7 of 7`, exit 0 | 0 of 7, exit 1 |
  | H (honest control) | `backed 7 of 7`, exit 0 | 7 of 7, exit 0 |

- `--fetch` with the draft script, from 2026-10-22T14:22:45Z to 14:22:53Z:
  - world B: `quotes found on live pages 7 of 7`, exit 0;
  - world C: `quotes found on live pages 6 of 7` (Gemini CLI not found), exit 1.
- `--fetch` on world H at 2026-10-22T14:24:34Z: `quotes found on live pages 7 of 7`, exit 0. The two
  URLs I inferred returned 200 via `curl -L`: the Copilot SDK skills page (875,354 B) and the Copilot
  CLI add-skills page (625,849 B).
- Page bytes I read are peer fetches in `/fast/scratch/hyaku/kotoba-r51/build/`:
  - `SrcVSCode/agent-skills.md` (sha256 `de5ba34f…`), lines 150, 289
  - `ReviewOverlapRows/claude-skills.md` (`cdfcb0df…`), lines 389-390, 551
  - `ReviewOverlapRows/opencode-skills.md` (`f10ced73…`), lines 192-231
  - `src-gemini/skills.md`, line 200
  - `SrcCodex/build-skills.md` (`ed6e324f…`), lines 43, 218
  - `src-copilot-sdk/skills.md` (`64856ff4…`), line 809
  - `SrcCopilotCli/cli-plugin-reference.md` (`d0d362cc…`), lines 21, 31
