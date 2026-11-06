# CriticClaimR100 — falsification of C1 and C2 against the full candidate (round 100, wave r100-w1)

Seat: CriticClaimR100 (critic, leaf; no subagent dispatch). Status: **complete**.

Scratch: `/fast/scratch/hyaku/kotoba-r100/CriticClaimR100/` (clone `repo/` at `03a98eb7`, candidate
`candidate/` at `0add611b`, single-patch clones `cand-scribe/` `ba28f696`, `cand-anchor/`
`58ac7b2a`, `cand-arms/` `2e93a4bc`; TMPDIR and HYAKU_SCRATCH set there; removed before yield).
Receipts: `.ufo/waves/round-100/w1/CriticClaimR100/`.

## Frozen inputs

- Lane base `7b449a637c03d9b4c43a81b4df37cb38c2ea89ee`; instrument `d1e1170d950fc378bb6a28bbfc5a62802669be86`;
  freeze `03a98eb78b63bf9895cbe00ba0f3c8b0e53aa687`.
- C1 counter `verifiers/fixtures/round-100/selftest-kills.py` (v6.2), C2 counter
  `verifiers/fixtures/round-100/anchor-lists.py` (v1). Neither edited by this seat.
- Patches applied in the item's order onto a fresh `--shared` clone at `03a98eb7`, committed with
  the scratch identity: **candidate `0add611bb987fd724b82a396d977857ee56191b0`**
  (`git rev-parse --show-toplevel` = the candidate clone). `git apply --check` passed for all three:
  ScribeCorpusR100 `042c22700eb5b0ac343686ba67cbaf6ba77acbcabdbccf234d971b964ccc67d1`,
  ExecAnchorR100 `f2d1efee8815ef635859fdb2b805e09973ceb6c70a34b447d0005b92c87d9c92`,
  ExecArmsR100 `7b4e2dbc2450ebbc34360c557897b9b60f0895005cd1d0d631b4dac1746c857e`.

## Verdicts

- **C1 on the full candidate: MET.** `c1` → `C1 targets killed 6 of 6 (run errors 0); positive killed
  1 of 1; honest CLEAN; comment decoys held 6 of 6; code decoys held 6 of 6`, `C1-PREDICATE-MET`,
  rc 0 (`full-c1.txt`). Honest self-test `0 failure(s) over 168 assertions` (base 154, +14).
  Per-target blind failure counts: t01 4, t02 1, t03 1, t04 6, t05 1, t06 1 — every one a
  `REPORTED-FAILURE` with a `self-test FAIL: ` line, no run error.
- **C1 `--rules v5`: MET.** Same tally, `C1-PREDICATE-MET`, rc 0 (`full-c1-v5.txt`).
- **C1 positive controls at the candidate: all MET.** `r99c1` 12 of 12, `r98c1` 9 of 9, `r97c1` 13
  of 13, `r96c1` 11 of 11, `r95c1` 3 of 3; every one `…-PREDICATE-MET`, rc 0
  (`full-r99c1.txt`, `full-r98c1.txt`, `full-r97c1.txt`, `full-r96c1.txt`, `full-r95c1.txt`).
- **C2 on the full candidate: MET.** `C2 mismatches 0 of 28; gate GREEN; self-test HELD; revert mutant
  KILLED; frozen 3 of 3; battery ok`, `C2-PREDICATE-MET`, rc 0 (`full-c2.txt`). Battery
  `guards 5 of 5; tip battery exit 0: 4 of 6`; the two red corpus gates are the expected unindexed
  round-99 spot-check lesson plus the new round-100 lesson (the C2 counter does not read them).
- **Do-nothing controls at `7b449a63`: REPRODUCED.** C1 `c1` 0 of 6, UNMET rc 1 (`ctl-c1-base.txt`);
  C1 `--rules v5` 0 of 6, UNMET rc 1 (`ctl-c1-base-v5.txt`); `r99c1` 12 of 12, MET rc 0
  (`ctl-r99c1-base.txt`); C2 `mismatches 8 of 28; gate GREEN; self-test HELD; revert mutant ABSENT;
  frozen 2 of 3; battery ok`, UNMET rc 1 (`ctl-c2-base.txt`). All match the pre-data receipts
  line-for-line except the seed.

### Separability

| candidate | C1 `c1` | C2 |
|---|---|---|
| full `0add611b` | 6 of 6, `C1-PREDICATE-MET`, rc 0 | 0 of 28, `C2-PREDICATE-MET`, rc 0 |
| arms-only `2e93a4bc` | 6 of 6, `C1-PREDICATE-MET`, rc 0 | 8 of 28, `C2-PREDICATE-UNMET`, rc 1 (base state) |
| anchor-only `58ac7b2a` | 0 of 6, `C1-PREDICATE-UNMET`, rc 1 | 0 of 28, `C2-PREDICATE-MET`, rc 0 |
| scribe-only `ba28f696` | 0 of 6, `C1-PREDICATE-UNMET`, rc 1 | 8 of 28, `C2-PREDICATE-UNMET`, rc 1 |

Each claim is achieved by its own patch and not by either sibling; the corpus patch moves neither
counter. Receipts `arms-c1.txt`, `arms-c2.txt`, `anchor-c1.txt`, `anchor-c2.txt`, `scribe-c1.txt`,
`scribe-c2.txt`.

### Structural checks

- **Frozen anchors:** `anchors 56 of 56 match exactly once` in the candidate instrument
  (`anchors-candidate.txt`); the new self-test arms add no anchor occurrence (the two warned forms
  `        if not path.is_dir():` and `    for cid in wanted:` appear only at their original sites).
- **Patch confinement:** `verify_dispatch_prompts.py` diff is one hunk at line 1781, 0 deletions;
  `verify_skill_checklist.py` is three hunks (the one corrections row, the fix line, the self_test
  arms); `check_tip_battery.py` is one hunk inside `INSTRUMENT_PINS`.
- **`--box-proof` at the candidate:** `boxes proven 2`, rc 0. **Checklist `--self-test`:** `0
  failure(s) over 1886 assertions` (base 1864, +22).
- **C2 controls (pre-data receipts re-read):** p1, f1, f2, f3, f4, f5 all `C2-PREDICATE-UNMET`; f2
  (honest fix + row removal + pin, no arm) is refused by the kill conjunct alone (`revert mutant
  SURVIVED; frozen 3 of 3`), so the arm is load-bearing, not decoration.
- **Census:** candidate `corpus/SOURCES.md` `file ok`, rc 0, rows 207 → 211 (S282–S285), one new W04
  (S285 shares S279's URL); the Scribe's receipt matches.
- **S282 grounding:** the opened page's `Path.is_dir` text ("False will be returned if the path is
  invalid, inaccessible or missing, or if it points to something other than a directory") plus the
  `Path.exists` contrast ("True if the path points to an existing file or directory") is exactly the
  pair the t04 arm needs; the L1 receipt's digest `090f3b03…` reproduces. Verified.
- **Mined mistake's control:** `git show 0a65cceb:verifiers/check_tip_battery.py | sed -n 344p`
  prints the `instrument-size` line, no `rev-parse`; line 349 at `0a65cceb` and line 344 at
  `52e8e95a` carry the read. The revision-qualified fix (C100-1 + Q90) is falsifiable and the
  committed control fails the bare pointer. Verified.

## Attack findings

A1 **Do-nothing / cheaper change.** Do-nothing is UNMET on both claims (reproduced). The pre-data
controls refuse the cheaper C2 shapes: fix line only (mismatches 0, gate RED, revert SURVIVED,
frozen 2 of 3, battery FAIL), no-arm (refused by the kill conjunct alone), row-kept (gate RED),
data-only removal (mismatches 8), governance-forced-PASS (frozen refuses). No cheaper C1 shape
reaches 6 of 6: each target needs its own observation, and the arms are the only inserted code.

A2 **C2 axis naming.** The surface is the checklist gate; the axis is consistency/calibration. The
fleet-shaped sandbox `--json` diff base→candidate (built by the round-base `build_sandbox`) shows
**no collateral reading change**: 11 PASS / 0 FAIL / 0 N/A both sides, exit 0 both sides; the only
difference is `governance.citation_resolves` evaluated 1665→1666 and corrections excused 19→18 — the
retired row's subject now resolves and is counted instead of excused. `trigger.citation_resolves`
and `trigger.command_binary_resolves` subject lists are byte-identical (`json-sandbox-diff.txt`).
This is a real calibration change (the gate's model of "resolves" now matches its documented
contract), not relabelled bookkeeping; but the real-tree gate verdict is green before and after, so
the claim's real-tree effect is the removal of the workaround plus one counted subject — modest, and
disclosed in the plan.

A3 **Truth table's "resolves".** Hand-checked all 14 rows against the fixed regex and the real
`citation_resolve`: r01–r04 comma forms resolve; r05–r07 single/range/bare resolve; r08–r14 stay red
(missing file, word segment, empty segment, dangling dash, leading comma, word anchor). The counter's
header discloses it does not check line existence; the fixture file has 40 lines and every positive
anchor is in range. The real checklist's `trigger.citation_resolves` runs over SKILL.md, whose comma
anchors (`S090 :10,18,34,40-42`, `skills.mdx:137,142`) are source-ID/relative tokens outside
`CITATION_ROOTS`, so the real SKILL.md never needs the fix; the only real-tree repo-path comma anchor
is `SCORECARD.md:529` (the retired row's subject), and the fix heals it. The claim is a calibration
fix, not a live-red repair — honest, but its real-tree scope is one token.

A4 **C1 targets.** t01 (not-a-directory exits 0), t02 (substrate EnvError exits 1), t03 (`--json`
payload `exit_code 0`), t04 (`exists()` lets a plain file reach `iterdir`) are real exit-ladder
defects; t05 (latin-1 decode) is a real decode-contract defect; t06 (stable sort) is the weakest: it
changes only presentation order, no verdict, no exit code, and no documented order contract. The
exclusions are honest (m19 provably equivalent, m09 reporting-only, m21 latent on the committed
SKILL.md, m04 RUN-ERROR); m03's admission is honest (the `--json` payload is the machine-readable
verdict). The claim's "6 of 6" is met, but t06 is a framing stretch a canonical judge may discount.

A5 **S282 grounds t04** — verified (above).

A6 **Mined mistake's control** — verified (above).

A7 **v7 counter carry.** Recorded as carried, not claimed, with a reason (a rules change needing its
own forgery controls). Honest as a disclosure; it is now a three-round deferral (98→99→100) and
remains a routed debt, not a defect in this round's claims.

## Defects

- **D1 (C1, framing).** `t06-runchecks-sorted` is presentation-order only: a stable sort changes no
  verdict, no exit code, and no documented order contract; the instrument's docstring specifies exit
  codes but not result order. The arm is a legitimate function-contract assertion, but calling the
  survivor a "false green of the exit/decode/order contract" overstates it. Smallest safe correction:
  keep the arm, and name t06 in the plan/report as an order-contract target rather than a
  verdict-bearing false green (the plan already partly does); the frozen predicate cannot change
  after scoring, so this is a framing note for the canonical judge, not a rescue.
- **D2 (C2, scope).** The real-tree gate is green at the base (via the round-99 correction row) and
  green at the candidate; the only real-tree observable change is the +1 evaluated subject and the
  −1 correction. The claim's measured improvement is on the hermetic truth table. Honest, but the
  "consistency" axis is calibrated by a fixture, not by a live red; a reader should not read C2 as a
  repo-state repair.
- **D3 (carried).** The v7 counter (g11/g16) is carried again; disclosed, not claimed. No action this
  round.
- **D4 (expected drift, not a claim failure).** The full candidate's corpus gates stay red
  (`verify_corpus_integrity.py` exit 1, `verify_corpus_independent.py` exit 1) from the unindexed
  round-99 spot-check lesson and the new round-100 lesson; the C2 counter does not read them and the
  plan assigns the coverage-map rows and baseline re-record to the L1.
