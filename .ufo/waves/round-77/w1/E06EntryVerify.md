# E06EntryVerify — C1 knowledge entry finalized and verified against the frozen counter

Seat: E06EntryVerify (executor, round 77 w1). Claim: **C1 depth (sourced)** — the entry
`corpus/knowledge/description-craft-round76.md`. Scope: the entry only; every other landable file
(SKILL.md row, SOURCES cell, lesson) is another seat's and was used here as a scratch **stand-in**.

## Evidence base

- Lane HEAD (freeze): `6523aced1ee0ebe07dca996213bdc645a6acbd1e`; r77 claim base:
  `2f675548eaad2a037a899d39247c1fd7a88aaf48`. `git diff --stat 2f675548 6523aced -- SKILL.md
  corpus/SOURCES.md .ufo/waves/round-76/snapshots/` prints nothing → the measured bytes and the
  snapshot set are identical at base and freeze tip.
- Counter: `verifiers/check_desc_craft.py`, sha256 `cf3c45d9e3985f11889816f4bb371dc0d5541c10c09ce2ab3966a4bff4603b9e`,
  `--print-self-sha` matches its in-file `SELF_SHA` (`True`). Not edited by this seat.
- Scratch: `/fast/scratch/hyaku/kotoba-r77/E06EntryVerify/` (clone `--shared`, user.name/email set
  before the first scratch commit, `rev-parse --show-toplevel` = the clone dir). Removed before yield.
- Snapshot bytes verified by digest, not trusted: optimizing-descriptions 13,403 B / 196 lines /
  `7cc54fbb…bd837`; evaluating-skills 16,973 B / `a799805f…fb684`; best-practices 15,060 B /
  `ab9f3b60…fb41` — each equals the counter's pinned `PAGE_SHA`.

## Audit values recomputed from lane bytes (not copied from the draft)

`verifiers/check_desc_craft.py` `description_measures(SKILL.md)` at the clone of lane HEAD →
**clip 1022 / stripped 1021 / first sentence 151** (`:1470` counter lines 355–377). Description block =
file lines 4–18 (15 source lines), key at line 3 (`description: >`), `frontmatter_lines` = 17 lines.
The entry states exactly 1022 and 151, and names 1021 as the stripped variant.

## Quote verification (every quote, independently)

Method = the counter's own rules applied to the committed bytes: literal substring of **one** physical
line after whitespace collapsing, 3–25 words, occurs below the page's first heading (line 5), absent
from both other snapshots, and on a line the entry itself cites. Receipt:
`receipts/E06EntryVerify.quotes-verified.txt` (one row per span, with `COUNTED`/`skipped`).

| quote | words | line | page-unique | counted |
|---|---|---|---|---|
| "An under-specified description means the skill won't trigger when it should; an over-broad description means it triggers when it shouldn't." | 20 | 9 | yes | yes |
| "Frame the description as an instruction to the agent" | 9 | 25 | yes | yes |
| "Describe what the user is trying to achieve, not the skill's internal mechanics." | 13 | 26 | yes | yes |
| "Err on the side of being pushy" | 7 | 27 | yes | yes |
| "Explicitly list contexts where the skill applies, including cases where the user doesn't name the domain directly" | 17 | 27 | yes | yes |
| "A few sentences to a short paragraph is usually right" | 10 | 28 | yes | yes |
| "enforces a hard limit of 1024 characters." | 7 | 28 | yes | yes |
| "typically only consult skills for tasks that require knowledge or capabilities beyond what they can handle alone" | 17 | 19 | yes | yes |

Total counted at the tip = **11** (the eight above plus three sub-fragments the recheck token list also
quotes). Eight are genuine body quotes on eight distinct cited lines; the 4-quote floor is cleared by
body quotes alone.

Other page claims re-checked on the bytes: the four principles are the bullets at `:25`–`:28`; line 17 is
the trigger-burden sentence; line 19 opens "One important nuance:"; the worked example spans `:184`–`:189`
with the imperative clause at `:186`–`:188` and the reading at `:192`; `front-load` / `front load` /
`use case` / `lead with` / `starts with` / `first sentence` / `self-contained` / `self contained` = 0 hits,
the only `front` hits being `frontmatter` at lines 9 and 173.

Lane claims re-checked: 8 quoted trigger phrases with 108 characters of inner quoted span and 7 sentences
in the rendered description (regex over the render); `check_sibling_census.description_of` and
`verify_harness_claims`' `len(re.sub(r"\s+", " ", desc).strip())` both return **1021** on these bytes;
`corpus/knowledge/frontmatter-trigger-surface.md:153`–`:154` is the two-line sentence "`description` craft
is audit-hygiene, not routing surface"; the five-phrase ground sweep at `2f675548` returns 0 files for each
phrase; the nine recheck tokens each `grep -c -F` = 1 (exit 0).

## C1 counter at a scratch tip (entry + minimal stand-ins)

Scratch tip `d97d5bd61c092a44141fb2491e3a504c1babbb19` = lane HEAD + my entry + (stand-ins) the
`skill-patch.md` § Body craft row, the S213 `used-by` append, and `corpus/lessons/round-76.md` from
`lesson-draft.md` with `<freeze>`/`<tip>` substituted and its HTML comment stripped.

```
$ python3 -B verifiers/check_desc_craft.py --repo <clone> --rev d97d5bd
(a) snapshot chain: pass
(b) located quotes: pass
(c) act-on: pass
(d) self-audit: pass
(e) registry: pass
(f) provenance: pass
description craft backed 6 of 6
exit=0
```
Receipt `receipts/E06EntryVerify.c1-tip-6of6.txt`.

Per-conjunct attribution (mutants, receipts beside them):

- **(a) snapshot chain** — independent of my file: snapshots + manifest + fetch record + in-file digest
  table are committed at HEAD; needs the lesson `## Gate`. **The r76 `lesson-draft.md` as written fails
  (a)**: its Gate quote is wrapped in inner backticks (`"`A few sentences…`"`), so the counter's
  `quote_spans` sees a span containing backticks that is not in the page
  (`(a) the lesson Gate carries no <=25-word quote located in the optimizing-descriptions snapshot`,
  `…backed 5 of 6`, exit 1). De-backticking that one span in the stand-in turns the counter green; the
  landed lesson must drop the inner backticks.
- **(b) located quotes** — mine. Absent entry → `3 of 6`, exit 1 (`c1-m1`). Rule table carrying real
  text from the wrong page (best-practices lines, everything else de-quoted) → `(b) … carries 1 located
  page-unique quote(s) of the required 4`, `5 of 6`, exit 1 (`c1-m3d`).
- **(c) act-on** — the `skill-patch.md` row (447 chars) satisfies it; my entry name must match the path
  the row cites (`corpus/knowledge/description-craft-round76.md`).
- **(d) self-audit** — mine. Audit row changed 1022 → 1023 → `5 of 6`, exit 1 (`c1-m2`).
- **(e) registry** — stand-in SOURCES append + lesson old→new paragraph; both parse.
- **(f) provenance** — mine; `entry_head` returns `verified-at: 2026-10-27`, `recheck:` present, source
  line carries S213 and the URL (absent entry fails it).

## Counter slack observed (routed, not mine to fix)

`quote_spans(entry)` runs over the whole entry, including the provenance block. The `recheck:` line's
double-quoted tokens are themselves located page-unique quotes, so a world whose rule table quotes the
**wrong page** still prints `6 of 6` when the recheck tokens are present (`c1-m3a`, `c1-m3b`, exit 0);
only after the recheck tokens are also de-quoted does `(b)` fail (`c1-m3d`). Consequence: `(b)` proves
"the entry quotes the page ≥4 times", not "the rule table's quotes are the page's". A w2 falsifier should
test exactly this; my entry does not rely on it (8 body quotes), but a hollow entry could.

## Every change from `.ufo/waves/round-76/build/entry-draft.md`, with reason

(1) Stale base hash `b7f13f4` → `2f675548…` in § ground and § This lane's own `description`, measured, with
the byte-identity check (`git diff --stat 2f675548 6523aced -- SKILL.md` empty) stated in both places —
r77's base is `2f675548` and the draft asserted coverage at a revision two rounds old. (2) The § ground
phrase sweep was re-run at the new base with the literal command and its result (`0 files` for each of the
five phrasings), replacing an unlabelled "matched 0 files". (3) `source:` tail reworded: the loop counsels
at `:157`/`:159` are "recorded here as corroboration, not tabulated as rules" — the draft said "recorded,
not admitted", which contradicted the § Body craft row that quotes `:159` and `:157`. (4) "the caution at
`:19`" → "the nuance at `:19`" (line 19 opens "One important nuance:"). (5) Opening sentence rewritten:
the draft's "§ Writing effective descriptions is four principles for the field that decides whether a skill
is read at all (`:17`)" is ungrammatical and pins the four principles at a line that does not hold them; now
"four bulleted principles (`:25`–`:28`) for the field that decides whether a skill is read at all (`:17`)".
(6) Both baseline digests normalized to one abbreviation shape (`a799805f…99fb684`, `ab9f3b60…b87fb41`) —
the draft's first had a 5-character tail and the second a 4-character tail. (7) Added the sentence that the
page's first heading is line 5 and every quote sits below it — the `after_first_heading` arm the draft only
asserted. (8) Added the accounting sentence naming the `:17`, `:19` and `:28` bound sentences, so every
quoted span in prose is attributable. (9) The audit section's "Measured at base `b7f13f4` … so the counter's
recomputation at the measured tip governs" now names both the r77 base and the freeze tip, states that the
§ Body craft row lands below the description block, and keeps the recompute-governs rule. (10) The
first-sentence row now cites its committed convention home (`plans/round-76-addendum-4.md`). (11) Imperative
verdict row: the draft quoted sentence 1 with backticks the render does not contain; replaced with the exact
render text and "seven sentences" (counted). (12) Unnamed-domain verdict: "2 of the 8 phrases … avoid the
artifact nouns" replaced with the counted shape — 5 of 8 contain `skill`, 1 more names the field
(`frontmatter description`), only `trigger words` and `prompt craft` name neither. (13) The
`frontmatter-trigger-surface.md` citation now says the quoted sentence joins across the two cited source
lines (it is a two-line sentence). (14) Worked-example range `:184`–`:188` → `:184`–`:189`, with the
imperative clause located at `:186`–`:188` — the draft's range cut the example before the clause ends.
(15) The absence sweep is now a runnable case-insensitive list with the `frontmatter`-only caveat (lines 9,
173) — the draft asserted 0 hits without the two-hit qualification. (16) The closing bullet of § What this
entry does not claim was rewritten to name `:157`/`:159` as loop procedure carried by the § Body craft row,
resolving (3). (17) § Limits now states how the 1021 reading was produced (`len()`, measured at
`6523aced`). (18) The draft's `<!-- build note … Strip this comment on landing -->` is removed — this file
is the landing copy. (19) `recheck:` extended with the run context ("run from a shared clone of this lane
at `6523aced`, exit 0") and its nine tokens were executed verbatim; the token list itself is unchanged.

## Operability for the integrator

- Landing the entry adds an unindexed corpus file: with the entry present,
  `verify_corpus_integrity.py --json` reports `unindexed: 4`
  (`corpus/knowledge/description-craft-round76.md`, `corpus/lessons/round-75-verifier-spotcheck.md`,
  `corpus/lessons/round-76-verifier-spotcheck.md`, `corpus/lessons/round-76.md`) — the entry and the new
  lesson need `corpus/README.md` rows in the same landing (R76-D4's touch list already carries
  `corpus/README.md`). Receipt `receipts/E06EntryVerify.corpus-integrity-with-entry.txt`.
- `sources-census.sh validate --file <clone>/corpus/SOURCES.md --today 2026-10-27` → `file ok`, exit 0,
  one pre-existing `W04 S213 duplicate url` (the row is re-used, no new row).
  Receipt `receipts/E06EntryVerify.census-sources-row.txt`.
- The entry path is the counter's constant: it must land at `corpus/knowledge/description-craft-round76.md`
  (round number is the counter's, not this round's).

## Risks

- (a) still depends on a lesson Gate quote **without** inner backticks and on a lesson that exists at all;
  `corpus/lessons/round-76.md` does not exist at lane HEAD (the r76 wave stopped before data).
- (c) depends on the § Body craft row landing with the entry path and `S213` in the same row and ≥2 located
  fragments; `skill-patch.md` satisfies this today, and any rewording must re-clear it.
- The `(b)` slack above is a counter property, not an entry property; my entry clears (b) with body quotes
  alone, but a w2 critic should attack the recheck-token path.

## Tooling

No installs, no upgrades, no pacman (host-wide pause respected). Python 3 stdlib + git only.

## Verdict

The entry is final, quote-verified against committed snapshot bytes, audit-verified against recomputed
lane bytes (1022 / 1021 / 151), and drives the frozen C1 counter to `description craft backed 6 of 6`,
exit 0, in a scratch world with stand-ins for the other seats' files.

VERDICT: C1 entry finalized and verified — 6 of 6 conjuncts pass at a scratch tip (`d97d5bd`), exit 0; three entry-level falsifiers fail as designed; blockers routed (lesson Gate backticks, README index rows, counter's recheck-token slack in (b)).
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/E06EntryVerify.description-craft-round76.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w1/E06EntryVerify.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/receipts/E06EntryVerify.commands.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/receipts/E06EntryVerify.c1-tip-6of6.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/receipts/E06EntryVerify.c1-m1-entry-absent.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/receipts/E06EntryVerify.c1-m2-audit-1023.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/receipts/E06EntryVerify.c1-m3d-wrong-page-table.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/receipts/E06EntryVerify.c1-m3a-prose-fragments-carry-b.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/receipts/E06EntryVerify.c1-m3b-recheck-tokens-carry-b.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/receipts/E06EntryVerify.quotes-verified.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/receipts/E06EntryVerify.corpus-integrity-with-entry.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/receipts/E06EntryVerify.census-sources-row.txt
