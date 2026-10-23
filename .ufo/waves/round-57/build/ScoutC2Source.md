Result: DONE — both specs were fetched and quoted byte-exactly, but the target URL `https://spec.commonmark.org/0.31.2/` is **already** SOURCES row S005 (`corpus/SOURCES.md:18`, status `queued`, teaches has no language rule), so S086 cannot be minted on that URL; the free-URL row drafted below is the GFM spec, and the CommonMark half needs an S005 amendment instead. Neither spec states "a fence with no info string declares no language"; both state only that the info string's first word is *typically* the language, and both explicitly decline to mandate renderer treatment of the info string.

# Fetch ledger (all four URLs opened by curl this round; no freshness claim made)

`date -u` before and after each fetch; `curl -sS [-L] -o <file> -w 'status=%{http_code} bytes=%{size_download} url=%{url_effective}'`. Scratch dir `/fast/scratch/hyaku/kotoba-r57/ScoutC2Source` (bounds-compliant). No installs or upgrades were performed.

| # | URL | fetched (`date -u`) | status | bytes | sha256 |
|---|---|---|---|---|---|
| 1 | https://spec.commonmark.org/0.31.2/ (HTML, the S005 URL) | start `Fri 23 Oct 2026 04:46:46 AM UTC`, end `04:46:47 AM UTC` | 200 | 514,698 | `c85f56cc2101f761cc94215c677cd2c7c1ecca9c47be016479fdfe718af60f0d` |
| 2 | https://spec.commonmark.org/0.31.2/spec.txt (plain source) | start `Fri 23 Oct 2026 04:47:00 AM UTC`, end `04:47:01 AM UTC` | 200 | 204,857 (9,748 lines) | `bfef4ddc97276b6ab6c2a28ace48478e35b1c50e60cde9f517ab8ab030aa3b82` |
| 3 | https://github.github.com/gfm/ (HTML, §4.5) | start `Fri 23 Oct 2026 04:46:54 AM UTC`, end `04:46:55 AM UTC` | 200 | 508,310 | `b153d814fdfc8624bb6da7449162c1cd707a637f7d1c1b636eb44b9cf63fa220` |
| 4 | https://github.github.com/gfm/spec.txt (plain-source attempt) | `Fri 23 Oct 2026 04:47:01 AM UTC` | **404** | 9,379 | `b620507312c5e97566a3c6cfaf99144fefc18a0da7d941401dfa0f5f58fb0368` |

Command forms actually run (exit 0 each; the 404 is a status field, not a curl failure):
```
curl -sS -o cm0312.html -w 'status=%{http_code} bytes=%{size_download} url=%{url_effective}\n' https://spec.commonmark.org/0.31.2/
curl -sS -o cm0312-spec.txt ... https://spec.commonmark.org/0.31.2/spec.txt
curl -sS -L -o gfm.html ... https://github.github.com/gfm/
curl -sS -o gfm-spec.txt ... https://github.github.com/gfm/spec.txt
```
Version identity: CommonMark page declares `Version 0.31.2 (2024-01-28)` at `cm0312.html:117`; GFM page declares `Version 0.29-gfm (2019-04-06)` at `gfm.html:119`. [INFERENCE] from that label, GFM's §4.5 tracks CommonMark 0.29, not 0.31.2 — its §4.5 prose differs from 0.31.2 in three places (see "Wording differences" below), none of which touch the info-string/language sentence.

**Byte-identity observation (not a freshness claim):** the CommonMark page sha256 `c85f56cc2101f761…` matches the sha256 recorded for S005 in `corpus/lessons/round-46.md:67` on 2026-10-19T18:40:53Z. The bytes have not moved between the two openings.

# The duplicate that blocks S086-as-specified

```
$ grep -n commonmark corpus/SOURCES.md
18:| S005 | CommonMark Spec 0.31.2 — https://spec.commonmark.org/0.31.2/ | spec | A | ... | queued | 2026-10-19 | on-release | — |
```
`grep -n -i "gfm\|github.github.com" corpus/SOURCES.md` → no hits. So:
- The **CommonMark 0.31.2 URL is taken** by S005. Minting S086 on that URL would create a second row for one page, which the SOURCES preamble forbids in spirit ("A row exists only for a source the row's author opened this round") and which the C1 lane's own source bookkeeping would double-count.
- The **GFM URL is free**; a GFM row can be S086 without collision. Current id space at lane HEAD `01312a77`: S001-S078 only (`grep -c "^| S0" corpus/SOURCES.md` → 78), so S079-S085 are still reserved for the C1 client seats and S086 lands after them.
- S005's `teaches` cell says nothing about the info string's role in naming a language, and S005 is still `queued` with `used-by` `—`, while the lane's own instrument already cites the section by name: `verifiers/verify_skill_checklist.py:340`, `:738`, `:781` ("Delimiters follow CommonMark 0.31.2 § Fenced code blocks"). A citation without a mined row is the corpus gap to close; the language sentence is the missing clause.

# The quote (byte-exact, identical bytes in both specs)

Target phrase, 17 words, no markdown bytes to strip, spanning one line break:

> the info string, the first word is typically used to specify
> the language of the code block.

- `cm0312-spec.txt:2275-2276` (CommonMark 0.31.2, inside §4.5; the section's `<h2 id="fenced-code-blocks">` is at `cm0312.html:2726`)
- `gfm.html:2697-2698` (GFM §4.5; the section's `<h2 id="fenced-code-blocks">` is at `gfm.html:2229`)
- The exact 125 bytes of those two lines hash identically in both files:
```
$ sed -n '2275,2276p' cm0312-spec.txt | sha256sum   → 146d9eb5491d7052b999c51ab252bcb13d6fa8c1bc4e0a1597fe5e0077228925
$ sed -n '2697,2698p' gfm.html      | sha256sum   → 146d9eb5491d7052b999c51ab252bcb13d6fa8c1bc4e0a1597fe5e0077228925
$ diff <(sed -n '2275,2276p' cm0312-spec.txt) <(sed -n '2697,2698p' gfm.html)  → no output
```
The quote is a clause of a longer sentence: it begins after "Although this spec doesn't mandate any particular treatment of" (`cm0312-spec.txt:2274`; GFM spells the apostrophe U+2019: `doesn’t` at `gfm.html:2696`) and it stops before the following " In HTML output, …" on the second line. The opening clause matters, because the sentence's force is to *decline* to mandate — the quoted clause alone must not be read as a requirement on renderers.

Supporting quotes, each ≤25 words:

| # | exact bytes | where | words |
|---|---|---|---|
| A | `The line with the opening code fence may optionally contain some text following the code fence` | `cm0312-spec.txt:1934-1935`; GFM equivalent at `gfm.html:2237-2239` with "whitespace" at `:2239` where 0.31.2 says "spaces or tabs" at `:1936` — proves the info string is **optional** | 16 |
| B | `The first word of the [info string] is typically used to specify the language of the code sample` | `cm0312-spec.txt:1965-1966`; strip exactly 2 bytes `[` `]` around `info string` → 18 words; GFM equivalent `gfm.html:2264-2265` has `<a href="#info-string">info string</a>` instead (strip the 2 tags) | 18 |
| C | `However, this spec does not mandate any particular treatment of the [info string].` | `cm0312-spec.txt:1967-1968` (strip 2 bytes `[` `]`); GFM `gfm.html:2266-2267` carries `<a href="#info-string">…</a>` (strip 2 tags) | 13 |
| D | `Note that not every feature of the HTML samples is mandated by the spec.` | `cm0312-spec.txt:265-266` — CommonMark only; **GFM has no such sentence** (`grep -n "not every feature" gfm.html` → no hits) | 14 |
| E | `In HTML output, the language is normally indicated by adding a class to the code element consisting of language- followed by the language name.` | `cm0312-spec.txt:2276-2278` (strip 4 backtick bytes: `` `code` ``, `` `language-` ``); GFM `gfm.html:2698-2700` uses `<code>code</code>` and `<code>language-</code>` (strip those 4 tags) | 24 |

# Answer to the second question: what the specs say about renderers and an info-less block

**Nothing specific.** Neither spec contains a sentence about a fence with no info string; the phrase set `no language`, `without an info`, `empty info`, `no info` returns zero hits in `cm0312-spec.txt` (`grep -n -i "no language\|without an info\|absent\|no info" cm0312-spec.txt` → exit 1, no output). What exists instead:

1. **The info string is optional** (quote A) — but "optional" is a permission, not an assertion that absent means no language.
2. **The first word of the info string is typically the language**, "and rendered in the `class` attribute of the `code` tag", and that sentence ends by refusing to constrain implementers (quote C).
3. **The expected HTML for an info-less fence carries no class attribute**, shown only as a test example, never as prose:
   - CommonMark Example 119: markdown at `cm0312-spec.txt:1973-1976` (three-backtick fence with no info string), expected output at `:1978-1980` = `<pre><code>&lt;` / ` &gt;` / `</code></pre>`.
   - GFM Example 89: `gfm.html:2269-2284`; the expected-document cell escapes to `<pre><code>` with no class (`gfm.html:2281-2283`).
4. **CommonMark then says the examples are not binding on renderers** (quote D): "not every feature of the HTML samples is mandated by the spec". GFM lacks that sentence and instead states the HTML convention softly (quote E: "normally indicated by adding a class … `language-` followed by the language name") — a convention that presupposes a language is present.

**Therefore the claim "a fence with no info string declares no language" is not in either spec.** What the specs support, verbatim, is: the info string may be absent, and if present its first word is *typically* the language. The step from "no info string" to "no language declared" is [INFERENCE] — a sound one for the specs' own HTML output (the example has no class), but written nowhere, and explicitly unmandated for renderers. Any lane rule keyed on `info_string == ""` is a **host convention**, which the spec neither licenses nor forbids. That is the whole of what this source can settle for a later C2 round.

Wording differences between the two files in §4.5 (none in the quoted sentence, all recorded so a later seat does not treat them as errors): GFM says the fence begins "indented no more than three spaces" (`gfm.html:2236`) where 0.31.2 says "preceded by up to three spaces of indentation" (`cm0312-spec.txt:1932`); GFM trims "leading and trailing whitespace" (`:2238`) where 0.31.2 trims "spaces or tabs" (`:1936`); GFM's closer may be "followed only by spaces" (`gfm.html:2253`) where 0.31.2 allows "spaces or tabs" (`:1951-1952`).

# Operability: where the premise is already load-bearing in the lane (evidence only, no fix sketched)

- `verifiers/verify_skill_checklist.py:131-133`: command subjects are fenced blocks whose "info string (first whitespace token, lowercased)" is in `{"", bash, sh, shell, console}` — the empty info string is treated as **shell-bearing**, i.e. the instrument assumes `""` means "run this", the opposite direction from "declares no language".
- `verifiers/verify_skill_checklist.py:781-783`: same rule restated in `fenced_regions`' docstring; `:340-341` and `:738` cite "CommonMark 0.31.2 § Fenced code blocks" for the delimiter rules.
- So the lane's `""`-as-shell rule is a **lane convention**; S086/S005 can support "the info string is optional and typically names the language", and cannot support either "no language" or "must be shell". A later C2 redesign that leans on the spec for this needs the convention stated as the lane's own, not as spec text.
- `verifiers/check_infoless_fences.py:30` already encodes the class distinction verbatim: "PASS-expected (fence has NO info string; besides the class lines it holds …)" — consistent with the withdrawn claim's framing, not with the spec's silence.

# Draft SOURCES row (exact 11-column shape of `corpus/SOURCES.md`, one line)

Header verified: `| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |` (`corpus/SOURCES.md:12-13`). Draft for the free GFM URL:

```
| S086 | GitHub Flavored Markdown Spec — https://github.github.com/gfm/ | spec | A | What §4.5 says about a fence's info string and the language it names, and what either spec says about renderer treatment of an info-less fence (C2 redesign evidence, not a C2 fix) | §4.5 Fenced code blocks, h2 at `gfm.html:2229`, prose at `:2264-2267` and `:2695-2700`, info-less Example 89 at `:2269-2284`; Version 0.29-gfm (2019-04-06) at `:119`; fetched 2026-10-23T04:46:54Z, HTTP 200, 508,310 B, sha256 `b153d814fdfc8624bb6da7449162c1cd707a637f7d1c1b636eb44b9cf63fa220`; plain-text route /gfm/spec.txt is 404 (9,379 B, sha256 `b6205073…`); quote `the info string, the first word is typically used to specify the language of the code block.` at `:2697-2698` (125 B, sha256 `146d9eb5491d7052b999c51ab252bcb13d6fa8c1bc4e0a1597fe5e0077228925`, byte-identical to `spec.commonmark.org/0.31.2/spec.txt:2275-2276`) | The info string is optional and its first word is "typically used to specify the language of the code block", but the spec "doesn't mandate any particular treatment of the info string" and nowhere states that a fence with no info string declares no language — the info-less case appears only as Example 89's expected output `<pre><code>` with no class attribute | mined | 2026-10-23 | on-release | .ufo/waves/round-57/build/ScoutC2Source.md |
```

If the L1 prefers to hold one CommonMark-family row instead of two, the alternative is to mine S005 (no new URL) by amending its `teaches` and evidence cells — exact replacement text for `corpus/SOURCES.md:18`:

```
| S005 | CommonMark Spec 0.31.2 — https://spec.commonmark.org/0.31.2/ | spec | A | Fenced code block syntax the lane's box/quote extraction implements, and what the info string does and does not declare | § Fenced code blocks; version 0.31.2 (`div.version`, line 117 of the page fetched from https://spec.commonmark.org/0.31.2/); re-fetched 2026-10-23T04:46:46Z, HTTP 200, 514,698 B, sha256 `c85f56cc2101f761…` byte-identical to the 2026-10-19 fetch (`corpus/lessons/round-46.md:67`); plain source `spec.txt` (200, 204,857 B, sha256 `bfef4ddc…`) prose at `:1934-1936`, `:1964-1968`, `:2273-2278`; info-less Example 119 at `:1972-1981`; quote `the info string, the first word is typically used to specify the language of the code block.` at `spec.txt:2275-2276` | A code fence is at least three backticks or tildes preceded by up to three spaces of indentation; a backtick fence's info string may not contain a backtick; the info string itself is optional, its first word is typically the language, and the spec does not mandate any treatment of it | mined | 2026-10-19 | on-release | .ufo/waves/round-57/build/ScoutC2Source.md |
```

Either way, the sentence must not be restated as "a fence with no info string declares no language" in the row's `teaches`; that sentence is the scout's inference, not the source's.

# Remaining unknowns

- Whether the `0.31.2` HTML page and `/0.31.2/spec.txt` are generated from the same `spec.txt` this round: the sentences match byte-for-byte in both representations at the quoted span; no generation proof was taken.
- GFM's plain-text source is not served at `/gfm/spec.txt` (404). The HTML is therefore the only fetched representation for GFM; any later seat re-quoting GFM must strip tags and say which ones, as done in quotes B/C/E.
- Whether any client or lane host documents a convention that an info-less fence is shell: not checked here (out of scope; this seat's question was the two specs).
- S079-S085 were not present in `corpus/SOURCES.md` at HEAD `01312a77` (`grep -c "^| S0"` → 78), so S086's final number depends on the C1 seats landing first.
