<!-- SC05ScorecardDrafts — round 77 (hyaku run 10, attempt 1), wave w1, seat SC05.
     Input: .ufo/waves/round-76/build/scorecard-draft.md (r76 draft; r76 seats were unscored and the
     closure found defects, so its numbers were treated as claims to verify, not as facts).
     Scope: SCORECARD.md only. This seat edits no lane file; the L1 integrates after the wave.
     Predicate sentences below are byte-copied from plans/round-77.md:26 (C1) and plans/round-77.md:38
     (C2) — Q26: the same sentence in plan, receipt label and SCORECARD.
     Everything asserted here was read from committed bytes at lane HEAD 6523aced1ee0ebe07dca996213bdc645a6acbd1e
     or base 2f675548eaad2a037a899d39247c1fd7a88aaf48 and is named with its command in §4.
     Values that only exist after integration are slots: [[SLOT: ...]].
     Integration anchors (SCORECARD.md, 469 lines, 204,036 bytes at HEAD):
       axes table header :26 | depth row :28 | consistency row :29
       § planned :38-:180 (last `**Next:` line :166; "Historical carry remains named" paragraph :170)
       move log second table body ends :305, `## Capabilities` :307; Capabilities tail sentence :320
       appended annotation tail ends :469; the file's last forward pointer is `**Next: round 67**` at :371. -->

# 1. axes-table row text — round 77

**Score effect: HOLD on both rows.** Depth stays 9, consistency stays 10, delta 0 on each. The rubric
(SCORECARD.md:19-23) bands the two readings: `9 + machine-checked or externally audited`,
`10 + repeated non-author verification in the opposite direction`. Both counters were authored by the lane
and the r77 data is landed by the lane, so neither number can be re-measured upward by the author; a score
moves only on a non-author re-measurement. `Last change` therefore keeps its current value on both rows
(`60` / `15`) — the evidence cell gains a clause, the score cells do not move.

## 1a. depth — `SCORECARD.md:28` (Score cell stays `9`, Owned `owned`, Last change stays `60`)

Clause to prepend at the start of the evidence cell (immediately after `| depth | 9 | `), old cell content
preserved verbatim after it:

**round 77 (C1 — description craft backed; score held 9, delta 0; band reasoning: 9 = "machine-checked or externally audited", which the counted, byte-recomputing counter keeps supported; 10 = "repeated non-author verification in the opposite direction", and the lane authored both the counter and the data, so no raise is self-measurable — HOLD pending the non-author closure; declared limit: admission is not compliance, the audited `description` still fails the page's imperative and "short" rules):** `python3 -B verifiers/check_desc_craft.py --rev <rev>` prints `description craft backed K of 6` and exits 0 only when all six conjuncts hold at `<rev>`; at the r77 base `2f675548eaad2a037a899d39247c1fd7a88aaf48` (the r76 base was `b7f13f4b39cbd43076a85568adca763a6f674e7a`) it prints `description craft backed 0 of 6` and exits 1. Measured: `description craft backed 0 of 6`, exit 1 at `2f675548eaad2a037a899d39247c1fd7a88aaf48` (`.ufo/waves/round-77/receipts/c1-base-2f675548eaad2a037a899d39247c1fd7a88aaf48.txt`, the counter's own status captured as `exit=1`) → [[SLOT: C1 after — the exact counter line `description craft backed K of 6` and its own exit status at the integrated tip, copied from the tip receipt]] (tip receipt [[SLOT: path `.ufo/waves/round-77/receipts/…` naming the tip revision on its first line]]). The counter is unchanged from the r76 freeze `ec7f853`: sha256 `cf3c45d9e3985f11889816f4bb371dc0d5541c10c09ce2ab3966a4bff4603b9e` at `ec7f853`, at the r77 base and at HEAD (re-hashed 2026-10-27, §4); `--self-test` `0 failure(s) over 53 assertions`, exit 0 (`.ufo/waves/round-77/receipts/selftests-base.txt`). Conjuncts (a)–(f) are exactly `plans/round-76.md` § C1 as corrected by `plans/round-76-addendum-1.md` and `plans/round-76-addendum-4.md`. Content: description-craft guidance from S213 (`https://agentskills.io/skill-creation/optimizing-descriptions.md`, re-opened this round by two independent seats) admitted at guide-advice level as `corpus/knowledge/description-craft-round76.md`; acted on as one `SKILL.md` § Body craft rule row citing the entry and S213 with three quote fragments; row S213's `used-by` in `corpus/SOURCES.md` gains `corpus/knowledge/description-craft-round76.md` after `corpus/knowledge/skill-eval-artefacts-round70.md` with the old→new change logged in `corpus/lessons/round-76.md`; the entry opens with `source:`/`verified-at:`/`recheck:`; the snapshot chain `.ufo/waves/round-76/snapshots/` pins three page bodies in four places (`snapshots/MANIFEST.sha256`, `snapshots/fetch-record.json` HTTP 200 records, the counter's in-file digest table, and the round-76 lesson `## Gate`; the S213 `anchor` cell is not edited in place), and the ≥4 located quotes are ≤25 words, verbatim after the page's first heading and page-unique. Conjunct (d) recomputes the audit numbers from the measured revision's bytes under the pinned convention (folded-scalar render, whole block, CLIP chomping; first sentence to and including the first `. `); at the r77 base the counter's own `description_measures` returns `(1022, 1021, 151)` (clip / stripped / first sentence, re-run by this seat §4), and the tip value is whatever (d) recomputes at `<tip>`. Controls before data: base `0 of 6`; fabricated/stub entry + empty snapshot set; real text from the wrong page; token dump naming all six conjuncts — receipts [[SLOT: `.ufo/waves/round-77/receipts/c1-controls.txt` — absent at authoring; the r76 control world was scored on an earlier counter blob `87837d7a…`, so the r77 re-run on the frozen `cf3c45d9…` bytes is the receipt that counts]]. Bound: the counter counts form, sources, tokens and pinned bytes; the judgement that the page teaches these rules belongs to the named non-author attack seats and the closure.

## 1b. consistency (calibration sub-axis) — `SCORECARD.md:29` (Score cell stays `10`, Owned `owned`, Last change stays `15`)

Clause to prepend at the start of the evidence cell (immediately after `| consistency (calibration sub-axis) | 10 | `), old cell content preserved verbatim after it:

**round 77 (C2 — r75 routed repairs; score held 10, delta 0; band reasoning: 10 is this lane's rubric top band, "repeated non-author verification in the opposite direction", met at round 12's two-leg independent derivation and un-movable upward; a landing that closes defects a non-author closure routed maintains the band rather than raising it, and a drop would need a non-author to find a record defect — HOLD pending the non-author closure):** `python3 -B verifiers/check_r75_routed_repairs.py --rev <rev>` prints `r75 routed repairs closed 4 of 4` and exits 0 only when all four repairs hold at `<rev>`; at the r77 base `2f675548eaad2a037a899d39247c1fd7a88aaf48` (r76 base `b7f13f4b39cbd43076a85568adca763a6f674e7a`) it prints `r75 routed repairs closed 0 of 4` and exits 1. Measured: `r75 routed repairs closed 0 of 4`, exit 1 at `2f675548eaad2a037a899d39247c1fd7a88aaf48` (`.ufo/waves/round-77/receipts/c2-base-2f675548eaad2a037a899d39247c1fd7a88aaf48.txt`, captured `exit=1`, with the nine per-repair fail notes printed beside it) → [[SLOT: C2 after — the exact counter line `r75 routed repairs closed 4 of 4` and its own exit status at the integrated tip, copied from the tip receipt]] (tip receipt [[SLOT: path `.ufo/waves/round-77/receipts/…` naming the tip revision on its first line]]). The counter is unchanged from the r76 freeze `ec7f853`: sha256 `989203c40e1aab55fc14ee1d444dd4fa8b49fe01144b2dcdeaa6a27fa39f4a63` at `ec7f853`, at the r77 base and at HEAD (re-hashed 2026-10-27, §4); `--self-test` `0 failure(s) over 27 assertions`, exit 0 (`.ufo/waves/round-77/receipts/selftests-base.txt`). R1–R4 are exactly `plans/round-76.md` § C2 with `plans/round-76-addendum-5.md`: R1, an appended correction in `corpus/lessons/round-75.md` naming the superseded M75-1 text and the Gate reject candidate, asserting the folded-render measurement of the r75-tip description (1,022 clip-preserving / 1,021 stripped; block lines 4–18) and citing `corpus/lessons/round-75-verifier-spotcheck.md`, plus `.ufo/waves/round-76/receipts/r1-folded-render.txt` recomputing the render from the measured revision's bytes; R2, `.ufo/waves/round-76/receipts/noharm-at-tip.txt` naming the r75 final tip `ac9f29510d3914a6edb97c8dbdb3445cab9141de` on its first line and carrying stdout plus exit codes of `verify_corpus_integrity.py --json` and `verify_corpus_independent.py --json` green there (the counter re-runs both gates at that exact revision and compares normalized stdout), cited from `LOG.md` § Round 75; R3, `.ufo/waves/round-76/w2-registry-note.md` reconciling seat `R75Attack28` (named report absent; 63 of 64 report files) with a machine-checkable excerpt of `.ufo/waves/round-75/w2-results.json`, cited from `LOG.md` § Round 75; R4, an appended closing line in `LOG.md` § Round 75 after the "w2 falsify results pending" text recording the w2 settlement (64 seats, 0 dead, 63/64 reports, R75Attack28 phantom). Controls before data: base `0 of 4`; a token-dump world (right filenames, forged or empty content) must fail; each repair has a must-fail `--self-test` arm — receipts [[SLOT: `.ufo/waves/round-77/receipts/c2-controls.txt` — absent at authoring; the r76 control receipt is `87837d7a…`-era and is re-run this round on the frozen `989203c4…` bytes]]. Bound: the counter checks content, not file presence; R1's text arms are presence-and-quote floors over the lane's own records (disclosed in the counter docstring), while R1's number, R2's greenness and R3's counts are recomputed from committed bytes or a sandbox re-run.

# 2. Move log rows — round 77

Insert after `SCORECARD.md:305` (the `| 55 | operability | …` row), keeping the second move-log table's
column order `| Round | Axis | Before | After | Evidence |`. Both `After` cells are slots: the after-value is
a measurement, not a plan, and the author does not fill it.

| Round | Axis | Before | After | Evidence |
|---|---|---|---|---|
| 77 | depth | `description craft backed 0 of 6`, exit 1 @ `2f675548eaad2a037a899d39247c1fd7a88aaf48` (base receipt `.ufo/waves/round-77/receipts/c1-base-2f675548eaad2a037a899d39247c1fd7a88aaf48.txt`; base control, no data) | [[SLOT: `description craft backed K of 6` + the counter's own exit status at the integrated tip, from the tip receipt]] | `verifiers/check_desc_craft.py` (frozen `ec7f853`, sha256 `cf3c45d9e3985f11889816f4bb371dc0d5541c10c09ce2ab3966a4bff4603b9e`, self-test 0/53 exit 0), `plans/round-77.md` § C1, `corpus/knowledge/description-craft-round76.md`, `SKILL.md` § Body craft, `corpus/SOURCES.md` row S213 `used-by`, `corpus/lessons/round-76.md` `## Gate`, `.ufo/waves/round-76/snapshots/` (MANIFEST.sha256 + fetch-record.json HTTP 200), tip receipt [[SLOT: path]] |
| 77 | consistency | `r75 routed repairs closed 0 of 4`, exit 1 @ `2f675548eaad2a037a899d39247c1fd7a88aaf48` (base receipt `.ufo/waves/round-77/receipts/c2-base-2f675548eaad2a037a899d39247c1fd7a88aaf48.txt`; R1–R4 all `open`) | [[SLOT: `r75 routed repairs closed 4 of 4` + the counter's own exit status at the integrated tip, from the tip receipt]] | `verifiers/check_r75_routed_repairs.py` (frozen `ec7f853`, sha256 `989203c40e1aab55fc14ee1d444dd4fa8b49fe01144b2dcdeaa6a27fa39f4a63`, self-test 0/27 exit 0), `plans/round-77.md` § C2 + `plans/round-76-addendum-5.md`, `corpus/lessons/round-75.md` (appended correction), `.ufo/waves/round-76/receipts/r1-folded-render.txt`, `.ufo/waves/round-76/receipts/noharm-at-tip.txt`, `.ufo/waves/round-76/w2-registry-note.md`, `LOG.md` § Round 75; tip receipt [[SLOT: path]] |

# 3. `planned` replacement — round 78

Insert at the end of § planned (after `SCORECARD.md:166`, before the "Historical carry remains named"
paragraph at `:170`). It replaces the file's current forward pointer as the plan of record; the older
`**Next: round 67**` line at `SCORECARD.md:371` and every earlier `**Next:` line stay as records
(append-only). No `**Round 77 completed …**` line is pre-written here: the round's disposition belongs to
the closure, and a scribe seat cannot write a verdict it has not seen.

**Next: round 78** — re-measure every before-value first (Q19). The two r77 claims are measured, not admitted: their verdict belongs to the w2 falsify wave and the non-author closure, and no score moves on the author's own measurement (depth held 9, consistency held 10). Candidates: (a) the non-author closure itself — re-run both frozen counters at the landed tip, re-open the S213 quotes against the sha256-pinned snapshots, attack each claim, mutate each touched gate and re-run the no-harm battery; depth's band-10 path ("+ repeated non-author verification in the opposite direction") is the closure's to measure and cannot be self-declared; (b) the held eval-fidelity claim — S213's trigger-rate protocol (should-trigger queries, about 3 runs each, threshold 0.5, held-out validation split) stays held until a controlled held-out query experiment is designed before data, the condition the r75 Gate set; (c) the description repair the r76 entry routes forward — the imperative gap and the "short" rule, against a 1,022-character render with 2 characters of headroom under the 1,024 ceiling: any rewrite moves the number C2-R1 pins, so it needs its own before/after counter and a matching render receipt before data; (d) r76 hygiene not yet closed after w2 — R76-D5's per-wave dead-seat count with the r76 52-vs-64 report-file reconciliation, R76-D1's stray `kotoba-shukukin/` path, R76-D4's index + baseline repair (stale totals 144/99/43 against observed 146/102/44) with receipts, and the r74 D2/D3 forward pointers (`.ufo/waves/round-76/build/B10RepairD2D3.*`) only if their gate receipts exist; (e) the L0 open question (the all-axes reading, including adjacency) and the held advisory values — coverage 8.5, operability 8.5, freshness 8, calibration 8.5, adjacency 8.0. considerthese 2026-10-26 proposals 1/2/4/5 stay declined with the r76 Gate reasons; no assimilation (frozen claims, § Frozen and resumed rounds).

# 4. What this seat verified (not assumed) at 2026-10-27

| check | command (run from the lane root, read-only) | output |
|---|---|---|
| counter bytes = pinned, at HEAD | `sha256sum verifiers/check_desc_craft.py verifiers/check_r75_routed_repairs.py` | `cf3c45d9e3985f11889816f4bb371dc0d5541c10c09ce2ab3966a4bff4603b9e` / `989203c40e1aab55fc14ee1d444dd4fa8b49fe01144b2dcdeaa6a27fa39f4a63` |
| counter bytes = pinned, at base `2f675548` | `git show 2f675548…:verifiers/check_desc_craft.py \| sha256sum` (same for the C2 counter) | same two digests |
| counter bytes = pinned, at the r76 freeze `ec7f853` | `git show ec7f853:verifiers/<counter>.py \| sha256sum` | same two digests (commit type `commit`) |
| base receipts exist and are red for the right reason | `cat .ufo/waves/round-77/receipts/c1-base-….txt` / `c2-base-….txt` | `description craft backed 0 of 6` … `exit=1`; `r75 routed repairs closed 0 of 4` … `exit=1`, nine per-repair fail notes |
| self-tests at base | `cat .ufo/waves/round-77/receipts/selftests-base.txt` | `0 failure(s) over 53 assertions` / `0 failure(s) over 27 assertions`, `exit=0` each |
| snapshot chain bytes | `sha256sum .ufo/waves/round-76/snapshots/*.md` vs `MANIFEST.sha256` vs `fetch-record.json` vs the counter's in-file table | all four agree; optimizing-descriptions = `7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837`, HTTP 200, 13,403 bytes |
| description measurements | import the frozen counter and call `description_measures()` on HEAD and base `SKILL.md` | `(1022, 1021, 151)` at both |
| S213 `used-by` today | `awk 'NR==153' corpus/SOURCES.md` | `corpus/knowledge/skill-eval-artefacts-round70.md` (r77 target: append `, corpus/knowledge/description-craft-round76.md`) |
| claim data absent at the base | `ls corpus/knowledge/description-craft-round76.md`; C1 base receipt notes | absent; counter's (a)/(b)/(d)/(f) note "is not committed at the measured revision" |
| controls receipts absent at authoring | `ls .ufo/waves/round-77/receipts/ \| grep controls` | no match (0) — hence the slots in §1 |
| SCORECARD anchors | `grep -n` on section headers and the two axes rows | depth row `:28`, consistency row `:29`, move-log body ends `:305`, `## Capabilities` `:307`, tail ends `:469`, last `**Next:` `:371` |

Not verified here, deliberately: any tip measurement (no data has landed and the L1 integrates after the
wave), the r77 control worlds (E01/E02 own them), S213 live re-open (S01/S02 own it), and the r76 drafts'
admission status (E06/E07/E08 verify them). This seat ran no build, lint or gate, and installed no tool.

# 5. Bounds and open items

- **No Capabilities row is proposed.** A row enters only through a round that demonstrates the capability
  running (`SCORECARD.md:320`); r77 re-lands data on instruments frozen in r76 and the r76 wave produced
  controls only.
- **Saturation unchanged.** Owned-axis line is 10.0; consistency sits at 10 and depth at 9, so the nudge
  stays dormant and no saturation is claimed (`SCORECARD.md:322`).
- **Both rows are drafts until the closure.** If a non-author re-measurement moves either score, this
  clause is superseded by an appended annotation, not rewritten in place.
- **Slot list:** C1 after-value + tip receipt; C2 after-value + tip receipt; `c1-controls.txt`; `c2-controls.txt`.
