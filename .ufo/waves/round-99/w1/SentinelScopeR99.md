# SentinelScopeR99 — scope, safety and no-harm on the round-99 candidate

Seat: SentinelScopeR99 (attack/sentinel). Lane: kotoba-shokunin. Round 99, wave r99-w1.
Base / freeze commit: `b53e209603e7c480cd975ea543e415b66f695438`.
Scratch: `/fast/scratch/hyaku/kotoba-r99/SentinelScopeR99/` (TMPDIR + HYAKU_SCRATCH).

Status: **complete.** Candidate `89cd871846a79c7cced58efd1729943822b4290b` measured.
Scope: PASS (9 owned paths, SKILL.md / spot-checks / fixtures / the two frozen corpus gates / the
dispatch production bytes all unchanged). No-harm: 7 of 8 checks PASS; the tip battery reads 5 of 6
and `carried-reds.py` reads `green 2 of 3 … C2-PREDICATE-UNMET` on **one** cause — the equal-count
baseline (203/174 vs the tree's 204/175), which the L1 re-records at integration (proved: 204/175 →
`green 3 of 3`, battery `6 of 6`, `C2-PREDICATE-MET`). Safety: PASS. Findings F1–F5 below.

## Base readings (recorded before the candidate exists)

Commands run from `/home/vgpnk/Projects/shokunin/kotoba-shokunin` at `b53e2096`:

```
python3 -B verifiers/verify_dispatch_prompts.py --prompts /home/vgpnk/Projects/shokunin/.ufo/prompts \
  --state-dir /home/vgpnk/Projects/shokunin/.ufo/state --fleet /home/vgpnk/Projects/shokunin
FAIL dispatch.04: evaluated 1227 — 1227 file(s) evaluated: 1199 PASS, 6 FAIL, 22 N/A; 29 out of scope; failing files: kake-L1.md (report_path_literal,report_stem_is_lane_id), kasegi-L1.md (...), kengaku-L1.md (...), kotoba-L1.md (...), kumitate-L1.md (...), protocol-L1.md (report_path_literal)
FAIL dispatch.08: evaluated 1219 — 1219 file(s) evaluated: 1180 PASS, 10 FAIL, 29 N/A; 14 out of scope; failing files: kake-round-65..68.md, souji-round-46..51.md (filename_report_dir_round_equal)
rc=1
```

```
python3 -B verifiers/verify_dispatch_prompts.py --box-proof
boxes proven 2
rc=0
```

Base file hashes (sha256, at `b53e2096`):

| file | sha256 |
|---|---|
| SKILL.md | `fc0feaa3583837b7eec66a709a4110221f7d29bb72c4c0ddfe05016c3904d0df` |
| verifiers/verify_dispatch_prompts.py | `46bc97a6ce1de2c86b2f3782a30f7e09dbd24d4b0a35519260fc8c9b8b3b594a` |
| verifiers/verify_corpus_integrity.py | `a0b52d2419e28bf45bfcdf167dff5dfd44fdd7356cbc606eea1ea2ee8304b011` |
| verifiers/verify_corpus_independent.py | `7efc431b5ec39e50ed38c242b520b60c606bbf3682cfb224a6af11feaf57554b` |
| verifiers/verify_skill_checklist.py | `90e89f7acfdd5b9680247debe8bc4130b208ff39531b6279cffcf22c6609d2f8` |
| verifiers/check_tip_battery.py | `d5bf4e6496126598595150095fe5739f9e94e67a52209f69fadd2fb790bf961f` |
| corpus/SOURCES.md | `5714b67e8d5db7bb124bf139eee3cf13c80b9b70af7919f84ce764960241b0f8` |
| corpus/README.md | `7dfc52201365ef817830e0c0aff9abbe2f4a976199622630b4c2c07352bc4135` |
| LOG.md | `6f584a6d8cbd95a759ff694fcf9d8d4d5fb06c8728afc8a79584fd34de1714f7` |

51 `corpus/lessons/round-*-verifier-spotcheck.md` files hashed at base; 451 files under `verifiers/fixtures/`.

Base no-harm readings:

```
python3 -B verifiers/check_gate_registry.py --rev b53e2096...
gate registry rows conformant 74 of 74 lane verifiers; phantom 0
rc=0

bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file corpus/SOURCES.md
file ok .../corpus/SOURCES.md   rc=0    W04 count 34 (matches receipts/census-before.txt)
```

Scope-checker self-validation (synthetic, in scratch): base-vs-base rc 0; a production
mutation of `run_checks` → `SCOPE-VIOLATION production node changed: run_checks` rc 1;
a self-test-only mutation → rc 0 (allowed); a mutation of the shared helper `read_text`
→ `SCOPE-VIOLATION production node changed: read_text` rc 1.

Safety harness self-validation at base: `--self-test` under an audit hook refusing
`socket.connect`/`subprocess.Popen`/`os.system` → `0 failure(s) over 128 assertions`,
`SAFETY no network/subprocess audit event fired`, rc 0.

## Candidate

Patches (READY): ExecArmsR99 `9b705bc807855d0149a9eda9e2d45d2f024a34bb71606f99979f158f3f9af924`
(`C1: dispatch-prompt self-test arms r99-t01..t12 kill the round-99 frozen survivors`).
ExecRedsR99 `bd32f78d32547aed25f0f554966655ef8ac10586b968f9f4bb89ea3ca89d8720` (patch present; READY not yet written),
ScribeCorpusR99 `23e8f62460dab4a515a0c67d8930d86b4197a63546e894e804516aee3fa6352e` (patch present; READY not yet written).

All three READY files are now present (`ExecRedsR99_READY`, `ScribeCorpusR99_READY`,
`ExecArmsR99_READY`).

**ScribeCorpusR99's patch changed after my first build** (`23e8f624…` → `94a39dee…`, 11:22 → 11:36);
the readings below are for the final patch set:

| seat | patch sha256 |
|---|---|
| ExecRedsR99 | `bd32f78d32547aed25f0f554966655ef8ac10586b968f9f4bb89ea3ca89d8720` |
| ScribeCorpusR99 | `94a39deec29cda3920a1bb16e70c0ddfbb2d3f8ba8e6e2b09943db7ef2fc92fa` |
| ExecArmsR99 | `9b705bc807855d0149a9eda9e2d45d2f024a34bb71606f99979f158f3f9af924` |

Candidate built in my own scratch clone at
`89cd871846a79c7cced58efd1729943822b4290b` (base + ExecRedsR99 + ScribeCorpusR99 + ExecArmsR99,
scratch identity, `rev-parse --show-toplevel` = `$D`).

### Pre-validation of the arms patch alone (base + ExecArmsR99 = `a4c374aaa41d3b4a5e28988c2b2b6da99132eee9`)

```
git -C $D diff --stat b53e2096
 verifiers/verify_dispatch_prompts.py | 270 +++++++++++++++++++++++++++++++++++
 1 file changed, 270 insertions(+)
python3 -B scope_check.py <lane> b53e2096 $D a4c374a
 PRODUCTION-IDENTICAL outside self_test() and its self-test-only helpers   rc=0
python3 -B safety_run.py $D/verifiers/verify_dispatch_prompts.py
 0 failure(s) over 154 assertions / SAFETY no network/subprocess audit event fired   rc=0
python3 -B verifiers/verify_dispatch_prompts.py --box-proof   -> boxes proven 2   rc=0
live run over /home/vgpnk/Projects/shokunin/.ufo/prompts -> same two FAIL verdict lines as base (1227/1219 evaluated), rc=1
```

Safety scan of the added lines: no `/tmp`, no socket/urllib/http/subprocess, no credential-shaped
strings; the only `chmod` calls are `0o000` on a TMPDIR fixture and `0o600` in its `finally`.

## (1) Scope

`git -C "$D" diff --name-status b53e2096 3b4e1e4f` — nine paths, every one owned by the plan's
file-ownership table:

```
M LOG.md                                  (ExecRedsR99: one appended correction notice)
M corpus/README.md                        (ExecRedsR99: coverage-map rows incl. round-99.md)
M corpus/SOURCES.md                       (ScribeCorpusR99: appended S281 row)
M corpus/lessons/round-81.md              (ExecRedsR99: line 8 hash quoting only)
A corpus/lessons/round-99.md              (ScribeCorpusR99: new lesson)
M verifiers/check_tip_battery.py          (ExecRedsR99: INSTRUMENT_PINS block only)
M verifiers/corpus-baseline.json          (ExecRedsR99: equal-mode re-record)
M verifiers/verify_dispatch_prompts.py    (ExecArmsR99: self_test() arms only)
M verifiers/verify_skill_checklist.py     (ExecRedsR99: GOVERNANCE_CORRECTIONS + HORIZON only)
```

| check | command | observed | verdict |
|---|---|---|---|
| SKILL.md byte-identical | `git show <rev>:SKILL.md \| sha256sum` | base = cand = `fc0feaa3…` | PASS |
| no spotcheck file touched | per-file sha256 over `corpus/lessons/*spotcheck*` (51 files) | no `CHANGED` line | PASS |
| fixtures untouched | `git ls-tree -r <rev> -- verifiers/fixtures \| sha256sum` | base = cand = `2ac892e4…` | PASS |
| verify_corpus_integrity.py byte-identical | sha256 | base = cand = `a0b52d24…` | PASS |
| verify_corpus_independent.py byte-identical | sha256 | base = cand = `7efc431b…` | PASS |
| dispatch production code identical | `scope_check.py` (AST reachability: every base production-reachable top-level node and every unnamed top-level statement compared by source segment) | `PRODUCTION-IDENTICAL outside self_test() and its self-test-only helpers`, rc 0 | PASS |

The scope checker was itself falsified before use: a production mutation of `run_checks` and a
mutation of the shared helper `read_text` both produce `SCOPE-VIOLATION`, while a self-test-only
mutation passes.



## (2) No-harm

All commands run against the final candidate `89cd871846a79c7cced58efd1729943822b4290b` in `$D`.

| check | observed line | verdict |
|---|---|---|
| `check_gate_registry.py --rev <cand>` | `gate registry rows conformant 74 of 74 lane verifiers; phantom 0`, rc 0 | PASS |
| round-98 counter `c1 <cand> "$D"` | `C1 targets killed 9 of 9 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 9 of 9; code decoys held 9 of 9` / `C1-PREDICATE-MET`, rc 0 | PASS |
| round-98 counter `r97c1 <cand> "$D"` | `R97C1 targets killed 13 of 13 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 13 of 13; code decoys held 13 of 13` / `R97C1-PREDICATE-MET`, rc 0 | PASS |
| `check_assertion_floors.py --self-test` | `0 failure(s) over 176 assertions`, rc 0 | PASS |
| `verify_dispatch_prompts.py --box-proof` | `boxes proven 2`, rc 0 | PASS |
| live run over `/home/vgpnk/Projects/shokunin/.ufo/prompts` | `FAIL dispatch.04: evaluated 1227 — 1199 PASS, 6 FAIL, 22 N/A; 29 out of scope` and `FAIL dispatch.08: evaluated 1219 — 1180 PASS, 10 FAIL, 29 N/A; 14 out of scope`, rc 1 — `diff` against the base run: **LIVE-VERDICT-LINES-IDENTICAL** | PASS |
| census `sources-census.sh validate --file <cand>/corpus/SOURCES.md` | `file ok …/corpus/SOURCES.md`, rc 0, `W04=34` (base 34; not above 34) | PASS |
| full tip battery `check_tip_battery.py --repo "$D" --rev <cand> --fleet …` | `guards 5 of 5; tip battery exit 0: 5 of 6`, rc 1 — `gate verifiers/verify_corpus_integrity.py exit 1` | **FAIL — baseline drift, see below** |
| C2 counter `carried-reds.py <cand> "$D" --fleet …` | `C2 carried reds green 2 of 3; self-tests held 3 of 3; frozen 4 of 4; guards ok` / `C2-PREDICATE-UNMET`, rc 1 | **UNMET — same baseline drift** |

### The one red: `verify_corpus_integrity` / C2 on the candidate as built

`verifiers/corpus-baseline.json` (ExecRedsR99) expects `tracked_files 203`, `report_total 174`;
the candidate tree observes **204** and **175**. The +1 file and +1 report pointer are exactly
`corpus/lessons/round-99.md` (ScribeCorpusR99's file, which adds one tracked corpus file and one
`.ufo/reports/...` pointer). `commit_total` already matches at 72.

```
DRIFT   corpus.index.tracked_files: observed=204 expected=203
DRIFT   corpus.pointers.report_total: observed=175 expected=174
6/9 checks pass
```

In a fleet-shaped sandbox (the counter's own construction) the drift list is exactly
`corpus.index.tracked_files, corpus.pointers.report_total` — no `report_dead` line. A bare worktree
additionally shows `report_dead=1` for `corpus/lessons/round-81.md:29:
../../.ufo/reports/round-76/kotoba.md`; that pointer resolves through the fleet root and is absent
only because a clone has no sibling `.ufo`. It is a measurement artefact, not a candidate defect.

ExecRedsR99's own full-candidate receipt (`ExecRedsR99/c2-candidate.txt`, rev `d0afe6a7`) reads the
same `green 2 of 3 … C2-PREDICATE-UNMET`, so the builder observes the drift too.

**Remediation probe (decisive).** In a second, undisturbed clone I applied the three patches, then
changed only the two `expect` values to `204` / `175` and committed (`7adbb847e8205030cf77486d0fc7509637981684`).
`carried-reds.py` on that revision:

```
red verifiers/verify_skill_checklist.py exit 0 GREEN
red verifiers/verify_corpus_integrity.py exit 0 GREEN: 9/9 checks pass
red verifiers/verify_corpus_independent.py exit 0 GREEN: exit 0
selftest … 1864 / 178 / 109 HELD
frozen 4 of 4
battery gate … all six exit 0 … tip battery exit 0: 6 of 6
C2 carried reds green 3 of 3; self-tests held 3 of 3; frozen 4 of 4; guards ok
C2-PREDICATE-MET
```

So the baseline re-record is the **only** remaining blocker: the L1 must re-record
`corpus-baseline.json` to `tracked_files 204`, `report_total 175` (`commit_total 72` unchanged)
after ScribeCorpusR99's lesson lands. This is the drift the seat spec names; it is not a scope
violation and not a C2 failure of the ExecRedsR99-only candidate.

## (3) Safety

| check | observed | verdict |
|---|---|---|
| no hardcoded `/tmp` in new code | `grep '^+.*/tmp'` over all three patches: none | PASS |
| no network / subprocess in the self-test | `safety_run.py` installs an audit hook refusing `socket.connect`, `socket.getaddrinfo`, `urllib.Request`, `subprocess.Popen`, `os.system`, `os.exec*`, `os.spawn*`, `ftplib`/`smtplib` connect, then runs `--self-test`: `0 failure(s) over 154 assertions`, `SAFETY no network/subprocess audit event fired`, rc 0 | PASS |
| fixtures only under TMPDIR | `TMPDIR=<scratch> … --self-test` leaves the TMPDIR empty afterwards; `git -C "$D" status --porcelain` empty after the run | PASS |
| minimal environment | `env -i PATH=… HOME=… TMPDIR=… PYTHONDONTWRITEBYTECODE=1 … --self-test` → `0 failure(s) over 154 assertions`, rc 0 | PASS |
| chmod-000 fixture restored/removed | the only `chmod` calls are `victim.chmod(0o000)` on a TMPDIR fixture and `victim.chmod(0o600)` in its `finally`; no mode-000 file survives under the scratch TMPDIR | PASS |
| no credential-shaped strings | `grep -E 'AKIA\|ghp_\|sk-[A-Za-z0-9]{10}\|BEGIN (RSA\|OPENSSH\|PRIVATE)\|password\|passwd\|token=\|secret'` over all three patches: none | PASS |
| anti-sniffing (arms observe behaviour) | the 28 new `rec(...)` assertions call `lane_of`, `evaluate_dispatch_04/08`, `box_proof` (via the existing `run_proof` closure), `run_checks`, `main`, `_verdict_of`, `EnvError`; the only `read_bytes` is a backup of the fixture-tree `SKILL.md`; no `__file__`/`inspect`/`getsource`/`ast` use; no bare `assert`; 4 `try/except` guards route crashes into `rec(...)` | PASS |



## Findings / risks

**F1 (high, blocks C2 as built — disclosed drift, not a scope violation).** `verifiers/corpus-baseline.json`
expects `tracked_files 203` / `report_total 174`; the final candidate observes `204` / `175`.
`carried-reds.py` therefore reads `green 2 of 3 … C2-PREDICATE-UNMET` and the tip battery
`5 of 6`. The delta is exactly `corpus/lessons/round-99.md`. Remediation probe
`7adbb847…` (same three patches + `expect 204/175`) reads `green 3 of 3 … tip battery exit 0: 6 of 6`
/ `C2-PREDICATE-MET`. **Smallest remediation:** the L1 re-records `corpus-baseline.json` to
`tracked_files 204`, `report_total 175` (`commit_total 72` unchanged) after the final
ScribeCorpusR99 patch lands. No other byte needs to change.

**F2 (medium, provenance defect).** The `note` ExecRedsR99 wrote into `corpus-baseline.json` claims
the re-record was taken "over the round-99 candidate tree (base b53e209 + candidate patches in order
ExecRedsR99, ScribeCorpusR99, ExecArmsR99)". The arithmetic contradicts it: base `report_total` is
166, the eight new `corpus/README.md` spot-check rows add 8 pointers → **174**, and
`tracked_files` 203 is the base count with **no** new corpus file. Both are the counts of
base + ExecRedsR99 **only**; the full candidate is 204/175. The builder's own receipt
(`ExecRedsR99/c2-candidate.txt`, rev `d0afe6a7`) honestly reports `green 2 of 3 … UNMET`, so this is
a wrong provenance sentence in the baseline note, not a hidden failure — but the note must not be
cited as evidence that the re-record covered ScribeCorpusR99's file. The L1's re-record (F1)
supersedes it.

**F3 (low, operational).** ScribeCorpusR99's patch changed after first publication
(`23e8f624…` → `94a39dee…`, 11:22 → 11:36) with no version marker in the file name. A seat that
built a candidate from the first bytes measures a stale tree (I did, at `3b4e1e4f`). The L1 should
gate on the READY sha256, not on the path.

**F4 (low, measurement trap).** In a bare clone, `verify_corpus_integrity` reports
`report_dead=1` for `corpus/lessons/round-81.md:29: ../../.ufo/reports/round-76/kotoba.md`; in a
fleet-shaped sandbox (the counter's and the battery's construction) it is 0. Anyone reading the gate
in a plain clone will misattribute a red. No candidate change is needed.

**No scope violation found.** Nine changed paths, all owned; SKILL.md, the 51 spot-check files, the
451 `verifiers/fixtures/` files, `verify_corpus_integrity.py` and `verify_corpus_independent.py` are
byte-identical to the base; `verify_dispatch_prompts.py`'s production bytes are unchanged outside
`self_test()` and its self-test-only helpers.

**No safety violation found.** No `/tmp` literal, no network or subprocess in the self-test (audit
hook), fixtures only under TMPDIR (empty afterwards, repo clean), minimal-env run passes, the
chmod-000 fixture is restored in a `finally` and leaves nothing behind, no credential-shaped string
in any patch.

**F5 (medium, integration hazard — not mine to fix).** At 11:44:56 the L1 began writing the
integration into the lane worktree (`LOG.md`, `corpus/README.md`, `corpus/SOURCES.md`,
`corpus/lessons/round-81.md`, `corpus/lessons/round-99.md`, `verifiers/*` are now modified there).
`corpus-baseline.json` in the lane still reads `expect 203` / `expect 174` — F1 is live.
Also untracked at the lane root: `repo/`, a broken `git clone --shared` whose alternate points at
`/fast/scratch/hyaku/kotoba-r99/ReviewerRedsR99/repo/.git/objects` (that scratch clone no longer
exists; `git -C repo rev-parse HEAD` → `fatal: bad object HEAD`). It is not mine and I did not
remove it, but `git add -A` in the lane would stage it as a gitlink/junk. The L1 must delete
`kotoba-shokunin/repo/` before staging.

## Residual risk

- The baseline re-record must be taken **after** the last corpus change of the landing tree; if
  ScribeCorpusR99's lesson or the README rows change again, 204/175 move.
- `report_total` counts report pointers, so a future edit to `corpus/lessons/round-99.md` that adds
  or removes a `.ufo/reports/...` token re-opens the drift.
- I did not judge C1's kill predicate or C2's laundering question; those belong to the reviewers and
  the L1. My readings are scope, no-harm and safety only.
