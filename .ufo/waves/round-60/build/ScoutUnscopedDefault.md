Result: DONE — On the four eligible pages, a rule file without the scope key is always-loaded (Claude Code), manual only when both keys are omitted (VS Code), one of always / agent-requested / manual depending on the other fields (Cursor), and not stated (Copilot CLI); a match applies on Read/Write/Edit (Claude Code), when the agent creates or modifies a file (VS Code), when a matching file is in context (Cursor), or when Copilot CLI is working with a matching file (read vs create/edit not stated).

No tools installed. Scratch: `/fast/scratch/hyaku/kotoba-r60/ScoutUnscopedDefault/`. Fetched with the counter's curl (`-sSL --max-time 30`, Chrome/130 UA, `Accept: text/markdown, text/plain;q=0.9, */*;q=0.8`). `date -u` before the fetch: `Fri 23 Oct 2026 12:08:15 PM UTC`. Pipeline exit 0.

| Client | URL | HTTP | Response `date` | Bytes | sha256 |
|---|---|---|---|---|---|
| Claude Code | `https://code.claude.com/docs/en/memory.md` | 200 | `Fri, 23 Oct 2026 12:08:16 GMT` | 54043 | `82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7` |
| VS Code | `https://code.visualstudio.com/docs/agent-customization/custom-instructions.md` | 200 | `Fri, 23 Oct 2026 12:08:16 GMT` | 23715 | `a45c9e9f50c62949ea60711c6d657d065752c573a0c945215f32063fa56caa1f` |
| Copilot CLI | `https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md` | 200 | `Fri, 23 Oct 2026 12:08:16 GMT` | 8730 | `00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980` |
| Cursor | `https://cursor.com/docs/rules` | 200 | `Fri, 23 Oct 2026 11:56:27 GMT` | 17403 | `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8` |

`sha256sum` of the four bodies printed those digests (exit 0). `wc -l`: 664, 367, 110, 399. Content-Type `text/markdown` on all four. The phrase `creates or changes` occurs on none of them (`grep -nF 'creates or changes'` exit 1, no output).

Word counts below are `printf '%s\n' '<quote>' | wc -w` on that quote, run in that order, output `14 / 13 / 17 / 12 / 20 / 15 / 17 / 17 / 15 / 7 / 11 / 18 / 7 / 8 / 11 / 9 / 9`. Each quote is a byte-exact substring of the `sed -n` line (checked by Python `quote in line`). Nothing inside a quote was stripped.

## Claude Code — without `paths`: always loaded at launch

Not agent-requested and not manual. Two lines say so.

```
sed -n '188p' claude.md
Rules without [`paths` frontmatter](#path-specific-rules) are loaded at launch with the same priority as `.claude/CLAUDE.md`.
```

Quote (whole line, 14 words): `Rules without [`paths` frontmatter](#path-specific-rules) are loaded at launch with the same priority as `.claude/CLAUDE.md`.`

```
sed -n '209p' claude.md
Rules without a `paths` field are loaded unconditionally and apply to all files. A path-scoped rule loads when Claude uses the Read, Write, or Edit tool on a matching file. It also loads when Claude views a matching file with a Bash command that [counts as a read](/docs/en/tools-reference.md#edit-tool-behavior), such as `cat` or `head` on a single file. Matching also works when Claude reaches a file through a symlinked path to the project directory, for example in a symlinked checkout.
```

Quote (first sentence, 13 words): `Rules without a `paths` field are loaded unconditionally and apply to all files.`

Line 250's Required cell is `No` for `paths`, but that cell does not say the load behavior. Line 252 says unparseable frontmatter is loaded as if it had no `paths` (same unconditional path). Not the primary fact.

## Claude Code — a match applies on Read, Write, or Edit

On read and on write/edit, not create/edit only. Same line 209, second sentence (17 words): `A path-scoped rule loads when Claude uses the Read, Write, or Edit tool on a matching file.` The rest of the line adds a Bash view that counts as a read (`cat` or `head` on a single file). `creates or changes` and `creates or modifies` are absent from this page.

Line 172 is the coarser note (12 words, inside the `> ` callout): `Rules load into context every session or when matching files are opened.` It does not name the tool.

Both facts sit on line 209, so one Action citation can carry "without `paths`" and "Read, Write, or Edit".

## VS Code — without `applyTo` alone: not stated on the cited page

The page never says that an `*.instructions.md` file lacking only `applyTo` is always loaded, agent-requested, or manual. `applyTo`'s Required cell is `No` (line 156) and that cell does not give the fallback.

What is stated is omitting both keys (line 173, first sentence, 17 words): `If you omit both `description` and `applyTo`, attach the file manually when you want to use it.`

```
sed -n '173p' vscode.md
If you omit both `description` and `applyTo`, attach the file manually when you want to use it. For Claude rules, use the `paths` property instead of `applyTo`.
```

The description mechanism, stated separately, is on-demand, not "without `applyTo`":

```
sed -n '105p' vscode.md
You can create file-based instructions with `*.instructions.md` Markdown files. VS Code automatically attaches files with an `applyTo` pattern that matches the files being changed. The agent can also load an instructions file on demand when its `description` matches the current task.
```

Quote (third sentence, 17 words): `The agent can also load an instructions file on demand when its `description` matches the current task.`

Line 249's `**` default is about Claude `.claude/rules`, not VS Code `applyTo`. Do not cite it as the VS Code omission rule.

```
sed -n '249p' vscode.md
> For `.claude/rules` instructions files, use a `paths` property instead of `applyTo` for glob patterns, following the [Claude rules format](https://code.claude.com/docs/en/memory#basic-structure). The `paths` property accepts an array of glob patterns and defaults to `**` when omitted.
```

Quote (last sentence, 15 words): `The `paths` property accepts an array of glob patterns and defaults to `**` when omitted.`

## VS Code — a match applies when the agent creates or modifies

Not "creates or changes" (that phrase is absent). Not stated for a read that does not create or modify (`grep -nEi 'read tool|when .*read|opens a file|file is opened'` on this page: no output).

```
sed -n '54p' vscode.md
* **File pattern**: VS Code automatically attaches an `.instructions.md` file when its `applyTo` pattern matches a file that the agent creates or modifies.
```

Quote (after the 20-byte label `* **File pattern**: `, 20 words): `VS Code automatically attaches an `.instructions.md` file when its `applyTo` pattern matches a file that the agent creates or modifies.`

Line 105, second sentence (15 words): `VS Code automatically attaches files with an `applyTo` pattern that matches the files being changed.`

Line 347 repeats `creates or modifies` and adds the neither-case manual attach. It does not say "omit both".

```
sed -n '347p' vscode.md
* For `*.instructions.md` files, check that `applyTo` matches a file the agent creates or modifies, or that `description` clearly identifies the relevant task. If neither applies, attach the file manually.
```

Quote (last sentence, 7 words): `If neither applies, attach the file manually.`

The omit-both sentence (173) and the creates-or-modifies sentence (54, also 347) are not the same line. An Action cell cites one line: 54 or 105 for the match timing, 173 for omit-both. 347 has both "creates or modifies" and the manual fallback, but not the words "omit both".

## Copilot CLI — without `applyTo`: not stated on the cited page

The 110-line page has no `omit`, no `without`, no `manual`, no `on demand` (`grep -nEi 'omit|without|manual|on demand'` matched only the two `Optionally` steps). Those are step 2 (subdirectories) and step 5 (`excludeAgent`), not `applyTo`. Step 4 tells the author to write `applyTo`; it does not say what a file in `.github/instructions` does when the key is absent. The "Read" hits are "create the directory", "reads the referenced file", "only be read by Copilot cloud agent", and "Further reading" — none is a load rule for a missing key.

What the page does say is the with-key case only (line 11, clause after the em dash, 11 words): `a file with an `applyTo` value applies only to matching files.`

```
sed -n '11p' copilot.md
Unless noted in the table below, Copilot CLI discovers repository and agent instruction files in the **standard locations**: the repository root, the current working directory, intermediate directories between them, and any directories nested in the path of a file it is working on. Modular instruction files (those matching `*.instructions.md`) are path-specific—a file with an `applyTo` value applies only to matching files.
```

## Copilot CLI — when a match applies: "working with"; read vs create/edit not stated

```
sed -n '32p' copilot.md
Path-specific instructions are included only when their `applyTo` value matches a file that Copilot CLI is working with. An instruction file that you disable using `/instructions` is not included.
```

Quote (first sentence, 18 words): `Path-specific instructions are included only when their `applyTo` value matches a file that Copilot CLI is working with.`

No `creates or`, no `Edit`, no `modify` on this page. The read-versus-create/edit distinction is not stated on the cited page. Line 32 is the only Action line for the timing fact. There is no line an Action cell can cite for the missing-key fact.

## Cursor — without `globs`: three stated behaviors, not one

Project rules in `.cursor/rules`. The page's own table (lines 65–70) splits on the other two fields. `globs` omitted is not "always loaded" by itself.

```
sed -n '65,70p' cursor.md
| `alwaysApply` | `description` | `globs`  | Behavior                                                         |
| :------------ | :------------ | :------- | :--------------------------------------------------------------- |
| `true`        | —             | —        | Always included. Globs and description are ignored.              |
| `false`       | —             | provided | Auto-attached when a matching file is in context.                |
| `false`       | provided      | omitted  | Agent reads the description and pulls the rule in when relevant. |
| `false`       | omitted       | omitted  | Included only when you `@`-mention the rule in chat.             |
```

Behavior cell only (the other three cells are not in the quote):

- Line 67, `globs` absent because `alwaysApply` is true (7 words): `Always included. Globs and description are ignored.` Always loaded. The dash cells are "—", not the word `omitted`.
- Line 69, `globs` omitted and `description` provided (11 words): `Agent reads the description and pulls the rule in when relevant.` Agent-requested.
- Line 70, `globs` omitted and `description` omitted (9 words): `Included only when you `@`-mention the rule in chat.` Manual.

Line 42 is a different miss: a plain `.md` in `.cursor/rules` is ignored because it has no frontmatter at all, not because `globs` is absent from an `.mdc` rule.

Do not cite line 186 as the without-key rule. It is under `## Rule file format`, its example frontmatter has `description` and `alwaysApply: false` and no `globs`, and the sentence drops the manual row:

```
sed -n '186p' cursor.md
If alwaysApply is true, the rule will be applied to every chat session. Otherwise, the description of the rule will be presented to the Cursor Agent to decide if it should be applied.
```

That "otherwise" contradicts line 70 (no description and no globs → `@`-mention only). The table at 67–70 is the page's "Under the hood" account.

Line 305 is Team Rules, not a file in `.cursor/rules`. Separate surface: `Rules without a glob pattern apply to every conversation.` (9 words). Do not use it as the project-rule Action fact.

## Cursor — a match applies when a matching file is in context

Read vs create/edit is not stated on the cited page (`grep -nEi 'creates or|modifies|Read, Write|on edit'` no output).

Line 68 behavior cell (8 words): `Auto-attached when a matching file is in context.` That row is `globs` provided, not omitted.

The three without-`globs` facts and the in-context fact are four different rows. One Action citation cannot cover both "without the key" and "when a match applies".

## Citation map for an Action cell (one line each)

| Client | Without the scope key | When a matching rule applies | Same line? |
|---|---|---|---|
| Claude Code | 188 launch; 209 unconditionally, all files | 209 Read, Write, or Edit (also Bash that counts as a read) | Yes, 209 |
| VS Code | 173 manual, only when both `description` and `applyTo` are omitted; `applyTo` alone not stated | 54 and 347 `creates or modifies`; 105 `files being changed`. Not on read | No. 347 has the timing and "if neither, manually", not "omit both" |
| Copilot CLI | not stated on the cited page | 32 `working with`. Read vs create/edit not stated | No without-key line |
| Cursor | 67 always (when `alwaysApply` is true); 69 agent-requested; 70 manual | 68 `in context`. Read vs create/edit not stated | No |

Confidence: high on these four fetched pages. Unresolved: no other URL was opened, so a fact that lives only on a help or changelog page is outside this note; the Action cell still has to cite the snapshot of the row's own page.
