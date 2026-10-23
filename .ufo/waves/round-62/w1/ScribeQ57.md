# ScribeQ57 — Q57 draft and scope report

## Behavior / proposed row

The proposed row preserves the current five-column table shape (`id`, `criterion`, `applies to`, `grounded in`, `supersedes`). It defines absorption from paired, same-instance arm-level observations; a plan-text-only attack is not evidence. The bound is arm-level, not world-level.

```markdown
| Q57 | An erratum (or any amendment) is recorded as absorbed only when each fresh attack instance used to establish its class is rejected by the landed instrument and disabling the guard assigned to that erratum in-process admits that same instance. A plan-text attack does not establish absorption. The receipt names both directions and the disabled guard. | erratum/amendment absorption claims and their receipts | M93 `erratum recorded as absorbed without an arm-level receipt` (`corpus/lessons/round-62.md` § Mistakes); round-62 C1 absorption matrix (`plans/round-62.md` § C1; `verifiers/check_erratum_absorption.py --self-test`). Bound: arm-level, not world-level. | — |
```

The M93 and matrix citations are draft pointers from the frozen round-62 plan. At inspection, `corpus/lessons/round-62.md` and a published C1 matrix receipt were not present in the lane listing; this report does not claim either was independently verified or executed by this scribe. The plan specifies the matrix and its command in `plans/round-62.md` § C1.

## Overlap and clause ownership

| Row | Owns | Relationship to Q57 |
|---|---|---|
| Q56 | Whether quote/source equality is byte-exact or quote-equal after documented shaping. | No overlap: it governs quote-byte descriptions, not absorption evidence. |
| Q34 | Append-only compliance claims for `corpus/SOURCES.md`, checked by its named verifier. | No overlap: it does not define QUALITY-row append behavior or an absorption verdict. |
| Q35 | Verifier inventory and `SKILL.md` gate-registry/self-test declarations. | Adjacent surface only: Q35 owns registration and gate-kind correctness for a verifier; Q57 owns what evidence supports an absorption claim. A verifier can be subject to both without either row replacing the other. |
| Q57 | Absorption verdict evidence: landed-instrument rejection and same-instance admission with the named guard disabled in-process; plan-text attacks excluded; arm-level bound. | New clause; supersedes none. |

## Gate / scratch-copy check

Structural five-column parse check on a scratch copy of the current `corpus/QUALITY.md`, with the proposed Q57 row appended in memory. The copy itself was not changed; the check verified all pipe-table rows have five cells, IDs are unique, and Q57 is the last parsed data row.

Command:

```sh
date -u +%Y-%m-%dT%H:%M:%SZ
mkdir -p /fast/scratch/hyaku/kotoba-r62/ScribeQ57 && cp /home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/QUALITY.md /fast/scratch/hyaku/kotoba-r62/ScribeQ57/QUALITY.md && python3 -B -c 'from pathlib import Path; p=Path("/fast/scratch/hyaku/kotoba-r62/ScribeQ57/QUALITY.md"); text=p.read_text(); row="| Q57 | An erratum (or any amendment) is recorded as absorbed only when each fresh attack instance used to establish its class is rejected by the landed instrument and disabling the guard assigned to that erratum in-process admits that same instance. A plan-text attack does not establish absorption. The receipt names both directions and the disabled guard. | erratum/amendment absorption claims and their receipts | M93 `erratum recorded as absorbed without an arm-level receipt` (`corpus/lessons/round-62.md` § Mistakes); round-62 C1 absorption matrix (`plans/round-62.md` § C1; `verifiers/check_erratum_absorption.py --self-test`). Bound: arm-level, not world-level. | — |"; lines=[line for line in (text+"\n"+row).splitlines() if line.startswith("|")]; assert len(lines) >= 3; assert all(len(line.strip().strip("|").split("|")) == 5 for line in lines); ids=[line.split("|")[1].strip() for line in lines[2:]]; assert len(ids) == len(set(ids)); assert ids[-1] == "Q57"; print("table rows=%d; columns=5; Q57 parsed" % (len(lines)-2))'
rc=$?
printf 'exit=%s\n' "$rc"
exit "$rc"
```

Output:

```text
2026-10-23T20:51:17Z
table rows=57; columns=5; Q57 parsed
exit=0
```

No absorption-matrix self-test or data run was run for this scribe assignment. The structural check is not evidence that the matrix ran or that C1 passed.

## Touched surfaces, limits, out of scope

- Read: `plans/round-62.md` § C1; `corpus/QUALITY.md` Q34/Q35/Q56 and table header; round-62 wave files as listed at inspection.
- Scratch artifact: `/fast/scratch/hyaku/kotoba-r62/ScribeQ57/QUALITY.md` (byte copy of the source used by the parse check).
- Report artifact: `.ufo/waves/round-62/w1/ScribeQ57.md`.
- `corpus/QUALITY.md` was not edited. No verifier, lesson, matrix, or product code was edited. No git/jj mutation, dispatch, or ask was performed. No installs.
- No world-level semantics, cross-arm isolation, landed matrix result, or M93 lesson content was independently verified here; the criterion expressly claims only the arm-level bound.

Installs: no installs.
Blockers: none.
Produced: Q57 draft row, Q56/Q34/Q35 clause ownership check, and scratch-copy table-parse evidence.
