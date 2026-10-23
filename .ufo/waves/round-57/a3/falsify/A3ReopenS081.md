Result: MIXED — live bytes match S081's recorded sha256, and the Gate quote is a verbatim 14-word middle sentence of line 97 (not Q42-shaped); the committed note names that line but not the span, and the candidate's S081 clause is the accurate one.

## Fetch

`date -u` → `Fri 23 Oct 2026 06:45:44 AM UTC`.

`curl -sS -D headers -o agent-plugin-reference.md -w 'http_code=%{http_code} size_download=%{size_download} url_effective=%{url_effective} num_redirects=%{num_redirects}' https://code.visualstudio.com/docs/agents/reference/agent-plugin-reference.md` → `http_code=200 size_download=21972 url_effective=https://code.visualstudio.com/docs/agents/reference/agent-plugin-reference.md num_redirects=0` (exit 0). Header `date: Fri, 23 Oct 2026 06:45:44 GMT`; `content-type: text/markdown; charset=UTF-8`; `content-length: 21972`; `last-modified: Thu, 22 Oct 2026 22:05:20 GMT`. `wc -c` → `21972`. `sha256sum` → `d6e10328d582db6210fcccc453947d8140ff08a41c31170c4c90816578a44f9e`.

Row at `07c33d73` `corpus/SOURCES.md:94`: HTTP 200, 21,972 B, sha256 `d6e10328d582db6210fcccc453947d8140ff08a41c31170c4c90816578a44f9e` (opened 2026-10-23T04:47:13Z). Byte count and sha256 match. No tools installed.

## Gate quote

`corpus/lessons/round-57.md:16`: "A root `plugin.json` that declares the canonical Agent Plugins `$schema` uses Agent Plugins semantics." (14 words).

In the fetched file (412 lines, trailing newline): line 97, 1-based columns 106–207 (102 bytes; `line[105:207] == quote`, file offset 5189). Byte-exact, backticks on `plugin.json` and `$schema` kept.

Line 97 is three sentences split on `. `:

1. "VS Code auto-detects the plugin format by checking the root manifest and format-specific manifest paths." (15 words) — not quoted.
2. The Gate quote, including its period.
3. "The Copilot format is used as the default when no other format marker is found." (15 words) — not quoted.

Not shaped under Q42. No folded line break (one line). No stripped markup. Not a fence (prose under `## Plugin formats`, line 95). No list marker omitted. The only cut is which sentence on the line is quoted.

## Unshaped quote of the same location

Yes. The Gate quote itself is already an unshaped ≤25-word statement of that location: a root `plugin.json` that declares the Agent Plugins `$schema`.

A whole-line alternative states the same place, with nothing else on the line left out. `agent-plugin-reference.md:47` (17 words), the entire line: "An Agent Plugins 1.0 package has a `plugin.json` file at its root that declares the standard's schema:" Same location: `plugin.json` at the package root for an Agent Plugins package that declares the schema. Not inside a fence. I would not replace the Gate quote. Q42 replaces a quote that needs shaping, and this one does not.

Weaker, not proposed: line 101 is a table row (pipes stay if the quote is unshaped) naming `plugin.json` plus the schema URL, but not the word "root". Line 102 names Copilot's `plugin.json`, the other format, not the schema-declaring case.

## Which note

Committed entry, `corpus/knowledge/plugin-manifests-round57.md:33`: `S081 `agent-plugin-reference.md:97``. The line is right. It does not say the quote is the middle sentence. It does not claim a shaping that did not happen.

Lesson, `corpus/lessons/round-57.md:22-24`: "S079, S081, S084 and S085 are one line each and unshaped (S084 is a contiguous substring: …)". "One line" and "unshaped" are true for S081. The parenthesis carves out only S084, which reads as if S081 were the whole line. That reading is false.

Candidate, `.ufo/waves/round-57/a3/a2-candidate.patch` (knowledge hunk, untrusted, checked here only for S081): `S081 `agent-plugin-reference.md:97`, the middle sentence of a three-sentence line`. Accurate. The patch's other row clauses and the sentence crediting attempt-2 residual seats were not re-opened.

## Text to land (S081 only)

Knowledge Quote locations, that clause:

old: `S081 `agent-plugin-reference.md:97``

new: `S081 `agent-plugin-reference.md:97`, the middle sentence of a three-sentence line (the sentence before it and the sentence after it are not quoted)`

Lesson Gate quote notes, S081 only (S079, S084, S085 not re-opened):

old: `S079, S081, S084 and S085 are one line each and unshaped (S084 is a contiguous substring:`

new: `S079, S084 and S085 are one line each and unshaped (S081 `agent-plugin-reference.md:97` is the middle sentence of a three-sentence line, with no line break, markup, fence info string, or list marker removed; S084 is a contiguous substring:`

Do not change the Gate quote or the sha256 cell.
