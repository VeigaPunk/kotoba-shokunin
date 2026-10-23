Result: DONE — Copilot CLI: ELIGIBLE `.github/instructions/**/*.instructions.md` key `applyTo` line 66

Client: Copilot CLI. One eligible path-scoped instruction file. Not marked experimental, preview, or deprecated (those words are absent from the fetched page). No tools installed.

## Page

- URL: `https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md`
- Pinned host: `docs.github.com` (Copilot CLI pin in `verifiers/check_hook_files.py` HOSTS). How-to path, not changelog/release/news/blog.
- `date -u` immediately before the fetch: `Fri 23 Oct 2026 10:29:28 AM UTC` (saved at `/fast/scratch/hyaku/kotoba-r60/CensusCopilotCLI/date-fetch1.txt`).
- Fetch: `curl -sSL -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'` of the `.md` URL. HTTP/2 200, `content-type: text/markdown; charset=utf-8`, 8730 bytes, sha256 `00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980`.
- Same sha256 from `Accept: text/markdown` on the URL without `.md` (also HTTP 200, 8730 bytes). The HTML URL without that Accept header is a different body (603412 bytes, sha256 `0959b521c413899e5949d4b2264e90651ecac6dca94f8e5ac018c64bc0d62f68`) and was not scored.
- Fetched bytes: `/fast/scratch/hyaku/kotoba-r60/CensusCopilotCLI/cli-md.body` (copy `/fast/scratch/hyaku/kotoba-r60/CensusCopilotCLI/add-custom-instructions.md`, same sha256). Header dump: `cli-md.hdr`.

Title line 1: `Adding custom instructions for GitHub Copilot CLI`. This is Copilot CLI's own page, not the VS Code or github.com coding-agent page.

## Token

Exact printed token (line 18, backticked table cell): `.github/instructions/**/*.instructions.md`

`sed -n '18p'` of the fetched bytes:

```
| `.github/instructions/**/*.instructions.md`              | Modular repository instructions, discovered in the standard locations but not intermediate directories.                                                         |
```

Applies only to matching files (not the repository-wide file on line 17):

- Line 11: `Modular instruction files (those matching `*.instructions.md`) are path-specific—a file with an `applyTo` value applies only to matching files.`
- Line 32: `Path-specific instructions are included only when their `applyTo` value matches a file that Copilot CLI is working with.`

## Quote (no bytes stripped)

Contiguous slice of line 18, from the opening backtick of the token through the word `locations` (14 spaces between the closing backtick and the table pipe; 128 bytes). Saved at `/fast/scratch/hyaku/kotoba-r60/CensusCopilotCLI/quote.txt`.

```
`.github/instructions/**/*.instructions.md`              | Modular repository instructions, discovered in the standard locations
```

Whitespace split after removing backticks (count unchanged if backticks stay, because they are not their own words): **10 words** (need 6–25).

1. `.github/instructions/**/*.instructions.md`
2. `|`
3. `Modular`
4. `repository`
5. `instructions,`
6. `discovered`
7. `in`
8. `the`
9. `standard`
10. `locations`

Token span on the backtick-stripped quote is `[0, 41)`. `(?i)\b(rules?|instructions?)\b` hits `instructions` at offsets 8–20 and 26–38 inside that span, and `instructions` at 76–88 in `repository instructions,` **outside** the span.

## Scope key

K = `applyTo`. L = 66 (first line where K is a key taking a path pattern).

`sed -n '66,69p'`:

~~~~
   applyTo: "app/models/**/*.rb"
   ---
   ```

~~~~

K is at an identifier boundary, followed by `:`. The same line holds the run `app/models/**/*.rb` of `[A-Za-z0-9_./*{},!-]` containing `*`. The block-or-next-3-lines clause is not needed.

Later key sites on the same page, not used as L: line 74 `applyTo: "**/*.ts,**/*.tsx"` and line 94 `applyTo: "**"`.

## Action line

`sed -n '60p'`:

```
4. At the start of the file, create a frontmatter block containing the `applyTo` keyword. Use glob syntax to specify what files or directories the instructions apply to.
```

What a rule author does: put an `applyTo` glob in the frontmatter of a `NAME.instructions.md` file under `.github/instructions` so the instructions apply only to the named files (steps 1–4, lines 54–60).

## Conjuncts

| conjunct | on the fetched bytes |
|---|---|
| Own Copilot CLI documentation | YES — line 1 title |
| Pinned host `docs.github.com` | YES |
| Not a changelog/release/news/blog URL | YES |
| Names a file for an instruction file | YES — line 18, "Modular repository instructions" |
| Applies only when the agent works on matching files | YES — lines 11 and 32 |
| Path regex `^(~/|\./)?[A-Za-z0-9_.-]+(/[A-Za-z0-9_.*-]+)*/?$` (`check_hook_files.py` TOKEN_RE) | YES — `*` is legal in a non-first segment, including `**` |
| ≥ 2 segments after one leading `~/` or `./` | YES — 4 segments (`.github`, `instructions`, `**`, `*.instructions.md`); nothing stripped |
| First segment starts with `.` | YES |
| No segment word skill/agent/command/prompt/plugin/extension/hook (and plurals). `instructions` is allowed | YES — words are `github`, `instructions`, `**`, `*`, `instructions`, `md` |
| E7: no dot in a non-final segment except as its first character | YES — only `.github` has a dot, and it is the first character |
| No other client's marker (`claude`, `codex`, `vscode`, `gemini`, `cursor`, `opencode`) | YES — `copilot` is also absent |
| E5 shared-token ban | DROPPED by the row rule — not applied |
| K stands as a key that takes a path pattern on one line L | YES — `applyTo:` on line 66 |
| Glob containing `*` on L, or the block rule, or glob/pattern on L | YES — `app/models/**/*.rb` on line 66 |
| Verbatim quote, 6–25 words, token at a segment boundary, and rule/instruction outside the token | YES — 10 words, line 18 slice |
| A line an Action cell can cite | YES — line 60 |
| Marked experimental/preview/deprecated | NO |

## Wrong key

`description` is not on this page. The printed non-scoping frontmatter key is `excludeAgent`.

`sed -n '95,98p'`:

~~~~
   excludeAgent: "code-review"
   ---
   ```

~~~~

Line 95 has `excludeAgent` followed by `:`, so the key-form half passes, but the line has no run of `[A-Za-z0-9_./*{},!-]` containing `*`, and no word `glob`/`globs`/`pattern`/`patterns`. What follows `:` is `"code-review"`, not only spaces, `[`, or `|`, so the next-3-lines block rule does not open. Lines 96–98 are `   ---`, `   ``` `, and a blank line. **FAIL** the Scope-key rule.

A second miss: line 60 backticked `` `applyTo` `` is not followed by `:` or `=` and is not a `| `applyTo` |` table cell. The word `glob` on that line does not make it a key site. **FAIL** the key-form half. Line 66 is the site.

Not a candidate: `.github/copilot-instructions.md` (line 17) is repository-wide, not matching-files only. `$HOME/.copilot/instructions/**/*.instructions.md` (line 16) fails TOKEN_RE (`$`) and the first segment is not dot-led. `AGENTS.md` / `CLAUDE.md` / `GEMINI.md` are not path-scoped instruction files under this rule (`CLAUDE.md` also carries another client's marker).

## Also well-formed (not the counted token)

Folder `.github/instructions` (line 54: `Create the `.github/instructions` directory`) passes the same token grammar (2 segments, E7, no banned word, no foreign marker). Quote, whole line 56, 11 words, `instruction` outside the token, no bytes stripped:

```
2. Optionally, create subdirectories of `.github/instructions` to organize your instruction files.
```

The counted token is the file pattern on line 18, because that is the rule file the location table names. [INFERENCE] A counter that banned `*` outside the final segment would reject the counted token and still have this folder. TOKEN_RE as written does not ban it. The client is one eligible client either way.

## Base counts (rev `31092dc6f875370bddd6eb1e4da4ca0d210c56af`)

```
git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin grep -ilF '.github/instructions/**/*.instructions.md' 31092dc6f875370bddd6eb1e4da4ca0d210c56af -- . ':!.ufo' | wc -l
```

`wc -l` printed `0`. With `set -o pipefail` the pipeline exit is 1 because `git grep` exits 1 when no file matches.

```
git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show 31092dc6f875370bddd6eb1e4da4ca0d210c56af:SKILL.md | grep -cF 'applyTo'
```

Printed `0`, exit 1 (grep's no-match exit).

The shorter folder string `.github/instructions` is already in one base file outside `.ufo`: `corpus/knowledge/instruction-surface-census-round13.md`. That is not the counted token.
