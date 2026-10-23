Result: BREAKS — the frozen C1 predicate is met (exit 0, `plugin manifests found on the live page 7 of 7; new ground 3`) by a hollow table whose "Plugin manifest" column names bare words (`Plugins`, `Extensions`) and page navigation strings; the four assigned network-side fabrication worlds (404, off-pin redirect, absent quote, URL/longer-path token) are all rejected at 0 of 7.

# CtlC1Fabricated — fabricated-source control for C1

Seat: KotobaR57.CtlC1Fabricated. UTC 2026-10-23T04:17Z–04:31Z.
Counter: `verifiers/check_plugin_manifests.py`, sha256 `2ac51d2a2f50d85590c307e6ef5aab05a0b660de42a33e5657011ecc05d6305b`
(the plan's frozen version; every run printed this sha in its first line). Counter bytes never modified; no
patched counter was used. `--self-test` was not run by me (not needed for a score; the author's receipt stands).
Sandbox clone: `/fast/scratch/hyaku/kotoba-r57/CtlC1Fabricated`, checked out at
`ee50d8fa7b5d260fff8bc332f4a90513bee518ff`. Every sandbox hash below is labelled
`sandbox <hash> (/fast/scratch/hyaku/kotoba-r57/CtlC1Fabricated)`; none is a lane hash.
Raw receipt: `.ufo/waves/round-57/controls/CtlC1Fabricated.txt` (final: 213 lines, sha256
`60d4d3a2fea9b5d6…`; the v1 part is the first 124 lines, sha256 `c55bfa82cbe4d775…`); line pointers below
are to the final file.

## Worlds and scores

All five worlds are complete SKILL table + entry + SOURCES rows + `## Gate`; each was committed in the
sandbox and scored with `timeout 300 python3 -B verifiers/check_plugin_manifests.py --rev <rev> --fetch`.

| world | what it fakes | sandbox rev | result | exit |
|---|---|---|---|---|
| W1-404 | 7 pinned-host docs URLs that 404; fabricated quotes; Gate holds them | `cde10678…` | `0 of 7; new ground 0` | 1 |
| W2-offpin | 3 pinned URLs that redirect off the client's pins + 4 404s | `04fc043e…` | `0 of 7; new ground 0` | 1 |
| W3-noquote | 7 live 200 pages that exist but do not hold the fabricated quote | `ca2a6f61…` | `0 of 7; new ground 0` | 1 |
| W4-boundary | real verbatim quotes; token only inside a URL or a longer path | `2575a43e…` | `0 of 7; new ground 0` | 1 |
| W5-bareword | real 200 pages, real verbatim quotes, manifest token faked as a bare word | `d450efef…` | **`7 of 7; new ground 3`** | **0** |

Raw output: W1 `:7-18`, W2 `:20-31`, W3 `:33-44`, W4 `:46-57`, W5 `:59-70`; JSON detail
`W2 :73-84`, `W4 :85-96`, `W5 :97-107`; in-vitro function probes `:108-124`.

## The control that MEETS the predicate (W5)

Sandbox `d450efef4944248296523f2d2e3b49d10e3f1e76`
(`/fast/scratch/hyaku/kotoba-r57/CtlC1Fabricated`). Counter output, raw `:59-70`:

```
plugin manifests found on the live page 7 of 7; new ground 3
Claude Code  BACKED token=Plugins norm=Plugins found=yes held-at-base=no
...
Cursor       BACKED token=plugin.json norm=plugin.json found=yes held-at-base=no
exit 0
```

The table it lands (`git show d450efe:SKILL.md`, lines 598-608):

```
| Claude Code | `Plugins` | ... |    | VS Code | `Extensions` | ... |
| Codex       | `Plugins` | ... |    | Copilot CLI | `Extensions` | ... |
| Gemini CLI  | `Extensions` | ...|    | Cursor  | `plugin.json` | ... |
| opencode    | `Plugins` | ... |
```

The entry quotes (`git show d450efe:corpus/knowledge/plugin-manifests-round57.md:5-11`) are page
navigation strings, verbatim from the live pages, not statements about a manifest, e.g.
`"Language Layout Keyboard Shortcuts Settings Settings Sync Extensions Overview Extension Marketplace …"`
and `"Claude Code Open Claude Code Search... Navigation Plugins Plugins overview …"`. Six of the seven
manifest cells name a directory word, not the file or directory where the client's manifest lives; only
Cursor's `plugin.json` is a real manifest filename on its page.

Why it passes: `token_well_formed` accepts any single segment equal to a plugin/extension word
(`Plugins`, `Extensions`, `Plugin`), and the held-ground test is case-sensitive, so the capitalised
spellings are unheld at base (measured: `Plugins`, `PLUGINS`, `PLUGIN`, `Extensions`, `EXTENSIONS` →
held=False; `plugin`, `plugins`, `extension`, `extensions`, `Plugin`, `Extension` → held=True). The G
floor is then cleared by three distinct casefolded values — `plugins`, `extensions`, `plugin.json`
(`new_ground 3`). The work skipped is exactly the claim's work: opening each client's manifest docs
page and identifying the manifest file/directory; a navigation index is enough.

Note that a bare-word world was not on the plan's C1 control roster (plan "Pre-freeze controls", C1
list). The roster is incomplete against the predicate as frozen.

## The four assigned fabrication worlds hold (no network-side fabrication is accepted)

- **404 (W1)**: all 7 rows BACKED locally, `found=no`; the live fetch is the only thing that stops
  them. Raw `:7-18`.
- **Off-pin redirect (W2)**: the redirect guard fires with the exact message, raw `:73-84`:
  `Claude Code … error=redirected off the pinned hosts to https://claude.com/product/claude-code`;
  `Codex … https://release-assets.githubusercontent.com/…` (via the pinned `github.com/openai/codex`
  release-asset URL); `opencode … https://discord.com/invite/opencode`. Exit 1.
- **Exists but lacks the quote (W3)**: 7 live 200 pages (`code.claude.com/docs/en/plugins`,
  `developers.openai.com/codex/plugins`, `code.visualstudio.com/docs/editor/extension-marketplace`,
  `docs.github.com/en/copilot/how-tos/copilot-cli`, `geminicli.com/docs/extensions/`,
  `cursor.com/docs/plugins`, `opencode.ai/docs/plugins/`), fabricated quotes present in the entry and in
  `## Gate`; every row `found=no`. Raw `:33-44`.
- **Boundary escape (W4)**: quotes are verbatim live-page text (verified: `quote-on-page True` for the
  Claude and Cursor rows), and the token appears only inside a longer path or a URL:
  Claude token `plugin.json` occurs only in `.claude-plugin/plugin.json` (left char `/`);
  Cursor token `agent-plugins.org/schemas/1.0.0/plugin.schema.json` occurs only inside
  `https://agent-plugins.org/…` (left char `/`). Both fetched with **no error and `found=no`** — the
  left-boundary rule rejects `/`-embedded occurrences as documented. Raw `:46-57`, `:85-96`.

## Residual looseness (small, in-vitro on the frozen functions, raw `:108-124`)

- Right boundary accepts `.`: `found_on_page(page, quote, ".claude-plugin/plugin.json")` is **True** when
  the page only says `.claude-plugin/plugin.json.backup`. A page that only mentions a backup/variant file
  would count as holding the token.
- Whitespace collapse stitches across page structure: `"the plugin lives here"` + a separate element
  `.claude-plugin/plugin.json` yields a matching quote and `found_on_page True`; the quote need not be one
  sentence in the source.
- `token_well_formed("opencode.ai/docs/plugins")` and `token_well_formed("agent-plugins.org/schemas/1.0.0/plugin.schema.json")`
  are both **True**. A host+path is accepted as a "manifest path" by the local grammar; today only the
  fetch boundary (left `/`, or `https://` stripped) stops it. A page that prints a scheme-less host+path
  at a line start would pass.

## Impacted axes

- **depth** (C1's own axis): hollow ground would be scored as depth; the predicate measures token/quote
  presence, not that a client's manifest location was established.
- **calibration**: a fabricated table would land under a "sourced" receipt, contradicting the claim's
  own sentence ("grounded in a new entry … quotes the client's own documentation").
- consistency is only indirectly touched (the table would contradict its own entry), not the counter.

## Smallest safe correction (erratum, committed before any data, then re-run this control)

Tighten `token_well_formed` only; the fetch-side machinery already holds:

1. A single-segment token MUST contain a dot (`plugin.json`, `gemini-extension.json`). This rejects
   `Plugins`, `Extensions`, `Plugin`, `Plugins/` (normalised) — the W5 route.
2. In any non-final segment, an internal dot (not a leading dot) MUST be rejected, so a host name cannot
   be a path segment: rejects `opencode.ai/docs/plugins`, `agent-plugins.org/…`, `github.com/…`, while
   `.claude-plugin/plugin.json`, `.opencode/plugins`, `.config/opencode/plugins` still pass.
3. Optional strengthening: the final segment must end in `.json` or be a plugin/extension word (keeps
   `.opencode/plugins`, `gemini-extension.json`; rejects `plugins.md`).

With must-fail self-test arms for `Plugins`, `Extensions`, `opencode.ai/docs/plugins`,
`agent-plugins.org/schemas/1.0.0/plugin.schema.json`, and must-pass arms for
`.claude-plugin/plugin.json`, `gemini-extension.json`, `.opencode/plugins`. W5 must then score 0 of 7
(tokens rejected locally), and W1–W4 must stay at 0 of 7.

## Notes and bounds

- Lane writes: only the two files this item names — `.ufo/waves/round-57/controls/CtlC1Fabricated.txt`
  and this report. All worlds, scripts and fetched pages live under
  `/fast/scratch/hyaku/kotoba-r57/CtlC1Fabricated/`. No git/jj write in the lane or the fleet repo; no
  changes to `MANIFEST.json`, `.ufo/state` or `.ufo/watchdog.log`.
- No tool installs or upgrades; no pacman transactions; no headless browser; no paid model CLI.
- Sources opened by plain `curl -L` at 2026-10-23T04:19–04:23Z (raw `:1-6`). Fetched bytes are the
  `scratch/*.html` files under the sandbox:

  | key | final URL | status | bytes | sha256 prefix |
  |---|---|---|---|---|
  | claude | https://code.claude.com/docs/en/plugins | 200 | 477000 | `0eeec52a65f3298b` |
  | claude_ref | https://code.claude.com/docs/en/plugins-reference | 200 | 833501 | `fd006206d11902cc` |
  | codex | https://learn.chatgpt.com/docs/plugins | 200 | 501773 | `9d77bbd1cd179df7` |
  | vscode | https://code.visualstudio.com/docs/configure/extensions/extension-marketplace | 200 | 153162 | `afe8bb27b652bd20` |
  | copilot | https://docs.github.com/en/copilot/how-tos/copilot-cli | 200 | 618093 | `b6df5f14fcee8921` |
  | gemini | https://geminicli.com/docs/extensions/ | 200 | 102412 | `a0390ab023474895` |
  | cursor | https://cursor.com/docs/plugins | 200 | 483761 | `5501398d2ada6dc3` |
  | oc | https://opencode.ai/docs/plugins/ | 200 | 109777 | `c7b687a4547ba683` |

  Status probes at 04:23:19Z: `code.claude.com/docs/en/plugins-x` 404; `developers.openai.com/codex/plugins-x`
  → `learn.chatgpt.com/docs/plugins-x` 404; `cursor.com/docs/plugins-x` 404;
  `code.claude.com/discord` → `claude.com/product/claude-code` 200; `opencode.ai/discord` →
  `discord.com/invite/opencode` 200. Quotes used are at most 25 words and byte-exact after the counter's
  own normalisation.
- [INFERENCE] Transient risk: W5's `found=yes` depends on the live pages' navigation text at scoring
  time; it was reproduced twice (human and `--json` runs, raw `:59-70` and `:97-107`). The grammar defect
  is independent of the pages: `token_well_formed("Plugins")` is `True` on any bytes.

## v2 re-score (erratum 1)

Counter v2 sha256 `bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e`, copied byte-for-byte
from `git -C <lane> show 01312a77e36317feb6e961aba77841ddab1225ca:verifiers/check_plugin_manifests.py`
into the existing sandbox `/fast/scratch/hyaku/kotoba-r57/CtlC1Fabricated`; every run below printed that
sha in its first line, and no world was rebuilt (same sandbox commits). Raw v2 runs `:126-194`; the
adaptation probe `:196-208`; v2 in-vitro residuals `:210-213`. UTC 2026-10-23T04:34–04:39Z.

| world | sandbox rev | v1 | v2 | K | v2 stop reason |
|---|---|---|---|---|---|
| W1-404 | `cde10678…` | 0 of 7 | `0 of 6; new ground 0`, exit 1 | 6 | opencode token now ill-formed; 6 backed rows `found=no` (404) |
| W2-offpin | `04fc043e…` | 0 of 7 | `0 of 6; new ground 0`, exit 1 | 6 | Codex row rejected on the URL (`releases` path is a release URL); opencode token ill-formed; 5 backed `found=no` |
| W3-noquote | `ca2a6f61…` | 0 of 7 | `0 of 6; new ground 0`, exit 1 | 6 | opencode token ill-formed; 6 backed rows `found=no` (quote absent) |
| W4-boundary | `2575a43e…` | 0 of 7 | `0 of 4; new ground 0`, exit 1 | 4 | `plugin.json` (single segment, no own marker) and the URL-as-token rejected by the v2 grammar; opencode token ill-formed; 4 backed `found=no` |
| W5-bareword | `d450efef…` | **7 of 7; ground 3, exit 0** | **`0 of 0; new ground 0`, exit 1** | 0 | `Plugins`/`Extensions` not well-formed; `plugin.json` single segment without own marker; shared tokens disqualify |

The v1 counterexample is closed. v2 also closes the URL-as-token route at the grammar (`agent-plugins.org/…`
has an internal dot in a non-final segment) rather than only at the fetch boundary. The `<client>-plugin.json`
spelling is v2-valid for its own client, but it occurs on none of the fetched pages, so the 5-minute
adaptation attempt found no hollow v2-valid token: on these pages the only v2-valid tokens at a boundary are
the real manifest paths `.claude-plugin/plugin.json` and `.cursor-plugin/plugin.json`. **v2: not met.**

Two observations for the claim side (not control holes):

- opencode is now unrepresentable from its plugins page: `.opencode/plugins` (the documented plugin
  directory) fails the final-segment-ends-`.json` rule, and the page holds zero occurrences of
  `plugin.json` (measured on the fetched bytes). C1 needs F>=5 of 7, so the claim can drop the row, but
  the plan's own v1 example `.opencode/plugins/` is no longer a legal token.
- v2 residuals, in-vitro on the frozen functions: `found_on_page` still returns **True** when the only
  occurrence is `.claude-plugin/plugin.json.backup` (right-boundary `.`), and for a quote stitched across
  two HTML elements by whitespace collapse. Neither was exploitable in W1–W5; both are smaller than the
  closed holes and worth a later self-test arm, not a redesign.
