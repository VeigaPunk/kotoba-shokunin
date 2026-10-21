verdict: PARTIAL — attacked the four SHONEN.md boxes at 7ad7fad: boxes 1, 2 and 4 have a resolvable round-47 lane pointer that supports [~]; box 3 has no round-47 evidence at all (its [~] still rests on the round-8 cold run), and no box has a non-author verifier that could justify [x].

# W2ShonenEvidence — round-47 SHONEN boxes (falsify wave 2)

Lane: W2ShonenEvidence (leaf; no subagents). Target: the four boxes of `SHONEN.md` at tip
`7ad7fadfc09354b74fb66605dfb0c1182c115a2f`. Scratch clone:
`/fast/scratch/kotoba-r47/w2/W2ShonenEvidence/kotoba-shokunin` (canonical fleet layout, detached at tip).
Production `kotoba-shokunin` was read only; `SHONEN.md` was not edited and no marks were written.
`SHONEN.md` is byte-identical to BASE (`sha256 f012cd2f…`) and to the round-46 landing
(`git show f2f9ee1:SHONEN.md | sha256sum` → the same hash): all four boxes are `[~]`, none `[x]`.

Per `/home/vgpnk/Projects/shokunin/PROTOCOL.md:63-65`, a box is `[x]` only from a reviewer who did
not author the round, and "a subagent the lane dispatched is still the lane" — this report, and the
falsify wave that dispatched it, cannot supply `[x]` for any box.

## Box lines (one per box)

- Box 1 — `SHONEN.md:5-6` (decision tables, error patterns, checklists, cited sources): strongest round-47 pointer `.ufo/waves/round-47/build/ShonenEvidence.md:14-17` (wave-1 recount: 7 anatomy rows, 5 decision rows, 41 boxes 15/9/9/8, 39 Sources at BASE); tip re-measure confirms `SKILL.md:63-69`, `:157-161`, `:179-350`, `:369-528` and `verifiers/verify_skill_checklist.py --json` → "41 boxes mapped", and the round-47 edit at `SKILL.md:151` adds the S012 citation — **supports [~]** (lane-run); counterexample: `SHONEN.md:6` still says 38 Sources, the tip has 39.
- Box 2 — `SHONEN.md:7-8` (end-to-end domain task logged in LOG.md): strongest round-47 pointer `LOG.md:2317-2326`, with the C1 task at `LOG.md:2321` (omp 18.12.5 `lq`/`Xl`/`Fo`, opencode 1.19.3 npm/round-14 lineage, before→after in the same entry) — **supports [~]** (lane-run; no non-author reviewer); caveats: the after battery is untracked and the floors gate is load-marginal (F2, F3).
- Box 3 — `SHONEN.md:9-10` (instructions executable without oral context): strongest round-47 pointer `LOG.md:2319` (the replacement coordinator integrated the surviving wave-1 output after the host crash), which exercises the round's written handoff but not `SKILL.md`; no round-47 cold run of the skill exists — **does not support [~] as fresh evidence**; the mark rests on `corpus/lessons/round-8-aggregator-box3-coldrun.md:36-41`, and that file at `:44` records that a lane-dispatched reviewer does not count as non-author.
- Box 4 — `SHONEN.md:11-12` (no cross-domain bleed; PROVINCE.md still accurate): strongest round-47 pointer `PROVINCE.md:15` (round-47 Core row) plus `:22` (round-47 freshness annotation) — **supports [~]** for PROVINCE accuracy (21/21 backticked paths resolve; "33 of 41" matches the live `checklist.box_map_complete` detail; surfaces 7/7 and pins 3/3 reproduce at default resolution); the no-bleed half has no round-47 scan and still cites `.ufo/round-46/scouts/w2-connector.md` at `PROVINCE.md:26`.

## Findings

### F1 — Box 1's SHONEN evidence was stale at birth and round 47 did not refresh it

- `SHONEN.md:6` cites `.ufo/round-46/scouts/B2.md` (`:44`) with "38 Sources entries". B2 pins
  `SKILL.md` at `055d3b9` (sha `0404fdc0…`, 521 lines, 38 Sources — I reproduced all three).
- At the tip `SKILL.md` is sha `24df651b…`, 528 lines, **39** Sources bullets; the 39th appeared at
  `f2f9ee1` — the same commit that wrote the current `SHONEN.md`. So the count was already wrong
  when the box line was written, and the round-47 SKILL.md edit (description token, S012 sentence,
  opencode path) left it wrong.
- The structural counts still hold at the tip: 7 anatomy data rows (`SKILL.md:63-69`),
  5 decision rows (`:157-161`), 41 boxes 15/9/9/8 (`:179-253`, `:254-299`, `:300-330`, `:331-350`),
  39 Sources bullets (`:369-528`), and `verifiers/verify_skill_checklist.py --json` →
  `"41 boxes mapped (8 executed, 0 delegated, 33 unexecuted)"`.
- Round-47 did re-measure the box in wave 1 (`.ufo/waves/round-47/build/ShonenEvidence.md:14-17`)
  and noticed the 38-vs-39 counterexample (`:17`), but that finding never reached `SHONEN.md`:
  `git diff c61a973 7ad7fad -- SHONEN.md` is empty.

### F2 — The after battery is not in the landed tree

- `git ls-files .ufo/waves/round-47/after | wc -l` → `0`; `git status --porcelain .ufo/waves/round-47/after`
  → `?? .ufo/waves/round-47/after/`. The `before/` directory is tracked (9 files) and `build/` is
  tracked (200 files); `after/` is the odd one out.
- The after `SUMMARY.md` timestamp is 13:46:38, the landing commit 13:46:13 — the battery was run
  25 s after the commit landed and never committed.
- Consequence for box 2: the LOG entry's numbers are re-derivable by command (I re-ran every one
  below), but a fresh clone at 7ad7fad cannot read the after records; `.ufo/waves/round-47/after/SUMMARY.md:3-10`
  exists only in the fleet worktree.

### F3 — `check_assertion_floors.py` is load-marginal at its default 120 s timeout

- At default settings in the scratch clone under the falsify wave's load:
  `python3 -B verifiers/check_assertion_floors.py` → **exit 2**, `FAIL harness_independent self-test
  timed out after 120s (hung?)`, with the other 8 instruments PASS.
- The self-test itself is not broken: `python3 -B verifiers/verify_harness_independent.py --self-test`
  → exit 0 after 132 s with `0 failure(s) over 104 assertions`; with
  `--self-test-timeout 300` the guard → exit 0, 9/9 PASS, 118 s.
- The recorded landing run passed: `.ufo/waves/round-47/after/check_assertion_floors.out:1-9` is 9 PASS
  with `harness_independent observed=104 floor=104`. So this is a timeout margin under load, not a
  lost assertion; it still means "floors exit=0" is not reproducible at default settings while a
  falsify wave runs.
- A wave-1 reviewer already named the class (`.ufo/waves/round-47/build/RevScorecardRows.md:170`,
  "IND self-test hang under wave load"), but neither `LOG.md:2326` ("Not claimed") nor the
  `SCORECARD.md:104` debt list carries it. The guard's own docstring treats a timeout as a named
  failure (`verifiers/check_assertion_floors.py:33`, message at `:505`).

### F4 — Box 3 has no round-47 cold run, only a crash-handoff proxy

- `LOG.md:2319` says the first coordinator died with the host session and the replacement
  (`KotobaR47-2`) integrated the surviving wave-1 output. That is a genuine written-context handoff,
  but it tests plans and wave reports, not `SKILL.md`'s instructions.
- `grep -rln 'cold run\|cold-run\|cold start\|cold-start' .ufo/waves/round-47/build/*.md` → `ShonenEvidence.md` and `RevPriorRoundReport.md`; the latter only checks that the round-8 cold-run file path resolves (`:485`), it reports no run. The wave-1 seat itself records "no fresh non-author re-run is planned" (`.ufo/waves/round-47/build/ShonenEvidence.md:34`).
- `corpus/lessons/round-47.md` has only `## Mistakes` and `## Gate` (no `## Spot-check`), and
  `SHONEN.md:10`'s "no fresh non-author re-run since" is still true at the tip. A wave-1 reviewer
  stated the same condition for the round's gate decisions at
  `.ufo/waves/round-47/build/RevPriorRoundReport.md:86-90`. The round-8 file's own `:44` records
  that a lane-dispatched reviewer counts as the lane, so even the historical "non-author" credit is
  bounded.

### F5 — Box 4's PROVINCE half is accurate; the bleed half is a round old

- Re-verified at the tip: all 21 backticked `*.md|*.py|*.json|*.sh` paths in `PROVINCE.md` exist;
  `PROVINCE.md:21`'s "33 of 41 boxes" matches the live check detail's count (8 executed + 0
  delegated + 33 unexecuted); `PROVINCE.md:22`'s "surfaces 7/7, pins 3/3 at default resolution" reproduces
  (`verify_surfaces.py --json` exit 0, 7/7, 42 ids; `check_substrate_pins.py` exit 0, 3/3).
- No round-47 sibling-overlap scan exists: `PROVINCE.md:26` still cites
  `.ufo/round-46/scouts/w2-connector.md`, and the only round-47 reports that mention that file are
  `ShonenEvidence.md` and `RevPriorRoundReport.md` (both quoting it).
- The one round-47 change that touches a tameshi-adjacent surface is the 3-line planter fix in
  `verifiers/fault_injection_corpus.sh` (insert inside `## Coverage map`), a repair to this lane's
  own corpus harness, not an import of tameshi's method — no bleed observed. [INFERENCE] the
  tameshi boundary is unexercised, not violated.
- Nit: `PROVINCE.md:10` still reads "Appended round 46" while `:15` is a round-47 row added to the
  same section; descriptive, not a false claim.

### F6 — Round-47 claims that survived the re-run (a finding, not padding)

- C1: `verify_surfaces.py --json` exit 0, 7/7 PASS (42 loader-kind entries, 42 ids, OC-1..OC-6
  9/9 classes); `check_substrate_pins.py` exit 0, 3/3 (`omp fdbc8136…`, `opencode 179ca421…`).
- C2: `verify_skill_checklist.py --json` exit 0, 11 PASS / 0 FAIL, `trigger.no_xml_tag` PASS over
  `name` and `description` (`verifiers/verify_skill_checklist.py:1294-1312`); four fixture dirs
  `verifiers/fixtures/checklist/xml-tag-{codespan,split,dq-escape,control}` match the four cases
  claimed at `SKILL.md:151`; `--self-test` exit 0, `0 failure(s) over 1845 assertions`;
  frontmatter `<skills>` count 0.
- C3: `verify_corpus_integrity.py --json` exit 0 and `verify_corpus_independent.py --json` exit 0;
  the erratum registry at `verifiers/verify_skill_checklist.py:377-384` pins `LOG.md:2111`
  (sha256 `7dcbf123…`, token `.ufo/round-45/drafts/v10/post-r44-hunt.py`, absence wording,
  horizon 2315); `verifiers/corpus-baseline.json:13-16` expects `tracked_files` 60;
  `fault_injection_corpus.sh` exit 0, `verdict: ALL PASS`.
- Honest disclosure holds: `verify_harness_claims.py` exit 1, 21/28 — the same count the LOG
  discloses at `LOG.md:2326` (seven DRIFT ids, not named there); I re-ran it and got 21/28.

## Commands run (all in the scratch clone unless noted; `python3 -B`, `PYTHONDONTWRITEBYTECODE=1`)

| command | exit | key output |
|---|---|---|
| `git clone … && git checkout --detach 7ad7fad` | 0 | HEAD `7ad7fad…` |
| `python3 -B verifiers/verify_skill_checklist.py --json` | 0 | `pass 11, fail 0`; box map "41 boxes mapped (8 executed, 0 delegated, 33 unexecuted)" |
| `python3 -B verifiers/verify_skill_checklist.py --self-test` | 0 | `0 failure(s) over 1845 assertions` |
| `python3 -B verifiers/verify_surfaces.py --json` | 0 | `pass 7, fail 0`; 42 loader-kind entries / 42 ids |
| `python3 -B verifiers/check_substrate_pins.py` | 0 | `OK 3/3 pins hold` |
| `python3 -B verifiers/verify_corpus_integrity.py --json` | 0 | 0 DRIFT |
| `python3 -B verifiers/verify_corpus_independent.py --json` | 0 | 0 DRIFT |
| `bash verifiers/fault_injection_corpus.sh --repo "$PWD"` | 0 | `verdict: ALL PASS` |
| `python3 -B verifiers/verify_harness_claims.py` | 1 | `21/28 checks pass` (same seven DRIFT ids as `LOG.md:2326`) |
| `python3 -B verifiers/check_assertion_floors.py` | **2** | `FAIL harness_independent self-test timed out after 120s (hung?)`; other 8 PASS |
| `python3 -B verifiers/verify_harness_independent.py --self-test` | 0 | `0 failure(s) over 104 assertions` (132 s) |
| `python3 -B verifiers/check_assertion_floors.py --self-test-timeout 300` | 0 | 9/9 PASS (118 s) |
| `sed -n '/^---$/,/^---$/p' SKILL.md \| grep -c '<skills>'` | 1 | `0` |
| `git ls-files .ufo/waves/round-47/after \| wc -l` | 0 | `0`; `git status` → `?? .ufo/waves/round-47/after/` |
| `git show f2f9ee1:SHONEN.md \| sha256sum` | 0 | `f012cd2f…` == tip == BASE |

## Counterexamples (with repro)

1. **SHONEN.md:6 count is stale (38 vs 39).**
   ```
   awk '/^## Sources/{f=1;next} f&&/^- /{n++} END{print n}' SKILL.md          # 39
   git show 055d3b9:SKILL.md | awk '/^## Sources/{f=1;next} f&&/^- /{n++} END{print n}'  # 38
   git show f2f9ee1:SHONEN.md | sha256sum                                   # f012cd2f… == tip
   ```
   The 39th bullet was added at `f2f9ee1`, the commit that wrote the current SHONEN line.

2. **The after battery is untracked.**
   ```
   git ls-files .ufo/waves/round-47/after | wc -l          # 0
   git ls-files .ufo/waves/round-47/before | wc -l         # 9
   git status --porcelain .ufo/waves/round-47/after        # ?? .ufo/waves/round-47/after/
   ```

3. **Floors default exits 2 under wave load, but the floor is intact.**
   ```
   python3 -B verifiers/check_assertion_floors.py            # exit 2, harness_independent 120 s timeout
   python3 -B verifiers/verify_harness_independent.py --self-test   # exit 0, 104 assertions, 132 s
   python3 -B verifiers/check_assertion_floors.py --self-test-timeout 300  # exit 0, 9/9
   ```
   Recorded landing run: `.ufo/waves/round-47/after/check_assertion_floors.out` 9 PASS.

4. **Box 3 has no round-47 cold run.**
   ```
   grep -rln 'cold run\|cold-run\|cold start\|cold-start' .ufo/waves/round-47/build/*.md  # RevPriorRoundReport:485 only checks the path
   grep -n '^## ' corpus/lessons/round-47.md           # Mistakes, Gate — no Spot-check
   ```

## Not checked

- S012–S015 pages were not re-fetched (network); I verified the committed rows
  (`corpus/SOURCES.md:25-28`), the re-open note, and the claimed commands, not the live URLs.
- The round-13 landing commit behind `SHONEN.md:10`'s "both fixed in round 13" was not opened; I
  only verified the fixes in the current text (`SKILL.md:97`, `:503`).
- `fault_injection_corpus.sh --self-test` was not run (default harness only).
- The omp/opencode dumps were not re-read by hand; I relied on `verify_surfaces.py`/`check_substrate_pins.py`
  for the C1 byte claims.
- The seven `verify_harness_claims.py` DRIFT rows were not adjudicated (outside the box target); I
  only confirmed the disclosed 21/28.
- `SHONEN.md` history before `f2f9ee1`, other lanes' SHONEN conventions, and the fleet-root
  `PROTOCOL.md` beyond `:59-66` were not examined.
- The after battery's landing-time environment was not reconstructed; I compared its recorded
  outputs with my re-runs.

Tooling installed or updated: none (no pacman, uv, npx, cargo or npm runs).

Artifacts: `W2ShonenEvidence.checklist.json`, `W2ShonenEvidence.surfaces.json`,
`W2ShonenEvidence.floors-default.out`, `W2ShonenEvidence.floors-timeout300.out`,
`W2ShonenEvidence.ind-selftest.out`, `W2ShonenEvidence.harness-claims.out` (same directory).
