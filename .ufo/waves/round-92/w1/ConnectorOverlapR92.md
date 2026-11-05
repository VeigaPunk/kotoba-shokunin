# ConnectorOverlapR92 — r92-w1 cross-claim overlap, sibling copies, seat-name uniqueness

Read-only seat. Base: freeze commit `e073723ae667b64e534f8621bddb83ad12ad0e71` (lane HEAD equals it
at read time; `git status --porcelain` shows only round-92 wave paths). All line numbers are at the
freeze base unless marked *postimage* (candidate = base + ExecKillPin.patch + ExecLadderR92.patch,
verified by application in my scratch clone, clone deleted afterwards). Sources read in full first:
`plans/round-92.md`, `plans/round-92-controls.md`.

## 1. Shared surfaces among the round's code changes (O-list)

**O1 — check_freeze_gate.py self-test arms ↔ floors-registry drift arm (C2b-internal, three-file coupling).**
The drift arm `arm_floor_row` (`verifiers/check_freeze_gate.py:344-354`, asserts at :352-354
`row["floor"] == len(ARMS)`) reads the registry (`REGISTRY_REL` :68) and freezes the registry floor
to the live arm count. C2(b) appends three rung arms to `ARMS` (:512+, postimage :615-617) so
`len(ARMS)` moves 31 → 34; the same patch must move, and does move: `verifiers/floors-registry.json`
freeze_gate floor (:25-27, floor :26, 31 → 34) and both in-file tables of
`verifiers/check_assertion_floors.py` — `EXPECTED_INSTRUMENTS` freeze_gate :206 (31 → 34) and
`INSTRUMENTS` freeze_gate :292-293 (31 → 34). All four edits sit in ExecLadderR92's ONE patch, so
there is no half-bump window at integration; the floors guard's own drift machinery
(`check_assertion_floors.py:397-406, 426+`, registry read :762) would red any partial application.
Verified: candidate registry/tables/arms agree at 34 (textual; arms count 31+3).

**O2 — check_tip_battery.py INSTRUMENT_PINS (C2b) ↔ C1's honest worlds (cross-claim, cross-builder).**
`ctl-c2-honest.sh` (ExecCtlWorlds, not yet on disk) runs the public gates at the LANDING rev and
requires the instrument-pin guard to hold (`check_tip_battery.py:328-331` compares each pinned
path's rev blob against `INSTRUMENT_PINS` :132-152). ExecLadderR92's patch appends the admission for
its own changed floors-registry-listed blobs — check_assertion_floors.py postimage
`4ed35c4ea4925340f4752e7b02424f01b6026237` (postimage :145) and a NEW path entry for
check_freeze_gate.py `(a6f18c2…, 856f543…)` (postimage :146-152). Verified empirically: applying
both builder patches to e073723, `git hash-object` gives exactly 4ed35c4… (floors guard),
856f543bb6782af280e3a5a6b723f44532deac43 (freeze gate) — the pinned literals match the landing
blobs. The coupling is closed **as bytes**, but only while every patch is applied together: C1's
honest ctl is evidence about the integrated revision, not about ExecLadderR92's patch alone.

**O3 — check_mutation_battery.py (C2a) ↔ pins/registry: NO coupling.**
ExecKillPin's postimage blob is `263204a0fed26a74a998a9cdf6318ec3f0eb5c9a`; check_mutation_battery.py
is neither floors-registry-listed (`floors-registry.json` instruments, 19 rows) nor
INSTRUMENT_PINS-pinned (six scripts, :133-151). No admission needed; the gate registry stays 74 rows
(no new gate rows — controls are freeze-gate-executed fixtures). Q73 sweep reproduced:
`check_assertion_floors.py:15,290,292`, `check_freeze_gate.py:2,13,350`, battery constants :55-58 +
G3 fixture text :498 — no historical byte-pin outside the touch list.

**O4 — the battery's manifest read ↔ the C1 manifest-only world's rows (cross-claim).**
The read: `check_mutation_battery.py:343` `parse_manifest(git_show(lane, rev, MANIFEST))` (G1,
:121-123; MANIFEST :53), target-set check :344-345, parse refusals :140-146 (rid/target) and
:156-158 (**empty `edits` → CouldNotEvaluate, exit 2**). The v1 control
`verifiers/fixtures/round-91/ctl-c1-manifest-only.sh:10-11` appends a kill row with
`"edits": []` to the working tree and passes `--rev HEAD` of the unmodified base checkout, so the row
is never read (the defect). The planned v2 commits the row in the scratch clone and passes that rev —
the row then hits the :156-158 refusal → exit 2 "naming the row". ExecKillPin's patch adds only
`KILL_SET_PINNED` (:83-88 postimage), two helpers (:177-190) and three self-test arms (:766-779);
**parse_manifest and the predicate path are byte-unchanged by C2(a)**, so the exit-2 semantics C1's
v2 world depends on are untouched. Note: the battery names only the FIRST offending row per parse
pass (raises at :157), so "naming the rows" (plural) rests on the ctl script, not the battery.

**O5 — the shared constant 17.**
`KILL_SET_PINNED = 17` (battery postimage :83-88), `ctl-c1-honest.sh`'s expected
`killed 17 of 17 kill-set` (LINE_FMT :66, counts :390-397), and
`verifiers/fixtures/mutation-battery/manifest.tsv` (17 kill rows counted at freeze; file frozen,
outside every touch list) all derive from the same manifest. Consistent today; a future manifest
edit would break both claims at once — named, not smoothed.

**O6 — C2b grammar changes touch every declared plan the gate parses.**
Rung 2 (duplicate control names → exit 3, parse-time :187-190 postimage) and rung 3 (declared
exit 126/127 → exit 3, :125-131 postimage) apply to all plans: `plans/round-92-controls.md` (6
controls, unique names, no declared 126/127 — remains valid spec, verified by reading the six
declarations) and the r88 fixtures `verifiers/fixtures/freeze-gate/r88-controls.md` (must stay
exit 1) / `r88-controls-fixed.md` (must stay exit 0) — the patch keeps the self-test arms for both.
Also: rung 1's work-root check (:295-299 postimage) runs AFTER parse, so invalid spec (3) outranks
unusable work root (2); the default work root (`:249-254`, TMPDIR or gettempdir) is a real directory,
so normal runs keep exit-0/1 semantics.

**O7 — C1's new fixture dir vs C2 patches: zero write overlap.**
`verifiers/fixtures/` at the freeze contains `round-92-predata` but no `round-92` (git ls-tree) —
ExecCtlWorlds writes only new files; both existing patches touch only the five named
instrument/registry files. Disjointness proven by application: both patches applied sequentially to
one scratch clone, no conflict, and each patch's index base equals the freeze blob of its file
(aa409dc / a6f18c2 / 6f2c52f / bde784f / d16e05d) — both are e073723-based per the PATCH BASE rule.

**O8 — predata worlds flip by design (C2b vs frozen controls).**
`verifiers/fixtures/round-92-predata/fp-duplicate-names.md` and `fp-exit127.md` are the defect
worlds the new rungs now refuse (exit 3). The frozen pre-data controls plan must not be re-run at
the landing expecting `6 control(s) held`; the committed freeze receipts are the evidence of record.
No repair proposed — this is the controls' defect-demonstration design, and nobody may amend frozen
predicates.

**O9 — second-order: the tip battery's pinned path set grows 6 → 7.**
The new `check_freeze_gate.py` INSTRUMENT_PINS entry means every future rev that changes the freeze
gate needs a fresh admission (the round-91 `landing` mistake class, now permanently armed against
this file). Standing cost, by design of the coupling; named for the next round's plan.

## 2. Sibling copies (grep across /home/vgpnk/Projects/shokunin/, read-only; kotoba lane excluded from the sibling set)

`check_freeze_gate`, `check_mutation_battery`, `ctl-c2-capline-only`: **zero hits in any sibling
lane repo.** All hits are kotoba's own fleet-root report echoes:
`.ufo/reports/round-89/kotoba.md:9,34,57,103`; `.ufo/reports/round-90/kotoba.md:11,18,21,43,47,49,84,86`;
`.ufo/reports/round-91/kotoba.md:22,25,33,35,49,50,56,68,103`.

`controls-run`: no sibling carries kotoba's `controls-run.sh`; the sibling hits are each lane's own
unrelated receipt filenames/prose containing the token — souji-shokunin
`.ufo/waves/round-30/w2/SwarmExecutor07-receipts/` (`replay-controls-run2.tsv` manifest.sha256:240,
deliver-controls-replay.txt:19), souji `.ufo/waves/round-59/w1/S59Scribe.md:12,122`,
`S59Scribe/gate-draft.md:61`, `S59Reviewer/verified-sha256.txt:6`, souji `LOG.md:2791`;
kama-shokunin `.ufo/waves/round-42/w1/out/R42D02.md:118,172`; kama round-55 V4Receipts.md:53;
mado-shokunin `.ufo/waves/round-47/w1/ExecCounterC1.md:81`, `run-final-battery.sh:29`,
`w2/SentPrivacyW2/README.md:45-46`, `findings.md:90-91`; tabi-shokunin round-34
`w1-results.json:100`, `RevC1Controls.md:5`; tameshi-shokunin round-56
`T56W2ConnectorSeparability.md:55`, round-57 `d4-results.json:166`; kaidoku-shokunin round-52
`MutTriV6/receipts.tsv:4`, `MutTriV6/probe/collect_receipts.py:23`; chousa-shokunin round-61
`ScoutMistakesThisRound.md:17`; kagi-shokunin round-38 `build-results.json:10`;
kengaku-shokunin round-90 `ConnectorOverlap/receipts/names.txt:604`. Ran with gitignore on AND off
(identical sibling set; ignored-file pass added only untracked wave dirs). **Verdict: no sibling
copy of any of the four names exists.**

## 3. Seat-name uniqueness (Q69/M131)

This wave's registry (`.ufo/waves/round-92/w1/swarm-registry.json`, 12 members): ExecCtlWorlds,
ExecKillPin, ExecLadderR92, ScoutPyDocs, ScribeCorpusR92, ConnectorOverlapR92, ReviewerCtl,
MutTesterCtl, ReviewerFloors, MutTesterBattery, CriticClaimsR92, SentinelScopeR92.

Searched all 12 names over the LIVE sibling waves (revenger round-95, kake round-95/96, kaidoku
round-95/96, kagi round-43, souji round-68, kotodama round-93/94) and every other lane's
today-active wave dir (mori round-95/96, kengaku round-92, kasegi round-78, tabi round-68, tameshi
round-87, tsukuroi round-83, kumitate round-90, mado round-87, chousa round-80, revenger
round-92/94): **zero matches.** Historical same-lane reuse exists (ExecCtlWorlds was a kotoba
round-89 seat — `.ufo/reports/round-89/kotoba.md:18`; MutTesterBattery a kotoba round-90/91 seat)
but same-lane cross-round reuse is not a concurrent-sibling collision, and this round's R92/role
suffixes disambiguate. **Verdict: all 12 seat names are unique among concurrent waves. No finding.**

## Findings (contradictions named, not smoothed)

- **F1 — docstring vs ownership contradiction.** `check_assertion_floors.py:12` (docstring floor
  list) still reads "freeze_gate 31" after the floor moves to 34. The registry's own BUMP-IN-STEP
  RULE (`floors-registry.json:2` $comment) says registry + both tables + guard docstring move in one
  change; the plan's touch list gives ExecLadderR92 "the two in-file freeze_gate floor cells ONLY",
  which forecloses the docstring edit. The plan wins (frozen ownership); no gate reads the docstring
  (floors self-test arms swap table rows only, :818-1050), so nothing reds — residual is a stale
  narrative literal at :12, not a half-bump.
- **F2 — ExecCtlWorlds not yet on disk.** As of this read, `w1/` has no ExecCtlWorlds dir, patch, or
  READY (ExecKillPin: patch + 5 receipts + READY `KILLPIN-READY N=28`; ExecLadderR92: patch + 3
  receipts, no READY yet). O2/O4/O5 are the interfaces its build must honor; per my poll rules my
  item names no READY files to await, so I report what exists.
- **F3 — wording deviation, C2(a).** The plan pins the kill-set size of "the measured revision's
  committed manifest"; the patch reads the WORKING-TREE manifest
  (`Path(__file__).resolve().parent.parent / MANIFEST`, patch hunk at :766-769). They coincide on a
  clean tree; judgment on whether that satisfies the frozen sentence belongs to the claim's
  reviewers (MutTesterCtl/CriticClaimsR92), I only name it.
- **F4 — O8's flip** is expected behavior; any future re-run of `--plan plans/round-92-controls.md`
  at a post-landing rev REFUSES by construction (the r91 addendum-A5 shape in reverse).

## Connector move (one bounded proposal)

**Move:** ExecCtlWorlds (and ReviewerCtl) should read `ctl-c2-honest.sh`'s landing-revision
expectations against the INTEGRATED candidate — both builder patches applied — never against
ExecLadderR92's patch alone, and derive the admitted-blob check by reading the landing
`INSTRUMENT_PINS` rather than restating blob literals. **Why it improves an axis without harming
another:** it hardens C1's consistency verdict (the control's "public gates PASS" claim is about the
landing revision, and O2/O5 show its conjuncts live in two other builders' files), with zero new
writes and no change to any frozen predicate, counter, manifest or control byte. **Risks:** none to
bytes; only effort — the attack build already clones and applies patches named in its item.
**Verification:** `git clone` the lane at e073723 in scratch, apply both builder patches, run
`python3 -B verifiers/check_tip_battery.py --rev <candidate>` (guards line must read
`guards 5 of 5` with only the three carried red corpus gates failing) and
`python3 -B verifiers/check_mutation_battery.py --self-test` (`0 failure(s) over 28 assertions`).
Done by the owning seats; I verified the byte-level precondition only (hash-object evidence above).

## Verification performed by this seat

- `git -C kotoba-shokunin rev-parse HEAD` → `e073723ae667b64e534f8621bddb83ad12ad0e71`.
- `git clone --shared … $D && git -C $D checkout -q e073723…`; `git -C $D apply` ExecKillPin.patch
  then ExecLadderR92.patch → both applied, no conflict; `git -C $D rev-parse --show-toplevel` == $D
  before any step; clone + entire scratch dir removed before this report (`rm -rf` verified: path
  absent).
- `git -C $D hash-object` postimages → `263204a0…`, `856f543b…`, `4ed35c4e…` (all three match the
  pinned/admitted literals in the applied `check_tip_battery.py:145,151-152`).
- Freeze blobs `git rev-parse e073723:<file>` → aa409dc / a6f18c2 / 6f2c52f / bde784f / d16e05d —
  equal to each patch's index base (PATCH BASE respected by both builders).
- `awk -F'\t' 'NR>1 && $3=="kill"' manifest.tsv | wc -l` → 17 (24 lines total).
- Fleet greps (tool grep, gitignore on and off): four instrument/control names and twelve seat
  names, kotoba excluded — results in §2 and §3.
- No installs; no writes outside my two report paths and my (now removed) scratch.
