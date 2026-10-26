# ExecIdsR74 — assimilation scratch pipeline (kotoba round 74, wave 1)

**Verdict: PASS for the assigned scratch pipeline.** All four assignment legs ran on
committed bytes and the staged package: the collision/id lists were re-derived
byte-identically, the 0–3-space guard was proven on a census-valid indented row, the
three staged pages were renumbered by document (S232→S223, S237→S224, S236→S225) and
normalised to 11 columns in scratch, a lane mirror validated at exit 0 while a
duplicate-id mutant and a 10-cell mutant exited 1, and `append_rows.py` composed the
append block both from my draft rows and from the three real `ExecSrc*R74` rows. No
lane file was modified (`git status --porcelain` shows untracked wave evidence only,
`^ M` count 0), nothing was appended to the live registry, and nothing under
`/home/vgpnk/Projects/shokuknow` was written.

Base: lane tip `1e03d1991bc02281b00a5b7a5e00c9d5d5d72908`, frozen plan commit
`329e7d91d7d750031c35d264f0e34af1d0ce8385`.

## 1. Id lists re-derived, byte-identical

```
$ grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' <lane>/corpus/SOURCES.md | grep -oE 'S[0-9]+' | sort
$ grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' /home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md | grep -oE 'S[0-9]+' | sort
$ comm -12 reg-ids staged-ids > collisions
$ cmp -s <derived> <committed>   # per file
```

Observed (`id-lists-rederivation.txt`):

```
reg-ids: byte-identical to committed (148 lines)
staged-ids: byte-identical to committed (188 lines)
collisions: byte-identical to committed (20 lines)
quarantine-slice: byte-identical to committed (13 lines)
reg-ids highest: S222
staged-ids highest: S390
collisions: S203 S204 … S222
```

The stage of the plan commit is therefore reproducible from the live bytes; the
collision set is exactly `S203`–`S222` (20 ids), and the next free lane id is `S223`.

## 2. Guard proof (once) — indented rows are real registry rows

Fixture `assimilation/guard-proof/registry-scratch.md` carries one column-zero row
(`S233`) and one one-space-indented row (` | S234 | indented |`). Observed
(`guard-proof/guard-proof.txt`):

```
$ grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' registry-scratch.md
2
$ grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' … | grep -oE 'S[0-9]+' | sort
S233
S234
$ grep -oE '^\|[[:space:]]*S[0-9]{3,}' … | grep -oE 'S[0-9]+' | sort   # column-zero-only
S233
0-3-space collisions: 1 -> S234
column-zero-only collisions: 0 (empty = misses the indented collision)
```

The real parser agrees the indented fixture is a valid registry:

```
$ scripts/sources-census.sh validate --today 2026-10-25 --file …/guard-proof/registry-scratch.md
file	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-74/assimilation/guard-proof/registry-scratch.md
validate --file exit=0
```

So a column-zero-only extractor would false-green an indented collision; the frozen
0–3-space pattern is required and was used for every count in §1.

## 3. Renumber map — by document (URL), not arithmetic

Order rule: **one id per document URL, keyed by URL, assigned in byte-ascending URL
order starting at lane-highest+1 (`S222` → `S223`).** Staged ids are metadata; no id is
computed from another id, so re-pointing one citation cannot shift the next.

| document (URL) | staged | new |
|---|---|---|
| `agentskills.io/skill-creation/best-practices.md` | S232 | **S223** |
| `agentskills.io/skill-creation/quickstart.md` | S237 | **S224** |
| `agentskills.io/skill-creation/using-scripts.md` | S236 | **S225** |

Emitted by the tool (`renumber-map.tsv`, `append-rows-test.txt` §1):

```
https://agentskills.io/skill-creation/best-practices.md	S232	S223
https://agentskills.io/skill-creation/quickstart.md	S237	S224
https://agentskills.io/skill-creation/using-scripts.md	S236	S225
```

The three rows sit at `SOURCES.append.md:36` (S232), `:40` (S236), `:41` (S237); each
was extracted with `sed -n '<line>p'` and carries 11 cells in the campaign schema.

## 4. Normalised rows and stripped prose

Draft rows: `rows/best-practices.md`, `rows/quickstart.md`, `rows/using-scripts.md`
(one line each, 11 cells, no escaped pipe, no cell pipe; `awk -F'|'` → `cells=11`).
Normalisation applied per the assignment: `recheck: 90d`, `opened: 2026-10-25`,
`used-by: corpus/knowledge/spec-skill-creation-craft-round74.md`, `status: mined`
(written only in the final mirror, where the entry exists), anchor rewritten in this
seat's words. `S232`'s anchor carries my own located quote from the fetched page:
line 96 of my fetch reads, in full, `Not every part of a skill needs the same level of
prescriptiveness. Match the specificity of your instructions to the fragility of the
task.`; the row quotes only the second sentence (13 words) and names the dropped
prefix. `S236`/`S237` keep the assigned `<<located by ExecSrc*R74>>` placeholder.

Stripped staged prose (campaign recheck conditions and the two Gate pointers
`spec-description-trigger-discipline.md`, `spec-script-craft-rules.md`) is recorded in
`assimilation/gate-notes.md`, not in any row cell.

## 5. `append_rows.py` — the append-block tool

`build/ExecIdsR74/append_rows.py` takes one row file per page and `--start-id`, orders
rows by the URL in the `source` cell, assigns sequential ids, and emits the Registry
append block. It gates 11 cells, no `\|`, no cell pipe, `S<next>`/`S[0-9]{3,}` ids, and
the census enums (kind/tier/status/opened/recheck, E05–E09), and refuses a duplicate
document URL. Tests (`append-rows-test.txt`):

```
## 1. draft rows (strict one-line mode), start id 223
exit=0                                # block + renumber-map.tsv as above
## 2. real seat rows, strict mode
append_rows: …ExecSrcQuickstartR74/row.md: expected exactly one non-empty line, got 22
exit=2
## 3. real seat rows, --allow-prose
append_rows: … recheck '90d — re-fetch the `.md` and confirm the' is not an ISO date,
NNd, or symbolic cadence (use --normalize-recheck to strip trailing prose)
exit=2
## 4. real seat rows, --allow-prose --normalize-recheck --status mined
exit=0
```

The three real seat rows landed mid-run (22:37–22:38) and were snapshotted before
testing: `ExecSrcBestPracticesR74/row.md:1` (11 cells, `S223`, `queued`, `90d`),
`ExecSrcQuickstartR74/row.md:11` (11 cells, `S<next>`, `queued`, recheck prose),
`ExecSrcScriptsR74/row.md:8` (11 cells, `S<next>`, `mined`, `90d`). Their composed
block is `append-block-final.md`; every rewrite is logged:

```
https://agentskills.io/skill-creation/best-practices.md	status	queued	mined
https://agentskills.io/skill-creation/quickstart.md	recheck	90d — re-fetch …	90d
https://agentskills.io/skill-creation/quickstart.md	status	queued	mined
```

Final block cells (`awk -F'|'`): ids `S223`/`S224`/`S225`, all `status=mined`,
`opened=2026-10-25`, `recheck=90d`, `used-by=corpus/knowledge/spec-skill-creation-craft-round74.md`,
11 cells each, 0 escaped pipes.

## 6. Mirror gate and mutants

Mirror = copy of `corpus/` + `SKILL.md` + the append block in the Registry table + the
stub entry at `corpus/knowledge/spec-skill-creation-craft-round74.md` (scratch only,
`/tmp/k74w1-ExecIdsR74.bC5h/`). Observed (`mirror-census-transcript.txt`):

```
$ scripts/sources-census.sh validate --today 2026-10-25 --file …/mirror/corpus/SOURCES.md
file	ok	…/mirror/corpus/SOURCES.md
exit=0                                  # 20 W04 warnings, same set as the lane
$ … --file …/mirror/corpus/SOURCES.dup-id.md      # one extra row reusing S223
file	E03	S223 duplicate id
exit=1
$ … --file …/mirror/corpus/SOURCES.10col.md       # one extra row, used-by dropped
file	E01	S226 fields=10
exit=1
```

The mirror with the block composed from the real seat rows also validates at exit 0
(`mirror-final-census.txt`: `file ok`, 151 registry rows, W04 warnings only).

**Pipeline defect found and recorded:** the addendum's minimal mirror (copy of
`corpus/` only) is not enough — 11 pre-existing rows name `SKILL.md` in `used-by`, so a
corpus-only mirror exits 1 with `E11 … missing used-by SKILL.md`
(`mirror-census-missing-skill-md.txt`, E11 count 11). Copying the lane's `SKILL.md` into
the mirror root is required for a green scratch gate. This is a fact about the mirror,
not about the registry.

## 7. Source opening and the quarantine rows

Own fetches (`curl -sL --max-time 60 -A 'Mozilla/5.0'`, access date 2026-10-25), saved
raw under `snapshots/` with `fetch-log.tsv`:

| URL | HTTP | bytes | sha256 |
|---|---|---|---|
| https://agentskills.io/skill-creation/best-practices.md | 200 | 15 060 | `ab9f3b6091a0f24816b52cd7b90a3fdf53e621f47dba13b36694be272b87fb41` |
| https://agentskills.io/skill-creation/using-scripts.md | 200 | 12 078 | `2cd7727106b423a758b4b6b1ab3545da74845a98e68e6718279846f89d62ad1f` |
| https://agentskills.io/skill-creation/quickstart.md | 200 | 4 080 | `7c480b447edac58fd8ff8f250c471dfc7d4621155b91fabed46379075c32bffb` |

`S236` and `S237` are in the lane's quarantine slice with the register's prose class
"the cited source could not be fetched". My hand-check fetched both at HTTP 200 and the
byte counts equal the staged size cells (12 078 B, 4 080 B), so the absence is stale as
of 2026-10-25 rather than a fabrication class. Per the assignment the draft rows keep
the `<<located by ExecSrc*R74>>` placeholders, and the landed seat rows supply the
located anchors; gate-notes records my own located lines as cross-check only
(`using-scripts.md:50`, `quickstart.md:21`).

## 8. Files written (all untracked wave evidence; no tracked lane file touched)

- `assimilation/guard-proof/{registry-scratch.md,guard-proof.txt,reg-ids-0-3space,reg-ids-column-zero,staged-scratch-ids.txt,staged-ids-scratch,collisions-0-3space,collisions-column-zero}`
- `assimilation/gate-notes.md`
- `w1/build/ExecIdsR74/append_rows.py`, `append-block.md`, `append-block-final.md`
- `w1/build/ExecIdsR74/renumber-map.tsv`, `renumber-map-final.tsv`, `normalization-log.tsv`
- `w1/build/ExecIdsR74/rows/{best-practices,quickstart,using-scripts}.md`
- `w1/build/ExecIdsR74/snapshots/{best-practices,using-scripts,quickstart}.md`, `fetch-log.tsv`
- `w1/build/ExecIdsR74/{id-lists-rederivation.txt,append-rows-test.txt,mirror-census-transcript.txt,mirror-census-missing-skill-md.txt,mirror-final-census.txt}`
- this report: `w1/ExecIdsR74.md`

No tool installs. `/tmp/k74w1-ExecIdsR74.bC5h` (scratch mirror, mutant files, row
snapshot, bad-row fixture) was deleted after the evidence above was copied out.

## 9. Risks and handoff

- **Append source:** use `append-block-final.md` (the seat rows that located quotes),
  not the placeholder draft `append-block.md`; the draft exists to pin the normalised
  shape. Re-running the tool with `--rows-dir w1/build` at append time picks up any
  later edits to the three `row.md` files.
- **Status flips:** two seat rows were `queued`; the final block's `mined` is justified
  only once the entry exists at the cited path (logged in `normalization-log.tsv`).
- **Placeholders:** `S224`/`S225` anchors in my draft are intentional placeholders;
  they must not be appended as-is if the seat rows change.
- **Quarantine:** the register still calls S236/S237 unfetchable; the lane lesson's Gate
  block should record the 200-status fetch and the byte-count equality so a later
  reviewer can see why adoption rests on the seat rows' located quotes.
- **Checks the L1 should run:** the lane census at the landing tip
  (`scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`,
  exit 0), `append_rows.py --rows-dir … --allow-prose --normalize-recheck --status mined`
  on the final seat rows, and the mirror gate above after any further row edit.
