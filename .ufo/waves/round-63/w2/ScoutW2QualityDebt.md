# ScoutW2QualityDebt

role: scout (leaf; no subagent dispatch)
item: standing quality debts on SCORECARD.md Next line at cbbee56e
revision judged: cbbee56e9a3589b0b46736ad36f1b77701def80e (committed bytes only)
installs: none

Axes used: exact Next-line bytes; debt identity; closed-with-pointer versus still-open, each with a search; carry-forward of only debts still open; no production edit.

## Pinned Next line

Command:

```
git show cbbee56e9a3589b0b46736ad36f1b77701def80e:SCORECARD.md | nl -ba | sed -n '371p'
```

Verbatim line 371:

```
**Next: round 63** — candidates: (1) depth: the six survivor instances (E2c ×2, E2e ×2, E2f G7) as live-row fixes — v3.1 closes five, the sixth (`e2f-compound-purpose-outside-citation`, G9) is a named residual — once the closure upholds the frozen matrix; the W8 escape class and A2's F6 compound-purpose bound stay the named residuals. (2) calibration: the v2 successor's first exercise on fresh routed defects (the G-a count against a new round's build subtree), not a rewrite of the frozen six. Standing debt: SentBounds' pre-wave baseline receipt; helper-invocation receipts; the r62 wave-2 dispositions.
```

The three debts are the clause after `Standing debt:`. `plans/round-63.md` does not name any of them. Round 63's logged work closes the r62 spot-check §6 defects 1-4 (`LOG.md:2568-2575`), a different list.

## (1) SentBounds' pre-wave baseline receipt — STILL OPEN

Origin: `.ufo/waves/round-61/wave/SentBounds.md:9-70`. Closure would be a committed pre-dispatch snapshot of fleet status, lane status, runtime-file bytes, sibling HEADs/statuses, and the jj op id (`SentBounds.md:68`; keys `fleet_status` at `:177` and `jj_op_head` at `:181`). Round 62's scout said not to claim it closed (`.ufo/waves/round-62/w1/ScoutR62Candidates.md:36`).

Command:

```
git grep -n -I -e 'fleet_status' -e 'jj_op_head' -e 'pre-wave baseline' cbbee56e9a3589b0b46736ad36f1b77701def80e -- '*.md' '*.json' '*.txt'
```

Output: 13 lines. Every hit is the unrun proposal inside `SentBounds.md`, or a later mention of the debt name. No captured receipt.

```
SentBounds.md:9    ### Medium — No pre-wave baseline makes status drift non-attributable
SentBounds.md:84   capture must run before dispatch
SentBounds.md:177  "fleet_status": git_status(FLEET),
SentBounds.md:181  "jj_op_head": ops[0]["id"],
SentBounds.md:207  fleet_delta = changed_paths(before["fleet_status"], ...)
SentBounds.md:209  FLEET_DRIFT print
SentBounds.md:241  if op["id"] == before["jj_op_head"]
ScoutR62Candidates.md:36   row 11, plan covers? no
ScoutR62Candidates.md:53   both SentBounds debts
FalsifyReportClaims.md:614 and :617   Next-line diffs that name the debt
ExecScorecardRow.md:20     carries the debt forward "until evidenced closed"
SCORECARD.md:371           the pinned Next line
```

`git cat-file -e` fails for `cbbee56e:.ufo/waves/round-61/bounds.md`, `round-62/bounds.md`, and `round-63/bounds.md`. Name scan of those trees finds `SentBounds.md`, `RevBaseline.md` (r61 counter re-run), and `ExecNoHarmBaseline.md` (C2 check-5 no-harm before-state). None is a frozen pre-dispatch baseline.

Verdict: still open. No pointer closes it.

## (2) helper-invocation receipts — STILL OPEN

Origin: `SentBounds.md:72-80`. Closure would be a precommitted receipt of each helper invocation: before/after jj op ids, helper path, hash, and argv.

Command:

```
git grep -n -I -e 'helper-invocation' -e 'helper invocation' cbbee56e9a3589b0b46736ad36f1b77701def80e -- SCORECARD.md LOG.md plans corpus/lessons .ufo/waves/round-61 .ufo/waves/round-62 .ufo/waves/round-63
```

Output: the phrase occurs only as the debt name, the r61 remediation sentence (`SentBounds.md:80`), and the r62 scout row. `LOG.md` has zero hits. `plans/round-63.md` has zero hits. Hits:

```
SentBounds.md:80                 record each helper invocation ... path/hash/argv
ScoutR62Candidates.md:5 and :53  debt named; plan has no hit
FalsifyReportClaims.md:614       r61 form, with the op-log qualifier
FalsifyReportClaims.md:617       r63 form, qualifier dropped, third debt added
FalsifyScorecard.md:145          qualifier drop called cosmetic
ExecScorecardRow.md:20           carried forward
SCORECARD.md:371                 pinned Next line
```

The qualifier drop is the only change since the r61 Next line. It does not add a receipt.

Fleet helper, read-only: `rg -n -e 'op log' -e 'argv' -e 'invocation receipt' /home/vgpnk/Projects/shokunin/scripts/hyaku/jj-lane.sh` exits 1 (no hits). The helper still does not write the ledger `SentBounds.md:76` said was absent.

Verdict: still open. No pointer closes it.

## (3) the r62 wave-2 dispositions — STILL OPEN (remainder only)

The phrase entered the Next line at `e6da78b` (`git log -S 'the r62 wave-2 dispositions' -- SCORECARD.md` returns that one commit), from `FalsifyReportClaims.md:25` ("record actual falsify dispositions"). It is still on the line at `e53b6e5` and `35d44b4`. `e53b6e5` rewrote candidate (1) from "six surviving errata classes" to "six survivor instances" and left this debt in place.

Closed subset — do not re-open:

- `corpus/lessons/round-62.md` ## Falsify corrections, F1-F17.
- `corpus/lessons/round-62-verifier-spotcheck.md:147-152`: "every correction landed before closure (F1–F17 ...)".
- `e53b6e5` applied FalsifyScorecard: `SCORECARD.md:369` has real seat counts (no `{W2_COUNT}` / `{TOTAL}`), report pointer `../.ufo/reports/round-62/kotoba.md`, before-state "2 of 5 classes with one committed arm-level reject".
- `FalsifyClaimC2.md:16-18`: the kill-arm gap on `de5e3471` is closed by the `604ae4fb` hardening.
- `FalsifyC2HonestH1.md` is committed and folded at `LOG.md:2574` (spot-check defect 1, not the whole wave).

Still false at `cbbee56e` (no fix and no explicit decline):

1. M93 hollow-control diagnostic. `corpus/lessons/round-62.md:25` still says `absorption-hollow.txt:5-8` "its diagnostic is a missing `check_scoped_rules.py` path, not the intended guard-direction rejection". The receipt says the opposite:

```
## variant H (hollow: never runs the guard-mutation direction)
$ python3 -B /tmp/r62hollow/hollow.py --self-test
absorption self-test failed: guard-mutation direction is missing for one or more errata
exit=1
```

Named by `FalsifyLesson.md:17-40` and `FalsifyReportClaims.md:51-55`. The false sentence is still the live M93 clause.

2. Before-control timestamp. `LOG.md:2549` still says `absorption-before.txt`, `2026-10-23T20:53:36Z`. Receipt line 2 is `date_utc=2026-10-23T20:57:43Z`. F14 fixed the 0-of-5 count and left the clock (`FalsifyReportClaims.md:63-67`).

3. Blanket no-harm / import sentence. `SCORECARD.md:36` still ends "No axis harmed: the frozen counter is byte-identical (`5a5adc94…`) and the successor self-test imports the frozen six unchanged." `noharm-tip.txt` at this revision still prints `FAIL  reg_gate`, `FAIL  corpus-idx`, and `Battery exit code: 124`. Round 63 corrected the fleet report's no-harm bullet (`LOG.md:2573`) and did not correct this SCORECARD sentence (`FalsifyReportClaims.md:9-13` and `:45-49`). F12 records a seat bound; it does not make line 36 true.

4. R-b "complete list". `LOG.md:2557` still says "complete list to date" and does not name `corpus/lessons/round-61-verifier-spotcheck.md` (`FalsifyReportClaims.md:81-85`). The substring `spot-check` is absent from that line. The file is in the tree (183 lines).

No-defect reports (`FalsifyC2D1Basis`, `FalsifyC2RevArg`, `FalsifyRegistryRows`, `FalsifySourcesRow`, `FalsifySubmissionSweep`, `FalsifyV31Worlds`) add nothing to the open list.

Verdict: still open. Pointer for the closed subset: `corpus/lessons/round-62.md` ## Falsify corrections and `round-62-verifier-spotcheck.md:147-152`. That pointer does not cover the four sentences above.

## Verified debt list (Next: round 64)

Carry all three. Drop none. Narrow (3) so F1-F17 are not redone. Survivor clauses (W8, F6) are outside this seat; do not treat `ExecScorecardRow.md:20` as verified here.

Exact proposed standing-debt text. Replace the `Standing debt:` clause on the new Next line. Do not rewrite the historical `Next: round 63` line.

```
Standing debt still open: (1) SentBounds' pre-wave baseline receipt — no committed pre-dispatch snapshot of fleet status, lane status, runtime bytes, sibling HEADs and the jj op id (the only fleet_status / jj_op_head bytes are the unrun proposal in .ufo/waves/round-61/wave/SentBounds.md); (2) helper-invocation receipts — no precommitted helper path/hash/argv and before/after op-id receipt (SentBounds.md:80); (3) the r62 wave-2 dispositions still false at cbbee56e — M93 (corpus/lessons/round-62.md:25) still says the hollow control's diagnostic is a missing check_scoped_rules.py path, while .ufo/waves/round-62/controls/absorption-hollow.txt:8 says "guard-mutation direction is missing for one or more errata"; LOG.md:2549 still dates that before-receipt 2026-10-23T20:53:36Z (line 2 of the file is 2026-10-23T20:57:43Z); SCORECARD.md:36 still says "No axis harmed" and "imports the frozen six unchanged" against noharm-tip.txt FAIL reg_gate, FAIL corpus-idx, Battery exit code: 124; LOG.md:2557 still calls R-b a complete list and omits corpus/lessons/round-61-verifier-spotcheck.md. Do not re-open F1-F17 or the e53b6e5 SCORECARD count/pointer/instance fixes or the committed FalsifyC2HonestH1 fold at LOG.md:2574.
```

Smallest safe corrections, append-only, for the L1 (not applied here):

- M93's "shown able to fail" clause becomes: `absorption-hollow.txt:8` records `absorption self-test failed: guard-mutation direction is missing for one or more errata`, exit 1. The missing-path sentence was never true of that receipt (`FalsifyLesson.md:27-33`).
- After `LOG.md:2549`, append: the receipt's own `date_utc` is `2026-10-23T20:57:43Z`; `20:53:36Z` does not appear in the file.
- After the round-62 axis annotation, append: `noharm-tip.txt` records `FAIL reg_gate`, `FAIL corpus-idx`, and `Battery exit code: 124`. Hash identity of `check_scoped_rules.py` is not a no-harm pass, and the v2 successor scores with its own evaluators; `check_repairs` is a comparison control.
- After `LOG.md:2557`, append: the list omitted `corpus/lessons/round-61-verifier-spotcheck.md`, added by the non-author closure, not by the lane.

Confidence: high on the searches and the four remaining sentences. Not claimed: a line-by-line re-score of every wave-2 report beyond the named residues and the F1-F17 ledger.
