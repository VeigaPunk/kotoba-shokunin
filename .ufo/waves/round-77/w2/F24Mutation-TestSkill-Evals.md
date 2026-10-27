# F24ChecktationTestSkill — r77 w2

Lane HEAD: `6523aced1ee0ebe07dca996213bdc645a6acbd1e`. The worktree has only the freeze commit; claim data is not committed. `corpus/SOURCES.md` S213 still has only `corpus/knowledge/skill-eval-artefacts-round70.md`. No lane files were changed. Scratch clone was restored to HEAD with clean status, then removed. No tools installed.

Frozen hashes match plan: `check_desc_craft.py` `cf3c45d9e3985f11889816f4bb371dc0d5541c10c09ce2ab3966a4bff4603b9e`; `check_r75_routed_repairs.py` `989203c40e1aab55fc14ee1d444dd4fa8b49fe01144b2dcdeaa6a27fa39f4a63`.

At HEAD, C1 command `python3 -B verifiers/check_desc_craft.py --repo . --rev 6523aced1ee0ebe07dca996213bdc645a6acbd1e` → `description craft backed 0 of 6`, exit 1. C2 command with `--work /fast/scratch/hyaku/kotoba-r77/F24Mutation-TestSkill-Evals/work` → `r75 routed repairs closed 0 of 4`, exit 1.

Assigned gate at HEAD: `python3 -B verifiers/check_skill_evals_v2.py --repo . --rev 6523aced1ee0ebe07dca996213bdc645a6acbd1e` → `skill eval artefacts verified 2 of 10`, exit 1, SKILL-line finding; no used-by finding. `--self-test` → 0 failures, exit 0.

Used-by worlds (scratch commits): A `c8da07a53d9a1120a3ffa896921d930aea3f238b`, exact comma-member append plus stub: no used-by finding; C1(e) advances to missing lesson. B `f8701cff4283a13c7fcee20a8877433195e402de`, `.bak` substring: v2 F7 exact-member failure plus A10 census failure; C1(e) rejects. C `e6efe5e5d9561654e876c25f8095766d077b3fcc`, only new member plus stub: v2 F7 fails while census passes; C1(e) advances to missing lesson.

Mutants (SELF_SHA updated): arm disabled — killed by substring self-test (10/10 accepted, exit 1); exact-member weakened to substring — killed likewise, exit 1; comma changed to semicolon — killed by multi-member positive (9/10, exit 1); `.strip()` removed — survived, self-test 0 failures, exit 0 (fixture does not test a whitespace-prefixed required member). Live W-B with arm disabled/substring no longer emitted F7, but A10 caught the missing path. Restored gate full sha256: `d4df34cf48ba11cc6631cd1e7ef24334b634f92d1e8b54fcd6368b39e4224bfb`; HEAD and clean status confirmed; scratch removed.

No-harm blocker: v2 live counter is already red at HEAD. Bisect: `--rev 559ee76` gives 10/10 exit 0; `--rev d118a3b` gives 2/10 exit 1, unchanged at HEAD. The sourced “does not specify equality” line hits broad `NEGATION_RE`, making `good=[]` and gating all eight fact credits. The r76 battery receipt has no live v2 `--rev` section. Minimal repair: refine negation matching without changing the r75 claim text; retest self-test and live gate. Separate static C1(e) concern: `ENTRY not in used_by` is string substring membership; exact comma-member parsing/re-pin would be required. No full-green C1 world tested.

VERDICT: assigned v2 exact-member arm discriminates tested worlds; three mutants killed, strip mutant survived; claim data absent and live no-harm gate red.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w2/F24Mutation-TestSkill-Evals.md