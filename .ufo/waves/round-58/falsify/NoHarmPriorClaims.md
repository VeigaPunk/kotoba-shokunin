Result: MIXED — the four r54–r57 decision tables are byte-identical and the anatomy block moved verbatim, but "the only removed lines are the moved anatomy block" is literally false: four earlier-round base lines were also removed and re-added amended (3 path-case fixes, 1 gate-registry annotation).

# NoHarmPriorClaims — SKILL.md prior-claims diff, `f56f6e1` → `46b4a70`

Scope: `git --no-optional-locks diff f56f6e191762c27c1aa2af11a204db9e2ca4edec 46b4a7061c688cefd3e3ec9cbb655130ba1aafbe -- SKILL.md` (run in lane, read-only, `Fri 23 Oct 2026 08:26:14 AM UTC`). Stat: `1 file changed, 21 insertions(+), 23 deletions(-)`, 6 hunks. Diffs were enumerated with difflib opcodes over the two `git show` blobs (sha256 of full blobs: base `b2083523a3856c0c8c917fd90e9fe31092e201ab684e50c4d93f8e08ee572eb9`, content `18e0fde1abdb2a7a56e1fdcce18cd04bae4f35d78668ae2485dc36b653f9ada6`); every removed and inserted line was accounted for. Lane tip `8e52f064` `HEAD:SKILL.md` blob is byte-identical to `46b4a70:SKILL.md` (`18e0fde1…`); working tree clean for SKILL.md.

## 1. Protected decision tables — byte-identical (HOLDS)

Section = heading through the line before the next heading of same-or-higher level; table = the contiguous `|`-line run inside it. sha256 over exact bytes:

| Section | base lines | content lines | section sha256 (both revs) | table-only sha256 (both revs) |
|---|---|---|---|---|
| `### Agent-definition files by client` | 97–110 | 79–92 | `d58286428094f8a5ffa173ef3c32d02cab48dcc30056aa0df24e30f16caf17eb` | `cbd3caf444ae01e39ad5effa6c68c039e9e55053a1098918600acfedb5c34978` |
| `### Plugin manifests by client` | 111–124 | 93–106 | `47c97b3a5a84d4282e4c2203895183e6bceb518052da68b37caa67151542f1a7` | `035beee42ff14e8329f0adf3d3c46152cf5f57d5f0c2d5f74ad94a8f4329a986` |
| `### Description thresholds by client` | 189–202 | 185–198 | `5f9e9b43e166e36640f72e7c7ba3b80130702a1c6aea44f9bf2cdb66335b3b64` | `318f6f1177708dd8b23ce9661dbc2c71cb76910582236941f4aa345b105d46bc` |
| `### Explicit invocation by client` | 203–218 | 199–214 | `2a5639557b175183e607e851f87c8fd8dbc2db7ef816c4bb3567d6437cfd1638` | `fa69f3512897d5c8bc1fdcdff4cf02a6cf23373526d19229faee5f58d8c7d013` |

Line shifts are pure displacement: −18 above the insert point (the 19-line anatomy block collapsed to a 1-line pointer) and −4 below it (the 14 inserted C1 lines offset). The new `### Custom command files by client` was inserted as a sibling *after* `### Plugin manifests by client` (content 106–119; the block's trailing blank at 120 is shared context with `## Router model` at 121), touching zero base lines. The two added gate-registry rows (content 450, 465) sit below all four protected tables and do not affect their offsets.

## 2. Removed lines — literal claim BREAKS (Low, wording defect)

There are **zero pure deletions** in the diff: all 23 removed lines appear in `replace` opcodes. 19 are the anatomy block (base 58–76 → one pointer line at content 58). The other **four base lines were removed and re-added amended**:

| base line | content line | change | routed repair |
|---|---|---|---|
| 353 `form: \`/home/vgpnk/projects/…\`` | 349 | `projects` → `Projects` only | R5 paths |
| 460 `\| check_infoless_fences.py … 2=could-not-evaluate \|` | 457 | appends ` — claim withdrawn r57; not a claim gate until redesigned and re-controlled` in the exit-code cell | R1 registry annotation |
| 514 `- \`/home/vgpnk/projects/…/*-L1.md\`` | 512 | `projects` → `Projects` only | R5 paths |
| 516 `- \`/home/vgpnk/projects/…/*-round-*.md\`` | 514 | `projects` → `Projects` only | R5 paths |

Char-level ndiff confirms the three path lines differ only in `p`→`P` case and the registry row only in the appended annotation. All four are earlier-round landed lines; the two gate-registry rows added (content 450 `check_command_files.py`, 465 `check_sweep_mutants.py` + the amended 457) likewise mutate an earlier-round landed table — all are named routed repairs (R1/R5), so this is a wording defect in the claim, not undisclosed harm. If "no-harm" was meant as "no earlier landed line changed at all except the anatomy move", that is false. If meant as "no earlier landed line dropped without replacement / no protected decision table touched", that holds. Suggested honest phrasing for the L1's claim: *"the only removed lines are the moved anatomy block plus four lines re-added verbatim except R5 path-case (`projects`→`Projects`, 3 lines) and the R1 withdrawn-claim annotation on the `check_infoless_fences.py` registry row (1 line); the four r54–r57 decision tables are byte-identical."*

## 3. Move fidelity — verbatim (HOLDS)

- Base `SKILL.md:58–76` == `corpus/knowledge/anatomy-and-compression.md:122–140` byte-for-byte: both hash `0a6a535e2a37145324ca42e39324715559e95b4c23cbfc3fa357bec55ff54e2d`.
- KB file diff base→content is append-only: `26 insertions(+)`, one hunk `@@ -114,0 +115,26 @@` adding `## Moved from SKILL.md § Skill-file anatomy (round 58)` (line 116), a 4-line provenance note (118–120), and the 19-line block (122–140). File predates round 58 (log shows round-5/round-15/round-57 history) — the move extends the existing convention, no earlier rows touched.
- Pointer line (content `SKILL.md:58`) names the correct path and anchor (`§ Moved from SKILL.md § Skill-file anatomy (round 58)` = KB line 116).
- KB note cites the block as "Verbatim from `SKILL.md` § Skill-file anatomy at `3de87aad` lines 58–76": verified — the block sits at exactly 58–76 in `3de87aad:SKILL.md` and is byte-identical to the base copy. Correct.

## 4. Inserts — all additions, no overwrites

16 pure inserts: the 15-line C1 section (content 106–120) and 2 gate-registry rows (450, 465). 21 total insertions = 16 inserts + 5 replacement new lines (1 pointer + 4 amended re-adds). ✓ reconciles with `--stat`.

## Residual risk / verification gaps

- Scoped to `SKILL.md` per item. Other earlier-round files the content commit touches (README rows, sources, registry, other corpus files) are sibling-seat territory — not covered here.
- sha256 section comparison is the semantic check this item names; no LSP applies (plain Markdown).
- The pointer line itself (content `SKILL.md:58`) is new prose, not verified against any frozen claim beyond what §3 covers.
