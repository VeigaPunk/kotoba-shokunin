# MutTesterDispatchR99 — new C1 mutants beyond the frozen set (round 99, wave r99-w1)

Seat: MutTesterDispatchR99 (mutation-tester, leaf; no subagent dispatch). Status: **complete** —
22 new mutants measured at the freeze and on the ExecArmsR99 candidate.

Instrument under test: `verifiers/verify_dispatch_prompts.py --self-test` (SKILL.md § Dispatch-prompt
fidelity checklist, boxes `dispatch.04` / `dispatch.08`), its live CLI (`run_checks`, `main`, the
exit-2 ladder, `read_text`), `box_proof`, `_file_result` and `dispatch_box_sha256`.

- **BASE**: freeze `b53e209603e7c480cd975ea543e415b66f695438`, instrument sha256
  `46bc97a6ce1de2c86b2f3782a30f7e09dbd24d4b0a35519260fc8c9b8b3b594a`, counter
  `verifiers/fixtures/round-99/selftest-kills.py` sha256
  `aff389533c966a668b477da11432ded511f24c31e80c5a108ff950a4f4af9be1`, honest self-test
  `0 failure(s) over 128 assertions`.
- **CANDIDATE**: freeze + `ExecArmsR99.patch` (sha256
  `9b705bc807855d0149a9eda9e2d45d2f024a34bb71606f99979f158f3f9af924`, equal to the sha256 in
  `ExecArmsR99_READY`), my scratch rev `787d531038e21371e70977c95c9d68ee840e5f74`, instrument sha256
  `749287b121f305b0d3958efb3954a0ef8c78681e341fe13a064400835d84bda4`, honest self-test
  `0 failure(s) over 154 assertions` (128 → 154, +26).
- The candidate is byte-exactly the READY patch on the freeze: `git -C "$D" diff --binary
  b53e2096 HEAD` normalises to the same 15124 bytes and the same sha256
  `ad087b479627466a0037032fb581988c7cf4486a7f6ab37272fbef9d139b38ed` as the patch file once its
  mnemonic diff prefixes (`c/`…`i/`, a git-config artifact of the builder) are rewritten to `a/`…`b/`.
  `git apply --check` passed before the apply; `git -C "$D" rev-parse --show-toplevel` = `$D`.

## Scope

Design ≥10 NEW mutants of the instrument's evaluation path that are not a row of
`CLAIMS["c1"|"r98c1"|"r97c1"|"r96c1"]` of `verifiers/fixtures/round-99/selftest-kills.py` and not
n01–n20 of `.ufo/waves/round-98/w1/MutTesterDispatchR98.md`; apply each with the counter's own method
and classify KILLED / RUN-ERROR / SURVIVED at the base AND on the candidate. Not a lane file, not a
patch, no lane write: measurements only, in `/fast/scratch/hyaku/kotoba-r99/MutTesterDispatchR99/`.

Checked mechanically against the 53 frozen rows (13 c1, 10 r98c1, 14 r97c1, 12 r96c1, 4 r95c1, each
including its positive): **0 exact duplicates** (no anchor+replacement pair repeats a frozen row).
Four anchor adjacencies are disclosed, each a different replacement and a different defect:

| mine | shares its anchor with | difference |
|---|---|---|
| m06-runchecks-reversed | c1 `t06-runchecks-first-only`, n07 | t06/n07 truncate to `wanted[:1]`; m06 reverses the order |
| m09-readtext-what-dropped | c1 `t09-readtext-oserror-empty`, n10 | t09/n10 return `""`; m09 keeps the raise and drops the `what` field |
| m19-l1-lane-nongreedy | c1 `t01-l1-suffix-unanchored`, n01 | t01/n01 remove the `$`; m19 makes the lane group non-greedy |
| m10-proof-cases-last-dropped | n17 | n17 keeps `cases[:1]`; m10 drops `cases[:-1]` |

## Method (the v6.1 counter's, imported not re-implemented)

`probe_r99.py` reads `verifiers/fixtures/round-99/selftest-kills.py` at REV into scratch and imports
`RUNNER`, `classify`, `code_decoy`, `NotEvaluated`, `DECOY_MARK` from that copy, then reproduces
rules 1–9:

- literal single-anchor substitution (`original.count(anchor) == 1`, line count preserved);
- **source-blind** run: mutant text compiled with the instrument's path and executed as `__main__`
  with argv `[path, --self-test]` while the file on disk holds the honest bytes;
- **mirror** run: the mutant text on disk;
- **fresh git-less world per run**: `git archive` of REV once, `cp -a --reflink=auto` per run, no
  `.git`; minimal child env (PATH, LANG, TMPDIR, HOME, XDG_CACHE_HOME, PYTHONDONTWRITEBYTECODE);
- **comment decoy** (replacement lines appended as `# r97-decoy` comments) and **code decoy**
  (mutated statement under `if __name__ == "__decoy__":`), each run with its own text on disk;
- shuffled order with an honest run first, last and at a random interior position;
- KILLED iff blind AND mirror are both REPORTED-FAILURE (exit 1, `self-test FAIL: ` line, last
  summary `N failure(s) over M assertions` with N ≥ 1); RUN-ERROR otherwise; a baseline that is not
  CLEAN makes the reading inconclusive.

`witness_r99.py` loads the honest and each mutated instrument as modules (no subprocess) and calls
the mutated function on the same fixture input, so every verdict-bearing survivor has an exhibited
input where honest and mutant disagree.

## Mutant table (22 new mutants, none in the frozen tables)

| id | anchor (literal, unique) | defect |
|---|---|---|
| m01-main-notdir-exit-zero | the not-a-directory `return 2` in `main()` | a missing prompts/state/fleet directory exits 0, not 2 |
| m02-main-env-error-exit-one | the `EnvError` handler's `return 2` in `main()` | a substrate error during the live run exits 1 (a content fail), not 2 |
| m03-main-json-exitcode-zero | `"exit_code": 2,` in the not-a-directory `emit_json` | the `--json` substrate-error payload reports `exit_code 0` while returning 2 |
| m04-main-argv-ignored | `args = build_parser().parse_args(argv)` | `main()` ignores its argv and parses an empty command line |
| m05-check-flag-not-repeatable | `--check`'s `action="append"` | the repeatable flag keeps only its last value (`args.check` is a `str`) |
| m22-main-dir-check-exists | `if not path.is_dir():` | a plain file passes the substrate check as a directory |
| m06-runchecks-reversed | `for cid in wanted:` | `run_checks` returns its results in reverse request order |
| m07-runchecks-else-04 | the `else` branch's `evaluate_dispatch_08` append | `run_checks` evaluates `dispatch.04` for every id, never `dispatch.08` |
| m08-readtext-latin1 | `return path.read_text(encoding="utf-8")` | every prompt decodes as latin-1 (mojibake, no decode error) |
| m09-readtext-what-dropped | the `EnvError` message in `read_text` | the substrate message drops the `what` argument (reporting-only) |
| m10-proof-cases-last-dropped | `for c in cases:` | `box_proof` skips the last fixture case of every box |
| m11-proof-na-arm-dropped | the `NA_ARM_CONJUNCT … and not na_ok` test | `box_proof` no longer requires the N/A-arm case |
| m12-proof-control-dropped | `if not control_ok:` | `box_proof` no longer requires an all-PASS control case |
| m13-proof-substrate-exit-one | `if substrate_error: return 2` | a fixture substrate error exits 1 (failed proof), not 2 |
| m14-proof-proven-threshold | `return 0 if proven == 2 else 1` | one proven box is enough for exit 0 |
| m15-proof-conjunct-first-only | `for n in CONJUNCTS.get(cid, ()):` | only the first named conjunct per box must be covered |
| m16-proof-cofail-widened | `allowed = ALLOWED_CO_FAIL.get(n, frozenset())` | the isolation rule is dropped: a case failing two conjuncts covers both |
| m17-lane-of-kind-swap | `return m.group("lane"), int(m.group("round")), "round"` | `lane_of` labels every round file as an L1 spawn file |
| m18-report-stem-truncated | the report-stem group `([^\s…]+)` | the stem is capped at three characters |
| m19-l1-lane-nongreedy | `L1_FILE_RE`'s `(?P<lane>.+)` | the L1 lane group is non-greedy |
| m20-file-result-last-conjunct-ignored | `if "FAIL" in statuses:` | a FAIL on the last conjunct no longer makes the file FAIL |
| m21-box-fenced-continuation | `if not line.strip() or j + 1 in opaque:` | a fenced line inside a box's continuation is hashed into the box text |

Anchors verified on both instruments before every run: **22 of 22 match exactly once at both
revisions**, every replacement keeps the line count, every text compiles (`probe-*.txt` line
`anchors: 22 of 22 match exactly once, line counts preserved`).

## Results — base vs candidate

Receipts `probe-base.txt` (seed `7135e690cd2d23f0`), `probe-cand.txt` (seed `8941ad1b55ede6b8`).
Honest bracket CLEAN 3 of 3 at both revisions (128 and 154 assertions); all 22 comment decoys and
all 22 code decoys HELD at both revisions.

**Base: KILLED 10, SURVIVED 11, RUN-ERROR 1. Candidate: KILLED 13, SURVIVED 8, RUN-ERROR 1.**

| id | base | candidate | evidence |
|---|---|---|---|
| m01-main-notdir-exit-zero | SURVIVED | SURVIVED | — |
| m02-main-env-error-exit-one | SURVIVED | SURVIVED | — |
| m03-main-json-exitcode-zero | SURVIVED | SURVIVED | — |
| m04-main-argv-ignored | RUN-ERROR | RUN-ERROR | no summary line: with argv dropped the run falls through to the LIVE fleet (`FAIL dispatch.08: evaluated 1219 — …`), so rule 1 reads RUN-ERROR |
| m05-check-flag-not-repeatable | SURVIVED | **KILLED** | 2 failures / 154: `r99-t08-main-check-ignored: main() with only --check dispatch.04 exits 0 when that check passes: got (1, 'FAIL dispatch.08: …' ×11)` and `… the run prints one result line` |
| m22-main-dir-check-exists | SURVIVED | SURVIVED | — |
| m06-runchecks-reversed | SURVIVED | **KILLED** | 1 failure / 154: `r99-t06-runchecks-first-only: run_checks of both checks returns both results: got ['dispatch.08', 'dispatch.04']` |
| m07-runchecks-else-04 | SURVIVED | **KILLED** | 2 failures / 154: `r99-t06-runchecks-first-only: … got ['dispatch.04', 'dispatch.04']` and `r99-t08-main-check-ignored: the same tree under --check dispatch.08 exits 1 …: got (0, 'PASS dispatch.04: …')` |
| m08-readtext-latin1 | SURVIVED | SURVIVED | — |
| m09-readtext-what-dropped | SURVIVED | SURVIVED | — |
| m10-proof-cases-last-dropped | **KILLED** | **KILLED** | 4 failures: e.g. `box proof: deleting d04-stem leaves the box unproven: got (0, 'boxes proven 2\n', '')` |
| m11-proof-na-arm-dropped | **KILLED** | **KILLED** | e.g. `box proof: deleting d08-missing-state leaves the box unproven: got (0, 'boxes proven 2\n', '')` |
| m12-proof-control-dropped | **KILLED** | **KILLED** | e.g. `box proof: deleting d04-control leaves the box unproven: got (0, 'boxes proven 2\n', '')` |
| m13-proof-substrate-exit-one | **KILLED** | **KILLED** | `box proof: a missing fixture directory is a substrate error: got (1, "box-proof: … No such file or directory …")` |
| m14-proof-proven-threshold | **KILLED** | **KILLED** | e.g. `box proof: deleting d04-placeholder leaves the box unproven: got (0, 'boxes proven 1\n', …)` |
| m15-proof-conjunct-first-only | **KILLED** | **KILLED** | e.g. `box proof: deleting d04-stem leaves the box unproven: got (0, 'boxes proven 2\n', '')` |
| m16-proof-cofail-widened | **KILLED** | **KILLED** | `box proof: a relabelled placeholder copy cannot cover the stem: got (0, 'boxes proven 2\n', '')` |
| m17-lane-of-kind-swap | **KILLED** | **KILLED** | `control: dispatch.08 verdict PASS: got None` / `control: dispatch.08 evaluated 1: got 0` |
| m18-report-stem-truncated | **KILLED** | **KILLED** | `control: dispatch.04 verdict PASS: … "report stem(s) kot != lane id 'kote'"` |
| m19-l1-lane-nongreedy | SURVIVED | SURVIVED | equivalent (see below) |
| m20-file-result-last-conjunct-ignored | **KILLED** | **KILLED** | `round above state: dispatch.08 FAIL: got {… 'verdict': 'PASS', … 'round_le_latest_dispatched': {'status': 'FAIL', …}}` |
| m21-box-fenced-continuation | SURVIVED | SURVIVED | latent (no committed input) |

The only base→candidate movement is **m05, m06, m07 SURVIVED → KILLED**: the round-99 `r99-t06` arm
compares the `run_checks` id list (kills the reversal and the else-branch mapping) and the
`r99-t08` arm asserts one result line and the `--check dispatch.08` exit code (kills the
non-repeatable parser). No other classification changes; no mutant moves the other way.

## Differential witnesses

Receipts `witness-base.txt`, `witness-cand.txt` (11 DIFFERS + 1 SAME at each revision; the two files
differ only in scratch paths and the rev line). Every verdict-bearing survivor:

| id | witness input | honest | mutant |
|---|---|---|---|
| m01 | `main()` with a plain file as `--prompts` | rc 2, `ERROR …: not a directory (prompts directory)` | rc 0, same message |
| m02 | `main()` on a prompts dir holding a mode-000 prompt (uid 1000) | rc 2, `ERROR …: Permission denied (prompt file)` | rc 1, same message |
| m03 | `main(["--json", …])` with a plain file as `--prompts` | rc 2, payload `exit_code: 2` | rc 2, payload `exit_code: 0` |
| m22 | `main()` with a plain file as `--prompts` | rc 2, `ERROR …: not a directory` | raises `NotADirectoryError: [Errno 20] Not a directory: …` |
| m08 | `read_text` on a UTF-8 file holding `café` | `"café\n"` | `"cafÃ©\n"` (latin-1) |
| m05 | `main(["--check","dispatch.04","--check","dispatch.08", …])` | rc 0, 2 lines, ids `[dispatch.04, dispatch.08]` | rc 0, **11** lines, ids `[dispatch.08] × 11` |
| m06 | `run_checks(…, ["dispatch.04","dispatch.08"])` | ids `[dispatch.04, dispatch.08]` | ids `[dispatch.08, dispatch.04]` |
| m07 | `run_checks(…, ["dispatch.08"])` | ids `[dispatch.08]` | ids `[dispatch.04]` |
| m04 | `main()` with argv naming tree A while the module defaults name tree B (A passes, B FAILs) | rc 0, both checks PASS | rc 1, `FAIL dispatch.08 … (filename_role_round_equal)` — it read the default tree |

Equivalent / no-verdict mutants:

- **m19-l1-lane-nongreedy — provably equivalent, not merely input-equivalent.** `^(?P<lane>.+)-L1\.md$`
  and `^(?P<lane>.+?)-L1\.md$` both split at the unique position where the end-anchored suffix
  `-L1.md` begins, so no name distinguishes them. Witness SAME on `a-L1-L1.md` (both `('a-L1', None,
  'l1')`) and `kote-L1.md` (both `('kote', None, 'l1')`). Do not admit it to a future target table.
- **m21-box-fenced-continuation — latent.** Witness DIFFERS: a box whose continuation carries a
  two-space fence hashes `276b0a3b…` honest and `d9e73d60…` mutant. No committed `SKILL.md` box
  carries a fenced line inside its continuation, so no committed input reaches it.
- **m09-readtext-what-dropped — reporting-only.** Same `EnvError`, same exit path; only the message
  loses `(prompt file)` (witness DIFFERS on the message text).
- **m03-main-json-exitcode-zero — output-only for the process contract.** The process exit code is 2
  under both; the machine-readable payload disagrees. No self-test assertion reads the JSON payload.
- **m04-main-argv-ignored — RUN-ERROR, not a survivor.** `parse_args([])` drops `--self-test`, so the
  instrument prints no summary line at all and rule 1 classifies RUN-ERROR. It carries no verdict.

## Findings

**F1 (main result).** The candidate closes 3 of the 11 base survivors — m05, m06, m07 — through its
new `r99-t06` / `r99-t08` arms, and 8 survive unchanged. 7 of my 7 `box_proof` bookkeeping mutants
(m10–m16) and the `_file_result` aggregation mutant (m20) are killed at the base already: the box
proof's case/coverage bookkeeping is the best-covered surface I probed.

**F2 (the exit-2 ladder is the sharpest remaining hole).** m01, m02 and m22 each change a
substrate-absence outcome and none is observed at the candidate. The candidate's `t09` arm tests
`read_text`'s `EnvError` **directly** (ExecArmsR99.md: "t09 mode-000 prompt → `EnvError`"), not
`main`'s handler, so m02 (an `EnvError` during the live run exits 1, indistinguishable from a content
fail) survives. m22 is worse than a wrong code: a plain file passes the `is_dir()` check and the run
dies with a `NotADirectoryError` traceback. Minimal arms for a future round: (a) `main()` with a
plain file as `--prompts` → rc 2; (b) `main()` with a mode-000 prompt → rc 2, not 1; (c)
`main(["--json", …])` on a plain file → payload `exit_code 2`. Each is a `rec(...)` assertion on
`main`'s return value with stdout captured in-process, which the candidate's arms already do.

**F3 (the parser's append semantics are killed only incidentally).** m05 dies because `--check
dispatch.04` under `action="store"` makes `list("dispatch.04")` eleven characters and the run prints
eleven `dispatch.08` lines — the `t08` arm's "one result line" assertion catches that, not the
append action itself. Likewise m06/m07 die because `t06` compares the id list. No arm names result
order or the check mapping as such; a future mutant that permutes results without changing the set
(e.g. a stable sort by id) would survive.

**F4 (a lost argv escapes the fixture world — and is unmeasurable).** m04 (`main()` parses `[]`
instead of its argv) does not merely break the entry point: with `--self-test` gone it falls through
to the live branch, whose defaults are the absolute fleet paths (`DEFAULT_PROMPTS =
/home/vgpnk/Projects/shokunin/.ufo/prompts`), and the mutant then evaluated the host's real 1219-file
prompt directory (`FAIL dispatch.08: evaluated 1219 — 1219 file(s) evaluated: 1180 PASS, 10 FAIL,
29 N/A; 14 out of scope`). It printed no `N failure(s) over M assertions` summary, so rule 1 returns
RUN-ERROR and the mutant can be neither killed nor scored. Two consequences: (a) a mutant that
breaks `main`'s argv handling is invisible to a self-test harness whose only entry is
`main([... "--self-test"])`; (b) the counter's rule 8 (git-less world) does not confine absolute
paths, so a mutant can read the host fleet during a scored run — read-only here, but the counter
cannot tell a read from a write. Both are counter/harness bounds, reported not rescued.

**F5 (decode path unobserved).** m08 (every prompt decoded as latin-1) survives: the self-test's
fixture prompt texts are pure ASCII (the instrument's only two non-ASCII characters are an em-dash in
a comment and one in the result-line format string, neither read through `read_text`), and `read_text`
has no decode-error arm. A non-ASCII report path would compare a mojibake stem against the lane id.
This is a coverage finding about the claim's scope (the C1 target list does not include it), not a
defect in the patch.

**F6 (equivalent mutant, no verdict).** m19 is provably equivalent (F above); it is not a coverage
finding and must not be promoted to a target.

## Bounds and risks

- Single-line (or up to three-line) literal substitutions only; multi-line restructuring defects are
  out of scope.
- The probe reuses the counter's `RUNNER`, so the counter's disclosed bounds apply unchanged; no
  mutant here is a self-sniffer, and none needs git, network, or an environment variable beyond
  TMPDIR/HOME.
- The m02 witness needs a non-root uid (this run is uid 1000); as root a mode-000 file is readable
  and the arm would read a false pass. The instrument's own `t09` arm carries the same guard.
- **Live-fleet read (disclosed).** The m04 mutant's blind and mirror runs fell through to the
  instrument's absolute default paths and read the host's real `/home/vgpnk/Projects/shokunin/.ufo/`
  prompts/state (1219 prompt files) — read-only, no write, no state kept. It is the one run in this
  probe that left the per-run world; every other run stayed inside its `git archive` copy. The
  counter's rule 8 does not confine absolute paths (see F4).
- Base and candidate readings use the same driver, anchors and scratch layout, so the delta is
  attributable to the patch alone.
- A surviving mutant is a coverage finding, not permission to change the contract: the frozen
  predicate, the counter and the builder's arms are untouched by this seat.
- No lane file, no `SKILL.md`, no corpus file, no frozen instrument; no git/jj write in the lane.
  The only git writes were inside `$D` (the scratch clone): `apply`, `add`, one scratch-identity
  commit.

## Verification log

- Candidate build: `git clone --shared` of the lane at the freeze, `git apply --check` OK, `git apply`,
  scratch-identity commit `787d531038e21371e70977c95c9d68ee840e5f74`; `git rev-parse --show-toplevel`
  = `$D`; the normalised candidate diff equals `ExecArmsR99.patch` byte for byte (sha256
  `ad087b479627466a0037032fb581988c7cf4486a7f6ab37272fbef9d139b38ed`).
- Anchors checked against both instruments before every run: 22 of 22 match exactly once, line
  counts preserved, every text compiles.
- `probe_r99.py base b53e2096 …` → KILLED 10, SURVIVED 11, RUN-ERROR 1; honest CLEAN 3 of 3 (128);
  comment decoys 22 of 22, code decoys 22 of 22; seed `7135e690cd2d23f0` (`probe-base.txt`).
- `probe_r99.py cand 787d5310 …` → KILLED 13, SURVIVED 8, RUN-ERROR 1; honest CLEAN 3 of 3 (154);
  comment decoys 22 of 22, code decoys 22 of 22; seed `8941ad1b55ede6b8` (`probe-cand.txt`).
- `witness_r99.py` at both revisions → 11 DIFFERS + 1 SAME (m19) each, identical modulo scratch paths
  and the rev line (`witness-base.txt`, `witness-cand.txt`).
- Receipt sha256 (full): `probe-base.txt`
  `dc17987d0dd157c16e76e4af8b5402c3d3ed979a4f8b6688b94a1bb88133731d`, `probe-cand.txt`
  `6267fec9744a4cf13d50689be9d998963ec057ee42d02fa3cd96ad4e4b679db8`, `witness-base.txt`
  `3f866a2f769f334ccb0378cce1fa947babdb4be991cac2622a91485f373d6f6e`, `witness-cand.txt`
  `e8fba053b14d4c109aebd83bbc00c36c7d612a009ade7d9edd0e7e6439e99287`, `probe_r99.py`
  `d0dda91c7ef1e74b2c706e014ccd5da9cb5fa8f997a1bf03cad310ccb03bc955`, `witness_r99.py`
  `73eedab57aa84cc41b52a0f66f0f36871c8a59f821325bd4eef91e315d1299dc`.
- Scratch `/fast/scratch/hyaku/kotoba-r99/MutTesterDispatchR99/` removed before yield.
- Tool installs: none needed.

## Files written

- `.ufo/waves/round-99/w1/MutTesterDispatchR99.md` (this report)
- `.ufo/waves/round-99/w1/MutTesterDispatchR99/probe_r99.py`, `witness_r99.py` (drivers)
- `.ufo/waves/round-99/w1/MutTesterDispatchR99/probe-base.txt`, `probe-cand.txt`,
  `witness-base.txt`, `witness-cand.txt` (receipts)
