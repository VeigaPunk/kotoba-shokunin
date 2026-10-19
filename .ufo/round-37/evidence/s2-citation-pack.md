# CommonMark citation pack -- code fences + list-item indentation

Scout seat S2, round 37.  Every quote is asserted character-for-character
against the pinned `spec.txt` (prose quotes against the WHOLE paragraph, so a
range can never truncate them; rule quotes against explicit ranges), and every
cited example number is verified against the published HTML by comparing the
example's markdown input.  Verification run: `python3 -B spec_cite.py` ->
`cite-verify.txt`, `PROSE_OK=True RULES_OK=True EXAMPLES_OK=True`.

## 0. Provenance and version identity

- **0.31.2** -- https://spec.commonmark.org/0.31.2/ -- `spec.txt` sha256 `257c41ad946f7a1414a499aca402a1aa8fdac3678532266611348c1cf54f4b80`, page sha256 `c85f56cc2101f761cc94215c677cd2c7c1ecca9c47be016479fdfe718af60f0d`
  - canonical source: `https://raw.githubusercontent.com/commonmark/commonmark-spec/0.31.2/spec.txt`
- **0.30** -- https://spec.commonmark.org/0.30/ -- `spec.txt` sha256 `b74aec17b162406c847fe0849aaee880c9bbba241e50e09ecb6664f13ce8a7a6`, page sha256 `ff53804c4e87e1a05efecfeebcf705e12c37b240515ec8ad845a1a6c16d63571`
  - canonical source: `https://raw.githubusercontent.com/commonmark/commonmark-spec/0.30/spec.txt`
- Section numbers are the same in both versions: **4.4** Indented code blocks,
  **4.5** Fenced code blocks, **5.2** List items, **5.3** Lists (line scan:
  `section-headings.txt`).
- **The cited sections' prose and examples are identical between 0.30 and
  0.31.2**, so a citation from one version holds verbatim in the other:
  every prose paragraph below was found verbatim in BOTH versions, 23/23 cited
  examples match their HTML input in the version cited, and the four sections'
  example bodies are byte-identical across versions (0 differing bodies;
  `prose-030-*.txt` vs `prose-0312-*.txt` differ only in three typos:
  "down side"->"downside", "characer"->"character", two dead URLs).
  The 0.30 line numbers are the 0.31.2 ones **+4** for these paragraphs.

## 1. Prose citations (paragraph ranges, both versions)

| # | shape it pins | 0.31.2 | 0.30 | first line |
|---|---|---|---|---|
| P1 | indented code = 4+ spaces | 1736-1742 | 1740-1746 | An [indented code block](@) is composed of one or more |
| P2 | indentation ambiguity: list item wins | 1759-1761 | 1763-1765 | If there is any ambiguity between an interpretation of ind |
| P3 | code fence definition | 1936-1940 | 1940-1944 | A [code fence](@) is a sequence |
| P4 | info string belongs to the opener | 1942-1948 | 1946-1952 | The line with the opening code fence may optionally contai |
| P5 | closer: same char, >= opener length | 1950-1957 | 1954-1961 | The content of the code block consists of all subsequent l |
| P6 | closer indent + unclosed fence | 1959-1967 | 1963-1971 | The closing code fence may be preceded by up to three spac _modulo: no real down side->no real downside_ |

Full quoted text of every paragraph is in `cite-verify.txt` (asserted); the
load-bearing sentences are:

- **P3**: "A code fence is a sequence of at least three consecutive backtick
  characters (`) or tildes (~).  (Tildes and backticks cannot be mixed.)" /
  "begins with a code fence, preceded by up to three spaces of indentation."
- **P4**: "If the [info string] comes after a backtick fence, it may not contain
  any backtick characters." -- the info string is a property of the OPENER.
- **P5**: "... a closing code fence of the same type as the code block began
  with (backticks or tildes), and with at least as many backticks or tildes as
  the opening code fence." -- same character AND length >= opener.
- **P6**: "The closing code fence may be preceded by up to three spaces of
  indentation, and may be followed only by spaces or tabs" / "If the end of
  the containing block (or document) is reached and no closing code fence has
  been found, the code block contains all of the lines after the opening code
  fence until the end of the containing block (or document)."
- **P1**: "each preceded by four or more spaces of indentation" -- indented
  code.
- **P2**: "If there is any ambiguity between an interpretation of indentation
  as a code block and as indicating that material belongs to a list item, the
  list item interpretation takes precedence" -- the decoy exception.

## 2. Numbered-rule citations (explicit ranges)

| rule | version | lines | what it pins |
|---|---|---|---|
| R1 list item, basic case (W + N) | 0.31.2 | 4113-4121 | |
| R2 item starting with indented code | 0.31.2 | 4423-4428 | |
| R3 rule #2's 6-space note | 0.31.2 | 4434-4436 | |
| R4 item starting with a blank line | 0.31.2 | 4579-4584 | |
| R5 rule #4 indentation tolerance | 0.31.2 | 4715-4719 | |
| R6 the symmetric rule #1 in 0.30 | 0.30 | 4117-4125 | |

R1/R6 are the same rule text in the two versions (the only difference is a
typo in the 0.30 copy: `of Ls*,` for `of *Ls*,`); R2/R3/R4/R5 are the 0.31.2
rules #2, #3, #4 that govern indented-code decoys inside list items.

## 3. Example citations (number verified against the published HTML)

| version | example | what it pins | anchor |
|---|---|---|---|
| 0.31.2 | 100 | indented code block (see also 107) | https://spec.commonmark.org/0.31.2/#example-100 |
| 0.31.2 | 107 | indented code block, 4+ spaces | https://spec.commonmark.org/0.31.2/#example-107 |
| 0.31.2 | 108 | indentation ambiguity: the list item wins | https://spec.commonmark.org/0.31.2/#example-108 |
| 0.31.2 | 110 | `    - one` is literal code text | https://spec.commonmark.org/0.31.2/#example-110 |
| 0.31.2 | 119 | simple backtick fence | https://spec.commonmark.org/0.31.2/#example-119 |
| 0.31.2 | 121 | fewer than three backticks is not a fence | https://spec.commonmark.org/0.31.2/#example-121 |
| 0.31.2 | 122 | closer must use the same character | https://spec.commonmark.org/0.31.2/#example-122 |
| 0.31.2 | 123 | closer must use the same character (mirror) | https://spec.commonmark.org/0.31.2/#example-123 |
| 0.31.2 | 124 | closer must be at least as long as the opener | https://spec.commonmark.org/0.31.2/#example-124 |
| 0.31.2 | 125 | closer >= opener length (tilde mirror) | https://spec.commonmark.org/0.31.2/#example-125 |
| 0.31.2 | 126 | unclosed fence: empty block | https://spec.commonmark.org/0.31.2/#example-126 |
| 0.31.2 | 127 | unclosed fence: no closer in the file | https://spec.commonmark.org/0.31.2/#example-127 |
| 0.31.2 | 128 | unclosed fence closed by the enclosing blockquote | https://spec.commonmark.org/0.31.2/#example-128 |
| 0.31.2 | 134 | four spaces of indentation is too many (not a fence) | https://spec.commonmark.org/0.31.2/#example-134 |
| 0.31.2 | 135 | closer indented <=3 spaces | https://spec.commonmark.org/0.31.2/#example-135 |
| 0.31.2 | 137 | a 4-space-indented closer is content | https://spec.commonmark.org/0.31.2/#example-137 |
| 0.31.2 | 145 | backtick info string cannot contain backticks | https://spec.commonmark.org/0.31.2/#example-145 |
| 0.31.2 | 146 | tilde info string may contain backticks/tildes | https://spec.commonmark.org/0.31.2/#example-146 |
| 0.31.2 | 147 | a closing fence cannot carry an info string | https://spec.commonmark.org/0.31.2/#example-147 |
| 0.31.2 | 253 | rule #1 worked example | https://spec.commonmark.org/0.31.2/#example-253 |
| 0.31.2 | 257 | continuation needs W+N; a 2-space line is indented code | https://spec.commonmark.org/0.31.2/#example-257 |
| 0.31.2 | 258 | continuation at W+N stays inside the item | https://spec.commonmark.org/0.31.2/#example-258 |
| 0.30 | 124 | 0.30 twin of the same-length rule | https://spec.commonmark.org/0.30/#example-124 |

## 4. Shape -> rule -> example

The machine-checkable form is `c3-shapes/` + `c3_matrix.py`; oracle verdicts
(cmark 0.31.2 and markdown-it-py 4.2.0, agreeing on all 18 label rows) are in
`matrix-head-blob.md` (before) and `matrix-live.md` (candidate).

| shape | rule | example | spec verdict |
|---|---|---|---|
| opener = 3+ backticks/tildes, <=3 spaces indent | P3 | 119, 121 | fence; 4+ spaces is indented code instead |
| info string on the opener only | P4 | 145, 146, 147 | a closer-shaped line carrying text is content |
| closer must share the opening character | P5 | 122, 123 | different-char fence line is content |
| closer length >= opener | P5 | 124, 125 | shorter fence line is content |
| closer <=3 spaces indent, nothing after it | P6 | 135, 137 | 4-space-indented closer is content |
| unclosed fence | P6 | 126, 127, 128 | content to the end of the containing block/document |
| indented code = 4+ spaces | P1 | 107, 110, 134 | literal text; never a box |
| ambiguity favours the list item | P2 | 108 | inside a list item, deeper indent is list content |
| continuation indent = W+N | R1 | 253, 257, 258 | a line short of W+N is not (necessarily) the item's |
| item whose first block is indented code | R2, R3 | rule #2 | needs 4 extra spaces beyond the item edge (6 in the example) |
| item starting with a blank line | R4 | rule #3 | allowed; W+1 for later lines |
| item may be indented <=3 spaces | R5 | rule #4 | same tolerance on every line |

## 5. Adjudication notes for the C3 builder (spec vs lane policy)

1. **Unclosed fence.** The spec makes it well-defined (P6: content to the end of
   the containing block or document -- example 128 shows a blockquote ending it).
   The lane's r35-D4 residual asks for a LOUD FAIL instead: that is a lane policy
   overlay, not a spec requirement, and it is the right call here, because a
   scanner that silently swallows every later box reads exactly like a file with
   no boxes.  Cite P6 + example 128 and state the policy explicitly.
2. **Indented-code decoys are context-dependent.** `    - [ ] x` at top level is
   literal code (P1, example 110); inside a list item the same shape may be list
   content (P2, example 108) or code needing 4 extra spaces (R2/R3). A flat,
   line-oriented scanner cannot decide this without a container model.  Named
   residual: the decoy class this round must either be scoped to the flat case
   (with the ambiguity documented) or explicitly deferred.
3. **Different-char fence line inside a block.** It is content (P5, examples
   122/123), and the live code already gets this right by comparing the first
   character -- but such a line is then NOT added to the opaque set, which
   matters for command-eligible shell blocks.

## 6. Oracle provenance

- `cmark --version` -> `cmark 0.31.2` (Arch `extra` package `cmark 0.31.2-1`,
  the reference C implementation, spec-version-matched to this pack).
- `uv run --with markdown-it-py python3 -c ...` -> `markdown-it-py 4.2.0`.
- Re-derive: `python3 -B c3_matrix.py head-blob` (before) / `... live` (candidate).

