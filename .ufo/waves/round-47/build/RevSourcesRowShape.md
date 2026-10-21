# RevSourcesRowShape — `corpus/SOURCES.md` registry vs SOURCES-CONTRACT-v1

verdict: the census is clean at BASE but it is blind to the fields that break: 9 of 11 rows carry no revision in `anchor`, all four `mined` rows point `used-by` at a non-corpus file, S009/S010 are stale against BASE and need superseding rows (rule 2 forbids in-place anchor edits), and C3's index row alone cannot zero its DRIFT (the corpus baseline must also move 58→59).

Lane: leaf reviewer. BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd` (`kotoba-shokunin`, branch master).
All line numbers are at BASE. Read-only: nothing in the lane repo was modified; my only writes are this
report and `RevSourcesRowShape.rows.json` under `.ufo/waves/round-47/build/`.
Contract source of truth: fleet `/home/vgpnk/Projects/shokunin/.ufo/waves/kaika/SOURCES-CONTRACT-v1.md`
(exists, 5618 B, read), carried in full at fleet `CORPUS.md:107-181`.

Scratch clone used for every measurement below:
`git clone -q --no-hardlinks … /fast/scratch/kotoba-r47/RevSourcesRowShape/lane && git -C … checkout -q --detach c61a973b2e02e1ded169703ddcb06466f4edd8bd` → `c61a973` (exit 0).
Tools installed/updated: **none** (no `pacman`, `uv`, `npm` transaction was needed or run).

---

## 1. Census at BASE (CORPUS.md § Census, all seven commands)

Run from the scratch clone root, verbatim from `CORPUS.md:150-166`:

| # | command | output | exit |
|---|---|---|---|
| 1 | `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` | `11` | 0 |
| 2 | `awk -F'|' '/^\|…S[0-9]{3,}…\|/ && NF!=13 {n++} END{print n+0}'` | `0` | 0 |
| 3 | tier histogram | `A=10 C=1` | 0 |
| 4 | status histogram | `mined=4 queued=6 rejected=1` | 0 |
| 5 | duplicate ids | *(empty)* | 0 |
| 6 | enum violations + tier inflation | *(empty)* | 0 |
| 7 | mined rows whose `used-by` paths do not exist | *(empty)* | 0 |

**The census passes at BASE and it is the wrong instrument**: it counts rows, checks cell shape, enum
membership and *path existence*. It never looks at what a row claims, whether the cited path cites
the row, whether the anchor carries a revision, or whether the quoted output still holds. Everything
below is outside the census's reach — which is the point of this lane.

---

## 2. Findings by severity

### HIGH-1 — S010's `anchor` carries no revision at all (`corpus/SOURCES.md:23`)

The row quotes two counted outputs (`"0 failure(s) over 1597 assertions"`, `"checklist.box_map_complete … 41 boxes mapped"`)
and its anchor cell contains **no** version, commit, sha256 or date:

```
| S010 | kotoba own work — verifiers/verify_skill_checklist.py — --self-test exit 0 and --json exit 1 (9 PASS / 1 FAIL governance.citation_resolves at LOG.md:2111) runs 2026-10-19 | own-work | A | The lane's executed-box gate and frontmatter parse coverage | Final line "0 failure(s) over 1597 assertions"; --json "checklist.box_map_complete ... 41 boxes mapped" | … | queued | 2026-10-19 | on-commit | — |
```

Contract v1 field list: *"`anchor` — exact section / heading / page / line **plus revision (version, commit, or
publication date)**"* (contract file:44-45). The revision exists but was dropped from the row: it is
recorded in the lesson's Gate table (`corpus/lessons/round-46.md:72` → `file sha256
214ae44dcba45ba19656a0b2aa6c49900c618f6716a64fef0776f06437cfc8d0`) and that sha is still the live
file's sha at BASE (`sha256sum verifiers/verify_skill_checklist.py` → `214ae44d…`, exit 0). A reader
of the row alone cannot tell which bytes produced "1597".

Measured at BASE, to be fair to the row's content: `python3 -B verifiers/verify_skill_checklist.py --self-test`
→ `0 failure(s) over 1597 assertions` (exit 0) — the count is still true; and at the lane root
`python3 -B verifiers/verify_skill_checklist.py --repo "$PWD" --skill "$PWD/SKILL.md" --json` → exit 1,
`9 PASS / 1 FAIL`, FAIL detail `LOG.md:2111: '.ufo/round-45/drafts/v10/post-r44-hunt.py' does not resolve
from /home/vgpnk/Projects/shokunin/kotoba-shokunin` — so S010's `source` cell is accurate too.
**The defect is the missing pin, not the claim.**

Repair path matters: contract rule 2 allows in-place edits to `status`/`recheck`/`used-by` only; a
wrong anchor must become **a new row whose `teaches` opens `supersedes S0NN —`**. So S010 cannot be
"fixed" by editing the anchor. Note C2 and C3 will invalidate S010's `teaches` anyway — it says the
frontmatter check "is a lenient structural parse with no XML-tag rule", true at BASE
(`verifiers/verify_skill_checklist.py:76` — "Limit: a structural parse, not semantic YAML validation.";
`grep -niE 'xml|<skills>|tag' verifiers/verify_skill_checklist.py` → only cmark-oracle comments at
1551/1894). Plan one superseding row S012 that carries the sha256 pin *and* the post-C2 wording,
instead of two edits.

### HIGH-2 — S009's `on-commit` recheck has already fired and was never logged (`corpus/SOURCES.md:22`)

S009 anchors on `commit 78ee57e`. That pin is honest and verifiable:

```
git show 78ee57e:verifiers/compare_harness_independent.py | sha256sum
→ ccf41c23d2c766124b27f60653508cd1590aa625cbf8afd8da68b56f7b5bc04d      # == the sha recorded at corpus/lessons/round-46.md:71
sha256sum verifiers/compare_harness_independent.py        (at BASE)
→ 778b367e5e5f94fc90132f4070aec3e2395b26914a1d0a50a188558c55cff332      # the file moved after the pinned commit
python3 -B verifiers/compare_harness_independent.py --self-test          (at BASE)
→ self-test: 0 failure(s) over 330 assertions                              (exit 0)
```

The row quotes `Final line "self-test: 0 failure(s) over 328 assertions"` — true at its pinned commit,
**false at HEAD** (330). The row's `recheck` value is `on-commit`; the commit the row names has been
superseded, so the recheck obligation is due and unmet, and no lesson logs it. That is precisely the
drift class the lane's own M4/M9 mistake rows are about (a source that moved without the record
moving). Either re-pin S009 (superseding row) or record the recheck in the round-47 lesson with the
old→new log rule 2 requires.

### MED-1 — every `mined` row points `used-by` at a file the contract's field definition excludes

Contract: *"`used-by` — repo-relative paths of **the knowledge entries or lessons** citing the row,
comma-separated, or `—`"* (contract file:52-53). All four mined rows carry `SKILL.md`
(`corpus/SOURCES.md:14` S001, `:15` S002, `:16` S003, `:21` S008) — `SKILL.md` is the lane's skill
file, not a knowledge entry and not a lesson.

Why this matters beyond wording: the registry's expansion metric is defined as *"counts admitted
`knowledge/` entries whose `source:` cites a `mined` row on uncovered coverage-map ground"*
(contract rule 4). At BASE that count is **zero**:

```
grep -rlE '\bS0[0-9]{2}\b' corpus/knowledge/    → exit 1 (no match)
```

Four `mined` rows and no knowledge entry cites any of them — the mined status is real only against
`SKILL.md:151`. The cheapest repair in the whole contract: `used-by` is one of the three in-place
mutable fields, so `used-by` may be changed to `SKILL.md, corpus/knowledge/frontmatter-trigger-surface.md`
(with the old→new log in the lesson) **if and only if** that knowledge entry is made to cite the ids —
or, if the lane intends `SKILL.md` to count, the deviation should be recorded once rather than left
implicit in four rows.

### MED-2 — the `mined` invariant is upheld by prose and enforced by nothing

Checked per row: the used-by path of each mined row does contain that row's id, at BASE:

```
SKILL.md:151  … Portability floor (spec + vendor + YAML, `corpus/SOURCES.md` S001, S002, S003, S008): …
```

→ S001 ✓, S002 ✓, S003 ✓, S008 ✓ (all four literal ids present on one line). **PASS**, and the
counterexample that shows how thin the guarantee is: `LOG.md:2315` records that at `f2f9ee1` the same
citation was the range `S001–S003`, which *"a literal-id check cannot see"* — the fix was to spell the
ids out in prose, not a gate. Nothing in the lane reads the registry:
`grep -ln 'SOURCES' verifiers/*.py verifiers/*.sh` → exit 1 (no verifier mentions `SOURCES.md`);
`grep -n 'used-by\|used_by' verifiers/*.py` → no output. So `status=mined` is currently unfalsifiable
by any instrument the lane owns. A one-line census sibling — *"mined rows whose used-by path does not
contain the row id"* — would have gone red on the `f2f9ee1` range form and would keep the invariant
honest. That is a concrete, falsifiable gate proposal (it fails on the f2f9ee1 form, passes now).

### MED-3 — the round lesson's own row count contradicts the registry and its own fetch log

`corpus/lessons/round-46.md:59` — *"admitted as rows: 10 (9 `queued` A-tier, incl. 2 own-work)"*.
At BASE: registry = 11 rows (census #1 → `11`), the lesson's own Gate table lists **11** rows
(lines 63–73, S001–S011), and the committed fetch log's census block records
`status histogram → "queued=10 rejected=1"` (i.e. ten queued at fetch time, before the four
`queued→mined` changes). The registry's own search-log note also totals 11 (8 + 1 rejected + 2 own-work).
So "10 (9 queued)" is number-drift in an append-only file — CORPUS.md's rule *"A count carries its
command"* is violated and the number is wrong in the direction that hides a row. Repair is an
appended note in the lesson, never an edit.

### MED-4 — the search log's stop rationale misstates the frozen contract (`corpus/SOURCES.md:52`)

> "Stop rationale: the contract asks 8–14 honest rows; a short registry of opened rows beats a long one (contract rule 4)."

There is no such quota. The frozen contract rule 4 reads *"**There is no row quota**; a short registry
of opened, honestly tiered rows beats a long one"* (contract file:118-119), carried at `CORPUS.md:125`.
`grep -n 'quota\|8–14\|8-14' /home/vgpnk/Projects/shokunin/CORPUS.md` → only line 125 (`no row quota`);
the contract file contains no "8–14" either. The standing record of the lane's taste therefore cites a
quota its governing contract explicitly disclaims, and attributes it to rule 4. Append-only fix: an
appended correction note under § Search log.

### MED-5 — S007's anchor has no revision and its scope ("this host's actual behaviour") is not re-derivable from the cited URL today (`corpus/SOURCES.md:20`)

Anchor: `§ Standard Compliance and Interoperability` — no version, no date, no section-number anchor.
The URL `https://docs.python.org/3/library/json.html` is a moving target: re-read today (2026-10-21) it
serves **"Python 3.15.1 documentation"** (page `<title>`; `og:image` path `3.15/`; source tree
`3.15/Lib/json/__init__.py`), while this host runs `python3 --version` → **3.14.8**.

The recorded quote still exists on the page (fetched artifact lines 575-576: *"Repeated names within an
object are accepted, and only the value of the last name-value pair is used."*), and the host behaviour
is measurable today: `python3 -c "import json; print(json.loads('{\"a\":1,\"a\":2}'))"` → `{'a': 2}`
(exit 0). But the row's *scope* is "This host's actual duplicate-name decode behavior" while the cited
page now documents a different interpreter than the host's — the scope is not derivable from the anchor,
and `recheck: 365d` (the longest in the registry) is scheduled against a page that changes every
Python release. The honest superseding row pins `https://docs.python.org/3.14/library/json.html` and the
one-line host command.

### MED-6 — 6 of 11 rows carry `teaches` clauses that no recorded quote grounds (contract rule 1)

Rule 1: *"The round lesson's `## Gate` records, for every new row, the URL, the access date, and a
≤25-word quote with its location **grounding `teaches`**"*. The Gate table's quotes are all ≤25 words
(I counted all 11 — max 16 words ✓), but one quote cannot ground a multi-clause `teaches`:

| row | `teaches` clauses | recorded quote grounds | ungrounded clause(s) |
|---|---|---|---|
| S001 | 3 (name 1-64 + directory match; description 1-1024 + what/when; body <500 lines) | only the 500-line clause (`lessons/round-46.md:63`) | name & description constraints |
| S002 | 2 (colon-YAML invalid; lenient warn-and-load) | only the first (`:64`) | "warn and load anyway on name mismatch" — the load-bearing clause for the lane's strict-gate decision **and** S011's flip condition |
| S003 | 4 (no XML tags; third person; what+when; <500 lines) | only "Cannot contain XML tags" (`:65`) | third person, what+when, 500 lines |
| S006 | 1 + parenthetical | the parenthetical is in the *location* cell, not the quote (`:68`) | receiver-behaviour clause |
| S007 | 2 | the first (`:69`) | "the implementation default the comparator must not inherit uncritically" |
| S011 | 3 rejection reasons | only the name-mismatch claim (`:73`) | "credits an angle-bracket ban to the spec which has none (**0 mentions**)"; "quantitative claims cite unnamed analyses" |

S005, S008, S009, S010 are fully grounded by one quote each ✓. Two of the ungrounded clauses happen to
be true today — I re-read the live spec and the live client guide (§4 below) and confirmed S001's
name/description constraints and S002's lenient-validation bullets — but the *record* does not show it,
which is the rule-1 defect. S011's "(0 mentions)" is also a count without a command in the row (the
command `grep -ciE 'angle bracket' spec.md` → 0 lives in the lesson, `:73`).

### LOW-1 — S001's anchor locator does not match any live heading (`corpus/SOURCES.md:14`)

Anchor: `§ Skill metadata table, § Progressive disclosure`. The live spec (re-read 2026-10-21) has
headings ``## `SKILL.md` format`` → `### Frontmatter` (the field table) → `#### `name` field` … and
`## Progressive disclosure`; there is **no** "Skill metadata" heading. The second locator is exact:
"Keep your main `SKILL.md` under 500 lines. Move detailed reference material to separate files." still
sits under `## Progressive disclosure` ✓. A re-checker grepping the first locator gets 0 hits.

### LOW-2 — S004 and S005 are in no path and in no citation (`corpus/SOURCES.md:17-18`)

`## Paths` (`:26-40`) contains exactly two sequences — `S001 → S008 → S003 → S002 → S011` and
`S006 → S007 → S009 → S010`. `grep -n 'S004\|S005' corpus/SOURCES.md` → only their own rows (17, 18).
Both are `queued`, so the contract does not demand a citation yet, but two of eleven registry rows have
no reader, no path and no knowledge entry — and S005's scope ("Fenced code block syntax the lane's
box/quote extraction implements") describes a live dependency of `verify_skill_checklist.py`'s command
extraction that the registry never grounds.

### LOW-3 — the r46 timestamp-label defect does **not** reach the `opened` column, but survives uncorrected in the committed evidence (`corpus/lessons/round-46.md:77`)

The defect as recorded: S001–S008 `accessed_utc` read `18:40Z` while the seat's work was near `21:40Z`;
"the 18:40 values are local time (UTC−3) labelled `Z` — the date holds, the hour label is wrong".

I checked the arithmetic against this host: `date +%z` → `-0300`, `/etc/localtime` →
`America/Sao_Paulo`. So `18:40:53` local = `21:40:53Z` — **the same calendar date under either
reading**. Consequence for the registry: all eleven `opened` values (2026-10-19, `corpus/SOURCES.md:14-24`)
are date-safe, and SOURCES.md's date-only `opened` column carries no mislabel. **No defect in the
registry's `opened` column.**

The defect does survive in the machine-readable evidence that `corpus/SOURCES.md:6-7` points readers at:
`.ufo/round-46/evidence/w2/sources/fetch-log.json` (tracked, `git ls-files` → present) still carries
`2026-10-19T18:40:5xZ` for all eight external rows, and the lesson's Gate table (`:63-70`, `:73`)
prints the same mislabelled instants. The lesson documents the defect in prose but never corrects the
evidence file. Two further observations for whoever repairs it:
* the fetch-log's `accessed_utc` for S009/S010 is **not a timestamp at all** — it is the string
  `"2026-10-19T21:42Z (run); file sha256 at HEAD ccf41c23…"` — so the field is not machine-parseable
  as a time in 2 of 11 rows;
* the fetch log carries **no independent corroboration** of the true UTC instant (no HTTP `Date:`
  header, no recorded `date -u` per row). "18:40 local ⇒ 21:40:53Z" is an inference from the host's
  UTC−3 offset, not a re-derivation. A repair should capture `date -u` (or the response `Date:`) at
  fetch time in the next round's log, otherwise the next instance of this class is equally unprovable.

### LOW-4 — the lesson's Spot-check section still reads "pending" (`corpus/lessons/round-46.md:79`)

> "### Spot-check — pending — non-author verification by the orchestrator after landing; agree/disagree recorded here by a later append"

The verification landed in a separate file (`corpus/lessons/round-46-verifier-spotcheck.md`: admit S003/S006,
reject S011, both "agree"), and the promised append to `round-46.md` never happened — the file still
says "pending". The lesson's own § Gate therefore understates the round's evidence.

---

## 3. Row-by-row table (BASE `corpus/SOURCES.md:14-24`)

| row | line | kind/tier | status | anchor has a *content* revision? | used-by | used-by cites the id? | teaches grounded by the recorded quote? | verdict |
|---|---|---|---|---|---|---|---|---|
| S001 | 14 | spec/A | mined | ✗ (access date only; "Skill metadata table" heading absent today) | `SKILL.md` | ✓ (SKILL.md:151) | ✗ (2 of 3 clauses) | anchor needs superseding row |
| S002 | 15 | docs/A | mined | ✗ (access date only) | `SKILL.md` | ✓ | ✗ (lenient clause) | anchor needs superseding row |
| S003 | 16 | docs/A | mined | ✗ (access date only) | `SKILL.md` | ✓ | ✗ (3 of 4 clauses) | anchor needs superseding row; C2 will cite this row |
| S004 | 17 | spec/A | queued | ✗ (access date only) | — | n/a | ✓ | in no path, in no citation |
| S005 | 18 | spec/A | queued | ✓ (`version 0.31.2`) | — | n/a | ✓ | in no path, in no citation |
| S006 | 19 | spec/A | queued | ✗ (row title carries "RFC 8259"; anchor cell carries nothing) | — | n/a | ✗ (parenthetical) | anchor cell needs a revision |
| S007 | 20 | docs/A | queued | ✗ (moving URL; now 3.15.1 docs, host is 3.14.8) | — | n/a | ✗ (2nd clause) | scope not re-derivable → superseding row |
| S008 | 21 | spec/A | mined | ✗ (row title carries "1.2.2"; anchor cell carries nothing) | `SKILL.md` | ✓ | ✓ | anchor cell needs a revision |
| S009 | 22 | own-work/A | queued | ✓ (`commit 78ee57e`, verified) | — | n/a | ✓ | **stale**: file moved to `778b367e…`, self-test now 330 ≠ quoted 328; `on-commit` recheck due |
| S010 | 23 | own-work/A | queued | ✗ (no version/commit/sha/date at all) | — | n/a | ✓ | **anchor has no revision**; content still true at BASE |
| S011 | 24 | community/C | rejected | ✗ (access date only) | — | n/a | ✗ (2 of 3 reasons; "(0 mentions)" lacks a command) | rejection still holds today (see §4); anchor needs a revision |

Column semantics used above: "content revision" = a version / commit / sha256 / publication date that
pins *what bytes were read*, as opposed to an access date. Under the contract's literal wording
("version, commit, or publication date") **9 of 11 rows fail**; under the lenient reading (an access
date counts) 4 of 11 fail (S006, S007, S008, S010) — S008 and S006 recover their version from the
`source` title cell, so the strict-failing set is S001, S002, S003, S004, S006, S007, S010, S011 plus
S008's anchor cell. Either way **S010 and S007 are the two rows where the gap has teeth** (an
unpinned counted output; an unpinned moving doc).

---

## 4. Freshness re-checks I ran on live pages (2026-10-21)

| source | what I checked | result |
|---|---|---|
| `https://agentskills.io/specification` (S001) | re-read whole page | "Keep your main `SKILL.md` under 500 lines…" ✓ still under `## Progressive disclosure`; `name` "Must be 1-64 characters" / "Must match the parent directory name" ✓; `description` "Must be 1-1024 characters" ✓; **no heading named "Skill metadata"** (LOW-1); no "angle bracket" phrase anywhere on the page → S011's "(0 mentions)" claim still holds |
| `https://agentskills.io/client-implementation/adding-skills-support` (S002) | re-read whole page | `### Handling malformed YAML` ✓ and the recorded quote verbatim ✓; `### Lenient validation` ✓ with "Name doesn't match the parent directory name → warn, load anyway" ✓ → **S011's flip condition ("the client guide tightens to refuse mismatched names") is NOT met; the rejection stands** |
| `https://docs.python.org/3/library/json.html` (S007) | re-read whole page | quote still present (artifact lines 575-576) ✓, but the page now serves **3.15.1** docs vs host **3.14.8** (MED-5) |

Not re-opened (no re-open claimed): S003 (Anthropic best-practices — C2's executor owns that re-open),
S004, S005, S006, S008, S011. S011's rejection was checked from the S002 side only.

---

## 5. Cross-lane hand-offs (measured, for the integrator — not my lane's edits)

* **C3 index row alone cannot zero the DRIFT.** `python3 -B verifiers/verify_corpus_integrity.py --json`
  at BASE → exit 1 with 2 DRIFT: `corpus.index.tracked_files` observed **59** / expected **58**, and
  `corpus.index.unindexed` observed **1**. `python3 -B verifiers/verify_corpus_independent.py --json`
  → exit 1 with 1 DRIFT (the same unindexed file). The unindexed file is
  `corpus/lessons/round-46-verifier-spotcheck.md` (index check at `verifiers/verify_corpus_integrity.py:433`;
  `git ls-files corpus/` = 59 = 58 `.md` + `corpus/knowledge/sibling-citation-routing-round16.json`).
  Adding the index row clears `unindexed` but **does not change the file count**, so the baseline must
  also move: `verifiers/corpus-baseline.json` `checks["corpus.index.tracked_files"].expect` 58 → 59
  (the baseline's own `notes` history shows this exact bump per round: 47→48→52→…). Two edits, not one.
* **C3's erratum subject is confirmed at BASE.** `LOG.md:2111` reads: *"At `2026-10-19T19:38:15Z`, the
  census replay command `python3 .ufo/round-45/drafts/v10/post-r44-hunt.py` and its two documented R41
  draft replay commands each exited 2 **because the referenced runners are absent**."* The cited runner
  is absent (`test -e .ufo/round-45/drafts/v10/post-r44-hunt.py` → exit 1; `.ufo/round-45/drafts/`
  does not exist) and the line itself records the absence — exactly the erratum case. The gate agrees:
  the lane-root `--json` run FAILs at `LOG.md:2111` with that exact path.
* **C2 before-value, pinned to the right site.** The `<skills>` token in the *description* is at
  `SKILL.md:14` (the description is a folded block scalar `>` spanning lines 3-…). The before-command
  `grep -c '<skills>' <(sed -n '/^---$/,/^---$/p' SKILL.md)` → `1` (exit 0) ✓. A whole-file
  `grep -c '<skills>' SKILL.md` → `8` (lines 14, 22, 91, 96, 99, 111, 151, 430) — the frontmatter-scoped
  count is the correct before-value; the whole-file count is a body-inclusive decoy.
* **Dead pointer in the registry's own provenance.** The search log's "Where:" points at the kaika-w1
  dossier `kotoba-art.md` (`corpus/SOURCES.md:46`, repeated in the Leads section at `:87`), and the
  fetch log's `cwd` is `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kotoba-shokunin`.
  Neither exists on this host today (`find /home/vgpnk/Projects/shokunin/.tower -name kotoba-art.md`
  → nothing; `.tower/worktrees/kaika/` absent). The contract file itself is still present
  (`.ufo/waves/kaika/SOURCES-CONTRACT-v1.md`, 5618 B) ✓, so the *contract* is verifiable even though
  the *dossier* that fed the search log is not.

---

## 6. Commands run, with exit codes (all reproducible)

| command | exit | key output |
|---|---|---|
| `git clone --no-hardlinks … && git checkout --detach c61a973b…` | 0 | `c61a973` |
| census #1 rows | 0 | `11` |
| census #2 malformed | 0 | `0` |
| census #3 tier hist | 0 | `A=10 C=1` |
| census #4 status hist | 0 | `mined=4 queued=6 rejected=1` |
| census #5 dup ids | 0 | *(empty)* |
| census #6 enum/inflation | 0 | *(empty)* |
| census #7 mined used-by existence | 0 | *(empty)* |
| `sha256sum verifiers/compare_harness_independent.py verifiers/verify_skill_checklist.py` | 0 | `778b367e…`, `214ae44d…` |
| `git show 78ee57e:verifiers/compare_harness_independent.py \| sha256sum` | 0 | `ccf41c23…` (== lesson's recorded sha) |
| `python3 -B verifiers/compare_harness_independent.py --self-test` | 0 | `self-test: 0 failure(s) over 330 assertions` |
| `python3 -B verifiers/verify_skill_checklist.py --self-test` | 0 | `0 failure(s) over 1597 assertions` |
| `python3 -B verifiers/verify_skill_checklist.py --repo "$PWD" --skill "$PWD/SKILL.md" --json` (lane root, read-only) | 1 | 9 PASS / 1 FAIL `governance.citation_resolves` @ `LOG.md:2111` |
| `python3 -B verifiers/verify_corpus_integrity.py --json` | 1 | DRIFT `tracked_files` 59/58, DRIFT `unindexed` 1 |
| `python3 -B verifiers/verify_corpus_independent.py --json` | 1 | DRIFT `corpus.index.unindexed` 1 |
| `grep -rlE '\bS0[0-9]{2}\b' corpus/knowledge/` | 1 | no match (no knowledge entry cites an S row) |
| `grep -ln 'SOURCES' verifiers/*.py verifiers/*.sh` | 1 | no verifier reads the registry |
| `grep -n 'S004\|S005' corpus/SOURCES.md` | 0 | lines 17, 18 only |
| `grep -c '<skills>' SKILL.md` / frontmatter-scoped | 0 / 0 | `8` / `1` |
| `test -e .ufo/round-45/drafts/v10/post-r44-hunt.py` | 1 | absent (LOG.md:2111's recorded absence) |
| `date +%z` | 0 | `-0300` (America/Sao_Paulo) |
| `python3 --version` | 0 | `Python 3.14.8` (vs 3.15.1 docs served at docs.python.org/3 today) |
| 3 live page re-reads (§4) | 0 | S001/S002 anchors verified; S007 page version drift |

---

## 7. What I did NOT check

* **No re-open of S003, S004, S005, S006, S008, S011.** S003's re-open is C2's lane; I did not fetch the
  Anthropic best-practices page, `agents.md/`, the CommonMark spec, RFC 8259, the YAML spec or the
  agentman tutorial. Their anchors are unverified for today's content (S005 is the only one whose
  anchor carries a content revision, `version 0.31.2`, and I did not re-check the spec version).
* **No re-derivation of the fetch-log's sha256 values.** The reader-text shas depend on the reader's
  normalization, which I did not reproduce; only the two local-file shas (S009/S010) were verified
  against `git show`.
* **No fleet-wide conformance sweep.** I checked no sibling lane's `corpus/SOURCES.md`; the contract's
  census § note says default discovery covers child repositories only, and a lane-level reviewer
  would be the wrong scope for the fleet.
* **No lane gates beyond the ones above.** `verify_surfaces.py`, `check_substrate_pins.py` and
  `verify_harness_claims.py` (C1's territory) were not run; I made no claim about substrate pins.
* **No source re-open of the S003/S002 client-contract claim in the SKILL.md body.** SKILL.md:151's
  prose ("no XML tags (Anthropic rule)") is consistent with the live pages I read, but I did not test
  whether a *client* would reject the token — that is C2's fixture question, not mine.
* **Not verified:** that the reader-text sha256 pins would still match if the pages were re-fetched
  (no sha reproduction); that the `opened` dates are the true access dates (the hour label is
  provably wrong; the date is only *consistent*); that the 11 rows are the round's *only* rows
  (the lesson's own count says 10 — MED-3).
* **No lane file was modified.** Every measurement above was taken in
  `/fast/scratch/kotoba-r47/RevSourcesRowShape/lane` (detached at BASE) except the single read-only
  `--json` run at the lane root (a verifier with no write path — `grep -nE "open\([^)]*['\"][wax]"`
  over `verifiers/verify_skill_checklist.py` → no match) and the three public page reads.
