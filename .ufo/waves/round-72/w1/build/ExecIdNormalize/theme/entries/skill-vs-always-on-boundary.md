source: S214 — Letta Docs — Skills — https://docs.letta.com/letta-code/skills/ — the "Skills" page under the Letta agent harness; quote "The Letta agent harness implements the open Agent Skills standard."; also "Skills are portable across Letta, Codex, Claude Code, Hermes Agent, OpenClaw, and other compatible agents."; and the scope table 「Project-scoped」 / 「Agent-scoped (MemFS)」 / 「Computer-scoped」 — opened 2026-10-23 (carried from the staged campaign row S261; this seat did not re-open the page)
source: S215 — Factory Documentation — Skills — https://docs.factory.ai/cli/configuration/skills — the "Skills" page under the Droid harness; quote "Use skills when instructions are too specific for always-on AGENTS.md"; also "Create reusable SKILL.md workflows that Droid can discover, invoke, and share across projects."; and the install path ".factory/skills/" — opened 2026-10-23 (carried from the staged campaign row S262; this seat did not re-open the page)
source: S216 — pi-mono — coding agent — Skills — https://raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/docs/skills.md — the "# Skills" heading of the file; quote "Pi advertises each available skill by name and description, then loads its full instructions only when the task calls for them."; also "Use a skill when a workflow needs more context than a prompt template but does not need a new executable integration point." — opened 2026-10-23 (carried from the staged campaign row S263; this seat did not re-open the page)
source: S217 — Hermes Agent Docs — Skills — https://hermes-agent.nousresearch.com/docs/user-guide/features/skills — the "Learning a skill from sources" section; quote "house authoring standards (≤60-char description, the standard section order, Hermes-tool framing, no invented commands)"; also "/learn is the fast way to turn something you already know — or a pile of reference material — into a reusable skill, without hand-writing the SKILL.md" — opened 2026-10-23 (carried from the staged campaign row S264; this seat did not re-open the page)
verified-at: 2026-10-23
recheck: 90d — re-fetch and confirm the three scopes and the portability list are unchanged (ran 2026-10-23) (row S214; every row's own stripped prose is in the round-72 Gate notes)
ground: normalization candidate, round 72 wave 1; rows S214, S215, S216, S217 from staged S261, S262, S263, S264

# Skill versus always-on file versus one-off prompt — the middle rung (round 72, candidate)

**Candidate entry.** Rows normalized by seat ExecIdNormalize in round-72 wave 1 from the read-only campaign package `merge/kotoba/`; admission is the source-opening seats' and the L1's decision, and the rule prose for `SKILL.md` § Trigger-fidelity checklist is the C1 seat's. Every claim below is the staged row's own `teaches` cell; the quotes are carried from the row's `anchor` cell and were not re-fetched here.

## What the rows teach

- **S214** — a **three-scope** model the lane has not held — project scope at the shared `.agents/skills/` root, an **agent-scoped** tier inside the agent's own memory filesystem, and a computer-scoped bundle — plus an explicit portability claim naming four other compatible agents
- **S215** — the clearest first-party statement of the **decision boundary** between the three ways to give an agent instructions: a skill is what you use when instructions are too specific for always-on `AGENTS.md` and too structured for a one-off prompt — the middle rung of the lane's instruction-surface ladder, stated by a vendor rather than inferred
- **S216** — the same decision boundary as S215 from a different vendor, and a naming of the three rungs: a skill is for a workflow that needs more context than a prompt template but not a new executable integration point — between a prompt and an MCP tool
- **S217** — a **house authoring standard** with a concrete description-length limit of sixty characters — against the specification's 1024 — and a `/learn` command that synthesises a skill from arbitrary sources and then holds it to the house standard, including a rule that the skill must not invent commands

## Located quotes (carried from the anchor cells)

| row | quotes |
|---|---|
| S214 | "The Letta agent harness implements the open Agent Skills standard." / "Skills are portable across Letta, Codex, Claude Code, Hermes Agent, OpenClaw, and other compatible agents." |
| S215 | "Use skills when instructions are too specific for always-on AGENTS.md" / "Create reusable SKILL.md workflows that Droid can discover, invoke, and share across projects." |
| S216 | "Pi advertises each available skill by name and description, then loads its full instructions only when the task calls for them." / "Use a skill when a workflow needs more context than a prompt template but does not need a new executable integration point." |
| S217 | "house authoring standards (≤60-char description, the standard section order, Hermes-tool framing, no invented commands)" / "/learn is the fast way to turn something you already know — or a pile of reference material — into a reusable skill, without hand-writing the SKILL.md" |

