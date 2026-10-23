Result: DONE — no sibling-lane corpus contradicts the census; kotoba's own corpus has adjacent hook statements that the new section must keep scoped (plugin-bundled `hooks/hooks.json`, the `.claude/hooks` executable surface, and opencode's chat-transform hook), none of which conflicts with the client-config rows once scope is stated.

## Method

Searched every sibling lane (`/home/vgpnk/Projects/shokunin/*-shokunin` except `kotoba-shokunin`, read-only) under its `corpus/` for the census path tokens and client hook event names: `.claude/settings`, `codex/hooks`, `.github/hooks`, `.copilot/hooks`, `.gemini/settings`, `.cursor/hooks`, `hooks.json`, `PreToolUse`, `PostToolUse`, `SessionStart`, `UserPromptSubmit`, `SubagentStop`, `BeforeTool`, `AfterModel`. Also searched kotoba's `corpus/` and `SKILL.md` for hook references. Evidence below cites file:line and the last commit touching that file (or working-tree status for uncommitted files).

## Sibling lanes

- **No contradiction found** for Codex, VS Code, Copilot CLI, Gemini CLI, Cursor, or opencode: no sibling corpus outside game-dev-3d names any of those clients' hook config paths or events.
- `game-dev-3d-shokunin` is the only sibling lane whose corpus touches Claude Code hook surfaces, and it does **not** contradict the census:
  - `game-dev-3d-shokunin/corpus/knowledge/unreal-mcp/upstream/README.md:25` (commit `366bb02f87a2557d54bc5c5e4d817c45ccf67a9a`): "The `SessionStart` hook is a bash script (`hooks/unreal-context.sh`) invoked by `hooks/hooks.json` as `bash ${CLAUDE_PLUGIN_ROOT}/hooks/unreal-context.sh`." This is a **plugin-bundled** hook (`hooks/hooks.json` at the plugin root), not Claude Code's client hook config file; it is the same scope as kotoba's Plugin manifests table (`corpus/knowledge/plugin-manifests-round57.md:54`).
  - `game-dev-3d-shokunin/corpus/knowledge/unreal-mcp/upstream/README.md:50` (same commit): "Commit this to `.claude/settings.json` in the project that should use the plugin." This concerns `enabledPlugins`, not hooks; consistent with the census row that Claude Code's hook config lives in `.claude/settings.json`.
  - `game-dev-3d-shokunin/corpus/knowledge/unreal-mcp/adaptation-kimi.md:34-36,42` (commit `830095a7220e0be8b9a7eba50f85cbe86fbab08a`): maps the Claude plugin's `hooks.json` + `SessionStart` to kimi's `[[hooks]]` in `config.toml`; records that kimi has no `.claude/settings.json` surface at all. This is kimi-scope and does not assert a Claude Code client hook location.
- `kumitate-shokunin` (sibling) documents omp's own hook files, not a census client:
  - `kumitate-shokunin/corpus/knowledge/kimi-modes-machinery.md:148,152,423,485` (commit `364f1d5954158ef8844bca4a5fef57b05d2f2ca5`): `.omp/hooks/pre/ufo-godspeed-inject.js`, project-scoped (`<cwd>/.omp/hooks/pre/`), plus `primeagent-assimilation.js` and `ufo-l0-monitor.js`. omp is not a census client, so this is adjacent only: it must not be read as a missing client row, and the new section's "Hook files by client" must not be mistaken for an exhaustive list of all hook mechanisms on the host.

## Kotoba's own corpus the new section must agree with

1. Plugin manifests table — `corpus/knowledge/plugin-manifests-round57.md` (commit `bc09a8307f253fafca3f1461bcc45627d7b6eea7`):
   - Line 54 (Claude Code): plugin ships "hooks" as a component.
   - Line 55 (Codex): "lifecycle hooks for manually installed Codex desktop plugins".
   - Line 56 (VS Code): "agents, commands, rules and hooks read from `com.github.copilot` (Claude and Copilot formats keep their own hook files)".
   - Line 57 (Copilot CLI): "agents, skills, hooks, MCP server configurations".
   - Line 58 (Gemini CLI): "hooks (in `hooks/hooks.json`, not in the manifest)".
   - Line 59 (Cursor): "hooks, and a `variables` schema"; "Cursor Plugins discover … `hooks/hooks.json` … per component only when its manifest field is absent".
   - Line 60 (opencode): "install runtime hooks that edit incoming prompts and outgoing system instructions".
   These are **plugin-bundled** hook surfaces. The new section's rows are **client hook-config files** (`.claude/settings.json`, `~/.codex/hooks.json`, `.github/hooks/*.json`, `~/.copilot/hooks/*.json`, `.gemini/settings.json`, `.cursor/hooks.json`). They do not contradict, but the two scopes must be distinguished or a reader will conflate Gemini's plugin `hooks/hooks.json` with its project `.gemini/settings.json` (and Claude's plugin hooks with `.claude/settings.json`).

2. Executable-surface census — `corpus/knowledge/instruction-surface-census-round13.md:265` (commit `e792607e85c78998bbf0ae4e2b5d350683eec0f7`): "`omp:discovery/extensions` … Extension/hook/tool module roots (`.gemini/extensions`, `.codex/tools`, `.claude/hooks`) — executable surfaces, out of prompt-craft province." This names `.claude/hooks` as an executable root discovered by omp, distinct from `.claude/settings.json` hook config. The new section's Claude row must not be read as saying `.claude/hooks` does not exist; it only says the client's hook config file is `.claude/settings.json`.

3. opencode chat-transform hook — `corpus/knowledge/instruction-surface-census-round13.md:283` (same commit): "the plugin `experimental.chat.system.transform` hook" is a non-file prompt surface. The new section's opencode row (`SKILL.md` `### Hook files by client`, opencode row, events `execute.before`, `execute.after`) lists tool-execution events only. These are different hook subsets of the same plugin module; not contradictory, but the row should not imply opencode hooks are only tool-execution hooks, or the plugin-manifests cell and census row should be cross-referenced.

4. `SKILL.md` already carries the new section in the working tree (uncommitted, on top of freeze commit `4b2125c91ea1868a83b7b28eb4bbbacc35f469fe`; `corpus/knowledge/hook-files-round59.md` is also untracked). The section's table header `| Client | Hook config | Events | Action |` and its rows match the census paths; no change needed to the paths themselves.

## Affected axes

- Adjacency / consistency: the new section stays consistent with the census paths and with kotoba's own plugin-manifests and instruction-surface rows, provided scope (client config file vs. plugin-bundled hook file vs. omp executable root) is stated.
- No axis is harmed by the census rows themselves; the only risk is a reader conflating scopes, which is a documentation adjacency issue, not a data contradiction.

## Proposed move

No factual correction to the census is required. Add a one-line scope note to `corpus/knowledge/hook-files-round59.md` (and optionally the SKILL.md section) stating that the rows name each client's hook **config file**; plugin-bundled hooks live in the plugin's `hooks/hooks.json` (per `corpus/knowledge/plugin-manifests-round57.md:54-59`) and omp's own hooks live under `.omp/hooks/` (sibling lane kumitate), and that `.claude/hooks` is an executable root discovered by omp (`instruction-surface-census-round13.md:265`), not the config file. No row path or event should change.

## Risks

- If the scope note is omitted, a falsifier could read the Gemini row as denying `hooks/hooks.json` in extensions, or the Claude row as denying `.claude/hooks` as an executable root, producing a false contradiction with `plugin-manifests-round57.md` and `instruction-surface-census-round13.md`.
- If the opencode row is read as the complete hook vocabulary, it would understate the prompt-transform hook documented in `instruction-surface-census-round13.md:283` and the plugin-manifests cell at `plugin-manifests-round57.md:60`.

## Verification

- Sibling-lane search: `for d in $(ls -d *-shokunin | grep -v kotoba); do grep -rn -i 'hook' "$d/corpus" …` for client path/event tokens returned no matches except `game-dev-3d-shokunin` (plugin scope, cited above) and `kumitate-shokunin` (omp scope, cited above).
- Kotoba citations verified by `nl -ba` on the cited files at the commits listed. Working-tree status confirmed `SKILL.md`, `corpus/README.md`, `corpus/SOURCES.md` modified and `corpus/knowledge/hook-files-round59.md` untracked in `kotoba-shokunin` (HEAD `283124cd52af465734954c887ccd67f73ddb9fd8`).
