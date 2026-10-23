# Round 60 — plan (kotoba, hyaku phase 4, attempt 1)

Base `31092dc6f875370bddd6eb1e4da4ca0d210c56af` (round-59 spot-check tip). L1 `KotobaR60`, dispatched 10:24Z
2026-10-23; freeze 12:24Z, hard stop 13:24Z. Round 59 was admitted (C1 depth verified; the closure's depth ruling
rests on the row count plus semantic re-reads, not on new ground). This plan is committed in two steps: **draft**
(this text: row rule, semantic conjuncts and target formula fixed, C1 target `TBD`) before any census seat returns,
then **freeze** (census record + target + counter + its sha) before the control wave scores it and before any C1 data.
A rule changed after the freeze is a second measurement, never the declared one (Q28).

## Routed defects from `corpus/lessons/round-59-verifier-spotcheck.md` § 7

| R | defect | route this round |
|---|---|---|
| R1 | Gemini reject reason says the hooks-overview span is "29 words"; by `wc -w` it is 25 | a seat re-fetches `https://geminicli.com/docs/hooks.md`, cuts lines 94-97 at the token and pastes the exact command and count; the lesson `round-60.md` carries an append-only correction of `round-59.md` § Gate with that command (the round-59 lesson and `w0/CensusGeminiCLI.md` are not edited) |
| R2 | M84 and M85 end in a "rule for next rounds" with no `QUALITY.md` row | new QUALITY rows citing M84 (re-score a census token before the freeze after any swap) and M85 (a quote-shaping note is written from the fetched bytes, not from a description), or a stated reason an existing row covers each |
| R3 | report said "Closed 10:12Z" after the report commit (10:10:35Z) | the round-60 report states no clock time later than a `date -u` line taken before the fleet commit; lesson mistake M86 |
| R4 | carried: `SHONEN.md:6` pointer drift; C2 redesign; 13 counter survivors; S096 anchor label; S097 `teaches` wording; L0 `kotoba \| round-55 \|` | `SHONEN.md:6` pointer repointed to the line that holds the decision-table pointer now (`SKILL.md:227` at the base); S096 anchor label and S097 wording get one append-only correction row each (SOURCES rule: no in-place anchor edit); the 13 survivors of the round-59 counter and the C2 redesign stay carried (no claim rests on them); the L0 question stays open |

## Claims (1 declared)

### C1 — depth (lowest owned axis, 9): scoped rule files by client (sourced; the learning claim)

Surface: `SKILL.md` gains `### Scoped rule files by client` beside § Hook files by client — per client, the file or
folder its own docs name for a rule (instruction) file that applies only when the agent works on matching files, the
frontmatter key that names the matching paths, and what a rule author does with it (scope a rule to the files it is
about instead of loading it every turn). Grounded in `corpus/knowledge/scoped-rules-round60.md` and new
`corpus/SOURCES.md` rows opened 2026-10-23. Base state: `SKILL.md` at the base has 0 lines holding `applyTo`, `globs`,
`.claude/rules`, `.cursor/rules` or `.github/instructions` (`git show 31092dc6:SKILL.md | grep -cF <t>` → 0 each); the
corpus mentions `.cursor/rules` and `.github/instructions` only as omp loader classes (round-13 census), never a
client's scope key.

**Semantic conjuncts (the point of this round).** Round 59's Events conjunct proved a name was printed on the page, not
that it was an event (`round-59-verifier-spotcheck.md` § Counter limits). This counter reads the semantic cells:

- **Scope key cell** — the first backticked span K (`^[A-Za-z][A-Za-z0-9_-]*$`) must be cited as `S### :L` (the
  row's own source id; `S###:L` also accepted) and, on line L of the committed snapshot, K must stand **as a key that
  takes a path pattern**: K at an identifier boundary, followed (after an optional closing `"`, `'` or backtick and
  optional spaces) by `:` or `=`, or K as a backticked table cell (`` | `K` | ``); AND a path pattern on that line —
  a run of `[A-Za-z0-9_./*{},!-]` containing `*` — or, when nothing but spaces, `[` or `|` follows the `:` on line
  L, on one of the next 3 lines; OR the word `glob`, `globs` or `pattern`/`patterns` on line L outside K's own span.
  A printed name that is not the scoping key (`description`, `name`, `alwaysApply`, a product name) fails.
- **Action cell** — at least 3 words and a citation `S### :L` to the row's own source; line L of the snapshot shares
  at least 2 distinct content words with the cell (lowercase `[a-z]{4,}` words outside backticks and citations,
  minus a pinned stopword list in the counter). An action invented apart from the cited line fails.


**Draft amendment A1 (committed `bfe8cc2b`; before the freeze, before any control or C1 data; the rule is tightened, never loosened).**
Census seat `CensusCursor` (`.ufo/waves/round-60/w0/CensusCursor.md:94-108`) showed the drafted Scope-key rule passes a
wrong key: `cursor.com/docs/rules` line 65 (`` | `alwaysApply` | `description` | `globs` | ``) passes for `description`
through the table-cell form plus the word `globs` elsewhere on the line, and line 99 (`description: RPC service
conventions and patterns …`) passes through the word `patterns`. A printed-but-wrong name passing is the failure this
round exists to stop, so the two conjuncts read, from A1 on:

- **Scope key cell (A1)** — K must stand in **key form** on line L: K at an identifier boundary, followed (after an
  optional closing `"`, `'` or backtick and optional spaces) by `:` or `=`. Its **value** V is the rest of line L after
  that `:`/`=`; when V is empty or only `[`, `|` or `>`, V is the first nonblank line among the next 3 lines, which must
  begin (after spaces) with `-` or a quote. After stripping leading `-`, `[`, quotes and spaces, the **first token** of V
  (up to whitespace, a comma or a closing quote/bracket) must contain `*` and consist only of `[A-Za-z0-9_./*{},!-]`.
  The table-cell form and the glob/pattern-word alternative are removed. `description: "Applies to **/*.ts"` fails
  (first token `Applies`).
- **Action cell (A1)** — W = the distinct content words of the cell (lowercase `[a-z]{4,}` outside backticks and
  citations, minus the pinned stopwords); |W| ≥ 3 and at least max(2, ⌈|W|/2⌉) of W occur on the cited line. Limit
  stated before any control: a cell built from the line's own words passes even if it inverts the line's meaning
  (negation); that reading stays with the falsify-wave `Cells<Client>` seats.
- The live conjunct uses the same key-form test at any line of the live page.

Counter: `python3 -B verifiers/check_scoped_rules.py --rev <rev> --fetch` (built pre-freeze from
`verifiers/check_hook_files.py`, sha256 `f695d59e…`; everything not named here is that counter's behaviour). Row rule
(fixed in this draft):

- Section heading line exactly `### Scoped rule files by client`; first table header `| Client | Rule files | Scope
  key | Action |`; clients Claude Code, Codex, VS Code, Copilot CLI, Gemini CLI, Cursor, opencode; HOSTS = the
  pinned map of `check_hook_files.py`; token = first backticked span of the Rule files cell.
- Token well-formed iff: the path regex of `check_hook_files.py`; after stripping one leading `~/` or `./` it has
  ≥ 2 path segments and its first segment starts with `.`; no segment split on `-`, `.`, `_` holds `skill`, `skills`,
  `agent`, `agents`, `command`, `commands`, `prompt`, `prompts`, `plugin`, `plugins`, `extension`, `extensions`,
  `hook`, `hooks` (`rule`, `rules`, `instructions` are allowed: this is the rule-file table); E7; the foreign-name
  guard. **E5 is dropped:** two rows may share a token when each row is backed on its own client's pinned host
  (VS Code and Copilot CLI may both document `.github/instructions/`); a token copied into a row whose own host does
  not back it still fails the host pin and the quote.
- Backed iff: the entry table `| Client | Rule files | Source | Quote |` has the client's row with the same token; the
  quote is 6–25 words, contains the token (or its normalised form) case-sensitively at segment boundaries and matches
  `(?i)\b(rules?|instructions?)\b` outside the token span; the source is a new tier-A row opened 2026-10-23 on the
  client's pinned host (not changelog/release/news/blog/tracker); the quote is in the lesson `## Gate`; the committed
  snapshot `.ufo/waves/round-60/snapshots/<S###>.page` exists at the revision, its sha256 equals the sha256 printed in
  that SOURCES row, the quote is found on it, and both semantic conjuncts hold on it.
- With `--fetch`: the row is **found** iff it is backed and the quote and a key site for K (the Scope key rule above,
  at any line) are also found on the live page, fetched with `curl -sSL` and a browser User-Agent, up to 3 attempts,
  final URL on the pinned host.
- Prints `scoped rule files backed on committed snapshots S of K; found on the live page F of K` (without `--fetch`
  the live part reads `live not run` and F = 0), then `counter sha256 <hex>; rev <rev>` and one `reject <client>:
  <reasons>` line per non-found row.
- **Census (Q45), recorded before the target:** W0 census seats (one per client, scouts, no lane content) score each
  client's candidate against this rule, including both semantic conjuncts on the fetched bytes.
- **Target formula (fixed now, applied to the census at freeze):** T_F = F_max − 1, where F_max is the census count of
  eligible clients. If F_max < 3 the claim is redesigned before data, never after. Predicate (the same sentence in the
  counter, the receipt label and here): *exit 0 iff F ≥ T_F* on `--rev <rev> --fetch`; receipt label
  `C1 predicate: --fetch exit 0 (F>=TARGET)`.
- **Census (freeze record, W0 reports `.ufo/waves/round-60/w0/Census*.md`, fetched 10:29–10:34Z, no lane content;
  every eligible key line re-read by the L1 against amendment A1 from the lines the seats pasted):**

  | Client | census | eligible token | key K, line (A1 value) | page (seat report) |
  |---|---|---|---|---|
  | Claude Code | ELIGIBLE | `.claude/rules/` | `paths` :198, block value, next line `- "src/api/**/*.ts"` | code.claude.com/docs/en/memory.md, quote :168 (`CensusClaudeCode`) |
  | Codex | NOT ELIGIBLE — nested `AGENTS.md`/`AGENTS.override.md` by directory; `~/.codex/rules/` is an experimental command execpolicy whose `pattern` key takes no glob | — | — | developers.openai.com Codex AGENTS.md and rules pages (`CensusCodex`) |
  | VS Code | ELIGIBLE | `.github/instructions/**/*.instructions.md` | `applyTo` :164, `applyTo: '**/*.py'` | code.visualstudio.com/docs/agent-customization/custom-instructions.md, quote :32 (`CensusVSCode`) |
  | Copilot CLI | ELIGIBLE | `.github/instructions/**/*.instructions.md` (same token as VS Code; E5 dropped by the draft) | `applyTo` :66, `applyTo: "app/models/**/*.rb"` | docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md, quote :18 (`CensusCopilotCLI`) |
  | Gemini CLI | NOT ELIGIBLE — directory-scoped `GEMINI.md` (JIT discovery in the accessed directory and its ancestors); `fileName` takes no glob | — | — | geminicli.com/docs/cli/gemini-md.md (`CensusGeminiCLI`) |
  | Cursor | ELIGIBLE | `.cursor/rules` | `globs` :85, `globs: src/components/**/*.tsx` | cursor.com/docs/rules (`Accept: text/markdown`; the `.md` URL 404s), quote :32 (`CensusCursor`) |
  | opencode | NOT ELIGIBLE — nested `AGENTS.md` by directory; the `instructions` key adds files, it does not scope a rule to matching files | — | — | opencode.ai/docs/rules.md (`Censusopencode`) |

  F_max = 4. Wrong keys the census found on the eligible pages, each failing A1: Cursor `description` :65/:99/:179
  and `alwaysApply` :65 (`CensusCursor`), VS Code `description` :163 (`CensusVSCode`), Copilot `excludeAgent` :95
  (`CensusCopilotCLI`). Sibling scan `w0/ConnSiblingScoped.md`: no lane owns the surface (FITS).
- **Target (frozen by the formula): T_F = 3.** Counter `verifiers/check_scoped_rules.py` with `TARGET = 3` (line 232),
  built by `ExecC1Counter` from the draft plus A1 (A1 sent to the seat by message before its build finished); the seat
  read this freeze record's T_F = 3 from the L1's working copy after every census report was written and set the
  constant itself (disclosed, `w0/ExecC1Counter.md`); frozen sha256
  `6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440`; self-test `0 failure(s) over 302 assertions`,
  exit 0; base `--rev 31092dc6` → `0 of 0; live not run`, exit 1 (seat run; the L1 re-runs both in a sandbox clone of
  the freeze commit, receipt `.ufo/waves/round-60/receipts/freeze-selftest.txt`).
- Commit order: target and counter are committed before the control wave scores them; a control that meets the
  predicate forces a redesign before any data (erratum), never a change after data.

**Erratum E1 — redesign before data (pre-registered branch: F_max < 3).** No C1 data has been scored; no lane row,
entry, snapshot or SKILL section exists. Control seat `CtlFabSnapshot` (`.ufo/waves/round-60/controls/CtlFabSnapshot.md`)
found that the frozen v1 counter rejects a source whose URL is already a base SOURCES URL (`check_scoped_rules.py`
`base_url_keys`, `url_key`, the `already a base SOURCES URL` reason), a conjunct the W0 census seats never scored: the
Claude Code, Copilot CLI and Cursor census pages are base rows S043, S048 and S049 (round 53, always-on rule files;
none of the three rows records `paths`, `applyTo` or `globs`: `grep "^| S04[3-9] |" corpus/SOURCES.md | grep -cw` → 0
each). Re-census W0b (`.ufo/waves/round-60/w0b/`, one scout per affected client, the base key list in
`.ufo/waves/round-60/w0b-base-url-keys.txt`) scored that conjunct:

| Client | non-base page found | L1 decision |
|---|---|---|
| Claude Code | only locale copies of the base page (`/docs/de/memory.md`, `/docs/ja/memory.md`; the token's quote meets the rule word only through an English anchor slug) | **reject**: a locale copy is the base page under another URL; using it evades the novelty conjunct without new reading |
| Copilot CLI | only the `enterprise-cloud@latest` rendering of the base how-to (same text, 8,826 B vs 8,730 B) | **reject**: a versioned copy of the base page, same reason |
| Cursor | none (`docs/context/rules` redirects to the base page; 367 sitemap URLs swept) | not eligible under v1 |
| VS Code | its census URL `docs/agent-customization/custom-instructions.md` is not a base key | eligible under v1 |

Under v1, F_max = 1 < 3, so the plan's rule redesigns the claim before data. **Counter v2** changes only that
conjunct, so that the novelty sits on the fact, not the URL: a row whose URL is a base URL is accepted only when its
SOURCES teaches cell starts `re-opens S### —` naming the base row with that URL, and the client's scope key K occurs
nowhere in that base row's line (the held row never recorded the scoping fact); the live final URL may equal only the
row's own re-opened key. Everything else, `TARGET = 3` and the predicate sentence are unchanged. Census under v2:
Claude Code (re-opens S043), VS Code (new URL), Copilot CLI (re-opens S048), Cursor (re-opens S049) → F_max = 4,
T_F = F_max − 1 = 3 by the same formula. The v1 control receipts stay committed as v1 evidence; every control is
re-scored under v2, and v2-specific controls (forged `re-opens` prefix, wrong base id, alias URL) are scored before data.
Counter v2: `verifiers/check_scoped_rules.py`, built by `ExecC1Counter` (`w0/check_scoped_rules_v2.py` sha256
`89754828…`, diff `w0/counter-v1-v2.diff`); the L1 then corrected one docstring word (line 30, "round-59" → "round-53":
the held rows are round 53's), no code change; frozen v2 sha256
`ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a`; seat self-test `0 failure(s) over 318
assertions`, exit 0; L1 sandbox receipt `.ufo/waves/round-60/receipts/freeze2-selftest.txt`.

**Erratum E2 — C1 declared exploratory before data (phase-4 rule: "a claim whose counter any control meets is
re-designed before data or declared exploratory").** Two v2 control worlds meet the predicate (`F >= 3`, `--fetch`
exit 0): `CtlReopenForged` variant d (`.ufo/waves/round-60/controls-v2/CtlReopenForged.md`: real rows, keys, quotes and
actions, but the three re-open snapshots are round-53 scratch bytes from 2026-10-22 under a row that says it was
fetched today) and `CtlReopenHeldKey` (b) (locale and enterprise alias URLs with real content; the L1 rejects aliases
by judgment in E1, the counter does not). Neither world skips the table work; each forges only source provenance (when
the bytes were fetched, or which URL is the held page), which the counter cannot authenticate. A redesign that tells
an old identical byte stream from a fresh one does not exist, and no time remains to re-control another counter
before the hard stop. So C1 is **exploratory** from this commit on, before any C1 data is integrated into the lane: it
improves `SKILL.md` with a per-client scoped-rule decision table whose semantic cells (scope key in key form with a
glob value; an action drawn from its cited line) are machine-read against committed snapshot lines, which round 59's
hook table lacked (its Events conjunct proved only that a name was printed). It verifies only as
`unprovable-but-better` with a named non-author reviewer; otherwise it lands `unprovable`. Counter v2 output is
reported as supporting evidence, never as the claim's verdict; the counter, target and predicate stay unchanged.

## Pre-freeze control wave (phase-4 rule)

Fresh mutation-tester / executor seats build and score, with the frozen counter at the freeze commit: do-nothing (the
base, and an empty section), junk rows, all-false (every row fabricated, no sources), no-reader (rows and entry, no
snapshots), fabricated snapshot (invented page whose sha256 is written into its row), wrong-key (real token, quote and
page; the Scope key cell names a printed non-scoping key such as `description` or `alwaysApply` at its real line),
invented-action (real everything, Action cell text unrelated to its cited line), and shortcut keyed on labels (rows
copied from § Hook files by client). Every receipt names the counter sha; any control that meets the predicate forces
redesign before data.

## Frontier step

SOURCES rows for C1 (≥ T_F new rows) plus the R4 correction rows, the census before/after
(`scripts/sources-census.sh validate`), one mined mistake in `corpus/lessons/round-60.md` `## Mistakes` (R1 class:
a stated word count without its counting command, with a check shown able to fail), C1 the sourced claim.

## Shape

Pre-freeze W0 (census + counter build + sibling scan, ordinary `task`), pre-freeze controls (ordinary `task`), then the
default two v1 waves (build, falsify). The L1 holds the §3 planner seat.
