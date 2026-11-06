# CriticClaimR96 — falsification of C1 against the full candidate

Seat: CriticClaimR96 (critic, r96-w1). Scope: attack the frozen claim C1 on the candidate
`679775abb9277a7b8d17f060b0f5b4ced2b127b6` + `ExecArmsR96.patch` + `ScribeCorpusR96.patch`.
No lane writes; scratch clone only. Candidate built in
`/fast/scratch/hyaku/kotoba-r96/CriticClaimR96/repo` as `509bc6c95bd5ad24521c3409801f653f06198113`
(identity `scratch <scratch@invalid>`, `rev-parse --show-toplevel` asserted = the clone; both patches
`git apply`-clean at the freeze commit).

## Verdict

**C1-PREDICATE-MET at the candidate.** The eleven frozen targets are real false greens/reds of the
dispatch.04/.08 conjuncts, the landed arms are behavioural, the controls reproduce, the axis is
depth (lowest owned), and the sources ground the mutant classes. Four defects are recorded; none
changes the predicate. **D1 and D4 need an L1 addendum to the plan's prose** (not to the predicate,
target, counter or builder).

## Axes under test — readings

| axis | reading | evidence (receipt under `w1/CriticClaimR96/`) |
|---|---|---|
| 1 candidate c1 | **MET** — `killed 11 of 11 (run errors 0); positive 1 of 1; honest CLEAN; comment decoys 11 of 11; code decoys 11 of 11`, rc 0 | `candidate-c1.txt` (6.5 s) |
| 2 candidate r95c1 | **MET** — `3 of 3; positive 1 of 1; honest CLEAN; decoys 3 of 3`, rc 0 | `candidate-r95c1.txt` (81 s) |
| 3 base do-nothing | **reproduced** — `0 of 11`, `C1-PREDICATE-UNMET`, rc 1 | `c1 0f66016a $D` 5.3 s |
| 4 forgery worlds f1–f5 | **all five reproduce the pre-data receipts** | `forgeries-built.txt`, `forgery-rerun.txt` |
| 5 targets real | **all 11 confirmed** as wrong verdicts on crafted fixtures | `probe-targets.txt` |
| 6 axis naming | **depth, correct** — depth 9 < consistency 10; surface named is the instrument's `--self-test` | SCORECARD axes table; plan § C1 |
| 7 sources | **grounded** — independent fetch, both digests match, quotes located | `source-digests.txt` |
| 8 mined-mistake control | **reproduced** — pre-fix builder reads `C1-NOT-EVALUATED: code decoy t05 … does not compile`, rc 2 | `prefix-decoy-control.txt` |
| 9 lesson Gate / dispositions | **Gate real** (2 rejects with flip conditions, Ant amendment); dispositions honest except D4 | `corpus/lessons/round-96.md`; plan § Inherited state |
| 10 cheaper change | **no cheaper/do-nothing path found** | f1–f5 reproduce; no do-nothing MET; arms behavioural |

### 4 — forgery worlds (my rebuild vs the committed receipt)

| world | my reading | receipt | match |
|---|---|---|---|
| f1-text-sniff | `0 of 11; comment 0/11; code 0/11; UNMET` | same | ✓ |
| f2-crash-signal | `0 of 11; run errors 1; UNMET` | same | ✓ |
| f3-summary-no-line | `0 of 11; run errors 1; UNMET` | same | ✓ |
| f4-honest-trip | `11 of 11; honest REPORTED-FAILURE; decoys 0/11; UNMET` | same | ✓ |
| f5-label-only | `0 of 11; UNMET` | same | ✓ |

### 5 — the eleven targets are real (base instrument, crafted fixtures)

`t01` both `${LANE}` and `$LANE` read PASS (honest FAIL); `t02` bare `$LANE` PASS; `t03` `${LANE}`
PASS; `t04` round 7 vs baseline 7 reads FAIL (honest PASS — a false red of the inclusive bound);
`t05` an all-N/A dispatch.08 reads box PASS (honest N/A); `t06` a round token only on a later line
reads PASS (honest FAIL); `t07` round-6 beside round-7 reads PASS (honest FAIL); `t08` a placeholder
in the second path reads PASS (honest FAIL); `t09` a second stem `other` reads PASS (honest FAIL);
`t10` baseline `abc` reads PASS (honest N/A); `t11` no report path reads all-PASS (honest all-N/A).
Every one is a wrong verdict on a case the box text names — none contrived. The landed arms kill
exactly these behaviours: my on-disk arm map (`armmap.txt`) shows failure counts
2,1,1,2,3,2,1,1,1,3,5 — identical to the source-blind counter's — and every failure line names the
arm's target (`t01/t02`, `t01/t03`, `t04`, `t05`, `t06`, `t07`, `t08`, `t09`, `t10`, `t11`).

### 8 — mined mistake `decoy-builder-cuts-elif-chain`

Removing v4 rule 2 (the `elif` climb) from a scratch copy of the counter and running `c1` at the
base reproduces the committed control byte for byte:
`C1-NOT-EVALUATED: code decoy t05-finish-allna-pass does not compile: invalid syntax
(verify_dispatch_prompts.py, line 499)`, rc 2. The fix is therefore shown able to fail, and the
fixed builder holds `t05`/`t07` decoys at base while still tripping f1's sniffer (code decoys 0/11).

### 9 — lesson Gate and round-95 dispositions

- Gate: S271 (PIT Mutation operators, 16-word quote at HTML 317-319, `<=` → `<` row at 334-335) and
  S272 (POSIX XCU 2.6.2, 22-word quote at HTML 790-791) admitted with URL/date/HTTP/bytes/sha256/
  quote; **two same-round rejects** (mutmut — observed that only `<`→`<=` is stated, flip condition
  named; gnu.org — host timeout, flip condition named); the round-95 Ant reject reason is amended
  append-only with the `haltonerror`/`errorproperty`/`haltonfailure` facts and the narrower ground
  ("no definition of an error"). `corpus/lessons/round-95.md` is not edited. I re-fetched the Ant
  page (HTTP 200, 33365 B, sha256 `3f1ee369…c4a1`) and the three attribute lines match.
- Census on the candidate: `sources-census.sh validate --file` rc 0, **34 W04** (same as base),
  rows 196 → 198; both new rows NF=13, no `|` inside a cell.
- Round-95 routed defects 1/2/3/5/6 are dispositioned as the plan says (1 landed in the lesson,
  2 shipped as f3/f4 committed controls, 3 and 5 carried, 6 orchestrator-side). **Defect 4's
  exit-ladder sub-item is not dispositioned — see D4.**

## Candidate scope / identity proofs (my own, not the builder's receipt)

- `git diff --stat 679775ab..HEAD` → 4 files, +337: `corpus/README.md` (+1), `corpus/SOURCES.md`
  (+2), `corpus/lessons/round-96.md` (+206), `verifiers/verify_dispatch_prompts.py` (+128).
- Instrument: single contiguous 128-line insertion at base offset 37070, **inside `def self_test()`**
  (`def run_checks` and `def self_test` offsets unchanged; `def box_proof` shifts by the insertion);
  prefix and suffix **byte-identical**; reconstruction equals the candidate bytes.
- All 11 c1 anchors: base 1, candidate 1, **0 inside the insertion**; the mutated statements keep
  their line count (the insertion is whole lines).
- `SKILL.md` byte-identical; no `/tmp` literal and no network call in the new code.
- Honest self-test at the candidate: `0 failure(s) over 78 assertions`, rc 0; `--box-proof`:
  `boxes proven 2`, rc 0. Floors registry `dispatch_prompts` floor 56 ≤ 78 (a floor, not an exact
  count — no pinned-count gate found: `check_assertion_floors.py` uses ≥, `box_proof_case_deletion.py`
  runs `--box-proof` only).

## Defects

**D1 — calibration, MEDIUM — the plan miscounts its own pre-freeze sweep.**
`plans/round-96.md` § C1 says "22 hand mutants, **17** survive the 56-assertion self-test".
`receipts/recon-sweep.txt` holds 22 mutants of which **18** read `rc 0` (survivors) and 4 read
`rc 1`; under the v4 outcome classes one of those four (`m-l1-in-08`, `TypeError`) is a RUN-ERROR,
not a kill, so **19 of 22 are non-kills**. The disclosed bound then enumerates only 3 of the
**7** non-target survivors (`m-rstrip-dot`, `m-fleetroot-stem-pass`, `m-empty-baseline-pass`),
omitting `m-fleetroot-no-baseline`, `m-noreport-08-pass`, `m-placeholder-re-angle`,
`m-stem-sibling-pass`. Impacted axes: calibration (the bound understates the residual), depth (the
claim's stated bound). Smallest safe correction: an L1 addendum
(`plans/round-96-addendum-*.md`) stating the receipt's count (22 mutants, 18 rc-0 survivors, 3
reported kills + 1 run error) and enumerating the seven non-target survivors; no predicate, target
or counter change. (The same undercount is repeated in `w1/ExecArmsR96.md` § Risks — the addendum
should cover both texts.)

**D2 — calibration, LOW — the frozen sources receipt carries a wrong word count.**
`receipts/sources-opened.txt` records the POSIX quote as "19 words"; the quoted string measures
**22** (`printf … | wc -w`). The ≤25-word located-quote bound still holds and no reading changes.
The scribe already recorded the drift honestly in `corpus/lessons/round-96.md` § Gate ("Number
drift, recorded not rescued … The true count is 22") without editing the frozen receipt — the right
handling; no further action.

**D3 — labelling, LOW — one landed assertion names the wrong arm.**
`verifiers/verify_dispatch_prompts.py` (candidate) has
`rec("t05-finish-allna-pass: the no-report-path dispatch.04 evaluates 1", r["evaluated"] == 1, …)`
inside the t11 block. The assertion is behavioural and correct; only its label is wrong (it guards
t11's `evaluated` count). The counter does not read labels, so no reading changes. Smallest
correction: rename at the next touch of `self_test()`; not worth a re-land.

**D4 — calibration, LOW-MEDIUM — round-95 routed defect 4 is only partly dispositioned, and its
exit-ladder sub-item is still live in v4.**
The plan names the sub-items "recompile-compare / bytecode forgery worlds; exit ladder; crash
world", then dispositions only the crash world (f2 committed) and the recompile/bytecode worlds
(wave attack item). The **counter exit ladder (ReviewerCounterV3 F1/F3)** sub-item is neither landed
nor explicitly carried or assigned. I probed it: a scratch world whose instrument is not valid UTF-8
(`31b67683`, parent `679775a`) makes v4 exit **1 with a traceback**
(`UnicodeDecodeError … invalid start byte`) instead of 2 could-not-evaluate — ReviewerCounterV3's F1
is unchanged in v4 (`f1-exit-ladder.txt`). F3 (a non-compiling mutant reaching `code_decoy`'s
`ast.parse`) is latent as in v3: the mutant phase's `run_text` compile raises `NotEvaluated` first,
so no frozen reading is affected. Impacted axis: calibration (a routed defect silently dropped).
Smallest safe correction: an L1 addendum line naming the disposition — v4 keeps the v3 0/1/2 ladder
and F1 is carried (or fixed in a later counter), F3 is unreachable for the frozen tables; not
claimed.

## What would have made C1 UNMET (none observed)

- a target surviving or reading RUN-ERROR at the candidate — none (11/11 KILLED, 0 run errors);
- the honest self-test not CLEAN at the candidate — it is CLEAN at 78 assertions;
- a decoy not holding — 11/11 and 11/11 held;
- a frozen anchor matching twice or the production text changing — anchors 1/1/0-in-insertion,
  prefix/suffix byte-identical;
- `r95c1` refusing the generalisation — MET at base and at the candidate;
- a control world meeting the counter — all five UNMET, the do-nothing world UNMET;
- the target being contrived — all 11 reproduce real wrong verdicts on box-named cases.
