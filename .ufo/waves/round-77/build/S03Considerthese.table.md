# S03Considerthese — considerthese disposition table (round 77, w1)

Read-only input: `considerthese/2026-10-26.md` (latest), earlier files 10-22…10-25, 10-19…10-21 skimmed for carried items.
Lane HEAD `6523aced1ee0ebe07dca996213bdc645a6acbd1e` (r77 freeze). All paths are relative to
`/home/vgpnk/Projects/shokunin/kotoba-shokunin` unless prefixed `FLEET:` (= `/home/vgpnk/Projects/shokunin`).
Every `file:line` below was opened in this seat; nothing here is taken from a summary.

Measured at HEAD (this seat, committed bytes): `SKILL.md` 590 lines, 78,647 B (`wc -lc`), 147 lines >120 chars, 77 >300, longest 1,095;
`## Gate registry` = `SKILL.md:445-513`, 24,897 B (~31.7 %); frontmatter description folded render 1,022 chars (1,021 stripped),
first sentence 151 chars (PyYAML `safe_load` + first-period cut). The 10-26 numbers are therefore still current (proposal 3 premise holds;
proposal 1's 78,569 B is 78 B stale).

## A. The five self-improvement proposals of 2026-10-26 (`considerthese/2026-10-26.md:15-19`)

| # | Proposal (line) | Status at r77 HEAD | Where the disposition lives (resolves?) | r77 can mine as the one allowed item? |
|---|---|---|---|---|
| 1 | Byte ceiling (≤70 KB, ratchet) + 200-char max-line check in floors guard (`:15`) | **Declined r76, not implemented.** SKILL.md grew 70,606 → 78,647 B since 10-25; the C1 act-on row (r76 draft: +3 lines → 593, `.ufo/waves/round-76/build/skill-patch.md:7`) will add bytes again | Reason (600-line box is a checklist budget pinned per box in `verifiers/checklist-baseline.json`; replacing it = baseline-map change + own claim): `plans/round-76.md:11` ✔; draft Gate `.ufo/waves/round-76/build/lesson-draft.md:91-95` ✔ (draft). Non-author closure marks it "agree-with-caveat — written only in the plan, not in a lesson Gate": `corpus/lessons/round-76-verifier-spotcheck.md:64` ✔. **`corpus/lessons/round-76.md` does not exist at HEAD** (`ls` → no such file), so the plan's "recorded in the round-76 lesson Gate" pointer is dead until R76-D2 lands it (`corpus/lessons/round-76-verifier-spotcheck.md:80`). | **No.** Widens the frozen claims (new gate = new claim; floors registry + checklist baseline touch). Keep declined; disclose that C1's row makes the byte metric worse. |
| 2 | Move `## Gate registry` to `verifiers/REGISTRY.md` (`:16`) | **Declined (L0 question), not implemented.** Section still at `SKILL.md:445` | `corpus/QUALITY.md:83` (Q67) ✔; `FLEET:.ufo/l0-questions.md:174` (kotoba \| round-73 question) ✔; `FLEET:PROTOCOL.md:398` ("registry home is its own SKILL.md") and `:418-421` (closure grades no gate conformant without a row at the registry home) ✔; `plans/round-73-addendum-1.md:14-17` ✔; r76 draft `lesson-draft.md:96-98` ✔; closure agrees: `corpus/lessons/round-76-verifier-spotcheck.md:63` ✔. Best-resolved of the five. | **No.** Protocol-named home; L0 decides, not a round. |
| 3 | Land the r74-rejected description page and audit kotoba's own description against it (`:17`) | **Mined r76 (C1) — no data landed** (honest stop: `plans/round-77.md:8`); re-mined r77 as C1 (`plans/round-77.md:11`). At HEAD: no `corpus/knowledge/description-craft-round76.md`, no `check_desc_craft.py` data pass (base `0 of 6`). | `plans/round-76.md:11,20`; `plans/round-77.md:11,22-32`; closure verdict "mined as C1 candidate": `corpus/lessons/round-76-verifier-spotcheck.md:62`; r74 reject was a W04 duplicate-URL/flip-state call, not an advice-inadmissibility ruling (same row, citing `corpus/lessons/round-74-verifier-spotcheck.md:116`). Prior mining attempts on the same theme: r68 `corpus/lessons/round-68.md:122-126`, r69 `corpus/lessons/round-69.md:129-131`, r70 `corpus/lessons/round-70.md:219-229`, r73 withdrawn `plans/round-73-addendum-1.md:21-33` + `corpus/lessons/round-73.md:69-70`. | **Already the allowed item** (C1's motivation). Scope note: C1 conjunct (d) *audits* length/first sentence and records the numbers; it does not rewrite the description, and the "omp 99-char render cliff" is not on the S213 page (`lesson-draft.md:84-87` (line 87)). The proposal's second clause ("close both") is only half met by an audit table. |
| 4 | "Provisional" close until the falsify wave (or non-author mutation battery) runs (`:18`) | **Declined r76 as procedure; not codified.** r77's own shape practises it informally: data lands after w1, SCORECARD/LOG/QUALITY rows only after w2 (`plans/round-77.md:52-53,56-57` Landing order step 4). r73 and r74 did close with w2 undispatched: `corpus/lessons/round-73.md:100`, `corpus/lessons/round-74.md:113`. | `plans/round-76.md:11` ✔ ("procedure"); r76 draft `lesson-draft.md:100-101` ✔. **Draft defect:** it argues "this round's v2 band puts 22 of 64 seats on attack (34.4%) … inside the one wave, so a 'wave 2 pending' state does not arise" — true for r76's single wave, **false for r77** (two v1 waves, `plans/round-77.md:50-53`), so r77's lesson must not copy the sentence; the 22/64 figure is the corrected taxonomy (`lesson-draft.md:121` M76-6), the plan's 53 % / 34-attack sentence (`plans/round-76.md:64`) is the superseded one. | **Not as a rule or claim** (closure procedure, no counter). Cheapest honest handling: one sentence in the r77 lesson Gate recording that r77 withdraws no SCORECARD row until w2 settles, labelled *practised, not adopted*. No new file, no new gate. |
| 5 | Evidence budget: per-round cap or compression of seat logs (`:19`) | **Declined (operator-level), not implemented.** `.ufo/` is 202 MB at HEAD (`du -sh .ufo`; proposal says 203 MB) | r76 draft `lesson-draft.md:102-103` ✔ (draft only); `plans/round-76.md:11` ✔ ("operator-level"). Older ancestors: `considerthese/2026-10-21.md:32-34` (`.ufo` 122 M, no gate) and 10-20 "evidence-budget watch" (`considerthese/2026-10-21.md:40`). No QUALITY row or L0 question names it (grep of `corpus/QUALITY.md`, `FLEET:.ufo/l0-questions.md` for "evidence budget/cap" → none). | **No.** Fleet policy; a lane cannot cap fleet evidence. If wanted, route as an L0 question line — a parent-owned file, not a seat write. |

## B. Hit-rate ledger item (`considerthese/2026-10-26.md:21`, "2 of 5 of yesterday's … 5 of 13")

- r77 may state, from committed bytes: of the five 10-26 proposals, **0 implemented**, 1 mined twice (3; data pending), 4 declined with reasons (reasons live in the plan and a *draft*, one file short of resolving). Source for the previous ledger: `considerthese/2026-10-26.md:21`.

## C. Carried-forward open items from earlier files (not in the latest file; for completeness)

| File:line | Item | Status at HEAD |
|---|---|---|
| `considerthese/2026-10-25.md:19` | byte ceiling + max-line (= 10-26 #1) | open/declined as A.1 |
| `considerthese/2026-10-25.md:20` | registry out of SKILL.md (= 10-26 #2) | L0 question, A.2 |
| `considerthese/2026-10-25.md:21` | route entries' author bullets into audit checklist | worked r72 (`corpus/lessons/round-72.md:65-67`) — implemented |
| `considerthese/2026-10-25.md:22` | intro frame "two harnesses" | implemented r72/r74 (`SKILL.md:21-23` now "two harnesses this lane can observe … 11 clients"; `corpus/lessons/round-74.md:72`) |
| `considerthese/2026-10-25.md:23`, `2026-10-24.md:41`, `2026-10-23.md:29` | description self-audit | = 10-26 #3 (C1, pending) |
| `considerthese/2026-10-24.md:31` | every round carries a reader-facing claim | C1's SKILL.md § Body craft row would be one; unlanded |
| `considerthese/2026-10-24.md:35` | reader diff (SKILL.md changed lines) in each reflection | open, operator/bot-side |
| `considerthese/2026-10-23.md:31` | client × surface coverage grid (tool/permission allowlists, settings precedence, skill-vs-command collision) | open frontier rows, not widened-in |
| `considerthese/2026-10-23.md:33` | per-axis "last landed claim" line | open, bot-side |
| `considerthese/2026-10-22.md:27` | root `STATUS.json` | ignored |
| `considerthese/2026-10-22.md:29` | fresh non-author cold-routing run (SHONEN box 3) | open |

## D. Verdict for round 77

1. The one allowed considerthese item is proposal 3 = C1; it is not widened by anything in this table. 1/2/4/5 stay declined with the r76 reasons.
2. **Pointer repair r77 needs (hygiene, already routed as R76-D2):** write `corpus/lessons/round-76.md` `## Gate` so that proposals 1/2/4/5's reasons resolve to a committed lesson; the r76 draft `lesson-draft.md:89-103` (item 4 at :99-101) is usable for 1, 2, 5 as written but the proposal-4 clause (`:100-101`) must be re-worded because it hard-codes "the one wave".
3. Do not claim any 10-26 proposal as "implemented" in r77 reports: at HEAD none is. After C1 lands, proposal 3 is "mined and (audit-half) implemented; description text unchanged (1,022 / first sentence 151)".
4. Disclose, not fix: C1's act-on row increases SKILL.md bytes/lines (590 → ≈593 per the r76 draft) so proposal 1's metric moves the wrong way for the 5th consecutive round.
