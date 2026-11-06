# SentinelScopeR98 — scope, safety and no-harm on the round-98 candidate

Seat: SentinelScopeR98 (leaf; no subagent dispatch). Lane: /home/vgpnk/Projects/shokunin/kotoba-shokunin.
Base / freeze: 63cd48d9de2c44eb40691ca05d3a41cc2f9a3248.
Scratch: /fast/scratch/hyaku/kotoba-r98/SentinelScopeR98.
Scratch clone `$D` = /fast/scratch/hyaku/kotoba-r98/SentinelScopeR98/repo (`git rev-parse --show-toplevel` == $D,
checked out at the freeze commit before any patch).
Candidate revision: **384b68507060aa5916d418ca96bea53690713fc2** (`$D` = base + ExecArmsR98.patch +
ScribeCorpusR98.patch, committed under the scratch identity `scratch <scratch@invalid>`; `git apply --check`
passed on the clean clone before applying).

Patches applied (sha256 as named by the READY files; both match the files on disk):
- `ExecArmsR98/ExecArmsR98.patch` `27b412a58bf7583beb3d47013903a9d47203374b7ca0e1843aff816b90ffa6bf`
- `ScribeCorpusR98/ScribeCorpusR98.patch` `6eae5cf25c15441ef7b783bb37982ba9a641469f7798159777eb38ca7d014d20`

## Axes

1. scope — only owned files changed; SKILL.md and frozen instruments byte-identical; production code of
   verifiers/verify_dispatch_prompts.py outside self_test()/self-test helpers byte-identical.
2. no-harm — gate registry 74/74; round-97 and round-96 counters MET; assertion floors self-test; box proof
   2 boxes; live dispatch run verdict lines equal base vs candidate; census rc 0 with W04 count.
3. safety — no hardcoded /tmp in new code, no network in self-tests, no credential-shaped strings, fixtures
   under TMPDIR only; v6 counter scratch root empty after a run and its pristine export removed.

## 1. Scope — PASS

| check | command | observed |
|---|---|---|
| changed files | `git -C $D diff --stat 63cd48d9 <cand>` | `corpus/README.md +1`, `corpus/SOURCES.md +4`, `corpus/lessons/round-98.md +282`, `verifiers/verify_dispatch_prompts.py +183` — 4 files, 470 insertions, 0 deletions; every one is an owned file |
| name-status | `git -C $D diff --name-status 63cd48d9 <cand>` | `M corpus/README.md`, `M corpus/SOURCES.md`, `A corpus/lessons/round-98.md`, `M verifiers/verify_dispatch_prompts.py` |
| SKILL.md | `git -C $D diff --stat 63cd48d9 <cand> -- SKILL.md` | empty; sha256 base `fc0feaa3583837b7eec66a709a4110221f7d29bb72c4c0ddfe05016c3904d0df` == candidate |
| frozen fixtures / spotchecks | `git -C $D diff --name-only 63cd48d9 <cand> -- verifiers/fixtures/ corpus/lessons/round-9*-verifier-spotcheck.md` | empty — no dispatch-prompts fixture, no round-9x fixture, no other verifier, no spotcheck file touched |
| production region (docstring → `run_checks()`) | sha256 of bytes before the `# self-test (temporary fixtures only)` banner | base `f3412973a96e4106e528e50bb43900d9c61c4e778d095f82308e197ab43cbc05` (25851 B) == candidate |
| production region (`box_proof()` → EOF) | sha256 of bytes from `def box_proof(` | base `647ec36bf38857e1b6415dbc5846c7020de52efee857449b205da3b95ea32e8b` (9659 B) == candidate |
| self-test region only | diff hunk | one hunk `@@ -1331,6 +1331,189 @@ def self_test() -> int:` — entirely inside `self_test()` (base lines 679–1343); self-test region 769 → 952 lines; file mode 100755 preserved |
| SOURCES rows | `grep -cE '^\| S[0-9]{3} \|'` | 202 → 206 (S277 mined, S278 mined, S279 mined, S280 rejected — matches the Scribe READY) |
| README | diff | exactly one added index row (`Round-98 lesson | lessons/round-98.md`) |
| lesson file | diff | new file, 282 lines, author line `ScribeCorpusR98` (no lane-identity heading) |

## 2. No-harm

| check | command | observed | verdict |
|---|---|---|---|
| gate registry | `cd $D && python3 -B verifiers/check_gate_registry.py --rev <cand>` | `gate registry rows conformant 74 of 74 lane verifiers; phantom 0`, rc 0 (base also 74 of 74) | PASS |
| round-97 counter, c1 | `HYAKU_SCRATCH=$S python3 -B verifiers/fixtures/round-97/selftest-kills.py c1 <cand> $D` | `C1 targets killed 13 of 13 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 13 of 13; code decoys held 13 of 13`, `C1-PREDICATE-MET`, rc 0 (base: same 13 of 13) | PASS |
| round-97 counter, r96c1 | `… round-97/selftest-kills.py r96c1 <cand> $D` | `R96C1 targets killed 11 of 11 (run errors 0); …; R96C1-PREDICATE-MET`, rc 0 | PASS |
| round-96 counter, c1 | `… round-96/selftest-kills.py c1 <cand> $D` | `C1 targets killed 11 of 11 (run errors 0); …; C1-PREDICATE-MET`, rc 0 (base: same 11 of 11) | PASS |
| round-96 counter, r95c1 | `… round-96/selftest-kills.py r95c1 <cand> $D` | `R95C1 targets killed 3 of 3 (run errors 0); …; R95C1-PREDICATE-MET`, rc 0 | PASS |
| assertion floors self-test | `cd $D && python3 -B verifiers/check_assertion_floors.py --repo $D --self-test` | `0 failure(s) over 176 assertions`, rc 0 (base: same) | PASS |
| assertion floors battery (bonus) | `… check_assertion_floors.py --repo $D --script dispatch_prompts=$D/verifiers/verify_dispatch_prompts.py` | completed rc 0, **19 of 19 floors PASS**, including `PASS dispatch_prompts observed=128 floor=56` (base self-test 105 assertions → candidate 128) and `PASS floors_guard observed=176 floor=176` | PASS |
| box proof | `cd $D && python3 -B verifiers/verify_dispatch_prompts.py --box-proof` | `boxes proven 2`, rc 0 | PASS |
| live dispatch run | `cd $D && python3 -B verifiers/verify_dispatch_prompts.py --prompts /home/vgpnk/Projects/shokunin/.ufo/prompts` | rc 1; `diff` of the `PASS|FAIL dispatch` lines base vs candidate: **no difference** — dispatch.04 `1225 evaluated: 1197 PASS, 6 FAIL, 22 N/A; 29 out of scope`, dispatch.08 `1217 evaluated: 1178 PASS, 10 FAIL, 29 N/A; 14 out of scope` | PASS |
| census | `scripts/sources-census.sh validate --file $D/corpus/SOURCES.md` | rc 0, final line `file ok …/repo/corpus/SOURCES.md`; **W04 count 34 → 35** (`S277 duplicate url docs.python.org/3/library/subprocess.html across scopes`) | **FAIL vs the item's "W04 unchanged at 34"** |

### Candidate vs plans/round-98-addendum-1.md — finding F2 (headline: the corpus patch predates the L1's own amendment)

`plans/round-98-addendum-1.md` (mtime 08:47, written "after ScribeCorpusR98 and ScoutSourcesR98 reported and
before the landing revision exists") re-points the frontier rows and forbids a new row on the subprocess URL:

| id | addendum 1 (authoritative) | candidate SOURCES.md |
|---|---|---|
| S277 | git-archive(1) — mined | **Python `subprocess` — mined** (the row A1 removes) |
| S278 | proc_pid_environ(5) — mined | git-archive(1) — mined |
| S279 | ptrace(2) — mined | proc_pid_environ(5) — mined |
| S280 | PR_SET_DUMPABLE(2const) — rejected | PR_SET_DUMPABLE(2const) — rejected (match) |

The candidate therefore carries a **one-position shift, a spurious row (S277 subprocess, which A1/Q84 removes
in favour of citing the existing S265) and a missing row (ptrace(2), which A2 admits as S279)**. The Scribe
patch is 08:45 and its READY 08:46, i.e. both predate the 08:47 addendum; the lesson's § Gate cites the same
pre-addendum numbering (S277 subprocess at line 29, S279 proc_pid_environ at line 108) and records the
subprocess row's own W04 at lines 59–67/198.

Consequence: **the candidate as built cannot be the landing revision** — the L1 must have the Scribe re-cut
`ScribeCorpusR98.patch` per addendum 1 (S277 git-archive, S278 proc_pid_environ, S279 ptrace(2), S280
PR_SET_DUMPABLE rejected, subprocess cited as S265), or land the addendum's rows at integration. The W04
34→35 below is the symptom of exactly the row A1 removes; re-cutting per A1 should return the census to 34.
This does not touch C1: the addendum changes no predicate, counting command, kill rule, target or mutant, and
the verifier half of the candidate is unaffected.

### Census W04 deviation — finding F1 (no-harm; caused by F2)

The item's bar is "census `--file` on the candidate SOURCES.md (rc 0, W04 count unchanged at 34)". The
candidate reads **rc 0 but W04 = 35**. Cause: S277 re-registers
`https://docs.python.org/3/library/subprocess.html`, already carried by S263 and S265. Those two rows share
the same scope text (`docs`/A, the run()-vs-communicate() timeout contract), so the same-URL-across-scopes
rule did not fire at the base; S277's scope (the `Popen(env=…)` paragraph) differs, so the rule fires once.
The Scribe's READY discloses it ("W04 34->35 (the S277 duplicate-URL finding)") and the lesson says so at
lines 59–67 and 198; the plan admits S277. So this is a **disclosed deviation from the seat item's
expectation, not a silent regression**: the census stays rc 0 (warnings never change status) and no other
warning class changed. Smallest remediation: drop S277 in favour of the already-registered row, or have the
L1 accept the one warning explicitly at integration.

## 3. Safety

| check | command | observed | verdict |
|---|---|---|---|
| hardcoded /tmp in new code | added-line scan of both patches (`safety_scan.py`) | 0 hits in either patch; base `verifiers/verify_dispatch_prompts.py` has no `/tmp` either | PASS |
| network in self-tests | added-line scan + read of the 183 added lines | 0 hits (`socket`/`urllib`/`http`/`requests`/`subprocess`/`os.environ`/`getenv` absent from added lines); the arms call `lane_of`, `evaluate_dispatch_04/08`, `state_source`, `_verdict_of`, `dispatch_box_sha256`, `box_proof`, `report_paths` only | PASS |
| credential-shaped strings | added-line scan of both patches | 0 hits (`ghp_`, `sk-`, `AKIA`, `BEGIN … PRIVATE KEY`, `password=`/`token=`/`api_key=`) | PASS |
| fixtures only under TMPDIR | read of `lane_case()` and the proof tree in `self_test()` | both build under `root` = `tempfile.TemporaryDirectory(prefix="dispatch-selftest-")`; the new arms write only `case/…`, `map_path`, `proof/SKILL.md`, all under `root` | PASS |
| v6 counter scratch root empty after a run | `find $S/kotoba-r98 -mindepth 1` before/after `selftest-kills.py c1 <cand> $D` | before: 1 entry (the empty root `…/kotoba-r98/selftest-kills`); after: 1 entry (the same empty root); no `run.*` dir, no pristine export tree | PASS |
| Scribe prose mentions | grep of the Scribe patch | one `curl -sS -L …` line in `corpus/lessons/round-98.md:24` — a re-fetch instruction in prose, not executable; `TMPDIR` mentions are prose in the lesson | noted, benign |

## 4. Claim readings observed at the candidate (context; C1/C2 are not my claim)

- `selftest-kills.py c1 <cand> $D` (v6): `C1 targets killed 9 of 9 (run errors 0); positive killed 1 of 1;
  honest CLEAN; comment decoys held 9 of 9; code decoys held 9 of 9`, `rules v6: honest runs CLEAN 3 of 3;
  mirror runs reported 10 of 10; seed ab1d93651683c85d`, `C1-PREDICATE-MET`, rc 0.
- The C1 MET reading also proves the frozen anchors still match exactly once at the candidate: the counter
  applies each mutant with a single-match requirement and reports an anchor miss as could-not-evaluate.

## Files written

- `.ufo/waves/round-98/w1/SentinelScopeR98.md` (this report)
- receipts under `.ufo/waves/round-98/w1/SentinelScopeR98/`: `scope-diff.txt`, `safety-scan.txt`,
  `scratch-cleanliness.txt`, `gate-registry-cand.txt`, `box-proof-cand.txt`, `base-live-dispatch.txt`,
  `cand-live-dispatch.txt`, `census-cand.txt`, `floors-cand.txt`, `v6-c1-cand.txt`,
  `r97-counter-c1-cand.txt`, `r97-counter-r96c1-cand.txt`, `r96-counter-c1-cand.txt`,
  `r96-counter-r95c1-cand.txt`.
- Scratch `/fast/scratch/hyaku/kotoba-r98/SentinelScopeR98/` (removed before yield).

Tool installs: none.
