# MutC1Index — C1 repair-shape mutation probe

- **Pinned base:** `2a8eba56b3f9321b70c569fa2816d42237ca49a2`.
- **Measured tree:** `/tmp/k67-mutc1index-2a8eba56/repo`, an isolated `/tmp` archive of that base plus only the C1 index-row/baseline repair. This is not a claim about the moving lane working tree or a later tip.
- **Axes:** detector discrimination, exact restoration, evidence fidelity.
- **Detector (every run, cwd above):** `python3 -B verifiers/verify_corpus_integrity.py`.
- **Pristine control:** exit **0**; printed **`9/9 checks pass`**. The control was green before any mutant was scored.
- **Repair derivation:** `python3 -B verifiers/verify_corpus_integrity.py --no-baseline --json` observed `tracked_files=119`, `unindexed=0`, `report_total=82`, `commit_total=38`; the scratch baseline expectations moved 118→119, 79→82, and 37→38 respectively.

## Mutants

### M-a — remove the r66 coverage-map row

- **Mutant:** remove the round-66 spot-check coverage-map row from corpus/README.md.
- **Expected detector:** nonzero exit and `corpus.index.unindexed: observed=1`.
- **Command:** `python3 -B verifiers/verify_corpus_integrity.py`.
- **Actual output (verbatim DRIFT line):**
  ```text
DRIFT   corpus.index.unindexed: observed=1 expected=0 / empty
  ```
  Detail: `unindexed: corpus/lessons/round-66-verifier-spotcheck.md`; summary: `8/9 checks pass; DRIFT: corpus.index.unindexed`.
- **Exit / verdict:** **1 / killed**.

### M-b — corrupt one baseline value only

- **Mutant:** corrupt only baseline corpus.pointers.report_total expect 82 -> 83; `corpus/README.md` stayed at the honest hash.
- **Expected detector:** nonzero exit and a `corpus.pointers.report_total` DRIFT.
- **Command:** `python3 -B verifiers/verify_corpus_integrity.py`.
- **Actual output (verbatim DRIFT line):**
  ```text
DRIFT   corpus.pointers.report_total: observed=82 expected=83
  ```
  Summary: `8/9 checks pass; DRIFT: corpus.pointers.report_total`.
- **Exit / verdict:** **1 / killed**.

### M-c — add unindexed junk under `corpus/lessons/`

- **Mutant:** append tracked junk corpus/lessons/round-67-mutc1index-junk.md without a coverage-map row (scratch-only stage-0 index entry). The scratch-only index entry is necessary because this gate enumerates tracked files; a merely untracked junk file would not exercise the claimed behavior. No git/jj write command was run.
- **Expected detector:** nonzero exit and an `unindexed` finding for the junk path.
- **Command:** `python3 -B verifiers/verify_corpus_integrity.py`.
- **Actual output (verbatim lines):**
  ```text
           unindexed: corpus/lessons/round-67-mutc1index-junk.md
DRIFT   corpus.index.tracked_files: observed=120 expected=119
DRIFT   corpus.index.unindexed: observed=1 expected=0 / empty
  ```
  Summary: `7/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.index.unindexed`.
- **Exit / verdict:** **1 / killed**.

## Restoration evidence

| Arm | Before → mutant → restored SHA-256 (behavior-bearing bytes) | Restored detector |
|---|---|---|
| M-a `corpus/README.md` | `3e587c01242bbc52ae4cae0c67ec158bea96b70d9800ff2c0db5cfeee4171f31` → `19d303b059be9611d1f20c5ac4e37f988f63d38df8b45355732e68c9887f53c2` → `3e587c01242bbc52ae4cae0c67ec158bea96b70d9800ff2c0db5cfeee4171f31` | R-a exit 0, `9/9 checks pass`, output byte-identical to control |
| M-b `verifiers/corpus-baseline.json` | `043ce0d2837680777b3c4e9daa947bf665a850b4ff45c1a1a26ff0bed95d2aa6` → `c908b0ccf48891a31d636b722511dba0f509c8a8eab5d370cfefc1c404e1b35a` → `043ce0d2837680777b3c4e9daa947bf665a850b4ff45c1a1a26ff0bed95d2aa6` | R-b exit 0, `9/9 checks pass`, output byte-identical to control |
| M-c `.git/index` (scratch only) | `844b700e6ee2e58d9f106ed41302381cd7da2731c5e3601cbe9d3ba19a912b50` → `21adbe08e80c19afcd8cfcc380eaa31b49092367c2cf149ab441f5d1af65a23c` → `844b700e6ee2e58d9f106ed41302381cd7da2731c5e3601cbe9d3ba19a912b50` | R-c exit 0, `9/9 checks pass`, output byte-identical to control |
| M-c junk file | `ABSENT` → `0dd6a4caf12f1e0ba900c4b339cf87e8dd2b6266fc335c3e73d79e77479eca36` → `ABSENT` | removed before R-c |

Final scratch hashes match the pristine repaired state for `corpus/README.md` (`3e587c01242bbc52ae4cae0c67ec158bea96b70d9800ff2c0db5cfeee4171f31`), `verifiers/corpus-baseline.json` (`043ce0d2837680777b3c4e9daa947bf665a850b4ff45c1a1a26ff0bed95d2aa6`), and the scratch index (`844b700e6ee2e58d9f106ed41302381cd7da2731c5e3601cbe9d3ba19a912b50`); the junk file is absent. **3/3 mutants killed; 0 survived; 0 inconclusive.** Full pristine/mutant/restored stdout and the complete state hashes are in `controls/C1-mutants.txt`.

No tools were installed or updated.

Report: .ufo/waves/round-67/w1/MutC1Index.md
