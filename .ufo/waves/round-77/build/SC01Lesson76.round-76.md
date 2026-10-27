---
author: kotoba (round-77 w1 seat SC01Lesson76, writing the round-76 lesson)
date: 2026-10-27
round: 76
lane: kotoba
---

# Round 76 lessons — kotoba

**This is the round-76 lesson, written in round 77.** Round 76 closed as an honest stop and never wrote this file; the
non-author closure routed it as **R76-D2** (`corpus/lessons/round-76-verifier-spotcheck.md` §5, defect CD2 in §1). It is
written here because C1 conjunct (a) and conjunct (e) read it (`verifiers/check_desc_craft.py`), and because a round whose
Gate and Mistakes exist only in a `.ufo` draft has no rejection it can keep. Every number below names the revision it was
measured at; nothing here is a round-77 claim, and no axis moves with this file.

Round 76 froze two counters at `ec7f853` — `verifiers/check_desc_craft.py` (`description craft backed K of 6`) and
`verifiers/check_r75_routed_repairs.py` (`r75 routed repairs closed 4 of 4`) — and landed **no claim data**. At the
round-76 tip `6ce2724` the frozen counters read `description craft backed 0 of 6`, exit 1
(`.ufo/waves/round-76/receipts/c1-base-final.txt`) and `r75 routed repairs closed 0 of 4`, exit 1
(`.ufo/waves/round-76/receipts/c2-base-final.txt`); `git diff --stat b7f13f4 6ce2724 -- SKILL.md corpus/` prints nothing,
so no `SKILL.md`, `corpus/knowledge/`, `corpus/SOURCES.md`, `corpus/QUALITY.md` or lesson byte moved between the r75 tip
and the r76 tip. The same two red reads reproduce at the round-77 base `2f675548` on the unchanged counter bytes
(`.ufo/waves/round-77/receipts/c1-base-2f675548eaad2a037a899d39247c1fd7a88aaf48.txt`,
`.ufo/waves/round-77/receipts/c2-base-2f675548eaad2a037a899d39247c1fd7a88aaf48.txt`), which is why round 77 re-lands
both claims.

## Gate

**S213 access record — re-opened 2026-10-27 (row written 2026-10-25).** `https://agentskills.io/skill-creation/optimizing-descriptions.md`,
registry row `corpus/SOURCES.md:153`. Committed snapshot `.ufo/waves/round-76/snapshots/optimizing-descriptions.md`:
13,403 bytes, 196 lines, sha256 `7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837`. That digest is pinned
a fourth time beside `snapshots/MANIFEST.sha256:1`, `snapshots/fetch-record.json` (HTTP 200, `fetched_at`
`2026-10-27T16:57:56Z`, 13,403 bytes) and the digest table inside `verifiers/check_desc_craft.py`. **Access date:
2026-10-27** — the date the fetch record carries. Three independent re-opens this round agree byte for byte:
`S01Reopen1` (curl, start 2026-10-27T19:44:56Z) and `S02Reopen2` (urllib, server `Date` 19:45:20 GMT), recorded at
`.ufo/waves/round-77/build/S01Reopen1.access-record.txt` and `.../S02Reopen2.access-record.txt`, and this seat's own fetch
(HTTP 200, 13,403 bytes, 196 lines, same sha256). The page has not moved; C1 is not blocked by source drift.

**Located quote (10 words, ≤ 25).** "A few sentences to a short paragraph is usually right" —
`.ufo/waves/round-76/snapshots/optimizing-descriptions.md:28`, after the page's first heading (line 5), inside § Writing
effective descriptions (heading line 21). `grep -F -c` over the three snapshots returns 1 / 0 / 0: the line occurs in the
optimizing-descriptions body and in neither `evaluating-skills.md` nor `best-practices.md`, so it is page-unique content
and not site chrome.

**Admit.** The page's four description-writing rules — imperative phrasing, user intent over mechanics, deliberate
breadth that names contexts the user never names, and length under the specification's 1024-character ceiling — are
admitted at the same guide-advice level round 74 used for the same guide set (`S223`–`S225`,
`corpus/knowledge/spec-skill-creation-craft-round74.md`): documentary evidence from the format's own maintainers, no agent
client run, no trigger-rate claim. They are acted on in `SKILL.md` § Body craft (one rule row citing the entry and S213,
carrying quote fragments that occur verbatim in this snapshot) and turned on the lane's own `description`: at
`2f675548` the folded render is **1022 characters clip / 1021 stripped** with a **151-character first sentence**, printed
by the counter's own `description_measures` under the convention pinned in `plans/round-76-addendum-1.md`
§ Render-length convention. The per-rule grading of that field lives in the entry's audit table, where conjunct (d)
recomputes it; it is not restated here.

**Reject (held).** Any claim that this page's trigger-rate protocol is evidence that kotoba's description triggers
reliably. Its 20-query × 3-run loop, its 0.5 threshold and its train/validation split are instructions to run, not a run;
no held-out query experiment exists in this lane, so the round-75 Gate hold stands and the entry carries it as a limit.

**Reject (refused).** The staged package entry `spec-description-trigger-discipline.md` (package
`/home/vgpnk/Projects/shokuknow/merge/kotoba/`, staged row `S231`) as a citable artifact. It rests on this same page and
carries the package's 2026-10-23 opening; fleet `CORPUS.md` rule 1 requires the source to be opened in the round that
writes the row. The page was opened directly this round with its own snapshot, fetch record and three independent
fetches, so the entry is written from this round's bytes and nothing is adopted from the package.

**Reversed.** The round-75 Gate's reject candidate — "any claim that the 1021-character description size … remains
current; current frontmatter is materially shorter" — is false. The folded render is 1022 clip / 1021 stripped over the
`description` block, and it is unchanged at `65a5c7a`, `ac9f295`, `b7f13f4b`, `4de12b61` and `2f675548`; the r75 `awk`
window `NR>=3&&NR<=8` read six source lines whose lengths are 14, 76, 78, 73, 79, 72 (392 of 1022 rendered characters),
not the value. The superseded row text is named, not rewritten (M76-1 below).

**Candidates from `considerthese/2026-10-26.md` (proposals 1–5).** **Proposal 3 is taken** — admit the
optimizing-descriptions page and then audit the lane's own `description` against it; both halves are this round's C1
motivation, and the closure re-opened the source and agreed. **Proposals 1, 2, 4 and 5 are declined**, each for a reason
of contract, not a judgement that it is wrong: **1** (byte ceiling plus a 200-character line check) replaces a
checklist-executed budget whose box text is sha256-pinned per box in `verifiers/checklist-baseline.json` and executed by
`verify_skill_checklist.py` — a baseline-map change that needs its own claim and is outside this round's touch list;
**2** (move `## Gate registry` to `verifiers/REGISTRY.md`) is an L0 question, not a claim, per Q67
(`corpus/QUALITY.md:83`) because `SKILL.md` is the protocol-named registry home; **4** (close a round "provisional" until
its falsify wave runs) is closure procedure owned by the protocol and scorecard, and round 76 ran one v2 wave with the
attack seats inside it; **5** (a per-round evidence cap / `.ufo` compression) is operator-level fleet policy over the
working tree, which a lane cannot set from inside a round's claim surface.

**Assimilation: none.** The only staged artifact on this theme is refused above as a staged artifact and re-grounded
in-round, so no `SOURCES.append.md` row, no entry and no renumber map is imported by this round.

## Spot-check

Carried from `corpus/lessons/round-76-verifier-spotcheck.md` §3 as recorded there; the decisions are **not re-judged
here**. That spot-check sampled the round's gate-level decisions in `plans/round-76.md` and the lane report because no
lane `## Gate` existed at the tip (its CD2).

| Item | Decision | Re-opened source (as recorded) | Agree? | Reason (as recorded) |
|---|---|---|---|---|
| considerthese proposal 3 | mined as C1 candidate (admit-for-claim; nothing admitted into knowledge at that point) | `considerthese/2026-10-26.md:17`; `corpus/lessons/round-74-verifier-spotcheck.md:116`; live fetch 13,403 B, sha256 `7cc54fbb…` | agree | page resolves and the byte count and digest prefix match the S213 pin; the r74 reject was a W04 duplicate-URL/flip-state call, not a ruling that the advice is inadmissible |
| considerthese proposal 2 | declined | `corpus/QUALITY.md:83` (Q67); fleet `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md:174` (the spot-check wrote it lane-relative, where no such file exists); `SKILL.md` still carries `## Gate registry` | agree | Q67 and the filed L0 question confirm the protocol makes `SKILL.md` the registry home; relocating it is an L0 question |
| considerthese proposal 1 | declined | `SKILL.md` at the tip: `wc -lc` → 590 lines, 78,647 B (the proposal cites 78,569 B) | agree-with-caveat | the size observation resolves; the decline reason is sound but at that point was written only in the plan, not in a lesson Gate |
| newly written SOURCES row | n/a | `corpus/SOURCES.md` unchanged (151 rows at base and tip); row S213 re-opened instead, its quote 17 words and verbatim on the live page | — | the lane wrote no new row |

## Mistakes

| class | evidence pointer | captured-by | fix |
|---|---|---|---|
| M76-1 · `number-drift` | `corpus/lessons/round-75.md:11` measured the description with `awk 'NR>=3&&NR<=8'` and `:5` of that lesson rejected the imported 1,021 on that reading. That window is 6 of the block's source lines: at `2f675548` their lengths are 14, 76, 78, 73, 79, 72 (`git show 2f675548:SKILL.md \| awk 'NR>=3&&NR<=8{print length($0)}'`), 392 of a 1022-character render. | none at r75 — Q54/Q60 pin a reproducible count at a revision, not the measurement unit against the artefact's own parse unit; the error was found in r76 by seat `B21RevMethod` (`.ufo/waves/round-76/w1/B21RevMethod.md` §2–§4). | `plans/round-76-addendum-1.md` § Render-length convention fixes clip 1022 (stripped 1021) and requires both printed beside every receipt; the frozen counters print both. No general criterion landed: `corpus/QUALITY.md` at `2f675548` ends at Q73 and the r76 build's promised Q74 row (`.ufo/waves/round-76/build/B08-q74-quality-row.diff`) is not in the tree. |
| M76-3 · `vacuous` | `.ufo/waves/round-76/w1/A11MutRedBefore.md`: the red-before probe ran `python3 -B verifiers/check_desc_craft.py …` from a checkout where the file does not exist — `can't open file .../verifiers/check_desc_craft.py`, exit 2, four times — and returned INCONCLUSIVE. It tested the counter's *presence* at base instead of running the frozen counter from its freeze commit against `--rev <base>` data. | none — the plan fixed *when* the counter bytes exist (freeze before data), not how the red-before invocation is formed. | State the invocation beside the frozen predicate: run the counter from its freeze commit with `--rev <base>`. The round-77 base receipt does that — `.ufo/waves/round-77/receipts/c1-base-2f675548….txt` names the command, the counter sha256 and `description craft backed 0 of 6`, exit 1. |
| M76-5 · `scope` | The plan's declared seat surface is not the one the dispatch uses. `plans/round-76.md:64` budgets `labrat` 4 and `sonic` 1; the committed `.ufo/waves/round-76/w1-spec.json` holds 64 items with **0** labrat and **0** sonic (roles: executor 15, scribe 10, reviewer 10, scout 10, critic 6, mutation-tester 4, simplifier 3, revenger 3, sentinel 2, connector 1). | the pre-dispatch role validator (`unknown_role`) caught it — the guard working; no `corpus/QUALITY.md` row covers plan-vs-dispatch role drift. | `plans/round-76-addendum-1.md` § Wave role correction records the validated topology; this lesson states the dispatched mix, not the plan's estimate. |
| M76-6 · `number-drift` | The same plan sentence reads `30 build + 34 attack (attack share 53%)`, and its §3 role floors sum to 56, not 64. The dispatch's attack roles — reviewer 10 + critic 6 + mutation-tester 4 + sentinel 2 — are **22 of 64 = 34.4%**; adding the three simplifier seats (the plan's own "attack-simplifier") gives 25 of 64 = 39.1%, and no split yields 34. The dispatch commit `4de12b6`'s own subject says `34% attack share`. | none — no gate recounts a plan's seat arithmetic against the dispatch it produces. | The addendum's taxonomy is the one this round's claim uses and this lesson names the dispatched mix with its numbers; a plan's floor line should be generated from the dispatch spec, not typed beside it. |
| M76-7 · `attribution` | `.ufo/waves/round-76/base-battery/base-battery.txt:2-6` records `verify_corpus_integrity.py --json` as its header, the JSON's last three lines and `exit=0`, and `:7-11` the same shape for `verify_corpus_independent.py`. `.ufo/waves/round-76/build/B10RepairD2D3.measurements.txt:102-105` names the form (`... --json \| tail -3; echo exit=$?`) and reports that re-running the same command without the pipe at the same base gives `exit 1` and the four DRIFTs — the recorded status was `tail`'s, not the verifier's. | none — no receipt rule pinned the gate's own status. Three r76 seats diagnosed it independently (`.ufo/waves/round-76/w1/B10RepairD2D3.md:81-83`, `B11RepairD4.md:193-196`, `B24TipBatteryScript.md:242-246`, the last with the pipe-versus-direct control); the wave's own control `.ufo/waves/round-76/receipts/pipeline-exit-demo.txt` shows `false \| cat` reporting 0 against `false` reporting 1; and the class **recurs** — r54's closure recorded the same shape for `check_description_thresholds.py` (`.ufo/waves/round-54/falsify/W2CriticLesson.md:87`: "that is `tail`'s exit code, not the counter's"). The criterion the r76 control was written for (Q75) is not in `corpus/QUALITY.md` at `2f675548`; the Q75 row is a round-77 draft (`.ufo/waves/round-77/build/SC03QualityRows.quality-rows.md`), not a landed criterion. | `plans/round-77.md` § No-harm battery: every receipt captures the **gate's own** exit status, no `\| tail` pipeline (`cmd > out 2>&1; echo "exit=$?" >> out`), applied in `.ufo/waves/round-77/receipts/`. |
| M76-8 · `landing` | `git show --stat 6ce2724` → one added path, `kotoba-shokukin/.ufo/waves/round-76/w1/A18ScoutSnapshot.md` (typo'd directory, lane repo root). The typo'd tree is still in `HEAD`: `git ls-tree -r --name-only HEAD \| grep shokukin` lists `kotoba-shokukin/` twice (r75's `R75Facet48.md` and this r76 copy), so the "recover fleet-root A18 seat report" commit added a duplicate inside the lane instead of removing the fleet-root copy. Recorded as CD1 in `corpus/lessons/round-76-verifier-spotcheck.md` §1. | Q49 (seat reports stay lane-local and the final misroot sweep covers every seat-writable directory) caught the fleet-root copy in r75 but not a recovery commit that re-adds it inside the lane. | R76-D1: remove `kotoba-shokukin/` from the lane tree. Open at the round-77 base `2f675548`; round 77's disclosed hygiene work carries it (`plans/round-77.md` § Trigger, § Disclosed hygiene). |

Draft rows **not** carried, with the read that dropped them. The r76 draft's slice off-by-one row is subsumed by M76-1's
convention (the counters now print clip and stripped together). Its F7 row — "S213's `used-by` must equal one path
exactly, so an append turns `check_skill_evals_v2.py` red" — does not hold at the delivered blob:
`verifiers/check_skill_evals_v2.py:289-292` splits the cell on commas and tests membership, and the message the draft
quotes (`S213 used-by != ...`) does not occur in the file (`grep -c` → 0). Either it was repaired mid-wave or was measured
on a pre-freeze blob; the delivered counter admits the append, so there is no defect to record.

## Routed defects

**R1–R4 (round-75 closure) — not landed in round 76; re-routed as R76-D3 = round 77's C2.** At `6ce2724`
`check_r75_routed_repairs.py` reads `R1: open … R4: open`, `r75 routed repairs closed 0 of 4`, exit 1
(`.ufo/waves/round-76/receipts/c2-base-final.txt`), and the path-limited diff above shows `corpus/lessons/round-75.md` and
the `LOG.md` § Round 75 block untouched; `.ufo/waves/round-76/receipts/r1-folded-render.txt` and
`.ufo/waves/round-76/w2-registry-note.md` are drafts under `build/`, not committed at that revision. Round 77 re-lands
them against the frozen bytes.

**D2/D3 (round-74 closure) — prepared, not landed.** `LOG.md` § Round 74 still lacks the `d5aebcf` line and
`corpus/knowledge/sibling-overlap-census-round49.md` still lacks the round-74 forward pointer; the drafts are
`.ufo/waves/round-76/build/B10RepairD2D3.D2-log-round74.md` and `…/B10RepairD2D3.D3-r49-forward-pointer.md`.

**D4 — landed.** `check_spec_craft.py` (floor 250) and `check_sibling_reread.py` (floor 47) are floored in
`verifiers/floors-registry.json:65-73` and in the in-file tables of `verifiers/check_assertion_floors.py`; receipt
`.ufo/waves/round-76/receipts/d4-selftests.txt`.

**D5 — conditional, not landed.** The condition ("if a later freshness claim depends on the judged cells") did not
arise: round 76's C1 is depth over the `description` field and C2 is the r75 repairs. Recorded, not built.

**R76-D1 — open** (M76-8). **R76-D2 — this file.** **R76-D3 — round 77's C1 and C2.** **R76-D4 — round 77's index,
baseline and no-harm battery.** **R76-D5 — a dead-seat count per wave and the 52-vs-64 report-file reconciliation**
(round 76 wrote 52 report files for 64 seats and declined to infer a dead-seat count; spot-check §1 CD4).

## Status changes

**S213 `used-by`** — old: `corpus/knowledge/skill-eval-artefacts-round70.md`; new:
`corpus/knowledge/skill-eval-artefacts-round70.md, corpus/knowledge/description-craft-round76.md` (comma + space, the
separator the census parser splits on; matches `OLD_USED_BY` in `verifiers/check_desc_craft.py:124`). The cell is
`corpus/SOURCES.md:153`. The append and the entry file land in the **same** commit: with the cell appended and the entry
absent, `scripts/sources-census.sh validate --file corpus/SOURCES.md` exits 1 with
`E11 S213 missing used-by corpus/knowledge/description-craft-round76.md`. No other cell changes — `status` stays `mined`,
`opened` stays 2026-10-25, `recheck` stays `90d`, and the row keeps 11 cells. S213 is re-used, not reopened as a new id,
and `corpus/knowledge/description-craft-round76.md` is a new entry, not a row.

**Falsify corrections: none.** No falsy wave was dispatched in round 76 and none is claimed here; the closure's §2
re-check found the claims unlanded rather than wrong.
