# CriticC1Bound

role: UFO-FSD critic; advisory, not a canonical judgment or admission
item: C1 as a depth move versus fixture-fitting; round 63, wave 1

Axes: **depth** (assigned); **calibration/consistency** only where the measured scope is overstated. No other axis move is assessed.

## Findings

1. **(a) G9 adds a real, bounded distinction beyond G7: clause-local citation support.**
   Evidence: `verifiers/check_scoped_rules_v31.py:1046-1058,1061-1088`; reviewed v32 `:1061-1126,1129-1158`; frozen declaration `plans/round-63.md:51-75`.
   G7 asks whether a backticked identifier occurs anywhere in the raw cited line **or page**. An ordinary-prose addition with no identifier cannot fail it. Global A2 lets a long supported sentence subsidize unsupported words in its tail. G9 partitions at `;`/case-insensitive standalone `and` outside backticks and applies the existing `ceil(2|W|/3)` threshold separately to each clause with at least three content words.
   For the frozen `secretly uploads files` tail, the whole cell has 7 supported words of 10 (need 7), but that tail has 0 of 3 (need 2). G9 can distinguish those inputs without a fixture-id or exact-phrase lookup. This is more than relabeling G7, but remains lexical discrimination, not source entailment.
   Smallest safe correction: describe the capability as **coordinated-clause lexical support against the cited line**, with its minimum-size and delimiter bounds. Do not describe it as general compound-purpose understanding.

2. **(b) The strongest fixture-fitting argument concerns the chosen universe, not a fabricated numerator.**
   Evidence: `verifiers/check_erratum_absorption.py:159-164,212-229`; `verifiers/check_scoped_rules_v31.py:2554-2586`; reviewed v32 `:2624-2656,2681-2691`; `plans/round-63.md:60-75`.
   The six ids were already frozen in r62; r63 did **not** invent a new denominator after measuring. V32 scores the actual six attacks, sums actual before/after reasons, asserts all six rejects, and adds an actual guard-disabled rescore. These are meaningful defenses against label-only credit. I found no basis to call the intended `6 of 6` arithmetic dishonest.
   The strongest fixture-fitting objection is to treating *complete repair of this already-visible synthetic catalogue* as saturation; the frozen plan itself does not claim saturation. The remaining attack and the positive fixture text are known before rule design. Four inherited positives are not a held-out authoring population: their cited action lines reproduce their Action cells (`v31:2209-2241`). The G9 kill arm establishes causal dependence on this guard, not generalization beyond its training witness.
   The r62 spot-check verified **measurement**, not class closure: `corpus/lessons/round-62-verifier-spotcheck.md:66-91` independently derives `absorbed 2 of 5; surviving 6` from ten committed attacks. Its depth rationale is the new measured matrix (`:116`), not proof that the successor closes every represented erratum class.
   Smallest safe correction: retain the honest six-instance counter, but label `6 of 6` **all six frozen survivor instances**, never all G9/E2f cases, all errata, or semantic saturation.

3. **(c) A one-word deletion supplies a sharp later falsifier of any class-closure reading. A longer variant defeats the minimum-size defense too.**
   Evidence: original complete input at `verifiers/check_erratum_absorption.py:221-227`; `v31:1008-1043` defines the lexical sets/thresholds; reviewed v32 `:1116-1125` skips clauses below `MIN_CONTENT` and accepts each qualifying clause at the existing forward fraction. Exact proposed inputs are in Artifacts.
   **[INFERENCE: static trace, not an executed v32 result]** Delete only `secretly` from the frozen attack. `uploads files` has two content words, so G9 skips it. Whole-cell A2 shares 7 of 9 words (need 6), reverse coverage is 7 of 7 (need 3), all words occur on the original page, and G7 has no identifier to reject. The predicted reason list is `[]` although the cited sentence still does not assert uploading.
   **[INFERENCE: static trace]** Use the qualifying tail `uploads project files using glob syntax`. It has six content words; four (`project`, `using`, `glob`, `syntax`) match the cited line, meeting its threshold of four. The full cell still has the same nine distinct words. This tail is not skipped, yet the predicted result remains `[]` for an unsupported uploading relation.
   **Delivered empirical cross-checks (not executed by this seat):** `RevClaimC1.md` under this report's directory records the short-tail admission (Finding 3), and its vocabulary-disjoint `silently broadcasts telemetry` witness rejects with the actual G9 diagnostic (Artifacts), supporting generic rather than exact-string behavior. Finding 4 (`:74-87`) additionally measures the longer tail under **both** the original frozen page and a fuller uploading-sentence page: 4/6 line coverage meets need 4, `g9_conjunct` returns `[]`, and `action_conjunct` admits. Thus the original-page overlap witness now has an empirical peer receipt, not only my static derivation. This is a semantic boundary inside the declared lexical-support contract, not a failure of the narrow six-instance predicate. The peer's public-self-test transcript also records the planned three lines and exit 0 at sha `8371f707…`; the L1 still owns the committed receipt.
   A later round observing either `action_conjunct(...) == []` while the headline remains `survivors closed 6 of 6` would falsify **exhaustive G9/semantic closure**, not falsify the six-instance datum. Conversely, admission of the unchanged frozen original with G9 enabled would directly falsify C1's actual narrow claim.
   Impact: depth/generalization and calibration if the headline is broadened. These traces do not demonstrate a new false rejection or harm to an existing positive.
   Smallest safe correction: publish these boundaries and preserve the frozen catalogue. If pursuing broader closure later, add independent negative/positive pairs prospectively; do not silently replace the original arm or lower its target. Changing `MIN_CONTENT` alone cannot fix the six-word overlap witness.

4. **The strongest already-measured local warning is that a closed synthetic instance need not close its published counterpart.**
   Evidence: `corpus/knowledge/erratum-absorption-round62.md:54-64` expressly leaves entailment to reviewer judgment and records bounded E2c/G7 closure. The inherited receipt in `.ufo/waves/round-62/w2/FalsifyE2fPair.md:84-104` records the published S103 event as accepted by v31 while the synthetic missing-identifier event rejects. The same report `:22-35` explains that these are different inputs, not renamed copies.
   Independent source inspection here: `.ufo/waves/round-60/snapshots/S103.page:194` states conditional path scoping; `:427,599` contain `InstructionsLoaded` elsewhere on the page. V32 retains G7's whole-page occurrence check (`:1046-1058`). A perfect score over the synthetic pair therefore cannot erase the earlier published-event limitation. The inherited supported-abbreviation false rejection is also already recorded at `.ufo/waves/round-62/w2/FalsifyV31G7TooStrong.md:14-71`; no rerun was needed or performed.
   These are inherited bounds, not newly introduced G9 regressions or grounds to expand this seat into a G7 rewrite. Their relevance is that `6 of 6` cannot safely mean “the formerly open semantic classes are now solved” or establish universal no-harm.
   Smallest safe correction: carry the r62 Limits forward alongside the new exact-instance closure. Do not overwrite the historical `5 of 6` receipt or imply G9 cured G7/E2c.

5. **(d) Should the numeric depth score move? No: recommend holding 9, while allowing a bounded technical-depth improvement to be considered.**
   Evidence: `SCORECARD.md:17-22` defines 9 as machine-checked/external audit and 10 as repeated non-author verification in the opposite direction; `:36` already holds depth 9 and separates v31 from r62's counted predicate. Canonical `AXES.md:11,43-55` permits technical improvement without forcing a scalar increase.
   A generic clause guard plus an asserted kill arm improves verifiable technical detail relative to v31, if the L1's committed receipt establishes the planned result. It is not merely an exact-string patch. But replaying a fully visible six-instance set and its four familiar positives supplies no new independent, repeated non-author verification of the broadened semantic surface. Neither `6/6` nor this lane-dispatched critique earns a higher band.
   This is a **bound/measurement-scope issue**, not an established failure of C1's frozen predicate. If broader class closure or saturation is asserted, it is unsupported; if a future probe finds supported actions newly rejected and the restriction is deliberately retained, that is a tradeoff for the canonical judge, not a Pareto improvement this critic can approve.
   Smallest safe correction: retain score 9; record the bounded clause-check improvement separately from instance completion and semantic coverage. No admission, rejection, score mutation, or canonical Rust judgment is issued here.

## Artifacts

Verbatim proposed later-round vectors; **not executed** in this seat. All use the frozen fixture's original cited line/page. Expected acceptance below is inference from the reviewed implementation, not a test receipt.

```python
lines = ["The configuration stores project rules using glob syntax."]
page_text = (
    "The configuration stores project rules using glob syntax.\n\n"
    "## Unrelated section\nThe agent secretly uploads files."
)
short_tail = (
    "The configuration stores project rules using glob syntax "
    "and uploads files."
)
qualifying_tail = (
    "The configuration stores project rules using glob syntax "
    "and uploads project files using glob syntax."
)
# Later observation to record, on a revision-pinned /tmp copy:
# action_conjunct(lines, short_tail, 1, page_text)
# action_conjunct(lines, qualifying_tail, 1, page_text)
# Static prediction for each: []
```

Verbatim proposed reporting language:

```text
The successor closes all six frozen r62 survivor instances. Its new G9 arm
checks cited-line lexical support for clauses split at semicolons or standalone
“and” outside backticks, when a clause has at least three content words.
This is not semantic entailment or exhaustive G9/E2f closure. The r62 G7/E2c
limitations remain. Depth score held at 9.
```

Read-only digest command exercised from the lane directory:

```sh
sha256sum verifiers/check_scoped_rules_v31.py verifiers/check_scoped_rules_v32.py
```

Real output at the final digest observation:

```text
a07c2269ea077e4866827e3fae907c45aea7c960bbe5f56b21210a0cecea3858  verifiers/check_scoped_rules_v31.py
8371f707c571b74f6e3ec072690c771342fdd078b220c6ec3c617c6b18f21f28  verifiers/check_scoped_rules_v32.py
```

The cited v32 functions/self-test were read as working-tree snapshot `E8A9`; it changed during this build wave. This is not a committed after-measurement or a claim that its public self-test passed. No gate, mutation probe, build, lint, formatter, network fetch, alternate runtime, or judge was executed. No tools were installed or updated. Only this report was written in the lane.

## Verdict

**ATTACKS** the inference from `6 of 6` to semantic closure, saturation, or a numeric depth increase; does not attack the legitimacy of the bounded generic guard or the computed six-instance numerator.

To change my mind about a higher score: independently selected unsupported compound claims and supported paraphrases, committed before results, checked in both directions by repeated non-author review, with explicit scope and preserved inherited bounds. For C1's narrow completion alone, the L1 still needs its committed public-self-test receipt including the real G9-disabled flip; this seat did not run it. No blocker remains for this assigned critique.
