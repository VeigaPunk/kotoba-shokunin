# ConnectorOverlap — round 91 cross-claim overlap and sibling copies (read-only)

Seat: ConnectorOverlap (connector, leaf, read-only). Base read: freeze commit
`9af1a7af2adf0ab07cfd53f92affc1ed8d992262` (`plans/round-91.md`, `plans/round-91-controls.md`).
Nothing was written in any repo, lane, or sibling. The only writes are this report, its receipts
copied under `.ufo/waves/round-91/w1/ConnectorOverlap/`, and `CONNECTOR_READY`. Scratch
`/fast/scratch/hyaku/kotoba-r91/ConnectorOverlap/` held base-bytes copies for read-only counting and is removed before yield.

## Commands and observed output

### 2a. Sibling grep as specified (fleet, `.py`/`.md`, kotoba tree excluded)

```
grep -rln 'check_mutation_battery\|SELF_TEST_TIMEOUT_S\|check_freeze_gate' /home/vgpnk/Projects/shokunin --include='*.py' --include='*.md' 2>/dev/null | grep -v '/kotoba-shokunin/'
/home/vgpnk/Projects/shokunin/.ufo/reports/round-89/kotoba.md
/home/vgpnk/Projects/shokunin/.ufo/reports/round-90/kotoba.md
```

Count: **2**. Both are fleet-root report files that narrate kotoba's round history (not a sibling lane,
not code). Lane owner: fleet root (read-only for every seat). Zero `.py` copies anywhere outside the kotoba lane.

### 2b. Broadened scan (all file types, same three names plus `check_assertion_floors` and `check_tip_battery`)

```
grep -rIl --exclude-dir=.git --exclude-dir=kotoba-shokunin -e check_mutation_battery -e SELF_TEST_TIMEOUT_S -e check_freeze_gate -e check_assertion_floors -e check_tip_battery /home/vgpnk/Projects/shokunin
→ 41 files
```

Split by owner (41 = 19 sibling-lane + 22 fleet-root):

- **Sibling lanes: 19 files, all prior-round artifacts owned by that lane, all mentions or quoted text, none a copy of instrument code.**
  - `souji-shokunin` 1 file: `.ufo/waves/round-52/w1/S52connector01/evidence/01-sibling-term-sweep.txt` (7 hits; sweep table naming `check_tip_battery.py` and the floors row).
  - `kumitate-shokunin` 5 files: `round-41/verify/ConnSiblingA2.md`, `round-59/w1/ConnectorSiblings.stream.jsonl` (a tool read of kotoba `PROVINCE` text), `round-65/w1/K65ConnOverlap.md`, `round-80/w1-results.json`, `round-80/w1/K80ConnectSiblings.md`.
  - `kagi-shokunin` 1 file: `round-28/build/ConnKotoba.md` (floors anchor notes).
  - `tameshi-shokunin` 1 file: `round-17/w1/C01SiblingOverlap.md`.
  - `chousa-shokunin` 5 files, all `round-80/w1/R80ConnectorA/`: `anchors-search.txt`, `kotoba--corpus__QUALITY.md.blob`, `kotoba--corpus__QUALITY.md.receipt`, `kotoba-narrow.txt`, `kotoba-search.txt`. These quote kotoba's corpus text (`QUALITY.md` Q65/Q66/Q35 rows), not verifier code.
  - `mori-shokunin` 1 file: `round-49/w1/Mo49ConnSiblings.md`.
  - `kengaku-shokunin` 2 files: `round-77/w1/ConnectorR77.md`, `round-82/w1/ConnectorR82.md`.
  - `kama-shokunin` 2 files: `round-47/w1/out/N1Overlap.md` and `round-47/w1/out/N1Overlap/overlap.md`.
  - `kaidoku-shokunin` 1 file: `round-76/w1/ConnectorCross/receipt.json` (a path string `./kotoba-shokunin/verifiers/check_assertion_floors.py`).
- **Fleet root (not a sibling lane): 22 files.** 18 `.ufo/reports/round-NN/kotoba.md` narrative reports; `MANIFEST.json` (3 hits); `.ufo/l0-questions.md`; `.ufo/waves/kaika-w1/connect-instruments.md`; `.ufo/waves/hyaku/jj-w1/reports/JjAuditKotoba.md`. All read-only, none in the round's touch list.

Verdict on copies: **no sibling lane holds a copy of any of the six round surfaces** (`check_mutation_battery.py`,
`fixtures/mutation-battery/manifest.tsv`, `check_assertion_floors.py`, `floors-registry.json`,
`check_tip_battery.py`, `check_freeze_gate.py`). No sibling file is a `.py` copy. The sibling copies are
mentions and quoted kotoba text, so none needs a lane-owner decision.

### 2c. Base blobs of the touched instruments (`git rev-parse 9af1…:<path>`)

```
verifiers/check_assertion_floors.py   c10c0f108f484221d0a7600ac227f10f019f5d4d  (unpinned at base)
verifiers/check_freeze_gate.py        f98a62ee0b6b2cd470031dd9089ffc4b69d916a0
verifiers/check_tip_battery.py        46d6bccb0dcd6a99928ab8479bd8ec46e401d81c
verifiers/check_mutation_battery.py   91d3ad4c645fa226a6f22008e21f45969505fc43
manifest.tsv                          7954322c4c08631df300ed8378ff07a5b1562b7f
floors-registry.json                  6a1cbe92a26d25c9894e29e05ff7c8cd493290bb
```

### 2d. Anchor-count check of the `fg-*` kill rows against base `check_freeze_gate.py`

Stdlib `re`, read-only, run on `git show 9af1…:verifiers/check_freeze_gate.py` and the base manifest:

```
fg-m1-expect-exit-sign-flip        edit1 matches=1 lines=[276]
fg-m1b-expect-stdout-sign-flip     edit1 matches=1 lines=[280]
fg-m2-control-skip-w_added_red     edit1 matches=1 lines=[269]
fg-m2b-control-skip-last           edit1 matches=1 lines=[269]
fg-m3-ladder-refusal-to-2          edit1 matches=1 lines=[287]
fg-m3b-ladder-eval-to-1            edit1 matches=1 lines=[274]
fg-m4-parse-drop-stdout-clause     edit1 matches=1 lines=[133]
fg-x1-parse-drop-exit-clause       edit1 matches=1 lines=[124]
```

Every anchor matches exactly once at base. `check_mutation_battery.py:166-171` raises
`CouldNotEvaluate("anchor miss … expected 1")` on any other count, so a count change is a battery exit 2.

### 2e. Receipts read (copied to `.ufo/waves/round-91/w1/ConnectorOverlap/`)

- `tipbattery-before.txt`: `gate verifiers/check_assertion_floors.py exit 0 wall 179.0s`; `wall 182.8s`;
  `FAIL guard instrument-pin: verifiers/check_assertion_floors.py blob c10c0f10… … is not a pinned blob`;
  `guards 4 of 5; tip battery exit 0: 3 of 6`.
- `harness-selftest-duration.txt`: `loadavg-start: 2.73 2.77 3.87`, `wall-seconds: 160.2`, `loadavg-end: 3.16 3.11 3.84`, `0 failure(s) over 123 assertions`.
- `freeze-gate-r91.txt`: `freeze gate: 4 control(s) held — freeze may proceed`, `rc=0`.

## (1) Overlaps among the round's surfaces (with line numbers at the base)

**O1 — ladder edit vs. the C1 `fg-*` kill rows (HIGHEST).** C2 leg B repairs
`verifiers/check_freeze_gate.py` (owner ExecLadder). C1's manifest (`manifest.tsv` lines 2–9, owner
ExecBatteryArms) anchors eight kill rows into that file: `fg-x1` 124–125, `fg-m4` 133–134, `fg-m2`/`fg-m2b`
269–270, `fg-m3b` 274–275, `fg-m1` 276, `fg-m1b` 280, `fg-m3` 287–288. The exit-ladder region is 262–294.
Any text change inside the anchored spans, or any duplicate of the anchor text, turns the battery into exit 2.
Plan C2 leg B(d) requires `fg-m3` and `fg-m3b` to stay killed inside C1's run, so this is a hard shared
contact. Constraint for ExecLadder: keep the literal anchor text of the rows above unchanged and unique at
the landing bytes, or the L1 must amend `manifest.tsv` (which the plan's "exactly +3 rows" forbids without an
addendum). Line shifts are harmless (the anchors are content-based); text edits in those spans are not.

**O2 — battery `PROBES[FG]` baselines vs. ladder exit semantics.** `check_mutation_battery.py:66-68` declares
`fg-self-test` exit 0, `fg-fixed-plan` (`verifiers/fixtures/freeze-gate/r88-controls-fixed.md`) exit 0 and
`fg-unsat-plan` (`verifiers/fixtures/freeze-gate/r88-controls.md`) exit 1. `check_baseline` at `:304-311` raises
`CouldNotEvaluate` (exit 2) if the landing bytes return any other exit. Any ladder repair that changes those three
exits takes C1 red. The two fixture plans are not owned by any claim and must not change. Severity medium.

**O3 — the pre-data controls run through the instrument being repaired.** `plans/round-91-controls.md` (four
controls, all `expect: exit 1`) was executed through `check_freeze_gate.py` at base (`freeze-gate-r91.txt`,
`4 control(s) held`). ExecLadder's repair changes that same gate. Plan § No-harm lists post-state checks but not
a re-run of this control plan at the landing. Recommendation: the L1 re-runs
`python3 -B verifiers/check_freeze_gate.py --plan plans/round-91-controls.md` at the landing revision and expects
`freeze gate: 4 control(s) held` with rc 0. [INFERENCE: the controls' expectations should be unchanged by the repair;
not observed.] Severity low–medium.

**O4 — freeze_gate count vs. the floor (ExecLadder ↔ ExecFloorsCap).** ExecLadder adding a self-test arm moves
`check_freeze_gate.py --self-test` from 30 to N' > 30. The floor for it sits in three places owned by the
floors-guard builder: `check_assertion_floors.py:200` (`"freeze_gate": 30` in EXPECTED_INSTRUMENTS), `:280-281`
(INSTRUMENTS row, floor 30), and `floors-registry.json` `freeze_gate` (floor 30). The compare at
`check_assertion_floors.py:673` is `assertions >= floor`, so N' > 30 stays green. The BUMP-IN-STEP comment at
`:198-199` implies the floor should move in the same change, but ExecFloorsCap owns only the `floors_guard` row
of `floors-registry.json`. Decision needed before landing: either leave `freeze_gate` at 30 (green, one-sided: a
dropped arm down to 30 passes silently) or extend ExecFloorsCap's ownership to the `freeze_gate` row and both
in-file tables. Severity medium (anti-shrink weakened, not red).

**O5 — the tip battery's 280-s gate budget vs. the 360-s child cap (ExecFloorsCap leg A(a) ↔ check_tip_battery.py).**
`check_tip_battery.py:113` `GATE_TIMEOUT_S = 280` bounds the whole floors gate run; the floors gate measured
179.0 s at base (`tipbattery-before.txt`). C2 leg A(a) sets `SELF_TEST_TIMEOUT_S = 360` (`check_assertion_floors.py:202`).
The per-child cap is `child_timeout_s(base, load) = base × min(max(1, load), 15.0)`
(`check_assertion_floors.py:206`, `:209-220`, call at `:659`). At landing the child cap is 360 × load, so under any
load ≥ 1 it exceeds 280 s, and the tip battery's 280-s kill fires first. The 2× Q39 calibration does not protect the
tip-battery path; the 280-s budget does. Also, `check_tip_battery.py:113` is in no claim's touch list.
[INFERENCE from the formula and the measured 160.2 s harness self-test: the base cap is 120 × load, so on an
idle host (load ≤ 1) the cap is 120 s < 160.2 s and the floors walk would fail `harness_independent` with a
timeout; the base is green only because the measured load was ~2.7–3.2. Not observed on an idle host.]
Severity medium. Recommendation: the L1 records the 280-s bound as a known coupling in the landing receipt, or
re-measures the floors gate wall at the landing.

**O6 — INSTRUMENT_PINS is a last-edit-wins pin (ExecFloorsCap ↔ ExecFloorsCap).** `check_tip_battery.py:134-137`
admits three blobs for `check_assertion_floors.py`; the base blob `c10c0f10…` is not among them (the r90 bump gap,
the reason `guards 4 of 5`). The append must name the landing blob, which is the hash of the final floors bytes.
Any later change to `check_assertion_floors.py`, including an attack-seat fix or a re-patch, unpins the blob and
reproduces `FAIL guard instrument-pin`. Ordering rule: the INSTRUMENT_PINS append is the last edit to floors bytes.
Severity high if violated, low if observed.

## Checked and clean (no overlap)

- **FX fixture rows** (`check_mutation_battery.py:491-520`) name the `FG` path but are applied to synthetic
  fixture stubs (`build_fixture`, `:536-537`, `:660`, `:666`), not to the real `check_freeze_gate.py` bytes. No
  coupling to ladder edits.
- **Registry counter** (`check_gate_registry.py:196-208`) checks that the self-test cell names an exact handler
  flag, not a count. `SKILL.md:520` (`over N assertions`) and `SKILL.md:522` (`M >= 8`, `E >= 4`) name no literal
  count that C1's 17 or C2's N' would make stale. No SKILL edit is needed (plan agrees).
- **Tip battery list** (`check_tip_battery.py:159-166`) does not contain `check_mutation_battery.py` or
  `check_freeze_gate.py`. Neither C1 nor leg B can trip `instrument-pin`.
- **File-level ownership** is one writer per file across ExecBatteryArms, ExecFloorsCap, ExecLadder, ScribeCorpus.
  The overlaps above are content-level, not file-level.
- **Probe observation** includes stdout (`check_mutation_battery.py:13-19`), but baselines are measured at the same
  revision (`:351-352`), so the count change in O4 does not redden C1 by itself.

## (2) Sibling copies — count and owner

- Code copies in sibling lanes: **0**.
- Mention or quote copies: **19** in 8 sibling lanes (souji 1, kumitate 5, kagi 1, tameshi 1, chousa 5, mori 1,
  kengaku 2, kama 2, kaidoku 1). Each file is owned by its own lane, and none is a shared surface.
- Fleet-root reports and manifests naming kotoba instruments: **22**, read-only, none in the round's touch list.

## (3) Boundary sentence

The round's surfaces (`verifiers/check_mutation_battery.py`, `verifiers/fixtures/mutation-battery/manifest.tsv`,
`verifiers/check_assertion_floors.py`, `verifiers/floors-registry.json`, `verifiers/check_tip_battery.py`,
`verifiers/check_freeze_gate.py`) are **clean** against sibling lanes: no sibling lane owns or copies them, and the
only sibling contact is 19 read-only prior-round citations.

## Risks for the L1

1. O1 (ExecLadder ↔ manifest rows fg-m1…fg-m3b): highest. Check `manifest.tsv` anchors against the final
   `check_freeze_gate.py` before integration.
2. O5 (tip battery 280-s gate vs. the 360-s cap): the 280-s bound is the operative limit on the tip-battery path.
3. O4 (freeze_gate floor 30 unbumped): decide before landing.
4. O6 (INSTRUMENT_PINS): the pin must match the final floors bytes.
5. O3 (controls re-run): recommended, not in the plan.
