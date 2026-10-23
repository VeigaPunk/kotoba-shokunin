---
source: S096 https://code.claude.com/docs/en/hooks.md; S097 https://learn.chatgpt.com/docs/hooks.md; S098 https://code.visualstudio.com/docs/agent-customization/hooks.md; S099 https://docs.github.com/en/copilot/concepts/customizations/hooks.md; S100 https://geminicli.com/docs/hooks/best-practices.md; S101 https://cursor.com/docs/hooks
verified-at: 2026-10-23
recheck: python3 -B verifiers/check_hook_files.py --rev <rev> --fetch
---

# Hook files by client (round 59)

A hook is a command (or other handler) the client runs itself at a named lifecycle event — before a tool call, at
session start — configured in a file the client reads. A rule written into a prompt, skill or always-on file is text the
model reads; a hook is run by the client at the event. This entry records, from each client's own documentation read
on 2026-10-23 (vendor pages, not a runtime test), which file holds hook configuration and which event names the page
prints, so an author can route a must-run check to the right file. Snapshots of the exact fetched bytes are committed
at `.ufo/waves/round-59/snapshots/S096.page`–`S101.page`; each sha256 equals its SOURCES row.

Scope boundary (province): this lane routes a rule to the client's hook file and names the events; writing, running or
debugging hook code stays outside it, as the round-13 census already ruled for extension/hook/tool module roots
(`corpus/knowledge/instruction-surface-census-round13.md` § excluded surfaces: "executable surfaces, out of
prompt-craft province"). Host package and initramfs hooks are tsukuroi's (`.ufo/waves/round-59/w0/ConnSiblingHooks.md`).

| Client | Hook config | Source | Quote |
|---|---|---|---|
| Claude Code | `.claude/settings.json` | S096 | This `PreToolUse` hook in `.claude/settings.json` runs a project script before each Bash command, and blocks the command if the script fails: |
| Codex | `~/.codex/hooks.json` | S097 | a default `hooks/hooks.json` file. See [Build plugins](https://developers.openai.com/plugins/build/plugins#bundled-mcp-servers-and-lifecycle-hooks) for the plugin packaging rules. In practice, the four most useful locations are: - `~/.codex/hooks.json` |
| VS Code | `.github/hooks/*.json` | S098 | Automation shared with a repository &#124; `.github/hooks/*.json` at the repository root &#124; &#124; Hooks |
| Copilot CLI | `~/.copilot/hooks/*.json` | S099 | Copilot CLI also supports personal hooks in `~/.copilot/hooks/*.json`. |
| Gemini CLI | `.gemini/settings.json` | S100 | When you open a project with hooks defined in `.gemini/settings.json`: |
| Cursor | `.cursor/hooks.json` | S101 | If you have hooks defined in `.cursor/hooks.json` at the root of your project, cloud agents pick them up and run them during their work. |

## Per-client notes

- **Claude Code (S096).** Project `.claude/settings.json`; user `~/.claude/settings.json` and local
  `.claude/settings.local.json` also hold hooks (`hooks.md:243-245`). Events include `SessionStart` (`:33`),
  `PreToolUse` (`:37`), `PostToolUse` (`:40`) and `SessionEnd` (`:65`). Command hooks run with the user's full
  permissions; the page says to review and test every hook command before adding it (`:4146`).
- **Codex (S097).** Hooks live next to active config layers, as `hooks.json` or inline `[hooks]` tables in
  `config.toml`; the page lists `~/.codex/hooks.json` first among the four most useful locations (`hooks.md:30-46`).
  Events include `PreToolUse` and `SessionStart` (`:25,27`). Non-managed hooks must be reviewed and trusted before they
  run (`:19`).
- **VS Code (S098).** Repository-shared hooks in `.github/hooks/*.json` (`hooks.md:59`); personal, settings, plugin
  and agent-scoped sources also exist (`:58-62`). The feature is marked Preview (`:4,11`). Events include
  `sessionStart` and `preToolUse` (`:128,130`). The page calls hook configuration and scripts executable code to
  review before use (`:202`).
- **Copilot CLI (S099).** Repository hooks in `.github/hooks/*.json` and personal hooks in `~/.copilot/hooks/*.json`
  (`hooks.md:28`). The row leads with the personal path because the repository pattern is the VS Code row's token
  (one token, one row: rule E5). Events include `sessionStart` and `preToolUse` (`:34,37`).
- **Gemini CLI (S100).** Project hooks in `.gemini/settings.json` (`best-practices.md:413`); the page prints
  `BeforeTool` and `AfterModel` (`:31`) and asks you to verify the source of project hooks before enabling them
  (`:442`). Its session events are on the separate hooks page, which is not a row.
- **Cursor (S101).** Project `.cursor/hooks.json` runs for cloud agents (`hooks:50`); user `~/.cursor/hooks.json` is
  not available to cloud agents (`:102`). Events include `preToolUse` and `postToolUse` (`:27,67`); `sessionStart` (`:1340`) is not run for cloud agents (`:88`). The
  served `hooks.md` URL answered HTTP 404 to the counter's curl header set; `https://cursor.com/docs/hooks` served
  the same markdown bytes.
- **opencode — no hook file.** Hook code is a plugin module, discovered by default in `.opencode/plugins/` and
  `~/.config/opencode/plugins/` (configured plugin paths and npm packages also load; § Plugin manifests by client;
  S085, S087; `.ufo/waves/round-59/build/CriticCensus.md` OC-1); `opencode.ai/docs/hooks.md` is HTTP 404
  (`.ufo/waves/round-59/w0/Censusopencode.md`, `.ufo/waves/round-59/build/SrcOpencodeNegative.md`).

## Quote shaping (per row)

- S096, S099, S100, S101: one source line, bytes unchanged.
- S097: lines 38-44 folded to single spaces; the Markdown link and the list marker `-` are kept as printed.
- S098: lines 59-60 (a table row and the next heading) folded to single spaces; the three literal `|` bytes are
  written `&#124;` so the quote stays in one Markdown cell.

## Not held

- Runtime behaviour: no hook was run; which events fire, in what order, and with what payload is the pages' word.
- Precedence and merging across user, project, local, managed and plugin scopes beyond what a page states.
- Whether an event name means the same thing on two clients (`preToolUse` on VS Code and Copilot CLI; the Copilot page
  warns against assuming event support across surfaces).
