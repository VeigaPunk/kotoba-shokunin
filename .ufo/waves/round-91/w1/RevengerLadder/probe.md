# RevengerLadder — freeze-gate exit-rung probe (round 91, w1)

Hypothesis (one, falsifiable): every exit rung of `verifiers/check_freeze_gate.py` matches the module
docstring ladder — 0 pass, 1 refused, 2 could-not-evaluate, 3 invalid spec.

Trees measured (scratch clones, lane not written):
- **base** = `9af1a7af2adf0ab07cfd53f92affc1ed8d992262` (freeze commit, unmodified gate).
- **candidate** = base + `ExecLadder.patch` (ExecLadder verdict REPAIRABLE; `ExecLadder_READY` present),
  committed in scratch as `057fbb54280faa30949838c23b59d11e1d34d9d7` (scratch identity, scratch clone only).
  Its floor-coupling is NOT in the patch (see Finding 2).

Commands: `python3 -B verifiers/check_freeze_gate.py …` run from the clone root; `--work` pointed at scratch.
Scratch plans (missing command, timeout, non-executable command, no block, empty block, no command,
orphan expect, bad clause, prose line, exit-only expect, non-UTF-8 plan, `--work` under a file) are
under the scratch `plans/` and `work-extra/`; the driver scripts and raw results are in `receipts/`.
`rc` is the process exit code; "first line" is the first line of the observed stream.

## Table

| # | probe (abridged command) | rung claimed by docstring | base rc | candidate rc | first line (candidate; base where different) |
|---|---|---|---|---|---|
| A | `--plan verifiers/fixtures/freeze-gate/r88-controls-fixed.md` | 0 held | 0 | 0 | `freeze gate: 4 control(s) held — freeze may proceed` |
| B | `--plan verifiers/fixtures/freeze-gate/r88-controls.md` | 1 refused | 1 | 1 | `REFUSED control w_added_red (line 36): declared "exit 0; stdout contains D5=FAIL"; observed exit=0 stdout=w_added_red D5=PASS\n (stdout literal 'D5=FAIL' absent …)` |
| C2a | `--plan …/no-such-plan.md` (missing plan) | 2 could-not-evaluate | 2 | 2 | `COULD-NOT-EVALUATE: cannot read plan …no-such-plan.md: [Errno 2] No such file or directory` |
| C2b | `--plan plans/gone.md` (control command not found) | 2 | 2 | 2 | `COULD-NOT-EVALUATE control gone (line 2): command not found (rc=127)` |
| C2c | `--plan plans/slow.md --timeout 1` (`sleep 200`) | 2 | 2 | 2 | `COULD-NOT-EVALUATE control slow (line 2): timeout after 1s` |
| C2d | `--plan plans/noexec.md` (non-executable command) | 2 | 2 | 2 | `COULD-NOT-EVALUATE control noexec (line 2): command not executable (rc=126)` |
| C2e | `--plan verifiers/fixtures/freeze-gate` (a directory) | 2 | 2 | 2 | `COULD-NOT-EVALUATE: cannot read plan …freeze-gate: [Errno 21] Is a directory` |
| C3a | `--plan plans/no-block.md` | 3 invalid spec | 3 | 3 | `INVALID SPEC: no ## Controls block found` |
| C3b | `--plan plans/empty.md` | 3 | 3 | 3 | `INVALID SPEC: empty ## Controls block` |
| C3c | `--plan plans/nocmd.md` (control with no command) | 3 | 3 | 3 | `INVALID SPEC: control broken (line 2): no command` |
| C3d | `--plan plans/orphan.md` (expect with no control) | 3 | 3 | 3 | `INVALID SPEC: orphaned expect line (line 2): no preceding control entry …` |
| C3e | `--plan plans/badclause.md` (`expect: stderr contains x`) | 3 | 3 | 3 | `INVALID SPEC: control c (line 3): unrecognized expect clause 'stderr contains x'` |
| C3f | `--plan plans/prose.md` (prose line inside block) | 3 | 3 | 3 | `INVALID SPEC: unrecognized line inside ## Controls block (line 4): 'this is prose'` |
| C3g | `--plan plans/exitonly.md` (exit-only expect) | 3 | 3 | 3 | `INVALID SPEC: control healed (line 3): expect has no stdout literal (A2 …)` |
| C3h | no arguments | 3 (invalid invocation) | 3 | 3 | stderr `usage: check_freeze_gate.py [-h] [--self-test] [--plan FILE] [--work DIR]` |
| C3i | `--self-test --plan plans/empty.md` | 3 (invalid invocation) | 3 | 3 | stderr `usage: check_freeze_gate.py …` |
| O | `--self-test` | 0 | 0 | **1** | base `0 failure(s) over 30 assertions`; candidate `FAIL arm floors-row freeze_gate (path + floor == assertion count): freeze_gate floor 30 != self-test assertion count 31` |
| X1 | `--plan plans/nonutf8.md` (plan body contains byte 0xff) | 2 "the plan file unreadable" | **1** | **2** | base: stderr `Traceback … UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff`; candidate: `COULD-NOT-EVALUATE: cannot read plan …: 'utf-8' codec can't decode byte 0xff in position 66` |
| X2 | `--plan verifiers/fixtures/freeze-gate/r88-controls-fixed.md --work work-extra/afile/sub` (work root under a regular file) | not enumerated; spirit = 2 | 1 | 1 | stderr `Traceback (most recent call last):` (uncaught `NotADirectoryError` from `os.makedirs`) |
| X3 | `--self-test` (extra run) | 0 | 0 | 1 | as O |

Raw: `receipts/probe-results-base.tsv` (17 rows), `receipts/probe-results-candidate.tsv` (17 rows),
`receipts/extra-base.tsv`, `receipts/extra-candidate.tsv`; the base non-UTF-8 traceback in `receipts/out6.txt`;
the candidate commit and clean apply in `receipts/out7.txt` (`APPLIES-CLEAN`, rev `057fbb5…`).

## Verdict: FAILS

The hypothesis as stated does NOT hold. Two rung mismatches, one repaired by the candidate, one not:

1. **First mismatch — base, X1 (rung 2 mis-reported as rung 1).** A plan that is not UTF-8 raises
   `UnicodeDecodeError`, which is not an `OSError`, so the `except OSError` at `run_gate` escapes; CPython
   exits 1 with a traceback. The docstring assigns "the plan file unreadable" to rung 2. Observed base rc 1.
   The candidate (`except (OSError, UnicodeError)`) returns rc 2 with the documented
   `COULD-NOT-EVALUATE: cannot read plan` line. **This mismatch is repaired by the candidate.**
   The base probe confirms ExecLadder's derivation (not only its citation).
2. **Residual mismatch — X2, both trees (uncaught work-root failure).** `--work` under a regular file raises
   `NotADirectoryError` out of `run_control`'s `os.makedirs`, exit 1 with a traceback. Rung 1 is defined as
   "refused, naming the first violated control"; a traceback names no control, so exit 1 is not the
   documented rung 1 meaning. The docstring's rung-2 list does not name `--work`, so the strict reading is a
   mismatch and the lenient reading is not contradicted. Not repaired (ExecLadder F4, outside the routed
   pointer); a repair would be a scope widening, so this is routed, not fixed.

Everything else matched the documented ladder on both trees: pass (0), refused (1), missing / unreadable
/ unexecutable / timeout (2), and all invalid-spec forms (3), including the argparse usage path that the
`_Parser` comment maps to 3.

## Findings for the L1 (not repaired here)

- **F-1 candidate patch is not landable alone.** The patch adds one self-test arm (30 → 31 assertions). The
  existing `arm floors-row freeze_gate` asserts `floors-registry.json` floor == `len(ARMS)`, so the candidate's
  own self-test exits 1 (row O, X3). The bump (`freeze_gate` 30 → 31) must land with the patch in
  `verifiers/floors-registry.json` and the two in-file tables of `verifiers/check_assertion_floors.py`
  (ExecFloorsCap owns the row; the L1 integrates). Verified only in scratch by ExecLadder (floor 31 → exit 0).
  Plan C2 leg B(b) requires `--self-test` exit 0 at the landing: **not met by the patch alone.**
- **F-2 X2 residual** (above). Recorded for round 92; the plan's leg B(a) "honest stop" clause covers only the
  routed-pointer question, not this extra path.
- **F-3 (carried from ExecLadder, not re-probed here):** duplicate control names pass silently (F1); a
  signal-killed control reads `observed exit=-9` and refuses (F3, judgement).
- **Scope note:** this probe is a reverse-engineering read of observed rung behaviour. It did not change the
  instrument, the plan, the controls, or any frozen predicate.

## Confidence

High on every table row (each observed twice-readable from TSV; base rows reproduced against the same
scratch plans). High on X1 base/candidate (traceback and the repaired line both observed). Medium on X2's
classification as a mismatch: it turns on whether an uncaught `--work` failure is "rung 1" or an
uncovered case; the verdict is FAILS on the strict reading.
