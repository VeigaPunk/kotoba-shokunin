VERDICT: INCOMPLETE RECEIPT / DURABILITY PROBE — the receipt scanner and claimed tip receipts are not yet present, so no receipt-level pass can be certified.

Observed at inspection:
- `.ufo/waves/round-76/receipts/` contains only `census-before.txt`, `fetch-recheck.txt`, and `d4-selftests.txt`; there is no `receipt-revs.txt`, `r1-folded-render.txt`, `noharm-at-tip.txt`, or counter result receipt yet.
- `.ufo/waves/round-76/build/check_receipt_revs.sh` exists and documents the intended Q36/Q50 rule: each receipt must name a measured revision (full 40-hex token, or explicitly marked `<rev>` placeholder); it categorizes unqualified 40-hex tokens as weak.
- Current durable drafts are `build/scorecard-draft.md` and `build/entry-draft.md`; `build/log-draft.md` was not present at inspection. SCORECARD draft lines 4–6 explicitly say it asserts no tip measurement, and lines 10–11 use base revision `b7f13f4b39cbd43076a85568adca763a6f674e7a` for measured red results. These do not currently cite any new tip-result receipt.
- `receipts/d4-selftests.txt` explicitly names `tip: 4de12b61f75c73e3675ef0e422cc2be0f7da8960` (lines 3–4), so its revision identification is strong; its results are self-tests, not a claimed tip counter result.
- `receipts/census-before.txt` contains an explicit full tip `4de12b61f75c73e3675ef0e422cc2be0f7da8960` at line 73 in a `git show ... # tip HEAD` command and elsewhere names baseline; it is identifiable, though this is the base census receipt and its tip comparison context must not be mistaken for a new no-harm-at-tip result.
- `receipts/fetch-recheck.txt` is present, but I did not establish a complete measured-revision attribution for it in this probe; do not treat it as a tip measurement.

Inference: no receipt presently visible asserts a new frozen-counter tip result without naming its tip; instead, required tip evidence is absent. Once receipts land, run the existing scanner and compare each cited draft claim against the exact receipt filename and measured rev, rather than inferring durability from the scanner's token-only category.

Commands/exits: none run by this scout. The plan path supplied by the task, `PLANS/ROUND-76.MD`, was not found in the lane; this probe relied on the wave spec, scanner draft, current receipts listing, and SCORECARD draft. No tools installed; no scratch created; no git/jj mutation.