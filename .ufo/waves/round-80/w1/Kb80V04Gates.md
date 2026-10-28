# Kb80V04Gates — independent gate-green audit

Axes: depth, consistency, calibration, operability, freshness. Audit clone: `/fast/scratch/hyaku/kotoba-r80/Kb80V04Gates/clone`, independently cloned and checked out at base `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`; `rev-parse --show-toplevel` matched the clone. This was a separate clone, not a sibling's world.

## Findings by severity

### Blocker — C1 after-value unverifiable; required stack is not published

At inventory time, these required artifacts were absent from round-80 `build/`: `Kb80E01Registry.patch`, both `Kb80E05GrammarFix-*.patch` files, `Kb80E05GrammarFix.blobs`, `Kb80E06CounterErratum.patch`, and `Kb80E06CounterErratum.sha256`. Only `Kb80E06CounterErratum.cap60-provisional.py` existed; I did not substitute it for the finalized erratum. The final `receipts/freeze-shas.txt` was also absent. Without the frozen counter, final composed instrument pins, and both grammar changes, running the requested after-value would violate the freeze discipline and would not audit the landed stack. Therefore I did not claim any of the six final gates green, did not run either final battery form, and did not run the two corpus `--json` commands.

Calibration command, run directly in my base clone with the base counter bytes:

`cd /fast/scratch/hyaku/kotoba-r80/Kb80V04Gates/clone && python3 -B verifiers/check_tip_battery.py --rev HEAD --repo .`

Observed: `guards 5 of 5; tip battery exit 0: 1 of 6`; command exit 1. Breakdown: registry 1, floors 1, checklist 1, integrity 1, independent 1, correction sweep 0. Full command output and its own exit status are in `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80V04Gates-base-battery.txt`. This independently reproduces the base red anchor; it is not an after-value.

### Blocker — C2 counter prerequisites are not green/evaluable from the published bytes

My clone's `.ufo/waves/round-79/snapshots/` contains 18 files but no `MANIFEST.sha256`, although the C2 counter conjunct and coverage row name that file. The published `Kb80E08C2Entry-receipts.txt` reports the draft counter's S229/Microsoft Agent Framework quote `location_ok: false` (`quote lies in the first-heading block (Q70)`). I did not run the counter for an after-value: the published counter hash is `74e067cc…`, and the finalized freeze receipt/counter set was not present. C2's final `N of 6` and generator score are therefore not verified; the missing manifest and S229 receipt are concrete blockers, not a green result.

### High — the plan's named unresolvable citations do not match the base gate findings

Read-only base bytes at `corpus/SOURCES.md:171-172` contain the two actual unresolvable tokens: `7bb48f213ac677f943d5c791199ed3dddf302f00` on S230 and S231. The plan names Gemini/zed `owner/repo@<hex>` citations, but the base gate subjects are bare-hex `commit` citations. A grammar change limited to in-token `owner/repo@<hex>` cannot clear these findings. The C1 grammar patches were missing, so I could not verify that the published repair uses the plan's explicit-third-repository line-scope clause. The S05 audit/runbook evidence identifies an additional attribution problem: S230's pi-mono row associates this hash with the wrong repository, while S231's Mistral citation is consistent with the Mistral fetch record. A classification-only INFO rule must not be reported as validating that S230 attribution.

## Applied patch set and composition

In my clone I applied successfully: `Kb80E02Symlink.patch`, `Kb80E04DeadPointer.patch`, `Kb80S08ReadmeRows.patch`, `Kb80S09SkillRule.patch`, `Kb80S10Province.patch`, `Kb80S05SourcesEdits.patch`, and `Kb80E12Census-S232-S243.patch`. I copied the published `allowed-tools-surfaces-round80.md` and `check_allowed_tools.py` into their corresponding clone paths. The E04 instrument hash from my clone was `051b8c5f8676cba5c8d6047c8c9f7fcb56cd8f9f`, matching `Kb80E04DeadPointer.blob`.

`Kb80E03IndexBaseline.patch` is a duplicate rows-only alternative to S08: after S08's identical coverage rows were applied, `git apply --check` on E03 exited 1 (`patch failed: corpus/README.md:154`). I used S08's patch once, not both. The E03 runbook confirms the three rows are byte-identical and says its baseline-snapshot patch is a probe preview, not landable; it directs a clean-tree refresh after E04+E05. The published refresh script exists, but I did not run it because E05 and its required zero-mode repair were absent.

## Verification gaps and residual risk

- No final landed stack existed in `build/` during this audit; all after-values remain unverified. In particular, no direct exit captures exist here for the six final gates, two final corpus JSON reports, C2 counter, or either amended battery form.
- The S08 and E03 rows overlap; integration must select one, not apply both.
- The C2 snapshot manifest and the S229 quote-location issue remain unresolved in the available published bytes.
- My scratch clone was removed before handoff. No tool was installed or updated.

VERDICT: Base calibration independently reproduced; final C1 and C2 gate-green claims are unverifiable because the frozen repair stack and C2 prerequisites were not available.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/w1/Kb80V04Gates.md; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80V04Gates-base-battery.txt
