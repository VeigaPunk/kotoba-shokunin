Result: DONE — VS Code: ELIGIBLE .github/hooks/audit.json

VS Code's own hooks page names a file that holds hook configuration. The token that passes every C1 conjunct is `.github/hooks/audit.json`. The repository discovery pattern `.github/hooks/*.json` also passes the path grammar, but Copilot CLI's hooks reference prints that same token, so a Copilot row that leads with it is E5 (both rows out). The user directory `~/.copilot/hooks/` fails the foreign-name guard (`copilot`).

## Lead candidate

- Token, as printed: `.github/hooks/audit.json`
- Page: https://code.visualstudio.com/docs/agent-customization/hooks.md (pinned host `code.visualstudio.com`; not a changelog, release, news, blog, or issue URL)
- What it is: the file the page tells you to create, whose body is a `hooks` map that runs a command on `preToolUse`. Line 77: `Create `.github/hooks/audit.json`:`
- Fetched bytes: `/fast/scratch/hyaku/kotoba-r59/CensusVSCode/hooks.md`
- `date -u` immediately before the fetch: `Fri 23 Oct 2026 09:02:50 AM UTC`
- Response `date` header: `Fri, 23 Oct 2026 09:02:51 GMT`
- HTTP 200, content-type `text/markdown; charset=UTF-8`, 15152 bytes
- sha256 `98c5be6b693a19ccd10c79b933d56e010101cef5a0eed699bd25e80289461e08`
- No bytes stripped. The `.md` variant is the page (the HTML twin was saved beside it and not used).

### Quote (7 words, lines 77–82)

Verbatim, newline kept, no markdown stripped. The seventh word is the JSON key; that is the `hooks` outside the path token. A window that also reaches the heading word `hook` on line 73 is 26 words and fails the 25-word cap.

~~~~
Create `.github/hooks/audit.json`:

```json
{
  "version": 1,
  "hooks":
~~~~

Whitespace split: `Create` / `` `.github/hooks/audit.json`: `` / `` ```json `` / `{` / `"version":` / `1,` / `"hooks":`. The path token starts after the opening backtick (a boundary character) and ends before the closing backtick. `"hooks":` is outside that span and matches `(?i)\bhooks?\b`.

### Events on the same page

Identifiers, byte-exact, each matching `^[A-Za-z][A-Za-z0-9_.:-]*$`:

| Name | Line |
|---|---|
| `sessionStart` | 128 |
| `userPromptSubmitted` | 129 |
| `preToolUse` | 130 |
| `postToolUse` | 131 |
| `preCompact` | 132 |
| `subagentStart` | 133 |
| `subagentStop` | 133 |
| `agentStop` | 134 |
| `sessionEnd` | 135 |
| `PreToolUse` | 139 |

Line 128 cell: `` `sessionStart` ``. Line 130 cell: `` `preToolUse` ``.

### Conjuncts for `.github/hooks/audit.json`

- Pinned host, client's own current docs: YES (`code.visualstudio.com`, HTTP 200 markdown above).
- Not a changelog / release / news / blog / issue URL: YES (`/docs/agent-customization/hooks`).
- Path regex `TOKEN_RE` of `verifiers/check_command_files.py` (`^(~/|\./)?[A-Za-z0-9_.-]+(/[A-Za-z0-9_.*-]+)*/?$`): YES. A `.` inside `[]` is literal, so `audit.json` is a legal final segment.
- After one leading `~/` or `./`, at least two segments: YES (`.github`, `hooks`, `audit.json`).
- First segment starts with `.`: YES.
- No segment, split on `-` `.` `_`, is skill/skills/agent/agents/command/commands/prompt/prompts/rule/rules/plugin/plugins/extension/extensions: YES (`github`, `hooks`, `audit`, `json`).
- E7, no dot in a non-final segment except as its first character: YES (`.github` is dot-led; `hooks` has no dot).
- No other client's marker (`claude`, `codex`, `vscode`, `copilot`, `gemini`, `cursor`, `opencode`): YES.
- E5, not a token another client's row would lead with: YES on the pages fetched. Absent from Copilot CLI `gh-hooks.md` (`find` of `audit.json` is -1), and absent from the Claude, Codex, Cursor, and Gemini hooks pages below. opencode's guessed hooks URL was HTTP 404; its v2 `llms.txt` lists no hooks page. Not a full opencode tree sweep.
- Quote 6–25 words, token case-sensitive at a segment boundary, `hook`/`hooks` outside the token: YES (7 words, above).
- At least two event names on this page: YES (table above).
- Preview / experimental / deprecated: Preview, not deprecated. Line 4 title `Configure agent hooks in Visual Studio Code (Preview)`. Line 11: `The VS Code hooks experience is in Preview.` Preview is not a failing conjunct in the row rule.

### New-ground pre-count

```
git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin grep -ilF '.github/hooks/audit.json' a975cbbf00534443c49bf02e29c813a3db0bf0f8 -- . ':!.ufo' | wc -l
```

Output `0`. `git grep` itself exited 1 (no match); `wc` exited 0. Base `a975cbbf00534443c49bf02e29c813a3db0bf0f8`.

## Rejected candidates (same hooks page unless noted)

### `.github/hooks/*.json` — fails E5

Printed at hooks.md line 59: `` `.github/hooks/*.json` at the repository root ``. Same fetch as above. Grammar, dot-led first segment, E7, forbidden words, and foreign-name all pass (segments `.github`, `hooks`, `*.json`). An 8-word verbatim quote on lines 59–60 also passes the quote rule:

```
`.github/hooks/*.json` at the repository root |
| Hooks
```

Copilot CLI documents this exact token. Fetched `https://docs.github.com/en/copilot/reference/hooks-reference.md` at `Fri 23 Oct 2026 09:03:50 AM UTC`, HTTP 200, 72175 bytes, sha256 `7ad7c168f319ce390802289ededf8dead2742959b18b5ccf6f41c2342cbf1c97`, saved at `/fast/scratch/hyaku/kotoba-r59/CensusVSCode/gh-hooks.md`. Line 22: `Repository-level hook files — `.github/hooks/*.json` in the repository root.` The same token is also on lines 30, 90, and 919. A Copilot CLI row that leads with it disqualifies both rows. VS Code's page line 18 says the editor, the Copilot app, and Copilot CLI share this harness and its hook format.

Pre-count, same command shape, pattern `.github/hooks/*.json`: `0` (`git grep` exit 1).

Checked for this token and did not find it: Claude `https://code.claude.com/docs/en/hooks.md` (200, 274129 bytes, sha256 `c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8`); Codex `https://developers.openai.com/codex/hooks.md` redirected to `https://learn.chatgpt.com/docs/hooks.md` (200, 47133 bytes, sha256 `57166ef03e7059732dd90925d5c42dd4d187eb2625d66cc154d0fbd2edb65f92`); Cursor `https://cursor.com/docs/hooks.md` (200, 69145 bytes, sha256 `8436af768468590299c1beab9ea34bff8c5f1e5649ae244a989c28960dd2c88d`); Gemini `https://geminicli.com/docs/hooks.md` (200, 8341 bytes, sha256 `a06a92438d3110690e875d61feef49a850d82eda618bb837146a1a7ff7a4c8d9`). Those four fetches were `Fri 23 Oct 2026 09:07:57 AM UTC`. opencode `https://opencode.ai/docs/hooks.md` was HTTP 404 (97 bytes). This was a same-token check, not a Q30 silence sweep.

### `~/.copilot/hooks/` — fails the foreign-name guard

hooks.md line 58: `User hook files in `~/.copilot/hooks/`, or `$COPILOT_HOME/hooks/` when `COPILOT_HOME` is set.` Grammar passes (`.copilot` / `hooks`). The lower-cased token contains `copilot`, Copilot CLI's marker, so it is foreign to VS Code. Copilot CLI also prints it (gh-hooks.md line 23). Pre-count pattern `.copilot/hooks`: `0`.

### Other printed paths

- `.github/copilot/settings.json`, `.github/copilot/settings.local.json`, `~/.copilot/settings.json` (hooks.md line 65): inline `hooks` maps, but each token contains `copilot`.
- `.claude/settings.json`, `.claude/settings.local.json` (line 65), `~/.claude/settings.json` (migrate page): contain `claude`.
- `.github/hooks/log-tool-use.cjs` (line 94) and `.github/hooks/tool-use.log` (line 110): grammar passes, but they are the script and its log, not the hook configuration.
- `com.github.copilot/hooks/hooks.json` (plugin reference line 310): hook file inside a plugin, but the first segment is not dot-led, E7 fails (`com.github.copilot`), and the token contains `copilot`. `hooks/hooks.json` is not dot-led.
- `chat.hookFilesLocations` (hooks.md line 71): a setting id, not a dot-led path. The page says it does not configure Copilot discovery. The legacy Local reference does not name a default hook file path.
- `$COPILOT_HOME/hooks/` and `%USERPROFILE%\.copilot\hooks\`: not `TOKEN_RE`.

The migration page `https://code.visualstudio.com/docs/agent-customization/migrate-customizations.md` (fetched `Fri 23 Oct 2026 09:03:18 AM UTC`, HTTP 200, 59037 bytes, sha256 `a671708e4247448a8128000d5ef3b7c4ebbef15a81d7feccd74d486c1b64941a`) repeats `.github/hooks/*.json` at line 271 and the same user path at line 272, and prints event names at lines 311–318 (`SessionStart`, `PreToolUse`, and others). It does not print `.github/hooks/audit.json`. Saved at `/fast/scratch/hyaku/kotoba-r59/CensusVSCode/migrate.md`.

No tools installed. No lane file edited except this report.