verdict: landing class reproduced at BASE c61a973 — the closure commit added corpus/lessons/round-46-verifier-spotcheck.md without a coverage-map row or a baseline pin refresh; both corpus instruments exit 1 there and were green at the parent 04192c2, so the closure is the single commit that turned them red. The existing instrument already captures the class; the missing piece is a closure-time run (no hook exists) and a second artifact (the pin), not a new predicate. Candidate fix (index row + pin 58→59) takes both instruments to exit 0 in a scratch clone; mutations show it can fail.

# MistakeUnindexedLanding — round-47 build (mistake mining, leaf lane)

Scope: `c61a973` `corpus/lessons/round-46-verifier-spotcheck.md` vs `corpus/README.md` (integrator-authored; recorded as a class, not blamed). Fleet-side closure enforcement is routed as adjacency (§6), not implemented here. Production files untouched: `git status --short` in the repo shows only the pre-existing `?? .ufo/waves/`, `?? plans/round-47.md`.

Environment: git 2.56.0; Python 3.14.8; no tools installed or upgraded. Scratch clone: `/fast/scratch/kotoba-r47/MistakeUnindexedLanding/lane` (detached at `c61a973b2e02e1ded169703ddcb06466f4edd8bd`). All verifier runs below were executed in that clone, not in the repo.

## 1. What the closure commit did (BASE)

- `git show --stat c61a973` → `corpus/lessons/round-46-verifier-spotcheck.md | 17 +++++++++++++++++`, `1 file changed, 17 insertions(+)`. No change to `corpus/README.md`, `verifiers/corpus-baseline.json`, or any file that references the new file.
- `git grep -n 'round-46-verifier-spotcheck' c61a973 -- corpus verifiers` → no match, exit 1. The file is referenced by nothing at BASE.
- `corpus/README.md` at BASE: 116 lines; coverage-map table ends at `corpus/README.md:62` (`| Round-46 lessons | lessons/round-46.md |`). No row names the spot-check file.
- `verifiers/corpus-baseline.json:13-16` pins `corpus.index.tracked_files` `"expect": 58` (set at the r46 landing; see its `round46_landing` note). The tree has 59 tracked corpus files: `git ls-files corpus | wc -l` → 59 = 58 `.md` (`grep -c '\.md$'` → 58) + `corpus/knowledge/sibling-citation-routing-round16.json` (`grep -v '\.md$'` → 1, exit 0). The verifier's `md_files` is 58; its `tracked_files` is 59 and includes the `.json`.
- `corpus/QUALITY.md` has 18 criteria (Q01–Q18), none on index coverage (`git grep -n -i 'unindexed|index row|indexed in' c61a973 -- corpus/QUALITY.md corpus/lessons/round-46.md` → no output, exit 1). The r46 `## Mistakes` table (`corpus/lessons/round-46.md:17-37`, M1–M19) has no index-coverage class. So at BASE the class has no `captured-by` criterion in the lane's own bar, even though an instrument captures it.

## 2. Instrument results (scratch clone, exit codes recorded)

| state | command | exit | key output |
|---|---|---|---|
| 04192c2 (parent-of-closure) | `python3 -B verifiers/verify_corpus_integrity.py --no-baseline --json` | 0 | tracked 58, unindexed 0 |
| f2f9ee1 (r46 landing) | same | 0 | tracked 58, unindexed 0 |
| 04192c2 | `python3 -B verifiers/verify_corpus_independent.py --json` | 0 | — |
| **c61a973 (BASE)** | `python3 -B verifiers/verify_corpus_integrity.py` | **1** | `DRIFT corpus.index.tracked_files: observed=59 expected=58`; `DRIFT corpus.index.unindexed: observed=1 expected=0 / empty`; `7/9 checks pass` |
| c61a973 | `python3 -B verifiers/verify_corpus_integrity.py --json` | 1 | `unindexed_detail: ["corpus/lessons/round-46-verifier-spotcheck.md"]`; report_total 40, report_dead 0, commit_total 29, commit_unresolvable 0, commit_nonhash 0 |
| c61a973 | `python3 -B verifiers/verify_corpus_independent.py` | 1 | `unindexed` DRIFT, `head: c61a973`, counts identical to integrity |
| c61a973 | `python3 -B verifiers/verify_corpus_integrity.py --self-test` | 0 | `self-test: 0 failure(s) over 150 assertions` |
| c61a973 | `python3 -B verifiers/verify_corpus_independent.py --self-test` | 0 | `self-test: 91 assertions, 0 failures` |

These match `.ufo/waves/round-47/before/SUMMARY.md` (`corpus integrity: exit=1 DRIFT tracked_files 59!=58, unindexed 1`; `corpus independent: exit=1 DRIFT unindexed`) and `before/verify_corpus_integrity.py.out`.

Mechanism: `verifiers/verify_corpus_integrity.py:548-549` builds the tracked set from `git ls-files corpus`; `:433-434` computes `unindexed` as tracked corpus files not covered by a README coverage-map FILE-column pattern. The instrument is correct for this class; it was simply not run at closure.

## 3. Landing history (the class, measured)

- Commits that add a non-README `corpus/**/*.md`: **30** (`git log --name-status -- corpus`, `A` rows).
- Of those, **9** add such a file without touching `corpus/README.md` in the same commit: `0f658ff`, `23ae301`, `63ceba7`, `683d147`, `778310d`, `8c300ad`, `9a74726`, `b0c7cb2`, `c61a973` (command: per-commit `git show --name-only` co-touch count; exit 0).
- At HEAD (= c61a973) the verifier reports exactly one unindexed file (`c61a973`'s). So every one of the other 8 orphan landings was closed by a later commit. Closures seen in history: `911b870` ("restore the aggregator's committed corpus lesson, index it" — closes `0f658ff`), `cd4798b` ("kotoba index row + tracked_files pin refresh" — closes `b0c7cb2`, same day, 2026-10-14). Other closures: successors touching README (`e997d45`, `abef8aa`, `a614927`, `5cc1340`, `0089974`); not all were individually re-verified.
- Per-commit verifier spot-measure (`git checkout --detach <c>` in scratch, `--no-baseline --json`): `0f658ff` unindexed 2 (`checklist-execution-round15.md`, `round-9-aggregator-corpus-verdict.md`); `63ceba7` 1; `683d147` 1 (`round-8-aggregator-box3-coldrun.md`); `b0c7cb2` 1 (`round-19-recensus.md`); `911b870` 0; `cd4798b` 0. Commits `23ae301`, `778310d`, `9a74726`, `8c300ad` returned non-JSON from the verifier (script absent or erroring at that commit; not investigated — see §7).
- Prior statement of the same class in the lane's own index: `corpus/README.md:42` (`Round-9 aggregator corpus verdict` row) — "Round 15 … added this index row, since an unindexed or dead-pointer corpus file keeps this repo's own gate non-zero". So the class is recurrent (r9 → r15, r19 → same-day fix, r46 open), not a one-off.

Interpretation: the instrument's predicate (tree-level: every tracked file is indexed; tracked count equals pin) is the right one. The landing class recurs because (a) the lane's convention is land-then-index in a later commit (9/30 landings), and (b) nothing requires the instrument to run at the closure commit.

## 4. Counterexamples and blind spots (measured)

1. **Untracked file is invisible.** At 04192c2 with `corpus/lessons/probe-untracked.md` created but not added: integrity exit **0** (`tracked 58 unindexed 0`). Same probe after `git add -N` (intent-to-add): exit **1** (`tracked 59 unindexed 1`). After `git add`: exit **1**. So a working-tree run before staging is blind to the class; the instrument reads `git ls-files`, not the directory. A closure gate must run after `git add -N` / staging, or additionally list `git ls-files -o --exclude-standard corpus`.
2. **The index row alone does not restore green.** Candidate README row only (pin left at 58): integrity exit **1**, `DRIFT corpus.index.tracked_files: observed=59 expected=58` (`8/9 checks pass`). The pin is a second closure artifact.
3. **The pin alone does not restore green.** Pin 59 with no row: exit **1**, `DRIFT corpus.index.unindexed: observed=1`. Both artifacts are required.
4. **Commit-level predicate would over-fire.** "A commit that adds a corpus file must touch `corpus/README.md`" flags 9/30 landings, including 8 whose orphan was closed later in history and 5 aggregator-authored lessons. As a *policy* it would block the lane's historical land-then-index practice; the tree-level predicate is the one that matches the gate's contract. Choose the tree-level check at the closure commit; do not adopt the commit-level one without an explicit integrator decision.
5. **Mis-typed row is still caught.** README row renamed to `round-46-verifier-spotchek.md` (pin 58, as in the run): exit **1** with `DRIFT corpus.index.tracked_files: observed=59 expected=58` (pin unrefreshed), `unindexed 1`, `stale_patterns 1`, `missing_paths 1` — the regression arm for the row content works.
6. **Row present, file absent**: exit **1** with `stale_patterns 1`, `missing_paths 1`.

## 5. Candidate fix (drafted, NOT applied to the repo)

Artifact: `.ufo/waves/round-47/build/MistakeUnindexedLanding.patch` (1784 bytes; `git diff` from scratch, two files):
- `corpus/README.md` +1 row after line 62: `| Round-46 verifier spot-check (integrator) | lessons/round-46-verifier-spotcheck.md | … |`
- `verifiers/corpus-baseline.json:15` `"expect": 58` → `59`.

Result in scratch: integrity `python3 -B verifiers/verify_corpus_integrity.py` → **exit 0, `9/9 checks pass`**; independent `python3 -B verifiers/verify_corpus_independent.py` → **exit 0**; integrity `--self-test` → exit 0 (`0 failure(s) over 150 assertions`). Fix-can-fail arms: §4 items 2, 3, 5, 6 (each exit 1 with the named DRIFT).

Overlap warning: round-47 plan C3 ("corpus index covers `round-46-verifier-spotcheck.md`") is the same row. The integrator must merge, not apply both. This patch is evidence and a candidate, not a second owner of C3.

## 6. Routing (adjacency, fleet-side — not implemented here)

- No hook enforces the closure: `git config --get core.hooksPath` → exit 1 (unset); no `.githooks/`, `.github/`, or `.git/hooks` non-sample hooks in the repo (`ls -a` and `ls .git/hooks | grep -v sample` → empty). Closure-time enforcement is therefore a process step, which lives on the integrator/fleet side. Proposed adjacency for the integrator: a required pre-commit step on the staged closure tree — `git add -N` the new files, run both corpus instruments, refuse on exit ≠ 0. Fleet-root files were not read or edited.
- Proposed lane-owned rows for the integrator to append (QUALITY.md and lesson files are append-only; not written by this lane):
  - M20 (new lesson row, new file or the next round's lesson — not an edit of `round-46.md`): "Corpus file landed without coverage row or pin refresh". Evidence: `git show --stat c61a973`; verifier exit 1 with `unindexed_detail`. captured-by: `corpus.index.unindexed` + `corpus.index.tracked_files` (red only if run). fix: §5 + §4.1 staging rule.
  - Q19 (proposed): "A commit that adds a tracked corpus file also adds its coverage-map row and refreshes `corpus-baseline.json`'s `tracked_files` expectation; both corpus instruments exit 0 on the staged tree (untracked files included via `git add -N`)." grounded in M20.

## 7. What I did NOT check

- The jj-colocated closure path: the repo is jj-colocated (`jj log -r @` → `wkxxslzzqppx…`). I did not test whether a `jj` snapshot changes the untracked-file blind spot in §4.1 — [INFERENCE] it may, but unobserved.
- The per-commit verifier results for `23ae301`, `778310d`, `9a74726`, `8c300ad` (non-JSON output; not diagnosed), and the successor-closure claims beyond those listed in §3 (only HEAD-state was verified for "all closed").
- Whether `W3ReviewKotoba`'s spot-check report exists in the fleet repo (`.ufo/waves/kaika-w3/` — cited by the lesson, not opened).
- The fleet-root hooks or any fleet-level closure gate; none was read.
- The round-47 C2/C1 gates and the other before-values; I ran only the two corpus instruments.
- Whether the lane's `knowledge/` or `SOURCES.md` files carry any further unindexed files: the verifier reported `unindexed 1` at BASE, so none beyond the closure file.
- No subagents were used; no git mutating command ran in the repo; the scratch `git stash` was popped before the candidate was copied.

## Commands (exit codes)

- `git show --stat c61a973` → 0
- `git grep -n 'round-46-verifier-spotcheck' c61a973 -- corpus verifiers` → 1
- `git grep -n -i 'unindexed|index row|indexed in' c61a973 -- corpus/QUALITY.md corpus/lessons/round-46.md` → 1
- `python3 -B verifiers/verify_corpus_integrity.py` at c61a973 (scratch) → 1; `--json` → 1; `--self-test` → 0
- `python3 -B verifiers/verify_corpus_independent.py` at c61a973 → 1; `--self-test` → 0
- Same integrity/independent at 04192c2 and f2f9ee1 → 0
- Untracked probe at 04192c2: plain → 0; `git add -N` → 1; staged → 1
- Candidate row only → 1 (tracked DRIFT); pin only → 1 (unindexed DRIFT); row + pin → 0 (9/9) and independent → 0
- Mistyped row → 1; row with missing file → 1
- `git config --get core.hooksPath` → 1
- `git status --short` (repo) → 0, only pre-existing untracked `.ufo/waves/`, `plans/round-47.md`
