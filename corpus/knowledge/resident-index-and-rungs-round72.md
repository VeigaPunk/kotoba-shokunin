source: S214 — Factory Documentation — Skills — https://docs.factory.ai/cli/configuration/skills (308 → https://docs.factory.com/harness/skills) — the page intro, and the "Use a different surface when the guidance has another shape" table (`S262-factory-droid-skills.md:106-114`) — located quote "Use skills when instructions are too specific for always-on `AGENTS.md`, too structured for a one-off prompt, and useful enough to reuse." (snapshot `S262-factory-droid-skills.md:9`; the `AGENTS.md` code span is the snapshot's own)
source: S215 — pi-mono — coding agent — Skills — https://raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/docs/skills.md (the repo alias `badlogic/pi-mono` 301s to `earendil-works/pi`; the raw path itself serves 200) — the `# Skills` heading, line 5 of the raw file — located quote "Use a skill when a workflow needs more context than a prompt template but does not need a new executable integration point." (snapshot `S263-pi-skills.md:5`)
source: S216 — Hermes Agent Docs — Skills — https://hermes-agent.nousresearch.com/docs/user-guide/features/skills — § Agent-Managed Skills (skill_manage tool), the self-improvement-loop paragraph — located quote "memory stores small durable facts that should always be in context, while skills store longer procedures that should load only when relevant" (snapshot `S264-hermes-skills.md:610-612`)
verified-at: 2026-10-25
recheck: 180d — `for p in "https://docs.factory.ai/cli/configuration/skills|too specific for always-on" "https://raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/docs/skills.md|more context than a prompt template" "https://hermes-agent.nousresearch.com/docs/user-guide/features/skills|should load only when relevant"; do u=${p%%|*}; q=${p#*|}; printf '%s ' "$(curl -fsSL "$u" | sed 's/<[^>]*>//g' | tr -s ' \n' ' ' | grep -c "$q")"; done` — prints "1 1 1" on 2026-10-25; any 0 means the page moved or the fetch failed, which is a re-open, never a silent edit
ground: the lane's surface maps say where a client reads a skill, an always-on file and a command file (`corpus/knowledge/instruction-surface-census-round13.md`, `corpus/knowledge/alwayson-rule-files-round53.md`, `corpus/knowledge/command-files-round58.md`) and `corpus/knowledge/anatomy-and-compression.md:76` holds "One authoritative home per fact; the skill keeps the pointer" — but no entry states which of the three a piece of guidance belongs in: `grep -rn 'middle rung\|one-off prompt\|three rungs\|three-step' --include=*.md corpus/ SKILL.md` printed nothing at base `c69711ee`.

# The three-rung instruction ladder — what belongs in a skill, in an always-on file, or in a one-off prompt (round 72)

Authority note: three vendor pages, one harness each (tier B, vendor documentation). Factory and pi
state the boundary as advice; Hermes states it as a rule its own `skill_manage` linter checks on
skills an agent writes, and says of that linter "They warn; they never block a write."
(`S264-hermes-skills.md:643-644`). No page says a client refuses a mis-runged instruction, and no
client's loading behaviour was observed.

## The boundary, as three vendors state it

| id | vendor | row | the boundary it states | located quote |
|---|---|---|---|---|
| F1 | Factory (Droid) | S214 | three conjuncts in one sentence — too specific for always-on `AGENTS.md`, too structured for a one-off prompt, **and useful enough to reuse**; the reuse conjunct is the one the lane had not seen stated | "Use skills when instructions are too specific for always-on `AGENTS.md`, too structured for a one-off prompt, and useful enough to reuse." |
| F2 | Factory (Droid) | S214 | the same page's five-surface table: `AGENTS.md` for always-on repository instructions, a skill for a reusable workflow, a slash command for a simple user-invoked prompt, a droid for a subagent, an MCP server for external tools | "Always-on repository instructions, commands, conventions, and safety rules." (`S262-factory-droid-skills.md:110`) |
| F3 | pi | S215 | two bounds: below, a workflow needing more context than a prompt template; above, one needing a new executable integration point | "Use a skill when a workflow needs more context than a prompt template but does not need a new executable integration point." |
| F4 | pi | S215 | the mechanism the middle rung buys — name and description resident, full instructions loaded when the task calls: the resident index | "Pi advertises each available skill by name and description, then loads its full instructions only when the task calls for them." (`S263-pi-skills.md:3`) |
| F5 | Hermes Agent | S216 | the rung rule in the harness's own words: always-in-context facts stay in memory, longer procedures load only when relevant | "memory stores small durable facts that should always be in context, while skills store longer procedures that should load only when relevant" |
| F6 | Hermes Agent | S216 | the non-duplication half: a skill must not repeat what the always-on file already loads every turn | "Skills also do not restate what is already loaded every turn (the repo's `AGENTS.md`, tool schemas)." (`S264-hermes-skills.md:636-637`) |
| F7 | Hermes Agent | S216 | a house authoring standard applied to a skill `/learn` synthesises, including **no invented commands** | "(≤60-char description, the standard section order, Hermes-tool framing, no invented commands)" (`S264-hermes-skills.md:123-126`, the `house authoring standards` link's parenthetical) |

## What a skill author does with this

- **Choose the rung by what is read every turn.** The always-on file is read on every turn, a skill
  body only when the task is relevant, a prompt once (F5); its own row is standing instructions,
  commands, conventions and safety rules (F2). Only some tasks need it? One rung down.
- **Never restate the always-on file in a skill.** A body that repeats a standing rule pays twice and
  drifts (F6); where the rule must apply before any skill is chosen, it lives there and the skill points.
- **Read Factory's sentence as a conjunction and test reuse first.** Too specific for `AGENTS.md` and
  too structured for a prompt are necessary, not sufficient; a workflow used once has nothing to reuse,
  and a skill for it adds an invocation decision a prompt does not have (F1). Factory writes no "rung"
  word — it publishes a surface table (F2) — so the ladder is the lane's name for the boundary.
- **The upper bound is execution, not size.** A skill is for a workflow that does *not* need a new
  executable integration point (F3); guidance that must run at an event goes to the client's hook file
  (`corpus/knowledge/hook-files-round59.md`), guidance that must reach a tool to an MCP server (F2).
- **Keep the always-on file an index, not a body.** The client's own index entry for a skill is its
  name and description, with the body fetched on demand (F4), so the always-on file spends its
  every-turn cost on constraints and pointers to what exists, never on a body only some tasks read.
- **Check the harness's house standard before the format's,.**
  One harness caps a synthesised skill's description at 60 characters and forbids commands the agent
  cannot run (F7). The
  same choice repeats one level down: a skill's always-on part is its `SKILL.md` body, depth goes to
  `references/` (`S264-hermes-skills.md:634-636`) — the lane's one-authoritative-home rule.

## Limits

- Documentary evidence only: three pages read 2026-10-25, all English, not a census — a client silent
  here is not a client without a boundary; no client's loading, routing or refusal was observed.
  Shaping disclosed — quotes are matched on each page's markdown export with whitespace collapsed;
  F1 and F6 carry a code span, F7 a markdown link across three source lines.
- pi supports the middle rung and the resident index only: its page mentions neither `AGENTS.md` nor
  MCP (0 occurrences each), and "executable integration point" is defined in its sibling
  `docs/extensions.md`. The always-on half rests on Factory (F1, F2) and Hermes (F5, F6).
- F7's standard is what `/learn` applies when it synthesises a skill, and the page does not say a
  hand-written skill is checked against it; 60 characters is one harness's number, not the format's.
  Hermes' linter is advisory (warns, never blocks, `S264-hermes-skills.md:638-644`).
- The rung boundary that fails in practice is the invocation decision between rung two and rung three;
  the lane measures it elsewhere and restates no figure here —
  `corpus/knowledge/skill-activation-telemetry.md` (compressed router surface) and `corpus/lessons/round-5.md`.

## Scope

Prompt-and-skill craft: which of three instruction surfaces a piece of guidance belongs in. Not:
where each client reads each surface (the round-53/56/58/59/60 maps), the `description`'s trigger
craft (§ Frontmatter craft), how to test a skill once it exists
(`corpus/knowledge/skill-eval-artefacts-round70.md`), or any measured activation figure (kengaku's
adjacent ground).

## Related

- `corpus/knowledge/anatomy-and-compression.md` — "One authoritative home per fact; the skill keeps
  the pointer": the compression rule this entry's rung choice enforces.
- `corpus/knowledge/alwayson-rule-files-round53.md` — which always-on file each client reads.
- `corpus/knowledge/command-files-round58.md` — the prompt rung, per client.
- `corpus/knowledge/hook-files-round59.md` — the surface for guidance that must run at an event.
- `corpus/knowledge/skill-eval-artefacts-round70.md` — testing a skill after it is routed here.
