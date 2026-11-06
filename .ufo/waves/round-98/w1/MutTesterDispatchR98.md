# MutTesterDispatchR98 — new C1 mutants beyond the frozen set (round 98, wave r98-w1)

Seat: MutTesterDispatchR98 (mutation-tester, leaf; no subagent dispatch). Status: **complete** —
20 new mutants measured at the base and on the candidate.

Instrument under test: `verifiers/verify_dispatch_prompts.py --self-test` (SKILL.md § Dispatch-prompt
fidelity checklist, boxes `dispatch.04` / `dispatch.08`).

- BASE: freeze `63cd48d9de2c44eb40691ca05d3a41cc2f9a3248`, instrument sha256
  `1e67db315d22b41cfe4760983708af7815860a926f6ad5f9f25137d12110690f`, honest self-test
  `0 failure(s) over 105 assertions`.
- CANDIDATE: freeze + `ExecArmsR98.patch` (sha256 `27b412a58bf7583beb3d47013903a9d47203374b7ca0e1843aff816b90ffa6bf`,
  equal to the sha256 in `ExecArmsR98_READY`), my scratch rev `67b11243dead375d62935685b34e64a4d691593b`,
  instrument sha256 `de7c0074b0284afafe2b5d9e1dafcf6e95eadaf7083c119025aedcf8707c9009`, honest self-test
  `0 failure(s) over 128 assertions`. `git -C cand diff 63cd48d9 HEAD -- verifiers/verify_dispatch_prompts.py`
  hashes to the same `27b412a5…` — the candidate is byte-exactly the READY patch on the freeze.

## Scope

Design ≥10 NEW mutants of the instrument's evaluation path that are not t01..t09/p00 of the round-98
`CLAIMS["c1"]` table, not any row of `r97c1`/`r96c1`, and not m20-m34 of
`.ufo/waves/round-97/w1/MutTesterDispatchR97.md`; apply each with the v6 counter's own method and
classify KILLED / RUN-ERROR / SURVIVED at the base AND on the candidate. Not a lane file, not a patch,
no lane write: measurements only, in `/fast/scratch/hyaku/kotoba-r98/MutTesterDispatchR98/`.

## Method (the v6 counter's, imported not re-implemented)

`probe_r98.py` reads `verifiers/fixtures/round-98/selftest-kills.py` at REV into scratch and imports
`RUNNER`, `classify`, `code_decoy`, `NotEvaluated`, `DECOY_MARK` from that copy, then reproduces
rules 1-9:

- literal single-anchor substitution (`original.count(anchor) == 1`, line count preserved);
- **source-blind** run: mutant text compiled with the instrument's path and executed as `__main__`
  with argv `[path, --self-test]` while the file on disk holds the honest bytes;
- **mirror** run: the mutant text on disk;
- **fresh git-less world per run**: `git archive` of REV once, `cp -a --reflink=auto` per run, no
  `.git`; minimal child env (PATH, LANG, TMPDIR, HOME, XDG_CACHE_HOME, PYTHONDONTWRITEBYTECODE);
- **comment decoy** (replacement lines appended as `# r97-decoy` comments) and **code decoy**
  (mutated statement under `if __name__ == "__decoy__":`), each run with its own text on disk;
- shuffled order with an honest run first, last and at a random interior position;
- KILLED iff blind AND mirror are both REPORTED-FAILURE (exit 1, `self-test FAIL: ` line, last summary
  `N failure(s) over M assertions` with N >= 1); RUN-ERROR otherwise; a baseline that is not CLEAN
  makes the reading inconclusive.

`witness_r98.py` loads the honest and each mutated instrument as modules (no subprocess) and calls the
mutated function on the same fixture input, so every verdict-bearing survivor has an exhibited input
where honest and mutant disagree.

## Mutant table (20 new mutants, none in the frozen tables)

| id | anchor (literal, unique) | defect |
|---|---|---|
| n01-l1-suffix-unanchored | `L1_FILE_RE = re.compile(r"^(?P<lane>.+)-L1\.md$")` | the L1 name regex is not end-anchored: `kote-L1.md.bak` names a spawn file |
| n02-role-round-above | `        elif rr != round_n:` | a role-line round ABOVE the file-name round passes |
| n03-proof-map-hash-unenforced | `        if entry.get("text_sha256") != pinned:` | the map's `text_sha256` pin is not compared |
| n04-proof-missing-skill-as-pinned | `        live = {}` | a missing/unreadable SKILL.md is treated as hashing to the pins |
| n05-proof-verdict-mismatch-unenforced | `            if f["verdict"] != c.get("expect_verdict"):` | a case whose observed verdict differs from its expected verdict passes |
| n06-proof-conjunct-status-unenforced | `                if status != c.get("expect_conjunct_status", "FAIL"):` | a case's named-conjunct expected status is not compared |
| n07-runchecks-first-check-only | `    for cid in wanted:` | `run_checks` evaluates only the first requested check |
| n08-main-fail-exit-zero | `    code = 1 if any(r["status"] == "FAIL" for r in results) else 0` | a FAILing live check exits 0 |
| n09-main-check-ignored | `    wanted = list(args.check) if args.check else list(CHECK_IDS)` | `--check` is ignored |
| n10-readtext-oserror-empty | `        raise EnvError("%s: %s (%s)" % (path, exc.strerror or exc, what))` | an unreadable prompt file reads as empty text |
| n11-verdict-of-prefix | `        if f["file"] == fname:` | the verdict lookup matches a prefix, so a longer name shadows the exact one |
| n12-report-stem-dotdot | `        if not stem or stem in (".", ".."):` | (dead branch — see equivalents) |
| n13-map-duplicate-first-wins | `        entries[e.get("box_id")] = e` | a duplicate box entry keeps the FIRST entry instead of the last |
| n14-finish-fails-nas | `    if fails:\n        status = "FAIL"` | a check with a FAILing file and an N/A file reads N/A, not FAIL |
| n15-outofscope-nonmd-evaluated | `        lane, _round, kind = lane_of(name)\n        if lane is None:` | a name that is not a dispatch-prompt name and does not end `.md` is evaluated instead of listed out of scope |
| n16-box-section-ignored | `        if not bm or section != DISPATCH_SECTION:` | every checklist box in SKILL.md is hashed, not only the dispatch section |
| n17-proof-case-first-only | `        for c in cases:` | only the first fixture case per box is evaluated |
| n18-finish-na-count-zero | `    nas = [f for f in files if f["verdict"] == "N/A"]` | the detail counts N/A files as PASS (reporting-only) |
| n19-state-baseline-exists | `    if base.is_file():` | a DIRECTORY named `<lane>.report-baseline` counts as a baseline |
| n20-box-ninth-limit | `        if len(out) < len(BOX_ORDER):` | the nine-box cap is dropped (a tenth dispatch box raises IndexError) |

Anchors verified against the base instrument and the candidate: 20 of 20 match exactly once at both
revisions, and every replacement keeps the line count (`probe_r98.py` refuses otherwise; the counter's
code decoy refuses a line-count change).

Two anchor adjacencies are disclosed, neither a frozen row: **n14** mutates the same statement as
`r97c1` t12 (`    if fails:` in `_finish`) but with a different replacement and a different defect
(t12: only a single FAIL counts, so one FAIL + one PASS reads N/A; n14: a coexisting N/A file
suppresses FAIL), and **n19** mutates the baseline kind test where the round-98 t07 mutates the legacy
kind test (`<lane>.round`), a different line and a different file.

## Results — base vs candidate

Receipts `probe-base.txt`, `probe-cand.txt`. Honest bracket CLEAN 3 of 3 at both revisions (105 and
128 assertions); all 20 comment decoys and all 20 code decoys HELD at both revisions.

**Base: KILLED 3, SURVIVED 17, RUN-ERROR 0. Candidate: KILLED 4, SURVIVED 16, RUN-ERROR 0.**

| id | base | candidate | evidence |
|---|---|---|---|
| n01-l1-suffix-unanchored | SURVIVED | SURVIVED | — |
| n02-role-round-above | SURVIVED | SURVIVED | — |
| n03-proof-map-hash-unenforced | SURVIVED | SURVIVED | — |
| n04-proof-missing-skill-as-pinned | SURVIVED | SURVIVED | — |
| n05-proof-verdict-mismatch-unenforced | SURVIVED | SURVIVED | — |
| n06-proof-conjunct-status-unenforced | **KILLED** | **KILLED** | 1 failure / 105 (cand 1 / 128): `box proof: a must-fail case naming an unnamed conjunct is rejected: got (0, 'boxes proven 2\n', '')` |
| n07-runchecks-first-check-only | SURVIVED | SURVIVED | — |
| n08-main-fail-exit-zero | SURVIVED | SURVIVED | — |
| n09-main-check-ignored | SURVIVED | SURVIVED | — |
| n10-readtext-oserror-empty | SURVIVED | SURVIVED | — |
| n11-verdict-of-prefix | SURVIVED | SURVIVED | — |
| n12-report-stem-dotdot | SURVIVED | SURVIVED | equivalent (dead branch) |
| n13-map-duplicate-first-wins | SURVIVED | SURVIVED | — |
| n14-finish-fails-nas | SURVIVED | SURVIVED | — |
| n15-outofscope-nonmd-evaluated | SURVIVED | **KILLED** | 2 failures / 128: `r98-t01-lane-suffix-unanchored: a '.bak' prompt evaluates 0 files: got 1` and `… is out of scope: got []` |
| n16-box-section-ignored | **KILLED** | **KILLED** | 12 failures / 105 (cand 13 / 128), e.g. `box proof: a complete corpus proves both boxes: got (1, 'boxes proven 0\n', "… live SKILL.md box hash '7ce9850e…' != pinned '62c20a81…'")` |
| n17-proof-case-first-only | **KILLED** | **KILLED** | 5 failures / 105 (cand 6 / 128), e.g. `box proof: a complete corpus proves both boxes: … 'no isolated must-fail case for conjunct report_path_literal'` |
| n18-finish-na-count-zero | SURVIVED | SURVIVED | reporting-only |
| n19-state-baseline-exists | SURVIVED | SURVIVED | verdict-equivalent |
| n20-box-ninth-limit | SURVIVED | SURVIVED | equivalent on the committed SKILL.md |

The only base→candidate movement is **n15 SURVIVED → KILLED**: the round-98 `r98-t01` arm's `.bak`
prompt (`kote-round-7.md.bak`) is a name that is not a dispatch-prompt name and does not end `.md`, so
the mutant evaluates it (1 file) where the honest run lists it out of scope (0 files). The arm was
written for the round-name anchoring and incidentally covers this name-filter class. No other
classification changes; n16/n17 gain one failing assertion each from the new arms.

## Differential witnesses

Receipts `witness-base.txt`, `witness-cand.txt` (19 DIFFERS at each revision; the two files differ
only in scratch paths; n12 is SAME by construction). Every verdict-bearing survivor:

| id | witness input | honest | mutant |
|---|---|---|---|
| n01 | `evaluate_dispatch_04` on a prompts dir holding `kote-L1.md.bak` | `evaluated 0`, status `N/A`, out_of_scope `[kote-L1.md.bak]` | `evaluated 1`, status `PASS`, out_of_scope `[]` |
| n02 | `evaluate_dispatch_08` on `kote-round-7.md` whose role line says round 8 | file `FAIL`, role conjunct `FAIL` | file `PASS`, role conjunct `PASS` |
| n03 | `box_proof` with the map's `dispatch.04` `text_sha256` = 64 zeros | rc 1, `boxes proven 1`, err `map text_sha256 … != pinned …` | rc 0, `boxes proven 2` |
| n04 | `box_proof` with `SKILL.md` deleted | rc 1, `boxes proven 0`, err `live SKILL.md box hash None != pinned …` | rc 0, `boxes proven 2` |
| n05 | `box_proof` with a PASS-labelled duplicate of the stem must-fail case | rc 1, `boxes proven 1`, err `verdict 'FAIL', expected 'PASS'` | rc 0, `boxes proven 2` |
| n07 | `run_checks(..., ["dispatch.04","dispatch.08"])` | `['dispatch.04','dispatch.08']` | `['dispatch.04']` |
| n08 | `main()` on a prompt with a wrong report stem | rc 1, `FAIL dispatch.04 …` | rc 0, same output line |
| n09 | `main(["--check","dispatch.04"])` on a case where 04 PASSes and 08 FAILs | rc 0, one line | rc 1, two lines (08 FAIL) |
| n10 | `evaluate_dispatch_04` on a mode-000 prompt file (uid 1000) | raises `EnvError` | returns `evaluated 1`, status `N/A` |
| n11 | `box_proof` with the control case's `file` truncated to `kote-round-7` | rc 1, err `file 'kote-round-7' not evaluated` | rc 0, `boxes proven 2` |
| n13 | `box_proof` with two `dispatch.04` map entries (bad disposition first, good second) | rc 0, `boxes proven 2` (last wins) | rc 1, `boxes proven 1`, err `map disposition is 'executed:elsewhere.py' …` |
| n14 | `evaluate_dispatch_08` on one FAILing round file beside one N/A round file | check `FAIL` | check `N/A` |
| n15 | `evaluate_dispatch_04` on a prompts dir holding `notes.txt` with a report path | `evaluated 0`, status `N/A`, out_of_scope `[notes.txt]` | `evaluated 1`, status `FAIL` |
| n18 | `_finish` with one N/A file | status `N/A`, detail `… 0 PASS, 0 FAIL, 1 N/A …` | status `N/A`, detail `… 1 PASS, 0 FAIL, 0 N/A …` |
| n19 | `state_source` where `<lane>.report-baseline` is a DIRECTORY and `<lane>.round` exists | `('stale', None, 'state-stale: only kote.round present …')` | `('none', None, 'unreadable … (Is a directory)')` |
| n20 | `dispatch_box_sha256` on a synthetic skill with ten dispatch boxes | 9 keys, last `dispatch.09` | raises `IndexError: tuple index out of range` |

## Equivalent and no-verdict mutants (not kill targets)

- **n12-report-stem-dotdot — equivalent (dead branch).** `report_paths` runs
  `stem = m.group(2).rstrip(".,;:")` before `if not stem or stem in (".", "..")`. A stem made only of
  dots is already `""` after the `rstrip`, so `if not stem` catches it first and the tuple test can
  never fire. Witness `report_paths("….ufo/reports/round-7/..")` → `[]` under both (SAME).
- **n20-box-ninth-limit — equivalent on the committed input.** The live `SKILL.md` has exactly nine
  dispatch boxes, so `len(out) < len(BOX_ORDER)` is true for every one of them and the mutant hashes
  the same nine keys. The difference is latent: a tenth dispatch box raises `IndexError` instead of
  being ignored (witness above). No committed input reaches it, so it carries no verdict.
- **n18-finish-na-count-zero — reporting-only.** Only the `detail` string's PASS/N/A counts change;
  the file verdicts, the check status and the exit code are identical (witness: status `N/A` both).
- **n19-state-baseline-exists — verdict-equivalent.** A directory named `<lane>.report-baseline`
  sends both versions to a non-baseline state (honest `state-stale` via the legacy file, mutant
  `none`/`unreadable`); `round_le_latest_dispatched` is `N/A` either way, so no verdict differs. The
  round-98 `t07` arm varies the *legacy* entry's kind, not the baseline entry's.

## Findings

**F1 (coverage, main result).** The round-98 patch adds 23 assertions (105 → 128) and kills exactly
the nine frozen survivors plus, incidentally, n15; **16 of the 20 new mutants survive at the candidate
unchanged** (12 of them verdict-bearing; n12/n18/n19/n20 are equivalent or reporting-only). The
surviving classes are untouched by t01..t09: the L1 name regex's anchoring, the direction of the
role-round comparison, three box-proof map-side rules, the case verdict-mismatch check, the whole live
CLI (`run_checks`, `main`'s exit codes, `--check`), `read_text`'s substrate error, `_verdict_of`'s
prefix match, duplicate map entries, and `_finish`'s FAIL+N/A aggregation.
This is a coverage finding about the claim's scope, not a defect in the patch: C1's target is the
nine, and the patch meets it (the builder's reading, not mine).

**F2 (box proof — map parsing, the sharpest survivors).** n03, n04 and n13 each disable one map-side
rule and the proof still reads `boxes proven 2` rc 0: the map's `text_sha256` pin is never compared
with `PINNED_BOX_SHA` (n03), a missing/unreadable `SKILL.md` is treated as hashing to the pins (n04),
and a duplicate box entry keeps the first instead of the last (n13). The round-98 t04/t05 arms vary
the disposition and the live `SKILL.md` hash, but not these three. Minimal arms: (a) map
`text_sha256` = 64 zeros → `boxes proven 0`, rc 1; (b) delete `SKILL.md` → rc 1; (c) duplicate the
`dispatch.04` entry with a bad first copy → the last entry must win, rc 0.

**F3 (box proof — case expectations).** n05 (a case whose observed verdict differs from its expected
verdict) and n11 (a prefix match in `_verdict_of`) survive; n06 (the named-conjunct expected status)
is killed by the existing bogus-conjunct arm. The verdict-mismatch check is unobserved: a PASS-labelled
case whose observed verdict is FAIL still proves both boxes.

**F4 (live CLI unobserved — structural).** n07, n08, n09 and n10 survive because `--self-test` never
calls `run_checks` or `main`. The instrument's live exit ladder (a FAILing check → 1, a substrate
error → 2), the `--check` selection and `read_text`'s `EnvError` path are not exercised by the
self-test at all. The `--self-test` is a unit test of `evaluate_dispatch_04/08` and `box_proof`, not
of the CLI; a full close needs arms that call `run_checks`/`main` on fixture trees.

**F5 (evaluation path).** n01 (the L1 regex is not end-anchored, so `kote-L1.md.bak` is a spawn file
and its report path is evaluated), n02 (a role round *above* the file-name round passes; only the
below direction is covered by the existing role arm) and n14 (a check with one FAILing file and one
N/A file reads N/A, not FAIL) are verdict-bearing and unobserved.

**F6 (killed, coverage confirmed).** n06 is killed by the existing "must-fail case naming an unnamed
conjunct" arm (1 failure); n16 by the box-proof live-hash arms (12/13 failures); n17 by the
coverage/deletion arms (5/6 failures); n15 on the candidate by the new `r98-t01` `.bak` arm (2
failures). These four are not coverage findings.

## Bounds and risks

- Single-line (or two-line) literal substitutions only; multi-line restructuring defects are out of
  scope.
- The probe reuses the counter's `RUNNER`, so the counter's disclosed bound applies unchanged; no
  mutant here is a self-sniffer.
- The n10 witness needs a non-root uid (the run is uid 1000); a root run reads a mode-000 file, which
  the instrument's own t10 arm records.
- Base and candidate readings use the same driver, anchors and scratch layout, so the delta is
  attributable to the patch alone.
- A surviving mutant is a coverage finding, not permission to change the contract: the frozen
  predicate and the builder's arms are untouched by this seat.

## Verification log

- Candidate build: `git clone --shared` of the lane at the freeze, `git apply --check` OK, `git apply`,
  scratch-identity commit `67b11243dead375d62935685b34e64a4d691593b`; `git rev-parse --show-toplevel`
  = the clone; `git diff 63cd48d9 HEAD -- verifiers/verify_dispatch_prompts.py` sha256
  `27b412a58bf7583beb3d47013903a9d47203374b7ca0e1843aff816b90ffa6bf` = the patch file = the
  `ExecArmsR98_READY` sha256.
- Anchors checked against both instruments before every run: 20 of 20 match exactly once, line counts
  preserved, every text compiles.
- `probe_r98.py base 63cd48d9 …` → KILLED 3, SURVIVED 17, RUN-ERROR 0; honest CLEAN 3 of 3 (105);
  comment decoys 20 of 20, code decoys 20 of 20; seed `de1c1176bc4fddd6` (receipt `probe-base.txt`).
- `probe_r98.py cand 67b11243 …` → KILLED 4, SURVIVED 16, RUN-ERROR 0; honest CLEAN 3 of 3 (128);
  comment decoys 20 of 20, code decoys 20 of 20; seed `4d40315ae6b05ea9` (receipt `probe-cand.txt`).
- `witness_r98.py` at both revisions → 19 DIFFERS each, identical modulo scratch paths and the rev
  line; n12 SAME (receipts `witness-base.txt`, `witness-cand.txt`).
- Kill evidence with the failing assertion lines: `killed-base-full.txt`, `killed-cand-full.txt`.
- Receipt sha256: `probe-base.txt` `37beea54…81818d9`, `probe-cand.txt` `43adc82a…594b0a`,
  `witness-base.txt` `e16ac7c3…4ba296c`, `witness-cand.txt` `55468693…5b2e84e`,
  `killed-base-full.txt` `dcfc2c8f…efe7532d`, `killed-cand-full.txt` `d5c202fb…a3e8238`,
  `probe_r98.py` `1d10321f…ac87db4`, `witness_r98.py` `f81ec19c…9dc9146`.
- No lane file, no SKILL.md, no corpus file, no frozen instrument; no git/jj write in the lane.
- Tool installs: none needed.

## Files written

- `.ufo/waves/round-98/w1/MutTesterDispatchR98.md` (this report)
- `.ufo/waves/round-98/w1/MutTesterDispatchR98/probe_r98.py`, `witness_r98.py` (drivers)
- `.ufo/waves/round-98/w1/MutTesterDispatchR98/probe-base.txt`, `probe-cand.txt`,
  `witness-base.txt`, `witness-cand.txt`, `killed-base-full.txt`, `killed-cand-full.txt` (receipts)
- Scratch only: `/fast/scratch/hyaku/kotoba-r98/MutTesterDispatchR98/` (removed before yield).
