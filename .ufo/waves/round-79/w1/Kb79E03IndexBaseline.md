# Kb79E03IndexBaseline — C1 repair 3 of 4: corpus index and baseline

Round 79 w1 (kotoba). Lane `/home/vgpnk/Projects/shokunin/kotoba-shokunin`, plan commit
`2c56622375641193a03bb97c0624e6536f3dffba` (F1). Lane tip at the time of writing: `91a2fce`
(freeze clarifications; `corpus/README.md` and `verifiers/corpus-baseline.json` are byte-identical
to the plan commit — `git show 2c56622:corpus/README.md` hashed equal to the worktree file).
Item: index the six tracked-but-unindexed corpus files, and make the corpus baseline
re-recordable at any tip by a re-runnable script.

## 1. What the two gates actually read (measured, not inferred)

| gate | index source | `unindexed` rule |
|---|---|---|
| `verifiers/verify_corpus_integrity.py` | column 2 (`cells[2]` of a pipe-split line) of every pipe-starting row between `## Coverage map` and the next `## ` heading, backticked tokens only, fence regions skipped (`file_column_tokens`, `verifiers/verify_corpus_integrity.py:388-421`; section rule `SECTION_HEADING_RE`/`COVERAGE_HEADING_RE` at :155-157) | a tracked corpus file (`git ls-files corpus/`, README excepted) that no column-2 token denotes is `unindexed` |
| `verifiers/verify_corpus_independent.py` | same cells, independently written (`coverage_cells`, `verifiers/verify_corpus_independent.py:317-346`), then `POINTER_RE`/brace/glob expansion over them (:349-411) | same closed-set rule, computed against tracked ∪ on-disk |

Both gates therefore need exactly one thing per file: a backticked corpus-relative path in column 2
of a coverage-map row. Column 3 is prose but *not* inert for the integrity gate: it is scanned for
`.ufo/reports/round-<n>/*.md` pointers and `commit `<hex>`` citations, so the six rows I wrote carry
neither shape (measured: `report_total` 106 and `commit_total` 45 are unchanged by the rows;
receipts in §4).

Baseline form (copied from earlier refreshes, studied with
`git -C <lane> log --oneline -- verifiers/corpus-baseline.json` → `1cf5afa`, `559ee76`, `aa9c9ad`,
`14ab415`, …): one JSON object, `indent=1`, keys `as_of`, `host`, `measured_against`
(`repo`, `head`, `head_subject`, `git_status`, `command`, `note`), `checks` (id → `{mode, expect}`),
`notes` (append-only prose history, one key per round). `git show 1cf5afa` is the minimal form: a
single `expect` 42 → 43. `git show aa9c9ad` is the fuller form (`130/0/89/39` with a note). My
refresh follows the fuller form and appends `notes.round79_rerecord`.

## 2. The six rows (each description read from its own file, not from the plan)

Appended contiguously after the `Round-74 verifier spot-check (closure)` row (patched file lines
150–155), so the block sits inside the table with no blank line:

| area | file |
|---|---|
| Round-75 non-author spot-check (closure) | `lessons/round-75-verifier-spotcheck.md` |
| Round-76 non-author spot-check (closure) | `lessons/round-76-verifier-spotcheck.md` |
| Round-77 lessons | `lessons/round-77.md` |
| Round-77 non-author spot-check (closure) | `lessons/round-77-verifier-spotcheck.md` |
| Round-78 lessons | `lessons/round-78.md` |
| Round-78 non-author spot-check (closure) | `lessons/round-78-verifier-spotcheck.md` |

Each basis cell states what the file contains, read at the base tree: r75 spot-check ("admitted,
improved and bounded", five-row discernment table, quality/discernment harmed, R1–R4); r76
spot-check (honest stop, all axes unchanged, R76-D1–D5); r77 lesson (both candidate claims rejected
because the do-nothing control reached C1 `6 of 6` and C2 `4 of 4`); r77 spot-check
(`rejected-honest-stop`, both frozen sha256s matching the plan, R77-D1–D3); r78 lesson (no
knowledge/S### row, predicate-reachability mistake); r78 spot-check (both claims `unprovable`, four
routed defects). The three non-author files are named "written by the hyaku closure, not the lane
(outside review; never edited here)" exactly as the neighbouring closure rows (rounds 51–73) do, and **no
spot-check byte was touched** (the tip battery's `spotcheck-identity` guard has nothing to see;
`git diff 2c56622..1196983 --stat` shows only `corpus/README.md` and
`verifiers/corpus-baseline.json`).

## 3. The refresh script

`build/refresh-corpus-baseline.py` (stdlib only, `sha256 8481be46ab6b74656fe7fa68c53300a5e490ee23265e69768d4dfeed770b470a`).

- **What it records:** for every id in `checks`, the observation is taken from that id's last
  component in the integrity gate's own `--no-baseline --json` document. `equal` rows get the
  observed integer; `zero` rows are written `expect: 0` and never fitted. It refuses if any
  baseline id has no observed key or an unknown mode.
- **Preconditions (exit 2, baseline untouched):** `--repo` is a directory *and* the toplevel of a
  git work tree; the tree carries the two gates, the baseline and `corpus/README.md`;
  `git status --porcelain --untracked-files=all` is empty (the gate reads worktree bytes while the
  baseline is recorded at HEAD, and `git ls-files corpus/` cannot see untracked files);
  `verify_corpus_integrity.py --self-test` exits 0; both gates run and emit JSON (exit 2/3 is an
  environment answer, not a measurement); the two gates agree on every class this script records
  (`tracked_files`, `unindexed`, `stale`, `missing`, `report_total`, `commit_total`).
- **Carried residual:** a nonzero zero-mode class refuses **unless** named with
  `--carry <check-id>`; its expectation still stays 0, the residual is printed and stamped into
  `measured_against.note`, and `corpus.index.*` can never be carried (an unindexed/stale row is the
  thing the caller must fix first). This is how the E04-owned `report_dead` is handled without
  laundering it.
- **Divergence, not refusal, for the three advisory zero classes** (`report_dead`,
  `commit_unresolvable`, `commit_nonhash`): a gate disagreement is printed and stamped into the
  note, because their expectation is 0 either way and the disagreement is a finding about the
  instruments (§6).
- **Head honesty:** `measured_against.head` is the abbreviated sha only when `refs/heads` contains
  it; a detached measurement commit is labelled
  `"<sha> (detached measurement commit; resolvable in the measuring clone only, not in the lane repository)"`.
  (`git branch --contains` is not usable: on detached HEAD it prints the pseudo-entry
  `(HEAD detached from …)`.)
- **Writes:** exactly one path, `<repo>/verifiers/corpus-baseline.json` (refuses a symlink). Raw
  gate JSON goes to a `tempfile.mkdtemp` under `$TMPDIR` and is removed unless `--keep-temp`.
- **Post-condition:** re-runs the integrity gate with the new baseline; drift not covered by a
  carried id → exit 3. Then runs the independent gate and prints its last line and exit code; a
  red independent gate is printed to stderr as `independent: red (exit 1)` and does not fail the
  write — the baseline serves the integrity gate and the caller's next step adjudicates it.
- **Exit:** 0 written (or `--dry-run`), 2 refused, 3 internal/post-condition failure.

Refusals measured (receipt `build/Kb79E03/script-refusals.txt`, all `rc=2`): not a git work tree;
`--carry corpus.index.unindexed`; a git repo missing the gates/baseline ("unexpected tree"); a tree
with one modified file ("dirty tree: … M plans/round-79.md").

## 4. Evidence (scratch clone, every command with its own exit)

Scratch: `S=/fast/scratch/hyaku/kotoba-r79/Kb79E03IndexBaseline`, shared clone checked out at
`2c56622…`, toplevel assertion passed (`git -C "$S/clone" rev-parse --show-toplevel` = the clone).
Commits in the clone: `35bbecd` (six rows), `1196983` (baseline re-record).

Base, before any change (`python3 -B verifiers/verify_corpus_integrity.py --json`, rc **1**):

    corpus.index    tracked=150 unindexed=6 stale=0 missing=0
    corpus.pointers report_dead=1/106 commit_total=45
    4/9 checks pass; DRIFT: tracked_files 144≠150, unindexed 6≠0, report_total 106≠99,
                        report_dead 1≠0, commit_total 45≠43

`python3 -B verifiers/verify_corpus_independent.py --json`, rc **1**:
`unindexed 6` = `corpus/lessons/{round-75-verifier-spotcheck,round-76-verifier-spotcheck,
round-77-verifier-spotcheck,round-77,round-78-verifier-spotcheck,round-78}.md`; `stale 0`,
`missing 0`, `report_total 106`, `commit_total 45`, `report_dead 0`.

After the six rows (`35bbecd`, baseline still old), rc **1**:

    integrity:    unindexed=0 stale=0 missing=0; 5/9 (the three equal classes + report_dead drift)
    independent:  unindexed=0 stale=0 missing=0; exit 0

Refresh (`refresh-corpus-baseline.py --repo $S/clone --carry corpus.pointers.report_dead`), rc **0**
(receipt `build/Kb79E03/write4.txt`):

    gate disagreement (not recorded, expectation stays 0): corpus.pointers.report_dead integrity 1 vs independent 0
    corpus.index.tracked_files         144 -> 150
    corpus.pointers.report_total       99 -> 106
    corpus.pointers.commit_total       43 -> 45
    carried red: corpus.pointers.report_dead observed 1, expectation stays 0
    post-refresh: 8/9 checks pass, exit 1, drift: corpus.pointers.report_dead
    independent: exit 0

At the refreshed tip `1196983` (receipts `tip-integrity.txt`, `tip-independent.txt`):

    corpus.index    tracked=150 unindexed=0 stale=0 missing=0  (168 FILE-column patterns over 149 md files)
    corpus.pointers report_dead=1/106 commit_total=45 unresolvable=0 nonhash=0
    8/9 checks pass; DRIFT: corpus.pointers.report_dead
    independent: index tracked_files=150 unindexed=0 stale=0 missing=0 … exit 0

Patch proof on a **pristine** second clone at the plan commit (`git -C applytest reset --hard
2c56622 && git apply --check <patch>`, rc 0; apply; measure): identical numbers —
`unindexed=0 stale=0 missing=0`, `8/9`, `report_dead=1`, independent `exit 0`
(`build/Kb79E03/apply-integrity.txt`, `apply-independent.txt`). Rows-only patch alone:
`unindexed=0 stale=0 missing=0`, `5/9` (`build/Kb79E03/rows-only-integrity.txt`).

Diff: `git diff --stat 2c56622..1196983` → `corpus/README.md | 6 ++++++`,
`verifiers/corpus-baseline.json | 17 +++++++++--------` (2 files, 15 insertions, 8 deletions;
numstat 6/0 and 9/8). `corpus-baseline.json` changes only the three `expect` values,
`as_of`/`measured_against`, and one appended `notes.round79_rerecord`.

Patch-format note for integration: the lane and its clones run with `diff.mnemonicPrefix=true`, so
a bare `git diff` emits `i/`…`w/` headers that `git apply` rejects. All three patch files were
generated with `--src-prefix=a/ --dst-prefix=b/` and pass `git apply --check` from `2c56622`.

## 5. Final-tip procedure (the exact order the L1 must run)

This round adds more corpus files (`corpus/lessons/round-79.md`, the C2 entry, a round-79
spot-check), so the baseline recorded here is a mid-wave snapshot and **must be re-derived at the
final tip**. Order:

1. Land every new corpus file, then write its coverage-map row in `corpus/README.md` (column 2,
   backticked corpus-relative path) — every row while its file is tracked; a row without its file
   is `stale_patterns` +1 *and* `missing_paths` +1.
2. Commit the content through `jj-lane.sh` (the gate's universe is `git ls-files`, so commit, do
   not stage only).
3. From the lane toplevel with a clean tree:
   `python3 -B .ufo/waves/round-79/build/refresh-corpus-baseline.py --repo .`
   (add `--carry corpus.pointers.report_dead` only if E04's repair has not landed). It prints
   old → new per key and refuses on a dirty tree.
4. Commit `verifiers/corpus-baseline.json` alone (the recorded `head` is step 2's commit, which is
   a real lane object: the lane's detached HEAD is contained in `refs/heads/master`, which
   is the rule the script uses, so the label is a plain sha there).
5. Re-run both gates and the tip battery:
   `python3 -B verifiers/verify_corpus_integrity.py --json` (target `9/9`, exit 0),
   `python3 -B verifiers/verify_corpus_independent.py --json` (target exit 0),
   `python3 -B verifiers/check_tip_battery.py --rev <tip>` in both `--repo .` and absolute forms.

Integration of this seat's work: apply `build/Kb79E03IndexBaseline.patch` (rows only — the durable
content fix) or `build/Kb79E03IndexBaseline.with-baseline.patch` (rows + the mid-wave baseline; its
`measured_against.head` says it is a detached measurement commit and its counts will be overwritten
by step 3 at the final tip). `build/Kb79E03IndexBaseline.baseline-snapshot.patch` is the baseline
hunk alone, kept as evidence.

## 6. `report_dead`: what the baseline shows, and the exact residual

The baseline records `corpus.pointers.report_dead` as `mode: zero, expect: 0`. My refresh does not
change that, so **the gate stays red on it**: the observation is 1 at the base, after the six rows,
and at the refreshed tip. `8/9` is the ceiling this seat can reach; E04 owns the last check.

The single site (integrity gate, `--json` detail): `corpus/lessons/round-77-verifier-spotcheck.md:15:
HEAD:.ufo/reports/round-77/kotoba.md`. It is **not a missing file**: the fleet report exists
(`/home/vgpnk/Projects/shokunin/.ufo/reports/round-77/kotoba.md`, 8547 B). It is a resolver-prefix
defect:

- `UFO_POINTER_RE` (`verifiers/verify_corpus_integrity.py:146`) admits `:` inside the token, so the
  harvested token is `HEAD:.ufo/reports/round-77/kotoba.md`;
- `report_pointer_exists` (:273-277) grants the fleet hop only when
  `token.startswith(".ufo/reports/")`, which this token fails;
- the independent gate's `POINTER_RE` (`verifiers/verify_corpus_independent.py:123-124`) excludes
  `:` from its character class, so it harvests `.ufo/reports/round-77/kotoba.md`, takes the fleet
  hop, and reads `report_dead 0`.

So the two instruments disagree on this class (integrity 1, independent 0) while agreeing on the
file's existence. The fix is a tokenizer/hop repair in the corpus gate (or a resolution rule that
peels a git object prefix) — **not** an edit to the non-author spot-check, whose bytes the tip
battery's `spotcheck-identity` guard pins. E04 should also expect the two-gate divergence in its
receipts; my script prints and stamps it rather than hiding it.

## 7. Risks, limits, what I did not do

- The refreshed baseline in the patches was measured on a detached scratch commit; at the final tip
  it must be re-recorded (step 3) so `measured_against.head` names a lane object.
- The rows are descriptions of files I read at the base tree; they make no claim about the files'
  contents beyond what those bytes say.
- I did not run the tip battery (another seat owns it) and did not run any build/lint/test loop.
- I did not edit any spot-check, gate, `SKILL.md`, `SOURCES.md`, `LOG.md`, `SCORECARD.md`,
  `MANIFEST.json`, `templates/`, `scripts/`, `.ufo/state/` or the lane git/jj state. No tool
  installs or upgrades were needed (none run; pacman untouched).
- Scratch (`/fast/scratch/hyaku/kotoba-r79/Kb79E03IndexBaseline`, two clones + fixture) was removed
  before yielding; receipts were copied into `build/` first.

VERDICT: Six coverage-map rows land cleanly from the plan commit; both gates read `unindexed 0, stale 0, missing 0`, the refreshed baseline is `tracked 150 / report 106 / commit 45` (from the gate's own `--no-baseline --json`), and the round's ceiling for this seat is `8/9` with only the E04-owned `report_dead` (`HEAD:`-prefixed token defeats the integrity gate's fleet hop; the independent gate reads 0) still red.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79E03IndexBaseline.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79E03IndexBaseline.with-baseline.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79E03IndexBaseline.baseline-snapshot.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/refresh-corpus-baseline.py, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79E03/
