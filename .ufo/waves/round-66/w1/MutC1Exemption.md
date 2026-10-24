# MutC1Exemption — old G9 one-word exemption reinsertion (round 66, w1)

Seat: mutation-tester (leaf; no dispatch). Axis: depth (C1). No production edit; all mutation work in a temporary sandbox.
Pinned base: `11385e04e368c1e94ab1a5a89d7439033eb1f855`. Observed lane tip (read-only measurement): Git `2a8eba56b3f9321b70c569fa2816d42237ca49a2`, jj working change `98c994b017ca50393e0316c8409028f8cdeb4031`.
Every measurement below ran against sandbox bytes; the lane tree was never written.

## Mutant

- Sandbox: `/tmp/mutc1exemption-MutC1Exemption/{pristine,mutant,restored}/verifiers/` — full copy of lane `verifiers/` (minus `__pycache__`) so the self-test's script-relative sibling load (`check_erratum_absorption.py`) resolves; `lane_dir()` falls back to the lane root as designed.
- Pristine bytes: `verifiers/check_scoped_rules_v32.py` sha256 `97d8971667d5b894bae76c3d811c00d578ee1bf0b4a777b429e04686bed26def` — identical in lane, sandbox `pristine/`, `mutant/`, and `restored/` before mutation; matches `receipts/C1-measure.txt`.
- Mutation applied at G9, inside `g9_conjunct`, immediately after the empty-clause skip:

```diff
@@ -1142,6 +1142,8 @@
         w = page_words(clause)
         if not w:
             continue
+        if len(w) < 2:
+            continue
         need = clause_need(len(w))
         if covered(w, line_w) >= need:
             continue
```

- Mutant sha256 `73c885784d5290a59c517fd5ed49ec821c20e4b1bb636b1221b5cbb2a8d61c10` (exactly two added lines; `diff -u` above is the complete delta).
- Fidelity check against the pinned base: `git show 11385e04…:verifiers/check_scoped_rules_v32.py` G9 contains `MIN_CLAUSE = 2` and `if len(w) < MIN_CLAUSE: continue` with the docstring "a one-word clause is below A2's own MIN_SHARED floor and stays exempt." The literal reinsertion reproduces that pre-landing skip behavior byte-for-behavior on clause length, while leaving the landed `clause_need` coupling in place.

## Expected detector

`python3 -B <copy>/verifiers/check_scoped_rules_v32.py --self-test` — the verifier's own bounded self-test (240 assertions at the measured tip), which carries the new witness `A2 G9: a ONE-word off-citation clause is rejected`. Expect exit 1 with that single named failure.

## Outputs (actual)

### Control probe — C1-one-word-control fixture, pristine vs mutant

Same fixture as `.ufo/waves/round-66/controls/C1-one-word-control.txt` (`line = "The index stores project rules."`, page adds `## Schedule\nThe agent secretly exfiltrates telemetry.`, `cell = line + " and exfiltrates."`), invoked directly on `g9_conjunct([line], cell, 1, page)`:

- pristine: `split: ['The index stores project rules', 'exfiltrates.']` → `['A2 G9: clause "exfiltrates." is supported outside the cited line']`
- mutant: `split: ['The index stores project rules', 'exfiltrates.']` → `[]` (the exact pre-landing control result; the mutation is a faithful proxy for the old exemption)

### Self-test on pristine bytes

```
counter sha256 97d8971667d5b894bae76c3d811c00d578ee1bf0b4a777b429e04686bed26def
worlds reject 7 of 7; eligible rows pass 4 of 4
survivors closed 6 of 6
must-fail E2e guard disabled admits e2e-negated-path-key: yes
must-fail G7 disabled admits e2f-backticked-event-claim: yes
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
self-test: 0 failure(s) over 240 assertions
pristine_exit=0
```

Baseline is green; the detector is not itself broken, so the mutant result is conclusive.

### Self-test on mutant bytes

```
counter sha256 73c885784d5290a59c517fd5ed49ec821c20e4b1bb636b1221b5cbb2a8d61c10
worlds reject 7 of 7; eligible rows pass 4 of 4
survivors closed 6 of 6
must-fail E2e guard disabled admits e2e-negated-path-key: yes
must-fail G7 disabled admits e2f-backticked-event-claim: yes
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
FAIL A2 G9: a ONE-word off-citation clause is rejected: got False, expected True
self-test: 1 failure(s) over 240 assertions
mutant_exit=1
```

- Named failure: `FAIL A2 G9: a ONE-word off-citation clause is rejected: got False, expected True`
- Exit: `1`
- Exactly one failure over the same 240 assertions; the companion arm `A2 G9: a ONE-word clause supported by the cited line passes` stayed green, so the mutation is attributed solely to the off-citation witness and does not merely over-reject the accepted one-word case.
- The mutant run's `counter sha256` is its own bytes (`73c88578…`), confirming the detector executed the mutated copy, not the lane file.

### Self-test after restoration

```
$ cp /tmp/mutc1exemption-MutC1Exemption/pristine/verifiers/check_scoped_rules_v32.py \
     /tmp/mutc1exemption-MutC1Exemption/mutant/verifiers/check_scoped_rules_v32.py
$ sha256sum lane/verifiers/check_scoped_rules_v32.py sandbox/{pristine,mutant}/verifiers/check_scoped_rules_v32.py
97d8971667d5b894bae76c3d811c00d578ee1bf0b4a777b429e04686bed26def  lane/verifiers/check_scoped_rules_v32.py
97d8971667d5b894bae76c3d811c00d578ee1bf0b4a777b429e04686bed26def  sandbox/pristine/verifiers/check_scoped_rules_v32.py
97d8971667d5b894bae76c3d811c00d578ee1bf0b4a777b429e04686bed26def  sandbox/mutant/verifiers/check_scoped_rules_v32.py
...
self-test: 0 failure(s) over 240 assertions
restored_exit=0
```

## Verdict

**KILLED.** The C1 one-word witness kills the old `len(w) < 2` exemption: the pre-landing control advertises the defect (`[]`), pristine bytes are green at 240/0, and reinserting the skip turns the self-test red at exit 1 with the single named assertion `A2 G9: a ONE-word off-citation clause is rejected`. The exemption is no longer admissible; `clause_need(1) = 1` plus the witness is load-bearing.

Scope note: this is a coverage/behavior finding for the assigned mutation only. No claim, counter, threshold, plan, or receipt was changed; no judgment of the C1 claim's score is offered.

## Restoration evidence

- Lane source never mutated: `verifiers/check_scoped_rules_v32.py` sha256 `97d8971667d5b8…d26def` before and after the probe (same value as `C1-measure.txt`); `git status --porcelain verifiers/` remained empty.
- Sandbox mutant path restored byte-exactly to pristine: `97d89716…d26def` == pristine == lane, and the restored copy's self-test printed `0 failure(s) over 240 assertions`, exit 0.
- Sandbox retained at `/tmp/mutc1exemption-MutC1Exemption/` (pristine/mutant-now-restored/restored copies, `restored.out`) for audit; it is outside the lane, fleet root, jj state, and Git index.
- Tools installed/updated: none (host pacman transaction pause observed; nothing needed).
