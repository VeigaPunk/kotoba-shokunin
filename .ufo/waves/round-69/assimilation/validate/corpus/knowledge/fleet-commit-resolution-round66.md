source: S122 — FORCE11 Software Citation Principles — https://force11.org/info/software-citation-principles-published-2016/, §6.7 Unique identification. The original paper states that a commit reference together with a repository URL is not recommended as durable software citation; this entry applies its version-context distinction to a local integrity check, not to citation permanence.
verified-at: 2026-10-24
recheck: `python3 -B verifiers/verify_corpus_integrity.py` must exit 0 after the round-66 corpus baseline is re-recorded; `python3 -B verifiers/verify_corpus_integrity.py --self-test` must retain the lane-only, fleet-only and neither-repository commit-resolution arms.

# Resolve commit references in their repository context

`verify_corpus_integrity.py` checks citations in lane corpus files. A closure-authored spot-check can cite the fleet report's commit, which is not an object in the child-lane repository. The resolver therefore checks the lane repository first and falls back to the configured fleet root; one citation remains one counted citation. A token present in neither repository stays unresolved.

This check establishes only that a historical object exists in one of the lane's two declared repositories. It does not make a raw commit identifier a persistent or independently resolvable software citation. The S122 source explicitly cautions against presenting a commit reference with its repository URL as a durable software citation; the gate's scope is local evidence integrity, not research citation policy.

Evidence: `verifiers/verify_corpus_integrity.py` defines `commit_resolves`, the lane/fleet fallback and a matching-code-span context exclusion. Its self-test distinguishes lane-only, fleet-only, nonexistent, non-repository and missing-fleet-root cases; the r66 routed-repairs counter's no-fleet-hop mutant fails D2. The before-state and counter control are recorded in `.ufo/waves/round-66/controls/C2-before.txt`; the landed gate receipt is `.ufo/waves/round-66/receipts/C2-integrity-after.txt`.
