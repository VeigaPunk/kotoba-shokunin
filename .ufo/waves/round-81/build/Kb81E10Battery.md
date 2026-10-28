# Kb81E10Battery — base no-harm battery receipt index (round 81, w1)

Runner: `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/run-battery.sh`
(r81 port of `.ufo/waves/round-80/build/run-battery.sh`; sha256
`19b878a12d07a5dc5a0e05b548a0be23910deaef72360be07f40b40f921fc76a`, source sha256
`cddf2dd8852801206a152dec62a62d64409453a280cef82cb3a002d7636d7601`; diff = 3 hunks, all
header/scratch-root text, no logic).

Invocation (runner exit 1 = a red battery is a reading, not a runner failure):

```
HYAKU_SCRATCH=/fast/scratch/hyaku/kotoba-r81/Kb81E10Battery \
bash .ufo/waves/round-81/build/run-battery.sh \
  b284223105f4d106f7e8f56ed4fd296c643cda0e \
  /home/vgpnk/Projects/shokunin/kotoba-shokunin \
  .ufo/waves/round-81/build/base-battery
# -> run-battery.sh: rev b284223105f4d106f7e8f56ed4fd296c643cda0e; 14 receipt(s), 10 exit 0, 4 non-zero
# -> 01/02: fleet root /home/vgpnk/Projects/shokunin; guards 5 of 5; tip battery exit 0: 4 of 6
# RUNNER-EXIT=1
```

Measured rev `b284223105f4d106f7e8f56ed4fd296c643cda0e`; fleet root
`/home/vgpnk/Projects/shokunin`; world `.../kotoba-r81/Kb81E10Battery/battery/run-541851-12958/world/kotoba-shokunin`
(removed on exit); utc `2026-10-28T02:27:36Z`; python 3.14.8; git 2.56.0. Every receipt line 1
is `# rev=<full> cmd=<command> utc=<ISO>` (checked for all 14 files; 15/15 OK).

Caveat for readers of `base-battery/index.txt`: the runner's `figure_of` reports the last
non-comment body line, so the two `--json` receipts (05/06/07) index as `}`; their verdict lives
in the receipt's `exit=` and in this table.

## Receipts (one line per file, in `base-battery/`)

| file | exit | figure / reading |
|---|---|---|
| `01-tip-battery-dot.txt` | 1 | `fleet root /home/vgpnk/Projects/shokunin; guards 5 of 5; tip battery exit 0: 4 of 6` — `--repo .` form from the world lane root, `--fleet` explicit |
| `02-tip-battery-abs.txt` | 1 | same line, absolute `--repo <lane>` form; identical to form 1 |
| `03-gate-registry.txt` | 0 | `gate registry rows conformant 63 of 63 lane verifiers; phantom 0` |
| `04-assertion-floors.txt` | 0 | 17 `PASS` floor rows, 0 fail, last `PASS sibling_reread observed=47 floor=47` |
| `05-skill-checklist.txt` | 0 | JSON: 11 checks `PASS`, 0 FAIL/WARN/SKIP; `trigger.line_budget` = 596 lines within budget 600 |
| `06-corpus-integrity.txt` | 1 | JSON: 5 DRIFT — `tracked_files` 155≠154, `unindexed` 1, `report_total` 111≠109, `report_dead` 1, `commit_unresolvable` 2 |
| `07-corpus-independent.txt` | 1 | JSON: 2 DRIFT — `index.unindexed` 1, `commit_unresolvable` 2 (`report_dead` 0 here) |
| `08-correction-sweep.txt` | 0 | `correction sweep: 0 stale block(s)` |
| `09-census.txt` | 0 | `kotoba	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md`; 31 `W04 duplicate url` warnings, no error verdict |
| `10-skill-lines.txt` | 0 | `596 SKILL.md` |
| `11-skill-bytes.txt` | 0 | `80920 SKILL.md` |
| `12-skill-long120.txt` | 0 | `151` lines > 120 chars |
| `13-skill-long300.txt` | 0 | `81` lines > 300 chars |
| `14-skill-longest.txt` | 0 | `longest=1095 line=514` |
| `index.txt` | — | runner/rev/repo/fleet/world/utc/python/git header + per-receipt `exit=`/figure lines + `receipts=14 green=10 non-zero=4` |

Failing-gate detail (verbatim from 06/07):

- `corpus/lessons/round-80-verifier-spotcheck.md` — unindexed (both gates).
- `corpus/lessons/round-77-verifier-spotcheck.md:15: HEAD:.ufo/reports/round-77/kotoba.md` —
  `report_dead` (integrity only; the independent gate reads `report_dead 0` for the same token).
- `corpus/SOURCES.md:171` and `:172: 7bb48f213ac677f943d5c791199ed3dddf302f00` —
  `commit_unresolvable` 2 (both gates).

Runtimes: tip battery form 1 wall 111.0 s, form 2 wall 108.8 s (floors gate alone 107.8 s
inside each); whole runner 334.8 s wall.
