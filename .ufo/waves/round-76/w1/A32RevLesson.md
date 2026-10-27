# A32RevLesson — round-76 lesson-draft completeness review

verdict: PASS-WITH-FINDINGS — all four required elements present in `build/lesson-draft.md`; one unresolved receipt-content conflict and one stale cross-reference must be fixed before landing.

Seat: reviewer, leaf. Reviewed artifact: `.ufo/waves/round-76/build/lesson-draft.md` (drafted by
B17LessonScribe, ~221 lines at review time; reviewed the current bytes — the draft was revised twice
during this review and each revision landed a fix, so the findings below are against the latest text).

## Checklist verdict

| required piece | present | verified |
|---|---|---|
| Gate with ≥1 admit | YES — S213 description-writing rules admitted at r74 guide-advice level | `plans/round-76.md` § C1; `corpus/knowledge/spec-skill-creation-craft-round74.md` precedent named in-text |
| Gate with ≥1 reject | YES — two: (a) held: eval-fidelity claim (no held-out experiment exists in the lane); (b) refused: staged `S231`/`spec-description-trigger-discipline.md` (rule-1 scope mismatch, re-grounded from this round's own snapshot) | r75 spot-check §4 agreed the same hold; refusal reason is an observed scope mismatch, not an assertion about what the source lacks |
| reject grounded in observed fact (Q62) | YES — both rejects name observed facts (absence of any experiment; the staged row's 2026-10-23 opening vs `CORPUS.md` rule 1 + byte-identical in-round re-open) | `corpus/QUALITY.md:78` (Q62); `w1/A24ScoutFresh.md` cmp exit 0 |
| S213 re-open record (URL, access date 2026-10-27, ≤25-word located quote) | YES — URL + `fetched_at` 2026-10-27T16:57:56Z HTTP 200 + quote at line 28 (10 words) | verified below |
| mistakes rows, all four fields | YES — 6 rows, each `class \| evidence pointer \| captured-by \| fix` (the r75 4-column shape) | rows M76-1 … M76-6 |
| routed-defect dispositions | YES — R1–R4 each with a disposition; D1 (landed r75), D2–D4 (landed), D5 (conditional, not landed); forward F1; F2 closed by `plans/round-76-addendum-1.md` | spot-check §6 R1–R4; plan § Trigger D1–D5 |
| status changes old→new | YES — S213 `used-by` old→new cells verbatim; "no other cell changes" stated; r75 Gate reject reversal logged | committed S213 row verified below |

## Verified facts (my own commands, run at review time)

- `wc -c -l snapshots/optimizing-descriptions.md` → `196 13403` (matches the draft's "13,403 bytes, 196 lines").
- `sha256sum` → `7cc54fbb…bfd837` = the MANIFEST line for `optimizing-descriptions.md` exactly.
- `sed -n '5p;21p;28p'` → line 5 `# Optimizing skill descriptions` (first heading), line 21 `## Writing effective descriptions`, line 28 contains the quoted phrase.
- `grep -cF 'A few sentences to a short paragraph is usually right'` → optimizing-descriptions **1**, evaluating-skills **0**, best-practices **0** (page-unique; last command exits 1 on a zero count — that is the check succeeding, not failing).
- quote word count `wc -w` → **10** ≤ 25. `snapshots/fetch-record.json` → HTTP 200, 13,403 B, `fetched_at` 2026-10-27T16:57:56Z — all match the draft.
- `git show b7f13f4…:SKILL.md | python3 -c '…yaml.safe_load…'` → `clip 1022 stripped 1021 first_sentence 151` (exit 0) — my own recompute, agrees with the draft's Gate self-audit numbers and with `build/B08-verify.txt` §7.
- committed S213 row (`corpus/SOURCES.md:153`): `used-by` = `corpus/knowledge/skill-eval-artefacts-round70.md`; `status` mined; `opened` 2026-10-25; `recheck` 90d — the draft's "old" value and unchanged cells are accurate.
- `w1/A11MutRedBefore.md` confirms `exit 2` ×4 + INCONCLUSIVE (grounds the `vacuous` row, M76-3 by position).
- `w1/A24ScoutFresh.md` row for optimizing-descriptions: same sha256 vs r70/r74 snapshots, `cmp` exit 0 — grounds the Gate freshness sentence.
- Freeze discipline clean: `corpus/lessons/round-76.md` absent from the lane tree; draft lives only under `build/`.

## Findings (severity ordered)

**HIGH — R2 receipt first-line conflict is resolved in the draft but not reconciled with the frozen no-harm clause.**
`plans/round-76.md` § C2 R2: "receipt `.ufo/waves/round-76/receipts/noharm-at-tip.txt` names the tip
revision on its first line"; § No-harm battery: "receipt `.ufo/waves/round-76/receipts/noharm-at-tip.txt`
names the final tip". The draft's R2 disposition picks the r75 tip (`b7f13f4…`) for the first line and
explicitly says "not the r76 judged tip" — which leaves the frozen "names the final tip" clause
unaddressed (scorecard-draft mirrors the final-tip reading; log-draft's placeholder table flags
`<tip-rev>`). One file cannot satisfy both first-line clauses after round 76 lands. Fix options: the
receipt carries both named revisions (first line per the counter's chosen arm + an explicit
final-tip line for the battery) with the counter arm stating which line it reads, or an addendum
names a second receipt path. The draft should state the collision instead of silently picking a side.

**MEDIUM — stale cross-reference to the entry draft.**
Gate: "The entry … carries eight such located quotes (§ The admitted rules) and the two-sided
illustration at `:179`–`:190`". Current `build/entry-draft.md` has no section "The admitted rules"
(sections are the quote table, `## This lane's own description, measured`, `## What this entry does
not claim (Q62)`, `## Limits`, `## Related`), is ~110 lines so `:179`–`:190` does not exist, and
carries 5 quote-table rows plus a 9-token recheck sweep — "eight" matches neither. Either the entry
restores that section/count or the lesson cites the entry's actual quote table and § measure.

**LOW — mistake-row ids implicit for rows 2–4.**
`M76-3` (Round honesty bullet) and `M76-4` (routed-forward F1) are cited by id, but rows 2–4 of the
Mistakes table carry no in-cell id (`number-drift`, `vacuous`, `reference-drift`); the mapping is by
row position only. Add `M76-2`/`M76-3`/`M76-4` to those class cells to match M76-1/M76-5/M76-6.

**LOW — "five printed lengths" should be six.**
M76-1's evidence cell says B21's "`372` mis-sums its own five printed lengths". B21's row prints six
lengths `14,76,78,73,79,72` (sum 392; the five content-line lengths sum 378; `372` matches neither).
Direction is right; the count is off — say "six printed lengths" or drop the parenthetical.

**LOW — committed dispatch files do not match the live wave for this seat pair.**
`w1-dispatch.json`/`w1-spec.json` assign the lesson-draft task to `B16ProseRead`; the live wave
dispatched it to `B17LessonScribe` (live B16 received the prose-read prompt). Same
spec-vs-results reconciliation family as R3; worth one sentence in Round honesty or routed-forward if
the committed spec files are the wave's record.

**INFO — forward-tense dispositions.**
At review time `verifiers/check_desc_craft.py` and `verifiers/check_r75_routed_repairs.py` are absent
from the lane tree and `receipts/` holds `checklist-base.txt`, `tip-battery.sh`,
`description-audit-4de12b61….txt`, `receipt-revs.txt`, `fetch-recheck.txt`, `census-before.txt`,
`d4-selftests.txt` — no `r1-folded-render.txt`, `noharm-at-tip.txt`, or control receipts yet. The
draft's "closed" dispositions and the fourth digest pin (the counter's in-file table) are post-landing
assertions; the header comment already discloses that landed state is recorded in `w1/B17LessonScribe.md`.
If any named artifact fails to land, the corresponding "closed" becomes false — integration check.

## Residual risk / verification gaps

- I did not run the frozen counters (absent from the tree); nothing in this review implies a counter result.
- The entry's audit verdicts (met/partial/not-met cells) were checked for internal consistency against the lesson's summary only; quote-verbatim coverage belongs to A01RevQuoteLocate.
- D2/D3 landing drafts exist (`build/B10RepairD2D3.formA.patch` / `.formB.patch`) and D4's receipt exists (`receipts/d4-selftests.txt`); whether the dispositions' exact landed wording matches the drafts is an integration-time check, not covered here.
- No installs, no subagents, no scratch created (read-only `git show`, `sha256sum`, `wc`, `grep`, `sed`); three background `bash` jobs exited 0/0/1 (the 1 is the expected zero-count grep). No git/jj writes, no lane mutation.
