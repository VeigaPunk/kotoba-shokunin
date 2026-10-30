# Kb82C06Freshness — host pin timing attack (C1 freshness critic)

Seat: Kb82C06Freshness (critic, leaf; no subagent dispatch)
Claim under attack: C1 — host substrate re-pin, predicate
`check_substrate_repin_v2.py` prints `pins OK 3/3; surfaces pass 7 of 7;
removal ledger 3 of 3 verified`, exit 0. Base: `47dbe8781657de563ff867caca6244d28e3db504`.
Scope assigned: challenge host pin timing — file changed between derivation and
pin, executable wrapper mistaken for ELF, mtime precision mismatch, binary
absent then recreated. Freeze before/after digests; any drift invalidates the
after result. Read-only seat: no production mutation, no clone needed.

## Verdict up front

No drift. The after-value is NOT invalidated by any of the four timing
scenarios. One bounded caveat: 4 long-running omp daemons still execute the
pre-install image (omp/18.13.3, deleted inode); the pin certifies the installed
command path, which is what the frozen predicate and the loader re-derivation
both measure.

## Attack 1 — file changed between derivation and pin (TOCTOU)

Five independent measurements of `/home/vgpnk/.local/bin/omp` across the wave
window, all identical on sha256, mtime_ns, inode, size:

| measurer | artifact | sha256 (omp) | mtime_ns |
|---|---|---|---|
| Kb82E02Pins (14:53:55Z) | build/Kb82E02Pins-host-sha256.txt, -host-stat.txt | e7dd2b606c4ebe9d1a7bcfad1b8820db968cd6b05409fed1c6bc8db0b6a95a8f | 1793326786168359786 |
| Kb82E06Controls | build/Kb82E06Controls-host-measure.json | e7dd2b60…a95a8f | 1793326786168359786 |
| this seat BEFORE | build/Kb82C06Freshness-freeze-before.txt | e7dd2b60…a95a8f | 2026-10-29 23:19:46.168359786 -0300 |
| this seat AFTER (+30 s) | build/Kb82C06Freshness-freeze-after.txt | e7dd2b60…a95a8f | same |
| this seat FINAL (15:10:42Z) | build/Kb82C06Freshness-freeze-final.txt | e7dd2b60…a95a8f | same |

Inode 246583165, Links: 1, size 276244656 in every freeze; `diff` of the
before/after receipts shows header labels only (build/Kb82C06Freshness-freeze-*.txt).
opencode unchanged too: ca9b3ee262e33bb4e7aa0e1230dc61086a474c8c8016b980081d0719712fd2e7,
inode 145019585. No writer holds either path (`lsof` clean; running processes
hold only a deleted .bak, see attack 4). The proposed pin values in
build/Kb82E02Pins-repin.patch (sha256 e7dd2b60…, mtime
`2026-10-29T23:19:46.168359786-03:00`) equal every independent measurement.

## Attack 2 — executable wrapper mistaken for ELF

The round-72 arrangement (1,680-byte Bourne wrapper at `omp`, ELF at `omp.real`)
is gone. As of this wave:

- `ls /home/vgpnk/.local/bin/omp.real` → exit 2, "No such file or directory"
  (absent, not a dangling symlink). Only `omp` (276,244,656 B) and `omp-swarm`
  (11,185 B, unpinned) match `omp*` in that dir.
- Magic bytes `7f 45 4c 46` (od -N 64); readelf: Class ELF64, Type EXEC,
  Machine x86-64, entry 0x1a40600, 9 program headers — a genuine dynamically
  linked ELF, not a script, not a polyglot (first two bytes 0x7f 'E', no `#!`).
- `file(1)`: "ELF 64-bit LSB executable … not stripped" (exit 0).
- `omp --version` → `omp/18.14.0` (exit 0); embedded changelog line
  `## [18.14.0] - 2026-10-29` present in the bytes.
- `which omp` → `/home/vgpnk/.local/bin/omp` (the pinned path is the executed
  path for new invocations).

The repin patch's path move of `BINARIES["omp"]` from the dead `omp.real` to
`omp` therefore lands the pin on an ELF, not on a wrapper. Evidence:
build/Kb82C06Freshness-elf-check.txt.

## Attack 3 — mtime precision mismatch

Imported the frozen guard's own parser
(`verifiers/check_substrate_pins.py::parse_iso_ns`, via importlib on the base
tree, no repo mutation) and ran it on the proposed pin stamp:

- pin `2026-10-29T23:19:46.168359786-03:00` → epoch_ns 1793326786168359786,
  tolerance_ns 0 (9-digit fraction = exact instant).
- live `stat().st_mtime_ns` → 1793326786168359786. delta_ns = 0 → PASS.
- fabricated 8-digit (µs-precision) pin parses with tolerance_ns 9 — the guard
  reports the window rather than silently weakening, and the actual pin does
  not use it.
- materially different instant → DRIFT (delta 2786 ns shown).

The documented 874-ns float-truncation hazard does not bite: the pin is the
ns-exact 9-digit ISO form the guard requires. opencode's mtime is the
reproducible-build stamp 1985-10-26 05:15:00.000000000 -0300 and carries no
mtime pin (sha256 only), so no precision exposure on that row. Evidence:
freeze-before transcript inline in this seat's build artifacts; parse run
reproduced from build files.

## Attack 4 — binary absent then recreated

- The path is a stable regular file: inode 246583165, Links: 1, Birth
  2026-10-29 23:19:45.681939157 -0300, unchanged from before through final
  freeze — a create-then-write install (birth +486 ms before mtime), not an
  in-place rewrite, and no delete+restore occurred inside the measured window.
- Cross-seat inode agreement (E02 stat, E06 measure, this seat's 3 freezes) is
  the discriminator that closes the perfect-restore loophole: sha+mtime alone
  cannot distinguish a stable file from a byte-identical recreation with
  `-r`-copied timestamps, but a recreation would change the inode. None did.
  Inode pinning itself is outside the frozen contract (PINS_TOTAL=3) — recorded
  as residual surface, not a defect of this claim.
- **Bounded caveat (provenance, not pin drift):** four omp daemons started
  2026-10-29 03:54–04:01 execute a deleted image —
  `/proc/<pid>/exe` → `/home/vgpnk/.local/bin/omp.1793326784107.2252158.0.bak
  (deleted)`, sha256 42d39fa8996fed9f999e26306e60e2fdbea0c0de0d0b2d68feba275f44c41d04
  on all four PIDs, embedded changelog `## [18.13.3] - 2026-10-28` → omp/18.13.3,
  the pre-install lineage (neither the r51 pin 85d9daf3… nor the current
  e7dd2b60…). These daemons hold the old inode via text reference; they hold no
  writer FD on the path file and cannot rewrite a running executable (ETXTBSY).
  Consequence: the pin certifies the installed command path (what a fresh exec
  runs, what `verify_surfaces.py`/`check_substrate_pins.py` read, and what the
  loader re-derivation dumped — strings-dump sha256 81277d3572277…, cited in
  build/Kb82E01Paths-loader-pairs-18.14.0.txt and matching
  build/Kb82E02Pins-omp-18.14.0.strings.sha256.txt). It does not certify the
  image of those 4 still-running daemons; on restart they exec the pinned
  18.14.0. This is inherent to path-based pinning and matches the frozen
  predicate's wording ("the bytes it measured" at the default path).

## No auto-update channel observed

`systemctl --user list-timers` has no omp/upgrade timer; `crontab` not installed;
no install receipts newer than the binary under ~/.local/share; lsof shows no
open writer on either pinned path. The install appears to be the manual
23:19:44–46 -03:00 swap on 2026-10-29 (rename-old-to-.bak + write-new +
unlink-bak, per the deleted .bak name pattern embedding epoch-ms 1793326784107).

## Consistency with sibling artifacts

- Proposed pins (Kb82E02Pins-repin.patch) == all independent measurements.
- Loader-pair derivation (Kb82E01Paths) was run on the same bytes: its header
  cites strings-dump sha256 81277d3572277… == Kb82E02Pins strings.sha256 file ==
  dump of the pinned e7dd2b60 image.
- Before receipt `.ufo/waves/round-82/receipts/before-pins.txt` (1 PASS / 2
  UNREADABLE, exit 2) is consistent with `omp.real` absent and the old default.

## Residual / out-of-contract risks (named, not scored)

1. sha+mtime pins cannot detect a byte-perfect recreation with restored
   timestamps; only cross-time inode witnesses close that window (done this
   wave: inode 246583165 stable across 5 measurements).
2. Running-daemon image divergence (18.13.3 vs pinned 18.14.0) persists until
   those 4 PIDs restart; anyone scoring "what code is executing right now"
   rather than "what the pinned path contains" must account for it.
3. A writer with user privileges could replace the path between any two checks;
   no such writer was observed (lsof clean, no timers, no cron).

VERDICT: No timing drift; all four attack scenarios resolved or bounded-caveated. The
C1 re-pin after-value may be scored against the frozen counter; the pin certifies
/home/vgpnk/.local/bin/omp bytes e7dd2b60… (omp/18.14.0), not the executing image of
the 4 still-running 18.13.3 daemons.

DELIVERABLES:
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/w1/Kb82C06Freshness.md
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C06Freshness-freeze-before.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C06Freshness-freeze-after.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C06Freshness-freeze-final.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C06Freshness-elf-check.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C06Freshness-writers.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C06Freshness-proc-check.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C06Freshness-deleted-image.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C06Freshness-install-trail.txt
