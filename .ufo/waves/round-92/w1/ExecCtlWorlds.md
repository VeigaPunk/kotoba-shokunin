# ExecCtlWorlds — C1 build (round 92): shortcut and honest control worlds

Seat: ExecCtlWorlds (executor, leaf). Base: e073723ae667b64e534f8621bddb83ad12ad0e71 (freeze).
Scratch commit (scratch identity, scratch clone only): 81f7c8b91d592cece20d81e981a13a88c376b525.
Patch: `.ufo/waves/round-92/w1/ExecCtlWorlds/ExecCtlWorlds.patch` (`git diff --cached --binary` over
`verifiers/fixtures/round-92/`, 5 new files, mode 100755). Apply-check at e073723 passed.
Receipt: `.ufo/waves/round-92/w1/ExecCtlWorlds/probe.txt`. READY: `.ufo/waves/round-92/w1/ExecCtlWorlds_READY`.

## Files (all new, `verifiers/fixtures/round-92/`)

| script | world | exit | stdout line |
|---|---|---|---|
| `ctl-c2-capline-only-v2.sh` | cap-only shortcut, committed in scratch | 1 | `C2-SHORTCUT-REFUSED: instrument-pin admission missing (FAIL guard instrument-pin: ...)` |
| `ctl-c2-honest.sh` | freeze (or `$1`) | 0 | `C2-PREDICATE-MET` |
| `ctl-c1-manifest-only-v2.sh` | manifest-only shortcut, row committed in scratch | 1 | `C1-SHORTCUT-REFUSED: rows committed and read; instrument cannot evaluate (rc 2)` |
| `ctl-c1-honest.sh` | freeze (or `$1`) | 0 | `C1-PREDICATE-MET` |
| `controls-run.sh` | the frozen counting command | 0 | `round-92 controls: shortcuts refused 2 of 2; honest held 2 of 2` |

No script writes the lane; every world is a scratch clone under `${HYAKU_SCRATCH:-/fast/scratch/hyaku}/kotoba-r92/ExecCtlWorlds/`, removed by trap. `bash -n` passes on all five.
`verifiers/fixtures/round-91/` is byte-identical to the base (`git diff --quiet e073723 -- verifiers/fixtures/round-91` → yes).

## Construction decisions

- **C2 shortcut cap value is 330, not 320.** At the freeze `SELF_TEST_TIMEOUT_S` is already 360, so "set it ≥ 320" is a byte no-op and
  the blob stays pinned. 330 is ≥ 320 *and* ≥ 2 × MEASURED_SELFTEST_S (161 → 322), so the cap conjunct alone holds and only the
  missing INSTRUMENT_PINS admission can refuse the world. The changed blob is unpinned; the tip battery's instrument-pin guard FAILs on it.
- **C1 shortcut row targets `verifiers/check_gate_registry.py`** (no probe set), not a probed target as round-91 did. The battery's
  `parse_manifest` refuses it before any probe runs: `could-not-evaluate: manifest mb-c1-shortcut-kill: target 'verifiers/check_gate_registry.py' has no probe set`, rc 2.
  The row is read from the committed rev through `git show <rev>:<manifest>`, so the "rows committed and read" conjunct holds; the round-91 defect (working-tree append, base rev passed) is not reproduced.
- Honest C2 reads its three conjuncts with `ast` over `git show <rev>:<path>` (cap, measured constant, `INSTRUMENT_PINS` admission of the
  floors blob), then runs the public tip battery and greps the `guard instrument-pin PASS` line. Its overall tip-battery rc is not gated
  (carried red corpus gates, per plan § no-harm).

## Observed (one run of `controls-run.sh` from the scratch clone; per-script runs before it agreed)

- `controls-run.sh` rc=0, stdout: `round-92 controls: shortcuts refused 2 of 2; honest held 2 of 2`.
- C2 shortcut: `tip battery exit 1`; `FAIL guard instrument-pin: verifiers/check_assertion_floors.py blob a189e61be79828fa856a1fdc900dcec10801a1af at <rev> is not a pinned blob` (rc 1; ~189 s).
- C2 honest: cap 360 ≥ 2×161: True; floors blob 6f2c52fb2e09e817dff3360b97400a5d6e53626c admitted: True; `guard instrument-pin PASS`; `C2-PREDICATE-MET` (rc 0).
- C1 shortcut: `could-not-evaluate: manifest mb-c1-shortcut-kill: target 'verifiers/check_gate_registry.py' has no probe set`; `C1-SHORTCUT-REFUSED ...` (rc 1; ~2 s).
- C1 honest: `G2 copy integrity PASS: 23 mutant copies and 3 revision copies`; `G3 ... PASS: 1 SKILL.md line`; `mutation battery killed 17 of 17 kill-set; equivalents survived 6 of 6; disclosed survivors 0 of 0`; `C1-PREDICATE-MET` (rc 0; ~34 s).

## Findings for the L1 (no amendment needed; predicates unchanged)

1. The honest scripts default to the lane tip (`git rev-parse HEAD` of the script's repo). At landing, the default moves to the landing commit; the
   `controls-run.sh` counting line must be re-read at the landing revision (the plan's landing predicate), not inherited from this probe at e073723.
2. The tip battery prints its guard lines only after all six gates have run (~3 min here); the C2 world is therefore slow, not short-circuited.
3. Tip-battery sandbox fleet root is `repo.parent`: in the scratch it is the seat dir, in the lane it is the fleet root (the sandbox symlinks each entry). Verdicts do not depend on it.

## Install / host changes

None. No packages, no kernel/sysctl, no PATH changes. Scratch removed at yield.
