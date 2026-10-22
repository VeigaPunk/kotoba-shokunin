# kotoba-shokunin — Province

**Domain:** prompt & skill craft — scopes SKILL.md/AGENTS.md quality, trigger fidelity

**Owns:** the domain knowledge, playbooks, error patterns, and checklists above.
**Refuses:** anything outside this domain; report cross-domain evidence back to the orchestrator rather than absorbing it.

## Core

Appended round 46 (LEARNING.md § Province is a frontier); surfaces the lane governs now:

- `SKILL.md` — trigger/frontmatter craft, anatomy and compression, decision tables, the four fidelity checklists (backed by `corpus/knowledge/frontmatter-trigger-surface.md`, `corpus/knowledge/anatomy-and-compression.md`, `corpus/knowledge/fail-closed-and-anti-patterns.md`).
- Agent-definition, always-on (AGENTS.md-class) and dispatch-prompt craft — `corpus/knowledge/agent-defs-commands-and-round-prompts.md`, `corpus/knowledge/agents-md-and-dispatch-surfaces.md`, `corpus/knowledge/dispatch-prompt-audit-round7.md`.
- Executable instruments over those surfaces — `verifiers/verify_skill_checklist.py`, `verifiers/verify_surfaces.py`, `verifiers/verify_harness_claims.py`, `verifiers/compare_harness_independent.py`, `verifiers/verify_corpus_integrity.py`, `verifiers/verify_corpus_independent.py`, `verifiers/check_substrate_pins.py`, `verifiers/check_assertion_floors.py`.
- Frontmatter XML-tag rule (round 47, moved from Frontier): S003's Anthropic rule (`corpus/SOURCES.md`; superseded as a row by S019 in round 48) is approximated lexically on the unparsed `name` and `description` text by `verifiers/verify_skill_checklist.py` check `trigger.no_xml_tag`, with four discriminating fixtures (code-span, folded split, YAML escape, arrow/comparison control); it is not the packager's parsed-value rule (round 48 entry below); this file's description is tag-free.
- Frontmatter rule authorities (round 48): which authority imposes which SKILL.md frontmatter rule — open spec (S018), its reference validator skills-ref (S017), Anthropic docs (S019), Anthropic's packager (S012), Codex docs (S021) — and what the lane's lexical `trigger.no_xml_tag` actually executes (S020), with run counterexamples: `corpus/knowledge/frontmatter-rule-authorities-round48.md`.

## Frontier

Explored, not held — the live list is `corpus/README.md` § Frontier:

- Executed checklist coverage (33 of 41 boxes still lane-attested prose), command extraction outside the declared vocabulary, implicit-intent trigger fidelity, MCP/plugin instruction surfaces, sibling arbitration clauses, per-render skill consumption.
- Loader-rule freshness: the omp 18.12.3 substrate drift (surfaces 5/7, pins 1/3) and the frontmatter `description` XML-token rule — `corpus/lessons/round-46.md` § Mistakes, `corpus/SOURCES.md`. **Round 47:** the XML-token half moved to Core; the round-46 figures above are historical (they were the round-44 before-column, `corpus/lessons/round-47.md` M20). omp 18.12.5 and opencode 1.19.3 were re-derived and re-pinned (surfaces 7/7, pins 3/3 at default resolution). Still not held: re-derivation after a rebuild is manual — the omp extractor is a callee-name allowlist and opencode changed lineage under the same path family.

## Adjacent

Sibling-owned ground (report, don't absorb) — evidence `.ufo/round-46/scouts/w2-connector.md`:

- chousa — deep-research method (source hierarchy, citation chaining); kotoba cites it, never re-derives it.
- kumitate — orchestration/dispatch runtime and swarm lifecycle; kotoba owns the prompt wording, not the runtime.
- kengaku — LLM/model evaluation and route telemetry.
- tameshi — verification-fixture craft and mutation testing.
- kasegi — security research incl. prompt-injection exploits.
- kotodama (worldbuilding/naming), mado (desktop config), revenger (shipped-artifact RE), mori (fleet observability), kama (model serving) — no overlap observed.
