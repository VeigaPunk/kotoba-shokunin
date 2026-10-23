# ExecIndexCorpus — corpus index lines for round 59 (INDEX drift at base)

Result: DONE — three index rows are delivered as an apply-clean patch; the base `corpus.index.unindexed`
DRIFT is caused by the round-58 spot-check landing without a row, and `verifiers/corpus-baseline.json`
does need a re-record, but a re-record alone can NOT make the gate green: `corpus.pointers.commit_unresolvable`
is zero-mode (baseline-independent) and stays 1 until one citation in `corpus/lessons/round-54-verifier-spotcheck.md:147`
is reshaped. Both facts are measured below.

## 1. How the instrument decides "indexed"

`verifiers/verify_corpus_integrity.py` (read at the freeze rev; line cites are that file):

- `file_column_tokens()` (`:361`) harvests backticked tokens from **column 2 only** (`cells = line.split("|")`
  `:382`, `file_cell = cells[2]` `:385`) of every row inside the `## Coverage map` section
  (`COVERAGE_HEADING_RE`, `:153`; the next `## ` heading ends it, `:377-379`). Fenced lines are opaque
  (`fenced_lines` `:325`, applied `:410`).
- Each token is brace-expanded and matched against the tracked set (`expand_pattern`, `:250-258`;
  `covered |= hits`, `:432`); `covered` is therefore "paths some FILE-column pattern denotes".
- `unindexed` = tracked `corpus/` files minus `corpus/README.md` that `covered` misses (`:443-444`):
  `unindexed_names = [t for t in tracked if t != INDEX_NAME and t not in covered]`.
  `tracked` is `git ls-files corpus/` (`tracked_corpus_files`, `:557`), so an **untracked** new corpus file is
  invisible to the check: rows-first and file-first fail in different ways (see § 7).
- Verdicts: `zero` ids are baseline-free and always adjudicated (`evaluate`, `:664-681`), so
  `unindexed`, `stale_patterns`, `missing_paths`, `report_dead`, `commit_unresolvable`, `commit_nonhash`
  cannot be silenced by editing the baseline. Only the three `equal` ids (`tracked_files`, `report_total`,
  `commit_total`) move by re-record.

## 2. How earlier spot-check lessons were indexed

Every closure-authored spot-check before this one carries a coverage-map row in `corpus/README.md` with the
same shape, and the row is added in the **following** round (grep of `corpus/README.md` at `67b68e0`):

| row | line | wording of the tail |
|---|---|---|
| Round-54 spot-check | `:86` | "landed without an index row, indexed round 55" |
| Round-55 spot-check | `:89` | "…indexed round 56" |
| Round-56 spot-check | `:92` | "…indexed round 57" |
| Round-57 spot-check | `:95` | "…indexed round 58" |
| Round-58 spot-check | **absent** | this file is the drift: `corpus.index.unindexed observed=1` |

The round-53 precedent also records the harm verbatim (`:83`: "landed without an index row, indexed round 54"),
and the same class is lesson M21 (round-47). The round-58 spot-check landed in `a975cbb`
(`git log --oneline -1 a975cbbf` → `a975cbb round-58 verifier spot-check (integrator, hyaku): non-author
admit/reject`) with no row, which is exactly the shape those rows describe.

## 3. Delivered patch

`/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/build/ExecIndexCorpus.patch`
(sha256 `5e879e0ac264301de38ee6b3c4b7d49440393dbd0fc78a7d19fd5dd041c82080` — final value in § 10 ls), 14 lines,
`corpus/README.md` only, inserts three rows after `| Round-58 lessons | … |` (base line 97) and before the blank
line that precedes `## Frontier`:

```
+| Round-58 non-author spot-check (closure) | `lessons/round-58-verifier-spotcheck.md` | written by the hyaku closure, not the lane (outside review; never edited here): round 58 admitted, C1 verified (`6 of 6; new ground 4`); routed defects R1–R6 (round 59 works R1–R5 in `lessons/round-59.md`); landed at `a975cbbf` without an index row (which turned `verify_corpus_integrity.py` red at that base: `unindexed 1`), indexed round 59 |
+| Hook files by client (round 59) | `knowledge/hook-files-round59.md` | six clients' own docs (S096–S101) on the file or folder each names for hook configuration — `.claude/settings.json`, `~/.codex/hooks.json`, `.github/hooks/*.json`, `~/.copilot/hooks/*.json`, `.gemini/settings.json`, `.cursor/hooks.json` — and the events each hook fires on; opencode not eligible (its hook code lives only in plugin folders); `SKILL.md` § Hook files by client; `../verifiers/check_hook_files.py --rev <rev> --fetch` |
+| Round-59 lessons | `lessons/round-59.md` | `## Gate` S096–S101 with access records and the rejections; `## Mistakes` M79 onward; the round-58 routed defects R1–R5 |
```

Row-shape checks against rows S089–S095's neighbours and the frozen claim: the label of the entry row is the
`SKILL.md` section name (`§ Hook files by client`), the tail names the counter with `--rev <rev> --fetch`, the
spot-check row uses the established "landed at `<rev>` without an index row …, indexed round N" phrasing, and
M79 is the next free mistake number (`corpus/lessons/round-58.md` last id is M78).
The File cells are in the counter's corpus-relative form; the client paths and the counter command sit in the
**Basis** cell, which the INDEX reader never harvests (`cells[2]` only, § 1), so `~/.codex/hooks.json` and the
globs cannot become stale/missing findings.

Application check at the base rev (pristine clone, patch not applied):

```
$ cd /fast/scratch/hyaku/kotoba-r59/base && git apply --check --verbose <patch>
Checking patch corpus/README.md...
apply --check exit=0
```

The lane's own `corpus/README.md` is byte-identical to that clone (`sha256sum` both:
`bc14ad4f9ee806014ba352683a27a99b1617777b48ce257d719b4528acfb7709`; `git diff 67b68e0..HEAD -- corpus/README.md`
is empty at lane HEAD `283124c`), so the patch applies to the lane as it stands — unless another seat lands the
same rows first (see § 9). Checked against the lane itself, read-only:

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin && git apply --check --verbose <patch>
Checking patch corpus/README.md...
exit 0
```

## 4. Gate before → after (measured, not asserted)

Sandbox `/fast/scratch/hyaku/kotoba-r59/ExecIndexCorpus` = clean clone at
`67b68e0f9a0c48e5aa5ced63e6117cfca69da491`; two stub corpus files created there (never in the lane) and
`git add`ed so `git ls-files` counts them, as the real landing will:

before (pristine `/fast/scratch/hyaku/kotoba-r59/base`, same rev, committed baseline):

```
$ python3 -B verifiers/verify_corpus_integrity.py --json     # exit=1
DRIFT corpus.index.tracked_files          observed=94 expected=81
DRIFT corpus.index.unindexed              observed=1  expected=0 / empty
        unindexed_detail: corpus/lessons/round-58-verifier-spotcheck.md
PASS  corpus.index.stale_patterns         0
PASS  corpus.index.missing_paths          0
DRIFT corpus.pointers.report_total        observed=64 expected=51
PASS  corpus.pointers.report_dead         0
DRIFT corpus.pointers.commit_total        observed=33 expected=32
DRIFT corpus.pointers.commit_unresolvable observed=1  expected=0 / empty
        commit_unresolvable_detail: corpus/lessons/round-54-verifier-spotcheck.md:147: 451a02ff
PASS  corpus.pointers.commit_nonhash      0
```

after the three rows + the two stub files, **old** baseline (exit=1):

```
PASS  corpus.index.unindexed              0            <- the assigned drift is closed
PASS  corpus.index.stale_patterns         0
PASS  corpus.index.missing_paths          0
DRIFT corpus.index.tracked_files          96 vs 81
DRIFT corpus.pointers.report_total        64 vs 51
DRIFT corpus.pointers.commit_total        33 vs 32
DRIFT corpus.pointers.commit_unresolvable 1  vs 0 / empty
```

`index_patterns` 111 → 114 and `index_tokens_total` 111 → 114 (one new pattern per row); `report_total` and
`commit_total` are **unchanged by the rows** (no `.ufo/reports/` pointer and no `commit `hex`` citation in any
of the three Basis cells — checked deliberately, since those are `equal` pins).

## 5. Baseline: yes, it needs a re-record — and the re-record alone is not enough

`verifiers/corpus-baseline.json` pins `tracked_files 81` / `report_total 51` / `commit_total 32`, recorded at
round 54 (`notes.round54_rerecord`: "tracked_files 78 -> 81 … report_total 49 -> 51"). At the round-59 base the
pins are already stale by the rounds 55–58 landings: observed 94 / 64 / 33. Measured independently at the
round-58 tip to show the sequence:

```
$ (clone at ed44e0c4) python3 -B verifiers/verify_corpus_integrity.py --json   # exit=1
DRIFT tracked_files 93 vs 81; DRIFT report_total 62 vs 51; DRIFT commit_total 33 vs 32;
DRIFT commit_unresolvable 1;  (unindexed PASS)                     -> 4 DRIFT
$ (clone at a975cbbf)  … identical except tracked_files 94 and unindexed 1  -> 5 DRIFT
```

So the round-58 spot-check's "corpus-integrity 4 DRIFT at tip" was accurate at `ed44e0c4`, and that commit's
own new file is what made it 5 at `a975cbbf`. Round 59 with this item's rows lands at **4 DRIFT** (measured in
§ 4) and stays red until the baseline is re-recorded (→ 1 DRIFT) **and** the § 6 citation is repaired (→ 0).

**Command that does the re-record** (the baseline's own `measured_against.command`, and the form every
`notes.round*` entry names):

```
python3 -B verifiers/verify_corpus_integrity.py --no-baseline --json
```

then copy the observed values of the three `equal` ids into `checks.<id>.expect` and add a `notes.round59_*`
sentence naming what moved and why (round-54 form). Re-recording is not a "fit the denominator" move here: the
pin has been stale since round 54, and the round-59 rows add **no** pointer and **no** citation, so for this
item's own work only `tracked_files` moves.

Expected pin set after the round-59 corpus files land (measured with the stubs; re-measure for real, the lesson
and the entry prose may add pointers/citations of their own):

| id | old pin | new pin | why |
|---|---|---|---|
| `corpus.index.tracked_files` | 81 | **96** | 94 observed at base + the two new files this item indexes (`knowledge/hook-files-round59.md`, `lessons/round-59.md`); the round-58 spot-check was already tracked. Any further corpus file this round adds 1 each |
| `corpus.pointers.report_total` | 51 | **64** | drifted by rounds 55–58; unchanged by my rows |
| `corpus.pointers.commit_total` | 32 | **32** (unchanged) | only if § 6's repair is taken; without it, 33 |
| the six `zero` ids | 0 | 0 | baseline-independent; measured 0 after the repair |

## 6. Blocker the re-record cannot clear: `commit_unresolvable` (zero-mode)

`corpus/lessons/round-54-verifier-spotcheck.md:146-147` reports on a citation shape and instantiates it:

```
`` commit `451a02ff` `` grammar in the new entry
```

`COMMIT_RE` (`:149`) matches `commit `451a02ff`` there, the token is 8 hex chars, and `inside_quotes` is false
(the span is in backticks, not double quotes), so it counts as a promise. It does not resolve in this repo —
it is an upstream gemini-cli hash:

```
$ git cat-file -e 451a02ff^{commit}; echo $?
fatal: Not a valid object name 451a02ff^{commit}
128
```

`corpus.pointers.commit_unresolvable` is `zero` mode, so `evaluate()` (`:670-672`) adjudicates it with no
baseline: **no re-record can clear it** and the gate keeps exiting 1 at the landed tree.

Smallest repair consistent with the counter's own documented idiom (a document *reporting on* a citation is a
"quoted meta-finding", moved to `commit_quoted_detail`, docstring `:60-61`, applied at `:498`) — insert two
double quotes:

```diff
--- a/corpus/lessons/round-54-verifier-spotcheck.md
+++ b/corpus/lessons/round-54-verifier-spotcheck.md
@@ -145,5 +145,5 @@
 No axis is harmed. The `commit_unresolvable` 0→1 that `W2CriticNoHarm` found at `58db81c4` (the
-`` commit `451a02ff` `` grammar in the new entry) was fixed in `cae8f2ea`. At the tip the entry reads
+"`` commit `451a02ff` ``" grammar in the new entry) was fixed in `cae8f2ea`. At the tip the entry reads
 `google-gemini/gemini-cli@451a02ff`.
```

Measured on the patched tree with the re-recorded pins (`simA`):

```
$ python3 -B verifiers/verify_corpus_integrity.py
corpus.index    tracked=96 unindexed=0 stale=0 missing=0  (114 FILE-column patterns over 95 md files)
corpus.pointers report_dead=0/64 commit_total=32 unresolvable=0 nonhash=0 (shapes [relative=1, absolute=42,
                tilde=1, bare=20], quoted-excluded=6, pointer-excluded=8)
9/9 checks pass
plain exit=0
$ python3 -B verifiers/verify_corpus_integrity.py --self-test    # exit=0
self-test: 0 failure(s) over 152 assertions
$ python3 -B verifiers/verify_corpus_independent.py               # exit=0
index tracked_files=96 index_tokens=114 (outside coverage map=18) unindexed=0 stale=0 missing=0
points candidates=74 checked=64 excluded=8 quoted=2 dead=0
commits candidates=38 citations=32 hex=32 quoted=6 nonhash=0 unresolvable=0
```

The independent instrument agrees on every number, including `unresolvable=0`. Two consequences for the L1:
(a) the repair edits an outside-authored spot-check, so it needs the one-line record the lane uses for that
(LOG entry or the round-59 lesson corrections section) — the file's own header says "never edited here";
(b) if the L1 declines the edit, then `commit_total` re-records to **33**, not 32, and the gate must be
recorded as red on `commit_unresolvable` with this file named as the cause.
An alternative prose rewrite ("a bare commit-plus-hex citation in the new entry") removes the token the same
way; I did not measure it — [INFERENCE] it clears the same test, since no `commit `hex`` span remains.

## 7. Ordering constraint (the rows and the files must land in one commit)

- Rows first, files untracked → each token matches no tracked file: `corpus.index.stale_patterns` +1 per row
  (`index_findings`, `:434`), a `zero` DRIFT.
- Files first, rows later → `corpus.index.unindexed` +1 per file (`:443-444`) — the exact drift this item closes.
- Measured in the sandbox with the stubs added and **no** rows: `tracked_files=96, unindexed=3`
  (`hook-files-round59.md`, `round-58-verifier-spotcheck.md`, `round-59.md`), `stale_patterns=0`.

## 8. Boundaries honoured

Nothing in the lane was written, staged, committed or checked out: every run above happened in
`/fast/scratch/hyaku/kotoba-r59/{ExecIndexCorpus,base,simA,tip58}`; lane git use was
`git --no-optional-locks log/diff/status`, `git apply --check` (writes nothing, exit 0, reported in § 3),
plus reads. No jj commands. No package installs or upgrades this item (nothing needed). No model/CLI calls.
Files I wrote in the lane: this report and `.ufo/waves/round-59/build/ExecIndexCorpus.patch`, nothing else.

## 9. Risks for the integrator

1. **Duplicate rows.** If a scribe seat also drafts these rows, take exactly one set — applying the patch twice
   duplicates three table rows (the counter would still pass: duplicate rows are harmless to `covered`, but the
   README would be wrong).
2. **Row wording vs. what actually lands.** The entry row claims S096–S101 and an Events column; the lesson row
   claims S096–S101 with "the rejections" and M79. If a seat opens S102 (the reserved supporting page) or a
   client is rejected outright, amend those two Basis cells accordingly (round-57 row precedent has no result
   suffix; round-57's entry row carries "(C1 missed: `4 of 4; new ground 4`)" — the L1 may append the C1 line
   once the counter runs).
3. **The base pin is stale by four rounds.** A reader who sees "4 DRIFT at base" should not read it as damage
   from round 59; § 5's table separates the inherited drift from this item's one-file move.

## 10. Evidence paths

```
$ ls -l /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/build/ExecIndexCorpus.patch \
        /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/build/ExecIndexCorpus.md
-rw-r--r-- 1 vgpnk vgpnk 16167 Oct 23 06:40 .ufo/waves/round-59/build/ExecIndexCorpus.md
-rw-r--r-- 1 vgpnk vgpnk  2335 Oct 23 06:38 .ufo/waves/round-59/build/ExecIndexCorpus.patch
$ sha256sum .ufo/waves/round-59/build/ExecIndexCorpus.patch
5e879e0ac264301de38ee6b3c4b7d49440393dbd0fc78a7d19fd5dd041c82080  .ufo/waves/round-59/build/ExecIndexCorpus.patch
```

The `.md` size above was taken before this block was written into it, so a fresh `ls -l` shows this file a few
hundred bytes larger; the `.patch` is final (its hash is re-checked after every write).

Sandboxes (all mine, nothing of the lane): `/fast/scratch/hyaku/kotoba-r59/ExecIndexCorpus` (rows + stubs),
`.../base` (pristine `67b68e0`, before-state), `.../tip58` (pristine `ed44e0c4`), `.../simA` (rows + stubs +
re-recorded pins + the § 6 repair). No sandbox commit hash is cited anywhere in this report.
