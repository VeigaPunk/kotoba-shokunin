# Kb79E05ControlsA — C1 control worlds, set A (round 79, wave w1)

Seat: leaf executor, C1 calibration controls. Date 2026-10-27. Lane base `b10bcbc6b00f8f56b202ccbadca311007b5b463c`;
plan/validated-dispatch commit F1 `2c56622375641193a03bb97c0624e6536f3dffba`; round start `daa3a09`.

Counter under test (FROZEN, never edited by this seat):

    /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_tip_battery.py
    sha256 e33b17d74f5935a43b04272baf2d88d1d4cf4f879ee9cfa48bb25f89e744bc4a
    git blob a356e9d101f3021687a80e73fca284e7436976d2  (identical at base b10bcbc6 and at all six world HEADs)

Every world ran the frozen bytes: `sha256sum` of `verifiers/check_tip_battery.py` inside each world clone returned
`e33b17d7…bc4a`, and `git rev-parse HEAD:verifiers/check_tip_battery.py` returned `a356e9d1…76d2` in every world.
No world edits the counter, `INSTRUMENT_PINS`, or any of the six battery scripts.

Command per world (exact, all from the fleet root with absolute paths):

    python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_tip_battery.py \
      --repo /fast/scratch/hyaku/kotoba-r79/Kb79E05ControlsA/<w>/kotoba-shokunin \
      --rev <world commit> --fleet /home/vgpnk/Projects/shokunin

`--fleet` is passed explicitly (the counter's default is `--repo`'s parent; the world clones live under a seat scratch
dir, so the fleet root is named to keep the sandbox fleet-shaped, as in `receipts/tipbattery-base-*.txt`).
`TMPDIR=/fast/scratch/hyaku/kotoba-r79/Kb79E05ControlsA/tmp/<w>` per world. Each command's own exit status was captured
(`cmd > out 2>&1; rc=0; cmd || rc=$?`), never a pipeline's.

## Readings

| world | world commit | guards | `tip battery exit 0:` | counter exit | what stopped it |
|---|---|---|---|---|---|
| WA0 base tree + empty commit | `4523046` | 5 of 5 | 1 of 6 | 1 | five red gates (none of the five guards fires) |
| WA0b F1 plan tree + empty commit | `df24b3d` | 5 of 5 | 1 of 6 | 1 | same five red gates (attribution: F1's plan+receipts do not move the figure) |
| WA1 baseline re-recorded to observed totals | `b0266d7` | 5 of 5 | 1 of 6 | 1 | `corpus_integrity` stays red on the two zero-mode rows |
| WA2 floors registry lowered 1863 → 1 | `54b234e` | **4 of 5** | 1 of 6 | 1 | guard `floors` (`row checklist floor 1 < base 1863`); the lowered floor does not even flip its gate |
| WA3 WA1 + WA2 + two placeholder registry rows | `3ba4596` | **4 of 5** | **2 of 6** | 1 | guard `floors`; `check_gate_registry` flips 1 → 0 on the placeholder rows |
| WA4 LOG.md `Correction:` label quoting the dead token | `ed61840` | 5 of 5 | 1 of 6 | 1 | no guard fires; nothing flips, and the line ADDS one dead citation |

Base reference (`.ufo/waves/round-79/receipts/tipbattery-base-dot.txt`, `-abs.txt`): `guards 5 of 5; tip battery exit 0: 1 of 6`, exit 1.
**No world reached 6 of 6.** WA3 reached 2 of 6 and was stopped by a guard; nothing here is a counter defect that
reaches the target. The full verbatim stdout/stderr of all six runs is in `build/Kb79E05ControlsA.receipts.txt`.

Per-world gate lines from the receipts (exit codes as printed by the counter):

- WA0 / WA0b / WA1 / WA4: `check_gate_registry 1`, `check_assertion_floors 1`, `verify_skill_checklist 1`,
  `verify_corpus_integrity 1`, `verify_corpus_independent 1`, `check_correction_sweep 0` → 1 of 6.
- WA2: `check_assertion_floors exit 2` (`wall 0.0s`), all else as WA0 → 1 of 6, guards 4 of 5.
- WA3: `check_gate_registry exit 0`, `check_assertion_floors exit 2`, `check_correction_sweep exit 0` → 2 of 6,
  guards 4 of 5, `FAIL guard floors: row checklist floor 1 < base 1863`.

## What each world changed (patches in `build/`)

- **WA0** — empty commit on `b10bcbc6`. Tree hash `ac65dc60d8e1db584d87f89906bc74fd08cc4d16` = base tree.
- **WA0b** — empty commit on F1 `2c5662`. Tree `aa7a2b4b8914…ff165` = F1 tree (a control that the plan/receipt files
  alone do not move the do-nothing figure; they were never meant to, and they do not).
- **WA1** (`Kb79E05ControlsA.WA1.patch`, 1 file, +7/−31) — `verifiers/corpus-baseline.json` rewritten to the observed
  values `tracked_files 150`, `report_total 106`, `commit_total 45`; every zero-mode expectation left at 0 and **no index
  row added** (exactly the shortcut). Result: `verify_corpus_integrity` still exits 1 on
  `corpus.index.unindexed zero observed 6 DRIFT` and `corpus.pointers.report_dead zero observed 1 DRIFT` (diag D2).
- **WA2** (`…WA2.patch`, 1 file, +2/−2) — `verifiers/floors-registry.json`, `checklist.floor` 1863 → 1, in-file tables
  and docstring untouched (the half-bump the registry exists to catch). Two independent stops: the registry anchor
  `exit 2 — FAIL registry floor drift: checklist registry=1 expected=1863 row=1863` (diag D3), and the tip battery's
  `floors` guard `row checklist floor 1 < base 1863` → guards 4 of 5.
- **WA3** (`…WA3.patch`, 3 files, +11/−33) — WA1 + WA2 plus one placeholder line each in `SKILL.md`'s `## Gate registry`
  for `verifiers/check_desc_craft.py` and `verifiers/check_r75_routed_repairs.py` (the two rows the base battery names as
  missing). The registry check flips: `check_gate_registry 1 → 0`, `gate registry rows conformant 62 of 62 lane
  verifiers; phantom 0` (diag D4). The counter still exits 1 because the same world carries WA2's lowered floor.
- **WA4** (`…WA4.patch`, 1 file, +1) — `LOG.md` gets one appended
  `- **Correction:** the token \`.ufo/reports/round-76/kotoba.md\` quoted at LOG.md:2818 is stale; … names no corrected
  address.` Result: nothing flips; and measured over the identical non-fleet-linked shape, WA0 → WA4 moves
  `governance.citation_resolves` `evaluated 1315 → 1316` with one additional dead subject (`… (+31 more)` → `… (+32
  more)`), diag D5. A text label cannot excuse anything: at the frozen bytes corrections are the in-file
  `GOVERNANCE_CORRECTIONS` tuple (`verifiers/verify_skill_checklist.py:426`), validated against a byte-pinned LOG line
  (`correction_problems`, same file ~:1714). **The world is strictly harmful** — it adds a citation the tree must
  afterwards repair.

WA0/WA0b carry no patch bytes by construction (empty commits); their tree hashes are recorded above and in the receipts.

## Measured calibration findings (evidence the L1 can use; no claim data, no repair is claimed here)

1. **The do-nothing figure is stable across the two candidate bases.** WA0 (`b10bcbc6` + empty) and WA0b (F1 `2c5662`
   + empty) both read `guards 5 of 5; 1 of 6; exit 1`. The base receipt's figure is not an artifact of the lane's
   working tree.
2. **Re-baselining alone cannot reach the corpus gate.** WA1 keeps 5 of 5 guards and 1 of 6: two zero-mode rows stay
   red by design (`unindexed 6`, `report_dead 1`). The reached-by-shortcut figure is therefore **1**, not 2.
3. **Lowering a floor is caught twice and buys nothing.** WA2: the registry anchor exits 2 before any self-test runs,
   *and* the tip battery's `floors` guard fails. A repair that needs a floor moved cannot do it in
   `floors-registry.json` alone; the in-file tables and docstring must move in the same change, which then collides
   with `instrument-pin` (see 5).
4. **`check_gate_registry` is syntactic.** WA3 proves a one-line row naming an existing script with no content flips
   the gate to 62 of 62 exit 0. For C1 this is good news (the repair is cheap and real rows are indistinguishable from
   placeholders by this gate alone) and bad news (the gate is not evidence that the row was reviewed). It is a gate
   property, not a counter defect: the counter still exited 1.
5. **The `check_assertion_floors` failure is data-repairable within `instrument-pin` — this is the important one.**
   The failing row is `checklist observed=1863 floor=1863 self_test_failures=1`. Traced: the one failing assertion is
   `governance: live round-65 corrections land, errata-excused` in `verify_skill_checklist.py --self-test`, whose
   predicate is `status == "PASS" and "2 recorded absence(s) excused" in detail and "4 recorded correction(s) excused"
   in detail` (`verifiers/verify_skill_checklist.py:2524-2526`) — i.e. **an assertion about the live tree**, not a
   code bug. Run in a fleet-shaped sandbox at the base tree it prints `1 failure(s) over 1863 assertions` and the sole
   red subject is `LOG.md:2818: '.ufo/reports/round-76/kotoba.md' does not resolve …` (diag D6). So a LOG.md data
   repair flips `verify_skill_checklist` **and** clears the floors self-test in one move: the repair set for C1 can stay
   inside data plus `SKILL.md`/`corpus/` content, with the six battery scripts byte-identical to their pinned blobs.
   Two constraints on that repair: (i) the sandbox has no tracked `.ufo/`, so a bare `.ufo/reports/...` token stays dead
   there — the repair must use a form that resolves from the repo root *inside the sandbox*; (ii) the four corrections'
   corrected tokens are `../.ufo/...`, resolvable only because the fleet root's `.ufo` is symlinked into the sandbox
   (`/home/vgpnk/Projects/shokunin/.ufo/reports/round-60/kotoba.md` and `.ufo/watchdog.log` both exist today — verified
   by `ls`; they are outside lane write scope).
   [INFERENCE] the ladder is therefore: LOG.md:2818 repair → `skill_checklist` 1→0 and `assertion_floors` 1→0;
   `gate_registry` via two real rows (WA3); `corpus_integrity`/`corpus_independent` via index rows + the HEAD-pointer
   repair + an honest baseline re-record (WA1 shows why the re-record alone is not enough). That ladder is *not* run
   here and is not claimed: it belongs to the repair seat, and step 4's last gate (`corpus.independent`) was not
   attacked by any world in this set.
6. **Two corpus instruments disagree on one tree.** At the base tree both exit 1, but
   `verify_corpus_integrity --no-baseline --json` observes `report_dead 1`
   (`corpus/lessons/round-77-verifier-spotcheck.md:15: HEAD:.ufo/reports/round-77/kotoba.md`) while
   `verify_corpus_independent --json` observes `report_dead 0` over the same bytes (its only red row is
   `corpus.index.unindexed 6`) — diag D7. A C1 repair that fixes one of those pointers may not satisfy both gates'
   predicates; the L1 should reconcile the two readings before scoring `6 of 6`. Reported as a measured
   inconsistency, not as a defect in either instrument's own declared predicate.

## Scope, hygiene, blockers

- Files written in the lane: `.ufo/waves/round-79/build/Kb79E05ControlsA.receipts.txt`,
  `.ufo/waves/round-79/build/Kb79E05ControlsA.diagnostics.txt`, four world patches
  (`Kb79E05ControlsA.WA1.patch`…`WA4.patch`) and this report. Nothing else in the lane was touched: no commit, add,
  stash or checkout; no `MANIFEST.json`, `scripts/`, `.ufo/state/`, `SKILL.md`, `corpus/`, `verifiers/` edit (the
  world edits exist only as patches against scratch commits).
- Scratch: `/fast/scratch/hyaku/kotoba-r79/Kb79E05ControlsA/` (six world clones named `kotoba-shokunin`, one probe
  clone with fleet symlinks for the self-test trace), removed before yielding; every patch and receipt was copied into
  `build/` first. No writes to `/tmp` beyond sub-50 MB files, none cited.
- No tool installs or upgrades were needed (no pacman: host-wide pause respected).
- Blocker: none. Residual for the L1: `verify_corpus_integrity` vs `verify_corpus_independent` disagreement on
  `report_dead` (finding 6) is unresolved by this seat and sits on the critical path of the C1 ladder.

VERDICT: No control world in set A reaches 6 of 6 (best shortcut WA3 = 2 of 6, stopped by the `floors` guard); the frozen tip battery held at 5 of 5 guards for the base, baseline-only, and LOG-label worlds — and its `check_assertion_floors` failure is a data-assertion about `LOG.md:2818`, not a pinned-instrument defect.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/w1/Kb79E05ControlsA.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79E05ControlsA.receipts.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79E05ControlsA.diagnostics.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79E05ControlsA.WA1.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79E05ControlsA.WA2.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79E05ControlsA.WA3.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79E05ControlsA.WA4.patch
