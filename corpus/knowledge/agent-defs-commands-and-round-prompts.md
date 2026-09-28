# Agent definitions, slash commands & round-N dispatch prompts

Sourced 2026-09-28. Extends `agents-md-and-dispatch-surfaces.md`: the host has
two more instruction surfaces (agent-definition files, command files) and a
second dispatch-prompt mode (round-N self-iteration). All evidence local.

## Fact — agent-definition files have a two-zone structure

18 files at `/home/vgpnk/.config/opencode/agents/*.md` (14–197 lines).
Zone 1 = frontmatter, zone 2 = a system prompt loaded for every task the
agent receives.

Frontmatter keys observed (per-file subsets):

| Key | Seen in | Function |
|-----|---------|----------|
| `name`, `description` | 17/18 (ufo.md has description only) | Roster index — how the orchestrator picks the delegate |
| `model`, `cascade`, `cascade_class`, `effort`, `variant` | distiller, ufo | Routing/cost policy |
| `permission_mode`, `agents_md`, `prompt_mode`, `mode`, `steps`, `permission` | distiller, janitor, ufo | Capability/scope grants |
| `whenToUse`, `subagents` | orch only | Orchestrator's delegation roster |

`description` carries capability + negative routing: 11 of 18 files carry
`NOT …` exclusion cues (round-6 audit corrected this round-4 count of 7 —
connector, critic, distiller, executor, labrat, mutation-tester, reviewer,
scout, scribe, sentinel, simplifier) — a terse exclusion convention, the
delegation-table analogue of a skill's anti-triggers.

## Fact — posture text is copy-pasted, and one file carries it twice

14 of 18 files embed the identical 9-line block (round-6 audit corrected
this round-4 count of 13 — orch.md:23 carries it too; verified by `md5sum`
over the matched region): four godspeed axioms + the
"IMMEDIATELY STOP ASKING CLARIFYING QUESTIONS" paragraph. `mutation-tester.md`
embeds the block **twice** in-file (`grep -c "Godspeed-enabled" = 2`,
lines 8–14 + 34–40) — still unfixed at round-6 audit. Four files omit it
entirely (bootstrapper, distiller, janitor, musketeer); bootstrapper opens
with its own operational contract instead.

**Craft implication (opinion):** copy-paste zones are acceptable in one-shot
files but are a standing drift risk in durable files — one drifted copy of 13
is the observed failure (mutation-tester's doubling). Prefer `agent:`/`agents_md:`
frontmatter flags, a shared include, or a single durable home.

## Fact — frontmatter ages: dated operational notes go stale

`ufo.md` `cascade_note` records a parked provider with an `until 2026-08-29`
date — past at survey time. Frontmatter has no freshness mechanism; a dated
operational claim is a stale-risk fact and belongs in a dated status file
(`~/.local/state/…`-style), not in a routing surface.

## Fact — command files are thin routers, not procedures

3 files at `/home/vgpnk/.config/opencode/command/*.md` (10–13 lines).
Shape: frontmatter `description` (+ `agent:` when delegating to a named agent
— `ufo.md` sets `agent: ufo`), then the body. Two idioms observed:

1. **Pointer-then-rules** (sekhmet.md, xbrd.md): line 1 = "Use the `<name>`
   skill (`<path>`) for … `$ARGUMENTS`", then 3–4 literal rules that must hold
   *even if the skill file drifts* (env pins, `-j 64` cap, `--gs` terminator,
   verbatim-quote requirement). Procedures stay in the skill.
2. **Inline protocol** (ufo.md): when the command *is* the orchestrator's
   procedure (6 numbered steps) it inlines them — justified because no skill
   file owns orchestration.

## Fact — dispatch prompts have two modes with different completeness budgets

| Mode | Files | Size | Carries | Omits |
|------|-------|------|---------|-------|
| Spawn (task dispatch) | 8× `*-L1.md` | 9–12 lines | 6 stanzas: role+wd → context → job w/ embedded verify cmds → L2 routing map → report path+fence → `| godspeed` | — |
| Round (self-iteration) | 6× `*-round-N.md` | 3–4 lines | role+wd+round → self-iterate imperative → land-scope+commit+report path → `| godspeed` | L2 map, verify cmds |

Round prompts omit the routing map deliberately: the instruction names a
*method* (pick highest-value gap), not a task, and the durable context
(SKILL.md, LOG.md, corpus gap list) already lives in the repo. `diff` of
`kake-round-4.md` vs `kasegi-round-4.md` shows only name+path differ — same
template. `protocol-round-4.md` is a 4-line hybrid (numbered jobs, still no L2
map) because its repo is the protocol, not a domain.

**Craft implication:** completeness budget scales with what the reader can
recover. A spawn subagent recovers nothing → 6 stanzas. A round L1 re-reads
its own repo → the prompt carries only what changed since spawn (round number,
method directive). Putting stale risk in the wrong file is the failure mode in
both directions: routing maps duplicated into every round prompt drift, and
durable context assumed in a spawn prompt is simply absent.
