# FrQualityCriteria — QUALITY.md rows for routed defects 3, 4, 5 (final)

Seat: `KotobaR48.FrQualityCriteria` (scribe, leaf, no delegation).
My working base was `75f671b`; while this seat worked, the L1 landed `887b6af` (C1 freshness records + lesson M24–M27 + QUALITY Q20–Q21) and `84b9c9b` (records). All findings below were re-verified against the landed HEAD `84b9c9b`. Read-only on the lane; the only file I wrote there is this report. Scratch: `/fast/scratch/hyaku/kotoba-r48-a2/seats/FrQualityCriteria/`. Tools installed or updated: none.

## Findings

### F1 — Landed state: defect 3 is covered; defects 4 and 5 are not

`corpus/QUALITY.md` at HEAD carries **Q01–Q21**. The L1 landed:

- **Q20** (grounded in M24) — covers **routed defect 3** (parsed vendor rule versus lexical mirror): "A check that approximates an authority's rule names the parsed rule it approximates, and carries run counterexamples in both directions (what it misses, what it over-flags); 'stricter'/'looser' is a measured direction, never a label." This satisfies the required "name the parsed rule it approximates and keep its counterexamples". I verified the underlying check behaviour independently (F3): four fixtures reproduce the landed `C2LaneCheckerRun.md` verdicts.
- **Q21** (grounded in M26) — covers a repair-claim class (routed defect 1's cause naming), not my scope.

**De defects 4 (custody/hash equality) and 5 (closure metadata over frozen inputs) have no QUALITY row at HEAD** (`grep -c 'custody\|byte identity\|frozen input\|closure metadata' corpus/QUALITY.md` → 0). The lesson's "Routed items" table dispositions both items ("no cleanup this round", "no frozen input edited") but nothing would catch a violation. I draft two new rows for them.

### F2 — Two new rows, Q22 and Q23, in the exact table shape

Append after Q21 (verbatim, patch `quality-q22-q23.patch` applies cleanly to `84b9c9b`; 23 Q-rows, all 6 pipes, table shape preserved):

```
| Q22 | A byte-hash match against an original committed artifact establishes byte identity only; it does not establish custody, recovery of historical objects, original inode/mtime or uninterrupted possession, and absence/reconstruction facts plus all held evidence are preserved before any targeted cleanup. | custody/recovery claims, cleanup and pruning notes | M28 Hash match read as custody (`corpus/lessons/round-48.md` § Mistakes) | — |
| Q23 | New closure metadata is added as an indexed entry that re-records its own baseline; frozen inputs, historical receipts and claimed producer targets are not rewritten to make the gate green, and the corpus index baseline and the source-pin baseline remain distinct ownership surfaces. | closure/index/baseline edits | M29 Closure metadata written over frozen inputs (`corpus/lessons/round-48.md` § Mistakes) | — |
```

`supersedes` is `—` for both; Q22/Q23 restate no existing row. Q22 is deliberately narrower than Q11 (evidence-bundle size) and Q03 (records name the commit): it targets the custody reading of a hash match. Q23 targets the "indexed, not rewritten" half; M21 (round-47) already covers "corpus file landed without its index row" and is instrument-captured, so Q23 is the criterion side of the same routed item.

Numbering: Q22/Q23 are the next free ids at HEAD. FrMistakeScribe's proposed M27→Q23 was merged into M24→Q20 by the L1, so Q23 is free; I confirmed with the peer (its attribution class is captured by Q20). If the L1 instead wants Q24 for the second row, the patch renumbers only the id cell.

### F3 — How a reviewer shows each criterion fails a bad candidate

**Q22 (bad candidate: a report says a reconstructed snapshot was "recovered" because four hashes match).**
- `sha256sum` of a copy of `.ufo/round-48/verification/before-configured-root.json` → identical `8bec447a…`; `stat -c '%i %y %n'` shows **different** inode and mtime (95860370/2026-10-21 vs 1879172615/2026-10-22); `cmp` exit 0. Byte identity holds, custody does not.
- `git cat-file -e b1b48d1` (and `5d50621`, `371e901`, `51385ae`, `d68eae3`, `2e6e5c1`) → **exit 128** each; tree `a736f640…` → **exit 1**. The named historical objects do not resolve in lane or fleet stores; a hash match cannot recover them (the fleet round-47 custody append states the same: "The restored snapshot is **reconstructed**, not uninterrupted custody").
- `git rev-parse --verify df2db79` → exit 128; `/fast/scratch/kotoba-r47/shared` absent. So a candidate upgrading "four hashes match" to "custody restored" fails Q22 on these three receipts.

**Q23 (bad candidate: new corpus metadata lands and the gate is made green by editing the wrong surface).**
- Add `corpus/lessons/round-49.md`, tracked but with no coverage-map row → `python3 -B verifiers/verify_corpus_integrity.py --json` → `corpus.index.tracked_files` DRIFT (64 vs 63) and `corpus.index.unindexed` DRIFT (1), checker **exit 1**.
- Re-record `verifiers/corpus-baseline.json` `tracked_files` expect 63→64 *without* the index row → still **exit 1** (`unindexed` is a baseline-free `zero` check, `verify_corpus_integrity.py:631`). A baseline bump cannot buy an index row.
- Add the coverage-map row **and** re-record the expectation → **exit 0**, and `git diff --stat verifiers/baseline.json verifiers/checklist-baseline.json verifiers/surfaces-baseline.json` is **empty**: the corpus baseline (9 `corpus.*` checks) and the source-pin baseline (28 harness checks, `verifiers/baseline.json`) are separate ownership surfaces, and one is not touched to fix the other (the L1's own landing `887b6af` only changed `corpus-baseline.json`, 5 lines — the correct shape this criterion mandates).
- A candidate that instead edits a frozen input fails on hashes: `corpus/lessons/round-47.md` = `c6db414f…`, `round-47-verifier-spotcheck.md` = `fbd5a1fb…` (the value the parent recorded as `new_note_sha256`), `before-configured-root.json` = `8bec447a…` (the plan's pin), `after-configured-root.json` = `47e41ea9…`, ruler `01af33a6…`, oracle `1d09a38c…`, all stable at HEAD.

### F4 — Class text for the lesson (`corpus/lessons/round-48.md` § Mistakes, append after M27)

House shape: `class | evidence pointer (command → output) | captured-by | fix`.

**M28 Hash match read as custody**
- evidence: `sha256sum <lane>/.ufo/round-48/verification/before-configured-root.json ./copy.json` → identical `8bec447a…` while `stat -c '%i'` → `95860370` vs `1879172615`; `git cat-file -e b1b48d1` (and five more) → exit 128 each; `git cat-file -e a736f640…` → exit 1; fleet `.ufo/reports/round-47/kotoba.md` line 183 "The restored snapshot is **reconstructed**, not uninterrupted custody".
- captured-by: `none → Q22`.
- fix: Q22 — state what a hash match proves (byte identity) and what it does not (custody, inode/mtime, historical-object recovery); preserve absence/reconstruction facts and held evidence before any targeted cleanup.

**M29 Closure metadata written over frozen inputs**
- evidence: tracked-but-unindexed `corpus/lessons/round-49.md` → `verify_corpus_integrity.py` exit 1 (`unindexed` DRIFT 1, `tracked_files` DRIFT 64 vs 63); bumping only `corpus-baseline.json` → still exit 1; index row + expectation → exit 0 with the three other baselines untouched (`git diff --stat` empty).
- captured-by: `none → Q23`.
- fix: Q23 — index new metadata and re-record the owning baseline; leave frozen inputs, historical receipts, claimed producer targets and the other baseline surface alone.

### F5 — Out of scope / not mine
- I did not write `corpus/lessons/round-48.md` (lesson scribe's file; I hand only the M28/M29 class text), `corpus/SOURCES.md`, `corpus/README.md`, `corpus/knowledge/`, `README.md` or `verifiers/`.
- I did not run any fetched upstream code. The vendor-side verdicts cited in the lesson's M24 evidence come from `.ufo/waves/round-48/build/C2LaneCheckerRun.md` (peer seat); my own runs are lane-checker and `yaml.safe_load` only, labelled as such below.
- Observation for the L1, not changed by me: `corpus/QUALITY.md:7` says `grounded in` names a row in `round-46.md` § Mistakes, while Q19 already cites `round-47.md` and Q20–Q23 cite `round-48.md`. The prose pointer is stale; I left it alone (criteria are append-only; the preamble is not a criterion row).

## Evidence (commands, exit codes, paths, hashes — verified at landed HEAD)

| command | exit | result |
|---|---|---|
| `git -C <lane> rev-parse HEAD` | 0 | `84b9c9b…` (records) after `887b6af…` |
| `git show 887b6af --stat` | 0 | 7 files, 184 insertions; QUALITY +2 (Q20, Q21) |
| `python3 -B verifiers/verify_skill_checklist.py --skill fx/alias2.md --check trigger.no_xml_tag` | 0 | `PASS … no XML tag in name, description`; `description 2 chars` |
| same, `--skill fx/sq.md` | 1 | `FAIL … XML tag in description: '\\u003c'` |
| same, `--skill fx/uni2.md` | 0 | `PASS` on `Use <名> here.` |
| same, `--skill fx/comp.md` | 0 | `PASS` on `Use 5 < 6 when comparing budgets.` |
| same, `--skill fx/plain.md` | 1 | `FAIL … '<skills>'` (control) |
| `yaml.safe_load` on `fx/alias2.md` frontmatter | 0 | `description = 'Use <skills> here.'` → contains `<` |
| `yaml.safe_load` on `fx/sq.md` frontmatter | 0 | `description = 'Use \\u003cskills\\u003e here.'` → no `<` |
| `sha256sum <lane>/.ufo/round-48/verification/before-configured-root.json ./copy.json` | 0 | both `8bec447aa538446e84b7cb87b902c5f1021c42bd7a01f81ea14313262f7e2312` |
| `stat -c '%i %s %y %n' <original> ./copy.json` | 0 | inodes `95860370` vs `1879172615`; mtimes 2026-10-21 vs 2026-10-22 |
| `cmp <original> ./copy.json` | 0 | identical bytes |
| `git cat-file -e b1b48d1` (+`5d50621`,`371e901`,`51385ae`,`d68eae3`,`2e6e5c1`) | 128 | all six absent |
| `git cat-file -e a736f6407ba02a038a6c0256c40cc932727688fc` | 1 | tree absent |
| `git rev-parse --verify df2db79` | 128 | `fatal: Needed a single revision` |
| `ls /fast/scratch/kotoba-r47/shared` | 2 | snapshot directory absent |
| tracked+unindexed `corpus/lessons/round-49.md` → `verify_corpus_integrity.py --json` | 1 | `unindexed` DRIFT 1, `tracked_files` DRIFT 64 vs 63 |
| same after bumping `corpus-baseline.json` expect 63→64 | 1 | `unindexed` still DRIFT (baseline-free `zero` check) |
| same after adding the coverage-map row **and** the expectation | 0 | all checks PASS; `git diff --stat` of the other three baselines empty |
| `git diff --stat 75f671b..HEAD -- verifiers/baseline.json verifiers/checklist-baseline.json verifiers/surfaces-baseline.json verifiers/corpus-baseline.json` | 0 | only `corpus-baseline.json` (5 lines) |
| `sha256sum corpus/lessons/round-47.md corpus/lessons/round-47-verifier-spotcheck.md corpus/lessons/round-46.md` | 0 | `c6db414f…`, `fbd5a1fb…`, `1e99174b…` |
| `sha256sum .ufo/round-48/verification/*.json .ufo/round-48/tools/config-root-ruler.py .ufo/round-48/oracle/config-root-cases.json` | 0 | before `8bec447a…`, after `47e41ea9…`, ruler `01af33a6…`, oracle `1d09a38c…` |
| `git diff __check ../quality-q22-q23.patch` (fresh clone at `84b9c9b`) | 0 | applies; 23 Q-rows, all 6 pipes |

Route of the three defects: `corpus/lessons/round-47-verifier-spotcheck.md:72` (defect 3), `:73` (defect 4), `:74` (defect 5). Patch: `quality-q22-q23.patch`; class text for M28/M29 in F4.
