# ExecLadder — C2 leg B (freeze-gate exit ladder): findings

Seat: ExecLadder (executor, build seat). Base: `9af1a7af2adf0ab07cfd53f92affc1ed8d992262`.
Scratch clone: `/fast/scratch/hyaku/kotoba-r91/ExecLadder/repo` (removed at yield).

## Verdict: REPAIRABLE — with a required coupling to the floors registry

- **Defect (re-derived, not from the routed pointer):** `verifiers/check_freeze_gate.py` base line 260,
  `except OSError as exc:` around `plan_path.read_text(encoding="utf-8")` (line 259). A non-UTF-8 plan raises
  `UnicodeDecodeError`, which escapes; CPython exits 1 (rung 1, "refused"). The docstring (line 22) assigns an
  unreadable plan file to rung 2. Observed at base: `rc=1`, traceback, empty stdout.
- **Repair (patch `.ufo/waves/round-91/w1/ExecLadder/ExecLadder.patch`, 1 file):** line 260 →
  `except (OSError, UnicodeError) as exc:`; one new self-test arm `arm plan-not-utf8 could-not-evaluate`
  (lines 365–369), listed in `ARMS`. Self-test 30 → 31 assertions.
- **Coupling (not in my patch):** `arm_floor_row` pins `verifiers/floors-registry.json` `freeze_gate.floor == len(ARMS)`.
  The shipped registry reads 30, so the patched self-test is `FAIL arm floors-row freeze_gate … floor 30 != … 31`,
  `1 failure(s) over 31 assertions`, rc=1. The floor row belongs to ExecFloorsCap (floors_guard row only), so I did
  not edit it. The landing must bump `freeze_gate` 30 → 31 in `floors-registry.json` (line 26) and in
  `check_assertion_floors.py` (line 200 `"freeze_gate": 30` and line 280 `("verifiers/check_freeze_gate.py", 30, …`).
  With that bump (scratch only) the self-test reads `0 failure(s) over 31 assertions`, exit 0.

## Evidence (observed)

- Rung table, base and patched: `.ufo/waves/round-91/w1/ExecLadder/rung-probe-base.txt` and `rung-probe-patched.txt`
  (script `rung-probe.sh`). Only the not-UTF-8 plan changes rung (1 → 2); every other path is identical.
- Able-to-fail: revert world (line 260 restored) → `FAIL arm plan-not-utf8 could-not-evaluate: unexpected
  UnicodeDecodeError(…)`, `1 failure(s) over 31 assertions`, rc=1. Receipt `able-to-fail.txt` (1).
- Patched gate: `0 failure(s) over 31 assertions`, rc=0 (apply-check on a fresh clone at the base:
  `APPLY-CHECK-OK`). Receipt `selftest-patched-scratch-floor31.txt`.
- Battery anchors: the eight `fg-m1, fg-m1b, fg-m2, fg-m2b, fg-m3, fg-m3b, fg-m4, fg-x1` rows, each anchor
  `re.findall` count = 1 on the patched bytes. No anchor covers a touched line. Manifest not edited.

## Findings (routed to L1; none repaired)

- **F1 duplicate control names:** two `control same` entries both run and the plan reads
  `freeze gate: 2 control(s) held`, rc 0. Addendum A2.4 claims "the docstring is corrected at the freeze commit";
  `check_freeze_gate.py` contains no duplicate-name sentence at all. Doc-truth claim not realised; no arm pins it.
- **F2 declared 127:** a control declaring `expect: exit 127` is never compared (rc 126/127 is read as
  could-not-evaluate first). Consistent with the docstring; a bound.
- **F3 signal kill:** `kill -9 $$` refuses (rung 1) with `observed exit=-9`. Arguably could-not-evaluate; judgement.
- **F4 work root under a file:** `--work <file>/sub` raises `NotADirectoryError` uncaught from `os.makedirs`
  (`run_control`, line 219): rc 1, traceback. Not named in the ladder. A second repair would widen the change
  beyond the routed pointer; recorded for round 92.
- **F5 BOM:** a plan with a UTF-8 BOM before `## Controls` reads rung 3. Consistent with the grammar.
- **Routed pointer:** `.ufo/reports/round-90/kotoba.md:113`, `ReviewerRepairs/review.md`, and `ReviewerRepairs.md`
  do not name the rung. The identification of this defect with the routed phrase is [INFERENCE]. If the L1 reads
  "probe world" as the battery's `fg-*` probes only, leg B narrows to `unprovable` per plan leg B(a).

## Files

- Patch: `.ufo/waves/round-91/w1/ExecLadder/ExecLadder.patch` (1 file: `verifiers/check_freeze_gate.py`).
- Ladder record: `.ufo/waves/round-91/w1/ExecLadder/ladder-defect.md`. Plan path `receipts/ladder-defect.md`: the L1 copies it at landing.
- Receipts: `.ufo/waves/round-91/w1/ExecLadder/{rung-probe.sh, rung-probe-base.txt, rung-probe-patched.txt, able-to-fail.txt, selftest-patched-scratch-floor31.txt}`.
- READY: `.ufo/waves/round-91/w1/ExecLadder_READY` (`verdict=REPAIRABLE rc=0`; the rc=0 holds with the floor bump in §Coupling; the patch alone reads rc=1).

## Tooling

No installs. No pacman, sysctl, or `/proc/sys` write. No git write in the lane or fleet (scratch clones only, `rev-parse --show-toplevel` asserted).
