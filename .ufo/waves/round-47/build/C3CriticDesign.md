verdict: C3's governance half is real calibration only in the pinned, fail-closed form. A line-sha-pinned erratum with a horizon beats both alternatives: same-line absence detection masks 120 live subjects, and leaving the gate red hides every new dead citation at the exit-code level. But "10/10, evaluated 804" can't tell the registry apart from three in-place LOG launderings, so the falsifier must also pin the BASE LOG prefix and run the mutation arms. The corpus-index half is honest bookkeeping, not calibration. C3 and C2 are causally separable: the patches commute and their effects add.

# C3 critic — design attack (round 47, BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd`)

Lane-authored advice, not closure. Artifacts:
- `.ufo/waves/round-47/build/C3CriticDesign.patch`: a prototype of the smallest safe correction (sha256 `b5f5a824…62bd9`). It changes `verifiers/verify_skill_checklist.py` only, +113/−10.
- `.ufo/waves/round-47/build/C3CriticDesign.probes.json`: the raw probe output (sha256 `1b047dc3…5678a`).

## Axes
- **Calibration:** the records must match repo state without making the gate weaker.
- **Operability:** the counting commands have to be runnable and the gate output has to be readable.
- **Freshness:** this claim doesn't touch freshness. No substrate is involved.

## F1. The record is true and the instrument is wrong
`LOG.md:2111` says the census replay command `python3 .ufo/round-45/drafts/v10/post-r44-hunt.py` "exited 2 because the referenced runners are absent".

- `git log --all --oneline -- .ufo/round-45/drafts/v10/post-r44-hunt.py` returns 0 commits, and the file isn't on disk. A `find / -xdev` and a `find /fast` turned up 0 hits.
- That token is the only dead subject among the 805, and it appears only at LOG.md:2111 (probe `A0_base`, `token_occurrences_as_subject`).
- The gate (`verifiers/verify_skill_checklist.py:1454-1495`, constants `:347-349`) can't read a recorded absence. Its only exclusions are same-line double quotes and the two schematic forms (`:179-185`, `:215-221`). Because LOG is append-only, those exclusions can't be applied after the fact.

So this is a false red, and repairing it is instrument calibration, not record editing.

## F2. Option (c), leaving the gate red as honest debt, removes the gate's sensitivity
**Probe result (`C_masking`):** I appended a new live-promise dead citation to a copy of LOG. The status went from FAIL to FAIL and the exit code didn't change (`status_changed: false`); only the detail text changed.

**History shows the same masking:**
- `LOG.md:1743` records exactly one failure (at `LOG.md:1618`).
- `LOG.md:1849` and `LOG.md:1972` record seven dead R44 draft citations (`1649`, `1655`, `1657`, `1661`, …) after drafts were pruned. Going from 1 to 7 dead subjects never changed the gate verdict.
- "Pre-existing" red runs were logged as normal at `LOG.md:1582`, `1743`, `1849`, `1972`, `2149` and `2303`.

Option (c) is honest about the debt, but it switches off the gate for every later round. I reject it.

## F3. Option (b), same-line absence detection, weakens the gate
I used the vocabulary regex `absent|missing|do(es) not exist|not found|never committed|pruned|deleted|removed|no longer exist`.

- At BASE, 121 subjects sit on 56 matching lines, and 120 of them resolve. Those 120 would lose coverage, and the evaluated count would drop from 805 to 684.
- A planted line, "runner `corpus/knowledge/r47-absent-a.md` is absent; rerun evidence in `corpus/knowledge/r47-planted-live-promise.md`", carries two dead tokens and still PASSes (`B_on_planted`).

I reject (b).

## F4. Strongest counterexample: in-place laundering reaches the same after-counts
Each of these single-line edits to `LOG.md:2111` gives `PASS 804` under the BASE gate (`in_place_evasion`):
- de-rooting the token to `drafts/v10/post-r44-hunt.py`;
- wrapping the code span in `"…"` (the quoted count goes from 9 to 10);
- swapping a path segment for `…` (the schematic count goes from 3 to 4).

This is not hypothetical. Commit `50507ca` (round 45) rewrote `LOG.md:1649`, `1655` and `1657` in place, de-rooting `.ufo/round-44/drafts/v2/probe.py` to `drafts/v2/probe.py`, with this diff:

```
git diff -U0 50507ca^ 50507ca -- LOG.md
@@ -1649 +1649 @@
```

The de-rooted form survives at `LOG.md:1978` and `1985`. It escapes the root set described in the limit at `:209-214`, and the citation becomes un-navigable.

So the plan's after-target ("10/10, 0 DRIFT, 0 DRIFT", `plans/round-47.md:34-39`) can't distinguish calibration from laundering.

## F5. What a pinned, fail-closed erratum looks like
To key the row, I used (line, sha256 of the line text, token, absence wording) plus a horizon.

**Why a token-only key fails:** it passes a new line that promises "Rerun passes: `python3 <same token>` exit 0" (`same_token_new_live_promise_token_keyed`: PASS).

**Why line numbers alone aren't stable:** merge `78ee57e` removed `LOG.md:1206` (`@@ -1206 +1205,0`). The `LOG.md:1618` cited at `:1743` doesn't hold that text today. GovCensus also reports r46 receipts that cite 2112.

**The prototype** (`C3CriticDesign.patch`):
- The registry is an in-source constant, `GOVERNANCE_ERRATA` / `GOVERNANCE_ERRATA_HORIZON = 2315`, so it doesn't add a new JSON authority. Adding a row means a reviewed verifier diff, and that diff moves the checklist source SHA that LOG records each round.
- Rows apply only to LOG.md lines at or below the horizon. This answers C3SentinelErrata's attack ("append an absence line, hash it yourself"): a new line can't be excused without moving the horizon in source. Forward-dated absences use the existing same-line quote convention.
- Each row must match the line's SHA-256 and its absence wording, must name a subject on that line, and the path must still be dead. A stale or mismatched row FAILs.
- Excused subjects are counted in the detail as "N recorded absence(s) excused".

**Results in a canonical-layout scratch clone** (`/fast/scratch/kotoba-r47/C3CriticDesign/canon/kotoba-shokunin`, ancestors symlinked to the fleet root; it reproduces BASE exactly at 9/1, 805, 9 quoted, 3 schematic):

| Case | Exit | Result |
|---|---|---|
| Base | 0 | PASS, 804 evaluated, 1 excused |
| Planted new dead citation | 1 | FAIL, names LOG.md:2316 |
| Runner file restored | 1 | FAIL, stale |
| De-root in place | 1 | FAIL, line drifted |
| Quote-wrap in place | 1 | FAIL, line drifted |
| Mid-file insertion shifts lines | 1 | FAIL, drifted + 2112 named |
| Appended copy of the absence line | 1 | FAIL, names 2316 |

`--self-test` passes with 0 failures over 1605 assertions (1597 + 8 new hermetic arms). The floor for this instrument is 1597 and works as a minimum (`verifiers/floors-registry.json`, `check_assertion_floors.py:28-29`).

The pinned row is therefore strictly stronger than BASE for line 2111: the in-place launderings that pass at BASE now FAIL.

**Remaining tradeoff, which the judge must weigh:** a row is a reviewed exception, not an authentication. The absence wording is a reader affordance; the hash plus the still-dead test are what make it fail closed.

## F6. Separability from C2
I ran the matrix in the canonical scratch clone against the peer draft `.ufo/waves/round-47/build/C2CriticRule.patch`:

| Tree | Live exit | Pass / fail | Governance check | Self-test assertions |
|---|---|---|---|---|
| BASE | 1 | 9 / 1 | FAIL, 805 | 1597 |
| C3 only | 0 | 10 / 0 | PASS, 804 | 1605 |
| C2 only | 1 | 10 / 1 | FAIL, 805 | 1837 |
| C2 then C3 | 0 | 11 / 0 | PASS, 804 | 1845 |
| C3 then C2 | 0 | 11 / 0 | PASS, 804 | 1845 |

- Both orders apply cleanly (`git apply --check`), and the combined diffs are byte-identical (`369a32a9…07f7` in both orders).
- The deltas add up: +8 from C3 and +240 from C2.
- C2's new check (`no_xml_tag`) is PASS/2 in every tree, whether or not C3 is applied.

**Code paths that stay disjoint:**
- C2 touches `CHECK_IDS` (`:282-293`), which the fixture loop multiplies per fixture (`:1832-1846`).
- C3 touches `check_governance_citations`, the hermetic block (`:2023-2061`) and the docstring (`:179-185`, `:215-221`).

**One shared artifact:** the totals strings in `plans/round-47.md:39` ("10/10 (11/11 with C2)"). Attribute by check id, not by totals.

The corpus half shares `verifiers/corpus-baseline.json:13-15` (`tracked_files`) with any other round-47 corpus file:
- With my governance patch, `MistakeUnindexedLanding.patch` (README row plus expectation 58→59) gives integrity exit 0 and independent exit 0.
- `ScoutReadmeIndex.patch` pre-indexes three round-47 files that don't exist yet (expectation 62). It leaves `stale_patterns` and `missing_paths` at 3, and integrity and independent both exit 1.

The C3 corpus move should land as its own 58→59 refresh.

## Before→after counting commands that would falsify C3
Run these at the canonical path, or in a canonical-layout clone. In my plain `.../lane` scratch clone, the BASE checklist reads 7/3, with 25 dead `../` and `name_directory` failures, so a plain scratch clone can't produce these counts.

1. `python3 -B verifiers/verify_skill_checklist.py --json --check governance.citation_resolves` — before: FAIL 805. After: PASS, evaluated **exactly 804**, with "9 quoted", "3 schematic" and "1 recorded absence(s) excused". C3 is falsified if evaluated is below 804, or if the quoted or schematic counts over the BASE prefix change.
2. `git show c61a973:LOG.md | cmp - <(head -n 2315 LOG.md)` — must exit 0 (append-only prefix). Also `git diff c61a973 -- LOG.md | grep -c '^-[^-]'` must return 0. A nonzero result here falsifies C3 however green item 1 is.
3. Mutation arms (from the F5 table) must all exit 1 at the after-tree: a planted dead citation, the restored runner, a 1-byte edit of line 2111, and a past-horizon row.
4. `python3 -B verifiers/verify_skill_checklist.py --self-test` must exit 0 with at least 1597 assertions plus the new errata arms. Separately, `verify_skill_checklist.py --json` statuses should be compared per check id against C2-only and C3-only trees.
5. `python3 -B verifiers/verify_corpus_integrity.py --json` — must show `tracked_files` 59 = expect 59, `unindexed` 0 with `corpus/lessons/round-46-verifier-spotcheck.md` gone from `unindexed_detail`, and `report_total` 40 and `commit_total` 29 unchanged. If they change, the baseline note must name the row tokens responsible. Then `python3 -B verifiers/verify_corpus_independent.py --json` must show `unindexed` 0, exit 0.

## Commands run (exit codes)
- `verify_skill_checklist.py --help`: 0.
- Production repo, read-only module imports: `probe_c3.py` 0, `probe_evade.py` 0, `probe_tracked.py` 0. The last one found 0 subjects resolving only via untracked files and 24 `../` subjects.
- Scratch `lane` clone, checklist at `36ab0d3`, `f2f9ee1`, `04192c2` and `c61a973`: 7/3 each, exit 1, because of the location artifact described above.
- Canonical scratch clone:
  - checklist at BASE: exit 1, 9/1;
  - after the patch: exit 0, 10/0;
  - self-test: exit 0, 1605;
  - mutation arms as tabled in F5;
  - separability matrix as in F6;
  - corpus verifiers as in F6.
- `git log` and `git diff` were read-only in the lane.

## Disclosures
- I ran `python3 -B verifiers/check_assertion_floors.py --repo $PWD` in the production lane. My item didn't name it; it is self-test-driven. Output:
  - 8 PASS;
  - `harness_independent` timed out at 120 s, which I attribute to host load [INFERENCE];
  - the exit code wasn't captured (`tail` masked it).

  Afterwards `git status --short` showed only the pre-existing untracked `.ufo/waves/` and `plans/round-47.md`.
- For a few seconds my scratch `canon/` directory contained a symlink to the fleet root's `.git`. Git ran only inside the clone, which has its own `.git`. I deleted the symlink, and the fleet HEAD was unchanged (`879df5e`).
- No tools were installed or updated.

## Not checked
- Whether `SCORECARD.md` needs errata. My prototype limits rows to LOG.md, and SCORECARD rows should be reworded, as round 37 did.
- The `recheck:` line at `corpus/knowledge/harness-independent-round41-census.md:3`, which still instructs running the absent runner. It is corrected only by the annotation at `:115`, and no corpus gate checks `recheck:` commands.
- Whether round-47 LOG appends that cite untracked `.ufo/waves/round-47/…` would die in a clean canonical clone [INFERENCE: yes, unless committed].
- The C2 patch's own correctness.
- `verify_harness_claims.py`.
