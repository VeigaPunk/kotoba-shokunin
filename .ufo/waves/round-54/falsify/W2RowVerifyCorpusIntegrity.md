Result: HOLDS — every cell of the `verify_corpus_integrity.py` registry row survives attack (all four declared exit codes produced with their declared meanings, self-test genuine, baseline really read as expected values, write scope accurate, gate is the right kind); three collateral findings are reported for the wave (one real defect in wave-1 C1 content: a commit citation that resolves nowhere).

Attacked row, as landed at bf65974c7845a06d7ef621ad998c6378ff735cd5 (SKILL.md:459; file byte-identical at wave tip 58db81c4 — `git diff --stat bf65974c 58db81c -- verifiers/verify_corpus_integrity.py verifiers/corpus-baseline.json` is empty):

| `verifiers/verify_corpus_integrity.py` | gate | `python3 -B verifiers/verify_corpus_integrity.py` | 0=clean, 1=failed, 2=could-not-evaluate, 3=could-not-evaluate | `--self-test` | `verifiers/corpus-baseline.json` | self-test fixtures under `$TMPDIR` | kotoba |

Environment: sandbox clone `/fast/scratch/hyaku/kotoba-r54/W2RowVerifyCorpusIntegrity` at 58db81c4 (detached). No LSP server was available to this seat (no `lsp` device in the seat toolset), so all checks below are direct source reads and executed runs; grep was used only to locate lines, never as semantic proof. No tools were installed or upgraded (none needed). No paid model calls, no network.

## 1. Entry command — HOLDS

`python3 -B verifiers/verify_corpus_integrity.py` from the repo root, exactly as the cell declares. No `--rev` is needed: the gate grades the tree it runs on (`--repo` defaults to the script's grandparent, PROTOCOL.md § Gate standard "a gate grades the tree it runs on"), so the row is consistent with the standard.

- At wave tip 58db81c4: exit 1, last line `5/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.pointers.report_total, corpus.pointers.commit_total, corpus.pointers.commit_unresolvable` (4 DRIFT rows printed above it).
- At the C2 landing commit bf65974c (run with `git switch -q --detach bf65974c`, then back): exit 1, last line `6/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.index.unindexed, corpus.pointers.report_total`.
- Read-only proof: after all entry and self-test runs, `git status --porcelain | wc -l` printed `0`. No network use in the measurement path (docstring line 48: "Determinism: every list is sorted, no network, no writes anywhere"; the only subprocesses are `git ls-files`/`git cat-file` helpers, verifiers/verify_corpus_integrity.py:534-557). Runtime a few seconds, well under 10 minutes.

The redness itself is not a row defect: the pinned baseline is stale by design this round (as_of 2026-09-29, head d85982d; the drift rule forbids freshness work). The gate is honestly reporting drift against its committed expected values — which is the behavior the row promises.

## 2. Self-test — HOLDS (one PROTOCOL-clause caveat, minor)

`python3 -B verifiers/verify_corpus_integrity.py --self-test` → exit 0, output `self-test: 0 failure(s) over 152 assertions`.

- It is the script's own self-test: argparse `--self-test` (line 1273) dispatches to `self_test()` defined in the same file (line 754) at line 1290. It is not a nested call (no `subprocess`/`main(` invocation anywhere in lines 754-1264; the only subprocess use in the file is the measurement `git()`/`git_ok()` helpers at 534-557) and not usage text (real tally line, real assertions).
- What it asserts: in-process fixtures under `tempfile.TemporaryDirectory()` (line 950; writes at 955-957 only) covering brace expansion, fence handling, token filtering, quoted meta-findings, pointer resolution (relative/absolute/tilde/bare, fleet-root bare), non-hash and lookbehind rules, and `evaluate()` verdict classes PASS/OBSERVE/DRIFT including the baseline-free mode — finding-id level assertions on `*_detail` lists, matching PROTOCOL's "stable expected finding-id".
- Caveat (minor, finding D3 below): `self_test()` never calls `main()` and asserts no exit code, so the PROTOCOL § Gate standard Self-test clause ("asserting both the exit code and a stable expected finding-id") is only half-satisfied. The counter's row rules do not measure this and the Self-test cell itself is accurate.

## 3. Verdict map — HOLDS (all four codes produced with the declared meaning; one mislabeled crash path, minor)

Declared: 0=clean, 1=failed, 2=could-not-evaluate, 3=could-not-evaluate. Production sites and empirical runs:

- 0=clean — produced at line 1351 (`return 1 if drift else 0`). Empirical: clean sandbox fixture repo (one tracked corpus file covered by one `## Coverage map` pattern) with a matching minimal baseline → last line `9/9 checks pass`, exit 0.
- 1=failed — line 1351 with drift; self-test failure path line 1264. Empirical: tip run exit 1 with 4 DRIFT rows; bf65974c run exit 1 with 3 DRIFT rows. Meaning matches: DRIFT = the checked surface disagrees with committed expected values.
- 2=could-not-evaluate — lines 1301 (`except Inconclusive`) and 1304 (`except OSError`), printing `INCONCLUSIVE: …` to stderr. Empirical: `--repo /nonexistent/repo` → stderr `INCONCLUSIVE: repo directory not found: /nonexistent/repo`, exit 2.
- 3=could-not-evaluate — line 1344, missing baseline (and not `--no-baseline`), message names it: `no baseline at <path> — observations above only (exit 3)`. Empirical: `--baseline /nonexistent/baseline.json` → exit 3. Meaning matches: without expected values the equal checks cannot be compared, so could-not-evaluate is the right class.

No produced code is missing from the map: the only other exits are argparse usage errors (exit 2 — same code, and a usage error is genuinely could-not-evaluate) and uncaught crashes (exit 1 — see residual risk).

## 4. Pinned values — HOLDS

`verifiers/corpus-baseline.json` is really read as expected values: `BASELINE_NAME = "corpus-baseline.json"` (line 123), default path `<repo>/verifiers/corpus-baseline.json` (main, ~1306), read at line 1310 (`baseline = json.loads(baseline_path.read_text())`), then compared by `evaluate()` (line 664) against observations. The file's structure `{checks: {<check-id>: {mode, expect}}}` matches the nine check ids the script computes (verified by loading it: top keys `as_of, checks, host, measured_against, notes`; e.g. `corpus.index.tracked_files` mode `equal` expect 78, `corpus.pointers.report_total` expect 49), and the DRIFT rows observed at tip/bf65974c name exactly those ids with those expects — the pinned values are live in the verdict path, not decorative.

## 5. Write scope — HOLDS

Cell: "self-test fixtures under `$TMPDIR`". The only writes in the entire file are inside `self_test()`'s `tempfile.TemporaryDirectory()` block (lines 950, 955-957: two `mkdir`, one `write_text`, all under the tmpdir root), and `TemporaryDirectory` honors `$TMPDIR`. The entry path writes nothing (docstring line 48; empirical: porcelain clean after runs; `python3 -B` prevents `__pycache__`). The cell names exactly the writes that exist.

## 6. Gate vs probe — HOLDS

The script can fail and does: exit 1 with DRIFT rows at tip and at bf65974c (§1). PROTOCOL § Gate standard: "A tool that cannot fail is a probe" — this one reads surfaces, compares against expected values persisted in its own repo, and returns a verdict. `gate` is the right kind.

## Collateral findings (out-of-row, for the wave; no lane file patched)

- **D1 (real defect, wave-1 C1 content, medium):** `corpus/knowledge/skill-listing-thresholds-round54.md:43` (Gemini CLI row) cites ``commit `451a02ff` `` as evidence for "no truncation at `skillLoader.ts:211` or `snippets.ts:320`", and the hash resolves nowhere: lane clone `git cat-file -e 451a02ff^{commit}` → exit 128; fleet root `/home/vgpnk/Projects/shokunin` → exit 128; absent from `git log --all`; jj in the lane (read-only, `--ignore-working-copy`) → `Error: Revision '451a02ff' doesn't exist`. This single citation moved `corpus.pointers.commit_unresolvable` 0→1 at tip (visible in the bf65974c-vs-tip runs above: unresolvable=0 at bf65974c, =1 at tip, detail names this file:line). A claim pinned to evidence that does not exist is an over-wide-record-class defect (the defect family that recurred in rounds 50-53). Proposed fix (text): either cite the resolvable git commit that actually contains the Gemini CLI tree evidence, or reword the cell to name the evidence without the ``commit `<hex>` `` citation shape so the corpus's own convention is not violated.
- **D2 (context, next round's freshness work):** the gate is red at bf65974c and tip for stale-baseline reasons — including `corpus.index.unindexed: observed=1` for `corpus/lessons/round-53-verifier-spotcheck.md`, a tracked corpus file no FILE-column pattern of `corpus/README.md` covers (it landed with round 53's admission). Expected under this round's drift rule (no freshness work); flagging so the next round's baseline re-freeze also indexes that file.
- **D3 (minor, this row):** the self-test asserts finding ids but never an exit code (§2 caveat). Proposed fix (text): inside `self_test()`, exercise the verdict-to-code mapping on the existing tmpdir fixtures — call the CLI entry with `--baseline` pointing at a tmpdir baseline and assert 0 (agreeing) and 1 (drifting), assert 3 for a missing baseline, and assert `corpus_observations` on a missing directory raises `Inconclusive` (→ 2). All four mappings then carry self-test evidence, satisfying PROTOCOL § Self-test fully.

## Residual risk and verification gaps

- An uncaught crash (e.g. corrupt baseline JSON at line 1310, or a `UnicodeDecodeError` on a non-UTF-8 corpus file, neither of which is `OSError`/`Inconclusive`) exits 1 with a traceback, which the declared map reads as `failed` rather than could-not-evaluate. All declared codes are produced with the declared meanings, so the map cell holds, but an operator cannot distinguish crash-1 from drift-1 without reading stderr. A wrapper for those two error classes into `Inconclusive` (→ 2) would close it; recorded here, not patched.
- The 0-code run used a synthetic fixture repo + minimal baseline (sandbox only), not a clean state of the lane tree, because no lane state this round is green against the stale baseline. The mapping code path exercised is the same line 1351.
- The counter's docstring explicitly excludes "whether each declared exit code is really produced" and "whether gate-vs-probe is the right kind" from C2; both were closed here by execution, so the row has no unverified remainder beyond the D3/D1 items above.
