# RevW2SCORECARD — SCORECARD round-64 material, deletions audit, delta-0 honesty

Seat: `kotoba-r64.RevW2SCORECARD-2` (wave 2, falsify). Read-only outside this file; no git/jj writes; no installs.
Lane `kotoba-shokunin`, measured 2026-10-24. Commands run from the lane root unless stated; scratch under `/tmp/r64sc`, `/tmp/r64tip` (`c019919c` tree), `/tmp/r64base` (`078eec4` tree).

## Pin correction (material)

The SCORECARD round-64 annotations are **not** at the declared measured tip `c019919c`. `git diff --name-only 078eec4 c019919c` contains no `SCORECARD.md`; the block lands only in the measurements commit `b99fb79` (`git diff --numstat c019919c b99fb79 -- SCORECARD.md` → `3 1`). `b99fb79`'s parent is `c019919c` (no rewrite). Audit boundary used below: predicates at `c019919c`, prose at `b99fb79` where the annotation lives.

## Predicates — re-run at the measured tip (all HOLD)

| Check | Command | Result |
|---|---|---|
| C1 counter identity | `sha256sum verifiers/check_scoped_rules_v32.py` @ `c019919c` | `f8f69cada703c8d821690fe01539b433afb7e92e9cdf1752b3365745a7d1113d` — matches `C1-span-measure.txt` pinned sha |
| C1 frozen predicate | `python3 -B verifiers/check_scoped_rules_v32.py --self-test` @ `c019919c` | exit 0; `worlds reject 7 of 7; eligible rows pass 4 of 4` / `survivors closed 6 of 6` / `must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes` / `self-test: 0 failure(s) over 223 assertions` — four lines byte-identical to `plans/round-64.md:46-58` and the receipt |
| C1 before | v32 @ `078eec4` | sha `12d093a1cdbba4e0…` (= r63's recorded committed sha), `self-test: 0 failure(s) over 219 assertions`, exit 0 — annotation's "219 assertions" confirmed |
| C1 do-nothing control | `check_scoped_rules_v31.py --self-test` @ `c019919c` | `survivors closed 5 of 6`, `0 failure(s) over 201 assertions`, exit 0 — annotation confirmed |
| C2 conjunct 1 | `check_r64_routed_repairs.py --rev c019919c…` | `r63 routed defects closed 4 of 4`, exit 0 |
| C2 conjunct 2 | `check_r64_routed_repairs.py --rev 078eec4…` | `r63 routed defects closed 0 of 4`, exit 1, plus refusal line; matches `plans/round-64.md:102-115` verbatim |
| Axis values | `SCORECARD.md:28-29` @ `b99fb79` | `depth | 9`, `consistency (calibration sub-axis) | 10` — "held 9 / held 10" is the table's value |
| Q59 fail-demonstration survives its repair | `git show <rev>:corpus/QUALITY.md \| grep -c 'M-a/M-b/M-e/M-f/M-j'` | `35d44b4b`=0, `849a546e`=2, `078eec4`=2, `c019919c`=2, `b99fb79`=2 — the pipe repair did not falsify Q59's own "fix shown able to fail" count |
| Next-line evidence pointers | `f3c82574` / `b614e8b1` in `.ufo/waves/round-64/w1/RevC1Predicate.md`; M95 census `15 instances / 13 outside` at `LOG.md:2596`; `verifiers/floors-registry.json` has **0** `check_scoped_rules*` rows | Present/accurate — the Next-line debt is evidence-backed |

## F1 — HIGH — the round's only no-harm receipt is a FAIL at the measured tip, and the LOG bullet hides it

Evidence:

- `.ufo/waves/round-64/receipts/noharm-tip.txt` (committed `b99fb79`, header `tip c019919c…`): `FAIL corpus-idx tip leaves new corpus file(s) unindexed: corpus/knowledge/g7-span-pinning-round64.md corpus/lessons/round-64.md`; `FAIL check-ptr unresolved citation pointers grew (base=3 tip=4)` with `LOG.md:2602`/`LOG.md:2603` naming `.ufo/waves/round-64/receipts/C1-span-measure.txt` / `C2-r64-measure.txt`; `--- verdict --- no-harm FAILED: 2 arm(s) failed`; `noharm exit=1`.
- `LOG.md:2609` No-harm bullet reports only `gate registry at base 41 of 41, exit 0` — no tip verdict, no failing arms. `SCORECARD.md:375` claims `score held 9, delta 0` and `score held 10, delta 0` with no mention of a red gate.
- This repeats *verbatim* the defect the lane already recorded as round-62 spot-check defect 4 (`LOG.md:2573`: "The round-62 report's No-harm bullet says 'battery arms as printed' without naming the two interim reds"). Recurrence one-class-inside-the-round that writes Q60 is a calibration defect, not a formatting nit.

Why it is not repaired by the measurement commit: `README.md:114-115` @ `b99fb79` do index both new corpus files, and `git cat-file -e b99fb79:<receipt>` returns 0 for all three receipts (128 at `c019919c`) — so the two reds are plausibly cleared at `b99fb79`. But **no no-harm re-run is committed at any rev**: the only committed no-harm receipt in the round declares FAILED/exit 1. The round therefore carries no green no-harm evidence, and the annotation's delta-0 statement is unsupported on the gate axis it does not mention.

Required disposition: either commit a `noharm-tip.txt` re-run at the repair rev (PASS or the named reds), or append a LOG corrections line naming the two tip reds and their repairing revs, and amend the SCORECARD annotation (append-only correction, as done for the r63 stale-bytes receipt at `SCORECARD.md:375` tail).

## F2 — MEDIUM — LOG Receipts bullet cites a control file that does not exist at any rev

`LOG.md:2610` names `.ufo/waves/round-64/controls/noharm-base.txt` beside `C1-before.txt`, `C2-before.txt`. `git cat-file -e`:

```
c019919c .ufo/waves/round-64/controls/noharm-base.txt => 128
b99fb79  .ufo/waves/round-64/controls/noharm-base.txt => 128
```

The file is absent in both revisions; the only committed no-harm artifact is `receipts/noharm-tip.txt`. This is exactly the Q60 class the round added (`corpus/QUALITY.md` Q60: "an artifact cited with a revision must exist at that revision"), committed into `LOG.md` at `c019919c` — the round violates its own new rule inside the entry that claims the M95 closure (the `check-ptr` red in F1 is measured on this same entry). Fix: drop the path or commit the base column receipt.

## F3 — MEDIUM — deletion audit: clean except the two above; no unrecorded content deletions

`git diff --numstat 078eec4 c019919c`, non-zero deletion column — complete set (4 files, 32 deleted lines):

| File | +/− | Recorded where |
|---|---|---|
| `.ufo/waves/round-63/w2/MutW2SplitClauses.md` | 82/29 | `LOG.md:2601` Inherited-state bullet names 82+/29- and the `temporal mismatch` marker |
| `corpus/QUALITY.md` | 2/1 | Q59 malformed-row pipe repair (scope + fix cells) — `LOG.md:2608` ("Q59's malformed row is repaired (pipe count)") |
| `corpus/README.md` | 1/1 | 219→223 correction, self-describing in the new cell ("the stale `219` this index carried at round 63 is corrected here") |
| `corpus/knowledge/compound-clause-citation-round63.md` | 5/1 | freshness note appended, self-describing, naming 223 and the r64 knowledge entry |

No standing claim is falsified by a deletion: Q59's grep count still prints 2 at every rev ≥ `849a546e` (table above); the `219` occurrences that remain are scoped to historical/measured-at statements and the freshness note; the `Next:` line was replaced (`SCORECARD.md:371`), and its replacement carries evidence pointers that all resolve (table above). The five r63-annotation claims I spot-checked (counter sha, assertion count, `5 of 6` do-nothing, `0 of 5` base, axis mapping) are unchanged in the r64 window.

## F4 — LOW — annotation's kill-conjunct wording is broader than the frozen predicate

`SCORECARD.md:375` says "SM1–SM6 each exit 1 on the landed bytes with **arm-attributed FAIL lines**; SM4/SM6 via the pre-existing `eligible world` arms". `plans/round-64.md:310-316` (erratum E3.1) requires "each of SM1–SM6 … with **its own discriminating `check()` label** — an arm is credited only when its own `check()` label is the FAIL line", and then exempts SM4/SM6. The annotation's first clause reads as the stronger claim and is only reconciled by its own parenthetical. The receipt's SM4/SM6 FAIL lines are `FAIL eligible world: …`, which by E3.1 are credited by attribution, not as the arm's own label. Recommend the annotation carry E3.1's exact sentence ("credited by the R64-M9 attribution rule; SM4/SM6 are not new-arm pins"), since the block self-describes as verbatim.

## F5 — LOW (residual) — the kill conjunct has no committed runner

`SM1_branch_removed`/`SM4_page_check_dropped` appear only in prose/mutant records (`.ufo/waves/round-63/w2/MutW2V32.md`, `.ufo/waves/round-64/w1/RevC1Predicate.md`); no committed script applies the six mutants. I verified the landed sha and the four predicate lines at `c019919c`, but **did not re-run the six mutants**; the exit-1 assertions rest on the receipt alone. Given `RevC1Predicate` Q1's demonstrated dishonest counter that prints the lines with tautology checks, the kill conjunct's independence is the property most worth a re-runnable artifact. Not a falsification today; record as debt.

## F6 — LOW — "Before: SM1 surviving at exit 0" not independently re-run

I confirmed the base counter identity (`12d093a1…`), the `219` count and exit 0 at `078eec4`, and that `controls/C1-before.txt` (committed `c019919c`) carries the SM1-survives sentence. I did not rebuild the SM1 mutant at base. No contradiction found.

## Verdict recommendation (not an admission)

- Both frozen predicates: **HOLD** — wording verbatim, measured rev correct, both C2 conjuncts and the C1 four-line predicate reproduce at `c019919c`.
- `score held 9 / held 10, delta 0`: **defensible as axis scores** (table values unchanged; no capability row entered), but **the round is not no-harm-clean**: F1 (FAIL receipt + silent LOG bullet + no green re-run) is an unrecorded harm and a repeat of a recorded defect class; F2 is a fabricated-path citation. Disposition: hold the axes only with F1/F2 recorded as append-only corrections in LOG + SCORECARD and a re-run no-harm receipt at `b99fb79`; otherwise the delta-0 sentence is over-claimed for calibration.

## Verification gaps

- No `lsp` server would answer markdown/py config here (no server started; text/git evidence only, recorded as such).
- Wave-1 seat reports I relied on for pointer existence: `RevC1Predicate.md`, `ScoutQualityDebt.md` — read, not re-derived.
- Did not re-run `noharm-battery.sh` (would take the full gate set) nor the SM1–SM6 battery; both recorded above as receipt-based.
- Working tree is at `b99fb79` (HEAD); no working-tree files were read as evidence — all quotes come from `git show`.
