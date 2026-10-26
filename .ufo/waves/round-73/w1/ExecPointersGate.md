# kotoba — round 73, wave 1 — seat ExecPointersGate

**Verdict: delivered.** The mined-mistake fix `check_report_pointers.py` exists as a draft, its self-test passes
57 assertions, and it is shown able to fail on the r72 report at the r72 tip — exit 1 naming
`tip-check_tip_battery.txt` and `receipts/tip-check_substrate_repin_v2.txt` — while a corrected copy of the same
report reads `36 of 36` exit 0. The gate also reproduces **19 of 19** readings expected by the controls seat
(`ExecPointersControls`), after fixing the four pre-freeze defects that seat found (D1 vacuous `0 of 0`, D2 a
parenthetical hiding a broken pointer, D3 directory-only passes, D4 `path:line` false positive). One of those
fixes moves the counter's exit tail (`M == 0` or `B == 0` → exit 2), so **the L1 owes one addendum sentence
before freeze 2** (§ 8). No committed lane file was touched.

## 1. Deliverable

| item | value |
|---|---|
| path | `.ufo/waves/round-73/w1/build/ExecPointersGate/check_report_pointers.py` |
| bytes / lines | 40,352 B / 901 lines |
| sha256 | `2537a22733c45e58da387777ed9e632e03f0819a54761cf0875db23659ddddf6` |
| usage | `python3 -B check_report_pointers.py --report <path> --repo <lane> --rev <rev> [--round N] [--verbose]` |
| stdout line 1 (frozen) | `report pointers resolved N of M; unresolved U` |
| stdout line 2 | `pointer objects: blob B, directory D` |
| exit | 0 iff `U == 0` **and** `B > 0`; 1 on unresolved; 2 on unreadable report/rev, non-repo, no round
derivable, `M == 0`, or `B == 0` |
| runtime | 0.170 s wall on the r72 report at `072048f` (37 pointers, one `git ls-tree -r` + one
`git cat-file -t` per pointer) |
| network | none; committed bytes only (`git cat-file -t <rev>:<path>`) |

Self-test, run from the draft's own directory:

```
$ python3 -B check_report_pointers.py --self-test
self-test: 0 failure(s) over 57 assertions
```

The self-test builds one throwaway fixture repo per run (`git init` under a fresh `mktemp` dir, `rev-parse
--show-toplevel` asserted equal to that dir **before** the first commit, throwaway identity, tree deleted in a
`finally`). 57 assertions cover: green tally, red tally + each unresolved name + each nearest name, fenced-block
exclusion, command-span exclusion, placeholder exclusion, glob exclusion, receipts-relative resolution, bare-name
ladder (root / `verifiers/` / `scripts/` / round wave / `corpus/` / non-fixture / round receipts), a buried
fixture copy failing to launder a bare name, a directory-only report refused, a path-first multi-word span still
counted, cross-round repair suggestion, `:line` and `:line-line` locator stripping, occurrence counting,
`--round` naming the wave dir, empty report refused, and every exit-2 arm (missing report, unreadable rev,
non-repo dir, no `--report`, non-integer `--round`, no traceback on stderr).

## 2. RED-BEFORE — the gate must fail on the defect it exists for

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
$ python3 -B .ufo/waves/round-73/w1/build/ExecPointersGate/check_report_pointers.py \
    --report /home/vgpnk/Projects/shokunin/.ufo/reports/round-72/kotoba.md \
    --repo . --rev 072048fa8e8a52c707d25f7079772fa317244eb7 --round 72
report pointers resolved 34 of 37; unresolved 3
pointer objects: blob 33, directory 1
unresolved pointer: S2xx.sha256 (report line 45) -> .ufo/waves/round-72/receipts/S2xx.sha256 (nearest: none)
unresolved pointer: tip-check_tip_battery.txt (report line 70) -> .ufo/waves/round-72/receipts/tip-check_tip_battery.txt (nearest: tip-tip_battery.txt)
unresolved pointer: receipts/tip-check_substrate_repin_v2.txt (report line 103) -> .ufo/waves/round-72/receipts/tip-check_substrate_repin_v2.txt (nearest: tip-substrate_repin_v2.txt)
EXIT=1
```

Both closure tokens are named, each with the file the author meant. The quoted report lines (`cat -A`, trailing
`$` is the newline):

```
$ sed -n '70p;103p' /home/vgpnk/Projects/shokunin/.ufo/reports/round-72/kotoba.md | cat -A
  (`tip-check_tip_battery.txt`, `tip-tip_battery-run2.txt`): the counter's sandbox reads `check_assertion_floors.py` and$
  (`receipts/tip-check_substrate_repin_v2.txt`).$
```

and the tree at that rev holds only the corrected names:

```
$ git ls-tree -r --name-only 072048fa8e8a52c707d25f7079772fa317244eb7 -- .ufo/waves/round-72/receipts \
    | grep -E 'tip-'
.ufo/waves/round-72/receipts/tip-author_rules.txt
.ufo/waves/round-72/receipts/tip-noharm.txt
.ufo/waves/round-72/receipts/tip-substrate_repin_v2.txt
.ufo/waves/round-72/receipts/tip-tip_battery-run2.txt
.ufo/waves/round-72/receipts/tip-tip_battery.txt
```

The third unresolved token is **not** a counter defect and I did not hide it: `S2xx.sha256` is the r72 report's own
redaction mask for the `S2<xx>.sha256` snapshot manifests (line 45: "their sha256 stay in the `S2xx.sha256`
manifests"), a family written in the shape of a file name. The gate's universe is fixed before data (§ 7, R4/R5
permit a glob or a `<placeholder>` but not an `xx` mask swallowed at run time), so the mask reads unresolved. The
r73 report must therefore write families as a glob (`` `S2*.sha256` ``) or as plain prose — the corrected-copy
control below does exactly that.

## 3. Positive control — the gate can also pass, and its count is not stuck red

A scratch copy of the same r72 report with three textual fixes (the two drift tokens corrected to the names in the
tree, the mask written as a glob) — the fetched report itself was never modified:

```
$ sed -e 's/`tip-check_tip_battery\.txt`/`tip-tip_battery.txt`/' \
      -e 's|`receipts/tip-check_substrate_repin_v2\.txt`|`receipts/tip-substrate_repin_v2.txt`|' \
      -e 's/`S2xx\.sha256`/`S2*.sha256`/' \
      /home/vgpnk/Projects/shokunin/.ufo/reports/round-72/kotoba.md > $D/fixed.md
$ python3 -B check_report_pointers.py --report $D/fixed.md --repo . \
    --rev 072048fa8e8a52c707d25f7079772fa317244eb7 --round 72
report pointers resolved 36 of 36; unresolved 0
pointer objects: blob 35, directory 1
EXIT=0
```

`36` not `37`: the corrected mask is a glob and, by R4, a glob is not a pointer. That is the gate's universe
shrinking by an explicit rule, not by a silent reread of the report.

## 4. Calibration against the controls seat (19 of 19 readings match)

I rebuilt their battery read-only (their `run_worlds.py` writes into their directory, so I keep my own replay as
`build/ExecPointersGate/run_controls_worlds.py`, which writes nothing and takes `--round` per report, and run the
`untracked-worktree` sandbox by hand):

```
$ python3 -B run_controls_worlds.py
absolute-path          report.md                  OK        exp 0 1 of 1  got 0 1 of 1
bare-cross-round       report.md                  OK        exp 0 1 of 1  got 0 1 of 1
dir-legit              report.md                  OK        exp 0 2 of 2  got 0 2 of 2
dir-only               report.md                  OK        exp 2 5 of 5  got 2 5 of 5
dir-only               report-mixed.md            OK        exp 1 5 of 6  got 1 5 of 6
fence-hides-prose      report.md                  OK        exp 1 0 of 1  got 1 0 of 1
fence-hides-prose      report-fence-only.md       OK        exp 2 0 of 0  got 2 0 of 0
fence-hides-prose      report-code-span.md        OK        exp 0 1 of 1  got 0 1 of 1
later-rev-only         report.md                  OK        exp 1 1 of 4  got 1 1 of 4
line-suffix            report.md                  OK        exp 0 2 of 2  got 0 2 of 2
multiword-span         report-broken.md           OK        exp 1 0 of 1  got 1 0 of 1
multiword-span         report-valid-section.md    OK        exp 0 1 of 1  got 0 1 of 1
no-pointers            report.md                  OK        exp 2 0 of 0  got 2 0 of 0
typo-near              report.md                  OK        exp 1 1 of 3  got 1 1 of 3
typo-near              report-wrong-existing.md   OK        exp 0 1 of 1  got 0 1 of 1
untracked-worktree     *                          SKIP      sandbox recipe (untracked file in a clone)
wrong-round-receipts   report.md                  OK        exp 1 2 of 3  got 1 2 of 3
wrong-round-receipts   report-correct.md          OK        exp 0 3 of 3  got 0 3 of 3
controls worlds: 0 mismatch(es)
EXIT=0
```

The nineteenth reading, the untracked-file world, in a `git clone --shared` of the lane checked out at `072048f`
with the drifted receipt recreated **untracked**:

```
$ git clone --shared -q --no-checkout …/kotoba-shokunin $D/lane && git -C $D/lane checkout -q 072048f
$ echo untracked > $D/lane/.ufo/waves/round-72/receipts/tip-check_tip_battery.txt
$ git -C $D/lane status --porcelain
?? .ufo/waves/round-72/receipts/tip-check_tip_battery.txt
$ python3 -B check_report_pointers.py --report …/untracked-worktree/report.md --repo $D/lane \
    --rev 072048fa8e8a52c707d25f7079772fa317244eb7 --round 72
report pointers resolved 2 of 4; unresolved 2
pointer objects: blob 2, directory 0
unresolved pointer: receipts/tip-check_tip_battery.txt (report line 3) -> … (nearest: tip-tip_battery.txt)
unresolved pointer: tip-check_tip_battery.txt (report line 6) -> … (nearest: tip-tip_battery.txt)
EXIT=1
```

The gate reads committed bytes only: an untracked file on disk does not resolve, so the exact r72 defect cannot
pass through the work tree. My first pass on their battery read `typo-near/report-wrong-existing.md` as a
mismatch; that was **my runner** passing the world's round instead of the report's own `"round": 72`, not the
gate — re-run above.

## 5. The four pre-freeze defects the controls seat found, and what changed

Their README reports its readings against `sha256:4fba056…` (31,500 B). All four are fixed in `2d1d7932…`:

| # | defect (their world) | fix in the draft | self-test arm |
|---|---|---|---|
| D1 | `0 of 0` exits 0, so a report that drops its backticks reads green (`no-pointers`, `fence-hides-prose/report-fence-only.md`) | `M == 0` → exit 2, message `cannot evaluate: the report holds no backticked pointer token, so nothing was resolved`; the frozen count line is unchanged | `empty: zero pointers is exit 2, never a vacuous pass` |
| D2 | a span whose first word contains `/` was called a command, so one parenthetical word hid a broken pointer (`multiword-span`) | `is_command_span` decides on a command head or a `.py`/`.sh` word plus shell metacharacters; a path coming first no longer exempts the span | `multiword: a path-first span is not a command span`, `multiword: the broken pointer is named` |
| D3 | five directory tokens read `5 of 5` and passed (`dir-only`) | resolution returns the object kind (`git cat-file -t`); the tally line `pointer objects: blob B, directory D` is always printed; `B == 0` with `M > 0` → exit 2, message `cannot evaluate: every pointer names a directory` | `dir-only: three directories resolve and the gate refuses to pass`, `dir+blob: a directory with a blob exits 0` |
| D4 | `corpus/knowledge/frontmatter-trigger-surface.md:116-120` read unresolved — a false positive that would block this round's own report | trailing `:\d+(-\d+)?$` stripped before resolution (R6); the counter resolves the file and never claims the line | `locator: a bare locator resolves at the lane root`, `locator: a ranged locator resolves the file`, `locator: a missing file still fails, named without the locator` |

I also extended their cross-round observation: an unresolved receipts token now prints a same-basename receipt
from another round when one exists, preferring the **nearest** round, so their residual (2) closes:

```
$ python3 -B check_report_pointers.py --report .ufo/waves/round-73/w1/build/ExecPointersControls/wrong-round-receipts/report.md \
    --repo . --rev ac8fc59523c2e41dbd46e0c2787e94949aa3cec0 --round 73
report pointers resolved 2 of 3; unresolved 1
pointer objects: blob 2, directory 0
unresolved pointer: receipts/c2-base.txt (report line 4) -> .ufo/waves/round-73/receipts/c2-base.txt (nearest: base-sweeps.txt, other round: .ufo/waves/round-72/receipts/c2-base.txt)
```

`c2-base.txt` also exists in round 71's receipts; the suggestion picks round 72, the neighbour of the report's
round. The self-test asserts both the suggestion and the round preference (fixture rounds 7 and 8 against a
round-9 report), and the 18-world loop above was re-run at the final sha with no mismatch.

The controls seat re-ran the whole battery twice while the draft moved: at `2d1d7932…` (39,836 B) and again at the
final `2537a227…` (40,352 B). Its second result, in
`.ufo/waves/round-73/w1/build/ExecPointersControls/readings/` (`summary.tsv` carries the gate sha; `GATE.txt`
pins `sha256 2537a22… bytes 40352`): **19 of 19 readings match, 0 diff, self-test 0 failures over 57 assertions,
r72 red-before `34 of 37` exit 1**. Its four defect findings are closed (F1 vacuous `0 of 0`, F2 multi-word span,
F3 directory-only, F4 `path:line`), and F8 (cross-round nearest name) closed at this sha. The only item it leaves
open is the same one I flag in § 8.3: the freeze addendum must carry the `M == 0` / `B == 0` tail beside the
frozen sentence. Their F7 also re-confirmed two limitations recorded in § 7: an existing-but-wrong artifact and a
bare cross-round name both pass, and `receipts/../../SKILL.md` cannot resolve (`git` rejects `..`).

## 6. Exclusion rules — derived here, not inherited

`ScoutReceiptPointers.md` did **not** exist under `.ufo/waves/round-73/w1/` at the time of writing (listing on
2026-10-25 shows 32 seat reports, none of them that seat), so the exclusion rules are my own derivation, pinned as
R1–R8 in the module docstring:

- **R1** only inline code spans (two backticks, one physical line);
- **R2** fenced blocks skipped whole (``` and ~~~ fences, fence state tracked per line);
- **R3** command code spans skipped (shell metacharacters, or a first word that is a command head / ends in
  `.py`/`.sh` — a path that merely comes first does not qualify, per D2);
- **R4** globs skipped (`*?[{`, literal `...`); **R5** placeholders skipped (`<`, `>`);
- **R6** absolute/home tokens skipped, `./` dropped, surrounding quotes and trailing `,.;:()` dropped, trailing
  `:line[-line]` locator dropped (not verified);
- **R7** prefix tokens (`.ufo/waves/`, `receipts/`, `corpus/`, `verifiers/`, `plans/`), where `receipts/…` maps to
  `.ufo/waves/round-<N>/receipts/…` with `--round N` or `round-(\d+)` in the report path;
- **R8** bare tokens (`BARE_EXTENSIONS`) resolved by a fixed ladder: lane root → `verifiers/` → `scripts/` → the
  report's round wave dir → `corpus/` → any match outside a fixture area (`build/`, `controls/`, `evidence/`,
  `work/`, `base-outputs/`, `snapshots/`, `fixtures/`) → the round receipts dir.

If that seat's report lands with different rules, the L1 reconciles; nothing here depends on its absence.

## 7. What this gate does not do (stated, not implied away)

- Nothing outside an inline code span is checked, so a prose path is invisible; the counter constrains **cited
  pointers**, never citation completeness.
- A broken pointer written inside a fence (R2), inside a command line (R3), as a glob (R4), as a `<placeholder>`
  (R5) or as an absolute path (R6) passes. `fence-hides-prose/report-fence-only.md` now exits 2 rather than 0 only
  because no pointer survives at all (D1); a report with one good pointer and one broken pointer in a fence still
  passes.
- A bare name loses round attribution (R8): an existing-but-wrong receipt from the same wave dir passes
  (`typo-near/report-wrong-existing.md`, documented blind spot); semantic mis-citation is the reviewer/critic's
  class, not this counter's.
- An existing artifact of another round can satisfy a bare name whose own round lacks it — the ladder prefers the
  report's round, but does not refuse a later match.
- Line numbers are stripped, never checked.
- A file present in the work tree but not at `--rev` never resolves (verified in the clone above).
- The `xx` redaction mask (`S2xx.sha256`) is not special-cased; r73 must write families as globs or prose.

## 8. Integration notes for the L1

1. **Landing path** `verifiers/check_report_pointers.py`; the draft has no path dependency — run from `/tmp` with
   absolute `--report`/`--repo` it prints the same `34 of 37` / `blob 33, directory 1` on the r72 report as it does
   from the lane root — so no edit is needed on landing.
2. **Registry row** (shape copied from `SKILL.md:449`, eight protocol fields):
   ```
   | `verifiers/check_report_pointers.py` | gate | `python3 -B verifiers/check_report_pointers.py --report <path> --repo . --rev <rev> --round <N>` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | none | none | kotoba |
   ```
   The self-test flag is an exact `add_argument` handler; the entry command contains `verifiers/…`; the verdict
   map declares `0=clean` and `1=failed`.
3. **Addendum sentence owed before freeze 2** (the only change to the plan's predicate, and it is a strengthening):
   > the counter is exit 2, not exit 0, when the report holds no backticked pointer token (`M == 0`) or when every
   > pointer names a directory (`B == 0`); the printed count line is unchanged, and `0 of 0` is the
   > could-not-evaluate class.
   Without it the `no-pointers` and `dir-only` shortcut worlds score a pass and the claim's own kill rule fires.
4. **Round-73 report admissibility**: cite at least one backticked blob pointer (it will), and never reuse the
   `S2xx.sha256` mask shape — write `` `S2*.sha256` `` or plain `S2xx.sha256`.
5. The plan's Frontier step says the counter is shown able to fail on the r72 report at the r72 tip "before it is
   run on the r73 report at the r73 tip (exit 0)"; § 2 and § 3 are that evidence pair.

## 9. Files written, scratch, tooling

- Deliverable: `.ufo/waves/round-73/w1/build/ExecPointersGate/check_report_pointers.py` (new).
- Evidence tool: `.ufo/waves/round-73/w1/build/ExecPointersGate/run_controls_worlds.py` (new, read-only replay of
  the controls seat's 18 pinned readings; writes nothing).
- Scratch: `/tmp/k73w1-ExecPointersGate.rRDi` (report copies, the world loop) and
  `/tmp/k73w1-ExecPointersGate-clone.yr8Z` (the untracked-file clone) — both deleted before return.
- No committed lane file was modified (no `SKILL.md`, `corpus/`, `verifiers/`, `plans/`, `LOG.md`, `SCORECARD.md`,
  `PROVINCE.md`, `SHONEN.md`, `README.md`); no lane git write; no jj call; the fleet repo, sibling lanes and
  `shokuknow` untouched; no fixture commit outside a `mktemp` dir.
- Tool installs: none (python3 and git from the host; `pacman` untouched).
- Peer coordination: three one-line messages to `ExecPointersControls` (unfinalised warning, stable candidate sha,
  then this final sha with the nearest-round fix) and their confirmation of the 19-of-19 battery.

## 10. Risks and blockers

- **R1 (needs the L1):** the predicate tail in § 8.3 must land as an addendum; it is the only deviation from the
  plan's literal "exit 0 iff U == 0", and it exists because a vacuous pass would be a shortcut world.
- **R2 (report craft):** a family mask written as a file name reads unresolved by rule; the r73 report must not use
  the `S2xx.sha256` shape.
- **R3 (staging):** the gate is built against the assignment's channel list, which includes `plans/` and bare
  receipt names; the plan's Frontier sentence lists four prefixes. The extra channels only add pointers (strictly
  more failing surface), never remove one.
- **R4 (coverage ceiling):** fenced and command-span pointers stay unchecked by design; a critic should not read
  `unresolved 0` as "every path in the report exists".
