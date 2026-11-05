# ExecFloorsBump — r90-w1 carry-in floors half-bump completion

## Files changed (production, owned)
- `verifiers/floors-registry.json` — `"instrument_total": 18` -> `19` (ONLY change; registry sha256 after: `724b73d3bd992d1562a9cd4c76bddc7fb4f6057323368c5144f25262e37b344b`).
- `verifiers/check_assertion_floors.py` — sha256 after: `7120c7d6c8412bf6e61826f3940f40b83e2e2b26d58d2bcf7175c99a83cfbadb`. Exactly four hunks:
  1. `EXPECTED_INSTRUMENTS`: added `"freeze_gate": 30` (with a round-90 comment).
  2. `INSTRUMENTS`: added row `"freeze_gate": ("verifiers/check_freeze_gate.py", 30, r"(?m)^(\d+) failure\(s\) over (\d+) assertions$", 2, 1)` — regex, groups and floor copied to match the instrument's `0 failure(s) over N assertions` line; floor 30 copied from the registry row.
  3. F6 self-test arm: swap literal `'"instrument_total": 18'` -> `'"instrument_total": 19'`; F6 anchor-history comment extended (`round 90: 19 with freeze_gate`).
  4. Module docstring: `freeze_gate 30` added to the floored-instrument list + one round-90 registration note (BUMP-IN-STEP RULE satisfied: registry + both tables + docstring in one change).
  No other row changed: `git diff` shows only these hunks (verified hunk-by-hunk before running proofs).

## Evidence (all commands run at lane tip `git rev-parse master` = `6fa5bb6d4ceeb51f0455e512a52d8b75628f404c`)
- Self-test: `python3 -B verifiers/check_assertion_floors.py --self-test` -> `0 failure(s) over 165 assertions`, rc=0. Receipt: `.ufo/waves/round-90/receipts/floors-selftest.txt`.
- Live: same script bare -> 19/19 `PASS ...`, including `PASS freeze_gate observed=30 floor=30`, rc=0 (180.9 s wall). Receipt: `.ufo/waves/round-90/receipts/floors-live.txt` (records both attempts, see Finding 1).
- Regression (Q05, scratch only): `git archive HEAD` extracted to `/fast/scratch/hyaku/kotoba-r90/ExecFloorsBump/halfbump` (= guard bytes before the bump: both tables without freeze_gate, F6 literal 18; registry 19 entries with `instrument_total` 18). Bare run there reproduces BOTH base FAIL lines byte-for-byte vs `.ufo/waves/round-90/receipts/base-floors.txt`, rc=2:
  - `FAIL registry size drift: instrument_total=18 but 19 entries in verifiers/floors-registry.json`
  - `FAIL registry row vanish: freeze_gate (listed in verifiers/floors-registry.json, absent from both guard tables)`
  Receipt: `.ufo/waves/round-90/receipts/floors-regression.txt`.
- Handoff: `.ufo/waves/round-90/w1/FLOORS_READY` = guard sha256 `7120c7d6c8412bf6e61826f3940f40b83e2e2b26d58d2bcf7175c99a83cfbadb`.

## Findings
1. PRE-EXISTING child-cap drift (NOT caused by this bump; observed at the live walk): `verifiers/verify_harness_independent.py --self-test` now takes ~167 s standalone on this host (passes: `0 failure(s) over 123 assertions`). The guard's child-cap base `SELF_TEST_TIMEOUT_S = 120` scales only with load, so the bare live walk deterministically fails (exit 2, `self-test timed out`) whenever the 1-min loadavg < ~1.4 at that child's start. Attempt 1 hit exactly this (load 1.08 -> cap 129.8 s); attempt 2 under load 4.91 passed. The guard docstring's round-56 baseline measured this child at 53.8 s — fixture growth since then (~3x) outpaced the flat base. This is the round-56 class in reverse (idle host, not loaded host, produces the false red). Remedy (raise the base or re-baseline the child) is a guard-owner/L1 decision; NOT landed here (outside this seat's assigned change).
2. Registry drift counters behaved exactly as designed: the half-bump state reds on two independent arms (size drift + row vanish), and the completed bump clears both — the regression arm proves the discriminators still bite.
3. No tool installs were needed (stdlib + existing python3/git only); no pacman use.

## Risks
- Any integration gate that runs the bare live guard on an idle host will read the attempt-1-style rc=2 until Finding 1 is remedied. Receipts here record the exact cap arithmetic, so a re-run under load is reproducible.
- `floors_guard`'s own row floor stays 150 vs observed 165 (headroom 15) — untouched per assignment; no action needed this round.

## Bounds compliance
- Writes: the two owned production files, three `floors-*.txt` receipts, `w1/FLOORS_READY`, this report. No other lane writes; no git/jj writes anywhere (only read-only git: `rev-parse`, `diff`, `archive`); scratch was `/fast/scratch/hyaku/kotoba-r90/ExecFloorsBump` (removed before yield); TMPDIR pointed there for all guard runs; no /proc writes, no network, no secret reads.
