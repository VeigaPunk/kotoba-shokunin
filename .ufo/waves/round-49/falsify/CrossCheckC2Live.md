# CrossCheckC2Live: round-49 falsify, dispatch instrument comparison (operability)

VERDICT: HOLDS-BOUNDED. Applies to the landed C2 figures (verifier output, box proof, mutation sensitivity) and to the dispatch.08 identity conjunct, which agrees on all 279 round files. Bounded by F1 (dispatch.04 is undercounted by one under the box's literal text) and F2 (the dispatch.08 PASS 250 rests on the round-49 authority re-word, which the blind instrument does not share).

## Provenance
- Judged bytes: clone of the lane at c48793dbe5eb30cd661f42ecad7399ae94e3d7ad (equals lane master) [C9]. Sha256 of the clone equals the lane working copy for verify_dispatch_prompts.py (512cff27...) and c2-independent-indep.py (86f11165...) [C11]. checklist-baseline.json (049429aa...) and SKILL.md (fa6ffc29...) were hashed in the clone only.
- Snapshot: scratch `prompts-snap`, 381 files; `diff -rq` against live `.ufo/prompts` exit 0 [C8b]. State copied with `cp -a` (`state-snap`, 81 entries: 80 plus the dotfile `.gitkeep`). Alt-next copied (`alt-next-snap`). Fleet mirror: 21 empty `<lane>-shokunin` directories (live root also has 21).
- Scratch root: /fast/scratch/hyaku/kotoba-r49/falsify/CrossCheckC2Live. Per-file table: out/per-file-diff.tsv (292 rows). Join output: out/join.txt.
- Installs or updates: none. Python stdlib and the existing git only.

## Commands (exit codes verbatim)
- C1: `python3 -B <clone>/verifiers/verify_dispatch_prompts.py --json --prompts <snap> --state-dir <state-snap> --fleet <mirror>` gives exit 1 (out/verifier.json). C1t, the same without `--json`, gives exit 1 (out/verifier.txt).
- C2: `python3 -B <clone>/.ufo/waves/round-49/build/c2-independent-indep.py --prompts <snap> --state <state-snap> --alt-state <alt-next-snap> --out out/indep.json` gives exit 0.
- C3: `python3 -B verifiers/verify_dispatch_prompts.py --box-proof --map verifiers/checklist-baseline.json` (clone root) prints `boxes proven 2`, exit 0.
- C4: verifier `--self-test` prints `0 failure(s) over 32 assertions`, exit 0. Blind `--self-test` prints `SELF-TEST PASS: 8 fixture arms behaved as specified`, exit 0.
- C5: `cmp out/verifier.json <clone>/.ufo/waves/round-49/build/c2-live-run-1115Z.json` exit 0; `cmp out/verifier.txt <...>/c2-live-run-1115Z.txt` exit 0.
- C6: mutation A (dispatch.08 disposition set to `unexecuted:none`, scratch map with SKILL.md copied alongside) prints `boxes proven 1`, exit 1. Mutation B (fixture d04-placeholder `<lane>` changed to `kote`) prints `boxes proven 1`, exit 1. Control prints `boxes proven 2`, exit 0.
- C7: `python3 -B join.py` in scratch, exit 0. Every count tagged [C7] comes from it.
- C8: inline Python in scratch (not saved), tagged [C8]. C8b: `diff -rq`.

## Reproduction of the landed records
| Record | Result |
|---|---|
| dispatch.04 FAIL on six `*-L1.md` with a `<lane>` report path (LOG:2372; SCORECARD:31) | REPRODUCES [C1, C5]. Kake, kasegi, kengaku, kotoba, kumitate and protocol each write `.ufo/reports/round-1/<lane>.md`. Qualified: the blind instrument FAILs seven (F1) [C7]. |
| dispatch.08 PASS 250, N/A 29 at 11:15Z (LOG:2372) | REPRODUCES exactly [C1, C5]: `279 file(s) evaluated: 250 PASS, 0 FAIL, 29 N/A; 13 out of scope`. |
| `boxes proven 2`, exit 0 (SCORECARD:255; LOG:2372) | REPRODUCES [C3]. |
| Capability row: each conjunct of each box can fail (SCORECARD:255) | HOLDS. The manifest has 9 cases, and all six conjuncts have a must-fail case. |
| Mutation claims: `boxes proven 1`, exit 1 (SCORECARD:31) | REPRODUCES [C6]. |
| Map 8 executed / 2 delegated / 31 unexecuted (SCORECARD:31) | REPRODUCES: 41 entries [C8]. |
| "Blind agrees on the six dispatch.04 failures" (SCORECARD:31) | TRUE BUT INCOMPLETE. Omits the blind's seventh FAIL and its 168 dispatch.08 FAILs (F6) [C7]. |

## Per-file disagreements (dispatch scope, 291 files)
dispatch.04 cross-tab (verifier, blind) [C7]: PASS/pass 259; FAIL/fail 6; N/A/pass 21; N/A/fail 1; out of scope/pass 4.
- N/A vs pass, 21 files: aggregator-round-4 to -12 (9 files) and protocol-round-4 to -15 (12 files). Cause F1. Both instruments read the stem as the lane id.
- N/A vs fail, 1 file: aggregator-L1.md, which writes `.ufo/reports/round-1/AGGREGATE.md` (aggregator-L1.md:9). Cause F1.
- Out of scope vs pass, 4 files: revenger, tabi, tameshi and tsukuroi `*-round-1-continuation-kaika.md`. Cause F4.
- Agree: the six L1 FAILs (same `<lane>` placeholder reasons) and kagi-L1 (PASS). `.gitkeep` is not a `.md`; both ignore it.

dispatch.08 identity conjunct (filename = role line = report dir) [C7]: 279 of 279 round files agree (PASS in both); verifier identity FAIL 0, blind identity FAIL 0. The parse layers (role round, report paths, stems) agree on 292 of 292 root files [C7].
- Out of scope vs pass, 8 L1 files: aggregator, kagi, kake, kasegi, kengaku, kotoba, kumitate, protocol. Cause F3.
- Out of scope vs pass, 4 continuation files. Cause F4.

dispatch.08 state conjunct (explains 250/29 and 168) [C7], cross-tab over 279 files (verifier, blind): PASS/FAIL 161; PASS/pass 89; N/A/FAIL 7; N/A/pass 22.
- 146 files in 15 lanes that have `.report-baseline`: blind FAIL against a stale `.round` (dated 2026-10-15). Verifier PASS against `.report-baseline`.
- 15 files, kotodama (4) and souji (11): no `.round` file at all. Blind FAILs them as "no state file" and labels the class state-bound-exceeded. Their `.report-baseline` values (52 and 22) would pass.
- 7 files in six stale-only lanes (aggregator 2, audio 1, game-dev-2d 1, game-dev-3d 1, lore 1, protocol 1): blind FAIL; verifier N/A ("state-stale, not compared").
- 22 files in the same six lanes: blind PASS against the stale `.round`; verifier N/A (same rule).

Per lane [C8] (verifier PASS or N/A; blind pass-fail against `.round`; blind counts include continuation files):
- N/A lanes: aggregator (.round 10) 9 N/A, 7-2; audio (1) 2 N/A, 1-1; game-dev-2d (1) 2 N/A, 1-1; game-dev-3d (1) 2 N/A, 1-1; lore (1) 2 N/A, 1-1; protocol (14) 12 N/A, 11-1.
- No `.round`: kotodama (baseline 52) 4 PASS, 0-4; souji (baseline 22) 11 PASS, 0-11.
- Baselined lanes (.round to baseline): chousa 1 to 28, 6 PASS, 1-5; kagi 16 to 28, 23, 14-9; kaidoku 1 to 25, 14, 1-13; kake 16 to 29, 25, 13-12; kama 1 to 25, 18, 1-17; kasegi 17 to 23, 17, 14-3; kengaku 13 to 29, 18, 10-8; kotoba 16 to 49, 18, 13-5; kumitate 18 to 39, 21, 15-6; mado 1 to 23, 13, 1-12; mori 2 to 25, 16, 2-14; revenger 1 to 62, 3 PASS plus 1 out of scope, 2-2; tabi 1 to 22, 12 plus 1, 2-11; tameshi 1 to 26, 16 plus 1, 2-15; tsukuroi 1 to 25, 15 plus 1, 2-14.

## Findings (ordered by severity)
F1 (medium; changes a count). `lane_kind` (verifier :161-175) and the dispatch.04 fleet-root branch (:345-359) exempt `aggregator` and `protocol` from the stem conjunct. Neither has a `<lane>-shokunin` repository, but both have state files. The judged box (SKILL.md:317-319 at c48793d) says "filename = the lane's `<id>`", with no exception. Effect: 22 N/A, including aggregator-L1.md, which writes AGGREGATE.md. The literal L1 dispatch.04 FAIL count is 7, not 6. No fixture covers the exemption (the manifest has none), so box-proof cannot detect it. The stem conjunct can never FAIL for those 22 files.

F2 (medium; explains the 250). The judged dispatch.08 text names `.report-baseline` (SKILL.md:329-334). Commit c48793d says "dispatch.08 authority re-worded to report-baseline" [C10]. The verifier implements that text faithfully (`state_source` :178-203), so the PASS is a judged-text verdict. Three caveats: (a) for all 17 lanes with a baseline, the baseline equals the lane's highest prompt round (kotoba 49, kotodama 52, revenger 62, and so on) [C8]. The check is a consistency test between prompts and one driver, not an independent one. (b) The 29 N/A files get no state comparison, and `_finish` (:449-454) still reports the check as PASS. (c) Under the base wording (`.round`, a5adc146 SKILL.md:325-327) the same files give 168 FAILs [C7]. The record discloses the re-word (LOG:2372) but not this consequence.

F3 (low; coverage). `evaluate_dispatch_08` drops every `*-L1.md` (:391-396, "carries none"). The judged identity conjunct still applies to the role line and report dir for those files. The blind instrument checks both, and 8 of 8 PASS. No verdict conflict, but 8 comparisons are never made.

F4 (low; scope). `ROUND_FILE_RE` (:92) matches only `-round-<N>.md`, so the four continuation prompts are never dispatched by the verifier. SKILL.md:306 names `*-round-N.md`, so the literal reading is defensible. Both instruments would pass them (round 1 against `.round` = 1 and baselines 22, 25, 26, 62).

F5 (latent; not on the snapshot). The parse layers agree on all 292 files [C7], so these show only in inline probes P1 (scratch, not saved):
- `**.ufo/reports/round-7/kote.md**` (bold markdown): verifier stem `kote.md**`, so dispatch.04 FAILs a correct path. Blind PASS.
- Role line `round-7` (hyphen) or a blank first line: verifier role is None, so dispatch.08 identity FAILs. Blind PASS.
- `{{lane}}` in a path: verifier PASS, blind FAIL. `<>`: verifier FAIL, blind PASS.

F6 (record). SCORECARD:31 says the blind "agrees on the six dispatch.04 failures." That is true, but it omits the blind's seventh FAIL (F1) and its 168 dispatch.08 FAILs (F2). LOG:2372 gives the verifier's figures without saying that the dispatch.04 count depends on F1. Both instruments' counts should sit side by side in the record.

F7 (blind instrument defects; low). (a) failure_class "state-bound-exceeded" is applied to the 15 no-`.round` files (blind bound branch, lines 248-256). (b) `failures_that_persist_on_alt_state` = 7 is `len(bound) - alt_pass`. Those 7 are the files with no alt value, and none is shown to persist. (c) `state_report_baseline` is recorded per file and never read. (d) Its header cites SKILL.md:313-315 and :325-327, which are base a5adc146 lines; the judged lines are 317-319 and 329-334.

Closure (89 files): out of scope for both (the verifier's `iterdir` is non-recursive, :304). Blind: dispatch.04 pass 89, dispatch.08 FAIL 89. Not compared.

## Residual risk and verification gaps
- The 250/29 split moves when the driver writes `.report-baseline`. Reproduction is on the snapshot taken at check time.
- Not run (outside this assignment): R1 repair, floors guard, corpus baseline, Q25, R4 count provenance.
- Off-snapshot parser behaviour (F5) is probed with five inline cases, not measured over a corpus.
- No web sources used. No installs.
