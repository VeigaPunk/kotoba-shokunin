# Kb82R02Checklist — independent checklist root-cause recon

Axes: freshness (exact receipt/source provenance), operability (hermetic selftest without weakening the live gate).

## Observed evidence

Named before revision: `47dbe8781657de563ff867caca6244d28e3db504`, as recorded in both round-82 before receipts. No checks rerun, no production after-values scored, no patch or production mutation. Read-only filesystem observations and SHA-256s are captured in `build/Kb82R02Checklist-evidence.json`. Source hashes identify inspected working-tree bytes; I did not independently bind them to Git blobs at the named revision.

- `receipts/before-checklist-selftest.txt:1-6`: command `python3 -B verifiers/verify_skill_checklist.py --self-test`; exact summary `1 failure(s) over 1863 assertions`, command-owned `exit=1`. Its sole failing arm is `governance: live round-65 corrections land, errata-excused`.
- `receipts/before-checklist.txt:65-78`: public JSON gate `governance.citation_resolves` is FAIL, evaluated 1363; 10 other checks PASS, command-owned `exit=1`. It reports the same four unresolved subject occurrences as the selftest receipt.
- Semantic tooling unavailable: `read xd://lsp` returned `No such tool`. The following trace is literal source inspection, not LSP reference/definition proof.

## Source trace and root cause — high confidence

All verifier references below are in `verifiers/verify_skill_checklist.py`.

1. `main`, lines 2706-2709, dispatches `--self-test` directly to `self_test`.
2. Governance fixture tests initially use an isolated `gov_repo` created by `TemporaryDirectory`, lines 2375-2378. Correction fixture coverage already exists at 2460-2514.
3. Inside that fixture block, lines 2521-2523 switch the repository argument to `live_repo = Path(__file__).resolve().parent.parent` and pass global `GOVERNANCE_CORRECTIONS`. The still-indented temporary-directory scope does not make that call hermetic.
4. `check_governance_citations`, lines 1766-1785, resolves the supplied repo and reads its actual `LOG.md` and `SCORECARD.md` (`GOVERNANCE_FILES`, line 394). Thus the selftest consumes evolving governance content beside the verifier, not the fixture files and not a revision-pinned tree.
5. `citation_subjects`, lines 1624-1661, extracts every qualifying backticked word; same-line quoted meta-findings and schematic paths are excluded. It does not deduplicate occurrences. `strip_token_dressing`, 1079-1084, accepts only a numeric line or numeric range suffix, not comma-separated line numbers.
6. `errata_problems` and `correction_problems`, 1688-1749, validate narrowly pinned exceptions. The resolver removes only those exact subjects, then tests every remaining subject via `citation_resolve`, 1807-1812. Ordinary slash-bearing tokens reach `safe_resolve`, 1537-1539 and 947-966, which checks filesystem existence under the repo, not PATH.
7. The assertion at 2524-2527 requires overall PASS plus two excused absences and four excused corrections. The saved failure already has both expected exception counts; unrelated new unresolved subjects alone invalidate overall PASS. This is test isolation debt, not evidence that the four historical correction rows stopped working.
8. A second live dependency remains at 2531-2542: dropping LOG.md:2678's erratum or lowering its horizon is also tested against `live_repo`. It is not the reported failing arm, but isolating only the first call would leave selftest hermeticity incomplete.

The public caller deliberately retains the live behavior: `main` enables governance when the checked skill is `repo/SKILL.md` (2711-2716) and calls the same resolver with global corrections at 2795-2798. Repairing the selftest must not remove that public route or soften its unresolved-subject predicate.

## Exact four stale subject occurrences

These are **four occurrences, three unique tokens**; they are not the four historical `GOVERNANCE_CORRECTIONS` rows.

| Subject | Exact token | Observed explanation |
|---|---|---|
| SCORECARD.md:480 | `.ufo/wapes` | Unquoted historical R3 old-path mention remains a live extracted subject. Old path absent; `.ufo/waves/round-81/dispositions/wapes.txt` exists. The arrow/prose correction does not itself register a governance exception. |
| SCORECARD.md:482 | `corpus/lessons/round-80-verifier-spotcheck.md:30,37` | Lesson exists; literal comma-suffix path does not. `strip_token_dressing` leaves `:30,37` intact. Lesson lines 30 and 37 actually carry the cited non-author judgment and depth verdict. This is an unsupported citation spelling, not missing lesson content. |
| SCORECARD.md:484, first occurrence | `.ufo/reports/round-81/kotoba.md` | Lane-relative target absent; fleet-relative `../.ufo/reports/round-81/kotoba.md` exists. First occurrence appears in the described tip no-harm battery command. |
| SCORECARD.md:484, second occurrence | `.ufo/reports/round-81/kotoba.md` | Same incorrect lane-relative token repeated in the wider-set command; each occurrence is independently extracted and reported. |

The saved detail has no `(+N more)` suffix; resolver lines 1813-1817 would append one after more than four failures. The receipt therefore names exactly four reported failures, rather than merely truncating a larger set.

## Inference and remaining unknowns

- High-confidence inference: replacing all live-dependent selftest calls with isolated pinned fixtures can address C2 without making the public live citation failure green. Existing fixture cases explicitly exercise missing registration, pin drift, dead replacement, restored stale token and unrelated dead subject; retain them and the assertion floor.
- Live failures are genuine under the current exported lexical existence contract. The comma-anchor case is not an actual missing document; do not misdescribe it as one or broaden anchor grammar as an unrequested C2 repair.
- No independently executed repaired selftest, mutation discriminator, host re-pin, or 6/6 battery result is claimed. No judgment on eventual integration. No tool installs, scratch clone, fixture commits, background processes, or heavy work were needed.
- Provenance limit: before command outputs are existing receipts, not commands executed by this seat; their declared revision is recorded, not independently Git-object verified here.

Self-evaluation: accuracy 4/5 (receipt revision not independently blob-bound); completeness 5/5 (both live call arms and all four subject occurrences traced); clarity 4/5 (source trace is necessarily detailed); actionability 5/5 (isolation boundary and public behavior distinguished); conciseness 4/5 (full occurrence table retained for exactness). Overall 4.4/5. Highest-impact improvement would be independent base-blob binding; no verification claim substitutes for it.

VERDICT: Nonhermetic selftest reads live governance; historical exceptions still validate in the recorded failure. Four live citation occurrences remain legitimately red under the current resolver contract. No patches.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/w1/Kb82R02Checklist.md; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82R02Checklist-evidence.json
