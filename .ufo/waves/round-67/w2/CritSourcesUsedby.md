# CritSourcesUsedby — round 67, wave 2

## Attack result

**No `used-by` defect found.** The attacked axis is **calibration / source-registry
back-reference consistency**. S123, S124 and S129 each name exactly the two admitted
entries that cite it; none has a missing or extra admitted citer. No C1-gate or C2-depth
regression follows from this item. The smallest safe correction is **no change to the
three cells**.

The strongest apparent counterexample is the lane-wide raw grep: it returns many more
files than the cells name. That does not falsify the cells, because the governing
contract does not define `used-by` as every file containing an ID. It says
“repo-relative paths of the **knowledge entries or lessons** citing the row”
(`/home/vgpnk/Projects/shokunin/CORPUS.md:107-108`). Plans, the verifier, the coverage
map, source rows themselves, drafts, controls and seat logs are not admitted
`corpus/knowledge/` entries or `corpus/lessons/` lessons. Adding those paths would widen
`used-by` beyond the contract.

## Measurement and direct evidence

- Measured revision: `da86c03e482a6aef433c34d733726b37c7cf6607` (the landed tip, not
  base `2a8eba56b3f9321b70c569fa2816d42237ca49a2`). `git rev-parse HEAD` printed the
  same full hash.
- Frozen measurement universe: `git archive` of that revision extracted at
  `/tmp/kotoba-r67-crit-sources-usedby.lRxUtr`. A lane-wide Grep was run separately for
  each literal ID with `output_mode=files_with_matches`, `include_ignored=true`, and no
  head limit; a byte-level set reconciliation independently gave the counts below.
  A live-tree sweep was also made. It additionally saw in-flight wave-2/runtime files,
  but no additional admitted citer. The three registry rows, the knowledge entry and
  the lesson are unchanged from the frozen revision; the scoped `git diff --name-only`
  named only `corpus/README.md`, which is not a `used-by`-eligible entry.
- `corpus/knowledge/instruction-authority-ladder-round67.md:3-5` directly cites S123,
  S124 and S129 in its three `source:` fields.
- `corpus/lessons/round-67.md:20-42` directly cites all three in Gate, and
  `:114-119` records all three status/`used-by` changes.
- The landed cells are at `corpus/SOURCES.md:134-136`.

Let **K** be this complete admitted-citer set:

1. `corpus/knowledge/instruction-authority-ladder-round67.md`
2. `corpus/lessons/round-67.md`

| Row | `used-by` cell | Admitted citers found | Missing admitted citer | Extra cell member | Exact under contract? |
|---|---|---|---|---|---|
| S123 | K | K | none | none | yes |
| S124 | K | K | none | none | yes |
| S129 | K | K | none | none | yes |

If “that set” in the attack item is instead interpreted as the **raw whole-lane grep
set**, then no cell equals that much larger set: the raw matches outside the cells are
exactly `R123 \ K` (44 paths), `R124 \ K` (32 paths), and `R129 \ K` (36 paths), fully
specified below. Those are not missing contract entries. This distinction is necessary
rather than pedantic: two S123 raw hits are not citations to this row at all.
`.ufo/waves/round-66/w1/ReviewC1Witness.md:34,49,61,63,66` uses `(S123 :2)` as a
synthetic citation fixture, while
`.ufo/round-44/evidence/omp-live-18.12.2-strings.txt:561137` contains the four bytes
inside an encoded blob. A naive “every grep hit belongs in `used-by`” repair would
therefore introduce false provenance.

## Complete frozen lane-wide raw-match sets

This appendix preserves the complete sweep without confusing raw matches with admitted
citations. Paths are repo-relative. Define five disjoint groups from the executed set
reconciliation.

### A — present in all three raw sets (33 paths)

- `.ufo/waves/round-67/controls/SOURCES.append.r67.md`
- `.ufo/waves/round-67/controls/staged-ids`
- `.ufo/waves/round-67/controls/validate/corpus/SOURCES.append.r67.md`
- `.ufo/waves/round-67/controls/validate/corpus/SOURCES.md`
- `.ufo/waves/round-67/controls/validate/corpus/knowledge/instruction-authority-ladder-round67.md`
- `.ufo/waves/round-67/controls/validate/corpus/lessons/round-67.md`
- `.ufo/waves/round-67/w1-spec.json`
- `.ufo/waves/round-67/w1/RevFabrication.md`
- `.ufo/waves/round-67/w1/ReviewAppendOnly.md`
- `.ufo/waves/round-67/w1/ReviewSources.md`
- `.ufo/waves/round-67/w1/controls/staged-ids`
- `.ufo/waves/round-67/w1/controls/validate/corpus/SOURCES.md`
- `.ufo/waves/round-67/w1/controls/validate/corpus/knowledge/instruction-authority-ladder-round67.md`
- `.ufo/waves/round-67/w1/drafts/SOURCES.append.r67.md`
- `.ufo/waves/round-67/w1/drafts/check_instruction_authority.py`
- `.ufo/waves/round-67/w1/drafts/round-67-lesson.md`
- `.ufo/waves/round-67/w1/drafts/round-67-report.md`
- `.ufo/waves/round-67/w1/logs/CriticC2.log`
- `.ufo/waves/round-67/w1/logs/CriticProvenance.log`
- `.ufo/waves/round-67/w1/logs/ExecC2Counter.log`
- `.ufo/waves/round-67/w1/logs/ExecTransform.log`
- `.ufo/waves/round-67/w1/logs/RevFabrication.log`
- `.ufo/waves/round-67/w1/logs/ReviewAppendOnly.log`
- `.ufo/waves/round-67/w1/logs/ReviewEntry.log`
- `.ufo/waves/round-67/w1/logs/ReviewSources.log`
- `.ufo/waves/round-67/w1/logs/ScribeEntry.log`
- `.ufo/waves/round-67/w1/logs/ScribeLesson.log`
- `.ufo/waves/round-67/w1/logs/ScribeReadmeIndex.log`
- `.ufo/waves/round-67/w1/logs/ScribeReport.log`
- `.ufo/waves/round-67/w1/logs/ScribeSources.log`
- `corpus/SOURCES.md`
- `corpus/knowledge/instruction-authority-ladder-round67.md`
- `corpus/lessons/round-67.md`

### B — present only in the S123 and S124 raw sets (1 path)

- `.ufo/waves/round-67/w1/logs/ExecCollision.log`

### C — present only in the S123 and S129 raw sets (4 paths)

- `.ufo/waves/round-67/w1/CriticC2.md`
- `.ufo/waves/round-67/w1/logs/ReviewC1Repair.log`
- `.ufo/waves/round-67/w1/logs/ReviewCounter.log`
- `corpus/README.md`

### D — present only in the S123 raw set (8 paths)

- `.ufo/round-44/evidence/omp-live-18.12.2-strings.txt`
- `.ufo/waves/round-66/w1/ReviewC1Witness.md`
- `.ufo/waves/round-67/w1/ExecCollision.md`
- `.ufo/waves/round-67/w1/ReviewCounter.md`
- `.ufo/waves/round-67/w1/logs/ExecC2JunkControl.log`
- `.ufo/waves/round-67/w1/logs/ExecQualityBar.log`
- `plans/round-67.md`
- `verifiers/check_instruction_authority.py`

### E — present only in the S129 raw set (1 path)

- `.ufo/waves/round-67/w1/logs/ConnSibling.log`

Thus the complete raw sets and counts are:

- **R123 = A ∪ B ∪ C ∪ D — 46 files.**
- **R124 = A ∪ B — 34 files.**
- **R129 = A ∪ C ∪ E — 38 files.**

There are no S124-only or S124+S129-only paths. The contract-relevant citation set for
each row remains K, so all three cells survive the strongest local counterexample.
