# MutCensusGuardBase — before-column mutation probe of the sibling-census content guard

**FAILS** — at `f30464660c675d1c1e2851a3bf0366a3aaffe5a8` the sibling-census content guard
(`verifiers/check_sibling_census.py`) does **not** reject duplicate rows: a duplicated census row, a
duplicated `PROVINCE.md` § Adjacent row and a consistent duplicate pair all exit **0**. The D3
duplicate-row check does not exist yet and is still needed; the case-variant duplicate is killed
only incidentally, by the sibling-repo directory lookup, not by a duplicate check.

- Lane: kotoba-shokunin, base `f30464660c675d1c1e2851a3bf0366a3aaffe5a8` (master).
- Scratch: `/fast/scratch/hyaku/kotoba-r50/build/MutCensusGuardBase/` — private clone `lane/` (at
  the base commit), harness `mutants.py`, full log `run-log.txt`, one directory per mutant under
  `mutants/`. The lane checkout was never written to except this report file.
- Detector: `python3 -B verifiers/check_sibling_census.py <census.md> --province <PROVINCE.md>`
  (exit 1 = killed, exit 0 = survived); `--fleet` defaults to `/home/vgpnk/Projects/shokunin`
  (20 sibling repos, read-only `git show` at the pinned commits).

Baseline on the pristine pair, in the clone (exit 0; the baseline is green, so every verdict below
is a real mutant verdict, not a broken detector):

    $ python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md
    rows 20 verified 20
    province rows 20 matched 20
    exit 0

## Results

| id | mutation | exit | verdict |
|---|---|---|---|
| M1 | duplicate one census row (kasegi, verbatim) | 0 | **SURVIVED** |
| M2 | duplicate one PROVINCE § Adjacent row (kasegi, verbatim) | 0 | **SURVIVED** |
| M3 | add a census row duplicating kasegi, lane cell case-varied (`Kasegi`) | 1 | killed (incidentally) |
| M3b | case-vary the existing kasegi census row's lane cell in place (`Kasegi`) | 1 | killed (incidentally) |
| M4a | swap the commit cells of the kasegi and kaidoku census rows (census only) | 1 | killed |
| M4b | swap those two commits in census **and** PROVINCE, consistently | 1 | killed |
| M5 | kasegi census row `adjacent`→`none`, PROVINCE row edited to match | 0 | **SURVIVED** |
| M6 | delete the kasegi row from the census table and from the PROVINCE table | 1 | killed |
| M7 | duplicate the kasegi row consistently in census **and** PROVINCE | 0 | **SURVIVED** |
| M8 | duplicate the kasegi census row at a different (older) kasegi commit, PROVINCE repointed there | 0 | **SURVIVED** |

## Evidence per mutant (verbatim guard output)

**M1 — duplicate census row — exit 0 — SURVIVED.** The census table is verified 21 times for 20
lanes; the extra row is re-read at its pinned commit and passes every content check.
`seen_lanes` is a set, so the duplicate lane is invisible to the lane-set check, and
`census_meta[lane]` is a dict, so the second row simply overwrites the first.
Output: `rows 21 verified 21` / `province rows 20 matched 20`.

**M2 — duplicate PROVINCE row — exit 0 — SURVIVED.** `province_lanes` is a set too, and the only
province count check is `len(rows) < len(expected)` (19 rows fails, 21 rows passes). The guard
prints a green line showing 21 rows for 20 lanes.
Output: `rows 20 verified 20` / `province rows 21 matched 21`.

**M3 — case-variant duplicate (`Kasegi`) — exit 1 — killed, but not by a duplicate check.** The
guard's own semantics are case-insensitive (`normalize_lane` lowercases; the label prints "lane
kasegi"), so the lane-set check sees 20 lanes and the province cross-check sees 20 matched. The
kill comes only from `repo_dir_for()` using the raw cell against a case-sensitive filesystem.
Output: `FAIL row 9 (census line 77) (lane kasegi): no sibling repo at
/home/vgpnk/Projects/shokunin/Kasegi-shokunin` / `rows 21 verified 20` / `province rows 20
matched 20`.

**M3b — case-variant rename in place — exit 1 — killed by the same filesystem lookup.** Note the
province line: the census row now reads `Kasegi` and PROVINCE reads `kasegi`, and the cross-check
still matches, because both sides are lowercased. The only kill is the directory name.
Output: the same `FAIL ... no sibling repo at .../Kasegi-shokunin` / `rows 20 verified 19` /
`province rows 20 matched 20`.

**M4a — commit swap, census only — exit 1 — killed** (both the pinned-bytes re-derivation and the
province commit cross-check fire):

    FAIL row 6 (census line 74) (lane kaidoku): git show 1fafde8f1145:SKILL.md in /home/vgpnk/Projects/shokunin/kaidoku-shokunin failed (fatal: path 'SKILL.md' exists on disk, but not in '1fafde8f11454f3b0b98ab7f2b2e640aaf7f399a')
    FAIL row 9 (census line 77) (lane kasegi): git show 08c7a7299ed6:PROVINCE.md in /home/vgpnk/Projects/shokunin/kasegi-shokunin failed (fatal: path 'PROVINCE.md' exists on disk, but not in '08c7a7299ed61c3fdc30ddb0adfe4e812d5eac76')
    FAIL province row 6 (line 16): lane kaidoku commit 08c7a7299ed6 does not match the census 1fafde8f1145
    FAIL province row 9 (line 19): lane kasegi commit 1fafde8f1145 does not match the census 08c7a7299ed6
    rows 20 verified 18
    province rows 20 matched 18

**M4b — commit swap in both tables — exit 1 — killed by the pinned-bytes re-derivation.** The
province cross-check alone passes here ("matched 20"); the kill is the guard re-reading the
sibling bytes at the pinned commit. A swap cannot be made to survive by editing both tables.
Output: the same two `git show ... failed` FAIL lines as M4a / `rows 20 verified 18` /
`province rows 20 matched 20`.

**M5 — non-`none` row downgraded to `none`, PROVINCE edited to match — exit 0 — SURVIVED.**
kasegi's adjacency rests on kotoba's own description, not on kasegi's bytes. The guard's `none`
arm fires only when the sibling's own `SKILL.md` description or `PROVINCE.md` at the pin names
kotoba; kasegi's do not (`git -C kasegi-shokunin show <pin>:PROVINCE.md | grep -ic kotoba` → 0),
so the downgrade is accepted. This is a gap in the classification judgement, not in the duplicate
rule. Output: `rows 20 verified 20` / `province rows 20 matched 20`.

**M6 — lane deleted from both tables — exit 1 — killed** (lane set + province row count):
`FAIL lane set: 1 sibling lane(s) never surveyed: kasegi` and `FAIL province: the `## Adjacent`
table has 19 row(s), fewer than the 20 sibling lane(s)` / `rows 19 verified 19` /
`province rows 19 matched 19`.

**M7 — duplicate row in both tables — exit 0 — SURVIVED.** A consistent duplicate pair is fully
accepted. Output: `rows 21 verified 21` / `province rows 21 matched 21`.

**M8 — duplicate row at a different pin — exit 0 — SURVIVED.** The second kasegi row carries the
older pin `c8b719d22882863ea7cd89b14c8bc078228001ed`, which still holds the same `PROVINCE.md:3`
quote and a description that does not name kotoba, so the row passes every content check; the
PROVINCE row is repointed to that pin and the cross-check passes against the last-written
`census_meta` entry. The census therefore records two pins for one lane and the guard is green.
Output: `rows 21 verified 21` / `province rows 20 matched 20`.

## Which survivors a duplicate-row check would kill

A per-table duplicate-row check on the normalized lane name would kill **M1, M2, M7 and M8** (and
M3, if it normalizes case — M3 is presently killed only by the filesystem, so a check on the raw
cell would leave the case-variant duplicate alive on a case-insensitive filesystem or if the repo
directory were renamed). It would **not** kill **M5**: that is a classification downgrade, not a
duplicate, and needs the D3 precedence rule plus a check that reads kotoba's own side (the
direction the planned `--skill` content guard takes). M5 is a known limit of a duplicate-row
check, not a miss of it. Shape for the D3 fix, from what the mutants show: build the lane set
while parsing and fail on a repeat of a normalized lane name, per table (census table and
PROVINCE `## Adjacent` table separately). A row-count check will not do it — 21 rows is currently
accepted and printed as a green line.

## Adjacent fact for the C1 build seat (not part of this probe)

The plan's Q25 content-guard command does not exist at this base commit:

    $ python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md --skill SKILL.md
    usage: check_sibling_census.py [-h] [--fleet DIR] [--province PATH] [--self-test] [census]
    check_sibling_census.py: error: unrecognized arguments: --skill SKILL.md
    exit 2

## Restoration evidence

Before hashes (clone at the base commit; the lane checkout at the same base has the same three):

    census   9c7d2f1649fff276a580be3a9ce9e99df8ab9841bac225dbe934fa02138cbf36
    province 2bbd759a03a7cfb233cfaef8ffee6cb07689a00be648d7f52b9038f4bc71a17f
    guard    3500508a86fdb30b84c9918b2157b2866d40d336f3114526f0cc11bab0495ea3

After the whole probe (the harness never writes to the clone's inputs; every mutant has its own
copy under `mutants/<id>/`): the same three hashes, unchanged. The lane checkout
`/home/vgpnk/Projects/shokunin/kotoba-shokunin` still carries them and `git rev-parse HEAD` =
`f30464660c675d1c1e2851a3bf0366a3aaffe5a8`; only this report file was written there. No git
write command and no jj command was run in the lane, the fleet repo or any sibling lane repo;
sibling repos were read with `git show` / `git log` only.

## Reproduction and tooling

    cd /fast/scratch/hyaku/kotoba-r50/build/MutCensusGuardBase
    python3 -B mutants.py        # prints the baseline and every mutant with its exit code

No tool was installed or upgraded by this seat (the probe needs only `git` and `python3`, already
on the host).
