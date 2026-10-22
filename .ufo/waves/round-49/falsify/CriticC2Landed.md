# CriticC2Landed — round 49 falsify, C2 (operability) as landed

**Verdict: HOLDS-BOUNDED** for the C2 counter `boxes proven 2` and for the operability hold at 8.5. **FAILS** on two readings: that `dispatch.04` and `dispatch.08` are "executed as written", and the capability row's sentence "proves … that each conjunct of each box can fail".

Judged bytes: `master` at `c48793dbe5eb30cd661f42ecad7399ae94e3d7ad`, checked out in a private clone at `/fast/scratch/hyaku/kotoba-r49/falsify/CriticC2Landed/repo`. The live fleet was read at 2026-10-22T11:26:59Z. Attacked: `verifiers/verify_dispatch_prompts.py`, its fixtures and manifest, the `dispatch.08` box re-word in `SKILL.md`, the SCORECARD operability row, the moves row and the capabilities row.

## Findings

**F1 — `boxes proven 2` checks a narrower rule than the box text (operability, calibration).** The proof requires three things: the map entry, the pinned hash, and the instrument's own `CONJUNCTS` list (three per box) discriminated by 9 fixtures. It never checks that those conjuncts cover the box text. The `dispatch.04` box says "no `<…>` placeholder **or unsubstituted variable**". I ran the real `evaluate_dispatch_04`/`_08` on fixtures in scratch (`probe.py`):
- A placeholder in the round directory, `.ufo/reports/round-<N>/kote.md`, reads **N/A, not FAIL**, on both boxes. `REPORT_PATH_RE` needs `round-\d+`, so the path is never seen as a report path.
- `.ufo/reports/round-${ROUND}/kote.md` also reads N/A on both boxes.
- `${FLEET}/.ufo/reports/round-7/kote.md` and `$ROOT/.ufo/reports/round-7/kote.md` read **PASS** on both boxes. The prefix variable lies outside the matched span.
- A check reads FAIL only if some file FAILs, so a directory of such prompts reads N/A or PASS, never red.

**F2 — the proof survives instrument mutants, including one that erases the round's only live finding.** I monkeypatched the module in memory (no file edits) and called `box_proof` (`mutants.py`). Results:

| Mutant | `--box-proof` | `--self-test` |
|---|---|---|
| M1: variable clause deleted | `boxes proven 2`, exit 0 | exit 0 (0 failures over 32) |
| M2: legacy `.round` compared instead of `state-stale` | 2, exit 0 | exit 1 (2 failures) |
| M3: fleet-root-role branch deleted | 2, exit 0 | exit 0 |
| M4: only the first report path checked | 2, exit 0 | exit 0 |
| M5: `*-L1.md` files dropped from scope | 2, exit 0 | exit 1 |

Under M5 the live `dispatch.04` reads `PASS 279 file(s) evaluated: 258 PASS, 0 FAIL, 21 N/A` (`mutlive.py`). All six live FAILs vanish while the proof still prints 2. No fixture or self-test case covers the "unsubstituted variable" conjunct, so M1 survives both.

**F3 — the `dispatch.08` box was re-worded in the claim commit, so "executed as written" is circular.** The base map hash for `dispatch.08` was `c1e80da8…`. `PINNED_BOX_SHA` is `f5c37baa…`, which is the hash of the re-worded box. The pin proves only that `SKILL.md` and the instrument were committed together.

The plan said: "The full `dispatch.08` box is executed, state clause included; its live failures are findings" (`plans/round-49.md:76`). Against the box as written at base, the blind instrument failed **166 of 289** prompts (`DispatchIndependent.md:25`, J7). The landed box moved the authority to `.report-baseline` and added a `state-stale` N/A arm, which gives 0 FAIL. The SCORECARD says the second instrument "agrees on the six dispatch.04 failures". On `dispatch.08` the two instruments do not measure the same box, so nothing independent checks the re-worded box.

The re-word is disclosed and the reason for it is real: all 21 `.round` files are frozen at 2026-10-15. It is still a change of definition made in the claim round, not an execution of the earlier box.

**F4 — on the live fleet, the state clause checks the driver against itself.** `scripts/hyaku/inline.sh:98-100` calls `render_prompt "$lane" "$n"` and then `record_report_baseline "$lane" "$n"` in the same step. `shokunin-watchdog.sh:122-126` writes `"$n $digest"`. A driver-written `<lane>-round-N.md` therefore gets N ≤ baseline by construction. The clause can only fail if the baseline write fails after the render, or if a prompt is written by hand. Live result: `round_le_latest_dispatched` 0 FAIL out of 250 compared files.

Counterexample to the wording: the authority is the *most recent* dispatch, not the *highest*. Re-dispatching an older round would lower the baseline and turn every newer prompt into a false FAIL. [INFERENCE: not run on the fleet, because that would mean dispatching.]

**F5 — the fleet-root carve-out hides one literal-box FAIL and downgrades 21 PASSes.** The live `dispatch.04` has 22 N/A files, all aggregator or protocol prompts. In **21 of 22** the report stem equals the lane id, so the box as written PASSes them. The remaining one, `aggregator-L1.md`, has stem `AGGREGATE`, which the box as written FAILs. The literal live split would be 7 FAIL, not 6. The instrument's `out_of_scope` list names the carve-out; the SCORECARD row does not.

**F6 — no gate enforces `boxes proven 2`.** Nothing runs `--box-proof`: the floors guard reruns `--self-test` only (row `dispatch_prompts`, floor 32). In the scratch clone, a map that delegates `dispatch.04` to `verifiers/check_sibling_census.py` gives:
- `verify_skill_checklist.py --check checklist.box_map_complete`: `PASS … 8 executed, 2 delegated, 31 unexecuted`, exit 0;
- the box proof on that map: `boxes proven 1`, exit 1.

The round-49 sizing defect (`CriticC2Sizing`) is closed only for the one hand-run measurement. Nothing guards it after landing.

**F7 — hand sample of 10 live files: truthful under the instrument's model.** The files were every 29th non-fleet-root name: chousa-round-1, kagi-round-4, kake-round-18, kama-round-20, kengaku-round-14, kotoba-round-6, kumitate-round-9, mori-round-23, tabi-round-21, tsukuroi-round-20. For each I read line 1 and every `.ufo/reports/round-N/<stem>` occurrence:
- the role-line round, the report directory round and the stem all match the file name;
- each baseline is at least N;
- the instrument says PASS/PASS for all 10, so **10 of 10 agree**.

Extra spot checks:
- `kake-L1.md`: FAIL, correct (`.ufo/reports/round-1/<lane>.md`).
- `kotoba-round-49.md`: PASS, correct.
- `aggregator-round-10.md` and `protocol-round-15.md`: N/A, but the literal box gives PASS (see F5).
- `audio-round-101.md`: N/A, state-stale. The base box gives FAIL (101 > `.round` 1).
- `tabi-round-1-continuation-kaika.md`: out of scope for both boxes, although its role line and report directory carry round 1.

No false FAIL found. The false greens found are the N/A downgrades in F1 and F5.

**F8 — capability row under AXES.md § Capabilities: bounded.** The capability runs, and `--box-proof` passes (exit 0). The live run exits 1 with real findings, which counts as a passing demonstration of a checker.

Two defects:
- The row's "proves … that each conjunct of each box can fail" is false for the variable conjunct (F1, F2: M1).
- AXES says "a capability without a passing demonstration in the round report is pre-claiming". `.ufo/reports/round-49/` holds only `kotodama.md` (`ls -la`, exit 0), so the row is pre-claiming until the kotoba round-49 report shows the demonstration.

**F9 — operability hold at 8.5: honest.** The rubric needs "machine-checked or externally audited" for 9. 31 of 41 boxes stay unexecuted, and F1 and F2 show the new check is itself partial. A raise would not hold; a drop is not warranted, because nothing earlier regressed. The hold is right. The leftover "8.5 — was 8.0" cell text is stale from round 16 but harmless.

## Impacted axes

operability (instrument coverage of the box text; F1, F2, F6), calibration/consistency (capability-row wording, "executed as written", and the second-instrument agreement claim; F3, F5, F8). No harm to other axes was found.

## Smallest safe correction

1. Match `round-([^/\s]+)` and treat a non-digit round directory as a `report_path_literal` FAIL. Scan the whole path token, prefix included, for `$VAR` and `${…}`. Add fixtures `d04-variable` and `d04-round-dir-placeholder` to the manifest.
2. Add manifest cases that kill M2 to M5: a legacy-only state lane that must read N/A `state-stale`, a failing `*-L1.md`, a fleet-root file, and a two-path prompt whose second path is bad.
3. Run `--box-proof` from a gate (the checklist gate's delegated arm, or a floors-guard row) so that `boxes proven 2` is enforced.
4. Re-word the capability row to "each of the instrument's six named conjuncts". Record in the operability row that `dispatch.08` was re-worded in the claim commit, and that the box as written at base reads 166 of 289 FAIL (blind instrument). Either apply the stem conjunct to fleet-root roles (21 PASS, 1 FAIL `AGGREGATE`) or name that carve-out in the row.

## Evidence (commands, exit codes)

- `git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin repo && git -C repo checkout -q c48793dbe5eb30cd661f42ecad7399ae94e3d7ad`: exit 0.
- `python3 -B verifiers/verify_dispatch_prompts.py --box-proof --map verifiers/checklist-baseline.json` → `boxes proven 2`, exit 0.
- `python3 -B verifiers/verify_dispatch_prompts.py --self-test` → `0 failure(s) over 32 assertions`, exit 0.
- `python3 -B verifiers/verify_dispatch_prompts.py`, exit 1:
  - `FAIL dispatch.04: evaluated 287 — 259 PASS, 6 FAIL, 22 N/A; 28 out of scope`;
  - `PASS dispatch.08: evaluated 279 — 250 PASS, 0 FAIL, 29 N/A; 13 out of scope`.
  - This matches `.ufo/waves/round-49/build/c2-live-run-1115Z.txt`. The JSON form was saved as `live.json` (sha256 `f183a0bc…`), exit 1.
- N/A by lane for `dispatch.08`: protocol 12, aggregator 9, audio 2, game-dev-2d 2, game-dev-3d 2, lore 2 (Python Counter over `live.json`, exit 0). For `dispatch.04`, 22 N/A of which stem == lane id in 21 (same method, exit 0).
- `python3 -B probe.py` (sha256 `beefcce9…`), exit 0: results in F1.
- `python3 -B mutants.py` (sha256 `4f2d8f91…`), exit 0: results in F2. `python3 -B mutlive.py` (sha256 `041bf836…`), exit 0: the M5 live result.
- `git show a5adc146…:verifiers/checklist-baseline.json` → `dispatch.08` `text_sha256` `c1e80da8…`, compared with pinned `f5c37baa…` (instrument line 81).
- Scratch-clone remap check: `verify_skill_checklist.py --map verifiers/remap-probe.json --check checklist.box_map_complete` exit 0, and `--box-proof --map` on the same map gave `boxes proven 1`, exit 1. The probe file was removed afterwards.
- `check_assertion_floors.py` → `PASS dispatch_prompts observed=32 floor=32` (no box-proof row).
- Driver: `sed -n 85,110p scripts/hyaku/inline.sh` and `sed -n 115,150p scripts/shokunin-watchdog.sh` (read-only), exit 0.
- Tool installs or upgrades: none. Web sources: none opened. No lane, fleet or sibling writes apart from this report.
