# Pointer-gate controls — round 73 wave 1, seat ExecPointersControls

Hard-negative and shortcut worlds for the mined-mistake fix `check_report_pointers.py`
(plan `/home/vgpnk/Projects/shokunin/kotoba-shokunin/plans/round-73.md` § Frontier step; gate draft at
`../ExecPointersGate/check_report_pointers.py`, owned by seat ExecPointersGate).

Each `<world>/` holds `report.md` (plus variants), a `world.json` with the revision, the round, the
expected exit/tally and the **honest reading** (what a calibrated gate must do, as distinct from what the
frozen predicate literally does), and — for the untracked world — a sandbox recipe the runner builds.
`run_worlds.py` runs the draft on every world and writes the actual reading under `readings/` (one file
per run, a `summary.tsv`, and `GATE.txt` naming the gate sha256/bytes/mtime measured). Every reading file
carries the gate sha it was produced with, so a battery that straddles an edit is detectable.

```
python3 -B run_worlds.py                 # default gate: ../ExecPointersGate/check_report_pointers.py
python3 -B run_worlds.py --gate PATH --keep-sandboxes
```

Exit 0 iff every measured exit matches its expected exit. The runner writes nothing outside this
directory (sandboxes under /tmp, removed at exit).

## Worlds — 19 readings, measured at the final freeze candidate `sha256:2537a22…`

Draft identity at measurement: 40,352 B, mtime 2026-10-25T21:12:51, `--self-test` 0 failures over 57
assertions, r72 RED-BEFORE `34 of 37` exit 1. `readings/GATE.txt` and `readings/summary.tsv` are
authoritative. **All 19 readings match.**

| world | report | rev | expected | measured | reading |
|---|---|---|---|---|---|
| `dir-only` | report.md | ac8fc59 | exit 2, `5 of 5` | exit 2, `5 of 5` | D3 fix: `pointer objects: blob 0, directory 5`, cannot evaluate |
| `dir-only` | report-mixed.md | ac8fc59 | exit 1, `5 of 6` | exit 1, `5 of 6` | can fail; the directory tokens inflate M |
| `dir-legit` | report.md | 072048f | exit 0, `2 of 2` | exit 0, `2 of 2` | fair-use directory + blob stays green |
| `later-rev-only` | report.md | 072048f | exit 1, `1 of 4` | exit 1, `1 of 4` | Q60: round-73 receipts absent at the base |
| `later-rev-only` | report.md @ control | ac8fc59 | exit 0, `4 of 4` | exit 0, `4 of 4` | same text, later rev: revision sensitivity real |
| `untracked-worktree` | report.md | 072048f | exit 1, `2 of 4` | exit 1, `2 of 4` | untracked file on disk never resolves |
| `fence-hides-prose` | report.md | 072048f | exit 1, `0 of 1` | exit 1, `0 of 1` | a resolving fenced token does not mask prose |
| `fence-hides-prose` | report-fence-only.md | 072048f | exit 2, `0 of 0` | exit 2, `0 of 0` | D1 fix: no-pointer universe is cannot-evaluate |
| `fence-hides-prose` | report-code-span.md | 072048f | exit 0 (blind spot, documented) | exit 0, `1 of 1` | command spans unchecked |
| `wrong-round-receipts` | report.md | ac8fc59 | exit 1, `2 of 3` | exit 1, `2 of 3` | bare `receipts/` maps to round 73 |
| `wrong-round-receipts` | report-correct.md | ac8fc59 | exit 0, `3 of 3` | exit 0, `3 of 3` | the honest fix is the full round path |
| `no-pointers` | report.md | ac8fc59 | exit 2, `0 of 0` | exit 2, `0 of 0` | D1 fix: vacuous 0 of 0 refused |
| `typo-near` | report.md | ac8fc59 | exit 1, `1 of 3` | exit 1, `1 of 3` | nearest names exact (`census-before.txt`, `check_tip_battery.py`) |
| `typo-near` | report-wrong-existing.md | ac8fc59 | exit 0, `1 of 1` | exit 0, `1 of 1` | existing-but-wrong artifact is out of class |
| `line-suffix` | report.md | ac8fc59 | exit 0, `2 of 2` | exit 0, `2 of 2` | D4 fix: locator stripped, file resolved |
| `multiword-span` | report-broken.md | ac8fc59 | exit 1, `0 of 1` | exit 1, `0 of 1` | D2 fix: prose after a path no longer hides it |
| `multiword-span` | report-valid-section.md | ac8fc59 | exit 0, `1 of 1` | exit 0, `1 of 1` | `<lesson> § <section>` counted and resolved |
| `absolute-path` | report.md | ac8fc59 | exit 0 (blind spot, documented) | exit 0, `1 of 1` | absolute receipts unchecked |
| `bare-cross-round` | report.md | ac8fc59 | exit 0, `1 of 1` | exit 0, `1 of 1` | bare name loses round attribution |

## Defects this battery found (all four fixed in the draft)

Pre-fix snapshots and readings are preserved in `readings/` file headers (gate sha per reading) and in
`.ufo/waves/round-73/w1/ExecPointersControls.md`. Summary:

| defect | pre-fix reading | fix in the draft |
|---|---|---|
| D1 vacuous `0 of 0` read as pass | `no-pointers` exit 0; self-test pinned "empty: zero pointers is exit 0" | `M == 0` → exit 2, `cannot evaluate: … no backticked pointer token` |
| D2 one prose word hid a broken pointer | `multiword-span/report-broken.md` exit 0, `0 of 0` | `is_command_span` no longer treats a path head as a command |
| D3 every pointer a directory read as pass | `dir-only` exit 0, `5 of 5` (r72 report's own `receipts/base-outputs/` is a tree) | prints `pointer objects: blob b, directory d`; `B == 0` → exit 2 |
| D4 `path:line-line` was a false positive | `line-suffix` exit 1, `1 of 2` while nearest named the same file | `LOCATOR_SUFFIX = re.compile(r":\d+(?:-\d+)?$")` stripped before resolution |

## Residual items for freeze 2 (reported, not fixed by the controls seat)

- The docstring still prints the old sentence "exit 0 iff U == 0" (line 22) beside the tail (line 25) and
  the exit-codes block; the L1's freeze addendum must carry one predicate sentence with the `M >= 1`,
  `B >= 1` conditions, or the counter contradicts its own frozen sentence.
- The nearest-name column now suggests a cross-round repair (fixed at `2537a22`): `receipts/c2-base.txt` read
  at round 73 prints `nearest: base-sweeps.txt, other round: .ufo/waves/round-72/receipts/c2-base.txt`.
- A line locator is stripped, not verified: `corpus/lessons/round-72.md:99999` (98-line file) reads
  `1 of 1` exit 0. Documented in the draft's blind-spot list; out of the existence class.
- RED-BEFORE names three tokens: the two `tip-check_*` defects (plan requirement met) and
  `S2xx.sha256`, the r72 report's own redaction mask. Do not re-use the mask in the r73 report.
- Blind spots now stated in the draft: prose outside code spans, fences, command spans, globs,
  placeholders, absolute paths, bare-name round loss, committed-bytes-only.
