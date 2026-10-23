Result: DONE — fault_injection_corpus.sh's 4d700b17 changes are harness/stale-expectation repairs that do not weaken detection (two mutation probes confirm), and the remaining red (FAIL-control-dirty, fault-f FAIL) is a real corpus finding at tip `f0e6b695`, with one stale-baseline contributor.

Seat: KotobaR55.ReviewFaultInjection (reviewer, wave 2 falsify, routed defect 6). Read-only on the lane; all execution in sandbox clone `/fast/scratch/hyaku/kotoba-r55/ReviewFaultInjection` at `f0e6b695b746775823b65a8c45de7d50ea33e84f` (cloned 2026-10-23T00:11:49Z, `date -u`; TMPDIR `/fast/scratch/hyaku/kotoba-r55/ReviewFaultInjection-tmp`). No tools installed; no network fetches.

## Runs (sandbox, all under `timeout 900`)

1. Entry: `TMPDIR=... timeout 900 bash verifiers/fault_injection_corpus.sh` → exit 1, `verdict: FAILURES PRESENT`. Rows:
   - `fault-0-control | integrity | 1 | corpus.pointers.commit_unresolvable | FAIL-control-dirty`; independent also exit 1.
   - must-fire a–e all PASS (class seen among drifts); `fault-g | ... | PASS(no new drift vs control)`; `fault-h | ... | PASS(context: quoted=2, control=1, checked=54 unchanged)`.
   - `fault-f | integrity | 1 | corpus.pointers.commit_unresolvable | FAIL`.
2. `--self-test` → exit 0: T1 must-fire fires on planted (a); T2 no-op world preserves control result (exit=1, fired=corpus.pointers.commit_unresolvable); T3 must-not-fire preserves control result; T4 plant guard rejects unmutated world. `self-test: OK`.
3. Instrument on pristine tip checkout: `python3 -B verifiers/verify_corpus_integrity.py --repo . --no-baseline --json` → exit 1, zero-mode DRIFT only `commit_unresolvable=1`, detail `corpus/lessons/round-54-verifier-spotcheck.md:147: 451a02ff`; all other zero checks clean (`unindexed=0`, `stale_patterns=0`, `missing_paths=0`, `report_dead=0`, `commit_nonhash=0`).
4. Baseline mode (same command without `--no-baseline`) → exit 1, DRIFT on `tracked_files` (expect 81, observed 84), `report_total` (expect 51, observed 54), `commit_total` (expect 32, observed 33), plus the same `commit_unresolvable`.
5. `git cat-file -e '451a02ff^{commit}'` → `fatal: Not a valid object name 451a02ff^{commit}`, exit 128 (matches round-54 spotcheck §3: not a lane object; it is the google-gemini/gemini-cli commit in S060's URL).

## Findings

1. [Confirmed real] The remaining control red is a genuine corpus finding, not a harness false negative. The instrument itself reports zero-mode DRIFT `commit_unresolvable=1` on a pristine clone of the tip tree (evidence 3, 5). The gate's `FAIL-control-dirty` correctly refuses to pass. The `fault-f` FAIL is likewise honest: its control is dirty, so the blind-spot count/baseline signal is not distinguishable; the repaired predicate refuses to fabricate a PASS (evidence 1).
2. [Minor, maintenance] A secondary contributor to `fault-f`'s red is stale baseline count expectations: `verifiers/corpus-baseline.json` expects tracked_files 81 / report_total 51 / commit_total 32 while the tip tree has 84 / 54 / 33 (evidence 4). That is refresh lag (counts recorded before round 54–55 growth), not a corpus defect; it keeps baseline-mode control exit 1 so `ctl_base_ex=0` cannot hold.
3. [Change review — no detection weakening] Each change is a stale-expectation or harness-defect repair, verified by mutation probes on copies of the tip script (fault_mut_a.sh / fault_mut_g.sh in the sandbox):
   - M1, must-fire reversion: `plant_a` altered to append the pointer double-quoted (plant passes its own marker grep; the injection no longer creates a dead pointer). Run → `fault-a | integrity | 1 | corpus.pointers.commit_unresolvable | WRONG-CLASS(expected=corpus.pointers.report_dead)`, exit 1. The gate notices the reverted injection.
   - M2, must-not-fire strengthening: `plant_g` altered to also plant a real dead pointer. Run → `fault-g | integrity | 1 | corpus.pointers.report_dead,corpus.pointers.commit_unresolvable | FALSE-POSITIVE`, exit 1. The gate notices the new drift vs control.
   - `fault_h_context` replaces the stale absolute `quoted=1` with a control-relative `quoted = ctl_quoted + 1` while still requiring `checked` unchanged and drift set equal (evidence 1: quoted=2 vs control=1, checked=54 unchanged). `fault_must_not_fire` compares both instruments to control instead of demanding absolute exit 0. `fault_known_blind_f` is stricter (clean control in both modes, exact `base_ex=1`). Self-test T2/T3 are now control-relative but T1/T4 (machinery can fail; plant guard) are intact and pass.
4. [Residual] The registry row `SKILL.md:469` is still unannotated even though the gate legitimately stays red for the real finding in finding 1; the builder's proposed one-cell annotation (`ExecFaultInjection.md:28`) is not in the SKILL.md diff between `a10240c0` and the tip. Routed defect 6's "repair the gate" half is done; the "annotate the row" half is not.

## Residual risk / verification gaps

- Detection probes covered the must-fire reversion and must-not-fire strengthening directions; the blind-spot (f) direction cannot be positively exercised while the control is red on a real finding. Its new predicate was reviewed statically (requires `ctl_ex=0`, `ctl_fired=-`, `ctl_base_ex=0`, `base_ex=1`, `delta=1`).
- Green depends on repairing the genuine finding (`round-54-verifier-spotcheck.md:147` cites bare `451a02ff`, a non-lane commit) and refreshing `corpus-baseline.json` counts; neither is this seat's to fix.
