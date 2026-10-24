# CriticW2CalibrationMapping

role: UFO-FSD critic (leaf; advisory evidence, not admission or canonical judgment)
item: Attack round-63 score-axis identity and require a bounded C2 reconciliation with numeric delta 0.
reviewed revision: `cbbee56e9a3589b0b46736ad36f1b77701def80e`

## Axes and verdict on the committed bytes

**Impacted axis: calibration**, specifically truthful ownership, score identity, and the scope of the consistency reconciliation. Depth is named only to establish the lowest owned score.

**Advisory verdict: the score-mapping claim is falsified; actual numeric score inflation is not observed.** The committed plan and two committed draft artifacts conflate the owned consistency sub-axis (10) with separate advisory calibration (8.5). `SCORECARD.md` itself is unchanged from the frozen before revision. The C2 counter really returns 5/5 at the reviewed revision, but that result coexists with the false score mapping: it does not check score-axis identity. The defect is fixable by an explicit mapping erratum and a zero-delta, bounded C2 annotation—not by switching which row supplies the before or after score.

## Counterexample and exact failure locations

The strongest counterexample is the real reviewed tree, not a hypothetical mutant:

1. `SCORECARD.md:11-15` declares **consistency a sub-axis of calibration** and makes non-owned axes advisory. Its row at `:29` is `| consistency (calibration sub-axis) | 10 |`; `:33` is `| calibration (advisory) | 8.5 — was 8.0 |`. Depth at `:28` is 9. The round-62 completion at `:369` explicitly says “the consistency row held 10.” The earlier disposition at `:365` already identifies depth 9 as lowest owned.
2. At the same tree, `plans/round-63.md:6` says **“Lowest owned axis: calibration/consistency (8.5) below depth (9)”** and `:9` says **“C2 works the lowest owned axis (calibration).”** Both fail the declared owned-row mapping. `:77` additionally reverses the hierarchy in **“calibration (consistency sub-axis)”**. The opening `:5-6` has the hierarchy right; the C2 heading does not.
3. `.ufo/waves/round-63/w1/ExecScorecardRow.md:16` proposes **“Calibration (consistency sub-axis; C2, score held 8.5; a band move waits on the non-author closure)”**. This is the unsafe drafted C2 row: it attaches 8.5 to the reversed sub-axis label, omits the separate owned 10, and does not explicitly record numeric delta 0 or the in-sample reconciliation bound. It must not be copied into the live scorecard as written.
4. `.ufo/waves/round-63/w1/ScribeReportSkeleton.md:58` repeats **“C2 works the lowest owned axis, calibration/consistency (8.5), below depth (9)”** in the drafted Trend verdicts. Its `:6` accurately reports what the erroneous plan says, but is not independent support for that mapping. The draft body at `:58` fails if used as the current round assessment.
5. Provenance of the faulty score instruction is preserved in `.ufo/waves/round-63/w1-spec.json:91` and `.ufo/waves/round-63/w1-dispatch.json:407`, in the `ExecScorecardRow` payload: **“(b) C2 calibration — score held 8.5 (a band move waits on the non-author closure)”**. These are historical dispatch data, not an authority to override `SCORECARD.md`. Preserve them; supersede their erroneous mapping explicitly in the integrated annotation.

### Other requested surfaces

| Surface at the reviewed revision | Finding |
|---|---|
| `SCORECARD.md` | Correctly distinguishes owned consistency 10 from advisory calibration 8.5. No round-63 C2 score annotation has landed; `:36` is still the round-62 annotation and `:371` is still “Next: round 63.” No actual score increase was made. |
| `corpus/lessons/round-63.md:1-64` | No 8.5/10 identity swap or numeric increase. However, it does not carry the mapping reconciliation or an explicit C2 numeric delta 0. Its M94 arithmetic erratum does not correct the distinct ownership error. |
| `LOG.md:2568-2575` | The appended round-62 correction block names factual repairs, not scores. No label swap or score increase appears there; it also lacks the mapping/zero-delta reconciliation. |
| `.ufo/waves/round-63/w1/ScribeLesson.md:20,42,70` | Safely flags the mapping conflict and declines a numeric increase. This is a draft report, not the landed lesson, and its warning was not integrated into that lesson. |
| `.ufo/waves/round-63/w1/CriticCalib.md:76-78` | Already correctly distinguishes the two rows and recommends numeric delta 0. A warning in a seat report does not itself correct the plan or the proposed score row. |
| `corpus/knowledge/compound-clause-citation-round63.md:43-52,89-91` | Calls correction practice calibration and explicitly bounds the checks to token linkage; it assigns neither 8.5 nor 10 and does not interchange them. |

**Bound:** no committed text inspected asserts an earned +1.5 increase. Producing one by taking advisory 8.5 as the baseline and owned consistency 10 as the result would be an identity switch, not improvement. Likewise, silently relabeling the owned row to 8.5 would change recorded ownership/score, not reconcile it. These are unsupported framings, not acceptable tradeoffs to balance against successful repairs; admission remains the canonical judge's decision.

## Attack commands and verbatim output

Only revision-pinned extracted code was executed. C2 reads committed lane objects through `--root`; no lane worktree, Git index, or jj state was changed. Independent probes were run concurrently. Exit status is recorded separately from process output.

### Pinning the reviewed bytes

Working directory: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.

```sh
mktemp -d /tmp/kotoba-r63-calibration.XXXXXX
```

```text
/tmp/kotoba-r63-calibration.E1y2y6
```

Exit 0.

```sh
git archive cbbee56e9a3589b0b46736ad36f1b77701def80e | tar -x -C /tmp/kotoba-r63-calibration.E1y2y6
```

No stdout; exit 0. File/regex inspections above used `read`/`grep` tools against this extracted snapshot, not mutable lane files. In particular, both JSON payloads were opened with `?q=.. | objects | select(.name? == "ExecScorecardRow")` to inspect the complete score instruction, rather than relying on truncated search excerpts.

### Did an actual scorecard change land?

Working directory: lane repo (read-only object comparison).

```sh
git diff --exit-code 35d44b4b4dcdda234b5dbff7af37e432fec55f05 cbbee56e9a3589b0b46736ad36f1b77701def80e -- SCORECARD.md
```

No stdout; exit 0. Thus the faulty plan/draft is not evidence that the authority's numeric scores actually increased.

### C2 before control

Working directory for this and subsequent Python commands: `/tmp/kotoba-r63-calibration.E1y2y6`.

```sh
python3 -B verifiers/check_r63_routed_repairs.py --root /home/vgpnk/Projects/shokunin/kotoba-shokunin --rev 35d44b4b4dcdda234b5dbff7af37e432fec55f05
```

```text
FAIL late-write-tracked   not a tracked blob at 35d44b4b4dcdda234b5dbff7af37e432fec55f05
FAIL receipt-rev-named    LOG never names 3f911504ce76d9ca186f297d6d4a9cd8ed77508a
FAIL entry-size-named     LOG never states 64 lines / 1044 words for corpus/knowledge/erratum-absorption-round62.md
FAIL append-only          prefix=True grew_by=0 line(s)
FAIL noharm-arms-named    LOG does not name reg_gate 36 of 38 + corpus-idx
r62 routed defects closed 0 of 5
```

Exit 1.

### C2 reviewed tree: all checks pass while the mapping is wrong

```sh
python3 -B verifiers/check_r63_routed_repairs.py --root /home/vgpnk/Projects/shokunin/kotoba-shokunin --rev cbbee56e9a3589b0b46736ad36f1b77701def80e
```

```text
PASS late-write-tracked   tracked at cbbee56e9a3589b0b46736ad36f1b77701def80e
PASS receipt-rev-named    LOG names 3f911504ce76d9ca186f297d6d4a9cd8ed77508a on 1 line(s)
PASS entry-size-named     LOG states 64 lines / 1044 words on 1 line(s)
PASS append-only          prefix=True grew_by=9 line(s)
PASS noharm-arms-named    LOG names reg_gate 36 of 38 + corpus-idx on 1 line(s)
r62 routed defects closed 5 of 5
```

Exit 0. `verifiers/check_r63_routed_repairs.py:162-168` lists its five checks; none reads `SCORECARD.md` or tests the plan's axis labels. The positive result therefore cannot establish score mapping, a numeric score increase, or general calibration. Do not change the frozen counter after data just to make it certify a broader claim.

### C2 instrument controls

```sh
python3 -B verifiers/check_r63_routed_repairs.py --self-test
```

```text
self-test: 0 failure(s) over 15 assertions
```

Exit 0. This is the instrument's finite control result, not a score-axis measurement.

### C1 counting predicate (round cross-check; no calibration-score inference)

```sh
python3 -B verifiers/check_scoped_rules_v32.py --self-test
```

```text
counter sha256 4246069129115f039158fa5abe1b9f592b167d5438e5e7c5e9b2b21468c17c33
world W1: Claude Code reject=True arm=A4 line='entry row S900: A4: snapshot sha256 06277eb1ae94... is already recorded by base row S010 and the teaches cell declares no supersedes'
world W2: Claude Code reject=True arm=A3 line="entry row S900: A3: URL 'https://code.claude.com/docs/de/memory.md' is a rendering alias of the committed row S112 URL 'https://code.claude.com/docs/e"
world W3: Cursor reject=True arm=A1 line="entry row S903: A1: scope key 'rules' is not a canonical key for Cursor (canonical: globs); S903 URL 'https://cursor.com/docs/rules' is already a base"
world W4: Cursor reject=True arm=live line='live page: not found'
world W5: Claude Code reject=True arm=A1 line="entry row S900: A1: scope key 'patterns' is not a canonical key for Claude Code (canonical: paths)"
world W6: Claude Code reject=True arm=A2 line='entry row S900: snapshot .ufo/waves/round-60/snapshots/S900.page: A2: action cell supports 5 of its 8 content word(s) at line 6 (need >= 6)'
world W7: all reject=True arm=A1
world W0: exit=1
worlds reject 7 of 7; eligible rows pass 4 of 4
survivor e2c-wrong-supersedes-target: before accepted; after rejected
survivor e2c-supersedes-with-fresh-fetch: before accepted; after rejected
survivor e2e-negated-path-key: before accepted; after rejected
survivor e2e-commented-equals-key: before accepted; after rejected
survivor e2f-backticked-event-claim: before accepted; after rejected
survivor e2f-compound-purpose-outside-citation: before accepted; after rejected
survivors closed 6 of 6
must-fail E2e guard disabled admits e2e-negated-path-key: yes
must-fail G7 disabled admits e2f-backticked-event-claim: yes
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
self-test: 0 failure(s) over 208 assertions
```

Exit 0.

```sh
python3 -B verifiers/check_scoped_rules_v31.py --self-test
```

```text
counter sha256 a07c2269ea077e4866827e3fae907c45aea7c960bbe5f56b21210a0cecea3858
world W1: Claude Code reject=True arm=A4 line='entry row S900: A4: snapshot sha256 06277eb1ae94... is already recorded by base row S010 and the teaches cell declares no supersedes'
world W2: Claude Code reject=True arm=A3 line="entry row S900: A3: URL 'https://code.claude.com/docs/de/memory.md' is a rendering alias of the committed row S112 URL 'https://code.claude.com/docs/e"
world W3: Cursor reject=True arm=A1 line="entry row S903: A1: scope key 'rules' is not a canonical key for Cursor (canonical: globs); S903 URL 'https://cursor.com/docs/rules' is already a base"
world W4: Cursor reject=True arm=live line='live page: not found'
world W5: Claude Code reject=True arm=A1 line="entry row S900: A1: scope key 'patterns' is not a canonical key for Claude Code (canonical: paths)"
world W6: Claude Code reject=True arm=A2 line='entry row S900: snapshot .ufo/waves/round-60/snapshots/S900.page: A2: action cell supports 5 of its 8 content word(s) at line 6 (need >= 6)'
world W7: all reject=True arm=A1
world W0: exit=1
worlds reject 7 of 7; eligible rows pass 4 of 4
survivor e2c-wrong-supersedes-target: before accepted; after rejected
survivor e2c-supersedes-with-fresh-fetch: before accepted; after rejected
survivor e2e-negated-path-key: before accepted; after rejected
survivor e2e-commented-equals-key: before accepted; after rejected
survivor e2f-backticked-event-claim: before accepted; after rejected
survivor e2f-compound-purpose-outside-citation: before accepted; after accepted
survivors closed 5 of 6
must-fail E2e guard disabled admits e2e-negated-path-key: yes
must-fail G7 disabled admits e2f-backticked-event-claim: yes
bound: G9 remains unimplemented; e2f-compound-purpose-outside-citation survives per CriticC1Hollow.
self-test: 0 failure(s) over 201 assertions
```

Exit 0.

## Smallest safe correction — exact proposed text

Preserve the frozen plan and historical seat/dispatch reports. Append the following named mapping erratum to the plan, and carry its mapping into the lesson and appended LOG record. Do not silently rewrite the pre-data declarations or replace the existing 10 with 8.5.

```markdown
## Score-axis mapping erratum (post-data; frozen predicates unchanged)

The owned SCORECARD row is `consistency (calibration sub-axis)` at 10. The separate `calibration (advisory)` row is 8.5; these scores and ownership labels are not interchangeable. This corrects this plan's opening claim that calibration/consistency 8.5 is the lowest owned axis and its C2 heading's reversed parent/sub-axis wording. Among the owned rows, depth 9 is lowest, and C1 works depth. The all-axes versus owned-only lowest-axis question remains open; this correction does not resolve it by relabeling an advisory row as owned.

C2 works consistency (calibration sub-axis; owned): a bounded, externally prompted, in-sample reconciliation of the named r62 spot-check discrepancies under five committed-byte checks. Recorded scores are held: consistency 10 → 10, numeric delta 0; separate advisory calibration 8.5 → 8.5, numeric delta 0. The repair-check count is not an axis score, five independent routed-defect closures, unseen-case calibration accuracy, or evidence of saturation. No score increase or new axis assignment is claimed.
```

Use this exact C2 annotation instead of the unsafe drafted C2 segment (the unrelated C1 segment need not change):

```markdown
**Round 63 C2 — consistency (calibration sub-axis; owned): bounded reconciliation; numeric delta 0.** The recorded consistency score is held 10 → 10. Separate advisory calibration is held 8.5 → 8.5, numeric delta 0; it is not the owned C2 score. `python3 -B verifiers/check_r63_routed_repairs.py --rev <rev>` prints `r62 routed defects closed 0 of 5`, exit 1 @ `35d44b4b4dcdda234b5dbff7af37e432fec55f05`, and `r62 routed defects closed 5 of 5`, exit 0 @ `cbbee56e9a3589b0b46736ad36f1b77701def80e`. These are five finite committed-byte repair checks for the known r62 spot-check, not an axis-score increase or general calibration evidence. The counter's headline is its frozen label, not proof that every routed obligation is closed. Holding the prior recorded 10 does not newly establish saturation. Verdicts remain with the non-author closure.
```

For the drafted report's Trend verdicts, replace the erroneous lowest-owned sentence with:

```text
C1 works depth, the lowest owned score at 9. C2 works the owned consistency sub-axis of calibration, recorded at 10; it is a bounded reconciliation with numeric delta 0. The separate advisory calibration score remains 8.5, numeric delta 0. These labels are not interchangeable, and the all-axes versus owned-only lowest-axis question remains open.
```

The correction does not require a counter redesign, a numeric raise, a new authority, or a retrospective claim retargeting. The integrated report should point to this seat report as the executed measurement evidence; this seat is not an outside-lane promotion or discernment verifier.

## New source reopened and review bounds

Reopened the round's new [S119, ICMJE — Corrections and Version Control](https://www.icmje.org/recommendations/browse/publishing-and-editorial-issues/corrections-and-version-control.html) with the static `read` URL tool on 2026-10-23. The returned native-reader text includes: “The journal should archive all prior versions of the article.” This supports preserving prior records and identifying corrections; it supplies neither score values nor ownership authority. No byte-identity, HTTP-code, or digest comparison is claimed for this reader fetch.

Only this assigned lane report was written. Scratch extraction and the instrument's constructed repositories were confined to `/tmp`. No production changes, Git-index/jj mutations, runtime judgments, builds, linters, formatters, or tool installs/updates were performed. Verification exercised is exactly the commands above. L1 integration, any resulting remeasurement, and canonical judgment are not performed by this critic.

Report: `.ufo/waves/round-63/w2/CriticW2CalibrationMapping.md`
