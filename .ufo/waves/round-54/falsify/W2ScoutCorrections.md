# W2 — scout, corrections (S060, S061, § Rows touched, S046 diff, census)

Result: MIXED — S060 and S061 hold on substance (bytes reproduce, every quote is verbatim,
no teaches cell is wider than its evidence, S046 changed only in `used-by`, the census exits 0),
but two contract-form breaks remain: S060's `teaches` does not open with rule 2's literal
`supersedes S0NN —`, and S060's lesson § Gate row records no URL (rule 1).

Scope: the two correction rows at `5a097e12b9409a1f425fbc76334f36f1402eb4cc` (also unchanged at
tip `58db81c4465b0e9b07ef2485b87d8970683afac6`), `corpus/lessons/round-54.md` § Rows touched and
§ Gate rows for them, S046's in-place diff from `422ffd1082b3f4ae3ebda6060eb1a8d779f6dfd4`, and
`scripts/sources-census.sh validate`. Lane files were read only; nothing in the lane was written
except this report. All executing work ran in `/fast/scratch/hyaku/kotoba-r54/` (clone at tip:
`W2ScoutCorrections`; base clone `base422`; mutation copies `mutA`, `mutB`). No tools installed.

## Fetch record (ordinary curl, no browser)

| URL | UTC | HTTP | bytes | sha256 |
|---|---|---|---|---|
| https://raw.githubusercontent.com/google-gemini/gemini-cli/451a02ff03f1d2a8fe870c120fd5342cfd6f9fd1/docs/cli/gemini-md.md | 2026-10-22T21:52:00Z | 200 | 3,807 | `d00eeaef22453de4756a9862d8467750f772e239c4ee9b6f755709429b47c2cf` |
| https://zed.dev/docs/ai/instructions.md | 2026-10-22T21:52:00Z | 200 | 3,169 | `7c63efe035bf063809fb9815d4ed4ce6bdde6adb718e56ecd245e025f8244ab9` |
| https://geminicli.com/docs/cli/gemini-md.md | 2026-10-22T21:53:38Z | 200 | 3,816 | `e5fbfd6d580643a300b5ee0e622d9e2d8f97d4d23460e6b08e1c656251c2f2c2` |
| https://raw.githubusercontent.com/zed-industries/zed/cfb894a5dde8ccf3fba1659164f47fdd1c024e2e/docs/src/ai/instructions.md | 2026-10-22T21:53:38Z | 200 | 3,256 | `1bc6e31274cb4f7ff637f74c2fab1d0051ff258b5f310db485580336f91d7f4a` |
| https://raw.githubusercontent.com/zed-industries/zed/cfb894a5/docs/src/ai/instructions.md | 2026-10-22T21:56:20Z | 200 | 3,256 | same as above (`cmp` identical) |
| https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/gemini-md.md | 2026-10-22T21:54:46Z | 200 | 3,807 | `d00eeaef…` (`cmp` identical to the pinned fetch) |

Files kept at `/fast/scratch/hyaku/kotoba-r54/W2ScoutCorrections-src/{s060.md,s061.md,served-gemini.md,zed-src.md,zed-short.md,gemini-main.md}`.

## Attacks and verdicts

### A1 — re-fetch S060's pinned source: HOLDS
`corpus/SOURCES.md:73`. Fetched bytes are 3,807 B, sha256 `d00eeaef…`, matching the row's
`(200, 3,807 B, sha256 d00eeaef…)` and the main-branch copy is byte-identical (`cmp` clean),
matching the row's "current main 21:16:21Z, byte-identical".

### A2 — S060 teaches quotes verbatim: HOLDS
`supersedes S046's teaches cell — …` (`corpus/SOURCES.md:73`). The only quoted string,
"a different name or a list of names", is at `gemini-md.md:97-98` verbatim: line 97 reads
`To specify a different name or a list of names, use the` and line 98 `` `context.fileName` property. ``.
The example at `:105` is `"fileName": ["AGENTS.md", "CONTEXT.md", "GEMINI.md"]`, all three names
in the order the row states. `@file.md` import at `:73-75`: "importing content from other files
using the `@file.md` syntax. This feature supports both relative and absolute paths." The negative
"no occurrence of `replaces`" reproduces: `grep -o -i replac s060.md | wc -l` → `0`, and
`wc -l s060.md` → `116` (the row says 0 hits over 116 lines).

### A3 — S060 teaches no wider than its evidence: HOLDS
Each clause maps to a read line: default filename `:3` ("which use the default name `GEMINI.md`")
and `:96`; `settings.json`/`context.fileName` `:96-98`; example `:105`; import `:73-75`.
The two absence claims are page-scoped ("the page states no rule …"), and the whole 116-line file
was read; `fileName` appears only in the `:94-108` section and no ordering rule exists anywhere.
Anchor section ranges are exact: headings at lines 11, 71, 94; last content lines 38, 92, 108;
next headings at 40, 94, 110.

### A4 — S060's teaches opening against CORPUS.md rule 2: BREAKS (format, low)
`/home/vgpnk/Projects/shokunin/CORPUS.md:116-118`: "A correction is a new row whose `teaches` opens
`supersedes S0NN —`." S060 opens `supersedes S046's teaches cell — `; the em dash does not follow
the id. The registry's other seven correction rows are literal: S018, S019, S020, S021, S038,
S039 and S061 all open `supersedes S0NN — `. The append-only gate quotes the rule
verbatim (`verifiers/check_sources_append_only.py:7`) but does not test the opening form (its body
checks protected cells only), and the census matches the substring `supersedes S[0-9]{3}`
(`scripts/sources-census.sh:648`), so no mechanic catches it. The sense is narrower than the
template and arguably more precise, but the letter of rule 2 is not met. See Fix 1.

### A5 — S060's § Gate row records the URL: BREAKS (format, low; repeat of round 53)
`corpus/lessons/round-54.md:30`, URL column: "google-gemini/gemini-cli `docs/cli/gemini-md.md` at
`451a02ff` (raw), re-opened at main and on the served docs page". No `scheme://host` string, so
CORPUS.md rule 1 (`/home/vgpnk/Projects/shokunin/CORPUS.md:112-115`: "records, for every new row,
the URL, the access date, and a ≤25-word quote")
is not met on its face. The URL is reconstructible from `corpus/SOURCES.md:73` and my fetches
confirm it, so the defect is a record-shape defect, not a lost source. The same shape already
sits in round 53's Gate (`corpus/lessons/round-53.md:26`, S046) — a repeat, not new drift. No
verifier in `verifiers/` checks that it does: the ones that read § Gate read row ids and
double-quoted strings, not the URL column (`verifiers/check_description_thresholds.py:198-203`,
`verifiers/check_overlap_levers.py:356-357`). See Fix 2.

### A6 — re-fetch S061's source: HOLDS
`corpus/SOURCES.md:74`. Served page 3,169 B, sha256 `7c63efe0…` — the row's digest prefix and
byte count reproduce, as does round 53's `20:05:08Z` fetch that it says it matches.

### A7 — S061's § Gate quote verbatim and ≤25 words: HOLDS
`corpus/lessons/round-54.md:31`: "Project instruction files apply to the current project. Zed uses
the first matching file in this list:" — line 25 of the fetched page, character for character;
17 words, matching § Rows touched' "17-word quote" (`corpus/lessons/round-54.md:54`).

### A8 — S061's teaches no wider than its quote: HOLDS, with a paraphrase note
The teaches cell (`corpus/SOURCES.md:74`) says "the re-opened page still says Zed uses the first
matching project instruction file in the list". The page says "Zed uses the first matching file in
this list". The cell inserts the two words "project instruction". It is not in quotation marks, it
is faithful (line 25's first sentence defines the list as project instruction files), and it is
16 words, one word under the 17-word quote. So it is not wider than its evidence, but it is not a
verbatim quote either; anyone treating the cell as a quotation would find it off by two words.

### A9 — S061's anchor arithmetic and secondary claims: HOLDS
Every number in the anchor cell reproduces on my fetches: served nav line 1 is 91 B
(`head -1 s061.md | wc -c` → 91, 90 characters plus newline); source frontmatter 4 lines are 178 B;
removing either leaves exactly `62 lines, 3,078 B, sha256
2ec79b6c0dce27397b32672bbe92f3a808e3f62b69ad651be809e03329b48db9` on both sides (`wc -l -c` and
`sha256sum` on `tail -n +2 s061.md` and `tail -n +5 zed-src.md`). The 8-character form `cfb894a5`
returns the same 3,256 B and digest. The "no revision marker" claim reproduces:
`grep -n -i -E 'revision|commit|updated|sha256|version' s061.md` → no output, exit 1. The
parenthetical S050 still carries ("frontmatter only differs") is indeed false for the reason S061
gives: the served page also adds the `llms.txt` navigation line.

### A10 — S061's "not a new reading" phrase: HOLDS with a caveat
The teaches cell says the row "records the in-place anchor edit of `e792607e` as a correction, not
a new reading", while the anchor does record a corrected byte comparison (the S050 parenthetical is
false). Defensible if "reading" means the source's content (unchanged); ambiguous if it means the
row's own findings (one of which is new). Not counted as a break.

### A11 — S046's only in-place change is `used-by`: HOLDS
Cell-wise parse of the S046 row at `422ffd10`, `5a097e1` and tip `58db81c`: the only differing
column is `used-by`, `corpus/knowledge/alwayson-rule-files-round53.md` →
`corpus/knowledge/alwayson-rule-files-round53.md, corpus/lessons/round-54.md`. `anchor`, `teaches`,
`status`, `opened`, `recheck` are byte-identical across all three revisions. This matches
`corpus/lessons/round-54.md:46-47` exactly, including the odd but true "status `mined` → `mined`".
S046's `teaches` still says "replaces" (`corpus/SOURCES.md:59`) — left in place by design; the
live consumer already flags it (`corpus/knowledge/alwayson-rule-files-round53.md:28`, "the S046
row's \"replaces\" wording is wrong"), so no live entry teaches the falsehood.

### A12 — S061's correction target is real: HOLDS
`git show e792607e -- corpus/SOURCES.md` shows a single changed cell for S050: the anchor phrase
"at commit `cfb894a5` (frontmatter only differs)" → "at zed-industries/zed@`cfb894a5` (frontmatter
only differs)"; every other S050 cell unchanged. Exactly what `corpus/lessons/round-54.md:51-53`
and M45 (`:13`) state.

### A13 — § Rows touched text: HOLDS
`corpus/lessons/round-54.md:44-58` matches observation: S046's `used-by` old→new string is exact;
S060's supersession of the `teaches` cell only is true (S046's other cells unchanged); S050 "not
edited" is true between base and tip; the quoted bytes of the `replaces` pushback and the
"0 hits on both" grep reproduce on the pinned and served pages; the "frontmatter only differs"
falsity is confirmed. One observation: S060 also restates S046's anchor ranges (11-38, 94-108 vs
S046's 13-36, 94-106). S046's ranges were not wrong, only narrower, so "supersedes … only" holds,
but a reader comparing the two anchors sees two different ranges for the same sections.

### A14 — rows unchanged after the correction commit: HOLDS
S046, S050, S060, S061 and `corpus/lessons/round-54.md` are byte-identical between `5a097e1` and
tip `58db81c` — no later in-place edit touched the rows I attacked.

## Census

Command (read-only, fleet script, lane as named target):
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`
→ exit 0, last line `kotoba	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md`,
preceded by six `W04` lines: S018, S019, S021, S054, S055, S056.

- Base comparison: the same command against a clone at `422ffd10` exits 0 with three `W04` lines
  (S018, S019, S021). So this round added three warning lines (S054, S055, S056), all of the
  legitimate shape "same URL, new scope, new row" that the plan's own guard (a) requires.
  W-codes do not change the exit status by the script's contract (`:18`, `:33`).
- E04 (duplicate URL+scope) is silent for S060 and S061 only because their `teaches` cells match
  `supersedes S[0-9]{3}` (`:645-649`). Mutation checks in the sandbox:
  - `mutA`: S060's `supersedes S046's teaches cell — ` removed → `E04 S060 duplicate url … within
    scope …`, exit 1. The marker is load-bearing.
  - `mutB`: S060's opening changed to `supersedes S001 — ` (wrong row) → prints `ok`, exit 0.
    So the census certifies the marker's presence, not that the named row is the colliding one.
    The two rows do name the right rows (S046, S050), observed.
- Conclusion: the census passes as the ticket asks, and the `ok` is a format verdict, not proof
  that each correction supersedes the row whose URL and scope it repeats.

## Proposed fixes (text only; the L1 integrates)

**Fix 1 (A4, rule 2 opening).** Do not edit S060 in place — its `teaches` is a protected cell.
Record the deviation in `corpus/lessons/round-54.md` § Mistakes, e.g.:
`| M48 | contract-form | S060's teaches opens "supersedes S046's teaches cell —", not CORPUS.md rule 2's "supersedes S0NN —" (the lane's other seven correction rows use the literal form). The sense is narrower, not wider; no mechanic catches the form (append-only gate checks cells only, census matches the substring). | append-only rule 2 as written; S018/S019/S020/S021/S038/S039/S061 as precedent | Append-only: no in-place fix. The next round's correction rows must use the literal form; a future row may restate S060's scope. |`
If the L1 prefers a correction instead, the new row must itself open `supersedes S060 — …`.

**Fix 2 (A5, rule 1 URL).** Replace the S060 URL cell in `corpus/lessons/round-54.md:30` with the
pinned URL, keeping the re-open note:
`https://raw.githubusercontent.com/google-gemini/gemini-cli/451a02ff03f1d2a8fe870c120fd5342cfd6f9fd1/docs/cli/gemini-md.md (main and served routes named in corpus/SOURCES.md:73)`.
Round 53's S046 Gate row has the same shape; it is carried, not edited (closed round).

**Fix 3 (optional, later round).** Tighten `scripts/sources-census.sh` E04 to require the literal
prefix `supersedes S0NN —` *and* that the named id is the row sharing the URL+scope; as written, a
wrong id passes (`mutB`).

## Not checked here (other seats own them)
- `verifiers/check_sources_append_only.py` red/green behaviour and its self-test.
- Whether S060/S061 pass the C1 counter's Gate-quote matching (neither row is a C1 client row:
  they teach context files, not description thresholds).
- Round 53's own registry rows beyond S046/S050.
