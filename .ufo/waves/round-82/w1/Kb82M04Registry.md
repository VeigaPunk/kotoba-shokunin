# Kb82M04Registry — round 82 registry-gate and checklist self-test probes

Base: `47dbe8781657de563ff867caca6244d28e3db504` (scratch clone, `git -C clone`, toplevel asserted before every mutation). Control-world probes only; no production after-value scored. Lane-owned output: this file plus `.ufo/waves/round-82/build/Kb82M04Registry-probes/`. No commits, pushes, or jj mutations in the fleet; no tools installed (pacman paused, none needed).

## Axes

- freshness: registry rows and verdict descriptions still describe the code after an edit.
- operability: the registry gate rejects unregistered verifiers; the checklist self-test count/invariant guards catch arm removal.
- no-harm: fleet bytes untouched; scratch removed after copying receipts.

## Results

| # | Probe | Expected | Observed | Verdict |
|---|---|---|---|---|
| A1 | Comment-only edit to existing `check_gate_registry.py` | no new row needed | counter `64 of 64; phantom 0`, exit 0 | confirmed |
| A2 | Failure exit changed `1` → `3` in `check_gate_registry.py` (row still says `1=failed`) | row drift visible | counter flags nothing about the exit map; a failing run now exits 3 | **gap** (verdict-map exit codes are not checked; the counter's own docstring says it does not run scripts, Q31) |
| A3 | Self-test flag string changed `--self-test` → `--selftest` (argparse `dest` kept) | row flagged | `verifiers/check_gate_registry.py no self-test flag --self-test lacks an exact handler`; `63 of 64`; exit 1 | confirmed |
| A3′ | Same rename without `dest=` | — | gate crashed with `AttributeError` before judging (self-inflicted; not a gate result) | recorded, not a finding |
| B1 | Unregistered `verifiers/zz_r82_probe_unregistered.py` | rejected | `no registry rows naming it: 0 (need 1)`; `64 of 65`; exit 1 | confirmed |
| B2 | Unregistered `verifiers/zz_r82_probe_unregistered.js` | rejected | `64 of 64`, exit 0 — outside universe (`.py`/`.sh` only) | **gap** |
| B3 | Unregistered `verifiers/r82sub/zz_r82_probe_nested.py` | rejected | `64 of 64`, exit 0 — outside universe (no recursion) | **gap** |
| C1 | Remove live governance arm `governance: live round-65 corrections land, errata-excused` | count drop caught | self-test `1 failure(s) over 1862 assertions`, exit 1; floors `FAIL checklist observed=1862 floor=1863 self_test_failures=1`, exit 1, 149 s | confirmed (count floor) |
| C2 | Replace that arm with `rec(..., True, None)` (count preserved) | named arm visibly lost | self-test `1 failure(s) over 1863 assertions`; floors `FAIL checklist observed=1863 floor=1863 self_test_failures=1`, exit 1, 150 s | red only because the other arm is still red |
| C3 | Also replace `governance: LOG.md:2678 erratum is load-bearing` with a tautology | silent green should be impossible | self-test `0 failure(s) over 1863 assertions`, exit 0; floors `PASS checklist observed=1863 floor=1863`, exit 0, 147 s | **invariant gap**: named-arm identity is not enforced; count plus failure-count floor pass a tautology |

Gate-registry self-test on base: `0 failure(s) over 28 assertions`, exit 0. Base counter: `64 of 64; phantom 0`, exit 0.

## C2 baseline discrepancy (for L1)

- At base `47dbe87` the checklist self-test measures **2 failures over 1863** in the scratch clone (exit 1): both live-governance arms fail (`live round-65 corrections land` and `LOG.md:2678 erratum is load-bearing`).
- The committed before receipt (`.ufo/waves/round-82/receipts/before-checklist-selftest.txt`) records **1 failure over 1863**, taken against the fleet working tree (HEAD `006a834`, dirty `corpus/SOURCES.md`), not base `47dbe87`.
- Mechanism, derived: the live arms check corrections whose tokens are `../.ufo/...` relative to the repo's parent. The fleet's parent `/home/vgpnk/Projects/shokunin/.ufo/reports/round-60/kotoba.md` exists (checked, exit 0). The scratch clone's parent has no `.ufo` (checked, exit 2). Which exact token flips the second arm was not isolated.
- Consequence: the live arms depend on the checkout's parent directory, so "unchanged live governance must not change fixture results" is not met by the arms as written. The C2 repair must isolate both arms from live files, and its after-value must be measured at the declared base.

## Recommendations (not implemented; seat is leaf-only)

1. Registry gate: extend `judge_row` (or a companion check) to compare each verdict-map code's declared class against the script's observed exit mapping, or at least flag a numeric exit literal in `main` that is absent from the verdict map. Current check passes a verdict-map drift silently.
2. Universe: either document that `.js`/`.ts`/nested verifiers are out of scope in SKILL.md's registry section, or widen the universe. Currently an unregistered non-`.py`/`.sh` verifier passes.
3. Checklist invariant: the floor guard should also require the named arm set (e.g., a recorded list of arm names or a hash of arm bodies in `floors-registry.json`). Count plus failure count alone cannot detect the C3 tautology substitution.

## Mistakes

| Step | What happened | Correction |
|---|---|---|
| A3 | Renamed the flag without `dest=`; gate crashed on `args.self_test` | redone with `dest="self_test"`; the crash is reported as not a gate result |
| A3 counter | Ran the counter from the working tree (base code) with `--rev` of probeA; exit read 1 instead of 3 | re-ran from a clean `probeA` checkout; exit 3 recorded |
| Shell | Non-zero exits aborted the rest of multi-command calls; some exit records were lost | re-ran with `set +e`; all reported exits come from re-runs with files |
| Read cache | After the C1 cut, the read view showed a stale CUT-state line count | verified by `grep`, `wc -l`, `sha256sum`, `git diff`; disk matched base `b7d7…` |
| Commit | `commit --amend` rewrote probeA (scratch only) | recorded final revisions below |

## Hash and revision evidence

- Base checklist `verify_skill_checklist.py` sha256 `b7d7b0fca8be17cfa18e75fe4d130a0d429e34f5f4e1a30fdc5fb22a70539615`; base `check_gate_registry.py` `01b8ad1b1a2d9f7568dc6b970cd5c9ec621bf58af411973f001fa3ad0c35ddce`; base `SKILL.md` `fb448d66e007730b15e76f48ec76a0d946182e7b75e476314b556c75d282f57a`.
- Probe revisions (scratch, not for integration): probeA `dafe445a1259b138c80bfe73c7c1aad453c661cd`; probeB1 `92bcf8d50b1304b0e6e448238389dd3d951780d7`; probeB2 `1bea92cbcf678d9c60d2cf2180bee0ed2356efea`; probeB3 `5950619428fa08f1835a7eb28e14f86dd733661f`.
- C3 modified checklist sha256 `f3a103c8620e0c1395cac78e5d83c198046d8ff61f16c18620c90719865fd3e3` (diff `e1167257c0b97c05b923015e369bd01ef36932fe1a7b77d9c79ede5f39a19226`).
- Receipts and probe sources: `.ufo/waves/round-82/build/Kb82M04Registry-probes/` with `SHA256SUMS.txt`.

## Tooling and elapsed

- Tools installed or updated: none.
- Floor-guard runs: 149 s (C1), 150 s (C2), 147 s (C3); load was not sampled. Disk guard before work: status OK, `/fast` 47%.

## Verdict

Registry gate: a new unregistered `.py` verifier is rejected, a comment-only edit needs no row, and a renamed self-test flag is flagged. Gaps: verdict-map exit drift is unchecked; `.js`/nested verifiers escape the universe. Checklist: arm removal is caught by the count floor, but a tautology replacement that keeps count and clears failures passes silently. The C2 base baseline is 2 failures, not the receipt's 1, because the live arms depend on the parent directory.

VERDICT: registry gate rejects an unregistered `.py` verifier and flags a stale self-test flag; verdict-map drift and non-`.py`/`.sh`/nested verifiers escape; checklist floor catches arm removal but not a count-preserving tautology; C2 base measures 2 failures, not 1.

DELIVERABLES:
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/w1/Kb82M04Registry.md
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82M04Registry-probes/SHA256SUMS.txt

Report: .ufo/waves/round-82/w1/Kb82M04Registry.md
