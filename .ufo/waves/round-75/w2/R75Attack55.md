# R75Attack55 — independent attack on R75Facet55

## Scope and pinned bytes

Target: `.ufo/waves/round-75/w1/R75Facet55.md`. I independently reopened the cited D1 lines in `corpus/lessons/round-74-verifier-spotcheck.md:34-37`, plan lines `plans/round-74.md:13,172-174`, and `verifiers/check_seat_counts.py:12-24,59-89,92-102,111-131` at `65a5c7a663249e0522cc49e4a148424200d9ddfe` (`git rev-parse HEAD`). The checkout had six untracked paths under `.ufo/waves/round-75/`; these do not alter the cited committed bytes.

## Re-runs

At the pinned revision, I ran the instrument itself:

```
python3 -B verifiers/check_seat_counts.py --spec .ufo/waves/round-74/w1-spec.json --dir .ufo/waves/round-74/w1 --rev 65a5c7a663249e0522cc49e4a148424200d9ddfe
=> seat reports committed 34 of 34; missing 0: none; unmatched 0: none  (exit 0)

python3 -B verifiers/check_seat_counts.py --spec .ufo/waves/round-74/w2-spec.json --dir .ufo/waves/round-74/w2 --rev 65a5c7a663249e0522cc49e4a148424200d9ddfe
=> seat reports committed 0 of 33; missing 33; unmatched 0: none  (exit 1)
```

(The second output was truncated by the command interface after the missing-name list began; exit and `0 of 33` were visible.) An independent `git ls-tree -r --name-only <pinned-rev> -- .ufo/waves/round-{68..74}/{w2,falsify}` sweep returned exit 0 and zero `.md` entries in each round directory. This confirms the *report-presence* result, not the dispatch history.

## Verdicts

**Core narrow finding survives.** The lesson's stated 34 seats against a 64-seat floor and the absence of committed w2 reports are consistent with the pinned counter and source. F2 correctly warns that this counter measures committed report files, not spawned agents; it also correctly observes that `agentId: null` is not discriminating evidence if both run and abandoned registries share that shape.

**F1's central claim is overstated / not established by its proposed detector.** Its sweep counts `.md` records in `w2/` or `falsify/`; zero proves no such reports were committed at this revision. It cannot prove that a wave was or was not dispatched, nor classify a round as lacking a falsify wave. The report itself notes the distinction between declaration and dispatch, but then treats class B (no committed reports) as evidence about the wording “without a falsify wave.” A dispatched wave whose seats did not commit reports is a counterexample to that inference. The historical `0` outputs therefore do not independently falsify the quoted streak. F1's claim that class C alone yields “third” is a plausible interpretation, not a demonstrated unique class definition; the report has no evidence that the original wording intended “rounds since routing.” Verdict: **inconclusive on whether “third” is false**, though the carried-count concern is actionable as a measurement/provenance gap.

**F2 proposed mutant arm is non-vacuous only for one output field.** The described mutant copies a bare timestamp into the marker, while the claimed output is `verdict unchanged (spawned 0)`. That assertion tests only the spawned-count field; it does not test the candidate status classification `abandoned` versus `unknown`/`unmarked`. A detector that ignores marker bytes entirely and always prints `spawned 0` passes that mutant. Add an expected status for the bare-timestamp fixture (e.g. `unknown`, not `abandoned`) and assert it changes from arm (a); otherwise this mutant cannot support the status-control claim. This is a control-design weakness, not a counterexample to the observed abandoned marker text.

**F3 arithmetic holds as written.** The plan parenthetical sums to 14 (`3+2+2+4+2+1`), while its executor label says 16; this is visible at `plans/round-74.md:172`. The discrepancy does not falsify the separate committed 34/34 count.

**F4 is a presentation/scope issue, not a failed count.** The D1 sentence reports 34 against a policy floor; the counter independently gives 34/34 for wave 1 and 0/33 for declared wave 2. Calling the overall declared sum 34/67 is valid only if the abandoned wave's spec is included as declared scope, which should be labeled rather than silently interpreted as completed-wave accounting.

## Final attack result

Facet55 is **partly upheld**: its counter outputs, plan arithmetic observation, and caution about registry/marker evidence are supported. Its strongest assertion that the “third” streak is false is **not proved by the offered sweep** because the sweep observes committed reports, not dispatch. Its proposed bare-timestamp mutant is **insufficient for status classification** because the asserted unchanged output omits status. No lane source or artifacts were changed.