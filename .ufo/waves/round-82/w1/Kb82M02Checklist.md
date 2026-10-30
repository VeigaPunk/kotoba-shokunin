# Kb82M02Checklist — mutation test of E03 replacement governance fixture

Seat: Kb82M02Checklist (leaf member, no subagents). Lane: round-82 C2 operability (hermetic checklist self-test). Base: `47dbe8781657de563ff867caca6244d28e3db504`.
Judged on: freshness, operability. No production after-values scored. No commits, pushes or jj mutation. No tool installs (none needed).

## Scope and setup

- Scratch clone: `/fast/scratch/hyaku/kotoba-r82/Kb82M02Checklist/clone` (`git clone --shared`, checkout base; toplevel asserted). Pristine `verifiers/verify_skill_checklist.py` sha256 `b7d7b0fca8be17cfa18e75fe4d130a0d429e34f5f4e1a30fdc5fb22a70539615`; clone copy unchanged after all runs (same sha).
- Mutants were applied to separate `cp -a` copies of the clone (`mut/M1`..`mut/M6`), never to the clone itself. Each copy's `git rev-parse --show-toplevel` asserted.
- Self-test command for every run: `python3 -B verifiers/verify_skill_checklist.py --self-test`, cwd = the copy, `TMPDIR` in scratch.
- Failing arm names below are taken from the raw self-test output files, not from any patch-author claim.

## Base control (unmutated, scratch clone)

`base-selftest.txt`: exit 1, `2 failure(s) over 1863 assertions`. Both reds are live-corpus arms:
- `governance: live round-65 corrections land, errata-excused`
- `governance: LOG.md:2678 erratum is load-bearing`

Environment note (not a mutant result): the clone has no fleet-root `.ufo/`, so `../.ufo/...` correction targets do not resolve from the scratch parent. The fleet before-receipt (`receipts/before-checklist-selftest.txt`) shows 1 failure over 1863 with a different detail. The live arms are red at base in both settings, so a live-arm red cannot count as a new kill. Fixture arms must do the killing.

## Mutants and independently observed results

Mutants are edits to the pristine file. Line numbers refer to pristine `b7d7...`. Full unified diffs: `build/Kb82M02Checklist.mutants.diff`.

| Mutant | Edit | Self-test result (observed) | Verdict |
|---|---|---|---|
| M1 remove correction check | L1791-1792: `cproblems, cexcused = [], set()` | `9 failure(s)`: 7 new fixture reds: `pinned correction excuses the named stale subject`, `correction past horizon`, `line drift`, `wording`, `no live red subject`, `correction never masks another dead subject`; and `correction for a restored token is stale` observed PASS (should be FAIL/stale). Plus the 2 base live reds. | KILLED |
| M2 lower corrections horizon | L425: `GOVERNANCE_CORRECTIONS_HORIZON = 2620` (was 2723) | `2 failure(s)`: identical arm names to base. Only the live arm's detail changed (row LOG.md:2621 now reported as "past horizon 2620"). No fixture arm changed. | SURVIVED (pass/fail count unchanged) |
| M3a restore absent file in never-masks arm | L2504: `unlink()` replaced by `write_text("")` for `corpus/gone.md` | `3 failure(s)`: new red `correction never masks another dead subject` (detail: `correction ... 'corpus/gone.md': stale, the old token now resolves`). | KILLED |
| M4a remove correction-excused subject filter | L1794-1795 replaced by `pass` | `3 failure(s)`: new red `governance: pinned correction excuses the named stale subject` (`corpus/gone.md does not resolve`, `1 recorded correction(s) excused`). | KILLED |
| M4b over-broad filter (`subjects = []`) | L1794-1795 replaced by `subjects = []` | `22 failure(s)`: 20 fixture arms red (e.g. `quoted/schematic exclusions pass non-vacuously`, `unquoted dead path fails and is named`, every erratum and correction arm) plus 2 live. | KILLED |
| M5 disable corrected-token replacement guard | L1744-1746 replaced by `elif False:` + unused body | `2 failure(s)` = base set. `correction corrected token dead fails closed` is still GREEN. | SURVIVED (fixture defect, see below) |
| M6 disable live-red subject guard | L1740 replaced by `elif False:` | `3 failure(s)`: new red `correction no live red subject fails closed` (`1 recorded correction(s) excused` for a non-matching row). | KILLED |

Expected-red arms, as specified:
- remove correction check: pinned-correction arm red — observed red.
- lower horizon: a horizon-load-bearing arm red — NOT observed; no fixture arm exists for the corrections horizon (the errata horizon has one, `governance: LOG.md:2678 erratum is load-bearing`, at self-test L2538; no corrections analogue).
- restore absent file: never-masks arm red — observed red.
- remove unrelated-dead filter: pinned-correction arm red (M4a) and never-masks/quoted arms red (M4b) — observed red. "Unrelated-dead filter" was interpreted as the post-correction subject filter (L1794-1795); both removal and over-broadening were run.
- disable replacement guard: `corrected token dead` arm red — NOT observed (see survivor analysis).
- live-red guard: `no live red subject` arm red — observed red.

## Survivor analysis

### M5 — `corrected token dead` arm cannot reach its guard (fixture defect)

The arm's notice line (self-test L2463-2466) reads `SCORECARD.md:9 token "corpus/gone.md" -> "corpus/live.md" (round-65 notice).` It does not contain the dead corrected token `corpus/absent-xyz.md`. The wording guard (`corrected not in text`, pristine L1738) therefore fires first, and the replacement guard (L1744) is unreachable from that fixture. The arm passes on the stale subject's own `does not resolve` text, so M5 and the pristine code give the same result.

Independent probe (`build/Kb82M02Checklist.probe-original-*.txt`), same row, same function:
- pristine: `status=FAIL`, detail `correction wording not on the line`.
- M5: `status=FAIL`, identical detail.

Repaired-fixture probe (`build/Kb82M02Checklist.probe_corrected2.py`, outputs `probe-repaired-*.txt`), with the notice line naming the dead corrected token `"corpus/absent-xyz.md"`:
- pristine: `status=FAIL`, detail `correction ... corrected token 'corpus/absent-xyz.md' does not resolve`.
- M5: `status=PASS evaluated=1 ... 1 recorded correction(s) excused`, so the arm goes RED under M5.

Proposed repair (NOT applied to the seat's tree and NOT verified inside the full self-test): give this arm its own notice line naming the dead corrected token, with its own `sha256` digest, and keep the existing notice for the other arms. That is a fixture-only change in `verify_skill_checklist.py` self-test. Full in-suite verification is for the main agent after integration.

### M2 — corrections horizon has no hermetic load-bearing arm

Lowering `GOVERNANCE_CORRECTIONS_HORIZON` changes only the live arm's detail. The live arm is already red at base, so the pass/fail count does not move. The repaired C2 requires fixture-only evidence; after the live arm is removed from the pass/fail set, nothing kills this mutant. Suggested fixture arm (analogue of L2528-2542): a hermetic repo with a correction row at line N and `corrections_horizon=N-1`, expecting `past horizon` in detail. Not implemented here.

## Mistakes (own work)

- First M5 edit used the wrong indent and introduced a syntax error (edit tool warned). Corrected via a second edit before any run; the verified mutant parses and its output is the one reported.
- Several bash batches returned empty output / exit 1 without running their commands. Re-ran each mutant as a single command and recorded the output files. M2's original exit code was not captured (rerun output used). The M1 exit code was not captured; the `9 failure(s)` line is observed. Counts above come from the output files, not from exit codes.

## Evidence (build artifacts)

Under `build/` with `Kb82M02Checklist.sha256.txt`:
- `Kb82M02Checklist.base-selftest.txt` sha256 `7e479816f56ddae680389767142be8af6ce9becfeac92e92bab84f8e57044c5e`
- `Kb82M02Checklist.M1.selftest.txt` `6163a2bc5876dedd1ed411fb8995579857bfde106839905c95799c7492215486`
- `Kb82M02Checklist.M2.selftest.txt` `5466c4c0ee59419833ac0ca4dcc2a3d6d551ab5d25a0debe0138da4ecab40d03`
- `Kb82M02Checklist.M3a.selftest.txt` `0fd3b60e2f589f6f1f2e6b2905c8a88e39c4e0a00e2afd7942fd67b6838e5486`
- `Kb82M02Checklist.M4a.selftest.txt` `ef878d42fb8312cea33720aec83c01145ba8cd0c5bf5ae89230c3a87cc4be7e9`
- `Kb82M02Checklist.M4b.selftest.txt` `2b805bc81b979c155729d152dd50716946f6441bee1ddb7eaf0376b40f26b50b`
- `Kb82M02Checklist.M5.selftest.txt` `0cabc3bc1c75f5d7122021a1c58fdcdf227e0aa4a3fc8d74cb8940fbc1c3d7a1`
- `Kb82M02Checklist.M6.selftest.txt` `2d92b62a270d685efbddd150a6854466ff004f4bfdbc2427fbdb27af351bc416`
- `Kb82M02Checklist.mutants.diff` `569c7dae6c39b70d34188c0af10aae15a6f526daa8d080e30e191f41a7f1bd8a`
- probes: `Kb82M02Checklist.probe-original-{pristine,M5}.txt`, `Kb82M02Checklist.probe-repaired-{pristine,M5}.txt`, `Kb82M02Checklist.probe_corrected2.py`

Pristine verifier sha256 (independent re-hash after all runs): `b7d7b0fca8be17cfa18e75fe4d130a0d429e34f5f4e1a30fdc5fb22a70539615`.

## Result

- Mutants: 7. Killed: 5 (M1, M3a, M4a, M4b, M6). Survived: 2 (M2 horizon; M5 replacement guard).
- Base C2 target (`0 failures`) is not reached by this seat; this seat only tests the fixture's discriminating power. Both survivors are fixture coverage gaps to fix before C2 can claim the replaced arms are load-bearing.
- Scratch deleted after receipts were copied (see final step).

VERDICT: MUTATION-PARTIAL — 5 of 7 mutants killed by named fixture arms; M5 (corrected-token guard) and M2 (corrections horizon) survive; fixture repair for M5 probe-validated only.

DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/w1/Kb82M02Checklist.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82M02Checklist.mutants.diff, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82M02Checklist.sha256.txt
