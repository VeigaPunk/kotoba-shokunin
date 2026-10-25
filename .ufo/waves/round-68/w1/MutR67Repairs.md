# MutR67Repairs — round 68 wave 1, mutation-tester (C2 routed-repairs counter)

Axes attacked: `consistency` (C2's calibration sub-axis) — the detector itself: does
`check_r67_routed_repairs.py` *reject* a world in which each routed defect (R67-1..4) is
reintroduced, and does its `--self-test` kill the same classes? One defect in the detector
counts as much as one defect in the corpus.

## Target identity (moving target, pinned)

- The mandated draft `.ufo/waves/round-68/w1/drafts/check_r67_routed_repairs.py` **did not
  exist** at session start (checked 23:0x: `ls: cannot access ... No such file or directory`);
  the live iteration was `verifiers/check_r67_routed_repairs.py` (tracked, uncommitted `M`).
  While the battery ran, the L1 edited it under me — a transient mid-edit state
  (sha `194017b2…`, 276→ lines, calls `selftest` without defining it) crashed `--self-test`
  with `NameError: name 'selftest' is not defined`; the next coherent state is pinned as
  **production snapshot `a3b91848618b9efa3478176e2b891298248d61b1ca2cdfdaea20236cc24d7660`**
  (276 lines). HEAD `cafa29d0`'s committed copy (204 lines) has **no** `--self-test` at all.
- The assigned draft **appeared mid-battery** (23:20) and was then pinned and given the same
  battery: **draft `cc380d930f7595c57a472d5abfdce626d3453edbbb0c87d5673f3517766bf0ba`**
  (662 lines).
- All runs against a `--no-hardlinks` scratch clone `/tmp/mut68/lane` (git-only, no `.jj`).
  **The lane repo was never pointed at any counter run** — the production snapshot's
  `_baseline_values` executes `git -C <repo> checkout <rev> -- corpus verifiers` (see F3).

## Worlds (scratch clone commits off pristine `3cd73836d81420961105b6a4c46a1f3a771ac8b3`)

| mutant | world mutation | commit |
|---|---|---|
| X1 / D1 | lines naming the observed `environment error: cannot read corpus/knowledge/instruction-authority-ladder-round67.md` deleted from LOG.md, SCORECARD.md, corpus/lessons/round-68.md | `35deef2e716e…` |
| X2 / D2 | real receipt path `.ufo/waves/round-67/controls/census-validate-append.txt` re-replaced by the wrong `w1/controls/` form in all three records | `dda210a97f8e…` |
| X3 / D3 | every record line naming `.ufo/waves/round-67/w1/controls/junk-world` deleted | `eaafeb26519f…` |
| X3b / D3' | disclosure kept, junk-world dir recreated in the repo working tree (the counter's second conjunct) | (worktree only, at ORIG) |
| X4a / D4 | coverage-map table row for `round-67-verifier-spotcheck` dropped from corpus/README.md | `19ef6f031a90…` |
| X4b / D4' | stale baseline: `tracked_files` expect 124→121, `report_total` 85→82 (the base's stale numbers) | `3cf742b5f5f1…` |

## Results — production snapshot `a3b91848` (runs P/S; scratch only)

Baseline: `--self-test` exit 0, `0 failure(s) over 6 assertions`; honest world
`--rev 3cd73836…` → `r67 routed defects closed 4 of 4`, exit 0; base `--rev e94ae32a…` →
**exit 2**, stderr `environment error: cannot read corpus/lessons/round-68.md at
e94ae32a5cd8dc3ee8e2d247816784bec2750cc0` — **not** the `0 of 4` line its own docstring
promises (defect F1 below; the R67-1 environment/content misclassification recurs on the
base conjunct; exit is nonzero, so the C2 before-shape still holds).

| mutant | expected | observed | verdict | printed |
|---|---|---|---|---|
| X1 | reject, D1 finding | exit 1, `closed 2 of 4` | **KILLED — PASS** | `D1: no record carries the appended correction naming the observed …line` |
| X2 | reject, D2 finding | exit 1, `closed 2 of 4` | **KILLED — PASS** | `D2: no record names the real receipt path .ufo/waves/round-67/controls/census-validate-append.txt` |
| X3 | reject, D3 finding | exit 1, `closed 2 of 4` | **KILLED — PASS** | `D3: the disclosure of .ufo/waves/round-67/w1/controls/junk-world is missing, or the path still exists` |
| X3b | reject, D3 finding | exit 1, `closed 2 of 4` | **KILLED — PASS** | same D3 line (second conjunct fires) |
| X4a | reject, D4 finding | exit 1, `closed 3 of 4` | **KILLED — PASS** | `D4: corpus/lessons/round-67-verifier-spotcheck.md has no coverage-map index row` |
| X4b | reject, D4 finding | exit 1, `closed 3 of 4` | **KILLED — PASS** | `D4: baseline corpus.index.tracked_files expects 121, the gate's own measurement yields 124` + `…report_total expects 82 … yields 85` |

### Its `--self-test` vs the same mutants

The self-test's five broken worlds (D1 absent, D2 absent, D3 absent, D4 index absent, D4
stale baseline) all report `PASS broken world rejected`, 0 failures — but **it does not kill
all of the same classes**. Counter-neuter probes (real mutations of the counter):

- `if OBSERVED in joined:` → `if True:` → self-test exit 1, `FAIL broken world survived: D1
  correction absent` — **caught**.
- `if expect.get(key) != value:` → `if False:` → exit 1, `FAIL … D4 stale baseline` —
  **caught**. (`indexed = True` → `False` → exit 1 via honest-world red — **caught**.)
- `if REAL_RECEIPT in joined:` → `if True:` → **self-test exit 0, 0 failures — NOT caught.**
  Cause: the "D2 receipt path absent" world is built by *dropping whole records* containing
  the path, which co-breaks D3 (the junk disclosure rides the dropped records); a counter
  blind only to D2 still fails that world on D3. The D1/D3 worlds are confounded the same way;
  only the two D4 worlds isolate their defect.
- `if JUNK in joined and not (repo / JUNK).exists():` → `if JUNK in joined:` → self-test
  exit 0 (**not caught**) **and** it false-PASSes the real X3b world: `r67 routed defects
  closed 4 of 4`, exit 0 while junk-world exists. The still-exists leg is structurally
  untestable in that harness: `check()` is called with `Path("/nonexistent")` and the
  `junk_exists` parameter is dead (every broken world passes `False`; the dir is created
  under the fixture `root`, never under `repo`).

## Results — assigned draft `cc380d93` (runs T/U; scratch only)

| run | expected | observed | verdict |
|---|---|---|---|
| self-test | 0 failures | exit 0, `self-test: 0 failure(s) over 23 assertions` (includes `could-not-evaluate` zero-hash and missing-`--rev` negative probes) | PASS |
| honest `3cd73836` | 4 of 4, exit 0 | `control at e94ae32a: 0 of 4` + 4× `PASS` + `r67 routed defects closed 4 of 4`, exit 0 | PASS |
| base `e94ae32a` | 0 of 4, nonzero | `0 of 4`, exit 1, all four `FAIL` | PASS — **F1 fixed**: the promised base line prints; no environment misclassification |
| X1 | reject, D1 only | exit 1, `closed 3 of 4`, `D1…FAIL`, D2–D4 `PASS` | KILLED — PASS |
| X2 | reject, D2 only | exit 1, `closed 3 of 4`, `D2…FAIL`, others `PASS` | KILLED — PASS |
| X3 | reject, D3 only | exit 1, `closed 3 of 4`, `D3…FAIL` | KILLED — PASS |
| X3b | reject, D3 only | exit 1, `closed 3 of 4`, `D3…FAIL` | KILLED — PASS |
| X4a | reject, D4 only | exit 1, `closed 3 of 4`, `D4…FAIL` | KILLED — PASS |
| X4b | reject, D4 only | exit 1, `closed 3 of 4`, `D4…FAIL` | KILLED — PASS |

Draft self-test kill power — true always-`closed` neuters of `check_d1..check_d4`: **all four
caught** (`self-test: 7–8 failure(s) over 23 assertions`, exit 1). Bonus property observed:
a neutered counter also *refuses to score real worlds* — its inline pinned-base control trips
(`could-not-evaluate: pinned base e94ae32a scores 1 of 4, expected 0 of 4`, exit 2), so a
blinded detector disarms instead of false-PASSing. Per-defect isolation in the real-world
runs is clean (no confounding). The draft also replaced `git checkout` with
`git archive <rev>` extraction for the gate measurement — read-only, F3 fixed.

## Defects routed to the L1

- **F1 (production snapshot `a3b91848`, uncommitted):** base conjunct prints
  `environment error: cannot read corpus/lessons/round-68.md at e94ae32a…` and exits 2; its
  docstring promises `r67 routed defects closed 0 of 4`. This is R67-1's class
  (environment vs content verdict) on the counter built to close R67-1. The draft fixes it.
- **F2 (production snapshot):** `--self-test` cannot kill a D2-only regression (confounded
  record-filter worlds) nor the X3b still-exists class (dead `junk_exists` param; repo pinned
  to `/nonexistent`). The draft's fixture-based self-test kills all four neuter classes.
- **F3 (production snapshot, hazard):** `_baseline_values` runs
  `git -C <repo> checkout <rev> -- corpus verifiers` against the `--repo` it is given. Run
  as the frozen predicate commands (`python3 -B verifiers/check_r67_routed_repairs.py --rev
  <rev>` in the lane), it would overwrite lane working-tree bytes from `<rev>` — today that
  would have destroyed the L1's own uncommitted counter edits — and it updates the lane's Git
  index, which wave rules forbid seats to touch. It also contradicts the docstring "reads the
  COMMITTED bytes at `--rev` (never the working tree)": the gate measurement reads the
  post-checkout working tree. Draft replaced this with `git archive` into a temp dir.

Non-defect, noted: in the production snapshot D4's credit is `if not findings: closed += 1`,
so with any other defect open the count under-reports D4 with no D4 line (e.g. X1: `2 of 4`
with only a D1 finding). Cannot produce a false PASS (4 requires empty findings); cosmetic.

## Restoration evidence

- Lane bytes: `sha256sum -c` over the session-start snapshot — **7/7 stable files byte-identical**
  (`verifiers/corpus-baseline.json`, `verify_corpus_integrity.py`, `corpus/README.md`,
  `LOG.md`, `SCORECARD.md`, `corpus/lessons/round-68.md`, `corpus/lessons/
  round-67-verifier-spotcheck.md`). The eighth file, the counter itself, reads FAILED only
  because the L1 changed it mid-session (`194017b2…` → `a3b91848…`, both recorded above) —
  not by this seat; this seat wrote nothing in the lane except this report.
- Lane git: no `add/commit/stash/checkout/reset/push` and no `jj` command was ever run
  against the lane; status diff before/after shows only sibling-seat churn on paths this
  seat never touched.
- Scratch: `/tmp/mut68/lane` back on pristine `3cd73836…`, `status --porcelain` empty;
  mutant commits citable by sha; all raw outputs under `/tmp/mut68/results/` (`P0-P2`, `X1-X4b`,
  `T0-T8`, `U-*`), variants under `/tmp/mut68/variants/` (`pristine/pinned/draft` + neuters).

Verdict: production snapshot kills all six assigned world-mutants (C2 counter stands), but
carries F1–F3 and a self-test that misses two of the same mutant classes. The assigned draft
kills all six **and** its self-test kills all four counter-neuter classes — take the draft.
