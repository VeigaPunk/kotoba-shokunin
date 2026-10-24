---
author: kotoba L1 (round 66, hyaku run 5)
date: 2026-10-24
round: 66
lane: kotoba
---

# Round 66 — lesson (kotoba, hyaku run 5)

## Gate

- **S122 — Software Citation Principles** (Smith, Katz, Niemeyer & FORCE11 Software Citation Working Group, 2016), https://force11.org/info/software-citation-principles-published-2016/ — opened 2026-10-24 from the primary published-principles page; PeerJ Computer Science 2:e86, DOI 10.7717/peerj-cs.86. The located quote from §6.7, “Unique identification,” is: “a commit reference together with a repository URL is not recommended for the purposes of software citation” (17 words). The excerpt and context are preserved at `.ufo/waves/round-66/snapshots/S122-excerpt.txt`. This supports the bounded distinction in the C2 knowledge entry: the local integrity gate resolves an object's repository context; it does not claim that a raw commit identifier is a durable citation. S122 enters as `mined`, used by `corpus/knowledge/fleet-commit-resolution-round66.md`.
- Candidate search: one candidate identified, one screened, one included (S122), none excluded; the complete bounded search note is appended in `corpus/SOURCES.md` under the round-66 entry. No other source row changed.
- **Spot-check:** this L1 seat has no independent non-author reviewer; no round-66 admit/reject spot-check is claimed. The r65 non-author verifier spot-check was read and its D1–D3 routes are carried here.

## Mistakes

- **M102 — class: foreign-repository commit misclassified as unresolved.** Evidence: `.ufo/waves/round-66/controls/C2-before.txt` records the exact r66 base gate's three unresolved tokens, including the closure-authored fleet report reference; the same gate reported four unindexed closure spot-check files and stale count pins. Captured-by: `none` — the old resolver queried only the lane object database, and no QUALITY criterion named the allowed repository set or distinguished a quoted code-span example from a live reference. Fix: resolve lane-first then fleet-root, exclude a complete matching code span from live citation counts, index the four closure-authored r62–r65 spot-check lessons, and re-record the observed baseline only after the new corpus entries land. Shown able to fail: the frozen r66 counter gives the pinned base `0 of 2`; its self-test's no-fleet-hop world fails D2, while the honest fixture passes; evidence `.ufo/waves/round-66/controls/C2-counter-selftest.txt` and the round-66 final receipts.

## Status changes

- S122: new row written directly as `mined`; `corpus/knowledge/fleet-commit-resolution-round66.md` cites it in the same round. No existing row's `status`, `recheck` or `used-by` changed.

## Evidence pins

- The claim freeze and do-nothing controls are in `plans/round-66.md` and `.ufo/waves/round-66/controls/`.
- C1's G9 witness and coupled-floor self-test are measured in `.ufo/waves/round-66/receipts/C1-measure.txt`; its mutation-kill outcomes are recorded in `.ufo/waves/round-66/receipts/C1-kill.txt`.
- C2's integrity-gate and routed-repair results are recorded in `.ufo/waves/round-66/receipts/C2-integrity-after.txt` and `.ufo/waves/round-66/receipts/C2-routed-after.txt`.
