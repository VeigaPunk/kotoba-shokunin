Result: DONE — Drafted the requested 13-line section from the six eligible client censuses and the opencode exclusion; no product file was edited.

## Exact section text

```markdown
### Hook files by client
For a rule whose action must run at a documented client event, use that client's hook; these pages describe event-triggered actions, not a general hook-over-prompt/skill rule (basis: `corpus/knowledge/hook-files-round59.md`, S096–S101). Host package/initramfs hooks are tsukuroi's, not this table.

| Client | Hook config | Events | Action |
|---|---|---|---|
| Claude Code | `.claude/settings.json` | `PreToolUse`, `PostToolUse` | Run a project script before each Bash; block the command on failure. |
| Codex | `~/.codex/hooks.json` | `PreToolUse`, `SessionStart` | Run commands or MCP tools at lifecycle events. |
| VS Code | `.github/hooks/audit.json` | `sessionStart`, `preToolUse` | Configure command hooks for agent events. |
| Copilot CLI | `~/.copilot/hooks/*.json` | `sessionStart`, `preToolUse` | Configure personal hooks for CLI events. |
| Gemini CLI | `.gemini/settings.json` | `BeforeTool`, `AfterModel` | Define project hooks for tool and model events. |
| Cursor | `.cursor/hooks.json` | `preToolUse`, `postToolUse` | Run command-based hooks during cloud-agent work. |
| opencode | — (plugin code only) | `tool.execute.before`, `tool.execute.after` | Register event hooks in plugin modules; no dedicated hook file. |

```
The block is 13 lines including its final blank line; every row is under 400 characters. Event identifiers and hook locations come from the respective W0 census reports: `CensusClaudeCode.md:7-39`, `CensusCodex.md:23-59`, `CensusVSCode.md:7-49`, `CensusCopilotCLI.md:9-39`, `CensusGeminiCLI.md:9-48`, `CensusCursor.md:21-65`, and `Censusopencode.md:40-68`. The opencode row intentionally shows no standalone hook config; the census says its hook code is in plugin folders and those paths are ineligible under the frozen segment rule. No S102 support row is requested for that excluded row.

## Gates and provenance

- Read the frozen spec before drafting: `verifiers/check_hook_files.py:12-21` describes the depth claim and `:52-74` / `:112-136` specify row, event, source and snapshot checks. `TARGET=4`, `NEW_TARGET=5` are at `:253-254`; counter sha256 recorded in the controls is `f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71`.
- Read required controls `CtlFabEvents.md` and `CtlFabSnapshot.md`, plus `controls/SUMMARY.md`. The summary records all eight controls as predicate NOT MET (`SUMMARY.md:7-20`). These are read receipts, not runs by this seat.
- No counter, build, test, fetch, or product-code execution was run for this draft. No tools were installed or updated.
- The read of the requested knowledge entry path returned “not found”; S096–S101 and quote/event details were therefore cross-referenced to the supplied W0 census/control artifacts. Their presence and exact committed state at the future measured revision remain for integration to establish.
- At the freeze SKILL.md was 597 lines (assignment context). This 13-line addition requires at least 10 verbatim lines moved out to keep the 600-line cap; `ExecBudgetMove` remains the integrator's responsibility.

## Touched surfaces and scope

Only this report is written: `.ufo/waves/round-59/build/ScribeSkillSection.md`. No lane source, SKILL.md, corpus, snapshot, counter, or Git/jj state was modified. No sources were fetched; no citations, snapshots, or integration state are asserted as committed by this seat.

## Finding — census/control conflict (verbatim)

`CensusVSCode.md:1` says: `Result: DONE — VS Code: ELIGIBLE .github/hooks/audit.json`

`CensusVSCode.md:3` says: `The repository discovery pattern .github/hooks/*.json also passes the path grammar, but Copilot CLI's hooks reference prints that same token, so a Copilot row that leads with it is E5 (both rows out).`

But `CtlFabEvents.md:64-72` labels the different path as its census token:

```text
| VS Code | .github/hooks/*.json | afterToolSettle, BeforeHookRun |
```

Draft uses the census report's eligible token `.github/hooks/audit.json`, not the conflicting control-world token. The control receipt's remaining fabricated events are not used.

## Commands and output

No shell command or verifier was run before writing this report. The required post-write command is run once after writing; its exact command and output are included in the handoff message.