# MutTesterRedsR99 receipts — index

All runs used the frozen lane counter
`verifiers/fixtures/round-99/carried-reds.py` (sha256
`5f964253755e0d69f7651a0be43288aaad60fec3ba6c5a25328f5619972bf358`) with
`HYAKU_SCRATCH=/fast/scratch/hyaku/kotoba-r99/MutTesterRedsR99` and the scratch
clone `repo` at the world revision. The lane was never written.

## Controls / worlds

| file | world | verdict |
|---|---|---|
| `w0-green-base.txt` | W0 `721fb5af` honest route | `C2-PREDICATE-MET` |
| `run-W1.txt` | W1 `0f27688e` receipt corrected to `SKILL.md` | **MET** (F2) |
| `run-W2.txt` | W2 `9ad51a6a` non-literal corrections block | UNMET, frozen 3 of 4 |
| `run-W3.txt` | W3 `aa4f447b` horizon 999999 + absent line 4000 | UNMET, green 2 of 3 |
| `run-W4.txt` | W4 `7c13c7e1` computed `INSTRUMENT_PINS` | UNMET, frozen 3 of 4 |
| `run-W5.txt` | W5 `1d7d4a1f` forced-PASS governance + pin | UNMET, frozen 3 of 4 |
| `run-W6.txt` | W6 `51c6558a` one glob coverage row | **MET** (F4) |
| `run-W7.txt` | W7 first build (doubled quote pair) | MET (superseded) |
| `run-W7-clean.txt` | W7 `0009d013` clean quote rewrite | **MET** (F1) |
| `run-W8.txt` | W8 `7f4cd9cd` rows pinned to old lines 2620/779 | **MET** (F3) |
| `run-W9.txt` | W9 `ca0bae4a` changed checklist blob not pinned | UNMET, guards FAIL |
| `run-W10.txt` | W10 `e55cf830` self-test fixture altered | UNMET, self-tests 2 of 3 |

`world-revs.txt` lists every revision; `world-diffs.txt` shows the W1/W7/W8
evidence hunks; `worlds.py` / `build_w0.py` rebuild every world from
`b53e209603e7c480cd975ea543e415b66f695438`.

## Counter mutants (scratch copies; the lane counter is untouched)

| file | mutant | run receipt | result |
|---|---|---|---|
| `M1-drop-reds.py` | drops `green == 3` | `mut-M1-on-W3.txt` | MET → killed by W3 |
| `M2-drop-selftests.py` | drops `held == 3` | `mut-M2-on-W10.txt` | MET → killed by W10 |
| `M3-drop-frozen.py` | drops `frozen == 4` | `mut-M3-on-W5.txt` | MET → killed by W5 |
| `M4-pass-min-10.py` | `CHECKLIST_PASS_MIN = 10` | `mut-M4-on-W3C.txt` | UNMET → survives |
| `M5-accept-na.py` | accepts N/A lines | `mut-M5-on-W3C.txt` | UNMET → survives alone |
| `M45-pass-min-10-accept-na.py` | both edits | `mut-M45-on-W3C.txt` | UNMET (green 1 of 3) |
| `M6-skip-checklist-literal.py` | accepts a non-literal corrections block | `mut-M6-on-W2.txt` | MET → killed by W2 |
| `M7-skip-pins-literal.py` | accepts a dict-shaped pins block | `mut-M7-on-W4.txt` | MET → killed by W4 |
| `M8-drop-guards.py` | drops `guards_ok` | `mut-M8-on-W9.txt` | MET → killed by W9 |

`mutant-diff-*.txt` are the exact diffs against the frozen counter. W3C is a
rebuild of the committed w3 control
(`.ufo/waves/round-99/receipts/ctl-worlds/w3-checklist-gov-na-pinned.patch`),
rev `32921fde`; its pristine reading is the committed
`.ufo/waves/round-99/receipts/c2-ctl-w3-checklist-gov-na-pinned.txt`.

## Helpers

- `probe_worlds.py` — fast gate/self-test pre-check in a fleet-shaped sandbox.
- `probe_gov.py` — enumerates the live dead governance subjects and correction
  problems (the counter's `last()` truncates them to 300 chars).
- `make_mutants.py` — builds the mutant copies from the frozen counter.
