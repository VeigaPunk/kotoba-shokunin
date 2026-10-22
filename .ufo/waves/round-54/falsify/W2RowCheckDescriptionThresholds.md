Result: HOLDS — every cell of the `verifiers/check_description_thresholds.py` registry row was verified against observed behavior in a sandbox clone; no cell requires correction.

Attack target: SKILL.md § Gate registry row for `verifiers/check_description_thresholds.py`,
landed at bf65974c7845a06d7ef621ad998c6378ff735cd5 (row text byte-identical at bf65974:SKILL.md:446
and tip SKILL.md:460). Sandbox: `/fast/scratch/hyaku/kotoba-r54/W2RowCheckDescriptionThresholds`
at 58db81c4465b0e9b07ef2485b87d8970683afac6.

## Cell-by-cell

- **Name** — HOLDS. File exists; byte-identical between bf65974 and tip
  (`git diff bf65974 58db81c -- verifiers/check_description_thresholds.py` → 0 lines) and between the
  plan commit e3371548 and tip (frozen counter, diff empty).

- **Kind `gate`** — HOLDS. It reads surfaces (SKILL.md, the entry, SOURCES.md, the lesson via
  `git show` under `--rev` or `--root` files; check_description_thresholds.py:114-125, 410-417) and
  returns a verdict it can fail: `--rev 422ffd1082b3f4ae3ebda6060eb1a8d779f6dfd4` →
  `description thresholds backed 0 of 7 clients`, exit 1. Not a probe
  (PROTOCOL.md:391-392: a tool that cannot fail is a probe).

- **Entry command** — HOLDS. `python3 -B verifiers/check_description_thresholds.py --rev
  58db81c4465b0e9b07ef2485b87d8970683afac6` from the clone root → all 7 clients `BACKED`,
  last line `description thresholds backed 7 of 7 clients`, exit 0. `LANE` resolves from `__file__`
  (line 76), so `--rev` is cwd-independent; run from the row's stated root anyway.

- **Verdict map `0=clean, 1=failed, 2=could-not-evaluate`** — HOLDS. All declared codes produced with
  the declared meaning; no produced code missing:
  - 0 = clean: tip run, `backed 7 of 7` ≥ TARGET=4 (lines 81, 438-443) → exit 0.
  - 1 = failed: base-rev run → exit 1 (line 443).
  - 2 = could-not-evaluate: `--rev deadbeefdeadbeef` → `could-not-evaluate: git show
    deadbeefdeadbeef:SKILL.md failed: fatal: invalid object name 'deadbeefdeadbeef'.`, exit 2
    (lines 414-416). Usage errors also exit 2 via `ap.error` (lines 405, 408): bare invocation →
    exit 2; `--self-test --rev HEAD` → exit 2.
  - Only exit sites: `sys.exit(main())` (447), `self_test()` (391), `ap.error`→2 (405, 408);
    `-h` → argparse 0. No uncaught-exception path found: `r[0]` guarded at line 157, SOURCES row
    cells guarded by `len(c) == 13` at line 176, `HOSTS[client]` only iterated over `CLIENTS` (245).
    An uncaught Python exception would exit 1 (mislabeled "failed" rather than could-not-evaluate)
    but no reachable trigger was found [INFERENCE — no trigger constructed].

- **Self-test `--self-test`** — HOLDS as a literal claim. Flag exists (line 401) and runs the
  script's own in-memory assertion suite over `judge`/`host_ok`/`table_rows` (lines 307-391) — not a
  nested call or usage text (mutual exclusion enforced, line 404-405). Observed:
  `self-test: 0 failure(s) over 22 assertions`, exit 0. Gap vs the PROTOCOL self-test clause
  (PROTOCOL.md:398-402: "asserting both the exit code and a stable expected finding-id … over
  isolated fixtures"): the suite asserts judge outcomes only — no exit-code assertion, no fixture
  tree, no subprocess self-invocation. The cell is true; the script's self-test is weaker than the
  clause's stated shape. Script is frozen this round — recorded, not fixable here. A self-test
  failure exits 1 = failed, consistent with the map.

- **Pinned values `in-file`** — HOLDS. Every expected value is a module constant: CLIENTS/HOSTS
  (84-102), SKILL_HEADING/SKILL_HEADER/ENTRY_HEADING/ENTRY_HEADER (103-106), TARGET/OPENED/MAX_WORDS
  (81-83), regex pins (107-111). No baseline/pin file is read; the only file reads are the four
  judged inputs (`read_file`, 114-125). `in-file` is literally true.

- **Write scope `none; --fetch reads the network`** — HOLDS. Grep finds no write calls; the only
  I/O outside `git show`/file reads is `urllib.request.urlopen` (line 235) under `--fetch`, which is
  a plain GET. Sandbox runs left `git status --porcelain` clean. `-B` suppresses bytecode and no
  lane module imports this file (grep for importers: none), so no `.pyc` side effect. `--self-test`
  is pure in-memory — no fixtures, no temp files.

- **Owner `kotoba`** — HOLDS (uniform across the section; consistent with the lane id).

## Residual risks (no cell break; not in the row's cells)

- `--root /nonexistent-dir` exits 1 (`backed 0 of 7 clients`) — a missing input root reads as
  "failed", not "could-not-evaluate"; the declared map has no code covering it. The entry command
  uses `--rev`, which maps this class to 2 correctly (missing files → empty text → failed verdict,
  bad rev → 2).
- Under `--fetch` the same 0/1 is emitted on a second basis (`found`, lines 420-442) and a network
  exception is folded into `found=False` → exit 1 = failed rather than could-not-evaluate
  (lines 426-428). The plan calls `--fetch` "a second measurement", so the widened meaning of 1 is
  arguably intended, but the row's verdict map then covers two semantics.
- Registry preamble wording (SKILL.md:449, section-level, not this row): "what each one checks:
  `verifiers/README.md`" — the README has bullets for only 5 of the 24 registered verifiers
  (`check_substrate_pins.py`, `fault_injection_corpus.sh`, `verify_corpus_independent.py`,
  `verify_corpus_integrity.py`, `verify_harness_claims.py`); this script has no bullet there.

## Corrected row text

None — all cells hold; no correction proposed.

## Evidence commands (all in the sandbox clone unless noted)

- `python3 -B verifiers/check_description_thresholds.py --rev 58db81c4465b0e9b07ef2485b87d8970683afac6`
  → exit 0, `description thresholds backed 7 of 7 clients`.
- `python3 -B verifiers/check_description_thresholds.py --self-test` → exit 0,
  `self-test: 0 failure(s) over 22 assertions`.
- `python3 -B verifiers/check_description_thresholds.py --rev 422ffd1082b3f4ae3ebda6060eb1a8d779f6dfd4`
  → exit 1, `description thresholds backed 0 of 7 clients`.
- `python3 -B verifiers/check_description_thresholds.py --rev deadbeefdeadbeef` → exit 2,
  `could-not-evaluate: git show deadbeefdeadbeef:SKILL.md failed: fatal: invalid object name`.
- `python3 -B verifiers/check_description_thresholds.py` (no args) → exit 2, argparse usage error.
- `python3 -B verifiers/check_description_thresholds.py --self-test --rev HEAD` → exit 2, argparse
  mutual-exclusion error.
- `python3 -B verifiers/check_description_thresholds.py --root /nonexistent-dir` → exit 1,
  `backed 0 of 7`.
- `git diff e3371548..58db81c` and `git diff bf65974..58db81c` on the script → both empty.
- `git status --porcelain` after all runs → clean.
- `grep -rn 'check_description_thresholds' --include='*.py' .` → only the script itself.
- `grep` for write calls in the script → only `urlopen` (line 235).

No tools installed. Nothing executed outside the sandbox clone; no lane files modified (report file
excepted, per bounds).
