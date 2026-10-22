# ReplayC2BoxProof: C2 box proof and instrument (round 49 falsify)

FAILS: applies to the claim that `boxes proven 2` shows both dispatch boxes executed as worded, with every conjunct discriminated. The literal counting command HOLDS at c48793d (exit 0, `boxes proven 2`). At base a5adc146 the instrument is absent (exit 2, no proof).

Scope: lane master c48793dbe5eb30cd661f42ecad7399ae94e3d7ad (origin/master equals HEAD of my clone). All runs in private clones under /fast/scratch/hyaku/kotoba-r49/falsify/ReplayC2BoxProof/ (head, base, mut-*, probe). No lane, fleet or sibling writes.
Tools: none installed or upgraded (read ~/.omp/agent/RULES.md). Used python3 3.14.8, git 2.56.0, jaq 3.1.1 (the `jq` on this host). No web sources.

## 1. Reproduction (exit codes verbatim)

| # | Command | Result |
|---|---|---|
| R1 | `python3 -B verifiers/verify_dispatch_prompts.py --box-proof --map verifiers/checklist-baseline.json` (head) | stdout `boxes proven 2`, exit 0; repeated at the end of the run, exit 0 |
| R2 | same command (base a5adc146) | `can't open file ... verify_dispatch_prompts.py`, exit 2; fixtures dir absent |
| R3 | `jq '[.boxes[]\|select((.box_id\|startswith("dispatch."))and(.disposition\|test("^(executed\|delegated):")))]\|length' verifiers/checklist-baseline.json` | 2, exit 0 (map-entry count, supporting only) |
| R4 | `python3 -B verifiers/verify_skill_checklist.py --json` (head) | exit 1; `checklist.box_map_complete` PASS, "41 boxes mapped (8 executed, 2 delegated, 31 unexecuted)". The three FAILs are environmental to my clone: `trigger.name_directory` (dir named `head`), `trigger.citation_resolves` and `governance.citation_resolves` (`../.ufo/reports` absent) |
| R5 | `python3 -B verifiers/verify_dispatch_prompts.py --self-test` (TMPDIR in scratch) | `0 failure(s) over 32 assertions`, exit 0 |
| R6 | `python3 -B verifiers/verify_dispatch_prompts.py --json` (default paths, read-only) | exit 1; see F7 |

Pin (question 2): instrument PINNED_BOX_SHA (verify_dispatch_prompts.py:80-81) = map text_sha256 = live SKILL.md hash under verify_skill_checklist's extract_boxes. dispatch.04 `62c20a81...0515` (SKILL.md line 317); dispatch.08 `f5c37baa...46d2` (line 329). The instrument's own dispatch_box_sha256 agrees on all nine dispatch boxes. HOLDS.

## 2. Findings

F1 HIGH. The proof does not execute the box text. The wording enters only as a SHA-256 pin (box_proof :782-790). The conjunct logic is hand-written (CONJUNCTS :84-90; evaluate_dispatch_04/08 :302-442) and runs on nine fixture directories.
- T1: dispatch.04 wording changed (adds "no leading `~`"), pins kept: exit 1, `boxes proven 1`, "live SKILL.md box hash 'e997b550...' != pinned '62c20a81...'". Skill box_map_complete FAIL. This part is correct.
- T2: same wording change, pin updated in instrument and map: exit 0, `boxes proven 2`. Skill box_map_complete PASS. No evaluator implements or tests the new clause.
So "proven" means: pinned text unchanged, and nine fixtures agree with hand-written code. It does not mean the wording is enforced.

F2 HIGH. Conjuncts as worded are not all covered. Committed corpus = manifest.json, 9 cases.

| Box wording (SKILL.md) | Instrument conjunct | Committed fixture | Gap and test |
|---|---|---|---|
| 04 "no `<...>` placeholder" | report_path_literal | d04-placeholder (FAIL) | placeholder before `.ufo/` PASSES (P2); `round-<N>` gives N/A (P3) |
| 04 "or unsubstituted variable" | report_path_literal (VARIABLE_RE) | none (no `$` in any fixture; self-test :552-730 has none) | M2 still `boxes proven 2`; `${FLEET}/` prefix PASSES (P1) |
| 04 "filename = the lane's `<id>`" | report_stem_is_lane_id | d04-stem (FAIL) | covered |
| not in wording | lane_identity_known | d04-unknown-lane (FAIL) | extra clause (F6) |
| 08 "identical across filename, role line" | filename_role_round_equal | d08-role-round (FAIL) | covered; M5 removes it silently (F4) |
| 08 "identical across ... report dir" | filename_report_dir_round_equal | d08-report-dir-round (FAIL) | `round-<N>` dir gives N/A, exit 0 (Q2) |
| 08 "<= latest dispatched" | round_le_latest_dispatched | d08-above-state (N > state) | equality untested: no fixture has N = state (control is 7 vs 9); M1 still `boxes proven 2` |
| 08 "legacy `.round` only: state-stale, not compared" | N/A branch :438-440 | none in committed corpus | M3 still `boxes proven 2`; only the self-test covers it (M3 self-test exit 1) |
| 08 "neither file: N/A" | N/A branch | d08-missing-state (N/A) | covered |

F3 HIGH (latent; no live hit found). An unsubstituted placeholder can PASS or go N/A, with exit 0.
- P1 `${FLEET}/.ufo/reports/round-7/kote.md`: dispatch.04 PASS, exit 0. Box says FAIL.
- P2 `<root>/.ufo/reports/round-7/kote.md`: PASS, exit 0. Box says FAIL.
- P3 `.ufo/reports/round-<N>/kote.md`: N/A "no report path found", exit 0. P4 `round-$R`: N/A, exit 0. Q2 (dispatch.08, `round-<N>` in dir): N/A, exit 0.
- Cause: REPORT_PATH_RE (:95) starts at `.ufo/` and needs digits; the check (:324-325) rebuilds the path from the match, dropping any prefix.
- Controls behave: P5 `round-7/$LANE.md` FAIL, exit 1; P6 `round-7/kote.md` PASS, exit 0.
- Live check (_grep over /home/vgpnk/Projects/shokunin/.ufo/prompts, gitignore off): no non-digit round token and no placeholder before `.ufo/`. Positive control `round-1/<lane>` matched six files, so the grep works.

F4 MEDIUM. The proof does not enforce its own coverage. M5 (manifest without d08-role-round): exit 0, `boxes proven 2`. M6 (manifest without both PASS controls): exit 0, `boxes proven 2`. "Every conjunct" and "every control" hold only for cases the manifest lists. Also d04-placeholder FAILs two conjuncts (report_path_literal and report_stem_is_lane_id), so it does not isolate its named conjunct.

F5 MEDIUM. SKILL.md lines 129-131 say `--box-proof` prints `boxes proven 2` only when both boxes are delegated there "and its committed fixtures discriminate every conjunct". The proof checks delegation and pins only. The committed corpus does not discriminate the variable clause, the equality boundary or the state-stale arm (M1, M2, M3). As written, the sentence is false.

F6 MEDIUM. Instrument scope differs from the wording (documented in the docstring, not in SKILL.md).
- (a) lane_identity_known is not in the box text.
- (b) Fleet-root roles (aggregator, protocol) are exempt from the stem clause (:345-359). Live: 22 of 287 dispatch.04 files (12 protocol, 10 aggregator) are N/A on that clause. No fixture or self-test arm covers the exemption (_grep for fleet-root, protocol, aggregator over fixtures and self-test: 0 hits).
- (c) dispatch.08 state-stale N/A matches the wording.

F7 LOW. Live fleet run (R6). dispatch.04 FAIL: 287 evaluated, 259 PASS, 6 FAIL, 22 N/A, 28 out of scope. The six FAILs (kake-L1, kasegi-L1, kengaku-L1, kotoba-L1, kumitate-L1, protocol-L1) all carry `.ufo/reports/round-1/<lane>.md`, so the lane's own kotoba-L1.md is a live finding. dispatch.08 PASS: 279 evaluated, 250 PASS, 0 FAIL, 29 N/A (all legacy state-stale). The check-level PASS hides those 29 N/A.

F8 INFO (holds). The nine fixture directories on disk equal the nine manifest directories. 9 cases: 2 PASS controls, 6 must-fail, 1 N/A. 25 fixture files tracked at c48793d (`git ls-files`), tree clean (`git status --short` empty), not ignored (`git check-ignore` exit 1). Both box extractors agree on all nine dispatch boxes.

## 3. Mutants and probes (scratch only; every row run)

| id | change | box-proof exit, stdout | self-test exit | result |
|---|---|---|---|---|
| head | none | 0, `boxes proven 2` | 0 | baseline |
| M1 | instrument :428 `<=` to `<` | 0, `boxes proven 2` | 0 | missed |
| M2 | instrument :158 drop VARIABLE_RE | 0, `boxes proven 2` | 0 | missed |
| M3 | instrument :440 legacy state to FAIL | 0, `boxes proven 2` | 1 | missed by proof, caught by self-test |
| M4 | instrument :362 stem never fails | 1, `boxes proven 1` | 1 | caught |
| M5 | manifest without d08-role-round | 0, `boxes proven 2` | not run | missed |
| M6 | manifest without PASS controls | 0, `boxes proven 2` | not run | missed |
| T1 | wording changed, pins kept | 1, `boxes proven 1` | not run | caught (hash) |
| T2 | wording changed, pins updated | 0, `boxes proven 2` | not run | missed (F1) |

| probe | input | CLI result | box says |
|---|---|---|---|
| P1 | `${FLEET}/...` report path | PASS, exit 0 | FAIL |
| P2 | `<root>/...` report path | PASS, exit 0 | FAIL |
| P3 | `round-<N>` report path | N/A, exit 0 | FAIL |
| P4 | `round-$R` report path | N/A, exit 0 | FAIL |
| P5 | `round-7/$LANE.md` | FAIL, exit 1 | FAIL |
| P6 | control | PASS, exit 0 | PASS |
| Q1 | dispatch.08, state 7, round 7 | PASS, exit 0 | PASS (untested by corpus) |
| Q2 | dispatch.08, `round-<N>` dir | N/A, exit 0 | FAIL |

## 4. Required fixes (not applied; read-only seat)
1. Check the whole report-path token including any prefix; make an unsubstituted round token FAIL, not N/A.
2. Add fixtures for: `$VAR` and `${...}`; N equal to state (PASS); legacy-only `.round` (N/A); fleet-root exemption.
3. Enforce in box_proof: each conjunct needs a must-fail case, each check needs a must-pass control, each fixture directory needs a manifest case.
4. Correct SKILL.md lines 129-131, or make the claim true.
5. Decide whether lane_identity_known and the fleet-root exemption belong in the box wording.

## 5. Residual risk and gaps
- Ran in git clones at c48793d, not the jj-colocated lane working copy. Same commit, so bytes match; the working copy was not inspected.
- Skill checklist exit 1 is environmental to my clone path; box_map_complete PASSED. Not re-run in a correctly named directory.
- Did not read LOG, SCORECARD or lessons for the claim text (records seat).
- Did not test other working directories; `--map` resolves SKILL.md relative to the map.
- F7 verdicts are the instrument's output; not adjudicated against each prompt's intent.
- [INFERENCE] dispatch_box_sha256 omits verify_skill_checklist's indented-code-marker rule. Both agree today; not exercised.
