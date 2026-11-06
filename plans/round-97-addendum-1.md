# Round 97 — addendum 1 (integration disclosures; post-data, not an amendment)

Author: KotobaR97 (L1). Written after wave `r97-w1` settled (`.ufo/waves/round-97/r97-w1-results.json`,
11 seats) and after the landing commit `693be9c321c26078a2adbf32c220dfcd371cbe35`. Nothing here changes
a frozen predicate, counting command, kill rule, mutant table or target of `plans/round-97.md`; the v5
counter and the C2 runner are byte-identical to the instrument commit `94a10217` at the landing. These
are disclosures the frozen kill rule routes as findings ("a new forgery world a seat builds that reads
MET under v5 is a disclosed finding, not a rescue and not a narrowing").

## A1 — committed-reference forgery g10 reads MET under v5 (ExecForgeryV5 F1; CriticClaimR97 D1)

`.ufo/waves/round-97/w1/ExecForgeryV5/g10-head-compare.patch` compiles
`git show HEAD:verifiers/verify_dispatch_prompts.py` inside the counter's per-run clone and compares the
in-memory function code objects and four regex constants with it. Rule 5 (mirror) changes only
working-tree bytes; the clone's HEAD still holds the unmutated world commit, so the fake detects every
mutant in both blind and mirror runs and stays CLEAN on all three honest runs. It reads
`R96C1-PREDICATE-MET` under v5 with no behavioural arm. The plan's disclosed bounds named external
state and the guard-aware code sniffer g2b; this committed-reference class was not named. Named now as a
bound in `corpus/QUALITY.md` Q87. Measured fix direction (seat-local, not through the frozen counter): a
git-less per-run copy. Routed to round 98.

MutTesterCounterV5's g12 (compare on-disk bytes with `HEAD:`) is REFUSED under v5 — consistent with A1:
the byte compare sees the original text in the blind run; g10 compares the executing code objects.

## A2 — seeded-replay forgery g11 reads MET when `KOTOBA_R97_SEED` is set (ExecForgeryV5 F2; CriticClaimR97 D2)

`fresh_world()` hands the child `dict(os.environ, …)`, so the replay seed is visible to the measured
self-test. g11 replays the shuffle and is CLEAN exactly on the honest and decoy indices:
`R96C1-PREDICATE-MET` with seed `deadbeefdeadbeef`; unseeded the same world reads UNMET (honest 2 of 3).
The landing readings are unseeded (no `KOTOBA_R97_SEED` in the runner environment), so they are not
affected; the bound is disclosed and routed (minimal child environment).

## A3 — counter-rule mutation coverage (MutTesterCounterV5)

The committed C2 predicate kills 2 of 9 counter-rule mutants (V1, V8 via g3). V2/V3 show as tally
deviations only; V4 (HOME/XDG not reset), V5 (no shuffle), V6 (honest-any), V7 (uncaught
UnicodeDecodeError, exit ladder) and V9 (decoy RUN-ERROR held) survive. C2's frozen predicate is about
the three committed worlds, not rule-level adequacy; routed: committed controls that flip V4–V9.

## A4 — dispatch-checker survivors after C1 (MutTesterDispatchR97)

15 new mutants at base and landing candidate: KILLED 3, RUN-ERROR 1, SURVIVED 11 (m20, m22–m28, m31,
m34; m32 equivalent). The 27 C1 arms kill none of them: C1 is per-survivor, as frozen. Routed.

## A5 — other seat notes

- t10 arm records a passing assertion under uid 0 (ExecArmsR97 F3, ReviewerArmsR97 N1, CriticClaimR97
  D4): the landing host runs uid 1000, so the real arm executes; a root reading would be an honest red.
- t09 is an output-contract regression, not a false verdict (CriticClaimR97 D3): the plan's framing
  overstates one of the 13; the count and predicate are unchanged.
- ReviewerCounterV5 F1: uncaught non-NotEvaluated exceptions exit 1 with a traceback (latent,
  fail-closed: never MET/rc 0). Routed to the next counter (exit ladder).
- ConnectorOverlapR97: the `dispatch_prompts` assertion floor (56) is a minimum below the observed count
  (105 at landing), so arm deletions down to 56 read PASS; `verify_corpus_integrity.py` already red at
  the freeze (baseline stale). Round-98 candidate A.
- Integration source: the lane working tree holds S275/S276 as rejected rows (202 rows) beyond the
  scribe's two-row candidate (200 rows); intentional — both are same-round rejects with access record
  and flip in `corpus/lessons/round-97.md` § Gate (SentinelScopeR97 O-1, CriticClaimR97 D6).
