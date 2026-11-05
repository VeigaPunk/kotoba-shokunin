# ScribeCorpus — round 91 w1 (S262, S263, one rejection row; two knowledge entries; the round lesson)

Seat: **ScribeCorpus** (scribe, leaf member — no subagent dispatch).
Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`. Base (the freeze commit):
`9af1a7af2adf0ab07cfd53f92affc1ed8d992262`.

Writes, all lane-side, all named by the item:

| path | what |
|---|---|
| `.ufo/waves/round-91/w1/ScribeCorpus/ScribeCorpus.patch` | the patch (4 files, `--binary`, against the freeze base) |
| `.ufo/waves/round-91/w1/ScribeCorpus/census-after.txt` | census validate + row counts on the applied tree |
| `.ufo/waves/round-91/w1/ScribeCorpus/ground-measurements.txt` | base and ground-clone instrument readings |
| `.ufo/waves/round-91/w1/ScribeCorpus_READY` | the READY file (list of files changed) |
| `.ufo/waves/round-91/w1/ScribeCorpus.md` | this report |

**The lane was not written.** Every corpus file lives in the seat's own scratch clone
(`/fast/scratch/hyaku/kotoba-r91/ScribeCorpus/repo`, a `--shared` clone of the lane at the freeze
base); the patch is the only channel to the lane, and the L1 integrates it. Scratch was removed
before yield. No `git`/`jj` write touched the lane or the fleet root.

## Files in the patch

| file | change |
|---|---|
| `corpus/SOURCES.md` | **append only** — three rows after S261: S262 (PIT/pitest "Basic concepts", `mined`), S263 (Python `subprocess` docs, `mined`), S264 (Wikipedia "Mutation testing", `rejected`). No existing row was touched; the row count went 187 → 190 |
| `corpus/knowledge/mutation-battery-arms-round91.md` | **new** — C1's knowledge entry: the three new guard arms and what each guards, the two-sided rule and why the equivalents stay generated, the bounds |
| `corpus/knowledge/timeout-calibration-round91.md` | **new** — C2 leg A's knowledge entry: the Q39 calibration arithmetic, the MEASURED constant, the bounds |
| `corpus/lessons/round-91.md` | **new** — the round lesson: `## Gate`, `## Mistakes`, `## Considerthese`, `## Sources` |

## The three SOURCES rows

Ids confirmed before writing: `grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md |
grep -oE 'S[0-9]+' | sort -V | tail -1` → **S261**, so S262/S263 are the next two and the rejection
row takes S264. Each row is 13 `|`-delimited fields (the table's 11 columns), contains no `|` inside
any cell and no escaped pipe, and carries `status`/`opened`/`recheck`/`used-by` in the shape the
header declares. S262 and S263 are `mined` with the knowledge files that cite them in `used-by`;
S264 is `rejected` and its `teaches` cell begins `REJECTED: <reason>; flip: <what changes it>`.

The located quotes are copied from the scout's receipt
(`.ufo/waves/round-91/w1/ScoutSources/quote-receipts.txt`, cross-checked in
`.ufo/waves/round-91/w1/ScoutSources/ScoutSources.md`), not re-fetched:

- **S262** — `https://pitest.org/quickstart/basic_concepts`, accessed 2026-11-05. Quote (18 words):
  "not all mutations will behave differently than the unmutated class. These mutants are referred to
  as equivalent mutations." The row's scope names what S262 adds over S260 (the third outcome state
  `No coverage` and the two named grounds of equivalence), so the two rows do not read as duplicates.
- **S263** — `https://docs.python.org/3/library/subprocess.html`, accessed 2026-11-05. Quote (25
  words): "If the timeout expires, the child process will be killed and waited for. The
  TimeoutExpired exception will be re-raised after the child process has terminated." The row is
  scoped to the `run()` contract (the one the lane's `subprocess.run(..., timeout=cap)` call site
  binds) with the `Popen.communicate()` no-kill sentence as the contrast.
- **S264** — `https://en.wikipedia.org/wiki/Mutation_testing`, accessed 2026-11-05, page revision
  1373580212. **Rejected**: crowd-editable tertiary text is a lead, never support, and its own score
  formula counts equivalent mutants in the denominator — the opposite convention from the two-sided
  rule (Q47) C1 rests on. Flip recorded in the row and in the lesson's `## Gate`.

## Commands and observed output

**Census validate (applied tree = base + this patch).**
`bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file corpus/SOURCES.md
--today 2026-11-05` → `file ok <path>`, exit **0**; the only lines emitted are the 33 pre-existing
W04 duplicate-URL warnings (unchanged class) and no E-code. Census counts: `rows 190`, `tier.A 149`,
`tier.B 23`, `tier.C 18`, `status.mined 165`, `status.queued 7`, `status.rejected 18`.

**Plan counting command.** `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`
→ **190** (187 at the base, receipt `.ufo/waves/round-91/receipts/census-before.txt`).

**Patch applies.** Fresh `--shared` clone of the lane at the freeze base →
`git apply --check .ufo/waves/round-91/w1/ScribeCorpus/ScribeCorpus.patch` → OK; applied → `M
corpus/SOURCES.md`, `?? corpus/knowledge/mutation-battery-arms-round91.md`, `?? corpus/knowledge/
timeout-calibration-round91.md`, `?? corpus/lessons/round-91.md` (exactly the four owned files, no
stray path).

**Base instrument readings (scratch clone at the freeze base)** — used to ground the C1 entry:
`python3 -B verifiers/check_mutation_battery.py --self-test` → `0 failure(s) over 19 assertions`,
exit 0; the frozen run at the base rev → `mutation battery killed 14 of 14 kill-set; equivalents
survived 6 of 6; disclosed survivors 0 of 0`, exit 0; the manifest holds 14 kill rows and 6
equivalent rows.

**Ground-candidate readings (base + the three builder patches, scratch clone, scratch identity
`43650d3e249d85a49a168a4f1a04b7d085dac81f`)** — used to ground *both* knowledge entries, never
presented as a landing measurement: `--self-test` → `0 failure(s) over 25 assertions`, exit 0; the
frozen run → `mutation battery killed 17 of 17 kill-set; equivalents survived 6 of 6; disclosed
survivors 0 of 0`, exit 0, with `mb-m2-g1-commit-check-skipped`, `mb-m15-clean-tree-guard-off` and
`mb-m16-restore-unverified` each `killed [bat-self-test exit 0->1]` — i.e. the three new arms are
the kill channel, observed. The tip battery at the ground candidate reads `guards 5 of 5; tip
battery exit 0: 3 of 6` (the `instrument-pin` guard now PASSes at blob
`6f2c52fb2e09e817dff3360b97400a5d6e53626c`).

## Findings (for the L1 / the canonical judge)

1. **The plan's census arithmetic is one short of what the seat item requires.** `plans/round-91.md`
   § Frontier step predicts "Census before→after: 187 → 189 expected". The item requires the
   rejection candidate to be *in the registry table* as a `rejected` row (S264), and the counting
   command counts rejected rows, so the measured after-count is **190**. Both the plan's `189` and
   the item's shape cannot hold at once; the plan is frozen and is not edited here, so the count is
   measured and reported (in the lesson's `## Gate` and above) and the plan's expectation is
   corrected at integration. The census itself is clean (`validate` exit 0, no E-code).
2. **`corpus/README.md` needs the three index rows — that is the L1's touch-list item, not this
   seat's.** `verify_corpus_integrity.py --json` on the applied tree reads
   `corpus.index.unindexed 4` with `unindexed_detail` = the three new corpus files plus the
   pre-existing `corpus/lessons/round-90-verifier-spotcheck.md` (carried). The plan's touch list
   names `corpus/README.md` ("index rows for the new corpus files; append-only Frontier notes"),
   and no seat owns that file, so the three coverage-map rows land with the L1's integration. If
   they do not, `corpus.index.unindexed` rises from its carried 1 to 4.
3. **The C1 knowledge entry's `used-by` cells name two files each** (the knowledge entry and the
   lesson). `verify_corpus_integrity`'s `E11` check requires every `used-by` path to exist on disk;
   both exist once this patch lands, and the census `validate` above confirms it (exit 0, no E11).
4. **The C2 leg-A receipt's measured revision is `9264baaa…`, not the freeze base.** The receipt
   `.ufo/waves/round-91/receipts/harness-selftest-duration.txt` names its own measured revision
   (`9264baaa823cdae3d009a4004e014639551e016f`, the round base) and its own load (1-minute loadavg
   2.73 → 3.16); the C2 knowledge entry cites the receipt as it is, and `verified-at` names the
   freeze commit separately, so the two revisions are not conflated. (ExecFloorsCap's report
   records the same point.)
5. **The rejection candidate's status enum matters for `W01`.** A tier-C row with status `mined`
   and a non-`—` `used-by` would raise `W01`; S264 is tier C with status `rejected`, so it does
   not, and `W02` (thin reject reason) does not fire either — its `teaches` cell is long.

## Out of scope / not done, and why

- **`corpus/README.md` index rows** — the plan's touch-list item for the L1 (see finding 2); this
  seat's file ownership is the two knowledge files, the lesson and the three SOURCES rows.
- **No `SKILL.md` edit, no registry row, no `corpus/QUALITY.md` edit** — none is in this seat's
  ownership, and `SKILL.md` is at the 600-line ceiling (receipt `base-skill-size.txt`).
- **The Jia & Harman survey route** (the plan's third-choice S262 route) was opened and readable
  but is *not* proposed as a row: the corpus already screened that work out in round 64, and S260
  plus S120 already carry the killed/survived/equivalent vocabulary. It is recorded as a lead in
  the lesson's `## Gate` only.
- **The plan, the controls and every frozen instrument were not touched**, and no counter's
  predicate was repaired.

## Tooling

No package or tool was installed or upgraded; no `pacman`, `uv`, `npm` or `cargo` transaction; no
`sysctl` write and no `/proc/sys` write; no change to any PATH directory. Only `git`, `python3 -B`
and the fleet's own read-only `scripts/sources-census.sh` were used.

## Bounds of this report

Every number above was observed in a scratch clone of the lane at the named revision, or read from
a committed receipt under `.ufo/waves/round-91/receipts/`. No claim is made about the landing
revision: the landing measurement is the L1's, and this seat's entries carry the frozen predicate as
their `recheck:` line so the landing can re-derive them.
