# Deliverable draft — ScribeEntryRung (round 72, wave 1)

Two blocks. Block 1 is the entry to land at `corpus/knowledge/resident-index-and-rungs-round72.md`
(the fence is a delivery wrapper, not part of the file). Block 2 is the `SKILL.md` pointer.
Placeholder ids `S2XX-<short-name>` are for the L1's numbering from S214 by document.

Quote status: every located quote below was checked by this seat against the **committed snapshots**
under `.ufo/waves/round-72/snapshots/` (word-bounded, whitespace-normalized — commands and results in
the report), not relayed from the staged package. All four source-opening seats have landed and none
contradicts a quote: `ExecSrcFactory` (`S262-factory-droid-skills.md:9`), `ExecSrcPi` ("located
verbatim"), `ExecSrcHermes` ("verbatim in it"), `ExecSrcLetta` (portability sentence "byte-exact").
Two of their findings changed this draft and are carried below: Letta names **five** agents, not six,
and pi's page mentions neither `AGENTS.md` nor MCP.

## Block 1 — the entry

```markdown
source: S2XX-factory — Factory Documentation — Skills — https://docs.factory.ai/cli/configuration/skills (308 → https://docs.factory.com/harness/skills) — the page intro, and the "Use a different surface when the guidance has another shape" table (`S262-factory-droid-skills.md:106-114`) — located quote "Use skills when instructions are too specific for always-on `AGENTS.md`, too structured for a one-off prompt, and useful enough to reuse." (snapshot `S262-factory-droid-skills.md:9`; the `AGENTS.md` code span is the snapshot's own)
source: S2XX-pi — pi-mono — coding agent — Skills — https://raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/docs/skills.md (the repo alias `badlogic/pi-mono` 301s to `earendil-works/pi`; the raw path itself serves 200) — the `# Skills` heading, line 5 of the raw file — located quote "Use a skill when a workflow needs more context than a prompt template but does not need a new executable integration point." (snapshot `S263-pi-skills.md:5`)
source: S2XX-hermes — Hermes Agent Docs — Skills — https://hermes-agent.nousresearch.com/docs/user-guide/features/skills — § Agent-Managed Skills (skill_manage tool), the self-improvement-loop paragraph — located quote "memory stores small durable facts that should always be in context, while skills store longer procedures that should load only when relevant" (snapshot `S264-hermes-skills.md:610-612`)
source: S2XX-letta — Letta Docs — Skills — https://docs.letta.com/letta-code/skills/ (→ https://docs.letta.com/configuration/skills) — the page intro, the sentence after the page summary — located quote "Skills are portable across Letta, Codex, Claude Code, Hermes Agent, OpenClaw, and other compatible agents." (snapshot `S261-letta-skills.md:15`)
verified-at: 2026-10-25
recheck: 180d — `for p in "https://docs.factory.ai/cli/configuration/skills|too specific for always-on" "https://raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/docs/skills.md|more context than a prompt template" "https://hermes-agent.nousresearch.com/docs/user-guide/features/skills|should load only when relevant" "https://docs.letta.com/letta-code/skills/|portable across Letta"; do u=${p%%|*}; q=${p#*|}; printf '%s ' "$(curl -fsSL "$u" | sed 's/<[^>]*>//g' | tr -s ' \n' ' ' | grep -c "$q")"; done` — prints "1 1 1 1" on 2026-10-25; any 0 means the page moved or the fetch failed, which is a re-open, never a silent edit
ground: the lane's surface maps say where a client reads a skill, an always-on file and a command file (`corpus/knowledge/instruction-surface-census-round13.md`, `corpus/knowledge/alwayson-rule-files-round53.md`, `corpus/knowledge/command-files-round58.md`) and `corpus/knowledge/anatomy-and-compression.md:76` holds "One authoritative home per fact; the skill keeps the pointer" — but no entry states which of the three a piece of guidance belongs in: `grep -rn 'middle rung\|one-off prompt\|three rungs\|three-step' --include=*.md corpus/ SKILL.md` printed nothing at base `c69711ee`.

# The three-rung instruction ladder — what belongs in a skill, in an always-on file, or in a one-off prompt (round 72)

Authority note: four vendor pages, one harness each (tier B, vendor documentation). Factory and pi
state the boundary as advice; Hermes states it as a rule its own `skill_manage` linter checks on
skills an agent writes, and says of that linter "They warn; they never block a write."
(`S264-hermes-skills.md:643-644`). No page says a client refuses a mis-runged instruction, and no
client's loading behaviour was observed.

## The boundary, as four vendors state it

| id | vendor | row | the boundary it states | located quote |
|---|---|---|---|---|
| F1 | Factory (Droid) | S2XX-factory | three conjuncts in one sentence — too specific for always-on `AGENTS.md`, too structured for a one-off prompt, **and useful enough to reuse**; the reuse conjunct is the one the lane had not seen stated | "Use skills when instructions are too specific for always-on `AGENTS.md`, too structured for a one-off prompt, and useful enough to reuse." |
| F2 | Factory (Droid) | S2XX-factory | the same page's five-surface table: `AGENTS.md` for always-on repository instructions, a skill for a reusable workflow, a slash command for a simple user-invoked prompt, a droid for a subagent, an MCP server for external tools | "Always-on repository instructions, commands, conventions, and safety rules." (`S262-factory-droid-skills.md:110`) |
| F3 | pi | S2XX-pi | two bounds: below, a workflow needing more context than a prompt template; above, one needing a new executable integration point | "Use a skill when a workflow needs more context than a prompt template but does not need a new executable integration point." |
| F4 | pi | S2XX-pi | the mechanism the middle rung buys — name and description resident, full instructions loaded when the task calls: the resident index | "Pi advertises each available skill by name and description, then loads its full instructions only when the task calls for them." (`S263-pi-skills.md:3`) |
| F5 | Hermes Agent | S2XX-hermes | the rung rule in the harness's own words: always-in-context facts stay in memory, longer procedures load only when relevant | "memory stores small durable facts that should always be in context, while skills store longer procedures that should load only when relevant" |
| F6 | Hermes Agent | S2XX-hermes | the non-duplication half: a skill must not repeat what the always-on file already loads every turn | "Skills also do not restate what is already loaded every turn (the repo's `AGENTS.md`, tool schemas)." (`S264-hermes-skills.md:636-637`) |
| F7 | Hermes Agent | S2XX-hermes | a house authoring standard applied to a skill `/learn` synthesises, including **no invented commands** | "(≤60-char description, the standard section order, Hermes-tool framing, no invented commands)" (`S264-hermes-skills.md:123-126`, the `house authoring standards` link's parenthetical) |
| F8 | Letta | S2XX-letta | the middle rung is the portable one: the harness implements the open standard and names five agents skills travel across | "Skills are portable across Letta, Codex, Claude Code, Hermes Agent, OpenClaw, and other compatible agents." |

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
- **Check the harness's house standard before the format's, and let portability pick the middle rung.**
  One harness caps a synthesised skill's description at 60 characters and forbids commands the agent
  cannot run (F7); skills, not always-on files or prompts, are what travel between agents (F8). The
  same choice repeats one level down: a skill's always-on part is its `SKILL.md` body, depth goes to
  `references/` (`S264-hermes-skills.md:634-636`) — the lane's one-authoritative-home rule.

## Limits

- Documentary evidence only: four pages read 2026-10-25, all English, not a census — a client silent
  here is not a client without a boundary; no client's loading, routing or refusal was observed.
  Shaping disclosed — quotes are matched on each page's markdown export with whitespace collapsed;
  F1 and F6 carry a code span, F7 a markdown link across three source lines.
- pi supports the middle rung and the resident index only: its page mentions neither `AGENTS.md` nor
  MCP (0 occurrences each), and "executable integration point" is defined in its sibling
  `docs/extensions.md`. The always-on half rests on Factory (F1, F2) and Hermes (F5, F6).
- F7's standard is what `/learn` applies when it synthesises a skill, and the page does not say a
  hand-written skill is checked against it; 60 characters is one harness's number, not the format's.
  Hermes' linter is advisory (warns, never blocks, `S264-hermes-skills.md:638-644`), and F8 is Letta's
  assertion about its own family — five named agents plus "other compatible agents", none observed.
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
```

## Block 2 — `SKILL.md` § Instruction surfaces pointer

Primary form: one line, +1 line net (line 65 is 82 characters today; the fused sentence wraps to two
lines). It carries no action cell because it is prose, not a table row; the decision itself is the
entry's.

```diff
--- a/SKILL.md
+++ b/SKILL.md
@@ -65 +65,2 @@
-"All craft below" cell refers to this file's craft sections below — kept verbatim.
+"All craft below" cell refers to this file's craft sections below — kept verbatim. Rung choice
+before the fix: `corpus/knowledge/resident-index-and-rungs-round72.md` (S2nn–S2mm).
```

Alternative form: a decision-table row set, +6 lines (blank, header, separator, three rows), each row
carrying its action in the `put it in` cell. Use only if the L1 frees the lines for the four
`§ Trigger-fidelity checklist` boxes as well.

```diff
--- a/SKILL.md
+++ b/SKILL.md
@@ (after the "All craft below" paragraph, § Instruction surfaces)
+
+| guidance that is… | put it in | why (documented) |
+|---|---|---|
+| used once, or shaped for this turn only | a one-off prompt (command file) | nothing to reuse; a skill for it adds an invocation decision a prompt does not have (S2nn) |
+| reusable, too specific for the always-on file, too structured for a prompt, and not an executable integration | a skill | Factory states the three conjuncts and a five-surface table, pi the two bounds (S2nn) |
+| a constraint that applies before any skill is chosen, or a pointer to what exists | the always-on file, as an index of names and descriptions | pi advertises name + description and loads the body on demand; the index is what makes the body on-demand (S2nn) |
```

## Integration notes for the L1

1. **Numbering.** Four ids by document from S214. The entry's `source:` lines are the only id sites;
   the table's `row` column repeats them, so a renumber touches both.
2. **Quote cells — this is where C1(d) can fail.** Take the quotes exactly as above, not the staged
   cells. Evidence: the staged Factory cell is an 10-word prefix and, because the snapshot's line 9
   carries `` `AGENTS.md` `` as a code span, the staged cell is *not* a contiguous byte string in
   `S262-factory-droid-skills.md`; the full 21-word sentence with the code span is (verified). The
   staged Letta cell ("The Letta agent harness implements the open Agent Skills standard.") likewise
   fails the snapshot because "Agent Skills" is a markdown link on `S261-letta-skills.md:15`; the
   portable sentence matches. The staged Hermes cell fails because "house authoring standards" is a
   link target on `:123`; the parenthetical matches. A counter that strips markdown links/code spans
   before matching would accept the staged cells — one that does not must take the cells above.
3. **`used-by`.** Each of the four rows' `used-by` cell must list
   `corpus/knowledge/resident-index-and-rungs-round72.md` (C1(b)).
4. **A4 box.** The box needs the tokens `prompt`, `always-on`, `skill`, `index` and the tail
   `(sourced: <ids>; entry: corpus/knowledge/resident-index-and-rungs-round72.md)`. The entry supplies
   `index` in F4 and in the always-on-file bullet; nothing in the entry uses "index" for anything but
   the resident name-and-description catalogue.
5. **Corpus index.** `corpus/README.md` § Coverage map needs a row in the round-68/69/70 form, and the
   corpus baseline counts move (`tracked_files`, `report_total`) — the base is already 5 DRIFT.
6. **PROVINCE.** This is Core ground: a rung-selection rule the lane owns. The measured degradation
   curve in the second staged entry (`context-rot-and-always-on-context.md`) is *not* absorbed here
   and must not be cited by this entry.
7. **No markers left.** All four seats confirmed their quotes; nothing in block 1 needs deleting
   before landing. If a wave-2 critic contradicts one, the row is refused, not reworded.
