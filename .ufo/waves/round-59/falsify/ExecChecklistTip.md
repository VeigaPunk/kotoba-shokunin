Result: MIXED — every lane gate keeps its base exit code at the round-59 data commit and the corpus-integrity DRIFT name set shrinks 5 → 4, but the round-59 content adds one new unresolvable-commit instance (`corpus/lessons/round-59.md:45`), so "no new drift instance" does not hold even though "no gate turned red" does.

# Round-59 falsify — gate tip receipts

Seat `KotobaR59.ExecChecklistTip`. Item: QUALITY Q50 / round-58 R2 discipline — tip receipts for
this round. Receipt written: `.ufo/waves/round-59/receipts/data-r59-c63ccc68.txt` (this report is
its narrative; every number below is copied from that receipt, which also carries byte counts and
sha256 of each command's stdout).

Rev under test: `c63ccc6823e1f6a8577acbb43d19551eadbbee9a`. Base: `a975cbbf00534443c49bf02e29c813a3db0bf0f8`.
After-tip: `d64d945b3435e2532203c505ad64ecf5d91b780e`.

## What this seat attacks

Two claims, both failable:

- **A1 after-column no-harm.** For the five gates the item names, the round-59 data commit is not
  worse than the base: every gate that exits 0 at base exits 0 at `c63ccc68`, and no DRIFT
  *check name* is added.
- **A2 receipt discipline.** The numbers this seat records are reproducible from the named rev and
  agree with receipts other seats committed for the same revs (a receipt that cannot be reproduced
  or that contradicts a sibling receipt is the failure mode M80 named).

## Verdicts

| claim | verdict | one-line evidence |
|---|---|---|
| A1 (exit codes, gate by gate) | **HOLDS** | base `0,1,0,0,0` → data `0,1,0,0,0`; same five commands, same order |
| A1 (DRIFT *name* set does not grow) | **HOLDS** | 5 names → 4 names; `corpus.index.unindexed` leaves the set (1 → 0) |
| A1 (no new drift *instance*) | **BREAKS** | `commit_unresolvable` 1 → 2; new detail `corpus/lessons/round-59.md:45: b8e7d8aa…`; `commit_total` 33 → 34 |
| A2 (reproducible, agrees with sibling receipts) | **HOLDS** | base numbers identical to `.ufo/waves/round-59/receipts/base-r59-a975cbbf.txt:27-33`; counter hash identical to `.ufo/waves/round-59/C1-measure.txt:4` |

So the item's deliverable is **MIXED**: green on the gate layer, red on one instance inside an
already-red check, and the before/after column is *not* green at either end (the baseline is stale
by construction — see Risks).

## Findings

### F1 — HOLDS: gate exit codes are unchanged from base to data commit

Ran in `/fast/scratch/hyaku/kotoba-r59/ExecChecklistTip/kotoba-shokunin` at
`c63ccc6823e1f6a8577acbb43d19551eadbbee9a` (`git rev-parse HEAD` printed that rev; `git status
--porcelain` 0 lines):

| # | command | exit | stdout bytes | sha256 (first 16) | summary |
|---|---|---|---|---|---|
| 1 | `python3 -B verifiers/verify_skill_checklist.py --json` | **0** | 2559 | `825a89d423c7e5be` | pass 11 / fail 0 / na 0; 587 lines ≤ 600; 141 citations |
| 2 | `python3 -B verifiers/verify_corpus_integrity.py --json` | **1** | 4014 | `fcfefe614a3c2e21` | 4 DRIFT / 5 PASS |
| 3 | `python3 -B verifiers/check_gate_registry.py --rev c63ccc68…` | **0** | 1682 | `b7a3efdd19779025` | 33 of 33 rows conformant; phantom 0 |
| 4 | `python3 -B verifiers/check_assertion_floors.py` | **0** | 580 | `031572c9188b3934` | 14 PASS, 0 FAIL |
| 5 | `python3 -B verifiers/check_correction_sweep.py --rev c63ccc68…` | **0** | 35 | `cf2ccb3f6f36c243` | 0 stale block(s) |

Base `a975cbbf`, same five commands: `0,1,0,0,0`; checklist sha `6f71dcbae861e7ff` (596 lines,
137 citations), integrity sha `fc6468de2048959c`, registry sha `ddb633ac617b8e47` (32 of 32),
floors sha `031572c9188b3934` (byte-identical to the data rev), sweep sha `cf2ccb3f6f36c243`
(byte-identical). The full captures are `out/cmd1.out` … `out/cmd5.out` and `outbase/cmd1.out` … `outbase/cmd5.out`
under the sandbox root.

The one number that moves in the *good* direction is `corpus.index.unindexed`: 1
(`corpus/lessons/round-58-verifier-spotcheck.md`) → 0, because the round-59 commit indexes both new
corpus files. `corpus.index.stale_patterns`, `missing_paths`, `pointers.report_dead` and
`commit_nonhash` stay at 0 throughout.

### F2 — BREAKS: one new unresolvable-commit citation, introduced by the data commit

`verify_corpus_integrity.py --json` at `c63ccc68`, exit 1, `observed.corpus.commit_unresolvable`
= 2 with details:

```
corpus/lessons/round-54-verifier-spotcheck.md:147: 451a02ff           (present at base and earlier)
corpus/lessons/round-59.md:45: b8e7d8aa99cb903d1b89d5b82696b2db3a337d9b   (NEW at c63ccc68)
```

`commit_total` moves 33 → 34 for exactly this citation. The line reads (verbatim fragment, 13
words): `sandbox commit `b8e7d8aa99cb903d1b89d5b82696b2db3a337d9b` at `/fast/scratch/hyaku/kotoba-r58/MutC1Content``.
The hash is genuinely a scratch-only sandbox commit: `git cat-file -t b8e7d8aa…` exits **128**
("could not get object info") in the lane, in the fleet-root repo, and in the sandbox clone. It is
correctly *labelled* in prose ("sandbox commit … at /fast/scratch/…", and the sentence ends "This
is the earlier seat's recorded run, not a run by me"), but the checker cannot see the label:
`COMMIT_RE = re.compile(r"(?<![A-Za-z0-9_-])commit[ \t]+`([^`\n]+)`")`
(`verifiers/verify_corpus_integrity.py:149`) matches `commit` + whitespace + backticked token, so
"sandbox commit `<40 hex>`" is harvested as a lane-commit promise.

Same hash, same provenance, already committed at `.ufo/waves/round-58/falsify/MutC1Content.md:148`
(`Commit: sandbox b8e7d8aa…`) — the lesson copied it from `.ufo/waves/round-59/build/ScribeMistakes.md:13`.
`.ufo/` is outside `corpus/`, so the copy is what creates the lane-visible citation.

**Exact correction** (one-line text edit, no counter or rule change): in
`corpus/lessons/round-59.md:45`, replace

```
sandbox commit `b8e7d8aa99cb903d1b89d5b82696b2db3a337d9b` at `/fast/scratch/hyaku/kotoba-r58/MutC1Content`
```

with

```
a scratch-only sandbox commit; see `.ufo/waves/round-58/falsify/MutC1Content.md:148` for its hash
```

i.e. keep the provenance pointer, drop the backtick that sits immediately after the word `commit`.
No evidence is lost (the hash stays in the committed round-58 report line), and the checker's
`commit_total` returns to 33 and `commit_unresolvable` to 1. The alternative — teaching
`verify_corpus_integrity.py` to exempt `sandbox commit`-prefixed hashes — touches a verifier and its
floors mid-falsify and is not recommended for this wave. Note that `readme`/baseline expectation
(32 / 0) is stale anyway (Risks), so the text edit is about not *adding* instances, not about
turning the check green.

### F3 — HOLDS: the DRIFT name set shrinks, and the flat `report_total` is explained

DRIFT names at `c63ccc68` (4 of 9 checks; the other 5 PASS):

```
corpus.index.tracked_files           96 vs 81
corpus.pointers.report_total         64 vs 51
corpus.pointers.commit_total         34 vs 32
corpus.pointers.commit_unresolvable   2 vs 0
```

Base had the same four plus `corpus.index.unindexed` 1 vs 0 → 5 names. The data commit adds two
corpus files (`corpus/knowledge/hook-files-round59.md`, `corpus/lessons/round-59.md`; `git diff
--name-status a975cbbf c63ccc68 -- corpus/` shows those two `A` rows plus `M` of QUALITY.md,
README.md, SOURCES.md, knowledge/anatomy-and-compression.md), which is why `tracked_files` moves
94 → 96 while the other two stay indexed.

`report_total` is flat at 64 **because the pointer population is flat, not because the new files
are unread**: `UFO_POINTER_RE` (`verifiers/verify_corpus_integrity.py:144-146`) harvests only
`.ufo/reports/round-<N>/*.md`. `grep -c 'ufo/reports/round-'` returns 0 for both new files; the
round-59 lesson's 10 wave citations are `.ufo/waves/...`, outside that population. `corpus_md_files`
93 → 95 confirms the files were scanned.

### F4 — HOLDS: the measure-receipt tip is byte-identical to the data commit for all five gates

`git diff --name-status c63ccc68 d64d945b` is exactly one line, `A .ufo/waves/round-59/C1-measure.txt`
— nothing under `corpus/` or `verifiers/`. I re-ran the gates in a third clone at
`d64d945b3435e2532203c505ad64ecf5d91b780e` rather than inferring: all five captures are `cmp -s`
identical to the data-rev captures (2559/4014/1682/580/35 bytes; sha256 as in F1, with commands 3
and 5 run with `--rev d64d945b…`). So the receipt names *both* the data commit and the current
round-59 tip, and the numbers carry without recomputation (M80's failure mode is assertion without
a receipt; this is the receipt).

### F5 — HOLDS: agreement with the receipts other seats committed

- Base column: my independent run reproduces `.ufo/waves/round-59/receipts/base-r59-a975cbbf.txt`
  exactly — 5 DRIFT with `tracked_files 94 / unindexed 1 / report_total 64 / commit_total 33 /
  commit_unresolvable 1` (that file's lines 27-33), exit 0/1/0/0/0.
- Counter hash: `git show c63ccc68:verifiers/check_hook_files.py | sha256sum` =
  `f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71`, identical to
  `.ufo/waves/round-59/C1-measure.txt:4`; `TARGET = 4` / `NEW_TARGET = 5` sit at that file's lines
  253-254 as the goal states. (Cross-check only — the C1 measurement itself is other seats' item.)
- Registry: `check_gate_registry.py` goes 32 of 32 → 33 of 33 because `verifiers/check_hook_files.py`
  is registered at the data commit (the registry listing diff is the single added row). A new gate
  cannot be a phantom: phantom stays 0.

## Risks and notes

- **The before/after column cannot be green at either end.** `verifiers/corpus-baseline.json` is
  dated `as_of 2026-09-29`, measured at `head d85982d` (round 16) with expected
  `tracked_files 81 / report_total 51 / commit_total 32 / commit_unresolvable 0`. Corpus growth since
  then is what the numeric DRIFT measures; base `a975cbbf` was already 94/64/33/1. Recording this as
  a round-59 regression would be wrong; recording `4 DRIFT` as "clean" would be wrong too. The
  decision to re-baseline is the L1's, and is out of this seat's writable scope.
- **Lane HEAD moved during the run**: at 09:58Z the lane was at `3f15f844` with a dirty tree
  (`M SKILL.md`, `M corpus/README.md`, `M corpus/knowledge/hook-files-round59.md`,
  `M corpus/lessons/round-59.md`, `?? .ufo/waves/round-59/falsify-taskcall-sent.json`). My numbers
  are pinned to `c63ccc68` / `d64d945b`; the dirty tree was never in any clone (`git status
  --porcelain` 0 lines in all three).
- **Setup precondition verified by this seat, not assumed.** A plain clone at `c63ccc68` in a
  directory named `seatclone` with no fleet-root mirror gives `verify_skill_checklist.py --json`
  **exit 1, pass 8 / fail 3**: `trigger.name_directory` (`name 'kotoba-shokunin' != directory
  'seatclone'`), `trigger.citation_resolves` (`SKILL.md:577: '../.ufo/reports/round-7/kotoba.md'`
  does not resolve) and `governance.citation_resolves` (`LOG.md:177,255,311,779` … `(+21 more)`).
  Capture: `/fast/scratch/hyaku/kotoba-r59/ExecChecklistTip/bare/checklist-bare.json`, 3090 bytes,
  exit 1. The three receipt clones are therefore each named `kotoba-shokunin` with the fleet-root
  siblings symlinked into their parent, exactly as `.ufo/waves/round-59/w0/ExecR2TipReceipts.md`
  § Method prescribes. Exit 0 (11/11) is only meaningful in that configuration; a reviewer who
  re-runs in a bare clone will see three false reds, not a finding.
- **Minor observation, no claim**: `verify_skill_checklist.py --json` emits a top-level `exit_code`
  key, `verify_corpus_integrity.py --json` does not (`keys = ['observed','results']`). Consumers
  must read the process status for the latter. Recorded because Q50 receipts invite mechanical
  consumption.
- No tool installed or upgraded. Python 3.14.8, `python3 -B`. No network access — none of the five
  commands fetches. No lane write, no lane jj/git write, no sandbox commit (so no sandbox hash is
  cited bare anywhere in my artifacts).

## Files this seat wrote

| file | role |
|---|---|
| `.ufo/waves/round-59/receipts/data-r59-c63ccc68.txt` | the receipt: revs, commands, exit codes, byte counts, sha256, DRIFT names, before/after columns |
| `.ufo/waves/round-59/falsify/ExecChecklistTip.md` | this report |

Nothing else was written in the lane. Scratch state lives only under
`/fast/scratch/hyaku/kotoba-r59/ExecChecklistTip/`.
