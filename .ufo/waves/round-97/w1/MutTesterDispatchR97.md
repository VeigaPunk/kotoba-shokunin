# MutTesterDispatchR97 — C1 mutants beyond the frozen set (round 97, wave r97-w1)

Seat: MutTesterDispatchR97 (mutation-tester, leaf; no subagent dispatch). Status: **complete** —
15 new mutants measured at the base and on the candidate.

Instrument under test: `verifiers/verify_dispatch_prompts.py --self-test` (SKILL.md § Dispatch-prompt
fidelity checklist, boxes `dispatch.04` / `dispatch.08`).

- BASE: freeze `148395bf42af97436b1b832a97a175515f981939`, instrument sha256
  `cf363a5c11a8bc863564aa6dccbe9491aa90f3cbcf37d598a5d68856173a99dd`, honest self-test
  `0 failure(s) over 78 assertions`.
- CANDIDATE: freeze + `ExecArmsR97.patch` (sha256 `22638a4e8a81cc8fabf1760660d5908ed40d8a0a5e4b9d09212d7c87d8973c80`,
  verified equal to the sha256 in `ExecArmsR97_READY`; the builder's own scratch rev is
  `ac7a00f5c570b8a21702a961667ade86eacbd1ab`, mine is `3da5a522e7c33ee589808d8e9ec28d1f67a60755` —
  same patch bytes, metadata-only difference). Instrument sha256
  `1e67db315d22b41cfe4760983708af7815860a926f6ad5f9f25137d12110690f`, honest self-test
  `0 failure(s) over 105 assertions`. The insertion is inside `self_test()` only: the text before
  `def self_test()` and from `def box_proof(` on is byte-identical to the base (checked), and
  `--box-proof` still reads `boxes proven 2`.

## Scope

Design ≥10 NEW mutants of the instrument's evaluation path that are not t01..t13/p00 of the round-97
table and not t01..t11 of `r96c1`, apply each with the v5 counter's own method, and classify
KILLED / RUN-ERROR / SURVIVED at the base AND on the candidate. Not a lane file, not a patch, no lane
write: measurements only, in `/fast/scratch/hyaku/kotoba-r97/MutTesterDispatchR97/`.

## Method (the v5 counter's, imported not re-implemented)

`probe_r97.py` copies `verifiers/fixtures/round-97/selftest-kills.py` (sha256
`b4200c5209b1c8a72bf0aaea0a191c1ba26dcf677db59e3b5163ee0ea3744fc7`) into scratch and imports
`RUNNER`, `classify`, `code_decoy`, `NotEvaluated`, `DECOY_MARK` from that copy, and reproduces
rules 2–5:

- literal single-anchor substitution (`original.count(anchor) == 1`, line count preserved);
- **source-blind** run: mutant text compiled with the instrument's path and executed as `__main__`
  with argv `[path, --self-test]` while the file on disk holds the honest bytes;
- **mirror** run: the mutant text on disk;
- **fresh world per run**: `git clone --shared --no-checkout` of REV + `checkout --detach REV`, fresh
  `TMPDIR`, `HOME`, `XDG_CACHE_HOME`, removed after the run (v5 rule 4);
- **comment decoy** (replacement lines appended as `# r97-decoy` comments) and **code decoy**
  (mutated statement under `if __name__ == "__decoy__":`), each run with its own text on disk;
- KILLED iff blind AND mirror are both REPORTED-FAILURE (exit 1, last summary `N failure(s) over M
  assertions` with N ≥ 1, ≥1 `self-test FAIL: ` line); RUN-ERROR otherwise; a baseline (honest) run
  that is not CLEAN makes the whole reading inconclusive;
- honest run before and after the table, instrument sha256 recorded, on-disk bytes re-hashed after
  every run (`restored OK`, 62 of 62 runs at each rev, 0 `MISMATCH`).

`witness_r97.py` loads the honest and each mutated instrument as modules (no subprocess) and calls
the mutated function on a witness input, so every non-equivalent survivor has an exhibited input
where honest and mutant disagree.

## Mutant table (15 new mutants, none in the frozen tables)

| id | class | anchor (literal, unique) | defect |
|---|---|---|---|
| m20-lane-suffix-unanchored | lane-name-parse | `ROUND_FILE_RE = re.compile(r"^(?P<lane>.+)-round-…\.md$")` | the name regex is not end-anchored: `kote-round-7.md.bak` names a prompt |
| m21-l1-kind-round | l1-kind | `return m.group("lane"), None, "l1"` | an L1 spawn file is typed `round`, so dispatch.08 evaluates it |
| m22-dirs-first-only | report-dir-set | `dirs = sorted({r for r, _s in paths})` | only the lowest report-dir round is compared |
| m23-verdict-first-file | `_verdict_of` | `for f in result["files"]:` | the verdict lookup searches only the first file |
| m24-proof-disposition-unenforced | box-proof map | `if entry.get("disposition") != want:` | a non-delegation disposition is accepted |
| m25-proof-live-hash-unenforced | box-proof live hash | `if live.get(cid) != pinned:` | the live SKILL.md box hash is not compared |
| m26-fence-any-close | box-hash fence | `if m and m.group(1)[0] * 3 == fence:` | any fence line closes a block, whatever its marker |
| m27-legacy-exists | state legacy kind | `if legacy.is_file():` | a directory named `<lane>.round` counts as legacy state |
| m28-prompts-include-dirs | prompts listing | `… iterdir() if p.is_file())` | a directory in the prompts dir is read as a prompt file |
| m29-file-result-na-first | `_file_result` precedence | `if "FAIL" in statuses: … elif "N/A" …` | one FAIL + one N/A reads N/A, not FAIL |
| m30-state-splitlines | state-source split | `first = raw.split()[:1]` | the baseline round is the whole first line, not its first field |
| m31-md-uppercase | report-stem suffix | `if stem.endswith(".md"):` | an upper-case `.MD` suffix is stripped like `.md` |
| m32-report-paths-sorted | report-path order | `return out` | `report_paths` returns sorted instead of text order |
| m33-role-last-line | role line | `m = ROLE_ROUND_RE.search(lines[0])` | the role round is read from the last line |
| m34-finish-fails-first-only | `_finish` detail | `for f in fails[:12])` | the failing-files detail names only the first file |

Anchors verified against the freeze instrument **and** the candidate: 15 of 15 match exactly once at
both revisions, and every replacement keeps the line count (`probe_r97.py` refuses otherwise; the
counter's code decoy refuses a line-count change).

One candidate mutant was dropped before scoring: `ROUND_FILE_RE` `.+` → `.+?` (greedy → non-greedy).
The `$` anchor forces the split to the unique trailing `-round-<N>.md`, so the two forms are
**equivalent on every input** (witness `kote-round-3-round-7.md` → `('kote-round-3', 7, 'round')`
under both). Recorded here as an equivalent, not counted in the table.

## Results — base vs candidate

Receipts `probe-base.txt`, `probe-cand.txt`. Honest before/after CLEAN at both revisions (78 and 105
assertions), every run `restored OK`.

**Totals identical at both revisions: KILLED 3, RUN-ERROR 1, SURVIVED 11.** All 15 comment decoys
HELD and all 15 code decoys HELD at both revisions.

| id | base | candidate | evidence (candidate) |
|---|---|---|---|
| m20-lane-suffix-unanchored | SURVIVED | SURVIVED | — |
| m21-l1-kind-round | RUN-ERROR | RUN-ERROR | `TypeError: %d format: a real number is required, not NoneType` (blind and mirror) |
| m22-dirs-first-only | SURVIVED | SURVIVED | — |
| m23-verdict-first-file | SURVIVED | SURVIVED | — |
| m24-proof-disposition-unenforced | SURVIVED | SURVIVED | — |
| m25-proof-live-hash-unenforced | SURVIVED | SURVIVED | — |
| m26-fence-any-close | SURVIVED | SURVIVED | — |
| m27-legacy-exists | SURVIVED | SURVIVED | — |
| m28-prompts-include-dirs | SURVIVED | SURVIVED | — |
| m29-file-result-na-first | **KILLED** | **KILLED** | 4 failures / 105 assertions, e.g. `unknown lane: dispatch.04 FAIL` |
| m30-state-splitlines | **KILLED** | **KILLED** | 8 failures / 105, e.g. `control: dispatch.08 verdict PASS` |
| m31-md-uppercase | SURVIVED | SURVIVED | — |
| m32-report-paths-sorted | SURVIVED | SURVIVED | verdict-equivalent (below) |
| m33-role-last-line | **KILLED** | **KILLED** | 11 failures / 105 (base: 10 / 78), e.g. `control: dispatch.08 verdict PASS` |
| m34-finish-fails-first-only | SURVIVED | SURVIVED | — |

The only base→candidate movement in the table is kill **strength**: m33 10 → 11 failing assertions
(one extra independent observation of the role-line defect, from the new `t08` arm); m29 stays 4, m30
stays 8. No classification changes.

## Differential witnesses (base → mutant; identical on the candidate)

Receipts `witness-base.txt`, `witness-cand.txt` (15 DIFFERS at each; the two files differ only in
scratch paths). Every non-equivalent survivor is behaviourally distinct:

| id | witness input | honest | mutant |
|---|---|---|---|
| m20 | `lane_of("kote-round-7.md.bak")` | `(None, None, None)` | `('kote', 7, 'round')` |
| m21 | `evaluate_dispatch_08` on a `kote-L1.md` case | `(0, 1, 'N/A')` | `TypeError: %d format …` |
| m22 | dispatch.08, paths in round-7 **and** round-8 | conjunct `FAIL` | conjunct `PASS` |
| m23 | `_verdict_of` on a two-file result, target second | the file dict | `None` |
| m24 | `box_proof` with `disposition: executed:…` | `(1, "map disposition is … not …")` | `(0, 'boxes proven 2')` |
| m25 | `box_proof` with the dispatch.04 box reworded | `(1, "live SKILL.md box hash … != pinned …")` | `(0, 'boxes proven 2')` |
| m26 | `dispatch_box_sha256` with `~~~` inside a ``` block | `{}` | `{'dispatch.01': 'a45c11…'}` |
| m27 | `state_source` where `kote.round` is a directory | `('none', None, 'no state file …')` | `('stale', None, 'state-stale …')` |
| m28 | prompts dir with a directory `ghost-round-7.md` | `evaluated 1` | `EnvError: … Is a directory (prompt file)` |
| m29 | `_file_result` with one FAIL and one N/A conjunct | `'FAIL'` | `'N/A'` |
| m30 | `state_source` on `"9 <64 zeros>"` | `('baseline', 9, …)` | `('none', None, 'non-integer round …')` |
| m31 | `report_paths("…/round-7/kote.MD")` | `[(7, 'kote.MD')]` | `[(7, 'kote')]` |
| m32 | `report_paths` with round-9 then round-4 | `[(9,'k'), (4,'k')]` | `[(4,'k'), (9,'k')]` |
| m33 | `role_round` round 6 on line 1, round 7 on the last line | `6` | `7` |
| m34 | `_finish` detail with two failing files | names `a` and `b` | names `a` only |

## Equivalent mutants (named, with the reason)

- **m32-report-paths-sorted** is *verdict-equivalent*: every consumer of `report_paths` uses a set
  (`stems`, `dirs`), a length, or truthiness; the only observable change is the order of the `bad`
  list in the `report_path_literal` detail string. Witness above shows the order difference and no
  status/verdict difference. Not worth an arm.
- **`ROUND_FILE_RE` greedy → non-greedy** (dropped before scoring): the `$` anchor makes the split
  unique, so the two forms agree on every input.

## Findings

**F1 (coverage, main result).** The candidate's 27 new behavioural assertions kill the thirteen
frozen survivors and **none of these 15 new mutants**: 11 survive at the candidate exactly as at the
base, 10 of them behaviourally distinct (witnesses above; m32 is verdict-equivalent). The surviving
classes are untouched by t01..t13: name-regex anchoring, `_verdict_of` lookup breadth, three
box-proof enforcement points, `state_source`'s legacy kind test, the prompts listing filter, the
`.MD` suffix, and the `_finish` failing-files detail. This is a coverage finding about the claim's
scope, not a defect in the patch: C1's target is the thirteen, and the patch meets it
(`C1-PREDICATE-MET`, 13 of 13, decoys 13 of 13 — the builder's reading, not mine).

**F2 (box proof — the sharpest survivors).** m24 and m25 each disable one of the box proof's two
map-side checks (`disposition`, live SKILL.md hash) and the self-test still reads
`0 failure(s) over 105 assertions`, because the self-test's proof tree is built with a correct map
and a copy of the real SKILL.md and never varies either. The proof's own claim — "the map delegates
the box … and the live SKILL.md box text hashes to it" — is therefore unobserved by the self-test.
Minimal arm: build the proof tree once with `disposition: executed:…` and once with a reworded
`dispatch.04` box, and assert `box_proof` reads `boxes proven 0` / rc 1 for each.

**F3 (dispatch.08 report-dir set).** m22 lets a prompt carry a round-7 report path beside a round-8
one and still read `filename_report_dir_round_equal` PASS, because only the lowest dir is compared.
This is a real dispatch-prompt defect class (a stale or wrong report dir escapes the box), and no
arm has a second dir above the file-name round.

**F4 (RUN-ERROR, not a kill).** m21 reproduces the round-96 F6 class from a different mutation:
typing an L1 file as `round` sends `round_n = None` into `"%d" % round_n`, so the mutant crashes
(`TypeError`) instead of reporting. Under the counter's rules a crash can never be a kill; any arm
aimed at the L1-kind defect must first make that detail path total.

**F5 (state kind and listing).** m27 (a directory named `<lane>.round` counts as legacy state) and
m28 (a directory named like a prompt file in the prompts dir raises `EnvError` where the honest run
ignores it) both survive: no arm varies the *kind* of the state or prompt entry, only its content.

**F6 (extraction edges).** m20 (`.md.bak` names a prompt), m31 (`.MD` stripped like `.md`) and m34
(the failing-files detail names only the first file) survive with the witnesses above. m34 is a
reporting-only survivor (no verdict differs); the other two change verdicts.

## Bounds and risks

- Single-line literal substitutions only; multi-line restructuring defects are out of scope.
- Equivalence for m32 is a static argument over its consumers plus the witness, not a proof over all
  inputs.
- The probe reuses the counter's `RUNNER`, so the counter's disclosed bound applies unchanged; no
  mutant here is a self-sniffer.
- Base and candidate readings use the same driver, anchors and scratch layout, so the delta is
  attributable to the patch alone.
- A surviving mutant is a coverage finding, not permission to change the contract: the frozen
  predicate and the builder's arms are untouched by this seat.

## Verification log

- Candidate build: `git clone --shared` of my scratch clone at the freeze, `git apply --check` OK,
  `git apply`, scratch-identity commit `3da5a522…`; `git rev-parse --show-toplevel` = the clone.
- Candidate identity: instrument sha256 `1e67db31…`; text before `def self_test()` and from
  `def box_proof(` byte-identical to the base; `--self-test` `0 failure(s) over 105 assertions`;
  `--box-proof` `boxes proven 2`.
- `probe_r97.py base 148395bf… $D` → KILLED 3, RUN-ERROR 1, SURVIVED 11; honest CLEAN 78; decoys
  15 of 15 each; 62 of 62 runs `restored OK` (receipt `probe-base.txt`).
- `probe_r97.py cand 3da5a522… $S/cand` → KILLED 3, RUN-ERROR 1, SURVIVED 11; honest CLEAN 105;
  decoys 15 of 15 each; 62 of 62 runs `restored OK` (receipt `probe-cand.txt`).
- `witness_r97.py base …` and `witness_r97.py cand …` → 15 DIFFERS each, identical modulo scratch
  paths (receipts `witness-base.txt`, `witness-cand.txt`).
- Anchors checked against both instruments before every run: 15 of 15 match exactly once, line
  counts preserved.
- Receipt sha256: `probe-base.txt` `909e5c2c…fcbab`, `probe-cand.txt` `51a1ec52…f2965`,
  `witness-base.txt` `5b8d4d71…1a24f`, `witness-cand.txt` `fa760b95…828a960`, `probe_r97.py`
  `c938f62e…350f`, `witness_r97.py` `a35bf28e…5b9a9`.
- No lane file, no SKILL.md, no corpus file, no frozen instrument; no git/jj write in the lane.
- Tool installs: none needed.

## Files written

- `.ufo/waves/round-97/w1/MutTesterDispatchR97.md` (this report)
- `.ufo/waves/round-97/w1/MutTesterDispatchR97/probe_r97.py`, `witness_r97.py` (drivers)
- `.ufo/waves/round-97/w1/MutTesterDispatchR97/probe-base.txt`, `probe-cand.txt`,
  `witness-base.txt`, `witness-cand.txt` (receipts)
- Scratch only: `/fast/scratch/hyaku/kotoba-r97/MutTesterDispatchR97/` (repo, cand, tmp; removed
  before yield).
