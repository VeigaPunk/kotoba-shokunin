# MutDescGuard — round-50 falsify: description mutants against the C1 guard

**HOLDS-BOUNDED** — applies to C1 (adjacency): "kotoba's `SKILL.md` frontmatter `description` value names the census lanes classed non-`none`, each in a clause that carries an ownership or routing word: guard line `skill description names K of N non-none lanes`, 5 of 9 → 9 of 9". Every mutation the round-50 plan's re-sizing note names as the counter's red arms is **killed** at `956ee167` and at the lane's later landings (`a78fec1`, `bf109ca`, `87eeae2`): removing any one of the nine lane names, a bare list of the nine names, a negated sentence, a capitalised duplicate replacing one name, a YAML comment line carrying four names, an over-1024-character description, and a lane named only in the discovery-root note clause. Two mutants survive — a **false split** (`chousa owns SKILL.md audits`) and the same false split in the other direction (kotoba gives away its own audit ground) — and both are **already bounded by the claim statement** (SCORECARD adjacency row: "Bounded: the clause test is lexical (a false ownership sentence that names the lane passes, seat mutant m9)"; the census entry says the same; `LOG.md` round-51 candidate: "a pinned owner phrase per `adjacent` row so the description guard catches a false ownership sentence"). Those two are a **known coverage gap of the lexical rule, not a contract miss**. A third, sharper survivor I found — a **marker leaking across a sentence boundary** — is *not* named by any existing bound and is a bounded coverage finding. A fourth: the "first 99 characters unchanged" clause asserted in the `LOG.md` C1 entry and the lesson is turned on by **no verifier** (a Q26 finding of the M31 class).

Read-only on the lane checkout: no file there was edited except this report. All mutation happened in `/fast/scratch/hyaku/kotoba-r50/falsify/mutdescguard/` (private clones; scripts `mutate.py`, `mutate2.py`–`mutate10.py`, `mutateA.py`; JSON `results2.json`, `results3.json`).

## Detector (the same bounded detector on pristine, mutated and restored bytes)

```
python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md --skill SKILL.md
```

Exit 0 = pass, exit 1 = a check failed. Pristine at `956ee16`: exit 0, `skill description names 9 of 9 non-none lanes`, `skill description length 1008 of 1024`, `rows 20 verified 20`, `province rows 20 matched 20`. The baseline is green, so every exit-1 below is a kill, not a pre-existing red. The **before column**, measured with the landed guard on the base bytes (`git show f3046466:SKILL.md`): exit 1, `skill description names 5 of 9 non-none lanes`, four FAILs (chousa, kama, kotodama, tameshi). The claim's before/after pair reproduces.

## Mutant table

Every mutant replaces the frontmatter `description` value only; the rest of `SKILL.md` is byte-identical to the judged revision. "names line" is the guard's own stdout line.

| # | mutant | exit | `names K of N` line | len | killed / survived |
|---|---|---|---|---|---|
| m00 | base (control, re-wrapped) | 0 | `names 9 of 9 non-none lanes` | 1008 | pass (control) |
| m01–m09 | drop **chousa / kagi / kake / kama / kasegi / kengaku / kotodama / kumitate / tameshi** (nine mutants, one per lane) | 1 each | `names 8 of 9 non-none lanes` each | 975 / 1002 / 1002 / 975 / 1000 / 948 / 904 / 995 / 962 | **killed** ×9 |
| m10 | bare list of the nine names | 1 | `names 0 of 9 non-none lanes` | 78 | **killed** (9 FAILs) |
| m11 | negated sentence | 1 | `names 5 of 9 non-none lanes` | 841 | **killed** (4 FAILs) |
| m12 | capitalised duplicate replacing one name (`Kagi owns…` in chousa's slot) | 1 | `names 8 of 9 non-none lanes` | 1006 | **killed** |
| m13 | YAML comment line after the description carrying 4 names | 1 | `names 5 of 9 non-none lanes` | 792 | **killed** (4 FAILs) |
| m14 | description over 1024 characters | 1 | `names 9 of 9 non-none lanes` | 2608 | **killed** (length arm) |
| m15 | lane named only in the discovery-root note clause | 1 | `names 8 of 9 non-none lanes` | 1016 | **killed** |
| m16 | **false split** — `chousa owns SKILL.md audits` | **0** | `names 9 of 9 non-none lanes` | 1004 | **SURVIVED** |
| m17 | false split, other direction — kotoba gives away its audit ground | **0** | `names 9 of 9 non-none lanes` | 1004 | **SURVIVED** |
| m18 | lane named only in a lower-case `not` clause | 1 | `names 8 of 9 non-none lanes` | 1023 | **killed** |
| m12b | capitalised repeat of the **same** name (`Chousa owns…`) | 0 | `names 9 of 9 non-none lanes` | 1008 | survived — **correct**, one lane counted once |
| m19 | two lanes in one clause, one marker | 0 | `names 9 of 9 non-none lanes` | 1000 | **SURVIVED** (marker on the wrong lane) |
| m20a | lane with **no marker of its own**, marker leaked from the previous sentence | **0** | `names 9 of 9 non-none lanes` | 1020 | **SURVIVED** — new, see below |
| m20b | the same words with a capital letter after the period | 1 | `names 8 of 9 non-none lanes` | 1020 | killed — proves the mechanism |
| m21 | lane named only as the repo-directory form `kotodama-shokunin` | 0 | `names 9 of 9 non-none lanes` | 985 | survived — the `-shokunin` form counts as the lane |
| m25 | description's **first 99 characters** rewritten | 0 | `names 9 of 9 non-none lanes` | 999 | survived — **no verifier turns on it** |

## Survivors, and whether the claim statement already bounds them

**m16 / m17 — the false split. Already bounded.** `chousa owns SKILL.md audits` names chousa in a clause carrying `owns`, so G1 binds it; the guard cannot see that the split is false. This is the build seat's own recorded mutant **m9** (`.ufo/waves/round-50/build/CensusGuard.md:198-206`: "Known pass (recorded, not hidden): m9 … G1 cannot see that the split is false") and the critic's `CriticC1Sizing.md` m9. The bound is explicit in three places: the SCORECARD adjacency row ("the clause test is lexical (a false ownership sentence that names the lane passes, seat mutant m9)"), the census entry § Round 50 ("The clause test is lexical: a clause that names a lane next to a false ownership word still passes"), and the guard's own docstring ("The marker rule is a lexical approximation, not a parse of intent"). `LOG.md` round 51 already carries the fix as a candidate. **Not a contract miss; a known lexical-approximation gap, carried.**

**m19 — the marker attaches to the wrong lane. Already bounded.** `chousa does research and kama owns endpoint verification` binds chousa to kama's `owns`. The census entry names this direction too, and `CensusGuard.md:250` records the false-positive direction explicitly ("a marker in a clause that does not really attach to the lane").

**m20a — the marker leaks across a sentence boundary. NOT bounded; new.** The description reads `…fixes route to the owning lane. chousa research ownership stays with kotoba.` chousa's own clause carries **no** ownership word (`ownership` is not in the marker list; `own` does not match inside `ownership` — the marker regex is whole-word). But `CLAUSE_SPLIT` (`check_sibling_census.py:442`) splits a sentence end only on `(?<=[.!?])\s+(?=[A-Z])` — a **capital** letter. Because `chousa` is lower-case the period does not close the clause, so chousa's text is glued to the preceding `fixes route to the owning lane.` and inherits its `route` marker. The guard prints `names 9 of 9 non-none lanes`, exit 0. Proof that the mechanism is the capital letter and nothing else: the identical words with `Chousa` capitalised (m20b) split the clause and are **killed** (`names 8 of 9`, exit 1); `Chousa is a sibling lane` (m24) likewise.

This is a **coverage finding, not a contract miss**: the claim says "each in a clause that carries an ownership or routing word", and chousa *is* in a clause that carries one under the guard's own (lexical) clause definition, which the guard and the census entry both declare an approximation. But the guard's docstring names two counterexamples ("a clause with a marker but no lane is harmless, a lane named in a clause without a marker is refused even when the surrounding sentences do state a split") and **not** this third case: a lane whose own sentence carries no marker, bound anyway because a **lower-case sentence start** failed to close the previous clause. Cheap fix in the spirit of the round-50 `m8` fix to `description_of`: make `CLAUSE_SPLIT` break a sentence end on `(?<=[.!?])\s+` regardless of the next letter's case, or require the marker to sit in the same sentence as the lane.

**m21 — the `-shokunin` repo-directory form counts as the lane.** `token_in` (`…:403`) matches `kotodama` inside `kotodama-shokunin` because the trailing boundary excludes only `[a-z0-9]`, not `-`. The build seat recorded the same shape as **m6** ("the suffixed names are whole tokens under `token_in`, so they count as *mentions* but the clause carries no marker"); with a marker present (m21) it binds. Whether it should count is unsettled in the corpus: a bounded observation, not a defect.

**m12b — a capitalised repeat of the same name survives, and that is correct.** The guard counts each lane once, case-insensitively; the claim says "names each census lane", not "names it exactly once". The build seat's own m7 arm asserts the same ("capitalised repeats counted once"). **Not a finding.**

**m25 — the "first 99 characters unchanged" clause is not measured by anything.** The round-50 `LOG.md:2393` C1 entry and `corpus/lessons/round-50.md:50` both state the description kept its "first 99 characters unchanged". Rewriting the first 99 characters leaves **every** verifier's exit code identical: `check_sibling_census.py --skill` exit 0 → 0 (only the length line moves, 1008 → 999); `verify_skill_checklist.py` exit 1 → 1 (the same pre-existing `trigger.citation_resolves` FAIL, a path artefact of the scratch clone — the sibling fleet report is outside it); `verify_corpus_integrity.py` 1 → 1; `verify_surfaces.py` 1 → 1; `check_substrate_pins.py` 1 → 1. Nothing reads the first 99 characters. The clause is true of the landed bytes (base and landed first-99 strings are byte-identical), so it is a **statement without a counter**, not a false statement — the M31 class (a headline asserting properties its counter never measured), applied to a clause the round-50 statement added.

## Q25 / Q26 on the C1 claim

**Q25 (counter shown able to fail): PASS.** The guard's exit code changes on 11 of the 13 contract-targeting mutants; the base is green, so each exit-1 is a kill.

**Q26 (statement asserts nothing its counter does not measure): HOLDS for the statement as re-sized.** Each clause is turned on: "names the census lanes classed non-`none`" by the nine drop mutants (each names its lane in the FAIL); "each in a clause that carries an ownership or routing word" by m10/m11/m13/m15/m18/m20b; the count clause by the guard's own stdout line; the 1024-character clause by m14. The membership list is read from the census file's own `classification` column, not hard-coded, so the D3 ruling moving a row moves the list with it. The one clause **not** turned on anywhere is the "first 99 characters unchanged" clause, which sits in the LOG entry and the lesson rather than in the plan's re-sized statement text (m25 above).

## Cross-checks

- The **rejected first counter** (case-sensitive, whole-frontmatter name count) was run on every mutant for contrast: it prints 9 on m10 (bare list), m11 (negated), m13 (YAML comment), m14 (over-length), m15, m16, m17 — the arms the round-50 critic rejected it for. The landed guard prints 0, 5, 5, 9(fail), 8, 9, 9. The re-sizing fixed the arms the critic named.
- The plan's **case-folded parsed-description cross-check** agrees with the guard's count on every mutant (9/8/8/8/8/8/8/8/8/8, 9, 9, 8, 8, 5, 9, 9, 9) except where the guard's clause rule binds more or fewer than a raw name count — m10 (9 vs 0), m11 (9 vs 5), m13 (9 vs 5), m15 (9 vs 8), m18 (9 vs 8). The guard is the stricter of the two.
- **Parser agreement with PyYAML**: `description_of` and `yaml.safe_load` agree exactly on the base and on m10, m13, m14 (1,008 / 78 / 136 / 2,608 characters, all equal). The round-50 `m8` fix to `description_of` holds: a column-0 YAML comment is not swallowed into the value by either parser.
- **Guard self-test**: `python3 -B verifiers/check_sibling_census.py --self-test` → `self-test: 0 failure(s) over 68 assertions`, exit 0. **Floors gate**: `python3 -B verifiers/check_assertion_floors.py` → `PASS sibling_census observed=68 floor=68`, exit 0 — the D3 registration is live.
- **Reproduction at the lane's later landings**: all 18 verdicts reproduce unchanged at `a78fec1`, `bf109ca` and `87eeae2` (`SKILL.md` sha256 `834dd842…`, `05457302…`; base exit 0 `names 9 of 9`; every drop exit 1 `names 8 of 9`; bare list exit 1 `names 0 of 9`; negated exit 1 `names 5 of 9`; caps-duplicate exit 1 `names 8 of 9`; comment exit 1 `names 5 of 9`; over-1024 exit 1; discovery-note exit 1 `names 8 of 9`; both false splits exit 0 `names 9 of 9`).

## Restoration evidence

The judged file, `SKILL.md` at `956ee167`, sha256 `9fe2ca74b00ce51e087237c34d031a576ad8c191b642612b447fd53c26340702`, is byte-identical after every mutant: each run rewrote the bytes, ran the detector, then wrote the original bytes back and asserted `sha256 == 9fe2ca74…`. After the final mutant the guard on the restored file printed `skill description names 9 of 9 non-none lanes`, `skill description length 1008 of 1024`, exit 0, and `SKILL.read_bytes() == BASE_BYTES` was `True`. The same check at `a78fec1` restored sha256 `834dd842…` and at `87eeae2` restored sha256 `05457302…`, both with `bytes_equal True`. The lane checkout was never written to except this report; `SKILL.md` there carries only peers' later landings and its working-tree hash matches HEAD.

## Tools

No tool was installed or upgraded by this seat. Python 3.14.8 (`python3 -VV`), git 2.56.0, PyYAML 6.0.3 (already present), all used from the system. No network fetch was needed.

## Recommended follow-ups (not applied; the seat is read-only on the lane)

1. Tighten `CLAUSE_SPLIT` so a sentence end closes a clause regardless of the next letter's case, or require the marker to be in the same sentence as the lane — kills m20a without touching m20b.
2. Give the "first 99 characters unchanged" clause a counter, or drop it from the `LOG.md` C1 entry and the lesson line (it is the M31 class applied to a round-50 clause).
3. Decide whether the `-shokunin` repo-directory form should count as naming a lane (m21).
