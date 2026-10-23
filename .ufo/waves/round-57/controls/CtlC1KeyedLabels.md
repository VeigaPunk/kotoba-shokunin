Result: MIXED — the frozen C1 counter rejects the keyed-labels world (`found 0 of 7`, exit 1), yet every non-fetch guard is satisfiable from the counter's own docstring and labels, and the live-page guard is the only wall: with it alone removed the same world prints `found 7 of 7; new ground 7` and exits 0.

Counter attacked: C1 `verifiers/check_plugin_manifests.py` as committed at
`ee50d8fa7b5d260fff8bc332f4a90513bee518ff`, sha256
`2ac51d2a2f50d85590c307e6ef5aab05a0b660de42a33e5657011ecc05d6305b` (the sha the
counter itself prints; the copy in `sandbox b0514f6347a5dbed21f3af405d19371b21cbff17`
(`/fast/scratch/hyaku/kotoba-r57/CtlC1KeyedLabels`) hashes identically, checked with
`git show ee50d8fa…:verifiers/check_plugin_manifests.py | sha256sum`). No byte of the
counter was modified; it was never copied into a variant for any scored run.

## The control world

Built only from the counter's docstring examples (`.claude-plugin/plugin.json`,
`gemini-extension.json`, `.opencode/plugins/`), its `CLIENTS`/`MARKERS` labels (each
remaining token is `<marker>-plugin/plugin.json`), and its self-test fixture shapes
(`.claude-plugin/plugin.json`). No page was opened or read: URLs are guessed paths on
the counter's own pinned hosts, and every quote is invented. World commit:
`sandbox b0514f6347a5dbed21f3af405d19371b21cbff17`, one commit on top of the freeze
commit; it adds only `SKILL.md` § `### Plugin manifests by client` (7 rows),
`corpus/knowledge/plugin-manifests-round57.md`, 7 rows `S079`–`S085` in
`corpus/SOURCES.md`, and a hollow `corpus/lessons/round-57.md` `## Gate`.

| Client | token (docstring/label-keyed) | id | guessed URL (unread) |
|---|---|---|---|
| Claude Code | `.claude-plugin/plugin.json` | S079 | `code.claude.com/docs/en/plugins` |
| Codex | `.codex-plugin/plugin.json` | S080 | `developers.openai.com/codex/plugins` |
| VS Code | `.vscode-plugin/plugin.json` | S081 | `code.visualstudio.com/api/extension-guides/overview` |
| Copilot CLI | `.copilot-plugin/plugin.json` | S082 | `docs.github.com/en/copilot/how-tos/copilot-cli/plugins` |
| Gemini CLI | `gemini-extension.json` | S083 | `geminicli.com/docs/extensions/` |
| Cursor | `.cursor-plugin/plugin.json` | S084 | `cursor.com/docs/plugins` |
| opencode | `.opencode/plugins/` | S085 | `opencode.ai/docs/plugins/` |

Quotes were shaped to the checks, e.g. Claude Code `"Plugins are declared in
`.claude-plugin/plugin.json`."` (5 words, token inside, `Plugins` outside the span),
each repeated verbatim in `## Gate`.

## Scores (all from the frozen counter, `--rev b0514f63…`)

1. Structural run (no `--fetch`), `timeout 120 python3 -B verifiers/check_plugin_manifests.py --rev b0514f63…`
   → exit 1, `plugin manifests backed 7 of 7; new ground not computed (needs --fetch)`.
   Every guard before the live page passes: table heading/header/cells, token grammar,
   foreign-marker, 3–25-word quote containing the token case-sensitively plus a
   plugin/extension word outside it, `S###` id absent at base, kind `docs`, tier `A`,
   status `mined`, opened `2026-10-23`, pinned host, new (non-base) URL, Gate quote.
2. Predicate run `--fetch` → exit 1 (receipt
   `.ufo/waves/round-57/controls/CtlC1KeyedLabels.txt`, sha256
   `1ab5f3102717669d218649e18a5324cdb4a0f8dc318124a785c200b6b75e543e`, fetched
   2026-10-23T04:17:50Z):
   ```
   plugin manifests found on the live page 0 of 7; new ground 0
   ```
3. Same run with `--json` (frozen counter): 6 of 7 guessed URLs answered (no
   `fetch_error`); Copilot CLI `HTTP Error 404: Not Found`. So the world fails on
   reachable pages, not on dead guesses alone.

## Which guard stops it

`found_on_page()` inside the `--fetch` stage — specifically its **quote conjunct**
`norm(quote) in norm_page(page_text)`. A probe that imports the frozen counter
unmodified and calls its own `fetch`/`norm`/`norm_page`/`token_forms`/
`token_at_boundary` reported, for all 7 rows:

```
Claude Code  bytes=477000 quote_in_page=False token_forms_hit=['.claude-plugin/plugin.json']
Codex        bytes=501773 quote_in_page=False token_forms_hit=[]
VS Code      bytes=67319  quote_in_page=False token_forms_hit=[]
Copilot CLI  FETCH-ERROR HTTP Error 404: Not Found
Gemini CLI   bytes=102412 quote_in_page=False token_forms_hit=[]
Cursor       bytes=483761 quote_in_page=False token_forms_hit=['.cursor-plugin/plugin.json']
opencode     bytes=109777 quote_in_page=False token_forms_hit=['.opencode/plugins/', '.opencode/plugins']
```

The probe printed booleans and byte counts only, never page text. The invented
quotes are absent everywhere (7/7), while 3 guessed token strings do occur at token
boundaries on the guessed pages, unread — so the token side is guessable from labels
alone; the quote is the wall.

## Does removing that guard alone let it pass?

Two precise readings, both measured with the counter's own `predicate()`:

- Remove only the quote conjunct (token still required): found would be 3 → F=3 < 5,
  `predicate(True, 3, 3)` → exit 1. **No.** G would already be met (3 distinct
  zero-held tokens), but F stops it.
- Remove the live-page guard as a whole (found := backed, nothing else changed):
  `predicate(True, 7, 7)` → exit 0. The counter's own `held_in_base`/
  `new_ground` give `held-at-base` **False for all seven** tokens
  (`{'.claude-plugin/plugin.json': False, '.codex-plugin/plugin.json': False,
  '.copilot-plugin/plugin.json': False, '.cursor-plugin/plugin.json': False,
  '.opencode/plugins': False, '.vscode-plugin/plugin.json': False,
  'gemini-extension.json': False}`), so G=7 clears G≥3 **by construction**.
  **Yes — removing that one guard lets a zero-source, zero-read world pass.**
- Non-fetch reading (`--fetch` dropped) stays exit 1, so the fetch flag itself is
  load-bearing, not decorative.

So C1's discrimination rests on exactly one check: the live page must literally hold
the quote. The `G>=3` half supplies no evidence of learning — a world keyed on the
counter's labels clears it with tokens that are all new ground at base — and the
structural half is fully keyed-open.

Leads I did not turn into a control (marked, not claimed): a page that reflects
arbitrary text on a pinned host would satisfy the quote conjunct. I probed only the
obvious github.com reflection path: `github.com/anthropics/claude-code/search?q=…`
returns `302` to `https://github.com/search?q=repo%3Aanthropics%2Fclaude-code+…`,
whose final path `/search` is outside the pin `/anthropics/claude-code`, so `host_ok`
on the final URL rejects it (curl status/redirect only, 2026-10-23T04:19Z). [INFERENCE]
that guard covers that particular reflection path; other pinned hosts were not probed.

## Impacted axes

- **depth** (C1's axis): the claim's learning content is guarded only by the live
  quote; hollow structural content is free.
- **calibration**: the predicate separates "guessed world" from "sourced world" by one
  conjunct; a single relaxation turns F from 0 to 7.
- **consistency**: invented `S079`–`S085` rows pass every SOURCES check that reads the
  row (`docs`/`A`/`mined`/opened/pinned host/not-at-base); nothing ties a row to an
  actual access.
- **freshness**: `opened 2026-10-23` is a literal the author types; it is keyable.

## Smallest safe correction

Add one conjunct that a guess cannot satisfy and that reuses the fetch already made:
require the SOURCES row's anchor cell to record the fetch evidence —
`fetched <ISO>Z, HTTP <status>, <bytes> B, sha256 `<hex>`` — and have the `--fetch`
stage recompute `sha256` (and the byte count) of the bytes it fetched and require them
to equal the recorded values before `found_on_page` is consulted. That is one cell
convention plus one comparison in `fetch`/the `--fetch` loop; it costs no new network
call and no new revision read. This hollow world carries no hash (its rows say
`guessed path, page unread`), and a fabricated hash fails because the counter hashes
the live bytes itself. It does not fix the Q31 gap the plan already names — a real
seat could still copy a page fragment that merely mentions the file — which stays the
falsify-wave reviewer's reading.

No tool install or upgrade was made. Longest command was the `--fetch` score (2 s,
under `timeout 420`); no process was killed. Lane writes: only this report and
`CtlC1KeyedLabels.txt` under `.ufo/waves/round-57/controls/`; all git writes were in
the labelled sandbox clone.
