# Kb82E02Pins — C1 baseline pin owner: host omp 18.14.0 independent byte identity + candidate re-pin

Seat: Kb82E02Pins (leaf; C1 baseline pin owner). Axes: freshness, operability.
Base: `47dbe8781657de563ff867caca6244d28e3db504` (intake). Frozen counter: `verifiers/check_substrate_repin_v2.py` (round-72 counter, unchanged; target line `host substrate re-derived: pins OK 3/3; surfaces pass 7 of 7; removal ledger 3 of 3 verified`, exit 0 — target only, NOT executed by this seat on production).
Scratch: `/fast/scratch/hyaku/kotoba-r82/Kb82E02Pins/` (clone `--shared`, checkout 47dbe87, toplevel asserted; no commits; TMPDIR under scratch). No installs/upgrades (none needed; pacman paused). No production file, pin, ledger, census, index, or jj state touched; no seat commit/push.

## 1. Independent host measurement (read-only; exact outputs retained)

Commands ran with command-owned exit capture (no pipelines on the measured commands).

```
$ /home/vgpnk/.local/bin/omp --version
omp/18.14.0            # exit=0
$ sha256sum /home/vgpnk/.local/bin/omp /home/vgpnk/.opencode/bin/opencode
e7dd2b606c4ebe9d1a7bcfad1b8820db968cd6b05409fed1c6bc8db0b6a95a8f  /home/vgpnk/.local/bin/omp
ca9b3ee262e33bb4e7aa0e1230dc61086a474c8c8016b980081d0719712fd2e7  /home/vgpnk/.opencode/bin/opencode   # exit=0
$ stat /home/vgpnk/.local/bin/omp
Modify: 2026-10-29 23:19:46.168359786 -0300   (epoch ns 1793326786168359786)
size 276244656, inode 246583165, mode 0755, regular file  # exit=0
$ file /home/vgpnk/.local/bin/omp
ELF 64-bit LSB executable, x86-64, dynamically linked, not stripped
```

- `/home/vgpnk/.local/bin/omp` is **the ELF itself** (regular file, not a symlink; ELF magic verified by `file` and by `grep -a -m1 '## \[18\.14\.0\]'` on the bytes → `## [18.14.0] - 2026-10-29`, exit 0 — version claim bound to bytes two ways: exec output and embedded changelog).
- No `omp.real` exists anywhere in `~/.local/bin`; the round-72 1,680-byte wrapper generation is gone from the host (directory listing retained in scratch receipts).
- opencode at `/home/vgpnk/.opencode/bin/opencode`: sha256 `ca9b3ee2…` — **byte-identical to the pinned round-72/53 pin**; mtime 1985-10-26 (reproducible-epoch stamp, ns 499162500000000000). No opencode re-pin needed or performed; no version exec performed on it.
- Own `strings -n 4` dump of the new omp (GNU binutils 2.47): 2,546,730 lines / 47,434,077 bytes, sha256 `81277d3572277febcaf0853f10cf8778c64920f58a13fba98ef0accbb70a8319`, empty stderr (dump artifact retained as a sha stub in build/).
- Cross-seat corroboration on every identity field: `Kb82S03Knowledge-current-bytes.txt` (S03; sha/size/mtime identical; S03 did not exec `--version`), `Kb82E01Paths.md` §1, `Kb82E19PinGuard_before.json`, `Kb82E17CorpusPins.md` §5 — four independent measurements agree with this seat's.

## 2. baseline.json `measured_against` semantics (inspected, unchanged in structure)

- Pin keys: exactly `omp_binary_sha256`, `omp_binary_mtime`, `opencode_binary_sha256` — mirrored by `check_substrate_pins.py:EXPECTED_PINS` (lines 78–82). Discovery (`DISCOVER_RE`, line 83) additionally resolves any other `<substrate>_binary_<kind>`-shaped key → UNSUPPORTED if unresolvable (vacuity guard); my added `omp_round82_note` is not pin-shaped and is invisible to the pin set. Pin keys are exact-bytes (Unicode-category hygiene), exit ladder 3 > 2 > 1 > 0.
- mtime value format: ISO-8601 with a timezone offset and exactly 9 fractional digits (round-51 note documents this as the parsed format). Verified with the guard's own `parse_iso_ns`: candidate stamp `2026-10-29T23:19:46.168359786-03:00` → epoch ns `1793326786168359786` == live stat mtime, tolerance 0. Matches the PinGuard freeze constraint (timezone + exactly nine fractional digits, no tolerance widening).
- Version is **note metadata only** — no version pin key exists; versions live in `omp_roundNN_note` rows. Historical notes (r21/r44/r51/r72, opencode r53/r72) are history and stay byte-identical.

## 3. Candidate patch (returned only; L1 integrates)

Two forms, both generated from the scratch clone at base 47dbe87 + edits (no commits):

1. **`build/Kb82E02Pins-repin.patch`** — sha256 `31694f0d882ddc9834922184355353fccba97abdf2100c062ba8716ba144483c`, 44 lines, 2 files:
   - `verifiers/baseline.json`: `omp_binary_sha256` 85d9daf3… → `e7dd2b606c4ebe9d1a7bcfad1b8820db968cd6b05409fed1c6bc8db0b6a95a8f`; `omp_binary_mtime` → `2026-10-29T23:19:46.168359786-03:00`; new `omp_round82_note` (path/version/sha/mtime/size/dump-sha + "byte identity only, no expected-count changes; loader re-derivation precedes scored integration").
   - `verifiers/check_substrate_pins.py`: `BINARIES["omp"]` `/home/vgpnk/.local/bin/omp.real` → `/home/vgpnk/.local/bin/omp` + comment.
2. **`build/Kb82E02Pins-baseline-only.patch`** — sha256 `c94c15804bd3390cad99b4d78466ffd4816a8b6f691174397029fd1e6e1d7a32`, 23 lines, baseline.json hunks only. **Use this form together with `Kb82E01Paths-c1-paths.patch`** (E01 owns all four default-path edits incl. the same pins-guard hunk — same target value, different comment; L1 should take exactly one of the two overlapping hunks). Scope guard: no `surfaces-baseline.json`, `census-removals.json`, expected-count, or assertion-floor changes anywhere in either form.

## 4. Control worlds (scratch clone, authorized; NOT a production after-score)

| world | command | result |
|---|---|---|
| candidate + live host | `python3 -B verifiers/check_substrate_pins.py --json` | 3 PASS / 0 fail, **exit 0**; mtime row delta_ns 0, tolerance_ns 0 (before receipt was 1 PASS / 2 UNREADABLE, exit 2) |
| negative: sha pin zeroed | same | omp_binary_sha256 DRIFT, **exit 1** |
| negative: mtime pin −1s | same | omp_binary_mtime DRIFT, **exit 1** |
| restored candidate | same | 3/3 PASS, **exit 0** |
| guard self-test (isolated fixtures) | `--self-test` | `0 failure(s) over 62 assertions`, **exit 0** |

JSON row outputs retained: `Kb82E02Pins-control-{neg-sha,neg-mtime,pos-restored}.json`; raw host measurement: `Kb82E02Pins-host-sha256.txt`, `Kb82E02Pins-host-stat.txt`. Green is therefore discriminating (both DRIFT arms fire), not vacuous.

## 5. Re-pin gating status

- Condition "re-pin only after independent loader derivation": materially satisfied by landed peer evidence — E01: unchanged round-52 extractor derives all 8 loader pairs on the 18.14.0 dump, zero undeclared, and the full `verify_surfaces.py` gate runs **7/7 PASS** on live dumps of both harnesses with patched defaults; E12 (github group): exact pair match both directions, loader-literals live, 7/7 decoys; E10/E13 per-group probes landed; E17: census 42/42 and removal ledger anchors recompute exactly from committed bytes, live opencode dump byte-identical to the round-72 dump; E19: frozen independent predata guard (9/9 fixture arms) pins the live identities outside candidate control. Remaining loader seats (E09, E11, E14–E16) were still in flight at this report; L1 owns the final integration order.
- This patch is **CANDIDATE / unscored production**. The scored measurement is L1's run of the frozen counter at the integrated revision after the predata freeze receipt exists: target `pins OK 3/3; surfaces pass 7 of 7; removal ledger 3 of 3 verified`, exit 0. The pins half of that line is what this patch enables; the surfaces half additionally requires E01's default-path patch (and no baseline/surfaces/ledger semantic change, per PinGuard scope rules).

## Risks / notes

- Overlap with E01 on `check_substrate_pins.py:64-72` is documented above; both hunks produce the identical resulting value — dedupe at integration, no semantic risk.
- The 18.14.0 dump line count in this seat's receipt (2,546,730) differs by ±1 from E12's count (2,546,731) — dump sha256 agrees exactly (`81277d35…`); the delta is a trailing-newline counting artifact between producers, not a bytes difference in the dump file (both sha-bound).
- E19's freeze requires candidate mtime stamps with timezone + exactly 9 fractional digits: satisfied.
- No axis-score claim, no 6/6 tip-battery claim, no production after-value scored. Pacman untouched; no PATH-dir writes; disk guard checked (scratch 428G free) before the strings dump.

VERDICT: PASS (candidate) — host omp 18.14.0 byte identity independently measured (sha256 e7dd2b606c4ebe9d1a7bcfad1b8820db968cd6b05409fed1c6bc8db0b6a95a8f, mtime ns 1793326786168359786, version double-bound); opencode pin verified unchanged (ca9b3ee2…); baseline.json pin semantics inspected; minimal candidate re-pin patch returned (values + note + pins-guard path default) with discriminating control worlds (3/3 PASS exit 0; both DRIFT arms exit 1; guard self-test 62/62) and full loader-derivation gating evidence corroborated across E01/E10/E12/E13/E17/E19. Patch stays unscored until L1 integrates it with the paths patch after the predata freeze.

DELIVERABLES:
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/w1/Kb82E02Pins.md
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E02Pins-receipt.json (sha256 4a965f9df271b78123bf11fe670068ca0312653e34ef8816f33ab8e3e354b77b)
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E02Pins-repin.patch (sha256 31694f0d882ddc9834922184355353fccba97abdf2100c062ba8716ba144483c)
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E02Pins-baseline-only.patch (sha256 c94c15804bd3390cad99b4d78466ffd4816a8b6f691174397029fd1e6e1d7a32)
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E02Pins-omp-18.14.0.strings.sha256.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E02Pins-control-neg-sha.json
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E02Pins-control-neg-mtime.json
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E02Pins-control-pos-restored.json
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E02Pins-host-sha256.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E02Pins-host-stat.txt
