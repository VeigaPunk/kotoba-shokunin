# A16 — C2 headline critique (Q26)

**Verdict:** “R1–R4 closed” is not yet justified by the frozen counter contract as written. It can demonstrate required artifacts/content are present, but several routed requirements are stronger than presence and need explicit cross-checks. Counter implementation is not present yet, so this is a specification-level finding, not a claim about its eventual behavior.

## Counterexample / evidence

The committed r75 spot-check §6 enumerates exactly R1–R4 (no R5): `corpus/lessons/round-75-verifier-spotcheck.md` lines 77–80.

- **R1 scope loss:** The routed text requires correcting M75-1 and the Gate reject candidate, fixing the folded-scalar counting method, and “re-derive any plan/claim that consumed the ‘materially shorter’ assertion.” The planned C2 conjunct checks the correction paragraph and a 1022 receipt, but does not say it verifies the re-derivation. Thus a correction and receipt could be present while a downstream claim still consumes the false assertion. Also, R1 is a historical measurement “at tip” in the r75 spot-check, whereas the plan says to recompute from “the measured revision” without identifying it. The counter must use the r75 tip `b7f13f4b39cbd43076a85568adca763a6f674e7a`, not silently substitute the judged r76 revision; otherwise it measures a different proposition and may be affected by C1's description edit. My quick raw-line character count is not a YAML-folded render and is not evidence for/against 1022.
- **R2 authenticity:** The routed defect is missing *actual* post-landing green corpus-gate evidence at the final r75 tip. The plan requires a receipt naming a tip and containing stdout/exit codes. A correctly formatted but fabricated green receipt with the right revision can satisfy those textual conditions unless the counter reruns the two gates at that revision or otherwise verifies their output. The listed must-fail arm (“receipt without the tip rev”) does not catch this.
- **R3 reconciliation:** The routed defect says the results entry names an absent report (63/64) and asks to recover the bytes or record the phantom “so the results file reconciles with the wave dir.” Current local evidence: `w2-results.json` names R75Attack28 and the directory has 63 `.md` reports. A note that merely contains an excerpt is not reconciliation; counter should compare the excerpt to the actual results entry and confirm report absence/count at the referenced revision.
- **R4 correctness:** The plan asks for a closing line with 64 seats, 0 dead, 63/64 reports, and the phantom disposition. Presence/order checks alone admit a line with incorrect numbers. Counter should derive these values from the r75 results and report directory (or explicitly narrow the claim to a recorded assertion, not closure).

## Impacted axes

Consistency/calibration (headline claims stronger than evidence predicate); freshness (historical r75 premise must not be replaced by r76 state); operability (counter should deterministically validate the receipt and reconciliation); coverage (R1's downstream re-derivation is omitted from the specified checks).

## Smallest safe correction

Before freezing the counter, pin R1's measurement to the r75 base revision; add explicit checks for R1's downstream re-derivation, R2's gate results at the claimed revision, R3's excerpt/count against `w2-results.json` and the wave directory, and R4's reported values against those same bytes. If these checks are intentionally outside the counter, narrow the headline from “closed” to “four repair artifacts present” and leave closure to a named independent adjudication. The counter file `verifiers/check_r75_routed_repairs.py` did not exist when inspected; no implementation verdict is made.