# SentinelScopeR96 — scope, safety, no-harm on the r96-w1 candidate

Seat: SentinelScopeR96 (sentinel). Lane: kotoba-shokunin. Round 96, wave r96-w1.
Base/freeze commit: `679775abb9277a7b8d17f060b0f5b4ced2b127b6`.
Candidate built in my scratch clone from the two READY patches:
**`9cc4efa920cdf56e6ed9923e5212f1f0731c3bc7`** (ExecArmsR96 then ScribeCorpusR96; scratch identity
`scratch <scratch@invalid>`; `git rev-parse --show-toplevel` == `$D` asserted before every commit).
Scratch: `/fast/scratch/hyaku/kotoba-r96/SentinelScopeR96` (TMPDIR + HYAKU_SCRATCH), removed before yield.
Scratch clone: `/fast/scratch/hyaku/kotoba-r96/SentinelScopeR96/repo` (`git clone --shared`, checked out
at the freeze).

Builder inputs (READY verified before building):
- `ExecArmsR96_READY` — patch sha256 `799bbaac9485587900baeaee0291db2bc5beca97978ab773e2a2d5b770b73088`.
- `ScribeCorpusR96_READY` — patch sha256 `6cb886c3db99eaef7f89d744f47f395624ed31fefeeb3456c30899c0ec1289dd`.
Both `git apply --check` clean at `679775a`; both applied with no fuzz.

## Verdict

**PASS on all three axes.** Scope is exactly the four owned paths; the instrument's production code is
byte-identical outside `self_test()` (one contiguous insertion, base line 799); every no-harm gate holds
at the candidate; the new code carries no `/tmp`, no network, no credential-shaped string, and writes
only under `tempfile`. Two notes, neither a blocker: one mislabelled new assertion (label only) and one
pre-existing red gate that the candidate does not regress.

## (1) Scope

`git -C $D diff --stat 679775a 9cc4efa`:

```
 corpus/README.md                     |   1 +
 corpus/SOURCES.md                    |   2 +
 corpus/lessons/round-96.md           | 206 +++++++++++++++++++++++++++++++++++
 verifiers/verify_dispatch_prompts.py | 128 ++++++++++++++++++++++
 4 files changed, 337 insertions(+)
```

| check | command | observed | verdict |
|---|---|---|---|
| A changed paths are exactly the owned set | `scope_check.py $D 9cc4efa` | `['corpus/README.md','corpus/SOURCES.md','corpus/lessons/round-96.md','verifiers/verify_dispatch_prompts.py']` | PASS |
| C no unowned path | same | `[]` | PASS |
| C no spotcheck/fixture/plan/floors/other verifier | same | `[]` | PASS |
| B SKILL.md byte-identical | `git rev-parse <rev>:SKILL.md` | `e3b2524131a192172f357af3ca0e013511cbeea4` both sides | PASS |
| B SKILL.md 600 lines | same | `600` | PASS |
| D instrument prefix through `run_checks()` byte-identical | `scope_check.py` | prefix 25850 B both sides, equal | PASS |
| D instrument suffix `box_proof()`/`main()` byte-identical | same | suffix 9656 B both sides, equal | PASS |
| D only region changed is the self-test section | same | middle 20829 -> 28544 B; single hunk `@@ -797,6 +797,134 @@ def self_test() -> int:` | PASS |
| E SOURCES.md additions only | `git diff -U0` | no removed line; exactly `S271`,`S272` appended after S270 before `## Paths` | PASS |
| F README additions only, one round-96 row | `git diff -U0` | 1 added line, names `lessons/round-96.md` | PASS |
| G new lesson file present | `git cat-file -e` | present, 206 lines, `## Gate`/`## Mistakes`/`## Status changes`/`## Considerthese`/`## Settlement` | PASS |
| frozen anchors unique (counter contract) | text count at base and candidate | all 11 anchors `base=1 cand=1` | PASS |
| diff is text, insertions only | `git diff --numstat` / `--binary` | `1/0, 2/0, 206/0, 128/0`; 0 binary hunks | PASS |
| base blob linkage | `git diff` index lines | instrument `6e239ae..c6ecbd5`, SOURCES `a8ef375..e0b2ef1`, README `7299890..74e1139` — all match the freeze blobs | PASS |

The instrument change is a single contiguous +128-line insertion inside `self_test()` (base line 799,
after `def self_test` at 679 and before `box_proof()` at 985). My prefix/suffix byte comparison confirms
the executor's `production-identity.txt` independently.

## (2) No-harm at the candidate `9cc4efa`

| check | command | observed | verdict |
|---|---|---|---|
| gate registry | `python3 -B verifiers/check_gate_registry.py --rev 9cc4efa` | `gate registry rows conformant 74 of 74 lane verifiers; phantom 0`, rc 0 (base: same line) | PASS |
| C1 counter | `selftest-kills.py c1 9cc4efa $D` | `C1 targets killed 11 of 11 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 11 of 11; code decoys held 11 of 11` / `C1-PREDICATE-MET`, rc 0 | PASS |
| v4 positive control | `selftest-kills.py r95c1 9cc4efa $D` | `R95C1 targets killed 3 of 3 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 3 of 3; code decoys held 3 of 3` / `R95C1-PREDICATE-MET`, rc 0 | PASS |
| round-95 counter c1 | `verifiers/fixtures/round-95/selftest-kills.py c1 9cc4efa $D` | `C1 targets killed 3 of 3 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 3 of 3; code decoys held 3 of 3` / `C1-PREDICATE-MET`, rc 0 | PASS |
| round-95 counter r94c1 | `verifiers/fixtures/round-95/selftest-kills.py r94c1 9cc4efa $D` | `R94C1 targets killed 3 of 3 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 3 of 3; code decoys held 3 of 3` / `R94C1-PREDICATE-MET`, rc 0 | PASS |
| assertion floors | `python3 -B verifiers/check_assertion_floors.py --self-test` | `0 failure(s) over 176 assertions`, rc 0 | PASS |
| box proof | `python3 -B verifiers/verify_dispatch_prompts.py --box-proof` | `boxes proven 2`, rc 0 | PASS |
| live run, base vs candidate | `verify_dispatch_prompts.py --prompts /home/vgpnk/Projects/shokunin/.ufo/prompts --state-dir /home/vgpnk/Projects/shokunin/.ufo/state` | both rc 1; `diff live-base.txt live-cand.txt` empty (`LIVE-IDENTICAL`) | PASS |
| census on candidate SOURCES.md | `scripts/sources-census.sh validate --file $D/corpus/SOURCES.md` | rc 0, `34` W04 (unchanged), `file ok` | PASS |
| honest self-test | `python3 -B verifiers/verify_dispatch_prompts.py --self-test` | `0 failure(s) over 78 assertions` (base 56; floor 56) | PASS |

Live-run verdict lines are identical at base and candidate (production code unchanged):
`FAIL dispatch.04: evaluated 1219 — 1191 PASS, 6 FAIL, 22 N/A; 29 out of scope; ...` and
`FAIL dispatch.08: evaluated 1211 — 1172 PASS, 10 FAIL, 29 N/A; 14 out of scope; ...`.

Base-side controls I measured myself (so the candidate rows are not taken on trust):
`selftest-kills.py c1` at `679775a` -> `C1 targets killed 0 of 11` / `C1-PREDICATE-UNMET`, rc 1;
`r95c1` at `679775a` -> MET, rc 0; round-95 `c1`/`r94c1` at `679775a` -> both MET, rc 0.

## (3) Safety

| check | method | observed | verdict |
|---|---|---|---|
| no hardcoded `/tmp` in new code | `grep -n '/tmp'` over the added lines of both patches | none | PASS |
| no network in self-tests | `grep -niE 'socket\|urllib\|http.client\|requests\.\|curl\|wget\|urlopen\|open_connection'` over added instrument lines | none | PASS |
| no credential-shaped strings | `grep -niE 'api[_-]?key\|secret\|password\|BEGIN .*PRIVATE\|AKIA\|ghp_\|sk-[A-Za-z0-9]{8}'` | instrument: only the word "token" in two comments about round tokens (benign); scribe: none | PASS |
| fixtures only under TMPDIR | read of the added arms | every fixture goes through `_write_case(root, ...)` with `root = Path(tmp)` from `tempfile.TemporaryDirectory`; no absolute-path `open()`/`mkdir`/`Path()` in the added lines | PASS |
| no self-source reading in the new arms | `grep -nE '__file__\|inspect\|linecache\|tokenize\|dis\.\|ast\.\|read_text\|open\('` | none | PASS |
| no subprocess / env dependence | `grep -nE 'subprocess\|os.system\|popen\|os.environ\|getenv'` | none | PASS |
| no eval/exec/compile, no destructive fs, no time/random | `grep -nE '\b(eval\|exec\|compile)\(\|remove\|unlink\|rmtree\|rename\|chmod\|symlink\|time\.\|random\|datetime'` | none | PASS |
| assertions reported, never crashed | AST audit of `self_test()` | 62 `rec(...)` call sites (18 added sites -> 22 assertions via 2 loops), 0 bare `assert`, 0 added `raise`, 0 `print`, 0 `sys.exit`, 0 added imports | PASS |
| scribe patch is prose + two registry rows | `git diff -U2` | SOURCES rows S271/S272 appended in the Registry table; README one row; lesson is a scaffold | PASS |

The `curl` mentions in the scribe lesson are prose in the access record (how the source was fetched
and hashed), not executable code in the lane.

## Findings

1. **LOW — one new assertion is mislabelled.** In the t11 block the last assertion reads
   `rec("t05-finish-allna-pass: the no-report-path dispatch.04 evaluates 1", r["evaluated"] == 1, ...)`
   while it observes the t11 fixture (`noreport`). It still counts and is behavioural, and the t11 arm's
   own kill rests on the five correctly-labelled t11 assertions; the convention "every new self-test
   assertion names the arm it guards" is violated in the label only. Smallest remediation: rename the
   label to `t11-noreport-04-pass: ...` (no behaviour change). Not a blocker for C1.
2. **Carried red gate, not a regression.** `python3 -B verifiers/check_sources_append_only.py --rev`
   reads `sources append-only breach 19 change(s) in 9 of 62 commits`, rc 1 at the freeze and
   `19 change(s) in 9 of 63 commits`, rc 1 at the candidate — the same 19 pre-existing breaches in the
   same 9 old commits; the candidate commit is not a breacher. This is one of the plan's carried
   "three long-standing red gates"; the scribe's two appended rows do not add a breach.
3. **Floor is a floor.** The candidate reports 78 assertions against the registry floor of 56 for
   `dispatch_prompts`; no floors edit was made (scope check confirms `verifiers/floors-registry.json`
   untouched), and the plan states raising it is not claimed.
4. **Candidate revision is scratch-only.** `9cc4efa` exists only in my scratch clone; the L1 rebuilds
   from the two READY patches named above.

## Evidence log (copied to this seat's receipt dir)

- `c1-cand.txt` — C1 counter at `9cc4efa`: MET, 11 of 11, rc 0.
- `r95c1-cand.txt` — R95C1 positive control at `9cc4efa`: MET, rc 0.
- `r95c1-r95-cand.txt` — round-95 `c1` at `9cc4efa`: MET, rc 0.
- `r94c1-cand.txt` — round-95 `r94c1` at `9cc4efa`: MET, rc 0.
- `census-base.txt` (34 W04, rc 0) vs `census-cand.txt` (34 W04, rc 0).
- `live-base.txt` vs `live-cand.txt` — byte-identical.
- `append-base.txt` vs `append-cand.txt` — same 19 breaches; denominator 62 -> 63.
- `scope-cand.txt` — the scope run (`scope fails: 0`, rc 0); `scope_check.py` — the checker (scratch tool,
  never in the lane); `added-lines.txt`, `scribe-added.txt` — the scanned added lines.

## Risks / notes

- No host/kernel setting was changed; no package was installed; no network was used by any counter or
  self-test I ran.
- The lesson file is a scaffold with `<pending>` settlement fields by design; the L1 completes them.
