# ScribeSources — round 85, w1 — registry CRLF repair, S213 used-by, coverage-map index rows

Seat: `ScribeSources`. Round 85 attempt 1, lane kotoba, host linux, 2026-11-04.
Scope: the four record repairs named by the seat spec — (1) normalize `corpus/SOURCES.md`
from CRLF to LF with a proof that no cell changed, (2) update S213's `used-by` cell,
(3) add coverage-map index rows to `corpus/README.md`, (4) validate the census and the
corpus index census.

**Result: all four items are done and every acceptance criterion reads green.**
The census `--file` run exits 0 with 0 E-codes; the tr-diff proof of the normalization
is empty and reproducible; S213's `used-by` old→new is recorded; 8 index rows are added;
and `corpus.index.unindexed` reads **observed 0**.

## A contract deviation this seat made, and the L1's correction

**This seat first wrote the round-85 re-opening record into S213's `anchor` cell. That
is a protected cell under SOURCES rule 2 — a breach. The L1 (`KotobaR85`) caught it and
corrected it: the anchor is restored to the exact base text, the `used-by` addition is
preserved, and the re-opening record stays in the round lesson and in the scout source
packet, which is where a rule-2 re-open belongs.**

Rule 2, verbatim from `verifiers/check_sources_append_only.py:5-6`: *"Only `status`,
`recheck` and `used-by` change in place, and each change is logged old->new in the round
lesson. A correction is a new row whose `teaches` opens `supersedes S0NN —`."*

The corrected state is verified with the gate's **own** `compare()` (base vs worktree):
**0 breaches, 1 log note** (S213 `used-by`) — receipt
`.ufo/waves/round-85/w1/ScribeSources/append-only-conformance.txt`. No new registry row
was minted (the plan declares `sources_rows_added: 0`, and a new row would be a W04
duplicate — the round-74 rejection reason).

## Files written

| path | what |
|---|---|
| `corpus/SOURCES.md` | CRLF → LF normalization (byte-level, cells unchanged) + S213 `used-by` cell update |
| `corpus/README.md` | 8 new coverage-map index rows |
| `.ufo/waves/round-85/w1/ScribeSources/crlf-proof.txt` | the tr-diff proof, byte counts, final-state diff |
| `.ufo/waves/round-85/w1/ScribeSources/s213-usedby.txt` | S213 old → new, constraint checks, the deviation record |
| `.ufo/waves/round-85/w1/ScribeSources/append-only-conformance.txt` | rule-2 conformance of the worktree, via the gate's own `compare()` |
| `.ufo/waves/round-85/w1/ScribeSources/readme-index-rows.txt` | the 8 rows, their shape check, the grounding head lines |
| `.ufo/waves/round-85/w1/ScribeSources/census-lane-file.txt` | census `--file` output, exit 0 |
| `.ufo/waves/round-85/w1/ScribeSources/census-fleet-root.txt` | census `--root … kotoba` output, exit 0 |
| `.ufo/waves/round-85/w1/ScribeSources/corpus-integrity.txt` | `verify_corpus_integrity.py --json` reading, all 9 checks |
| `.ufo/waves/round-85/w1/ScribeSources/corpus-independent.txt` | `verify_corpus_independent.py --json` cross-check |
| `.ufo/waves/round-85/w1/ScribeSources/residual-index-ordering.txt` | the index-ordering constraint for the L1 (measured) |
| `.ufo/waves/round-85/w1/ScribeSources.md` | this report |

No other file was written. No git/jj mutation. No file outside the lane and this seat's
scratch was touched. `corpus/lessons/` is unmodified (`git status --short corpus/lessons/`
is empty) — the seven lesson/spot-check files are indexed, never edited.

## Item 1 — CRLF → LF, with the no-cell-changed proof

The committed `corpus/SOURCES.md` was CRLF (436 CRLF, 0 lone CR, 436 LF; 203 260 B).
The census's `## Registry` heading test compares a `\r`-suffixed heading, never enters
the section on this host, and reports every row as E12 — the 180 E12 rows in
`.ufo/waves/round-85/receipts/census-round-start.txt` (exit 1).

Normalization was byte-level (`\r\n` → `\n`, then any lone `\r` → `\n`): 203 260 B →
202 824 B, delta **−436 = exactly the CRLF count**. The worktree was byte-identical to
the base blob before the write (verified by `cmp` at the time), so the
normalization-only intermediate is exactly `git show BASE:corpus/SOURCES.md | tr -d '\r'`
and the proof is reproducible byte-for-byte against the corrected tree:

```
$ diff <(git show 1c8f37edf2e5ac0fb3c2be1c88e32406313fe47b:corpus/SOURCES.md | tr -d '\r') <(tr -d '\r' < corpus/SOURCES.md)
diff exit = 0
diff stdout+stderr bytes = 0
```

Empty output, exit 0 — byte-identical modulo CR. The same fact in the byte direction:
`cmp` exit 0, identical. Line count 436 → 436 and registry rows 180 → 180 unchanged.

**Final-state closure of the audit trail.** Re-running the same command against the
corrected tree reports exactly **one** changed line — line 153, the S213 row of item 2 —
and the byte-level diff with the S213 row excluded is empty (`diff exit=0 ; output
bytes=0`). So the CRLF normalization itself changed no cell, and the only other change
is the declared S213 edit. The current worktree is 60 B larger than the intermediate:
that is the `used-by` addition and nothing else.

Full receipt: `.ufo/waves/round-85/w1/ScribeSources/crlf-proof.txt`.

No other file's line endings were touched (`git diff --numstat` shows only
`corpus/SOURCES.md` and `corpus/README.md` modified).

## Item 2 — S213's `used-by` cell

**OLD** `corpus/knowledge/skill-eval-artefacts-round70.md`
**NEW** `corpus/knowledge/skill-eval-artefacts-round70.md, corpus/knowledge/description-trigger-discipline-round85.md`

The pre-existing path is kept; one path is appended. The row stays at **13
pipe-separated fields**, no cell holds a literal `|`, and **every other cell of the row
is byte-identical to the base** (the anchor cell included — the L1's restoration,
verified cell-by-cell). Both `used-by` paths exist on disk.

**Ordering.** The L1 directed that this update wait until the entry exists. It did not
exist when the seat began (a poll found it landing at 17:18, 225 s later); the edit was
applied only after the file was on disk, so the census's E11 check (a mined row's
`used-by` paths must exist on disk) reads clean.

**The re-opening record this seat measured** (and where it now lives). This seat
re-fetched S213's page independently — own `curl`, own `sha256sum`, own `cmp` — so the
claim is its own measurement, not a transcription of ScoutSource's: HTTP 200, 13 403 B,
sha256 `7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837`, byte-identical
to the committed r76 lane snapshot, the located quote still present verbatim at page
line 92. That record lives in the round lesson and in the scout packet
(`.ufo/waves/round-85/w1/ScoutSource/fetch-record.txt`) — **not** in the registry row,
per the L1's correction.

Full receipt: `.ufo/waves/round-85/w1/ScribeSources/s213-usedby.txt`.

## Item 3 — 8 coverage-map index rows

Rows appended at the end of the `## Coverage map` table, before `## Frontier`, in the
existing 3-column shape (`Area | File | Basis`, 5 pipe-split cells, one backticked token
in the File cell). `git diff --numstat corpus/README.md` shows **8 insertions, 0
deletions** — no existing row was touched.

Seven rows are the files the base receipt named as unindexed
(`.ufo/waves/round-85/receipts/before-gates.txt`):

| Area | File |
|---|---|
| Round-81 non-author spot-check (closure) | `lessons/round-81-verifier-spotcheck.md` |
| Round-82 lessons | `lessons/round-82.md` |
| Round-82 non-author spot-check (closure) | `lessons/round-82-verifier-spotcheck.md` |
| Round-83 lessons | `lessons/round-83.md` |
| Round-83 non-author spot-check (closure) | `lessons/round-83-verifier-spotcheck.md` |
| Round-84 lessons | `lessons/round-84.md` |
| Round-84 non-author spot-check (closure) | `lessons/round-84-verifier-spotcheck.md` |

The eighth is the round-85 documentary entry, added at the L1's direction
("index row new entry+lesson round85"):

| Area | File |
|---|---|
| Description trigger discipline (round 85) | `knowledge/description-trigger-discipline-round85.md` |

Each basis cell is one clause taken from that file's own head — the round number and
host, the two claims or the conformance scope, the closure author — never invented
content. The receipt quotes the grounding head lines for each.

These are closure/lane records: **indexed, never edited**. `git status --short
corpus/lessons/` is empty.

Full receipt: `.ufo/waves/round-85/w1/ScribeSources/readme-index-rows.txt`.

## Item 4 — validation

```
$ bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file corpus/SOURCES.md
file	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md
exit=0
```

**0 E-codes** (E01–E12). 33 W04 duplicate-URL warnings remain — the pre-existing
non-fatal class, unchanged by this seat. Receipt:
`.ufo/waves/round-85/w1/ScribeSources/census-lane-file.txt`.

```
$ bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba
kotoba	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md
exit=0
```

**0 E-codes**, same 33 W04 rows, tail `kotoba ok …`. This is the same file the `--file`
run reads (kotoba is the lane), so both now read the LF-normalized registry. At the base
commit this command exited 1 with 180 E12 rows. Receipt:
`.ufo/waves/round-85/w1/ScribeSources/census-fleet-root.txt`.

```
$ python3 -B verifiers/verify_corpus_integrity.py --json
PASS   corpus.index.unindexed   observed=0  expected=0
```

**`corpus.index.unindexed` observed 0**, `unindexed_detail = []`. The full 9-check
reading:

```
  DRIFT  corpus.index.tracked_files         observed=165  expected=157
  PASS   corpus.index.unindexed             observed=0    expected=0
  PASS   corpus.index.stale_patterns        observed=0    expected=0
  PASS   corpus.index.missing_paths         observed=0    expected=0
  DRIFT  corpus.pointers.report_total       observed=122  expected=113
  PASS   corpus.pointers.report_dead        observed=0    expected=0
  DRIFT  corpus.pointers.commit_total       observed=54   expected=47
  DRIFT  corpus.pointers.commit_unresolvable observed=1   expected=0
  PASS   corpus.pointers.commit_nonhash     observed=0    expected=0
```

These readings are **at the committed tip** — the L1's integration commit `6a520b6`
("reopen S213 for bounded documentary note, normalize registry LF, preserve protected
cells and index inherited records") carries `corpus/SOURCES.md` (LF-normalized, S213
`used-by`) and `corpus/README.md` (the 8 rows) together with the round-85 entry file, so
the entry's index token is now tracked and `corpus.index.stale_patterns` reads **0**.
Before that commit the same worktree read stale=1 — the uncommitted-worktree reading,
which cleared itself when the entry was staged, exactly as measured in
`residual-index-ordering.txt`.

The remaining classes are recorded **as-is**, not claimed:

- `corpus.index.stale_patterns` — **now 0.** It read 1 in the pre-commit worktree
  because the round-85 entry's row named a file that was on disk but not yet in the git
  index; `git ls-files corpus/` lists the **index**, so a staged-but-uncommitted file IS
  listed (probed in a throwaway repo). The L1's integration commit carried the entry
  file with the README, and the class cleared itself exactly as measured in
  `residual-index-ordering.txt`. No baseline change was involved and none would have
  helped — a refresh cannot clear a zero-mode class.
- `tracked_files` 165 vs 157, `report_total` 122 vs 113, `commit_total` 54 vs 47 — the
  baseline-refresh class the L1 clears at the final pre-report commit (plan §
  Conformance repairs 2). This seat added no corpus file and removed none, and its
  edits introduced no report pointer and no commit citation: the S213 cell change
  touches `used-by` only, the 8 README basis cells name no report path and no
  `commit \`token\`` citation, and `report_total`/`commit_total` are unchanged at 122/54
  across the edit.
- `commit_unresolvable` 1 — the pre-existing `corpus/lessons/round-81.md:8` orphan hash
  `8b1cc1b0…`, named in the base receipt. Not this seat's row; not repaired here.

Receipts: `.ufo/waves/round-85/w1/ScribeSources/corpus-integrity.txt` and
`corpus-independent.txt` (the independent instrument reads the same coverage map and
reports the same `unindexed=0` — the reading is not an artefact of one code path).

## Findings for the L1

**1. The index-ordering constraint, measured.** The round-85 entry row must land in the
**same commit as the entry file**: a row that lands first reads
`corpus.index.stale_patterns=1`, and committing the entry without a row leaves
`corpus.index.unindexed=1`. The same applies to the round-85 lesson
`corpus/lessons/round-85.md` (ScribeLesson's file) — its row must land in the same commit
that carries its bytes, or `corpus.index.missing_paths` reads 1.

**The lesson row was deliberately NOT added by this seat**, because ScribeLesson's file
was not on disk when this seat wrote. Measured, all three states:

```
lesson row added, lesson file NOT on disk                -> unindexed=0 stale=2 missing=1
lesson row added, lesson file on disk but not yet indexed -> unindexed=0 stale=1 missing=1
lesson row added, lesson file staged/committed           -> unindexed=0 stale=0 missing=1
```

A coverage-map row naming a file that does not exist is a broken promise the index
census correctly reports — so the lesson row belongs in the L1's integration commit,
together with ScribeLesson's file and its bytes, not in a worktree where the file is
absent. (The `missing=1` in the third line above is the simulated state where the row
is added but the file's bytes are still absent; with both in the same commit it reads 0.)

The entry row, whose file **is** on disk, was added by this seat. Its `stale=1` was the
uncommitted-worktree reading only: `git ls-files corpus/` lists the git **index**, so a
staged-but-uncommitted file IS listed (proved in a throwaway repo). It cleared itself
when the L1's integration commit `6a520b6` carried the entry file with the README —
`corpus.index.stale_patterns` now reads **0**. No baseline change was involved and none
would have helped, since a baseline refresh cannot clear a zero-mode class. The
remaining `equal`-mode classes still need the baseline refresh. Receipt:
`.ufo/waves/round-85/w1/ScribeSources/residual-index-ordering.txt`.

**2. S018's digest is stale** (flagged by ScoutSource): the specification page now serves
7 685 B (sha256 `bf4137a7…`) while the S018 row pins 7 608 B (`9a67de89…`). The
1024-character rule is still present, so C1's R3 is unaffected, but the row's digest no
longer matches the live page. S018 is a registry row and this seat owns
`corpus/SOURCES.md` — but re-opening S018 is outside this seat's four assigned repairs
and would need its own live fetch and citation change, so it is reported here rather
than done. **Not repaired by this seat.**

**3. The census's W04 class is 33 rows**, not the 32 the round-82/83/84 lessons record
(S249 was added at round 81). W04 is a non-fatal warning and does not change any gate's
exit code. Recorded, not claimed.

**4. `check_sources_append_only.py --rev <base>` reads 19 breaches in 9 of 51 committed
commits** (S207, S209, S210, S248 anchors among them). These are pre-existing and
unchanged by this seat; the worktree delta is clean (0 breaches, 1 permitted log note).
Recorded for the round's awareness.

## Out of scope (not done by this seat)

- `corpus/lessons/round-85.md`, `LOG.md`, and the round-84 correction block —
  ScribeLesson's files.
- `corpus/knowledge/description-trigger-discipline-round85.md` — ScribeC1Entry's file.
- `verifiers/check_description_render.py`, `verifiers/fixtures/description-render/` —
  ExecC1Counter's files.
- The four omp path constants and the candidate baseline — ExecC2Pin's files.
- `SKILL.md` — integrated by the L1.
- The baseline refresh, and the integration commit that carries the round-85 entry and
  lesson files with their index rows — the L1's round-end step.

## Environment

- **Tooling**: no install, no upgrade, no package manager transaction. `python3`,
  `curl`, `sha256sum`, `cmp`, `grep`, `diff`, `tr` were already present; nothing in the
  operator tooling directive applied. (PACMAN is paused host-wide and was not touched;
  the operator's tooling directive was read first at `/home/vgpnk/.omp/agent/RULES.md`.)
- **Scratch**: `/fast/scratch/hyaku/kotoba-r85/ScribeSources` — created with
  `mkdir -p`, passed explicitly as the only write target for the fetch and the probe
  scripts, removed before yielding.
- **Git**: read-only only (`status`, `ls-files`, `show`, `cat-file`, `diff`,
  `rev-parse`); no mutation. The `git ls-files` index-semantics probe used a throwaway
  repository under this seat's scratch.
- **Reads**: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh` (read only, not
  modified), the lane's `corpus/`, `verifiers/verify_corpus_integrity.py`,
  `verifiers/verify_corpus_independent.py`, `verifiers/check_sources_append_only.py`,
  and the wave-85 receipts. The read-only `shokuknow` tree was not read or written by
  this seat.
