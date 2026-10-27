# A28SimplifierRead — read-back attack on the round-76 SKILL.md patch row and the C1 entry

**Axes:** depth, consistency, calibration, freshness, coverage, operability, adjacency.
**Scope:** report only. No lane file written but this one; no counter run (both are absent at the
time of writing — `verifiers/check_desc_craft.py` and `verifiers/check_r75_routed_repairs.py` did not
exist, so no `K of 6` / `4 of 4` / exit code is claimed). No data, no draft, no receipt produced.

## Bytes read (pinned to hashes, because the drafts moved during the pass)

| artifact | path | sha256 | size |
|---|---|---|---|
| patch draft | `.ufo/waves/round-76/build/skill-patch.md` | `253a382e170b3766bc7346dd5311cefb559e3156864f10ae8ea32def09d6f8aa` | 77 lines, 7,944 B |
| entry draft | `.ufo/waves/round-76/build/entry-draft.md` | `6ff08be67d8e20312e541b7467c83f927c6c7f9e20882e015ffe188e77d1e4f9` | 110 lines, 16,163 B (14:03:53 local) |
| quote set | `.ufo/waves/round-76/build/quotes-s213.md` | read for cross-reference | 13 quotes + JSON |
| base | `SKILL.md` at `b7f13f4b39cbd43076a85568adca763a6f674e7a` | — | 590 lines |
| page set | `.ufo/waves/round-76/snapshots/{optimizing-descriptions,evaluating-skills,best-practices}.md` | `7cc54fbb…fd837` / `a799805f…fb684` / `ab9f3b60…fb41` | 13,403/16,973/15,060 B |

Note for the integrator: the entry draft was rewritten once during this pass (the earlier bytes carried
a `:152` citation and a `1 \`NOT <lane>\` clause` count; both are gone from the bytes above). **F14 and
F17 are regressions introduced by that rewrite**; F18's `:152` defect is already closed in the current
bytes. Findings below are graded against the hashes in this table, not against any earlier revision.

## Method (read-back protocol)

For every sentence of the patch's three pins and of the entry, I asked one question: **can a reader with
this file, a shell at the lane root, and no conversation execute or check it?** Three grades:
**EXECUTABLE** (the sentence names its object, its bound and its check), **RECOVERABLE** (one named hop —
a cited file, a heading, a grep — gets there), **UNEXECUTABLE-AS-WRITTEN** (two readings give two
different results, or the object is undefined). Every number I could recompute, I recomputed; the
"verified" list at the end records what survived.

## Findings

### The SKILL.md row (`skill-patch.md` Pin 2 → `SKILL.md` line 219 as read)

**F1 — UNEXECUTABLE-AS-WRITTEN (highest severity).** Row cell 3, sentence 3:
`Re-check the length after each edit — "descriptions tend to grow during optimization" —`. *Length of
what, against which number, measured how?* Two readings of the same file give two answers:

- `.ufo/waves/round-76/snapshots` → the `description:` block occupies **15 physical lines** (frontmatter
  lines 4–18); the YAML folded scalar renders to **1,022 characters**.
- `grep -n '1024' SKILL.md` finds the bound once, at **`:162`** (`## Frontmatter craft — the trigger
  surface`: "`description` ≤1024 chars"), 43 lines above the row and in another subsection. Between lines
  218 and 440 the string `1024` does not occur at all, and `grep -n 'fold'` over the whole file returns no
  measurement convention.

So the row instructs a re-check whose unit is stated nowhere in `SKILL.md` and whose bound is one heading
away. This is not hypothetical: the same ambiguity produced **M75-1 and M76-1** and cost round 76 an
addendum (`plans/round-76-addendum-1.md` § Render-length convention, committed `7eed80e`). The entry gets
this right (rule-table row 6: "count the rendered value, never the frontmatter's physical lines"); the
SKILL.md row — the surface a later author actually reads — drops exactly that clause.
*Smallest fix, in the existing cell:* `Re-check the rendered length (1024 characters) after each edit`.
Four words, no new line.

**F2 — RECOVERABLE.** Same cell: `when an eval miss prompts a rewrite`. `eval miss` is not a term of art
in `SKILL.md`. The hop exists and is short: line 193 names `evals/evals.json` and `should_trigger`, and
the entry's rule-table row 8 supplies the actionable form. *Fix:* `when a should-trigger eval misses`.

**F3 — RECOVERABLE.** Rule cell: `write the description as an imperative about user intent, and err pushy`.
`err pushy` has a verb with no object; the six sibling rule cells in the same table (lengths 164–260) are
all full clauses. The quote in the next cell supplies the intended sense ("Err on the side of being
pushy"), so a reader recovers it in one pass. *Fix:* `and err toward over-inclusion`.

**F4 — NOTE, no change needed (recorded so it is not "tidied" later).** The source cell
`S213 optimizing-descriptions; \`corpus/knowledge/description-craft-round76.md\`` puts a repo path in the
one column where all six sibling rows carry only `S### pagename`. That is a second convention *and* it is
required: C1 conjunct (c) reads the entry path from the row. The preamble sentence immediately above
(`the description page's row (round 76) is entry …`) is what makes the extra path legible — so the
preamble is load-bearing and must not be trimmed as redundancy.

**F5 — UNEXECUTABLE-AS-WRITTEN (stale against the addendum).** Pin 3, C1 row, verdict cell lists the
digest homes as `snapshots/MANIFEST.sha256`, `snapshots/fetch-record.json` and `the in-file digest table` —
**three** homes. `plans/round-76-addendum-1.md` (committed `7eed80e`, before this draft was written) fixes
**four**, the fourth being "the round-76 lesson `## Gate` access record". A counter built from this row
checks three and passes; the addendum's conjunct (a) requires four. The registry row is the surface the
next round reads to learn what this gate checks. *Fix:* append `and in the round-76 lesson \`## Gate\`
access record` to the cell.

**F6 — UNEXECUTABLE-AS-WRITTEN (contradicts the addendum).** Pin 3, C2 row: `receipts/r1-folded-render.txt`
`printing 1022 recomputed from the measured SKILL.md`. The addendum's closing rule is explicit: "Every
receipt that prints the number must print both variants (clip 1022 / stripped 1021) and name the
convention". The row's wording permits a receipt that prints only 1022 — the exact off-by-one the
addendum exists to prevent. *Fix:* `printing clip 1022 / stripped 1021 with the convention named`.

**F7 — UNEXECUTABLE-AS-WRITTEN (path convention).** Both registry rows use wave-relative paths
(`snapshots/MANIFEST.sha256`, `receipts/r1-folded-render.txt`, `receipts/noharm-at-tip.txt`,
`w2-registry-note.md`) while the registry's existing rows use repo-root-relative paths — `.ufo/waves/
round-73/snapshots/MANIFEST.sha256`, `.ufo/waves/round-74/receipts/sibling-heads-freeze.tsv` (5 such cells
between lines 451 and 512). Worse, the C1 row is internally inconsistent: its *pinned-values* cell uses
`.ufo/waves/round-76/snapshots/MANIFEST.sha256` and its *verdict* cell the bare `snapshots/…`. A reader at
the repo root resolves none of the bare ones. *Fix:* prefix `.ufo/waves/round-76/`.

**F8 — the draft's own integration instruction yields the wrong artifact.** Pin 1 says "Replace the
existing two-line paragraph with **these three lines**"; the code block it points at is **four** lines, and
the draft's header arithmetic (`+5 → 595`) only closes with four (2→4 preamble, +1 row, +2 registry). I
rendered the three pins on a scratch copy of the base: **590 → 595**, preamble `206`–`209`, new row `219`,
new registry rows `516`–`517`, `## Gate registry` `448` — matching the draft's *anchor* claims exactly and
contradicting its "three lines" prose. An integrator who trusts the prose lands on 594 lines with every
post-row anchor one line early. *Fix:* say four.

**F9 — ordering hazard, unstated.** Pin 3 names two verifiers that do not exist yet. `check_gate_registry.py`
("compares rows with files", `SKILL.md:449`) treats a `verifiers/*.py` row with no such blob as a **PHANTOM
row** and requires `0=clean`/`1=failed` plus an exact active `--self-test` handler in the file. The patch
must therefore land in one commit with both verifier files; the draft's "out of this seat" list reads as if
they land separately. *Fix:* one sentence in § Scope notes.

**F10 — calibration note, not a defect.** The row is 540 characters; the six rows it joins are 164–260.
Gate-registry rows in this file run to 809, so 540 is inside the file's tolerance; splitting it into two
rows would cost +1 line (596, still inside the 600 box) and is optional.

### The entry (`entry-draft.md`, `6ff08be6`)

**F11 — UNEXECUTABLE-AS-WRITTEN (undefined column) → deletion candidate.** Rule-table header (line 22):
`| page | S id | rule | quote | location | tokens | action |`. `tokens` is undefined and mixed: for six
rows it holds the page's **bolded bullet label** (`Use imperative phrasing`, `Keep it concise`, …), for the
pushy row it holds **the quote itself**, and for the 1024 row a substring of the quote. Nothing reads it:
the `recheck:` tokens (line 3) are quotes, not this column, and conjunct (b) counts `quote` cells. A reader
cannot tell whether it is a count, a search string, or a label. *Fix:* delete the column (8 cells + header,
zero informational loss), or rename it `page's bullet label` and blank the two rows that repeat their quote.

**F12 — UNEXECUTABLE-AS-WRITTEN (miscount, and the reconciler was dropped in the rewrite).** Lines 41–42:
`Counts from the same render … 9 sibling lanes named`. Measured on the render: **10** distinct lane names —
`kagi, kake, kasegi, kengaku, kumitate` (sentence 4), `chousa, kama, kengaku, tameshi, tsukuroi` (sentence
5), `kotodama` (sentence 6, the `NOT kotodama-shokunin` clause) → 9 + 1. The earlier revision carried
`1 \`NOT <lane>\` clause` beside the 9, which reconciled the count; the current bytes dropped it, so a
reader who recounts gets 10 against a stated 9 with no rule to resolve it. *Fix:* `9 sibling lanes named
plus the one negated lane (kotodama) in sentence 6`.

**F13 — RECOVERABLE (unit unstated).** Line 50 (pushy verdict): `8 quoted trigger phrases in 149 characters
plus 3 anti-trigger categories in 153`. The 8 phrases total **108** characters; 149 and 153 are the lengths
of sentences 2 (`Triggers:`) and 3 (`Anti-triggers:`) of the render — both verified. So the numbers are
right and a careful reader lands on the sentence-length reading, but only by trial. *Fix:* `in the
149-character \`Triggers:\` sentence … in the 153-character anti-trigger sentence`.

**F14 — coverage regression in the rewrite.** The rule table admits **8** rules; the audit table rates
**7**. `:157` (anti-overfit) has no verdict row — the earlier revision had one (`not applicable yet`).
Conjunct (d) only compares the two measured values, so nothing mechanically notices. A reader cannot tell
deliberate omission from forgetfulness. *Fix:* restore the row, or say in § Limits that the audit covers
7 of the 8 admitted rules and why.

**F15 — two comparison rules in one sentence.** Line 19: `Every quote below is a literal substring of one
line …: no join across lines, no dropped bytes, whitespace-collapsed comparison only.` The first clause and
the last clause describe different checks (single-line substring vs collapsed comparison), and a counter
must implement exactly one. All 13 quotes satisfy the strict one (I checked 8 of them word-bounded:
`1 / 0 / 0` in the three snapshots each). *Fix:* delete `, whitespace-collapsed comparison only` — it buys
nothing and licenses a looser check than the sentence before it.

**F16 — the recheck guards 7 of the 8 admitted rules.** Line 3's token list has seven entries covering the
header quote and rule rows 1–6; rows 7 (`:159` growth) and 8 (`:157` anti-overfit) are admitted in the
table but have no drift token, so a page edit there passes the recheck silently. *Fix:* add
`'descriptions tend to grow during optimization'` and `'Avoid adding specific keywords from failed queries'`
(the earlier revision had both), or state the 7/8 coverage.

**F17 — line range truncates the block it cites (rewrite regression).** Line 20: `its worked "After" block
(\`:184\`–\`:188\`)`. The block is `:184`–`:189` (`:184` `description: >` … `:189` `explicitly mention "CSV"
or "analysis.""`, fence at `:190`); the earlier revision's `:179`–`:190` was the whole snippet. The
consequence is concrete: the audit's own "even if they don't explicitly mention" reference (row 4's
unnamed-domain verdict) lives on `:189`, outside the cited range. *Fix:* `:184`–`:189`.

**F18 — closed in the current bytes (recorded for the record).** The earlier revision cited
`corpus/knowledge/frontmatter-trigger-surface.md:152` for "`description` craft is audit-hygiene, not routing
surface"; the phrase actually spans `:153`–`:154` (`:154` verified) and is not a single-line substring. The
current revision cites `:153`–`:154` — correct. No action; do not "restore" the old citation from an older
report.

**F19 — inherited wording, not this round's defect.** Line 3 / § Limits: `any 0 means the page moved or the
fetch failed` and `the recheck line counts tokens, and a 0 there is a re-open of the page`. The command
greps the **local snapshot** and never fetches: a zero can only mean the snapshot changed, never that the
URL moved. The wording is copied verbatim from `corpus/knowledge/spec-skill-creation-craft-round74.md:5`
(same phrase), so fixing it here alone would create the divergence the consistency axis penalises. *Route:*
lane-level wording item (a digest re-compare step: `sha256sum -c .ufo/waves/round-76/snapshots/MANIFEST.sha256`),
out of this round's scope.

**F20 — NOTE (true, reader-ambiguous).** `ground:` (line 4): "`verifiers/` held no counter for the
`description` field's **wording**". `verifiers/check_description_thresholds.py` exists at base and counts
description *thresholds*; the same entry cites it later. The qualifier "wording" carries the entire
distinction — keep it, and do not let a compressor drop it.

**F21 — small adjacency note.** `source:` (line 1) attributes the `:9` located quote under `§ How skill
triggering works (\`optimizing-descriptions.md:13\`)`; `:9` is the page's opening paragraph, above that
heading, and `:13`–`:17` is what the section actually says. One word ("opening paragraph, before `:13`")
makes the attribution exact.

## Deletion candidates (simplifier output, none executed — report only)

| # | candidate | evidence it is dead weight | risk of deleting |
|---|---|---|---|
| D1 | entry rule-table `tokens` column (F11) | read by no recipe, no conjunct, no counter; duplicates the quote in 2 of 8 rows | none found; if it was meant as the recheck's token list, the recheck already carries its own |
| D2 | `, whitespace-collapsed comparison only` (F15) | contradicts the sentence's own "literal substring of one line" | would loosen a check if kept, so deleting is the strict direction |
| D3 | "these three lines" (F8) | contradicted by its own code block and by its own `+5` arithmetic | none; replacing it with "four" is the fix |
| D4 | `(6 name a skill artifact, 2 do not)` in the counts line | repeated verbatim by the unnamed-domain verdict ("2 of the 8 phrases (`trigger words`, `prompt craft`) avoid the artifact nouns") — one home per fact | keep the verdict copy, drop the counts copy |
| D5 | `\`:159\`, line only, no quote here` in the verdict-table location cell | meta-annotation about the artifact, not information for the reader; `:159` suffices | low value either way; not worth a change on its own |

## Verified true (what a reader *can* execute, with the command I ran)

| claim | check | result |
|---|---|---|
| three snapshot digests | `sha256sum` on all three | `7cc54fbb…fd837` / `a799805f…fb684` / `ab9f3b60…fb41` — equal to `MANIFEST.sha256` and to the entry |
| page size | `wc -lc optimizing-descriptions.md` | `196 13403` — matches the entry |
| 8 rule-table quotes are page-unique | `grep -c -F` per quote × 3 snapshots | `1 / 0 / 0` for all 8 |
| located quote `:9`, 20 words | `sed -n 9p`; word split | present, 20 words, page-unique |
| render length 1022 / 1021 | `yaml.safe_load` of the frontmatter, `len()` | 1022 clip / 1021 stripped — the addendum's convention reproduced |
| first sentence 151 | same render, first `. ` boundary, period included | 151 |
| 148 words, 7 sentences | whitespace split / period split | 148 / 7 |
| 8 phrases, 3 anti-triggers, 87-char sentence 7 | same render | 8, 3, 87 — all match |
| 149 / 153 sentence lengths (F13) | same render | sentence 2 = 149, sentence 3 = 153 |
| recheck recipe | ran line 3 verbatim from the lane root | seven `1`s, exit 0 |
| base sweep `0 files` | `git grep -l -F` at `b7f13f4` over `SKILL.md corpus/knowledge corpus/QUALITY.md` × 5 phrasings | 0 files each |
| `frontmatter-rule-authorities-round48.md:44` | `sed -n 44p` | "description length … `MAX_DESCRIPTION_LENGTH = 1024`" — supports the citation |
| `skill-listing-thresholds-round54.md:15`–`:16` | `sed -n 15,16p` | "Four clients document 1,024 … None … documents a cut" — supports the citation |
| S213 row anchor + `used-by` | `sed -n 153p corpus/SOURCES.md` | "Running multiple times" subsection; `used-by` = `skill-eval-artefacts-round70.md` — matches `ground:` |
| patch anchors | scratch render of the three pins on base | 590 → 595; preamble 206–209; row 219; registry 516–517; `## Gate registry` 448 |
| new row's 3 quote fragments | `grep -c -F` | `1 / 0 / 0` each |
| registry row conformance (shape) | `check_gate_registry.py` rules 26–44 read | 8 cells, `gate`, `0=clean` + `1=failed`, `--self-test`, pinned cell carries a backticked existing path, owner `kotoba` — conformant *once the files land* (F9) |

## Preserved contract

Nothing in either frozen predicate is touched or weakened by this report: C1's 6 conjuncts, C2's 4
repairs, the controls (C1-W1..W3, C2-W1) and the no-harm battery are as committed. All fixes above are
cell-level edits inside text the plan already names; none adds a line except the optional F10 split and
the optional F14/F16 restorations, which fit inside the 5-line budget margin (595 → up to 598).

## Tradeoffs

- F1's fix lengthens the row by four words and **restates** the entry's measurement clause. That is
  deliberate duplication: `SKILL.md` is the surface an author reads before touching a description, and the
  entry is where the audit lives; the duplication is the same one the lane already accepts between the
  portability floor (`:162`) and the client table (`:166`–`:176`). If the lane prefers one home, the
  alternative is a pointer (`count the rendered value, see \`corpus/knowledge/description-craft-round76.md\``)
  — same words, one more hop for the reader.
- F12's fix adds a clause to a count line; the cheaper option is to make the counts line stop at 9 by
  deleting the `NOT` clause from the render — not available, because the description is out of this
  round's touch list.
- F7 rewrites four cells to full paths; that is a path-convention correction, not new content, and it is
  the only fix here that touches the registry's *shape* rather than its words.

**Tooling:** none installed, no package manager run, no network fetch. Scratch `/fast/scratch/hyaku/
kotoba-r76/A28SimplifierRead/` (base copy, patched renders) was removed; nothing under `/tmp` is cited.

VERDICT: A28SimplifierRead — advisory HOLD on box-3 ("Instructions executable ... without oral context") as drafted: 3 sentences UNEXECUTABLE-AS-WRITTEN (F1 row length re-check; F5 registry conjunct-(a) digest homes; F6 registry 1022-only receipt), 1 integration instruction that produces the wrong artifact by one line (F8), 1 unstated same-commit ordering hazard (F9), 3 recoverable in one hop (F2, F3, F13), 5 deletion candidates (D1-D5, none executed), and 0 fabricated numbers found in either draft — every checkable figure in the entry reproduced from committed and fetched bytes.
