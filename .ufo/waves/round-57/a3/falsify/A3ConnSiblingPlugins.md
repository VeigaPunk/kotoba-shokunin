Result: HOLDS — sibling lanes record no contradiction of `corpus/knowledge/plugin-manifests-round57.md` at `07c33d73ddce769d9cea2846a6313164401b5478`; two independent runtime observations agree with its Claude Code and Codex manifest paths, and the remaining sibling facts are a global-vs-project opencode path nuance plus an out-of-scope Kimi manifest family.

# Question

Adjacency check (route, never fix): do sibling lanes (`/home/vgpnk/Projects/shokunin/*-shokunin`, read-only) record plugin or extension manifest facts that agree with or contradict `corpus/knowledge/plugin-manifests-round57.md` at `07c33d73ddce769d9cea2846a6313164401b5478`? Search terms (exact strings from the task): `.claude-plugin`, `.codex-plugin`, `.cursor-plugin`, `gemini-extension.json`, `plugin.json`, `.opencode/plugins`.

# Method

Commands (run 2026-10-23, read-only; `--exclude-dir=.git/scratch/clone/worktrees/live` where noted):

- `grep -rn --exclude-dir=.git --exclude-dir=scratch --exclude-dir=clone --exclude-dir=worktrees --exclude-dir=live '\.claude-plugin' /home/vgpnk/Projects/shokunin/*-shokunin` (excluding `kotoba-shokunin`) → hits only in `game-dev-3d-shokunin` (unreal-mcp vendored upstream) and `kagi-shokunin` cached HTML (no manifest fact).
- `grep -rn ... '\.codex-plugin' ...` → one substantive hit: `kaidoku-shokunin/.ufo/waves/round-20/w1/ScoutWasmCarriers.md:46`.
- `grep -rn ... '\.cursor-plugin' ...` → no hits outside `kotoba-shokunin` (the `.cursor-plugin` evidence in this lane's own `A3ScoutHostPlugins.md` is in-lane, not a sibling).
- `grep -rn ... 'gemini-extension\.json' ...` and `grep -rn ... 'gemini-extension' ...` → no hits.
- `grep -rn ... '\.opencode/plugins' ...` (corpus scope) → no hits.
- `grep -rn ... 'plugin\.json' ... | grep -i manifest` → Kimi `kimi.plugin.json` facts (kumitate, tabi) plus kaidoku's `.codex-plugin` citation; no VS Code/Copilot/Gemini/Cursor client-manifest facts.
- `grep -rn ... 'plugin manifest' ...` → `game-dev-3d-shokunin` (unreal-mcp) and `kumitate-shokunin/corpus/knowledge/kimi-skills-plugins.md`.

# Agreements

1. **Claude Code — `.claude-plugin/plugin.json`** (kotoba row, S079). Sibling lane `game-dev-3d-shokunin` treats `.claude-plugin/plugin.json` as the Claude Code plugin manifest of its vendored upstream Unreal MCP plugin:
   - `game-dev-3d-shokunin/corpus/knowledge/unreal-mcp/README.md:145` — "**`.claude-plugin/plugin.json`** — plugin manifest, name"
   - `game-dev-3d-shokunin/corpus/knowledge/unreal-mcp/PROVENANCE.md:27` — "plugin version | `3.1.1` | `jq -r .version upstream/.claude-plugin/plugin.json`"
   - `game-dev-3d-shokunin/corpus/knowledge/unreal-mcp/adaptation-kimi.md:41` — "`.claude-plugin/plugin.json` manifest" (mapped onto Kimi's `kimi.plugin.json`).
   Agreement in path shape; scope is one vendored plugin, not a client-doc rule.

2. **Codex — `.codex-plugin/plugin.json`** (kotoba row, S080). Sibling lane `kaidoku-shokunin` observes ChatGPT's bundled plugins carrying `.codex-plugin/plugin.json`:
   - `kaidoku-shokunin/.ufo/waves/round-20/w1/ScoutWasmCarriers.md:46` — "plugins `browser`/`chrome` version `26.1013.40934` (`.../plugins/browser/.codex-plugin/plugin.json:2-3`, `.../plugins/chrome/.codex-plugin/plugin.json:2,55`)".
   Runtime observation agrees with the documented Codex manifest path; it is not a documentation citation.

# Contradictions / nuances (none blocking; all scoped)

1. **opencode path shape (nuance, not a contradiction).** Kotoba row (S085) records project-local plugins under `.opencode/plugins/` (plural) as auto-loaded, with no JSON manifest. Sibling lane `kagi-shokunin` records the *global* opencode plugin surface instead:
   - `kagi-shokunin/corpus/knowledge/adjacency-breadth.md:55` — "opencode: `opencode.json`, `agents/`, `plugin/`, `tools/`;"
   - `kagi-shokunin/corpus/knowledge/config-layering.md:18` — global `~/.config/opencode/opencode.json` "supplies … plugins"
   - `kagi-shokunin/corpus/knowledge/handler-trust-boundary.md:7` — "`~/.config/opencode/plugin/fnm-nudge.js`"
   These are global XDG paths (`~/.config/opencode/plugin/`, singular) versus kotoba's project-tree path (`.opencode/plugins/`, plural). They describe different surfaces and do not assert a JSON manifest for opencode, so they neither corroborate nor refute the S085 token. No sibling lane records a project-local `.opencode/plugins/` fact. Routed for awareness only; no entry change proposed.

2. **Kimi manifest family (out of scope, not a contradiction).** `kumitate-shokunin` and `tabi-shokunin` record Kimi's own plugin manifest `kimi.plugin.json` (an eighth client not among kotoba's seven rows, which also excludes omp, noted in § Limits of the entry):
   - `kumitate-shokunin/corpus/knowledge/kimi-skills-plugins.md:277` — managed plugin root carries `kimi.plugin.json:4` with version `1.11.3`
   - `kumitate-shokunin/corpus/knowledge/kimi-skills-plugins.md:381` — "`~/.kimi-code/plugins/managed/kimi-webbridge/kimi.plugin.json` (the plugin's own manifest, distinct from `~/.kimi-code/plugins/installed.json`)"
   - `kumitate-shokunin/corpus/knowledge/kimi-skills-plugins.md:415` — "Manifest | **none** — `SKILL.md` is the whole contract | `~/.kimi-code/plugins/managed/kimi-webbridge/kimi.plugin.json` (own schema URL) **plus** registry row in `~/.kimi-code/plugins/installed.json`"
   - `tabi-shokunin/corpus/knowledge/webbridge-plugin-anatomy.md:57` — "Version consistency: manifest `1.11.3` (kimi.plugin.json:4)"
   - `tabi-shokunin/corpus/knowledge/browser-surface-census.md:116` — "Manifest: `~/.kimi-code/plugins/managed/kimi-webbridge/kimi.plugin.json:3` name"
   - `tabi-shokunin/corpus/knowledge/webbridge-daemon-disposition.md:29` — "`kimi.plugin.json` (manifest; `"version": "1.11.3"`, :3)"
   This is additional evidence for a client outside the entry's seven-row scope; it does not contradict any row.

# What is absent (negative results)

- No sibling lane records facts about `gemini-extension.json`, `.cursor-plugin`, or `.codex-plugin` as a client manifest *rule* (only the runtime observation above for Codex).
- No sibling lane records VS Code (`plugin.json` shared root) or Copilot CLI manifest facts.
- No sibling lane records opencode having a JSON manifest; kagi's facts are JS plugin files, consistent with kotoba's "no JSON manifest" statement.

# Route

No lane file edit proposed. If the L1 wants the opencode global-vs-project nuance or the Kimi manifest family reflected in `plugin-manifests-round57.md`, that is a content decision for the source seats (S085 re-open / a new source row), not an adjacency fix. This report is the adjacency finding.

# Limits

- Searched sibling lanes' corpora and `.ufo/waves` (excluding `.git`, scratch, clone, worktrees, live HTML) for the six exact strings plus `plugin manifest` / `gemini-extension`. Cached HTML mirrors and interactive-session JSONL were not exhaustively line-read; only grep hits were inspected.
- No sibling lane file was edited. No tool installed. Read-only lane access only.