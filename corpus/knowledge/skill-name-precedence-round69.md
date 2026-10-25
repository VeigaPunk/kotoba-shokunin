source: S203 — Roo Code Documentation — Skills — https://docs.roocode.com/features/skills — the "What Skills Let You Do" section, Override Control bullet — located quote "Project skills override global skills, mode-specific override generic"
source: S204 — Amp — Agent Skills — https://ampcode.com/docs/customize/skills — the "Skill Sources and Precedence" section — located quote "Local skills mask repository skills with the same name."
source: S205 — Deep Code — Agent Skills — https://deepcode.vegamo.cn/en/docs/configuration/agent-skills — the "Scan Locations" section — located quote "only the highest-priority one is kept"
source: S206 — Junie — Agent Skills — https://junie.jetbrains.com/docs/agent-skills.html — the "Skill location" section — located quote "the project-level skill takes precedence and the user-level skill is ignored."
source: S207 — opencode — Agent skills (served V1 docs page) — https://opencode.ai/docs/skills/ — the "Troubleshoot loading" section — located quote "Ensure skill names are unique across all locations"
verified-at: 2026-10-25
recheck: 90d — re-fetch all five pages and confirm each located quote and the rule it carries are unchanged

# Skill name-collision precedence by client — what each client documents about two same-named skills

The round-56 entry `agent-definition-files-round56.md` and its successors map where a client's
agent, command, hook, scoped-rule and plugin files live. This entry holds a different surface:
**what a client documents about two skills that share one `name`**. Round 50's
`skill-selection-rules-round50.md` already carries a "which one wins" column with same-name rules
for six client pages, opencode among them; the delta here is **four clients that column does not
hold** (Roo Code, Amp, Deep Code, Junie) plus the cross-client synthesis below.

## The per-client map

| client | collision rule the client documents | located quote | source |
|---|---|---|---|
| Roo Code | scope order, with the root above the mode split: a project-scope skill beats a global-scope skill; within one scope the native `.roo/skills/` root outranks the shared `.agents/skills/` root, and the page's own precedence ladder orders locations before it orders mode-specific against generic — the quote's two clauses are therefore not independent | "Project skills override global skills, mode-specific override generic" | S203 |
| Amp | source order over eleven sources, and the order inverts by tree: `~/.agents/skills/` (item 2) precedes project `.agents/skills/` (item 4), while project `.claude/skills/` (item 5) precedes `~/.claude/skills/` (item 6); a personal-repository skill masks a workspace one, and both mask official Amp skills | "Local skills mask repository skills with the same name." | S204 |
| Deep Code | root order: roots are scanned in a numbered priority order (project roots before user roots), and one winner is kept per name | "only the highest-priority one is kept" | S205 |
| Junie | scope order for the `.junie/skills/` pair only: a project-level skill beats a user-level one of the same name, and the loser is ignored. The page loads `.agents/skills/`, extension, custom-folder and built-in skills too and states no order among them | "the project-level skill takes precedence and the user-level skill is ignored." | S206 |
| opencode (V1 route) | no precedence stated: the troubleshooting guidance asks only that names be unique across every location it loads. The same client's V2 docs route documents an order (observed by this round's ScoutOpencode seat, not mined into a row); this entry counts the V1 route and claims nothing about the V2 ladder | "Ensure skill names are unique across all locations" | S207 |

## What a skill author does with this

- **Four of the five cited routes resolve a collision by order, not by merging.** One body wins and
  the other is not shown. A skill author cannot rely on two same-named skills being combined.
- **The orders are not three different kinds, and one of them reverses.** Roo Code and Deep Code both order scope first
  (project before global/user) and the native root before the shared one; Junie states only the
  project/user pair; Amp is the one flat source list. The same pair of skills can still resolve
  differently on two clients, because the orders name different keys.
- **The one route that states no order asks for uniqueness instead.** opencode's V1 page has no
  winner; its remedy is names that cannot collide.
- **The portable rule is therefore uniqueness.** Give a skill a `name` that will not collide with a
  skill the user may install elsewhere; do not depend on any client's order.

## Limits

- Documentary evidence only: what each page states, not observed client behaviour.
- The Roo quote is the unshaped Override Control bullet; the page's in-scope root order is
  markup-bearing (`<strong>`, `<code>`) and the "Roo-specific (higher priority)" labels are code-
  fence comment lines inside its `Choose a location` blocks (QUALITY Q42 shaping, disclosed).
- opencode is one of the lane's pinned clients; four of the five are not. The V2 route's ladder is
  named but not adopted — the V2 route was read this round only to bound the claim, and its row (S064) was mined in round 54 for a different question and no longer matches the page's bytes.
- Junie's rule universe is the `.junie/skills/` pair only; the page states no order among the
  other roots it loads. Roo's collision surface is stated in plain 16-word prose in the same
  section, which the quote above does not carry.
- Five clients, all English pages, read 2026-10-25. A pinned sibling's Kimi-scope rule
  (kumitate `corpus/knowledge/kimi-skills-plugins.md`) is deliberately outside this entry.

## Scope

Prompt-and-skill craft: where a skill must sit and what it must be named for its body to be the one
a client loads. Sibling boundaries: the distribution and installation channel of a skill package
is not this entry's ground; a client's trust gate for untrusted bodies is
`corpus/knowledge/client-trust-gates-round68.md`.

## Related

- `corpus/knowledge/skill-selection-rules-round50.md` — the six-client same-name column this entry
  extends.
- `corpus/knowledge/client-trust-gates-round68.md` — what clients do with an untrusted skill body.
