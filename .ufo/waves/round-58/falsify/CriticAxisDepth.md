Result: MIXED — the landed table contains actionable technical depth beyond locations, but two cells are weak and Cursor's audit exclusion overclaims its evidence; F/G alone still measures location backing, not that depth.

# Scope and critic verdict

Attacked C1's axis naming against `SKILL.md:107-119` at content commit `46b4a7061c688cefd3e3ec9cbb655130ba1aafbe`, and the earlier objection in `.ufo/waves/round-58/build/CriticAxisFit.md:9-45`. This is a read-only content critique, not canonical judgment, admission, or a counter rerun. Axes: **depth and coverage**.

**The landed content is not only a locator map.** Its format, parameter, invocation, compatibility and migration distinctions give readers choices after they already know the folder. A depth label is therefore defensible for the actual content. The earlier critique remains correct about the frozen observable: source-backed locations and new location tokens do not establish semantic correctness. That limitation must not be turned into the stronger, unsupported assertion that the delivered cells contain no depth.

# Cell count

Population: seven rows times the two requested columns = **14 cells**. A decision-bearing cell supplies a format/key/substitution choice, applicability boundary, migration direction or precedence rule that changes authoring/auditing. Naming another directory alone would be locator-only. Counts describe content, not newly learned facts or a machine score.

| Landed row | What a file sets | Action |
|---|---|---|
| Claude Code, `SKILL.md:113` | Direct technical choice: Markdown, invocation mapping, excluded frontmatter keys and named arguments. | Direct choice: retain/audit older files, prefer skills for new work. |
| Codex, `:114` | Direct technical choice: `/prompts:` invocation, metadata and positional/all-argument placeholders. | Direct choice: user-local/deprecated form is unsuitable for repository distribution; migrate to skills. |
| VS Code, `:115` | Direct technical choice: `.prompt.md`, frontmatter controls and `${input:…}` rather than another client's placeholder syntax. | Direct applicability choice: Local harness versus a skill for other harnesses. |
| Copilot CLI, `:116` | **Indirect/weak:** `as Claude Code` imports another row's schema rather than stating CLI-specific facts. | Direct precedence choice: a same-named skill wins. The folder clause is locative, but the whole cell is not path-only. |
| Gemini CLI, `:117` | Direct technical choice: TOML, required `prompt`, optional `description`, colon namespacing and `{{args}}`. | Direct choice: TOML rather than Markdown; inspect both scopes. |
| Cursor, `:118` | Direct but thin: Markdown workflow body. The accompanying schema-absence wording needs the evidence qualification below. | **Unsupported exclusion:** `Audit the body only; nothing else to check` tells a reader to stop auditing beyond what the evidence establishes. |
| opencode, `:119` | Direct technical choice: `.md` discovery, slash-separated nested names, optional frontmatter, trimmed template and `$ARGUMENTS`. | **Generic/weak:** keeping a complete prompt template is actionable, but supplies no separate client-specific branch and overlaps held command craft. |

Tally:

- `What a file sets`: **6 direct-detail cells, 1 inherited cross-reference, 0 path-only cells**.
- `Action`: **5 specific source-linked decisions, 1 generic action, 1 unsupported exclusion, 0 path-only cells**.
- Combined: **11 cells with directly stated, source-linked, client-specific detail; 1 generic action; 1 inherited schema; 1 unsupported exclusion. Zero cells merely restate a path.** Of the 14, 13 explicitly state an authoring/auditing constraint or action; the remaining cell is the Copilot cross-reference. Counting a cell's supported component does not certify every clause in that cell.

Source support for this classification is recorded in the build receipts, not independently fetched by this seat: `SrcClaudeCode.md:18,53`; `SrcCodex.md:17,41`; `SrcVSCode.md:5-8,38`; `SrcCopilotCLI.md:20`; `SrcGeminiCLI.md:7,53`; `SrcCursor.md:6,16-18,32`; `Srcopencode.md:5,70`. All those paths are under `.ufo/waves/round-58/build/`.

# Strongest local counterexamples

## 1. Counterexample to the locator-only characterization

A reader already knows all seven directories and wants to reuse one Markdown command body across clients. `SKILL.md:117` still tells that reader to author Gemini's required TOML `prompt` and use `{{args}}`; `:115` supplies VS Code's different input syntax and Local-harness boundary; `:114` supplies Codex's different invocation and migration direction. Those are decisions a directory map cannot resolve. The corresponding source receipts give explicit format/argument/harness support, rather than deriving these distinctions from path spelling.

[INFERENCE] Removing the semantic/action cells while retaining every location would preserve location coverage but remove these authoring choices. This is a static content comparison, not an executed client failure.

Consequently the conditional objection in `CriticAxisFit.md:13-15,43-45` is partly answered by the landed table. Its important limit remains: **F/G is not a count of those decisions.** `verifiers/check_command_files.py:763-784` selects the location from `sr[1]`, never examines `sr[2]` there, and checks only a minimum word count for `sr[3]`. The landed entry already discloses this in `corpus/knowledge/command-files-round58.md:65-68`. No counter, target or rule change is proposed.

## 2. Fixable defect: Cursor converts incomplete evidence into audit completeness

`SKILL.md:118` makes the actionable claim `Audit the body only; nothing else to check`. But `build/SrcCursor.md:6,16-18,32` records only what particular command summaries establish and separately records migration guidance. It does not establish that all other audit dimensions are inapplicable. Missing schema documentation on selected pages is not evidence that no other behavior needs checking.

The source seat's draft actually preserved that narrower scope: its absence statement concerned the cited pages, while its action suggested migration. The landed action instead turns the limit into an unconditional stop rule. That is a real defect in depth precision, not merely a stylistic preference. I make no claim that Cursor lacks a schema: I did not perform the release-notes/current-docs-source-tree/corpus sweep required for a client-wide silence finding.

Smallest safe correction, without changing locations or the frozen observable:

- What a file sets: `Markdown workflow prompt; the cited pages do not establish frontmatter or argument behavior`.
- Action: `Audit the Markdown workflow body; this row does not establish a complete schema audit`.

## 3. Weak cells must not receive unsupported or duplicate depth credit

**Copilot:** `as Claude Code` at `SKILL.md:116` is useful shorthand only if full schema equivalence is established. The cited S028 loading/override passage establishes loading and precedence, not that every S089 frontmatter field and named-argument behavior is supported identically. `build/SrcCopilotCLI.md:20` records narrower CLI-specific facts: individual `.md` files and filename-derived names. This review does not demonstrate that equivalence is false; it identifies the unestablished inheritance.

Smallest safe correction: replace `as Claude Code` with the narrower `.md`/filename facts and cite that CLI-specific reference already recorded in the build receipt, rather than borrowing the complete S089 schema by implication.

**opencode:** the Action cell is generic, not locator filler, but it is not an independent new depth fact. Held craft already describes command frontmatter/body structure and pointer-versus-inline protocol choices (`corpus/knowledge/agent-defs-commands-and-round-prompts.md:51-63`). Its new row's stronger depth evidence is the documented discovery/name/template/argument behavior in the adjacent cell. No forced rewrite of the generic action is needed to establish that distinction.

Similarly, held Codex/VS Code locations (`corpus/knowledge/instruction-surface-census-round13.md:102-103`) do not erase their richer landed format/harness details; nor do new citations turn those locations into new coverage. Do not equate the 14 cells, seven rows, F, G, or the count above with wholly new knowledge.

# Disposition and limits

Impacted axes: **depth** (real technical detail, weakened by unsupported audit exclusion and schema inheritance); **coverage** (location expansion, distinct from semantic detail).

The fixable defects are the Cursor exclusion and Copilot's unqualified inheritance. The unavoidable evidence limit is that the frozen F/G result cannot certify the decision cells. Text corrections plus accurately bounded reporting are the safe response; relabelling the frozen claim, altering its predicate, or declaring a depth-band/saturation result from these counts is not. Admission and scoring remain with the canonical judge.

Read-only command evidence from this review, each returned normally with exit 0:

```text
timeout 30s git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show 46b4a7061c688cefd3e3ec9cbb655130ba1aafbe:SKILL.md
Output: landed SKILL.md, including the seven rows transcribed/count-classified above.

timeout 30s git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin diff 46b4a7061c688cefd3e3ec9cbb655130ba1aafbe -- SKILL.md corpus/knowledge/command-files-round58.md
Output: empty; the local line-numbered reads of these two files matched the attacked commit.

timeout 30s git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin diff --unified=3 f56f6e191762c27c1aa2af11a204db9e2ca4edec 46b4a7061c688cefd3e3ec9cbb655130ba1aafbe -- SKILL.md
Output: added Custom command files section with the seven landed rows; the existing anatomy move and other routed edits were also shown, not evaluated by this scoped seat.
```

No client runtime, lane code, counter, test, canonical judge, mutation or external fetch was executed. External-source claims above are attributed to existing build receipts, not fresh verification. No sandbox was needed; no tools were installed or updated. Only this assigned report was written. The milestone's other attacks were not this seat's assignment.
