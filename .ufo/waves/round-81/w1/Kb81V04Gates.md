# Kb81V04Gates — no-harm battery / receipts audit (round 81, w1)

Axes: depth, consistency, calibration, operability, freshness. Scope: audit receipts and prose claims visible at 2026-10-28 02:44 UTC; no lane code edited. The wave was still in progress (51/64 w1 reports); I found no post-integration `after-final-*` receipts or completed C1 controls receipt.

## Findings by severity

### Blocker — no final C1 after-value receipts exist in the inspected wave state

At inspection, `.ufo/waves/round-81/receipts/` contained only `census-before.txt`, `freeze-shas.txt`, and `tipbattery-base-dot.txt`. No `after-final-dot.txt`, `after-final-abs.txt`, C1 controls result, or landed-tip battery receipt was present. Thus I cannot verify the frozen predicate at the landed tip or claim the requested no-harm checks passed. The plan requires both `--repo .` and absolute forms at the final tip; base-form evidence is not a substitute. The C1 control driver existed, but its only output receipts were `Kb81E06Controls-smoke.txt` and `smoke2.txt`, both run on base counter bytes, not the amended frozen counter. Do not score C1's after-value from these.

### High — freeze receipt omits the C2 counter pin, while C2 counter bytes continued changing

`receipts/freeze-shas.txt` freezes the C1 counter patch/post-image and the two corpus-instrument patch/blob identities, and records `LINE_CAP=900`; my independent `git apply` + `git hash-object` re-derivation matched its C1 counter blob `eb00200e…` and SHA256 `1753b11c…`, plus instrument blobs `bbee51f2…` and `59602942…`. But the plan's freeze requirement also names the new C2 counter SHA256; the receipt contains no C2 counter entry. During this audit, `build/check_sdk_allowed_tools.py` changed across observed hashes (`eb71aa23…`, then `739a7181…`), while `build/c2_controls.txt` declared the earlier `eb71aa23…` value. The C2 seat later said frozen-ready, but without a committed matching freeze record I cannot verify controls correspond to the final counter bytes. Freeze the final hash and re-run any dependent controls before using them as frozen evidence.

### High — E15 report claims 14 G1 battery receipts but only 4 gate/tip files are published

`build/Kb81E15Order.md` lines 43–44/731 claim the G1-only run produced 14 receipts, 10 green, 4 non-zero, 335 s; `build/Kb81E15Order/battery-content-group/index.txt` contains only its runner header and no per-receipt rows, and that directory held only files 01–04 at inspection. In particular receipts 05–14, which are needed to substantiate the six-gate/census claims, are absent. The report's stated summary is therefore not fully re-derivable from the published receipt set. Restore the complete receipt set or qualify the prose to the surviving evidence.

### Medium — base `verify_corpus_independent` does not have `report_dead=1`

Re-derived from E10's stamped base receipts `build/base-battery/06-corpus-integrity.txt` and `07-corpus-independent.txt`, and independently from E11's blocks 04/05 and K02's JSONs. E10 index: gate exits `0,0,0,1,1,0` = 4/6; its two tip receipts `01-tip-battery-dot.txt` and `02-tip-battery-abs.txt` both name full rev `b284223105f4d106f7e8f56ed4fd296c643cda0e`, print `guards 5 of 5; tip battery exit 0: 4 of 6`, and end `exit=1`. The integrity gate has five DRIFTs: tracked_files 155, unindexed 1, report_total 111, report_dead 1, commit_unresolvable 2. The independent gate has only two DRIFTs: unindexed 1 and commit_unresolvable 2; `report_dead` is observed 0/PASS. E11's independent re-run agrees exactly. Any report/plan prose attributing `report_dead 1` to both gates is unsupported; the base receipts explicitly show the disagreement.

### Medium — plan's literal sibling-census command exits 2; the runner does not run it

The plan § No-harm list writes `check_sibling_census.py --skill SKILL.md` and expects exit 0. I executed that exact command in the base clone: it emitted usage requiring positional `CENSUS.md`, exit 2. The plan's actual S06 receipts use explicit census paths and flags; the reusable `run-battery.sh` runs census validation but does not run `check_sibling_census.py`. The plan/runbook should use a runnable census argument (and specify `--province` if intended) and provide a receipt for that command. No green sibling-census verdict follows from the literal plan command.

## Re-derived supporting receipts

- `build/base-battery/index.txt`: 14 receipts, 10 exit 0 / 4 non-zero; the two battery forms are explicitly entries 01/02. JSON receipt figures end in `}` by the runner's `figure_of`, but their JSON bodies and `exit=` trailers contain the gate verdicts; I read the bodies directly.
- Base census: independently ran `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`; exit 0, 32 lines, 31 `W04` lines, byte-identical to `receipts/census-before.txt`.
- C2 controls: `build/c2_controls.txt` summary reports 8 worlds, 8 PASS, 0 DIVERGE/BUILD-ERROR; C0/C2/C4/N1 read 0/1 exit 1; C1/C3 refuse with exit 2; H1/R1 oracle worlds read 1/1 exit 0. These are control/oracle worlds, not the C2 landed after-value.
- C2 base receipts `Kb81E09C2Counter-base.txt` show both base forms 0/1, exit 1, rev b284223…; `Kb81E09C2Counter-selftest.txt` reports 0 failures over 135 assertions. Their exact counter bytes are not frozen by the current freeze receipt.
- S249 snapshot: 28,395 B, SHA256 `ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2`, agrees with `S249.manifest`, `S249.fetch.json`, and `Kb81S11GateQuotes-verify.json`.
- E05 final patch re-hash and fresh-base reapplication matched `freeze-shas.txt`; patch SHA `c15680f8…`, amended counter blob `eb00200e…`, SHA256 `1753b11c…`. Independently composed E01/E02 instrument hashes matched the frozen pins.

## Receipt metadata / uncovered prose

E10's 14 base-battery receipts are self-identifying: each has full `# rev=… cmd=… utc=…` and its own `exit=`. E11's 21-block independent receipt names the base rev in its report and command blocks, and its six primary gates have own exit trailers. By contrast, the legacy `receipts/tipbattery-base-dot.txt` has no `exit=` trailer (E10 correctly supplies an independent replacement), and auxiliary S06/E01 base probe outputs generally state the revision in their accompanying report rather than receipt headers. E15's G1 JSON and refresh receipts often identify only abbreviated scratch commit ids; these are fixture revisions, not the final lane tip. Keep those distinctions explicit.

The plan's declared E6 `LINE_CAP=140` was revised pre-freeze to 900, recorded in the freeze receipt and C04 report. The freeze records final measured arithmetic +402/−29 against the guard's base, within 900. This is not a 140-cap result; prose still describing the 140 cap or 60–120-line estimate must not be presented as the final frozen predicate.

Independent base runs in both counter forms were performed in `/fast/scratch/hyaku/kotoba-r81/Kb81V04Gates/clone`; each returned exit 1 and `guards 5 of 5; tip battery exit 0: 4 of 6`. Their outputs are published as `build/Kb81V04Gates-base-battery.txt` and `build/Kb81V04Gates-base-battery-abs.txt`. The scratch directory was removed. No tool installed or updated.

## Residual risk and verification gaps

No post-integration gate verdicts were available at inspection, and the C1 controls had not completed on the frozen counter. I did not claim any final battery, corpus-gate, baseline-refresh, report-pointer, sibling-census, or C2-after result. Re-run the missing final checks at the actual landed revision and capture each command's own exit code and exact measured rev before any final claim.

VERDICT: Base C1 calibration independently reproduced in both forms and matches E10; final C1/C2 after-values remain unverified, with missing frozen C2 hash, incomplete E15 receipts, and a non-runnable sibling-census command.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81V04Gates.md; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81V04Gates-base-battery.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81V04Gates-base-battery-abs.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81V04Gates-census-rerun.txt