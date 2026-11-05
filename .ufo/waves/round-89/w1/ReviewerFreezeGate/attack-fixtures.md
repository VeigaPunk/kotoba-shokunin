# attack-fixtures — ReviewerFreezeGate (r89-w1, C1)

Informative fixture-world records forged by ReviewerFreezeGate. Plan files
verbatim; outputs re-observed on the final gate bytes
(sha256 `a20e6f9afff367dfb56b3d8fa437a176627bf55623d1f6b20dea320943e15e41`).

## The six forged plans (verbatim body, minus this header)
Each under this dir as `<name>.md`; body exactly as run.

- `attack-1-zero-on-refusing.md` — `- control w_added_red: bash
  verifiers/fixtures/freeze-gate/sim-w-added-red.sh` `expect: exit 0`.

- `attack-2-false-command.md` — `- control always_false: false` `expect: exit 0`.

- `attack-3-wrong-literal.md` — `- control w_tip: bash
  verifiers/fixtures/freeze-gate/sim-w-tip.sh` `expect: exit 0; stdout
  contains D5=TAMPERED`.

- `attack-4-second-fails.md` — `- control good_one: bash
  verifiers/fixtures/freeze-gate/sim-w-healed.sh` `expect: exit 0; stdout
  contains D5=PASS`; second control `- control bad_two: /bin/sh -c 'echo
  bad_two D5=PASS; exit 1'` `expect: exit 0; stdout contains D5=PASS`.

- `attack-5-unexpected-exit2.md` — `- control exits_two_once: /bin/sh -c
  'echo "sim: transient hiccup" >&2; exit 2'` `expect: exit 0`.

- `attack-7-order-litmus.md` — `- control w_added_red: bash …sim-w-added-red.sh`
  `expect: exit 0; stdout contains D5=PASS`; `- control w_tip: bash
  …sim-w-tip.sh` `expect: exit 0; stdout contains D5=PASS`.

- `attack-8-hidden-reentry.md` / `attack-8-h2-placement.md` — heading
  re-entry worlds; both `INVALID SPEC: empty ## Controls block`, exit 3.

## Observed outputs (gate, lane working tree, final gate bytes)

    A1 exit=0 : freeze gate: 1 control(s) held — freeze may proceed
    A2 exit=1 : REFUSED control always_false (line 4): declared "exit 0"; observed exit=1 stdout= (exit mismatch: declared 0, observed 1)
    A3 exit=1 : REFUSED control w_tip (line 4): declared "exit 0; stdout contains D5=TAMPERED"; observed exit=0 stdout=w_tip D5=PASS\n (stdout literal 'D5=TAMPERED' absent from observed stdout)
    A4 exit=1 : REFUSED control bad_two (line 6): declared "exit 0; stdout contains D5=PASS"; observed exit=1 stdout=bad_two D5=PASS\n (exit mismatch: declared 0, observed 1)
    A5 exit=1 : REFUSED control exits_two_once (line 4): declared "exit 0"; observed exit=2 stdout= (exit mismatch: declared 0, observed 2)
    A6 exit=0 : freeze gate: 1 control(s) held — freeze may proceed   (nondet world; re-run >10× stable)
    A7 exit=0 : freeze gate: 2 control(s) held — freeze may proceed

## Sim receipt-rename probes (clone /fast/scratch/hyaku/kotoba-r89/ReviewerFreezeGate/repo)

Receipts moved away from their committed paths one at a time and restored
after each (cmp bit-identical in every case):

    ExecMonotoneD5/receipts.txt absent →
      sim-w-added-red   rc=2  receipt missing: …/ExecMonotoneD5/receipts.txt
      sim-w-silenced    rc=2  receipt missing: …/ExecMonotoneD5/receipts.txt
      sim-w-healed      rc=2  receipt missing: …/ExecMonotoneD5/receipts.txt
    ExecMonotoneD5.md (review-row) absent →
      sim-w-added-red   rc=2  receipt missing: …/ExecMonotoneD5.md
    CriticFalsify/attacks.md absent →
      sim-w-silenced    rc=2  receipt missing: …/CriticFalsify/attacks.md
    receipts/before-C2-tip.txt absent →
      sim-w-tip         rc=2  receipt missing: …/receipts/before-C2-tip.txt
    receipts/l1-c2-tip.txt absent →
      sim-w-tip         rc=2  receipt missing: …/receipts/l1-c2-tip.txt
    ReviewerC2/review.md absent →
      sim-w-tip         rc=2  receipt missing: …/ReviewerC2/review.md

Receipts present (committed bytes) with all sims runnable:

    clone unsat plan  exit=1  REFUSED control w_added_red (line 36) … D5=PASS\n …
    clone fixed plan  exit=0  freeze gate: 4 control(s) held — freeze may proceed
    receipt absent    unsat → still exit=1 REFUSED … observed exit=2 …  (no silent pass)

## Grammar/shape probes (direct gate runs on constructed plans)

    duplicate names    exit=1  REFUSED control same-name (line 2)  (docstring says SpecError; reviewed as doc-truth drift)
    CRLF plan file     exit=1  REFUSED control c1 (line 2)         (CRLF tolerated, trailing CR treated as ws)
    %-prefixed line    exit=3  INVALID SPEC: unrecognized line inside ## Controls block (line 2)
    '- control: no-name' exit=3 INVALID SPEC: unrecognized line inside ## Controls block (line 2)
    '- control a false' (no colon) exit=3 INVALID SPEC: unrecognized line (line 2)
    'expect: stdout contains x; exit 0' (clause order) exit=0 (order not enforced — valid spec)
    h2-later-heading re-open  exit=3 INVALID SPEC: empty ## Controls block
    indented 2sp heading (closing) exit=1 (parsed as 'deep' control name; refuses on that control)
    '  ## Controls' (leading spaces before header) does NOT open a block; errors on content inside

## Predicate-arm re-runs (lane, final gate bytes)

    self-test           exit=0  0 failure(s) over 30 assertions
    r88-controls.md     exit=1  REFUSED control w_added_red (line 36): declared "exit 0; stdout contains D5=FAIL"; observed exit=0 stdout=w_added_red D5=PASS\n …
    r88-controls-fixed  exit=0  freeze gate: 4 control(s) held — freeze may proceed
