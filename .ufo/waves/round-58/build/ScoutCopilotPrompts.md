Result: HOLDS — Copilot CLI docs, README, and changelog still print no own command or prompt-file folder; the only command-file path is `.claude/commands/` (Claude Code), and `.github/prompts/` is IDE-only.

Scout seat ScoutCopilotPrompts. Read-only. No tools installed or updated. No lane code executed. Fetched bytes kept under `/fast/scratch/hyaku/kotoba-r58/ScoutCopilotPrompts/` (not lane content). This attacks the W0 census negative (plan `plans/round-58.md` Copilot CLI row: NOT ELIGIBLE). The negative holds. No new SOURCES page (S092 stays unused): nothing here is an own C1 token.

## Sweep

Pinned hosts only. `date -u` lines are the clock immediately before each curl batch.

CLI docs source tree (Q30): GitHub contents API listed every markdown file under `github/docs` `main` at `content/copilot/reference/copilot-cli-reference/`, `content/copilot/how-tos/copilot-cli/`, and the three child dirs `customize-copilot/`, `use-copilot-cli/`, `set-up-copilot-cli/`, `automate-copilot-cli/`. Batch `Fri 23 Oct 2026 08:09:25 AM UTC`. 54 files, each HTTP 200, 679512 bytes total. Raw bodies: `https://raw.githubusercontent.com/github/docs/main/<path>`. Per-file status, size, and sha256 are in the scratch manifest `docs-src-manifest.tsv`. A case-sensitive count over those 54 files plus the README and changelog bodies:

| Needle | Hits |
|---|---|
| `.github/prompts` | 0 |
| `.github/commands` | 0 |
| `.copilot/prompts` | 0 |
| `prompt file` / `prompt files` | 0 |
| `custom command` / `custom commands` | 0 |
| `.claude/commands` | 3 (command reference, plugin reference, changelog) |
| `com.github.copilot/commands` | 1 (plugin reference) |
| `commands/` | those same three files only |

The one `.copilot/commands` substring hit is inside `com.github.copilot/commands`, not a `~/.copilot/commands` path. [INFERENCE] No other spelling of an own `~/.copilot/...` command or prompt directory appears in that tree.

Lane corpus grep for `.github/prompts`, `~/.copilot/commands`, `.copilot/prompts`, `com.github.copilot/commands`: the only command-file hit is `corpus/knowledge/instruction-surface-census-round13.md:102`, which attributes `.github/prompts/` to VS Code Copilot prompt files, not to Copilot CLI.

Not opened (assignment bound): copilot-cli source other than README and changelog, and GitHub issues. Absence below is documentation absence, not a binary claim.

## Candidate A — `.claude/commands/` — CLI scope, not own

URL: `https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference.md`

Batch `Fri 23 Oct 2026 08:08:29 AM UTC`. HTTP 200. 461944 bytes. sha256 `c61997efd7c939324e1f1b846fcb9ed420e5bbfd5eb5319531c6e6210025b5c9`. Same bytes as the W0 census fetch.

Quote, rendered line 1334, no bytes stripped, 13 words:

```
Commands are an alternative to skills stored as individual `.md` files in `.claude/commands/`.
```

Section heading on line 1343 of the docs source, and the same sentence at source line 1345 (`content/copilot/reference/copilot-cli-reference/cli-command-reference.md`, raw HTTP 200, 177073 bytes, sha256 `48de33ea09a3e532f2355c45886d6e17aa37090fe9599cd4240a1d04f035c7f2`). CLI page. The token carries Claude Code's marker `claude`. Not an own folder. Same path the census already rejected under E5.

Changelog corroboration only (changelog URLs never count as a C1 source). URL: `https://raw.githubusercontent.com/github/copilot-cli/main/changelog.md`. Same 08:08:29Z batch. HTTP 200. 289859 bytes. sha256 `c4b793bd6555bf699c1f6ef61fb9052e6400df8f475c97fdae25ba5084531dfb`. Line 2932, under `## 0.0.399 - 2026-01-29`, 9 words, no bytes stripped:

```
Support `.claude/commands/` single-file commands as simpler alternative to skills
```

Plugin-reference diagram repeats the same path, not a second folder. URL: `https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference.md`. Same batch. HTTP 200. 47200 bytes. sha256 `d0d362cc5aa2ef84775145e499596c7e6529531c7b29972ae29f547b5da220d0`. Line 456, inside a fenced diagram: `--- then commands (.claude/commands/), skills override commands ---`.

## Candidate B — `com.github.copilot/commands/` — CLI scope, plugin namespace, not a dot-led user folder

Same plugin-reference fetch (200, 47200 bytes, sha256 above).

Token as printed, rendered line 159, table cell: `com.github.copilot/commands/`. The row is `| Slash commands | `com.github.copilot/commands/`        |`. Three words once the pipes are ignored, so it is not a 6-word quote. Prose on line 154 names only the parent (10 words, no bytes stripped):

```
Copilot CLI reads its client-specific components from the `com.github.copilot` directory:
```

Line 164: `These locations apply only to Agent Plugins 1.0 plugins.`

Creating-a-plugin page, same batch, HTTP 200, 7711 bytes, sha256 `c0642867c28a816b5a1210a3f51d66efd2f37cd09ae950228a3c517cf5cb7d64`, URL `https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-creating.md`. Line 21, contiguous 19-word substring, no bytes stripped, names `commands` but not the `commands/` path:

```
Copilot-specific components such as agents, commands, rules, hooks, and LSP servers come from the `com.github.copilot` directory in the plugin.
```

Line 69 of that page names `com.github.copilot/agents/` and `com.github.copilot/hooks/hooks.json`, not `commands/`.

Legacy manifest field, plugin reference line 213: `` `commands` `` default cell is `—`, description `Path(s) to command directories.` No default directory is printed.

CLI scope. Own marker (`copilot`), but the first segment does not start with `.`, and `com.github.copilot` has dots after its first character. Fails the C1 leading-dot rule and E7. Does not overturn NOT ELIGIBLE.

## Candidate C — `~/.copilot/skills` and the `~/.copilot` inventory — CLI scope, not command files

URL: `https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills.md`. Same 08:08:29Z batch. HTTP 200. 10057 bytes. sha256 `989af4981773349a74feaebfe98cdac9895b394707d201545ba55c8f9f4131a0`. Line 15, 17 words, no bytes stripped:

```
For **personal skills**, shared across projects, create a `~/.copilot/skills` or `~/.agents/skills` directory in your local home directory.
```

Line 13 prints `.github/skills`, `.claude/skills`, `.agents/skills`. Final segment is `skills` (banned). Not a command or prompt folder.

Config directory page: `https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-config-dir-reference.md`. Same batch. HTTP 200. 166811 bytes. sha256 `8be36090c19a7e284d4137f03db150927f3f215fb3b21ddfc9d87c614bec21b0`. Line 11, 8 words:

```
The `~/.copilot` directory contains the following top-level items.
```

Path column, lines 15–35, observed: `agents/`, `config.json`, `copilot-instructions.md`, `extensions/`, `hooks/`, `ide/`, `installed-plugins/`, `instructions/`, `logs/`, `lsp-config.json`, `mcp-config.json`, `mcp-oauth-config/`, `mcp-secrets/`, `permissions-config.json`, `plugin-data/`, `providers.json`, `session-state/`, `command-history-state/`, `session-store.db`, `settings.json`, `skills/`. No `commands/` and no `prompts/`. The docs-source copy of this page (74754 bytes, sha256 `78eb9462dcaf3171f29da007e10981632da3d4d323eb4994ad416896a940a54a`) is one of the 54 files in the zero-hit count for `commands/` and `prompts/`.

`command-history-state/` is CLI state, not a user-written prompt folder. Heading line 324. Line 326, 16 whitespace-separated words, no bytes stripped:

```
Contains command history data used for reverse search (<kbd>Ctrl</kbd>+<kbd>R</kbd>) and history navigation in the interactive interface.
```

One segment, not dot-led, and the page says the directory is managed automatically.

## Candidate D — SDK "custom slash commands" — CLI scope, not a folder

Changelog line 2306, under `## 1.0.10 - 2026-03-20`, same changelog fetch. 13 words, no bytes stripped:

```
SDK clients can register custom slash commands when starting or joining a session
```

No path. Registration is programmatic. The phrase `custom command` does not occur; this line matched only as prose in a manual read, not as a folder. Built-in `/model`, `/diff`, and the rest of the command-reference slash list are shipped commands, not user files.

## Candidate E — `.github/prompts/` — IDE scope, absent from CLI pages

Zero hits in the 54-file CLI tree, the README, and the changelog (table above).

Not a Copilot CLI page. URL: `https://docs.github.com/en/copilot/concepts/prompting-and-context/prompt-files.md`. Batch `Fri 23 Oct 2026 08:10:29 AM UTC`. HTTP 200. 2316 bytes. sha256 `73b58a8dd61fd374eeaa508cbb5a8dbe1b63f590686adbcbef1fc6d750cfbd20`. The body contains `.github/prompts` once and `Copilot CLI` zero times. Line 5, 13 words, no bytes stripped:

```
Repository prompt files use the `.prompt.md` extension and are typically stored in `.github/prompts/`.
```

Line 11, 13 words, no bytes stripped:

```
Prompt files are available in Visual Studio Code, Visual Studio, JetBrains IDEs, and Xcode.
```

Tutorial, also not under `copilot-cli`. URL: `https://docs.github.com/en/copilot/tutorials/customization-library/prompt-files/your-first-prompt-file.md`. Batch `Fri 23 Oct 2026 08:10:17 AM UTC`. HTTP 200. 3039 bytes. sha256 `117468ccb3abe5d07ae8f76a309f291b0fb93dae6d06de789feb9b90aa87b0ed`. Line 47: `Save the prompt file above as `explain-code.prompt.md` in your `.github/prompts` folder.` Line 7 note, second sentence, 13 words, no bytes stripped:

```
Prompt files are only available in VS Code, Visual Studio, and JetBrains IDEs.
```

That sentence does not name Xcode; the concepts page does. Neither names Copilot CLI. Index `https://docs.github.com/en/copilot/tutorials/customization-library/prompt-files.md`, same 08:10:17Z batch, HTTP 200, 1073 bytes, sha256 `c31554c2e174de26fdb00892c7bba02334cb036bbe867ef862132143c0836876`, is a link list and prints no path. A how-tos URL `https://docs.github.com/en/copilot/how-tos/customization-library/prompt-files.md` returned HTTP 404, 502 bytes, sha256 `979615bad4719ae23bf76385ee60de8b1b05c785ce74497dee80ecb54c69c522`.

`https://docs.github.com/en/copilot/concepts/customizations/comparing-customizations.md` (not a CLI-only page; it does name Copilot CLI for instructions, skills, agents, hooks, plugins, and extensions). Batch 08:10:17Z. HTTP 200. 17525 bytes. sha256 `b1c562f583a475e7bd61ac08816d480025e681fe7db73ced498390d8c6078ed9`. Zero `.github/prompts`, zero `prompt file`, zero `.claude/commands`.

## README

URL: `https://raw.githubusercontent.com/github/copilot-cli/main/README.md`. Batch 08:08:29Z. HTTP 200. 7740 bytes. sha256 `33657f2e7383f2167b47d5f8c549a6071905a5c93d5d67d17e5c5399f126f07b`. Title line 1: `# GitHub Copilot CLI`. Grep for `commands/`, `prompts/`, `prompt file`, `custom command`, `.claude/commands`: no matches. The only customization paths in backtick spans are `~/.copilot/lsp-config.json` (line 160) and `.github/lsp.json` (line 163).

## Unresolved

Whether the copilot-cli program, outside README and changelog, loads some undocumented directory was not checked. Issues on github.com/github/copilot-cli were not fetched. Neither gap is a printed own folder on the assigned doc surfaces.
