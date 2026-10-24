# RevW2LabelOnly

role: reviewer (attack: the C2 frozen predicate's letter — label-only counter)
item: Reproduce RevCalibChecks F1's 17-line label-only counter against the frozen
C2 predicate verbatim; draft the minimal kill — the base-control arm
(`--rev 35d44b4b…` must NOT print `5 of 5`, must exit nonzero) — as plan erratum
E2 text plus the exact counter patch (argparse validation of `--rev` + the arm),
with a transcript showing the label-only counter failing the arm and the honest
counter passing it.

Lane state under test: tip `cbbee56e9a3589b0b46736ad36f1b77701def80e` (committed,
jj-colocated). Zero writes to the lane: every probe ran against
`git clone --no-checkout` copy `/tmp/r63lo/lane-clone` or `tempfile.mkdtemp`
scratch. Tooling: none installed; pacman untouched per the pause.

## 1. The frozen predicate, at the letter

`plans/round-63.md` §C2 (lines 88–95), committed at `cbbee56e`:

```
python3 -B verifiers/check_r63_routed_repairs.py --rev <rev>
```

prints `r62 routed defects closed 5 of 5` and exits 0, where each of the five
checks is **computed from committed bytes at `<rev>`**, never from a literal
comparison: …

The binding surface is exactly: one command, one printed line, exit 0. The
honest-computation requirement sits in a `where` clause that no command arm
tests; `<rev>` is unbound (no rev is named where the count must be <5). C1's
predicate wraps `--self-test`, which carries a must-fail arm; C2's does not.

## 2. Attack — the label-only counter meets the predicate verbatim

`/tmp/r63lo/check_label_only.py`, reproduced per RevCalibChecks F1 (16 code
lines + docstring; never opens git, never reads a byte):

```python
#!/usr/bin/env python3
"""Dishonest counter A: label-only. …(docstring elided)…"""
import argparse
import sys

p = argparse.ArgumentParser()
p.add_argument('--rev', required=True)
p.parse_args()
print('r62 routed defects closed 5 of 5')
sys.exit(0)
```

Verbatim transcript (all runs this seat, /tmp):

```
=== A1 label-only @ TIP cbbee56e (frozen predicate command shape) ===
$ python3 -B check_label_only.py --rev cbbee56e9a3589b0b46736ad36f1b77701def80e
r62 routed defects closed 5 of 5
exit=0

=== A2 label-only @ BASE 35d44b4b ===
$ python3 -B check_label_only.py --rev 35d44b4b4dcdda234b5dbff7af37e432fec55f05
r62 routed defects closed 5 of 5
exit=0

=== A3 label-only @ garbage rev ===
$ python3 -B check_label_only.py --rev garbage-rev-xyz
r62 routed defects closed 5 of 5
exit=0
```

Verdict on the committed bytes: **the hole is real and verbatim.** The program
prints the required line and exits 0 at every `<rev>` — including a revision
that does not exist. RevCalibChecks F1 is confirmed on the committed
`cbbee56e` plan text, not just argued. The predicate as written cannot
distinguish this file from the honest instrument; C2's claim would stand on a
constant printer.

Honest counter for contrast (committed script, sha256
`5a15feac0358fd537ad3a54cad589fa5f41743971e02f9d3e742fa4c3528c6ec`, run against
the /tmp clone):

```
=== B1 @ TIP ===  PASS×5 → r62 routed defects closed 5 of 5, exit=0
=== B2 @ BASE === FAIL×5 → r62 routed defects closed 0 of 5, exit=1
      (append-only: prefix=True grew_by=0 line(s) — E1's second conjunct fires)
=== B3 @ garbage === argparse error → exit=2
```

Two corrections to RevCalibChecks, from measured committed behavior:

- **F3's `1 of 5` base figure is stale.** Their reference carried the pre-E1
  single-conjunct check 4. The committed script's check 4 has E1's growth
  conjunct (`grew_by=0` → FAIL at base), so the committed counter prints
  **0 of 5, exit 1** at `35d44b4b` — matching the declared expected-result
  count. The plan's *prose* is the stale part: line 113 still says "check 4
  passes (an empty delta is a prefix…)" while printing `0 of 5`. E2 must fix
  that clause (draft below does).
- **`--rev` validation is already committed** (`REV_RE` + `ap.error`, lines
  59, 359–360): non-40-hex exits 2. The patch below retains it verbatim —
  it is the arm's load-bearing half: `35d44b4b` short-form is rejected, so
  the arm must name (and does name) the full 40-hex.

## 3. Minimal kill — the base-control arm

The smallest predicate change that unconditionally fails every rev-agnostic
constant printer: name the do-nothing rev as a second arm.

### Proposed erratum E2 text (insert after E1, `plans/round-63.md` line 159)

```markdown
## Erratum E2 (post-data, wave-2 falsification — seat RevW2LabelOnly,
## reproducing wave-1 RevCalibChecks F1)

`§C2`'s frozen predicate named one command arm — `--rev <rev>` prints
`r62 routed defects closed 5 of 5`, exit 0 — and left "computed from committed
bytes at `<rev>`" in a `where` clause no arm tests. A 17-line script printing
that literal line meets the predicate at every `<rev>`, including nonexistent
revisions (w2 evidence: label-only counter, same bytes at tip, r62 tip, and
`garbage-rev-xyz`).

E2 adds the do-nothing control as a second named arm of the same predicate:

```
python3 -B verifiers/check_r63_routed_repairs.py --rev 35d44b4b4dcdda234b5dbff7af37e432fec55f05
```

prints `r62 routed defects closed 0 of 5` and exits nonzero. The full 40-hex
is required: the counter rejects short forms (`argparse` `REV_RE`, exit 2).
"Exits nonzero" is used rather than `exit 1` so environmental failures
(exit 2) still satisfy the arm. The exact `0 of 5` headline is required so a
printer emitting `4 of 5` — or nothing — with a nonzero exit also fails.

E2 also corrects one stale clause in `§C2`'s expected result, superseded by
E1: "4 passes (an empty delta is a prefix — recorded honestly as a check that
only bites when text is rewritten)" is replaced by "4 fails on E1's
growth conjunct (zero lines appended at the tip)". The measured base run
already prints `0 of 5`; this aligns the prose with E1.

Bound, declared with the erratum: a counter keyed on the rev STRING (5-of-5
at `<rev>`, 0-of-5 at `35d44b4b…`) satisfies both named arms with zero
computation — demonstrated in w2 (rev-keyed constant printer). That class is
bound by the counter's `--self-test`, which the patch below extends to run
the real r62 tip as the same arm inside the instrument; a future C-claim
wanting predicate-level binding of computed-ness needs a supplied-bytes
self-test or a mid-score fixture (RevCalibChecks F2/F5), not another named
rev. The success rev remains the round's measured tip (`cbbee56e`), per the
predicate's `<rev>`.
```

### Proposed counter patch (`verifiers/check_r63_routed_repairs.py`)

Two hunks: docstring parity with the re-armed predicate, and the arm made
instrument-level — `self_test()` exercises `run()` against the lane's real
r62 tip so a hard-coded headline fails inside the self-test, not just at the
CLI. (`--rev` argparse validation is already committed and unchanged; shown
in §2, B3 → exit 2.)

```diff
--- a/verifiers/check_r63_routed_repairs.py
+++ b/verifiers/check_r63_routed_repairs.py
@@ -10,7 +10,11 @@
 
 Frozen predicate:
   python3 -B verifiers/check_r63_routed_repairs.py --rev <rev>
-prints `r62 routed defects closed 5 of 5` and exits 0.
+prints `r62 routed defects closed 5 of 5` and exits 0, AND
+  python3 -B verifiers/check_r63_routed_repairs.py --rev 35d44b4b4dcdda234b5dbff7af37e432fec55f05
+prints `r62 routed defects closed 0 of 5` and exits nonzero (erratum E2:
+the do-nothing control is a named arm of the predicate, so a constant
+printer that never opens a committed byte fails it).
 
 The five checks, each COMPUTED from `git show <rev>:<path>`:
 
@@ -44,6 +48,8 @@
 from __future__ import annotations
 
 import argparse
+import contextlib
+import io
 import re
 import subprocess
 import sys
@@ -339,6 +345,19 @@
         finally:
             R62_TIP = saved_tip
 
+        # E2 arm: the predicate's do-nothing control, exercised against the
+        # lane's real r62 tip.  run() must report all five checks red, print
+        # the exact 0-of-5 headline, and exit nonzero there; a counter that
+        # hard-codes the headline fails this arm.
+        buf = io.StringIO()
+        with contextlib.redirect_stdout(buf):
+            rc = run(LANE, R62_TIP)
+        lines = buf.getvalue().splitlines()
+        check("E2 arm: the lane r62 tip scores 0 of 5, nonzero exit",
+              (lines[-1] if lines else "", rc),
+              ("r62 routed defects closed 0 of 5", 1))
+        check("E2 arm: all five checks report FAIL at the lane r62 tip",
+              sum(1 for ln in lines if ln.startswith("FAIL")), 5)
         print("self-test: %d failure(s) over %d assertions"
               % (failures, assertions))
         return 1 if failures else 0
```

## 4. Transcript — label-only fails the arm, honest passes it

Patched file is `/tmp/r63lo/check_patched.py`, also dropped into the clone at
`lane-clone/verifiers/` so `LANE` resolves there (zero lane writes).

```
=== C1 patched --self-test (LANE=clone; new arm inside) ===
self-test: 0 failure(s) over 17 assertions
exit=0            # committed self-test baseline: 0 failure(s) over 15 assertions
                  # → the arm adds exactly 2 assertions, both green

=== C2 patched --rev cbbee56e… (success arm) ===
PASS×5 … r62 routed defects closed 5 of 5
exit=0

=== C3 patched --rev 35d44b4b… (E2 arm command) ===
FAIL×5 … r62 routed defects closed 0 of 5
exit=1            # honest counter PASSES the arm

=== C4 patched --rev garbage-rev-xyz ===
check_patched_run.py: error: --rev must be a full 40-hex revision (or use --self-test)
exit=2            # argparse validation retained

=== A1–A3 (label-only, §2) under E2's two-arm predicate ===
arm 2 requires `0 of 5` + nonzero at 35d44b4b…; label-only prints `5 of 5`,
exit 0 there → label-only FAILS the E2 predicate. ✔ minimal kill verified.
```

Residual bound, demonstrated (not hypothetical):

```
=== E1/E2 rev-keyed constant printer (/tmp/r63lo/check_rev_keyed.py) ===
--rev cbbee56e… → r62 routed defects closed 5 of 5, exit=0
--rev 35d44b4b… → r62 routed defects closed 0 of 5, exit=1
--self-test     → argparse error: --rev required, exit=2
```

It satisfies both E2 arms with zero computation — the explicit residual —
and fails only the instrument's `--self-test` surface (no flag, exit 2),
which is why the patch binds the arm inside `self_test()` against the real
tip rather than trusting CLI shape alone.

## 5. Verdict

**C2's frozen predicate is FALSIFIED at the letter** on committed bytes: a
label-only printer meets it verbatim at every rev including nonexistent ones.
The committed instrument itself is sound — honest 5-of-5 at tip, 0-of-5 exit 1
at base, argparse-guarded `--rev`, 15-assertion self-test. The defect is in the
plan sentence (and the counter's docstring copy of it), not the checks.

**Smallest safe correction:** erratum E2 as drafted — one added command arm
(exact `0 of 5` + nonzero at `35d44b4b…`), one stale-prose fix (the "4
passes" clause), the rev-keyed bound declared, plus the counter patch that
puts the same arm inside `--self-test` (17 assertions, all green on the /tmp
clone). Everything beyond — rev-keyed constants, the bytes-fingerprint class
— is bounded by E2's declared bound or needs the heavier supplied-bytes
control (RevCalibChecks F5), explicitly not claimed minimal.

Artifacts: `/tmp/r63lo/{check_label_only.py,check_rev_keyed.py,check_committed.py,check_patched.py,lane-clone/}`.
Report: `.ufo/waves/round-63/w2/RevW2LabelOnly.md` (this file).
