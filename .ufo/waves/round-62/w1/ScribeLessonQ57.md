# ScribeLessonQ57 — round 62 report

## Behavior

Created `corpus/lessons/round-62.md` with the Gate, Mistakes, Status changes, and Falsify corrections sections; Gate includes S118, the round-start census receipt, and the r61 rejection decisions from `ScoutKeyPagesA.md`. Appended Q57 to `corpus/QUALITY.md`. The lesson records M93 against `check_scoped_rules.py:972-1040`, cites the r61 claim against the draft-only attack basis, names the C1 matrix, and preserves v31's declared G9 compound-purpose survivor.

## Gates and observed outcomes

Round-start census was not rerun; its existing receipt records:

```text
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba
exit=0
```

The C1 matrix was not rerun by this scribe. The recorded command is `python3 -B verifiers/check_erratum_absorption.py --self-test`; `.ufo/waves/round-62/controls/absorption-hollow.txt:16-27` records `errata measured 5 of 5; absorbed 2 of 5; surviving 6; controls 2 of 2` and exit 0.

Q57's table structure was checked read-only:

```text
$ python3 -B -c 'from pathlib import Path; lines=[line for line in Path("corpus/QUALITY.md").read_text().splitlines() if line.startswith("|")]; data=lines[2:]; ids=[line.split("|")[1].strip() for line in data]; assert all(len(line.split("|")) == 7 for line in lines) and len(ids) == len(set(ids)) and ids[-1] == "Q57"; print("QUALITY table parsed: five cells per row, unique ids, Q57 final")'
QUALITY table parsed: five cells per row, unique ids, Q57 final
exit=0
```

The requested corpus-integrity command was also run:

```text
$ python3 -B verifiers/verify_corpus_integrity.py
corpus.index    tracked=104 unindexed=2 stale=2 missing=0  (122 FILE-column patterns over 103 md files)
corpus.pointers report_dead=0/68 commit_total=34 unresolvable=1 nonhash=0
3/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.index.unindexed, corpus.index.stale_patterns, corpus.pointers.report_total, corpus.pointers.commit_total, corpus.pointers.commit_unresolvable
exit=1
```

This verifier reported index/pointer drift, not a QUALITY table parse error. It lists the round-62 lesson and knowledge-entry README patterns as stale; the two older verifier-spotcheck lessons are unindexed. No index or knowledge-entry edits were in scope.

## Exact appended row

```markdown
| Q57 | An erratum (or any amendment) counts as absorbed only when each fresh attack instance of its class is rejected by the landed instrument and disabling that erratum's guard in-process admits that same instance; a plan-text attack does not establish absorption, and the receipt names both verdict directions and the disabled guard. | erratum/amendment absorption claims and their receipts | M93 `erratum recorded as absorbed without an arm-level receipt` (`corpus/lessons/round-62.md` § Mistakes); C1 matrix (`.ufo/waves/round-62/controls/absorption-hollow.txt:16-27`; `python3 -B verifiers/check_erratum_absorption.py --self-test`). Clause ownership: Q34 owns SOURCES append-only claims; Q35 owns verifier inventory and `SKILL.md` gate-registry/self-test declarations; Q36 owns receipt revision identity; Q56 owns quote/source equality; Q57 owns absorption evidence. Bound: arm-level, not world-level. | — |
```

## Findings and limits

- The hollow control receipt records the variant exiting 1, but the diagnostic is a missing `/tmp/r62hollow/check_scoped_rules.py` path. The lesson discloses that this receipt alone does not show failure for the intended guard-direction reason; `ExecAbsorbInstrument.md:70-72` separately reports rejection of the semantic hollow shortcut for missing run records.
- `corpus/knowledge/erratum-absorption-round62.md` was absent when read and was not created by this assignment. The S118 `used-by` cell already names it. No post-round census was run.
- The v31 source was present when inspected and declares G9 as surviving in its self-test code; no v31 self-test was run by this scribe.
- No tools were installed. No product code, source registry, index, knowledge entry, git/jj state, build, lint, or other test was changed or run.

## Touched surfaces and artifacts

- `corpus/lessons/round-62.md` — created.
- `corpus/QUALITY.md` — Q57 appended.
- `.ufo/waves/round-62/w1/ScribeLessonQ57.md` — this report.
- Read-only evidence: `.ufo/waves/round-62/census-before.txt`, `.ufo/waves/round-62/controls/absorption-hollow.txt`, `.ufo/waves/round-62/w1/SrcRulesFrontmatter.md`, `.ufo/waves/round-62/w1/ExecAbsorbInstrument.md`, `.ufo/waves/round-61/wave/ScoutKeyPagesA.md`, and `plans/round-62.md`.
