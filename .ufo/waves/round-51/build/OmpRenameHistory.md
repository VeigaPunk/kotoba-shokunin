# OmpRenameHistory — loader-registration callee renames since round 18 (round-51 build, advisory)

Result: five omp rebuilds since round 18 renamed the loader registration callees (six counting round
18's own rebuild; the fifth, 18.12.6, is unrepaired at this writing); the call *shape* never changed,
only identifiers — callee, first-arg name, and group-variable names — and on 18.12.6 a group constant
(`S$`) is now ambiguous, so a callee-only re-pin cannot reach 7 of 7.

## Rename history

| # | rebuild mtime (-0300) | omp version | old → new callees | re-derived by | red hours | rounds that landed red |
|---|---|---|---|---|---|---|
| 1 | 2026-10-14T08:39:28 | not recorded (sha 55016ef5→ff59fc1b) | `Id/Cl/jD[ef]` → `+Tl/dr/GW` | round 18, `02302c5` 2026-10-14T10:00:38 | 1h21m | 0 (round 19 landed 21:15, green) |
| 2 | 2026-10-16T05:15:11 | 18.11.1 (sha bf1e86a9) | `+Co/Dl/Hj` | round 21, `2ca8d01` 2026-10-19T01:21:10 | 68h05m | 0 round landings in the window (10-16→10-18 has only non-round commits; `4e92f36` 10-18 was red and unrecorded, `LOG.md:1209`) |
| 3 | 2026-10-19T12:35:55 | 18.12.2 (sha 9513ef9f) | `+I5/Gl/Mo` | round 44, measured 15:09:38, `7d8bf2f` 15:30:15 | 2h33m (to measurement) | 1 — round 43 landed 15:00:53 (`6fbbff5`) pinning 18.11.1 while the host had run 18.12.2 for 2h25m |
| 4 | 2026-10-19T16:23:32 | 18.12.3 (sha 065b5079) | renamed again; names **not recorded** (live gate 5/7, 0/8 extraction at the round-46 census with the I5/Gl/Mo list) | **never** (superseded by 18.12.5) | 35h07m | 1 — round 46 landed 19:29:36 (`f2f9ee1`); round 47's plan then carried the stale 18.12.3 premise (`corpus/lessons/round-47.md` M20) |
| 5 | 2026-10-21T03:30:38 | 18.12.5 (sha fdbc8136) | `+lq/Xl/Fo` (groups var-bound `f$/m$`) | round 47, `7ad7fad` 2026-10-21T13:46:13 | 10h15m | 0 (round 47 was the repair round) |
| 6 | 2026-10-21T20:37:24 | 18.12.6 (sha 85d9daf3) | `+bq/Ho/Kl` (groups var-bound `v$/S$`) | pending (round 51) | 14h31m at the plan's round start (2026-10-22T11:09) and counting | 3 — rounds 48 (`e5c926c` 10-22T06:16:51), 49 (`f304646` 08:57), 50 (`43ca0bf` 11:04) |

Callee generations are read from the committed allowlist (one generation per commit that touched it:
`02302c5`, `2ca8d01`, `7d8bf2f`, `7ad7fad`); version/mtime for rows 2–5 come from
`verifiers/baseline.json` `measured_against` at `2ca8d01`, `7d8bf2f`, `7ad7fad` and from
`.ufo/round-46/evidence/S2/g1-strings-census.json` (`binary.stat`, `version_stdout`) for 18.12.3.
Row 6 is my own read of the installed binary.

## What changed besides the callee name (from the committed fixtures)

- **Argument count: unchanged — 3 everywhere.** `jDe(e, BWr, "CLAUDE.md")` (clean),
  `Dl(e, BWr, "CLAUDE.md")` / `I5(e, BWr, "CLAUDE.md")` / `Co(e, "gemini", "GEMINI.md")` (newcallees),
  `lq(u, f$, "AGENTS.md")` / `Xl(u, "gemini", "GEMINI.md")` (18.12.5), `bq(u, v$, "AGENTS.md")` /
  `Ho(u, "gemini", "GEMINI.md")` / `Kl(u, "gemini", "GEMINI.md")` (live 18.12.6).
- **Quoting: unchanged.** The `.md` file is double-quoted in every generation; the group is a
  double-quoted lowercase literal or an identifier; wrapped calls keep the same trailing `,`/`)`.
- **First argument: `e` → `u`** between the `Co/Dl/Hj` generation and 18.12.5, but the pattern
  consumes it positionally (`[^\s,()]+`), so the gate never saw this rename.
- **Group variables are the second volatile leg, and older than the 18.12.5 rename:** var-bound
  groups already exist in the committed 18.12.2 live dump (`d$` → agents-md, `u$` → claude-md), and
  the names move per rebuild (`BWr` early, `f$/m$` in 18.12.5, `v$/S$` in 18.12.6). What is new in
  18.12.6 is not var-binding but a *collision*: `S$` is also bound to an unrelated string.
- **The declared pair set never changed:** the same 8 `(group, file)` pairs in every generation
  (18.12.2 census and 18.12.6 live dump: 11 call sites; the 18.12.5 fixture: 11 real call sites plus
  one planted alias decoy line; the clean/newcallees fixtures are curated subsets of 2 pairs each).

## Blocking detail for the 18.12.6 re-derivation (measured, not in the plan)

Adding `bq/Ho/Kl` to `OMP_CALL_RE` is necessary but not sufficient. The live dump binds the group
variable twice: `var S$ = "title"` (strings line 843423) and `var S$ = "claude-md"` (line 895604).
`constant_table` drops conflicted names, so `omp:claude-md/CLAUDE.md` extracts as
`('<unresolved-var:S$>', 'CLAUDE.md')`; `check_literal_present` then FAILs that row and
`check_no_uncovered_class` FAILs on the undeclared `omp:<unresolved-var:S$>/CLAUDE.md` — the live
gate stays **6/7**. The 18.12.2 dump shows the same var-bound leg resolving cleanly (`d$`/`u$`, no
collision), so this is a name-reuse hazard of the minified bundle, not a new call shape. The group leg
needs a scoped resolution (chunk-local or nearest-preceding assignment, or disambiguation by the
quoted file literal in the same call). With the callees added and resolution unchanged, the other 7
declared pairs do extract, so this is the only residual row.

## Assessment

A callee-name-independent shape rule (`<any identifier>(<v>, <group>, "<FILE>.md")`) would have kept
the callee leg green across all five renames: on the committed 18.12.2 live dump and on the live
18.12.6 dump it yields the same 8 declared pairs (11 call sites, no extra pair on either dump), so no
re-pin of callee names would ever have been needed. It would not by itself have kept
the gate green on 18.12.6 — the group leg is equally volatile and now ambiguous (`S$`), so the pair
still resolves to `<unresolved-var:S$>` — and it pays the over-match risk the module comment names at
`verifiers/verify_surfaces.py:138-160` ("a name harmless in one bundle over-matches the other";
"its live bundle is full of single-letter callees that must not feed this extractor"): the
fixtures' alias decoy `q(u, "evil", "EVIL.md")` is extracted by the unrestricted rule in 3 of the 4
omp fixtures as the undeclared class `omp:evil/EVIL.md`, which flips `no_uncovered_class` to FAIL
unless the group/file are additionally constrained to the declared pair set (that constraint removes
the decoy but, on the live dump, also removes `claude-md` until `S$` is resolved).

## Evidence (commands, exit codes)

- `git -C …/kotoba-shokunin log --format='%h %ci %s' -- verifiers/verify_surfaces.py verifiers/baseline.json verifiers/fixtures/surfaces/` → exit 0 (10 commits; callee generations at `02302c5`, `2ca8d01`, `7d8bf2f`, `7ad7fad`).
- `git show <c>:verifiers/baseline.json | python3 -c …` for `02302c5, 2ca8d01, a46321c, 7d8bf2f, 7ad7fad, 6fbbff5` → exit 0; omp mtimes `2026-10-14T08:39:28`, `2026-10-16T05:15:11`, `2026-10-19T12:35:55`, `2026-10-21T03:30:38`; `6fbbff5` (round 43) still pins `bf1e86a9` / 10-16T05:15:11.
- `stat -c '%y %s' /home/vgpnk/.local/bin/omp`; `sha256sum`; `omp --version` → `2026-10-21 20:37:24.615549837 -0300`, `85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4`, `omp/18.12.6`; exit 0 each.
- `strings -n 4 /home/vgpnk/.local/bin/omp > omp-18.12.6-strings.txt` → exit 0; 48,148,449 bytes, sha256 `953b19dffc4d51bd877330b90f0e994db38e90ee5f80575f08a31f3b73e7d96f`.
- `python3 -B shape_probe.py` (unrestricted vs allowlisted shape over every omp fixture, the opencode fixture, the live dump) → exit 0: live 18.12.6 11 hits / callees `{Ho:4, Kl:5, bq:2}` / 0 allowlisted; 18.12.5 fixture 12 hits (11 allowlisted) + `('evil','EVIL.md')`; clean fixture 3 hits (2 allowlisted) and newcallees fixture 6 hits (5 allowlisted), each with `('evil','EVIL.md')`; `strings-opencode-clean.txt` 0 hits.
- `python3 -B constrained_probe.py` (same rule, group/file constrained to the 8 declared pairs) → exit 0: 8 kept on the 18.12.5 fixture, 7 kept on the live dump, dropped `('title','CLAUDE.md')`.
- `python3 -B -c …` (unrestricted shape + the lane's `constant_table`/`extract_classes` over `.ufo/round-44/evidence/omp-live-18.12.2-strings.txt`) → exit 0: 11 hits, callees `{Gl, I5, Mo}`, 8 pairs; `d$ -> agents-md`, `u$ -> claude-md`, all 8 declared pairs extracted.
- `python3 -B live_extract_probe.py` (imports the lane's `extract_classes`/`constant_table`, no writes) → exit 0: current allowlist `[]`; with `Ho|Kl|bq` added → 7 declared pairs + `('<unresolved-var:S$>','CLAUDE.md')`; `S$` absent from the constant table, `v$ -> agents-md`.
- `python3 -B gate_sim.py` (lane's `check_literal_present` + `check_no_uncovered_class` on the live dump) → exit 0: current allowlist `literal_present False` (8 rows) and `no_uncovered False` (vacuity, 33 blind literals); callees added → `literal_present False` (1 row: `omp:claude-md/CLAUDE.md`), `no_uncovered False` (1 undeclared: `omp:<unresolved-var:S$>/CLAUDE.md`).
- Read-only compliance: no git/jj write command was run in the lane, the fleet root or any sibling lane; the lane received only this report file. All scratch files live in `/fast/scratch/hyaku/kotoba-r51/build/OmpRenameHistory/` (`shape_probe.py`, `constrained_probe.py`, `live_extract_probe.py`, `gate_sim.py`, `omp-18.12.6-strings.txt`). No tool was installed or upgraded.

## Remaining unknowns

- 18.12.3's callee names: unrecoverable from the lane — the only capture is its dump sha256
  (`5a8d1712…`, 48,098,273 bytes, not committed); the binary was replaced by 18.12.5.
- No 18.12.4 build is attested anywhere in the lane (searched `LOG.md`, `corpus/lessons/`, `.ufo/`).
- The round-18 binary's omp version string was never recorded (only sha `ff59fc1b`); `ff59fc1b`'s
  mtime is the one fact that dates it.
- Row 6's red duration is a snapshot at the plan's round start; it grows until the re-derivation lands.
