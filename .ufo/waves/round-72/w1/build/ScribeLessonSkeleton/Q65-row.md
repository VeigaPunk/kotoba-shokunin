# QUALITY row draft — Q65 (for `corpus/QUALITY.md`, table after Q64 at line 80)

Status: **draft**, produced by seat `ScribeLessonSkeleton` in round-72 wave 1. Not landed; the L1
lands it. It is the criterion for **M124**, which this draft found to have `none` in the existing
bar (the other two mistakes map to Q50 and Q09 — see the lesson skeleton).

Table form (five cells, `corpus/QUALITY.md:9` header: `| id | criterion | applies to | grounded in |
supersedes |`):

| Q65 | A plan's no-harm battery is run at the plan's own base before the plan freezes, and every value the plan promises for the tip is either measured at that base or struck before data; a promised row add is checked arithmetically against the file's stated ceiling at that base, so a row that needs freed lines and frees none is not a plan item. Extends Q19, which binds a carried **before**-value only. | claim plans' § No-harm battery, promised tip values and row-add arithmetic; lesson `## Gate` | M124 (`corpus/lessons/round-72.md` § Mistakes: the r71 plan promised `check_gate_registry.py --rev <tip>` "(53 of 53)" at `plans/round-71.md:171` while its own base reads `conformant 51 of 53` and the two rows never existed in any commit; its report battery ran three of the plan's six items — `.ufo/reports/round-71/kotoba.md:53-56`; `SKILL.md` 600 lines / 72,688 B at the base). Red-before: `.ufo/waves/round-72/receipts/base-battery.txt` (`check_gate_registry exit=1`; `SKILL.md lines: 600  bytes: 72688`). Fix shown able to fail: `<<C3 counter base receipt, 2 of 6>>`. | — |

## Why no existing row covers it

- **Q19** (`corpus/QUALITY.md:30`) — "A carried or planned before-value is re-measured at round start
  and printed with its command and commit". The r71 plan's `53 of 53` is a promised **after**-value;
  Q19's scope cell names `planned` rows and plan before-columns, not promised tip values.
- **Q36** (`:47`) and **Q50** (`:61`) — both bind a result a report **states**: Q36 requires a cited
  receipt to name its own revision, Q50 requires a committed receipt naming the exact tip. Neither
  binds a gate the plan listed and the report omitted, nor a row add promised past a line ceiling.
- **Q63** (`:79`) — binds a counter item run on an honest world, not a plan's own battery.
- Hence `none`, and M124's mechanism is the class this row carries.

## Checks this row's landing can be tested with

```sh
# the promised value is measured at the base, not copied
python3 -B verifiers/check_gate_registry.py --rev c69711ee08279609374d895bb0f3c8c18ccf15c9 | tail -1
# -> gate registry rows conformant 51 of 53 lane verifiers; phantom 0   (the promise read 53 of 53)
# the row add was never committed
git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin log --oneline -S'check_skill_evals_v2' -- SKILL.md   # prints nothing
# the ceiling the promise had to be checked against
tail -1 /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-72/receipts/base-battery.txt
# -> SKILL.md lines: 600  bytes: 72688
```
