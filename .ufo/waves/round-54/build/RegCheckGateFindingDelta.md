Result: DONE — inspected the verifier at the assigned sandbox revision, ran help and self-test, and prepared the C2 row with observed outcomes and scope.

| `verifiers/check_gate_finding_delta.py` | gate | `python3 -B verifiers/check_gate_finding_delta.py --base <rev> --head <rev>` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | temp trees/indexes under `$TMPDIR`; repo read-only | kotoba |

Evidence for the cells:

- **Name / kind:** sandbox source `verifiers/check_gate_finding_delta.py:1-21` describes comparing a gate's finding-set delta and says a new head finding exits 1. `:85-106` implements the comparison. It can fail on new findings, so `gate` is appropriate.
- **Entry command:** source docstring `:14-15` shows the invocation; `:156-167` makes `--repo` default to `.` and requires `--base` and `--head`. Thus the row's command is the shortest invocation from the repository root.
- **Verdict map and exit paths:** source `:94-106` returns 1 for nonempty `new`, otherwise 0; `:47-53` raises `SystemExit(2)` if the nested gate exits outside 0/1 or emits no stdout. `:165-166` also sends missing required revisions through argparse's exit-2 usage error. `:109-151` returns 1 for self-test assertion failures and 0 when they pass. `--help` likewise exits 0. Uncaught errors such as `git archive`/`read-tree` failures (`:58-60`, `:78-81`) or malformed JSON (`:51`) terminate Python with status 1 [INFERENCE]; they do not produce a distinct explicit status. The nested gate's exit 3, when encountered, is normalized to wrapper exit 2 by `:47-50`.
- **Self-test:** the literal flag is at `:161`; its in-file expected results are at `:116-146`. In the clone, command `mkdir -p .tmp && TMPDIR="$PWD/.tmp" python3 -B verifiers/check_gate_finding_delta.py --self-test` exited **0**; last script output line: `self-test: 0 failure(s) over 9 assertions`. The temporary fixtures were confined to the clone's `.tmp` directory.
- **Pinned values / expected-value files:** `in-file` refers to the delta expectations exercised by the self-test (`:116-146`); this wrapper does not read a fixed expected-value file directly. Its default nested gate is `verifiers/verify_corpus_integrity.py` (`:159`), whose default expected-value file is `verifiers/corpus-baseline.json` in each evaluated revision (`verify_corpus_integrity.py:101-103,1292-1310`; that path exists in the clone). `--gate` can override the nested gate, so the baseline is not a fixed pin of the wrapper itself.
- **Write scope:** `:85-93` uses a `TemporaryDirectory`, extracts revision trees (`:56-64`), and creates per-revision indexes (`:67-81`, with `GIT_INDEX_FILE` pointed at the temp path). The repository is read-only in these paths. Self-test also creates temporary fixture trees (`:123-133`). The default nested verifier describes itself as doing no writes (`verify_corpus_integrity.py:46-48`); a custom `--gate` is outside this wrapper's write guarantee.
- **Owner / row rules:** `check_gate_registry.py:20-36` requires gate rows to declare `0=clean`, `1=failed`, a literal self-test flag, non-`none` pinned values, and owner `kotoba`; it permits `in-file`. `:65` pins that owner.

Execution evidence (clone: `/fast/scratch/hyaku/kotoba-r54/RegCheckGateFindingDelta`, checked out at `7ad05d342d7505ab674a5ebcf5ac1106b2f45c39`):

- `python3 -B verifiers/check_gate_finding_delta.py --help` — exit **0**; last output line: `  --self-test`.
- `mkdir -p .tmp && TMPDIR="$PWD/.tmp" python3 -B verifiers/check_gate_finding_delta.py --self-test` — exit **0**; last output line: `self-test: 0 failure(s) over 9 assertions`.
- No main two-revision comparison was run; the self-test exercises the delta model and synthetic nested-gate outputs, not Git revision extraction or the real default baseline. Both requested runs completed; no network access was used.

Documentation comparison at this revision:

- Search for `check_gate_finding_delta` / `finding_delta` in `SKILL.md`, `verifiers/README.md`, and `verifiers/floors-registry.json` returned no matches. `SKILL.md:532-533` points to the verifier inventory in README and to registry rows under `§ Gate registry`, but the registry heading/table is not present at this checkout. `verifiers/README.md:3-6,8-50` describes the inventory and says rows live in SKILL.md; it has no entry for this script. `floors-registry.json:2-4,5-56` identifies itself as the `check_assertion_floors.py` instrument registry, not the gate registry. No contradictory behavioral statement was found; the finding-delta script is absent from these references at the pre-C2 checkout.

Risk: the self-test does not exercise revision extraction, the real nested gate, or errors from malformed gate JSON. The wrapper's explicit status 1 is for a new finding, but uncaught runtime errors also end at process status 1 [INFERENCE]. Blockers: none.
