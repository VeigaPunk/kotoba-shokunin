# ReviewerBatterySelfTest — C1 patch review (round 94, wave r94-w1)

Status: COMPLETE — no blocking finding; recommendation to L1: land ExecBatterySelfTest.patch as-is.

## Scope
- Patch under review: `.ufo/waves/round-94/w1/ExecBatterySelfTest/ExecBatterySelfTest.patch` (builder ExecBatterySelfTest, owns `verifiers/check_mutation_battery.py`).
- Review against plans/round-94.md § C1, ANTI-SNIFFING (behaviour-only arms), FROZEN ANCHORS (byte-identical, declared multiplicity).

## Checklist
- [x] READY file seen; sha256 recorded (cbf44a34c6f99bf4ae3fb353c5e34fc34d4efc1567f67a1c3f29037991d04834).
- [x] Patch applies on a fresh scratch clone at edc731a91a956f6df20c27a74fb981b286f6ba58.
- [x] Only `verifiers/check_mutation_battery.py` touched (26 insertions, all in `self_test()`).
- [x] Frozen anchors byte-identical, multiplicity unchanged (1x pin call, 3x CNE print, 1x `return n == want, "observed`).
- [x] Each new arm observes behaviour (fixture run rc/output), never checker source text.
- [x] k1 killed — mutant applied by hand, failing assertion identified: the new working-tree-read arm.
- [x] k2 killed — the three new not-labelled arms.
- [x] k3 killed — the two new added-rows arms (live + rev path).
- [x] k0 positive still killed.
- [x] Module pin restored on every path (no new rebinding; existing `finally` covers all arms).
- [x] Manifest anchors matched once (mb-m2/mb-m15/mb-m16 each x1 on candidate).
- [x] round-93 `c1-killpin-rev.sh <cand-rev>` reads `C1-PREDICATE-MET` on candidate (drop world rc 2 names kill-set-size; other world rc 2 does not; honest world rc 0: `mutation battery killed 17 of 17 kill-set; equivalents survived 6 of 6`).
- [x] Frozen counter `selftest-kills.py c1 <cand-rev> $D` → `C1-PREDICATE-MET`, rc 0: `C1 targets killed 3 of 3; positive killed 1 of 1; honest rc 0; decoys held 3 of 3` (per-mutant failure counts 1/3/2/4 match my by-hand runs exactly).
- [x] No-harm: honest world of the round-93 gate runs the full battery `--rev` on the candidate → 17/17 kills, 6/6 equivalents, rc 0 (manifest anchors hold in-world, not only by count). Tip axis A/B (identical invocation `--repo $D`): base edc731a and candidate 3004f36 both read `guards 5 of 5; tip battery exit 0: 2 of 6` (rc 1, carried reds; `check_assertion_floors.py` times out at 280 s inside this sandbox at BOTH revs) → candidate reading == base reading, no C1 effect. The plan's parenthetical "3 of 6" is a different-invocation number, not a patch regression.

## Findings

### Blocking
(none so far)

### Non-blocking
1. Plan-vs-invocation number: plans/round-94.md's no-harm line says the tip battery reads "3 of 6" at base; under my sandboxed invocation (`--repo <scratch clone>`, HYAKU_SCRATCH under /fast) BOTH base edc731a and candidate read "2 of 6" — `check_assertion_floors.py` hits the 280 s gate timeout inside this sandbox at both revs (wall 280.1 s of a 338 s run). Base == candidate, so this is not a C1 effect; flagging only so the L1 landing reading is taken with the plan's own invocation shape and not compared against my sandboxed 2-of-6.
2. Residual (not a frozen target): k2 substitutes all three `print("could-not-evaluate: %s" % exc)` sites at once, and the new arms kill via main()'s CouldNotEvaluate print (x2 arms) and run_evaluate's print (x1 arm); main()'s OSError print has no dedicated "not labelled" arm. A future mutant labelling ONLY the OSError print would survive — out of the frozen claim's scope, noted for a later round.
3. The k1 arm proves the committed-bytes direction (dirty tree with a dropped row still exits 0). Any working-tree dependence of the pin read flips it, so the single direction suffices; no gap found.

## Verdict

**No blocking finding.** The C1 patch (sha256 cbf44a34c6f99bf4ae3fb353c5e34fc34d4efc1567f67a1c3f29037991d04834) meets § C1 as reviewed: behaviour-only arms, k1/k2/k3 killed by exactly the new arms for the stated reasons, positive k0 still killed, honest 38/38 green, frozen anchors and manifest anchors intact, production code unchanged, module pin restored on every path, round-93 gate MET, frozen counter `C1-PREDICATE-MET` rc 0 with decoys 3-of-3 held. Recommendation to L1: land as-is. (This verdict is a recommendation, not an admission.)

## Evidence (commands → observed lines)

- `sha256sum ExecBatterySelfTest.patch` → `cbf44a34…04834` (== READY trailer).
- Fresh clone at edc731a + `git apply --check` → OK; clone removed.
- `git apply` in my clone; scratch commit `3004f36379028902d624bdf3ac852d38e75a971a` (identity scratch <scratch@invalid>); `git rev-parse --show-toplevel` == the clone; tree clean.
- `git diff --stat edc731a..HEAD` → `1 file changed, 26 insertions(+)` (only check_mutation_battery.py; all hunks in self_test()).
- Anchor counts on candidate: k1 anchor 1, k2 anchor 3, k3 anchor 1; mb-m2/mb-m15/mb-m16 edit anchors 1 each.
- Honest self-test at candidate → `0 failure(s) over 38 assertions`, rc 0.
- By-hand mutants in the working tree (restored byte-exact after each): k1 rc 1 (1 failure — the new k1 arm), k2 rc 1 (3 failures — the three new k2 arms), k3 rc 1 (2 failures — the two new k3 arms), k0 rc 1 (4 failures incl. both pre-existing drop arms).
- Frozen counter: `python3 -B verifiers/fixtures/round-94/selftest-kills.py c1 3004f36379028902d624bdf3ac852d38e75a971a $D` (HYAKU_SCRATCH=my scratch) → honest rc 0 `0 failure(s) over 38 assertions`; k1 rc 1 KILLED (1 failure); k2 rc 1 KILLED (3); k3 rc 1 KILLED (2); k0 rc 1 KILLED (4); decoys k1/k2/k3 rc 0 HELD; `C1 targets killed 3 of 3; positive killed 1 of 1; honest rc 0; decoys held 3 of 3`; `C1-PREDICATE-MET`; rc 0.
- `bash verifiers/fixtures/round-93/c1-killpin-rev.sh 3004f36… $D` → drop world rc 2 names kill-set-size yes; other world rc 2 names kill-set-size no; honest world rc 0 `mutation battery killed 17 of 17 kill-set; equivalents survived 6 of 6; disclosed survivors 0 of 0`; `C1-PREDICATE-MET`; rc 0.
- Tip battery A/B (`--repo $D`): base edc731a → `guards 5 of 5; tip battery exit 0: 2 of 6`, rc 1 (assertion_floors timeout 280 s); candidate 3004f36 → identical tally and per-gate lines.


## Patch review (static)

- READY seen at poll iteration 8 (~16 min). READY sha256 matches the patch file: `cbf44a34c6f99bf4ae3fb353c5e34fc34d4efc1567f67a1c3f29037991d04834`; READY claim "31 -> 38 assertions" matches observed (+7 `t.check` calls).
- `git apply --check` on a SECOND fresh clone at edc731a passed; that clone removed.
- Diff: `1 file changed, 26 insertions(+)` — only `verifiers/check_mutation_battery.py`; all four hunks inside `self_test()`; `evaluate()`, `main()`, `materialize()`, `kill_set_check()`, `parse_manifest()` untouched → production behaviour unchanged.
- Frozen anchors on candidate 3004f36379028902d624bdf3ac852d38e75a971a: `ok_pin, pin_detail = kill_set_check(committed, pinned)` x1; `print("could-not-evaluate: %s" % exc)` x3; `return n == want, "observed` x1 — all byte-identical, no new occurrence (the patch adds no line containing any anchor).
- Manifest anchors mb-m2 / mb-m15 / mb-m16 each still match exactly once on the candidate.
- Anti-sniffing: every new arm observes behaviour — `run_main`/`run_evaluate` rc+output on committed fixture worlds, `kill_set_check` on manifest TEXTS (live manifest, appended-row copy, unparseable text), and one `git status --porcelain` precondition on a fixture. No arm reads the checker's own source. The new arms are consistent with the pre-existing round-93 arm conventions (`run_evaluate(..., pinned)` rev-path arms, live `kill_set_check` arms).
- Module pin: no new `KILL_SET_PINNED` rebinding; new arms pass `module_pin` / explicit `pinned` captured before the `try`; the existing `finally: KILL_SET_PINNED = module_pin` still restores on every path (also on exceptions).

## Mutant kill channels (each mutant applied by hand in the candidate clone working tree, self-test run, byte-exact restoration verified by clean `git status`)

- k1-worktree-manifest → rc 1, `1 failure(s) over 38 assertions`, FAIL: `k1 working-tree read: a kill row dropped in the working tree only exits 0 (committed bytes govern) without kill-set-size` — output shows the mutant read the dirty working-tree manifest (`could-not-evaluate: arm kill-set-size: manifest at 7e04cb5b0998 has observed 8 kill rows, p[inned 9]`).
- k2-label-every-cne → rc 1, `3 failure(s) over 38 assertions`, all three new k2 arms (G1 short-rev refusal, G1 commit-check refusal, rev-path anchor miss) — every `could-not-evaluate:` line gains the `arm kill-set-size:` label.
- k3-accept-added-rows → rc 1, `2 failure(s) over 38 assertions`: live-append arm (`observed 18 kill rows, pinned 17` no longer refused) + rev-path added-rows arm (pin passes, battery proceeds to `rc 0` instead of `rc 2 naming kill-set-size`).
- k0-accept-any (positive) → rc 1, `4 failure(s)`: the two pre-existing drop arms plus the two new k3 arms.
- No pre-existing assertion fails under k1/k2/k3 — the new arms are the kill channels and nothing regressed.

## Honest run on candidate

- `python3 -B verifiers/check_mutation_battery.py --self-test` at 3004f363: `0 failure(s) over 38 assertions`, rc 0.


## Preparation (before patch landed)

- Read plans/round-94.md in full; read frozen counter `verifiers/fixtures/round-94/selftest-kills.py` in full (CLAIMS["c1"]: k1 anchor `ok_pin, pin_detail = kill_set_check(committed, pinned)` x1; k2 anchor `print("could-not-evaluate: %s" % exc)` x3; k3 anchor `return n == want, "observed` x1; positive k0 `return True, "observed`).
- Scratch clone created per recipe: `/fast/scratch/hyaku/kotoba-r94/ReviewerBatterySelfTest/repo` at edc731a91a956f6df20c27a74fb981b286f6ba58; `git rev-parse --show-toplevel` == the clone.
- Baseline instrument understood: 31 self-test assertions; `evaluate()` reads the manifest via `git_show(lane, rev, MANIFEST)` into `committed` and pins via `kill_set_check(committed, pinned)`; `materialize()` enforces clean scratch clone; `run_evaluate` (self-test helper) prints `could-not-evaluate: %s` (3 occurrences of that literal in the file: main() x2, run_evaluate x1).
- Gap analysis at base (why k1/k2/k3 survive): every rev-path fixture arm commits the manifest it probes (working tree == HEAD for the manifest; the `dirty` arm poisons only the FG stub), so k1's working-tree read is observationally identical; CNE-output assertions are substring checks (`"G1" in out`, `"anchor miss" in out`) so k2's added label passes; no arm evaluates a committed manifest with count ABOVE its pin, so `n >= want` passes every arm.
- My clone's honest self-test at edc731a: `0 failure(s) over 31 assertions`, rc 0, 4.3 s (TMPDIR/HYAKU_SCRATCH pointed at my scratch dir).
- Pre-data receipts copied to `w1/ReviewerBatterySelfTest/`: redbefore-c1-base.txt (targets killed 0 of 3; positive killed 1 of 1; decoys held 3 of 3; UNMET rc 1), forgery-c1-run.txt (source-sniffer killed targets 3 of 3 but decoys held 0 of 3 → UNMET via decoy guard), census-before.txt.
- Manifest coupling noted: `verifiers/fixtures/mutation-battery/manifest.tsv` rows mb-m2, mb-m15, mb-m16 anchor on check_mutation_battery.py bytes (G1 commit-check, G1 clean-tree, G2 restore) — each must still match exactly once on the candidate; the round-93 `c1-killpin-rev.sh` gate builds drop/other/honest worlds from a candidate rev.

