# CriticMistakeClass — round 73, wave 1 (critic, leaf)

**Scope:** the plan's `## Frontier step` mined mistake and its fix (`verifiers/check_report_pointers.py`).
Read-only. No lane file touched; no tool installed; no scratch directory created (the prototype below ran
in a REPL and wrote nothing).

**Verdict.**

1. The factual core of the mined mistake **reproduces**: the r72 report cites two receipt paths that exist
   at no revision (F1). D2's claim holds.
2. `captured-by: none` is **false**, twice: three `QUALITY.md` criteria that should have caught it existed at
   the r72 tip (Q36, Q50, **Q60**, the last minted in round 64 for this exact defect), and the lane already
   owns a report-scanning instrument (`check_report_hashes.sh`, Q41) plus a one-off arm that is *literally*
   "a report cites a receipt path that does not exist" (`check_r67_routed_repairs.py` D2). The r72 defect is a
   **third recurrence after capture**, not an uncaptured class (F2). Under the fleet's own definition of the
   field (`CORPUS.md:172`) the row as planned would itself be a false statement about a criterion.
3. The proposed fix is aimed at the pointer half but is **not yet a measurement** of it: under the plan's own
   token rule the red-before demo emits 6 findings of which 1 is true (F3), the frozen interface cannot locate
   its subject (F4), and it would be the lane's fourth pointer resolver (F5).
4. The SOURCES.md D3 splice is a **second defect on a different class**, invisible to any report-only gate and
   not caught by the append-only gate (proved exit 0), so the mistake needs **two rows** (F7). The planned
   repair (plan bullet 3, append a correction entry) lands in the same section and would be unguarded.

## F1 — independent re-derivation of the unresolved tokens

Report `/home/vgpnk/Projects/shokunin/.ufo/reports/round-72/kotoba.md`, lane tree at
`072048fa8e8a52c707d25f7079772fa317244eb7` and at the r72 tip `e8207c64bda07b23964eabface7a917b2200bc8d`
(committed lane files identical at both: `git diff --name-only 072048f HEAD` lists only `plans/` and
`.ufo/waves/round-73/`).

```
$ sed -n '70p;103p' .ufo/reports/round-72/kotoba.md
  (`tip-check_tip_battery.txt`, `tip-tip_battery-run2.txt`): the counter's sandbox reads `check_assertion_floors.py` and
  (`receipts/tip-check_substrate_repin_v2.txt`).
```

```
$ git cat-file -e 008411c:<path>   and   e8207c6:<path>
128 .ufo/waves/round-72/receipts/tip-check_tip_battery.txt        @008411c
128 .ufo/waves/round-72/receipts/tip-check_tip_battery.txt        @e8207c6
128 .ufo/waves/round-72/receipts/tip-check_substrate_repin_v2.txt @008411c
128 .ufo/waves/round-72/receipts/tip-check_substrate_repin_v2.txt @e8207c6
0   .ufo/waves/round-72/receipts/base-outputs                    @both
```

So: two dead pointers, exactly as closure D2
(`corpus/lessons/round-72-verifier-spotcheck.md:31-34`) says. Two corrections to the plan's sentence:

- The plan writes "the r72 report **and SHONEN** cited receipt files that do not exist". The lane's
  `SHONEN.md` at the base cites no receipt: `git show 072048f:SHONEN.md | grep -n 'receipt\|tip\|\.ufo'`
  returns only `.ufo/round-46/...` and `PROVINCE.md` evidence lines (exit 0, no receipt token). The citation
  is in the report's `## SHONEN` **section** (`:103`). `SHONEN` unqualified points a reader at a file that
  never cited it — the mined-mistake row would repeat the class it records.
- The bare token `tip-check_tip_battery.txt` (`:70`) has no `receipts/` prefix. This matters for F3.

## F2 — `captured-by: none` is false

The fleet defines the field as the rule, not the instrument (`CORPUS.md:172`):

> captured-by (the `QUALITY.md` criterion or protocol rule that should have caught it, or `none`)

Three criteria existed at the r72 tip **and** at the base — `git show <rev>:corpus/QUALITY.md` returns 3
matching rows at both revisions — and each binds this citation form:

| line | id | why it binds the r72 line |
|---|---|---|
| `corpus/QUALITY.md:75` | Q60 | "The check is `git cat-file -e <rev>:<path>`, which exits 128 (nonzero) for a path the revision does not carry" — the F1 command is that check. |
| `corpus/QUALITY.md:61` | Q50 | "Every gate result a report states for the lane tip has a committed receipt that names that exact tip revision" — `:70` states `4 of 6` @ `008411c` "twice (`tip-check_tip_battery.txt`, …)". |
| `corpus/QUALITY.md:47` | Q36 | "A no-harm or tip receipt cited in a report names the revision it measured in the receipt itself" — `:103` cites a tip receipt. |

Q60 is the criterion minted *for this class in this lane*, and the lesson says so in as many words
(`corpus/lessons/round-64.md:57-62`, M96 = "M95-class recurrence, in the report itself"): the quote is
"Captured-by: none at r63 — now **Q60**." So r72's `tip-check_*` is the **third** occurrence
(M96 r64 → r67 R67-2 → r72), the second one after Q60 existed. Recurrence-after-capture is the fleet's
costliest ledger fact (`mistakes.md` §3.5, §4; C01 ranks on it). A row that says `none` deletes that fact.

Instruments that already exist (so the plan's "no criterion caught it" is also wrong about coverage, not
only about capture):

- `verifiers/check_r67_routed_repairs.py:19-21` — the gate's own contract line: "R67-2 the r67 report cites a
  census receipt path that does not exist". D2 (same file, `REAL_RECEIPT`/`WRONG_RECEIPT`, `:61-62`, check at
  `:160-163`) is the first arm for exactly this defect, three rounds ago.
- `.ufo/waves/round-57/build/check_report_hashes.sh` (Q41) already takes `<lane> <report>` and exits 1 on a
  report. Run on the r72 report it is **green**, i.e. it scans hashes only:

```
$ .ufo/waves/round-57/build/check_report_hashes.sh <lane> <r72 report> ; echo exit=$?
exit=0
```

- `verifiers/verify_corpus_integrity.py` — the plan's parenthetical is accurate for this gate but narrower
  than stated: `report_pointer_exists` (`:273-277`) resolves `.ufo/reports/…` pointers **found inside corpus
  files**, and the scope line says so (`:43`, "POINTERS reads every tracked \*.md under corpus/"; tracked set
  `:615-617`). It never opens the fleet report as an input.

Correct label: **class `reference-drift`, captured-by Q60 (criterion), no general arm** — predecessor arms
`check_r67_routed_repairs.py` D2 (r68) and `check_report_hashes.sh` (r57). That framing also supplies the
kill criterion the plan currently lacks: the new gate must fail on a world where the r67 D2 presence check
would still pass.

## F3 — the red-before demo cannot name what the plan promises

A scratch implementation of the plan's literal sentence ("resolves every backticked `.ufo/waves/…`,
`receipts/…`, `corpus/…`, `verifiers/…` token of a report against the lane tree at a revision"), run on the
r72 report at the r72 tip:

```
LITERAL IMPLEMENTATION (lane-relative)
16: receipts/base-outputs/
17: receipts/census-before.txt
60: receipts/tip-*.txt
73: receipts/tip-noharm.txt
103: receipts/tip-check_substrate_repin_v2.txt
106: receipts/tip-noharm.txt
dead count: 6
```

Five of those six are resolution-map artifacts: the lane root has no `receipts/` (`ls -d receipts` → "No such
file or directory"), while `.ufo/waves/round-72/receipts/base-outputs`, `census-before.txt` and
`tip-noharm.txt` all exit 0 under `git cat-file -e`. Adding the round map (`receipts/` →
`.ufo/waves/round-<N>/receipts/`, N from the report's own path):

```
ROUND-SCOPED CORRECTION
60: receipts/tip-*.txt
103: receipts/tip-check_substrate_repin_v2.txt
dead count: 2
```

`:60` is still false red — a glob (`has_glob` `:205`, excluded by `is_excluded_pointer` `:280-293`,
`verify_corpus_integrity.py`).

The plan's demo promises "exit 1, naming the `tip-check_*` tokens" (plural). Under **any** version of the
stated rule the counter names **one**: `:103`. The other, `:70`, is a bare basename outside all four prefixes,
so it is never tokenized. A demo whose red comes from artifacts is not a measurement, and the plan's own
kill rule ("shown able to fail by naming the `tip-check_*` tokens") cannot be satisfied as written.

The fix is cheap and it is worth freezing in the plan, because the honest version of the rule reaches the
promised result exactly. With a declared map (prefixed `receipts/` round-scoped, globs excluded) **plus** a
bare-basename arm with a fixed search order — `.ufo/waves/round-N/`, `.ufo/waves/round-N/w1/`,
`.ufo/waves/round-N/receipts/`, `verifiers/`, lane root — the r72 report yields precisely two findings:

```
FINDINGS with declared map + search order:
  (70,  'tip-check_tip_battery.txt', 'bare')
  (103, 'receipts/tip-check_substrate_repin_v2.txt', 'prefixed')
```

and the other 14 bare tokens in that report (`tip-tip_battery-run2.txt`, `c3-base.txt`, `census-*.txt`,
`verify_*.py`, `ExecOC1/2.md`, `SKILL.md`, …) all resolve under that order, so the bare arm does not need a
separate false-positive world — it needs the order written down.

## F4 — the frozen interface cannot locate its subject

The fix runs as `verifiers/check_report_pointers.py` over "a report at a revision". The r73 report is
`.ufo/reports/round-73/kotoba.md` — the **fleet** path; the lane only caches report copies for rounds 20-45
(`git ls-tree -r --name-only HEAD | grep '^\.ufo/reports/'` → 25 files, last
`.ufo/reports/round-45/kotoba.md`; zero matches for `round-7[23]`, and
`git cat-file -e 072048f:.ufo/reports/round-72/kotoba.md` exits 128). So a `--rev <rev>`-only interface has no
report to open: at the base the r72 subject is absent from the lane tree, and at freeze 2 the r73 subject is
not written yet. Scanning the lane's old copies instead would measure a stale duplicate. The do-nothing
control that C1/C2/C3 each carry is absent for this fix entirely. `check_report_hashes.sh` already solves the
addressing with `<lane> <report>`; the same two-argument shape (plus `--rev`) is the smallest fix.

## F5 — duplicate authority: this would be the fourth pointer resolver

Existing resolvers for the same token family:

1. `verifiers/verify_corpus_integrity.py:147` (`UFO_POINTER_RE`), `:273-277` (`report_pointer_exists`),
   `:280-293` (`is_excluded_pointer`).
2. `verifiers/verify_corpus_independent.py:124` (regex), `:269` (fleet fallback) — the independent twin, whose
   whole purpose is to disagree with (1) only on real defects.
3. `verifiers/check_r67_routed_repairs.py` D2 — presence of the correct receipt path in the records.

A fourth, newly written resolver will drift from (1) and (2) exactly the way `check_tip_battery.py` drifted
from its gates (M127). The counter must import or port (1)'s three functions and carry a cross-check arm
against (1)'s output on a report-shaped fixture, and it needs its registry row (the plan already requires rows
for new gates).

## F6 — class and where the defect sits

`reference-drift` is admissible for the pointer half (fleet C01 contains absent paths — M006, "README gap
example paths both absent"). It is not the lane's precise name: r64 minted M96 for this exact shape and Q60
for its check; the receipt form has M48/Q36 and M80/Q50. Keep the fleet class word, name M96/Q60 as the
predecessor, and put the recurrence in the row — that is the ledger fact that matters.

The SOURCES.md splice is **not** `reference-drift`: the bytes it damages still resolve as tokens. It is the
fleet's `landing` class (`CORPUS.md:173-176` list; C09), i.e. an append that landed in the wrong place.

## F7 — D3 needs its own row, its own arm, and it is not caught by anything today

At the r72 tip the damage is worse than the closure's summary: line 214 **starts a new `## ` heading inside
the search log** (the stray `## Leads (unopened)` string from the damaged note now leads a line):

```
$ git show e8207c6:corpus/SOURCES.md | sed -n '206,215p' | nl -ba -v206
   207   `
   209 - **2026-10-24 — placement correction (appended by the L1 in wave 2):** the two round-64 notes
   210   originally landed at EOF under `
   211 (blank)
   212 - **2026-10-25 — round-72 assimilation openings.** … (S214-S216, staged S262, S263, S264) …
   214 ## Leads (unopened)` (the placement defect `CriticW2Frontier` F3 caught at the
   215   measured tip); their content is preserved verbatim and they are relocated to the end of `## Search log` here.
```

Two negatives, both run:

```
$ python3 -B verifiers/check_sources_append_only.py --rev e8207c6 --base c69711e ; echo exit=$?
sources append-only rows clean: 1 commits scanned, 0 protected-cell changes
exit=0
```
Q34's instrument is blind by construction — `parse()` (`:46-62`, row regex `:31`) reads only `| S### |` rows;
the spliced note is prose.

A gate that resolves report tokens can never see it either: the damaged bytes live in `corpus/SOURCES.md`, and
the region contains no dead path token (`## Leads (unopened)` is a heading string; `merge/kotoba/` and the
report's other out-of-lane tokens are outside the prefix set). Running `check_report_pointers.py` on the r73
report therefore says nothing about D3 — including after the planned repair, which appends a correction entry
**into the same search log** and can splice again.

So: **two rows**. Row A `reference-drift` (F1 tokens, captured-by Q60, fix F3-F5). Row B `landing`
(`corpus/SOURCES.md:209-215` at `e8207c6`, captured-by none — Q34's instrument is blind, Q31 is about counter
descriptions), fix = a search-log placement arm: over `--base..--rev`, every line the commit adds to
`## Search log` must be a contiguous block at the section end, no pre-existing line of the section may be
split, and no `## ` heading may appear inside the section. Red-before world: the r72 range (exit 1 naming
`corpus/SOURCES.md:209-215`); green world: a clean append; and it must be run on the r73 repair commit before
the r73 report — otherwise the repair of a placement defect is not guarded against being the next one.

## Impacted axes

`consistency` (calibration) — the capture cell is a calibration statement, and a wrong one is exactly what the
axis measures; no C1/C2/C3 predicate is touched by this critique. Secondary: the fleet's C01 recurrence ledger
and the `## Mistakes` row's admissibility under `CORPUS.md:172-178`.

## Smallest safe corrections

1. Rewrite the mined-mistake row: two rows, classes `reference-drift` (pointer) and `landing` (splice);
   captured-by `Q60` (row A, predecessors M96/R67-2, arms `check_r67_routed_repairs.py` D2 and
   `check_report_hashes.sh`) and `none` (row B, with the Q34 blindness stated).
2. State the counter's resolution set and its map before freeze 2: base = lane root at `--rev`; `receipts/` →
   `.ufo/waves/round-<N>/receipts/`; globs excluded via the existing `has_glob`/`is_excluded_pointer`;
   out-of-lane tokens (`merge/…`, `~/.local/bin/…`) declared out of scope; and the report passed as an
   argument (`--report <path> --rev <rev>`), because no lane revision carries the round-73 report (lane copies
   stop at `round-45`).
3. Freeze the demo's finding set, not its exit code: with the map and search order of F3 the r72 report must
   yield exactly `70: tip-check_tip_battery.txt` and `103: receipts/tip-check_substrate_repin_v2.txt`, exit 1;
   add the r63 report's `@ 35d44b4b` paths (M96's own world) as a second red-before.
4. Reuse (1)'s resolver and add the cross-check arm; add the registry row. The fleet-root hop already exists
   in both twins for exactly this shape (`verify_corpus_integrity.py:127,273-277`;
   `verify_corpus_independent.py:45,265-266`), so the counter does not need a new path-resolution policy —
   it needs the existing one with the report as an input.
5. Add the search-log placement arm and run it on the r73 repair commit before the report.

## Not verified / limits

- I did not implement or run the planned counter (it does not exist yet); F3's numbers come from scratch
  re-implementations of the plan's literal sentence and of the map/search order I propose, and are
  reproducible only under those readings. The two-finding result is *my* proposed policy, not the plan's.
- I did not re-open the r63 report to confirm M96's `35d44b4b` world byte-for-byte; the lesson's own text is
  the evidence I read (`corpus/lessons/round-64.md:57-62`).
- Gate self-tests (`--self-test`) of `verify_corpus_integrity.py` / `verify_corpus_independent.py` were not run
  (out of scope; another seat owns the battery).
