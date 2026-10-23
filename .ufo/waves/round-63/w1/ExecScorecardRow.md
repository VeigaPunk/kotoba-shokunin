# ExecScorecardRow
role: SCORECARD draft scribe
item: Draft the append-only round-63 axis annotation and replacement Next line.

## Findings

1. Existing style is an append-only “Round 62 axis annotations” paragraph followed by a separate “Next: round 63” line; it keeps the score and verdict beside the counted command and receipt reference. Evidence: `SCORECARD.md:36` and `SCORECARD.md:371`.
2. The frozen C1 predicate is `python3 -B verifiers/check_scoped_rules_v32.py --self-test` and requires the three exact output lines below, exit 0. The committed do-nothing v31 control at `35d44b4b` records `survivors closed 5 of 6`, the G9 instance still accepted, and only two must-fail arms. Evidence: `plans/round-63.md:35-75`; `.ufo/waves/round-63/controls/C1-do-nothing-v31.txt:1-12`.
3. The C2 plan expects `0 of 5` at base `35d44b4b` and `5 of 5` at the measured r63 tip; the five checks are bounded to the r62 routed defects. This is the plan’s expected result, not an execution receipt observed for this draft. Evidence: `plans/round-63.md:88-120`.
4. The previous Next line names W8 and A2/F6 as survivor debt and lists the standing quality debt. The C2 plan bounds its counter to the five named defects, leaving any new mismatch class out of scope. Evidence: `SCORECARD.md:371`; `plans/round-63.md:119-120`.
5. This is proposed SCORECARD text only: no product file was changed and no r63 after-result was run or independently observed here. The `<measured-commit>` placeholders must be replaced only from the eventual measured receipt/commit; “measured” and the after counts below are requested draft content, not execution evidence from this seat.

## Artifacts

```markdown
**Round 63 axis annotations (append-only; verdicts belong to the non-author closure).** *Depth (C1, score held 9; verdict: measured):* `python3 -B verifiers/check_scoped_rules_v32.py --self-test` → `worlds reject 7 of 7; eligible rows pass 4 of 4` / `survivors closed 6 of 6` / `must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes`, exit 0 @<measured-commit>. Before: the v31 do-nothing control, `python3 -B verifiers/check_scoped_rules_v31.py --self-test`, records `survivors closed 5 of 6` and only two must-fail arms @ `35d44b4b`; after: v32 closes `6 of 6`. The G9-disabled control must admit the frozen instance as shown by the third predicate line. *Calibration (consistency sub-axis; C2, score held 8.5; a band move waits on the non-author closure):* `python3 -B verifiers/check_r63_routed_repairs.py --rev <rev>` → `r62 routed defects closed 0 of 5`, exit 1 @ `35d44b4b` → `r62 routed defects closed 5 of 5`, exit 0 @<measured-commit>.
```

```markdown
**Next: round 64** — survivor debt: the W8 escape class and A2's F6 compound-purpose bound; C2 remains bounded to the five r62 spot-check defects, so a new self-assessment mismatch class remains outside its counter. Carry-forward quality debt until evidenced closed: SentBounds' pre-wave baseline receipt; helper-invocation receipts; the r62 wave-2 dispositions.
```

## Scope

- Behavior: drafted the round-63 depth/calibration annotation and the replacement Next line; neither was applied to `SCORECARD.md`.
- Gates: none run; no r63 after-result was executed or independently observed.
- Touched surface: this report only. Out of scope: production files, `SCORECARD.md`, tests, commits, and all other lane files.
- Artifact path: `.ufo/waves/round-63/w1/ExecScorecardRow.md`.

## Verdict

PROPOSES — I would change this to an execution-backed scorecard entry only after the v32 self-test, C2 `--rev` counter, and a measured commit/receipt are available; update the Next line if those receipts or the carried debts establish a different survivor/quality-debt state.
