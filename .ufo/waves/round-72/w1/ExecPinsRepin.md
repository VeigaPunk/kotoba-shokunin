# ExecPinsRepin — round 72 wave 1 (build): host-substrate pin move (C2 draft)

**Verdict.** The pin move is drafted as five patches against the base and proven in a
fleet-shaped sandbox: `check_substrate_pins.py` reads **exit 2, `DRIFT 3/3 pins failed`**
before and **exit 1, `DRIFT 1/3 pins failed: opencode_binary_sha256`** after — i.e. **2 of 3
pins hold** (omp sha256 and the ns-exact omp mtime, `delta 0 ns (tolerance 0 ns)`). The
third pin **cannot honestly hold** from this seat: the opencode half is a new lineage
(v2.1.4) that no surface has been derived on, so I did **not** move `opencode_binary_sha256`
onto those bytes; the measured v2.1.4 identity is recorded in an append-style note instead.
All four touched scripts' `--self-test` still exit 0 at their **exact** floors
(62 / 175 / 10 / 123). Consequence for C2: with this patch alone the counter reads
`pins OK 2/3; surfaces pass 5 of 7`, so C2's frozen predicate (`k == 3`, `p == 7`) is
**not** reachable until OC-1…OC-6 are re-derived on the v2.1.4 dump by the derivation seat.

## 1. Host substrate re-measured (2026-10-25), my own values

```
$ sha256sum /home/vgpnk/.local/bin/omp.real /home/vgpnk/.opencode/bin/opencode /home/vgpnk/.local/bin/omp
85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4  /home/vgpnk/.local/bin/omp.real
ca9b3ee262e33bb4e7aa0e1230dc61086a474c8c8016b980081d0719712fd2e7  /home/vgpnk/.opencode/bin/opencode
ed62a41ec662fd80b3ca522896375b75cec4638e413dd2592f109a716853b2e1  /home/vgpnk/.local/bin/omp
$ stat -c '%n %y %s' /home/vgpnk/.local/bin/omp.real /home/vgpnk/.opencode/bin/opencode
/home/vgpnk/.local/bin/omp.real 2026-10-21 20:37:24.615549837 -0300 256702432
/home/vgpnk/.opencode/bin/opencode 1985-10-26 05:15:00.000000000 -0300 240416944
$ python3 -c "import os,datetime;st=os.stat('/home/vgpnk/.local/bin/omp.real');print(st.st_mtime_ns)"
1792625844615549837
$ /home/vgpnk/.opencode/bin/opencode --version
opencode v2.1.4
```

- omp: **identical bytes to the r51 pin** (`85d9daf3…`) and the **same ns-exact mtime**
  (`2026-10-21T20:37:24.615549837-03:00`, `st_mtime_ns` 1792625844615549837). The omp half
  is a **path move, not a rebuild** — confirmed against
  `verifiers/baseline.json:5-6`, which carries those two values.
- `~/.local/bin/omp` is a 1,680-byte Bourne wrapper, not a binary. Its own bytes say so
  (`sed -n '2p;13p' /home/vgpnk/.local/bin/omp`):

  ```
  # omp crash-restart wrapper (installed 2026-10-23 after a SIGSEGV freeze series
  # Real binary: ~/.local/bin/omp.real (override with OMP_REAL).
  ```

  Quotes are 13 and 8 words; I dropped the rest of line 2 after the word `series`.
- opencode: new lineage, **v2.1.4**, sha256 `ca9b3ee2…`, size 240,416,944. Its mtime
  (`1985-10-26T05:15:00…`) is a normalized stamp — **no mtime pin exists for opencode**
  (`EXPECTED_PINS` in `verifiers/check_substrate_pins.py:76-80` is omp-sha, omp-mtime,
  opencode-sha only), so nothing mtime-shaped was pinned to it.

## 2. Patch set (deliverables)

Under `.ufo/waves/round-72/w1/build/ExecPinsRepin/`:

| file | change |
|---|---|
| `patches/check_substrate_pins.py.patch` | `BINARIES` → `~/.local/bin/omp.real`, `~/.opencode/bin/opencode`; docstring host-anchor paragraph re-written (round 72) |
| `patches/verify_surfaces.py.patch` | `DEFAULT_BINARIES` → same two paths; a round-72 comment above the dict; an append-only `GENERATION NOTE (round 72)` beside the round-47 note |
| `patches/verify_harness_claims.py.patch` | `OMP_BIN` → `omp.real`, `OC_BIN` → `~/.opencode/bin/opencode`; docstring substrate table re-written |
| `patches/verify_harness_independent.py.patch` | `DEFAULT_OMP_BINARY` → `omp.real` (+ comment) |
| `patches/baseline-json.patch` | two append-style `measured_against` notes: `omp_round72_note`, `opencode_round72_note` |
| `patches/all.patch` | the five above as one patch |

`git apply --stat all.patch` → `5 files changed, 42 insertions(+), 16 deletions(-)`. **No
check logic, threshold, tolerance or pin key moved**: the pins file's diff touches only the
docstring (`:39-49`) and the two `BINARIES` values (`:65-69`); the ns-exact parser, the
sha256 comparison, the hygiene/discovery guards and `EXPECTED_PINS` are byte-identical to
the base. Strictness is therefore unchanged, only the file each pin is resolved against.

`baseline.json` keeps `opencode_binary_sha256` at the 1.19.4 bytes
(`538fcb1b…`, `verifiers/baseline.json:11`) and adds:

- `omp_round72_note` — the path move, wrapper sha, and the re-measured omp sha/mtime/size
  with "no value moved";
- `opencode_round72_note` — v2.1.4 path, version, sha256, size, normalized mtime, the fact
  that the npm 1.19.4 path is gone, and **why the pin is deliberately not moved**.

The new keys do not trip the discovery regex (`^<prefix>_binary_<kind>$`): the patched
guard still checks exactly 3 pins —
`python3 -c "import json;...['measured_against']"` lists the notes, and
`check_substrate_pins.py --json` emits 3 check records, no `UNSUPPORTED` row.

## 3. Proof in a fleet-shaped sandbox

Construction (per contract): `P=$(mktemp -d /tmp/k72fleet-ExecPinsRepin.XXXX)`, every entry
of `/home/vgpnk/Projects/shokunin` except `kotoba-shokunin` symlinked in,
`git clone --shared -q <lane> $P/kotoba-shokunin`. The **before** tree was a second such
sandbox checked out at the base `c69711ee08279609374d895bb0f3c8c18ccf15c9`
(`git -C … rev-parse HEAD` → `c69711ee…`); the **after** tree is `e61fd294…` (whose
`verifiers/` and `SKILL.md` are identical to the base —
`git diff --stat c69711e..HEAD -- verifiers/ SKILL.md` is empty) with `all.patch` applied.
`git apply --check all.patch` against a `git archive` of the base tree: clean.

### 3.1 `check_substrate_pins.py` (the item's headline)

Before, at base, from the sandbox root:

```
$ python3 -B verifiers/check_substrate_pins.py
ERROR UNREADABLE opencode_binary_sha256: [Errno 2] No such file or directory: '/home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe'
FAIL omp_binary_sha256: sha256 drift: expect=85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4 got=ed62a41ec662fd80b3ca522896375b75cec4638e413dd2592f109a716853b2e1
FAIL omp_binary_mtime: mtime drift (sha256 not compared): pinned_ns=2026-10-21T20:37:24.615549837-03:00 observed_ns=1792799242557636701 delta_ns=173397942086864 tolerance_ns=0
FAIL opencode_binary_sha256: UNREADABLE: [Errno 2] No such file or directory: …
DRIFT 3/3 pins failed: omp_binary_sha256, omp_binary_mtime, opencode_binary_sha256
exit=2
```

After, patches applied, same command, same sandbox shape:

```
$ python3 -B verifiers/check_substrate_pins.py
PASS omp_binary_sha256: 85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4
PASS omp_binary_mtime: delta 0 ns (tolerance 0 ns)
FAIL opencode_binary_sha256: sha256 drift: expect=538fcb1b6408c8d4608822acee19f7ff5b3a3eb3383c0633c4f06170857312a7 got=ca9b3ee262e33bb4e7aa0e1230dc61086a474c8c8016b980081d0719712fd2e7
DRIFT 1/3 pins failed: opencode_binary_sha256
exit=1
```

**Which pins hold after:** `omp_binary_sha256` (PASS) and `omp_binary_mtime` (PASS, 0 ns
delta at 0 ns tolerance). `opencode_binary_sha256` does **not** hold, and must not yet
(§5). The opencode row changed verdict class from `UNREADABLE` (path gone) to `DRIFT`
(real bytes measured, pin honestly stale) — a red that names the measured sha instead of
the missing path.

### 3.2 The other three touched scripts, defaults only (no flags)

```
before  verify_surfaces.py            exit 2  ERROR opencode binary not found: /home/vgpnk/.npm/_npx/…/opencode.exe
before  verify_harness_claims.py      exit 2  INCONCLUSIVE: template anchor occurs 0x in /home/vgpnk/.local/bin/omp (want 1)
before  verify_harness_independent.py exit 2  SUBSTRATE template marker absent from the omp binary

after   verify_surfaces.py            exit 1  pass 5 / fail 2  (FAIL surfaces.literal_present, FAIL surfaces.opencode_extract)
after   verify_harness_claims.py      exit 1  17/28 checks pass (11 DRIFT, all catalogue/db/log rows)
after   verify_harness_independent.py exit 0  24 derived, 4 scoped out, 0 unlanded (of 28 named checks)
```

Surfaces' two reds are exactly the two the plan predicts for the v2.1.4 bytes:
`surfaces.opencode_extract: vacuity: extraction produced 0 class(es) from 7 rule(s)` and
`surfaces.literal_present: … opencode:instructions/CONTEXT.md (literal 'CONTEXT.md' absent
from opencode dump)`. The `pass 5 fail 2` figure matches the plan's `--opencode-binary`
reading, now reached from the **default** path.

`verify_harness_claims.py`'s 11 DRIFTs are catalogue growth (`omp.catalogue.total
observed=206 expected=7`, `oc.roots.names_plus_builtin observed=75 expected=7`, …), not
substrate rows; §4 proves they are not caused by this patch.

### 3.3 Defaults-only equivalence proof

The patch must change *which file* is read, never *what is checked*. So I ran each base
script with the new paths passed explicitly and diffed against the patched script at its
defaults:

```
base pins     --omp-binary …/omp.real --opencode-binary …/.opencode/bin/opencode   vs patched default → diff: identical output
base surfaces --omp-binary …/omp.real --opencode-binary …/.opencode/bin/opencode   vs patched default → diff: identical output
base harness  --omp-bin    …/omp.real --oc-bin         …/.opencode/bin/opencode     vs patched default → diff: one line, a live timestamp
```

The harness diff is `newest catalogue 2026-10-25T21:45:12.721Z` vs `…21:45:20.370Z` — a
wall-clock observation of the live session tree, not a check outcome. No PASS/FAIL/DRIFT
line differs in any of the three.

## 4. Self-tests versus `verifiers/floors-registry.json`

`--self-test` on each touched script, before (base tree) and after (patched tree):

| instrument | before | after | floor (`floors-registry.json`) |
|---|---|---|---|
| `check_substrate_pins.py` | `0 failure(s) over 62 assertions`, exit 0 | `0 failure(s) over 62 assertions`, exit 0 | `pins` 62 |
| `verify_surfaces.py` | `0 failure(s) over 175 assertions`, exit 0 | `0 failure(s) over 175 assertions`, exit 0 | `surfaces` 175 |
| `verify_harness_claims.py` | `self-test: 0 failure(s) over 10 assertions`, exit 0 | `self-test: 0 failure(s) over 10 assertions`, exit 0 | `harness` 10 |
| `verify_harness_independent.py` | `0 failure(s) over 123 assertions`, exit 0 | `0 failure(s) over 123 assertions`, exit 0 | `harness_independent` 123 |

Counts are **equal**, not raised, so no bump-in-step edit to `floors-registry.json` or the
guard docstring is due. The guard itself agrees (`verifiers/check_assertion_floors.py`,
46 s):

```
PASS harness observed=10 floor=10
PASS surfaces observed=175 floor=175
PASS pins observed=62 floor=62
PASS harness_independent observed=123 floor=123
FAIL checklist observed=1862 floor=1862 self_test_failures=1
exit=1
```

The single FAIL is the checklist arm the plan records as inherited from r71
(`expected a red the r71 errata row removed`); it is untouched by these patches and its
row's count is unchanged.

## 5. The pin that cannot honestly hold — and why

`opencode_binary_sha256` stays at `538fcb1b…` (npm opencode-ai 1.19.4). Pinning
`ca9b3ee2…` now would assert that the lane's opencode surfaces were derived on v2.1.4;
they were not, and the derivation is measurably broken on those bytes:

```
$ python3 -B verifiers/verify_surfaces.py     # defaults → v2.1.4
FAIL surfaces.opencode_extract: vacuity: extraction produced 0 class(es) from 7 rule(s) …
FAIL surfaces.literal_present: 1 loader literal(s) not verifiable: opencode:instructions/CONTEXT.md
exit=1
```

So the pin is red **by design** until the OC-1…OC-6 re-derivation lands. The measured
identity is not lost: it is written into `opencode_round72_note` (path, version, sha256,
size, normalized mtime, dump sha256) with the sentence "pin deliberately NOT moved".
**C2 note for the L1:** the predicate's `k == 3` requires a `p == 7`-grade derivation
first; a pin-only patch cannot reach it, and lowering the target is the plan's Q45
decision, not this seat's.

## 6. Cross-instrument effects (observed, not inferred)

- `compare_harness_independent.py` (in the plan's no-harm battery): before `exit 2` in 0 s —
  `live instrument failed with no stdout: exit 2: INCONCLUSIVE: template anchor occurs 0x`.
  After: `exit 2` in 68 s with a substantive finding —
  `false blocker: scoped row omp.catalogue.found declares observable {"candidate_blocks": 9663, …} but recomputation gives {"candidate_blocks": 9676, …}`.
  Same exit code, so no harm; the join now runs and names live session-tree drift (13 more
  session files) that was previously masked by the unreadable substrate. That drift is
  pre-existing host state, not this patch.
- `check_opencode_repin.py` (r53 frozen counter) runs the tree's own `verify_surfaces.py
  --json` and `check_substrate_pins.py --json` with **no path flags** (`:19-23`), so on a
  patched rev it will read `surfaces pass 5 of 7 … pins OK 2/3` instead of `0 of 7 … 0/3`.
  Its predicate (`P == 7`, `k == n == 3`) still fails, so its exit stays 1 — no false green.
- No other verifier passes `--omp-binary/--opencode-binary/--omp-bin/--oc-bin` or
  references the old defaults (`grep -rn "omp-binary\|opencode-binary\|omp-bin\|oc-bin"
  --include=*.py verifiers/` → only the four touched files), so no caller breaks.

## 7. Shared-input provenance (recorded, since the dumps are wave-wide inputs)

`/tmp/k72-oc-strings.txt` and `/tmp/k72-omp-strings.txt` were **rewritten by another seat at
18:39** mid-wave (mtime moved, content did not):

```
$ sha256sum /tmp/k72-omp-strings.txt /tmp/k72-oc-strings.txt
953b19dffc4d51bd877330b90f0e994db38e90ee5f80575f08a31f3b73e7d96f  /tmp/k72-omp-strings.txt
020fb25393e5ce881ac2da70222acedebc5cef2d3810d07e4625b2cde885b089  /tmp/k72-oc-strings.txt
```

Both shas equal the values the dispatch states, before and after the rewrite. Provenance
spot-check against the live binaries by literal occurrence count (`grep -a -o … | wc -l`):

```
available_skills        binary_occ=4  dump_occ=4
skills rescanned        binary_occ=2  dump_occ=2
CONTEXT.md              binary_occ=0  dump_occ=0
disableClaudeCodePrompt binary_occ=0  dump_occ=0
system-context-builtins binary_occ=0  dump_occ=0
Compress into one routing hint (omp.real)  binary_occ=1  dump_occ=1
```

So the dumps do correspond to `~/.opencode/bin/opencode` (v2.1.4) and `~/.local/bin/omp.real`
for every literal I sampled, and the three absent literals are absent in both. I did not
re-dump either binary.

## 8. Files, cleanup, tooling

- Deliverables: `patches/{all,check_substrate_pins,verify_surfaces,verify_harness_claims,verify_harness_independent,baseline-json}.patch`
  and `evidence/{before,after}-*.txt` (raw outputs of every command quoted above) under
  `.ufo/waves/round-72/w1/build/ExecPinsRepin/`.
- No committed lane file was modified; the patches were authored and exercised only inside
  the sandbox clones. Scratch sandboxes (`/tmp/k72fleet-ExecPinsRepin.8QaM`,
  `/tmp/k72fleet-ExecPinsRepinB.2YPi`, `/tmp/k72w1-ExecPinsRepin.xfPE`) are deleted before
  return; no git write happened outside them, and no commit was made anywhere.
- No tool installed or upgraded. Long single runs recorded: surfaces default 15 s,
  harness_independent self-test 34 s, compare_harness_independent 68 s, assertion floors
  46 s — each run alone, none above 300 s.

## 9. Risks / open items handed to the L1

1. `k == 3` is unreachable without the OC-1…OC-6 re-derivation on v2.1.4; if the L1 lands
   this patch alone, C2's receipt will read `pins OK 2/3; surfaces pass 5 of 7`.
2. If a later seat does pin `ca9b3ee2…`, `opencode_round72_note` must be edited in the same
   change (it currently states the pin is deliberately not moved), and the note's
   "0 classes from 7 rules" sentence must be replaced with the re-derived counts.
3. `verify_harness_claims.py` still carries the 1.19.4-era check table in `baseline.json`
   (`checks` block: `oc.*` expectations of 7 skills); it now runs against a 75-skill host,
   so 11 rows read DRIFT. That is C3's calibration ground, untouched here.
