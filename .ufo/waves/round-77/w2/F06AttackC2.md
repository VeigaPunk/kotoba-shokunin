# F06AttackC2 — C2 R1 truth and correction semantics

Axes attacked: **consistency** (primary), calibration, operability. Scope: frozen C2 only, especially R1. No lane source files or git/jj state changed; no tools installed.

## Landed-state blocker

The requested landed tip is not present in the lane checkout: read-only `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse HEAD` returned `6523aced1ee0ebe07dca996213bdc645a6acbd1e`, the plan's frozen base, and status reported zero staged/unstaged changes with round-77 artifacts untracked. Thus there is no committed R1 correction to truth-test. The W1 receipt `receipts/E05R3R4Repair.c2-after-r3r4.txt` itself records only a scratch fixture `65414b283a4b046332e474a3e407b5a8a5dce9ac`, `2 of 4`, exit 1; it explicitly leaves R1/R2 open. These are not landed claim data.

## Frozen C2 counter at actual HEAD

Verified counter digest:
`sha256sum /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_r75_routed_repairs.py` → `989203c40e1aab55fc14ee1d444dd4fa8b49fe01144b2dcdeaa6a27fa39f4a63` (matches plan pin).

Exact command:
`python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_r75_routed_repairs.py --repo /home/vgpnk/Projects/shokunin/kotoba-shokunin --work /fast/scratch/hyaku/kotoba-r77/F06AttackC2/work --rev 6523aced1ee0ebe07dca996213bdc645a6acbd1e`

Output: `r75 routed repairs closed 0 of 4`; R1, R2, R3, R4 all open. Process exit: **1**. This is base evidence only and does not verify C2 at a final tip.

## R1 semantics attack

Frozen contract from round-76 §C2 R1 and C2 counter docstring: appended correction to `corpus/lessons/round-75.md` names superseded M75-1 text and Gate reject candidate, asserts the folded-render 1,022 value/lines 4–18, cites spotcheck; separate committed receipt recomputes those values at its named revision.

Counter implementation (docstring and `r1_correction`/`r1_receipt`, lines 20–26 and 286–382 of `verifiers/check_r75_routed_repairs.py`) bases correction semantics on append-vs-base and string/window/token checks, while receipt number is recomputed from the named committed revision. This is a deliberate limited evidence gate, not proof that the correction accurately explains the historical error. In particular it checks that the appended correction *asserts* 1022 and quotes named strings; semantic truth must come from the actual underlying revision and source evidence, not keyword presence. The W1 E05 report states R1 is unlanded, so no changed correction text could be reopened here. No claim is verified by draft or scratch fixture.

Smallest safe correction if landed correction contradicts the historical bytes: replace only the false sentence with a correction that quotes the superseded text and reports the recomputed clip-preserving measurement for the pinned R75_TIP, preserving the frozen target and receipt. This improves consistency/calibration without harm to other axes. Do not alter counter predicates or rewrite the frozen claim during this wave.

## Counter weakness observed in supporting evidence

E05's own report documents an R3 excerpt mutation: removal of the long verbatim excerpt while retaining required report-path token still leaves R3 closed because the path token is itself a ≥20-character substring of the output. Receipt `E05R3R4Repair.c2-control-paraphrase-only.txt` records `R3: closed` in that mutation world. This is outside my assigned R1 focus, but it means C2's R3 excerpt check is not an independent falsifiable condition. The safe future correction is a new pre-data counter revision excluding windows that overlap the required path token (or requiring a distinct excerpt); it must not be patched into frozen r77 bytes. The observed mutation does not itself refute R1.

## Verdict

R1 truth/correction semantics remain **unverified** because the claimed r77 data is absent from committed HEAD; actual C2 base run fails as expected. Counter pin matches. Do not accept C2 as landed or call the R1 correction verified until the claim commit exists and the frozen counter is run at that exact revision. R3 excerpt-arm weakness should be tracked for a later counter version.

VERDICT: BLOCKED — current lane HEAD is the r77 base; C2 reports 0 of 4 (exit 1), and no landed R1 correction is available to attack.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w2/F06AttackC2.md