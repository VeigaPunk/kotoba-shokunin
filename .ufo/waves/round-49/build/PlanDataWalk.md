# PlanDataWalk — C2 instrument skeleton (kotoba round 49)

Read-only walk over `/home/vgpnk/Projects/shokunin/.ufo/prompts` and `.ufo/state/`.
Snapshot: 2026-10-22T09:45:37Z. All counts non-recursive over the prompts root unless
stated; every count carries its command in Evidence. No lane edit; nothing executed
from the population.

## Findings

### F1 Population and name classes

| class | count | names |
|---|---|---|
| `<lane>-round-<N>.md` | 274 | 23 lanes: aggregator 9, audio 2, chousa 6, game-dev-2d 2, game-dev-3d 2, kagi 23, kaidoku 14, kake 24, kama 18, kasegi 17, kengaku 18, kotoba 18, kotodama 3, kumitate 21, lore 2, mado 12, mori 16, protocol 12, revenger 3, souji 11, tabi 12, tameshi 15, tsukuroi 14 |
| `<lane>-L1.md` | 8 | aggregator, kagi, kake, kasegi, kengaku, kotoba, kumitate, protocol |
| other | 5 | `.gitkeep`; `revenger-round-1-continuation-kaika.md`, `tabi-…`, `tameshi-…`, `tsukuroi-…` (4 continuation files, first line is a normal round-1 role line) |

- `closure/` (86 files) re-uses the same `round-<N>` name grammar but holds closure/integrator
  prompts: line 1 of `closure/chousa-round-27.md` is `You are the hyaku non-author integrator of
  record (the protocol lane's closure role) for ONE`. 86/86 carry no round token on line 1 and
  0/86 are byte-identical to their root namesakes. A recursive scan adds 86 phantom round files.
- The population is live. The first count this session returned 285 files / 272 round prompts;
  the 09:45:37Z count returns 286 / 274 (`mori-round-25.md` mtime 06:42, `kumitate-round-39.md`
  06:43). Any published count needs the timestamp; the instrument should accept a pinned listing
  for citable output.

### F2 Role-line and report-path forms (6 lanes, oldest → newest)

| file (lines) | line 1 (role line) | `.ufo/reports/` lines |
|---|---|---|
| `audio-round-1.md` (67) | `You are the audio L1, round 1. Working dir: …/<audio-repo>.` | 39: `Write the round report at` + `/home/vgpnk/Projects/shokunin/.ufo/reports/round-1/audio.md` |
| `kagi-round-3.md` (3) | `You are the kagi-shokunin L1, round 3 of up to 1024. Working dir: /home/vgpnk/projects/shokunin/kagi-shokunin.` | 2: `… then write .ufo/reports/round-3/kagi.md in the main repo.` |
| `chousa-round-24.md` (200) | `You are the chousa L1, round 24. Working dir: …/chousa-shokunin.` | 62 write (`reports/round-24/chousa.md`), 108 fleet report (`…fleet-ledger/.ufo/reports/round-24/chousa.md`), 124 fail-closed check |
| `kama-round-25.md` (350) | `You are the kama L1, round 25. Working dir: …/kama-shokunin.` | 101 `Write the round report at` + abs path; 252 `your report` + abs `…/round-25/kama.md`; appended lines in; 315 `-- .ufo/reports/round-25/kama.md` |
| `kotodama-round-51.md` (350) | `You are the kotodama L1, round 51. Working dir: …/kotodama-shokunin.` | 101, 252, 315 — same three forms; template twin of kama-25 |
| `game-dev-3d-round-108.md` (200) | `You are the game-dev-3d L1, round 108. Working dir: …/game-dev-3d-shokunin.` | 62, 108, 124 as chousa-24 |

Derived grammar the instrument must accept:

- Role line: `You are the (shokunin[- ])?<lane>(-shokunin)? L1( \(model [^)]+\))?, round (\d+)( of up to (\d+))?\.`
  Families over 274 files: `<lane> L1, round N.` 173; `<lane> L1, round N of up to M.` 57;
  `<lane>-shokunin L1, round N of up to M.` 34; `shokunin-<lane> L1, …` 6 (protocol 4–9);
  `shokunin <lane> L1 (model m_qwen), round N of up to M.` 2 (aggregator 4–5).
- Round token = first `\d+` after the word `round`; the `of up to 1024` cap must not be captured.
- Report path roots (580 mentions over 274 files): fleet-repo absolute 327, relative 236,
  fleet-ledger absolute 17. Basename is always `round-<N>/<lane>.md`; 0 exceptions.
- Anchor dispatch.04 on the write target, not every mention. Write forms:
  `Write the round report at` 175, numbered `N. Write` (protocol 4–9, aggregator 4–5),
  `Write .ufo/… on the main repo` 57, `then write .ufo/… in the main repo` 34,
  `write only` (fleet report) 17, `Report: write` (L1 files). References to exclude:
  `your report …; appended lines in` 135, `Fail closed: if … exists` 17,
  `Review all reports under` 2 (aggregator 4–5, whose input is `round-3/AGGREGATE.md`).
- Placeholder clause must be scoped to the report path. A whole-file `<…>` scan flags 232/274
  because the newest template prompts carry metavariables in prose (`<lane> | round-<N> |
  <question>`, `kama-round-25.md:139`). Scoped to report paths: 0/274.

### F3 The nine dispatch boxes against today's population

| box | mechanically executable today? | evidence |
|---|---|---|
| dispatch.01 shape/lines | no | line count is mechanical, "6 stanzas" is not. L1 8/8 within 9–12 lines; `round files are 3–4 lines` holds for 40/274. Observed round lengths: 396 (69), 11 (57), 3 (34), 67 (23), 200 (17), 350 (15). The clause describes the round-7 shape, not today's rendered template. |
| dispatch.02 spawn stanza order | no | no stanza markers in any L1 file; 6/8 L1 files contain a duplicated 5-line block, so order detection collides with dispatch.07. |
| dispatch.03 `\| godspeed` final line | yes, ambiguous | strict last-line equality 23/274 rounds, 0/8 L1; suffix reading 122/274, 8/8. 152 round files carry no `\| godspeed` tail at all. Reading must be declared. |
| dispatch.04 literal path, filename = lane id | yes | 274/274 basename = `<lane>.md`, 0 placeholders in any report path. Needs write-target anchoring plus the aggregator exception (L1 writes `AGGREGATE.md`, rounds write `aggregator.md`). |
| dispatch.05 delta only / no L2 map | no | fleet model-map tokens (`m_lunamax`/`executor/scribe`) present in 93/274; "delta only" has no decidable predicate. |
| dispatch.06 self-contained, no deictics | partly | path resolution decidable (`audio-round-1.md:1` `<audio-repo>` is a real fail); "deictic" is not (`this\|above\|previous\|earlier` hits 232/274 — false-positive machine). |
| dispatch.07 no `\n`, no duplicate blocks | partly | literal `\n` 0/274 rounds, 6/8 L1; duplicate blocks need a stated rule. Repeated non-empty line: 6/8 L1s, 3 lines each. |
| dispatch.08 round token identity + ≤ state | identity yes, ≤ clause no | identity 274/274 (file name, role line, report dir all agree). ≤ against `.ufo/state/<lane>.round` fails 19/21 lanes and is unverifiable on 2 — see F4. |
| dispatch.09 explicit scope fence | no | keyword proxy `do not touch\|MUST NOT` hits 69/274; no grammar for "names what MUST NOT be written plus the dir it may write". |

Only dispatch.04 is executable as written today; dispatch.08 is executable in its identity half
and needs a state-source amendment for its `≤` half.

### F4 State comparison — `<lane>.round` is stale, `.report-baseline` is live

- All 21 `.round` files share mtime 2026-10-15 (18× `01:50:57`, 3× `01:45:42`) — frozen since a
  fleet reset. `.report-baseline` (same directory, format `<round> <sha256>`) is refreshed at every
  in-session dispatch by `scripts/hyaku/inline.sh:100` calling `record_report_baseline` (defined
  `scripts/shokunin-watchdog.sh:122`), and that path never writes `<lane>.round` (the `.round`
  write sits at `scripts/shokunin-watchdog.sh:220`; `pgrep -af shokunin-watchdog` returns no
  process, and `.round` files have not changed since 2026-10-15). Newest baseline is
  2026-10-22T06:42.
- Against `.round`: highest prompt round exceeds the value on 19/21 lanes, and kotodama/souji have
  no `.round` at all → the `≤` clause is non-PASS on 21/21 target lanes.
- Against `.report-baseline`: present for 17 lanes, highest prompt round == baseline on all 17
  (0 exceed); absent for audio, game-dev-2d, game-dev-3d, lore.

| lane | hi prompt | `.round` | hi > `.round` | `.report-baseline` | hi > baseline |
|---|---|---|---|---|---|
| audio | 101 | 1 | YES | NA | NA |
| chousa | 28 | 1 | YES | 28 | no |
| game-dev-2d | 105 | 1 | YES | NA | NA |
| game-dev-3d | 108 | 1 | YES | NA | NA |
| kagi | 28 | 16 | YES | 28 | no |
| kaidoku | 25 | 1 | YES | 25 | no |
| kake | 28 | 16 | YES | 28 | no |
| kama | 25 | 1 | YES | 25 | no |
| kasegi | 23 | 17 | YES | 23 | no |
| kengaku | 29 | 13 | YES | 29 | no |
| kotoba | 49 | 16 | YES | 49 | no |
| kotodama | 51 | NA | NA | 51 | no |
| kumitate | 39 | 18 | YES | 39 | no |
| lore | 103 | 1 | YES | NA | NA |
| mado | 22 | 1 | YES | 22 | no |
| mori | 25 | 2 | YES | 25 | no |
| revenger | 62 | 1 | YES | 62 | no |
| souji | 22 | NA | NA | 22 | no |
| tabi | 22 | 1 | YES | 22 | no |
| tameshi | 25 | 1 | YES | 25 | no |
| tsukuroi | 24 | 1 | YES | 24 | no |

Skeleton decision for dispatch.08: read the state round from `<lane>.report-baseline` field 1;
fall back to `<lane>.round` only with a `state-stale` annotation (state mtime older than the
prompt's); emit `state-unavailable` (not FAIL) for the four legacy lanes. As written against
`.round`, the instrument would report 21/21 FAIL on today's fleet — a stale-file artifact, not a
prompt defect, and a red count the round cannot defend (Q14/Q18).

## Remaining unknowns

- Whether C2's population count should be 274 (round prompts) or 286 (all `*.md`) — mode split
  must be stated in the instrument's output or the SCORECARD row will be unreproducible.
- Whether the four legacy lanes (audio 101, lore 103, game-dev-2d 105, game-dev-3d 108) are retired;
  no state source exists that can satisfy a `≤` clause for them.
- Which aggregator report name is canonical for dispatch.04 (`AGGREGATE.md` at L1 vs `aggregator.md`
  at rounds) — recommend excluding non-sibling fleet lanes from box 04 rather than encoding two names.

## Evidence (commands, exit codes, hashes)

- `date -u +%Y-%m-%dT%H:%M:%SZ` → `2026-10-22T09:45:37Z`.
- `cd .ufo/prompts && ls -1 *.md | wc -l` → 286; `ls -1 *-L1.md | wc -l` → 8;
  `ls -1 | grep -cE '^[a-z0-9-]+-round-[0-9]+\.md$'` → 274; `ls -1 *continuation*.md | wc -l` → 4;
  `ls -1 closure | wc -l` → 86. All exit 0.
- Lane/round census and state table: shell loop over the 21 lanes using
  `ls -1 .ufo/prompts | grep -E "^<lane>-round-[0-9]+\.md$"` and
  `cut -d' ' -f1 .ufo/state/<lane>.report-baseline`; output table saved at
  `/fast/scratch/hyaku/kotoba-r49/seats/PlanDataWalk/table.tsv` (22 lines incl. header). Exit 0.
- `ls -l --time-style=+%Y-%m-%dT%H:%M:%S .ufo/state/*.round | awk '{print $6}' | sort | uniq -c`
  → `3 2026-10-15T01:45:42`, `18 2026-10-15T01:50:57`; `ls -1 .ufo/state/*.round | wc -l` → 21.
- Python scan of the root (fullmatch on `[a-z0-9-]+-round-\d+\.md`) produced the box metrics:
  3–4 lines 40/274; strict `| godspeed` 23, suffix 122; L1 strict 0, suffix 8; L1 `\n` 6/8;
  whole-file placeholder 232, report-path placeholder 0; model-map tokens 93; fence proxy 69;
  deictic proxy 232; write verbs 175/57/34/17; path roots 327/236/17 = 580. Exit 0.
- `closure/` hash comparison (sha256 per file vs root namesake): 0 identical, 86 differ, 0 missing;
  byte counts from `wc -c`/`wc -l` (exit 0) as quoted in F2.
- Read-only sources: `kotoba-shokunin/SKILL.md:300-330`, `verifiers/checklist-baseline.json`
  (`dispatch.01`–`dispatch.09`, all `unexecuted:`), `scripts/shokunin-watchdog.sh:27-31,92-146,200-221`,
  `scripts/hyaku/inline.sh:7,100`; `grep -rn report-baseline scripts/` exit 0;
  `pgrep -af 'shokunin-watchdog|hyaku'` matched hyaku seat commands only, no watchdog process.
  No tool installs or upgrades; no web sources opened; nothing fetched.
