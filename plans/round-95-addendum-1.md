# Round 95 — addendum 1 (integration disclosures; KotobaR95, after the landing reading)

Written after the scored landing reading at `d1144fab4b31f1f5196cb347303894e7b1e54eda`, so it changes
**nothing** that was frozen at `673d1e2e6f850bb54dda9698cf825cf6788c7d0d`: the predicate sentence,
the counter (`verifiers/fixtures/round-95/selftest-kills.py`, sha256 `d6ae74af…1d269001`), the
mutant table, the kill rule and the target stand as frozen. This addendum only discloses what the
attack seats found and routes it. The C1 verdict is the non-author closure's.

## A1 — the counter's anti-sniffing bound is wider than the plan states

The plan's § Disclosed bounds names "a self-test that sniffs its own compiled code objects (not
its source file) and proves the decoy guard dead". Two attack seats measured that bound and one
wider shape:

- **Guard-aware bytecode sniffers** (ReviewerCounterV3 f8; ExecCounterForgery g2): a ~20-line `dis`
  scan that skips the body under the decoy guard counts N5 (g2: N1 and N5) KILLED with both decoys
  held. Both worlds still read UNMET because the other targets survive, so the predicate was not
  met by a forgery — but the per-target defence is gone for this shape.
- **Recompile-and-compare** (ExecCounterForgery g3, finding F2): a self-test that recompiles its own
  on-disk file and compares `co_code` with the running functions detects a source-blind run without
  reading for the mutant's text; it killed N1 and N11 with every decoy held (N5 survived because the
  comparison was on `co_code` only). Rule 3's wording ("text, tokens, AST, inspect/linecache") does
  not name this shape; a `co_consts`-aware version would plausibly kill all three [INFERENCE: not
  built]. This is outside the plan's stated bound.

Consequence for the reading: `C1-PREDICATE-MET` at the landing shows the frozen targets are killed by
a self-test that is not one of the eleven forgery shapes measured (f1–f6, g1–g5); it does not by
itself prove the arms are behavioural. That proof is the independent hand-application by three
seats that named the failing behavioural assertion per mutant: ReviewerBatteryKills (n1 by the two
`n1 manifest-at-rev` first-commit arms, n5 by `n5 label-targets-cne`, n11 by the `+2` live and
rev-path arms), CriticClaimR95 (`candidate-c1.txt`, failure counts 2/1/2) and MutTesterBattery95,
and the code reading of the diff (a single 67-line hunk inside `self_test()` that calls
`run_evaluate`/`kill_set_check` on built fixtures; no `__file__`, `inspect`, `dis`, `tokenize` or
`__code__` access — SentinelScopeR95 § safety).

Routed to round 96: name recompile-and-compare and code-object scans as refused shapes in the
reviewer checklist (a Q85 extension), and commit g2/g3 as control worlds in the next counter's
battery. A source-blind run cannot hide its own code objects from an in-process self-test, so these
shapes stay a review duty, not a counter guarantee.

## A2 — the rule-1 control is run-granular, not predicate-granular

CriticClaimR95 F2: f6 shows rule 1 at RUN granularity (the n11 run is RUN-ERROR, where `rc != 0`
would read KILLED), but under the round-94 rule f6 still reads UNMET because n1 and n5 survive, so
f6 does not flip the predicate between rule sets. A live, non-forged demonstration exists:
MutTesterBattery95 m11 (default/caller pin swapped) crashes with `TypeError` and no summary — RUN-ERROR
under v3, KILLED under the round-94 rule. The mined-mistake fix is "shown able to fail" at run
granularity by f6 and m11; a predicate-flipping crash world is routed to round 96.

## A3 — provenance and counter hygiene (non-blocking)

- CriticClaimR95 F1: round-94 MutTesterBattery94 recorded **four** survivors (N1, N4, N5, N11); the
  plan says three. N4 (the pin check moved after the probe loop) was recorded there as "probably an
  equivalence in practice"; MutTesterBattery95 re-ran it and it still survives (not observable in any
  fixture). Carried, not claimed.
- ReviewerCounterV3 F1/F3: an exception other than the counter's own `NotEvaluated` (a non-UTF-8
  instrument, a `SyntaxError` raised by `ast.parse` inside `code_decoy()` before the compile check)
  exits 1, not 2 — fail-closed (no false MET) but outside the stated exit ladder. F2: a timeout kills
  only the runner child. Routed to the next counter.
- MutTesterBattery95 m08 (`!=` relaxed to `<` in the target-set check) survives: the only wrong-target
  world is a missing-target world; no extra-target world exists. Routed to round 96 as a C1-family
  survivor.
