# ScribeSourcesCorrection — r72 closure defect D3 (SOURCES.md Search-log correction) + D4 (LOG.md note)

**Verdict.** Both drafts are written and form-proved. D3's damage map is confirmed independently against
`git show c69711e:corpus/SOURCES.md` and the insertion commit's own diff: commit `a0f7f17` cut the round-64
placement-correction note's heading code span at its opening backtick and inserted the round-72 note between
the note's first and second lines. The D3 note is 11 lines, carries two quoted spans that are literal
substrings of `c69711e:206-208`, adds no registry row, and contains no line-initial `|` and no `## `.
D4 is **not** merely "dangling comma/period" as the r72 spot-check reports (quoted verbatim below): the
wave-1 draft of that bullet carried a second clause, so `,.` is a truncation at a comma. The one-line
repair I propose keeps the truncation out and does not import the dropped clause.

No lane file was modified. No scratch dir, no network fetch, no gate run (out of scope for this seat).

## Deliverables

- `.ufo/waves/round-73/w1/build/ScribeSourcesCorrection/entry.md` — the Search-log note, ready to append.
- `.ufo/waves/round-73/w1/build/ScribeSourcesCorrection/log-note.md` — the exact replacement line for
  `resident-index-and-rungs-round72.md:45` plus the one-line `LOG.md` note.
- `ScoutSourcesDamage.md` is absent from `.ufo/waves/round-73/w1/`: at my first `ls` the directory held only
  `build/` and `swarm-registry.json`, and at the second only those plus a sibling `ScoutCnCensus.md`. The
  damage map in S1 is therefore mine, derived from the repo, not read from that seat.

## S1 — D3 damage, exact coordinates (re-derived, not taken from another seat)

Base state, `git show c69711e:corpus/SOURCES.md | sed -n '206,208p'`:

```
- **2026-10-24 — placement correction (appended by the L1 in wave 2):** the two round-64 notes
  originally landed at EOF under `## Leads (unopened)` (the placement defect `CriticW2Frontier` F3 caught at the
  measured tip); their content is preserved verbatim and they are relocated to the end of `## Search log` here.
```

Insertion commit — `git show --stat --oneline a0f7f17` first line:
`a0f7f17 round-72: claim data — four author-facing rule boxes + S214-S216 + rung entry (C1); …` and its
SOURCES hunk `@@ -204,7 +207,11 @@` shows exactly:

```
-  originally landed at EOF under `## Leads (unopened)` (the placement defect `CriticW2Frontier` F3 caught at the
+  originally landed at EOF under `
+
+- **2026-10-25 — round-72 assimilation openings.** … (one long line) … the rung rule is fully carried by three vendor statements.
+
+## Leads (unopened)` (the placement defect `CriticW2Frontier` F3 caught at the
```

Tip state, `awk 'NR>=209&&NR<=217{printf "%d\t%.95s\n",NR,$0}' corpus/SOURCES.md`:

```
209  - **2026-10-24 — placement correction (appended by the L1 in wave 2):** the two round-64 notes
210    originally landed at EOF under `
211  (blank)
212  - **2026-10-25 — round-72 assimilation openings.** Question: where do vendors state …
213  (blank)
214  ## Leads (unopened)` (the placement defect `CriticW2Frontier` F3 caught at the
215    measured tip); their content is preserved verbatim and they are relocated to the end of `## Search log` here.
216  (blank)
217  ## Leads (unopened)` list (anthropics/skills, Anthropic Engineering, learn.chatgpt.com
```

- The r72 note itself is intact (line 212 ends `… the rung rule is fully carried by three vendor statements.`), so the defect is placement + a cut code span, not a truncated insertion.
- `git blame -L 205,220 corpus/SOURCES.md` attributes 210-214 to `a0f7f17` and 209, 215, 216, 217 to `dad926c` / `7ad7fad` — the split lines are the r72 edit's.
- Stray level-2 headings: `grep -n '^## ' corpus/SOURCES.md` → `10, 159, 177, 214, 217, 239, 281` (7);
  `git show c69711e:corpus/SOURCES.md | grep -n '^## '` → `10, 156, 174, 210, 232, 274` (6). So r72 added
  exactly one stray heading (`:214`); `:217` and `:281` are the pre-existing pair the 2026-10-24 note itself
  admits (`c69711e:210`, `:274`).
- Coordinates agree with the r72 spot-check's citation of `209-215`: at `e8207c6` the same five lines sit at
  `209, 210, 212, 214, 215` (`git show e8207c6:corpus/SOURCES.md | grep -n '^## '` → `214, 217, 239, 281`),
  i.e. no line shift between `e8207c6` and the tip.

## S2 — the draft entry (`.ufo/waves/round-73/w1/build/ScribeSourcesCorrection/entry.md`)

```
- **2026-10-25 — search-log correction (r72 closure defect D3; appended in round 73).**
  Question: where did the round-72 assimilation note land? At `c69711e` the round-64
  placement-correction note sits at `corpus/SOURCES.md:206-208` and its title reads
  "2026-10-24 — placement correction (appended by the L1 in wave 2)"; its second line reads
  "originally landed at EOF under" its quoted heading string. Commit `a0f7f17` (round-72 claim
  data) inserted the round-72 note between that note's first and second lines and cut the
  heading code span at its opening backtick. Reader-visible at the tip: `corpus/SOURCES.md:214`
  starts with a level-2 heading marker followed by `Leads (unopened)` and the note's tail, and
  `:217` keeps the older stray of the same family (already at `c69711e:210`). No bytes before
  this note are rewritten — the split sentence stays where `a0f7f17` left it and this note is
  the correction of record (CORPUS rule 2, append-only); it adds no registry row.
```

Quoted spans, shaped as documented: `2026-10-24 — placement correction (appended by the L1 in wave 2)`
(dropped the wrapping `**…**` and the trailing `:**`), 11 words; `originally landed at EOF under` (dropped
everything after `under`, namely the cut heading string and the rest of the sentence), 5 words. Both are
literal substrings: `git show c69711e:corpus/SOURCES.md | sed -n '206,208p' | grep -cF -- "<span>"` → `1`
for each. Neither is "byte-exact" in the report sense — the `**` shaping is stated.

Landing anchor for the L1: end of `## Search log`, i.e. insert after tip line 237
(`- Round 51 (2026-10-22): overlap levers by client — …`, the last note before the blank line 238 and
`## Leads (unopened)` at 239). The note's own `:214` / `:217` references stay valid because the anchor is
later in the file.

## S3 — form proofs (run from `.ufo/waves/round-73/w1/build/ScribeSourcesCorrection`)

```
$ wc -l < entry.md                      → 11          (limit 12)
$ grep -cE '^ {0,3}\|[[:space:]]*S[0-9]' entry.md   → 0   (no registry row)
$ grep -cE '^[[:space:]]*\|' entry.md   → 0           (no row of any kind)
$ grep -cE '^\|' entry.md               → 0
$ grep -cE '^## ' entry.md              → 0           (no heading)
$ grep -c '##' entry.md                 → 0           (no heading marker anywhere, even mid-line)
$ printf '%s' '2026-10-24 — placement correction (appended by the L1 in wave 2)' | wc -w → 11
$ printf '%s' 'originally landed at EOF under' | wc -w → 5
```

Registry side-effect: the lane's S-id row count is `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]' corpus/SOURCES.md`
→ `142` today; the draft contributes 0, so appending it leaves 142. I did not run `census validate` before
or after (plan line 36) — that gate reads `../` fleet-root paths and belongs to the L1's landing, not this
seat.

## S4 — D4: what `,.` actually is (correction to the r72 spot-check's characterisation, quoted verbatim)

The r72 spot-check, `corpus/lessons/round-72-verifier-spotcheck.md:44-46`, says verbatim:
`**D4 admitted entry carries a garbled bullet:**` / `` `corpus/knowledge/resident-index-and-rungs-round72.md:45` — "Check the harness's house standard before the format's,." (dangling comma/period). ``
Line 137 of the same file says verbatim: ``4. Fix `resident-index-and-rungs-round72.md:45` ("format's,.").``

That is the symptom, not the cause. The wave-1 draft of the same bullet,
`.ufo/waves/round-72/w1/build/ScribeEntryRung/resident-index-and-rungs-round72.md:64`, reads:

```
- **Check the harness's house standard before the format's, and let portability pick the middle rung.**
```

and its draft body carried an extra sentence with F8 (`skills, not always-on files or prompts, are what
travel between agents (F8)`). The landed entry kept neither: `grep -c '^| F' corpus/knowledge/resident-index-and-rungs-round72.md`
→ `7` (last row `26:| F7 | Hermes Agent | S216 | …`) and `grep -c -i portability corpus/knowledge/resident-index-and-rungs-round72.md`
→ `0`. So `,.` is a truncation at the draft's comma, and the landing edit deliberately dropped the F8 /
portability half — restoring it would be a claim edit, which plan lines 37-38 forbid verbatim
(`(a lane-authored entry typo, not a claim edit; the verified-at/quote lines are untouched)`).

Exact replacement line for `:45` (draft file `log-note.md`):

```
- **Check the harness's house standard before the format's rules.**
```

`rules` is the noun the landed bullet's own continuation (lines 46-47: the 60-character description cap and
"forbids commands the agent cannot run (F7)") enumerates. Rejected: (a) delete the comma only — leaves an
elliptical headline with no head noun; (b) restore the draft's `, and let portability pick the middle rung`
— imports a claim the landed F table (F1-F7) does not carry. Both rejections are evidenced above, not
asserted.

One-line `LOG.md` note (append after the current Round 72 block, matching the `- <date> — round N:` form):

```
- 2026-10-25 — round 73: repaired the r72 closure-defect D4 typo at `corpus/knowledge/resident-index-and-rungs-round72.md:45` — "before the format's,." → "before the format's rules." (the bullet's own continuation names those rules: F7's 60-char description cap and no-invented-commands clause; the wave-1 draft's dropped ", and let portability pick the middle rung" is not restored, because the landed F table ends at F7 and the entry carries no portability finding. Quotes and `verified-at` lines untouched.)
```

Scope note: the garbled token appears in exactly three lane files —
`grep -rn "format's,\." --include=*.md .` → the entry at `:45`, the spot-check at `:46` and `:137`, and
`plans/round-73.md:37` (the frozen plan's own citation). Only `:45` is rewritten; the other three are
citations of the defect and stay.

## S5 — calibration / limits

- Observed: all line numbers, hashes (`c69711e`, `a0f7f17`, `e8207c6`, tip `ac8fc59`), heading counts, row
  count, word counts, and the four `grep -c` form proofs above, all run in this seat.
- Not observed: whether the L1's `census validate` stays exit 0 after the append (gate not run, out of
  scope); whether any other wave-1 seat drafts a competing note for the same block; whether the stray
  `## Leads (unopened)` at `:217` / `:281` should get their own appended notice — the draft names them as
  pre-existing and leaves them for a later round, because repairing them is a rewrite of filed bytes.
- Not done, deliberately: no `pacman`, no `uv`/`npx` install (nothing needed); no fixture repo; no
  `/tmp` scratch; no git write of any kind; no jj.
