# CriticCalib

role: critic (leaf; advisory, not the canonical judge)
item: C2 — circularity, calibration-axis validity, and append-only discrimination

Axes: **calibration / consistency** (self-assessment fidelity, measurement honesty, provenance). Other axes are not assessed by this seat.

## Findings

1. **Fixable measurement defect: the frozen before headline contradicts its own five arms.** `plans/round-63.md:97-117` defines four failing content checks at `35d44b4b` and one passing prefix check, but demands `0 of 5`. The literal verdict vector is `[false, false, false, true, false]`, hence **1 of 5**, not 0. This is arithmetic derived from the frozen definitions, not an executed result from the new counter. Counting only newly repaired arms could yield zero, but that is a different metric and cannot silently replace the five-check sum.
   - Evidence command, run from the lane: `git ls-tree -r 35d44b4b -- .ufo/waves/round-62/w2/FalsifyC2HonestH1.md` → no output.
   - Evidence: `plans/round-63.md:111-117` explicitly says check 4 passes at the same revision where the headline is supposed to be zero.
   - Impact: calibration; manufacturing zero would repeat the self-assessment mismatch C2 claims to repair.
   - Smallest safe correction: append a named plan erratum stating raw baseline **1/5**, content baseline **0/4**, prefix **pass**; retain target **5/5**. Do not turn a true invariant arm false merely to obtain zero.

2. **The five measured checks are not the spot-check's five routed defects. A full score does not establish complete routing closure.** Compare `corpus/lessons/round-62-verifier-spotcheck.md:159-177` with `plans/round-63.md:97-109`:

   | Original routed requirement | What the counted predicate establishes |
   | --- | --- |
   | Commit/revert late report **and**, if committed, fold its H1 finding into the entry/Q57 or fix with a receipt | Path tracked only; no required learning/repair |
   | Correct receipt revision, entry size, **and false post-report child-commit claim** | Revision and size only; child-commit correction not counted |
   | Correct/re-probe Cursor rejection reason | Outside these five checks; plan openly reports it separately |
   | Name both interim reds **as fixed at tip** | Names result tokens and 36 of 38; naming alone need not establish final repair |
   | Keep SHONEN author/non-author boundary | Not counted; operator-owned, not a repair earned this round |
   | Preserve committed LOG text | Added invariant occupying one counted slot |

   - Evidence: spot-check `:161-169` requires semantic absorption of the late finding and all three citation corrections. `:173-175` requires fixed-at-tip wording, not just failure-token presence. Frozen check definitions above omit these conditions.
   - Strong counterexample **[INFERENCE; plan-level, not executed]**: track the late file, append the correct receipt token/size/no-harm tokens, preserve the base LOG prefix, but leave the H1 bound and false-child assertion uncorrected. All five stated checks can pass while two explicitly routed obligations remain open.
   - Impact: calibration; a five-check denominator must not masquerade as a five-defect closure denominator.
   - Smallest safe correction: call the headline five **repair checks**, and report every original §6 item/sub-item separately with committed evidence. Complete the omitted obligations rather than declaring them closed from this headline. Keep source freshness and SHONEN ownership separate.

3. **Post-defect authorship is legitimate regression measurement, not independent calibration evidence. Local independent evidence exposes exactly the missing dimension.** The non-author spot-check supplies an externally identified error set, so re-deriving and correcting those facts is not inherently circular. It becomes circular when passing a counter designed around those same known facts is treated as an independent test of the lane's ability to recognize new overreach.
   - Evidence: late finding `.ufo/waves/round-62/w2/FalsifyC2HonestH1.md:60-120` records that the lane's own `**not**` R-c wording and honest variants M-a/M-b/M-e/M-f/M-j fail the v2 successor, although its chosen honest fixture passes. This seat read that evidence; it did **not** re-run those old probes.
   - Evidence: `corpus/knowledge/erratum-absorption-round62.md:46-64` and `corpus/QUALITY.md:68` at inspection do not yet carry that H1-narrowness bound. Merely tracking the report cannot fix this mismatch.
   - An independently specified closure audit would trace every §6 obligation through the entry/Q57 and appended corrections, not only detect the file and expected tokens. A genuinely independent calibration evaluation would additionally use fresh honest/dishonest cases not used to design the counter, checking correct acceptance as well as rejection. The known H1 variants are regression cases now, not a held-out population.
   - Impact: calibration / discernment. This seat is lane-dispatched and cannot supply the required outside validation itself (`LEARNING.md:40-46`).
   - Smallest safe correction: claim an **in-sample, externally prompted reconciliation**, not a new general discrimination capability; carry the H1 bound and leave numeric scores unchanged absent independent transfer evidence.

4. **Committed-byte agreement is not receipt authenticity if the proposed counter lets both sides change together.** The plan extracts receipt values from the target revision and checks that the correction agrees. That is useful consistency checking, but the receipt and the correction are both lane-controlled inputs.
   - Evidence command: `git show 35d44b4b:.ufo/waves/round-62/C2-successor-measure.txt` includes the actual line:
     ```text
     receipt_rev=3f911504ce76d9ca186f297d6d4a9cd8ed77508a
     ```
   - Evidence command: `git show 35d44b4b:corpus/knowledge/erratum-absorption-round62.md | wc -l -w` → `64 1044`.
   - Evidence command: `git show 35d44b4b:.ufo/waves/round-62/noharm-tip.txt` includes:
     ```text
     Measured revision: 3e7aed9b61bbfd83e0c800213b6dfc6da6191f85
     FAIL  reg_gate    expected exit 0 in both columns, got base=0 tip=1
             tip: gate registry rows conformant 36 of 38 lane verifiers; phantom 0
     FAIL  corpus-idx  tip leaves new corpus file(s) unindexed: corpus/lessons/round-61-verifier-spotcheck.md
     Battery exit code: 124
     ```
   - Counterexample **[INFERENCE; not executed]**: replace the receipt's historical token or failure result and append a matching correction. Target-byte equality alone does not detect the co-change; a baseline-derived identity check would. Do not describe the historical battery as a successful complete run merely because its two named interim failures were later repaired.
   - Impact: calibration / false provenance.
   - Smallest safe correction: preserve/pin the two original receipt blobs against the frozen base, or explicitly report that the five checks prove consistency with supplied committed receipts, not independent authentication of them. Size checks may legitimately change when the entry gains a bound; that is not permission to rewrite the historical receipts.

5. **Append-only is a real safety property, but this arm is free on a no-op and weaker than the historical invariant. There is an actual local counterexample.** Prefix preservation can fail when an old byte is edited; it is not a vacuous predicate on all revisions. Nevertheless it is already true before any repair and cannot earn a newly closed defect. It also protects only the frozen base prefix, not every subsequently committed suffix.
   - Evidence commands and real outputs:
     ```text
     $ git show a745411c:LOG.md | wc -l
     2543
     $ git diff --numstat a745411c e53b6e5c -- LOG.md
     23	0	LOG.md
     $ git diff --unified=0 a745411c e53b6e5c -- LOG.md
     [single hunk header:] @@ -2543,0 +2544,23 @@
     $ git diff --numstat e6da78bb e424f2a4 -- LOG.md
     5	4	LOG.md
     $ git merge-base --is-ancestor e6da78bb e424f2a4
     [no output; successful]
     ```
   - The endpoint is a pure append after all 2,543 baseline lines, yet an intervening descendant transition rewrote four already-committed LOG lines. The full diff replaces the committed C1-before and C2-predicate bullets. This is also independently recorded in the spot-check `:45-52`.
   - The analogous r63 suffix rewrite is therefore a concrete behavioral class the frozen-base prefix arm cannot exclude, even if all final correction tokens are present. This is a demonstrated history/endpoint distinction, not a run of the proposed new counter.
   - Impact: calibration; claiming full append-only enforcement from endpoint preservation overstates the evidence.
   - Smallest safe correction: describe this arm as **frozen-prefix preservation** and count it as a no-harm guard, not a new repair. If full history-level append-only is claimed instead, check each relevant parent→child LOG transition, including newly committed corrections, and demonstrate a suffix-rewrite negative case. A pre-base violation cannot be retroactively repaired by preserving the base.

6. **No numeric calibration-axis move is supported by C2 alone; a bounded within-band consistency repair can still be real.** The axis is self-assessment fidelity, not paperwork volume (`AXES.md:15`); correcting false claims does address it. But a post-hoc finite closure checklist supplies neither an error rate over an independent population nor evidence of transfer to future assessments.
   - Evidence: `SCORECARD.md:17-22` defines bands by independent verification, not a fraction of known corrections. `:29`, `:36`, and `:369` retain the **owned consistency/calibration sub-axis at 10**. The separate older advisory calibration disposition at `:365` is **8.5**. `plans/round-63.md:5-9` calls calibration/consistency 8.5 the lowest owned axis; these labels must not be silently interchanged to create a score increase.
   - Recommendation, not admission: **numeric delta 0**. If all substantive corrections land, record a bounded reconciliation improvement with its command/revision and independently checked facts. Do not infer saturation, a band increase, or stronger future calibration from 5/5. Resolving the existing 10-versus-8.5 mapping is separate authority work, not something this seat changes.
   - Fixable versus non-admissible overclaim: arithmetic, missing correction obligations, and wording are fixable. Trading truthful arm results or historical provenance for a prettier headline is not a harmless measurement choice; the canonical judge should reject that framing rather than average it against the repairs.

## Artifacts

Proposed report-bound text (new text produced by this seat; not integrated):

```text
C2 measures four content checks and one frozen-LOG-prefix preservation guard
for the r62 spot-check. Its literal before vector is F,F,F,T,F: 1 of 5
(content 0 of 4; prefix preserved). Any after count is reported only after
measurement at the named committed revision. These are repair-check counts,
not five independent newly closed routed defects or an accuracy estimate.
Every original §6 item and sub-item has its own closure/disposition pointer.
The instrument was designed after those defects were known; success shows
bounded in-sample reconciliation, not unseen-case calibration, historical
receipt authentication, acceptance of honest repairs generally, or full
history-level append-only enforcement. No numeric axis-score increase follows.
```

Minimal semantic counterexample (analysis artifact, not executed code):

```text
Track the real late H1 report without folding its finding into the entry/Q57.
Append receipt_rev=3f911504ce76d9ca186f297d6d4a9cd8ed77508a,
the then-current entry line/word counts, and the measured no-harm tokens.
Preserve every byte of the frozen LOG prefix.
Leave the false post-report-child assertion without a named correction.
Result predicted from the five frozen definitions: 5/5 checks can coexist
with unclosed §6.1 and §6.2 obligations. This is not a measured gate result.
```

No production files changed. Only this report was written. No installs, git/jj mutations, new-counter execution, build, lint, or test suite runs were performed; the history counterexample used read-only git evidence. Suggested L1 checks after integration: raw baseline arm transcript; original-§6 semantic closure crosswalk; receipt-identity preservation; old-prefix edit and newly committed suffix-rewrite negative cases if history-level enforcement is claimed.

## Verdict

**ATTACKS** the `0 of 5 → 5 of 5` headline as written and any numeric/general-calibration inference. Not an admission decision. The smallest defensible outcome is a truthfully counted, explicitly bounded, within-band reconciliation with numeric delta 0. I would change my mind about the bounded closure after a named arithmetic erratum, committed evidence for every omitted §6 obligation, and a measured after transcript. I would change my mind about broader calibration only with independent fresh-case discrimination/recognition evidence and an unambiguous score-axis mapping; adding more known tokens or lane-dispatched attestations is insufficient.

Report: `.ufo/waves/round-63/w1/CriticCalib.md`
