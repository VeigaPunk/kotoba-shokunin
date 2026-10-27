# B11RepairD4 — D4: floor the two unfloored round-74 self-tests

Seat: `B11RepairD4` (executor). Round 76, wave w1. Plan: `plans/round-76.md` § Trigger (D2–D4 land
this round as disclosed hygiene repairs **outside C2's frozen counter scope**) and § Touch list
(`verifiers/floors-registry.json` (+2 rows, bump-in-step with the guard's in-file tables);
`verifiers/check_assertion_floors.py` (in-file tables + docstring, same change)).

Defect closed: `corpus/lessons/round-74-verifier-spotcheck.md:141-142` (routed defect 4, item 4) —
"Floor the two new self-tests (`check_spec_craft.py --self-test` 250, `check_sibling_reread.py
--self-test` 47) in the assertion floors — the known gap the lane named (E1.3)." This is the r62
F17 class re-found for two instruments: an arm dropped from either file read green with every gate
passing, because no floor covered them.

**Verdict: D4 CLOSED. Both floors land in one change (registry + both in-file tables + docstring +
the guard's own F6 anchor). Measured floors 250 and 47 equal the r74 spot-check's recorded values;
the guard now runs 17 instruments (was 15), all PASS, exit 0.**

Files changed (2, both named in the plan's touch list; no commit made — the lane index is untouched):

- `verifiers/floors-registry.json` — `instrument_total` 15 → 17; two new rows `spec_craft` (floor
  250, `verifiers/check_spec_craft.py`) and `sibling_reread` (floor 47,
  `verifiers/check_sibling_reread.py`). Appended after `scoped_rules_v32`, matching the r65
  precedent's ordering and the file's existing 2-space-indent shape.
- `verifiers/check_assertion_floors.py` — the two in-file tables (`EXPECTED_INSTRUMENTS`,
  `INSTRUMENTS`) gain the matching rows; the module docstring's floor list gains
  `spec_craft 250, sibling_reread 47` plus the round-76 provenance sentence; **and** the guard's own
  F6 self-test anchor (`'"instrument_total": 15'` → `'"instrument_total": 17'`) is updated in the
  same change, with the count-history comment extended.

The exact diff is reproduced verbatim in § Diff below and is also saved at
`/fast/scratch/hyaku/kotoba-r76/B11RepairD4/d4.diff` (scratch, removed on exit).

## Receipts

| Receipt | Content |
|---|---|
| `.ufo/waves/round-76/receipts/d4-selftests.txt` | both self-tests run at the lane root, full stdout + exit codes, plus the comparison against the r74 spot-check's recorded 250 / 47 |
| `.ufo/waves/round-76/receipts/d4-floors-after.txt` | the guard's `--self-test` (165 assertions, exit 0) and the live 17-instrument walk (all PASS, exit 0), both on a scratch copy carrying the edit |

## Measured counts — observed == recorded

```
$ python3 -B verifiers/check_spec_craft.py --self-test
...
self-test: 0 failure(s) over 250 assertions
exit=0

$ python3 -B verifiers/check_sibling_reread.py --self-test
self-test: 0 failure(s) over 47 assertions
exit=0
```

The r74 spot-check (`corpus/lessons/round-74-verifier-spotcheck.md:141-142`) records
"`check_spec_craft.py --self-test` 250, `check_sibling_reread.py --self-test` 47". **Observed 250
and 47 — equal to the recorded values, so no substitution was needed and the recorded numbers are
reused verbatim as the floors.** (Both counters were already re-measured at the round-76 base and
were unchanged.)

## The guard after the edit — 17 instruments, all PASS

```
$ python3 -B verifiers/check_assertion_floors.py
PASS harness observed=10 floor=10
PASS corpus_integrity observed=164 floor=164
PASS corpus_independent observed=105 floor=105
PASS surfaces observed=218 floor=218
PASS checklist observed=1863 floor=1863
PASS pins observed=62 floor=62
PASS harness_independent observed=123 floor=123
PASS compare_harness_independent observed=330 floor=330
PASS floors_guard observed=165 floor=150
PASS dispatch_prompts observed=56 floor=56
PASS sibling_census observed=68 floor=68
PASS overlap_levers observed=55 floor=51
PASS alwayson observed=89 floor=89
PASS correction_sweep observed=25 floor=25
PASS scoped_rules_v32 observed=240 floor=240
PASS spec_craft observed=250 floor=250          <- new
PASS sibling_reread observed=47 floor=47        <- new
exit=0
```

`--self-test` on the same tree: `0 failure(s) over 165 assertions`, exit 0 (unchanged from the
base's 165 — the guard's own assertion count is not moved by this edit, so its own floor of 150
stays correct and no self-referential re-bump is needed).

## Why the D4 change is load-bearing (measured, not asserted)

**Arm deletion is now caught.** With the new row in place, deleting one self-contained arm from
`verifiers/check_spec_craft.py` (the `(a') chrome-only tokens` world) makes the guard read:

```
FAIL spec_craft observed=247 floor=250 self_test_failures=86
```

and exit 1. At the base the guard never ran `check_spec_craft.py` at all — there was no
`spec_craft` line in its walk at all, so the same deletion was invisible to the floors guard
(measured: the base walk prints 15 instrument lines, the edited walk prints 17).

**Half-bumps are caught (registry ↔ tables).** Lowering only the registry's `spec_craft` floor to
249 (the guard's own tables left at 250):

```
FAIL registry floor drift: spec_craft registry=249 expected=250 row=250
exit=2
```

**Row deletion is caught.** Dropping the `spec_craft` row from both in-file tables while the
registry keeps it:

```
FAIL registry row vanish: spec_craft (listed in verifiers/floors-registry.json, absent from both guard tables)
exit=2
```

**The in-step F6 anchor was necessary.** Reverting only the guard's F6 self-test anchor
(`'"instrument_total": 17'` → `'"instrument_total": 15'`) while leaving the registry at 17 reds the
guard's own self-test:

```
2 failure(s) over 165 assertions
FAIL: mutation anchor lands exactly once (F6/total): got 0
FAIL: F6 size drift: names the class: got 'FAIL registry path absent: alwayson ...'
```

This is the r65 precedent's shape (r65 changed `'"instrument_total": 14'` → `15` in the same commit
that added `scoped_rules_v32`): the registry's declared total is a count-checked anchor, so a row
added without moving it stops landing. Verified the other direction too — the anchor at 17 with the
registry at 17 is what makes F6 pass.

## Findings for the L1 (adjacency; none of these are in my write scope)

**F1 (HIGH — the tip battery's `instrument-pin` guard will red at the tip).**
`verifiers/check_tip_battery.py` pins the six battery scripts by **blob sha**, and
`verifiers/check_assertion_floors.py` is one of them: `INSTRUMENT_PINS` names two allowed blobs
(`780f6fe5…` and `50348420…`). Any edit to the guard changes its blob, and the pin set is closed.
Measured in a fleet-shaped scratch sandbox:

```
# with the D4 edit (rev 55dd6f1…):
FAIL guard instrument-pin: verifiers/check_assertion_floors.py blob 9cb860bd… at 55dd6f1… is not a pinned blob
guard no-deletions PASS / floors PASS / instrument-size PASS / spotcheck-identity PASS
→ guards 4 of 5

# at the base (rev b7f13f4…, same sandbox, same scratch tree):
guard instrument-pin PASS
→ guards 5 of 5
```

So the D4 edit is what tips that guard red; it is not pre-existing. The r72 precedent shows how
this is normally handled: when r72 raised the floors, `a0f7f17` changed the guard and `30d27da`
(released 7 s earlier) added the *new* guard blob `50348420…` to the pin set, so the tip battery
kept reading 5 of 5. **The L1 must add the new guard blob to `INSTRUMENT_PINS` in
`verifiers/check_tip_battery.py` in the same landing.** The blob sha of the guard as it stands with
this edit is `9cb860bda21ef8d24fcb0603aa85372b96f3ac41` — but it must be recomputed from the
*landed* bytes, because any further edit to the guard changes it again. This file is not in my
write scope (the plan's touch list names only the registry and the guard), so I did not touch it.

Note also that the tip battery's other guards are unaffected by the edit: `instrument-size` reads
"instruments added 22 / deleted 3 lines (cap 40)" — PASS, well inside the 40-line cap; and
`floors` reads the 17 rows against the base's 15 and passes, because the guard's floors guard only
rejects a *lowered* floor or a *dropped* row, and this edit adds rows.

**F2 (MEDIUM — a coordinated three-artifact half-bump still reads green, as documented).** Lowering
`spec_craft`'s floor to 249 in the registry **and** in both in-file tables is self-consistent and
the guard reads `PASS spec_craft observed=250 floor=249`, exit 0. This is the guard's **documented**
trust boundary, not a regression: the registry's `$comment` states that "a coordinated edit of this
anchor as well is a three-artifact edit and out of scope for this guard". The r74 spot-check's D4
item asks for the two rows to be *floored*, which they now are; the residual is the pre-existing
boundary and is named, not silently inherited. The tip battery's `floors` guard is the second
layer: it compares the registry against the *base* revision's rows and rejects a floor lowered
below base — but only for rows present at the base, so a newly-added row's floor is not covered by
that second layer either.

**F3 (LOW — pre-existing red at the round-76 base, unrelated to this edit).** The base-battery
receipt `.ufo/waves/round-76/base-battery/base-battery.txt` records `verify_corpus_integrity.py
--json` as **exit 0** at `b7f13f4`, and `plans/round-76.md` § Base battery repeats "corpus integrity
exit 0". Re-measured, it is **exit 1** at that same base, with four DRIFT rows:

```
corpus.index.tracked_files          observed 145 expected 144  DRIFT
corpus.index.unindexed               observed 1   expected 0    DRIFT
corpus.pointers.report_total         observed 101 expected 99   DRIFT
corpus.pointers.commit_total         observed 44  expected 43   DRIFT
```

The cause is that `b7f13f4` (the r75 closure's own landing) added
`corpus/lessons/round-75-verifier-spotcheck.md` — the 145th tracked corpus file — **without an index
row in `corpus/README.md`** (checked: `git show b7f13f4:corpus/README.md` contains no reference to
it), and the baseline was not re-recorded. Verified this is a base condition and not my edit: at
`b7f13f4` in a clean clone the same four DRIFTs appear and the exit is 1; at its parent `ac9f295`
the corpus tree has 144 files and the gate reads exit 0. **The likely cause of the receipt's
exit=0 is a pipe artifact**: the receipt keeps only the JSON tail (`}\n ]\n}`) and reports
`exit=0`, but `python3 … --json | tail -3; echo $?` reports the *tail's* exit, not the verifier's —
the same command run without a pipe exits 1. This is a base-battery receipt-accuracy defect, not a
D4 defect, and it is outside my write scope (the receipt is the L1's, and `corpus/README.md` /
`verifiers/corpus-baseline.json` are corpus files the plan assigns to other seats). It matters
because the round-76 no-harm battery runs `verify_corpus_integrity.py --json` and will read red at
the tip for this reason. I did not repair it: touching `corpus/README.md` or the corpus baseline is
not in my write scope and would collide with the r75-closure repair lane.

## Method notes (honesty about what was measured where)

- The lane repo is a **jj** repo with a colocated `.git`; I used plain `git` (read-only) for all
  inspection and made **no** commit, branch, checkout, stash or index write in the lane. The two
  edited files are left as working-tree modifications for the L1 to land.
- The guard was run on a **scratch copy** (per the seat spec), at
  `/fast/scratch/hyaku/kotoba-r76/B11RepairD4/fleet/kotoba-shokunin` — a `git clone --shared` of
  the lane with the two edited files copied in, plus symlinks to every fleet-root entry so the
  fleet-relative `../.ufo/…` citation tokens resolve. This matters: a scratch copy that is *not*
  fleet-shaped makes `verify_skill_checklist.py --self-test` read
  `FAIL … '../PROTOCOL.md' does not resolve …` (2 failures over 1863 assertions) — an artifact of
  the missing fleet siblings, **not** of any edit; the same command in the lane reads
  `0 failure(s) over 1863 assertions`, exit 0. I confirmed the identical failure in a *pristine*
  clone at the base with zero edits, which is what attributed it.
- The guard's live walk takes ~100–110 s (it reruns 17 instruments' self-tests). Each measurement
  below was run to completion; no result is extrapolated.

## Verification summary (all commands and exit codes as run)

| Command | Where | Result |
|---|---|---|
| `python3 -B verifiers/check_spec_craft.py --self-test` | lane root | `0 failure(s) over 250 assertions`, exit 0 |
| `python3 -B verifiers/check_sibling_reread.py --self-test` | lane root | `0 failure(s) over 47 assertions`, exit 0 |
| `python3 -B verifiers/check_assertion_floors.py --self-test` | scratch copy w/ edit | `0 failure(s) over 165 assertions`, exit 0 |
| `python3 -B verifiers/check_assertion_floors.py` | scratch copy w/ edit | 17 PASS, exit 0 |
| `python3 -B verifiers/check_assertion_floors.py` | lane root w/ edit | 17 PASS, exit 0 |
| `python3 -B verifiers/check_assertion_floors.py` | scratch copy at base | 15 PASS (no `spec_craft`/`sibling_reread` line), exit 0 |
| arm deleted from `check_spec_craft.py` + guard | scratch copy w/ edit | `FAIL spec_craft observed=247 floor=250`, exit 1 |
| registry floor lowered only (250→249) + guard | scratch copy w/ edit | `FAIL registry floor drift: spec_craft`, exit 2 |
| row dropped from both tables + guard | scratch copy w/ edit | `FAIL registry row vanish: spec_craft`, exit 2 |
| F6 anchor reverted to 15 + guard `--self-test` | scratch copy w/ edit | 2 failures over 165 assertions, exit 1 |
| `python3 -B verifiers/check_tip_battery.py --rev <D4 commit> --repo . --fleet ..` | fleet-shaped scratch | `guards 4 of 5` — `FAIL guard instrument-pin: … blob 9cb860bd… is not a pinned blob`; exit 1 |
| `python3 -B verifiers/check_tip_battery.py --rev b7f13f4… --repo . --fleet ..` | same scratch | `guards 5 of 5`; exit 1 (corpus gates red at base — F3) |

## Diff (exact, `git diff` of the two files at the lane)

```diff
diff --git i/verifiers/check_assertion_floors.py w/verifiers/check_assertion_floors.py
index 5034842..9cb860b 100644
--- i/verifiers/check_assertion_floors.py
+++ w/verifiers/check_assertion_floors.py
@@ -8,7 +8,12 @@ the recorded floor (harness 10, corpus_integrity 164, corpus_independent 105,
 surfaces 218, overlap_levers 51, checklist 1863, pins 62,
 harness_independent 123, compare_harness_independent 330, floors_guard 150,
 dispatch_prompts 56, sibling_census 68, alwayson 89, correction_sweep 25,
-scoped_rules_v32 240; round 65 (claim C1) registers scoped_rules_v32 at the
+scoped_rules_v32 240, spec_craft 250, sibling_reread 47; round 76 (hygiene
+repair D4 -- the round-74 spot-check's routed defect 4, item 4) floors the
+two round-74 counters whose self-tests were UNFLOORED, so an arm dropped
+from either file now reds this guard (the r62 F17 class, re-found by the
+r74 closure) instead of passing every gate silently; round 65 (claim C1)
+registers scoped_rules_v32 at the
 round-65 landed count (234) so the v32 pinning arms cannot be deleted with
 every gate green (r62 F17 re-found by RevC1Predicate Q2), and bumps checklist
 1852 -> 1862 (claim C2's governance-corrections battery: one positive arm,
@@ -180,6 +185,8 @@ EXPECTED_INSTRUMENTS = {
     "alwayson": 89,
     "correction_sweep": 25,
     "scoped_rules_v32": 240,
+    "spec_craft": 250,
+    "sibling_reread": 47,
 }
 SELF_TEST_TIMEOUT_S = 120
 # Round-56 routed defect 4 (round-55 spot-check, 'routed defects' item 4): the
@@ -240,6 +247,17 @@ INSTRUMENTS = {
     # one-word G9 witness and its supported-word control (234 -> 240).
     "scoped_rules_v32": ("verifiers/check_scoped_rules_v32.py", 240,
                          r"self-test:\s*(\d+) failure\(s\) over (\d+) assertions", 2, 1),
+    # Round 76 (D4 -- the r74 spot-check's routed defect 4, item 4): the two
+    # round-74 counters' self-tests were UNFLOORED, so an arm dropped from
+    # either file still read green with every gate passing -- the r62 F17
+    # class, re-found for these two instruments by the r74 closure. The floors
+    # are the landed counts: check_spec_craft.py --self-test 250 and
+    # check_sibling_reread.py --self-test 47 (r74 spot-check, 'routed
+    # defects' item 4; re-measured at the round-76 base, unchanged).
+    "spec_craft": ("verifiers/check_spec_craft.py", 250,
+                   r"self-test:\s*(\d+) failure\(s\) over (\d+) assertions", 2, 1),
+    "sibling_reread": ("verifiers/check_sibling_reread.py", 47,
+                       r"self-test:\s*(\d+) failure\(s\) over (\d+) assertions", 2, 1),
 }
@@ -819,10 +837,11 @@ def self_test() -> int:
         # F6 -- the registry's own declared size is load-bearing. The anchor is
         # the live registry's own declared total (round 49: 10; round 50: 11 with
         # sibling_census; round 51: 12 with overlap_levers; round 53: 13 with alwayson;
-        # round 58: 14 with correction_sweep; round 65: 15 with scoped_rules_v32),
+        # round 58: 14 with correction_sweep; round 65: 15 with scoped_rules_v32;
+        # round 76: 17 with spec_craft and sibling_reread),
         # including this guard's self-test); a stale literal here would stop landing
         # and the count-check would name it.
-        text = swap(registry_text, '"instrument_total": 15', '"instrument_total": 10',
+        text = swap(registry_text, '"instrument_total": 17', '"instrument_total": 10',
                     "F6/total")
         proc = run(write_tree(tmp / "f6", source, text), tmp / "f6")
         rec("F6 size drift: exit 2", proc.returncode == 2, proc.returncode)
diff --git i/verifiers/floors-registry.json w/verifiers/floors-registry.json
index ad0349f..005ffdb 100644
--- i/verifiers/floors-registry.json
+++ w/verifiers/floors-registry.json
@@ -1,6 +1,6 @@
 {
   "$comment": "Authoritative instrument registry for verifiers/check_assertion_floors.py (round-37 claim C2a, scout M7's HIGH). The guard's two in-file tables (EXPECTED_INSTRUMENTS, INSTRUMENTS) agree with each other by construction, so a coordinated edit -- the same row deleted from BOTH, a floor lowered in BOTH, a row path repointed -- was self-consistent and silent: the instrument stopped rerunning while the guard still printed all-PASS (scout M7, round 35; re-probed at 041f6ba by seat P5). This file is the anchor OUTSIDE the edited file: any disagreement fails loudly before a self-test runs, naming the class. BUMP-IN-STEP RULE: when a row's floor moves, edit this file, both in-file tables and the guard docstring in the same change; a half-bump now fa…
-  "instrument_total": 15,
+  "instrument_total": 17,
   "instruments": {
     "checklist": {
       "floor": 1863,
@@ -61,6 +61,14 @@
     "scoped_rules_v32": {
       "floor": 240,
       "path": "verifiers/check_scoped_rules_v32.py"
+    },
+    "spec_craft": {
+      "floor": 250,
+      "path": "verifiers/check_spec_craft.py"
+    },
+    "sibling_reread": {
+      "floor": 47,
+      "path": "verifiers/check_sibling_reread.py"
     }
   }
 }
```

(The registry `$comment` line is elided above only for width; it is byte-unchanged by this edit.)

## Scope discipline

Two files written, both named in the plan's touch list for this repair. No commit, branch, checkout,
stash or index write in the lane repo or the fleet root; the fleet root's tracked files
(`LOG.md`, `SCORECARD.md`, `MANIFEST.json`, …) were read only. `corpus/`, `SKILL.md`, `LOG.md`,
`SCORECARD.md`, `plans/`, `considerthese/`, `templates/`, `scripts/` and `.ufo/state/` were not
modified. No subagent dispatched. Scratch (`/fast/scratch/hyaku/kotoba-r76/B11RepairD4/`) is removed
before this seat yields. No tools were installed.

## Recommended next step for the L1

1. Land these two files as one change (registry + guard; the F6 anchor is part of the guard file,
   so the single commit carries it).
2. **Add the landed guard blob to `INSTRUMENT_PINS` in `verifiers/check_tip_battery.py`** (F1), the
   r72 precedent. Recompute the sha from the landed bytes — the blob named in this report
   (`9cb860bd…`) is the sha of the bytes as they stand now, not of the landed commit.
3. Route F3 (the corpus-index drift at the round-76 base) to whoever owns `corpus/README.md` and
   `verifiers/corpus-baseline.json`; the round-76 no-harm battery runs
   `verify_corpus_integrity.py --json` and will read red at the tip until that is repaired, for a
   reason that predates this wave.

VERDICT: D4 CLOSED — floors landed in one change (registry + both in-file tables + docstring + the
guard's F6 anchor), observed counts 250/47 equal the r74 spot-check's recorded values, the guard
now runs 17 instruments all PASS exit 0, and an arm deleted from either counter is now measured to
red the guard. Two adjacency findings for the L1: F1 the tip battery's `instrument-pin` guard needs
the landed guard blob added to its pin set (it reads 4 of 5 with this edit, 5 of 5 at base), and F3 a
pre-existing corpus-index drift at the round-76 base that makes the base-battery receipt's
"corpus integrity exit 0" unreproducible.
