# RevW2ScorecardWording

role: UFO-FSD reviewer (wave-2 falsify seat; advisory — a verdict emitted here is a recommendation, never an admission)
item: Attack the drafted SCORECARD row text in `.ufo/waves/round-63/w1/ExecScorecardRow.md` § Artifacts; verify (1) the `survivors closed 6 of 6` bound, (2) the C2 row's repair-check naming, measured rev, delta 0 and 10-vs-8.5 axis-mapping caution, (3) the Next: round 64 line's retained debts; propose exact final wording for both paragraphs with every claim traceable to a receipt at `cbbee56e9a3589b0b46736ad36f1b77701def80e`.

Axes: **depth** (every wording claim re-derived from committed bytes; every counting command re-run on revision-pinned copies). **Consistency** (draft vs frozen plan, CriticC1Bound, CriticCalib, and the committed SCORECARD table). No other axis assessed.

## The attack (commands + verbatim output)

Lane tip confirmed: `git rev-parse HEAD` → `cbbee56e9a3589b0b46736ad36f1b77701def80e` ("round-63: wave-1 build — G9 guard closes sixth frozen survivor (v32), r62 routed-repairs counter, S119 + entry, LOG corrections (defects 1-4), w1 evidence"). The draft file is byte-identical between working tree and cbbee56e (`git status --porcelain` on the path: empty). Verifiers are clean: working-tree sha256 of `check_scoped_rules_v32.py` = `4246069129115f039158fa5abe1b9f592b167d5438e5e7c5e9b2b21468c17c33`, `check_scoped_rules_v31.py` = `a07c2269ea077e4866827e3fae907c45aea7c960bbe5f56b21210a0cecea3858`, `check_r63_routed_repairs.py` = `5a15feac0358fd537ad3a54cad589fa5f41743971e02f9d3e742fa4c3528c6ec` — each equal to `git show cbbee56e:<path> | sha256sum`. No lane file, jj state, or git index was mutated; probes ran on `git archive`-extracted pinned copies (`/tmp/r63snap` @ cbbee56e, `/tmp/r62base` @ `35d44b4b4dcdda234b5dbff7af37e432fec55f05`).

1. C1 after — pinned copy @ cbbee56e: `python3 -B verifiers/check_scoped_rules_v32.py --self-test` (verbatim, abridged at the world lines):
   ```
   counter sha256 4246069129115f039158fa5abe1b9f592b167d5438e5e7c5e9b2b21468c17c33
   … world W1..W7 reject=True …
   worlds reject 7 of 7; eligible rows pass 4 of 4
   survivor e2c-wrong-supersedes-target: before accepted; after rejected
   survivor e2c-supersedes-with-fresh-fetch: before accepted; after rejected
   survivor e2e-negated-path-key: before accepted; after rejected
   survivor e2e-commented-equals-key: before accepted; after rejected
   survivor e2f-backticked-event-claim: before accepted; after rejected
   survivor e2f-compound-purpose-outside-citation: before accepted; after rejected
   survivors closed 6 of 6
   must-fail E2e guard disabled admits e2e-negated-path-key: yes
   must-fail G7 disabled admits e2f-backticked-event-claim: yes
   must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
   self-test: 0 failure(s) over 208 assertions
   EXIT=0
   ```
   The denominator is fixed in the committed source: `survivor_ids` is a literal six-tuple at `check_scoped_rules_v32.py:2657-2664`, load-asserted as "all six frozen survivor instances were loaded" at `:2672-2673`, and the headline at `:2687-2689` sums over exactly those ids.
2. C1 before — pinned copy @ `35d44b4b`: `python3 -B verifiers/check_scoped_rules_v31.py --self-test` → `survivors closed 5 of 6`; exactly two must-fail lines (E2e, G7); sixth survivor `before accepted; after accepted`; `bound: G9 remains unimplemented; e2f-compound-purpose-outside-citation survives per CriticC1Hollow.`; `self-test: 0 failure(s) over 201 assertions`; EXIT=0. Matches the committed control receipt `.ufo/waves/round-63/controls/C1-do-nothing-v31.txt` @ cbbee56e.
3. C2 before — lane, committed counter: `python3 -B verifiers/check_r63_routed_repairs.py --rev 35d44b4b4dcdda234b5dbff7af37e432fec55f05` → five FAIL lines (late-write-tracked, receipt-rev-named, entry-size-named, `append-only  prefix=True grew_by=0 line(s)`, noharm-arms-named), `r62 routed defects closed 0 of 5`, EXIT=1. Matches committed `.ufo/waves/round-63/controls/C2-before-r62tip.txt`. Note the append-only arm fails at base on E1's second conjunct (zero appended lines), so the landed `0 of 5` is truthful — CriticCalib finding 1's arithmetic objection is resolved by erratum E1 as landed.
4. C2 after — lane, committed counter: `python3 -B verifiers/check_r63_routed_repairs.py --rev cbbee56e9a3589b0b46736ad36f1b77701def80e` →
   ```
   PASS late-write-tracked   tracked at cbbee56e9a3589b0b46736ad36f1b77701def80e
   PASS receipt-rev-named    LOG names 3f911504ce76d9ca186f297d6d4a9cd8ed77508a on 1 line(s)
   PASS entry-size-named     LOG states 64 lines / 1044 words on 1 line(s)
   PASS append-only          prefix=True grew_by=9 line(s)
   PASS noharm-arms-named    LOG names reg_gate 36 of 38 + corpus-idx on 1 line(s)
   r62 routed defects closed 5 of 5
   EXIT=0
   ```
5. Draft-text anchors read at cbbee56e: `ExecScorecardRow.md:16` (both artifact paragraphs, read `:raw:16`); `SCORECARD.md` axes table (`depth 9`; `consistency (calibration sub-axis) | 10` owned; advisory `calibration 8.5`) and `:371` (current "Next: round 63" line); `LOG.md` @ cbbee56e ends with `### Round-62 corrections (appended in round 63; the r62 spot-check's §6 defects 1-4)` (defects 2a, 2b, 2c, 4, 1→Q57 fold, 3 re-probe); `receipts/C1-g9-measure.txt` @ cbbee56e. No round-63 LOG entry exists yet at cbbee56e (grep `^## 2026-10-23 — Round 6[23]` matches only Round 62 at line 2545) — the annotation and Next line are still unapplied proposals, so this wording review lands before integration.

## Findings (by severity)

- **F1 — HIGH (item clause 2 fails on all three sub-demands).** The drafted C2 segment (ExecScorecardRow.md:16, raw) reads: `*Calibration (consistency sub-axis; C2, score held 8.5; a band move waits on the non-author closure):* `--rev <rev>` … exit 0 @<measured-commit>.` (a) It never calls the five checks repair checks — CriticCalib finding 2's smallest correction demands exactly that framing so a five-check denominator is not read as five-defect closure. (b) It carries placeholders (`<rev>`, `<measured-commit>`) where the measured rev is now known and verified: `cbbee56e9a3589b0b46736ad36f1b77701def80e` (attack step 4). (c) It states neither delta 0 nor the 10-vs-8.5 axis-mapping caution (CriticCalib finding 6), and worse, `score held 8.5` silently interchanges the labels: the SCORECARD axes table holds the owned `consistency (calibration sub-axis)` row at **10** while the advisory `calibration` disposition is **8.5** (`SCORECARD.md` ownership note; round-47 line "Scores remain … calibration 8.5 (delta 0 each)"); `plans/round-63.md:5-9` calls "calibration/consistency (8.5)" the lowest owned axis. As drafted, an integrator cannot tell which number the row annotates — the exact confusion CriticCalib finding 6 prohibits.
- **F2 — HIGH (item clause 1 fails).** The drafted C1 sentence "after: v32 closes `6 of 6`" is unbounded: it names no denominator, so it is readable as semantic G9/E2f closure or saturation — precisely the reading CriticC1Bound finding 2 attacks ("label `6 of 6` **all six frozen survivor instances**, never all G9/E2f cases, all errata, or semantic saturation") and finding 4 (carry the r62 G7/E2c limits forward; the published S103 counterpart stayed accepted under v31 while the synthetic pair rejects — `.ufo/waves/round-62/w2/FalsifyE2fPair.md:84-104`). The committed counter itself pins the denominator (six-tuple, `v32:2657-2664`); the wording must say so.
- **F3 — LOW.** The drafted before-sentence "records `survivors closed 5 of 6` and only two must-fail arms" is accurate (attack step 2) but omits v31's `bound: G9 remains unimplemented` line — the line that shows the sixth instance was a *declared* bound, which is what makes the after-flip a bounded instance closure rather than a surprise. One clause fixes it; no arithmetic changes.
- **F4 — INFO (receipt drift, not a row-text defect).** The committed receipt `.ufo/waves/round-63/receipts/C1-g9-measure.txt` records v32 sha256 `552308806b17…` and `205 assertions`; the committed v32 blob at cbbee56e is `42460691…` with `208 assertions` (three G9 kill-arm probes added at `v32:2726-2730` after the receipt was taken, per MutG9Guard). The three predicate lines are identical in both, and my re-run of the committed blob (attack step 1) reproduces the full predicate, exit 0. The row must not cite the receipt's stale digest; flag the drift instead. Also, no dedicated committed receipt file exists for the C2 after-run at cbbee56e (the 5-of-5 transcript lives only in this and sibling wave-2 re-runs; the counter plus the LOG corrections block it reads are the committed evidence).
- **Clause 3 — PASS, no finding.** The drafted "Next: round 64" line keeps the W8 escape class and A2's F6 compound-purpose bound as survivor debt (F6 remains a class bound even though its frozen instance closed — CriticC1Bound finding 3's admitting tails stay inside the lexical contract), keeps the C2-bounded sentence matching `plans/round-63.md:119-120`, and keeps all three carried quality debts verbatim from the current `SCORECARD.md:371` line (SentBounds' pre-wave baseline receipt; helper-invocation receipts; the r62 wave-2 dispositions). Dropping the old line's "six survivor instances … once the closure upholds the frozen matrix" candidate is correct — it is resolved, at instance scope, by C1's row.

## Verdict on the committed bytes

**ATTACKS** the draft at cbbee56e as integration-ready text: clauses (1) and (2) of the assigned verification fail (F1, F2); clause (3) passes unchanged. The underlying measured facts are sound — every count the draft quotes reproduced exactly on the committed bytes (steps 1–4) — so this is a wording correction, not a measurement defect.

## Exact proposed final wording (both paragraphs)

Paragraph 1 — replacement for the Round-63 axis-annotations paragraph:

```markdown
**Round 63 axis annotations (append-only; verdicts belong to the non-author closure).** *Depth (C1, score held 9; verdict: measured):* `python3 -B verifiers/check_scoped_rules_v32.py --self-test` → `worlds reject 7 of 7; eligible rows pass 4 of 4` / `survivors closed 6 of 6` / `must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes`, exit 0 @ `cbbee56e9a3589b0b46736ad36f1b77701def80e` (committed v32 sha256 `42460691…`; re-run on the committed blob reproduces all three predicate lines). `survivors closed 6 of 6` counts exactly the counter's fixed tuple of all six frozen r62 survivor instances — `e2c-wrong-supersedes-target`, `e2c-supersedes-with-fresh-fetch`, `e2e-negated-path-key`, `e2e-commented-equals-key`, `e2f-backticked-event-claim`, `e2f-compound-purpose-outside-citation` — instance closure only, not semantic entailment, not exhaustive G9/E2f closure, and no saturation claim; the r62 G7/E2c limits remain (the published S103 counterpart stayed accepted under v31). Before: the v31 do-nothing control, `python3 -B verifiers/check_scoped_rules_v31.py --self-test`, records `survivors closed 5 of 6`, only two must-fail arms and `bound: G9 remains unimplemented` @ `35d44b4b4dcdda234b5dbff7af37e432fec55f05` (`.ufo/waves/round-63/controls/C1-do-nothing-v31.txt`); after: v32 closes all six frozen instances and the G9-disabled must-fail arm admits the frozen instance (the third predicate line; receipt `.ufo/waves/round-63/receipts/C1-g9-measure.txt` was taken pre-final integration — same predicate lines, 205 vs the committed counter's 208 assertions). *Consistency (calibration sub-axis; C2; row held 10, advisory calibration disposition 8.5 — the 10-vs-8.5 mapping between the table row, the plan's "lowest owned axis" naming and the older advisory disposition is unresolved authority work this row does not settle; numeric delta 0 under both readings; a band move waits on the non-author closure):* `python3 -B verifiers/check_r63_routed_repairs.py --rev 35d44b4b4dcdda234b5dbff7af37e432fec55f05` → `r62 routed defects closed 0 of 5`, exit 1 (`.ufo/waves/round-63/controls/C2-before-r62tip.txt`) → `--rev cbbee56e9a3589b0b46736ad36f1b77701def80e` → `r62 routed defects closed 5 of 5`, exit 0. The five are repair checks — `late-write-tracked`; `receipt-rev-named` (`3f911504ce76d9ca186f297d6d4a9cd8ed77508a`); `entry-size-named` (`64 lines / 1044 words`); `append-only` (frozen-LOG prefix preserved plus at least one appended correction line, per erratum E1: base `prefix=True grew_by=0` fails, tip `prefix=True grew_by=9` passes); `noharm-arms-named` (`reg_gate 36 of 38`, `corpus-idx`) — counted against the r62 spot-check's routed defects only; the spot-check's remaining routed obligations (the false post-report child-commit record, the H1→Q57 fold, the S049 re-probe) are dispositioned in the appended `### Round-62 corrections` LOG block, outside the counted five.
```

Paragraph 2 — the Next line, unchanged from the draft (it passes clause 3 as committed):

```markdown
**Next: round 64** — survivor debt: the W8 escape class and A2's F6 compound-purpose bound; C2 remains bounded to the five r62 spot-check defects, so a new self-assessment mismatch class remains outside its counter. Carry-forward quality debt until evidenced closed: SentBounds' pre-wave baseline receipt; helper-invocation receipts; the r62 wave-2 dispositions.
```

Traceability map (claim → receipt at cbbee56e): three predicate lines + exit 0 → step-1 re-run of committed blob `42460691…`; six ids → `v32:2657-2664`; v31 before lines → committed `controls/C1-do-nothing-v31.txt` + step-2; C2 before/after → committed `controls/C2-before-r62tip.txt` + step-4 re-run of committed counter `5a15feac…`; receipt token / sizes / no-harm tokens → `LOG.md` `### Round-62 corrections` block @ cbbee56e (consumed by the counter's checks 2, 3, 5); 10 vs 8.5 → SCORECARD axes table (`consistency (calibration sub-axis) | 10`; advisory `calibration 8.5`) and round-47 disposition line; W8/F6 + standing debts → `SCORECARD.md:371`; C2 bound → `plans/round-63.md:119-120`.

## Smallest safe corrections

1. Replace the draft's two artifact paragraphs with the wording above (fixes F1, F2, F3 in one edit; nothing else in ExecScorecardRow.md needs to change).
2. For the L1 at closure (not scorecard text): either re-record the C1 measure receipt against the committed v32 or append one line to it — `Receipt taken pre-final integration; committed v32 sha256 4246069129115f039158fa5abe1b9f592b167d5438e5e7c5e9b2b21468c17c33 re-run reproduces the three predicate lines, exit 0` — and consider committing the C2 after transcript as `.ufo/waves/round-63/receipts/C2-repairs-after.txt` (closes F4's gaps).

## Residual risk and verification gaps

- The digest drift in `C1-g9-measure.txt` (205 vs 208 assertions) is real; I verified the predicate lines are identical between the receipt's snapshot and the committed blob, but I did not diff the full 205-assertion subset — a reader comparing the two transcripts sees only the three added G9-probe lines (`v32:2726-2730`) plus their three assertions, per the in-source comment; not separately re-verified line-by-line.
- No committed receipt file yet shows the C2 after-run; my 5-of-5 transcript is a wave-2 re-run over committed bytes (counter and inputs all pinned), reproducible by anyone, but the L1 has not committed it — hence correction 2.
- The round-63 LOG entry and the SCORECARD application do not exist at cbbee56e; I reviewed proposed text only. Whether the L1 integrates this wording is outside my write scope (I wrote only this report; no production file, lane jj state, or git index touched).
- `grew_by=9` matches the nine-line corrections block; I did not independently recount the block's lines beyond the counter's own arithmetic and the visible block.
- No tools were installed or updated (none needed; pacman pause respected).
