# Seat report — Kb79RV02GateExemplars (round 79 w1)

Role: review readiness of the C1 repair exemplars; produce the acceptance checklist the
L1 and wave-2 reviewers apply to the four C1 repair patches. Leaf seat; no subagents; no
installs (none needed — record: zero tools installed/updated).

## What was read (grounding)
- plans/round-79.md (first, absolute): frozen predicate, kill rule, W0–W7 controls,
  landing order, no-harm battery list.
- corpus/QUALITY.md rows Q05:16, Q18:29, Q25:36, Q35:46, Q36:47, Q46:57, Q50:61, Q58:70,
  Q64:80, Q65:81 (plus Q70:86, Q71:87, Q72:88 where the checklist leans on them).
- corpus/lessons/round-72.md § Mistakes (M124 tip battery promised-not-run → Q50;
  M125 stale self-test arm → Q65) and round-73.md § Mistakes (M128 pointer gate;
  M130 tip-battery path-derivation hardening = commit 11b05d9).
- git log/diffs for the registry trio: last baseline refreshes 14ab415 (r75 note-only
  line change documenting the refresh), 1cf5afa (commit_total 42→43), 559ee76 (41→42);
  last gate hardening 11b05d9 (check_tip_battery.py +134: M127 `Path(args.repo).resolve()`
  fix, guard base rebased to r73 base, 69-assertion self-test; corpus-baseline
  re-recorded).

## Verification run (all commands' own rc captured; scratch under
/fast/scratch/hyaku/kotoba-r79/Kb79RV02GateExemplars, removed before this yield)
1. `sha256sum verifiers/check_tip_battery.py` →
   `e33b17d74f5935a43b04272baf2d88d1d4cf4f879ee9cfa48bb25f89e744bc4a` — matches the
   frozen pin; working-tree counter bytes are the frozen bytes.
2. Base receipts read (both forms identical): guards 5 of 5 PASS; gates
   registry/floors/checklist/integrity/independent exit 1, correction_sweep exit 0 →
   `tip battery exit 0: 1 of 6`, exit=1, measured rev b10bcbc6…, base 072048f….
3. Scratch clone at base b10bcbc6… (toplevel asserted): `verify_skill_checklist.py
   --self-test` rc=1 → `2 failure(s) over 1863 assertions` (BARE clone);
   `verify_corpus_integrity.py --json` rc=1 → tracked 150/144, unindexed 6 (exact list
   in checklist §0-G4), report_total 106/99, report_dead 1
   (`corpus/lessons/round-77-verifier-spotcheck.md:15: HEAD:.ufo/reports/round-77/kotoba.md`),
   commit_total 45/43; `check_gate_registry.py --rev b10bcbc6…` rc=1 →
   `check_desc_craft.py` / `check_r75_routed_repairs.py` `no registry rows naming it:
   0 (need 1)`, `60 of 62 lane verifiers; phantom 0`.
4. Fleet-shaped sandbox (lane clone + fleet-root symlinks, the counter's own shape):
   `verify_skill_checklist.py --self-test` rc=1 → `1 failure(s) over 1863 assertions` —
   arm `governance: live round-65 corrections land, errata-excused`
   (verify_skill_checklist.py:2524) failing on `LOG.md:2818: '.ufo/reports/round-76/kotoba.md'
   does not resolve`, detail shows `2 recorded absence(s) excused, 4 recorded
   correction(s) excused` — matches the battery receipt's `self_test_failures=1`.
5. Code reads: check_tip_battery.py guards (:111 LINE_CAP, :125 INSTRUMENT_PINS,
   :145 BATTERY, :279-336 run_guards); verify_corpus_integrity.py :146 UFO_POINTER_RE,
   :264-277 resolve/fallback, :495-524 dead loop (no correction machinery);
   verify_skill_checklist.py :2500-2560 arm bodies; floors-registry.json:2 BUMP-IN-STEP,
   :5-7 floor 1863; corpus-baseline.json expects + notes; SKILL.md 590 lines, sample row
   :462; LOG.md:2619-2621 (prior correction rows), :2818 (dead token), :177.

## Findings (full detail + citations in build/Kb79RV02.review-checklist.md §7)
- F1 HIGH: the single report_dead token (`HEAD:`-prefixed, a git object expression in
  r77 spot-check prose) is captured verbatim by integrity's UFO_POINTER_RE
  (verify_corpus_integrity.py:146), resolves nowhere (base join :264-270; fleet
  fallback needs the `.ufo/reports/` prefix, :272-277), and integrity has no
  correction/errata machinery (grep 0 hits). All mechanical greens are forbidden
  (edit the closure-owned spot-check / land a phantom `HEAD:.ufo` tree / edit pinned
  instruments). Unless a patch presents an evidenced legal route, C1 ends per its own
  kill rule with this routed as a counter approximation defect (Q20/Q23 class).
- F2 MEDIUM: spotcheck-identity pins only the 27 base (≤ r72) spot-checks; the
  r73–r78 spot-checks are post-base INFO — the plan's W7 control cannot trip the
  counter on those files. Guard-coverage gap to report; never to exploit.
- F3 MEDIUM: checklist self-test arm 2524 pins literal substrings
  `"2 recorded absence(s) excused"` / `"4 recorded correction(s) excused"`; a new
  counted correction (Q64 route) re-breaks it (M125 class). Lane-side report copy
  (G3(a), precedent: lane-tracked `.ufo/reports/round-2X/kotoba.md`) avoids the
  collision; Q64 row route must re-prove the arm fleet-shaped.
- F4 LOW: bare-clone validation shows a false second failing arm (2 vs 1 failures) —
  Q18 false-red trap; only fleet-shaped or counter runs are battery evidence.

## Deliverables
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79RV02.review-checklist.md
- Evidence copies: build/Kb79RV02-base-chk-selftest-bare.txt, build/Kb79RV02-base-chk-selftest-fleetshape.txt,
  build/Kb79RV02-base-integrity.json, build/Kb79RV02-base-registry.txt

VERDICT: exemplars are review-ready — guards and pins understood and cited; one high
finding (report_dead `HEAD:` token likely ungreenable inside the frozen guards) must be
dispositioned by the L1 before any patch is scored as 6 of 6.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79RV02.review-checklist.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/w1/Kb79RV02GateExemplars.md
