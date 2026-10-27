# B13SkillPatch — SKILL.md patch draft (round 76, w1)

VERDICT: DRAFT COMPLETE, NOT APPLIED — artifact `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-76/build/skill-patch.md`, two pins (one § Body craft row, two § Gate registry rows), patched file **593 lines of 600**, trigger-fidelity checklist byte-identical. Revised after B15Simplifier D1–D2 (see F7).

Seat shape: leaf scribe, no dispatch, no background jobs, no installs, no git/jj writes. Base measured: `b7f13f4b39cbd43076a85568adca763a6f674e7a` (lane `SKILL.md`, 590 lines).

## Behavior (what the draft contains)

1. **Pin 1 — one description-craft rule row**, inserted after base line 216 (`confirm discovery before trusting a path`), inside the existing `| rule | source | what a skill author does |` table, at patched line 217. 3 cells, 447 characters, 65 words. Source cell cites **both** `S213 optimizing-descriptions` and `corpus/knowledge/description-craft-round76.md`, so C1 conjunct (c) is satisfied by the row alone. The advice cell carries three page rules and **three verbatim quote fragments** (C1 requires ≥2):

   | fragment (words) | snapshot line | occurrences in page / evaluating-skills / best-practices |
   |---|---|---|
   | `Err on the side of being pushy` (7) | 27 | 1 / 0 / 0 |
   | `descriptions tend to grow during optimization` (6) | 159 | 1 / 0 / 0 |
   | `Avoid adding specific keywords from failed queries` (8) | 157 | 1 / 0 / 0 |

   Each ≤25 words, after the page's first heading (L5), 6–8 words so a ≥5-word token rule also passes, and page-unique against both sibling snapshots.

2. **Pin 2 — two Gate-registry rows**, appended after base line 512 (`check_sibling_reread.py`), at patched lines 514–515, in the registry's eight columns and house style (backticked path, `gate`, `--rev <rev>`, `0=clean, 1=failed, 2=could-not-evaluate` + round label + frozen verdict line, `--self-test`, pinned-values, write-scope, `kotoba`):
   - `verifiers/check_desc_craft.py` — `description craft backed 6 of 6` at the measured rev / `0 of 6` at base; pinned values `in-file SELF_SHA and the three page digests; .ufo/waves/round-76/snapshots/MANIFEST.sha256`; read-only, self-test fixtures under `$TMPDIR`.
   - `verifiers/check_r75_routed_repairs.py` — `r75 routed repairs closed 4 of 4` / `0 of 4`; R1 folded-render receipt (1022), R2 tip-named no-harm receipt cited from LOG § Round 75, R3 `w2-registry-note.md` R75Attack28 reconciliation cited from LOG, R4 appended closing line; pinned values in-file; read-only.

**Preamble deliberately unchanged:** base bytes up to line 216 are identical in the patched copy. The plan's touch list names the § Body craft *row* and the § Gate registry *rows* — not the preamble — and § Compression rules' own "one authoritative home per fact" rule makes a second naming of the entry path there redundant, since conjunct (c) forces it into the row's source cell and the counter is discoverable from its registry row.

Line budget: 590 + 3 = **593 ≤ 600**, margin 7. `build/budget.txt` (B02) was absent at 13:59 and at every check since, so anchors were computed directly (`wc -l SKILL.md` = 590).

Checklist: the patch touches only § Body craft and § Gate registry. `diff` of base 218–307 against patched 219–308 (offset +1 after the inserted row) is **empty**; 19 boxes, no text, box added or removed. The `trigger.line_budget` box text is unchanged and moves from base line 285 to patched 286.

## Gates run (exact commands, outcomes)

Run in the lane and in `/fast/scratch/hyaku/kotoba-r76/B13SkillPatch/`; nothing applied to the lane tree.

| check | command | result |
|---|---|---|
| base line count | `wc -l SKILL.md` | 590, exit 0 |
| pins apply cleanly; anchors hold | python: extract two ```` ```text ```` blocks, insert, assert base 216/512 anchors | exit 0 |
| row/registry cell counts | python `l.count('|') - 1` | row 3 cells; registry rows all 8 cells; exit 0 |
| patched line count | `wc -l SKILL.patched.md` | **593**, exit 0 |
| preamble untouched | python `out[:216] == src[:216]` | `True`, exit 0 |
| checklist unchanged | `diff <(sed -n '218,307p' SKILL.md) <(sed -n '219,308p' SKILL.patched.md)` | empty, exit 0; **CHECKLIST-IDENTICAL**, `grep -c '^- \['` = 19 |
| fragments verbatim and page-unique | `grep -c -F` in the three snapshots | `1 / 0 / 0` for each, exit 0 |
| snapshot identity | `sha256sum .ufo/waves/round-76/snapshots/*.md` | optimizing-descriptions `7cc54fbb…bfd837` (13,403 B), evaluating-skills `a799805f…fb684`, best-practices `ab9f3b60…fb41` — equal to `MANIFEST.sha256` and the three `fetch-record.json` HTTP 200 records |
| my fetch vs snapshot bytes | `cmp <scratch fetch> snapshots/optimizing-descriptions.md` | clean, exit 0 |
| clause grounding | `python3` count of each advice clause in the snapshot | each occurs exactly once, exit 0 |

Not run, not claimed: `check_desc_craft.py` and `check_r75_routed_repairs.py` do not exist yet (B06/B07), so no counter ran against this draft; `check_gate_registry.py` cannot see the two rows until they are applied.

## Touched surfaces

- `.ufo/waves/round-76/build/skill-patch.md` (the draft; `build/` created by this seat, now shared), `.ufo/waves/round-76/w1/B13SkillPatch.md` (this report).
- Read-only: `SKILL.md`, `plans/round-76.md`, `verifiers/check_spec_craft.py`, `verifiers/checklist-baseline.json`, `corpus/SOURCES.md`, `.ufo/waves/round-76/snapshots/*`, peers' `build/quotes-s213.md`.
- Scratch `/fast/scratch/hyaku/kotoba-r76/B13SkillPatch/` used for the fetch and patched copies; removed before yield.

## Out of scope

Entry `corpus/knowledge/description-craft-round76.md` (B04/B12); both counters (B06/B07); `verifiers/floors-registry.json` + `check_assertion_floors.py` in-file tables (+2 rows, another seat); `corpus/SOURCES.md` S213 `used-by` (B14); lesson/LOG/SCORECARD rows (B08/B17–B19); controls and receipts C1-W1..W3, C2-W1.

## Findings

- **F1 (calibration, from B04QuotesScribe):** S213 does not state front-loading the use case or a self-contained first sentence (0 hits); its worked `After` example puts the imperative clause second. The row attributes neither.
- **F2 (operability):** 6–8-word spans, three fragments — one spare over C1's ≥2, and safe under a ≥5-word token rule.
- **F3 (budget):** `budget.txt` absent; 593 reproducible as 590+3; preserve the delta if B02's anchors differ.
- **F4 (adjacency):** `check_spec_craft.py` counts only rows citing S223–S225 (its `skill_problems`), so the S213 row cannot disturb `spec craft backed 3 of 3`.
- **F5 (frontmatter untouched, per B21RevMethod):** no frontmatter byte changes, so the 1022-char folded render (1021 stripped) and 2/3-char headroom under `SKILL_DESCRIPTION_MAX = 1024` stand. C1 (d)'s audit table is B12's and must carry the counter's recomputation.
- **F6 (matching convention, per B03SnapshotFetch):** fragment 1 sits inside `**bold**`, fragments 2–3 mid-line after a bullet — located only by word-bounded substring, never whole-line equality.
- **F7 (accepted simplification, B15Simplifier D1–D2):** dropped the preamble edit (touch-list scope + one-authoritative-home) and shortened the row from 540 chars/83 words to 447/65; re-measured 593 (not 595), preamble `out[:216] == src[:216]`, checklist still byte-identical, all three fragments still page-unique.
- **F8 (cross-seat arithmetic):** 594 belongs to a variant that *keeps* a 3-line merged preamble; this draft's 593 comes from leaving the preamble byte-identical. Both are below the 600 box; the difference is the preamble, not the counters or rows.
