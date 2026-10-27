# F24ChecktationTestSkill — r77 w2

Lane HEAD: `6523aced1ee0ebe07dca996213bdc645a6acbd1e`. The worktree has only the freeze commit; claim data is not committed. `corpus/SOURCES.md` S213 still has only `corpus/knowledge/skill-eval-artefacts-round70.md`. No lane files were changed. Scratch clone was at `/fast/scratch/hyaku/kotoba-r77/F24Mutation-TestSkill-Evals/clone`, configured as prescribed, verified top-level, restored to HEAD with `status_count=0`, then removed. No tools installed.

## Frozen counters at HEAD

Pinned hashes match plan: `check_desc_craft.py` `cf3c45d9e3985f11889816f4bb371dc0d5541c10c09ce2ab3966a4bff4603b9e`; `check_r75_routed_repairs.py` `989203c40e1aab55fc14ee1d444dd4fa8b49fe01144b2dcdeaa6a27fa39f4a63`.

Commands/results (exit is gate's own exit):
- `python3 -B verifiers/check_desc_craft.py --repo . --rev 6523aced1ee0ebe07dca996213bdc645a6acbd1e` → `description craft backed 0 of 6`, exit 1.
- `python3 -B verifiers/check_r75_routed_repairs.py --repo . --rev 6523aced1ee0ebe07dca996213bdc645a6acbd1e --work /fast/scratch/hyaku/kotoba-r77/F24Mutation-TestSkill-Evals/work` → `r75 routed repairs closed 0 of 4`, exit 1 (R1–R4 open).

## Assigned skill-evals used-by arm

At pristine HEAD, `python3 -B verifiers/check_skill_evals_v2.py --repo . --rev 6523aced1ee0ebe07dca996213bdc645a6acbd1e` → `skill eval artefacts verified 2 of 10`, exit 1. It has no used-by finding at pristine HEAD; its red is the SKILL-line finding. The gate self-test passes: `self-test: 0 failure(s)`, exit 0.

Scratch committed worlds:
- World A `c8da07a53d9a1120a3ffa896921d930aea3f238b`: S213 used-by appended with exact second member `corpus/knowledge/description-craft-round76.md` plus a fixture stub. v2 emits no used-by finding; red remains the unrelated SKILL-line finding, exit 1. C1(e) advances to “round-76.md is not committed” (membership passed, lesson absent).
- World B `f8701cff4283a13c7fcee20a8877433195e402de`: S213 used-by changed to r70 path `.bak`. v2 reports `F7: S213 used-by lacks exact member ...` and A10 census failure, exit 1. C1(e) reports the description-craft path is not listed.
- World C `e6efe5e5d9561654e876c25f8095766d077b3fcc`: only description-craft path, stub exists. v2 reports F7 exact-member failure while census passes, exit 1. C1(e) passes membership and advances to missing lesson.

Mutation controls on v2 arm (SELF_SHA recomputed for each scratch mutation): arm disabled → self-test failed on substring junk (`10/10`, no finding), exit 1; exact-member weakened to substring → same kill, exit 1; delimiter changed comma→semicolon → multi-member positive self-test failed `9 of 10`, exit 1. Mutant removing `.strip()` **survived** self-test (`0 failure(s)`, exit 0): fixtures put the required path first and do not test whitespace around a later member. Live W-B with disabled/substring mutant no longer emitted F7, but A10 still caught the nonexistent path. Restored pristine gate hash at cleanup: `d4df34cf48ba11cc6631cd1e7ef24334b634f92d1e8b54fcd6368b39e4224bfb`; restored HEAD and clean status confirmed before scratch removal.

## Separate no-harm blocker

The r77 plan requires live `check_skill_evals_v2.py --rev` in the final battery. At HEAD it is already red. Bisect: `python3 -B ... --rev 559ee76` → `10 of 10`, exit 0; at `d118a3b` (r75 M75-1 clarification) → `2 of 10`, exit 1, same at HEAD. The added “does not specify equality” phrase triggers the gate's broad `NEGATION_RE`; `good=[]` gates all eight fact credits (`if good`). The r76 receipt lists the file only under gate-registry conformance, not a live `--rev` section. Minimal repair: refine the negation detector to reject hostile/negated citation forms while allowing the sourced “does not specify” wording; preserve the r75 claim text and run self-test plus live `--rev`. This is outside my write scope.

C1 `conjunct_e` at `check_desc_craft.py:904-907` uses `ENTRY not in used_by` where `used_by` is a raw string (the parser returns a cell string). This is substring matching, unlike the exact-member v2 arm and the `used-by lists` predicate. Static code finding only; no full-green C1 world was committed at HEAD, so its behavioral impact was not tested. Minimal repair is split comma-delimited members and strip before membership, requiring counter re-pin; harms no other axis if the frozen contract is preserved.

No claim data is landed, so this is not a verification of C1/C2. Scratch mutation evidence was isolated and removed.

VERDICT: v2 exact-member used-by arm discriminates the tested worlds; mutant suite killed 3, strip mutant survived; landed claim data absent and live v2 no-harm gate is red at HEAD.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w2/F24ChecktationTestSkill.md