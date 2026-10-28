# Kb81K02Patterns — cross-round pattern map, round 81 w1

Seat: leaf executor, `Kb81K02Patterns`. Lane HEAD = base `b284223105f4d106f7e8f56ed4fd296c643cda0e` (`git rev-parse --short HEAD` → `b284223`). Read-only on the lane; no lane file, index or commit touched. No tool installed (none needed). No scratch clone created. Receipts: `.ufo/waves/round-81/build/Kb81K02Patterns/` (`integrity-base.json`, `independent-base.json`, empty `*.err` files). Every count below carries the command that produced it.

## 0. Headline findings

1. **The plan's base truth for the independent gate is wrong.** Plan § C1 says `verify_corpus_independent.py` exits 1 "on the same `commit_unresolvable` 2 plus `report_dead` 1". Measured at base: `report_dead` = 0 in the independent gate (`pointers.report_dead` = 0, `report_dead_detail` = []). Only the integrity gate reads 1. The M103 divergence (two gates, one token, two answers) is still live at base, and the r81 plan repairs only one of the two gates.
2. **Q76 as drafted is not a new class, and its `captured-by: none` is wrong.** Q40 (M53, `corpus/lessons/round-56.md`) already requires a final sweep of every seat-writable directory with recorded disposition; Q27 binds seat records to output; Q49 (M79) restates Q40 for `Report:` paths. What none of them covers is non-report output outside any seat's writable scope — which is exactly where `.ufo/wapes` sits. The enforceable fix is an extension of Q40's sweep to the lane's full untracked set, not a seat-behaviour rule.
3. **Three of the four r81 repair designs re-create a proven-failing pattern.** R1 (`## SHONEN` substring + ≥400 B) is a marker-distinction arm at a second site. R2 (manifest + committed receipt) is self-attested evidence unless its bytes are pinned outside the lane commit. E6's "reviewed pin" certifies bytes, not logic (r80 E05's pinned blob was killed on logic). None of these three controls is in the plan's W0–W9 list.
4. **C2's control list omits the two controls Q71 and Q74 require.** The plan's C2 controls are C0–C4 (base, sha mismatch, unupdated `used-by`, quote without snapshot, first-answer baseline). No independent mechanical generator (Q74) and no script-only world beside the headline (Q71) are named. Because the counter is form-level (`documented` = conjuncts over committed bytes that a script can write), a script-only world is the first thing a critic will build.
5. **Recurring classes over r76–r80:** shortcut-world-reaches-target (4 rounds: r77, r78, r79, r80), command-status/measurement error (r76, r80), stray/misrooted artifact (9 instances across r50–r80, each answered with a narrower Q row, never a mechanism), self-attested evidence (r79, r80, r81 designs).

## 1. Recurring mistake classes (r77–r80, with the earlier history that makes them recurring)

| class | instances (pointer) | criterion that captured it | what did not change |
|---|---|---|---|
| shortcut world reaches target | r77 C01: a cheap stub reaches C1 `6 of 6` (`.ufo/waves/round-77/w1/C01CritDoNothing.md`); r78 lesson "Predicate-reachability" (`corpus/lessons/round-78.md:11`); r79 in-file script-only world `1 of 6` vs independent C4 generator `6 of 6` (`corpus/lessons/round-79.md:18`); r80 W8–W10 `6 of 6` (`.ufo/waves/round-80/w1/Kb80C01C1.md`) | Q37 (M49/M50, r55: "the cheapest real-input shortcut"); Q71 (M135); Q74 (M79-1); Q75 (M80-4) | controls are still enumerated as expectations in the plan and run by the attack seat after drafting (see §4) |
| measurement: pipeline status captured instead of the command's exit | r76 base battery `cmd \| tail` (`corpus/lessons/round-77.md:20`, row "number-drift"); r80 M80-1 (`corpus/lessons/round-80.md:47`, receipt `.ufo/waves/round-80/receipts/m80-1-pipe-vs-direct.txt`: `pipe-rc=0` vs `direct-rc=1` on the same command) | Q50/Q65 and "count carries its command" (r77 row); M80-1 is `captured-by: none` | the same error recurred 4 rounds later; no check rejects a pipe in a receipt |
| measurement: awk range that matches its own start line | r80 M80-2 (`corpus/lessons/round-80.md:48`): the prescribed `awk '/^## Gate registry/,/^## /'` prints 17 B | none (new) | — |
| stale planned premise (base truth stated from a summary) | r81 plan independent `report_dead 1` (measured 0, §0.1); r80 plan named `google-gemini/gemini-cli@451a02ff` and `zed-industries/zed@cfb894a5` as the red pair — the measured red tokens were the bare `7bb48f21…` at `SOURCES.md:171-172` (`.ufo/waves/round-80/w1/Kb80K02Patterns.md` §0.1; `Kb80C01C1.md:66`) | none; Q-criteria require re-measurement (Q21, Q36) but the plan text is not checked against the measurement | the r80 K02 correction was not cited in the r81 plan (`grep -n -o "Kb80K02\|M102\|M103\|M45\|Q37\|Q40" plans/round-81.md` → no output) |
| stray / misrooted output | see §3 (9 instances) | Q27, Q40, Q49 | — |
| self-attested or marker-attested evidence | r79 in-file fixture; r80 marker classes (W8–W10); r81 R1 and R2 designs (§4) | Q75 (M80-4), Q74 | each round's repair is re-specified in the same grammar that was killed |

## 2. Repair designs already proven failing under attack

- **Existence-only report-pointer check (r79 E04 → r80 E04).** Killed by `Kb80C01C1.md` §W10: a seven-byte `marker` committed at the fleet report path reaches `guards 5 of 5; tip battery exit 0: 6 of 6` (`.ufo/waves/round-80/build/Kb80C01C1-canonical-fleet-marker-default.txt`). The r80 E04 patch has no content check (`grep -n "SHONEN\|400" .ufo/waves/round-80/build/Kb80E04DeadPointer.patch` → no output), so the fix is existence-only, as the kill said.
- **Marker-based external class (r80 E05).** Killed by W8 (real lane commit `56b0764e…` absent from lane and fleet, masked by a line marker) and W9 (lane-URL row with the same dead hash). `Kb80E05GrammarFix.md` §Residuals R1 names the spoofability and accepts it as "the L1's declared trade"; the W8/W9 controls were not that trade, they were a reachable 6/6.
- **r81 R1 as written (`verify_corpus_integrity.py`: `<rev>:<path>` resolves; resolved bytes contain `## SHONEN`, ≥400 B).** Predicted red, not yet run. A substring-plus-size test is a marker-distinction arm: a fabricated fleet file of 400+ bytes containing `## SHONEN` passes and reaches the target. The attack model of W10 (the attacker controls the fleet copy the battery reads, `--fleet` or the scratch fleet) defeats any check whose reference bytes are attacker-writable. A binding survives only if its reference lives in bytes the attacker's commit cannot reach, e.g. a pinned blob sha of the fleet report in an instrument pinned by the guard or in `freeze-shas.txt`. [INFERENCE: this is the design consequence of the W10 attack model; it has not been run.] Suggested control W12 (pre-freeze, scored on the frozen counter): a 400+ B fabricated file with a `## SHONEN` heading at the fleet report path, in a scratch fleet. Expected under R1 as written: `6 of 6` → R1 is killed.
- **r81 R2 as written (`verifiers/external-commits.json` + committed fetch/ls-remote receipt).** Predicted red, not yet run. The manifest and the receipt are both committed lane bytes; a seat can commit an absent lane commit, a manifest row, and a fabricated `*.fetch.json` with `HTTP 200` and the matching hash. The plan's kill list does not include this. Suggested control W11: that exact world. Expected under R2 as written: `6 of 6`. The fix that the attack model permits is the same as R1's: pin the manifest's sha256 and each referenced receipt's sha256 in the counter (or freeze-shas), so a new exemption is an instrument-pinned edit, not a data edit.
- **"Reviewed pin" (E6 `INSTRUMENT_PINS`).** The r80 E05 blob was published as an `INSTRUMENT_PINS` value by its own patch, with no independent review recorded (`Kb80E05GrammarFix.md` §Blobs), and its logic was then killed by W8–W10. A pin certifies that the bytes are the ones named, not that the logic is correct. The r81 plan pins "the two reviewed r81 instrument blobs … with seat reviews" but names no non-author reviewer. Recommend the freeze receipt name the reviewer or state that the pin is self-review.
- **r79 W1 patches.** The r79 integrity patch failed the frozen instrument-pin guard, the LOG-citation symlink world reached `1 of 6`→`3 of 6`, and the index/baseline patch left `report_dead` red (`corpus/lessons/round-79.md:7`). These are the repairs the r81 plan's W1/W2/W3 controls were written to reproduce; the r81 plan's W1 expectation is correct for the integrity gate only (independent `report_dead` = 0, §0.1).

## 3. Stray / misrooted output — is `.ufo/wapes` covered?

### 3.1 Recurrence (each with a recorded fix; none mechanical)

| round | instance | pointer | criterion added |
|---|---|---|---|
| r50 | M32 misroot sweep before last seat returned (`.ufo/waves/round-49/`) | `corpus/lessons/round-50.md:18` | none recorded in the lesson row |
| r51 | M34 cancelled-seat output untracked | `corpus/lessons/round-51.md:18` (per Q40 row) | Q40 precursor |
| r56 | M53 `cancelled-seat-output-untracked` | `corpus/lessons/round-56.md` § Mistakes (cited by Q40) | Q40 |
| r58 | R1 `ReviewBudgetMove.md` written to fleet root after the misroot sweep | `corpus/lessons/round-58-verifier-spotcheck.md:243-252` | Q49 precursor |
| r59 | M79 misrooted seat report and premature sweep | `corpus/lessons/round-59.md:41` | Q49 |
| r70 | M120 seat report misrooted into fleet repo | `corpus/lessons/round-70.md:279-283` | — |
| r75 | `kotoba-shokukin/.ufo/waves/round-75/w1/R75Facet48.md` found by fleet misroot sweep | `corpus/lessons/round-75.md:12` | Q49 cited |
| r76 | CD1 duplicate typo path committed (`6ce2724`) | `corpus/lessons/round-76-verifier-spotcheck.md:25,79` | — |
| r80 | R80-D2 `.ufo/wapes` | `corpus/lessons/round-80-verifier-spotcheck.md:13,66` | Q76 draft (this round) |

That is nine instances in nine rounds. Each recurrence added a narrower row (Q27 → Q40 → Q49 → Q76 draft) and none added a gate. The only mechanism I found is the orchestrator's warning `scripts/hyaku/inline.sh:172`: `[ -n "$(git -C "$cwd" status --porcelain)" ] && echo "WARN lane repo has uncommitted changes: …"`. It prints a warning and does not block close. [INFERENCE: whether it runs before or after the last seat's write was not checked.]

### 3.2 Who saw `.ufo/wapes` and what they recorded

Twelve r80 seat reports name `.ufo/wapes` (`grep -l "wapes" .ufo/waves/round-80/w1/*.md` → Kb80E02Symlink, Kb80E06CounterErratum, Kb80E15BaselineOrder, Kb80S02Log, Kb80S06Shonen, Kb80S08ReadmeRows, Kb80S10Province, Kb80S11GateQuotes, Kb80S15FreezeShas, Kb80S16CensusLog, Kb80S17ReceiptIndex, Kb80Y01Simplify). Each says "not mine, left in place". None removed it. Their descriptions disagree on its type:
- Kb80S08ReadmeRows (line 61) and Kb80S10Province (lines 142–143): "empty 4 KiB directory".
- Kb80S06Shonen (lines 124–126), Kb80S11GateQuotes (line 98), Kb80S17ReceiptIndex (line 43): "594-byte regular file".

Current measurement: `stat -c '%F %s %y' .ufo/wapes` → `regular file 594 2026-10-27 20:17:03`. The directory reports carry no timestamp, so the conflict cannot be resolved from the reports. The lesson for the class: the seats who called it a directory did not re-measure the type with `stat`/`file`, and the seats who saw a regular file did not state a timestamp. [INFERENCE: the discrepancy may be a changed object between observations; unverified.]

### 3.3 Is it covered by Q49 or Q22?

- **Q49** (M79): covers seat `Report:` paths and "the recorded final misroot sweep covers every seat-writable directory only after the last seat settles." `.ufo/wapes` is not a report, and `.ufo/` root is not in any seat's writable scope (the wave spec gives `.ufo/waves/round-80/` only), so the sweep as worded does not reach it. Not covered.
- **Q40** (M53): same sweep, same scope ("every seat-writable directory"), "any later report it finds". Not covered for non-report files outside the writable scope.
- **Q22** (M28): "absence and reconstruction facts plus all held evidence are preserved before any targeted cleanup." This covers the R3 disposition step: move the file to `dispositions/wapes.txt` and delete the root copy only after the content is committed. Covered as a procedure.
- **Q27**: binds seat records to output; a seat that is not accounted for cannot be the origin of an unrecorded file, but `.ufo/wapes`'s origin seat was never identified in any r80 report. Not covered.

**Verdict on the Q76 draft:** the class (stray probe output outside the wave dir) is real and not captured by Q40/Q49 for non-report files, so a row is warranted. But the draft as worded ("a seat's probe/debug output lands only inside the wave dir") is a seat-behaviour rule that no sweep can check, and its `captured-by: none` ignores Q40. The enforceable form is an extension of Q40's sweep: the final sweep covers the lane's full untracked set (`git -C <lane> status --porcelain`, every path must be a declared seat output or a recorded disposition), and the warning in `scripts/hyaku/inline.sh:172` becomes a close gate. Q49 duplicates Q40 for reports (M79 repeats M53/M34); whether to merge them is an L0 decision, not made here.

## 4. Controls the plan does not yet list (pre-freeze, Q37)

The r81 plan lists W0–W9 (C1) and C0–C4 (C2). Its receipts directory at the time I read it held only `census-before.txt` and `tipbattery-base-dot.txt` (`ls .ufo/waves/round-81/receipts/`), so the W-expectations are predictions, not measurements. Q37 requires receipts committed before data. Suggested additions, each scored on the frozen counter:

- **W11 (R2):** absent lane commit + `external-commits.json` row + fabricated `*.fetch.json` (HTTP 200, matching hash). Predicted `6 of 6` under R2 as written.
- **W12 (R1):** 400+ B fabricated file with `## SHONEN` at the fleet report path. Predicted `6 of 6` under R1 as written.
- **W13 (gate divergence):** a dead `<rev>:<path>` token that the integrity gate reads red and the independent gate reads green (base: `report_dead` integrity 1, independent 0). The battery is red when either gate is red, so this does not change the battery verdict, but it is a self-test arm M103 asks for and the plan does not have.
- **C2-Q71:** a script-only world writing the entry, the row and the copied snapshot (copy `S249.md`, take any ≤25-word quote containing `allowed-tools` from the text view). Predicted `1 of 1` on the frozen counter; the headline must then say "form-level; generator world = 1 of 1" and assign the depth judgement to a named non-author reviewer (Q71, Q74).
- **C2-Q74 generator:** an independent mechanical generator writing the complete proposed evidence shape from the committed snapshot, scored on the same counter.

## 5. Cap arithmetic premise (C1 § E6 (a))

The plan's bound "40 base-spent + measured added ≤ 140" has no measured base-spent term. At base, `verifiers/check_tip_battery.py:111` reads `LINE_CAP = 40`, which is the cap, not a spend. The r80 accounting (`Kb80E05GrammarFix.md` §Line accounting) measured added lines against `072048fa`, not against `b284223`. Recommend the freeze receipt measure base→b284223 numstat of the six instruments before data, as the plan already requires for the reviewed blobs, and state the base-spent term as measured.

## 6. Pattern-level recommendations to L1 (not edits)

1. Replace the independent-gate premise in § C1 base truths with the measured 0; add W13 (§4).
2. Re-specify R1 and R2 with pinned reference bytes (fleet report blob sha; manifest and receipt sha256 in the counter or freeze-shas); add W11 and W12 to the controls before freeze.
3. Frame Q76 as an extension of Q40's sweep to the full untracked set, not a seat-behaviour row; note the Q49/Q40 duplication for L0.
4. Add Q71 headline and Q74 generator controls to C2 before freeze; state C2's headline as form-level.
5. Cite Q37, Q40, Q49, Q75 and the r80 K02 §3 recommendations in the r81 plan; the plan currently cites none of them (`grep` above).
6. Measure the cap base-spent term (§5).

## 7. Limits

- I did not run the r81 controls (W0–W13, C2 controls); they are predictions, marked as such.
- I did not run `check_tip_battery.py`, the independent integrity/gate receipts of the `--repo <lane>` absolute form, or any scratch fleet. The base integrity and independent runs (§0.1) are the only counter executions in this seat.
- The `.ufo/wapes` type conflict (§3.2) was not resolved; the current `stat` output is the only measurement.
- Lines of `scripts/hyaku/inline.sh` were read, not executed.

## 8. Commands and exit codes (own runs, read-only, `--no-baseline`, outputs in build/Kb81K02Patterns/)

- `python3 -B verifiers/verify_corpus_integrity.py --repo /home/vgpnk/Projects/shokunin/kotoba-shokunin --no-baseline --json` → exit 1. Non-PASS rows: `corpus.index.unindexed` = 1 (`corpus/lessons/round-80-verifier-spotcheck.md`), `corpus.pointers.report_dead` = 1, `corpus.pointers.commit_unresolvable` = 2 (`corpus/SOURCES.md:171-172`); OBSERVE rows `tracked_files` = 155, `report_total` = 111, `commit_total` = 46.
- `python3 -B verifiers/verify_corpus_independent.py --repo /home/vgpnk/Projects/shokunin/kotoba-shokunin --json` → exit 1. Non-PASS rows: `corpus.index.unindexed` = 1, `corpus.pointers.commit_unresolvable` = 2; `pointers.report_dead` = 0; `report_total` = 111, `tracked_files` = 155.
- `stat -c '%F %s %y' .ufo/wapes` → `regular file 594 2026-10-27 20:17:03.654585389 -0300`.
- `grep -n -o "Kb80K02\|M102\|M103\|M45\|Q37\|Q40" plans/round-81.md` → no output.
- `grep -n "^| Q76 " corpus/QUALITY.md` → no row (Q76 is not yet defined; Q75 is the last row).

VERDICT: Plan's independent-gate base premise is wrong (report_dead 0 measured, not 1); Q76 is a real gap only as an extension of Q40's sweep to non-report untracked files (Q49/Q40 cover reports only); R1 and R2 as written re-create the marker and self-attested classes and need W11/W12 controls; C2 needs Q71/Q74 controls before freeze.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81K02Patterns.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81K02Patterns/integrity-base.json, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81K02Patterns/independent-base.json
