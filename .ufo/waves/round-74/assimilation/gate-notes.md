# Assimilation gate notes — round 74, seat ExecIdsR74

Scope: the three staged `agentskills.io/skill-creation/` rows of the read-only package
`/home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md` (staged `S232`
best-practices, `S236` using-scripts, `S237` quickstart), normalised to the lane's
11-column registry schema in scratch. Nothing was appended to the lane registry; the
staged package was never written.

## Renumber map — by document, not arithmetic

Order rule: **one new id per document URL, the URL is the key, and the sequence follows
byte-ascending URL order** (ASCII/UTF-8) starting at the lane's highest id + 1
(`S222` at base `1e03d19`). The staged ids are metadata; no id is derived from another
id's arithmetic, so re-pointing one citation can never shift the next.

| document URL | staged id | new id |
|---|---|---|
| https://agentskills.io/skill-creation/best-practices.md | S232 | S223 |
| https://agentskills.io/skill-creation/quickstart.md | S237 | S224 |
| https://agentskills.io/skill-creation/using-scripts.md | S236 | S225 |

The same map is emitted by `append_rows.py --start-id 223 --map renumber-map.tsv` from
the three draft row files (evidence:
`.ufo/waves/round-74/w1/build/ExecIdsR74/renumber-map.tsv`). The mirror's stub entry
cites S223/S224/S225 next to their URLs, so every citation follows its document.

## Normalisation applied to all three rows

| cell | staged | normalised |
|---|---|---|
| anchor | long campaign prose with quoted passages and `\n`-free bold markup | rewritten in this seat's words; the located quote for S223 is mine (fetch below); S236 and S237 carry `<<located by ExecSrc*R74>>` |
| recheck | `90d — <re-verify prose> (ran 2026-10-23)` | `90d` |
| opened | `2026-10-23` | `2026-10-25` (this seat's access date) |
| used-by | campaign entries `spec-description-trigger-discipline.md` / `spec-script-craft-rules.md` | `corpus/knowledge/spec-skill-creation-craft-round74.md` |
| status | `mined` | `mined` |

`status: mined` is written **only** in the final mirror, where the cited entry exists
(the mirror carries the stub at the repo-relative path, so census `E11` resolves). No
row with this status was added to the live registry by this seat.

## Stripped staged prose (kept here, not in the row cells)

Campaign recheck cells, verbatim from `SOURCES.append.md` (line numbers in that file):

- S232 (line 36): `90d — re-fetch the `.md` and confirm the fragility-matching and
  procedures-over-declarations rules are unchanged (ran 2026-10-23)`
- S236 (line 40): `90d — re-fetch the `.md` and confirm the one-off-command list and the
  script-interface rules are unchanged (ran 2026-10-23)`
- S237 (line 41): `90d — re-fetch the `.md` and confirm the `.agents/skills/` default and
  the portability sentence are unchanged (ran 2026-10-23)`

Campaign Gate pointers stripped from `used-by`:

- S232 → `corpus/knowledge/spec-description-trigger-discipline.md` (campaign-side entry;
  its Gate is the campaign's access, not this lane's)
- S236, S237 → `corpus/knowledge/spec-script-craft-rules.md` (same caveat)

This lane's own Gate block must carry its own access date and located quote in
`corpus/knowledge/spec-skill-creation-craft-round74.md` (entry scribe) and in the round
lesson; these campaign cells prove nothing about this lane's access.

## Quarantine — S236 and S237

The lane's register slice (`assimilation/quarantine-slice`, re-derived byte-identically)
lists `S236` and `S237` with the prose class "the cited source could not be fetched, so
no quote was checked". Hand-check this round (seat ExecIdsR74, own fetch, 2026-10-25):

| url | HTTP | bytes | sha256 |
|---|---|---|---|
| https://agentskills.io/skill-creation/using-scripts.md | 200 | 12 078 | `2cd77271…` |
| https://agentskills.io/skill-creation/quickstart.md | 200 | 4 080 | `7c480b44…` |

Both payloads are **present now**, and both byte counts equal the staged size cells
(12 078 B and 4 080 B), so the register's absence is stale at fetch time rather than a
fabrication class. Per the seat assignment the anchor cells still say
`<<located by ExecSrc*R74>>`: the located quote is taken from the per-page ExecSrc row
(`ExecSrcScriptsR74/row.md`, `ExecSrcQuickstartR74/row.md`) when it lands, and no staged
quote is relied on. My own located lines for cross-check (not substituted into the row):

- `snapshots/using-scripts.md:50` → `* Pin versions with `npx package@version` for reproducibility.` (8 words)
- `snapshots/quickstart.md:21` → `A skill is a folder containing a `SKILL.md` file. VS Code looks for skills in `.agents/skills/` by default. ...` (23 words; the line continues with `Create `.agents/skills/roll-dice/SKILL.md` in your project:`)

## S223 located quote and dropped bytes

`snapshots/best-practices.md:96` reads in full:

```
Not every part of a skill needs the same level of prescriptiveness. Match the specificity of your instructions to the fragility of the task.
```

The row quotes the second sentence (`Match the specificity of your instructions to the
fragility of the task.`, 13 words) and names the dropped prefix: `Not every part of a
skill needs the same level of prescriptiveness.`

## Post-hoc — the three ExecSrc*R74 seat rows landed during this seat's run

The per-page seat rows appeared at 22:37–22:38 while this seat was testing, so the
appendable block is composed from them rather than from this seat's placeholder draft:

- `ExecSrcBestPracticesR74/row.md:1` — 11 cells, id `S223`, status `queued`, recheck `90d`
- `ExecSrcQuickstartR74/row.md:11` — 11 cells, id `S<next>`, status `queued`, recheck
  `90d — re-fetch …` (prose: not census-conformant until stripped)
- `ExecSrcScriptsR74/row.md:8` — 11 cells, id `S<next>`, status `mined`, recheck `90d`

`append_rows.py --allow-prose --normalize-recheck --status mined` turns them into
`.ufo/waves/round-74/w1/build/ExecIdsR74/append-block-final.md`; the rewrites are in
`normalization-log.tsv` (2 status flips `queued → mined`, 1 recheck prose strip for
quickstart). The final block validates at exit 0 in a scratch mirror
(`mirror-final-census.txt`: `file ok`, 151 rows, W04 warnings only). This seat's own
`rows/` draft remains the normalisation shape and keeps the S236/S237 placeholder
anchors, as the assignment required before the seat rows landed.

## Fetch evidence

`.ufo/waves/round-74/w1/build/ExecIdsR74/snapshots/fetch-log.tsv`; snapshots are the
raw `.md` responses (15 060 / 12 078 / 4 080 B, all ≤ 300 KB) with sha256 pins. The
staged cells' own byte counts (15 060 / 12 078 / 4 080) agree with the three fetches.
