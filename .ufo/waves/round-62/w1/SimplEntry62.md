# SimplEntry62 — economy pass on the round-62 prose drafts (SimplEntry class re-cover)

Seat: `KotobaR62.SimplEntry62` (simplifier, leaf; no dispatch, no subagent, no ask tool). Wave: `kotoba-r62-w1` (build). Date: 2026-10-23. Lane tip at dispatch: `45a7ecfac9e203297f3146c45d63f5e79367470c`. Lane write: this report only. Scratch (untrusted, never evidence): `/fast/scratch/hyaku/kotoba-r62/SimplEntry62/`.

## 0. Branch taken (honesty first)

The seat prompt authorizes two branches: trim ScribeEntry62's and ScribeLesson62's reports if present, else work from `plans/round-62.md` § C1/§ C2 and the r61 entry/lesson for shape. **The else-branch ran.** `ScribeEntry62.md` and `ScribeLesson62.md` were absent at every check of `.ufo/waves/round-62/w1/` from my first (before the directory existed) through my final check at `2026-10-23T21:01Z`, while 27 sibling reports were present (incl. `ExecInstancesA1–A4`, `ScoutPriorReceipts`, `SrcRulesFrontmatter`, `ScribeQ57`, `ExecAbsorbInstrument`). Both scribes were registered and running the whole time; their drafts never became reviewable in my window. What I could not verify is named in §5.

Deliverable below: the two round-62 prose documents (`corpus/knowledge/erratum-absorption-round62.md`, `corpus/lessons/round-62.md`) with the economy pass already applied — before/after byte counts and a per-cut home map. If the scribe drafts land later, §6 is the mechanical re-run checklist; `RevSentNovelty.md`'s 23-row keep/cut table applies to the real drafts the same way.

## 1. Method

- Trim rules (compression rule 2, `corpus/knowledge/anatomy-and-compression.md`): one authoritative home per fact; cut restatement of facts already held elsewhere (pointer instead); cut hedging that a Limits/declared-bounds list already carries; cut any sentence its table repeats. Never cut a measured value, a bound, or a command (seat mandate).
- Inputs: `plans/round-62.md` § C1/§ C2 (frozen); `corpus/knowledge/scoped-rules-counter-round61.md` (r61 entry shape + arm ground); `corpus/lessons/round-61.md` (lesson shape); measured w1 evidence: `ScoutPriorReceipts.md` (before-state 0 of 5), `ExecInstancesA1/A2/A3/A4.md` (instance verdicts), `SrcRulesFrontmatter.md` (S118 fetch record), `ScribeQ57.md` (Q57 row), `ExecAbsorbInstrument.md` (matrix line, wave evidence). No counter was run by this seat; every measured value below is quoted from a committed seat report.
- Before-texts: full-shape drafts composed at r61 verbosity from the same inputs (the redundancy a first draft carries); after-texts: the same facts, economy-passed. Byte counts are `wc -c` over the four scratch files, run 2026-10-23T21:00:45Z.

## 2. Byte counts (before → after)

```text
$ wc -c /fast/scratch/hyaku/kotoba-r62/SimplEntry62/{entry-before,entry-after,lesson-before,lesson-after}.md
10911 /fast/scratch/hyaku/kotoba-r62/SimplEntry62/entry-before.md
 5190 /fast/scratch/hyaku/kotoba-r62/SimplEntry62/entry-after.md
 4880 /fast/scratch/hyaku/kotoba-r62/SimplEntry62/lesson-before.md
 2473 /fast/scratch/hyaku/kotoba-r62/SimplEntry62/lesson-after.md
23454 total
```

- Entry `corpus/knowledge/erratum-absorption-round62.md`: **10911 → 5190 B (−52.4%)**.
- Lesson `corpus/lessons/round-62.md`: **4880 → 2473 B (−49.3%)**.

## 3. Entry — trimmed text (target: `corpus/knowledge/erratum-absorption-round62.md`)

```markdown
source: S118 (re-opens S103) + `plans/round-62.md` § C1 + `.ufo/waves/round-62/w1/{ScoutPriorReceipts,ExecInstancesA1,ExecInstancesA2,ExecInstancesA3,ExecInstancesA4}.md` + arm ground `corpus/knowledge/scoped-rules-counter-round61.md`
verified-at: `<pending>` — the C1 matrix data run had not been committed when this draft was written; an unrun check has not passed
recheck: `python3 -B verifiers/check_erratum_absorption.py --self-test`; then `python3 -B verifiers/check_scoped_rules_v31.py --self-test` (full stdout, `date -u`, exit code each).

# Erratum absorption (round 62): the five r61 errata scored against the landed v3 counter

Before-state: 0 of 5 erratum classes had a committed arm-level receipt against the landed counter — every r61 attack measured draft text or v2 bytes (`ca2585a4…`), not the landed arms (`ScoutPriorReceipts.md`). This entry carries the round-62 arm-level map. Arm wording, guard lists, and the seven A4 conditions stay in the r61 entry; the instrument's absorption definition, frozen predicate, and kill arms stay in `plans/round-62.md` § C1.

## Absorption map (instance measurements committed this round)

Primitive-level instance verdicts from the four instance seats; counter sha `5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91` in every run. The matrix's computed line (`errata measured 5 of 5; absorbed k of 5; surviving n; controls 2 of 2`) is `<pending — data run not committed at draft time>` and re-verifies this table.

| Erratum | Arm | Instance | Verdict |
|---|---|---|---|
| E2 | A3(a) `url_key` | `E2-locale-segment-reject` | REJECT |
| E2 | A3(a) | `E2-mdx-suffix-reject` | REJECT |
| E2 benign | A3(a) | `E2-md-drop-accept`, `E2-trailing-slash-accept`, `E2-query-accept` | ACCEPT ×3 |
| E2b | A3(b) `alias_why` | `E2b-ja-locale-reject` | REJECT |
| E2b | A3(b) | `E2b-at-latest-reject` | REJECT |
| E2b benign | A3(b) | `E2b-distinct-path-accept` | ACCEPT |
| E2c | A4(iv) `alias_sha_why` | `F-A4-7` (full sha re-recorded, unanchored teaches) | REJECT |
| E2c | A4(iv) | `F-A4-11` (anchored `supersedes S048 —`, prefix-only named row) | **ACCEPT — survivor** (condition 5 unimplemented: primitive cannot read the named row's digest) |
| E2c probes | A4(iv) | condition-(3) appended unanchored `supersedes` / condition-(6) anchor-cell fetch claim | REJECT / **ACCEPT — survivor** (condition 6 invisible to the teaches-only API) |
| E2e | A1 `a1_conjunct`+`scope_conjunct` | `E2e-fresh-1-bold-marker` (`paths: **`) | REJECT |
| E2e | A1 | `E2e-fresh-2-negated-within-60` ("Do not use paths: …") | **ACCEPT — survivor** (MutA1's G7 negation guard absent from the landed `scope_conjunct`) |
| E2e benign | A1 | Claude S103:198-199 pair, Cursor `globs: **/*.mdc`, VS Code/Copilot `applyTo` | ACCEPT ×4 |
| E2f | A2 `action_conjunct` | `E2f-event-token-backticked` (`` `InstructionsLoaded` ``, S103:194) | **ACCEPT — survivor** (G7 raw-tokenizer conjunct absent; forward 8/10 need 7, reverse 8/15 need 5) |
| E2f | A2 | `E2f-W6-sib-style` (S103:209) | REJECT (existing reverse fraction 8/34, need 12 — not G7) |
| E2f bound | A2 | `F6-compound-purpose-bound` (S106:60) | ACCEPT (declared surviving bound) |

## The E2f gap and the v3.1 successor

The landed `action_conjunct` implements the forward/reverse support fractions but no G7 raw-tokenizer event-claim conjunct and no G9 compound-purpose conjunct: `content_words` (`check_scoped_rules.py:972-977`) strips backticked spans, so `` `InstructionsLoaded` `` is erased before claim detection and the remaining words clear the fractions. The gap closes in a copy, `verifiers/check_scoped_rules_v31.py`, carrying the frozen E2f form (G5 key-on-line ∧ G7 raw-tokenizer; F6/G9 stays a declared surviving bound); it must print the unchanged r61 line `worlds reject 7 of 7; eligible rows pass 4 of 4` plus `E2f fresh instances reject 2 of 2`, exit 0. Landing conditions if it cannot keep both sides, and the exact MutA2 guard wording, are the plan's and MutA2's to say (`plans/round-62.md` § C1; `.ufo/waves/round-61/wave/MutA2.md:360-368`). The frozen `check_scoped_rules.py` bytes are never edited. `<pending — successor run not committed at draft time>`

## Declared bounds (disclosed limits, not oversights)

- **F6 compound purpose** — survives even the full G5+G7 form; G9 is the fuller guard the successor does not implement.
- **E2's 11 canonical spellings** — one document's canonical-equivalence spellings stay admitted (r61 entry, A3).
- **A4(iii) consistency-only** — committed-byte/recorded-date consistency is not acquisition authentication; backdated commits pass (r61 entry, A4).

## Limits

Arm-level audit only. Not measured, and not claimed by any sentence above: world-level semantics (the seven-world predicate re-runs unchanged); reviewer judgment per Q31 — a check the counter does not run is named as reviewer judgment, and the W8 semantic-substitution class survives all four arms (MutFixtureEscape); the sha pin is carried, not re-established (the instrument fails closed on drift, exit 2). S118's fresh bytes ground only the `paths`-glob evidence for E2e; the proposition itself is already held by S103/S112.
```

### Entry cut list (before → after, with the fact's home)

| # | Cut (from the before-text) | Where the fact lives now |
|---|---|---|
| E1 | Intro narrative retelling r61 (counter landing, "tempting to read…", "walks through each erratum…") | One ground sentence keeps the before-state; the r61 story's home is `corpus/knowledge/scoped-rules-counter-round61.md` + `ScoutPriorReceipts.md` (0-of-5 census) |
| E2 | Whole `## Arms` section (A1–A4 guard wording, canonical key set, `paths`-glob S118 sentence re-stated inside A1) | r61 entry arms section (lines 13–47); canonical keys re-verified in `ExecInstancesA1.md`; the `paths` glob fact's home is S103/S112 (+S118's fresh bytes, kept once in Limits) |
| E3 | `## How the matrix decides absorption` (two-directions definition, stub mutation, controls, sha-pin fail-closed narration) | `plans/round-62.md` § C1 (frozen predicate + kill arms); fail-closed exit 2 kept once in Limits |
| E4 | Table `Note` column prose (per-row reason paraphrases) | Instance ids + verdicts stay in the table; full reason strings live in `ExecInstancesA1/A3/A4.md` and `ExecInstancesA2.md` output blocks |
| E5 | E2f section: MutA2 guard-wording exposition and the "if the successor cannot keep both sides, it does not land" clause | `plans/round-62.md` § C1 successor paragraph; `.ufo/waves/round-61/wave/MutA2.md:360-368` (pointer kept) |
| E6 | `## Declared bounds` hedge ("restated here only because entries are read alone…") | Bounds stay as three one-line bullets, each citing its r61-entry home |
| E7 | `## Limits` summarizing sentence ("It follows that absorption here means…") | The absorption definition's home is plan § C1; the Limits bullets already carry the bound |
| E8 | Separate `## Not held` section (duplicate of Limits: W8, Q31, pending-markers) | Merged into `## Limits` — one home for "what the instrument does not measure" (Q31's applies-to names knowledge-entry Limits) |

## 4. Lesson — trimmed text (target: `corpus/lessons/round-62.md`)

```markdown
---
author: kotoba L1 round 62
date: 2026-10-23
round: 62
lane: kotoba
---

# Round 62 — lesson (kotoba, hyaku run 5, attempt 1)

## Gate

The following source rows were opened on 2026-10-23 by the named seats. Their source snapshots are proposed integration targets, not claimed landed bytes.

- **S118 Claude Code (re-opens S103)** — https://code.claude.com/docs/en/memory.md — accessed 2026-10-23T20:49:56Z (HTTP 200, 55,354 B, sha256 `02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801`; seat `SrcRulesFrontmatter`; snapshot target `.ufo/waves/round-62/snapshots/S118.page`) — `memory.md:250`: "| `paths` | No | Glob patterns that [scope the rule to matching files](#path-specific-rules). Accepts a YAML list or a comma-separated string |"

## Mistakes

- **M93 — class: erratum recorded as absorbed without an arm-level receipt** · The r61 close credited "five pre-data arm amendments each forced by a measured attack" (`.ufo/reports/round-61/kotoba.md:40`, fleet) while no committed receipt scored any of the five classes against the landed counter — 0 of 5 (`ScoutPriorReceipts.md`); the landed `action_conjunct` has no raw-tokenizer event-claim conjunct (`content_words`, `check_scoped_rules.py:972-977`, strips backticked spans; `E2f-event-token-backticked` ACCEPT, `ExecInstancesA2.md`), and E2c/E2e survivors are measured in `ExecInstancesA4.md`/`ExecInstancesA1.md`. No erratum is called absorbed without the matrix measuring both directions on that class. · captured-by: C1's absorption matrix (`plans/round-62.md` § C1; `python3 -B verifiers/check_erratum_absorption.py --self-test`, data run `<pending>` — an unrun check has not passed) · fix: successor `verifiers/check_scoped_rules_v31.py` + Q57 + the matrix · shown able to fail: the hollow-auditor control receipt `.ufo/waves/round-62/controls/absorption-hollow.txt` — `<pending commit; an uncommitted control has not failed anything yet>`.
- **M93+ — no additional mistake is asserted in this draft.** In-wave reports remain evidence for the L1 to adjudicate.

## Falsify corrections

- **M93 — wave 2 placeholder: the L1 fills this line after wave 2 falsification.**

## Status changes (contract rule 2, old → new)

- S118 — no old status (new row) → `queued` — flipped in the same commit that lands `corpus/SOURCES.md` S118 and `.ufo/waves/round-62/snapshots/S118.page` (its used-by target); no existing row's protected cell changed. `<landing pending>`
```

### Lesson cut list (before → after, with the fact's home)

| # | Cut (from the before-text) | Where the fact lives now |
|---|---|---|
| L1 | § Gate narrative: why S118 re-opens S103, scratch-saved fetch story, second-seat re-verification, census-after plan | `corpus/SOURCES.md` S118 row `teaches` cell; the fetch story's home is `SrcRulesFrontmatter.md`; re-verification is `RevS118.md`'s; census/Q34 commands' home is `CORPUS.md` § SOURCES contract + `corpus/QUALITY.md` Q34 |
| L2 | S103 prior-open comparison (2026-10-23T12:08:16Z, 54,043 B, sha `82d60341…`) | `corpus/SOURCES.md` S103 row |
| L3 | M93 narrative expansion: full r61 sentence with seat list, "It follows that…" paragraph, per-class survivor narration | The quoted sentence's home is `.ufo/reports/round-61/kotoba.md:40` (pointer kept); the 0-of-5 census and the class map's home is the entry's absorption table + `ScoutPriorReceipts.md`/`ExecInstancesA1/A2/A4.md`; the both-directions rule stays as M93's one sentence |
| L4 | § Falsify corrections explainer paragraph ("Corrections in this section record what wave 2's falsification passes changed…") | Cut; the placeholder line stays (the L1 fills it); r61's lesson carries no explainer either |
| L5 | § Status changes explainer (append-only narration naming `check_sources_append_only.py` and whose receipt it is) | Append-only command + proof home: `corpus/QUALITY.md` Q34; contract rule 2's home is `CORPUS.md`; the old→new line itself stays |

### Not cut (mandate guarantees)

All measured values and bounds survive verbatim: both sha256s, S118's timestamp/HTTP/bytes, `memory.md:250` quote (19 words, under the 25-word contract rule), `kotoba.md:40` pointer, 0-of-5, `check_scoped_rules.py:972-977`, every instance id and verdict (incl. all four measured survivors and F6), support fractions (8/10 need 7; 8/15 need 5; 8/34 need 12), `worlds reject 7 of 7; eligible rows pass 4 of 4`, `E2f fresh instances reject 2 of 2`, MutA2 pointer, the three declared bounds (F6; E2's 11 spellings; A4(iii) consistency-only), the Q31 Limits clauses (world-level, reviewer judgment, sha pin/exit 2, W8), and every recheck command. Needle check run over both after-texts (grep -F per value; only intentional L1/L2/L5 homes reported absent — none is a value or bound):

```text
$ for n in …27 entry needles…; do grep -q -F -- "$n" entry-after.md || echo "ENTRY-AFTER MISSING: $n"; done
$ for n in …10 lesson needles…; do grep -q -F -- "$n" lesson-after.md || echo "LESSON-AFTER MISSING: $n"; done
LESSON-AFTER MISSING: check_sources_append_only   # home: corpus/QUALITY.md Q34 (L5)
LESSON-AFTER MISSING: S103 :                      # home: corpus/SOURCES.md S103 row (L2)
NEEDLE-CHECK-DONE
```

## 5. Live wave evidence encountered, and what this seat did not verify

- `ExecAbsorbInstrument.md` (landed 21:00Z) measures `errata measured 5 of 5; absorbed 2 of 5; surviving 6; controls 2 of 2`, exit 0 — consistent with the instance-level survivors above and **revising the plan's expected `absorbed 4 of 5; surviving 1`**. The entry text deliberately prints the matrix line as `<pending — data run not committed at draft time>` rather than asserting either number: no committed receipt existed at draft time (M90: controls and data commits come first), and this seat ran no counter. When the L1 lands the receipt, the marker resolves to the computed line.
- Not verified by this seat: the scribes' actual drafts (never present); the matrix/successor/controls receipts (not yet committed); the v3.1 successor's output; the landed-vs-wave distinction on every verdict quoted here (quoted from committed w1 seat reports, which are wave evidence until the L1 integrates them).

## 6. If ScribeEntry62 / ScribeLesson62 land after this report

Apply the same pass mechanically: (1) every fact in RevSentNovelty's table rows marked CUT gets a pointer to its prior home, not a restatement; (2) the entry keeps exactly one table (the absorption map) and one Limits list; (3) the lesson keeps the r61 Gate/Mistakes/Falsify/Status shape with one bullet each; (4) measured values, bounds, and commands are never cut — check with the §4 needle list; (5) hedge only what no Limits list already carries. Any sentence whose fact is already in the r61 entry, the plan, or a seat report should become a pointer.

Installs: no installs.
Blockers: none — named limitation: the two scribe drafts never landed in my window (absent at every check through 2026-10-23T21:01Z), so the pass ran on the authorized fallback inputs; §6 makes it re-runnable on the real drafts without re-analysis.
Produced: the economy-passed round-62 entry (`corpus/knowledge/erratum-absorption-round62.md`, 10911→5190 B) and lesson (`corpus/lessons/round-62.md`, 4880→2473 B) with per-cut home maps, no-cut guarantees, and the honesty markers the pending receipts require.
