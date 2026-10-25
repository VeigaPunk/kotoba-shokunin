source: S209 — Agent Skills — Evaluating skill output quality — https://agentskills.io/skill-creation/evaluating-skills.md — § Designing test cases, § Running evals, § Writing assertions, § Grading outputs — fetched 2026-10-25 (16 973 B; snapshot `.ufo/waves/round-70/snapshots/S209-evaluating-skills.md`, sha256 `a799805f…`)
source: S210 — Agent Skills — Optimizing skill descriptions — https://agentskills.io/skill-creation/optimizing-descriptions.md — § Designing trigger eval queries, § Testing whether a description triggers, § Avoiding overfitting with train/validation splits — fetched 2026-10-25 (13 403 B; snapshot `S210-optimizing-descriptions.md`, sha256 `7cc54fbb…`)
source: S211 — anthropics/skills — skill-creator `scripts/run_eval.py` at tree `dbd4588f9e1033efb41dad4bef2f7947c8993d44` (equal to `main` on 2026-10-25, `git ls-remote`) — the pass/fail branch (lines 230–234) and the argparse defaults (lines 266–267) — fetched 2026-10-25 (11 464 B; snapshot `S211-run_eval.py.txt`, sha256 `43e3b8f8…`)
verified-at: 2026-10-25
recheck: 90d — `python3 -B verifiers/check_skill_evals.py --rev <rev> --fetch` (the eight quotes on the committed snapshots and on the live pages); a changed page is a re-open, never a silent snapshot swap
ground: the lane held the skill-creator trigger loop (S124: 20 queries, 3 runs, 60/40 held-out split) but no row for the specification's own `skill-creation/` evaluation pages and no entry on the output-quality artefact — `grep -n 'evaluating-skills\|evals.json' corpus/SOURCES.md corpus/knowledge/*.md` printed nothing at `7d51253f`. Theme assimilated from the read-only campaign package `merge/kotoba/` (staged `spec-eval-file-format.md`, rows S234 and S231, renumbered by document to S209 and S210); S211 is lane-opened.

# Skill evaluation artefacts — what the specification ships for testing a skill (round 70)

A skill is tested on two separate questions, and the specification gives each its own artefact:
**does the output come out right** (an assertion set in `evals/evals.json`, graded per run) and
**does the skill fire when it should** (a trigger query set labelled `should_trigger`, scored as a
trigger rate). Human review is reserved for what neither can capture.

## Facts (counted by `verifiers/check_skill_evals.py`)

| id | fact | row | located quote |
|---|---|---|---|
| F1 | The one hand-authored artefact lives inside the skill directory at `evals/evals.json` (prompt, expected output, optional input files per case). | S209 | "The main file you author by hand is evals/evals.json." |
| F2 | Three more JSON files come out of the eval run rather than being authored up front — per-run `grading.json` and `timing.json`, and one `benchmark.json` per iteration — produced by the agent, by scripts, or by the author during the run. | S209 | "The other JSON files (grading.json, timing.json, benchmark.json) are produced during the eval process" |
| F3 | Every case runs twice — with the skill and without it (or against a snapshot of the previous version) — so the result is a delta over a baseline, not an absolute score. | S209 | "run each test case twice: once with the skill and once without it" |
| F4 | Grading is evidence-bearing: each assertion gets PASS or FAIL plus evidence that quotes or references the output. | S209 | "recording PASS or FAIL with specific evidence" |
| F5 | Assertions a program can check (valid JSON, row count, file exists) go to a verification script; an LLM judge is the fallback for the rest. | S209 | "scripts are more reliable than LLM judgment for mechanical checks" |
| F6 | Style, visual design and whether an output feels right are left to human review rather than forced into pass/fail assertions. | S209 | "Not everything needs an assertion." |
| F7 | A should-trigger query passes when its trigger rate over repeated runs is above the threshold, 0.5 by default; a should-not-trigger query passes below it. | S210 | "A should-trigger query passes if its trigger rate is above a threshold (0.5 is a reasonable default)." |
| F8 | The reference implementation passes a should-trigger query at a rate equal to the threshold too (`>=`), where the specification's wording says above. | S211 | "did_pass = trigger_rate >= trigger_threshold" |

## What the facts change for an author

- **Ship the evaluation with the skill.** `evals/evals.json` sits beside `SKILL.md`, so it is versioned
  with the instructions it tests and travels with the skill when it is handed over (F1). Start with
  2–3 cases and add assertions only after the first run shows what to check (S209 § Designing test
  cases).
- **Read results as a delta.** A with-skill pass rate means nothing without the without-skill run
  of the same prompt (F3); `timing.json` exists because a skill that improves output but triples
  tokens is a different trade from one that is better and cheaper (S209 § Capturing timing data).
- **Split the checks by who can make them.** Script what a program can verify (F5), let an LLM grade
  only judgement properties, and leave taste to a human (F6). A PASS needs concrete evidence; a
  section titled "Summary" with one vague sentence is a FAIL (F4; S209 § Grading principles).
- **Trigger sets are labelled, repeated and split.** About 20 queries, 8–10 that should trigger and
  8–10 that should not, each with `should_trigger`; run each about 3 times and score the rate (F7);
  keep ~40% as a validation set that never guides edits, and pick the best iteration by validation
  pass rate, not the last one (S210 § Avoiding overfitting, § The optimization loop). This matches
  the skill-creator loop the lane already held (S124) — the specification states it independently.

## The one disagreement, and the action it implies

The specification says a should-trigger query passes when its rate is **above** the threshold (F7);
skill-creator's `run_eval.py` passes it at **`>=`** (F8), while it passes a should-not-trigger query
only at `rate < threshold`, matching the specification's below — so at exactly 0.5 the two disagree
on should-trigger queries only. With the
reference default of **3 runs per query** (`--runs-per-query`, default 3, line 266) a rate of exactly
0.5 cannot occur (0, 1/3, 2/3, 1), so the default configuration never hits the gap. It opens with an
**even** run count: at 2 or 4 runs, one query that fired half the time passes under `run_eval.py` and
fails under the specification's wording. **Action:** keep the run count odd, or state which rule the
report applies when it is even.

## Scope and refusals

Scope: the specification's evaluation guidance and one reference implementation. No claim is made
that any client *runs* `evals/evals.json` automatically — none of the three sources says so, and the
lane has not observed it. Staged material refused this round (reason and flip in
`corpus/lessons/round-70.md` § Gate): the raw `.mdx` duplicates of the two pages (staged S285/S286),
the announcement post (staged S301) and the description improver (staged S303) — none adds a fact
this entry states.
