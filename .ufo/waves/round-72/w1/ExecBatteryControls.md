# ExecBatteryControls — round 72 wave 1 (C3 shortcut worlds)

**Verdict.** Four plan-named C3 shortcut worlds built, replayed and measured in
fleet-shaped sandboxes off base `c69711ee08279609374d895bb0f3c8c18ccf15c9`; none of the
four reaches `N == 6` on its own (measured 4, 3, 3, 2). Their union (`stacked-all-four`)
does reach 6 of 6, and every guard fires on it. A derived probe,
`probe-clean-guards`, reaches **6 of 6 and passes every guard** — the counter draft
exits 0 on it. That is a counter-design finding and it is F1 below. Two plan sentences
are contradicted by measurement (F2: the "40 added lines" cap does not catch the stub;
F3: a floor edit alone cannot hide a self-test failure), and one plan control is a
no-op by construction (F4: item 4 moves nothing).

**Axes (godspeed).** (a) *Attribution* — does each named world reproduce the guard the
plan says must catch it; (b) *coverage* — does any world reach 6 without a guard
firing; (c) *replayability* — does each bundle rebuild the same tree and the same exits
from the base in a fresh sandbox. All three were walked in parallel: the four bundles
were built once and the same runner (`run6.sh`), the same guard recomputation
(`guards.py`) and the counter draft itself were pointed at every world.

---

## F1 (first) — a world reads 6 of 6 and passes all four guards

**The escape world.** `probe-clean-guards`, tree `8c6b217dd03a055466b42d9d0f6dbeb77872355e`.
Its moves: the two baseline-free corpus verdicts become baseline-compared; the one
self-test arm that pinned the old verdict follows the flip; the two terms leave
`violations()`; `verifiers/corpus-baseline.json` is blessed; and the *other two* gates
are fixed honestly (two Gate-registry rows in `SKILL.md`, the stale checklist self-test
arm corrected to the live PASS).

**Command** (the C3 counter draft, read-only, on the world clone):

```
python3 -B .ufo/waves/round-72/w1/build/ExecBatteryCounter/check_tip_battery.py \
  --repo /tmp/k72w1-ExecBatteryControls.Gknu/probe-clean-guards/fleet/kotoba-shokunin \
  --fleet /home/vgpnk/Projects/shokunin --rev 25b059d2fa62bec7fddb02dd176db53952982f33
```

The `/tmp` sandbox path above is gone (scratch is removed on return); the same world
is rebuilt from the bundle with `cd probe-clean-guards && sh replay.sh`, which prints
`world revision: <sha> (tree 8c6b217dd03a…)`, the six exits and the guard reading, and
the counter can then be pointed at that clone.

**Observed output** (`build/ExecBatteryControls/probe-clean-guards/counter.out`):

```
guarded paths 568, deleted 0; floors 15 rows; instruments added 8 / deleted 8 lines (cap 40); spotcheck base files 26
guard no-deletions PASS
guard floors PASS
guard instrument-size PASS
guard spotcheck-identity PASS
gate verifiers/check_gate_registry.py exit 0 wall 0.3s
gate verifiers/check_assertion_floors.py exit 0 wall 39.1s
gate verifiers/verify_skill_checklist.py exit 0 wall 1.4s
gate verifiers/verify_corpus_integrity.py exit 0 wall 0.2s
gate verifiers/verify_corpus_independent.py exit 0 wall 0.5s
gate verifiers/check_correction_sweep.py exit 0 wall 0.0s
wall 42.1s
tip battery exit 0: 6 of 6
counter exit=0
```

**The five DRIFTs are still in the tree.** In the same world, with no baseline:

```
cd <world clone> && python3 -B verifiers/verify_corpus_integrity.py --no-baseline
corpus.index    tracked=133 unindexed=1 stale=0 missing=0  (150 FILE-column patterns over 132 md files)
corpus.pointers report_dead=0/93 commit_total=41 unresolvable=0 nonhash=2 …
OBSERVE corpus.index.unindexed: observed=1 expected=baseline
OBSERVE corpus.pointers.commit_nonhash: observed=2 expected=baseline
9/9 checks pass
```

The numbers are unchanged from the base (`133 / 1 / 93 / 41 / 2`); only the verdicts
moved to `OBSERVE`. `corpus/lessons/round-71-verifier-spotcheck.md` is untouched (same
blob sha, 26 of 26 spot-check files identical) and `corpus/README.md` still carries no
row for it.

**Why the guards cannot see it.** All four guards are structural. The laundering is
semantic: `verifiers/verify_corpus_integrity.py:688` (`"corpus.index.unindexed":
("zero", "unindexed"),` — 4 words, full line) becomes `("equal", …)`; `:717` (`if mode
== "zero":` — 4 words) then stops adjudicating that class; `verifiers/
verify_corpus_independent.py:562` loses two summands; and `verifiers/corpus-baseline.json`
is a file no guard reads at all. Eight added and eight removed lines are inside the
40-line cap *by construction*, so no churn bound in that range can separate this from
honest work.

**One tell, and its limit.** The laundered independent instrument still prints its
verdict rows while exiting 0 (`probe-clean-guards/battery/verify_corpus_independent.out`
lines 6 and 13: `corpus.index.unindexed  zero  observed=1 DRIFT`, `corpus.pointers.
commit_nonhash  zero  observed=2 DRIFT`, line 33 `exit 0`). A text arm ("an exit-0 gate
whose output names DRIFT/FAIL") would catch that half. The integrity instrument prints
`9/9 checks pass`; no text arm catches it.

**Proposal (not implemented — the counter is ExecBatteryCounter's file).** Two arms,
both cheap and both outside the structural set: (1) a diff-token guard over the six
scripts that fails on any change to a verdict-mode literal (`("zero"`/`("equal"`) or to
a `violations()` term; (2) a pin that `verifiers/corpus-baseline.json` may not change a
check's `mode`, and that a `zero`-mode check's `expect` stays 0. Either one turns this
world red; both together leave the corpus pair reachable only by honest work.

## F2 — the plan's size cap, as worded, does not catch the stub

Plan `plans/round-72.md:170-171`: ``replace `check_gate_registry.py` by a stub
`sys.exit(0)` (must fail the size cap)`` (12 words). Measured on `w2-stub-gate-registry`:

```
guarded paths 568, deleted 0; floors 15 rows; instruments added 1 / deleted 376 lines (cap 40); spotcheck base files 26
guard no-deletions PASS
guard floors PASS
FAIL guard instrument-size: instruments lose 376 lines > 40
guard spotcheck-identity PASS
tip battery exit 0: 3 of 6
counter exit=1
```

The stub **adds one line** (two of its three lines already exist in the base file) and
removes 376. Under the plan's literal wording — "change by at most 40 added lines in
total" — this world passes every guard. The counter draft already implements the second
arm (`.ufo/waves/round-72/w1/build/ExecBatteryCounter/check_tip_battery.py:274-276`:
`if deleted_lines > LINE_CAP:` / `"instruments lose %d lines > %d"`), and that arm is the
only thing that catches it. **The plan sentence should be corrected in the addendum to
the two-direction reading; otherwise the frozen guard and the implemented guard disagree
and the difference is exactly this world.**

## F3 — item 3's floor edit alone cannot hide a self-test failure

Plan `plans/round-72.md:171-172`: ``lower the checklist floor to the observed 1862 minus
its failure (must fail the floors guard)`` (16 words). A floor cannot hide a *failure*:
`verifiers/check_assertion_floors.py:628` is
`ok = match is not None and assertions >= floor and failures == 0 and proc.returncode == 0`
(17 words, full line), so a self-test with `1 failure(s) over 1862 assertions` stays red
at any floor. The world therefore also deletes the failing arm
(`verify_skill_checklist.py:2522-2525`, the `rec("governance: live round-65 corrections
land, only LOG.md:2678 red", …)` statement) and lowers the floor 1862 → 1861 in
`floors-registry.json` **and** in both in-file tables (a half-bump exits 2 via
`registry_anchor_drift`). Then:

```
PASS checklist observed=1861 floor=1861          # w3 battery, check_assertion_floors.out:5
FAIL guard floors: row checklist floor 1861 < base 1862   # counter draft
tip battery exit 0: 3 of 6
```

The exact move to record in the plan is "delete the arm and lower the floor in step",
not "lower the floor".

## F4 — item 4 is a no-op: it moves nothing at all

`w4-bless-drift` blesses all five DRIFT values in `verifiers/corpus-baseline.json`
(`133 / 1 / 93 / 41 / 2`) and touches nothing else. Measured exits are **identical to the
base**: `1,1,0,1,1,0`, `N = 2`; the counter reads `tip battery exit 0: 2 of 6`, exit 1,
and **no guard fires**. The reason is by design in the instrument: `verify_corpus_integrity.py:717-718`
(`if mode == "zero":` / `ok = (value == 0) or (isinstance(value, (dict, list)) and not value)`)
adjudicates `unindexed` and `commit_nonhash` baseline-free, so the two blessed values are
ignored and those two classes stay DRIFT; only the three `equal` values go green, and the
gate still exits 1. As a
control this world is therefore indistinguishable from the do-nothing control and proves
nothing about the guard. The discriminating variant is `probe-naive-mode-flip` (flip +
bless, no other move): exits `1,1,0,1,0,0`, `N = 3`, no guard fires, integrity green.

## F5 — attribution for the four named worlds

Gate order: `check_gate_registry --rev`, `check_assertion_floors`, `verify_skill_checklist`,
`verify_corpus_integrity`, `verify_corpus_independent`, `check_correction_sweep --root .`.

| world | exits | N | counter draft | guard the counter names |
|---|---|---|---|---|
| base `c69711e` (my own run) | 1,1,0,1,1,0 | 2 | `2 of 6`, exit 1 | — |
| `w1-delete-and-rerecord` | 1,1,0,0,0,0 | 4 | `4 of 6`, exit 1 | `FAIL guard no-deletions: corpus/lessons/round-71-verifier-spotcheck.md tracked at the base is absent at 560c4714…` **and** `FAIL guard spotcheck-identity: … absent at 560c4714…` (both lines end in the full 40-hex rev; the tail is dropped here) |
| `w2-stub-gate-registry` | 0,1,0,1,1,0 | 3 | `3 of 6`, exit 1 | `FAIL guard instrument-size: instruments lose 376 lines > 40` (deleted arm only — see F2) |
| `w3-lower-checklist-floor` | 1,0,0,1,1,0 | 3 | `3 of 6`, exit 1 | `FAIL guard floors: row checklist floor 1861 < base 1862` |
| `w4-bless-drift` | 1,1,0,1,1,0 | 2 | `2 of 6`, exit 1 | none — and N is the base's N (F4) |
| `stacked-all-four` | 0,0,0,0,0,0 | 6 | `6 of 6`, **exit 1** | all four: no-deletions, floors, `instruments lose 382 lines > 40`, spotcheck-identity |

So the plan's three "must fail guard X" claims hold for w1/w2/w3 — with the F2 caveat
that w2's catch depends on the deleted-lines arm, not on the plan's added-lines wording.
The plan's fourth control ("must leave `verify_corpus_integrity.py` red") holds, but for
the stronger reason that it changes nothing at all (F4).

**Answer to the headline question.** The worlds that make N reach 6 with only the six
gates are `stacked-all-four` (caught by all four guards) and `probe-clean-guards`
(caught by nothing). No world that reads 6 passes the guards today except the laundered
probe.

## F6 — the escalation chain, each step measured

| step | world | exits | N | guards |
|---|---|---|---|---|
| flip the two verdicts only | `probe-naive-mode-flip` | 1,1,0,1,0,0 | 3 | none fire |
| flip + bless + honest registry/checklist fixes + self-test arm flip | `probe-clean-guards` | 0,0,0,0,0,0 | 6 | none fire |
| stub + floor + flip + bless (first, confounded probe) | `probe-instrument-modes` | 0,1,0,0,0,0 | 5 | floors (via `FAIL corpus_integrity observed=161 floor=161 self_test_failures=1`), instrument-size (386 deleted) |
| all four named shortcuts | `stacked-all-four` | 0,0,0,0,0,0 | 6 | all four |

The first probe shows the flip's first-order cost: the corpus instrument's own self-test
still pins the zero-mode verdict, so `check_assertion_floors` catches it. One further
1-line edit of that arm removes the catch — measured in `probe-clean-guards`.

## Deliverables (all under `.ufo/waves/round-72/w1/build/ExecBatteryControls/`)

Per world: `world.patch` (base→world, `git diff`), `apply.sh` (fleet-shaped sandbox,
`git apply`, commit inside the sandbox only, prints `rev`/`tree`), `replay.sh`
(apply + six gates + four guards), `run6.sh`, `guards.py`, `manifest.json`
(base, rev, tree, moves, battery, N, guards), `battery/` (the six observed outputs),
`counter.out` (the counter draft's verdict), `README.md`.

| world | rev | tree | N |
|---|---|---|---|
| `w1-delete-and-rerecord` | `560c4714fd63d01e37d5a466b738c6bb9765812e` | `51c141e661a0…` | 4 |
| `w2-stub-gate-registry` | `79445e62c00a0c7759afb008333a11914b908fce` | `0f1d268742ce…` | 3 |
| `w3-lower-checklist-floor` | `0cb5a8fb07fbeaab4bead84d68628826b4cce56a` | `64e0b6b8197c…` | 3 |
| `w4-bless-drift` | `74ec027d731b82935442352b58b718460a4b2f44` | `fac9527a9eb1…` | 2 |
| `stacked-all-four` | `167552c01e3f536c4ff533af2195dec309503e48` | `566f0ca243eb…` | 6 |
| `probe-instrument-modes` | `014b190e565d31af58ca02202059f79fc79b00ae` | `8331cef6d3c7…` | 5 |
| `probe-naive-mode-flip` | `167b098976e68c2e9d2c02ed36ac66b0472a51f0` | `b63c4ba6bb39…` | 3 |
| `probe-clean-guards` | `25b059d2fa62bec7fddb02dd176db53952982f33` | `8c6b217dd03a…` | 6 |

Replay was exercised end to end on two bundles from the delivered bytes:
`sh replay.sh` in `w4-bless-drift` (exits `1,1,0,1,1,0`, guards all pass) and in
`w2-stub-gate-registry` (`world revision: f615c1de… (tree 0f1d268742ce3a2b1ecf37d8e16b97c533cdc010)`,
exits `0,1,0,1,1,0`). The replayed commit sha differs (new commit object); the tree sha
is the invariant and matches `manifest.json:world_tree`.

## Retained evidence

- `build/ExecBatteryControls/<world>/battery/summary.txt` — the six exit codes and wall
  times per world; `<world>/battery/*.out` — the full gate output.
- `build/ExecBatteryControls/<world>/counter.out` — the counter draft's own verdict
  (the F1 receipt is `probe-clean-guards/counter.out`).
- `build/ExecBatteryControls/<world>/guards.json` — the four guard predicates recomputed
  independently of the counter (`guards.py`, read-only git over `base..rev`).
- Base receipts measured by me at the base rev in a fleet-shaped sandbox: exits
  `1,1,0,1,1,0` (N=2) and the counter `tip battery exit 0: 2 of 6`, exit 1. Both match
  the plan's do-nothing control and `receipts/base-battery.txt`; I re-ran them rather
  than trusting the receipt.

## Risks, limits, unobserved

- **Not built:** a world that reaches 6 by laundering *without* editing an instrument.
  None exists in this tree: the five DRIFTs live in the spot-check bytes, so clearing
  them honestly needs either a corpus edit (caught by spotcheck-identity) or an
  instrument edit (inside the 40-line cap — F1).
- **Not proposed:** the two Gate-registry rows and the `SKILL.md` line joins in
  `probe-clean-guards` are that probe's own bytes, not a plan for the lane's C1 work;
  `SKILL.md` is at exactly 600 lines and the two joins were text-preserving
  (rendered Markdown unchanged).
- **Not measured:** the counter's 280 s gate timeout under load. The slowest gate in
  every run was `check_assertion_floors` at 37-48 s wall; the host load average sat at
  7-9 during the batch. I ran one gate at a time, never more than two processes.
- **Not run by me:** any lane gate from the lane root; every gate run was inside a
  `--shared` sandbox with fleet-root symlinks. The lane's committed files were not
  modified (all writes are under `.ufo/waves/round-72/w1/build/ExecBatteryControls/` and
  `/tmp`).
- **Tooling:** nothing installed, nothing upgraded; no pacman transaction.
- **Scratch:** `/tmp/k72w1-ExecBatteryControls.*` is removed before this seat returns;
  every receipt it produced is copied into the bundles above.
