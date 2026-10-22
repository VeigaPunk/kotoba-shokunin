# CensusGuard — round-50 build (C1 content guard + D3 duplicate rows)

**Result: the two assigned changes land in `verifiers/check_sibling_census.py` (the only file
touched).** The guard now refuses a duplicated lane row in **both** the census table and the
PROVINCE.md `## Adjacent` table (exit 1, the lane is named), and gains `--skill PATH`: it fails
(exit 1) naming every census lane classified non-`none` that the SKILL.md frontmatter
`description` does not name with a split. On the base `SKILL.md` it exits 1 and prints
`skill description names 5 of 9 non-none lanes`, missing chousa, kama, kotodama, tameshi.

**Patch:** `/fast/scratch/hyaku/kotoba-r50/build/CensusGuard/patch.diff` (unified diff against
`f30464660c675d1c1e2851a3bf0366a3aaffe5a8`, one file, 496 insertions / 13 deletions).
`git apply --check` against a fresh clone at the base commit: clean.
Scratch: `/fast/scratch/hyaku/kotoba-r50/build/CensusGuard/` (`lane/` = private clone at
`f3046466`, `mut/` = mutants and fixtures, `verify/` = patched copy used for the runs below).

## Change 1 — D3: a duplicated lane row is refused (both tables)

`duplicate_lane_failures(rows, columns, subject)` builds the lane set while parsing and fails on
a repeat of the **normalized** lane name (`normalize_lane`: lower-cased, `-shokunin` suffix
dropped), so `Alpha` and `alpha` are the same lane. It runs on the census table (9 columns) and
on the PROVINCE.md `## Adjacent` table (4 columns), each with its own message. No row-count
check is used: a duplicate is 21 rows over 20 lanes, and the row count has a floor but no ceiling.

Why: the lane set is a set, so a duplicate collapses and the row count grows without a new lane
(round-49 falsify `ReviewLessonQ25.md` §4; seat `MutCensusGuardBase`).

**Live evidence (real files, base commit).** Duplicate census row (`mut/census.dup.md`, the
`audio` row repeated):

```
$ python3 -B verifiers/check_sibling_census.py ../mut/census.dup.md --province PROVINCE.md
FAIL census table: lane audio appears in more than one row (rows 1 (line 69), 2 (line 70)): a duplicated row inflates the table without surveying a new lane
rows 21 verified 21
province rows 20 matched 20
exit=1
```

Duplicate PROVINCE row (`mut/PROVINCE.dup.md`, the `audio` row repeated):

```
$ python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province ../mut/PROVINCE.dup.md
FAIL province `## Adjacent` table: lane audio appears in more than one row (rows 1 (line 11), 2 (line 12)): a duplicated row inflates the table without surveying a new lane
rows 20 verified 20
province rows 21 matched 21
exit=1
```

The **unpatched** code passes both — the falsify finding, reproduced:

```
$ python3 -B ../mut/base.py ../mut/census.dup.md --province PROVINCE.md
rows 21 verified 21
province rows 20 matched 20
exit=0
$ python3 -B ../mut/base.py corpus/knowledge/sibling-overlap-census-round49.md --province ../mut/PROVINCE.dup.md
rows 20 verified 20
province rows 21 matched 21
exit=0
```

## Change 2 — `--skill PATH`: the C1 content guard

`--skill PATH` reads the YAML frontmatter `description` of PATH with the file's own
`description_of` helper, takes the census lanes whose classification is not `none` (9 lanes at the
base commit: chousa, kagi, kake, kama, kasegi, kengaku, kotodama, kumitate, tameshi), and fails
(exit 1) naming each such lane that the description does not carry as a whole token,
case-insensitively (`token_in`). Each census lane counts once however often it is written.

### L1 steer (binding, from `CriticC1Sizing.md` § Required changes 3–4) — all four applied

- **(a) `description_of` ends the value at ANY column-0 line.** The old lookahead required a
  column-0 line *containing a colon*, so a colon-free YAML comment was swallowed into the
  description (mutant m8). The new lookahead is `(?=^\S|\Z)`. The parsed value now matches PyYAML
  exactly on all four files checked (SKILL.md, base.md, m7, m8): lengths 814/814, 814/814,
  856/856, 814/814, byte-equal strings. The old parser gave 847 for m8 and contained
  `# chousa kama kotodama tameshi`. The m8 arm asserts the comment is not in the parsed value.
  This helper also derives the sibling cells, so `--self-test` and the live census run were both
  re-run after the change — the live census still prints `rows 20 verified 20`.
- **(b) whole-token, case-insensitive, case-folded dedup.** `token_in` is case-insensitive; the
  count is over census lanes, not over occurrences. Mutant m7 (base + `Kagi, Kake: see above.
  kotodama, tameshi.`) reports **7 of 9**, not 9 — the capitalised repeats do not double-count.
- **(c) G4 length cap.** The parsed description must be 1–1024 characters (S018 `Must be 1-1024
  characters`). Over-length and empty descriptions fail, and the length line
  `skill description length L of 1024` is always printed.
- **(d) G1 clause binding.** The description is split into clauses (on `;` and on a sentence end)
  and a lane counts as NAMED only when some clause that contains it also carries an ownership or
  routing marker from a list pinned in the file
  (`owns/own/owned/route/routes/routing/NOT/see above/as above/see also`). The rule is named as a
  lexical approximation in every failure message that uses it, and the docstring records that it
  has counterexamples in both directions. `NOT` is matched upper-case only (it is how the fleet
  writes a refusal; lower-case "not" occurs in ordinary prose such as "not skill files" and would
  bind every clause it appeared in).

### Printed lines (always, failure or not)

```
skill description names K of N non-none lanes
skill description length L of 1024
```

`K` counts only clause-bound lanes; `N` is the number of non-`none` census lanes.

## Live runs (required outputs), base commit `f3046466`

```
$ python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md
rows 20 verified 20
province rows 20 matched 20
exit=0

$ python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md --skill SKILL.md
FAIL skill description does not name the non-none census lane chousa
FAIL skill description does not name the non-none census lane kama
FAIL skill description does not name the non-none census lane kotodama
FAIL skill description does not name the non-none census lane tameshi
rows 20 verified 20
province rows 20 matched 20
skill description names 5 of 9 non-none lanes
skill description length 814 of 1024
exit=1
```

`names 5 of 9` as required; the four named lanes are chousa, kama, kotodama, tameshi — exactly the
four the base description omits. The unpatched file has no `--skill` option at all
(`unrecognized arguments: --skill SKILL.md`, exit 2).

## Self-test

**Assertion count: 44 before → 68 after** (24 new assertions). The floors registry floor is the
L1's to bump; the new count is 68.

```
$ python3 -B verifiers/check_sibling_census.py --self-test
self-test: 0 failure(s) over 68 assertions
exit=0
```

### Shown able to fail (each arm first fails against the unpatched code)

`mut/unpatched.py` is this file with the three changes reverted (duplicate refusal removed from
both tables, `--skill` not wired into the CLI and its unit check neutered, `description_of`
restored to the old lookahead). Against it the new arms fail — 21 of the 68 assertions are red:

```
FAIL census duplicate row: fails: got []
FAIL census duplicate row: names the lane and the rows: got []
FAIL census case-variant duplicate row: fails: got ['row 2 (census line 6) (lane alpha): no sibling repo at .../Alpha-shokunin']
FAIL province duplicate row: fails: got []
FAIL province duplicate row: names the lane and the rows: got []
FAIL consistent duplicate rows: fail in both tables: got []
FAIL skill: the base-shaped description names five of nine: got (9, 9)
FAIL skill: the missing lanes are named in the failures: got []
FAIL skill m7: seven of nine (case-folded, no double count): got (9, 9)
FAIL skill m7: the two unbound lanes are named: got []
FAIL skill m1: a bare list does not bind the lanes: got (9, [])
FAIL skill m1: the bare-list lanes are named in the failures: got []
FAIL skill m5: a negated mention does not bind the lanes: got (9, [])
FAIL skill: an over-length description fails: got []
FAIL skill: an empty description fails: got []
FAIL skill m8: a column-0 comment is not swallowed into the description: got 'Prompt and skill craft. Sibling boundary: the five sibling lanes kagi, kake, kas'
FAIL cli --skill: the count line is printed: got 'rows 2 verified 2\n'
FAIL cli --skill: the length line is printed: got 'rows 2 verified 2\n'
FAIL cli --skill: a missing lane exits 1: got (0, 'rows 2 verified 2\n')
FAIL cli --skill: the missing lane is named: got 'rows 2 verified 2\n'
FAIL cli --skill: the count line is printed on failure too: got 'rows 2 verified 2\n'
self-test: 21 failure(s) over 68 assertions
exit=1
```

### Arms added

Duplicate rows: census table (duplicated `alpha` row), case-variant duplicate (`Alpha` vs `alpha`
— the unpatched code exits 1 there only because the repo directory lookup is case-sensitive, not
because the duplicate is caught), PROVINCE.md `## Adjacent` table, and a consistent duplicate pair
in both tables (must fail in both). `--skill`: a routed description naming every non-none lane
passes; the base-shaped description names five of nine and the four missing lanes are named; m7
reports seven of nine with the two unbound lanes named; m1 (bare list) and m5 (negated mention) are
refused; over-length and empty descriptions fail the length cap; m8 (column-0 comment) is not
swallowed; at the CLI level a missing lane exits 1 and both summary lines are printed on failure
and on success.

### Mutants from the critic seat, run against the patched guard

Command per file: `python3 -B verifiers/check_sibling_census.py
corpus/knowledge/sibling-overlap-census-round49.md --skill <mutant>`.

| mutant | guard result | note |
|---|---|---|
| base | 5 of 9, exit 1 | missing chousa, kama, kotodama, tameshi |
| m1 bare list | 5 of 9, exit 1 | the four names are refused: named but in a clause with no marker |
| m5 negated | 5 of 9, exit 1 | same; the negated clause carries no marker |
| m7 case duplicates | **7 of 9**, exit 1 | capitalised repeats counted once |
| m8 column-0 comment | 5 of 9, exit 1 | the comment is not in the description (the old parser said 9 of 9) |
| m9 wrong split | 9 of 9, **exit 0** | known pass, see below |
| m6 `-shokunin` suffix | 5 of 9, exit 1 | the suffixed names are whole tokens under `token_in`, so they count as *mentions* but the clause carries no marker |

**Known pass (recorded, not hidden): m9** — `chousa, kama, kotodama and tameshi own SKILL.md
audits; kotoba does not.` The clause does contain the marker "own", so G1 binds those four lanes
and the guard exits 0. G1 cannot see that the split is false (the critic says the same: "G1 … catches
m1, but m5 and m9 still pass"). Catching m9 needs G3 (a pinned owner phrase per lane) or G2
(direction), neither of which this seat was scoped to add; the steer asked for G1 + G4 only. m6 and
m9 are recorded as known passes of the G1 rule and the falsify wave should treat them as such
rather than as a defect in the arms.

The G1 marker rule is a lexical approximation with counterexamples in both directions, as the
critic required: it accepts "chousa owns the research method" and also accepts a clause whose
marker attaches to the wrong lane ("chousa, kama own their own audits"), and it refuses a correct
split phrased without a listed marker.

## Pre-existing self-test flake found and fixed (same file, in scope)

The self-test flaked about once in thirty runs at the base commit, in the arm `mechanical: a
two-word quote fails`. The cause is in the fixture, not the guard: that arm built its census row
from **fleet-g**'s alpha commit but ran it against **fleet-a**'s alpha repo. The two repos hold
byte-identical `SKILL.md` content, so their commit ids differ only by the commit timestamp — the
arm passed only when the two commits landed in the same wall-clock second. Measured:

- base file, 120 runs → **3 failures** (the failing assertion printed `git show <fleet-g
  commit>:SKILL.md … fatal: path 'SKILL.md' exists on disk, but not in '<commit>'`, i.e. the commit
  was not in the repo it was checked against);
- the same two repos one second apart → the commits differ and `git show` fails exactly as above
  (reproduced directly).

The arm now uses fleet-a's own alpha commit, so it does not depend on two commits sharing a
timestamp. After the fix: **0 failures in 80 runs**. The fix touches only the self-test fixture
(two lines); no guard behaviour changed. It matters this round because the guard is being
registered in the floors registry (D3): a self-test that fails 1 run in 30 would make the floors
gate fail randomly.

## Floors registry (D3: the guard enters `verifiers/floors-registry.json`)

**Not done by this seat** — the registry and the `check_assertion_floors.py` in-file tables are
L1-owned files and the steer says the registry floor is bumped by the L1. What the L1 needs:

- new assertion count: **68** (was 44 at the base commit);
- path `verifiers/check_sibling_census.py`;
- summary pattern `self-test:\s*(\d+) failure\(s\) over (\d+) assertions` (assertion count in
  group 2) — verified to match this file's output: `('0', '68')`;
- the registry row and both in-file tables (`INSTRUMENTS` and `EXPECTED_INSTRUMENTS` in
  `verifiers/check_assertion_floors.py`, plus `verifiers/floors-registry.json`) must move
  together; `instrument_total` goes 10 → 11.

Until that lands, `check_assertion_floors.py` does not run this instrument at all
(`grep -n "check_sibling_census" verifiers/floors-registry.json verifiers/check_assertion_floors.py`
→ no match, exit 1).

## Risks and limits

- The G1 marker rule is lexical, not a parse of intent. False-negative direction: m9, m6.
  False-positive direction: a marker in a clause that does not really attach to the lane. Both are
  documented in the file's docstring and in the failure messages.
- The G4 cap uses the length of the *parsed* description, which equals the YAML value (814 for the
  base SKILL.md, matching PyYAML). A description of exactly 1024 characters passes; 1025 fails.
- The `--skill` lane set is derived from the census file's `classification` column. If the
  round-50 precedence ruling (D3) moves a lane between `none` and non-`none`, the lane list and the
  target move with it — the guard reads the census, it does not hard-code the nine.
- The duplicate check compares normalized lane names, so a lane written twice with two different
  classifications now fails rather than silently overwriting — that is the intent.
- `description_of` is shared with the sibling-cell derivation. The change was re-checked against
  the live census (`rows 20 verified 20`, `province rows 20 matched 20`, exit 0), so no sibling
  cell moved.

## Commands run (exit codes verbatim)

| command | output | exit |
|---|---|---|
| `python3 -B verifiers/check_sibling_census.py --self-test` (patched) | `self-test: 0 failure(s) over 68 assertions` | 0 |
| `python3 -B verifiers/check_sibling_census.py --self-test` (mut/unpatched.py) | `self-test: 21 failure(s) over 68 assertions` | 1 |
| `python3 -B verifiers/check_sibling_census.py corpus/… --province PROVINCE.md` | `rows 20 verified 20` / `province rows 20 matched 20` | 0 |
| `python3 -B verifiers/check_sibling_census.py corpus/… --province PROVINCE.md --skill SKILL.md` | 4 FAIL lines + `skill description names 5 of 9 non-none lanes` + `skill description length 814 of 1024` | 1 |
| `python3 -B verifiers/check_sibling_census.py ../mut/census.dup.md --province PROVINCE.md` | `FAIL census table: lane audio appears in more than one row …` | 1 |
| `python3 -B verifiers/check_sibling_census.py corpus/… --province ../mut/PROVINCE.dup.md` | `FAIL province \`## Adjacent\` table: lane audio appears in more than one row …` | 1 |
| `python3 -B ../mut/base.py ../mut/census.dup.md --province PROVINCE.md` | `rows 21 verified 21` (unpatched passes the duplicate) | 0 |
| `python3 -B ../mut/base.py corpus/… --skill SKILL.md` | `error: unrecognized arguments: --skill SKILL.md` | 2 |
| `git apply --check patch.diff` (fresh clone at base) | — | 0 |
| self-test, 80 consecutive runs (patched) | `self-test: 0 failure(s) over 68 assertions` every run | 0 |
| self-test, 120 consecutive runs (base file, `mut/base.py`) | 3 runs failed on the pre-existing fixture flake | 1 |

Tools installed: none. No pacman transaction, no package install.
