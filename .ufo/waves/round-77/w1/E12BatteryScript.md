# E12BatteryScript — round 77, wave w1 (no-harm battery runner)

Seat: executor (`E12BatteryScript`), kotoba lane. Lane HEAD at run time:
`6523aced1ee0ebe07dca996213bdc645a6acbd1e` (round-77 freeze). No lane file outside
`.ufo/waves/round-77/{build,w1}/` was written; every git use was read-only
(`rev-parse`, `cat-file -e`, `clone --shared`, `checkout` inside the scratch clone only).

## 1. Deliverable: the runner

`.ufo/waves/round-77/build/E12BatteryScript.battery.sh`
sha256 `40b37324156a7e5a1cdbe5bdbebb480d8ec01ae9a211687e9dd27404d2bb2972`
(the same value is recorded in both receipts as `runner sha256:`).

```
E12BatteryScript.battery.sh --rev <rev> --receipt <path>
    [--repo <lane>] [--census-root <dir>] [--census-lane <name>]
    [--census-script <path>] [--scratch-parent <dir>] [--timeout <secs>]
```

What it does, in order:

1. resolves `<rev>` to a commit in the lane (`git -C <lane> rev-parse --verify`);
2. builds a scratch **fleet-shaped** sandbox under
   `/fast/scratch/hyaku/kotoba-r77/E12BatteryScript/run.XXXXXX` (trap-removed, also on
   INT/TERM): `fleet/kotoba-shokunin` is a `git clone --shared --no-checkout` of the
   lane, and every other entry of the fleet root is a read-only symlink beside it;
3. checks `<rev>` out **in the clone only** (`checkout -f --detach`), asserts
   `git rev-parse --show-toplevel` equals the clone and `HEAD` equals the resolved SHA,
   and sets `user.name`/`user.email` for the clone before anything could commit;
4. runs all 13 battery items from the clone root, printing each command and reading
   **that command's own `$?` on the next line** (`exit=N`);
5. writes the transcript to `<receipt>`; **line 1 is the resolved SHA**;
6. exit 0 only when every item is green, 1 when any is red, 2 for a usage/environment
   failure.

Design points that are deliberate, not incidental:

- **Fleet shape is a measurement requirement.** `verify_skill_checklist` rejects
  `name != directory`, and the lane's `../.ufo/...` citations need the fleet beside the
  lane (round-73 M127). A clone named `clone` outside a fleet reads red on bytes that
  are not red in the lane — see §5, where I measured exactly that with my own first
  version.
- **No pipeline on the status path.** Each gate is a simple command inside `run()`,
  redirected to a file; `rc=$?` is read on the next line. The r76 `| tail` defect
  (`.ufo/waves/round-76/receipts/pipeline-exit-demo.txt`) cannot recur; the control is
  re-run in `.ufo/waves/round-77/build/E12BatteryScript.exit-verify.txt`.
- **Absent instrument ≠ red gate.** Before each Python gate the runner asks
  `git cat-file -e <rev>:verifiers/<gate>.py`; when absent it records `exit=2` with the
  reason and does **not** run the command, so a missing script never reads as a gate
  verdict (check_tip_battery's discipline).
- **Per-gate watchdog** `timeout --signal=TERM --kill-after=15 <secs>` (default 900);
  a watchdog kill is recorded as `exit=124` and is red.
- **Both census forms**, because they measure different trees: the plan's form
  (`validate --root /home/vgpnk/Projects/shokunin kotoba`) parses the **fleet lane
  path**, not the clone; `validate --file <clone>/corpus/SOURCES.md` measures the
  revision under test. Both exits are recorded and both were 0 at base.
- **`wc -l SKILL.md`** is run as a gate, and the 600-line budget is a separate derived
  item whose status is read from `wc -l < SKILL.md` directly (redirection, not a pipe).

Fixes relative to `.ufo/waves/round-76/receipts/tip-battery.sh`: that script measured
the repository it was run in (no clone, so `--rev` could disagree with the tree), had no
absent-instrument status, omitted `check_tip_battery`, `check_skill_evals_v2`,
`check_desc_craft`, `check_r75_routed_repairs` and both census forms, and read the line
count through `wc -l < SKILL.md | tr -d ...` (a pipeline). All of that is replaced.

## 2. Base receipt (deliverable)

```
$ .ufo/waves/round-77/build/E12BatteryScript.battery.sh \
    --rev 6523aced1ee0ebe07dca996213bdc645a6acbd1e \
    --receipt /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/E12BatteryScript.battery-base.txt
battery_exit=1
```

`E12BatteryScript.battery-base.txt` (588 lines): line 1 =
`6523aced1ee0ebe07dca996213bdc645a6acbd1e`; header records lane, clone path,
fleet-shaped sandbox, `.ufo` shape present, census root, watchdog, runner sha256,
UTC time. Result: **gates green 4 of 13; battery: FAIL (9 of 13 red)**.

| # | item | exit | reading |
|---|---|---|---|
| 1 | `verify_corpus_integrity.py --json` | 1 | 4 DRIFTs: tracked 146 vs 144, unindexed 2, report_total 102 vs 99, commit_total 44 vs 43 |
| 2 | `verify_corpus_independent.py --json` | 1 | `corpus.index.unindexed` 2 (`round-75-verifier-spotcheck.md`, `round-76-verifier-spotcheck.md`); everything else PASS/INFO |
| 3 | `check_gate_registry.py --rev` | 1 | `60 of 62 lane verifiers; phantom 0` — `check_desc_craft.py` and `check_r75_routed_repairs.py` have 0 rows |
| 4 | `check_assertion_floors.py` | 1 | `FAIL checklist observed=1863 floor=1863 self_test_failures=1` (all other 16 rows PASS) |
| 5 | `check_tip_battery.py --rev` | 1 | guards 5 of 5; `tip battery exit 0: 1 of 6` (registry/floors/checklist/corpus×2 red; `check_correction_sweep` 0) |
| 6 | `verify_skill_checklist.py --json` | 1 | `fail 1, pass 10`; the one fail is `governance.citation_resolves` at `LOG.md:2818` |
| 7 | `check_skill_evals_v2.py --rev` | 1 | `skill eval artefacts verified 2 of 10` (SKILL.md rendered-line arm) |
| 8 | `check_desc_craft.py --rev` (C1) | 1 | `description craft backed 0 of 6`; (a)–(f) all fail, entry + lesson not committed |
| 9 | `check_r75_routed_repairs.py --rev --work` (C2) | 1 | `r75 routed repairs closed 0 of 4`; R1–R4 open (receipts/note/LOG lines absent) |
| 10 | census `validate --root … kotoba` (fleet lane path) | 0 | `kotoba ok`, 20 W04 duplicate-url warnings (same set as r75/r76) |
| 11 | census `validate --file <clone>/corpus/SOURCES.md` | 0 | `file ok`, same 20 W04 warnings |
| 12 | `wc -l SKILL.md` | 0 | `590 SKILL.md` |
| 13 | SKILL.md budget ≤ 600 (derived) | 0 | `590 lines, within the 600-line budget (wc -l status 0)` |

Four of the nine reds are the ones the plan predicts (items 1, 2, 8, 9). Items 3, 4, 5,
6, 7 are findings — §4.

## 3. Exit-status verification (Q75 capture control)

`E12BatteryScript.exit-verify.txt`: an independent fleet-shaped sandbox (own clone, own
symlinks), `<rev>` checked out, then gates run **directly**, `$?` read on the next line.

```
pipeline control:  false | cat >/dev/null; echo $?  -> 0
direct control:    false;                     echo $?  -> 1
runner check_desc_craft exit: exit=1 ; direct: exit=1
runner check_gate_registry exit: exit=1 ; direct: exit=1
runner verify_corpus_independent exit: exit=1 ; direct: exit=1
runner verify_skill_checklist exit: exit=1 ; direct: exit=1
runner census --file exit: exit=0 ; direct: exit=0
runner wc -l SKILL.md exit: exit=0 ; direct: exit=0
```

Six items (four red, two green) agree exactly, so the capture is not stuck at 0 or at 1.
The direct `verify_skill_checklist` run in the fleet-shaped sandbox reproduces the
runner's single failure (`fail 1, pass 10`, `LOG.md:2818`), i.e. the runner's reading is
the gate's reading. The `battery: PASS` branch is **unexercised**: no revision in range
has all 13 items green (§4), so I do not claim it; the fold over captured statuses is
exercised for both `0` and non-`0` in every run.

## 4. Findings (first falsifiers)

**F1 — committed citation regression at `LOG.md:2818` (not among R76-D1…D5).**
`LOG.md` § Round 76 ends with the token `` `.ufo/reports/round-76/kotoba.md` `` written
bare. `verify_skill_checklist`'s `governance.citation_resolves` requires repo-root
resolution, so it reads red from the lane root; the file exists at the fleet root, so a
`../` prefix resolves it. Consequences at base: item 6 red, item 4 red (the checklist's
own self-test carries the same arm: `self_test_failures=1`), and item 5 red (two of its
six gates are the checklist and the floors guard). Provenance measured, not assumed:
`verify_skill_checklist.py --json` at the r76 base `b7f13f4` exits **0 (11 pass, 0
fail)** while at `6523ace` it exits **1 (1 fail)**; `git blame -L 2818,2818 -- LOG.md`
attributes the line to `ec7f853` (round-76 freeze). Receipt:
`E12BatteryScript.base-provenance.txt`. This is a lane-owner edit, not mine.

**F2 — gate registry 60 of 62 is the pre-data state, and it is the two r76 counters.**
`check_gate_registry.py --rev b7f13f4` exits 0 (`60 of 60`); at `6523ace` it is
`60 of 62`. The two rows the r76 plan scheduled (SKILL.md § Gate registry, +2 rows) are
the missing bytes, so item 3 goes green only when the data lands — the plan's touch list
already covers it, but the battery must not be read as green before that.

**F3 — `check_skill_evals_v2` `2 of 10` is inherited, not this round's.**
It reads `2 of 10`, exit 1 at **both** `b7f13f4` and `6523ace`
(`SKILL.md: 0 rendered lines name the entry + S211/S212/S213`). It belongs to the r71 C2
claim and is a standing red independent of C1/C2 here. Consequence for the plan: the
"every item re-run at the final tip" battery cannot be all-green unless this is either
repaired or recorded as a standing red; it is not caused by, and cannot be fixed by,
the round-77 data.

**F4 — the two corpus gates are red at base exactly as R76-D4 says, and the r76 base
was red too.** At `6523ace`: tracked 146/144, unindexed 2, report_total 102/99,
commit_total 44/43; `verify_corpus_independent` sees the same 2 unindexed files. The
second-revision run (§ below) also reads `exit=1` for both at `b7f13f4`, which matches
the corrected r76 evidence in `LOG.md` § Round 76 ("both corpus gates red at the r75
closure base") and not the earlier r76 plan line that claimed exit 0 there.

**F5 — second revision exercises the revision parameter.** Same script, `--rev
b7f13f4b39cbd43076a85568adca763a6f674e7a`, receipt
`E12BatteryScript.battery-r76base.txt`: **7 of 13 green, 6 red**, with
`check_gate_registry` 0, `check_assertion_floors` 0, `verify_skill_checklist` 0
(the F1 token did not exist yet), `check_tip_battery` `4 of 6`, and the two round-76
counters recorded as `exit=2 — verifiers/<gate>.py is not present at <rev>; the gate was
not run`. So the runner is revision-parameterised, its verdicts change with the
revision, and an absent instrument is not laundered into a red or green gate reading.

## 5. My own defect, retained

The first version cloned to `<scratch>/clone` — right bytes, wrong shape. The checklist
then read `FAIL name_directory` and two `citation_resolves` failures that do not exist in
the lane (9 of 13 red, floor self-test failures 2 instead of 1). Fixed by the
fleet-shaped sandbox (§1); both runs are kept:
`E12BatteryScript.battery-base.clone-shape-defect.txt` (superseded, 27 779 bytes) and
`E12BatteryScript.battery-base.txt` (final, 588 lines). The defect receipt is the
evidence for why the shape rule is in the script header.

The mechanism, for reviewers: `governance.citation_resolves` resolves tokens against the
repo and then hops to the repo's **parent**, so a bare clone under `/fast/scratch` with
no fleet beside it reports spurious failures (`../PROTOCOL.md`, `../.ufo/...`). The
sandbox supplies that parent (every fleet-root entry symlinked read-only beside the
clone), which is why the runner's checklist reading equals the lane's: `10 pass / 1
fail`, exit 1, the sole failure being `LOG.md:2818`. Seat `E10GateRepair` measured the
same `10/1` at `6523ace` in a clone it placed beside a fleet overlay, and `11/0` at
`b7f13f4`; the two independent readings agree. E10 also reported the two in-place /
append-only repair routes (its receipts `E10GateRepair.battery-log-pointer.txt`
§§5–7); both are lane edits outside this seat's write scope and are the L1's call.

## 6. Operability notes

- Wall time: 210 s for the base run (dominated by `check_assertion_floors` ≈ 100 s and
  `check_tip_battery` ≈ 108 s), 204 s for the r76 base; the two runs also completed
  concurrently, so ~4 min per receipt is the working estimate.
- Trap cleanup verified: after both runs `/fast/scratch/hyaku/kotoba-r77/E12BatteryScript/`
  holds no `run.*` directory (only my own `xcheck/`, removed before yield).
- The runner refuses a fleet root that is the lane itself, a non-directory fleet root, a
  non-commit `--rev`, a clone whose toplevel is not the clone, and a HEAD that differs
  from the resolved rev (all exit 2 with a message).
- No tools installed or upgraded (nothing was needed; no pacman, no uv/npx).

## 7. Risks / open

- R1: the plan's "battery green at the final tip" is unreachable while F1 stands (it
  alone keeps items 4, 5, 6 red). The L1 must fix `LOG.md:2818` (or record F1 as a known
  red) before quoting a green battery, and the fix must land **before** the tip-battery
  run — otherwise `check_tip_battery` and the floors arm stay red at the tip whatever
  else is repaired. `E10GateRepair` reports both candidate routes measured to take the
  checklist and the floors arm to exit 0 (an in-place one-line rewrite, which breaks
  LOG.md's append-only rule, versus a four-edit append-only correction whose pinned row
  and notice sha256 live in its receipt §6); I verified neither route and applied
  nothing.
- R2: F3 (evals_v2 2 of 10) is a second unavoidable red at any tip of this lane's
  current bytes; it should be named as a standing red in the round report rather than
  left for a reviewer to discover.
- R3: my runner's census fleet-form reads the **live** fleet lane path by design (the
  plan's command); it is not a measurement of the clone. Both forms are labelled in the
  receipt, but a reader skimming only the fleet line would be reading the lane on disk,
  not `<rev>`.

VERDICT: Runner built and exercised (two revisions, 4/13 and 7/13 green); base is red on 9 of 13 — the 4 planned reds plus three findings: a committed `LOG.md:2818` citation regression that also reddens floors/checklist/tip-battery, the pre-data 60-of-62 registry, and an inherited evals_v2 2-of-10 — so a green tip battery requires lane edits outside this seat's scope.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/E12BatteryScript.battery.sh, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/E12BatteryScript.battery-base.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/E12BatteryScript.battery-r76base.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/E12BatteryScript.exit-verify.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/E12BatteryScript.base-provenance.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/E12BatteryScript.battery-base.clone-shape-defect.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w1/E12BatteryScript.md
