# BaselineGatesA — no-harm baseline, part A (round-50 build)

**Result: BASELINE CAPTURED at `f3046466` — 7 of the 9 assigned runs exit 0; `verify_corpus_integrity.py --json` and
`verify_corpus_independent.py` exit 1 at the base commit with 4 and 2 DRIFTs, and `--box-proof` prints
`boxes proven 2` (exit 0) after deleting any one of the 6 must-fail cases — 0 of 6 killed, as the plan states.**

Run: 2026-10-22T12:34Z. Private clone at
`/fast/scratch/hyaku/kotoba-r50/build/BaselineGatesA/lane` and a fleet-shaped clone at
`.../BaselineGatesA/fleet/kotoba-shokunin`, both `rev-parse HEAD` = `f30464660c675d1c1e2851a3bf0366a3aaffe5a8`.
No file in the lane checkout was touched except this report; no jj command; no pacman/uv install.

## Supplying the fleet path and sibling repos

`verify_skill_checklist.py` needs two things the bare clone cannot give:

1. the repo directory named `kotoba-shokunin` — otherwise `trigger.name_directory` fails
   (`name 'kotoba-shokunin' != directory 'lane'`);
2. the fleet-root siblings `../.ufo` and `../PROTOCOL.md` — otherwise `trigger.citation_resolves` (SKILL.md:527)
   and `governance.citation_resolves` (LOG.md:177/255/311/779/974 …, +7 more) fail.

I supplied both without touching the lane: `.../BaselineGatesA/fleet/` holds a second clone named
`kotoba-shokunin` plus symlinks for every entry of `/home/vgpnk/Projects/shokunin` (20 `*-shokunin` lane repos and
the root files) and an explicit symlink `.ufo -> /home/vgpnk/Projects/shokunin/.ufo`. Note the trap: a `*` glob
does **not** include `.ufo`, so the first fleet-shaped run still failed the two citation checks; adding the dotfile
symlink moved the run to 11 PASS / 0 FAIL. The real lane checkout already has exactly this shape, so the raw-clone
red is a location artifact, not lane state.

`check_sibling_census.py` was run exactly as assigned (`--province PROVINCE.md`, default `--fleet
/home/vgpnk/Projects/shokunin`); it reads sibling repos read-only with `git show`. `verify_corpus_integrity.py`
and `verify_corpus_independent.py` need only the repo tree: `.ufo` is **tracked** in git at the base commit
(`git ls-files .ufo | wc -l` = 10333), so their result is identical in the raw clone and the fleet-shaped clone.

## Table — command, exit, summary line

| command (cwd = clone root) | exit | summary line |
|---|---|---|
| `python3 -B verifiers/verify_skill_checklist.py --json` (bare clone) | 1 | `pass 8 fail 3 na 0` — all 3 fails are location artifacts (above) |
| same (fleet-shaped clone) | 0 | `pass 11 fail 0 na 0` |
| `python3 -B verifiers/verify_skill_checklist.py --self-test` | 0 | `0 failure(s) over 1845 assertions` |
| `python3 -B verifiers/verify_corpus_integrity.py --json` | 1 | 4 DRIFT of 9 checks: `tracked_files 67 != 66`, `unindexed 1`, `report_total 44 != 43`, `report_dead 2` |
| `python3 -B verifiers/verify_corpus_independent.py` | 1 | `corpus.index.unindexed observed=1 DRIFT`, `corpus.pointers.report_dead observed=2 DRIFT`, last line `exit 1` |
| `python3 -B verifiers/check_assertion_floors.py` | 0 | 10/10 `PASS … observed==floor` (checklist 1845, dispatch 32, corpus_integrity 150, …) |
| `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md` | 0 | `rows 20 verified 20` / `province rows 20 matched 20` |
| `python3 -B verifiers/check_sibling_census.py --self-test` | 0 | `self-test: 0 failure(s) over 44 assertions` |
| `python3 -B verifiers/verify_dispatch_prompts.py --self-test` | 0 | `0 failure(s) over 32 assertions` |
| `python3 -B verifiers/verify_dispatch_prompts.py --box-proof --map verifiers/checklist-baseline.json` | 0 | `boxes proven 2` |
| supplementary: delete one must-fail case, rerun `--box-proof` (6 runs) | 0 (×6) | `boxes proven 2` every time |

## Findings

1. **The base commit is red on corpus integrity, and it is not a clone artifact.** Both trees measure the same four
   DRIFTs, and three of them come from one file: `corpus/lessons/round-49-verifier-spotcheck.md` is committed at
   base (20,598 bytes) but has no `corpus/README.md` index row — row 70 indexes `lessons/round-49.md` only. That
   single omission produces `unindexed 1`, `tracked_files 67` against the re-recorded baseline 66, and
   `report_total 44` against 43. This is the round-47 M21 class ("unindexed closure landing") repeating.
   It also contradicts the spot-check's own no-harm line, "Corpus integrity moves from 4 DRIFT to 1 DRIFT"
   (`corpus/lessons/round-49-verifier-spotcheck.md:140`): that was measured at `c48793d`, before the spot-check
   file itself landed. The fourth DRIFT (`report_dead 2`) is the acknowledged round-48 closure pointer
   `.ufo/reports/round-48/kotoba.md`, which exists at the fleet root but not in the repo —
   `git cat-file -e f3046466:.ufo/reports/round-48/kotoba.md` exits 128.
   Consequence for this build wave: the no-harm comparison must start from f3046466's measured state (this table),
   not from "1 DRIFT". Indexing the spot-check file would also move `tracked_files` and `report_total`, so it must
   be done with the floors bump-in-step rule or explicitly declared as drift.

2. **Operability baseline is exactly the plan's before-value.** `verifiers/fixtures/dispatch-prompts/manifest.json`
   holds 9 cases, 6 of them must-fail: `d04-placeholder` (`report_path_literal`), `d04-stem`
   (`report_stem_is_lane_id`), `d04-unknown-lane` (`lane_identity_known`), `d08-role-round`
   (`filename_role_round_equal`), `d08-report-dir-round` (`filename_report_dir_round_equal`), `d08-above-state`
   (`round_le_latest_dispatched`). Deleting each in turn from a scratch copy and rerunning `--box-proof` gave
   `boxes proven 2`, exit 0, six times. The fixture half of `box_proof` therefore does not enforce case coverage.
   The D2 stale wording is present verbatim: `box_proof` docstring (lines 41-43) "A file's verdict is FAIL if any
   conjunct FAILs…" beside the fixture claim, and the `--box-proof` help at line 488 "discriminate every conjunct".

3. **Adjacency baseline: 5 of 9.** Plan counter over the SKILL.md frontmatter at the base commit prints `5`, names
   `kagi kake kasegi kengaku kumitate`. The census classifies 9 rows `adjacent` (`chousa, kagi, kake, kama, kasegi,
   kengaku, kotodama, kumitate, tameshi`), 8 `none`, 3 `NONE` (the no-SKILL.md rows) and **0 `contested`** — so the
   9-lane target is the adjacent set, exactly the 4 missing names `chousa, kama, kotodama, tameshi`.

4. **The assigned census run cannot see the description at all.** The base guard's `--help` offers only `census`,
   `--fleet`, `--province`, `--self-test`; there is no `--skill` arm. So `--province PROVINCE.md` exits 0 today no
   matter what the description says: the C1 content guard (Q25) does not exist yet and must add the arm, the red
   fixture, and a self-test assertion. The guard is also absent from `verifiers/floors-registry.json`, whose 10
   instruments are `checklist, compare_harness_independent, corpus_independent, corpus_integrity, floors_guard,
   harness, harness_independent, pins, surfaces, dispatch_prompts` — D3's registry item confirmed.

5. The census self-test's 44 assertions and the dispatch self-test's 32 assertions are counted by
   `check_assertion_floors.py`, which is green: nothing in this baseline is below its floor.

## Not established here

- I did not run `check_substrate_pins.py`, `verify_surfaces.py` or `verify_harness_claims.py`; the round-49
  spot-check records them as red from host state (omp 18.12.6) at both base and head.
- I did not attempt a fix for the unindexed spot-check file, the 0-of-6 box-proof bound, or the missing `--skill`
  arm: this item is baseline only.
- The scratch fleet symlink tree is disposable; it lives at
  `/fast/scratch/hyaku/kotoba-r50/build/BaselineGatesA/fleet` and is not part of any patch.

## Evidence (verbatim tails)

Bare-clone checklist failures (exit 1, `pass 8 fail 3`):
`trigger.name_directory: name 'kotoba-shokunin' != directory 'lane'`;
`trigger.citation_resolves: line 527: '../.ufo/reports/round-7/kotoba.md' does not resolve`;
`governance.citation_resolves: LOG.md:177 … (+20 more)`.

Box-proof deletion probe (scratch):
```
deleted=d04-placeholder       exit=0 out=[boxes proven 2]
deleted=d04-stem              exit=0 out=[boxes proven 2]
deleted=d04-unknown-lane      exit=0 out=[boxes proven 2]
deleted=d08-role-round        exit=0 out=[boxes proven 2]
deleted=d08-report-dir-round  exit=0 out=[boxes proven 2]
deleted=d08-above-state       exit=0 out=[boxes proven 2]
```

C1 counter at base:
```
git show f3046466:SKILL.md | awk 'NR==1&&/^---$/{f=1;next} f&&/^---$/{exit} f' \
  | grep -oiwE 'chousa|kagi|kake|kama|kasegi|kengaku|kotodama|kumitate|tameshi' | sort -u | wc -l
5
```

Corpus integrity DRIFTs (identical in both trees):
```
DRIFT corpus.index.tracked_files obs=67 exp=66
DRIFT corpus.index.unindexed obs=1 exp=0 / empty      # corpus/lessons/round-49-verifier-spotcheck.md
DRIFT corpus.pointers.report_total obs=44 exp=43
DRIFT corpus.pointers.report_dead obs=2 exp=0 / empty
DRIFT_COUNT=4 OF 9
```

No web source was opened; no tool was installed or upgraded.
