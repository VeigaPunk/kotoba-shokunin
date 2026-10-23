Result: DONE — Claude Code: ELIGIBLE `.claude/commands/`

Census seat CensusClaudeCode. Read-only. No tools installed. No lane code executed. Fetched bytes kept under `/fast/scratch/hyaku/kotoba-r58/CensusClaudeCode/` (not lane content).

## Page

Primary (quote source): `https://code.claude.com/docs/en/slash-commands.md`

- Access: `Fri 23 Oct 2026 07:37:48 AM UTC` (`date -u` immediately before the curl that saved the body). Header recheck `Fri 23 Oct 2026 07:39:39 AM UTC`: `HTTP/2 200`, `content-type: text/markdown; charset=utf-8`, no `Location`.
- Fetch: `curl -sSL -o <body> -w "%{http_code} %{url_effective}"`, exit 0. Final status 200, effective URL unchanged.
- Bytes: 114542. sha256: `6b070e872dea28905a7ea7f45c4d5960f5bdf28cc73ac808799af6d50435ffbd`. 1253 lines. Title line 5: `# Extend Claude with skills`.
- Same bytes at `https://code.claude.com/docs/en/skills.md` (HTTP/2 200, `text/markdown`, sha256 identical, `cmp` identical).
- `https://docs.claude.com/en/docs/claude-code/slash-commands.md` and `https://docs.anthropic.com/en/docs/claude-code/slash-commands.md`: HTTP/2 301, `location: https://code.claude.com/docs/en/slash-commands.md`. With `-L` the first fetch landed on that page (same sha256).
- Not a changelog, release, news, or blog URL.

`https://code.claude.com/docs/en/commands.md` (built-in command reference, not the custom-file page): same curl, 200, effective URL unchanged, 54225 bytes, sha256 `80164a5bc0d09cd44fef9d2d99d152a4fefae04adace1cdfba55d7448db7ed52`. Grep of that body for `.claude/commands`, `custom command`, and `slash command`: no matches. Header (lines 5–7) is `# Commands` / built-in commands and bundled skills. Not the source of the token.

## Token

Printed folder: `.claude/commands/`

It is the directory where a user writes a Markdown file that Claude Code still loads as a custom slash command. Line 17 (same file): a file at `.claude/commands/deploy.md` and a skill at `.claude/skills/deploy/SKILL.md` both create `/deploy`. Line 172 calls the Markdown file in `.claude/commands/` a command file, "the older format", and says it still works.

`~/.claude/commands` does not occur in the fetched body (count 0). Personal skills are printed as `~/.claude/skills/<skill-name>/SKILL.md` (line 159), which is a different path and fails the segment ban below.

## Quote

File `code.claude.com_docs_en_slash-commands.md.body` line 172. No bytes stripped. Contiguous substring (confirmed `quote in file` True). 14 whitespace-separated words (backticks left in: still 14).

`**Command files**: a Markdown file in `.claude/commands/` is the older format and still works.`

The token `.claude/commands/` is inside that span. Outside it, `Command` matches `(?i)\bcommands?\b` (`**Command files**:` …).

## C1 conjuncts

Scored against `plans/round-58.md` § C1 and the v2 path regex `TOKEN_RE` in `verifiers/check_plugin_manifests.py:258` (`^(~/|\./)?[A-Za-z0-9_.-]+(/[A-Za-z0-9_.*-]+)*/?$`). Own-marker behaviour taken from that file's foreign-name guard (`:91-94`, `:561-567`, self-test `:1222`: a `.claude` token is not foreign to Claude Code).

| Conjunct | Verdict |
|---|---|
| Own documentation on a pinned host | YES. `code.claude.com` (also reached by 301 from `docs.claude.com` and `docs.anthropic.com`) |
| Folder or file pattern for a user-written reusable prompt / custom slash-command file | YES. Markdown command file in `.claude/commands/`; a file there creates a `/` command (lines 17, 172, 450) |
| v2 path regex | YES. `.claude/commands/` full-matches `TOKEN_RE` |
| After one leading `~/` or `./`, ≥ 2 path segments | YES. Nothing to strip. Non-empty segments `.claude` and `commands` |
| First segment starts with `.` | YES. `.claude` |
| Final non-empty segment, split on `-` `.` `_`, holds `command` / `commands` / `prompt` / `prompts` | YES. `commands` |
| No segment word is skill, skills, agent, agents, rule, rules, plugin, plugins, extension, extensions | YES. Words are `claude`, `commands` |
| No dot inside a non-final segment except as its first character | YES. The only dot in `.claude` is the first character |
| No other client's marker (`codex`, `vscode`, `copilot`, `gemini`, `cursor`, `opencode`) | YES. `claude` is this client's own marker, not another client's |
| Not the same path as another client's row | Not shown as shared. A site-constrained search of cursor.com, docs.cursor.com, opencode.ai, geminicli.com, developers.openai.com, and code.visualstudio.com for `.claude/commands` returned no matches (the engine then relaxed the constraint; the hits were Claude pages). This seat did not fetch those clients' docs. E5 is cross-row and is not closed here |
| Quote 6–25 words, token case-sensitive, command(s)/prompt(s) outside the token | YES. 14 words, line 172, as quoted above |
| Source is not changelog / release / news / blog | YES |

## Older, not withdrawn

The word `deprecated` does not occur. `legacy` occurs only as example skill names (`legacy-system-context`, line 563; `"legacy-context"`, line 933), not as a label on this directory.

The page does mark the form as older and still supported:

- Line 17: `**Custom commands have been merged into skills.**` and `Your existing `.claude/commands/` files keep working.`
- Line 172: `is the older format and still works` and `Prefer a skill for new work`.

That does not fail any C1 conjunct. The recommended successor `.claude/skills/<skill-name>/SKILL.md` (lines 159–160) is not eligible: the segment `skills` is banned, and the printed `<skill-name>` is outside `TOKEN_RE`.

## Near-misses on the same page (not the row)

| Printed text | Line | Why it is not the token |
|---|---|---|
| `.claude/commands/deploy.md` | 17, 450 | Final segment `deploy.md` splits to `deploy`, `md`. No command/prompt word |
| `.claude/commands/frontend/component.md` | 451 | Final segment `component.md` splits to `component`, `md` |
| `.claude/skills/<skill-name>/SKILL.md` | 159–160 | Segment `skills` banned; angle brackets fail `TOKEN_RE` |
| `~/.claude/skills/…` | 109, 116, 159 | Same `skills` ban. `~/.claude/commands` is not printed |

## Q30

Not run. A candidate exists on the current docs page, so the silent-client sweep does not apply.
