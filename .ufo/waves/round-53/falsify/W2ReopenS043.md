Result: MIXED — the S043 row's anchor cell re-fetches byte-identically (HTTP 200, 51,971 B, same sha256) and every SOURCES cell holds against the page, but the knowledge entry quotes "see AGENTS.md" on `memory.md:436` where those words do not occur, leaves its "imports inside code are ignored" clause uncited, and omits `.claude/AGENTS.md` from its names-read cell, while the round lesson holding the Gate record is not in the judged revision.

Seat: `KotobaR53.W2ReopenS043` (leaf; no subagents, no model calls, no installs, no lane writes except this file). Target: `corpus/SOURCES.md:56` (row S043) and every S043 location in `corpus/knowledge/alwayson-rule-files-round53.md`. Lane at judged revision `c775d6823bfca8f0de8c0874032a954438b38edc`; all lane reads were read-only, all probes wrote only under `/fast/scratch/hyaku/kotoba-r53/w2/W2ReopenS043/`.

Bytes judged: the S043 row at `corpus/SOURCES.md:56` is byte-identical in the working tree and at `c775d68` (`git show c775d68:corpus/SOURCES.md | awk 'NR==56' | sha256sum` = `32c562665e161ee613e431107df3ddbb0d98ff0b1fc42fe8b5d1174bbd528533`, same as the worktree line). Every knowledge-entry line number in this report is a line of the committed blob at `c775d68` (`git show c775d68:corpus/knowledge/alwayson-rule-files-round53.md`, sha256 `25f9bfba996a09fe91f04f1adcfda4b264f0a3db794c615c3186306fd15e27db`), where `:1`, `:25`, `:39`, `:44`, `:46`, `:50`, `:60`, `:65` and `:79` carry the text quoted below. The working-tree copy of that file changed twice while this seat ran (`dcf3f1ad...` then `f228357b...`; other seats are adding S052 and rewording other rows), so working-tree line numbers drift by a few lines. Findings are stated against the judged revision.

## 1. Re-open receipt (HOLDS)

Commands and observed output (scratch directory `/fast/scratch/hyaku/kotoba-r53/w2/W2ReopenS043/`):

```
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-10-22T20:36:33Z
$ curl -sS -D headers.txt -o memory.md -w 'http_code=%{http_code} bytes=%{size_download} url=%{url_effective} time=%{time_total}\n' https://code.claude.com/docs/en/memory.md
http_code=200 bytes=51971 url=https://code.claude.com/docs/en/memory.md time=0.589982
curl_exit=0
$ sha256sum memory.md
971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff  memory.md
$ wc -c memory.md
51971 memory.md
```

Row anchor cell (`corpus/SOURCES.md:56`): "fetched 2026-10-22T20:04:43Z, HTTP 200, 51,971 B, sha256 971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff". Every value matches the independent fetch 32 minutes later, byte for byte. **HOLDS.**

URL, UTC access time, status, bytes, sha256 of this seat's fetch: `https://code.claude.com/docs/en/memory.md`, 2026-10-22T20:36:33Z, HTTP 200, 51,971 B, `971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff`. Content-Type `text/markdown; charset=utf-8`. Ordinary `curl` only; no browser, no challenge bypass.

Observation (not a defect): the response carries `last-modified: Thu, 22 Oct 2026 20:36:34 GMT`, equal to this request's own second and not to the 20:04:43Z fetch, while the body sha256 is unchanged. The header is request-stamped, so the row's sha256 (not `last-modified`) is the revision identity — which is what `ScribeClaudeCode.md:30` already records. [INFERENCE from two fetches; the header/body divergence is observed.]

## 2. Row cells against the page (all HOLD)

`memory.md` has 638 lines in the fetched bytes; every cited range exists and says what the row says.

| row cell | cited lines | observed page text (quote, <=25 words) | verdict |
|---|---|---|---|
| anchor § AGENTS.md table | `:354-358` | `:357` "An `AGENTS.md` and a `CLAUDE.md` or `CLAUDE.local.md` in your working directory or above it \| Your `CLAUDE.md` files only" | HOLDS |
| anchor § When Claude Code reads AGENTS.md | `:368-378` | `:368` "By default, Claude reads `AGENTS.md` only when you have no `CLAUDE.md` in your working directory or above it." | HOLDS |
| anchor § Choose which instruction files load | `:388-393` | `:390` "`claude-md-or-agents-md` \| Your `CLAUDE.md` files, or your `AGENTS.md` files when you have no `CLAUDE.md` or `CLAUDE.local.md`" | HOLDS |
| anchor § Share one file with other coding tools | `:440-452` | `:442` "putting an `@AGENTS.md` import in a `CLAUDE.md` next to it"; `:452` "a symlink also works:" | HOLDS |
| anchor § My CLAUDE.md is too large | `:617-619` | `:619` "Claude Code skips a file over 4 MiB." | HOLDS |
| teaches: both present, no import → CLAUDE.md only | `:357` | same table row as above | HOLDS |
| teaches: import and symlink are the two documented redirects | `:442-445`, `:452-455` | `:445` "`@AGENTS.md`"; `:455` "ln -s AGENTS.md CLAUDE.md" | HOLDS |
| teaches: file over 4 MiB skipped | `:619` | "Claude Code skips a file over 4 MiB." | HOLDS |
| scope: CLAUDE.md family, AGENTS.md, rules | `:356-357`, `:370-371` | `:370` "a `CLAUDE.md`, `.claude/CLAUDE.md`, or `CLAUDE.local.md` in your working directory or any directory above it"; `:371` ".claude/rules/ files" keep loading | HOLDS |

Section titles in the anchor cell match the page headings exactly (`## AGENTS.md` at `:350`, `### When Claude Code reads AGENTS.md` at `:366`, `### Choose which instruction files load` at `:384`, `### Share one file with other coding tools` at `:440`, `### My CLAUDE.md is too large` at `:617`). Ranges name the table/body rather than the heading for the first three; the sections named are unambiguous.

## 3. Row contract shape (HOLDS)

- The row has 13 pipe-separated fields (11 registry columns plus the two empties), so `E01` cannot fire; the URL appears once in the registry (no `E04` duplicate).
- `kind` docs, `tier` A (Anthropic's own documentation, primary for the scope it names), `status` `mined` with a `used-by` path that exists and cites S043 (`corpus/knowledge/alwayson-rule-files-round53.md:25`, `:1`), `opened` 2026-10-22, `recheck` 2027-01-20 = exactly 90 days after opening (ISO-date form allowed by fleet `CORPUS.md:105-106`).
- `python3`-free census command: `bash scripts/sources-census.sh validate --today 2026-10-22 --root /home/vgpnk/Projects/shokunin kotoba` → exit 0; printed `kotoba<TAB>ok<TAB>/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md` (tabs shown) and the three pre-existing W04 duplicate-URL notes (S018, S019, S021) that the plan already records at base. No S043 finding.
- Round contract rule 1 (`CORPUS.md:112-115`) asks the round lesson's Gate to record URL, access date and a <=25-word quote with location for every new row. `corpus/lessons/round-53.md:23` does: URL, `2026-10-22T20:04Z`, `51,971 B, 971d75bf...`, and the quote "An `AGENTS.md` and a `CLAUDE.md` or `CLAUDE.local.md` in your working directory or above it" -> "Your `CLAUDE.md` files only" at `memory.md:357` (18 words), which grounds `teaches`. **HOLDS.**

## 4. Knowledge-entry citations, line by line

| # | claim (path:line) | cite | observed | verdict |
|---|---|---|---|---|
| K1 | source set for S043 (`alwayson-rule-files-round53.md:1`) | `memory.md:354-358, 368-378, 440-461` | all ranges inside the 638-line file; `:461` is the Windows bullet of the Share section | HOLDS |
| K2 | names read: CLAUDE.md, .claude/CLAUDE.md, CLAUDE.local.md; AGENTS.md only when none exists (`:25`) | `:356, 368-370` | `:356` AGENTS.md when no CLAUDE.md/CLAUDE.local.md; `:370` lists all three counting names | HOLDS |
| K3 | both present reads "Your `CLAUDE.md` files only" (`:25`) | `:357` | verbatim in the table cell | HOLDS |
| K4 | redirect: a CLAUDE.md with an `@AGENTS.md` import (`:25`) | `:442-445` | `:442` names the import in a CLAUDE.md next to AGENTS.md; `:445` shows the fenced line | HOLDS |
| K5 | redirect: a CLAUDE.md symlink to AGENTS.md (`:25`) | `:452-455` | `:452` "a symlink also works:"; `:455` `ln -s AGENTS.md CLAUDE.md` | HOLDS |
| K6 | prose mention is not a redirect, quoted as "see AGENTS.md" (`:50`) | `:436` | the quoted words are absent from the page; `:436` says "Claude sees `AGENTS.md` only if it decides to open the file" | **BREAKS** (quote only; claim holds) |
| K7 | imports inside code are ignored (`:25`) | none | true at `:112` "Import parsing skips Markdown code spans and fenced code blocks.", but `:112` is in neither the row anchor nor the entry's source-line set | **BREAKS** (citation gap) |
| K8 | with two files in one directory Claude Code reads only CLAUDE.md (`:39`) | S043 (no line) | `:357` table row | HOLDS |
| K9 | symlink gives every client that reads either name the same bytes (`:44`) | `:455` | `:455` is the symlink command; the cross-client byte identity is a filesystem inference, not S043 text | HOLDS (line), INFO (unmarked inference) |
| K10 | Claude Code expands an `@AGENTS.md` import (`:46`) | S043 (no line) | `:442` and `:378` ("`@path` imports ... are expanded") | HOLDS |
| K11 | nearest authority on stale text is advice to remove outdated instructions (`:60`) | `:90` | "Review your CLAUDE.md files ... periodically to remove outdated or conflicting instructions" | HOLDS |
| K12 | 200-line target and 4 MiB skip (`:65`) | `:88, :619` | `:88` "target under 200 lines per CLAUDE.md file"; `:619` "Claude Code skips a file over 4 MiB." | HOLDS |
| K13 | AGENTS.md read directly only from v2.1.277 (`:79`) | `:364` | "Reading `AGENTS.md` directly requires Claude Code v2.1.277 or later." | HOLDS |

## 5. Defects

**D1 (LOW) — fabricated quotation attributed to `memory.md:436`.** `corpus/knowledge/alwayson-rule-files-round53.md:50` reads: a prose mention is not a redirect (S043 `:436`), then quotes "see AGENTS.md" as the example. The string does not exist in the fetched bytes:

```
$ grep -nF 'see AGENTS.md' memory.md; echo "exit=$?"
exit=1
$ grep -ni 'prose' memory.md; echo "exit=$?"
exit=1
```

`grep -rln` shows the phrase occurs nowhere else in the lane (`verifiers/`, `corpus/`) except that line; variant checks (`see \`AGENTS.md\``, `See AGENTS.md`) also return nothing, and the only `see [AGENTS.md]` hit is a documentation cross-link at `:40`, not the prose-instruction case. The nearest real wording at `:436` is "tells Claude in words to read `AGENTS.md`"; the nearest wording to the quoted phrase is the lane fixture `verifiers/fixtures/alwayson/a07-prose-mention/CLAUDE.md:3` ("See AGENTS.md for the shared rules."), i.e. lane example text, not vendor text. The claim itself is supported by `:436`: "**A `CLAUDE.md` that tells Claude in words to read `AGENTS.md`**: Claude sees `AGENTS.md` only if it decides to open the file." Fix: quote that sentence (13 words) and drop the invented example, or label the example as the fixture's wording. No counter, box map or verdict consumes the quote, so the damage is evidentiary precision only.

**D2 (LOW) — uncited clause in the Claude Code redirect cell.** `:25` ends "imports inside code are ignored" with no `S043 :line` and no bracket; the page does say it at `:112` ("Import parsing skips Markdown code spans and fenced code blocks."), but `:112` is outside both the row's anchor set (`354-358, 368-378, 388-393, 440-452, 617-619`) and the entry's source-line list (`354-358, 368-378, 440-461`). A reader following the entry's own anchors cannot reach the sentence. Fix: append `:112` to the entry's source line (and optionally the row anchor); no claim change needed.

**D3 (LOW) — the names-read column omits `.claude/AGENTS.md`, which the cited section states.** `:25` lists `CLAUDE.md`, `.claude/CLAUDE.md`, `CLAUDE.local.md` and `AGENTS.md` only when none of those exists; `memory.md:375`, inside the same cited section (`:368-378`), says "every `AGENTS.md` and `.claude/AGENTS.md` in your working directory and the directories above it" load at session start. The cell does not claim to be exhaustive, but a reader taking it as the client's project-level name list misses a documented variant. Fix: add `.claude/AGENTS.md` to the AGENTS.md clause (the box and instrument need no change).

**Observation O1 (INFO) — unmarked inference at `:44`.** "A `CLAUDE.md` symlink to `AGENTS.md` gives every client that reads either name the same bytes (S043 `:455`; ...)" cites the command line correctly, but S043 says only that Claude "reads the content once" (`:437`); the universal client claim is a filesystem inference. The entry marks its other inferences explicitly ([INFERENCE] in the omp row), so this one reads as sourced when it is derived. Not a break: the cited line supports the mechanism the sentence rests on.

**Observation O2 (INFO) — anchor revision form.** Fleet `CORPUS.md:99-100` asks the anchor for "section / heading / page / line plus revision (version, commit, or publication date)". S043 supplies fetch time, HTTP status, bytes and sha256, but no version or publication date. The page states no version and its `last-modified` is request-stamped (section 1), so the sha256 is the only stable identity; sibling rows S035 (`corpus/SOURCES.md:48`) and S036 (`:49`) use the same substitute. Not a defect under registry practice; recorded so the choice is visible.

**Observation O3 (LOW, publication state) — the Gate record is not in the judged revision.** Contract rule 1 (`CORPUS.md:112-115`) requires the round lesson's `## Gate` to record each new row's URL, access date and <=25-word quote. The record exists and is correct in the working tree (`corpus/lessons/round-53.md:23`, verified in section 3), but it is not in the revision: `git cat-file -e c775d68:corpus/lessons/round-53.md` fails and `git status --porcelain` lists the file as `??` untracked. If `c775d68` is the final judged revision, the S043 Gate evidence is absent from it; the lesson needs committing before the revision is final.

## 6. What this seat did not cover

- The page is live and carries no usable revision header; identity rests on byte equality between 20:04:43Z and 20:36:33Z. A later edit can only be caught by re-fetch and sha comparison.
- The rendered HTML page was not fetched; the row anchors the `.md` bytes, which are what was checked.
- S044-S051 rows, the C1/C2 counters, the erratum guards and the no-harm matrix are other seats' targets; nothing here touches them.
- No tool was installed or upgraded; no lane file was edited except this report; the census script was run read-only (it writes only stdout unless `--out` is given).
