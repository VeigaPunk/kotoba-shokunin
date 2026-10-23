Result: DONE — Cursor: ELIGIBLE .cursor/hooks.json

Cursor's own docs, on pinned host `cursor.com`, name `.cursor/hooks.json` as the project file that holds hook configuration: commands the client runs on lifecycle events. The same page prints many event identifiers. The token passes every C1 conjunct below. User-level `~/.cursor/hooks.json` is the same path after stripping one leading `~/` (not a second new-ground token). Not marked experimental, preview, or deprecated.

## Fetch

- URL: `https://cursor.com/docs/hooks.md` (`.md` variant tried first; final URL unchanged).
- Local `date -u` at fetch start (also `/fast/scratch/hyaku/kotoba-r59/CensusCursor/fetch-utc.txt`): `Fri 23 Oct 2026 09:03:03 AM UTC`.
- Response `Date` header: `Fri, 23 Oct 2026 09:02:56 GMT`. Status line: `HTTP/2 200`. `content-type: text/markdown; charset=utf-8`. `x-matched-path: /api/raw`.
- Bytes: 69145. sha256: `8436af768468590299c1beab9ea34bff8c5f1e5649ae244a989c28960dd2c88d`. Lines: 1507.
- Saved: `/fast/scratch/hyaku/kotoba-r59/CensusCursor/hooks.md` (headers: `hooks.md.headers`).
- Same URL without `.md` also returned HTTP 200, final URL `https://cursor.com/docs/hooks`, 1307361 bytes, sha256 `380c5a72c14ca5d72cfbc91f90bf7d285c2d2f1652588c4aa7dfcfe5dcdc8bd3`, saved as `hooks.html`. Quotes and line numbers below are from `hooks.md`, not the HTML.
- `https://docs.cursor.com/hooks` redirected to `https://cursor.com/docs` (homepage, not this page). `https://cursor.com/docs/agent/hooks.md` was HTTP 404.

Host `cursor.com` is pinned. Path `/docs/hooks.md` has no changelog, release, news, blog, or issue segment.

What the file is (line 3, verbatim): Hooks are custom scripts defined in `hooks.json`, spawned processes that run before or after stages of the agent loop. Line 50 says cloud agents run command-based hooks defined in `.cursor/hooks.json`.

## Candidate

Token as printed: `.cursor/hooks.json` (backtick span on line 50; also lines 98, 659, and inside longer spans on lines 112, 144, 648, 771).

Line 50 bytes:

```
Cloud agents run command-based hooks from your repository. If you have hooks defined in `.cursor/hooks.json` at the root of your project, cloud agents pick them up and run them during their work.
```

## Quote

Verbatim, no bytes stripped (the two backticks stay). One sentence, lines 50 of `hooks.md`. 24 words after removing those two backtick bytes (the command-file counter counts `quote.replace("`", "").split()`); 24 either way, because a backtick is not whitespace.

If you have hooks defined in `.cursor/hooks.json` at the root of your project, cloud agents pick them up and run them during their work.

Word 4 is `hooks`, outside the token span. Word 7 is `.cursor/hooks.json`. After the backticks are removed the token is bounded by spaces (left boundary; right character is not a letter, digit, `_`, or `-`).

## Events

Same page, under `### Hook events` (line 858). Each name is the heading text, byte-exact, and matches `^[A-Za-z][A-Za-z0-9_.:-]*$`.

| name | line |
|---|---|
| preToolUse | 860 (`#### preToolUse`) |
| postToolUse | 897 |
| postToolUseFailure | 936 |
| subagentStart | 970 |
| subagentStop | 1010 |
| beforeShellExecution | 1058 (`#### beforeShellExecution / beforeMCPExecution`) |
| beforeMCPExecution | 1058 |
| afterShellExecution | 1102 |
| afterMCPExecution | 1123 |
| afterFileEdit | 1147 |
| beforeReadFile | 1159 |
| beforeTabFileRead | 1196 |
| afterTabFileEdit | 1219 |
| beforeSubmitPrompt | 1255 |
| afterAgentResponse | 1283 |
| afterAgentThought | 1294 |
| stop | 1316 |
| sessionStart | 1338 |
| sessionEnd | 1372 |
| preCompact | 1404 |
| workspaceOpen | 1442 |

`afterFileEdit` is also a JSON key on line 150.

## C1 conjuncts

Grammar checked against `TOKEN_RE` and the segment rules in `verifiers/check_command_files.py` (`a975cbbf`), with the round-59 extra forbidden words `command`, `commands`, `prompt`, `prompts` from `plans/round-59.md` (the command-file counter itself still requires a command/prompt word in the final segment; that requirement is not in the C1 hook rule).

| conjunct | result |
|---|---|
| `TOKEN_RE` `^(~/|\./)?[A-Za-z0-9_.-]+(/[A-Za-z0-9_.*-]+)*/?$` | yes |
| after one leading `~/` or `./`, at least 2 segments | yes (`.cursor`, `hooks.json`; nothing to strip) |
| first segment starts with `.` | yes |
| no segment word (split on `-` `.` `_`, case-insensitive) in skill/skills/agent/agents/command/commands/prompt/prompts/rule/rules/plugin/plugins/extension/extensions | yes (words: `cursor`, `hooks`, `json`) |
| E7: no dot in a non-final segment except as its first character | yes (only non-final segment is `.cursor`) |
| no other client's marker (`claude`, `codex`, `vscode`, `copilot`, `gemini`, `opencode`) | yes (`cursor` is Cursor's own marker) |
| E5: not a token another client's row would lead with | yes, not observed (detail below) |
| quote 6–25 words, token case-sensitive at a segment boundary, `hook`/`hooks` outside the token | yes (24; line 50) |
| at least 2 distinct event identifiers on this page | yes (table above) |
| pinned host, not a changelog/release/news/blog/issue page | yes |
| file holds hook configuration (commands run on a lifecycle event) | yes (lines 3 and 50) |
| marked experimental / preview / deprecated | no. Case-insensitive search of `hooks.md` and `hooks.html` for `experimental`, `preview`, `deprecated`, `beta`, `alpha`: no matches |

## E5

No fetched page of another client contains the bytes `.cursor/hooks.json`.

| page | status | hits |
|---|---|---|
| `https://code.claude.com/docs/en/hooks.md` | 200, 274129 bytes | 0 |
| `https://developers.openai.com/codex/hooks.md` (final `https://learn.chatgpt.com/docs/hooks.md`) | 200, 47133 bytes | 0 |
| `https://geminicli.com/docs/hooks.md` | 200, 8341 bytes | 0 |
| `https://docs.github.com/en/copilot/reference/hooks-reference.md` | 200, 72175 bytes | 0 |
| `https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/use-hooks.md` | 200, 9310 bytes | 0 |
| `https://opencode.ai/docs/plugins.md` | 200, 9357 bytes | 0 |
| `https://opencode.ai/docs/config.md` | 200, 26060 bytes | 0 |

Guessed hooks URLs that 404'd, so those paths were not a source: `code.visualstudio.com/docs/copilot/customization/hooks.md`, `code.visualstudio.com/docs/copilot/chat/hooks.md`, `code.visualstudio.com/docs/copilot/overview.md`, `opencode.ai/docs/hooks.md`. A web search for the exact token outside `cursor.com` returned third-party Cursor repos and a blog, not another client's pinned docs. Lane `corpus/` has no match. Base tree count is 0 (below). [INFERENCE] A non-Cursor row that led with this token would also fail that client's foreign-name guard, because the token contains `cursor`. Sibling census reports were not read.

## New-ground pre-count

```
git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin grep -ilF '.cursor/hooks.json' a975cbbf00534443c49bf02e29c813a3db0bf0f8 -- . ':!.ufo' | wc -l
```

Output: `0`. The same command for `.cursor/hooks` (the form named in the plan draft) also printed `0`.

## Other printed paths (not the lead token)

| printed token | well-formed under the hook rule? | why it is not the lead |
|---|---|---|
| `~/.cursor/hooks.json` (lines 102, 112, 116, 651, 669, 789) | yes; normalises to `.cursor/hooks.json` | same token after stripping `~/`. A quote that also works: line 102, `User-level hooks (`~/.cursor/hooks.json`) are not available in cloud agents.` (9 words after dropping the two backticks; `(` is a left boundary and `)` is a legal right edge) |
| `hooks.json` alone (line 3) | no | one segment; does not start with `.` |
| `` `<project>/.cursor/hooks.json` ``, `` `<project-root>/.cursor/hooks.json` `` | no | `<` `>` fail `TOKEN_RE`; first segment is not dot-led |
| `/etc/cursor/hooks.json`, `/Library/Application Support/Cursor/hooks.json`, `C:\\ProgramData\\Cursor\\hooks.json` | no | leading `/` or spaces or backslashes fail `TOKEN_RE`; first segment is not dot-led |
| `.cursor/hooks/` and `~/.cursor/hooks/` | grammar yes (normalise `.cursor/hooks`) | page calls this the hook-script directory (lines 127, 157, 790), not the config file. Not a second recommended row token |
| `.cursor/hooks/format.sh` | grammar yes | example script, not the config location |

## Tools

No package installed.
