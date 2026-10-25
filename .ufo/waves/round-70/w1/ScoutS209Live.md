# ScoutS209Live — round 70 wave 1

**Verdict: HOLDS.** F1–F6: all 6 quotes present on the live S209 page (each exactly once after stripping `*`/backticks). Section attribution correct at the H2 level the entry's `source:` line uses. Snapshot drift: **no** — live page is byte-identical to the committed snapshot (16 973 B, sha256 `a799805f…`, empty `diff`). No fact text contradicts the page; one wording nuance on F5 (below, non-blocking).

Measured at lane tip `16b212a390c7ce68b6bce49b2c3766b154fbcbae`, fetch 2026-10-25 11:56 UTC. No tools installed. Scratch `/tmp/k70w1-ScoutS209Live.riHO` deleted.

## 1. Live fetch vs committed snapshot

```
curl -fsSL https://agentskills.io/skill-creation/evaluating-skills.md -o $W/live.md   # exit 0
wc -c   → 16973 live.md ; 16973 .ufo/waves/round-70/snapshots/S209-evaluating-skills.md
sha256sum → a799805f3a285390c1b6e906b691f56684fa1031b499d177f664f464d99fb684 (both)
diff live.md snapshot → (empty), exit 0
```

The snapshot is the committed blob, not only the working-tree file:
`git ls-tree 16b212a3 …/S209-evaluating-skills.md` → blob `4cc9f00b…`; `git cat-file -p 16b212a3:… | sha256sum` → `a799805f…`. Last commit that touched it: `53de0ac 2026-10-25 07:43:02 -0300 round-70: frozen plan … pinned source snapshots`, which is the freeze commit. The verifier pins the same hash: `verifiers/check_skill_evals.py:47-49`. The entry's `source:` line states 16 973 B / `a799805f…`, which matches.

`curl -fsSI` → `HTTP/2 200`. `last-modified` equals the request `date` (11:56:36 GMT), so the server generates that header per request. It is not evidence of a content change, and the content is unchanged.

## 2. Quote location (normalisation: drop `*` and backticks, the verifier's `norm()` at `verifiers/check_skill_evals.py:76-77`)

Script: a line-by-line search in the stripped live page, with each match assigned to its nearest preceding `##` and `###` heading.

| fact | live line | hits | H2 section | H3 subsection | raw-line match without stripping |
|---|---|---|---|---|---|
| F1 "The main file you author by hand is evals/evals.json." | 86 | 1 | Running evals | Workspace structure | no (backticks) |
| F2 "The other JSON files (grading.json, timing.json, benchmark.json) are produced during the eval process" | 86 | 1 | Running evals | Workspace structure | no (backticks) |
| F3 "run each test case twice: once with the skill and once without it" | 52 | 1 | Running evals | — (H2 body, above the first H3) | no (`**`) |
| F4 "recording PASS or FAIL with specific evidence" | 170 | 1 | Grading outputs | — | no (`**`) |
| F5 "scripts are more reliable than LLM judgment for mechanical checks" | 172 | 1 | Grading outputs | — | yes |
| F6 "Not everything needs an assertion." | 144 | 1 | Writing assertions | — | yes |

Page headings, as observed: `# Evaluating skill output quality`(5), `## Designing test cases`(11), `## Running evals`(50), `### Workspace structure`(54), `### Spawning runs`(88), `### Capturing timing data`(114), `## Writing assertions`(129), `## Grading outputs`(168), `### Grading principles`(207), `## Aggregating results`(216), `## Analyzing patterns`(248), `## Reviewing results with a human`(258), `## Iterating on the skill`(273), `### The loop`(288).

**Section check:**
- The entry's `source:` line names § Designing test cases, § Running evals, § Writing assertions and § Grading outputs. Every quote falls under one of those H2 headings. Precision note: F1 and F2 sit in the `### Workspace structure` subsection of Running evals.
- § Designing test cases holds none of the six quotes. It backs the F1 parenthetical instead: "(prompt, expected output, optional input files per case)" is at lines 13–17, and "Store test cases in `evals/evals.json` inside your skill directory" is at line 19.
- Section attribution is correct.

The verifier agrees independently:

```
python3 -B verifiers/check_skill_evals.py --rev 16b212a390c7ce68b6bce49b2c3766b154fbcbae --fetch
measured-rev: 16b212a390c7ce68b6bce49b2c3766b154fbcbae
skill eval facts backed 8 of 8
live quotes found 8 of 8
exit=0
```

## 3. Depth: paraphrase claims in the fact column against the page

- **F2** says "per-run `grading.json` and `timing.json`, one `benchmark.json` per iteration". The workspace tree at lines 64–83 has `timing.json`/`grading.json` under each `with_skill/` and `without_skill/`, and `benchmark.json` once under `iteration-1/`. Correct. The sentence continues on line 86 with "— by the agent, by scripts, or by you", which matches the fact's "by the agent, by scripts, or by the author".
- **F3** says "or against a snapshot of the previous version" and calls the result a "delta". Line 52 only says "(or with a previous version)". The word "snapshot" is backed by line 112 under § Spawning runs: "Snapshot it before editing (`cp -r <skill-path> <workspace>/skill-snapshot/`) … save to `old_skill/outputs/`". "Delta" is backed by line 246: "focus on the raw pass counts and the delta". Correct.
- **F4** says the evidence "quotes or references the output". Line 170: "The evidence should quote or reference the output". Correct.
- **F5** calls the LLM judge "the fallback for the rest". This is a wording nuance, not a quote failure. Line 172 puts the LLM *first*: "The simplest approach is to give the outputs and assertions to an LLM …". Scripts are then recommended for the code-checkable subset. The partition the fact states is accurate (script for mechanical checks, LLM for the rest). "Fallback" reorders the page's framing, though: the page presents the LLM as the default and scripts as the reliability upgrade. The verifier does not judge this; its key terms (`scripts`, `LLM judgment`, `mechanical`) all pass.
- **F6** says "left to human review". Line 144: "These are better caught during [human review](#reviewing-results-with-a-human)". Correct.
- **Prose citations** in "What the facts change", lines 30–39 of the entry:
  - "Start with 2–3 cases" is at line 43 (`**Start with 2-3 test cases.**`).
  - "add assertions only after the first run" is at line 48. Both are under § Designing test cases, which is correct.
  - The "triples tokens" trade-off is at line 116, under § Capturing timing data, which is correct.
  - "a section titled 'Summary' with one vague sentence … FAIL" is at line 209, under § Grading principles, which is correct.

## 4. Unobserved / limits

- Only the `.md` endpoint was fetched. The rendered HTML page and the `.mdx` source were not compared.
- S210 and S211 (F7 and F8) are out of scope. The verifier's live count includes them (8 of 8), but I did not re-open them by hand.
