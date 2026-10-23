Result: BREAKS — half the hypothesis holds (all four real scope-key lines pass A1) and half is falsified: nine other (K, line) pairs on the four eligible pages also pass `key_site`, and the frozen counter backs a row end-to-end (exit 0, 4 of 4 live) with one of them as the Scope key.

Seat `KotobaR60.ExecKeyForms` (leaf). I wrote no lane file except this report (the lane's
in-flight C1 files — `corpus/SOURCES.md`, `corpus/README.md`,
`corpus/knowledge/scoped-rules-round60.md`, `corpus/lessons/round-60.md`, the snapshots — are
siblings' work; I only read them). No tool installed (nothing missing; pacman untouched).
Probe scripts and outputs: `/fast/scratch/hyaku/kotoba-r60/ExecKeyForms/probe/`.

## What was run

Read-only import of a COPY of `verifiers/check_scoped_rules.py`
(`/fast/scratch/hyaku/kotoba-r60/ExecKeyForms/probe/counter_copy.py`):

```
$ sha256sum /fast/scratch/hyaku/kotoba-shokunin/verifiers/check_scoped_rules.py   # lane
ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a
$ sha256sum /fast/scratch/hyaku/kotoba-r60/ExecKeyForms/probe/counter_copy.py      # the copy imported
ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a
$ python3 -B counter_copy.py --self-test
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a
self-test: 0 failure(s) over 318 assertions        (exit 0)
```

Matching the brief's freeze sha `ca2585a4…`. `TARGET` read from the committed file:
`grep -n "^TARGET" verifiers/check_scoped_rules.py` → `249:TARGET = 3`.

The four eligible pages are the census fetch bytes (sha256 and size measured here with
`sha256sum` / `wc -c`; `date -u` → `Fri 23 Oct 2026 12:16:14 PM UTC`):

| Client | census page | bytes | sha256 |
|---|---|---|---|
| Claude Code | `CensusClaudeCode/memory.md` | 54043 | `82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7` |
| VS Code | `CensusVSCode/agent-custom-instructions.md` | 23715 | `a45c9e9f50c62949ea60711c6d657d065752c573a0c945215f32063fa56caa1f` |
| Copilot CLI | `CensusCopilotCLI/cli-md.body` | 8730 | `00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980` |
| Cursor | `CensusCursor/rules.md` | 17403 | `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8` |

Sweep method: for every line of each page, every token matching
`[A-Za-z0-9_][A-Za-z0-9_-]*` was tested with the counter's own
`key_site(lines, L, token)` — a superset of "every `<word>:` line", because `key_site`
itself requires the key at an IDENT boundary followed by `K:` / `K=` (after an optional
closing quote/backtick). `any_key_site(page, K)` was run for every key that stood in key
form anywhere on the page. Script: `probe/probe_broad.py`; raw output `probe/broad.out`,
`probe/allpages.out`.

## Part 1 — the hypothesis, measured

Hypothesis under test: *every real scope-key line on the four eligible pages passes A1 and
no other key line on those pages does.*

### 1a. First clause — CONFIRMED (4 of 4), plus the real key's other genuine sites

```
$ sed -n '198p' CensusClaudeCode/memory.md          ->  paths:
$ sed -n '231p' CensusClaudeCode/memory.md          ->  paths:
$ sed -n '164p' CensusVSCode/agent-custom-instructions.md ->  applyTo: '**/*.py'
$ sed -n '66p'  CensusCopilotCLI/cli-md.body        ->     applyTo: "app/models/**/*.rb"
$ sed -n '74p'  CensusCopilotCLI/cli-md.body        ->     applyTo: "**/*.ts,**/*.tsx"
$ sed -n '94p'  CensusCopilotCLI/cli-md.body        ->     applyTo: "**"
$ sed -n '85p'  CensusCursor/rules.md               ->  globs: src/components/**/*.tsx
```

`key_site` = True and `scope_conjunct` = `[]` for all four census pairs
(`paths`:198, `applyTo`:164, `applyTo`:66, `globs`:85), and `any_key_site` = True for all
four keys on their page. The census lines and keys are correct.

### 1b. Second clause — FALSIFIED. Every (K, line) that passes, per page

Claude Code — 4 passing pairs, 2 of them on a key that is not the scope key:

```
K='paths'            L=198   REAL
K='paths'            L=231   REAL (same key, second example)
K='patterns'         L=238   extra
K='claudeMdExcludes' L=339   extra
```

```
$ sed -n '238p' CensusClaudeCode/memory.md
Each brace group multiplies the number of expanded patterns: `src/*.{ts,tsx}` expands to two patterns, and `{a,b}/{c,d}/*.{ts,tsx}` to eight. To keep expansion bounded, a rule's whole `paths` list shares one budget of 1,000 expanded patterns and 4 MiB, and patterns without braces don't count against it.

$ sed -n '339p' CensusClaudeCode/memory.md
  "claudeMdExcludes": [

$ sed -n '340p' CensusClaudeCode/memory.md
    "**/monorepo/CLAUDE.md",
```

VS Code — 6 passing pairs, 1 on the scope key:

```
K='sessions'  L=32    extra      K='sessions'  L=128   extra
K='sessions'  L=221   extra      K='sessions'  L=228   extra
K='Sync'      L=287   extra      K='applyTo'   L=164   REAL
```

```
$ sed -n '32p' CensusVSCode/agent-custom-instructions.md
> **For Local harness sessions:** Project instructions can use `.github/copilot-instructions.md`, `AGENTS.md`, or `CLAUDE.md`. Targeted instructions can use `.github/instructions/**/*.instructions.md` or Markdown files in `.claude/rules`. The Local harness-specific settings in the sections below control discovery.

$ sed -n '287p' CensusVSCode/agent-custom-instructions.md
To sync profile instructions, enable Settings Sync and run **Settings Sync: Configure** from the Command Palette (`kb(workbench.action.showCommands)`). Select **Prompts and Instructions** from the list of settings to sync.
```

Copilot CLI — 3 passing pairs, all on the scope key; **no extra key passes** (the only clean page):

```
K='applyTo' L=66 REAL      K='applyTo' L=74 REAL      K='applyTo' L=94 REAL
```

Cursor — 3 passing pairs, 1 on the scope key:

```
K='globs' L=85 REAL      K='rules' L=146 extra      K='order' L=307 extra
```

```
$ sed -n '146p' CensusCursor/rules.md
There are two ways to create rules:

$ sed -n '148p' CensusCursor/rules.md
- **`/create-rule` in chat**: Type `/create-rule` in Agent and describe what you want. Agent generates the rule file with proper frontmatter and saves it to `.cursor/rules`.

$ sed -n '307p' CensusCursor/rules.md
- **Precedence**: Rules are applied in this order: **Team Rules → Project Rules → User Rules**. All applicable rules are merged; earlier sources take precedence when guidance conflicts.
```

Totals: **3 of the 4 eligible pages carry at least one non-scope key line that passes A1**;
16 passing (K, L) pairs in all, of which **9 name a key that is not the client's scope key**
(Claude Code 2, VS Code 5, Cursor 2). The clause "no other key line on those pages does" is
false.

### 1c. The mechanism: `**` (markdown bold) reads as a path pattern

A1 asks only that the first value token contain `*` and match
`^[A-Za-z0-9_./*{},!-]+$` (`pattern_value`), and `first_value_token` strips leading
`- [ " ' \`` and space but **not** `*`. Probed value reads (`probe/probe_bold.py`):

```
Claude Code  K='patterns' L=238   first_value_token='src/*.{ts'   pattern_value=True
VS Code      K='sessions' L=32    first_value_token='**'          pattern_value=True
VS Code      K='Sync'     L=287   first_value_token='Configure**' pattern_value=True
Cursor       K='rules'    L=146   first_value_token='**'          pattern_value=True
Cursor       K='order'    L=307   first_value_token='**Team'      pattern_value=True
```

Two families, both prose, neither a scoping key: (i) a bold marker `**` immediately after a
colon — `sessions:**`, `order: **Team`, and, through the block-value rule, `rules:` whose
next list item starts `- **`; (ii) an inline-code glob after a prose colon (`patterns:
`src/*.{ts,tsx}``). The prose colon is not distinguished from a configuration colon.

## Part 2 — three INVENTED Action cells per page

Three plausible generic rule-author-advice cells per eligible page, each cited at the line
of that page that shares the most content words with it (`cs.content_words` intersection),
then scored with the counter's `action_conjunct`. Word counts below are the counter's own
`|W|` (distinct content words) and `need` (`action_need`), printed by `probe/probe_final.py`;
the raw `wc -w` count of each cell is in the appendix.

| Client | invented cell | \|W\| | need | best line | shared | `action_conjunct` | counter row |
|---|---|---|---|---|---|---|---|
| Claude Code | Create the rule file in the project and add frontmatter so it loads only for the matching files. | 8 | 4 | 209 | 6 | **PASSES** | backed |
| Claude Code | Keep one instruction file per topic and set the scope key to the glob pattern of the files it applies to. | 9 | 5 | 66 | 4 | fails | rejected |
| Claude Code | Give the agent the right project context by scoping the rule to the file patterns you name. | 10 | 5 | 242 | 4 | fails | rejected |
| VS Code | Put the guidance in an instructions file and add frontmatter so it attaches only to the files you name. | 7 | 4 | 105 | 4 | **PASSES** | backed |
| VS Code | Use one instruction file per topic and set the scope key to the glob pattern of the matching files. | 8 | 4 | 156 | 4 | **PASSES** | backed |
| VS Code | Scope the instruction to the file patterns you want so the agent gets the right project context. | 10 | 5 | 9 | 3 | fails | rejected |
| Copilot CLI | Create the instruction file in the repository and add frontmatter so it applies only to matching files. | 8 | 4 | 11 | 6 | **PASSES** | backed |
| Copilot CLI | Keep one instruction file per topic and set the scope key to the glob pattern of the files it applies to. | 9 | 5 | 11 | 4 | fails | rejected |
| Copilot CLI | Scope the instruction to the file patterns you name so the agent gets the right project context. | 10 | 5 | 11 | 3 | fails | rejected |
| Cursor | Create the rule file in the project and add frontmatter so it attaches only to the matching files. | 8 | 4 | 42 | 4 | **PASSES** | backed |
| Cursor | Use one rule file per topic and set the scope key to the glob pattern of the files it applies to. | 8 | 4 | 305 | 6 | **PASSES** | backed |
| Cursor | Scope the rule to the file patterns you name so the agent gets the right project context. | 10 | 5 | 42 | 4 | fails | rejected |

**6 of 12 invented cells pass `action_conjunct`, and the counter backs all 6.** The cells are
not built from the cited line's words; they pass because the page is dense in the domain
vocabulary (`rule`, `file`, `files`, `pattern`, `patterns`, `glob`, `matching`, `attaches`,
`applies`, `frontmatter`, `project`), and the author picks the cited line.

The lines that accept them are visibly about something else — e.g. the Claude Code cell
"add frontmatter so it loads only for the matching files" is accepted at line 209, whose own
text is the *unconditional-load* rule:

```
$ sed -n '209p' CensusClaudeCode/memory.md
Rules without a `paths` field are loaded unconditionally and apply to all files. A path-scoped rule loads when Claude uses the Read, Write, or Edit tool on a matching file. It also loads when Claude views a matching file with a Bash command that [counts as a read](/docs/en/tools-reference.md#edit-tool-behavior), such as `cat` or `head` on a single file. Matching also works when Claude reaches a file through a symlinked path to the project directory, for example in a symlinked checkout.
```

Under-determined citations, measured: the real action cell accepts 10 of 664 lines on the
Claude Code page, 1 of 367 on VS Code, 2 of 111 on Copilot CLI, 2 of 399 on Cursor. A minimal
3-content-word cell is weaker still: `need` = `max(2, ceil(3/2))` = 2, so "applies matching
files" is accepted by 11 of 664 Claude Code lines, "scope rule files" by 8, and the same
cells pass on VS Code and Cursor (raw output `probe/launder.out`).

## Part 3 — end-to-end: the counter CLI on real sandbox commits

A complete C1 world (SKILL.md section, entry file, SOURCES rows, lesson `## Gate`, committed
snapshots) was built in the sandbox clone and scored with the real CLI
(`probe/build_world.py`). Every hash below is a **sandbox** commit in
`/fast/scratch/hyaku/kotoba-r60/ExecKeyForms`, never the lane.

| World | change vs the census | counter output | exit |
|---|---|---|---|
| W-real | none — census tokens, keys, quotes | `backed on committed snapshots 3 of 4; live not run` | 1 |
| W-fix | Copilot CLI folder token + pipe-free quote | `backed on committed snapshots 4 of 4` | 1 |
| W-wrong | W-fix + VS Code Scope key `sessions` (S105 :32) | `backed on committed snapshots 4 of 4` | 1 |
| W-invented-best-line | W-fix + VS Code Action = invented cell cited :105 | `backed … 4 of 4` | 1 |
| W-invented-real-line | same cell cited at the real action line :329 | `backed … 3 of 4`, reject VS Code: `action cell shares 2 of its 7 content word(s) with line 329 (need >= 4)` | 1 |
| W-real with `--fetch` | none — census rows verbatim | `backed … 3 of 4; found on the live page 3 of 4`, reject Copilot CLI: `quote holds 1 words` | **0** |
| W-fix with `--fetch` | no change | `backed … 4 of 4; found on the live page 4 of 4` | **0** |
| W-wrong with `--fetch` | wrong key `sessions` | `backed … 4 of 4; found on the live page 4 of 4` | **0** |

Sandbox commits: W-real `c3fa21c7fda83c841ca0031666c0ec34c3794241`; W-fix `f4490259b4601af4126f2c99f0cf58fe2909cf4c`;
W-wrong `43fe1e1664f50b67982fb28a7fa9094854e76b26`; W-invented-best-line
`7fb6b20227243307484a698221ba0164c7707b64`; W-invented-real-line
`0348da0be85473343ed0d759fabae99c8bf382c5`; `--fetch` runs
`e5e6c7b0faee13bae824a794225e2c2cf94019f1` (the census rows verbatim, 3 of 4),
`d8a6774c30982de9b2d92a3e75f982e19f3b55f3` (real keys, 4 of 4) and
`c8791c71ee732cc404f4cf1f1e68985921eebbd6` (wrong key `sessions`, still 4 of 4).

The live path is genuinely exercised — a negative control with a 404 URL prints
`reject VS Code: live fetch failed: HTTP 404 at https://code.visualstudio.com/docs/agent-customization/no-such-page-xyz.md`
(sandbox `828535951de212b415214dcb82322161f04a40f9`, `found 3 of 4`). So **the predicate
sentence is met with a wrong scope key**, which is exactly what the cancelled `CtlWrongKey`
control was to detect.

Which wrong keys are caught, and which are not (`probe/probe_wrongkeys.py`):

- **Caught** — every key the W0 census named: Claude Code `description`@248, VS Code
  `description`@155 and @163, VS Code `name`@154, Copilot CLI `excludeAgent`@95, Cursor
  `description`@179 and @99, Cursor `alwaysApply`@74. Each returns
  `scope key '<K>' is not in key form with a path pattern at line L`. The plan's statement
  "wrong keys the census found … each failing A1" is correct.
- **Not caught** — 8 of the 9 probe-found extras are backed end-to-end: Claude Code
  `patterns`@238, `claudeMdExcludes`@339; VS Code `sessions`@32/128/221/228, `Sync`@287;
  Cursor `order`@307. Only Cursor `rules`@146 is rejected, and by the **v2 re-open conjunct**
  (`base row S049 already records key rules`), not by A1.

The counter's scope conjunct is therefore a *form* test, not a semantic one: it never checks
that K names the matching-paths key. A1 narrows the field (it removes the table-cell form and
the glob/pattern-word alternative the census demonstrated under the draft) but does not pin
the key.

## Risks the L1 must weigh (all measured, none hypothetical)

1. **Copilot CLI's census quote carries a literal `|`, which truncates the entry row's Quote
   cell — the plan's quote as written cannot be backed.** The census token is
   `.github/instructions/**/*.instructions.md` and the census quote is the line-18 slice,
   which contains a literal `|` (the markdown cell separator). The counter's `cells()` splits
   a table row on `|`, so the entry row's Quote cell truncates to the token alone — the
   counter then reads a 1-word quote:
   ```
   cells('| Copilot CLI | .github/… | S106 | `tok` | Modular repository instructions, … |')
     -> er[3] = '`.github/instructions/**/*.instructions.md`'   (1 word)
   ```
   Dropping the pipe makes the quote no longer be on the page (`the quote is not on the
   page`), and `\|` fails the same way. An exhaustive search of the page finds **0**
   pipe-free quotes holding that token (the token occurs on line 18 only, which is the table
   row). Consequence, measured: with the plan's Copilot row verbatim,
   `--rev … --fetch` prints `backed 3 of 4; found on the live page 3 of 4` and exits **0**
   (sandbox `e5e6c7b0faee13bae824a794225e2c2cf94019f1`) — the predicate survives at
   `3 ≥ TARGET 3`, but the Copilot CLI row the table claims is a **rejected** row, not a
   backed one.
   Two working alternatives, both measured. (a) The HTML entity `&#124;` in place of the
   literal pipe —
   `` `…instructions.md`              &#124; Modular repository instructions, discovered in the standard locations `` —
   survives `cells()` as one 10-word cell and passes `quote_why`, because `page_plain` runs
   `html.unescape` on the quote side and `norm_page` unescapes the page side too:
   ```
   cells        : ['Copilot CLI', '…', 'S106', '`…instructions.md`   &#124; Modular … locations']
   er[3] words  : 10
   quote_why    : []
   gate check   : True
   ```
   (b) The folder token `.github/instructions` (`token_well_formed` True, no foreign marker)
   with the pipe-free quote `2. Optionally, create subdirectories of \`.github/instructions\` to organize your instruction files.`
   → backed, and `--fetch` then gives 4 of 4, exit 0.
   Read-only observation: the in-flight lane entry `corpus/knowledge/scoped-rules-round60.md`
   (a sibling's file, not mine) already writes the Copilot quote with `&#124;`, i.e. option (a).
2. **The wrong-key hole is reachable by a real author, not only by an adversary.** Cursor
   `rules` is the plausible one and is blocked only by the re-open conjunct; Claude Code
   `patterns` is plausible and is not blocked at all.
3. **The invented-action hole is wide.** 6 of 12 invented cells pass, because the conjunct is
   bag-of-words overlap against an author-chosen line. The plan already pre-registers the
   negation limit ("a cell built from the line's own words passes even if it inverts the
   line's meaning"); this finding is broader — the cell need not be built from the line at all.
   A control that invents an Action cell and keeps the *real* citation line is rejected (see
   W-invented-real-line); a control free to choose the line is not.
4. **Line-number drift.** All my line numbers are the census bytes above. The live pages are
   re-fetched at counter time; a page edit shifts them. The committed snapshot pins the
   snapshot side, so this affects only re-fetch hygiene.
5. **Section cost.** The generated section with four client rows added **9** lines to
   `SKILL.md` (587 → 596 in the sandbox world: `wc -l` before/after), not the ~14 the brief
   budgets for `ExecBudgetMove`. Useful for the budget seat.

## What was not measured

- No live fetch of the *census* pages for the key sweep (the sweep is on the census bytes,
  which are the bytes the snapshots pin). The `--fetch` runs above are the counter's own.
- The three non-eligible clients' pages were swept for completeness only (appendix); they are
  outside the hypothesis and their key sites do not affect C1.
- No mutation of the lane; no lane counter run; no `--fetch` against the lane revision (no
  C1 data is committed yet).

## Appendix — the sweep over every census page under `Census*/`

Eligible (the hypothesis's four): Claude Code 4 passing pairs (2 extra), VS Code 6 (5 extra),
Copilot CLI 3 (0 extra), Cursor 3 (2 extra).

Not eligible, swept for completeness (`probe/probe_allpages.py`):

| Page | lines | passing (K, L) pairs |
|---|---|---|
| `CensusCodex/agents-md.body` | 219 | 8 — `scope`@11, `scope`@12, `order`@13, `loads`@210, `appears`@211, `names`@212, `truncated`@213, `confusion`@214 |
| `CensusCodex/rules.body` | 139 | 0 |
| `CensusGeminiCLI/gemini-md.md.body` | 116 | 11 — `file`@18, `Location`@20, `Scope`@21, `files`@23, `Location`@25, `Scope`@27, `files`@30, `Location`@31, `Scope`@34, `imports`@77, `json`@100 |
| `Censusopencode/rules.md` | 183 | 1 — `fallbacks`@74 |
| `Censusopencode/v2-instructions-accept.md` | 128 | 0 |

The German-locale Claude Code page the W0b seat scored (`RecensusClaudeCode/de-memory.body`,
664 lines) behaves identically: `paths`@198, `paths`@231, `Muster`@238, `claudeMdExcludes`@339.

## Appendix — `wc -w` of every invented cell (M85)

```
$ bash /tmp/wc_cells.sh
18 <- Create the rule file in the project and add frontmatter so it loads only for the matching files.
21 <- Keep one instruction file per topic and set the scope key to the glob pattern of the files it applies to.
17 <- Give the agent the right project context by scoping the rule to the file patterns you name.
19 <- Put the guidance in an instructions file and add frontmatter so it attaches only to the files you name.
19 <- Use one instruction file per topic and set the scope key to the glob pattern of the matching files.
17 <- Scope the instruction to the file patterns you want so the agent gets the right project context.
17 <- Create the instruction file in the repository and add frontmatter so it applies only to matching files.
17 <- Scope the instruction to the file patterns you name so the agent gets the right project context.
18 <- Create the rule file in the project and add frontmatter so it attaches only to the matching files.
21 <- Use one rule file per topic and set the scope key to the glob pattern of the files it applies to.
17 <- Scope the rule to the file patterns you name so the agent gets the right project context.
3 <- scope rule files
3 <- applies matching files
3 <- glob pattern files
```

(The `wc -w` figures are whitespace counts; the `|W|` column in Part 2 is the counter's own
`content_words` count, which drops stopwords — that is why a 19-word cell can have `|W|`=7.)
