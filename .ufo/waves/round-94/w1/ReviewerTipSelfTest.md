# ReviewerTipSelfTest — C2 patch review (round 94, r94-w1)

Verdict: **no blocking findings. C2 patch admitted on evidence.**
Reviewed: `.ufo/waves/round-94/w1/ExecTipSelfTest/ExecTipSelfTest.patch`, sha256
`726e15b9c617a6e690a46e6b2748428c283186223dd51568232346928e7983d7`. READY (`ExecTipSelfTest_READY`, 20:25)
names the same sha256; nothing moved between review and READY.
Candidate (my scratch clone): `aeb325039e1fcddadde5491f1594d619b68d2ba0` = freeze `edc731a` + that patch.

## Checklist (assignment)

- Parameterized keydrop arm covers all six BATTERY scripts, behavioural world each: **YES.**
  `arms` = `keydrop-0..5` (one world per BATTERY row, each dropping only that row's key) + `keyswap`.
  Each world is a fixture git world (`_make_world`/`_drive`); verdicts read rc and checker output only.
- Each assertion names the exact path: **YES.** Missing-key assertions carry the path in the label
  (`names the missing key <path>`) and in the detail (`FAIL guard instrument-pin: <path> has no INSTRUMENT_PINS key`).
  New assertion `names only that key` checks exactly one such line starting with the path.
- Production `run_guards()` unchanged: **YES.** The whole pre-self-test region is byte-identical to
  `edc731a` (`cmp` on sed-extracted regions); `run_guards` byte-identical.
- `INSTRUMENT_PINS` restored: **YES.** `INSTRUMENT_PINS = saved_pins` runs after every arm.
- FROZEN ANCHOR `        for path in scripts:` / `            if path not in INSTRUMENT_PINS:` occurs
  **exactly 1x** in the candidate, byte-identical to base.
- ANTI-SNIFFING: **behavioural.** No `__file__`/getsource/source-text read in the new arms;
  `key_lines` filters the checker's output, not its source.
- Only `verifiers/check_tip_battery.py` in the diff: **YES** (`13 insertions, 7 deletions`).

## Hand-applied mutants on the candidate (exact counter substitutions, instrument restored after)

- `p1-one-key-hardcode` → rc 1, **`20 failure(s) over 102`**: all four assertions fail in each of
  `keydrop-0..4`. Labels name the exact path, e.g.
  `FAIL pin keydrop-0 world FAIL names the missing key verifiers/check_gate_registry.py`,
  `...verifiers/check_assertion_floors.py`, `...verifiers/verify_skill_checklist.py`,
  `...verifiers/verify_corpus_integrity.py`, `...verifiers/verify_corpus_independent.py`.
  keydrop-5 and keyswap still pass (their missing key is the one the hardcode still checks).
- `p2-skip-first-key` → rc 1, **`4 failure(s) over 102`**: exactly the `keydrop-0` world
  (`verifiers/check_gate_registry.py`, the row `scripts[1:]` skips).
- Base (`edc731a`) for contrast: p1 and p2 both rc 0 `0 failure(s) over 80`, i.e. survive.

## Frozen counter c2 on candidate `aeb325039e1fcddadde5491f1594d619b68d2ba0`

Receipt: `counter-c2-reviewer.txt`.
`C2 targets killed 2 of 2; positive killed 1 of 1; honest rc 0; decoys held 2 of 2` → **`C2-PREDICATE-MET`, rc 0.**
- honest: `self-test: 0 failure(s) over 102 assertions`, rc 0
- p1 KILLED (rc 1), p2 KILLED (rc 1), positive p0 KILLED (rc 1)
- decoys p1 and p2 both rc 0 HELD (comment-only decoys do not trip the self-test)

## Round-93 `c2-pinkey.sh` on candidate

Receipt: `c2-pinkey-reviewer.txt`. **`C2-PREDICATE-MET`, rc 0.**
honest `guard instrument-pin PASS` and `guards 5 of 5`; keydrop names `verifiers/check_correction_sweep.py`
at `guards 4 of 5`; keyswap names the same key at `guards 4 of 5`.

## Time budget

Receipt: `timings-reviewer.txt`.
- base `edc731a` honest self-test: `0 failure(s) over 80`, wall **3.04 s**
- candidate honest self-test: `0 failure(s) over 102`, wall **4.76 s** (+1.72 s for five extra keydrop worlds)
- hand-mutant runs: p1 15.67 s, p2 19.80 s
- Budgets: the floors guard has **no tip-battery row** (see F1), so no floors self-test budget applies.
  The binding budget is the frozen counter's `TIMEOUT_S = 600` per self-test run (timeout → could-not-evaluate,
  never a kill). Headroom is about 30x. **Fits.**

## Findings

- **F1 (non-blocking, assignment premise corrected).** The assignment asked me to read
  `check_assertion_floors.py` for the tip-battery entry. None exists. `verifiers/floors-registry.json` registers
  19 instruments, none of them `check_tip_battery.py`, and `check_assertion_floors.py` never mentions the tip
  battery. So the floors guard neither times nor floors this self-test. Not a counter defect; the predicate is unaffected.
- **F2 (non-blocking).** Two of the four per-arm assertions label the world by arm index only (`pin keydrop-4 world
  exits 1`, `... tally reads guards 4 of 5`). The path-naming assertions carry the exact path, and each world directory
  (`guard-pin-keydrop-<n>`) maps 1:1 to the frozen BATTERY row. I saw no mis-attribution in any failure output.
- **F3 (non-blocking, process).** The builder's `c2-pinkey.txt` was a mid-run snapshot (truncated at
  `keydrop: INSTRUMENT_PINS keys 6`); the completed file reads `C2-PREDICATE-MET`. Wave-process note.
- **F4 (environmental, not predicate).** My honest c2-pinkey run read `tip battery exit 0: 2 of 6` at the
  candidate rev; the builder's read `3 of 6` at its rev about 25 min earlier. The count of carried reds moves with
  live fleet state. The c2-pinkey predicate reads only the guard lines and the `guards N of 5` tally, so it holds.

## Residual risk / verification gaps

- The anti-sniffing guard catches comment-reading sniffers only (the counter header's disclosed bound). I read the
  new arms: they observe rc and output of fixture worlds and never read checker source. That is not proof against an
  AST-aware sniffer.
- Hand-mutant runs used the counter's exact substitutions via Python string replacement, not the counter's own
  `mutate()`. The authoritative reading is the counter run above.
- I did not run the lane tip battery at the lane's `--rev`; that is the L1's landing gate.
- Round-92 `controls-run.sh` and round-93 `c1-killpin-rev.sh` were out of my assignment scope and were not run.

## Tooling

No installs. Used stdlib Python and bash only.
