# B14SourcesUpdate — S213 `used-by` patch draft (round 76, w1)

Seat: leaf scribe, report-only. Draft written to
`.ufo/waves/round-76/build/sources-patch.md`; no lane file was modified by this seat.

## Axes

Bears on **consistency** (the C1 registry conjunct (e) is landed as one in-place permitted-cell
change with a logged old→new), **operability** (the patch is copy-pasteable and its application
constraint is named), **calibration** (two frozen requirements collide over the same cell and are
reported rather than silently picked), **adjacency** (the change reaches `check_skill_evals_v2`,
which no other seat's item names). No claimed movement on depth, freshness or coverage: those rest
on seats that fetch, write the entry and act on SKILL.md.

## Behaviour (commands as run, exit codes as seen)

Base measured: lane HEAD `4de12b61f75c73e3675ef0e422cc2be0f7da8960`; the contract's C2 base
`b7f13f4` carries the byte-identical S213 row.

1. Read the S213 row raw (`corpus/SOURCES.md:153`) — 11 cells, `used-by` =
   ` corpus/knowledge/skill-eval-artefacts-round70.md `, `status mined`, `recheck 90d`.
2. Built a lane mirror at `/fast/scratch/hyaku/kotoba-r76/B14SourcesUpdate/lane` (`cp -a corpus`,
   plus `SKILL.md`) and applied the cell change with a Python cell-index edit (cell 11 only).
3. Column check: `awk -F'|' 'NR==153{print "NF="NF}'` → `NF=13` before and after; `len(line.split("|"))`
   → 13 (11 cells + 2 edge empties); row count `grep -cE '^\|[[:space:]]*S[0-9]{3,}'` → 151 → 151.
4. Census, entry-absent arm: `sources-census.sh validate --file <mirror>/corpus/SOURCES.md` →
   `file E11 S213 missing used-by corpus/knowledge/description-craft-round76.md`, **exit 1**.
5. Census, entry-present arm (stub file): `file ok <mirror>/corpus/SOURCES.md`, **exit 0** (20
   pre-existing `W04` lines unchanged). Real-lane base control same day: `kotoba ok`, **exit 0**.
6. Append-only gate, purpose-built two-commit fixture: `log … S213 used-by: … -> …` +
   `sources append-only rows clean: 1 commits scanned, 0 protected-cell changes`, **exit 0**;
   negative control (S213 `teaches` altered) → `breach … S210 teaches`, **exit 1**.
7. Append-only gate, lane clone (`git clone --shared`, read-only): base
   `breach 18 change(s) in 8 of 44 commits` exit 1 → with the patch
   `breach 18 change(s) in 8 of 45 commits` exit 1 **plus** one `log` note. **0 new breaches.**
8. `check_skill_evals_v2.py` on the same clone: `2 of 10` at `b7f13f4` and at `4de12b6` → `1 of 10`
   with the patch, adding `F7: S213 used-by != corpus/knowledge/skill-eval-artefacts-round70.md
   (exact match required)`; exit 1 in all three states (already red at base).
9. Apply-check from the artifact alone: extracted the two fenced lines from
   `build/sources-patch.md`, substituted the new one into a fresh lane copy → census `file ok`,
   **exit 0**; the substituted line equals the mirror line byte-for-byte.

Old→new `used-by` (verbatim cells):
` corpus/knowledge/skill-eval-artefacts-round70.md ` →
` corpus/knowledge/skill-eval-artefacts-round70.md, corpus/knowledge/description-craft-round76.md `

## Gates

| gate | state with this patch | evidence |
|---|---|---|
| census `validate` (kotoba) | exit 0, `ok`, 151 rows | mirror + apply-check; entry file must land with it (`E11` otherwise, exit 1) |
| 11-column contract (`NF=13`, `E01`) | holds; `NF=13`, 11 cells | §Columns of the patch |
| append-only (`check_sources_append_only.py`) | permitted cell: `log`, 0 new breaches (18 → 18); gate already red at base | fixture exit 0; clone 8 of 44 → 8 of 45 |
| `check_skill_evals_v2.py` | **2 of 10 → 1 of 10**, exit 1 (red at base too) | clone, three revs |
| `check_spec_craft.py` (green at base, 3/3) | **fails 0 of 3 if the SOURCES line lands without the entry**; 3 of 3 once the entry exists | clone: `--rev bccb297` → `spec craft pages backed 0 of 3`, exit 1, "not census-conformant (conjunct (b))"; with an entry stub in the same tree → `3 of 3`, exit 0 |
| `check_desc_craft.py` (C1 counter) | **not run: file absent** — `ls verifiers/check_desc_craft.py` → *No such file or directory* | also `check_r75_routed_repairs.py` absent |

## Touched surfaces

Written: `.ufo/waves/round-76/build/sources-patch.md`,
`.ufo/waves/round-76/w1/B14SourcesUpdate.md` (this report), and
`/fast/scratch/hyaku/kotoba-r76/B14SourcesUpdate/` (removed before yield).
Not written: `corpus/SOURCES.md` and every other lane file, the lane git index/state, counters,
receipts, snapshots, `MANIFEST.json`, `templates/`, `scripts/`, `.ufo/state/`, `considerthese/`.
Nothing installed (no pacman, no uv/npx); no git write outside the scratch fixtures (each fixture
asserted `git rev-parse --show-toplevel` = the fixture dir before committing).

## Out of scope (owned elsewhere)

- The anchor cell digest (C1 conjunct (a)) — see F1; not applied here.
- `corpus/knowledge/description-craft-round76.md` — B03/B26 fetch and another seat drafts it; my
  patch only names the path in `used-by` (the census `E11` constraint makes the two commit together).
- `corpus/lessons/round-76.md` `## Status changes` line — B17LessonScribe owns it; the exact text
  was messaged and is reproduced in the patch artifact.
- `verifiers/check_skill_evals_v2.py` relaxation — F2; outside the round's touch list.

## Findings

**F1 (contract conflict, moved to the L1).** `plans/round-76.md:27` requires "the optimizing-descriptions
digest equals the digest recorded in the S213 row's anchor update", but the touch list says
"`corpus/SOURCES.md` (S213 used-by cell only)" and S213's anchor carries **no** sha256 today
(its anchor names the subsection + `upstream commit 69ef37e…` only; S212 likewise). Fixture receipt:
appending `; fetched sha256 7cc54fbb… (2026-10-27, 13 403 B)` to the anchor cell →
`breach 9fe719c4b S213 anchor: …`, exit 1. Precedent: `bf98d28` (r71) edited S209/S210 anchors in
place and those two still appear as breaches in the lane's own 18. Options (touch-list widening
with +1 breach; a `supersedes S213 —` row; or dropping the anchor clause from the frozen sentence)
are listed in the patch artifact §CF-1; choosing is an L1 act, not a seat act.
Digest both fetch seats agree on: `7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837`
(13 403 B, `.md` route; B26 records the extensionless URL serving a 344 074 B HTML body instead).

**F2 (counter collision).** C1(e) wants S213 `used-by` to *list* the new entry;
`check_skill_evals_v2.py:289` (`if row[10].strip() != ENTRY:`, documented `:21` as EXACT) wants it
to *equal* the r70 entry. Both cannot hold; measured cost of the append is one finding (2 of 10 →
1 of 10) on a counter that is already red at base and is not in the base/no-harm battery lists.

**F3 (docstring overstatement, existing).** `check_skill_evals_v2.py:36` claims the S212/S213
anchors carry "fetched sha256 in the anchor cell"; neither row does, and the enforced check (`A9`)
only requires the token `upstream commit`. Not caused by this round; it is why F1's clause reads as
already-satisfied to a reader of the docstring.

**F4 (ordering constraint, operability).** Because the census raises `E11` for a `used-by` path
absent on disk, the SOURCES line and `corpus/knowledge/description-craft-round76.md` must land in
one commit; either alone produces `kotoba E11 … exit 1`. Measured knock-on: the SOURCES line alone
also drops `check_spec_craft.py` from `3 of 3` exit 0 to `0 of 3` exit 1 (it runs census
conformance as its conjunct (b)); adding the entry file in the next commit restores `3 of 3` exit 0.

**F5 (unverifiable at time of writing).** Conjunct (e) could not be exercised against its own
counter (`verifiers/check_desc_craft.py` absent). The `used-by` half is verified against
`sources-census.sh` (the parser any such counter must agree with) and the membership convention in
`check_spec_craft.py:691`; that is evidence about the registry, not about the counter.

**F6 (base-battery claim not reproducible; affects C2/R2).** `plans/round-76.md` § Base battery
states "corpus integrity exit 0; corpus independent exit 0" at base `b7f13f4`. Measured today in a
clean `git clone --shared` of the lane, and on the real lane, both verifiers are **red**:

```
# clone at b7f13f4 (tree clean) and real lane at HEAD — identical verdicts
$ python3 -B verifiers/verify_corpus_integrity.py --json
DRIFT corpus.index.tracked_files 145 != 144 ; DRIFT corpus.index.unindexed 1 != 0/empty ;
DRIFT corpus.pointers.report_total 101 != 99 ; DRIFT corpus.pointers.commit_total 44 != 43
exit=1
$ python3 -B verifiers/verify_corpus_integrity.py --no-baseline --json   # still red
DRIFT corpus.index.unindexed 1
exit=1
$ python3 -B verifiers/verify_corpus_independent.py --json
DRIFT corpus.index.unindexed 1                                          exit=1
```

The cause is the recurring one already recorded three times in `corpus/README.md:138,141,144`:
the closure lands `lessons/round-75-verifier-spotcheck.md` without an index row, "which turned
`verify_corpus_integrity.py` red at that base". Measured fix, in the clone at `b7f13f4` plus one
`corpus/README.md` row for `lessons/round-75-verifier-spotcheck.md`:

```
$ python3 -B verifiers/verify_corpus_integrity.py --no-baseline --json   -> exit=0
$ python3 -B verifiers/verify_corpus_independent.py --json               -> exit=0
$ python3 -B verifiers/verify_corpus_integrity.py --json                 -> still exit=1
   (count drift vs the r70 baseline: tracked_files 145 != 144, report_total 101 != 99,
    commit_total 44 != 43 — needs the baseline re-record, cf. the `round70_rerecord` note)
```

Operational consequence for R2's receipt (`.ufo/waves/round-76/receipts/noharm-at-tip.txt`, "reading
green"): green is reachable only via the `corpus/README.md` index row (already in the touch list as
"corpus/README.md (index row)") **plus** `--no-baseline` for the integrity leg, or a baseline
re-record. Recording integrity's default-mode 3 DRIFTs as green would be a fabricated verdict.

## Artifact paths

- `.ufo/waves/round-76/build/sources-patch.md` — old/new cell text, full old/new lines, receipts,
  CF-1/CF-2 option sets, lesson line.
- `.ufo/waves/round-76/w1/B14SourcesUpdate.md` — this report.
- Scratch (removed on yield): `/fast/scratch/hyaku/kotoba-r76/B14SourcesUpdate/`
  (`lane/`, `applycheck/`, `appendfix/`, `anchfix/`, `clone/`, `append-only-base.txt`,
  `append-only-clone.txt`).

```
VERDICT: DRAFT-ONLY | file=corpus/SOURCES.md cell=used-by(11) row=S213 | NF=13 / 11 cells | rows 151->151 | census exit 0 in 2 arms (E11 exit 1 without the entry) | spec_craft 3 of 3 stays green ONLY if the entry lands with it (0 of 3 otherwise, measured) | append-only 0 new breaches (+1 permitted-cell log) | check_skill_evals_v2 2 of 10 -> 1 of 10 (already red) | conflict CF-1 anchor-digest vs touch-list UNRESOLVED (L1) | conflict CF-2 exact-match used-by UNRESOLVED (L1) | base battery NOT reproducible: integrity 4 DRIFTs exit 1 at b7f13f4, independent DRIFT exit 1; green via README index row + --no-baseline (measured) | lane files written: 0 | installs: 0
```
