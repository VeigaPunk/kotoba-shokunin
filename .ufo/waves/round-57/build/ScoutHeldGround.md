Result: DONE — at base `47c05558` all eight likely manifest tokens are absent outside `.ufo/` (case-sensitive 0, case-folded 0, and the frozen counter's own held rule returns False for each), while 49 files / 115 lines state plugin/extension facts; 24 held statements the new entry must agree with, scope or correct are listed below with path:line.

# ScoutHeldGround — what the lane already holds about plugins/extensions at base

Seat: `KotobaR57.ScoutHeldGround` (leaf). Read-only plus one sandbox probe. No lane file written; no counter edited.
Sandbox: `/fast/scratch/hyaku/kotoba-r57/KotobaR57.ScoutHeldGround`, cloned from the lane and checked out at
`01312a77e36317feb6e961aba77841ddab1225ca` (`git rev-parse --short HEAD` → `01312a7`, 180 MB). Probe scripts
`probe_held.py`, `probe_burned.py` live there only. Lane reads use `git --no-optional-locks`; no git/jj write
anywhere. `date -u` at probe time: `Fri 23 Oct 2026 04:49:07 AM UTC`. No tool installed or upgraded.

## 1. Population and method

- `git -C <lane> grep -l -i -E 'plugin|extension' 47c05558 -- . ':!.ufo'` → **49 files**; `-h … | wc -l` → **115 matching lines**.
  Restricted to `*.md`: **32 files / 68 lines** (exit 0 for both).
- `SKILL.md` at base: **0** matches (`git grep … 47c05558 -- SKILL.md` exit 1). At `01312a77` it holds exactly **one**:
  `SKILL.md:464`, the C1 Gate-registry row naming `verifiers/check_plugin_manifests.py` (added by the freeze commit,
  not held ground). So any statement that "SKILL.md says nothing about plugins" is true only of base.

## 2. The direct question: are the likely manifest tokens held at base?

Raw substring counts, `git grep -F -o … <token> 47c05558 -- . ':!.ufo'`, case-sensitive (cs) and case-folded (cf):

| token | cs | cf | occurrences inside `.ufo/` (ci) |
|---|---|---|---|
| `.claude-plugin/plugin.json` | 0 | 0 | 24 `plugin.json` + 15 `.claude-plugin` occurrences (overlapping; all under `.ufo/`) |
| `.codex-plugin/plugin.json` | 0 | 0 | 0 |
| `.cursor-plugin/plugin.json` | 0 | 0 | 0 |
| `gemini-extension.json` | 0 | 0 | 4 (`gemini-extension`) |
| `.github/plugin/plugin.json` | 0 | 0 | 0 |
| `plugin.json` | 0 | 0 | 24 |
| `.opencode/plugins` | 0 | 0 | 0 |
| `.opencode/plugin` | 0 | 0 | 0 |

Extra tokens the plan claims, confirmed: `.claude-plugin` 0/0, `.codex-plugin` 0/0, `.cursor-plugin` 0/0,
`.github/plugin` 0/0, `marketplace.json` 0/0 (15 in `.ufo/`), `.opencode/plugin/` 0/0. The exclusion is load-bearing:
without `':!.ufo'` the same greps return non-zero counts from `.ufo/` only.

Rule-exact confirmation (not a substring proxy): ran the **frozen counter's own** `held_in_base()` —
case-insensitive at path-segment boundaries, NUL-free blobs only, `.ufo/` never read — over base:

```
cd /fast/scratch/hyaku/kotoba-r57/KotobaR57.ScoutHeldGround && timeout 240 python3 -B probe_held.py   # exit 0
counter sha256 bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e
base 47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a blobs outside .ufo/ 519
.claude-plugin/plugin.json             held=False     .codex-plugin/plugin.json   held=False
.cursor-plugin/plugin.json             held=False     gemini-extension.json       held=False
.github/plugin/plugin.json             held=False     plugin.json                 held=False
.opencode/plugins                      held=False     .opencode/plugin            held=False
```

Discrimination controls in the same run (proof the probe can say True): `plugins` **True**, `extensions` **True**,
`Extensions` **True**, `.claude/plugins` **True**, `claude-plugins` **True**, `.github/instructions` **True**,
`.cursor/rules` **True**, `.opencode/agents` **True**, `plugin` **True**; `claude-plugin` (singular, undotted)
**False**, `marketplace.json` **False**, `gemini-extension` (prefix) **False**.

Consequence for `new ground G`: the *words* `plugin(s)`/`extension(s)` are held, and so are the global roots
`~/.config/opencode/plugins` and `~/.claude/plugins`, but no manifest **path** is. G ≥ 3 on path tokens is reachable
without tuning — this is exactly the trap `CtlC1HeldVariant` fell into under v1 and v2 closed with the boundary rule.

## 3. Statements the new entry must agree with, scope, or correct

Direction key: **CORRECT** = the statement becomes false or too wide; **EXTEND** = append-only note, do not rewrite;
**AGREE** = the entry may not contradict it; **SCOPE** = the entry must narrow it explicitly.

### 3.1 Custody and province (must be corrected or extended if C1 lands)

| path:line | what it holds | direction / what the entry (or L1) must do |
|---|---|---|
| `PROVINCE.md:19` | "…checked by `verifiers/check_mcp_instructions.py`. **Plugin surfaces and measured client behaviour stay Frontier.**" | CORRECT: plugin *manifest documentation* moves to Core in part (round-52 pattern "moved from Frontier … in part"); keep "measured client behaviour" Frontier verbatim, and add that C1 documents what manifests declare, not that clients load them. |
| `PROVINCE.md:28` | Frontier bullet: "…MCP/plugin instruction surfaces (round 52: MCP server `instructions` per client moved to Core; **plugin surfaces and measured client behaviour stay here**)…" | CORRECT the same clause only; leave the rest of the bullet (sibling arbitration, command extraction, R-items) untouched. |
| `corpus/README.md:102` | Frontier row `MCP/plugin instruction surfaces`: "the two target harness configs carry no MCP/plugin keys; the classes are live elsewhere" | EXTEND: the row now has two held halves (MCP round 52 at `:106-109`; plugin manifests round 57). If the counter docstring's Frontier row *Plugin manifests* is added, it must claim only manifests + declared payload surfaces, and the parent row keeps measured behaviour and non-manifest plugin surfaces. |
| `corpus/README.md:110-111` | "still not held: **plugin surfaces**, tool-description budgets beyond the two documented limits, and any measured client behaviour" | CORRECT: "plugin surfaces" becomes partially held (manifests); tool-description budgets and measured client behaviour stay not held. |
| `SCORECARD.md:130`, `SCORECARD.md:134` | historical next-round lists name "plugin instruction surfaces" / "carried: … plugin surfaces" | AGREE with no edit (history); the round-57 SCORECARD entry must not repeat "plugin surfaces" as wholly carried. |
| `corpus/lessons/round-53.md:80` | "Carried with reasons … plugin surfaces (Frontier; not this round's area)" | AGREE, historical; cite as the carry history if the entry needs one. |
| `corpus/knowledge/mcp-server-instructions-round52.md:7` | "Frontier area: MCP and plugin instruction surfaces (`corpus/README.md` § Frontier; `PROVINCE.md` § Frontier)." | AGREE: the new entry is the sibling half of the same Frontier area; it must cite the same row and must not re-open the MCP half. `:67-89` is also the shape model (docs-only, no client run, omp not checked, revision caveats). |

### 3.2 Loader/model facts (the entry may not contradict these)

| path:line | what it holds | direction / consequence |
|---|---|---|
| `corpus/knowledge/instruction-surface-census-round13.md:266` | `omp:discovery/plugins`, literal `plugins`: "**Plugin module roots (`~/.config/opencode/plugins`, marketplace cache) — code, not text**" | AGREE. (a) opencode's held plugin root is a JS-module root with **no manifest file**; (b) the held string is the *global* `~/.config/opencode/plugins`, not project `.opencode/plugins` — a project token is new by string but **not by class**, so the entry must not present the root as newly discovered; (c) a client with no `.json` manifest cannot count (round context) — say so, do not invent one. |
| `census:265` + `verifiers/surfaces-baseline.json:197-202` | `omp:discovery/extensions`, literal `extensions`: "Extension/hook/tool module roots (`.gemini/extensions`, `.codex/tools`, `.claude/hooks`) — executable surfaces, out of prompt-craft province" | AGREE + SCOPE: `gemini-extension.json` is the manifest that *declares* an extension; the census excludes the *module root* as code. The entry must draw that line, or the two statements read as contradictory. The class is pinned in the baseline, so adding/rekeying a census class would move `verify_surfaces.py` — forbidden this round. |
| `census:100` + `surfaces-baseline.json:146-148` | `omp:marketplace/plugin-rules`: "Load rules from marketplace plugin rules directories" | AGREE: omp reads rule text out of marketplace plugin dirs; a marketplace index (`marketplace.json`) is a catalogue, not a plugin manifest — this is why the counter rejects any `marketplace` segment, and the entry should say the distinction, not omit it. |
| `census:93`, `census:115-116`, `instruction-surface-remeasure-round13.md:33` | `claude-plugins` in omp's opt-in set `RTo`; priorities `omp-plugins 90`, `agent-plugins 70–75`, `claude-plugins 70` | AGREE: omp treats plugin dirs as *instruction providers*; plugin-shipped **rule/context text** is a live surface (user-level only behind `enabledProviders`). "What a plugin can ship" must not stop at skills/agents/commands/MCP. |
| `census:283` | opencode non-file prompt surface list includes "the plugin `experimental.chat.system.transform` hook" | AGREE: plugin code can inject system-prompt text at runtime; even if opencode's row says "no `.json` manifest", this surface is already held and must not be denied. |
| `census:391` + `corpus/README.md:166-174` + `LOG.md:85-86` | "host absence ≠ support absence"; `~/.config/opencode/plugin/fnm-nudge.js` live; LOG's "MCP/plugin surfaces verified absent" refined | AGREE: never restate "plugin surfaces absent". The live instance is a JS nudge script (a hook, not a manifest); what the two target configs lack is *keys*, not the class. |
| `census:187,193,195,222`, `census:296-298`, `census:310-312`, `LOG.md:935,938`, `corpus/knowledge/opencode-extraction-round14.md:9` | `ConfigInstructionPlugin` ("the plugin subscribes every candidate file and republishes on change"), `ReadTool.Plugin`, `SessionInstructions.load` as opencode anchors | **False friend**: these are opencode config-plugin class/API names, not client plugin packages. Must not be cited as plugin-surface evidence. |
| `corpus/knowledge/agent-definition-files-round56.md:62` + `SKILL.md:104` | Codex agent files: five `features.*` keys set to false (`shell_tool`, `apps`, **`plugins`**, `memories`, `request_permissions_tool`) | AGREE: Codex gates plugins behind a feature key a subagent file cannot enable; the Codex row's Action must not imply an agent file controls plugins. |

### 3.3 Other held observations (one real conflict risk)

| path:line | what it holds | direction / consequence |
|---|---|---|
| `corpus/knowledge/claude-md-surface.md:61` | "Vendored CLAUDE.md in `go/pkg/mod`, bun cache, **plugin dirs are inert (never cwd)** — count them out of any surface census." | **SCOPE or CORRECT at the line.** If the Claude row says a plugin can ship context/rule text, "plugin dirs are inert" becomes too wide. The defensible reading is "plugin dirs are not cwd-walked for CLAUDE.md discovery"; add the dated narrowing at the line (round-56 R6 precedent) rather than leaving both statements unreconciled. |
| `claude-md-surface.md:41` | `claude plugin configure cc-plugin-agents-md@builtin --json` (Claude Code 2.1.304; default `claude-md-or-agents-md`) | AGREE: a Claude **built-in plugin** is already configured on this host and governs CLAUDE.md/AGENTS.md preference. The entry must not claim no plugin is configured here. |
| `render-mechanism-round7.md:72`; `harness-router-models-round9.md:79`; `harness-verifier-round10.md:132`; `harness-independent-round37.md:158,288,447`; `verifiers/baseline.json:121` | `~/.claude/plugins/cache` / `oc.roots.plugins_cache` | AGREE: on this host Claude's plugin root is a *cache of per-plugin directories* (the natural home of `.claude-plugin/plugin.json` — [INFERENCE], not measured). Round 10 recorded the path absent and round 37 `:447` records a two-path ambiguity, so cite it as a dated path observation, not a live inventory. |
| `corpus/knowledge/opencode-offer-trace-round8.md:75` | `~/.config/opencode/` = "config/agents/plugin/skills **symlinks** — inputs to discovery, not session state" | AGREE: the opencode global plugin entry is a symlink to a JS file; "plugin" there is a file, not a directory with a manifest. |
| `corpus/knowledge/sibling-overlap-census-round49.md:216-217`, `corpus/knowledge/skill-selection-rules-round50.md:22` | S028 quote "**Agents and skills** use first-found-wins precedence." (`cli-plugin-reference.md:415`) | AGREE: Copilot CLI arbitrates duplicate plugin components by first-found-wins; the entry must not state a different precedence. |
| `corpus/lessons/round-54.md:42`, `corpus/lessons/round-54-verifier-spotcheck.md:186`, `corpus/SOURCES.md:41` (S028), `corpus/lessons/round-51.md:50` | "the caps are on **plugin manifest and marketplace metadata**, not on a skill's `description`"; S028's fetch record names "§ Plugin entry fields (`:349`)"; S028 "was not used: it does not carry this lever" | AGREE on content + **sourcing constraint**: the lane already holds that Copilot CLI documents plugin-manifest fields, but S028 is a BASE row whose URL is a base URL, so the C1 counter rejects it. The Copilot row must open a **new** docs.github.com page, must not present that manifest as new ground, and must not assert a per-skill removal lever (round-51 checked S028 for one and found none). |
| `corpus/knowledge/skill-overlap-levers-round51.md:101` | VS Code `ChatStrictPluginOnlyCustomization` (all-or-nothing switch) | AGREE: VS Code's docs distinguish plugin-provided customization; the VS Code Action must not read as a skill-removal lever and must not contradict this switch. |
| `corpus/knowledge/frontmatter-rule-authorities-round48.md:51` | Anthropic `build-skills.md:11` mentions a plugin directory | AGREE: supports (does not prove) that Claude skills travel in plugins; it is not a frontmatter rule and not a manifest path. |
| `corpus/lessons/round-56.md:36`, `corpus/lessons/round-56-verifier-spotcheck.md:192` | `agent-plugins.org/specification.md` rejected: not a pinned host, states a negative only | AGREE: do not revive it as a source; a cross-client plugin spec is not a client manifest row. |

### 3.4 Word collisions that are **not** held ground (do not cite as plugin claims)

`corpus/QUALITY.md:36` ("counts names, extensions or rows" — file extensions); `LOG.md:649` ("citation-resolution extension");
`considerthese/2026-10-19.md:78` ("`verify_corpus_integrity.py` extension"); `corpus/knowledge/alwayson-rule-files-round53.md:62`
("lane extension of the skills rule"). Also `census:265-266`'s literals `plugins`/`extensions` are held **words**, not
held paths — confirmed True by the probe while all eight path tokens are False.

Completeness of the non-prose surface: no verifier at base reads a plugin manifest. The pinned plugin/extension values are
`verifiers/baseline.json:121` (`oc.roots.plugins_cache`) and `verifiers/surfaces-baseline.json:146-148,197-210` (the three census
rows above). Two traps in `verifiers/*.py`:
`verifiers/check_overlap_levers.py:908-916` is a **crafted false-pass world B** ("Copilot CLI | managed plugin policy … `enabledPlugins`,
`extraKnownMarketplaces`"); `enabledPlugins`/`extraKnownMarketplaces` occur **nowhere in `corpus/`** at base, so that row is a test
input, not a held fact and not citable.
`verifiers/check_explicit_invocation.py:146-153` lists `plugin`/`plugins` in `BUILTINS`, i.e. built-in CLI command words the round-55
counter excludes — a vocabulary fact, not a plugin-surface statement. A C1 change needs no pinned-value edit — and must not cause one.

## 4. Corpus contracts the entry must satisfy (binding, not content)

- **Index row**: `corpus/README.md:30-91` is the coverage map (`| Note | File | … |`, last row `Round-56 lessons` at `:91`).
  `verifiers/verify_corpus_integrity.py` INDEX reads column 2 only, so the new `knowledge/plugin-manifests-round57.md`
  needs a row, and `corpus/lessons/round-57.md` needs one; otherwise `corpus.index.unindexed` fails (rounds 46, 48–50, 53, 54
  each landed "unindexed 1" once).
- **SOURCES**: header at `corpus/SOURCES.md:12-13` is 11 columns (`id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by`).
  Rows are append-only (M45; `verifiers/check_sources_append_only.py`). Highest id at base **and** at `01312a77` is **S078**
  (`git grep -E 'S07[9]|S08[0-5]' …` exit 1 both), so **S079–S085 are free**; the C1 spec's per-client order is
  S079 Claude Code, S080 Codex, S081 VS Code, S082 Copilot CLI, S083 Gemini CLI, S084 Cursor, S085 opencode
  (the frame in `build/ScribeC1Entry.md` already uses that order).
- **Gate**: each quote must also occur, whitespace-normalised, in `corpus/lessons/round-57.md` § `## Gate`; that file does
  not exist at `01312a77`, so it is a landing prerequisite.
- **Gate registry**: `SKILL.md:440-446`; the C1 row already exists at `SKILL.md:464` (tip). The new `### Plugin manifests by client`
  heading is separate and must leave registry rows alone (`check_gate_registry.py` compares rows with files).
- **Line budget**: `SKILL.md` is 596 lines at base and 598 at `01312a77` (budget 600) — the plan's `ExecBudgetMove` must land
  before the table; this seat did not verify any budget move.

## 5. Frozen counter constraints (form, from `verifiers/check_plugin_manifests.py` v2 @ `01312a77`, sha256 `bf11a4ef…`)

SKILL heading exactly `### Plugin manifests by client`; first table header exactly
`| Client | Plugin manifest | What a plugin can ship | Action |`; entry header `| Client | Manifest | Source | Quote |`.
Manifest cell's **first** backticked span = the token; entry `Manifest` cell must equal it (backticks stripped, case-sensitive).
Token: final segment ends `.json` **and** carries `plugin(s)`/`extension(s)`; ≥2 segments after one `~/`/`./`, or contains the
row's own client marker; no `marketplace` segment; no dotted non-final segment except as its first character; no other client's
marker. Quote 6–25 words, containing the token verbatim (case-sensitive) and a `plugin(s)`/`extension(s)` word **outside** it.
Source row: not at base, kind `docs`, tier `A`, status `mined`, opened `2026-10-23`, URL on the client's pinned host (segment-exact),
URL not equal (after `url_key`) to any base row's URL, no `changelog|release|releases|news|blog` path segment.
K = well-formed rows; F = live pages holding quote+token; G = distinct casefolded tokens with no held occurrence at base.

**Burned hosts/routes — every base row on a client's pinned hosts is unusable as a C1 source** (`probe_burned.py`, exit 0):

| client | base rows on its pinned hosts (id: path) |
|---|---|
| Claude Code | S003, S019 `platform.claude.com/…/best-practices`; S022, S053, S065 `code.claude.com/docs/en/skills`; S023 `…/overview`; S026 `…/sub-agents`; S033 `…/mcp`; S043 `…/memory`; S072 `…/agent-sdk/subagents`; S062 `…/claude-code/<sha>/changelog` (also E3) |
| Codex | S013, S021, S054 `learn.chatgpt.com/docs/build-skills`; S044 `…/agent-configuration/agents-md`; S063 `…/config-file/config-reference`; S035 `developers.openai.com/codex/mcp`; S073 `…/codex/subagents`; S066 `…/blog/eval-skills` (also E3) |
| VS Code | S025, S055, S067 `code.visualstudio.com/docs/agent-customization/agent-skills`; S074 `…/custom-agents`; S047 `…/copilot/customization/custom-instructions`; S034 `code.visualstudio.com/updates/v1_104` |
| Copilot CLI | S028 `docs.github.com/…/cli-plugin-reference`; S031, S038, S056 `…/cli-command-reference`; S027, S030, S048, S068, S075 `docs.github.com/en/copilot/…`; S042 `raw…/copilot-cli/<sha>/changelog` (E3) |
| Gemini CLI | S029 `geminicli.com/docs/cli/skills`; S057 `…/skills-best-practices`; S036 `…/tools/mcp-server`; S076 `…/core/subagents`; S046, S060, S069 raw `google-gemini/gemini-cli/<sha>/…` |
| Cursor | S049 `cursor.com/docs/rules`; S052 `cursor.com/help/customization/rules`; S058 `cursor.com/docs/release-notes`; S070 `…/skills`; S077 `…/subagents` |
| opencode | S024, S039, S059 `opencode.ai/docs/skills`; S064 `opencode.ai/v2/docs/skills`; S045 `opencode.ai/docs/rules`; S016, S051 `github.com/anomalyco/…`; S041, S071, S078 raw `…/docs/content/*.mdx` |

Note the pin shape: bare hosts match any path (`host == h or host.endswith("." + h)`); `github.com/anthropics/claude-code`-style pins
match a path prefix only (`host_ok`, `:513-530`). `url_key` strips a trailing `.md`, so `…/plugins` and `…/plugins.md` are one key.

## 6. What this seat did **not** establish

- **No live page was opened.** Whether any client documents a `.json` plugin manifest, and what it says, is the source seats' question;
  nothing here is a source claim.
- **Cursor**: base holds **zero** statements about Cursor plugins (`cursor-plugin` 0, no plugin mention on any cursor.com row).
  Its row is unconstrained by held text — new ground by string, with nothing to agree with.
- **opencode**: base says plugins are *code modules* (`census:266`), with no manifest; per the round context its row "cannot count"
  unless documentation names a `.json` manifest — the entry must say so honestly. F ≥ 5 must come from the other six.
- **Gemini CLI**: the class `extensions` is held, the token `gemini-extension.json` is not; the entry must connect the manifest to the
  existing class rather than present extensions as a discovery.
- **VS Code**: the only held plugin-adjacent statement is the `ChatStrictPluginOnlyCustomization` lever; the word "extension" in base is
  never about VS Code extensions.
- `[INFERENCE]`: that `.claude-plugin/plugin.json` sits under `~/.claude/plugins/cache/<plugin>/` — implied by the five cache-path
  observations, not measured by this seat.
- Consistency check against sibling drafts (read-only): `build/ScribeFrontier.md`'s conditional Core bullet and append-only note agree
  with §3.1 (`PROVINCE.md:19,28`, `corpus/README.md:102,110-111`) and keep measured behaviour Frontier; `build/ScribeC1Entry.md`'s frame
  uses S079–S085 in the counter's client order. Neither draft conflicts with any statement above.
