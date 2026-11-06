# SentinelScopeR97 — scope, safety and no-harm on the round-97 candidate

Seat: **SentinelScopeR97** (leaf member, no subagent dispatch).
Assigned surface: scope + no-harm + safety on the candidate built from
`148395bf42af97436b1b832a97a175515f981939` plus `ExecArmsR97.patch` and `ScribeCorpusR97.patch`.

**Verdict: PASS on every assigned check. No defect found in the candidate.**
Two observations outside the candidate (lane integration state, and a non-defect quirk) are in § 4.

## 0. Environment and candidate

- Scratch: `/fast/scratch/hyaku/kotoba-r97/SentinelScopeR97/` (`TMPDIR` and `HYAKU_SCRATCH` both set to it).
- Scratch clone `$D = /fast/scratch/hyaku/kotoba-r97/SentinelScopeR97/repo`,
  `git clone -q --shared /home/vgpnk/Projects/shokunin/kotoba-shokunin "$D" && git -C "$D" checkout -q 148395bf…`;
  `git -C "$D" rev-parse --show-toplevel` → `/fast/scratch/hyaku/kotoba-r97/SentinelScopeR97/repo` (asserted).
- Patches received and sha256-checked against their READY files:

| patch | sha256 | READY | files |
|---|---|---|---|
| `ScribeCorpusR97.patch` | `3f2712c471c814b31300af5caf7df59a8de8aac8f24cb3a77c184e94681b4902` | matches | 3 (`corpus/README.md`, `corpus/SOURCES.md`, `corpus/lessons/round-97.md`) |
| `ExecArmsR97.patch` | `22638a4e8a81cc8fabf1760660d5908ed40d8a0a5e4b9d09212d7c87d8973c80` | matches | 1 (`verifiers/verify_dispatch_prompts.py`) |

- Both `git -C "$D" apply --check` → rc 0; applied in order, committed under the scratch identity
  `scratch <scratch@invalid>`.
- **Candidate revision: `868c2b0c1375689f9e650f45bf5fb10f206c6339`**
  (`$D` = `148395bf` + `ScribeCorpusR97.patch` + `ExecArmsR97.patch`; `git status` clean afterwards).
  Reproduce: clone at `148395bf`, `git apply` the two patches above, commit.
- All base readings were taken from the lane **before** the lane working tree was edited (§ 4.1):
  latest base receipt mtime 01:11:46, first lane edit 01:15:46.

## 1. Scope (candidate)

### 1.1 `git -C "$D" diff --stat 148395bf… 868c2b0c…`

```
 corpus/README.md                     |   1 +
 corpus/SOURCES.md                    |   2 +
 corpus/lessons/round-97.md           | 179 +++++++++++++++++++++++++++++++++++
 verifiers/verify_dispatch_prompts.py | 231 +++++++++++++++++++++++++++++++++++
 4 files changed, 413 insertions(+)
```
`--name-status`: `M corpus/README.md`, `M corpus/SOURCES.md`, `A corpus/lessons/round-97.md`,
`M verifiers/verify_dispatch_prompts.py`. Every path is owned by one of the two builders; **no other
file is touched** (0 deletions anywhere).

### 1.2 Frozen surfaces

| check | observed | verdict |
|---|---|---|
| `SKILL.md` sha256 at base vs candidate | `fc0feaa3583837b7eec66a709a4110221f7d29bb72c4c0ddfe05016c3904d0df` both | **BYTE-IDENTICAL** |
| `verifiers/fixtures/dispatch-prompts/` + `verifiers/fixtures/round-9*/` trees (`git ls-tree -r` diff) | empty | **IDENTICAL** |
| `*-verifier-spotcheck.md` / `SKILL.md` in the changed set | none | **UNTOUCHED** |
| changed paths under `verifiers/` | `verifiers/verify_dispatch_prompts.py` only | **PASS** |

### 1.3 Production code of `verify_dispatch_prompts.py` outside `self_test()`

Byte-region split at `\ndef _write_case(` (end of `run_checks()`) and `\ndef box_proof(`:

```
base prefix/suffix bytes: 26321 / 9659
cand prefix/suffix bytes: 26321 / 9659
PREFIX-IDENTICAL
SUFFIX-IDENTICAL
middle base 28071 bytes -> cand 41724 bytes
hunks outside self-test region: 0
```

The module docstring through `run_checks()` and `box_proof()`/`main()` are **byte-identical**; all 231
added lines fall inside the self-test region (`_write_case` … `self_test()`), i.e. `self_test()` and
self-test-only helpers. `ExecArmsR97`'s own `production-identity.txt` reports the same split
(common prefix 54060, common suffix 9991, 0 inserted lines at column 0).

### 1.4 Frozen anchors (the counter substitutes these literally)

`check_anchors.py` over the candidate blob: **14 of 14 anchors exact-once** (t01…t13 + `p00`), i.e. no
second occurrence of any anchor text was introduced (in particular no bare `if note:` / `if fails:`
line in the new code). Receipt: `anchors-cand.txt`.

### 1.5 Scribe patch content scope

- SOURCES rows `| S[0-9]{3} |`: **198 → 200** (S273 + S274), exactly as the READY claims; no row rewritten.
- `corpus/README.md`: exactly one index row added (`| Round-97 lesson | lessons/round-97.md | …`).
- `corpus/lessons/round-97.md`: new file, sections `## Gate`, `## Corrections`, `## Mistakes`,
  `## Status changes`, `## Considerthese`, `## Settlement`; `## Corrections` carries **C97-1**, the named
  correction of the round-96 routed defect 1 (S272 receipt line 12 says 19 words, the quote measures 22),
  pointing at the frozen receipt without editing it.
- Independent word-count cross-check of the two new quotes (`wc -w`): S273 quote **21** words (row: 21),
  S274 quote **25** words (row: 25) — both agree.
- No `/fast/scratch` or credential-shaped string in any added line; the single `/home/vgpnk/Projects/shokunin/scripts`
  path in the lesson has precedent (round-95/round-96 lessons each carry one).

## 2. No-harm (candidate vs base)

| check | command | base `148395bf` | candidate `868c2b0c` | verdict |
|---|---|---|---|---|
| gate registry | `check_gate_registry.py --rev <rev>` (script from `$D`) | `rows conformant 74 of 74; phantom 0`, rc 0 | `rows conformant 74 of 74; phantom 0`, rc 0 | **PASS** |
| round-96 counter `c1` | `verifiers/fixtures/round-96/selftest-kills.py c1 <rev> "$D"` | `targets killed 11 of 11 … C1-PREDICATE-MET` rc 0 | `targets killed 11 of 11 … C1-PREDICATE-MET` rc 0 | **MET** |
| round-96 counter `r95c1` | same, `r95c1` | `R95C1 … killed 3 of 3 … MET` rc 0 | `R95C1 … killed 3 of 3 … MET` rc 0 | **MET** |
| round-95 counter `c1` | `verifiers/fixtures/round-95/selftest-kills.py c1 <rev> "$D"` | `killed 3 of 3 … MET` rc 0 | `killed 3 of 3 … MET` rc 0 | **MET** |
| round-95 counter `r94c1` | same, `r94c1` | `R94C1 … killed 3 of 3 … MET` rc 0 | `R94C1 … killed 3 of 3 … MET` rc 0 | **MET** |
| floors guard self-test | `check_assertion_floors.py --self-test` | `0 failure(s) over 176 assertions` rc 0 | `0 failure(s) over 176 assertions` rc 0 | **PASS** |
| box proof | `verify_dispatch_prompts.py --box-proof` | `boxes proven 2` rc 0 | `boxes proven 2` rc 0 | **PASS** |
| live run over `/home/vgpnk/Projects/shokunin/.ufo/prompts` | `verify_dispatch_prompts.py --prompts …` | rc 1, sha256 `f54b30bf…d6df` | rc 1, **byte-identical** to base (`diff` empty) | **PASS** (production unchanged) |
| census on `corpus/SOURCES.md` | `scripts/sources-census.sh validate --file …` | rc 0, **34** `W04`, 0 `E` | rc 0, **34** `W04`, 0 `E` | **PASS** |
| self-test assertion count | `verify_dispatch_prompts.py --self-test` | 78 assertions | **105** assertions (+27, as the READY claims) | **PASS** (floor 56) |

- The live run's two `FAIL` lines (`dispatch.04` 6 FAIL / `dispatch.08` 10 FAIL) are the fleet's
  pre-existing prompt defects, identical at base and candidate — the check is that the verdict lines did
  not move, and they did not.
- `floors-registry.json` → `instruments.dispatch_prompts.floor = 56`; the candidate's 105 ≥ 56, so the
  floor is met and the self-test did not shrink (+27 net).
- **v5 counter C1 at the candidate** (`selftest-kills.py c1 868c2b0c… "$D"`), receipt `v5-c1-cand.txt`:

```
C1 targets killed 13 of 13 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 13 of 13; code decoys held 13 of 13
rules v5: honest runs CLEAN 3 of 3; mirror runs reported 14 of 14; seed 86d29cd8d116e802
C1-PREDICATE-MET
```
  rc 0. (Not my claim to score — recorded because it is the strongest no-harm signal on the self-test
  region: the arms are behavioural and the decoys still hold.)

## 3. Safety

| check | evidence | verdict |
|---|---|---|
| no hardcoded `/tmp` in new code | `grep -c "/tmp"` over the candidate `verify_dispatch_prompts.py` → **0**; added-lines grep over both patches → no hit | **PASS** |
| no network in self-tests | `grep -nE "urllib\|socket\|http\|requests\|urlopen\|curl\|wget"` over the whole candidate file → **no hit**; imports are stdlib only (`argparse contextlib hashlib io json os re shutil sys tempfile` + `from pathlib import Path`) | **PASS** |
| no credential-shaped strings | added lines of both patches grepped for `ghp_`, `sk-`, `AKIA`, `PRIVATE KEY`, `password=`, `secret=`, `token=` → **no hit** | **PASS** |
| fixtures only under TMPDIR | self-test run with `TMPDIR=$S/selftest-tmp` → rc 0, **0 leftovers** under that TMPDIR; `git -C "$D" status --porcelain` **empty** after the whole battery (nothing written into the repo); all fixtures are built under `tempfile.TemporaryDirectory` | **PASS** |
| chmod-000 fixture restored | code: `state_file.chmod(mode)` (fixture, `mode=0o000`) with `finally: (case/"state"/"kote.report-baseline").chmod(0o600)`; empirically **0 files with mode 000** anywhere under the scratch tree after the run; `euid == 1000`, so the unreadable arm really ran (the `geteuid()==0` branch that records instead of exercising was not taken) | **PASS** |
| v5 counter leaves nothing under its scratch root | `$S/kotoba-r97/selftest-kills`: **0 entries before**, **0 entries after** the `c1` run; the round-95/round-96 roots are likewise 0 after their runs | **PASS** |
| no stray processes of mine | `ps -u vgpnk` filtered to `selftest-kills\|verify_dispatch` → only **other seats'** runs (CriticClaimR97, ReviewerCounterV5, ReviewerArmsR97, ExecForgeryV5, MutTesterCounterV5); none started by me | **PASS** |

## 4. Findings / observations

1. **Observation (outside the candidate, informational for the L1).** The lane working tree is **not**
   the candidate: since 01:15:46 it carries an integration state with more than the two patches —
   `corpus/QUALITY.md` +1, `corpus/SOURCES.md` **+4** rows (S273, S274 plus **rejected** S275 pytest
   `tmp_path` and **rejected** S276 `pathlib.Path.is_dir`), `corpus/README.md` +1, the 231-line verifier
   change, and a `corpus/lessons/round-97.md` that differs from the scribe's scaffold (it documents
   S275/S276 as rejected rows and states "198 → 202 rows"). That state is internally consistent — the
   lane's own `sources-census.sh validate --file …/corpus/SOURCES.md` reads **rc 0, 34 `W04`, 0 `E`** —
   and it does not contradict the scribe's Gate (both call S275 rejected and S276 unrowed/rejected).
   It matters only because a gate that measures "the lane" measures 202 rows, while the candidate I was
   assigned measures 200. **My base readings predate every one of those edits** (latest base receipt
   01:11:46), so they are genuine base readings; the candidate bytes I measured come from the patches in
   my own scratch clone, never from the lane working tree.
2. **Non-defect quirk.** `ScribeCorpusR97.patch` carries `c/` / `i/` diff prefixes rather than the
   protocol's `a/` / `b/`. It parses and applies cleanly (`git apply --check` rc 0, `git apply --stat`
   → `3 files changed, 182 insertions(+)`), so nothing needs fixing; noted only so a future reader does
   not mistake it for a malformed patch.
3. **Non-defect quirk.** The self-test run from a copy **outside** the repo layout reports 13 failures
   at **both** base (78 assertions) and candidate (105 assertions) — the box-proof arm needs `SKILL.md`
   relative to the module. This is pre-existing and identical in both, not a regression; it is why the
   assertion counts in § 2 were taken from the blobs but the pass/fail verdicts from inside a clone.
4. **No defect found in the candidate** on any assigned axis: scope, frozen surfaces, production-region
   byte-identity, anchor exact-once, no-harm battery, and the six safety checks all pass.

## 5. Receipts (this directory)

`battery.log` (whole run), `v5-c1-cand.txt`, `r96-c1-{base,cand}.txt`, `r96-r95c1-{base,cand}.txt`,
`r95-c1-{base,cand}.txt`, `r95-r94c1-{base,cand}.txt`, `gate-cand.txt`, `floors-selftest-cand.txt`,
`boxproof-cand.txt`, `selftest-cand.txt`, `live-base.txt`, `live-cand.txt`, `census-cand2.txt`,
`census-lane-now.txt`, `anchors-cand.txt`, `base-hashes.txt`.
Scratch (`/fast/scratch/hyaku/kotoba-r97/SentinelScopeR97/`, including the candidate clone) is removed
before this seat yields; the candidate is reproducible from `148395bf` + the two sha256-pinned patches.
