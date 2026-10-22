# ReviewProvinceFrontier: PROVINCE.md and corpus/README.md against round 51

Verdict: FAILS at HEAD 59903b2637689739a5b9901956301da72d0effe1. Five stale locations: PROVINCE.md:17, :23, :24, corpus/README.md:88, and the end of corpus/README.md § Known gaps (after line 132). Each is missing or still states the round-47 state. The round-51 text for all five exists only as uncommitted edits in the lane working copy, which the integrator is still applying. Those edits would clear every finding if committed as they stand; I judged HEAD, not the working copy.

## Answers to the three questions (at HEAD)

1. Does any line still say omp 18.12.5 is current? YES. corpus/README.md:88 and PROVINCE.md:24 name round-47 omp 18.12.5 as the last re-derived and re-pinned binary. Round 51 (commit e032030) landed omp 18.12.6 and neither line was updated.
2. Does any line say surfaces are 5/7 as current? NO. PROVINCE.md:24 gives "(surfaces 5/7, pins 1/3)" only as the round-46 drift, and the same bullet says "the round-46 figures above are historical". corpus/README.md:88 quotes it only in a parenthetical labelled a "stale copy". Not stale.
3. Does Core's sibling-arbitration line omit the new entry? YES. PROVINCE.md:17 ends at the round-50 sentence and names neither `corpus/knowledge/skill-overlap-levers-round51.md` nor `verifiers/check_overlap_levers.py`. The index row at corpus/README.md:75 does list the entry at HEAD.

## Stale lines at HEAD, with minimal appended corrections

1. PROVINCE.md:17 (§ Core, sibling arbitration). Stale by omission. Append after "...a stated split.":
   " Round 51: the per-client overlap levers join Core. Each of the 7 pinned clients documents a lever, other than description wording, that removes one named skill from the candidates (`corpus/knowledge/skill-overlap-levers-round51.md`; `verifiers/check_overlap_levers.py` prints `overlap levers backed 7 of 7 clients`). None is a tie-break between two skills that both stay candidates."

2. PROVINCE.md:23 (§ Frontier, first bullet). Stale by omission; the open question has moved. Append at the end of the line:
   " Round 51 (appended): the per-client overlap levers moved to Core (7 of 7 clients, none a tie-break); the open question is now whether naming a lane, or removing one of an overlapping pair, improves routing."

3. PROVINCE.md:24 (§ Frontier, loader-rule bullet). Stale: the latest re-pin it reports is 18.12.5. Append after "...same path family.":
   " **Round 51:** omp 18.12.6 re-derived and re-pinned (sha256 `85d9daf3…`); surfaces 7/7 (`verifiers/verify_surfaces.py --json`: pass 7, fail 0, exit 0) and pins 3/3 (`verifiers/check_substrate_pins.py`: `OK 3/3 pins hold`, exit 0). The 18.12.5 figures above are the previous pin."

4. corpus/README.md:88 (§ Frontier table, "Loader-rule freshness", second cell). Stale: the row presents round-47 omp 18.12.5 as the state. Append at the end of the second cell, before the third cell's separator:
   " **Round 51:** omp 18.12.6 is the current pin (`verifiers/verify_surfaces.py --json` → pass 7, fail 0, exit 0; `verifiers/check_substrate_pins.py` → `OK 3/3 pins hold`, exit 0); the round-47 18.12.5 figures are the previous state."

5. corpus/README.md, § Known gaps, after line 132 (the sibling-arbitration bullet ends there). Stale by omission. Append as a new line:
   "  **Round 51 (append-only):** the per-client overlap levers now live in Core (`PROVINCE.md` § Core): 7 of 7 pinned clients document a removal lever other than description wording (`knowledge/skill-overlap-levers-round51.md`; `python3 -B ../verifiers/check_overlap_levers.py --rev <rev>` → `overlap levers backed 7 of 7 clients`). None decides between two skills that both remain candidates, so whether removing one of an overlapping pair, or naming the neighbour, improves routing is still unmeasured."

Root cause: commit e032030 (C1) changed the verifiers and the baseline but neither of the two documents' Frontier or Core rows; commit 34cfffb (C2) added the index rows and the PROVINCE.md:35 and :46 edits, but not the Core, Frontier or Known-gaps text.

## Checked and consistent at HEAD (no action)

- corpus/README.md index rows 72 (finding 4 superseded), 75 (the levers entry, seven client pages) and 76 (round-51 lessons) are present at HEAD and match the entry, the lesson and the counter.
- PROVINCE.md:35 (the D6 pointer) and PROVINCE.md:46 (the kama row) are present at HEAD.
- The working copy's replacement text is accurate against the counters. Its "7 of 7", "pass 7", "fail 0" and "OK 3/3" figures match the runs below. The working copy has no line that calls 18.12.5 or 5/7 current.
- PROVINCE.md:14 (the Core instrument list) does not name check_overlap_levers.py. It is named at PROVINCE.md:17, the same convention round 49 used for check_sibling_census.py. Not stale.

## Evidence (commands and exit codes)

- `git clone -q <lane> <scratch>/lane && git checkout -q 59903b26…`: exit 0. Lane HEAD, lane master and origin/HEAD are all 59903b26.
- `git log --oneline 43ca0bfb..59903b26`: 5 commits (7c81a78, e032030, 34cfffb, e621902, 59903b2).
- `git diff --stat 43ca0bfb 59903b26`: 19 files, +1883 -45. Of the two documents, only PROVINCE.md (4 lines) and corpus/README.md (5 lines) changed, and not in the Core, Frontier or Known-gaps text.
- `git blame -s -L 17,17 HEAD -- PROVINCE.md`: 956ee16. `-L 23,24`: 956ee16 and 7ad7fad. `-L 88,88 HEAD -- corpus/README.md`: 7ad7fad (the round-47 text).
- `git blame -s -L 143,143 HEAD -- corpus/README.md`: exit 128, "file corpus/README.md has only 142 lines".
- `diff <(git show HEAD:PROVINCE.md) PROVINCE.md`: exit 1, lines 17 and 23-24 differ (both files 58 lines). `diff <(git show HEAD:corpus/README.md) corpus/README.md`: exit 1, line 88 differs and lines 133-143 are appended (HEAD 142 lines; working copy 153).
- `cmp` of HEAD against the working copy: differs at PROVINCE.md line 17 and corpus/README.md line 88.
- `python3 -B verifiers/verify_surfaces.py --json` (scratch clone at 59903b26): exit 0, `{'exit_code': 0, 'fail': 0, 'pass': 7}`.
- `python3 -B verifiers/check_substrate_pins.py`: `OK 3/3 pins hold`, exit 0.
- `python3 -B verifiers/check_overlap_levers.py --rev 59903b2637689739a5b9901956301da72d0effe1` (no `--fetch`, no network): `overlap levers backed 7 of 7 clients`, exit 0.
- `sha256sum /home/vgpnk/.local/bin/omp`: 85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4, mtime 2026-10-21 20:37:24 -0300. This matches the pin in verifiers/baseline.json. I did not execute omp, so its version string was not re-read.
- The working copy's "4 renamed-callee generations (3 at base)" reproduces from `.ufo/waves/round-51/build/OmpRenameHistory.md` rows 2, 3, 5 and 6 (row 4's names are unrecorded). Citation nit only: the round-47 generation appears in verify_surfaces.py's arm comments (lines 172-175), not among the `omp_round*_note` keys, which are round21, round44 and round51.

## Residual risk and gaps

- The fix sits uncommitted in the working copy. If HEAD ships as it is, all five findings stand. The roster shows the integrator running "Apply frontier drafts"; I did not contact it.
- Not re-measured: the checklist counts in corpus/README.md § Known gaps (8 executed, 2 delegated, 31 unexecuted). checklist-baseline.json is unchanged by round 51, so the round did not touch them.
- Nit, not stale: the working copy's corpus/README.md:88 and PROVINCE.md:24 use root-relative `verifiers/...` command paths, while the index rows use `../verifiers/...`. Command strings only; they run from the repo root.
- Tools: none installed or upgraded. Scratch directory: /fast/scratch/hyaku/kotoba-r51/falsify/ReviewProvinceFrontier/ (lane clone at 59903b26, base snapshot, surfaces.json). The lane itself was only read; the only write is this report.
