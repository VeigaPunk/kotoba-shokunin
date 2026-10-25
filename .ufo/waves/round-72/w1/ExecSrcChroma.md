# ExecSrcChroma — source opened: staged S254 (Chroma, *Context Rot*)

## Verdict

**The source is reachable and every S254-sourced claim in the staged row and in
`context-rot-and-always-on-context.md` is confirmed at the page, except one sentence of the
entry that is the lane's own extrapolation (`confirmed-after-shaping`): the report measures
input length on NIAH/LongMemEval/repeated-words prompts and never measures an always-on
instruction file or agent turns (`grep -c -i 'always.on'` on the rendered snapshot → `0`;
`grep -c -i 'skill'` → `0`).** No claim is `absent` and none is `source-unreachable`. The
staged quote is a byte-exact substring of the fetched bytes. One operational note for the L1:
the staged URL **301s** to `https://www.trychroma.com/research/context-rot`, and no
markdown/raw export exists (three probes 404), so a recheck must follow the redirect or pin
the final URL.

Snapshot written (only committed-file-shaped write outside my build dir):
`.ufo/waves/round-72/snapshots/S254-chroma-context-rot.html` — 269 388 B, 595 lines,
`sha256 f49b06cbb703a7b6fbec4f10b36a17566196afb6c99b9d4e3f90ef03cf48e235`.

## 1. Fetch record (command and observed output)

```
$ S=$(mktemp -d /tmp/k72w1-ExecSrcChroma.XXXX); cd "$S"
$ curl -fsSL -A 'Mozilla/5.0' -w 'HTTP=%{http_code} FINAL=%{url_effective} SIZE=%{size_download} CT=%{content_type}\n' \
    https://research.trychroma.com/context-rot -o page.html
HTTP=200 FINAL=https://www.trychroma.com/research/context-rot SIZE=269388 CT=text/html; charset=utf-8
exit=0
$ sha256sum page.html
f49b06cbb703a7b6fbec4f10b36a17566196afb6c99b9d4e3f90ef03cf48e235  page.html
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-10-25T21:36:55Z
```

- Requested URL: `https://research.trychroma.com/context-rot` (the staged row's URL).
- Redirect observed (`curl -sSI`): `HTTP/2 301` … `location: https://www.trychroma.com/research/context-rot`
  (`server: Vercel`, `date: Sun, 25 Oct 2026 21:38:51 GMT`). With `-L`: `redirects=1 final=https://www.trychroma.com/research/context-rot`.
- Final URL: `https://www.trychroma.com/research/context-rot`; HTTP 200; `text/html; charset=utf-8`.
- Access date (UTC): **2026-10-25T21:36:55Z** (page's own date: `July 14, 2025`, snapshot line 10).
- Byte size: **269 388**; lines: **595**; sha256: **f49b06cb…f48e235** (above, full).
- Citation block in the page (snapshot lines 17–24) names the same URL family:
  `url = {https://trychroma.com/research/context-rot},` (line 23) — i.e. the no-`www` host the
  page itself prints, which is a third spelling; the canonical served path is the `www` one.

Machine copy of the same record: `.ufo/waves/round-72/w1/build/ExecSrcChroma/S254-fetch-log.json`.

## 2. Export form: no `.md`, no `.pdf`, no `.txt` — the quote lives in the rendered HTML

```
$ for u in https://research.trychroma.com/context-rot.md https://www.trychroma.com/research/context-rot.md \
           https://research.trychroma.com/context-rot/index.md; do curl -sS -A 'Mozilla/5.0' -o /dev/null \
           -w '%{http_code} %{size_download} %{url_effective}\n' -L "$u"; done
https://research.trychroma.com/context-rot.md      => 404 29205 https://www.trychroma.com/research/context-rot.md
https://www.trychroma.com/research/context-rot.md  => 404 29205 https://www.trychroma.com/research/context-rot.md
https://research.trychroma.com/context-rot/index.md=> 200 315501 https://www.trychroma.com/   (redirect to site root, not an export)
$ for u in …/context-rot.pdf …/context-rot.txt ; do … ; done
https://www.trychroma.com/research/context-rot.pdf => 404 29207 text/html; charset=utf-8
https://research.trychroma.com/context-rot.pdf     => 404 29207 text/html; charset=utf-8
https://research.trychroma.com/context-rot.txt     => 404 29207 text/html; charset=utf-8
```

So there is **no markdown/raw export**: the page is a Next.js SSR document whose article body is
already one element per line (line 15 is a 311-byte `<p>`). The quoted sentence lives in the
**rendered HTML**, `<p>` at line 15, and is duplicated verbatim inside the Next.js RSC payload on
line 595 (a 154 372-byte single line). `grep -n -o '<sentence>' page.html` → `15:` and `595:`.

## 3. Snapshot and the rendered twin

| file | what it is | bytes | lines | sha256 |
|---|---|---|---|---|
| `.ufo/waves/round-72/snapshots/S254-chroma-context-rot.html` | **fetched bytes, verbatim** (`cp` of the curl output) | 269 388 | 595 | `f49b06cbb703a7b6fbec4f10b36a17566196afb6c99b9d4e3f90ef03cf48e235` |
| `.ufo/waves/round-72/w1/build/ExecSrcChroma/S254-chroma-context-rot.rendered.txt` | **draft rendering** (not the snapshot): block tags → space, remaining tags removed, HTML entities unescaped, whitespace runs collapsed, **line numbering preserved from the HTML** | 201 115 | 595 | `ed072e5d228e6a325a55d28301473dd9428f323eb38e809879cab68aaf16be80` |

The rendering exists only because one quote (Q2 below) is **not contiguous in the raw HTML** —
markup splits the footnote marker. If the L1 wants a text-form snapshot for C1(d) it should copy
the rendering into `snapshots/` and pin the hash above; otherwise pin the HTML.

Machine copy of the located quotes: `.ufo/waves/round-72/w1/build/ExecSrcChroma/S254-located-quotes.json`.

## 4. Located quotes — every S254-sourced sentence in the row and the entry

Line numbers are snapshot lines; each quote is ≤25 words, pasted from `sed -n '<L>p'` of the
snapshot (HTML form) with the dropped bytes named. Word-bounded presence was checked by regex
`(?<!\w)…(?!\w)` over both files.

| # | claimed by | located | section | line | quote (≤25 words) | dropped bytes |
|---|---|---|---|---|---|---|
| Q1 | row quote cell **and** entry "The finding" (verbatim, in quotes) | **yes**, byte-exact substring | untitled summary paragraph before `Introduction#` (line 27) | 15 (also 595) | `model performance degrades as input length increases, often in surprising and non-uniform ways` (13 w) | leading `<p>` + clause `We demonstrate that even under these minimal conditions, `; trailing sentence `Real-world applications … in practice.` + `</p>` |
| Q2 | row: "also the LongMemEval and repeated-word tasks"; entry: "LongMemEval items plus a synthetic repeated-word task" | **yes, rendered form only** | untitled task-list paragraph | 14 (also 595) | `a conversational question-answer evaluation using LongMemEval [2], as well as a synthetic task in which models replicate a series of repeated words` (23 w) | leading `<p>Additionally, we include `; inline `<a …>2</a>` link markup (this is why the string is **not** contiguous in the HTML); trailing `Each task … alone.` + `</p>` |
| Q3 | entry: "the report notes that real applications carry far more complexity, so the effect is likely stronger in practice" | **yes** (entry is a paraphrase) | same summary paragraph | 15 (also 595) | `Real-world applications typically involve much greater complexity, implying that the influence of input length may be even more pronounced in practice` (21 w) | prefix `<p>We demonstrate … ways. ` and `</p>` |
| Q4 | entry: "Deliberately simple tasks, deliberately controlled, and degradation still appears" | **yes** | untitled task-list paragraph | 14 (also 595) | `Each task remains intentionally simple and is deliberately controlled to isolate the impact of context length alone` (17 w) | prefix through `… repeated words. ` and `</p>` |
| Q5 | row scope: effect stronger in practice; entry's "likely stronger in practice" | **yes** | `Limitations & Future Work` (line 468) | 469 (also 595) | `we would expect performance degradation to be even more severe under those conditions` (13 w) | `<p>` + three preceding sentences (`Our experiments … multi-step reasoning.`); trailing `</p>` |
| Q6 | entry front matter: "Hong, Troynikov and Huber (Chroma), 2025" | **yes** | BibTeX citation block | 19 (also 595) | whole line, 8 content words: `<span class="line"><span>  author = {Hong, Kelly and Troynikov, Anton and Huber, Jeff},</span></span>` | two `<span …>` wrappers and the BibTeX `author = {` / `},` syntax |
| Q7 | freshness: the page's own date | **yes** | masthead | 10 (also 595) | `July 14, 2025` (3 w) | the rest of line 10 is site chrome (nav, `Pricing`, `Log in`, title) and the `<p>` wrapper; `Chroma Technical Report` precedes it in the same line |
| Q8 | row scope: "models of its vintage"; entry: nothing numeric | **yes** | meta description (line 3) and Contributions bullet (line 35) | 3 (also 6, 9, 10, 595) | `we evaluate 18 LLMs` (4 w) | meta-tag attributes on line 3; line 35's variant is `An evaluation across 18 LLMs, including leading closed-source and open-weights models, revealing nonuniform performance with increasing input length` (18 w) |

Section headings observed in the article body (`<h1>`/`<h2>` with line numbers), for the L1's
`## Gate` record: `Introduction#` 27, `Contributions#` 31, `Related Work#` 45,
`Needle in a Haystack Extension#` 52, `Needle-Question Similarity#` 76/112, `Impact of
Distractors#` 78/169, `Needle-Haystack Similarity#` 86/214, `Haystack Structure#` 88/228,
`LongMemEval#` **245**, `Repeated Words#` **286**, `Limitations & Future Work#` **468**,
`Conclusion#` 473, `Footnotes#` 476, `References#` 481, `Appendix#` 512, `Models Tested#` 533.

## 5. Verdict per claim in the entry `context-rot-and-always-on-context.md`

Source for every row: the snapshot above. `[INFERENCE]` marks my own reading, not a page sentence.

| claim (entry) | verdict | evidence |
|---|---|---|
| Title/lead: "input length degrades quality, non-uniformly" | **confirmed** | Q1 at line 15; also line 35 "revealing nonuniform performance with increasing input length" |
| "Chroma's report isolates input length on controlled tasks — LongMemEval items plus a synthetic repeated-word task" | **confirmed** | Q2 (line 14) + Q4 (line 14: "deliberately controlled to isolate the impact of context length alone") + section headings `LongMemEval#` 245, `Repeated Words#` 286 |
| Quoted sentence "model performance degrades … non-uniform ways" | **confirmed**, byte-exact substring of the fetched bytes (line 15) | Q1 |
| "Deliberately simple tasks, deliberately controlled, and degradation still appears" | **confirmed** | Q4 + Q1 ("even under these minimal conditions") |
| "the report notes that real applications carry far more complexity, so the effect is likely stronger in practice" | **confirmed** (paraphrase; verbatim sentence is Q3 at line 15, restated at Q5 in `Limitations & Future Work`) | Q3, Q5 |
| Front matter "Hong, Troynikov and Huber (Chroma), 2025" | **confirmed** | Q6 (line 19) and line 20 `year = {2025},`, line 22 `institution = {Chroma},` |
| Front matter "the report's own summary and task list" | **confirmed** | the summary is Q1 (line 15); the task list is Q2 (line 14) — both in the pre-`Introduction` block, not in a section |
| Front matter "retrieved 2026-10-23" | **not verifiable by this seat** (the package's own access date; I observed the live page on 2026-10-25T21:36:55Z). Stated, not contested. | — |
| "Chroma's report says that the always-on strategy's cost is not a constant but a **degradation curve** — and not a smooth one, so the safe size of an always-on block cannot be computed by multiplying a token cost" | **confirmed-after-shaping** | The page's own object is *input length*, never an always-on file: `grep -c -i 'always.on'` on the rendered snapshot → `0`; `grep -c -i 'skill'` → `0`; `agent` occurs twice, both as motivation (line 29 "Real applications, such as agent tasks or summarization, demand significantly more processin…"; line 113). "Not a smooth one" is the page's "non-uniform"; "cannot be computed by multiplying a token cost" is the lane's inference, not a page sentence. The report's own scope caveat is Q5's preceding sentence: "this evaluation is not exhaustive of real-world use cases." |
| "the effect is likely stronger in practice" used as a *cost* argument for always-on context | **confirmed-after-shaping** | Q3/Q5 say "may be even more pronounced" / "we would expect … even more severe" — hedged predictions about long-context applications generally, not a measurement of an always-on instruction block. |
| "Compression and progressive disclosure are the escape from both" / "keep a pointer resident and the payload retrievable" | **absent from this source** (lane synthesis; the page's nearest sentence is the Conclusion, line 475: "what matters more is how that information is presented") | [INFERENCE] this is the entry's own craft rule and must not be attributed to S254 |

**Nothing in the entry is `fabricated`**: every S254-attributed sentence either is a verbatim
page sentence or a shaping of one, and the one extrapolation is named above.

## 6. URL host+path (for lane duplicate detection) and the lane's own state

- Requested: `research.trychroma.com/context-rot` → **301** → served: `www.trychroma.com/research/context-rot`.
- Page's own citation prints a third spelling: `trychroma.com/research/context-rot` (line 23).
  A duplicate check should normalise `research.` → `www.` and treat the bare-apex form as the same page.
- **Lane holds the URL nowhere as a registry row.** `grep -c '^| S[0-9]' corpus/SOURCES.md` → `139`
  rows; `grep -rn 'trychroma\|research/context-rot' --include=*.md --include=*.json --include=*.sh .`
  (excluding `.ufo/waves/round-72`) hits only `plans/round-72.md:190` (the plan's own text). The
  phrase `Chroma — Context Rot technical report.` appears twice, both inside a
  `## Leads (unopened)` list (`corpus/SOURCES.md:245` under the list opened at `:232`, and
  `corpus/SOURCES.md:287` under a second list opened at `:274`) — an unopened lead with no URL and
  no S id, so appending S254 is **not** a duplicate; it closes a lead the lane has carried.
- `[INFERENCE]` the two `## Leads (unopened)` sections at `:232` and `:274` are themselves a
  possible duplication defect in the lane file — flagged for the L1, not acted on here.

## 7. Consequences for wave 1 (facts the L1 can use, no claim made)

1. **C1/A4 scope:** S254 is a *capability measurement* (degradation curve over input length). If
   `resident-index-and-rungs-round72.md` cites it, the citation is pointer-only at most; the
   PROVINCE question is `ConnScopeSiblings`' and `kengaku`'s. My snapshot does not settle that.
2. **Row drafting (for `ExecIdNormalize`/the L1):** the staged row's quote cell is accurate as
   written; a fleet-schema `quote` cell of ≤25 words can be Q1 verbatim, and the `recheck` cell
   should say the URL 301s to the `www` path (otherwise a recheck that greps the staged host will
   look like drift).
3. **Snapshot pin text** (round-70 style, for an entry `source:` line):
   `source: S254 — https://www.trychroma.com/research/context-rot — 269 388 B / sha256 f49b06cb… — Hong, Troynikov and Huber (Chroma), 2025-07-14 — retrieved 2026-10-25`.

## 8. Method, bounds, cleanup

- Read-only against the lane: I opened `plans/round-72.md`, the staged row
  (`SOURCES.append.md:58`), the staged entry, and `corpus/SOURCES.md`; I wrote **only**
  `snapshots/S254-chroma-context-rot.html`, `w1/build/ExecSrcChroma/*` and this report. No git
  write, no jj call, no gate run (wave 1 is in flight; the L1 owns post-integration gates).
- No tool installs or upgrades this wave (nothing needed).
- Scratch `/tmp/k72w1-ExecSrcChroma.aX7V` removed before returning.
- No credential material, session URL or `op://` reference was read or written.
