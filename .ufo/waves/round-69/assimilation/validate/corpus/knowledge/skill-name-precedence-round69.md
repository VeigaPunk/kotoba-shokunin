# Skill name-collision precedence by client — which same-named skill wins

source: S203 — Roo Code Documentation — Skills — https://docs.roocode.com/features/skills — "What Skills Let You Do" (Override Control) and "Choose a location"
source: S204 — Amp — Agent Skills — https://ampcode.com/docs/customize/skills — "Skill Sources and Precedence"
source: S205 — Deep Code — Agent Skills — https://deepcode.vegamo.cn/en/docs/configuration/agent-skills — "Scan Locations"
source: S206 — Junie — Agent Skills — https://junie.jetbrains.com/docs/agent-skills.html — "Skill location"
source: S207 — opencode — Agent skills (served docs page) — https://opencode.ai/docs/skills/ — "Troubleshoot loading"
verified-at: 2026-10-25
recheck: 90d — re-fetch all five pages and confirm each located quote and the rule it carries are unchanged

## Question

Two skills with the same `name` reach one client — one in the project, one in the user's home,
or one in the client's own folder and one in the shared `.agents/skills/` folder. Which one does
the model see? A skill author who cannot answer this cannot predict which body runs.

## Answer by client

| Client | Collision rule the client documents | Located quote | Source |
|---|---|---|---|
| Roo Code | Scope order: a project skill beats a global one, a mode-specific skill beats a generic one; within one scope the native `.roo/skills/` root is labelled higher priority than the shared `.agents/skills/` root | "Project skills override global skills, mode-specific override generic" | S203 |
| Amp | Source order: a fixed ordered list of skill sources, in which a local skill masks a repository skill of the same name | "Local skills mask repository skills with the same name." | S204 |
| Deep Code | Root order: roots are scanned in a numbered priority order and one winner is kept per name | "only the highest-priority one is kept" | S205 |
| Junie | Scope order: project-level beats user-level, and the loser is ignored rather than merged | "the project-level skill takes precedence and the user-level skill is ignored." | S206 |
| opencode | No precedence stated: the troubleshooting guidance asks for names that are unique across every location it loads | "Ensure skill names are unique across all locations" | S207 |

## What a skill author does with this

- **Four of five clients resolve a collision by order, not by merging.** One body wins and the
  other is not shown. A skill author cannot rely on two same-named skills being combined.
- **The orders differ in kind.** Roo Code and Junie order by *scope* (project over global or user);
  Deep Code orders by *root*; Amp orders by *source*. The same pair of skills can resolve
  differently on two clients.
- **One client states no order at all.** opencode's only guidance is uniqueness, so a collision
  there has no documented winner.
- **The portable rule is therefore uniqueness.** Give a skill a `name` that will not collide with a
  skill the user may install elsewhere; do not depend on any client's order.

## Limits

- Documentary evidence only: what each page states, not observed client behaviour.
- Roo Code's "Override Priority" section states the in-scope root order in markup-bearing text
  (`<strong>` around project/global, `<code>` around `.roo/` and `.agents/`); the entry's located
  quote is the unshaped Override Control bullet instead (QUALITY Q42), and the root label rests on
  the unshaped "Roo-specific (higher priority)" heading lines.
- Five clients, none of them the lane's pinned seven; a pinned client's collision rule is not
  claimed here.

## Scope

Prompt-and-skill craft: where a skill must sit and what it must be named for its body to be the one
a client loads. Sibling boundaries: the distribution and installation channel of a skill package
is not this entry's ground; a client's trust gate for untrusted bodies is
`corpus/knowledge/client-trust-gates-round68.md`.
