Result: HOLDS — Issues, discussions, the CLI changelog, and the current docs source still name no Copilot CLI command or prompt folder of its own; `.github/prompts` stays an IDE path the cheat sheet marks unsupported on Copilot CLI, and the only command-file path in the changelog is `.claude/commands/`.

Attacks the Copilot CLI negative in `corpus/knowledge/command-files-round58.md:18-21`, `SKILL.md:116`, and `corpus/lessons/round-58.md:23-29` (NOT ELIGIBLE; no own folder). Goes past `.ufo/waves/round-58/build/ScoutCopilotPrompts.md`, which did not open issues or discussions. No tools installed. No lane code run. Fetched bytes under `/fast/scratch/hyaku/kotoba-r58/ScoutCopilotNegative/`.

## Q30 — changelog

`https://raw.githubusercontent.com/github/copilot-cli/main/changelog.md`. `date -u` immediately before the batch: `Fri 23 Oct 2026 08:28:39 AM UTC`. HTTP 200. 289859 bytes. sha256 `c4b793bd6555bf699c1f6ef61fb9052e6400df8f475c97fdae25ba5084531dfb` (same bytes as the 08:08Z fetch in `ScoutCopilotPrompts`). 3570 lines. Exact counts in those bytes:

| Needle | Count | Line |
|---|---:|---|
| `.github/prompts` | 0 | — |
| `.github/commands` | 0 | — |
| `.copilot/prompts` | 0 | — |
| `.copilot/commands` | 0 | — |
| `.github/copilot/commands` | 0 | — |
| `prompt file` / `prompt files` / `.prompt.md` | 0 | — |
| `com.github.copilot/commands` | 0 | — |
| `.claude/commands` | 1 | 2932 |
| `command files` | 1 | 2695 |
| `Commands from plugins` | 1 | 2824 |
| `custom paths` | 1 | 2617 |

Line 2932, under `## 0.0.399 - 2026-01-29` (heading line 2921). 9 words, leading `- ` not included, no other bytes stripped:

```
Support `.claude/commands/` single-file commands as simpler alternative to skills
```

Line 2695, under `## 0.0.412 - 2026-02-19` (heading line 2664). 6 words, the clause before the em dash; the rest of the bullet omitted:

```
Command files no longer require YAML frontmatter
```

That bullet names no directory. [INFERENCE] It continues the `.claude/commands/` files from 0.0.399, because that is the only command-file path in this changelog. Line 2617 (`## 0.0.417 - 2026-02-25`) is plugin `plugin.json` paths, not a user folder. Line 2824 (`## 0.0.406 - 2026-02-07`) translates plugin commands into skills. `~/.copilot` occurs 16 times (settings, logs, hooks, instructions); none is `commands/` or `prompts/`. Line 2512 is `~/.copilot/hooks`.

`docs.github.com` has no separate Copilot CLI changelog page. The reference index fetched in the same 08:28:39Z batch (`https://docs.github.com/en/copilot/reference/copilot-cli-reference.md`, HTTP 200, 1021 bytes, sha256 `d9c707cc59fe9a145646d0dbc8a63a5d9ecb9419f434781e3f0a45b433ff6b90`) links command, plugin, programmatic, ACP, and config-dir references only.

## Q30 — docs source tree

GitHub contents API, `github/docs` `main`, walked `content/copilot/how-tos/copilot-cli` and `content/copilot/reference` (depth ≤ 3). 99 markdown files. Raw bodies downloaded after `Fri Oct 23 08:30:11 AM UTC 2026` and before `Fri Oct 23 08:31:09 AM UTC 2026`. Each HTTP 200. 1146915 bytes total. Per-file size and sha256: scratch `docs-src-manifest.tsv`. Exact counts over those 99 files:

| Needle | Files |
|---|---|
| `.github/prompts` | 1: `reference/customization-cheat-sheet.md:21` |
| `.github/commands`, `.copilot/prompts`, `.github/copilot/commands` | 0 |
| `.copilot/commands` | 1, and it is the substring inside `com.github.copilot/commands` at `cli-plugin-reference.md:171` |
| `.claude/commands` | `cli-command-reference.md:1345`, `cli-plugin-reference.md:429` |
| `prompt file` / `prompt files` | cheat sheet and `custom-instructions-support.md:140` (JetBrains editor prose, not CLI) |

Code search on the same tree, `Fri Oct 23 08:31:09 AM UTC 2026`, `gh api search/code` (exit 0):

- `repo:github/docs path:content/copilot .github/prompts` — total 9, `incomplete_results` false. Eight are IDE prompt-file pages (concepts, tutorials, the IDE repository-instructions how-to). The ninth is the cheat sheet. None sit under `copilot-cli/`.
- `path:content/copilot .copilot/prompts` — total 0.
- `path:content/copilot .copilot/commands` — total 1, `cli-plugin-reference.md` only.

The eight IDE sources were fetched next (each HTTP 200). Grep for `Copilot CLI`, `copilot_cli`, and `copilot-cli`: no hits. The only `CLI` hit is the substring inside `ECLIPSE` at `add-repository-instructions-in-your-ide.md:350`.

Concepts source `content/copilot/concepts/prompting-and-context/prompt-files.md`, HTTP 200, 2681 bytes, sha256 `5f2d8591d5094996583be1ee6a7280ee8a64fc0ca9e42ff15877a403065faa88`. Line 19 names VS Code, Visual Studio, JetBrains, and Xcode via liquid plus the literal `Xcode`. The line does not contain `CLI`. 5 words, liquid and the rest of the sentence omitted:

```
Prompt files are available in
```

Cheat sheet source, same 99-file set: `content/copilot/reference/customization-cheat-sheet.md`, HTTP 200, 7954 bytes, sha256 `560d6a0ec3d96a8ee9caae13d506d1f473c2e248ccec65f7579a5f8344c93e2a`. Also the rendered page, `Fri 23 Oct 2026 08:28:16 AM UTC`, HTTP 200, 10699 bytes, sha256 `25f43326fb38833208df14cc9d9f6a72bf182f0785bf5b2a86748953a0fc3b25`, URL `https://docs.github.com/en/copilot/reference/customization-cheat-sheet.md`.

Source line 21 names `.github/prompts/*.prompt.md` as the prompt-file location, with no client in that cell. Source line 54's last header cell is `{% data variables.copilot.copilot_cli_short %}`. Rendered line 47 prints that cell as `Copilot CLI`. Source line 51, 4 words:

```
✗ = not supported
```

Source line 57, the whole row, no bytes stripped (9 whitespace-separated tokens besides the pipes):

```
| Prompt files | ✓ | ✓ | P | ✗ | P | ✗ | ✗ |
```

The last cell is the Copilot CLI column. Prompt files are not supported there. Rendered line 50 matches. `copilot-feature-matrix.md` (HTTP 200, 10792 bytes, sha256 `0c21a959ce07719b930bd31dfc8ecb23be3e97064bfedf417c4cd5722933a3dc`) has no `prompt`, `commands/`, or `.claude/` hit.

Config-dir source `cli-config-dir-reference.md`, HTTP 200, 74754 bytes, sha256 `78eb9462dcaf3171f29da007e10981632da3d4d323eb4994ad416896a940a54a`. Line 22, 8 words:

```
The `~/.copilot` directory contains the following top-level items.
```

Path column, lines 26–46: `agents/`, `config.json`, `copilot-instructions.md`, `extensions/`, `hooks/`, `ide/`, `installed-plugins/`, `instructions/`, `logs/`, `lsp-config.json`, `mcp-config.json`, `mcp-oauth-config/`, `mcp-secrets/`, `permissions-config.json`, `plugin-data/`, `providers.json`, `session-state/`, `command-history-state/`, `session-store.db`, `settings.json`, `skills/`. No `commands/` and no `prompts/`. Line 59, 18 words, says `COPILOT_HOME` moves that directory; it does not add a folder:

```
You can change the location of this directory by setting the `COPILOT_HOME` environment variable to a different path.
```

Command-reference source line 1345 (177073 bytes, sha256 `48de33ea09a3e532f2355c45886d6e17aa37090fe9599cd4240a1d04f035c7f2`) still places command files in `.claude/commands/`. Plugin-reference source (33751 bytes, sha256 `e8910f62faa9710da029ce74a1072735addfabee6004cd17727d27ba1c55c09f`) line 171 is `com.github.copilot/commands/`, line 176 limits it to Agent Plugins 1.0, line 212's legacy `commands` default is `—` with the 4-word description `Path(s) to command directories.`, and line 429 repeats `.claude/commands/`.

## Q30 — lane corpus

`grep` on `/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus` for `\.copilot/commands|\.copilot/prompts|\.github/commands|com\.github\.copilot/commands|no own folder|no command folder of its own|\.github/prompts`.

No `.copilot/commands`, `.copilot/prompts`, or `.github/commands`. The negative is `command-files-round58.md:18`. `com.github.copilot/commands/` is named there as a plugin path (`:20-21`). `.github/prompts` in this corpus is the VS Code row (`command-files-round58.md:37`, S091) and `instruction-surface-census-round13.md:102` ("VS Code Copilot prompt files"). README `:96` says Copilot CLI loads Claude Code's folder.

## Issues (the surface the prior scout left closed)

Phrase search via `gh api search/issues`, `Fri Oct 23 08:27:34 AM UTC 2026`. GitHub's search ignores punctuation inside quotes, so totals are not exact-string counts. Bodies below were fetched and scanned.

`https://github.com/github/copilot-cli/issues/618` — closed `completed` `2026-03-05T15:09:25Z`. Issue JSON HTTP via `gh api`, 5436 bytes, sha256 `8db4a79395811ed90925056b984ce7674210e7b68809b71ef4a9ed1d7cc7bf2e`. Comments JSON 59159 bytes, sha256 `b8e46a90c477fa8361b82716eccce653f1c7403a25bbb2d68814d003ebb2cf2c`. Title, 10 words: `Feature Request: Support custom slash commands from .github/prompts directory`. The request is that the CLI does not recognize `.github/prompts/*.prompt.md`.

Collaborator EvanBoyle, comment 4005755203, `2026-03-05T15:09:25Z`, `author_association` COLLABORATOR. Extracted body 152 bytes, sha256 `733fced66ecfb5d614d5a14011a609e63f4a846feda931b2cf90be8eeca9b2ac`, one line. Second sentence only, 16 words; the first sentence (`Hey folks, the guidance here is to convert these into skills. `) omitted:

```
We do not plan on supporting prompt files given that they have been superseded by skills.
```

Comment 4014310549 (vandenberghev, `2026-03-06T21:42:09Z`), line 5, 9 words then a markdown link. Visible link text is 4 words, `cli supports prompt files`, target `https://docs.github.com/en/copilot/reference/customization-cheat-sheet#ide-and-surface-support`:

```
Ended up here because the docs wrongly state the
```

The current cheat-sheet source (above) marks that column `✗`. The file as of 2026-03-06 was not fetched, so whether the cell was `✓` that day is unresolved. It is not a current own folder.

Other fetched issues, same 08:27:54Z batch:

| Issue | State | What it is |
|---|---|---|
| #98 | open | Request to reuse prompt files. Comment 4847198932 (SqlBenjamin, `2026-06-30`) line 31 heading `What We Need`; line 35 contains the ASCII substrings `~/.copilot/prompts/` and `.github/prompts/` wrapped in U+00A0, as a proposed `/prompt` command, not as current behavior. |
| #4869 | open | `Add supports for reusable prompts stored as `.github/prompts/myprompt.prompt.md``. 0 comments. |
| #1113 | closed duplicate `2026-04-06` | Asks for `.github/commands/` or `.github/prompts/`. |
| #1004, #1334 | closed duplicate `2026-04-06` | Same request, pointed at IDE prompt files. |
| #3343 | open | Proposes `~/.copilot/commands/`. Body line 18 bytes are `A \~/.copilot/commands/\ directory where markdown files define machine-level slash commands.` (tildes backslash-escaped). 0 comments. Not a doc. |
| #942 | closed completed `2026-01-21` | Asks for `.github/prompts` in the CLI. EvanBoyle comment 3776057089, 7 words: `We shipped /review and /plan this week!` Built-in commands, not a user folder. |
| #1194 | open | Guesses completion should use `.github/prompts/`. |

tmarly on #1113, comment 3845863300, `2026-02-04T07:46:20Z`, extracted body sha256 `dfb2c7eb6fbbbb20076cce63df5cd606fd980edcdf4999f51cbabca2b95effbd`. First sentence, 17 words, double space after `working` kept:

```
On my side, it's working  (tested on 0.0.399 and 0.0.401), with the file in the directory `.claude/commands`.
```

That confirms the foreign folder on 0.0.399 and 0.0.401, and that a `.prompt.md` name had to lose the word `prompt`. It does not name an own folder.

## Discussions

`hasDiscussionsEnabled` true, `totalCount` 131. All 131 bodies scanned (`Fri Oct 23 08:30:11 AM UTC 2026`, saved JSON 111232 bytes, sha256 `3c3d477b9164e15f4dcd6b15f95e268728f358671b6a4ddf5627662280deca77`). All 72 comments scanned (`Fri Oct 23 08:32:00 AM UTC 2026`; no discussion had more than 50 comments). Exact counts for `.github/prompts`, `.copilot/commands`, `.copilot/prompts`, `.github/commands`, `.github/copilot/commands`, `.claude/commands`, `com.github.copilot/commands`: 0 in bodies and 0 in comments. `prompt files`: 0 in bodies.

GraphQL search totals (2, 9, 5, 7, 1) are punctuation-insensitive false positives. Release-note discussions #263 and #227 mention ordinary "prompts", not a path. #605 "Home directory" (REST 2326 bytes, sha256 `1fe52e634407e2a6072301cc45d186bf4c62bc275162f1b06eee2b7e121d1898`) asks for `GITHUB_COPILOT_HOME`. RyanHecht, `2025-12-08T15:52:41Z`, 16 words:

```
Copilot CLI respects the `XDG_CONFIG_HOME` environment variable, and falls back to `$HOME` if that's not present.
```

That is a home relocation, not a command folder. Current docs name `COPILOT_HOME` for the same directory (config-dir source line 59) and still list no `commands/` or `prompts/`.

## What does not overturn NOT ELIGIBLE

- `.github/prompts` — IDE pages, open feature requests, and a maintainer refusal. The cheat sheet's Copilot CLI cell is `✗`.
- `~/.copilot/prompts/` and `~/.copilot/commands/` — proposals on open issues #98 and #3343. Absent from changelog, docs source, and discussion text.
- `.claude/commands/` — still Claude Code's folder (changelog line 2932, command-reference source line 1345, a user's 0.0.399 test).
- `com.github.copilot/commands/` — plugin namespace, source line 171, already rejected in the lesson Gate.

## Unresolved

The copilot-cli program source, other than README (prior seat) and this changelog, was not opened. An undocumented load path in the binary would not be a documented folder. The cheat sheet blob of 2026-03-06 was not retrieved, so the "docs wrongly state" comment is unchecked against that day's bytes. Neither gap is a printed own folder on the surfaces this seat opened.
