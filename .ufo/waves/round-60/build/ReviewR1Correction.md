Result: HOLDS — the recount reproduces in full from independently fetched bytes (25 at the token, 29 through line 97, page byte-stable over four fetches today), and the draft correction paragraph makes no claim beyond the verified evidence; four LOW/INFO nits, none touching the counts, the decision, or the paragraph's assertions.

Seat: `KotobaR60.ReviewR1Correction`, wave `build`, round 60 attempt 1. Reviewed artifact: `.ufo/waves/round-60/w0/ExecR1Recount.md`. Leaf: no subagents; only lane write is this report. Scratch: `/fast/scratch/hyaku/kotoba-r60/ReviewR1Correction/` (`hooks.md`, `hooks2.md`, `best-practices.md`). No tool installed or upgraded this run; all commands short (≤90 s timeouts), no lane or fleet git/jj writes.

## 1. Independent fetch

```
$ date -u
Fri 23 Oct 2026 12:09:17 PM UTC
$ curl -sSL -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36' -o hooks.md -w 'status=%{http_code} bytes=%{size_download}\n' https://geminicli.com/docs/hooks.md
status=200 bytes=8341
$ sha256sum hooks.md
a06a92438d3110690e875d61feef49a850d82eda618bb837146a1a7ff7a4c8d9  hooks.md
```

Second fetch 12:11:31 UTC: `status=200 bytes=8341`, same sha256, `cmp hooks.md hooks2.md` → exit 0. Identical to the executor's two fetches (10:29:31Z / 10:30:24Z, same sha) — four fetches today, one byte stream. `best-practices.md` at 12:11:31 UTC: `status=200 bytes=17650`, sha256 `fb44fbcfaccc3cdb7895d989f3808bed66cfa6516411535c4c4d9077d242e7bc` — equals the S100 record at `corpus/lessons/round-59.md:14` (17,650 B, `fb44fbcf…`).

## 2. Pipelines re-run on my bytes (all reproduce, exit 0)

```
$ grep -n 'Hooks are configured' hooks.md ; grep -n 'Project settings' hooks.md
94:Hooks are configured in `settings.json`. Gemini CLI merges configurations from
97:1.  **Project settings**: `.gemini/settings.json` in the current directory.
$ sed -n '94,97p' hooks.md | cat -A        # third line is `$` alone — line 96 empty
$ sed -n '94,97p' hooks.md | tr '\n' ' ' | sed -E 's/^.*Hooks/Hooks/; s/(`\.gemini\/settings\.json`).*/\1/' | wc -w
25
$ sed -n '94,97p' hooks.md | tr '\n' ' ' | sed -E 's/^.*Hooks/Hooks/; s/(\.gemini\/settings\.json`).*/\1/' | wc -w
25
$ sed -n '94,97p' hooks.md | wc -w
29
$ sed -n '94,97p' hooks.md | tr '\n' ' ' | sed -E 's/^.*Hooks/Hooks/' | wc -w
29
$ sed -n '94,97p' hooks.md | tr '\n' ' ' | sed -E 's/^.*(`\.gemini\/settings\.json`)//' | tr -s ' ' '\n' | grep -v '^$' | nl -ba
     1	in
     2	the
     3	current
     4	directory.
$ sed -n '97p' hooks.md | wc -w
8
```

Arithmetic check: the printed 25-word span ends at `` `.gemini/settings.json` `` (word 25; manual count confirms 1.–21. through `lowest):`, 22.–24. = `1.` `**Project` `settings**:`, 25 = the token); the full span is 29 words, so no earlier cut yields 29. The cut spans printed by my pipelines are byte-identical to §3 of `ExecR1Recount.md` (including the double spaces after `lowest):` and before `1.`).

## 3. Draft paragraph vs evidence — claim by claim

| Draft claim | Evidence | Verdict |
|---|---|---|
| `round-59.md` § Gate and `w0/CensusGeminiCLI.md:50` record the span as "29 words" | `corpus/lessons/round-59.md:27` "reject: 29 words, above the 25-word cap"; `CensusGeminiCLI.md:50` "29 whitespace-separated words from `Hooks` through the token" | verified |
| 29 is the count through the end of line 97 (`sed -n '94,97p' hooks.md \| wc -w` → 29) | reproduced: 29 | verified |
| tail past the token is "in the current directory." | reproduced: `in`/`the`/`current`/`directory.` | verified |
| cut at the token the span is 25 words, not 29 (command quoted) | reproduced: 25, both cut variants | verified |
| 2026-10-23T10:29:31Z, HTTP 200, 8,341 B, sha256 `a06a9243…` | executor's fetch record; my two fetches match byte-for-byte | verified |
| span needs folding across a blank line and a list item | line 96 empty (`cat -A`), line 97 starts `1.`; the 25-word span includes `1. **Project settings**:` | verified |
| the unshaped 10-word `best-practices.md:413` quote names the same token | `sed -n '413p'` = "When you open a project with hooks defined in `.gemini/settings.json`:", `\| wc -w` → 10; sha256 equals S100's | verified |
| reject stands on Q42, not on the cap | cap 6–25 inclusive is `plans/round-60.md:82` ("the quote is 6–25 words"); 25 is inside it, so the count alone no longer rejects; shaping ground is Q42 (`corpus/QUALITY.md:53`) | verified |

No overstatement found: the paragraph asserts only the two counts, their commands, the fetch identity of the page, the shaping reason, the replacement quote's existence, and the M85 rule.

## 4. Findings

- **LOW (F1) — the draft's counting command is inside a broken markdown code span.** Draft line 4 of the paragraph wraps the pipeline in single backticks while the pipeline itself contains backticks (`` (`\.gemini\/settings\.json`) ``). CommonMark closes the span at the first inner backtick, so the committed lesson would render the command garbled — precisely the bytes M85 requires to survive verbatim. Fix before integration: double-backtick delimiters (the content has only single-backtick runs), e.g. ``` ``sed -n '94,97p' hooks.md | tr '\n' ' ' | sed -E 's/^.*Hooks/Hooks/; s/(`\.gemini\/settings\.json`).*/\1/' | wc -w`` ```, or put the command on its own fenced line. Text unchanged.
- **LOW (F2) — report prose mis-cites the cap line.** `ExecR1Recount.md` §5 cites `plans/round-60.md:61` for the 6–25 cap; line 61 is A1 Scope-key text. The cap is at `plans/round-60.md:82` ("Backed iff: … the quote is 6–25 words"; grep `6[–-]25` → only :82). The draft paragraph itself does not cite the plan, so the integration is unaffected.
- **LOW (F3) — snapshot-range claim overstated.** §1 of `ExecR1Recount.md` says `.ufo/waves/round-59/snapshots/` holds `S096.page`–`S102.page`; `ls -l` shows `S096.page`–`S101.page` only (six files, no `S102.page`). Side claim only; the finding built on it (no committed `hooks.md` snapshot) stands.
- **INFO (F4) — "Six lines" miscount in report prose.** The fenced draft paragraph in §6 has 7 content lines, not 6. The paragraph's content is unaffected; the L1 should not copy the "Six lines" sentence anywhere.
- **INFO (F5) — "29 words" also propagates in round-59 dispatch provenance.** `.ufo/waves/round-59/build-dispatch.json:395`, `build-spec.json:52`, `build-taskcall-sent.json:27` say "(the hooks overview quote was 29 words)" in the `SrcGeminiCLI` prompt. These are immutable dispatch records, and the draft correctly limits itself to the two records the round-59 R1 routed (Gate + census); noted so a later reader does not take the dispatch prose as contradicting the correction.
- **INFO (F6) — the Q42 ground is stronger than the draft states.** `hooks.md:97` alone is an unshaped 8-word quote naming the token ("1.  **Project settings**: `.gemini/settings.json` in the current directory.", `wc -w` → 8), so the reject stands even under Q42's strict "unshaped quote from the same page" reading, not only via the 10-word best-practices quote. No draft change needed.

## 5. Residual risk and verification gaps

- The counts anchor to today's live bytes: no committed `hooks.md` snapshot exists in the lane (`find .ufo/waves/round-59 -iname '*hooks*'` → only `w0/ConnSiblingHooks.md`, `build/ScoutHookSecurity.md`; snapshots hold `S096.page`–`S101.page`). Four fetches today (two executor, two mine) are byte-identical, so the risk is time, not disagreement; the pasted commands re-derive the counts on any future bytes.
- The executor's residual claim "nothing else in the round-59 record claims a word count for this page" is false in the letter (F5: three dispatch JSONs) but the two scored records are the only ones a correction can amend; no gap remains in the correction's scope.
- Not re-verified (out of scope): the executor's §5 alternative-cut claim about `best-practices.md` being "the row's quote" (confirmed independently at `round-59.md:14`) and anything about round-60 C1 eligibility — this review covers the round-59 R1 recount only.

```
$ ls -l /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-60/build/ReviewR1Correction.md
-rw-r--r-- 1 vgpnk vgpnk 8216 Oct 23 09:15 /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-60/build/ReviewR1Correction.md
```
