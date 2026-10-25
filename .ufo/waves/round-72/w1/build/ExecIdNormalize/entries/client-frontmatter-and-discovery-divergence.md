source: S220 — Agent Skills — skill.md (the format one-pager) — https://agentskills.io/skill.md — "Product summary" and "Key files and paths"; quote "at startup they load only the name and description of each skill (~50-100 tokens per skill)"; also "Discovery paths: `.agents/skills/` (cross-client standard), `.<client>/skills/` (client-specific)"; fetched as `.md` 16 035 B on 2026-10-23 — opened 2026-10-23 (carried from the staged campaign row S255; this seat did not re-open the page)
source: S221 — Agent Skills — How to add skills support to your agent (loading model, validation and disclosure) — https://agentskills.io/client-implementation/adding-skills-support.md — "The core principle: progressive disclosure" three-tier table, "### Lenient validation" and "### Behavioral instructions"; quote "The lenient approach above deliberately relaxes these to improve compatibility with skills authored for other clients."; also the tier table "~50-100 tokens per skill" and "<5000 tokens (recommended)"; fetched as `.md` 20 446 B on 2026-10-23 — opened 2026-10-23 (carried from the staged campaign row S256; this seat did not re-open the page)
verified-at: 2026-10-23
recheck: 90d — re-fetch the `.md` and confirm the frontmatter list, the discovery paths and the ~50-100 token figure are unchanged (ran 2026-10-23) (row S220; every row's own stripped prose is in the round-72 Gate notes)
ground: normalization candidate, round 72 wave 1; rows S220, S221 from staged S255, S256

# Client frontmatter and discovery divergence — the two rows this theme adds (round 72, candidate)

**Candidate entry.** Rows normalized by seat ExecIdNormalize in round-72 wave 1 from the read-only campaign package `merge/kotoba/`; admission is the source-opening seats' and the L1's decision, and the rule prose for `SKILL.md` § Trigger-fidelity checklist is the C1 seat's. Every claim below is the staged row's own `teaches` cell; the quotes are carried from the row's `anchor` cell and were not re-fetched here.

## What the rows teach

- **S220** — the canonical frontmatter list in one place — `name`, `description`, optional `license`, `compatibility`, `metadata`, `allowed-tools` — the **cross-client standard** being `.agents/skills/` with client-specific roots beside it, and the metadata cost quantified at ~50-100 tokens per skill, which is the budget the lane's other figures now reconcile against
- **S221** — the normative loading model with its token costs (catalog ~50-100 tokens per skill at session start; instructions under 5000 tokens on activation; resources on reference), the **lenient-validation** policy that deliberately relaxes the specification's strict `name` constraints "to improve compatibility with skills authored for other clients", and the two behavioural-instruction blocks a client is told to put beside the catalog

## Located quotes (carried from the anchor cells)

| row | quotes |
|---|---|
| S220 | "at startup they load only the name and description of each skill (~50-100 tokens per skill)" / "Discovery paths: `.agents/skills/` (cross-client standard), `.<client>/skills/` (client-specific)" |
| S221 | "The lenient approach above deliberately relaxes these to improve compatibility with skills authored for other clients." |

