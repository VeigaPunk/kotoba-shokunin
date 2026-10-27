# Kb79SM01LineBudget — SKILL.md line budget (Q65), round 79 w1

Seat scope: verify the SKILL.md line-budget arithmetic for round 79's two claims (C1 consistency,
C2 depth), state whether the budget is tight, and cut only if it is. **It is not tight: no cut, no patch.**
Every number below carries its command and its own exit status; receipts are in
`.ufo/waves/round-79/build/Kb79SM01-*` (raw gate output) and
`.ufo/waves/round-79/build/Kb79SM01-measurements.txt` (the ledger).

## 1. How the checklist counts (the instrument, not arithmetic by hand)

`trigger.line_budget` is not a constant: the threshold is read out of the file's own box.

- `verifiers/verify_skill_checklist.py:471-473` — `LINE_BOUND_BOX_RE = file\b[^.\n]{0,40}?\d+[^.\n]{0,20}?lines?\b`
  and `INT_RE`; the first integer in the first box whose text matches is the limit.
- `:1485-1494` `box_line_budget()` returns `("box at line %d")`; `:321` `DEFAULT_MAX_LINES = 600` is used only
  when no box states a bound; `:1496-1506` `check_line_budget()` fails on `if n > limit` — **inclusive**: 600
  passes, 601 fails.
- The binding box is `SKILL.md:285` `- [ ] File ≤ 600 lines; overflow already moved to referenced depth files.`
  and the tool names it at runtime: `(from box at line 285)`.

Measured boundary (own exit codes, `Kb79SM01-r-lb-b600.txt` / `-r-lb-b601.txt`):

| file | command | rc | line |
|---|---|---|---|
| 600-line copy | `python3 -B verifiers/verify_skill_checklist.py --skill <copy> --repo <lane> --check trigger.line_budget` | 0 | `PASS … evaluated 600 — 600 lines within budget 600 (from box at line 285)` |
| 601-line copy | same | 1 | `FAIL … evaluated 601 — 601 lines exceed budget 600 (from box at line 285)` |

The box also defeats `--max-lines` in both directions, measured: 601 lines with `--max-lines 5000` still
rc 1; 592 lines with `--max-lines 100` still rc 0. So neither a flag nor a reworded box can move the limit —
the box text is pinned by hash in `verifiers/checklist-baseline.json` (see §4).

## 2. The arithmetic

`wc -l SKILL.md` → **590** (`wc -c` → 78647 B; `awk 'length>200'` → 129 lines). Headroom = 600 − 590 = **10 lines**.

The plan's promised SKILL.md growth is stated in `plans/round-79.md`:

- C1: two registry rows — `check_gate_registry.py` reports `60 of 62 lane verifiers` at base because
  `check_desc_craft.py` and `check_r75_routed_repairs.py` have no row → **2 lines** (registry rows are one
  physical line each: 60 such rows occupy lines 453-512, one per line).
- C2: one registry row for the new counter + "≤4 rule lines" → **≤5 lines**.

Worst case 590 + 2 + 5 = **597 ≤ 600**, i.e. **3 lines spare**. The seat's cut class is therefore not needed
for the declared work; the budget is *not tight* by the instrument's own comparison.

## 3. The 7 lines, measured rather than assumed (scratch clone at plan commit F1)

Scratch: `/fast/scratch/hyaku/kotoba-r79/Kb79SM01LineBudget/clone`, `TMPDIR` inside it; two conformant rows
appended to the `## Gate registry` table; commit `2d190a8828a859abb0e26b45a05eaf30f11b2f5f`.

- `wc -l SKILL.md` → **592** — exactly +2, no wrapping, no blank separator.
- `python3 -B verifiers/check_gate_registry.py --rev 2d190a88…` → **rc 0**,
  `gate registry rows conformant 62 of 62 lane verifiers; phantom 0`. C1's registry repair is complete at a
  rev where the C2 counter does not exist yet, so the plan's landing order (C1 alone, measured on its own) holds.
- A 597-line probe (same two rows + five top-level prose lines, standing in for C2's row and ≤4 rule lines),
  run against the **lane** root so citations resolve against the real fleet:
  `--repo <lane>` full run → **rc 0**; `PASS trigger.line_budget … 597 lines within budget 600`;
  `PASS checklist.box_map_complete … 45 boxes`; `PASS trigger.citation_resolves … 214 repo-rooted citation
  token(s) resolve`; `N/A governance.citation_resolves` (that check runs only with the repo SKILL.md).
- The same in-clone comparison at F1 vs the 592 commit `8a13e30f…`: the FAIL set differs only in the line
  number of a pre-existing scratch-path artifact (`../.ufo/reports/round-7/kotoba.md`, line 580 → 582), which
  is green in the lane; no new red is introduced by the rows.

## 4. Two measured traps for the L1's C1/C2 commits

1. **Pinned-values cell.** `check_gate_registry.py` requires every backticked path in the pinned-values cell to
   exist at the measured rev (`git cat-file -e`). `check_desc_craft.py`'s own `ENTRY` constant is
   `corpus/knowledge/description-craft-round76.md`, and that file is **not committed** at F1
   (`git cat-file -e F1:corpus/knowledge/description-craft-round76.md` → exit 128; the counter itself prints
   `description craft backed 0 of 6`, rc 1 — r76's honest stop). A row that copies the constant into the pinned
   cell measures **61 of 62, rc 1** (scratch commit `b9e0a2e3…`). The row must pin paths that exist
   (e.g. `.ufo/waves/round-76/snapshots/MANIFEST.sha256`, `…/fetch-record.json`) and leave the counter's red
   to the counter.
2. **Where the rule lines land.** Both are `checklist.box_map_complete` FAILs, measured with the lane's real map:
   appending one *indented* continuation line to the line-budget box → `map entry trigger.14 has no live box …
   unmapped box at line 285`, rc 1; inserting a new `- [ ]` box → `unmapped box at line 285`, rc 1
   (evaluated 46). Column-0 prose outside boxes (the 597 probe) → `PASS`, 45 boxes. C2's ≤4 rule lines must be
   top-level prose, never a box continuation and never a new checklist box.

## 5. Why no cut is proposed (the stated class is empty)

The seat's candidate class was "duplicated prose that a knowledge entry already holds verbatim (the round-72
move pattern)". Swept, not assumed:

- `python3 -B .ufo/waves/round-79/build/Kb79SM01-dupsweep.py` → rc 0, **4** prose lines with a ≥12-token
  verbatim run: `SKILL.md:113`, `:127`, `:422`, `:424`. Each is the *knowledge entry* quoting or naming
  SKILL.md (`sibling-overlap-census-round74.md:103` carries the cell `SKILL.md:127 chang…`;
  `skill-overlap-levers-round51.md` restates the same round-50/51 error pattern and names the entry), i.e.
  reverse citations, not movable duplicates. A 6-token scan hits 111 lines, but those are table cells and
  shared vocabulary (client and file names) that the decision tables and the gates read.
- Census of the 590 lines: `45` checklist boxes (152 lines inside them) — every box is pinned by text hash in
  `checklist-baseline.json`; `151` table rows (60 of them gate-registry rows that `check_gate_registry.py`
  parses; the surfaces tables are read by `check_agent_definitions.py`, `check_plugin_manifests.py`,
  `check_command_files.py`, `check_hook_files.py`, `check_scoped_rules*.py`,
  `check_description_thresholds.py`, `check_explicit_invocation.py`, `check_spec_craft.py`,
  `check_cn_vendor_surfaces.py`); `308` prose lines; `65` blank; `21` headings.
- Therefore the round-72 pattern has no unapplied instance: SKILL.md already points at its depth files rather
  than restating them. The only remaining line classes are hash-pinned boxes, gate-read rows, pointer lines and
  prose with no verbatim duplicate — no cut would keep "no pointer, no quote, no row a gate reads" while
  freeing a line. Cutting anyway would also shift the SKILL.md line numbers that this wave's other seats cite
  in receipts (a consistency cost with zero budget benefit).

## 6. Operability notes for the rest of round 79

- SKILL.md's 600-line bound is load-bearing for **C1**: `verify_skill_checklist.py` is one of the six gates in
  the frozen tip battery (`receipts/tipbattery-base-dot.txt`: `guards 5 of 5; tip battery exit 0: 1 of 6`,
  `exit=1`). At 597 the file passes; 598, 599 and 600 also pass (measured: 600 rc 0) and line 601 is the first
  red, so **four** unplanned lines past 597 red `trigger.line_budget`, hence the checklist gate, hence C1.
  Treat the 3 spare lines as a hard reserve for C2's rule and nothing else.
- The wave's own no-harm battery line `wc -l SKILL.md ≤ 600` is the same bound, not a second one; no gate pins
  SKILL.md bytes or long-line count (sweep of `verifiers/*.py` for a second numeric SKILL.md bound found none;
  the only SKILL.md size check is the box). Base figures for the plan's considerthese proposal-1 measurement:
  78647 B, 129 lines > 200 chars.
- Not run by this seat (not its item, and not a substitute for the L1's battery): `check_tip_battery.py`,
  the corpus gates, `check_assertion_floors.py`. No tool installed or upgraded. SKILL.md is byte-identical to
  base and F1 (`sha256 7b1263b5…`), and no lane file outside `.ufo/waves/round-79/` was written.

VERDICT: Not tight — 590/600 with the plan's 7-line promise landing at 597 and 3 lines spare (600 inclusive, 601 fails); the duplicated-prose cut class is empty (4 hits, all reverse citations), so nothing was cut and no patch is delivered; two measured traps recorded for the C1 pinned-values cell and for where C2's rule lines may land.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/w1/Kb79SM01LineBudget.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79SM01-measurements.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79SM01-dupsweep.py, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79SM01-dupsweep.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79SM01-r-gr.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79SM01-r-gr-trap.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79SM01-r-sc-F1.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79SM01-r-sc-H3.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79SM01-r-sc-k592-lane.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79SM01-r-sc-k597-lane.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79SM01-r-sc-k592-map.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79SM01-r-sc-k597-map.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79SM01-r-lb-b600.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79SM01-r-lb-b601.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79SM01-r-lb-b601-max5000.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79SM01-r-lb-k592-max100.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79SM01-r-bm-wrap.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79SM01-r-bm-newbox.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79SM01-fails-F1.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79SM01-fails-H3.txt
