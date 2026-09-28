# AGENTS.md & dispatch-prompt surfaces

Sourced 2026-09-28. Closes the AGENTS.md gap filed in round-1 corpus README.

## Fact — three instruction surfaces load differently

| Surface | Files observed | Load condition |
|---------|----------------|----------------|
| SKILL.md | 16 under `~/.agents/skills/` + `~/.config/opencode/skills/` | Opt-in via frontmatter `description` routing |
| AGENTS.md | 6 identical-shape files in `/home/vgpnk/projects/shokunin/*/AGENTS.md` + `~/.agents/AGENTS.md` | Always injected for sessions rooted in the repo |
| Dispatch prompt | 8 files `/home/vgpnk/projects/shokunin/.ufo/prompts/*-L1.md` (9–12 lines) | One-shot, read once by a spawned subagent |

## Fact — AGENTS.md shape is constraint-only

The six shokunin child AGENTS.md files share an identical 5-line template
(verified by `cat`; `md5sum` values differ only because each embeds its repo
name — e.g. `16318e91…` kotoba vs `fe1b783a…` kagi):

```
# <name> operating rules
- Work only within this repo and its PROVINCE.md scope.
- Every change appends a LOG.md entry with the evidence that motivated it.
- Never fabricate domain knowledge: cite a file, a command output, or a source.
```

`~/.agents/AGENTS.md` (~60 lines) is longer but still constraint-only: posture
rules ("name the axes", "iterate cheap in parallel"), runtime bans ("no
worktrees"), and operator-attested capability records. Zero procedures, zero
trigger language, zero frontmatter.

**Craft implication (opinion):** bytes in AGENTS.md are paid every session
unconditionally — the metric is *constraint survival*, not match precision.
Procedures and how-to content placed there are misfiled: they should live in an
opt-in SKILL.md.

## Fact — dispatch prompts follow a fixed stanza order

From `diff` of `.ufo/prompts/kagi-L1.md` vs `kotoba-L1.md` (same template,
different round/job) and `aggregator-L1.md`:

1. Role + working dir (`You are the X L1 … Working dir: …`)
2. Context (domain ownership + rank)
3. Job (imperative, embeds verification commands like `the-janitor --help`)
4. L2 subagent routing map (lane → model)
5. Report path + scope fence ("Do not touch MANIFEST.json or other repos")
6. Literal suffix ` | godspeed`

**Craft implication:** the reader is a blank-context subagent — a missing
stanza is unrecoverable because there is no conversation to clarify with.
Completeness beats brevity; embed verification commands in the job stanza
rather than describing them.

## Fact — dispatch prompts drift across rounds in the routing stanza

kotoba-L1 round-1 prompt put scout on `m_zfl`; an operator interjection
moved scout to `m_flash`, and the round-2 kagi prompt already carries
`scout m_flash`. Dispatch prompts are regenerated per round — they are the
*wrong* place for durable routing policy; the fleet map belongs in a durable
surface (this is why it appears verbatim in every prompt instead of being
referenced).
