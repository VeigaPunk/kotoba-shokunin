# B15Simplifier — redundancy and right-sizing of the round-76 build drafts

VERDICT B15Simplifier: report-only, no lane byte edited. 9 of 10 findings were taken by the draft seats while I measured (SKILL.md patch 593 lines, 447-char rule row, no preamble edit; entry 98 lines / 5 rule rows with the 1024 row demoted, nine recheck tokens, the unsupported attribution cut; lesson preamble cut to a pointer and its stale entry-description corrected; M76-6's taxonomy named). 1 was a false positive of mine and is withdrawn (`:152`). 1 remains open: the R1 correction's internal duplication, conditional on `check_r75_routed_repairs.py`, which did not exist in the tree at any read. No frozen predicate verdict is claimed.

Seat: simplifier, leaf (no subagent dispatch). Write scope used: this report only.
Scratch: `/fast/scratch/hyaku/kotoba-r76/B15Simplifier` created for symmetry and removed unused (`rm -rf` exit 0, verified by listing the parent); every finding is a byte measurement or an occurrence count on files readable in place, so no clone, worktree or fixture was needed and none was made.
Installs: none (no tool installed or updated by this seat).
Fleet root cwd: `/home/vgpnk/Projects/shokunin`; all paths below resolve from `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.

## Method, and what "no semantic caller" means for prose

The seat standard (semantic `references` through the `lsp` device) is a code-symbol test. No round-76 draft is code, and no LSP call is claimed here. A prose deletion can break exactly three things, and each candidate was tested against all three by reading the consumer:

1. a **frozen counter conjunct** that reads the text — C1 (c)'s § Body craft row, C2 R1's superseded-text naming (from `plans/round-76.md` § C1/§ C2; both counters were `test -f` exit 1 for the whole session, so each such item is marked CONDITIONAL with its fallback);
2. a **table whose shape a live counter parses** — `verifiers/check_spec_craft.py` anchors on `SKILL_HEADING` (its line 183), takes the section body to the next heading, walks `tables(section)`, and requires `MIN_ACTION_WORDS = 5` content words plus a page-unique token in the action cell; preamble prose is therefore free, row cells are not;
3. a **cross-entry pointer** another entry or lesson cites.

Objects, final bytes (the entry and the SKILL.md patch were each rewritten twice mid-review; every number below is from the final copy, verified by mtime and size at read time):

| draft | final | notes |
|---|---|---|
| `build/entry-draft.md` | 98 lines / 1618 words, 5 rule rows | rewritten 14:02, ~14:07 and 14:09 by B12 after this seat's messages |
| `build/skill-patch.md` | 7729 B | rewritten 14:06 by B13; rule row 447 chars / 65 words, preamble dropped, total 593 |
| `build/lesson-draft.md` | 220 lines / 3041 words | landed 14:05, revised after this seat's O2/O3/O5; **new object** — was absent at my first read |
| `build/B08-r1-round-75-correction.diff` | 23 added lines / 685 added words | rewritten 14:05 |
| `build/quotes-s213.md` | 118 lines | 13-quote pool, justified duplicate (non-finding 3) |
| `build/w2-registry-note.md` | 106 lines | R3 note |
| `build/log-draft.md`, `build/scorecard-draft.md` | 187 / — | paste-ready text, four-bullet shape matching r71–r73 |

## Closed findings — measured before, measured after

| id | object | what I measured before | what the draft now holds | contract preserved |
|---|---|---|---|---|
| D1 | `skill-patch.md` Pin 1 (preamble) | 2 lines (104/107 chars) replaced by 4 (104/106/106/33); the entry path stated twice in one section, once in the row that C1 (c) forces | **dropped**; preamble byte-identical to base; total 593 (margin 7) | (c) satisfied by the row alone; `check_spec_craft.py` reads rows, not the preamble (its `skill_section()` at line 765 splits on the heading and its `skill_problems()` walks `tables(section)`) |
| D2 | `skill-patch.md` Pin 2 (rule row) | 540 chars / 83 words vs the six existing rows at 164–260 chars / 25–43 words | **447 chars / 65 words**, three fragments kept case-exact | still ≥2 fragments for (c); `grep -n -F` gives snapshot lines 27/157/159 and 0 occurrences in `S209-evaluating-skills.md` and round-74 `best-practices.md`; action cell keeps ≥5 content words and a page-unique token |
| D3 | `entry-draft.md` rule 6 (1024 ceiling re-statement) | 8 rule rows; row 6 quoted the page's restatement of the *specification's* limit, whose authority the lane already holds 4× plus `check_description_thresholds.py`, and which the entry's own § What this entry does not claim conceded | **5 rule rows**; the ceiling survives as an audit row citing `:28` plus `frontmatter-rule-authorities-round48.md:44`; `recheck:` prints nine tokens | (b) needs ≥4 quotes and has 5; no fact re-derived |
| D4 | `entry-draft.md` § Related | 124 words making four pointers, two of them repeats of pointers already made in § What this entry does not claim | **4 bullets / 113 words**, each pointer made once | every pointer still made where its fact is used |
| D5 | `entry-draft.md` § Limits b2 | eval-fidelity held stated in two places ~60 lines apart | merged into bullet 1, keeping `:19`; Limits is 225 words | the hold is still stated once, with its unique bound |
| D6 | `entry-draft.md` counts | "148 words … 9 sibling lanes … 1 `NOT` clause" used by no verdict while the sentence claimed they were; `149`/`153` figures uncounted (Q13) | four counts, each consumed by a verdict (7 sentences, 8 phrases, 3 categories, 2 chars headroom) | no counter reads these numbers; C1 (d)'s two values untouched |
| D8 | `entry-draft.md` finding 3 pointer | I reported `:152` where the quote's distinctive words sit at line 154 | the draft cites **`:153`–`:154`**, which is the correct span: line 153 ends "for those, `description` craft" and 154 begins "is audit-hygiene, not routing surface" | **withdrawn as my false positive** — the sentence spans two lines and B12's span citation is better than my single-line number |

## Findings raised by this seat — final disposition of each

### O1 — `entry-draft.md:8-9`: an attribution that no cited entry supports, and that its own `ground:` line contradicts — **TAKEN (final: parenthetical cut, `ground:` kept)**

The pre-fix intro read:

> § Writing effective descriptions is four principles for the field that decides whether a skill is read at all (`:17`, already in the lane's `spec-skill-creation-craft-round74.md` and `frontmatter-trigger-surface.md`).

**Landed fix (B12, 14:09):** the parenthetical was cut and `ground:` kept — the entry now reads "… whether a skill is read at all (`:17`). What the lane did not hold is the writing itself: …", 98 lines / 10,887 B, with no quote, cell, token or recheck string moved (5 rule rows and the nine recheck tokens re-measured after the edit). The `ground:` line it must not contradict reads:

> … and **no entry carried the page's writing principles**; at base `b7f13f4` a phrase sweep of `SKILL.md corpus/knowledge/*.md corpus/QUALITY.md` for five rule phrasings … matched 0 files …

Two problems, both checkable in committed bytes:

- **The citation is empty.** `spec-skill-creation-craft-round74.md` mentions S213 three times and every one is an exclusion: `:116` ("…`evaluating-skills` S212 and `optimizing-descriptions` S213"), `:133` ("…not the description page (S213), or an evaluation of any skill's output quality"), `:141` ("…the pages (S209, S212, S213), the siblings this entry does not re-open"). `frontmatter-trigger-surface.md` contains none of the four principles:

```
$ grep -n "S213\|description page" corpus/knowledge/spec-skill-creation-craft-round74.md
116:  `evaluating-skills` S212 and `optimizing-descriptions` S213), the specification page itself, and whether
133:page (S213), or an evaluation of any skill's output quality (S212, and kengaku's ground).
141:  pages (S209, S212, S213), the siblings this entry does not re-open.
$ grep -in "imperative\|user intent\|pushy\|concise\|1024" corpus/knowledge/frontmatter-trigger-surface.md
149:    noun with slash-form or imperative-context triggers.        # a trigger-kind note, not a principle
```

- **It contradicts the entry's own novelty line.** If the four principles were already held by two entries, `ground:`'s "no entry carried the page's writing principles" is false; if `ground:` is right, the parenthetical is false. It cannot be both, and the wave's depth claim rests on the second reading.

Smallest safe correction: drop `spec-skill-creation-craft-round74.md` from the parenthetical and cite `render-mechanism-round7.md` for the render half (already one of the entry's § Related bullets, and the entry that actually holds "the `description` string is what the router renders"), or drop the parenthetical entirely — the sentence's own point ("what the lane did not hold is the writing itself") stands without it. This is a Q23-shaped item (a rule credited to authorities that do not state it) inside the depth claim, so it is worth fixing before the entry is cited as backing 6 of 6.

### O2 — `lesson-draft.md:46-47`: stale cross-reference into the entry it describes — **TAKEN (B17: "stale ×3")**

Fixed to five quotes in the opening rule table, five rule rows from `:25`–`:28`, worked example `:184`–`:188`, plus the Q62 section. Re-measured after the edit: `build/entry-draft.md` has 5 `| optimizing-descriptions |` rows and cites `:184`–`:188`, so the lesson's sentence now matches the draft it describes.

Pre-fix text: "The entry `corpus/knowledge/description-craft-round76.md` carries **eight** such located quotes (**§ The admitted rules**) and the two-sided illustration at `:179`–`:190` …". Against the entry of that moment: **5** rule rows, no `§ The admitted rules` heading at all (the headings are `## This lane's own description, measured`, `## What this entry does not claim (Q62)`, `## Limits`, `## Related`; the rules table sits under the H1 with an intro paragraph), and the illustration cited at `:184`–`:188`. The lesson therefore described a revision two edits old — the classic stale-name class, landing in the round's own historical record.

This is the stale-name class: a lesson written against revision N−2 describing revision N. It lands in a lesson that is the round's own record, so the wrong number becomes the cited history.

### O3 — `lesson-draft.md` was 2× the corpus's largest lesson, with its first 29 lines duplicating the plan and the LOG — **TAKEN (preamble cut); my total-size headline overstated, the per-defect figure is the fair one**

Pre-fix measurement:

```
$ wc -lw build/lesson-draft.md corpus/lessons/round-73.md corpus/lessons/round-74.md corpus/lessons/round-75.md
  216  2770 build/lesson-draft.md
  104   ... corpus/lessons/round-73.md
  117   ... corpus/lessons/round-74.md
   12   ... corpus/lessons/round-75.md
```

Lines 1–28 (before `## Gate`) were a claims preamble — frozen claim sentences, wave shape with a seat split, the addendum's two corrections — every fact of which already sits in `plans/round-76.md`, `LOG § Round 76` (paste-ready text 1) and the SCORECARD annotation. B17 replaced it with a 10-line pointer and moved the wave mix to M76-6, where it is evidence; re-measured, the preamble is 25 lines / 215 words against r74's 17 / 126.

The body rows were not compressed, and the lesson is now **220 lines / 3041 words** — larger in total than when I flagged it, because M76-6 gained the taxonomy alternatives O5 asked for. My "2× the largest lesson" framing compared totals and is the wrong calibration: per disposition it is +30%, not 2×.

| lesson | lines | words | defects + mistakes | lines per item |
|---|---|---|---|---|
| round-74 | 117 | 1970 | 7 + 6 = 13 | 10.6 |
| round-76 (final) | 220 | 3041 | 10 + 6 = 16 | 13.75 |

Section split of the final draft: preamble 25/215, `## Gate` 85/934 (r74: 64/913), `## Mistakes` 10/882 (r74: 14/725), `## Routed defects` 56/532 (r74: 12/203), `## Round honesty` 25/339, `## Status changes` 15/126. `## Round honesty` is **precedent, not a new section** (`corpus/lessons/round-72.md` and `round-73.md` carry it), so it stays; the surplus is in Routed defects, which disposes 10 items where r74 disposed 7.

### O4 — `B08-r1-round-75-correction.diff`: two of its paragraphs duplicate the row three lines above it and Q74 (CONDITIONAL on B07)

Final measurements: 23 added lines / 685 words appended to a **12-line** lesson. The corpus's own correction precedent is 6 lines / 87 words (`corpus/lessons/round-74.md` § Falsify corrections).

| fragment | measure | why it duplicates |
|---|---|---|
| naming paragraph (`:10`) | 148 words | necessary — it names the superseded M75-1 sentence and the Gate reject candidate, both verbatim |
| indented verbatim row (`:14`) | 108 words, one 1087-char line | **third copy**: the filed row still sits at `corpus/lessons/round-75.md:11`, three lines above the append point, and the naming paragraph already quotes the superseded sentence |
| "Why the row's numbers reproduced" (`:16`) | 110 words | **second copy of Q74's reasoning**: Q74's row already carries "`length($0)` counts the two-space YAML indent and the `description: >` marker line (the r75 window `NR>=3&&NR<=8` sums to 392 for a block that renders 1,022)" |
| three-command block (`:20`–`:24`) | ~84 words | the same three commands with the same outputs are reprinted in `build/B08-m76-1-round-76-row.md` § Numbers (`3:14 4:76 5:78 6:73 7:79 8:72`; `1037`; `1022 1021`) |

Order of safety: cut the command block first (~84 words, cite `receipts/r1-folded-render.txt`, which C2 R1 requires anyway), then the "Why" paragraph (~110 words, point at Q74), then the indented row (~108 words) — the last only if `check_r75_routed_repairs.py` does not search for the full row string; it did not exist at any read, so keep the fallback: if it does, keep the indented row and take the other two cuts. Keep unconditionally: the naming paragraph, the slice paragraph (`:18`, 28 words — the reproducible definition of the 1022/1021 pair), the "Re-derivation owed by R1" paragraph (Q21: names the plan note it withdraws) and "Rule landed".

### O5 — M76-6's replacement value rested on a taxonomy that was not stated and disagreed with the plan's own — **TAKEN (B17 named the taxonomy and both alternatives)**

The lesson already logged the drift (good, and not my finding to duplicate): plan "30 build + 34 attack (53%)" vs the dispatched mix. But the replacement value it printed — "42 build + 22 attack = 34.4% (attack roles per `w1-spec.json`: reviewer 10, critic 6, mutation-tester 4, sentinel 2)" — was a third taxonomy. The committed bytes admit two other computable splits:

```
$ python3 -c "import json;d=json.load(open('.ufo/waves/round-76/w1-spec.json'));\
import collections;print(len(d['items']), collections.Counter(i['role'] for i in d['items']))"
64 Counter({'executor': 15, 'scribe': 10, 'reviewer': 10, 'scout': 10, 'critic': 6,
           'mutation-tester': 4, 'simplifier': 3, 'revenger': 3, 'sentinel': 2, 'connector': 1})
$ python3 -c "import json;d=json.load(open('.ufo/waves/round-76/w1-spec.json'));n=[i['name'] for i in d['items']];\
print('A-named', sum(x[0]=='A' for x in n), 'B-named', sum(x[0]=='B' for x in n))"
A-named 36 B-named 28
```

- plan's own attack list is "reviewer, critic, mutation-tester, labrat, sentinel, attack-simplifier seats" — it **includes** simplifiers and **omits** revengers; under that list the wave has 10+6+4+0+2+3 = **25 attack / 39 build = 39.1%**;
- attack *roles* as a class (reviewer, critic, mutation-tester, simplifier, revenger, sentinel) = **28 / 36 = 43.75%**;
- the dispatch's own naming (A = attack seat) = **36 A / 28 B**.

M76-6's 22 is reproducible only inside its own parenthetical definition, which excludes the three simplifiers — and this seat is one of them (B15, build-side), while two others (A27SimplifierAudit, A28SimplifierRead) are attack-side and A-named. The fix value should be one of the three computable splits with the taxonomy named in the same sentence; otherwise the lesson replaces one unreproducible number with another.

## Non-findings — measured, and recorded so they are not "simplified" later

1. **The frozen predicate sentence recurs in the plan, the SCORECARD draft, the LOG draft and both registry cells.** Mandated: the plan says "same sentence in plan, counter receipt label, and SCORECARD row". Not a duplicate to cut.
2. **Registry cells at 1156 (C1) and 922 (C2) chars.** Existing maximum 1095 (`check_sibling_reread`, `SKILL.md:511`) and 1037 (`check_spec_craft`, `:512`). C1 states each of (a)–(f) once with no internal repetition; `verifiers/README.md` names only early-round instruments (`grep -n "check_spec_craft\|check_sibling_reread" verifiers/README.md` → no hits), so for round-70+ counters the registry cell is the only per-counter description. Cutting these to one-liners would create a second convention.
3. **`quotes-s213.md` carries its 13 quotes twice (table + "Consumable JSON").** A real consumer exists — `w1/B26FetchRecheck.md:71` re-checked every quote against the snapshot through the JSON block — so the duplicate is justified. Forward condition for B06: if `check_desc_craft.py` reads quote text from the pool instead of recomputing it from `snapshots/optimizing-descriptions.md`, the counter inherits a second authority for quote truth; the pool must stay input, never the verdict's input.
4. **`w2-registry-note.md` at 106 lines.** First of its kind (no `.ufo/waves/round-7*/` precedent), every fenced block is a distinct check (no top-level `report` field; neither path form exists; no add-commit in any ref; no untracked leftover; 63 `.md` + registry = 64 entries; 64 results / 0 empty / 64 unique names). No cut.
5. **`log-draft.md` re-narrating R1–R4 in its Trigger bullet.** Four bullets matching `## Round 71`–`## Round 73` is the fixed shape and the Trigger bullet is the round's own statement of what it was routed. No cut.
6. **`B08-m76-1-round-76-row.md` carrying both 5- and 4-column shapes.** Draft with an explicit "one shape only" disposition and an anchor for each. No cut.
7. **M76-5 (labrat 4 / sonic 1 in the plan's floor vs 0 / 0 dispatched)** is already logged in the lesson with its guard named (the pre-dispatch role validator returning `unknown_role`). I re-measured the roles and confirm the dispatch has 0 labrat and 0 sonic; no new finding, and nothing to add to the row.
8. **`sibling-description-rewrites-round8.md` (497 lines) is not a redundancy target for this entry.** It proposes per-lane rewrite text and derives the omp truncator; the entry re-derives neither (it defers to `skill-listing-thresholds-round54.md` and `render-mechanism-round7.md`). B20ConnOverlap reaches the complementary outside-in conclusion (0 strict sibling hits).

## Right-sizing verdict (Q11) on the final bytes

| entry | lines | words | rules | words/rule |
|---|---|---|---|---|
| `description-craft-round76.md` (final draft) | 98 | 1618 | 5 | ~324 |
| `spec-skill-creation-craft-round74.md` | 141 | 1965 | 6 | 327 |
| `chinese-vendor-skill-surfaces-round73.md` | 92 | 2394 | 4 vendors | — |
| `skill-eval-artefacts-round70.md` | 88 | 1504 | 8 facts | 188 |

Section split of the final draft: header incl. rules table 647, self-audit 489, not-claim 144, limits 225, related 113. The entry is now **inside** the precedent band and denser per rule than the r74 entry it descends from, with a self-audit section that r74 had no equivalent of. Its remaining excess is small and deliberate (the audit is the C1 (d) deliverable). By the same measure the **lesson draft is the round's oversized artifact** — 220 lines / 3041 words against r74's 117 / 1970 — but on the per-disposition figure (+30%, 13.75 vs 10.6 lines per item) that is the cost of disposing 10 defects rather than 7, and O3's preamble cut is already in.

Nothing here changes a claim: the "safe now" items preserved C1 (b) ≥4 quotes (5 present), C1 (c)'s row citations and fragments (3, case-exact), C1 (d)'s two numbers (1022 / 151, untouched), C2 R1's naming duty, and the line budget (593 of 600, margin 7). I edited no lane file and ran no counter as evidence: an unrun check has not passed, and neither frozen counter existed in the tree at any read of this seat.
