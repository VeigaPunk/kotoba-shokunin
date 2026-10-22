# Falsify ReviewBaselineRerecord — corpus baseline re-record 59903b2 (attack)

VERDICT: HOLDS-BOUNDED — the re-record is honest and fully reconciled; the claim wording
"three files / two pointers added since BASE" counts from the stale round-50 recorded baseline
(a78fec1), not from BASE 43ca0bf, where only 2 files and 1 pointer are new. Both accounting
frames are disclosed in the landed README row, so this is calibration wording, not laundering.

## What moved, measured (private clones at the exact SHAs; lane untouched)

`python3 -B verifiers/verify_corpus_integrity.py --no-baseline --json`, run in
clone@43ca0bf and clone@59903b2 (both exit 1, JSON `observed.corpus`):

| field | BASE 43ca0bf | HEAD 59903b2 | delta |
|---|---|---|---|
| tracked_files | 70 | 72 | +2 |
| corpus_md_files | 69 | 71 | +2 |
| report_total | 45 | 46 | +1 |
| report_pointer_shapes absolute | 41 | 42 | +1 |
| index_patterns | 87 | 90 | +3 |
| unindexed | 1 (round-50-verifier-spotcheck.md) | 0 | fixed |
| report_dead | 2 | 2 | unchanged |
| commit_total | 30 | 30 | unchanged |

Recorded baseline `verifiers/corpus-baseline.json`: `expect` tracked_files 69→72,
report_total 44→46; all other checks untouched (mode `report_dead` stays `zero`).
The 69/44 values were set by a78fec1 (round-50 falsify corrections); a diff of that
baseline file shows ONLY the two expect values changed this round — the stale
`as_of` 2026-09-29 / `measured_against` round-16 provenance block was already stale
at BASE (pre-existing condition, not introduced here; minor hygiene note only).

## The three tracked files behind 69→72

1. `corpus/lessons/round-50-verifier-spotcheck.md` — NOT new at HEAD. It was added by the
   BASE commit 43ca0bf itself (`git log --diff-filter=A` → `43ca0bf round-50 verifier
   spot-check`), i.e. one commit AFTER a78fec1 recorded 69/44. It is the +1 catch-up:
   tracked 69@a78fec1 → 70@BASE → 72@HEAD. Round-50 closure content (author: hyaku closure
   `HyakuCloseKotoba50`, non-author), indexed round 51; the new README row discloses the
   omission verbatim: "landed at `43ca0bfb` without an index row (which turned
   `verify_corpus_integrity.py` red at that base: `unindexed 1`), indexed round 51".
2. `corpus/lessons/round-51.md` — genuinely new at HEAD. Round-51 lesson: C1/C2 claims,
   Mistakes M33/M34, Q27, Gate rows S030–S031, D1–D7 disposition. Verified by reading it.
3. `corpus/knowledge/skill-overlap-levers-round51.md` — genuinely new at HEAD. The C2 entry
   (source rows S030/S031/S025/S022/S024/S029/S021, verified-at 2026-10-22, recheck command
   with per-page sha256 pins plus `check_overlap_levers.py --fetch`). Verified by reading it.

`git diff --name-status 43ca0bf 59903b2 -- corpus`: 5 M (QUALITY, README, SOURCES,
sibling-overlap-census-round49, skill-selection-rules-round50), 2 A (items 2–3), 0 D/R.
`tracked_corpus_files` (verifier's own `git ls-files corpus/` wrapper): 69@a78fec1,
70@BASE, 72@HEAD — matches the JSON counts exactly.

## The two report pointers behind 44→46

Pointer lists rebuilt with the verifier's own code path (`UFO_POINTER_RE` + `is_excluded_pointer`
+ `inside_quotes`, per-line, exactly as `citation_findings` counts `report_total`):

- a78fec1: 44 pointers. → BASE 45: +1 = `corpus/lessons/round-50-verifier-spotcheck.md:10`
  → `/home/vgpnk/Projects/shokunin/.ufo/reports/round-50/kotoba.md` (absolute, live).
  This is the catch-up pointer — on disk at BASE, absent from the recorded 44.
- BASE 45 → HEAD 46: +1 = `corpus/lessons/round-51.md:18` → the same round-50 fleet report
  (the M34 evidence pointer). This is the only pointer new relative to observed BASE.
- Removals: NONE in either hop (set diff `a78fec1→BASE→HEAD` is add-only), so no offsetting
  deletion is hidden inside the +2 total. commit_total stays 30 with 0 unresolvable/nonhash.
- Liveness of the target checked on the real fleet FS:
  `ls -la /home/vgpnk/Projects/shokunin/.ufo/reports/round-50/kotoba.md` → 9,100 B, Oct 22.

## report_dead 2 — same two pointers as BASE: confirmed

`report_dead_detail` is byte-identical at BASE and HEAD:
- `corpus/lessons/round-48-verifier-spotcheck.md:9: .ufo/reports/round-48/kotoba.md`
- `corpus/lessons/round-48-verifier-spotcheck.md:23: .ufo/reports/round-48/kotoba.md`

Both are bare-shape tokens, so `resolve_pointer` resolves them under the citing file's own
directory (`corpus/lessons/.ufo/reports/round-48/kotoba.md`) — absent; the fleet copy of
round-48/kotoba.md does not satisfy a bare token. Pre-existing since round-48, unchanged.

## No laundered drift — gate arithmetic

With baseline (`--json`):
- clone@BASE: exit 1 — DRIFT ×4: tracked_files (70≠69), unindexed (1), report_total (45≠44),
  report_dead (2). The corpus gate was red at BASE for exactly the three re-recordable
  reasons plus the carried dead pair.
- clone@HEAD: exit 1 — DRIFT ×1: report_dead (2) only; 8/9 checks PASS (72=72, 46=46,
  unindexed 0, stale 0, missing 0, commits clean).

So the re-record repairs exactly what a re-record may repair (counts/index), leaves the
zero-mode dead check un-normalized, and adds only additively-explained content. Every added
item is round-51 authored or round-50 closure content now indexed with an honest disclosure.
index_patterns +3 = exactly the three added README rows (spotcheck closure, levers entry,
round-51 lessons); the one modified README row re-characterizes round-50 finding 4 as
superseded — disclosed corpus editing, not a count trick.

## Residual risk / gaps

- Runs were in private clones, not the lane working copy (read-only bounds); the verifier
  reads `git ls-files` + working tree of the checked-out SHA, so content identity holds.
- Absolute pointer liveness hits the live fleet FS; fleet file moves would change
  report_total liveness independently of the lane. Inherent to the instrument, not this commit.
- Baseline `measured_against` provenance block still describes the round-16/17 re-record
  (pre-existing staleness; expect values are the only fields rounds update).
