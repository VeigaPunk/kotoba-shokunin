# Kb81E15Order — integration-order runbook (executor, leaf) — round 81 / w1

Deliverable: `.ufo/waves/round-81/build/Kb81E15Order.md` (the ordered L1 integration recipe) plus its
receipts in `.ufo/waves/round-81/build/Kb81E15Order/`. This report is the seat's own account: what was
measured, what the measurements changed, and what the integrator must re-check before each commit group.

Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`, base `b284223105f4d106f7e8f56ed4fd296c643cda0e`
(`HEAD` detached at the base, bookmark `master` at `b2842231`, `ahead=0 behind=0`). Nothing in the lane,
its git/jj state or the fleet root was written; every probe ran in a scratch clone under
`/fast/scratch/hyaku/kotoba-r81/Kb81E15Order/` (removed before yielding).

## 1. What the runbook delivers

An ordered recipe with the gate reading after each group, and the failure modes with the exact strings
they print. Groups:

    G0  plans/round-81.md                                     (the frozen plan, before any repair)
    G1  corpus content + README rows + SOURCES rows + snapshots/ + dispositions/
    G2  verify_corpus_integrity.py + verify_corpus_independent.py + external-commits.json
        + check_tip_battery.py   (ONE commit: the pins are a function of exactly these bytes)
    G3  verifiers/check_sdk_allowed_tools.py + SKILL.md + PROVINCE.md   (ONE commit: registry row must
        be contiguous with the table, and the file must exist when the row is measured)
    G4  LOG.md + SCORECARD.md
    G5  .ufo/waves/round-81  (+ rm .ufo/wapes)   → the tree becomes clean
    G6  refresh-corpus-baseline.py, then commit verifiers/corpus-baseline.json ALONE (no --carry)
    G7  final battery both forms + C2 counter + report + report-pointer gate
    §3.9 Path B — the ordering if C1 stops (re-cut to 140 / unfixable pin / a control world at 6 of 6)

The ordering rests on four measured facts: the snapshot is a claim input and lives inside the wave dir
(so it must land before the C2 counter can read 1); the index classes are a see-saw (files + rows in one
commit); the registry universe is the top level of `verifiers/` and goes 63 → 64; and the refresh refuses
on **any** untracked file, which is why the wave evidence commits before the refresh.

## 2. Measurements that decided the recipe (all first-hand, receipts named)

| reading | value | receipt |
|---|---|---|
| base registry | `63 of 63; phantom 0`, exit 0 | `Kb81E15Order/base-registry.txt` |
| counter file, no registry row | `63 of 64`, exit 1 | `registry-counter-no-row.txt` |
| counter + row **contiguous** with the table | `64 of 64; phantom 0`, exit 0; SKILL.md 597 lines | `registry-counter-with-row.txt` |
| row present, counter file absent | `63 of 63; phantom 1`, exit 1 | `registry-row-no-file.txt` |
| row placed after the blank line before `## Sources` | invisible to the parser → `63 of 64`, exit 1 | same probe series (runbook § 7.1) |
| refresh at the r81 base | `refused: zero-mode corpus.index.unindexed observed 1`, exit 2, baseline untouched | `refresh-base.txt` |
| G1 content group (real bytes) | `unindexed 0 / stale 0 / missing 0`, `tracked_files 157`, `report_total 111`, `report_dead 1`, `commit_unresolvable 2` (both `SOURCES.md:171-172`) | `G1-integrity.json`, `G1-independent.json` |
| battery at a G1-only tip | `guards 5 of 5; tip battery exit 0: 4 of 6`, exit 1 in both forms; 14 receipts, 10 green | `battery-content-group/` |
| base self-tests | tip battery 69 assertions, integrity 164, independent 105 — all exit 0 | `base-*-selftest.txt` |
| `HEAD:.ufo/reports/round-77/kotoba.md` | resolves in the **fleet** root (8547 B, `## SHONEN`), not in the lane | runbook § 7.3 |
| composed instrument spend (current patches) | **402 added / 29 deleted** (22/3 base + E01 210/10 + E02 170/16) vs frozen `LINE_CAP` 900 | `composed-numstat-v2.txt`, `Kb81E15Order-instrument-cap.txt` |
| C2 at the composed G1+G2+G3 tip | `sdk allowed-tools surface documented 1 of 1`, exit 0, conjuncts a–g ok; `generator world: 1 of 1` | `C2-after.txt` |
| composed G1+G2+G3 tip | `guards 5 of 5; tip battery exit 0: 5 of 6`, exit 1 — the single red is integrity's two equal-mode baseline classes (`tracked_files 157≠154`, `report_total 111≠109`); `report_dead 0`, `commit_unresolvable 0`; independent exit 0; registry `64 of 64`; SKILL 597 lines | `composed-full-tipbattery.txt`, `composed-integrity.json`, `composed-independent.json` |
| `check_province_core.py --rev <tip> --repo .` | `province core rows 2 of 2`, exit 0 | `composed-province-core.txt` |

## 3. Two findings that reached the L1 mid-wave

**(a) The cap arithmetic, measured before the plan was revised.** On the wave's first patch cuts the
composed instrument delta was 269/21 (E02 alone) and 472/31 (E01+E02) against the then-frozen
`LINE_CAP = 140`. That measurement is what made the erratum's 140 → 900 revision visible as a live
decision rather than a silent widening: the plan (current sha256 `4573a9ba…`) now declares 900 with
TIGHT pin tuples, `grep -n '140' plans/round-81.md` returns nothing, and the current stack measures
402/29 — 498 lines under the bound. My 140-era receipts are kept and labelled superseded. The plan's own
E6 justification sentence still cites the superseded cuts (+203/-10, +247/-18, delta +472/-31); the L1
owns that sentence and the freeze receipt must record the measured 402/29 (Main has assigned this).

**(b) One stale pin, which the counter named itself.** At the composed tip built from E01 `6bbb304b…`,
E02 `d8bf88c8…` and the intermediate erratum `c66103f3…`:

    instruments added 402 / deleted 29 lines (cap 900)
    FAIL guard instrument-pin: verifiers/verify_corpus_independent.py blob
      59602942075d8fe77061876fb52eb32a44313697 at d3f29d59… is not a pinned blob
    guards 4 of 5; tip battery exit 0: 4 of 6

The erratum still pinned `7b37461a…`, the earlier 247/18 cut of E02. `Kb81E05Erratum` republished
(`c15680f8…`, counter sha256 `1753b11c…`) with the independent pin at `59602942…` and the integrity pin at
`bbee51f2…`. The runbook records it as a named failure class: **the pin hexes are a function of the
repair bytes, so every re-cut of E01/E02 re-opens § 2.5's check.** Receipt:
`Kb81E15Order/composed-prestale-pin-tipbattery.txt`.

## 4. Traps recorded for the integrator (measured, not inferred)

* The registry parser ends the table section at the first line with no cells: an appended row must be
  contiguous with the last table row (which is why G3 combines file + row + SKILL sentence + PROVINCE).
* `verify_skill_checklist.py` reds `trigger.name_directory` and the `../.ufo/...` citations in any clone
  whose directory is not named `kotoba-shokunin`; judge it in the battery runner's fleet-shaped world.
* The round-76-style symlink commit is **not** needed this round (the dead token is the round-77
  `HEAD:` object, resolvable fleet-side); the fallback is named in the runbook if R1 dead-ends.
* `jj-lane.sh state kotoba` did not read this lane from the fleet root in my run
  (`not a real clone (missing .git directory): kotoba`, exit 1) — use `git rev-parse` /
  `for-each-ref` / `jj bookmark list`.
* `.ufo/wapes` is not blocked by the lane's path guard and survives commits; it blocks the refresh until
  deleted (its bytes are committed under `dispositions/`).
* `run-battery.sh` (r81, sha256 `19b878a1…`) differs from the r80 copy and passes `--fleet` explicitly;
  the frozen predicate's literal `--repo .` / `--repo <lane>` forms are still measured by hand at the tip.

## 5. Tooling, scratch, and non-actions

No tool was installed or upgraded (nothing was needed; pacman paused host-wide and never invoked).
Scratch `/fast/scratch/hyaku/kotoba-r81/Kb81E15Order` removed before yielding; receipts copied to
`.ufo/waves/round-81/build/Kb81E15Order/` first. No file outside that build directory and this report
was written; the plan, corpus, SKILL/PROVINCE, verifiers and the fleet root were read only.

## 5a. The staged reading the recipe is built on (measured, both ends)

    r81 base                 guards 5 of 5; tip battery exit 0: 4 of 6   exit 1
    + G1 (content)           guards 5 of 5; tip battery exit 0: 4 of 6   exit 1   (R1/R2 load-bearing)
    + G2 + G3 (composed)     guards 5 of 5; tip battery exit 0: 5 of 6   exit 1   (integrity: equal-mode only)
    + G6 (refresh+baseline)  guards 5 of 5; tip battery exit 0: 6 of 6   exit 0   (EXPECTED, not measured
                                                                                   by this seat — the L1 measures it)

The third line is the one an integrator is most likely to misread as a stalled repair: `report_dead` and
`commit_unresolvable` are already 0 there, and only the baseline's equal-mode counts keep integrity red.
`6 of 6` before G6 would mean a hand-edited or carried baseline.

## 6. Residual risk the L1 should carry

* The composition may still move (E01/E02 were re-cut twice during the wave). Every pin claim in the
  runbook is timestamped by patch sha256; re-run § 2.4–§ 2.5 against the frozen bytes before G2.
* The C2 counter prints a `generator world: 1 of 1` line that reaches the target. That is the r79/r80
  failure class (a mechanical generator satisfying the predicate); it is the critics' surface, recorded
  here as an observation, and I did not adjudicate or narrow it.

VERDICT: integration-order runbook delivered with first-hand r81-byte gate readings (registry 63→64 arms, G1 class set, refresh refusal, composed cap 402/29, the counter's own stale-pin FAIL, C2 1 of 1, staged battery 4/6 and 5/6 measured, post-G6 6/6 predicted only) and both a full-landing and a C1-stop ordering; no lane file mutated.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E15Order.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81E15Order.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E15Order/
