source: S258 (Nosek et al., "The preregistration revolution", PNAS 2018, https://pmc.ncbi.nlm.nih.gov/articles/PMC5856500/, anchor §Preregistration Distinguishes Prediction and Postdiction, HTML line 1451, revision PMC5856500) and S259 (own-work: corpus/lessons/round-88-verifier-spotcheck.md @ a5b3b15c00b1de5db321e4226a0a7db17340e605, lines 73-74)
verified-at: 2026-11-05 @ plan draft 43fc7840202d542bcd1f5d7fab6e6f3dbb7f19b3 (addendum 1: plans/round-89-addendum-1.md)
recheck: python3 -B verifiers/check_freeze_gate.py --self-test (expect `0 failure(s) over 30 assertions`, exit 0) and python3 -B verifiers/check_freeze_gate.py --plan verifiers/fixtures/freeze-gate/r88-controls.md (expect exit 1, `REFUSED control w_added_red`)

# Freeze gate: a declared control must be observed before the freeze

## What the gate refuses

`verifiers/check_freeze_gate.py` executes every control a plan declares under a `## Controls` block,
before the plan's freeze commit, and refuses the freeze when an observed result contradicts the declared
expectation. An expectation is `expect: exit <rc>; stdout contains <literal>` (A2: the stdout literal is
required, so an exit-only declaration cannot pin an observable verdict).

The class it closes is the round-88 failure (`corpus/lessons/round-88.md` § Mistakes row 2): the freeze
shipped a control `w_added_red` whose declared FAIL the predicate could not produce, and the control was
never executed before the freeze. The round-88 spot-check's routed defect 3 (S259) asked for a freeze
that "must execute every frozen control and refuse the freeze on an expectation the predicate cannot
satisfy".

## What the gate measures, and what it does not

- Measured: declared exit code and stdout literal against the observed exit and stdout of each control's
  command, run in the lane with the TMPDIR honoured and a timeout.
- Oracle for the round-89 controls: `verifiers/fixtures/freeze-gate/sim-*.sh`, each a receipt grep over the
  committed round-88 receipts. A missing receipt makes the simulator exit 2 (fail-closed; ReviewerFreezeGate
  rename probes, all six sims).
- Not measured: whether the predicate is satisfiable in general. The headline is therefore bounded (addendum
  1, A2.3) to "refuses a declared expectation that contradicts the control's recorded verdict". The reproduction
  of round 88 is mechanical: the same gate refuses `r88-controls.md` (exit 1) and holds `r88-controls-fixed.md`
  (exit 0).
- Known doc-truth drift, recorded not repaired: a duplicate control name is documented as invalid spec but is
  processed as two entries, the first observed refusal winning (ReviewerFreezeGate F-risk-2; addendum A2.4).

## Shape of the fixtures

`r88-controls.md` declares what the round-88 freeze expected for its four C2 controls; `r88-controls-fixed.md`
declares the observed verdicts recorded in the committed round-88 receipts
(`corpus/lessons/round-88-verifier-spotcheck.md` § Routed defects; `.ufo/waves/round-88/w1/ExecMonotoneD5.md`
F1 records `w_added_red` observed PASS).

## Inference, labelled

S258 does not discuss executable controls. The sentence "a control whose expectation cannot be observed under
that commitment is not a confirmation" is this lane's inference from S258's preregistration principle
(S258 quote, HTML line 1451: "committing to analytic steps without advance knowledge of the research outcomes").

## Bounds

The gate reads its own plan file and the named commands. A control that is itself wrong (a simulator that
prints the wrong verdict from a correct receipt) is outside what the gate can see; the simulators are
receipt-grounded and their outputs are pinned to fixed sentences.
