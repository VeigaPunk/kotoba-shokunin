Result: DONE — Gemini CLI: ELIGIBLE `.gemini/settings.json`

Gemini CLI's own docs on pinned host `geminicli.com` name `.gemini/settings.json` as the project file that holds hook configuration (lifecycle commands run on events such as `BeforeTool` and `SessionStart`). One eligible token. Not marked experimental, preview, or deprecated. Base-tree pre-count is 0.

## Lead candidate

| Field | Value |
|---|---|
| Token (as printed) | `.gemini/settings.json` |
| Page | https://geminicli.com/docs/hooks/best-practices.md |
| Also names the same file | https://geminicli.com/docs/hooks.md line 97 (project settings); the 6–25-word quote is on best-practices, not on that line |
| Fetched | `Fri 23 Oct 2026 09:03:23 AM UTC` (`date -u` immediately before curl). Response `date: Fri, 23 Oct 2026 09:03:23 GMT` |
| HTTP | 200, `content-type: text/markdown; charset=utf-8`, `content-length: 17650` |
| Bytes / sha256 | 17650 / `fb44fbcfaccc3cdb7895d989f3808bed66cfa6516411535c4c4d9077d242e7bc` |
| Saved | `/fast/scratch/hyaku/kotoba-r59/CensusGeminiCLI/geminicli.com_docs_hooks_best-practices.md.body` |
| Line | 413 |
| Quote (10 words, no bytes stripped) | When you open a project with hooks defined in `.gemini/settings.json`: |

Quote is line 413 byte-exact (`repr`: `'When you open a project with hooks defined in `.gemini/settings.json`:'`). Whitespace split is 10 words with or without the two backtick bytes (U+0060) that wrap the path. After removing those backticks the token sits between a space and `:`. With them, the left character is `` ` `` and the right character is `` ` ``. Both are path-segment boundaries under `check_command_files.py` `first_boundary` (`BOUNDARY_PREV` includes space and backtick; `:` and backtick are not a letter, digit, `_`, or `-`). The word `hooks` is at quote offsets 29–34, outside the token span. Case-sensitive match of `.gemini/settings.json`.

User-Agent on every fetch: `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36`. No tools installed.

## Events (same page, and the hooks page)

Identifier regex `^[A-Za-z][A-Za-z0-9_.:-]*$`.

Same page as the quote, `best-practices.md` line 31, byte-exact:

`hooks that run frequently (like `BeforeTool` or `AfterModel`).`

- `BeforeTool` — line 31 (also lines 655 and the JSON key context is not required)
- `AfterModel` — line 31 (also lines 76 and 103)

Also on that page: `AfterAgent` lines 74 and 79.

Client's own hooks page `https://geminicli.com/docs/hooks.md` (fetched `Fri 23 Oct 2026 09:02:48 AM UTC`, response `date: Fri, 23 Oct 2026 09:02:49 GMT`, HTTP 200, 8341 bytes, sha256 `a06a92438d3110690e875d61feef49a850d82eda618bb837146a1a7ff7a4c8d9`, saved `.../geminicli.com_docs_hooks.md.body`). Event table, each name backticked:

- `SessionStart` line 40
- `SessionEnd` line 41
- `BeforeAgent` line 42
- `AfterAgent` line 43
- `BeforeModel` line 44
- `AfterModel` line 45
- `BeforeToolSelection` line 46
- `BeforeTool` line 47
- `AfterTool` line 48
- `PreCompress` line 49
- `Notification` line 50

`hooks.md` lines 94–97 say hooks are configured in `settings.json` and then name `.gemini/settings.json`, but that span is 29 whitespace-separated words from `Hooks` through the token, so it is not a legal 6–25-word quote. The legal quote is the best-practices line above. `hooks.md` line 94's bare `` `settings.json` `` is a different, failing token (one segment, not dot-led).

## C1 conjuncts for `.gemini/settings.json`

Path regex used: `check_command_files.py` `TOKEN_RE` = `^(~/|\./)?[A-Za-z0-9_.-]+(/[A-Za-z0-9_.*-]+)*/?$`. Segment words: split on `-`, `.`, `_`, empties dropped. Nothing was stripped (`~/` and `./` are absent). Segments: `.gemini`, `settings.json`. Words: `gemini`; `settings`, `json`.

- Own documentation: yes — Gemini CLI docs, title "Hooks Best Practices", fetched markdown.
- Pinned host: yes — `geminicli.com` (not a changelog, release, news, blog, or issue URL).
- Names a file that holds hook configuration: yes — "hooks defined in `.gemini/settings.json`". `hooks.md` line 94: "Hooks are configured in `settings.json`" and line 97 lists this path as project settings. The JSON object key is `hooks`; commands run on lifecycle events.
- `TOKEN_RE`: yes.
- After one leading `~/` or `./`, at least 2 path segments: yes — 2, nothing stripped.
- First segment starts with `.`: yes — `.gemini`.
- No segment word in {skill, skills, agent, agents, command, commands, prompt, prompts, rule, rules, plugin, plugins, extension, extensions}: yes.
- E7, no dot in a non-final segment except as its first character: yes — the only dot in `.gemini` is the first character; `settings.json` is final.
- No other client's marker {claude, codex, vscode, copilot, cursor, opencode}: yes. The token does contain `gemini`, which is Gemini CLI's own marker (`foreign_marker("Gemini CLI", ".gemini/settings.json")` is None in that checker).
- E5, not a token another client's row would lead with: yes — not shared. A web search for the exact token off `geminicli.com` and off `github.com/google-gemini` returned a Google blog and third-party pages, not Claude Code, Codex, VS Code, Copilot CLI, Cursor, or opencode docs. This seat did not fetch those six clients' pages. The marker `gemini` makes the token foreign to each of them, so a row of theirs that led with it would fail the foreign-name guard; if one did, E5 would disqualify both rows. None was observed.
- Quote 6–25 words, token case-sensitive at a segment boundary, `hook`/`hooks` outside the token: yes — 10 words, details above.
- At least 2 distinct event identifiers, with line numbers, on this page or the hooks page: yes — `BeforeTool` and `AfterModel`, both line 31.
- Not changelog/release/news/blog/issue: yes.

Feature status: not marked experimental, preview, or deprecated. Grep of the hooks markdown (`hooks.md`, `best-practices.md`, `writing-hooks.md`) and of the HTML at `https://geminicli.com/docs/hooks/` found none of those words. `https://geminicli.com/docs/reference/configuration.md` section `#### hooksConfig` (line 2300) and `#### hooks` (line 2319) describe `hooksConfig.enabled` default `true` with no such label. (That configuration file does use "preview" and "deprecated" for unrelated model and UI settings.)

## Other printed paths (not a second eligible row)

- `~/.gemini/settings.json` — `hooks.md` line 98, user settings. `TOKEN_RE` yes; after stripping `~/` the segments are the same as the lead token, so `normalise` is `.gemini/settings.json`. Same population member, not a second one. The legal quote contains the normalised form, not the `~/` spelling.
- `/etc/gemini-cli/settings.json` — `hooks.md` line 99. Fails `TOKEN_RE` (leading `/`) and the first segment `etc` does not start with `.`.
- `` `settings.json` `` — `hooks.md` line 94. One segment; first segment does not start with `.`.
- `.gemini/hooks/` — writing-hooks.md line 34 `mkdir -p .gemini/hooks` ("Create a directory for hooks", line 24). Grammatically well-formed (segments `.gemini`, `hooks`; `hooks` is not a forbidden word), but the docs tell you to create that directory for scripts named later in each hook's `command`. They say hooks are defined in `.gemini/settings.json`, not discovered from this folder. The line-24 word `hooks` and the line-34 token are more than 25 words apart (a note and a code fence sit between them). Not the config file.
- `hooks/hooks.json` — extensions reference, https://geminicli.com/docs/extensions/reference.md lines 242–243, fetched in the same `09:03:23Z` batch, HTTP 200, 12022 bytes, sha256 `8b9eecb254df04220b23d56da6d63018abe7c5364122af7dee16b05d63b1fe72`, saved `.../geminicli.com_docs_extensions_reference.md.body`. Byte-exact: `hooks in a `hooks/hooks.json` file within your extension directory.` That is a hook-configuration file (extension hooks, "not defined in the `gemini-extension.json` manifest", line 244). It fails the dot-led first segment (`hooks` does not start with `.`). Not eligible. The same page's sub-agent note (line 256) is a preview label for sub-agents, not for hooks.

## New-ground pre-count

Token with no leading `~/` or `./` and no trailing `/`: `.gemini/settings.json`.

```
git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin grep -ilF '.gemini/settings.json' a975cbbf00534443c49bf02e29c813a3db0bf0f8 -- . ':!.ufo' | wc -l
```

Output: `0` (pipeline exit 0). Unpiped, the same `git grep` exited 1 with empty stdout (no file at that revision outside `.ufo/` contains the token). `--no-optional-locks` is the only addition to the assigned command.

## Fetch notes

Markdown variants were used (`*.md` returned `text/markdown`). HTML for `/docs/hooks/` was also saved (HTTP 200, 123916 bytes) and checked only for an experimental badge. `https://geminicli.com/docs/hooks/index.md` was HTTP 404. No headless browser. No lane git or jj writes.
