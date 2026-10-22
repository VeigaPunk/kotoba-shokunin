# AGENTS.md & dispatch-prompt surfaces

Sourced 2026-09-28. Closes the AGENTS.md gap filed in round-1 corpus README.

## Fact — three instruction surfaces load differently

| Surface | Files observed | Load condition |
|---------|----------------|----------------|
| SKILL.md | 16 under `~/.agents/skills/` + `~/.config/opencode/skills/` | Opt-in via frontmatter `description` routing |
| AGENTS.md | 6 identical-shape files in `/home/vgpnk/projects/shokunin/*/AGENTS.md` + `~/.agents/AGENTS.md` — **round-53 correction (2026-10-22):** the root is `/home/vgpnk/Projects/shokunin` (capital `P`; the lowercase path does not exist on this host) and it held 17 `AGENTS.md` files, of which 9 share the 5-line body (md5 `12a62ab9…` over lines 2-end), 4 share a second body (`96f7dfd1…`) and 4 are singletons | Always injected for sessions rooted in the repo — **bounded round-53 (2026-10-22):** true of the harnesses of that era (omp, opencode), not of every client: Claude Code reads `CLAUDE.md` files only when one counts and nothing under `.agents/` (S043 `memory.md:357`, `:378`), Codex reads `AGENTS.override.md` ahead of `AGENTS.md` with at most one file per directory (S044 `agents-md.md:11-12`); per-client table `corpus/knowledge/alwayson-rule-files-round53.md` |
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
**round-53 correction (2026-10-22):** the file changed. `~/.agents/AGENTS.md`
measures 14 lines / 949 B (sha256 `7b06a503…`), its first line is
`# Operator tooling directive — 2026-10-19`, and none of the quoted posture text
survives (`name the axes` 0 hits, `iterate cheap in parallel` 0, `no worktrees`
0). Line 5 now sends the reader to `~/.omp/agent/RULES.md` before any install, so
"zero procedures" no longer holds of it: it carries a cross-file procedure
pointer and a dated heading. The delegated instrument's verdict on that
directory, run 2026-10-22: `verify_alwayson.py --check alwayson.04 --target
~/.agents` → `FAIL ... AGENTS.md:1 ISO date/timestamp '2026-10-19'`, exit 1.
`~/.agents` has no VCS, so the round-6 bytes are not recoverable; this is a
re-measurement, not a diff. The sibling family is 17 files, not 6 — the row
above carries the split.

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
