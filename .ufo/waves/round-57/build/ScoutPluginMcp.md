Result: DONE — for six of seven clients the plugin docs name a manifest path that satisfies C1 v2 and which held surfaces a plugin can ship; Copilot CLI's only manifest path is on a page already cited at base (S028), so its row cannot be backed under v2 and C1 sits at exactly F=5.

# Scout: plugin manifests and the held surfaces a plugin ships

Seat `KotobaR57.ScoutPluginMcp`, round 57 build wave, 2026-10-23. Lane repo read-only; no writes outside this
report; no install needed (nothing installed, nothing upgraded). Scratch copies of fetched pages:
`/fast/scratch/hyaku/kotoba-r57/ScoutPluginMcp/pages/` (29 files); quote checks in
`/fast/scratch/hyaku/kotoba-r57/ScoutPluginMcp/quotecheck.py`.

Bounds note: no sandbox world was needed. Nothing here executes lane code; every fetch is an ordinary
`curl -sSL --max-time 30` (no browser, no challenge bypass). Base token test was read-only
`git --no-optional-locks grep -F -i -o <token> 47c05558 -- . ':!.ufo'`.

## 1. Fetch receipts (status, bytes, sha256 of the exact bytes saved)

All times are the `date -u` line pasted before the batch; one batch may cover several URLs.
`curl -sSL --max-time 30 -o <file> -w '%{http_code} %{size_download}'`.

| # | URL | UTC | status | bytes | sha256 |
|---|---|---|---|---|---|
| 1 | https://code.claude.com/docs/en/plugins-reference.md | 2026-10-23T04:47:00Z | 200 | 42124 | `f2910dd6020f5448e5d8c9a8c3b5af7b31b7222d247c20b25f44a712b805916e` |
| 2 | https://code.claude.com/docs/en/plugins/components.md | 2026-10-23T04:47:48Z | 200 | 38390 | `2b5c47b750e4c09e97d8abb992a8e9b690d1ae7d63d477b458a363eb8a1beb0a` |
| 3 | https://code.claude.com/docs/en/mcp.md | 2026-10-23T04:49:08Z | 200 | 130411 | `f8df5bcff278cb6bb995a1316156deef019577047fcb559131279fade1c3804d` |
| 4 | https://developers.openai.com/plugins/build/plugins.md | 2026-10-23T04:47:48Z | 200 | 38036 | `c37e330df8f040df8ee2f48035992b37c6a7decf6c3f5640822ca0907118c4e1` |
| 5 | https://developers.openai.com/codex/plugins.md | 2026-10-23T04:47:00Z | 200 | 14241 | `612ebfed2779c4aa5c412d8b069ed723e8c2ea264a140ebed5ad52a0853d4db0` |
| 6 | https://code.visualstudio.com/docs/agents/reference/agent-plugin-reference.md | 2026-10-23T04:47:31Z | 200 | 21972 | `d6e10328d582db6210fcccc453947d8140ff08a41c31170c4c90816578a44f9e` |
| 7 | https://code.visualstudio.com/docs/agent-customization/agent-plugins.md | 2026-10-23T04:47:09Z | 200 | 16711 | `b717e6f2bf05db2e161ffef8fe82d1002ccea452c7a45d91dc95d7505153757e` |
| 8 | https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference.md | 2026-10-23T04:47:26Z | 200 | 47200 | `d0d362cc5aa2ef84775145e499596c7e6529531c7b29972ae29f547b5da220d0` |
| 9 | https://docs.github.com/en/copilot/concepts/agents/about-plugins | 2026-10-23T04:49:45Z | 200 | 613014 | HTML, grep only |
| 10 | https://geminicli.com/docs/extensions/reference.md | 2026-10-23T04:47:00Z | 200 | 12022 | `8b9eecb254df04220b23d56da6d63018abe7c5364122af7dee16b05d63b1fe72` |
| 11 | https://geminicli.com/docs/core/subagents.md | 2026-10-23T04:49:45Z | 200 | 23614 | `4b9baa88628b0a2bdaea87dc6b9a5c5dd2d998274ba9a93cc6ed23c53b8ee2db` |
| 12 | https://cursor.com/docs/plugins.md | 2026-10-23T04:47:00Z | 200 | 20323 | `74387ff95205965ca3060fac4d12966fea7b1525cc0e972e6f265bbee591cb62` |
| 13 | https://cursor.com/docs/reference/plugins.md | 2026-10-23T04:47:48Z | 200 | 30324 | `3bbf36f3320382adb68509aa758e2e764fd31c5de5f5c70c6af1683497b11204` |
| 14 | https://opencode.ai/docs/plugins.md | 2026-10-23T04:47:00Z | 200 | 9357 | `c76613823185b6bf7f6a164211bcdc7bba3bc738aba1cc927b51189f8da8681e` |

404s probed and rejected (all ordinary curl): `code.visualstudio.com/docs/copilot/customization/agent-plugins.md`
(9 B), `.../copilot/customization/overview.md` (9 B), `docs.github.com/.../customize-copilot/plugins.md`,
`.../concepts/agents/copilot-cli/plugins.md`, `.../how-tos/copilot-cli/use-plugins.md`,
`.../customize-copilot/use-plugins.md`, `.../concepts/plugins.md`, `.../concepts/agents/about-plugins.md`,
`.../concepts/agents/copilot-cli/about-plugins.md` (all 502-byte 404 body),
`raw.githubusercontent.com/github/copilot-cli/main/docs/plugins.md` (14 B), and
`api.github.com/repos/github/copilot-cli/contents/docs` (404 — the CLI repo has no `docs/` directory).

Line numbers below are 1-based lines of the saved bytes.

## 2. Comparison table — what a plugin can ship (per client, with locations)

Each cell names the documented plugin location and the saved-bytes line; "same shape" means the plugin uses the
documented standalone format.

| Client | MCP server config in a plugin | Skills folder | Agents folder | Commands | Hooks | Context file | Source lines |
|---|---|---|---|---|---|---|---|
| Claude Code | `.mcp.json` at plugin root, "same shape as a project `.mcp.json`" (`components.md:381`, `mcp.md:466-479`); or inline/`mcpServers` key (`plugins-reference.md:151-152, 303-313`) | `skills/<name>/SKILL.md` (`plugins-reference.md:618`; `components.md:59,224-232`); root `SKILL.md` = single skill (`components.md:253`) | `agents/*.md`, subfolders are part of the name (`plugins-reference.md:620`; `components.md:295-319`) | `commands/*.md` (`plugins-reference.md:619`; `components.md:269`) | `hooks/hooks.json` (`plugins-reference.md:621`; `components.md:333`) | **none** — `CLAUDE.md` at plugin root is not loaded and validate warns (`plugins-reference.md:665`; `components.md:255`) | 42124 B |
| Codex | root `mcp.json` (Agent Plugins schema; transport `type` per server) (`build/plugins.md:707-726`); compat `.mcp.json` (`:66-80`) | `skills/` (`build/plugins.md:18, 655`) | **no plugin agent surface documented** | **none documented** | `hooks/hooks.json`, manually installed Codex desktop only (`build/plugins.md:21-22, 82-84, 703`) | none documented | 38036 B |
| VS Code | `mcp.json` (Agent Plugins) or `.mcp.json` (Copilot format) at plugin root, auto-discovered (`agent-plugin-reference.md:209-240`) | `skills/` (`:71`; layout `:26-30`) | `com.github.copilot/agents/` (`:81`; example `:36-39`) | `com.github.copilot/commands/` (`:82`) | `com.github.copilot/hooks/hooks.json` (`:84-85`; `:296-300`) | none documented | 21972 B |
| Copilot CLI | Agent Plugins: root `mcp.json` with matching `$schema` (`cli-plugin-reference.md:146-150`); legacy: `.mcp.json`, `.github/mcp.json`, or `mcpServers` field (`:407`) | `skills/` only, no root-`SKILL.md` fallback (`:145-148, 405`) | `com.github.copilot/agents/` (`:158`) or legacy `agents/` with `.agent.md` files (`:211, 404`) | `com.github.copilot/commands/` (`:159`), legacy `commands` path field (`:213`) | `com.github.copilot/hooks/hooks.json` (`:161`), legacy `hooks.json` or `hooks/hooks.json` (`:406`) | none documented | 47200 B |
| Gemini CLI | `mcpServers` map in `gemini-extension.json`, loaded "just like" `settings.json` servers, `trust` unsupported (`extensions/reference.md:146-151`) | `skills/<name>/SKILL.md` (`:248-250`) | `agents/*.md` in extension root (`:258-259`); subagents page: `name` and `description` required (`core/subagents.md:362-368, 583-587`) | `commands/*.toml` (`:231-238`) | `hooks/hooks.json` inside the extension, not in the manifest (`:242-244`) | **`contextFileName`** in the manifest; defaults to `GEMINI.md` if present (`extensions/reference.md:158-161`) | 12022 B |
| Cursor | `mcp.json` at plugin root (`reference/plugins.md:163`); manifest `mcpServers` overrides discovery (`:93`) | `skills/` (`:46, 158`); root `SKILL.md` = single-skill plugin (`:164`) | `agents/` (`.md/.mdc/.markdown`) (`:49, 160`) | `commands/` (`:51, 161`) | `hooks/hooks.json` (`:53, 162`) | none documented | 30324 B |
| opencode | **no plugin manifest or plugin MCP file** — plugins are code modules (`.opencode/plugins/`, `~/.config/opencode/plugins/`, npm via `opencode.json` `plugin` array) that export hooks (`plugins.md:15-32, 64-65`) | none via plugins | none via plugins | none via plugins | code hooks only (same page) | none | 9357 B |

## 3. Manifest token, quote and base-URL test for the C1 table (evidence for the scribe)

Counter rules read from `verifiers/check_plugin_manifests.py` v2 (`:225-247` hosts/markers, `:535-565`
token grammar, `:646-707` entry verdict, `:461-490` URL keys). Verified with an independent reimplementation of
`page_plain` + `PLUGIN_WORD_RE` + token span over the saved bytes (`quotecheck.py`, all listed below `present=True`,
`token_at_boundary=True`, `plugin_word_outside=True`).

| Client | SKILL.md token (= entry `Manifest` cell) | S### | URL | Quote (verbatim; lines of the saved bytes) | words | base-URL? | held at base? |
|---|---|---|---|---|---|---|---|
| Claude Code | `.claude-plugin/plugin.json` | S079 | https://code.claude.com/docs/en/plugins-reference.md | "Save the manifest at `.claude-plugin/plugin.json` under the plugin root." (`:34`) | 9 | no | 0 |
| Codex | `.codex-plugin/plugin.json` | S080 | https://developers.openai.com/plugins/build/plugins.md | "Put OpenAI-specific presentation, registered MCP server mappings, and hook settings under `extensions.com.openai` in root `plugin.json`. Existing `.codex-plugin/plugin.json` files remain supported as a compatibility fallback." (`:24-26`) | 24 | no | 0 |
| VS Code | `.plugin/plugin.json` | S081 | https://code.visualstudio.com/docs/agents/reference/agent-plugin-reference.md | "\| Claude \| `.claude-plugin/plugin.json` \| \| Legacy OpenPlugin \| `.plugin/plugin.json` \|" (`:103-104`) | 11 | no | 0 |
| Copilot CLI | `.github/plugin/plugin.json` | — | (only on https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference, `:402`) | "Legacy plugins: `.plugin/plugin.json`, `plugin.json`, `.github/plugin/plugin.json`, or `.claude-plugin/plugin.json` (checked in this order)." (`:402`) | 11 | **YES — S028** | 0 |
| Gemini CLI | `gemini-extension.json` | S083 | https://geminicli.com/docs/extensions/reference.md | "Each extension must have a `gemini-extension.json` file in its root directory." (`:106-107`) | 11 | no | 0 |
| Cursor | `.cursor-plugin/plugin.json` | S084 | https://cursor.com/docs/reference/plugins.md | "Every Cursor Plugin requires a `.cursor-plugin/plugin.json` manifest file." (`:65`) | 8 | no | 0 |
| opencode | none — code module, no `.json` manifest | — | — | — | — | — | — |

Base-token check (read-only, base `47c05558`): every token above returns `held-count=0`
(`git --no-optional-locks grep -F -i -o -- <token> 47c05558 -- . ':!.ufo' | wc -l`), so new ground is 5 distinct
tokens with the rows as listed (6 if a Copilot token ever backs).

**Copilot CLI is the hard limit.** Its four legacy manifest locations and `.github/plugin/plugin.json` appear only
on `cli-plugin-reference.md:402`, and that page is base row S028's source. `url_key` drops a trailing `.md`
(`check_plugin_manifests.py:461-479`), so citing the `.md` route normalises back to S028's URL key and
`entry_row_verdict` rejects it as "already a base SOURCES URL" (`:697-698`). No other pinned Copilot page holds the
literal: `plugins-creating.md:14,75` says only "additional manifest locations" and names `plugin.json`;
`about-plugins` (HTML) names `plugin.json` and "additional manifest locations" but not the path; the CLI repo has no
`docs/`. Consequences for C1: F = 5 of K = 6 (predicate needs F ≥ 5, G ≥ 3) — no slack. If a sixth backed row is
wanted, the only honest route is a new client-specific manifest page published on a pinned host, which does not
exist today.

**Scribe guardrails (from the counter source, verified against the fetched pages).**
- Never put `.plugin/plugin.json` on the Copilot CLI row: a token on two client rows disqualifies both
  (`check_plugin_manifests.py:720, 746-749`), and VS Code needs it.
- A bare `plugin.json` on any row is not well-formed (one segment, no client marker; `:535-565`) — it would leave
  that row out of K but also unbacked.
- Entry `Manifest` cell must be exactly the SKILL.md token, case-sensitive (`:656-658`); quotes go into
  `corpus/lessons/round-57.md` § Gate verbatim (whitespace-normalised, `:675-676`).
- Ids per the row order above: S079 Claude Code, S080 Codex, S081 VS Code, S082 Copilot CLI (no URL can back it),
  S083 Gemini CLI, S084 Cursor, S085 opencode.
- The Cursor row must cite `https://cursor.com/docs/reference/plugins.md` (the 8-word quote is there); the overview
  page `cursor.com/docs/plugins.md` holds a different, 17-word sentence at `:207-208` that also passes.
- New ground: no candidate URL above appears in base `corpus/SOURCES.md` except the Copilot reference
  (per-URL `git grep -c -F` at `47c05558` returned no lines for the other six).

**VS Code quote caveat.** `.plugin/plugin.json` appears in a format table only, and the single row
"`| Legacy OpenPlugin | .plugin/plugin.json |`" has no `plugin`/`extension` word outside the token ("OpenPlugin"
does not match `\bplugin\b`). The quote therefore has to span rows 103-104 and carries Claude's token inside the
quote text. That passes the counter's quote rules (verified) but reads as a two-row citation; a reviewer should see
it as such.

**Codex quote caveat.** The 24-word quote deliberately includes "root `plugin.json`" (28 words if extended); the
24-word form is the longest safe slice (`MAX_WORDS = 25`).

## 4. Does a plugin-shipped skill/agent follow the held rules?

Held rows referred to: `corpus/knowledge/agent-definition-files-round56.md` (S072–S078) and
`corpus/knowledge/mcp-server-instructions-round52.md` (S033–S036, S041, S042).

1. **Agent format is the same; the location and the name are not.** Claude Code plugin agents are Markdown files
   under `agents/` (same schema as `.claude/agents/`, S072/S026) but the name is scoped
   `my-plugin:review:security` from plugin + subfolders + file (`components.md:295-319`), and a missing or
   >256-character `name` falls back to the file name (`components.md:326`). Cursor plugin agents are found in
   `agents/` and "require YAML frontmatter" with `name` and `description` (`reference/plugins.md:236-265`), while
   the held standalone row records all five keys as optional with the name derived from the file name (S077) —
   a documented difference between the two Cursor surfaces, not a measured load behaviour. Gemini extension agents
   are `.md` under `agents/` (`extensions/reference.md:258-259`) and the subagents page keeps `name` and
   `description` required (`core/subagents.md:362-368`), matching the held S076 rules; the page states extensions
   "can bundle and distribute subagents" (`:583-587`). VS Code and Copilot CLI plugin agents live in
   `com.github.copilot/agents/` (`agent-plugin-reference.md:81`; `cli-plugin-reference.md:158`) rather than the
   held project folder `.github/agents/` (S074/S075); Copilot's legacy plugin form keeps `.agent.md` files
   (`cli-plugin-reference.md:211`), and the consumer page warns that "Support for a package format doesn't guarantee
   that every component works in every harness or client" (`docs/agent-customization/agent-plugins.md:219`).
2. **Claude plugin agents cannot add hooks or MCP servers.** `permissionMode`, `hooks`, `mcpServers` and
   `initialPrompt` are ignored in a plugin agent's frontmatter; the page says to add those as plugin hooks/MCP
   servers instead (`components.md:325`). Copilot CLI does the opposite: a plugin-shipped agent may declare its own
   `mcp-servers` frontmatter, with `${PLUGIN_ROOT}` (or `${CLAUDE_PLUGIN_ROOT}`/`${COPILOT_PLUGIN_ROOT}`) expanded
   inside it, and the page notes workspace and user agents have no plugin root so their frontmatter is left
   unchanged (`cli-plugin-reference.md:219-237`). The held agent entries record no per-agent MCP capability, so
   this is new surface, not a contradiction of them.
3. **Plugin content loses to project content on a name clash.** Copilot CLI: "the agent or skill in the plugin is
   silently ignored. The plugin cannot override project-level or personal configurations"; agents dedupe by
   file-derived ID and skills by the `name` field (`cli-plugin-reference.md:413-417`). A reader auditing a project
   tree therefore treats a plugin-supplied skill as a lower-precedence duplicate, not as an override.
4. **MCP `instructions` is still server-sent, not plugin-authored.** Every plugin MCP surface above is a server
   *config*: Claude `.mcp.json` is "in the same shape as a project `.mcp.json`" (`components.md:381`;
   `mcp.md:472`), Gemini extension `mcpServers` load "just like" `settings.json` servers except `trust`
   (`extensions/reference.md:148-154`), Codex portable `mcp.json` only adds the transport `type`
   (`build/plugins.md:88, 707-726`), VS Code auto-discovers `.mcp.json` (`agent-plugin-reference.md:228-240`),
   Cursor parses `mcp.json` for server entries (`reference/plugins.md:163`). So the round-52 per-client behaviour
   for the `instructions` string (S033 Claude tool-search cap 4,096 chars; S034 VS Code base prompt; S035 Codex
   server-wide guidance, first 512 chars; S036 Gemini appended to system instructions; S042 Copilot CLI allowlist
   flag) applies unchanged to a plugin-bundled server. Two caveats: Copilot CLI's held `--allow-all-mcp-server-instructions`
   flag and per-server allowlist still decide whether the text reaches the prompt (`S042`,
   `cli-command-reference.md:660`), and the page also says standalone MCP servers should be added with
   `copilot mcp add` rather than through a plugin install (`cli-plugin-reference.md:68`). Cursor has no round-52
   row, so a Cursor plugin MCP server's instructions handling remains unheld.
5. **Only Gemini ships an always-on context file.** `contextFileName` names a file in the extension directory,
   defaulting to `GEMINI.md` when present (`extensions/reference.md:158-161`). Claude Code explicitly does not load
   a plugin-root `CLAUDE.md` and warns about it; instructions must be a skill (`plugins-reference.md:665`;
   `components.md:255`). On the opened plugin pages of Codex, VS Code, Copilot CLI, Cursor and opencode, no
   context-file mechanism is documented — skills are the instruction vehicle. (Bounded claim: page-scoped, not a
   Q30 sweep.)

## 5. Suggested 'What a plugin can ship' cells (facts only, all line-cited above)

- Claude Code: skills/, agents/, commands/, hooks/hooks.json, .mcp.json; no CLAUDE.md.
- Codex: skills/, mcp.json (compat .mcp.json), hooks/hooks.json (desktop only); no agents or commands.
- VS Code: skills/, mcp.json or .mcp.json, com.github.copilot/{agents,commands,hooks}.
- Copilot CLI: skills/ (fixed), mcp.json or legacy .mcp.json, com.github.copilot/{agents,commands,hooks}; project files win on name clash.
- Gemini CLI: mcpServers, contextFileName (GEMINI.md), commands/*.toml, hooks/hooks.json, skills/, agents/.
- Cursor: skills/, rules/, agents/, commands/, hooks/hooks.json, mcp.json.
- opencode: none — plugins are code modules exporting hooks; no manifest, skills, or agents.

## 6. Remaining unknowns

- Whether any client actually *loads* a plugin-shipped skill/agent with the standalone rules; all above is
  documentation, no client was run (bounds forbid paid calls anyway).
- Cursor plugin-agent required keys: the page says frontmatter is required and names `name`/`description`, but the
  plugin field table has no Required column (`reference/plugins.md:259-265`), so per-field optionality is
  `[INFERENCE]`.
- Copilot CLI manifest backing (see §3) needs an L1 decision only if a sixth backed row is required; the predicate
  itself passes at F=5.
- opencode plugin-shipped MCP servers: the plugin page documents no MCP surface; not swept against opencode's
  changelog or docs source tree, so "no plugin MCP" is page-scoped.
