# R75Facet60 — the Gemini CLI row's `docs`-row provenance: a `code` negative backed by a row whose scope excludes code

Seat `R75Facet60` (leaf; read-only; no delegation, no edits, no scratch, no live fetch, no install, no gate run,
no git/jj mutation). Measured revision `65a5c7a663249e0522cc49e4a148424200d9ddfe`; `git status --porcelain`
prints only `?? .ufo/waves/round-75/`, so every lane byte cited here is that commit's byte.
Axes claimed: **calibration** (what a claim's evidence class actually supports) and **operability** (a check a
later round can run that can go red). No claim about the other four axes.

**Facet object.** `SKILL.md:174`, § Description thresholds by client, **cell index 2** ("Past the threshold"),
with companion `corpus/knowledge/skill-listing-thresholds-round54.md:44` (entry row) and source
`corpus/SOURCES.md:70` (S057). Row cells, split on `|`:

| idx | cell text (verbatim) |
|---|---|
| 0 | `Gemini CLI` |
| 1 | `No threshold: ~100 words is a size estimate for metadata (name + description), which is always in context.` |
| 2 | `The loader keeps frontmatter.description as-is (skillLoader.ts:211) and the prompt template inserts it directly (snippets.ts:320) at google-gemini/gemini-cli@451a02ff; no description cut appears in these steps, so longer descriptions spend context.` |
| 3 | `Treat ~100 words as the docs' size estimate, not a limit: keep name and description short and move detail into the SKILL.md body, which loads only after activation (skills-best-practices.md:24-25)` |

## 0. Same-wave overlap, disclosed (calibration)

Facets 49, 53, 59 and 64 of this same wave already read this table. What they hold, and what this seat adds:

| sibling | already holds | this seat's delta |
|---|---|---|
| `R75Facet49` — "the Gemini CLI threshold row's code-level negative claim" | same row and same cell; O2 the pin is an 8-hex abbreviation whose full hash exists only for `docs/cli/gemini-md.md`; O3 no committed snapshot; O5 the counter does not read the code clause; a `description.slice(0, 1024)`-injected snapshot mutant | **D1**: the *source row's own declared scope* excludes the claim — S057 is kind `docs` with "not a measurement of any installed binary" — and **no `code`-kind row exists at all** for those two files (measured counts below) |
| `R75Facet53` — "`SKILL.md:166` credits the whole table to a counter that reads one column" | cell-2 unread; measured worlds; measured `7 of 7` at HEAD; a control for the `:166` sentence | none on the sentence; I use its `7 of 7` as attribution and keep my own O6 [INFERENCE] separate |
| `R75Facet59` | the past-cells' "none documents a cut"; a `1024`-row count control | none |
| `R75Facet64` | the `1024` clause and the counter docstring disclaimer | none |

**New here and in no sibling report** — verified with `grep -l 'validate_skill' ; grep -l 'addendum-2' ;
grep -l 'not a measurement of any installed binary' .ufo/waves/round-75/w1/*.md`, each returning this file alone
(62 reports present when checked; the directory is still filling): the `docs`-kind / scope-cell argument, the
absence of any `code`-kind Gemini row, the corpus's own contrary code fact (skill-creator validator 1024), the
undefined subject "these steps", and the r73 withdrawal that already forbids a re-score claim of this class.

## 1. Observations (verified from committed bytes)

**O1 — the backing row is `docs`, and its scope cell excludes code.** `corpus/SOURCES.md:70` = S057, cells:
kind `docs`; tier `A`; URL `https://geminicli.com/docs/cli/skills-best-practices.md`; scope "What Gemini CLI's
own documentation states about how much of a skill's name and description stays in the model's context …
(vendor documentation of a soft budget, **not a measurement of any installed binary**)". Its anchor pins
`451a02ff` for `docs/cli/skills-best-practices.md` only; its `teaches` cell reads "A skill's name and
description are always in context as metadata budgeted at about 100 words". Neither cell covers
`packages/core/src/skills/skillLoader.ts` or `packages/core/src/prompts/snippets.ts`.

**O2 — no `code` row exists for the cited files.** `grep -c 'skillLoader' corpus/SOURCES.md` → `0`;
`grep -c 'snippets.ts' corpus/SOURCES.md` → `0`. The only three Gemini rows on a github host are S046, S060 and
S069, and each is kind `docs` (`grep -n 'github.com/google-gemini\|raw.githubusercontent.com/google-gemini'
corpus/SOURCES.md`, kind cell read per row).

**O3 — no committed bytes.** `git ls-files | grep -cE 'skillLoader\.ts|snippets\.ts'` → `0`. The cited code lives
in the lane only as prose: `.ufo/waves/round-54/build/SrcGeminiCLI.md:87` (`skillLoader.ts:211` —
`description: frontmatter.description,`; loader's only `length` use is quote stripping at `:66`), `:88`
(`snippets.ts:314-325`, `renderAgentSkills` at `:320`), `:91` (the negative sweep
`grep -rn -E "description\.(slice|substring|substr)|\.slice\(0, *[0-9]+\)"` over four files → rc=1), `:32`
(fetched-byte sha256, 6,560 B).

**O4 — the reading was independently reproduced, so this is not a single-seat quote defect.** The wave-2
falsifier re-fetched at the pinned commit (`.ufo/waves/round-54/falsify/W2SrcGeminiCLI.md:25`: 200,
6,560 / 70,505 / 11,751 / 11,017 B with hashes) and re-located both pointers (`:37`: "`skillLoader.ts:211` …
`snippets.ts:320` … (exact line confirmed)"). The defect is **evidence custody**, not verification: two
independent readings, zero held bytes, zero registry row.

**O5 — the gate never reads cell 2.** `verifiers/check_description_thresholds.py:106`
`SKILL_HEADER = ("client", "documented threshold", "past the threshold", "action")`; `judge()` reads `sr[1]`
(`:281`, numbers), `sr[3]` (`:284`, non-empty action) and the entry cells — `sr[2]` is never read. The self-test
(`def self_test` `:334`, body to `:462`) has 26 `check(` arm calls beside its nested `def check`; a line-slice
scan for `sr[2]`/`r[2]`/`past` returns False. Sibling `R75Facet53` measured the gate at this revision reading
`description thresholds backed 7 of 7 clients`, exit 0 — so cell 2's content cannot move the verdict. (I did not
run the gate myself: editing wave in flight.)

**O6 — the number conjunct cannot separate a maximum from an absence.** `:281`
`tokens = NUM_RE.findall(sr[1])`, then `:323` `if tokens and not has_token(quote, tokens)`; `NUM_RE` (`:109`)
is `\d[\d,]*(?:\.\d+)?%?`. Gemini's cell 1 holds `100` and its quote holds `100`, so the row that says
**"No threshold"** satisfies the very conjunct the `1,024 characters` rows satisfy. [INFERENCE] the row
scores `backed` (not my measurement; sibling `R75Facet53`'s `7 of 7` is consistent with it).

**O7 — the negative's subject is undefined and the corpus holds a contrary code fact.** "no description cut
appears in **these steps**" names no file set; the underlying reading covers four files (`SrcGeminiCLI.md:87-91`).
Separately, Gemini CLI's own bundled skill-creator validator refuses `description` > 1024 —
`.ufo/waves/round-50/build/SrcGeminiCliSkills.md:35` (`validate_skill.cjs:71-72`, pinned at `09d81bf116…`).
Neither `SKILL.md:174` nor entry `:44` mentions it, so the client column reads "No threshold" with nothing
bounding what the vendor ships. [INFERENCE] whether that validator is present at `451a02ff` is unverified this
round (fetch banned); `451a02ff` is ~6 h later than the validator's pin — `09d81bf1…` main tip 2026-10-22T12:38:52Z
(`.ufo/waves/round-50/build/SrcGeminiCliSkills.md:35`), `451a02ff…` 2026-10-22T19:07:09Z
(`.ufo/waves/round-53/build/ScribeGemini.md:135`).

## 2. What is left unaddressed after the siblings' findings

- **D1 provenance class (Q12/Q23; new).** A `docs` row whose scope cell says it is not a measurement of shipped
  code is used to back a `code` claim, and the registry holds no `code` row for those files. The gate accepts
  `kind ∈ {docs, spec, code}` for the entry's `S###` (`check_description_thresholds.py`, SOURCES-row test), so
  kind is never matched to the cell's claim type. Closing D1 requires a registry row, not a sentence.
- **D2 surface claim (Q31; held by `R75Facet53`).** `SKILL.md:166` says the table is "checked by
  `verifiers/check_description_thresholds.py`" and names no cell or bound; the same file already uses the honest
  form twice — `SKILL.md:85` and `:99`, "…the other cells are reviewer readings". Recorded here as confirmation,
  not as new ground.
- **D3 number conjunct (Q26; adjacent to `R75Facet59`/`R75Facet64`).** O6's equality is the calibration defect:
  a documented absence and a documented maximum pass the same test. Siblings count `1024` rows; none treats the
  "No threshold" row as the boundary case, which is where the audit's generalisation would go wrong.
- **D4 scope/negative (Q14; new).** The row asserts a universal negative with an undefined subject, no sweep
  pointer on the SKILL.md surface, and no mention of the vendor-shipped 1024 refusal in the corpus (O7).

## 3. Concrete checks / controls (each able to fail)

**G1 — `code-cells` conjunct (closes D1).** Extend the existing gate rather than add a file (inventory stays
green under `check_gate_registry.py`). For every threshold row whose cell 2 matches
`\b[\w./-]+\.(ts|tsx|js|cjs|py|go|rs):\d+`, require and print a new count:
(h) a SOURCES row of kind `code` whose URL contains the cell's commit and whose anchor lists the same
`<path>:<line>`; (i) a committed snapshot of that path under `.ufo/waves/<round>/snapshots/`, sha256 pinned in a
committed MANIFEST, with the quoted code token present at the cited line after whitespace collapse only;
(j) printed line `code cells backed K of K`, exit 0 requiring `K == K` beside the existing `N == 7`.
Must-fail arms: `:211`→`:212` (exit 1); a snapshot with `description.slice(0, 1024)` injected at the cited line
(exit 1; `R75Facet49:95` proposes the same mutant — reference it, do not re-own); a code pointer with no `code`
row (exit 1); **the honest row plus a manufactured `code` row and snapshot (exit 0, exact printed line)** — the
exit-0 arm is what Q48 requires and what a red-only conjunct lacks. Cost: 6.5 KB + 70.5 KB snapshots
(`W2SrcGeminiCLI.md:25`), inside Q11.

**G2 — surface disclosure (closes D2).** `SKILL.md:166` takes the `:85`/`:99` form in one sentence.
Check (census, not a claim): `grep -c 'past-threshold cells are reviewer readings' SKILL.md` → `1` after, `0`
at `65a5c7a6`. Sibling `R75Facet53`'s control is the same target; land one, not two.

**G3 — bound the negative (closes D4).** Cell 2's clause names its file set
(`skillLoader.ts`/`snippets.ts`/`promptProvider.ts`), points at the sweep
(`.ufo/waves/round-54/build/SrcGeminiCLI.md:91`), and states the vendor validator's 1024
(`SrcGeminiCliSkills.md:35`, pinned at `09d81bf1`). Check: a word-bounded test that the cell contains all three
filenames and the token `1024`; `cell bounded 3 of 3` → exit 0, dropping either `promptProvider.ts` or `1024`
→ `2 of 3` → exit 1.

**G4 — make D3 measurable (calibration, not prose).** Two worlds on the current gate: a row reading
`1,024 characters` and a row reading `No threshold: ~100 words …` must **both** read `backed` today; that
equality is the finding. After G1/G2, a "No threshold" row additionally requires a `no-cap` annotation conjunct
(the absence is stated over a named file set), with an arm that drops the annotation and must read
`no-cap annotation 0 of 1`, exit 1. Distinct from `R75Facet59`'s `1024`-row count, which measures a different
quantity.

## 4. Risks for a round-75 description-audit claim

1. **Re-score risk, already routed.** `plans/round-73-addendum-2.md:15-19` withdrew an own-description claim
   because `ReviewerDescFeasibility` and `CriticSeparability` V10 (`CriticSeparability.md:314-334`) found it
   re-scores this same held rule — "quality work, never depth". A r75 claim that re-runs
   `check_description_thresholds.py` or only rewords `SKILL.md:174` repeats the withdrawn class.
2. **Where new ground is.** `code`-kind Gemini rows at `451a02ff`: `0` today (verified). Opening that row,
   committing the two snapshots and landing G1 is new ground with a counter that reads red on today's tree and
   green after, and that stays falsifiable offline.
3. **Staleness of the target.** Entry `:29-31` records the docs-host banner: Gemini CLI replaced by Antigravity
   CLI for unpaid-tier/Google One users on 2026-06-18, "short" recheck advised but no pin recorded. An audit
   treating Gemini CLI as live inherits that.
4. **Network ban.** Any r75 claim that `:211`/`:320` resolve must land its own snapshot in-round or bound itself
   to the committed prose at `SrcGeminiCLI.md:87-88` / `W2SrcGeminiCLI.md:37`; re-deriving live without a
   committed snapshot is Q51's class.

## 5. Blockers and non-findings

- **Blocker (exact):** the two cited code lines cannot be re-derived from committed bytes — the lane holds no
  snapshot and this round bans fetch; the O6 backed-row conclusion and the validator's presence at `451a02ff`
  stay [INFERENCE].
- **Non-finding:** the `~100 words` reading is faithful to S057's quote; S057 is a well-formed row (11 cells,
  tier A, `mined`, `used-by` names the entry, `90d` recheck); the falsifier did reproduce the code pointers, so
  this is not a Q42/Q53 unverified-quote defect.
- **Not run:** `check_description_thresholds.py --rev 65a5c7a6` (wave in flight; sibling `R75Facet53`'s `7 of 7`
  is cited as their measurement, not mine). No installs; no scratch directory created.
