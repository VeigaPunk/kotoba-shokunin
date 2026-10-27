# A14CritHollowC2 — C2 token-dump attack

**Verdict: token-dump rejected; counter not hollow on this world.**

**Axes:** consistency (primary), calibration, operability.

Built scratch token-dump revision `90096e2bc41c4d51a2cccf7d0ab10b8527fd0b00` on base `b7f13f4b39cbd43076a85568adca763a6f674e7a`. It had both receipts present with the wrong measured revision (the base) and forged green/1022 claims; a correction paragraph that named no superseded M75-1 or Gate text; an empty R3 note; and a LOG closing line with no settlement facts. It did not include the R2/R3 LOG citations.

Exact scoring command:

```sh
python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_r75_routed_repairs.py --repo /fast/scratch/hyaku/kotoba-r76/A14CritHollowC2/world --rev 90096e2
```

Observed output: `r75 routed repairs closed 0 of 4`; exit **1**. R1 rejected missing M75-1 and verbatim superseded-text/Gate excerpts, missing 1,022 assertion, lines 4–18 and spot-check citation; R1 receipt also lacked the stripped-render number, convention and line range. R2 re-ran both corpus gates at the wrong base revision and observed exit 1/DRIFT, and rejected the missing LOG citation. R3 rejected the empty note for missing the seat, excerpt, absent report path and counts, and missing LOG citation. R4 rejected the factless closing line. Thus none of the four repairs passed on this forged world.

**Counterexample / evidence:** the strongest attempted token dump was rejected by content checks and by recomputation/re-execution rather than filename presence. The counter's R2 behavior is particularly effective against a forged green receipt: it checks the committed measured revision in a sandbox. No fix is needed to reject this world.

**Smallest safe correction / follow-up:** none for this attack. One contract alignment point for the L1: the frozen plan says the receipt recomputes and prints 1022; the counter additionally requires the stripped variant 1021 and names the clip-chomping convention and frontmatter lines 4–18. These extra checks are defensible provenance for the reported render convention, but should be documented in the frozen contract/receipt label or removed if not intended. This is not a hollowness finding.

Scratch clone and fixture were removed. No tools installed.
