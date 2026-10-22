Result: DONE — S046's "replaces" wording has no support in the source (0 case-insensitive hits for `replac` over the pinned 116 lines), and the append-only correction is drafted as S060 with its Gate record and the S046 `used-by` old→new line; every draft artifact was shape-checked and the census validated it in a sandbox clone (exit 0, 53 rows, 0 malformed, three carried W04 warnings).

# ScribeS046Fix — round 54 build, routed defect 2 (S046 teaches cell)

Seat: scribe, leaf (no subagent dispatch, no peer messages). The lane was read-only for this seat; all execution
ran in the sandbox clone `/fast/scratch/hyaku/kotoba-r54/ScribeS046Fix/lane`, cloned from the lane and checked
out at `7ad05d342d7505ab674a5ebcf5ac1106b2f45c39`. Lane HEAD moved to `90cae9af` while the seat ran (L1 errata 1–3
and the defect-6 pointer fix); `git diff --name-status 7ad05d34..HEAD` → `plans/round-54.md`,
`verifiers/baseline.json` only, so `corpus/SOURCES.md` is unchanged and the line numbers below hold at the tip.
No lane file was written or edited. No tool was installed or upgraded.

## 1. What the source says against what S046 claims

S046 (`corpus/SOURCES.md:59`) teaches: "… a string or list in `context.fileName` replaces the name, the page's
example being `AGENTS.md`, `CONTEXT.md` and `GEMINI.md`, and an `@file.md` import pulls another file's bytes in".

The page says four things about the setting and never uses the word "replace":

- `gemini-md.md:96` — "While `GEMINI.md` is the default filename, you can configure this in your `settings.json` file."
- `gemini-md.md:97-98` — "To specify a different name or a list of names, use the `context.fileName` property."
- `gemini-md.md:105` — `"fileName": ["AGENTS.md", "CONTEXT.md", "GEMINI.md"]`, an example that keeps `GEMINI.md`
  in the list beside the two other names.
- `gemini-md.md:73-75` — imports: "by importing content from other files using the `@file.md` syntax. This feature
  supports both relative and absolute paths."

Nothing on the page states whether a configured name replaces the default or adds to it, and nothing orders the
listed names. The measurable form of that negative:

```
$ grep -o -i replac pinned.md | wc -l          → 0        (116-line file, whole file)
$ grep -o -i replac current-raw.md | wc -l     → 0
$ grep -o -i replac served.md | wc -l          → 0
```

The rendered HTML route has 3 hits for `replac`, none of them the rule: two are inline JavaScript
(`oldIcon.replaceChildren(...)`, `window.location.pathname.replace(...)`) and one is the site banner sentence
quoted in § 4 below ("Gemini CLI was replaced by Antigravity CLI …", a product replacement, not a filename rule).

## 2. Fetch records (all opened 2026-10-22, ordinary `curl`, no browser, no challenge bypass)

| what | URL | when (UTC) | status | bytes | sha256 |
|---|---|---|---|---|---|
| pinned raw (S046's own URL) | `https://raw.githubusercontent.com/google-gemini/gemini-cli/451a02ff03f1d2a8fe870c120fd5342cfd6f9fd1/docs/cli/gemini-md.md` | 2026-10-22T21:16:17Z | 200 | 3,807 | `d00eeaef22453de4756a9862d8467750f772e239c4ee9b6f755709429b47c2cf` |
| current docs source tree (main) | `https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/gemini-md.md` | 2026-10-22T21:16:21Z | 200 | 3,807 | same sha (`cmp pinned.md current-raw.md` → identical) |
| current docs page, markdown route | `https://geminicli.com/docs/cli/gemini-md.md` | 2026-10-22T21:16:26Z; re-fetched 21:17:28Z, same sha | 200, `text/markdown` | 3,816 | `e5fbfd6d580643a300b5ee0e622d9e2d8f97d4d23460e6b08e1c656251c2f2c2` |
| current docs page, rendered routes `/docs/cli/gemini-md/` and `/docs/cli/gemini-md` | `https://geminicli.com/docs/cli/gemini-md/` | fetched in the loop that completed 21:16:26Z | 200, `text/html` | 109,443 (both routes, one sha) | `2b0d60bebef3481fae272aa27f40984cddff8c62ee039844f3074542eb3a01ea` |

The pinned bytes are the same bytes S046 recorded (3,807 B, `d00eeaef…`), and main head is byte-identical: the
pinned text is not stale. The served markdown copy differs from the pinned file in exactly four link targets plus
a missing final newline (`grep -o '](\([^)]*\))' | sort` on both → 4 targets, all rewritten
`../reference/memport.md`→`/docs/reference/memport`, `./gemini-ignore.md`→`/docs/cli/gemini-ignore`,
`../tools/memory.md`→`/docs/tools/memory`, `./custom-commands.md`→`/docs/cli/custom-commands`). § Customize the
context file name is the same text at `:94-108` in both. 116 newlines in the pinned copy, 115 in the served copy.

Quote word counts, each ≤25 (counted by `len(q.split())`): `:96` 14 words, `:97-98` 14, `:105` 4, `:73-74` 22.

## 3. Draft artifact 1 — the S060 row (append-only correction)

Paste into `corpus/SOURCES.md` immediately after the S052 row (line 65, the last row of the `## Registry`
table). Do NOT append at end of file: `sources-census.sh validate` then prints
`E12 S060 row outside Registry section`, exit 1 (measured, § 7 run 2).

```
| S060 | Gemini CLI docs source — Provide context with GEMINI.md files (google-gemini/gemini-cli, commit pinned in the URL) — https://raw.githubusercontent.com/google-gemini/gemini-cli/451a02ff03f1d2a8fe870c120fd5342cfd6f9fd1/docs/cli/gemini-md.md | docs | A | Gemini CLI's documented context-file names, the `context.fileName` list setting and the `@file.md` import redirect (vendor documentation at a pinned commit; not a measurement of any installed binary) | § Understand the context hierarchy (`gemini-md.md:11-38`); § Modularize context with imports (`:71-92`); § Customize the context file name (`:94-108`); fetched 2026-10-22T21:16:17Z (200, 3,807 B, sha256 `d00eeaef…`); current main 21:16:21Z, byte-identical; served as https://geminicli.com/docs/cli/gemini-md.md 21:16:26Z and 21:17:28Z (200, 3,816 B, sha256 `e5fbfd6d…`), same § Customize text, four relative links rewritten and no final newline | supersedes S046's teaches cell — `GEMINI.md` is the default filename (`:3`, `:96`); `context.fileName` is the `settings.json` property that specifies "a different name or a list of names" (`:97-98`), its example listing `AGENTS.md`, `CONTEXT.md` and `GEMINI.md` together (`:105`); the page states no rule for whether a configured name replaces or adds to the default, and no ordering for listed names; an `@file.md` line imports another file's content from a relative or absolute path (`:73-75`); the file contains no occurrence of "replaces" (0 hits over its 116 lines) | mined | 2026-10-22 | 2027-01-20 | corpus/lessons/round-54.md |
```

Design notes, each measured (§ 7):

- **Scope cell copied verbatim from S046.** Same URL and same scope hits the census's E04 branch, which exempts a
  row whose teaches matches `supersedes S[0-9]{3}`; with the same scope no W04 warning is added either. A
  rewritten scope also validates but adds a fourth `W04 duplicate url … across scopes` beside the three carried
  ones (S018, S019, S021). I chose the quiet form; both were run.
- **`supersedes S046's teaches cell`** states the correction's reach exactly: S046's `source`, `kind`, `tier`,
  `scope`, `anchor` and `opened` cells are untouched, so no cell loses its record.
- **`used-by` = `corpus/lessons/round-54.md`**, the lesson Gate row below; it must exist in the same landing.
  Measured with the lesson moved away: `E11 S046 missing used-by corpus/lessons/round-54.md` and
  `E11 S060 missing used-by corpus/lessons/round-54.md`, exit 1. The S046 `used-by` addition is coupled to the
  same file, so the lesson and both row changes land together or not at all.
- **`status mined`** is earned by that Gate citation, not by the entry. If the L1 lands the row without the Gate
  row, the honest status is `queued` (contract: mined = cited by ≥1 path in `used-by`).
- **No in-place edit to S046.** Its teaches cell keeps the over-wide wording forever; the correction is the row.

## 4. Draft artifact 2 — Gate record for `corpus/lessons/round-54.md` § Gate

Table row for the Gate table (same seven columns as `corpus/lessons/round-53.md` § Gate), then the notes and the
correction log. `corpus/lessons/round-54.md` does not exist at the tip; this is L1-owned text.

```
| S060 | google-gemini/gemini-cli `docs/cli/gemini-md.md` at `451a02ff` (raw), re-opened at main and on the served docs page | 2026-10-22T21:16:17Z (main 21:16:21Z; served 21:16:26Z, re-fetched 21:17:28Z) | pinned 200, 3,807 B, sha256 `d00eeaef…`; served 200, 3,816 B, sha256 `e5fbfd6d…` | "To specify a different name or a list of names, use the `context.fileName` property." (14 words); `"fileName": ["AGENTS.md", "CONTEXT.md", "GEMINI.md"]` (4 words); "You can break down large `GEMINI.md` files into smaller, more manageable components by importing content from other files using the `@file.md` syntax." (22 words) | `gemini-md.md:97-98`, `:105`, `:73-74`; default at `:3`, `:96` | ScribeS046Fix |

- The word S046 borrowed, `replaces`, is not in the source: `grep -o -i replac` over the pinned 116-line file
  → 0 hits; the same grep over the served markdown copy → 0 hits.
- The served markdown copy differs from the pinned file in four link targets rewritten to `/docs/...` and a
  missing final newline; § Customize the context file name is the same text at `:94-108`. The rendered HTML
  route carries the sentence once.
- The served page carries a site banner, in two paragraphs: "Unpaid tier and Google One users: Gemini CLI was
  replaced by Antigravity CLI on June 18th, 2026." (17 words) and "Gemini CLI has not been optimized for Gemini 4
  Argon. To use Gemini 4 Argon, please use Antigravity." (18 words). The banner is site chrome: it is absent
  from all three markdown copies (`grep -c -i antigravity` → 0, 0, 0). It does not change § Customize; it bears
  on how long the row stays useful, not on this correction.

### Correction log

- **S046 (append-only correction; round-53 spot-check routed defect 2).** S046's `teaches` cell says a string or
  list in `context.fileName` "replaces the name". The pinned bytes and the served page state no such rule, and
  `"replaces"` does not occur in the file. S060 supersedes S046's teaches cell and no other cell; S046's
  `source`, `kind`, `tier`, `scope`, `anchor` and `opened` cells are unchanged. In-place changes, old→new:
  `used-by` `corpus/knowledge/alwayson-rule-files-round53.md` →
  `corpus/knowledge/alwayson-rule-files-round53.md, corpus/lessons/round-54.md`; status `mined` → `mined`;
  recheck `2027-01-20` → `2027-01-20`.
```

## 5. Draft artifact 3 — the S046 in-place change (only `used-by`)

At `corpus/SOURCES.md:59`, last cell only:

- old: `corpus/knowledge/alwayson-rule-files-round53.md`
- new: `corpus/knowledge/alwayson-rule-files-round53.md, corpus/lessons/round-54.md`

Logged old→new in the lesson as in § 4. `status` `mined` → `mined` and `recheck` `2027-01-20` → `2027-01-20`
are unchanged: the source is a pinned commit whose bytes cannot move, and the entry still cites S046, so `mined`
stays earned. The banner quoted in § 4 is a reason the L1 might shorten the recheck cadence; that is a judgment
call outside this draft, and I did not invent one.

Optional (L1 decision, an entry edit outside this seat's scope): make the correction reachable from
`corpus/knowledge/alwayson-rule-files-round53.md:28` by changing that row's `row` cell `S046` →
`S046, S060` (and, if wanted, the clause "the S046 row's "replaces" wording is wrong" →
"the S046 row's "replaces" wording is wrong (corrected by S060)"). If that lands, extend S060's `used-by` with
`corpus/knowledge/alwayson-rule-files-round53.md` in the same change.

## 6. Q29 (corrections registered in the sweep) — measured, and not mine to land

Q29 says a correction's stale phrase and declared result go into `verifiers/check_correction_sweep.py`'s registry
in the same commit. Two measured facts decide the shape:

- A registry row on `corpus/SOURCES.md` is red forever. The sweep's rule is per block, and a table row is one
  block (`check_correction_sweep.py:85-105`), so S046's row must carry the declared pattern; rule 2 of the SOURCES
  contract forbids editing it. Measured with a mutant registry row
  (`{"file": "corpus/SOURCES.md", "stale": r"replaces the name", "declared": r"supersedes S046"}`):
  `FAIL probe-so corpus/SOURCES.md:59 stale claim without the declared result`, exit 1 — S060's own row was green.
- A registry row on `corpus/lessons/round-54.md` works only with a `SEEDED` addition: as written, the self-test
  builds its fixtures from `SEEDED` (`:77-83`), so the row raises `RuntimeError: missing
  corpus/lessons/round-54.md` inside `--self-test`, exit 1. With `"corpus/lessons/round-54.md"` added to
  `SEEDED`, `--self-test` → `0 failure(s) over 11 assertions`, exit 0, and `--root <clone>` → `0 stale block(s)`.

So the honest options are: (a) land that lesson row plus the `SEEDED` entry plus a red/green assertion pair in
`self_test` (the row alone is unexercised), or (b) record the exception in the lesson. My recommendation is (a)
only if the L1 is willing to touch a verifier in a wave whose two claim counters are frozen; otherwise (b) with
this paragraph's measured reason as the record. No floors bump is needed either way:
`verifiers/floors-registry.json` has 13 instrument keys and none is the correction sweep.

## 7. Verification runs (sandbox clone unless stated)

1. Row shape, contract census:
   `awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF!=13 {n++} END{print n+0}' corpus/SOURCES.md`
   → `0`; row count `grep -cE …` → `52 → 53`; the S060 row's own `NF=13`.
2. Append point: row appended at end of file →
   `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file <clone>/corpus/SOURCES.md --today 2026-10-22`
   → `E12 S060 row outside Registry section`, exit 1.
3. Row inserted after line 65 with the lesson stub present → same command → exit 0, output:
   `file W04 S018 …` / `file W04 S019 …` / `file W04 S021 …` / `file ok <path>/corpus/SOURCES.md`.
   These are the three warnings the round-53 closure already carried; no new warning, no E04.
4. Rewritten-scope variant (not chosen) → exit 0 plus a fourth line
   `file W04 S060 duplicate url raw.githubusercontent.com/google-gemini/gemini-cli/451a02ff… across scopes`.
5. Sweep mutant A and mutant B as quoted in § 6; the clone's `verifiers/check_correction_sweep.py` was restored
   afterwards (`git checkout -- verifiers/check_correction_sweep.py`; `git status --porcelain` then showed only
   `M corpus/SOURCES.md` and `?? corpus/lessons/round-54.md`, the two fixtures, before run 7 committed them).
6. Lane untouched: no write, no git write, no jj command. Lane reads only (`git log`, `git diff --name-status`,
   `git status --porcelain`, `sed -n`, `grep`).
7. Landing shape against the rule-2 gate the L1 is drafting: the lane working tree carries an untracked
   `verifiers/check_sources_append_only.py` (189 lines, sha256 `d4d1d62b16ededc8f31e5df71738285bd88768a2b3e3b9824b2782143fef3805`).
   I copied that file into the clone, committed the S060 row plus the lesson stub (`3efe5e4`), then S046's
   `used-by` change alone (`2bd67d2`), and ran
   `python3 -B verifiers/check_sources_append_only.py --repo . --rev HEAD --base 7ad05d34…` →
   `log  2bd67d23c S046 used-by: …les-round53.md -> …les-round53.md, corpus/l…` and
   `sources append-only rows clean: 2 commits scanned, 0 protected-cell changes`, exit 0. The row append alone
   produced no note, and no protected cell moved.
8. That draft gate's own self-test: `--self-test` → `self-test: 0 failure(s) over 14 assertions`, exit 0. The
   census on the same committed state → exit 0, the three carried W04 lines and `ok`, no fourth warning.
9. The `used-by` dependency, measured: with `corpus/lessons/round-54.md` moved out of the clone, the same census
   command prints the three W04 lines plus `E11 S046 missing used-by corpus/lessons/round-54.md` and
   `E11 S060 missing used-by corpus/lessons/round-54.md`, exit 1; the lesson was restored afterwards and
   `git status --porcelain` is empty.

## 8. Findings for the L1

1. **The routed defect is real and exactly as routed**: the word "replaces" appears nowhere in the source, at the
   pin or at main head or on the served page; the page only says the setting specifies "a different name or a
   list of names" and its example keeps `GEMINI.md` in the list.
2. **The docs host announces a product transition.** The served page's banner: "Unpaid tier and Google One users:
   Gemini CLI was replaced by Antigravity CLI on June 18th, 2026." (17 words) and "Gemini CLI has not been
   optimized for Gemini 4 Argon. To use Gemini 4 Argon, please use Antigravity." (18 words). It does not delete
   the page. This matters to the C1 Gemini CLI row (S057) and to any recheck cadence: the docs page is still
   evidence of what Gemini CLI documents, but the client it describes is announced as superseded for those
   tiers. I make no claim about installed behavior.
3. **Append-only rows still append to the table, not the file.** `E12` fires on an end-of-file row. S060 goes
   after the row that is last when it lands: line 66 today (after S052 at 65), or line 73 if S053–S059 all land
   first. It is a row of the `## Registry` table either way.
4. **Scope equality is load-bearing for the census.** A superseding row that keeps the superseded row's scope
   cell avoids both `E04` (via the `supersedes S…` phrase) and a new `W04`; a rewritten scope costs a warning.
   The three carried W04 rows (S018, S019, S021) are exactly the earlier supersessions that rewrote scope.
5. **The correction sweep cannot express an append-only supersession** (§ 6), and
   `verifiers/check_correction_sweep.py` has no row in `verifiers/floors-registry.json` — an unfloored
   instrument. Both are recorded, not repaired here.
6. **The round-53 entry is already calibrated on this point**: `corpus/knowledge/alwayson-rule-files-round53.md:28`
   says "the S046 row's "replaces" wording is wrong" and cites the loader lines that add rather than replace.
   S060 gives that sentence a row to point at; it does not change the entry's finding.
7. **A rule-2 gate is being drafted in the lane's working tree** (`verifiers/check_sources_append_only.py`,
   untracked at the time of this seat, sha256 `d4d1d62b…`). The drafted landing passes it (§ 7 runs 7–8): the
   append is silent, the `used-by` change is printed as a log note, no protected cell moves. If that gate lands,
   the lesson must carry the old→new line or the note is unlogged — which § 4 provides.

## 9. Out of scope for this seat, and limits of the record

- Not done, by bounds: no edit to `corpus/SOURCES.md`, `corpus/lessons/round-54.md`, `SKILL.md`, the entry, any
  verifier, `floors-registry.json` or `LOG.md`; no commit in the lane or the fleet (the two probe commits exist
  only in the sandbox clone), no push, no jj; no C1 or C2 counter run; no client CLI executed; no model call;
  no `ask`.
- Statements here are about documentation bytes. I ran no Gemini CLI binary and make no claim about its behavior.
  The two "replaces" negatives are bounded to the three files named and their line counts; they are not a Q30
  client-level negative (no changelog or source-tree sweep was needed for a claim about one page's text, and none
  is asserted).
- The served markdown sha and the HTML sha were computed from the saved bytes at the times recorded; the two HTML
  routes were fetched in one loop that completed 21:16:26Z, so the per-route second is not recorded separately.
- The row's `mined` status and its `used-by` depend on the Gate row landing in `corpus/lessons/round-54.md`;
  until then the row is `queued`.

## Artifacts

- `/fast/scratch/hyaku/kotoba-r54/ScribeS046Fix/pinned.md` (3,807 B, `d00eeaef…`), `current-raw.md`,
  `served.md` (3,816 B, `e5fbfd6d…`), `site-*.out` (HTML, `2b0d60be…`)
- `/fast/scratch/hyaku/kotoba-r54/ScribeS046Fix/row.txt` — the exact S060 row line
- `/fast/scratch/hyaku/kotoba-r54/ScribeS046Fix/lesson-stub.md` — the Gate row, notes and correction log
- `/fast/scratch/hyaku/kotoba-r54/ScribeS046Fix/lane` — clone at `7ad05d34` carrying two probe commits,
  `3efe5e4` (S060 row at line 66 plus the lesson stub) and `2bd67d2` (S046 `used-by` old→new), the state the
  census, append-only gate and self-test runs in § 7 were made against. Nothing was pushed; the clone is local.
- This report is the only file written in the lane:
  `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-54/build/ScribeS046Fix.md`.
