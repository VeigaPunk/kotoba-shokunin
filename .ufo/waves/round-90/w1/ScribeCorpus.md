# Round 90 — ScribeCorpus (scribe seat): corpus material for C1 and C2

Seat: ScribeCorpus (scribe, leaf). Wrote the round-90 corpus material only: the two SOURCES rows, the two
knowledge entries, the Q82 criterion and the lesson scaffold. No production instrument, plan, control, gate
registry or frozen instrument was touched. No git or jj write was run anywhere in the lane or the fleet
(read-only git only: `rev-parse`, `show`, `diff`, `status`, `ls-files`, `cat-file`, `log`).

Write scope honoured — exactly five corpus paths, plus this seat's wave directory:

- `corpus/SOURCES.md` — S260 and S261 appended (2 insertions, 0 deletions; `git diff --stat` = `2 ++`).
- `corpus/knowledge/mutation-battery-round90.md` — new.
- `corpus/knowledge/host-census-round90.md` — new.
- `corpus/QUALITY.md` — Q82 appended (1 insertion, 0 deletions; `git diff --stat` = `1 +`).
- `corpus/lessons/round-90.md` — new (scaffold).
- `.ufo/waves/round-90/w1/ScribeCorpus/` — receipts copied here (below) and this report.

## Handoffs consumed

| handoff | content | read at |
|---|---|---|
| `w1/SOURCE_READY` | `https://stryker-mutator.io/docs/mutation-testing-elements/mutant-states-and-metrics/` | `.ufo/waves/round-90/w1/ScoutMutSource/s260-notes.md`, `s260-quote-receipts.txt`, `receipts-rejected-routes.txt` |
| `w1/BATTERY_READY` | `0828fd9b6277c98826521109b7abac5930dea9c9e5bb26314d84b54218477e3b` | `.ufo/waves/round-90/w1/ExecBattery/battery-selftest.txt`, `battery-run.txt`, `battery-record.json` |
| `w1/CENSUS_READY` | `host skill surfaces measured 83: identical 0, drifted 0, lane-absent 83` | `.ufo/waves/round-90/receipts/c2-host-census.txt`, `c2-name-collisions.txt` |

`w1/ROOTS_READY` (content `83`) and `w1/INDEX_READY` (content `corpus.index.unindexed 0`) were also present and
were read as corroboration (ScoutHostRoots' `roots-data.md`; `receipts/index-integrity.txt`).

## What was written

**SOURCES rows.** S260 (tier A, kind `docs`) carries the Stryker Mutator documentation that grounds the
mutant / killed / survived vocabulary, the mutation-score formula `detected / valid * 100` and the
equivalent-mutant notion; five located quotes with HTML line anchors and byte sizes are recorded in the row
and in the lesson's § Gate. S261 (tier A, kind `own-work`) carries the round-89 mutant matrix at the round
base — 14 rows over the two round-89 gate instruments, 13 killed and 1 recorded SURVIVED — as the measured
prior round's evidence for the manifest's three classes. Both rows are `queued` with `used-by` naming
`corpus/knowledge/mutation-battery-round90.md`. Append-only: `git diff corpus/SOURCES.md` shows 2 insertions
and **no** deleted line (the S259 row is byte-identical to `HEAD`).

**Knowledge entries.** `mutation-battery-round90.md` opens with the Q12 provenance trio (source citing S260
+ S261 with anchors; `verified-at` naming the BATTERY_READY sha256 and the lane rev; `recheck` naming the two
runnable commands), then states what the battery does (the three manifest classes, the probe set, the
baseline-flip kill rule, the Q47 two-sided measure, guards G1–G3), what it does **not** prove (no oracle for
equivalent correctness beyond the three generated rewrite kinds; the Q79 path-dependent D5 baseline), a
§ Limits block naming the five reviewer-judged parts (per-row class assignment, the survivor disposition
text, the choice of rewrite kinds, the probe set's completeness, the observation filter), and an
§ Open item recording the survivor-class defect as routed. `host-census-round90.md` opens with the trio
(source: the round-82 capability + this round's receipts; `verified-at`: the CENSUS_READY measured line;
`recheck`: the census command and the NAME-COLLISION grep), then states the measured line, the NAME-COLLISION
ledger result, the routed read-only findings, and the bounds.

**Q82.** One row appended to `corpus/QUALITY.md`, extending Q11 and M15 without rewriting either: a
per-round wave-evidence byte budget measured at landing with `du -sb` of the round's wave tree, stated with
its date and compared against the two prior rounds, with a bundle over the budget naming the oversized
artifact and the claim it serves. Grounded in this lesson's § Mistakes and § Considerthese and in
`considerthese/2026-10-26.md` proposal 5 (2026-10-26). Append-only: `git diff corpus/QUALITY.md` shows 1
insertion and **no** deleted line (Q81 is byte-identical to `HEAD`).

**Lesson scaffold.** `corpus/lessons/round-90.md` opens with the author line (ScribeCorpus seat; the L1
completes the settlement), then § Gate (S260 admitted with five located quotes; three rejected routes with
reason + flip — mutmut as sole support, the mutmut glossary as absent, the ACM DL DOI at HTTP 403, Wikipedia
at tier C — plus S261 admitted; the census before → after with commands and exit codes; assimilation none,
L0 `kotoba | round-88` still open), § Mistakes (the r89 floors half-bump row: class, evidence pointer,
captured-by = the registry's own BUMP-IN-STEP RULE and the guard anchor outside the edited file, fix = the
completed bump + the half-bump regression arm), a routed-findings list (the survivor-class defect, the G3
registry row, the pre-existing child-cap drift), § Considerthese (proposal 5 mined as Q82; proposals 3 and 4
carried), § Sources, § Assimilation, and a § Seat record placeholder the L1 completes.

## Evidence (commands and observed lines)

SOURCES row count, before → after (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`):
**185** (receipt `.ufo/waves/round-90/receipts/census-before-rows.txt`) → **187**. The census validator:

    $ bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba
    kotoba	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md
    rc=0

33 W04 duplicate-URL warnings, the same 33 as at the round base — no new warning, no E-code. Shape checks:
every registry row has 13 pipe-delimited fields (`awk -F'|'` NF!=13 → no output), no duplicate id, and the
kind/tier/status enums are clean (tier A + kind `community` → no row; `community` never at tier A).

Append-only proofs:

    $ git diff --stat corpus/SOURCES.md corpus/QUALITY.md
     corpus/QUALITY.md | 1 +
     corpus/SOURCES.md | 2 ++
    $ git diff corpus/SOURCES.md corpus/QUALITY.md | grep '^-' | grep -v '^---' | wc -l
    0

Corpus integrity in the lane working tree (`python3 -B verifiers/verify_corpus_integrity.py --json`):
`unindexed 0`, `report_dead 0`, `commit_nonhash 0`, `commit_unresolvable 1` (the pre-existing
`corpus/lessons/round-81.md:8` site, outside this seat's files), `commit_total 62` — unchanged by this
seat's writes, because the new files cite revisions without the counted `commit `<hex>`` token form.

Q82's fix arm (`grep -c 'du -sb .ufo/waves/round-90/' corpus/lessons/round-90.md`): **1** at the round-90
tip, **0** at the round-89 tip (`git show 0c20d8ab…:corpus/lessons/round-89.md` → no match). The two fixed
comparison figures: `du -sb .ufo/waves/round-88/ .ufo/waves/round-89/` → `609628` and `1578934` (2026-11-05).

## Findings (routed; nothing repaired here)

1. **The survivor-class row does not hold at the final bytes — the L1 must rule before any scored reading.**
   The r89 matrix (S261) records `d5-m1a-d5iii-leg-only` as SURVIVED; the round-90 battery measures that row
   as **killed** (it flips both frozen D5 probes), so the measured line reads
   `mutation battery killed 13 of 13 kill-set; equivalents survived 6 of 6; disclosed survivors 0 of 1` and the
   exit is 1. The r89 anchor `if not grew:` is absent from the revision bytes (the d5iii condition is
   `if not grew and not added:`). Reclassify to `kill` (then `killed 14 of 14 …; disclosed survivors 0 of 0`,
   which reads exit 0 once the registry row lands) or keep it a survivor with a disposition that can be
   satisfied at these bytes. Source: `.ufo/waves/round-90/w1/ExecBattery.md` finding 1 and
   `w1/ExecBattery/d5-m1a-*.txt`.
2. **The G3 registry row is the L1's landing act.** Until `SKILL.md` names `check_mutation_battery.py`, the
   frozen predicate exits 1 with `G3 registry presence FAIL: 0 SKILL.md line(s) name check_mutation_battery.py`.
   The counts line is printed either way; the exit is not.
3. **Both new SOURCES rows are `queued`, and the entries citing them are written.** The SOURCES contract makes
   `mined` mean "cited by ≥1 path in `used-by`"; the citing entries exist in this seat's writes, so the L1 may
   flip both rows to `mined` at integration (a contract-permitted in-place status change, logged old→new in
   the lesson). Left `queued` here so the status change lands in one place with the L1's settlement.
4. **The corpus index does not yet cover this seat's two new knowledge entries.** `corpus/README.md` is
   ExecIndexRow's file (one row, already landed) and no owned row covers
   `corpus/knowledge/mutation-battery-round90.md` or `corpus/knowledge/host-census-round90.md`; the lesson file
   `corpus/lessons/round-90.md` is likewise uncovered. Measured in a scratch clone with the three files added
   to the index: `unindexed 3`
   (`['corpus/knowledge/host-census-round90.md', 'corpus/knowledge/mutation-battery-round90.md',
   'corpus/lessons/round-90.md']`). In the lane working tree the count reads 0 only because the three files
   are not yet tracked. **The L1 must add three index rows to `corpus/README.md` at integration**, or the
   landing `corpus.index.unindexed` reads 3. (The r89 freeze commit added the same three rows for that round's
   corpus files, so this is the same act, not a new one.)
5. **The pre-existing child-cap drift** (ExecFloorsBump finding 1): the bare live floors-guard walk can read
   exit 2 on an idle host because `verify_harness_independent.py --self-test` now takes ~167 s against a flat
   120 s cap. Not caused by the r90 bump; routed as a host-load-dependent false red.
6. **C2's findings duty is vacuous on this host.** The plan asks that every `drifted` and `identical` finding
   be named as a read-only finding. Neither class exists here (83 lane-absent, 0 drifted, 0 identical), because
   the census matches by directory name and no installed skill directory name equals a fleet-root entry name.
   The NAME-COLLISION class is likewise empty in the live root (0 duplicate-name pairs; the receipt's own
   `grep -c 'NAME-COLLISION'` prints 1, which is the mandated count line). Recorded as an honest all-clear
   rather than a skipped duty.

## Bounds

- Nothing outside the five owned corpus paths and `.ufo/waves/round-90/w1/ScribeCorpus/` was written; the
  plan, the controls plan, every frozen instrument, `corpus-baseline.json`, `SKILL.md`, `LOG.md`,
  `SCORECARD.md` and every other lane's files were read only.
- The three corpus files are **not** committed by this seat (no git write). The L1's integration commit lands
  them, and the index rows of finding 4 must land with them.
- `corpus/lessons/round-90.md` is a scaffold by design: the Gate record, the Mistakes row and the
  Considerthese entry are written; the seat record, the claim verdicts and the settlement are the L1's.
- The C1 numbers quoted in the knowledge entry are the ExecBattery seat's measured readings at the scratch
  candidate `1c5c1cb5ed41fbe5d2216eb15500831d7b4f33a6` (lane tip + the two owned files, in a scratch clone).
  The lane tip itself has no manifest, so the battery exits 2 there — the landing commit must carry both
  `verifiers/check_mutation_battery.py` and `verifiers/fixtures/mutation-battery/manifest.tsv` before the
  predicate is measured.
- The r90 wave-evidence byte figure is deliberately **not** pinned in the corpus: the tree grows while seats
  write (three separate `du -sb` readings during this seat's run gave 764101 B, 868450 B and 1198440 B).
  Q82 requires the figure at landing, and the two fixed comparison rounds are stated instead.

## Tools

None installed or updated. No pacman transaction (host-wide pacman is paused), no kernel or sysctl change, no
`/proc` write, no network write.

## Checks for the main agent

- `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`
  → expect `kotoba ok`, exit 0, 33 W04 warnings, no E-code.
- `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → expect 187.
- `git diff corpus/SOURCES.md corpus/QUALITY.md | grep '^-' | grep -v '^---' | wc -l` → expect 0 (append-only).
- `python3 -B verifiers/verify_corpus_integrity.py --json` → expect `unindexed 0` **after** the three index rows
  for this seat's corpus files land (finding 4).
- `grep -c 'du -sb .ufo/waves/round-90/' corpus/lessons/round-90.md` → expect 1.
