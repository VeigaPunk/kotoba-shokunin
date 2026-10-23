Result: DONE — VS Code: ELIGIBLE `.github/prompts`

Census seat CensusVSCode. Read-only. No tools installed. No lane code executed. Fetched bytes kept under `/fast/scratch/hyaku/kotoba-r58/CensusVSCode/` (not lane content).

## Page

Primary (quote source): `https://code.visualstudio.com/docs/agent-customization/prompt-files.md`

- Access: `Fri 23 Oct 2026 07:38:12 AM UTC` (`date -u` immediately before the curl that saved the body). Response header `date: Fri, 23 Oct 2026 07:38:12 GMT`.
- Fetch: `curl -sSL -D prompt-files.md.hdr -o prompt-files.md`, exit 0. `HTTP/2 200`, `content-type: text/markdown; charset=UTF-8`, `content-length: 13729`, no `Location`. Effective URL unchanged.
- Bytes: 13729. sha256: `4ad1b2bcaf78c9166b1609610f354d9cb8b1ff9c9e7cf643c443fad04dac6685`. 228 lines. Title line 3: `# Use prompt files in VS Code`. `last-modified: Thu, 22 Oct 2026 22:04:58 GMT`.
- Not a changelog, release, news, or blog URL. Pinned host `code.visualstudio.com`.

Same token in the docs source (pinned host `github.com/microsoft/vscode-docs`, raw mirror allowed): `https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/agent-customization/prompt-files.md`. `date -u` `Fri 23 Oct 2026 07:40:50 AM UTC`, `HTTP/2 200`, `content-type: text/plain; charset=utf-8`, 14475 bytes, sha256 `5cd8b9074795dbaee1bb4e791070660fe95009cd9a33035ddeca907ec85b3e15`. The table cell is byte-identical; it is line 35 there because the file starts with YAML front matter the published page does not. Quote below is from the published page.

Old path `https://code.visualstudio.com/docs/copilot/customization/prompt-files.md`: HTTP 404, 9 bytes, body `Not Found`, sha256 `0019dfc4b32d63c1392aa264aed2253c1e0c2fb09216f8e2cc269bbfb8bb49b5` (first batch, `date -u` `Fri 23 Oct 2026 07:37:50 AM UTC`). The HTML URL without `.md` followed to `https://code.visualstudio.com/docs/agent-customization/prompt-files` (final 200, 133911 bytes, sha256 `9cd80a9a074c3a7f2b1ef2be9b775fdf9aa2c5cf558ca19851954fa9edfc4061`). Not quoted; the markdown page is the source.

## Token

Printed folder: `.github/prompts`

Line 25 of the published markdown, inside a backtick span: `| Workspace | `.github/prompts` folder |`. Section heading line 19: `## Prompt file locations`. Line 21 says the table is the default file locations the Local harness uses for prompt files. A prompt file is a reusable Markdown file the user invokes as a slash command (line 5).

## Quote

Lines 25–28 of `prompt-files.md`. No bytes stripped. Contiguous substring, byte offset 1890–2016 (126 bytes). Confirmed `ws(quote) in ws(page)` after collapsing whitespace. 22 whitespace-separated words with the backticks left in; 22 after removing them.

```
`.github/prompts` folder |
| User profile | Your user data (specific to your VS Code profile) |

To create a user-level prompt
```

The token `.github/prompts` is the first word (backticks attached; they are not whitespace). Outside that span, the final word `prompt` matches `(?i)\bprompts?\b`. The `prompts` inside `.github/prompts` is inside the span and does not count. Four of the 22 words are a bare `|`.

## C1 conjuncts

Scored against `plans/round-58.md` § C1 and the v2 path regex `TOKEN_RE` in `verifiers/check_plugin_manifests.py:258` (`^(~/|\./)?[A-Za-z0-9_.-]+(/[A-Za-z0-9_.*-]+)*/?$`). Own-marker behaviour taken from that file's foreign-name guard (`:91-94`, `:561-567`).

| Conjunct | Verdict |
|---|---|
| Own documentation on a pinned host | YES. `code.visualstudio.com`. Same cell on `github.com/microsoft/vscode-docs` (raw mirror) |
| Folder or file pattern for a user-written reusable prompt / custom slash-command file | YES. Workspace default location of prompt files, which the page says are invoked as slash commands (lines 5, 19–25) |
| v2 path regex | YES. `.github/prompts` full-matches `TOKEN_RE` |
| After one leading `~/` or `./`, ≥ 2 path segments | YES. Nothing to strip. Non-empty segments `.github` and `prompts` |
| First segment starts with `.` | YES. `.github` |
| Final non-empty segment, split on `-` `.` `_`, holds `command` / `commands` / `prompt` / `prompts` | YES. `prompts` |
| No segment word is skill, skills, agent, agents, rule, rules, plugin, plugins, extension, extensions | YES. Split words are `github` and `prompts` (a leading `.` only adds an empty piece) |
| No dot inside a non-final segment except as its first character | YES. The only dot in `.github` is the first character |
| No other client's marker (`claude`, `codex`, `copilot`, `gemini`, `cursor`, `opencode`; `vscode` is this client's own) | YES. Neither segment contains those strings |
| Not the same path as another client's row | Not a row yet. The same token is printed on Copilot CLI's pinned host; see below. E5 is cross-row and is not closed here |
| Quote 6–25 words, token case-sensitive, command(s)/prompt(s) outside the token | YES. 22 words, lines 25–28, as quoted above |
| Source is not changelog / release / news / blog | YES |

## Same path on another pinned host

`https://docs.github.com/en/copilot/tutorials/customization-library/prompt-files/your-first-prompt-file.md` (Copilot CLI pin `docs.github.com`, not a VS Code pin). `date: Fri, 23 Oct 2026 07:40:57 GMT`, `HTTP/2 200`, `content-type: text/markdown; charset=utf-8`, 3039 bytes, sha256 `117468ccb3abe5d07ae8f76a309f291b0fb93dae6d06de789feb9b90aa87b0ed`. Line 47, no bytes stripped:

`1. Save the prompt file above as `explain-code.prompt.md` in your `.github/prompts` folder.`

Line 49 then says to enter `/explain-code` in Visual Studio Code. If the Copilot CLI row uses `.github/prompts`, v2 E5 disqualifies both rows. This seat does not decide that row.

A site-constrained search for `.github/prompts` on `developers.openai.com`, `code.claude.com`, `geminicli.com`, `cursor.com`, `opencode.ai`, and `code.visualstudio.com` returned no matches; the engine then dropped the site constraint. This seat did not fetch those other clients' docs. `code.visualstudio.com` was fetched directly above.

## Not deprecated; Local-only

The word `deprecated` on the prompt-files page is about tool-set references (line 44), not this folder. `legacy` does not occur.

The page does limit where the files run. Line 17, no bytes stripped:

`Prompt files run only in **Local** harness sessions in the Chat view.`

Migration page `https://code.visualstudio.com/docs/agent-customization/migrate-customizations.md`, header `date: Fri, 23 Oct 2026 07:39:35 GMT`, `HTTP/2 200`, `text/markdown`, 59037 bytes, sha256 `a671708e4247448a8128000d5ef3b7c4ebbef15a81d7feccd74d486c1b64941a`. Line 168: Copilot harness sessions do not load `*.prompt.md` files, and `Prompt files remain supported in Local harness sessions.`

Settings page `https://code.visualstudio.com/docs/agents/reference/ai-settings.md`, same header date `Fri, 23 Oct 2026 07:39:35 GMT`, `HTTP/2 200`, `text/markdown`, 65476 bytes, sha256 `4708c18ff395b3a1121d58f03bca5e72cbe7ffcef6e19bfc6d0b078e333f6632`. Line 356 marks `setting(chat.promptFilesLocations)` `_(Deprecated)_` and prints the default `{ ".github/prompts": true }`. That is the same token, on a setting the page labels deprecated. The location table on the prompt-files page is not under that label. Not a second path.

## Near-misses (not the row)

| Printed text | Where | Why it is not the token |
|---|---|---|
| `.prompt.md` | prompt-files.md line 35 | One segment. After stripping, fewer than 2 path segments |
| `~/prompts/style-guide.md` | prompt-files.md line 56 | An example of a file a prompt may reference, not the command-file folder. After stripping `~/`, the first segment is `prompts`, which does not start with `.` |
| `Your user data (specific to your VS Code profile)` | prompt-files.md line 26 | User-profile scope. Not a path token |
| `{ ".github/prompts": true }` | ai-settings.md line 356 | Same folder, as the default of a setting that page marks deprecated |

`https://code.visualstudio.com/learn/customizations/6-prompt-files.md` (`Fri 23 Oct 2026 07:38:12 AM UTC`, HTTP/2 200, 5531 bytes, sha256 `780968575728a76a0c623ec6bb501997ab8f8470b4587519c3114c2a99cfc589`) describes prompt files and does not print `.github/prompts`.

## Q30

Not run. A candidate exists on the current docs page, so the silent-client sweep does not apply.
