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
  never reach the `<skills>` router — craft here is audit-side, not
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
rows at round 7, 17 rows at round 9 (**all 17 keys reproduced** against today's
on-disk descriptions; `select count(*)` → 17, 2026-09-28) — and rows land
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

Seven surface classes observed on this host; each loads differently, so each
has different craft rules. Applying skill-file rules to an always-loaded file
(or vice versa) is the most common cross-surface mistake.

| Surface | Load condition | Parse surface | Dominant failure | Craft rule |
|---------|----------------|---------------|------------------|------------|
| SKILL.md | Opt-in: activated when `description` matches intent | frontmatter = router index; body = executor contract | False activation / missed activation | All craft below (frontmatter, tables, gates) |
| Agent definition (`opencode/agents/*.md`) | Roster: orchestrator picks by `description`, then body becomes the subagent's system prompt | `description` = delegation index; body = persistent identity | Wrong-lane delegation; stale routing metadata | Terse negative routing in description (`NOT general-purpose. NOT explore.`); identity + constraints in body, never a per-task job; dated operational notes belong in status files, not frontmatter |
| AGENTS.md | Always-on: injected into every session in its repo | No frontmatter, no router — every byte loads on each injection (loader strings exist in both binaries; 0 captured injections on this host) | Token drag, stale constraint decay | Terse imperative rules only; no triggers, no prose, no procedures that belong in a skill |
| Command file (`opencode/command/*.md`) | Opt-in: user invokes `/<name>` | `description` + `agent:` frontmatter; body = command contract | Skill drift without a guardrail | Pointer-then-rules idiom: line 1 names the owning skill + `$ARGUMENTS`; then only the literal rules that must hold even if the skill drifts — procedures stay in the skill |
| Dispatch prompt — spawn (L1/L2 lanes) | Ephemeral: consumed once by a subagent | Whole file is the contract; no persistence | Missing stanza → unrecoverable agent (no conversation to clarify with) | Fixed 6-stanza order; complete, self-contained; ends with `| godspeed` |
| Dispatch prompt — round (`*-round-N.md`) | Ephemeral: re-ignites a live L1 lane | Relies on durable repo context (SKILL/LOG/corpus) | Stating stale per-round policy (routing maps drift between rounds) | 3–4 lines: role+round → method directive → land-scope+report → `| godspeed`; carry only what changed since spawn |
| CLAUDE.md | Conditional always-on: loader exists in both harness binaries (9/17 string refs) but injects only when the repo carries the file — cold on this host (0 captured injections) | Same as AGENTS.md: every byte loads when present | Same as AGENTS.md + dual-name collision | One owner per repo: redirect file (llama.cpp 1-liner → AGENTS.md) or pick one name; a 4339-line file is an unconditional session tax |

**AGENTS.md evidence:** six shokunin child repos carry shape-identical 5-line
operating rules (scope, LOG-evidence, no-fabrication) — identical shared body
under a per-repo first line (`md5sum` differs across the six; hashing lines
2+ gives one hash — `/home/vgpnk/projects/shokunin/*/AGENTS.md`, re-verified
round 7). The host-level `~/.agents/AGENTS.md` (75 lines) is NOT pure
constraints: it carries procedures (`Load and obey
~/.agents/godspeed-core/directive.md` at :18, `the-janitor tac-check` at :55)
and dated attestations (:48,:51) — a mixed surface, flagged by the round-7
AGENTS.md checklist audit (`corpus/knowledge/alwayson-checklist-round7.md`).

**Agent-definition evidence:** 18 files under `~/.config/opencode/agents/`
(14–197 lines). Frontmatter keys beyond `name`/`description` are routing and
grant policy — `model`/`cascade`/`effort` (distiller, ufo), `permission_mode`/
`agents_md` (distiller), `whenToUse`/`subagents` (orch's delegation roster).
11 of 18 descriptions carry `NOT …` negative routing (round-6 audit,
`corpus/knowledge/agent-def-audit-round6.md`, corrected the round-4 count of
7) — the delegation-table analogue of anti-triggers. Posture text is
copy-pasted: 14 files share one identical 9-line godspeed preamble
(round-4 said 13; orch.md was missed), verified by `md5sum` over the region
and re-verified round 7 (shared md5 `c91c0d66…`, still 14/18);
`mutation-tester.md` carries it **twice** in-file — the observed cost of
copy-paste zones in durable files.

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

## Router model — which harness, which gate

Two harnesses consume skills here, and neither shares the other's catalogue
tag, render, or offer gate. Read the harness's own artifacts before predicting
a render — a rule proven on omp is wrong on opencode.

| Harness | Catalogue tag | Description render | Offer gate (action) | Failure mode |
|---------|---------------|--------------------|---------------------|--------------|
| omp | `<skills>` (ELF template) | `cache.get(key) ?? previewSkillDescription` — cached LLM line, else deterministic truncator (`_8n=100`; first sentence if ≥40 chars, else last-space cut + `…`); hard 99-char cliff | Ship the dir under an omp discovery root (`.agents/skills`, `.claude/skills`, project walk-up) and front-load the capability + WHEN into the first ≤99 chars | Trigger material past offset 99 or in sentence 2 renders as nothing (all 13 observed `Triggers:`/反触发/`Excludes` clauses lost) |
| opencode | `<available_skills>` (`fmt(list,{verbose:true})`) | Full `description` byte-for-byte + `<location>` in the system-prompt catalogue; no truncation, no cache (the TUI skill list collapses whitespace only) | Define `description` and a frontmatter `name:`; leave the `skill` permission enabled; if a same-name duplicate exists, do not rely on which copy wins | Missing `description` is filtered out of the catalogue; a denied `skill` permission omits the whole block; duplicate names are last-parsed-wins under unbounded parse concurrency (round-9 re-verify: first-scanned-wins was wrong) |

Check before predicting: on omp read the cache db
(`sqlite3 -readonly ~/.omp/agent/skill-descriptions.db "select count(*) from
skill_descriptions;"`) **and** the newest `<skills>` block
(`~/.omp/agent/sessions/**/*.jsonl`) — the catalogue freezes at session start,
so db coverage is time-varying; on opencode read the global roots and
`grep -o 'message=init count=[0-9]*' ~/.local/share/opencode/log/opencode.log`.

## Frontmatter craft — the trigger surface

`description` is an index, not a summary. On **omp** the router ingests it
through a **cache-or-truncate** render (mechanism proven from the omp binary,
`corpus/knowledge/render-mechanism-round7.md`): if a `sha256(prompt + name +
ws-collapsed description)` row exists in `~/.omp/agent/skill-descriptions.db`
the render is that LLM one-liner (≤160 chars, ≤12 words); otherwise a
deterministic truncator keeps at most 99 chars — first sentence wins if ≥40
chars, else last-space cut + `…`. Measured over the live 17-skill omp
catalogue: only 17.7% of source description chars reach the router, 53/62
quoted trigger spans are lost, and all 13 `Triggers:`/反触发/`Excludes`/`不用于`
clause markers sit past the cliff — none render (round-7 measurement; round 9
adds the drift: cache coverage 5/17 → 17/17 rows, so the truncator is now the
fallback, not the default — a session started before a row landed still shows
the truncation). On **opencode** the full `description` reaches the model
untruncated, so front-loading there is style, not survival; trigger strings and
anti-triggers stay mandatory on both, because the offer gate and the model's own
matching both read the description. Field rules distilled from the survey and
this measurement:

1. **Capability first, triggers second.** One clause naming what the skill does
   ("xbreed ask — optional cross-model advisory protocol"), then trigger
   material.
2. **Quote literal trigger strings.** `Triggers: "sekhmet", "swarm", "L3", "fan
   out"` (sekhmet-l3); `"/wwkd", "plan this", "break this down"` (wwkd). Quoted
   strings match how routers and humans actually phrase intent (design
   guidance — no matcher-level measurement exists for either harness).
3. **Include implicit-intent triggers.** bailian-model-recommend activates on
   `"做一个XX"` in its frontmatter 触发词 (the fuller `"我想做一个XX"` sits in
   its body 适用场景). If users arrive without naming the skill, the
   description must catch the *need*, not the name.
4. **Co-locate anti-triggers.** Most surveyed files carry exclusions in the
   description itself: omarchy "Excludes Omarchy source development",
   bailian-gen "反触发：普通问答、编程、写作、翻译不走本技能". Observed
   exceptions (2 of 10 bailian files): bailian-train-deploy and
   bailian-docs-llm-wiki keep exclusion lists only in the body (反触发表 /
   何时不要使用) — a second-layer net for router error, not a substitute:
   an anti-trigger in the body but not the frontmatter still causes false
   activation — the catalogue is built from frontmatter only (see § Router model).
5. **State sibling boundaries when overlap exists.** bailian-model-recommend:
   "当用户同时涉及模型查询和模型选择时，优先使用本 skill". Naming the neighbor
   and the arbitration rule prevents double-activation.
6. **Always-on skills say so explicitly.** godspeed: "Use on every prompt …
   without waiting for a keyword." If activation is unconditional, the
   description must override the trigger assumption, not rely on it.
7. **Declare runtime needs in metadata, not prose.** `metadata.requires.bins:
   ["bl"]` on 7 of 10 bailian skills (docs-llm-wiki, model-recommend and
   train-deploy omit `requires:`), `compatibility:` on model-recommend.
   Machines read metadata; prose warnings get skipped.
8. **On omp the 99-char cliff is absolute — write for the truncator, not the
   compressor.** Anything past ws-collapsed offset 99 is invisible whenever the
   cache misses: 0 chars survive in all 14 measured truncations; effective keep
   is 55–96 (last-space back-off). Put the capability clause + the most
   match-critical WHEN material in the first ≤99 chars; everything later is
   only reachable if the async LLM cache has landed *for this session's
   catalogue* — coverage is time-varying (5/17 rows at round 7; 17 rows at round
   9, all 17 keys reproduced against today's on-disk descriptions) and the cache
   key includes the description, so **editing a `description` invalidates its row
   and reverts that skill to the truncator** until the compressor writes a new
   one. The cache path also rewrites, so late text may return paraphrased, not
   verbatim. opencode has no cliff: its system-prompt catalogue renders the full
   description. CJK
   edge (omp only): the sentence regex knows only `[.!?]`, so 。；： don't count
   and CJK text cuts mid-clause at an incidental ASCII space (549→44 observed).
9. **Exploit the omp first-sentence branch.** If the first `.`/`!`/`?` sentence
   is ≥40 chars it renders whole with NO ellipsis — a clean complete hint
   (godspeed does this: keeps "Use on every prompt…" verbatim). But the same
   branch *discards* sentence 2+: godspeed's own trigger list sits in its
   second sentence and is gone. Put trigger material inside sentence 1 or
   accept the loss.
10. **Verify the render by reproduction, not assumption.** H7s is ~10 lines —
    re-run it (recipe in `corpus/knowledge/render-mechanism-round7.md`) or
    grep the newest `<skills>` block in `~/.omp/agent/sessions/**/*.jsonl`.
    The catalogue is frozen per session at render time and two variants can
    coexist same-hour, so today's render is evidence, not a spec.
11. **Invocation-shaped triggers for domain-term names.** When the skill's
    name is also a domain term (ufo, omarchy), a bare noun trigger cannot
    separate invocation from reference — measured 2026-09-28: all 5 literal
    `ufo` misses in opencode.db were domain mentions, not calls. Pair the
    noun with slash-form or imperative-context triggers.
12. **Skill files outside a discovery root never route.** omp loads
    `.agent/skills` + `.agents/skills` (project walk-up + user home),
    `.claude/skills`, marketplace cache. A SKILL.md at a bare repo root (the
    six `*-shokunin` files) is never offered — for those, `description` craft
    is audit-hygiene, not routing surface; check the discovery root before
    predicting router behavior.

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

1. **Spend tokens in the description; save tokens in the body.** The description
   is always loaded — density there has the highest leverage. The body loads only
   on activation, but still competes with the task context.
2. **Depth moves to files, not prose.** Hub skills point to `reference/<group>.md`
   and `bl <cmd> --help` instead of duplicating flag docs ("do not guess flags" —
   bailian-cli). One authoritative home per fact; the skill keeps the pointer.
3. **Command blocks verbatim-copyable.** Env setup first, then the command
   (sekhmet-l3 live-wave block). No placeholders that require guessing the shape.
4. **Failure signatures inline.** Pitfalls earn their lines only when they carry
   the observed symptom: zsh `status` readonly-variable trap, 404 deploy
   propagation delay, `--learning-rate` must be string `"3e-4"` not number
   (bailian-train-deploy 反幻觉清单). "Be careful" without a signature is noise.
5. **Never restate the trigger in the body.** The body assumes activation
   succeeded; "when to use this skill" paragraphs in the body are dead weight —
   move them to the description.
6. **~600-line module bound.** wwkd principle 8: fits in one file, one screen,
   single-sitting readable. Largest observed production skill: omarchy at 392
   lines. Past ~600 lines, split: decision surface stays in SKILL.md, depth goes
   to `reference/` / `assets/` with a pointer line. Gods-eye rule: if you can't
   hold the whole file while editing it, the reader can't either (heuristic, not
   measured).

## Trigger-fidelity checklist

Run before shipping any SKILL.md. Every item is checkable by reading the file —
no runtime needed. (For AGENTS.md / dispatch prompts, use the per-surface rows
in "Instruction surfaces" instead — this checklist assumes a routed file.)

- [ ] `name` matches the directory / invocation surface.
- [ ] `description` contains ≥1 literal trigger string in quotes or an explicit
      `Triggers:` list.
- [ ] `description` contains at least one anti-trigger or exclusion clause.
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
- [ ] Every failure claim — any warning, dominant-failure label, or causal
      "X breaks because Y" assertion — carries its observed signature (error
      text, exit code, version constraint) **or** is explicitly framed as
      design guidance, not an observed failure. No bare warnings.
- [ ] Every source citation resolves from a named base: repo-relative paths
      resolve from the file's own repo by default; any other root must be
      named in the file (`~/.config/opencode/opencode.json`, not bare
      `opencode.json`); bare basenames that exist under multiple roots fail.
- [ ] Stale-risk facts (model names, versions, prices) are either pinned with a
      source or deferred to `--help` / reference files.
- [ ] File ≤ ~600 lines; overflow already moved to referenced depth files.
- [ ] No `TODO`, placeholder sections, or "coming soon" — a skill ships complete
      or names the missing prerequisite.

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
form: `.ufo/prompts/`). Checkable by reading the file; round-7 application +
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
      dir, and ≤ the lane's `.ufo/state/<id>.round` (which holds the lane's
      *latest* round — equality against a sibling's state is wrong).
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

| Smell | Why it fails | Fix |
|-------|--------------|-----|
| Description = capability only, no triggers | Router can't match unseen phrasings — the shonen mint template produces exactly this (`Domain specialist — scopes X`); 5/5 sibling SKILL.md files failed items 2–3 in the round-5 fleet audit | Add quoted trigger strings + implicit intents |
| Anti-trigger only in body | The offer stage never sees it (frontmatter-only catalogue); false activation | Move exclusion clause into `description` |
| Flags documented in prose | Drifts from `--help`; agents guess | Pointer to `reference/` or `--help` |
| Procedures before scope | Agent acts before knowing boundaries | Anatomy order: gate → decide → act |
| Warning without signature | "Be careful" teaches nothing | Attach observed error text / version / exit code |
| Sibling skill hardcoded as path dep | Missing sibling = dead skill | Soft hand-off by name + `--help` fallback (bailian family rule) |
| Recursive skill load | Skill that must read itself to work | In-line the essential rule; reference the rest |
| 600+ line monolith | Router and agent both lose the thread | Split at anatomy boundary 3↔4 |
| Procedures in AGENTS.md | Always-loaded bytes pay every session; procedures belong in opt-in files | Move how-to to SKILL.md; keep only constraints |
| Dispatch prompt missing a stanza | Blank-context subagent fails unrecoverably | Role → context → job → routing → report → `| godspeed` |
| Copy-pasted posture block in durable files | One drifts silently — 13 copies observed, one file already carries it twice | Centralize: `agent:`/`agents_md:` frontmatter flags or a shared include |
| Per-task job text in an agent-definition body | Body loads for every delegation; the job goes stale while the identity persists | Identity + constraints in body; the job lives in the dispatch prompt |
| Dated operational note in frontmatter | No freshness mechanism — `cascade_note` past its `until` date still routes | Move dated facts to a status file; frontmatter holds stable policy |
| Command file that re-states skill procedures | Two owners of the same steps; the skill drifts, command contradicts | Pointer-then-rules: name the skill, keep only rules that must hold anyway |
| Spawn-mode prompt used for a round ignite | 6-stanza completeness when the reader re-loads its own repo is pure drag | 3–4 lines: role+round, method, land-scope, `| godspeed` |
| Bin invoked without declared location | `command -v` returns nothing; agent guesses a path (kake: `webzites` on no PATH) | Declare the bin path or a prerequisite check step |
| Trigger list past the omp 99-char cliff | omp's render is `cache.get(key) ?? slice(0,99)`+`…`: all 13 observed `Triggers:`/反触发/`Excludes` clauses sit past the cut and never reach the router when the cache misses (85.5% of quoted trigger spans lost); the cliff is omp-only — opencode's system-prompt catalogue renders the full description | Capability + WHEN-hint inside the first ≤99 chars; the rest is body material on omp; on opencode nothing is cut, so trigger order is not survival-critical |
| Trigger list in sentence 2 (omp) | omp's ≥40-char first-sentence branch renders sentence 1 verbatim and drops everything after — godspeed loses its own trigger list this way; opencode renders every sentence | Put trigger material inside sentence 1, or keep the description to one sentence |
| CJK description with incidental ASCII spaces (omp) | omp's sentence regex knows only `[.!?]`; CJK text cuts at an incidental space mid-clause (549→44 chars observed) | CJK skills must front-load harder; expect sub-90-char keeps |
| Copy-pasted round prompt restating durable policy | The routing map in a round prompt drifts with every bucket change — 38 files carry `m_composer`/`m_antigravity`/`m_grok` aliases retired by MISSION.md | Round prompt carries delta only; durable policy lives where the lane re-reads it (MISSION.md) |

## Refusals

- Won't fabricate domain content: claims need a file, a command output, or a
  cited source (repo AGENTS.md rule).
- Won't audit the *content* of another skill's `reference/` tree — that's the
  owning domain's province. Report cross-domain evidence back, don't absorb it.
- Won't produce a description without anti-triggers, or a body without a
  fail-closed path for its prerequisites.

## Sources

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
- `~/.opencode/bin/opencode` + upstream `github.com/sst/opencode` (dev):
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
  compressor template (`Compress into one routing hint …`) — the description is
  hashed as the YAML loader yields it (`>` keeps a trailing newline, `>-`
  strips it), so a ws-strip-only check under-reports coverage; cache
  `~/.omp/agent/skill-descriptions.db` (17 rows at round 9, up from 5; all 17
  keys reproduce, newest catalogue 17/17 cache, 0 truncations).
- `corpus/knowledge/harness-router-models-round9.md` — the two-harness router
  model (tag, render, offer gate, failure mode, verify recipe) with the
  round-9 key-reproduction and freeze evidence.
- `corpus/knowledge/claim-scope-audit-round9.md` — the round-9 consistency
  measurement: harness-claim scope before (31 claim units, 9 UNSCOPED) and after.
- `corpus/knowledge/render-mechanism-round7.md` — mechanism + survival
  measurement: cliff = offset 99, keep 55–96; the char-survival figure (17.7% of
  description chars reaching the router) is logged in `LOG.md` round 7 and
  `../.ufo/reports/round-7/kotoba.md`, not in the artifact. Loss figures
  (53/62 quoted spans, 13/13 `Triggers:` clauses) describe the cache-miss
  truncation path only.
- `corpus/knowledge/dispatch-prompt-audit-round7.md` — 12-item dispatch
  checklist + 43-file application (37 fail ≥1 item) + resolvability sweep
  (dead `~/wikillm` path, dead `~/.xbgst` env file, generator contract bugs).
- `corpus/knowledge/alwayson-checklist-round7.md` — 8-item AGENTS.md
  checklist + application (host file FAIL), self-audit results (4 fails
  cured), sentinel re-verify (all cross-domain defects persist).
