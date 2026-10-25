# Round 69 / wave 1 — D8 corpus-integrity baseline verification (ExecIntegrityBaseline)

**Assignment:** verify D8/R68-8 — run `verifiers/verify_corpus_integrity.py --no-baseline --json` in a
sandbox clone of the lane at the branch tip, read `verifiers/corpus-baseline.json`, and compare the four
`expect` values (`corpus.index.tracked_files`, `corpus.index.unindexed`,
`corpus.pointers.report_total`, `corpus.pointers.commit_total`) with the gate's own observed values.

**Verdict: D8 is NOT closed at the tip. 3 of the 4 expectations drift; only `commit_total` matches.**
The baseline was never re-recorded after the round-68 closure committed its own spot-check lesson
(`a5f7459`), and that lesson has no coverage-map row. The baseline file itself is faithful to the head it
names — the drift is a later, unrecorded corpus change, not a hand-set expectation.

## 1. Two sets (no baseline edit; read-only comparison)

Baseline file `/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/corpus-baseline.json`
(sha256 `d3f8acd44d65786bead302812035e7288c4760e7a169df53964f8917be2d488d`, unchanged at tip; identical
bytes in lane working tree and sandbox):

| check | baseline `expect` | gate `observed` at tip | relation |
|---|---|---|---|
| `corpus.index.tracked_files` | 124 | **125** | **DRIFT +1** |
| `corpus.index.unindexed` | 0 | **1** | **DRIFT +1** |
| `corpus.pointers.report_total` | 85 | **87** | **DRIFT +2** |
| `corpus.pointers.commit_total` | 38 | 38 | equal |

Gate's own verdict line (baseline mode, sandbox at tip):

```
DRIFT   corpus.index.tracked_files: observed=125 expected=124
DRIFT   corpus.index.unindexed: observed=1 expected=0 / empty
DRIFT   corpus.pointers.report_total: observed=87 expected=85
6/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.index.unindexed, corpus.pointers.report_total
exit=1
```

`--no-baseline --json` mode (the mode the assignment names) adjudicates the three `equal` checks as
`OBSERVE` (`expected: "baseline"`) and reports `corpus.index.unindexed` as the single `zero`-mode
`DRIFT`; the observed values are identical (`125 / 1 / 87 / 38`).

## 2. Exact command + sandbox identity

```
git clone --shared --no-local /home/vgpnk/Projects/shokunin/kotoba-shokunin /tmp/exec-integrity-69b
git -C /tmp/exec-integrity-69b checkout a238989a96cb0d2b939679126b832d75b861ca6e   # branch tip
python3 -B verifiers/verify_corpus_integrity.py --no-baseline --json               # exit 1
python3 -B verifiers/verify_corpus_integrity.py                                    # 6/9, exit 1
```

Sandbox HEAD = lane tip `a238989a96cb0d2b939679126b832d75b861ca6e` (`round-69: frozen plan, three
counters … and base/junk controls`), clean tree (`git status --porcelain` empty). Nothing was run in the
lane; the lane's Git index, jj state and working tree were read only. The verifier's `FLEET_ROOT` commit
hop read `/home/vgpnk/Projects/shokunin` read-only (`git cat-file -e` only).

## 3. Drift attribution (causal chain, each link re-opened)

1. `59ac5c6` (`round-68: C1 counter fix … and the C2 census baseline re-record`) re-recorded the baseline
   to `124 / 0 / 85 / 38`, measured at head `605b84ba`. **Reproduced independently:** a second `--shared`
   clone checked out at `605b84ba` returns exactly `tracked_files 124, unindexed 0, report_total 85,
   commit_total 38` (`unindexed_detail []`). The record was taken from the gate's own measurement, as its
   note claims.
2. `a5f7459` (`round-68 verifier spot-check (integrator, hyaku)`), parent `2cf0d99`, then added one new
   tracked corpus file: `git diff --stat 605b84ba a238989 -- corpus/` →
   `corpus/lessons/round-68-verifier-spotcheck.md | 207 +++++`. It is the **only** corpus change between
   the re-record and the tip.
3. That file explains all three drifts exactly:
   - **tracked_files 124 → 125**: one new tracked corpus file.
   - **unindexed 0 → 1**: `unindexed_detail` = `["corpus/lessons/round-68-verifier-spotcheck.md"]`; no
     coverage-map row exists for it (`grep 'round-68-verifier-spotcheck' corpus/README.md` → no match at
     tip).
   - **report_total 85 → 87**: the lesson carries exactly two report pointers, both
     `.ufo/reports/round-68/kotoba.md`; `report_dead 0` (the fleet file
     `/home/vgpnk/Projects/shokunin/.ufo/reports/round-68/kotoba.md` exists, 22067 bytes). 85 + 2 = 87.
   - **commit_total 38 = 38**: the lesson adds no commit citations; every new file since the record adds
     none, so this expectation still holds.
4. No later corpus change: the tip commit `a238989` touches only `plans/`, `verifiers/check_*.py` and
   `.ufo/waves/` controls; its measurement is byte-identical to the plan's frozen control
   `.ufo/waves/round-69/controls/C2-base-integrity.txt` (`measured-rev: a5f7459…`, same three DRIFTs,
   `6/9`, `exit=1`). My tip run and the frozen control agree.

This is the same class the coverage map already records for r66→r67 and r67→r68 ("landed at `…` without
an index row, which turned `verify_corpus_integrity.py` red"); r68's closure committed its spot-check
*after* its own re-record and repeated it.

## 4. Draft-state forward values (sandbox overlay — NOT a lane measurement)

Two throwaway `--shared` clones at the tip, overlaid with the L1's uncommitted working tree
(`rsync -a corpus/ verifiers/ PROVINCE.md`, `git add -A` inside /tmp). Purpose: fix the value a correct
D8 re-record must carry, and check the draft does not re-drift.

| state (sandbox) | tracked | unindexed | report_total | commit_total |
|---|---|---|---|---|
| tip, committed `a238989` | 125 | 1 | 87 | 38 |
| tip + **only** the draft's round-68 spot-check README row | **125** | **0** | **87** | **38** |
| tip + full draft (2 new corpus files staged) | **127** | **1** | **87** | **39** |

Findings for the C2 seat:

- The L1 draft **already carries** the round-68 coverage-map row
  (`| Round-68 verifier spot-check (closure) | \`lessons/round-68-verifier-spotcheck.md\` | …`), and it
  works: `unindexed` for that file clears to 0 (probe above), so the missing half of D8 is in flight.
- The draft's two new corpus files (`knowledge/skill-name-precedence-round69.md`, `lessons/round-69.md`)
  move the counts: `tracked_files` 125 → **127**, `commit_total` 38 → **39** (the lesson's
  ``commit `a238989a` `` token; it resolves), `report_total` stays **87** (neither new file cites a
  `.ufo/reports/` path).
- **The draft does not index `lessons/round-69.md`** (`grep -c 'lessons/round-69.md' corpus/README.md` →
  0), so under the draft `unindexed` stays 1 with the detail now naming the round-69 lesson. A re-record
  taken before that row lands reproduces the r68 defect one round later.
- Therefore D8's re-record must be taken **after** the wave's corpus files and their index rows land, and
  should read **127 / 0 / 87 / 39** (not `125 / 0 / 87 / 38`, which is only correct if neither round-69
  corpus file lands).

## 5. Baseline integrity

- `verifiers/corpus-baseline.json` is **unmodified** at tip and in the lane working tree
  (`git diff --quiet HEAD -- verifiers/corpus-baseline.json` → clean; same sha256 into the sandbox).
- The four `expect` values in the file are exactly `124 / 0 / 85 / 38`; the file's
  `measured_against.head` is `605b84ba`, and that head reproduces them. Treat the baseline as honest at
  its named revision, stale only with respect to the two commits after it.
- I did not edit the baseline or any committed file.

## 6. Risks / limits

- The comparison is count-level, as D8 specifies; `tracked_files` being equal in some future tree would
  not by itself prove the same file set. The attribution above is by explicit set difference
  (`git diff --stat`, `unindexed_detail`), not by arithmetic alone.
- `report_total` depends on `FLEET_ROOT` resolution for bare pointers; the sandbox gates read the real
  fleet repo read-only. `report_dead 0` at both tip and `605b84ba`, so the hop does not mask anything
  here.
- The draft-overlay rows 2–3 are sandbox reproductions of the working tree, not lane measurements; the
  authoritative D8 predicate must be re-run by the parent after the content wave lands.

## 7. Cleanup

Sandboxes `/tmp/exec-integrity-69b`, `/tmp/exec-integrity-69b-base`, `/tmp/exec-integrity-69b-draft`,
`/tmp/exec-integrity-69b-min` removed at the end of this seat; JSON/`txt` receipts stayed in `/tmp`.
No installs or upgrades were performed. No lane, fleet or jj state was written.

Report: `.ufo/waves/round-69/w1/ExecIntegrityBaseline.md`
