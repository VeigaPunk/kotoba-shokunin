# Substrate-pin guard (round 23)

The round-21/22 named debt closed executably: the `measured_against` pins in
`verifiers/baseline.json` had **zero readers** — `grep -c measured_against
verifiers/*.py verifiers/*.sh` → 0 across all six instruments, and corrupting
the omp sha (or deleting the whole block) left every gate green (round-22
scout M6, proven executably; the 2026-10-16 omp rebuild `ff59fc1b`→`bf1e86a9`
passed `verify_harness_claims.py` 28/28 while the surfaces gate burned).

`verifiers/check_substrate_pins.py` (round 23, merged design per scouts
D1-D3/V1-V12 from the round-22 P1-P8 specs; file sha256 `fafe88d881eb…`) enforces
them: it hashes the live omp and opencode binaries (sha256 both; omp mtime
compared **ns-exact** via `stat().st_mtime_ns` — the naive `fromisoformat()
.timestamp()` parse under-reads the 9-digit fractional pin by 874 ns and
false-drifts) and diffs against the pins. It **hashes bytes, never executes**
the binaries — an exec writes to `opencode.log`, which is another gate's input
(round-22 scout F9). opencode's mtime is a 1985 packer constant and unpinnable;
only its sha is enforced.

## Exit ladder

0 all pins hold · 1 a pin drifted (`DRIFT`), a required pin is absent from the
baseline (`PIN_ABSENT`), or the whole `measured_against` block is missing/null
(`VACUOUS` — the round-22 M6-D2 class: the block must not be silently
deletable) · 2 environment unreadable (binary missing/EACCES/directory) · 3
baseline missing/unparseable or a malformed pin value (the round-22 P6-D1
TypeError class — no tracebacks, ever). `--json` mirrors the ladder in an
`exit_code` field.

## Verification battery (all re-run by the integrator at landing)

- live: `python3 verifiers/check_substrate_pins.py` → exit 0, `OK 3/3 pins
  hold`, omp mtime `delta 0 ns`.
- `--self-test` → `0 failure(s) over 46 assertions` over
  `verifiers/fixtures/pins/` (mini.bin sha256 `d3b4640e…` — byte-identical to
  the round-22 P4 design; tripwire.bin is a 0755 sentinel that appears only if
  exec'd, turning hash-never-exec into an assertion; per-case pin JSONs are
  generated in tmp because mtimes are not checkout-stable — scout D4).
- six red probes on /tmp baseline copies: sha drift → 1 naming the pin
  (text and `--json`); mtime-only drift → 1 naming `omp_binary_mtime`;
  missing binary → 2 naming the path; corrupt baseline JSON → 3 no traceback;
  missing/null `measured_against` → 1 `VACUOUS`; one pin deleted → 1
  `PIN_ABSENT`.
- red-before replay: a baseline copy re-pinned to the round-18 omp sha
  `ff59fc1b…` → exit 1 `DRIFT omp_binary_sha256` — the state the 2026-10-16
  rebuild actually produced while the harness gate kept printing its passing
  count.
- determinism: two live runs byte-identical; read-only (baseline hash
  unchanged, no exec — scout V3 strace: exactly one execve, the python
  interpreter itself).

## Defect classes closed (round-22 evidence)

P7-C9 silent shrink: deleting one pin exited 0 `OK 2/2` on the canonical
prototype → here `PIN_ABSENT` exits 1. P6-D1/P7-C1 TypeError: non-string pin
values trace-backed → here exit 3 with a named error. M6-D2 silent block
deletion → here `VACUOUS` exit 1. P1's 874 ns parse trap → integer-ns compare,
tolerance 0.

## Honest ceiling

Pin equality is a **change detector, not provenance**: it proves the bytes at
the pinned paths match the pinned hashes at check time — not that those bytes
are the ones the census measured, not that the paths were not swapped before
first pinning, and not that unpinned substrate (session caches, registries,
the opencode log grammar) is unchanged. A red guard is fixed by re-recording
the pin **plus a mechanism note** (what moved and why), never by weakening the
pin. Host-local: a fresh clone elsewhere has no binaries and gets exit 2.

Report: `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/reports/round-23/kotoba.md`.
