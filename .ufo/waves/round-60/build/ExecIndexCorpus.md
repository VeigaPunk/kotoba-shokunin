# ExecIndexCorpus — corpus index rows for round 60 (INDEX drift at base)

Result: DONE — three coverage-map rows are delivered as an apply-clean patch; the base
`corpus.index.unindexed` DRIFT (1, the round-59 spot-check) is closed by the patch, but the gate
cannot be made green by index rows alone: `corpus.pointers.commit_unresolvable` is zero-mode
(baseline-independent) and stays 1 until one citation in
`corpus/lessons/round-54-verifier-spotcheck.md:147` is reshaped, and the three `equal` pins
(`tracked_files` 81, `report_total` 51, `commit_total` 32) are stale by four rounds. Both facts
are measured below, with the exact repair path.

## 1. How the instrument decides "indexed"

`verifiers/verify_corpus_integrity.py` at the freeze rev `b1cd64bb45eee744c4ec93be8631f1eddb28fddd`
(line cites are that file; its bytes are identical at lane HEAD `56a611d` —
`git show <rev>:verifiers/verify_corpus_integrity.py | sha256sum` → `21137dc0499b09f6d97cabb0da0fe3faa580aa2d04a96066d03d81d230ff1877` for both):

- `file_column_tokens()` (`:361`) harvests **every backticked token in column 2 only** — the "File"
  column — of every table row inside the `## Coverage map` section (`COVERAGE_HEADING_RE` `:153`;
  the next `## ` heading ends the section, `:377-379`). `cells = line.split("|")` (`:382`),
  `file_cell = cells[2]` (`:385`). Fenced regions are opaque (`fenced_lines` `:325`, applied `:410`).
- Each harvested token is brace-expanded and matched against the **tracked** set (`expand_pattern`
  `:250-258`; `covered |= hits` `:432`): `covered` is "the paths some File-column pattern denotes".
- `unindexed` = tracked `corpus/` files other than `corpus/README.md` that `covered` misses
  (`:443-444`): `unindexed_names = [t for t in tracked if t != INDEX_NAME and t not in covered]`.
  `tracked` comes from `git ls-files corpus/` (`tracked_corpus_files` `:557`), so an **untracked**
  new corpus file is invisible to the check; an index row naming a file that is not yet tracked is
  a `stale_patterns` finding instead (`:434`) and a `missing_paths` finding if the file is absent
  on disk (`:437-441`).
- `missing_paths` resolves the token **relative to `corpus/`**, so the File cell must hold the
  corpus-relative path (`knowledge/scoped-rules-round60.md`), never a repo-relative one.
- Verdicts: `zero` ids are baseline-free and always adjudicated (`evaluate` `:664-681`), so
  `unindexed`, `stale_patterns`, `missing_paths`, `report_dead`, `commit_unresolvable`,
  `commit_nonhash` cannot be silenced by editing the baseline. Only the three `equal` ids
  (`tracked_files`, `report_total`, `commit_total`) move by a re-record.

## 2. How earlier entries/lessons were indexed

The coverage map in `corpus/README.md` gets one row per new corpus file, and every closure-authored
spot-check carries a row in the **following** round (grep of `corpus/README.md` at the freeze):

| row | README line | wording of the tail |
|---|---|---|
| Round-54 spot-check | `:86` | "landed without an index row, indexed round 55" |
| Round-55 spot-check | `:89` | "…indexed round 56" |
| Round-56 spot-check | `:92` | "…indexed round 57" |
| Round-57 spot-check | `:95` | "…indexed round 58" |
| Round-58 spot-check | `:98` | "landed at `a975cbbf` without an index row …, indexed round 59" |
| Round-59 spot-check | **absent** | **this is the drift**: `corpus.index.unindexed observed=1` |

`LOG.md` records the same practice — round 58's entry (`:2512`): "Corpus index: rows for
`lessons/round-58-verifier-spotcheck.md` (unindexed at base), the hook entry and the round-59 lesson
(`corpus/README.md`)." The harm is named in the rows themselves and is lesson M21 (round 47).
`CORPUS.md:46-48` states the governing rule: "An index row is a claim. Write the row when the file
exists, not before."

## 3. Delivered patch

`/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-60/build/ExecIndexCorpus.patch`
(sha256 `0d42a1839dfe29171403c4a7f062f36605603426ef97aa9f7c50b1c0f4806575`; 14 lines;
`corpus/README.md` only, three rows inserted after `| Round-59 lessons | … |` (base line 100) and
before the blank line that precedes `## Frontier`):

```
+| Round-59 non-author spot-check (closure) | `lessons/round-59-verifier-spotcheck.md` | written by the hyaku closure, not the lane (outside review; never edited here): round 59 admitted, C1 verified (`6 of 6; found 6 of 6; new ground 6`); routed defects R1–R4 (round 60 works them in `lessons/round-60.md`); landed at `31092dc` without an index row (which turned `verify_corpus_integrity.py` red at that base: `unindexed 1`), indexed round 60 |
+| Scoped rule files by client (round 60) | `knowledge/scoped-rules-round60.md` | seven clients' own docs (S103–S109) on the folder each names for a rule file that applies only to matching files, the frontmatter key that scopes it and what an author does with it — `.claude/rules/` (`paths`), `.github/instructions/**/*.instructions.md` (`applyTo`), `.cursor/rules` (`globs`); Codex, Gemini CLI and opencode not eligible (their rule files are directory-scoped and no glob key scopes them); `SKILL.md` § Scoped rule files by client; `../verifiers/check_scoped_rules.py --rev <rev> --fetch` |
+| Round-60 lessons | `lessons/round-60.md` | `## Gate` S103–S111 with access records and the rejections (S110–S111 are the R4 correction rows for S096's anchor and S097's `teaches` wording); `## Mistakes` M86 onward; the round-59 routed defects R1–R4 |
```

Row-content provenance (every cell checked against a committed file, not a description):

- Round-59 spot-check row — the file is closure-authored ("written by the hyaku closure, not the
  lane", header `corpus/lessons/round-59-verifier-spotcheck.md:1-12`); the verdict line
  (`:218-220`) reads "status **ok**. C1 is verified … `6 of 6; found 6 of 6; new ground 6`, exit 0 …
  **admitted: true**"; the routed defects are R1–R4 (`§ 7`, `:193-209`); the landing revision is the
  commit that added the file — `git log --diff-filter=A --format='%H %s' -- corpus/lessons/round-59-verifier-spotcheck.md`
  → `31092dc6f875370bddd6eb1e4da4ca0d210c56af round-59 verifier spot-check (integrator, hyaku): non-author admit/reject`.
  The "red at that base: `unindexed 1`" clause is measured, not asserted: at `31092dc` the gate
  reads `unindexed 1` naming exactly `corpus/lessons/round-59-verifier-spotcheck.md` (§4).
- Entry row — the sources are the round-60 census (`plans/round-60.md` § Census, freeze record):
  eligible Claude Code (`.claude/rules/`, key `paths`), VS Code
  (`.github/instructions/**/*.instructions.md`, key `applyTo`), Copilot CLI (same token, key
  `applyTo`), Cursor (`.cursor/rules`, key `globs`); not eligible Codex, Gemini CLI and opencode
  (directory-scoped files, no glob key). The counter named in the tail exists at the freeze
  (`verifiers/check_scoped_rules.py`, sha256 `ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a`,
  `TARGET = 3` at `:249`) and the SKILL section name is the plan's own
  (`### Scoped rule files by client`, `plans/round-60.md` § C1).
- Lesson row — S103–S109 are the round-60 source ids; S110 and S111 are the R4 correction rows
  (S096 anchor label, S097 `teaches` wording), per `plans/round-60.md:17` § Routed defects R4 and
  the seat briefs that name the ids (`.ufo/waves/round-60/build-spec.json` items `ScribeR4S096`
  "draft correction row S110 (`supersedes S096 —` …)" and `ScribeR4S097` "draft correction row S111
  (`supersedes S097 —`)"); M86 is the next free mistake id (the round-59 lesson's last is M85:
  `grep -o "M[0-9]\+" corpus/lessons/round-59.md | sort -u | tail -3` → `M83 M84 M85`).

The File cells are in the corpus-relative form the reader resolves against `corpus/` (§1). The
client paths, the scope keys, the SKILL section name and the counter command sit in the **Basis**
cell, which the INDEX reader never harvests (`cells[2]` only) — so `.github/instructions/**/*.instructions.md`
cannot become a stale or missing finding.

Application check against the lane as it stands (read-only; `git apply --check` writes nothing):

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin && git apply --check --verbose .ufo/waves/round-60/build/ExecIndexCorpus.patch
Checking patch corpus/README.md...
exit 0
```

The lane's `corpus/README.md` is byte-identical to the freeze's (`git show b1cd64b:corpus/README.md | sha256sum`
= `sha256sum corpus/README.md` = `259cf31d81bb9c52768dcdb33b57f6a7a6bc8b3ac97a6a264e1e0b036e430750`), and
`git log b1cd64b..HEAD -- corpus/README.md` is empty, so the patch applies as the lane stands —
unless another seat lands the same rows first (see §7).

## 4. Gate before → after (measured, not asserted)

Sandbox `/fast/scratch/hyaku/kotoba-r60/{beforeC,afterC}` = clean clones at
`b1cd64bb45eee744c4ec93be8631f1eddb28fddd`; two stub corpus files created there (never in the lane)
and `git add`ed so `git ls-files` counts them, as the real landing will.

before (pristine `beforeC`):

```
$ python3 -B verifiers/verify_corpus_integrity.py     # exit=1
corpus.index    tracked=97 unindexed=1 stale=0 missing=0  (114 FILE-column patterns over 96 md files)
DRIFT   corpus.index.tracked_files: observed=97 expected=81
DRIFT   corpus.index.unindexed: observed=1 expected=0 / empty
DRIFT   corpus.pointers.report_total: observed=66 expected=51
DRIFT   corpus.pointers.commit_total: observed=33 expected=32
DRIFT   corpus.pointers.commit_unresolvable: observed=1 expected=0 / empty
4/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.index.unindexed, corpus.pointers.report_total, corpus.pointers.commit_total, corpus.pointers.commit_unresolvable
           unindexed: corpus/lessons/round-59-verifier-spotcheck.md
           commit_unresolvable: corpus/lessons/round-54-verifier-spotcheck.md:147: 451a02ff
```

after the three rows + the two stub files (`afterC`):

```
$ python3 -B verifiers/verify_corpus_integrity.py     # exit=1
corpus.index    tracked=99 unindexed=0 stale=0 missing=0  (117 FILE-column patterns over 98 md files)
DRIFT   corpus.index.tracked_files: observed=99 expected=81
DRIFT   corpus.pointers.report_total: observed=66 expected=51
DRIFT   corpus.pointers.commit_total: observed=33 expected=32
DRIFT   corpus.pointers.commit_unresolvable: observed=1 expected=0 / empty
5/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.pointers.report_total, corpus.pointers.commit_total, corpus.pointers.commit_unresolvable
```

**The assigned drift is closed**: `corpus.index.unindexed` 1 → 0, and `corpus.index.stale_patterns`
and `corpus.index.missing_paths` stay 0. `index_patterns` and `index_tokens_total` move 114 → 117
(one new File-column pattern per row). `report_total` (66) and `commit_total` (33) are **unchanged
by the rows** — no `.ufo/reports/` pointer and no ``commit `hex` `` citation in any of the three
Basis cells, which was checked deliberately because those two are `equal` pins.

Both corpus instruments agree, and the finding-delta instrument confirms no new finding and one
resolved (`verifiers/check_gate_finding_delta.py`, run over committed trees so the archived README
is the patched one):

```
$ python3 -B verifiers/verify_corpus_independent.py     # afterC
index   tracked_files=99 index_tokens=117 (outside coverage map=18) unindexed=0 stale=0 missing=0
points  candidates=76 checked=66 excluded=8 quoted=2 dead=0 shapes={'absolute': 42, 'tilde': 1, 'relative': 1, 'bare': 22}
commits candidates=38 citations=33 hex=33 quoted=5 nonhash=0 unresolvable=1

$ python3 -B verifiers/check_gate_finding_delta.py --repo . --base b1cd64b… --head HEAD --gate verifiers/verify_corpus_integrity.py --json
base drift 5 / head drift 4 — new: []  resolved: ["corpus.index.unindexed"]
finding delta: new 0, resolved 1     (exit 0)
```

(`verify_corpus_integrity.py --self-test` → `self-test: 0 failure(s) over 152 assertions`, exit 0 —
unchanged by this patch, which touches only a Markdown file.)

**Re-measured against the files that actually landed.** While this seat worked, the two new corpus
files were written in the lane by their own seats (`corpus/knowledge/scoped-rules-round60.md`,
7757 B; `corpus/lessons/round-60.md`, 7186 B; both still untracked at lane HEAD, and `corpus/SOURCES.md`
gained rows S103–S111). The measurement was repeated in a clean sandbox (`finalC`) with the patch
applied and **those real files** staged instead of stubs:

```
$ python3 -B verifiers/verify_corpus_integrity.py     # exit=1
corpus.index    tracked=99 unindexed=0 stale=0 missing=0  (117 FILE-column patterns over 98 md files)
corpus.pointers report_dead=0/66 commit_total=33 unresolvable=1 nonhash=0
DRIFT   corpus.index.tracked_files: observed=99 expected=81
DRIFT   corpus.pointers.report_total: observed=66 expected=51
DRIFT   corpus.pointers.commit_total: observed=33 expected=32
DRIFT   corpus.pointers.commit_unresolvable: observed=1 expected=0 / empty
5/9 checks pass

$ python3 -B verifiers/check_gate_finding_delta.py --repo . --base b1cd64b… --head HEAD --gate verifiers/verify_corpus_integrity.py --json
new []   resolved ["corpus.index.unindexed"]
```

Same numbers as with the stubs: the real files add no report pointer and no commit citation
(`report_total` 66 and `commit_total` 33 unchanged), so §5's pin table holds for the real landing
as well as for the stubbed one. The landed entry's `source:` line reads "S103–S109; S103, S106 and
S108 re-open round-53 rows S043, S048 and S049", its table header is `| Client | Rule files | Source | Quote |`
and its four rows carry exactly the tokens and scope keys the entry row names (`.claude/rules/` with
`paths`, `.github/instructions/**/*.instructions.md` with `applyTo`, `.cursor/rules` with `globs`);
its § Directory-scoped negatives covers Codex (S104), Gemini CLI (S107) and opencode (S109) as the
row states. The landed lesson's `## Gate` lists S103–S111 (S110 = S096 anchor correction,
S111 = S097 `teaches` correction) and its `## Mistakes` section is reserved for M86 onward, so both
Basis cells match the landed prose.

## 5. The other four DRIFTs are inherited, and only two of them are the baseline's fault

`verifiers/corpus-baseline.json` pins `tracked_files 81` / `report_total 51` / `commit_total 32`,
recorded at round 54 (`notes.round54_rerecord`: "tracked_files 78 -> 81 … report_total 49 -> 51").
At the round-60 base the pins are already stale by the rounds 55–59 landings: observed 97 / 66 / 33.
The round-59 spot-check's own note agrees — `corpus/lessons/round-59-verifier-spotcheck.md:139-140`
records "Corpus integrity DRIFT 5 → 4 (`receipts/`, `C1-remeasure-tip.txt`; the remaining
`commit_unresolvable 1` is present at base)". So the same four ids were the round-59 tip's own
DRIFT set, and the round-60 base carries them forward unchanged.

**Command that does the re-record** (the baseline's own `measured_against.command`):

```
python3 -B verifiers/verify_corpus_integrity.py --no-baseline --json
```

then copy the observed values of the three `equal` ids into `checks.<id>.expect` and add a
`notes.round60_*` sentence naming what moved and why (round-54 form). Re-recording is not "fit the
denominator" here: the pins have been stale since round 54, and this item's own rows add **no**
pointer and **no** citation, so for this item's work only `tracked_files` moves.

Expected pin set at the round-60 landing (measured with the stubs; re-measure for the real files,
which may add pointers/citations of their own):

| id | old pin | pin to write | why |
|---|---|---|---|
| `corpus.index.tracked_files` | 81 | **99** | 97 observed at base + the two new corpus files this item indexes (`knowledge/scoped-rules-round60.md`, `lessons/round-60.md`); the round-59 spot-check was already tracked. Any further corpus file this round adds 1 each |
| `corpus.pointers.report_total` | 51 | **66** | drifted by rounds 55–59; unchanged by my rows |
| `corpus.pointers.commit_total` | 32 | **32** if §6's repair is taken, else **33** | the repair moves one citation from the counted set to the quoted-excluded set |
| the six `zero` ids | 0 | 0 | baseline-independent; measured 0 after the repair |

## 6. Blocker the re-record cannot clear: `commit_unresolvable` (zero-mode)

`corpus/lessons/round-54-verifier-spotcheck.md:146-147` reports on a citation shape and instantiates it:

```
`` commit `451a02ff` `` grammar in the new entry
```

`COMMIT_RE` (`:149`) matches ``commit `451a02ff` `` there, the token is 8 hex chars, and
`inside_quotes` is false (the span is in backticks, not double quotes), so it counts as a promise.
It does not resolve in this repo — it is an upstream gemini-cli hash:

```
$ git cat-file -e 451a02ff^{commit}; echo $?
fatal: Not a valid object name 451a02ff^{commit}
128
```

`corpus.pointers.commit_unresolvable` is `zero` mode, so `evaluate()` (`:670-672`) adjudicates it
with no baseline: **no re-record can clear it** and the gate keeps exiting 1 at the landed tree.

Smallest repair consistent with the counter's own documented idiom (a document *reporting on* a
citation is a "quoted meta-finding", moved to `commit_quoted_detail`, docstring `:60-61`, applied at
`:498`) — insert two double quotes:

```diff
--- a/corpus/lessons/round-54-verifier-spotcheck.md
+++ b/corpus/lessons/round-54-verifier-spotcheck.md
@@ -145,5 +145,5 @@
 No axis is harmed. The `commit_unresolvable` 0→1 that `W2CriticNoHarm` found at `58db81c4` (the
-`` commit `451a02ff` `` grammar in the new entry) was fixed in `cae8f2ea`. At the tip the entry reads
+"`` commit `451a02ff` ``" grammar in the new entry) was fixed in `cae8f2ea`. At the tip the entry reads
 `google-gemini/gemini-cli@451a02ff`.
```

Measured on a sandbox tree with that repair **and** the §5 re-record (`simA`):

```
$ python3 -B verifiers/verify_corpus_integrity.py     # exit=0
corpus.index    tracked=99 unindexed=0 stale=0 missing=0  (117 FILE-column patterns over 98 md files)
corpus.pointers report_dead=0/66 commit_total=32 unresolvable=0 nonhash=0 (shapes [relative=1, absolute=42,
                tilde=1, bare=22], quoted-excluded=6, pointer-excluded=8)
9/9 checks pass
$ python3 -B verifiers/verify_corpus_independent.py     # exit=0
index   tracked_files=99 index_tokens=117 unindexed=0 stale=0 missing=0
points  candidates=76 checked=66 excluded=8 quoted=2 dead=0
commits candidates=38 citations=32 hex=32 quoted=6 nonhash=0 unresolvable=0
```

Note the interaction the L1 must not miss: **the repair drops `commit_total` from 33 to 32**
(the citation moves to the quoted-excluded set), so §5's pin for `commit_total` is 32 only when the
repair is taken. Measured: with the repair but the `commit_total` pin left at 33, the gate reads
`DRIFT corpus.pointers.commit_total: observed=32 expected=33` and `8/9 checks pass`; with the pin
corrected to 32 it reads `9/9 checks pass`, exit 0.

Two consequences for the L1: (a) the repair edits an outside-authored spot-check, so it needs the
one-line record the lane uses for that (a LOG entry or the round-60 lesson's corrections section) —
that file's own header says "never edited here"; (b) if the L1 declines the edit, then
`commit_total` re-records to **33** and the gate must be recorded as red on
`corpus.pointers.commit_unresolvable` with this file named as the cause. An alternative prose
rewrite ("a bare commit-plus-hex citation in the new entry") removes the token the same way;
[INFERENCE] it clears the same test, since no ``commit `hex` `` span remains — not measured.

## 7. Ordering constraint (the rows and the files must land in one commit)

Measured in two sibling sandboxes at the freeze rev:

- **Files tracked, rows absent** (`ordA`): `tracked_files=99, unindexed=3`
  (`knowledge/scoped-rules-round60.md`, `lessons/round-59-verifier-spotcheck.md`, `lessons/round-60.md`),
  `stale=0` — the `unindexed` drift this item closes.
- **Rows present, files absent** (`ordB`, patch applied): `tracked_files=97, unindexed=0` but
  `stale_patterns=2` (`corpus/README.md:102: knowledge/scoped-rules-round60.md`,
  `corpus/README.md:103: lessons/round-60.md`) and `missing_paths=2` (the same two tokens) — two
  `zero` DRIFTs, worse than the single one it replaces.

So the L1 must land the two new corpus files **and** the three rows in the same commit (or land the
files first and the rows in the same commit that adds them), as the round-58 and round-59 landings
did.

## 8. Boundaries honoured

Nothing in the lane was written, staged, committed or checked out: every run above happened in
`/fast/scratch/hyaku/kotoba-r60/{ExecIndexCorpus,base,beforeC,afterC,ordA,ordB,simA,at31092,deltaC}`;
lane git use was `git --no-optional-locks log/diff/status/ls-files`, `git apply --check` (writes
nothing, exit 0, reported in §3), plus reads. No jj commands. No package installs or upgrades this
item (nothing needed). No model/CLI calls, no `ask`, no `model` parameter.

Files I wrote in the lane: this report and `.ufo/waves/round-60/build/ExecIndexCorpus.patch`,
nothing else. The two stub corpus files exist only in the sandbox clones.

## 9. Risks for the integrator

1. **Duplicate rows.** If a scribe seat also drafts a coverage row for
   `knowledge/scoped-rules-round60.md` or `lessons/round-60.md`, take exactly one set — applying
   the patch twice duplicates three table rows (the counter would still pass: duplicate rows are
   harmless to `covered`, but the README would be wrong).
2. **Row wording vs. what actually lands.** The entry row claims the census's eligible tokens and
   the three negative clients; the lesson row claims S103–S111, M86 onward and R1–R4. If a seat
   opens a different source id, or the L1 records the C1 counter result in the row (the round-57
   entry row precedent carries "(C1 missed: `4 of 4; new ground 4`)"), amend those two Basis cells
   accordingly.
3. **The pins are stale by four rounds.** A reader who sees "4 DRIFT at base" should not read it as
   damage from round 60; §5's table separates the inherited drift from this item's one-file move.
4. **The gate will not be green from the patch alone.** §5's re-record and §6's citation repair
   are both required; the patch is the index half only, by design (the index row is a claim about a
   file, and the files land with it).
5. **The lane moved under this seat.** When this seat finished, the lane working tree held the two
   new corpus files (untracked) and a modified `corpus/SOURCES.md` (rows S103–S111) from other
   seats. The patch's context lines still apply (`git apply --check` → exit 0 at 09:22Z), because
   those seats changed `corpus/SOURCES.md` and added new files, not `corpus/README.md`. If a
   different seat adds coverage rows for the same two files before the L1 applies this patch,
   take one set, not two (§9.1).

## 10. Evidence paths

```
$ ls -l /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-60/build/ExecIndexCorpus.patch \
        /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-60/build/ExecIndexCorpus.md
-rw-r--r-- 1 vgpnk vgpnk 2680 Oct 23 09:22 .ufo/waves/round-60/build/ExecIndexCorpus.patch
-rw-r--r-- 1 vgpnk vgpnk  <size> Oct 23 <time> .ufo/waves/round-60/build/ExecIndexCorpus.md
$ sha256sum .ufo/waves/round-60/build/ExecIndexCorpus.patch
0d42a1839dfe29171403c4a7f062f36605603426ef97aa9f7c50b1c0f4806575  .ufo/waves/round-60/build/ExecIndexCorpus.patch
```

(The `.md` size above was taken before this block was written into it, so a fresh `ls -l` shows
this file larger; the `.patch` is final — its hash is re-checked after every write.)

Sandboxes (all mine, nothing of the lane): `/fast/scratch/hyaku/kotoba-r60/ExecIndexCorpus` (rows +
stubs), `.../base` and `.../beforeC` (pristine `b1cd64b`, before-state), `.../afterC` and
`.../deltaC` (rows + stubs), `.../finalC` (rows + the **real** landed corpus files), `.../ordA`
(files, no rows), `.../ordB` (rows, no files), `.../simA` (rows + stubs + re-recorded pins + the §6
repair), `.../at31092` (pristine `31092dc`).
Sandbox commits: `sandbox 8948755` (/fast/scratch/hyaku/kotoba-r60/afterC),
`sandbox 863e6a9` (/fast/scratch/hyaku/kotoba-r60/deltaC) and the `finalC` commit (rows + the real
landed files) — the latter two are the trees the finding-delta measurements in §4 used.
