Result: DONE — VS Code: ELIGIBLE `.github/instructions/**/*.instructions.md` key applyTo line 164

VS Code's own current docs, on pinned host `code.visualstudio.com`, name a targeted instruction file that applies only when an `applyTo` glob matches a file the agent creates or changes. The file-based feature is not marked experimental, preview, or deprecated on this page. No tool was installed.

## Fetched bytes

Tried the old path first. `date -u` printed `Fri 23 Oct 2026 10:29:05 AM UTC`.

`curl -sSL` with a Chrome User-Agent to `https://code.visualstudio.com/docs/copilot/customization/custom-instructions.md` returned HTTP 404, body `Not Found`, 9 bytes, sha256 `0019dfc4b32d63c1392aa264aed2253c1e0c2fb09216f8e2cc269bbfb8bb49b5`. Response `date: Fri, 23 Oct 2026 10:29:06 GMT`. Saved at `/fast/scratch/hyaku/kotoba-r60/CensusVSCode/custom-instructions.md`.

The unsuffixed old URL followed a redirect. Same `date -u` line. Final URL `https://code.visualstudio.com/docs/agent-customization/custom-instructions`, HTTP 200, 162320 bytes, sha256 `1286d04983e30671ccdc82cab51e2a1a79288aecc5f4983162cda7db8721c369`. HTML, not the scored bytes. Saved at `/fast/scratch/hyaku/kotoba-r60/CensusVSCode/custom-instructions.html`.

Scored page: `date -u` printed `Fri 23 Oct 2026 10:29:10 AM UTC`.

`curl -sSL` same User-Agent to `https://code.visualstudio.com/docs/agent-customization/custom-instructions.md` returned HTTP 200, `content-type: text/markdown; charset=UTF-8`, `content-length: 23715`, `last-modified: Thu, 22 Oct 2026 22:04:56 GMT`, response `date: Fri, 23 Oct 2026 10:29:11 GMT`. `wc -c` 23715. sha256 `a45c9e9f50c62949ea60711c6d657d065752c573a0c945215f32063fa56caa1f`. 367 lines. Saved at `/fast/scratch/hyaku/kotoba-r60/CensusVSCode/agent-custom-instructions.md`.

## Token as printed

`.github/instructions/**/*.instructions.md`

Line 27, Copilot row, column Targeted instructions (`sed -n '27p'`):

```
| Copilot | [`.github/copilot-instructions.md`](#use-a-githubcopilot-instructionsmd-file) or [`AGENTS.md`](#use-an-agentsmd-file) | [`.github/instructions/**/*.instructions.md`](#use-instructionsmd-files) |
```

Also on line 32, inside the Local-harness note. The Copilot table cell is not local-only.

## Quote (line 32)

No markdown bytes stripped. Substring of `sed -n '32p'`:

```
> **For Local harness sessions:** Project instructions can use `.github/copilot-instructions.md`, `AGENTS.md`, or `CLAUDE.md`. Targeted instructions can use `.github/instructions/**/*.instructions.md` or Markdown files in `.claude/rules`. The Local harness-specific settings in the sections below control discovery.
```

Quote, 10 words after `quote.replace("`", "").split()` (the counter's count):

Targeted instructions can use `.github/instructions/**/*.instructions.md` or Markdown files in `.claude/rules`.

Words: Targeted, instructions, can, use, `.github/instructions/**/*.instructions.md`, or, Markdown, files, in, `.claude/rules.`

Token span in the backtick-stripped quote is bytes 30-71; the character on each side is a space. `(?i)\b(rules?|instructions?)\b` matches `instructions` at 9-21, outside that span, and `rules` at 101-106 (the `.claude/rules` tail), also outside. Two further `instructions` matches sit inside the token and do not count.

## Scope key

K = `applyTo`. L = 164. `sed -n '164,167p'`:

```
applyTo: '**/*.py'
---
# Python testing

```

`applyTo` is at an identifier boundary, followed by `:`. The same line has the run `**/*.py` (class `[A-Za-z0-9_./*{},!-]` and contains `*`).

A second passing site, line 156, is the backticked table cell plus the word `pattern` and the glob `**` (`sed -n '156p'`):

```
| `applyTo` | No | Glob pattern that automatically applies the instructions to matching files, relative to the workspace root. Use `**` to match all files. |
```

Line 54 has the word `pattern` but `applyTo` is not followed by `:` or `=` and is not a table cell, so it is not a key site:

```
* **File pattern**: VS Code automatically attaches an `.instructions.md` file when its `applyTo` pattern matches a file that the agent creates or modifies.
```

## Action line

`sed -n '329p'`:

```
* For task or language-specific instructions, use multiple `*.instructions.md` files per topic and apply them selectively by using the `applyTo` property.
```

That is what a rule author does: put the guidance in an instructions file and apply it selectively with `applyTo`, instead of loading it every turn. Line 105 is the behaviour the key produces (`sed -n '105p'`):

```
You can create file-based instructions with `*.instructions.md` Markdown files. VS Code automatically attaches files with an `applyTo` pattern that matches the files being changed. The agent can also load an instructions file on demand when its `description` matches the current task.
```

## Conjuncts (on the fetched markdown)

- Own docs on a pinned host (`code.visualstudio.com`): yes.
- Names a rule/instruction file: yes. Line 27, Targeted instructions column. Line 105 calls them instructions files.
- Applies only for matching files: yes. Lines 54, 105, and 156. Not the always-on project file.
- Path regex of `check_hook_files.py` (`TOKEN_RE`): yes. `fullmatch` is true. `*` is legal in a non-first segment, so the middle `**` is inside the regex.
- At least two segments after one leading `~/` or `./`: yes. `.github`, `instructions`, `**`, `*.instructions.md`.
- First segment starts with `.`: yes.
- No segment word skill(s)/agent(s)/command(s)/prompt(s)/plugin(s)/extension(s)/hook(s): yes. `instructions` is allowed by the C1 row rule. Split of `*.instructions.md` on `-._` is `*`, `instructions`, `md`.
- E7 (no dot in a non-final segment except as its first character): yes. `.github` has the dot first; `instructions` and `**` have none; the dots in `*.instructions.md` are in the final segment.
- No other client's marker (`claude`, `codex`, `vscode`, `copilot`, `gemini`, `cursor`, `opencode`): yes.
- E5 (shared token): dropped by the row rule. Not applied.
- Frontmatter key K names the matching paths: yes, `applyTo`.
- K stands as a key that takes a path pattern on line L: yes, line 164 (and line 156).
- Verbatim 6-25-word quote with the token and rule/instruction outside the token: yes, 10 words, line 32.
- A line an Action cell can cite: yes, line 329.

## Status marks

Grep of the fetched markdown for experimental / preview / deprecated / beta hits three lines, none of them this feature:

- Line 130: `setting(chat.instructionsFilesLocations)` "remains supported and is not deprecated" (custom search locations, not `applyTo`).
- Line 292: "Settings-based code generation and test generation instructions are deprecated as of VS Code 1.102." The same line points at file-based instructions as the replacement.
- Line 323: an example sentence in which moment.js "is deprecated". Not a product mark.

No experimental, preview, or beta mark on the page.

## Wrong key: `description`

A careless author would cite `description` (line 155 table, line 163 example). It fails the Scope-key rule.

Line 163 (`sed -n '163p'`):

```
description: 'Use when creating or updating Python unit tests.'
```

`description` is followed by `:`, but the line has no `*` run, and it has no whole word glob/globs/pattern/patterns. After `:` the value is `'Use when creating or updating Python unit tests.'`, not only spaces, `[`, or `|`, so the next-three-lines block exception does not apply. Line 164's glob does not rescue line 163.

Line 155 is a backticked table cell and still fails: no `*` and no glob/pattern word (`sed -n '155p'`):

```
| `description` | No | Describes the tasks for which the file is relevant. Include it for on-demand discovery. |
```

`name` (lines 154 and 162) fails the same way.

`paths` is the other tempting miss. Line 249 tells Claude-rule authors to use `paths` "for glob patterns" and mentions `**`, but `paths` is never followed by `:` or `=` and is never a backticked table cell on this page, so it is not a key site. `.claude/rules` also carries Claude Code's marker and is not the VS Code token.

## Other printed paths (not the chosen token)

- `.github/instructions` (line 120, Copilot workspace folder) and `.github/instructions/` (line 135, code block) are also well-formed under the same grammar, and the folder has its own quote. Line 128, 7 words after backtick strip: `Workspace instruction files use `.github/instructions` or `.claude/rules``. Outside word: `instruction`. Same key line 164. Eligible as a folder token. The plan's shared-token example is this folder. The result line uses the targeted-file glob because that is the path in the Targeted instructions column.
- `.github/copilot-instructions.md` (line 64) is project-wide, not path-scoped, and the substring `copilot` is Copilot CLI's marker.
- `~/.copilot/instructions` (line 122) carries `copilot`.
- `.claude/rules` (lines 28, 121, 249) carries `claude`.
- `*.instructions.md` is one segment, fails `TOKEN_RE`, and does not start with `.`.

## Base tree at `31092dc6f875370bddd6eb1e4da4ca0d210c56af`

```
git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin grep -ilF '.github/instructions/**/*.instructions.md' 31092dc6f875370bddd6eb1e4da4ca0d210c56af -- . ':!.ufo' | wc -l
```

Printed `0`. `wc` exit 0.

The same command with `.github/instructions` printed `1`. The one path is `corpus/knowledge/instruction-surface-census-round13.md` (omp loader class, not this scope key).

```
git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show 31092dc6f875370bddd6eb1e4da4ca0d210c56af:SKILL.md | grep -cF 'applyTo'
```

Printed `0`. `grep -c` exit 1, which is grep's zero-matches status, not a missing file.
