# MutSiblingCensus — mutation battery on `verifiers/check_sibling_census.py` (round-73 wave 1)

**Verdict: 9 of 12 assigned single-point mutants KILLED by the gate's own self-test; 3 SURVIVED — M03 (cap off-by-one), M05 (clause source = whole file), M09 (substring token match). M05 and M09 are exactly the seat's warned failure mode: a rewritten description can drop a sibling clause and still read conformant. M03 is a boundary-calibration gap in the other direction: a description of exactly the allowed 1,024 characters is falsely rejected and the self-test stays green. All three are coverage findings against the self-test as R3's detector (replacement C2, `plans/round-73-addendum-1.md`); the contract is not changed by this seat, and the live tree shows no delta today (all four live runs: exit 0, `skill description names 9 of 9 non-none lanes`, length 1019 of 1024 — independently confirming the addendum's 1,019/1,024 figure). The lane file was never modified: sha256 `2f9d8a88…eedc7` before and after; `git status --porcelain verifiers/` empty.**

Base `072048f`, lane `/home/vgpnk/Projects/shokunin/kotoba-shokunin`. Python 3.14.8. Date 2026-10-25. Mutant copies + harness + raw results: `.ufo/waves/round-73/w1/build/MutSiblingCensus/` (`mutation_battery.py`, `mutants/M*.py`, `results.json`). No tooling was installed or upgraded; all runs sequential (each 0.7–1.4 s), inside the process caps.

## Baseline (pristine bytes)

```
$ python3 -B verifiers/check_sibling_census.py --self-test     # lane root, 60 s cap
self-test: 0 failure(s) over 68 assertions        exit 0, 1.38 s
$ sha256sum verifiers/check_sibling_census.py
2f9d8a88b1d3dd8562455006d5ea89ec02546a1ecb9d023f327d88e5502eedc7
```

Detector per mutant: `python3 -B .ufo/waves/round-73/w1/build/MutSiblingCensus/mutants/<name>.py --self-test` (same harness, same cwd, 60 s cap). KILLED = exit ≠ 0 (assertion failures on stderr); SURVIVED = exit 0 with the baseline summary line.

## Battery (12 single-point mutants)

| # | mutant (single point, file:line of pristine anchor) | expected detector | observed (self-test) | verdict | mutant sha256[:16] |
|---|---|---|---|---|---|
| M01 | `marker_in` final `return False` → `return True` — G1 clause binding neutered (`:462`) | m1 bare-list arm, m5 negated arm | rc=1: `skill m1: a bare list does not bind the lanes: got (9, [])`; `skill m1: the bare-list lanes are named in the failures: got []`; `skill m5: a negated mention does not bind the lanes: got (9, [])` | **KILLED** | `94305bf1f83e1d47` |
| M02 | G4 ceiling dropped: `or length > SKILL_DESCRIPTION_MAX` removed (`:541`) | over-length rec | rc=1: `skill: an over-length description fails: got []` | **KILLED** | `217e66aae0431eb4` |
| M03 | cap off-by-one: `>` → `>=` at `:541` (exactly-1024 rejected) | none — no exactly-1024 fixture | rc=0, `self-test: 0 failure(s) over 68 assertions` | **SURVIVED** | `f4201f638be99c85` |
| M04 | `description_of` lookahead `(?=^\S\|\Z)` → `(?=^\S*:\|\Z)` — value no longer ends at a bare column-0 line, a column-0 comment is swallowed (`:397`; round-50 m8 regression) | m8 rec | rc=1: `skill m8: a column-0 comment is not swallowed into the description: got 'Prompt and skill craft. Sibling boundary: the five sibling lanes kagi, kake, kas…'` | **KILLED** | `6dc8746eb9447b6c` |
| M05 | clause source `description` → `text` in `skill_description_failures` (`:537`) — lanes named only in a `Triggers:` list (or anywhere in the file) now bind | none — no Triggers/body fixture | rc=0, `self-test: 0 failure(s) over 68 assertions` | **SURVIVED** | `f385bab66afced5f` |
| M06 | one inserted early return after `:535`: empty/unreadable description ⇒ `{"named": 0, "total": 0, …, "failures": []}` (all-pass) | empty-description rec | rc=1: `skill: an empty description fails: got []` | **KILLED** | `701e1f8902062a35` |
| M07 | G4 floor dropped: `length < SKILL_DESCRIPTION_MIN or` removed (`:541`) | empty-description rec (needs a `1-1024` failure) | rc=1: `skill: an empty description fails` — failures hold only the nine does-not-name lines, no `1-1024` length failure | **KILLED** | `e8ccb78053291235` |
| M08 | does-not-name failure never appended (`:543-546` block → bare `continue`) | FIVE/BARE/NEGATED failure-count recs, CLI missing-lane exit | rc=1, 4 FAIL lines incl. `cli --skill: a missing lane exits 1: got (0, 'rows 2 verified 2\nskill description names 1 of 2 non-none lanes…')` — the mutant gate exits 0 with a lane missing | **KILLED** | `7b997f1c967951fa` |
| M09 | `token_in` word-boundary guards dropped (`:403-405`): plain `re.search(re.escape(name), text, re.I)` — `kake` matches inside `kakegawa` | none — no fixture has a lane inside a superstring | rc=0, `self-test: 0 failure(s) over 68 assertions` | **SURVIVED** | `b1624ce521507c45` |
| M10 | description truncated to first 256 chars (`:535-536`) | routed-all rec | rc=1, 3 FAIL lines: `skill: a routed description names every non-none lane: got (7, 9, […kumitate, …tameshi])` (first indices: kotodama 243, kumitate 283, tameshi 337 — the latter two fall beyond 256); `skill: an over-length description is over the cap: got 256` | **KILLED** | `198d053ea25daf56` |
| M11 | duplicate test disabled: `if len(entries) > 1:` → `if False and …` (`:493`) | duplicate-row recs (census + province) | rc=1, 6 FAIL lines: `census duplicate row: fails: got []`; `province duplicate row: fails: got []`; `consistent duplicate rows: fail in both tables: got []`; the case-variant rec then trips a different failure (`no sibling repo at …/Alpha-shokunin`) — still red | **KILLED** | `c6b833d6758a58f9` |
| M12 | returned `total` hard-coded to 9 (`:562`) | CLI count-line recs | rc=1, 2 FAIL lines: `cli --skill: the count line is printed: got '…skill description names 2 of 9 non-none lanes…'` (expects 2 of 2) | **KILLED** | `bae7d9b7ddb5d636` |

0 inconclusive; the baseline detector passed before the battery, so every verdict above is a killed/survived reading, not a baseline artifact.

## Survivor probes (differential, same fixtures through pristine vs mutant `skill_description_failures`)

**M05 — a lane named only inside the frontmatter `Triggers:` list binds.** Fixture: frontmatter whose `description` value is the base-shaped five-lane routing (`SKILL_DESC_FIVE`) plus a `Triggers:` block naming the four missing lanes in marker-bearing clauses. `description_of` ends the value at the column-0 `Triggers:` line (pristine parses 5 lanes), yet the mutant reads clauses from the whole file:

```
pristine: named 5, failures 4 (chousa, kama, kotodama, tameshi missing)  → gate exit 1
M05:      named 9, failures 0                                            → gate exit 0
```

So a rewritten description may drop all four sibling clauses and still read conformant whenever a `Triggers:` line (or any body text) carries `owns`/`route` next to the lane names. The self-test has no fixture with a `Triggers:` list, so it cannot see this class.

**M09 — `kake` accepted from inside `kakegawa`.** Fixture: description naming `kakegawa owns its own SKILL.md content` plus the other eight lanes; lane `kake` itself never appears:

```
pristine: named 8, failures 1 (kake missing)   → gate exit 1
M09:      named 9, failures 0                  → gate exit 0
```

The whole-token guard (`(?<![a-z0-9-])…(?![a-z0-9])`, `:404`) is untested by the self-test: no fixture lane occurs as a substring of another token, so the boundary guards could be deleted without a single assertion moving.

**M03 — false rejection at the cap boundary.** Boundary sweep on the routed-all fixture padded to exact lengths:

```
len=1023  pristine: 0 failures (named 9) | M03: 0 failures (named 9)
len=1024  pristine: 0 failures (named 9) | M03: 1 failure 'skill description length 1024 is outside 1-1024 characters (S018: …)'
len=1025  pristine: 1 failure            | M03: 1 failure
```

A conformant description at exactly the S018 maximum would fail an off-by-one counter while the self-test reports 0 failures over 68 assertions. Directly relevant to replacement-C2 R3: the live description measures 1,019 chars, 5 characters under the boundary a rewrite will steer toward.

**Live `--skill` differential (read-only, lane root):** `python3 -B <copy> corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md --skill SKILL.md` for pristine, M03, M05, M09 — all exit 0, tails identical: `province rows 20 matched 20` / `skill description names 9 of 9 non-none lanes` / `skill description length 1019 of 1024`. No live delta today: the survivors are gaps in the self-test's regression net, not present-tense gate failures on the committed tree.

## Interpretation notes

- **M04 reading:** "stop reading at the first column-0 line" is pristine behavior (`:397` already ends the value at any column-0 line); a literal mutant would be a no-op against these bytes. Implemented as the only defect-shaped reading — the round-50 m8 regression, where the value does *not* stop there and a column-0 comment is swallowed. Killed by the m8 arm, as expected.
- **M06 shape:** one behavioral point (unreadable ⇒ vacuous pass) expressed as a single inserted early return after the parse at `:535`; every other mutant is a one-token textual edit at the anchor shown.
- Per the role contract, the survivors are recorded as coverage findings; the counter, its fixtures and the frozen R3 predicate are untouched by this seat. If the wave wants the net closed: an exactly-1024-character green fixture kills M03; a Triggers-list fixture (lane bound only outside the description value) kills M05; a `kakegawa`-style superstring fixture kills M09.

## Restoration / hygiene evidence

- Lane bytes before and after the battery: `2f9d8a88b1d3dd8562455006d5ea89ec02546a1ecb9d023f327d88e5502eedc7` (`sha256sum verifiers/check_sibling_census.py`, run first and last); post-battery detector re-run on the lane file: exit 0, `self-test: 0 failure(s) over 68 assertions`, 0.71 s.
- `git status --porcelain verifiers/` → empty (no tracked file modified; no git/jj write of any kind performed).
- No `/tmp/k73w1-MutSiblingCensus.*` scratch was created (harness tempdirs are `TemporaryDirectory` and self-cleaned); mutant copies live permanently under `.ufo/waves/round-73/w1/build/MutSiblingCensus/mutants/` as declared artifacts with their hashes in `results.json`.
- Bounds: 12 self-test runs + 4 probe imports + 4 live runs, strictly sequential, longest single process 1.38 s — inside the 4-process / 120 s caps; no tool installs (nothing recorded).
