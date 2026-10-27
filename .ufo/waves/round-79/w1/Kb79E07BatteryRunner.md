# Seat Kb79E07BatteryRunner — C1 final-tip battery runner (round 79 w1)

Assignment: build `run-battery.sh <rev> <lane-repo> <out-dir>` for the plan's
no-harm battery (`plans/round-79.md` § No-harm battery), prove it once at the r79
base `b10bcbc6b00f8f56b202ccbadca311007b5b463c`, and deliver the base receipts.
Delivered: the runner, a reader crosschecker, and 14 receipts + index at the base.

## 1. Usage

```
run-battery.sh <rev> <lane-repo> <out-dir> [<report-path>]
```

`bash /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/run-battery.sh <rev> /home/vgpnk/Projects/shokunin/kotoba-shokunin <out-dir>`

`<rev>` is resolved to a full commit hash first; `<lane-repo>` must be the lane's
own git toplevel (the real lane, not a clone — the two `check_tip_battery.py`
forms build their own fleet-shaped sandbox from `--repo`/`--fleet`, so they need
the real lane); `<out-dir>` receives one receipt per command plus `index.txt`;
the optional fourth argument adds the plan's `check_report_pointers.py` step on
a round report. Exit 0 = every command exited 0, exit 1 = at least one command
exited non-zero (a red battery is a reading, not a runner failure), exit 2 =
usage/environment error (unresolvable rev, non-toplevel lane, absent gate at
that rev, unclonable lane, scratch toplevel mismatch).

Runner bytes: sha256 `94c40d8afa85c31ade71a13b2d0a0cde6112cc3739729b84d3fa7143eeea6d28`
Reader bytes: sha256 `bab2d5279eef7469d2406152b41e5e7a587dada1f7302d79e1c0242712cf753b`

## 2. Behaviour

Receipt format (one file per command, `<out-dir>/NN-<name>.txt`):

```
# rev=<full hash> cmd=<the command> utc=<ISO-8601 Z>
# cwd=<the directory the command ran in>
# timeout=<n>s shell=bash-o-pipefail wall=<n>s
# note=<why this command is shaped this way>
<body: the command's own stdout+stderr, byte for byte>
exit=<the command's own status>
```

Exit capture is the command's own: `( cd "$cwd" && exec timeout ... bash -o
pipefail -c "$cmd" ) > body 2>&1; rc=$?` — never a downstream pipeline's. The
two `awk … | wc -l` figures run under `bash -o pipefail`, so their `exit=` is the
pipeline's own status (any stage failing), and the header says so
(`shell=bash-o-pipefail`). A hang is receipted as `exit=124` (coreutils
`timeout`), never as green.

Commands, in order: 01 `check_tip_battery.py --rev <rev> --repo .` run from the
lane root (plan form 1); 02 the same counter with `--repo <abs lane>` (form 2);
03–08 the six frozen gates (`check_gate_registry.py --rev`, `check_assertion_
floors.py`, `verify_skill_checklist.py --json`, `verify_corpus_integrity.py
--json`, `verify_corpus_independent.py --json`, `check_correction_sweep.py
--root .` — the same argv the frozen battery runs); 09 the fleet census
(`sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`);
10–14 the SKILL.md figures (`wc -l`, `wc -c`, lines >120, lines >300, longest
line + its number); 15 (optional) `check_report_pointers.py`.

Where each runs: 01/02 from the real lane; 03–08 and 10–14 in a scratch clone
checked out at `<rev>`; 09 at the fleet root against the live lane tree (the
census has no `--rev`; its receipt says `# note=census reads the LIVE lane tree`).

The scratch clone is **fleet-shaped**, not bare: clone at
`$S/world/<lane basename>`, every other entry of the lane's fleet root symlinked
beside it (the same construction as `check_tip_battery.build_sandbox`). This is
not decoration — see §6 finding F1: the same rev reads
`verify_skill_checklist.py --self-test` as 2 failures in a bare clone and 1 in a
fleet-shaped one, because the governance checks resolve `../.ufo/...` from the
repo root. Scratch lives at `$HYAKU_SCRATCH/kotoba-r79-battery/run-<pid>-<rand>`
(default `$HYAKU_SCRATCH=/fast/scratch/hyaku`), `TMPDIR` is exported inside it,
the per-run dir is removed on exit (verified: `ls -A
/fast/scratch/hyaku/kotoba-r79-battery` is empty after two runs). Only the empty
shared parent stays, deliberately: a concurrent run may own it. Read-only on the
lane; no git write outside scratch. Commands run one at a time, so the runner
never holds more than one battery process.

## 3. Base run (tested once, as assigned)

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build
$ bash run-battery.sh b10bcbc6b00f8f56b202ccbadca311007b5b463c \
      /home/vgpnk/Projects/shokunin/kotoba-shokunin \
      /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/battery-base
RUNNER EXIT=1
run-battery.sh: rev b10bcbc6b00f8f56b202ccbadca311007b5b463c; 14 receipt(s), 7 exit 0, 7 non-zero
01-tip-battery-dot: fleet root /home/vgpnk/Projects/shokunin; guards 5 of 5; tip battery exit 0: 1 of 6
02-tip-battery-abs: fleet root /home/vgpnk/Projects/shokunin; guards 5 of 5; tip battery exit 0: 1 of 6
```
wall 318.71 s, Python 3.14.8, git 2.56.0, receipts 68 K total (all small text).

| receipt | exit | last body line |
|---|---|---|
| 01-tip-battery-dot.txt | 1 | `fleet root /home/vgpnk/Projects/shokunin; guards 5 of 5; tip battery exit 0: 1 of 6` |
| 02-tip-battery-abs.txt | 1 | `fleet root /home/vgpnk/Projects/shokunin; guards 5 of 5; tip battery exit 0: 1 of 6` |
| 03-gate-registry.txt | 1 | `gate registry rows conformant 60 of 62 lane verifiers; phantom 0` |
| 04-assertion-floors.txt | 1 | `FAIL checklist observed=1863 floor=1863 self_test_failures=1` |
| 05-skill-checklist.txt | 1 | `"pass": 10` (fail 1: `governance.citation_resolves LOG.md:2818 '.ufo/reports/round-76/kotoba.md' does not resolve`) |
| 06-corpus-integrity.txt | 1 | 5 DRIFT of 9: `index.tracked_files` 150/144, `index.unindexed` 6/0, `pointers.report_total` 106/99, `pointers.report_dead` 1/0, `pointers.commit_total` 45/43 |
| 07-corpus-independent.txt | 1 | 1 DRIFT: `corpus.index.unindexed` 6 |
| 08-correction-sweep.txt | 0 | `correction sweep: 0 stale block(s)` |
| 09-census.txt | 0 | `kotoba ok /home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md` (20 W04 warning lines) |
| 10-skill-lines.txt | 0 | `590 SKILL.md` |
| 11-skill-bytes.txt | 0 | `78647 SKILL.md` |
| 12-skill-long120.txt | 0 | `147` |
| 13-skill-long300.txt | 0 | `77` |
| 14-skill-longest.txt | 0 | `longest=1095 line=511` |

This reproduces the plan's base receipts
(`.ufo/waves/round-79/receipts/tipbattery-base-{dot,abs}.txt`) exactly: guards
5 of 5, gates 1 of 6, both forms, exit 1. Base figures for considerthese
2026-10-26 proposal 1 (recorded, not claimed): SKILL.md 590 lines / 78647 B /
147 lines >120 / 77 lines >300 / longest line 1095 at line 511.

## 4. Cross-check: standalone gates vs the frozen battery's own readings

`python3 -B battery-crosscheck.py battery-base` (output
`build/battery-base-crosscheck.txt`, exit 0):

```
verifiers/check_assertion_floors.py      1  1  1  agree
verifiers/check_correction_sweep.py      0  0  0  agree
verifiers/check_gate_registry.py         1  1  1  agree
verifiers/verify_corpus_independent.py   1  1  1  agree
verifiers/verify_corpus_integrity.py     1  1  1  agree
verifiers/verify_skill_checklist.py      1  1  1  agree
crosscheck: 0 gate(s) disagree; forms print the same frozen line: yes; revs seen b10bcbc6…
crosscheck: 6 of 6 gate(s) compared across both forms and the standalone receipts
```

So the by-hand receipts and the sandbox's per-gate lines agree at the base, and
the single green gate is `check_correction_sweep.py` — i.e. the plan's `1 of 6`
is exactly the five red gates named in its Trigger, not a miscount.

## 5. Negative controls (the runner's own falsifiers)

`build/runner-negative-controls.txt`:

- N1 unresolvable rev → `exit=2`, message `cannot resolve deadbeef… in
  /home/vgpnk/Projects/shokunin/kotoba-shokunin`, no out-dir created.
- N2 a rev that resolves but predates the gates (root commit
  `43e0c0224876da4a7ba0a86d852b6f621cfecd67`) → `exit=2`,
  `check_gate_registry.py absent at 43e0c0…`, zero receipts written.

An unrun check therefore cannot masquerade as green: the battery either
produces a receipt with an `exit=` line or refuses to start.

## 6. Findings for the L1 (calibration, not claim data)

- **F1 — the floors gate is fleet-shape sensitive at the same rev.**
  `verify_skill_checklist.py --self-test` in a bare clone at `b10bcbc` reads
  `2 failure(s) over 1863 assertions` (three runs, identical; receipts
  `build/probe-bare-clone/selftest-bare-{1,2,3}.log`), so the bare-clone
  `check_assertion_floors.py` receipt reads
  `FAIL checklist observed=1863 floor=1863 self_test_failures=**2**`
  (`build/probe-bare-clone/04-assertion-floors.bare-clone.txt`,
  `build/probe-bare-clone/run-bare-clone-v1.log`); fleet-shaped, the same rev
  reads `self_test_failures=**1**` (receipt 04 here, and the same line in the
  plan's Trigger). The failures are `governance: live round-65 corrections land`
  and `LOG.md:2678 erratum is load-bearing`, both resolving
  `../.ufo/reports/round-60/kotoba.md` from the repo root. Consequence for C1:
  any receipt for this gate must name its world shape, and a repair judged on a
  bare clone would be judged against a world the tip battery never measures.
  The runner therefore fleet-shapes the clone.
- **F2 — `verify_corpus_integrity.py` at base has five DRIFT rows, not four.**
  The plan's Trigger quotes four; the receipt also carries
  `corpus.pointers.commit_total observed=45 expected=43` (receipt 06). If the
  repair is scoped to the four named rows, C1 cannot reach 6 of 6.
- **F3 — the census is live-tree, not revision-bound.** `sources-census.sh`
  accepts `--root` (fleet) and a lane id, no `--rev`; receipt 09 measures the
  lane's working tree as it stood at run time. Its `# note=` says so; a census
  receipt can never be attributed to a commit by its own command line.
- **F4 — fleet-level pointers resolve against the LIVE fleet, in the runner and
  in the frozen counter alike.** The fleet-shaped clone symlinks the real fleet
  entries, so `../.ufo/...` reaches the live `.ufo`, not a snapshot of it. Same
  semantics as `check_tip_battery.build_sandbox`; a receipt that depends on
  `../.ufo` is only as reproducible as the fleet is.
- **F5 — the frozen battery's own run is not cheap:** 01/02 cost ~100 s each
  (the floors gate alone is 101 s inside them) and the whole 14-command set was
  319 s. Running both forms twice per wave is ~10 min of wall time; budget it in
  the landing order rather than in a lane commit.
- **F6 — `check_report_pointers.py` cannot be revision-bound** (its subject is a
  report file outside the lane tree), which is why it is the runner's optional
  fourth argument rather than a fixed receipt.

## 7. Risks / limits

- The runner measures the tree of `<rev>` for gates 03–08 and 10–14, but the two
  tip-battery forms and the census read the real lane and the live fleet by
  design (§F3/F4). A receipt set is therefore "rev-bound tree + live fleet".
- A scratch clone cannot be passed as `<lane-repo>`: the tip battery derives its
  fleet root from `--repo`'s parent, and a clone under `$HYAKU_SCRATCH` has no
  fleet beside it — it would fail or measure a different world. The runner takes
  the real lane and says so in the usage text.
- Gate timeouts are generous (600 s, 900 s for the tip batteries) so a slow host
  cannot turn a green gate into `exit=124`; a host that needs more than that will
  receipt a timeout, which is a reading, not silence.
- Tooling: nothing installed or upgraded this seat (authorised installs unused).

## 8. Files changed

- `.ufo/waves/round-79/build/run-battery.sh` (new, executable, 273 lines)
- `.ufo/waves/round-79/build/battery-crosscheck.py` (new, executable)
- `.ufo/waves/round-79/build/battery-base/` (new: 14 receipts + index.txt, 68 K)
- `.ufo/waves/round-79/build/battery-base.run.log` (new: the run's stdout/stderr)
- `.ufo/waves/round-79/build/battery-base-crosscheck.txt` (new: crosscheck output)
- `.ufo/waves/round-79/build/runner-negative-controls.txt` (new: N1/N2)
- `.ufo/waves/round-79/build/probe-bare-clone/` (new: bare-clone probe logs and
  the superseded bare-clone receipts 04/05 + v1 run log)
- scratch `/fast/scratch/hyaku/kotoba-r79/Kb79E07BatteryRunner` removed.

VERDICT: Runner delivered and measured once at base b10bcbc — 14 receipts, both frozen forms read `guards 5 of 5; tip battery exit 0: 1 of 6` (exit 1), the six by-hand gate exits agree 6 of 6 with the sandbox's own lines, and two negative controls exit 2 with zero receipts; two calibration defects for C1 are on record (floors self-test count is fleet-shape dependent 2 vs 1; corpus integrity has five DRIFT rows, not the four quoted).
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/run-battery.sh, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/battery-crosscheck.py, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/battery-base/, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/battery-base-crosscheck.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/runner-negative-controls.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/w1/Kb79E07BatteryRunner.md
