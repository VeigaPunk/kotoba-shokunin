Result: BREAKS — C1's frozen predicate is met (exit 0, `plugin manifests found on the live page 5 of 7; new ground 4`) by a hollow control whose "manifest" cells are the bare words `Plugins`/`Extensions` and whose quotes are 3–5-word page fragments, so the claim can be scored green without one sourced manifest fact.

# C1 pre-freeze control — do-nothing and junk (seat KotobaR57.CtlC1DoNothingJunk)

## Scored object

- Counter: `verifiers/check_plugin_manifests.py` from `ee50d8fa7b5d260fff8bc332f4a90513bee518ff`,
  sha256 `2ac51d2a2f50d85590c307e6ef5aab05a0b660de42a33e5657011ecc05d6305b` (printed as line 1 of every
  run). Unchanged in the sandbox: `git --no-optional-locks diff --quiet ee50d8fa -- verifiers/check_plugin_manifests.py`
  exit 0 (the receipt header records this).
- Sandbox: `/fast/scratch/hyaku/kotoba-r57/KotobaR57.CtlC1DoNothingJunk`, clone of the lane, checked out at
  `ee50d8fa`.
- Raw receipt: `.ufo/waves/round-57/controls/CtlC1DoNothingJunk.txt` — 10 runs, exit code after each, each run's
  first line the counter sha256 above and its second line `counter rev <measured rev>`.
- Measured revisions: base `47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a`; freeze
  `ee50d8fa7b5d260fff8bc332f4a90513bee518ff`; `sandbox e0467875067425fec8b7b2214639a7c206a860bb` (world A);
  `sandbox d6705829c26308634688730109cdedf7c1b6fadc` (world B); `sandbox f004025e98da24ca5a4559d3a22b7211e2ff4a8b`
  (world C), all under `/fast/scratch/hyaku/kotoba-r57/KotobaR57.CtlC1DoNothingJunk`.

| run | measured rev | --fetch | summary line | exit |
|---|---|---|---|---|
| do-nothing base | `47c05558` | no | `plugin manifests backed 0 of 0; new ground not computed (needs --fetch)` | 1 |
| do-nothing base | `47c05558` | yes | `plugin manifests found on the live page 0 of 0; new ground 0` | 1 |
| do-nothing freeze | `ee50d8fa` | no | `plugin manifests backed 0 of 0; …` | 1 |
| do-nothing freeze | `ee50d8fa` | yes | `plugin manifests found on the live page 0 of 0; new ground 0` | 1 |
| junk A (no sources) | `sandbox e0467875` | no | `plugin manifests backed 0 of 7; …` | 1 |
| junk A (no sources) | `sandbox e0467875` | yes | `plugin manifests found on the live page 0 of 7; new ground 0` | 1 |
| junk B (7 junk sources) | `sandbox d6705829` | no | `plugin manifests backed 7 of 7; …` | 1 |
| junk B (7 junk sources) | `sandbox d6705829` | yes | `plugin manifests found on the live page 0 of 7; new ground 0` | 1 |
| junk C (bare-word tokens) | `sandbox f004025e` | no | `plugin manifests backed 7 of 7; …` | 1 |
| junk C (bare-word tokens) | `sandbox f004025e` | yes | `plugin manifests found on the live page 5 of 7; new ground 4` | **0** |

## Findings

### 1. Do-nothing — both revisions, both modes: exit 1 (no content, no surprises)

At `47c05558` and at `ee50d8fa` every client rejects with `SKILL.md rows naming client: 0 (need exactly 1);
no entry row names the client`; K=0, F=0, ground 0. Correct behaviour: an empty world cannot pass.

### 2. Junk A — a well-formed table with no source rows: exit 1 both modes

World A (`sandbox e0467875`) adds the exact heading `### Plugin manifests by client` with the frozen header and
seven rows (tokens `.claude-plugin/plugin.json`, `.codex-plugin/plugin.toml`, `.vscode-plugin/plugin.json`,
`.copilot-plugin/plugin.json`, `gemini-extension.json`, `.cursor-plugin/plugin.json`, `.opencode/plugins/`; action
cell 8 words), a knowledge entry table with seven plausible quotes, and a `## Gate` section carrying those quotes.
K=7 — so all seven tokens pass the grammar — but `backed 0 of 7` and every rejection is
`entry row S79x: S79x absent or malformed in SOURCES.md`. The SOURCES arm alone stops the table; this is the
cheapest hollow world and it is rejected.

### 3. Junk B — seven junk SOURCES rows on live pinned-host pages that do not hold the quotes: exit 1 both modes

World B (`sandbox d6705829`) adds `S790`–`S796` (kind `docs`, tier `A`, status `mined`, opened `2026-10-23`, each on
a pinned host) and keeps the fabricated quotes and their Gate records. Offline the counter says `backed 7 of 7`:
the SKILL.md grammar, the entry token/quote rules, the Gate record and the new-row/pinned-host/not-base-URL SOURCES
rules are all satisfiable by hollow content. With `--fetch` the answer is `found 0 of 7; new ground 0`, exit 1 —
the live arm is what separates this world.

Per-client diagnosis (probe in the sandbox, `.ctl/probe.py` and `.ctl/pages/`, which loads the frozen counter's own
`norm_page`, `token_at_boundary` and `token_forms`; not a scored run):

- pages fetched with curl, all HTTP 200 (UTC 2026-10-23T04:18:04Z–04:18:05Z):
  code.claude.com/docs/en/plugins 477,000 B; developers.openai.com/codex/ 381,019 B; code.visualstudio.com/api
  53,489 B; docs.github.com/en/copilot 931,788 B; geminicli.com/docs/extensions/ 102,412 B; cursor.com/docs
  603,587 B; opencode.ai/docs/plugins/ 109,777 B;
- `quote_on_page=False` for all seven quotes;
- the token is on the page at a boundary for only two clients: Claude Code (`.claude-plugin/plugin.json`) and
  opencode (`.opencode/plugins/` and `.opencode/plugins`). The other five tokens are invented, so for them both arms
  fail. For Claude and opencode only the quote arm fails: the page text around the token reads, verbatim,
  `The manifest, a JSON file at .claude-plugin/plugin.json , gives the plugin its name` and
  `Project plugin directory ( .opencode/plugins/ )` — neither holds the fabricated quotes.

So world B proves false provenance is rejected, and it also shows that on these seven pinned pages a real row is
available for only two clients at these tokens.

### 4. Junk C — the predicate MEETS with bare-word "manifests" and page fragments: exit 0

World C (`sandbox f004025e`) is deliberately hollow and scores `plugin manifests found on the live page 5 of 7; new
ground 4`, exit 0. It is a junk world: five clients are found, no row names a manifest file that grounds the claim.

Three things make it pass.

**(a) `token_well_formed` admits a bare word.** `TOKEN_RE` (`verifiers/check_plugin_manifests.py:211`) accepts a
single segment, and `token_well_formed` (`:474-483`) only asks that some segment split on `-._` be
`plugin`/`plugins`/`extension`/`extensions`. So `Plugins` and `Extensions` are "manifest tokens" for a row:

- world C `SKILL.md:604-610` — Codex `` `Plugins` ``, VS Code `` `Extensions` ``, Gemini CLI `` `Extensions` ``;
  Claude Code keeps `.claude-plugin/plugin.json`, opencode keeps `.opencode/plugins/`, Copilot CLI and Cursor keep
  their invented paths.

**(b) A 3-word page fragment is a valid quote.** `MIN_WORDS = 3` (`:171`). The entry (`corpus/knowledge/plugin-manifests-round57.md:8-14`
in `sandbox f004025e`) and the Gate (`corpus/lessons/round-57.md:9-15`) carry fragments lifted verbatim out of the
pages' navigation and list text, found with the counter's own normalisation:

| client | token | quote (world C) | page location |
|---|---|---|---|
| Claude Code | `.claude-plugin/plugin.json` | `.claude-plugin/plugin.json , gives the plugin` | mid-sentence, 5 words |
| Codex | `Plugins` | `Plugins and connections Plugin` | nav |
| VS Code | `Extensions` | `Extensions Publishing Extensions` | heading pair |
| Gemini CLI | `Extensions` | `Extensions Browse extensions` | nav |
| opencode | `.opencode/plugins/` | `plugin directory. .opencode/plugins/` | list label |

None of these says where a manifest lives or what a plugin ships; the Claude fragment is cut mid-sentence before
the manifest is named.

**(c) G counts a case-variant of an already-held word as new ground.** `new_ground` (`:928-934`) keys `held` by the
case-preserved token and only casefolds when counting distinct values, so `Plugins` is new ground while `plugins` is
held. Measured with the counter's own `held_in_base` at base: `Plugins held=False`, `plugins held=True`,
`Extensions held=False`, `extensions held=True` (sandbox `.ctl/held.txt`). The successful run prints
`held-at-base=no` for both `Plugins` and `Extensions`, giving distinct values `plugins`, `extensions`,
`.claude-plugin/plugin.json`, `.opencode/plugins` → G=4.

**(d) Side gaps this world also exercised.** The entry's `Manifest` cell is never read: `entry_row_verdict`
(`:552-566`) uses `er[2]` (source) and `er[3]` (quote) only. In world C the entry still said
`.codex-plugin/plugin.toml` / `.vscode-plugin/plugin.json` / `gemini-extension.json` while `SKILL.md` said
`Plugins` / `Extensions`, and all seven rows were still BACKED. The same token `Extensions` is also accepted for two
different clients (VS Code and Gemini CLI) with no cross-client uniqueness rule.

### 5. Hidden landing blocker outside the counter: the SKILL.md 600-line box

`SKILL.md:296` carries the executed box `File ≤ 600 lines; …`; the file is 598 lines at the freeze commit and the
world C table (heading + blank + header + separator + 7 rows = 12 lines) takes it to 610 lines in `sandbox f004025e`.
The minimum C1 table is 10–12 lines for seven clients, so C1 as specified lands over a box its own lane gate
executes (`trigger.line_budget`) unless at least 8–10 existing lines are removed. The plan's C1 surface names no
line removal. The frozen counter cannot see this; the pre-freeze call should.

## Impacted axes

- **depth (worked by C1)** — not measured by the predicate: green is reachable with no manifest location and no
  grounding prose. The axis would be credited for a hollow table.
- **calibration** — the predicate no longer separates a sourced table from a hollow one; a control meeting the
  frozen predicate is the strongest calibration failure available at pre-freeze.
- **consistency** — two duplicate authorities the counter tolerates: the entry `Manifest` column is never compared
  to `SKILL.md`, and one token may serve two clients.
- **operability** — the 600-line box on `SKILL.md` fails at landing (598 of 600 at freeze).
- freshness and adjacency: not affected by these controls.

## Smallest safe correction

Add a path-shape requirement to `token_well_formed` and leave every other frozen arm untouched:

```python
n = normalise(token)
if n.lower() in PLUGIN_WORDS:                      # a bare plugin/extension word is not a manifest
    return False
if "/" not in n and not re.match(r"^[A-Za-z0-9_-][A-Za-z0-9_.-]*\.[A-Za-z0-9]+$", n):
    return False                                    # no path and no dotted filename
```

This keeps the spec's own examples (`.claude-plugin/plugin.json` has a `/`; `gemini-extension.json` has a dotted
filename; `.opencode/plugins/` has a `/`) and rejects `Plugins`, `Extensions`, `vscode-extensions` and `extension.`.
Shown on a **probe copy, not the scored counter** (`sha256 4d71aabf4d577e80aa079c781b19d46c7cdf17291cb416cade589f14cda0889b`,
sandbox `.ctl/patched-not-scored.py`; its output is not a receipt): world C scores `plugin manifests found on the
live page 2 of 4; new ground 2`, exit 1, with `reject Codex/VS Code/Gemini CLI: SKILL.md manifest token '…' is not
well-formed`, while Claude Code and opencode stay found. Because the plan's own rule says a stricter erratum must be
committed before data, this control forces C1 to be redesigned (stricter token) or withdrawn before any data seat.

Two smaller corrections worth folding into the same erratum: compare the entry `Manifest` cell's first backticked
span to the `SKILL.md` token (or drop the column), and state in the plan that C1 must cut lines to stay inside
`SKILL.md`'s 600-line box. If the claim wants prose grounding rather than fragments, raise `MIN_WORDS` (the
`plugin directory. .opencode/plugins/` example passes at 3); that is a scope choice for the L1, not a defect of
this control.

## Bounds and hygiene

- Only two lane files written: this report and `.ufo/waves/round-57/controls/CtlC1DoNothingJunk.txt`. No lane git
  writes, no jj, no fleet writes; all sandbox commits are inside `/fast/scratch/hyaku/kotoba-r57/KotobaR57.CtlC1DoNothingJunk`
  and every hash above is labelled `sandbox <hash> (<path>)`.
- Every run was wrapped in `timeout` (300 s; observed ≤4 s); no `pkill`/`killall`; no contention tests; no headless
  browser; one `curl` per page with `--max-time 30`.
- Tooling: nothing installed or upgraded (no pacman transaction attempted); `curl`, `git`, `python3` were already
  present.
- No real C1 content meant for landing and no C2 instrument change were written; world D's single page fragment is control-only, not an admitted source or entry.

## v2 re-score

Erratum 1 names C1 v2 at lane commit `01312a77e36317feb6e961aba77841ddab1225ca`; copied bytes into the same
sandbox, sha256 `bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e`, committed there as
`sandbox bf6ac028f12e7da2e807f88cf6b0a289c7a4f5fd`
(`/fast/scratch/hyaku/kotoba-r57/KotobaR57.CtlC1DoNothingJunk`). The v2 counter was unmodified for all runs.
The complete raw re-score is appended to the same `.txt` receipt; each run prints this sha256 and its measured
revision.

| world | measured revision | v2 no-fetch | v2 --fetch | result |
|---|---|---|---|---|
| do-nothing base | `47c05558` | backed 0 of 0 | found 0 of 0, G=0 | exit 1 both |
| do-nothing freeze | `ee50d8fa` | backed 0 of 0 | found 0 of 0, G=0 | exit 1 both |
| junk A, no sources | `sandbox e0467875` | backed 0 of 5 | found 0 of 5, G=0 | exit 1 both |
| junk B, seven junk sources | `sandbox d6705829` | backed 5 of 5 | found 0 of 5, G=0 | exit 1 both |
| original world C | `sandbox f004025e` | backed 2 of 3 | found 0 of 3, G=0 | exit 1 both |
| adapted hollow world D | `sandbox b976598184193f6ad4c3cf01c997a193df2bdbe7` | backed 7 of 7 | found 1 of 7, G=1 | exit 1 both |

World C is rejected under v2 by the new token, shared-token, entry-Manifest and 6-word guards. World D is the
five-minute hollow adaptation: all seven tokens are distinct v2-shaped `.json` paths, all entry Manifest cells
match, all quotes are at least six words, Gate/SOURCES rows are present, and all rows are BACKED. Its seven paths
are invented except the Claude path; the other six quotes are fabricated and not on their cited pages. The Claude
quote is a short page fragment (`.claude-plugin/plugin.json , gives the plugin its name`), not a landing entry; the
control remains hollow in purpose and metadata. Only Claude is found; the remaining six token/quote pairs fail the
live-page test. Thus the v2 hollow adaptation does **not** meet the predicate. Best hollow-control score: **F=1/7,
G=1, exit 1** (`sandbox b976598184193f6ad4c3cf01c997a193df2bdbe7`).

During the five-minute adaptation attempt I also checked four alternate official pinned-host pages, using ordinary
curl (no browser): Codex `https://developers.openai.com/codex/plugins/` (HTTP 200, 501,773 B,
sha256 `9d77bbd1cd179df75f678099b8fb9376b2094cd59c28eb35ab64960cdd8f69ae`, 04:39:36Z), Copilot
`https://docs.github.com/en/copilot/concepts/extensions` (HTTP 200, 620,875 B, sha256
`e302304b3523b78b58a244133b37ba09155481d160d0b838455d4a17f612e446`, 04:39:36Z), Cursor
`https://cursor.com/docs/plugins` (HTTP 200, 483,761 B, sha256
`5501398d2ada6dc3f54f59cd06b83c1db5ab3a39876033a1274d32b848910a03`, 04:39:37Z), and Gemini
`https://geminicli.com/docs/extensions/` (HTTP 200, 102,412 B, sha256
`a0390ab023474895db1eb34dfbd006485117148cf8843f9ad8532377be65456f`, 04:39:37Z). The v2 token miner found no
eligible tokens on the Codex, Copilot or Gemini pages; it found `.cursor-plugin/plugin.json` on the Cursor page,
where the surrounding text expressly documents that manifest. I did not use that real claim as a hollow row.
This attempt found no hollow way to reach F>=5; no extra world was needed to determine the predicate remained
unmet.
