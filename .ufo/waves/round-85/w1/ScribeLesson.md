# ScribeLesson — round 85 w1 (lesson, log entries, r84 correction, Q-criterion)

Seat: ScribeLesson. Round 85 attempt 1, lane kotoba-shokunin, host linux, 2026-11-04.
Scope: `corpus/lessons/round-85.md` (new), `LOG.md` (append-only), the append-only
`## Correction, round 85` block in `corpus/lessons/round-84.md`, and the appended
`Q76` criterion row in `corpus/QUALITY.md`. Leaf member — no subagent dispatch.

## Files written

| path | what |
|---|---|
| `corpus/lessons/round-85.md` | the round-85 lesson: intro (base `1c8f37edf2e5ac0fb3c2be1c88e32406313fe47b`, freeze `f822dd113fe9f58661dd642dc207669581a4ab57`, the two claims), `## Gate` (S213 opened live with the five located quotes and their counting commands; census before/after; rows added 0; the S213 `used-by` old→new; frontier rows advanced 0; the C1 and C2 predicates verbatim with their base readings; the three records this round touched), `## Mistakes` (four rows), `## Ruled out` (three items with reasons), and three append-only `## Correction (round 85, …)` blocks (the r84-D1 count, the wave's attack-role accounting, the C1 disposition). |
| `corpus/lessons/round-84.md` | `## Correction (round 85, append-only; r84-D1 — the "10 FAIL instruments" count)`: the measured **11** `FAIL` rows with both counting commands; the r84 text is not rewritten. 18 insertions, 0 deletions. |
| `corpus/QUALITY.md` | `Q76` appended (never renumbered): a count quoted from another artifact's rows names that artifact and the row-selection rule, not only the number, and carries its counting command. 2 insertions, 0 deletions. |
| `LOG.md` | four appended entries: C1 (killed before data), C2 (measured), intake (S213 re-open + merge/kotoba adoption through this lane's gate + considerthese proposal 3), and the registry-conformance / routed-defect entry (CRLF repair, seven index rows, the pre-existing reds, the r84-D1 closure, the attack-role accounting correction). 126 insertions, **0 deletions**. |
| `.ufo/waves/round-85/w1/ScribeLesson/receipts/` | `lesson-measurements.txt`, `r84-d1-counting.txt`, `pre-existing-reds.txt` — the commands and observed output this seat ran. |
| `.ufo/waves/round-85/w1/ScribeLesson.md` | this report. |

Scratch `/fast/scratch/hyaku/kotoba-r85/ScribeLesson` was removed on exit.

## Evidence (commands + observed output)

- **S213 opened live** — `curl -sL -o "$S/page.md" -w 'HTTP %{http_code} size %{size_download}\n' https://agentskills.io/skill-creation/optimizing-descriptions.md` → `HTTP 200 size 13403`;
  `sha256sum` → `7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837`;
  `cmp` against the committed `.ufo/waves/round-76/snapshots/optimizing-descriptions.md` → identical.
  Every one of the seven quotes the lesson carries was checked **verbatim** against
  the scout packet: `IN-PACKET IN-LESSON` for all seven (quotes (a) 10 words, (b) 21,
  (c) 13, (c2) 23, (d) 9, (e) 21, and the line-92 negative pass criterion 12).
  Each word count is re-derived in the lesson with a `grep -o … | wc -w` command
  against the committed snapshot (Q54 requires the command beside the count).
- **Census before** — `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` → exit **1**, 180 E12 rows
  (`.ufo/waves/round-85/receipts/census-round-start.txt`).
  **Census after** — the same command → exit **0**, 33 W04 rows, 0 E rows, last line
  `kotoba ok /home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md`;
  `… validate --file corpus/SOURCES.md` → exit **0**, `file ok`.
  Row count `grep -cE '^ {0,3}\| S[0-9]{3}' corpus/SOURCES.md` → 180 before, 180 after.
- **S213 `used-by` old→new** — a cell-by-cell diff of the base row against the landed
  row shows exactly one differing cell (index 11, the `used-by` cell): `corpus/knowledge/skill-eval-artefacts-round70.md` →
  `corpus/knowledge/skill-eval-artefacts-round70.md, corpus/knowledge/description-trigger-discipline-round85.md`;
  13 pipe-separated fields both sides.
- **C1 base reading** — `python3 -B verifiers/check_description_render.py --rev 1c8f37edf2e5ac0fb3c2be1c88e32406313fe47b` →
  `description render rules met 4 of 8`, exit 1 (R1 151 > 99; R4 no `use this skill when`; R6 eval set absent; R8 entry absent).
- **C2 base and after** — base: pins exit 2 `UNREADABLE 2/3 pins failed: omp_binary_sha256, omp_binary_mtime`,
  surfaces exit 2 `omp binary not found: /home/vgpnk/.local/bin/omp.real`.
  After at `bf9ab28e011e4243356078951e33d919ad63a0c5`: pins exit 0 `OK 3/3 pins hold`
  (mtime delta 0 ns at tolerance 0 ns), surfaces exit 0 `"pass": 7`, `"fail": 0`
  (`.ufo/waves/round-85/receipts/c2-after.json`); re-measured at the tip by this seat with the same two commands, same readings.
- **r84-D1 count** — `grep -c '^FAIL' .ufo/waves/round-83/receipts/after-floors-gate-r83.txt` → **11**;
  `grep '^FAIL' … | grep -vc 'floors_guard'` → **10**. Both commands and both outputs are in
  the r84 correction block, the lesson's correction block, and the LOG entry.
- **Pre-existing reds (recorded, not claimed)** — `python3 -B verifiers/verify_skill_checklist.py` → exit 1,
  `FAIL governance.citation_resolves` (1428 evaluated at the base reading);
  `check_sibling_census.py` with the round-49 census → `province rows 20 matched 4`, exit 1;
  with the round-74 census → `province rows 20 matched 20`, `skill description names 10 of 10 non-none lanes`, exit 0.
- **No invented hash** — every 40-hex token introduced by this seat (7 in the lesson, 4 in the LOG append)
  resolves as a commit: `git cat-file -e <hash>^{commit}` → OK for all.
- **LOG diff is append-only** — `git diff --numstat LOG.md` → `126  0` (zero deletions);
  same for `corpus/lessons/round-84.md` (`18  0`) and `corpus/QUALITY.md` (`2  0`).
- **Corpus gates after the writes** — `verify_corpus_independent.py`: `tracked_files=165 … unindexed=0 stale=0 missing=0`,
  `points … dead=0`, `commits … nonhash=0 unresolvable=1 external=2` (the pre-existing deliberate
  dead-clone hash, unchanged).

## Risks / hand-off notes

1. **This lesson's own coverage-map row is still the integrator's step.** `corpus/README.md` is
   ScribeSources' file and no row names `lessons/round-85.md` yet. ScribeSources measured both
   failure shapes (`corpus/README.md:171` row-before-bytes → `missing_paths` = 1; no row → `unindexed` = 1)
   in `.ufo/waves/round-85/w1/ScribeSources/residual-index-ordering.txt`, which assigns the ordering
   to the integrator. The lesson says so explicitly; the row must land in the same commit as this file's bytes.
2. **`corpus/QUALITY.md` is a second writer's file in principle.** Q76 was appended at the tail
   (never renumbered), as the seat item directs. If the L1 or another seat also appends a Q row,
   the two must be ordered by Q-number, not by position — Q76 is currently the last row.
3. **The C1 count is a historical reading.** The lesson cites the base reading `4 of 8` from the
   committed base receipt and the committed instrument at `759cf354…`; the instrument's active path
   was removed by the quarantine, so a reader re-running the command must use the frozen copy under
   `.ufo/waves/round-85/frozen/` — and the quarantine note says that copy must not be run. The lesson
   and the LOG entry both name the frozen path rather than the removed active path, so no citation
   points at a file that no longer exists.
4. **`corpus.pointers.commit_unresolvable` stays 1.** The dead-clone hash `8b1cc1b…` in
   `corpus/lessons/round-81.md:8` is deliberate and not repairable by fabricating external
   provenance; the L1 owns the baseline refresh and the `--carry` decision. The lesson does not
   promise a zero there.
5. **`corpus/SOURCES.md` S018's digest is stale** (the specification page now serves 7 685 B against
   the row's 7 608 B pin) — flagged by the source seat, unclaimed freshness debt, not this round's claim.
6. **The wave's attack-role accounting is corrected, not rewritten.** The frozen plan and claims
   still say 6 of 16 = 37.5 %; the strict addendum set gives 4 of 16 = 25 %. The correction is
   appended in the lesson and the LOG, and the frozen files are untouched.
7. **No tooling was installed or upgraded** under the operator directive — `curl`, `coreutils`
   (`sha256sum`, `wc`, `cmp`, `grep`, `diff`), `git` (read-only) and the lane's own Python were
   already present, so there is no tool/version/channel record to give. No pacman transaction.
8. **No git or jj write was performed by this seat.** The three lane files are written in the
   working tree for the integrator to commit; the lane's history is unchanged by this seat.

## Deviations from the seat item (all L1-directed, all recorded)

- The item named two Mistakes rows; the L1 asked for the C1 control falsification as a third
  ("Three mistakes rows desired incl C1 killed") and then for a source-overreach row
  ("add source-overreach mistake if appropriate"), so the section carries four: M85-1 (r84-D1),
  M85-2 (the CRLF registry), M85-3 (the frozen R6 measures form), M85-4 (the entry's source
  over-reach). The two item-named rows are the first two, unchanged in class, evidence pointer,
  captured-by and fix.
- The item asked for exactly two mistakes; the L1's two later instructions add two more, and
  both are evidenced, so the lesson states all four and says so here.
- The item's Lesson § Gate asked for the C1/C2 predicates "verbatim from the plan". The C1
  predicate's own path was removed by the L1's quarantine between the plan and this write, so the
  LOG entry quotes the plan's sentence verbatim and then cites the frozen path where the bytes now
  live; the lesson quotes the plan sentence verbatim and names the relocation in prose.
