# R01RevQuotes — independent quotation verification, round-77 w1

Reviewer seat R01RevQuotes, 2026-10-27. Scope: EVERY quotation in
`.ufo/waves/round-76/build/entry-draft.md` and
`.ufo/waves/round-76/build/quotes-s213.md`, checked against the three committed
round-76 snapshots (`.ufo/waves/round-76/snapshots/`, freeze commit `6523aced`,
r76/r77 base bytes — SKILL.md is byte-identical between `b7f13f4` and
`6523aced`, `cmp` exit 0), plus every `optimizing-descriptions.md:N` line
pointer the entry makes.

- Criteria (seat brief): literal substring of ONE line of
  `optimizing-descriptions.md`, whitespace-collapse only, ≤ 25 words, line is
  after the page's first heading, absent from `evaluating-skills.md` and
  `best-practices.md` (whole body, per-line test, chrome included).
- Method: the attached script `R01RevQuotes.verify_quotes.py` (this dir),
  pure stdlib, recomputes everything from bytes; full output in
  `R01RevQuotes.verification-log.txt` (same dir). Script exit code 1 because
  two required checks fail (findings F1/F2 below); every other check passes.
- No LSP device exists in this session's tool inventory; all artifacts are
  markdown, so byte-level script verification is the semantic check here.
  No tools were installed (system `python3` only).

## Result by line (29 quote candidates)

PASS on claimed line, whitespace-collapsed literal, page-unique, ≤ 25 words,
after first heading (line 5):

| ids | snapshot lines | notes |
|---|---|---|
| E01 (entry `source:` located quote) | :9 | 20 words == claimed 20 |
| E02, E03, E04, E05 | :25, :26, :27, :27 | audit-table quote column |
| E06, E07 | :28 | incl. `enforces a hard limit of 1024 characters.` |
| E08 (`even if they don't explicitly mention`), E09 (`:19` caution) | :27, :19 | |
| E10, E11 (fragments) | :28, :25 | |
| Q01–Q13 (quotes-s213 table rows 1–13) | :25, :25, :26, :27, :27, :17, :45, :155, :28, :28, :28, :159, :157 | every claimed word count and line number correct |
| F01–F03 (suggested-min fragments) | :25, :45, :28 | |
| F04 (`Analyze CSV and tabular data files`) | :185 | |

FAIL / defects:

- **R01-F1 — entry-draft.md, audit row "imperative phrasing": sentence-1 quote is not literal.**
  The entry quotes sentence 1 as `"Prompt & skill craft — audits, writes, and
  rewrites `SKILL.md` / `AGENTS.md` / dispatch prompts / system prompts …"`.
  The committed `description` value (folded render of `SKILL.md` at `b7f13f4`
  and at freeze tip `6523aced`, renders identical) contains **no backticks**:
  `… rewrites SKILL.md / AGENTS.md / dispatch prompts / system prompts for
  trigger fidelity and decision density.` The no-backtick form is found; the
  as-written backticked form is found in 0/2 renders. The row's numbers are
  correct against the same bytes (clip 1022 / stripped 1021 / first sentence
  151 — recomputed), so the defect is the quote's punctuation only. Fix before
  landing: drop the backticks in the landed copy of
  `corpus/knowledge/description-craft-round76.md`.
- **R01-F2 — quotes-s213.md § "What the page shows by example": the fragment
  `Use this skill when the user has a CSV, TSV, or Excel file` spans physical
  lines :186–:187** of the snapshot (`… Use this` / `skill when …`). It fails
  the one-line criterion and MUST NOT be lifted into any located-quote row
  (conjunct (b) would reject it). Prose use is accurate; F04 on :185 is fine.
- **R01-F3 (informational) — entry cites the worked example as `:184`–`:188`;**
  the yaml block runs :179–:190 and the After-value ends at :189. The cited
  range stops one line short; the substantive claim (imperative trigger clause
  second, capability clause first, reading at `:192`) verifies exactly.

## Everything else that was verified green

- Snapshot identity: sha256 `7cc54fbb…d837` (13403 B / 196 L), `a799805f…fb684`
  (16973 / 300), `ab9f3b60…fb41` (15060 / 277) — recomputed == MANIFEST.sha256
  (`sha256sum -c`, exit 0) == fetch-record.json (3× HTTP 200).
- quotes-s213.md's consumable JSON: all 13 items match recomputed
  words/line/occurrences/in_evaluating/in_best_practices/after_first_heading/
  chrome_hit field-for-field.
- Page-uniqueness: none of the 13 (+ fragments) occurs in
  `evaluating-skills.md` or `best-practices.md`; zero chrome hits (nothing
  before line 5).
- entry-draft `recheck:` tokens: all nine occur on exactly one snapshot line
  each (so the 90-day recheck loop's `1`-per-token expectation holds on these
  bytes).
- Absence sweeps: `front-load`, `front load`, `use case`, `lead with`,
  `starts with`, `first sentence`, `self-contained`, `self contained`,
  `opening`, `single sentence`, `one-sentence` → 0 hits each (case-insensitive);
  `front` hits exactly lines {9, 173} — both drafts' calibration claims hold,
  so "no front-loading / no self-contained-first-sentence rule" is correctly
  NOT attributed to S213.
- All 20 `optimizing-descriptions.md:N` pointers made by the two drafts
  (:5, :9, :13, :17, :19, :21, :25, :26, :27, :28, :43, :45, :149, :155,
  :157, :159, :184-range, :185, :192) resolve to the cited text on the cited
  line.
- Lane-side quotations (secondary, committed bytes via `git show`): L02
  sentence-7 (`Note: shokunin files sit outside … reads this text.`, exactly 87
  chars) found; L03 "`description` craft is audit-hygiene, not routing surface"
  found in `corpus/knowledge/frontmatter-trigger-surface.md` (`audit-hygiene`
  on :154, entry cites :153–:154 — the quote spans the two lines).

## Conjunct (b) readiness

≥ 4 located quotes required; 13 table quotes pass cleanly. The four the
quotes file recommends for coverage — #2 `Frame the description as an
instruction…` (:25), #8 `If should-trigger queries are failing…` (:155),
#10 `long enough to cover the skill's scope…` (:28), #13 `Avoid adding
specific keywords from failed queries` (:157) — all PASS. (b) is satisfiable
without any of the defective strings.

Not in this seat's scope (left to the assigned seats): audit-row verdicts and
the `8 quoted trigger phrases, 108 characters` claim (A17CritAudit), conjunct
(d) recompute (counter), SKILL.md row fragments beyond the three the quotes
file names (all three verified above as one-line substrings).
