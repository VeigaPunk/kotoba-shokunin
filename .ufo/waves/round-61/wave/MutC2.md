# MutC2 — mutation probe of `verifiers/check_routed_repairs.py` (C2 calibration counter)

- Seat: `kotoba-r61-wave-MutC2`, round 61 attempt 1 (hyaku run 5), 2026-10-23.
- Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin` — read-only to this seat. No
  lane/fleet/jj/git-index mutation was issued. Only read-only git reads (`show`,
  `rev-parse`, `log`) and the committed C2 base control rerun were executed.
- Scratch (untrusted, never cited as evidence itself):
  `/fast/scratch/hyaku/kotoba-r61/kotoba-r61-wave-MutC2/verifiers/`.
- My only lane write is this report (`…/.ufo/waves/round-61/wave/MutC2.md`).
- Installs: none (pacman paused host-wide; no tool was needed).

## 1. Target bytes and provenance

Measured bytes = committed HEAD blob = lane working copy:

```
$ sha256sum /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_routed_repairs.py
61d8c5831d1904cba921ccc547b8308753c1726e704d4cc2b5cec10d60c77356  .../verifiers/check_routed_repairs.py
$ git show HEAD:verifiers/check_routed_repairs.py | sha256sum
61d8c5831d1904cba921ccc547b8308753c1726e704d4cc2b5cec10d60c77356  -
$ git log --oneline -3 -- verifiers/check_routed_repairs.py
7827628 round-61: plan freeze (3 claims, frozen predicates), C2 routed-repairs counter + base control, census-before, v2 wave spec+dispatch (68 seats, 46 attack)
```

Provenance note (accuracy, not a defect): the checker does **not** exist at base
`f3246d1493b60ea1c0d947a19c39f9e08e92f326` (`git show f3246d14:verifiers/check_routed_repairs.py`
→ `fatal: path … exists on disk, but not in 'f3246d14…'`). It landed in the plan-freeze commit
`7827628`; the C2 base control is therefore a `--rev f3246d14` run *from the freeze revision*.
That control reproduces against committed base blobs:

```
$ python3 -B verifiers/check_routed_repairs.py --rev f3246d1493b60ea1c0d947a19c39f9e08e92f326
R-a count correction: missing
R-b landed-scope names: missing
R-c base-measure pointer: missing
R-d census-after file: missing
R-e byte-exact criterion + M91: missing
R-f controls-ancestry receipt: missing
routed repairs verified 0 of 6
exit=1
```

This matches the committed control receipt `.ufo/waves/round-61/controls/C2-base.txt`
(`routed repairs verified 0 of 6`, `base-exit=1`). Date of all runs: 2026-10-23, 19:10–19:13 UTC.

## 2. Detector (bounded, identical on pristine / mutated / restored)

```
python3 -B <scratch>/verifiers/check_routed_repairs.py --self-test
```

`--self-test` is handled in `main()` before any `git_show`/`rev-parse`, does no subprocess,
network, or file write; its stdout + exit code (0 = pass, 1 = any fixture arm fails) are the
whole detector. Scratch copies were made with `cp` from the committed bytes (hash above), so the
detector path is irrelevant to the result (nothing under `<script>/..` is read on the
`--self-test` path).

Pristine baseline (must pass, else the probe is inconclusive):

```
$ python3 -B pristine.py --self-test
self-test all-repairs: 6 of 6 (want 6) ok
self-test base-world: 0 of 6 (want 0) ok
self-test no-log: 3 of 6 (want 3) ok
self-test no-quality: 5 of 6 (want 5) ok
self-test without-round-61.md: 5 of 6 (want 5) ok
self-test without-census-after.txt: 5 of 6 (want 5) ok
self-test without-controls-ancestry.txt: 5 of 6 (want 5) ok
self-test ra-without-command: 5 of 6 (want 5) ok
self-test rb-missing: 5 of 6 (want 5) ok
self-test: 0 failure(s)
exit=0
```

Hash of pristine copy = `61d8c58…d77356` (same as lane bytes).

## 3. Results — one mutant per assigned point

| # | mutation | self-test | verdict | catching arm |
|---|---|---|---|---|
| m1 | delete R-a `claimed 32` test | `0 failure(s)` exit 0 | **SURVIVED** | none (finding F1) |
| m2 | delete R-c `C1-measure.txt` test | `0 failure(s)` exit 0 | **SURVIVED** | none (finding F2) |
| m3 | delete R-d `exit=0` tail check → `rd = census is not None` | `1 failure(s)` exit 1 | KILLED | `without-census-after.txt` (6 vs 5) |
| m4 | delete R-e `M91` test | `1 failure(s)` exit 1 | KILLED | `without-round-61.md` (6 vs 5) |
| m5 | delete R-f `merge-base --is-ancestor` test | `0 failure(s)` exit 0 | **SURVIVED** | none (finding F3) |
| m6 | R-a first `and` → `or` | `1 failure(s)` exit 1 | KILLED | `ra-without-command` (6 vs 5) |
| m7 | drop the base-world self-test arm | `0 failure(s)` exit 0 | **SURVIVED** | none (finding F4) |

Kill rate: 3 of 7. Four assigned mutants are not caught by the frozen self-test. Each is a
coverage finding; none shows the six checks scoring wrong on the existing fixtures.

### m1 — R-a `claimed 32` removed

```
@@ -68,7 +68,6 @@
     ra = (
         "build reports" in log
-        and "claimed 32" in log
         and "committed 29" in log
         and ".ufo/waves/round-60/build" in log
     )
```

```
self-test all-repairs: 6 of 6 (want 6) ok
self-test base-world: 0 of 6 (want 0) ok
self-test no-log: 3 of 6 (want 3) ok
self-test no-quality: 5 of 6 (want 5) ok
self-test without-round-61.md: 5 of 6 (want 5) ok
self-test without-census-after.txt: 5 of 6 (want 5) ok
self-test without-controls-ancestry.txt: 5 of 6 (want 5) ok
self-test ra-without-command: 5 of 6 (want 5) ok
self-test rb-missing: 5 of 6 (want 5) ok
self-test: 0 failure(s)
exit=0
```

### m2 — R-c `C1-measure.txt` removed

```
@@ -78,7 +78,7 @@
     rc = any(
-        "receipts/freeze2-selftest.txt" in line and "C1-measure.txt" in line
+        "receipts/freeze2-selftest.txt" in line
         for line in log.splitlines()
     )
```

```
self-test all-repairs: 6 of 6 (want 6) ok
self-test base-world: 0 of 6 (want 0) ok
self-test no-log: 3 of 6 (want 3) ok
self-test no-quality: 5 of 6 (want 5) ok
self-test without-round-61.md: 5 of 6 (want 5) ok
self-test without-census-after.txt: 5 of 6 (want 5) ok
self-test without-controls-ancestry.txt: 5 of 6 (want 5) ok
self-test ra-without-command: 5 of 6 (want 5) ok
self-test rb-missing: 5 of 6 (want 5) ok
self-test: 0 failure(s)
exit=0
```

### m3 — R-d `exit=0` tail check removed (killed)

```
@@ -84,12 +84,7 @@
-    rd = (
-        census is not None
-        and [ln for ln in census.splitlines() if ln.strip()][-1].strip() == "exit=0"
-        if census is not None
-        else False
-    )
+    rd = census is not None
```

```
self-test all-repairs: 6 of 6 (want 6) ok
self-test base-world: 0 of 6 (want 0) ok
self-test no-log: 3 of 6 (want 3) ok
self-test no-quality: 5 of 6 (want 5) ok
self-test without-round-61.md: 5 of 6 (want 5) ok
self-test without-census-after.txt: 6 of 6 (want 5) FAIL
self-test without-controls-ancestry.txt: 5 of 6 (want 5) ok
self-test ra-without-command: 5 of 6 (want 5) ok
self-test rb-missing: 5 of 6 (want 5) ok
self-test: 1 failure(s)
exit=1
```

### m4 — R-e `M91` removed (killed)

```
@@ -97,7 +97,6 @@
         "Q56" in quality
         and "byte-exact" in quality
         and lesson is not None
-        and "M91" in lesson
     )
```

```
self-test all-repairs: 6 of 6 (want 6) ok
self-test base-world: 0 of 6 (want 0) ok
self-test no-log: 3 of 6 (want 3) ok
self-test no-quality: 5 of 6 (want 5) ok
self-test without-round-61.md: 6 of 6 (want 5) FAIL
self-test without-census-after.txt: 5 of 6 (want 5) ok
self-test without-controls-ancestry.txt: 5 of 6 (want 5) ok
self-test ra-without-command: 5 of 6 (want 5) ok
self-test rb-missing: 5 of 6 (want 5) ok
self-test: 1 failure(s)
exit=1
```

### m5 — R-f `merge-base --is-ancestor` removed

```
@@ -104,7 +104,6 @@
     rf = (
         ancestry is not None
-        and "merge-base --is-ancestor" in ancestry
         and "exit 0" in ancestry
     )
```

```
self-test all-repairs: 6 of 6 (want 6) ok
self-test base-world: 0 of 6 (want 0) ok
self-test no-log: 3 of 6 (want 3) ok
self-test no-quality: 5 of 6 (want 5) ok
self-test without-round-61.md: 5 of 6 (want 5) ok
self-test without-census-after.txt: 5 of 6 (want 5) ok
self-test without-controls-ancestry.txt: 5 of 6 (want 5) ok
self-test ra-without-command: 5 of 6 (want 5) ok
self-test rb-missing: 5 of 6 (want 5) ok
self-test: 0 failure(s)
exit=0
```

### m6 — R-a first `and` → `or` (killed)

```
@@ -68,7 +68,7 @@
     ra = (
         "build reports" in log
-        and "claimed 32" in log
+        or "claimed 32" in log
         and "committed 29" in log
         and ".ufo/waves/round-60/build" in log
     )
```

(Python precedence: this reads `A or (B and C and D)`, so the dropped counting-path clause is
bypassed whenever `build reports` appears.)

```
self-test all-repairs: 6 of 6 (want 6) ok
self-test base-world: 0 of 6 (want 0) ok
self-test no-log: 3 of 6 (want 3) ok
self-test no-quality: 5 of 6 (want 5) ok
self-test without-round-61.md: 5 of 6 (want 5) ok
self-test without-census-after.txt: 5 of 6 (want 5) ok
self-test without-controls-ancestry.txt: 5 of 6 (want 5) ok
self-test ra-without-command: 6 of 6 (want 5) FAIL
self-test rb-missing: 5 of 6 (want 5) ok
self-test: 1 failure(s)
exit=1
```

### m7 — base-world arm dropped

```
@@ -182,7 +182,6 @@
     }
     expect("all-repairs", world, 6)
-    expect("base-world", {k: None for k in world}, 0)
     expect("no-log", {**world, "LOG.md": None}, 3)
```

```
self-test all-repairs: 6 of 6 (want 6) ok
self-test no-log: 3 of 6 (want 3) ok
self-test no-quality: 5 of 6 (want 5) ok
self-test without-round-61.md: 5 of 6 (want 5) ok
self-test without-census-after.txt: 5 of 6 (want 5) ok
self-test without-controls-ancestry.txt: 5 of 6 (want 5) ok
self-test ra-without-command: 5 of 6 (want 5) ok
self-test rb-missing: 5 of 6 (want 5) ok
self-test: 0 failure(s)
exit=0
```

## 4. Findings and fixes (all four survivors become killable)

The fix is confined to `self_test()`'s fixture arm set plus an arm-count guard; the frozen six
checks (`check_repairs`) are untouched. This was verified: the candidate patch diff touches only
`self_test` (`@@ -155,8 +155,11 @@` and `@@ -207,6 +210,27 @@`). Candidate text (draft for the L1; **not**
applied to the lane):

```diff
--- verifiers/check_routed_repairs.py
+++ verifiers/check_routed_repairs.py (draft hardening)
@@ -155,8 +155,11 @@
     """Fixture arms: each repair absent -> count drops; base world -> 0 of 6."""
     failures = 0
 
+    arms = 0
+
     def expect(name: str, blobs: dict[str, str | None], want: int) -> None:
-        nonlocal failures
+        nonlocal failures, arms
+        arms += 1
         got, _ = check_repairs(blobs)
@@ -207,6 +210,27 @@
     expect("rb-missing", {**world, "LOG.md": log_without_rb}, 5)
 
+    log_without_ra_count = (
+        "round-60 build reports claimed 31 committed 29 "
+        "(`ls .ufo/waves/round-60/build | wc -l`)\n"
+        "landed scope names plans/round-60.md and considerthese/2026-10-23.md\n"
+        "erratum: base measurement is receipts/freeze2-selftest.txt not C1-measure.txt\n"
+    )
+    expect("ra-without-count", {**world, "LOG.md": log_without_ra_count}, 5)
+
+    log_without_rc_pointer = full_log.replace(" not C1-measure.txt", "")
+    expect("rc-without-c1-pointer", {**world, "LOG.md": log_without_rc_pointer}, 5)
+
+    expect(
+        "ancestry-without-merge-base",
+        {**world, ".ufo/waves/round-61/receipts/controls-ancestry.txt": "exit 0\n"},
+        5,
+    )
+
+    if arms != 12:
+        failures += 1
+        print(f"self-test arm-count: {arms} (want 12) FAIL")
+
     print(f"self-test: {failures} failure(s)")
```

Mapping of finding → catching arm → demonstration:

- **F1 (m1 survived):** the counter never requires the literal `claimed 32`; a LOG line saying
  `claimed 31 committed 29` would count R-a as repaired. Fix: `ra-without-count` arm (want 5).
- **F2 (m2 survived):** R-c collapses to "any line mentions `receipts/freeze2-selftest.txt`";
  the pointer-disambiguation requirement (`C1-measure.txt` on the same line) is unguarded.
  Fix: `rc-without-c1-pointer` arm (want 5).
- **F3 (m5 survived):** R-f passes on any ancestry receipt containing `exit 0`, e.g. an
  unrelated command transcript; the `merge-base --is-ancestor` invocation is unguarded.
  Fix: `ancestry-without-merge-base` arm (want 5).
- **F4 (m7 survived):** the self-test has no arm-count invariant, so deleting an arm is
  invisible. Fix: `arms != 12` guard. All four survivors are then killed:

```
$ python3 -B hardened.py --self-test
... (12 arms, all ok) ...
self-test: 0 failure(s)
exit=0

$ python3 -B h1.py --self-test   # hardened + m1
self-test ra-without-count: 6 of 6 (want 5) FAIL
self-test: 1 failure(s)
exit=1

$ python3 -B h2.py --self-test   # hardened + m2
self-test rc-without-c1-pointer: 6 of 6 (want 5) FAIL
self-test: 1 failure(s)
exit=1

$ python3 -B h5.py --self-test   # hardened + m5
self-test ancestry-without-merge-base: 6 of 6 (want 5) FAIL
self-test: 1 failure(s)
exit=1

$ python3 -B h7.py --self-test   # hardened + m7
self-test arm-count: 11 (want 12) FAIL
self-test: 1 failure(s)
exit=1
```

Full hardened baseline output (shows the three new arms pass on pristine bytes, so the additions
do not encode the mutation):

```
self-test all-repairs: 6 of 6 (want 6) ok
self-test base-world: 0 of 6 (want 0) ok
self-test no-log: 3 of 6 (want 3) ok
self-test no-quality: 5 of 6 (want 5) ok
self-test without-round-61.md: 5 of 6 (want 5) ok
self-test without-census-after.txt: 5 of 6 (want 5) ok
self-test without-controls-ancestry.txt: 5 of 6 (want 5) ok
self-test ra-without-command: 5 of 6 (want 5) ok
self-test rb-missing: 5 of 6 (want 5) ok
self-test ra-without-count: 5 of 6 (want 5) ok
self-test rc-without-c1-pointer: 5 of 6 (want 5) ok
self-test ancestry-without-merge-base: 5 of 6 (want 5) ok
self-test: 0 failure(s)
exit=0
```

Residual on F4's fix, declared: the arm-count guard is itself part of `self_test()`, so a
two-point mutant that deletes both the guard and an arm still survives `--self-test`. The
do-nothing control is nevertheless exercised independently by the committed C2 base control
(`--rev f3246d14` → `0 of 6`, exit 1, pasted in §1). If the L1 adopts the guard, it should not
be described as tamper-proof.

## 5. Calibration reading (what this means for C2, not a contract change)

- C2's measured sentence is the counter's own `6 of 6` output. The frozen self-test is the only
  in-repo guard that the counter still discriminates; as committed it is blind to three
  single-substring removals and to arm removal. A repair whose count digits are wrong (F1), whose
  pointer line drops the `C1-measure.txt` disambiguation (F2), or whose ancestry receipt lacks the
  `merge-base --is-ancestor` invocation (F3) would still score as repaired.
- The three killed mutants show the fixture set does bite where it has an arm (`census exit=0`,
  lesson `M91`, AND→OR). There is no evidence of a mis-scoring check; the gap is fixture coverage.
- Recommendation to the L1 (integrator decides): either adopt the §4 arm additions when freezing
  the counter, or record the four coverage gaps in the round's honesty line. Do not weaken or
  reinterpret the frozen six repair definitions.

## 6. Restoration evidence

```
$ sha256sum check_routed_repairs.py( lane ) pristine.py restored.py hardened.py
61d8c5831d1904cba921ccc547b8308753c1726e704d4cc2b5cec10d60c77356  lane:verifiers/check_routed_repairs.py
61d8c5831d1904cba921ccc547b8308753c1726e704d4cc2b5cec10d60c77356  pristine.py
61d8c5831d1904cba921ccc547b8308753c1726e704d4cc2b5cec10d60c77356  restored.py
$ cmp pristine.py restored.py && echo ok
ok
$ python3 -B restored.py --self-test | tail -2
self-test rb-missing: 5 of 6 (want 5) ok
self-test: 0 failure(s)
exit=0
```

Lane file hash before the probe and after all runs: `61d8c58…d77356` (identical; §1 and final
`sha256sum` at 19:12:34 UTC). Scratch mutants m1–m7 remain in scratch only; scratch is untrusted
and is not evidence. No `git`/`jj` write, no `--fetch`, no dispatch, no lane file edited.

## 7. Close

- Installs: none.
- Blockers: none.
- Attacked the C2 calibration counter by deleting five substring tests (R-a `claimed 32`,
  R-c `C1-measure.txt`, R-d `exit=0`, R-e `M91`, R-f `merge-base --is-ancestor`), flipping R-a's
  AND to OR, and dropping the base-world arm — 3 of 7 mutants killed by `--self-test`, 4 survive
  (findings F1–F4) and are killed by the §4 fixture/arm-count additions, demonstrated on hardened
  scratch copies.
