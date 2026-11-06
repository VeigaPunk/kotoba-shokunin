# ReviewerBatteryKills — round 95, w1 — review of ExecBatteryKills C1 patch

Seat: ReviewerBatteryKills (reviewer, leaf, no subagent dispatch). Lane: kotoba-shokunin.
Item: waited for `ExecBatteryKills_READY`; reviewed `ExecBatteryKills/ExecBatteryKills.patch`
(sha256 `f9506fe3033d2d5e2ee26dbb42748e892ceb46e99695922b4ca78a822bc41d96`, matches READY) against
plans/round-95.md § C1 and the context's ANTI-SNIFFING / FROZEN ANCHORS rules; hand-applied each
frozen mutant in my candidate clone and named the failing assertion with its `FAIL ` line; ran the
frozen counter c1 + r94c1 and the round-93 killpin control on the candidate.

**Verdict: no blocking findings. The patch is review-clean; C1 is honestly met on my independently
built candidate `81171b00e8b49a84e3ce26b2c61920808dc036b8`.** Non-blocking observations below.

## Candidate build (my clone, not the builder's)

- Scratch clone `D=/fast/scratch/hyaku/kotoba-r95/ReviewerBatteryKills/repo` from the lane,
  checked out at the freeze commit `673d1e2e6f850bb54dda9698cf825cf6788c7d0d`;
  `git rev-parse --show-toplevel` == D before any commit.
- `git apply --check` OK, then applied; `git status` shows ONLY
  `verifiers/check_mutation_battery.py`, `67 insertions(+), 0 deletions(-)`.
- Committed with the scratch identity (`scratch <scratch@invalid>`) → candidate
  **81171b00e8b49a84e3ce26b2c61920808dc036b8** (same patch bytes on the same base as the
  builder's `3d13eb939e18fa7cc8b4e4622eddb589f0027fe1`; their commit lives only in their clone).

## Review checklist

1. **Production code byte-identical outside `self_test()`.** Single hunk, entirely inside
   `self_test()` (after the `revmiss` arm, before the k1 `revwt` arm). Byte compare of the
   candidate file vs the freeze-commit file: bytes before `def self_test() -> int:` identical,
   bytes from `\ndef head(repo: Path) -> str:` identical. SKILL.md untouched.
2. **FROZEN ANCHORS intact.** On the candidate bytes, exact-count check (same counts as base):
   `committed = git_show(lane, rev, MANIFEST).decode("utf-8")` 1/1;
   `raise CouldNotEvaluate("manifest must name exactly the targets %s"` 1/1;
   `return n == want, "observed` 1/1; `ok_pin, pin_detail = kill_set_check(committed, pinned)`
   1/1; `print("could-not-evaluate: %s" % exc)` 3/3. The patch adds NO occurrence of any anchor
   (the N5 arm asserts the substring `"manifest must name exactly the targets" in out`, which does
   not contain the `raise CouldNotEvaluate(` anchor; the n11 live arms call
   `kill_set_check(extra_text, module_pin)`, not the anchored call shape).
   The mutated statements keep their line counts (all single-line substitutions).
3. **Mutation-battery coupling (manifest anchors).** On the candidate bytes the manifest-row
   anchors mb-m2 (G1 commit check), mb-m15 (clean-tree guard), mb-m16 (restore read-back) still
   match exactly once each (regex count = 1).
4. **ANTI-SNIFFING — every new arm observes behaviour.** All 8 new checks read only:
   `rc, out` from `run_evaluate(...)` (public `main`/`evaluate` on a fixture world),
   `ok/detail` from `kill_set_check(text, pin)` (the pin function's return), or precondition
   manifest bytes (`_git_fixture(wt-style)` status checks are pre-existing; the new arms use
   `build_fixture` + file writes + `head`). No `__file__`, tokenize, ast, linecache or inspect
   reads of the instrument in the added hunk (the only `__file__` in `self_test()` is the
   pre-existing live-manifest arm).
5. **Module pin restored on every path.** The patch rebinds no module global; new helpers
   `_commit`/`_extra_kill_rows` are pure. The existing `finally: KILL_SET_PINNED = module_pin`
   and the per-arm try/finally rebinds (`git`, `place`, `write_target`) are untouched; an
   exception raised by a new arm propagates after the finally restores the pin. No new leak path.
6. **Fixture git confined to fixture dirs; no identity leak.** `_commit` uses `_git_fixture(repo,
   "add", "-A")` and commits with the fixture identity
   `battery-selftest <battery-selftest@example.invalid>` (same identity `build_fixture` uses);
   the instrument's `git()` helper always `-C str(repo)` and runs under `clean_env()` (GIT_*
   scrubbed). No lane identity, no seat name, no writes outside the self-test's mkdtemp root.
7. **Tally growth:** `t.check` sites 38 → 45 (one new site runs twice in `for extra in (2, 3)`)
   → honest runtime tally 46 assertions; every new assertion names the arm it guards.

## Kills — hand-applied mutants, named failing arms (candidate working tree, `--self-test`)

For each mutant I wrote the substitution into the candidate's working tree (anchor count asserted
= 1), ran `python3 -B verifiers/check_mutation_battery.py --self-test` in the candidate clone,
then restored the candidate bytes (sha256 re-verified `f102b419…660a109e`, `git status` clean).

- **n1-manifest-at-head** (`git_show(lane, rev, …)` → `git_show(lane, "HEAD", …)`): rc 1,
  `2 failure(s) over 46 assertions`. Failing arm:
  `FAIL n1 manifest-at-rev: run at the first commit reads that commit's satisfying manifest, exit 0 without kill-set-size`
  — detail under the mutant:
  `could-not-evaluate: arm kill-set-size: manifest at 511db010e6ae has observed 8 kill rows, pinned 9`
  (the mutant read the HEAD manifest — one kill row dropped — instead of `--rev`'s satisfying one).
  The reverse-direction arm also fails:
  `FAIL n1 manifest-at-rev (reverse): run at the first commit (kill row dropped) exits 2 naming kill-set-size though HEAD satisfies`
  (mutant reads the satisfying HEAD bytes and runs to verdict exit 0 instead of refusing).
  Both directions pin the kill to the stated defect (N1). REPORTED-FAILURE, not a run error.
- **n5-label-targets-cne** (target-set refusal labelled `arm kill-set-size:`): rc 1,
  `1 failure(s) over 46 assertions`. Failing arm:
  `FAIL n5 label-targets-cne: a committed manifest missing a probe target exits 2 naming the target set without the kill-set-size label`
  — detail under the mutant:
  `could-not-evaluate: arm kill-set-size: manifest must name exactly the targets ['verifiers/check_freeze_gate.py', 'verifiers/check_mutation_battery.py', 'verifiers/check_r86_routed_repairs_v3.py']`.
  The arm passes `pinned_count - 1`, so the pin check would pass — the only exit-2 path is the
  target-set refusal, isolating the label (N5). REPORTED-FAILURE.
- **n11-accept-plus-two** (`n == want` → `(n == want or n == want + 2)`): rc 1,
  `2 failure(s) over 46 assertions`. Failing arms:
  `FAIL arm kill-set-size (n11): the live manifest with 2 kill rows appended is refused by the pin naming the observed count`
  (detail `observed 19 kill rows, pinned 17` — the mutant accepted the +2 manifest) and
  `FAIL n11 accept-plus-two (rev path): a committed manifest with two kill rows above the pin exits 2 naming kill-set-size and the observed count`
  (the rev-path world runs to the battery verdict instead of refusing — mutant accepted 12 == 10+2).
  Kills N11 for the stated reason.
- **n10-accept-plus-one (positive)**: still killed, by the PRE-EXISTING k3 arms
  (`FAIL arm kill-set-size (k3): the live manifest with one kill row appended is refused by the pin`,
  `FAIL k3 added rows (rev path): …`), `2 failure(s) over 46 assertions` — the new arms do not
  weaken the positive control.

## Frozen counter on the candidate (my independent runs)

`HYAKU_SCRATCH=<my scratch> python3 -B verifiers/fixtures/round-95/selftest-kills.py … 81171b00… $D`:

- **c1 → rc 0**, `C1 targets killed 3 of 3 (run errors 0); positive killed 1 of 1; honest CLEAN;
  comment decoys held 3 of 3; code decoys held 3 of 3` → `C1-PREDICATE-MET`. Honest
  `0 failure(s) over 46 assertions`. Per-mutant: n1 KILLED 2 failures, n5 KILLED 1, n11 KILLED 2,
  positive n10 KILLED 2. All six decoy runs HELD.
- **r94c1 → rc 0**, `R94C1 targets killed 3 of 3 (run errors 0); positive killed 1 of 1; honest
  CLEAN; comment decoys held 3 of 3; code decoys held 3 of 3` → `R94C1-PREDICATE-MET` (k1 3, k2 4,
  k3 5, k0 9 failures; honest 46 assertions) — the v3 rules still hold the round-94 arms; the new
  arms do not blanket-refuse anything.
- **round-93 `c1-killpin-rev.sh 81171b00… $D` → rc 0, `C1-PREDICATE-MET`**: drop world rc 2 names
  kill-set-size; other world rc 2 without the label; honest world rc 0 with the frozen predicate
  line `mutation battery killed 17 of 17 kill-set; equivalents survived 6 of 6; disclosed
  survivors 0 of 0` — the battery's own `--rev` run is green on the candidate.

Baseline at the freeze commit (my clone) reproduced the pre-data receipts exactly:
c1 rc 1 `C1-PREDICATE-UNMET` (0 of 3), r94c1 rc 0 `R94C1-PREDICATE-MET`.

The builder's own receipts (`ExecBatteryKills/counter-c1.txt`, `counter-r94c1.txt`,
`c1-killpin-rev.txt`, `selftest-honest.txt`) agree with my independent runs line-for-line
(only rev/clone names differ).

## Findings

**Blocking: none.**

Non-blocking observations:

1. **`controls-run.txt` scope.** The builder's round-92 `controls-run.sh` receipt is a LANE
   reading: `ctl-*.sh` resolve the repo as the lane (`LANE=$(dirname …)/../../..`) and take no
   REPO argument, so they cannot point at a scratch candidate; the builder's receipt measures the
   lane at its then-HEAD, not the candidate. Not a patch defect and not a counter defect (by
   design those are L1 landing-time readings). Candidate-scoped evidence for the same coupling
   concern is the round-93 killpin honest world above (battery `--rev` green at the candidate
   bytes). L1 should still run `controls-run.sh` at the landing revision.
2. **Depth note (not a defect).** The N1 arms pass `pinned` explicitly via `run_evaluate`; the
   rev path's default-pin branch (`pinned=None` → KILL_SET_PINNED) at a rev ≠ HEAD world is not
   exercised. No frozen mutant targets that branch.
3. **Counter: no defect found.** The v3 counter behaved exactly per its header on all five runs I
   made (base c1/r94c1, candidate c1/r94c1, plus the killpin control); classification, decoy
   handling and anchor counting all matched the specification.

## Counter runs (evidence index)

Lane receipts under `.ufo/waves/round-95/w1/ReviewerBatteryKills/`:
`base-c1.txt`, `base-r94c1.txt`, `cand-c1.txt`, `cand-r94c1.txt`, `cand-killpin.txt`,
`mut-n1.txt`, `mut-n5.txt`, `mut-n11.txt`, `mut-n10.txt`.

## Verification gaps / residual risk

- The plan's disclosed bound stands unchanged: a self-test sniffing its own compiled code objects
  while proving the decoy guard dead is outside the v3 counter's reach (plan § Disclosed bounds).
  This patch does not worsen it (its arms are behaviour-only).
- Killing the frozen mutant set shows those mutants die, not that every mutant dies (plan §
  Disclosed bounds).
- Round-92 controls on the candidate are not runnable by design (lane-rev-scoped); covered at
  landing by L1 (observation 1).
- Timing: honest self-test 46 assertions; candidate counter runs ~58 s each, well under the 600 s
  timeout; run errors 0 everywhere.

## Attribution / bounds compliance

Seat ReviewerBatteryKills only. Writes: this report, receipts under
`.ufo/waves/round-95/w1/ReviewerBatteryKills/`, and my scratch
`/fast/scratch/hyaku/kotoba-r95/ReviewerBatteryKills/` (deleted before yield). Git writes only in
my scratch clone (candidate commit). No pacman, no tool installs, no host/kernel setting touched,
no secrets, no /proc/sys. Message traffic: none needed (no blockers).
