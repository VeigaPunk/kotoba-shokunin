# How snapshot.md was produced (shaping declared)

Input: `raw-cli-skills.html` (the fetched 217520-byte response, sha256 in `snapshot.sha256`).
Script: BeautifulSoup(html.parser) over `div.vp-doc`; blocks mapped to markdown
(`h1`–`h6` → `#`; `pre` → fenced block, content verbatim; `ul`/`ol` → `-`/`n.`; `table` → pipe table;
inline `code` → backticks; `strong` → `**…**`).

Two deliberate transformations, both named here because they mean snapshot.md is *not* byte-exact to the HTML:
1. Whitespace inside an inline text node is collapsed to a single space (`[ \t]+` → ` `). English/Chinese
   prose only; fenced code blocks are untouched. Rendered HTML collapses the same runs, so no word moves.
2. VitePress's heading anchor links are kept as they render: each heading ends with `[​](#anchor)` where the
   bracket holds U+200B ZERO WIDTH SPACE. Quotes therefore never span a heading tail.

Nothing else is added or removed: no sentence, table row or code block was dropped, reordered or truncated.

Consequence for C1 predicate (d) — "found in its snapshot after whitespace collapse only": the located quote
below is a contiguous literal substring of a single snapshot line (line 661-662 with the newline between two
adjacent bullets collapsed), so it is found with `re.sub(r'\s+',' ',…)` and no other shaping.
