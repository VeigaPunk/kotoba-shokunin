# Kb80M01Instruments — mutation probe

## Result

**INCONCLUSIVE — no mutant verdicts claimed.** The required pristine round-80 instrument stack was not available in the build directory when checked, and I did not run mutant counter worlds against a failing/unfrozen baseline. This avoids misreporting baseline failures as killed mutants.

## Evidence

- Authoritative plan read: `plans/round-80.md`; it requires a green amended tip battery and says the E5 amendment is limited to `LINE_CAP` 40→60 and two reviewed instrument pins.
- E04 patch applied in my isolated clone from `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`: `build/Kb80E04DeadPointer.patch`. Published E04 blob receipt names `051b8c5f8676cba5c8d6047c8c9f7fcb56cd8f9f` for `verifiers/verify_corpus_integrity.py`.
- The E04 gate self-test was run on the isolated applied patch: `python3 -B verifiers/verify_corpus_integrity.py --self-test` → exit 0. Receipt: `build/Kb80M01Instruments.pristine-integrity-selftest.txt`.
- The build-directory sweep for E05/E06 outputs (`E05`, `E06`, `GrammarFix`, `CounterErratum`, `check_tip_battery`) returned none at the time of the check. The available grammar artifacts were probes/receipts only, not the reviewed patches; the available amended-counter candidate was an unrelated probe script, not a frozen E5 counter.
- Consequently, no pristine amended counter with the two reviewed pins was available to run. No mutation was applied, so there are no mutant diffs, before/after mutant hashes, or restoration claims.

| Mutant requested | Detector expected | Receipt | Verdict |
|---|---|---|---|
| Drop E04 regression arm | E04 self-test and/or amended counter guard | none — no mutant applied | inconclusive |
| External-token classification flip | both corpus-gate self-tests and amended counter | none — reviewed E05 patch unavailable | inconclusive |
| Neutralize `<rev>:` fix | E04 self-test and amended counter | none — no mutant applied | inconclusive |
| Weaken regression-arm assertion | E04 self-test and amended counter | none — no mutant applied | inconclusive |
| Pad to 60 / 61 lines | amended counter cap self-test/guard | none — reviewed E5 counter unavailable | inconclusive |

The available grammar probe receipt is `build/Kb80L01Grammar-integrity-receipt.txt`; it includes synthetic probe findings and is not a pristine round-80 stack run, so it is not treated as mutation evidence.

Non-author audit notice received after this probe (not independently verified here): Kb80V03Instruments reports the base `commit_unresolvable` tokens are `corpus/SOURCES.md:171-172` pi-mono citations, while the plan-named Gemini/Zed examples are quoted context. The notice says a classifier limited to `owner/repo@<hex>` inside the backticked token would miss the actual blockers; the plan's explicit-third-repository line-context clause is therefore material. This does not change the probe verdict because the reviewed grammar patch and green baseline were unavailable.

Additional stack-runner notice received after this probe (not independently verified here): Kb80E10Battery reports the 21-line remaining instrument budget after E04, a published grammar candidate exceeding the 60-line cap, the real unresolvable citations at `corpus/SOURCES.md:171-172`, and a third-repository citation hazard in the C2 entry. These findings reinforce why a green pristine world must precede mutation scoring; they are not represented as my own detector runs.

VERDICT: INCONCLUSIVE; required reviewed E05/E06 bytes and a green pristine amended-counter world were unavailable, so no mutant was scored.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/w1/Kb80M01Instruments.md /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80M01Instruments.pristine-integrity-selftest.txt