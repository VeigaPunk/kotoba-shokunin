# MutGuardCode — round-50 falsify: mutation probe of `verifiers/check_sibling_census.py`

**Verdict: HOLDS-BOUNDED** — applies to C1's content guard (`verifiers/check_sibling_census.py` at `956ee1676e4c18480bce8ac3993541462be76e11`). Its `--self-test` kills 17 of 28 single-point mutants in the round-50 code paths, so the guard can genuinely fail on the paths the C1 counter relies on (duplicate-lane refusal, `--skill` handling, the description value, the clause split, the marker list, the length cap). But 11 mutants survive, and for seven of them I demonstrated a real behaviour difference on input the self-test never builds. The survivors are coverage findings against the guard's self-test, not changes to the C1 contract. The C1 live counter reproduces: `skill description names 9 of 9 non-none lanes`, `length 1008 of 1024`, exit 0.

## Setup

- Private clone `/fast/scratch/hyaku/kotoba-r50/falsify/MutGuardCode/lane` at `956ee1676e4c18480bce8ac3993541462be76e11`; pristine verifier sha256 `2f9d8a88b1d3dd8562455006d5ea89ec02546a1ecb9d023f327d88e5502eedc7`.
- Baseline `python3 -B verifiers/check_sibling_census.py --self-test` → `self-test: 0 failure(s) over 68 assertions`, exit 0. The baseline is clean, so a failing mutant is a kill, not a pre-existing failure.
- Each mutant is a **single-point** edit: write the mutated bytes over the verifier, run the self-test, restore the exact pristine bytes, re-check the sha256. All 28 restored byte-exactly (`git status --porcelain` empty at the end).

## Mutant table

`--self-test` failures = failed assertions out of 68; `crash` = the run aborted with a traceback before printing the summary (still a non-zero exit).

| # | mutant | area | self-test failures | verdict |
|---|---|---|---|---|
| D1 | duplicate threshold `> 1` → `> 2` | duplicate-lane detection | 6 | killed |
| D2 | census duplicate call uses `PROVINCE_COLUMNS` | duplicate-lane detection | 4 | killed |
| D3 | province duplicate call uses `CENSUS_COLUMNS` | duplicate-lane detection | 3 | killed |
| D4 | duplicate detection drops case folding | duplicate-lane detection | 1 | killed |
| D5 | duplicate detection keeps rows with too many cells | duplicate-lane detection | 0 | **SURVIVED** |
| S1 | description ends only at a column-0 alphabetic line | `description_of` column-0 end | 1 | killed |
| S2 | description ends only at a column-0 comment line | `description_of` column-0 end | 0 | **SURVIVED** |
| S3 | block-scalar indicator not stripped | `description_of` column-0 end | 2 | killed |
| K1 | clause split drops the sentence-end branch | clause splitting | 3 | killed |
| K2 | clause split drops the semicolon branch | clause splitting | 0 | **SURVIVED** |
| K3 | clause split: capital lookahead → any letter | clause splitting | 2 | killed |
| K4 | clause split keeps empty clauses | clause splitting | 0 | **SURVIVED** |
| M1 | marker list drops `see above` | ownership/routing marker list | 2 | killed |
| M2 | marker list drops `route` | ownership/routing marker list | 0 | **SURVIVED** |
| M3 | marker `NOT` matched case-insensitively | ownership/routing marker list | 0 | **SURVIVED** |
| M4 | all markers matched case-sensitively | ownership/routing marker list | 0 | **SURVIVED** |
| M5 | marker match drops the leading word boundary | ownership/routing marker list | 0 | **SURVIVED** |
| M6 | marker test `any` → `all` over clauses | ownership/routing marker list | 0 | **SURVIVED** |
| L1 | length-cap comparison dropped | 1-1024 length check | 1 | killed |
| L2 | `SKILL_DESCRIPTION_MAX` 1024 → 2048 | 1-1024 length check | 1 | killed |
| L3 | `SKILL_DESCRIPTION_MIN` 1 → 0 | 1-1024 length check | 1 | killed |
| T1 | `token_in` loses case-insensitivity | case-folded dedup | 0 | **SURVIVED** |
| T2 | `normalize_lane` loses case folding | case-folded dedup | 1 | killed |
| C1 | skill failures not added to the result | `--skill` handling | 2 | killed |
| C2 | non-`none` filter compares against `None` | `--skill` handling | 7 | killed |
| C3 | `--skill` check not run at the CLI | `--skill` handling | crash | killed |
| C4 | `lane_classes` classification not lower-cased | `--skill` handling | 0 | **SURVIVED** |
| C5 | `named` counter not incremented | `--skill` handling | 7 | killed |

Totals: **17 killed, 11 survived** of 28; no mutant was inconclusive (the baseline passes).

## Findings (survivors)

**F1 — the case-insensitive lane match is not asserted (T1).** `token_in` is documented as case-insensitive, but the m7 fixture writes `Kagi, Kake:` while the same lanes also appear lower-case earlier in the description, so dropping `re.I` changes nothing the arms see. Difference shown: `Sibling boundary: Kama owns local model serving.` → pristine names 1 of 1, mutant 0 of 1 and fails. The "capitalised repeat" arm the round-50 critic asked for does not test capitalisation.

**F2 — the description value's end is pinned only for a comment (S2).** The guard promises the value ends at ANY column-0 line; the only arm is m8, a column-0 comment, so a mutant ending the value only at a column-0 `#` line survives. Difference shown: with a column-0 `keywords: chousa, kama` line after the value, pristine parses `Sibling boundary: kagi owns secrets and vault ops.` while the mutant swallows `keywords: chousa, kama` into the value — a false "lane named" a real YAML parse would not produce.

**F3 — the semicolon clause separator carries the m1/m5 refusal and is not asserted (K2).** Dropping the `;` branch of `CLAUSE_SPLIT` survives. Difference shown: `Sibling boundary: chousa is listed; routes own their own ground.` → pristine refuses `chousa` (named 0 of 1, 1 failure), the mutant accepts it (named 1 of 1). The semicolon split is what stops a name in one clause being bound by a marker in the next clause — the refusal m1 and m5 exist for — and no arm depends on it.

**F4 — the `NOT` marker rule is untested (M3, M4).** The docstring says `NOT` is upper-case only, because lower-case `not` "would bind every clause it appeared in"; no fixture contains `NOT` or a standalone `not`, so both mutants survive. Difference shown: `Sibling boundary: chousa is not the owner of this ground.` → pristine refuses `chousa` (named 0 of 1, 1 failure), the M3 mutant accepts it (named 1 of 1) — the negated mention m5 is about, uncaught.

**F5 — the `route` marker entry is untested (M2).** Removing `route` from the pinned marker list survives. Difference shown: `Sibling boundary: chousa route to the owning lane.` → pristine names 1 of 1, mutant 0 of 1. The live SKILL.md also says `owns`, so today's description is unaffected; the marker-list entry itself is unpinned.

**F6 — `any` vs `all` over the clauses naming a lane is untested (M6).** Both survive. Difference shown: `… kagi owns secrets and vault ops. Kagi is also mentioned here.` → pristine names 1 of 1, mutant 0 of 1. G1's rule ("some clause that contains it also carries a marker") is not asserted.

**F7 — a mis-cased census classification silently empties the non-`none` set (C4).** The `lane_classes` map is built with `cells[4].strip().lower()` while the row check lower-cases separately; removing the `.lower()` in the map survives. Shown on the live census with its 9 `adjacent` cells written `Adjacent`: pristine prints `skill description names 9 of 9 non-none lanes` and exits 0; the mutant prints `skill description names 0 of 0 non-none lanes` and **also exits 0** — a vacuous pass (Q25). The live census uses lower-case today, so this does not bite at this revision, but no arm asserts the non-`none` set cannot silently become empty.

**F8 — two weak survivors, near-equivalent on the fixtures (D5, K4).** D5 keeps rows with too many cells in the duplicate check; K4 keeps empty clauses. Neither changes any arm's outcome; the unasserted behaviour is that a malformed row must not count as a duplicate and that empty clauses are dropped. Weak coverage, not a behaviour gap.

**Not findings (killed).** The duplicate-lane refusal (D1-D4), the column-0 end against a non-comment line (S1), the block-scalar strip (S3), the sentence-end clause split (K1, K3), the `see above` marker (M1), all three length-cap arms (L1-L3), the case-folded lane normalisation (T2) and the `--skill` plumbing (C1, C2, C3, C5) are caught by the self-test: the D3 duplicate-row guard and the C1 `--skill` path are shown able to fail (Q25).

## Evidence (commands, verbatim exit codes)

```
$ git -C lane rev-parse HEAD                                  -> 956ee1676e4c18480bce8ac3993541462be76e11
$ python3 -B verifiers/check_sibling_census.py --self-test     -> self-test: 0 failure(s) over 68 assertions  (exit 0)
$ python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md \
      --province PROVINCE.md --skill SKILL.md                  -> rows 20 verified 20 / province rows 20 matched 20 /
                                                                  skill description names 9 of 9 non-none lanes /
                                                                  skill description length 1008 of 1024          (exit 0)
$ python3 mutate.py   # 28 mutants: write -> self-test -> restore -> sha256 check    (exit 0)
    killed 17, survived 11; every mutant restored byte-exactly (sha256 check True for all 28)
$ python3 probe.py    # pristine vs mutant on the same input: T1, S2, K2, M3 diff=YES;
    M2, M6 diff=YES in the second probe run (the first M6 run used the wrong lane map)
$ git -C lane status --porcelain                              -> (empty)
$ sha256sum lane/verifiers/check_sibling_census.py pristine.py -> 2f9d8a88...2eedc7 (both, identical)
```

Harness and probes (scratch directory only, not in the repo): `/fast/scratch/hyaku/kotoba-r50/falsify/MutGuardCode/{mutate.py,probe.py,pristine.py,full_output.txt}`.

## Bounds and tooling

- The lane repo was read only; the only file written there is this report. All mutation and execution happened in `/fast/scratch/hyaku/kotoba-r50/falsify/MutGuardCode/`. No `jj` command and no git write command was run in the lane, the fleet root or any sibling repo.
- No tool was installed or upgraded for this seat. Versions used: `python3` 3.14.8 (system), `git` 2.56.0 (system); `python3 -B` so no bytecode files were written.
- Judged axis: adjacency. The C1 live counter and its guard reproduce at `956ee1676e4c18480bce8ac3993541462be76e11`; the gaps above are in the guard's self-test, not in the C1 statement. C2 (`--box-proof`) was outside this seat's surface.
