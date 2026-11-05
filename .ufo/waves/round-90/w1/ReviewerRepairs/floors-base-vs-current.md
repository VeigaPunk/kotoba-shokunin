diff --git c/corpus/README.md w/corpus/README.md
index 569b2bc..32ce4e6 100644
--- c/corpus/README.md
+++ w/corpus/README.md
@@ -183,6 +183,7 @@ Domain: prompt & skill craft — SKILL.md/AGENTS.md quality, trigger fidelity.
 | Round-89 lessons | `lessons/round-89.md` | round 89's lane lesson: the freeze gate (C1, `verifiers/check_freeze_gate.py`) and the instance-level D5 successor (C2, `verifiers/check_r86_routed_repairs_v3.py`) as pre-freeze instruments; `## Gate` (S258 admitted, S258 route (a) rejected), `## Mistakes` (report immutability, Q81; the MERGE-REPORT count), seat-death record |
 | Freeze gate: declared controls observed before the freeze (round 89) | `knowledge/freeze-gate-round89.md` | a declared control must be observed before the freeze: exit-plus-stdout expectations executed by `verifiers/check_freeze_gate.py` against receipt-grounded simulators; the round-88 unsatisfiable control reproduced mechanically (exit 1 refused, fixed plan exit 0); S258 and S259 |
 | Instance-level D5 against a base receipt (round 89) | `knowledge/instance-d5-round89.md` | per-name value and detail non-growth against a base receipt pinned at a clean freeze commit, with record blobs, a receipt self-digest and the Q79 location class; the v2 name-level blindness recorded as the control; five pre-freeze worlds |
+| Round-89 verifier spot-check (indexed round 90) | `lessons/round-89-verifier-spotcheck.md` | the non-author closure of round 89 (kotoba round 89 admitted; C1 and C2 evidence-verified, the S258/S259 admits and the assimilation reject agreed; routed notes 1–3 for round 90); landed at `0c20d8a` after the r89 landing measurement, indexed round 90; written by the hyaku closure, never edited here |
 
 ## Frontier
 
diff --git c/verifiers/check_assertion_floors.py w/verifiers/check_assertion_floors.py
index 84e99de..c10c0f1 100644
--- c/verifiers/check_assertion_floors.py
+++ w/verifiers/check_assertion_floors.py
@@ -8,10 +8,14 @@ the recorded floor (harness 10, corpus_integrity 164, corpus_independent 105,
 surfaces 218, overlap_levers 51, checklist 1863, pins 62,
 harness_independent 123, compare_harness_independent 330, floors_guard 150,
 dispatch_prompts 56, sibling_census 68, alwayson 89, correction_sweep 25,
-scoped_rules_v32 240, spec_craft 250, sibling_reread 47, omp_root_semantics_v2 68;
-round 88 (claim C1's guard S4) registers the v2 omp root-semantics counter at its
+scoped_rules_v32 240, spec_craft 250, sibling_reread 47, omp_root_semantics_v2 68,
+freeze_gate 30; round 88 (claim C1's guard S4) registers the v2 omp root-semantics counter at its
 landed count (69) minus one, so a dropped grounding, binding or forgery arm reds
-this guard instead of passing every gate silently; round 76 (hygiene
+this guard instead of passing every gate silently; round 90 (carry-in r89
+half-bump) registers freeze_gate (verifiers/check_freeze_gate.py) at its r89
+landed count (30), completing the registry's half-bump so a dropped
+freeze-gate self-test arm reds this guard instead of passing every gate
+silently; round 76 (hygiene
 repair D4 -- the round-74 spot-check's routed defect 4, item 4) floors the
 two round-74 counters whose self-tests were UNFLOORED, so an arm dropped
 from either file now reds this guard (the r62 F17 class, re-found by the
@@ -191,6 +195,9 @@ EXPECTED_INSTRUMENTS = {
     "spec_craft": 250,
     "sibling_reread": 47,
     "omp_root_semantics_v2": 68,
+    # round 90 (carry-in r89 half-bump): freeze_gate joins with the row the
+    # registry already carries (floor 30), completing the bump in one step.
+    "freeze_gate": 30,
 }
 SELF_TEST_TIMEOUT_S = 120
 # Round-56 routed defect 4 (round-55 spot-check, 'routed defects' item 4): the
@@ -267,6 +274,11 @@ INSTRUMENTS = {
     # below so a dropped arm reds this guard, and S4 reads the same row.
     "omp_root_semantics_v2": ("verifiers/check_omp_root_semantics_v2.py", 68,
                               r"(?m)^(\d+) failure\(s\) over (\d+) assertions$", 2, 1),
+    # round 90 (carry-in r89 half-bump): the freeze-gate counter registers at
+    # its r89 landed count (check_freeze_gate.py --self-test 30, the registry
+    # row's floor), completing the bump in one change (BUMP-IN-STEP RULE).
+    "freeze_gate": ("verifiers/check_freeze_gate.py", 30,
+                    r"(?m)^(\d+) failure\(s\) over (\d+) assertions$", 2, 1),
 }
 
 
@@ -848,10 +860,10 @@ def self_test() -> int:
         # sibling_census; round 51: 12 with overlap_levers; round 53: 13 with alwayson;
         # round 58: 14 with correction_sweep; round 65: 15 with scoped_rules_v32;
         # round 76: 17 with spec_craft and sibling_reread; round 88: 18 with
-        # omp_root_semantics_v2),
+        # omp_root_semantics_v2; round 90: 19 with freeze_gate),
         # including this guard's self-test); a stale literal here would stop landing
         # and the count-check would name it.
-        text = swap(registry_text, '"instrument_total": 18', '"instrument_total": 10',
+        text = swap(registry_text, '"instrument_total": 19', '"instrument_total": 10',
                     "F6/total")
         proc = run(write_tree(tmp / "f6", source, text), tmp / "f6")
         rec("F6 size drift: exit 2", proc.returncode == 2, proc.returncode)
diff --git c/verifiers/floors-registry.json w/verifiers/floors-registry.json
index ec8dc57..6a1cbe9 100644
--- c/verifiers/floors-registry.json
+++ w/verifiers/floors-registry.json
@@ -1,6 +1,6 @@
 {
   "$comment": "Authoritative instrument registry for verifiers/check_assertion_floors.py (round-37 claim C2a, scout M7's HIGH). The guard's two in-file tables (EXPECTED_INSTRUMENTS, INSTRUMENTS) agree with each other by construction, so a coordinated edit -- the same row deleted from BOTH, a floor lowered in BOTH, a row path repointed -- was self-consistent and silent: the instrument stopped rerunning while the guard still printed all-PASS (scout M7, round 35; re-probed at 041f6ba by seat P5). This file is the anchor OUTSIDE the edited file: any disagreement fails loudly before a self-test runs, naming the class. BUMP-IN-STEP RULE: when a row's floor moves, edit this file, both in-file tables and the guard docstring in the same change; a half-bump now fails loudly on the side that was missed. Every declared path here must stay UNDER --repo: round 40 (claim C2, seat P3) closed V3's confinement residual -- an absolute path or a `../` traversal in this file (or in the guard's own tables) now fails exit 2 as 'escape: ...', because the guard joins it as `repo / path` and an absolute operand silently discards the repo (measured green at r39 bytes: B2's arm B, E2's A25b, drafts/p3/out/ARMS-BEFORE.txt C1/C2). An in-repo `..` such as `verifiers/../verifiers/x.py` stays allowed. TRUST BOUNDARY (documented, not enforced): a coordinated edit of this anchor as well is a three-artifact edit and out of scope for this guard; a symlink INSIDE the tree pointing outside --repo is not a declared-path escape; --script NAME=PATH stays an explicit operator override by design (a unique-bytes stub anywhere, including outside --repo, is the operator's affordance -- but an override that resolves to or matches the bytes of another row's canonical instrument is named 'override repoint').",
-  "instrument_total": 18,
+  "instrument_total": 19,
   "instruments": {
     "checklist": {
       "floor": 1863,
