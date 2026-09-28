---
name: kotoba-shokunin
description: >
  Prompt & skill craft — audits, writes, and rewrites SKILL.md / AGENTS.md /
  dispatch prompts / system prompts for trigger fidelity and decision density.
  Use when asked to improve an instruction file's trigger surface, write
  frontmatter descriptions, add decision
  tables, compress an overlong prompt, build an anti-pattern or error-pattern
  section, or check whether a skill's claims are verifiable. Triggers: "skill
  file", "SKILL.md", "frontmatter description", "trigger words", "prompt craft",
  "write a skill", "audit this skill", "skill quality". Anti-triggers: general
  prompt engineering for model outputs (not skill files), runtime code changes,
  and domain content inside a skill's reference/ tree — those belong to the
  owning domain skill, not this one.
---

# kotoba-shokunin — prompt & skill craft

A SKILL.md is a **loader contract**: the frontmatter `description` is the
only part the router always sees — and on this host it is not seen raw. The
`<skills>` catalogue (template embedded in the omp ELF, rendered per session)
is a *model-compressed* render capped ~95–103 chars/skill; the body is the
only part the executing agent always sees. Craft means both surfaces earn
their tokens. Rank: shonen.

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
| 4 | Procedures | Numbered steps, copy-pasteable command blocks | bailian-train-deploy steps 1–7 |
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
| AGENTS.md | Always-on: injected into every session in its repo | No frontmatter, no router — every byte loads every time | Token drag, stale constraint decay | Terse imperative rules only; no triggers, no prose, no procedures that belong in a skill |
| Command file (`opencode/command/*.md`) | Opt-in: user invokes `/<name>` | `description` + `agent:` frontmatter; body = command contract | Skill drift without a guardrail | Pointer-then-rules idiom: line 1 names the owning skill + `$ARGUMENTS`; then only the literal rules that must hold even if the skill drifts — procedures stay in the skill |
| Dispatch prompt — spawn (L1/L2 lanes) | Ephemeral: consumed once by a subagent | Whole file is the contract; no persistence | Missing stanza → unrecoverable agent (no conversation to clarify with) | Fixed 6-stanza order; complete, self-contained; ends with `| godspeed` |
| Dispatch prompt — round (`*-round-N.md`) | Ephemeral: re-ignites a live L1 lane | Relies on durable repo context (SKILL/LOG/corpus) | Stating stale per-round policy (routing maps drift between rounds) | 3–4 lines: role+round → method directive → land-scope+report → `| godspeed`; carry only what changed since spawn |
| CLAUDE.md | Conditional always-on: loader exists in both harness binaries (9/17 string refs) but injects only when the repo carries the file — cold on this host (0 captured injections) | Same as AGENTS.md: every byte loads when present | Same as AGENTS.md + dual-name collision | One owner per repo: redirect file (llama.cpp 1-liner → AGENTS.md) or pick one name; a 4339-line file is an unconditional session tax |

**AGENTS.md evidence:** six shokunin child repos carry byte-identical 5-line
operating rules (scope, LOG-evidence, no-fabrication) differing only in repo
name — `md5sum` differs, content shape identical
(`/home/vgpnk/projects/shokunin/*/AGENTS.md`, surveyed 2026-09-28). The
host-level `~/.agents/AGENTS.md` is longer but still pure constraints
(posture rules, bans, capability statements) — zero procedures, zero triggers.

**Agent-definition evidence:** 18 files under `~/.config/opencode/agents/`
(14–197 lines). Frontmatter keys beyond `name`/`description` are routing and
grant policy — `model`/`cascade`/`effort` (distiller, ufo), `permission_mode`/
`agents_md` (distiller), `whenToUse`/`subagents` (orch's delegation roster).
11 of 18 descriptions carry `NOT …` negative routing (round-6 audit
corrected the round-4 count of 7) — the delegation-table analogue of
anti-triggers. Posture text is copy-pasted: 14 files share one identical
9-line godspeed preamble (round-4 said 13; orch.md was missed), verified by
`md5sum` over the region; `mutation-tester.md` carries it **twice**
in-file — the observed cost of copy-paste zones in durable files.

**Command-file evidence:** 3 files under `~/.config/opencode/command/`
(10–13 lines). Two idioms: pointer-then-rules (sekhmet.md, xbrd.md — line 1
names the owning skill + `$ARGUMENTS`, then 3–4 rules that must hold even if
the skill drifts) and inline protocol (ufo.md — justified because no skill
owns orchestration). `agent: <name>` in frontmatter delegates to a named
roster agent (ufo.md → `agent: ufo`).

**Spawn dispatch-prompt anatomy** (from `.ufo/prompts/*-L1.md`, 9–12 lines each):
`role + working dir` → `context (domain + rank)` → `job (imperative, with
verification commands embedded)` → `L2 routing map` → `report path + scope
fence` → literal ` | godspeed` suffix. A stanza missing from a spawn dispatch
is permanently absent — the subagent cannot ask for it back. Budget the file
for completeness, not brevity; the reader is a blank-context agent. Round
prompts invert this: the reader re-loads its own repo, so the prompt carries
only the round number and method — observed template variance is exactly
`name` + `path` (`diff kake-round-4.md kasegi-round-4.md`).

Craft asymmetry to respect: SKILL.md optimizes *match precision* (trigger
density in the description); AGENTS.md optimizes *constraint survival* (a rule
that must hold unconditionally, so it must be short enough to always be read);
agent definitions optimize *delegation precision* (capability + exclusions an
orchestrator matches); spawn prompts optimize *one-shot completeness*
(everything the reader needs, nothing it can look up); round prompts optimize
*delta-only weight* (everything durable is already in the repo).

## Frontmatter craft — the trigger surface

`description` is an index, not a summary — and on this host it is an index
*through a compressor*: measured renders run ~95–103 chars vs 160–820 source
chars (10191 `Skill description compression failed` warns in `~/.omp/logs/`),
so the render is advisory, not verbatim. Field rules distilled from the survey:

1. **Capability first, triggers second.** One clause naming what the skill does
   ("xbreed ask — optional cross-model advisory protocol"), then trigger
   material.
2. **Quote literal trigger strings.** `Triggers: "sekhmet", "swarm", "L3", "fan
   out"` (sekhmet-l3); `"/wwkd", "plan this", "break this down"` (wwkd). Quoted
   strings match how routers and humans actually phrase intent.
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
   activation — the router never reads the body.
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
8. **Front-load match-critical text.** Because the router's input is a
   compressed render of `description`, put the capability clause and the most
   match-critical trigger material in the first ~95 chars; treat anything
   later as strengthener, not guarantee. Quoted trigger strings still help —
   they give the compressor salient tokens to keep — but measure placement,
   not presence.
9. **Invocation-shaped triggers for domain-term names.** When the skill's
   name is also a domain term (ufo, omarchy), a bare noun trigger cannot
   separate invocation from reference — measured 2026-09-28: all 5 literal
   `ufo` misses in opencode.db were domain mentions, not calls. Pair the
   noun with slash-form or imperative-context triggers.

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
   hold the whole file while editing it, the router can't either.

## Trigger-fidelity checklist

Run before shipping any SKILL.md. Every item is checkable by reading the file —
no runtime needed. (For AGENTS.md / dispatch prompts, use the per-surface rows
in "Instruction surfaces" instead — this checklist assumes a routed file.)

- [ ] `name` matches the directory / invocation surface.
- [ ] `description` contains ≥1 literal trigger string in quotes or an explicit
      `Triggers:` list.
- [ ] `description` contains at least one anti-trigger or exclusion clause.
- [ ] Overlapping sibling skills are named with an arbitration rule in the
      `description` (body/PROVINCE boundary text does not count — the router
      never reads it). N/A only when no named overlap exists.
- [ ] Body opens with a one-line role statement, not a restatement of triggers.
- [ ] Every prerequisite — any binary, file, env var, or sibling artifact a
      body command assumes, declared or implied — has a **fail-closed** path
      stated ("if X is missing, stop and do Y; do not guess" — bailian-cli
      pattern).
- [ ] Every decision-table row contains an action cell (see the table rule
      above — need not be the last column).
- [ ] Every command (fenced block or inline) is runnable as pasted: its binary
      resolves on PATH or at a location the file declares; bins are declared
      in metadata or checked in a prerequisite step.
- [ ] Every failure claim carries its observed signature (error text, exit code,
      version constraint) — no bare warnings.
- [ ] Every source citation resolves from a named base: repo-relative paths
      resolve from the file's own repo by default; any other root must be
      named in the file; bare basenames that exist under multiple roots fail.
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

## Anti-patterns

| Smell | Why it fails | Fix |
|-------|--------------|-----|
| Description = capability only, no triggers | Router can't match unseen phrasings — the shonen mint template produces exactly this (`Domain specialist — scopes X`); 5/5 sibling SKILL.md files failed items 2–3 in the round-5 fleet audit | Add quoted trigger strings + implicit intents |
| Anti-trigger only in body | Router never sees it; false activation | Move exclusion clause into `description` |
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
- `/home/vgpnk/projects/shokunin/.ufo/prompts/*-round-*.md` (6 files, 3–4
  lines) — round self-iteration mode; template variance is name+path only.
- `~/.config/opencode/agents/*.md` (18 files, 14–197 lines) — agent-definition
  surface: roster frontmatter (`subagents`, `cascade`, `permission_mode`),
  negative routing (`NOT …` family in 11/18 — round-6 audit corrected
  round-4's 7), shared godspeed preamble in 14/18 (doubled in
  mutation-tester.md), stale dated `cascade_note` and missing `name:` key
  in ufo.md, `aaron` bin declared-but-absent in scout.md.
- `~/.config/opencode/command/*.md` (3 files, 10–13 lines) — command surface:
  pointer-then-rules idiom, `agent:` delegation key, `$ARGUMENTS`.
- CLAUDE.md files: `find ~ -maxdepth 6` → 16 hits (5 operator-authored, 1
  dispatch template, 10 vendored/cache); loader strings in both harness
  binaries but 0 captured injections — seventh surface class, cold channel.
- `~/.local/share/opencode/opencode.db` — literal-trigger miss proxy over 398
  sessions / 415 skill calls: unique-token triggers 0 misses; godspeed
  always-on coverage 51.5%; domain-term names ambiguous (`ufo` misses are
  references, not invocations).
