Result: DONE — Copilot CLI: ELIGIBLE `~/.copilot/hooks/*.json`

Copilot CLI's own docs on docs.github.com name personal hook files at `~/.copilot/hooks/*.json`. That token passes every C1 conjunct. The repository pattern `.github/hooks/*.json` is also documented, but VS Code's hooks page prints that same token and it carries no foreign marker, so a VS Code row would lead with it and E5 would disqualify both. The personal glob is not printed by the other clients' hooks pages fetched here, and it contains Copilot CLI's own marker `copilot`, which the foreign-name guard rejects for every other client.

No tool was installed or updated.

## Lead candidate

Token as printed: `~/.copilot/hooks/*.json`

Page: https://docs.github.com/en/copilot/concepts/customizations/hooks.md
Fetched: `Fri 23 Oct 2026 09:02:56 AM UTC` (curl -sSL, browser UA, no redirect; effective URL is that address).
HTTP 200, 8428 bytes, sha256 `23370e092d2e2e81587b84038d0be116d99243a83c810b8e8cd41cf8734a10f4`.
Saved: `/fast/scratch/hyaku/kotoba-r59/CensusCopilotCLI/concepts-hooks.md` line 28.

Quote (verbatim, 8 words, no bytes stripped; backticks are on the page):

> Copilot CLI also supports personal hooks in `~/.copilot/hooks/*.json`.

`hooks` in "personal hooks" is outside the token. The token sits between backticks (left and right boundaries). Checked: the sentence is a contiguous substring of the fetched file, and `len(quote.split())` is 8.

Events on that same page, byte-exact identifiers (each line is `* **<name>**: ...`; the name itself is the identifier, markdown `**` not part of it):

| Name | Line |
|---|---|
| sessionStart | 34 |
| sessionEnd | 35 |
| userPromptSubmitted | 36 |
| preToolUse | 37 |
| postToolUse | 38 |
| agentStop | 39 |
| subagentStop | 40 |
| errorOccurred | 41 |

Line 32 says these are examples of Copilot CLI hook events. All eight match `^[A-Za-z][A-Za-z0-9_.:-]*$`.

The client's hooks reference prints a larger backticked set on the same pinned host (not required, since the quote page already has eight). Fetched in the same batch: https://docs.github.com/en/copilot/reference/hooks-reference.md — HTTP 200, 72175 bytes, sha256 `7ad7c168f319ce390802289ededf8dead2742959b18b5ccf6f41c2342cbf1c97`, file `hooks-reference.md`. Backticked names and lines: `agentStop` 270, `errorOccurred` 271, `notification` 272, `permissionRequest` 273, `postToolUse` 274, `postToolUseFailure` 275, `preCompact` 276, `preToolUse` 277, `sessionEnd` 278, `sessionStart` 279, `subagentStart` 280, `subagentStop` 281, `userPromptSubmitted` 282, `userPromptTransformed` 283.

Not marked experimental, preview, or deprecated for Copilot CLI. The only "public preview" sentence on the concepts page is about Visual Studio Code (line 24), and the next paragraph says the configuration below is for Copilot CLI and Copilot cloud agent. The hooks reference and the CLI how-to do not use those words.

## Conjuncts for `~/.copilot/hooks/*.json`

| Conjunct | Verdict |
|---|---|
| Own docs, pinned host (docs.github.com), not changelog/release/news/blog/issue | yes |
| Page names a file that holds hook configuration (commands run on lifecycle events) | yes — line 28, personal hooks; events are session/tool/prompt lifecycle |
| Path regex of `check_command_files.py` (`TOKEN_RE`) | yes |
| After one leading `~/`, at least 2 segments (`.copilot`, `hooks`, `*.json`) | yes |
| First segment starts with `.` | yes |
| No segment word in skill/skills/agent/agents/command/commands/prompt/prompts/rule/rules/plugin/plugins/extension/extensions | yes |
| E7: no dot inside a non-final segment except as its first character | yes (the dot in `*.json` is final) |
| No other client's marker (claude, codex, vscode, gemini, cursor, opencode) | yes — `copilot` is this client's own marker |
| E5: not the same token another client's row would lead with | yes — exact token only in `concepts-hooks.md` among pages fetched; see E5 notes |
| Quote 6–25 words, token at segment boundaries, `hook`/`hooks` outside the token | yes — 8 words |
| At least 2 event identifiers on this page or the client's hooks page | yes — eight on this page |
| Marked experimental/preview/deprecated | no |

## E5 notes

Fetched `Fri 23 Oct 2026 09:04:40 AM UTC` (and codex/gemini/opencode at `Fri 23 Oct 2026 09:06:13 AM UTC`), same UA, saved under `/fast/scratch/hyaku/kotoba-r59/CensusCopilotCLI/`.

| Page | Result for this exact token |
|---|---|
| VS Code `https://code.visualstudio.com/docs/agent-customization/hooks.md` (200, 15152 B, sha256 `98c5be6b693a19ccd10c79b933d56e010101cef5a0eed699bd25e80289461e08`) | does not print `~/.copilot/hooks/*.json`. It does print `~/.copilot/hooks/` (line 58) and `.github/hooks/*.json` (line 59) |
| Claude `https://code.claude.com/docs/en/hooks.md` (200, 274129 B, sha256 `c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8`) | no `.github/hooks` |
| Cursor `https://cursor.com/docs/hooks.md` (200, 69145 B, sha256 `8436af768468590299c1beab9ea34bff8c5f1e5649ae244a989c28960dd2c88d`) | lead paths are `.cursor/hooks.json` and `~/.cursor/hooks.json`, not this token |
| Codex `https://developers.openai.com/codex/hooks.md` → `https://learn.chatgpt.com/docs/hooks.md` (200, 47133 B) | token absent |
| Gemini `https://geminicli.com/docs/hooks.md` (200, 8341 B); `.../docs/cli/hooks.md` was 404 | token absent |
| opencode `https://opencode.ai/docs/hooks.md` and `.../hooks/` | HTTP 404 |

A Python scan of every file in the scratch dir found `~/.copilot/hooks/*.json` only in `concepts-hooks.md`. [INFERENCE] No other client row would lead with it: the token contains `copilot`, and `foreign_marker` in `verifiers/check_command_files.py` treats that as Copilot CLI's marker, so it is foreign to the other six.

## Other tokens (not the lead)

| Token | Where printed | Why not the lead |
|---|---|---|
| `.github/hooks/*.json` | concepts line 28; hooks-reference line 22 ("Repository-level hook files"); tutorial line 71; cli-config-dir line 470 | Grammar passes. E5 fails: VS Code line 59 prints this exact token as the repository hook source, and the token has no foreign marker, so a VS Code row would lead with it and both rows would be out |
| `~/.copilot/hooks/` | hooks-reference line 23; use-hooks line 78 | Grammar passes. Quote on the reference, 15 words, no bytes stripped: `files in the user-level hooks directory. By default this is `~/.copilot/hooks/` on macOS and Linux`. VS Code line 58 prints the same token. It is foreign to VS Code because of `copilot`, so VS Code should not lead with it, but it is the same printed token. Not used as the lead |
| `.github/hooks/` | use-hooks line 13 (CLI how-to); cli-config-dir line 108 | Grammar passes. The how-to sentence on line 13 has no `hook`/`hooks` outside the token. VS Code does not print this directory token alone, but it prints `.github/hooks/*.json`, which is the colliding form |
| `~/.copilot/settings.json` and `.github/copilot/settings.json` | hooks-reference lines 25 and 24 (inline `hooks` object) | Grammar passes (own marker). Settings files that can hold hooks, not the dedicated hook files. VS Code line 65 prints both |
| `.claude/settings.json` | hooks-reference line 24, "also read" | Foreign marker `claude`. Not eligible |
| `$COPILOT_HOME/hooks/`, `%USERPROFILE%\.copilot\hooks\` | hooks-reference line 23; use-hooks lines 81 and 118 | Fail `TOKEN_RE` (`$`, `%`, backslash). First segment is not dot-led |
| `hooks/hooks.json` | hooks-reference line 26 (plugin install dir) | First segment is not dot-led |

## New-ground pre-count

Token without the leading `~/`: `.copilot/hooks/*.json`.

```
git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin grep -ilF '.copilot/hooks/*.json' a975cbbf00534443c49bf02e29c813a3db0bf0f8 -- . ':!.ufo' | wc -l
```

Output: `0`. `git grep` itself exited 1 (no file matched); `wc` printed 0. The same command for `.github/hooks/*.json`, `.copilot/hooks`, and `.github/hooks` also printed 0.

## Fetches (Copilot CLI pages, 09:02:56Z)

| File | URL | HTTP | Bytes | sha256 |
|---|---|---|---|---|
| use-hooks.md | https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/use-hooks.md | 200 | 9310 | `aa74c0640fe6f814d057a7a9446a275c3b2758dc16e6c7d1d340837838b96b51` |
| hooks-reference.md | https://docs.github.com/en/copilot/reference/hooks-reference.md | 200 | 72175 | `7ad7c168f319ce390802289ededf8dead2742959b18b5ccf6f41c2342cbf1c97` |
| concepts-hooks.md | https://docs.github.com/en/copilot/concepts/customizations/hooks.md | 200 | 8428 | `23370e092d2e2e81587b84038d0be116d99243a83c810b8e8cd41cf8734a10f4` |
| tutorial-hooks.md | https://docs.github.com/en/copilot/tutorials/copilot-cli-hooks.md | 200 | 24837 | `e55fd855934aba5d0e2339e2c41a431a92ce10eec725367015e1a8a09abd307e` |
| cli-config-dir.md | https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-config-dir-reference.md | 200 | 166811 | `8be36090c19a7e284d4137f03db150927f3f215fb3b21ddfc9d87c614bec21b0` |

`https://docs.github.com/en/copilot/concepts/agents/hooks.md` (the how-to's link) returned HTTP 404, 502 bytes, sha256 `979615bad4719ae23bf76385ee60de8b1b05c785ce74497dee80ecb54c69c522`. The concepts page that did load is the customizations URL above.

User-Agent on every curl: `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36`.
