# ExecC1BaseControl — C1 BEFORE control

## Measurement scope

- Repository: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.
- Pinned base and measured `git rev-parse HEAD`: `2a8eba56b3f9321b70c569fa2816d42237ca49a2` (the independent JSON also reports `"head": "2a8eba5"`).
- `git status --short --untracked-files=no` showed only pre-existing modifications to `.ufo/waves/round-65/w1/swarm-registry.json` and `.ufo/waves/round-66/w1/swarm-registry.json`; it showed no tracked `corpus/` or `verifiers/` modification.
- No repair was made. No file under `corpus/` or `verifiers/` was modified.

## Exact BEFORE evidence

The verbatim stdout, empty stderr streams, and exit codes for both requested commands are recorded in [controls/C1-base.txt](controls/C1-base.txt).

- `python3 -B verifiers/verify_corpus_integrity.py`: exit **1**; stdout ends `5/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.index.unindexed, corpus.pointers.report_total, corpus.pointers.commit_total`; stderr was empty.
- `python3 -B verifiers/verify_corpus_independent.py --json`: exit **1**; JSON reports `corpus.index.unindexed` observed `1`, verdict `DRIFT`, with detail `corpus/lessons/round-66-verifier-spotcheck.md`; stderr was empty.

## DRIFT baseline keys and verbatim gate lines

Four keys in `verifiers/corpus-baseline.json` were DRIFT under the primary gate:

| Baseline key | Verbatim gate output |
|---|---|
| `corpus.index.tracked_files` | `DRIFT   corpus.index.tracked_files: observed=119 expected=118` |
| `corpus.index.unindexed` | `DRIFT   corpus.index.unindexed: observed=1 expected=0 / empty` |
| `corpus.pointers.report_total` | `DRIFT   corpus.pointers.report_total: observed=82 expected=79` |
| `corpus.pointers.commit_total` | `DRIFT   corpus.pointers.commit_total: observed=38 expected=37` |

The other five checks were PASS, yielding the printed `5/9 checks pass` summary. The independent instrument does not compare equal-count keys to this baseline: its JSON marks the three count observations `INFO` and independently marks `corpus.index.unindexed` `DRIFT`.

## Files changed / remaining limits / blockers

- Wrote only `.ufo/waves/round-67/w1/controls/C1-base.txt` and this report; command captures used distinct files under `/tmp`.
- This is BEFORE evidence only; no repaired-tree or AFTER result was measured.
- Blockers: none.
