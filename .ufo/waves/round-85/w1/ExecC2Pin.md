# ExecC2Pin — round 85 w1 (C2 payload: substrate re-pin, attacked)

Date: 2026-11-04. Seat: ExecC2Pin (leaf executor). Lane: kotoba-shokunin.
Item: (a) re-point the four host-anchored omp path constants to this host's ELF; (b) stage
`baseline.json.candidate` with re-derived omp pins + `omp_round85_note`; (c) four controls on the
candidate in scratch; (d) surfaces before/after pair. No tool installs were needed (stdlib +
coreutils only); no pacman, no tooling-authorization events.

## (a) The four path edits (diffs retained in receipt.txt)

Each site gained the dated one-line comment
`# round 85: this host's omp is the ELF itself (omp/18.15.0); omp.real does not exist` and the path
moved `.real`-suffix → the ELF. Every other constant unchanged.

1. `verifiers/check_substrate_pins.py` — `BINARIES["omp"]`: `/home/vgpnk/.local/bin/omp.real` →
   `/home/vgpnk/.local/bin/omp`.
2. `verifiers/verify_surfaces.py` — `DEFAULT_BINARIES["omp"]`: same move.
3. `verifiers/verify_harness_claims.py` — `OMP_BIN = HOME / ".local/bin/omp"` (was `omp.real`).
4. `verifiers/verify_harness_independent.py` — `DEFAULT_OMP_BINARY = Path("/home/vgpnk/.local/bin/omp")`
   (was `omp.real`).

The superseded round-72 comment lines were left in place as history (mirrors the baseline.json
retained-note convention); the new round-85 line states the current truth directly above the constant.

## (b) The candidate — `w1/ExecC2Pin/baseline.json.candidate`

Byte-surgical copy of `verifiers/baseline.json` (exact diff: 3 lines), `verifiers/baseline.json`
itself untouched:

- `measured_against.omp_binary_sha256` =
  `6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f` — re-derived 2026-11-04 with
  `sha256sum /home/vgpnk/.local/bin/omp` (ELF 64-bit x86-64, 276,785,328 bytes, `omp --version` =
  `omp/18.15.0`).
- `measured_against.omp_binary_mtime` = `2026-11-01T17:11:07.281808804-03:00` — `st_mtime_ns`
  1793563867281808804 rendered as a ns-exact 9-digit ISO stamp at the fixed `-03:00` host offset;
  round-tripped through the checker's own `parse_iso_ns`: delta 0 ns, tolerance 0 ns.
- `measured_against.omp_round85_note` — version, sha256, size, mtime, the re-derivation commands,
  and that the 18.12.6 pin (omp.real, `85d9daf3…`, `2026-10-21T20:37:24.615549837-03:00`) is
  superseded: `omp.real` does not exist on this host and the `omp` path itself is now the ELF (the
  round-72 1,680-byte crash-restart wrapper is gone).
- `opencode_binary_sha256` unchanged (`ca9b3ee2…`, v2.1.4 — still holds, PASSes live).

## (c) Controls on the candidate (scratch, TMPDIR=scratch; full tails in receipt.txt)

| # | Command (cwd = lane) | Exit | Observed tail |
|---|---|---|---|
| 1 | `python3 -B verifiers/check_substrate_pins.py` (candidate NOT passed; real baseline unswapped) | 1 | `DRIFT 2/3 pins failed: omp_binary_sha256, omp_binary_mtime` — the instrument proves it reads the baseline against the new path |
| 2 | `… --baseline $S/c2-opencode-sha.json` (opencode sha under the omp pin) | 1 | `DRIFT 1/3 pins failed: omp_binary_sha256` |
| 3 | `… --baseline $S/c3-absent.json` (both omp pins deleted) | 1 | `PIN_ABSENT 2/3 pins failed: omp_binary_sha256, omp_binary_mtime` — absent pin is loud, never a silent pass |
| 4 | `… --baseline $S/baseline.json.candidate --omp-binary /home/vgpnk/.opencode/bin/opencode` | 1 | `DRIFT 2/3 pins failed: omp_binary_sha256, omp_binary_mtime` — different ELF must fail |
| + | green arm: `… --baseline $S/baseline.json.candidate` (defaults) | 0 | `OK 3/3 pins hold`; `omp_binary_mtime: delta 0 ns (tolerance 0 ns)` |

Instrument hygiene after the edit: `check_substrate_pins.py --self-test` → exit 0,
`0 failure(s) over 62 assertions`; `ast.parse` clean on all four edited files.

## (d) Surfaces before/after pair

- After the path edit: `python3 -B verifiers/verify_surfaces.py --json` → **exit 0, `"pass": 7`,
  `"fail": 0`**; its omp section reads `path: /home/vgpnk/.local/bin/omp`, sha256 `6737ee24…`,
  `source: "binary"` (payload archived as `surfaces-after.json`). No `--omp-binary` override needed —
  the C2 surfaces half holds through the default path.
- Base path arm: `… --json --omp-binary /home/vgpnk/.local/bin/omp.real` → exit 2,
  `"error": "omp binary not found: /home/vgpnk/.local/bin/omp.real"` (`surfaces-base.json`).

## Acceptance mapping

- Four path edits' diffs — receipt.txt § `git diff` (all four files).
- Candidate pin values — receipt.txt header + `baseline.json.candidate` (this dir).
- Four control receipts with exit codes — receipt.txt control battery + table above.
- Surfaces exit 0 pass 7 fail 0 after the edit — `surfaces-after.json`.

## Risks / hand-off notes

- `verifiers/baseline.json` is deliberately NOT edited (out of my ownership). Until the candidate is
  swapped in by the integrator, the default `check_substrate_pins.py` run stays exit 1 (control 1) —
  that drift is the proof the guard reads, and the candidate green arm shows the post-swap state.
- The `verify_harness_claims.py` / `verify_harness_independent.py` defaults now resolve to a real
  binary where they previously hit UNREADABLE (`omp.real` missing, exit 2). Their committed
  `checks` (template sha/bytes pinned against the 18.12.6 baseline) [INFERENCE] will now run live
  against the 18.15.0 ELF and may read DRIFT (exit 1) instead of UNREADABLE — same pre-existing red
  class ("recorded, not claimed"), now measurable. I did not run those two instruments (not in my
  item; their before/after belongs to the reviewers).
- The `omp` ELF is 18.15.0; `surfaces-baseline.json` extraction survives it (pass 7 / fail 0
  measured). No other file was written; scratch `/fast/scratch/hyaku/kotoba-r85/ExecC2Pin` was
  deleted after receipts were copied here.
