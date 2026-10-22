# BoxProofCoverage — C2 operability and routed defect D2 (round 50, build wave)

Seat: BoxProofCoverage (executor, operability). Lane base `f30464660c675d1c1e2851a3bf0366a3aaffe5a8`.
Scratch: `/fast/scratch/hyaku/kotoba-r50/build/BoxProofCoverage/` (`lane/` = private clone at the base
commit, `verifyclone/` = fresh base clone with the patch applied, `basefile/` = the base instrument for
the before-measurements). No lane, fleet or sibling file was written except this report. No tool was
installed or upgraded. Python 3.14.8, git 2.56.0.

**Result:** the box proof now enforces its own fixture coverage: every one of the six named conjuncts
needs an *isolated* must-fail case, so deleting any one of the six must-fail manifest entries exits 1
(0 of 6 → 6 of 6), the intact corpus still prints `boxes proven 2` exit 0, and the docstring, the
`--box-proof` help text and the module docstring now state the six-conjunct bound and the four
box clauses that are not proven.

## Files changed

* `verifiers/verify_dispatch_prompts.py` — the only code file (the assignment's file bound).
* No new fixture file: the committed `verifiers/fixtures/dispatch-prompts/manifest.json` already
  carries one must-fail case per named conjunct, plus the two controls and the N/A case.

Patch (unified diff against `f30464660c675d1c1e2851a3bf0366a3aaffe5a8`, one file,
+331/−12): `/fast/scratch/hyaku/kotoba-r50/build/BoxProofCoverage/patch.diff`
(sha256 `5f170988e020ccb75c24b564e05b107d9446753ed46417dea3bc02b105d7a7ba`).
`git -C verifyclone apply --check` → exit 0; the applied tree is what the evidence below was measured on.

## What landed (L1 steer items 1–3 and 5)

1. **Coverage on the observation, not the label.** The single pinned list is the existing `CONJUNCTS`
   constant, moved next to `PINNED_BOX_SHA` (no second list). A conjunct `n` of box `cid` is covered
   only when some case has `expect_verdict == "FAIL"`, observed verdict FAIL, observed `n` FAIL, and
   its *other* observed FAIL conjuncts are a subset of the new pinned
   `ALLOWED_CO_FAIL = {"report_path_literal": frozenset({"report_stem_is_lane_id"})}` (one-line reason
   in the code: the report path's placeholder sits inside the file stem). Each uncovered conjunct gets
   its own stderr line, e.g. `box-proof: dispatch.04: no isolated must-fail case for conjunct
   report_stem_is_lane_id`. The box is not counted → `boxes proven 1`, exit 1.
2. **Controls and the N/A arm.** Each box also needs a must-pass case whose *observed* conjuncts are
   all PASS (`box-proof: dispatch.04: no all-PASS control case`) and, for the box that owns the arm, a
   case whose observed `round_le_latest_dispatched` is N/A (`box-proof: dispatch.08: no N/A case for
   conjunct round_le_latest_dispatched`). Both lines are their own problem line; both make the box
   uncounted (exit 1).
3. **Substrate errors.** `EnvError`/`OSError` raised while a case is evaluated (missing fixture
   directory, unreadable fixture file) is caught per case, reported as a problem line and answered
   with **exit 2**, never a traceback. The base answers the same input with an uncaught
   `FileNotFoundError` traceback and exit 1.
5. **Discriminating self-test arms**, shown failing on the base first: twin-then-delete exits 0;
   note-only manifest edit exits 0; "delete `d04-stem` plus add a placeholder copy labelled stem"
   exits 1. Plus: each of the six must-fail deletions exits 1 and names its box and conjunct; each
   control and the N/A deletion exits 1; a corpus with no must-fail case proves no box; a case naming
   a conjunct the box does not have is rejected; a missing fixture directory is exit 2, no traceback.

**D2 (wording).** The `box_proof` docstring, the `--box-proof` help text and the module docstring no
longer say the fixtures "discriminate every conjunct". They now name the six conjuncts, state one
must-fail fixture case each, state that the coverage is read from the observed statuses rather than
the case labels, and state that the box clauses without a fixture — the unsubstituted variable,
`<=` at equality, the legacy-state arm and a non-digit round folder — are **not** proven.

## Evidence

Commands (in the scratch clone at the base commit, and in `verifyclone/` with the patch applied):

```
python3 -B verifiers/verify_dispatch_prompts.py --box-proof --map verifiers/checklist-baseline.json
python3 -B verifiers/verify_dispatch_prompts.py --self-test
```

**Before (base instrument, `basefile/verify_dispatch_prompts.py`):**

| arm | exit | stdout |
|---|---|---|
| intact | 0 | `boxes proven 2` |
| delete `d04-placeholder` | 0 | `boxes proven 2` |
| delete `d04-stem` | 0 | `boxes proven 2` |
| delete `d04-unknown-lane` | 0 | `boxes proven 2` |
| delete `d08-role-round` | 0 | `boxes proven 2` |
| delete `d08-report-dir-round` | 0 | `boxes proven 2` |
| delete `d08-above-state` | 0 | `boxes proven 2` |
| note-only manifest edit | 0 | `boxes proven 2` |
| delete `d04-stem` + placeholder copy labelled stem | 0 | `boxes proven 2` |
| missing fixture directory | 1 | (empty) — uncaught `FileNotFoundError` traceback on stderr |

Base self-test: `0 failure(s) over 32 assertions`, exit 0.

**After (patch applied):**

| arm | exit | stdout | stderr |
|---|---|---|---|
| intact | 0 | `boxes proven 2` | (empty) |
| delete `d04-placeholder` | 1 | `boxes proven 1` | `dispatch.04: no isolated must-fail case for conjunct report_path_literal` |
| delete `d04-stem` | 1 | `boxes proven 1` | `dispatch.04: no isolated must-fail case for conjunct report_stem_is_lane_id` |
| delete `d04-unknown-lane` | 1 | `boxes proven 1` | `dispatch.04: no isolated must-fail case for conjunct lane_identity_known` |
| delete `d08-role-round` | 1 | `boxes proven 1` | `dispatch.08: no isolated must-fail case for conjunct filename_role_round_equal` |
| delete `d08-report-dir-round` | 1 | `boxes proven 1` | `dispatch.08: no isolated must-fail case for conjunct filename_report_dir_round_equal` |
| delete `d08-above-state` | 1 | `boxes proven 1` | `dispatch.08: no isolated must-fail case for conjunct round_le_latest_dispatched` |
| delete `d04-control` | 1 | `boxes proven 1` | `dispatch.04: no all-PASS control case` |
| delete `d08-control` | 1 | `boxes proven 1` | `dispatch.08: no all-PASS control case` |
| delete `d08-missing-state` | 1 | `boxes proven 1` | `dispatch.08: no N/A case for conjunct round_le_latest_dispatched` |
| twin of `d04-stem` replaces it | 0 | `boxes proven 2` | (empty) |
| note-only manifest edit | 0 | `boxes proven 2` | (empty) |
| delete `d04-stem` + placeholder copy labelled stem | 1 | `boxes proven 1` | `dispatch.04: no isolated must-fail case for conjunct report_stem_is_lane_id` |
| missing fixture directory | 2 | `boxes proven 1` | `dispatch.04/d04-stem: [Errno 2] No such file or directory: …` (no traceback) |

Every stderr line above is prefixed `box-proof: ` in the real run.

**Self-test counts.** After: `0 failure(s) over 56 assertions`, exit 0 (base: 32 assertions, 0
failures). The same 24 new arms run against the **base** instrument (the arms spliced into the base
file, `box_proof` untouched) give `18 failure(s) over 56 assertions`, exit 1 — the 18 are the six
must-fail deletions (12 arms), the three control/N/A deletions, the laundering arm, the
no-must-fail-corpus arm and the substrate-error arm. The arms that must hold on both sides (intact
proof, note-only edit, twin) pass on the base, so they are not the discriminator; the coverage and
substrate arms are.

**Other checks.** `python3 -m py_compile verifiers/verify_dispatch_prompts.py` → exit 0.
`git -C verifyclone apply --check ../patch.diff` → exit 0; after applying, self-test exit 0 and
`boxes proven 2` exit 0.

## Risks and blockers

* **A plain relabel of the placeholder case, without a deletion, still exits 0** (`boxes proven 2`).
  That is the intended consequence of reading the observation instead of the label: the coverage is
  unchanged, so the proof is unchanged. The laundering form the steer names — delete `d04-stem` and
  add a placeholder copy labelled stem — exits 1. A hash-pin implementation would fail the twin and
  the note-edit arms; this implementation passes them, so the arms discriminate the two mechanisms.
* **The proof is coupled to the pinned box text.** A reworded `dispatch.04`/`dispatch.08` box in
  `SKILL.md` makes the proof fail loudly (pin mismatch) and the new self-test copies the live
  `SKILL.md`, so a box reword without a re-pin also fails the self-test. That is the pre-existing pin
  contract, unchanged by this seat.
* **The self-test reads the live `SKILL.md`** (`Path(__file__).parent.parent / SKILL_NAME`) and copies
  it into a temporary tree; it never writes the lane's copy.
* **Not mine, still open:** the SCORECARD operability row, the claim headline and the decision to run
  `--box-proof` from a gate are the L1's/records seat's files (D2 wording outside my file bound); the
  deletion driver and its denominator (critic item 4) belong to the driver seat. The `SKILL.md`
  sentence at lines 128–133 lists three unproven clauses; the fourth (non-digit round folder) is
  named in the instrument's docstring and help text only.
* No blocker. The change is confined to one file; the L1 integrates the diff.
