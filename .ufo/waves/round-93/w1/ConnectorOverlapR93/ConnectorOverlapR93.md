# ConnectorOverlapR93 — cross-claim overlap, sibling copies, seat-name uniqueness (round 93)

Seat: ConnectorOverlapR93 (read-only connector, kotoba r93-w1). Freeze/base of every citation:
`6d7eee0570912d9f3b9d3e3d0137f3c755451233` (= lane HEAD at read time, verified `git rev-parse HEAD`).
Method: read `plans/round-93.md` in full; snapshotted the freeze tree with `git archive 6d7eee0 | tar -x`
into my scratch; every `file:line` below is freeze-commit bytes. No git/jj writes anywhere; no lane
writes outside `.ufo/waves/round-93/w1/ConnectorOverlapR93*/`. No tools installed (pacman pause respected;
none needed).

## Part 1 — shared surfaces: where one claim's change can flip another's reading

### O1 — The round-92 SHORTCUT controls are byte-pinned at e073723; C1's new check cannot fire in them
`verifiers/fixtures/round-92/ctl-c1-manifest-only-v2.sh:9` pins `FREEZE=e073723ae667b64e534f8621bddb83ad12ad0e71`,
`:16` clones+checks it out, and `:44` runs **the clone's own** `verifiers/check_mutation_battery.py` —
round-92 bytes, forever. Same shape for the C2 shortcut: `ctl-c2-capline-only-v2.sh:9,:16,:38` (clone's
tip battery). So the grep at `ctl-c1-manifest-only-v2.sh:46`
(`could-not-evaluate: manifest mb-c1-shortcut-kill:`) reads the OLD instrument regardless of the C1 patch:
**the feared "C1's check fires before the control's grep" cannot happen.** Caveat: this immunity holds only
while the control's FREEZE pin stays `e073723`; refreshing that pin to the r93 freeze would be a frozen-control
amendment (L1/addendum act), not a builder move.

### O2 — The round-92 HONEST controls run the landed bytes post-landing (the real coupling)
`ctl-c1-honest.sh:15` runs the **lane working-tree** battery at REV (default lane HEAD) and needs
rc 0 + `mutation battery killed 17 of 17 …`; `ctl-c2-honest.sh:52,:55` runs the **lane working-tree** tip
battery and greps `^guard instrument-pin PASS$`; `controls-run.sh` must keep reading
`shortcuts refused 2 of 2; honest held 2 of 2` (C1 kill rule). Post-landing constraints, both implied by the
frozen predicates: C1's committed-manifest count check must be **silent at 17 kill rows**
(`verifiers/fixtures/mutation-battery/manifest.tsv` has exactly 17 kills: 8 fg rows :2-9, 6 d5 rows :10-15,
3 mb rows :22-24), and C2's required-key check must be **silent with the frozen 7-key dict**
(`verifiers/check_tip_battery.py:132-176`). During the wave neither honest control can name a candidate
(they default to lane HEAD and hardcode `$LANE`); only the round-93 counters accept `REPO`.

### O3 — C1's count check must fire AFTER manifest parse, BEFORE probe baselines (else the drop world stays unnamed)
Freeze `verifiers/check_mutation_battery.py` order in `evaluate()`: parse at `:365`
(`rows = parse_manifest(git_show(lane, rev, MANIFEST)…)`), target-set refusal `:366-367`, g3 `:368-369`,
`dest = materialize(...)` `:371`, probe baselines with CNE raise at `:337-339`. Pre-data receipt
`receipts/redbefore-c1-base.txt`: the drop world today reads
`could-not-evaluate: baseline bat-self-test exit 1, declared 0: the revision does not hold the frozen baseline`
— the refusal is **shadowed by the BAT baseline** (the materialized clone's working-tree manifest has 16 kill
rows, so its `--self-test` arm fails). If ExecKillPinRev inserts the kill-row count check **after** the
baselines, the drop world keeps reading that baseline CNE with no `kill-set-size` name → C1-PREDICATE-UNMET.
Safe window: count from the already-parsed `rows` (do **not** re-parse through `kill_set_size`/`kill_set_check`,
`:177-188`, whose `manifest malformed` relabel re-surfaces parse diagnostics) between `:367` and `:371`.

### O4 — C1 must not touch the three mb anchor regions nor break the BAT baseline
`manifest.tsv:22` (mb-m2) anchors `if rc != 0 or out\.decode\(\)\.strip\(\) != rev:\n        raise
CouldNotEvaluate\("G1: %s is not a commit` (evaluate `:356-358`); `manifest.tsv:23` (mb-m15) anchors the
materialize status check (`:308-310`); `manifest.tsv:24` (mb-m16) anchors the row-loop restore line
`place(dest / row.target, data[row.target], rec_sha[row.target], "restore " + row.target)` (evaluate body,
~`:399`). The O3 window touches none of them; any reformat that shifts those exact byte regions gives
`anchor miss` → CNE at `:198` → the candidate's honest world exits 2 — the round-92 ExecLadderR92/fg-x1
integration-defect class (round-92 report § 4). Also `PROBES` declares `BAT: (("bat-self-test",
["--self-test"], 0),)` at `check_mutation_battery.py:72-79`: the candidate's `--self-test` must stay exit 0
in all three counter worlds, and the kill rule keeps requiring `--self-test` → `0 failure(s)`.
(Note: BAT is the **mutation battery's** probe target; the tip battery has no probe of
check_mutation_battery — the item's "the battery's PROBES target BAT" resolves here.)

### O5 — C2 must keep `INSTRUMENT_PINS` a static dict literal; the check must be key-based, not count-based
Two external AST readers consume the dict's literal form:
- `ctl-c2-honest.sh:41` — `pins = const(show("verifiers/check_tip_battery.py"), "INSTRUMENT_PINS")` with
  `ast.literal_eval` over the **committed** bytes. Rebuilding the dict programmatically (comprehension /
  `dict.fromkeys(BATTERY)`) makes `literal_eval` fail → the control's conjunct errors →
  C2-PREDICATE-UNMET (C2's own kill rule).
- `c2-pinkey.sh:39-70` (`edit_pins`) — ast-parses the dict, line-splices the
  `verifiers/check_correction_sweep.py` key span, re-`literal_eval`s to assert removal. Same constraint.
The required-key check belongs in `run_guards` just before the `:343` per-path loop
(`for path, allowed in INSTRUMENT_PINS.items():` — the silent-drop hole; forgery-c2.patch's hunk context
`@@ -340,6` marks the same spot), reported under the existing `instrument-pin` id so the guard count stays 5
(`guard_ids` `:419-420`, tally `:439-440`). It must fire on **key absence regardless of count**: the frozen
keyswap conjunct (`c2-pinkey.sh:84-86` `hit()`: a `FAIL guard instrument-pin:` line naming
`verifiers/check_correction_sweep.py` AND `guards 4 of 5`) is checked identically in keydrop and keyswap;
`receipts/forgery-c2-run.txt` shows the count form (`len < 7`) is silent in keyswap (only the junk-key blob
FAIL fires) → UNMET — exactly the falsified shape the plan discloses.

### O6 — C2's self-test reseeds flip under a required-key check (builder-internal, but silent if missed)
`check_tip_battery.py` `self_test()` sets `INSTRUMENT_PINS = {}` globally at `:512-513` and reseeds only
`BATTERY[0][0]` at `:578`, `:592`, `:712` (restored `:598`, `:718`). With a required-key check, **every**
fixture world gains `FAIL guard instrument-pin: <six BATTERY paths>` lines → the frozen-line assertion
`… guards 5 of 5; tip battery exit 0: 6 of 6` and the exit-0 assertions (satisfying world `:529-531`,
pin-ok world `:595-597`, gate worlds, floors/spotcheck worlds) all flip. The C2 patch must seed all six
required keys in fixture worlds while keeping `guard_ids` and the 5-tally; the tip self-test was
`0 failure(s) over 74` at round-91 landing — that number will move if arms are added, which is fine, but
`0 failure(s)` must hold (kill rule).

### O7 — Neither patched file is in the other instrument's guarded set: the candidate's guard run is base-identical
Tip battery guards cover the six `BATTERY` scripts (`check_tip_battery.py:178-186` — gate-registry, floors,
skill-checklist, corpus-integrity, corpus-independent, correction-sweep), the floors registry, corpus/ +
verifiers/ + SKILL.md no-deletions, and `corpus/lessons/*-verifier-spotcheck.md`. **Neither
`verifiers/check_mutation_battery.py` nor `verifiers/check_tip_battery.py` is in `BATTERY` or
`INSTRUMENT_PINS`** → the C1/C2 line deltas and blobs are invisible to instrument-size/instrument-pin;
the honest `guards 5 of 5` is unchanged (`receipts/redbefore-c2-base.txt`: honest PASS, 5 of 5).
Corollary, already disclosed in the plan's C2 scope: the checker pins others, never itself — an edit that
removes both a key and the required-key check is out of scope for an in-file guard (disclosed, not a new
defect). Symmetrically, the mutation battery's targets FG/D5/BAT (`check_mutation_battery.py:58-60`) exclude
check_tip_battery.py → the C2 patch flips no battery probe and no manifest anchor.

### O8 — Scribe and mined-mistake interactions
(a) `corpus/lessons/round-93.md` does **not** match `SPOTCHECK_RE` (`-verifier-spotcheck\.md$`,
`check_tip_battery.py:107`) → the spotcheck-identity guard reports it as INFO ("spotcheck added"), never a
failure; the frozen `round-92-verifier-spotcheck.md` must stay byte-identical (guard + lane freeze — no seat
may touch it). (b) ExecReceiptRevs' `check-receipt-revs.sh` targets the round-92 defect (receipts naming
`cd355c47…`, a scratch rev that never resolved in the lane). The round-93 counters by design name
scratch-clone revisions (`c1-killpin-rev.sh` prints `rev … repo /fast/scratch/…`; `c2-pinkey.sh` likewise).
If any w1 receipt naming a scratch-only rev is later treated as landing evidence, the new check fails at
landing **by construction**. Procedural mitigation (already the plan's landing rule): L1 re-measures at the
landed lane revision; w1 receipts should keep naming rev + repo so the mapping stays auditable.

## Part 2 — sibling copies

Greps over all 20 sibling lane repos (`kaidoku revenger kake kengaku kasegi kagi tabi kama kumitate
kotodama mado tameshi mori tsukuroi chousa souji lore game-dev-2d audio game-dev-3d`), plus the fleet root:

- **KILL_SET_PINNED** — 0 hits outside kotoba (`check_mutation_battery.py:87` and its prose). No sibling
  carries the constant; the silent-constant class does not propagate.
- **kill-set-size** — 0 hits outside kotoba (instrument + round-92/93 fixtures/receipts/reports).
- **INSTRUMENT_PINS** (case-insensitive) — 28 files, all `instrument_pins`-class receipt/tool **data**, none
  a copy of kotoba's iterate-a-pins-dict guard: kaidoku `red_controls.py:339` (builds the dict, folds at
  `:829-837`), `probe.py:621-628` (pins vs worktree dict **equality** — a dropped key breaks equality, i.e.
  fail-closed, the opposite class), `drive.py:241`, claims/acceptance/receipt JSONs; kake r95
  `battery_driver.py:136` (`instrument_pins=8/8 ok` — a counted tally, drop-visible); tameshi r56 report
  `T56W1CritC1.md:323-331` quotes a **historical** counter with its own INSTRUMENT_PINS loop where a dropped
  key IS silent — the same class, but a closed round artifact, not a live sibling instrument; mado r49 /
  chousa r65,r80 / kengaku r82 / kama r47 / kumitate r65,r80 hits are prose or copies of kotoba's QUALITY.md
  referencing kotoba paths.
- **check_tip_battery** — no sibling runs or forks it; every hit is an overlap note citing kotoba
  (`kengaku …/round-82/w1/ConnectorR82.md:91`, `kama …/round-47/w1/out/N1Overlap.md:70`,
  `kumitate …/round-65/w1/K65ConnOverlap.md:22` and `round-80` notes, `chousa round-80` anchor-search copies
  of kotoba QUALITY Q65/Q66).

**Verdict:** the F-4 silent-key-drop class is kotoba-local. C2's fix has no cross-lane propagation surface;
kaidoku's and kake's pin mechanisms are already drop-visible; no sibling shares a byte of either instrument.

## Part 3 — seat-name uniqueness (Q69)

Fleet-wide `find` over `/home/vgpnk/Projects/shokunin` (.git/.jj pruned) for all 12 names
(ExecKillPinRev, ExecPinCoverage, ExecReceiptRevs, ScoutGitRevs, ScribeCorpusR93, ConnectorOverlapR93,
ReviewerKillPin, ReviewerPinCov, MutTesterKillPin, MutTesterPinCov, CriticClaimsR93, SentinelScopeR93):
the only hits are `kotoba-shokunin/.ufo/waves/round-93/w1/{ExecKillPinRev, ExecPinCoverage/,
ExecPinCoverage.patch, ExecPinCoverage_READY, ExecReceiptRevs}` (nine seats had no files on disk yet at read
time — dirs are created lazily). Concurrent sibling waves run rounds 94-99 (kotodama 94-96, kake 95-97,
mori 95-97, kaidoku 96-98, revenger 96-98, lore 97-99; kengaku 91-92, kumitate 89-91, and older lanes are
static): **no sibling round-93, no name reuse.**
**Uniqueness verdict: UNIQUE — no finding.**

## Risks

1. O3/O4 are the build-time constraints for ExecKillPinRev (insertion window `check_mutation_battery.py:367-371`;
   never touch `:356-358`, materialize `:308-310`, the restore line, `KILL_SET_PINNED = 17` at `:87`, or
   `manifest.tsv` — the kill set stays 17).
2. O5/O6 are the constraints for ExecPinCoverage (literal dict at `check_tip_battery.py:132`; key-based check
   before the `:343` loop; reseed the six required keys in every self-test fixture world).
3. The r92 honest controls can only certify lane-resolvable revisions; mid-wave candidate readings flow only
   through the round-93 counters' `REPO` argument — receipts must name both rev and repo (O8b).
4. Frozen counters outlive the 120 s probe cap; one counter run at a time per seat (bounds already state it).

## Verification (for the integrator)

- `git -C <lane> rev-parse HEAD` == `6d7eee0…` while reading (it was).
- Re-run any cited grep at the freeze; `bash verifiers/fixtures/round-92/controls-run.sh` at the freeze reads
  `shortcuts refused 2 of 2; honest held 2 of 2`, rc 0 (frozen bytes; unaffected by either patch per O1).
- Landing-time re-check per O2: the two honest controls at the landed rev.
