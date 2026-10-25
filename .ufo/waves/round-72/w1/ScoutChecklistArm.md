# ScoutChecklistArm — round-72 wave 1 (build)

**Verdict: stale real-repo arm; corrected expectation specified; regression shapes verified in a scratch fleet-shaped sandbox; assertion count unchanged at 1862; exact diff to land below (not applied — lane untouched).**

## 1. Arm location

`verifiers/verify_skill_checklist.py` (`self_test()`):

- `rec("governance: live round-65 corrections land, only LOG.md:2678 red", …)` — lines **2522–2525**; preceding explanatory comment lines 2515–2518.
- The relevant module constants: `GOVERNANCE_ERRATA_HORIZON = 2678` (line 400); the r71 errata row `(2678, "d7f442…", ".ufo/waves/round-67/w1/controls/junk-world/", "Routed defect R67-3 (disclosure)")` (lines 406–415); `GOVERNANCE_CORRECTIONS_HORIZON = 2723` with 4 correction rows (lines 425–444: LOG.md:2619, 2620, 2621, 2723).

## 2. What the arm was written to assert (round 65 → now)

Git history of the arm (`git log -L 2515,2525:verifiers/verify_skill_checklist.py`; `git log -S "live round-65 corrections land"`):

| commit | round | arm asserted |
|---|---|---|
| `80bb892` | 65 | `"governance: live round-65 corrections land, check PASS"` → `status == "PASS" and "3 recorded correction(s) excused" in detail` (three round-65 rows excuse three base reds; floors 1852→1862 registered in the same commit) |
| `8edeb49` | 70 C2 | same name, `"5 recorded correction(s) excused"` (two round-70 rows added) |
| `4dba3bc` | 70 wave-1 | LOG.md:2678 correction row **withdrawn** (M118/Q64, laundering); arm flipped to `"governance: live round-65 corrections land, only LOG.md:2678 red"` → `status == "FAIL" and "4 recorded correction(s) excused" in detail and "LOG.md:2678" in detail and "LOG.md:2676" not in detail`. Comment: LOG.md:2678 names a removed directory with no replacement address, which a correction may not carry, so the check stays FAIL on it. |
| `bf98d28` | 71 | r71 **errata** row appended for LOG.md:2678 (recorded absence of the removed `junk-world/` mirror; gate horizon 2315→2678). Live check now excuses LOG.md:2678 via that errata row → returns PASS → the round-70 arm (expecting FAIL) breaks. |

## 3. Live gate now (failures reproduce identically in sandbox)

`python3 -B verifiers/verify_skill_checklist.py --self-test` (lane root) → exit 1:

```
self-test FAIL: governance: live round-65 corrections land, only LOG.md:2678 red: got ('PASS', 1272, '1272 governance citation token(s) resolve across 2 files; 10 quoted meta-finding(s), 3 schematic token(s) excluded, 2 recorded absence(s) excused, 4 recorded correction(s) excused')
1 failure(s) over 1862 assertions
```

The live CLI check agrees: `python3 -B verifiers/verify_skill_checklist.py --json` → `{'status': 'PASS', 'evaluated': 1272, 'id': 'governance.citation_resolves', 'detail': '1272 governance citation token(s) resolve across 2 files; 10 quoted meta-finding(s), 3 schematic token(s) excluded, 2 recorded absence(s) excused, 4 recorded correction(s) excused'}`.

## 4. Corrected expectation

The arm must now assert the r71 state: both errata rows (LOG.md:2111 post-r44-hunt.py; LOG.md:2678 junk-world/) **and** all four corrections land, so the live check **PASSes** with no red subject:

```python
rec("governance: live round-65 corrections and r71 errata land",
    status == "PASS" and "2 recorded absence(s) excused" in detail
    and "4 recorded correction(s) excused" in detail
    and "LOG.md:2678" not in detail and "LOG.md:2676" not in detail,
    (status, evaluated, detail))
```

## 5. Regression shape (still FAILS when the errata row is removed / horizon lowered)

The corrected arm runs `check_governance_citations(Path(__file__).resolve().parent.parent, corrections=GOVERNANCE_CORRECTIONS)` with the **default** `errata=GOVERNANCE_ERRATA` / `horizon=GOVERNANCE_ERRATA_HORIZON`, so it is inherently sensitive to both mutants. Verified in a scratch fleet-shaped sandbox (`P=$(mktemp -d /tmp/k72fleet-ScoutChecklistArm.XXXX)`; symlinks for every fleet-root entry **including dotfiles** `.ufo`, `.ufo-scratch`; `git clone --shared -q` of the lane at `e61fd29`; `git rev-parse --show-toplevel` == `$P/kotoba-shokunin`; the c69711e→HEAD diff for `verify_skill_checklist.py`/`LOG.md` is empty). All runs: `python3 -B verifiers/verify_skill_checklist.py --self-test`.

| world | exit | self-test output |
|---|---|---|
| unmutated (corrected arm) | 0 | `0 failure(s) over 1862 assertions` |
| **mutant A** — r71 errata row `(2678, …)` removed from `GOVERNANCE_ERRATA` | 1 | `self-test FAIL: governance: live round-65 corrections and r71 errata land: got ('FAIL', 1273, "LOG.md:2678: '.ufo/waves/round-67/w1/controls/junk-world/' does not resolve from /tmp/k72fleet-ScoutChecklistArm.SxRw/kotoba-shokunin; 10 quoted meta-finding(s), 3 schematic token(s) excluded, 1 recorded absence(s) excused, 4 recorded correction(s) excused")` |
| **mutant B** — `GOVERNANCE_ERRATA_HORIZON` 2678→2677 | 1 | `self-test FAIL: governance: live round-65 corrections and r71 errata land: got ('FAIL', 1273, "erratum LOG.md:2678 '.ufo/waves/round-67/w1/controls/junk-world/' is past horizon 2677 or absent; LOG.md:2678: '.ufo/waves/round-67/w1/controls/junk-world/' does not resolve from /tmp/k72fleet-ScoutChecklistArm.SxRw/kotoba-shokunin; 10 quoted meta-finding(s), 3 schematic token(s) excluded, 1 recorded absence(s) excused, 4 recorded correction(s) excused")` |

Both mutants yield exactly one failing assertion (the corrected arm) and keep the total at 1862. (The `quote` bytes for the row: line 2678 carries `Routed defect R67-3 (disclosure)` — `sed -n '2678p' LOG.md` = `- **Routed defect R67-3 (disclosure).** `.ufo/waves/round-67/w1/controls/junk-world/` — a 254 MB` — 9 words; dropped: `untracked control mirror — was left in the lane working tree …` remainder. Line 2676: `  `.ufo/waves/round-67/w1/controls/census-validate-append.txt`; the file that exists is` — 11 words; dropped: `  …` continuation. Line 2723: `  - LOG.md:2676 token ".ufo/waves/round-67/w1/controls/census-validate-append.txt" -> ".ufo/waves/round-67/controls/census-validate-append.txt" (the r67 census receipt sits directly under controls/, as the R67-2 erratum on that line says).` — 22 words; dropped: none except trailing newline. Digests verified byte-exact against the row pins: 2678 `d7f442ed…c510`, 2723 `a2b5c003…35be`, 2111 `7dcbf123…0135`, 2619/2620/2621 `b11e4e8e…`, `1dcb9d9e…`, `6836c34a…`.)

## 6. Assertion count before/after (1862 floor)

- Before (live, unmutated lane): `1 failure(s) over 1862 assertions` — observed 1862 = floor 1862, floor guard red (`self_test_failures=1`).
- After (corrected arm): `0 failure(s) over 1862 assertions` — observed 1862 = floor 1862; the corrected arm keeps the rec count (one rec replaces one rec), so **no floor bump is needed**.
- `python3 -B verifiers/check_assertion_floors.py` in the sandbox with the corrected arm: exit 0, all 15 instruments PASS, including `PASS checklist observed=1862 floor=1862`.

## 7. Exact diff to land (produced in the sandbox clone; lane not edited)

```diff
--- a/verifiers/verify_skill_checklist.py
+++ b/verifiers/verify_skill_checklist.py
@@ -2512,16 +2512,20 @@ def self_test() -> int:
             status == "FAIL" and "corpus/other-dead.md" in detail
             and "1 recorded correction(s) excused" in detail,
             (status, evaluated, detail))
-        # live corrections land against the real repo: the three round-65
-        # rows and the round-70 row (K69-11, LOG.md:2676) excuse four reds;
-        # LOG.md:2678 names a removed directory with no replacement address,
-        # which a correction may not carry, so the check stays FAIL on it.
+        # Round 71 (routed defect K69-11 closure): LOG.md:2678 records
+        # R67-3's disclosure -- the removed control mirror `junk-world/`
+        # has no resolving replacement, so a correction may not carry it;
+        # the r71 errata row (recorded absence) now excuses it.  Live
+        # state: both errata rows and all four corrections land -> PASS;
+        # dropping or lowering the 2678 errata row must re-redden
+        # LOG.md:2678.
         status, evaluated, detail = check_governance_citations(
             Path(__file__).resolve().parent.parent,
             corrections=GOVERNANCE_CORRECTIONS)
-        rec("governance: live round-65 corrections land, only LOG.md:2678 red",
-            status == "FAIL" and "4 recorded correction(s) excused" in detail
-            and "LOG.md:2678" in detail and "LOG.md:2676" not in detail,
+        rec("governance: live round-65 corrections and r71 errata land",
+            status == "PASS" and "2 recorded absence(s) excused" in detail
+            and "4 recorded correction(s) excused" in detail
+            and "LOG.md:2678" not in detail and "LOG.md:2676" not in detail,
             (status, evaluated, detail))
```

## 8. Notes

- The sandbox reproduction required the fleet shape exactly as `check_r69_routed_repairs_v2.py` builds it (lines 176–201): symlink **every** parent entry including dotfiles `.ufo` / `.ufo-scratch` (my first sandbox missed dotfiles; without them `../.ufo/reports/…` corrected tokens fail to resolve and the world is not the live one).
- Scratch cleanup: sandbox `$P` and all `/tmp/k72-*` scratch files deleted after evidence capture. No lane file was modified; no git writes performed.
