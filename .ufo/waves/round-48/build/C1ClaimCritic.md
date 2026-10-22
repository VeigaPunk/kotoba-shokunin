# C1ClaimCritic — round 48 (attempt 2) C1 framing attack

Seat: `KotobaR48.C1ClaimCritic` (leaf critic, read-only on the lane; no delegation). Lane base `75f671b109d8eddd0d64c1429bd6379fe577175a`; candidate `26035dcec54d8e42f3a8b47ae8ca551c18aec295` (consumer sha256 `2d824c0b…`). Scratch: `/fast/scratch/hyaku/kotoba-r48-a2/seats/C1ClaimCritic/`. Disclosure: as a critic, not a blind builder, I read `verifiers/verify_harness_claims.py` (the producer), lines 257-277 and 457-509. Nothing from it went into any candidate code.

## Verdict

**No. Configured-root enumeration does not repair routed defect 1, not even "half" of it.** It is a real, bounded fix to one input class in the independent instrument's `oc.roots.names_plus_builtin` row, which is the same row behind defect 1. It does not touch the join definition, which is what defect 1 is about. The plan's heading ("repair routed defect 1 … configured-root half") is false provenance and has to be reworded. The measured after-value is close to sizing-compliant but needs three fixes, listed below.

## Findings

**F1 — Defect 1 has no configured-root half (provenance, fixable).** Defect 1 asks for three things: resolve the independent join definition, freeze a new carrier/toolchain prospectively, and preserve the 21/24 and 20/24 evidence. Round-47's falsify seat isolated the 21/24 → 20/24 delta to exactly one cause. The row `oc.roots.names_plus_builtin` went from live 10 to 11 because the producer's `OC_BIN` now reaches the npx ELF, which carries the `customize-opencode` marker, while the independent side keeps built-ins at 0 by declaration (`.ufo/waves/round-47/falsify/W2DepthNoHarm.md` §3.2–3.4: a 2×2 code×binary matrix, and reverting the constant gives back 21/24). Configured roots are not part of that delta. On this host neither `~/.config/opencode/skill` nor `~/.config/opencode/skills` exists, and the live row reads **10 under both base and candidate, with all 28 values identical**. So the frozen-carrier live join reads exactly what round 47 measured. Against each part of defect 1:
- *Join definition:* untouched. The built-in marker versus 0-by-declaration split stays open, and the plan says so.
- *New carrier/toolchain frozen prospectively:* partly addressed as a method only. The oracle `1d09a38c…` and ruler `01af33a6…` were frozen before the BASE observation (`.ufo/round-48/instrument.json`). However, they are a synthetic, independent-only matrix: no producer, no comparator, no opencode binary, and an empty catalogue carrier. They are not a join carrier or toolchain.
- *Preserve 21/24 and 20/24:* met by not touching the evidence. `W2DepthNoHarm.md` and `C1HarnessDriftRoot.md` are still tracked at the base.

**F2 — Strongest counterexample: the fix can fake a defect-1 "repair" by coincidence (a tradeoff the judge must not credit).** The producer counts direct children of `~/.agents/skills`, `~/.config/opencode/skills` (plural only) and `~/.claude/skills`, then adds 1 when the binary has the marker. The candidate now also counts the singular `skill/` root. One unlogged singular-root skill therefore cancels the built-in +1, and the row "agrees" while both definitional gaps are still there. Measured row-level probe (`join_probe.py`, exit 0):

| case | producer | independent base | independent candidate | join base → candidate |
|---|---|---|---|---|
| no config roots, marker | 3 | 2 | 2 | disagree → disagree |
| unlogged `skill/zeta`, marker | 3 | 2 | **3** | disagree → **agree (coincidence)** |
| unlogged `skills/zeta`, marker | 4 | 2 | 3 | disagree → disagree |
| unlogged `skill/zeta`, no marker | 2 | 2 | 3 | **agree → disagree (new red)** |
| unlogged `skills/zeta`, no marker | 3 | 2 | 3 | disagree → agree (real convergence) |
| nested `skills/group/eta`, marker | 3 | 2 | 2 | disagree → disagree |

The candidate matches upstream better than the producer does, because upstream scans both `{skill,skills}`. So this is a tradeoff, not a defect in the candidate. Still, a future live 21/24 on a host with a singular root would be laundering in exactly the shape the spot-check forbids ("Do not force 21/24 …"). The SCORECARD row has to name this hazard.

**F3 — Recursive loader parity is open, and it is broader than recursion (scope, stated).** I opened the pinned upstream loader myself. Configured directories are scanned with `{skill,skills}/**/SKILL.md`, which is recursive. `cfg.skills.paths` (from `opencode.json`) is scanned with `**/SKILL.md`. Pulled `skills.urls` directories are scanned too. `config.directories()` returns more than the single `--oc-config`. The candidate enumerates direct children of one config root only, and it uses directory names for the config roots but frontmatter-or-directory names for the agents root. The nested case above stays at 2 where upstream-faithful counting would give 3. `instrument.json` already lists recursive parity, name identity and readable-file discrimination as unproved, so the claim is honest only if the wording keeps all of them, plus `skills.paths`/urls and multiple config directories, out of scope.

**F4 — Q05 is unmet at the candidate (fixable).** Both clones' `--self-test` print `0 failure(s) over 104 assertions`, exit 0. The candidate diff touches only the derive block (13 insertions, 8 deletions). The plan requires the fix to ship its own regression arm. When that arm lands:
- the consumer sha256 changes from `2d824c0b…`, so the L1 pre-run (`ruler-l1-01.json`, verdict clean, sha256 `536b3687…`) does not measure the landed bytes and must be re-run;
- `verifiers/floors-registry.json` `harness_independent` floor 104 must be bumped in step under its BUMP-IN-STEP rule.

A good arm is an unlogged singular root plus an unlogged plural root in a fixture, with the target row asserted. That arm should fail on BASE.

**F5 — After-value sizing: close, but three gaps (fixable).**
- *One value:* the plan lists four conjuncts (verdict clean, 0 target failures, 0 behavioral mismatches, exit 0). In the ruler they are one predicate, so declare one value: **ruler exit 0, target failures 5 → 0**, with the other conjuncts as receipt fields.
- *One command over committed bytes:* the consumer comes from `git show <revision>:…` and is hash-checked, and the oracle and baseline are hash-checked. The ruler itself is run from a working-tree path and is never hash-checked by its own invocation. Its bytes match the committed `01af33a6…` today, but the command does not guarantee that. Either run it as `python3 -B <(git -C <lane> show <landed>:.ufo/round-48/tools/config-root-ruler.py) …` or pair it with `git show <landed>:.ufo/round-48/tools/config-root-ruler.py | sha256sum` = `01af33a6…`. The placeholders `<landed>` and `<sha of landed consumer>` must become literals in SCORECARD.
- *No universal clause:* "0 behavioral mismatches" is enumerated over 13 synthetic cases × 27 non-target values × 28 statuses, which is fine within that set. It must not be written as "no harm" or as "preserves the join". The ruler never runs the producer or the comparator.

**F6 — Lane observation (not my change).** The lane working copy has an uncommitted `verifiers/verify_harness_independent.py` equal to the candidate bytes (`2d824c0b…`), while HEAD has `872993f8…`. Whoever owns integration should know about it before measuring `<landed>`.

## Impacted axes
- **Depth** (owned): real but bounded coverage gain. No score move is justified, because the defect-1 join is unchanged.
- **Calibration**: the claim heading overstates provenance (F1). SCORECARD has to state what is still open.
- **Consistency / no-harm**: there is a new coincidental-agreement path and a new red on singular-root hosts without the marker (F2). Neither appears on this host today.

## Smallest safe correction
1. Rename C1 to "narrow the configured-root input gap in `oc.roots.names_plus_builtin` (the row behind routed defect 1); defect 1 stays open and routed".
2. Land the Q05 arm and the floor bump, then re-run the ruler on the landed commit with the literal consumer sha and a hash-pinned ruler.
3. Carry defect 1 forward unchanged, adding the F2 hazard: any future agreement on this row has to be checked against singular-root counts before it is read as a definitional resolution.

## Proposed SCORECARD wording (depth row, round 48)

> **round 48 (C1 — improved-bounded; depth holds 9):** the independent instrument's `oc.roots.names_plus_builtin` also enumerates direct-child `SKILL.md` directories under `--oc-config/skill` and `--oc-config/skills` when the opencode log does not name them, as a set union with the log roots and the agents root. On the frozen 13-case synthetic oracle `1d09a38c…` with ruler `01af33a6…`, target failures went 5 → 0 and ruler exit 1 → 0, with 0 non-target value or status changes, at `<landed>` (consumer `<sha256>`; before receipt `8bec447a…` at `197b5a4`). This narrows one input-class gap in the row the round-47 spot-check routed as defect 1. **It does not resolve defect 1.** Built-ins stay 0 by declaration while the producer counts the `customize-opencode` marker. This host has neither configured root, so the row's live value is 10 before and after, and the round-47 frozen-carrier evidence (21/24 base, 20/24 tip; `.ufo/waves/round-47/falsify/W2DepthNoHarm.md`) stands unchanged. Not claimed: recursive `{skill,skills}/**` parity, `skills.paths`/`skills.urls`, multiple config directories, frontmatter-name identity, any live-join or no-harm result. Known hazard: the producer counts only the plural configured root, so an unlogged singular-root skill can now cancel the built-in +1 and make this row agree by coincidence. Such an agreement is not a defect-1 repair.

## Evidence

| Command (cwd = seat scratch unless noted) | Exit | Result |
|---|---|---|
| `git clone -q <lane> lane`; `git clone -q …/cand cand && git -C cand checkout -q 26035dc…` | 0 | lane HEAD `75f671b…`; cand `26035dc…` |
| `sha256sum {lane,cand}/verifiers/verify_harness_independent.py` | 0 | `872993f8…` / `2d824c0b…`; producer `d9d9eb66…` in both |
| `git -C cand diff --stat 75f671b 26035dc` | 0 | 1 file, +13/−8 (derive only) |
| `ls ~/.config/opencode/{skill,skills}` | 2 each | ENOENT |
| `python3 -B {lane,cand}/verifiers/verify_harness_independent.py --json --catalogue-carrier empty-carrier` | 0, 0 | target 10 / 10; differing ids `[]` |
| `python3 -B {lane,cand}/verifiers/verify_harness_independent.py --self-test` | 0, 0 | `0 failure(s) over 104 assertions` in both |
| `python3 -B join_probe.py > probe-result.json` | 0 | table in F2; probe `04cfd754…`, result `08aa076e…` |
| `git show 75f671b:.ufo/round-48/tools/config-root-ruler.py \| sha256sum` | 0 | `01af33a6…` = working tree = `instrument.json` pin |
| `git show 75f671b:.ufo/round-48/verification/before-configured-root.json \| sha256sum` | 0 | `8bec447a…` (matches plan) |
| read `/fast/scratch/hyaku/kotoba-r48-a2/ruler-l1-01.json` (sha256 `536b3687…`) | — | verdict clean, settled 13, target_failures `[]`, mismatches `[]` |

Web source, opened by this seat. I fetched it only and did not execute it: `https://raw.githubusercontent.com/anomalyco/opencode/e3c4eb242585dcd77be1a867391b7c25fd47ce52/packages/opencode/src/skill/index.ts`, accessed 2026-10-22T08:14:11Z, `curl` exit 0, sha256 `91dce57f590e1ad3103e0555b893500e098a95cde2739422b699233889b205e6`.
- Line 24: `const OPENCODE_SKILL_PATTERN = "{skill,skills}/**/SKILL.md"`
- Lines 205–207: `const configDirs = yield* config.directories()` … `yield* scan(state, dir, OPENCODE_SKILL_PATTERN)`
- Lines 211 and 219: `for (const item of cfg.skills?.paths ?? [])` … `yield* scan(state, dir, SKILL_PATTERN)` (`SKILL_PATTERN = "**/SKILL.md"`, line 25)

Lane sources cited: `corpus/lessons/round-47-verifier-spotcheck.md:39,70`; `.ufo/waves/round-47/falsify/W2DepthNoHarm.md` §3.2–3.4; `verifiers/verify_harness_claims.py:472-479,504`; `verifiers/verify_harness_independent.py:592-623` (candidate); `.ufo/round-48/instrument.json` `outside_review_delta.unproved_limits`; `scripts/hyaku/lane-addendum.md:202-209` (claim sizing).

Tooling: nothing installed or upgraded (stock `python3`, `git`, `curl`, `rg`). No pacman transaction. No VCS write in the lane or the fleet repo. The only lane write is this report.
