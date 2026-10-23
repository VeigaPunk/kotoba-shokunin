Result: HOLDS — all five §9 conformance checks pass at the frozen plan commit a10240c0940f770a5f2a5f32a7e3c363dd5d40c0: one predicate per claim with identical sentence, exit condition and receipt label; controls and counters committed in the plan commit before any content; receipt-recorded counter sha256 values equal the committed counter bytes; none of the four control receipts meets its predicate; both claims name axis and surface.

Evidence below. All paths relative to the lane root /home/vgpnk/Projects/shokunin/kotoba-shokunin. Read-only seat: every git invocation was read-only (log, show, ls-tree, diff, merge-base --is-ancestor, branch --contains); no counters were executed (receipt-based; see Residual risk); no tooling installed or changed.

## 1. ONE predicate per claim; plan sentence = counter condition = receipt label

The plan declares the scheme in its heading: `## Claims — one frozen predicate each (plan sentence = counter condition = receipt label)` (plans/round-55.md:16). A grep for `Predicate (frozen)` over plans/round-55.md returns exactly two hits, lines 24 and 47 — one per claim; no second predicate sentence exists in the plan.

C1 (depth):
- Plan sentence: `python3 -B verifiers/check_explicit_invocation.py --rev <rev> --fetch` exits 0 iff it prints `explicit invocation forms found on the live page F of K; new ground G` with F ≥ 4 and G ≥ 2; receipt label `C1 predicate: --fetch exit 0 (F>=4, G>=2)` (plans/round-55.md:24-26).
- Counter condition: verifiers/check_explicit_invocation.py:529-530 prints exactly `explicit invocation forms found on the live page %d of %d; new ground %d` (found, len(backed), ground); with `--fetch` the counted value is F (`value = found`, line 535); the exit expression is line 536 `return 0 if value >= TARGET and ground >= NEW_TARGET else 1`, with `TARGET = 4` (line 93) and `NEW_TARGET = 2` (line 94). So exit 0 ⇔ F ≥ 4 ∧ G ≥ 2 — the same condition as the plan sentence. The docstring states the same predicate (lines 64-68: "Exit 0 iff the counted value (K, or F with --fetch) is at least TARGET (4) AND G is at least NEW_TARGET (2) … The declared C1 predicate is the `--fetch` form").
- Receipt label: `.ufo/waves/round-55/controls/C1-base.txt:14` and `C1-shortcut.txt:24` both carry `C1 predicate: --fetch exit 0 (F>=4, G>=2)` verbatim (followed by `— NOT MET by the … control`).

C2 (operability):
- Plan sentence: `python3 -B verifiers/check_could_not_evaluate.py --rev <rev>` exits 0 iff it prints `could-not-evaluate probes honoured 25 of 25; controls held 13 of 13`; receipt label `C2 predicate: exit 0 (25 of 25, 13 of 13)` (plans/round-55.md:47-49).
- Counter condition: verifiers/check_could_not_evaluate.py:236-237 prints exactly `could-not-evaluate probes honoured %d of %d; controls held %d of %d` with `N_PROBES = 25` (line 83) and `N_GATES = 13` (line 84); the exit expression is line 238 `return 0 if honoured == N_PROBES and held == N_GATES else 1`. The printed numbers are the same two counts the exit tests — identical condition to the plan sentence. Docstring states the same (lines 40-43).
- Receipt label: `.ufo/waves/round-55/controls/C2-base.txt:60` and `C2-shortcut.txt:58` both carry `C2 predicate: exit 0 (25 of 25, 13 of 13)` verbatim.

## 2. Controls and counters committed in the plan commit, before any content

`git -C . log --format='%H %cI %s' -- .ufo/waves/round-55/controls plans/round-55.md verifiers/check_explicit_invocation.py verifiers/check_could_not_evaluate.py` returns exactly one commit:

```
a10240c0940f770a5f2a5f32a7e3c363dd5d40c0 2026-10-22T20:11:10-03:00 round-55: plan, frozen C1/C2 counters and §9 control receipts (before data)
```

- Nothing before it (parent f0e5de82…, the round-54 spot-check) touches these paths; nothing after it exists: `git log -n 6` shows master tip = a10240c0 = the plan commit, so zero content commits (SKILL.md, corpus/, gate fixes) precede the controls — they cannot, the tip is the controls commit. Q28 satisfied.
- `git show --stat a10240c0` confirms the commit contains exactly 7 files: the four receipts (14/24/60/58 lines), plans/round-55.md (92 lines), and the two counters (540 + 242 lines), 1030 insertions, nothing else.
- `git ls-tree -r --name-only a10240c0 -- .ufo/waves/round-55/controls` lists exactly C1-base.txt, C1-shortcut.txt, C2-base.txt, C2-shortcut.txt — the do-nothing and shortcut receipts the plan § Controls names (plans/round-55.md:70,71,75,76).

## 3. Receipt-recorded counter sha256 equals committed counter bytes (Q24)

`git show a10240c0940f770a5f2a5f32a7e3c363dd5d40c0:<path> | sha256sum`:

- `verifiers/check_explicit_invocation.py` → `4fc6e01ad576531c95265c7dcd2440b0b2bda0cd3520a0b317c46cd78b3ff5e5` — equals the value recorded in C1-base.txt:1 and C1-shortcut.txt:1.
- `verifiers/check_could_not_evaluate.py` → `0c1258e2c282996a9ea1e5e5da2fa269cdb4c10f88a3ddc17da1f76c8ad56c3d` — equals the value recorded in C2-base.txt:1 and C2-shortcut.txt:1.

Working-tree drift check: `sha256sum` of both working-tree counter files returns the same two digests, and each of the four receipts plus plans/round-55.md hashes identically to its `git show a10240c0:` blob (e.g. plan b84b6c2f094782765c1575f962bc7b7352d48b32cfba65637c1d97991eeea202 both ways). What the seats see is what was frozen.

## 4. Neither control meets its predicate

- C1 do-nothing (`C1-base.txt`): summary `explicit invocation forms found on the live page 0 of 0; new ground 0` (line 10), `exit 1` (line 11). F=0 < 4 → predicate NOT MET; the receipt says so at line 14.
- C1 shortcut (`C1-shortcut.txt`): without `--fetch` it reaches `explicit invocation forms backed 7 of 7 clients; new ground 7`, `exit 0` (lines 11-12) — confirming the un-fetched form is gameable by fabricated data; with `--fetch`, the predicate form prints `explicit invocation forms found on the live page 0 of 7; new ground 0`, `exit 1` (lines 22-23) → NOT MET (line 24). The `--fetch` keying is load-bearing and the shortcut discriminates.
- C2 do-nothing (`C2-base.txt`): `could-not-evaluate probes honoured 13 of 25; controls held 13 of 13`, `exit 1` (lines 55-56) → NOT MET (line 60). Cross-check: the receipt's 12 MISS lines match the plan's twelve-miss list one-for-one — R+G box_proof_case_deletion.py, R+G check_mcp_instructions.py, R+R+G check_gate_finding_delta.py, R check_overlap_levers.py, R check_description_thresholds.py, G check_correction_sweep.py, G check_assertion_floors.py, G verify_corpus_independent.py (plans/round-55.md:52-56 vs receipt lines 4-54); 25 probes = 12 R + 13 G over 13 gates, matching the counter's GATES table (check_could_not_evaluate.py:66).
- C2 shortcut (`C2-shortcut.txt`): `could-not-evaluate probes honoured 25 of 25; controls held 0 of 13`, `exit 1` (lines 55-56) → NOT MET (line 58). The plan predicted held < 13 via the V control; the receipt shows all 13 V runs MISS and additionally 3 S runs MISS (alwayson_boxes, assertion_floors, verify_corpus_independent) — a stronger failure in the required direction; see Observation O3.

All four receipts carry the frozen label with `NOT MET`; none records an exit 0 on a predicate run.

## 5. Axes named by surface

- C1 — depth: plan header `**C1 — depth (lowest owned axis; the learning claim; the sourced claim). Surface: a new SKILL.md decision table …**` (plans/round-55.md:17-19); counter docstring line 1 `frozen counter for the round-55 C1 (depth) claim`; the counter reads only SKILL.md, corpus/knowledge/explicit-invocation-round55.md, corpus/SOURCES.md, corpus/lessons/round-55.md (constants at check_explicit_invocation.py:88-92). SCORECARD.md § axes has the depth row (SCORECARD.md:28); the plan's base scores cite the same table (`depth 9`).
- C2 — operability: plan `**C2 — operability. Surface: the could-not-evaluate error paths of thirteen registered gates under verifiers/**` (plans/round-55.md:44-46); counter docstring line 1 `frozen counter for the round-55 C2 (operability) claim`; the counter reads only exit codes of gate scripts (its runs list, lines 66-84). SCORECARD.md operability row (SCORECARD.md:31); plan base score 8.5.
- Causal separability is stated and holds: each counter reads only its own claim's surface (plans/round-55.md:59-63), and neither counter's inputs intersect the other's.

## Findings (observations; no defect in the frozen artifacts)

- O1 (minor, symmetry): the do-nothing receipts record the counters' self-test results (`self-test: 0 failure(s) over 29 assertions`, C1-base.txt:12-13; `…over 12 assertions`, C2-base.txt:58-59), the two shortcut receipts record none. The predicate does not require a self-test line in shortcut receipts; noting the asymmetry only.
- O2 (note, jj bookkeeping): `git log --all` on the counter paths also surfaces three anonymous off-branch heads from the same timestamp — 34f30e28 and 4abc5225 are tree-identical to a10240c0, and e1ebda74 is the same change minus the four receipts (diff name-status: only the four `D` lines). None is reachable from master; the frozen blobs are the plan-commit blobs (verified by hash in §3). Future audits that use `--all` should scope to master to avoid confusion.
- O3 (observation on the C2 shortcut stub): under the shortcut "exit 2 unless --self-test in argv", three gates' S controls returned 1 rather than 0 (C2-shortcut.txt lines for check_alwayson_boxes.py, check_assertion_floors.py, verify_corpus_independent.py). The receipt records this honestly and the control still fails the predicate (0 of 13 held, exit 1), which is the required direction; the stub's self-test arm on those three gates is simply stricter than the plan's description. No repair route needed — the receipt is data frozen at the plan commit.
- O4 (calibration): the C1 shortcut receipt demonstrates the no-fetch form passes (7 of 7, exit 0) on purely fabricated quotes, and the C2 do-nothing receipt shows S/V controls all hold (13 of 13) at base while 12 probes miss — so `controls held` cannot mask probe misses and vice versa. Both shortcuts discriminate in the right direction.

## Residual risk and verification gaps

- I did not re-execute either counter. This is a read-only seat and the five checks are static properties of frozen objects; the receipts byte-match the plan commit (§3), so re-running would only re-derive the same frozen evidence at real cost (C2 spawns 51 gate runs in temporary clones; C1 needs live network for `--fetch`). If the L1 wants a live re-derivation before judging, run both counters in a sandbox clone at a10240c0; exit expressions and printed sentences cited in §1 are what to compare against.
- The C1 `--fetch` predicate is fail-closed on network or decode errors (`found = False`, check_explicit_invocation.py:509-511): transient fetch loss fails the claim rather than passing it. Conservative direction, by design; a judging-time network outage would read as NOT MET, not as a counter fault.
- Gate probe expectations (which gate gets how many R probes, lines check_could_not_evaluate.py:66-84) were cross-checked arithmetically against the frozen receipts, not re-derived from the gate scripts themselves; the wave-2 diff-scope review of each changed gate is the plan's own trust boundary for that (Q33), and this seat does not duplicate it.
