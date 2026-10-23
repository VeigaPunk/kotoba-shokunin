# ScribeEntry
role: scribe
item: Draft the compound-clause citation knowledge entry (depth G9 and correction-practice section)

## Findings

1. **Frozen G9 contract.** Evidence: `plans/round-63.md:51-68` — defines `g9_conjunct`, splits at `;` and the word `and` outside backticks, checks each clause with at least `MIN_CONTENT` content words against the cited line using A2's `fwd_need`, restricts G9 findings to clauses supported by the page, and names the frozen instance plus the four eligible fixture rows. The specified no-harm result is `eligible rows pass 4 of 4`; that is an acceptance criterion, not a result I ran.

2. **Depth provenance and baseline.** Evidence: `corpus/knowledge/erratum-absorption-round62.md:13-16,33-35,48` — names `e2f-compound-purpose-outside-citation` as an E2f survivor, says v31 closed five of six survivors, and retains G9 as an explicit bound. The depth draft therefore cites the frozen `verifiers/check_erratum_absorption.py` catalogue and v31/v32 counters, not S119.

3. **Observed guard wording.** Evidence: `verifiers/check_scoped_rules_v32.py:1061-1126` — the current readable file defines the requested split boundaries and rejects a clause only when the page supports it but the cited line does not. Its `content_words` and A2 helpers make the check lexical, with a three-distinct-content-word floor and the same forward-support threshold.

4. **Verification remains unclaimed.** Evidence: `verifiers/check_scoped_rules_v32.py:2647-2685` — in the version I read, the self-test still expected G9 to survive and printed `bound: G9 remains unimplemented`; I did not execute a gate. The draft labels v32's desired output as an acceptance target, not an observed result. This read may predate the L1's integration.

5. **Correction-source boundary.** Evidence: `plans/round-63.md:124-127` — S119 is planned as the primary correction/errata-practice source for transparent, appended, linked correction rather than in-place rewrite. I did not independently fetch S119; the integrated lesson/source row and quote must supply that provenance. The draft cites S119 only for correction practice.

6. **Touched surface and exclusions.** I wrote only this assigned report. I did not create or edit `corpus/knowledge/compound-clause-citation-round63.md`, production counters, source rows, snapshots, or any other lane file; no tests or gates were run.

## Artifacts

Verbatim proposed entry (draft only; not written to the product path):

```markdown
source: S119

## What it is

This entry records two separate practices. The depth half closes a known citation gap: an otherwise-supported Action sentence must not carry an unrelated compound clause that its cited line does not support. Its evidence is the frozen erratum catalogue and the v31/v32 counters, not S119. S119 is cited only for the correction-practice section below.

## The rule

### Compound clauses: depth (G9)

A clause the cited line does not support may not ride on a sentence it does support. Split the Action cell at semicolons (`;`) and the standalone word `and` (case-insensitive), but only outside backticked spans. For each resulting clause with at least three distinct content words, require the same forward-support threshold A2 uses against the cited line: at least `max(2, ceil(2n/3))` supported content words, where `n` is the clause's distinct content-word count and support is the existing exact-word/four-character-prefix match. If the page supports the clause but the cited line does not, reject it as supported outside the cited line. If the page does not support it, A2's page-containment check is responsible; G9 does not duplicate that finding.

The false-positive bound is deliberately narrow, not a population-wide error rate: G9 ignores clauses with fewer than three distinct content words and clauses not supported by the page. The frozen no-harm check is the four eligible rows (S900–S903), which must all pass; that finite fixture result does not establish universal precision.

### Correction practice (S119 only)

When correcting a prior record, append a transparent, linked correction rather than silently rewriting the earlier account. This source supports correction practice only; it is not evidence for the G9 rule or its measured behavior.

## Method provenance

G9 is a narrow extension of A2's citation-support check: it applies A2's existing forward-support threshold separately to each split clause, then reports only page-supported clauses that fail at the cited line. The v31 predecessor and the frozen erratum catalogue identify the named survivor; v32 is the successor whose self-test must demonstrate closure. The correction method is separately attributed to S119. The guard mutation and eligible-row checks are test controls, not source-prose entailment judgments.

## Limits

This is lexical support, not semantic entailment. It cannot determine whether words on the cited line are being used in a different predicate role; a clause can remain unsupported in meaning while passing because the line's words match. The splitter recognizes only `;` and `and` outside backticks, so other coordinators or punctuation (for example `but`, `or`, or a comma) do not create a separate clause for G9. The three-word/page-support restrictions and four eligible fixtures bound the exercised surface but do not prove a general false-positive rate. Reviewers still decide whether source prose entails an Action claim.

## Verification

Use the frozen catalogue and both successor counters:

- `python3 -B verifiers/check_erratum_absorption.py --self-test` — frozen survivor catalogue, including `e2f-compound-purpose-outside-citation`.
- `python3 -B verifiers/check_scoped_rules_v31.py --self-test` — do-nothing baseline; its recorded result is `survivors closed 5 of 6`.
- `python3 -B verifiers/check_scoped_rules_v32.py --self-test` — required target: `worlds reject 7 of 7; eligible rows pass 4 of 4`, `survivors closed 6 of 6`, and `must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes`, exit 0.
- `python3 -B verifiers/check_r63_routed_repairs.py --rev <rev>` — separate C2 acceptance target: `r62 routed defects closed 5 of 5`, exit 0.

These are verification instructions and frozen targets, not execution receipts from this seat.
```

## Verdict

PROPOSES — use this scoped draft when integrating the knowledge entry. I would change the wording if the final G9 implementation changes the frozen split/support boundary, if its eligible-row controls do not support the stated no-harm bound, or if the fetched S119 source does not substantiate the correction-practice sentence. No execution evidence is claimed here.