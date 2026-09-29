# Instruction-surface census — round 13

**Claim (the round's axis move, coverage 7 → 8.5).** The instruction-surface
inventory is **derived from loader code**, not from host observation: every class
the two target harnesses can read is named with its literal, its load condition,
and either the craft row that governs it or a reason for excluding it. The
derivation is machine-checked (`verifiers/verify_surfaces.py`) and independently
re-measured by a non-author lane.

**Round-14 amendment (2026-09-28, coverage 8.0 → 8.5).** Two pieces of this
census changed status and are edited in place below rather than left stale:
`surfaces.no_uncovered_class` remains omp-only by construction, and opencode is
covered by its own machine check, `surfaces.opencode_extract` (seven code-shape
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

### B. opencode — instruction model (code-anchored, byte-verified)

The instruction service resolves, in this order (all four quoted from the shipped
JS; the module registers itself as `Instruction.*`):

1. **User-level candidates** — `n = [X.join(config,"AGENTS.md"), …!disableClaudeCodePrompt ? [X.join(home,".claude","CLAUDE.md")] : []]`, first existing wins.
2. **Project walk-up, name-priority** — `y = ["AGENTS.md", …!disableClaudeCodePrompt ? ["CLAUDE.md"] : [], "CONTEXT.md"]`, and `Instruction.find(T)` is
   `for (let d of y) { let w = X.resolve(X.join(T,d)); if (existsSafe(w)) return w }` **per directory**, while `Instruction.resolve` walks `while (G.startsWith(N) && G !== N)` from cwd up to the worktree root. So *within one directory only the first name that exists is claimed*: AGENTS.md beats CLAUDE.md beats CONTEXT.md.
3. **Declared list** — `if (T.instructions) for (let O of T.instructions) { … glob or literal path … }`.
4. **Remote entries** — `Instruction.system` filters `instructions` to `https://`/`http://`, fetches them (`concurrency: 4`) and renders `Instructions from: <url>` blocks next to local ones (`concurrency: 8`).

**Two subsystems, two semantics — do not merge them** (critic lane, round 13):
`Instruction.system`/`systemPaths` is *first-match* per directory
(`Instruction.find` breaks on the first name that exists in `y`), while
`InstructionContext.observe` (targets `["AGENTS.md"]` only, all-match `H.up` from
cwd to the project dir plus `<config>/AGENTS.md`, registered as the
`core/instructions` context provider; `XH.unavailable` when an unreadable project
`AGENTS.md` is present) is *all-match* and ambient — it emits replace/remove
messages when a file changes. Consequence: which rules a session obeys can differ
between the two channels *within one session*. `jX` in `jX(L.config,"AGENTS.md")`
is `path.join` (import verified in the same chunk), so the global candidate is the
opencode config directory, not the cwd — an `[INFERENCE]` the host census left
open — and the ambient channel is why a rule can appear *after* the prompt is
built.

| class_id | literal | kind | governed by | evidence |
|---|---|---|---|---|
| `opencode:instructions/AGENTS.md` | AGENTS.md | loader-literal | AGENTS.md row | `y[0]` in the priority list; `globUp("AGENTS.md",cwd,worktree)` |
| `opencode:instructions/CLAUDE.md` | CLAUDE.md | loader-literal | CLAUDE.md row | `y[1]`, gated by `disableClaudeCodePrompt` = `all({broad: OPENCODE_DISABLE_CLAUDE_CODE, direct: OPENCODE_DISABLE_CLAUDE_CODE_PROMPT})` |
| `opencode:instructions/CONTEXT.md` | CONTEXT.md | loader-literal | Cross-tool rule files | `y[2]`; 1 occurrence of the literal in the opencode binary |
| `opencode:config/AGENTS.md` | AGENTS.md | loader-config | AGENTS.md row | `n[0]` = `<config-dir>/AGENTS.md` |
| `opencode:claude-home/CLAUDE.md` | CLAUDE.md | loader-config | CLAUDE.md row | `n[1]` = `~/.claude/CLAUDE.md` |
| `opencode:config/instructions` | instructions | loader-config | § Instruction surfaces → Declared instruction list | `.instructions` reader + schema example `"instructions": ["AGENTS.md","docs/style.md"]` |
| `opencode:config/instructions-remote` | https:// | loader-config | Declared instruction list | `Instruction.system` fetches `https://`/`http://` entries (`concurrency: 4`, 5 s timeout) and renders `Instructions from: <url>` |
| `opencode:read-hook/instructions` | <system-reminder> | loader-literal | Cross-tool rule files | second channel: `Instruction.resolve`, called from `ReadTool.execute`, appends the nearest ancestor instruction file to a **tool result** as a `<system-reminder>` — a rule can arrive mid-session attached to a read (second witness §4; 18 literal hits in the opencode bytes) |
| `opencode:instruction-context/AGENTS.md` | AGENTS.md | loader-literal | AGENTS.md row | **second subsystem, its own load condition** (round 14, after the blind witness enumerated it and left it id-less): `A=M.fn("InstructionContext.observe")` registered as the `system-context-builtins` context with key `BP=XH.Key.make("core/instructions")`, walking `H.up({targets:["AGENTS.md"],start:cwd,stop:project})` **all-match** and keeping an **ungated** `<config>/AGENTS.md` candidate (`jX(L.config,"AGENTS.md")`). Same file class as `opencode:instructions/AGENTS.md`, different semantics (ambient, all-match, replace/remove on change vs first-match per directory), so it is declared separately rather than merged into that row's prose. Rule `OC-6` in `opencode-extraction-round14.md` owns it |

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
| No loader-derived inventory existed | this file + `verifiers/verify_surfaces.py` (round 13: 4 checks; round 14: 7 checks incl. `surfaces.opencode_extract`, `surfaces.literal_parity`, `surfaces.kind_parity`, exit 0/1/2/3, `--self-test` 72 assertions) + `verifiers/surfaces-baseline.json` |
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
  `surfaces.opencode_extract` — seven code-shape rules (OC-1…OC-6, anchors and
  derive-vs-witness stated per rule) that must reproduce all 9 declared opencode
  class ids, must produce no undeclared id, must each match, and must not produce
  zero classes (a zero extraction FAILs with `vacuity:`). Evidence, drop-one
  matrix and residual ceilings: `opencode-extraction-round14.md`.
  For omp the check is real (8 extracted pairs, parity both ways, an empty baseline
  produces 41 `extra row` findings — recorded in the round's evidence). Parity is
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