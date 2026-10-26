# Round-74 C1 shortcut-control worlds — seat `ExecSpecControlsR74`

Twelve self-contained shortcut worlds for the C1 depth predicate (*spec craft pages backed N of 3*),
plus the positive control. Every world is one `world.patch` applied to a **fresh `git clone --shared`**
of the lane at base `1e03d1991bc02281b00a5b7a5e00c9d5d5d72908` inside a fleet-shaped `/tmp` sandbox;
the commit exists only inside that clone. Nothing here was applied to the lane tree, the fleet repo,
the lane index or `jj` state.

Plan: `plans/round-74.md` § C1, frozen at `329e7d91d7d750031c35d264f0e34af1d0ce8385`.
Counter measured: `../ExecSpecCounterR74/check_spec_craft.py`, **FINAL** frozen copy — file sha256
`2ac18bedf3ab7e7767eeeddd68eaf7130139405b137e62f7ab677dd0a4e13840`, its own blanked
`SELF_SHA` `4065253e24f203772a30b6498101a77e4a88fca8a72aaa8377d71e46f42c39c8` (verified by
`--print-self-sha` before the run). The same twelve lines were produced at two earlier frozen copies
(`525a3c6e…`, `0e973df3…`) during the counter's edit window; the table is unchanged across all three.
Rescore with `./score_worlds.sh ../ExecSpecCounterR74/check_spec_craft.py` (<60 s).
The printed table is `score-worlds.out`, the per-world counter stdout is each `<world>/score.stdout.txt`.

## The table

| world | plan item | what it does | clause it defeats | expected | measured |
|---|---|---|---|---|---|
| `w00-honest-full` | added positive control | every conjunct honest | none | 3 of 3, exit 0 | **3 of 3, exit 0** |
| `w01-staged-entry` | (1) | staged entry copied unchanged, staged ids S236/S237, no registry rows | (a) no rule-table row; (b) no registry row | 0 of 3, exit 1 | **0 of 3, exit 1** |
| `w02-queued-status` | (2) | three rows appended with status `queued` | (b) status not `mined` | 0 of 3, exit 1 | **0 of 3, exit 1** |
| `w03-invented-token` | (3) | S223 second token `--frobnicate-index .`, absent from the snapshot | (a) token not located | 2 of 3, exit 1 | **2 of 3, exit 1** |
| `w04-snapshot-edited` | (4) | quickstart snapshot hand-edited, manifest pin left | (c) sha256 mismatch → exit 2 | exit 2 | **exit 2, `snapshot_tampered` on stderr, no stdout** |
| `w05-cross-page-tokens` | (5) | SKILL rows citing `best-practices (S223)` carry quickstart-only tokens (Q37 real text) | (e) no S223 token in the action cell | 2 of 3, exit 1 | **2 of 3, exit 1** |
| `w06-token-stuffed` | (6) | S224 tokens cell: four real best-practices tokens, none in using-scripts | (a) tokens not located | 2 of 3, exit 1 | **2 of 3, exit 1** |
| `w07-entry-outside` | (7) | entry at `corpus/spec-skill-creation-craft-round74.md`; rows and PROVINCE name it | (a) frozen entry path absent | 0 of 3, exit 1 | **0 of 3, exit 1** |
| `w08-staged-rows` | (8) | package `SOURCES.append.md` appended as-is inside `## Registry` | (b) registry not census-conformant; two rows per id | below 3 | **0 of 3, exit 1** |
| `w09-skill-rows-only` | (9) | SKILL subsection present; entry and rows absent | (a)/(f) entry absent | 0 of 3, exit 1 | **0 of 3, exit 1** |
| `w10-two-pages` | (10) | honest for two pages, no `quickstart` row anywhere | (a)/(b)/(e) quickstart only | 2 of 3, exit 1 | **2 of 3, exit 1** |
| `w11-opened-staged-date` | (11) | three rows `opened` 2026-10-23, the staged fetch date | (b) `opened` not a round-74 date | 0 of 3, exit 1 | **0 of 3, exit 1** |

Kill rule: no shortcut world reaches 3 of 3; the positive control reaches exactly 3 of 3 and exit 0,
so the "must score below 3" rule is not vacuous on this counter.

Census at every applied revision (`bash scripts/sources-census.sh validate --today 2026-10-26
--file <clone>/corpus/SOURCES.md kotoba`): exit 0 for all worlds except `w08-staged-rows`, exit 1
(434 `E` findings: `E03` 23 duplicate ids, `E09` 188 prose rechecks, `E11` 223 used-by paths the
staged rows name but the lane does not hold; the staged file re-numbers S223–S225 as well, so the
counter also reports two registry rows per cited id).

## Snapshot bytes carried in every world

Fetched by this seat on 2026-10-25 with `curl -sL --max-time 60 -A 'Mozilla/5.0'`; each is embedded
verbatim in `world.patch` at `.ufo/waves/round-74/snapshots/<page>.md` and pinned in the same patch's
`MANIFEST.sha256`:

| page | URL | HTTP | bytes | sha256 |
|---|---|---|---|---|
| best-practices | `https://agentskills.io/skill-creation/best-practices.md` | 200 | 15 060 | `ab9f3b6091a0f24816b52cd7b90a3fdf53e621f47dba13b36694be272b87fb41` |
| using-scripts | `https://agentskills.io/skill-creation/using-scripts.md` | 200 | 12 078 | `2cd7727106b423a758b4b6b1ab3545da74845a98e68e6718279846f89d62ad1f` |
| quickstart | `https://agentskills.io/skill-creation/quickstart.md` | 200 | 4 080 | `7c480b447edac58fd8ff8f250c471dfc7d4621155b91fabed46379075c32bffb` |

## Construction constraints measured on the counter (not claims about it)

1. **The entry must open with the provenance trio.** The counter's `entry_head()` reads leading
   `source:` lines, then `verified-at:`, then `recheck:`, at the very top of the rendered entry. The
   first honest draft put a `# title` first and read `0 of 3` with
   `entry does not open with source: lines`; the frozen worlds put the three `source:` lines first.
   The real round-74 entry has the same constraint.
2. **A mid-edit counter is an environment error, not a score.** The counter's `SELF_SHA` guard exits 2
   with `counter drifted` when the running copy's blanked sha differs from its pin; copies taken while
   the file was being edited scored 4 of 12 worlds as `- of 3, 2` in an earlier run. `score_worlds.sh`
   now freezes one copy and asserts its blanked sha before scoring.
3. **Exit 2 prints no score line.** `w04` is the only world in that class; the harness reports it as
   `- of 3, 2` and keeps its stderr (`environment error: snapshot_tampered: …/quickstart.md`).
4. **w08's staged rows are rejected twice over:** census `E03` duplicate ids (the campaign rows
   re-number S203–S3xx including S223–S225) and `E09` prose rechecks; the counter reports the
   duplicate registry rows before it reads the census.

## Replay

All worlds at once (prints `<world> <N of 3> <exit>`):

```
cd /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-74/w1/build/ExecSpecControlsR74
./score_worlds.sh ../ExecSpecCounterR74/check_spec_craft.py
```

One world: each `<world>/README.md` carries the exact command block (fleet-shaped sandbox,
`git clone --shared -q --no-checkout`, `git apply`, commit with a throwaway in-clone identity, then
`python3 -B _check_spec_craft_ctl.py --rev HEAD`).

## Files

- `<world>/world.patch` — the whole world as a diff against the base (`git apply`-clean; replayed).
- `<world>/README.md` — what the world changes, the clause it defeats, expected and measured score,
  the census exit, and the exact replay.
- `<world>/score.stdout.txt` / `score.stderr.txt` — the counter's own output for that world.
- `score_worlds.sh` — the harness; `score-worlds.out` — its printed table; `scores.txt` — the same
  table as parsed into the per-world READMEs.
- `build_worlds.py` — the generator (provenance only; the worlds are self-contained patched files).
