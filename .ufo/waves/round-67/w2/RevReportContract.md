# RevReportContract — round 67, wave 2

## Scope and attack

This attacks **the draft's readiness to satisfy the canonical round-report contract**, not the
truth of landed C1/C2. The compared contract is
`/home/vgpnk/Projects/shokunin/.ufo/prompts/kotoba-round-67.md` §4, especially lines 99–129.
The reviewed draft is
`.ufo/waves/round-67/w1/drafts/round-67-report.md`; `git status --short -- <that path>` was empty
and `git rev-parse master` printed `da86c03e482a6aef433c34d733726b37c7cf6607`.
The pinned base `2a8eba56b3f9321b70c569fa2816d42237ca49a2` is distinct; it was not
re-measured in this contract review.

The strongest counterexample is simple: filing the current bytes unchanged would file a
self-declared skeleton (draft lines 1–11), not a completed report. The draft is honest about
that limitation; the successful attack is against **contract completeness**, not against its
honesty.

**Verdict: final-report readiness is falsified.** All six intended sections occur in the intended
order, all six top-level Work-performed bullets have pointer fields, and the SHONEN marker shape
passes. Those positives do not cure the unfilled landed/measurement/frontier data or the absence
of all three Trend verdicts. This is a scoped recommendation, not a round-admission judgment.

## Findings by severity

### Blocker if filed unchanged — required landed, measurement, and frontier values are still placeholders

The draft contains **74 literal `TBD` occurrences on 71 lines** (a mechanical lexical count,
including mentions in instructions and commands, not a claim of 74 distinct semantic fields).
Every required section contains at least one. Concrete contract failures are:

- **Landed changes:** §4 requires every change to be tied to a `LOG.md` entry and its carrying
  commit (contract lines 107–108). The draft instead says it “asserts no landing” while TBD slots
  remain (line 77), leaves the inventory revision as `TBD` (lines 79–81), and leaves both the LOG
  pointer and carrying hash unfilled in all six landed-change bullets (lines 83–124).
- **Before → after measurements:** §4 requires one measurement per claim with its counting
  command and measured commit (contract lines 109–110). Commands are present for C1 (draft lines
  136–141) and C2 (165–169), but the integrated tip is TBD (131–132). C1 lacks the committed base
  receipt, observed half-controls, all after outputs/exits, and its hit/miss verdict (143–161).
  C2 lacks observed base/junk results, counter-falsification evidence, after output/exit, and its
  hit/miss verdict (171–188). A command plus a target is not an observed measurement.
- **Sources & frontier:** §4 requires rows before→after with a counting command, rows added by
  tier, rows touched old→new, and frontier rows advanced (contract lines 111–115). The draft has
  the command shape, but the after row count and one counting-command revision are TBD (205–214),
  as are the added-tier ledger (215–226), touched-row ledger (227–233), and advancement ledger
  (234–237). Census after-data and the Gate/mistake evidence are also unfilled (198–204, 238–244).

These are exactly the kinds of placeholder slots that must not become a completion marker under
contract lines 121–125. **Repair:** populate them from committed bytes and observed receipts at a
named full measured revision; do not convert the plan's targets into results.

### High — none of the three Trend lines carries a verdict or supporting evidence

The contract requires exactly one of `improved`, `harmed`, `unchanged`, or
`unprovable-but-better`, with evidence, for each of expansion, quality, and discernment
(contract lines 116–117). The draft has three correctly labelled bullets but their values are:

| Trend | Draft evidence | Result |
|---|---|---|
| expansion | `TBD (expansion verdict)` and instructions to fill it, lines 252–254 | no verdict; no supporting observation |
| quality | `TBD (quality verdict)` and instructions to fill it, lines 255–257 | no verdict; no supporting observation |
| discernment | `TBD (discernment verdict)` and instructions to fill it, lines 258–260 | no verdict; no supporting observation |

Thus the count is **0/3 evidence-backed verdicts**, not 3/3. The allowed-verdict words in the
instructions at lines 248–250 are not assigned verdicts. **Repair:** put one allowed value on each
line and cite the specific observed receipt/diff that supports it; use the bounded verdict only as
the contract permits and with its missing test named.

### Low — the measurement heading is not the canonical heading spelling

The intended sections are all present, but draft line 126 is
`## Before -> after measurements` (ASCII `->`), whereas contract lines 109–110 name
**Before → after measurements** (Unicode arrow). Semantically this is the measurement section;
strictly, the exact canonical heading is absent. **Repair:** normalize the arrow to `→` so both
human and exact-heading consumers see the required section.

## Required-section presence and order

| Required order | Contract section | Draft location | Presence |
|---:|---|---:|---|
| 1 | Work performed | line 13 | present, exact heading |
| 2 | Landed changes | line 75 | present, exact heading |
| 3 | Before → after measurements | line 126 | intended section present and in order; heading uses `->` |
| 4 | Sources & frontier | line 190 | present, exact heading |
| 5 | Trend verdicts | line 246 | present, exact heading |
| 6 | SHONEN | line 262 | present, exact heading |

**No intended section is wholly missing and their relative order is correct.** The sole naming
exception is the exact `Before → after measurements` title noted above.

Work performed also opens correctly with two declared claims and their axes: C1/consistency and
C2/depth (draft lines 15–18).

## Work-item evidence-pointer audit

At the structural level, **6/6 top-level Work-performed bullets carry an `Evidence pointer` field
or explicit evidence paths**. It would therefore be inaccurate to report “no evidence pointers.”
At the finished-report level, every bullet still leaves material observed evidence unfilled:

| Work item | Pointer(s) present | Unfilled evidence called out by the draft |
|---|---|---|
| C1 repair, lines 20–29 | plan §C1 and named base/half-control receipt paths, lines 24–26 | control provenance and after-repair receipt/revision, lines 26–29 |
| C2 ladder, lines 30–39 | plan §C2 and wave-1 report directory, lines 36–37 | source/entry review, self-test and measured-revision bundle, lines 37–39 |
| Frontier/mistake, lines 40–46 | plan, lesson and census paths, lines 43–44 | committed close evidence, outputs and failing control, lines 44–46 |
| Assimilation, lines 47–58 | package report/rows/knowledge paths, lines 51–52 | assimilation and considerthese dispositions, lines 53–58 |
| Waves/review, lines 59–66 | plan and `w1-spec.json`, lines 64–65 | observed accounting and committed wave-evidence paths, lines 61–66 |
| Inherited/no-harm/scope, lines 67–73 | plan §Inherited state, lines 69–70 | no-harm disposition and tooling record, lines 70–73 |

So the calibrated answer is **yes for pointer-field presence, no for completed evidence content**.
The plan/draft pointers do not fill the explicitly deferred observations; draft lines 9–11 themselves
say that plans and draft paths are not after-measurements.

## SHONEN marker-rule audit

The draft has **four lines for the four boxes in `SHONEN.md`** (source boxes at lines 5, 7, 9 and
11; draft lines 269–272). All four use `[~]`; none uses `[x]`, so the named-non-author condition for
`[x]` is not triggered. Each `[~]` line carries an inherited evidence pointer. I opened at least
one cited target for every box in the reviewed checkout:

- Box 1: `.ufo/round-46/scouts/B2.md:44` and
  `corpus/knowledge/anatomy-and-compression.md:102-108` resolve.
- Box 2: `corpus/knowledge/cold-run-round11.md` resolves and records the cold run.
- Box 3: `corpus/lessons/round-8-aggregator-box3-coldrun.md` resolves; its lines 33–41 preserve
  the B1/B2 limits and `[~]` verdict rather than claiming an unconditional pass.
- Box 4: `PROVINCE.md` §Adjacent (lines 35–42) and
  `corpus/knowledge/sibling-overlap-census-round49.md` resolve.

Accordingly, **the `[x]`/`[~]`/`[ ]` allocation and resolvable-pointer rule is satisfied on the
evidence checked**. All four round-67 recheck fields are nevertheless TBD (draft lines 269–272);
those fields must not be represented as fresh rechecks or fresh non-author verification. The draft
explicitly preserves that distinction at lines 264–267.

## Residual risk and verification gaps

- This was a full read and contract audit of the named **draft**, not an audit of any separately
  filed final report at the fleet report path. A later, populated report must be reviewed on its
  own bytes.
- I did not rerun C1, C2, either census, append-only checks, or any wave accounting command. No
  conclusion here verifies or falsifies the landed claims themselves.
- The 74/71 TBD figures are lexical counts from a local Python read; section semantics, pointer
  fields, verdict absence, and marker allocation were judged from the full file, not inferred from
  grep output.
- Work-item pointer **presence** was audited exhaustively, but every work-item target was not
  re-opened. SHONEN pointer resolution was checked in the current checkout by opening the cited
  files; historical commands and old short-hash LOG references were not re-executed.
- Exact-heading consumer behavior was not tested. The ASCII-arrow item is therefore a concrete
  canonical-text mismatch and compatibility risk, not a claim about an uninspected parser.
