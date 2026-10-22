VERDICT: HOLDS-BOUNDED — the one SCORECARD edit this round made (the routed-defect D2 qualifier on the operability row) is true at HEAD. But 5 of the 23 current-state statements checked in SCORECARD.md and SHONEN.md do not match HEAD, and SCORECARD.md has no round-51 record of the C1 or C2 moves.

# CriticCalibrationRows — calibration attack on SCORECARD.md and SHONEN.md at HEAD 59903b26

Attacks: how well the lane's self-assessment matches the repo at HEAD `59903b2637689739a5b9901956301da72d0effe1` (axis: calibration, the owned consistency sub-axis).
Method: I ran every statement in a private clone at HEAD, inside a copied fleet layout (BaseReplay.md § Setup: `.ufo` and `PROTOCOL.md` copied, sibling lanes symlinked), at scratch `/fast/scratch/hyaku/kotoba-r51/falsify/CriticCalibrationRows/`, between 2026-10-22T15:15Z and 15:18Z. Gate logs are in `logs/*.log` there; each log has a `# cmd:` header and an `# exit_code:` trailer.
Scope rule: I counted only statements written as current state (present tense, capability evidence, the annotation's "for current status", the `Next: round 51` block, and the SHONEN evidence lines). I did not count records labelled "round N".

## Count
N = 23 statements checked, M = 5 mismatches.

## Mismatches (M = 5)
1. **The substrate-pin capability row in SCORECARD says `--self-test` gives `'0 failure(s) over 51 assertions'`.** HEAD prints `0 failure(s) over 62 assertions`, exit 0. The row has no annotation, and the floors guard also records pins as 62.
   Command: `python3 -B verifiers/check_substrate_pins.py --self-test`.
2. **The Round 41 calibration annotation under the Capabilities table says the floors registry "has nine rows" and tells readers to "use the nine-row vector for current status" (`10/145/86/87/1597/62/104/118/150`).** HEAD has 12 rows, all PASS with observed equal to floor, exit 0: harness 10, corpus_integrity 150, corpus_independent 91, surfaces 115, checklist 1851, pins 62, harness_independent 123, compare_harness_independent 330, floors_guard 150, dispatch_prompts 56, sibling_census 68, overlap_levers 22. Six of the nine stated values are wrong (145, 86, 87, 1597, 104, 118), and three rows are missing. Round 51's own floors (surfaces 115, overlap_levers 22) appear nowhere in SCORECARD.
   Command: `python3 -B verifiers/check_assertion_floors.py`.
3. **The dispatch-prompt box check capability row says "no gate runs `--box-proof`".** At HEAD the checklist gate does run it. `checklist.box_map_complete` reports PASS with detail `delegated verifiers/verify_dispatch_prompts.py: --box-proof exit 0: boxes proven 2`. The code is `verify_skill_checklist.py:960` `supports_box_proof`, `:985` `delegated_box_proof`, and the call at `:1263-1268`. The row also contradicts the operability row's round-50 segment and its round-51 qualifier. The corrected wording should be "runs it, fails open when the help probe does not advertise the flag".
   Command: `python3 -B verifiers/verify_skill_checklist.py --json` (exit 0, pass 11).
4. **The `Next: round 51` block (SCORECARD line 122) still lists "the omp 18.12.6 re-pin (open Q09 debt …)".** At HEAD that debt is closed. The pins check gives `OK 3/3 pins hold`, exit 0, with omp sha256 `85d9daf3…07ccfa4` and mtime delta 0 ns. The surfaces check gives `pass 7, fail 0`, exit 0 against the same binary. Round 51's C1 commit `e0320302` closed the debt, but there is no correction note and no "Round 51 completed" line. The newest freshness statement is still the freshness row's round-48 "open freshness debt per Q09" (DRIFT 2/3, surfaces 5/7).
   Commands: `python3 -B verifiers/check_substrate_pins.py` and `python3 -B verifiers/verify_surfaces.py --json`.
5. **SHONEN box 1's evidence says "38 Sources entries".** HEAD has 39 using the same count as round-46 scout B2. There were 38 at B2's frozen HEAD `055d3b9`, and 39 at both BASE `43ca0bf` and HEAD, so this was stale before round 51 and did not change this round. The other three counts on that line still match: 7 anatomy rows, 5 decision rows, and 41 boxes split 15/9/9/8.
   Command: `git show <rev>:SKILL.md | awk '/^## Sources/{f=1;next} /^## /{f=0} f && /^- /' | wc -l` gives 38 at `055d3b9`, 39 at `43ca0bf`, and 39 at HEAD.

## Matches (18)
- **Substrate-pin guard:** exit 0, `OK 3/3 pins hold`, omp mtime `delta 0 ns`.
- **Round 41 annotation:** the guard passes everything at observed equal to floor, and its own self-test is 150 (the floors_guard row shows observed 150).
- **Dispatch-prompt box check, `--box-proof --map verifiers/checklist-baseline.json`:** prints `boxes proven 2`, exit 0.
- **Dispatch-prompt box check, missing fixtures:** there is no fixture for an unsubstituted variable or for a non-digit round folder. The manifest has 9 cases, none of either kind. Self-test is 0 failures over 56 assertions.
- **Sibling-description check, self-test:** 68, floored at 68 (`--self-test` exit 0).
- **Sibling-description check, false ownership sentence passes:** confirmed. My length-neutral probe replaced "kama owns endpoint verification" with "kama owns all SKILL.md audits" and the guard still printed `9 of 9`, exit 0. The `Next: round 51` owner-phrase candidate is therefore still needed.
- **Sibling-description check, repeated lane:** rejected. With the kake row duplicated in a copy of PROVINCE.md, the guard exits 1: `lane kake appears in more than one row`.
- **Sibling-description check, description over 1,024 characters:** fails. A 1063-character copy exits 1.
- **Adjacency row, "1,019 after the falsify-wave … correction":** the guard prints `skill description length 1019 of 1024`, and `names 9 of 9`, exit 0.
- **Operability round-51 qualifier, "The one live delegate advertises the flag and is green":** true. See the box_map_complete detail in mismatch 3.
- **Operability round-51 qualifier, the fail-open functions it names:** `supports_box_proof` and `delegated_box_proof` exist at `:960` and `:985`.
- **Operability round 50, "the checklist gate now runs each delegated instrument's `--box-proof`":** true.
- **Coverage row, "verify_surfaces.py 7/7":** true. HEAD shows 7 pass, exit 0.
- **`Next: round 51`, the callee finding:** `.ufo/waves/round-50/build/BaselineGatesB.md:34-43` does name `Kl`, `Ho`, `bq` and the `S$` rebind.
- **SHONEN box 1, the other three counts:** 7 anatomy rows (SKILL.md:66-72), 5 decision rows (:169-175), and 41 boxes split 15/9/9/8 (`grep -c '^- \[ \]' SKILL.md` gives 41, and the per-section awk gives 15/9/9/8).

## Gaps I did not count in M (the scorecard says nothing, so there is no statement to falsify)
- **G1. SCORECARD.md has no record of round 51's landed moves.** `grep -c -i 'overlap.lever\|round 51\|round-51' SCORECARD.md` returns 2. Those two hits are the D2 qualifier on line 31 and the `Next: round 51` plan on line 122. Not recorded:
  - C1 freshness: surfaces 5/7 → 7/7, pins DRIFT 2/3 → OK 3/3, floors 99 → 115, plus the new overlap_levers floor of 22.
  - C2 depth: `overlap levers backed 0 of 7 clients` → `7 of 7`. I re-ran `python3 -B verifiers/check_overlap_levers.py` at HEAD and got `7 of 7`, exit 0.

  This breaks the lane's own precedent. Rounds 49 and 50 wrote their move-log rows in their landing commits: `git log --oneline -- SCORECARD.md` lists `c48793d` (round-49 C2) and `956ee16` (round-50 "SCORECARD round-50 rows"). The round-51 diff of SCORECARD.md is 1 line changed (`git diff --stat 43ca0bf HEAD -- SCORECARD.md`).
- **G2. The two corpus gates are red at HEAD, and SCORECARD's newest integrity statement says green.**
  - `python3 -B verifiers/verify_corpus_integrity.py --json` exits 1 with 8 PASS and 1 DRIFT (`corpus.pointers.report_dead` observed 2).
  - `python3 -B verifiers/verify_corpus_independent.py --json` exits 1 with the same DRIFT.

  The newest SCORECARD statement is the calibration row's round-47 "exit 0, 9/9". It is labelled round 47, so I did not count it. The HEAD commit message does disclose "8/9 (report_dead 2 carried)", but that disclosure lives only in commit text, not in the self-assessment.
- **G3. The newest Saturation running window is stale.** The round-46 refresh says "no capability row has entered since round 29", but rows entered at rounds 49 and 50. It is labelled round 46 and is not a gate statement, so I did not count it.

## Axes affected
- Calibration, including the owned consistency sub-axis: all five mismatches and G1–G3.
- Freshness: mismatch 4 and G1.
- Operability: mismatch 3.
- Adjacency: no mismatch. Its bounded claims hold, including the lexical-test bound.

## What is a defect and what is a tradeoff
- Mismatches 1–5 and G1–G3 are fixable defects. Every one is a stale or missing record; no gate behaviour is wrong.
- The verifiers themselves agree with what the lane says is bounded about them.
- Only mismatch 4 and G1 are caused by round 51. Mismatches 1, 2, 3 and 5 were stale before round 51 and are carried over.

## Smallest safe correction (append-only, the lane's idiom)
1. Add a round-51 annotation under the Capabilities table, with the commands above:
   - pins self-test is 62;
   - the floors registry has 12 rows, with the vector from mismatch 2;
   - the dispatch row's "no gate runs `--box-proof`" is superseded: the checklist gate runs it and fails open when the help probe does not advertise the flag.
2. Add a correction note under the `Next: round 51` block: Q09 closed at `e0320302` (pins OK 3/3, surfaces 7/7, omp 18.12.6 sha `85d9daf3…`). Add a "Round 51 completed" line and two move-log rows, one for freshness C1 and one for depth C2, each with before → after and its command.
3. In SHONEN box 1, recount Sources to 39 and give the awk command.
4. Record the current corpus-gate state, 8/9 with exit 1 and report_dead 2 carried, in the calibration row or the round-51 note.

## Evidence (exit codes verbatim)
These ran in the clone at HEAD 59903b26.

| Command | Exit | Result |
|---|---|---|
| `python3 -B verifiers/check_substrate_pins.py` | 0 | `OK 3/3 pins hold` |
| `python3 -B verifiers/check_substrate_pins.py --self-test` | 0 | `0 failure(s) over 62 assertions` |
| `python3 -B verifiers/verify_surfaces.py --json` | 0 | pass 7, fail 0 |
| `python3 -B verifiers/check_assertion_floors.py` | 0 | 12 PASS rows |
| `python3 -B verifiers/verify_dispatch_prompts.py --box-proof --map verifiers/checklist-baseline.json` | 0 | `boxes proven 2` |
| `python3 -B verifiers/verify_dispatch_prompts.py --self-test` | 0 | 0 failures over 56 assertions |
| `python3 -B verifiers/verify_skill_checklist.py --json` | 0 | pass 11; box_map `41 boxes mapped (8 executed, 2 delegated, 31 unexecuted)` |
| `python3 -B verifiers/check_overlap_levers.py` | 0 | `overlap levers backed 7 of 7 clients` |
| `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md --skill SKILL.md` | 0 | 9 of 9, length 1019 |
| same guard with `--self-test` | 0 | 68 assertions |
| same guard with the false-ownership SKILL.md copy | 0 | 9 of 9, length 1017 |
| same guard with the 1063-character copy | 1 | fails on length |
| same guard with the duplicated-kake PROVINCE.md copy | 1 | fails on the repeated lane |
| `python3 -B verifiers/verify_corpus_integrity.py --json` | 1 | 8 PASS, 1 DRIFT `report_dead`=2 |
| `python3 -B verifiers/verify_corpus_independent.py --json` | 1 | DRIFT `report_dead`=2 |

## Bounds kept
- No writes in the lane except this report file.
- No git or jj write commands anywhere.
- No tool installed or upgraded, and no web source opened.
- Probes ran only in `.../CriticCalibrationRows/probe/`.
