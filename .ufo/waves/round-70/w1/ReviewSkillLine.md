# ReviewSkillLine — round 70 wave 1 (reviewer, read-only)

**Verdict: CHANGES RECOMMENDED — the C1 gate-registry row is wrong; the SKILL.md line is fine as written but should get three edits.**

The SKILL.md line at `SKILL.md:241` gets everything right against the entry and the S209–S211 snapshots, and nothing in it overclaims. It loses actionability in three places that cost no lines to fix. Its placement is defensible but weak.

The C2 registry row (`SKILL.md:522`) is accurate in every claim I re-ran.

The C1 registry row (`SKILL.md:521`) says the counter reads 10 of 10 at the measured rev. At the measured tip it reads **9 of 10**, which contradicts the round's own lesson. This is the one high-severity finding.

Checklist gate, run in the lane: exit 0, 11 PASS, 0 FAIL. `trigger.line_budget` passes at **600 of 600** (no headroom left). `trigger.citation_resolves` passes (181 tokens) and `governance.citation_resolves` passes (1253 tokens).

All runs were at tip `16b212a390c7ce68b6bce49b2c3766b154fbcbae`, from `/home/vgpnk/Projects/shokunin/kotoba-shokunin`, with `TMPDIR` set to my own scratch dir `/tmp/k70w1-ReviewSkillLine.R1Ng` (deleted before return). Tools installed or updated: none.

## Commands and observed output

```
$ rg -n 'Testing a skill' SKILL.md
241:- **Testing a skill — the spec's own artefacts.** Hand-author `evals/evals.json` in the skill dir and run each case with and without the skill; grade PASS/FAIL with quoted evidence, script the mechanical checks, leave taste to a human. Trigger sets label ~20 queries `should_trigger` at ~3 runs each: the spec passes a should-trigger query only *above* 0.5, skill-creator's `run_eval.py` at `>=` 0.5, so keep the run count odd — `corpus/knowledge/skill-eval-artefacts-round70.md` (S209–S211).

$ git diff --stat 7d51253f… 16b212a3… -- SKILL.md
 SKILL.md | 3 +++          (line 241, rows 521–522; base 597 lines → tip 600)

$ python3 -B verifiers/verify_skill_checklist.py --json      (lane tree)
exit=0  pass=11 fail=0 na=0
trigger.line_budget          PASS  "600 lines within budget 600 (from box at line 320)"
trigger.citation_resolves    PASS  "181 repo-rooted citation token(s) resolve from the repo root"
governance.citation_resolves PASS  "1253 governance citation token(s) resolve across 2 files; 10 quoted meta-finding(s), 3 schematic token(s) excluded, 1 recorded absence(s) excused, 5 recorded correction(s) excused"

$ git clone -q --shared . $TMPDIR/sb && git -C $TMPDIR/sb checkout -q 16b212a3… && (cd $TMPDIR/sb && python3 -B verifiers/verify_skill_checklist.py --json)
exit=1
trigger.line_budget          PASS  600 lines within budget 600
trigger.citation_resolves    FAIL  line 590: '../.ufo/reports/round-7/kotoba.md' does not resolve from /tmp/k70w1-ReviewSkillLine.R1Ng/sb
governance.citation_resolves FAIL  correction LOG.md:2619 … '../.ufo/reports/round-60/kotoba.md' does not resolve; … (+30 more)
   (this is lesson M116 reproduced: `../` tokens are dead outside the real lane checkout)

$ python3 -B verifiers/check_r69_routed_repairs.py --rev 16b212a3…
r69 routed defects closed 9 of 10
  K69-11: governance.citation_resolves FAIL
exit=1
$ python3 -B verifiers/check_r69_routed_repairs.py --rev 7d51253f…   → closed 0 of 10, exit=1
$ python3 -B verifiers/check_r69_routed_repairs.py --self-test       → 0 failure(s) over 17 assertions, exit=0

$ python3 -B verifiers/check_skill_evals.py --rev 16b212a3…          → skill eval facts backed 8 of 8, exit=0
$ python3 -B verifiers/check_skill_evals.py --rev 16b212a3… --fetch  → backed 8 of 8; live quotes found 8 of 8, exit=0
$ python3 -B verifiers/check_skill_evals.py --rev 7d51253f…          → backed 0 of 8 (entry absent), exit=1
$ python3 -B verifiers/check_skill_evals.py --self-test              → 0 failure(s) over 13 assertions, exit=0 (incl. "tampered snapshot is an environment error (exit 2)")

$ python3 -B verifiers/check_gate_registry.py --rev 16b212a3…        → gate registry rows conformant 51 of 51 lane verifiers; phantom 0, exit=0

$ sha256sum .ufo/waves/round-70/snapshots/*   (all three tracked: git ls-files)
a799805f…  S209-evaluating-skills.md   7cc54fbb…  S210-optimizing-descriptions.md   43e3b8f8…  S211-run_eval.py.txt
   (prefixes match the entry's `source:` lines)
```

## Correctness of line 241, claim by claim against the snapshots

| Line claim | Source bytes | Result |
|---|---|---|
| Hand-author `evals/evals.json` in the skill dir | S209:19 "Store test cases in `evals/evals.json` inside your skill directory"; S209:86 "The main file you author by hand is `evals/evals.json`" | correct |
| run each case with and without the skill | S209:52 "once **with the skill** and once **without it** (or with a previous version)"; S209:112 "When improving an existing skill, use the previous version as your baseline" | correct, but drops the previous-version baseline (finding M2) |
| grade PASS/FAIL with quoted evidence | S209:170 "recording **PASS** or **FAIL** with specific evidence. The evidence should quote or reference the output" | slightly narrower ("quote *or reference*") |
| script the mechanical checks | S209:172 "use a verification script — scripts are more reliable than LLM judgment for mechanical checks" | correct |
| leave taste to a human | S209:144 "Not everything needs an assertion … better caught during human review" | correct |
| ~20 queries `should_trigger`, ~3 runs each | S210:41 "Aim for about 20 queries: 8-10 that should trigger and 8-10 that shouldn't"; S210:90 "(3 is a reasonable starting point)" | correct but ambiguous (finding M3) |
| spec passes only *above* 0.5 | S210:92 "passes if its trigger rate is above a threshold (0.5 is a reasonable default)" | correct |
| `run_eval.py` at `>=` 0.5 | S211:232 `did_pass = trigger_rate >= trigger_threshold`; S211:267 `--trigger-threshold … default=0.5`; S211:266 `--runs-per-query … default=3` | correct |
| so keep the run count odd | at t = 1/2, k/n = 1/2 has a solution only for even n (n ∈ {2,4,6} below 8, by enumeration) | correct for 0.5. Other thresholds have their own gaps (t = 2/3 at n = 3, t = 3/5 at n = 5), but the line scopes the claim to 0.5, so this is informational only. |

**Overclaim:** none. The line makes no claim that a client runs `evals.json`, matching the entry's § Scope. "The spec's own artefacts" fits S209/S210; `run_eval.py` is attributed by name to skill-creator, not to the spec.

## Findings, by severity

### H1 — the C1 registry row states a reading the counter does not produce (`SKILL.md:521`)

The row says: "`r69 routed defects closed 10 of 10` at the measured rev and `0 of 10` at the pinned base". The counter at the measured tip prints `r69 routed defects closed 9 of 10` with `K69-11: governance.citation_resolves FAIL`, exit 1 (output above).

The round's own lesson already records this as a miss: `corpus/lessons/round-70.md:136-142` (M116) and `:149-150` ("C1 stands a **miss as declared** (9 of 10)"). So the shipped SKILL.md contradicts the lane's lesson at the same commit.

`check_gate_registry.py` passes the row (51 of 51 conformant) because it checks the row's shape, not the reading it states.

**Edit** — replace that clause in the row's description cell with:

> `r69 routed defects closed 9 of 10` at the measured rev (K69-11 reads FAIL in any `/tmp` sandbox — `corpus/lessons/round-70.md` M116; a miss as declared) and `0 of 10` at the pinned base

This edit changes no line count.

### M1 — the line sits in a section that fits only half of it (`SKILL.md:241`)

It is a lone bullet at the end of `### Explicit invocation by client`, under `## Frontmatter craft — the trigger surface`. It follows directly after the unrelated decision-table pointer at `:240`, with no blank line between them. The bullet still renders, because a list may interrupt a paragraph.

- The trigger-rate half does belong here: `:228` says an implicit-trigger measure must first set aside explicit activations.
- The output-quality half (`evals.json`, the baseline run, grading) is not frontmatter craft.
- Its natural home is `## Trigger-fidelity checklist`, whose intro (`:255`) says "Every item is checkable by reading the file — no runtime needed". This line is that checklist's runtime counterpart.

The budget is 600 of 600, so any move must keep the line count unchanged.

**Edit (minimum, keep the line where it is):** link it to `:228` (folded into M3's rewrite below).

**Edit (alternative):** delete `:241` and append its text to the end of the `:255-257` paragraph as "Runtime testing is separate: …". This nets −1 line. It touches no `- [ ]` box, so the box hashes (`verify_skill_checklist.py:341` `BOX_RE`) are unaffected.

### M2 — the baseline omits the previous-version case (`SKILL.md:241`)

When an agent revises an existing skill (this lane's usual case), S209:112 says the baseline is a snapshot of the previous version, not a run without the skill. The line's "with and without the skill" would lead an executing agent to the wrong comparison. The entry carries this (F3, "or against a snapshot of the previous version"); the line dropped it.

### M3 — "label ~20 queries `should_trigger`" can be misread as all-positive, and the line gives no file shapes (`SKILL.md:241`)

S210:41 asks for 8–10 queries that should trigger and 8–10 that should not, each labelled `should_trigger` true or false (S210:36-37). An agent hand-authoring `evals.json` also gets no key names. S209:23-29 and :157 show `skill_name`, `evals[]` with `id`, `prompt`, `expected_output`, `files`, and `assertions` (added after the first run, S209:43).

**Edit for M1 (minimum), M2 and M3** — rewrite line 241 in place (one line, net 0):

```
- **Testing a skill — the spec's evaluation artefacts.** Hand-author `evals/evals.json` in the skill dir (`skill_name`; `evals[]` of `id`, `prompt`, `expected_output`, `files`; `assertions` added after the first run) and run each case with and without the skill — against a snapshot of the previous version when revising; grade each assertion PASS/FAIL with evidence that quotes or references the output, script the mechanical checks, leave taste to a human. Trigger sets: ~20 queries, 8–10 `should_trigger: true` and 8–10 `false`, ~3 runs each, rate counted over implicit activations only (table above): the spec passes a should-trigger query only *above* 0.5, skill-creator's `run_eval.py` at `>=` 0.5, so at threshold 0.5 keep the run count odd — `corpus/knowledge/skill-eval-artefacts-round70.md` (S209–S211).
```

This keeps the entry path, so the C2 counter's SKILL.md-cite condition (`check_skill_evals.py:137`) still holds. It adds no `../` or `corpus/` token beyond the existing entry path.

### L1 — no line budget left

The base was 597 lines and this round added 3, so SKILL.md now sits at exactly 600 of 600. The next SKILL.md addition FAILs `trigger.line_budget` unless it moves content out at the same time. This is not a defect of this round; future editors should be told.

## The C2 registry row (`SKILL.md:522`) — accurate

- "`8 of 8` at the measured rev and `0 of 8` at the pinned base": observed, as above.
- Exit 2 on a tampered snapshot: the self-test case passes.
- "`--fetch` reads the three live URLs": a fetch failure is only a note and never changes the verdict (`check_skill_evals.py:187` "network is a second evidence, never the verdict"; `:349` exit depends on `n` only). The row's "none (read-only)" side-effect cell is consistent with this.
- The canonical command carries `--fetch` while the frozen predicate leaves it optional. That is harmless, because the exit code ignores the fetch.

The C1 row's side-effect cell ("temporary sandbox clone under `$TMPDIR` (removed)") also holds: after the run, my `TMPDIR` held only my own `sb`/`sb.json`.

## Residual risk and gaps

- I did not open `controls/C1-skip-control.txt` or the C2 junk/forged controls; they are outside this seat's scope.
- The live `--fetch` match is as of 2026-10-25 11:5x UTC only.
- The per-client explicit-invocation forms at `:232-238` were not re-checked; they predate this round.
