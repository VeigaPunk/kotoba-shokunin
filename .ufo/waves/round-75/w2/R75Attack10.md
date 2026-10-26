# R75Attack10 — attack on R75Facet10

## Verdict

**Not sustained as a material finding; its cited factual observations survive.** The report itself concedes that it identifies no current description making the alleged stale/category-confused claim. Its proposed control is generally sensible, but the presented evidence does not establish a concrete defect to correct. Treat this as an audit caution, not an actionable r75 finding.

## Independent evidence

Measured repository tip is `65a5c7a663249e0522cc49e4a148424200d9ddfe` (`65a5c7a`). Both cited files exist as committed blobs at that tip. `git show 65a5c7a:<path> | git hash-object --stdin` equals `git rev-parse 65a5c7a:<path>` for each:

- `corpus/knowledge/skill-eval-artefacts-round70.md`: `c103d829b4cf071f9d5f3bc53a4a730b1296b772`
- `corpus/lessons/round-74-verifier-spotcheck.md`: `9f3e7b33105fe17793b4465e8ff744ef587ad2cb`

The r70 entry confirms the report's facts: lines 1-6 list S209/S210 then S212/S213 as superseding citations; line 9 pins its `ground:` sweep to `7d51253f`; lines 76-80 limit scope to guides/reference implementation and disclaim native client execution, with the plugin as near-miss. The r74 lesson lines 46-64 describe C1 as `improved`; its evidence table marks counter outcomes and self-test as evidence-verified rather than remeasured. The baseline commit object `7d51253f` exists.

Counterevidence to a broad implication that the r70 entry is merely stale historical evidence: the committed r70 entry itself has a “Round 75 correction — equality wording” section (lines 84-88), and `corpus/lessons/round-75.md:5` records a source opened 2026-10-27 and the scoped candidate-admit/reject criteria. `SKILL.md:193` contains the live advice-level statement about the guides and comparator, rather than asserting current absence based on the r70 baseline. These do not prove that every description is correctly sourced, but they show current scoped work; no bad description/citation is identified in R75Facet10.

## Control assessment and limits

The suggested source-row/anchor/provenance/snapshot check is non-vacuous for provenance and byte identity, and the report appropriately says semantic entailment still needs review. However, its failure condition is hypothetical (“a description whose cited row resolves but whose located passage does not entail its wording”): no such description is cited. Thus the control cannot establish the report's proposed weakness absent a specific claim to test. The report's stated check was not independently run as a claim-level audit because it supplies no target description; safe read-only identity checks above were run.

No LSP device/server is available in this review context; no semantic references/definition/diagnostics results are claimed. No live fetch, source edits, or production changes.
