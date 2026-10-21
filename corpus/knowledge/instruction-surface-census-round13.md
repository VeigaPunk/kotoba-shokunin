# Instruction-surface census — round 13

**Claim (the round's axis move, coverage 7 → 8.5).** The instruction-surface
inventory is **derived from loader code**, not from host observation: every class
the two target harnesses can read is named with its literal, its load condition,
and either the craft row that governs it or a reason for excluding it. The
derivation is machine-checked (`verifiers/verify_surfaces.py`) and independently
re-measured by a non-author lane.

**Round-18 errata (2026-10-14, substrate rebuild, append-only).** Both binaries
changed since this census: omp `55016ef531…` → `ff59fc1b48…` (2026-10-14) and
opencode `f9dab32248…` → `d9123b9bcd…` (v2.0.26). § A stays live — the same
`.md` registration shapes persist under renamed callees (`Id|Cl|jD[ef]` →
`Tl|dr|GW`, allowlist re-pinned in the verifier) — but **§ B's opencode model
was superseded and is rewritten below**: the name-priority array, the
`.claude` home candidate, the remote-instructions fetcher, the
`fn("Instruction.resolve")` read-hook and the `instruction-context` subsystem
are all gone from the new binary; the five old class ids in § B's table are
historical (falsified-pointer preservation — they describe the 2026-09-28
binary, not the current one). The round-13/14 quotes of § B prose remain as
historical records; the table and the prose above it now describe the live
binary. Binaries at re-derivation: omp `ff59fc1b484c1308a7247ad208305005627b3fac62b440737c2b1835ac32074e`,
opencode `d9123b9bcdb0a31f7ab9fe9812b58a9dc1768ad6d97e7b276dff1181813218c9`.

**Round-14 amendment (2026-09-28, coverage 8.0 → 8.5).** Two pieces of this
census changed status and are edited in place below rather than left stale:
`surfaces.no_uncovered_class` remains omp-only by construction, and opencode is
covered by its own machine check, `surfaces.opencode_extract` (six code-shape
rules, two-way parity, zero-extraction FAILs); the census row columns **id,
literal and kind** are now compared per id against the baseline
(`surfaces.literal_parity`, `surfaces.kind_parity`), closing the round-13
mutation escape in the literal column and finding a third column in the same
class. Evidence file: `opencode-extraction-round14.md`; the two ceilings that
remain are stated in § Honest ceiling.

**Scope of the machine-checked half (stated first, because it is narrower than the
claim sounds).** `surfaces.no_uncovered_class` proves *set parity over a documented
extraction set* — the `.md`-suffixed `(Id|Cl|jD[ef])(<v>, "<group>", "<file>.md")`
registration shapes in the omp dump — never existential completeness. The
description-anchored registry list below is wider and hand-audited; extraction
limits are enumerated in § Honest ceiling.

## Method

| # | Extraction | Command | What it proves |
|---|-----------|---------|----------------|
| 1 | Call-shape scan (L1, raw bytes — no `strings`, no offsets) | `python3 -c` over `open('/home/vgpnk/.local/bin/omp','rb').read()` with `re.compile(rb'(Id\|Cl\|jDe\|jDf\|n4\|o4\|CTt)\(\s*[A-Za-z_$][A-Za-z0-9_$]*\s*,\s*"([A-Za-z0-9_./-]+)"\s*,\s*"([A-Za-z0-9_./-]+)"')` | the registration pairs, with their group names |
| 2 | Registry-description scan (L1) | filter ASCII runs of 12–140 bytes beginning `Load` / `Standalone` / `Custom` / `Load system` over the same bytes | the registry's **own class descriptions** — the wider inventory |
| 3 | Second witness (L2 lane `scout-independent` / seat `ProposedReptile`, **blind**: never read this file, the plan, the other scouts' scratch, or the verifier) | own printable-run extractor over raw bytes (`re.finditer(rb"[\x20-\x7e]{8,}")` → offset/len/text TSV, 833,846 omp runs / 344,469 opencode runs), each candidate adjudicated by reading the enclosing code window — `strings` never invoked | independent re-derivation; record: `corpus/knowledge/instruction-surface-remeasure-round13.md` |
| 4 | Host existence (L2 lane `ExecHostCensus`) | `find`/`ls`/`python3 json.load` over `~` (node_modules/.git/pkg-caches excluded) | which classes have live instances here |
| 5 | Injection probe (L2 lane `LabratInject`) | scratch project + marker strings + live session capture | read-by-loader vs actually-reaches-the-prompt |

Binaries (2026-09-28): omp `sha256 55016ef5317af556…`, opencode `sha256
f9dab32248695e9e…`, identical to the binary hashes `verifiers/baseline.json`
**records** in `measured_against` (recorded, not check-enforced: the enforced pin
there is the 273-byte compression-template sha256, which is what invalidates every
cache key when it moves).

**Anchors are literals, never offsets.** The round-move brief carried `strings`
line numbers from two different invocations (`-n 4` and `-n 6`); the reviewer
lane re-ran them and found every one stale, correctly. Nothing here cites an
offset.

## Class inventory

Every id below is a backticked `` `harness:group/literal` `` token; the parity
check compares this set to `verifiers/surfaces-baseline.json` both ways.

### A. omp — machine-extracted rule-text registrations

| class_id | literal | kind | governed by | evidence |
|---|---|---|---|---|
| `omp:agents-md/AGENTS.md` | AGENTS.md | loader-group | § Instruction surfaces → AGENTS.md | `jDe(e,Pqr,"AGENTS.md")`, `Pqr = "agents-md"`; registry: "Standalone AGENTS.md files (Codex/Gemini style)" |
| `omp:claude-md/CLAUDE.md` | CLAUDE.md | loader-group | § Instruction surfaces → CLAUDE.md | `jDe(e,BWr,"CLAUDE.md")`, `BWr = "claude-md"`; registry: "Standalone CLAUDE.md files (Claude Code style)" |
| `omp:opencode/AGENTS.md` | AGENTS.md | loader-group | § Instruction surfaces → AGENTS.md | `Id(e,"opencode","AGENTS.md")`; registry: "Load AGENTS.md from `~/.config/opencode/`" |
| `omp:gemini/GEMINI.md` | GEMINI.md | loader-group | § Instruction surfaces → Cross-tool rule files | `Id(e,"gemini","GEMINI.md")` / `Cl(e,"gemini","GEMINI.md")`; registry: "Load GEMINI.md context files" |
| `omp:gemini/system.md` | system.md | loader-group | § Instruction surfaces → Cross-tool rule files | `Id(e,"gemini","system.md")`; registry: "Load system.md custom system prompt files" |
| `omp:gemini/SYSTEM_TEMPLATE.md` | SYSTEM_TEMPLATE.md | loader-group | § Instruction surfaces → Cross-tool rule files | `Cl(e,"gemini","SYSTEM_TEMPLATE.md")`; registry: "Custom system prompt files (SYSTEM.md, SYSTEM_TEMPLATE.md) that modify agent behavior" |
| `omp:github/copilot-instructions.md` | copilot-instructions.md | loader-group | § Instruction surfaces → Cross-tool rule files | `Cl(e,"github","copilot-instructions.md")`; registry: "Load copilot-instructions.md from `.github/` and `~/.copilot/`; AGENTS.md from `COPILOT_CUSTOM_INSTRUCTIONS_DIRS`" |
| `omp:windsurf/memories/global_rules.md` | memories/global_rules.md | loader-group | § Instruction surfaces → Cross-tool rule files | `Id(e,"windsurf","memories/global_rules.md")`; registry: "Load rules from Windsurf (`.windsurf/rules/*.md`, `memories/global_rules.md`, `.windsurfrules`)" |

The registry names rule-text classes as **directories/patterns** whose literals
are not `*.md` call shapes. They are hand-declared (extraction set B) and still
probed by `surfaces.literal_present`:

| class_id | literal | kind | governed by | evidence (registry description, verbatim) |
|---|---|---|---|---|
| `omp:cursor/rules` | rules | loader-literal | Cross-tool rule files | code reads `<cwd>/.cursor/rules/*.{mdc,md}` + `~/.cursor/rules` (second witness §3); the registry description says "Load rules from `.cursor/rules/*.mdc` and legacy `.cursorrules`" but **no code path reads `.cursorrules`** — description overstates the class |
| `omp:windsurf/rules` | rules | loader-literal | Cross-tool rule files | code reads `<cwd>/.windsurf/rules/*.md` + `~/.codeium/windsurf/memories/global_rules.md`; the description adds `.windsurfrules`, which **no code path reads** — same description-vs-code gap |
| `omp:github/instructions` | instructions | loader-literal | Cross-tool rule files | "Load `*.instructions.md` from `.github/instructions/` and `COPILOT_CUSTOM_INSTRUCTIONS_DIRS`" (×2, one Copilot-scoped) |
| `omp:clinerules/.clinerules` | .clinerules | loader-literal | Cross-tool rule files | "Load rules from `.clinerules` (single file or directory)" |
| `omp:omp-dir/RULES.md` | RULES.md | loader-literal | Cross-tool rule files | single-file rules class: `~/.omp/agent/RULES.md` + nearest `<ancestor>/.omp/RULES.md` (second witness §3; literal 6 hits in the omp bytes) |
| `omp:provider-gate/enabledProviders` | enabledProviders | loader-config | Cross-tool rule files (craft caveat) | opt-in set `RTo` = {cursor, codex, claude, claude-plugins, gemini, opencode, windsurf, github}; `eu()` admits a provider's **user** paths only when enabled (`enabledProviders`, `*`/`all`, or `CLAUDE_CONFIG_DIR` for claude) and `disabledProviders` removes it entirely; **project-level paths are never gated** — so a repo carrying `GEMINI.md`/`.cursor/rules` may still be read by nobody |
| `omp:agents/rules` | rules | loader-literal | Cross-tool rule files | "Load rules from `.agent/rules` and `.agents/rules` (project walk-up + user home)" |
| `omp:agents-md-walkup/AGENTS.md` | AGENTS.md | loader-literal | AGENTS.md row | "Load AGENTS.md from `.agent` and `.agents` (project walk-up + user home)" |
| `omp:omp-dir/AGENTS.md` | AGENTS.md | loader-literal | AGENTS.md row | "Load AGENTS.md from `.omp/` directories" |
| `omp:claude-dir/CLAUDE.md` | CLAUDE.md | loader-literal | CLAUDE.md row | "Load CLAUDE.md files from `.claude/` directories" |
| `omp:codex/AGENTS.md` | AGENTS.md | loader-literal | AGENTS.md row | "Load context files from `~/.codex/AGENTS.md` (user-level only)" |
| `omp:agent-system-prompt/SYSTEM.md` | SYSTEM.md | loader-literal | Cross-tool rule files | one id for the whole **SYSTEM family**, which omp registers per provider (registry, verbatim): "Load SYSTEM.md and SYSTEM_TEMPLATE.md from `.agent` and `.agents` (project walk-up + user home)"; "Load SYSTEM.md and SYSTEM_TEMPLATE.md from `.codex` (project cwd + user home)"; "Load system prompt from `.claude/SYSTEM.md`"; "Load system.md custom system prompt files" + "Custom system prompt files (SYSTEM.md, SYSTEM_TEMPLATE.md)" (gemini); plus `SYSTEM.md`/`SYSTEM_TEMPLATE.md` under `~/.omp/agent` + nearest `<ancestor>/.omp` (second witness §3). Declared at family granularity deliberately — the craft rule is the same for every variant, and the critic lane's "`.codex/SYSTEM.md` undeclared" finding is this row |
| `omp:marketplace/plugin-rules` | plugins | loader-literal | Cross-tool rule files | "Load rules from marketplace plugin rules directories" |
| `omp:agents/prompts` | prompts | loader-literal | Cross-tool rule files | "Load prompts from `.agent/prompts` and `.agents/prompts` (project walk-up + user home)" |
| `omp:github/prompts` | prompts | loader-literal | Cross-tool rule files | "Load `*.prompt.md` from `.github/prompts/` (VS Code Copilot prompt files)" |
| `omp:codex/prompts` | prompts | loader-literal | Cross-tool rule files | "Load prompts from `~/.codex/prompts` and `.codex/prompts/`" |
| `omp:agents/skills` | skills | loader-literal | § Instruction surfaces → SKILL.md | "Load skills from `.agent/skills` and `.agents/skills` (project walk-up + user home)" |

### A2. omp — provider priority decides which file wins (single-lane derivation)

Attributed to the omp scout lane (`DisciplinaryAlpaca`, round 13), **not**
independently confirmed by the second witness (which did not read the merge):
omp's registry is a capability table — `Ut(<id>, {id, displayName, description,
priority, load})` — sorted by descending priority, and `xr()` merges with
**first-wins dedupe by `key()`**. For the `context-files` capability the key is
`user` | `project:<depth>`, so **exactly one file wins per directory depth**, by
provider priority: `.omp/AGENTS.md` at depth 0 beats a root `AGENTS.md`. Reported
priorities: native 100, skillshare 95, omp-plugins 90, claude 80, agents /
agent-plugins 70–75, codex and claude-plugins 70, gemini 60, opencode 55, cursor
50, windsurf 50, cline 40, github 30, agents-md / claude-md / mcp-json / ssh /
omp-managed 1–10. Project-level foreign directories (`.gemini`, `.codex`,
`.opencode`, `.cursor`, `.windsurf`, `.github`, `.vscode`) load unconditionally;
user-level paths pass the `eu()`/`RTo` gate. Same lane: omp supports `@`-imports
(inlining arbitrary files, reported depth 5), does **not** consume an
`instructions` key from `opencode.json` (only `mcp`), and — as the critic lane
also found — the `.cursorrules` / `.windsurfrules` literals live only in
description strings.

Craft consequence if it holds: "one owner per repo" is enforced *for you* by
priority, not by the filename — you do not get to choose which of `.omp/AGENTS.md`
and `AGENTS.md` is read at the same depth; the higher-priority provider wins.
A future round should confirm the merge on the second witness's extractor before
this becomes a checklist item.

### A3. Wire-level probe (partial — the lane hit its model rate limit mid-run)

Lane `LabratInject` drove `omp -p` against a local HTTP capture server in an
isolated `PI_CONFIG_DIR` home and grepped the **request bodies** for marker
strings. It failed part-way (provider rate limit), so this section records only
what it established with a reproducer, not a finished probe:

- **Established:** the capability that reads context files dedupes by
  `level:depth` (`yf`), so **one project context file per depth bucket reaches the
  prompt**; with a bare `AGENTS.md` alone it is injected, and with `AGENTS.md`
  *and* `CLAUDE.md` at depth 0 only one survives — the same practical outcome as
  opencode's first-name-wins, reached by a different mechanism (bucket collision
  rather than an ordered name list). `.github/copilot-instructions.md` and an
  `alwaysApply` `.instructions.md`/`.mdc` rule landed in the prompt (the latter in
  a `<generic-rules>` section); `Cl(e,"gemini","GEMINI.md")` resolved to
  `cwd/.gemini/GEMINI.md` only, with no walk-up.
- **Established negative (a false friend killed twice):** the
  `for (const s of ["AGENTS.md","CLAUDE.md"])` loop is **memory consolidation**,
  not context loading — matching the host census's "false friend" reading and the
  census's exclusion of that loop from the class inventory.
- **Not established (carried):** the full provider-priority table (§ A2) is still
  single-lane; whether the depth-bucket collision is deterministic across reruns
  was mid-investigation when the lane died; opencode was reached but not
  characterised by the same wire method.

Consequence for the census's own ceiling: the floor under "a loader registration
is not proof of injection" is now *measured for one host state and one harness*,
which is a real narrowing — and the round still does not claim injection for any
class the probe did not exercise.

### B. opencode — instruction model (re-derived 2026-10-14 for v2.0.26)

**Round-47 errata (append-only):** this subsection describes the v2.0.26 binary,
which is no longer on the host. Its four table rows and its `config/instructions`
§ C row moved, byte-identical, to `## Superseded class rows and the round-47
opencode ledger (not inventory)` below; the live opencode classes are in § B′.

**Historical note (append-only errata):** the round-13/14 § B described the
2026-09-28 binary — a name-priority walk-up `["AGENTS.md","CLAUDE.md","CONTEXT.md"]`,
a `~/.claude/CLAUDE.md` home candidate, a declared `instructions` list with
remote `https://` fetches, a `fn("Instruction.resolve")` read-hook emitting
`<system-reminder>` tool-result blocks, and a second `instruction-context`
subsystem. None of those anchors exists in v2.0.26 (`CONTEXT.md`: 0
occurrences; `disableClaudeCodePrompt`: 0; `Instruction.resolve`: 0;
`InstructionContext.observe`: 0; `system-context-builtins`: 0). The ids it
declared — `opencode:instructions/{AGENTS,CLAUDE,CONTEXT}.md`,
`opencode:claude-home/CLAUDE.md`, `opencode:config/instructions-remote`,
`opencode:read-hook/instructions`, `opencode:instruction-context/AGENTS.md` —
are superseded-revision claims preserved as historical, not live classes.

**The v2.0.26 model (byte-verified against sha256 `d9123b9b…`):** one
`InstructionDiscovery` state (`core/instructions`) fed by three file sources
and one API channel:

1. **Project source** — `opencode.config.instruction` walks up **all-match**
   for `AGENTS.md` only: `ConfigInstructionPlugin.projectSource` calls
   `i.up({targets:["AGENTS.md"],start:<cwd>,stop:<project>,type:"file"})`.
   Disabled by config `project:false` (`OPENCODE_CONFIG_PROJECT_DISABLE` /
   `OPENCODE_DISABLE_PROJECT_CONFIG`, wired `V7({project:i.config?.project})`).
2. **Global source** — `<opencode config dir>/AGENTS.md` via
   `j5(r.config,"AGENTS.md")` (the `.claude` home candidate no longer exists).
   The plugin subscribes every candidate file and republishes on change
   (`instructions rescanned`).
3. **Read-hook** — `ReadTool.Plugin` walks up from every read path for
   `AGENTS.md` (`targets:[a$]`, `a$` = `"AGENTS.md"`), keeps only hits *outside*
   the project root, and calls `SessionInstructions.load`, which publishes
   `Instructions from: <path>` synthetic entries.
4. **API-managed entries** — `session.instructions.entry.{list,put,remove}` at
   `/api/experimental/session/:sessionID/instructions/entries`, durable and
   announced at the next step boundary.

Render/diff: `Instructions from:` initial, `New instructions apply from:` /
`The instructions changed:` / `…no longer apply.` on watch events.
`config.instructions` ("Additional paths or URLs supplying ambient
instructions") remains **schema-declared only** — no consumer found in this
binary; recorded as an excluded class, not a governed one.

| class_id | literal | kind | governed by | evidence |
|---|---|---|---|---|

### B′. opencode — instruction model (re-derived 2026-10-21 for 1.19.3, round 47)

**Substrate:** npm `opencode-ai` 1.19.3 — `/home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe`,
sha256 `179ca421d61eefeadfa0c50e084a6e79c1623734732f0f4593f81ccfd3ab7ee9`, the bytes the
`~/.local/bin/opencode` npx wrapper executes. Frozen copy and `strings -n 4` dump:
`/fast/scratch/kotoba-r47/shared/` (`SHA256SUMS`). This is a different distribution
channel from v2.0.26 (`~/.opencode/bin`, removed 2026-10-20), not its successor: the
dump self-reports `var n="1.19.3"` and contains no `2.0.26`.

**Lineage finding.** Every v2.0.26 anchor is absent from the 1.19.3 dump
(`ConfigInstructionPlugin` 0, `ReadTool.Plugin` 0, `SessionInstructions` 0,
`session.instructions.entry.put` 0, `j5(r.config,"AGENTS.md")` 0, `InstructionDiscovery` 0),
and every round-14 anchor is present (counts: the round-47 ledger after § D). The loader model is the round-13/14
one recorded as historical in § B's first note: the `@opencode/Instruction` service
(name-priority first-match walk-up, config + `.claude` home candidates, declared
`instructions` list with a remote `https://` half, the `Instruction.resolve` read hook)
plus the `instruction-context` subsystem. Rules OC-1..OC-6 in
`verifiers/verify_surfaces.py` were re-measured anchor by anchor on the dump; two were
tightened (OC-3b now requires the `.filter(` call — the round-14 pattern also matched
OC-3a's loop; OC-4 adds the `ReadTool.execute` caller — `<system-reminder>` alone has
18 hits). Whether either subsystem fires at runtime is not decided by strings (§ Honest
ceiling).

**Identity changes the re-derivation surfaced (not carried silently):**
- the read hook walks *inside* the instance directory
  (`while(G.startsWith(N)&&G!==N)`), so v2.0.26's "keeps only hits outside the
  project" reading does not transfer — the round-14 id `read-hook/instructions` is the
  live one, `read-hook/AGENTS.md` is retired;
- `config/instructions` has a proven consumer on this binary, so round 18's exclusion
  reason ("no loader consumer proven") is false here — re-verdicted `governed`;
- `/instructions/entries` survives only in the generated client SDK
  (`instructions:{entry:{list:` …`/api/session/${…}/instructions/entries`); no server
  route or `session.instructions.entry.put` id exists — `api-entries/instructions` is
  retired, not re-anchored onto a client stub.

| class_id | literal | kind | governed by | evidence |
|---|---|---|---|---|
| `opencode:instructions/AGENTS.md` | AGENTS.md | loader-literal | AGENTS.md row | `y=["AGENTS.md",` first priority-list element; first-match per directory via `globUp(T,d.directory,d.worktree)` (OC-1, OC-5; dump 443993) |
| `opencode:instructions/CLAUDE.md` | CLAUDE.md | loader-literal | CLAUDE.md row | second element, gated: `...!t.disableClaudeCodePrompt?["CLAUDE.md"]:[]` (OC-1; dump 443993) |
| `opencode:instructions/CONTEXT.md` | CONTEXT.md | loader-literal | Cross-tool rule files | last element `"CONTEXT.md"]` (OC-1; 1 occurrence of `CONTEXT.md` in the 1.19.3 dump) |
| `opencode:config/AGENTS.md` | AGENTS.md | loader-config | AGENTS.md row | `n=[X.join(r.config,"AGENTS.md")` in `Instruction.systemPaths` (OC-2; dump 443993) |
| `opencode:claude-home/CLAUDE.md` | CLAUDE.md | loader-config | CLAUDE.md row | `X.join(r.home,".claude","CLAUDE.md")`, gated by `disableClaudeCodePrompt` (OC-2; dump 443993) |
| `opencode:config/instructions` | instructions | loader-config | § Instruction surfaces → Declared instruction list | consumer proven: `for(let O of T.instructions)` inside `Instruction.systemPaths` globs each local entry (OC-3a; dump 443993) — re-verdicted from round 18's `excluded` |
| `opencode:config/instructions-remote` | https:// | loader-config | Declared instruction list | `(T.instructions??[]).filter((q)=>q.startsWith("https://")||q.startsWith("http://"))` fetched with `{concurrency:4}` and rendered `Instructions from: ` (OC-3b; dump 443993) |
| `opencode:read-hook/instructions` | <system-reminder> | loader-literal | Cross-tool rule files | `fn("Instruction.resolve")` (dump 443995) called from `fn("ReadTool.execute")` (dump 444228) walks up *inside* the instance directory and attaches the nearest instruction file to the read's tool result in a `<system-reminder>` (OC-4) |
| `opencode:instruction-context/AGENTS.md` | AGENTS.md | loader-literal | AGENTS.md row | second subsystem: `InstructionContext.observe` + `targets:["AGENTS.md"]` all-match walk + ungated `jX(L.config,"AGENTS.md")`, key `Key.make("core/instructions")`, registered as `system-context-builtins` (OC-6; dump 445481-445487) |

### C. Excluded loader-derived classes (each with its reason)

| class_id | literal | kind | reason it is not a craft-governed rule-text class |
|---|---|---|---|
| `omp:discovery/mcp-configs` | mcp.json | loader-config | Config discovery (`mcp.json`, `.mcp.json`, `~/.cursor/mcp.json`, `.vscode/mcp.json`, `mcp_config.json`, `.claude.json`, `[mcp_servers.*]`) — supplies servers, not rule text; no prompt-craft rule |
| `omp:discovery/settings` | settings.json | loader-config | Settings discovery (cursor/gemini/claude/codex/opencode) — behavior flags, not durable constraints |
| `omp:discovery/extensions` | extensions | loader-literal | Extension/hook/tool module roots (`.gemini/extensions`, `.codex/tools`, `.claude/hooks`) — executable surfaces, out of prompt-craft province |
| `omp:discovery/plugins` | plugins | loader-literal | Plugin module roots (`~/.config/opencode/plugins`, marketplace cache) — code, not text |
| `omp:discovery/commands` | commands | loader-literal | Command-file roots: the *Command file* row governs the craft; the literal root list is discovery detail |
| `omp:discovery/skills-roots` | skills | loader-literal | Skill roots beyond `.agent(s)/skills` (`.github/skills`, `~/.codex/skills`, `~/.claude/skills`, `~/.omp/agent/managed-skills`): covered by the SKILL.md row's craft, which is name/render-scoped, not root-scoped |
| `omp:unknown/managed-skills` | managed-skills | loader-literal | `~/.omp/agent/managed-skills` — omp-managed skill store; [INFERENCE] merge precedence with the user root is untraced, so it is excluded with this reason rather than claimed |
| `omp:unknown/subagent-roster` | agents | loader-config | `omp agents unpack` → `~/.omp/agent/agents` (37 files live) — the **omp-side analogue of the opencode agent-definition row**, but the load path is inferred from the unpack target, not read from a session; excluded pending that trace |

### D. Non-loader mentions (no class id — these are not classes at all)

| literal / path | kind | why it is here and not in the inventory |
|---|---|---|
| `.cursor/rules/`, `.cursorrules`, `.github/copilot-instructions.md` (opencode) | prompt-text | occur **only** inside opencode's `/init` command prompt template — instructions *to* a model, byte-identical at two sites |
| `CLAUDE.md` (opencode agent-creation/review prompts) | prompt-text | advisory wording in prompt text; the loader is the one in § B |
| `.cursor/rules` (bun `init` template list) | template-list | scaffolding enumerations; the round-move brief's "false friend" — narrowed to this literal, since omp's `.cursor/rules` **is** a live class |
| `.ufo/prompts/*.md` (197 files) | doc | no harness loads this directory; a fleet filesystem convention. The two dispatch rows in § Instruction surfaces are labeled host-observed for this reason |
| `~/.local/templates/dispatch/*.md` (7 files) | doc | harness-named dispatch templates copied by hand — no loader |
| `~/.grok/{AGENTS.md,rules,agents}` | doc | a **third** harness, outside this lane's two-harness scope; reported, not absorbed |
| `~/.agents/AGENTS.md` + `~/.agents/godspeed-core/*.md` | doc | reachable through the AGENTS.md *class*; listed here because the host file, not a harness, is what pulls the godspeed-core files in |
| opencode non-file prompt surfaces: MCP server instructions (`<mcp_instructions>`), references (`<available_references>`), the plugin `experimental.chat.system.transform` hook, config `{file:…}`/`{env:…}` substitution, the API `system` field | doc | they reach the prompt but are **not file classes**, so they cannot be governed by a filename-convention craft row; recorded so the inventory's boundary is explicit (three lanes agree on this list: census, second witness §5, opencode scout) |
| omp memory store (the `Vcl`-family reader) | doc | reads the harness's own memory files into prompt context — a state store, not a rule-file convention; boundary flagged by both the second witness (§5, "flagged as uncertain") and the critic lane (memory reader uncovered) |
| omp extra non-registry prompt surfaces (omp scout lane, round 13): `PERSONALITY.md`, `TITLE_SYSTEM.md`, `APPEND_SYSTEM.md` (via `.omp`/`.claude`/`.codex`/`.gemini` dirs), `WATCHDOG.md` + `WATCHDOG.yml` `instructions:` keys, bundled rules/agents embedded in the binary, sharpshooter/hindsight memory files | doc | prompt-reaching but either single-harness extras outside the file-convention classes this craft skill governs, or embedded content with no file to write; listed so the boundary is explicit and attributable to one lane |

## Superseded class rows and the round-47 opencode ledger (not inventory)

Moved here in round 47, bytes unchanged, from § B (four rows) and § C (one row):
the v2.0.26 opencode classes. They sit outside `## Class inventory`, so
`verify_surfaces.py` does not count them; the ledger after them records every
opencode id's round-47 verdict.

| class_id | literal | kind | governed by | evidence |
|---|---|---|---|---|
| `opencode:project/AGENTS.md` | AGENTS.md | loader-literal | AGENTS.md row | `ConfigInstructionPlugin.projectSource` + `targets:["AGENTS.md"]` all-match walk (OC-1) |
| `opencode:config/AGENTS.md` | AGENTS.md | loader-config | AGENTS.md row | `j5(r.config,"AGENTS.md")` global candidate (OC-2) |
| `opencode:read-hook/AGENTS.md` | AGENTS.md | loader-literal | Cross-tool rule files | `ReadTool.Plugin` + `targets:[a$]` + `SessionInstructions.load` → `Instructions from:` (OC-4) |
| `opencode:api-entries/instructions` | instructions | loader-config | § Instruction surfaces → Declared instruction list | `/instructions/entries` + `session.instructions.entry.put` (OC-6) |

| class_id | literal | kind | reason it is not a craft-governed rule-text class |
|---|---|---|---|
| `opencode:config/instructions` | instructions | loader-config | Schema-declared "ambient instructions" list in v2.0.26; **no loader consumer proven** in the binary — only the read-hook publishes file contents (round-18 re-derivation, OC-3 witness only) |

**Class ledger (round 47; every id the census ever declared for opencode).** Count
command: `python3 -c 'import sys;d=open(sys.argv[1],errors="replace").read();print(d.count(sys.argv[2]))' /fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings '<anchor>'`.

| id | round-46 state | round-47 verdict | anchor (count on the 1.19.3 dump) |
|---|---|---|---|
| `opencode:project/AGENTS.md` | governed (OC-1, v2.0.26) | retired | `ConfigInstructionPlugin.projectSource` 0 |
| `opencode:config/AGENTS.md` | governed (OC-2) | retained, re-anchored | `X.join(r.config,"AGENTS.md")` 1 (round-18 anchor `j5(r.config,…)` 0) |
| `opencode:read-hook/AGENTS.md` | governed (OC-4, v2.0.26) | retired | `ReadTool.Plugin` 0, `SessionInstructions.load` 0 |
| `opencode:api-entries/instructions` | governed (OC-6, v2.0.26) | retired | `session.instructions.entry.put` 0; client stub `instructions:{entry:{list:` 1 |
| `opencode:config/instructions` | excluded | re-verdicted governed | `for(let O of T.instructions)` 1 |
| `opencode:instructions/AGENTS.md` | historical (round 18) | resurrected | priority array 1 |
| `opencode:instructions/CLAUDE.md` | historical | resurrected | `disableClaudeCodePrompt` 3 |
| `opencode:instructions/CONTEXT.md` | historical | resurrected | `CONTEXT.md` 1 |
| `opencode:claude-home/CLAUDE.md` | historical | resurrected | `X.join(r.home,".claude","CLAUDE.md")` 1 |
| `opencode:config/instructions-remote` | historical | resurrected | `Instructions from: ` 4 |
| `opencode:read-hook/instructions` | historical | resurrected | `fn("Instruction.resolve")` 1, `fn("ReadTool.execute")` 1 |
| `opencode:instruction-context/AGENTS.md` | historical | resurrected | `InstructionContext.observe` 1, `system-context-builtins` 1 |

**Round-47 falsify errata (append-only; evidence `.ufo/waves/round-47/falsify/`).**
Lane-dispatched wave-2 seats re-measured this census at the landing tree and found
these statements wrong or stale; the text above stays as landed, corrected here:
- Substrate identity of § B′: `corpus/SOURCES.md` S015 (frozen-snapshot sha256s).
- § B′ OC-6 row: `instruction-context` is its own layer; it is composed as a
  dependency of the `system-context-builtins` layer, not registered as it
  (`W2InstrContext.md`).
- § B′ read-hook row: `Instruction.resolve` attaches the instruction file found at
  every ancestor level, nearest first, not one "nearest" file; its stop test is an
  unseparated string prefix, so a sibling path sharing the prefix is walked too
  (`W2ReadHook.md`).
- § B′ OC-1 row: the name-priority walk in `Instruction.systemPaths` uses
  `findUp` (all ancestors, first name with hits wins); `globUp` serves the
  declared `instructions` entries and the OC-5 switch (`W2ClaudeGate.md`).
- § B′ lineage sentence: the six named v2.0.26 anchors count 0, but
  `/instructions/entries` survives as a client-SDK stub (ledger row above); "every
  v2.0.26 anchor" overstated it. Upstream, npm `@opencode/cli` 2.x still ships the
  v2.0.26 model (`W2OcLineage.md`): "retired" in the ledger is host-scoped.
- Ledger row `instructions/AGENTS.md`: its count anchor is `y=["AGENTS.md",`
  (count 1); "priority array" is prose (`W2CensusAnchors.md`).
- § B's first historical note calls the round-13/14 ids "not live classes"; on
  1.19.3 the ledger re-instates them. The moved `config/instructions` row's "no
  loader consumer proven" is v2.0.26-scoped.
- § A's evidence cells still quote 18.12.2-era-and-earlier omp call shapes
  (`Id`/`Cl`/`jDe`), absent from 18.12.5, whose shapes are `lq(u,f$,"AGENTS.md")`,
  `Xl(u,"gemini","GEMINI.md")`, `Fo(u,"github","copilot-instructions.md")`. The class
  set is re-proven by the gate on 18.12.5; the human-readable evidence column was
  not re-derived (carried to round 48, `W2SurfacesRerun.md`, `W2KnowledgeStale.md`).
- § Honest ceiling's "six code-shape rules … 5 declared opencode class ids" and
  "self-test 75 assertions" are now 7 rules, 9 ids and 99 assertions.
- Gate strength: every OC rule is a whole-dump presence test (decoys and severed
  call/delivery/gate edges survive; OC-1's gate term is a tautology); the ledger
  and these counts have no machine gate (`W2DropOC1.md`…`W2DropOC6.md`,
  `W2LedgerComplete.md`).

## The disagreement this census had to adjudicate

Two L2 lanes reached opposite verdicts on opencode's `CLAUDE.md`:

- `ExecHostCensus`: "all CLAUDE.md refs in opencode are `/init` prompt text → the
  loader is omp-only", row overstates evidence.
- `ReviewerAnchors` (verify lane): "opencode **does** have a CLAUDE.md loader —
  candidates `[AGENTS.md, CLAUDE.md, CONTEXT.md]` + `[config/AGENTS.md,
  ~/.claude/CLAUDE.md]`, gated by `disableClaudeCodePrompt`".

Byte-level adjudication (L1, method 1–2): **the reviewer is right and the host
census under-read the binary.** The instruction service's priority list
(`y`) and candidate list (`n`) are quoted in § B above. Consequence for the skill:
the row's *claim* ("loader exists in both harness binaries") is substantively
true, but its *evidence* ("9/17 string refs") was exactly the class of proof this
round forbids — a reference count cannot separate a loader from prompt text, and
the lane that used it reached the opposite conclusion from the lane that read the
code. The row now cites the code shapes.

Second correction, same class: the round-move brief's "false friend" note said the
`.cursorrules` hits were the bun template list. Only `.cursor/rules` is. The real
`.cursorrules` occurrences are the cursor registry description ("Load rules from
`.cursor/rules/*.mdc` and legacy `.cursorrules`") — a **live omp class**, so the
"false friend" claim is narrowed to one literal, not the class.

## Reconciliation — what the skill said, what it says now

| Before (round 12) | After (round 13) |
|---|---|
| "Seven surface classes **observed on this host**" — enumeration method host observation | two harness loader models quoted from code, with the *class ids* in this file; the seven craft rows keep their craft rules and gain two rows (cross-tool rule files, declared instruction list) |
| CLAUDE.md row: "loader exists in **both** harness binaries (9/17 string refs)" | omp class `claude-md` + opencode `y[1]`/`n[1]` with the env gate named — counts removed as evidence |
| Dispatch-prompt rows: unqualified | labeled **host-observed; no harness loader** (the class is a `.ufo/prompts/` convention) |
| No loader-derived inventory existed | this file + `verifiers/verify_surfaces.py` (round 13: 4 checks; round 14: 7 checks incl. `surfaces.opencode_extract`, `surfaces.literal_parity`, `surfaces.kind_parity`, exit 0/1/2/3, `--self-test` 75 assertions) + `verifiers/surfaces-baseline.json` |
| Coverage row gap: "no MCP/plugin surface on this host" | refined: *config* absent for the two target harnesses, but `~/.codex/config.toml [mcp_servers.node_repl]` and `~/.config/opencode/plugin/fnm-nudge.js` are live, and both binaries support the surfaces (host absence ≠ support absence) |

## Honest ceiling — what this census cannot decide

- **Injection vs discovery.** `Id/Cl/jDe` prove file discovery; a loader
  registration is not proof that a file reached a prompt this session. The probe
  lane's captures are the only injection evidence here, and they cover one host
  state.
- **Extraction-set completeness, per harness.** The call-shape regex misses
  (a) group names passed as variables other than the two resolved (`Pqr`, `BWr`),
  (b) non-`.md` literals by construction, (c) other binaries' differently-minified
  shapes. **For opencode this file's ceiling was a hole and is now a named
  boundary (round 14):** `surfaces.no_uncovered_class` still extracts zero pairs
  there by construction, and opencode is instead covered by
  `surfaces.opencode_extract` — six code-shape rules (OC-1…OC-6, anchors and
  derive-vs-witness stated per rule) that must reproduce all 5 declared opencode
  class ids, must produce no undeclared id, must each match, and must not produce
  zero classes (a zero extraction FAILs with `vacuity:`). Evidence, drop-one
  matrix and residual ceilings: `opencode-extraction-round14.md`.
  For omp the check is real (8 extracted pairs, parity both ways, an empty baseline
  produces 38 `extra row` findings — recorded in the round's evidence). Parity is
  over the extraction set, never over the world.
- **Craft adequacy.** Whether a repo *should* carry `.cursor/rules` next to
  `AGENTS.md` is a judgment this file does not make; it names the divergence and
  the precedence rule, nothing more.
- **Reason truth.** An exclusion reason is a written judgment; the checker only
  proves one exists.
- **Host existence is depth-capped and was not stable under the round.** Counts came
  from `find` at maxdepth 6–7 excluding vendored caches; and `~/Projects/bounties`
  disappeared mid-survey (listed, then `test -e` → GONE minutes later, per the
  connector lane's §4b) — any host count that named it (e.g. one vendored
  `CLAUDE.md`, `pendle-core-v2-public`) is unobservable now and must never be
  reported as a governed pass. The loader-derived half of this file is unaffected:
  it reads the binaries, not the tree.
- **Row-column parity: three of five columns are machine-checked, two are prose.**
  Mutation lane round 13: of 13 planted mutations, 11 were caught; **two escaped** —
  rewriting a census row's *literal* column to `WRONG.md`, or its *evidence* column
  to `NOT-EVIDENCE`, still exited 0, because `surfaces.table_parity` compares class
  **ids** and `surfaces.literal_present` probes the **baseline's** literal.
  **Round 14 closed the first of those and found a third column in the same
  class:** `surfaces.literal_parity` compares the row's second cell and
  `surfaces.kind_parity` the third cell against the baseline per id (both refuse
  0-vs-0), and a declared id carried outside the row's first cell FAILs because no
  per-id comparison could be anchored to it. Verified: a live census copy with
  `AGENTS.md` → `WRONG.md` exits 1 naming the id and line while `table_parity`
  stays PASS; a copy with `loader-group` → `loader-literal` exits 1 on
  `kind_parity` alone. Standing residual: the `governed by` and `evidence` columns
  have **no machine counterpart** in the baseline (its `reason` field is different
  prose), so a rewrite there is caught by a reader, not by the checker — named here
  rather than smoothed over. The baseline is the checked source; the census text is
  now the checked source for id, literal and kind only.
- **Still unmeasured:** implicit-intent fidelity (unchanged from round 12).

## SKILL.md instruction-surfaces table (absorbed at round 22, bytes verbatim)

Provenance: moved verbatim from `SKILL.md` § Instruction surfaces at round 22 (dispatch HEAD `b16300f`, source lines 76-166; body sha256 `e046a0252cc96f173d148b419b7856e23fe789659cf02bc5b3237e8da26114f5`, the `sed`-canonical hash with trailing newline) under the
≤600-line budget — the round-15 idiom. Byte-preservation gate: `git show b16300f:SKILL.md | sed -n '76,166p' | sha256sum` must reproduce that hash; contiguity: this exact body block is a substring of this file.
The table's "All craft below" cell refers to SKILL.md's craft sections — kept verbatim, noted not smoothed.

> Round-24 erratum (append-only, outside the pinned block): the block below is
> byte-preserved from round 22, so its own stale counts stand uncorrected inside
> it — the block's internal "seven" code-shape rules text (live: 6, OC-1…OC-6; census :337 at round-22 landing, shifted by this note's own insertion — round-25 fix). The editable
> sites (lines 28, 272, 287, 288, 293) were corrected in place at round 24.


Nine surface classes; the loader-derived class inventory behind them (per-harness
literals, load conditions, exclusions with reasons) is
`corpus/knowledge/instruction-surface-census-round13.md`, and its machine check
covers **both** harnesses: `verifiers/verify_surfaces.py` (7 checks) extracts omp's
`.md` registration call shapes and opencode's instruction-service shapes — seven
named rules, all anchors load-bearing, an empty baseline or a zero extraction a
FAIL — and compares the census's id, literal and kind cells per id against
`verifiers/surfaces-baseline.json` (rule set and falsifier matrix:
`corpus/knowledge/opencode-extraction-round14.md`). Each class loads differently, so each
has different craft rules. Applying skill-file rules to an always-loaded file
(or vice versa) is the most common cross-surface mistake. Two of the nine
(dispatch prompts) are **host-observed** — no harness loads `/home/vgpnk/projects/shokunin/.ufo/prompts/`;
they are a fleet filesystem convention and say so in the table.

| Surface | Load condition | Parse surface | Dominant failure | Craft rule |
|---------|----------------|---------------|------------------|------------|
| SKILL.md | Opt-in: activated when `description` matches intent | frontmatter = router index; body = executor contract | False activation / missed activation | All craft below (frontmatter, tables, gates) |
| Agent definition (`opencode/agents/*.md`) | Roster: orchestrator picks by `description`, then body becomes the subagent's system prompt | `description` = delegation index; body = persistent identity | Wrong-lane delegation; stale routing metadata | Terse negative routing in description (`NOT general-purpose. NOT explore.`); identity + constraints in body, never a per-task job; dated operational notes belong in status files, not frontmatter |
| AGENTS.md | Always-on: injected into every session in its repo | No frontmatter, no router — every byte loads on each injection (loader code in both harnesses: omp class `agents-md` `jDe(e,Pqr,"AGENTS.md")`, opencode `y[0]` + config `instructions`; 0 captured injections on this host) | Token drag, stale constraint decay | Terse imperative rules only; no triggers, no prose, no procedures that belong in a skill |
| Command file (`opencode/command/*.md`) | Opt-in: user invokes `/<name>` | `description` + `agent:` frontmatter; body = command contract | Skill drift without a guardrail | Pointer-then-rules idiom: line 1 names the owning skill + `$ARGUMENTS`; then only the literal rules that must hold even if the skill drifts — procedures stay in the skill |
| Dispatch prompt — spawn (L1/L2 lanes) | Ephemeral: consumed once by a subagent (**host-observed** — no harness loads `/home/vgpnk/projects/shokunin/.ufo/prompts/`; the class is a fleet filesystem convention) | Whole file is the contract; no persistence | Missing stanza → unrecoverable agent (no conversation to clarify with) | Fixed 6-stanza order; complete, self-contained; ends with `| godspeed` |
| Dispatch prompt — round (`*-round-N.md`) | Ephemeral: re-ignites a live L1 lane (**host-observed**, same convention; ~72 round files under the shokunin tree) | Relies on durable repo context (SKILL/LOG/corpus) | Stating stale per-round policy (routing maps drift between rounds) | 3–4 lines: role+round → method directive → land-scope+report → `| godspeed`; carry only what changed since spawn |
| CLAUDE.md | Conditional always-on: **omp** registers it as its own class (`claude-md`, "Standalone CLAUDE.md files (Claude Code style)") and reads it *alongside* AGENTS.md; **opencode** reads `CLAUDE.md` (project walk-up `y[1]`) and `~/.claude/CLAUDE.md` (`n[1]`) only while `OPENCODE_DISABLE_CLAUDE_CODE` / `_PROMPT` is unset, and only when no `AGENTS.md` exists in that directory (first name wins in `y`) — cold on this host (0 captured injections) | Same as AGENTS.md: every byte loads when present | Same as AGENTS.md + dual-name collision, now with a **harness divergence**: omp obeys both files, opencode obeys AGENTS.md alone | One owner per repo: redirect file (llama.cpp 1-liner → AGENTS.md) or pick one name; a 4339-line file is an unconditional session tax; never assume both files are read — check which harness you are writing for |
| Cross-tool rule file (`GEMINI.md`, `.cursor/rules/*.mdc`, `.cursorrules`, `.github/copilot-instructions.md`, `.windsurf/rules/*.md`, `*.instructions.md`, `.clinerules`, `SYSTEM.md`/`SYSTEM_TEMPLATE.md`, `CONTEXT.md`) | Loaded as **separate** classes by omp (one per tool ecosystem: gemini/github/cursor/windsurf/clinerules); opencode folds three of the names into one priority list per directory (`y` = AGENTS.md → CLAUDE.md → CONTEXT.md, first hit wins) | Durable rule text wearing another agent's filename convention | Silent rule drift between two agents reading two files; a rename that quietly disables a class on one harness and not the other | One owner per *family*, not per filename: keep AGENTS.md, redirect or delete the rest; omp reads every registered class while opencode reads one name per directory, so agreement is an assumption — the per-class literals are in `corpus/knowledge/instruction-surface-census-round13.md` |
| Declared instruction list (`opencode.json` `instructions: []`) | Opt-in list: each entry is a path, a glob, or an `https://` URL that opencode fetches (`concurrency: 4`) and renders as an `Instructions from: <url>` block beside local files | Composed rule supply: several files, local or remote, merged by the harness | A stale URL or a moved path silently drops a whole rule layer — no diff to review | Prefer repo-relative paths/globs over remote URLs; treat a remote entry as a supply chain (pin it) and edit the target file rather than renaming it — the list is the only pointer |

**AGENTS.md evidence:** six shokunin child repos carry shape-identical 5-line
operating rules (scope, LOG-evidence, no-fabrication) — identical shared body
under a per-repo first line (`md5sum` differs across the six; hashing lines
2+ gives one hash — `/home/vgpnk/projects/shokunin/*/AGENTS.md`, re-verified
round 7). The host-level `~/.agents/AGENTS.md` (75 lines) is NOT pure
constraints: it carries procedures (`Load and obey
~/.agents/godspeed-core/directive.md` at :18, `the-janitor tac-check` at :55)
and dated attestations (:48,:51) — a mixed surface, flagged by the round-7
AGENTS.md checklist audit (`corpus/knowledge/alwayson-checklist-round7.md`).

**Agent-definition evidence:** 18 `.md` files under
`~/.config/opencode/agents/` (14–197 lines) — plus **two count corrections
found in round 13** (connector lane defect D3): that directory holds a 19th
non-`.md` entry (`ls ~/.config/opencode/agents/ | wc -l` → 19), and opencode
loads the *singular* `agent/` directory too (`~/.config/opencode/agent/ufo.md`
is live and is the effective definition for that name; the loader's own doc
table says `agent(s)/<name>.md`). The **omp-side roster** is separate and
ungoverned here: `~/.omp/agent/agents/*.md` → 37 files (excluded in
`corpus/knowledge/instruction-surface-census-round13.md` because its load path
is inferred from `omp agents unpack`, not read from a session). Frontmatter keys
beyond `name`/`description` are routing and
grant policy — `model`/`cascade`/`effort` (distiller, ufo), `permission_mode`/
`agents_md` (distiller), `whenToUse`/`subagents` (orch's delegation roster).
11 of 18 descriptions carry `NOT …` negative routing (round-6 audit,
`corpus/knowledge/agent-def-audit-round6.md`, corrected the round-4 count of
7) — the delegation-table analogue of anti-triggers. Posture text is
copy-pasted: 14 files share one identical 9-line godspeed preamble
(round-4 said 13; orch.md was missed), verified by `md5sum` over the region
and re-verified round 7 (shared md5 `c91c0d66…`, still 14/18);
`mutation-tester.md` carries it **twice** in-file — the observed cost of
copy-paste zones in durable files. The 18/14/11 counts are round-13-unverified
(they are round-6/7 measurements of a directory whose membership has since
changed); re-run the commands before citing them.

**Command-file evidence:** 3 files under `~/.config/opencode/command/`
(10–13 lines). Two idioms: pointer-then-rules (sekhmet.md, xbrd.md — line 1
names the owning skill + `$ARGUMENTS`, then 3–4 rules that must hold even if
the skill drifts) and inline protocol (ufo.md — justified because no skill
owns orchestration). `agent: <name>` in frontmatter delegates to a named
roster agent (ufo.md → `agent: ufo`).

**Spawn dispatch-prompt anatomy** (from `/home/vgpnk/projects/shokunin/.ufo/prompts/*-L1.md`, nominally 9–12 lines each):
`role + working dir` → `context (domain + rank)` → `job (imperative, with
verification commands embedded)` → `L2 routing map` → `report path + scope
fence` → literal ` | godspeed` suffix. A stanza missing from a spawn dispatch
is permanently absent — the subagent cannot ask for it back. Budget the file
for completeness, not brevity; the reader is a blank-context agent. Round
prompts invert this: the reader re-loads its own repo, so the prompt carries
only the round number and method — observed template variance is name + path
(`diff` of `kake-round-4.md` vs `kasegi-round-4.md`, both under
`/home/vgpnk/projects/shokunin/.ufo/prompts/`). Round-7 audit caveat
(`corpus/knowledge/dispatch-prompt-audit-round7.md`): 6 of 8 spawn files
reach 12 lines only by duplicating their first 5 lines with literal `\n`
escapes, and 30/35 round files restate the L2 map (with stale model aliases
`m_composer`/`m_antigravity`/`m_grok` that predate the MISSION.md bucket) —
the artifact population, not the template, is what's dirty.

Craft asymmetry to respect: SKILL.md optimizes *match precision* (trigger
density in the description); AGENTS.md optimizes *constraint survival* (a rule
that must hold unconditionally, so it must be short enough to always be read);
agent definitions optimize *delegation precision* (capability + exclusions an
orchestrator matches); spawn prompts optimize *one-shot completeness*
(everything the reader needs, nothing it can look up); round prompts optimize
*delta-only weight* (everything durable is already in the repo).
