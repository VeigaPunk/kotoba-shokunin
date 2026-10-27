# Kb79E04DeadPointer — C1 repair 4 of 4: the one dead report pointer

Seat: executor, round 79 wave w1 (leaf, no spawns). Lane base for every measurement:
`b10bcbc6b00f8f56b202ccbadca311007b5b463c`; scratch trees sit on plan-freeze commit
`2c56622375641193a03bb97c0624e6536f3dffba` (`git diff b10bcbc 2c56622 -- corpus/` is empty, so the
corpus I measured is the C1 base corpus).

Scratch: `/fast/scratch/hyaku/kotoba-r79/Kb79E04DeadPointer/{clone,w7,applycheck}` (clone at the plan
commit, `.git` asserted via `git rev-parse --show-toplevel` before every mutation). Receipts:
`.ufo/waves/round-79/build/Kb79E04DeadPointer/`. No tool was installed; pacman was not invoked; no
background service; scratch removed before yield (see §9).

## 1. The disagreement, measured (why the two gates read the same bytes differently)

`corpus/lessons/round-77-verifier-spotcheck.md:15` cites the fleet report as a git object expression:

```
| Report shape | `git show HEAD:.ufo/reports/round-77/kotoba.md` headings → … | conformant, real report, not marker |
```

Receipt `tokenizers-base-vs-independent.txt` (integrity module loaded from the **base bytes**
`git show 2c56622:verifiers/verify_corpus_integrity.py`, `--json` sites for the corpus):

```
integrity(BASE bytes) UFO_POINTER_RE tokens: ['HEAD:.ufo/reports/round-77/kotoba.md']
independent           pointer_tokens:       ['.ufo/reports/round-77/kotoba.md']
integrity BASE  report_pointer_exists('HEAD:.ufo/reports/round-77/kotoba.md'): False  -> report_dead
independent     report_pointer_exists('.ufo/reports/round-77/kotoba.md'): True  -> alive
fleet HEAD carries HEAD:.ufo/reports/round-77/kotoba.md: True
lane  HEAD carries HEAD:.ufo/reports/round-77/kotoba.md: False
```

Root cause is the token boundary, not the resolution:

- `verify_corpus_integrity.py:146-148` `UFO_POINTER_RE` has a lazy prefix
  `(?:/|~|(?:\.\.?/)*)[^\s`\"]*?\.ufo/…`: from the backtick the prefix swallows `HEAD:`, so the token
  is the whole object expression. `report_pointer_exists` (:273-277, base bytes) then resolves it as a
  **working-tree path** from `corpus/lessons` (`…/corpus/lessons/HEAD:.ufo/…` → absent) and never
  reaches the fleet hop, whose gate is `token.startswith(".ufo/reports/")` — false for a prefixed token.
- `verify_corpus_independent.py:123-125` `POINTER_RE` starts its leading class with
  `[^\s`"()\[\],;:]*` — `:` is excluded, so the token is the path only, and its fleet-root hop
  (`:265-270`) finds `/home/vgpnk/Projects/shokunin/.ufo/reports/round-77/kotoba.md`.

Base values (lane): `report_dead=1/106` (integrity, DRIFT vs `0 / empty`) and `points … dead=0`
(independent) — the same corpus, two verdicts.

## 2. The principled fix: resolve the revision, not the working tree

`<rev>:<path>` is a **git object expression**, not a path of the citing working tree. The report it
names lives in the **fleet** repository, which is why the citing directory can never hold it. Decision:

- **Not an exclusion.** The item keeps honest detection for "a `HEAD:` form naming a path that does not
  exist in the repo it is resolved against"; excluding the class deletes that verdict. The existing
  `pointer-excluded` classes are placeholders/globs/whitespace — schematic shapes, not real
  citations; this token is a real, truthful citation.
- **Not a working-tree resolution** (the independent gate's current reading). Measured
  (`revision-vs-worktree.txt`, repair bytes): an **untracked** file at
  `.ufo/reports/round-9/untracked.md` in the citing repo gives
  `HEAD:.ufo/reports/round-9/untracked.md` → `False` (dead), while the fleet's committed
  `HEAD:.ufo/reports/round-77/kotoba.md` → `True`. A revision-resolving predicate cannot be bought by
  an uncommitted file; a working-tree predicate can.
- **Resolved lane-first, then fleet**, the same hop `commit_resolves` already uses for commit citations
  (`:600-612`, marker `COMMIT_HOP_MARKER`): the citing repository is the nearest ancestor of the citing
  directory carrying `.git` (a directory in a clone, a file in a worktree), then the fleet root; the
  object must exist in that revision (`git cat-file -e <rev>:<path>`).

Patch (`Kb79E04DeadPointer.patch`, 17 insertions, 0 deletions,
sha256 `d7169dd8f9db17a908f00c1e62a668d73c7ca96cca75626807fb81889f4a5d78`):

```python
def report_pointer_exists(base: Path, token: str, fleet_root: Path = FLEET_ROOT) -> bool:
    """Check the citing directory first, then the fleet root for bare report paths."""
    head, _, rest = token.partition(":")
    if head and rest.startswith(".ufo/reports/"):  # `<rev>:<path>`: a revision, not a tree path
        at = base.resolve()  # the citing repository first, then the fleet root
        lane = next((p for p in (at, *at.parents) if (p / ".git").exists()), None)
        return bool(lane) and git_ok(lane, "cat-file", "-e", token) or git_ok(
            fleet_root, "cat-file", "-e", token)
```

`verify_corpus_independent.py` is **untouched**: its current verdict (alive) is already the corpus
answer, and it is a pinned instrument (see §7 B1); editing it would add a second unpinned blob for no
gain (its `dead=0` and integrity's post-fix `dead=0` agree, §4).

QUALITY rows:
- **Q05** (a fix ships its own regression arm): the arm is committed in the same patch and was run
  first against the pre-fix bytes — `FAIL pointer/rev/dead: got (3, 3) want (2, 3)`, §3.
- **Q18** (a new false red is harm; control arm from every input class): every pointer observation is
  byte-identical base→repair except `report_dead` (§4 receipt `pointer-observations-base-vs-repair.txt`),
  and the new predicate is strictly narrower-green on rev tokens: a rev token that previously resolved
  as a working-tree path could only have been a literal `HEAD:` directory name (never present), so the
  change cannot turn an alive pointer dead. Held-out classes exercised: rev-in-lane, rev-in-fleet,
  path-absent-in-revision, rev-that-does-not-resolve, plain/relative/absolute/tilde/bare, angle-bracket
  placeholders (unchanged, §4).
- **Q58** (a defect closes on a counter recomputing from the measured revision's bytes): both the arm
  (`citation_findings` + the real resolver over a fixture revision) and the corpus run recompute from
  committed bytes at the measured rev; nothing is asserted from prose or from the pre-revision state.

## 3. The arm fails on the pre-fix code (required proof, both outputs pasted)

Commit `d97ff63` = **arms only**, no fix (`prefix-arms.txt`):

```
$ python3 -B verifiers/verify_corpus_integrity.py --self-test
FAIL pointer/rev/dead: got (3, 3) want (2, 3)
self-test: 1 failure(s) over 165 assertions
rc=1
```

Commit `2e0a31d` = arms + fix (`postfix-selftest.txt`):

```
$ python3 -B verifiers/verify_corpus_integrity.py --self-test
self-test: 0 failure(s) over 165 assertions
rc=0
```

The arm is behavioural, not structural: it builds a one-commit fixture repo carrying
`.ufo/reports/round-53/kotoba.md` at `HEAD` (the fleet role) beside a non-repo citing directory (the
lane role) and asks `citation_findings` for three rev tokens — in-revision, absent-in-revision,
unresolvable-rev — asserting `(report_dead, report_total) == (2, 3)`. On pre-fix bytes all three are
dead (`(3, 3)`); the two negatives stay dead after the fix, so the arm pins both the repair and the
honesty it must not lose.

## 4. The repair's readings

Integrity at the repair rev `2e0a31decc9633219952cb1e139bc7c41f3ae61f` (`integrity-repair.txt`):

```
corpus.pointers report_dead=0/106 commit_total=45 unresolvable=0 nonhash=0 (shapes [relative=1,
absolute=44, tilde=1, bare=60], quoted-excluded=6, pointer-excluded=8; sites in --json)
  corpus.pointers.report_dead            zero     observed=0 PASS
5/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.index.unindexed,
corpus.pointers.report_total, corpus.pointers.commit_total
rc=1
```

The four remaining drifts are exactly the rows E03 owns (index rows + `verifiers/corpus-baseline.json`);
the dead-pointer row is green and `report_dead_detail` is empty. E03's expected values at this rev, as
read from the same receipt: `tracked_files 150→144` (needs the 6 unindexed lessons in the coverage map),
`unindexed 6→0`, `report_total 106→99` (my repair does **not** move it: 106 before and after),
`commit_total 45→43`. Note for E03: any world that deletes a pointer instead of resolving it reads
`report_total=105` (§7 B3), so the baseline value is a fingerprint of which repair landed.

Independent at the same rev (`independent-repair.json`):

```
points  candidates=116 checked=106 excluded=8 quoted=2 dead=0 shapes={'absolute': 44, 'tilde': 1,
'relative': 1, 'bare': 60}
```

Both gates now read `checked=106, dead=0` — they agree on the population and the verdict
(`pointer-observations-base-vs-repair.txt` shows every other pointer/commit observation identical
base→repair; the only deltas are `report_dead 1→0` and its detail).

Floors (`floors-repair.txt`, full 17-instrument walk):

```
PASS corpus_integrity observed=165 floor=164
FAIL checklist observed=1863 floor=1863 self_test_failures=2
```

`checklist` is the row another repair owns (the lane reads `1` failure: `LOG.md:2818:
'.ufo/reports/round-76/kotoba.md' does not resolve`). The clone reads `2` because that instrument's
self-test resolves `../.ufo/…` against the clone's parent; `checklist-child-attribution.txt` shows the
same `2 failure(s)` in the **unpatched** clone, so the extra failure is scratch-environment, not my
change.

## 5. Line budget (tip-battery `instrument-size`)

`run_guards` sums `git diff --numstat BASE rev -- <six battery scripts>` and fails above 40 added
(`check_tip_battery.py:296-320`; `BASE = 072048fa8e8a52c707d25f7079772fa317244eb7`). At the repair rev:

```
22 3 verifiers/check_assertion_floors.py     (r76 D4 bump, not ours)
17 0 verifiers/verify_corpus_integrity.py    (this repair, arms included)
```

39 added / 3 deleted → under the 40 cap with **one line of headroom**; the frozen guard itself reads it
that way at the repair rev (`tipbattery-repair.txt`):
`guarded paths 586, deleted 0; floors 15 rows; instruments added 39 / deleted 3 lines (cap 40)` and
`guard instrument-size PASS`. That headroom is the binding
constraint of this repair: the 5-line predicate + 1 comment line + an 11-line self-test arm is what
fits; a richer fixture (separate lane/fleet revisions, per-token dead detail) does not. It also means
the "bump the registry floor in step" the item asks for cannot also spend lines here (§7 B2).

## 6. Patch hygiene

```
$ git apply --check Kb79E04DeadPointer.patch   # clone at 2c56622
apply_check_rc=0
 verifiers/verify_corpus_integrity.py |   17 +++++++++++++++++
```

The patch is a plain diff from the plan-freeze commit (no `.ufo`, no data, no floors change) and does
not touch the frozen counter, `MANIFEST.json`, or any pinned instrument other than the one it repairs.

## 7. Blockers — measured, with the exact minimal remedy (no counter edits made)

**B1 — `instrument-pin` forbids the honest repair.** The tip battery pins each of the six scripts to a
fixed blob set inside the frozen counter itself (`check_tip_battery.py:118-139`, `:310-315`: any blob
not in the tuple fails). The repair's blob is not there (`pin-map.txt`):

```
integrity blob at plan commit 2c56622: e470eaaea5ef11c582b8353c9344ddf730c1a57a   (pinned)
integrity blob at repair rev 2e0a31d: 051b8c5f8676cba5c8d6047c8c9f7fcb56cd8f9f   (0 occurrences in
                                                                                 the frozen pin map)
```

`check_tip_battery.py` is frozen by C1's own predicate (sha256
`e33b17d74f5935a43b04272baf2d88d1d4cf4f879ee9cfa48bb25f89e744bc4a`, re-verified at the plan commit).
Measured at the repair rev (`tipbattery-repair.txt`, absolute `--repo`/`--fleet` form):

```
measured rev 2e0a31decc9633219952cb1e139bc7c41f3ae61f in a fleet-shaped sandbox; base 072048fa…
guarded paths 586, deleted 0; floors 15 rows; instruments added 39 / deleted 3 lines (cap 40); spotcheck base files 27
guard no-deletions PASS
guard floors PASS
guard instrument-size PASS
FAIL guard instrument-pin: verifiers/verify_corpus_integrity.py blob 051b8c5f8676cba5c8d6047c8c9f7fcb56cd8f9f at 2e0a31decc9633219952cb1e139bc7c41f3ae61f is not a pinned blob
guard spotcheck-identity PASS
fleet root /home/vgpnk/Projects/shokunin; guards 4 of 5; tip battery exit 0: 1 of 6
rc=1
```

Four of five guards hold; the one that fails is the pin, by name. So the repair cannot be measured as
`6 of 6` without editing the frozen counter's pin tuple: C1's own
kill rule ("a repair needs a guard to be edited") therefore fires on the one red that is *code-side*.
Every other base red is data-side (gate-registry rows absent from `SKILL.md` — `grep -c
check_desc_craft SKILL.md` → 0, same for `check_r75_routed_repairs`; the `LOG.md:2818` citation;
index rows + baseline), so this is the single blocker for the claim.

**B2 — the requested floors-registry bump is unsatisfiable in-round.** `check_assertion_floors.py`
cross-checks the registry against **two in-file tables** and refuses to run on disagreement, and that
guard is itself pinned. Registry-only bump, measured (`floors-registry-bump.txt`):

```
$ python3 -B verifiers/check_assertion_floors.py      # corpus_integrity floor 164 -> 165 in the registry only
FAIL registry floor drift: corpus_integrity registry=165 expected=164 row=164
rc=2
```

So the floor stays `164` and the new arm is above it (`observed=165`) — green, but the three added
assertions are **not floored**: dropping the arm later would still read `PASS` at 164. A real bump needs
`EXPECTED_INSTRUMENTS`, `INSTRUMENTS` and the registry moved together, i.e. a second pinned-instrument
blob change, which belongs to the same re-freeze as B1 if the L1 chooses that route.

**B3 — the declared control world W7 is not blocked by the guard my item names.** `spotcheck-identity`
compares only `corpus/lessons/*-verifier-spotcheck.md` **present at the battery base** (r73,
`072048fa`), and reports later additions as INFO (`check_tip_battery.py:321-335`). Measured:

```
base(r73) spotcheck files: 27
base has round-77 spotcheck: no            # git cat-file -e 072048fa:corpus/lessons/round-77-…
rev77 spotcheck blob at plan commit: 71968f6b2f48e875fb385e745c76c60cda7c936a
```

W7 world `31d00cde24bb15c7ed7e212f21c0844701bea4fc` (one table cell in that lesson rewritten to drop
`HEAD:`; gate bytes untouched), `integrity-w7.txt`:

```
corpus.pointers report_dead=0/105 …
5/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.index.unindexed,
corpus.pointers.report_total, corpus.pointers.commit_total
```

i.e. deleting the truthful citation repairs the row with **zero instrument change** and no guard
objects. [INFERENCE, and I did not take it] with E03's index/baseline rows and the other seats'
data-side rows (registry rows, `LOG.md` correction) this world reads `6 of 6`; every one of those rows
is data-side by the readings in §7 B1 and the base receipt. Per C1's own rule ("any world reaching
`6 of 6` is a counter or guard defect") W7 is therefore a **guard defect on the record**, not a repair
route: the plan expects `spotcheck-identity` to protect a file that postdates the guard's base. I did
not narrow or edit the lesson; the world exists only in scratch.

## 8. Residuals (named, not repaired)

1. **The two gates still classify the token differently.** Independent strips the rev prefix and reads
   the *path*; integrity (post-fix) reads the *revision*. They agree on this corpus (§4). Divergence
   case: a `HEAD:` form whose path exists in the fleet working tree but not in fleet `HEAD` — integrity
   dead, independent alive. Not repaired: `verify_corpus_independent.py` is pinned (B1) and the item
   requires its current verdicts to stand.
2. **`HEAD` is resolved at measurement time.** Like `commit_resolves`' live-object reading, a rotated
   fleet `HEAD` could flip this verdict later; the pre-fix gate was dead in every case, so this is not
   a regression, but the predicate is a presence check at a moving ref, not at a pinned commit.
3. **The line cap is the design ceiling for this gate.** 1 line of headroom (39/40) means the next
   repair to this instrument must either shrink an existing block or arrive with a re-frozen counter.

## 9. What the L1 should do, and what I did not do

- **If C1 continues:** one re-freeze commit that (a) adds blob
  `051b8c5f8676cba5c8d6047c8c9f7fcb56cd8f9f` to
  `INSTRUMENT_PINS["verifiers/verify_corpus_integrity.py"]`, (b) moves `corpus_integrity`'s floor
  164→165 in `EXPECTED_INSTRUMENTS`, `INSTRUMENTS` and `verifiers/floors-registry.json` together, and
  (c) re-declares C1's frozen counter sha; then land the patch and measure both battery forms. This is
  a counter edit — the L1's call, not a seat's.
- **Otherwise:** C1 honest-stops on B1, and the routed defects are B1 (a pin set with no re-pin path
  makes a code-side false red unreachable in-round) and B3 (`spotcheck-identity`'s base set leaves
  every post-r73 spot-check lesson editable, so its documented control W7 is unguarded).
- **Verification the L1 should run after integrating:** `python3 -B verifiers/verify_corpus_integrity.py
  --self-test` (0/165), `--json` (`report_dead 0`, `report_total 106`),
  `python3 -B verifiers/verify_corpus_independent.py --json` (`dead=0`),
  `python3 -B verifiers/check_assertion_floors.py` (`PASS corpus_integrity observed=165 floor=164`),
  and the tip battery in both `--repo .` and absolute forms (expect the `instrument-pin` line until the
  re-freeze lands).
- **Not done, deliberately:** no lane commit/push, no edit to the lesson, `verifiers/floors-registry.json`
  (measured that a registry-only bump reds the guard), `MANIFEST.json`, `SKILL.md`, `LOG.md`, any other
  seat's build directory, the frozen counter, or `.ufo/state/`. Lane writes: this report plus
  `.ufo/waves/round-79/build/Kb79E04DeadPointer/`.
- **Scratch hygiene:** my own defect, caught and repaired mid-run — a probe did `rm -rf .ufo` inside the
  repair clone, which deleted 25 *tracked* `.ufo/reports/*` files there; restored with
  `git checkout -- .ufo` (`git status --porcelain` empty afterwards), and the `check_assertion_floors`
  walk was re-run clean (`floors-repair.txt`). The first walk's `checklist` count was not used.

## 10. Evidence index

`.ufo/waves/round-79/build/Kb79E04DeadPointer/`: `Kb79E04DeadPointer.patch` (sha256
`d7169dd8…a5d78`), `apply-check.txt`, `pin-map.txt`, `tokenizers-base-vs-independent.txt`,
`prefix-arms.txt`, `postfix-selftest.txt`, `integrity-repair.txt`, `integrity-repair.json`,
`independent-repair.json`, `pointer-observations-base-vs-repair.txt`, `floors-repair.txt`,
`floors-registry-bump.txt`, `revision-vs-worktree.txt`, `checklist-child-attribution.txt`,
`integrity-w7.txt`, `tipbattery-repair.txt`.

VERDICT: The dead report pointer has one honest repair — `<rev>:<path>` resolved against the citing repository then the fleet (17 lines, arm fails 1/165 on pre-fix bytes and passes 0/165 after, corpus `report_dead` 1→0 with every other pointer observation unchanged, both gates then read `checked=106 dead=0`) — but it cannot be measured as `6 of 6` under the frozen counter: `instrument-pin` pins only `e470eaae`, so C1 needs a re-freeze that pins `051b8c5f` (and the 164→165 floor) or must honest-stop; and the declared control W7 is unguarded because `spotcheck-identity`'s base is the r73 tree, which does not contain the round-77 lesson.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79E04DeadPointer/Kb79E04DeadPointer.patch (sha256 d7169dd8f9db17a908f00c1e62a668d73c7ca96cca75626807fb81889f4a5d78), /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79E04DeadPointer/ (15 receipts), /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/w1/Kb79E04DeadPointer.md
