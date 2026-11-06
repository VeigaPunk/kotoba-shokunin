# MutTesterDispatchR100 — new C1 mutants beyond the frozen set (round 100, wave r100-w1)

Seat: MutTesterDispatchR100 (mutation-tester, leaf; no subagent dispatch). Status: **complete** —
16 new mutants measured at the freeze and on the ExecArmsR100 candidate, each with a differential
witness at both revisions.

Instrument under test: `verifiers/verify_dispatch_prompts.py --self-test` (SKILL.md § Dispatch-prompt
fidelity checklist, boxes `dispatch.04` / `dispatch.08`), its live CLI (`main`, `run_checks`,
`emit_json`, `read_text`), `build_parser` and `box_proof`.

- **BASE**: freeze `03a98eb78b63bf9895cbe00ba0f3c8b0e53aa687`, instrument sha256
  `749287b121f305b0d3958efb3954a0ef8c78681e341fe13a064400835d84bda4` (the round-99 landing; the
  round-99 arms are already in it), counter `verifiers/fixtures/round-100/selftest-kills.py` sha256
  `220002289d06064b521f33a04dba25a3ba337fa310e32654a7b5822704b8c64c`, honest self-test
  `0 failure(s) over 154 assertions`.
- **CANDIDATE**: freeze + `ExecArmsR100.patch` (sha256
  `7b4e2dbc2450ebbc360c557897b9b60f0895005cd1d0d631b4dac1746c857e`, equal to the sha256 in
  `ExecArmsR100_READY`), built in my own scratch clone: rev
  `a2918960b82528783bd4650734894ca266115e05`, instrument sha256
  `78da1c4644421e5ccb48403cc3bb222ea474d2f28dc120cfb5acc63cc7d12eaf`, honest self-test
  `0 failure(s) over 168 assertions` (154 → 168, +14). `git diff --numstat` base→candidate is
  `144 0 verifiers/verify_dispatch_prompts.py`: insert-only, one hunk inside `self_test()`, no
  production line changed. The candidate reads `C1-PREDICATE-MET` (6 of 6) in my reproduction
  (`counter-c1-cand.txt`), so the revision I measured is the one the counter scores.

## Scope

Design ≥10 NEW mutants of the instrument's evaluation path that are not a row of
`CLAIMS["c1"|"r99c1"|"r98c1"|"r97c1"|"r96c1"]` of
`verifiers/fixtures/round-100/selftest-kills.py` and not m01–m22 of
`.ufo/waves/round-99/w1/MutTesterDispatchR99.md`; apply each with the counter's own method and
classify KILLED / RUN-ERROR / SURVIVED at the base AND on the candidate. Not a lane file, not a
patch, no lane write: measurements only, in `/fast/scratch/hyaku/kotoba-r100/MutTesterDispatchR100/`.

Checked mechanically against the 52 frozen DP rows (6 c1, 12 r99c1, 9 r98c1, 13 r97c1, 11 r96c1,
each including its positive): **0 exact duplicates** (no anchor+replacement pair repeats a frozen
row). Four anchor adjacencies are disclosed, each a different replacement and a different defect:

| mine | shares its anchor with | difference |
|---|---|---|
| w09-readtext-errors-replace | c1 `t05-readtext-latin1` | t05 decodes as latin-1; w09 keeps UTF-8 and adds `errors="replace"` |
| w10-runchecks-duplicate-first | c1 `t06-runchecks-sorted`, r99c1 `t06-runchecks-first-only` | t06 sorts, r99c1 truncates to `[:1]`, w10 appends a duplicate |
| w13-main-code-all-not-any | r99c1 `t07-main-fail-exit-zero` | t07 hard-codes 0; w13 turns `any` into `all` |
| w14-main-wanted-empty | r99c1 `t08-main-check-ignored` | t08 always runs all checks; w14 runs none |

## Method (the v6.2 counter's, imported not re-implemented)

`probe_r100.py` reads `verifiers/fixtures/round-100/selftest-kills.py` at REV into scratch and
imports `RUNNER`, `classify`, `code_decoy`, `NotEvaluated`, `DECOY_MARK` from that copy, then
reproduces rules 1–9:

- literal single-anchor substitution (`original.count(anchor) == 1`, line count preserved);
- **source-blind** run: the mutant text compiled with the instrument's path and executed as
  `__main__` with argv `[path, --self-test]` while the file on disk holds the honest bytes;
- **mirror** run: the mutant text on disk;
- **fresh git-less world per run**: `git archive` of REV once, `cp -a --reflink=auto` per run, no
  `.git`; minimal child env (PATH, LANG, TMPDIR, HOME, XDG_CACHE_HOME, PYTHONDONTWRITEBYTECODE);
- **comment decoy** (replacement lines appended as `# r97-decoy` comments) and **code decoy**
  (mutated statement under `if __name__ == "__decoy__":`), each run with its own text on disk;
- shuffled order with an honest run first, last and at a random interior position;
- KILLED iff blind AND mirror are both REPORTED-FAILURE (exit 1, a `self-test FAIL: ` line, last
  summary `N failure(s) over M assertions` with N ≥ 1); RUN-ERROR otherwise; a baseline that is not
  CLEAN makes the reading inconclusive.

`witness_r100.py` loads the honest and each mutated instrument as modules (no subprocess) and calls
the mutated function on the same fixture input, so every verdict-bearing survivor has an exhibited
input where honest and mutant disagree.

## Mutant table (16 new mutants, none in the frozen tables)

| id | anchor (literal, unique) | defect |
|---|---|---|
| w01-substrate-state-fleet-unchecked | the three-entry substrate loop in `main()` | the loop checks prompts three times: a plain file as `--state-dir` or `--fleet` passes the not-a-directory gate |
| w02-substrate-state-what-mislabeled | `(state_dir, "state directory"),` | the state-directory substrate error names the prompts directory (reporting-only) |
| w03-json-success-exitcode-zero | `"exit_code": code,` | the success `--json` payload reports `exit_code 0` on a run that exits 1 |
| w04-json-na-count-zero | the success payload's `"na": sum(...)` | the payload always reports `na 0` |
| w05-json-pass-count-zero | the success payload's `"pass": sum(...)` | the payload always reports `pass 0` |
| w06-json-fail-count-zero | the success payload's `"fail": sum(...)` | the payload always reports `fail 0` |
| w07-enverror-json-exitcode-zero | the EnvError `--json` payload | the payload reports `exit_code 0` while `main` returns 2 |
| w08-enverror-json-error-empty | the EnvError `--json` payload | the payload carries an empty error string (output-only) |
| w09-readtext-errors-replace | `return path.read_text(encoding="utf-8")` | invalid UTF-8 bytes decode to U+FFFD instead of raising `UnicodeDecodeError` |
| w10-runchecks-duplicate-first | `for cid in wanted:` | `run_checks` returns the first requested check a second time at the end |
| w11-parser-state-default-prompts | `--state-dir`'s default | a live run without `--state-dir` reads the prompts directory as state |
| w12-parser-check-choices-dropped | `--check`'s `choices=CHECK_IDS` | an unknown `--check` id is accepted and silently runs `dispatch.08` |
| w13-main-code-all-not-any | `code = 1 if any(...)` | the run exits 1 only when every check FAILs, not when any does |
| w14-main-wanted-empty | `wanted = list(args.check) if args.check else list(CHECK_IDS)` | a run with no `--check` evaluates nothing and exits 0 |
| w15-emit-json-sort-keys-off | `print(json.dumps(payload, indent=2, sort_keys=True))` | the `--json` payload is not key-sorted (output-only) |
| w16-parser-map-default-fixtures | `VERIFIERS_DIR / BASELINE_NAME` | the default `--box-proof` map path points into the fixtures directory |

Anchors verified on both instruments before every run: **16 of 16 match exactly once at both
revisions**, every replacement keeps the line count, every text compiles.

## Results — base vs candidate

Receipts `probe-base.txt` (seed `7c10cb38b68a660c`) and `probe-cand.txt` (seed `3bfab8176e26d4ac`).
Honest bracket CLEAN 3 of 3 at both revisions (154 and 168 assertions); all 16 comment decoys and
all 16 code decoys HELD at both revisions.

**Base: KILLED 3, SURVIVED 13, RUN-ERROR 0. Candidate: KILLED 3, SURVIVED 13, RUN-ERROR 0.**

| id | base | candidate | evidence |
|---|---|---|---|
| w01-substrate-state-fleet-unchecked | SURVIVED | SURVIVED | — |
| w02-substrate-state-what-mislabeled | SURVIVED | SURVIVED | — |
| w03-json-success-exitcode-zero | SURVIVED | SURVIVED | — |
| w04-json-na-count-zero | SURVIVED | SURVIVED | — |
| w05-json-pass-count-zero | SURVIVED | SURVIVED | — |
| w06-json-fail-count-zero | SURVIVED | SURVIVED | — |
| w07-enverror-json-exitcode-zero | SURVIVED | SURVIVED | — |
| w08-enverror-json-error-empty | SURVIVED | SURVIVED | — |
| w09-readtext-errors-replace | SURVIVED | SURVIVED | — |
| w10-runchecks-duplicate-first | **KILLED** | **KILLED** | base 3 failures / 154: `r99-t06-runchecks-first-only: … returns both results: got ['dispatch.04', 'dispatch.08', 'dispatch.04']`; candidate 4 failures / 168, adding `r100-t06-runchecks-sorted: run_checks returns results in request order: got ['dispatch.08', 'dispatch.04', 'dispatch.08']` |
| w11-parser-state-default-prompts | SURVIVED | SURVIVED | — |
| w12-parser-check-choices-dropped | SURVIVED | SURVIVED | — |
| w13-main-code-all-not-any | **KILLED** | **KILLED** | 1 failure / 154 and / 168: `r99-t07-main-fail-exit-zero: main() on a FAILing check exits 1: got (0, 'FAIL dispatch.04: …', '')` |
| w14-main-wanted-empty | **KILLED** | **KILLED** | base 2 failures / 154: `r99-t07-main-fail-exit-zero: … got (0, '', '')` and `… the run reports FAIL dispatch.04: got ''`; candidate 4 failures / 168, adding two `r100-t02-enverror-exit-one` failures (no check runs, so no `EnvError`) |
| w15-emit-json-sort-keys-off | SURVIVED | SURVIVED | — |
| w16-parser-map-default-fixtures | SURVIVED | SURVIVED | — |

**No mutant moves SURVIVED → KILLED.** The candidate's 14 new assertions close the six frozen
targets' surfaces (prompts substrate, `EnvError` exit, not-a-directory `--json` `exit_code`,
`is_dir`, UTF-8 decode, request order) and add incidental kill evidence for two already-killed
mutants (w10, w14), but they observe none of the 13 survivors.

## Differential witnesses

Receipts `witness-base.txt`, `witness-cand.txt`: **16 DIFFERS, 0 SAME, 0 skipped at each revision**
(the two files differ only in scratch paths and the instrument line). Every one of the 16 mutants
has an exhibited input where the honest and mutated modules disagree.

| id | witness input | honest | mutant |
|---|---|---|---|
| w01 | `main()` with a plain file as `--state-dir` | rc 2, `ERROR …: not a directory (state directory)` | rc 0, `PASS dispatch.04 …` (the file is never checked) |
| w02 | same input | message names `(state directory)` | message names `(prompts directory)` |
| w03 | `main(["--json", …])` on a tree whose `dispatch.04` FAILs | rc 1, payload `exit_code 1` | rc 1, payload `exit_code 0` |
| w04 | `main(["--json", …])` on a tree with no state baseline | payload `na 1`, statuses `['PASS', 'N/A']` | payload `na 0`, same statuses |
| w05 | `main(["--json", …])` on a PASSing tree | payload `pass 2` | payload `pass 0` |
| w06 | `main(["--json", …])` on the FAILing tree | payload `fail 1` | payload `fail 0` |
| w07 | `main(["--json", …])` with a mode-000 prompt (uid 1000) | rc 2, payload `exit_code 2` | rc 2, payload `exit_code 0` |
| w08 | same input | payload `error` = the permission message | payload `error` = `""` |
| w09 | `read_text` on a file holding `caf\xe9` | raises `UnicodeDecodeError` | returns `'caf\ufffd\n'` |
| w10 | `run_checks(…, ["dispatch.04","dispatch.08"])` | ids `[dispatch.04, dispatch.08]` | ids `[dispatch.04, dispatch.08, dispatch.04]` |
| w11 | `main()` with no `--state-dir` (module defaults patched to the fixture tree) | rc 0, `PASS dispatch.08` | rc 0, `N/A dispatch.08` (state read from prompts) |
| w12 | `main(["--check","dispatch.09", …])` | `SystemExit(2)`, `invalid choice: 'dispatch.09'` | rc 0, runs `dispatch.08` |
| w13 | `main()` on one FAIL + one PASS | rc 1 | rc 0 |
| w14 | `main()` with no `--check` | rc 0, two result lines | rc 0, no result line |
| w15 | `emit_json({"b":1,"a":2})` | `{"a": 2, "b": 1}` | `{"b": 1, "a": 2}` |
| w16 | `main(["--box-proof"])` with `VERIFIERS_DIR`/`FIXTURES_DIR` patched to a copied tree | rc 0, `boxes proven 2` | rc 2, `cannot read the box map …/fixtures/dispatch-prompts/checklist-baseline.json` |

## Findings

**F1 (main result).** 13 of the 16 new mutants survive at `03a98eb7` **and at the candidate** — the
round-100 patch moves none of them. The three that die do so through round-99 arms (w10 via
`r99-t06`, w13 and w14 via `r99-t07`); the new `r100-t06` and `r100-t02` arms add kill evidence for
w10 and w14 but no new coverage of a surviving surface. The self-test's 168 assertions still do not
observe the `--json` payload, the state/fleet substrate entries, the parser defaults/choices,
`read_text`'s error mode or `emit_json`'s serialisation.

**F2 (the `--json` payload is unobserved except one field).** w03 (success `exit_code`), w04/w05/w06
(the `na`/`pass`/`fail` counts), w07 (the EnvError payload's `exit_code`) and w08 (its `error` text)
all survive both revisions. The frozen c1 target t03 closes only the *not-a-directory* payload's
`exit_code`; the success payload and the EnvError payload stay open. Minimal arms:
`main(["--json", …])` on a FAILing tree → parse the payload, assert `exit_code == 1` and `fail == 1`;
on a mode-000 prompt → assert `exit_code == 2` and a non-empty `error`. Both are `rec(...)`
assertions on `main`'s captured stdout, the shape the round-99 and round-100 arms already use.

**F3 (the substrate loop checks only `--prompts` in practice).** w01 shows that a plain file as
`--state-dir` passes the not-a-directory gate and the run proceeds (rc 0, `PASS dispatch.04`). The
frozen t01/t04 targets and the new `r100-t01`/`r100-t04` arms exercise the prompts entry only; the
state and fleet entries are unobserved. Minimal arm: `main()` with a plain file as `--state-dir` →
rc 2 and a `not a directory` line.

**F4 (parser defaults and choices are dead code under the harness).** w11 (`--state-dir` defaulting
to the prompts dir), w12 (`--check` without `choices`) and w16 (the `--box-proof` default map path)
all survive: the self-test always passes explicit paths and valid check ids. w16's witness shows the
default is load-bearing (`--box-proof` with no `--map` reads `boxes proven 2` honest, `cannot read
the box map` mutant), so this is real behaviour, not a cosmetic one.

**F5 (decode error mode, the other side of t05).** w09 turns a `UnicodeDecodeError` on a non-UTF-8
byte into a silent `\ufffd` substitution. The frozen t05 changes the *encoding* (latin-1); w09 keeps
UTF-8 and changes the *error mode*. The self-test's fixtures are ASCII, so neither was observed by a
base arm; t05 is closed by the round-100 patch, w09 is not.

**F6 (output-only and consumer-only survivors, named not promoted).** w02 (message label), w08
(error text) and w15 (key order) change no exit code and no verdict a consumer reads. w04/w05/w06
change counts a `--json` consumer reads but not the exit code; they are verdict-bearing only for a
payload consumer, on the same rationale that admitted the frozen m03. None is promoted to a target
here — a surviving mutant is a coverage finding, not permission to change the contract.

**F7 (equivalence).** None of the 16 is provably equivalent: every one has a `DIFFERS` witness at
both revisions. w15 is the closest to output-only — JSON key order is not semantic for a consumer —
but the emitted bytes differ, so it is not an equivalent mutant.

## Bounds and risks

- Single-line (or up to three-line) literal substitutions only; multi-line restructuring defects are
  out of scope.
- The probe reuses the counter's `RUNNER`, so the counter's disclosed bounds apply unchanged; no
  mutant here is a self-sniffer, and none needs git, network, or an environment variable beyond
  TMPDIR/HOME.
- The w07/w08 witness needs a non-root uid (this run is uid 1000); as root a mode-000 file is
  readable and the case prints a skip instead of a false pass.
- w11's witness patches the module's `DEFAULT_PROMPTS`/`DEFAULT_STATE_DIR` globals after load, so no
  case reads the host fleet; w16's witness copies the committed map, `SKILL.md` and fixtures into the
  scratch tree for the same reason.
- No lane file, no `SKILL.md`, no corpus file, no frozen instrument; no git/jj write in the lane. The
  only git writes were inside my scratch clones: `checkout`, `apply`, one scratch-identity commit.
  The lane's instrument bytes at `03a98eb7` are unchanged (sha256 `749287b1…`), and the lane working
  tree was not modified by this seat.

## Verification log

- Scratch clone at the freeze: `git clone --shared`, `checkout 03a98eb7…`,
  `git rev-parse --show-toplevel` = `/fast/scratch/hyaku/kotoba-r100/MutTesterDispatchR100/repo`.
- Anchor check: `16 of 16 match exactly once, line counts preserved`; every mutant text compiles.
- `probe_r100.py base 03a98eb7… repo --full --seed 7c10cb38b68a660c` → KILLED 3, SURVIVED 13,
  RUN-ERROR 0; honest CLEAN 3 of 3 (154); comment decoys 16 of 16, code decoys 16 of 16
  (`probe-base.txt`).
- Candidate build: `git apply --check` OK, `git apply`, scratch-identity commit
  `a2918960b82528783bd4650734894ca266115e05`; `git diff --numstat 03a98eb7… HEAD` =
  `144 0 verifiers/verify_dispatch_prompts.py`; instrument sha256 `78da1c46…`.
- `probe_r100.py cand a2918960… cand --full` → KILLED 3, SURVIVED 13, RUN-ERROR 0; honest CLEAN 3 of
  3 (168); decoys 16 of 16 and 16 of 16 (`probe-cand.txt`).
- `witness_r100.py` at both revisions → 16 DIFFERS, 0 SAME, 0 skipped each (`witness-base.txt`,
  `witness-cand.txt`).
- Counter cross-checks on my own clones: `selftest-kills.py c1 03a98eb7… repo` →
  `C1 targets killed 0 of 6 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held
  6 of 6; code decoys held 6 of 6` → `C1-PREDICATE-UNMET` rc 1 (`counter-c1-base.txt`, matches
  `receipts/redbefore-c1-base.txt`); `… c1 a2918960… cand` → `C1 targets killed 6 of 6 (run errors
  0); … C1-PREDICATE-MET` rc 0 (`counter-c1-cand.txt`).
- Receipt sha256 (full): `probe_r100.py`
  `1af6d11207068c208ccb6e754693d4a53707efe76b3195399f0e11d6e97179f6`, `witness_r100.py`
  `795242ca8174d934a85fa32bf748b3421a87c1bd3575de86d7d1577b9bc627c3`, `probe-base.txt`
  `570e1051f706bd0f01be90898e907ff5aa75d4b99f8afbb5b03befc31b0cce2d`, `probe-cand.txt`
  `cf81a3071b39c7d62d86a72ea5b4ee74d3b48de83540cf2294258ba94bf1e27c`, `witness-base.txt`
  `32df645c4191bcf506668099b0d5dbc5daab5be18166e676ae12b26b7e55ae19`, `witness-cand.txt`
  `5a984dbca63e7f1071608b0e8b57d70a87745c95f9b6ee2b1f5e4482c92551ad`, `counter-c1-base.txt`
  `e0bde647d3d5a509279c743b21bea8b8a4874eb85486be44fd1379d8237cb564`, `counter-c1-cand.txt`
  `b7c8a1663445b9d6afaac218bafe024caf95c3fbda70145b02dee373f96b6684`.
- Scratch `/fast/scratch/hyaku/kotoba-r100/MutTesterDispatchR100/` removed before yield.
- Tool installs: none needed.

## Files written

- `.ufo/waves/round-100/w1/MutTesterDispatchR100.md` (this report)
- `.ufo/waves/round-100/w1/MutTesterDispatchR100/probe_r100.py`, `witness_r100.py` (drivers)
- `.ufo/waves/round-100/w1/MutTesterDispatchR100/probe-base.txt`, `probe-cand.txt`,
  `witness-base.txt`, `witness-cand.txt`, `counter-c1-base.txt`, `counter-c1-cand.txt` (receipts)
