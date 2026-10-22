# CensusRecheckTool — C1 content guard (routed defect R2)

Round 49 build wave, seat `CensusRecheckTool`, axis `adjacency`. Session hyaku, 2026-10-22.
Lane base `a5adc146a2995dcc5a95a6d8db6e5674f75191ac`.

## Findings

1. **The guard is green against the real landed census, and red against every
   mutation of it.** `corpus/knowledge/sibling-overlap-census-round49.md` and the
   round-49 `PROVINCE.md` landed from other seats during this wave. The guard on
   the real pair gives `rows 20 verified 20` / `province rows 20 matched 20`,
   exit 0. Mutating exactly one thing — a quote word, a commit, a dropped lane
   row, an empty quote cell, a heading-line quote, a province classification, a
   province lane, the province table itself — flips it to exit 1 with a FAIL
   line naming the row. That is the R2 class the round-48 spot-check named: the
   counter fails on content, not only on shape.

2. **The exact `recheck:` command the census entry names already works.** The
   entry carries `recheck: python3 -B verifiers/check_sibling_census.py
   corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md`.
   Run in a clone with the instrument at `verifiers/check_sibling_census.py`, it
   prints `rows 20 verified 20` / `province rows 20 matched 20` and exits 0 —
   the L1 only has to land the file at that path.

3. **The lane-set check is what makes "20 of 20" a measurement rather than a
   claim.** The sibling-lane set is derived from the filesystem (`*-shokunin`
   directories under `--fleet`, minus kotoba): 21 such directories at the real
   fleet root, minus kotoba = **20**, matching the plan's declared after-value.
   Dropping the `revenger` row gives `lane set: 1 sibling lane(s) never
   surveyed: revenger`.

4. **Design note the L1 should know before landing:** the guard counts a lane
   as *surveyed* as soon as a row names it, even if that row then fails its
   quote check. Otherwise a census could satisfy the lane-set check by dropping
   exactly the rows whose quotes are false; both failures are reported.

5. **One check I first wrote had to be dropped, and the reason generalises.** My
   first version required the `path:line` path to be among the skill file(s) in
   the `path` cell. The real census has 12 rows whose `path` cell is `SKILL.md`
   while the quote was located in the sibling's `PROVINCE.md` — the columns are
   independent (`path` says *which skill file the lane has*, `path:line` says
   *where this quote was read*). Requiring them to agree produced 12 false reds
   against a correct census. The check is gone; only the `path:line` path drives
   the `git show`, which is what the task text specifies. Lesson: the column
   contract must be derived from the entry, not guessed.
6. **Not done, and out of scope for this seat:** the `recheck:` line citing the
   script is the L1's to write. The script's exit ladder and stdout shape are
   what that line depends on: `rows N verified M` and `province rows N matched M`.

## Files

- `verifiers/check_sibling_census.py` — the instrument, intended landing path.
  923 lines, 38 247 bytes, sha256 `8889d2190e300710042c238c6618343b5b1527f7ef901683ef1bbc536b3c8ddc`.
- Deliverable patch (not landed by me):
  `/fast/scratch/hyaku/kotoba-r49/seats/CensusRecheckTool/check_sibling_census.patch`
  — 39 369 bytes, sha256 `639df5f3d21d84041a2c9b5937fd607b983829dab86ce92efd64f4546f608bf7`,
  `git apply --check` clean against a fresh clone of the lane.
- Scratch copy of the same bytes:
  `/fast/scratch/hyaku/kotoba-r49/seats/CensusRecheckTool/check_sibling_census.py`.

The lane checkout was **not** modified by this seat: `git status --porcelain`
in the lane shows `M PROVINCE.md`, `M SCORECARD.md`, `?? .ufo/waves/round-49/`,
`?? corpus/knowledge/sibling-overlap-census-round49.md`, `?? plans/round-49.md` —
the four non-`.ufo/` entries are other seats' work, not mine
(`verifiers/check_sibling_census.py` is absent from the lane).


## Evidence (commands with exit codes)

```
$ python3 check_sibling_census.py --self-test              # scratch copy
self-test: 0 failure(s) over 39 assertions
EXIT=0

$ git apply --check -v ../check_sibling_census.patch   # in a fresh clone of the lane
Checking patch verifiers/check_sibling_census.py...
APPLY_CHECK=OK
$ git apply ../check_sibling_census.patch && python3 verifiers/check_sibling_census.py --self-test
APPLIED=OK
self-test: 0 failure(s) over 39 assertions
SELFTEST_EXIT=0
```
The census entry's own `recheck:` command, run in a clone with the instrument at
`verifiers/` and the entry + PROVINCE.md copied in — and the same command
against the lane's live tree — both give the same green result:

```
$ python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md
rows 20 verified 20
province rows 20 matched 20
EXIT=0
```

Red arms against the **real landed census** — each fixture is the real census
with exactly one thing changed; every FAIL line names the row:

| arm | exit | FAIL line |
|---|---|---|
| mutated quote (lore) | 1 | `row 13 (census line 71) (lane lore): quote not found at PROVINCE.md:3 (+/-2 lines)` / `rows 20 verified 19` |
| mutated quote (audio) | 1 | `row 1 (census line 59) (lane audio): quote not found at PROVINCE.md:3 (+/-2 lines)` / `rows 20 verified 19` |
| wrong commit | 1 | `row 1 (census line 59) (lane audio): git show 000000000000:PROVINCE.md in …/audio-shokunin failed (fatal: path 'PROVINCE.md' exists on disk, but not in '0000…')` / `rows 20 verified 19` |
| missing lane | 1 | `lane set: 1 sibling lane(s) never surveyed: revenger` / `rows 19 verified 18` |
| empty table | 1 | `census table is empty: 0 rows in … (refusing an empty census)` / `rows 0 verified 0` |
| empty quote cell | 1 | `row 13 (census line 71) (lane lore): empty quote cell` / `rows 20 verified 19` |
| heading-line quote (real `kasegi` heading at `PROVINCE.md:1`) | 1 | `row 9 (census line 67) (lane kasegi): quote sits on a markdown heading (PROVINCE.md:1): a title-only quote is not a scope statement` / `rows 20 verified 19` |
| province classification mismatch | 1 | `province row 1 (line 11): lane audio classification 'contested' does not match the census 'none'` / `province rows 20 matched 19` |
| province bare-name list | 1 | `province: the `## Adjacent` section of … holds no lane table (`| lane | classification | commit | ... |`); a bare-name list is not a table` / `province rows 0 matched 0` |
| province lane dropped | 1 | `province: lane lore is in the census but not in the `## Adjacent` table` + `province: the `## Adjacent` table has 19 row(s), fewer than the 20 sibling lane(s)` / `province rows 19 matched 19` |

The same arms were re-run in isolation against the self-test's temp-repo
fixture and each printed a distinct, non-vacuous FAIL message; the green arm
printed `failures: [] verified: 1` — the arms are red for their own reason, not
because a shared setup is broken. Usage-error ladder on the real census (all
exit 2, no traceback): missing province / missing census / missing fleet / no
argument / unknown flag — each EXIT=2. Determinism: two consecutive live runs
produced byte-identical stdout on the real census (sha256
`6f6aa45595bbca35718d6ebc276f88a51ba7ec4f7347e53c7ffeb11ae35f93d6` both times).

Read-only: the script writes only inside its own `tempfile.TemporaryDirectory`
(the self-test's throwaway git repos). It never writes to the lane or to a
sibling repo; sibling content is read through `git -C <repo> show`.

Tooling: no installs were needed or performed this wave — the instrument is
stdlib-only Python 3. Interpreter `python3` 3.14.8; `git` 2.56.0.

## Risks and blockers

- **The census entry and PROVINCE.md are still untracked/uncommitted in the
  lane.** The guard was run against their current on-disk bytes and against
  copies of the same bytes in a clone; once the L1 commits them the same
  command must be re-run from the committed tree — the entry's `recheck:` line
  is only meaningful from a checkout.
- **Column-count coupling.** The guard requires exactly 9 cells per census row
  and 4 per province row. The landed entries satisfy both; a reshaped table
  fails with `expected N cells, found M` naming the row.
- **A quote spanning several physical lines** (a folded YAML `description: >`
  block) is matched against the collapsed ±2-line window and attributed to the
  first window line carrying its first word. That path is exercised in the code
  but has **no dedicated self-test arm**; only incidental coverage.
- **The heading-line rule is strict by design** and rejects a census row that
  quotes a sibling's `# Title` line. That is the L1's requested behaviour, and
  it correctly fires on the real `kasegi` heading — but it is the check most
  likely to need wording adjustment if real rows ever need to cite a title.
- The sibling-lane set is derived from the filesystem at run time, so a fleet
  that gains or loses a `*-shokunin` directory turns the lane-set check red.
- **Self-test coverage gap.** The self-test uses synthetic temp repos only; the
  real-fleet runs above were manual, not committed as a fixture, because such a
  fixture would pin the siblings' commits into kotoba's repo — a custody
  question for the L1, not this seat.
