# E08SourcesUsedBy — the S213 `used-by` change (round 77 w1, build draft)

Status: **draft artifact, applied only in scratch clones.** No lane file was written by this seat.
The patch `E08SourcesUsedBy.SOURCES.patch` applies to lane HEAD
`6523aced1ee0ebe07dca996213bdc645a6acbd1e` and touches one line of `corpus/SOURCES.md`.

## The change — one cell of one row

| item | value |
|---|---|
| file | `corpus/SOURCES.md` |
| row | `S213` (the 138th of 151 registry rows; file line **153**) |
| column | `used-by` = cell index 11 of 11 (13 pipe-fields incl. the two edge empties) |
| status cell | unchanged, remains ` mined ` |
| `recheck` cell | unchanged, remains ` 90d ` |
| `opened` cell | unchanged, remains ` 2026-10-25 ` |
| every other cell | unchanged (verified cell-by-cell; see below) |

Old cell, verbatim (leading and trailing single spaces are part of the cell):

```
 corpus/knowledge/skill-eval-artefacts-round70.md 
```

New cell, verbatim:

```
 corpus/knowledge/skill-eval-artefacts-round70.md, corpus/knowledge/description-craft-round76.md 
```

Separator: **comma + space**, the lane's house style (58 registry rows already carry multi-member
`used-by` cells, e.g. `SKILL.md, corpus/knowledge/frontmatter-rule-authorities-round48.md`) and the
only separator the census splits on (`scripts/sources-census.sh`, `usedby_findings()`:
`IFS=',' read -r -a paths <<< "$usedby"`, then `trim_cell` per member).

## Measured on committed bytes (scratch clone, base 6523ace)

| measurement | old | new | delta |
|---|---|---|---|
| row characters | 810 | 857 | +47 |
| row UTF-8 bytes (excl. newline) | 814 | 861 | +47 |
| row bytes with newline (`wc -c` of the line) | 815 | 862 | +47 |
| sha256 of the row bytes | `72683738c5ea97ee7287ec75f645989350530813d4cbb53bbcf8971b473721a6` | `478c8dfd10b9cb8e8781b7ddbd877815858f99dd09ca44d65dc34f5caf799cda` | — |
| `|`-fields of the row (`NF`) | 13 | 13 | 0 |
| parsed cells | 11 | 11 | 0 |
| registry rows in file | 151 | 151 | 0 |
| file lines | 381 | 381 | 0 |

`+47` is exactly `len(", corpus/knowledge/description-craft-round76.md")` = 45 + 2. The added bytes
are ASCII, so the character and byte deltas agree; nothing else on the line moves.

Cell-by-cell equality check (all 11 cells compared, only `used-by` differs):

```
cells equal except used-by: []
```

Whole-file check: exactly one line differs between base and patched file —

```
changed line numbers [153] len base 381 len new 381
```

## The unified patch

`E08SourcesUsedBy.SOURCES.patch` (6760 B, sha256
`2a05870c2064c015d410e1a6587f506b2964bb85376eccc619e4385a08b8f564`) is
`git diff 6523ace 2015094 -- corpus/SOURCES.md` from the scratch clone. Applied at lane HEAD in a
second independent shared clone:

```
$ git -C <fresh clone at 6523ace> apply --check E08SourcesUsedBy.SOURCES.patch   -> exit=0
$ git -C <fresh clone at 6523ace> apply         E08SourcesUsedBy.SOURCES.patch   -> exit=0
$ cmp <fresh clone>/corpus/SOURCES.md <verified arm-B>/corpus/SOURCES.md         -> identical
```

## Landing constraint (must be honoured by the L1)

The `used-by` cell and the entry `corpus/knowledge/description-craft-round76.md` **must land in the
same commit**: the census resolves every `used-by` member against the lane root and raises `E11`
when the file is absent. Measured three-arm (receipts in `E08SourcesUsedBy.receipts.txt`):

| state | census (`validate --file …/SOURCES.md --today 2026-10-27`) | `check_skill_evals_v2.py` | `check_spec_craft.py` |
|---|---|---|---|
| base `6523ace` | `ok`, 20 W04, exit 0 | `2 of 10`, exit 1 (pre-existing) | `3 of 3`, exit 0 |
| arm A `2015094` (append, entry absent) | `E11 S213 missing used-by corpus/knowledge/description-craft-round76.md`, exit 1 | `1 of 10`, exit 1 (`A10: census validate … non-zero`) | `0 of 3`, exit 1 (`not census-conformant … (conjunct (b))`) |
| arm B `aee7ac0` (append + entry + lesson) | `ok`, 20 W04, exit 0 | `2 of 10`, exit 1 (same single finding as base) | `3 of 3`, exit 0 |
