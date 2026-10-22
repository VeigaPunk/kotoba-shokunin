VERDICT: FAILS (narrow). Commit order, plan immutability, commit identity and remote push HOLD. "No target value moved" FAILS for C2: the reviewed term list that sets the C2 count gained three terms in commit 34cfffbb, after the plan commit. Under the list the plan committed, the same HEAD content counts 4 of 7 (exit 1), not 7 of 7.

Scope: sizing order, target movement, author identity, push. C1 and C2 mechanics, fixtures, fetch checks and routed defects belong to other seats; I touch them only where they move a target value.

## Findings, highest severity first

1. HIGH. C2 target moved after the plan commit (calibration).
- Plan commit 7c81a787 (12:07:31 -0300) calls the reviewed list "a reviewer's judgment frozen in code" (plans/round-51.md:102) and says "No target value moved" (:73). It names no terms.
- Commit 34cfffbb (12:11:45 -0300) edits REVIEWED_LEVERS (`git diff 7c81a787 34cfffbb -- verifiers/check_overlap_levers.py`: 5 insertions, 3 deletions) and lands the content those terms score in the same commit: Copilot CLI `ignoredSkillsLocations`; Claude Code `disable-model-invocation: true`; Gemini CLI `/skills disable <name>`.
- Probe in a scratch clone at 59903b26, with the plan-commit counter (blob fee473d) copied in as verifiers/_old_counter.py:
  - HEAD counter, `--rev 59903b26`: 7 of 7, exit 0.
  - Plan-commit counter, `--rev 34cfffbb`: 4 of 7, exit 1. Unbacked: Copilot CLI, Claude Code, Gemini CLI.
  - Plan-commit counter, `--rev 59903b26`: 4 of 7, exit 1.
  - HEAD counter, `--rev 43ca0bfb`: 0 of 7, exit 1. The before-value does not depend on the list.
  - HEAD counter `--self-test`: 0 failures, 22 assertions, exit 0.
- The widening is disclosed only outside the plan: the entry's § Limits ("The L1 added three terms before landing so that a quote could carry the exact backtick span") and the commit message ("reviewed list +3 terms"). The plan's "frozen" and "no movement" sentences are false for HEAD.
- Recommendation to L1, not applied: either report the C2 after-value as 4 of 7 on the plan-commit list, with the three terms named as a post-plan widening (commit 34cfffbb); or name the widening, its commit and the list change in the plan's two sentences (plans/round-51.md:73 and :102). Either way, the word "frozen" must go from the plan.

2. MEDIUM. The lane's working tree is ahead of the pushed commit.
- `git --no-optional-locks status --porcelain`: ` M PROVINCE.md`, ` M SCORECARD.md`, ` M corpus/README.md`, `?? .ufo/waves/round-51/`. Against HEAD (`diff HEAD --numstat`): PROVINCE.md 3/3, SCORECARD.md 10/2, corpus/README.md 12/1.
- mtimes: 12:14:57 (PROVINCE.md, corpus/README.md) and 12:19:04 (SCORECARD.md), all after the last commit (12:12:02).
- The uncommitted SCORECARD.md text says "Round 51 completed" and adds round-51 score rows: "pass 7 of 7 ... @ e0320302" and "7 of 7 @ 34cfffbb". None of these lines is in HEAD or on origin. Commit or drop them before the lane is called landed. I did not touch them.

3. MEDIUM. The sizing evidence is untracked, so "before any landing" rests on file times.
- `git ls-tree -r --name-only 59903b26 -- .ufo/waves/round-51` prints nothing; `git check-ignore` exits 1, so the folder is not ignored either. It is untracked.
- CriticC1Sizing.md mtime 11:24:27 -0300; CriticC2Sizing.md 11:26:04 -0300. Both precede the plan commit (12:07:31). File times are not proof. The git order itself is provable (below).

4. LOW (recorded). Other numbers moved after the plan commit; none is named in the plan.
- e0320302 (C1): verifiers/floors-registry.json surfaces floor 99 -> 115; new overlap_levers floor 22; instrument_total 11 -> 12 (ratchet raises). verifiers/baseline.json omp sha256 and mtime re-pinned (fdbc8136... -> 85d9daf3...), as the plan describes.
- 59903b26: verifiers/corpus-baseline.json expect 69 -> 72 and 44 -> 46 (re-record; counts not re-derived here).
- The plan's own stated values did not move in its text: 5 of 7 -> 7 of 7; 2 of 2; DRIFT 2/3 -> OK 3/3; 0 of 7 -> 7 of 7; self-test 22.

5. LOW. C1's counter code changed after the plan commit: verifiers/verify_surfaces.py (281 changed lines, e0320302) and verifiers/check_assertion_floors.py (28). The plan pre-describes the `Kl|Ho|bq` allowlist growth and the module-scope `S$` rule (plans/round-51.md:82-87), so this is declared, not a moved target. verifiers/surfaces-baseline.json is byte-unchanged from 43ca0bfb (`git diff --quiet`, exit 0). C1 mechanics not re-derived.

6. INFO. The base commit 43ca0bfb (outside the range) is authored by protocol-shokunin <protocol@shokunin.local> at 11:04:58 -0300. Every round-51 commit is by the lane identity.

## Checks that HOLD

Order (`git log --format='%H %ci %s' 43ca0bfb..59903b26`, exit 0; 5 commits, oldest first):
    7c81a787 12:07:31  plan with re-sized claims + C2 counter (first commit of the round)
    e0320302 12:07:41  C1 freshness
    34cfffbb 12:11:45  C2 depth content (+ REVIEWED_LEVERS +3)
    e6219026 12:11:48  D1 DescDraft wave evidence
    59903b26 12:12:02  corpus baseline re-record
- `git log --format='%h %ci %an %s' -- plans/round-51.md` lists 7c81a787 only, as an addition. `git cat-file -e 43ca0bfb:plans/round-51.md` exits 128: the plan is absent at base.
- Plan blob 008d28cd5bfa3f109714520c3d2397b27f0aec65 at 7c81a787, at HEAD (`git rev-parse <rev>:plans/round-51.md`), and in the working copy (`git hash-object`). `git diff 7c81a787 59903b26 -- plans/round-51.md` is empty, exit 0. No plan text moved after landing.
- The re-sizing section sits in the first claim commit (7c81a787 also adds the C2 counter), so "at or before the first claim commit" holds with equality.
- Identity: all 5 commits have author and committer `kotoba-shokunin <kotoba@shokunin.local>`. Lane config: `user.name=kotoba-shokunin`, `user.email=kotoba@shokunin.local`.
- Push: `git ls-remote origin refs/heads/master` = 59903b2637689739a5b9901956301da72d0effe1, exit 0, at 15:17:54Z. `git rev-parse master` and `git rev-parse refs/remotes/origin/master` both give 59903b26. jj 0.45.1 (already at /home/vgpnk/.local/bin/jj; not installed by this seat), read-only: `jj --ignore-working-copy --no-pager bookmark list --all-remotes master` shows master, @git and @origin at 59903b26, exit 0, window 15:19Z. Git HEAD is detached (`git symbolic-ref --short HEAD` exits 128); `master` names the same commit. The push covers committed history only; finding 2 is outside it.

## Evidence (commands and exit codes)
- Scratch: `git clone -q <lane> /fast/scratch/hyaku/kotoba-r51/falsify/ReviewCommitOrder/lane`, `checkout -q 59903b26`, then `git show 7c81a787:verifiers/check_overlap_levers.py > verifiers/_old_counter.py` (scratch only).
- `python3 -B verifiers/check_overlap_levers.py --rev 59903b26...` -> 7 of 7, exit 0.
- `python3 -B verifiers/_old_counter.py --rev 34cfffbb...` -> 4 of 7, exit 1. Same with `--rev 59903b26...`.
- `python3 -B verifiers/check_overlap_levers.py --rev 43ca0bfb...` -> 0 of 7, exit 1.
- `python3 -B verifiers/check_overlap_levers.py --self-test` -> 0 failures, 22 assertions, exit 0.
- `git diff --stat 43ca0bfb 59903b26 -- verifiers/` -> 7 files, 1261 insertions, 30 deletions, exit 0.
- `git diff --stat 7c81a787 59903b26 -- verifiers/ plans/` -> 7 files, 337 insertions, 33 deletions; plans/round-51.md not listed; exit 0.
- `git diff --quiet 43ca0bfb 59903b26 -- verifiers/surfaces-baseline.json` -> exit 0.
- `git --no-optional-locks status --porcelain` and `diff HEAD --numstat` -> exit 0 (finding 2).
- Disclosure search: `_grep` (literal only; no lsp device in this seat's tool list, so no semantic claim rests on it) for `ignoredSkillsLocations|reviewed list|frozen in code|No target value moved` -> plans/round-51.md:73 and :102; the entry's § Limits; .ufo/waves/round-51/falsify-dispatch.json.

## Gaps and residual risk
- Not re-derived: C1 numbers and mechanics; C2 term semantics (critic seats); corpus counts 69 -> 72 and 44 -> 46; `--fetch` on the plan-commit list (the 4 of 7 is the offline count).
- Critic report timing rests on file times only.
- jj was used only with `--ignore-working-copy`; I did not check whether jj imported git refs into the lane's operation log.
- Writes: this report only, at the lane path. Probes ran in the scratch clone. No git or jj mutating command ran in the lane. Tooling: no installs or updates by this seat.
