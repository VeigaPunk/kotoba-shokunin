# ScribeSOURCES — round-66 SOURCES.md addition audit (read-only)

Seat: `ScribeSOURCES`, leaf member, no subagent dispatch. No product file, registry row,
counter, threshold, plan, receipt or VCS state was edited. The only write is this report.
No tool was installed or upgraded (none needed).

## Revision pins

- Plan-pinned base: `11385e04e368c1e94ab1a5a89d7439033eb1f855` (round-65 verifier spot-check).
- Measured lane tip (git HEAD at read time): `2a8eba56b3f9321b70c569fa2816d42237ca49a2`
  (`round-66 verifier spot-check (integrator, hyaku): non-author admit/reject`).
- `corpus/SOURCES.md`, `corpus/lessons/round-66.md` and
  `corpus/knowledge/fleet-commit-resolution-round66.md` are clean against HEAD
  (`git status --porcelain` on the three paths prints nothing). One unrelated tracked
  modification exists in the working tree: `.ufo/waves/round-66/w1/swarm-registry.json`.
- `jj` working-copy change is `omvyzpnszwon 98c994b017ca`; the audit below reads the
  working tree at git HEAD `2a8eba5`, where the three audited files are unmodified.
- Audited bytes: the S122 row (line 133) plus the two round-66 search bullets
  (lines 336-337) hash to
  `c373d6e78691c33ae1cb71f29cd8425fe6e87baed138a6b5ed0823feb79faa44`.

## Assignment

Audit the round-66 `corpus/SOURCES.md` addition and its search note against fleet
`SOURCES-CONTRACT-v1.md` (kaika, 2026-10-19; read at
`/home/vgpnk/Projects/shokunin/.ufo/waves/kaika/SOURCES-CONTRACT-v1.md`) on: opened this
round, next id, 11 columns, tier/scope, URL, anchor, teaches, status, opened/recheck,
used-by; identify any enum or missing-path issue. Do not edit.

## What the round-66 diff actually is

`git diff 11385e04..2a8eba5 -- corpus/SOURCES.md`: 3 insertions, 0 deletions, no other row
touched.

- `+` row `S122` at line 133 (registry table; `## Registry` starts line 10, `## Paths`
  starts line 135, so the row is inside the registry).
- `+` bullet at line 336: "2026-10-24 — round-66 S122 source opening" (question, where,
  counts, stop rationale).
- `+` bullet at line 337: "Round-66 search-query clarification (append-only; same bounded
  search, no new candidates)" (exact query, search venue).

Row provenance by `git blame`:

- S122 row and the first search bullet: `806b53b` (2026-10-24 03:56:49 -0300,
  `round-66: land G9 coupling and integrity fixes`).
- `used-by` widened and the clarification bullet added: `9e75e73` (2026-10-24 04:20:01
  -0300, `round-66: record measurements and learning`).
- No later commit touches `corpus/SOURCES.md` (`git diff 9e75e73..HEAD` on the path is empty).

## Contract checklist (contract v1 text paired with observed bytes)

| # | Contract item (v1) | Observed | Verdict |
|---|---|---|---|
| 1 | "A row exists only for a source the row's author opened this round" | row `opened` = `2026-10-24`; round-66 commits are dated 2026-10-24; lesson Gate records access 2026-10-24; snapshot `Accessed: 2026-10-24` | PASS |
| 2 | "`id` — `S` + 3 or more digits, the next unused; never reused" | S122 unique; base max id was S121; no duplicate ids (`sort \| uniq -d` prints nothing) | PASS (see F6 on the two documented lower gaps) |
| 3 | "11 columns means NF=13; must print 0" malformed | S122 `NF=13`; all 120 rows `NF=13`; contract awk prints 0 malformed; no `\|` inside any cell | PASS |
| 4 | `kind` enum; `tier` enum scoped to `scope`; "`community` is never A" | `paper` ∈ {spec, docs, paper, code, tool, dataset, talk, book, community, own-work}; `A` ∈ {A,B,C}; kind ≠ community, so no tier-inflation; scope cell is bounded to "software commit-reference context" and explicitly disclaims durable citation | PASS |
| 5 | "`source` — title — canonical URL or DOI" | Title + `https://force11.org/info/software-citation-principles-published-2016/` + parenthetical `(PeerJ Computer Science 2:e86; DOI https://doi.org/10.7717/peerj-cs.86)` — two URLs in one `source` cell | NOTE F1 |
| 6 | "`anchor` — exact section / heading / page / line plus revision (version, commit, or publication date). Never a bare homepage." | `§6.7 Unique identification, paragraph on commit references; §1 Principle 6 (page opened 2026-10-24)`. Sections are exact and locatable on the live page (§6.7 at extracted line 381-382; §1 "Software citation principles" at line 135 with Principle 6 = Specificity at line 142). The only revision token in the anchor is the access date; the artifact revision (PeerJ CS 2:e86, 2016) is in `source` and the snapshot, not in the anchor | NOTE F2 |
| 7 | "`teaches` — one grounded learner benefit" | "A commit reference with its repository URL is still not a recommended durable software citation; preserve repository context when checking local version evidence" | NOTE F3 (the word "durable" is the row's gloss, not in the located quote; §6.7's stated fallback is omitted) |
| 8 | "`status` — queued · mined (cited by ≥1 path in `used-by`) · rejected" | `mined`; `used-by` names two citing paths, both of which cite S122 | PASS |
| 9 | "`opened` — ISO date ... `recheck` — ISO date or cadence (`90d`, `180d`, `on-release`)" | `2026-10-24`; `180d` (180d is already used by 6 other rows) | PASS |
| 10 | "`used-by` — repo-relative paths ... comma-separated, or `—`" | `corpus/knowledge/fleet-commit-resolution-round66.md, corpus/lessons/round-66.md`; both files exist; both grep-hit S122 (knowledge `source:` line 1 and gate prose line 9; lesson `## Gate` line 12 and `## Status changes`) | PASS |
| 11 | Rule 1: Gate records URL, access date, ≤25-word quote with location | lesson `## Gate` line 12 records URL, "opened 2026-10-24", a 17-word quote, location "§6.7, 'Unique identification'," and the snapshot path; quote is 17 words | PASS |
| 12 | Rule 2: append-only; only status/recheck/used-by change in place; each logged old→new | `check_sources_append_only.py --rev 2a8eba5 --base 11385e04` → "sources append-only rows clean: 2 commits scanned, 0 protected-cell changes", exit 0; one permitted log line (`9e75e73 S122 used-by: …round66.md -> …round66.md, corpus/l…`); lesson § "SOURCES used-by correction (append-only)" logs the old→new pair | PASS |
| 13 | Rule 5: question/query, where searched, date, identified/screened/included/excluded, exclusion reasons, stop rationale | split across two bullets: line 336 has question, opening URL + read location, date, `1 identified / 1 screened / 1 included / 0 excluded`, stop rationale; line 337 supplies the literal query and "web search" venue. Excluded = 0, so no exclusion reasons are owed | NOTE F4 |
| 14 | Rule 6: no credentials, session/private URLs, `op://` | none present | PASS |
| 15 | Shape: "`## Search log` — one prose note per bounded search (rule 5)" | both round-66 bullets are at EOF (336-337), physically under the second `## Leads (unopened)` heading (line 253, added by `dad926c`, 2026-10-24 01:44, a round-64 commit), not under `## Search log` (line 153). Round-63 (line 271) and round-64 (lines 295, 335) notes already sit in the same place | NOTE F5 (inherited placement drift, extended by this addition) |
| 16 | No `\|` inside any cell | NF=13 proves it for S122 and all 120 rows | PASS |

## Enum and missing-path verdict

- **Enum issues: none.** `kind=paper`, `tier=A`, `status=mined`, `recheck=180d`, `opened`
  ISO — all inside contract v1's enums; no `community`-as-A inflation.
- **Missing-path issues: none.** The contract's mined `used-by` path check prints nothing
  for the whole file (120 rows); both S122 paths exist and cite the row. The lesson's
  snapshot path `.ufo/waves/round-66/snapshots/S122-excerpt.txt` exists (12 lines).
- No duplicate id, no malformed row, no second URL collision: force11.org is not in the
  census's 16 W04 duplicate-URL warnings.

## Freshness evidence (judged axis)

Live re-open from this seat, 2026-10-24T07:35:15Z:

```
curl -sS -L https://force11.org/info/software-citation-principles-published-2016/
http=200 bytes=265111 type=text/html; charset=UTF-8
url_effective=https://force11.org/info/software-citation-principles-published-2016/
sha256 11b81f6aa5446ab1bc9f0670ee77133d41dcf939284671958249789e1bd471a7
```

- The exact 17-word quote is present, in the §6.7 paragraph ("6.7. Unique identification."
  at extracted line 381; quote in the following paragraph at line 382), matching the
  lesson Gate and `.ufo/waves/round-66/snapshots/S122-excerpt.txt`:
  "a commit reference together with a repository URL is not recommended for the purposes
  of software citation".
- §1 exists as "1. Software citation principles" (extracted line 135); Principle 6 is
  "Specificity" (extracted line 142), so the anchor's "§1 Principle 6" resolves.
- The snapshot is an excerpt, not a full-page snapshot (its own first line says so); this
  seat's fetch is the only full-page hash recorded here and is not claimed as the lane's
  access receipt.
- The bundled DOI `https://doi.org/10.7717/peerj-cs.86` redirects to
  `https://peerj.com/articles/cs-86`; the HEAD returned 403 to this unauthenticated
  client. That is an access gate, not evidence the DOI is dead; the primary FORCE11 URL
  is the one opened and quoted.

## Findings

**F1 — `source` carries two URLs; the registry has no other such row.**
Contract v1: "`source` — title — canonical URL or DOI". Observed S122 `source`:
`FORCE11 Software Citation Working Group — Software Citation Principles (Smith et al.,
2016) — https://force11.org/info/software-citation-principles-published-2016/ (PeerJ
Computer Science 2:e86; DOI https://doi.org/10.7717/peerj-cs.86)`. A scan of all 120 rows
for 2+ `http(s)://` in the `source` cell returns only S122. The second URL is the paper
DOI and is redundant with the opened page's own citation line; it is not an enum or path
defect.

**F2 — anchor revision is an access date, not a version/commit/publication date.**
Contract v1: anchor is "exact section / heading / page / line plus revision (version,
commit, or publication date)". The S122 anchor's revision token is "(page opened
2026-10-24)". Neighbouring paper rows put artifact revision inside the anchor
(S120: "arXiv:2102.11378v2 HTML (26 Feb 2021), the artifact opened and quoted"; S118
puts fetch hash + snapshot path in the anchor). The S122 artifact revision (PeerJ
Computer Science 2:e86, 2016) is present in `source` and in the snapshot, so the row as
a whole identifies the revision; the anchor cell alone does not. Report for the canonical
judge to rule whether the row-level revision satisfies the anchor clause.

**F3 — `teaches` adds "durable", which the located quote does not contain, and omits
§6.7's fallback.** Quote: "…not recommended for the purposes of software citation"
(17 words). `teaches`: "…still not a recommended durable software citation…". The page
also states, two paragraphs later (extracted line 386): "if (1) the software authors did
not register a DOI and/or release a specific version, or (2) the version of the software
used does not match what is available to cite … falling back on a combination of the
repository URL and version number/commit hash would be an appropriate way to cite the
software used." The `scope` cell's disclaimer bounds the C2 use, and the knowledge entry
repeats "durable"; the omission is a precision issue in `teaches`, not an enum/path
defect. No conflicting contract text found; reported for the judge.

**F4 — rule 5 fields are split across two bullets for one bounded search.**
Line 336 states question, opening URL/read location, date, 1/1/1/0 counts and stop
rationale, but not the literal query or the search venue. Line 337 supplies
`site:force11.org software citation principles Smith citation software 2016 persistent
identifier` and "web search", and declares "same bounded search, no new candidates".
Counts are not double-counted. Contract shape says "one prose note per bounded search".
The fields are jointly complete; neither bullet alone is.

**F5 — the two bullets are not in `## Search log`.**
They are appended at EOF under the second `## Leads (unopened)` heading (line 253; two
such headings exist at lines 211 and 253). The `## Search log` section starts at line
153. This placement is inherited: the round-63 note (line 271) and both round-64 notes
(295, 335) are already under that heading, so round 66 extends a pre-existing shape
drift rather than introducing it.

**F6 — id gaps below S122 are documented reservations, not reuse.**
Rows S092 and S116 do not exist in the file or anywhere in `corpus/SOURCES.md` history
(`git log -S'| S116 |'` and `-S'| S092 |'` on the path return nothing). They are named as
never-written reservations in `corpus/lessons/round-58.md:43-44` (S092) and
`corpus/lessons/round-61.md:18` (S116, "no row is invented"). The lane therefore applies
"next unused" as max+1 after documented gaps; S122 follows S121 and does not reuse either
id. No contract breach observed, but the literal "next unused" reading would have pointed
at S092/S116 earlier in the sequence — noted for the judge, not charged to this round.

## Gates executed by this seat (read-only)

```
# contract census block, lane root, working tree at 2a8eba5
grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md
# -> 120
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF!=13 {...}' corpus/SOURCES.md
# -> 0 malformed
# duplicate ids -> nothing; enum/tier-inflation scan -> nothing
# mined used-by missing-path loop -> nothing

python3 -B verifiers/check_sources_append_only.py \
  --rev 2a8eba56b3f9321b70c569fa2816d42237ca49a2 \
  --base 11385e04e368c1e94ab1a5a89d7439033eb1f855
# -> log  9e75e7345 S122 used-by: ... ; sources append-only rows clean:
#    2 commits scanned, 0 protected-cell changes ; exit 0
```

Round-66 census receipts read for comparison (not re-run):
`.ufo/waves/round-66/census-before.txt` (119 rows at base, exit 0) and
`.ufo/waves/round-66/census-after.txt` (120 rows at tip, exit 0). Both carry 16
pre-existing `W04` duplicate-URL warnings, none naming `force11.org`. My independent row
count (120) matches `census-after.txt`.

## Out of scope / not claimed

- No C1 or C2 claim, counter, control or receipt was scored, re-run or modified. No judge
  statement is made here.
- No wave-seat data was read as evidence for this audit; this report's evidence is the
  files, git history, the lane's append-only gate and this seat's live fetch.
- No mutation, no sandbox clone, no dispatch, no installation/upgrade.
- I did not edit `corpus/SOURCES.md`, the lesson, the knowledge entry, the plan, controls
  or receipts; the lane Git/jj state is untouched.
- Freshness is claimed only for the primary FORCE11 URL as observed at
  2026-10-24T07:35:15Z; the DOI redirect returned 403 to HEAD and is not characterized
  beyond that.

## Artifact paths

- This report: `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-66/w1/ScribeSOURCES.md`
- Audited row: `corpus/SOURCES.md:133`
- Audited search notes: `corpus/SOURCES.md:336-337`
- Contract: `/home/vgpnk/Projects/shokunin/.ufo/waves/kaika/SOURCES-CONTRACT-v1.md`
- Snapshot: `.ufo/waves/round-66/snapshots/S122-excerpt.txt`
- Gates: `verifiers/check_sources_append_only.py`; census receipts
  `.ufo/waves/round-66/census-before.txt`, `.ufo/waves/round-66/census-after.txt`
- Lesson: `corpus/lessons/round-66.md` (`## Gate`, `## Status changes`,
  `## SOURCES used-by correction (append-only)`)
