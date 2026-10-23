Result: DONE — Read-only reasoning identifies a real wrong-key false positive on Claude Code's page and unsupported Actions on every eligible page; no counter or runtime probe was run.

# Scope and axes

Assigned revision: `b1cd64bb45eee744c4ec93be8631f1eddb28fddd`. Axes: **depth** (does the table teach the actual scoping mechanism?) and **calibration** (does mechanical acceptance warrant semantic correctness?). Only this report was written. No lane code, snapshots, counter, rule, target, or routing was changed. No tools were installed or updated.

All acceptance predictions below are **[INFERENCE] from the frozen implementation**, not observed predicate results. No sandbox world, self-test, measurement, new fetch, model/client invocation, or canonical judgment was performed. Source files were inspected with `read` and `grep`; shell commands only inspected identities, byte lengths, and enumerated word-set lengths.

# Counter identity and source provenance

Observed command, exit 0:

```sh
timeout 20s git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show b1cd64bb45eee744c4ec93be8631f1eddb28fddd:verifiers/check_scoped_rules.py | sha256sum
```

```text
ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a  -
```

Observed command, exit 0:

```sh
timeout 20s sha256sum /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_scoped_rules.py /fast/scratch/hyaku/kotoba-r60/CensusClaudeCode/memory.md /fast/scratch/hyaku/kotoba-r60/CensusVSCode/agent-custom-instructions.md /fast/scratch/hyaku/kotoba-r60/CensusCopilotCLI/add-custom-instructions.md /fast/scratch/hyaku/kotoba-r60/CensusCursor/rules.md
```

```text
ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a  /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_scoped_rules.py
82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7  /fast/scratch/hyaku/kotoba-r60/CensusClaudeCode/memory.md
a45c9e9f50c62949ea60711c6d657d065752c573a0c945215f32063fa56caa1f  /fast/scratch/hyaku/kotoba-r60/CensusVSCode/agent-custom-instructions.md
00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980  /fast/scratch/hyaku/kotoba-r60/CensusCopilotCLI/add-custom-instructions.md
884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8  /fast/scratch/hyaku/kotoba-r60/CensusCursor/rules.md
```

Thus the implementation read in the lane has the assigned revision's counter bytes.

Observed command, exit 0:

```sh
timeout 20s wc -c /fast/scratch/hyaku/kotoba-r60/CensusClaudeCode/memory.md /fast/scratch/hyaku/kotoba-r60/CensusVSCode/agent-custom-instructions.md /fast/scratch/hyaku/kotoba-r60/CensusCopilotCLI/add-custom-instructions.md /fast/scratch/hyaku/kotoba-r60/CensusCursor/rules.md
```

```text
 54043 /fast/scratch/hyaku/kotoba-r60/CensusClaudeCode/memory.md
 23715 /fast/scratch/hyaku/kotoba-r60/CensusVSCode/agent-custom-instructions.md
  8730 /fast/scratch/hyaku/kotoba-r60/CensusCopilotCLI/add-custom-instructions.md
 17403 /fast/scratch/hyaku/kotoba-r60/CensusCursor/rules.md
103891 total
```

Original acquisition facts below are inherited from the W0 receipts, **not a fresh network observation by this seat**. Hashes and byte lengths were independently observed above.

| Client | Original URL | Original `date -u` stdout | HTTP | Receipt |
|---|---|---|---|---|
| Claude Code | https://code.claude.com/docs/en/memory.md | `Fri 23 Oct 2026 10:29:06 AM UTC` | 200 | `.ufo/waves/round-60/w0/CensusClaudeCode.md:7-11`; saved `CensusClaudeCode/date-start.txt:1` |
| VS Code | https://code.visualstudio.com/docs/agent-customization/custom-instructions.md | `Fri 23 Oct 2026 10:29:10 AM UTC` | 200 | `.ufo/waves/round-60/w0/CensusVSCode.md:13-15` |
| Copilot CLI | https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md | `Fri 23 Oct 2026 10:29:28 AM UTC` | 200 | `.ufo/waves/round-60/w0/CensusCopilotCLI.md:7-12`; saved `CensusCopilotCLI/date-fetch1.txt:1` |
| Cursor | https://cursor.com/docs/rules | `Fri 23 Oct 2026 10:29:16 AM UTC` | 200 | `.ufo/waves/round-60/w0/CensusCursor.md:7-12`; saved `CensusCursor/date-u.txt:1`; markdown Accept header |

In the evidence below, `Census.../file` abbreviates `/fast/scratch/hyaku/kotoba-r60/Census.../file`. The printed `sed -n` commands are **reproduction selectors, not commands executed by this seat**; their lines were observed through ranged `read`. Excerpts are exact contiguous spans; no internal Markdown bytes were removed.

# K1 — a genuine exclusion setting passes as the Scope key

Candidate Scope key cell:

```text
`claudeMdExcludes` (S103 :339)
```

Saved bytes, `CensusClaudeCode/memory.md:339-341`:

```sh
sed -n '339,341p' /fast/scratch/hyaku/kotoba-r60/CensusClaudeCode/memory.md
```

```text
  "claudeMdExcludes": [
    "**/monorepo/CLAUDE.md",
    "/home/user/monorepo/other-team/.claude/rules/**"
```

Why this is WRONG, not merely another spelling of the scoping key:

- `memory.md:333`, exact sentence inside that line: `The `claudeMdExcludes` setting lets you skip specific files by path or glob pattern.`
- `memory.md:335`, exact first sentence: `This example excludes a top-level CLAUDE.md and a rules directory from a parent folder.` The following sentence locates the setting in `.claude/settings.local.json`, not rule frontmatter.
- `memory.md:246`, exact sentence inside that line: `` `paths` is the only field Claude Code reads from a rule; any other field is ignored without an error. ``

Reproduction selectors for those observations:

```sh
sed -n '333p' /fast/scratch/hyaku/kotoba-r60/CensusClaudeCode/memory.md
sed -n '335p' /fast/scratch/hyaku/kotoba-r60/CensusClaudeCode/memory.md
sed -n '246p' /fast/scratch/hyaku/kotoba-r60/CensusClaudeCode/memory.md
```

These prose excerpts are contiguous sentence selections from the observed lines, not summaries presented as quotations.

**[INFERENCE] A1 Scope-key acceptance:**

1. `claudeMdExcludes` satisfies `KEY_IDENT_RE` (`verifiers/check_scoped_rules.py:305`).
2. On line 339 it has identifier boundaries; its closing quote and colon satisfy `KEY_SUFFIX_RE` (`:306`, `:793-811`, `:862-866`).
3. The remainder is ` [`; `block_only` accepts it (`:307`, `:833-835`).
4. The first following nonblank line, 340, begins with a quote. `value_after` accepts it without checking JSON versus YAML, a frontmatter fence, or the setting's purpose (`:838-850`).
5. `first_value_token` strips the opening quote/spaces and obtains `**/monorepo/CLAUDE.md`; it contains `*` and only allowed characters (`:308-309`, `:814-830`). Therefore `key_site(..., 339, "claudeMdExcludes")` returns true (`:853-869`).

No relation is required between that setting and the rule-file token/quote. A legitimate `.claude/rules/` quote elsewhere on the same genuine page can remain unchanged. An otherwise ordinary Action such as `Use scoped rules for files (S103 :194)` also remains acceptable (word-set receipt A below). Thus separate individually accepted cells need not describe the same mechanism.

**Live boundary:** `any_key_site` scans every page line (`:872-878`); `live_why` checks only the quote plus such a site (`:964-969`). If the live page retains these census bytes, the wrong key also passes that live key-site check. This does **not** claim an executed whole-row/re-open/live/predicate result: all other backing conjuncts and current live availability remain prerequisites.

**Impact:** depth loses the intended conditional-loading fact and may teach the inverse operation; calibration loses the claim that a printed-but-wrong key necessarily fails. This is a semantic sufficiency defect in the heuristic, not evidence that the implementation diverges from A1's literal key-form rule.

## Other eligible pages: attempted wrong keys

The same saved-byte scan found no additional wrong key passing A1 on these pages. This is bounded to the examined census Markdown, not a claim about all vendor documentation or later live bytes.

| Client | Observed competing key sites | Why these do not provide a false positive |
|---|---|---|
| VS Code | `agent-custom-instructions.md:162-164`: `name: 'Python testing'`, `description: 'Use when creating or updating Python unit tests.'`, `applyTo: '**/*.py'` | Wrong keys start with `Python` or `Use`, not a token containing `*`; `applyTo` is the genuine key. |
| Copilot CLI | `add-custom-instructions.md:94-95`: `applyTo: "**"`, `excludeAgent: "code-review"` | `excludeAgent` has no `*`; `applyTo` is genuine. |
| Cursor | `rules.md:74,85-86,99-100,114,179-180,254-255`: `alwaysApply` takes booleans; `description` starts `RPC`, `This`, or `Your`; `label` starts `Your` | None of those wrong keys has the required first value token. The table at :65 is not key form. `globs` at :85 is genuine. |

These are key/value snippets from their indicated lines, not shaped full-line quotations. Claude Code's `claudeMdExcludes` is the stronger local counterexample than reusing the named `description`/`alwaysApply` traps.

# A1 — meaning-inverted Actions pass on every eligible page

Implementation: `content_words` removes backticks/citations, lowercases, and returns a **set** (`verifiers/check_scoped_rules.py:881-886`). `never`, `only`, `without`, `when`, `their`, and `even` are stopwords (`:330-342`); `not` is below `CONTENT_RE`'s minimum length (`:315`). The acceptance test is only set-intersection size (`:889-912`). It contains no direction, negation, condition, word-order, or operational-context test.

## Source lines and exact excerpts

- **Claude Code**, `CensusClaudeCode/memory.md:194`, exact first sentence: `Rules can be scoped to specific files using YAML frontmatter with the `paths` field.`
- **VS Code**, `CensusVSCode/agent-custom-instructions.md:329`, exact contiguous suffix beginning at `use`: `use multiple `*.instructions.md` files per topic and apply them selectively by using the `applyTo` property.`
- **Copilot CLI**, `CensusCopilotCLI/add-custom-instructions.md:32`, exact first sentence: `Path-specific instructions are included only when their `applyTo` value matches a file that Copilot CLI is working with.`
- **Cursor**, `CensusCursor/rules.md:131`, complete line: `Use `globs` to scope a rule to specific files or directories. Separate multiple patterns with commas.`

Reproduction selectors:

```sh
sed -n '194p' /fast/scratch/hyaku/kotoba-r60/CensusClaudeCode/memory.md
sed -n '329p' /fast/scratch/hyaku/kotoba-r60/CensusVSCode/agent-custom-instructions.md
sed -n '32p' /fast/scratch/hyaku/kotoba-r60/CensusCopilotCLI/add-custom-instructions.md
sed -n '131p' /fast/scratch/hyaku/kotoba-r60/CensusCursor/rules.md
```

No backticks, punctuation, or internal words were stripped from these excerpt spans.

## Candidate Action cells

These are **invented counterexamples, not vendor quotations or proposed content**:

| Client | False Action cell | Why its meaning is unsupported |
|---|---|---|
| Claude Code | `Never use scoped rules for files (S103 :194)` | Prohibits the scoped-rule use the line describes. |
| VS Code | `Never apply instructions selectively (S105 :329)` | Reverses the line's explicit authoring advice. |
| Copilot CLI | `Include path-specific instructions even when their `applyTo` value never matches a file (S106 :32)` | Reverses the inclusion condition: the source requires a matching file. |
| Cursor | `Never scope a rule to specific files or directories (S108 :131)` | Prohibits the operation the line explicitly recommends. |

The source IDs are the assignment's IDs; line numbers refer to census bytes. They are not a claim that these cells were integrated or that later fetched snapshots have unchanged numbering.

### Word-set receipts

Sets below were derived manually using the frozen regex and stopword list. The commands count the displayed distinct-token enumerations, **not an executed `content_words` or counter result**. Every listed command returned exit 0 with the shown stdout.

**A — Claude Code:** W and the shared set are both `{scoped, rules, files}`.

```sh
timeout 10s printf '%s\n' 'scoped rules files' | timeout 10s wc -w
```

```text
3
```

Thus both cardinalities are the command's output above; threshold `max(2, ceil(3/2)) = 2`. **[INFERENCE] passes**. Removing `Never` leaves exactly the same retained set. The positive Action used to isolate K1 has this same retained set.

**B — VS Code:** W and the shared set are both `{apply, instructions, selectively}`.

```sh
timeout 10s printf '%s\n' 'apply instructions selectively' | timeout 10s wc -w
```

```text
3
```

Thus both cardinalities are the command's output above; threshold `max(2, ceil(3/2)) = 2`. **[INFERENCE] passes**.

**C — Copilot CLI:** W is `{include, path, specific, instructions, value, matches, file}`. Hyphenated `path-specific` splits into the separate runs `path` and `specific`; the backticked key is removed.

```sh
timeout 10s printf '%s\n' 'include path specific instructions value matches file' | timeout 10s wc -w
```

```text
7
```

The shared set is `{path, specific, instructions, value, matches, file}`. `include` is not `included`; no stemming is assumed.

```sh
timeout 10s printf '%s\n' 'path specific instructions value matches file' | timeout 10s wc -w
```

```text
6
```

Using those observed enumeration lengths, threshold `max(2, ceil(7/2)) = 4`; the shared enumeration exceeds it. **[INFERENCE] passes**, despite negating the matching condition.

**D — Cursor:** W and the shared set are both `{scope, rule, specific, files, directories}`.

```sh
timeout 10s printf '%s\n' 'scope rule specific files directories' | timeout 10s wc -w
```

```text
5
```

Thus both cardinalities are the command's output above; threshold `max(2, ceil(5/2)) = 3`. **[INFERENCE] passes**.

## A2 — an unrelated operation passes without negation

Invented Action cell for the VS Code row:

```text
Publish multiple files globally (S105 :329)
```

The cited line discusses applying scoped instructions, not publication. W is `{publish, multiple, files, globally}`; only `{multiple, files}` is shared. Neither `publish` nor `globally` appears on that line. This exploits the permitted unsupported half, not just discarded negation.

Observed enumeration commands, both exit 0:

```sh
timeout 10s printf '%s\n' 'publish multiple files globally' | timeout 10s wc -w
```

```text
4
```

```sh
timeout 10s printf '%s\n' 'multiple files' | timeout 10s wc -w
```

```text
2
```

Using those enumeration lengths, threshold `max(2, ceil(4/2)) = 2`; the shared set exactly meets it. **[INFERENCE] passes**. Raising sensitivity to the word `never` alone would not address this case.

**Effect on the counter:** conditional on an otherwise backed real-source row, each Action above passes its Action conjunct. The live check does not inspect the Action at all (`verifiers/check_scoped_rules.py:964-969`, `:2537-2547`), so a normal live reread of the same genuine quote/key does not repair the semantic error. In particular, rows with correct keys but inverted Actions can still contribute to F. This is a static counterexample to semantic sufficiency, not an observed whole-predicate control receipt.

# Would falsify Cells seats catch these?

`plans/round-60.md:61-64` explicitly records the negation limitation and assigns that reading to `Cells<Client>`. **[INFERENCE] A genuinely independent semantic re-read should catch every example above**, because the contradictions are explicit in the cited source/context:

| Relevant semantic review | Required discriminating read | Expected result, not an observed receipt |
|---|---|---|
| Claude Code Cells | Compare the nominated key's :339 JSON setting with :335 settings-file placement and :246 rule-frontmatter authority; then compare its Action with :194. | Reject the exclusion key and the prohibition. Merely checking :339 for a glob misses K1. |
| VS Code Cells | Read :329 as a recommendation to apply instructions selectively. | Reject both the prohibition and unrelated global-publication advice. |
| Copilot CLI Cells | Preserve the `only when` matching condition at :32. | Reject the never-matching inclusion advice. |
| Cursor Cells | Read the imperative `Use` and the scoping operation at :131. | Reject the prohibition. |

Re-running `key_site` or the overlap arithmetic is **not** that semantic read and would miss the corresponding cases. This distinction matters: source genuineness and a matching snapshot hash do not establish that the cell faithfully represents it.

No Cells receipt was available in the examined `falsify/` directory (the directory read returned empty). Moreover, `.ufo/waves/round-60/controls/SUMMARY.md:14-22` records the cancelled `CtlWrongKey`/`CtlInventedAction` seats and expressly discloses the absent pre-data semantic-control receipts. Therefore this report cannot state that those cases have already been caught by the review pipeline.

# Smallest safe correction and calibration boundary

1. **Artifact correction, not counter redesign:** retain Claude Code's genuine `paths` key at census :198 with its :199 glob, not `claudeMdExcludes`. Retain source-faithful positive Actions: scoped rules for matching files; selective instruction application; inclusion only on matching paths; `globs`-based scoping. Re-read line numbers against each final committed snapshot before citing them.
2. **Independent semantic evidence:** have the already-planned Cells review establish that each nominated key is a rule-frontmatter matching-path key for the named rule files, and preserve each Action's operation and condition. The K1 discrimination requires the surrounding settings/frontmatter context, not only the pattern-bearing line. This is the smallest correction to an affected row and its evidence; it does not require another authority or runtime.
3. **Keep the frozen measurement intact:** do not change the counter, STOPWORDS, rule, target, or census to make these disappear. The negation tradeoff was predeclared (`plans/round-60.md:61-64`); the unrelated-operation case and the exclusion-setting case expose the same lack of semantic entailment in different ways. Literal implementation conformance is not semantic validation. Describe the counter as checking cited key/value shape plus lexical support, with semantic validity resting on independent source reading.
4. **No admission conclusion:** a malformed or inverted cell is a fixable content defect if corrected and independently reread. If the claim instead relies only on mechanical acceptance as proof of correct scoping meaning, that unsupported inference is for the canonical Rust judge to reject; this seat neither judges the claim nor supplies a passing receipt.

Report: .ufo/waves/round-60/build/CriticKeyRule.md
