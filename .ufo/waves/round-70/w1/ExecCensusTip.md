# ExecCensusTip — round 70 wave 1 (executor, census + id collision at the measured tip)

**Verdict: PASS (census), with one forward-hazard finding (id collisions grow 6 → 9 at the tip).**
Both `validate` runs exit 0 with 0 E-codes and 18 W04 rows, line-for-line identical to
`receipts/census-before.txt`. Registry rows went from 134 at the base to 137 at the tip (S209–S211 added),
and the new rows add no W04. Re-running the plan's id-collision procedure reproduces the committed base
numbers exactly (134 / 188 / 6). At the tip, though, the set is **9**: the lane's new S209/S210/S211 reuse
three ids that the staged package assigns to *different* documents, and the lane does not record this.

Scratch: `/tmp/k70w1-ExecCensusTip.T8Pl` (deleted before return). No lane file written except this report.
No tools installed or updated.

## Setup

```
git clone -q --shared /home/vgpnk/Projects/shokunin/kotoba-shokunin lane && cd lane && git checkout -q 16b212a390c7ce68b6bce49b2c3766b154fbcbae
head=16b212a390c7ce68b6bce49b2c3766b154fbcbae tree=5ac2e8feff0681919665f49624867176cf336299   (git status --porcelain: 0 lines)
sha256 SKILL.md          9d2379bd…ad5c  (= git show 16b212a3:SKILL.md)
sha256 corpus/SOURCES.md 1f8f649d…602d  (= lane working tree corpus/SOURCES.md; no drift vs tip)
sha256 scripts/sources-census.sh 3fb72615…4e30
```

The clone carries `SKILL.md` at its root next to `corpus/`, so `E11` used-by paths resolve as they do in the lane.

## 1. Census validate

| run | command | exit | W04 | E-codes | W01–W03 | stderr |
|---|---|---|---|---|---|---|
| sandbox tip | `sources-census.sh validate --file <sandbox>/lane/corpus/SOURCES.md` | 0 | 18 | 0 | 0 | 0 B |
| lane, read-only | `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` | 0 | 18 | 0 | 0 | 0 B |
| mirror (corpus/ + SKILL.md only) | `validate --file <scratch>/mirror/corpus/SOURCES.md` | 0 | 18 | 0 | — | — |
| control: mirror **without** SKILL.md | `validate --file <scratch>/noskill/corpus/SOURCES.md` | **1** | 18 | 11 × E11 (`S002 missing used-by SKILL.md`, …) | — | — |

The control shows that copying SKILL.md alongside is load-bearing. This matches the first-attempt note in
`assimilation/census-validate-append.txt`.

**W04 comparison:** I ran `grep $'\tW04\t' <out> | cut -f2-` on each output and diffed it against the same
slice of `.ufo/waves/round-70/receipts/census-before.txt` (18 rows: S018, S019, S021, S054, S055, S056, S065,
S086, S103, S104, S106, S110, S111, S114, S115, S118, S207, S208). Both diffs printed `identical`. S209–S211
add no W04 rows.

**Row counts:** I ran `sources-census.sh census --file …`. At the tip it reports `rows 137` (tier A 129, B 7,
C 1; mined 129, queued 7, rejected 1; missing 0; exit 0). At the base it reads `53de0ac:corpus/SOURCES.md`
and reports `rows 134`, which matches the plan's "Census before … 134 rows" (`plans/round-70.md:104`).

## 2. Id collision check (plan procedure, `plans/round-67.md:131-134` pattern, re-run in scratch)

```
PAT='^ {0,3}\|[[:space:]]*S[0-9]{3,}'
grep -oE "$PAT" <SOURCES> | grep -oE 'S[0-9]+' | sort -u   # reg-ids
grep -oE "$PAT" /home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md | grep -oE 'S[0-9]+' | sort -u   # staged-ids (read-only)
comm -12 reg-ids staged-ids
```

| set | count | vs committed `assimilation/` file |
|---|---|---|
| reg-ids at base `53de0ac` | 134 | `diff` → identical to `reg-ids` |
| staged-ids | 188 | `diff` → identical to `staged-ids` |
| collisions at base | 6: S203 S204 S205 S206 S207 S208 | matches `collisions` and `corpus/lessons/round-70.md:38-40` |
| reg-ids at tip `16b212a3` | 137 (`comm -13` base→tip: S209 S210 S211) | — |
| **collisions at tip** | **9: S203 … S208, S209, S210, S211** | not recorded anywhere in the lane |

**Guard proof (re-run):** the fixture `  | S234 | indented |` produces 1 collision (`S234`) under the 0–3-space
pattern. The column-zero pattern counts 0 rows on the same file. This reproduces
`assimilation/guard-proof/`.

**Finding F1 — S209–S211 now collide with staged ids that name different documents.** I ran
`grep -nE '^ {0,3}\| *S2(09|10|11|31|34) \|' merge/kotoba/SOURCES.append.md`:
- staged S209 = ManyIH, arXiv 2604.09443 (line 13)
- staged S210 = SkillRouter, arXiv 2603.22455 (line 14)
- staged S211 = SkillsBench, arXiv 2602.12670 (line 15)
- staged S231 / S234 = the two agentskills.io pages, now lane S210 / S209

The renumber was correctly done by document (`corpus/lessons/round-70.md:43-47`), and the lane ids are the
authoritative ones. However, it put the lane rows on ids the package already uses for other documents. Any
later assimilation from this package must renumber staged S209–S211 too. Staged S209 (ManyIH) is already in
the lane as **S129**, so that one is a duplicate by document, not a new row. SkillRouter and SkillsBench
match no lane row; I checked with `grep` for the arXiv ids over the tip `corpus/SOURCES.md`.
`git grep` over `16b212a3` for `staged S209|S210|S211` and the three paper names finds no lane record of the
tip-time collision set; the only hits are in round-63/67 artefacts. This finding is not a C1 or C2 item, and
neither counter reads it. It is an operability and consistency hazard for the next assimilation round, and
I am routing it to the L1 rather than remediating it.

## Risks / unobserved

- The `--root` run reads the lane working tree. Its `corpus/SOURCES.md` sha equals the tip blob, but I did
  not hash the other working-tree files that E11 resolves.
- I ran no counters (C1/C2) and no no-harm battery; that is outside this seat.
