# ScribeCorrections
role: Leaf scribe; committed-byte correction evidence.
item: ScribeCorrections — draft appended LOG.md corrections for r62 spot-check defects 2 and 4.

## Findings

1. **Receipt revision.** I measured the requested base commit, not the moving worktree. At `35d44b4b`, `C2-successor-measure.txt` says `receipt_rev=3f911504ce76d9ca186f297d6d4a9cd8ed77508a`; the same file at `3f911504` says `receipt_rev=3e7aed9b61bbfd83e0c800213b6dfc6da6191f85`. The correction value is the former.
   Evidence command/output is reproduced verbatim under Artifacts.
2. **Knowledge-entry size.** Committed `corpus/knowledge/erratum-absorption-round62.md` at `35d44b4b` is 64 lines and 1,044 words (`wc -l -w`).
3. **Child-commit conflict.** The in-lane spot-check identifies the r62 closed lane tip as `e53b6e5c0aaa1ef2b0861b9399fef44f8b907f02` and says the report was committed at `def4b9ff…` (`corpus/lessons/round-62-verifier-spotcheck.md:11-20`). At the requested base, the commit graph has one direct descendant of that lane tip: `35d44b4b…`, whose parent is `e53b6e5c…` and whose subject is `round-62 verifier spot-check (integrator, hyaku): non-author admit/reject`. It was committed at `19:36:39 -03`, after the report time `18:56:15 -03` cited at line 20. Thus the requested literal correction “no post-report child commit exists” is contradicted by the lane graph. The spot-check's own phrase is verbatim: “no child exists — the cited tip is the tip” (line 49); it is not supported for the cited `e53b6e5c` lane tip. `git rev-list --children 35d44b4b --max-count=1` prints only `35d44b4b`; that query does not show descendants of its starting commit. I have not read the fleet-repo report itself (hard-bound out of scope), so cannot exclude a different citation in that file.
4. **Interim no-harm reds.** The committed receipt at its measured revision `3e7aed9b…` reports `reg_gate` at 36 of 38 lane verifiers; each of the two named new instruments has 0 registry rows (1 required). `corpus-idx` reports the single unindexed path `corpus/lessons/round-61-verifier-spotcheck.md` (`noharm-tip.txt:12-17`). These are interim receipt results, not a claim about the later tip.
5. **Execution and surfaces.** Only read-only Git/blob and counting/search commands were run; no build, test, or other gate was run. No tool was installed. I did not edit `LOG.md` or product files. The sole write is this report. The worktree had advanced to `8c4cefa8…` with untracked round-63 work, so all requested figures were taken from committed `35d44b4b` bytes.

## Artifacts

Proposed appended block (not applied to `LOG.md`):

```markdown
- **Round-62 spot-check corrections (committed-byte re-derivation at `35d44b4b4dcdda234b5dbff7af37e432fec55f05`).** The C2 receipt at this tip pins `receipt_rev=3f911504ce76d9ca186f297d6d4a9cd8ed77508a` (the file at `3f911504` itself pins `3e7aed9b61bbfd83e0c800213b6dfc6da6191f85`); the erratum entry is **64 lines / 1,044 words**. The report-cited lane tip `e53b6e5c0aaa1ef2b0861b9399fef44f8b907f02` has one direct post-report child in this base history: `35d44b4b4dcdda234b5dbff7af37e432fec55f05`, the spot-check commit. No separate final-sweep child is evidenced; do not state that no post-report child commit exists. The interim no-harm receipt measured at `3e7aed9b61bbfd83e0c800213b6dfc6da6191f85` recorded `reg_gate` at **36 of 38** lane verifiers (the two new instruments each had 0 registry rows, 1 required) and `corpus-idx` leaving `corpus/lessons/round-61-verifier-spotcheck.md` unindexed.
```

Commands and outputs underlying that draft:

```text
$ git show 35d44b4b4dcdda234b5dbff7af37e432fec55f05:.ufo/waves/round-62/C2-successor-measure.txt | grep -n 'receipt_rev'; git show 3f911504:.ufo/waves/round-62/C2-successor-measure.txt | grep -n 'receipt_rev'
2:receipt_rev=3f911504ce76d9ca186f297d6d4a9cd8ed77508a
2:receipt_rev=3e7aed9b61bbfd83e0c800213b6dfc6da6191f85

$ git show 35d44b4b4dcdda234b5dbff7af37e432fec55f05:corpus/knowledge/erratum-absorption-round62.md | wc -l -w
     64    1044

$ git rev-list --children 35d44b4b4dcdda234b5dbff7af37e432fec55f05 --max-count=1
35d44b4b4dcdda234b5dbff7af37e432fec55f05

$ git rev-list --ancestry-path e53b6e5c0aaa1ef2b0861b9399fef44f8b907f02..35d44b4b4dcdda234b5dbff7af37e432fec55f05 | wc -l
1

$ git log --ancestry-path --format='%H %P' e53b6e5c0aaa1ef2b0861b9399fef44f8b907f02..35d44b4b4dcdda234b5dbff7af37e432fec55f05
35d44b4b4dcdda234b5dbff7af37e432fec55f05 e53b6e5c0aaa1ef2b0861b9399fef44f8b907f02

$ git show -s --format='%H %cI %s' e53b6e5c0aaa1ef2b0861b9399fef44f8b907f02; git show -s --format='%H %cI %s' 35d44b4b4dcdda234b5dbff7af37e432fec55f05
e53b6e5c0aaa1ef2b0861b9399fef44f8b907f02 2026-10-23T18:56:08-03:00 round-62: seventh sweep — SCORECARD corrections from FalsifyScorecard (before-state 2 of 5 at line 369, six survivor instances wording, four gate rows) + its report
35d44b4b4dcdda234b5dbff7af37e432fec55f05 2026-10-23T19:36:39-03:00 round-62 verifier spot-check (integrator, hyaku): non-author admit/reject

$ git show 35d44b4b4dcdda234b5dbff7af37e432fec55f05:.ufo/waves/round-62/noharm-tip.txt | grep -n -A3 -E 'reg_gate|corpus-idx'
12:FAIL  reg_gate    expected exit 0 in both columns, got base=0 tip=1
13-        tip: verifiers/check_erratum_absorption.py        no registry rows naming it: 0 (need 1)
14-        tip: verifiers/check_routed_repairs_v2.py         no registry rows naming it: 0 (need 1)
15-        tip: gate registry rows conformant 36 of 38 lane verifiers; phantom 0
--
17:FAIL  corpus-idx  tip leaves new corpus file(s) unindexed: corpus/lessons/round-61-verifier-spotcheck.md 

$ git rev-parse HEAD; git status --porcelain
8c4cefa8e1b751d5f93dbcc65349b8e985b102d8
?? .ufo/waves/round-62/w2/FalsifyC2HonestH1.md
?? .ufo/waves/round-63/w1-dispatch.err
?? .ufo/waves/round-63/w1-dispatch.json
?? .ufo/waves/round-63/w1-spec.json
?? .ufo/waves/round-63/w1/
?? verifiers/check_scoped_rules_v32.py
```

Touched surfaces: read-only base blobs, `corpus/lessons/round-62-verifier-spotcheck.md`, and `LOG.md` context; written artifact: `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-63/w1/ScribeCorrections.md`. Out of scope: fleet report/repository, any LOG or production edit, and all gates.

## Verdict

ATTACKS — the requested no-post-report-child assertion conflicts with the lane commit graph. I would change this only if the exact report-cited commit is shown to be a different repository/object from `e53b6e5c…`, or a bounded graph for that exact citation shows no post-report descendant. The fleet report itself was not read under the lane hard bounds.
