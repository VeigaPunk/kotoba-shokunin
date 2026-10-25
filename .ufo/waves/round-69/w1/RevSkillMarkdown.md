# RevSkillMarkdown — round 69, wave 1 review: SKILL.md registry rows + corpus/README.md coverage rows

Scope: the round-69 working-tree diff of `SKILL.md` (three Gate registry rows) and
`corpus/README.md` (two coverage-map rows), against PROTOCOL.md § Gate standard and the
coverage-map contract. Lane base `a5f7459f99bb27bf697e9438362e75ac5833eca8`, lane HEAD
`a238989a96cb0d2b939679126b832d75b861ca6e` (the frozen plan + three counters commit).
All code execution ran in `git clone --shared` sandbox `/tmp/r69-revskillmd-sandbox`
(landing commit `0c431cf7e505469611e978f1c81289d54fa89cbe`), never in the lane; the lane's
git index, jj state and fleet repo were not touched. No installs, no package changes.

## Verdict

**Both diffs are contract-compliant as written.** Three registry rows sit in the § Gate registry
table, every entry command is accepted by its script's own argparse, and each row carries the
eight PROTOCOL fields with a declared verdict vocabulary the script actually uses. Two
coverage-map rows sit in the § Coverage map table and resolve through the index contract. The
SKILL.md diff adds exactly three lines and changes nothing else.

One **Medium** sequencing precondition and one **Low** accuracy defect are reported below; neither
is a shape failure, and both have a one-line fix.

## 1. SKILL.md — three new Gate registry rows (lines 517, 518, 519)

Placement: `## Gate registry` starts at `SKILL.md:463`; the table header
`| Name | Kind | Entry command | Verdict map | Self-test | Pinned values | Write scope | Owner |`
is at `SKILL.md:469`; the three added rows are its last three rows (`517`, `518`, `519`),
immediately before the blank line and `## Sources` (`SKILL.md:521`). Each added row has 8 cells,
matching the header; no stray `|` inside a cell; no trailing whitespace or CR
(`git diff --check` clean, `grep -P '^\+.*(\r| $)'` empty).

Diff shape: `git diff --numstat a5f7459f… -- SKILL.md` → `3 0 SKILL.md`. One hunk. No other line,
no reflow, no deletion. `git diff a5f7459f…..HEAD -- SKILL.md` is empty, so the rows are purely
working-tree draft lines — no committed SKILL.md change exists in this round yet.

### Entry-command acceptance (the contract clause asked for)

| Row | Entry command as written | argparse flag | Observed |
|---|---|---|---|
| 517 | `python3 -B verifiers/check_skill_precedence.py --rev <rev>` | `--rev` at `verifiers/check_skill_precedence.py:374` | exact command at sandbox landing rev → `measured-rev: 0c431cf…`, `skill precedence backed 5 of 5`, exit 0. `--rev zzz` → exit 2 `environment error: unknown revision zzz`; `--revv zzz` → exit 2 `error: unrecognized arguments: --revv zzz` (acceptance is non-vacuous) |
| 518 | `python3 -B verifiers/check_r68_routed_repairs.py --rev <rev>` | `--rev` at `verifiers/check_r68_routed_repairs.py:456` | accepted; at the partial landing rev prints `measured-rev: …` then the per-defect findings, exit 1 (D7/D8 still open, as expected pre-closure); `--rev zzz` exit 2 environment, `--revv` exit 2 argparse |
| 519 | `python3 -B verifiers/check_province_core.py --rev <rev>` | `--rev` at `verifiers/check_province_core.py:158` | exact command at landing rev → `province core rows 2 of 2`, exit 0; same two negative controls exit 2 |

Every command's `<rev>` is a plain `--rev` value with `default=None`, so no other argument is
required to satisfy the row; the `--repo`/`--fetch`/`--self-test` flags all have defaults.

### Field-level compliance (PROTOCOL.md § Gate standard, fleet root `PROTOCOL.md:380-418`)

Run of the lane's own registry counter at the sandbox landing rev:

```
gate registry rows conformant 49 of 49 lane verifiers; phantom 0     (exit 0)
```

and its non-vacuity control at the pre-row rev `a238989a96cb…`:

```
gate registry rows conformant 46 of 49 lane verifiers; phantom 0     (exit 1)
```

So the 49-of-49 result is produced by the three added rows, not by a lenient parse. Per row that
counter proves: one row per verifier name, `gate` kind, entry-command cell names the script,
verdict map declares `0=clean` and `1=failed` (here plus `2=could-not-evaluate`, the only other
code the three scripts return — checked in each docstring and `main()`), the self-test cell
`--self-test` is an exact active `add_argument` handler in the script, pinned values `in-file`,
non-empty write scope, owner `kotoba`.

Self-test capability (column's claim, run by me in the sandbox): C1
`0 failure(s) over 18 assertions`; C3 `0 failure(s) over 10 assertions`; C2
`0 failure(s) over 23 assertions`.

### Row text versus the scripts (consistency)

- 517: the five-id / `mined` / `opened 2026-10-25` / source-cell / located-quote conjuncts are
  `check_skill_precedence.py:24-45` (docstring) and its code — the ≤25-word cap is real
  (`:156`, `0 < len(q.split()) <= 25`), `ENTRY`/`VERIFIED_AT`/`OPENED` at `:61,64,65`, headline at
  `:397`. Verdicts in the row were reproduced: `5 of 5` at the landing rev, `0 of 5` exit 1 at the
  pinned base, and `--fetch` → `live quotes found 5 of 5`, exit 0 (S203-S207 each `found`).
- 518: all eight named repairs map to implemented conjuncts — D1 receipts, D2 self-test, D3
  (`d3_r67_counter`, `check_r68_routed_repairs.py:252ff`; the "missing records is content" half is
  real at `check_r67_routed_repairs.py:85,125-135`, and the no-git-write half greps
  `["']checkout["']`), D4 shaping notes, D5 `supersedes S201 —` + approval sentence in anchor
  (`:252-264`), D6, D7 with 24 paths from `.ufo/waves/round-68/w1/…` (the base run lists
  10 modified-blob + 14 untracked = 24, matching the row's "24"), D8 index row + baseline.
- 519: bullet-names-entry/counter/round, entry indexed (`:78,107-108`), Frontier/Adjacent
  byte-identical to base — all implemented; `2 of 2` at the landing rev, `0 of 2` exit 1 at base.

## 2. corpus/README.md — two new coverage-map rows (lines 130, 131)

Placement: `## Coverage map` at `corpus/README.md:5`, header `| Area | File | Basis |` at `:7`,
rows inside the table and before `## Frontier` (`:133`). Each row has 3 cells, no stray `|`, diff
is `2 0` (two additions, nothing else changed).

| Row | File cell | Resolution | Tracked? |
|---|---|---|---|
| 130 | `knowledge/skill-name-precedence-round69.md` | `corpus/knowledge/skill-name-precedence-round69.md` exists on disk (4781 B) | **No** — `git status` `??`, `git ls-files` empty at review time (see F1) |
| 131 | `lessons/round-68-verifier-spotcheck.md` | `corpus/lessons/round-68-verifier-spotcheck.md` exists (17302 B) | **Yes** — `git ls-files` lists it |

At the sandbox landing rev (both files committed) both cells resolve and are counted by the
lane's own index gate:

```
corpus.index  tracked=127 unindexed=1 stale=0 missing=0   (unindexed: corpus/lessons/round-69.md only)
```

i.e. the two new rows' files are indexed and present, and the only unindexed file is the
round-69 lesson, which this wave does not index. The reverse control — commit the README rows but
not the entry — is caught:

```
missing_paths: corpus/README.md:130: knowledge/skill-name-precedence-round69.md -> knowledge/skill-name-precedence-round69.md
corpus.index  tracked=126 unindexed=1 stale=1 missing=1
```

Content of the rows is consistent with what they cite: row 130's five ids are `S203`-`S207` in
`corpus/SOURCES.md:144-148` and the entry's `source:` lines name exactly those five with the
stated quotes (entry lines 1-5; `verified-at: 2026-10-25`, line 6); row 131's "the S201 refusal
disagreement" and "R68-1 … R68-8" exist in
`corpus/lessons/round-68-verifier-spotcheck.md:122-201`. Row 130's cited command
`--rev <rev> --fetch` was executed verbatim: exit 0, `live quotes found 5 of 5`.

## Findings

### F1 (Medium, sequencing precondition — must be honoured at closure)

`corpus/README.md:130` (and `SKILL.md:517`, which asserts "the entry has a coverage-map index
row") name `corpus/knowledge/skill-name-precedence-round69.md`, which is **untracked** in the
reviewed tree. An index row resolves only against committed bytes: the lane's integrity gate
reads the tracked set, and the dangling variant is demonstrably caught
(`missing_paths: corpus/README.md:130`, `stale_patterns 1`) while `check_skill_precedence.py`
then reports `skill precedence backed 0 of 5`, exit 1 (content verdict).
Fix: land `corpus/knowledge/skill-name-precedence-round69.md` in the same commit as
`SKILL.md:517` + `corpus/README.md:130`; never commit the index row alone. No text change needed.

### F2 (Low, write-scope accuracy — `SKILL.md:517`)

The write-scope cell reads `none; --fetch reads the network`. The counter does write outside the
lane: `--rev` materialises the measured revision into
`tempfile.TemporaryDirectory(prefix="k69-prec-rev-")` (`check_skill_precedence.py:385`), and
`--self-test` builds worlds under `mkdtemp(prefix="k69-prec-world-")` (`:279`). That is the exact
entry command in this row, so "none" is understated. Precedent in the same table discloses it for
siblings: `SKILL.md:477` (`check_r67_routed_repairs`: "temp checkout of `corpus/` and `verifiers/`
under `$TMPDIR`") and the new `SKILL.md:518` ("temporary sandbox clones under `$TMPDIR`").
`SKILL.md:476` carries the same imprecise wording, so this is an inherited convention rather than
new invention, and `check_gate_registry.py` (non-empty cell) passes either way. Suggested cell:
`none to the lane; temp revision export and self-test worlds under $TMPDIR (removed); --fetch reads the network`.

### F3 (Info, no rule broken)

The three rows are appended after the `verify_*.py` block (`SKILL.md:517-519`) although every
other `check_*.py` row sits higher in the table and the r68 row was inserted alphabetically
(`SKILL.md:476`). Neither PROTOCOL.md § Gate standard nor `SKILL.md` § Gate registry imposes an
order, and the table is not sorted today, so this is cosmetic; `check_gate_registry.py` is
order-agnostic (49 of 49 above).

## Measurements (all reproducible in the sandbox)

Sandbox: `git clone --shared` of the lane at `/tmp/r69-revskillmd-sandbox`; landing commit
`0c431cf7e505469611e978f1c81289d54fa89cbe` = lane HEAD plus the five drafted lines and the two
untracked corpus files.

| Run | Result |
|---|---|
| `check_gate_registry.py --rev 0c431cf…` | `49 of 49 …; phantom 0`, exit 0 |
| `check_gate_registry.py --rev a238989…` (pre-row control) | `46 of 49 …; phantom 0`, exit 1 |
| `check_skill_precedence.py --rev 0c431cf…` | `skill precedence backed 5 of 5`, exit 0 |
| `check_skill_precedence.py --rev a5f7459f…` | `skill precedence backed 0 of 5`, exit 1 (+ same finding line as `controls/C1-base.txt`) |
| `check_skill_precedence.py --rev 0c431cf… --fetch` | `live quotes found 5 of 5` (S203-S207 all `found`), exit 0 |
| `check_province_core.py --rev 0c431cf…` | `province core rows 2 of 2`, exit 0 |
| `check_province_core.py --rev a5f7459f…` | `province core rows 0 of 2`, exit 1 (+ same two finding lines as `controls/C3-base.txt`) |
| `check_r68_routed_repairs.py --rev a5f7459f…` | `r68 routed defects closed 0 of 8`, exit 1 (+ same `controls/C2-base.txt` class) |
| self-tests (C1/C3/C2) | 18 / 10 / 23 assertions, `0 failure(s)` each |
| `verify_corpus_integrity.py @landing` | `tracked=127 unindexed=1 stale=0 missing=0`; DRIFT on `tracked_files 127≠124`, `report_total 87≠85`, `commit_total 39≠38`, exit 1 |
| `verify_corpus_integrity.py @dangling control` | `missing=1 stale=1`, `missing_paths: corpus/README.md:130`, exit 1 |

## Residual risk and verification gaps

- F1 is a state, not a text defect: I could not observe the entry tracked because the L1 has not
  committed it. Verification of the landed state must be a `git cat-file -e <rev>:corpus/knowledge/skill-name-precedence-round69.md`
  plus `verify_corpus_integrity.py` `missing=0` at the closure rev.
- The `--fetch` arm proves the five located quotes are on today's live pages; it cannot prove the
  *opening* happened on `2026-10-25` — that date rests on the entry's `verified-at:` line and
  SOURCES rows' `opened` cells. Pages are mutable; a later drift is a re-measurement, not a
  contradiction of this row.
- Row 131's claims about the r68 closure are presence-level: I confirmed the lesson carries
  R68-1…R68-8 and the S201 refusal disagreement, not that the closure's re-derivations are
  correct (outside this seat's scope).
- `verify_corpus_integrity.py` is red at any rev carrying only these two map rows, on baseline
  drift and the unindexed round-69 lesson. That is C2/D8's baseline re-record and the round's
  later lesson row, not a defect in either reviewed line; recorded here so the closure does not
  read the redness as coverage-map damage.
- 518's `8 of 8` is unreachable in the wave-1 tree (D7/D8 open by design); I verified the row
  describes the counter, not that the counter is currently green.
