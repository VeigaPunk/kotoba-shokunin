# PinsRepin — round 51 build, C1 companion (omp 18.12.6 re-pin)

**Result: `OK 3/3 pins hold` (exit 0) after the re-pin; base was `DRIFT 2/3 pins failed: omp_binary_sha256, omp_binary_mtime` (exit 1).** The re-pin touches only `verifiers/baseline.json` § `measured_against` (`omp_binary_sha256`, `omp_binary_mtime`, plus one new `omp_round51_note`); no other key, file, or gate moved.

## Files changed

- `verifiers/baseline.json` (the only file this seat owns) — clone
  `/fast/scratch/hyaku/kotoba-r51/build/PinsRepin/lane`, based on
  `43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10`.
- Patch delivered: `/fast/scratch/hyaku/kotoba-r51/build/PinsRepin/patch.diff`
  (`git diff 43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10 -- verifiers/baseline.json`;
  3 insertions, 2 deletions, one file).
- This report: `.ufo/waves/round-51/build/PinsRepin.md` (lane path).

No file in the lane checkout was edited other than this report. No git/jj write ran in the
lane, the fleet root, or any sibling lane; all writes happened in the private clone.

## What the re-pin records

| key | base value | new value |
|---|---|---|
| `omp_binary_sha256` | `fdbc8136084c9a10439569157b2af62312e2b0d801cab54c73e89476da798e7e` (omp/18.12.5) | `85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4` (omp/18.12.6) |
| `omp_binary_mtime` | `2026-10-21T03:30:38.135013187-03:00` | `2026-10-21T20:37:24.615549837-03:00` |
| `omp_round51_note` | absent | new key, `omp_round44_note` style |

`opencode_binary_sha256` (`179ca421…`) was left untouched and still holds.

## Format derivation (how the mtime string was chosen)

The guard's `parse_iso_ns` (`verifiers/check_substrate_pins.py:169-193`) reads an ISO-8601
stamp with a UTC offset, takes the fractional digits as nanoseconds and sizes the acceptance
window to the pin's own quantum. A 9-digit fraction therefore yields `tolerance_ns = 0`, so
the pin must reproduce `st_mtime_ns` exactly.

- `os.stat('/home/vgpnk/.local/bin/omp').st_mtime_ns` → `1792625844615549837`.
- Rendered in the host's local zone (−03:00, the same offset the round-47 pin used) with 9
  fractional digits → `2026-10-21T20:37:24.615549837-03:00`.
- UTC form of the same instant: `2026-10-21T23:37:24.615549837+00:00`.
- The pin string is ns-exact: the guard reports `delta 0 ns (tolerance 0 ns)`.

`sha256sum /home/vgpnk/.local/bin/omp` → `85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4`;
`/home/vgpnk/.local/bin/omp --version` → `omp/18.12.6`; the binary's embedded changelog carries
`## [18.12.6] - 2026-10-21` (and `## [18.12.5] - 2026-10-21` for the previous build).

`omp_round51_note` records: re-pin time `2026-10-22T14:19:07.958107Z`, version `omp/18.12.6`,
sha256 `85d9daf3…`, mtime `2026-10-21T20:37:24.615549837-03:00`, the previous pin
`fdbc8136…` (omp/18.12.5) with its mtime `2026-10-21T03:30:38.135013187-03:00`, and the
`-03:00` ns-exact note. It names the opencode pin as unchanged.

## Evidence (commands, exit codes)

All commands ran in the clone `/fast/scratch/hyaku/kotoba-r51/build/PinsRepin/lane` against
the host's installed binaries (the guard is host-anchored).

Base, before the edit:

```
$ python3 -B verifiers/check_substrate_pins.py            → EXIT=1
FAIL omp_binary_sha256: sha256 drift: expect=fdbc8136… got=85d9daf3…
FAIL omp_binary_mtime: mtime drift: pinned_ns=2026-10-21T03:30:38.135013187-03:00 observed_ns=1792625844615549837 delta_ns=61606480536650 tolerance_ns=0
PASS opencode_binary_sha256: 179ca421…
DRIFT 2/3 pins failed: omp_binary_sha256, omp_binary_mtime

$ python3 -B verifiers/check_substrate_pins.py --self-test → EXIT=0
0 failure(s) over 62 assertions

$ python3 -B verifiers/verify_harness_claims.py             → EXIT=1
21/28 checks pass; DRIFT: omp.db.rows, omp.offered.skills, omp.cache.misses,
omp.catalogue.total, omp.catalogue.missing_names, omp.cache.verified_skills,
oc.roots.names_plus_builtin
```

After the edit:

```
$ python3 -B verifiers/check_substrate_pins.py            → EXIT=0
PASS omp_binary_sha256: 85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4
PASS omp_binary_mtime: delta 0 ns (tolerance 0 ns)
PASS opencode_binary_sha256: 179ca421…
OK 3/3 pins hold

$ python3 -B verifiers/check_substrate_pins.py --json     → EXIT=0
{"pass": 3, "fail": 0, "exit_code": 0}   (three PASS checks, mtime delta_ns 0, tolerance_ns 0)

$ python3 -B verifiers/check_substrate_pins.py --self-test → EXIT=0
0 failure(s) over 62 assertions        (identical count to base; the self-test runs on
                                        temporary fixtures only, never on baseline.json)

$ python3 -B verifiers/verify_harness_claims.py             → EXIT=1
21/28 checks pass; the same seven DRIFT checks as the base run, same observed values
```

Proof that the edit moves no harness-claims check: the base and after stdout files are
byte-identical.

```
$ diff harness_base.txt harness_after.txt   → no differences (exit 0)
$ md5sum harness_base.txt harness_after.txt
21df01a619af410208e0e2645780e53d  harness_base.txt
21df01a619af410208e0e2645780e53d  harness_after.txt
```

The reason is structural, not incidental: `verify_harness_claims.py` reads only
`baseline["checks"]` (`evaluate()`, line 570) and never `measured_against`
(`grep -c measured_against verifiers/verify_harness_claims.py` → 0). The 28 `checks` rows and
the `notes` block are untouched by this diff.

Secondary check that the re-pin does not move the primary C1 counter:
`python3 -B verifiers/verify_surfaces.py --json` → `{"pass": 5, "fail": 2, "exit_code": 1}`
before and after this edit (unchanged; that gate is the other seat's item and does not read
`baseline.json`).

Diff scope, in the clone:

```
$ git diff --stat 43ca0bfb… -- verifiers/baseline.json
 verifiers/baseline.json | 5 +++--
 1 file changed, 3 insertions(+), 2 deletions(-)
$ python3 -c "json.load(open('verifiers/baseline.json'))"  → parses; measured_against keys:
  ['omp_binary_sha256', 'omp_binary_mtime', 'omp_round21_note', 'omp_round44_note',
   'omp_round51_note', 'opencode_binary_sha256', 'command', 'round18_move', 'round47_note']
  checks: 28 entries
```

Only three keys are touched: the two pins and the new note. `omp_round51_note` is not
pin-shaped (`<prefix>_binary_<kind>` does not match it) and carries no hygiene characters,
so the guard's discovery pass does not pick it up — the guard still reports exactly three
pins.

## Risks and blockers

1. **The re-pin records the substrate as of 2026-10-22T14:19Z.** The pin holds only while
   `/home/vgpnk/.local/bin/omp` is byte-identical (sha256 `85d9daf3…`, mtime
   `2026-10-21T20:37:24.615549837-03:00`). A further omp rebuild re-breaks the guard the
   same way — that is the guard working, not a defect of this edit.
2. **`verify_harness_claims.py` is red (21/28, exit 1) on this host, before and after.**
   The drift is live-host state (11 offered skills vs 7 pinned, 17 db rows vs 14), not
   caused by the re-pin; the two runs are byte-identical. This seat did not touch the
   `checks` block, which is the right home for those expectations if the L1 wants them
   refreshed.
3. **Advisory, out of this seat's file scope:** `verifiers/verify_harness_claims.py:33-36`
   asks that a baseline update be followed by a `LOG.md` entry citing the script, and the
   round plan asks for a round-51 lesson/census line. Neither file belongs to this seat, so
   the L1 should carry the `LOG.md` line for the 18.12.6 re-pin.
4. No blockers: the pin format, the sha256 and the ns-exact mtime were all derived and
   verified against the guard's own parser.

## Tooling

No tool was installed or upgraded this round: the work needed only Python 3 stdlib
(`json`, `hashlib`, `os.stat`) and the tools already on the host (`sha256sum`, `stat`,
`git`). No pacman transaction was run; no host service was restarted.
