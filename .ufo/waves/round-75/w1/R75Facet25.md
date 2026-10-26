# R75Facet25 — calibration/control weakness

## Finding
The strongest distinct candidate is the broadening risk in the r74 C1 presentation: its measurements establish source admission, pinned snapshot identity, and presence of six body-craft rows, but those alone do not establish that the descriptions' factual claims are supported by those source pages. The spot-check explicitly distinguishes this: page fidelity is a reviewer judgement (round-74-verifier-spotcheck.md:58), while the counter result is evidence-verified only (lines 60–64). This distinction is useful for an r75 description audit: do not use row coverage or a successful mechanical counter as a proxy for sourced depth/calibration.

## Observed evidence
- `corpus/lessons/round-74-verifier-spotcheck.md:58` records the page-fidelity review as a judgment, with ~44 line pointers and a reported result of 0 overreach / 0 unsupported. This is a bounded claim about the reviewed entry and snapshots, not an automatic consequence of the counter.
- `corpus/lessons/round-74-verifier-spotcheck.md:60-64` reports the counter's 0/3→3/3 and 250-assertion self-test as evidence-verified, then labels coverage improved. The explicit boundary prevents conflating countability with fidelity.
- `corpus/QUALITY.md:36-37` requires a content guard that changes on a falsified-content mutant (Q25), and each headline clause be activated by counter output or a guard that changes when falsified (Q26). This offers a concrete falsifiability standard.
- `corpus/QUALITY.md:34` (Q23) separately requires located authority quotes and a sweep of other authorities for attributed rules; it is directly relevant when audit prose attributes requirements to an external guide.
- `corpus/knowledge/skill-eval-artefacts-round70.md:76-80` carefully bounds scope: it says no client is known to natively run the artefact and identifies the documented Claude plugin as an opt-in near-miss. That is good calibration precedent, not evidence that an r75 audit candidate has been validated.

## Concrete control
For each proposed description-audit claim, split the headline into factual clauses, then make a small claim-to-source table: exact description phrase; source snapshot and exact line/quote; whether the quote supports the clause or merely resembles it; scope/hedge retained. Add a falsification arm by deleting or changing the cited description phrase and require the content guard's output to change (Q25); for vendor-rule attributions, quote the authority and record the bounded authority sweep (Q23). Keep any judgement-only rating distinct from mechanically counted output, as r74 lines 58 and 60–64 do.

## Limits / confidence
High confidence in the distinction and the control criteria above: they are stated in committed lesson/QUALITY bytes. This is not a fresh audit of all candidate descriptions or the referenced source pages. The r74 plan is historical by task specification and is not treated as a frozen r75 claim. No sources were live-fetched and no unobserved counter behavior is asserted.
