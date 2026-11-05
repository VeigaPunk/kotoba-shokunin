# Round 92 — addendum 1 (L1 integration: repair, errata, disclosed deviations)

Author: KotobaR92 (L1, attempt 1). Freeze: `plans/round-92.md` and `plans/round-92-controls.md`
in commit `e073723ae667b64e534f8621bddb83ad12ad0e71`. Integration candidate measured at scratch
commit `cd355c4796fa165ff2b7d822401b4027da29e4d0` (lane tree snapshot, scratch identity); the
landing revision is the lane commit that carries the same bytes (named in the report).

**Timing disclosure.** Every entry below was written AFTER the wave-1 seats returned candidate
readings (their receipts under `.ufo/waves/round-92/w1/`). No entry changes a predicate sentence, a
counting command, a kill rule, a target, a control script, a probe, a manifest row, or a PROBES
entry. Where a text entry corrects my own frozen plan, the correction is an erratum: the frozen
bytes stay as committed, and the correct reading is recorded beside them.

## A1 — the fg-x1 anchor regression: repaired by moving the rung-3 check (D1, critic + mutation-tester F-1)

ExecLadderR92's rung-3 rewrite changed `verifiers/check_freeze_gate.py` `parse_expect` from
`control.expect_rc = int(m.group(1))` to `rc = int(m.group(1)) … control.expect_rc = rc`. The frozen
battery manifest row `fg-x1-parse-drop-exit-clause` (`verifiers/fixtures/mutation-battery/manifest.tsv`
line 9; NOT owned by any builder) anchors on the original two-line sequence, so the battery aborted on
the candidate: `could-not-evaluate: anchor miss: fg-x1-parse-drop-exit-clause edit 1 matches 0 time(s)`,
rc 2. Consequence: `ctl-c1-honest.sh` read `C1-PREDICATE-UNMET` rc 2 on the unrepaired candidate.
Evidence: `.ufo/waves/round-92/w1/CriticClaimsR92/CriticClaimsR92.md` D1 (replay
`receipts/anchor_replay.py`: base 19 edits 0 mismatches; candidate 1 mismatch) and
`.ufo/waves/round-92/w1/MutTesterBattery/MutTesterBattery.md` F-1.

**Repair (L1, integration only).** The rung-3 check moves ABOVE the anchored line, and the anchored
two lines are restored byte-identical to base:
```
            if int(m.group(1)) in (126, 127):
                raise SpecError(... exit %d is unobservable ...)
            control.expect_rc = int(m.group(1))
            continue
```
The manifest row, the battery PROBES and the anchor text are untouched. Anchor count in the repaired
file: `re.findall(r"            control\.expect_rc = int\(m\.group\(1\)\)\n            continue", src)` → 1.
The repaired freeze-gate blob is `0abfe8b1b3037cad614e99b7a0622a549cedf6e4`; the admission for it is
appended to `INSTRUMENT_PINS["verifiers/check_freeze_gate.py"]` in `verifiers/check_tip_battery.py`
(append only; the earlier blobs `a6f18c27…` and `856f543b…` are kept). The round-92 freeze-gate
self-test is unchanged in count (34) because no arm was added or removed.

**Able-to-fail evidence for the blocker and for the repair.** Before repair: candidate
`ctl-c1-honest.sh` → `C1-PREDICATE-UNMET`, rc 2 (critic receipt). After repair: see
`.ufo/waves/round-92/receipts/landing/` (`bat-rev.txt`, `ctl-c1-honest.txt`).

## A2 — plan-text errata (my own frozen wording; no predicate changed)

- **(i) `verifiers/fixtures/freeze-gate/r88-controls.md` is the REFUSAL fixture, not the honest
  world.** Plan § C2(b) says it "still exits 0". It exits 1 and names `w_added_red` at base and at
  the candidate (its frozen predicate is the refusal; `fg-r88-refusal-fixture.txt`). The honest
  world is `verifiers/fixtures/freeze-gate/r88-controls-fixed.md` (rc 0, 4 controls held). Correct
  reading: the honest counterpart the plan intended is `r88-controls-fixed.md`. (ReviewerFloors R1,
  MutTesterBattery F-3, CriticClaimsR92 D4.)
- **(ii) The landing no-harm conjunct "corpus integrity rc 0" was wrong at base.** `verify_corpus_integrity.py`
  reads `4/9 checks pass` rc 1 at base (`receipts/base-corpus-integrity.txt`, DRIFT on five checks; the
  carried reds are named in the plan's no-harm table). Correct landing conjunct: the DRIFT set at the
  landing revision is the base DRIFT set, with the expected round-92 growth on
  `corpus.index.tracked_files` and `corpus.index.index_patterns` only. (CriticClaimsR92 D5.)
- **(iii) The floors drift arm fires in the guard run, not in `--self-test`.** `check_assertion_floors.py`
  routes `--self-test` to `self_test()` before `registry_drift()` runs in `main()`. The plan's
  "floors `--self-test` FAIL (drift arm fires)" for a registry floor left at 31 is therefore wrong
  about the surface: the guard run (`python3 -B verifiers/check_assertion_floors.py`, no flag) reads
  `FAIL registry floor drift: freeze_gate registry=31 expected=34` rc 2
  (MutTesterBattery m6, F-2). The arm is real; the surface named in the plan is not.
- **(iv) Receipt pointers.** The plan's `receipts/census-before.txt` is at
  `.ufo/waves/round-92/census-before.txt`; the plan's `nowork-c1-controls.txt` was never produced — the
  do-nothing control is the committed pair `receipts/redbefore-ctl-c1.txt` and `receipts/redbefore-ctl-c2.txt`
  (run at the round-92 base tip `5031a782`, whose checker bytes equal the freeze base's); the plan's
  `q73-sweep.txt` is `receipts/q73-sweep-raw.txt`. The rp-m6 probe's BASE constant is `5031a782`
  (the pre-freeze tip); its checker bytes equal the freeze base's (the freeze commit adds plans and
  receipts only). (ReviewerCtl R12, MutTesterBattery F-6.)

## A3 — disclosed deviations from the frozen C2(a) wording (implementation, measured as the frozen red-before)

- `KILL_SET_PINNED = 17` is a **literal**, not "derived at load from the measured revision's committed
  manifest". A self-compare of a manifest against its own count cannot fail; the literal is what makes
  the arm able to fail (ExecKillPin report; CriticClaimsR92 D3a).
- The arm reads the **working-tree** manifest (`Path(__file__).parent.parent / MANIFEST`), not
  `git show <rev>:MANIFEST`. The frozen red-before world (`receipts/redbefore-m6-dropped-row.txt`) is a
  working-tree drop, so the frozen predicate's world is the working-tree world. Consequence (named,
  not hidden): a committed-revision dropped row is refused by the battery's baseline check with rc 2
  and does NOT name `kill-set-size` (CriticClaimsR92 D2: `could-not-evaluate: baseline bat-self-test exit
  1, declared 0`). This is a naming gap on the rev path, routed to round 93; it is not a silent pass.
- The tip battery's pin guard iterates `INSTRUMENT_PINS.items()`, so removing the whole key for a
  pinned path is silent (MutTesterBattery m7a, F-4). Routed to round 93; the tuple-omission mutant m7c
  is killed.

## A4 — carried findings (routed to round 93, not claimed closed)

- **F1 (MutTesterCtl).** `controls-run.sh` does not pin a refused world's exit code in its own
  counting path: a mutant that accepts a refused-world rc 0 scores `2 of 2` on the real worlds (the
  real worlds are correct, so the frozen counting cannot see the mutant). The candidate's refusal is
  shown by its stub, not by the frozen counting. Routed: a stub refused-rc-0 arm in the counter's
  self-test in round 93.
- **F-5 (MutTesterCtl, scope note).** The frozen counting takes ~7 minutes (438 s measured by the
  seat); the 120 s per-probe guidance binds probes, not the frozen counting, which runs once per
  landing.
- **R1 (ReviewerCtl).** The refused C2 world's stdout reads `FAIL guard instrument-pin: … is not a
  pinned blob`, not the plan's quoted `unpinned` / `guards G of 5` tokens. The scored counting line is
  unaffected; the plan's sentence is a description of the refusal, and the refusal's conjunct (the pin)
  is named. Recorded here as the plan-wording difference it is.

## A5 — inherited `r91-w1-results.json`

Already tracked at base (commit `931746a`, round-91 settlement). Not round-92 work.

## A6 — late round-91 seat files found in the lane tree

`.ufo/waves/round-91/w1/ReviewerRepairs.md` and `.ufo/waves/round-91/w1/ReviewerRepairs/` are
untracked in the lane at round-92 integration. They are round-91 `ReviewerRepairs` seat output
(the seat recorded dead; `r91-w1-results.json` records `FileNotFoundError` for the output). They are
committed under round 92 as wave evidence for round 91 with this disclosure, not deleted (evidence
is not destroyed). Attribution: the round-91 seat, late write; the round-91 lesson's "no late files"
line is corrected by this entry.
