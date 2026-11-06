# ExecBatteryKills — round 95 w1 (C1 build: battery self-test kills N1, N5, N11)

Status: DONE (build, receipts, patch and READY on disk).
Venue: scratch clone `/fast/scratch/hyaku/kotoba-r95/ExecBatteryKills/repo` at the freeze
commit `673d1e2e6f850bb54dda9698cf825cf6788c7d0d` (toplevel asserted); candidate committed there as
`3d13eb939e18fa7cc8b4e4622eddb589f0027fe1` (scratch identity `scratch <scratch@invalid>`).

## Change

One file: `verifiers/check_mutation_battery.py` — 67 inserted lines, 0 removed, all inside
`self_test()` (plus two nested helpers `_commit`, `_extra_kill_rows` defined next to it).
`evaluate()` / `kill_set_check()` / `main()` / module pin capture-restore are untouched:
verified by byte comparison against the freeze commit (prefix lines 1-661 identical, suffix
identical, diff is a pure insertion). `KILL_SET_PINNED = 17` intact. FROZEN ANCHORS identical
in count and content (verified programmatically): `committed = git_show(lane, rev, MANIFEST).decode("utf-8")`
1x; `raise CouldNotEvaluate("manifest must name exactly the targets %s"` 1x;
`return n == want, "observed` 1x; `ok_pin, pin_detail = kill_set_check(committed, pinned)` 1x;
`print("could-not-evaluate: %s" % exc)` 3x. The inserted text contains no anchor and adds no
occurrence of any anchor. No network; rev-scoped reads go through `git show` inside the
instrument itself; fixtures are local `git init` repos (same pattern as the existing arms).

### New behavioural arms (8 new `t.check`, 38 -> 46 assertions)

- **N1 (manifest at `--rev`, both directions).** Two-commit fixtures whose first commit
  satisfies the pin while HEAD drops a kill row, and the reverse. `run_evaluate` at the
  first commit's full hash must exit 0 without naming `kill-set-size` when that commit
  satisfies, and exit 2 naming `kill-set-size` when it does not — even though HEAD says the
  opposite in each direction. A mutant reading the manifest at HEAD fails the two
  first-commit arms.
- **N5 (target-set refusal label).** A rev-path fixture whose committed manifest drops
  every BAT-target row (the surviving target set != PROBES; the target-set check fires
  before the pin check). It must exit 2 with `manifest must name exactly the targets` in
  the output and WITHOUT `kill-set-size`. The N5 mutant (prefixing the refusal with
  `arm kill-set-size:`) fails this arm.
- **N11 (added rows, +2 and +3).** Live `kill_set_check` on the live manifest with two
  and three extra kill rows appended must be refused naming the observed count; plus a
  rev-path fixture with two rows above the pin exits 2 naming `kill-set-size` and the
  observed count. The N11 mutant (`n == want or n == want + 2`) fails the +2 arms.

## Evidence (receipts under `.ufo/waves/round-95/w1/ExecBatteryKills/`)

- `selftest-honest.txt` — `0 failure(s) over 46 assertions`, rc 0.
- `counter-c1.txt` — frozen v3 counter `c1` at `3d13eb93…`:
  `C1 targets killed 3 of 3 (run errors 0); positive killed 1 of 1; honest CLEAN;
  comment decoys held 3 of 3; code decoys held 3 of 3` → **C1-PREDICATE-MET**, rc 0.
  Which arms kill which mutant (from the manual pre-check in this seat; the counter reports
  counts): N1 by 2 failing arms, N5 by 1, N11 by 2, positive N10 by the pre-existing k3 arms.
- `counter-r94c1.txt` — `R94C1 targets killed 3 of 3 (run errors 0); positive killed 1 of 1;
  honest CLEAN; comment decoys held 3 of 3; code decoys held 3 of 3` → **R94C1-PREDICATE-MET**, rc 0.
- `c1-killpin-rev.txt` — round-93 `c1-killpin-rev.sh` at `3d13eb93…`: drop/other/honest
  worlds all `yes` → **C1-PREDICATE-MET**, rc 0 (production behaviour unchanged).
- `ExecBatteryKills.patch` — `git diff --binary` from the freeze commit; sha256
  `f9506fe3033d2d5e2ee26dbb42748e892ceb46e99695922b4ca78a822bc41d96`; proven to apply
  with `git apply --check` on a second fresh clone at `673d1e2e6f850bb54dda9698cf825cf6788c7d0d`
  (clone removed after proof; applied bytes identical to the candidate).
- `controls-run.txt` — see note below.

## Round-92 controls-run.sh note

`controls-run.sh` and its `ctl-*.sh` children take **no REPO argument**: the lane is derived
from the script's own path, and the candidate commit `3d13eb93…` exists only in the scratch
clone, so `ctl-c1-honest.sh <candidate rev>` cannot resolve the rev in the lane. The honest
world of the candidate is instead measured by `c1-killpin-rev.sh` (honest world at
`3d13eb93…`: `killed 17 of 17 kill-set; equivalents survived 6 of 6`, rc 0), which is the
same battery predicate the round-92 honest world checks, and production code is
byte-identical to the freeze commit, so the round-92 reading against the lane tip is
unaffected by this patch. A `controls-run.sh` invocation against the lane was run with `HYAKU_SCRATCH` pointed at
this seat's scratch (`controls-run.txt`: `round-92 controls: shortcuts refused 2 of 2;
honest held 2 of 2`, rc 0; full per-script output in `controls-run-stderr.txt`). It ran at
the lane/freeze revision whose `validate_manifest`/battery bytes are unchanged by this patch
(the diff is inside `self_test()` only), which is the correct reading for a self-test-only
patch; the candidate's own honest-world battery reading is `c1-killpin-rev.txt` above.

## Risks / notes

- The N5 arm drops every BAT-target row, which also changes the kill count; the arm is
  valid because `evaluate()` checks the target set before the pin (lines 368-370), and the
  arm asserts the target-set label with the `kill-set-size` label absent, not the exit path.
- N11 live arms reuse `first_kill` / `module_pin` captured by the existing live arms; row
  ids for appended rows are unique per arm index, so `parse_manifest` never raises on the
  honest run.
- No counter defect found; nothing in the frozen predicates, anchors, or manifest was touched.
- No installs performed (no pacman, no uv, no binaries); no host/kernel settings touched.
- Seat attribution: ExecBatteryKills only. No lane commits. Lane writes: this report, the
  receipts dir above, the patch, and the READY file once the controls receipt lands.

## Tooling

None installed. No pacman. No host-setting change. No kernel setting touched.
