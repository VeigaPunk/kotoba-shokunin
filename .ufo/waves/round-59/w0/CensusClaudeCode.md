Result: DONE — Claude Code: ELIGIBLE `.claude/settings.json`

Census seat CensusClaudeCode. Client: Claude Code. No lane files edited. No tools installed. No model calls.

## Candidate

Token (printed): `.claude/settings.json`

That file is where Claude Code's own hooks reference says project hooks are defined. Hook locations table, same page: user `~/.claude/settings.json`, project `.claude/settings.json`, local `.claude/settings.local.json`. `~/.claude/settings.json` normalises (strip one leading `~/`) to the same token, so it is not a second row. Plugin `hooks/hooks.json` is named but its first segment does not start with `.`, so it is not the row token. `.claude/hooks/` is an example directory for scripts the settings file points at, not the configuration location the Hook locations table names.

## Fetch

- URL: https://code.claude.com/docs/en/hooks.md (curl -sSL, browser UA; effective URL identical; pinned host code.claude.com)
- date -u immediately before the fetch: Fri 23 Oct 2026 09:02:19 AM UTC
- HTTP status: 200 (content-type: text/markdown; charset=utf-8; response date: Fri, 23 Oct 2026 09:02:20 GMT)
- Byte count: 274129 (curl size_download and wc -c agree)
- sha256: c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8
- Saved bytes: /fast/scratch/hyaku/kotoba-r59/CensusClaudeCode/hooks.md
- Headers: /fast/scratch/hyaku/kotoba-r59/CensusClaudeCode/hooks.md.headers
- Not a changelog, release, news, blog, or issue page. Path is /docs/en/hooks.md.

## Quote

Line 910 of the saved bytes, verbatim (no bytes stripped). 21 whitespace-separated words with or without the four backtick bytes (U+0060) that wrap PreToolUse and the token:

This `PreToolUse` hook in `.claude/settings.json` runs a project script before each Bash command, and blocks the command if the script fails:

Token `.claude/settings.json` is case-sensitive. Left neighbour is a space (after the backtick is removed) or a backtick (if kept); both are path-segment boundaries. Right neighbour is a space or a backtick, not a letter, digit, `_`, or `-`. The word hook sits outside the token (hooks? word match).

## Events (same page, byte-exact)

| Line | Name |
|---|---|
| 33 | SessionStart |
| 37 | PreToolUse |
| 40 | PostToolUse |
| 65 | SessionEnd |

Each is a table identifier matching ^[A-Za-z][A-Za-z0-9_.:-]*$. The page prints many more (Setup, Stop, UserPromptSubmit, and others) in the same table, lines 33-65.

## C1 conjuncts

| Conjunct | Verdict |
|---|---|
| Own docs, pinned host code.claude.com | yes |
| Names a file that holds hook configuration (lifecycle commands) | yes — line 225 "Hooks are defined in JSON settings files."; line 237 "Hook locations"; line 244 token |
| Path regex TOKEN_RE of verifiers/check_command_files.py | yes |
| After one leading ~/ or ./ strip: >= 2 segments | yes — .claude, settings.json (nothing stripped) |
| First segment starts with . | yes |
| No segment word (split on -, ., _) in skill/skills/agent/agents/command/commands/prompt/prompts/rule/rules/plugin/plugins/extension/extensions | yes — words claude, settings, json |
| E7: no dot in a non-final segment except as its first character | yes — .claude |
| No other client's marker (codex, vscode, copilot, gemini, cursor, opencode) | yes — only own marker claude |
| E5: not the same token another client's row would lead with | yes — web search restricted to cursor.com, docs.cursor.com, opencode.ai, geminicli.com, developers.openai.com, code.visualstudio.com, docs.github.com returned no hits for this token (constraint then relaxed; hits were Claude's own pages). The foreign-name guard rejects this token for every other client because it contains claude. |
| Quote 6-25 words, token at segment boundaries, hook/hooks outside the token | yes — line 910, 21 words |
| >= 2 event names on that page, identifier regex | yes — lines 33 and 37 at minimum |
| Page is not changelog/release/news/blog/issue | yes |

## Status marks

The settings-file hook configuration is not marked experimental, preview, or deprecated. Separate marks on the same page, not about this token: agent hooks (type agent) are experimental (lines 396 and 3990); PreToolUse's old top-level decision and reason fields are deprecated (line 1974); a changedFiles list is called public beta (line 1783).

## New-ground pre-count

Command:

git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin grep -ilF '.claude/settings.json' a975cbbf00534443c49bf02e29c813a3db0bf0f8 -- . ':!.ufo' | wc -l

Output: 0 (pipeline exit 0). git grep itself exits 1 when there is no match; wc -l is 0. The token string is absent from the base tree outside .ufo.
