# Kb82C01Counter — attack on the unchanged C1 counter: omp stub + real opencode

Axes: freshness; operability. No production after-value measured, no axis score, no 6/6 tip-battery claim.

## Question

Can a revision meet the unchanged round-72 counter
(`verifiers/check_substrate_repin_v2.py`, sha256 `629487a116bdf287f2bcd43652ead051b052efd0a32632b38a45fece6ed4b348`)
by pinning an **omp stub** in the pins instrument while running the **real opencode** — and does the
outside E19 guard (`build/Kb82E19PinGuard_guard.py`, sha256 `61ace2b9e586f34f9344e0147a5f586b94c9680e17f900494f76b36ecbfd77e3`,
byte-identical to the peer's frozen manifest) reject that world?

## Why the counter is expected to be hollow for omp

The counter measures only ONE live substrate: `HOST_OPENCODE = ~/.opencode/bin/opencode`
(its own `strings -n 4` dump). Its pin-holding guard `holds()` special-cases only the
`opencode_binary_sha256` row against those live bytes; every other PASS row counts with no
independent measurement — there is no live-omp read anywhere in the counter. The pins
instrument (`check_substrate_pins.py --json`) is run with no path flag, so the *tree's own*
`BINARIES` dict and `baseline.json` decide what an omp pin is compared against: a tree may
point `BINARIES["omp"]` at any host path, pin that file's sha256/mtime, and its pins script
reports PASS. `git archive` cannot carry an mtime, so the stub lives at a fixed-utime host
path outside the tree (scratch), referenced by absolute path.

## Worlds (scratch clone `/fast/scratch/hyaku/kotoba-r82/Kb82C01Counter/clone`, deleted after
receipts; commits preserved in `build/Kb82C01Counter_worlds.bundle`)

- **World A — honest control** (`96c1ebee0b119025675519c8c7476d677a441265`): both instruments'
  omp default moved `omp.real` → `/home/vgpnk/.local/bin/omp` (real ELF, 18.14.0); baseline
  pins the live sha256 `e7dd2b606c4ebe9d1a7bcfad1b8820db968cd6b05409fed1c6bc8db0b6a95a8f` and
  ns mtime `2026-10-29T23:19:46.168359786-03:00`. Diff vs base: 3 files, 4/4 lines (paths + 2 pins).
- **World B — the attack** (`3436e2c569794d78e3e73583a0dc323d315400b0`): pins instrument's
  `BINARIES["omp"]` → a 279-byte stub at a fixed-mtime scratch path
  (sha256 `2b64866f540af87d00637bd93444ef02fe861669f401673944adff41ed216adf`,
  mtime_ns `1792600644618559837`, pinned ns-exact); `verify_surfaces.py` omp default → the REAL
  host omp; opencode real and pinned everywhere (`ca9b3ee2…`, the live sha the counter itself
  dumps). Instruments otherwise byte-identical to base.
- **World C — both instruments on the stub** (`aacc21d051c2f0dbc8250a6c45a8dab38fa74c66`):
  boundary probe for the counter's remaining backstop.

## Exact counter outputs (unchanged lane counter, `--repo <clone> --rev <rev>`)

World A — exit **0**, elapsed 17 s:

```
host substrate re-derived: pins OK 3/3; surfaces pass 7 of 7; removal ledger 3 of 3 verified
substrate opencode: /home/vgpnk/.opencode/bin/opencode sha256 ca9b3ee262e33bb4e7aa0e1230dc61086a474c8c8016b980081d0719712fd2e7 bytes 240416944 strings 1237844
```

World B — exit **0**, elapsed 16 s, stdout **byte-identical** to world A
(same sha256 `eff2065964e7251426628530c3eb3cbe3b5ce003856119b1476fc239680975de`): the frozen
target line is met by the shortcut. Direct pins-instrument evidence (world B tree run
directly, exit 0) shows the stub carrying two of the three PASS rows:

```
omp_binary_sha256 PASS expect 2b64866f540af87d observed 2b64866f540af87d /fast/scratch/hyaku/kotoba-r82/Kb82C01Counter/stub/omp
omp_binary_mtime  PASS expect 2026-10-21T13:37 observed 1792600644618559 /fast/scratch/hyaku/kotoba-r82/Kb82C01Counter/stub/omp
opencode_binary_sha256 PASS expect ca9b3ee262e33bb4 observed ca9b3ee262e33bb4 /home/vgpnk/.opencode/bin/opencode
```

World C — exit **1**: `pins OK 3/3; surfaces pass 5 of 7; removal ledger 3 of 3 verified`,
`FAIL surfaces: 5 of 7 check(s) PASS`. The counter's surfaces conjunct catches a full-stub
world (string-extraction fails on the stub), but cannot see a pins-side-only stub.

## Does the outside E19 guard reject them? YES

Guard run (never executes candidate instruments; frozen live identities embedded):

- World A: exit **0**, all 15 checks PASS — the honest re-pin world is accepted.
- World B: exit **1**. RED checks, exactly the three omp-identity checks:
  - `omp.sha-pin` — pinned `2b64866f…` ≠ live `e7dd2b606c…`;
  - `omp.ns-mtime-pin` — pinned `1792600644618559837` ≠ live `1793326786168359786`;
  - `check_substrate_pins.py.omp.defaults` — the tree's pins instrument default measures the
    279-byte non-ELF stub at the scratch path, identity-unequal to the live host omp.
  GREEN: `opencode.*`, both `*.executable-AST` (instruments byte-identical to base),
  `verify_surfaces.py.omp.defaults` (real host binary), `census.exact-base-identities`,
  `removal-ledger.unchanged`.
- World C: exit **1**, both instruments' omp defaults RED (plus the two pin checks).

## Numeric limitation (declared, not suppressed)

The unchanged C1 counter's `pins OK 3/3` conjunct is **hollow for the omp half**: any tree
that points its pins instrument at a self-pinned substrate (stub, older build, or any file)
while keeping the surfaces instrument and the opencode pin honest meets the full frozen
target with exit 0 and output indistinguishable from the honest world. The counter's own
output names only the opencode substrate, so the two worlds' receipts are byte-identical.
This is precisely the gap the plan's outside-guard set must cover: the frozen E19
independent guard rejects the shortcut world on independent live-host measurement
(sha256, ns mtime, default-path identity, AST shape, census/ledger equality). Per the plan's
rule, a shortcut meeting the target invalidates the numeric certification **unless the
independently frozen guards reject it** — here they do reject it, so the certification stands
only with E19 (or an equivalent independent omp-identity measurement) in the scoring path.
Smallest safe correction if a future round wants the counter self-sufficient: have the
counter measure the live host omp (sha256 + ns mtime at a frozen path, as it already does for
opencode) and hold the two omp pin rows against those bytes. Not applied — the counter is
frozen and this seat returns findings only.

## Reproduction

`build/Kb82C01Counter_worlds.bundle` carries the three world commits
(`fixture/worldA`, `fixture/worldB`, `fixture/worldC`); base
`47dbe8781657de563ff867caca6244d28e3db504` is the prerequisite. World B/C re-runs need the
stub recreated: 279 bytes, sha256/mtime in `build/Kb82C01Counter_worlds.json` (content:
`#!/bin/sh\n# fixture omp stub -- NOT the host substrate\n` + `\x7fELF` + `stub-loader-agents-md\n`×10).
Counter runs: `python3 -B verifiers/check_substrate_repin_v2.py --repo <clone> --rev <world>`;
guard runs: `python3 -B build/Kb82E19PinGuard_guard.py --repo <clone> --rev <world>`.

## Receipts (all command-owned exits, no pipelines)

- `build/Kb82C01Counter_counter-worldA.{stdout,stderr}` — exit 0, frozen line.
- `build/Kb82C01Counter_counter-worldB.{stdout,stderr}` — exit 0, frozen line (identical bytes to A).
- `build/Kb82C01Counter_counter-worldC.{stdout,stderr}` — exit 1, `surfaces pass 5 of 7`.
- `build/Kb82C01Counter_pins-worldB-direct.json` — pins instrument PASS rows on the stub.
- `build/Kb82C01Counter_guard-world{A,B,C}.json` (+ empty `.stderr`) — guard exits 0/1/1.
- `build/Kb82C01Counter_worlds.json`, `build/Kb82C01Counter_worlds.bundle`, `build/Kb82C01Counter_SHA256.txt` (16 files).

Host facts measured live this seat: omp 18.14.0 ELF at `~/.local/bin/omp`,
sha256 `e7dd2b606c4ebe9d1a7bcfad1b8820db968cd6b05409fed1c6bc8db0b6a95a8f`, 276244656 bytes,
mtime `2026-10-29T23:19:46.168359786-0300`; `omp.real` absent (matches plan before-receipt);
opencode sha256 `ca9b3ee262e33bb4e7aa0e1230dc61086a474c8c8016b980081d0719712fd2e7`. Both match
E19 `HOST_FROZEN` exactly. No installs/upgrades; pacman untouched; load average ≤ 2.2 during runs.

VERDICT: Unchanged C1 counter IS shortcuttable by omp stub + real opencode (exit 0, frozen line, output byte-identical to the honest world) — declared a numeric limitation of the counter, never suppressed; the outside E19 guard rejects the shortcut world (exit 1, omp.sha-pin / omp.ns-mtime-pin / check_substrate_pins.py.omp.defaults red) and accepts the honest world (exit 0, 15/15).
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/w1/Kb82C01Counter.md ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C01Counter_counter-worldA.stdout ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C01Counter_counter-worldA.stderr ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C01Counter_counter-worldB.stdout ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C01Counter_counter-worldB.stderr ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C01Counter_counter-worldC.stdout ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C01Counter_counter-worldC.stderr ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C01Counter_pins-worldB-direct.json ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C01Counter_guard-worldA.json ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C01Counter_guard-worldB.json ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C01Counter_guard-worldC.json ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C01Counter_worlds.json ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C01Counter_worlds.bundle ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C01Counter_SHA256.txt
