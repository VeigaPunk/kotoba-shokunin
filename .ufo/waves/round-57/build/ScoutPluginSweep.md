# ScoutPluginSweep — plugin surfaces beyond the seven clients; gaps between them

Result: DONE — omp *does* carry client-specific plugin manifests (`.omp-plugin/plugin.json`, catalog `.omp-plugin/marketplace.json`) plus a cross-vendor fallback, and the largest gap between the seven counted rows is that three installed clients (Cursor, Codex, omp) each **read `.claude-plugin/plugin.json`**, so one manifest file is simultaneously the documented answer for one client and a compatibility path for three others.

Scope note: read-only host inspection, installed-binary `strings`, official docs and the open Agent Plugins spec. No lane file edited, no counter run or scored, no paid model call. No tools installed or upgraded (nothing needed; pacman was paused and unused). All scratch under `/fast/scratch/hyaku/kotoba-r57/ScoutPluginSweep/`.

---

## 1. omp (this host's harness): it has plugin manifests, three layers

Binary `/home/vgpnk/.local/bin/omp`, `omp v18.12.6`, ELF, not stripped (`file` + `omp --help`, exit 0). Strings index: `/fast/scratch/hyaku/kotoba-r57/ScoutPluginSweep/omp.strings` (1,142,189 lines, `strings -n 8`).

**(a) Per-plugin manifest is `.omp-plugin/plugin.json`** — strings:519221 region and:549086
> `for (const R of [".omp-plugin", ".claude-plugin"]) {`

:544559 `return await Ue(Ac.join(u, ".claude-plugin", "plugin.json")) !== null;`
:251976/252026 `.claude-plugin` and `.claude-plugin/marketplace.json`.

**(b) Its own marketplace catalog is `.omp-plugin/marketplace.json`, with Claude Code's file as the documented fallback** — documented in `omp://marketplace.md` (134-file doc set, listed at `omp://`):
> "catalog file at `.omp-plugin/marketplace.json` (preferred) or `.claude-plugin/marketplace.json` (Claude Code-compatible fallback)"

and, in the same doc, the compatibility statement:

> "It is compatible with the Claude Code plugin registry format."

Same doc: plugins are "a directory containing Claude/OMP plugin content such as skills, commands, agents, rules, hooks, tools"; install version resolution "tries catalog `version`, `.claude-plugin/plugin.json`, root `plugin.json`, then `package.json`". Binary agrees: strings:715110 `var b = [".omp-plugin/marketplace.json", ".claude-plugin/marketplace.json"];`.

**(c) A root `plugin.json` (Agent Plugins 1.0.0) is also accepted** — `omp://marketplace.md`:
> "Root `plugin.json` packages declaring the Agent Plugins 1.0.0 schema use the portable `agent-plugins` discovery provider for skills and `mcp.json`"

**(d) Separate, non-manifest extension mechanism**: `omp --help` exit 0 lists `-e, --extension=<value>  Load an extension file`, `--no-extensions  Disable extension discovery`, `--hook`. `omp://extension-loading.md` and `omp://skills/authoring-extensions.md` cover TS/JS modules; `package.json` `omp.extensions` declares them (marketplace.md). So omp has **both** a JSON manifest (plugins/marketplaces) and a module loader (extensions) — the two words are not synonyms in omp.

**(e) omp reads a *third* client's format**: `omp://gemini-manifest-extensions.md` documents a `gemini` discovery provider (priority 60) that scans `~/.gemini/extensions` (opt-in via `enabledProviders`) and `<cwd>/.gemini/extensions` for `gemini-extension.json`, and says the native provider "also reads `gemini-extension.json`". Host state matches: `~/.gemini/` exists but holds only `antigravity-cli/` and `config/` — no `extensions/` (`ls -la`, exit 0), and `find ~/.gemini ~/.config -maxdepth 5 -name gemini-extension.json` → no hits. omp itself: `omp plugin list` → "No plugins installed" (exit 0); `omp plugin discover --json` → "No plugins available" (exit 0).

**For the entry's Limits:** omp is an eighth client with a real manifest pair (`.omp-plugin/plugin.json`, `.omp-plugin/marketplace.json`). It belongs in Limits, not a counted row, because it is not one of the seven frozen clients — but a reader auditing this host will meet it.

## 2. Plugin folders actually installed on this host, and the manifest files they hold

| Root | Exists | Manifest files actually present |
|---|---|---|
| `~/.claude/plugins` | yes | `.claude-plugin/marketplace.json` ×1 (`marketplaces/claude-plugins-official/.claude-plugin/marketplace.json`) and `.claude-plugin/plugin.json` ×41 = 40 under `marketplaces/claude-plugins-official/` (14 `external_plugins/`, 26 `plugins/`) + 1 under `synced/<uuid>/cowork-plugin-management/.claude-plugin/plugin.json`; also a vendor-sync `manifest.json` under `synced/<uuid>/` — not a plugin manifest (Claude's own sync ledger) |
| `~/.cursor/plugins` | yes | `.cursor-plugin/plugin.json` ×14 (all 14 cached `cursor-public` plugins), `.claude-plugin/` ×3, `.codex-plugin/` ×2 |
| `~/.codex/plugins` | yes | **no** manifest JSON; only `.plugin-appserver/codex` (296,885,960 B) and `.plugin-appserver/codex-code-mode-host` (74,277,776 B) binaries (the Codex CLI itself, staged) and an empty `.remote-plugin-install-staging` |
| `~/.config/opencode` | yes | no plugin dir at all: only `cli.json`, `opencode.json`, `service.json` (95–163 B) |
| `~/.gemini/extensions` | **no** (`ls` exit 2: "No such file or directory") | — |

Commands: `find … -name plugin.json -o -name marketplace.json …` (see table counts), `find ~/.cursor/plugins/cache -name plugin.json -path '*.cursor-plugin*' | wc -l` → 14; `ls ~/.cursor/plugins/cache/cursor-public | wc -l` → 14; `find ~/.claude/plugins -name plugin.json -path '*.claude-plugin*' | wc -l` → 41.

Observed manifest shapes (read verbatim):
- `~/.claude/plugins/marketplaces/claude-plugins-official/plugins/hookify/.claude-plugin/plugin.json` — `{name, description, author{name,email}}`, nothing else.
- `…/claude-plugins-official/.claude-plugin/marketplace.json:1-3` — `"$schema": "https://anthropic.com/claude-code/marketplace.schema.json"`, `"name": "claude-plugins-official"`, plus `renames{}` and `plugins[]`.
- `~/.cursor/plugins/cache/cursor-public/github/9b93e81…/.cursor-plugin/plugin.json` — `name, displayName, version, minClientVersions{cursor}, description, author, homepage, repository, license, logo, keywords, category, tags, variables{}, mcpServers: "./mcp.json"`. Cursor's manifest points at its MCP file by relative path; `mcp.json` sits at the plugin root.

**Gap this exposes:** an installed plugin directory is not proof of a manifest-shaped contract. `~/.codex/plugins` is populated yet holds zero manifest JSON, and `~/.config/opencode` holds zero plugin content — a reader cannot infer "Codex has no plugin system" or "opencode has plugins here" from the folders alone.

## 3. Cross-client reuse of plugin formats (the real gap between the rows)

### 3.1 Cursor reads Claude Code's manifest — observed code, not inference
Cursor bundle `/home/vgpnk/.local/share/cursor-agent/versions/2026.10.22-27dcf5f/index.js` (cursor-agent is a bash wrapper; `readlink -f` → this tree; `index.js` is the real bundle):

- `D=[".cursor-plugin/plugin.json",".claude-plugin/plugin.json","plugin.json"]`
- `N=[".cursor-plugin",".claude-plugin"]`
- `M=[".cursor-plugin/marketplace.json",".claude-plugin/marketplace.json"]`
- consumption is a read loop, `for(const s of D){ … await Bc(i) …}` and `async function Nc(t,e,r){…for(const s of D…}` — candidate paths are tried in order, not merely listed.
- `B=new Set(["https://agent-plugins.org/schemas/1.0.0/plugin.schema.json","https://agent-plugins.org/schemas/1.0.0/mcp.schema.json"])` with `q(t)` classifying a manifest's `$schema` as supported/unsupported — Cursor validates the open-standard schemas too.
- the same module writes a `.cursor-plugin` directory (`join(e,".cursor-plugin"); mkdir(…,{recursive:true}); writeFile`) — [INFERENCE] the CLI can also emit/copy a Cursor manifest when importing, which is why both a read path and a write path appear together.

### 3.2 Codex reads Claude Code's *and* Cursor's manifests
`strings -n 6 /home/vgpnk/.codex/plugins/.plugin-appserver/codex` (632,673 lines) contains literal runs:

- `.codex-plugin/plugin.json.claude-plugin/plugin.json.cursor-plugin/plugin.json` (repeated, e.g. alongside `agents/openai.yaml`, `mcp.json`, `app.json`)
- `.agents/plugins/api_marketplace.json.claude-plugin/marketplace.json.cursor-plugin/marketplace.json`
- error strings `skipping marketplace that failed to load`, `failed to read marketplace file`, `plugin app config is missing an app id`, `Agent Plugins MCP config is not a regular …`, and the schema URL fragment `https://agent-plugins.org/schem…`
- **no** `gemini-extension.json`, no `.omp-plugin`, no `.opencode` (grep counts 0).

### 3.3 omp reads Claude Code's manifest and Gemini's extensions
§1(a)(b)(e): `.claude-plugin/plugin.json` as candidate alongside `.omp-plugin/plugin.json`; `gemini-extension.json` loaders in `omp://gemini-manifest-extensions.md`. `omp://marketplace.md` states the marketplace format compatibility in words.

### 3.4 Claude Code does **not** read the others' manifests; it only *detects* them
`strings -n 6 /opt/claude-code/bin/claude` (617,872 lines): `.claude-plugin` 83 hits (its own), `.cursor-plugin` 0, `.codex-plugin` 0, `.omp-plugin` 0, `gemini-extension.json` 2. Both Gemini hits are onboarding/migration notices, not loaders:
> `label:"gemini-extension.json",reason:"Gemini extensions map to Claude Code plugins. Not auto-converted yet."`

and the neighbouring detector emits `label:".gemini/system.md",reason:"Gemini system.md replaces the system prompt…"`. So Claude Code's cross-client behaviour is *advice*, not format support — a materially different row-level fact than Cursor/Codex/omp.

### 3.5 A vendor-neutral format already sits underneath this
`https://agent-plugins.org/` (fetch: `date -u` → `Fri 23 Oct 2026 04:48:27 AM UTC`, HTTP 200, 92,648 B, sha256 `ee65399fa3ac87ff2214b9c23e25d700ce1e38e2b4635af5b7d2fd5c11690aef`), docs at `/docs.md` (HTTP 200, 3,479 B, sha256 `8012118b11d14c11ecc3a8043190ff93c72f846e001730ccc99efbf67ec1b7a9`), schema at `/schemas/1.0.0/plugin.schema.json` (HTTP 200, 1,805 B, sha256 `0a4aad95ce337878ad38802ebf0daa3fde76abe3f65400c86bcbb1ec0b3ab883`):

> "Agent Plugins is an open, vendor-neutral standard for packaging reusable components into portable plugins." (docs.md:10)

> "Its initial Technical Steering Committee includes Core Maintainers from Amazon, Cursor, Microsoft, OpenAI, and Vercel." (docs.md:42)

The portable package is a directory with **bare `plugin.json` at the root**, `skills/`, `mcp.json`, and reverse-domain client namespaces (`com.example.client/hooks/`). Schema title: `"Agent Plugins Manifest"`, `description`: `"Machine-readable schema for plugin.json in Agent Plugins 1.0.0"`. Cursor, Codex and omp all reference these schema URLs (3.1, 3.2, §1c).

### 3.6 One package, three manifests, on this host
Cursor's public cache already ships multi-client packages. Of 14 cached plugins: 14 carry `.cursor-plugin/`, 3 carry `.claude-plugin/`, 2 carry `.codex-plugin/`; **both** multi-client ones carry all three:
- `~/.cursor/plugins/cache/cursor-public/aws-agents/d00d03ae…/` → `.claude-plugin/`, `.codex-plugin/`, `.cursor-plugin/`, `mcp.json`, `.mcp.json`, root `plugin.json`, `skills/`
- `~/.cursor/plugins/cache/cursor-public/elevenlabs/1c5f1de1…/` → `.claude-plugin/`, `.codex-plugin/`, `.cursor-plugin/`, `mcp.json`, `server.json`, `skills/`, `architect/`

`aws-agents/.codex-plugin/plugin.json:1-4` → `{"name":"aws-agents","version":"1.0.0","description":"Build, deploy, and operate AI agents on AWS…`.

**Doc-level cross-client statement (Cursor, official):** `https://cursor.com/docs/reference/plugins` (`date -u` → `Fri 23 Oct 2026 04:49:18 AM UTC`, HTTP 200, 642,433 B, sha256 `480632655ad1242a7f38d28b28f89e43f4cf9a949df016654967518611faa3db`): `.cursor-plugin/plugin.json` ×13, `agent-plugins` ×13, `CLAUDE_PLUGIN_ROOT` ×3, `.claude-plugin` literal ×0. The page documents Cursor as reading the Agent Plugins open standard (`"Agent Plugins (open standard)"`, links to `https://agent-plugins.org/schemas/1.0.0/…`) and expands `${CLAUDE_PLUGIN_ROOT}`; it does **not** document `.claude-plugin/plugin.json` as a Cursor path — that exists only in the shipped code (3.1). Docs lag implementation here; record the code, not the docs, if the entry names Cursor's fallback.

## 4. What this means for the C1 entry's Limits (prose the Scribe can lift)

1. **A manifest path is not a client identity.** `.claude-plugin/plugin.json` is the Claude Code answer *and* a documented-compatible fallback in omp (`omp://marketplace.md`) *and* a read candidate in Cursor and Codex. A reader who greps one `.claude-plugin` directory cannot tell which client will load it; three on this host would.
2. **Bare root `plugin.json` is deliberately client-neutral.** Agent Plugins 1.0.0 (Amazon/Cursor/Microsoft/OpenAI/Vercel TSC) puts it at the package root; Cursor lists it as candidate 3, omp maps it to its `agent-plugins` provider. The v2 counter rejects a bare `plugin.json` token (needs ≥2 segments or the row's own client marker) — that rejection is *correct*, because the file identifies no client. Do not "fix" it into a counted row.
3. **Presence ≠ contract.** `~/.codex/plugins` is populated but manifest-free; `~/.config/opencode` has no plugin dir; `~/.gemini/extensions` does not exist. Directory listing alone says nothing about manifests.
4. **"Documented" and "read" are different claims.** Claude Code documents Gemini extensions only as a migration notice ("Not auto-converted yet") and reads neither `.cursor-plugin` nor `.codex-plugin`; Cursor and Codex read Claude's file while Cursor's docs do not name it. State per client which of the two you verified.
5. **omp is an eighth client outside the frozen seven** with two real manifest paths. Keep it in Limits; it is not a row.
6. **One package may carry several manifests** (aws-agents, elevenlabs: 3 each). A plugin directory can be the answer for three rows at once; the entry's per-client framing stays true, but "the manifest a plugin dir contains" is plural in practice.
7. **Extension ≠ manifest** in omp: `-e/--extension` loads TS/JS modules and `package.json` `omp.extensions`; the JSON manifest is only for plugins/marketplaces (`omp://extension-loading.md`, `omp://marketplace.md`). Rows that say "manifest path" must not be read as "the only way a plugin ships instructions".

## 5. Unverified / remaining unknowns (honest gaps)

- **Codex docs page not verified.** `https://developers.openai.com/codex/plugins` fetched HTTP 200, 501,773 B, sha256 `9d77bbd1cd179df75f678099b8fb9376b2094cd59c28eb35ab64960cdd8f69ae`, but grep for `.claude-plugin`, `.cursor-plugin`, `.codex-plugin`, `agent-plugins`, `plugin.json` → 0 hits and no extractable `<title>`; content is client-rendered. Codex cross-client evidence here is **binary only**. Codex documentation status: *not checked* (by the Q30 rule, not "silent").
- **Gemini CLI and opencode bundles not opened.** Both `gemini` and `opencode` are npx wrappers; the resolved packages (`~/.npm/_npx/d07ada7b4a99c96e/…/@google/gemini-cli`, `~/.npm/_npx/e2094862b59aac7b/…/opencode-ai`) ship only `bundle`/`bin` + postinstall, and grep for `.claude-plugin|.cursor-plugin|.codex-plugin|gemini-extension.json|agent-plugins` returned 0 — but the native payload those postinstalls fetch was not inspected, so **0 here is not absence**. opencode did yield one `.opencode/plugin` literal.
- **Cursor's write path** (`mkdir .cursor-plugin`, `writeFile`) is read as an import/emit step by inference, not traced to a command.
- **`agent-plugins.org` compatibility matrix** (which clients are certified) not opened beyond `/` and `/docs.md`; a `/client-implementers` page exists per docs.md and was not read.
- **`claude-code` docs manifest-reference** (`code.claude.com/docs/en/plugins/manifest-reference`, HTTP 200, 833,501 B, sha256 `fd006206d11902cc3912a5e8b9fe036e5ac2268575f8e9b1082137d5ea3f352b`) shows `.claude-plugin/plugin.json` ×3 and `plugin.json` ×16 — corroborates the Claude row but was not mined line-by-line here; ScribeC1Entry owns that row.
- **Nothing here scores.** No counter was run; if the entry quotes any of this as a counted source it must open the page itself and take its own byte-exact quote (bounds: ≤25 words, line numbers in the fetched bytes). My Cursor/Codex/omp strings evidence is **host observation**, which the counter cannot read.

## 6. Commands and exit codes (spot-checkable)

| Command | Exit | Observed |
|---|---|---|
| `omp --help` | 0 | `omp v18.12.6`; `-e, --extension=<value> Load an extension file`; `--no-extensions` |
| `omp plugin --help` | 0 | actions `install\|uninstall\|list\|link\|doctor\|features\|config\|enable\|disable\|marketplace\|discover\|upgrade` |
| `omp plugin list` | 0 | `No plugins installed` |
| `omp plugin discover --json` | 0 | `No plugins available` |
| `find /home/vgpnk/.cursor/plugins/cache -name plugin.json -path '*.cursor-plugin*' \| wc -l` | 0 | `14` |
| `find /home/vgpnk/.claude/plugins -name plugin.json -path '*.claude-plugin*' \| wc -l` | 0 | `41` |
| `ls -la ~/.claude/plugins ~/.codex ~/.gemini/extensions ~/.config/opencode ~/.cursor` | 2 | all listed except `~/.gemini/extensions` (no such directory) |
| `strings -n 6 /home/vgpnk/.codex/plugins/.plugin-appserver/codex \| grep -c '\.claude-plugin'` | 0 | `11` |
| `strings -n 6 /opt/claude-code/bin/claude \| grep -c '\.cursor-plugin'` | 1 | `0` |
| `grep -o 'D=\["\.cursor-plugin/plugin\.json",…' cursor-agent/…/index.js` | 0 | `D=[".cursor-plugin/plugin.json",".claude-plugin/plugin.json","plugin.json"]` |

Bounds respected: no lane/jj/git writes (`jj`/`git` never invoked), no `pkill`, every command under `timeout`, no subagents, no paid model call, report is the only file written in the lane.
