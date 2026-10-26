# ScribeLessonProvinceR74 — round-74 wave-1 bookkeeping blocks

**Verdict: delivered.** Six bookkeeping blocks drafted at
`.ufo/waves/round-74/w1/build/ScribeLessonProvinceR74/blocks.md` (251 lines, 23,833 B; `wc -lc` below), every
data-dependent value `<<…>>` (161 placeholders). No lane file edited, no gate run, no network fetch, no number
invented, no scratch directory created. Before-values are quoted from `plans/round-74.md` and labelled as
plan-stated, not as receipts: the C1/C2 do-nothing receipts do not exist yet (`ls .ufo/waves/round-74/receipts/`
lists five files, neither is one).

## Deliverable

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin && wc -lc .ufo/waves/round-74/w1/build/ScribeLessonProvinceR74/blocks.md
    251 23833 .ufo/waves/round-74/w1/build/ScribeLessonProvinceR74/blocks.md
$ grep -o '<<[^>]*>>' .ufo/waves/round-74/w1/build/ScribeLessonProvinceR74/blocks.md | wc -l
161
```

Blocks, in landing order: (0) a fill map, placeholder class → the one command/file that settles it; (1)
`corpus/lessons/round-74.md` skeleton — front matter, Claims with both frozen predicates verbatim and
`329e7d91d7d750031c35d264f0e34af1d0ce8385` as the freeze commit, `## Gate` (id collision, renumber map by
document, guard proof, three row slots with URL/snapshot/access date/HTTP/bytes/sha/quote, Q45 census, admitted,
entry rewrites, rejected with flips, S236/S237 quarantine verdicts, spot-check sample, considerthese item 4),
`## Mistakes` header only, `## Routed defects` (seven r73 items), `## Round honesty`, `## Falsify corrections`,
`## Status changes`; (2) the SCORECARD Round-74 annotation paragraph in the Round-73 shape; (3) two Move-log rows
in the round-55 shape; (4) the `## Round 74` LOG entry in the Round-73 shape; (5) three `corpus/README.md` index
rows plus two Frontier append-only notes; (6) four SHONEN evidence-line proposals, boxes `[~]` unchanged.

## Findings

**F1 — house form has a sixth section the brief does not name.** Command and output:

```
$ grep -n '^## ' corpus/lessons/round-73.md corpus/lessons/round-72.md
corpus/lessons/round-73.md:16:## Gate
corpus/lessons/round-73.md:72:## Mistakes
corpus/lessons/round-73.md:83:## Routed defects (r72 spot-check § 6)
corpus/lessons/round-73.md:92:## Round honesty
corpus/lessons/round-73.md:98:## Falsify corrections
corpus/lessons/round-73.md:102:## Status changes
corpus/lessons/round-72.md:9:## Gate
corpus/lessons/round-72.md:70:## Mistakes
corpus/lessons/round-72.md:90:## Round honesty
corpus/lessons/round-72.md:96:## Status changes
```

`## Round honesty` exists in both exemplars, between `## Routed defects` and `## Falsify corrections`; round 72 has
no `## Routed defects`/`## Falsify corrections` at all. The skeleton keeps `## Round honesty` and carries a
house-form note saying the L1 may drop it, but that dropping it departs from both exemplars.

**F2 — the Move log stops at round 55; rounds 56–73 are absent.** The table is `SCORECARD.md:185-305`, and the
highest round in it is 55:

```
$ awk -F'|' '/^\| [0-9]+(-[0-9]+)? \|/{gsub(/ /,"",$2); print $2}' SCORECARD.md | sort -n | tail -4
54
54
55
55
```

The two round-55 rows are at `SCORECARD.md:304-305`, which is why they are the shape exemplar. Appending two
round-74 rows continues a table with an 18-round gap; the draft says so and proposes no backfill (out of scope for
a scribe).

**F3 — both planned counters and the snapshot directory are absent at HEAD.** Values that depend on them are
placeholders, including the two frozen sha256 cells:

```
$ ls verifiers/check_spec_craft.py verifiers/check_sibling_reread.py
ls: cannot access 'verifiers/check_spec_craft.py': No such file or directory
ls: cannot access 'verifiers/check_sibling_reread.py': No such file or directory
$ ls .ufo/waves/round-74/snapshots
ls: cannot access '.ufo/waves/round-74/snapshots': No such file or directory
$ ls plans/round-74*
plans/round-74.md
```

So the skeleton cannot name a freeze revision for either counter, a snapshot file, an access date or a quote; all
of those are `<<…>>` with the settling command named in the fill map.

**F4 — routed item 2 is already done in the plan commit; the draft does not repeat it.** Read-only git:

```
$ git log --oneline -4
329e7d9 (HEAD, origin/master, origin/HEAD, master) round-74: plan, base receipts, index r73 closure file, id scratch, sibling freeze heads
1e03d19 round-73 verifier spot-check (integrator, hyaku): non-author admit/reject
ec756f6 round-73: tip receipts (battery both forms 6 of 6, C1, no-harm battery)
da9eb0b round-73: wave-1 seat reports, results, ready marker
$ git diff --stat 1e03d1991bc02281b00a5b7a5e00c9d5d5d72908 329e7d91d7d750031c35d264f0e34af1d0ce8385
 corpus/README.md                                   |   1 +
 plans/round-74.md                                  | 174 +++++++++++++++++++
 verifiers/corpus-baseline.json                     |   5 +-
<<nine .ufo/waves/round-74/ receipt and assimilation lines elided here; the command printed all twelve>>
 12 files changed, 690 insertions(+), 2 deletions(-)
$ git diff 1e03d19 329e7d9 -- corpus/README.md | head -4
@@ -141,6 +141,7 @@ Domain: prompt & skill craft — SKILL.md/AGENTS.md quality, trigger fidelity.
 | Round-72 verifier spot-check (closure) | `lessons/round-72-verifier-spotcheck.md` | ...
+| Round-73 verifier spot-check (closure) | `lessons/round-73-verifier-spotcheck.md` | ...
```

The added line is the r73 closure index row (`corpus/README.md:144`). The lesson's `## Routed defects` item 2
records it as done and does not add a second row.

**F5 — the id-collision figures in the skeleton are measured, not copied.** Command and output:

```
$ wc -l .ufo/waves/round-74/assimilation/{reg-ids,staged-ids,collisions,quarantine-slice}
 148 reg-ids
 188 staged-ids
  20 collisions
  13 quarantine-slice
$ head -1 collisions; tail -1 collisions
S203
S222
```

148 lane ids, 188 staged ids, 20 collisions `S203`–`S222`, 13-row quarantine slice — the plan's numbers hold at the
plan commit. The quarantine slice files S236 and S237 under "the cited source could not be fetched, so no quote was
checked"; the skeleton keeps both as *verdict* placeholders rather than accepting that class, since the same pages
are this round's C1 sources.

**F6 — the base figures are plan-stated; the do-nothing receipts are not committed.** The plan's § Before-values
table gives C1 `0 registry rows; 0 hits …` and C2 `20 rows; 15 of 20 … differ …, pins 50–312 commits behind`; the
`spec craft pages backed 0 of 3` and `sibling rows re-pinned and re-read 0 of 20` come from the two § "Do-nothing
control" sentences. Receipts on disk:

```
$ ls .ufo/waves/round-74/receipts/
base-battery-l1.txt
base-sweeps.txt
census-before.txt
sibling-heads-freeze.tsv
sibling-staleness-base.tsv
```

No C1/C2 base receipt. Every before-cell in the draft is therefore written as plan-quoted with the receipt path as a
placeholder, so the landed text cannot imply an unrun measurement.

**F7 — census and freeze receipts check out.** `census-before.txt` is exit 0 with 148 rows and 20 W04 duplicate-URL
warnings (`grep -c 'W04' …` → `20`); the freeze file carries 20 lanes between two comment lines
(`grep -vc '^#' sibling-heads-freeze.tsv` → `20`; `wc -l` → 22). The head row for `chousa` shows head
`00f8c7f5…` against the r49 pin `6c5eb146`, matching the staleness receipt's `commits_since_pin=213`.

**F8 — SHONEN has exactly four boxes, all `[~]`** (`grep -c '^- \[~\]' SHONEN.md` → `4`), matching routed item 7.
The four proposals touch only evidence text and keep `[~]`; box 3's proposal is explicitly *no new evidence*.

**F9 — staged entry names verified against the package, not the plan's prose.**

```
$ ls /home/vgpnk/Projects/shokuknow/merge/kotoba/knowledge/corpus/knowledge/ | grep -i 'spec-\|script-craft\|description-trigger'
spec-description-trigger-discipline.md
spec-eval-file-format.md
spec-repo-governance-round7.md
spec-script-craft-rules.md
```

The plan names `spec-script-craft-rules.md` and `spec-description-trigger-discipline.md`; both exist. Read-only:
no write, no fetch inside the package.

**F10 — the r73 routed-item anchors were wrong in the first draft and are corrected.** The authoritative lines:

```
$ grep -n 'Falsify wave\|Index this file\|Correct D2\|Structural guard\|Fold C1\|compare_harness_independent\|Operator note' corpus/lessons/round-73-verifier-spotcheck.md
157:  1. **Falsify wave, for the second time:**
159:  2. **Index this file** …
161:  3. **Correct D2 in an appended correction** …
164:  4. **Structural guard for M129** …
166:  5. **Fold C1 into `SKILL.md`** …
168:  6. **`compare_harness_independent.py` exit 2** …
170:  7. Operator note: …
$ wc -l corpus/lessons/round-73-verifier-spotcheck.md
172
```

The skeleton now cites `:157`, `:159`, `:161`, `:164`, `:166`, `:168`, `:170` and the section range `:155-172` (my
first pass cited shifted ranges `:157-159`, `:160-161`, … — a draft-only defect, caught before filing).

**F11 — no lane file was touched.** `git status --porcelain` lists only untracked paths under
`.ufo/waves/round-74/` (other seats' generators, dispatch records and `w1/`), and `git diff --stat` is empty. The
deliverable is inside `w1/build/ScribeLessonProvinceR74/`, which is the permitted draft surface.

## Behaviour and gates

- Read: `plans/round-74.md`, `corpus/lessons/round-72.md`, `round-73.md`, `round-73-verifier-spotcheck.md`,
  `SCORECARD.md` (`:185-305`, `:464`), `LOG.md:2783-2799`, `corpus/README.md` (`:128-144`, `:215-227`), `SHONEN.md`,
  `PROVINCE.md`, `corpus/QUALITY.md:78`, `SKILL.md` section map, the round-74 receipts, the assimilation scratch and
  the staged package (listing + two greps).
- Wrote: only `.ufo/waves/round-74/w1/build/ScribeLessonProvinceR74/blocks.md` and this report.
- Gates: **none run** (not this seat's assignment). The draft's no-harm cells for `check_gate_registry.py`
  (`60 of 60` is the plan's target, base count unmeasured here) and the tip battery are placeholders, not claims.
- Network: none. Tooling installed: none. Scratch dirs: none.

## Out of scope / left to the L1

- Whether the Q45 census lowers `N == 3` before data; the renumber map, guard proof, snapshots, access dates and
  quotes; the admit/refuse verdicts (a refusal needs an observed fact, Q62 at `corpus/QUALITY.md:78`); the two
  counter sha256 values; any Move-log backfill for rounds 56–73.
- `<<C1-HELD>>` is a placeholder because the counter's `held at base:` print does not exist yet; the plan's C1
  do-nothing figure is `0 of 3`, which the draft attributes to the plan, not to a run of mine.

## Known limits (calibration)

- A skeleton cannot be scored on freshness; its only freshness content is that every anchor was re-read at the plan
  commit (F4, F5, F7, F10) while the plan's own before-values are carried as quotations, not measurements.
- The one place the draft goes beyond the brief (`## Round honesty`) is flagged in place, so the L1 can drop it
  without hunting.
