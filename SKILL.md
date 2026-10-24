---
name: kotoba-shokunin
description: >
  Prompt & skill craft — audits, writes, and rewrites SKILL.md / AGENTS.md /
  dispatch prompts / system prompts for trigger fidelity and decision density.
  Triggers: "skill file", "SKILL.md", "frontmatter description", "trigger
  words", "prompt craft", "write a skill", "audit this skill", "skill quality".
  Anti-triggers: general prompt engineering for model outputs (not skill
  files), runtime code changes, and domain content inside a skill's
  reference/ tree. Sibling boundary: kagi, kake, kasegi, kengaku and kumitate
  own their own SKILL.md content — this skill audits and reports; fixes route
  to the owning lane. chousa owns the research method; kama owns endpoint
  verification; kengaku owns measured capability effects of prompt format;
  tameshi owns the fixture and mutation method. NOT kotodama-shokunin:
  kotodama owns naming and language for fictional worlds despite the similar
  name. Note:
  shokunin files sit outside the omp skill discovery roots, so this text
  never reaches the omp router — craft here is audit-side.
---

# kotoba-shokunin — prompt & skill craft

A SKILL.md is a **loader contract**: the frontmatter `description` is the
only part any router ingests — and the two harnesses here show it differently.
On **omp** the `<skills>` catalogue (template in the omp ELF, rendered per
session) shows each skill as `- name: render` where `render` is
`cache.get(key) ?? previewSkillDescription`: a cached LLM one-liner if the
async compressor landed, else a deterministic `slice(0, _8n-1)` cut with
`_8n=100` (i.e. offset 99) plus last-space/`…` fallback (`skill-descriptions.ts`;
cache
`~/.omp/agent/skill-descriptions.db`). Cache coverage is time-varying — 5/17
rows at round 7, 17 rows at round 9, **18 at round 13** (2026-09-28T23:30Z) with
**all 17 live keys still reproducing** against today's on-disk descriptions
(2026-10-14 errata — the live set is now 7; see LOG.md round 18). The count is
not a coverage meter: rows are keyed per
`(name, description-as-loaded)` and never pruned, so the 18th row is a
*project-scoped* `ufo` copy the host once offered
(`~/Projects/origin-work/ufo-fsd-alpha/skills/ufo/SKILL.md` — 2026-10-14 errata:
historical path; the tree moved to `~/Projects/ufo-fsd-alpha` and that file no
longer carries the 690-char description the key was computed over, so the
mechanism is described, not re-pinned), not a new live skill. Rows land
*after* session start, so an already-open session keeps its truncator renders
(and an edited `description` misses its key, reverting that skill until a new
row lands). On **opencode** the `<available_skills>`
catalogue renders the full `description` byte-for-byte plus `<location>` — no
cliff. The body is the only part the executing agent always sees. Craft means
both surfaces earn their tokens.
Rank: shonen.

Evidence base: 16 production skill files surveyed 2026-09-28
(`~/.agents/skills/*/SKILL.md`, `~/.config/opencode/skills/ufo/SKILL.md`)
plus the host's other instruction surfaces (agent definitions, AGENTS.md
files, command files, dispatch prompts — see "Instruction surfaces").
Cited line numbers are points-in-time. Verify before trusting: if a cited
line has drifted, re-read the file and update the citation — do not
propagate a claim whose source moved.

Skill-file anatomy (observed load order, the seven-section table, and the "not a mandatory skeleton" note) moved verbatim to `corpus/knowledge/anatomy-and-compression.md` § Moved from SKILL.md § Skill-file anatomy (round 58).

## Instruction surfaces — pick the file before the fix

The nine-class surface table with its evidence paragraphs moved verbatim to
`corpus/knowledge/instruction-surface-census-round13.md` § SKILL.md instruction-surfaces
table (round 22; sha256 `e046a0252cc96f17…` pinned there). The machine check is unchanged:
`verifiers/verify_surfaces.py` (7 checks) reads that same census file. The table's
"All craft below" cell refers to this file's craft sections below — kept verbatim.

MCP server `instructions` (round 52, `corpus/knowledge/mcp-server-instructions-round52.md`, S032–S037, S040–S042):
server-wide text the server returns at `initialize` (spec 2025-11-25; at `server/discover` in the current
revision 2026-07-28, S040); the spec makes it optional and leaves placement to the client.

| guidance that is… | put it in | why (documented) |
|---|---|---|
| about the whole server: cross-tool order, constraints, rate limits | the server's `instructions`, first 512 characters self-contained | Codex uses it as server-wide guidance and asks for a self-contained first 512 characters (S035); Claude Code cuts it at 4,096 by default (S033) |
| about when to reach for the server at all | `instructions` | with tool search, Claude Code loads only tool names and server instructions at session start (S033) |
| about one tool's inputs | that tool's `description` | the spec says it "should not duplicate information already in tool descriptions" (S040); Claude Code, VS Code (S034), Codex, Gemini CLI (S036), opencode (S041) and Copilot CLI (S042) put `instructions` in front of the model already |
| needed on every client | a skill or always-on file too | the field is optional (S032), opencode drops a server's text when permissions deny all its tools (S041), and Copilot CLI needs a flag to include it from all servers (S042) |

### Agent-definition files by client

Where each client's own documentation puts its agent (subagent, custom agent) files, and what a file sets. Formats differ (Codex is TOML; the rest are Markdown with YAML frontmatter), so § Agent-definition fidelity checklist applies to opencode files only. Basis: `corpus/knowledge/agent-definition-files-round56.md` (S072–S078; Claude Code schema from its sub-agents page, S026); locations and quotes checked by `verifiers/check_agent_definitions.py`, the other cells are reviewer readings.

| Client | Definition location | What the file sets | Action |
|---|---|---|---|
| Claude Code | `.claude/agents/` (user `~/.claude/agents/`) | Markdown with YAML frontmatter, body is the system prompt; `name` and `description` required; `tools` allowlist; optional `model`; `disallowedTools` denylist (schema: sub-agents page, S026) | Write project subagents here and check keys against Claude Code's schema, not the opencode checklist |
| Codex | `.codex/agents/` (user `~/.codex/agents/`) | Standalone TOML, not Markdown; `name`, `description` and `developer_instructions` required; `model` keys; five supported `features.*` keys set to false turn capabilities off; permissions, sandbox and MCP servers come from the parent | Author TOML files; never port Markdown frontmatter to Codex |
| VS Code | `.github/agents` (user: `~/.copilot/agents` for the Copilot harness, profile storage for Local; also `.claude/agents` in Claude format) | `.agent.md` or `.md` Markdown with optional YAML frontmatter: `name`, `description`, `tools` | Put shared agents in the workspace folder and list their tools |
| Copilot CLI | `.github/agents/` (user `~/.copilot/agents/`) | Markdown profiles (`.agent.md`; `.md` also recognized); frontmatter with optional `name` and `tools` (full schema on a linked reference page, not a SOURCES row); the personal profile wins on the same ID | Keep repository profiles in the project folder and check which copy wins |
| Gemini CLI | `.gemini/agents/*.md` (user `~/.gemini/agents/*.md`) | Markdown with YAML frontmatter; `name` and `description` required for local agents; optional `tools` and `model`; on by default, off with `experimental.enableAgents: false` in `settings.json` | Commit team agents here and keep personal ones in the home folder |
| Cursor | `.cursor/agents/` (user `~/.cursor/agents/`; also reads `.claude/agents/` and `.codex/agents/`) | Markdown with YAML frontmatter; `name` (defaults to the file name), `description`, `model`, `readonly`, `is_background`, all optional; `readonly` restricts writes | Review Cursor's own schema; project and `.cursor/` files win name conflicts |
| opencode | `.opencode/agents` (user `~/.config/opencode/agents/`; V2 still discovers `agent/`, `agents/`, `mode/` and `modes/` per its pinned migration page `migrate-v1.mdx:486`, re-opened in round 56, not a SOURCES row) | Markdown frontmatter, body is the system prompt; V1 docs require `description` and use `permission` (`tools` deprecated); V2 uses `permissions` and ignores V1 fields mixed into a V2 file | Apply the checklist below to V1-format files only; convert a file's frontmatter to V2 all at once |

### Plugin manifests by client

A skill, agent, command or rule file can arrive inside a plugin (Gemini CLI: an extension) rather than from the project tree; find its manifest first. Each row leads with the client's own-format manifest path, else the default its docs name. Basis: `corpus/knowledge/plugin-manifests-round57.md` (S079–S088; S086 and S087 correct S080 and S085); `verifiers/check_plugin_manifests.py` checks the location and quote of eligible rows only (a shared root `plugin.json` and the opencode folder are not eligible), the other cells are reviewer readings.

| Client | Plugin manifest | What a plugin can ship | Action |
|---|---|---|---|
| Claude Code | `.claude-plugin/plugin.json` (optional; all other files at the plugin root) | skills (a root `SKILL.md` loads as one skill when there is no `skills/` folder and no `skills` key), commands (files or inline Markdown), agents, hooks, MCP and LSP server configs, MCP-bound message channels, output styles, workflows, themes, monitors, `bin/` executables, `agent`/`subagentStatusLine` defaults; a plugin-root `CLAUDE.md` is not loaded as context (put instructions in a skill) | Look in the plugin root when a skill or agent is not in the project tree |
| Codex | `.codex-plugin/plugin.json` (compatibility manifest the plugin creator scaffolds; portable packages use root `plugin.json`) | skills (including an onboarding skill users run at setup), MCP servers via `mcp.json` (the scaffold's optional `.mcp.json` starts with an empty `mcpServers` object), server mappings via `.app.json`, lifecycle hooks for manually installed desktop plugins, assets; the manifest example's `interface.defaultPrompt` holds prompt strings | Check both manifest forms before trusting bundled instructions |
| VS Code | `plugin.json` at the plugin root (Agent Plugins 1.0 and the default Copilot format; also reads `.claude-plugin/plugin.json` and Legacy OpenPlugin `.plugin/plugin.json`) | portable skills and MCP servers; agents, commands, rules and hooks under `com.github.copilot` in Agent Plugins 1.0; VS Code-specific automation templates | Identify the plugin format before moving components |
| Copilot CLI | `plugin.json` at the plugin root (legacy locations on its CLI plugin reference) | agents, skills, hooks, MCP server configs; in Agent Plugins 1.0 the Copilot-specific agents, commands, rules, hooks and LSP servers come from `com.github.copilot` (legacy plugins can name component paths in `plugin.json`) | Read the manifest before the bundled skills |
| Gemini CLI | `gemini-extension.json` (required, each extension root) | MCP servers, a context file (`contextFileName`; otherwise root `GEMINI.md` if present), TOML commands, hooks in `hooks/hooks.json`, skills, sub-agents (preview), policy rules and safety checkers; extensions load from `<home>/.gemini/extensions` | Audit the extension's context file as always-on text |
| Cursor | `.cursor-plugin/plugin.json` (Cursor Plugins; Agent Plugins use root `plugin.json`) | Cursor Plugins: rules, skills, agents, commands, MCP servers, hooks, and a user-configuration `variables` schema; Agent Plugins: skills and MCP servers; local development from `~/.cursor/plugins/local`; for Cursor Plugins, a root `SKILL.md` is a single-skill fallback only if neither a `skills/` folder nor a manifest `skills` field exists | Name the plugin format before packaging rules |
| opencode | `.opencode/plugins/` (local JavaScript/TypeScript modules, also global `~/.config/opencode/plugins/`; a published package's `package.json` is its minimal manifest) | code that registers commands, MCP server configuration, skills and tools, transforms existing agents, sends session prompts, and installs hooks that edit incoming prompts and outgoing system instructions | Review the module code and, for published packages, `package.json` |

### Custom command files by client

A reusable prompt the user invokes by typing `/name` lives in a command (prompt) file, not a skill: the user invokes it (Claude Code: a same-named skill wins, S089 `:214`). Before auditing one, find the folder the client reads and what a file may set; full quotes in `corpus/knowledge/command-files-round58.md` (S089–S095, S028).

| Client | Command files | What a file sets | Action |
|---|---|---|---|
| Claude Code | `.claude/commands/` (project; personal files under `~/.claude/`, S089 `:276`) | Markdown; `deploy.md` → `/deploy`; skill frontmatter except `name` and `paths`; `argument-hint`, named `arguments` for `$name` (S089 `:172,378,402-403,450`) | Audit it like a skill; the page calls it the older format, so author new work as a skill |
| Codex | `~/.codex/prompts/` (user only; not shared through the repo) | Markdown; `draftpr.md` → `/prompts:draftpr`; frontmatter `description`, `argument-hint`; `$1`–`$9`, `$ARGUMENTS` (S090 `:10,18,34,40-42`) | Deprecated for skills: never ship one in a repo, migrate it to a skill |
| VS Code | `.github/prompts` (workspace; user files in the profile) | `.prompt.md` Markdown; optional `description`, `name` (after `/`, defaults to the file name), `argument-hint`, `agent`, `model`, `tools`; `${input:…}` (S091 `:35,39-44,69-70`) | Local harness only: for other harnesses write an agent skill |
| Copilot CLI | no own folder: it loads Claude Code's .claude/commands/, and commands rank below same-named skills (S028 `:456`; S031 `:1334`) | Claude Code's command files; the CLI reference lists a shorter field set (S031 `:1334`) | Author in Claude Code's folder; a same-named skill wins |
| Gemini CLI | `~/.gemini/commands/` (user; project `.gemini/commands/`) | TOML `.toml`; required `prompt`, optional `description`; path → name, subfolders → `:` namespaces; `{{args}}` (S093 `:8-17,25-27,41-42,58-67`) | Write TOML, not Markdown; check the project and user copies |
| Cursor | `.cursor/commands` (scope not printed on the cited pages) | Markdown workflow prompt; these pages document no frontmatter or argument schema (S094 `:54`, `customize-cursor.md:31`) | Audit the body; check Cursor's current docs for any newer schema |
| opencode | `.opencode/commands/` (project; user `~/.config/opencode/commands/`) | `.md` only; nested path → `/`-separated name; optional YAML frontmatter; trimmed body is the template; `$ARGUMENTS`, `$1`–`$n`; legacy singular `command/` still read (S095 `:21,28,34,37,99,109`) | Keep the body a complete prompt template |

### Hook files by client

A rule the model must follow every time is still text it reads; a command hook is a command the client runs at an event (Claude Code also has prompt and agent hooks a model evaluates, S096 :395-396). VS Code: hooks act "without relying on the model to request the action" (S098 `:6`); Copilot: "Unlike custom instructions, hooks run code rather than asking the model to follow a rule." (S099 `:15`). Route a must-run check to the client's hook file; plugin-bundled hook files are § Plugin manifests by client, writing or running hook code is out of scope (round-13 census), and host package/initramfs hooks are tsukuroi's. Basis: `corpus/knowledge/hook-files-round59.md`, S096–S101 (vendor pages, not a runtime test).

| Client | Hook config | Events | Action |
|---|---|---|---|
| Claude Code | `.claude/settings.json` (project; user and local settings files too, S096 :243-245) | `PreToolUse`, `SessionStart` (S096 :37, :33) | Move a check that must run before a tool call into a hook here; review and test each command first, it runs with your user permissions (S096 :4146) |
| Codex | `~/.codex/hooks.json` (first of the page's four locations; repo layers and inline config.toml tables too, S097 :30-46) | `PreToolUse`, `SessionStart` (S097 :25, :27) | Put the hook here; by default a non-managed hook runs only after it is reviewed and trusted (S097 :19; a per-invocation bypass flag exists, :76-78) |
| VS Code | `.github/hooks/*.json` (repository-shared, Copilot harness sessions, S098 :18; other session targets use their own hooks, :22-30; personal, settings, plugin and agent sources too, S098 :58-62) | `preToolUse`, `sessionStart` (S098 :130, :128) | Preview (S098 :4); review hook config and scripts before use, they are executable code (S098 :202) |
| Copilot CLI | `~/.copilot/hooks/*.json` (personal; repository hooks share the VS Code row's folder pattern, S099 :28) | `preToolUse`, `sessionStart` (S099 :37, :34) | Check each event on each surface before relying on it: the page says not to assume events work unchanged across surfaces (S099 :26) |
| Gemini CLI | `.gemini/settings.json` (project, S100 :413) | `BeforeTool`, `AfterModel` (S100 :31) | Verify the source of project hooks before enabling them (S100 :442) |
| Cursor | `.cursor/hooks.json` (project; the user file is not available to cloud agents, S101 :102) | `preToolUse`, `postToolUse` (S101 :27, :67; cloud agents defer `sessionStart`, :88, self-hosted workers fire it, :104) | Keep cloud-agent checks in the project file; project hooks run only in a trusted workspace (S101 :649, :781) |
| opencode | no hook file: hook code is a plugin module (§ Plugin manifests by client; S085, S087) | `execute.before`, `execute.after` (V2 plugin API, V1 used tool.execute.before/after; S085 index.mdx :1738, :1746) | Read the plugin module; do not look for a hook config file |

### Scoped rule files by client

A rule that matters only for some files can live in a scoped rule file the client loads only for matching paths; every-session constraints stay in the always-on file (§ Always-on constraint-file checklist) and a check that must run at an event is a hook (§ Hook files by client). Basis: `corpus/knowledge/scoped-rules-round60.md`, S103–S109 (vendor pages, not a runtime test; S103, S106, S108 re-open S043, S048, S049). VS Code's row is its Local/Copilot-harness behaviour (S105 :32); Codex, Gemini CLI and opencode scope by directory instead.

| Client | Rule files | Scope key | Action |
|---|---|---|---|
| Claude Code | `.claude/rules/` (multi-file instructions, scoped to matching files; S103 :168) | `paths` (e.g. `src/api/**/*.ts`, S103 :198) | Scope rules to specific files using YAML frontmatter; apply only when matching specified patterns. (S103 :194) |
| Codex | no scoped rule file: AGENTS.md instructions are discovered by directory walk (S104 :12) | none (the project-root-to-current-directory walk determines loaded instructions, S104 :12) | Use nested AGENTS.override.md/AGENTS.md for directory-specific instructions, not matching-file rules (S104 :12) |
| VS Code | `.github/instructions/**/*.instructions.md` (Local-harness targeted instructions, S105 :32) | `applyTo` (`**/*.py`, S105 :164) | Use multiple instruction files per topic and apply them selectively (S105 :329) |
| Copilot CLI | `.github/instructions/**/*.instructions.md` (modular repository instruction files, S106 :18) | `applyTo` (e.g. `app/models/**/*.rb`, S106 :66) | Create a path-specific instruction file with an `applyTo` glob; use glob syntax to specify the files or directories the instructions apply to (S106 :60). |
| Gemini CLI | no scoped rule file: directory-scoped GEMINI.md context with just-in-time discovery (S107 :31-35) | none (directory and ancestor lookup scope context instead of a path-pattern key, S107 :31-33) | Put component-specific instructions in GEMINI.md context files; JIT discovery scans the accessed directory and its ancestors (S107 :31-33) |
| Cursor | `.cursor/rules` (project rule folder for `.mdc` files, S108 :32) | `globs` (example `src/components/**/*.tsx`, S108 :85) | Use `globs` to scope a rule to specific files or directories. Separate multiple patterns with commas. (S108 :131) |
| opencode | no scoped rule file: AGENTS.md guidance is directory-scoped, not matching-work-file scoped (S109 :64) | none (directory placement governs scope, S109 :64) | Place AGENTS.md in the project root; its guidance applies in that directory and its subdirectories (S109 :64) |

## Router model — which harness, which gate

Two harnesses consume skills here, and neither shares the other's catalogue
tag, render, or offer gate. Read the harness's own artifacts before predicting
a render — a rule proven on omp is wrong on opencode.

| Harness | Catalogue tag | Description render | Offer gate (action) | Failure mode |
|---------|---------------|--------------------|---------------------|--------------|
| omp | `<skills>` (ELF template) | `cache.get(key) ?? previewSkillDescription` — cached LLM line, else deterministic truncator (`_8n=100`; first sentence if ≥40 chars, else last-space cut + `…`); hard 99-char cliff | Ship the dir under an omp discovery root (`~/.agents/skills`, `~/.omp/agent/skills`, `~/.claude/skills`, project walk-up) and front-load the capability + WHEN into the first ≤99 chars | Trigger material past offset 99 or in sentence 2 renders as nothing (all 13 observed `Triggers:`/反触发/`Excludes` clauses lost) |
| opencode | `<available_skills>` (`fmt(list,{verbose:true})`) | Full `description` byte-for-byte + `<location>` in the system-prompt catalogue; no truncation, no cache (the TUI skill list collapses whitespace only) | Define `description` and a frontmatter `name:`; leave the `skill` permission enabled; if a same-name duplicate exists, do not rely on which copy wins | Missing `description` is filtered out of the catalogue; a denied `skill` permission omits the whole block; duplicate names are last-parsed-wins under unbounded parse concurrency (round-9 re-verify: first-scanned-wins was wrong) |

Check before predicting: on omp read the cache db
(`sqlite3 -readonly ~/.omp/agent/skill-descriptions.db "select count(*) from
skill_descriptions;"`) **and** the newest *catalogue-bearing* `<skills>` block —
mtime order is not a selection rule: the newest session file
(`~/.omp/agent/sessions/<project-slug>/<ts>/<Agent>.jsonl`) may carry no
`<skills>` block (round-8 box-3 cold run's B1), so take the two fields the verifier already resolves:
`python3 verifiers/verify_harness_claims.py --json` → `omp.catalogue_path` /
`omp.catalogue_timestamp`. The catalogue freezes at session start, so db coverage
is time-varying; on opencode read the global roots and
`grep -o 'message=init count=[0-9]*' ~/.local/share/opencode/log/opencode.log`.

### Run the verifier instead of re-typing the recipe

`python3 verifiers/verify_harness_claims.py` recomputes this whole table from
live state against `verifiers/baseline.json` and exits non-zero on drift —
**28 checks**: the omp key prefix read out of the ELF
(`omp.elf.template_sha256`, 273 B), `keys_reproduced` per offered skill under the
style-aware salt, cache-miss/truncation count, the newest captured `<skills>`
block matched line-by-line against the cache, offered vs dangling skill dirs,
name==folder, unmodelled YAML scalar forms (excluded, never guessed), opencode
`init count` max vs root-union+builtin, `<available_skills>` hits, per-root
duplicate split, `skill`-permission allow lines. Exit 0 agree / 1 drift
/ 2 environment unreadable / 3 no baseline; `--self-test` falsifies the script's
own truncator + block-scalar model. Cite this file for any harness number rather
than a hand-run recipe, and update the baseline only with a LOG entry naming the
mechanism that moved. Model + gaps: `corpus/knowledge/harness-verifier-round10.md`.

`python3 verifiers/verify_skill_checklist.py` executes this file's own checklist:
**11 checks** (`checklist.box_map_complete` + the eight boxes marked
`(executed: …)` below + `trigger.no_xml_tag`, bound to no box since round 47 +
`governance.citation_resolves` over the two root governance files), each fail-closed on fixtures, `evaluated N` per check,
exit 0/1/2/3 (`3` = box map missing, unparseable, or bound elsewhere).
`verifiers/checklist-baseline.json` maps **all 41 boxes** (8 executed, 2
delegated, 31 unexecuted with reason) by text hash, so drift FAILs. The two
delegated boxes are the dispatch-prompt fidelity boxes `dispatch.04` and
`dispatch.08`, run by `verifiers/verify_dispatch_prompts.py` (its
`--box-proof` prints `boxes proven 2` only when both boxes are delegated there
and each of its six named conjuncts has an isolated must-fail case, judged on
observed statuses; the checklist gate runs `--box-proof` only when the
delegate's `--help` output contains the flag text (a substring test) — a probe that times out, cannot
execute or does not show the flag is reported PASS with "not run", so the gate
fails open there, and a relative `--map` run from another directory gives a
false red and non-UTF-8 `--help` output crashes the gate
(`.ufo/waves/round-50/falsify/ReviewBoxProofGate.md` F1–F5, carried); the
unsubstituted-variable clause, the `≤` equality boundary, the legacy-state
arm and a non-digit round folder have no fixture yet). Limits and ceilings: `corpus/knowledge/checklist-execution-round17.md`.

## Frontmatter craft — the trigger surface

Render mechanism and the twelve trigger-craft rules: `corpus/knowledge/render-mechanism-round7.md` § Moved from SKILL.md § Frontmatter craft (round 56), verbatim; rules in `corpus/knowledge/frontmatter-trigger-surface.md` § Craft rules.

Portability floor (spec + vendor + YAML, `corpus/SOURCES.md` S018, S002, S019, S008): `name` ≤64 lowercase letters, digits and single hyphens, equal to the directory (the spec's charset wording is ambiguous on Unicode); `description` ≤1024 chars, no XML tags (Anthropic rule), quoted when it holds `: ` or ` #` (illegal in a YAML plain scalar — lenient loaders hide it, strict ones reject). `verifiers/verify_skill_checklist.py` `trigger.no_xml_tag` approximates the XML-tag rule lexically on the unparsed `name`/`description` text; Anthropic's packager (S012) refuses any `<`/`>` in the parsed value, so the two disagree in both directions. Which authority imposes which rule, with run counterexamples: `corpus/knowledge/frontmatter-rule-authorities-round48.md`.

### Description thresholds by client

A documented maximum is not a render cut: four clients state 1,024 and none documents a cut there, Claude Code and Codex cut or budget the listing, omp cuts at 99 (§ Router model). Basis: `corpus/knowledge/skill-listing-thresholds-round54.md` (S053–S059, S062–S064), checked by `verifiers/check_description_thresholds.py`.

| Client | Documented threshold | Past the threshold | Action |
|---|---|---|---|
| Claude Code | 1,536 characters per entry (`description` + `when_to_use`), whatever the budget; listing budget 1% of the context window (`0.01` default, `skillListingBudgetFraction`) | Truncated at the cap, with a startup warning (v2.1.105 raised the cap from 250); past the listing budget, descriptions of the least-invoked skills are dropped and every skill name stays | Put the key use case first and keep `description` within the spec's 1,024 (the listing cut is 1,536); raise `skillListingMaxDescChars` or `skillListingBudgetFraction`, or set low-priority skills `"name-only"` to leave budget for yours |
| Codex | Initial skills list: 2% of the model's context window, or 8,000 characters when the context window is unknown; `skills.max_context_tokens` sets a different budget, capped at 10,000 tokens | At the initial-list budget, Codex shortens descriptions first; for large skill sets it may omit skills from the initial list with a warning; selecting a skill still reads the full `SKILL.md`. | Front-load the use case and trigger words in `description` so matching survives shortening; do not rely on a long tail |
| VS Code | `description` maximum 1024 characters (authoring maximum; `name` 64) | Not documented: the page states no truncation, drop, warning or refusal past 1024, and no listing budget | Keep the description under 1024 characters, leading with what the skill does and when to use it |
| Copilot CLI | `description` max 1024 characters | Not documented; the page states the cap and no truncation, shortening or refusal | keep the description at 1024 characters or fewer, front-loaded on what the skill does and when to use it |
| Gemini CLI | No threshold: ~100 words is a size estimate for metadata (name + description), which is always in context. | The loader keeps `frontmatter.description` as-is (`skillLoader.ts:211`) and the prompt template inserts it directly (`snippets.ts:320`) at `google-gemini/gemini-cli@451a02ff`; no description cut appears in these steps, so longer descriptions spend context. | Treat ~100 words as the docs' size estimate, not a limit: keep name + description short and move detail into the `SKILL.md` body, which loads only after activation (`skills-best-practices.md:24-25`) |
| Cursor | 1,024 characters for `description` | No cut documented; the release notes document a warning: the skill still loads and `/skills` shows a yellow warning count listing what to fix (a body over about 5,000 tokens is warned the same way) | Keep `description` at or under 1,024 characters; an over-limit skill still loads and gets a yellow warning in `/skills`. |
| opencode | 1-1024 characters (v1 docs page; the v2 page says it enforces no maximum) | nothing: no cut, truncation, warning or refusal — both shipped trees print the whole string into `<available_skills>` (v1.19.4 `skill/index.ts:332`, v2.1.3 `skill/instructions.ts:21`) | keep the description inside 1-1024 characters, the rule the spec states too (S018), and front-load it for the clients that cut or shorten; opencode itself shows all of it |

### Explicit invocation by client

An implicit-trigger measure (Frontier *Implicit-intent fidelity*) must first set aside activations of a skill the turn named. Match the form on the raw turn text, before any slash-stripping cleanup, and set aside only the named skill's activation — another skill the model picks in the same turn still counts. The form says what the user-role text held, not who wrote it (a dispatcher can inject `/skill:godspeed`). Basis: `corpus/knowledge/explicit-invocation-round55.md` (S065–S071), checked by `verifiers/check_explicit_invocation.py`.

| Client | Explicit form | What it does | Action |
|---|---|---|---|
| Claude Code | `/skill-name` | Invokes the named skill directly; automatic loading stays possible unless `disable-model-invocation: true` (`skills.md:577`) | Mark that skill's activation explicit when the raw user text starts with its `/name`; count only the other activations as implicit |
| Codex | `$<skill-name>`, e.g. `$setup-demo-app` | Names the skill in the prompt so Codex invokes it when asked; `allow_implicit_invocation: false` keeps this and stops implicit use (S021) | Mark that skill's activation explicit when the raw user text holds `$` plus its name; only the rest can test description routing |
| VS Code | `/<skill-name>`, e.g. `/webapp-testing` | Invokes the named skill as a slash command, with optional context after it; `disable-model-invocation: true` makes this the only way (`:151`) | Mark that skill's activation explicit when the raw user text starts with its `/name`, even when task text follows |
| Copilot CLI | `/<skill-name>`, e.g. `/frontend-design` | Asks Copilot to use the named skill; without it Copilot picks skills from the prompt and each description (`add-skills.md:121`) | Mark that skill's activation explicit when the raw prompt holds `/` plus its name; the rest are description-routed |
| Gemini CLI | `activate_skill` (model tool call) | Loads the named skill after a description match, then asks the user to consent; the pages read document no user-typed form | Treat this call as the activation record, not as explicit intent: count it implicit unless the user's own text named the skill |
| Cursor | `/skill-name` | Attaches the named skill to one message (`cursor-skills.md:29`); with `disable-model-invocation: true` the agent will not apply it from context (`:175`), though a skill backing a Custom Mode stays in context all session (`:218`) | Mark that skill's activation explicit when the raw message holds its `/name`; for a flagged skill, also check whether a Custom Mode carried it |
| opencode | `@skill-id` | V2 docs: loads the named skill on the user's mention; `metadata["opencode/autoinvoke"]` set to false hides it from the model and keeps this path (`skills.mdx:137,142`); the V1 page states loading by exact name only | Mark that skill's activation explicit when the raw prompt holds `@` plus its ID; other `skill` tool calls the model makes in the turn stay implicit |

Decision-table shape (situation → table or plain steps) and the action-cell rule — every row needs an action cell (command, route, named fallback, or verdict), need not be the last column: `corpus/knowledge/anatomy-and-compression.md` § Moved from SKILL.md § Decision tables (round 57), verbatim.

## Compression rules

Six rules with their evidence: `corpus/knowledge/anatomy-and-compression.md`
§ Compression rules. The two that decide most edits: spend tokens in the
`description`, not the body; and one authoritative home per fact — depth moves to
a file and the skill keeps the pointer line. Also there: verbatim-copyable
command blocks, failure signatures inline, never restate the trigger in the body,
and the **~600-line module bound** (round 15 applies it to this file — §
Trigger-fidelity checklist, line-budget box).

## Trigger-fidelity checklist

Run before shipping any SKILL.md. Every item is checkable by reading the file —
no runtime needed. (For AGENTS.md / dispatch prompts, use the per-surface rows
in "Instruction surfaces" instead — this checklist assumes a routed file.)

Eight of the fifteen boxes are **executed, not read** — marked
`(executed: <check-id>)`: `python3 verifiers/verify_skill_checklist.py` runs them
and exits non-zero on any FAIL. `verifiers/checklist-baseline.json` maps every box
in this file to `executed:` / `delegated:` / `unexecuted:<reason>`, pinned by the
box's text hash — a reworded, added, or removed box FAILs the run rather than
passing silently.

- [ ] Frontmatter parses: the file opens with `---`, closes it, and carries a
      non-empty `name:` and `description:`. A file with no frontmatter never
      reaches a router catalogue, so every other box is vacuous on it.
      (executed: `trigger.frontmatter_parses`)
- [ ] `name` matches the directory / invocation surface.
      (executed: `trigger.name_directory`)
- [ ] `description` contains ≥1 literal trigger string in quotes or an explicit
      `Triggers:` list. (executed: `trigger.literal_trigger_string`)
- [ ] `description` contains at least one anti-trigger or exclusion clause.
      (executed: `trigger.anti_trigger_clause` — vocabulary test, not semantics:
      a marker-bearing but vacuous clause passes unearned, and a real exclusion
      phrased outside the vocabulary fails unearned)
- [ ] Overlapping sibling skills are named **concretely** with an arbitration
      rule in the `description` (a generic "the owning domain skill" does not
      count; body/PROVINCE boundary text does not count — the offer stage reads
      frontmatter only (§ Router model)). Write `N/A — no overlapping sibling exists` when applicable:
      a bare absence is indistinguishable from an unconsidered one.
- [ ] Body opens with a one-line role statement, not a restatement of triggers.
- [ ] Every prerequisite — any binary, file, env var, or sibling artifact a
      body **procedure** assumes — has a **fail-closed** path stated ("if X is
      missing, stop and do Y; do not guess" — bailian-cli pattern), or is
      declared in `metadata.requires`. Carve-out: a tool named inside an
      evidence *recipe* (a "verify with `md5sum`" citation) is a suggested
      reproduction path, not a runtime prerequisite — it needs a resolvable
      citation base, not a gate.
- [ ] Every decision-table row contains an action cell (see the table rule
      above — need not be the last column).
- [ ] Every command (fenced block or inline) is runnable as pasted: its binary
      resolves on PATH or at a location the file declares; bins are declared
      in metadata or checked in a prerequisite step.
      (executed: `trigger.command_binary_resolves` — declared vocabulary + fenced
      shell blocks; flags and command semantics are not covered)
- [ ] Every failure claim — any warning, dominant-failure label, or causal
      "X breaks because Y" assertion — carries its observed signature (error
      text, exit code, version constraint) **or** is explicitly framed as
      design guidance, not an observed failure. No bare warnings.
- [ ] Every source citation resolves from a named base: repo-relative paths
      resolve from the file's own repo by default; any other root must be
      named in the file (`~/.config/opencode/opencode.json`, not bare
      `opencode.json`); bare basenames that exist under multiple roots fail.
      The mechanically checkable subset is *executed*, not read: every backticked
      token whose implied base is this repo (a `corpus/`, `verifiers/`, `opencode/`
      or `.ufo/` prefix, or a `../` hop) resolves from the repo root, or this
      build FAILs naming the line. The corpus-internal remainder (README index coverage,
      lane-report pointers, corpus-file `commit` citations) is the corpus instrument's scope, not this box's. (executed: `trigger.citation_resolves`)
- [ ] A claim that only its author's instrument settles names that as a gap, and
      its second witness is a **derivation, not a re-run** — an independent
      implementation of the class model compared check-for-check, red and green.
      A re-run (or a cold run) of the author's own script reproduces its bugs with
      it and cannot falsify it; agreement between two derivations is evidence, and
      their first disagreement is the finding. Worked example:
      `corpus/knowledge/independent-verification-round12.md`.
- [ ] Stale-risk facts (model names, versions, prices) are either pinned with a
      source or deferred to `--help` / reference files.
- [ ] File ≤ 600 lines; overflow already moved to referenced depth files.
      (executed: `trigger.line_budget` — the number in this box is the threshold;
      `--max-lines` applies only when the box states none)
- [ ] No `TODO`, placeholder sections, or "coming soon" — a skill ships complete
      or names the missing prerequisite.
      (executed: `trigger.no_placeholder` — a line that names the marker after a
      negation, or quotes it in backticks, is read as the rule, not a stub)

## Agent-definition fidelity checklist

Run before shipping any `opencode/agents/*.md`. Every item is checkable by
reading the file plus two roster artifacts: `opencode.json` `agent` map and
the `subagents:` lists of reachable orchestrator agents. (For SKILL.md files
use the trigger-fidelity checklist; for AGENTS.md the surface row's craft
rule — terse imperatives only.)

- [ ] `name` matches the file stem. Absent `name:` fails latent (opencode
      falls back to stem) — still a defect when every sibling declares it.
- [ ] Reachability: the agent is enrolled in `opencode.json` `agent` map or in
      a reachable agent's `subagents:` roster. An orphan file delegates to no
      one — it is dead text until enrolled.
- [ ] `description` carries a capability clause plus an explicit routing cue:
      a named domain, tool, or axis — or negative routing (`NOT …`).
      Capability-only descriptions are the agent-surface twin of the shonen
      template defect.
- [ ] Frontmatter keys resolve *against the target harness's agent schema*
      (not a fixed list — observed extras: `mode`, `variant`,
      `cascade_class`, `steps`, permission maps): `subagents` entries name
      existing agent files/keys; `model`/`cascade` strings parse as
      `provider/model`; delegated names in body tables match enrollment keys
      (`the-scout` vs `scout` mismatch is a defect — only `the-janitor` is a
      real `the-` binary on this host).
- [ ] No dated operational text in frontmatter *including `description`*
      (`until <date>`, timestamps, live seat assignments, round-indexed
      routing notes like "Mandatory every PROPOSE round") — dated facts
      belong in status files; frontmatter holds stable policy. Dated body
      anecdotes are covered by the next item's staleness rule.
- [ ] Body is persistent identity + constraints, not per-task job text — no
      "your current task", round numbers, or one-shot instructions that go
      stale between delegations.
- [ ] No duplicated blocks in the body — the same paragraph must not appear
      twice (copy-paste posture zones; check repeated line runs) *and* no
      same-name blocks with differing content (labrat.md carries two
      different DESPAWN templates; a conflicting near-duplicate is a
      conflict defect, not a pass).
- [ ] No trigger restatement: the body assumes delegation succeeded —
      "when to use this agent" belongs in `description`/`whenToUse`.
- [ ] Every external command *and file path* named in the body resolves:
      binary on PATH (`command -v`), absolute path declared, file path
      resolvable from the file's own dir or a named base, or a prerequisite
      check stated (scout.md `aaron` on no PATH = fail). Harness tool/role
      literals (`SendMessage`, `TaskCreate`) aren't commands — they're
      governed by the host tool surface, not this item.

## Dispatch-prompt fidelity checklist

Run before shipping any `*-L1.md` / `*-round-N.md` dispatch prompt (observed
form: `/home/vgpnk/Projects/shokunin/.ufo/prompts/`). Checkable by reading the file; round-7 application +
full failure matrix in `corpus/knowledge/dispatch-prompt-audit-round7.md`
(37/43 files failed ≥1 item — the artifact population is dirtier than the
template).

- [ ] Shape matches mode: spawn files carry all 6 stanzas (9–12 lines);
      round files are 3–4 lines.
- [ ] Spawn stanza order: role+dir → context → job → L2 routing map →
      report path + scope fence → `| godspeed`.
- [ ] `| godspeed` is the literal final line.
- [ ] Report path is literal — no `<…>` placeholder or unsubstituted
      variable; filename = the lane's `<id>` (a `<lane>` placeholder cost two
      lanes their canonical round-1 report names).
- [ ] Round files carry delta only — the L2 routing map belongs in a durable
      file the lane re-reads (MISSION.md), not restated per round with
      driftable aliases (30/35 round files restate it; 3 stale aliases in
      38 files).
- [ ] Self-contained for a blank-context reader: no deictic references;
      every path/command literal resolves (`kengaku-L1.md` named a dead
      `~/wikillm/llm-wiki` grounding path).
- [ ] No literal `\n` escapes or duplicated stanza blocks — the file is
      parsed once, not templated twice.
- [ ] Round token `<N>` is identical across filename, role line, and report
      dir, and ≤ the lane's latest dispatched round — the first field of
      `.ufo/state/<id>.report-baseline` (hyaku driver); a lane with only the
      legacy `<id>.round` file (frozen since 2026-10-15) is reported
      `state-stale`, not compared; a lane with neither is N/A (equality against
      a sibling's state is wrong).
- [ ] Scope fence explicit: names what the lane MUST NOT write plus the dir
      it may write.

## Always-on constraint-file checklist (AGENTS.md-class)

Run before editing any always-loaded rules file. Round-7 evidence +
application matrix (6/6 repo files passed; the host `~/.agents/AGENTS.md`, then
75 lines and 14 at round 53, failed procedures/dates/style) in
`corpus/knowledge/alwayson-checklist-round7.md`. Boxes 4 and 7 run one at a time as
`python3 -B verifiers/verify_alwayson.py --check alwayson.04 --target <dir>` (and
`--check alwayson.07`); which name each client reads and what counts as a redirect:
`corpus/knowledge/alwayson-rule-files-round53.md`.

- [ ] Constraint-only content: durable rules/prohibitions/boundaries — no
      history, status, or rationale prose.
- [ ] No how-to procedures or command recipes; a single durable required
      *outcome* (e.g. "append a LOG entry") is allowed.
- [ ] No trigger/dispatch material — no activation or routing conditions.
- [ ] No dated or transient text; dates and live-state go to status files.
- [ ] Terse imperative style; no narrative paragraphs.
- [ ] Template-family consistency: a copied family keeps identical shared
      body; per-file substitutions only where declared.
- [ ] One canonical rule-file name per repo (AGENTS.md **or** CLAUDE.md, or
      an explicit redirect).
- [ ] Size justified per line: expansion = distinct every-session
      constraints only.

## Anti-patterns

Twenty rows with their observed evidence:
`corpus/knowledge/fail-closed-and-anti-patterns.md` § Anti-pattern table (full,
moved from `SKILL.md`, round 15 — read it before shipping any skill file). The
five highest-frequency rows: description without trigger strings; anti-trigger in
the body only; warning without a signature; a bin invoked with no declared
location; durable policy copy-pasted into a dispatch prompt.

Error pattern (round 50, corrected round 51): two sibling descriptions that both match, with nothing in either text saying who owns what; the eight pages from five clients read in `corpus/knowledge/skill-selection-rules-round50.md` document no rule between two such skills. Fix, when both should stay automatic: name the neighbour and the split in the description (`trigger.05`). The full text that stood here, with its check command, moved verbatim in round 55 to `corpus/knowledge/skill-overlap-levers-round51.md` § Moved from `SKILL.md`.

Overlap levers by client (round 51, `corpus/knowledge/skill-overlap-levers-round51.md`): each client documents a lever that removes one named skill from the candidates; none decides between two skills that both remain candidates, and the removed skill also stops firing automatically. When to use one, and what is reviewer judgment: that entry § Moved from `SKILL.md`. Checked by `python3 -B verifiers/check_overlap_levers.py`.

| client | lever | held by | effect | row | key term |
|---|---|---|---|---|---|
| GitHub Copilot SDK | list the skill in the session's disabled skills | app developer | removed in a scope | S030 | `disabledSkills` |
| GitHub Copilot CLI | frontmatter flag; the agent stops invoking the skill on its own | skill author | automatic choice off | S031 | `disable-model-invocation` |
| VS Code | frontmatter flag; manual `/` invocation only | skill author | automatic choice off | S025 | `disable-model-invocation` |
| Claude Code | frontmatter flag; description out of Claude's context, `/name` still works | skill author | automatic choice off | S022 | `disable-model-invocation` |
| opencode | skill metadata key; out of the model-facing list, still loadable by exact name | skill author | automatic choice off | S024 | `metadata["opencode/autoinvoke"]` |
| Gemini CLI | command disabling one named skill, user scope by default, `--scope workspace` for one project | user or operator | removed in a scope | S029 | `/skills disable <name>` |
| Codex | per-skill policy turning off implicit invocation | skill author | automatic choice off | S021 | `allow_implicit_invocation` |

## Refusals

- Won't fabricate domain content: claims need a file, a command output, or a
  cited source (repo AGENTS.md rule).
- Won't audit the *content* of another skill's `reference/` tree — that's the
  owning domain's province. Report cross-domain evidence back, don't absorb it.
- Won't produce a description without anti-triggers, or a body without a
  fail-closed path for its prerequisites.

## Gate registry

Registry home under PROTOCOL.md § Gate standard (round 54; what each one checks: `verifiers/README.md`).
Run commands from the repo root; `<rev>` is a full hash, never a moving ref. An undeclared nonzero code
reads as could-not-evaluate. `python3 -B verifiers/check_gate_registry.py --rev <rev>` compares rows with files.

| Name | Kind | Entry command | Verdict map | Self-test | Pinned values | Write scope | Owner |
|---|---|---|---|---|---|---|---|
| `verifiers/box_proof_case_deletion.py` | gate | `python3 -B verifiers/box_proof_case_deletion.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | `verifiers/checklist-baseline.json`, `verifiers/fixtures/dispatch-prompts/manifest.json` | temp exports under `$TMPDIR` | kotoba |
| `verifiers/check_agent_definitions.py` | gate | `python3 -B verifiers/check_agent_definitions.py --rev <rev> --fetch` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | none; `--fetch` reads the network | kotoba |
| `verifiers/check_agentdef_boxes.py` | gate | `python3 -B verifiers/check_agentdef_boxes.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate — claim withdrawn r56 before data; not a claim gate until redesigned and re-controlled | `--self-test` | in-file | temp archives and per-case dirs under `$TMPDIR` (removed) | kotoba |
| `verifiers/check_alwayson_boxes.py` | gate | `python3 -B verifiers/check_alwayson_boxes.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | temp archives and self-test repos (removed) | kotoba |
| `verifiers/check_assertion_floors.py` | gate | `python3 -B verifiers/check_assertion_floors.py` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | `verifiers/floors-registry.json` | temp fixtures under `$TMPDIR`; removable temp dirs under `verifiers/fixtures/compare-harness-independent` (nested self-test) | kotoba |
| `verifiers/check_callee_rename.py` | gate | `python3 -B verifiers/check_callee_rename.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | temp dirs under `$TMPDIR` (removed) | kotoba |
| `verifiers/check_command_files.py` | gate | `python3 -B verifiers/check_command_files.py --rev <rev> --fetch` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | self-test repos under `$TMPDIR` (removed); `--fetch` reads the network | kotoba |
| `verifiers/check_correction_sweep.py` | gate | `python3 -B verifiers/check_correction_sweep.py --root .` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | none; self-test fixtures under `$TMPDIR` | kotoba |
| `verifiers/check_could_not_evaluate.py` | gate | `python3 -B verifiers/check_could_not_evaluate.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | temporary clone (removed) | kotoba |
| `verifiers/check_description_thresholds.py` | gate | `python3 -B verifiers/check_description_thresholds.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | none; `--fetch` reads the network | kotoba |
| `verifiers/check_explicit_invocation.py` | gate | `python3 -B verifiers/check_explicit_invocation.py --rev <rev> --fetch` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | none; `--fetch` reads the network | kotoba |
| `verifiers/check_gate_finding_delta.py` | gate | `python3 -B verifiers/check_gate_finding_delta.py --base <rev> --head <rev>` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | `verifiers/corpus-baseline.json` | temp trees under `$TMPDIR` | kotoba |
| `verifiers/check_gate_registry.py` | gate | `python3 -B verifiers/check_gate_registry.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | none | kotoba |
| `verifiers/check_hook_files.py` | gate | `python3 -B verifiers/check_hook_files.py --rev <rev> --fetch` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | self-test repos under `$TMPDIR` (removed); `--fetch` reads the network | kotoba |
| `verifiers/check_scoped_rules.py` | gate | `python3 -B verifiers/check_scoped_rules.py --rev <rev> --fetch` | 0=clean, 1=failed, 2=could-not-evaluate — redesigned v3 round 61 (provenance-authenticating arms; measured on seven r60 worlds), the round-60 exploratory ruling (E2) unchanged; round-62 arm audit: `errata measured 5 of 5; absorbed 2 of 5; surviving 6; controls 2 of 2` — the E2c/E2e/E2f arm classes survive and G9 compound-purpose stays a declared bound; the v3.1 successor is separate evidence, not this gate | `--self-test` | in-file | self-test repos under `$TMPDIR` (removed); `--fetch` reads the network | kotoba |
| `verifiers/check_routed_repairs.py` | gate | `python3 -B verifiers/check_routed_repairs.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | none (read-only) | kotoba |
| `verifiers/check_erratum_absorption.py` | gate | `python3 -B verifiers/check_erratum_absorption.py --self-test` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | none (read-only) | kotoba |
| `verifiers/check_routed_repairs_v2.py` | gate | `python3 -B verifiers/check_routed_repairs_v2.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | none (read-only) | kotoba |
| `verifiers/check_scoped_rules_v31.py` | gate | `python3 -B verifiers/check_scoped_rules_v31.py --rev <rev> --fetch` | 0=clean, 1=failed, 2=could-not-evaluate — round-62 successor to the frozen v3 counter: closes five of the six measured survivor instances (E2c ×2, E2e ×2, E2f G7) with the r61 worlds/eligible line unchanged; G9 compound-purpose stays a declared bound; the frozen counter's bytes are unchanged | `--self-test` | in-file | self-test repos under `$TMPDIR` (removed); `--fetch` reads the network | kotoba |
| `verifiers/check_scoped_rules_v32.py` | gate | `python3 -B verifiers/check_scoped_rules_v32.py --rev <rev> --fetch` | 0=clean, 1=failed, 2=could-not-evaluate — round-63 successor to v31: adds the G9 cited-line clause guard (`;`/`and` clauses must clear A2's forward fraction at the cited line), prints `survivors closed 6 of 6` with three must-fail arms (E2e, G7, G9), and leaves the r61 `worlds reject 7 of 7; eligible rows pass 4 of 4` line and the frozen/v31 counters' bytes unchanged | `--self-test` | in-file | self-test repos under `$TMPDIR` (removed); `--fetch` reads the network | kotoba |
| `verifiers/check_r63_routed_repairs.py` | gate | `python3 -B verifiers/check_r63_routed_repairs.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate — round-63 C2 counter: five computed checks over the round-62 spot-check's routed defects (late write tracked, receipt revision named, entry size named, LOG append-only with growth, no-harm interim reds named); clean at `5 of 5`, failed at the r62 tip's `0 of 5` | `--self-test` | in-file | none (read-only) | kotoba |
| `verifiers/check_r64_routed_repairs.py` | gate | `python3 -B verifiers/check_r64_routed_repairs.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate — round-64 C2 counter: four computed checks over the round-63 spot-check's routed defects (seat edit committed, control revisions named, lowest axis corrected, assertion count named); clean at `4 of 4`, failed at base `078eec4`'s `0 of 4` | `--self-test` | in-file | none (read-only) | kotoba |
| `verifiers/check_seat_counts.py` | gate | `python3 -B verifiers/check_seat_counts.py --spec <spec> --dir <dir> --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate — round-62 routed-defect guard: a wave's committed seat reports are counted against the spec and every missing seat is named | `--self-test` | in-file | none (read-only) | kotoba |
| `verifiers/check_infoless_fences.py` | gate | `python3 -B verifiers/check_infoless_fences.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate — claim withdrawn r57 before data; not a claim gate until redesigned and re-controlled | `--self-test` | in-file | temp archives and per-case dirs under `$TMPDIR` (removed) | kotoba |
| `verifiers/check_mcp_instructions.py` | gate | `python3 -B verifiers/check_mcp_instructions.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | none; `--fetch` reads the network | kotoba |
| `verifiers/check_opencode_repin.py` | gate | `python3 -B verifiers/check_opencode_repin.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | `verifiers/surfaces-baseline.json`, `verifiers/baseline.json` | temp trees under `$TMPDIR` (removed) | kotoba |
| `verifiers/check_overlap_levers.py` | gate | `python3 -B verifiers/check_overlap_levers.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | self-test temp repo (removed); `--fetch` reads the network | kotoba |
| `verifiers/check_plugin_manifests.py` | gate | `python3 -B verifiers/check_plugin_manifests.py --rev <rev> --fetch` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | none; `--fetch` reads the network | kotoba |
| `verifiers/check_sibling_census.py` | gate | `python3 -B verifiers/check_sibling_census.py <census.md>` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | none; self-test repos under `$TMPDIR` | kotoba |
| `verifiers/check_sources_append_only.py` | gate | `python3 -B verifiers/check_sources_append_only.py --base 422ffd1082b3f4ae3ebda6060eb1a8d779f6dfd4 --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | none | kotoba |
| `verifiers/check_substrate_pins.py` | gate | `python3 -B verifiers/check_substrate_pins.py` | 0=clean, 1=failed, 2=could-not-evaluate, 3=could-not-evaluate | `--self-test` | `verifiers/baseline.json` | self-test files under `$TMPDIR` | kotoba |
| `verifiers/check_sweep_mutants.py` | gate | `python3 -B verifiers/check_sweep_mutants.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate — claim withdrawn r58 before data (plan erratum 1); not a claim gate until redesigned and re-controlled | `--self-test` | in-file | per-row temp git repos under `$TMPDIR` (removed) | kotoba |
| `verifiers/compare_harness_independent.py` | gate | `python3 -B verifiers/compare_harness_independent.py` | 0=clean, 1=failed, 2=could-not-evaluate, 3=failed | `--self-test` | `verifiers/harness-independent-scope.json`, `verifiers/fixtures/compare-harness-independent` | `--report`/`--receipt` targets; temp dirs | kotoba |
| `verifiers/fault_injection_corpus.sh` | gate | `verifiers/fault_injection_corpus.sh` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | temp clones under `${TMPDIR:-/tmp}` (removed) | kotoba |
| `verifiers/verify_alwayson.py` | gate | `python3 -B verifiers/verify_alwayson.py --check <box> --target <dir>` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | none | kotoba |
| `verifiers/verify_corpus_independent.py` | gate | `python3 -B verifiers/verify_corpus_independent.py` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | self-test fixtures under `$TMPDIR` | kotoba |
| `verifiers/verify_corpus_integrity.py` | gate | `python3 -B verifiers/verify_corpus_integrity.py` | 0=clean, 1=failed, 2=could-not-evaluate, 3=could-not-evaluate | `--self-test` | `verifiers/corpus-baseline.json` | self-test fixtures under `$TMPDIR` | kotoba |
| `verifiers/verify_dispatch_prompts.py` | gate | `python3 -B verifiers/verify_dispatch_prompts.py` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | `verifiers/checklist-baseline.json`, `verifiers/fixtures/dispatch-prompts/manifest.json` | self-test tree under `$TMPDIR` | kotoba |
| `verifiers/verify_harness_claims.py` | gate | `python3 -B verifiers/verify_harness_claims.py` | 0=clean, 1=failed, 2=could-not-evaluate, 3=could-not-evaluate | `--self-test` | `verifiers/baseline.json` | none | kotoba |
| `verifiers/verify_harness_independent.py` | gate | `python3 -B verifiers/verify_harness_independent.py --freeze <file>` (bare `--json` only derives) | 0=clean, 1=failed, 2=could-not-evaluate, 3=could-not-evaluate | `--self-test` | in-file | `--out`/`--write-freeze` paths; temp dirs | kotoba |
| `verifiers/verify_skill_checklist.py` | gate | `python3 -B verifiers/verify_skill_checklist.py` | 0=clean, 1=failed, 2=could-not-evaluate, 3=failed | `--self-test` | `verifiers/checklist-baseline.json`, `verifiers/checklist-command-vocabulary.json` | self-test trees under `$TMPDIR` | kotoba |
| `verifiers/verify_surfaces.py` | gate | `python3 -B verifiers/verify_surfaces.py` | 0=clean, 1=failed, 2=could-not-evaluate, 3=could-not-evaluate | `--self-test` | `verifiers/surfaces-baseline.json` | self-test temp files | kotoba |

## Sources

- `corpus/SOURCES.md` — where this lane learns: opened, scope-tiered source rows,
  study paths and search log; admission bar in `corpus/QUALITY.md`.
- Production skill files and what each demonstrates (wwkd, godspeed, sekhmet-l3,
  xbrd-ask, the bailian family, omarchy, ufo) moved verbatim to
  `corpus/knowledge/anatomy-and-compression.md` § Moved from SKILL.md § Sources —
  production skill files (round 59).
- `/home/vgpnk/Projects/shokunin/*/AGENTS.md` (17 files on 2026-10-22; 9 share
  the 5-line template body) + `~/.agents/AGENTS.md` (14 lines / 949 B) —
  always-on constraint files; no frontmatter, terse imperatives.
- `/home/vgpnk/Projects/shokunin/.ufo/prompts/*-L1.md` (8 files, 9–12 lines) —
  spawn dispatch-prompt stanza order and `| godspeed` terminator.
- `/home/vgpnk/Projects/shokunin/.ufo/prompts/*-round-*.md` (50 files, 3–11
  lines at round-9 recount; round-7 audit: 30 restate the L2 map with stale
  aliases) — round
  self-iteration mode; template variance is name+path only.
- Host surfaces studied (opencode agent and command files, CLAUDE.md files) moved verbatim to
  `corpus/knowledge/anatomy-and-compression.md` § Moved from SKILL.md § Sources — host surfaces (round 60).
- `~/.local/share/opencode/opencode.db` — literal-trigger miss proxy over 398
  sessions / 415 skill calls (415/216 re-verified round 9): unique-token
  triggers 0 misses; godspeed always-on session coverage 51.5%, re-interpreted
  round 8 as a consume-side gap (offer 387/387 = 100%, activation 205/399 =
  51.4%); domain-term names ambiguous (`ufo` misses are references, not
  invocations).
- `~/.local/share/opencode/log/opencode.log` — opencode offer trace
  (`message=init count=N` per instance, latest 18; `duplicate skill name`
  warns) and the `<available_skills>`-vs-`<skills>` tag split (round-8/9).
- opencode — npm `opencode-ai` 1.19.3 since round 47 (the `~/.local/bin/opencode`
  npx wrapper; pinned ELF and lineage in `verifiers/baseline.json` and
  `corpus/knowledge/instruction-surface-census-round13.md` § B′; the round-8/18
  `~/.opencode/bin` install is gone) + upstream `github.com/sst/opencode` (dev):
  `packages/opencode/src/skill/index.ts:321-343` (`fmt` verbose render,
  `description` filter), `:105-139` (add/duplicate: warn then **unguarded**
  assignment, last parsed wins), `:235-246` (`concurrency:"unbounded"` parse
  order), `session/system.ts:107-119` (`SystemPrompt.skills`, `skill`
  permission gate), `tui/src/component/dialog-skill.tsx:41` (TUI list =
  whitespace-collapse only).
- `~/.omp/agent/sessions/**/*.jsonl` (5842 files; `session_init` records
  ~4032–4120 across round-9 lanes — the counter moves inside a round, re-run
  before citing; 14 distinct catalogues at round 7) + `~/.omp/logs/
  http-400-requests/*.json` (32 catalogue-bearing captures at round-9 recount;
  23 at round 7) — render census:
  godspeed offered 3911/3911 at round 7 (4056+ records now); 2026-09-27 regime
  break 8.2K→1.75K block bytes.
- `~/.local/bin/omp` embedded JS (`strings -n 6`; cite anchors, not offsets —
  ELF offsets and `strings` line numbers shift across builds):
  `previewSkillDescription` (truncator: `t.replace(/\s+/g," ").trim()`,
  `if (t.length <= _8n) return t`, `t.slice(0, _8n-1)`, first-sentence
  `^.*?[.!?](?=\s|$)` kept if ≥40 chars, else last-space + `…`; `_8n = 100`),
  `createSkillDescriptionCompressor` (LLM path + validator ≤160 chars, ≤12
  words), key `A8n` = `sha256(K7s ‖ \x00 ‖ name ‖ \x00 ‖ description)` with the
  compressor template = the 273-byte bunfs prompt `compress-description-*.md`
  (the routing-hint line **plus** `Skill: {{name}}` / `Description:
  {{description}}`, placeholders included in the hash; sha256
  `c1f03c8e248eb40e…`, recovered by anchoring, not by offset) — the description
  is hashed as the YAML loader yields it (`>`/`|` keep a trailing newline,
  `>-`/plain strip it), so a ws-strip-only check under-reports coverage; cache
  `~/.omp/agent/skill-descriptions.db` (17 rows at round 9, up from 5; all 17
  keys reproduce, newest catalogue 17/17 cache, 0 truncations — round 10
  re-verified by `verifiers/verify_harness_claims.py`, 27/27 checks).
- `corpus/knowledge/harness-router-models-round9.md` — the two-harness router
  model (tag, render, offer gate, failure mode, verify recipe) with the
  round-9 key-reproduction and freeze evidence.
- `verifiers/README.md` — what each lane verifier checks (the round-10 to round-23
  verifier bullets, moved there verbatim in round 54); registry rows: § Gate registry.
- `corpus/knowledge/harness-verifier-round10.md` — what the verifier checks and
  the facts behind each check (key prefix bytes + sha256, style-aware salt,
  offer-gate roots, opencode counter checks) plus its open gaps.
- `corpus/knowledge/claim-scope-audit-round9.md` — the round-9 consistency
  measurement: harness-claim scope before (31 claim units, 9 UNSCOPED) and after.
- `corpus/knowledge/render-mechanism-round7.md` — mechanism + survival
  measurement: cliff = offset 99, keep 55–96; the char-survival figure (17.7% of
  description chars reaching the router) is logged in `LOG.md` round 7 and
  `../.ufo/reports/round-7/kotoba.md`, not in the artifact. Loss figures
  (53/62 quoted spans, 13/13 `Triggers:` clauses) describe the cache-miss
  truncation path only.
- `corpus/knowledge/dispatch-prompt-audit-round7.md` — 12-item dispatch
  checklist (artifact numbering; § Dispatch-prompt fidelity checklist below
  renders the same set as 9 merged boxes) + 43-file application (37 fail ≥1
  item) + resolvability sweep
  (dead `~/wikillm` path, dead `~/.xbgst` env file, generator contract bugs).
- `corpus/knowledge/alwayson-checklist-round7.md` — 8-item AGENTS.md
  checklist + application (host file FAIL), self-audit results (4 fails
  cured), sentinel re-verify (all cross-domain defects persist).
