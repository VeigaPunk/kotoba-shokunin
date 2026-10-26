# Round 74 — wave 1 — C1 shortcut-control worlds (seat `ExecSpecControlsR74`)

**Verdict: built and measured.** Twelve self-contained C1 shortcut worlds (the eleven named in
`plans/round-74.md` § C1 plus one positive control) are committed as `world.patch` bundles under
`.ufo/waves/round-74/w1/build/ExecSpecControlsR74/`, each with an exact README replay. Run against the
declared counter, **every shortcut world scores below 3 of 3 and the positive control scores exactly
3 of 3, exit 0**: the kill rule is not vacuous, and the three-page target is reachable by the frozen
shape. No lane file, fleet file, staged-package file, lane index or `jj` state was written; all git
writes happened in throwaway `--shared` clones; every `/tmp` scratch directory this seat made is
deleted.

Base: `1e03d1991bc02281b00a5b7a5e00c9d5d5d72908`, plan frozen at
`329e7d91d7d750031c35d264f0e34af1d0ce8385`. Counter:
`.ufo/waves/round-74/w1/build/ExecSpecCounterR74/check_spec_craft.py`, **FINAL** frozen copy — file
sha256 `2ac18bedf3ab7e7767eeeddd68eaf7130139405b137e62f7ab677dd0a4e13840`, its blanked `SELF_SHA`
`4065253e24f203772a30b6498101a77e4a88fca8a72aaa8377d71e46f42c39c8` (`--print-self-sha` printed
exactly that before the final run). The same twelve lines were also produced at the two earlier copies
`525a3c6e…` and `0e973df3…` during the counter's edit window, so the table did not ride on a moving
instrument. Rescore command: § 2.

## 1. Delivered

`.ufo/waves/round-74/w1/build/ExecSpecControlsR74/` (42 files, 876 KB):

- `w00-honest-full/` … `w11-opened-staged-date/` — each: `world.patch` (the whole world as a diff
  against the base, `git apply`-clean), `README.md` (changes, defeated clause, expected and measured
  score, census exit, exact replay), `score.stdout.txt` / `score.stderr.txt` (the counter's own output).
- `score_worlds.sh` — replays every world in a fleet-shaped sandbox and prints `<world> <N of 3> <exit>`.
- `score-worlds.out` — the printed table; `scores.txt` — the same table parsed into the READMEs.
- `README.md` — index, the table, snapshot provenance, construction constraints, replay.
- `build_worlds.py` — the generator (provenance; the worlds are self-contained).

Each world carries its own `corpus/knowledge/spec-skill-creation-craft-round74.md`,
`corpus/SOURCES.md` rows, `.ufo/waves/round-74/snapshots/{best-practices,using-scripts,quickstart}.md`
and `MANIFEST.sha256`, the `SKILL.md` subsection
`### Body craft — the specification's skill-creation guides`, and the `PROVINCE.md` § Core bullet.
Snapshot bytes are this seat's own fetch of the three pages on 2026-10-25 (`curl -sL --max-time 60 -A
'Mozilla/5.0'`, HTTP 200): best-practices 15 060 B sha256 `ab9f3b60…`, using-scripts 12 078 B
`2cd77271…`, quickstart 4 080 B `7c480b44…` (full digests in the bundle README).

## 2. Measured

```
$ cd .ufo/waves/round-74/w1/build/ExecSpecControlsR74
$ ./score_worlds.sh ../ExecSpecCounterR74/check_spec_craft.py
# counter frozen: …/_counter_frozen.py sha256 2ac18bedf3ab7e7767eeeddd68eaf7130139405b137e62f7ab677dd0a4e13840
# (blanked SELF_SHA 4065253e24f203772a30b6498101a77e4a88fca8a72aaa8377d71e46f42c39c8)
w00-honest-full 3 of 3 0
w01-staged-entry 0 of 3 1
w02-queued-status 0 of 3 1
w03-invented-token 2 of 3 1
w04-snapshot-edited - of 3 2
w05-cross-page-tokens 2 of 3 1
w06-token-stuffed 2 of 3 1
w07-entry-outside 0 of 3 1
w08-staged-rows 0 of 3 1
w09-skill-rows-only 0 of 3 1
w10-two-pages 2 of 3 1
w11-opened-staged-date 0 of 3 1
```

`-` is the counter's exit-2 class: it prints the environment error on stderr only, never a score line.
The same twelve lines were produced at two earlier frozen copies (`525a3c6e…`, `0e973df3…`) inside
the counter's edit window; this final run is the one `score-worlds.out` holds.

Per-world, the counter's own printed findings (each file's `score.stdout.txt`):

| world | counter output after the score line |
|---|---|
| `w00` | `backed: best-practices`, `backed: using-scripts`, `backed: quickstart` |
| `w01` | `no rule table row names any of best-practices, using-scripts, quickstart (the entry has no rule table)` |
| `w02` | `S223: status 'queued' (want 'mined')` (same for S224, S225) |
| `w03` | `best-practices: token '--frobnicate-index .' does not occur word-bounded in best-practices.md`; `backed: using-scripts`, `backed: quickstart` |
| `w04` | stderr: `environment error: snapshot_tampered: .ufo/waves/round-74/snapshots/quickstart.md` |
| `w05` | `best-practices: SKILL.md row citing S223 carries no best-practices token in its action cell: ['.agents/skills/roll-dice/SKILL.md']`; `… has 0 counting row(s) citing S223` |
| `w06` | `using-scripts: token 'pdfplumber' does not occur word-bounded in using-scripts.md` (also `pdf2image`, `pypdf`); `backed: best-practices`, `backed: quickstart` |
| `w07` | `PROVINCE.md § Core does not name corpus/knowledge/spec-skill-creation-craft-round74.md`; `entry … absent at HEAD (the frozen path is the entry's only home)` |
| `w08` | `best-practices: S223: 2 registry rows in corpus/SOURCES.md (want exactly 1)` (same for S224) |
| `w09` | `entry corpus/knowledge/spec-skill-creation-craft-round74.md absent at HEAD` |
| `w10` | `backed: best-practices`, `backed: using-scripts`; `quickstart: 0 rule-table row(s) in … (want exactly 1)` |
| `w11` | `S223: opened '2026-10-23' is not a round-74 date (2026-10-25 or 2026-10-26)` (same for S224, S225) |

## 3. Census at each applied revision

```
$ bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --today 2026-10-26 \
    --file <clone>/corpus/SOURCES.md kotoba
```

exit 0 for `w00`–`w07`, `w09`–`w11`; **exit 1 for `w08-staged-rows`** with 434 `E` findings —
`E03` 23 duplicate ids, `E09` 188 prose rechecks, `E11` 223 used-by paths the staged rows name but
the lane does not hold. `w08` appends the package's `SOURCES.append.md` as-is inside `## Registry`, so
its campaign rows re-number S223–S225 and (b) fails on both the duplicate-row check and the census.
This is the measured census half of plan item (8).

## 4. Two construction constraints measured on the counter (not claims about it)

1. **The entry must open with the provenance trio.** The counter's `entry_head()` reads leading
   `source:` lines, then `verified-at:`, then `recheck:`. My first honest draft put a `# title` first;
   the counter printed `spec craft pages backed 0 of 3` with
   `entry does not open with source: lines`, `entry has no verified-at: line after its source: lines`,
   `entry has no recheck: line after verified-at:`, and `cited S223, S224, S225 absent from the
   entry's own source: lines`. The committed worlds put the three `source:` lines at the top
   (`w00-honest-full/world.patch`, new file `corpus/knowledge/spec-skill-creation-craft-round74.md`).
   The real round-74 entry must do the same or (a) fails for every page.
2. **A mid-edit counter is an environment error, not a score.** An earlier run copied the counter
   while its seat was writing it: 4 of 12 worlds read `environment error: counter drifted — the
   running file is not the frozen counter`, exit 2, empty stdout. `score_worlds.sh` now freezes one
   copy and asserts its blanked sha equals its own `SELF_SHA` before scoring, and removes stale
   `score.*` files per world. The L1 must refill `SELF_SHA` after any edit of the landed counter.

## 5. Calibration

- **The positive control is additive and load-bearing.** The plan lists only shortcut worlds; without
  `w00` the "each must score below 3" rule would hold on a counter that can never print 3. `w00`
  reaches exactly 3 of 3 and exit 0, on the same bytes shape as the honest round-74 landing (entry,
  three `mined` tier-A rows opened 2026-10-25, pinned snapshots, six SKILL rows with the token inside
  each action cell, PROVINCE bullet).
- **The two-page world is the honest floor, measured.** `w10` is fully honest for two pages and reads
  `2 of 3`; it is the world the plan's Q45 census would land on if one page carried fewer than two
  locatable tokens, and it shows the counter's margin is real: 2 is reachable without any forgery.
- **The exit-2 class is separated from the score.** `w04` (snapshot hand-edited, manifest pin left)
  prints no score line; the harness keeps the class distinguishable (`- of 3 2`) instead of folding it
  into `0 of 3`.
- **Real-text shortcut (Q37) is the fifth world, not a fabricated one.** `w05` uses real quickstart
  tokens under a `best-practices (S223)` label; the counter rejects the rows because the token is not
  in that page's snapshot, and the finding names the token.

## 6. Limits and what I did not do

- The three snapshot pages are **this seat's** fetch, not the source seats' snapshots; the byte sizes
  and staging dates match the staged package (using-scripts 12 078 B, quickstart 4 080 B), but each
  world is self-contained, so a different snapshot naming in the real landing does not collide.
- The counter was still moving during the wave. I did not change any of its judgment tables; I only
  built worlds to its declared shape (its answer to my `agent://ExecSpecCounterR74` query, quoted in
  § 1–4 above). Rescore after it settles with the command in § 2 (<60 s).
- I did not run the lane gates, the tip battery, or any build/lint/test: out of scope for this wave
  and owned by the L1.
- No subagent/labrat was used; no tool was installed.

## 7. Evidence index (lane-relative)

| pointer | what |
|---|---|
| `.ufo/waves/round-74/w1/build/ExecSpecControlsR74/README.md` | index, table, provenance, replay |
| `…/ExecSpecControlsR74/score_worlds.sh` | harness (`<world> <N of 3> <exit>`) |
| `…/ExecSpecControlsR74/score-worlds.out` | measured table, frozen counter sha on the first line |
| `…/ExecSpecControlsR74/w00-honest-full/world.patch` | positive control: entry trio at the top |
| `…/ExecSpecControlsR74/w08-staged-rows/world.patch` | staged rows appended as-is (census rejects) |
| `…/ExecSpecControlsR74/w04-snapshot-edited/score.stderr.txt` | `snapshot_tampered` exit-2 class |
| `…/ExecSpecCounterR74/check_spec_craft.py` | the counter measured (sha pinned above) |
| `plans/round-74.md` § C1 | frozen predicate and the shortcut list |
