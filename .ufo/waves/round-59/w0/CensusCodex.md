Result: DONE — Codex: ELIGIBLE ~/.codex/hooks.json

Codex's own hooks page names `~/.codex/hooks.json` as a file Codex loads for lifecycle hooks (scripts or MCP tools run on events such as `PreToolUse` and `SessionStart`). The token passes every C1 conjunct below. Base-tree pre-count is 0.

## Fetch

Pinned host `learn.chatgpt.com` (also reached by a 308 from pinned `developers.openai.com`).

- URL fetched: `https://learn.chatgpt.com/docs/hooks.md`
- `date -u` at fetch: `Fri 23 Oct 2026 09:03:06 AM UTC`
- HTTP 200, `content-type: text/markdown; charset=utf-8`, final URL `https://learn.chatgpt.com/docs/hooks.md`
- bytes 47133
- sha256 `57166ef03e7059732dd90925d5c42dd4d187eb2625d66cc154d0fbd2edb65f92`
- saved: `/fast/scratch/hyaku/kotoba-r59/CensusCodex/learn.chatgpt.com_docs_hooks.md.body`
- User-Agent: `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36`
- Not a changelog, release, news, blog, or issue URL (`/docs/hooks.md`).

Same bytes via the other pinned host (followed with `-L` in the same batch, identical sha256, saved as `developers.openai.com_codex_hooks.md.body`):

- Request `https://developers.openai.com/codex/hooks.md` to `url_effective=https://learn.chatgpt.com/docs/hooks.md`, HTTP 200, 47133 bytes, sha256 `57166ef03e7059732dd90925d5c42dd4d187eb2625d66cc154d0fbd2edb65f92`, `date -u` `Fri 23 Oct 2026 09:03:06 AM UTC`.
- Redirect observed without `-L` at `Fri 23 Oct 2026 09:04:38 AM UTC`: `HTTP/2 308`, `location: https://learn.chatgpt.com/docs/hooks.md`, response `date: Fri, 23 Oct 2026 09:04:38 GMT`.

Page opens `# Hooks` and states hooks run commands on lifecycle events (lines 5-6, 21-28, 30-47 of the saved markdown).

## Lead token

Printed text: `~/.codex/hooks.json` (backtick span on line 44).

Section heading line 30: `## Where Codex looks for hooks`. Lines 42-47 name four locations; the first bullet is that token.

Quote (contiguous slice of the saved bytes, offset 2425, no bytes stripped; newlines kept). 13 words after deleting U+0060 backticks and splitting on whitespace (the command-file counter's count):

```
- `~/.codex/hooks.json`
- `~/.codex/config.toml`
- `<repo>/.codex/hooks.json`
- `<repo>/.codex/config.toml`

If more than one hook
```

The token sits at a path-segment boundary (preceded by a space once backticks are removed). The pattern hook/hooks matches outside that span: `hooks` inside the `<repo>/.codex/hooks.json` bullet and the word `hook` in `one hook`.

Events, byte-exact, identifier regex `^[A-Za-z][A-Za-z0-9_.:-]*$`, all on this page:

| Name | Line |
|---|---|
| PreToolUse | 25 |
| PermissionRequest | 25 |
| PostToolUse | 25 |
| PreCompact | 25 |
| PostCompact | 25 |
| UserPromptSubmit | 25 |
| SubagentStop | 25 |
| Stop | 25 |
| Interrupt | 26 |
| SessionStart | 27 |
| SubagentStart | 27 |
| SessionEnd | 28 |

## C1 conjuncts for ~/.codex/hooks.json

Path regex used: check_command_files.py TOKEN_RE = `^(~/|\./)?[A-Za-z0-9_.-]+(/[A-Za-z0-9_.*-]+)*/?$`. Segment split on `-`, `.`, `_`. Own marker `codex` is not foreign.

| Conjunct | Verdict |
|---|---|
| Own docs, pinned host, not changelog/release/news/blog/issue | yes |
| File holds hook configuration (commands/code run on a lifecycle event) | yes — hooks.json is a form Codex discovers hooks in (lines 32-44); events above |
| TOKEN_RE | yes |
| After one leading `~/`, at least 2 segments (`.codex` / `hooks.json`) | yes |
| First segment starts with `.` | yes |
| No segment word in {skill, skills, agent, agents, command, commands, prompt, prompts, rule, rules, plugin, plugins, extension, extensions} | yes — words are codex, hooks, json |
| E7: no dot in a non-final segment except as its first character | yes — `.codex` |
| No other client's marker (claude, vscode, copilot, gemini, cursor, opencode) | yes — only Codex's own marker codex |
| E5: not a token another client's row would lead with | yes (not shared). This seat did not open the other six clients' pages. A web search for the exact token found third-party writeups that name it as Codex's file, not another client's pinned-host docs leading with it. [INFERENCE] no sibling row leads with this token; the foreign-name guard would also reject it for every client except Codex |
| Quote 6-25 words, token case-sensitive at a segment boundary, hook/hooks outside the token | yes — 13 words, slice above |
| At least 2 event identifiers on this page | yes — twelve, table above |
| Marked experimental / preview / deprecated | no. Line 314: Hooks are enabled by default. Lines 321-322: `codex_hooks` still works as a deprecated alias of the feature key, not a deprecation of hooks |

## Other printed paths (not the lead)

| Printed token | Line | Why not the lead |
|---|---|---|
| `~/.codex/config.toml` | 45 | Also passes the same conjuncts (inline `[hooks]` in config.toml, lines 35 and 45). General config file, not the dedicated hook file. Different token, so it does not trip E5 against the lead |
| `<repo>/.codex/hooks.json` | 46 | Fails TOKEN_RE (`<` `>` outside the grammar) and the first segment `<repo>` does not start with `.` |
| `hooks.json` | 34 | One segment |
| `hooks/hooks.json` | 38 | First segment `hooks` does not start with `.` |
| `./hooks/hooks.json` | 389 | After stripping `./`, first segment `hooks` does not start with `.` |
| `.codex-plugin/plugin.json` | 382 | Segment word `plugin` (split on `-`) |

## New-ground pre-count

Token with one leading `~/` removed: `.codex/hooks.json`.

```
git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin grep -ilF '.codex/hooks.json' a975cbbf00534443c49bf02e29c813a3db0bf0f8 -- . ':!.ufo' | wc -l
```

Output: `0` (pipeline exit 0). `git grep` itself exited 1 (no match). Observed `Fri 23 Oct 2026 09:04:09 AM UTC` and rechecked in the same session. 0 files at `a975cbbf00534443c49bf02e29c813a3db0bf0f8` outside `.ufo`.

No tools installed. No lane files edited except this report.
