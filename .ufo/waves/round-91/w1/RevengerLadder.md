# RevengerLadder — scoped findings (round 91, w1)

Hypothesis: every exit rung of `verifiers/check_freeze_gate.py` matches the docstring ladder
(0 pass, 1 refused, 2 could-not-evaluate, 3 invalid spec).

**Verdict: FAILS** (first mismatch at base: non-UTF-8 plan → rc 1 traceback where rung 2 is documented).

- Base `9af1a7af2adf0ab07cfd53f92affc1ed8d992262`: non-UTF-8 plan exits 1 with `UnicodeDecodeError` (uncaught; `except OSError` misses it). The candidate (`ExecLadder.patch`, `except (OSError, UnicodeError)`) returns rc 2 with the documented `COULD-NOT-EVALUATE: cannot read plan` line. Repaired by the candidate.
- Residual on both trees: `--work` under a regular file exits 1 with an uncaught `NotADirectoryError` traceback. Rung 1 names a refused control, so this is a strict-reading mismatch. Not repaired (ExecLadder F4; outside the routed pointer).
- Candidate `--self-test` exits 1 (`freeze_gate floor 30 != self-test assertion count 31`). The patch cannot land alone; the `freeze_gate` floor bump (floors-registry.json and the two in-file tables of check_assertion_floors.py) must land with it. Plan C2 leg B(b) is not met by the patch alone.
- All other rungs (pass, refused, missing/unreadable/unexecutable/timeout = 2, all invalid-spec forms = 3) matched on both trees (17 rows each).

Full table, commands, rc and first lines: `RevengerLadder/probe.md`. Raw receipts: `RevengerLadder/receipts/`.
Candidate commit in scratch: `057fbb54280faa30949838c23b59d11e1d34d9d7` (scratch clone only, not in the lane).
Lane was not written; no git write was run in the lane.
