# CritK69Sandbox — round 70 wave 1: independent test of lesson M116 (K69-11 in a /tmp sandbox)

## Verdict

**M116 holds on its mechanism.** The frozen item K69-11, as the C1 counter runs it, cannot pass in
any `/tmp` placement at any revision from the base to the tip. It also has **no discriminating power**:
it reads FAIL both before the repair (`7d51253`) and after it (`8edeb49` onward). The same gate in a
fleet-shaped placement flips FAIL→PASS exactly at `8edeb49`, the commit where the repair lands.

**Placement answer:**

- **The frozen item can't be satisfied from any sandbox placement.** The counter creates a fresh
  `tempfile.TemporaryDirectory(prefix="k70-c1-")` and clones into `<tmp>/clone`. Every dead token is a
  one-hop `../` token, so it resolves against that fresh, empty directory. This holds even when
  `TMPDIR` points inside a full fleet mirror (finding 5).
- **A hand-built `/tmp` placement can satisfy the gate.** It needs a parent directory that mirrors the
  fleet root (symlinks to every fleet entry) with the clone named `kotoba-shokunin` inside it. That is
  a different world from the one the frozen item executes, so it does not rescue C1.

**Calibration defects in the lesson text** (wording only; the mechanism and the miss-as-declared are
unaffected):

- **(a) The "30+ other `../.ufo/…` tokens" count is wrong.**
  - The gate's dead list has 34 entries:
    - the 3 corrections;
    - 3 stale in-repo subjects that lose their excuse because those corrections fail;
    - 28 one-hop subject occurrences.
  - Of the 28 one-hop occurrences, only 15 are `../.ufo…`. The other 13 are other fleet-root paths:
    `../AXES.md`, `../PROTOCOL.md`, `../MISSION.md`, `../SCORECARD.md` and `../kasegi-shokunin/…`.
  - By unique token: 12 are `../.ufo…` and 7 are other fleet paths.
- **(b) "at every revision" is only true conditionally.** I observed it for all 8 revisions
  `7d51253^..16b212a`. The counter runs the gate from the `--rev` checkout, so a future revision that
  changes `citation_resolve` could pass. Such a revision would change the instrument after data, which
  the plan forbids ("no item is narrowed after data").

## Findings

### 1. Sandbox run at the tip: `governance.citation_resolves` FAIL

```
S=$(mktemp -d /tmp/k70w1-CritK69Sandbox.XXXX)   # -> /tmp/k70w1-CritK69Sandbox.Nx57
git clone -q --shared /home/vgpnk/Projects/shokunin/kotoba-shokunin $S/lane
git -C $S/lane checkout -q 16b212a390c7ce68b6bce49b2c3766b154fbcbae   # rev-parse = 16b212a…, porcelain 0 lines
cd $S/lane && python3 -B verifiers/verify_skill_checklist.py --json
```

Observed: `exit=1`, summary `{'exit_code': 1, 'fail': 3, 'na': 0, 'pass': 8}`. The failing checks are
`trigger.name_directory` (the clone directory is named `lane`), `trigger.citation_resolves` and
`governance.citation_resolves`. Detail of `governance.citation_resolves` (verbatim; `evaluated: 1256`):

> correction LOG.md:2619 LOG.md:2533 '.ufo/reports/round-60/kotoba.md': corrected token '../.ufo/reports/round-60/kotoba.md' does not resolve; correction LOG.md:2620 LOG.md:2580 '.ufo/watchdog.log': corrected token '../.ufo/watchdog.log' does not resolve; correction LOG.md:2621 SCORECARD.md:158 '.ufo/reports/round-60/kotoba.md': corrected token '../.ufo/reports/round-60/kotoba.md' does not resolve; LOG.md:177: '../.ufo/reports/round-9/kotoba.md' does not resolve from /tmp/k70w1-CritK69Sandbox.Nx57/lane … (+30 more); 10 quoted meta-finding(s), 3 schematic token(s) excluded, 1 recorded absence(s) excused, 2 recorded correction(s) excused

### 2. Real lane, read-only, same tip: 11/11 PASS

```
cd /home/vgpnk/Projects/shokunin/kotoba-shokunin && git rev-parse HEAD   # 16b212a390c7ce68b6bce49b2c3766b154fbcbae
git status --porcelain     # only ?? .ufo/waves/round-70/w1-dispatch.{err,json}, w1-spec.json, w1/  (untracked wave files; unchanged after the run)
python3 -B verifiers/verify_skill_checklist.py --json
```

Observed: `exit=0`, `{'exit_code': 0, 'fail': 0, 'na': 0, 'pass': 11}`, and
`governance.citation_resolves PASS` with `evaluated: 1253`:

> 1253 governance citation token(s) resolve across 2 files; 10 quoted meta-finding(s), 3 schematic token(s) excluded, 1 recorded absence(s) excused, 5 recorded correction(s) excused

### 3. Root cause in the gate source

```
rg -n 'def citation_resolve' -A 30 verifiers/verify_skill_checklist.py
```

`verifiers/verify_skill_checklist.py:1523-1546`: a token without `..` goes to `safe_resolve(tok, repo,
repo)`. A token with leading `..` hops is resolved as follows:

```
base = repo
for _ in range(hops):
    base = base.parent
return (base / "/".join(parts)).exists()
```

The existence test is therefore made against the checkout's filesystem ancestors, not against the git
object store or the clone's origin. `../X` means `<checkout parent>/X`. That parent is the fleet root
(`/home/vgpnk/Projects/shokunin`) only when the checkout is the real lane.

The callers are:

- the subject loop, `:1803`;
- the correction rows, `:1736` (stale must not resolve) and `:1738` (corrected must resolve);
- the errata rows, `:1701`.

So a dead one-hop corrected token has two effects: the correction itself is reported, and its stale
subject loses its excuse.

**Instrument for the token breakdown.** I wrote a scratch spy at `$S/dead_tokens.py`, since deleted.
It wraps `g.citation_resolve` and calls
`g.check_governance_citations(repo, corrections=g.GOVERNANCE_CORRECTIONS)`, the same call `main` makes
at `:2773`.

| placement | status | dead calls | unique dead | one-hop unique |
|---|---|---|---|---|
| `/tmp/…/lane` (plain clone) | FAIL | 40 | 24 | 19 |
| `/tmp/…/linked/kotoba-shokunin` + `../.ufo` symlink only | FAIL | 19 | 12 | 7 |
| real lane | PASS | 6 | 5 | 0 |

**What the table shows:**

- **The real lane's dead set is excused.** Its five dead tokens are all in-repo:
  - `.ufo/reports/round-60/kotoba.md`
  - `.ufo/watchdog.log`
  - `.ufo/round-45/drafts/v10/post-r44-hunt.py`
  - `.ufo/waves/round-67/w1/controls/census-validate-append.txt`
  - `.ufo/waves/round-67/w1/controls/junk-world/`

  They are the stale-side and recorded-absence probes, where a dead result is the expected one.
- **The only cause of the sandbox red is the one-hop tokens.** The sandbox has exactly the same five
  in-repo dead tokens as the real lane, so no in-repo token depends on untracked files. The 19
  sandbox-only dead tokens are all one-hop:
  - 12 unique `../.ufo…` tokens, e.g. `../.ufo/l0-questions.md` (5 calls) and `../.ufo/reports/round-{9,11,16,58,59,60,62}/kotoba.md`;
  - `../AXES.md` (4 calls), `../PROTOCOL.md` (2), `../MISSION.md` (1), `../SCORECARD.md` (1);
  - `../kasegi-shokunin/corpus/instruments/{,resolve.py,anchorcheck.py}` (1+2+2).
- **A `.ufo` symlink alone is not enough.** It clears the three corrections, but `../PROTOCOL.md`,
  `../kasegi-shokunin/…` and the others still FAIL. Observed detail:
  `LOG.md:311: '../PROTOCOL.md' does not resolve …; LOG.md:824: '../kasegi-shokunin/corpus/instruments/resolve.py' does not resolve …`.

**Occurrence arithmetic for calibration defect (a).** In the plain sandbox there are 31 one-hop dead
calls, 18 of them `../.ufo*`.

- 3 of those are correction checks, so 28 are subject occurrences: 15 `../.ufo…` and 13 non-`.ufo`.
- The 3 stale subjects lose their excuse. `.ufo/reports/round-60/kotoba.md` has 4 calls (2 stale
  checks + 2 subject failures) and `.ufo/watchdog.log` has 2 calls (1 + 1).
- Total: 3 + 3 + 28 = 34, which matches the gate's "4 shown + 30 more".

M116 says "30+ other `../.ufo/…` tokens". The true breakdown is 15 `../.ufo` occurrences, plus 13
other fleet-root occurrences, plus 3 un-excused in-repo stale subjects.

### 4. Discrimination sweep: plain `/tmp` versus a fleet-mirror placement under `/tmp`

**Mirror setup:** `$S/mirror/` holds 45 symlinks, one to each entry of `/home/vgpnk/Projects/shokunin`
except `kotoba-shokunin`. The clone sits at `$S/mirror/kotoba-shokunin`. I ran this for every
revision in `git rev-list --reverse 7d51253^..16b212a` (7 commits after the base, plus the base).

```
7d51253f9 plain FAIL 8P/3F    mirror FAIL 10P/1F
0b561744e plain FAIL 8P/3F    mirror FAIL 10P/1F
53de0ac9b plain FAIL 8P/3F    mirror FAIL 10P/1F
a647fa734 plain FAIL 8P/3F    mirror FAIL 10P/1F
8edeb4900 plain FAIL 8P/3F    mirror PASS 11P/0F
aa9c9adf8 plain FAIL 8P/3F    mirror PASS 11P/0F
ac3c0f14d plain FAIL 8P/3F    mirror PASS 11P/0F
16b212a39 plain FAIL 8P/3F    mirror PASS 11P/0F
```

**What the sweep shows:**

- **The mirror reproduces the real lane.** At the base, the mirror's red is
  `LOG.md:2676: '.ufo/waves/round-67/w1/controls/census-validate-append.txt' does not resolve …; LOG.md:2678: '.ufo/waves/round-67/w1/controls/junk-world/' does not resolve …`.
  That is exactly the inherited K69-11 red named in `corpus/lessons/round-69-verifier-spotcheck.md:208-212`.
  At `8edeb49` and the tip, the mirror reads 11/11 PASS, with the same 1253 / 5-corrections detail as
  the real lane.
- **The receipt's base comparison is now corroborated.** The committed receipt
  `.ufo/waves/round-70/receipts/K69-11-inplace.txt` (at `ac3c0f1`) reports only a recalled base reading
  for `7d51253` ("the L1's round-start run"), not a re-run. Its claim matches the mirror reading at the
  base above.
- **The plain sandbox cannot tell the two states apart.** It reads FAIL 8P/3F at every revision,
  before and after the repair.

This confirms M116's sentence "the item reads FAIL at every revision, repaired or not", for all 8
revisions that exist.

### 5. The counter's own path stays unsatisfiable, even with `TMPDIR` inside a fleet mirror

```
cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
TMPDIR=$S/tmpdir   python3 -B verifiers/check_r69_routed_repairs.py --rev 16b212a390c7ce68b6bce49b2c3766b154fbcbae
TMPDIR=$S/mirror   python3 -B verifiers/check_r69_routed_repairs.py --rev 16b212a390c7ce68b6bce49b2c3766b154fbcbae
```

Both runs printed `measured-rev: 16b212a…`, `r69 routed defects closed 9 of 10`,
`  K69-11: governance.citation_resolves FAIL`, `exit=1`. The lane's porcelain output was unchanged and
the temporary directory was cleaned up.

The source shows why (`verifiers/check_r69_routed_repairs.py:101-121`):

- the counter uses `tempfile.TemporaryDirectory(prefix="k70-c1-")`, then `clone = Path(tmp) / "clone"`;
- it runs `python3 -B <clone>/verifiers/verify_skill_checklist.py --json` with `cwd=clone`.

The clone's parent is always a freshly created, empty directory with a random name. No choice of
`TMPDIR` can place fleet entries beside `clone`, so every one-hop token stays dead.

Two routes could still turn K69-11 green under this counter:

- **Rewrite all 19 one-hop tokens.** They sit in append-only historical `LOG.md`/`SCORECARD.md` lines,
  which is why the round-65 correction mechanism exists. Rewriting them would break the lane's governance.
- **Ship a revision whose gate resolves `..` differently**, for example against the shared clone's
  origin. The counter executes the gate from `--rev`, so this would work, but it changes the instrument
  after data.

Neither route is a sandbox placement. Both are content changes the frozen plan forbids after data.

### 6. Capture claim ("Captured by: none … the self-test's honest world used a fake repo") holds

`verifiers/check_r69_routed_repairs.py:281-284`: the self-test's `checklist()` returns
`{"checks": [{"id": "governance.citation_resolves", "status": self.gate_status}]}` from a stub field.
The honest world never runs the real gate in a real sandbox, so the self-test could not have exposed
the one-hop resolution.

## Impacted axes

- **Consistency (C1).** The 9 of 10 reading is a structural miss of the item, not evidence about the
  repair. The repair itself is shown real by the mirror and in-place readings (FAIL at the base, PASS
  from `8edeb49`). C1 correctly stands as a miss as declared.
- **Calibration.** The M116 wording has two defects, (a) and (b), listed under the verdict.

## Smallest safe corrections

These are for the lane owner. I made no edits.

1. **Append a count correction to the round-70 lesson.** Do not edit M116 in place. Suggested text:
   the sandbox red is 34 entries = 3 corrections + 3 un-excused stale subjects + 28 one-hop
   occurrences (15 `../.ufo…`, 13 other fleet-root paths: `../AXES.md`, `../PROTOCOL.md`,
   `../MISSION.md`, `../SCORECARD.md`, `../kasegi-shokunin/…`).
2. **Qualify "at every revision".** Change it to "at every revision `7d51253..16b212a` (8 checked)"
   and add "for any revision whose gate resolves `..` against the checkout's parent".
3. **For future frozen sandbox items:** clone into `<tmp>/<fleet-mirror>/kotoba-shokunin`, with the
   parent populated by symlinks to the fleet root's entries. This placement discriminates (base FAIL,
   repair PASS) and reproduces the in-place reading. Alternatively, run the item once on an honest real
   world before freezing, which is M116's own fix.

## Not observed

- The counter's `--self-test` was not run.
- `trigger.name_directory` and `trigger.citation_resolves` in the sandbox are outside K69-11 and were
  only noted.
- I did not test revisions outside `7d51253^..16b212a`.

## Tooling

No installs or updates.

## Hygiene

- All scratch was under `/tmp/k70w1-CritK69Sandbox.Nx57`: shared clones `lane`, `named`, `linked`,
  `mirror`, `sweep`, the symlink mirror, JSON outputs and `dead_tokens.py`. It was deleted before
  returning.
- I made no writes to the lane, the fleet repository, jj or the Git index.
- **Tracked files changed during my run, not by me.** A final `git status --porcelain` in the lane
  shows ` M` on `corpus/README.md`, `corpus/knowledge/skill-eval-artefacts-round70.md`,
  `corpus/lessons/round-70.md` and `verifiers/verify_skill_checklist.py`. These are sibling-seat edits
  made while I worked. My real-lane gate run (finding 2) was taken when porcelain showed only the
  untracked `??` wave files, before and after the run. Every sandbox and mirror reading is pinned to
  committed revisions, so the working-tree edits cannot affect them.
