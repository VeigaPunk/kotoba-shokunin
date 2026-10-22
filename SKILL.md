---
name: kotoba-shokunin
description: >
  Prompt & skill craft — audits, writes, and rewrites SKILL.md / AGENTS.md /
  dispatch prompts / system prompts for trigger fidelity and decision density.
  Triggers: "skill file", "SKILL.md", "frontmatter description", "trigger
  words", "prompt craft", "write a skill", "audit this skill", "skill quality".
  Anti-triggers: general prompt engineering for model outputs (not skill
  files), runtime code changes, and domain content inside a skill's
  reference/ tree. Sibling boundary: the five `*-shokunin` domain skills
  (kagi, kake, kasegi, kengaku, kumitate) own their own SKILL.md content —
  this skill audits and reports; fixes route to the owning lane. Note: the
  shokunin files are not in an omp skill discovery root, so their descriptions
  never reach the omp skills router — craft here is audit-side, not
  router-visible.
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

## Skill-file anatomy

Observed load order, top to bottom. A file that inverts this order (procedures
before scope, examples before decision tables) reads worse under activation
pressure.

| # | Section | Function | Exemplar |
|---|---------|----------|----------|
| 0 | Frontmatter | Trigger index; the only always-loaded bytes | all |
| 1 | H1 + role statement | What this skill is, in one line | wwkd L16–24 |
| 2 | Prerequisite gate | Fail-closed dependency check before any action | bailian-cli "CRITICAL — MUST read bailian-protocol" |
| 3 | Decision surface | Tables/protocols that route the request | bailian-protocol class table; sekhmet-l3 flag table |
| 4 | Procedures | Numbered steps, copy-pasteable command blocks | bailian-finetune steps 1–7 |
| 5 | Boundaries | Refusals, anti-triggers, hand-offs | wwkd "Refusals"; bailian-train-deploy 反触发表 |
| 6 | References | Cited sources, relative links to depth files | wwkd "Source Excerpts"; bailian `reference/` links |

Not every file needs every section. godspeed is 18 lines: frontmatter + one
deferral ("Read `directive.md` … apply verbatim") + one invocation note. Anatomy
is a checklist of *available* organs, not a mandatory skeleton.

## Instruction surfaces — pick the file before the fix

The nine-class surface table with its evidence paragraphs moved verbatim to
`corpus/knowledge/instruction-surface-census-round13.md` § SKILL.md instruction-surfaces
table (round 22; sha256 `e046a0252cc96f17…` pinned there). The machine check is unchanged:
`verifiers/verify_surfaces.py` (7 checks) reads that same census file. The table's
"All craft below" cell refers to this file's craft sections below — kept verbatim.

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
`dispatch.08`, executed by `verifiers/verify_dispatch_prompts.py` (its
`--box-proof` prints `boxes proven 2` only when both boxes are delegated there
and its committed fixtures discriminate every conjunct). Limits and ceilings: `corpus/knowledge/checklist-execution-round17.md`.

## Frontmatter craft — the trigger surface

`description` is an index, not a summary. On **omp** the router ingests it
through a **cache-or-truncate** render (mechanism proven from the omp binary,
`corpus/knowledge/render-mechanism-round7.md`): a
`sha256(prompt ‖ 0x00 ‖ name ‖ 0x00 ‖ loader-held description)` hit in
`~/.omp/agent/skill-descriptions.db` renders that cache line; a miss keeps at
most 99 chars. The cache key includes the description, so **editing a
`description` invalidates its row and reverts the skill to the truncator** until
the compressor rewrites it. On **opencode** the full description reaches the
model untruncated; trigger strings and anti-triggers are mandatory on both
because the offer gate and the model's own matching both read the description.

Twelve rules with the measurements behind each — capability clause first, quote
literal *and* implicit-need triggers, co-locate anti-triggers (body-only
exclusions cannot prevent activation), name the overlapping sibling and its
arbitration rule, the 99-char cliff and its 55–96 effective keep, the ≥40-char
first-sentence branch that discards sentence 2+, the CJK `[.!?]`-only sentence
regex, `metadata.requires` over prose, render-by-reproduction, invocation-shaped
triggers for domain-term names, and the discovery roots:
`corpus/knowledge/frontmatter-trigger-surface.md` § Craft rules.

Portability floor (spec + vendor + YAML, `corpus/SOURCES.md` S018, S002, S019, S008): `name` ≤64 lowercase letters, digits and single hyphens, equal to the directory (the spec's charset wording is ambiguous on Unicode); `description` ≤1024 chars, no XML tags (Anthropic rule), quoted when it holds `: ` or ` #` (illegal in a YAML plain scalar — lenient loaders hide it, strict ones reject). `verifiers/verify_skill_checklist.py` `trigger.no_xml_tag` approximates the XML-tag rule lexically on the unparsed `name`/`description` text; Anthropic's packager (S012) refuses any `<`/`>` in the parsed value, so the two disagree in both directions. Which authority imposes which rule, with run counterexamples: `corpus/knowledge/frontmatter-rule-authorities-round48.md`.

## Decision tables — when to use one

| Situation | Table? | Evidence |
|-----------|--------|----------|
| Intent → command/route mapping | Yes: `Intent | Command | Notes` | bailian-cli "When to use which command" |
| Request classification with different actions | Yes: `Class | Pattern | Action` | bailian-protocol 4-class consent table |
| Flag → effect reference | Yes: `Flag | Effect` | sekhmet-l3 |
| Ordered pipeline | No — numbered steps or ASCII chain | bailian-finetune 7-step chain |
| One conditional | No — one sentence | — |

Table rule: every row must contain an **action cell** (command, route, named
fallback, or verdict) — it need not be the last column; a trailing
Source/Evidence column is allowed only when an action cell exists earlier in
the row. A table with no action column at all is documentation, not a
decision surface, and must not be presented as one.

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
form: `/home/vgpnk/projects/shokunin/.ufo/prompts/`). Checkable by reading the file; round-7 application +
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

Run before editing any always-loaded rules file. Observed evidence +
application matrix (6/6 repo files pass; the 75-line host `~/.agents/AGENTS.md`
fails procedures/dates/style) in `corpus/knowledge/alwayson-checklist-round7.md`.

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

## Refusals

- Won't fabricate domain content: claims need a file, a command output, or a
  cited source (repo AGENTS.md rule).
- Won't audit the *content* of another skill's `reference/` tree — that's the
  owning domain's province. Report cross-domain evidence back, don't absorb it.
- Won't produce a description without anti-triggers, or a body without a
  fail-closed path for its prerequisites.

## Sources

- `corpus/SOURCES.md` — where this lane learns: opened, scope-tiered source rows,
  study paths and search log; admission bar in `corpus/QUALITY.md`.
- `~/.agents/skills/wwkd/SKILL.md` — posture-skill anatomy: principles, phased
  protocol, refusals, quoted source excerpts.
- `~/.agents/skills/godspeed/SKILL.md` — minimal always-on skill (18 lines);
  deferral pattern.
- `~/.agents/skills/sekhmet-l3/SKILL.md` — ops-skill anatomy: env blocks, smoke
  gate, flag table.
- `~/.agents/skills/xbrd-ask/SKILL.md` — lane table, advisory protocol, epistemic
  constraints.
- `~/.agents/skills/bailian-protocol/SKILL.md` — consent decision table,
  classification with actions.
- `~/.agents/skills/bailian-cli/SKILL.md` — hub/routing tables, soft hand-offs,
  `metadata.requires.bins`.
- `~/.agents/skills/bailian-train-deploy/SKILL.md` — 反触发表, 反幻觉清单,
  numbered end-to-end procedure, failure signatures.
- `~/.agents/skills/bailian-model-recommend/SKILL.md` — implicit-intent triggers,
  sibling boundary arbitration.
- `~/.agents/skills/bailian-web-search/SKILL.md`, `bailian-gen/SKILL.md`,
  `bailian-finetune/SKILL.md` — routing workflows, consent short-forms.
- `~/.agents/skills/bailian-docs-llm-wiki/SKILL.md` — layered depth trees
  (wiki/models/raw), quality-score fallback, grep/jq query recipes.
- `~/.agents/skills/bailian-managed-agent/SKILL.md` — plan-before-apply
  guardrail, secrets-never-in-preview rules.
- `~/.agents/skills/bailian-sandbox/SKILL.md` — operational-boundary section,
  credential-redaction defaults.
- `~/.agents/skills/omarchy/SKILL.md` — largest observed file (392 lines);
  safety-rule callouts, config-location tables.
- `~/.config/opencode/skills/ufo/SKILL.md` — invariant lists (I1–I10), load-order
  with fail-closed resolution, dispatch contract.
- `/home/vgpnk/projects/shokunin/*/AGENTS.md` (6 files) + `~/.agents/AGENTS.md`
  — always-on constraint files; no frontmatter, terse imperatives.
- `/home/vgpnk/projects/shokunin/.ufo/prompts/*-L1.md` (8 files, 9–12 lines) —
  spawn dispatch-prompt stanza order and `| godspeed` terminator.
- `/home/vgpnk/projects/shokunin/.ufo/prompts/*-round-*.md` (50 files, 3–11
  lines at round-9 recount; round-7 audit: 30 restate the L2 map with stale
  aliases) — round
  self-iteration mode; template variance is name+path only.
- `~/.config/opencode/agents/*.md` (18 files, 14–197 lines) — agent-definition
  surface: roster frontmatter (`subagents`, `cascade`, `permission_mode`),
  negative routing (`NOT …` family in 11/18 — round-6 audit corrected
  round-4's 7), shared godspeed preamble in 14/18 (doubled in
  mutation-tester.md), stale dated `cascade_note` and missing `name:` key
  in ufo.md, `aaron` bin declared-but-absent in scout.md.
- `~/.config/opencode/command/*.md` (3 files, 10–13 lines) — command surface:
  pointer-then-rules idiom, `agent:` delegation key, `$ARGUMENTS`.
- CLAUDE.md files: `find ~ -maxdepth 6 -iname 'claude.md' -not -path
  '*/node_modules/*'` → 18 hits at round-7 recount (5 operator-authored, 1
  dispatch template, 12 vendored/cache); loader strings in both harness
  binaries (9 opencode / 17 omp) but 0 captured injections — seventh surface
  class, cold channel.
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
- `verifiers/verify_harness_claims.py` + `verifiers/baseline.json` — the round-10
  executable form of the harness claim set (28 checks, 4 exit codes, `--self-test`);
  the authority for every harness number in this file.
- `verifiers/check_substrate_pins.py` — round 23: enforces the
  `verifiers/baseline.json` `measured_against` pins (omp sha256 + ns-exact mtime,
  opencode sha256; exit 0/1/2/3, '--self-test' builds inline tempdir fixtures (the committed `verifiers/fixtures/pins/` is evidence-only — round 28);
  hashes bytes, never execs; a red guard is fixed by re-record + mechanism note,
  never by weakening the pin).
- `verifiers/verify_corpus_integrity.py` + `verifiers/corpus-baseline.json` — the
  round-11 executable form of the *corpus-internal* citation rules (9 checks over
  tracked `corpus/*.md`: index coverage, lane-report pointers in all four shapes,
  `commit` citations resolve, no non-hash commit token; exit 0/1/2/3, `--self-test`).
  This file's own citations and root `LOG.md`/`SCORECARD.md` citations are instead
  executed by `trigger.citation_resolves` / `governance.citation_resolves` in `verify_skill_checklist.py`.
  Run it before shipping an artifact set; a dead pointer is then a drift report, not a reviewer's memory.
- `corpus/knowledge/corpus-integrity-round11.md` — what the corpus verifier checks,
  the three counting recipes it replaced (why each could not express its class),
  the exclusion shapes it must not report, and the check that was designed and
  rejected (revision pins: digests are not commits).
- `corpus/knowledge/cold-run-round11.md` — the non-author cold run of the corpus
  verifier (runner, tree, command, exit code, spot-checks); the evidence class
  this repo uses when a check must not be its author's only witness.
- `verifiers/verify_corpus_independent.py` +
  `corpus/knowledge/independent-verification-round12.md` — the **second**
  witness, and the right shape for one: a derivation written from the class
  spec by a lane that did not author `verify_corpus_integrity.py` (and did not
  read it), compared check-for-check on two trees (green live, red on a clone at
  `d49dfa5` with the same ten dead-pointer sites). A re-run of the author's
  script is not a second witness — it launders a broken model; the comparison's
  own artefacts this round were two claim/behaviour gaps in the author's script
  (a documented quoted-context rule that could never fire; an index census that
  read more of `README.md` than it claimed) and one shared property (pointer
  resolution is host-anchored, so a clone's green verdict is not hermetic).
- `verifiers/fault_injection_corpus.sh` — the planted-fault harness, in-repo so
  the "the checks fire" claim stops depending on `/tmp` scratch; plants one
  fault per clone and asserts the *class* that must fire, plus a must-not-fire
  equivalent mutation. **Mutating — not a smoke check** (round-8 box-3 cold run,
  break point B2): the default path `git clone --no-hardlinks`s this repo once
  per fault class into `${TMPDIR:-/tmp}/round12-faults.$$` and `rm -rf`s each
  world, so it runs deliberately, never as an "is everything still fine" probe;
  `--self-test` exercises the assertion machinery on fixture worlds without
  cloning the repo (it still creates, and on exit removes, one `${TMPDIR}`
  scratch dir).
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
