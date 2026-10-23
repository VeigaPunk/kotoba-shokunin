Result: MIXED — Draft delivered with the frozen VS Code token, but its W0 report records a conflicting E5 finding.

# ScribeEntry — hook-files knowledge entry draft

## Behavior and touched surfaces

Prepared the requested knowledge-entry text below. Its six entry-table quote cells are intentional placeholders for L1 to fill from the Src-seat reports. I did not edit `corpus/knowledge/hook-files-round59.md` or any other product file; this report is the only file written.

The draft uses the frozen W0 token `.github/hooks/*.json` for VS Code, as specified in `plans/round-59.md:69` and the assignment. Conflict for the canonical judge, verbatim:

- `CensusVSCode.md:1`: `Result: DONE — VS Code: ELIGIBLE .github/hooks/audit.json`
- `CensusVSCode.md:3`: `The repository discovery pattern .github/hooks/*.json also passes the path grammar, but Copilot CLI's hooks reference prints that same token, so a Copilot row that leads with it is E5 (both rows out).`
- `plans/round-59.md:69`: `VS Code | ELIGIBLE (Preview) | .github/hooks/*.json (the seat's lead was the example file .github/hooks/audit.json; the folder pattern is the documented location)`

The draft preserves the frozen plan token instead of silently resolving this discrepancy. The quote placeholder and shaping note leave room for L1 to choose a Src-seat quote that carries that frozen token.

## Gates, provenance, and limits

- Read `skill://godspeed`; read house style `corpus/knowledge/command-files-round58.md:1-78`, the frozen counter docstring `verifiers/check_hook_files.py:1-230` and target constants `:253-254`, both required controls `CtlFabEvents.md` and `CtlFabSnapshot.md`, and W0 reports for Claude Code, Codex, VS Code, Copilot CLI, Gemini CLI, Cursor, and opencode. The cited census details are in `.ufo/waves/round-59/w0/Census*.md`.
- `corpus/lessons/round-59.md` was not present when read (`read` returned `Path ... not found`). The shaping notes rely on the fetched-byte/positive-baseline receipts in `CtlFabSnapshot.md:170-237` and the explicit tag-shaping constraint in `CtlFabEvents.md:133-140`; they avoid claiming unchanged bytes for any quote.
- No vendor page was fetched by this seat; the draft's scope line reports the W0 source-seat date, 2026-10-23. No counter, build, test, lint, or runtime check was run. No tool was installed or updated.
- Out of scope: filling source quotes, editing lane product files, resolving the VS Code census conflict, asserting runtime behavior, and claiming precedence across scopes.
- Artifact path: `.ufo/waves/round-59/build/ScribeEntry.md`.

## Full draft file text

```markdown
---
source: S096 https://code.claude.com/docs/en/hooks.md; S097 https://learn.chatgpt.com/docs/hooks.md; S098 https://code.visualstudio.com/docs/agent-customization/hooks.md; S099 https://docs.github.com/en/copilot/concepts/customizations/hooks.md; S100 https://geminicli.com/docs/hooks/best-practices.md; S101 https://cursor.com/docs/hooks
verified-at: 2026-10-23
recheck: python3 -B verifiers/check_hook_files.py --rev <rev> --fetch
---

# Hook files by client (round 59)

Scope: vendor documentation was read on 2026-10-23; this is not a runtime test.

Claude Code describes project hooks in `.claude/settings.json` and a project script run before a Bash command; Codex describes lifecycle hooks configured as scripts or MCP tools (S096, `.ufo/waves/round-59/w0/CensusClaudeCode.md:7-9,24-28`; S097, `.ufo/waves/round-59/w0/CensusCodex.md:3,23-29`). VS Code documents a repository hook JSON pattern and a file example whose `hooks` map runs a command, while Copilot CLI documents personal hook files and lifecycle-event names (S098, `.ufo/waves/round-59/w0/CensusVSCode.md:7-9,32-49`; S099, `.ufo/waves/round-59/w0/CensusCopilotCLI.md:7-20,22-35`). Gemini CLI says project settings define hooks, and Cursor describes custom scripts spawned around stages of the agent loop (S100, `.ufo/waves/round-59/w0/CensusGeminiCLI.md:17,23-34,58`; S101, `.ufo/waves/round-59/w0/CensusCursor.md:17-35`). Use the cited hook configuration when the desired behavior is an automatically run command or script on a documented event; these census pages describe hook configuration and events, not a comparison with skills or rules, so they do not establish that hooks replace instruction files.

| Client | Hook config | Source | Quote |
|---|---|---|---|
| Claude Code | `.claude/settings.json` | S096 | [L1 fills from SrcClaudeCode] |
| Codex | `~/.codex/hooks.json` | S097 | [L1 fills from SrcCodex] |
| VS Code | `.github/hooks/*.json` | S098 | [L1 fills from SrcVSCode] |
| Copilot CLI | `~/.copilot/hooks/*.json` | S099 | [L1 fills from SrcCopilotCLI] |
| Gemini CLI | `.gemini/settings.json` | S100 | [L1 fills from SrcGeminiCLI] |
| Cursor | `.cursor/hooks.json` | S101 | [L1 fills from SrcCursor] |

## Per-client notes (W0 census reports)

- **Claude Code (S096):** User and project settings use `~/.claude/settings.json` and `.claude/settings.json`; local settings use `.claude/settings.local.json` (`CensusClaudeCode.md:7-9`). The settings-file hooks are not marked experimental, Preview, or deprecated; the separate agent-hook type is experimental (`:58-60`). Four event names are tabulated in the report, which notes that the page prints more (`:30-39`).
- **Codex (S097):** Other documented locations include repository `.codex/hooks.json` and user/repository `config.toml` hook settings (`CensusCodex.md:42-47,80-89`). Hooks are enabled by default; the deprecated `codex_hooks` alias is not a deprecation of hooks (`:78`). Twelve event identifiers are listed (`:44-60`).
- **VS Code (S098):** The page names the repository pattern `.github/hooks/*.json` and gives `.github/hooks/audit.json` as an example (`CensusVSCode.md:7-9,76-85`). No default hook-file path for the legacy Local reference is named (`:101`). Hooks are marked Preview (`:64`); ten event names are listed (`:32-49`). The frozen row token follows `plans/round-59.md:69`; the conflicting census finding is recorded in the report above.
- **Copilot CLI (S099):** The repository pattern `.github/hooks/*.json` is also documented, while the row's personal token is `~/.copilot/hooks/*.json`; the report explains the shared-token/E5 concern (`CensusCopilotCLI.md:3,62-79`). The feature is not marked experimental, Preview, or deprecated (`:39`); eight event names are listed (`:22-35`).
- **Gemini CLI (S100):** User `~/.gemini/settings.json` normalizes to the project token; `/etc/gemini-cli/settings.json` and the script folder `.gemini/hooks/` are other printed paths, not the lead config (`CensusGeminiCLI.md:72-78`). The settings-file feature is not marked experimental, Preview, or deprecated (`:70`). Three event names are identified on the quoted best-practices page; its separate hooks page lists eleven (`:23-48`).
- **Cursor (S101):** User `~/.cursor/hooks.json` normalizes to the project token; `.cursor/hooks/` is a script directory, not the config file (`CensusCursor.md:110-119`). The config is not marked experimental, Preview, or deprecated (`:84`); twenty-one event names are listed (`:37-64`).

## opencode: not eligible

The census found no published hooks file or `.opencode/hooks` location: the documented hook code lives in `.opencode/plugins/` or `~/.config/opencode/plugins/`, and v2 also names `.opencode/plugin/`. Each path contains the forbidden `plugin` or `plugins` segment; the hooks documentation URLs returned 404 (`Censusopencode.md:5-8,40-107`).

## Quote shaping notes

The notes below identify the positive-baseline candidate spans and their table encoding (`.ufo/waves/round-59/controls/CtlFabSnapshot.md:170-237`); L1 should keep them aligned with the actual Src-seat quote selected for each placeholder.

- **S096:** One-line source span; retain its Markdown backticks and punctuation, with no content shaping (`CtlFabSnapshot.md:172-180`).
- **S097:** Fold source line breaks and blank lines to single spaces for the table cell; retain backticks and non-whitespace characters. Keep the quote span clear of the `<repo>` bullets, which are unsafe under the counter's page-side tag stripping (`CtlFabSnapshot.md:182-196`; `CtlFabEvents.md:133-140`).
- **S098:** Fold the line break to a space and encode each of the two table-pipe bytes as `&#124;`; preserve the remaining non-whitespace text (`CtlFabSnapshot.md:198-207`).
- **S099:** One-line source span; retain its punctuation and backticks without content shaping (`CtlFabSnapshot.md:209-217`).
- **S100:** One-line source span; retain its punctuation and backticks without content shaping (`CtlFabSnapshot.md:219-227`).
- **S101:** One-line source span; retain its punctuation and backticks without content shaping (`CtlFabSnapshot.md:229-237`).

## Not held

- Runtime behavior, reliability, or outcomes for any client; the cited evidence is vendor documentation, not a runtime test.
- Precedence or merging across user, project, local, and other scopes beyond what an individual page explicitly says.
```
