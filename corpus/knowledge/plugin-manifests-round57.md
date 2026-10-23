---
source: S079 https://code.claude.com/docs/en/plugins-reference.md; S080 https://developers.openai.com/plugins/build/plugins.md; S081 https://code.visualstudio.com/docs/agents/reference/agent-plugin-reference.md; S082 https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-creating.md; S083 https://geminicli.com/docs/extensions/reference.md; S084 https://cursor.com/docs/plugins.md; S085 https://raw.githubusercontent.com/anomalyco/opencode/bdf757209ff742b8551a4874347edb845241e5bb/services/www/src/docs/content/build/plugins/index.mdx; S086 https://developers.openai.com/plugins/build/plugins.md; S087 https://raw.githubusercontent.com/anomalyco/opencode/bdf757209ff742b8551a4874347edb845241e5bb/services/www/src/docs/content/plugins.mdx; S088 https://cursor.com/docs/reference/plugins.md
verified-at: 2026-10-23
recheck: python3 -B verifiers/check_plugin_manifests.py --rev <rev> --fetch
---

# Plugin manifests by client (round 57)

A skill, agent, command or rule file can reach a client inside a plugin (Gemini CLI: an extension) instead of from the
project tree. Before auditing such a file, find the plugin it came from and its manifest. This entry records, from each
client's own documentation opened on 2026-10-23, where that manifest lives and what a plugin can ship. It is vendor
documentation, not a runtime measurement: no client was run. Where the plugin folder itself sits: Gemini CLI loads
extensions from `<home>/.gemini/extensions` (S083 `extensions-reference.md:106`); either Cursor plugin format can be
developed from `~/.cursor/plugins/local` (S084 `plugins.md:211`); opencode discovers `.opencode/plugins/` and the global
`~/.config/opencode/plugins/` (S087 `plugins.mdx:44-60`).

**Row rule (applied to every row the same way).** The manifest cell leads with the client's own-format manifest path —
a path whose folder or file name names the client — and, where the client documents none, with the default manifest
its page names. Seven clients, one rule: Claude Code, Codex, Gemini CLI and Cursor document an own-format path; VS Code
and Copilot CLI default to the shared Agent Plugins root `plugin.json`; opencode plugins are code modules found by
folder, so its row names the folder (a published package's `package.json` is what its build guide calls a minimal
manifest, S085 `index.mdx:1769-1773`). The rule was fixed when the source seats returned (after the counter was frozen)
and it does not choose between paths to raise a count: VS Code's Legacy OpenPlugin `.plugin/plugin.json` would pass the
counter and is not used (`.ufo/waves/round-57/build/CriticC1Rows.md`, `SrcVSCode.md`), and neither is Copilot CLI's
legacy `.github/plugin/plugin.json`, which meets the counter's token grammar (base row S028) but is neither own-format nor
the default its creation guide names. It is one client-neutral rule among several: a rule that prefers a documented
format-specific path over a shared root default would pick VS Code's `.plugin/plugin.json` and could count five rows
(`.ufo/waves/round-57/a3/falsify/A3CriticMissHonesty.md` § 2, not run).

| Client | Manifest | Source | Quote |
|---|---|---|---|
| Claude Code | `.claude-plugin/plugin.json` | S079 | "Save the manifest at `.claude-plugin/plugin.json` under the plugin root." |
| Codex | `.codex-plugin/plugin.json` | S080 | "The plugin-creator skill will create the plugin folder, create a supported `.codex-plugin/plugin.json` compatibility manifest, and add MCP server wiring for the plugin." |
| VS Code | `plugin.json` | S081 | "A root `plugin.json` that declares the canonical Agent Plugins `$schema` uses Agent Plugins semantics." |
| Copilot CLI | `plugin.json` | S082 | "Choose a plugin format, then add a `plugin.json` manifest file to the root of the directory." |
| Gemini CLI | `gemini-extension.json` | S083 | "Each extension must have a `gemini-extension.json` file in its root directory." |
| Cursor | `.cursor-plugin/plugin.json` | S084 | "plugins with a `.cursor-plugin/plugin.json` manifest, which add rules, agents, commands, hooks, and" |
| opencode | `.opencode/plugins/` | S085 | "Plugins under `.opencode/plugins/` are loaded automatically, like the local example above." |

Quote locations (fetched bytes; first-fetch seat reports under `.ufo/waves/round-57/build/`, re-opened byte-identical by
the falsify seats `.ufo/waves/round-57/a3/falsify/A3ReopenS079.md`–`A3ReopenS085.md`): S079 `plugins-reference.md:34`,
the first sentence of a three-sentence line; S080 `build-plugins.md:135-137` (two line breaks folded to spaces; the
quote is the paragraph's first sentence, ending mid-line 137); S081 `agent-plugin-reference.md:97`, the middle sentence
of a three-sentence line; S082 `plugins-creating.md:27`, step 2 (the list number `2. ` is not quoted); S083
`extensions-reference.md:106-107` (one line break folded; the quote begins mid-line 106, after the load-path sentence,
which is not quoted); S084 `plugins.md:28`, a contiguous substring from `plugins with` through `and` (the list marker
and bold label before it and the `variables` link after it are not quoted); S085 `index.mdx:21`, the first sentence of
the line (the rest of the line is not quoted). No quote has markup stripped inside its span.

## What a plugin can ship

| Client | Instruction-bearing parts a plugin can ship | Source lines |
|---|---|---|
| Claude Code | skills (a root `SKILL.md` loads as a single skill when `skills/` and the `skills` key are both absent), Markdown commands (files or inline bodies) and agents, hooks, MCP and LSP server configurations, MCP-bound message channels, output styles, workflow `.js` files, themes, monitors, `bin/` executables, and `agent`/`subagentStatusLine` defaults; the manifest is optional and other plugin files sit under the plugin root, not inside `.claude-plugin/`; a plugin-root `CLAUDE.md` is not loaded as context (`claude plugin validate` warns), so context instructions go in a skill | S079 `plugins-reference.md:30,34,147-150,216,236-243,514-520,617-629,665` |
| Codex | skills under `skills/` (including an optional onboarding skill selected by `extensions.com.openai.onboardingSkill` when users run setup), MCP servers through `mcp.json` (compatibility scaffold: an optional `.mcp.json` with an initially empty `mcpServers` object) and registered-server mappings through `.app.json`, lifecycle hooks for manually installed Codex desktop plugins, assets; the manifest presentation example holds `extensions.com.openai.interface.defaultPrompt` prompt strings; portable packages put `plugin.json` at the root and `.codex-plugin/plugin.json` stays supported as a compatibility fallback; the scaffold always creates only the manifest | S080 `build-plugins.md:14-30,61-89,608-631,650-676,695-705`; S086 `plugins.md:59-89` |
| VS Code | portable skills and MCP servers; client-specific agents, hooks, automation templates and slash commands; in Agent Plugins 1.0, agents, commands, rules and hooks read from `com.github.copilot` (Claude and Copilot formats keep their own hook files); formats auto-detected (Agent Plugins 1.0 and Copilot root `plugin.json`, Claude `.claude-plugin/plugin.json`, Legacy OpenPlugin `.plugin/plugin.json`) | S081 `agent-plugin-reference.md:11-22,73-85,97-104,306-314,379,392` |
| Copilot CLI | agents, skills, hooks, MCP server configurations; in Agent Plugins 1.0, Copilot-specific agents, commands, rules, hooks and LSP servers come from `com.github.copilot` (legacy plugins can declare component paths such as `commands` and `lspServers` in `plugin.json`) | S082 `plugins-creating.md:14-21,48-71`; S028 `cli-plugin-reference.md:152,207,213,217` |
| Gemini CLI | MCP servers, a context file (`contextFileName`; otherwise root `GEMINI.md` if present), TOML commands, hooks (in `hooks/hooks.json`, not in the manifest), skills, sub-agents (a preview feature), policy rules and safety checkers | S083 `extensions-reference.md:104-112,146-161,229-269` |
| Cursor | Cursor Plugins: rules, skills, agents, commands, MCP servers, hooks, and a `variables` schema for user configuration; Agent Plugins (root `plugin.json`): skills and MCP servers; Cursor Plugins discover `skills/`, `rules/`, `agents/`, `commands/`, `hooks/hooks.json` and `mcp.json` per component only when its manifest field is absent; a root `SKILL.md` is a single-skill fallback only if neither a `skills/` folder nor a manifest `skills` field exists | S084 `plugins.md:9-30,211`; S088 `reference-plugins.md:13-16,65,88-94,112-118,152-166` |
| opencode | JavaScript/TypeScript code can register commands, MCP server configuration, skills and tools; transform existing agents (update/remove/default selection); send session prompts, transient generation requests and synthetic messages; and install runtime hooks that edit incoming prompts and outgoing system instructions; published packages use `package.json` as a minimal manifest | S085 `index.mdx:10-22,223-236,256-262,414-445,618-631,810-816,873-894,971-996,1335-1418,1770-1786`; S087 `plugins.mdx:44-60` |

## Findings

- Four of seven clients document an own-format manifest path (`.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`,
  `gemini-extension.json`, `.cursor-plugin/plugin.json`) — 4 — `python3 -B verifiers/check_plugin_manifests.py --rev
  ac22ca87 --fetch` 2026-10-23 (`.ufo/waves/round-57/C1-measure.txt`). VS Code, Copilot CLI, Codex and Cursor also read
  the shared Agent Plugins root `plugin.json`, so a root `plugin.json` alone does not tell which client a plugin targets.
- One package can serve several clients at once: VS Code reads Claude's format (S081 `:103`), and the host inventory
  found plugins shipping `.claude-plugin`, `.codex-plugin` and `.cursor-plugin` side by side
  (`.ufo/waves/round-57/build/ScoutPluginSweep.md`, host observation, not a documented rule; re-derived 2026-10-23T06:45Z
  in two `~/.cursor/plugins/cache` packages, `.ufo/waves/round-57/a3/falsify/A3ScoutHostPlugins.md`).
- A plugin-shipped MCP server is still a server configuration, so the round-52 `instructions` records apply to it
  unchanged (`corpus/knowledge/mcp-server-instructions-round52.md`); a plugin-shipped agent uses the client's agent
  format from `corpus/knowledge/agent-definition-files-round56.md`, but the client may ignore some keys inside a
  plugin (`.ufo/waves/round-57/build/ScoutPluginMcp.md`, reviewer reading).
- Gemini CLI's context file makes an extension an always-on instruction surface, which the always-on checklist covers
  once the file is found (`corpus/knowledge/alwayson-rule-files-round53.md`).

## Limits

- What `verifiers/check_plugin_manifests.py` checks (Q31): per client, the SKILL.md row token's shape (a `.json` final
  segment carrying `plugin`/`extension`, at least two segments or the client's own name, no dot in a non-final segment
  except as its first character, no `marketplace`, no other client's name, and no token shared by two client rows), the
  entry row's manifest cell equal to that token, a 6–25-word quote that
  holds the token and a plugin/extension word outside it, a new tier-A `mined` SOURCES row opened 2026-10-23 on the
  client's pinned host that is not a base URL or a change note, the quote in `corpus/lessons/round-57.md` § Gate, and
  with `--fetch` the quote and the token on the live page; new ground counts tokens held nowhere in the base tree
  outside `.ufo/`. It does not check the `What a plugin can ship` cells, the row rule above, or whether a client loads
  a plugin as documented; those are reviewer judgment. "Where the client documents none" for VS Code and Copilot CLI is
  a reading of S081 `agent-plugin-reference.md:99-104` and S028 `cli-plugin-reference.md:402`, which list no
  client-named path; the Q30 three-part sweep was not run for those two clients, so it is not a silence claim.
- Copilot CLI's legacy manifest locations are listed on the CLI plugin reference page, which is base row S028; this
  entry cites S028 only for component fields (`cli-plugin-reference.md:152,207,213,217`), never as a counted manifest
  source.
- opencode: the row names the discovery folder because a local plugin is a code module found by folder; a published
  package's `package.json` is the file the pinned build guide calls a minimal manifest (S085 `index.mdx:1769-1773`). The
  counter does not count either (a folder token and a `package.json` name both fail its grammar).
- omp, this host's harness, also reads plugin manifests (`.omp-plugin/plugin.json`, then `.claude-plugin/plugin.json`);
  that is binary evidence (`ScoutPluginSweep.md`), not a documented source, and omp is not one of the seven rows.
