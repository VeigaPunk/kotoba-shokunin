Result: MIXED — the C1 table is reachable honestly at exactly F=5 of 7 with zero slack (six if VS Code takes its legacy path), but three of the seven rows (Codex, VS Code, Copilot CLI) pass the frozen counter while misleading by construction because E1's grammar forbids the canonical root `plugin.json` and E5's uniqueness rule punishes the *true* shared token, with three more (Cursor, Gemini CLI, opencode) able to pass while their ship or manifest cell is false; the smallest safe correction is an assignment matrix plus a truth checklist, not a counter change.

Role: critic (pre-attack, no rows exist yet). I did not judge, admit or edit anything. I read the lane read-only, fetched the seven clients' own docs into my own scratch dir, and executed no lane code. No sandbox clone was needed (nothing executed); no tool installs.

## 1. Fetch receipts

All fetches `curl -sSL --max-time 25`, ordinary means, no browser. Scratch dir `/fast/scratch/hyaku/kotoba-r57/CriticC1Rows/`. `date -u` = `Fri 23 Oct 2026 04:47:38 AM UTC` (first batch), `04:48:15Z`, `04:48:37Z`, `04:48:56Z` (later batches). File name = URL with `https://` dropped and `/` → `_`.

| URL | HTTP | bytes | sha256 |
|---|---|---|---|
| https://code.claude.com/docs/en/plugins.md | 200 | 13,454 | `9f50044fa9a2c7c939f6e82cb2edb2a4c854f9fe814a528ae84098125436ee32` |
| https://code.claude.com/docs/en/plugins-reference.md | 200 | 42,124 | `f2910dd6020f5448e5d8c9a8c3b5af7b31b7222d247c20b25f44a712b805916e` |
| https://developers.openai.com/codex/plugins.md | 200 | 14,241 | `612ebfed2779c4aa5c412d8b069ed723e8c2ea264a140ebed5ad52a0853d4db0` |
| https://developers.openai.com/plugins/build/plugins.md | 200 | 38,036 | `c37e330df8f040df8ee2f48035992b37c6a7decf6c3f5640822ca0907118c4e1` |
| https://code.visualstudio.com/docs/agent-customization/agent-plugins.md | 200 | 16,711 | `b717e6f2bf05db2e161ffef8fe82d1002ccea452c7a45d91dc95d7505153757e` |
| https://code.visualstudio.com/docs/agents/reference/agent-plugin-reference.md | 200 | 21,972 | `d6e10328d582db6210fcccc453947d8140ff08a41c31170c4c90816578a44f9e` |
| https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference.md | 200 | 47,200 | `d0d362cc5aa2ef84775145e499596c7e6529531c7b29972ae29f547b5da220d0` |
| https://geminicli.com/docs/extensions/reference/ | 200 | 159,982 | `97847256ef4b28b9fecaf0e1fffdb25a78722ca65f663493a6763b5db2f20686` |
| https://cursor.com/docs/plugins.md | 200 | 20,323 | `74387ff95205965ca3060fac4d12966fea7b1525cc0e972e6f265bbee591cb62` |
| https://opencode.ai/docs/plugins.md | 200 | 9,357 | `c76613823185b6bf7f6a164211bcdc7bba3bc738aba1cc927b51189f8da8681e` |
| https://code.visualstudio.com/docs/editor/extension-marketplace | 200 | 153,162 | `afe8bb27b652bd201370939e1d3f5bcc5f616e8fcec482702e30ccf33569c23a` |
| https://geminicli.com/docs/extensions/ | 200 | 102,412 | `a0390ab023474895…` (HTML; contains no `gemini-extension.json`) |
| https://geminicli.com/docs/extensions/index.md | **404** | 31,633 | `d716f45c4728be29…` (404 body — the `.md` convention does not hold on geminicli.com) |
| https://code.visualstudio.com/docs/editor/extension-marketplace.md | **404** | 9 | `0019dfc4b32d63c1…` (`Not Found`) |

Note for source seats: the lane's usual `append .md` habit fails on geminicli.com (404) and on the VS Code extension-marketplace page (404); the live HTML URL is the one the counter will fetch.

Base held ground, re-verified read-only (`git --no-optional-locks grep -F -i -o <token> 47c05558 -- . ':!.ufo' | wc -l`), case-insensitive, matching the counter's E2 test: `.claude-plugin/plugin.json` 0, `.codex-plugin/plugin.json` 0, `.cursor-plugin/plugin.json` 0, `.plugin/plugin.json` 0, `.github/plugin/plugin.json` 0, `gemini-extension.json` 0. So every token below is new ground and G = the number of distinct tokens found.

## 2. What each client actually documents

| Client | Canonical manifest (client's own words) | E1 verdict | Honest countable? |
|---|---|---|---|
| Claude Code | "A plugin is a directory of components, usually with a manifest. The manifest, a JSON file at `.claude-plugin/plugin.json`" — `code.claude.com_docs_en_plugins.md:27` (18 words) | `.claude-plugin/plugin.json` passes (2 segments, `plugin` in final segment) | yes |
| Codex | root `plugin.json` is canonical; "Existing `.codex-plugin/plugin.json` files remain supported as a compatibility fallback." — `developers.openai.com_plugins_build_plugins.md:25-26`; "A portable plugin has a `plugin.json` manifest at its root." — `:560` | root `plugin.json` FAILS (1 segment, no `codex` marker); `.codex-plugin/plugin.json` passes | only via the fallback path |
| VS Code | "An Agent Plugins 1.0 package has a `plugin.json` file at its root" — `code.visualstudio.com_docs_agents_reference_agent-plugin-reference.md:47`; formats table `:99-104`: Agent Plugins 1.0 → `plugin.json`, Copilot → `plugin.json`, Claude → `.claude-plugin/plugin.json`, Legacy OpenPlugin → `.plugin/plugin.json` | root `plugin.json` FAILS (1 seg, no `vscode` marker); `.plugin/plugin.json` passes; `.claude-plugin/…` fails FOREIGN-NAME | only via a legacy/foreign path |
| Copilot CLI | "Agent Plugins (v1.0.0 or v1.1.0): `plugin.json` at the plugin root." and "Legacy plugins: `.plugin/plugin.json`, `plugin.json`, `.github/plugin/plugin.json`, or `.claude-plugin/plugin.json` (checked in this order)." — `docs.github.com_…_cli-plugin-reference.md:402` | root fails; `.plugin/plugin.json` and `.github/plugin/plugin.json` pass; `.claude-plugin/…` fails FOREIGN-NAME though Copilot **really loads it** | yes, via a fallback |
| Gemini CLI | manifest `gemini-extension.json` (single file at the extension directory root) — `geminicli.com_docs_extensions_reference_:186`; "hooks are not defined in the gemini-extension.json manifest" `:341-342`; `skills/` bundle `:343-346`; sub-agents "preview feature" `:347-349` | `gemini-extension.json` passes only because it carries its OWN marker (`gemini`) | yes |
| Cursor | two formats: "Agent Plugins … with a `plugin.json` manifest at the plugin root, packaging skills and MCP servers" vs "Cursor Plugins … with a `.cursor-plugin/plugin.json` manifest, which add rules, agents, commands, hooks, and variables" — `cursor.com_docs_plugins.md:27-28`; again `:207-208`, `:319-320` | `.cursor-plugin/plugin.json` passes; root fails | yes, but only one of the two formats |
| opencode | "A plugin is a **JavaScript/TypeScript module** that exports one or more plugin functions." — `opencode.ai_docs_plugins.md:64-65`; load order `:51-55`; install `:41-45` | **no `.json` manifest exists**; `opencode.json` (config) and `package.json` (deps) both fail the plugin-word / manifest test | **no — must be reported, never invented** |

Honest ceiling: Claude, Codex(fallback), Copilot(fallback), Gemini, Cursor = **F=5**, exactly the target, zero slack. A sixth (VS Code `.plugin/plugin.json`) is defensible only with an Action that says it is the legacy OpenPlugin format. opencode is a guaranteed non-count.

## 3. Clients whose row passes the counter while saying something false or misleading

**3.1 Codex — highest risk: names a documented fallback as if it were the manifest.** The only E1-passing *rule* path in the OpenAI plugin docs is `.codex-plugin/plugin.json`, and the same page calls it a *compatibility fallback* (`:25-26`) and says the packaging tool "scaffolds a supported `.codex-plugin/plugin.json` compatibility manifest" (`:54`). A row whose Manifest cell is that path and whose Action does not say "fallback; root `plugin.json` is canonical" tells the reader the wrong file is primary — and the primary is the file E1 forbids. A second trap on the same page: `my-first-plugin/plugin.json` (`:230`) is an *example instance* path that passes E1 and is on the live page, so a seat grepping for a passing token can land on it; it is a placeholder folder name, not a rule.

**3.2 Copilot CLI — the true cross-format answer is counter-forbidden.** Copilot loads Claude's `.claude-plugin/plugin.json` and the doc says so (`:107`, `:402`); the FOREIGN-NAME guard rejects any token containing `claude` for Copilot. So the row must either name the third legacy fallback (`.github/plugin/plugin.json`, third in the checked order — true but out of precedence) or hide the compatibility in prose. Either way the cell that promises "the plugin manifest" omits the paths checked ahead of it (Agent Plugins root `plugin.json`; legacy `.plugin/plugin.json` then root `plugin.json`). The counter cannot see the omission; the reader can be misled about precedence.

**3.3 VS Code — the canonical manifest is unexpressible, so the cell must name a legacy one.** VS Code's own default is root `plugin.json` with the Agent Plugins `$schema`, and "The Copilot format is used as the default when no other format marker is found." (`agent-plugin-reference.md:97`). The only token in the VS Code plugin-format docs that passes E1 is `.plugin/plugin.json` = *Legacy OpenPlugin* (`:104`). A row that stops there tells a reader to look for the rarest format. This is exactly the "editor extensions vs agent plugins" hazard in the assignment: `.vscode/extensions.json` is NOT a plugin manifest (it is the workspace recommendation list — `code.visualstudio.com_docs_editor_extension-marketplace:1868-1869`, quote: "the command creates an `extensions.json` file located in the workspace `.vscode` folder", 17 words), and it also fails `--fetch` because the page prints `extensions.json` and `.vscode` as separate `<code>` spans, never the contiguous `.vscode/extensions.json`. Grammar would accept it (`extensions` is a plugin word); only the live fetch kills it — so **a non-fetch "backed" number must never be quoted as evidence**.

**3.4 Cursor — union-of-formats ship cell.** `.cursor-plugin/plugin.json` is genuinely Cursor's format, so the token is safe; the ship cell is not. Cursor's Agent Plugins "packag[e] skills and MCP servers", while only Cursor Plugins "add rules, agents, commands, hooks, and variables" (`:27-28`). A ship cell listing rules/agents/commands/hooks for *all* Cursor plugins is false for a root-`plugin.json` plugin. The counter never reads that cell (plan Q31).

**3.5 Gemini CLI — the manifest is a filename, and hooks are explicitly outside it.** `gemini-extension.json` is true, but (a) the page states "hooks are not defined in the gemini-extension.json manifest" (`:341-342`), so "hooks" in the ship cell without the `hooks/hooks.json` qualifier is false; (b) sub-agents are "a preview feature currently under active development" (`:347-349`) — a ship cell saying "subagents" overstates; (c) the token is a bare filename, so the row must say it sits at the extension directory root (the cell cannot express the directory; put the directory in the Action). Also note the client's own term is **extensions**, not plugins — a row that renames them loses the reader.

**3.6 opencode — the free row: the predicate tolerates a false one.** opencode has no `.json` manifest at all (`:64-65`). F≥5 of K means **up to two rows may be rejected and the run still exits 0**, and the rejected row's SKILL.md prose still ships. So a false opencode row — e.g. `.opencode/plugin/plugin.json`, which passes E1's grammar and dies only at `--fetch` — costs the claim nothing, and a well-meant `.opencode/plugins/` (directory) or `opencode.json` (config) does not even enter K. The predicate cannot see rows it does not count; the L1 must read the reject lines and fix the sentence, not just chase F.

**3.7 Claude Code — "usually" vs mandatory.** The safest row, but the doc says "A plugin is a directory of components, **usually** with a manifest" (`plugins.md:27`), so "every plugin carries `.claude-plugin/plugin.json`" overclaims. Also the adjacent `.claude-plugin/marketplace.json` is a marketplace file, not a plugin manifest (the counter rejects `marketplace` segments; prose must too).

## 4. Counter-level structural findings

**A. E1 forbids the canonical answer for four of seven clients.** `verifiers/check_plugin_manifests.py:535-558` requires ≥2 path segments unless the token carries the row's own marker. Root `plugin.json` is the canonical Agent Plugins manifest for Codex, VS Code, Copilot CLI and Cursor. The rule therefore *forces* legacy/format-specific paths into a cell headed "Plugin manifest". Not fixable without touching a frozen counter; fix it in the Action cells and in the entry prose. [INFERENCE] a seat that notices the mismatch under F-pressure will fabricate a directory prefix rather than report the primary path.

**B. E5 punishes the true pair.** `shared_tokens` (`:634-642`) disqualifies every client sharing a token. VS Code (`agent-plugin-reference.md:104`) and Copilot CLI (`:402`) both document `.plugin/plugin.json` verbatim. Two seats drafting independently from these two pages are likely to pick the same string — both true, both rejected, F=4, exit 1, with the cause being a *correct* choice. This is the strongest counterexample available locally, and it is invisible in the reject text (it reads as a content error). Mitigation: assign the tokens before drafting (§6).

**C. The predicate is a 5-of-7 threshold, not a truth check.** `predicate` (`:1034-1038`) reads only found/ground. Consequences: two false rows are free; a rejected row's prose ships; and F=5 leaves no room for one flaky fetch (30 s timeout, one retry — `FETCH_TIMEOUT`).

**D. Silent-zero hazards in the table plumbing.** `skill_rows` (`:412-420`) reads **only the first table** of the section and returns `[]` if its header is not the frozen one — a preamble table inserted by the budget move, or a header with a changed column name, yields K=0 and F=0 with no content error. `client_name` (`:355-357`) requires the exact cell text: `Cursor (agent)` or `Claude Code (plugins)` never matches. A duplicate client row disqualifies that client — so the honest VS Code distinction (editor extensions vs agent plugins) **cannot** be a second row; it must be prose outside the table.

**E. G is not the risk.** With the §6 assignment, G=5 (or 6) distinct casefold tokens, base held 0 for all (verified above). G≥3 has two rows of slack.

## 5. Checklist — apply to every landed row (L1, then falsify seats)

Mechanical (a single miss is a reject line or a silent zero):
1. The section's **first** table is this table; heading byte-exact `### Plugin manifests by client`; header byte-exact `| Client | Plugin manifest | What a plugin can ship | Action |`; no table above it (watch the budget move).
2. Exactly one row per client, client cell byte-exact one of the seven names; no duplicate client row; any second row for VS Code's editor extensions goes in prose, not the table.
3. The token is the **first** backticked span of the Manifest cell. If the cell also mentions a second path, the first one is what is judged — put the judged path first.
4. Token grammar: `~/`/`./` optional; ≥2 segments OR own marker; final segment ends `.json` **and** splits (on `-._`) to plugin/plugin(s)/extension/extensions; no `marketplace` segment; no dotted non-final segment except a leading dot.
5. No other row of any client name uses the same casefold(normalise(token)) — specifically do not let two rows share `plugin.json`-style or `.plugin/plugin.json`.
6. No foreign marker anywhere in the token (claude/codex/vscode/copilot/gemini/cursor/opencode), even when the client genuinely reads that format.
7. Not an example-instance path (`my-first-plugin/plugin.json`) and not a user cache/install directory; the token is a manifest file the client's loader reads.
8. Entry row: `Manifest` cell equals the token or its `~/`-stripped form, exact and case-sensitive — no "or", no parentheses, no second path, no backticks around extra words.
9. Source: new S-id, `docs`, tier A, `mined`, opened `2026-10-23`, on the client's pinned host, not a re-cited base URL, no `changelog|release|releases|news|blog` in the path.
10. Quote: 6–25 words, contains the token byte-exact and case-sensitive, contains a plugin(s)/extension(s) word **outside** the token span, and appears verbatim (whitespace-normalised) in `## Gate`.
11. `--fetch` on the **exact URL recorded**, in the exact form the counter fetches (geminicli.com: HTML URL, not `.md`; VS Code extension-marketplace: HTML URL). A non-fetch run is not evidence.
12. Read every `reject <client>:` line and reconcile the SKILL.md sentence — a rejected row is still published text.

Truth (nothing in the counter measures these):
13. The Manifest cell names the client's **primary** path or, if it must name a fallback, the Action says "fallback/legacy" and gives the primary path in words (Codex root `plugin.json`; VS Code Agent Plugins root `plugin.json`; Copilot Agent Plugins root `plugin.json`, then legacy `.plugin/plugin.json`, then root `plugin.json`; Cursor Agent-format root).
14. The format name is stated when a client reads several formats (VS Code four; Copilot two; Cursor two). Do not present one format as the client's only one.
15. The ship cell lists only what **that format** can ship: Claude skills/agents/hooks/MCP/commands and a manifest that is "usually" present; Codex skills/MCP/apps (`extensions.com.openai` hooks); VS Code per format; Copilot Agent Plugins `skills/` fixed + `mcp.json`, legacy `agents/`/`hooks.json`/`.mcp.json`/`lsp.json`; Gemini `mcpServers`, `contextFileName`, themes, custom commands, `skills/`, hooks via `hooks/hooks.json` **not** the manifest, sub-agents **preview**; Cursor Cursor-format only rules/agents/commands/hooks/variables, Agent-format skills + MCP servers.
16. opencode's row says plainly that a plugin is a JS/TS module with no manifest; no invented `.json`. If a `.json` appears for opencode, the row is false even if the reject line hides it.
17. No row claims the plugin's contents are trusted or already loaded; the Action is what to do when a skill arrives inside a plugin (read the manifest, locate `skills/`/`agents/`, check the format).
18. User vs project locations: if named, they are the ones the doc gives (Cursor `~/.cursor/plugins/local` is a development location, not a project one; Copilot's `~/.copilot/installed-plugins/…` is an install cache, not a manifest location).

## 6. Smallest safe correction (assignment, not a counter change)

| Client | Token (Manifest cell) | Action must add |
|---|---|---|
| Claude Code | `.claude-plugin/plugin.json` | manifest is usual, not mandatory; marketplace file is separate |
| Codex | `.codex-plugin/plugin.json` | "compatibility fallback; root `plugin.json` is canonical" |
| Copilot CLI | `.github/plugin/plugin.json` | "third legacy location in the checked order; an Agent Plugins root `plugin.json` takes precedence" |
| Gemini CLI | `gemini-extension.json` | "at the extension directory root; hooks live in `hooks/hooks.json`; sub-agents preview" |
| Cursor | `.cursor-plugin/plugin.json` | "Cursor format; a root `plugin.json` Agent Plugin also loads (skills + MCP only)" |
| VS Code | `.plugin/plugin.json` (optional 6th) | "legacy OpenPlugin; four formats auto-detected, root `plugin.json` is the default" |
| opencode | no `.json` (write the reason in words) | "JS/TS module, no manifest; read the plugin source" |

With this assignment there is no E5 collision, F=5 (honest floor) or 6 (with VS Code), G=5 or 6, and every counted row's cell is true with the Action repairing the omission. The falsify wave should re-fetch the five/six URLs, diff token+quote against the entry, and re-read the reject lines for the two non-counting rows.

## 7. Impacted axes

- **depth (primary, 9)**: the table adds a real decision surface, but its ceiling is set by E1: root `plugin.json` — the single most common answer — can appear only in prose. The Action cell is the only place the depth can be preserved.
- **calibration (8.5)**: the 5-of-7 threshold lets two rows be wrong at exit 0. If SKILL.md ships a false opencode or VS Code row while the receipt says F=5, calibration takes the hit, not depth.
- **consistency (10)**: two clients sharing a token (E5) and two names for one thing (Gemini "extensions" vs the table's "plugins") are consistency defects the counter reports as rejects, not as wording.
- **freshness / adjacency**: untouched by this review; no freshness claim was made or implied.
- **Q31 boundary honoured**: "what a plugin can ship" completeness, and whether a client actually loads the documented path at runtime, remain unmeasured by C1 — findings 3.4, 3.5 and 3.7 live exactly on that boundary and must be carried as reviewer claims, not counter claims.

Tooling installed/updated: none (no install was needed; pacman is paused host-wide and nothing required it).
