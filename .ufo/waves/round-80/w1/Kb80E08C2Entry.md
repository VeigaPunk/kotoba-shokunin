# Kb80E08C2Entry — C2 knowledge entry (round 80, wave w1)

Leaf executor seat. Lane `/home/vgpnk/Projects/shokunin/kotoba-shokunin`, base
`398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93` (HEAD `c2f69d4f…`). No lane file was edited,
no commit/stash/checkout in the lane, no subagent dispatched. Everything below was measured
in my scratch clone `/fast/scratch/hyaku/kotoba-r80/Kb80E08C2Entry/clone` (a `--shared` clone
at the base) or against the lane's committed bytes read-only.

## Deliverable

`/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/allowed-tools-surfaces-round80.md`
— 24865 B, 159 lines, sha256 `caadf57d6ba02de6ffdcd5d2d8bea33f0dbe79dadc85d7d33ef075251ad1df15`.
It is a **file body, not a patch**: the L1 places it at
`corpus/knowledge/allowed-tools-surfaces-round80.md`.

Shape, in the order the plan § C2 requires:
`source:` lines for S226–S231 (six, each carrying the r79 row report's located quote verbatim
and the snapshot basename in backticks) → `verified-at: 2026-10-27` → `recheck: 30d — <the r79
recheck command shape>` → the frozen surface table (header `surface | source | page tokens |
grant | located quote`; first cells Open specification, Claude Code, Factory, Microsoft Agent
Framework, pi, Mistral Vibe; grant cells the frozen labels `experimental`, `pre-approves`,
`metadata-only`, `experimental`, `experimental`, `unstated`) → the divergence matrix → the
semantics matrix and the cross-client conflict reading → Limits.

Receipts: `.ufo/waves/round-80/build/Kb80E08C2Entry-receipts.txt` (600 lines, sha256
`fd886959d95d2213f6bf7cb3d3123f4f926f4daf3e1681e0e5f765542d92e111`) — every command's
own exit status, no pipeline verdicts.

## Behaviour and evidence

### The six located quotes, located byte-level in the pinned snapshots

I re-located every quote myself with the r79 draft counter's own `text_view`/`quote_location`
functions (`.ufo/waves/round-79/build/check_allowed_tools.py`, sha256 `74e067cc…`), so the
shaping is the counter's, not a re-implementation. Per-surface offsets (receipt §4):

| surface | words | text-view offset | raw byte offset | Q70 location |
|---|---|---|---|---|
| spec (S226) | 15 | 4267 | — | ok |
| claude (S227) | 25 | 67523 | 68988 | ok |
| factory (S228) | 22 | 12533 | 12928 | ok |
| msaf (S229) | 19 | 3938 | — | **fails** (see F1) |
| pi (S230) | 6 | 3414 | — | ok |
| vibe (S231) | 6 | 37473 | — | ok |

All six carry the word-bounded token `allowed-tools` (5–25 words) and their surface's frozen
page token; all six occur **once** in their own snapshot's text view and none occurs in
another snapshot's view (the Q70 shared-banner check). The four "—" rows exist only after the
declared text view (backticks deleted, list markers removed, whitespace collapsed) — the raw
bytes carry the markers — which is exactly why the entry names the shaping on its own line.

Pin cross-check: the six per-id `.manifest` files verify `OK` under `sha256sum -c`, and
`git show <base>:.ufo/waves/round-79/snapshots/<file>` hashes to the same six digests, so the
committed bytes at the base are the pinned bytes.

### The entry conforms to the counter's entry-level rules

Measured with the counter's own functions (receipt §5): `entry_problems: none`; six `source:`
lines then `verified-at` then `recheck` in order; the text-view shaping named; exactly one table
with the frozen header; six rows in the frozen surface order, five cells each; every row
carries a key token (`allowed-tools`), a value token and a grant token, all occurring
word-bounded in its own snapshot; every grant cell plain-text with exactly its frozen label.

### End-to-end measurement in the scratch clone

Stack: base clone + my entry + `Kb80S05SourcesEdits.patch` (the six `used-by` cells) +
`Kb80S09SkillRule.patch` + `Kb80S10Province.patch` + `.ufo/waves/round-79/snapshots/MANIFEST.sha256`
+ the published counter, with only `ENTRY` and `TARGET` retargeted at the round-80 entry (scratch
copy; `SELF_SHA` refilled for the copy). The six SOURCES anchor cells were rewritten into the
counter's `FETCHED_RE` form **in the scratch clone only** — the lane's `corpus/SOURCES.md` was
never touched.

Result with the published draft counter (receipt §9):

```
allowed-tools surfaces backed 5 of 6
script-only world: 0 of 6
opened this round 6 of 6
province surfaces named 6 of 6
skill rule line ok
registry home ok
  msaf: S229-msaf.html: quote lies in the first-heading block (Q70)
```

The generator world reaches 0 of 6, so the form claim does not rest on form generation (Q74).

### F1 — the msaf surface is structurally inadmissible under the draft counter's Q70 (counter defect, not an entry defect)

The draft's `quote_location` (r79 draft `:885`–`:897`) finds the page's first heading by
scanning the **text view** for a line starting with `#`. That heuristic is Markdown-shaped. For
an `.html` snapshot the tags are stripped, so the view has no `#` headings at all and the first
`#`-prefixed line it finds is a **Python comment inside a code sample**: view line 168,
`# Auto-approve load_skill and read_skill_resource, but not run_skill_script.` The predicate
then bars any quote starting at or before `first_head+1 = 169`.

The constraint is unsatisfiable for S229 (receipt §10):
- S229 names the field **exactly once** — raw bytes: 1 occurrence at line 818; text view: 1
  occurrence at line 95. No other spelling exists: the case-insensitive sweep for
  `allowed[-_ ]tools` over the text view returns exactly one form, `allowed-tools`, count 1.
- Conjunct (f) requires the quote to carry the word-bounded token `allowed-tools`, so any
  admissible quote must contain that single occurrence and must therefore start at or before
  view line 95.
- Q70 requires it to start at or after view line 169.
- 95 ≤ 169, so **no admissible msaf quote exists**. No narrowing can pass it.

The page's real structure says the quote is fine: the first heading is
`<h1 id="agent-skills">Agent Skills</h1>` at raw line 676, and the field row is at raw line 818
inside the `<h3 id="skillmd-format">` section opened at raw 771 — the quote is well after the
first heading. The defect is that the detector cannot see an HTML heading.

**Proof that the entry is complete and the predicate is the cap.** I re-ran the counter's own
`check()` with **one** change — the heading detector made snapshot-shape aware (for an `.html`
snapshot, the first `<h1>`–`<h6>` line of the raw bytes, mapped into the text view; the raw
`<h1 id="agent-skills">Agent Skills</h1>` maps to view line 1) — and with nothing else changed
(receipt §9):

```
with the DRAFT quote_location:        backed 5 of 6, opened 6 of 6
with a SHAPE-AWARE quote_location:     backed 6 of 6, opened 6 of 6
backed surfaces: ['spec', 'claude', 'factory', 'msaf', 'pi', 'vibe']
```

So the entry reaches 6 of 6 the moment the heading detector is shape-aware, with the same entry
bytes, the same registry rows, the same manifest and the same snapshots. I did **not** narrow,
reword or swap the msaf quote to dodge the predicate, and I did not edit the counter (not my
seat). The fix belongs to the counter seat (E07) as a pre-freeze heading-model erratum; the
mechanical generator inherits the same `first_head` logic and will need the same repair.

### F2 — the entry adds no token to any corpus-gate class

The corpus gates read a commit citation with `COMMIT_RE` = `(?<![A-Za-z0-9_-])commit[ \t]+`([^`\n]+)``
(`verify_corpus_integrity.py:151`), and a report pointer with `UFO_POINTER_RE`. I scanned the
entry's bytes with **the gates' own regexes** (receipt §7): **0 commit-shaped citations and 0
report pointers**. The only 40-hex token left in the file is the lane base commit
`398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93` in the `ground:` line, cited as "at base `398cbe1…`"
— not the `commit `…`` grammar, and it resolves in the lane. The entry therefore adds nothing
to `commit_total` / `commit_unresolvable` / `commit_truncated` / `commit_nonhash`, and
independently confirmed by E10, G01 and S08.

This mattered: my **first** draft carried the full-hex third-repository commit
`7bb48f213ac677f943d5c791199ed3dddf302f00` in a Limits bullet (and the pi-mono hashes
`bb65e3e4…` / `25cc5c7b…`). E10Battery, V02C2 and S01Lesson flagged that hazard before
integration, and my own gate scan confirmed it: under the current classification that line
reads `commit_unresolvable`, so landing the entry would have added a **third** unresolvable
token to the corpus gates and left them red. The bullet now cites the pinned snapshot and the
fetch record by name and asserts no third-repository digest at all.

### F3 — the counter's pin binding is per line, and the entry satisfies it

The counter's `snapshot_name` (r79 draft `:730`–`:756`) scans **every** line containing a sid
and collects every backticked pinned basename on those lines; two basenames on one line make
**both** sids ambiguous → `EnvError` → exit 2. My first draft put two snapshot names on four
prose lines (and five on one), which would have made the whole measurement exit 2.

I found them by scanning, split every such line, and re-measured (receipt §6): each of S226–S231
now binds to exactly one snapshot — S226→`S226-spec.md`, S227→`S227-claude.md`,
S228→`S228-factory.md`, S229→`S229-msaf.html`, S230→`S230-pi.md`, S231→`S231-vibe.md` — 0 fails.
The six `source:` lines still carry the full basename and the matching URL, so the row↔page
binding the counter checks is intact.

### F5 — the generator world stays at 0 of 6, so the Q70 repair cannot create the counter defect

`first_head` is used **twice** in the draft: by `quote_location` (the Q70 admissibility check)
and by `_mech_quote`'s body window (`body = lines[first_head + 2:]`), so a heading-model repair
moves both the entry's admissibility and the mechanical generator's window. The sentinel raised
the hazard that the repair might let the generator reach the target, which under the counter's
own exit rule (`m < TARGET`) would make the counter print its defect line and exit 1. I measured
all three states on the scratch clone's committed bytes (receipt §11):

| counter state | N (entry-backed) | M (generator) |
|---|---|---|
| the draft as published | 5 of 6 (opened 6 of 6) | **0 of 6** |
| shape-aware heading in the Q70 arm only | **6 of 6** (opened 6 of 6) | **0 of 6** |
| shape-aware in both places (the complete repair) | **6 of 6** (opened 6 of 6) | **0 of 6** |

M stays 0 of 6 in every state, and the counter's own code says why (receipt §11): the generator
world is held at 0 of 6 by two mechanisms, neither of them the heading window. The generator's
mechanical quote is `None` for five of the six surfaces (their field occurrence sits before the
body window), and the generator writes the no-judgement grant label `unstated` for every row,
while a row is only backed when that label equals the surface's **frozen** label — so the one
row that does get a mechanical quote is rejected as "grant label 'unstated' is not factory's
frozen label 'metadata-only'". The generator world's own per-surface findings are exactly that.

So the shape-aware repair is safe against the plan's kill rule: it takes the entry to 6 of 6 and
leaves the generator at 0 of 6. This is a measurement, not a claim score — the frozen round-80
counter is not in the lane yet, and the repair belongs to the counter seat.

### F4 — the base SOURCES row S230 cites the wrong repository's commit (erratum, not edited)

Reproduced from committed bytes (receipt §11):
- `corpus/SOURCES.md:171` (S230, the pi-mono row) reads "page revision `main` resolved to
  `badlogic/pi-mono` commit `7bb48f213ac677f943d5c791199ed3dddf302f00`".
- `.ufo/waves/round-79/snapshots/S230.fetch.json` records main at fetch time =
  `bb65e3e49710fbd14f10c7792d0eaa6e2b2c5923`, last commit touching the path =
  `25cc5c7bf4cbc76b2e134c729eb8d57d521ed749`, blob sha1 `19d2bf28910ce49caaaf4dde86d1e96330ca7b31`.
- `.ufo/waves/round-79/snapshots/S231.fetch.json` records "'main' resolved to commit
  `7bb48f213ac677f943d5c791199ed3dddf302f00`" — so `7bb48f21…` is **mistral-vibe's** commit.

The page bytes are right (the pinned `S230-pi.md` hashes to `5b980552…`, the recorded
pi-mono blob); only the commit citation is wrong, copied from S231. E12Census independently
confirmed it harder: the cited commit is absent from pi-mono (`git fetch` → "not our ref";
GitHub API 422) and present in mistral-vibe (API 200).

`corpus/SOURCES.md` is outside my write scope and the round's frontier step forbids touching the
anchor cell, so this belongs in the round-80 lesson as an erratum line (never an in-place
rewrite). Suggested wording, from S05SourcesEdits: *"S230 anchor erratum (round-80): the row
cites pi-mono commit `7bb48f21…`; its own fetch record records main at fetch as `bb65e3e4…`
(blob sha1 `19d2bf28…`), and `7bb48f21…` is mistral-vibe's commit (recorded correctly by
S231). Page bytes are right (sha256 `5b980552…`); only the commit citation is wrong."*
My Limits section states only what the fetch record supports — that the served revision was
older than the head — and asserts no hash. F6 adds a second clause to the same erratum line:
the row's recorded quote ("Experimental pre-approved tool list") is a 4-word cell fragment
without the field key, which cannot be repaired in place because the census requires 11 cells
and a literal `|` in a cell makes 12.

### F6 — the S230 registry row's recorded quote is not a located quote, and it cannot be repaired in place (census landmine)

`corpus/SOURCES.md:171` (S230) records its located quote as **"Experimental pre-approved tool list"** — 4 words, under the counter's 5-word floor, and carrying no `allowed-tools` token. The other five C2 rows record 15/25/22/19/6-word quotes that all carry the key. I measured this over the six rows' anchor cells (receipt §11).

Three facts decide what it means, and each is measured:

1. **It is not counter-load-bearing for C2.** The counter reads the located quote from the **entry's**
   surface row (`quote_of(row)` → `row[4]`), never from the registry row's anchor cell. No gate reads
   a registry anchor's quote at all: the census contains 0 occurrences of "located quote", and
   `verify_corpus_integrity.py` / `verify_corpus_independent.py` likewise. My entry carries the
   admissible 6-word pi quote in the entry cell, in the pipe-escaped form the counter's escape-aware
   cell splitting expects, and the counter's own `quote_of` reads it at 6 words with the key.
2. **It cannot be repaired in place.** The census splits a registry row naively on `|` and requires
   11 cells (NF=13). I inserted the pipe-bearing 6-word quote into a scratch copy of S230's anchor
   cell and re-ran the census: **`file E01 S230 fields=12`**. So an in-place "fix" of this cell would
   red the census — the opposite of a fix.
3. **The split is by design and was documented at draft time.** `Kb79R05PiRow.rows.md` § Hazard 1
   states that the vertical bar cannot live inside a registry cell, and the pi page names the field
   exactly once, inside a markdown table row — so every admissible pi quote necessarily contains the
   bar. The r79 seat therefore put the cell fragment in the registry row and the pipe-bearing form in
   the entry row.

So S230's registry row carries two defects of the same family — the wrong repository's commit (F4) and
a recorded quote that is not a located quote under the counter's reading — and both sit in a cell the
append-only rule protects and the census's cell-count rule forbids editing naively. The lesson erratum
is their home, and the erratum should state the pipe constraint so a later round does not attempt the
in-place edit and red the census. I edited no corpus file.

### Other findings reported, not repaired

- **`.ufo/waves/round-79/snapshots/MANIFEST.sha256` does not exist** at the base or at HEAD
  (18 committed files in that directory: six snapshots, six `.fetch.json`, six `.manifest`). The
  counter's `MANIFEST` constant names that path and `Repo.manifest()` raises `EnvError`
  ("snapshots are unpinned") when it is absent, so conjunct (c) cannot be evaluated until it is
  committed. The sentinel's `Kb80N01Sentinel-MANIFEST.proposed` holds the correct six pins
  (content = the per-id `.manifest` files verbatim); I verified those six digests against the
  committed snapshot bytes at the base.
- **The six committed SOURCES anchor cells do not match the counter's `FETCHED_RE`** — they
  write `fetched 2026-10-27, HTTP 200, 7608 B, sha256 `9a67…`` (a date without a time, and a
  backticked digest) where the regex wants `fetched <ISO8601>Z, HTTP 200, <bytes> B, sha256 <hex>`.
  I measured this independently (0 of 6 match) and confirmed it by the dry-run: with the anchors
  in the regex's form the same entry moves from 0 of 6 to 5 of 6, and the only remaining finding
  is F1. The rewrite belongs to the SOURCES owner (S05) or the L1; I did not edit the lane.
- **The recheck command, run live on 2026-10-27, prints `1 1 2 1 1 1` and exits 0** — the same
  six numbers the r79 skeleton recorded, in the order spec, claude, factory, msaf, pi, vibe
  (receipt §8). The factory anchor occurs twice in the served HTML and once in the same page's
  Markdown route. The entry's recheck line states that the predicate is the anchor-token count
  and not a digest, because the Microsoft Agent Framework page is served non-deterministically.

## Limits of my own evidence

- I did not install, load or run any client; every grant statement is documentary, read from
  the pages' own words. "Pre-approved", "does not add tools" and "Experimental" are quotes, not
  observations of a runtime.
- The counter I measured against is the published r79/r80 draft (byte-identical, sha256
  `74e067cc…`) with `ENTRY`/`TARGET` retargeted in a scratch copy; the frozen round-80 counter
  is not yet in the lane, so the headline `allowed-tools surfaces documented N of 6` has not been
  produced by the frozen bytes. **My 6 of 6 is a diagnostic measurement of the entry against the
  draft's own `check()` with one predicate repaired — not a claim score.**
- The msaf finding is a structural argument over the draft counter's code and the committed
  snapshot bytes; it says no admissible quote exists under that predicate, not that the page
  fails to document the field.
- The 18-page census and the round-79 negative sweep are not restated in this entry; the
  negative sweep is re-run in round 80 by its own seat.
- No snapshot was committed by me and no `corpus/` file was edited.
- The entry is not yet in the lane (`corpus/knowledge/allowed-tools-surfaces-round80.md` does
  not exist at the base), so no non-author can yet re-run the two token scans against the landed
  tree; the scans in this report are against the published build bytes.

## For the L1, in dependency order

1. Commit `.ufo/waves/round-79/snapshots/MANIFEST.sha256` (the sentinel's
   `Kb80N01Sentinel-MANIFEST.proposed` content — the six per-id `.manifest` files verbatim; I
   verified those six digests against the committed snapshot bytes). Without it the counter's
   conjunct (c) raises `EnvError` and exits 2 before scoring, and the SKILL.md registry row's
   pinned-values cell names that path.
2. Land the entry at `corpus/knowledge/allowed-tools-surfaces-round80.md`.
3. Land the six `used-by` cells (`Kb80S05SourcesEdits.patch`) and the tree rows
   (`Kb80S09SkillRule.patch`, `Kb80S10Province.patch`) — all three already measured green in
   my dry-run: opened 6 of 6, province 6 of 6, skill rule line ok, registry home ok.
   `Kb80S08ReadmeRows.patch` must land in the same commit as the round-80 lesson: its coverage
   map carries a row for `corpus/lessons/round-80.md`, and that file exists at neither the base
   nor the current tip (I checked all three: base, HEAD, worktree — all ABSENT), so the row
   would read as a missing path if the lesson had not landed with it. With S08's rows applied
   and my entry tracked I measured `corpus.index.unindexed = 0` (detail empty), so no extra
   coverage row is needed for my file.
4. Rewrite the six SOURCES anchor cells into the counter's `FETCHED_RE` form
   (`fetched <ISO8601>Z, HTTP 200, <bytes> B, sha256 <hex>` — no backticks around the digest).
   They are the only remaining non-Q70 blocker I measured: with them in that form the same entry
   moves from 0 of 6 to 5 of 6.
5. The counter seat's shape-aware heading repair (E07) takes it the last step to 6 of 6, with
   the generator world still at 0 of 6 (F5). If the repair does not land, C2 stops as an honest
   stop at 5 of 6 with the headline withdrawn — the plan's kill rule, not a narrowing.
6. Record the S230 anchor erratum in the round-80 lesson (never an in-place anchor edit), and
   re-run the baseline refresh after the files land.

## Touched surfaces

- `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/allowed-tools-surfaces-round80.md`
  — the entry (new file).
- `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E08C2Entry-receipts.txt`
  — the verification receipts (new file).
- `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/w1/Kb80E08C2Entry.md`
  — this report (new file).
- Scratch only (removed before yield): `/fast/scratch/hyaku/kotoba-r80/Kb80E08C2Entry/`.

VERDICT: The C2 entry is built and byte-verified — six located quotes located in the pinned snapshots, every counter entry-level conjunct satisfied, no corpus-gate token added, one pinned basename per line, and 6 of 6 under the counter's own check() once the heading detector is shape-aware (with the generator world still 0 of 6); the msaf surface is structurally inadmissible under the draft Q70 predicate, which I report as a counter defect (no admissible quote exists) and did not narrow around, alongside an unedited base SOURCES row that cites another repository's commit.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/allowed-tools-surfaces-round80.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E08C2Entry-receipts.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/w1/Kb80E08C2Entry.md
