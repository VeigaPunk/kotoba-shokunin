# kotoba-shokunin corpus

Domain: prompt & skill craft — SKILL.md/AGENTS.md quality, trigger fidelity.

## Coverage map

| Area | File | Basis |
|------|------|-------|
| Frontmatter trigger surfaces | `knowledge/frontmatter-trigger-surface.md` | 16 production skill files surveyed 2026-09-28 |
| Skill anatomy & compression | `knowledge/anatomy-and-compression.md` | same survey; line counts 18–392 |
| Failure/anti-pattern patterns | `knowledge/fail-closed-and-anti-patterns.md` | bailian family, ufo, sekhmet-l3 |
| AGENTS.md & dispatch prompts | `knowledge/agents-md-and-dispatch-surfaces.md` | 6 child AGENTS.md + `~/.agents/AGENTS.md` + 8 `.ufo/prompts/*-L1.md` |
| Agent defs, commands & round-N prompts | `knowledge/agent-defs-commands-and-round-prompts.md` | 18 `opencode/agents/*.md` + 3 `opencode/command/*.md` + 6 `*-round-N.md` |
| Fleet SKILL.md audit (round-5) | `knowledge/fleet-skill-audit-round5.md` | 13-item checklist applied to 5 sibling `*-shokunin/SKILL.md`, strict + refined readings |
| Harness system prompt (6th class) | `knowledge/harness-system-prompt.md` | observed-not-owned; notes from this session's injected preamble |
| Activation telemetry & compressed router surface | `knowledge/skill-activation-telemetry.md` | opencode.db `part` (415 calls / 216 sessions), opencode.log permission lines, omp session jsonl; `<skills>` render measured ~95–103 chars vs 160–820 source |
| Round-5 lessons | `lessons/round-5.md` | LOG.md round-5, commit `round-5`, report `../.ufo/reports/round-5/kotoba.md` |

## Known gaps

- Trigger-fidelity telemetry is *located* (round-5): per-call activation lives
  in `~/.local/share/opencode/opencode.db` `part` table with per-prompt
  attribution joins. Still unmeasured: false-negative/false-positive rates —
  the join recipe is proven, the prompt-intent labeling pass is future work.
- Surface taxonomy covers 5 writable classes + the harness-injected system
  prompt (observed, ELF-embedded template). Uncovered: CLAUDE.md files (7
  exist on this host per scout find, none surveyed), MCP tool descriptions
  (cached schemas seen, no server config found), plugin manifests.
- Sibling arbitration gap is now *measured*, not open: named overlaps exist
  (kagi↔kake CDP, kengaku↔bailian-docs-llm-wiki) and 0/5 descriptions carry an
  arbitration clause. Fixes are cross-domain — relayed in the round-5 report.
