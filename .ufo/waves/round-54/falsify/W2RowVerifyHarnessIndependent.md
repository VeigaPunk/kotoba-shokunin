Result: HOLDS — row `verifiers/verify_harness_independent.py` is accurate on every cell; two review notes (freeze `checks`-map drift is silently ignored; `in-file` pinned-values cell under-specifies where the comparison truth lives), no cell break, no corrected row required.

Seat: KotobaR54.W2RowVerifyHarnessIndependent (leaf, no subagent dispatch).
Scope: C2 registry row for `verifiers/verify_harness_independent.py` as landed at `bf65974c7845a06d7ef621ad998c6378ff735cd5`; checked against the sandbox clone at tip `58db81c4465b0e9b07ef2485b87d8970683afac6` (verifier byte-identical between the two revs: `git log bf65974c..58db81c -- verifiers/verify_harness_independent.py` empty; `sha256sum` 54f9c95b… in clone).

All commands ran in the sandbox clone `/fast/scratch/hyaku/kotoba-r54/W2RowVerifyHarnessIndependent` (clean `git status` before/after), Python `-B` where the row says so. No lane, fleet or sibling files touched.

---

## Cell-by-cell verdict

### 1. Name — HOLDS
Row name `verifiers/verify_harness_independent.py` matches the blob directly under `verifiers/` at both revs (exists at bf65974c; `git cat-file -e` OK). Universe M = 24 (.py/.sh blobs, `git ls-tree` count), row present exactly once in `## Gate registry` (SKILL.md:476 at tip).

### 2. Kind — HOLDS
`gate`. The script reads live surfaces (`Substrate`, lines 152–231), derives 28 rows, and compares them against a freeze/observed table; a mismatch exits 1 with `DRIFT`/`DISAGREE`. It is a committed, rerunnable verdict script that can fail — a probe by contrast cannot fail. PROTOCOL.md § Gate standard ("A tool that cannot fail is a probe") is satisfied.

### 3. Entry command — HOLDS
`python3 -B verifiers/verify_harness_independent.py --freeze <file>` (bare `--json` only derives) — ran as specified:
- bare derive: exit 0, prints `24 derived, 4 scoped out, 0 unlanded (of 28 named checks)`;
- `--json`: exit 0, one JSON document, `checks`=28, `landed`=24, `scoped_out`=4;
- `--freeze <file>` with a matching freeze: exit 0, `freeze clean: 24 landed rows match the frozen table`;
- `--freeze <file>` with a drifted freeze: exit 1, names each drifted row (`DRIFT omp.offered.skills derived=10 frozen=99999`).
Read-only; no network; no writes (verified: no file changed in clone); each run finished in ~45–80 s (live catalogue carrier ≈ 6 GB / 6342 `.jsonl`, read once per process, memoised `_CATALOGUE_CACHE`, line 375).
No `--freeze` file is committed at HEAD that stays green (see note B). This is a usage/ops property, not a row defect: the gate itself is exercised green by its self-test.

### 4. Verdict map — HOLDS
Declared: `0=clean, 1=failed, 2=could-not-evaluate, 3=could-not-evaluate`. Produced and observed:
- 0 clean: freeze match (`return 0`, line 1819), `--observed` all agree, `--help` (argparse), bare/`--json`, `--self-test` pass;
- 1 failed: freeze drift (`return 1`, line 1816), observed disagreement (line 1791), self-test failures (line 1693);
- 2 could-not-evaluate: unreadable substrate (`SUBSTRATE …`, line 1736) and argparse usage errors (unknown option — argparse exit 2);
- 3 could-not-evaluate: missing/unparseable freeze (`FREEZE …`, lines 1803–1804) and unparseable `--observed` (`OBSERVED …`, lines 1774–1775).
No produced code is undeclared (0/1/2/3 all covered; `self_test()` and `main()` only ever return 0/1/2/3; no other `sys.exit`). Docstring ladder (lines 95–100) says usage errors are 3 but argparse actually exits 2 — harmless because both map to could-not-evaluate in the verdict map; the registry cell itself is faithful to the code.

### 5. Self-test — HOLDS
`--self-test` runs the script's genuine self-test `self_test()` (lines 1232–1693), not a nested call or usage text: it builds synthetic substrate trees in `tempfile.TemporaryDirectory`, asserts derived values, and runs the committed fixture battery (`fixture_battery`, lines 1178–1229) via subprocess invocations of the same CLI over `$TMPDIR` trees (no network, no live-tree writes). Observed: `0 failure(s) over 123 assertions`, exit 0, ~80 s. The flag text `--self-test` occurs in the file (line 1709) and is the script's own self-invocation mode.

### 6. Pinned values — HOLDS (with note B)
Cell: `in-file`. The script's expectation rules and constants are in-file: `TEMPLATE_START/END` (129–130), `PREVIEW_CLIFF`/`COMPRESS_MAX_CHARS/WORDS` (133–135), the `self_test()` assertion literals, plus committed fixture cases under `verifiers/fixtures/harness-independent/` (present at bf65974c; `git ls-tree` shows oc-config/oc-log/omp-cache/template-keys). `in-file` matches the convention used by sibling self-contained gates (`check_alwayson_boxes.py`, `verify_corpus_independent.py`, etc.). The counter's rule (pinned-values cell `none|in-file|exists-path`) passes. Caveat, note B: the gate's live comparison target is the caller-named freeze file, which is regenerated (`--write-freeze`), not a committed repo baseline; the only committed freeze in the repo (`.ufo/round-46/drafts/u1/round37-reproduce/ind-freeze.json`) drifts from today's host (`DRIFT` on 6 rows, exit 1). No cell break; suggest appending `verifiers/fixtures/harness-independent` to the cell for the repo-side expectation corpus.

### 7. Write scope — HOLDS
Script writes only to caller-named `--out` (line 1765) / `--write-freeze` (line 1795) targets and to temp dirs inside `self_test()`/`fixture_battery()` (`TemporaryDirectory`, lines 1189, 1243); `--freeze` is read-only. Nothing else writes (`grep`: writes confined to fixture builders under tmp roots). Docstring line 102 says "nothing is written outside --out / --freeze paths" — imprecise (should read `--write-freeze`), but the registry cell is correct.

### 8. Owner — HOLDS
`kotoba` matches OWNER in the counter and all sibling rows.

### 9. Gate vs probe — HOLDS
Gate, not probe: compares live derived rows against a freeze/observed table and returns 1 on any disagreement, naming the drifted rows; bare/`--json` without comparison merely derives (the parenthetical in the entry-command cell says exactly this). Verdict classes map exactly onto the declared ladder. The self-test exercises both exit-0 and exit-1 verdict paths (pristine control 0, each named mutant 1 — lines 1200–1229).

---

## Findings (severity-ordered)

**F1 (medium, gate blind spot — not a row defect).** Freeze drift is only detected from the `results` list; mutating the human-readable flat `checks` map is silently ignored. `flatten_observed` (lines 802–825) prefers `document["results"]` when present and only falls back to `checks`. Repro, both in the clone:
- `checks["omp.offered.skills"] = 99999` in a write-freeze snapshot → `freeze clean: 24 landed rows match the frozen table`, exit 0;
- same value into the `results` entry → `DRIFT omp.offered.skills derived=10 frozen=99999` / `frozen drift on 1 row(s)`, exit 1.
Any hand-edit or external tool updating the flat map (the natural "pinned values" view) will not make the gate red. Proposed fix (report text only): make the drift comparison read the same canonical key as `--write-freeze` writes, or verify `checks` and `results` agree before comparing, or document that only the `results` list is authoritative.

**F2 (low, documentation precision).** Docstring exit ladder (lines 95–100) states usage errors exit 3; argparse actually exits 2 (observed). Registry cell already maps both 2 and 3 to could-not-evaluate, so no row change needed. Suggest correcting the docstring ladder, not the row.

**F3 (low, ops/residual).** No committed fresh freeze at HEAD: the only committed freeze (round-46 draft) drifts against today's substrate, so a plain `--freeze <file>` invocation against it is red (exit 1, 6 drifted rows) until regenerated. The gate is ready when the lane keeps a regenerated freeze; the row's `in-file` cell does not signal that dependency. No severity beyond note.

---

## Verification gaps
- Live runs read the ~6 GB catalogue carrier (read-only); runtime ~45–80 s per invocation, comfortably inside bounds. No network calls, no paid model calls, no installs (no tooling changes to report).
- The three missing/exotic verdict paths (unparseable freeze/observed, unreadable substrate, unknown option) were exercised; all exit codes matched the map.
- The row presented in this report is identical at bf65974c and tip; no drift between the two revs.
