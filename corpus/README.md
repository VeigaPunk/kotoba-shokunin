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
| Trigger-miss proxy (round-6) | `knowledge/trigger-miss-proxy-round6.md` | opencode.db 398 sessions: literal-trigger coverage + godspeed always-on hole (51.5%) |
| CLAUDE.md surface (7th class) | `knowledge/claude-md-surface.md` | 16-file census; loader strings in binaries, 0 captured injections |
| Agent-def audit (round-6) | `knowledge/agent-def-audit-round6.md` | 9-item checklist applied to 18 `opencode/agents/*.md` |
| Round-5 lessons | `lessons/round-5.md` | LOG.md round-5, commit `round-5`, report `../.ufo/reports/round-5/kotoba.md` |
| Round-6 lessons | `lessons/round-6.md` | LOG.md round-6, commit `round-6`, report `../.ufo/reports/round-6/kotoba.md` |

## Known gaps

- Implicit-intent fidelity is still unmeasured — the literal-trigger proxy
  (round-6) covers only prompts that name a skill. Needs an intent-labeling
  pass; the join recipe is proven.
- MCP tool descriptions: no `mcp` config exists on this host (opencode.json
  key set verified 2026-09-28) — the surface class is absent, not just
  unsurveyed. Plugin manifests: `~/.config/opencode/plugin/` holds one
  unrelated nudge script, no manifest conventions to survey.
- Sibling arbitration gap is *measured and persisted*: named overlaps exist
  (kagi↔kake CDP, kengaku↔bailian-docs-llm-wiki); 0/5 descriptions carry an
  arbitration clause, still true at round-6 re-check (all 5 descriptions
  unchanged post-audit). Fixes are cross-domain — relayed in reports.
