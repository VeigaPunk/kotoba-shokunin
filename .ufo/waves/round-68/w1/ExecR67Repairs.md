# ExecR67Repairs — C2 routed-repairs counter (round-68 wave 1, executor seat)

Seat: executor (judged on `consistency`). Deliverable: the independent C2 counter draft at
`.ufo/waves/round-68/w1/drafts/check_r67_routed_repairs.py` (662 lines, Python stdlib only).
Nothing written outside `w1/drafts/`; `verifiers/`, `corpus/`, `LOG.md`, `SCORECARD.md` untouched;
no git/jj mutation anywhere (the draft's gate run is read-only on the lane: `git archive` +
throwaway extraction; the throwaway clone used for the agreement matrix was deleted after use).

## 1. What was built

`check_r67_routed_repairs.py --rev <full-sha> [--repo <lane>]` prints
`r67 routed defects closed N of 4`; exit 0 iff N == 4, exit 1 for a content shortfall, exit 2 for
usage/environment (missing/unknown `--rev`, unreadable repo, gate unrunnable, or the pinned base
not scoring 0 of 4). `--repo` defaults to the lane root found by walking up from the script, so the
same file works from `w1/drafts/` and installed under `verifiers/`. `--self-test` builds a fixture
repo (with a stub gate measuring the same nine check ids) and drives the base control, the honest
world through public `main()`, and one broken world per defect.

The four checks, all from committed bytes at `--rev` unless stated:

- **D1 (R67-1).** Each of `LOG.md`, `SCORECARD.md`, `corpus/lessons/round-68.md` carries the
  observed line `environment error: cannot read
  corpus/knowledge/instruction-authority-ladder-round67.md` **as a count gain against the pinned
  base** `e94ae32a5cd8dc3ee8e2d247816784bec2750cc0` (the append-proof), with the base hash prefix
  `2a8eba56` present. A record still carrying the unobserved `0 of 1` claim passes only because the
  correction supersedes it in the same record (append-only; the claim text is never rewritten).
- **D2 (R67-2).** Each record names the real path
  `.ufo/waves/round-67/controls/census-validate-append.txt` as a count gain against the base, and
  every line naming the wrong `w1/controls/` form stands ≤2 lines from a line naming the real path
  (the erratum names both; a bare wrong path would assert the wrong location). The r67 report and
  r67 lesson are frozen, never edited, so their surviving wrong path is out of scope by the
  repair's own terms.
- **D3 (R67-3).** `LOG.md` and the r68 lesson each name
  `.ufo/waves/round-67/w1/controls/junk-world` with its size (`254`), AND the path does not exist
  in the working tree of `--repo` (worktree conjunct by nature: an untracked leftover no revision
  carries).
- **D4 (R67-4).** `corpus/lessons/round-67-verifier-spotcheck.md` is tracked at `--rev`, and every
  expect in the committed `verifiers/corpus-baseline.json` equals the gate's own measurement at
  that revision: `git archive --format=tar <rev>` is extracted into a throwaway repo whose objects
  fall back to the lane's (so `commit `<hex>`` citations resolve as in place), the tree is
  force-added, and the revision's own `verifiers/verify_corpus_integrity.py` runs there with
  `--no-baseline --json`. All six zero-mode checks must measure 0 — that is the coverage-map index
  row, read through the gate's own fence-aware extractor (not a substring; the CriticC2-B1 class) —
  and the three equal-mode checks must match the stored expects. **No stored number is trusted.**

## 2. Behavior — exact evidence

```
$ python3 -B .ufo/waves/round-68/w1/drafts/check_r67_routed_repairs.py --self-test
self-test: 0 failure(s) over 23 assertions        (exit 0)

$ python3 -B .ufo/waves/round-68/w1/drafts/check_r67_routed_repairs.py \
    --rev e94ae32a5cd8dc3ee8e2d247816784bec2750cc0
control at e94ae32a: 0 of 4
D1-r67-1-erratum-appended: FAIL
D2-r67-2-real-receipt-path: FAIL
D3-r67-3-junk-disclosed-and-removed: FAIL
D4-r67-4-indexed-and-rerecorded: FAIL
r67 routed defects closed 0 of 4                  (exit 1)

$ python3 -B .ufo/waves/round-68/w1/drafts/check_r67_routed_repairs.py \
    --rev cafa29d0adb489b9b6b146445ee8bb9eef074e6e
control at e94ae32a: 0 of 4
D1…D4 all PASS; r67 routed defects closed 4 of 4  (exit 0)

$ … --rev 2cf0d99a6d5a3e1cb0b73e3b71cb495fd1eadc6f     # current master
r67 routed defects closed 4 of 4                  (exit 0)
```

The self-test's five broken worlds each kill exactly one defect: drop the LOG erratum (D1),
assert a bare wrong receipt path (D2), drop the lesson disclosure (D3a) and restore the junk
directory in the worktree (D3b), drop the coverage-map row (D4a), keep a stale baseline (D4b);
public `main()` is driven for exit 0/1/2 and the two frozen print lines.

## 3. Agreement with the landed instrument — and four divergences the L1 should read

The L1 landed its own counter (`verifiers/check_r67_routed_repairs.py`, at `605b84b`, current at
`2cf0d99`; worktree == HEAD as of this report). Per the r67 precedent (LOG.md:2640, the independent
implementation as the round's outside-direction check), I ran the **committed** L1 instrument in a
throwaway clone (never against the lane — see divergence 2):

| revision | L1 committed counter | this draft |
|---|---|---|
| base `e94ae32` | `environment error: cannot read corpus/lessons/round-68.md at e94ae32…`, **exit 2** | `r67 routed defects closed 0 of 4`, exit 1 |
| tip `2cf0d99` | `r67 routed defects closed 4 of 4`, exit 0 | `r67 routed defects closed 4 of 4`, exit 0 |

1. **Base classification (R67-1's class, re-appearing).** The L1 counter `_materialize`s all three
   records and raises environment error when one is missing — at the base that prints an
   `environment error: …` line and exits 2, so its own docstring's stated control ("at the pinned
   base … must print `r67 routed defects closed 0 of 4` and exit nonzero") does not hold, and its
   `main()` enforces no base control at all. A missing record at the base is the *content* verdict
   "repair absent", exactly the misclassification round 68 is correcting for C1. My draft prints the
   content verdict and pins the base control in `main()` (r66 pattern).
2. **D4 substrate mutates the lane.** The L1 `_baseline_values` runs `git checkout <rev> -- corpus
   verifiers` **inside `--repo`** — it rewrites the lane working tree and Git index as a side
   effect of measuring (and races concurrent writers). My gate run is read-only on the lane by
   construction (archive → throwaway repo with object alternates → force-add there).
3. **D4 coverage.** The L1 compares only 4 of the 9 ids (tracked_files, unindexed, report_total,
   commit_total); stale_patterns, missing_paths, report_dead, commit_unresolvable and
   commit_nonhash go unverified at the measured revision. Mine enforces all nine, plus
   zero-modes == 0 explicitly. Its index-row test is a per-line table-cell match over the whole
   README (not fence- or section-scoped); mine lets the gate's own `unindexed` measure prove the
   row.
4. **D1/D2 are presence floors there, count-gains here.** The L1 checks its constants against the
   joined records (its docstring discloses this). Consequences: its D2 is satisfied by the base's
   pre-existing legacy line `LOG.md:2641` (which already named the real path), so D2 could never
   distinguish the erratum; its D1 passes with the correction in only one record. Mine requires the
   correction in each of the three records as a count gain against the pinned base, with the
   wrong-path window rule (≤2 lines) killing a bare wrong-path assertion. Cosmetic extra: its
   `for/else` suppresses the D4 `closed` increment whenever an earlier defect failed (verdict
   unaffected). Its committed `--self-test` (6 assertions) injects synthetic records, never runs
   the gate and never drives public `main()` — the r67 review precedent
   (`.ufo/waves/round-67/w1/ReviewCounter.md`) asked for the public-main measurement path; mine
   drives it with 23 assertions including exit codes.

## 4. Remaining risks

- The ±2-line window (D2) is a textual convention; an erratum reflowed past that distance flips
  D2 red — intentionally strict, documented in the docstring.
- D4 depends on the gate's CLI surface (`--no-baseline --json`, `results` rows); a gate CLI change
  re-sides as exit 2 (fail-safe, never a false PASS).
- The D3 worktree conjunct observes the live tree at run time (unavoidable for an untracked
  leftover; the disclosure half is committed-bytes).
- Master moved three times while this seat ran (`605b84b → cafa29d → 2cf0d99`); the receipt runs
  above pin exact revisions. My draft is currently untracked at
  `.ufo/waves/round-68/w1/drafts/check_r67_routed_repairs.py` (not in `2cf0d99`'s snapshot).

## 5. Blockers

None.
