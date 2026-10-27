# Round 76 — addendum 1 (pre-data correction to the frozen C1 conjunct list)

Date: 2026-10-27, after wave dispatch, before any data lands. Author: L1 `KotobaR76`.

## Correction

`plans/round-76.md` C1 conjunct (a) as written requires the optimizing-descriptions snapshot digest to
"equal the digest recorded in the S213 row's anchor update". That clause is **withdrawn**: the SOURCES
contract (CORPUS.md rule 2) permits in-place changes only to `status`, `recheck` and `used-by` — the
`anchor` cell may not be edited in place, and a new row for the same URL would be a duplicate (census
E04 family). The snapshot digest is therefore pinned in four places instead:

1. `.ufo/waves/round-76/snapshots/MANIFEST.sha256`,
2. `.ufo/waves/round-76/snapshots/fetch-record.json` (HTTP 200 record dated 2026-10-27),
3. the pinned digest table inside `verifiers/check_desc_craft.py`,
4. the round-76 lesson `## Gate` access record (URL, access date, ≤25-word located quote) — per contract rule 1.

The frozen headline `description craft backed 6 of 6` is unchanged; conjunct (a) now reads: the snapshot
set's digests appear identically in (1)–(4). Counters and seats implementing conjunct (a) must implement
this corrected form. The registry change this round remains the S213 `used-by` append only (logged old→new
in the lesson).

## Render-length convention (off-by-one closure)

Seat `B21RevMethod` measured the r75-tip description on committed bytes and found two conventions one
character apart: YAML folded-scalar render with clip chomping (trailing newline kept) = **1022**; the
stripped variant = **1021** (the same 1021 the lane's `check_sibling_census.description_of` guard prints
for the same bytes). The frozen targets that read this number — R1's "prints 1022" and C1 conjunct (d)'s
recompute — fix the convention as **clip-preserving (`len(yaml.safe_load(...)['description'])`, trailing
newline kept) = 1022 at the r75 tip**, which is also the r75 closure's measurement. Every receipt that
prints the number must print both variants (clip 1022 / stripped 1021) and name the convention, so the
off-by-one family that produced M75-1 cannot re-enter through measurement ambiguity. This names the
convention; it does not move either predicate.

## Reason
## Wave role correction (validated topology)

The initial planning estimate listed `labrat` and `sonic` as top-level seats. The validator refused
both roles (`unknown_role`); neither was dispatched. Their probe/read tasks were re-roled to
`scout`/`scribe`/`simplifier`. The validated and dispatched 64-seat mix is: executor 15, scribe 10,
reviewer 10, scout 10, critic 6, mutation-tester 4, simplifier 3, revenger 3, sentinel 2, connector
1. Attack roles (reviewer + critic + mutation-tester + sentinel) are 22/64 = 34.4%, above the 25%
minimum. The L1 remains the canonical planner; B01 carries the planning data-walk.

Caught by L1 self-review against CORPUS.md rule 2 before data; no seat output has been scored against
the withdrawn clause. This addendum is the committed record of the correction (Q28 discipline: the
counter's conjunct table and the plan now agree on this form).
