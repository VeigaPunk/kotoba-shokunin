# kotoba round 89 — addendum 1 (pre-score amendments to the frozen draft)

Written by the L1 (KotobaR89) before the freeze commit and before ANY candidate score. Every item below
is a change made after the wave r89-w1 settled and before the freeze receipt was written. No predicate
sentence, target or kill-rule sentence in `plans/round-89.md` changes; the amendments add arms, pins and
bounds, and each bound is stated as a narrowing of the headline, never a widening of a target.

Frozen-state check (run by the L1 at the freeze commit): `git diff 43fc784 -- plans/round-89.md` shows only
this addendum's pointer line and the freeze header; the frozen predicate lines are byte-identical.

## A1 — D5 gate `check_r86_routed_repairs_v3.py` (C2)

Source of each item: the critic's attack list (`.ufo/waves/round-89/w1/CriticFalsify/attacks.md`, N1–N5)
and the reviewer's findings (`.ufo/waves/round-89/w1/ReviewerD5Gate/review.md`, F1–F3), plus the control
seat's Q79 receipt (`.ufo/waves/round-89/receipts/ctl-equivalence.txt`).

| item | finding | change | self-test arm |
|---|---|---|---|
| A1.1 | N1 / F2 / F3 (Q79 location flip: `report_dead` 0 in the lane, 1 in a bare clone) | the receipt records `location_class` (`lane` | `clone`) from the tracked symlink `.ufo/reports/round-76/kotoba.md`; a receipt and a measured root of different classes return exit **2** (`SKIP location_flipped`), never a leg verdict | pure + pinned by the freeze-revision equivalence receipt |
| A1.2 | N2 (probe E: a same-count instance swap passes D5(iii)) | each receipt pins `details` = per check name, the sorted `*_detail` entries of the integrity observation; D5(iii) fails when a measured detail entry is absent from the receipt (`instance growth ... detail ...`); shrinking details pass | `arm d5iii detail: a same-count instance swap adds a detail entry` (and two must-pass arms) |
| A1.3 | N4 (the r87 launder guard, `check_r86_routed_repairs.py:425-432`, dropped by v2/v3) | the receipt pins blob ids of `corpus/lessons/round-86-verifier-spotcheck.md` and `corpus/lessons/round-81.md`; a changed or deleted record fails `snapshot_tampered` (`record blob changed`); an absent record pins as `null` | `arm record pin: an absent record pins as None, never raises` |
| A1.4 | N5 / C2-g (a receipt written from a dirty tree pins a state no commit names) | `--write-base-receipt` refuses a dirty tree (exit 2, `dirty tree`) | exercised by the freeze-commit receipt write (clean tree required) |
| A1.5 | F1 (receipt-value laundering: edited receipt values pass exit 0) | the receipt carries `receipt_sha256` (sha256 of the body with that field removed, sorted keys); `--receipt-sha256 HEX` pins the bytes being scored and a mismatch fails `snapshot_tampered` before any leg runs | exercised by the frozen ReviewerD5Gate F1 repro (`receipt-inflated2.json`), recorded in the landing receipts |
| A1.6 | ExecCtlWorlds hazard (a GIT_DIR-class env override in the caller shell read `commit_unresolvable` 10 for the clean 1) | every git call and the integrity `--json` / `--self-test` subprocesses run with the GIT_DIR-class variables removed (`_clean_env`) | none needed: the hazard is an environment property, pinned by the equivalence receipt |

Bound stated before the first candidate score: D5 reads the integrity gate's OUTPUT (names, values, detail
entries) and the pinned record blobs. It does not judge what a new citation means, and it reads detail
entries as text. The headline "instance-level" in plans/round-89.md § C2 is read, from this addendum on,
as: **per-check value non-growth AND per-check detail-entry non-growth (instance identity)**, for the
corpus `*.md` citation population the integrity instrument reads (N3: a dead citation in `LOG.md` is not in
that population and is named as an unmeasured residual, not counted).

## A2 — freeze gate `check_freeze_gate.py` (C1)

| item | finding | change | self-test arm |
|---|---|---|---|
| A2.1 | N7 (an exit-only control declaration, `expect: exit 0`, holds without pinning any observable verdict; the r88 failure class is exactly an unpinned verdict) | a `stdout contains <literal>` clause is REQUIRED on every control (SpecError, exit 3, `no stdout literal`) | `arm exit-only-expect refused (A2)` (replaces the earlier `exit-only-expect holds` arm, which asserted the defect) |
| A2.2 | N7 consequence: the arms that declared `expect: exit N` alone | each such arm now declares a stdout literal and keeps its assertion (`exit mismatch: declared 7, observed 0`, timeout, missing-command, prose-line) | the five arms re-run; self-test 30 of 30 |
| A2.3 | N6 (headline "refuses an unsatisfiable freeze" is broader than the measured oracle: the simulators grep the recorded round-88 receipt text) | the C1 headline is bounded in the LOG/SCORECARD wording to: **refuses a declared expectation that contradicts the control's recorded verdict** (the oracle is the simulator's receipt-grounded verdict, fail-closed when the receipt is absent); the instrument does not evaluate predicate satisfiability | none (wording bound; the arm set is unchanged) |
| A2.4 | ReviewerFreezeGate F-r89-C1-2/-3, F-risk-2 (duplicate control names documented as exit 3 but processed as re-runs) | the docstring is corrected at the freeze commit to state the observed behaviour (first observed refusal wins), and a duplicate name is recorded as a finding for round 90, not repaired here (no arm pins it yet) | none; disclosed |

Mutation battery (MutTesterGates, `.ufo/waves/round-89/w1/MutTesterGates/mutants.tsv`): the battery ran on the
pre-A2 gate bytes. A2 adds the arm that kills the parse-drop-stdout mutant class; the battery is NOT re-run
for this addendum and the C1 mutation leg is recorded as **carried** (one mutant class, `fg-m4`, is now killed
by the new arm by construction, not by measurement).

## N8 — freeze-diff path (kill-rule coverage)

The freeze-protocol diff command in plans/round-89.md § Round shape is extended, before the first candidate
score, to: `git diff <freeze> <landing> -- verifiers verifiers/fixtures plans corpus SKILL.md scripts
.ufo/waves/round-88/w1 .ufo/waves/round-88/receipts .ufo/waves/round-89/w1 .ufo/waves/round-89/receipts LOG.md
SCORECARD.md`, with the landing commit's allowed set named: the measurement receipts under
`.ufo/waves/round-89/receipts/landing-*` and the LOG/SCORECARD appends. Also required, at both revisions:
`git status --porcelain` empty and `git ls-files -o -i --exclude-standard` empty (K-d). The `-`-line check on
the plan diff (K-e): `git diff <draft> <freeze> -- plans/round-89.md | grep '^-' | grep -v '^---'` must print
nothing (the freeze header is additions only).

## N9 — sourced claims

S258 is opened at the canonical PMC route `PMC5856500` (the assignment's `PMC5813543` route is a different
article, recorded as an honest reject in ScoutSource's receipts). The `teaches` cell of S258 names the lane's
inference explicitly: the paper does not discuss executable controls; the inference that a control whose
expectation cannot be observed is not a confirmation is the lane's (labelled in the row and in the knowledge
entry). S259 word counts: the scout's counts are corrected in the lesson (line 73 = 18 words, line 74 =
8 words, both ≤ 25).

## N10 — Q80

The round is provisional until the mutation output is settled; this addendum records that MutTesterGates
output is present (`mutants.tsv`, `equivalents.tsv`, `summary.json`) and the round is not closed provisional
on that account.

## Not taken this round (recorded so the frozen set is complete)

- ExecFreezeGate duplicate-name arm (A2.4): deferred, disclosed.
- Scope extension of the D5 integrity population to `LOG.md` (N3 second option): not taken; the bound above is
  the disclosed residual.
- `pointers.commit_unresolvable` stays red at 1 (`corpus/lessons/round-81.md:8`): not repaired by this round.

## A1.7 — the w_healed control is re-derived (pre-score; the frozen clause "a healed red passes" is kept)

The wave-era control `w_healed` (ExecCtlWorlds) repaired `corpus/lessons/round-81.md:8`. Under A1.3 that
file is a pinned record: a repair changes its blob and the snapshot leg refuses it (`record blob changed`),
which is the Q64 rule working as designed (a historical lesson is never rewritten to green a gate). So the
declared control, as written, cannot pass by honest work at any revision. Recorded here, not hidden: this is
the same class as round 88's F1 (a control the predicate cannot satisfy), found by the same freeze discipline.

The re-derived `w_healed` is a real heal that rewrites no record: the BASE receipt is written at the round
base `a5b3b15c00b1de5db321e4226a0a7db17340e605` (where `corpus.index.unindexed` reads DRIFT 2:
`corpus/lessons/round-87-verifier-spotcheck.md`, `corpus/lessons/round-88-verifier-spotcheck.md` unindexed)
and the world is the freeze revision (where the README rows index both files, `unindexed` reads 0). Expected:
exit 0, `closed 5 of 5`, `instance drift 0`, with `corpus.index.unindexed` DRIFT → PASS in the d5ii leg.
Every world, including this one, is lane-shaped (Q79 location class), so the comparison is not a flipped
pairing. The four other controls (`w_added_instance`, `w_silenced`, `w_rerecorded`, `w_tip`) are re-run at
the freeze revision with the final gate and their final receipts are committed beside the wave-era ones,
which are not rewritten.
