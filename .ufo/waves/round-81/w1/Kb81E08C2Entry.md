# Kb81E08C2Entry — C2 entry build (round 81, w1)

Seat: leaf executor, no subagents, no background jobs beyond my own tool calls. Lane `kotoba-shokunin`, base
`b284223105f4d106f7e8f56ed4fd296c643cda0e`. Nothing in the lane was edited, staged, committed or checked out;
the lane git was read-only (`git grep`, `git ls-files`) and the one mutation-bearing fixture was a self-made
scratch clone whose `git rev-parse --show-toplevel` was asserted to be the clone itself.

Skill read first: `skill://godspeed`. Axes I named before working, and what each move bought:
**depth** (a seventh surface plus five mechanisms the r80 six-surface table has no column for),
**consistency** (every quoted span stated in one declared text view and re-located in committed bytes),
**calibration** (a located quote that actually occurs in the view, 13 words, containing `allowedTools` —
not the r80 string that does not), **operability** (the L1 gets ready-to-land cells, a census-validated row,
and a pre-flight against another seat's reference counter), **freshness** (double fetch, digest pinned,
cross-round byte identity, a runnable recheck that prints the digest and the occurrence count).

## What I built

1. `.ufo/waves/round-81/snapshots/S249.md` — the served page, raw bytes, 28 395 B,
   sha256 `ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2`.
2. `.ufo/waves/round-81/snapshots/S249.fetch.json` — the fetch record in the r79/r80 shape (`id`, `url`,
   `final_url`, `http`, `bytes`, `sha256`, `fetched_utc`, `ua`, `note`).
3. `.ufo/waves/round-81/snapshots/S249.manifest` — the per-snapshot pin line, same shape as r79's per-file `.manifest`.
   I did **not** write a directory-level `MANIFEST.sha256`: sibling seats add snapshots to this directory, so an
   aggregate written now would be stale on arrival (recorded in the integration-cells file as a do-not).
4. `.ufo/waves/round-81/build/allowed-tools-sdk-round81.md` — the entry, to be copied verbatim to
   `corpus/knowledge/allowed-tools-sdk-round81.md`. Header block: two `source:` lines (S249 with canonical URL +
   both section anchors + snapshot path + sha256 + fetch record; S248 because this entry is what its `used-by` moves to),
   `verified-at: 2026-10-27`, a runnable `recheck:`, a `ground:` line, then the declared text view.
   Body: a ten-row channels table (`channel | form | where | what it says | located span`), the page's own words
   span by span, a two-spellings section, the surrounding defaults, five negatives with their sweeps, Limits,
   Scope, Related.
5. `.ufo/waves/round-81/build/Kb81E08C2Entry.integration-cells.md` — the exact TEXT for the cells I may not edit
   (write scope excludes `corpus/`, `SKILL.md`, `PROVINCE.md`, `verifiers/`): the 11-cell S249 row, the single S248
   `used-by` cell old→new, the SKILL.md rule sentence, the counter registry row, the `corpus/README.md` coverage row,
   the `PROVINCE.md` `## Core` bullet, plus landing order and two do-nots.
6. Receipts in `.ufo/waves/round-81/build/`: `Kb81E08C2Entry-quoteprobe.txt`, `Kb81E08C2Entry-entrycheck.txt`,
   `Kb81E08C2Entry-sweeps.txt`, `Kb81E08C2Entry-census-scratch.txt`, `Kb81E08C2Entry-refcounter-preflight.txt`.

## Fetch and pin (freshness)

```
curl -sS -L -A 'Mozilla/5.0' --max-time 60 -o f1.md -w 'http=%{http_code} bytes=%{size_download} redirs=%{num_redirects}\n' https://code.claude.com/docs/en/agent-sdk/skills.md
   -> http=200 bytes=28395 redirs=0 final=https://code.claude.com/docs/en/agent-sdk/skills.md
(same command, f2.md, 1 s later) -> http=200 bytes=28395 redirs=0
sha256sum f1.md f2.md -> ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2  (both)
cmp f1.md f2.md -> rc=0
```
`date -u` at fetch time: `2026-10-28T02:27:26Z`; host local time `2026-10-27 23:27 -0300`, which is the round's
`opened`/`verified-at` date. The record states both rather than back-dating the UTC field.
Cross-round freshness: the same 28 395 B and the same digest are what r80's scout seat saved at
`.ufo/waves/round-80/build/Kb80S05-agent-sdk-skills.md` (I hashed that file myself: identical), so the page is
byte-identical across two rounds and two fetchers; the pin is the committed snapshot, never the URL.
The page states no revision, commit, last-modified or build id for itself — `grep -ci 'last-modified\|revision\|build id'`
over the commit-ready snapshot prints `0` (it names two version floors for other behaviours, raw lines 104 and 166).

## Located quote (calibration)

The plan's conjunct (d) wants a quote of ≤25 words carrying `allowed-tools`/`allowedTools` that occurs in the
snapshot's text view after the first heading. The r80 S248 row's first quoted string
(`… the skill's allowed-tools frontmatter or with the allowedTools option`) occurs **0** times in that view,
because the page wraps the frontmatter key in a Markdown link and the view keeps link targets. My entry's located
quote is the link-free span on the same raw line:

> `frontmatter or with the allowedTools option (allowed_tools in Python) in your query configuration`

13 words, contains `allowedTools`, exactly **1** occurrence in the view (view line 234, raw line 348), after the
view's first heading (view line 3, `# Extend agents with skills`), and not on the heading line nor the line after it.
Text view used: the round-80 counter's own implementation
(`.ufo/waves/round-80/build/check_allowed_tools.py`, `view_with_headings` / `ws`) — Markdown arm: backticks deleted,
unordered-list marker removed, whitespace collapsed — so the spans are stated in the same view the frozen counters apply.

Receipts: `Kb81E08C2Entry-quoteprobe.txt` (10 located spans + 1 expected negative: words, occurrences, raw line,
view line per span) and `Kb81E08C2Entry-entrycheck.txt` (self-attack over the finished entry: every double-quoted
span extracted, **30 spans checked, 0 failing** — each 1 occurrence, each ≤25 words, no backticks inside a quote).

## Negatives the entry claims, and their sweeps

`Kb81E08C2Entry-sweeps.txt`, each line the grep command's own exit status:
`precedence` 0, `priority` 0, `wins` 0, `override` 0, `clears` 0, `cleared` 0, `next message` 0, `unknown tool` 0
(all exit 1 = no match, which is the claim), `default` 3 (exit 0; raw 22, 28, 121 — none a tool default),
`subagent` 2 (exit 0; raw 24, 516 — neither about this option).
Base-state ground sweep, lane git read-only: `git grep -c 'allowedTools' b2842231 -- corpus/knowledge` prints two
files (`agent-definition-files-round56.md` 2, `chinese-vendor-skill-surfaces-round73.md` 1) and
`git grep -c 'allowed_tools' b2842231 -- corpus/knowledge` prints one (`allowed-tools-surfaces-round80.md` 1, its own
ground-line grep pattern). No base entry names an SDK session, a query-config option or an auto-allow relation.

## Operability: the proposed row and cells were measured, not asserted

Scratch clone at base, entry + snapshot + the exact integration-cell text applied, then:

```
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file <clone>/corpus/SOURCES.md --today 2026-10-27
  -> exit 0; E-codes 0 (base 0); W-codes 31 -> 32; the new line is
     file  W04  S249 duplicate url code.claude.com/docs/en/agent-sdk/skills.md across scopes
diff --stat -> corpus/SOURCES.md | 3 ++-   (1 insertion of S249, 1 cell changed on S248, no other cell touched)
```
That single new warning is the census's named warning class for the same URL under a distinct scope, and it matches
the r81 sentinel's independently measured A2 outcome (`Kb81N01Sentinel-census-decision-table.txt`); the error class
E04 fires only for same URL + same scope without a `supersedes` clause, which this row is not. A `queued` row carrying
a real `used-by` is accepted (E11 resolves the target's existence, nothing more), which is what the plan needs for
S248: the row keeps `status: queued` and only its last cell changes.

Pre-flight against another seat's instrument (explicitly **not** a claim after-value; the instrument is seat
Kb81E07C2Worlds's PROVISIONAL inline `ref-counter.py`, not the lane's counter):

```
python3 -B .ufo/waves/round-81/build/Kb81E07C2Worlds.ref-counter.py --repo <clone> --rev 1692ce1e40345dedab49d17b2cf90b49dc5ece88
  -> sdk allowed-tools surface documented 1 of 1
     snapshot sha256: ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2
     located quote: frontmatter or with the allowedTools option (allowed_tools in Python) in your query configuration
     exit 0
```
Its first run on the same fixture printed `0 of 1` with three findings, two of which were fixture defects I created
(snapshot copies not yet placed in the clone; and my README cell wrote `knowledge/…` while that reference checks the
repo-relative entry path). The second one is a real finding about the integration text, and I fixed it in the
published cell: the description cell now also carries `entry corpus/knowledge/allowed-tools-sdk-round81.md`. Both runs
are in `Kb81E08C2Entry-refcounter-preflight.txt`.

The header `recheck:` was executed as written
(`u=https://…; f=$(mktemp); curl -fsSL -A Mozilla/5.0 --max-time 60 "$u" -o "$f" && sha256sum "$f" && tr -d '\140' < "$f" | grep -c -F "<quote>"`):
printed the digest line and `1`, exit 0, on a third independent fetch.

## What changed versus r80, and what I consumed

- **Consumed** `.ufo/waves/round-80/build/Kb80S05-agent-sdk-skills.md` (byte-identical to my fetch; freshness evidence),
  `.ufo/waves/round-80/w1/Kb80S05SourcesEdits.md` (row provenance, the E11 ordering dependency, the W04 class), and the
  r80 counter's `view_with_headings`/`ws` as the declared text view.
- **Changed**: the r80 S248 row's located quote is not repeated — it cannot be located in the view (0 occurrences, link
  shaping). This entry states the span that does occur, and records the defect in Limits rather than repairing the row,
  because the plan changes exactly one S248 cell this round.
- **Shape sources, stated because the seat named `.ufo/waves/round-80/snapshots/` and that directory does not exist**:
  I took the fetch-record and per-snapshot `.manifest` shapes from the tracked r79 directory
  (`.ufo/waves/round-79/snapshots/S227.fetch.json`, `S230.fetch.json`, `S227.manifest`, `MANIFEST.sha256`) and the
  r80 page bytes from `.ufo/waves/round-80/build/`, which is where r80's scout actually wrote them. Derived, not copied,
  is nothing: the record fields are the r79 ones, and the round-80 directory's absence is a fact I am recording rather
  than working around silently.
- **Not consumed**: `Kb80E04DeadPointer.patch` and `Kb80E05GrammarFix.patch` are C1 instrument repairs (report-pointer and
  external-commit classification); they do not touch the C2 surface, so I read neither. If the L1 expects a C2 seat to
  have an opinion on them, that expectation is unmet by design, not by omission.
- The entry cites only S249 and S248 as `S###` ids. I deliberately do **not** write the id of the CLI skills page whose
  section the SDK page links, because a counter that requires every cited id to be a `mined` row with `used-by` naming
  the entry would fail on it; that page is described in prose instead. S248 is the one unavoidable id (conjunct (e)),
  and its `status` stays `queued` per the plan — flagged to seat Kb81E09C2Counter as a possible plan/counter tension.

## Risks

1. **S248 stays `queued` while its `used-by` names this entry.** Evidence: the census accepts it (E11 only wants the
   target to exist), and the plan forbids changing other cells. If the landing counter demands `mined` for every cited
   id, the fix is a plan-level decision, not an entry edit.
2. **The pin is stated twice by design** (counter constant and `S249.fetch.json`; the row's anchor carries the same
   digest and byte count). A re-fetch that returns a different digest invalidates all ten spans at once; the header
   recheck measures that, and the snapshot is the pin.
3. **The `.md` route only.** The HTML rendering of the same route was not read; the entry says so and claims nothing
   about it.
4. **Word floor.** The plan states a cap (≤25) only; the reference counter I pre-flighted with imposes a 3-word floor.
   The primary quote is 13 words and the longest span is 16, so both readings pass.

## Blockers

None. No tool was installed or upgraded, so there is no tooling line to record beyond that.

Scratch `/fast/scratch/hyaku/kotoba-r81/Kb81E08C2Entry` was created and removed after every receipt above was copied
into `.ufo/waves/round-81/build/`; no `/tmp` path is cited anywhere.

VERDICT: C2 entry built and pinned (S249 snapshot 28395 B / ac62c2df…, located quote 13 words, 1 occurrence in the declared view), 30/30 quoted spans re-locate, proposed S249 row censuses clean at exit 0 (E 0, W04 +1 warn) in a scratch clone, and another seat's reference counter reaches 1 of 1 there — no lane file edited, no after-value scored.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/allowed-tools-sdk-round81.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E08C2Entry.integration-cells.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E08C2Entry-quoteprobe.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E08C2Entry-entrycheck.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E08C2Entry-sweeps.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E08C2Entry-census-scratch.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E08C2Entry-refcounter-preflight.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/snapshots/S249.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/snapshots/S249.fetch.json, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/snapshots/S249.manifest
