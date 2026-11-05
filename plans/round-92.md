# Round 92 — kotoba (Linux host, omp 18.15.0) — plan

Author: KotobaR92 (L1, attempt 1). Round: 92. Base: lane tip at round start
`5031a78215778525a7c777116ad6f6b89acac817` (branch `master`, local == remote, `jj-lane.sh state`).
Freeze commit: **this commit** — the plan, the pre-data controls document and the pre-data
receipts under `.ufo/waves/round-92/receipts/` land together; every patch and measurement below is
`git diff --binary` from this freeze commit, and every landing measurement is taken at the landing
revision and named as such.

Claims are frozen here: predicate sentence, counting command, kill rule and target do not change
after any seat has scored (§9). An amendment is an L1 act via `plans/round-92-addendum-*.md`
BEFORE any scored reading.

## Inherited state resolved at freeze

- `.ufo/waves/round-91/r91-w1-results.json` — already tracked and landed before this round started:
  commit `931746a` "round-91: wave settlement (WAVE-DONE r91-w1, results file, ReviewerRepairs output
  unavailable), lesson and LOG corrections" (ancestor of the round-92 base; `git log --oneline -1 --
  .ufo/waves/round-91/r91-w1-results.json`). Round-91 spot-check routed defect 5 ("commit or remove")
  is resolved upstream; `jj-lane.sh commit` of the same path reads `nothing to commit`. Not round-92 work.
- No uncommitted tracked files; `git status --porcelain` clean except the paths this round creates.
- No `corpus/lessons/operator-*.md` exists (`ls corpus/lessons | grep operator` → empty at base).
- `corpus/lessons/round-91-verifier-spotcheck.md` read in full; its six routed defects are
  dispositioned: 1 → C1 this round; 2 → C2(a) this round; 3 → C2(b) this round; 4 → SOURCES
  correction row S265 this round; 5 → committed at freeze (above); 6 → carried reds named in the
  no-harm battery below.

## Claims (2 declared; causally separable; distinct axes)

### C1 — consistency (calibration sub-axis; score 10, held) — the two routed controls refuse their named shortcuts through the public path

Round-91 verifier spot-check routed defect 1 / round-91 lesson § Mistakes `vacuous` row /
`plans/round-91-addendum-1.md` A5. The round-91 pre-data controls do not refuse the shortcuts they
name: `ctl-c2-capline-only` reads only the working-tree cap and prints `C2-PREDICATE-MET`, exit 0,
on the cap-only shortcut world; `ctl-c1-manifest-only` appends kill rows to a clone's working tree
while passing the committed base rev to `--rev`, so G1 never reads them and its exit 1 holds for
the plain no-work reason.

**Red-before (measured at the round-92 base, receipts committed at freeze):**
- `bash verifiers/fixtures/round-91/ctl-c2-capline-only.sh` → `SELF_TEST_TIMEOUT_S=360`,
  `C2-PREDICATE-MET`, **exit 0** on the cap-only shortcut it names
  (`.ufo/waves/round-92/receipts/redbefore-ctl-c2.txt`).
- `bash verifiers/fixtures/round-91/ctl-c1-manifest-only.sh` → `C1-PREDICATE-UNMET`, **exit 1**,
  with the gate reading the committed base rev only: the appended working-tree rows are never
  evaluated (defect mechanism re-derived from committed round-91 bytes:
  `verifiers/fixtures/round-91/ctl-c1-manifest-only.sh:10-11` appends to `$S/...` then passes
  `git rev-parse HEAD` of the unmodified base checkout; A5 records G1 reads committed bytes)
  (`.ufo/waves/round-92/receipts/redbefore-ctl-c1.txt`).

**Landed change (one builder owns `verifiers/fixtures/round-92/`):**
- `ctl-c2-capline-only-v2.sh` — builds a committed cap-only shortcut world in scratch (cap ≥ 320,
  NO `INSTRUMENT_PINS` admission, no measured-duration constant), commits it there, and runs the
  public gates over those committed bytes: `check_tip_battery.py` (instrument-pin guard must FAIL
  naming the blob) and the cap conjunct. Prints `C2-SHORTCUT-REFUSED: instrument-pin admission
  missing (blob <sha> unpinned; guards G of 5)`, **exit 1**.
- `ctl-c2-honest.sh` — the honest world: at the landing rev the committed bytes carry cap ≥ 2×
  measured duration (Q39 headroom), the measured-duration constant, AND the `INSTRUMENT_PINS`
  admission; the public gates read PASS. Prints `C2-PREDICATE-MET`, **exit 0**.
- `ctl-c1-manifest-only-v2.sh` — builds the manifest-only shortcut world with the appended kill
  rows **committed** in the scratch clone (`git commit` there, scratch identity) and passes that
  committed rev to the battery, so G1 reads the rows. The battery cannot evaluate rows whose
  probes are absent: reads could-not-evaluate (exit 2) naming the rows. Prints
  `C1-SHORTCUT-REFUSED: rows committed and read; instrument cannot evaluate (rc 2)`, **exit 1**.
- `ctl-c1-honest.sh` — runs the battery predicate at the landing rev; `killed 17 of 17 kill-set`,
  exit 0 → prints `C1-PREDICATE-MET`, **exit 0**.
- `controls-run.sh` — the frozen counting command: runs the four scripts, prints exactly
  `round-92 controls: shortcuts refused 2 of 2; honest held 2 of 2`, **exit 0** iff both refused
  worlds exit 1 naming their conjunct and both honest worlds exit 0. Any other combination prints
  the observed line and exits 1.

**Predicate (frozen):** at the landing revision, `bash verifiers/fixtures/round-92/controls-run.sh`
exits 0 with that exact line; each refused world's stdout names its missing conjunct; the
red-before receipts above are committed at the freeze commit. Kill rule: no control, counter,
manifest or PROBES byte is amended after any scored reading.

**Do-nothing control (§9, executed before data):** the old round-91 control pair scored on the new
counter's vocabulary refuses `0 of 2` named shortcuts (cap-only reads MET exit 0; manifest-only is
unmet without its rows being read) — receipt
`.ufo/waves/round-92/receipts/nowork-c1-controls.txt`. A no-work round reaches 0 of 2; the target
2 of 2 is unreachable without the redesign.

### C2 — depth (score 9, held) — the dropped-row bound and the three same-class ladder rungs become fail-closed

Round-91 spot-check routed defects 2 and 3; round-91 lesson § Settlement (MutTesterBattery m6: a
dropped kill row keeps the self-test green and only the printed count changes); A3's routed
same-class ladder findings (F1 duplicate control names read held; F2 declared `exit 127` never
compared; F4 `--work` under a regular file → uncaught `NotADirectoryError`).

**(a) kill-set size pin** (builder owns `verifiers/check_mutation_battery.py`):
`--self-test` gains a named arm that pins the kill-set size — the number of `kill` rows the
battery evaluates from the measured revision's committed manifest must equal a pinned constant
derived from those same bytes at load; a manifest whose kill-row count differs fails the self-test
naming the arm (`FAIL arm kill-set-size …`), not only a changed printed count.
**Before (red, base, receipt `.ufo/waves/round-92/receipts/redbefore-m6-dropped-row.txt`):** a
scratch clone with one `kill` row removed from `verifiers/fixtures/mutation-battery/manifest.tsv`
(17 → 16) still prints `0 failure(s) over 25 assertions`, exit 0 (the m6 class, re-run at the
round-92 base bytes). **After:** the same world on the candidate bytes exits 1 naming
`kill-set-size` (17 pinned vs 16 observed); the honest self-test prints
`0 failure(s) over N`, N ≥ 26, exit 0.

**(b) three fail-closed rungs** (builder owns `verifiers/check_freeze_gate.py`; the worlds below
are the round-91 re-derived instances — `ExecLadder/ladder-defect.md` F1/F2/F4 — re-observed at
the round-92 base bytes, receipts `.ufo/waves/round-92/receipts/redbefore-ladder-*.txt`):
1. `--work` under a regular file (`<work>/<regular-file>/sub`) → **could-not-evaluate (exit 2)**
   naming the unusable work root (`--work <path>: not a directory`), no traceback (base: uncaught
   `NotADirectoryError`, exit 1 traceback). The sibling uncaught path at these bytes — `--work`
   naming an existing regular file directly — raises `FileExistsError` uncaught (observed,
   `redbefore-ladder-work.txt`); the same fix must cover both uncaught paths, and the receipt
   records both readings.
2. two `control <same-name>` entries, both passing → **invalid spec (exit 3)** naming the
   duplicate (base: `freeze gate: 2 control(s) held`, exit 0 — duplicate names are accepted as
   valid spec). The contradicting-duplicate shape (first declaration fails) is ALREADY refused at
   base (observed, same receipt) — the repair's target is parse-time acceptance, not comparison.
3. a control declaring `exit 127` → **invalid spec (exit 3)** naming the unobservable rung
   (`126/127 are the harness's own could-not-evaluate codes; a declared 127 can never be
   compared`) (base: `COULD-NOT-EVALUATE … rc=127`, exit 2 — the declared 127 never compared).
Self-test gains one named arm per rung: `0 failure(s) over N'`, N' ≥ 34, exit 0; the
`freeze_gate` floor moves 31 → N' in `verifiers/floors-registry.json` and in the two in-file
tables of `verifiers/check_assertion_floors.py` (`EXPECTED_INSTRUMENTS`, `INSTRUMENTS` — the A1
coupling), and `verifiers/check_tip_battery.py` `INSTRUMENT_PINS` gains the admission for every
floors-registry-listed instrument blob the patch changes (the round-91 `landing` mistake class —
this time named in the plan's touch list before data). The honest worlds stay green on the
candidate: `fp-minimal.md` reads held, and `verifiers/fixtures/freeze-gate/r88-controls.md` still
exits 0.

**Predicate (frozen):** (a) and (b) above, each with its red-before receipt committed at the
freeze commit and its after-reading taken at the landing revision. Kill rule: no control, counter,
manifest or PROBES byte is amended after any scored reading.

**Do-nothing control (§9):** the three rung probes at base bytes and the dropped-row self-test at
base bytes produce zero named findings and zero new arms (receipts above); a no-work round cannot
produce N ≥ 26 or N' ≥ 34, nor a refused world.

**Sourced claim:** C2 cites the row opened this round for the environment exception class:
S266 (Python exception reference, `NotADirectoryError`), recorded in `corpus/SOURCES.md` with URL,
access date and located quote; the `--work` rung's finding names the exception the environment
raises and why the gate must translate it to its own could-not-evaluate rung. C1's calibration
conjunct cites the S265 correction row (supersedes S263 — the anchor repair; the `run(timeout=)`
kill-and-wait contract the cap calibration rests on). Gate records for both rows are in
`corpus/lessons/round-92.md` § Gate.

## Axis and score discipline

- C1 is a consistency (calibration sub-axis) move: verdict verdicts of controls now match what
  they name (claim-scope coherence). C2 is a depth move (the lane's lowest owned non-retired axis,
  9) — both obligations met with these two claims; no third claim is declared (the planned
  intentions item (3) is folded into C2(b) — same axis, one claim).
- Scores are **held** (10 / 9); the SCORECARD rows carry the measured deltas as annotations, and
  the non-author closure rules the axis verdicts.
- No-harm (Q65/Q72): the battery below is run at the freeze base (before data) and re-run at the
  landing post-state; what is red at base is named red and may not silently change.

## No-harm battery (commands and base readings — receipts committed at freeze)

| check | command | base reading (expected) |
|---|---|---|
| battery self-test | `python3 -B verifiers/check_mutation_battery.py --self-test` | `0 failure(s) over 25 assertions`, rc 0 |
| floors self-test | `python3 -B verifiers/check_assertion_floors.py --self-test` | `0 failure(s) over 176 assertions`, rc 0 (≈161 s; the r91 landing count) |
| freeze-gate self-test | `python3 -B verifiers/check_freeze_gate.py --self-test` | `0 failure(s) over 31 assertions`, rc 0 |
| gate registry | `python3 -B verifiers/check_gate_registry.py --rev <base>` | `74 of 74 … phantom 0`, rc 0 |
| tip battery | `python3 -B verifiers/check_tip_battery.py --rev <base>` | guards 5 of 5; rc 1 from the three carried red corpus gates (named red at base) |
| corpus integrity (working tree, pre-freeze) | `python3 -B verifiers/verify_corpus_integrity.py` | rc 1 — `4/9 checks pass`; DRIFT named: corpus.index.tracked_files, corpus.index.unindexed, corpus.pointers.report_total, corpus.pointers.commit_total, corpus.pointers.commit_unresolvable (carried; committed-rev reading re-taken at landing) |
| sibling census (carried red) | `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md` | `province rows 20 matched 4`, rc 1 (carried red, unchanged; the round-74 census reads matched 20 rc 0 — the L0 round-87 territory) |
| province core | `python3 -B verifiers/check_province_core.py --rev <base>` | `province core rows 0 of 2`, rc 1 (carried red, stale base pin) |
| SKILL.md size (Q78) | `wc -l SKILL.md; wc -c SKILL.md` | 600 lines / 92 672 B — **at the ceiling; no seat edits SKILL.md** |
| checklist (carried red) | `python3 -B verifiers/verify_skill_checklist.py` | rc 1 — `governance.citation_resolves` FAIL (carried); `trigger.citation_resolves` PASS 260/260 |
| Q73 sweep | `grep -rn 'check_freeze_gate\|check_mutation_battery' verifiers/*.py \| grep -v fixtures/` | 12 hits: the floors registry rows (check_assertion_floors.py:15,290,292), check_freeze_gate self-references (:2,:13,:350), the battery's FG/BAT constants and G3 fixture text — no historical byte-pin counter outside the touch list (receipt `q73-sweep-raw.txt`) |
| census | `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` | 190 — `190 — grep -cE … @ 5031a782` (receipt `census-before.txt`, validate rc 0, 33 W04 warnings carried) |

Landing no-harm conjuncts: battery self-test rc 0 with N ≥ 26; floors self-test rc 0; freeze-gate
self-test rc 0; gate registry rc 0 (unchanged 74 — controls are freeze-gate-executed fixtures, not
new gate rows); tip battery `guards 5 of 5` plus the new admissions (rc 1 only from the same three
carried red corpus gates); corpus integrity rc 0 (no new DRIFT beyond the carried three-files
growth the gate counts by design); sibling census and province core carried red, byte-unchanged;
SKILL.md 600 lines (untouched); census 192 after the two appended rows, `sources-census.sh
validate --root /home/vgpnk/Projects/shokunin kotoba` exit 0.

## Touch list (file ownership; one writer per production file)

- `verifiers/fixtures/round-92/*` (new) — ExecCtlWorlds (C1).
- `verifiers/check_mutation_battery.py` — ExecKillPin (C2a).
- `verifiers/check_freeze_gate.py` — ExecLadderR92 (C2b).
- `verifiers/floors-registry.json` (`freeze_gate` floor only), `verifiers/check_assertion_floors.py`
  (the two in-file `freeze_gate` floor cells only), `verifiers/check_tip_battery.py`
  (`INSTRUMENT_PINS` appends only) — ExecLadderR92 (C2b coupling).
- `corpus/SOURCES.md` (append S265, S266), `corpus/lessons/round-92.md` (new), `corpus/README.md`
  (index rows for the new corpus files only), `corpus/QUALITY.md` (append one criterion row) —
  ScribeCorpusR92 drafts; L1 lands at integration.
- L1-only at integration: SCORECARD.md, LOG.md, PROVINCE.md § Core (append-only note if needed),
  plans/round-92-addendum-*.md if needed. **SKILL.md: no edits any seat or the L1 (600/600).**
- No seat or the L1 edits any `corpus/lessons/round-*-verifier-spotcheck.md` (tip battery
  spotcheck-identity guard), any frozen instrument outside the touch list
  (`check_r86_routed_repairs_v3.py`, `verify_corpus_integrity.py`, `corpus-baseline.json`,
  `check_gate_registry.py`, `verify_skill_checklist.py`, …), or `corpus/Frozen` bytes of round-91
  controls (`verifiers/fixtures/round-91/` stays byte-identical — the red-before evidence).

## Frozen-instrument risk named before data

Editing `check_freeze_gate.py` and `check_mutation_battery.py` changes blobs that other gates pin
or registry-count. The A1 coupling covers `freeze_gate` floors (registry + two in-file tables) and
the `INSTRUMENT_PINS` admission covers the tip battery's pin guard. Q73 sweep result: no historical
counter pins `check_freeze_gate.py` or `check_mutation_battery.py` byte-identical
(`grep -rn 'check_freeze_gate\|check_mutation_battery' verifiers/*.py | grep -v 'fixtures/'` shows
only the floors registry tables and the tip battery pins — receipts
`q73-sweep.txt`). If a scored reading finds a pinned section, the claim stops and the amendment
goes through an addendum before any further reading.

## Frontier step (§ 2b; inside the claim cap, not a claim)

- Census before: 190 — `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` @
  `5031a782` (receipt `.ufo/waves/round-92/receipts/census-before.txt`; validate rc 0). Census
  after (expected): 192 (S265 supersedes-S263 correction row + S266 new row; both appended, no row
  dropped; correction rows are rows by the census's own counting command — the A2 arithmetic is
  applied before the freeze this time). Validate at landing must exit 0.
- Mistake mining: the round-91 `vacuous` control class is mined into `corpus/lessons/round-92.md`
  § Mistakes (class · evidence · captured-by Q37's gap · fix = C1) and its prevention enters
  `corpus/QUALITY.md` as an appended criterion row citing that lesson (drafted by the scribe,
  landed by the L1). Any further mistake surfaced by the wave gets its row.
- Sourced claims: C2 → S266; C1 → S265 (both opened this round; Gate records carry URL, access
  date, ≤25-word located quotes).
- Assimilation: none — the shokuknow package stays unadopted (open L0 `kotoba | round-88`, 55-id
  collision standing; no claim depends on it). considerthese/2026-10-26.md read again this round;
  no proposal implemented (proposal 3 still blocked by the 600/600 SKILL.md ceiling; 1, 4, 5
  carried/mined as recorded in rounds 88–91).
- Wave: ONE v1 wave, band 8–16, 12 seats (executor 3, scout 1, scribe 1, connector 1, reviewer 2,
  critic 1, mutation-tester 2, sentinel 1 — attack share 5 of 12 ≈ 42 % ≥ 25 %; connectors 1 ≤ 2;
  the §3 L2 floor (≥ 8) is met inside the wave; the L1 holds the §3 planner seat — the validator
  rejects `planner` as a swarm role). Round total: 12 seats, no residual call planned.

## Round-shape discipline

- Pre-data controls and red-before receipts are executed and committed at the freeze commit
  BEFORE the wave dispatches (plans/round-92-controls.md is the executable control document).
- Seats never commit; the L1 integrates patches into the lane and lands every commit through
  `/home/vgpnk/Projects/shokunin/scripts/hyaku/jj-lane.sh commit … --as kotoba`.
- The report lands last, cites the pushed lane hash, carries the `## SHONEN` heading with one line
  per SHONEN.md box, and is committed via `fleet-commit.sh --as kotoba` only.
- Q80: the round lesson names the five attack seats; a wave without an attack seat closes
  provisional — not applicable here (five are named above).
