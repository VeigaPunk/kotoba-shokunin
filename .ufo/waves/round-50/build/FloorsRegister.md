# FloorsRegister — round-50 build seat (D3, last clause)

**Result: the registration the item asked for is DONE and integrated by the L1 (not by me);
my residual deliverable — the guard's own F30–F33 battery that makes the new row's
half-bump shapes fail loudly — is delivered as a patch that applies cleanly on top of the
L1's tree.**

**Files changed by this seat:** `verifiers/check_assertion_floors.py`,
`verifiers/floors-registry.json` (both in a private clone only; the lane checkout was never
written by me). **Patch:** `/fast/scratch/hyaku/kotoba-r50/build/FloorsRegister/patch.diff`
(diff against the L1's integrated commit `956ee16`; `git apply --check` OK, verified on a
fresh clone).

---

## 1. What the item asked, and what is now true

D3's last clause: `verifiers/check_sibling_census.py` was not in
`verifiers/floors-registry.json`; register it as instrument `sibling_census` in the registry
AND in both in-file tables of `verifiers/check_assertion_floors.py`, following the registry's
BUMP-IN-STEP rule (`instrument_total` 10 → 11).

**Status: satisfied at the L1's tree (`956ee16`, `git log --oneline -3` confirms the landing
commit `542f515`).** The lane's registry now reads:

```
instrument_total: 11
  checklist 1851 verifiers/verify_skill_checklist.py
  compare_harness_independent 330 verifiers/compare_harness_independent.py
  corpus_independent 91 verifiers/verify_corpus_independent.py
  corpus_integrity 150 verifiers/verify_corpus_integrity.py
  dispatch_prompts 56 verifiers/verify_dispatch_prompts.py
  floors_guard 150 verifiers/check_assertion_floors.py
  harness 10 verifiers/verify_harness_claims.py
  harness_independent 123 verifiers/verify_harness_independent.py
  pins 62 verifiers/check_substrate_pins.py
  sibling_census 68 verifiers/check_sibling_census.py
  surfaces 99 verifiers/verify_surfaces.py
```

(measured by `python3 -c "import json;d=json.load(open('verifiers/floors-registry.json'));…"`
at the lane HEAD.)

**The floor value differs from the item's instruction, and the difference is correct.** The
item said to use the count the base `check_sibling_census.py --self-test` prints at
`f30464660c675d1c1e2851a3bf0366a3aaffe5a8`. I measured that: **44 assertions** (below). But
the item also said another seat is adding self-test arms to that instrument and that the L1
raises the floor at integration — and that is what happened: the census seat's arms landed
with the L1's integration, so at `956ee16` the same command prints **68 assertions**, and the
L1 registered floor **68**. A floor of 44 would have been below the observed count and would
have under-registered the instrument. The L1's choice is the correct one.

I did not touch `verifiers/check_sibling_census.py` at any point (measured, never edited), as
the item required.

## 2. Measurements

All commands run in a private clone at `f30464660c675d1c1e2851a3bf0366a3aaffe5a8`
(`/fast/scratch/hyaku/kotoba-r50/build/FloorsRegister/lane`), except where a tree is named.

**Base (f3046466), before my edits:**

| command | output | exit |
|---|---|---|
| `python3 -B verifiers/check_sibling_census.py --self-test` | `self-test: 0 failure(s) over 44 assertions` | 0 |
| `python3 -B verifiers/check_assertion_floors.py` | 10 × `PASS` (harness 10, corpus_integrity 150, corpus_independent 91, surfaces 99, checklist 1845, pins 62, harness_independent 123, compare_harness_independent 330, floors_guard 150, dispatch_prompts 32) | 0 |
| `python3 -B verifiers/check_assertion_floors.py --self-test` | `0 failure(s) over 150 assertions` | 0 |

**At the L1's tree (`956ee16`) — my patch applied:**

| command | output | exit |
|---|---|---|
| `python3 -B verifiers/check_sibling_census.py --self-test` | `self-test: 0 failure(s) over 68 assertions` | 0 |
| `python3 -B verifiers/check_assertion_floors.py` | 11 × `PASS` … `floors_guard observed=169 floor=169`, `sibling_census observed=68 floor=68` | 0 |
| `python3 -B verifiers/check_assertion_floors.py --self-test` | `0 failure(s) over 169 assertions` | 0 |

The census row's summary shape is the sibling-census instrument's own
`self-test: N failure(s) over M assertions`; the guard parses it with
`r"self-test:\s*(\d+) failure\(s) over (\d+) assertions"` (count group 2), the same pattern the
`harness` / `corpus_integrity` rows use.

## 3. Planted-mismatch check (the item's explicit test)

The item asked me to plant a registry/table mismatch and confirm it fails. I planted three
shapes on the L1's tree (patched with my battery) and reverted each; every one exits **2**
with the class and the row named, and no instrument reran.

**(a) floor lowered in the registry only** (`verifiers/floors-registry.json`
`"floor": 68` → `67`; both in-file tables left at 68):

```
$ python3 -B verifiers/check_assertion_floors.py
FAIL registry floor drift: sibling_census registry=67 expected=68 row=68
EXIT=2
```

**(b) the census row deleted from BOTH in-file tables** while the registry still names it
(the row-vanish shape — the coordinated-deletion class this guard exists to catch):

```
$ python3 -B verifiers/check_assertion_floors.py
FAIL registry row vanish: sibling_census (listed in verifiers/floors-registry.json, absent from both guard tables)
EXIT=2
```

**(c) floor lowered in one in-file table only** (`EXPECTED_INSTRUMENTS` 68 → 67; the registry
left at 68) — planted on my own clone, same shape as (a) but through the in-file table
channel, so both drift lines name the row:

```
$ python3 -B verifiers/check_assertion_floors.py
FAIL registry floor drift: sibling_census floor=68 expected=67
FAIL registry floor drift: sibling_census registry=68 expected=67 row=68
EXIT=2
```

## 4. What my patch adds, and why

The registration itself is the L1's. My patch adds the part that was still missing and that
the round-38 precedent (F14/F15, added when `harness_independent` was registered) shows the
guard wants: **the guard's own self-test battery for the newly registered row**. Without it,
nothing in the guard's fixture battery exercised `sibling_census` — the row was registered but
not *guarded against its own half-bumps*, which is exactly the class (a coordinated or
one-sided edit that is self-consistent and silent) the anchor was built to catch.

Four new arms, **F30–F33**, all in a **hermetic one-instrument world** (a stub at the
declared path printing the census summary) so each arm is a true discriminator and the
battery stays fast:

- **F30 — control.** The same world with no drift: must exit 0 and print
  `PASS sibling_census observed=N floor=N`. Every arm below is measured against a world that
  really would pass, so a green arm means the drift check fired, not that the world was
  broken.
- **F31 — the row absent from the registry** while both in-file tables carry it (the D3
  defect shape, reversed): exit 2, `FAIL registry extra row: sibling_census`.
- **F32a — floor lowered in the registry only**: exit 2, `FAIL registry floor drift: sibling_census`.
- **F32b — floor lowered in one in-file table only**: exit 2, `FAIL registry floor drift: sibling_census`.
- **F33 — the row's path repointed at another instrument**: exit 2,
  `FAIL registry path drift: sibling_census`. The target is chosen to be *genuinely silent*
  without the anchor (the stub prints the same summary shape above the census floor), so the
  arm would read `PASS` and exit 0 if the anchor check were removed.

Each arm also asserts that **no instrument reran** (`PASS ` absent from stdout) and that the
failure is class- and row-named.

**In-step floor bump (BUMP-IN-STEP rule).** The guard's own self-test count moved 150 → 169
because of the new arms, so `floors_guard` is re-bumped **150 → 169 in all four carriers**:
`verifiers/floors-registry.json` (the external anchor), `EXPECTED_INSTRUMENTS`,
`INSTRUMENTS`, and the guard docstring's floor list. A half-bump would fail loudly on the
side that was missed.

**Patch scope:** `verifiers/check_assertion_floors.py` (+110/−4) and
`verifiers/floors-registry.json` (+1/−1). The registry edit is the `floors_guard` 150 → 169
re-bump only — the `sibling_census` entry and `instrument_total: 11` are the L1's, already in
the tree the patch is based on, so the patch applies without touching them.

**Verification of the patch itself:** `git apply --check` OK against a fresh clone of
`956ee16`; after applying, `--self-test` → `0 failure(s) over 169 assertions` (exit 0) and the
full guard → 11 × `PASS` (exit 0).

## 5. Findings worth recording

1. **The floor must be measured where it will be read.** The item's stated floor (44, the
   base count) was superseded by the census seat's arms before integration; the L1 registered
   68, the count at the integrated tree. A floor set from a stale measurement is a floor that
   under-registers — the guard would print `observed=68 floor=44` and stay green while the
   floor no longer described the instrument. **The floor must be re-measured at the tree the
   row lands on**, not carried over from the base commit.
2. **The anchor was the only thing standing between "registered" and "guarded".** The
   registration alone (registry + two tables) makes the *current* state correct, but leaves
   the new row unexercised by the guard's own battery — the newest row is where a later
   half-bump is likeliest (the round-38 F14/F15 precedent says exactly this). The delivered
   F30–F33 arms close that gap for `sibling_census`.
3. **The guard's fixture battery must stay hermetic.** My first attempt at F30–F32 ran the
   live eleven-instrument world, and the guard's 120 s per-instrument timeout killed the
   self-test (`TimeoutExpired` after 120 s, exit 1) because the repoint arm's mutation
   no-op'd (my literal anchor did not match the file's bytes — the file spells the summary
   pattern `failure\(s\)`, and the anchor I wrote did not) and the guard then ran the whole
   live set. The fix: backslash-free anchors plus one-instrument stub worlds. The battery now
   runs in **1.1 s** (was 120 s+ and failing). Worth recording as a guard-hygiene rule: a
   fixture arm that mutates the *live* world inherits the live world's cost.
4. **Byte-exact anchors, not eyeballed ones.** The mismatch in (3) was invisible in every
   rendered view of the file (the tool output normalises `\)` to `)`); only an ord-code dump
   of the actual bytes showed the difference. The guard's own `swap()` helper already warns
   about this ("a joined anchor must not appear anywhere else in this file's own text") —
   the same class of hazard applies to the anchor *text itself*.

## 6. Risks / boundaries

- The patch is based on the L1's integrated commit `956ee16`, not on `f3046466`: the
  registration the item asked for is already in that tree. If the L1 prefers a
  `f3046466`-based diff, the arms and the `floors_guard` re-bump port verbatim onto the base
  guard file — but the `sibling_census` floor must then be **68** (or whatever the census
  count is at the landing tree), never 44.
- The `floors_guard` floor 169 is coupled to the arm count. If the L1 drops any arm, the
  floor must be re-measured and re-bumped in all four carriers in the same change.
- **Nothing in the lane checkout was written by this seat.** Every mutation above happened in
  a private clone under `/fast/scratch/hyaku/kotoba-r50/build/FloorsRegister/`; the lane's
  `verifiers/check_sibling_census.py` was measured and never edited.
- No tool was installed or upgraded for this item (none needed; `python3` 3.14 and `git` from
  the base image sufficed).

## 7. Commands the L1 should run after integration

```
python3 -B verifiers/check_assertion_floors.py            # expect 11 × PASS, exit 0
python3 -B verifiers/check_assertion_floors.py --self-test # expect 0 failure(s) over 169 assertions, exit 0
python3 -B verifiers/check_sibling_census.py --self-test   # expect the count the floor names, exit 0
```
