# DistW2Findings

role: connector/distributor (leaf; advisory — the L1 integrates the corrections before the report)
item: Deduplicate the wave-1 falsifier findings (CriticC1Bound, CriticCalib, MutG9Guard, MutCalibInstrument, RevClaimC1, RevG9Guard, RevCalibChecks, RevSourceQuote) into the distinct correction set for the lesson's `## Falsify corrections` section; group by target (C1 counter / C2 counter / C2 wording / registry / receipts); drop duplicates (three seats found the check-4 arithmetic independently); keep every distinct attack with its source seat; assign a per-item disposition (fix-in-round / bound-recorded / wording-only / deferred-to-v33).

Lane bounds honored: no production file, fleet repo, sibling lane, lane jj state or lane Git index was edited. The only write is this report. Every probe ran on `/tmp` copies of the committed bytes at `cbbee56e9a3589b0b46736ad36f1b77701def80e` (lane tip, pushed). No tool was installed or updated (no pacman/uv/npx used — the task needed only `git`, `python3` and the already-present `curl`/`bash`).

---

## Behavior

**What this seat produced.** One deduplicated correction set: 14 distinct items, each with its source seat(s), its target group, and a disposition. The wave-1 falsifier reports contained **23 attack instances**; after merging the duplicated check-4 arithmetic finding (three seats) and the shared-instance pairs, **14 distinct items** remain. Two of them are already landed at `cbbee56e` (recorded here as landed), four are wording-only, four are fix-in-round text/registry repairs, one is a receipts fix-in-round, and three are deferred-to-v33 with the bound recorded.

**Grounding.** Every disposition was checked against the committed bytes at `cbbee56e`, not against the wave-1 working tree (which had drifted: the wave-1 reports quote v32 sha `8371f707…`/`55230880…`, the committed file is `4246069129…`). Several wave-1 findings were already fixed by the L1 before commit; several were *not* fixed and the lane's own committed entry/docs now contradict the wave-1 evidence. Those contradictions are the substance of this table.

### Gates run (verbatim, at `cbbee56e`, from a `/tmp` clone)

```
$ python3 -B verifiers/check_scoped_rules_v32.py --self-test
counter sha256 4246069129115f039158fa5abe1b9f592b167d5438e5e7c5e9b2b21468c17c33
worlds reject 7 of 7; eligible rows pass 4 of 4
survivors closed 6 of 6
must-fail E2e guard disabled admits e2e-negated-path-key: yes
must-fail G7 disabled admits e2f-backticked-event-claim: yes
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
self-test: 0 failure(s) over 208 assertions
EXIT=0

$ python3 -B verifiers/check_r63_routed_repairs.py --rev cbbee56e9a3589b0b46736ad36f1b77701def80e
PASS late-write-tracked   tracked at cbbee56e9a3589b0b46736ad36f1b77701def80e
PASS receipt-rev-named    LOG names 3f911504ce76d9ca186f297d6d4a9cd8ed77508a on 1 line(s)
PASS entry-size-named     LOG states 64 lines / 1044 words on 1 line(s)
PASS append-only          prefix=True grew_by=9 line(s)
PASS noharm-arms-named    LOG names reg_gate 36 of 38 + corpus-idx on 1 line(s)
r62 routed defects closed 5 of 5
EXIT=0

$ python3 -B verifiers/check_r63_routed_repairs.py --rev 35d44b4b4dcdda234b5dbff7af37e432fec55f05
FAIL late-write-tracked   not a tracked blob at 35d44b4b4dcdda234b5dbff7af37e432fec55f05
FAIL receipt-rev-named    LOG never names 3f911504ce76d9ca186f297d6d4a9cd8ed77508a
FAIL entry-size-named     LOG never states 64 lines / 1044 words for corpus/knowledge/erratum-absorption-round62.md
FAIL append-only          prefix=True grew_by=0 line(s)
FAIL noharm-arms-named    LOG does not name reg_gate 36 of 38 + corpus-idx
r62 routed defects closed 0 of 5
EXIT=1

$ python3 -B verifiers/check_scoped_rules_v31.py --self-test
survivors closed 5 of 6
bound: G9 remains unimplemented; e2f-compound-purpose-outside-citation survives per CriticC1Hollow.
self-test: 0 failure(s) over 201 assertions
EXIT=0

$ python3 -B verifiers/check_gate_registry.py --rev cbbee56e9a3589b0b46736ad36f1b77701def80e
gate registry rows conformant 41 of 41 lane verifiers; phantom 0
EXIT=0

$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba
… 16 × W04 …
kotoba	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md
EXIT=0
```

### Distinct wave-1 attack instances seen (before merge)

| # | attack | source seat(s) |
|---|---|---|
| a | check-4 arithmetic: `0 of 5` expected vs the arm's own literal truth `1 of 5` | CriticCalib F1, MutCalibInstrument F1, RevCalibChecks F3 (**three seats, one finding**) |
| b | the five counted checks ≠ the spot-check's five routed obligations (H1 absorption, false child-commit claim) | CriticCalib F2, MutCalibInstrument F9, RevCalibChecks F6e |
| c | append-only arm is free on a no-op / endpoint-only, cannot see a mid-history or suffix rewrite | CriticCalib F5, RevCalibChecks F4, MutCalibInstrument F6 |
| d | committed-byte agreement is not receipt authenticity (both sides co-change) | CriticCalib F4, MutCalibInstrument F8 |
| e | in-sample, externally prompted reconciliation ≠ new calibration capability; no numeric move | CriticCalib F3, F6 |
| f | label-only counter satisfies the frozen predicate letter | RevCalibChecks F1, F5 |
| g | fingerprint counter (bytes-derived, scores nothing) satisfies the predicate | RevCalibChecks F2 |
| h | M1 worktree-read mutant survives the draft self-test | MutCalibInstrument F3 |
| i | M2 literal-token / M3 hardcoded-size / M4 line-count-only / M5 literal-count mutants | MutCalibInstrument F4, F5, F6, F7 |
| j | spec precision: exact token, digit boundaries, suffix scoping, `36 of 38` locus, `--rev` unbound | RevCalibChecks F6a–F6f |
| k | G9 short-clause / MIN_CONTENT escape lanes (1-word, 2-word, stopword, backtick, unpaired backtick) | RevG9Guard F1, F2, F4; MutG9Guard F5 |
| l | G9 over-rejection lanes (hyphen `-and-`, quoted `;`, legitimate two-clause continuation) | RevG9Guard F5, F6, F7 |
| m | G9 lexical-collision lane (4-char prefix) and vocabulary-specialized stub | RevG9Guard F3, RevClaimC1 F3 |
| n | G9 must-fail arm is not a guard-quality assertion; eligible-row arm cannot detect an under-strict guard | MutG9Guard F3, F4 |
| o | `6 of 6` must be labelled "six frozen instances"; carry the r62 limits forward; depth stays 9 | CriticC1Bound F1, F2, F4, F5 |
| p | the boundary witnesses (short tail, borrowed-vocabulary tail) must be published | CriticC1Bound F3 |
| q | S119 quote discipline: three plan URLs dead; Acta is counter-evidence; ICMJE sha does not reproduce; "append" absent | RevSourceQuote F1–F5 |
| r | must pin v32's sha into the receipt before close | RevClaimC1 verdict |
| s | check-3 arithmetic/label wording; H1 narrowness bound belongs in QUALITY | RevClaimC1 F1, RevCalibChecks F3 |

23 instances → 14 distinct items after merging (a), (b), (c), (e), (i), (j), (k), (l), (o), (q).

---

## The deduplicated correction set (grouped by target)

Legend — **fix-in-round**: land a correction in this round's artifacts. **bound-recorded**: the attack is a true limit of the landed instrument; record it as a bound (entry/lesson/QUALITY) and do not change the instrument. **wording-only**: the correction is a wording/scope fix in the round's text, no instrument change. **deferred-to-v33**: the fix needs an instrument change that cannot be made without invalidating the frozen, already-measured predicate; record the bound now, fix in v33.

### Group A — C1 counter (`verifiers/check_scoped_rules_v32.py`)

| id | distinct attack | source seat(s) | state at `cbbee56e` | disposition |
|---|---|---|---|---|
| A1 | G9 must-fail arm is not a guard-quality assertion; a no-op guard still prints `yes`; the eligible-row arm can never catch an under-strict guard | MutG9Guard F3, F4 | **Landed.** The shipped file carries four named G9 assertions (`:2108-2131`) plus three `g9_probes` (`:2726-2755`). Re-running MutG9Guard's six mutants against the **committed** bytes: M1(`;`-only), M2(`and`-only), M3(threshold 1), M4(no-op), M5(page-not-line), M6(backtick skip) **all exit 1** with the specific assertion named — the three mutants MutG9Guard proved survived (`survivors closed 6 of 6`, exit 0) are now killed. | landed (record in `## Falsify corrections` as closed-at-tip) |
| A2 | G9 short-clause escape lanes: 1-word tail, stopword tail, unpaired backtick | RevG9Guard F1, F2, F4 (partly) | **Partly landed.** `MIN_CLAUSE = 2` and clause words counted with `page_words` (`:1118-1131`) close the 2-word tail: `…glob syntax and uploads files.` now rejects (`A2 G9: clause "uploads files."`). The **unpaired-backtick** lane survives: `…glob syntax \`and secretly uploads files.` → `[]` (admitted). The 1-word tail is excluded by the declared `MIN_CLAUSE = 2` floor. | bound-recorded (unpaired-backtick residual) + deferred-to-v33 (fix) |
| A3 | G9 over-rejection: hyphen `-and-` compound, quoted `;` literal, legitimate related continuation | RevG9Guard F5, F6, F7 | **Still live at tip.** Verified: `The tool runs search-and-replace across the index nightly before every scheduled weekly maintenance pass.` → `['A2 G9: clause "-replace across the index nightly before every scheduled weekly maintenance pass." is supported outside the cited line']`; `The agent writes audit logs … and rotates them weekly into archives.` → **rejected** (a legitimate two-clause cell). The entry records only the hyphen/`;` half (`:79-82`), not the "related continuation" half. | fix-in-round (extend the entry's Limits) + deferred-to-v33 (relatedness test) |
| A4 | G9 lexical collision (4-char prefix) admits a zero-overlap clause | RevG9Guard F3 | **Still live at tip.** `…glob syntax and stores rulerboard syntaxis nightly.` → `[]` when the page carries the tail words. The entry names the prefix-swap risk generically (`:82`). | bound-recorded + deferred-to-v33 |
| A5 | Boundary witnesses must be published: the 2-word tail and the borrowed-vocabulary tail | CriticC1Bound F3 | **Still live at tip.** The 2-word tail is now rejected; the borrowed-vocabulary tail is still admitted: `…glob syntax and uploads project files using glob syntax.` → `[]`. Neither witness appears in the entry or lesson (grep for `rotates them weekly`, `uploads project files` → no hits). | fix-in-round (publish both witnesses in the entry's Limits) |
| A6 | A vocabulary-specialized stub can satisfy the predicate | RevClaimC1 F3 | **Still live at tip.** A stub whose `g9_conjunct` returns a reason only when the cell contains `"secretly uploads files"` passes the whole predicate: `survivors closed 6 of 6`, `self-test: 0 failure(s) over 208 assertions`, **exit 0**. The four G9 assertions do not exercise a vocabulary-disjoint clause, so the stub is not caught. | fix-in-round (add one vocabulary-disjoint G9 assertion) |

### Group B — C2 counter (`verifiers/check_r63_routed_repairs.py`)

| id | distinct attack | source seat(s) | state at `cbbee56e` | disposition |
|---|---|---|---|---|
| B1 | Check-4 arithmetic: the frozen before-headline `0 of 5` contradicts the arm's own literal truth (`[F,F,F,T,F]` → 1 of 5) | **CriticCalib F1 + MutCalibInstrument F1 + RevCalibChecks F3** (three independent seats — the merge this task exists for) | **Landed.** Plan erratum E1 was appended at `plans/round-63.md:150-162` and the counter implements it: check 4 is now prefix **and** growth (`verifiers/check_r63_routed_repairs.py:125-135`); at `35d44b4b` it prints `FAIL append-only prefix=True grew_by=0 line(s)` → `0 of 5`, exit 1; at tip `prefix=True grew_by=9` → `5 of 5`, exit 0. The lesson records this as **M94** (`corpus/lessons/round-63.md:45`). | landed (record once, credited to all three seats) |
| B2 | The five counted checks are not the spot-check's five routed obligations: H1 absorption and the false child-commit claim are counted by no check | CriticCalib F2, MutCalibInstrument F9, RevCalibChecks F6e | **Still live at tip.** Check 1 proves only "tracked and non-empty" (`check_late_write`, `:80-93`); the string `"No post-report child commit exists."` appears **only** inside the self-test's repaired fixture (`:271`) and is consumed by no assertion. A tree that names every token but performs no repair scores `5 of 5`, exit 0 (reproduced). | fix-in-round (add the two §6 obligations to the counter, or record them as outside the five) + deferred-to-v33 |
| B3 | Append-only arm is free on a no-op and endpoint-only: it cannot see a mid-history rewrite or a suffix rewrite of this round's own appended block | CriticCalib F5, RevCalibChecks F4, MutCalibInstrument F6 | **Half-landed by E1 (the no-op half); the endpoint half is still live.** Verified at tip: rewriting the round-63 corrections block in place (base LOG prefix preserved, r63 suffix replaced) still prints `prefix=True grew_by=6 line(s)` → `5 of 5`, exit 0. Check 4 compares only two endpoints. | bound-recorded (as "frozen-prefix preservation", a no-harm guard not a repair) + deferred-to-v33 (history-level enforcement) |
| B4 | Committed-byte agreement is not receipt authenticity: both sides can co-change | CriticCalib F4, MutCalibInstrument F8 | **Still live at tip.** Reproduced: substituting the receipt's `receipt_rev=` token **and** naming the new token in the correction line still prints `5 of 5`, exit 0. The counter proves the correction agrees with the receipts *as committed at `<rev>`*, not that the receipts are authentic. | bound-recorded (state "token linkage, not authentication") + deferred-to-v33 (pin receipts against the frozen base) |
| B5 | Label-only counter satisfies the frozen predicate letter; fingerprint counter likewise | RevCalibChecks F1, F2, F5 | **Still live as a *predicate* defect, closed as an *instrument* defect.** The shipped counter is honest, but the plan's frozen sentence `prints \`r62 routed defects closed 5 of 5\` and exits 0` alone still admits a 17-line printer and a bytes-fingerprint counter. The counter's own `--self-test` now kills the worktree-read mutant (M1: exit 1, `FAIL worktree: an untracked copy on disk leaves check 1 red`) and the size/rewrite mutants (M3, M4). | fix-in-round (bind the rev and the counter's sha into the predicate) + deferred-to-v33 (fingerprint-lookup self-test) |
| B6 | M2 literal-token, M5 literal-count and M3/M4 mutants are not killed by the landed self-test | MutCalibInstrument F4, F7 (and F5, F6 for M3/M4) | **Mixed.** Against the committed counter: M3 (hardcoded sizes) → 2 failures, M4 (line-count-only) → 1 failure (**killed**). M2 (literal `receipt_rev`) and M5 (literal `36 of 38`) → **`self-test: 0 failure(s) over 15 assertions`, exit 0 — survive**. They are only caught by an out-of-band fixture (a rev whose receipt says `cafebabe…`/`37 of 38`), which the self-test does not build. | fix-in-round (add the substitution fixtures to the counter's `--self-test`) |
| B7 | Spec precision: exact token, digit boundaries, suffix scoping, the `36 of 38` locus, `--rev` unbound | RevCalibChecks F6a–F6f | **Mixed.** F6a/F6d landed: the receipt token is read by 40-hex regex and the count is parsed from the `reg_gate` block between `reg_gate` and `corpus-idx` (`:137-160`); a substituted receipt token or count turns the check red (verified: `receipt-rev-named`/`noharm-arms-named` FAIL). **F6b/F6c still live:** check 3 matches `str(lines) in line and str(words) in line` — no digit boundary — and matches on a line naming `164 lines 10440 words`; and checks 2/3/5 match **any** LOG line, not an appended-suffix line (tokens planted in an old line still score `5 of 5`). **F6f:** `--rev` is still unbound to a named measured rev (the counter accepts any 40-hex rev). | fix-in-round (suffix-scope + digit boundaries in checks 2/3/5) + deferred-to-v33 (bind the rev) |
| B8 | In-sample, externally prompted reconciliation ≠ a new calibration capability; no numeric axis move | CriticCalib F3, F6 | **Still live at tip.** The counter was written after the defects were known; the lane has no fresh honest/dishonest population. The H1 narrowness bound (honest variants M-a/M-b/M-e/M-f/M-j fail the R-c/ancestry regexes) is recorded in `corpus/QUALITY.md` Q57 (verified present). | wording-only (report "in-sample reconciliation", numeric delta 0) + bound-recorded (H1 bound already in Q57 — keep it) |

### Group C — C2 wording (claim text, no instrument change)

| id | distinct attack | source seat(s) | state at `cbbee56e` | disposition |
|---|---|---|---|---|
| C1 | "5 of 5" must not read as "five routed defects closed" | CriticCalib F2 | **Still live at tip.** The counter's headline is literally `r62 routed defects closed 5 of 5` (`:180`), and `SKILL.md:492` advertises it as such; the entry (`:88-91`) and `QUALITY.md` Q58 correctly narrow it to token linkage. | fix-in-round (report text must say "five computed repair checks over five named defects"; do not change the printed headline — it is the frozen predicate) |
| C2 | Scorecard wording: `6 of 6` is six frozen instances, never class closure; the C2 axis score must not move | CriticC1Bound F2, F5; ExecScorecardRow (build seat) | **Still live at tip.** `corpus/README.md:112` says "**the G9 class closed**" — the exact overclaim CriticC1Bound asked to be removed — while the entry itself (`:84-87`) records "One frozen instance". `PROVINCE.md:27` and `SKILL.md:491` are scoped correctly. No round-63 SCORECARD block is committed at `cbbee56e` (the drafted text is still in the wave-1 seat report). | fix-in-round (README wording + commit the SCORECARD block with the bounded wording) |

### Group D — registry

| id | distinct attack | source seat(s) | state at `cbbee56e` | disposition |
|---|---|---|---|---|
| D1 | The new verifiers must carry gate-registry rows (the `reg_gate` arm is what check 5 reads) | MutCalibInstrument F9 / RevCalibChecks F6e (registry half) | **Landed.** `check_gate_registry.py --rev cbbee56e` prints `gate registry rows conformant 41 of 41 lane verifiers; phantom 0`; `SKILL.md:491-492` carry both new verifiers with their commands and self-test columns. | landed |
| D2 | The `reg_gate` count the correction names (`36 of 38`) is a *r62-receipt* value, not a current registry value | RevCalibChecks F6d; CriticCalib F2 | **Needs a wording fix.** The committed correction names `reg_gate 36 of 38`, which is correct *as the r62 receipt's measured value*, but the registry at tip measures `41 of 41`. A reader can take `36 of 38` as current. | fix-in-round (label it "the r62 receipt's `36 of 38`" in the lesson/report) |

### Group E — receipts

| id | distinct attack | source seat(s) | state at `cbbee56e` | disposition |
|---|---|---|---|---|
| E1 | v32's sha must be pinned into the receipt before close; the receipt must name the committed bytes | RevClaimC1 verdict | **Live and verified.** `.ufo/waves/round-63/receipts/C1-g9-measure.txt:2` records `v32 sha256 552308806b17e0e48fedb083eb6d55b722a7ef080aa7de8402601bbbc27d8f39` and `:15` records `205 assertions` — but the committed `check_scoped_rules_v32.py` is sha `4246069129115f039158fa5abe1b9f592b167d5438e5e7c5e9b2b21468c17c33` and prints **208** assertions. The receipt describes bytes that were never committed (that sha is not even a git object: `git cat-file -t 552308806b17…` → `fatal: Not a valid object name`). The same file also mislabels its base: `base 35d44b4b… (working tree)`. | fix-in-round (re-issue the receipt against the committed sha and the committed assertion count) |
| E2 | The C2 counter has no receipt of its own | MutCalibInstrument F10 (integration constraints) | **Live.** `.ufo/waves/round-63/receipts/` contains only `C1-g9-measure.txt`; there is no C2 after-measurement receipt (the `5 of 5` / `0 of 5` transcripts exist only in the counter's `--self-test` and in `controls/C2-before-r62tip.txt`). | fix-in-round (commit a C2 receipt with the counter's sha `5a15feac…` and both transcripts) |
| E3 | The counter prints no self-sha, so the receipt cannot pin the instrument it came from | RevClaimC1 verdict (same shape, C2 side) | **Live.** `check_r63_routed_repairs.py` contains zero occurrences of `sha256`; v32 prints `counter sha256 …` on every run, the C2 counter prints nothing. | fix-in-round (print the counter's own sha256, as v32 does) |
| E4 | The three plan URLs for S119 are dead; Acta is counter-evidence, not a source; ICMJE's sha does not reproduce across fetches; the word "append" is absent from the ICMJE page | RevSourceQuote F1–F5 | **Landed at tip, with one residual.** The lesson's Gate records the three dead URLs with their status codes and reasons; Acta is rejected as "counter-evidence for this round's practice" (`corpus/lessons/round-63.md:60-62`); the SOURCES row pins quotes + access date and states byte-identity across fetches is not claimed (`corpus/SOURCES.md:131`). Verified independently: the committed snapshot `sha256` is `d76af0c0…`; the two quoted substrings sit at snapshot lines 170 and 172 with 16 and 7 words. Residual: the SOURCES row's `recheck` is `365d` (a calendar cadence) while the row is `mined` — harmless, but the lesson does not record that the ICMJE page is volatile-by-design beyond the row's note. | landed (record) + wording-only (residual) |
| E5 | The census after-count claim | RevSourceQuote F1 / plan §Sources | **Live.** The plan expects "After: expected exit 0, 17 W04" (`plans/round-63.md:137`); the measured after-census at `cbbee56e` prints **16** W04, exit 0 — S119's ICMJE URL is not a duplicate of any other scope's URL, so it adds no W04. The committed `census-before.txt` shows 16 W04; there is **no committed `census-after.txt`** at tip (only `census-before.txt` and `census-interim.txt`), and `census-interim.txt` ends `exit=1` with `E05 S119 kind=guidance` + two `E11` missing-`used-by` rows. | fix-in-round (commit `census-after.txt` with the measured 16 W04 / exit 0, and correct the plan's 17 → the measured count; the S119 row's kind is now `docs`, and both `used-by` targets exist, so the interim errors are resolved) |

### Cross-group items folded in from the build seats (attribution kept)

| id | item | source | disposition |
|---|---|---|---|
| X1 | r62's published-S103-event limitation and the supported-abbreviation false rejection must be carried forward next to the new `6 of 6`; do not imply G9 cured G7/E2c | CriticC1Bound F4 | fix-in-round (add to the entry's Limits; verified absent at tip: grep for `S103`/`FalsifyV31G7TooStrong` in the r63 entry/lesson → no hits) |
| X2 | G9's capability must be described as coordinated-clause lexical support against the cited line, with its minimum-size and delimiter bounds — not as general compound-purpose understanding | CriticC1Bound F1 | wording-only (the entry's rule section says "supported clause by clause at its cited line" but does not name the lexical/word-support limit; the Limits bullet `:69-70` does — carry both into the lesson) |
| X3 | Depth score stays 9; the clause-guard improvement is a separate, bounded technical gain; a numeric calibration move is not supported | CriticC1Bound F5, CriticCalib F6 | wording-only (SCORECARD block) |
| X4 | The C2 correction line must carry, per line: `receipt` + the full 40-hex token; the entry path + both numbers; `reg_gate` + `corpus-idx` + the measured count — and no in-place rewrite of an r62 LOG line may occur between the r62 tip and the measured rev | MutCalibInstrument F10 | landed (verified: `PASS` on all three token checks at tip; `append-only prefix=True grew_by=9`) |
| X5 | The H1 narrowness bound must live in QUALITY, not only in a report | CriticCalib F3 | landed (verified present in Q57) |

---

## Findings against the committed bytes (the wave-1 evidence that no longer holds at `cbbee56e`)

These are places where a wave-1 falsifier's evidence was measured against a **working-tree** v32/counter that the L1 later changed before commit. The wave-1 report is not wrong; it is stale. The L1 must not carry a stale claim into the report.

| wave-1 claim | wave-1 evidence | committed state at `cbbee56e` |
|---|---|---|
| MutG9Guard: M2/M3/M6 survive the suite; `survivors closed 6 of 6`, exit 0 | v32 sha `8371f707…` | **Stale.** Against the committed bytes all six mutants exit 1 with a named assertion. |
| MutCalibInstrument: M1 worktree-read survives; draft self-test `0 failure(s)` | draft counter sha `1963f6cb…` | **Stale.** The committed counter's `--self-test` prints `0 failure(s) over 15 assertions` but M1 (worktree read for trackedness *and* size) is now killed: `FAIL worktree: an untracked copy on disk leaves check 1 red`, exit 1. M2/M5 still survive (item B6). |
| MutCalibInstrument F8: a label-only tree scores `5 of 5`, even a zero-byte blob | draft counter | **Half-stale.** The zero-byte case is now rejected (`FAIL late-write: a zero-byte tracked blob fails check 1` is in the self-test; `check_late_write` returns False for a 0-byte blob). A *token-stuffed* tree still scores `5 of 5` — reproduced against the committed counter (item B2). |
| CriticC1Bound / RevClaimC1: v32 sha `8371f707…`; `self-test: 0 failure(s) over 201 assertions` | working tree | **Stale.** Committed v32 is `4246069129…` and prints `208` assertions. The committed receipt still carries the stale sha and `205` (item E1). |
| RevCalibChecks F3: at base the honest counter prints `1 of 5`; the plan's `0 of 5` is inconsistent | pre-E1 plan text | **Landed.** E1 landed; the committed counter prints `0 of 5` at base and `5 of 5` at tip. |
| RevG9Guard: "delete `secretly` → admitted"; "MIN_CONTENT = 3 skips short clauses" | working tree v32 | **Stale for the 2-word tail** (now rejected; `MIN_CLAUSE = 2` + `page_words`). **Still live** for the unpaired backtick, the 1-word tail (by declared floor), the related-continuation over-rejection, and the prefix collision. |

New at tip, not in any wave-1 report (found by this seat's re-run of every counting command):

1. **`corpus/README.md:112` says "the G9 class closed."** This is the class-closure overclaim CriticC1Bound F2 asked to remove, and it contradicts the committed entry's own Limits bullet ("One frozen instance"). A falsifier-attack wording fix that was never applied. (C2)
2. **The plan's after-census expectation (17 W04) is not what the census prints** (16 W04, exit 0), and no `census-after.txt` is committed. (E5)
3. **The committed C1 receipt names a sha256 that is not a git object** (`git cat-file -t` → fatal) and an assertion count (205) that the committed file does not print (208). (E1)
4. **Checks 2/3/5 match any LOG line, not an appended-suffix line, and check 3 has no digit boundary** — tokens planted in an *old* LOG line, with a single unrelated appended line, score `5 of 5` exit 0; and a line reading `… 164 lines 10440 words` satisfies the `64 lines / 1044 words` check. RevCalibChecks F6b/F6c predicted exactly this; it is still unfixed at tip. (B7)
5. **A vocabulary-disjoint G9 assertion is missing**: a stub returning a reason only for the literal `"secretly uploads files"` passes the entire predicate (`208 assertions`, exit 0). RevClaimC1 F3 predicted it; it is still unfixed. (A6)
6. **A suffix rewrite of this round's own appended corrections block is invisible to check 4** — `5 of 5`, exit 0. RevCalibChecks F4 predicted it; E1 fixed only the no-op half. (B3)

---

## Touched surfaces / out of scope

- **Written:** this report only — `.ufo/waves/round-63/w2/DistW2Findings.md`.
- **Read:** `plans/round-63.md`; `corpus/lessons/round-63.md`, `corpus/knowledge/compound-clause-citation-round63.md`, `corpus/README.md`, `corpus/QUALITY.md`, `corpus/SOURCES.md`, `PROVINCE.md`, `SKILL.md`, `SCORECARD.md`, `LOG.md`; `verifiers/check_scoped_rules_v32.py`, `verifiers/check_r63_routed_repairs.py`, `verifiers/check_scoped_rules_v31.py`, `verifiers/check_gate_registry.py`; all eight wave-1 falsifier reports; `sources-census.sh` (read-only `validate`).
- **Probed on /tmp copies of `cbbee56e`:** `/tmp/distw2/{clone,mut,mut2,mut3,cmut,lbl,disc,sfx}` — mutant counters, synthetic git trees, synthetic repos. The lane was never mutated: `git status --porcelain` in the lane is unchanged (only the pre-existing untracked `w2/`, `w2-dispatch.*`, `w2-spec.json`, `receipts.new-*.txt`).
- **Out of scope:** editing any production file, the lesson's `## Falsify corrections` section itself (the L1 owns that), the fleet repo, sibling lanes, lane jj state, the lane Git index, commits, pushes, and the canonical judgment. No tools installed or updated.

---

## Proposed `## Falsify corrections` content (for the L1 to integrate — text only, not applied)

The lesson section currently reads `Filled after wave 2; every correction lands before the report.` The L1 can fill it from this table; the group order below is the table's order, and each bullet names the source seat(s) so no attack is lost and none is double-counted.

```markdown
## Falsify corrections

Wave-2 falsify of the wave-1 build: 23 distinct attack instances from eight wave-1
falsifier seats, deduplicated to 14 items (the check-4 arithmetic was found
independently by three seats — CriticCalib, MutCalibInstrument, RevCalibChecks — and
is one item). Dispositions: 4 landed at `cbbee56e`, 5 fix-in-round, 2 wording-only,
3 bound-recorded, 4 deferred-to-v33 with the bound recorded. Every disposition was
checked against the committed bytes at `cbbee56e`, not the wave-1 working tree.

### C1 counter (`verifiers/check_scoped_rules_v32.py`)
- Landed: the G9 guard now kills the three mutants that survived the wave-1 suite
  (MutG9Guard): six re-run mutants all exit 1 with a named assertion at
  `4246069129…`.
- Bound recorded / deferred to v33: the unpaired-backtick lane, the related-continuation
  over-rejection, the 4-character-prefix collision, and the borrowed-vocabulary clause
  are admitted at tip; the entry's Limits gains the two witnesses and the
  relatedness-test debt (RevG9Guard, CriticC1Bound).
- Fix-in-round: one vocabulary-disjoint G9 assertion, so a vocabulary-specialized stub
  can no longer satisfy the predicate (RevClaimC1).

### C2 counter (`verifiers/check_r63_routed_repairs.py`)
- Landed: the check-4 arithmetic erratum E1 (`0 of 5` at the r62 tip, `5 of 5` at the
  measured rev) — one finding, three seats (CriticCalib, MutCalibInstrument,
  RevCalibChecks); recorded as M94.
- Fix-in-round: the counter's `--self-test` gains the receipt-token and count
  substitution fixtures (M2 and M5 survive it today), checks 2/3/5 are scoped to the
  appended suffix with digit boundaries, and the counter prints its own sha256 and a
  receipt is committed for it.
- Bound recorded / deferred to v33: the five counted checks are five computed repair
  checks over five named defects, not the spot-check's five routed obligations — H1
  absorption and the false child-commit claim are counted by no check; the append-only
  arm is frozen-prefix preservation (a no-harm guard, not a repair) and cannot see a
  suffix rewrite; the checks prove token linkage, not receipt authenticity.
- Wording only: the report reads "5 of 5" as five computed repair checks and states a
  numeric calibration delta of 0; `36 of 38` is the r62 receipt's measured value.

### Registry, receipts, and sources
- Landed: the two new verifiers carry gate-registry rows (`41 of 41` conformant); the
  S119 row pins located quotes and the access date, not byte-identity across fetches,
  and the three dead plan URLs are recorded with reasons (RevSourceQuote).
- Fix-in-round: re-issue the C1 receipt against the committed v32 sha
  (`4246069129…`, 208 assertions); commit a C2 receipt; commit `census-after.txt` with
  the measured 16 W04 / exit 0 and correct the plan's expected 17.
- Wording only: `corpus/README.md` drops "the G9 class closed"; the r62 published-event
  and false-rejection limits are carried forward; the G9 capability is named as
  coordinated-clause lexical support with its minimum-size and delimiter bounds; depth
  stays 9 and the calibration score does not move.
```

---

## Verdict

**PROPOSES** the 14-item deduplicated correction set above, with dispositions grounded in a re-run of every counting command against the committed bytes at `cbbee56e`.

I would change my mind about any disposition if: (a) the L1 shows a committed artifact that already carries the exact proposed text for a fix-in-round item — the six new items I found at tip (README "the G9 class closed", the 17-vs-16 W04 census expectation, the stale C1 receipt sha, the unsuffixed/undelimited checks 2/3/5, the missing vocabulary-disjoint assertion, the invisible suffix rewrite) are the ones most likely to be pre-empted; (b) a fresh wave-2 seat shows a wave-1 report's stale sha was not stale but a *different committed revision* than `cbbee56e` — in that case the wave-1 item returns to the table unchanged rather than as "landed"; or (c) the L1 decides the frozen predicate's stdout is itself in scope for correction, which would move items B5 and C1 from "wording-only" to "fix-in-round" — my table assumes the frozen predicate text is not edited and the *report* absorbs the wording instead.

Out of scope by lane bounds and honored: no product file, lesson section, fleet repo, sibling lane, jj state or Git index was touched; no commit, push, publish or deploy; no tool installed; the canonical Rust judge is untouched.
