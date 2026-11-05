# ReviewerFloors — attack C2(b): re-derived rungs at base, repairs and coupling verified

Seat: ReviewerFloors (round-92 wave 1, kotoba lane). Candidate under attack:
`e073723ae667b64e534f8621bddb83ad12ad0e71` + `ExecLadderR92.patch`, committed in my scratch
clone as **`e034d438fe546e05a78b540b1868e4b0abdf44a0`** (scratch identity, inside the clone only).
All receipts: `.ufo/waves/round-92/w1/ReviewerFloors/`.

## Verdict

**C2(b) candidate holds.** All six attack legs (a)–(f) pass on independently re-derived evidence.
Patch touches exactly the four owned files. Findings below are plan-text/receipt-content level
(R1–R3) and informational (R4–R5); no production defect found, no counter rescued.

## Legs

- **(a) base re-derivation** — `base-rerun-probes.txt`: at base rev e073723, the three probes
  reproduce the committed receipts exactly: work → uncaught `NotADirectoryError` rc 1 (probe
  exit 0); dupnames → `freeze gate: 2 control(s) held` exit 0; exit127 →
  `COULD-NOT-EVALUATE control one27 (line 6): command not found (rc=127)` rc 2.
  Twin re-derived by me (`base-twin-work-is-file.txt`): `--work` naming an existing regular
  file → uncaught `FileExistsError`, gate rc 1.
- **(b) candidate rungs** — `candidate-rungs-rerun.txt` + `candidate-rungs.txt` (twin block):
  work under a regular file → `COULD-NOT-EVALUATE --work <root>: not a directory`, **rc 2**
  naming the work root, no traceback; twin (`--work` = existing regular file) → same line,
  **rc 2**; dupnames → `INVALID SPEC: duplicate control dup (line 9): already declared at
  line 7`, **rc 3** naming the duplicate; exit127 → `INVALID SPEC: control one27 (line 7):
  exit 127 is unobservable (126/127 are the harness's own could-not-evaluate codes; a declared
  127 can never be compared)`, **rc 3**. The probe wrappers exit 1 on the candidate by design
  (their pass-condition is the base defect); the gate readings above are the after-state.
- **(c) honest worlds** — `candidate-honest-worlds.txt`: `fp-minimal.md` → held, rc 0;
  `r88-controls-fixed.md` → `freeze gate: 4 control(s) held`, rc 0; `r88-controls.md` → rc 1
  `REFUSED control w_added_red` (see R1).
- **(d) self-test** — `candidate-freezegate-selftest.txt`: `0 failure(s) over 34 assertions`,
  rc 0; N' = 34 ≥ 34; the three new arms are named in the candidate bytes
  (`candidate-coupling.txt` lines 615–617: work-root, parse-duplicate, unobservable-rung).
- **(e) coupling** — `candidate-coupling.txt`: floors-registry.json `freeze_gate` floor = 34 ==
  `EXPECTED_INSTRUMENTS["freeze_gate"]` (check_assertion_floors.py:206) ==
  `INSTRUMENTS["freeze_gate"]` (line 292) == N' 34. `check_assertion_floors.py --self-test` →
  `0 failure(s) over 176 assertions`, rc 0 (`candidate-floors-selftest.txt`).
- **(f) tip battery** — `candidate-tipbattery.txt` at e034d438: `guards 5 of 5`;
  `tip battery exit 0: 3 of 6`, process rc 1 from exactly the three carried red corpus gates
  (verify_skill_checklist 1, verify_corpus_integrity 1, verify_corpus_independent 1; gate
  registry 0, assertion floors 0, correction sweep 0) — the same pattern as
  `base-tipbattery.txt`. Admission present and correct: INSTRUMENT_PINS appends
  `4ed35c4ea4925340f4752e7b02424f01b6026237` to check_assertion_floors.py's tuple and adds
  `verifiers/check_freeze_gate.py: (a6f18c27…, 856f543b…)`; both candidate blobs verified
  against rev bytes by `git rev-parse HEAD:<path>` (`candidate-pins-static.txt`). Stale-blob
  admission FAILS as required (`candidate-tipbattery-stalepin.txt`): pin mutated to the old
  blob only → `FAIL guard instrument-pin: verifiers/check_freeze_gate.py blob 856f543b… is not
  a pinned blob`, guards 4 of 5, rc 1. Pin restored after the mutation; `git status --porcelain`
  clean; candidate HEAD re-verified e034d438.

## Findings

- **R1 (Low, plan-text defect — honest-world fixture misnamed).** plans/round-92.md § C2(b)
  says the honest world "`verifiers/fixtures/freeze-gate/r88-controls.md` still exits 0".
  That file is the *unsatisfiable* world: its frozen round-89 predicate — and the candidate's
  own surviving self-test arms (`arm_predicate_unsat_exit1`, `arm_unsat_names_w_added_red`) —
  pin it at **exit 1 REFUSED naming `w_added_red`**, which is what the candidate reads. The
  honest world that stays green is `r88-controls-fixed.md` (rc 0, 4 controls held). The seat
  item's "(c) … r88-controls.md exit 0" inherits the slip and cannot be implemented literally
  without breaking (d). No code change made or needed; frozen plan text — addendum is the L1's
  call.
- **R2 (Low, frozen-receipt content gap).** Plan § C2(b) rung 1: the FileExistsError twin is
  "observed, `redbefore-ladder-work.txt` … the receipt records both readings". The committed
  receipt contains **zero** `FileExistsError` mentions (only the NotADirectoryError reading;
  `git show e073723:…redbefore-ladder-work.txt | grep -c FileExistsError` → 0). I re-derived
  the twin at base myself, so the repair target stands, but the committed red-before evidence
  does not carry the reading the plan attributes to it.
- **R3 (Low, frozen-receipt content gap + verdict-ladder consequence, documented).** Plan
  § C2(b) rung 2: the contradicting-duplicate shape is "ALREADY refused at base (observed,
  same receipt)" — `redbefore-ladder-dup.txt` is 4 lines recording only the both-passing shape;
  no contradicting reading is committed. Re-derived by me (`contra-dup-base-vs-candidate.txt`):
  first-fails duplicate world at base → `REFUSED control dup (line 3)` rc 1 (plan's claim is
  true of the bytes); at candidate → `INVALID SPEC: duplicate control dup (line 5): already
  declared at line 3` rc 3. The already-refused shape's verdict moves 1 → 3 under parse-time
  rejection; both fail-closed and the plan's stated target is parse-time acceptance, but the
  movement is unrecorded in any receipt.
- **R4 (Info, pre-existing).** check_assertion_floors.py INSTRUMENTS comment still says
  "…--self-test 30, the registry row's floor" beside the cell that read 31 at base and 34 at
  candidate — staleness predates this patch; ownership (two cells only) correctly leaves it.
- **R5 (Info, self-disclosed invalid reading, superseded).** The first block of my
  `candidate-rungs.txt` ("1 control(s) held", rc 0) is my own invalid invocation — I passed a
  non-existent path with no regular-file blocker, so makedirs legitimately created it; the
  corrected reading is `candidate-rungs-rerun.txt`. Builder's NOTE-probes.txt discloses the
  same class of mis-taken reading on their side, corrected in candidate-work-root.txt — the
  disclosure is honest and my independent runs confirm the corrected readings.

## Residual risk and verification gaps

- My candidate revision e034d438 is my scratch commit; the L1's landing rev will differ by
  commit metadata. The four changed-file blobs are what the pins and floors rows actually
  bind; both admitted blobs verified against rev bytes, and the stale-blob refusal was
  exercised.
- I did not run no-harm items outside this item (sibling census, province core, SKILL size,
  Q73 sweep, SOURCES census); within the item, the tip battery exercised the six gates with
  the base-identical carried-red pattern.
- floors self-test wall time differs by context (5.6 s in my working tree vs ~182 s inside
  the battery sandbox, matching the base receipt's 181.8 s); both readings rc 0 over 176 —
  timing not investigated (outside item scope).
- No tool installs were made; no pacman use; no git/jj writes anywhere except the sanctioned
  scratch clone (single commit e034d438, scratch identity); scratch removed after receipts
  were copied.
