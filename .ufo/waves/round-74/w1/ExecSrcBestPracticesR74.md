# ExecSrcBestPracticesR74 — source opening: `skill-creation/best-practices.md` (C1 depth)

Seat: `ExecSrcBestPracticesR74`, leaf executor, round 74 wave 1, lane kotoba
(`/home/vgpnk/Projects/shokunin/kotoba-shokunin`, base `1e03d1991bc02281b00a5b7a5e00c9d5d5d72908`,
plan `329e7d91d7d750031c35d264f0e34af1d0ce8385`). Wrote only under
`.ufo/waves/round-74/w1/build/ExecSrcBestPracticesR74/` and this report; no committed lane file was touched.

## Verdict

The page opens and is the format maintainers' own body-craft guide, and it is worth a tier-A
registry row: **13 rules, each with a literal-verified quote and ≥2 rule tokens**, and the page is
**byte-equal to `docs/skill-creation/best-practices.mdx` at `agentskills/agentskills@69ef37e`
modulo site markup** (canonicalized diff, 174/174 body lines equal). Three defects in the staged
material are real and are refused below: the staged anchor records every section as `#` where the
page has `##` and `###`; the staged paraphrase "be prescriptive **only** where the task is fragile"
adds a restriction the page contradicts at L125; and the staged fetch date's byte-identity is not
re-provable (size equality only). One predicate hazard: the row must be **promoted from `queued` to
`mined` and the snapshot copied into `.ufo/waves/round-74/snapshots/` with a `snapshots/MANIFEST.sha256`
pin**, or C1 scores 0 at landing even with correct content. One depth gap in the lane surfaced as a
by-product: `S018` records the spec's 500-line rule but not the spec's 5,000-token recommendation
that this page attributes to it.

## 1. Fetch record (opened today, 2026-10-25)

```
$ curl -sL --max-time 60 -A 'Mozilla/5.0' -w 'HTTP:%{http_code} URL:%{url_effective} SIZE:%{size_download}\n' \
    'https://agentskills.io/skill-creation/best-practices.md'
HTTP:200 URL:https://agentskills.io/skill-creation/best-practices.md SIZE:15060
$ curl -sL --max-time 60 -A 'Mozilla/5.0' -w 'HTTP:%{http_code} URL:%{url_effective} SIZE:%{size_download}\n' \
    'https://agentskills.io/skill-creation/best-practices'
HTTP:200 URL:https://agentskills.io/skill-creation/best-practices SIZE:389017
$ wc -c bp-md.raw ; sha256sum bp-md.raw snapshot.md
15060 bp-md.raw
ab9f3b6091a0f24816b52cd7b90a3fdf53e621f47dba13b36694be272b87fb41  bp-md.raw
ab9f3b6091a0f24816b52cd7b90a3fdf53e621f47dba13b36694be272b87fb41  snapshot.md
$ date -I
2026-10-25
```

- `.md` form: HTTP 200, no redirect added (final URL identical), **15 060 B**, sha256 `ab9f3b60…`.
- No-`.md` form: HTTP 200, `text/html`, **389 017 B**; the prose is present (the fragility sentence
  occurs there — `grep -c` → 2, rendered copy plus hydration payload). The `.md` form is the text
  form; that is what I pinned. The raw HTML was text-extracted to 15 348 B (`bp-plain.text.txt`) and
  the 379 KB raw was deleted to stay inside the 300 KB snapshot bound.
- Snapshot saved at `…/build/ExecSrcBestPracticesR74/snapshot.md` (15 060 B, verbatim `.md` bytes,
  whitespace preserved) with `snapshot.sha256` holding
  `ab9f3b6091a0f24816b52cd7b90a3fdf53e621f47dba13b36694be272b87fb41`.

**F1 — the staged size reproduces, the staged date's byte-identity does not.** Staged S232 says
"fetched as `.md` 15 060 B on 2026-10-23". Today's fetch is 15 060 B, so the size is unchanged, but
byte-identity across two days is not observable from this session; the row records today's sha256 and
says nothing about 2026-10-23 beyond size equality.

## 2. Upstream: is `69ef37e` still the head of the docs path, and is the page the mdx?

```
$ curl -sL 'https://api.github.com/repos/agentskills/agentskills/commits?path=docs/skill-creation/best-practices.mdx&per_page=5'
3 commits returned:
b8d2613ac 2026-04-19T20:09:27Z  Point "progressive disclosure" links at `specification.mdx`
4be62ebad 2026-03-15T22:32:38Z  Add gotchas section to best practices guide
db92534bf 2026-03-10T19:19:12Z  Add best practices guide for skill creators
$ curl -sL 'https://api.github.com/repos/agentskills/agentskills/commits/main'
main head 69ef37e9424c0a7ea9dd2293b559e43ec8176379 2026-08-09T20:36:04Z
$ curl -sL 'https://api.github.com/repos/agentskills/agentskills/compare/69ef37e...b8d2613'
status behind ahead_by 0 behind_by 35
merge_base b8d2613ac050aa4aa8bfb2cf28380d81cdfcd1ca
$ sha256sum gh-692.mdx gh-head.mdx
a729bc1d746366ecb8c5056b100439fbf760007a0f836e089c0f3aff9ce5c2f8  gh-692.mdx
a729bc1d746366ecb8c5056b100439fbf760007a0f836e089c0f3aff9ce5c2f8  gh-head.mdx
```

**F2 — `69ef37e` is still `main`'s head, but it is not the head of the docs path; the path's last
commit is `b8d2613` (2026-04-19), which is an ancestor of `69ef37e` (`merge_base` equals `b8d2613`
itself).** The file bytes are the same at both because no commit after `b8d2613` touched the path:
`gh-692.mdx` and `gh-head.mdx` are byte-identical (sha256 `a729bc1d…`). So the lane's existing
anchor convention (`agentskills/agentskills@69ef37e`) stays valid for this page, and the honest anchor
is "mdx equal at `b8d2613` and at `69ef37e` (main head, 2026-08-09)".

**F3 — the served page equals the upstream mdx modulo markup, verified by canonicalized diff, not asserted.**

```
$ python3 … canonicalize(bp-md.raw) vs canonicalize(gh-head.mdx)
page lines 179 after header strip 176 mdx lines 174 ratio 0.9943
delete page ['# Best practices for skill creators',
             'How to write skills that are well-scoped and calibrated to the task.'] | mdx []
```

Canonicalization removed only: the 3-line site "Documentation Index" blockquote; the mdx frontmatter
and the title/description the site renders from it (the 2 deleted lines above); `<Tip>`/`</Tip>` →
`> [!TIP]`; relative link targets → absolute `…​.md` URLs with link text kept; fence info strings
(`theme={null}`); `-` → `*` bullet markers; `\<`/`\_`/`\*` escapes. After that, **all 174 body lines
are equal** — the single opcode is that frontmatter-derived delete. The word `byte-exact` is not used
for the page/mdx relation (it holds only for `gh-692.mdx` vs `gh-head.mdx`).

## 3. The rules an author acts on (13, every quote literal-verified)

Full table with dropped-bytes notes: `…/build/ExecSrcBestPracticesR74/rules-table.md`. Verification run
against the snapshot, whitespace collapse only:

```
PASS  1 words=12 tok=2/2 § Calibrating control, intro (L96)
PASS  2 words= 9 tok=2/2 § Structure large skills with progressive disclosure (L90)
PASS  3 words=10 tok=2/2 § Structure large skills with progressive disclosure (L92)
PASS  4 words=13 tok=2/2 § Match specificity to fragility (L111)
PASS  5 words= 9 tok=2/2 § Match specificity to fragility (L122)
PASS  6 words=14 tok=2/2 § Provide defaults, not menus (L129)
PASS  7 words=13 tok=2/2 § Favor procedures over declarations (L147)
PASS  8 words=10 tok=2/2 § Add what the agent lacks (L54)
PASS  9 words=12 tok=2/2 § Aim for moderate detail (L86)
PASS 10 words=11 tok=2/2 § Gotchas sections (L169)
PASS 11 words=13 tok=2/2 § Gotchas sections (L183)
PASS 12 words=11 tok=2/2 § Validation loops (L231)
PASS 13 words=16 tok=2/2 § Plan-validate-execute (L249)
rows 13 failures 0
```

The strongest twelve, with the page line each quote was cut from:

| # | line | quote (≤25 words, literal) | tokens | action |
|---|---|---|---|---|
| 1 | L96 | "Match the specificity of your instructions to the fragility of the task." | `fragility`, `prescriptiveness` | grade each part's prescriptiveness by how fragile its step is |
| 2 | L90 | "recommends keeping `SKILL.md` under 500 lines and 5,000 tokens" | `SKILL.md`, `references/` | cap the body; move detail into `references/` |
| 3 | L92 | "Read `references/api-errors.md` if the API returns a non-200 status code" | `references/api-errors.md`, `non-200` | attach each side file to its load condition |
| 4 | L111 | "when operations are fragile, consistency matters, or a specific sequence must be followed" | `migrate.py`, `--verify` | pin the exact command where the sequence is fragile |
| 5 | L122 | "Do not modify the command or add additional flags." | `migrate.py`, `--backup` | state the prohibition beside the pinned command |
| 6 | L129 | "When multiple tools or approaches could work, pick a default and mention alternatives briefly" | `pdfplumber`, `pdf2image` | one default, alternative only as an escape hatch |
| 7 | L147 | "A skill should teach the agent *how to approach* a class of problems" | `references/schema.yaml`, `_id` | teach the generalizing method, not one answer |
| 8 | L54 | "Focus on what the agent *wouldn't* know without your skill" | `pdfplumber`, `project-specific` | cut what the agent already knows |
| 9 | L86 | "Concise, stepwise guidance with a working example tends to outperform exhaustive documentation." | `stepwise`, `exhaustive` | steps plus one example over edge-case coverage |
| 10 | L169 | "The highest-value content in many skills is a list of gotchas" | `WHERE deleted_at IS NULL`, `soft deletes` | collect assumption-defying environment facts |
| 11 | L183 | "Keep gotchas in `SKILL.md` where the agent reads them before encountering the situation." | `SKILL.md`, `gotchas` | gotchas stay in the body |
| 12 | L231 | "Instruct the agent to validate its own work before moving on." | `validate.py`, `output/` | end workflows with validate-fix-repeat |
| 13 | L249 | "For batch or destructive operations, have the agent create an intermediate plan in a structured format" | `field_values.json`, `validate_fields.py` | plan file validated against a source of truth first |

Rows 4+5 are one rule in two halves; merge them for a 12-row entry. Token occurrence was checked
word-bounded against the snapshot, so a token like `migrate.py` (which the page writes inside a
plain code fence, not in backticks) still locates.

**F4 — the page does state the 500-line recommendation, and it attributes a second cap the lane does not hold.**
`sed -n '90p' snapshot.md`:
"The [specification](…) recommends keeping `SKILL.md` under 500 lines and 5,000 tokens — just the core instructions the agent needs on every run."
Cross-check at the pinned upstream file (`docs/specification.mdx` @ `69ef37e`, 7166 B, sha256 `b9079c0c…`):
L221 "2. **Instructions** (< 5000 tokens recommended): The full `SKILL.md` body is loaded when the skill is activated"
L224 "Keep your main `SKILL.md` under 500 lines. Move detailed reference material to separate files."
And on the served page (`https://agentskills.io/specification.md`, 200, 7608 B, sha256 `9a67de89…` — equal to
the `9a67de89…` prefix `S018` records, so the spec page is unchanged since 2026-10-22) the same two lines sit
at L234 and L237. `S018`'s anchor names mdx lines "27, 61-65, 94, 224" — it cites the 500-line line and not
the 5,000-token line. This page therefore supplies a rule the registry cannot currently cite:
an entry that states the token cap must cite L90 of this page (or `S018` must gain L221 in an appended note,
never a rewrite).

## 4. Staged claims, grounded or refused (step 4)

`spec-description-trigger-discipline.md` is the only staged entry citing this page (`grep -n 'best-practices\|S232\|S231' spec-script-craft-rules.md` → exit 1, no hits, so **no staged claim of
`spec-script-craft-rules.md` rests on this page**).

| staged claim | status | observed |
|---|---|---|
| source heading `# Calibrating control`, `# Provide defaults, not menus`, `# Favor procedures over declarations` | **refused as written** | levels are wrong: `## Calibrating control` L94, `### Provide defaults, not menus` L127, `### Favor procedures over declarations` L145 (and `### Match specificity to fragility` L98). The names exist; the recorded level does not |
| quote "Match the specificity of your instructions to the fragility of the task." | **located** | L96, literal, whole sentence. Preceding sentence "Not every part of a skill needs the same level of prescriptiveness." dropped |
| quote "A skill should teach the agent how to approach a class of problems, not what to produce for a specific instance." | **located after documented shaping** | L147 writes `*how to approach*` and `*what to produce*`; the staged copy drops four emphasis asterisks. Literal form in the page: "A skill should teach the agent \*how to approach\* a class of problems, not \*what to produce\* for a specific instance." |
| "give the agent freedom where several approaches work and explain *why*" | **located** | L100 "**Give the agent freedom** when multiple approaches are valid and the task tolerates variation. For flexible instructions, explaining *why* can be more effective…" |
| "be prescriptive only where the task is fragile" | **partly refused** | L111 says "**Be prescriptive** when operations are fragile…" — "when", not "only when". The page adds at L125 "Most skills have a mix. Calibrate each part independently.", which the staged "only" reads against. The staged sentence strengthens the source |
| "give a default rather than a menu of equal options" | **located** | L129 "When multiple tools or approaches could work, pick a default and mention alternatives briefly rather than presenting them as equal options." |
| "fetched as `.md` 15 060 B on 2026-10-23" | **size reproduces, date's byte-identity unobservable** | today 15 060 B, sha256 `ab9f3b60…`; nothing in this session can confirm the 2026-10-23 bytes (F1) |
| "Independently converges with ByteDance's freedom-grading ladder (S131)" | **not checkable from this page** | a two-source convergence claim; the page half is the L96/L100/L111 text above, the S131 half is not this seat's source |
| staged row S232 anchor listing only `Calibrating control` → `Match specificity…` | **incomplete, not wrong** | the page's other actionable sections are `## Spending context wisely` → `### … progressive disclosure` (L88-L92) and `## Patterns for effective instructions` (L163-L270), which carry rules 2, 3, 8-13 of the table above; a row scoped to three sections would lose nine of the thirteen rules |

**F5 — the staged entry's caveat sentence is missing a located qualifier.** L161: "This doesn't mean
skills can't include specific details — output format templates …, constraints like "never output PII," and
tool-specific instructions are all valuable." The staged text says the page wants "an approach … rather
than one specific output" and then moves on; the page's own limit on that rule is L161. An entry that
quotes L147 without L161 states a stricter rule than the source.

## 5. Absences on this page (Q62: refusals rest on observed absence)

```
$ grep -cE 'uvx|pipx|npx|bunx' snapshot.md
0
$ grep -c 'description' snapshot.md
1        # L277 only: a link to the Optimizing skill descriptions guide
```

**F6 — this page cannot ground the script-runner rules or any description rule.** `uvx`, `pipx`, `npx`,
`bunx` occur zero times (they belong to `using-scripts`, S236); `description` occurs once, as a link.
The entry must keep the one-off-command and trigger rules on S236/S213 and use this page only for body
craft — a row that cites this page for runners would be a false attribution.

## 6. Deliverables

All under `.ufo/waves/round-74/w1/build/ExecSrcBestPracticesR74/`:

- `snapshot.md` (15 060 B, byte copy of the fetched `.md`) and `snapshot.sha256`
  (`ab9f3b6091a0f24816b52cd7b90a3fdf53e621f47dba13b36694be272b87fb41`).
- `row.md` — the registry row, 11 cells, `id` placeholder `S223` (`S222` is the base maximum,
  `grep -c 'S223' corpus/SOURCES.md` → 0), kind `docs`, tier `A`, `status queued`, `opened 2026-10-25`,
  `recheck 90d`, `used-by corpus/knowledge/spec-skill-creation-craft-round74.md`, no `|` inside any cell.
  Cell check: `cells 11`.
- `rules-table.md` — the 13-row rule table with quotes, tokens, actions, dropped-bytes notes and the
  observed absences.
- `skill-md-rows.md` — draft of the `### Body craft — the specification's skill-creation guides`
  subsection for C1 condition (e): 3 rows citing S223, each action cell ≥5 words carrying a token
  (`SKILL.md` ×5, `references/` ×4 in the snapshot), quotes literal, placement proposed under
  `## Compression rules` (SKILL.md:190), cost 6 lines against the 570 → 600 budget.

## 7. Predicate and landing hazards (must be fixed before C1 is scored)

**F7 — `queued` cannot score.** `row.md` carries `status queued` as the assignment directs, but C1
predicate (b) requires the cited row to be an 11-cell row with status `mined`. Landing the row as
`queued` is one of the plan's own shortcut worlds ("rows appended with status `queued`"), which must score
below 3. The L1 must promote the cell to `mined` at landing; the draft is queued, not shippable as-is.

**F8 — the snapshot is not where predicate (c) looks.** C1 (c) pins
`.ufo/waves/round-74/snapshots/` against `snapshots/MANIFEST.sha256`. At base neither exists
(`ls .ufo/waves/round-74/` → `assimilation gen-w1.py receipts w1 w1-dispatch.err w1-dispatch.json
w1-spec.json w1.ready`). My snapshot lives in the build directory per the seat contract; the L1 must
copy it to `.ufo/waves/round-74/snapshots/best-practices.md` and write the manifest pin
`ab9f3b60…`, or the counter returns exit 2 for a missing snapshot regardless of content.

**F9 — the entry's `source:` line must carry today's record, not the staged one.** Predicate (a) requires
`source:` per cited id, then `verified-at:` and `recheck:`. The staged entries carry
`verified-at: 2026-10-23`; the entry landed this round must carry a round-74 date and the 15 060 B /
`ab9f3b60…` fetch record, or the "assimilation opens nothing" failure recurs (addendum §10).

## 8. Base absence this subsection closes (before-value, re-measured)

```
$ for p in 'fragility' 'defaults, not menus' 'procedures over declarations' 'progressive disclosure' \
           'gotchas' 'plan-validate-execute' 'validation loop' 'references/' '500 lines'; do
    printf '%-30s SKILL.md=%s PROVINCE=%s SOURCES=%s\n' "$p" \
      "$(grep -ciF "$p" SKILL.md)" "$(grep -ciF "$p" PROVINCE.md)" "$(grep -ciF "$p" corpus/SOURCES.md)"; done
fragility                      SKILL.md=0 PROVINCE=0 SOURCES=0
defaults, not menus            SKILL.md=0 PROVINCE=0 SOURCES=0
procedures over declarations   SKILL.md=0 PROVINCE=0 SOURCES=0
progressive disclosure         SKILL.md=0 PROVINCE=0 SOURCES=5
gotchas                        SKILL.md=0 PROVINCE=0 SOURCES=0
plan-validate-execute          SKILL.md=0 PROVINCE=0 SOURCES=0
validation loop                SKILL.md=0 PROVINCE=0 SOURCES=0
references/                    SKILL.md=0 PROVINCE=0 SOURCES=0
500 lines                      SKILL.md=0 PROVINCE=0 SOURCES=2
$ grep -c 'best-practices' SKILL.md
1        # the single hit is a URL: geminicli.com/docs/cli/skills-best-practices.md at SKILL.md:169
```

**F10 — the page is unreferenced in `SKILL.md` and its vocabulary is absent from the file.** Every
phrase above is 0 in SKILL.md and PROVINCE.md; the one `5000 tokens` mention in SKILL.md (L170) is
Cursor's client warning about an over-large body, not the spec's recommendation — so the subsection
adds a rule the file does not have rather than restating one it does. `SKILL.md` is 570 lines / 74 174 B
at base (`wc -lc`), leaving 30 lines of headroom for the 6-line subsection plus the 2 registry rows and
the routed item.

## 9. What was not done (unobserved, stated)

- No lane gate was run and no fleet-shaped sandbox built: this seat measures no lane counter, and the
  contract forbids verifying in-wave. `check_spec_craft.py` does not exist at base
  (`ls verifiers/check_spec_craft.py` — not present), so the counter is another seat's build.
- `using-scripts` and `quickstart` were not opened by this seat; the Q45 census and their rows belong to
  the seats assigned them. Nothing here asserts what those pages say.
- No tool was installed or upgraded (no `uv`, `npx` or binary needed).
- Scratch: none outside the build directory; nothing to delete.

## 10. Risks

- The staged "be prescriptive **only**" reading (F5/L125) is the kind of strengthening a reviewer will
  find in the entry if the L1 copies the staged prose; the landed text should carry L125's
  "calibrate each part independently".
- Two rows of `skill-md-rows.md` cite S223 with the same tokens (`SKILL.md`, `references/`); if a wave-2
  mutation-tester stuffs a row with tokens to test the counter, the counter must distinguish a token that
  occurs from a token that supports the action cell — the plan's bound (Q26/Q51) already assigns that
  judgement to a reviewer, and it should be assigned explicitly.
- The page is stable (last content change 2026-04-19, main head 2026-08-09), so the 90-day recheck will
  most likely be a no-op; the cost is one fetch and one sha256 compare, and `recheck 90d` is right.
