# ExecNoHarm — round 70 wave 1: no-harm battery at 16b212a3, by location

**Verdict.** At the measured tip `16b212a390c7ce68b6bce49b2c3766b154fbcbae`, all five checks exit 0 in
the lane checkout. In a `git clone --shared` sandbox whose `..` is not the fleet root, two of the
five exit 1: `verify_skill_checklist.py --json` and `check_assertion_floors.py`. Both failures come
from one cause: `../`-hop citations in `SKILL.md`, `LOG.md` and `SCORECARD.md` resolve against the
clone's parent directory. A control that symlinks the fleet root's top-level entries into the
sandbox parent turns both checks back to exit 0, with no other change. The other three checks give
byte-identical stdout in both locations. They do not depend on where the clone sits, but they do
depend on the host, because they hard-code the fleet root path.

Scope note: the plan's battery (`plans/round-70.md:110-114`) also lists the census `validate`. That
check was not in this assignment and I did not run it.

## Setup (commands as run)

```
D=$(mktemp -d /tmp/k70w1-ExecNoHarm.XXXX)          # -> /tmp/k70w1-ExecNoHarm.zxIR
git clone -q --shared /home/vgpnk/Projects/shokunin/kotoba-shokunin "$D/kotoba-shokunin"
cd "$D/kotoba-shokunin" && git checkout -q --detach 16b212a390c7ce68b6bce49b2c3766b154fbcbae
git rev-parse HEAD   -> 16b212a390c7ce68b6bce49b2c3766b154fbcbae
ls ..                -> kotoba-shokunin              (parent = /tmp/k70w1-ExecNoHarm.zxIR, not the fleet root)
git status --porcelain | wc -l -> 0
```

The lane checkout was at the same commit: `git rev-parse HEAD` printed `16b212a390c7ce68b6bce49b2c3766b154fbcbae`.
Its `git status --porcelain` was captured before the lane runs and diffed after them, and the diff
printed `status-unchanged`. The only entries were the pre-existing untracked
`.ufo/waves/round-70/w1-dispatch.{err,json}`, `w1-spec.json` and `w1/`. All runs used
`python3 -B` (Python 3.14.8, git 2.56.0), with `timeout 290` on each.

## Exit codes per location

| check | sandbox (`..` = /tmp dir) | lane (`..` = fleet root) | sandbox + fleet-entry symlinks at `..` |
|---|---|---|---|
| `verify_skill_checklist.py --json` | **1** | 0 | 0 |
| `verify_corpus_integrity.py` | 0 | 0 | not re-run |
| `verify_corpus_independent.py --json` | 0 | 0 | not re-run |
| `check_gate_registry.py --rev 16b212a3…` | 0 | 0 | not re-run |
| `check_assertion_floors.py` | **1** | 0 | 0 |

Raw sandbox output: `checklist exit=1 / integrity exit=0 / independent exit=0 / gatereg exit=0 / floors exit=1`.
Raw lane output: `checklist exit=0 / integrity exit=0 / independent exit=0 / gatereg exit=0 / floors exit=0`.

## Finding 1: the checklist fails only because of where the clone sits

Sandbox `verify_skill_checklist.py --json` printed `{'exit_code': 1, 'fail': 2, 'na': 0, 'pass': 9}`.
The two failing checks:

- `trigger.citation_resolves FAIL 181`, with detail `line 590: '../.ufo/reports/round-7/kotoba.md' does not resolve from /tmp/k70w1-ExecNoHarm.zxIR/kotoba-shokunin`.
  `git show 16b212a3:SKILL.md | sed -n 590p` prints `` `../.ufo/reports/round-7/kotoba.md`, not in the artifact. Loss figures ``.
- `governance.citation_resolves FAIL 1256`, with detail `correction LOG.md:2619 LOG.md:2533 '.ufo/reports/round-60/kotoba.md': corrected token '../.ufo/reports/round-60/kotoba.md' does not resolve; correction LOG.md:2620 LOG.md:2580 '.ufo/watchdog.log': corrected token '../.ufo/watchdog.log' does not resolve; correction LOG.md:2621 SCORECARD.md:158 …; LOG.md:177: '../.ufo/reports/round-9/kotoba.md' does not resolve … (+30 more); … 1 recorded absence(s) excused, 2 recorded correction(s) excused`.

The same checks in the lane: `trigger.citation_resolves PASS 181` and `governance.citation_resolves PASS 1253`,
`… 5 recorded correction(s) excused`. The evaluated count differs by 3 (1256 against 1253) because, in
the sandbox, the three round-65 corrections at `LOG.md:2619-2621` stop being excused (5 excused
becomes 2) and are counted as evaluated failures instead.

Mechanism. `verifiers/verify_skill_checklist.py:309` sets `DEFAULT_REPO = Path(__file__).resolve().parent.parent`,
and `:393` sets `CITATION_ROOTS = ("corpus/", "verifiers/", "opencode/", ".ufo/", "../")`. A `../` token
therefore resolves from the clone's parent directory.

The other nine checks are identical in both locations, including `trigger.line_budget PASS 600`.
`git show 16b212a3:SKILL.md | wc -l` prints `600`, so the 600-line limit holds with no room to spare.

**Control A.** Linking only `.ufo` at `..` (`ln -s /home/vgpnk/Projects/shokunin/.ufo $D/.ufo`) gave
`ctl-checklist exit=1`, with `trigger.citation_resolves PASS 181` but `governance.citation_resolves FAIL 1253`:
`LOG.md:311: '../PROTOCOL.md' …; LOG.md:824: '../kasegi-shokunin/corpus/instruments/resolve.py' …;
'../kasegi-shokunin/corpus/instruments/anchorcheck.py' …; LOG.md:1203: '../AXES.md' … (+9 more)`.
Governance citations also reach fleet-root files (`PROTOCOL.md`, `AXES.md`) and sibling lanes.

**Control B.** Linking every top-level fleet-root entry except `kotoba-shokunin` (`linked=45`) into
`$D` gave `ctl2-checklist exit=0`, with `trigger.citation_resolves PASS 181` and
`governance.citation_resolves PASS 1253 … 5 recorded correction(s) excused`. This is identical to the
lane result. It isolates the parent directory's contents as the only cause. The symlinks were removed
afterwards (`find $D -maxdepth 1 -type l -delete`, after which `ls -A $D` printed `kotoba-shokunin out`).

## Finding 2: the floors failure is inherited from the checklist self-test

Sandbox `check_assertion_floors.py` printed one failure, `FAIL checklist observed=1862 floor=1862 self_test_failures=1`.
Every other row was PASS (harness 10, corpus_integrity 161, corpus_independent 103, surfaces 175,
pins 62, harness_independent 123, compare_harness_independent 330, floors_guard 165/150,
dispatch_prompts 56, sibling_census 68, overlap_levers 55/51, alwayson 89, correction_sweep 25,
scoped_rules_v32 240).

To find the failing assertion, I ran `python3 -B verifiers/verify_skill_checklist.py --self-test` in
the sandbox. It exited 1 with `self-test FAIL: governance: live round-65 corrections land, check PASS: got ('FAIL', 1256, …)`
and `1 failure(s) over 1862 assertions`. That self-test assertion checks the live repository's
governance citations, so it carries Finding 1's location dependence.
`check_assertion_floors.py:616-617` runs each child `--self-test` with `cwd=repo`, and `:156` sets
`DEFAULT_REPO = Path(__file__).resolve().parent.parent`. The floors failure is that same assertion,
not a separate defect. Under Control A the result was still `FAIL checklist … self_test_failures=1`.
Under Control B it was `PASS checklist observed=1862 floor=1862` with `ctl2-floors exit=0`.

## Finding 3: integrity and independent do not depend on location, but they are tied to this host

Comparing sandbox and lane stdout, with the repo path normalised (`sed "s#<repo>#REPO#g" | diff`),
printed `identical-stdout` for `verify_corpus_integrity.py`, `verify_corpus_independent.py --json` and
`check_gate_registry.py`. All stderr files were 0 bytes.

Sandbox integrity printed `9/9 checks pass` and
`corpus.pointers report_dead=0/89 commit_total=39 unresolvable=0 nonhash=0 (shapes [relative=1, absolute=44, tilde=1, bare=43] …)`.
The pointer shapes explain why these checks pass in both locations:

- **One relative pointer.** `corpus/README.md:58` cites `` `../.ufo/reports/round-23/kotoba.md` `` from `corpus/`.
  That resolves to the clone's own `.ufo/reports/round-23/kotoba.md`, which is tracked in the lane
  (`git cat-file -e 16b212a3:.ufo/reports/round-23/kotoba.md` printed `tracked-in-lane`). It never
  reaches `..`. The fleet copy does not exist (`ls /home/vgpnk/Projects/shokunin/.ufo/reports/round-23/kotoba.md` printed `No such file or directory`).
- **The other pointers use fixed or home-relative paths.** There are 44 host-absolute pointers and 1
  `~/` pointer (`corpus/lessons/round-1-aggregator-audit.md:9`). The 43 bare `.ufo/reports/…` pointers
  fall back to a hard-coded constant:
  - `verify_corpus_integrity.py:125` sets `FLEET_ROOT = Path("/home/vgpnk/Projects/shokunin")`, and `:270-274` checks the citing directory, then `fleet_root / token`.
  - `verify_corpus_independent.py:44` sets `FLEET_ROOT = "/home/vgpnk/Projects/shokunin"`, and `:263-268` does the same.
  - Commit citations fall back to the same constant (`verify_corpus_integrity.py:591`, `verify_corpus_independent.py:489-491`).

[INFERENCE] On a host without `/home/vgpnk/Projects/shokunin` (or without the same `.ufo/reports`
content there), the bare and absolute pointers would read dead. I did not exercise this, because
moving the constant would mean editing a committed verifier.

`check_gate_registry.py` printed `gate registry rows conformant 51 of 51 lane verifiers; phantom 0` in
both locations. It reads only `git -C LANE` (`:67` sets `LANE = Path(__file__).resolve().parent.parent`,
and `:108-109` runs git there), so it works from the clone's own object database and never looks
outside the repo.

## Relevance to C1 / K69-11 (data, not a verdict)

`verifiers/check_r69_routed_repairs.py:103-116` builds its K69-11 sandbox at
`tempfile.TemporaryDirectory(prefix="k70-c1-")/clone` and runs the checklist with `cwd=clone`. That
sandbox's `..` is a temporary directory, the same situation as my sandbox, where
`governance.citation_resolves` read `FAIL 1256`. These measurements reproduce the mechanism behind
lesson M116, for which the plan already accepts a miss. A sandbox whose parent holds the fleet-root
entries reads PASS (Control B). I did not run `check_r69_routed_repairs.py` itself, because it is
outside this item's scope.

## Risks

- `trigger.line_budget` sits exactly at its limit (600 of 600). Any SKILL.md growth in this round fails the no-harm battery unless lines are removed elsewhere.
- Whether the checklist passes depends on where it runs. A battery run from any sandbox not placed beside the fleet entries reports a false regression: 2 checks red, plus the floors failure that follows from them.

## Files, tools, cleanup

- Working-tree drift after measurement: when this seat finished, `git status --porcelain` in the lane showed ` M corpus/README.md`, ` M corpus/knowledge/skill-eval-artefacts-round70.md`, ` M corpus/lessons/round-70.md` and ` M verifiers/verify_skill_checklist.py`. These are another seat's or the L1's edits, made after my lane runs; the before/after status diff around those runs printed `status-unchanged`. The lane exits above are therefore for the clean tip `16b212a3`, not for the current working tree. The sandbox numbers are for the committed tip in any case.
- Files changed: this report only. No committed lane file, fleet file, jj state or Git index was touched.
- Tools installed or updated: none.
- Scratch `/tmp/k70w1-ExecNoHarm.zxIR` (the clone and its outputs) is deleted before this seat returns.
