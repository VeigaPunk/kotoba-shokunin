# ScoutConsiderthese — round 70 wave 1

**Verdict: ACCURATE FOR `SKILL.md`, OVERSTATED AS WORDED.** The measurement reproduces exactly: the command prints 7. `7827628` is the first round-61 commit on the lane's lineage, and "nine rounds" (rounds 61–69) is correct. No new instruction for an executing agent landed in `SKILL.md` in that span. The lesson's wording has two calibration defects, both cosmetic to C2 and neither flipping its direction:

- **D1 (wrong):** "all Sources-list reflows". Six of the 7 lines are Sources reflows. The seventh is a reflow of the intro paragraph (`SKILL.md:45`, above `Rank: shonen` at :47). One Sources "reflow" also drops a word ("the round-9 consistency measurement" became "round-9 consistency measurement", `SKILL.md:583`), so it is not byte-pure.
- **D2 (scope overreach):** "no new instruction for an executing agent in nine rounds" is phrased more broadly than its `SKILL.md`-only measure supports. Suggestion 2 defines reader-facing text as "`SKILL.md`, a checklist, or a corpus entry linked from it". In the same span, `corpus/QUALITY.md` gained 7 imperative rows (Q56–Q62). `SKILL.md:523` links that file directly ("admission bar in `corpus/QUALITY.md`"). Those rows are lane record-keeping rules (receipts, errata, refusals), not prompt-craft guidance for a skill user. The claim holds only if "executing agent" means a skill user, so it should be scoped to say that.

Confidence: high on the facts (all observed below); medium on D2's classification of Q56–Q62 as not craft guidance (that is a judgement call).

## Findings

### F1 — Count reproduces: 7

```
git -C …/kotoba-shokunin diff 7827628^ 7d51253 -- SKILL.md | rg '^\+[^+]' | rg -v '^\+\| .verifiers/' | wc -l
→ 7
```

The 7 lines:

1. `+catalogue renders the full \`description\` … — no cliff. The body is the only part the executing agent always sees. Craft means` — **intro paragraph**, now at `SKILL.md:45`. This joins two old lines (hunk `@@ -42,8 +42,7 @@`) and came in with `da86c03` (round 67).
2. `+- \`corpus/SOURCES.md\` — where this lane learns: …` — Sources (`SKILL.md:523`).
3. `+- \`/home/vgpnk/Projects/shokunin/*/AGENTS.md\` (17 files …` — Sources.
4. `+- \`/home/vgpnk/Projects/shokunin/.ufo/prompts/*-round-*.md\` (50 files …` — Sources.
5. `+- \`corpus/knowledge/harness-router-models-round9.md\` — the two-harness router model` — Sources.
6. `+  (tag, render, offer gate, failure mode, verify recipe) with the round-9 …` — Sources.
7. `+- \`corpus/knowledge/claim-scope-audit-round9.md\` — round-9 consistency measurement: …` — Sources (`SKILL.md:583`); this one drops "the".

I checked for hidden wording changes by normalising whitespace across all non-table text at both revisions and running a word-level diff (difflib). The only non-whitespace difference in the whole non-table body is:

```
delete … `corpus/knowledge/claim-scope-audit-round9.md` — the round-9 consistency measurement: || … — round-9 consistency measurement:
```

So outside the gate table, `SKILL.md` changed by reflow plus one deleted article. There is no new instruction. "Gained 7 added lines" is literally true of the `+` lines, but those replace 11 removed non-table lines (`… | rg '^-[^-]' | rg -v '^-\| .verifiers/' | wc -l` → 11). The body's net line count went down.

### F2 — The filter excludes 18 gate-registry lines, and none of them is craft instruction

```
git diff 7827628^ 7d51253 -- SKILL.md | rg '^\+\| .verifiers/' | wc -l   → 18
```

The 18 are 15 new registry rows (from `check_client_trust_gates`, `check_r67_routed_repairs`, `check_routed_repairs` and so on through `check_province_core`) plus 3 rewritten rows (`check_scoped_rules`, `verify_corpus_independent`, `verify_corpus_integrity`). Each row is a lane-gate inventory entry: a command, its exit codes and the round's counter notes. The exclusion is sound for the reader-facing question, but the claim depends on it, so the lesson should say the table is excluded *because* it is lane-internal. It currently states the exclusion without the reason.

### F3 — `7827628` is the first round-61 commit; the range covers exactly rounds 61–69

```
git log --format='%h %ad %s' --date=iso 7827628~6..7827628
→ 7827628 … 15:48:49 round-61: plan freeze (3 claims, frozen predicates), …
  f3246d1 … 15:48:49 round-60 verifier spot-check (integrator, hyaku): non-author admit/reject
  79cf263 … round-60: close (attempt 2) …
git rev-parse 7827628^  → f3246d1493b60ea1c0d947a19c39f9e08e92f326   (the r60 spot-check)
git log --all --grep='round-61' --format='%h %ad %s' | tail -3   → oldest is 7827628
```

- `git log --all -S'round-61' -- plans` turns up three subjectless commits at the same timestamp (`991235c`, `cfe724e`, `e7dd439`, each with parent `f3246d1`). `git merge-base --is-ancestor <c> 7d51253` reports all three as **NOT ancestors** of the tip. They look like jj snapshots off the line and do not displace `7827628`.
- Round composition of `7827628^..7d51253`: 100 commits, no merges. Counts are 26× round-61, 20× round-62, 9× round-63, 8× round-64, 7× round-65, 7× round-66, 6× round-67, 10× round-68, 6× round-69 (4 written "round 69", 2 written "round-69"), and 1× `considerthese: 2026-10-24 daily reflection`. There is no round-60 or round-70 commit in the range.
- `7d51253` is "round-69 verifier spot-check (integrator, hyaku)". 61..69 inclusive is **9 rounds**, which is correct.

### F4 — Considerthese suggestion 2, read without editing

`considerthese/2026-10-24.md:31`, "**Cap the inward turn.**", proposes that every round carry at least one claim "whose output is text an executing agent reads (`SKILL.md`, a checklist, or a corpus entry linked from it)". A pure-instrument round must name the reader-facing claim it unblocks, and each reflection should add a "last reader-facing landing" line (r60 at the time). The lesson paraphrases this correctly (`corpus/lessons/round-70.md:165-167`). The reflection reads only up to r66 (`2a8eba5`); the lesson's extension to r69 rests on its own measurement, which F1 confirms.

### F5 — Under suggestion 2's own definition, a linked corpus file did gain instructions (D2)

I listed the files `SKILL.md` links outside the table (41 paths) and checked which changed in the range with `git diff --numstat 7827628^ 7d51253 -- <path>`:

```
8   0   corpus/QUALITY.md
142 1   corpus/SOURCES.md
163 0   LOG.md
25  19  SKILL.md
156 7   verifiers/verify_skill_checklist.py
```

`git diff 7827628^ 7d51253 -- corpus/QUALITY.md | rg '^\+[^+]'` shows 7 new rule rows, Q56–Q62, all imperative. Examples: "Reserve `byte-exact` for literal byte-for-byte equality…" (Q56); "a source row or staged claim is refused on an observed fact…" (Q62). They govern how the lane writes receipts and lessons, not how anyone writes prompts. So "no new instruction" holds only if "executing agent" means a skill user, which is the reading the lesson intends. The sentence should state that scope, for example: "no new reader-facing line in `SKILL.md` outside the gate registry".

### F6 — Reader-relevant depth landed in the corpus but is unreachable from `SKILL.md`

There are 10 new knowledge entries in the range (`git diff --name-status 7827628^ 7d51253 -- corpus/knowledge | rg '^A'`). Three hold external craft facts:

- `instruction-authority-ladder-round67.md` (S123/S124/S129)
- `client-trust-gates-round68.md` (S198–S202, S208)
- `skill-name-precedence-round69.md` (S203–S207)

`git show 7d51253:SKILL.md | rg -c <name>` returns no match for any of the 10. `corpus/README.md` indexes each one exactly once, but `SKILL.md` never links `corpus/README.md` (`rg 'corpus/README'` on the tip `SKILL.md` matches nothing). This supports the lesson's thesis: depth went into the corpus without reaching the executing agent's surface. It also means "no new instruction" is true of the surface, not of the lane's knowledge.

## Remaining unknowns

- Whether `SOURCES.md` "used-by" cells point to the r67–r69 entries, which would give a two-hop path from `SKILL.md`. Not checked; suggestion 2 says "linked from it", which I read as direct.
- Whether C2's single `SKILL.md` line (§ Frontmatter craft) is present at the measured tip `16b212a`. Not checked; outside this question.

## Tooling

Nothing installed or updated. I used only git, rg and python3, already present. My only scratch was `/tmp/k70sc_*` temp files, removed in the same commands. I made no edits to any committed file.
