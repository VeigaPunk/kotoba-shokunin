# Kb79A02EntrySkeleton — C2 entry skeleton (round 79, wave w1)

Seat: leaf scribe/author, item `C2 entry skeleton`. Draft only: the entry was written to
`.ufo/waves/round-79/build/Kb79A02EntrySkeleton.md` and NOT into `corpus/`. The six surface-table
rows are the `{{ROWS}}` marker for the L1 to stitch from the row seats' drafts; this seat wrote
none of them, opened no `S226`–`S231` registry row, ran no counter, and scored no claim data.

## What was produced

- `.ufo/waves/round-79/build/Kb79A02EntrySkeleton.md` — 89 lines, 20123 B. Order: six `source:`
  lines `S226`–`S231` (one per row seat; quote/snapshot left as `{{QUOTE}}`/`{{SNAP}}`), then
  `verified-at: 2026-10-27`, then a `recheck: 30d —` curl loop, then `ground:`, then the title, the
  two-paragraph documentary opening, the frozen table header `| surface | source | page tokens |
  grant | located quote |` + separator `|---|---|---|---|---|` + `{{ROWS}}`, `## Divergence matrix`
  (value form × grant semantics × where), `## What an author should do` (5 bullets), `## Limits`
  (counter-reads-cells wording, reviewer assignment, Claude `allowManagedPermissionRulesOnly` and
  workspace-trust caveats, snapshot text-view shaping, Q56 `byte-exact` reservation, pipe caveat),
  `## Not found / not checked` (the twelve census-silent pages, each `{{SWEEP}}`), `## Scope`,
  `## Related`.
- This seat report.

Shape checks, run from the build dir, all passing:

```
$ for m in '{{ROWS}}' '{{QUOTE}}' '{{SNAP}}' '{{SWEEP}}'; do printf '%s=%s ' "$m" "$(grep -o -F "$m" Kb79A02EntrySkeleton.md | wc -l)"; done
{{ROWS}}=1 {{QUOTE}}=6 {{SNAP}}=6 {{SWEEP}}=12
$ grep -c -F '| surface | source | page tokens | grant | located quote |' Kb79A02EntrySkeleton.md
1
$ grep -c -F '|---|---|---|---|---|' Kb79A02EntrySkeleton.md
1
$ grep -oE '\bS[0-9]{3}\b' Kb79A02EntrySkeleton.md | sort -u | tr '\n' ' '
S226 S227 S228 S229 S230 S231
$ awk 'NR>=25 && NR<=32 && /^\|/ {print NR": NF="NF}' FS='|' Kb79A02EntrySkeleton.md
25: NF=6 ... 32: NF=6        # 4 columns each (empty first/last field)
```

`byte-exact` occurs only in the Q56 reserved sense (`reserves byte-exact for literal byte
equality`); every quote claim is `quote-equal after documented shaping`.

After the L1's 2026-10-27 grounding-token message the draft's pipe bullet was rewritten (only pi's
quote is pipe-bearing now); after the canonical-factory freeze (`91a2fce`) the S228 source line and
the recheck loop were moved to `https://docs.factory.com/harness/skills`. Shape check re-run on the
final bytes: `89 20123`, `{{ROWS}}=1 {{QUOTE}}=6 {{SNAP}}=6 {{SWEEP}}=12`, header and separator once
each, ids `S226 S227 S228 S229 S230 S231`, all eight divergence-matrix rows 4 columns (`NF=6`).

## Stitch values for `{{QUOTE}}` / `{{SNAP}}` (one pair per source line, in order)

The entry keeps the marker form so the L1's replacement stays positional; these are the literals
measured and verified in the text view, one per `source:` line, with the snapshot the row seat owns:

| id | literal quote (text view) | words | snapshot:lines |
|---|---|---|---|
| S226 | The optional allowed-tools field: A space-separated string of tools that are pre-approved to run Experimental. | 15 | `S226-spec.md:174-177` |
| S227 | allowed-tools field grants permission for the listed tools during the turn that invokes the skill, so Claude can use them without prompting you for approval. | 25 | `S227-claude.md:617` |
| S228 | allowed-tools records the tools the skill is designed to use. Droid stores it as skill metadata and shows it in skill surfaces | 22 | `S228-factory.md:282` |
| S229 | allowed-tools No Space-delimited list of pre-approved tools the skill may use. Experimental - support may vary between agent implementations. | 19 | `S229-msaf.html:818-822` |
| S230 | the page's purpose-table row: `allowed-tools` / `Experimental pre-approved tool list` (that cell text carries 3 separators) | 8 | `S230-pi.md:78` |
| S231 | user-invocable: true allowed-tools: read grep ask_user_question | 6 | `S231-vibe.md:724-728` |

S226's literal is the L1-frozen 15-token form (the 24-word superset is not used); S227 and S228
carry the amended grounding tokens; S229 and S230 keep `Experimental`; S231's grant is `unstated`
and its grounding token is `allowed-tools:`. Each literal measured count 1 and 0 pipes in its own
shaped view, and the four I sent the L1 also measured 0 hits on the other five committed snapshots.

## Ground at base (re-run, not copied)

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
$ grep -rlE 'allowed-tools|allowed_tools' corpus/knowledge SKILL.md
corpus/knowledge/frontmatter-rule-authorities-round48.md
corpus/knowledge/chinese-vendor-skill-surfaces-round73.md      # rc=0
$ grep -c 'allowed-tools' SKILL.md
0
$ git grep -lE 'allowed-tools|allowed_tools' b10bcbc6b00f8f56b202ccbadca311007b5b463c -- corpus/knowledge SKILL.md
<same two files>                                               # rc=0
$ git grep -c 'allowed-tools' b10bcbc6b00f8f56b202ccbadca311007b5b463c -- SKILL.md
(nothing printed)                                              # rc=1 (0 hits)
$ git grep -c -iE 'allowed-tools|allowed_tools' b10bcbc6... -- corpus/knowledge
...:corpus/knowledge/chinese-vendor-skill-surfaces-round73.md:5
...:corpus/knowledge/frontmatter-rule-authorities-round48.md:2
```

Read, not inferred: `frontmatter-rule-authorities-round48.md:104` uses the key in a
specification-format sentence (`allowed-tools` as a space-separated string, spec.md:35, :176; "a
YAML list passes both"), `:160` lists it in a validator's allowed-key row;
`chinese-vendor-skill-surfaces-round73.md:25` names it among CodeBuddy's frontmatter keys and
`:46` compares spellings. Neither maps the field to a grant in any named client. Lane `HEAD` was
`daa3a09` when read; the sweep gives the same two files there.

## Own fetches (claude and factory required; all six taken for the matrix)

`curl -sSL -A 'Mozilla/5.0' --max-time 90 -o <name> -w '%{http_code}'`, 2026-10-27T21:41:29Z:

| surface | url | http | bytes | sha256 |
|---|---|---|---|---|
| spec | https://agentskills.io/specification.md | 200 | 7608 | `9a67de89132948b2300b8dc87b93817971d47f9be89b644444965881a8dfde16` |
| claude | https://code.claude.com/docs/en/skills.md | 200 | 117962 | `31623035b25ac7e6bebd8dec6234aa76e31018f0e2eb8b47da6b36cf015712f9` |
| factory | https://docs.factory.ai/cli/configuration/skills | 200 | 341235 | `81457fbf081aceaa5b90c50a8d7685450dc8801229f9a9202e40acde8fa201fa` |
| msaf | https://learn.microsoft.com/en-us/agent-framework/agents/skills | 200 | 157339 | `34016233a42a2191e319bb6ed49362956c6a6e86bbe64f2fa2e370326de548d2` |
| pi | https://raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/docs/skills.md | 200 | 4793 | `5b9805525b194474ef1fe5455a0917ef15ed7f710aa9bec2eee11879556469e5` |
| vibe | https://raw.githubusercontent.com/mistralai/mistral-vibe/main/README.md | 200 | 77634 | `fc48a5dbafe572fedd1457cffba8442aacd296dddaf50833ac3104252cb016b0` |

Four of the six are byte-identical to the committed snapshots (`S226-spec.md`, `S227-claude.md`,
`S229-msaf.html`, `S231-vibe.md`). Factory: the canonical `https://docs.factory.com/harness/skills`
returned 200 / 341235 B / sha `81457fbf…` — the same bytes as the assigned
`docs.factory.ai/cli/configuration/skills` path — and its Markdown route
`https://docs.factory.com/harness/skills.md` returned 200 / 17567 B / sha `81409d89…`,
byte-identical to `S228-factory.md`. Every factory sentence cited here was checked in both.

The recheck line in the draft was executed, not written blind:

```
$ for p in 'https://agentskills.io/specification.md|Space-separated string of pre-approved tools' \
 'https://code.claude.com/docs/en/skills.md|without asking permission during the turn' \
 'https://docs.factory.com/harness/skills|does not add tools' \
 'https://learn.microsoft.com/en-us/agent-framework/agents/skills|Space-delimited list of pre-approved tools' \
 'https://raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/docs/skills.md|Experimental pre-approved tool list' \
 'https://raw.githubusercontent.com/mistralai/mistral-vibe/main/README.md|allowed-tools:'; do \
 u=${p%%|*}; q=${p#*|}; printf '%s ' "$(curl -fsSL -A Mozilla/5.0 --max-time 60 "$u" | grep -c -F -- "$q")"; done
1 1 2 1 1 1
```

Printed at 2026-10-27T21:50:51Z with the canonical factory URL; the same loop with the assigned
`docs.factory.ai` URL printed the same six numbers at 21:42:57Z. Order spec, claude, factory, msaf,
pi, vibe; every anchor ≥1. The factory anchor occurs twice in the served HTML and once in the
Markdown route.

## Findings

**F1 — the amended text view makes the specification quote feasible, and the frozen form is 15 tokens.**
The L1's amendment (Markdown: inline-code delimiters and line-start unordered-list markers removed,
then whitespace collapsed) makes `S226-spec.md:174-177` one contiguous span. The L1 later froze the
15-token form; my independent measurement agrees and adds the location: count 1, shaped-view index
4267, 15 words, 0 pipes, both required tokens present.

> The optional allowed-tools field: A space-separated string of tools that are pre-approved to run Experimental.

My 24-word superset (through "may vary between agent implementations") also measured count 1 at the
same index and is a strict superset, but is not the frozen string; the spec row seat confirmed the
same index independently. The draft's source line carries `{{QUOTE}}`, so the frozen form drops in
without an edit from this seat.

**F2 — Vibe's natural quote is one word short of the floor; the 6-word form is verified.**
`allowed-tools: read grep ask_user_question` (after list-marker stripping) is 4 words, below (d)'s
5-word minimum. `user-invocable: true allowed-tools: read grep ask_user_question` is 6 words, 0
pipes, count 1 at shaped-view index 37473 in `S231-vibe.md` (`:724-728`). Adopted by the L1.

**F3 — Factory's blocker is dissolved by the token amendment, not by narrowing.**
The only `S228-factory.md` span holding both `allowed-tools` and the original token
`does not add tools` is the `:254` table row — 30 words, 4 pipes, i.e. over the 25-word cap and
cell-breaking. The L1 amended the factory grounding token to `metadata`, and the 22-word pipe-free
span the factory row seat had already submitted now satisfies (d) and (f): count 1 at shaped-view
index 12533 in `S228-factory.md:282`, 0 pipes, containing `allowed-tools` and `metadata`.

> allowed-tools records the tools the skill is designed to use. Droid stores it as skill metadata and shows it in skill surfaces

**F4 — after the amendment only pi's quote must carry the page's own `|` separators.**
Claude Code's 25-word pipe-free span (`:617`, count 1 at index 67523) replaces the 19-word
`:404` table-row prefix that contained 3 separators. Pi's sole occurrence of the field is its
purpose-table row — 8 words, 3 separators — so a counter that splits an entry row on `|` still
needs to treat those separators as page data (the stitched row would read as 7 fields, not 5).
The draft's Limits now states exactly this and no longer claims a factory blocker.

**F5 — row-feasibility table, measured in the text view on the committed snapshots (2026-10-27).**

| surface | span and frozen token | words | pipes | shaped index | occurrences |
|---|---|---|---|---|---|
| spec | `S226-spec.md:174-177`, `Experimental` | 15 | 0 | 4267 | 1 |
| claude | `S227-claude.md:617`, `without prompting you for approval` | 25 | 0 | 67523 | 1 |
| factory | `S228-factory.md:282`, `metadata` | 22 | 0 | 12533 | 1 |
| msaf | `S229-msaf.html:818-822`, `Experimental` | 19 | 0 | — (not indexed) | 1 |
| pi | `S230-pi.md:78` purpose-table row, `Experimental` | 8 | 3 | 3412 | 1 |
| vibe | `S231-vibe.md:724-728`, `allowed-tools:` | 6 | 0 | 37473 | 1 |

Each of the four spans I sent the L1 (spec, claude, factory, vibe) also returns zero hits in the
other five committed snapshots, so none is another page's text.

**F6 — the pi snapshot landed while this seat worked, and it is my fetch's bytes.** `S230-pi.md` is
4793 B, sha `5b980552…`, byte-identical to my own fetch (93 lines; `S230.manifest` and
`S230.fetch.json` present). Its `allowed-tools` row is `:78` and measures 8 words / 3 separators /
shaped-view index 3412 / count 1. The draft keeps the `{{SNAP}}` marker — replacement is positional
across all six source lines — and the stitch table now pins the pi literal and its line, so the
matrix cites `S230-pi.md:78` directly instead of a section.

**F7 — the matrix's factual base.** Every matrix cell rests on a line I re-grepped on the committed
snapshot: spec `:35`, `:172-177`, `:182`; claude `:404`, `:405`, `:617`, `:619`, `:632`, `:641-643`,
`:420-425`, `:432`, `:789`; factory `:235-238`, `:254`, `:282`, `:285-288`, `:298`, `:264` (legacy
`tools` key); msaf `:818`, `:825` (collection-where-scalar-expected blocks loading); vibe `:712`,
`:725-728`, `:969`, `:972-976`, `:1045-1048`, `:1039-1040`. The divergence that carries the entry:
Claude Code says the field does not restrict and clears on the next message; Factory says
metadata-only, no tools added, not a security boundary; the spec/MSAF/pi say pre-approved +
experimental; Vibe states nothing, and both pages that document a real restriction put it in a
different field or file (`disallowed-tools`; Vibe's `[tools.*]` config).

**F8 — Factory's source identity is the canonical host/path.** The L1's freeze commit `91a2fce`
pins the factory surface to `docs.factory.com/harness/skills` (the assigned
`docs.factory.ai/cli/configuration/skills` 308s through `docs.factory.com/cli/configuration/skills`),
with the snapshot as the same page's Markdown route `docs.factory.com/harness/skills.md`. Both
routes verified 2026-10-27: HTML 200 / 341235 B / sha `81457fbf…` — byte-identical to my fetch of
the assigned path — and Markdown 200 / 17567 B / sha `81409d89…` — byte-identical to the committed
`S228-factory.md`. The draft's S228 source line, its recheck entry and its Limits route note all
carry the canonical URL, and the redirect chain is named in the source line's parenthetical.

## Gates

None run and none claimed. My item names no gate, and the C2 counter
(`verifiers/check_allowed_tools.py`) is built and frozen by the L1 after this wave: no claim data
may be scored on it before the freeze. This seat ran no counter, produced no `N of 6`, and asserts
no gate result — the draft is a set of cells and quotes for the L1 to test.

## Touched surfaces

- New: `.ufo/waves/round-79/build/Kb79A02EntrySkeleton.md`, `.ufo/waves/round-79/w1/Kb79A02EntrySkeleton.md`.
- Read-only: `plans/round-79.md` (including the amended C2 predicate at `:37-42`), the six committed
  snapshots and manifests under `.ufo/waves/round-79/snapshots/`, `receipts/c2-census-l1.txt`,
  `receipts/freeze-shas.txt`, `corpus/SOURCES.md` header and rows `S216`–`S225`,
  `corpus/knowledge/frontmatter-rule-authorities-round48.md`,
  `corpus/knowledge/chinese-vendor-skill-surfaces-round73.md`,
  `corpus/knowledge/sibling-overlap-census-round74.md`, `corpus/knowledge/spec-skill-creation-craft-round74.md`,
  `corpus/QUALITY.md` (Q30/Q31/Q45/Q50/Q56/Q65/Q70/Q71), the row drafts `Kb79R02ClaudeRow.rows.md`
  and `Kb79R03FactoryRow.rows.md`.
- Lane git: read-only (`git rev-parse`, `git grep <rev>`, `git status`). No commit, add, checkout,
  stash; no `MANIFEST.json`, `scripts/`, `templates/`, `.ufo/state/` write; nothing at the fleet root.
- Scratch `/fast/scratch/hyaku/kotoba-r79/Kb79A02EntrySkeleton` (clones/fetches/shaping scripts)
  removed: `rm -rf` rc=0, `test -e` → removed.

## Out of scope (not done, by design)

The six `S226`–`S231` registry rows; the six surface-table rows (`{{ROWS}}`); the counter build and
its controls; the `SKILL.md` rule line and its gate-registry row; the `PROVINCE.md` Core bullet;
`LOG.md`/`SCORECARD.md`/lesson; the commit into `corpus/knowledge/`. Tooling: nothing installed,
nothing upgraded (no pacman, no network package install).

## Open items for the L1 before the C2 freeze

1. F4: decide how the counter treats pi's located quote, which must carry that page's `|` separators
   (8 words, 3 separators) because it is the page's only occurrence — a naive `split('|')` reads the
   stitched row as 7 fields. The other five rows are pipe-free after the token amendment.
2. Fill the six `{{QUOTE}}`/`{{SNAP}}` pairs from the "Stitch values" table above; S230's is now
   pinned to `S230-pi.md:78`, and S231's to `S231-vibe.md:724-728`.
3. Keep the S226 row on the frozen 15-token string (index 4267) rather than my 24-word superset, so
   a literal-match gate and the row agree.
4. The four amended quote strings sent to the L1 are verified at count 1 with 0 pipes and no
   cross-page hit; the entry needs no edit for them — its rows are `{{ROWS}}`.
5. Conjunct (c) needs a shared `MANIFEST.sha256` under `.ufo/waves/round-79/snapshots/`; none exists
   there at this read (`ls -1 MANIFEST*` → rc=2), only the six per-id `.manifest` files
   (`S226`–`S231`). The Vibe row seat reports the same gap for its `fc48a5db…` pin, so all six pins
   must be written before the freeze.

VERDICT: C2 entry skeleton delivered as a draft with all six required structural blocks and the amended text view named verbatim; every matrix fact re-grepped on the committed snapshots, no counter run and no claim data scored; the L1's amended grounding quotes are verified in the shaped view (spec 15 words/index 4267, claude 25/67523, factory 22/12533, pi 8/3412, vibe 6/37473 — each count 1, and only pi carries page separators), and the remaining open items are pi's pipe-bearing quote and the absent shared MANIFEST.sha256 pin file.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79A02EntrySkeleton.md; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/w1/Kb79A02EntrySkeleton.md
