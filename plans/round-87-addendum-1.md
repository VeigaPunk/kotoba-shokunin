# kotoba round 87 — addendum 1 (committed before the first candidate score)

Freeze: `669f2801c31ef27e18cc35a327d2e18f466281c7` (`plans/round-87.md` alone).
This addendum corrects **one measured miscount** and **one measurement mechanism**. It changes no
target, adds no claim and ships its own re-run controls.

## A1.1 — C1's denominator is 12, not 13

`plans/round-87.md` § C1 says "13 rows whose `root_pattern` equals the round-86 ledger's 13
patterns" and freezes the predicate `omp root semantics grounded N of 13`. The round-86 ledger
carries **12 data rows**:

    git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show 223ae62424f8ab1eb365d733eb648d6228ddd7e8:verifiers/omp-skill-roots.tsv | tail -n +2 | wc -l
    -> 12

The lane's own round-86 knowledge entry states it too:
`corpus/knowledge/omp-catalogue-model-round86.md:101` — "`root_pattern<TAB>binary_quote`, 12 rows)".
The plan's 13 is the ledger **file's** line count (header + 12) — the L1's counting error, found by
the `Sentinel-4` seat before any candidate world was scored.

**Corrected predicate** (the same sentence in the counter's docstring, in `SKILL.md`'s registry row
and in every receipt):

    python3 -B verifiers/check_omp_root_semantics.py --rev <rev>
        -> prints "omp root semantics grounded N of 12", exit 0 iff N == 12 and guards S1-S3 all
           PASS; exit 1 otherwise; exit 2 = could-not-evaluate.

Everything else is unchanged: the four per-row conjuncts, the three guards, the target "every row of
the ledger grounded", the base expectation (`0 of 12`, exit 1) and the six forgery worlds. The
denominator follows the committed ledger; the claim still requires **all** rows grounded, so the
target is not narrowed in the sense the kill rule forbids (nothing is admitted by shrinking the
denominator: a 12-row ledger with one ungrounded row is `11 of 12`, exit 1).

**Admissibility** (the round-86 closure's ruling, `corpus/lessons/round-86-verifier-spotcheck.md`
§ 2, whose wording this round adopted as its kill rule): this commit precedes the first candidate
score — the only readings taken so far are the base reading (`0 of 13` at `669f280`, a base
measurement, not a candidate) and the seat's own defect report; no candidate world has been scored.
It does not widen the target and it does not change the predicate's condition, only the miscounted
constant.

**Re-run controls (committed with the counters):** `w_base` (the base revision → `0 of 12`, exit 1),
`w_honest` (12 grounded rows → `12 of 12`, exit 0), and the six forgery worlds
(`w_noledger`, `w_docquote`, `w_nomodule`, `w_dotdot`, `w_star`, `w_shrink` (11 rows), `w_bound`,
`w_offset_order`) each still refused. `w_shrink` now means "11 rows".

## A1.2 — C2's D5 is measured in the lane worktree, not in a clone

`plans/round-87.md` § C2 D5 freezes "`python3 -B verifiers/verify_corpus_integrity.py --json` exits 0
at `<rev>`". `ExecRepairs` implemented that as a run inside a scratch clone; `Sentinel-4` measured
that this can never pass: the lane tracks `.ufo/reports/round-76/kotoba.md` as a **symlink** into the
fleet root, which dangles in any clone, so `corpus.pointers.report_dead` stays red there regardless
of the repairs (`corpus/lessons/round-81.md:28`). That is exactly QUALITY Q63's class: *a gate whose
verdict depends on where the checkout sits is never relocated into a temp-dir sandbox.*

**Corrected mechanism:** D5 runs the revision's gate **in the lane worktree**, and the counter first
asserts that the worktree's branch tip equals `<rev>` (via
`git -C <lane> rev-parse master`) — a mismatch is exit 2, never a pass. The predicate sentence is
unchanged: the gate must exit 0 at `<rev>`.

## A1.3 — what does not change

The kill rule (`after the first candidate score`), the C2 item set D1–D4, both targets ("all rows
grounded", "5 of 5"), the no-harm battery, the touch list and the admission rule are unchanged. No
candidate data existed at this commit.
