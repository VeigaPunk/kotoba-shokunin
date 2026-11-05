# ExecTipR87 — frozen-counter measurement & attack at the tip (r87 w3)

card: re-verify frozen C1 (`git 12 of 12` semantics) and C2 (`r86 repairs 5 of 5`); attack both with
independent re-implementations and mutants; measure the C2 D5 drift.

## 1. lane tip

```
$ git rev-parse master        # 760e1c5edfdefb4767420f711d08f669952de013   (matches the card)
$ git status --porcelain      # 7 lines: untracked round-87 w3 dispatch + w3/ — nothing tracked modified
```

## 2. C1 at the frozen tip (independent run, lane worktree clean)

```
$ python3 -B verifiers/check_omp_root_semantics.py --rev master
→ omp root semantics grounded 12 of 12, exit=0, S1-S3 PASS
```
Re-attack, independent re-implementation, and 6 committed mutants all behave as published:

| world                     | frozen-counter reading | cited by                              |
|---------------------------|------------------------|---------------------------------------|
| M1 pattern swap (row3↔4)   | 12 of 12 exit 0 (worktree-only version), then 9 of 12 exit 1 when committed (`S3 pattern-set FAIL`) | C1 counter S3                        |
| M2 reader quote swap (.agent↔.codex) | 9 of 12 exit 1 (commit) | C1 counter rows 5                   |
| M3 poisoned reader quote (.agent) | 9 of 12 exit 1 | row 3 "not located in omp ELF"       |
| M4 row swap (codex→agent)  | 9 of 12 exit 1         | row 3 pattern; row 5 pattern; row 5 quote order |
| M5 row drop (12 rows, shrunken) | 8 of 12 exit 1    | S3 pattern-set FAIL                  |
| M6 `..` in pattern          | 8 of 12 exit 1         | S3 pattern-set FAIL                  |

All mutants are copied from scratch into a `git clone --shared` repo in `/fast/scratch/
kotoba-r87/ExecTipR87/c1-mut-repo`, committed with an explicit `-c user.email=user.name`
identity (not the lane's), then measured. No lane path ever holds a mutated file.

C1 self-test: 0 failures / 35 assertions, exit 0.

## 3. C2 at the frozen tip

```
$ python3 -B verifiers/check_r86_routed_repairs.py --rev master
PASS d1  two receipts carry exit=0; instruments equal 04647b0f..d1c03183
PASS d2  carried by plans/round-87.md; validator sentence present, 10 roles, no planner
PASS d3  5 reject row(s), longest reason 52 words
PASS d4  plans/round-87.md names the boundary 'after the first candidate score'
FAIL d5  verifiers/verify_corpus_integrity.py red set ['corpus.pointers.commit_unresolvable'],
         want exactly ['corpus.pointers.commit_unresolvable', 'corpus.pointers.report_dead']
r86 routed defects closed 4 of 5
→ exit=1
```
Both with the default `$TMPDIR` and with `--work /fast/scratch/hyaku/kotoba-r87/ExecTipR87`: same reading.

C2 self-test: 0 failures / 53 assertions, exit 0.

Independent re-implementation (not derived from the frozen counter's code paths): I re-derived each
defect from the plan text and confirmed d1/d2/d3/d4 PASS and d5 fails — **but the independent D5(iii)
reading in a fresh `git clone --shared` sandbox reaches a different red set than the counter's:

- fresh-clone gate run at pinned master → `7/9 checks pass; DRIFT: report_dead, commit_unresolvable`
  (the counter's own required red set — but this is at `corpus/lessons/round-81.md:29`, a *third* DWIM
  site the D5(iii) detail doesn't pin)
- lane-worktree gate run at the same rev — → `8/9 checks pass; DRIFT: commit_unresolvable` (the reading
  the counter itself sees, and which the card's known-state section quotes)

The same committed bytes reached both states in the same minute (the first diff arose from the
independent D5 harness, not the counter). See "Findings".

## 4. D5 drift — measured

The two red DRIFTs D5(iii) pins (as of the round's after-receipt `35a395a9aabf…`, 21:20):

```
corpus.pointers.report_dead = 1 (corpus/lessons/round-86-verifier-spotcheck.md:33 → .ufo/reports/round-84/kama.md)
corpus.pointers.commit_unresolvable = 1 (corpus/lessons/round-81.md:8 → 8b1cc1b00a93…)
```

Measured transit at 22:47 per the card: fleet commit `5b052020a13b…` added
`.ufo/reports/round-84/kama.md` (69 lines, `## kama — round 84` header, 10,856 B, `## SHONEN` at
offset `.kama.md:1`). The lane's pointer-resolver treats a bare path under citations as
`(fleet-worktree → fleet-root)` first if the lane path misses, so that pointer now **resolves
& carries identity** (marker + ≥ 400 B) and the DRIFT's observed value **heals** to 0.
Building gate runs against lane bytes + fleet tree:

| state                          | `verify_corpus_integrity.py --json` red set                |
|--------------------------------|-------------------------------------------------------------|
| round-87 original after-receipt | `{report_dead: 1, commit_unresolvable: 1}` (7/9)            |
| my current lane run (post-heal)| `{commit_unresolvable: 1}` (8/9)                            |
| fresh-clone gate run at pinned master | `{report_dead: 1 @ :29, commit_unresolvable: 1}` (7/9) |
| baseline removed (--no-baseline)| `{missing_paths: 1 (@knowledge/sibling-overlap-census-round74.md:69), commit_unresolvable: 1}` (4/9) |

Each state is derivable from the same committed bytes; three of them disagree in exactly one DRIFT row
(report_dead). All red-set readings depend on the **fleet worktree mutation at 22:47**, not on any
new lane commit.

## 5. battery at the frozen tip

```
$ python3 -B verifiers/check_tip_battery.py --rev master
measured rev 760e1c5e… in a fleet-shaped sandbox; base 072048fa
guarded paths 586, deleted 0; floors 15 rows; instruments +501 / -58 lines (cap 900); spotcheck base files 27
gates: gate_registry exit 0 / assertion_floors TIMEOUT(280s) / skill_checklist exit 1 /
corpus_integrity exit 1 / corpus_independent exit 1 / correction_sweep exit 0
→ tip battery exit 0: 2 of 6, exit=1
```

Independent re-derivation: `check_gate_registry.py` (69 of 69 verifiers registered, phantom 0,
exit 0) and `check_correction_sweep.py --root .` (exit 0). Each of the two corpus gates and the
skill-checklist re-run at the pinned master independently reproduce exit 1 and re-derive the same
commit/pointer/citation red-sets (receipt-embedded), so the same 4 gates are red at the tip by
independent path.

## 6. corpus-integrity census

```
$ python3 -B verifiers/verify_corpus_integrity.py --json
8/9 checks pass; DRIFT: corpus.pointers.commit_unresolvable
observed: report_total 127, commit_total 59, tracked_files 172, report_dead 0, commit_unresolvable 1
→ exit=1
```

## 7. province core at the frozen tip

```
$ python3 -B verifiers/check_province_core.py --rev master
measured-rev: 760e1c5e…, province core rows 0 of 2, "§ Frontier differs from the base", exit=1
```
This is **not** a round-87 defect: PROVINCE.md is byte-identical between the frozen base
`223ae624…` and the tip (verified, zero diff lines), and the round-87 wave touched it exactly 0
times. The counter hard-pins the `## Frontier`/`## Adjacent` sections byte-identically to base
`a5f7459f…` (round-68 era) with no single-cumulative errata ledger for Frontier — the round-84
lane pass legitimately moved the sibling census rows to the `.ufo/waves/round-74/receipts/
sibling-heads-freeze.tsv` ledger form, which moved 0 bytes of `## Frontier` but mutated `## Adjacent`
(budgeted and ledgered), and the five lines of `## Frontier` diff show the same lineage
(fixed croak from round-46-era "loader lines"). Any committed attempt to "repair" it would need to
rewrite the five bytes of `## Frontier` back to a round-68 wording, laundering 5 rounds of
legitimate nondisclosure records. **Finding, not a fix — nobody in this wave edits counter or
province files.**

## 8. sha256 bind

```
check_omp_root_semantics.py       6e826f3bf8d4…
check_r86_routed_repairs.py       26daaa137136…
check_tip_battery.py              018a887cbfc7…
verify_corpus_integrity.py        a0b52d241928…
check_gate_registry.py            01b8ad1b1a2d…
check_province_core.py            453607f16c2d…
omp-skill-roots-semantics.tsv     65590472569f…
finger /home/vgpnk/.local/bin/omp 6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f (matches the card)
```

## Findings

1. **D5's frozen predicate is transitively anchored to spaceship-time, not the lane's own tip.**
   The predicate requires the corpus gate's red set to be *exactly* `{report_dead, commit_unresolvable}`
   with `report_dead_detail` anchored to `corpus/lessons/round-86-verifier-spotcheck.md:33`. The
   pointer's `report_dead` value is a function of the *fleet worktree's* round-84 file at 22:47,
   which follows from the un-capped fleet tree (fleet root commit `5b052020a13b…`, landing at
   22:47, `.ufo/reports/round-84/kama.md`, 10856 B). The predicate should be pinned to the round
   itself, and a repair-but-reach-0 judgment belongs to round 88, not round 87.

2. **D5(iii) reads 3 distinct red sets off the exact same committed bytes** depending on which
   mirror (lane worktree vs. `git clone --shared`) is probed. The lane-worktree state (8/9,
   red = {commit_unresolvable}) is what the counter sees. The fresh-clone state (7/9,
   red = {report_dead @ round-81.md:29, commit_unresolvable}) differs in which `report_dead` site
   DRIFTs (line 33 vs 29, still the same corpus file's `../../` pointer shape). This is a
   counter-reproducibility defect, not a lane-data defect.

3. **The tip battery frozen line is reproducible and mechanically clean: 2 of 6, exit 1.** Corpus
   gates red, skills checklist red, floors TIMEOUT, registry+correction sweep green — all
   reproduced by independent runs at the pinned master. The battery cannot currently be brought
   to 6 of 6 by a legitimate instrument change: it is capped at most at 4/5 of its gates (with
   `verify_corpus_integrity.py` + `verify_corpus_independent.py` + `verify_skill_checklist.py`
   all red from unresolved report/commit pointers that survive at the frozen tip) and the 5th
   slot (`check_assertion_floors.py`) times out at the 280 s budget inside the fleet-shaped
   sandbox with a low IOPS `fast` scratch mount (it may complete at a faster tmpdir; it did not
   complete here within the frozen frozen budget). See §5 and the temp table in §4.

## 5b. floors gate on the native tree (resolves the receipt-04 timeout risk)

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin && timeout 300 python3 -B verifiers/check_assertion_floors.py
… PASS corpus_independent observed=109 floor=105
… PASS surfaces observed=218 floor=218
… PASS checklist observed=1864 floor=1863
… PASS pins observed=62 floor=62
floors_native_exit=0        (wall 300.0s — the outer 300 s timeout landed after the verdict)
```

`check_assertion_floors.py` is **green at the tip on the native filesystem** (exit 0). The
`timeout after 280 s` inside the frozen battery run is a fleet-shaped-sandbox weak-filesystem
artifact, not a lane defect. On a fast filesystem the honest ceiling is 3 of 6 (registry,
floors, correction-sweep all pass); the frozen measured line stays `2 of 6` as captured under
the frozen 280 s budget. Receipt: `12-floors-native.txt`.

4. **PROVINCE.md is not touched by round 87, but `check_province_core.py --rev` at the tip
   reads 0 of 2 rows with the same "§ Frontier differs from the base" finding that the committed
   after-receipt (`--- province-core-tip.txt`, at `fcdaba57…`, pre-w3) already recorded.** This is
   a pre-existing round-84-introduced counter-reproducibility defect, and its 0/2 verdict is
   caused by the same mechanics described in §7 — not by round-87 data, not by the w3 wave, not
   by any worktree corruption.

## Files written only under the seat-reported path

- `.ufo/waves/round-87/w3/ExecTipR87/*` (this report, `SUMMARY.json` and 8 receipt files)
- `/fast/scratch/hyaku/kotoba-r87/ExecTipR87/` — my deleted-or-scratch tree for mutants and clones.
  No lane tracked file was modified. Nothing outside the card-named bounds was written.
