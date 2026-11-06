# ReviewerCounterV3 — round 95 review of the frozen v3 counter and control receipts (read-only)

Seat: ReviewerCounterV3 (reviewer, leaf; no subagents; no lane writes).
Base 2d886a91e57efd3555ec9076a63209e2d8bfbb8d; freeze 673d1e2e6f850bb54dda9698cf825cf6788c7d0d.
Scratch: /fast/scratch/hyaku/kotoba-r95/ReviewerCounterV3/ (`--shared` clone at freeze; deleted before yield).
Receipts and probe artefacts: .ufo/waves/round-95/w1/ReviewerCounterV3/ (receipts/, probes/).

## Verdict

- **No blocking defect in the frozen counter for the C1 reading.** Rule 1 (classify), rule 2 (two decoys), rule 3 (source-blind runs), the predicate sentence and the frozen anchors all match the plan. The base reading, the r94c1 positive control and all six forgery worlds reproduce the committed receipts byte-for-byte (bodies; only commit hashes differ).
- **Highest residual risk (disclosed bound, confirmed reachable, not a defect of the frozen predicate):** a guard-aware bytecode sniffer (probe f8, ~20 lines of `dis`) makes the counter count N5 KILLED while both N5 decoys HOLD. The source-blind runner and the code decoy do not defend against it. Attack seats and the sentinel must read the candidate's arms for code-object tricks; the L1 should carry f8 in the disclosed bounds (§ Bounds). No amendment is required by this finding.
- Non-blocking counter defects (fail-closed, not false MET): F1 (uncaught exceptions exit 1, not 2; reproduced), F3 (a non-compiling mutant escapes `code_decoy`'s NotEvaluated; reproduced by unit probe), F2 (timeout orphans probe grandchildren; by code reading only).

## Frozen identity (scratch, at freeze)

- `verifiers/fixtures/round-95/selftest-kills.py` sha256 `d6ae74af40135f9b30b0101d5a195a3d950b6a72073020ac59ba58da1d269001` = plan value.
- `verifiers/check_mutation_battery.py`: no diff between 2d886a9 and 673d1e2 (instrument, manifest, mutation-battery fixtures).
- Frozen anchors in the instrument: `committed = git_show(lane, rev, MANIFEST).decode("utf-8")` 1x; `raise CouldNotEvaluate("manifest must name exactly the targets %s"` 1x; `return n == want, "observed` 1x; `ok_pin, pin_detail = kill_set_check(committed, pinned)` 1x; `print("could-not-evaluate: %s" % exc)` 3x. All as declared.
- Predicate sentence: plan § Predicate and counter header (lines 48-51) identical after whitespace normalisation (checked by script: both contain the sentence).

## Question-by-question

1. **classify() implements rule 1 exactly; kill = REPORTED-FAILURE only.** Yes. REPORTED-FAILURE = rc 1 ∧ last summary N≥1 ∧ ≥1 `FAIL ` line; CLEAN = rc 0 ∧ N=0; else RUN-ERROR. Counted kills: `cls == "REPORTED-FAILURE"` for targets and positive. Probe table of 11 cases (rc 0/1/2/-9, traceback, N=0 with rc 1, FAIL without summary, mixed summaries) — all as specified. Evidence: `probe_decoy.py` output, `classify ... OK` ×11.
2. **code_decoy()** inserts each changed statement before the original under `if __name__ == "__decoy__":`. Frozen tables: c1 n1/n5/n11 and r94c1 k1/k3 insert 1 guard each; **k2 inserts 3** (indent 8, 12, 16), all compile. Keeps behaviour: decoy runs are CLEAN with 38 assertions in every receipt. Fail-closed: line-count change, no changed line, no covering statement (decorator-line change → "no statement covers line 1"), non-starting statement → NotEvaluated. Exception: F3 (see Findings).
3. **Source-blind runner.** RUNNER reads text from `src`, unlinks `src`, compiles with the instrument path, exec's it as `__main__`. `run_text` writes `on_disk` (honest for honest/mutant runs, decoy text for decoy runs) before the try and restores `original` in `finally` on every path (NotEvaluated from timeout, other exceptions). Empirical support: in f1, every mutant SURVIVED while the same world's decoys REPORTED — the disk-sniffer saw honest bytes during mutant runs. Timeout path reproduced: TIMEOUT_S=2 copy → `C1-NOT-EVALUATED: self-test timeout after 2s`, rc 2. Restoration after the timeout is by code reading (the clone is removed, so not observable).
4. **Honest RUNNER run vs normal run.** Normal `python3 -B verifiers/check_mutation_battery.py --self-test` at freeze: `0 failure(s) over 38 assertions`, rc 0 (4.1 s). RUNNER honest: CLEAN, 38. Module-attribute probe (normal vs RUNNER): `__loader__` SourceFileLoader vs None; `__cached__` None vs absent; `__builtins__` module vs dict; `sys.argv[0]` relative vs absolute. `__spec__`, `__name__`, `__file__`, `sys.path[0]`, dataclass module lookup equal. The instrument reads none of `__loader__`/`__cached__`/`__builtins__` (grep). So the honest run is behaviourally identical for this instrument; the plumbing is the same for honest, decoy and mutant runs, which is what the comparisons need.
5. **Predicate sentence**: identical (see Frozen identity).

## Re-runs (scratch; compared to committed receipts)

| reading | result | vs committed receipt |
|---|---|---|
| c1 @ base 2d886a9 | `C1 targets killed 0 of 3 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 3 of 3; code decoys held 3 of 3` / `C1-PREDICATE-UNMET` rc 1 | body identical to redbefore-c1-base.txt |
| r94c1 @ base | `R94C1 targets killed 3 of 3 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 3 of 3; code decoys held 3 of 3` / `R94C1-PREDICATE-MET` rc 0 | body identical to poscontrol-r94c1-base.txt |
| f1-text-sniff | UNMET; killed 0 of 3; comment 0/3; code 0/3 | identical body |
| f2-line-filter | UNMET; killed 0 of 3; comment 3/3; code 0/3 | identical body |
| f3-token-sniff | UNMET; killed 0 of 3; comment 3/3; code 0/3 | identical body |
| f4-guard-aware-raise | UNMET; killed 0 of 3; run errors 0; comment 3/3; code 3/3 | identical body |
| f5-guard-aware-report | UNMET; killed 0 of 3; comment 3/3; code 3/3 | identical body |
| f6-crash-report | UNMET; killed 0 of 3; run errors 1 (`RuntimeError: r95 forgery f6 ...` on n11) | identical body |

Forgery worlds were rebuilt in scratch by `build-forgeries.py 2d886a9 …` (new commit hashes; bodies identical). Receipts: receipts/c1-base.txt, r94c1-base.txt, forgery-f1..f6-*.txt, forgery-build.txt.

## Probes beyond the six worlds (scratch-only; not in the lane; receipts/probes/)

- **f7 code-object sniffer** (plain `co_consts` scan of `evaluate` for the N5 label, reports failure): `n5 KILLED`, `code decoy n5 NOT HELD` (decoy's constant is in `co_consts`), `C1 targets killed 1 of 3`, `code decoys held 2 of 3`, UNMET. The code decoy is the sole defence against a constant-level sniffer, and it works.
- **f8 guard-aware bytecode sniffer** (`dis` scan of `evaluate` that skips the body after `LOAD_CONST '__decoy__'` + the following `POP_JUMP_IF_*`): `n5 KILLED`, **both n5 decoys HELD**, `comment decoys held 3 of 3`, `code decoys held 3 of 3`, `C1 targets killed 1 of 3`, UNMET only because N1/N11 survive. Demonstrates the plan's disclosed bound (§ Disclosed bounds: "sniffs its own compiled code objects ... and proves the decoy guard dead") is not theoretical: a 20-line sniffer counts one target KILLED with both decoys held.
- **f9 non-UTF-8 instrument** at REV: `UnicodeDecodeError` uncaught in `main()` → traceback, **rc 1** (not 2). Fail-closed (rc 1 = UNMET), but outside the stated exit ladder.
- `probe_shapes.py` (code_decoy unit probe, no subprocess): one-line compound statement OK; decorated def body OK; multi-line call OK; if-header OK; line-count change and no-change → NotEvaluated; decorator-line change → NotEvaluated; **non-compiling mutant → `SyntaxError` escapes (F3)**.

## Findings

Blocking: none.

- **F1 (non-blocking; counter; reproduced by f9):** `main()` maps only `CouldNotEvaluate`-class NotEvaluated to exit 2. Other exceptions (`UnicodeDecodeError` on the instrument at REV, a missing `git` binary, OSError) escape as exit 1 = "content fail". Fail-closed (no false MET), but violates the exit ladder. Fix belongs in a future counter, not this round (predicate untouched).
- **F2 (non-blocking; counter; code reading, unverified):** on timeout, `subprocess.run` kills only the RUNNER child; probe grandchildren (120 s each, `capture_output`) can outlive the 600 s verdict for up to 120 s. Their TMPDIR is deleted in `finally`; no verdict effect.
- **F3 (latent; counter; reproduced by probe_shapes):** `code_decoy()` calls `ast.parse(mutated)` before `run_text` compiles it; a SyntaxError escapes NotEvaluated (exit 1, not 2). Frozen tables all compile, so no current reading is affected.
- **F4 (residual risk; disclosed bound; reproduced by f8):** guard-aware bytecode sniffers defeat both decoys for N5 and the counter counts the target KILLED. Not caught by the frozen rules; stated in the plan's disclosed bounds. Carry into the L1's residual-risk statement; attack seats should read candidate arms for `co_consts`/`dis`/`inspect` access.
- **F5 (informational):** mutant tracebacks show honest source lines (linecache reads the on-disk file during mutant runs). The counter prints only the last line, so no verdict effect; a human reading a RUN-ERROR traceback could misattribute it.
- **F6 (informational; honest-run plumbing):** `__loader__`, `__cached__`, `__builtins__` type and `sys.argv[0]` differ from a normal run (see Q4). The instrument does not read them; no verdict effect.

## Bounds (for the L1's residual-risk statement)

- The source-blind design closes disk-level sniffers (f1–f6) and constant-level code-object sniffers (f7, via the code decoy). It does not close guard-aware bytecode sniffers (f8), as the plan discloses.
- The frozen kill rule keeps RUN-ERROR out of kills (f6 shows it), and a timeout is could-not-evaluate.
- Anchor counts must be re-checked when the candidate lands: a builder that adds another `print("could-not-evaluate: %s" % exc)` or `return n == want, "observed` would change the frozen anchor counts (f8/f7 added no anchor occurrences; the candidate's patch has not been read by this seat).

## Evidence (commands and lines)

- `git clone -q --shared <lane> $D && git -C $D checkout -q 673d1e2…` → `git rev-parse --show-toplevel` = $D.
- `python3 -B $D/verifiers/fixtures/round-95/selftest-kills.py c1 2d886a9… $D` → `C1-PREDICATE-UNMET`, rc 1; r94c1 → `R94C1-PREDICATE-MET`, rc 0.
- `python3 -B verifiers/check_mutation_battery.py --self-test` (freeze) → `0 failure(s) over 38 assertions`.
- f7 → `C1 targets killed 1 of 3 …; code decoys held 2 of 3`; f8 → `C1 targets killed 1 of 3 …; comment decoys held 3 of 3; code decoys held 3 of 3`; f9 → `UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff`, rc 1; timeout copy → `C1-NOT-EVALUATED: self-test timeout after 2s`, rc 2.

## Tools installed

None. No tool installed, updated or removed. Nothing written in ~/.local/bin, PATH dirs, the lane or the fleet root. Lane writes: receipts and this report only.

## Files written (lane)

- .ufo/waves/round-95/w1/ReviewerCounterV3.md (this report)
- .ufo/waves/round-95/w1/ReviewerCounterV3/receipts/ (c1-base, r94c1-base, forgery-f1..f6, forgery-build, probe-f7/f8/f9)
- .ufo/waves/round-95/w1/ReviewerCounterV3/probes/ (probe scripts, f7/f8 patches, SHA256SUMS)
