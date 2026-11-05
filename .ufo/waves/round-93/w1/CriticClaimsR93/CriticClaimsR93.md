# CriticClaimsR93 — round-93 falsification report (wave r93-w1)

Seat: CriticClaimsR93 (critic, leaf — no subagents). Date: 2026-11-05.
Candidate measured: `a857c254e3eb270b44a75a3ab76e1ccb2696ab71` = freeze
`6d7eee0570912d9f3b9d3e3d0137f3c755451233` + the four builder patches, applied in a scratch
clone (`--shared` clone of the lane, committed with identity `scratch <scratch@invalid>`;
`git rev-parse --show-toplevel` asserted equal to the clone before the commit). Patch sha256s
verified against each READY before apply: ExecKillPinRev `c88bd6aa…`, ExecPinCoverage
`b14049dd…`, ExecReceiptRevs `e172509b…`, ScribeCorpusR93 `8057d6dc…`. At the candidate the
working tree changed exactly the six owned files (`corpus/README.md`, `corpus/SOURCES.md`,
`verifiers/check_mutation_battery.py`, `verifiers/check_tip_battery.py`, new
`verifiers/fixtures/round-93/check-receipt-revs.sh`, new `corpus/lessons/round-93.md`).
Scratch was deleted after the run; the candidate is rebuildable from the four w1 patches.
No lane file outside `.ufo/waves/round-93/w1/CriticClaimsR93/` was written by this seat.

## 1. Frozen counters on the candidate — both MET

**C1 — `bash verifiers/fixtures/round-93/c1-killpin-rev.sh a857c25… "$D"` → `C1-PREDICATE-MET`, exit 0.**
- drop world `a19e71e7962f05767b3e069172ebd4fd2461d379` rc 2 names kill-set-size **yes**:
  `could-not-evaluate: arm kill-set-size: manifest at a19e71e7962f has observed 16 kill rows, pinned 17`
- other world `27c34509e897f4d551b7e599e6c0ffaed1e5f541` rc 2 names kill-set-size **no**:
  `could-not-evaluate: baseline fg-self-test exit 1, declared 0: the revision does not hold the frozen baseline`
- honest world rc 0 names **no**: `mutation battery killed 17 of 17 kill-set; equivalents survived 6 of 6; disclosed survivors 0 of 0`

**C2 — `bash verifiers/fixtures/round-93/c2-pinkey.sh a857c25… "$D"` → `C2-PREDICATE-MET`, exit 0.**
- honest: `guard instrument-pin PASS`; last line `… guards 5 of 5; tip battery exit 0: 3 of 6`
  (tip rc 1 is the plan-disclosed carried corpus reds; this honest world is simultaneously the
  no-harm tip-battery reading at the candidate)
- keydrop: `FAIL guard instrument-pin: verifiers/check_correction_sweep.py has no INSTRUMENT_PINS key (battery instrument unpinned)`; tally `guards 4 of 5`
- keyswap: junk-key blob FAIL (`verifiers/r93-junk-key.py blob absent … is not a pinned blob`)
  **plus** the missing-key FAIL naming `verifiers/check_correction_sweep.py`; tally `guards 4 of 5`

## 2. Do-nothing and forgery controls — red confirmed, forgeries refused

- Do-nothing re-run (one, as assigned): `c1-killpin-rev.sh 6d7eee0570912d9f3b9d3e3d0137f3c755451233`
  (default REPO = lane) → drop world rc 2 names **no**
  (`could-not-evaluate: baseline bat-self-test exit 1, declared 0…`), `C1-PREDICATE-UNMET`, exit 1 —
  line-for-line consistent with `receipts/redbefore-c1-base.txt` (modulo world revs).
  `redbefore-c2-base.txt` read: at base, keydrop reads `guard instrument-pin PASS` / `guards 5 of 5`
  → `C2-PREDICATE-UNMET`. The red is real before both builds.
- Forgery controls: `forgery-c1-run.txt` ends `C1-PREDICATE-UNMET` via the **other** world (the
  blanket `arm kill-set-size:` prefix makes drop AND other both name the arm; the other conjunct
  "does NOT name" fails). `forgery-c2-run.txt` ends `C2-PREDICATE-UNMET` via the **keyswap** world
  (the count-based checker names the junk key, not `check_correction_sweep.py`). Patch shapes
  confirmed by direct read: `forgery-c1.patch` prefixes every could-not-evaluate line with
  `arm kill-set-size:`; `forgery-c2.patch` adds `if INSTRUMENT_PINS and len(INSTRUMENT_PINS) < 7`
  with a hardcoded finding naming `verifiers/check_correction_sweep.py`.

## 3. Clause audit (Q26) — no clause unchecked; residuals named

- C1 checks exactly the frozen conjuncts. Residual R2: the other-world conjunct reads only
  (rc 2 ∧ not-named) and cannot attribute cause — an unrelated rc-2-not-naming failure would also
  satisfy it. This run the cause is the intended one, grounded directly: emptying
  `verifiers/fixtures/freeze-gate/r88-controls-fixed.md` makes `check_freeze_gate.py --self-test`
  exit 1 (`INVALID SPEC: no ## Controls block found`; restored → exit 0), and the observed refusal
  line matches the pre-data receipt's other-world line at base.
- Order observation (not triggerable by the frozen edit, recorded): the named kill-set refusal
  fires after the targets-set guard in `evaluate()`; it fires here because the first kill row
  (`fg-m1-expect-exit-sign-flip` → `check_freeze_gate.py`) shares its target with 7 further kill
  rows. A manifest whose first kill row were the last row of its target would refuse on
  `manifest must name exactly the targets` (names-no) and C1 would flip UNMET — a fail-closed miss,
  consistent with the kill rule ("a miss is an honest stop").
- Naming is a grep over the whole battery output; the honest success line (`…kill-set;`) does not
  contain `kill-set-size`, confirmed by the honest conjunct reading "no".
- C2: the named FAIL line is itself an instrument-pin failure, so the `guards 4 of 5` attribution
  holds; in keyswap two instrument-pin failures occur but the guard tallies once — consistent.
  Disclosed scope confirmed in code: the new coverage loop iterates `BATTERY` scripts only;
  `check_freeze_gate.py` (unpinned by design) is not flagged; the guard count stays 5.

## 4. No-harm at the candidate — all green

- `check_gate_registry.py --rev a857c25…`: `gate registry rows conformant 74 of 74 lane verifiers; phantom 0`, rc 0.
- `verifiers/fixtures/round-92/controls-run.sh`: `round-92 controls: shortcuts refused 2 of 2; honest held 2 of 2`, rc 0.
- `check_mutation_battery.py --self-test`: `0 failure(s) over 31 assertions` (base 28 + the 3 new rev-path arms).
- `check_tip_battery.py --self-test`: `self-test: 0 failure(s) over 80 assertions`.
- `check_assertion_floors.py --self-test`: `0 failure(s) over 176 assertions`.
- `sources-census.sh validate --file <candidate>/corpus/SOURCES.md --today 2026-11-05`: rc 0; the
  W04 set is identical to `receipts/census-before.txt` (33 W04 rows + `ok`).
- SOURCES rows 192 → 194 (`S267`, `S268` appended; append-only respected; `corpus/README.md`
  gained exactly one index row for the new lesson).
- SKILL.md byte-identical freeze→candidate: sha256 `fc0feaa3…` both, 600/600 lines.

## 5. Mined-mistake check (`verifiers/fixtures/round-93/check-receipt-revs.sh`)

- **Fails on the round-92 landing receipts as required**: exit 1,
  `receipt revisions: 1 resolved, 4 unresolved over 18 files`, all four UNRESOLVED
  `cd355c4796fa165ff2b7d822401b4027da29e4d0` (`landing-rev.txt:1`, `tip-battery.txt:1`,
  `controls-run.stderr:23`, `controls-run.stderr:52`). Grounded:
  `git -C <lane> cat-file -e cd355c…^{commit}` → `fatal: Not a valid object name …`, exit 128 —
  the round-92 landing rev never existed in the lane. The mined mistake is real and caught.
- Passes on `.ufo/waves/round-93/receipts`: exit 0, `2 resolved, 0 unresolved, 2 scratch-declared`.
- **Defect D1 (medium, false-green, demonstrated twice):** the scratch exemption is a line-local
  substring (`world rev|scratch|forgery`, case-insensitive). (a) Live: round-92
  `bat-rev.txt:24` declares the same unresolved `cd355c4796fa` in a G1 line but escapes the check
  because the line contains `scratch clone detached at rev and clean`. (b) Synthetic: a bogus
  40-hex `REV=… (see scratch copy)` line beside a valid line is skipped and the file exits 0.
  A lane landing receipt whose only rev-bearing line mentions "scratch" is never resolved-checked.
  Smallest safe correction (builder-owned, ExecReceiptRevs): exempt a line only when "scratch"
  occurs inside a path-shaped token (e.g. matches `(^|[\s=:/(])(fast/)?scratch/`), not anywhere.
- **Defect D2 (low, false-green, demonstrated):** a header declaration corrupted by one extra hex
  char (41 hex) matches no `40-hex followed by non-hex` window and is silently dropped; beside a
  valid line the file exits 0. Fail-closed alternative: count header-shaped lines
  (`REV=`/`measured rev `/`rev` prefix) whose hash extraction failed and print them UNRESOLVED.
- **Defect D3 (low):** declarations are `^`-anchored; an indented `  rev <40hex>` is ignored
  (alone → exit 2 no-candidates; mixed with valid lines → silently skipped).
- Fail-closed directions confirmed: a bogus 12-hex G1 prefix → `UNRESOLVED` exit 1; a companion
  bogus 40-hex token on a header line → `UNRESOLVED` exit 1 (every token is counted).
- Residual R1 (inherent, disclosed): a 12-hex prefix that uniquely resolves to an unintended
  commit is undetectable; ambiguous prefixes fail closed via `rev-parse --verify`.

## 6. Verdict

C1-PREDICATE-MET and C2-PREDICATE-MET at `a857c254e3eb270b44a75a3ab76e1ccb2696ab71`, both with
their frozen world structure, controls, no-harm battery and mined-mistake check intact. No frozen
bytes were modified by this seat; no counter predicate was rescued or narrowed. Defects D1–D3 are
`check-receipt-revs.sh` quality findings for its owner (ExecReceiptRevs); none breaks the frozen
claim as scored, and D1's live instance still nets exit 1 on the round-92 dir because other lines
carry the same rev.

## Files written by this seat

- `.ufo/waves/round-93/w1/CriticClaimsR93/CriticClaimsR93.md` (this report)
- `.ufo/waves/round-93/w1/CriticClaimsR93/c1-candidate.txt`
- `.ufo/waves/round-93/w1/CriticClaimsR93/c2-candidate.txt`
- `.ufo/waves/round-93/w1/CriticClaimsR93/c1-redbefore-freeze-rerun.txt`
- `.ufo/waves/round-93/w1/CriticClaimsR93/noharm-battery.txt`
- `.ufo/waves/round-93/w1/CriticClaimsR93/receipt-revs-probes.txt`
- `.ufo/waves/round-93/w1/CriticClaimsR93/fg-selftest-cause.txt`

## Installations

None. No packages installed or upgraded; pacman untouched.
