# CritSourcesSchema — round 67 wave 2

## Scoped verdict

**FAIL: one schema defect survives at the landed tip.** S129 is collision-free but is not the next free id for this three-row append. S123 and S124 pass every assigned check; S129 passes every assigned check except id allocation.

Impacted axis: **calibration** (registry identity and the sufficiency of a collision-only rationale). This finding does not re-measure C1, falsify the external source text, or claim a C2 counter result.

Measured state: `da86c03e482a6aef433c34d733726b37c7cf6607`. `git rev-parse HEAD` printed that full hash; `git status --short -- corpus/SOURCES.md` printed nothing; `git diff --exit-code da86c03e482a6aef433c34d733726b37c7cf6607 -- corpus/SOURCES.md` exited 0. The pinned base is separately `2a8eba56b3f9321b70c569fa2816d42237ca49a2`. A base-to-tip diff shows exactly S123, S124 and S129 added after S122.

## F1 — S129 skips the next free id

- **Defect location:** `corpus/SOURCES.md:136`.
- **Counterexample:** the previous high-water row is S122 at `corpus/SOURCES.md:133`. S123 at line 134 and S124 at line 135 are sequential. Immediately after S124, the next free high-water id is **S125**, but the third row is **S129**. S125, S126, S127 and S128 are all absent from the landed registry.
- **Why the existing rationale does not close this:** `corpus/lessons/round-67.md:67-72` establishes an empty collision set and concludes that no renumbering was needed. Non-collision and next-free allocation are different predicates; S129 satisfies the first and fails the second.
- **Local corroboration:** `.ufo/waves/round-67/w1/ReviewSources.md:34-37` identified the same counterexample while the rows were uncommitted. The present measurement confirms that integration landed it unchanged.

### Smallest safe correction

For the still-open round-67 integration, change the arXiv row's id **S129 → S125** and atomically re-point that source's citations by URL/anchor, not by arithmetic over other ids:

- `corpus/SOURCES.md:136`;
- `corpus/knowledge/instruction-authority-ladder-round67.md:3`;
- `corpus/lessons/round-67.md:37,61,116`;
- `corpus/README.md:125-126` (the source shorthand becomes `S123-S125`, and the explicit list becomes `S123/S124/S125`).

Do not backfill S125-S128 with dummy sources, rewrite the read-only assimilation package, or alter historical wave logs. Re-run the row/citation checks and the append-only check over pinned base `2a8eba56b3f9321b70c569fa2816d42237ca49a2` to the corrected tip. If the L1 treats commit `da86c03e482a6aef433c34d733726b37c7cf6607` as already closed rather than current-round content under review, an in-place id rewrite is not append-only-safe: use the contract's new-row `supersedes S129 —` correction route instead of silently renaming the protected cell.

## Full assigned-check matrix

The header is at `corpus/SOURCES.md:12` and its separator at line 13; both parse as 11 columns. The three immediately preceding existing rows S120-S122 at lines 131-133 were used as controls and each also parses as 11 columns with 12 delimiter pipes and zero escaped pipes.

| row | file:line | columns | literal/escaped cell `|` | id allocation | kind / tier | status | opened | recheck |
|---|---|---:|---|---|---|---|---|---|
| S123 | `corpus/SOURCES.md:134` | 11 | none / none | pass: follows S122 | `spec` / `A` — pass | `mined` — pass | `2026-10-24` — pass | `90d` — bare cadence |
| S124 | `corpus/SOURCES.md:135` | 11 | none / none | pass: follows S123 | `code` / `A` — pass | `mined` — pass | `2026-10-24` — pass | `90d` — bare cadence |
| S129 | `corpus/SOURCES.md:136` | 11 | none / none | **fail: S125 was next** | `paper` / `A` — pass | `mined` — pass | `2026-10-24` — pass | `90d` — bare cadence |

The enum checks are grounded in pre-existing registry usage, not in the new rows themselves: `spec/A` already occurs at S001 (`corpus/SOURCES.md:14`), `code/A` at S012 (line 25), and `paper/A` at S120-S122 (lines 131-133). The header's `kind`, `tier`, `status`, `opened`, and `recheck` cells align with the values reported above.

The read-only parser audit split each selected row on `|` and inspected cells `[1:-1]`, separately counting `\|`. Its relevant observed output was:

```text
header_columns 11
separator_columns 11
S123 line=134 columns=11 raw_pipes=12 escaped_pipes=0
S124 line=135 columns=11 raw_pipes=12 escaped_pipes=0
S129 line=136 columns=11 raw_pipes=12 escaped_pipes=0
S125 ABSENT
S126 ABSENT
S127 ABSENT
S128 ABSENT
S129 present
```

Thus there is no second schema finding hidden by the id defect: all three rows have exactly 11 cells, no extra literal cell pipe, no escaped pipe, the required mined status and opening date, and bare `90d` cadences. No tools were installed or upgraded.

Report: .ufo/waves/round-67/w2/CritSourcesSchema.md
