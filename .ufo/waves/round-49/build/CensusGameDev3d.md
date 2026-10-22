ROW | game-dev-3d | main | 89dd182b70943a20ae9aa6c1ed0e3c9b6e79c080 | SKILL.md | none | no | yes | PROVINCE.md:3-5 | "Owns: 3D game production verified by executable headless fixtures — 3D movement and collision, spatial queries, camera projection and frustum behavior"

# game-dev-3d — C1 adjacency census

## Findings

**Classification: `none`.** The sibling's declared province is 3D game
production, not skill/prompt craft. Its scope-defining files never name kotoba,
declare no surface overlapping kotoba's Core (SKILL.md craft, AGENTS.md-class
and dispatch-prompt craft, instruments over those surfaces), and claim no
authorship or audit role over another lane's skill, prompt or always-on file.
The `none` sweep below returns 12 matching lines, every one of which is either
about the sibling's **own** `SKILL.md` or ordinary English in a domain sense
(`getter-trigger ordering`, `structural description`).

**Frontmatter description names kotoba: no.** The `description` (SKILL.md:3)
names two siblings — `game-dev-2d-shokunin` as anti-trigger and `revenger-shokunin`
as anti-trigger — and no third lane.

**Arbitration clause: yes, but not against kotoba.** SKILL.md:3 carries
"Sibling arbitration: 2D fixture patterns are inherited, 2D product surfaces are
not; contested scope is reported per `PROVINCE.md`, never absorbed." It
arbitrates against `game-dev-2d-shokunin` (2D). PROVINCE.md restates the same
clause in its Refuses list ("2D production scope (game-dev-2d — shared fixture
patterns are inherited, 2D product surfaces are not)"). kotoba is not mentioned.

**PROVINCE.md names kotoba: no.** `git show <pin>:PROVINCE.md | grep -c kotoba`
→ `0`. Its `## Adjacent` section (PROVINCE.md:72-78) names exactly five lanes:
`game-dev-2d`, `mado`, `kumitate`, `kengaku`, `revenger`. kotoba is not among
them, and kotoba's own `## Adjacent` does not name game-dev-3d either — the
non-overlap is symmetric, both directions.

**Refusal shape is adjacent-*different*, not adjacent-*shared*.** PROVINCE.md
refuses "harness/evidence auditing (harness-integrity, gate-evidence,
rlm-dispatch)". That is an **evidence**-audit refusal; it neither claims nor
refuses **craft** audit, and it is not the half kotoba owns (kotoba owns
SKILL.md/prompt/AGENTS.md craft and its instruments). No contested half exists.

### Why the two report-level touch points do not upgrade this to `adjacent`

Only 2 of 23,564 tracked files at the pin contain "kotoba" at all, both under
`reports/`:

1. `reports/round-101/r101-scout-roster.md:106` — a demand-routing roster that
   **rejects a demand away from kotoba**, quoting kotoba's own boundary
   (`SKILL.md:8-9`, `SKILL.md:447-448`) and its province sha256. This is
   read-only deference to kotoba's rule, the opposite of a claim on it.
2. `reports/round-104/skill/bleed.md:139` — a fleet loop
   `for f in /home/vgpnk/Projects/shokunin/*-shokunin/SKILL.md; grep -c 'Rank: shonen'`
   in which `kotoba-shokunin` scores `1`. This measures the sibling's own
   compliance with a fleet convention and files its own miss as "a convention
   gap, not a bleed"; the seat declares its only written path is its own report
   and no `SKILL.md` byte is written by it.

The same seat audits the sibling's **own** `SKILL.md` for frontmatter accuracy,
cross-domain bleed and PROVINCE consistency — a per-lane self-audit, not a fleet
census and not an audit of another lane's file. `reports/round-101/probes/skill-frontmatter.md`
parses frontmatter of the **vendored Epic plugin** SKILL.md files inside its own
`corpus/knowledge/unreal-mcp/upstream/` — domain content it owns and kotoba
explicitly refuses. Neither acts on kotoba's half, so neither reaches the
`adjacent` bar (shared boundary, each owning a different half).

## Evidence (all read-only, from the pinned commit)

Pin (branch `main`; `master` does not exist — `rev-parse master` rc 128,
`symbolic-ref -q HEAD` → `refs/heads/main`):

```
$ git -C …/game-dev-3d-shokunin rev-parse refs/heads/main
89dd182b70943a20ae9aa6c1ed0e3c9b6e79c080                          rc 0
$ git -C … rev-parse HEAD → rc 0, same 40-hex; rev-parse HEAD refs/heads/main | uniq | wc -l → 1 (HEAD == main)
```

Top level at the pin (`ls-tree --name-only`, rc 0): `AGENTS.md LOG.md PROVINCE.md
README.md SCORECARD.md SHONEN.md SKILL.md considerthese corpus reports` — `considerthese` is a tree holding one file, `2026-10-20.md`.

Skill files (`ls-tree -r --name-only <pin> | grep -E '^(skills?/[^/]+/)?SKILL\.md$'`,
rc 0): **`SKILL.md`** at the repo root. All `SKILL.md` in the tree: **7** —
the root file plus 3 vendored under `corpus/knowledge/unreal-mcp/upstream/skills/`
and 3 identical copies under `reports/round-104/gate/scratch/c85a816/…`
(byte-identical sizes: 23258/7098/6955).

```
$ git -C … show <pin>:SKILL.md   | wc -c → 25541
$ git -C … show <pin>:PROVINCE.md | wc -c → 7467
$ git -C … show <pin>:AGENTS.md  | wc -c → 3925   (Cursor-provider lane runbook)
$ sha256: SKILL.md f52b988afaa03bf4f47ed2e1501dbdccc2796ef6eda35bed032c4cafd51784ea
           PROVINCE.md dd8b032814479bdd6811f6b18fef814e21c5e35cbc3093814fa8d9531d8817ff
           AGENTS.md dc25e81737dac3de8f82934ecb0540a143700dc5cf8237c1e409adf1efd6b706
```

kotoba mentions, whole tree:

```
$ git -C … grep -l -i kotoba <pin> -- . | wc -l → 2
  reports/round-101/r101-scout-roster.md   (1 line)
  reports/round-104/skill/bleed.md         (1 line)
$ for f in SKILL.md PROVINCE.md README.md AGENTS.md SHONEN.md SCORECARD.md LOG.md; \
    do git -C … show <pin>:$f | grep -c kotoba; done → 0 0 0 0 0 0 0
$ git -C … show <pin>:considerthese/2026-10-20.md | grep -c kotoba → 0
```

`none` sweep (the required command form; line counts, `grep -Ec`):

```
$ for f in SKILL.md PROVINCE.md README.md AGENTS.md SHONEN.md SCORECARD.md LOG.md \
           considerthese/2026-10-20.md; do \
    git -C … show <pin>:$f | grep -Ec 'SKILL\.md|prompt|AGENTS\.md|frontmatter|trigger|description|kotoba'; done
SKILL.md 2 | PROVINCE.md 0 | README.md 1 | AGENTS.md 0 | SHONEN.md 0 | SCORECARD.md 2 | LOG.md 7 | considerthese 0
$ (same 8 files concatenated) | grep -Ec '…' → 12
```

Match inspection (`grep -nE`, rc 0): SKILL.md:3 (its own `description`),
SKILL.md:49 (row D "structural description"); README.md:12 (its own `SKILL.md`
summary); SCORECARD.md:328,336 (its own SKILL.md landed/coverage ledger);
LOG.md:787 `getter-trigger ordering`, 1384 `structural description`, 1411/1418/
1430/1433/1451 (its own SKILL.md landings). No line names kotoba, another
lane's SKILL.md, a prompt, or an AGENTS.md it authored.

Sibling-lane names in scope files (`grep -oE '\b(<lane>)-shokunin\b' | sort | uniq -c`):

```
SKILL.md    → 1 game-dev-2d-shokunin, 1 revenger-shokunin
PROVINCE.md → 3 kengaku-shokunin, 3 kumitate-shokunin, 2 mado-shokunin
AGENTS.md   → (none)      README.md → (none)
```

## Quotes (verbatim at the pin)

Scope, `PROVINCE.md:3-5` (21 words): "Owns: 3D game production verified by
executable headless fixtures — 3D movement and collision, spatial queries,
camera projection and frustum behavior".

Arbitration clause, `SKILL.md:3` (excerpt): "Sibling arbitration: 2D fixture
patterns are inherited, 2D product surfaces are not; contested scope is reported
per `PROVINCE.md`, never absorbed." — arbitrates `game-dev-2d-shokunin`, not kotoba.

Self-audit bound, `reports/round-104/skill/bleed.md:1-4`: "Owned path written:
`reports/round-104/skill/bleed.md` (this file only). No `SKILL.md` byte … was
written or modified." — the seat bounds itself to its own report and extends no
craft authority over other lanes.

## Remaining unknowns

- No `lsp` server applies to a read-only Markdown sibling repo, so every claim is
  git-object evidence (`git show <pin>:<path>`), not semantic resolution; grep is
  used for counts only and the classification rests on the read scope files.
- kotoba's Core and `## Adjacent` were read from the lane working tree (read-only),
  not a pinned kotoba commit; the lane's own pin is the L1's to record.
- No tool installs or upgrades were needed for this seat (none performed).
