Result: HOLDS — all eight cells of the gate registry row for verifiers/verify_corpus_independent.py hold under attack; the gate is RED at tip (exit 1) because the wave-1 C1 entry cites a foreign commit hash unresolvable in the lane object store, which is a verified corpus defect, not a row defect.

# Scope

Row attacked (SKILL.md:472, as landed at bf65974c7845a06d7ef621ad998c6378ff735cd5):

| `verifiers/verify_corpus_independent.py` | gate | `python3 -B verifiers/verify_corpus_independent.py` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | self-test fixtures under `$TMPDIR` | kotoba |

Sandbox: /fast/scratch/hyaku/kotoba-r54/W2RowVerifyCorpusIndependent at 58db81c4465b0e9b07ef2485b87d8970683afac6 (clone of the lane; no writes made to the lane). All commands below ran in the sandbox unless stated.

# Cell verdicts

## 1. Entry command — HOLDS (but RED at tip)

`python3 -B verifiers/verify_corpus_independent.py` (repo root, sandbox):

- exit 1 (`failed`), last lines: `corpus.pointers.commit_unresolvable    zero     observed=1 DRIFT` and `exit 1`.
- The single drift row: `corpus/knowledge/skill-listing-thresholds-round54.md:43: 451a02ff` (commit citation).
- Read-only: `git status --porcelain` empty and no `__pycache__`/`*.pyc` after the run; the script uses only `git ls-files` / `git cat-file -e` (read-only) plus file reads of tracked corpus md files (source lines 65–68, 86, 436).
- The failure is real, not a sandbox artifact: the same check in the lane object store fails (`git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin cat-file -e '451a02ff^{commit}'` → exit 128 "Not a valid object name"). The lane run would produce the identical drift (same corpus, same object store; the only sandbox-vs-lane difference is the worktree HEAD text, which does not change the verdict).
- Cross-instrument agreement: `verifiers/verify_corpus_integrity.py` (primary instrument) reports the same `commit_unresolvable: corpus/knowledge/skill-listing-thresholds-round54.md:43: 451a02ff` (5/9 checks pass; the verifier itself exits 0 as a reporting tool — not part of this row).
- C1 provenance: the citation landed in commit 5a097e12b9409a1f425fbc76334f36f1402eb4cc, line 55 of the new entry: `commit `451a02ff`` (Gemini CLI loader read at that hash). The gate's COMMITS class resolves citations against the *lane* repo (`git -C <repo> cat-file -e <token>^{commit}`, source line 436); `451a02ff` is a foreign (Gemini CLI sources) hash that is not in the lane object store, so it is unresolvable by this gate by design.

This is a finding for the C1 row seat/L1: either the cited object must be present in the lane object store, or the citation should be quoted context (double-quoted, per the COMMITS quirk: fully-inside-double-quotes citations are CONTEXT, source lines 27–28, 429–431) so it is not counted as a promise. The same text appears at C1 entry line 43 and lesson text line 40.

## 2. Self-test flag — HOLDS (isolation caveat below)

`python3 -B verifiers/verify_corpus_independent.py --self-test` (sandbox):

- Exit 0; last line `self-test: 93 assertions, 0 failures`; 93 `ok` lines.
- It is the script's own self-test: `--self-test` maps to the in-file `self_test()` (source lines 1006–1010, 703–993); no usage text, no nested invocation of another script. The nested `subprocess.run` calls re-invoke *this same file* on fixtures (lines 973–985) — still this script's own self-test, and those subprocess runs also pass (assertions 90–93).
- Fixtures are isolated under `tempfile.mkdtemp(prefix="corpus-independent-selftest-")` (line 705) and removed in `finally` (line 991); no network use (no socket/urllib/requests); `git init`/`git commit` happen only inside those temp fixture repos.
- Isolation caveat (defect in the self-test artifact, not a cell break): the bare-pointer dead fixture (`_fixture_pointers` dead `e.md`, lines 650–660, 883–889) exercises `report_pointer_exists` with the default `FLEET_ROOT` (module constant `/home/vgpnk/Projects/shokunin`, lines 43, 213–218) because `analyse_pointers(proot, corpus_markdown(proot))` (line 872) does not pass `fleet_root`. So the self-test verdict depends on the live fleet root: today `/home/vgpnk/Projects/shokunin/.ufo/reports/round-9/e.md` does not exist and the test passes; if the fleet root ever gains `round-9/e.md`, the same lane code would fail its own self-test without any lane change. The Gate standard § Self-test requires "isolated fixtures (temp trees, no network, no live-tree write)". Proposed fix (report text only): pass `fleet_root=os.path.join(tmp, "home")` or another temp root in the self-test call at line 872 (as the fleet-fallback assertions already do at lines 916–918), so the fixture is host-independent.

## 3. Verdict map / exit codes — HOLDS

Declared map `0=clean, 1=failed, 2=could-not-evaluate` is exactly the produced set; all paths verified from source and empirically:

- 0=clean: `exit_code()` returns 0 iff `violations()` == 0 (lines 504–511); verified at `ok 85`/`ok 86` and `cli: clean fixture exits 0` (assertions 90–91, 977).
- 1=failed: `exit_code()` returns 1 on any violation (lines 506–511); verified live at tip (above) and `cli: drifting fixture exits 1` (assertions 92, 983). Unhandled Python exceptions also exit 1 (`sys.exit(main())`, line 1023; interpreter exit 1 on traceback) — this maps unhandled crashes to `failed`, which is a defensible fail-closed reading, though not explicitly documented in the docstring; worth noting but not a break of the declared three-code map.
- 2=could-not-evaluate: `EnvError` → `main` returns 2 (lines 1011–1015); verified: `--repo /tmp/vci-nogit` (non-git dir) → `environment unreadable: not a git repository` exit 2; `--repo /nonexistent-xyz` → same, exit 2; `--bogus-flag` (argparse error) → exit 2. No other exit code is produced by the script (grep of all `return <int>`/`sys.exit` sites: 0/1/2 only).

## 4. Pinned values — HOLDS (`in-file` true)

- The gate's expected values are hard-coded in the script: the six zero-violation classes `CHECK_IDS` with mode `zero` (lines 45–55, 479–497) and `_v/ == 0 → PASS` (lines 500–501); the docstring's spec (lines 10–28) is also in-file. No baseline/pinned external file is read; the only file reads are the corpus md files being analysed (lines 271–275, 392–393, 423–425).
- Caveat: expected values are in-code, and the self-test asserts them against fixtures (assertions 85–89, 951–954), which satisfies the "in-file" cell. The gate's verdict also consults the live fleet root `/home/vgpnk/Projects/shokunin/.ufo/reports/` for bare report tokens (lines 213–218); that is a read-side oracle, not a pinned-value file, so it does not change the `in-file` classification, but it is a mutability risk under PROTOCOL Two Evidences (no frozen baseline for that input). Residual risk, not a cell break.

## 5. Write scope — HOLDS

- Main analysis path writes nothing (verified by `git status --porcelain` clean after both runs; source write sites are only `_write`/`os.makedirs` inside self-test fixtures, lines 576–589, 591–700).
- Self-test writes are confined to `$TMPDIR` (`mkdtemp`, line 705) and removed (line 991). Cell `self-test fixtures under `$TMPDIR`` is accurate.
- Minor wording nit: the cell does not say "(removed)", unlike sibling rows; not a break.

## 6. Gate vs probe — HOLDS (gate)

- It can fail: exit 1 on violations (verified live at tip); it reads surfaces (the corpus) and compares against expected values (zero-violation classes, in-file). Per PROTOCOL § Gate standard, this is a gate, not a probe. Kind cell `gate` is right.

## 7. Owner cell — HOLDS

`kotoba` (line 472 tail), matches OWNER pinned in the counter (check_gate_registry.py:65).

## 8. Counter conformance — HOLDS

`python3 -B verifiers/check_gate_registry.py --rev 58db81c4465b0e9b07ef2485b87d8970683afac6` → `gate registry rows conformant 24 of 24 lane verifiers; phantom 0`, exit 0. The attacked row is one of the 24 OK rows.

# Findings (severity order)

1. [HIGH, corpus/C1, not a row defect] Gate is RED at tip: `451a02ff` cited in `skill-listing-thresholds-round54.md:43` is unresolvable in the lane object store (`cat-file -e` exit 128). Both instruments agree (`verify_corpus_independent.py` exit 1; `verify_corpus_integrity.py` `commit_unresolvable` DRIFT). The wave-1 C1 Gemini CLI entry cites a foreign (Gemini CLI sources) commit under the gate's COMMITS class, which resolves only against the lane repo. Proposed fix for L1/C1 row seat: cite a lane-object-store commit, or make the citation quoted context (double quotes) so it is excluded as CONTEXT; or, if the foreign source hash must be recorded, record it outside commit-citation syntax.
2. [MED, self-test artifact] Self-test isolation leak: the bare-dead-pointer fixture consults the real `FLEET_ROOT` because `analyse_pointers` is called without `fleet_root` (line 872). Passes today (`round-9/e.md` absent from the fleet root); could fail spuriously if the fleet root changes. Proposed fix: pass a temp `fleet_root` (e.g. `os.path.join(tmp, "home")`) in the self-test call.
3. [LOW, wording] Script docstring (line 30) says `2 environment unreadable`, and unhandled Python exceptions exit 1 (`failed`); both are consistent with the declared map, but the docstring does not mention the crash→1 mapping. Not a break.

# Residual risk / verification gaps

- The verdict depends on the live fleet root (external mutable surface) with no frozen baseline; the registry schema and this row capture only write scope, not read scope, so this is a design residual, not a row lie.
- I did not re-run the gate against the *lane* working tree (bounds: run code only in the sandbox clone); the lane-vs-sandbox verdict is identical by construction (same corpus content, same object store, verdict independent of worktree position), and the object-store check was run read-only in the lane.

No cell broke, so no corrected row text is proposed; the row as landed is conformant and accurate. File the two findings above for L1.
