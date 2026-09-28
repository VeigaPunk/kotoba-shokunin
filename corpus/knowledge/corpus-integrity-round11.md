# Corpus integrity, executable — round 11

Sourced 2026-09-28 (round 11). This file is the human-readable half of
`verifiers/verify_corpus_integrity.py`; the script is the authority. Every number
below was printed by the command next to it — at the instant it was measured. The
landing note at the end recites the seven values that moved when the round-11
files landed, with the commands that re-derive them at the landed tree; the four
zero-claims (`report_dead`, `commit_nonhash`, `commit_unresolvable`, and the index
zeros) hold at both trees.

Before-state = committed `HEAD` (`d49dfa5`), reproduced by cloning it — an
uncommitted fix reads as "agree" to any check that reads the working tree, so
every before-number comes from a clone, never from `git show` text alone.

```bash
git clone -q --no-hardlinks . /tmp/before-clone
cd /tmp/before-clone && git rev-parse --short HEAD          # → d49dfa5
```

## Trigger — three zeros, two counting commands that could not count

Round 10's consistency row claimed three zeros (non-hash commit pointers 0,
unindexed corpus files 0, unresolved report pointers 0) and carried a command for
each. Two of those commands could not express the class they named. A claim whose
counting command cannot express its own scope is calibration debt **even when the
number is right** — the number stops being re-derivable the moment a defect
reappears.

## Defect 1 — a single-digit-blind pattern reporting a false zero

The row's pointer command searched for a backticked `commit` citation whose token
matched the class `round-[0-9]`. The literal pipeline is written here with the
backtick in a variable, because pasting the raw citation form would make this file
itself a `corpus.pointers.commit_nonhash` finding:

```bash
B='`'
git show HEAD:corpus/README.md | grep -cE "commit ${B}round-[0-9]${B}"    # → 0  (defect present at :38)
git show HEAD:corpus/README.md | grep -cE "commit ${B}round-[0-9]+${B}"   # → 1  (corpus/README.md:38)
git show HEAD:corpus/README.md | sed -n '38p' | cut -c30-80              # → token "round-10", not a hash
```

`[0-9]` matches exactly one digit, so the pattern cannot match `round-10` — the
only two-digit round in the corpus. With the defect present the command prints 0,
i.e. the row's "→ 0 (was 8)" could not have distinguished "fixed" from "never
seen". The two backticks are the same U+0060 character (checked by codepoint, not
by eye): the defect is arity, not quoting.

After the fix, both scopes are empty:

```bash
B='`'
grep -rn --include='*.md' -E "commit ${B}round-[0-9]+${B}" .        # → (no output)
git ls-files '*.md' | xargs grep -nE "commit ${B}round-[0-9]+${B}"  # → (no output)
```

## Defect 2 — an index command blind to a brace row

The row's index-coverage command, exactly as printed in `SCORECARD.md`, does not
measure anything: lifted from the markdown table its escaped pipes (`\|`) make the
left-hand grep match nothing, so `comm` reports every tracked file as unindexed
while exiting 0.

```bash
# as-printed (escaped pipes), abridged:
comm -13 <(grep -oE '(knowledge\|lessons)/[A-Za-z0-9._-]+\.md' corpus/README.md | sort -u) \
         <(git ls-files corpus/ | sed 's|^corpus/||' | sort -u) | wc -l
# → 33   (every tracked corpus file, i.e. the regex tokenized no index row at all)
```

With real pipes it runs and lists four entries — three of them index-covered:

```bash
comm -13 <(grep -oE '(knowledge|lessons)/[A-Za-z0-9._-]+\.md' corpus/README.md | sort -u) \
         <(git ls-files corpus/ | sed 's|^corpus/||' | sort -u)
# → lessons/round-1-aggregator-audit.md
# → lessons/round-4-aggregator-audit.md
# → lessons/round-5-aggregator-audit.md
# → README.md
```

`lessons/round-{1,4,5}-aggregator-audit.md` **has** an index row — the brace row at
`corpus/README.md:30` — but `[A-Za-z0-9._-]+` cannot tokenize a brace span, so the
command reports three covered files as uncovered. The true count, under
brace/glob-aware matching, is 0 unindexed with the index's own `README.md`
excluded:

```bash
git ls-files corpus/ | wc -l                    # → 36 tracked corpus files (33 before the round-11 files landed)
python3 verifiers/verify_corpus_integrity.py --json | \
  python3 -c 'import json,sys;o=json.load(sys.stdin)["observed"]["corpus"];print(o["index_patterns"], o["unindexed"], o["stale_patterns"], o["missing_paths"])'
# → 37 0 0 0   (32 0 0 0 at the before-state: the round-11 rows add five FILE-column tokens)
```

`L1` also reported this command emitting `comm: file 1 is not in sorted order`.
`[UNVERIFIED]` as a property of the command: it was observed once on this host
under `/tmp` disk-quota pressure (`sort: write failed: … Disk quota exceeded`,
leaving a truncated file), and five deliberate collation variants (as printed,
real pipes, `LC_ALL=C`, mixed-collation `sort`/`comm` pairs, unsorted file 1) all
exit 0 with empty stderr. The reproducible defect is the brace row.

## Defect 3 — dead report pointers inside a four-form class

Report pointers in `corpus/*.md` appear in four shapes, and only one form was
broken:

```bash
git grep -h -o -E '[^ `]*\.ufo/reports/round-[0-9]+/[^ `]*' HEAD -- 'corpus/*.md' \
  | sed 's|\(.*\)\.ufo/reports/.*|\1.ufo/reports/|' | sort | uniq -c
# HEAD →  9 ../.ufo/reports/   3 .ufo/reports/   8 /home/vgpnk/projects/shokunin/.ufo/reports/   1 ~/projects/shokunin/.ufo/reports/
```

That loose class counts 21 tokens at HEAD; the verifier's tighter class (the tail
must be a `.md` with no space or backtick) checks 19 of them — the difference is
one directory token (`.ufo/reports/round-1/`) and one placeholder
(`.ufo/reports/round-1/<lane>.md`), both excluded by design.

- 9 × `../.ufo/reports/round-N/kotoba.md`, all in `corpus/README.md`: from
  `corpus/`, `../.ufo` is `<repo>/.ufo`, which does not exist → **dead**.
- 1 × bare top-level form (report under `.ufo/` with no `../` hops) in
  `corpus/lessons/round-3.md`: also resolved from the citing directory, also dead.
- 8 × host-absolute and 1 × `~`-anchored: all resolving.

Fixed by moving every report pointer to the form the corpus already used for 10 of
them (host-absolute; the round-root of these reports is named, per the
citation-base rule), so the check can assert resolution from the citing file's own
directory for every shape:

```bash
cd corpus && for n in 1 3 4 5 6 7 8 9 10; do
  printf "round-%s %s\n" "$n" "$(test -f /home/vgpnk/projects/shokunin/.ufo/reports/round-$n/kotoba.md && echo OK || echo DEAD)"; done
# → OK ×9
```

The counting trap that hides this class: a `../.ufo` substring pattern also counts
a `../../.ufo` line, so `grep -c '\.\./\.ufo/reports/round-' corpus/README.md`
printed **9 before and 9 after** the repair (measured while the rows briefly held
the `../../.ufo` intermediate form). Only per-citing-directory resolution
separates the two states. At the landed tree the same command prints `0` — every
README row is host-absolute now, which is why the check's *shape* counters
(`report_pointer_shapes`) and not a substring `grep` are the readable surface.

## The verifier — 9 checks, 4 exit codes

`verifiers/verify_corpus_integrity.py` + `verifiers/corpus-baseline.json`.

| Check id | Agrees when | Before → after |
|---|---|---|
| `corpus.index.tracked_files` | tracked-corpus census matches the baseline | 33 → 36 |
| `corpus.index.unindexed` | every tracked corpus file has an index row under brace/glob expansion (self-reference excluded) | 0 → 0 |
| `corpus.index.stale_patterns` | no index row names a corpus file that does not exist | 0 → 0 |
| `corpus.index.missing_paths` | every FILE-column path (incl. `../verifiers/*`) exists | 0 → 0 |
| `corpus.pointers.report_total` | checked pointer count matches the baseline | 19 → 24 |
| `corpus.pointers.report_dead` | every checked pointer resolves from its citing file's directory | **10 → 0** |
| `corpus.pointers.commit_total` | hex `commit`-citation count matches the baseline | 18 → 22 |
| `corpus.pointers.commit_unresolvable` | every cited hex resolves as a commit in this repo | 0 → 0 |
| `corpus.pointers.commit_nonhash` | no live `commit` citation carries a non-hash token | **1 → 0** |

Exits: 0 all agree · 1 drift (names the firing ids) · 2 environment unreadable
(not a git repo / no corpus) · 3 no baseline. `--json` prints
`{"observed", "results"}`; `--self-test` falsifies the matcher model (brace
expansion, brace+glob coverage, pointer shapes, exclusion shapes, quoted
citations, hash classification) on fixtures.

Red-before / green-after, one command each:

```bash
python3 verifiers/verify_corpus_integrity.py --repo /tmp/before-clone --no-baseline ; echo "exit=$?"
# corpus.index    tracked=33 unindexed=0 stale=0 missing=0  (32 FILE-column patterns over 33 md files)
# corpus.pointers report_dead=10/19 commit_total=18 unresolvable=0 nonhash=1
#                 (shapes [relative=9, absolute=8, tilde=1, bare=1], quoted-excluded=1, pointer-excluded=1)
# 7/9 checks pass; DRIFT: corpus.pointers.report_dead, corpus.pointers.commit_nonhash
# exit=1
python3 verifiers/verify_corpus_integrity.py ; echo "exit=$?"
# corpus.pointers report_dead=0/24 commit_total=22 unresolvable=0 nonhash=0
#                 (shapes [relative=0, absolute=23, tilde=1, bare=0], quoted-excluded=1, pointer-excluded=8)
# 9/9 checks pass
# exit=0
```

The green-after block above is the landed tree (33 → 36 tracked files, 19 → 24
checked pointers, 21 → 22 commit citations; the `19`/`21`/`1` values in the
before-block are the clone's).

Exit codes probed, not asserted: perturbed baseline (`commit_total` expect 22 → 18)
→ exit 1 naming exactly that id; `--repo /tmp/notgit` → exit 2; baseline removed
→ exit 3.

**A synthetic tree lies about resolvability.** `git archive HEAD | tar -x` +
`git init && git add -A && git commit` in a fresh directory produces a repository
with no history for the cited hashes: `commit_unresolvable=18` and a third
spurious DRIFT. Used as the before-state, it would report a defect that does not
exist. Red-before runs need a clone (or a worktree); the synthetic tree is valid
only for path/index checks.

## Falsification — planted faults and equivalent mutants

Ten faults planted in throwaway clones (`FaultInjection` lane, non-author): a
deleted index target, an unindexed tracked file, a report pointer to a
non-existent round, a plausible-but-absent commit hash, a non-hash commit token,
a deleted report target, a renamed baseline, a non-git directory, a broken brace
row, and a blanked FILE-column token. **All ten surfaced** — 7 by the intended
zero-check, 2 by the exit-2/exit-3 guards, 1 mode-masked (`--no-baseline`
suppresses the `equal` comparison by design). No zero-check was decoration: each
spoke when its fault class was planted.

Four equivalent mutants were identified, i.e. changes the checker *should* treat
identically: an untracked file ≡ an absent file; a fully-quoted commit citation ≡
no citation; a pointer-shape-only rewrite ≡ no-op; a `<lane>` placeholder ≡ no
pointer. Each has a named reason, not a tolerance.

## Excluded shapes — what the pointer check must *not* report

| Shape | Carrier | Handled by |
|---|---|---|
| illustrative prose (`../sibling/SKILL.md`, `../bailian-protocol/…`) | `corpus/knowledge/fail-closed-and-anti-patterns.md` | outside the `.ufo/reports/round-N/*.md` class |
| quoted meta-finding (`../godspeed-core/directive.md`) | `corpus/knowledge/agent-def-audit-round6.md:77` | idem |
| placeholder pointer (`.ufo/reports/round-1/<lane>.md`) | `corpus/knowledge/dispatch-prompt-audit-round7.md:42` and six more sites in the round-11 records | `is_excluded_pointer` (`<`/`>` marker) → counted as `report_pointers_excluded` (8 at the landed tree, 1 at the before-state) |
| quoted `commit` citation, non-hash token | `corpus/lessons/round-6-aggregator-audit.md:45` | `inside_quotes` → `commit_quoted` context |
| quoted *report pointer* (a reported-absent path) | any corpus file that names an ABSENT path | `inside_quotes` → `report_pointers_quoted` context — **only after the round-12 repair**; before it the tokenizer swallowed the opening quote, so the match began at `"` and the rule could never fire (proof in `corpus/knowledge/cold-run-round11.md` §7) |
| ellipsis-mimicking-`../` (`corpus/.../.ufo/…`) | schematic prose | `is_excluded_pointer` (segment containing `..`) |
| glob spans, code literals, deliberate dead-path drift lists | `SKILL.md` (never scanned: outside `corpus/`) | scope |

Report pointers and commit citations are only checked inside **tracked
`corpus/*.md`**. `LOG.md`, `SCORECARD.md` and `SKILL.md` carry the same forms and
are not asserted — a named gap, not an oversight: the corpus is this lane's
artifact surface.

## A check that was designed and rejected

Revision pins of the form `` `SKILL.md` @ `143fe473…` `` were proposed for
checking (`@ <hex>` must resolve as a git object). Rejected: the token is an
**md5**, not a commit — `md5sum` of `SKILL.md` at `3b029b8` is exactly
`143fe473368ec9e2bbadde…` truncated to 8 bytes (`git show 3b029b8:SKILL.md |
md5sum` → `143fe473368ec9e2bb7adde9d0425b1c`, 487 lines). A resolvability check
without a label classifier would fail a correct digest, and a label classifier is
a second convention with no fixture. The two misleading sites were **relabelled**
instead (`@ md5 143fe473… (commit 3b029b8)`), which is the repair the defect
actually needed.

## Open gaps

- **Scope is `git ls-files`.** An untracked corpus file is invisible to both index
  checks (it is neither an unindexed tracked file nor a target of a stale
  pattern), and so is a pointer from an untracked file. Planted-fault run: "add a
  new corpus file, `git add` it" → `corpus.index.unindexed` fires; "add it and do
  not stage it" → silent. `git status` is the guard; the checker cannot be.
- The checked pointer population is 24, of which 23 are host-absolute. A check
  that asserts resolution is doing real work, but the host-absolute convention is
  machine-local: on another host the whole class fails at once. Repo-relative
  forms would be portable; the corpus has not been normalised to them.
- `corpus.pointers.commit_total` and `corpus.index.tracked_files` are
  change-detectors: they fire when the corpus legitimately grows. The growth
  procedure is manual (re-record `verifiers/corpus-baseline.json` after confirming
  each moved value is explained).
- `SKILL.md`'s 40 checklist boxes (14/9/9/8 by section at round 12 — 39/13/9/9/8 when this file was written; `grep -c '^- \[ \]' SKILL.md`)
  remain lane-attested. This round machine-checked counting, not execution: no
  verifier in this repo runs a single box.
- Report pointers in `LOG.md`/`SCORECARD.md`/`SKILL.md` are unchecked (above).
## Landing note (round 12)

The round-11 landing commit was taken by the round-12 respawn after the round-11
working tree was finished (landed as `4dd7753`): the two reported-absent tokens in
this artifact (the bare pre-fix form above, and the same class in `corpus/README.md`
rows already fixed) were rewritten as prose — a live pointer to an absent path is
exactly what the check must flag.

**Counts that moved at landing** (round-12 census, `/tmp/round12/ScoutClaimCensus/census.md`;
the moved values are stated above, so this table is the audit trail, not a second
set of claims):

| Value | Written as | At the landed tree | Command |
|---|---|---|---|
| tracked corpus files | 33 | **36** | `git ls-files corpus/ \| wc -l` |
| FILE-column tokens | 32 | **37** | `python3 verifiers/verify_corpus_integrity.py --json` → `index_patterns` |
| checked report pointers | 19 | **24** | same → `report_total` |
| `report_pointers_excluded` | 1 | **8** | same → `report_pointers_excluded` |
| `commit_total` (after) | 21 | **22** | same → `commit_total` |
| host-absolute / tilde of checked | 18+1 of 19 | **23+1 of 24** | same → `report_pointer_shapes` |
| `--self-test` assertions | 80 | **88** (86 after the quoted-token repair, +2 for the index-scope pins) | `python3 verifiers/verify_corpus_integrity.py --self-test` |

Cause of every move: the round-11 corpus files landed (three new tracked files,
five new index tokens, four new checked pointers) and the round-12 fill turned the
README's round-11 `landing hash` prose into a `commit` citation. `report_dead`,
`commit_nonhash`, `commit_unresolvable` and the index zeros are unchanged and zero
at both trees.

**One gap this file names and cannot close:** the planted-fault run above has no
re-runnable artifact — its log lived in `/tmp/round11/`, wiped under disk pressure.
The round-12 landing commits a fault harness
(`verifiers/fault_injection_corpus.sh`) so that record class stops depending on
`/tmp`.
