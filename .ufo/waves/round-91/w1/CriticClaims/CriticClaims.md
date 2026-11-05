# CriticClaims — round 91 w1: falsification of the frozen claims against the candidate

Seat: CriticClaims (critic, attack role; leaf). Writes only this file and `receipts/` under its own seat directory.
Candidate: base `9af1a7af2adf0ab07cfd53f92affc1ed8d992262` + the four builder patches
(ExecBatteryArms, ExecFloorsCap, ExecLadder, ScribeCorpus), committed in scratch clone
`/fast/scratch/hyaku/kotoba-r91/CriticClaims/cand` as `66fe55886134529b876b8cfa298e8870484b4d40`
(scratch identity; `rev-parse --show-toplevel` = the scratch clone). The four patches apply together on a clean base checkout (`git apply --check` OK for each, in order).
Receipts: `.ufo/waves/round-91/w1/CriticClaims/receipts/` (the candidate's own outputs; names listed per claim below).

## Proposed verdicts

| claim | proposed verdict | one-line basis |
|---|---|---|
| C1 (battery guard arms, depth) | **met** | predicate line byte-identical; N=25 ≥ 22; the three r90 mutants survive at base and are killed by named guard arms at the candidate |
| C2 leg A (floors cap + pin + freeze_gate coupling) | **met** | (a)(b)(d)(e) measured here; (c) met on builder receipts only (re-ran the cap-120 mutant) |
| C2 leg B (freeze-gate ladder) | **met for the re-derived instance; routed identity unprovable** | the non-UTF-8 defect is real (rc 1 → 2 after repair); the r90 pointer's identity with it is not established, and a second instance of the same ladder mismatch is unrepaired |
| C2 overall | **met, with the caveats in § C2 and § Findings** | both legs' after-states hold at the candidate |

The pre-data controls do not re-pass at the candidate (see § Controls): they are valid only at the freeze base, which is what they were declared for.

## C1 — depth (battery guard arms)

Predicate checks (plans/round-91.md § C1):

1. **Predicate text vs printed line.** The plan's sentence (soft-wrapped across lines 37–38 of `plans/round-91.md`), joined on whitespace, is byte-identical to the line the candidate prints: `mutation battery killed 17 of 17 kill-set; equivalents survived 6 of 6; disclosed survivors 0 of 0`. Evidence: `receipts/c1-predicate-candidate.txt`; the candidate run `python3 -B verifiers/check_mutation_battery.py --rev 66fe5588… --work <scratch>` exits 0 with `G1 revision identity PASS`, `G2 copy integrity PASS: 23 mutant copies and 3 revision copies`, `G3 registry presence PASS` and the exact line. N ≥ 22: `python3 -B verifiers/check_mutation_battery.py --self-test` → `0 failure(s) over 25 assertions`, rc 0 (base: 19; `receipts/c1-selftest-base.txt`).
2. **Class counts.** Manifest at the candidate: 17 kill / 6 equivalent / 0 survivor (`grep -cP '\tkill\t'` → 17).
3. **Kill channel is the guard arms, not a crash.** I replayed the three manifest recipes (`receipts/mutreplay.py`) against base bytes and candidate bytes, each replay applying the recipe's anchored edit, running the instrument's own `--self-test`, and restoring the file:
   - base bytes (`mb-m2`, `mb-m15`, `mb-m16` recipes): each `rc=0 0 failure(s) over 19 assertions` — the three guards are unobserved at base, as the plan states.
   - candidate bytes: `mb-m2` → `rc=1 FAIL G1 commit check: the refusal says the revision is not a commit`; `mb-m15` → `rc=1 FAIL G1 clean-tree guard: a dirtied scratch clone exits 2` and `… the refusal says the scratch clone is not clean at --rev`; `mb-m16` → `rc=1 FAIL G2 restore read-back: a tampered revision restore after a mutant exits 2` and `… names G2 copy integrity on the restore copy`.
   - Each failing line names the guard arm; no SyntaxError or crash is the kill channel.
4. **Shortcut: a committed manifest with three kill rows and no instrument change.** `mfw` (base + three appended kill rows, committed): `could-not-evaluate: manifest : target 'verifiers/check_mutation_battery.py' has no probe set`, rc 2 → UNMET. The shortcut is refused by a real world.
5. **Frozen control `ctl-c1-manifest-only` does not test the shortcut it names.** The script appends the rows to the working tree of a clone and reads `git rev-parse HEAD` (the base) as `--rev`; G1 reads committed bytes, so the appended rows are never read. Observed: `killed 14 of 14 kill-set`, `C1-PREDICATE-UNMET`, rc 1. The expectation (exit 1) holds, but for a reason unrelated to the shortcut. The control's own comment ("the instrument cannot evaluate (exit 2)") is false. Counter defect, not repaired here.

Other C1 findings:
- **Unbacked citation in the plan.** plans/round-91.md § C1 says the controls `ctl-c1-m2/mb-m15/mb-m16` "print `SURVIVED` (plans/round-91-controls.md)". The controls file declares only `ctl-c1-base`, `ctl-c1-manifest-only`, `ctl-c2-base`, `ctl-c2-capline-only`; grep finds the mutant names only in plans/round-91.md. The base SURVIVED evidence exists in the r90 receipts (`.ufo/waves/round-90/w1/MutTesterBattery/transcripts/harness-run.log` lines 9, 22, 23), and I re-observed it (above). The "no-work cannot reach 17" argument therefore rests on an r90 receipt, not on a frozen pre-data control.
- **Arm count differs from the plan text.** The plan says "three new self-test arms"; the patch adds three arms with six assertions (two per guard). N ≥ 22 is satisfied (25); the three guards are each red under their mutant.

## C2 — freshness (floors cap + pin; freeze-gate ladder)

**Leg A.**
- (a) `grep -n '^SELF_TEST_TIMEOUT_S = ' verifiers/check_assertion_floors.py` → `208:SELF_TEST_TIMEOUT_S = 360`. Met. (2 × ceil(160.2 s) on the 60 s grid = 360.)
- (b) `MEASURED_SELFTEST_S = 161` (line 214) and the arm `SELF_TEST_TIMEOUT_S >= 2 * MEASURED_SELFTEST_S` (line 1449) plus a second arm `MEASURED_SELFTEST_S == 161` (line 1451). Floors self-test at the candidate: `0 failure(s) over 176 assertions`, rc 0 (run in this session; the output was not saved as a receipt). Able-to-fail, my run: `cap120` mutant (`SELF_TEST_TIMEOUT_S = 120`) → `1 failure(s) over 176 assertions`, `FAIL: C2 leg A(b) cap >= 2 x measured: SELF_TEST_TIMEOUT_S=120 MEASURED_SELFTEST_S=161: got 120` (`receipts/floors-selftest-cap120-mutant.txt`). The plan's arm alone would not catch a lowered `MEASURED_SELFTEST_S`; the builder's `== 161` arm does (builder receipt `measured100`: red). Met.
- (c) over-cap sleeper → `timed out`, exit 2; sub-cap sleeper passes. Met on builder receipts (`ExecFloorsCap/mutants.txt`: `nocap` mutant → 16 failures incl. `C2 leg A(c) over-cap child: exit 2: got 0`). I did not re-run the nocap mutant.
- (d) `git rev-parse 66fe5588…:verifiers/check_assertion_floors.py` = `6f2c52fb2e09e817dff3360b97400a5d6e53626c`, which is the one entry added to `INSTRUMENT_PINS` (`check_tip_battery.py` line 141). Tip battery at the candidate (`receipts/tip-battery-candidate.txt`): every guard PASS including `instrument-pin`; gates `check_gate_registry` 0, `check_assertion_floors` 0, `check_correction_sweep` 0; `checklist`/`corpus_integrity`/`corpus_independent` still 1 (carried); final line `guards 5 of 5; tip battery exit 0: 3 of 6`. Met.
- (e) bare floors walk at the candidate: rc 0, `PASS floors_guard observed=176 floor=176`, `PASS freeze_gate observed=31 floor=31` (`receipts/floors-live-candidate.txt`). Met, but the plan wants `floors-live-landing.txt` at the landing revision — L1 must re-run at the landed rev.

**Leg B.**
- (a) Defect re-derived at base (`receipts/ladder-rung-base.txt`): a non-UTF-8 plan → `rc=1`, `UnicodeDecodeError` traceback. The docstring (line 22) assigns an unreadable plan to rung 2. Met as a re-derivation.
  - **Identity with the routed pointer is not established.** The r90 pointer ("probe-world exit-ladder inconsistency") is not named by ExecLadder's evidence (its own record marks the identification `[INFERENCE]`). A second, documented-by-docstring mismatch in the same ladder remains unrepaired and arguably fits the pointer better: a fail-closed simulator that exits 2 is reported by the gate as rc 1. Reproduced at the candidate: sim-w-healed with `receipts.txt` absent → sim `rc=2`; gate on `- control healed: bash …sim-w-healed.sh / expect: exit 0; stdout contains w_healed D5=PASS` → `REFUSED control healed … observed exit=2 … (exit mismatch: declared 0, observed 2 …)`, gate rc 1. The docstring (lines 47–50) states this is intended, so ExecLadder's "consistent with the docstring" classification is defensible. The identity question is the L1's call; I record it as contested, not as a falsification.
- (b) Repair in the candidate: `except (OSError, UnicodeError) as exc:`; `python3 -B verifiers/check_freeze_gate.py --self-test` → `0 failure(s) over 31 assertions`, rc 0 (base 30). Met — but only with the `freeze_gate` floor bump 30→31 (see § Findings F1).
- (c) Able-to-fail: revert the except line in a candidate copy → `FAIL arm plan-not-utf8 could-not-evaluate: unexpected UnicodeDecodeError(…)`, `1 failure(s) over 31 assertions`, rc 1 (reproduced in this session; output not saved as a receipt). Met.
- (d) `fg-m3-ladder-refusal-to-2` (`fail exit 1->2`) and `fg-m3b-ladder-eval-to-1` both `killed` in the candidate C1 predicate run. Met.

## Shortcut check (plan item 4)

| shortcut world | command | observed | result |
|---|---|---|---|
| raise child cap, no pin (base + `SELF_TEST_TIMEOUT_S = 360`) | `check_tip_battery.py --rev <that commit> --repo <that clone>` | `FAIL guard instrument-pin: … blob cb705e30… is not a pinned blob`; `floors` gate exit 1; `guards 4 of 5; tip battery exit 0: 2 of 6`; rc 1 (`receipts/tip-battery-capline-only-shortcut.txt`) | refused: C2 leg A(d) unmet |
| frozen control `ctl-c2-capline-only` on that same cap-only world | `bash verifiers/fixtures/round-91/ctl-c2-capline-only.sh` | `SELF_TEST_TIMEOUT_S=360`, `C2-PREDICATE-MET`, rc 0 | **control defect**: the control names the pin requirement in a comment but tests only `cap >= 320`; it reports MET for the shortcut it is declared to refuse |
| lower `MEASURED_SELFTEST_S` only (builder receipt, not re-run) | builder's `measured100` mutant | red at `MEASURED_SELFTEST_S == 161` | refused (the plan's own arm text would have admitted it) |
| ladder revert (leg B) | reverted except line | red at `plan-not-utf8` arm | refused |
| committed manifest rows, no instrument change (C1) | `mfw` clone | rc 2 `has no probe set` | refused |
| uncommitted appended manifest rows (C1, the frozen control's world) | `ctl-c1-manifest-only` | `killed 14 of 14`, UNMET | expectation holds for an unrelated reason (see C1 item 5) |
| arm added but unasserted (C1) | mutant replays | every guard mutant turns red with a named `FAIL` line counted in `25 assertions` | no unasserted arm found |

## Controls (pre-data, frozen)

Run through the candidate's patched freeze gate: `python3 -B verifiers/check_freeze_gate.py --plan plans/round-91-controls.md --timeout 1200` → **REFUSED on `ctl-c2-capline-only`** (declared `exit 1; stdout contains C2-PREDICATE-UNMET`, observed `exit=0 stdout=SELF_TEST_TIMEOUT_S=360 / C2-PREDICATE-MET`); the first three controls had passed before it (`receipts/` not copied: the gate printed only the refusal). At base the same gate reads `freeze gate: 4 control(s) held` (`.ufo/waves/round-91/receipts/freeze-gate-r91.txt`). The controls are therefore valid only at the freeze base. Any post-landing re-run of the controls plan refuses by construction, since `ctl-c2-capline-only` reads the working-tree cap. This is a frozen-declaration defect (the control bakes in a base-state expectation), recorded as a finding; not repaired (frozen).

## Corpus rows (plan item 5)

- New rows at the candidate's `corpus/SOURCES.md`: S262 (PIT basic concepts, tier A), S263 (Python subprocess, tier A), S264 (Wikipedia mutation testing, tier C, `rejected`).
- Quoted spans checked against the scout's receipt (`ScoutSources/quote-receipts.txt` + `ScoutSources.md`, both read): `Basic concepts`, `not all mutations will behave differently than the unmutated class. These mutants are referred to as equivalent mutations.`, `Last updated on Nov 05, 2026 (12:47 UTC)`, `If the timeout expires, the child process will be killed and waited for. The TimeoutExpire…`, `Mutation testing`, `the mutation score is the number of mutants killed / total number of mutants`, `Such mutants are called equivalent mutants`, `This page was last edited on 6 September 2026, at 19:05` — all IN the receipt. Scope: only double-quoted and curly-quoted spans were checked; unquoted paraphrase in the rows was not.
- Cell check: each new row has 12 `|` (11 inner cells), the header has 11 columns (`| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |`). No `|` inside a cell.
- Count: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → **190**, not the 189 the plan predicts. The plan's "at least one rejection row" and "187 → 189" are inconsistent: a rejection row in the same table is counted by the census. Recorded as a plan arithmetic defect.

## Findings (routed to L1; none repaired into frozen bytes)

- **F1 — frozen touch list incomplete (C2).** ExecLadder's repair requires `freeze_gate` 30→31 in `verifiers/floors-registry.json` and in `check_assertion_floors.py` (the `arm_floor_row` pins it to `len(ARMS)`). The plan's touch list says `floors-registry.json — floors_guard floor value only`. ExecFloorsCap made the bump under an L1 directive, which is outside its own ownership text ("floors_guard row ONLY"). The candidate's `freeze_gate` row reads 31 and the floors walk is green; the bump must be recorded in an addendum or the integration report.
- **F2 — frozen controls cannot re-pass at landing (see § Controls).** `ctl-c2-capline-only` is a base-state control; `ctl-c1-manifest-only` does not exercise its named shortcut.
- **F3 — plan citations/arithmetic.** SURVIVED-controls citation unbacked (§ C1); expected corpus count 189 vs actual 190 (§ Corpus rows).
- **F4 — leg B identity contested (§ C2 leg B (a)).** Two ladder mismatches are documented in the freeze gate: the unreadable-plan path (repaired) and the fail-closed-sim path (not repaired, docstring-documented). The routed pointer may name either.
- **F5 — same class, unrepaired instances in the ladder.** `--work` under a file → `NotADirectoryError` traceback, rc 1 (`receipts/ladder-rung-candidate.txt`, ExecLadder F4); duplicate control names → rc 0 (ExecLadder F1). Both are outside the routed pointer; the class is not closed.
- **F6 — corpus README.** `corpus/README.md` index rows for the three new corpus files are not landed (ScribeCorpus notes this; L1 must do it).
- **F7 — tip-battery sandbox context.** My candidate tip-battery run used `--repo <scratch clone>`; its `fleet root` line reads my scratch parent. The result is a candidate-shape reading; the landing reading must be re-measured by the L1 at the real fleet.

## Risks

- ExecLadder and ExecFloorsCap patches are coupled through the `freeze_gate` floor; applying either alone reds a self-test or the floors walk (builders' own receipts; ExecFloorsCap's `coupled` proof confirmed in its receipts).
- C2 leg B's identity with the routed pointer is a judgement; if the L1 rules that the sim path is the routed defect, leg B stays unmet and C2 cannot verify.
- Candidate measurements were taken in a scratch clone, not the lane. The L1 must re-run at the landed revision: the predicate line, `check_tip_battery.py --rev <landing>`, the bare floors walk, and the freeze-gate self-test.
- The 25 battery arms and 176 floors arms are measured on the candidate; the r91 self-test durations stand at ~3 s (battery) and ~7 s (floors cap-120 run) on this host, versus the 360 s cap; the leg A cap calibration itself was measured on 160.2 s (base receipt).

## Tooling

No installs. No pacman, no sysctl, no `/proc/sys` write, no PATH change. Git operations only in scratch clones (`clone --shared`, `checkout`, `commit` with the scratch identity), each after `rev-parse --show-toplevel` = the scratch path. No write in the lane or the fleet root. Scratch dir `/fast/scratch/hyaku/kotoba-r91/CriticClaims` removed at yield.
