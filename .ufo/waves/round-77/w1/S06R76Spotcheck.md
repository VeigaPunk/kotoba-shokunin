# S06R76Spotcheck — report (kotoba r77 w1)

Task: disposition table for R76-D1..D5 and CD1..CD4 from `corpus/lessons/round-76-verifier-spotcheck.md`, factual re-check of the closure, and unlearned disagreements. Read-only; no scratch dir created, no installs, nothing written outside the two named files.

Axes named: depth (does the closure's evidence resolve), consistency (does r77's plan cover every routed item), calibration (confirmed vs not-run marked), operability (one command per closure), freshness (HEAD `6523aced…` vs the r76 tip).

## Result
- Full table: `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/S06R76Spotcheck.table.md` (§A dispositions, §B disagreements, §C 26 claims marked).
- Of 26 closure claims checked: 21 confirmed, 1 partially confirmed (#24), 3 not re-measurable/not run (#8 remote moved, #25 template byte-diff, #26 clean tree at old tip), plus the 69-assertion D4 tally and `jj-lane.sh state` not run. None contradicted.
- All nine defects are still OPEN at HEAD, each mapped to a r77 seat/file and a closure command.

## Findings that need a fix or QUALITY criterion (details in the table §B)
1. **CD1 is under-scoped:** `git ls-files | grep shokukin` lists TWO typo paths: `kotoba-shokukin/.ufo/waves/round-75/w1/R75Facet48.md` (commit `ac9f295`, no correct-path twin) and the A18 file. E11's prompt names only A18. Deleting R75Facet48 would lose its only copy; it must be moved to `.ufo/waves/round-75/w1/`. Criterion: recovery/preservation commits are checked for the root of every added path (same typo, two rounds, introduced by the recovery step both times).
2. **CD2 repeats in r77:** the plan cites `corpus/lessons/round-76.md` and `round-77.md`; criterion "promised lesson lands or the citation is dropped"; SC01 must put all four decline reasons into the Gate.
3. **D5 root cause missed by the closure:** 7 of the 12 report-less seats (A03, A04, A08, A10, A12, A31, A36) reported the frozen counters absent (wave dispatched at `4de12b6`, counters landed at `ec7f853`); 3 builders (B06, B07, B28) wrote no report; A07, A23 answered inline. r77 avoids it: counter sha256 at HEAD equals the plan pins (`cf3c45d9…`, `989203c4…`). Criterion: attack waves are dispatched only after the counter is committed at the dispatch HEAD; "verifier absent" is a dispatch defect counted separately.
4. Closure ran no counter (by protocol); r77 needs a w2 non-author scratch re-run, not receipt re-reading. r76 controls were scored on stale blob `87837d7a…` (`c1-controls.txt:8`): r77 controls receipts must print the frozen sha beside each verdict.
5. Q74 (folded-scalar measurement) stands: QUALITY ends at Q73, and no existing row covers it.

## Commands run (all exit statuses read directly; no pipeline status used)
`ls corpus/lessons/round-76*.md`; `git ls-files | grep shokukin`; `sha256sum` of both A18 copies and both counters and the snapshot; `git merge-base --is-ancestor` ×6; `git show --stat 6ce2724`; `git diff --name-only/-- LOG.md/SCORECARD.md b7f13f4 6ce2724`; `git grep -c S213 6ce2724`; `wc -lc SKILL.md`; `python3 -B verifiers/verify_corpus_integrity.py --json` (exit 1, 2 unindexed) and `verify_corpus_independent.py --json` (exit 1); `scripts/sources-census.sh validate --root … kotoba` (exit 0, 20 W04); `git ls-remote origin refs/heads/master` (exit 0, `6523aced…`); JSON parses of the r76 `w1-results.json`/`w1-spec.json`.
Counters were not run (not this seat's job; receipts tails read).

VERDICT: closure facts hold (21/26 confirmed, none contradicted); all 9 defects open and mapped; two gaps need action: a second tracked typo path (R75Facet48, move don't delete) and the unrecorded D5 root cause (wave dispatched before counters were committed).
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/S06R76Spotcheck.table.md /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w1/S06R76Spotcheck.md
