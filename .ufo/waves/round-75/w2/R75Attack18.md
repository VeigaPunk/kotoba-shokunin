# R75Attack18 — S213 pin is not reproducible at measured revision

## Verdict

**Partially falsified; concrete evidence-control defect.** The target's central implementation claim survives inspection: at measured revision `65a5c7a663249e0522cc49e4a148424200d9ddfe`, the committed S211 `run_eval.py` groups observations in `query_triggers[query]`, computes `sum(triggers) / len(triggers)`, and uses `trigger_rate >= trigger_threshold` for should-trigger items (committed snapshot lines 100–127). Its CLI default is three runs and threshold 0.5 (lines 258–267). Thus the stated default unique-query and repeated-identical-string arithmetic is consistent with the inspected code: 3 observations cannot equal 0.5; duplicate identical query strings each schedule three runs into one string-keyed group, permitting 3/6 equality.

But the proposed pinned-byte check is not operable as written for both sources at the measured revision. `git show 65a5c7a:.ufo/waves/round-70/snapshots/S211-run_eval.py.txt` succeeds and hashes to `43e3b8f80dbf69c343967ba77e268fae991d9fa3ed68b32a0ff02532cd48657f`, matching the entry's abbreviated S211 pin. The corresponding `git show 65a5c7a:.ufo/waves/round-70/snapshots/S213-optimizing-descriptions.md` fails: that path does not exist in the committed tree (the failed command's empty-stream hash is not a content hash). The knowledge entry says S213 is pinned at source row 6 and directs snapshot checks, but it does not give a full digest in that row; its opening entries only provide a full hash for S210, not S213. Therefore the report's suggested two-snapshot reproduction cannot be completed from the claimed revision, and the guide wording/equality premise lacks the promised committed S213 bytes in this evidence set.

## Scope and materiality

This does not refute S211's comparator or establish that S213's quoted guide wording is false; it falsifies the assertion that the complete comparison is reproducible from the cited committed snapshots at the measured revision. The target itself appropriately labels this as historical and disclaims current-client behavior. The evidence gap is material to the proposed evidence control and confidence in the paired-source conclusion, not grounds to claim current runtime behavior or to discard the independently verified S211 fact.

## Safe check

Read-only committed-byte check only; no live fetch or model invocation:

- S211 `git show` succeeded; SHA-256 `43e3b8f80dbf69c343967ba77e268fae991d9fa3ed68b32a0ff02532cd48657f`.
- S213 `git show` at the same revision returned `fatal: path ... does not exist in ...`.
- Inspected S211 grouped-key aggregation and comparator directly in that committed file; no execution of `run_eval.py` (it invokes `claude -p` and creates `.claude/commands/` files, so the live command is not a safe cheap check).

**Finding:** repair the evidence trail before treating the exact guide-vs-reference comparison as reproducible: identify the actual committed S213 path/revision and full digest, or limit the verified claim to S211's implementation behavior. No lane source changes made.
