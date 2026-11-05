# ExecFreezeGate — the C1 freeze gate (r89 w1)

Seat: ExecFreezeGate (executor, leaf). Lane `/home/vgpnk/Projects/shokunin/kotoba-shokunin`,
base at plan draft `a5b3b15c00b1de5db321e4226a0a7db17340e605`. 2026-11-05.
Frozen predicate (plans/round-89.md § C1, carried verbatim in the gate docstring and receipts):
`--self-test` → `0 failure(s) over N assertions` (N ≥ floors floor), exit 0; `--plan
verifiers/fixtures/freeze-gate/r88-controls.md` → exit 1 naming `w_added_red`; `--plan
verifiers/fixtures/freeze-gate/r88-controls-fixed.md` → exit 0.

## Files written (all in this seat's ownership)

- `verifiers/check_freeze_gate.py` (new, executable, stdlib only, `python3 -B` style; no
  hardcoded temp path — the self-test asserts the absence of the literal).
- `verifiers/fixtures/freeze-gate/` (new): `sim-w-added-red.sh`, `sim-w-silenced.sh`,
  `sim-w-healed.sh`, `sim-w-tip.sh` (fail-closed simulators), `r88-controls.md`
  (the unsatisfiable r88 declarations), `r88-controls-fixed.md` (the observed verdicts).
- `verifiers/floors-registry.json`: ONLY the `freeze_gate` row added (floor = 30 = the
  self-test's assertion count; path = this gate). No other row touched;
  `instrument_total` intentionally untouched (not this seat's key).
- `.ufo/waves/round-89/w1/ExecFreezeGate/`: `predicates.txt`, `selftest.txt`,
  `sim-outputs.txt`, `sha256-and-floors-row.txt`; this report.
- `.ufo/waves/round-89/w1/FG_READY`: the script sha256
  `a20e6f9afff367dfb56b3d8fa437a176627bf55623d1f6b20dea320943e15e41`.

## Result — the three predicate arms, measured (receipts in `ExecFreezeGate/`)

```
$ python3 -B verifiers/check_freeze_gate.py --self-test
0 failure(s) over 30 assertions                                    exit=0
$ python3 -B verifiers/check_freeze_gate.py --plan verifiers/fixtures/freeze-gate/r88-controls.md
REFUSED control w_added_red (line 36): declared "exit 0; stdout contains D5=FAIL";
observed exit=0 stdout=w_added_red D5=PASS\n (stdout literal 'D5=FAIL' absent ...)  exit=1
$ python3 -B verifiers/check_freeze_gate.py --plan verifiers/fixtures/freeze-gate/r88-controls-fixed.md
freeze gate: 4 control(s) held — freeze may proceed                exit=0
```

The unsatisfiable arm mechanically reproduces r88 F1: the r88 freeze declared v2 D5 FAIL
(ii) for `w_added_red` and never executed the control; the committed receipts record
D5 PASS (ExecMonotoneD5 F1, CriticFalsify C2-S1 — spotcheck routed defect 3). The gate
executes every declared control (cwd = lane root, fresh TMPDIR per control, 120 s cap),
compares declared vs observed, and refuses on the first violated control.

## Simulator grounding (fail-closed: missing receipt → exit 2, never a guess)

| control | prints | grounds |
|---|---|---|
| w_added_red | `w_added_red D5=PASS` | `w1/ExecMonotoneD5.md` F1 marker + control row; `--- w_added` block of `w1/ExecMonotoneD5/receipts.txt` |
| w_silenced | `w_silenced D5=FAIL-world-unreachable` | `--- w_silenced` block ("FAIL d5 identity FAIL: rev has 8 names, base has 9"); C2-S2 row in `w1/CriticFalsify/attacks.md` |
| w_healed | `w_healed D5=PASS` | `--- w_healed` block (`PASS d5`) |
| w_tip | `w_tip D5=PASS` | `receipts/before-C2-tip.txt` (r87 do-nothing `FAIL d5`/`4 of 5`), `receipts/l1-c2-tip.txt` (v2 `5 of 5`, tip hash), `w1/ReviewerC2/review.md` item 4 |

Declarations come verbatim from plans/round-88.md § C2. In `r88-controls.md` only
`w_added_red` differs from the observed world (declared `D5=FAIL`), so exactly that
control refuses; `w_silenced`'s declared `D5=FAIL` holds as a substring of the observed
`D5=FAIL-world-unreachable`. Fail-closed proof (sims copied outside the lane → rc=2
naming the receipt) is in `sim-outputs.txt`, and asserted by four self-test arms.

## Findings

**F1 — floors-guard sync is REQUIRED in the same freeze change (L1-owned file).** After
adding the `freeze_gate` registry row, `python3 -B verifiers/check_assertion_floors.py`
fails fast with:
```
FAIL registry size drift: instrument_total=18 but 19 entries in verifiers/floors-registry.json
FAIL registry row vanish: freeze_gate (listed in verifiers/floors-registry.json, absent from both guard tables)
guard rc=2
```
`check_assertion_floors.py` is in no seat's ownership list, so I did not edit it. Per the
registry's own bump-in-step rule the freeze commit must add the `freeze_gate` row to both
in-file tables (`EXPECTED_INSTRUMENTS`, `INSTRUMENTS`), bump `instrument_total` 18→19, and
touch the guard docstring in the same change. This is pre-score state — no kill-rule
implication — but any no-harm battery that runs the guard before that sync reads rc=2.

**F2 — the seat item's pointer "ReviewerC2/review.md (C2-S2/S3) is imprecise."** review.md
contains no `C2-S2`/`C2-S3` markers anywhere (grepped). The committed C2-S2/S3 records live
in `w1/CriticFalsify/attacks.md` (rows 13–14, narrative 44–48, ruling 113–115) and are
cross-referenced in `r88-w1-results.json` (ScribeLesson and CriticFalsify entries).
Grounding was preserved without losing any required source: `sim-w-silenced` greps the
C2-S2 row in `attacks.md` (the file that actually carries it), and `sim-w-tip` greps
`review.md` item 4 — the reviewer's independent v2 re-derivation ("closed 5 of 5",
exit=0), which IS in review.md.

**F3 — first-run defects, caught and fixed before scoring.** (a) The sims' lane-root
derivation was one `..` short (`dirname/../../..` needed from
`verifiers/fixtures/freeze-gate/`); every sim fail-closed correctly during the broken
state (exit 2 on the mis-resolved receipt path), which is the designed behavior under
path drift. (b) The self-test's CLI helper returned a 3-tuple against 2-tuple unpacks.
Both fixed; the committed bytes are the tested bytes (self-test re-run green after the
fixes, `0 failure(s) over 30 assertions`).

## Scope discipline

- No git/jj write anywhere; read-only inspection only. No edits to any frozen r88
  instrument (`check_r86_routed_repairs_v2.py`, `check_omp_root_semantics_v2.py`,
  `verify_corpus_integrity.py`, `corpus-baseline.json`) — not opened for writing.
- Scratch: `/fast/scratch/hyaku/kotoba-r89/ExecFreezeGate/` used as TMPDIR, deleted
  before this seat yields. No tool installed or updated (none needed).
- No handoff waits: this seat gates on committed r88 receipts and the frozen plan only.

## Checks the main agent should run (not run by this seat)

1. `python3 -B verifiers/check_freeze_gate.py --self-test` → `0 failure(s) over 30 assertions`, exit 0.
2. `python3 -B verifiers/check_freeze_gate.py --plan verifiers/fixtures/freeze-gate/r88-controls.md` → exit 1, refusal names `w_added_red`.
3. `python3 -B verifiers/check_freeze_gate.py --plan verifiers/fixtures/freeze-gate/r88-controls-fixed.md` → exit 0.
4. `sha256sum verifiers/check_freeze_gate.py` → `a20e6f9a…e15e41` (matches FG_READY).
5. `python3 -c 'import json;json.load(open("verifiers/floors-registry.json"))'` → parses.
6. L1 pre-freeze: sync `check_assertion_floors.py` (F1) so the guard reads green at the freeze commit.
