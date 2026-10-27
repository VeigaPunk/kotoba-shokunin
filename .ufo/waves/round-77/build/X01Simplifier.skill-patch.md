# SKILL.md patch — cut (X01Simplifier, round 77 w1)

Cut of `.ufo/waves/round-76/build/skill-patch.md` (B13SkillPatch). **Three rows, the same anchors,
the same three inserted lines**; only the cell text shrank. Apply to the r77 base
`6523aced1ee0ebe07dca996213bdc645a6acbd1e` (`SKILL.md` **590** lines).

## Measurements (rendered characters, `len()` of the exact line)

| row | draft | cut | delta | draft words | cut words |
|---|---|---|---|---|---|
| § Body craft rule row | 447 | 395 | -52 | 65 | 56 |
| `check_desc_craft.py` registry row | 1156 | 822 | -334 | 148 | 108 |
| `check_r75_routed_repairs.py` registry row | 922 | 760 | -162 | 122 | 95 |
| **total** | **2525** | **1977** | **-548** (-21.7%) | | |

Line budget unchanged: +1 rule row, +2 registry rows → `wc -l` 593 at base 590.

## Anchors, measured at the r77 base (the r76 draft's list is stale in one place)

- Pin 1 insert point: base line **216**, the `confirm discovery before trusting a path` row; the new
  row lands at **217**. (Base 217 is the blank line that ends the table.)
- Pin 2 insert point: base line **512**, the last registry row (`verifiers/check_sibling_reread.py`);
  the two new rows land at **514–515** after the Pin 1 shift. (Base 513 is blank, base 514 is `## Sources`.)
- `## Gate registry`: base **445** → patched **446**. The draft says 448 — wrong; every other number
  in its list was measured on the r76 base and carried forward un-remeasured.
- `## Sources`: base **514** → patched **517**.
- Checklist box `File ≤ 600 lines`: base **285** → patched **286**, text unchanged.
- `SKILL.md` lines: **590** → **593** (`wc -l`).

## Pin 1 — § Body craft rule row (insert after base line 216; before the blank line that ends the table)

```text
| write the description as an imperative about the goal, not the mechanics | S213 optimizing-descriptions; `corpus/knowledge/description-craft-round76.md` | "Err on the side of being pushy": list the contexts the skill serves; "descriptions tend to grow during optimization", so re-check length after each edit; "Avoid adding specific keywords from failed queries" — name the category instead. |
```

Cut from the draft row: `, and err pushy` (the rule then appears verbatim as the third fragment
`"Err on the side of being pushy"` in the same row) and `, including ones the user never names`
(fragment four states it verbatim in the same row). No quote, no pointer, no cell lost: still three
cells, still `S213` + the entry path in the source cell, still three page-unique fragments.

## Pin 2 — § Gate registry rows (append after base line 512, i.e. after the `check_sibling_reread.py` row; before the blank line and `## Sources`)

```text
| `verifiers/check_desc_craft.py` | gate | `python3 -B verifiers/check_desc_craft.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate — round-76 C1 counter (depth), re-landed in round 77: six conjuncts over committed bytes — the pinned snapshot chain and digests, the entry `corpus/knowledge/description-craft-round76.md`'s located page-unique quotes, the `SKILL.md` § Body craft row citing entry and S213, the entry's audit table recomputed from `SKILL.md`, S213's `used-by` plus the round-76 lesson log, and the entry's provenance trio; `description craft backed 6 of 6` at the measured rev, `0 of 6` at the pinned base | `--self-test` | in-file SELF_SHA and page digests; `.ufo/waves/round-76/snapshots/MANIFEST.sha256` | none (read-only); `--self-test` fixture repos under `--work`/`$TMPDIR` (removed) | kotoba |
| `verifiers/check_r75_routed_repairs.py` | gate | `python3 -B verifiers/check_r75_routed_repairs.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate — round-76 C2 counter (consistency), re-landed in round 77: the four round-75 routed defects close on committed content — R1's appended correction in `corpus/lessons/round-75.md` plus the folded-render receipt recomputed from the measured `SKILL.md`, R2's tip-named no-harm receipt cited from `LOG.md` § Round 75, R3's `w2-registry-note.md` reconciliation cited there, R4's appended closing line; `r75 routed repairs closed 4 of 4` | `--self-test` | in-file SELF_SHA and the r75 tip constant; `.ufo/waves/round-76/receipts/` | none (read-only); `--self-test` fixtures under `$TMPDIR` (removed) | kotoba |
```

Both rows keep the registry's eight columns, the entry command, `0=clean, 1=failed, 2=could-not-evaluate`,
the frozen verdict line and the round label. Cut: the exhaustive restatement of each counter's
conjunct list, which is the counter docstring's subject (one authoritative home per fact). Kept:
`--self-test`, the pinned-values location, the write scope and the owner. Proven conformant — see
`X01Simplifier.receipt.txt`, `check_gate_registry.py --rev` prints `62 of 62`, own exit 0 (base: 60 of 62,
own exit 1).

## What a reader loses

Nothing the C1 counter reads. The quote table loses its `page` column (the intro names the single page
once instead of repeating it five times) and uses the lane's `:25`-shorthand location form; the measured
table loses its third column (the convention is stated once in the paragraph above it, with both the
clip and stripped numbers); the `ground:` line keeps the checkable sweep and the old `used-by` state.
