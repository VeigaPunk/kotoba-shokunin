# CritCalibration — round 70 wave 1 (critic, read-only)

**Verdict: 7 calibration mismatches between the self-assessment in `SHONEN.md`/`SCORECARD.md` and the state at `16b212a390c7ce68b6bce49b2c3766b154fbcbae`.** Six are in the repo and one is on the host. Of the six repo mismatches, one is substantive: `SCORECARD.md` and `SHONEN.md` disagree about whether the round-11 cold run counts as non-author evidence, and the consistency axis's band 10 depends on that answer. The other five are stale pointers, a stale count, or a dead pointer. Line budget, Sources count, checklist boxes, LOG pointers, the cold-run record count, and all round-69 annotation numbers hold at the tip.

How I counted: a statement counts as a mismatch when it is the latest in-file statement of a quantity or pointer, the file still relies on it as current evidence, it differs from what the tip shows, and no later append-only note in the same file corrects it. A value pinned to an old revision counts as stale only when that pinned value is still the promotion checklist's or capability row's evidence.

Scratch: `/tmp/k70w1-CritCalibration.NKJr` (deleted before return). Gates that read `../` paths were run in a `git clone --shared` checkout of the tip at `$D/fleet/kotoba-shokunin`. Its parent `$D/fleet/` holds read-only symlinks to every entry of `/home/vgpnk/Projects/shokunin`, so the clone resolves `../` the same way the real lane does. Nothing was installed.

## Mismatches (counted)

### 1. SHONEN box 1: the gate-registry count is 42, the tip has 51 (stale)
`SHONEN.md:6` says `check_gate_registry.py --rev 80bb8921…` prints `gate registry rows conformant 42 of 42 lane verifiers; phantom 0`. That was true at `80bb8921`, but it is still the box's only registry evidence.
```
$ python3 -B verifiers/check_gate_registry.py --rev 16b212a390c7ce68b6bce49b2c3766b154fbcbae | tail -1
gate registry rows conformant 51 of 51 lane verifiers; phantom 0      (exit=0)
$ python3 -B verifiers/check_gate_registry.py --rev 80bb89211841289bc802fa7b55057f0ef266d19e | tail -1
gate registry rows conformant 42 of 42 lane verifiers; phantom 0      (exit=0)
growth: e94ae32a 44 · a5f7459f 46 · 9ce102b9 49 · 7d51253f 49 · 8edeb490 51 · 16b212a3 51
$ git ls-tree --name-only 16b212a3 verifiers/ | sed 's/.*\.//' | sort | uniq -c
50 py, 1 sh, 7 json, 1 md, 1 fixtures      → 50 .py + fault_injection_corpus.sh = 51 = registry rows
```
Registry rows and verifier files agree, and phantom is 0. The SHONEN figure is 9 verifiers behind (the r66–r70 counters).

### 2. SHONEN box 1: the `SKILL.md:241` pointer has moved to `:240` (stale)
`SHONEN.md:6` says the decision-shape pointer is `SKILL.md:241`, "unchanged at `c019919c`".
```
$ git show c019919c:SKILL.md | awk 'NR==241'   → "Decision-table shape (situation → table or plain steps) …"
$ git show 16b212a3:SKILL.md | awk 'NR==240||NR==241'
240: Decision-table shape (situation → table or plain steps) …
241: - **Testing a skill — the spec's own artefacts.** Hand-author `evals/evals.json` …   (round-70 C2 line, 8edeb49)
```
At the tip, `:241` points to the round-70 C2 bullet instead of the decision-table pointer.

### 3. SHONEN box 4: the PROVINCE line numbers have shifted, and the re-grep caveat names the wrong section (stale)
`SHONEN.md:12` says `grep -n '^## Adjacent' PROVINCE.md` prints `35:` at `c019919c` and that the round-49 rewrite sentence is at `:37`. The caveat says to "re-grep after any § Frontier append".
```
$ git show c019919c:PROVINCE.md | grep -n '^## Adjacent'   → 35:## Adjacent ; line 37 = "Sibling-owned ground … Rewritten round 49 …"
$ git show 16b212a3:PROVINCE.md | grep -n '^## '           → 8:## Core  30:## Frontier  37:## Adjacent
tip line 37 = "## Adjacent" (the heading); the rewrite sentence is now line 39
$ git diff a5f7459f 9ce102b9 -- PROVINCE.md | wc -l         → 13 (one hunk @@ -25,6 +25,8 @@, +2 lines in § Core)
```
The 2-line shift came from round 69's **§ Core** append, which the caveat does not cover. The guard itself still holds: `check_sibling_census.py … --province PROVINCE.md` prints `rows 20 verified 20` / `province rows 20 matched 20`, exit 0.

### 4. Band 10 for consistency credits as non-author the same cold run that SHONEN box 2 says is lane evidence (contradiction, unresolved since round 57)
- `SCORECARD.md:29` (consistency 10) says: "**Band 10 = repeated non-author verification in the opposite direction:** leg 1 was round 11's cold run (non-author checking the author's numbers), leg 2 is this derivation (non-author deriving the verdicts …)". `SCORECARD.md:334-335` (§ Saturation) repeats "consistency 10 (criterion met)".
- `SHONEN.md:8` says the round-11 cold run (`corpus/knowledge/cold-run-round11.md`) was run "by a lane-dispatched reviewer — lane evidence per `../PROTOCOL.md` § Promotion gates, no non-author credit claimed".
- `../PROTOCOL.md:63-65` says "a reviewer who did not author the round's changes — a fresh lane or integrator review, never self-attestation; **a subagent the lane dispatched is still the lane**."
- The record calls itself non-author: `cold-run-round11.md:3` "**NON-AUTHOR cold run.** The runner (lane `ColdRunRecord`) …". Round 12's leg 2 (`independent-verification-round12.md`) was also a lane-dispatched seat.
- `SCORECARD.md:152` records this exact item ("band-10 attribution, `SCORECARD.md:29`") as routed to the closure in round 57. `git grep -n -i 'band-10 attribution' 16b212a3` finds no later resolution.

So the two self-assessment files class the same act in opposite ways, and the score of 10 rests on the reading that PROTOCOL rejects for promotion. Smallest safe correction: an append-only note under `## axes` that either states why rubric "non-author" differs from the promotion gate's definition, or records band 10 as resting on lane-dispatched legs pending the closure's ruling. Do not change the score in-lane; that ruling belongs to the closure.

### 5. `SCORECARD.md:29` cites a band-10 evidence pointer that no longer exists (dead)
```
$ ls -d /tmp/round12/ExecIndependentVerifier/compare.md
ls: cannot access '/tmp/round12/ExecIndependentVerifier/compare.md': No such file or directory
```
This was flagged at round 21 (`.ufo/round-21/scouts/G4.md:56`) and is still in the live axis row. `governance.citation_resolves` checks only repo-rooted tokens, so no gate catches it.

### 6. The assertion-floor capability row has no current row count (stale)
`SCORECARD.md:312` says "reruns all six instruments". The latest in-file current-value correction is `SCORECARD.md:318` (round 51): "`check_assertion_floors.py` passes 12 rows". No later note restates the count. Rounds 65 and 66 record individual floor bumps (checklist 1852→1862, `scoped_rules_v32` 234→240), but not the total.
```
$ python3 -B verifiers/check_assertion_floors.py   (sandbox at tip)
PASS harness 10 · corpus_integrity 161 · corpus_independent 103 · surfaces 175 · checklist 1862 · pins 62 ·
harness_independent 123 · compare_harness_independent 330 · floors_guard 165/150 · dispatch_prompts 56 ·
sibling_census 68 · overlap_levers 55/51 · alwayson 89 · correction_sweep 25 · scoped_rules_v32 240      exit=0
$ grep -c '^PASS' floors.out   → 15
```
The tip has 15 rows. The capability row reads 6, and its latest correction reads 12.

### 7. Host state: the substrate-pin capability says 3/3 pins hold, the host now shows drift
`SCORECARD.md:311` says `check_substrate_pins.py` → `exit 0`, `OK 3/3 pins hold`. `SCORECARD.md:318` (round 51) re-affirms "pins `OK 3/3`".
```
$ python3 -B verifiers/check_substrate_pins.py
FAIL omp_binary_mtime: mtime drift … delta_ns=173397942086864 tolerance_ns=0
PASS opencode_binary_sha256: 538fcb1b…
DRIFT 2/3 pins failed: omp_binary_sha256, omp_binary_mtime          exit=1
$ python3 -B verifiers/check_substrate_pins.py --self-test  → 0 failure(s) over 62 assertions (exit 0; matches SCORECARD:318)
```
The omp binary on the host has moved. This is host state rather than repo state. It bears on the freshness row (8), which cites `pins OK 3/3` at `6dd31164`.

## Claims verified as holding at the tip (not mismatches)
| Claim (file:line) | Command | Observed |
|---|---|---|
| SHONEN:6 Sources = 18 (and 18/20/33/18 at cbbee56e/c63ccc68/07c33d73/80bb8921) | `awk '/^## Sources/{p=1;next} /^## /{p=0} p && /^- /' SKILL.md \| wc -l` per rev | 18 · 18 · 20 · 33 · 18 · tip 18 |
| SHONEN:6 "38 Sources entries" at the round-46 tree | same awk at `055d3b9a` (SKILL sha `0404fdc0…` = B2's pin) | 38. The round-51 note's "counts 39" (`SCORECARD.md:318`) measured `43ca0bfb`, a different tree; SHONEN's scoped 38 is correct |
| SHONEN:6 41 checklist boxes | `grep -c '^- \[ \]' SKILL.md` @tip; checklist `box_map_complete` | 41; "41 boxes mapped (8 executed, 4 delegated, 29 unexecuted)" |
| SHONEN:6 round-64 registry row present | `grep -n check_r64_routed_repairs SKILL.md` | `495:` |
| SHONEN:6 decision rows `anatomy-and-compression.md:102-108` | `git diff --stat c019919c 16b212a3 -- corpus/knowledge/anatomy-and-compression.md` | empty; 5 data rows at 104-108 |
| SHONEN:8 box 2 logged at `LOG.md:287,294,342` | `awk 'NR==287\|\|NR==294\|\|NR==342'` at 078eec4 and at tip | same three cold-run-round11 lines at both; they sit under `LOG.md:250 ## Round 11` |
| SHONEN:8 box 2 / r69 closure "needs a LOG round-69 entry" | `grep -n '^## Round 6[5-9]\|^## Round 7' LOG.md` | `2698:## Round 69 — appended correction entry …`. No `## Round 70` heading yet, and neither file claims one |
| SHONEN:10 "corpus/knowledge/ holds one cold-run record"; no fresh non-author cold run | `git ls-tree -r --name-only 16b212a3 corpus \| grep -i cold`; `git grep -i 'cold run'` over the r46–r69 lessons | one knowledge record plus the round-8 lesson; the r48/r49/r50/r51/r65/r69 spot-checks all say box 3 still rests on round 8 |
| SHONEN:10 round-8 lesson pointers `:36` `:37` `:78` | `sed -n` on the lesson | B1, B2, and "the recipe gap stands" at those lines. `:100` is the round-13 section heading; the quoted text is at `:102`, a section pointer and acceptable |
| SKILL.md line budget 600 / SCORECARD:394,420 "600 of 600" | `wc -l` per rev; `verify_skill_checklist.py --json` (sandbox) | e94ae32 600 · a5f7459 600 · 9ce102b 597 · 7d51253 597 · tip 600; `trigger.line_budget PASS 600 lines within budget 600`, 11/11, exit 0. No lines of headroom are left |
| SCORECARD:34 description 1,019 chars | checklist `trigger.frontmatter_parses` | "description 1019 chars" |
| SCORECARD:431 "round 69 left this file byte-identical"; :436 sha `41c07e39…` | `git rev-parse a5f7459f:SCORECARD.md 9ce102b9:SCORECARD.md` | both blobs `41c07e394ca5c02fbfae0459586efd3cbc2caa11` |
| SCORECARD:433-435 r69 counters at 9ce102b | `check_skill_precedence` / `check_r68_routed_repairs` / `check_province_core` `--rev 9ce102b9…` and `--self-test` | 5 of 5 · 8 of 8 · 2 of 2, each exit 0; self-tests 22 · 25 · 10, matching the annotation |
| SCORECARD:357 "PROVINCE.md carries no frontier inventory" | `grep -n '^## Frontier' PROVINCE.md` → `30:` | false at the tip, but corrected in-file by the append at `SCORECARD.md:363` (round 46), so not counted |
| No-harm gates at the tip | sandbox: `verify_corpus_integrity.py`; `verify_corpus_independent.py --json`; `check_assertion_floors.py` | `9/9 checks pass` exit 0; exit 0 (`report_dead 0`); exit 0 |

## Side finding (outside SHONEN/SCORECARD, relevant to C1): lesson M116 states its unsatisfiability too broadly
`corpus/lessons/round-70.md:136-142` (M116) says: "In any `/tmp` sandbox the three round-65 corrected tokens and 30+ other `../.ufo/…` tokens are dead, so the item reads FAIL at every revision". Counterexample: a `/tmp` sandbox whose parent directory holds the fleet layout reads PASS.
```
$ D=/tmp/k70w1-CritCalibration.NKJr; mkdir $D/fleet; symlink every /home/vgpnk/Projects/shokunin/* and .* entry (except kotoba-shokunin) into $D/fleet
$ git clone --shared … $D/fleet/kotoba-shokunin && git checkout 16b212a3
$ python3 -B verifiers/verify_skill_checklist.py --json → pass 11 fail 0 exit 0;
  governance.citation_resolves PASS 1253 governance citation token(s) resolve across 2 files …   (same line as receipts/K69-11-inplace.txt)
$ python3 -B verifiers/check_r69_routed_repairs.py --rev 16b212a3… → r69 routed defects closed 9 of 10 / K69-11: governance.citation_resolves FAIL, exit=1
```
The frozen counter is unsatisfiable because of how it builds its sandbox: `check_r69_routed_repairs.py:103-116` clones into `TemporaryDirectory()/clone`, which has no fleet siblings. Being under `/tmp` is not the cause. The claim standing as a miss is unaffected. The correction is a wording one: "in the counter's sandbox layout (`<tmp>/clone`, no fleet siblings)" instead of "in any `/tmp` sandbox".

## Impacted axes
- consistency (calibration sub-axis, owned, 10): mismatches 4 and 5 bear on the band-10 basis directly; mismatches 1–3 and 6 are stale self-assessment pointers and counts.
- freshness (advisory, 8): mismatch 7.
- C1/C2 claims: none of the mismatches change C1 (9 of 10 at the tip, observed above) or C2.

## Smallest safe corrections (for the L1; this seat edits nothing)
1–3: refresh SHONEN boxes 1 and 4 to the tip: registry 51 of 51, pointer `SKILL.md:240`, Adjacent `37:` with the sentence at `:39`, and a caveat that covers any append above § Adjacent. 4–5: an append-only SCORECARD note under `## axes` recording the attribution conflict and the dead `/tmp/round12` pointer, with the score ruling left to the closure. 6: an append-only capability note giving the floors count, 15 rows at the tip. 7: record the host drift; re-pinning is a separate freshness move.

Tools installed or updated: none.
