# CriticClaimsR92 — falsification of the frozen round-92 claims against the full candidate

Seat: CriticClaimsR92 (critic, leaf; no subagent dispatch). Candidate verdicts only; the L1 rules the round.

## Candidate built

- Base: `e073723ae667b64e534f8621bddb83ad12ad0e71` (freeze commit), scratch clone `git clone --shared` + checkout.
- Patches applied in order (all `git apply --index`, all clean): `ExecCtlWorlds/ExecCtlWorlds.patch`,
  `ExecKillPin/ExecKillPin.patch`, `ExecLadderR92/ExecLadderR92.patch`, `ScribeCorpusR92/ScribeCorpusR92.patch`.
- Candidate commit (scratch identity, scratch clone only): **`d92f4d60c5f10ad20096ff3271c0094096ec5083`**.
- READY files present before build: `ExecCtlWorlds_READY` (`CTL-WORLDS-READY 81f7c8b9…`), `ExecKillPin_READY` (`KILLPIN-READY N=28`),
  `ExecLadderR92_READY` (`LADDER-READY N'=34`), `ScribeCorpusR92_READY` (`CORPUS-READY`).
- Diff vs freeze: 14 files, +505/−11. Ownership audit: every changed path is in the touch list; `SKILL.md` unchanged;
  no `corpus/lessons/*-verifier-spotcheck.md` changed; `verifiers/fixtures/round-91/` byte-identical; frozen instruments
  (`check_r86_routed_repairs_v3.py`, `verify_corpus_integrity.py`, `corpus-baseline.json`, `check_gate_registry.py`,
  `verify_skill_checklist.py`) unchanged; `verifiers/fixtures/mutation-battery/manifest.tsv` unchanged; battery PROBES unchanged.

## Verdict summary

| claim | verdict on candidate `d92f4d60` | basis |
|---|---|---|
| C1 (controls refuse named shortcuts, honest worlds held) | **UNMET** | frozen counting command rc 1, observed `shortcuts refused 2 of 2; honest held 1 of 2`; honest battery world rc 2 (defect D1) |
| C2(a) kill-set size pin | **MET** on the frozen world (working-tree dropped row) — one naming defect (D2) on the committed-rev variant | self-test 28 rc 0; dropped-row world rc 1 naming `kill-set-size` |
| C2(b) three fail-closed rungs | **MET** on all three rungs, self-test 34, floors 176, coupling, tip guards 5 of 5 — one plan-text defect (D4) | rung probes + honest worlds + tip battery reproduced |
| Do-nothing control (§9) | **MET** (as predicted: 0 of 2) | base old pair observed |
| Census 190 → 192 | **MET** | 192 rows; validate rc 0; 0 lines removed |

## Claim C1 — MET/UNMET against the frozen counter

Frozen counting command: `bash verifiers/fixtures/round-92/controls-run.sh` (exit 0 iff the exact line
`round-92 controls: shortcuts refused 2 of 2; honest held 2 of 2` and every refused world names its conjunct).

Observed on the candidate (rc 1; stdout is the non-exact observed line; per-script receipts in `receipts/controls-run.stderr`):

```
C2-shortcut rc=1 met=yes
C2-honest rc=0 met=yes
C1-shortcut rc=1 met=yes
C1-honest rc=2 met=no
observed: shortcuts refused 2 of 2; honest held 1 of 2
```

Per script, run once each by `controls-run.sh`:

1. `ctl-c2-capline-only-v2.sh` → rc 1. Stdout names the missing conjunct:
   `C2-SHORTCUT-REFUSED: instrument-pin admission missing (FAIL guard instrument-pin: verifiers/check_assertion_floors.py blob a189e61b… at ea1db4ef… is not a pinned blob)`. World rev `ea1db4ef`; diff from freeze 1 file, 1 insertion, 1 deletion (`SELF_TEST_TIMEOUT_S 360 → 330`). MET.
2. `ctl-c2-honest.sh` → rc 0. `cap conjunct: SELF_TEST_TIMEOUT_S 360 >= 2 x MEASURED_SELFTEST_S 161: True`;
   `admission conjunct: floors blob 4ed35c4e… in INSTRUMENT_PINS: True`; `guard instrument-pin PASS`; `C2-PREDICATE-MET`. MET.
3. `ctl-c1-manifest-only-v2.sh` → rc 1. World rev `50d8cc17`, committed manifest carries `mb-c1-shortcut-kill`. Stdout:
   `could-not-evaluate: manifest mb-c1-shortcut-kill: target 'verifiers/check_gate_registry.py' has no probe set`;
   `C1-SHORTCUT-REFUSED: rows committed and read; instrument cannot evaluate (rc 2)`. MET (see D7 on what this refusal actually tests).
4. `ctl-c1-honest.sh` → rc 2. Battery at `d92f4d60` stops on:
   `could-not-evaluate: anchor miss: fg-x1-parse-drop-exit-clause edit 1 matches 0 time(s) in the revision bytes, expected 1`;
   `C1-PREDICATE-UNMET: battery could not evaluate d92f4d60… (rc 2)`. **UNMET** (D1).

Q26 headline check, C1 predicate sentence (`controls-run.sh` exits 0 with the exact line; each refused world's stdout names its missing conjunct; red-before receipts committed at freeze):

- "controls-run.sh exits 0" — turned on by the counter's rc: **1** → UNMET.
- "exact line" — turned on by the hard-coded echo, reached only when both counts are 2 of 2 → not reached.
- "each refused world's stdout names its missing conjunct" — both refusals print a named reason (C2: `instrument-pin admission missing`; C1: `rows committed and read; instrument cannot evaluate`) → MET; the C1 reason names the probe gap, see D7.
- "red-before receipts committed at freeze" — `git ls-tree e073723 -- .ufo/waves/round-92/receipts/` lists `redbefore-ctl-c1.txt` and `redbefore-ctl-c2.txt` → MET. **Not turned on by any counter output**: checked by hand, not by `controls-run.sh`.
- Clauses no counter turns on: receipt presence (above); "no control, counter, manifest or PROBES byte is amended after any scored reading" — no counter exists for it; verified by hand: `git diff --stat` shows the manifest and battery PROBES untouched.

## Claim C2(a) — kill-set-size pin

- Base reproduction (red-before): `base-battery-selftest.txt` = `0 failure(s) over 25 assertions` rc 0; the dropped-row world at base bytes (`base-m6-world.txt`): `kill rows before=17 after=16`, `0 failure(s) over 25 assertions`, rc 0. **Matches `redbefore-m6-dropped-row.txt` byte-for-byte.** MET (red-before).
- Candidate self-test (`cand-bat-selftest.txt`): `0 failure(s) over 28 assertions`, rc 0. N ≥ 26 MET. The three new arms are named `arm kill-set-size: …`.
- Candidate dropped-row world, working-tree variant (`cand-m6-wt.txt`): `kill rows now 16`; rc 1;
  `FAIL arm kill-set-size: the live manifest's kill-row count equals the pin :: observed 16 kill rows, pinned 17`;
  `1 failure(s) over 28 assertions`. MET (the frozen predicate's world).
- Committed-rev variant (D2): committed dropped-row world rev `4379e493`, `battery --rev` → rc 2:
  `could-not-evaluate: baseline bat-self-test exit 1, declared 0: the revision does not hold the frozen baseline`. Fail-closed, but the arm is not named on this path (`cand-m6-rev.txt`).

## Claim C2(b) — three fail-closed rungs

Base reproduction (all match the committed red-before receipts):

- `rp-work-regular-file` at base: `NotADirectoryError: [Errno 20] Not a directory: …/notadir/sub`, rc 1 (`base-rp-work.txt`; `redbefore-ladder-work.txt`).
- `--work` naming a regular file directly at base (`base-work-direct.txt`): `FileExistsError: [Errno 17] File exists: …/plainfile`, rc 1 — the uncaught sibling path.
- `rp-duplicate-names` at base: `freeze gate: 2 control(s) held — freeze may proceed`, rc 0 (`base-rp-dup.txt`).
- `rp-exit127` at base: `COULD-NOT-EVALUATE control one27 (line 6): command not found (rc=127)`, rc 0 (`base-rp-127.txt`).

Candidate, each rung (`cand-*.txt`):

1. `--work <file>/sub`: `COULD-NOT-EVALUATE --work …/notadir/sub: not a directory`, rc 2, no traceback.
   `--work <file>` (named regular file): `COULD-NOT-EVALUATE --work …/tmp/plainfile: not a directory`, rc 2.
   `--work <file>/sub` direct: `COULD-NOT-EVALUATE --work …/plainfile/sub: not a directory`, rc 2. MET.
2. duplicate control names: `INVALID SPEC: duplicate control dup (line 9): already declared at line 7`, rc 3. MET.
3. declared `exit 127`: `INVALID SPEC: control one27 (line 7): exit 127 is unobservable (126/127 are the harness's own could-not-evaluate codes; a declared 127 can never be compared)`, rc 3. MET.
   The probe scripts print `rc=1` on the candidate by construction (their pass condition is the defect); the defect-observed reading is the refused-after state, not the probe exit (see risk R1).

Other candidate readings:

- Self-test: `cand-fg-selftest.txt` = `0 failure(s) over 34 assertions`, rc 0. N' ≥ 34 MET.
- Floors self-test: `cand-floors-selftest.txt` = `0 failure(s) over 176 assertions`, rc 0. MET.
- Floor coupling: `floors-registry.json` `freeze_gate` = 34; `check_assertion_floors.py` `EXPECTED_INSTRUMENTS` (line 206) and `INSTRUMENTS` (line 292) = 34. MET.
- Honest worlds: `fp-minimal.md` → `freeze gate: 1 control(s) held`, rc 0; `r88-controls-fixed.md` → rc 0.
- Tip battery `d92f4d60` (`cand-tip.txt`): `guard no-deletions/floors/instrument-size/instrument-pin/spotcheck-identity PASS`;
  `gate verifiers/check_gate_registry.py exit 0`, `check_assertion_floors.py exit 0`, `verify_skill_checklist.py exit 1`,
  `verify_corpus_integrity.py exit 1`, `verify_corpus_independent.py exit 1`, `check_correction_sweep.py exit 0`;
  `fleet root …; guards 5 of 5; tip battery exit 0: 3 of 6`. MET (only the three carried reds).

## Do-nothing control (§9) — MET

Old round-91 pair on base bytes (`base-oldctl-c2.txt`, `base-oldctl-c1.txt`):

- `ctl-c2-capline-only` → `SELF_TEST_TIMEOUT_S=360`, `C2-PREDICATE-MET`, rc 0 (refuses 0 of 1).
- `ctl-c1-manifest-only` → `killed 14 of 14 kill-set …`, `C1-PREDICATE-UNMET`, rc 1 (refuses 0 of 1; unmet for the no-work reason, not the shortcut).
- No new arms exist at base: battery `25`, freeze-gate `31`. The do-nothing round cannot reach N ≥ 26, N' ≥ 34 or a refused world. MET.

## Census arithmetic — MET

- `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`: base **190**, candidate **192**.
- Added S-rows: `+| S265`, `+| S266`. Removed lines in `corpus/SOURCES.md` diff: **0**.
- `sources-census.sh validate --file <candidate SOURCES.md>` (run in candidate clone): rc 0; 33 W04 warnings carried (base count 33).
- Caveat: validate on a `/tmp` copy of the base file returned rc 1 with E11 (used-by paths unresolved outside the repo root). That is my copy location, not a base defect; base was not validated in place.

## Defects (numbered; command and observed output)

**D1 — BLOCKING. C1 honest battery world is unmeasurable at the candidate (regression from the freeze-gate patch).**
Command: `bash verifiers/fixtures/round-92/ctl-c1-honest.sh` (default rev `d92f4d60`), and the replay in
`receipts/anchor_replay.py`.
Observed: `could-not-evaluate: anchor miss: fg-x1-parse-drop-exit-clause edit 1 matches 0 time(s) in the revision bytes, expected 1`,
`C1-PREDICATE-UNMET … (rc 2)`. Anchor replay: base `e073723` — 19 anchored edits, 0 mismatches; candidate `d92f4d60` — 19 edits, **1 mismatch**
(`('fg-x1-parse-drop-exit-clause', 1, 'verifiers/check_freeze_gate.py', 0, 1)`).
Cause: manifest row `fg-x1-parse-drop-exit-clause` (manifest line 9) anchors `            control\.expect_rc = int\(m\.group\(1\)\)\n            continue`.
ExecLadderR92's rung-3 rewrite changed that line to `control.expect_rc = rc` (`check_freeze_gate.py:131`). The manifest is outside every
builder's ownership, so no seat saw the conflict. ExecKillPin's `killed 17 of 17` was measured on its own commit `f7f9e266`
(battery patch only), not the candidate. The battery stops on the first unmatched anchor, so the whole battery is unmeasurable at any
revision carrying the ladder patch, which is a no-harm regression beyond C1.

Smallest tested correction (scratch only, not landed):
- (i) restore the anchor line: `check_freeze_gate.py:131` `control.expect_rc = rc` → `control.expect_rc = int(m.group(1))` (semantically identical;
  `rc` is still used by the raise). Commit `2787079b`: anchor replay 0 mismatches; `check_mutation_battery.py --rev 2787079b` →
  `mutation battery killed 17 of 17 kill-set; equivalents survived 6 of 6; disclosed survivors 0 of 0`, rc 0 (`cf-battery.txt`);
  `check_freeze_gate.py --self-test` → `0 failure(s) over 34 assertions`; `ctl-c1-honest.sh 2787079b` → `C1-PREDICATE-MET`.
- (ii) the one-line change moves the blob `856f543b…` → `63874f42…`, so the tip battery's pin admission must also append `63874f42f1fa6f293d548ca617dd1c15153d82e2`
  to `INSTRUMENT_PINS["verifiers/check_freeze_gate.py"]` (append only). Commit `b4138c99` (both changes): `check_tip_battery.py --rev b4138c99` →
  `guard instrument-pin PASS`, `guards 5 of 5; tip battery exit 0: 3 of 6`, rc 1 from the three carried reds only (`cf2-tip.txt`).
- Owner: ExecLadderR92 (owns `check_freeze_gate.py` and the `INSTRUMENT_PINS` appends). Not verified: the rest of the round's landed state with this correction, beyond the two gates above.

**D2 — committed-revision dropped row is refused without naming the arm.** Command: committed world (drop one kill row, commit, `check_mutation_battery.py --rev 4379e493`).
Observed: `could-not-evaluate: baseline bat-self-test exit 1, declared 0: the revision does not hold the frozen baseline`, rc 2. The working-tree variant names `kill-set-size`
(`FAIL arm kill-set-size … observed 16 kill rows, pinned 17`). The frozen C2(a) predicate is met on the working-tree world, so this is a naming gap, not a predicate failure.
Cause: the arm reads the working-tree manifest (see D3), and a `--rev` run reports the probe-baseline failure instead of the arm.

**D3 — KillPin deviations from the plan text (L1 must accept or amend).** `ExecKillPin.md` states: (a) `KILL_SET_PINNED = 17` is a literal, not "derived at load"
as the plan's wording requires; (b) the arm reads `Path(__file__).parent.parent / MANIFEST` (working tree), not `git show <rev>:MANIFEST` as the plan requires.
The builder's reasoning for both is recorded in its report; the plan wording for (a) is self-contradictory (a self-compare cannot fail), and for (b) the frozen
predicate's "committed manifest" is the reason D2 exists. Either accept both in an addendum or implement the committed-rev read.

**D4 — plan text is false: `verifiers/fixtures/freeze-gate/r88-controls.md` does not exit 0.** `plans/round-92.md` § C2(b) says it "still exits 0".
Observed at base and candidate: `REFUSED control w_added_red (line 36)…`, rc 1 (`cand-r88unsat.txt`). The honest world is `r88-controls-fixed.md` (rc 0). Plan-text
error for an L1 addendum; no counter depends on the wrong text.

**D5 — plan no-harm conjunct cannot be met as written.** `plans/round-92.md` landing conjunct: "corpus integrity rc 0". Base is rc 1 (4/9, five DRIFT; `base-corpus-integrity.txt`).
At the same scratch location, base and candidate produce **identical DRIFT sets**; the only differences are the expected round-92 growth (`tracked_files` 189 → 190; `index_patterns` 206 → 207).
The `report_dead=1` line is a location artifact of my clone (it appears at base too). A fleet-shaped run was not performed (not in the lane). Plan text needs an addendum.

**D6 — scope: scribe patch edits an existing README row.** `corpus/README.md` diff: the row `Admission bar (round 46)` is rewritten with an appended
"**round 92:** Q83 appended …" sentence. The ownership text allows "index rows for the new corpus files ONLY". Minor; L1 may reject the hunk or accept with an addendum.

**D7 — C1 manifest-only control refuses for a probe gap, not for "rows unread" (scope risk; [INFERENCE] for the generalization).**
`ctl-c1-manifest-only-v2.sh:44-54` exits 1 only on the `could-not-evaluate: manifest mb-c1-shortcut-kill:` line (rc 2). If the appended row's target had a probe set and its
edit was killable, the battery would exit 0 with a different count, and the script would print `C1-SHORTCUT-ACCEPTED` (exit 0) — the script never checks the
`17 of 17` conjunct. The named shortcut (no-probe target) is refused as frozen; the broader claim is not tested by any counter. [INFERENCE — code path only, not run.]

## Risks

- R1. The `rp-*` probes exit 1 on the candidate by construction (their pass condition is the old defect). Any landing check that reads the probe exit code as the gate will
  misread a fixed rung; read the printed line instead (ExecLadderR92 raised the same point).
- R2. `controls-run.sh` prints the observed line on failure, not a copy of the frozen line; it is exact only when both counts are 2 of 2.
- R3. The tip battery's `fleet root` line reads the fleet root of the sandbox; in my scratch clone it printed my clone path. The `guards 5 of 5` reading is unaffected.
- R4. Installs / host: none. No tools installed or upgraded; no sysctl or kernel setting changed; no pacman used. No lane, fleet, or sibling write; the lane was only read.
- R5. Scratch: all counterfactual commits (`2787079b`, `b4138c99`) live only in my scratch clone; the lane is untouched. The scratch directory is removed before yield.

## Receipts (in `.ufo/waves/round-92/w1/CriticClaimsR92/receipts/`)

`controls-run.stdout`, `controls-run.stderr`, `base-*` (battery/freeze-gate self-tests, dropped-row world, old control pair, three rung probes, direct `--work` file),
`cand-*` (battery and freeze-gate self-tests, floors self-test, dropped-row worlds working-tree and committed, rung probes, honest worlds, tip battery, corpus integrity, validate),
`cf-battery.txt`, `cf2-tip.txt` (counterfactual D1 correction), `anchor_replay.py` (the anchor check used for D1).
