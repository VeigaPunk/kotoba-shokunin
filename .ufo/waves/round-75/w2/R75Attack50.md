---
seat: R75Attack50
round: 75
mode: independent falsification (read-only lane evidence)
measured-at: 2026-10-27
measured-rev: 65a5c7a663249e0522cc49e4a148424200d9ddfe
---

# R75Attack50 — attack on R75Facet50

## Verdict

**Finding survives in its central, actionable claim; narrow its evidentiary wording.** The current threshold counter does not evaluate the opencode “Past the threshold” cell or its vendor-code citations, and it reports the row backed despite that cell’s code assertions. The report’s gate-blindness and version-digit control findings are directly supported by source inspection and a run at the pinned revision. I cannot independently re-derive the two upstream implementations from committed source bytes in this lane; the report itself documents that limitation, so the stronger claim that both trees actually render the entire string remains historical report evidence rather than independently reproduced fact here.

## Independent checks

- Reopened `SKILL.md:176` at measured revision. The row contains threshold `1-1024` and the claim “both shipped trees print the whole string into `<available_skills>`,” citing `skill/index.ts:332` and `skill/instructions.ts:21` without repository/package roots.
- Reopened `.ufo/waves/round-54/build/Srcopencode.md:25-26,54-55`. It records the v1.19.4 and v2.1.3 source paths, line descriptions, fetch URLs and digests, but is a report, not the source bytes. Thus it corroborates provenance and the historical reading, not an independently inspectable source-line proof. No live fetch was performed.
- Reopened `verifiers/check_description_thresholds.py:266-330`: `judge()` takes the number tokens from `sr[1]`, checks the action at `sr[3]`, and never reads `sr[2]` (the asserted behavior/citation cell). The counter consequently cannot test the claim or citation in that cell.
- Ran the stated safe bounded control at the measured revision: `python3 -B verifiers/check_description_thresholds.py --rev 65a5c7a663249e0522cc49e4a148424200d9ddfe` → each of seven clients `BACKED`; `description thresholds backed 7 of 7 clients`; exit 0.
- Reopened `verify_skill_checklist.py:1665-1685`: citation resolution evaluates only extracted repo-rooted citation tokens and returns N/A when none are present. The bare upstream basenames in this row are outside that check’s supported roots; it is not a control for these citations.
- Confirmed repository HEAD equals the report’s measured revision. Working tree status reports five untracked paths (the round-75 evidence directory); no source changes were made.

## Attack assessment

The core control weakness is materially actionable: the existing counter’s green result is not evidence that the opencode claim or citations are valid. The report proposes specific corruption probes (wrong line, nonexistent path, removed threshold, version-only numerals) and records prior sandbox outcomes; I did not repeat those mutations because they are not needed to establish the directly inspectable blind spot and this seat’s bounded check is the existing pinned-revision invocation. Its cited code-root ambiguity is also plausible from the historical paths: v1 lives under `packages/opencode`, v2 under `packages/core`; the row names neither. Exact upstream line behavior remains unverified in this attack and should not be promoted from the committed round-54 prose to a fresh source observation.

No duplicate or scope defect found in the central finding. The facet’s adjacent host-install discrepancy is explicitly marked contextual, not counted as its object; I did not treat it as evidence for or against the targeted row. No production/lane edits, live fetches, or scratch mutation were performed.
