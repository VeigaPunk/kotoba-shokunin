# Kb81E10Battery — battery runner + base no-harm receipts (round 81, w1)

Scope executed: (A) port the r80 battery runner into the r81 build dir; (B) run the base
no-harm set at `b284223105f4d106f7e8f56ed4fd296c643cda0e` and publish per-gate receipts.
No claim after-value was measured or scored (freeze discipline); this seat reads base only.

## A — runner port `build/run-battery.sh`

```
$ install -m 755 .ufo/waves/round-80/build/run-battery.sh \
                   .ufo/waves/round-81/build/run-battery.sh
$ bash -n .ufo/waves/round-81/build/run-battery.sh   # SYNTAX-OK
$ sha256sum .ufo/waves/round-80/build/run-battery.sh .ufo/waves/round-81/build/run-battery.sh
cddf2dd8852801206a152dec62a62d64409453a280cef82cb3a002d7636d7601  .../round-80/build/run-battery.sh
19b878a12d07a5dc5a0e05b548a0be23910deaef72360be07f40b40f921fc76a  .../round-81/build/run-battery.sh
```

`diff -u` = **3 hunks, text only, zero logic deltas**:

1. title lines 2–3: `round-80 … Kb80E10Battery` -> `round-81 … Ported from round-80 by seat
   Kb81E10Battery`.
2. `HYAKU_SCRATCH` doc block: default described as `/fast/scratch/hyaku/kotoba-r81/Kb81E10Battery`
   with per-run dir `$HYAKU_SCRATCH/battery/`.
3. `SCRATCH_ROOT` default: `…/hyaku}/kotoba-r80-battery` ->
   `${HYAKU_SCRATCH:-/fast/scratch/hyaku/kotoba-r81/Kb81E10Battery}/battery`.

Usage block (`sed -n '2,46p'`) still ends on the `mismatch, a required gate absent at <rev>).`
line, so `--help`/usage output is intact after the retitle (verified: lines 46–50 unchanged in
position). Contract musts all hold, inherited and re-verified in the run below: `set -u`;
`TMPDIR` exported inside scratch before any gate runs (the floors self-test writes fixtures
there); per-command own-exit capture `( cd "$cwd" && exec timeout "$tmo" bash -c "$cmd" ) >>"$f"
2>&1; rc=$?` (never a pipeline's status); receipt line 1
`# rev=<full> cmd=<command> utc=<ISO-8601Z>`.

## B — base battery: `build/base-battery/` (14 receipts, 10 green, 4 red)

```
$ HYAKU_SCRATCH=/fast/scratch/hyaku/kotoba-r81/Kb81E10Battery \
  bash .ufo/waves/round-81/build/run-battery.sh \
    b284223105f4d106f7e8f56ed4fd296c643cda0e \
    /home/vgpnk/Projects/shokunin/kotoba-shokunin \
    .ufo/waves/round-81/build/base-battery
# -> 14 receipt(s), 10 exit 0, 4 non-zero
# 01: fleet root /home/vgpnk/Projects/shokunin; guards 5 of 5; tip battery exit 0: 4 of 6
# 02: fleet root /home/vgpnk/Projects/shokunin; guards 5 of 5; tip battery exit 0: 4 of 6
# RUNNER-EXIT=1        (red battery = reading; see the runner's exit-status doc block)
```

Wall 334.8 s; tip-battery forms 111.0 s / 108.8 s (floors gate 107.8 s inside each); disk guard
checked pre-run (`/fast/scratch/hyaku` 27 % use, 592.2 G free). World:
`/fast/scratch/hyaku/kotoba-r81/Kb81E10Battery/battery/run-541851-12958/world/kotoba-shokunin`
(fleet-shaped clone, `HEAD == b2842231…`, removed on exit). Header invariant re-checked on all 14
receipts: 14/14 carry `# rev=b284223105f4d106f7e8f56ed4fd296c643cda0e cmd=… utc=…`.

Per-file index (full table with figures: `build/Kb81E10Battery.md`):

| # | receipt | exit | reading |
|---|---|---|---|
| 01 | tip-battery-dot | 1 | `guards 5 of 5; tip battery exit 0: 4 of 6` (`--repo .` from world lane root) |
| 02 | tip-battery-abs | 1 | identical line, absolute `--repo <lane>` |
| 03 | gate-registry `--rev` | 0 | `rows conformant 63 of 63 lane verifiers; phantom 0` |
| 04 | assertion-floors | 0 | 17 PASS floor rows, 0 fail |
| 05 | skill-checklist `--json` | 0 | 11 checks PASS, 0 FAIL/WARN/SKIP |
| 06 | corpus-integrity `--json` | 1 | 5 DRIFT |
| 07 | corpus-independent `--json` | 1 | 2 DRIFT |
| 08 | correction-sweep `--root .` | 0 | `0 stale block(s)` |
| 09 | fleet census (live tree) | 0 | `kotoba ok corpus/SOURCES.md`, 31 `W04` warnings |
| 10–14 | SKILL.md figures | 0 | 596 lines, 80920 B, 151 >120, 81 >300, `longest=1095 line=514` |

Base truths, matching `plans/round-81.md` §Trigger exactly (both tip-battery forms, exit 1):

- `06`: `tracked_files` 155≠154; `unindexed` 1 = `corpus/lessons/round-80-verifier-spotcheck.md`;
  `report_total` 111≠109; `report_dead` 1 =
  `corpus/lessons/round-77-verifier-spotcheck.md:15: HEAD:.ufo/reports/round-77/kotoba.md`;
  `commit_unresolvable` 2 = `corpus/SOURCES.md:171-172` `7bb48f213ac6…`.
- `07`: `index.unindexed` 1 (same file) and `commit_unresolvable` 2 (same two tokens).

## Findings handed to the L1 / the repair seats (measured, not judged)

**F1 — the plan's independent-gate sentence does not match bytes.** §Trigger says
`verify_corpus_independent.py` exits 1 "on the same `commit_unresolvable` 2 plus `report_dead` 1".
Measured at `b2842231` (receipt 07): `report_dead` **0** (PASS) and the second DRIFT is
`corpus.index.unindexed` 1. Exit 1 is real; the red set is not the one written. Independently of
the claim predicate (which measures the tip battery), R1's report-pointer resolution should be
proven on the gate that actually reads `HEAD:.ufo/reports/round-77/kotoba.md` dead — integrity —
and the two gates disagree on that token today (integrity `report_dead` 1, independent 0). The
round-81 lesson's base table should carry the measured set.

**F2 — SKILL.md budget headroom is 4 lines.** `05`: `trigger.line_budget` = "596 lines within
budget 600". The C2 SDK-channel line, the registry row text and any C1 documentation line all
land inside that budget; 151 lines already exceed 120 chars and the longest line is 1095 (line
514), so a line added without checking the 600 budget reddens the checklist gate.

**F3 — the C2 counter row is load-bearing, not bookkeeping.** `03` reads
`63 of 63 lane verifiers` conformant at base; a new `verifiers/check_sdk_allowed_tools.py`
without its registry row reads 63 of 64 and reddens `check_gate_registry.py` — which is itself
one of the six gates inside the tip battery.

**F4 — E6 arithmetic inputs, measured on the base counter.** Receipt 01 prints
`guarded paths 586, deleted 0; floors 15 rows; instruments added 22 / deleted 3 lines (cap 40)`.
So base consumption is **added 22 / deleted 3 against `LINE_CAP` 40**, i.e. the erratum's cap
check at the landed tip is `22 + (r81 instrument patch added lines) ≤ 140`, which leaves **118
added lines, not 140**. Consequence for the erratum: the plan's 60–120 estimate fits only up to
118 — a two-gate repair measuring 120 added lines (22 + 120 = 142) trips `instrument-size` and
the claim stops on its own kill rule. Prose in receipt 01 uses `base 072048fa8e8a…` (the
counter's BASE constant) as the comparison point, so `22` is instrumentation growth from
`072048fa` to `b2842231`, not from the r81 base. `floors 15 rows` is the row count of
`verifiers/floors-registry.json` (the tip battery's floors guard reads the registry file);
`check_assertion_floors.py` itself prints 17 counter rows. Both green — an observation about two
different row sources, not a defect.

**F5 — reader caveat on `index.txt`.** The runner's `figure_of` takes the last non-comment body
line, so the three `--json` receipts (05/06/07) index as `}`; their verdict is the `exit=` column
and the per-file table above. Left as-is (r80-reviewed behaviour; the exit status is the verdict
per M80-1) rather than "fixing" a reviewed artifact mid-claim.

## Not done (deliberately out of this seat's scope)

- No after-value of C1/C2 measured, no control/shortcut world scored, no counter or corpus file
  touched — those ride the executor/critic seats.
- No lane write outside `.ufo/waves/round-81/{build,w1}`; lane `git status --porcelain` is
  unchanged from this seat's start (`?? .ufo/wapes`, `?? .ufo/waves/round-81/`,
  `?? plans/round-81.md`; `HEAD = b2842231…`). No commit/add/checkout/stash in the lane.
- No tool installs; pacman not invoked (host-wide pause honoured). No background jobs beyond the
  single battery process; peak concurrency 1 battery + its own children.
- Scratch `/fast/scratch/hyaku/kotoba-r81/Kb81E10Battery` removed after the run (verified absent;
  only sibling seats' dirs remain under `kotoba-r81/`).

## Risks / blockers

- **R-1 (calibration):** the plan's baseline prose (F1) and any downstream seat copying it will
  state a red set the bytes do not show; the claim predicate is unaffected, the narrative is.
- **R-2 (budget):** F2's 4-line SKILL.md headroom is the tightest numeric in the wave; a C2 line
  added without re-counting reddens checklist and (via the battery) the C1 predicate.
- **R-3 (index legibility):** F5 means `base-battery/index.txt` alone under-reports 05/06/07
  figures; consumers should read the receipts' `exit=` or this seat's table.
- No blocker: the base battery is complete and reproducible with the command above.

VERDICT: r81 runner ported byte-faithfully (3 text hunks, no logic change) and the base no-harm battery is receipted at b2842231 — tip battery `guards 5 of 5; tip battery exit 0: 4 of 6`, exit 1, in both `--repo .` and absolute `--repo <lane>` forms; 14 receipts, 10 exit 0 / 4 exit 1, exactly the plan's base red set, with one plan-text divergence flagged (independent gate reads `report_dead 0`, its second DRIFT is `index.unindexed`).
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/run-battery.sh; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E10Battery.md; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/base-battery/ (01–14 receipts + index.txt); /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81E10Battery.md
