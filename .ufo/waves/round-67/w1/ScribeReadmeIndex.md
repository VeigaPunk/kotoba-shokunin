# ScribeReadmeIndex — round 67, wave 1

## Behavior

- Drafted the two requested three-column markdown rows for the `corpus/README.md` coverage map.
- Row 1 indexes `lessons/round-66-verifier-spotcheck.md`, names the hyaku closure rather than the lane as author, and identifies round 66 as the reviewed round.
- Row 2 indexes `knowledge/instruction-authority-ladder-round67.md` and follows the neighbouring knowledge-entry shape: area, repository-relative file, and basis with its checker.
- Supplied one placement line per row. Both belong under `## Coverage map`; Row 1 follows the existing `Round-66 lessons` row, and Row 2 follows Row 1 at the end of the current coverage rows.
- Did not edit `corpus/README.md`; integration remains with the L1.

## Gates and checks

Assigned C1/C2 predicates were **not run**: this seat's scope was the two index-row drafts, not gate measurement or claim judgment. No base/tip verification or `--rev` measurement is claimed.

Local read-only draft-structure check, run from `/home/vgpnk/Projects/shokunin/kotoba-shokunin`:

```bash
python3 -B - <<'PY'
from pathlib import Path
p = Path('/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-67/w1/drafts/README-index-rows.r67.md')
lines = p.read_text(encoding='utf-8').splitlines()
rows = [line for line in lines if line.startswith('| ')]
assert len(rows) == 2, len(rows)
cells = [[cell.strip() for cell in row.split('|')[1:-1]] for row in rows]
assert all(len(row) == 3 for row in cells), cells
assert cells[0][1] == '`lessons/round-66-verifier-spotcheck.md`'
assert cells[1][1] == '`knowledge/instruction-authority-ladder-round67.md`'
assert sum(line.startswith(('Row 1 placement:', 'Row 2 placement:')) for line in lines) == 2
print('PASS: 2 exact table rows; 3 columns each; required file cells; 2 placement lines')
PY
```

Outcome: exit 0; stdout exactly:

```text
PASS: 2 exact table rows; 3 columns each; required file cells; 2 placement lines
```

No other shell commands were run. No tools were installed or upgraded.

## Findings and provenance

- Read `corpus/README.md`: the round-60 and round-61 closure rows are at lines 104 and 108 in the inspected file and use three columns with closure-authorship notes. The existing `Round-66 lessons` row is line 123 and is the last coverage row before `## Frontier`.
- Read `corpus/lessons/round-66-verifier-spotcheck.md`: its frontmatter names `hyaku closure (non-author integrator, @m_swe)` and round 66; its closure disposition says round 66 is admitted; its routed notes are N1–N3. These observations support Row 1's note without re-judging the closure.
- Read `plans/round-67.md`: lines 41–45 require the r66 closure index row; lines 70–90 define the instruction-authority entry and its coverage-index requirement. Row 2 uses the plan's target-surface wording.
- Read the read-only assimilation source `/home/vgpnk/Projects/shokuknow/merge/kotoba/knowledge/corpus/knowledge/instruction-authority-ladder.md` for theme provenance. Nothing in that tree was changed or executed.
- A read of `verifiers/check_instruction_authority.py` returned `does not exist` in the inspected tree. No integrated knowledge entry or measured tip was inspected; Row 2 is an integration draft, not evidence that C2 passes. The L1 should reconcile its basis wording with the final landed entry if that entry differs from the frozen target surface.
- The assignment's pinned base is `2a8eba56b3f9321b70c569fa2816d42237ca49a2`; this seat did not measure that revision or any other revision.

## Touched surfaces

Created only these assigned artifacts:

- `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-67/w1/drafts/README-index-rows.r67.md`
- `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-67/w1/ScribeReadmeIndex.md`

No product file, corpus file, source registry, verifier, lane state, or sibling-seat artifact was modified.

## Out of scope / known limits

- No `corpus/README.md` integration, baseline re-record, source append, or knowledge-entry authoring.
- No C1/C2 verdict, source-truth judgment, closure judgment, commit, push, deployment, or subagent dispatch.
- The structural check validates only draft row count, column count, required file cells, and placement-line count; it does not execute either frozen claim predicate.

## Artifacts

- Draft: `.ufo/waves/round-67/w1/drafts/README-index-rows.r67.md`
- Report: `.ufo/waves/round-67/w1/ScribeReadmeIndex.md`

Report: .ufo/waves/round-67/w1/ScribeReadmeIndex.md
