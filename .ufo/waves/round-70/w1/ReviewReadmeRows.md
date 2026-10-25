# ReviewReadmeRows — round 70, wave 1 (reviewer, read-only)

**Verdict: 1 consistency mismatch (medium), 3 low-severity wording imprecisions, 0 dead paths, both corpus verifiers exit 0.**
The Round-70 lessons row (`corpus/README.md:135`) says `## Mistakes` M113-M115. The lesson it indexes holds **M113-M116**. M116 landed in `ac3c0f1` after the row was written in `8edeb49`, and the row was never updated.

Measured at lane HEAD `16b212a390c7ce68b6bce49b2c3766b154fbcbae` (working tree clean for tracked files; only untracked `.ufo/waves/round-70/w1*` paths). No tools installed, no scratch directory used, no lane file modified apart from this report.

## Rows under review

`rg -n 'round 70|Round-70|round-69-verifier-spotcheck' corpus/README.md` → lines 133 (Skill evaluation artefacts), 134 (Round-69 verifier spot-check), 135 (Round-70 lessons).

## Findings

### F-1 (medium, consistency) — README:135 understates the mistake range: M113-M115 vs M113-M116

- `rg -n '^## |M1[0-9][0-9]' corpus/lessons/round-70.md` → `113:- **M113 …`, `122:- **M114 …`, `129:- **M115 …`, `136:- **M116 — class: vacuous (an unsatisfiable counter item, this round's own).**`
- `corpus/README.md:135` → `` `## Mistakes` M113-M115 ``.
- How the drift happened: `git log --format='%h %s' 7d51253f..HEAD -- corpus/README.md corpus/lessons/round-70.md` → `8edeb49` added the three README rows and the lesson. `ac3c0f1` ("…M116 (K69-11 item unsatisfiable in a /tmp sandbox)…") changed only the lesson. Per-commit mistake ids: `8edeb49 M113 — M114 — M115 —`, `ac3c0f1 M113 — M114 — M115 — M116 —`.
- The omitted mistake is the round's own C1 miss (K69-11 cannot be satisfied in a `/tmp` sandbox; C1 stands at 9 of 10). Leaving it out of the index hides that miss.
- The row also breaks the coverage map's convention. Rows 65-69 list each mistake with a one-line gloss, for example `M111 (R68-6: a refusal whose reason was false), M112 (…)` (`rg -n '## Mistakes. M[0-9]+' corpus/README.md`). Row 135 gives a bare range.
- Fix: `` `## Mistakes` M113 (landing: r69 off-branch commits and `probe` attribution), M114 (number drift: nine/ten receipts, 18/22 assertions), M115 (r69 seat reports rewritten after filing), M116 (the K69-11 item cannot be satisfied in a `/tmp` sandbox; C1 a miss as declared) ``.

### F-2 (low) — README:135 omits two of the lesson's six sections

- `rg -n '^## ' corpus/lessons/round-70.md` → `## Inherited state (routed defect K69-5)` (line 17), `## Gate` (31), `## Mistakes` (111), `## Status changes` (153), `## considerthese` (163).
- The row indexes only Gate, Mistakes and Status changes. Two sections are missing:
  - Inherited state: the two pinned r69 seat-report blobs. C1 item K69-5 requires the lesson to name both paths.
  - considerthese: the "Cap the inward turn" measurement.
- This is an omission, not an overclaim.

### F-3 (low) — README:133 "re-opened 2026-10-25" is not true for S211

- `corpus/lessons/round-70.md:46-47` says S211 is "lane-opened, not staged". Only S209 and S210 had staged predecessors (staged S234 and S231, campaign recheck "ran 2026-10-23", line 92).
- So "re-opened" fits S209 and S210, but S211 was opened for the first time. The lesson itself says "Rows opened this round" (line 49).
- Suggested wording: "opened 2026-10-25 with snapshots".

### F-4 (low) — README:133 says "counted by `… --rev <rev> --fetch`", but `--fetch` is not part of the count

- `plans/round-70.md:91-93`: "`--fetch` repeats the quote match on each row's live URL (a second evidence, not part of N)".
- The README wording matches the entry's own `recheck:` line (`skill-eval-artefacts-round70.md:5`), so it is defensible as a recheck command. As a "counted by" statement it mixes the counting run with the live-page evidence.
- Suggested wording: "counted by `verifiers/check_skill_evals.py --rev <rev>` (`--fetch` re-checks the live pages)".

### Checked and found matching (no finding)

- **All paths resolve and are tracked:**
  - `git cat-file -e HEAD:<p>` succeeded for `corpus/knowledge/skill-eval-artefacts-round70.md`, `corpus/lessons/round-69-verifier-spotcheck.md`, `corpus/lessons/round-70.md`, `verifiers/check_skill_evals.py` and `verifiers/check_r69_routed_repairs.py`.
  - `git ls-tree --name-only HEAD .ufo/waves/round-70/snapshots/` lists the three snapshots.
  - Their sha256 prefixes `a799805f` / `7cc54fbb` / `43e3b8f8` and byte sizes 16973 / 13403 / 11464 match the entry's `source:` lines and the lesson's Gate.
- **The commands named in the rows exist:**
  - `check_skill_evals.py --help` → `[--rev REV] [--repo REPO] [--fetch] [--self-test]`; it prints `skill eval facts backed {n} of {TOTAL}` (line 341).
  - `check_r69_routed_repairs.py --help` → `[--rev REV] [--repo REPO] [--self-test]`; it prints `r69 routed defects closed {n} of {TOTAL}` (line 397).
  - Every flag the rows name is accepted.
- **README:133 content matches the entry's facts:**
  - The hand-authored `evals/evals.json` is F1.
  - The three run-produced JSON files are F2.
  - The with/without-skill baseline is F3.
  - PASS/FAIL with evidence is F4.
  - Scripts over LLM judgment is F5.
  - The `should_trigger` set and the 0.5 rule are F7.
  - The `>=` rule and the even-run-count gap are F8 plus the "one disagreement" section.
  - F6 (human review) is not mentioned. That is an omission, not an overclaim.
- **README:134 content matches the spot-check:**
  - Its sections are `## Per-claim re-check` (line 40), `## Per-axis verdicts` (100), `## Discernment spot-check` (117) and `## Routed defects` (150).
  - The discernment table has six admits (S203-S208) and one "reject (retained, corrected)", all marked **agree**; line 138 says "Disagreements: none".
  - Routed defects run K69-1 to K69-11 (lines 152-208).
  - "worked by round 70's C1 counter" is slightly broad: the counter covers 10 of the 11 defects, with K69-4 excluded (`plans/round-70.md:26-27`). This is consistent with the plan.
- **README:135 numbers match the committed scratch files:**
  - `wc -l` gives `reg-ids` 134, `staged-ids` 188, `collisions` 6 (S203-S208) and `quarantine-slice` 13, all tracked at HEAD.
  - The renumber map S234→S209 and S231→S210 is at lesson lines 44-47.
  - The S201 `(13 words)` → `(14 words)` line is at 155-158.
  - "S209-S211 mined at landing" is at 159-160.

## Verifier runs (cwd `/home/vgpnk/Projects/shokunin/kotoba-shokunin`)

```
$ python3 -B verifiers/verify_corpus_integrity.py
corpus.index    tracked=130 unindexed=0 stale=0 missing=0  (148 FILE-column patterns over 129 md files)
corpus.pointers report_dead=0/89 commit_total=39 unresolvable=0 nonhash=0 (shapes [relative=1, absolute=44, tilde=1, bare=43], quoted-excluded=6, pointer-excluded=8; sites in --json)
…
9/9 checks pass
exit=0

$ python3 -B verifiers/verify_corpus_independent.py --json
"head": "16b212a"; index: tracked_files 130, unindexed 0, stale_tokens 0, missing_paths 0;
pointers: report_total 89, report_dead 0; commits: commit_total 39, commit_unresolvable 0, commit_nonhash 0
results: unindexed PASS, stale_patterns PASS, missing_paths PASS, report_dead PASS,
         commit_unresolvable PASS, commit_nonhash PASS (3 INFO observe rows)
exit=0
```

## Residual risk and verification gaps

- Neither corpus verifier checks what a row's description says. Both check only path and pointer resolution, so F-1 passes 9/9 and all PASS rows. Description drift after a follow-up commit (`8edeb49` → `ac3c0f1`) has no gate. This is the same class as the "corrections sweep every mention" rule behind M114.
- I did not run the two counters themselves. That is other seats' scope; I only checked that their command-line interfaces match the rows.
- Out of scope, noticed in passing: `corpus/lessons/round-67.md:131` carries an `M107` bullet, while README's round-67 row lists M104-M106. I did not open it to see whether this is a cross-reference or a second drift.
