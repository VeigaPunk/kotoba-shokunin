# MutDispatchInstrument — mutation test of `verifiers/verify_dispatch_prompts.py`

**VERDICT: HOLDS-BOUNDED** — applies to C2 (operability): the dispatch.04/dispatch.08 *conjunct execution* holds under every conjunct mutant (all seven are killed by **both** `--self-test` and `--box-proof`), and the committed fixture corpus really does discriminate all six named conjuncts. The bound: the **box-proof's own preconditions** (map delegates to this instrument, text hash equals the pinned hash, `exit 0 only when N == 2`) and the **completeness of the fixture corpus** are asserted by no committed detector — 6 code survivors and 2 fixture-coverage survivors below. Nothing landed is wrong; the evidence chain around it is thinner than the claim's wording ("A box counts only when the map delegates it to this instrument, its text hash equals the instrument's pinned hash, … exits 0 only when N is 2", `plans/round-49.md` § C2).

## Attacked

`verifiers/verify_dispatch_prompts.py` @ `c48793dbe5eb30cd661f42ecad7399ae94e3d7ad` (sha256 `512cff275e0d4e68ea3bb6b6df5ec877054309ee96b38e70f880167dbba90452`; lane checkout byte-identical). Private clone `/fast/scratch/hyaku/kotoba-r49/falsify/mut-dispatch-instrument/repo`, harness `…/harness.py`, raw results `…/results.json`. No subagents dispatched (leaf seat).

## Baseline (pristine bytes, in the clone)

| command | exit | output |
|---|---:|---|
| `python3 -B verifiers/verify_dispatch_prompts.py --self-test` | 0 | `0 failure(s) over 32 assertions` |
| `python3 -B verifiers/verify_dispatch_prompts.py --box-proof --map verifiers/checklist-baseline.json` | 0 | `boxes proven 2` |
| same, run in the lane checkout (read-only, `-B`) | 0 | `boxes proven 2` |

## Mutants — `--self-test` kill? `--box-proof` below 2?

| mutant | `--self-test` | `--box-proof` |
|---|---|---|
| M01 dispatch.04 placeholder scan disabled (`bad = []`) | **killed** (exit 1) | **killed** (`boxes proven 1`, exit 1) |
| M02 stem-equals-lane disabled (`wrong = []`) | **killed** (exit 1) | **killed** (`boxes proven 1`, exit 1) |
| M03 known-lane check disabled (`lane_kind` → always `sibling-lane`) | **killed** (exit 1) | **killed** (`boxes proven 1`, exit 1) |
| M04 dispatch.08 role-line comparison disabled (`elif False:`) | **killed** (exit 1) | **killed** (`boxes proven 1`, exit 1) |
| M05 dispatch.08 report-dir comparison disabled (`elif False:`) | **killed** (exit 1) | **killed** (`boxes proven 1`, exit 1) |
| M06 state comparison disabled (`if round_n <= value:` → `if True:`) | **killed** (exit 1) | **killed** (`boxes proven 1`, exit 1) |
| M07 `state-stale`/N/A returned as PASS | **killed** (exit 1, 3 assertions) | **killed** (`boxes proven 1`, exit 1) |
| M07a `state-stale` compared as a baseline (`return "baseline", 999999, …`) | **killed** (exit 1) | **SURVIVED** (`boxes proven 2`, exit 0) |
| M07b fleet-root-role stem-conjunct exemption removed (`elif False:`) | **SURVIVED** (exit 0) | **SURVIVED** (`boxes proven 2`, exit 0) |
| M08 `--box-proof` live pinned-hash check disabled (`if live.get(cid) != pinned:` → `if False:`) | **SURVIVED** (exit 0) | **SURVIVED** (`boxes proven 2`, exit 0) |
| M08b `--box-proof` map pinned-hash check disabled | **SURVIVED** (exit 0) | **SURVIVED** (`boxes proven 2`, exit 0) |
| M09 `--box-proof` map-delegation check disabled (`if entry.get("disposition") != want:` → `if False:`) | **SURVIVED** (exit 0) | **SURVIVED** (`boxes proven 2`, exit 0) |
| M10 exit rule `N == 2` weakened (`return 0 if proven == 2 else 1` → `return 0`) | **SURVIVED** (exit 0) | **SURVIVED** (`boxes proven 2`, exit 0) |

No surviving mutant changed the stdout either: "boxes proven 2" alone cannot see any of them.

## Survivors, and the input that exposes each

1. **M09 — map-delegation check (the plan's own falsifier class).** With the check disabled: `boxes proven 2`, exit 0. Exposing input: `verifiers/checklist-baseline.json`, `dispatch.08.disposition` → `delegated:verifiers/verify_corpus_integrity.py` (an **existing** file). Pristine: `boxes proven 1`, exit 1, stderr `map disposition is 'delegated:verifiers/verify_corpus_integrity.py', not 'delegated:verifiers/verify_dispatch_prompts.py'`; under M09 the same map prints `boxes proven 2`. The independent gate `python3 -B verifiers/verify_skill_checklist.py --json` reports `checklist.box_map_complete` **PASS** (`41 boxes mapped (8 executed, 2 delegated, 31 unexecuted)`), so no other committed gate sees the mis-delegation. (A *nonexistent* target is caught by that gate — `delegates to a target that does not exist` — an existing-but-wrong target is not.) This is exactly the class `plans/round-49.md` § C2 re-sizing says the old counter could not see.
2. **M08 / M08b — the two pinned-hash checks.** Disabling either changes nothing observable (`boxes proven 2`, exit 0). The matching damage *is* caught by an independent gate: rewording the dispatch.04 box in `SKILL.md` → `verify_skill_checklist.py --json` reports `checklist.box_map_complete` FAIL (`map entry dispatch.04 has no live box`); corrupting the map's `text_sha256` → same check FAIL. But the instrument's own pin has **no committed test**, and the pin is self-referential (`PINNED_BOX_SHA` lives in the same file as the check that reads it), so a coordinated edit (box text + map hash + the constant) leaves every gate green while `boxes proven 2` executes a different box.
3. **M10 — `exit 0 only when N == 2`.** No committed test exercises the failing branch, so the exit rule can be weakened invisibly. With the map damaged (`dispatch.08.text_sha256` → `0…0`) the mutant prints `boxes proven 1` **and exits 0**; pristine exits 1. The stdout half of the claim still fires; the exit-code half does not.
4. **M07b — the fleet-root-role exemption (survives both detectors).** No committed fixture exercises a fleet-root-role lane (no `<lane>-shokunin` repo but a state file). Live impact, same command `python3 -B verifiers/verify_dispatch_prompts.py --json` over `/home/vgpnk/Projects/shokunin/.ufo/prompts`: pristine dispatch.04 = 259 PASS / 6 FAIL / 22 N/A; under M07b = 280 PASS / 7 FAIL / 0 N/A. The extra FAIL is `aggregator-L1.md` — a **false** failure, because that prompt's report path is `.ufo/reports/round-1/AGGREGATE.md` (stem `AGGREGATE` ≠ lane `aggregator`) and the exemption is what keeps the aggregator lane out of scope. Load-bearing on live data, unverified.
5. **M07a — the `state-stale` branch.** `--self-test` kills it, `--box-proof` does not: the committed fixture corpus has no legacy-only-state case, so `boxes proven 2` is printed while the branch the box text names explicitly ("a lane with only the legacy `<id>.round` file … is reported `state-stale`, not compared") is silently compared instead.
6. **Fixture-coverage is not enforced (data mutant; strongest structural gap).** `box_proof()` iterates the cases that exist; it never checks that a must-fail case exists for each conjunct. Measured on `verifiers/fixtures/dispatch-prompts/manifest.json`: minus `d08-above-state` (the only must-fail for `round_le_latest_dispatched`) → `boxes proven 2`, exit 0; minus `d04-stem` (the only must-fail for `report_stem_is_lane_id`) → `boxes proven 2`, exit 0; **controls only, no must-fail fixture at all** → `boxes proven 2`, exit 0; M02 + manifest minus `d04-stem` → `boxes proven 2`, exit 0 (the stem conjunct is wholly unexercised); M06 + manifest minus `d08-above-state` → `boxes proven 2`, exit 0. The manifest's own `note` claims "one must-fail mutant per conjunct of dispatch.04 and dispatch.08"; no code checks that claim. `--self-test` still killed the two combined mutants, so the self-test is all that stands between a dropped fixture and a silently untested conjunct.

## Other evidence

* **No committed gate runs `--box-proof`.** `grep -rn "box-proof" --include="*.py" --include="*.sh" .` finds only prose (`SKILL.md`, `LOG.md`, `SCORECARD.md`, `corpus/lessons/round-49.md`, `plans/round-49.md`, the manifest note). `verifiers/check_assertion_floors.py` reruns only `--self-test` (row `dispatch_prompts`, floor 32, registry `verifiers/floors-registry.json`), so `--self-test` is the only always-on detector for this instrument and `--box-proof` is a manual command.
* **Live run, for context** (not part of the box-proof): `python3 -B verifiers/verify_dispatch_prompts.py --json` in the clone over the live fleet prompts → exit **1**; dispatch.04 FAIL (6 files: `kake-L1.md`, `kasegi-L1.md`, `kengaku-L1.md`, `kotoba-L1.md`, `kumitate-L1.md`, `protocol-L1.md`), dispatch.08 PASS (250 PASS / 29 N/A, 279 evaluated). The box-proof never touches the live corpus, so it cannot see those six failures — by design, per the plan ("its live failures are findings").
* **Restoration evidence.** After every mutant the file was rewritten with the exact pristine bytes: sha256 back to `512cff275e0d4e68ea3bb6b6df5ec877054309ee96b38e70f880167dbba90452` (`restored_exact: true` for 13/13 mutants, `…/results.json`). Fixture probes restored `manifest.json` (`af3783949ba01e7a3d0c5701caae26d7d56bb99e7e166fcb25d442090d79ee51`), `SKILL.md` (`fa6ffc29112b4ad1303874a1299bed538d650915a4f44656a5fcfde6c8d4f607`) and `checklist-baseline.json` (`049429aaefd85009f55871de0afc593a4e570f757885399cb0963c85e57063e6`); `git status --porcelain` in the clone is empty at `c48793dbe5eb30cd661f42ecad7399ae94e3d7ad`.
* **No tools installed** (none needed; stock `python3` only — no pacman/uv/npm transaction this seat).
* **Observation, not mine:** the lane checkout carries an unstaged edit to `verifiers/check_sibling_census.py` (mtime 2026-10-22 08:30:59, "round-49 falsify correction, seat CriticC1Landed"). This seat did not write it; my judged bytes are the commit, unaffected.

## What would close the bound (findings only — nothing changed here)

A committed test that (a) breaks the map's delegation to an existing-but-wrong target and demands `boxes proven < 2`; (b) rewording a pinned box and demanding `boxes proven < 2`; (c) demands a non-zero exit whenever `boxes proven N` with N ≠ 2; (d) requires one must-fail fixture per conjunct plus a legacy-state-stale case in the manifest; (e) exercises a fleet-root-role lane. Any of these turns the survivors above into kills.
