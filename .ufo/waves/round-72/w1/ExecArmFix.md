# ExecArmFix — round 72 wave 1: repair of the stale checklist self-test arm (C3 consistency)

**Verdict: PROVEN.** The red is real at base `c69711e`; the repair makes the arm assert the true live
state (governance PASS with two errata-excused absences and four corrections excused) and adds one
regression assertion that fails on both required mutants; the checklist floor must be raised
**1862 → 1863** in step (registry + both in-file tables + guard docstring); `check_assertion_floors.py`
exits 0 at 1863 and `verify_skill_checklist.py` exits 0 (11/11 PASS). Nothing committed was modified;
all work happened in `--shared` clones at base and the deliverables live under
`.ufo/waves/round-72/w1/build/ExecArmFix/`.

Sandbox construction (every run below, from the lane root; `P` a fresh `mktemp -d`):

```
for e in /home/vgpnk/Projects/shokunin/* /home/vgpnk/Projects/shokunin/.[!.]*; do
  b=$(basename "$e"); [ "$b" = kotoba-shokunin ] && continue; ln -s "$e" "$P/$b"; done
git clone --shared -q /home/vgpnk/Projects/shokunin/kotoba-shokunin $P/kotoba-shokunin
git -C $P/kotoba-shokunin checkout -q c69711ee08279609374d895bb0f3c8c18ccf15c9
git -C $P/kotoba-shokunin rev-parse HEAD   # -> c69711ee08279609374d895bb0f3c8c18ccf15c9
```

Lane tip observed: `git -C …/kotoba-shokunin rev-parse HEAD` → `e61fd294c2e1cdd16d594b57b310254183ace1e7`;
`git diff --name-only c69711e… HEAD` → 24 paths, 23 under `.ufo/` plus `plans/round-72.md`; no path
under `verifiers/` differs from base, so base reproduction is faithful to the live tree.

## 1. Base reproduction (do-nothing control) — red, exit 1

```
$ python3 -B verifiers/verify_skill_checklist.py --self-test
self-test FAIL: governance: live round-65 corrections land, only LOG.md:2678 red: got ('PASS', 1272, '1272 governance citation token(s) resolve across 2 files; 10 quoted meta-finding(s), 3 schematic token(s) excluded, 2 recorded absence(s) excused, 4 recorded correction(s) excused')
1 failure(s) over 1862 assertions
$ echo $?
1
```

```
$ python3 -B verifiers/check_assertion_floors.py
FAIL checklist observed=1862 floor=1862 self_test_failures=1
$ echo $?
1
```

Quotes (≤25 words, copied from the pasted bytes; the rest of each line is named as dropped):
- `2 recorded absence(s) excused, 4 recorded correction(s) excused')` — dropped: the line prefix
  `self-test FAIL: … got ('PASS', 1272, '1272 governance citation token(s) resolve across 2 files;`
  and the middle `10 quoted meta-finding(s), 3 schematic token(s) excluded,`.
- `1 failure(s) over 1862 assertions` (whole line).
- `FAIL checklist observed=1862 floor=1862 self_test_failures=1` (whole line).

The plain gate was already green at base, so the red is the stale arm alone, not the gate:

```
$ python3 -B verifiers/verify_skill_checklist.py   # base c69711e
PASS governance.citation_resolves: evaluated 1272 — 1272 governance citation token(s) resolve across 2 files; 10 quoted meta-finding(s), 3 schematic token(s) excluded, 2 recorded absence(s) excused, 4 recorded correction(s) excused
$ echo ${PIPESTATUS[0]}
0
```

## 2. Root cause (file:line, lane base)

- `verifiers/verify_skill_checklist.py:2522` (base numbering) — the arm
  `rec("governance: live round-65 corrections land, only LOG.md:2678 red", …)` requires
  `status == "FAIL" and "4 recorded correction(s) excused" in detail and "LOG.md:2678" in detail`.
- `verifiers/verify_skill_checklist.py:400-419` — `GOVERNANCE_ERRATA_HORIZON = 2678` and the round-71
  errata row `(2678, "d7f442ed…", ".ufo/waves/round-67/w1/controls/junk-world/", "Routed defect R67-3 (disclosure)")`
  now excuse that red through `errata_problems` (`verify_skill_checklist.py:1688-1711`), so the live
  call returns PASS with 2 absences + 4 corrections excused. The arm pins a pre-errata world.

## 3. Repair — the delivered diff

`build/ExecArmFix/verify_skill_checklist.py.diff` (25 added / 8 deleted lines; well under the 40-line
cap). The live arm now asserts the observed truth and reuses one `live_repo` binding:

```
+        live_repo = Path(__file__).resolve().parent.parent
         status, evaluated, detail = check_governance_citations(
-            Path(__file__).resolve().parent.parent,
-            corrections=GOVERNANCE_CORRECTIONS)
-        rec("governance: live round-65 corrections land, only LOG.md:2678 red",
-            status == "FAIL" and "4 recorded correction(s) excused" in detail
-            and "LOG.md:2678" in detail and "LOG.md:2676" not in detail,
+            live_repo, corrections=GOVERNANCE_CORRECTIONS)
+        rec("governance: live round-65 corrections land, errata-excused",
+            status == "PASS" and "2 recorded absence(s) excused" in detail
+            and "4 recorded correction(s) excused" in detail,
             (status, evaluated, detail))
```

and adds the single regression assertion (one `rec`, so the assertion count moves by exactly +1):

```
+        dropped = check_governance_citations(
+            live_repo, errata=tuple(r for r in GOVERNANCE_ERRATA
+                                    if r[0] != 2678),
+            corrections=GOVERNANCE_CORRECTIONS)
+        low = check_governance_citations(
+            live_repo, errata=GOVERNANCE_ERRATA, horizon=2677,
+            corrections=GOVERNANCE_CORRECTIONS)
+        rec("governance: LOG.md:2678 erratum is load-bearing",
+            GOVERNANCE_ERRATA_HORIZON >= 2678
+            and dropped[0] == "FAIL" and "LOG.md:2678" in dropped[2]
+            and low[0] == "FAIL" and "past horizon 2677" in low[2],
+            (dropped, low))
```

Two deliberate choices: the row filter is `r[0] != 2678` rather than `[:-1]` (order-independent if a
row is appended later), and the boundary `2678`/`2677` is a **literal**, not `GOVERNANCE_ERRATA_HORIZON
- 1` — a horizon lowering would otherwise flow into the assertion and it would still pass (observed:
see mutant 2 below, first draft).

## 4. Regression assertion under mutants — both required mutants fail, exit 1

**Mutant 1 — errata row for LOG.md:2678 removed from `GOVERNANCE_ERRATA`** (tuple row deleted, tuple
closed): `python3 -B -c "import ast; ast.parse(...)"` → `syntax ok`, then

```
$ python3 -B verifiers/verify_skill_checklist.py --self-test
self-test FAIL: governance: live round-65 corrections land, errata-excused: got ('FAIL', 1273, "LOG.md:2678: '.ufo/waves/round-67/w1/controls/junk-world/' does not resolve from …
self-test FAIL: governance: LOG.md:2678 erratum is load-bearing: got ((…), (…))
2 failure(s) over 1863 assertions
$ echo $?
1
```

**Mutant 2 — `GOVERNANCE_ERRATA_HORIZON = 2677`** (`sed -i 's/^GOVERNANCE_ERRATA_HORIZON = 2678$/GOVERNANCE_ERRATA_HORIZON = 2677/'`):

```
$ python3 -B verifiers/verify_skill_checklist.py --self-test
self-test FAIL: governance: live round-65 corrections land, errata-excused: got ('FAIL', 1273, "erratum LOG.md:2678 '.ufo/waves/round-67/w1/controls/junk-world/' is past horizon 2677 or absent; …
self-test FAIL: governance: LOG.md:2678 erratum is load-bearing: got ((…), (…))
2 failure(s) over 1863 assertions
$ echo $?
1
```

In both mutants the new arm `governance: LOG.md:2678 erratum is load-bearing` is itself in the failure
list (named in the pasted output), not merely carried by the live arm.

**Mutant 3 (anti-shrink control) — the new arm deleted, nothing else changed:**

```
$ python3 -B verifiers/verify_skill_checklist.py --self-test
0 failure(s) over 1862 assertions          # exit 0 — a shrink is silent to the self-test
$ python3 -B verifiers/check_assertion_floors.py | grep -E '^FAIL|^PASS checklist'
FAIL checklist observed=1862 floor=1863
$ echo ${PIPESTATUS[0]}
1
```

This is why the floor must move: without the bump, deleting the regression arm reads green.

## 5. Floor change — 1862 → 1863, bumped in step

`verifiers/floors-registry.json` line 2 states the rule: `when a row's floor moves, edit this file,
both in-file tables and the guard docstring in the same change` (21 words, whole clause; dropped:
the leading `BUMP-IN-STEP RULE: `). Delivered, all four sites in one change:

- `floors-registry.json`: `"checklist": { "floor": 1862 → 1863, … }`
- `check_assertion_floors.py:168` `EXPECTED_INSTRUMENTS["checklist"]`: `1862 → 1863`
- `check_assertion_floors.py:213` `INSTRUMENTS["checklist"]`: `1862 → 1863`
- `check_assertion_floors.py:8` docstring summary `checklist 1863`, plus a round-72 sentence at
  lines 16-18 (`round 72 re-bumps checklist 1862 -> 1863 (the r71 errata row retired the stale
  live-landing red, and the LOG.md:2678 erratum gains a load-bearing regression arm)`)

Guard and gate at the patched tip (clean room: a second fleet-shaped clone at base with only the three
delivered diffs applied via `git apply`; `git apply --check` → clean):

```
$ python3 -B verifiers/verify_skill_checklist.py --self-test
0 failure(s) over 1863 assertions
$ echo $?
0

$ python3 -B verifiers/check_assertion_floors.py
PASS harness observed=10 floor=10
PASS corpus_integrity observed=161 floor=161
PASS corpus_independent observed=103 floor=103
PASS surfaces observed=175 floor=175
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
$ echo $?
0

$ python3 -B verifiers/verify_skill_checklist.py
PASS checklist.box_map_complete: evaluated 41 — 41 boxes mapped (8 executed, 4 delegated, 29 unexecuted); delegated verifiers/verify_dispatch_prompts.py: --box-proof exit 0: boxes proven 2; delegated verifiers/verify_alwayson.py: --box-proof exit 0: boxes proven 2
… (11 checks, all PASS) …
PASS governance.citation_resolves: evaluated 1272 — 1272 governance citation token(s) resolve across 2 files; 10 quoted meta-finding(s), 3 schematic token(s) excluded, 2 recorded absence(s) excused, 4 recorded correction(s) excused
$ echo $?
0
```

Floors-guard wall times, each run alone (single command, no concurrent seat work): 46.8 s (bump world),
43.4 s (clean room), 48.6 s (mutant 3). Under the 120 s base cap and the 300 s bound.

**Answer to "must the floor be raised": yes — 1862 → 1863.** The new assertion is the +1; leaving the
floor at 1862 lets the arm be deleted silently (mutant 3, exit 0 at 1862).

## 6. C3 cap check (informational, for the C3 owner)

The C3 predicate caps the six instrument scripts at 40 added lines over base. This repair touches two
of the six: `git -c diff.mnemonicPrefix=false diff --numstat` →
`6 4 verifiers/check_assertion_floors.py`, `25 8 verifiers/verify_skill_checklist.py` = **31 added
lines**, under the 40 cap. The floor is raised, never lowered, so the C3 floors guard holds too. With
this landed, `check_assertion_floors.py` moves from red to green in the tip battery (N: 2 → 3 of 6 at
base, assuming the other four are unchanged) — a C3 measurement, not this seat's claim.

## 7. Deliverables (under `.ufo/waves/round-72/w1/build/ExecArmFix/`)

| file | what |
|---|---|
| `verify_skill_checklist.py.diff` | the arm repair + regression assertion (25 +, 8 −) |
| `floors-registry.json.diff` | `checklist` floor 1862 → 1863 |
| `check_assertion_floors.py.diff` | in-step bump: docstring (3 sites of text) + both in-file tables |
| `verify_skill_checklist.py` | full patched file (identical to the tested bytes) |
| `check_assertion_floors.py` | full patched file |
| `floors-registry.json` | full patched registry |

All three diffs apply cleanly to base `c69711e` (`git apply --check` → clean) and the resulting tree
was what the clean-room runs above executed. The L1 lands them.

## 8. Risks and limits

- The live arm now asserts PASS on the live repo: any *new* unresolvable governance citation turns the
  self-test red — the intended fail-closed direction, but it makes the arm host-record-sensitive
  (unchanged in kind from the old arm).
- `evaluated 1272` is not pinned by the arm (only the two excused counts are); pinning it would make
  every append-only LOG.md growth a red. Deliberate.
- The regression asserts `GOVERNANCE_ERRATA_HORIZON >= 2678`; a future errata row *above* 2678 does not
  break it (the constant is monotone), a lowering below 2678 does.
- Not exercised: the C3 tip battery itself, the other five C3 gates, wave-2 falsification, and the
  guard's own mutation battery beyond mutant 3. No committed lane file, jj state, fleet repo, sibling
  lane or `shokuknow` path was written; no `git commit` ran anywhere.
- Tools installed: none (no `uv tool`, `npx` or binary install was needed; `pacman` untouched).
- Scratch: three fleet-shaped sandboxes and one `mktemp -d` scratch dir were deleted before return
  (`NO_LEFTOVER` for `/tmp/k72fleet-ExecArmFix*`); the shared `strings` dumps at `/tmp/k72-*` were not
  touched.
