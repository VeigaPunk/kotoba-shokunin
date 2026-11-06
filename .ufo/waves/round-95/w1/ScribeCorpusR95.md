# ScribeCorpusR95 — S270 row and the round-95 lesson scaffold (round 95, w1)

Seat: **ScribeCorpusR95** (scribe seat of `r95-w1`). Scope: `corpus/SOURCES.md` (APPEND one row
S270 only), `corpus/lessons/round-95.md` (new), `corpus/README.md` (one index row for the new
lesson ONLY). No other lane file was written; no frozen instrument, plan, counter, builder or
forgery patch was touched.

Status: **DONE** — patch written, receipts copied, READY written.

## What I produced

| artifact | path | bytes |
|---|---|---|
| patch | `.ufo/waves/round-95/w1/ScribeCorpusR95/ScribeCorpusR95.patch` | 25387 |
| lesson (scaffold) | `corpus/lessons/round-95.md` (in the patch) | 14890 |
| index row | `corpus/README.md` (in the patch, one row) | +1 line |
| registry row | `corpus/SOURCES.md` (in the patch, one appended row) | +1 line |
| receipts | `.ufo/waves/round-95/w1/ScribeCorpusR95/` | census-before/after/verify, fetch-record.txt, three fetched pages |

Scratch clone: `/fast/scratch/hyaku/kotoba-r95/ScribeCorpusR95/repo`, created exactly as
`git clone -q --shared <lane> "$D" && git -C "$D" checkout -q 673d1e2e6f850bb54dda9698cf825cf6788c7d0d`;
`git -C "$D" rev-parse --show-toplevel` printed the clone dir before every git call in it. The one
scratch commit is `c304f2b387e0b1ad18ecd0657f80832dfa336ca6` (identity `scratch <scratch@invalid>`,
inside the scratch clone only). The lane's own git/jj state was never written to — `git status` in
the lane shows only the pre-existing `corpus/QUALITY.md` modification and the orchestrator's
untracked `.ufo/waves/round-95/` files; the lane tip is still `673d1e2e6f850bb54dda9698cf825cf6788c7d0d`.

## Behavior delivered

**1. S270 row** (`corpus/SOURCES.md`, appended after S269 at line 211; 195 → 196 rows):
URL `https://docs.python.org/3/library/unittest.html`; kind `docs`; tier **A** (official Python
docs, the primary authority for the scope); scope = what separates a test *error* (unexpected
exception) from a test *failure* (explicitly signalled) for a kill counter; anchor = the
`TestResult.errors` entry (HTML line 2410, anchor id `unittest.TestResult.errors`, body 2412–2414)
and the `TestResult.failures` entry (HTML line 2418, anchor id `unittest.TestResult.failures`, body
2420–2422), the located quote at 2413–2414, the counterpart at 2421–2422, the page's version pin
`Python 3.15.2 documentation` (line 20) and footer `Last updated on Nov 05, 2026 (22:32 UTC)`
(line 3179), fetched 2026-11-05, HTTP 200, 336978 B, sha256
`f9510cd7d7a67a32fb891016cbb42bf1dfcb80a370c689ed222058acbff3506d`; status `mined`; opened
2026-11-05; recheck `90d`; used-by `corpus/lessons/round-95.md,plans/round-95.md`. No `|` inside any
cell — the row is 11 columns, NF = 13 (verified by splitting the row: 13 fields).

**2. `corpus/lessons/round-95.md`** — the scaffold, author ScribeCorpusR95, with `## Gate`
(S270 admitted with URL, access date, HTTP, bytes, sha256 and a ≤25-word located quote + its word
count; S260 re-opened as corroboration with its quote and **no new row**, with the reason given —
the registry already holds that URL at S260, and round-94 closure defect 1 says a frozen plan naming
a row must not force an admit; one same-round **REJECT** from the scout's candidates — the Apache
Ant `junit` task manual — with its observed-fact reason and its flip condition), `## Mistakes` (the
one `run-error-scored-as-kill` row: evidence `.../round-94/w1/CriticClaimsR94.md` **D8**,
captured-by `none`, fix = rule 1 of `verifiers/fixtures/round-95/selftest-kills.py`, shown able to
fail by `.../receipts/forgery-f6-crash-report.txt` — `run errors 1`, `C1-PREDICATE-UNMET`),
`## Status changes` (none — append-only, and the seat's ownership is append-rows-only; the optional
S260 used-by addition is named for the L1 as old→new), `## Sources`, `## Considerthese`
(`considerthese/2026-10-26.md` re-read; proposals 1, 2 and 3 named as still unimplemented with the
measured reasons and why none is taken this round), and `## Settlement` (an explicit L1 placeholder).

**3. `corpus/README.md`** — one index row for the new lesson only, in the shape of the round-94 row:
`| Round-95 lesson | \`lessons/round-95.md\` | … |`.

## Gates run and observed lines

```
$ git -C "$D" add -A -- corpus/SOURCES.md corpus/lessons/round-95.md corpus/README.md
$ git -C "$D" diff --cached --binary 673d1e2e6f850bb54dda9698cf825cf6788c7d0d > …/ScribeCorpusR95.patch
$ git -C "$D" diff --stat 673d1e2e6f850bb54dda9698cf825cf6788c7d0d HEAD
 corpus/README.md           |   1 +
 corpus/SOURCES.md          |   1 +
 corpus/lessons/round-95.md | 174 +++++++++++++++++++++++++++++++++++++++++++++
 3 files changed, 176 insertions(+)
```

**Patch applies on a second fresh clone** (clone → checkout 673d1e2e → `git apply --check`):
`APPLY-CHECK OK`, then `git apply` → ` M corpus/README.md`, ` M corpus/SOURCES.md`,
`?? corpus/lessons/round-95.md`; the verification clone was removed afterwards.

**Census — the seat's required gate** (receipt `census-before.txt` / `census-after.txt` /
`census-verify.txt`):

```
$ bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file "$D/corpus/SOURCES.md"
rc=0   W04 count: 34   E codes: 0
file	ok	/…/repo/corpus/SOURCES.md
```
Before the row: rc 0, **34** `W04`, 0 `E`. After: rc 0, **34** `W04`, 0 `E` — **no new `W04`**
(S270's URL is new to the registry) and no `E`-code. Rows 195 → 196;
`awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF!=13 {n++} END{print n+0}'` → 0
malformed rows. The same validate re-run on the freshly-patched verification clone also reads rc 0,
34 `W04`, 0 `E`.

**No-harm on the corpus verifiers** — the two corpus instruments were run on the patched clone and
on a pristine clone at the same freeze commit, and the readings are identical:

```
patched : index tracked_files=196 index_tokens=210 unindexed=4 stale=0 missing=0
          points candidates=166 checked=156 dead=1
          commits candidates=79 citations=68 hex=68 nonhash=0 unresolvable=1 external=2
baseline: index tracked_files=195 index_tokens=209 unindexed=4 stale=0 missing=0
          points candidates=166 checked=156 dead=1
          commits candidates=79 citations=68 hex=68 nonhash=0 unresolvable=1 external=2
```
The 4 unindexed files, the 1 dead report pointer and the 1 unresolvable commit are **pre-existing**
(the round-91…94 verifier spot-check lessons and `corpus/lessons/round-81.md`) and are unchanged by
this patch; `verify_corpus_integrity.py` prints the same set (rc 0 with the same pre-existing
findings). `verifiers/check_sources_append_only.py` prints the same `19 change(s) in 9 of 61 commits`
at the patched clone and at the baseline — my append raises **no** breach, and no `S269`/`S270`
line appears in its breach list.

**No frozen instrument touched.** `git diff --stat 673d1e2e… HEAD` names three corpus files only;
`verifiers/check_mutation_battery.py`, `verifiers/fixtures/round-95/*` (including the frozen
counter, whose sha256 is still `d6ae74af40135f9b30b0101d5a195a3d950b6a72073020ac59ba58da1d269001`),
`verifiers/fixtures/round-9*/`, `verifiers/fixtures/mutation-battery/manifest.tsv`,
`plans/round-95.md` and `SKILL.md` are byte-identical to the freeze commit.

## Evidence — the sources, fetched independently

Three independent readings of each page agree on one value (this seat, the scout, and the plan's
own record):

| page | HTTP | bytes | sha256 | plan/scout agreement |
|---|---|---|---|---|
| `docs.python.org/3/library/unittest.html` | 200 | 336978 | `f9510cd7d7a67a32fb891016cbb42bf1dfcb80a370c689ed222058acbff3506d` | plan's S270 record = MATCH; scout §1a = MATCH |
| `stryker-mutator.io/…/mutant-states-and-metrics/` | 200 | 27068 | `8641c38959222238f34aba0e20d3c51919cf183bf19a53f436257614cab656da` | plan's S260 record = MATCH; scout §1b = MATCH |
| `ant.apache.org/manual/Tasks/junit.html` | 200 | 33365 | `3f1ee369f541938791d02b8a09506e48ef33472bccb6c237c4280730c7bcc4a1` | scout §4 = byte-identical |

Located quotes (line numbers are lines of the fetched bytes; full record in
`…/ScribeCorpusR95/fetch-record.txt`):

- `unittest.html` line 2413–2414 — "Each tuple represents a test which raised an unexpected
  exception." — **10 words** (`wc -w` → 10); quote-equal after joining the fold after "an".
- `unittest.html` line 2421–2422 — "Each tuple represents a test where a failure was explicitly
  signalled using the assert* methods." — **15 words**; quote-equal after joining the fold after
  "failure" and taking the rendered link text of the `assert* methods` span.
- `stryker-mutant-states.html` line 24 — "The running of the tests resulted in an error (rather than
  a failed test)." — **14 words**; the `Killed` sentence at line 12, where S260's row says it is.
- `ant-junit.html` line 104 — "Stop the build process if a test fails (errors are considered
  failures as well)." — 14 words; `grep -ic 'unexpected exception' ant-junit.html` → **0** — the
  observed fact on which the Ant page is rejected.

## Findings

1. **The Ant `junit` manual is a same-round reject, on an observed fact.** It defines no
   error-vs-failure split (0 hits for "unexpected exception") and its only statement on the subject
   conflates the two — the opposite of what rule 1 rests on. Flip condition recorded in the lesson.
2. **Two scout candidates are admissible but were not written**: pytest's exit codes
   (`docs.pytest.org/en/stable/reference/exit-codes.html`, HTTP 200, 25787 B, sha256
   `a403306a1d763fc8123749544905dd64e8e0cfa5ed46a416679001c3142e3977`) and the TAP 13 specification
   (`testanything.org/tap-specification.html`, HTTP 200, 22741 B, sha256
   `d4d82502f11cae2bad4960586cb2a7bbead03bd55eabe1d85c76c86266d9b09a`). The pytest page is
   **process-level only** — it does not define the within-run error-vs-failure split, so it cannot
   ground rule 1; the TAP page is protocol-side. This seat's ownership is the single row S270, so
   neither is written; they are left for a later round as the scout proposes.
3. **The scout's first pytest guess was wrong and the correction is recorded**:
   `…/explanation/exit-codes.html` → **404** (2531 B error body), real path found from the reference
   toctree. The mutmut README URL → **404** (14 B), reproduced.
4. **The fleet-root `considerthese/` path named in the item does not exist**; the lane's own
   operator-authored directory is `/home/vgpnk/Projects/shokunin/kotoba-shokunin/considerthese/`
   (read-only, never written by this seat), and its latest file is `2026-10-26.md` — the same file
   the round-94 lesson cites. That is the file re-read for `## Considerthese`.
5. **The `SKILL.md` line box is at its limit, so no corpus row can land in it this round** — 600
   lines / 92672 B, 165 lines over 120 characters, 94 over 300, longest 1491 at line 518; the
   `## Gate registry` section is 37417 B of the file (40.4 %). This is the measured reason
   `considerthese/2026-10-26.md` proposal 2 (move the registry out) and proposal 3 (rewrite the
   frontmatter description) are **not taken** this round, and it is the ratchet Q78 asks for.
   Proposal 1's byte ceiling has no instrument holding it.

## Out of scope (not done, and why)

- **No second SOURCES row.** The scout's two admit-worthy candidates (pytest, TAP) are recorded in
  the lesson's Gate with their digests and left for a later round; this seat's ownership is one row.
- **No edit to S260's cells.** Its re-open verified the anchor against the current bytes; the
  `used-by` addition is named in `## Status changes` as an old→new the L1 may make at settlement
  (the round-94 precedent for S262), because this seat's ownership is append-rows-only.
- **No settlement content.** `## Settlement` is an explicit placeholder for the L1, as the item
  specifies.
- **No tool installs.** `curl`, `sha256sum`, `stat`, `awk`, `grep` and `git` were sufficient; nothing
  was installed or upgraded, so there is nothing to record under the operator tooling rule.
- **No host or kernel setting touched**, no `pacman` transaction (host-wide pause respected), no
  process left running.

## Risks

- The lesson is a **scaffold**: the settlement, the claim verdicts and the wave disposition are the
  L1's to write. The `## Settlement` section is explicitly marked as a placeholder.
- **S270's `recheck` is `90d`** (the cadence the sibling doc rows use). The page pins its version
  (`Python 3.15.2`) and its last-updated footer, so a re-fetch can relocate every cited line; the
  row names the digest so a changed page is detectable.
- The 4 pre-existing corpus-index drifts and the 1 dead report pointer are **not** mine and are
  **not** fixed by this patch; a reviewer comparing the two readings must not read them as new.
- Two sources were fetched from the network during this seat's run (the pages themselves); the
  counter and the census are network-free, and no instrument was executed with network access.
