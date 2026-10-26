# RevengerBatteryDiag — M127, reconstructed from artifacts (round 73, wave 1)

Seat: independent reverse-engineering of M127. Read-only on the lane; evidence in
`.ufo/waves/round-73/w1/build/RevengerBatteryDiag/`. No peer report was read before this
diagnosis was finished (ScoutBatteryDiag / ExecBatteryFix were not opened).

## Verdict

**CONFIRMED** — the cause is a *relative `--repo`* reaching `Path.parent`, i.e. two source
lines, not a timeout, not a lock, not the `--shared` clone, not env inheritance:

- `verifiers/check_tip_battery.py:609` `repo = Path(args.repo)` — never `.resolve()`d;
- `:610` `fleet = Path(args.fleet) if args.fleet else repo.parent`.

With `--repo .`, `Path(".").parent == Path(".")` (observed: `Path(".").parent = '.'`), so
`fleet` is the **process CWD** — the lane when invoked from the lane root, as the plan's and
the r72 ruler's command does. `build_sandbox` then symlinks *the lane's* entries into the
temporary parent instead of the *fleet root's* entries, and every `../`-cited token in the
measured tree resolves against the wrong tree. Two gates read `../`:

- `verifiers/verify_skill_checklist.py:1529-1550` (`citation_resolve`: leading `..` hops resolve
  against `repo`'s ancestors, bounded at 3) via `trigger.citation_resolves` and
  `governance.citation_resolves`;
- the same checklist gate's *self-test*, which two of its arms run against the live repo
  (`verify_skill_checklist.py:2521` `live_repo = Path(__file__).resolve().parent.parent`), and
  which `check_assertion_floors.py:217/622` reruns as a child (`checklist` row, floor 1863).

Refinement of the L1 statement (which is otherwise correct): the damaged value is not literally
"the lane", it is the **CWD**; it *is* the lane only because the documented invocation is
`cd <lane> && … --repo .`. The counter's own default (`--repo` defaulting to
`str(_default_lane())`, an absolute path) is **already correct** — M127 is produced by the
explicit relative argument the plan's base table and the r72 receipts use.

## Hypotheses, ranked by evidence, and how each was discriminated

Controlled variable in every test below: the two sandboxes are `git clone --shared` of the lane
at the **same** rev `072048fa8e8a52c707d25f7079772fa317244eb7` (`git rev-parse HEAD` printed the
same value in both); the only difference is *which entries are symlinked beside the clone* —
**laneshape** (siblings = the lane's entries: exactly what `fleet = Path(".")` produces) vs
**fleetshape** (siblings = the fleet root's entries: what `repo.parent` produces when `repo` is
absolute).

| # | hypothesis | status | discriminating observation |
|---|---|---|---|
| H1 | fleet root derived from an unresolved relative `--repo` (`:609-610`) → `../` citations resolve against the lane's own tree | **confirmed** | same rev, siblings swapped: checklist gate `1.43 s exit 1` → `1.43 s exit 0`; counter `2 of 6` → `4 of 6` after one line (below) |
| H2 | nested timeout under load (`check_assertion_floors.py` self-test cap) | **refuted** | constant is `SELF_TEST_TIMEOUT_S = 120` (`:184`) scaled by 1-min loadavg, clamped ×15 (`:188`, `child_timeout_s` `:191-202`); load during the runs was 17.9–24.9, i.e. cap 2148–2988 s. The failing child (`verify_skill_checklist.py --self-test`) ran 4.4 s, and the failure line names `self_test_failures=2`, never `timed out` |
| H3 | gates contend for a lock / fixed temp path | **refuted** | `run_battery` (`:327-346`) is a serial `for` loop — no two gates ever run at once; no `flock`/`fcntl` in any of the six gates; the counter's own dir is `tempfile.TemporaryDirectory(prefix="k72-tip-")` per run |
| H4 | `--shared` clone / checkout yields a different tree | **refuted** | both sandboxes `HEAD = 072048f…`; the green and red checklist runs both took 1.43 s (no I/O difference) |
| H5 | subprocess env differs from the hand run | **refuted** | `subprocess.run` at `:338` passes no `env=` (inherits); the red/green split reproduces inside one interpreter with one inherited env |
| H6 | the two corpus reds are also shape artifacts | **refuted** | `verify_corpus_integrity.py` and `verify_corpus_independent.py` read the same exits (1, 1) in **both** shapes, same walls (0.34–0.90 s); they name their own cause: `corpus/index.tracked_files: observed=136 expected=135`, `corpus.index.unindexed: observed=1`, `corpus.pointers.report_total: observed=95 expected=93`, `corpus.pointers.commit_unresolvable: observed=3`; independent's list starts `! corpus/lessons/round-72-verifier-spotcheck.md` (index = `corpus/README.md`, `verify_corpus_integrity.py:123`) |

## The failing output, both shapes, same rev

```
$ cd /tmp/k73w1-RevengerBatteryDiag.drAW/laneshape/kotoba-shokunin && python3 -B verifiers/verify_skill_checklist.py
FAIL trigger.citation_resolves: evaluated 187 — line 558: '../.ufo/reports/round-7/kotoba.md' does not resolve from /tmp/k73w1-RevengerBatteryDiag.drAW/laneshape/kotoba-shokunin
FAIL governance.citation_resolves: evaluated 1283 — correction LOG.md:2619 … '..' tokens … (+27 more)
exit 1   wall 1.43s

$ cd /tmp/k73w1-RevengerBatteryDiag.drAW/fleetshape/kotoba-shokunin && python3 -B verifiers/verify_skill_checklist.py
(no FAIL lines)  exit 0   wall 1.43s
```

Self-test (the child the floors gate runs):

```
laneshape   exit 1  wall 4.4s   2 failure(s) over 1863 assertions
fleetshape  exit 0  wall 4.7s   0 failure(s) over 1863 assertions
```

The two failing arms name the tree, not the rev:
`self-test FAIL: governance: live round-65 corrections land, errata-excused: got ('FAIL', 1283, "… corrected token '../.ufo/reports/round-60/kotoba.md' does not resolve …")` and
`self-test FAIL: governance: LOG.md:2678 erratum is load-bearing: …`.

Floors gate (the 78.6–128.1 s gate):

```
fleetshape  exit 0  wall 46.5s   … PASS scoped_rules_v32 observed=240 floor=240
laneshape   exit 1  wall 54.0s   FAIL checklist observed=1863 floor=1863 self_test_failures=2
```

The 46.5 s vs 54.0 s spread is load, and it is *below* both caps by a wide margin: the nested cap
scales **up** with load (120 s × loadavg, clamp 15 → 1800 s), so a loaded host cannot trip it;
the exposure the code actually has is the inverse — on an idle host (`load ≤ 1`) the cap is
120 s while the floors docstring records a child measured at 185–222 s in round 55. The outer
cap is `GATE_TIMEOUT_S = 280` (`:104`), and the largest floors wall observed anywhere in the
receipts is 128.1 s.

## Confirmed cause → the one-line delta, red-before / green-after at a fixed rev

Delta (my instrumented copy `.ufo/waves/round-73/w1/build/RevengerBatteryDiag/check_tip_battery_resolve.py`,
byte-identical to `verifiers/check_tip_battery.py` except line 609):

```
-    repo = Path(args.repo)
+    repo = Path(args.repo).resolve()
```

Red before / green after, same rev, same command line, cwd = lane:

```
A  python3 -B verifiers/check_tip_battery.py --rev 072048f… --repo .
   → gate check_assertion_floors.py exit 1 wall 83.4s; verify_skill_checklist.py exit 1 wall 2.5s
     gate verify_corpus_integrity.py exit 1; verify_corpus_independent.py exit 1
     tip battery exit 0: 2 of 6        exit=1   wall 89.1s

B  python3 -B …/check_tip_battery_resolve.py --rev 072048f… --repo .       (only delta: .resolve())
   → gate check_assertion_floors.py exit 0 wall 84.1s; verify_skill_checklist.py exit 0 wall 2.4s
     gate verify_corpus_integrity.py exit 1; verify_corpus_independent.py exit 1
     tip battery exit 0: 4 of 6        exit=1   wall 90.7s

C  python3 -B verifiers/check_tip_battery.py --rev 072048f…                 (exactly the C3 frozen predicate)
   → same per-gate exits as B; tip battery exit 0: 4 of 6   exit=1   wall 85.7s
```

The delta moves exactly the two M127 gates and nothing else; the remaining `N = 4` is the genuine
unindexed round-72 spot-check. Guard lines are byte-identical in A and C (`guarded paths 568,
deleted 0; floors 15 rows; instruments added 76 / deleted 24 lines (cap 40); spotcheck base files
26`), so the guards are shape-independent — only the gates' `../` reads were not.

Same mechanism at the r72 tip (`008411cff20e1488da31b744dc2c67d5baca3fcb`), which is where the
`4 of 6` receipt came from: laneshape checklist `exit 1` (line 558 token), fleetshape `exit 0`.
The token is unchanged between the two revs: `git show 008411cf:SKILL.md | sed -n 558p` prints
the same `../.ufo/reports/round-7/kotoba.md` line as `git show 072048f:SKILL.md | sed -n 558p`.

## Attacks on the frozen plan and on C3's own artifacts (each with the command that shows it)

**A1 — C3's do-nothing figure is taken with a command that is not C3's frozen predicate.**
The predicate (plan §C3) is `python3 -B verifiers/check_tip_battery.py --rev <rev>`; run C above is
exactly that and reads **`4 of 6`**, not `2 of 6`. The `2 of 6` in the base table and in
`receipts/c3-base-battery-counter.txt` is the `--repo .` variant (run A). Both exit 1, so the
control still fails, but the number, the per-gate attribution ("floors exit 1 (128 s), checklist
exit 1 (4.6 s)") and any "red before" receipt must be restated as `4 of 6` under the predicate
before C3 data (Q28 window is still open: no seat has scored C3 yet).

**A2 — C3 cannot reach `N == 6` without two repairs no seat item owns.** After the M127 fix the
base reads 4 of 6, the two reds being `corpus.index.tracked_files 136/135`,
`corpus.index.unindexed 1/0`, `corpus.pointers.report_total 95/93`,
`corpus.pointers.commit_unresolvable 3/0` (integrity) and the unindexed
`corpus/lessons/round-72-verifier-spotcheck.md` (independent, index `corpus/README.md`). The plan's
inherited-defect list has no item for indexing the r72 spot-check; the plan records the red but
routes no repair, so C3's frozen `N == 6` is unreachable as scoped.

**A3 — the counter could not have shown its own cause.** `run_battery` (`:338-346`) captures
stdout+stderr and keeps only `returncode`; `_tail` (`:152-156`) is used for `EnvError` only. A red
gate prints `exit 1` and nothing else, which is why M127 survived a round as "floors is slow".
Prescription for the delta: also print the first `FAIL` line of each non-zero gate (one line
changes the diagnosis from a guess to a quote).

**A4 — the counter's 42-assertion self-test is blind to this class.** Every arm drives `main()`
through `_drive` (`:431-443`) with an absolute `--repo` (`:433` `argv = ["--repo", str(lane), …]`)
and an explicit `--fleet` — no arm ever passes a relative repo. Observed: `--self-test` reads
`self-test: 0 failure(s) over 42 assertions`, exit 0, on **both** the original and the patched copy
(2.1 s each). The checklist gate solved the same problem earlier and guards it with its own arm
(`verify_skill_checklist.py:2545-2562`, "relative --repo: bounded hop resolves from absolute repo
root"); the counter needs the analogue, otherwise the one-line fix is not shown able to fail.

**A5 — with `--repo .` the sandbox leaks the live working tree, not just the wrong root.**
`readlink -f` on the laneshape siblings: `.ufo -> /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo`,
`corpus -> …/kotoba-shokunin/corpus`, `verifiers -> …/kotoba-shokunin/verifiers`,
`SKILL.md -> …/kotoba-shokunin/SKILL.md`. So any `../` read resolves against uncommitted local
state, and the two `.ufo` trees are not the same tree at all: the fleet root holds
`round-1 … round-108+`, the lane's own `.ufo/reports/` holds only `round-20 … round-45` — the
round-7 / round-9 / round-60 tokens cannot resolve there, which is exactly the observed failure
list. (The counter's docstring claim "guarded paths … committed bytes only" holds for the guards;
the gates' `../` reads are not covered by it.) This is the reason the receipt is *stable* rather
than flaky: the wrong tree is deterministic.

## Reproduction recipe (fleet-root gate runs need the `../` shape — never a bare `/tmp` clone)

```bash
S=$(mktemp -d /tmp/k73w1-RevengerBatteryDiag.XXXX)
for shape in laneshape fleetshape; do
  mkdir -p "$S/$shape"
  git clone --shared -q --no-checkout /home/vgpnk/Projects/shokunin/kotoba-shokunin "$S/$shape/kotoba-shokunin"
  src=/home/vgpnk/Projects/shokunin/kotoba-shokunin; [ "$shape" = fleetshape ] && src=/home/vgpnk/Projects/shokunin
  for e in "$src"/*  "$src"/.[!.]*; do n=$(basename "$e"); [ "$n" = kotoba-shokunin ] || ln -s "$e" "$S/$shape/$n"; done
  git -C "$S/$shape/kotoba-shokunin" checkout -q 072048fa8e8a52c707d25f7079772fa317244eb7
done
# then, per shape: python3 -B verifiers/verify_skill_checklist.py   and   python3 -B verifiers/check_assertion_floors.py
```

## Artifacts and hygiene

- `.ufo/waves/round-73/w1/build/RevengerBatteryDiag/check_tip_battery_resolve.py` — the one-line delta copy.
- `…/counter-repo-dot-orig.txt` (2 of 6), `…/counter-repo-dot-patched.txt` (4 of 6),
  `…/counter-frozen-predicate-norepo.txt` (4 of 6) — full outputs with exit and wall.
- Scratch `/tmp/k73w1-RevengerBatteryDiag.drAW` deleted before return; no committed lane file was
  modified; all git work happened inside `/tmp` clones (verified `rev-parse HEAD` per clone).
- No tool installed or upgraded (nothing needed); no pacman transaction was run.

## Confidence

High on the cause and the delta: same-rev, one-variable sandbox experiment with identical wall
times (1.43 s / 1.43 s), the counter's own red→green flip on a one-line change, and the same
mechanism reproduced at two revs. High on the timing refutation (constant + load arithmetic +
the failure string). Medium-high on A2 (I read the plan's item list and the corpus gate output;
whether an unwritten seat item exists is the L1's call). `[INFERENCE]`: that the L1 intends the
`.resolve()` delta — the receipts show the effect, not the intended patch text.
