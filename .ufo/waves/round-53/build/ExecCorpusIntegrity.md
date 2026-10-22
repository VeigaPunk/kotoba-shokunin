Result: PARTIAL — scoped fix and patch exported; requested verifier and self-test runs were not executed during the editing wave.

Files changed in the sandbox patch:
- `verifiers/verify_corpus_integrity.py`
- `verifiers/verify_corpus_independent.py`
- `corpus/README.md`

Delivery artifacts written in the lane:
- `.ufo/waves/round-53/build/ExecCorpusIntegrity.patch`
- `.ufo/waves/round-53/build/ExecCorpusIntegrity.md` (this report)

Behavior:
- Both corpus instruments check the citing directory first, then check the exact bare `.ufo/reports/...` token under `/home/vgpnk/Projects/shokunin` if the local file is absent. Neither instrument excludes an entire spot-check file.
- Each instrument has two new self-test assertions: the fleet-root report remains counted and resolves when the fleet file exists (+2 assertions per instrument; +4 total). `corpus/README.md` now indexes the round-52 closure spot-check in the existing Coverage map row style.
- `verifiers/corpus-baseline.json`, `verifiers/floors-registry.json`, and `verifiers/check_assertion_floors.py` were not changed.

Evidence and limits:
- Primary resolver/callsite/self-test: `verifiers/verify_corpus_integrity.py:270-274`, `:615`, `:950-965`.
- Independent resolver/callsite/self-test: `verifiers/verify_corpus_independent.py:213-217`, `:386`, `:910-922`.
- Coverage-map entry: `corpus/README.md:80`.
- Fleet-file existence command returned exit 0 and `PRESENT` for `.ufo/reports/round-48/kotoba.md`, `round-51/kotoba.md`, and `round-52/kotoba.md`.
- The task's plan-commit observation was `tracked_files=76`, `unindexed=1`, `report_total=49`, `report_dead=5`, `commit_total=31` (`plans/round-53.md:68-72`). [INFERENCE] The scoped edits should produce `tracked_files=76`, `unindexed=0`, `report_total=49`, `report_dead=0`, `commit_total=31`; these are not observed post-edit values because the verifier was not run.
- Self-test before/after tallies and fault-injection results: not observed. Per the fleet executor instruction, I did not run `bash verifiers/fault_injection_corpus.sh`, either instrument's `--self-test`, or the corpus-integrity gate during the editing wave. The total self-test assertion tallies are therefore unavailable; only the four added assertions above are known from the patch.
- LSP was unavailable in the exposed tool inventory; symbols were located with repository search and reads.

Commands run (exit code and output):
1. `unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE; git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r53/ExecCorpusIntegrity && git -C /fast/scratch/hyaku/kotoba-r53/ExecCorpusIntegrity checkout -q 3bb0a7a33e6eb585a83a1a55dee30b26079b1e36` — exit 0; no output.
2. `for p in .ufo/reports/round-48/kotoba.md .ufo/reports/round-51/kotoba.md .ufo/reports/round-52/kotoba.md; do if test -f "/home/vgpnk/Projects/shokunin/$p"; then printf 'PRESENT %s\\n' "$p"; else printf 'ABSENT %s\\n' "$p"; fi; done` — exit 0; `PRESENT` for all three paths.
3. `git -C /fast/scratch/hyaku/kotoba-r53/ExecCorpusIntegrity add -A && git -C /fast/scratch/hyaku/kotoba-r53/ExecCorpusIntegrity diff --cached --binary 3bb0a7a33e6eb585a83a1a55dee30b26079b1e36 > /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-53/build/ExecCorpusIntegrity.patch` — exit 0; no output.

Risks/blocker: The fallback intentionally uses the specified host fleet root and is host-path-specific. The post-edit counter values, fault-injection result, and self-test tallies remain unverified; the parent should run the requested checks after integration and re-record the corpus baseline last.