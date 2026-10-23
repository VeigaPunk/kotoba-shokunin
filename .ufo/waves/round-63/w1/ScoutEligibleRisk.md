# ScoutEligibleRisk

role: scout
item: ScoutEligibleRisk — over-rejection bound for planned `g9_conjunct` (C1)

Axes: (1) does a `;` / `and` split reject a cell that whole-cell A2 already accepts; (2) is each clause line-supported at `fwd_need`. Comma is inspected because the item names it; the planned rule does not split on it.

Rule applied, from `plans/round-63.md` (same split as the v32 draft at `verifiers/check_scoped_rules_v32.py:1061-1126`, not treated as frozen): split the action cell on `;` and on `\band\b` (case-insensitive) outside backticks. A clause with fewer than `MIN_CONTENT` (3) content words is skipped. Otherwise require `covered(clause, cited line) >= fwd_need(|W|)` where `fwd_need(n) = max(2, ceil(2n/3))`. Reject only when that fails and the same fraction holds against the page (`A2 G9: clause "…" is supported outside the cited line`). `action_conjunct` reaches G9 only after whole-cell forward, page-containment, and reverse all pass (`check_scoped_rules_v32.py:1144-1158`). Content words are v31's: lowercase `[a-z]{4,}` outside backticks and `S### :L`, minus `STOPWORDS` (`verifiers/check_scoped_rules_v31.py:314`, `:409-441`, `:1008-1018`, `:1035-1043`).

Evidence: numbers below are that import applied to the cells. No tools installed.

## Findings

1. **No eligible fixture is rejected. `eligible rows pass 4 of 4` holds under this split.** Cited line is the action sentence itself (`check_scoped_rules_v31.py:2209-2241`, action line `5 if S900 else 4` at `:2380-2381`), so every clause word is on the line.

| cell | split clauses | line support | G9 |
|---|---|---|---|
| S900 `;` | `Scope rules to specific files using YAML frontmatter` {scope, rules, specific, files, using, yaml, frontmatter} n=7 need 5 | 7/5 | pass |
| | `apply only when matching specified patterns.` {apply, matching, patterns, specified} n=4 need 3 | 4/3 | pass |
| S901 `and` | `Use multiple instruction files per topic` {multiple, instruction, files, topic} n=4 need 3 | 4/3 | pass |
| | `apply them selectively.` {apply, selectively} n=2 | <3 | skip |
| S902 `;` | ``Create a path-specific instruction file with an `applyTo` glob`` {create, path, specific, instruction, file, glob} n=6 need 4 (`with` is a stopword; `applyTo` is backticked out) | 6/4 | pass |
| | `use glob syntax to specify the files or directories the instructions apply to.` n=7 need 5 | 7/5 | pass |
| S903 none of `;`, `and`, `, ` | one clause, n=9 need 6 (`commas` is a word, not a comma) | 9/6 | pass |

The plan's sentence "S901/S903 carry no split boundary" is false for S901 (`plans/round-63.md:67`). The second clause is under `MIN_CONTENT`, so the pass still holds. The plan's "line 5" for S902 is the fixture's line 4 (`:2380`); the bytes are still the action sentence, so support does not change.

2. **A2 self-test cells near `check_scoped_rules_v31.py:2001-2030` (v32 copies at `:2071-2100`) do not take a G9 false reject.**

| cell | separators | clauses | verdict |
|---|---|---|---|
| `Scope rules to specific files using matching patterns. (S900 :1)` | none | 1 clause, 7/7 on the line | G9 pass; `action_conjunct` stays `[]` |
| `Scope the quantum lattice by frobnicating it. (S900 :1)` | none | 1 clause, 4/4 on its own line; page misses `frobnicating, lattice, quantum` | G9 does not fire (page fraction fails). Existing A2 page reject stands |
| invented `Create the rule file … and add frontmatter …` | `and` | c1 {create, file, project, rule} line 2/3 page 2/3; c2 {files, frontmatter, loads, matching} line 3/3 | G9 does not fire. Whole cell is already 5/8 need 6, so `action_conjunct` returns the A2 forward reason before G9 |
| G7 ``… and loads matching rule files `InstructionsLoaded`.`` | `and` | c1 n=6 line 6/4; c2 {loads, matching, rule, files} n=4 line 4/3 (identifier stripped by backticks) | G9 pass. G7 still the only reason. Same cell as `e2f-backticked-event-claim` (`check_erratum_absorption.py:215-220`), so disabling G7 still admits it |

3. **The frozen G9 attack is a true positive, not a false one.** Cell `The configuration stores project rules using glob syntax and secretly uploads files.` against line `…glob syntax.` and a page that adds `secretly uploads files` (`check_erratum_absorption.py:221-227`). Whole cell 7/10 need 7 (A2 forward passes, which is why v31 accepts it). Clause 2 {files, secretly, uploads} n=3 need 2, line 0, page 3. G9 rejects. W6's invented action (`v31.py:2496-2500`) would also G9-reject its first clause if called (page covers 3/3 via `projects`~`project`), but whole-cell forward is 5/8 need 6, so the world stays an A2 reject either way.

4. **Real measured action cells are the SKILL.md rows, not the knowledge entry.** `corpus/knowledge/scoped-rules-round60.md` has no Action column (quote table at `:13-18`). `action_conjunct` is called on the SKILL action cell (`check_scoped_rules_v32.py:1530-1534`). Citation is the first `S### :L` only (`:878-884`); `S107 :31-33` is line 31. v31 `action_conjunct` today: Claude, VS Code, Copilot, Cursor return `[]`; Codex, Gemini, opencode already return an A2 forward failure. G9 is reached only on the four passes.

| SKILL action | cited line | split | line-supported? | G9 fires? |
|---|---|---|---|---|
| Claude `;` (`SKILL.md:141`, S103:194) | line is the paraphrase that contains both clauses (`S103.page:194`) | c1 7/5, c2 4/3 | yes, yes | no |
| VS Code `and` (`SKILL.md:143`, S105:329) | line contains both halves, including `apply them selectively` | c1 4/3; c2 {apply, selectively} n=2 | yes; skip | no |
| Copilot `;` (`SKILL.md:144`, S106:60) | `S106.page:60` | c1 5/6 need 4, miss `path` only (`specific`~`specify`); c2 7/5 | yes, yes | no |
| Cursor (`SKILL.md:146`, S108:131) | line equals the cell (`S108.page:131`) | no `;`, no `and`, no `, ` | 9/6 | no |
| Codex `, ` (`SKILL.md:142`, S104:12) | not split (comma is not a boundary) | one clause, line 2/9 need 6 | n/a | not reached; v31 already `supports 2 of its 9 … need >= 6` |
| Gemini `;` and `and` (`SKILL.md:145`, S107:31) | line 31 is `When a tool accesses a file or directory, the CLI` | c1 line 1/4 page 6; c2 line 2/3 page 4; c3 {ancestors} skip | no, no, skip | not reached; v31 already `3 of its 11 … need >= 8`. Direct G9 would reject c1 and c2; that is the same reject, not a new one |
| opencode `;` and `and` (`SKILL.md:147`, S109:64) | `S109.page:64` has `sub-directories`, not `subdirectories` | c1 3/4 need 3 (miss `agents`); c2 {applies, directory, guidance} 2/3 need 2; c3 {subdirectories} skip | yes, yes, skip | not reached; v31 already `5 of its 8 … need >= 6` because `subdirectories` is off the line and off the page. G9 itself would not add a reject |

5. **Comma and the `&#124;` semicolon do not create a false positive on any cell this counter scores.** Planned split ignores `, `. The only action cell with `, ` outside backticks is Codex, already an A2 failure; splitting it on the comma still does not reach G9. Cursor's `with commas` has no comma character. Knowledge quotes are not `action_conjunct` inputs. Scored anyway against the lines named in `scoped-rules-round60.md:35-38`: S103:168 (comma, one clause, 8/6), S105:32 (no separator, 4/3), S108:32 (`and`, c1 4/3, c2 {version, controlled} skipped), S106:18. S106's quote contains `;` inside `&#124;`, which the planned splitter does cut: the left fragment has no content word (skip) and the right clause is 6/4 on line 18. Not a reject, and not an action cell.

6. **Cells at risk of a false positive: none.** A false positive here means G9 rejects a cell that whole-cell A2 already accepts. That set is the four eligible fixtures, the A2-pass cell, the G7 cell, and the four live passes (Claude, VS Code, Copilot, Cursor). Every clause in that set is line-ok or under 3 content words. Tightest pass is Copilot clause 1: 5 of 6, need 4, sole miss `path`. Dropping the `specific`~`specify` prefix still leaves 4/4. It would reject only if two further clause words left the line. Joining S107 lines 31-35 (the counter does not) makes Gemini's whole cell 9/11 need 8 and both clauses line-ok, so a range-join would also not G9-reject.

## Artifacts

Clause table above is the hand application. Reproduction is `content_words` / `fwd_need` / `covered` / `page_words` from `verifiers/check_scoped_rules_v31.py` plus split-on-`;`-and-`\band\b`-outside-backticks. Control result for the frozen attack: clause `secretly uploads files.` → line 0/2, page 3/2 → G9 reject, while whole-cell forward stays 7/10.

## Verdict

INFORMS. Planned `g9_conjunct` does not over-reject any action cell the v32 self-test accepts, and it does not newly reject any SKILL action row that v31 currently accepts. The G9 fixture is a real reject (second clause 0/2 on the cited line, 3/2 on the page). The plan's "S901 has no split boundary" is wrong and harmless: the `and`-clause has two content words and is skipped.

Would change this if a passing cell gained a ≥3-word clause whose cited-line coverage fell below `fwd_need` while the page still met it (Copilot clause 1 is the nearest, and it is still 5≥4), or if the splitter also cut on `, ` or on `;` inside `&#124;` and that fragment had ≥3 content words — neither happens on a cell this counter scores.
