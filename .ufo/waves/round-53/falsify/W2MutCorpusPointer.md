Result: MIXED — The checked-in fallback behavior holds, but five scope mutations survive the committed self-tests and are caught only by the targeted probe.

## Findings

- **Moderate, test-coverage gap (no runtime defect at the judged revision):** Both implementations' self-tests kill fallback removal. The independent self-test also rejects the tested “parent directory exists” mutation; the integrity self-test does not. Both built-in self-tests survive the `../` and non-report scope mutations. The direct probe catches every one of these cases. The `.ufo/reports/round-N/...md` extractor also means a non-report token cannot reach the fallback through normal corpus analysis; that case requires the direct helper probe.
- **Runtime behavior HOLDS:** At pristine and restored bytes, an existing bare fleet report resolves, a missing fleet report stays dead, `../` does not use the fleet fallback, and a non-report file does not use the fallback. The planted `.ufo/reports/round-99/kotoba.md` stayed dead in both corpus analyzers.

## Kill table

Mutations were applied separately to the fallback in each target, one file at a time. Hashes are `pristine → mutant → restored`; the restored hashes equal pristine.

| Mutation | Target and hashes | Built-in self-test | Targeted behavioral detector | Verdict |
|---|---|---|---|---|
| Remove fleet fallback | `verify_corpus_integrity.py` — `21137dc0499b09f6d97cabb0da0fe3faa580aa2d04a96066d03d81d230ff1877 → 70adfce0de3e39f467f343d39ff4c7c0b3303f4b924a5808f550e74322aa799f → 21137dc0499b09f6d97cabb0da0fe3faa580aa2d04a96066d03d81d230ff1877` | **Killed:** exit 1, `1 failure(s) over 152 assertions`; existing bare-report control became false. | Direct probe failed the existing-report case; detector exit 1. | HOLDS |
| Remove fleet fallback | `verify_corpus_independent.py` — `2d67a6d6e906d9b043153c1c86795cdb1031e08cb9be414460a4bc8f217231ff → adf97626b5cb7927dda3f53af43f51b6dc7536d7a13fa03264019826d318e3e1 → 2d67a6d6e906d9b043153c1c86795cdb1031e08cb9be414460a4bc8f217231ff` | **Killed:** exit 1, `1 failures` over 93 assertions; existing bare-report control became false. | Direct probe failed the existing-report case; detector exit 1. | HOLDS |
| Accept missing fleet file (check parent directory) | `verify_corpus_integrity.py` — `21137dc0499b09f6d97cabb0da0fe3faa580aa2d04a96066d03d81d230ff1877 → 8044089e626ef053d73ed688a95cbc34567279878d911e741c931e64b4109b43 → 21137dc0499b09f6d97cabb0da0fe3faa580aa2d04a96066d03d81d230ff1877` | **Survived:** exit 0, `0 failure(s) over 152 assertions`. | **Killed:** direct probe returned `actual=True` for missing round-99 report; planted-pointer detail disappeared from integrity output. Detector exit 1. | HOLDS; self-test gap |
| Accept missing fleet file (check parent directory) | `verify_corpus_independent.py` — `2d67a6d6e906d9b043153c1c86795cdb1031e08cb9be414460a4bc8f217231ff → afb1bb9531ea9afb188a14feb7a8c7a97979f30f0c67517a11b143228ba876d5 → 2d67a6d6e906d9b043153c1c86795cdb1031e08cb9be414460a4bc8f217231ff` | **Killed:** exit 1, `2 failures` over 93 assertions. | **Killed:** direct probe returned `actual=True`; planted-pointer detail disappeared from independent output. Detector exit 1. | HOLDS |
| Allow fallback for leading `../` | `verify_corpus_integrity.py` — `21137dc0499b09f6d97cabb0da0fe3faa580aa2d04a96066d03d81d230ff1877 → 7cf6467732e0a1d53e216ad0d4da414f4e15d0eb9b11751aa29d11b66289eff0 → 21137dc0499b09f6d97cabb0da0fe3faa580aa2d04a96066d03d81d230ff1877` | **Survived:** exit 0, `0 failure(s) over 152 assertions`. | **Killed:** traversal probe returned `actual=True`; detector exit 1. | HOLDS; self-test gap |
| Allow fallback for leading `../` | `verify_corpus_independent.py` — `2d67a6d6e906d9b043153c1c86795cdb1031e08cb9be414460a4bc8f217231ff → 8009cf564041789769d9e21aceda4653ee47bc729a8a2115f1a1c079b97f363b → 2d67a6d6e906d9b043153c1c86795cdb1031e08cb9be414460a4bc8f217231ff` | **Survived:** exit 0, `93 assertions, 0 failures`. | **Killed:** traversal probe returned `actual=True`; detector exit 1. | HOLDS; self-test gap |
| Remove report-only guard (allow ordinary fleet-root files) | `verify_corpus_integrity.py` — `21137dc0499b09f6d97cabb0da0fe3faa580aa2d04a96066d03d81d230ff1877 → 37f5a117efdf9d90ca0b282fd5eec2a2f464c409f7337d67c750ae5e802710fd → 21137dc0499b09f6d97cabb0da0fe3faa580aa2d04a96066d03d81d230ff1877` | **Survived:** exit 0, `0 failure(s) over 152 assertions`. | **Killed:** ordinary non-report probe returned `actual=True` (the same broad mutant also admitted `../`); detector exit 1. | HOLDS; self-test gap |
| Remove report-only guard (allow ordinary fleet-root files) | `verify_corpus_independent.py` — `2d67a6d6e906d9b043153c1c86795cdb1031e08cb9be414460a4bc8f217231ff → c1c066e343f8265dfd95d66e6c1365704db14a66e416bc22b5346ef2c7a7652e → 2d67a6d6e906d9b043153c1c86795cdb1031e08cb9be414460a4bc8f217231ff` | **Survived:** exit 0, `93 assertions, 0 failures`. | **Killed:** ordinary non-report probe returned `actual=True` (also admitted `../`); detector exit 1. | HOLDS; self-test gap |

## Detector and planted-pointer evidence

The same bounded detector was run on pristine bytes, after each mutation, and after restoration: `python3 -B fleet_detector.py` in the isolated clone `/fast/scratch/hyaku/kotoba-r53/w2/W2MutCorpusPointer`. Pristine and restored both exited 0 with both self-tests passing (integrity 152 assertions; independent 93), all eight direct behavior cases passing, and both planted-pointer checks passing. Each mutant run exited 1 on at least one expected check failure. The runner checked the exact dead-pointer detail, not the analyzers' overall exit code.

Pristine/restored output:

```text
integrity planted round-99 pointer dead: PASS; analyzer exit=1; report_dead: corpus/lessons/w2-mutation-probe.md:3: .ufo/reports/round-99/kotoba.md
independent planted round-99 pointer dead: PASS; analyzer exit=1; ! corpus/lessons/w2-mutation-probe.md:3: .ufo/reports/round-99/kotoba.md
detector: 0 failure(s)
detector_exit=0
```

On the integrity missing-file mutant, the same check printed `integrity planted round-99 pointer dead: FAIL; analyzer exit=1; pointer detail absent`; on the independent missing-file mutant, the equivalent independent line was `FAIL` / `pointer detail absent`. At pristine/restored bytes the pointer appeared in each dead-detail list. The overall analyzer exit 1 is not counted as a mutant kill: this sandbox intentionally has the planted dead pointer and its unindexed probe file, plus an existing unindexed corpus file and unresolved commit citation. The exact pointer-detail assertion is the tested result.

Source anchors: `verifiers/verify_corpus_integrity.py:270-274`, fallback self-test `:950-965`; `verifiers/verify_corpus_independent.py:213-218`, fallback self-test `:910-922`; report-pointer extractor `verifiers/verify_corpus_integrity.py:144-146`. The round-99 corpus file and detector helpers were created only in the scratch clone and removed after the run.

Restoration: the final hashes shown above match the pristine hashes for both target files; the restored detector exited 0. No lane source, Git index, or jj state was changed; no tools were installed.
