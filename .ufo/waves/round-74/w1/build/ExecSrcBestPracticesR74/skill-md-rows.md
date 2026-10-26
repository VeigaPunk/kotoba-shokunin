### Body craft — the specification's skill-creation guides

Draft for SKILL.md, C1 condition (e). Placement: directly under `## Compression
rules` (SKILL.md:190) — that section already owns the "spend tokens, not body"
decision and an H3 child keeps the H2 list unchanged. Line cost: 6 lines
(1 heading, 2 prose, 1 blank, 1 table header + separator, 3 rows) against the
570 → 600 budget. Two rows satisfy (e); the third is the strongest rule left and
can be dropped if the budget binds.

The format's own authoring guide (`corpus/SOURCES.md` S223, 15 060 B fetched
2026-10-25, upstream `agentskills/agentskills@69ef37e` `docs/skill-creation/best-practices.mdx`)
says how much body to spend and how prescriptive each part should be:

| Rule (S223) | What the guide states | Action |
|---|---|---|
| specificity tracks fragility | "Match the specificity of your instructions to the fragility of the task." — freedom plus the reason where several approaches work, an exact command where the step is fragile | Keep a row prescriptive only where the step is fragile, and state the reason when several fixes would work |
| size, then progressive disclosure | "recommends keeping `SKILL.md` under 500 lines and 5,000 tokens", and names the condition that loads each side file | Hold `SKILL.md` under 500 lines by moving detail into `references/`-style side files (here `corpus/knowledge/`), each named with the condition that loads it |
| defaults, not menus | "When multiple tools or approaches could work, pick a default and mention alternatives briefly" | Give one default route per row, and name an alternative only with the condition that selects it |

Verification of (e) for these rows: each action cell carries ≥5 words and at least
one token that occurs in `snapshot.md` (`SKILL.md` ×5, `references/` ×4, counted
above). Quotes are literal substrings of `snapshot.md` after whitespace collapse
only, in the page's own bytes — no marker removal needed for these three.
