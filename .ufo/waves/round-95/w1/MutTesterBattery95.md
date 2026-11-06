# MutTesterBattery95 — round 95, wave r95-w1 — mutants beyond the frozen set (C1)

Seat: MutTesterBattery95 (mutation-tester). Status: DONE (attack seat; candidate
`8e3f1b04117bbaf4da2c461abcb3ac32f4346841` = freeze `673d1e2e…` + `ExecBatteryKills.patch`
sha256 `f9506fe3…41d96`, verified against `ExecBatteryKills_READY` before apply).

## Tasking

On the candidate (freeze `673d1e2e6f850bb54dda9698cf825cf6788c7d0d` + `ExecBatteryKills.patch`),
design at least 8 NEW mutants of the `--rev` manifest/pin path of
`verifiers/check_mutation_battery.py`, not among the frozen n1/n5/n11/n10. Apply each with the
counter's method (literal substitution, source-blind via the counter's RUNNER) and classify
KILLED (REPORTED-FAILURE) / RUN-ERROR / SURVIVED. Re-run the round-94 survivor N4 (pin check moved
after the probe loop) and say whether it is observable at all.

## Method

- Candidate: freeze `673d1e2e6f850bb54dda9698cf825cf6788c7d0d` + `ExecBatteryKills.patch`,
  built in scratch clone `/fast/scratch/hyaku/kotoba-r95/MutTesterBattery95/repo`
  (`git rev-parse --show-toplevel` verified equal to the clone) and committed with the scratch
  identity so the frozen counter can name the revision.
- Application method = the frozen counter's own: each mutant is a literal substitution whose
  anchor occurrence count is asserted (all anchors verified to match exactly once at the freeze
  text); the mutated text is executed **source-blind** through the counter's `RUNNER` (imported
  read-only from `verifiers/fixtures/round-95/selftest-kills.py`): compiled under the
  instrument's path, executed as `__main__` with argv `[path, --self-test]`, while the
  instrument file on disk holds honest bytes.
- Classification = the counter's rule 1: REPORTED-FAILURE (exit 1, summary `N failure(s)` with
  N >= 1, at least one `FAIL ` line) -> KILLED; CLEAN -> SURVIVED; anything else -> RUN-ERROR.
  Honest baseline must be CLEAN or every reading is inconclusive.
- N4 (pin check moved after the probe loop) is a move, built as two literal edits: the 4-line
  pin-check block deleted and reinserted immediately before the results tally
  (`kills = [r for r in results …]`); both anchors asserted to match exactly once.
- Restoration: instrument bytes compared to the original after every run; `git status --porcelain`
  on the probe clone must be empty for the instrument.
- 11 new mutants (none of the frozen n1/n5/n11/n10; N10's `+1` shape excluded), each a plausible
  defect of the `--rev` manifest/pin path in `evaluate()` / `kill_set_check()`:

| id | anchor (abbrev.) | replacement (abbrev.) | defect modelled |
|---|---|---|---|
| m01 | `return n == want, "observed` | `return n == want + 3, "observed` | pin accepts exactly want+3 |
| m02 | `return n == want, "observed` | `return n <= want + 2, "observed` | pin accepts up to want+2 |
| m03 | `committed = git_show(lane, rev, MANIFEST)…` | `git_show(lane, rev + "^", …)` | manifest read at parent commit |
| m04 | `raise CouldNotEvaluate("manifest must name exactly the targets %s"` | `"manifest names unexpected targets %s"` | refusal message reworded |
| m05 | `if {row.target for row in rows} != set(PROBES):` | `if False:` | target-set check skipped |
| m06 | `kill_set_check(committed, pinned)` | worktree text when it differs from committed | pin fed working-tree text when dirty |
| m07 | `kill_set_check(committed, pinned)` | `kill_set_check(committed)` | caller's `pinned` ignored on the rev path |
| m08 | `if {…} != set(PROBES):` | `if {…} < set(PROBES):` | extra targets accepted (only missing refused) |
| m09 | `return n == want, "observed %d kill rows, pinned %d" % (n, want)` | `"observed %d kill rows" % (n,)` | pin detail drops the pinned number |
| m10 | `return False, "manifest malformed: %s" % exc` | `return True, …` | malformed manifest accepted by the pin |
| m11 | `want = KILL_SET_PINNED if pinned is None else pinned` | `want = pinned if pinned is None else KILL_SET_PINNED` | explicit pin and default swapped |

## Mutant table (measured on candidate `8e3f1b04117bbaf4da2c461abcb3ac32f4346841`)

Honest baseline: CLEAN, rc 0, `0 failure(s) over 46 assertions` (5.1 s). Counter sanity on the
same candidate: `C1 targets killed 3 of 3 (run errors 0); positive killed 1 of 1; honest CLEAN;
comment decoys held 3 of 3; code decoys held 3 of 3` — `C1-PREDICATE-MET`, rc 0
(`counter-c1-candidate.txt`). Every mutant ran source-blind through the frozen counter's RUNNER;
instrument bytes restored after every run (bytes match, `git status` clean, sha256
`f102b419f840ac284dcde959b4fc7d4e3dfe387e31bb3273a8a91dba660a109e`).

| id | verdict | rc | FAIL arms (evidence) |
|---|---|---|---|
| m01 pin `want + 3` | **KILLED** | 1 | 22 arms — every `run_main` world refuses: `could-not-evaluate: arm kill-set-size: … observed 9 kill rows, pinned 9`; incl. `satisfying world (clean)` and `kill-set-size rev path: a committed manifest matching the pin exits 0` |
| m02 pin `n <= want + 2` | **KILLED** | 1 | 8 arms — direct-call `dropped`/`k3`/`n11` arms and rev-path `revdrop`, `revadded`, `revn1`, `revn1r`, `revn11` (`revn11` asserts the 2-row world exits 2) |
| m03 manifest at `rev + "^"` | **KILLED** | 1 | 26 arms — every fixture is a single-commit repo, so `git show <rev>^:…` fails → CNE `G1: git show …^:… failed` (distinct from N1's `HEAD` shape and killed by both honest-expectation directions) |
| m04 target-set refusal reworded | **KILLED** | 1 | `n5 label-targets-cne: a committed manifest missing a probe target exits 2 naming the target set…` — the arm pins the refusal's exact message content, not just its exit code |
| m05 target-set check skipped | **KILLED** | 1 | same `n5 label-targets-cne` arm — with the check skipped the missing-target world **evaluates to rc 0** (the probe loop iterates manifest rows only, so no KeyError). Pre-registered RUN-ERROR expectation was wrong; measured outcome is a clean kill |
| m06 worktree text when dirty | **KILLED** | 1 | 3 arms — both new `n1 manifest-at-rev` two-commit arms (scratch clone worktree differs from the first commit) and `k1 working-tree read` (`observed 8 kill rows, pinned 9` from the dirty worktree) |
| m07 caller's `pinned` ignored | **KILLED** | 1 | `kill-set-size rev path: an unrelated baseline failure does not name kill-set-size` + `k2 label-every-cne (rev path)` (both pass `pinned_count + 1 = 10`; default 9 refuses) |
| m08 `!=` relaxed to `<` (proper subset) | **SURVIVED** | 0 | none — `0 failure(s) over 46 assertions`. The suite's only wrong-target world is a **missing-target** (proper subset) world, so `<` and `!=` are indistinguishable; no extra-target (superset) world exists |
| m09 pin detail drops `pinned %d` | **KILLED** | 1 | direct-call `arm kill-set-size (k3)` arm — requires `"pinned 17"` in the detail; detail shows only `observed 18 kill rows` |
| m10 malformed manifest accepted | **KILLED** | 1 | `arm kill-set-size: an unparseable manifest is refused, not raised` |
| m11 default/caller pin swapped | **RUN-ERROR** | 1 | crash, no summary: `TypeError: %d format: a real number is required, not NoneType` at `kill_set_check` line 189 via `run_main` worlds (`pinned=None` → `want=None`). Under the round-94 rule (`rc != 0` = killed) this scores KILLED; under the v3 rule 1 it is RUN-ERROR — a live demonstration of the round's mined-mistake fix |

Score: 9 KILLED, 1 SURVIVED, 1 RUN-ERROR, 0 NOT-EVALUATED. Every kill is a REPORTED-FAILURE
(a `FAIL ` line + `<N> failure(s)` with N >= 1, exit 1); no kill in the set is a crash-kill.

## N4 re-run (pin check moved after the probe loop)

**SURVIVED** — rc 0, `0 failure(s) over 46 assertions`, and the self-test's own stdout is
byte-identical to the honest run (`run-n4-pin-after-loop.txt` == `run-honest.txt`, 32 bytes:
the self-test prints only tally failures).

Observable at all? **Yes in principle, no to the arm suite.** A side experiment
(`n4observe.py`, receipt `n4observe/n4observe.txt`) executed the honest and N4 modules and ran
each module's `run_evaluate` on a pin-passing and a pin-failing rev-path fixture built with the
instrument's own helpers:

- pin-passing world (revok shape): honest rc 0 (23 lines), N4 rc 0 (23 lines), **0 diff lines**.
- pin-failing world (revdrop shape): honest rc 2 (**1 line** — the refusal only); N4 rc 2
  (**19 lines** — 11 row-status lines, G1/G2/G3 PASS lines and the predicate line precede the
  refusal), 22 diff lines. Exit code and the `kill-set-size` label are unchanged.

So N4's reordering is visible in `run_evaluate`'s captured buffer (refusal no longer first),
but the candidate arms assert only `rc == 2` and `"kill-set-size" in out` on that buffer — both
hold under N4 — and no arm asserts output ordering. A cheap optional arm (assert the refusal is
the first line of the revdrop buffer) would kill it; recorded as a coverage finding, not a
contract change.

## Findings

1. **Depth beyond the frozen set: 9 of 11 new mutants killed, all as REPORTED-FAILURE.** The
   candidate's arms are not one-assertion tricks: the kills span direct-call pin arms, both
   N1 two-commit rev-path arms, the N11 2-row and +3-row worlds, the N5 message-content arm,
   and the explicit-pin worlds (`pinned_count + 1`). The candidate is materially deeper on the
   `--rev` manifest/pin path than the frozen trio alone shows.
2. **Coverage gap (SURVIVED m08): the target-set check is pinned only on the missing-target
   side.** Relaxing `!= set(PROBES)` to `< set(PROBES)` (extra bogus targets accepted) changes
   nothing observable — the suite's single wrong-target world drops a target. A cheap extra
   world (manifest naming one probe target twice plus an unknown target, same kill count,
   expecting exit 2 naming the target set) would close it. Coverage finding, not a claim defect:
   C1's frozen targets stay killed; the predicate is untouched.
3. **Rule 1 demonstrably changes classifications (m11).** The pin-swap mutant crashes with an
   uncaught `TypeError` (exit 1, no summary). Under the round-94 rule it scores KILLED; the v3
   counter correctly scores RUN-ERROR. Direct evidence for the round's mined mistake
   `run-error-scored-as-kill`.
4. **N4 remains a survivor and is invisible to every arm**, though its reordering is detectable
   from the per-world captured buffer (refusal no longer the first line in pin-failing worlds).
   Same verdict as round 94; now with the precise observability boundary measured.
5. **Pre-registration corrections, recorded honestly:** m05 was expected to be RUN-ERROR (KeyError
   path) but is KILLED cleanly — the probe loop iterates manifest rows, not PROBES, so a
   missing-target manifest still evaluates (to rc 0, which the N5 arm refuses). m11 was expected
   KILLED and is RUN-ERROR (crash). m03's `rev^` kill is even stronger than predicted: 26 arms.

## Risks

- My candidate commit `8e3f1b04…` differs from the builder-quoted `3d13eb9…` only in commit
  metadata (separate scratch clones); the tree adds exactly the builder patch (67 insertions to
  `verifiers/check_mutation_battery.py` only) and the frozen counter reads `C1-PREDICATE-MET`
  on it. Verdicts are stated against my rev; re-running against `3d13eb9` should reproduce them.
- m08/n4 survivals are statements about THIS candidate's arm set (46 assertions). Any later arm
  addition can change them; receipts pin the exact instrument sha256
  `f102b419f840ac284dcde959b4fc7d4e3dfe387e31bb3273a8a91dba660a109e` per run.
- The N4 probe (`n4observe.py`) executes instrument code in-process outside the counter's
  RUNNER; it is an observability experiment only, never a kill measurement, and its fixture
  repos were created and removed entirely under the seat scratch.
- No counter defect found: no frozen anchor drifted (all anchors matched exactly once), and no
  run of the frozen counter was inconclusive.

## Hygiene

- Writes in the lane: this report, receipts under `.ufo/waves/round-95/w1/MutTesterBattery95/`
  only. No lane git writes; scratch-clone commit only (identity `scratch <scratch@invalid>`),
  toplevel asserted before committing. READY file untouched (builder-owned).
- Scratch `/fast/scratch/hyaku/kotoba-r95/MutTesterBattery95` deleted before yielding.
- No tooling installs, no pacman, no host/kernel setting changes, no secrets read or written.
- Poll: `ExecBatteryKills_READY` appeared on poll 3 (~6 min of a 75-minute budget).
