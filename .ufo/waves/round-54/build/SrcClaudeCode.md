Result: DONE — the Claude Code slice of C1 is sourced and counter-conformant in a sandbox clone (counter prints `Claude Code  BACKED`, `--fetch` finds the quote `1 of 1`), and this report delivers the registry row, fetch record, entry row, Gate rows and SKILL.md table row as text for the L1 to integrate; the lane itself carries none of it yet (grep for `S053` and for `### Description thresholds by client` in the lane both return 0).

Seat: SrcClaudeCode (leaf). Lane read-only; every write below happened in the sandbox clone
`/fast/scratch/hyaku/kotoba-r54/SrcClaudeCode/kotoba-shokunin`, prototype commit `3c5e659`
("scratch: prose precision", local, never pushed). Clone base `7ad05d342d7505ab674a5ebcf5ac1106b2f45c39`.

- Behaviour delivered (as text, for you to integrate): two SOURCES rows (S053, S053b), one entry file a
  `## Per-client record` row each for Claude Code, a lesson `## Gate` row per registry row, one
  `### Description thresholds by client` row, and two `corpus/README.md` coverage-map rows.
- Gates: `check_description_thresholds.py` (prototype `--root`) prints `backed 1 of 7`, exit 1 — the
  correct verdict for one client against target 4 — and `--fetch` finds the quote `1 of 1`; its
  `--self-test` is `0 failure(s) over 22 assertions`, exit 0. `verify_corpus_integrity.py --no-baseline`
  prints `8/9 checks pass`, the single drift pre-existing. `verify_skill_checklist.py` keeps
  `line_budget` PASS and fails only the two citation checks that fail identically at the pristine tip.
- Touched surfaces: my own files only — this report. Delivered text touches `corpus/SOURCES.md`,
  `corpus/knowledge/skill-listing-thresholds-round54.md` (new), `corpus/lessons/round-54.md` (new),
  `SKILL.md`, `corpus/README.md`.
- Out of scope: client behaviour, the other six clients, S053b renumbering, and any lane edit.

## 1. Fetch record (what I actually opened, 2026-10-22 UTC)

| # | URL | fetched (UTC) | HTTP | bytes | sha256 |
|---|---|---|---|---|---|
| 1 | https://code.claude.com/docs/en/skills.md | 2026-10-22T21:15:56Z | 200 | 111,928 | `d1359f0c64371b3f2e267069d9f752418466abadb2765eca2929ecbee4ce0b2b` |
| 2 | https://code.claude.com/docs/en/settings-reference.md | 2026-10-22T21:15:56Z | 200 | 413,033 | `022e35adb2721a940aff2eb1f2aab9a3aabbf4171b46c01e103aaf2dcd1c143d` |
| 3 | https://code.claude.com/docs/en/skills (served HTML, same page as row 1) | 2026-10-22T21:16:55Z | 200 | 1,234,519 | `cd766e720c1c42d92faa98605a444742c329132b5cca2f939df6a8cc5f69bc92` |
| 4 | https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md | 2026-10-22T21:18:45Z | 200 | 1,070,244 | `121129bcb4d33f3bafe4ea5bc30b4f6d5ec057e886030f84b62648c3115c2c49` |
| 5 | https://raw.githubusercontent.com/anthropics/claude-code/5ed799e5cc56bea9efff57398ca43e31d82784ff/CHANGELOG.md | 2026-10-22T21:19:52Z | 200 | 1,070,244 | `121129bcb4d33f3bafe4ea5bc30b4f6d5ec057e886030f84b62648c3115c2c49` (byte-identical to row 4, `cmp` silent) |
| 6 | https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md (canonical page for row 5) | 2026-10-22T21:19:20Z | 200 | 392,307 | `c3264efbe695f323631b2cd990f4f45996c3c707a31a83c2862d857d7dbe4760` |

Fetched bytes are kept at `/fast/scratch/hyaku/kotoba-r54/SrcClaudeCode/{skills.md,settings-reference.md,skills.html,CHANGELOG.md,CHANGELOG.5ed799e.md,CHANGELOG.blob.html}`.

Pinned commit for row 5: `git ls-remote https://github.com/anthropics/claude-code main` →
`5ed799e5cc56bea9efff57398ca43e31d82784ff refs/heads/main`.

Served page vs docs source, two notes:

- For skills, the `.md` endpoint and the served HTML agree. I ran the counter's own normalization
  (drop tags, unescape entities, strip backticks/asterisks/underscores, collapse whitespace, lowercase)
  over both artifacts and the 15-word quote is a substring of each: `skills.md` True, `skills.html` True.
- The same two routes served different bytes 12 hours apart, and the sentence did not move. S022 records
  the 09:41:02Z fetch of `skills.md` as 111,557 B, sha `cdfcb0df…`, and of the HTML route as 1,233,129 B,
  sha `10219534…` (`corpus/SOURCES.md:35`); my 21:15:56Z / 21:16:55Z fetch is 111,928 B and 1,234,519 B
  with the hashes in § 1. So a byte count in a row is a timestamp, not an identity for this page — which
  is why the S053 row records its own hashes and does not reuse S022's, and why the quote, not the size,
  is what the counter re-checks with `--fetch`.
- For the changelog, the canonical GitHub page is a client-rendered shell: the 392,307-byte served HTML
  contains neither `1,536` nor `listing cap` (`grep -c` → 0), so the readable artifact is the raw
  endpoint. That is why the row's URL is the raw URL at the pinned commit, and the blob page is recorded
  as opened with its difference named.

## 2. `corpus/SOURCES.md` rows (11 cells each; paste verbatim)

| S053 | Claude Code — Extend Claude with skills — https://code.claude.com/docs/en/skills.md | docs | A | Claude Code's documented limits on how much of a skill `description` reaches the model: the per-entry cap in its skill listing, the listing's character budget, and the settings that raise either (vendor documentation, not a measurement of the client binary) | § Frontmatter reference, `description` row (`skills.md:389`) and `when_to_use` row (`:390`); § Skill descriptions are cut short (`skills.md:1205-1213`); settings-reference § `skillListingBudgetFraction` (`settings-reference.md:2455-2469`) and § `skillListingMaxDescChars` (`:2471-2485`); fetched as https://code.claude.com/docs/en/skills.md (200, 111,928 B, sha256 `d1359f0c…`) and as the served HTML https://code.claude.com/docs/en/skills (200, 1,234,519 B, sha256 `cd766e72…`) on 2026-10-22; settings-reference fetched 2026-10-22T21:15:56Z (200, 413,033 B, sha256 `022e35ad…`) | `description` and `when_to_use` text is truncated at 1,536 characters in the skill listing; the budget scales at 1% of the model's context window | mined | 2026-10-22 | 90d | corpus/knowledge/skill-listing-thresholds-round54.md |
| S053b | Claude Code — CHANGELOG (skill description handling) — https://raw.githubusercontent.com/anthropics/claude-code/5ed799e5cc56bea9efff57398ca43e31d82784ff/CHANGELOG.md | docs | A | The release note that fixes the per-entry listing cap and its past-cap behaviour for Claude Code (vendor documentation, not a measurement of the client binary) | § 2.1.105 (`CHANGELOG.md:6398-6409`); pinned at anthropics/claude-code@`5ed799e5cc56bea9efff57398ca43e31d82784ff` (main, 2026-10-22); the raw bytes are byte-identical to https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md fetched 2026-10-22T21:18:45Z, and the canonical blob page https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md (200, 392,307 B) is a client-rendered shell that carries no changelog text in its served bytes | The per-entry cap was raised from 250 to 1,536 characters and a startup warning fires when descriptions are truncated | mined | 2026-10-22 | on-release | corpus/knowledge/skill-listing-thresholds-round54.md |

Both rows are `docs`/`A`: the first URL of row 1 is on `code.claude.com` and of row 2 on
`raw.githubusercontent.com`, which is the pinned host `provider/github.com/anthropics/claude-code` repo
in raw form (the counter's Claude Code host list is `code.claude.com`, `docs.claude.com`,
`docs.anthropic.com`, `platform.claude.com`, `github.com/anthropics/claude-code`,
`verifiers/check_description_thresholds.py:86-88`; the counter only checks the row named in the entry's
`row` cell, which is S053). S053b is yours to renumber as assigned.

Cell level: 11 cells, no `|` inside a cell, `source` = title — canonical URL, `anchor` = section + line
numbers + the pinned revision, `teaches` = one benefit drawn from quotes I fetched, `status` = `mined`
because `used-by` names the entry, `recheck` 90d for the docs page and `on-release` for the changelog,
whose content is keyed to version headings and removal notes rather than to calendar time.

## 3. Entry `corpus/knowledge/skill-listing-thresholds-round54.md`

The file does not exist in the lane (`ls` → No such file or directory). Create it with this content; the
per-client table is the cell the counter reads (`## Per-client record`, header
`client | row | quote | location | reading`).

```
source: S053 (https://code.claude.com/docs/en/skills.md, `skills.md:389, 390, 1205-1213`; settings-reference.md:2455-2485), S053b (https://raw.githubusercontent.com/anthropics/claude-code/5ed799e5cc56bea9efff57398ca43e31d82784ff/CHANGELOG.md, § 2.1.105 `CHANGELOG.md:6409`)
verified-at: 2026-10-22
recheck: python3 -B verifiers/check_description_thresholds.py --rev <rev> --fetch

# Skill-listing thresholds by client (round 54)

Frontier area: Per-render consumption, offer-render half (`corpus/README.md` § Frontier) — how much
of a skill's `description` reaches the model in each client: the authoring maximum, the per-entry cut
in the skill listing, and the listing budget. Every page below was opened on 2026-10-22; fetch times,
byte counts and sha256 are in `corpus/lessons/round-54.md` § Gate. These are documentation statements,
not measured client behaviour.

## Per-client record

| client | row | quote | location | reading |
|---|---|---|---|---|
| Claude Code | S053 | "the combined `description` and `when_to_use` text is truncated at 1,536 characters in the skill listing" | `skills.md:389`, § Frontmatter reference, `description` row | A per-entry listing cut, not an authoring maximum and not the budget: the page puts the 1,536-character limit inside the skill listing and names no frontmatter limit for `description`, so past it the entry is truncated (the changelog records a startup warning) while the listing still carries every skill name (`:1207`). |

## Per-client detail — Claude Code

Two numbers, one cut and one budget. The cut is per entry: "each entry's combined text is capped at
1,536 characters regardless of budget" (`skills.md:1213`), which is why the listing entry — not the
skill file — is where the loss happens. The changelog records the cap raise and names what happens past
it: "raised the listing cap from 250 to 1,536 characters and added a startup warning when descriptions
are truncated" (S053b, `CHANGELOG.md:6409`, § 2.1.105), so an over-long description is truncated and the
session warns at startup; a later release says the warning now reports the count ("Improved the skill
listing truncation warning to show how many skill descriptions are affected", `:4972`, § 2.1.178).

The budget is a share of the context window: "The budget scales at 1% of the model's context window."
(`skills.md:1207`). Past the budget Claude Code "drops descriptions starting with the skills you invoke
least" (`:1207`) and writes a warning to the debug log (`:1209`); the settings page says the names stay:
"keeps every skill's name but drops the descriptions of the least-used skills"
(`settings-reference.md:2457`). Both limits are configurable: `skillListingBudgetFraction` defaults to
`0.01`, "which reserves 1% of the context window" (`settings-reference.md:2461`), and
`skillListingMaxDescChars` defaults to `1536` (`:2477`), where "longer text is cut at the cap" (`:2473`).
`SLASH_COMMAND_TOOL_CHAR_BUDGET` sets a fixed character count instead of the fraction, and a skill set to
`"name-only"` in `skillOverrides` lists it without a description (`skills.md:1213`; the changelog calls it
"collapses description", `CHANGELOG.md:5902`), which frees its share of the budget for other skills.

## What follows for the craft

1. Front-load the trigger words. Only the first 1,536 characters of `description` plus `when_to_use`
   reach the listing, whatever the budget, so text after that point competes only when the user types
   `/skill-name`.
2. Treat the budget as shared, not per skill. One long description can push another skill's description
   out of the listing, so trimming your own description is not the only lever: `"name-only"` on the
   skills you never want auto-invoked keeps budget for the ones you do.
```

Deliverable (3), the entry row on its own:

```
| Claude Code | S053 | "the combined `description` and `when_to_use` text is truncated at 1,536 characters in the skill listing" | `skills.md:389`, § Frontmatter reference, `description` row | A per-entry listing cut, not an authoring maximum and not the budget: the page puts the 1,536-character limit inside the skill listing and names no frontmatter limit for `description`, so past it the entry is truncated (the changelog records a startup warning) while the listing still carries every skill name (`:1207`). |
```

Quote: 15 whitespace-separated words, taken byte-for-byte from `skills.md:389`, contains `1,536`
exactly as the page writes it (comma inside the number, no space). The two backticked words are part of
the fetched bytes; the counter removes backticks on both sides for its `--fetch` substring test.

## 4. Lesson `corpus/lessons/round-54.md` § Gate rows

The lesson file does not exist in the lane yet. Rows are the round-53 Gate shape
(`row | URL | opened (UTC) | bytes, sha256 | quote (≤25 words) | location | seat`); the counter reads
only `## Gate`, a first cell that is one `S###`, and the double-quoted strings in the other cells.

```
| S053 | https://code.claude.com/docs/en/skills.md | 2026-10-22T21:15:56Z | 111,928 B, `d1359f0c…` | "the combined `description` and `when_to_use` text is truncated at 1,536 characters in the skill listing" | `skills.md:389` | SrcClaudeCode |
| S053b | https://raw.githubusercontent.com/anthropics/claude-code/5ed799e5cc56bea9efff57398ca43e31d82784ff/CHANGELOG.md | 2026-10-22T21:19:52Z | 1,070,244 B, `121129bc…` | "raised the listing cap from 250 to 1,536 characters and added a startup warning when descriptions are truncated" | `CHANGELOG.md:6409`, § 2.1.105 | SrcClaudeCode |
```

The S053 quote is character-identical to the entry's quote cell; that equality is one of the counter's
tests, and it held in my prototype run.

## 5. Draft `SKILL.md` decision-table row

Deliverable (5), 4 cells, header `Client | Documented threshold | Past the threshold | Action`:

```
| Claude Code | 1,536 characters per entry (`description` + `when_to_use`), whatever the budget; listing budget 1% of the context window (`0.01` default, `skillListingBudgetFraction`) | Truncated at the cap, with a startup warning (v2.1.105 raised the cap from 250); past the listing budget, descriptions of the least-invoked skills are dropped and every skill name stays | Put the key use case first and keep the entry under 1,536 characters; raise `skillListingMaxDescChars` or `skillListingBudgetFraction`, or set low-priority skills `"name-only"` to leave budget for yours |
```

Placement I prototyped: a new section after the § Decision tables table-rule paragraph and before
`## Compression rules` (`SKILL.md:195-199` in the prototype; the module-bound box, `File ≤ 600 lines` at `SKILL.md:272`
at this tip, is untouched by a table). Six lines of block (heading, blank, header, separator, row, blank).

## 6. Corpus index rows (the coverage map needs them; the corpus gate measures it)

```
| Skill-listing thresholds by client (round 54) | `knowledge/skill-listing-thresholds-round54.md` | the documented number that limits how much of a skill `description` reaches the model, per client: an authoring maximum, a per-entry cut in the skill listing, or a listing budget, and what the client does past it (S053 Claude Code: `skills.md:389` truncates the entry at 1,536 characters, `skills.md:1207` budgets the whole listing at 1% of the context window, `settings-reference.md:2461/2477` the two settings; S053b: the changelog entry that raised the cap from 250 and added the startup warning); checked by `../verifiers/check_description_thresholds.py` (`description thresholds backed <K> of 7 clients`) |
| Round-54 lessons | `lessons/round-54.md` | <the L1 writes the basis text at landing; my prototype used a placeholder and it only needs to exist for `corpus.index.unindexed`> |
```

The first row's basis text names only my client; widen it when the other six rows land.

## 7. Verification I ran (sandbox clone, never the lane)

Counter, on the prototype working tree (all four files in place):

```
$ python3 -B verifiers/check_description_thresholds.py --root .
Claude Code  BACKED
Codex        no SKILL.md rows naming client: 0 (need 1); entry rows naming client: 0 (need 1)
... (VS Code, Copilot CLI, Gemini CLI, Cursor, opencode likewise)
description thresholds backed 1 of 7 clients
exit=1
$ python3 -B verifiers/check_description_thresholds.py --root . --fetch
description thresholds backed 1 of 7 clients
description thresholds found on the live page 1 of 1
exit=1
$ python3 -B verifiers/check_description_thresholds.py --self-test
self-test: 0 failure(s) over 22 assertions
exit=0
```

`Claude Code  BACKED` prints with no `why` item, and `--json` shows the row's resolved fields:
`"row": "S053"`, `"url": "https://code.claude.com/docs/en/skills.md"`, `"quote": "the combined ..."`,
`"tokens": ["1,536","1%","0.01"]`, `"backed": true, "why": []`. Exit 1 is the correct verdict for a
one-client prototype: the target is 4 and the counter counts 1.

Corpus integrity gate, `--no-baseline` (it compares against a pinned count baseline my slice changes by
design):

```
$ python3 -B verifiers/verify_corpus_integrity.py --no-baseline
8/9 checks pass; DRIFT: corpus.index.unindexed
observed: unindexed 1 ['corpus/lessons/round-53-verifier-spotcheck.md']
(from the same run's --json: stale_patterns 0, missing_paths 0, commit_unresolvable 0, commit_nonhash 0)
```

That single drift is pre-existing, not mine: a pristine clone at `7ad05d3` prints the same
`unindexed 1 ['corpus/lessons/round-53-verifier-spotcheck.md']` with `stale 0`
(`/fast/scratch/hyaku/kotoba-r54/SrcClaudeCode/kotoba-shokunin-baseline`). My two index rows removed
the drift my own files would have added.

Skill checklist gate, prototype: `PASS trigger.line_budget: evaluated 558 — 558 lines within budget 600`;
`PASS trigger.name_directory`; the two remaining FAILs are `trigger.citation_resolves` (line 548
`../.ufo/reports/round-7/kotoba.md`) and `governance.citation_resolves` (LOG.md citations to `../.ufo/…`
and `../PROTOCOL.md`). The pristine tip clone has the same two FAILs, plus `name_directory` because that
clone directory is not named `kotoba-shokunin`; in a correctly named clone my slice adds no failure.

Plan erratum 3 guards, measured at the plan commit `e3371548`:

```
$ git show e33715486a45a4a857b64c30e6b695f7995858b8:corpus/SOURCES.md | grep -c "| S053"
0
$ git show e33715486a45a4a857b64c30e6b695f7995858b8:SKILL.md | grep -c -F -e '1,536' -e '1%'
0
```

So guard (a) holds (S053 and S053b are absent at the plan commit, i.e. opened this round) and guard (b)
holds for this client by a wide margin: `1,536` and `1%` are both new to SKILL.md. Guard (c) holds:
`--fetch` found the quote on the live page 1 of 1.

## 8. Findings

1. **Three numbers, three kinds, one page.** Claude Code documents (i) a per-entry listing cut — the
   combined `description` + `when_to_use` is truncated at 1,536 characters in the skill listing
   (`skills.md:389`) and the cap applies "regardless of budget" (`:1213`); (ii) a listing budget — 1% of
   the model's context window (`:1207`), default `0.01`, configurable (`settings-reference.md:2461`);
   (iii) the per-entry cap's own setting, `skillListingMaxDescChars`, default `1536`
   (`settings-reference.md:2477`). Past the cut the text is truncated and the changelog records a startup
   warning (`CHANGELOG.md:6409`); past the budget the descriptions of the least-invoked skills are
   dropped while every name stays (`skills.md:1207`, `settings-reference.md:2457`), and a warning goes to
   the debug log (`skills.md:1209`). Those are two different warnings and I kept them apart.
2. **Not an authoring maximum — bounded to this page.** The skills page states no size limit on the
   `description` the frontmatter accepts: `grep -c "1024\|1,024" skills.md` → 3, and all three are the
   page's own JS byte formatter (`:1085`, `:1086`, `:1134`); the only numeric accept limit on the page is
   the 500-character `compatibility` row (`:407`). Anthropic's 1,024-character description maximum lives
   on a different page (S019, `best-practices.md:161`, already in the corpus). The entry's reading says
   "not an authoring maximum" and is bounded to `skills.md`; it does not claim what the loader does with
   a 2,000-character description. This negative is not new either: S022 (round 51) already swept this
   page for `1024` and recorded the same three byte-formatting hits (`corpus/SOURCES.md:35`), so the
   entry restates a prior hold and adds no ground. [INFERENCE] a longer description is accepted and only
   its listing entry is cut; the page implies it but does not say it, so the row does not.
3. **Prior holds, so the new content is named precisely.** The 1,536-character cap already sits in
   `corpus/knowledge/sibling-overlap-census-round49.md:221` and
   `corpus/knowledge/skill-selection-rules-round50.md:48`, and the 1% budget with the drop order at
   `sibling-overlap-census-round49.md:155`. S022's row goes further: it already names
   `skillListingMaxDescChars` and "regardless of budget" and records the no-1,024-cap sweep
   (`corpus/SOURCES.md:35`). Counted in the lane at this tip, `grep -r -F` over `SKILL.md` and `corpus/`:
   `skillListingBudgetFraction` 0 hits, `SLASH_COMMAND_TOOL_CHAR_BUDGET` 0, `skillListingMaxDescChars` 1
   (S022), `startup warning` 0, `250 to 1,536` 0, `settings-reference.md` 0. So the genuinely new ground
   this slice carries is the settings-reference page itself (never opened in this lane), the budget's
   `0.01` default, the two raising levers, the cap's `250 → 1,536` history and the truncation warning;
   the cap, its "regardless of budget" property and the 1,024 negative are re-sources for this round's
   table, not discoveries. Do not present the row as new ground on the cap itself, and expect a reviewer
   to ask why this is a fresh row and not a `used-by` edit on S022 — the answer is that the fresh row is
   the L1's assignment and that it opens a page S022 never touched; the alternative is one line in S022's
   `used-by` plus the same Gate quote, which the frozen counter accepts equally
   (`check_description_thresholds.py:271-290` reads tier, kind, status, opened, used-by and host, not
   novelty).
4. **A corpus gate rule shaped the row text.** `verify_corpus_integrity.py:149` reads the literal word
   `commit` followed by any backticked token as a lane commit pointer and fails an unresolvable one. My
   first S053b anchor said `upstream commit \`5ed799e5…\`` and the gate reported
   `commit_unresolvable: corpus/SOURCES.md:67` (exit 1). Rephrased to
   `pinned at anthropics/claude-code@\`5ed799e5…\`` the count went to 0 — the round-53 S050 correction
   ("at commit `cfb894a5`" → "zed-industries/zed@`cfb894a5`") is the same class, and the fix here is the
   same. Keep the `@` form when integrating; do not put the phrase "upstream commit `…`" back.
5. **Line budget is now the binding constraint, not this row.** Lane `SKILL.md` is 585 lines (another
   seat's C2 Gate-registry table landed while I worked); my block is 6 lines, so the file goes to about
   591, and six more client rows take it to about 597 against the `File ≤ 600 lines` box at `SKILL.md:272`. Any
   additional C1 prose (a "read this when" line, a note under the table) does not fit. If the L1 wants
   the safety margin back, the compressible material is elsewhere, not in the seven rows.
6. **Only one row per client.** The counter requires exactly one SKILL.md row and exactly one entry row
   naming each client; a second Claude Code row from another seat prints
   `SKILL.md rows naming client: 2 (need 1)` and the client stops counting. Whoever integrates must own
   the Claude Code row alone.
7. **Pre-existing lane drift, not a routed defect yet:**
   `corpus/lessons/round-53-verifier-spotcheck.md` has no coverage-map row (`corpus.index.unindexed` = 1
   at `7ad05d3`, measured in a pristine clone). Rounds 46, 48 and 49 recorded the same landing shape and
   were indexed a round later. I did not touch it; a one-row fix would make the corpus gate green.
8. **The counter's limits that matter to this row** (plan erratum 3, restated because it frames what the
   evidence can say): the `opened 2026-10-22` test is a date, not "new this round"; the number need not
   be about `description`; any subdomain of a pinned host passes; `--fetch` follows redirects without
   re-checking the host; `--json` is followed by the summary line. My row's evidence is what I fetched
   and the commands above, no more.

## 9. Not done / out of scope

- Nothing written in the lane except this report; no verifier, plan, SCORECARD, LOG, SOURCES or SKILL.md
  edit; no git write in the lane; no jj command.
- No client-behaviour measurement (no `claude -p`, no version probe): every statement is what the page
  says. The `--fetch` result is a page-presence test, not a render test.
- No Q30 three-part sweep: the client documents numbers, so the negative was not needed. The one absence
  I do claim (no frontmatter limit on `description` on `skills.md`) is bounded to that page and evidenced
  by the greps in finding 2, with the caveat that it is not a changelog + docs-tree + corpus sweep.
- No decision on S053b: renumbering is the L1's per the assignment.
- No tool installs or upgrades this seat (nothing was needed).

## 10. Artifacts

- This report: `.ufo/waves/round-54/build/SrcClaudeCode.md`.
- Sandbox clone and prototype: `/fast/scratch/hyaku/kotoba-r54/SrcClaudeCode/kotoba-shokunin` at local
  commit `3c5e659` (SOURCES rows `:66-67`, entry `corpus/knowledge/skill-listing-thresholds-round54.md`,
  lesson `corpus/lessons/round-54.md:7-8`, SKILL.md table `:195-199`, README index `:83-84`).
- Pristine tip checkout for the drift comparison:
  `/fast/scratch/hyaku/kotoba-r54/SrcClaudeCode/kotoba-shokunin-baseline`.
- Fetched bytes and their hashes: `/fast/scratch/hyaku/kotoba-r54/SrcClaudeCode/*.{md,html}` (six files,
  hashes in § 1).
