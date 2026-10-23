Result: DONE — Copilot CLI: NOT ELIGIBLE (only custom command-file folder is `.claude/commands/`, which carries Claude Code's marker and is Claude Code's path; `com.github.copilot/commands/` fails the leading-dot rule)

Census seat CensusCopilotCLI. Read-only. No tools installed or updated. No lane code executed. Fetched bytes kept under `/tmp/census-copilot-cli/` (not lane content).

## Verdict

Copilot CLI's own pages do state a folder where a user writes custom command files: `.claude/commands/`. That token fails the foreign-name guard (`claude` is Claude Code's marker) and is the same normalised path as Claude Code's eligible row, so E5 would disqualify both rows if Copilot CLI used it. The plugin slash-command directory `com.github.copilot/commands/` fails the first-segment-starts-with-`.` conjunct and the non-final-dot conjunct. Skill directories are the recommended reusable-prompt surface and fail the `skills` segment ban. No other printed path passes every C1 conjunct.

## Candidate A — `.claude/commands/`

Pinned host `docs.github.com`. Not a changelog, release, news, or blog URL.

- URL: `https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference.md`
- `date -u` immediately before the curl batch that saved this body: `Fri 23 Oct 2026 07:39:09 AM UTC`
- Fetch: `curl -sSL -o <body> -w "%{http_code} %{size_download}"`, exit 0. HTTP 200. 461944 bytes.
- sha256: `c61997efd7c939324e1f1b846fcb9ed420e5bbfd5eb5319531c6e6210025b5c9`
- Token as printed, line 1334, inside backticks: `.claude/commands/`
- Section heading on that line's subsection (line 1332): `### Commands (alternative skill format)`

Quote, line 1334, no bytes stripped. Contiguous substring of the fetched line. 13 whitespace-separated words (backticks left in):

```
Commands are an alternative to skills stored as individual `.md` files in `.claude/commands/`.
```

The token `.claude/commands/` sits at the end of that span (the following `.` is the sentence period, outside the token). Outside the token, `Commands` matches `(?i)\bcommands?\b`.

The same line continues, still on line 1334: "The command name is derived from the filename." The next sentence says command files use a simplified format and that no name field is required. Same fact, not a second location.

| Conjunct | Verdict |
|---|---|
| Own documentation on a pinned host | YES. `docs.github.com` |
| Folder or file pattern for a user-written reusable prompt / custom slash-command file | YES. Individual `.md` files in `.claude/commands/`; command name from the filename; called command files |
| v2 `TOKEN_RE` (`check_plugin_manifests.py:258`) | YES. `.claude/commands/` full-matches `^(~/|\./)?[A-Za-z0-9_.-]+(/[A-Za-z0-9_.*-]+)*/?$` |
| After one leading `~/` or `./`, ≥ 2 path segments | YES. Nothing to strip. Non-empty segments `.claude` and `commands` |
| First segment starts with `.` | YES. `.claude` |
| Final non-empty segment, split on `-` `.` `_`, holds `command` / `commands` / `prompt` / `prompts` | YES. `commands` |
| No segment word is skill, skills, agent, agents, rule, rules, plugin, plugins, extension, extensions | YES. Words are `claude`, `commands` |
| No dot inside a non-final segment except as its first character | YES. The only dot in `.claude` is the first character |
| No other client's marker (`claude`, `codex`, `vscode`, `copilot`, `gemini`, `cursor`, `opencode`) | NO. Lower-cased text contains `claude`. `foreign_marker` (`check_plugin_manifests.py:561-567`) returns Claude Code |
| Not the same path as another client's row | NO. Normalise (strip one trailing `/`) is `.claude/commands`, the token CensusClaudeCode recorded as ELIGIBLE from `https://code.claude.com/docs/en/slash-commands.md`. This seat did not re-fetch that page. E5 disqualifies both rows |
| Quote 6–25 words, token case-sensitive, command(s)/prompt(s) outside the token | YES. 13 words, line 1334, as quoted above |
| Source is not changelog / release / news / blog | YES |

Deprecated / legacy: the word `deprecated` does not appear on line 1332 or 1334. The section calls commands an alternative skill format and says they have lower priority than skills with the same name. Not labelled withdrawn.

The same path is repeated, still not a second token, in the plugin reference loading diagram.

- URL: `https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference.md`
- Same curl batch, `Fri 23 Oct 2026 07:39:09 AM UTC`. HTTP 200. 47200 bytes.
- sha256: `d0d362cc5aa2ef84775145e499596c7e6529531c7b29972ae29f547b5da220d0`
- Line 456, inside a fenced diagram: `--- then commands (.claude/commands/), skills override commands ---`

Changelog corroboration only (changelog URLs never count). `https://raw.githubusercontent.com/github/copilot-cli/main/changelog.md`, batch `Fri 23 Oct 2026 07:40:05 AM UTC`, HTTP 200, 289859 bytes, sha256 `c4b793bd6555bf699c1f6ef61fb9052e6400df8f475c97fdae25ba5084531dfb`. Line 2932, under `## 0.0.399 - 2026-01-29`: `- Support `.claude/commands/` single-file commands as simpler alternative to skills`. Grep of that file for `.github/prompts`, `.copilot/commands`, `.github/commands`, `prompt files`, and `custom commands`: no matches.

## Candidate B — `com.github.copilot/commands/`

Same plugin-reference fetch as above (200, 47200 bytes, sha256 `d0d362cc5aa2ef84775145e499596c7e6529531c7b29972ae29f547b5da220d0`, `Fri 23 Oct 2026 07:39:09 AM UTC`).

Token as printed, line 159, table cell: `com.github.copilot/commands/`

Prose on line 154 names only the parent: `Copilot CLI reads its client-specific components from the `com.github.copilot` directory:`. Line 152 says Agent Plugins 1.0 does not define portable commands and that client-specific files live in that namespace. Line 164: `These locations apply only to Agent Plugins 1.0 plugins.`

No contiguous no-shaping 6–25-word span on one line contains the full token. The table row is `| Slash commands | `com.github.copilot/commands/`        |` (three whitespace-separated words once the pipes are ignored). Not used as a backing quote.

| Conjunct | Verdict |
|---|---|
| Own documentation on a pinned host | YES. `docs.github.com` |
| Folder where a user writes slash-command files | YES, inside an Agent Plugins 1.0 plugin (`Slash commands` row). Legacy `commands` manifest field (line 213) has default `—` and names no directory |
| v2 `TOKEN_RE` | YES. Dots are allowed inside a segment by `TOKEN_RE` |
| After one leading `~/` or `./`, ≥ 2 path segments | YES. `com.github.copilot` and `commands` |
| First segment starts with `.` | NO. `com.github.copilot` |
| Final non-empty segment holds command/commands/prompt/prompts | YES. `commands` |
| No banned segment word | YES. Split words are `com`, `github`, `copilot`, `commands` |
| No dot inside a non-final segment except as its first character | NO. `com.github.copilot` has dots after the first character (v2 E7, `check_plugin_manifests.py:553`) |
| No other client's marker | YES. `copilot` is this client's own marker. `github` is not a client marker |
| Not the same path as another client's row | Not closed. This seat did not fetch the other six clients' pages for this token. [INFERENCE] VS Code's Agent Plugins docs also talk about a `com.github.copilot` namespace (corpus `plugin-manifests-round57.md`); whether they print this exact `commands/` path was not re-fetched here |
| Quote 6–25 words containing the token | NO, on the fetched page, without shaping |
| Not changelog / release / news / blog | YES |

Not marked deprecated. Line 164 limits the table to Agent Plugins 1.0; legacy plugins use manifest path fields instead.

## Candidates that are not command-file rows

Skills are how Copilot CLI documents a reusable prompt the user invokes with a slash name. Every printed skill directory fails the `skills` ban and the final-segment word test.

`https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills.md`, batch `Fri 23 Oct 2026 07:38:01 AM UTC`, HTTP 200, 10057 bytes, sha256 `989af4981773349a74feaebfe98cdac9895b394707d201545ba55c8f9f4131a0`. Line 13 prints `.github/skills`, `.claude/skills`, `.agents/skills`. Line 15 prints `~/.copilot/skills` and `~/.agents/skills`. Line 125 tells the user to include the skill name preceded by a forward slash. The same five directories are the skill-location table in the command reference, lines 1286–1291.

`https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-config-dir-reference.md`, batch `Fri 23 Oct 2026 07:40:05 AM UTC`, HTTP 200, 166811 bytes, sha256 `8be36090c19a7e284d4137f03db150927f3f215fb3b21ddfc9d87c614bec21b0`. The `~/.copilot` top-level table (lines 13–35) lists `agents/`, `skills/`, `instructions/`, `hooks/`, `extensions/`, and not `commands/` or `prompts/`. A count of the substrings `commands/` and `prompts/` in that file is 0.

Custom instructions (`.github/copilot-instructions.md`, `.github/instructions/**/*.instructions.md`, `$HOME/.copilot/copilot-instructions.md`, `$HOME/.copilot/instructions/**/*.instructions.md`) are always-on context, not a slash-command file. Final segments do not hold command/prompt. Page: `https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md`, same 07:38:01Z batch, HTTP 200, 8730 bytes, sha256 `00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980`, table lines 15–18.

Custom agents (`.github/agents/`, `~/.copilot/agents/`) fail the `agents` ban. `https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli.md`, batch `Fri 23 Oct 2026 07:39:09 AM UTC`, HTTP 200, 8379 bytes, sha256 `506783b43d77536f2771dd5670225a47cefa70365fb54f64316b2fed96ae34f2`, lines 25 and 27.

Extensions add slash commands as Node.js code, not as prompt files. `https://docs.github.com/en/copilot/tutorials/create-an-extension.md`, batch `Fri 23 Oct 2026 07:40:05 AM UTC`, HTTP 200, 21012 bytes, sha256 `6836b5a1b215a4a0a576a41fd458670186fc5055bfbb66178f5f5c7f7f43313d`. The user-level directory name in the config reference is `extensions/`, which is a banned segment and has no command/prompt word.

## Other fetches (no eligible token)

| URL | date -u batch | HTTP | bytes | sha256 |
|---|---|---|---|---|
| `https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/overview.md` | `Fri 23 Oct 2026 07:38:01 AM UTC` | 200 | 4304 | `38f2e097044641c32451491df4bbe4b7e232969fe50558aa3bb4fda2ac79189b` |
| `https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-creating.md` | same | 200 | 7711 | `c0642867c28a816b5a1210a3f51d66efd2f37cd09ae950228a3c517cf5cb7d64` |
| `https://docs.github.com/en/copilot/concepts/customizations/comparing-customizations.md` | `Fri 23 Oct 2026 07:39:09 AM UTC` | 200 | 17525 | `b1c562f583a475e7bd61ac08816d480025e681fe7db73ced498390d8c6078ed9` |
| `https://docs.github.com/en/copilot/reference/copilot-cli-reference.md` | same | 200 | 1021 | `d9c707cc59fe9a145646d0dbc8a63a5d9ecb9419f434781e3f0a45b433ff6b90` |
| `https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/overview.md` | `Fri 23 Oct 2026 07:40:05 AM UTC` | 200 | 20619 | `3d7922046390c5277e88a09c1f392f79e01f452bdf579193378472d466a9f7aa` |
| `https://docs.github.com/en/copilot/reference/custom-instructions-support.md` | same | 200 | 14612 | `90150f5a25f493640b9a52da6ac0a363ece8ece13429bd2c6c4e5ebb0c44e814` |
| `https://raw.githubusercontent.com/github/copilot-cli/main/README.md` | same | 200 | 7740 | `33657f2e7383f2167b47d5f8c549a6071905a5c93d5d67d17e5c5399f126f07b` |
| `https://docs.github.com/en/copilot/concepts/agents/about-agent-skills.md` | `Fri 23 Oct 2026 07:38:01 AM UTC` | 404 | 502 | `979615bad4719ae23bf76385ee60de8b1b05c785ce74497dee80ecb54c69c522` |
| `https://docs.github.com/en/copilot/concepts/agents/about-plugins.md` | `Fri 23 Oct 2026 07:39:09 AM UTC` | 404 | 502 | same 404 body sha |

The `.md` miss for agent skills was retried without the suffix: `https://docs.github.com/en/copilot/concepts/agents/about-agent-skills`, batch `Fri 23 Oct 2026 07:40:05 AM UTC`, HTTP 200, 566002 bytes of HTML (`<!DOCTYPE html>`), sha256 `7198da75109d1983e8d7976c6062ce1ed14b1cf1e76dea94e94d54c0b0016b6c`. Extracted text names project skills in `.github/skills`, `.claude/skills`, or `.agents/skills`. No `commands/` or `prompts/` path in that extract.

Backtick spans in the command-reference body that contain `command`, `prompt`, `skill`, `.github`, `.copilot`, `.claude`, `.agents`, or `slash` and look like paths do not include `.github/prompts`, `.copilot/commands`, or `~/.copilot/commands`. The command-file span in that set is `.claude/commands/`.

## Corpus

`grep` for `.claude/commands` under `/home/vgpnk/Projects/shokunin/kotoba-shokunin` hits the round-58 plan, the round-56 Claude changelog scout, and `CensusClaudeCode.md`. It does not hit a Copilot CLI knowledge row that prints a different command-file folder. `corpus/knowledge/instruction-surface-census-round13.md:102` attributes `.github/prompts/` to VS Code Copilot prompt files, not to Copilot CLI's own docs.

## Unresolved

Whether any of the other five clients (besides Claude Code) also print `.claude/commands/` was not fetched here. Claude Code does, which is enough for E5 on candidate A. Whether VS Code prints the exact plugin token `com.github.copilot/commands/` was not re-fetched; candidate B is already ineligible on the leading-dot and non-final-dot conjuncts.
