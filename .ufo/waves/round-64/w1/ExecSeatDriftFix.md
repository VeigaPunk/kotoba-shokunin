# ExecSeatDriftFix — C2 check 4

## Finding and exact appended note

I read `plans/round-64.md` § C2 (check 4), `.ufo/waves/round-63/w2/ExecW2E2Patch.md` §6 (the table's 21-assertion cell), and `corpus/lessons/round-63-verifier-spotcheck.md` § “Routed defects and notes for the lane,” item 4. No production file was edited.

Append this one paragraph to `.ufo/waves/round-63/w2/ExecW2E2Patch.md`:

> 2026-10-24 — Drift note (for the round-64 wave-evidence commit; its hash is pending landing): I ran `python3 -B verifiers/check_r63_routed_repairs.py --self-test`, which printed `self-test: 0 failure(s) over 23 assertions` and exited 0; the table's 21 is an intermediate tally. The spot-check's defect 4 says, “ExecW2E2Patch's table records the patched C2 counter at "21 assertions"; the committed counter has 23 (my count).” This append records the measured `23` and resolves the reported assertion-count drift.

The commit name is a plan-based handoff label, not an existing hash: the frozen plan places wave evidence after the corpus/LOG/SCORECARD commit. [INFERENCE] The amended seat artifact belongs in the round-64 wave-evidence commit; its hash is not yet available.

## Measurement evidence

Command run from the lane root:

```text
$ python3 -B verifiers/check_r63_routed_repairs.py --self-test
      label-only: base: rc=0 count=5 (want rc!=0 count<5)
      honest/base: base: rc=1 count=0 (want rc!=0 count<5)
      fingerprint: base: rc=1 count=0 (want rc!=0 count<5); partial: rc=0 count=5 (want rc!=0 count<5)
      honest/partial: base: rc=1 count=0 (want rc!=0 count<5); partial: rc=1 count=2 (want rc!=0 count<5)
      worktree-read: base: rc=1 count=0 (want rc!=0 count<5); target: rc=1 count=4 (want rc=0 count=5)
      honest/target: base: rc=1 count=0 (want rc!=0 count<5); target: rc=0 count=5 (want rc=0 count=5)
self-test: 0 failure(s) over 23 assertions
exit=0
```

## Check 4 boundary rule

Plan § C2 check 4 requires the amended `ExecW2E2Patch.md` to name the computed exact count `23` with non-hex boundaries. In the proposed note, the measurement is `over 23 assertions`: the immediately adjacent characters are spaces, so neither boundary is hexadecimal. The quoted defect sentence independently says `has 23 (my count)`, also bounded by spaces/parenthesis. Thus the note text meets check 4's number-boundary condition. This seat did not append it to the protected artifact, so full check-4 closure remains contingent on the L1 landing the paragraph at the measured revision and running the frozen counter.

## Grep proof

The specialized grep with non-hex-boundary regex `(^|[^A-Fa-f0-9])23([^A-Fa-f0-9]|$)` matched proposed-note line 9; its result includes `self-test: 0 failure(s) over 23 assertions`. This confirms the note itself contains the measured number with spaces on both sides.

## Scope

No tools were installed. Only this seat report was written; no lane file, Git index, jj state, or external substrate was changed.