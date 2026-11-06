# ExecBaseBattery — base no-harm readings and floors-timeout measurement (r95-w1)

Freeze commit `673d1e2e6f850bb54dda9698cf825cf6788c7d0d`. Scratch clone `/fast/scratch/hyaku/kotoba-r95/ExecBaseBattery/repo` (toplevel verified). Receipts (command, cwd, rc, wall_s, uptime start/end, output) under `.ufo/waves/round-95/w1/ExecBaseBattery/*.log`. No patch (seat spec: no-harm readings only). Host: 32 CPUs. `bc` unavailable (wall timed via Python).

## Results at 673d1e2e6f850bb54dda9698cf825cf6788c7d0d

| gate | rc | wall | final line |
|---|---|---|---|
| `check_gate_registry.py --rev 673d1e…` | 0 | 0.4 s | 74 of 74 conformant, phantom 0 |
| `check_assertion_floors.py --self-test` | 0 | 5.5 s | `0 failure(s) over 176 assertions` |
| `check_assertion_floors.py` (plain walk) | 0 | 190.3 s | all 19 PASS (checklist 1864/1863 … freeze_gate 34/34) |
| slowest child standalone `verify_harness_independent.py --self-test` | 0 | 173.1 s | `0 failure(s) over 123 assertions` |
| 2nd child `compare_harness_independent.py --self-test` | 0 | 3.1 s | (compare 330) |
| round-93 `c1-killpin-rev.sh 673d1e… $D` | 0 | 47.4 s | `C1-PREDICATE-MET` |
| round-93 `c2-pinkey.sh 673d1e… $D` | 0 | 596.9 s (3× tip battery) | `C2-PREDICATE-MET` |
| round-94 `selftest-kills.py c1 673d1e… $D` | 0 | 44.0 s | `C1-PREDICATE-MET` (3/3 + positive 1/1, decoys 3/3) |
| round-94 `selftest-kills.py c2 673d1e… $D` | 0 | 20.9 s | `C2-PREDICATE-MET` |
| round-92 `controls-run.sh` | 0 | 443.0 s | `shortcuts refused 2 of 2; honest held 2 of 2` |
| tip battery `check_tip_battery.py --rev 673d1e… --repo $D --fleet /home/vgpnk/Projects/shokunin` | 1 (3 of 6, base-red carry) | 213.6 s | `guards 5 of 5`; floors gate exit 0 wall 209.0 s (did NOT time out this run) |

Loaded host throughout (loadavg 1-min 2–30; tip-battery end 29.7).

## Routed defect 5 — why the floors gate timed out at 280 s under fleet load

Two stacked caps, badly mismatched:

- Inner (floors itself, `verifiers/check_assertion_floors.py`): per-child cap `child_timeout_s(360, load) = 360 × min(max(1,loadavg1),15)` — 360 s at idle, scaled by load. Slowest child measured standalone here: **173.1 s** at loadavg1 ~6 (round-91 pinned 161 s idle). Full walk is 190.3 s standalone (child = 91 % of it). So the inner cap is generous: at load 6 the cap is 2160 s.
- Outer (tip battery, `verifiers/check_tip_battery.py:113` `GATE_TIMEOUT_S = 280`, applied flat to all six gates in `run_battery`, line ~388: `subprocess.run(..., timeout=GATE_TIMEOUT_S)`): the floors gate is invoked bare (`("verifiers/check_assertion_floors.py", ())`, line 180) — no `--self-test-timeout`/`--load` override. This run it took **209.0 s** and passed, but only 71 s inside the cap. The margin is one slow sibling away.

Why it timed out in round 94: the standalone floor is already 190 s when measured alone (slowest child 173 s ≈ 91 % of total). Under fleet load (loadavg1 observed 20–30 during this seat's own runs on the 32-CPU host; tip-battery end 29.66), CPU contention stretches the child non-linearly — round-55 measured 185–222 s for the same child against a 120 s cap, and round-56 scaled the inner cap for exactly this reason (`child_timeout_s` docstring). The outer 280 s flat cap was never scaled. A child that needs 173 s idle needs only a 1.6× slowdown (load ~ that of 50+ runnable threads on 32 cores) to exceed the outer cap while the inner cap still holds (5400 s at load ≥15). The timeout is then reported as the gate not-counted (`rc=None, "timeout after 280 s"`), so the battery reads 2 of 6 instead of 3 of 6 (3 of 6 being the base-red carry: checklist/corpus_integrity/corpus_independent red at base by design).

Note the asymmetry: `floors` inside the tip battery *passes* under load whenever it finishes (its inner cap scales), but the tip *counts* it as timeout at 280 s flat. The round-94 landing `2 of 6` is this flat-cap artifact, not a floors failure.

## Smallest robust change (recommendation only — no file edited)

Give the floors gate in `check_tip_battery.py` a load-aware outer cap matching the inner one, e.g. `GATE_TIMEOUT_S_FLOORS = 360 × min(max(1.0, getloadavg1), 15)` computed per-gate in `run_battery` (reusing the floors `child_timeout_s` model), or pass `--self-test-timeout 280` … no: better to raise floors-gate outer cap to at least the inner cap so the outer can never fire before the inner. Minimal delta: per-gate timeout `(script == "verifiers/check_assertion_floors.py") ? child_timeout_s(360, load) : 280`. Alternatively a fixed 900 s floors-gate cap still covers 5.2× slowdown vs 173 s idle but less principled than mirroring the load scaling; any fixed cap re-creates the defect at higher load. Also worth a follow-up: unstick the child — 173 s of 190 s walk in one child suggests splitting `verify_harness_independent.py`'s self-test or running floors children concurrently (its inner walk is serial).

## Risks / blockers

- None blocking. All no-harm readings taken at the freeze commit match base expectations (74/74; round-93 C1/C2 MET; round-94 c1/c2 MET; round-92 2/2+2/2; floors self-test 176 assertions, walk all PASS; tip guards 5/5, 3/6 base-carry).
- No tool installs were needed; `bc` missing noted (used Python timing). No patch written per seat spec.
