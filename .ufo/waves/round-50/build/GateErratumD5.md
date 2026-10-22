# GateErratumD5 — routed defect D5: round-49 reject ledger + round-50 `## Gate` template

HOLDS-BOUNDED — applies to `corpus/lessons/round-49.md` § Gate (lines 21–24), which records "rejected 0"
while round 49 rejected 16 items; the drafts below are integration-ready text for the round-50 lesson,
not an edit to the round-49 lesson (append-only, owned by its round).

Seat `KotobaR50.GateErratumD5` (scribe, leaf, no dispatch). Lane read-only except this report.
Base `f30464660c675d1c1e2851a3bf0366a3aaffe5a8`, 2026-10-22. Tools installed/upgraded: none. No web
source opened; no sibling repo written; no jj; no git write in any lane.

## 1. The defect

`corpus/lessons/round-49.md:21-24`: "**Knowledge entries:** candidates 1, admitted 1
(`corpus/knowledge/sibling-overlap-census-round49.md`), rejected 0." That line scoped itself to
knowledge entries, where "rejected 0" is literally true. As the round's gate record it is false: the
round rejected a clause, overrode a seat call, re-classified two rows, re-sized two counters and
dropped one declared commitment, and none reached a reject line. The non-author closure named this D5
(`corpus/lessons/round-49-verifier-spotcheck.md:231`) and wrote its own reject samples outside the
lesson (`:169-176`), because the lesson has no reject line to sample. Rules the drafts obey:
`corpus/QUALITY.md:38-39` (rejections recorded in the lesson's `## Gate` with their reason; a
rejection is evidence of taste); `CORPUS.md:19-20` (candidates, admitted, rejected with reasons,
spot-check result); the round-49 falsify finding that the Gate has no `spot-check result` line
(`.ufo/waves/round-49/falsify/ReviewLessonQ25.md:44-52`, gap (a)).

## 2. Draft (a) — erratum block for the round-50 lesson

Append to `corpus/lessons/round-50.md` (it does not exist at `f30464660c…`; its `## Mistakes` section is
another seat's file, so this is drafted text for that seat or the L1 to splice in).

```markdown
### Erratum: the round-49 Gate recorded "rejected 0" (routed defect D5)

`corpus/lessons/round-49.md:21-24` reads "candidates 1, admitted 1, rejected 0". That line scoped
itself to knowledge entries, where "rejected 0" is literally true. As the round's gate record it is
false: round 49 rejected the items below, and a rejection is evidence of taste
(`corpus/QUALITY.md:38-39`). The round-49 lesson is append-only and owned by its round, so the
erratum lives here. Each item names what was rejected, the reason, and an evidence pointer.

| # | rejected | reason | evidence |
|---|---|---|---|
| 1 | the kasegi "prompt-injection exploits" clause | kasegi's tree never held it (`git grep` exit 1; `git log -S` empty) | `corpus/knowledge/sibling-overlap-census-round49.md:111-115`; `.ufo/waves/round-49/build/CensusKasegi.md:26-31` |
| 2 | kengaku's "route telemetry" clause | the sibling marks that surface ABSENT since 2026-10-15; the note copied the stale half | `.ufo/waves/round-49/falsify/RowKengaku.md:11-15` |
| 3 | mado's "no claim on kotoba ground" | mado surveys the omarchy skill file's frontmatter as its own surface | `.ufo/waves/round-49/falsify/RowMado.md:17` |
| 4 | kama's misquoted split | the quote dropped "agent" and "fallback" | `.ufo/waves/round-49/falsify/RowKama.md:29` |
| 5 | chousa's MINT.md "Rejected recipients" reading | the stated reason ("none is a scope surface") is wrong; MINT.md is a committed boundary record | `.ufo/waves/round-49/falsify/RowChousa.md:37` |
| 6 | kotodama's seat call `none` | overridden to `adjacent`: its description refuses kotoba's craft by name and `MINT.md:20` records the name collision | `corpus/knowledge/sibling-overlap-census-round49.md:60-63`; `.ufo/waves/round-49/build/CensusKotodama.md:19,30` |
| 7 | kake and kasegi's first-landing `none` | the rule's "either side" arm: kotoba's own description states the split (7 → 9 adjacent) | `corpus/knowledge/sibling-overlap-census-round49.md:143-149`; `.ufo/waves/round-49/falsify/CriticC1Landed.md:19,32` |
| 8 | tameshi's cited basis | the citation pointed at a wave report, an excluded surface; the row was re-based | `.ufo/waves/round-49/falsify/CriticC1Landed.md:26`; `.ufo/waves/round-49/falsify/RowTameshi.md:16` |
| 9 | tabi's `adjacent` | the split appears only in wave drafts; the row stays `none` | `corpus/knowledge/sibling-overlap-census-round49.md:54-55,171-176`; `.ufo/waves/round-49/falsify/RowTabi.md:23-26` |
| 10 | C1's name-count counter (10 → 20) | content-blind (CE1–CE4: a bare 20-name list also prints 20); re-sized to a classified, pinned row count | `plans/round-49.md:27-30,35-43`; `.ufo/waves/round-49/build/CriticC1Sizing.md:12,21-27`; `.ufo/waves/round-49/build/MineMistake.md:88-91` |
| 11 | C2's disposition-count counter (0 → 2) | content-blind (an unrelated instrument or a 10-byte stub still prints 2); re-sized to `boxes proven 2` | `plans/round-49.md:58-61,63-72`; `.ufo/waves/round-49/build/CriticC2Sizing.md:9-21`; `.ufo/waves/round-49/build/MineMistake.md:88-91` |
| 12 | M30's "the round-46 source does not carry the clause either" | false: that line carries the clause and mis-cites kasegi `PROVINCE.md:3-4`; the class and fix stand | `corpus/lessons/round-49.md:98-101`; `.ufo/waves/round-49/falsify/ReviewLessonQ25.md:12-19` |
| 13 | C2's "every per-conjunct mutant fails on its named conjunct" | the proof does not enforce its own coverage: removing the `d04-stem` case still prints `boxes proven 2` | `corpus/lessons/round-49.md:102-104`; `.ufo/waves/round-49/falsify/ReviewLessonQ25.md:20-29` |
| 14 | S022's "description alone" teaches cell | the page supports less than the cell claims; the cell was corrected | `.ufo/waves/round-49/falsify/ReopenS022.md:11-12` |
| 15 | the declared `dispatch.08` commitment ("executed … its live failures are findings") | the box was re-worded to a different authority before landing (`.round` → `.report-baseline`) and the plan never declared it; the old authority failed 166 of 289 prompts | `plans/round-49.md:76`; `.ufo/waves/round-49/falsify/CriticBoxReword.md:36`; `.ufo/waves/round-49/build/DispatchIndependent.md:25` |
| 16 | the round-48 entry's line 56 sweep and line 32 "24 probe fixtures" | the printed command gives 1 hit, not 0; no run list for 24 (21 of 23 reproduce) | `.ufo/waves/round-49/build/R4CountProvenance.md:14-21` |

Round 49 wrote no rejected source row: S022 and S023 were admitted and S018 stayed `mined`
(`corpus/lessons/round-49.md:39-40`); the registry's only `status=rejected` row is S011, rejected
2026-10-19. Carried, not rejected: the census guard's duplicate-row gap
(`corpus/lessons/round-49.md:105-106`), R5's unfrozen v2 oracle, R1's no-name fallback.
```

## 3. Notes on the ledger

- Items 1–5 are withdrawn lane-surface content; 6–9 are a seat call replaced or a seat's basis
  withdrawn; 10–11 are counters re-sized before any landing (a first declared counter is a rejected
  counter); 12–15 are statements the falsify wave overturned or bounded; 16 are round-48 counts that do
  not reproduce. Item 8's row (`tameshi`) kept its classification and changed only its basis; item 9's
  row (`tabi`) kept `none`. A rejected basis is still a reject decision. "Rejected 0" was true for
  source rows and false for the round; the two facts are recorded apart so neither is lost.

## 4. Draft (b) — the round-50 `## Gate` template

For `corpus/lessons/round-50.md`. Every line is mandatory; a line that cannot be filled says
"none — <sweep command> → <result>" rather than being dropped, so "rejected 0" can never again be the
whole record.

```markdown
## Gate

**Candidates (knowledge entries):** <N> — <how the candidate set was swept, with its command>.

**Admitted:** <N>
| entry | what it establishes | evidence pointer |
|---|---|---|
| `<path>` | <one clause> | `<path:line>` |

**Rejected:** <N> — a rejection is evidence of taste (`corpus/QUALITY.md:38-39`).
| rejected | reason | evidence pointer |
|---|---|---|
| <what was rejected> | <why it was rejected> | `<path:line>` |

**Source rows written this round** (each opened in this round; the seat report holds the full fetch
record): <N> — admitted <N>, rejected <N>. For each row: URL, accessed (UTC), a ≤25-word quote and its
location. A rejected row keeps its row with `status=rejected` and a `teaches` cell opening
`REJECTED: <reason>; flip: <what would change the verdict>`.

**Status changes logged old→new:** <each row id and the cell change, or "none">.

**Claims as declared, and any counter re-sized before landing:** for each claim, the first declared
counter, the reason it was rejected, and the counter that replaced it (with the critic seat that
attacked it).

**Seat calls overridden or re-based:** <lane, the seat's call, the call that replaced it, the reason,
the evidence pointer> — or "none".

**Carried items** (not rejects): <item, why it is carried, where it is routed>.

**Spot-check result (non-author):** <verdict, the seats that ran it, and every disagreement recorded
verbatim> — or "not yet run" with the dispatch that owes it.
```

Why each line is there: `candidates / admitted / rejected / spot-check result` is the `CORPUS.md:19-20`
minimum; admit and reject are separate lines so a rejection is never folded into an admit count
(`corpus/QUALITY.md:38-39`); the source-row ledger and the old→new log are `CORPUS.md` rules 1 and 2;
the counter-re-sizing and override lines exist because round 49's rejects lived exactly there; the
spot-check line exists because round 49's Gate had none (`ReviewLessonQ25.md:44-52`, gap (a)).

## 5. Out of scope

- The round-49 lesson was not edited (append-only, owned by its round); the erratum targets the
  round-50 lesson only. `corpus/lessons/round-50.md` was not created: it does not exist at
  `f30464660c…`, and its `## Mistakes` section is another seat's file.
- The census guard's duplicate-row gap, R5's unfrozen oracle, R1's no-name fallback and the D2/D3/D4
  wording work are other seats' files; named here only as carried items. No claim was re-measured and
  no verifier was executed: this seat read committed bytes only.

## 6. Evidence (commands run from the lane root; exit codes verbatim)

- `grep -n "rejected\|Rejected" corpus/lessons/round-49.md` → lines 22 and 27 only — no reject line
  (exit 0). `grep -n "^| S0" corpus/lessons/round-49.md` → lines 39, 40 (S022, S023 admitted) — no
  rejected row.
- `awk -F'|' '/^\|[[:space:]]*S[0-9]{3,}/ && NF==13 {s=$9; gsub(/^ +| +$/,"",s); if (s=="rejected")
  print $2}' corpus/SOURCES.md | wc -l` → `1` (S011, rejected 2026-10-19) — exit 0.
- `! sed -n '19,32p' corpus/lessons/round-49.md | grep -qi 'spot-check'` → exit 0 (no spot-check line).
  `grep -q "spot-check result" /home/vgpnk/Projects/shokunin/CORPUS.md` → exit 0;
  `grep -q "a rejection is" corpus/QUALITY.md` → exit 0 (`corpus/QUALITY.md:38`).
- `grep -q "D5 (gate record)" corpus/lessons/round-49-verifier-spotcheck.md` → exit 0 (line 231);
  `grep -q "reject (withdrawn as unsourced)"` → exit 0 (line 175); `grep -q "reject (falsify wave;
  reclassified"` → exit 0 (line 176).
- Existence checks for every cited pointer, all exit 0: census lines 54, 60, 111, 143, 147, 162, 168,
  171, 177, 182; lesson lines 21, 26, 39, 76, 98, 102, 105; plan lines 27, 35, 58, 63, 76; build seats
  `CensusKasegi.md:26`, `CensusKotodama.md:19,30`, `CensusChousa.md:39-41`, `CriticC1Sizing.md:12,21`,
  `CriticC2Sizing.md:9`, `MineMistake.md:88-91`, `R4CountProvenance.md:14,20,79`,
  `DispatchIndependent.md:25`, `PlanDataWalk.md:112`, `DispatchInstrument.md:145`; falsify seats
  `CriticC1Landed.md:19,26,32`, `ReviewLessonQ25.md:12,20,44`, `MutDispatchInstrument.md:44`,
  `RowTameshi.md:16,73`, `RowTabi.md:23`, `RowMado.md:17`, `RowKama.md:29`, `RowKengaku.md:11`,
  `RowChousa.md:37`, `ReopenS022.md:11`, `CriticBoxReword.md:36`.
- `git -C <lane> status --porcelain` → `?? .ufo/waves/round-50/` (this report), `?? plans/round-50.md`
  and ` M verifiers/verify_skill_checklist.py` (other seats' files, untouched by me); `git diff --stat
  HEAD -- corpus/` → empty, so the round-49 lesson and the corpus are unmodified by this seat.
