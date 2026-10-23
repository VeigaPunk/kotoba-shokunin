Result: MIXED — the live page matches S080's recorded sha256 and the Gate quote is the two-break fold at lines 135–137; the candidate note is accurate, and the committed note does not say the quote ends mid-line 137.

No tool was installed or updated.

## Fetch

`date -u` (command start): `Fri 23 Oct 2026 06:45:37 AM UTC`

```
curl -sS -L -D headers.txt -o plugins.md -w 'http_code=%{http_code}\n...' \
  https://developers.openai.com/plugins/build/plugins.md
```

Observed: HTTP/2 200, `num_redirects=0`, `url_effective=https://developers.openai.com/plugins/build/plugins.md`, `content-type: text/markdown; charset=utf-8`, `content-disposition: inline; filename="plugins.md"`, `content-length: 38036`, `size_download=38036`, `wc -c` = 38036, sha256 `c37e330df8f040df8ee2f48035992b37c6a7decf6c3f5640822ca0907118c4e1`. Header `date: Fri, 23 Oct 2026 06:45:37 GMT`. Header `last-modified: Fri, 23 Oct 2026 05:01:31 GMT`. Body is LF-only (0 CR) and has no trailing newline (970 lines). Saved at `/fast/scratch/hyaku/kotoba-r57a3/A3ReopenS080/plugins.md` (scratch, not the lane).

Row at `07c33d73` (`corpus/SOURCES.md` S080; lesson Gate `corpus/lessons/round-57.md:15`): HTTP 200, 38,036 B, sha256 `c37e330df8f040df8ee2f48035992b37c6a7decf6c3f5640822ca0907118c4e1`, opened 2026-10-23T04:47:08Z. Byte count and sha256 match this re-open. The `last-modified` header is later than that open; the body hash is unchanged, so this re-open does not show a body edit.

`build-plugins.md` is the seat's save name (`SrcCodex.md` at `07c33d73`, the curl `-o` path), not the URL filename. The bytes and line numbers below are the URL body. The Gate location cell uses the same alias.

## Gate quote (shaped: two line breaks folded)

Lesson Gate quote (`corpus/lessons/round-57.md:15`) and the entry quote (`corpus/knowledge/plugin-manifests-round57.md:25`) are the same 22-word string (backticks kept; word count is backtick-stripped whitespace split, the rule at `verifiers/check_plugin_manifests.py:664-665`, reimplemented here, counter not executed):

"The plugin-creator skill will create the plugin folder, create a supported `.codex-plugin/plugin.json` compatibility manifest, and add MCP server wiring for the plugin."

Fetched bytes, verbatim:

- line 135: `The plugin-creator skill will create the plugin folder, create a supported`
- line 136: `` `.codex-plugin/plugin.json` compatibility manifest, and add MCP server wiring ``
- line 137: `for the plugin. If you ask it to create a personal marketplace entry, the` (73 characters; the period is index 14)

Joining line 135, a space, line 136, a space, and line 137 through that period equals the Gate quote (checked equal). The two U+000A bytes are each replaced by one U+0020. Nothing else is changed: backticks stay, there is no list marker, and the span is not inside the `text` fence at lines 64–74. Not in the quote: the 58 bytes on line 137 after the period, ` If you ask it to create a personal marketplace entry, the`.

Shaping class: folded line breaks only. Not stripped markup, not a fence info string, not a list marker.

Outside the token, `\b(?:plugins?|extensions?)\b` (the counter's `PLUGIN_WORD_RE`, `check_plugin_manifests.py:266`, applied to the backtick-stripped quote) hits `plugin-creator`, `plugin folder`, and `for the plugin`. Those three words are not on line 136. No single one of lines 135–137 holds both the token and an outside plugin/extension word.

## Unshaped quote of the same location

Yes. Same location means `.codex-plugin/plugin.json` as the compatibility manifest. These are one source line each, backticks kept, no fold, no omitted list marker, ≤25 words:

| line | words | outside plugin/extension word | text |
|---|---|---|---|
| 54 | 7 | no | `It scaffolds a supported `.codex-plugin/plugin.json` compatibility manifest` |
| 26 | 8 | no | `` `.codex-plugin/plugin.json` files remain supported as a compatibility fallback. `` |
| 949 | 8 | no | `` Legacy packages can declare `hooks` directly in `.codex-plugin/plugin.json`. `` |
| 76, first sentence | 5 | no | `` Only `.codex-plugin/plugin.json` is always created. `` |

Line 54 is the same claim as the Gate quote (a supported `.codex-plugin/plugin.json` compatibility manifest). The sentence continues on line 55 (`and can also generate a local marketplace entry for testing.`), which is not part of that line. Line 26 is the tail of the sentence whose subject `Existing` is the last word of line 25. Line 949 is a whole sentence on one line but states where legacy packages declare hooks, not the compatibility-manifest role. The line 76 sentence is under the counter's 6-word floor.

The only unshaped 6–25 word span on this page that also has a plugin/extension word outside the token is line 676 (9 words): `` `.codex-plugin/plugin.json`; the path still resolves from the plugin root. `` That does not state the manifest location. The full sentence (`plugins.md:674-676`) says to put `extensions.com.openai.onboardingSkill` in that file, and that the skill path resolves from the plugin root.

So an unshaped ≤25-word quote of the same manifest location exists (line 54), and Q42's replacement condition (`corpus/QUALITY.md:53`) is met for the fold. Replacing the Gate quote with line 54 would remove every plugin/extension word outside the token. [INFERENCE] The frozen counter would then reject the Codex row (`check_plugin_manifests.py:673-674`). I would not land that swap in the Quote cell. The folded quote is the one that both names the location and keeps an outside plugin word.

## Which note is accurate

Committed note at `07c33d73`, `corpus/knowledge/plugin-manifests-round57.md:32-33`:

`S080 `build-plugins.md:135-137` (line breaks folded to spaces)`

True, and incomplete. It does not say how many breaks, and `:135-137` without the mid-line cut can be read as all of line 137. The lesson note already says "two" (`corpus/lessons/round-57.md:24`: `S080 folds two line breaks`) and also does not say the quote ends at the period.

Candidate replacement (`a2-candidate.patch` quote-locations hunk; a claim, checked against the fetch, not treated as evidence):

`S080 `build-plugins.md:135-137` (two line breaks folded to spaces; the quote is the paragraph's first sentence, ending mid-line 137)`

Accurate. Two breaks, each folded to a space; the paragraph is lines 135–138; the first sentence ends at the period on line 137. I would land that sentence as the S080 clause, and no other change to this row's quote.

Old → new, S080 clause only:

- old: `` S080 `build-plugins.md:135-137` (line breaks folded to spaces) ``
- new: `` S080 `build-plugins.md:135-137` (two line breaks folded to spaces; the quote is the paragraph's first sentence, ending mid-line 137) ``
