# ExecLessonMistake
role: scribe (calibration)
item: Draft one `corpus/lessons/round-63.md` § Mistakes entry; report only.

## Findings

1. The r62 close has one coherent calibration mistake: its self-assessment was not reconciled against the final committed tree. The non-author audit records five mismatches across spot-check §6 defects 1, 2, and 4: one late write absent from the close tree; three stale report citations (C2 receipt revision, entry size, and a claimed post-report child commit); and two interim no-harm reds omitted from the summary. Evidence: `corpus/lessons/round-62-verifier-spotcheck.md:45-58,159-175`; the five-count and separation of defect 3 (source-negotiation freshness, not self-assessment) are also stated in `plans/round-63.md:79-86`.

2. Historical committed bytes substantiate the tracked-state, receipt, and size mismatches. Exact read-only commands and observed output:

   ```text
   $ git ls-tree -r e53b6e5c0aaa1ef2b0861b9399fef44f8b907f02 -- .ufo/waves/round-62/w2/FalsifyC2HonestH1.md
   [no rows printed]

   $ git show e53b6e5c0aaa1ef2b0861b9399fef44f8b907f02:.ufo/waves/round-62/C2-successor-measure.txt
   # round-62 C2 successor data receipt
   receipt_rev=3f911504ce76d9ca186f297d6d4a9cd8ed77508a
   ...

   $ git show e53b6e5c0aaa1ef2b0861b9399fef44f8b907f02:corpus/knowledge/erratum-absorption-round62.md | wc -lw
        64    1044
   ```

   The spot-check says the report instead named `receipt_rev=e6da78bb…` and `723 words, 50 lines` (`corpus/lessons/round-62-verifier-spotcheck.md:45-52`). The spot-check also records the false child-commit claim at `:49-52`.

3. The committed no-harm receipt contains both omitted interim reds. Exact command and selected output (other receipt rows omitted):

   ```text
   $ git show e53b6e5c0aaa1ef2b0861b9399fef44f8b907f02:.ufo/waves/round-62/noharm-tip.txt
   Measured revision: 3e7aed9b61bbfd83e0c800213b6dfc6da6191f85
   FAIL  reg_gate    expected exit 0 in both columns, got base=0 tip=1
           tip: gate registry rows conformant 36 of 38 lane verifiers; phantom 0
   FAIL  corpus-idx  tip leaves new corpus file(s) unindexed: corpus/lessons/round-61-verifier-spotcheck.md
   Battery exit code: 124
   ```

   This is receipt evidence of two failing arms, not a full-battery pass: the captured run ended 124. The discrepancy is routed in spot-check §6.4 (`corpus/lessons/round-62-verifier-spotcheck.md:173-175`); `LOG.md:2566` points to the receipt but does not state those results.

4. A capture criterion existed but did not prevent the mistake: `plans/round-62.md:193-197` explicitly tasked wave 2 with checking the report claims and the lesson/no-harm/census. The r63 frozen C2 plan specifies a revision-bound counter for late-write tracking, receipt revision, entry size, append-only LOG, and no-harm tokens (`plans/round-63.md:91-109`). This is contract evidence only; I did not execute the r63 counter. Important limit: that frozen list does not explicitly assert that the false post-report child-commit claim is corrected; append-only alone does not check its truth (`plans/round-63.md:105-109`). I therefore do not claim the planned counter catches recurrence of all five points.

5. Provenance/scope: initial read-only inspection reported lane HEAD `8c4cefa8e1b751d5f93dbcc65349b8e985b102d8` and showed the late report plus in-progress r63 files untracked; I left those files untouched. `git cat-file -e e53b6e5c0aaa1ef2b0861b9399fef44f8b907f02:.ufo/reports/round-62/kotoba.md` returned `fatal: path '.ufo/reports/round-62/kotoba.md' does not exist in 'e53b6e5c0aaa1ef2b0861b9399fef44f8b907f02'` (exit 128), so report wording is sourced from the committed spot-check, not a lane report blob. Only this assigned report is written. No product files, gates, builds, tests, or linters were run/changed; no tools were installed. S049's Accept-header/source-freshness issue (defect 3), SHONEN (operator-owned), and G9 are outside this one mistake.

## Artifacts

Draft for `corpus/lessons/round-63.md` § Mistakes (proposed M94):

```markdown
- **M94 — class: close self-assessment not reconciled against the final committed tree** · Evidence: the r62 non-author spot-check routes the missing late write, three stale report citations (receipt revision, entry size, and a claimed post-report child commit), and omitted interim no-harm reds (`corpus/lessons/round-62-verifier-spotcheck.md:45-58,159-175`). At the r62 close tip, `git ls-tree -r e53b6e5c0aaa1ef2b0861b9399fef44f8b907f02 -- .ufo/waves/round-62/w2/FalsifyC2HonestH1.md` printed no rows; the committed C2 receipt says `receipt_rev=3f911504ce76d9ca186f297d6d4a9cd8ed77508a`, while the report named `e6da78bb…`; `git show e53b6e5c0aaa1ef2b0861b9399fef44f8b907f02:corpus/knowledge/erratum-absorption-round62.md | wc -lw` printed `64 1044`, not the report's `50 723`; and the committed `noharm-tip.txt` records `reg_gate` 36 of 38 plus the `corpus-idx` failure. · captured-by: `plans/round-62.md:193-197` explicitly required wave 2 to check report claims and lesson/no-harm/census; that check did not catch these mismatches. · fix: the r63 plan specifies `python3 -B verifiers/check_r63_routed_repairs.py --rev <rev>` to derive the tracked-file, receipt-revision, entry-size, append-only, and no-harm checks from committed bytes (`plans/round-63.md:91-109`). This is specified, not executed evidence. The frozen checks do not explicitly validate correction of the false child-commit claim, so I do not claim they catch recurrence of all five points.
```

No verification gate was run. Evidence commands above were read-only Git/show and `wc` queries against the frozen r62 tip.

## Verdict

INFORMS — propose M94 as a calibration lesson, bounded by the recorded gap in the r63 counter contract. I would change this assessment if committed r63 evidence showed the `--rev` predicate fails on each of the five stale-assertion recurrences (including a false child-commit claim) and passes only after the corresponding committed-byte corrections.