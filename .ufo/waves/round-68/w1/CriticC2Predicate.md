# Critic — C2 predicate falsification (round 68, wave 1)

Seat: critic (read-only vs production; controls built in `.ufo/waves/round-68/w1/controls/c2falsify-clone`,
a throwaway `git clone` of the lane — the lane worktree/index untouched: `git diff HEAD -- corpus verifiers`
= 0 lines at close). Base `e94ae32a…`, tip `cafa29d0…`.

## Verdict

**The frozen C2 predicate stands as frozen at the tip — all three conjuncts reproduce — but it
does not certify the substance the round narrates, and the instrument breaks two of its own
documented properties.** Tip: `9/9 checks pass` exit 0 · independent `--json` exit 0 ·
`r67 routed defects closed 4 of 4` exit 0. Before, as written in the plan: primary `6/9` exit 1
with `tracked_files 122/121`, `unindexed 1`, `report_total 85/82` (receipt
`controls/C2-base-integrity.txt`, reproduced); independent exit 1; instrument absent at base.

## Controls built and run (all in the scratch clone; revs are clone-local)

| # | Control | Result | Exit |
|---|---|---|---|
| C0 | HEAD counter `--rev e94ae32a` (its own base contract) | stdout **empty**; stderr `environment error: cannot read corpus/lessons/round-68.md at e94ae32a…` | 2 |
| K2b | index row alone at base (correct `lessons/` token, baseline stale) | `7/9 checks pass` (DRIFT tracked_files, report_total) | 1 |
| K3 | baseline re-record alone at base (expects = `--no-baseline` observation 122/85/38) | `8/9 checks pass` (DRIFT unindexed) | 1 |
| **E2** | **rubber-stamp row at HEAD**: landed contentful row replaced by `| (critic stub: names the file, carries no content) | \`lessons/round-67-verifier-spotcheck.md\` |  |  |` | **primary `9/9` exit 0 · independent exit 0 · counter `4 of 4` exit 0** (rev aee79021) | **0** |
| **F2** | **denial records**: LOG paragraph asserting the *opposite* of R67-1/2/3 while containing the three required substrings | **`4 of 4` exit 0** (rev b50c3d8c) | **0** |
| D2 | junk-world disclosure deleted, erratum text kept | `2 of 4` exit 1, single finding `D3: … disclosure … missing, or the path still exists` | 1 |
| B | junk-world dir re-created (empty) at fixed rev | `2 of 4` exit 1 — verdict at a pinned rev flips with worktree state | 1 |
| **G** | future round committed (README append, HEAD=c71f79ba), counter `--rev cafa29d` | counter returns `4 of 4`, but leaves **`M  corpus/README.md` staged** in the measured repo | — |

## Findings

1. **Rubber-stamp succeeds (E2).** A contentless coverage row + the honest baseline satisfies all
   three conjuncts. The counter's D4 checks `cells[1]` equals the backticked path and the baseline
   equals its own re-measurement; the row's other cells are never read. The baseline half *is*
   bound (a copied-wrong number fails — K3/D4 findings path), so the only soft spot is row
   substance — exactly attack (1)'s candidate. The r66 M101/M99 class is live again.
2. **D1/D2 are name-only floors, demonstrated (F2).** Text denying all three defects closes them.
   Disclosed (docstring, QUALITY Q33) but now proven end-to-end; the substantive re-runs the
   docstring leans on ("the re-run of the r67 counter at the r67 base") are outside the predicate.
3. **The counter's base contract is false — the R67-1 class recurs in the new instrument (C0).**
   Docstring: "At the pinned base it must print `r67 routed defects closed 0 of 4` and exit
   nonzero." Observed: empty stdout, exit 2 (`corpus/lessons/round-68.md` cannot exist at base →
   EnvError). M107's fix ("a missing entry is a content verdict, not an environment error") was
   applied to the C1 counter only; no receipt shows a C2-counter base run.
4. **The counter mutates the measured repo's Git index (G).** `_baseline_values` runs
   `git checkout <rev> -- corpus verifiers` in the live repo, rewriting index+worktree; docstring
   claims "reads the COMMITTED bytes at `--rev` (never the working tree)" — false for D4. Latent
   until any re-verification measures a non-HEAD rev after corpus edits (wave 2's use case); in
   the jj-colocated lane the next jj command would snapshot the reverted state. At HEAD it is
   benign (verified: lane diff vs HEAD after my runs = 0 lines).
5. **Count misdiagnoses (D2).** With only D3 failing it prints `2 of 4`, not `3 of 4`: D4's
   for/else credits it only `if not findings`, so one text defect suppresses D4's credit even when
   D4's own checks pass (no D4 finding is printed, yet D4 is not counted).
6. **D3's removal half is worktree-bound (B).** A pinned rev's verdict flips when the dir is
   re-created, and a fresh clone of the same rev auto-passes `exists()` — the R67-3 removal is not
   provable from committed bytes at all.
7. **Count `4 of 4` is right.** The spotcheck routes exactly 4 actionable defects; item 5
   (weekly-quota L0) is "already filed … Not duplicated here".
8. **Do-nothing halves hold for the gate, vacuously for the counter.** K2b 7/9 exit 1, K3 8/9
   exit 1 — each half red as claimed. The counter half of the sentence ("reaches neither 9/9 nor
   4 of 4") can never be exercised at a pre-r68 rev (finding 3), so it was never a live test.
9. **Side finding, already in the L1's own receipt:** `noharm-at-tip.txt` records the gate-registry
   verifier RED at tip — `check_r67_routed_repairs.py  no self-test cell names no backticked flag`,
   `45 of 46`, exit 1. The C2 counter has no `--self-test`; "no owned-axis harm" is contradicted by
   the committed receipt on the claim's own axis (consistency).

## Smallest safe corrections (round-routed, none score-affecting)

1. C2 counter: missing RECORDS at `--rev` → content verdict `0 of 4`, exit 1 (mirror the C1 fix;
   M107's own rule), or amend the docstring contract and append an erratum if the base print is
   declared unreachable.
2. Add `--self-test` to the C2 counter (stub-row, disclosure-deleted, baseline-mismatch,
   missing-record worlds) — cures the red registry row (45→46 of 46).
3. `_baseline_values`: materialize with `git archive <rev> | tar -x -C <tmp>` (or a temp
   worktree) — never `git checkout` in the live repo.
4. Credit D4 independently of other findings so `N` diagnoses per defect.
5. Disclose D4's row check as a presence floor (QUALITY Q33) and pin the stub-row world in the
   self-test; text floors cannot be made substantive, only bounded and named.
