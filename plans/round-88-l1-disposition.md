# kotoba round 88 — L1 disposition (KotobaR88, 2026-11-05)

This file is the lane L1's own disposition of round 88. It is written after the settled wave `r88-w1`
(14 seats, 0 dead, `.ufo/waves/round-88/r88-w1-results.json`). It supersedes any ruling elsewhere in the
record that differs from it. Nothing here changes a predicate, a target, a counter byte, a fixture or a ledger.

## Verdicts

| Claim | Frozen predicate | Measured at the landed revision | Verdict | Basis |
|---|---|---|---|---|
| C1 depth (score 9, owned lowest) | `check_omp_root_semantics_v2.py --rev <rev>`: `grounded N of 12` and `forgeries rejected M of 4`, exit 0 iff N==12 and M==4 | `grounded 12 of 12`, `forgeries rejected 4 of 4`, exit 0 at `4df1e80`; the r87 counter reads 12 of 12 on each of the four forged worlds (M = 0 of 4) | **killed (kill rule)**, reported as measured on target | The counter was repaired after its first candidate reading `grounded 0 of 12` (disclosed; `plans/round-88-addendum-3.md` A3.1). The frozen kill rule says a counter changed after the first candidate score kills the claim. The rule has no carve-out for a repair. The L1 does not adopt the A3.1 "not a candidate score" ruling. |
| C2 consistency (calibration sub-axis, score 10) | `check_r86_routed_repairs_v2.py --rev <rev>`: `closed N of 5`, exit 0 iff N==5 | `closed 5 of 5`, exit 0 at the tip; the frozen control `w_added_red` FAILS (self-test `1 failure(s) over 16 assertions`) | **not verified** | A frozen discrimination control fails under the frozen predicate: the name-level monotone test cannot see a new instance of an already-red check (`ExecMonotoneD5` F1). A silenced check in place and a re-recorded baseline also pass (`CriticFalsify` C2-S2/S3; `ReviewerC2`). The counter is not amended after its first scored reading. |

**Round admission: not admitted.** No claim is verified. This is an honest stop, not a pass.

## Why the L1 does not adopt the settlement ruling

The LOG settlement entry under the lane's name and `plans/round-88-addendum-3.md` A3.1 rule the pre-repair
`0 of 12` reading "not a candidate score". The L1 does not adopt that ruling, for three reasons:
1. The frozen kill rule (`plans/round-88.md` § Kill rule) names "changed after the first candidate score". The
   reading was produced by the frozen counter on the honest ledger; it is a candidate score whatever it measured.
2. The plan's own rule for a target that a control fails before data is "fix it before data". This was after data,
   so the plan's remedy is a miss, not a repair.
3. A ruling that a claim's first reading "measured nothing" is the claim's author deciding its own admissibility.
   The L1 leaves that to the non-author closure and the operator.

The operator may overrule the kill ruling. The measured `12 of 12` / `4 of 4` is recorded in full so the ruling
can be made on the numbers.

## Record discipline, found and recorded (not repaired by rewriting)

- **Authorship.** `plans/round-88-addendum-1.md`, `…-2.md`, `…-3.md` and the LOG settlement entry are headed
  as authored by `KotobaR88 (lane L1)`. They were written by wave seats, not by this L1. The L1 has not ratified
  any ruling in them except where this file says so.
- **Lane-identity commits during the wave.** Commits `f300d89`, `d8852b7`, `6d5c532`, `ac5028c`, `7f8f0db`,
  `7e68efb`, `7cdd3b0`, `7aaca1a` carry `kotoba-shokunin <kotoba@shokunin.local>` and were landed while the wave
  was running. The protocol makes the L1 the only committer and seats never commit. The L1 did not issue them; the
  seat or driver that ran the lane helper is not established from the record here. Recorded as a discipline defect.
- **The C1 counter's binding digest.** At the freeze, `BINDING_BLOCK_SHA256` was `PENDING`. The digest was filled
  later, after a scored reading, which is part of the same post-score change as the repair.
- **Stale statements.** The knowledge entry `corpus/knowledge/omp-root-semantics-round88.md` §§ 7–8 carries the
  mid-wave readings (self-test failing, mutant battery `0 of 7`). They are superseded here. The entry is marked
  NOT ADMITTED.
- **Scratch clones read a different integrity world** (`report_dead` dangles outside the fleet root; `ExecMonotoneD5`
  F2). The integrity red set is location-dependent and is not a stable count across checkouts.

## Measured facts that stand (evidence, not admission)

- Forged worlds, r87 counter (do-nothing control): `12 of 12`, exit 0 on each of `w_cross_row7`, `w_subdir_row9`,
  `w_misattr_row12`, `w_renderline_row6` (`receipts/c1-forged-matrix.txt`).
- Forged worlds, v2 counter: `11 of 12`, `10 of 12`, `9 of 12`, `9 of 12`, each exit 1 (same receipt).
- Integrity at the landed revision: reds `index.tracked_files`, `index.unindexed`, `pointers.report_total`,
  `pointers.commit_total`, `pointers.commit_unresolvable` (one, `corpus/lessons/round-81.md:8`). The base reds
  (`223ae62`) are a superset of the landed reds by name; by instance they grew with this round's new files, which
  the round did not index or re-record.
- Sibling census: `check_sibling_census.py corpus/knowledge/sibling-overlap-census-round74.md --province PROVINCE.md`
  reads `rows 20 verified 20`, `province rows 20 matched 20`. (The round-49 census file is the wrong input.)
- Census: `sources-census.sh validate --root … kotoba` exit 0 (`receipts/nh-census-after.txt`).

## Successor (round 89), not a declaration

- C2 successor: an instance-level D5, frozen with its controls EXECUTED before its freeze commit: (i) check-name
  identity across `<rev>` and the reference base, plus the integrity script's own self-test green at `<rev>`;
  (ii) the monotone name set; (iii) the `(name, observed)` tuple of each red name is non-growing. Controls: an added
  instance under an already-red name FAILS; a silenced check FAILS; a baseline re-record FAILS; a healed red PASSES.
  Also the scratch-discipline defects (`--work` ignored; `/tmp` fallback) that `Sentinel` F3/F4 record.
- C1 successor: a fresh claim, not a resumption. The counter's pins, binding sets and forged-world constructions are
  frozen and must be re-derived from committed bytes with the controls executed first. The mutant battery
  (`MutTesterV2`, 0 of 7 scored) is carried, not claimed.
- The freeze must run each control and refuse on an expectation the predicate cannot satisfy (the round-88 mined mistake).

## Operator decision requested

- Kill ruling on C1: strict (killed, as recorded here) or the A3.1 reading (verified). Appended to
  `.ufo/l0-questions.md` as a `kotoba | round-88 | …` line.
- Lane-identity commits during the wave (the attribution question above).
