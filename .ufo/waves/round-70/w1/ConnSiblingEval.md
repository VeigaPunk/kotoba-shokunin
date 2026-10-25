# ConnSiblingEval — round 70 wave 1 (connector, read-only)

**Verdict: STRICT_HITS 0.** No sibling lane owns the round's new ground: `evals/evals.json`, the `should_trigger` trigger-eval set, with/without-skill grading, or `benchmark.json`. None of the five pinned terms occurs on any sibling scope surface (PROVINCE.md, SKILL.md, corpus/knowledge). Across whole sibling Git trees the terms occur once, as a homonym in a tameshi wave report. The nearest seam is kengaku's "eval design … benchmark grader" scope. It is a MENTION, and kengaku's own split routes skill craft to kotoba. This agrees with `PROVINCE.md` § Adjacent: there is no new row and no reclassification.

Read at kotoba `HEAD` `16b212a390c7ce68b6bce49b2c3766b154fbcbae`; kengaku HEAD `f20a1097af900dc4595e0da0fa5e12e673f9ce7e`, tameshi HEAD `506e99c7b73c85711f066895984d501fcf7539cd`, chousa HEAD `7fb9a2321da78cf1a1b94dbe08c533461dbfd778` (worktrees, read-only). No tools installed. No scratch directory was needed: every command was a read.

## Coverage

There are 20 sibling lanes (`ls -d *-shokunin` gives 21; kotoba is excluded). All 20 have PROVINCE.md and corpus/knowledge. 18 have SKILL.md; audio and game-dev-2d have none (seed form, matching the § Adjacent rows).

## Findings

### F1 — strict-term sweep over scope surfaces: 0 hits

```
cd /home/vgpnk/Projects/shokunin && FILES=<20×PROVINCE.md, 18×SKILL.md, 20×corpus/knowledge, kotoba excluded>
rg -n -i 'evals\.json|should_trigger|trigger[ -]evals?|skill[ -]evaluation|benchmark\.json' $FILES
-> (no output) exit=1
```

### F2 — widened sweep over scope surfaces: mentions only

```
rg -n -i 'should[-_ ]trigger|evals?/evals|evaluating[-_ ]skills|skill[-_ ]creator|trigger[-_ ](eval|fidelity|test|quer)|with[-/ ]without[- ]skill|grading\.json|benchmark\b|skill[-_ ]evals?' $FILES
rg -n -i 'with[_ -]skill|without[_ -]skill|grading\.json|timing\.json|expected_output|agentskills|skill-creation|eval_queries|run_eval|run_loop' $FILES   -> (no output)
```

Classification of every distinct hit family:

| file:line | text (short) | class | why |
|---|---|---|---|
| kengaku-shokunin/SKILL.md:3 | "LLM/model research & evaluation — eval design, benchmark selection, offline replay grading … Triggers: … 'benchmark grader' … kotoba owns prompt and skill craft (kengaku keeps only measured capability effects)" | MENTION (closest seam) | Its object is the model; it explicitly assigns skill craft to kotoba |
| kengaku-shokunin/PROVINCE.md:30-32, :138 | "kotoba: prompt- and skill-craft rules, render/trigger behaviour — this lane keeps the *measured* effect of prompt format on capability" | MENTION; split stated by the sibling | Trigger behaviour goes to kotoba; only measured effects stay with kengaku |
| kengaku-shokunin/PROVINCE.md:8,13,37,123,196-219; SKILL.md:23-64,570,627,651-677; corpus/knowledge/benchmark-*.md, contamination-transparency-card.md, eval-design-digest-{2,3}.md, eval-prior-art-calibration.md, bench-arena-*.md | model benchmark selection, task validity, verifier execution, contamination cards | MENTION (`benchmark` homonym) | These are model and agent benchmarks, not skill `benchmark.json` |
| chousa-shokunin/corpus/knowledge/scope-refusal-r12.md:22,32; scope-phrase-gap-r18.md:9-37; verification-r16.md:27; claim-support-states-r24.md:78; archived-export-intake.md:103; claim-verification-r2.md:105 | `SCOPE_KENGAKU` phrase list (`model benchmark(s)`, `llm eval`); "Bare `benchmark`, `evaluation`, `eval` … stay" unrouted | MENTION | chousa refuses model-quality evaluation (PROVINCE.md:10-11 "model-quality or evaluation claims (→ kengaku)") and claims nothing about skill evaluation |
| game-dev-3d-shokunin/corpus/knowledge/unreal-mcp/README.md:144 | "`.gitignore` — ignores `skills/*-workspace/` skill-creator artifacts" | MENTION | A third-party plugin inventory; it reads skill-creator output paths, not the method |
| game-dev-3d-shokunin/corpus/knowledge/unreal-mcp/upstream/skills/unreal-mcp/SKILL.md:3; kumitate-shokunin/corpus/knowledge/kimi-skills-plugins.md:52,134,164 | vendored or recorded description `Trigger when…` texts | MENTION | Records of trigger text, with no trigger-eval method |
| kasegi-shokunin/corpus/knowledge/ai-assisted-finding-validation.md:8-39; kumitate-shokunin/corpus/knowledge/durable-execution-failure-detection.md:81,90; kotodama-shokunin/corpus/knowledge/verification/verification-method-overview.md:205; kake-shokunin/corpus/knowledge/ghp-subpath-spotcheck.md:33; kaidoku-shokunin/SKILL.md:1115; mori/tsukuroi grading/assertion lines | `benchmark`, `should trigger`, `grading` in other senses | NOISE | Lexical collisions only |

### F3 — tameshi: no strict hit; the one tree-wide term hit is a homonym

```
tameshi-shokunin/PROVINCE.md:3-5  "verification-fixture craft — the reusable method of honest checks: hermetic suites, mutation testing, fail-closed arms, verdict-line discipline"
tameshi-shokunin/PROVINCE.md:14-17 "every lane's gate remains its own; tameshi owns only the reusable craft … Never edits a sibling's gate code"
tameshi-shokunin/SKILL.md:3        triggers 'hermetic suites', 'mutation testing', 'gate fixtures'
```

A supplementary `git grep` of the strict pattern over every sibling's full tracked tree (`for d in …; git -C $d grep -n -I -i -E '<strict>' HEAD -- .`) returns one line: `tameshi-shokunin/.ufo/waves/round-17/w3/RR2.md:179` "T1 trigger evaluation: 3 stale". This is outside the scope surfaces (a wave report). It is also a homonym: `tameshi-shokunin/.ufo/waves/round-17/w2/CR42.md:153` "runbook:288-289 T1=stale; ledger ER-3 trigger 1=after hardening …" defines T1 as a re-pin trigger of the mutation ledger. Script-checked assertions (C2 surface) touch tameshi's fixture *method* only in kind. kotoba records what the spec says, so this is not a claim on tameshi's ground.

### F4 — chousa: no hit; research method only

`chousa-shokunin/PROVINCE.md:3-11` and `SKILL.md:3` cover question framing, source hierarchy and claim-vs-source checking. They refuse "model-quality or evaluation claims (→ kengaku)". C2's quote-located-in-snapshot check is kotoba's claim admission, as § Adjacent's chousa row already records. There is no new contact.

### F5 — census pin still current for the nearest seam

```
diff <(git show 1f3b0f1e…:SKILL.md | awk 'NR==3') <(git show HEAD:SKILL.md | awk 'NR==3')   (in kengaku-shokunin)
-> desc identical pin->HEAD
```

kengaku's commit has moved from `1f3b0f1e` to `f20a1097`, but its description (SKILL.md:3, 902 bytes) is byte-identical. So the § Adjacent kengaku row (`PROVINCE.md:59`, commit `1f3b0f1ec41…`) still holds as a boundary statement, and the census classification `adjacent` stands.

### F6 — kotoba's own records carry no sibling bound for the new ground

```
git -C kotoba-shokunin show HEAD:corpus/knowledge/skill-eval-artefacts-round70.md | rg -c -i 'kengaku|tameshi|chousa|sibling|adjacen'  -> (no count) rc=1   ; file is 65 lines
git -C kotoba-shokunin show HEAD:PROVINCE.md | rg -n 'round 69|round 70|Round 69|Round 70'                -> (no output)
```

`SKILL.md:241` (HEAD) adds "Testing a skill — the spec's own artefacts … `evals/evals.json` … `should_trigger`". The description lines `SKILL.md:12-14` already route chousa, kengaku and tameshi. Round 63 set a precedent of a sibling-bound sentence on the Core row (`PROVINCE.md` round-63 bullet, "Sibling bound (`ScoutW2SiblingOverlap` … STRICT_HITS 0)"). Neither the round-70 entry nor PROVINCE.md Core carries one for this ground yet.

## Proposed move (one, bounded)

**Affected axes:** adjacency (improves), coverage (improves), depth and consistency (neutral).

When the round-70 Core row is written, append a sibling-bound clause on the round-63 pattern. It should cite this report: STRICT_HITS 0 across 20 lanes and 58 scope surfaces. It should name the one live seam: kengaku (`SKILL.md:3`, `PROVINCE.md:30-32`) owns *measured* effects, so kotoba keeps the spec's artefact format and grading procedure. A *measured* trigger rate from running `should_trigger` on a harness (today a Frontier item, "implicit-intent trigger fidelity … unmeasured on any harness") would be a measured capability effect of description wording. Before such a row enters Core, it must be split with or routed to kengaku.

The non-obvious second-order effect: C2 is safe because it only documents. The lane's own Frontier, however, points at running trigger evals, and that is the first kotoba result kengaku's stated split would claim. Recording the split now costs one clause. Leaving it out invites a contested row in a later round.

**Risks:** `check_sibling_census.py --province PROVINCE.md` checks lane set, classification and commit, not boundary text (PROVINCE.md § Adjacent preamble). A Core-row clause is not checked by it, so the clause adds no regression surface. It also adds no mechanical guarantee. Writing it is the closure/L1's call; this seat edits nothing.

**Verification for the integrator:** re-run F1 (expect exit 1, no output) and F5 (expect `desc identical`) at the measured tip. After the clause lands, run `python3 -B verifiers/check_sibling_census.py --province PROVINCE.md`, which should stay exit 0 because rows are unchanged.

**Unobserved:** sibling `.ufo/` wave reports beyond the strict-term `git grep` in F3; untracked sibling files. Census `validate` was not run by this seat.
