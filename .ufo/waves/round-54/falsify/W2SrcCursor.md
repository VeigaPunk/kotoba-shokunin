Result: HOLDS — every Cursor cell lands: the S058 quote is verbatim at `release-notes.md:122`, the fetch record reproduces byte-for-byte 40 minutes later, the reading and SKILL.md cells stay inside the quote plus seat evidence, and no older lane row contradicts.

Seat: KotobaR54.W2SrcCursor (falsify wave). Scope: the Cursor rows landed at
`5a097e12b9409a1f425fbc76334f36f1402eb4cc` — `corpus/SOURCES.md` S058 (line 71),
`corpus/knowledge/skill-listing-thresholds-round54.md` § Per-client record (line 44 at HEAD),
`corpus/lessons/round-54.md` § Gate (line 28) plus its `### Rejected` record (line 41), and
`SKILL.md` § `### Description thresholds by client` (line 190). All judged on the committed
state at `5a097e12`/`58db81c` (the lane working tree carries later uncommitted edits; the
committed Cursor rows are unchanged under that diff — verified with `git diff HEAD`).

No lane edits, no git writes in the lane, no installs, no paid model calls. Sandbox:
`/fast/scratch/hyaku/kotoba-r54/W2SrcCursor/clone` at `5a097e12`; fetches under
`/fast/scratch/hyaku/kotoba-r54/W2SrcCursor/fetch/`. Sources opened with `curl` only.

## 1. Re-open of the source (falsify's own fetch record)

All fetched 2026-10-22T22:00:48Z with `curl -sS -L -A 'Mozilla/5.0 kotoba-research/54-falsify'`:

| URL | status | bytes | sha256 | matches S058 record |
|---|---|---|---|---|
| `https://cursor.com/docs/release-notes.md` | 200, `text/markdown` | 301,193 | `fd4d830aa5b02cd79d4c3ac485eb01d31ebb7436f152e27496e7cb02a23d82cd` | yes, byte-identical to the 21:19:23Z record |
| `https://cursor.com/docs/cli/changelog.md` | 200, `text/markdown` | 56,159 | `70d57616d76ddfa089d42b23a149fad68436ecd8711a94b33c13c3c64795167b` | yes (seat-recorded hash) |
| `https://cursor.com/changelog.md` | 200, `text/html` | 186,595 | `c228239ef746ae0876c87d9e879d8129dc1f84219fe104ff50123c72def779ab` | confirms the `### Rejected` record: `grep -c -i skill` → 0 |
| `https://cursor.com/docs/skills.md` | 200 | 18,477 | `a642fa96776c247dba126a325e1dd73dac3f532a70060e745fb9bbd5b377602d` | yes |
| `https://cursor.com/docs/agent/prompting.md` | 200 | 4,485 | `438f77bf7295d28002c81ce0658134ce7debe6dfa76bae926058b918ed378410` | yes |
| `https://cursor.com/help/customization/skills.md` | 200 | 6,569 | `7d551fc7939d4632228c7f178f89475113a1ad503000f890271ee95a4aee3a49` | seat's supporting page |
| `https://cursor.com/llms.txt` | 200 | 24,815 | `38cc4995af1037fea4daa16f4b2ed1062a4c21df63440e5703608eec1017085d` | sweep index |

The seat's 21:19:23Z UTC timestamp is not re-derivable but is consistent with the commit's
committer time (21:27:14Z); bytes and sha256 are reproduced exactly.

## 2. Quote and location — HOLDS

- Quote verbatim: `grep -Fbo` on the fetched bytes finds the recorded string at byte offset
  21,968, on line 122 (the seat reported offset 21,968 — reproduced). Word count: exactly 25
  (`wc -w`), the counter's `MAX_WORDS` ceiling, within 3–25.
- Anchor: `## v2026.10.08` is line 110, `### Skills` line 120, the bullet line 122 — the SOURCES
  anchor `release-notes.md:120-122` and the entry/Gate location `release-notes.md:122` are exact.
- Same-sentence claim: `diff` of `cli/changelog.md:17` vs `release-notes.md:122` →
  `SENTENCE-IDENTICAL`; the SOURCES anchor's "byte-identical" wording HOLDS.
- The bullet's fourth item ("a body over about 5,000 tokens") is verbatim-present; the SOURCES
  anchor's mention of it HOLDS.
- The number is about a skill `description`: the clause is "a description over 1,024 characters"
  inside a bullet headed "Agent Skills limits" linking to the SKILL.md format. The other two
  numbers in the sentence (64 chars → `name`, ~5,000 tokens → body) are not used as the Cursor
  threshold anywhere. No wrong-field substitution.

## 3. Cell-by-cell verdicts

**SOURCES S058** — HOLDS. 11 cells; `docs`/tier `A`/`mined`/`opened 2026-10-22`/`90d`/`used-by`
the entry; URL host `cursor.com` is a pinned Cursor host (`HOSTS["Cursor"] =
("cursor.com","docs.cursor.com")`, `check_description_thresholds.py:98`). `scope` and `teaches`
cells paraphrase the bullet accurately and stay inside it (they under-list the items, never
overstate; "a folder-name mismatch" compresses "a frontmatter `name` that doesn't match the
folder"). Opened-this-round guard (erratum 3a): `git show e3371548:corpus/SOURCES.md | grep -c
S058` → 0.

**Entry row (`:44`)** — HOLDS. `row` = S058; `location` `release-notes.md:122` exact. `reading`:
"Authoring maximum, not a listing cut" is the entry's own three-way taxonomy; "an over-length
description still loads" is verbatim-supported ("Skills that load but exceed the spec's limits
now show a yellow warning count"); "no truncation, shortening, drop or refusal is documented" is
a documented-absence claim backed by the seat's three-leg Q30 sweep (`SrcCursor.md` §5: changelog
+ release notes, all 168 docs + 109 help pages indexed by `llms.txt`, lane corpus) and by my own
re-sweep of every skill-bearing page in `llms.txt` (`skills.md`, `help/customization/skills.md`,
`analytics-api.md#skills-adoption`, `agent/prompting.md`, `release-notes.md`,
`cli/changelog.md`): zero hits for description cut/truncate/shorten/budget/drop.

**SKILL.md row (`:190`)** — HOLDS. Threshold `1,024 characters for description` matches the
quote's number token. "Past the threshold" (committed text): "Warned, not cut: the skill still
loads and `/skills` shows a yellow warning count listing what to fix (a body over about 5,000
tokens is warned the same way)" — every clause verbatim-supported; "not cut" is the verified
documented absence. Action "Keep `description` at or under 1,024 characters; move detail into
`references/` rather than the body" is prescriptive but consistent: `references/` is a documented
Cursor skills directory ("Additional documentation loaded on demand", fetched
`skills.md:267`; tree at `:99`) and the body is warned past ~5,000 tokens.

**Gate row (`round-54.md:28`)** — HOLDS. URL, UTC, 301,193 B, full sha256, quote and
`release-notes.md:122` all match my independent fetch and the entry quote byte-for-byte; seat
`SrcCursor` matches the build report.

**`### Rejected` record (`round-54.md:41`)** — HOLDS. `cursor.com/changelog.md` re-served as HTML
(200, 186,595 B) with `grep -c -i skill` → 0; the "false silence" reason is accurate — the
skill-limit sentence exists only on `docs/release-notes.md` and `docs/cli/changelog.md`.

## 4. Contradiction sweep — HOLDS

No older row contradicts S058. `S049`/`S052` (Cursor rules files) and
`alwayson-rule-files-round53.md:69` ("Cursor: Keep rules under 500 lines") cover rule files, a
different object. `skill-selection-rules-round50.md:46` lists 1,024-character `description` caps
without naming Cursor (verified on the full line). `instruction-surface-census-round13.md` Cursor
hits are omp loader classes, not client skill limits. The generic 1,024 portability floor
(SKILL.md, present at the plan commit, `grep -c -F '1,024'` → 1) is consistent with — and now
attributed for Cursor by — this row.

## 5. Counter re-run (sandbox clone at `5a097e12`)

```
python3 -B verifiers/check_description_thresholds.py --rev 5a097e12…
  Cursor       BACKED   →  description thresholds backed 7 of 7 clients   exit 0
python3 -B verifiers/check_description_thresholds.py --rev 5a097e12… --fetch
  Cursor       BACKED found=True   →  found on the live page 7 of 7       exit 0
```

Erratum-3 guard (c) HOLDS for Cursor (`found=True`). Guard (b) note: Cursor's number is not new
ground (`1,024` already in SKILL.md's portability floor at `e3371548`); the claim-level
two-new-clients requirement is met by other clients (Codex `2%`/`8,000` count 0 at the plan
commit), so this is no row defect — recorded for the judge's guard accounting.

## 6. Residual risk (informational, no break)

- "Authoring maximum" / Findings-1's "document 1,024" mildly blur that Cursor's 1,024 is a
  warn-only limit (the page never forbids an over-length description). The row's own text
  ("still loads", "Warned, not cut") carries the caveat, so this stays within noise; the lane
  working tree already holds a tighter uncommitted rephrasing ("No cut documented; the release
  notes document a warning").
- The quote ends mid-sentence at exactly 25 words — conformant (verbatim substring) but brittle:
  any added word in integration drops the client (seat finding F7).
- The anchor is line-pinned (`:120-122`) on a growing release-notes page; future releases will
  shift the bullet. The row's bytes+sha record makes drift detectable; `recheck 90d` is reasonable.
- My documented-absence evidence re-verifies the five skill-bearing pages, not the seat's full
  277-page sweep; the wider sweep rests on `SrcCursor.md` §5 evidence.

Verdict: HOLDS for all four artifacts. No corrected text needed.
