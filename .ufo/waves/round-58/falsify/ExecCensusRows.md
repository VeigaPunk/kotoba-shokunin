Result: HOLDS — at `46b4a7061c688cefd3e3ec9cbb655130ba1aafbe` the counter's own `fetch` + `found_on_page` returns True for all six counted rows and the W0 census quote for five of six (opencode's census URL is False, which is why the row moved); the mapping is real, three landings differ from the census (one forced, two by choice), and two clauses of the entry's Row rule are contradicted by the rows they govern.

Seat: ExecCensusRows (falsify wave, round 58). Item: attack the census→table mapping by execution.

## Setup and receipts

- Sandbox clone: `/fast/scratch/hyaku/kotoba-r58/ExecCensusRows` (clone=0, `checkout -q 46b4a70…` = 0, `rev-parse HEAD` = `46b4a7061c688cefd3e3ec9cbb655130ba1aafbe`). No lane write, no lane git/jj command, no fleet-root cwd.
- Counter blob identity: the imported `verifiers/check_command_files.py` prints `counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c`, byte-identical to the blob the L1's `.ufo/waves/round-58/C1-measure.txt` names at the same rev. So every result below is the frozen counter, not a copy.
- All six probes ran `python3 -B` under `timeout`, exit 0:
  - `probe/run_rows.py` (per-row `fetch`+`found_on_page`, landed and census) → `probe/rows.out`, exit 0
  - `verifiers/check_command_files.py --rev 46b4a70… --fetch` → `probe/recheck.out`, exit 0
  - `probe/probe_quotes.py` (byte/line spans, HTML mechanism) → `probe/quotes.out`, exit 0
  - `probe/probe_variants.py` (alternative spans through the counter's own conjuncts) → `probe/variants.out`, exit 0
- `date -u` at the counter re-run: `Fri 23 Oct 2026 08:27:48 AM UTC`; at the six-URL curl pass: `08:29:14`–`08:29:15 AM UTC`; at the opencode re-fetch: `08:28:37 AM UTC`.
- Tooling: nothing installed or updated. No model calls, no `ask`, no browser.

## 1. Landed rows: the counter's `fetch` + `found_on_page`, per counted row

Output of `probe/run_rows.py` (verifier functions called directly: `m.fetch(url, HOSTS[client], base_url_keys(base))` then `m.found_on_page(page, quote, token)`):

```
-- Claude Code row=S089 token='.claude/commands/' norm='.claude/commands'
   url   https://code.claude.com/docs/en/slash-commands.md
LANDED  Claude Code  True  bytes=114542 sha256=6b070e872dea2890  quote_words=14
-- Codex row=S090 token='~/.codex/prompts/' norm='.codex/prompts'
   url   https://learn.chatgpt.com/docs/custom-prompts.md
LANDED  Codex        True  bytes=3357   sha256=d6f7cf8dd9f31d2f  quote_words=9
-- VS Code row=S091 token='.github/prompts' norm='.github/prompts'
   url   https://code.visualstudio.com/docs/agent-customization/prompt-files.md
LANDED  VS Code      True  bytes=13729  sha256=4ad1b2bcaf78c916  quote_words=22
-- Gemini CLI row=S093 token='~/.gemini/commands/' norm='.gemini/commands'
   url   https://geminicli.com/docs/cli/custom-commands.md
LANDED  Gemini CLI   True  bytes=12129  sha256=8f3295e8ca502b0c  quote_words=18
-- Cursor row=S094 token='.cursor/commands' norm='.cursor/commands'
   url   https://cursor.com/docs/reference/deeplinks.md
LANDED  Cursor       True  bytes=5972   sha256=7ceb657892bdfa5d  quote_words=13
-- opencode row=S095 token='.opencode/commands/' norm='.opencode/commands'
   url   https://raw.githubusercontent.com/anomalyco/opencode/4e0bc52216d91c3a8d10035837b1b6f9b82fd1d3/services/www/src/docs/content/commands.mdx
LANDED  opencode     True  bytes=7242   sha256=dda6bba03043afff  quote_words=10
```

Six of six `found_on_page` = **True**, each with `quote-in-page=True` and `token-at-boundary=True` reported separately, so the conjunction is not passing on one leg. The full counter reproduces the headline (`probe/recheck.out`, exit 0, 08:27:48 UTC):

```
custom command files found on the live page 6 of 6; new ground 4
Claude Code  BACKED … found=yes held-at-base=no
Codex        BACKED … found=yes held-at-base=yes
VS Code      BACKED … found=yes held-at-base=yes
reject Copilot CLI: SKILL.md command token ':456' is not well-formed; no entry row names the client
Gemini CLI   BACKED … found=yes held-at-base=no
Cursor       BACKED … found=yes held-at-base=no
opencode     BACKED … found=yes held-at-base=no
exit=0
```

Quote word counts are 14 / 9 / 22 / 18 / 13 / 10, all inside the frozen 6–25 band (`MIN_WORDS`/`MAX_WORDS`, counter `:247-248`).

## 2. The same functions on the W0 census URLs and quotes

From `.ufo/waves/round-58/w0/Census*.md`, the URL, quote and token each seat recorded, run through the same `fetch`+`found_on_page`:

```
CENSUS Claude Code  True   bytes=114542 sha256=6b070e872dea2890   (quote 14 words)
CENSUS Codex        True   bytes=3357   sha256=d6f7cf8dd9f31d2f   (9 words)
CENSUS VS Code      True   bytes=13729  sha256=4ad1b2bcaf78c916   (22 words)
CENSUS Gemini CLI   True   bytes=12129  sha256=8f3295e8ca502b0c   (8 words)
CENSUS Cursor       True   bytes=5972   sha256=7ceb657892bdfa5d   (13 words)
CENSUS opencode     False  bytes=32304  sha256=32591ac3db0056fd   (10 words)  ← opencode.ai/v2/docs/commands/ (HTML)
CENSUS opencode     False  bytes=6712   sha256=853516ad84f3cf9c   (10 words)  ← census's dev/packages mirror
CENSUS Copilot CLI  FETCH-ERR OSError: reached a base SOURCES URL …/cli-command-reference.md
CENSUS Copilot CLI  FETCH-ERR OSError: reached a base SOURCES URL …/cli-plugin-reference.md
```

So five of six census quotes pass unchanged, and the census's own opencode URL fails the counter. The Copilot CLI row is not a counted row; both of its candidate URLs are refused because they are already base `SOURCES.md` URLs (S028/S056).

## 3. Where the landed row differs from the census, and why

### 3a. opencode — URL moved (census `opencode.ai/v2/docs/commands/` → S095 pinned raw mdx). Forced, and the entry's reason is accurate but incomplete.

The census read the page with `curl -H 'Accept: text/markdown'`. The counter's `fetch` sends only `User-Agent: kotoba-shokunin-counter/58` (counter `:909-911`), so it gets the HTML rendering: 32,304 B, sha256 `32591ac3db0056fd…`, and `found_on_page` = **False**.

The sentence *is* on that HTML page: `raw-count 'Put global commands' = 1`, context `<p>Put global commands in <code>~/.config/opencode/commands/</code> and project commands in <code>.opencode/commands/</code>.</p>`. The failure is the counter's page normalisation: `norm_page_case` replaces a tag with a space (counter `:845`), so `</code>`+`.` becomes `.opencode/commands/ .`. Measured:

```
norm_page slice: 'put global commands in ~/.config/opencode/commands/ and project commands in .opencode/commands/ . ~/.config/…'
quote norm     : 'put global commands in ~/.config/opencode/commands/ and project commands in .opencode/commands/.'
count of '.opencode/commands/ .' in norm_page(html) = 1 ; count of '.opencode/commands/.' = 0
```

The entry's note (entry:30, "the opencode quote is from the pinned docs source because the served page is HTML without `Accept: text/markdown`") is therefore correct about *which* fetch fails, but the operative cause is the closing-tag space before the sentence period, not the absence of the sentence. Both are true; the note names the weaker one.

Two further measured facts about the landed S095 target:
- The census's *other* opencode URL (`raw.githubusercontent.com/anomalyco/opencode/dev/packages/web/src/content/docs/commands.mdx`, `08:31:32 AM UTC`, 200, 6,712 B, sha `853516ad84f3cf9c…`) is **False** too, and measurably for a different reason: `grep -c 'Put global commands' = 0`, while the two folders are printed as list items — line 82 `- Global: `~/.config/opencode/commands/`` and line 83 `- Per-project: `.opencode/commands/``. That V1 source does not carry the quoted sentence at all. Only the V2 source carries the quote, so the pinned-commit move was the only path to this quote.
- The pinned mdx is not byte-identical to what the site serves today: `diff -u` (served `Accept: text/markdown` 7,220 B / sha `c3dc75fc…` vs pinned 7,242 B / sha `dda6bba0…`), `diff_exit=1`, 10 changed lines: the mdx adds `---` / `title: "Commands"` / `---` (which is why the quote is line 21 in S095 but line 19 in the census), and two example model strings differ (`claude-sonnet-5-5` pinned vs `claude-sonnet-4-5` served; `openai/gpt-6.1-sol` vs `openai/gpt-5`). The quoted sentence is identical in both. No claim depends on the differing lines.

### 3b. VS Code — quote reshaped to `prompt-files.md:21-25` with `&#124;` pipes. Not forced; the counter admits two spans.

The census span was lines 25–28 (22 words, token first). The landed span starts at the tail of line 21. Running the counter's own conjuncts (`word` cap, `token_span`, `command_word_outside`, `found_on_page`) on four spellings of the same page:

| variant | words | cap 6–25 | token in quote | command word outside | found_on_page |
|---|---|---|---|---|---|
| V1 landed (21 tail–25) | 22 | True | True | True | **True** |
| V2 table only (22–25) | 14 | True | True | **False** | True |
| V3 whole sentence (21–25) | 30 | **False** | True | True | True |
| V4 census (25–28) | 22 | True | True | True | **True** |

Consequences, all executed rather than argued:
- The 14-word table-only span is rejected because the only command/prompt word in it is inside the token (`command_word_outside` False). The 8-word prefix `that the Local harness uses for prompt files.` is load-bearing; it is not decoration.
- The page's own sentence naming the folder is line 21 (`The following table lists the default file locations that the Local harness uses for prompt files.`), and it does **not** contain `.github/prompts`; gluing it to the table rows costs 30 words and busts the frozen cap.
- V4 (the census span) also passes every test. The landed reshape is therefore a **choice between two passing spans**, not a necessity, and it is the one that starts mid-sentence (`that the Local harness…`). [INFERENCE] it was chosen to keep the `Scope | Default file location` header so the pipes read as a table, not to satisfy any counter rule.
- Defect against the entry's own Row rule (entry:23-27: "the quote is the page's own sentence naming it"): no ≤25-word span on this page both starts at a sentence and holds the token, so this clause is unsatisfiable for VS Code and false for the landed row. The Quote-notes paragraph (entry:28-31) discloses the pipe escaping and the `:21-25` span but not the mid-sentence start. Text the L1 may integrate: `the quote is the page's own sentence naming it, or for a page that names the folder only in a table, the shortest span that holds the folder and a command/prompt word outside it`.

### 3c. Gemini CLI — quote extended from the census's 8-word cut to the full 18-word sentence. Not forced; an improvement both ways.

Both pass: census 8 words (`…These commands`) → found True, cap True, command word outside True; landed 18 words (`…are available in any project you are working on.`) → same, found True. The landed version is the only one of the two that reads as a complete sentence. Disclosed at entry:29-30 ("the Gemini CLI quote keeps the page's list marker `1.` and bold markers"). No defect.

### 3d. Claude Code, Codex, Cursor — identical URL, quote and token in census and table.

Byte-exact against the pages: v1's quote is a raw substring of `slash-commands.md` line 172; Codex's of `custom-prompts.md` line 62; Cursor's of `deeplinks.md` line 54. All six tokens are identical between census and table (`token` column in §1 vs the census reports), and each entry cell equals its `SKILL.md` cell, which the counter's E4 already enforces for the backed rows.

## 4. The Row rule against the pages it rules (axis/sizing attack)

Entry:23-27 says the cell leads with "the project folder where both a project and a user folder exist, else the only one documented". Measured per page (counts of the printed spelling in the bytes the counter fetched):

| client | project spelling | user spelling | landed | rule says | verdict |
|---|---|---|---|---|---|
| Claude Code | `.claude/commands/` ×14 | `~/.claude/commands` ×**0** | project | only one documented → that one | conforms |
| Codex | absent | `~/.codex/prompts` ×4 | user | only one documented → that one | conforms |
| VS Code | `.github/prompts` ×1 | none printed (`user data (specific…` only) | project | only one documented | conforms |
| Gemini CLI | `<your-project-root>/.gemini/commands/` ×1, `<project>/.gemini/commands/` ×4 | `~/.gemini/commands/` ×6 | **user** | project folder when both exist | **contradicts** |
| Cursor | `.cursor/commands` ×1 | `~/.cursor/commands` ×0 | project | only one documented | conforms |
| opencode | `.opencode/commands/` ×18 | `~/.config/opencode/commands/` ×3 | project | project | conforms |

The Gemini CLI inversion is forced by the frozen token grammar, measured: `token_well_formed('<your-project-root>/.gemini/commands/') = False`, `token_well_formed('.gemini/commands/') = True` (`TOKEN_RE` admits neither `<` nor `>`). So the rule's project-first clause cannot be applied to the one row where both folders are documented in a form the grammar accepts only for the user folder. Not disclosed in the entry (Gemini_CLI.txt line 15: `` `<your-project-root>/.gemini/commands/`. These commands are specific to the``). Text the L1 may integrate: `the project folder where both exist and the page prints it in well-formed form, else the user folder`.

## 5. The reject line, and how much of "6 of 6" is content and how much is cell order

The counter's Copilot CLI line is `SKILL.md command token ':456' is not well-formed; no entry row names the client`. Measured bases: `token_well_formed(':456') = False`, and `SKILL.md:116` opens its Command-files cell with the citation `` `:456` `` rather than a path. The census's substantive reasons are different: `foreign_marker('Copilot CLI','.claude/commands/') = 'Claude Code'`, the same normalised path as Claude Code's row, and `com.github.copilot/commands/` failing the leading-dot rule. So the printed reason is the weakest of the three available, and the entry's Limits paragraph does disclose that the counter reads the first backticked span — the output is not wrong, it is uninformative.

Content dependence of the headline number, from an in-memory mutation (skill text only, no lane or sandbox file written; `judge()` called directly):

```
MUTANT Claude Code  backed=False
   why=["SKILL.md command token '.claude/commands/' is shared by rows Claude Code, Copilot CLI"]
MUTANT Copilot CLI  backed=False
   why=["… carries Claude Code's marker 'claude'", "… is shared by rows Claude Code, Copilot CLI", 'no entry row names the client']
mutant without Claude Code: F=5 G=3 (predicate=0)   ;  shipped tree: F=6 G=4
```

So if the Copilot CLI cell had led with the folder its own docs print, E5 would drop Claude Code too and the printed count would be `5 of 6; new ground 3`. The frozen predicate still exits 0 (`predicate=True, found=5, ground=3 → 0`), so **the claim's verdict does not depend on the cell's wording, but the printed 6 does**. Worth one line in the entry's Limits rather than any row change.

Cross-check on the VS Code row raised by `CensusVSCode.md`: `docs.github.com` (Copilot CLI's pinned host) does print the token — `your-first-prompt-file.md:47`, fetched `08:29:41 AM UTC`, HTTP 200, 3,039 B, sha256 `117468ccb3abe5d07ae8f76a309f291b0fb93dae6d06de789feb9b90aa87b0ed`, line read `1. Save the prompt file above as `.explain-code.prompt.md` in your `.github/prompts` folder.` (backticks in the source). The counter's E5 compares `SKILL.md` rows only and the Copilot row carries `:456`, so no disqualification fires; `.github/prompts` is not exclusive to VS Code in content, only in source. Neither the entry nor the SKILL cell claims exclusivity, so no text change is needed — this is a measured boundary, not a defect.

## 6. No-harm: the sources have not moved and the counter was not disturbed

Six-URL curl pass, `08:29:14`–`08:29:15 AM UTC`, each `curl -sSL -w 'status=%{http_code} bytes=%{size_download}'`, exit 0:

| URL | status | bytes | sha256 |
|---|---|---|---|
| `code.claude.com/docs/en/slash-commands.md` | 200 | 114,542 | `6b070e872dea28905a7ea7f45c4d5960f5bdf28cc73ac808799af6d50435ffbd` |
| `learn.chatgpt.com/docs/custom-prompts.md` | 200 | 3,357 | `d6f7cf8dd9f31d2faf5604ef3a6f8322132a7b66fa50823109cb681e372a0fa9` |
| `code.visualstudio.com/docs/agent-customization/prompt-files.md` | 200 | 13,729 | `4ad1b2bcaf78c9166b1609610f354d9cb8b1ff9c9e7cf643c443fad04dac6685` |
| `geminicli.com/docs/cli/custom-commands.md` | 200 | 12,129 | `8f3295e8ca502b0c70bb3bf672f0dc0130ecb868fad4a88d5cac0f36ac6f3872` |
| `cursor.com/docs/reference/deeplinks.md` | 200 | 5,972 | `7ceb657892bdfa5d7a32f1168411fcaeb63c2f6ab41a5f0c45116a0a3f3a6bf4` |
| `raw.githubusercontent.com/anomalyco/opencode/4e0bc52…/services/www/src/docs/content/commands.mdx` | 200 | 7,242 | `dda6bba03043afff71a0bec4f0cfa40aaac12d53c1b20358df15e557c1a7ec11` |

Every byte count and sha256 equals the one recorded in `corpus/SOURCES.md` S089/S090/S091/S093/S094/S095 (seats Src* at 08:07–08:11 UTC), ~20 minutes and one full counter run later. The counter re-run used the same blob (`aae12d36…`) as the L1's 08:20 receipt, so the falsify measurements and the claim's receipt are the same instrument on the same tree.

## 7. Risks and limits

- Five of six counted quotes ride mutable live pages (only S095 is commit-pinned). Any upstream edit changes F with no lane change; the receipts in `corpus/SOURCES.md` are the only drift detector.
- `found_on_page` will read **False** for an HTML-only page whose quoted sentence ends immediately after a code span, because `norm_page_case` turns `</code>` into a space before the period (measured on the opencode census URL). A future client whose only page is HTML is at risk of being scored absent while the sentence is present.
- Both Copilot CLI candidate URLs are base `SOURCES.md` URLs, so `fetch` refuses them by design; no future count can be attempted from those pages without a different URL.
- Scope kept to the row-named quote sources plus the opencode mirror and the Copilot tutorial. I did not re-open the census auxiliaries (`cursor.com/changelog/1-6`, the Gemini reference/extensions pages, the Codex README); no finding above depends on them.
- [INFERENCE] only where marked: the reason the VS Code span was reshaped (both V1 and V4 pass, so the intent is not recoverable from the counter).
- Nothing was written outside `/fast/scratch/hyaku/kotoba-r58/ExecCensusRows/` and this report. No lane file, `.ufo` state, MANIFEST, or sibling lane was touched.
