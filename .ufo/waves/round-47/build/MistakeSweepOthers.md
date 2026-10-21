verdict: r46 left eleven record defects outside M1–M19 — the worst is that the lesson's own evidence pointers are stale at BASE (M2 and M13 were wrong at birth; M5/M12/M7/M10 rotted when the landing commit shifted the lines), and the paragraph that certifies M7/M10 "still hold at HEAD" is false in the very commit that carries it; all are line/ref citations that no gate resolves because `governance.citation_resolves` tests path existence only.

# Scope and method

Targets: `LOG.md` § Round 46 (BASE lines 2001–2315), `corpus/lessons/round-46.md` (81 lines), `corpus/lessons/round-46-verifier-spotcheck.md` (17 lines), `corpus/SOURCES.md`, `corpus/QUALITY.md`, `SCORECARD.md`, `SKILL.md`, `SHONEN.md`, `README.md`, `.ufo/round-46/evidence/**` cited pins, and the fleet-root integrator report `/home/vgpnk/Projects/shokunin/.ufo/reports/round-46/kotoba.md` (the lane copy `.ufo/reports/round-46/` does not exist — confirmed `ls` exit 2).

Method: re-ran every pointer command in the M-table and the § Gate table at BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd`; where a command names `HEAD` without a ref, also ran it at the r46 commits `78ee57e` (merge of WIP `36ab0d3`) and `f2f9ee1` (landing) to separate "wrong at birth" from "rotted at landing". Every claim below is a command output I observed; the one inference is marked `[INFERENCE]`.

# Findings (not in round-46.md ## Mistakes M1–M19)

## N1 — M2's evidence pointer was wrong at birth (`SCORECARD.md:80` vs `:76`)

- BASE `corpus/lessons/round-46.md:20` (M2) cites `SCORECARD.md:80` for the quote "complete-census condition is UNMET".
- `grep -n 'complete-census condition is UNMET' SCORECARD.md` → `76:**Round 41 completed…` (exit 0).
- `sed -n '80p' SCORECARD.md | grep -c 'complete-census'` → `0` (grep exit 1). Line 80 is the *round-41 calibration annotation* (seat denominator), a different quote.
- Checked at write time: `git show 78ee57e:SCORECARD.md | grep -n 'complete-census condition is UNMET'` → `76:`; `git show 78ee57e:SCORECARD.md | sed -n '80p' | grep -c complete-census` → `0`. So this is not landing rot — the pointer never resolved.
- Counterexample considered: line 80 is cited correctly by M6 (`scout fragments, not proof of 41 declared/complete seats` does live there), so the two rows collided on one line number and M2 lost.
- Fix: cite the anchor text, not the line (`SCORECARD.md` § Round 41 completed).

## N2 — M5's two pointers rotted at the landing commit (`:165`→`:173`, `:100`→`:108`)

- BASE `corpus/lessons/round-46.md:23` (M5) cites `SCORECARD.md:165` (row 38, "None-path crash…") and `SCORECARD.md:100` (round-38 entry).
- At `78ee57e` both resolve exactly: `git show 78ee57e:SCORECARD.md | sed -n '100p;165p'` → the Round-38 completed entry and `| 38 | operability | 8.5 — … None-path crash …` (exit 0).
- At BASE they are `SCORECARD.md:173` and `:108`; `sed -n '165p' SCORECARD.md` is now row 33 (operability, box-map), and `sed -n '100p'` is `**Next: round 47**`.
- Root cause: `f2f9ee1` is a net +8 lines above line 100 (the round-46 scoreboard rows at `:28`/`:31`/`:33`); every SCORECARD line citation below that point shifted by +8. Same command family as M3's class, but the instance is new and lives in the lesson's own evidence cells.
- Counterexample: the fleet report's SCORECARD citations (`:28/:31/:33/:98/:100/:227-229/:283`) still resolve at BASE (`git show f2f9ee1:SCORECARD.md | sed -n …` byte-equal to BASE for those lines), so the rot is confined to citations below the inserted block.

## N3 — M13's `SKILL.md:15` is off by one; the token is on `:14`

- BASE `corpus/lessons/round-46.md:31` (M13) says "`SKILL.md:15` description carries the literal `<skills>` token".
- `sed -n '14p' SKILL.md | grep -c '<skills>'` → `1` (exit 0); `sed -n '15p' SKILL.md | grep -c '<skills>'` → `0` (exit 1). Line 15 is "router-visible." (the wrapped tail of the description); line 16 is the closing `---`.
- Same at `78ee57e` (`git show 78ee57e:SKILL.md | sed -n '14p'`) — wrong at birth, not rot.
- Relevance to r47 C2: the planned "grep the description block" check is correct (the token is inside the description), but any check keyed to line 15 would pass vacuously. The C2 fixture should scan the frontmatter span, never a fixed line.

## N4 — M12's `SHONEN.md:7-15` is out of range at BASE

- BASE `corpus/lessons/round-46.md:30` (M12) cites `SHONEN.md:7-15` for the PROTOCOL.md:65 attribution note.
- `wc -l < SHONEN.md` → `12`. At `78ee57e`, `git show 78ee57e:SHONEN.md | sed -n '7,15p'` contains `PROTOCOL.md:65` (exit 0) — true then, out of range now because the file was regenerated 50→12 in `f2f9ee1` (`git show 78ee57e:SHONEN.md | wc -l` → `50`; `git show f2f9ee1:SHONEN.md | wc -l` → `12`).
- Counterexample: `grep -c PROTOCOL SHONEN.md` → `1`, so the note survives; only the range is dead.

## N5 — M7/M10's `git show HEAD:` commands no longer reproduce, and the paragraph certifying them is false in its own commit

- BASE `corpus/lessons/round-46.md:25` (M7): "`git show HEAD:SHONEN.md | wc -l` → 50". At BASE that command returns `12` (exit 0); 50 is only true at `78ee57e` or earlier.
- BASE `corpus/lessons/round-46.md:28` (M10): "`git show HEAD:README.md | sed -n '6p'` → `**Domain:** >`". At BASE it returns the fixed line `**Domain:** prompt & skill craft — scopes SKILL.md/AGENTS.md quality, trigger fidelity`; `**Domain:** >` is only true at `78ee57e`.
- BASE `corpus/lessons/round-46.md:39-41` (closing paragraph): "M7 and M10 still hold at HEAD bytes, but L1's worktree regeneration (`SHONEN.md`, `README.md`) is uncommitted — the rows record both states."
  - `git rev-parse f2f9ee1:corpus/lessons/round-46.md` → `0efa038b88537f078e15146fd646c7fa7c5a64d5`; `git rev-parse HEAD:corpus/lessons/round-46.md` → same blob. The sentence is committed.
  - `git show f2f9ee1:SHONEN.md | wc -l` → `12`; `git show f2f9ee1:README.md | sed -n '6p'` → the fixed line; `git show --name-only --format='' f2f9ee1 | grep -E 'SHONEN.md|README.md'` → both files are in the landing commit.
  - So the paragraph asserts "still hold at HEAD bytes … uncommitted" inside the commit that commits the regeneration. This is the M3 class (record-vs-tree drift) reappearing in the lesson's *correction* paragraph, and it is not one of M1–M19.
- Counterexample that would rescue it: a commit ref in the sentence. There is none; `HEAD` is the only ref, which is why the sentence rots.

## N6 — the lesson's LOG range stops before the round's own landing entries

- BASE `corpus/lessons/round-46.md:6`: "Evidence: `LOG.md` § Round 46 entries (`LOG.md:2001-2298`)".
- `git show 78ee57e:LOG.md | wc -l` → `2298` — exact at write time.
- `git show f2f9ee1:LOG.md | wc -l` → `2310`; `wc -l < LOG.md` → `2315` at BASE. The range now excludes `LOG.md:2300` ("Round 46 landing…") and `LOG.md:2312` ("Round 46 landing pin and after-battery") — the two entries that carry the verdict and the after-battery.
- `sed -n '2298p' LOG.md` → `  Documentation-only change; no round run, no axis moved.` (the tail of the Devin-wiki entry, not a Round 46 heading), so the end line also points at the wrong content.
- Fix pattern: cite the heading anchor (`## 2026-10-19 — Round 46 landing …`) or a content hash, never an end line in an append-only file.

## N7 — the S001–S008 timestamp label defect is disclosed but uncaptured and uncorrected

- BASE `corpus/lessons/round-46.md:63-70` (S001–S008 rows, header `accessed (UTC)` at `:61`) record `2026-10-19T18:40:53Z`–`18:40:55Z`; the lesson's own prose at `:77` says those values are local time (UTC−3) labelled `Z`; the fleet report repeats it at `/home/vgpnk/Projects/shokunin/.ufo/reports/round-46/kotoba.md:121`.
- The artifact still carries the mislabel at BASE: `python3 -c "import json; print([r['accessed_utc'] for r in json.load(open('.ufo/round-46/evidence/w2/sources/fetch-log.json'))['rows']][:8])"` → the same eight `18:40:5xZ` strings (exit 0).
- No instrument reads the field: `grep -rn 'accessed' verifiers/` → no output (exit 1). `corpus/SOURCES.md` stores a date-only `opened` column (`:14-21`), so the wrong hour does not propagate into the registry — the defect lives only in the lesson table and the fetch log.
- Corroboration [INFERENCE]: the same table records S009/S010 at `21:42Z` (`:71-72`), ~3 h later in label terms for work that the seat did in one sitting; `corpus/SOURCES.md` first appears at `f2f9ee1` (`git show 78ee57e:corpus/SOURCES.md | grep -c '^| S0'` → `0`; `git log --format='%h %cI' -- corpus/SOURCES.md` → `f2f9ee1 2026-10-19T19:29:36-03:00` = `22:29:36Z`). A 18:40 *local* fetch (21:40Z) sits inside the landing window; an 18:40 *UTC* fetch (15:40 local) would predate the WIP commit `36ab0d3` (17:08-03) by ~1.5 h. I cannot decide the clock from artifacts alone; the lesson's `date -u` re-derivation is the only direct evidence and it is not recorded verbatim.
- Scope understated: the lesson's prose (`:77`) confines the defect to S001–S008, but S011 (`:73`, the rejected community row) carries the same `2026-10-19T18:40:55Z` label. The fetch log agrees — `[r['accessed_utc'] for r in …]['rows']` returns the same 18:40 values for all nine fetched rows.
- Calibration gap: the row class that would catch this (a timestamp must carry the zone it was taken in) exists nowhere in `corpus/QUALITY.md` Q01–Q18, and the M-table has no row for it. r47's erratum registry should decide whether an erratum *record* is enough or whether the artifact must be corrected.

## N8 — C2's arm count is recorded as six and as seven, and no side names its command

- Six: `SCORECARD.md:228` → `| 46 | operability | 8.5 — six registered shadow/duplicate arms exit 0 | 8.5 (held) — six arms exit 2 class-named…`; `LOG.md:2255` → "six named shadow/duplicate fixtures pass on the current snapshot".
- Seven: fleet report `:58` heading "Registered arms, frozen → landing:" followed by seven rows, the seventh at `:68` `| nested duplicate member | 0 | 2 |`; spotcheck `corpus/lessons/round-46-verifier-spotcheck.md:17` → "7 named bad-input cases 0→2 reject".
- Evidence reconciles the difference: `.ufo/round-46/evidence/w2/c2/summary.json` matrix has `live_shadow_arms` = 4 and `raw_duplicate_member_arms` = 2 (union 6); `.ufo/round-46/evidence/w2/l1-matrix/snapshot3/results.json` adds `raw-nested-duplicate-value` (0→2) and keeps `live-summary-and-mirror-optout` at 0→0. Flipping arms = 4 live + 3 raw = 7; the eighth case is the opt-out control. (Counts read via `python3 -c` over the two JSONs, exit 0.)
- Why it is a defect: the seven-row table is headed *Registered* arms, but `.ufo/round-46/claims.json` C2 registers only the two raw shapes "duplicate top-level `results`" and "duplicate per-record `re_derived`" — the nested arm is an extra measured arm. Six is the registered count, seven is the measured count; the report and spotcheck use 7 under the label "registered", SCORECARD uses 6 under the same word. The spotcheck's 7 carries no command.
- Counterexample: if claims.json's C2 text were read as "the raw duplicate-member door" generically (not two named shapes), 7 would be the registered count and SCORECARD would be the undercount. Either reading leaves one record wrong; the fix is to print the command and the case list.

## N9 — M8's live-carrier count no longer reproduces (same class as M19, unlabelled)

- BASE `corpus/lessons/round-46.md:26` (M8): `grep -c kotoba ../SCORECARD.md` → 38, and first lines "# kotoba-shokunin — Iteration Log"/"Scorecard".
- At BASE: `head -1 /home/vgpnk/Projects/shokunin/LOG.md` → `# shokunin (main repo) — Iteration log`; `head -1 /home/vgpnk/Projects/shokunin/SCORECARD.md` → `# shokunin (main repo) — Scorecard`; `grep -c kotoba /home/vgpnk/Projects/shokunin/SCORECARD.md` → `26` (exit 0).
- The row's *point* (fleet-root identity does not name the child lane) still holds; the count is a snapshot of a file other lanes rewrite. This is M19's failure mode applied to a fleet-root file, measured one round before M19 was written, with no snapshot pin or digest in the row.

## N10 — M19's `captured-by Q10` does not express M19's rule

- BASE `corpus/lessons/round-46.md:37` (M19) is grounded in `Q10` per `corpus/QUALITY.md:21`: "A measurement names the source sha256 before and after; a source that moves during the run invalidates the result."
- In the M19 race the comparator bytes were stable; the moving carrier was the *input* directory (`$HOME/.omp/agent/sessions`). A measurement can satisfy Q10 (source sha named, unchanged) and still take the false blocker. The fix that actually catches M19 — "measure on a frozen carrier snapshot (`cp -a`, listing digest)" — appears only in M19's own fix cell, in no Q row.
- `corpus/QUALITY.md` has 18 rows and none mentions a snapshot, a frozen input carrier, or a listing digest: `grep -cE 'snapshot|frozen carrier|listing digest' corpus/QUALITY.md` → `0` (exit 1).
- Impact on r47 C3: the erratum registry inherits this gap — a fail-closed registry that records *why* the citation gate is red must also pin the input carrier, or the same false-red recurs on the next live measurement.

## N11 — S009 names the wrong commit as "the round-46 landing commit"

- `corpus/SOURCES.md:22` (S009): "The comparator's own self-model at the round-46 landing commit … commit 78ee57e".
- The round's own records name `f2f9ee1` as the landing (`LOG.md:2300`, "landing commit `f2f9ee1`" at `LOG.md:2312`; lesson `:6` names `36ab0d3` merged by `78ee57e`). `78ee57e` is the merge of the WIP.
- The *measurement* is correctly pinned (328 assertions holds at `78ee57e`; the landing bumped to 330), so only the label is wrong. The lesson's § Gate cell additionally says "file sha256 at HEAD `ccf41c23…`" (`:71`); `git show HEAD:verifiers/compare_harness_independent.py | sha256sum` → `778b367e…` at BASE, `ccf41c23…` only at `78ee57e` — another unpinned-`HEAD` citation.
- Counterexample: the same row's own text "Final line 'self-test: 0 failure(s) over 328 assertions'" is true at `78ee57e`; a reader who takes "landing commit" literally would get 330 and think the row was false.

# Sweeps that found no additional instance (commands + outputs)

Run from the lane root at BASE; exit codes as shown.

| sweep | command | result |
|---|---|---|
| M-table size | `grep -c '^| M' corpus/lessons/round-46.md` | `19` (M1–M19, no gaps) |
| cited r46 evidence paths | `for p in .ufo/round-46/scouts/w2-reviewer.md .ufo/round-46/scouts/w2-critic.md .ufo/round-46/evidence/w2/l1-matrix/med3 .ufo/round-46/evidence/w2/l1-matrix/race-fresh2/results.json .ufo/round-46/evidence/w2/c1/summary.json .ufo/round-46/evidence/w2/c2/summary.json .ufo/round-46/evidence/w2/gates/meas-tree.sh; do test -e "$p" && echo present || echo MISSING; done` | 7/7 present |
| lesson hash pins | `sha256sum .ufo/round-46/scouts/C1.md .ufo/round-46/claims.json verifiers/verify_skill_checklist.py` | `d20b34c9…` / `ff60fce9…` / `214ae44d…` — all match the lesson (S010's file sha identical at `78ee57e` and BASE) |
| fleet-report hash pins | `sha256sum .ufo/round-46/evidence/w2/{c1,c2}/summary.json .ufo/round-46/evidence/w2/l1-matrix/snapshot{2,3}/results.json` | `8e4b9856…`, `ae14fdf0…`, `779c38d5…`, `bbe11ad0…` — all four match the report |
| after-battery stdout pins | `cat .ufo/round-46/evidence/w2/gates/after-f2f9ee1/summary.txt` | `surfaces … 8432070a…`, `pins … 16e71a19…` — match the report's byte-identical claim |
| M6 commands | `git show b1be35f:.ufo/round-40/claims.json \| grep '"seats"'`; `git ls-tree -r --name-only b1be35f -- .ufo/round-40/scouts/ \| wc -l` | `"seats": 40`; `41` — reproduces |
| M1 MANIFEST rows | `python3` over `/home/vgpnk/Projects/shokunin/MANIFEST.json` (`lanes` contains kotoba) | rounds 39–45 all present — reproduces |
| M16 | the lesson's verbatim `for f in corpus/knowledge/*.md; do …` one-liner | `32` missing of `34`; 2 with `source:` — reproduces |
| M12 file census | `ls corpus/lessons/ \| grep -E 'aggregator\|box3' \| wc -l` | `6` — reproduces |
| M13 gate-limit line | `grep -n 'structural parse' verifiers/verify_skill_checklist.py` | `76:` — reproduces |
| M14 pointers | `sed -n '2043p;2178p;2201p' LOG.md` | concurrent comparator change / `T1-after-landing-13` exclusion / N1 superseded — all match |
| M19 numbers | `grep -n '1127\|1131' .ufo/round-46/scouts/w2-reviewer.md` | line 37, `candidate_blocks:1127 → 1131` — reproduces |
| SOURCES census | `grep -c '^\| S0' corpus/SOURCES.md`; status column tally | 11 rows; mined 4 / queued 6 / rejected 1 — matches `LOG.md:2315` |
| SOURCES count command from the report | `grep -cE '^\|[\[:space:]]*S[0-9]{3,}[\[:space:]]*\|' corpus/SOURCES.md` | `11` at BASE and at `f2f9ee1` — reproduces |
| PROVINCE / README line refs | `sed -n '8p;16p;23p' PROVINCE.md`; `sed -n '64p' corpus/README.md` | `## Core`, `## Frontier`, `## Adjacent`, `## Frontier` — all match the report |
| comparator repair site | `sed -n '233p' verifiers/compare_harness_independent.py` | `def extract_json(text):` — matches the report |
| SCORECARD citations in the fleet report | `git show f2f9ee1:SCORECARD.md \| sed -n '28p;31p;33p;98p;100p;227,229p;283p'` | all eight resolve at BASE too |
| dead recheck beyond `LOG.md:2111` | `grep -rln 'post-r44-hunt.py' corpus/knowledge/ corpus/lessons/ LOG.md` | 3 files, all the *same* known runner (`corpus/knowledge/harness-independent-round41-census.md:3,53,115`); no second dead runner found |
| knowledge three-field rule | verbatim M16 loop + `ls corpus/knowledge/*.md \| wc -l` | 32/34 missing, 34 files — same as M16 |

# Why these survived: the gate only resolves paths

`verifiers/verify_skill_checklist.py:1431` `citation_resolve()` ends in `(base / …).exists()`; `governance.citation_resolves` (`:179`) is "the same existence predicate over repo-root". It caught `LOG.md:2111` because `.ufo/round-45/drafts/v10/post-r44-hunt.py` (a *path*) is absent. It cannot see `SCORECARD.md:80`, `SKILL.md:15`, `SHONEN.md:7-15`, `LOG.md:2001-2298`, or a `git show HEAD:` claim — every finding above is a line/ref citation, not a path. This is the concrete shape the r47 C3 erratum registry must close: a registry entry that pins *content* (hash or quoted phrase) and fails closed when the bytes at the cited location change, otherwise the same rot recurs silently next round.

# What I did NOT check

- Did not execute any r46 measurement arm (comparator joins, C1/C2/C3 matrices, floors, self-tests) — lane-wide gates are outside this leaf's contract, and the before-state is already recorded in `.ufo/waves/round-47/before/SUMMARY.md`. The pin checks above are hash/JSON reads, not replays.
- Did not inspect `.ufo/round-46/drafts/**` or `evidence/**` beyond the files cited by the lesson, the report, and the SCORECARD rows (8170 tracked files under `.ufo/round-46` at BASE).
- Did not verify URLs or quotes against the network; S001–S011's `fetched sha256` values are taken as recorded.
- Did not decide whether the S001–S008 clock is provably local: the only direct evidence is the lesson's own `date -u` re-derivation, which is not recorded verbatim. N7's mechanism is `[INFERENCE]`; the mislabel's persistence in `fetch-log.json` and the absence of any consumer are observed.
- Did not audit the fleet-root strays (28 files the reviewer wrote) — they were cleaned before BASE, and the fleet root is outside this lane.
- Did not read `LOG.md` entries 2001–2298 in full line-by-line; citations were resolved by content match at the referenced lines, and entry-level prose was skimmed for counts (all r46 counts named in the LOG that I re-ran reproduced except the ones listed above).
- No tool installs or upgrades were needed (nothing installed; no pacman/uv/npx transaction ran).

# Files

- This report: `.ufo/waves/round-47/build/MistakeSweepOthers.md`
- No patch and no JSON artifact: all writes are read-only checks; nothing in the lane tree was modified.
