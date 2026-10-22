# MutDuplicateRows — round-50 falsify: the duplicate-row mutants against the landed guard

**HOLDS-BOUNDED** — applies to the D3 repair (`corpus/lessons/round-50.md` § Routed defects: "the
guard now rejects a repeated lane in either table"; census entry § Round 50 D3: "the guard now fails a
lane that appears in more than one row of either table"). Every duplicate-row mutant the round-50 build
seat recorded (M1, M2, M3, M7, M8) is **killed** at `956ee167`, and so is the added `-shokunin`-suffix
duplicate (M9). The refusal is scoped to the two *named* tables, so a duplicate row planted in a
**second** table of the same shape in the same file still survives (M10, M11) — a bounded coverage gap,
not a contract miss. C1's own counter **HOLDS**: `skill description names 5 of 9 non-none lanes`
(exit 1) on the base files, `9 of 9` (exit 0) on the landed ones. The classification downgrade **M5
still survives**, and it does **not** fail via `--skill`. Every verdict is unchanged at the integrator's
two later landings (`a78fec1`, `bf109cac`); the guard file is byte-identical at all three revs
(`verifiers/check_sibling_census.py` sha256 `2f9d8a88…`).

## Findings

**F1 — the D3 duplicate-row refusal is real and kills every before-column duplicate mutant.** At
`956ee167` the guard refuses a repeated lane, per table, on the normalized lane name (case-insensitive,
`-shokunin` suffix dropped). Before (`f304646`, before-column `MutCensusGuardBase.md`): M1, M2, M7, M8
exited **0**. After: all exit **1**, the refusal printed before any row is verified, so it does not
depend on the duplicate row's other cells. M3 (`Kasegi`) is no longer killed *only* incidentally: the
duplicate refusal now fires as well as the filesystem lookup, so the case-variant duplicate is dead on a
case-insensitive filesystem too. M9 (lane cell `kasegi-shokunin`) is killed by the same refusal, and its
`repo_dir_for` lookup still resolves — a principled kill, not an accident.

**F2 — M5 does not fail via `--skill`. Answer: no.** M5 (kasegi's census row `adjacent`→`none`, with
the PROVINCE row edited to match) exits **0** on both detectors. The `--skill` arm reads the census's
classification map and requires every **non-`none`** lane to be named in the description; downgrading
kasegi removes it from the required set, so the arm prints `skill description names 8 of 8 non-none
lanes` and passes. The description still naming kasegi is not a failure, because the guard never checks
the converse (a lane named in the description must be classed non-`none`). This is the direction the
before-column said would be needed ("a check that reads kotoba's own side, the direction the planned
`--skill` content guard takes"); the landed `--skill` arm reads the other way — census → description —
so it cannot catch a downgrade. M5 is **out of D3's stated scope** (not a duplicate) and **out of C1's
stated direction** (C1 claims the description names the lanes the census classes non-`none`), so this
is a coverage finding about the census's truthfulness, not a failure of the claim as written.

**F3 — the refusal is table-scoped: a duplicate row in a second table of the same shape survives.**
`duplicate_lane_failures` is applied to the table `_select_table` picks, and `_select_table` breaks a
header-score tie in favour of the **first** block in the file. A duplicated kasegi row placed in a
second, verbatim-header census table appended to the census file (M10) — or in a second province-shaped
table at the end of the `## Adjacent` section (M11) — is therefore **not** refused: the guard prints
`rows 20 verified 20` / `province rows 20 matched 20` and exits **0**, while the file holds 21 lane rows
for 20 lanes. Conditions for the escape: the stray table must come *after* the real one (an earlier
table would be selected instead and the lane-set check would then fail), and must not out-score the real
header on the token count. The census file is append-only and carries round-50 sections, so a "restated"
table is a plausible edit; bounded finding: the guard should refuse a repeated lane in *every*
right-shaped table of the file, or state that its refusal covers one table per file.

## Results table

Detector: `python3 -B verifiers/check_sibling_census.py <census> --province <PROVINCE.md>`, and the same plus `--skill <SKILL.md>`; exit 1 = killed, 0 = survived.

| id | mutation | exit (province only) | exit (with `--skill`) | verdict |
|---|---|---|---|---|
| M1 | duplicate one census row (kasegi, verbatim) | 1 | 1 | **killed** (was SURVIVED) |
| M2 | duplicate one PROVINCE `## Adjacent` row (kasegi, verbatim) | 1 | 1 | **killed** (was SURVIVED) |
| M3 | census row duplicating kasegi, lane cell case-varied (`Kasegi`) | 1 | 1 | **killed** (duplicate refusal, not only the filesystem) |
| M5 | kasegi census row `adjacent`→`none`, PROVINCE row edited to match | 0 | 0 | **SURVIVED** (not via `--skill`; F2) |
| M7 | duplicate the kasegi row consistently in census **and** PROVINCE | 1 | 1 | **killed** (was SURVIVED) |
| M8 | duplicate the kasegi census row at a different (older) pin, PROVINCE repointed | 1 | 1 | **killed** (was SURVIVED) |
| M9 | duplicate the kasegi census row with a `-shokunin`-suffixed lane cell | 1 | 1 | **killed** (new probe) |
| M10 | duplicate the kasegi census row in a second census-shaped table | 0 | 0 | **SURVIVED** (new probe; F3) |
| M11 | duplicate the kasegi PROVINCE row in a second province-shaped table | 0 | 0 | **SURVIVED** (new probe; F3) |

## Evidence

Scratch: `/fast/scratch/hyaku/kotoba-r50/falsify/MutDuplicateRows/` — private clone `lane/` at
`956ee1676e4c18480bce8ac3993541462be76e11` (and `lane_tip/` at the two later tips), harness
`mutants.py`, logs `run-log.txt` and `tip-run*.txt`, one directory per mutant under `mutants/`. The
guard script was never edited; each mutant gets its own copy of the three input files.

    $ python3 -B mutants.py
    BASELINE --province only: exit 0   -> rows 20 verified 20 / province rows 20 matched 20
    BASELINE --skill: exit 0           -> skill description names 9 of 9 non-none lanes; length 1008 of 1024
    $ LANE_DIR=$PWD/lane_tip python3 -B mutants.py     # tips a78fec1 and bf109cac: identical verdicts,
                                                      # baseline exit 0, description length 1019 of 1024

Claim counter before and after (the guard's own `--skill` arm, on `git show <rev>:SKILL.md` saved to a
file; the base run names chousa, kama, kotodama and tameshi as not named):

    base rev f304646   -> skill description names 5 of 9 non-none lanes; length 814 of 1024; exit=1
    landed 956ee167    -> skill description names 9 of 9 non-none lanes; length 1008 of 1024; exit=0

The plan's shell counter agrees: `5` at `f304646`, `9` at `956ee167`. The landed guard is green on its
own fixtures: `python3 -B verifiers/check_sibling_census.py --self-test` → `self-test: 0 failure(s) over
68 assertions`, exit 0. Representative mutant outputs (verbatim; full log in `run-log.txt`):

    M1  exit 1  FAIL census table: lane kasegi appears in more than one row (rows 9 (line 77), 10 (line 78)): a duplicated row inflates the table without surveying a new lane
              rows 21 verified 21 / province rows 20 matched 20
    M3  exit 1  FAIL census table: lane kasegi appears in more than one row (rows 9 (line 77), 10 (line 78)): ...
              FAIL row 10 (census line 78) (lane kasegi): no sibling repo at /home/vgpnk/Projects/shokunin/Kasegi-shokunin
    M5  exit 0  rows 20 verified 20 / province rows 20 matched 20
              skill description names 8 of 8 non-none lanes
    M9  exit 1  FAIL census table: lane kasegi appears in more than one row (rows 9 (line 77), 10 (line 78)): ...
    M10 exit 0  rows 20 verified 20 / province rows 20 matched 20   (census file holds 21 lane rows)
    M11 exit 0  rows 20 verified 20 / province rows 20 matched 20

## Restoration evidence

The harness never writes into the clone's inputs: each mutant is built from in-memory copies of the
three files. Hashes of the private clone's inputs before and after the whole probe are identical (and
are the bytes of the judged rev `956ee167`):

    census   40ea8f98b7da2f8289b33b094c9aa4ada7890db5fb1ef61f23e02325b7bc196b  UNCHANGED
    province a6c12cdcce73cce674382c9529fc6b27c759befae3c736455fd6c480f5c2bccf  UNCHANGED
    skill    9fe2ca74b00ce51e087237c34d031a576ad8c191b642612b447fd53c26340702  UNCHANGED
    guard    2f9d8a88b1d3dd8562455006d5ea89ec02546a1ecb9d023f327d88e5502eedc7  UNCHANGED

The lane checkout has since moved on (integrator landings `a78fec1`, `bf109cac`); the guard file's
bytes are the same at all three revs (`2f9d8a88…`), and the census/PROVINCE/SKILL bytes differ there
(`f53a923b…`, `44fae238…`, `05457302…` at `bf109cac`) — that move was not mine. Only this report file
was written in the lane. No git write command (commit, add, stash, checkout, switch, reset, pull,
push, apply) and no jj command was run in the lane, the fleet repo or any sibling lane repo; sibling
repos were read with `git show` / `git cat-file` only. Observed during the probe, not mine: the lane's
`git status` shows concurrent modifications to `corpus/lessons/round-50.md`, `PROVINCE.md` and the census
(other writers); they were left untouched. No tool was installed or upgraded by this seat; the probe needs only `git` and `python3`.

Report: .ufo/waves/round-50/falsify/MutDuplicateRows.md
