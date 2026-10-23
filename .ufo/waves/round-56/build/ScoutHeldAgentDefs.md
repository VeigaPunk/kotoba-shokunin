# ScoutHeldAgentDefs — what the lane holds about agent-definition files at base b0b7140b

Result: DONE — the base tree holds opencode's agent-definition surface in depth (18 files, keys,
reachability, a nine-box checklist), holds Claude Code's directory only as an `AGENTS.md`
case-collision plus wave/row shadows, holds nothing for Codex as a definition location, and holds
nothing at all for VS Code, Copilot CLI, Gemini CLI or Cursor; C1's new ground (G>=2) can only come
from two distinct zero-count paths among {VS Code, Copilot CLI, Gemini CLI, Cursor}.

Seat: KotobaR56.ScoutHeldAgentDefs (round 56 build wave, leaf scout). Read-only: no lane file edited
except this report; no sandbox clone needed (only read-only git in the lane); no lane code executed;
no counters touched; no installs; no model calls. Work rev
`e02f5f5d2f37427e8a77b1c3efb45f84b78c67c8`; base `b0b7140b5a7cf8a50f13989ee6285fc8ee245c41` (the
counter's frozen `BASE_REV`, `verifiers/check_agent_definitions.py:120`). No C1 content exists at the
work rev yet (`git cat-file -e e02f5f5d:corpus/knowledge/agent-definition-files-round56.md` → exit
128; same for `corpus/lessons/round-56.md`), so this is a pre-content read.

## 1. What the counter will treat as held (mechanical G=0 forms)

Rule: G counts DISTINCT `normalise()`d paths whose case-insensitive fixed-string count in the
BASE_REV tree outside `.ufo/` is zero (`verifiers/check_agent_definitions.py:222-231`; spec docstring
`:1-90`). I ran the exact frozen command
`git -C <lane> --no-optional-locks grep -i -F -c -e <form> b0b7140b -- . ':!.ufo'` for every
candidate form. Counts (matching lines summed):

| normalised form | count at base | what the matching base text actually is |
|---|---|---|
| `.claude/agents` | 3 | all three are `.claude/AGENTS.md` case collisions: `corpus/knowledge/alwayson-rule-files-round53.md:25`; `verifiers/verify_alwayson.py:22`, `:77` |
| `.claude/agent` | 3 | same lines (substring of the plural) |
| `.codex/agents` | 5 | all five are `~/.codex/AGENTS.md` collisions: `LOG.md:484`; `alwayson-rule-files-round53.md:82`; `instruction-surface-census-round13.md:98`; `instruction-surface-remeasure-round13.md:63`, `:65` |
| `.opencode/agents` | 10 | 9 real `opencode/agents/*.md` lines in `verifiers/checklist-baseline.json:100-148` + one `.opencode/AGENTS.md` collision at `instruction-surface-remeasure-round13.md:63` |
| `.opencode/agent` | 10 | same lines (substring of the plural) |
| `.config/opencode/agents` | 24 | genuine opencode agent-definition text (see §2) |
| `.config/opencode/agent` | 25 | same 24 + `instruction-surface-census-round13.md:496` (singular `agent/` dir) |
| `.agents/agents` | 18 | all `~/.agents/AGENTS.md` collisions — mechanically held although the lane never calls it an agent-definition directory |
| `.github/agents`, `.github/agent`, `.vscode/agents`, `.vscode/agent`, `.copilot/agents`, `.copilot/agent`, `.gemini/agents`, `.gemini/agent`, `.cursor/agents`, `.cursor/agent` | 0 | no base text |

Mechanical consequences:
- Claude Code, Codex and opencode rows can never contribute G, whatever their docs say; only their
  F can count.
- G>=2 needs >=2 DISTINCT forms from {VS Code, Copilot CLI, Gemini CLI, Cursor}. `.github/agents`
  used for both VS Code and Copilot CLI is ONE distinct form → G=1.
- `.agents/agents` is held (18 hits) even though every hit is `.agents/AGENTS.md` — the
  `CtlC1RealNoForm` control used exactly this form for VS Code and Copilot CLI; do not reuse it.
- [INFERENCE] the `.claude/agents` and `.codex/agents` holds are case-insensitive collisions with
  the AGENTS.md always-on names, not statements that those directories are agent-definition
  locations; the counter cannot see the difference, so both clients are barred from G either way.

## 2. Held knowledge by client (path:line at b0b7140b, outside .ufo unless stated)

### opencode — deep; the only client with a held per-file surface
Paths:
- `~/.config/opencode/agents/*.md` (18 files, 14–197 lines): `SKILL.md:520`; `LOG.md:26`, `:73`;
  `corpus/knowledge/agent-defs-commands-and-round-prompts.md:9`;
  `corpus/knowledge/agent-def-audit-round6.md:5`;
  `corpus/knowledge/instruction-surface-census-round13.md:493`;
  `corpus/knowledge/sibling-overlap-census-round49.md:408`, `:410`; `PROVINCE.md:50`;
  `corpus/lessons/round-4-aggregator-audit.md:20`, `:30`, `:33`, `:46`;
  `corpus/lessons/round-6-aggregator-audit.md:44`.
- `opencode/agents/*.md` (checklist scope; 53 files over 3 roots at round 15: 18 live
  `~/.config/opencode/agents` + 18 `~/Projects/experimental-opencuff/.opencode/agents` + 17 snapshot
  under `~/Projects/webzites/.../state`): `SKILL.md:310`; `corpus/README.md:13`, `:19`;
  `instruction-surface-census-round13.md:473`; `corpus/knowledge/checklist-execution-round15.md:250`;
  `verifiers/checklist-baseline.json:100,106,112,118,124,130,136,142,148`.
- singular `~/.config/opencode/agent/` is loaded too (`~/.config/opencode/agent/ufo.md` live; the
  loader's own doc table says `agent(s)/<name>.md`): `instruction-surface-census-round13.md:495-497`.
- omp-side roster `~/.omp/agent/agents/*.md` (37 files, ungoverned; not one of the seven clients):
  `instruction-surface-census-round13.md:498`.
- Roster artifacts: `opencode.json` `agent` map (15 of 18; `ufo` is `default_agent`;
  distiller/janitor/musketeer reachable only via `orch.md` `subagents:` 16 entries; fileless config
  keys devin/kimi/raw): `corpus/knowledge/agent-def-audit-round6.md:53-59`.
- Command surface `~/.config/opencode/command/*.md` (3 files, `agent:` delegation key):
  `agent-defs-commands-and-round-prompts.md:51-63`; `SKILL.md:526`.

Statements:
- Two-zone structure (frontmatter + a system prompt loaded for every task): 
  `agent-defs-commands-and-round-prompts.md:7-11`.
- Frontmatter key table: `agent-defs-commands-and-round-prompts.md:13-20` (keys listed in §3).
- `description` capability + negative routing 11/18: `agent-defs-commands-and-round-prompts.md:22-27`;
  corrected counts (13→14 preamble, 7→11 routing): `agent-def-audit-round6.md:62-67`.
- Posture copy-paste 14/18, doubled in `mutation-tester.md` (lines 8–14 + 34–40):
  `agent-defs-commands-and-round-prompts.md:28-41`.
- Dated frontmatter `cascade_note` goes stale: `agent-defs-commands-and-round-prompts.md:44-49`.
- 15/18 clean verdict matrix; the four fails (ufo.md AD-1 `:36`, AD-5 `:41`; mutation-tester.md
  AD-7 `:45`; scout.md AD-9 `:47`): `agent-def-audit-round6.md:1-90`.
- Census surface row — "Roster: orchestrator picks by `description`, then body becomes the
  subagent's system prompt": `instruction-surface-census-round13.md:473`.
- Nine-box fidelity checklist, opencode-scoped, all boxes unexecuted:
  `SKILL.md:308-352` (box lines `:316, :318, :321, :325, :332, :337, :340, :345, :347`; intro
  "Run before shipping any `opencode/agents/*.md`" `:310`); dispositions + `text_sha256`:
  `verifiers/checklist-baseline.json:97-149` (`agentdef.01`–`agentdef.09`).

### Claude Code — directory held only in shadows
- S026 is a base row (`corpus/SOURCES.md:39`), "Create custom subagents". Its detail cites the
  location priority table (`sub-agents.md:158-164`) and the same-name paragraph (`:156`, `:176`)
  without naming any path; its recorded quote is the delegation sentence
  ("When Claude encounters a task that matches a subagent's description…", `sub-agents.md:11`):
  `corpus/lessons/round-50.md:60`. Re-opened byte-identical in round 50:
  `corpus/lessons/round-50-verifier-spotcheck.md:231-235`.
- The paths themselves (`.claude/agents/` project, `~/.claude/agents/` user, plugin `agents/`) are
  held only in the round-50 wave record: `.ufo/waves/round-50/build/SrcClaudeSubagents.md:49`
  ("managed settings 1 (highest), `--agents` CLI 2, `.claude/agents/` 3, `~/.claude/agents/` 4,
  plugin `agents/` 5 (lowest)"), present at b0b7140b, 15,224 B — and `.ufo/` is excluded from the
  counter's base text, so it does not even supply the collision count.
- Mechanical hold: `.claude/agents` = 3, all `.claude/AGENTS.md`
  (`alwayson-rule-files-round53.md:25`; `verify_alwayson.py:22`, `:77`).
- No base text anywhere writes lowercase `.claude/agents` outside `.ufo/` (`~/.claude/agents` = 0
  hits).

### Codex — nothing about agent definitions
- Base holds `~/.codex/AGENTS.md` as a user-level always-on file: `alwayson-rule-files-round53.md:81-82`;
  `instruction-surface-remeasure-round13.md:65`; `instruction-surface-census-round13.md:98`;
  `LOG.md:484`.
- No base statement that Codex has an agent-definition directory; `.codex/agents` = 5 only through
  those `AGENTS.md` strings.

### VS Code / Copilot CLI / Gemini CLI / Cursor — nothing
- No agent-definition path, key or per-client statement outside `.ufo/`. Their base rows are
  skills/instructions/release-notes surfaces only: VS Code S025, S034, S047, S055, S067;
  Copilot CLI S027, S028, S030, S031, S038, S048, S056, S068; Gemini CLI S029, S036, S057;
  Cursor S049, S052, S058, S070.
- Exactly one base SOURCES row concerns subagent definitions at all: S026. Every other row matching
  `agent` is a skills / instructions / MCP row.

## 3. Keys held (opencode agent files only)
`name`, `description` (roster index); `model`, `cascade`, `cascade_class`, `effort`, `variant`
(routing/cost policy); `permission_mode`, `agents_md`, `prompt_mode`, `mode`, `steps`, `permission`
(capability/scope grants); `whenToUse`, `subagents` (orchestrator's delegation roster) —
`agent-defs-commands-and-round-prompts.md:15-20`; `SKILL.md:521`; reachability
`agent-def-audit-round6.md:53-59`. No other client's agent-file keys are held at base.

## 4. C1 table cells: new knowledge vs restatement

Per-row verdict for the `### Agent-definition files by client` table (location cell = FIRST
backticked span; what the counter can score):

| Row | Location cell candidate | Counter verdict | New or restatement |
|---|---|---|---|
| Claude Code | `.claude/agents` (or `~/.claude/agents`) | held (3) → G=0; S026's URL is a base URL, so a new page is required even for F | RESTATEMENT of the wave-record/S026 scope knowledge; only F can be gained |
| Codex | `.codex/agents` | held (5, AGENTS.md collisions) → G=0 | cell content would be new knowledge (base holds none) but scores no G; F only |
| opencode | `.opencode/agents` or `~/.config/opencode/agents` | held (10 / 24) → G=0 | RESTATEMENT of §2 in full |
| VS Code | `.github/agents` (0) or `.vscode/agents` (0) | new if documented, own root `.github`/`.vscode`, kind `docs` | NEW knowledge if a new page documents it |
| Copilot CLI | `.github/agents` (0) or `.copilot/agents` (0) | new if documented; shares the `.github/agents` form with VS Code → only 1 distinct G form if both use it | NEW |
| Gemini CLI | `.gemini/agents` (0) | new if documented | NEW |
| Cursor | `.cursor/agents` (0) | new if documented; Cursor's own page also lists `.claude/agents/` and `.codex/agents/` compatibility (control evidence `CtlC1RealNoForm.md:96`), but those are held forms and not Cursor's own root (`OWN_ROOTS`, counter `:412-427`) | NEW |

Other columns: "What the file sets" — opencode is restatement (two-zone structure, keys,
reachability); the six other clients' content would be new knowledge, but the counter does not
measure it (Q31; reviewer reading in the falsify wave). "Action" — unmeasured beyond >=3 words.
Source/Quote — must be new rows (base has S001–S071, so S072+), quotes 3–25 words with the location
token verbatim (or without a leading `~/` / trailing `/`) plus `agent`/`subagent` outside the token.

F/G arithmetic the build must satisfy: F>=5 = the three held clients plus >=2 of the four new-path
clients found live; G>=2 = >=2 distinct zero-count forms among those found.

## 5. Traps for the build (anti-re-score)

1. `.github/agents` for both VS Code and Copilot CLI yields G=1; a second distinct form is required.
2. `.agents/agents` is held (18); do not use it (the `CtlC1RealNoForm` control did).
3. Claude Code cannot re-cite S026's URL (v1.1 URL key lowercases, drops scheme/`www.`/`.md`, folds
   slashes and query/fragment; v1.3 also rejects post-redirect base URLs).
4. Codex and Claude Code cannot contribute G even with a genuinely new, well-sourced statement.
5. The quote must sit on the live page with the path at a segment boundary, never inside a URL
   (v1.1 additions; `verifiers/check_agent_definitions.py:715-716`).
6. v1.2 conditions: SOURCES `kind` must be `docs`; URL not an issue/PR/discussion/commit page;
   normalised location under the client's own root (`:412-427`).
7. The nine agentdef box texts `SKILL.md:316-352` must stay byte-identical (session rule; hashes
   `checklist-baseline.json:97-149`).
8. SKILL.md is 598 of 600 lines at both base and work rev (`SKILL.md:300` carries the skill's own
   ≤600-line box) — the new heading + table must fit without touching the nine boxes.

## 6. Base SOURCES URL exclusion sets (new rows must be S072+)

71 base rows (S001–S071). Per client, base rows on the pinned hosts:
- Claude Code: S022, S026, S033, S043, S053, S065 (code.claude.com); S003, S019, S023
  (platform.claude.com); docs.claude.com: none.
- Codex: S035, S066 (developers.openai.com); S013, S021, S044, S054, S063 (learn.chatgpt.com).
- VS Code: S025, S034, S047, S055, S067 (code.visualstudio.com).
- Copilot CLI: S027, S028, S030, S031, S038, S048, S056, S068 (docs.github.com).
- Gemini CLI: S029, S036, S057 (geminicli.com).
- Cursor: S049, S052, S058, S070 (cursor.com).
- opencode: S024, S039, S045, S059, S064 (opencode.ai).
No base row cites any candidate agent-definition page (0 hits in SOURCES.md for `custom-agents`,
`codex/subagents`, `opencode.ai/docs/agents`, `about-agents`).

## 7. Unresolved / not checked

- Whether Codex, VS Code, Copilot CLI, Gemini CLI or Cursor documents an agent-definition directory
  at all, and which path: not answerable from base; the source seats' question. A negative needs the
  Q30 three-part sweep (changelog/release notes + docs source tree + lane corpus grep).
- Whether `.github/agents` is VS Code's documented workspace default or a compatibility path — the
  candidate pages were not fetched here.
- The actual F value depends on live pages; not checkable from base.
- No freshness claim made; C2 (withdrawn) is out of this report's scope.

## Evidence (commands and observed results)

All lane access read-only (`git --no-optional-locks`), cwd never the fleet root.

```
$ git -C <lane> --no-optional-locks grep -n -i -F <form> b0b7140b5a7cf8a50f13989ee6285fc8ee245c41 -- . ':!.ufo'
  .claude/agents            exit 0, 3 lines  (alwayson-rule-files-round53.md:25; verify_alwayson.py:22,77)
  .codex/agents             exit 0, 5 lines  (LOG.md:484; alwayson:82; census:98; remeasure:63,65)
  .opencode/agents          exit 0, 10 lines (checklist-baseline.json:100-148 ×9; remeasure:63)
  .opencode/agent           exit 0, 10 lines (same)
  .config/opencode/agents   exit 0, 24 lines
  .config/opencode/agent    exit 0, 25 lines (+ census:496)
  .agents/agents            exit 0, 18 lines (all .agents/AGENTS.md)
  .github/agents .vscode/agents .copilot/agents .gemini/agents .cursor/agents
  .github/agent  .vscode/agent  .copilot/agent  .gemini/agent  .cursor/agent   all exit 1 (0 hits)
$ git -C <lane> --no-optional-locks show b0b7140b:.ufo/waves/round-50/build/SrcClaudeSubagents.md
  exit 0, 15,224 B; :49 = Claude Code subagent location priority table
$ git -C <lane> --no-optional-locks show b0b7140b:corpus/SOURCES.md   # parsed: 71 rows, last id S071
$ git -C <lane> --no-optional-locks cat-file -e e02f5f5d:corpus/knowledge/agent-definition-files-round56.md   # exit 128
$ git -C <lane> --no-optional-locks cat-file -e e02f5f5d:corpus/lessons/round-56.md                            # exit 128
$ git -C <lane> --no-optional-locks show e02f5f5d:SKILL.md | wc -l                                              # 598
```

Reads: `verifiers/check_agent_definitions.py` (docstring `:1-90`; `BASE :120`; `git_grep_count
:222-231`; `OWN_ROOTS :412-427`; boundary check `:715-716`), `SKILL.md:300-352, 515-530`,
`corpus/SOURCES.md`, the three named knowledge entries, `corpus/README.md:13,19`, `LOG.md:26,73`,
`PROVINCE.md:50`, `corpus/lessons/round-4-aggregator-audit.md`, `round-6-aggregator-audit.md`,
`round-50.md`, `round-50-verifier-spotcheck.md`, `verifiers/checklist-baseline.json:95-152`.

Report: .ufo/waves/round-56/build/ScoutHeldAgentDefs.md
