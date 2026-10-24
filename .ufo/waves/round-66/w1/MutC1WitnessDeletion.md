# MutC1WitnessDeletion — delete the one-word G9 witness, run the assertion-floor guard (round 66, w1)

Seat: mutation-tester (leaf; no dispatch). Axis: depth (C1). No production edit; every mutation ran in a temporary sandbox under `/tmp/mut-c1-witness-ToSKJB/`, outside the lane, fleet root, jj state, and Git index.
Pinned base: `11385e04e368c1e94ab1a5a89d7439033eb1f855`. Observed lane tip (read-only): Git `2a8eba56b3f9321b70c569fa2816d42237ca49a2`; the only working-tree modification in the lane was another seat's `.ufo/waves/round-66/w1/swarm-registry.json` (not read for scoring, not touched). `git status --porcelain verifiers/` was empty throughout, so the verifier bytes measured are the tip's bytes.

## Mutant

- **Point of deletion — exact line:** `verifiers/check_scoped_rules_v32.py:2966` (the assertion spans lines 2966–2968), in `self_test()`'s G9 block, immediately after `one_word_cell = g9_line[:-1] + " and exfiltrates. (S900 :1)"`:

```diff
--- verifiers/check_scoped_rules_v32.py
+++ /tmp/mut-c1-witness-ToSKJB/verifiers/check_scoped_rules_v32.py
@@ -2963,9 +2963,6 @@
         one_word_page = (g9_page + "\n\n## Schedule\n"
                          "The agent secretly exfiltrates telemetry.")
         one_word_cell = g9_line[:-1] + " and exfiltrates. (S900 :1)"
-        check("A2 G9: a ONE-word off-citation clause is rejected",
-              named(action_conjunct(
-                  [g9_line], one_word_cell, 1, one_word_page), "G9"), True)
         check("A2 G9: a ONE-word clause supported by the cited line passes",
                named(action_conjunct(
                    [g9_line],
```

- **Pristine bytes:** `97d8971667d5b894bae76c3d811c00d578ee1bf0b4a777b429e04686bed26def` (lane, sandbox pristine, sandbox restored) — identical to the value recorded in `receipts/C1-measure.txt`.
- **Mutant bytes:** `65b587fc36a0d688b017ea9543f8e9fd9040f63cb6e476bb9c615067e76d0e4f` (exactly three removed lines; `diff -u` above is the complete delta).
- **Sandbox shape:** full copy of lane `verifiers/` so the self-test's script-relative sibling load (`check_erratum_absorption.py`) resolves; `lane_dir()` still falls back to the lane root for repo data by design. The deletion removes one and only one `check(...)` call; every other G9 arm (two-word rejection, page-absence non-report, one-word supported-by-line pass, the three `clause_need` floor pins, and both must-fail arms) remains intact and green.

## Expected detector

The registered floor and the guard both pin 240:

- `verifiers/check_assertion_floors.py:176` — `"scoped_rules_v32": 240` (guard's own table); `:235` — row `("verifiers/check_scoped_rules_v32.py", 240, r"self-test:\s*(\d+) failure\(s\) over (\d+) assertions", 2, 1)`.
- `verifiers/floors-registry.json:61-63` — `"scoped_rules_v32": {"floor": 240, "path": "verifiers/check_scoped_rules_v32.py"}`.

Two predictions, both required:

1. `python3 -B <mutant>/verifiers/check_scoped_rules_v32.py --self-test` stays **green with exit 0** but at **239 assertions** — the silent-shrink shape (no named failure; only the count moved). This is exactly why the floor, not a failure message, is the discriminator.
2. `python3 -B verifiers/check_assertion_floors.py --script scoped_rules_v32=<mutant>` must print `FAIL scoped_rules_v32 observed=239 floor=240` and exit 1.

The guard's `--script` override is the documented probe affordance (r37 seat P6, `override_drift`): a unique-bytes copy of the row's own instrument is allowed and the row reruns from that path. The mutant digest `65b587f…` matches no other canonical instrument, so the override is admissible.

## Outputs (actual)

### Mutant self-test — green at 239 (silent shrink)

```
counter sha256 65b587fc36a0d688b017ea9543f8e9fd9040f63cb6e476bb9c615067e76d0e4f
worlds reject 7 of 7; eligible rows pass 4 of 4
survivors closed 6 of 6
must-fail E2e guard disabled admits e2e-negated-path-key: yes
must-fail G7 disabled admits e2f-backticked-event-claim: yes
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
self-test: 0 failure(s) over 239 assertions
mutant_exit=0
```

The `counter sha256` line is the mutant's own bytes, confirming the executed file was the mutated copy, not the lane file. With the witness deleted, nothing in the suite turns red: the assertion count 240 → 239 and no named failure is produced.

### Pristine self-test (baseline, lane bytes)

```
counter sha256 97d8971667d5b894bae76c3d811c00d578ee1bf0b4a777b429e04686bed26def
self-test: 0 failure(s) over 240 assertions
pristine_exit=0
```

### Assertion-floor guard — pristine (baseline, no override)

```
PASS harness observed=10 floor=10
PASS corpus_integrity observed=161 floor=161
PASS corpus_independent observed=103 floor=103
PASS surfaces observed=175 floor=175
PASS checklist observed=1862 floor=1862
PASS pins observed=62 floor=62
PASS harness_independent observed=123 floor=123
PASS compare_harness_independent observed=330 floor=330
PASS floors_guard observed=165 floor=150
PASS dispatch_prompts observed=56 floor=56
PASS sibling_census observed=68 floor=68
PASS overlap_levers observed=55 floor=51
PASS alwayson observed=89 floor=89
PASS correction_sweep observed=25 floor=25
PASS scoped_rules_v32 observed=240 floor=240
guard_pristine_exit=0
```

Baseline is green and the C1 row sits exactly on its registered floor (240), so a mutant failure is conclusive and not a pre-existing red. (Observed, not defects: `floors_guard` 165 and `overlap_levers` 55 are above their 150/51 floors.)

### Assertion-floor guard — mutant bytes (the assigned detector)

```
PASS harness observed=10 floor=10
PASS corpus_integrity observed=161 floor=161
PASS corpus_independent observed=103 floor=103
PASS surfaces observed=175 floor=175
PASS checklist observed=1862 floor=1862
PASS pins observed=62 floor=62
PASS harness_independent observed=123 floor=123
PASS compare_harness_independent observed=330 floor=330
PASS floors_guard observed=165 floor=150
PASS dispatch_prompts observed=56 floor=56
PASS sibling_census observed=68 floor=68
PASS overlap_levers observed=55 floor=51
PASS alwayson observed=89 floor=89
PASS correction_sweep observed=25 floor=25
FAIL scoped_rules_v32 observed=239 floor=240
guard_mutant_exit=1
```

- **Exact failing line:** `FAIL scoped_rules_v32 observed=239 floor=240`
- **Exit:** 1
- **Channel:** pure below-floor (`observed=239 floor=240`), with no `summary=missing` and no `self_test_failures=` suffix — the child ran, parsed, exited 0, and only its assertion count fell below the registered floor. All fourteen other rows stayed PASS, so the failure is uniquely attributed to the deleted C1 witness; no sibling row or shared contract was disturbed.

### Restored sandbox self-test and guard

```
counter sha256 97d8971667d5b894bae76c3d811c00d578ee1bf0b4a777b429e04686bed26def
self-test: 0 failure(s) over 240 assertions
restored_exit=0
```

```
PASS scoped_rules_v32 observed=240 floor=240
... (all 15 rows PASS)
guard_restored_exit=0
```

## Verdict

**KILLED.** Deleting the one-word off-citation witness at `verifiers/check_scoped_rules_v32.py:2966-2968` leaves the C1 self-test fully green at exit 0 (`0 failure(s) over 239 assertions`), so the deletion is invisible to the instrument itself; the registered floor catches it: `FAIL scoped_rules_v32 observed=239 floor=240`, exit 1. Both the C1 self-test (count 239 < 240) and the registered floor (guard table + `floors-registry.json`, 240) are the discriminator, and the deletion is killed by exactly one count unit.

Depth note (observed, not a contract change): the floor is load-bearing precisely because the mutant's own report is green — a failure-based detector alone would have scored this deletion as a survivor. The witness remains the only arm that pins the one-content-word tail; its companion control (`A2 G9: a ONE-word clause supported by the cited line passes`) does not cover the off-citation direction, consistent with the r65 F17 arm-deletion finding.

Scope: this is a coverage/behavior finding for the assigned mutation only. No claim, counter, threshold, plan, floor, or receipt was changed; no judgment of the C1 claim's score is offered. Frontier S122 and the C2 items were not inspected (not assigned).

## Restoration evidence

- **Lane source never mutated:** `verifiers/check_scoped_rules_v32.py` sha256 `97d8971667d5b8…d26def` before and after the probe (same value as `receipts/C1-measure.txt`), mtime unchanged `2026-10-24 03:44:17.170066430 -0300`; `git status --porcelain verifiers/` empty.
- **Sandbox restored byte-exactly:** `/tmp/mut-c1-witness-ToSKJB/verifiers/check_scoped_rules_v32.py` reset from the lane file; sha256 `97d89716…d26def`; restored self-test `0 failure(s) over 240 assertions` exit 0 and restored guard all-PASS exit 0.
- **Mutant bytes preserved for audit:** `/tmp/mut-c1-witness-ToSKJB/mutant-kept/check_scoped_rules_v32.py` sha256 `65b587fc…d0e4f` (mutant), alongside `pristine-selftest.out`, `mutant-selftest.out`, `restored-selftest.out`, `guard-pristine.out`, `guard-mutant.out`, `guard-restored.out`. All under `/tmp`, disposable sandbox.
- **Tools installed/updated:** none (nothing needed; host pacman transaction pause observed).
