# CritC2Semantics — round 70 wave 1 — adversarial semantic read of the C2 entry

**Verdict: DEFECTS FOUND (2 high, 4 medium, 7 low). C2's count of 8 of 8 is accurate, but it does not certify the prose.**
The counter reads the fact cell only for its `S###` id and quote, so every overclaim below sits in text the counter does not score. The entry's one operational claim, "keep the run count odd" (entry:52–56), is **falsified by running the snapshot's own code**. The default configuration *can* hit the gap, and odd run counts open it too.

Scope read: `corpus/knowledge/skill-eval-artefacts-round70.md` at measured tip `16b212a390c7ce68b6bce49b2c3766b154fbcbae` (working tree equals the tip: `git diff 16b212a -- <entry>` is empty). Read against the three committed snapshots, with their hashes verified:

```
$ sha256sum .ufo/waves/round-70/snapshots/*
a799805f3a285390…  S209-evaluating-skills.md      (300 lines, 16973 B)
7cc54fbb6abbcf08…  S210-optimizing-descriptions.md (196 lines, 13403 B)
43e3b8f80dbf69c3…  S211-run_eval.py.txt          (310 lines, 11464 B)
```

Baseline counter run: `python3 -B verifiers/check_skill_evals.py --rev 16b212a3…` printed `skill eval facts backed 8 of 8`, exit=0.

The S211 pin holds. `git ls-remote https://github.com/anthropics/skills refs/heads/main` printed `dbd4588f9e1033efb41dad4bef2f7947c8993d44 refs/heads/main`, and `curl -fsSL raw.githubusercontent.com/anthropics/skills/dbd4588…/skills/skill-creator/scripts/run_eval.py | sha256sum` printed `43e3b8f80dbf…`, equal to the snapshot. Entry:3's provenance is therefore confirmed. No defect.

Line notation: `entry:N` is a line of the entry; `S209:N`, `S210:N` and `S211:N` are snapshot lines (`cat -n`).

---

## HIGH

### H1 — "Keep the run count odd" is falsified; the default configuration *does* hit the gap (entry:52–56; same overclaim in SOURCES S211 row, `corpus/SOURCES.md:152`)

- **Claim.** Entry:52–53 says "With the reference default of 3 runs per query … a rate of exactly 0.5 cannot occur … so the default configuration never hits the gap." Entry:53–54 says "It opens with an **even** run count". Entry:55 gives the action "keep the run count odd". SOURCES:152 adds "disagrees with the specification only at an even run count".
- **Counterexample 1: default configuration, duplicate query text.** `run_eval` groups runs by query *string*: `query_triggers[query].append(...)` (S211:213–222), then `trigger_rate = sum(triggers) / len(triggers)` (S211:229). If an eval set lists the same query twice, that query gets 2×3 = 6 runs, and a rate of 3/6 = 0.5 is reachable under the CLI defaults (S211:266–267).
- **Counterexample 2: odd run count, non-default threshold.** `--trigger-threshold` is a CLI flag (S211:267). With 5 runs and a threshold of 0.6 or 0.4, the float comparison `3/5 == 0.6` is True, so `>=` and "above" diverge at an odd run count.
- **Command.** I copied the S211 snapshot into a scratch sandbox and imported it with a stub `scripts.utils`. I replaced `ProcessPoolExecutor` with `ThreadPoolExecutor` and `run_single_query` with a deterministic fake, so no `claude` process was spawned. The scratch directory has been deleted. Observed output from `python3 -B probe.py` (Python 3.14.8):
  ```
  A dup-query default: runs=6 rate=0.5 should=True run_eval_pass=True spec_wording_pass=False
  B odd-runs thr0.6: runs=5 rate=0.6 should=True run_eval_pass=True spec_wording_pass=False
  C odd-runs thr0.4: runs=5 rate=0.4 should=True run_eval_pass=True spec_wording_pass=False
  D dup conflicting: runs=6 rate=0.0 should=False run_eval_pass=True spec_wording_pass=True
  float checks: True True True
  ```
  Case D shows a related effect: `query_items[query] = item` keeps only the last item (S211:218), so duplicated text with conflicting `should_trigger` labels collapses into one result row with one label.
- **Also.** Entry:50 says "at exactly 0.5". The disagreement actually occurs whenever the rate equals the configured threshold (S211:232 against S210:92), not only at 0.5.
- **Impacted axes:** depth (the entry's only action is wrong), consistency (SOURCES:152 repeats it).
- **Smallest safe correction.** Restate the condition: the two rules diverge exactly when `trigger_rate == trigger_threshold`, i.e. when runs-per-query × threshold is an integer, counting runs per *distinct query text*. Replace the action with "choose runs and threshold so their product is not an integer, and keep query texts unique; otherwise state which rule the report applies". Fix SOURCES:152 to match.

### H2 — The two agentskills.io *guides* are called "the specification", and that framing gives the F7/F8 "disagreement" normative weight it lacks (entry:8, 10, 26, 48, 50, 55, 60, 61; inherited from staged `spec-eval-file-format.md:2, 9`)

- **Claim.** Entry:8 has the title "what the specification ships"; entry:10 says "the specification gives each its own artefact"; entry:26 (F8) says "the specification's wording says above"; entry:48 says "The specification says a should-trigger query passes when its rate is **above**".
- **Contradicting evidence.** Both snapshots are `skill-creation/` how-to guides, and they point to the specification as a *separate* document. S210:28 says "The [specification](https://agentskills.io/specification.md#description-field) enforces a hard limit of 1024 characters", and S210:172 links `specification.md#description-field` again. S209 never uses the word "specification". The rule the entry treats as normative is advice: S210:92 says "(0.5 is a reasonable default)", and S210:90 says "3 is a reasonable starting point". The guide's own script computes only `trigger_rate` and no pass/fail (S210:128). The pages call skill-creator a Skill that "automates much of this workflow" (S209:300; S210:166), not a conforming implementation.
- **Provenance.** The staged file already said "The specification now defines…" (`/home/vgpnk/Projects/shokuknow/merge/kotoba/knowledge/corpus/knowledge/spec-eval-file-format.md:2,9`, `grep -n -i specification`). Re-grounding kept the label. SOURCES:150–151 repeat "the open specification's own procedure / protocol".
- **Impacted axes:** depth (source tier and authority), consistency (the label feeds the S209/S210 rows).
- **Smallest safe correction.** Say "the Agent Skills docs' evaluation guides (skill-creation/)" wherever the entry now says "the specification". Recast F8 and § "The one disagreement" as "skill-creator's runner uses `>=` where the guide's wording says above". Fix the S209 and S210 scope cells.

---

## MEDIUM

### M1 — False independence claim: "the specification states it independently" (entry:43–44)

- **Claim.** "This matches the skill-creator loop the lane already held (S124) — the specification states it independently."
- **Contradicting evidence.** S210:166 says "The [`skill-creator`] Skill automates this loop end-to-end: it splits the eval set, evaluates trigger rates in parallel…". S209:300 cross-references skill-creator the same way. The guide cites skill-creator, and both come from the same ecosystem; no snapshot supports independent derivation. Counting S210 as independent corroboration of S124 is a duplicate-authority error.
- **Impacted axes:** depth (corroboration count).
- **Correction.** Replace "states it independently" with "describes the same loop and points to skill-creator as automating it (S210:166)".

### M2 — "The one disagreement" is premature saturation, and the runner's client scope is unstated (entry:46 heading, entry:26 "The reference implementation", entry:60 "one reference implementation")

- **Evidence that the runner diverges elsewhere.**
  - **Registration.** The runner registers a temporary *command file* in `.claude/commands/` (S211:45, 53–54, 60–68). The guide says to register "the skill" and defines a trigger as the agent loading "your skill's `SKILL.md`" (S210:79, 81). The runner instead counts a `Skill` tool use or a `Read` of the command-file path (S211:137, 147, 164–166).
  - **Failed runs.** Timeouts (30 s default, S211:101, 178, 265) and exceptions (S211:223–225) are recorded as *not triggered*. That counts toward a pass for should-not-trigger queries and a fail for should-trigger queries. The guide says nothing on this.
  - **Client.** The runner works only with Claude Code: `claude -p` (S211:70–76) and `.claude/` (S211:22–32).
  - One reconciliation, in fairness: the runner's first-tool-call early exit (S211:141, 153–154) is endorsed by S210:134 ("stop a run early once … the agent either consulted the skill or started working without it"). That point is not a defect.
- **"Reference implementation".** No snapshot calls run_eval.py that. The lane coined the term, which is the "false provenance" pattern; SOURCES:152 says "Anthropic's reference trigger-eval runner". S124's row explicitly limits itself with "no claim about any other client" (SOURCES:135); S211 carries no such limit.
- **Impacted axes:** depth (saturation), consistency (client-scope rule applied to S124 but not S211).
- **Correction.** Use the heading "The pass-rule disagreement". Call the runner "skill-creator's Claude Code runner (run_eval.py)". Add one scope sentence: Claude Code only, trigger measured via a temporary command file, failed or timed-out runs count as not triggered.

### M3 — F6 and entry:37–38 overclaim the human-only lane; the quote supports none of the prose cell (entry:24, 37–38)

- **Claims.** F6 says style, visual design and whether an output feels right "are **left to** human review"; its quote is "Not everything needs an assertion." Entry:37–38 says "let an LLM grade **only** judgement properties, and **leave taste to a human**".
- **Evidence.**
  - S209:145 says these qualities "are **better caught** during human review", which is softer.
  - S209:211–213 recommends **blind comparison** in which "an LLM judge … scores holistic qualities — organization, formatting, usability, polish". That is an LLM judging taste.
  - S209:172 makes the LLM the *default* grader for all assertions, so the word "only" is unsupported.
  - The 5-word quote mentions neither human review nor style. Every subject in the prose cell sits outside the quote; the counter's key term (`check_skill_evals.py:64`) is the quote itself.
- **Correction.** F6: "Qualities hard to decompose into pass/fail (style, visual design, 'feels right') are better caught by human review than by assertions." Drop "only" and "leave taste to a human", or add the blind-comparison caveat.

### M4 — F1 "The **one** hand-authored artefact" says more than the quote ("The **main** file") and is contradicted on-page (entry:19)

- **Evidence.**
  - S209:86 says "The **main** file you author by hand is `evals/evals.json`", and the other JSON files may be produced "by you".
  - S209:262 has the reviewer hand-write `feedback.json` in the workspace.
  - S209:29, 35 show hand-supplied input files under `evals/files/`.
  - S210:34 and 146 describe hand-authored `eval_queries.json`, `train_queries.json` and `validation_queries.json`.
  - F1's parenthetical (prompt, expected output, optional input files) is true (S209:13–17) but sits outside the quote. It also omits that `evals.json` later carries `assertions` (S209:147–163).
- **Correction.** Write "The main hand-authored artefact…".

---

## LOW

### L1 — "Human review is reserved for what neither can capture" (entry:13)
S209:260 says "For each test case, review the actual outputs alongside the grades". Human review covers every case, not just a residue. S210 says nothing about human review for triggers. The wording came from staged `spec-eval-file-format.md:37` ("human review explicitly reserved"), although the staged file's own line 31 quotes "are better caught". So "every claim it makes was re-opened on S209" (`corpus/lessons/round-70.md:65–66`) did not catch it. **Fix:** "Human review covers what neither catches and reads every case's outputs (S209:260)."

### L2 — F3 "not an absolute score" and entry:34 "means nothing without" (entry:21, 34)
S209:221–231 records absolute `pass_rate` per configuration alongside `delta`. S209:244 advises: "focus on the raw pass counts and the delta". **Fix:** drop "not an absolute score" and change "means nothing without" to "is read against".

### L3 — F5 makes the LLM judge "the fallback" (entry:23)
S209:172 says "The simplest approach is to give the outputs and assertions to an LLM… For assertions that can be checked by code … use a verification script". The LLM is the default and scripts are the refinement. The routing clause ("use a verification script") is outside the quote, which only compares reliability. **Fix:** "an LLM judge grades the rest (the page's simplest default)".

### L4 — Scope disclaimer omits on-page automation (entry:60–62)
"None of the three sources says" that any client runs `evals/evals.json`. That is true of *clients*, but S209:300 says the skill-creator Skill "automates much of this workflow — running evals, grading assertions, aggregating benchmarks". A reader may take "no client" to mean "nothing runs it". Separately, entry:30–31 ("versioned with the instructions … travels with the skill when it is handed over") is a distribution claim that no snapshot makes; S209 only places the file in the skill directory (S209:19, 58–62). **Fix:** mark the second claim `[INFERENCE]` or drop it; name S209:300 in the scope line.

### L5 — Softened modal verbs hardened (entry:25, 42–43, 38–39)
- F7 "0.5 **by default**" versus S210:92 "0.5 is a **reasonable** default".
- Entry:42–43 "not the last one" versus S210:161 "the best description **may not** be the last one".
- Entry:38–39 drops S209:208's condition "If an assertion says 'includes a summary'".

### L6 — Header section lists don't cover the sections the body cites (entry:1–2)
Entry:43 cites S210 "§ The optimization loop", which is absent from entry:2's section list (S210:149). F2's per-iteration `benchmark.json` relies on S209 § Aggregating results (S209:215–217), which is absent from entry:1. F2's "during the run" is also loose: `benchmark.json` is written "once every run in the iteration is graded" (S209:217). Entry:3 gives the branch as "lines 230–234", but the pass/fail branch is S211:231–234 (230 is the label read), and the lesson itself says 231–232 (`round-70.md:62`).

### L7 — Refusal reasoning contradicted by S209 (outside the entry, but entry:62–65 depends on it)
`corpus/lessons/round-70.md:81` refuses S301 with the flip "an entry about blind comparators, **which S209 does not describe**". S209:211–213 describes blind comparison. Entry:64's "none adds a fact this entry states" may still hold, but the recorded flip condition is false on the snapshot. Routed note only: this file is lesson text, and I did not edit it.

---

## Counter blindness (structural, applies to every finding above)

`verifiers/check_skill_evals.py:143–174` (`awk 'NR>=125&&NR<=176'`) uses the fact cell only to collect `SID_RE` and `QUOTE_RE` matches (lines 144–145). It never compares the prose to the quote. So N = 8 shows that eight quotes exist on the snapshots with their key terms present. It does not show that the eight fact sentences, the "What the facts change" bullets, or § "The one disagreement" are supported. This is a declared tradeoff of C2's frozen predicate and not a counter defect. The judge should still not read 8 of 8 as semantic backing.

## Ranked summary

| rank | id | entry lines | snapshot evidence |
|---|---|---|---|
| 1 | H1 | 52–56 (+SOURCES:152) | S211:213–229, 232, 266–267; probe cases A–C |
| 2 | H2 | 8, 10, 26, 48, 50, 55, 60–61 | S210:28, 92, 172; S209:300 |
| 3 | M1 | 43–44 | S210:166; S209:300 |
| 4 | M2 | 26, 46, 60 | S211:22–32, 45–68, 101, 223–225, 265; S210:79–81 |
| 5 | M3 | 24, 37–38 | S209:145, 172, 211–213 |
| 6 | M4 | 19 | S209:86, 262; S210:34, 146 |
| 7 | L1 | 13 | S209:260 |
| 8 | L2 | 21, 34 | S209:221–231, 244 |
| 9 | L3 | 23 | S209:172 |
| 10 | L4 | 30–31, 60–62 | S209:19, 300 |
| 11 | L5 | 25, 38–39, 42–43 | S210:92, 161; S209:208 |
| 12 | L6 | 1–3 | S210:149; S209:215–217; S211:231 |
| 13 | L7 | (lesson:81) | S209:211–213 |

**Confirmed sound (no defect):** F4 (S209:170). F7's should-not-trigger half (S210:92). F8's quote and branch (S211:231–234). Entry:49–51's should-not-trigger agreement (S211:234). Entry:40–41's counts (S210:41, 90). Entry:35–36 timing rationale (S209:117). The S211 tree pin and hash were checked live (see top).

## Process notes

- **Tools installed:** none.
- **Read-tool fault:** the Read tool refused `S211-run_eval.py.txt` (11 464 B) and `check_skill_evals.py` (15 199 B) with "exceeds maximum allowed characters (100000)". I read both via `cat -n` and `awk` instead.
- **Scratch:** `/tmp/k70w1-CritC2Semantics.VhXP` (deleted; `ls -d /tmp/k70w1-CritC2Semantics.*` shows none).
- **Mutations:** no committed lane file, jj state, git index or fleet repo was mutated. `/home/vgpnk/Projects/shokuknow` was only grepped.
