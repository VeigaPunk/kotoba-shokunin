# ExecGateArms — self-test kill-arm design for C1/C2 successors

Seat: `KotobaR62.ExecGateArms` (leaf, operability). Date: 2026-10-23.
Lane `/home/vgpnk/Projects/shokunin/kotoba-shokunin` was read-only. This report is the only write. No git/jj mutation, dispatch, ask, test, or scratch write. No installs. The two assigned successor source paths were not present in the verifier directory listing when inspected, so this is a design and frozen-style cross-check, not an implementation review or run.

## Frozen style checked

- `verifiers/check_scoped_rules.py:1597-1619` uses `check(name, actual, expected)`, counts each assertion, and emits `FAIL <name>: got ..., expected ...` only on a failed assertion. Its world/predicate assertions at `:2444-2471` compute output from scored fixtures and finish with `self-test: <F> failure(s) over <A> assertions`; it returns 1 if any assertion fails. The new C1 arms should use this pattern and should not hard-code a green matrix sentence.
- `verifiers/check_routed_repairs.py:161-173,187-204,231-242` uses `expect(name, blobs, want)`, increments `arms`, prints `self-test <name>: <got> of 6 (want <want>) ok|FAIL`, and checks its expected arm count. Its existing all-absent fixture is explicitly `base-world: 0 of 6`. The CLI's unreadable-revision branch at `:149-152` prints `routed repairs verified could-not-evaluate: unreadable rev` to stderr and returns 2.
- Retained frozen-counter run evidence: `.ufo/waves/round-61/wave/ExecC2Audit.md:57-73` records `python3 -B verifiers/check_routed_repairs.py --self-test`, the 12 fixture lines (including `self-test base-world: 0 of 6 (want 0) ok`), `self-test: 0 failure(s)`, and `EXIT=0`; its recorded `date -u` is `Fri 23 Oct 2026 07:18:37 PM UTC`. This is prior committed evidence, not a run performed for this report.

## C1 — `check_erratum_absorption.py`

Use the frozen C1 counter as an immutable oracle: check its pinned hash before any instance scoring, and invoke the same arm-level helpers as the matrix. The five exact classes from `plans/round-62.md:40-60` are E2, E2b, E2c, E2e, E2f. The target should add the following ten named `check()` assertions (the survivor check is one tuple assertion; isolation is five).

| Arm | Fixture / exact assertion | Expected evidence line / result |
|---|---|---|
| **A. Counter-sha mismatch** | In a private temp copy of the frozen counter, change one byte; run the same counter-pin gate used by the instrument. Assert `(return_code, final_stderr_line, traceback_present) == (2, "could-not-evaluate: frozen counter sha256 mismatch", False)`. Do not alter the lane counter. | Exact stderr line: `could-not-evaluate: frozen counter sha256 mismatch`; exit **2**; no matrix summary. This follows the frozen C1 self-test's captured-`main()` exit-and-diagnostic assertions (`check_scoped_rules.py:1630-35`). |
| **B. Missing class** | Build the normal ten-instance fixture set, then remove both E2f instances / the E2f class from the candidate matrix. Assert `(return_code, final_stderr_line, matrix_summary_emitted) == (2, "could-not-evaluate: missing erratum class E2f", False)`. This must be a fail-closed input/evaluation error, not a 4-of-5 verdict. | Exact stderr line: `could-not-evaluate: missing erratum class E2f`; exit **2**; no `errata measured ...` line. |
| **C. Survivor is printed and counted** | Use one controlled accepted E2f event-claim instance that passes the frozen `action_conjunct` but is rejected by neither of the other guards. Capture the actual survivor records and computed summary; assert `(records, count, summary_line) == (["survivor E2f ST-E2f-event-claim: []"], 1, "surviving 1")`. `ST-E2f-event-claim` is a proposed synthetic fixture ID, not an observed lane ID. | Exact lines: `survivor E2f ST-E2f-event-claim: []` then `surviving 1`. The count must equal the number of emitted survivor records, not a literal independent of the fixtures. |
| **D1. Hollow auditor is killed** | Run a test auditor that prints the expected-looking predicate but omits the guard-disable / second-direction computation. Assert the candidate's self-test returns **1** and names the controls arm. The test harness should instrument guard-mutation calls, so a summary-only printer cannot satisfy it. | Proposed exact candidate diagnostic: `self-test controls: FAIL hollow auditor skipped guard-mutation direction`; exit **1**. |
| **D2. Label-only auditor is killed** | Run a constant-returning auditor on two held-out control pairs with the same visible label but opposite expected outcomes (one absorbed, one surviving). Assert it returns **1** and fails the controls arm; constants/labels alone must not satisfy both. | Proposed exact candidate diagnostic: `self-test controls: FAIL label auditor returned constants`; exit **1**. |
| **E. Guard-mutation isolation (five assertions)** | First assert the pristine ten class instances are rejected in pairs. Disable one guard at a time using the plan's admitting stub, restore it after each call, and compare the *whole* per-instance verdict map plus seeded controls to baseline. For each guard only that class's two verdicts may flip to accepted; the other eight instances and both controls must be unchanged. | Exact outcome lines (A=accepted, R=rejected; order fixed as shown): `guard mutation E2 isolation: E2=AA E2b=RR E2c=RR E2e=RR E2f=RR; controls unchanged`; `guard mutation E2b isolation: E2=RR E2b=AA E2c=RR E2e=RR E2f=RR; controls unchanged`; `guard mutation E2c isolation: E2=RR E2b=RR E2c=AA E2e=RR E2f=RR; controls unchanged`; `guard mutation E2e isolation: E2=RR E2b=RR E2c=RR E2e=AA E2f=RR; controls unchanged`; `guard mutation E2f isolation: E2=RR E2b=RR E2c=RR E2e=RR E2f=AA; controls unchanged`. Assert each complete vector, not just that the target pair changed. |

For the auditor-mutant diagnostics above, `self-test controls:` is intentional: plan §C1's kill rule says the hollow and label variants must fail the controls arm. On the normal instrument, all ten assertions should feed the frozen C1 aggregate style: `self-test: 0 failure(s) over <computed assertion count> assertions`, exit 0. A failure should be named by the `check()` helper; do not print a fabricated green predicate to hide it.

## C2 — `check_routed_repairs_v2.py`

Treat each listed input as a separate counted fixture arm. For the requested inventory there are **10 arms**: one base, six D trees, H1, H2, and one unreadable-revision case. Increment the arm counter for every case (including the CLI error case), then assert exactly 10. The successor's strict inequality for D trees is a requirement: do not replace it with an unmeasured exact score.

| Arm | Fixture / exact assertion | Expected evidence line / result |
|---|---|---|
| **A. Base world** | All six required blobs absent; assert `check_repairs(...) == 0`. | `self-test base-world: 0 of 6 (want 0) ok` — same exact form already exercised by the frozen counter. |
| **B1. D1 stale count** | Tree-derived count is 30 while LOG says 29; assert computed score `< 6`. | `self-test D1-stale-count: <computed K> of 6 (want <6) ok`, where K is the actual score 0–5. Do not invent K; the frozen plan specifies only `<6`. |
| **B2. D2 negation** | The correction is negated (`did not claim 32…`); assert computed score `< 6`. | `self-test D2-negated-correction: <computed K> of 6 (want <6) ok`. |
| **B3. D3 inverted pointer** | LOG names C1-measure as the true pointer and freeze2 as the wrong one; assert computed score `< 6`. | `self-test D3-inverted-pointer: <computed K> of 6 (want <6) ok`. |
| **B4. D4 bodyless census** | Census-after is only `exit=0`; assert computed score `< 6`. | `self-test D4-bodyless-census: <computed K> of 6 (want <6) ok`. |
| **B5. D5 substring IDs** | QUALITY/lesson use `Q560` and `M910`; assert computed score `< 6`. | `self-test D5-substring-ids: <computed K> of 6 (want <6) ok`. |
| **B6. D6 false ancestry receipt** | `exit 0` belongs to a different command and operands are not two distinct 40-hex hashes; assert computed score `< 6`. | `self-test D6-unowned-ancestry-exit: <computed K> of 6 (want <6) ok`. |
| **C1. H1 honest house style** | Six honest repairs, including split adjacent-line R-c pointers, asserted polarity, and `exit=0` census/ancestry style; assert score exactly 6. | `self-test H1-house-style: 6 of 6 (want 6) ok`. |
| **C2. H2 measured tip** | Score the H2 measured-tip tree through the production CLI/blob-read path, not only `check_repairs()` and not a constant. Assert exit 0 and the actual output line. | `routed repairs verified 6 of 6` and `self-test H2-measured-tip: exit 0 (want 0) ok`. The H2 bytes/revision must be the measurement target supplied for the run. |
| **D. Unreadable revision** | Through `main()`/CLI on an isolated repo, pass a valid-shaped but unresolved 40-hex revision; capture stdout/stderr. Assert return code exactly 2 and the frozen error line. | Stderr: `routed repairs verified could-not-evaluate: unreadable rev`; wrapper line: `self-test unreadable-rev: exit 2 (want 2) ok`. |
| **E. Arm-count guard** | Count all ten preceding fixture invocations. A dropped arm must make the self-test fail; e.g. remove D6 and leave the expected count unchanged. | Mutant diagnostic: `self-test arm-count: 9 (want 10) FAIL`, exit **1**. Healthy run ends `self-test: 0 failure(s)`, exit **0**. |

The D lines intentionally retain the frozen counter's `self-test <name>: <got> of 6 (want <want>) ok|FAIL` convention while changing the comparison for dishonest trees to `got < 6`. H1/H2 must compare to exactly 6. A label-only implementation must fail because every D/H/base result is computed from its input blobs; H1 and H2 prevent a reject-everything successor from passing.

## Risks and scope notes

1. **C1 frozen-plan survivor-count discrepancy:** `plans/round-62.md:35` freezes the printed predicate with `surviving 2`, but `:64-71` says the pre-data expected result is E2f surviving with `surviving 1`. Do not encode either full-matrix total into the isolated C1 survivor kill arm. The arm above makes the count unambiguous for its one-survivor fixture; the L1 should resolve which full-matrix sentence is normative before claiming the matrix result.
2. The plan does not state exact D-tree scores, only `<6`; hard-coding 5 would overconstrain the promised predicate. Print the actual computed K and compare strictly below 6.
3. H2 is only a true tip control if it runs the real CLI/blob path over the measured-tip bytes/revision. A synthetic `check_repairs()` call alone proves H1-style fixture scoring, not H2.
4. The assigned successor files were absent when checked; no source-level implementation or runtime behavior of either successor was verified. No tests/checks were run for this design report. LSP was unavailable in the exposed toolset; no definitions/refactors were needed.

## Retained evidence

- `plans/round-62.md:26-71,94-99,109-152` — frozen C1 matrix semantics, counter-sha and missing-class fail-closed requirement, survivor/control semantics, isolation kill rule, C2 D/H/base/unreadable requirements.
- `verifiers/check_scoped_rules.py:1597-1619,2444-2471` — frozen C1 assertion and computed-world self-test style.
- `verifiers/check_routed_repairs.py:39-45,125-152,161-242` — frozen C2 `expect()` output, base fixture, unreadable-revision behavior and arm-count guard.
- `.ufo/waves/round-61/wave/ExecC2Audit.md:57-73,111-118` — prior run transcript evidence. The self-test command/output/date/exit are recorded above; the unreadable-revision source branch itself is verified statically at `check_routed_repairs.py:149-152`.

No new measurements were made, so this report makes no new runtime pass/fail claim.

Installs: no installs.
Blockers: none.
Produced: C1/C2 self-test kill-arm assertions and expected evidence-line contracts, cross-checked against the frozen counters' self-test styles.