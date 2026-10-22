Result: MIXED — the four named repairs (README :75 index row, README Core-note correction, SCORECARD.md:28 depth lead, PROVINCE.md:18) are accurate against the spot-check, the SKILL.md § Anti-patterns table, and the plan-commit counter (measured `4 of 7`), and the SCORECARD lead now leads with the declared result; residuals found: one unqualified 7-of-7 sibling of routed defect 1 at PROVINCE.md:26, a stale line pointer in `corpus/lessons/round-52.md:71`, and a literal-string gap in the new sweep registry.

Target: routed defects 1–2 of `corpus/lessons/round-51-verifier-spotcheck.md:158-172` and their repairs. Lane head `c8407a45`; counters exercised in a scratch clone at `/fast/scratch/hyaku/kotoba-r52a2/ReviewCorrections` (never pushed).

## Repair-by-repair verdicts

### 1. `corpus/README.md:75` (index row) — HOLDS
Appended bold "Round 52 correction (routed defect 1)" inside the row, original text preserved. Verified content: "the effects in the landed table are `removed in a scope` (Copilot SDK, Gemini CLI) or `automatic choice off` (the other five), not \"removed everywhere\"" matches SKILL.md:409-418 cell-for-cell (S030 and S029 carry `removed in a scope`; S031, S025, S022, S024, S021 carry `automatic choice off`). "the declared round-51 count is 4 of 7 on the plan-commit counter `7c81a787` (7 of 7 only on the widened counter, Q28)" — measured (below). Append-in-place-of-record is the index's own convention (same pattern as row :59's "Round-48 qualification (append-only)" and row :72's supersede note).

### 2. `corpus/README.md` Core note (the round-51 append-only block inside the sibling-arbitration-gap bullet, now :147-167) — HOLDS
The spot-check defect's `corpus/README.md:133-141` is the same bullet (line numbers drifted between the spot-check and the landing; the round-51 note is :147-157 at `c8407a45`). The original note — pre-falsify lever set (`ignoredSkillsLocations`, `disable-model-invocation: true`, opencode permission `deny`) plus the unqualified `overlap levers backed 7 of 7 clients` — is retained verbatim at :147-157, and the "Round 52 correction (append-only; routed defect 1 …)" paragraph at :158-167 states the declared result `4 of 7` on `7c81a787` and lists the falsify-corrected lever set. The listed set matches SKILL.md:411-418 exactly: SDK `disabledSkills` (removed in a scope), Copilot CLI `disable-model-invocation`, VS Code `disable-model-invocation`, Claude Code `disable-model-invocation`, opencode `metadata["opencode/autoinvoke"]`, Gemini `/skills disable <name>` (removed in a scope), Codex `allow_implicit_invocation`. The "replaced in the falsify wave" triple matches `corpus/lessons/round-51.md:150-159` and the entry's corrections section `corpus/knowledge/skill-overlap-levers-round51.md:109-131`. Correctly appended, not rewritten.

### 3. `SCORECARD.md:28` depth lead — HOLDS (leads with the declared result)
The cell now opens "declared result, on the counter committed with the plan (`7c81a787`): … `0 of 7` exit 1 @ `43ca0bfb` → `4 of 7`, exit 1 on the landed content". The widened `7 of 7` @ `34cfffbb` follows, explicitly labelled "Second measurement, never the declared one (Q28)". The disclosure "(Lead rewritten round 52, routed defect 2 of the round-51 spot-check; the lead first written here gave the widened value.)" is in-cell, and the round-51 falsify-correction paragraph is preserved lower in the cell. "four counted rows are new to the corpus (…; the "six" first written here was the pre-falsify count)" matches `corpus/lessons/round-51.md:163` and the entry :127-131. Every stated value was re-measured:

| claim in the lead | measured | result |
|---|---|---|
| `0 of 7` exit 1 @ `43ca0bfb` on the plan-commit counter | `python3 -B verifiers/frozen_overlap_7c81a787.py --rev 43ca0bfb…` → `overlap levers backed 0 of 7 clients`, exit 1 | exact |
| `4 of 7` exit 1 on the landed content | same script `--rev 34cfffbb` → `4 of 7`, exit 1; `--rev c8579a4c` → `4 of 7`, exit 1 | exact |
| three named failure classes (Copilot SDK and Gemini `removed in a scope`; opencode quote with inner double quotes) | per-client lines: `effect not allowed ('removed in a scope')` (SDK, Gemini); `entry quote malformed (opencode)` — the malformed-quote clause is the inner-double-quote case (round-51 `CriticLeverSemantics.md` probe B2) | exact |
| widened counter `7 of 7`, exit 0 @ `34cfffbb` | `git show 34cfffbb:verifiers/check_overlap_levers.py` run with `--rev 34cfffbb` → `overlap levers backed 7 of 7 clients`, exit 0 | exact |
| falsify-hardened counter at the round-51 head: `7 of 7` | `check_overlap_levers.py` (unchanged c8579a4c→c8407a45 per `git diff`, empty) `--rev c8579a4c` → `7 of 7`, exit 0 | exact |

The claim that "`--fetch` found 7 of 7 quotes on the live pages (2026-10-22T15:10:48Z, exit 0)" was not re-run here (network); it is consistent with `.ufo/waves/round-51/falsify/ReplayC2Counter.md:18-21` (`quotes found on live pages 7 of 7`, exit 0). [INFERENCE] via prior seat record, flagged.

### 4. `PROVINCE.md:18` — HOLDS
Appended correction (round-51 text at :17 preserved). "the declared round-51 result is `overlap levers backed 4 of 7 clients` on the counter committed with the round-51 plan (`7c81a787`); `7 of 7` holds only on the counter widened after the plan (Q28), so the claim did not verify" — all verified above. "The levers themselves stand as recorded in `SKILL.md` § Anti-patterns" — the head counter at `c8579a4c` prints `7 of 7`, exit 0, so the standing table is consistent.

### 5. SCORECARD edited in place vs appended — NOT A VIOLATION (correct choice)
No append-only rule covers SCORECARD. `PROTOCOL.md:123-124` names `LOG.md` as the append-only file; `:314-321` covers `MANIFEST.json` `rounds`; `:524-529` covers `.ufo/l0-questions.md`; `:338-340` the ledger; `:135-137` filed reports. The SCORECARD row (`PROTOCOL.md:436`) describes a live score table — "every score is a claim: it carries the counting command … so a reader can re-derive it" — with no append-only clause; SCORECARD.md itself declares none (`grep -i append SCORECARD.md` hits only historical annotations). Moreover the routed defect demanded a headline rewrite — "the headline must lead with the declared result" (spot-check :167) — which an appended tail correction cannot satisfy; per `PROTOCOL.md:123-124` corrections land as new commits, never amended bytes, and this was a new commit (`c8407a4`) that preserves the superseded lead's substance in-cell plus full git history. The lane convention inside cells is newest-first prepend; the uncommitted working-tree edits to the coverage and freshness cells (see below) follow it.

## Findings (severity order)

1. **LOW — residual unqualified "7 of 7" sibling of routed defect 1.** `PROVINCE.md:26` (§ Frontier, first bullet) still reads "round 51: the per-client overlap levers moved to Core — **7 of 7 clients** document a non-wording removal lever" with no qualifier naming the declared result. The literal claim is true post-correction (all seven SKILL.md rows do document a lever, head counter `7 of 7`), so it is not the verbatim stale string the registry sweeps — but it is the same number as the superseded counter claim, in the same file one screen below the corrected line, and a reader of § Frontier still meets an unqualified `7 of 7`. Either qualify it or accept it deliberately; recommend a qualifier since the routed defect's substance was "the number without its declared counterpart".
2. **LOW — the M36 sweep registry is literal-string narrow.** `verifiers/check_correction_sweep.py:32` `r51-c2-province` `stale` pattern is the exact phrase `overlap levers backed 7 of 7 clients`, so finding 1's rephrased "7 of 7 clients document" is invisible to the fix for M36. The check does what its docstring claims (red at `c8579a4c` with 3 fails, green at `c8407a45` — verified, exits 1/0) and the docstring scopes rows as "a new superseded claim is added as a new registry row", so this is a coverage limitation, not a bug — but the same class of miss that produced M36 (a sweep keyed to one spelling) survives in the fix's design.
3. **LOW — stale line pointer in the round-52 lesson.** `corpus/lessons/round-52.md:71` says the README correction was "appended inside the same bullet (`:144-153`)". At `c8407a45` the correction occupies `corpus/README.md:158-167`; :144-153 falls inside the Round-50/Round-51 append-only notes. Small M36-adjacent pointer rot inside the same commit (both files landed in `c8407a4`), worth a one-line erratum.

## Verification performed (commands + exit codes, all observed)

- `python3 -B verifiers/check_correction_sweep.py --rev c8407a45…` → `correction sweep: 0 stale block(s)`, exit 0; `--rev c8579a4c…` → three `FAIL` lines (readme, scorecard-lead, province), exit 1. The M36 fix is red-then-green as claimed.
- Frozen counter `git show 7c81a787:verifiers/check_overlap_levers.py` run from `verifiers/` inside the scratch clone (the script's `--rev` resolves `Path(__file__).parent.parent`, so it must sit under a repo's `verifiers/` — running it from `/tmp` makes every rev print "SKILL.md table absent", a footgun worth noting for the other falsify seats):
  - `--rev 43ca0bfb…` → `0 of 7`, exit 1
  - `--rev 34cfffbb` → `4 of 7`, exit 1 (SDK/Gemini `effect not allowed ('removed in a scope')`; opencode `entry quote malformed`)
  - `--rev c8579a4c…` → `4 of 7`, exit 1 (identical reasons)
- Widened counter `git show 34cfffbb:…` at `--rev 34cfffbb` → `7 of 7`, exit 0. Head counter at `--rev c8579a4c` → `7 of 7`, exit 0.
- `git diff c8579a4c c8407a45 -- verifiers/check_overlap_levers.py` → empty (counter untouched this round).
- `git status --porcelain` → ` M SCORECARD.md`, `?? .ufo/waves/round-52/` (the inherited uncommitted edit and this wave's reports).

## Out-of-scope note for the L1

The uncommitted `git diff -- SCORECARD.md` (attempt-1 leftover) does **not** touch the depth row — it appears only as unchanged context. The diff prepends a round-52 lead to the coverage and freshness cells and appends a "Round 52 completed" paragraph plus two `| 52 |` ledger rows (`SCORECARD.md` working tree :128-131, :264-265). Its claims (`5 of 7` @ `c8407a45`, `4 of 4` @ `c2107ecf`, `--fetch` 5 of 5) match the C1/C2 counters as reported in the context, and seat `ReviewScorecardLeftover` owns it; flagged here only so the in-place question above is not read as covering uncommitted hunks it doesn't contain.

## Residual risk / gaps

- `--fetch` claims (7 of 7 live quotes at 15:10:48Z; the uncommitted `5 of 5`) not re-run; rested on prior seat records.
- The README Core correction's per-lever list matches SKILL.md, but I did not re-open the seven source pages; wording provenance rests on the round-51 records (`ReviewReviewedList.md`, `CriticC2Landed.md`, `CriticLeverSemantics.md`).
- `corpus/lessons/round-51-verifier-spotcheck.md` itself is a closure artifact (never edited by the lane); not scored.
- No installs; tools: system `python3` (3.x, `-B`), `git`. No network use.
