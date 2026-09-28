# kotoba-shokunin corpus

Domain: prompt & skill craft — SKILL.md/AGENTS.md quality, trigger fidelity.

## Coverage map

| Area | File | Basis |
|------|------|-------|
| Frontmatter trigger surfaces | `knowledge/frontmatter-trigger-surface.md` | 16 production skill files surveyed 2026-09-28 |
| Skill anatomy & compression | `knowledge/anatomy-and-compression.md` | same survey; line counts 18–392 |
| Failure/anti-pattern patterns | `knowledge/fail-closed-and-anti-patterns.md` | bailian family, ufo, sekhmet-l3 |
| AGENTS.md & dispatch prompts | `knowledge/agents-md-and-dispatch-surfaces.md` | 6 child AGENTS.md + `~/.agents/AGENTS.md` + 8 `.ufo/prompts/*-L1.md` |
| Round-1 lessons | `lessons/round-1.md` | LOG.md round-1, commit `round-1`, report `../.ufo/reports/round-1/kotoba.md` |
| Round-3 lessons | `lessons/round-3.md` | LOG.md round-3, commit `round-3`, report `../.ufo/reports/round-3/kotoba.md` |

## Known gaps

- No measured trigger-fidelity data (false-positive/negative activation rates);
  checklist is static-read only, no runtime telemetry.
- No corpus on **CLAUDE.md / system-prompt / AGENTS.md-in-harness** variants
  beyond this host's files; the surface taxonomy generalizes from 3 observed
  classes only.
- Sibling skill registry boundary is asserted generically ("owning domain
  skill"); no named rival exists in-registry to arbitrate against.
