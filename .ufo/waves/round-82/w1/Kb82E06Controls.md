# Kb82E06Controls — round-82 C1 predata shortcut controls

Seat: Kb82E06Controls (leaf, build+attack). Scope: drive the UNCHANGED counter
`verifiers/check_substrate_repin_v2.py` against sandbox shortcut worlds and
report which worlds reach the frozen target
`host substrate re-derived: pins OK 3/3; surfaces pass 7 of 7; removal ledger 3 of 3 verified`
(exit 0), and which independent guard rejects each. No production after
measurement; no host mutation; no lane mutation.

## Identities and setup

- Base: `47dbe8781657de563ff867caca6244d28e3db504` (clone `--shared` at
  `/fast/scratch/hyaku/kotoba-r82/Kb82E06Controls/clone`, every git call `-C`,
  toplevel asserted before each mutation; world commits on branch
  `sandbox/Kb82E06Controls-controls`, subjects `sandbox: Kb82E06Controls <world>`,
  scratch identity).
- Counter: `verifiers/check_substrate_repin_v2.py` from the base tree,
  sha256 `629487a116bdf287f2bcd43652ead051b052efd0a32632b38a45fece6ed4b348`,
  identical to the blob at base (`counter_unchanged_at_base: true` in the
  summary receipt). Matches base-tree blob at W0/W4/W7 (see per-world receipts).
- Lane repo HEAD before/after the seat run: `006a834cee4339ede8620e10c3995d5226141c0a`
  — untouched (freeze commit; the seat never writes the lane).
- Runner: stdlib-only
  `.ufo/waves/round-82/build/Kb82E06Controls_controls.py`, honors `--work`
  (all temporaries under `/fast/scratch/hyaku/kotoba-r82/Kb82E06Controls/work`,
  `TMPDIR` set there; no hardcoded `/tmp`). Command-owned exits throughout (no
  pipelines). Disk guard checked before work: `/fast/scratch/hyaku` 47% used,
  427.7G free — OK. No installs/upgrades needed; none performed.
- No subagents, no background jobs, no pacman. Peak concurrent processes: 1
  (sequential world runs; slowest W7 17.1s, total runner wall 56s).

## Independent host measurement (predata guard evidence, non-mutating)

Measured by the runner itself, before any world run:

- `/home/vgpnk/.local/bin/omp`: ELF 64-bit x86-64, `omp/18.14.0`,
  sha256 `e7dd2b606c4ebe9d1a7bcfad1b8820db968cd6b05409fed1c6bc8db0b6a95a8f`,
  276,244,656 bytes, mtime ns `1793326786168359786` =
  `2026-10-29T23:19:46.168359786-03:00`.
- `/home/vgpnk/.opencode/bin/opencode`: sha256
  `ca9b3ee262e33bb4e7aa0e1230dc61086a474c8c8016b980081d0719712fd2e7`,
  240,416,944 bytes — byte-identical to the round-72 pin already in
  `verifiers/baseline.json` (opencode half needs no re-pin).
- `strings -n 4` live opencode dump: 1,237,844 lines; every
  `FROZEN_REMOVALS` anchor regex (`CONTEXT\.md`, `disableClaudeCodePrompt`,
  the name-priority array join, the claude-home join) matches NOTHING
  (`frozen_removal_anchors_all_absent: true`) — the ledger conjunct's live
  side holds on the current host.
- Receipt: `build/Kb82E06Controls-host-measure.json`.

## World results (unchanged counter, `--repo <clone> --rev <world>`)

| world | rev | exit | counter first line | reached |
|---|---|---|---|---|
| W0-base (do-nothing control) | 47dbe87… | 2 | `cannot evaluate: verify_surfaces.py reported 0 row(s) (exit_code 2: omp binary not found: /home/vgpnk/.local/bin/omp.real); pins 1/3 row(s) PASS, surfaces 0/0 check(s) PASS` | no |
| W1-path-only | 98559f44… | 1 | `pins OK 1/3; surfaces pass 7 of 7; removal ledger 3 of 3 verified` | no |
| W2-pin-only | 29294a12… | 2 | `cannot evaluate: verify_surfaces.py reported 0 row(s) … omp binary not found` | no |
| W3-fake-omp-elf | d5462df0… | 1 | `pins OK 2/3; surfaces pass 5 of 7; removal ledger 3 of 3 verified` | no |
| W4-stdout-stub-gates | 30e15d49… | 0 | **`pins OK 3/3; surfaces pass 7 of 7; removal ledger 3 of 3 verified`** | **YES** |
| W5a-unkept-class | 0aadd218… | 1 | line reads `3 of 3`; stderr `FAIL kept-identity: … opencode:config/instructions` | no |
| W5b-ledger-extra | 42716403… | 1 | `removal ledger 3 of 4 verified` (ledgered live class) | no |
| W5c-ledger-missing | b3bfab49… | 1 | `removal ledger 2 of 3 verified` (frozen class unledgered) | no |
| W6-stray-opencode-pin | cd32935e… | 1 | `pins OK 2/3; …`; stderr `FAIL substrate identity: pin(s) opencode_binary_sha256 PASS on bytes that are not the live opencode` | no |
| W7-path+pin, real gates, no re-derivation | 6fe12d16… | 0 | **`pins OK 3/3; surfaces pass 7 of 7; removal ledger 3 of 3 verified`** | **YES** |

W0 reproduces the fleet before receipt
`.ufo/waves/round-82/receipts/before-c1-counter.txt` byte-for-byte in message
and exit (2). Counter's own `--self-test` (unchanged code, fixture worlds,
no host read): exit 0, `0 failure(s) over 16 assertions`
(`build/Kb82E06Controls-counter-selftest.txt`).

World definitions (single-diff each from base, except as noted):

- W1: both instruments' omp default path `omp.real` → `/home/vgpnk/.local/bin/omp`;
  pins/baselines untouched. Pins 1/3: both omp rows DRIFT (stale sha/mtime).
  Surfaces 7/7 against the live 18.14.0 ELF with the round-51-era baseline.
- W2: `baseline.json` omp sha/mtime → live values; paths untouched. Pins would
  be 3/3 but the surfaces instrument still cannot find `omp.real` → 0 rows →
  exit 2. Pin freshness alone cannot satisfy the counter.
- W3: a small crafted ELF-magic file `verifiers/sandbox-fake-omp.elf`
  committed in-tree, both instruments' omp default retargeted to it (tree-local
  `Path(__file__)` resolution, the only hermetic way — `git archive` paths are
  random), its sha pinned. Result: the **fake omp sha pin is counted as
  holding** (pins 2/3; the mtime row DRIFTs only because `git archive` cannot
  carry a filesystem mtime — a harness artifact the counter's own self-test
  works around with a committed stamp file). The REAL surfaces gate rejects
  the fake (5/7). Finding: the counter's substrate-identity guard binds ONLY
  the `opencode_binary_sha256` row; any omp bytes a tree pins count if the
  surfaces gate passes. W3 without an honest surfaces measurement (i.e. W4's
  stub) reaches target — W4 subsumes that combo.
- W4: `check_substrate_pins.py` and `verify_surfaces.py` replaced by stdlib
  stdout stubs printing canned 3×PASS / 7×PASS JSON; the opencode pin names
  the true live opencode sha (a hostile tree can read the world-readable host
  binary just as the counter does). Ledger file and baselines untouched.
- W5a/b/c: W4 stubs + one ledger/baseline move each (silent drop of a non-frozen
  opencode class; a live class added to the ledger; a frozen class removed from
  the ledger).
- W6: W4 stubs but the opencode pin names sha256 of non-live bytes.
- W7: W1+W2 combined (live path + live pins), REAL instruments, no baseline,
  ledger, or census edit of any kind.

## Findings

**F1 (the exact weakness L1 asked for). The unchanged counter alone accepts
W4-stdout-stub-gates: exit 0, frozen line `pins OK 3/3; surfaces pass 7 of 7;
removal ledger 3 of 3 verified`.** Every in-counter guard fails to reject it,
by construction: the row-count guards are satisfied exactly (3 pin rows, 7
checks); the vacuity guard sees non-empty reports; the substrate-identity
guard is satisfied because the stub names the true live opencode sha256
(`ca9b3ee2…`); the ledger conjunct holds against the real live dump because
the ledger is the base's exact `FROZEN_REMOVALS` set and all anchors are
absent (independently confirmed above). The counter's docstring predicts
exactly this shape and defers to external guards — confirmed live.

Independent guards that reject W4, by name:

1. **Reviewed postimage gate blobs / freeze receipt** — the world's
   `check_substrate_pins.py` blob is `ddc925e3546891f72923d74690823072409ceb56a9d547ad9ddad951fe31646c`
   and `verify_surfaces.py` is `c6466f0e2ee3141230bb13276f90976c1ddb994329ce37fac88e57c9d60d08e2`,
   vs base `c896e5b91dd998de845905ff23ddc4c03e8964e3efbabefadac8b7bedb5d9667`
   and `df0c7ccaab930bf22359d7c5ec174a1429d11e78e856b7e3272d9fe29baf8bab`
   (per-world receipts carry full tables). A 30-line stub and a 25-line stub
   cannot hash-match the 579-line / 2585-line frozen instruments; blob review
   without execution rejects the world before any numeric claim.
2. **Independent loader-pair derivation (S251 / E19-style)** — the tree
   contains no 18.14.0 extraction evidence at all (no re-derived loader-group
   calls or instruction literals); the freshness claim's evidentiary core is
   absent even though the counter's number prints.
3. **Independent host sha256/mtime measurement** — corroborates the stub's
   opencode pin but cannot detect that no measurement took place; it binds
   the claim to the host only after guards 1–2 establish the gates were real.
4. **Gate self-tests** — the stub gates have no `--self-test`; running the
   frozen instruments' self-tests on the proposed blobs fails immediately.

**F2. W7 (live path + live pins, REAL gates, zero re-derivation edits) also
reaches the target, and is the honest minimal candidate — not a defect.**
The real `verify_surfaces.py` dumped the real 18.14.0 ELF and found full
parity with the existing 33 omp + 9 opencode class baseline (7/7), twice
independently (W1 and W7); the pins name the host values my independent
measurement confirms (`e7dd2b…`, `168359786` ns). So the frozen numeric
target is met by a path+pin-only tree diff. Two consequences, stated exactly:

- The loader re-derivation the plan requires ("re-derive the new binary's
  loader-group calls and instruction literals before updating defaults and
  pins") is, on this host transition, **evidence that confirms the baseline
  rather than data that changes it** — it cannot be skipped, because guards
  1–4 above reject any tree that doesn't carry it (S251 receipt), but a
  faithful re-derivation is expected to leave `surfaces-baseline.json` and
  `census-removals.json` untouched (class set unchanged — the unchanged
  class-set comparison guard also passes W7).
- The counter's surfaces conjunct is doing real measurement work (W3's fake
  failed 5/7 through the REAL gate), so F1's weakness is specifically
  *gate substitution*, not gate inadequacy: the counter trusts the tree's
  instruments by design, and only external blob/derivation guards police that
  trust boundary.

**F3. Counter-native guards verified live and green:** W5a kept-identity
(silent class removal → exit 1 via stderr; note the frozen line on stdout
still reads `3 of 3` — the exit code and stderr are the signal, the headline
line alone is not), W5b ledger-exactness with a live class (`3 of 4`), W5c
frozen-set completeness (`2 of 3`), W6 substrate-identity on the opencode pin
(`2/3` + named FAIL). W0/W2 vacuity (0-row report → exit 2, never `0 of 7`).
W1/W2 show the conjuncts are individually load-bearing: neither path nor pin
freshness alone reaches target.

**F4. Certification boundary, as frozen by the plan:** a C1 green is
meaningful only as `unchanged counter (sha256 629487a1…) AND unchanged
class-set comparison AND reviewed gate blobs AND independent host sha256/mtime
matching the pins AND the S251 loader re-derivation receipt`. The counter's
`3/3,7/7,3/3` alone certifies nothing — W4 is the constructive proof.

## Risks / notes

- W3's mtime DRIFT is a fixture-harness artifact (`git archive` drops mtime);
the sha-pin holding on fake bytes is the real signal and is reported as such.
- The opencode substrate is byte-stable since round 72; all C1 motion is on
  the omp half.
- Scratch (`/fast/scratch/hyaku/kotoba-r82/Kb82E06Controls/`) deleted after
  receipts were copied; re-running the delivered runner reproduces every
  world and receipt (world revs recorded in `Kb82E06Controls-summary.json`).
- No blockers. L1's freeze sha for the counter was measured here as
  `629487a1…ed4b348` at base `47dbe87` if the integration receipt needs it.

VERDICT: unchanged counter run on base + 9 sandbox shortcut worlds; 2 of 10
worlds reach the frozen 3/3,7/7,3/3 target — W4 stdout-stub gates (true
weakness; rejected only by external blob-review / loader-derivation /
host-measurement / self-test guards, named) and W7 path+pin with REAL gates
(honest minimal candidate; surfaces parity with 18.14.0 confirmed by the gate
itself). All counter-native shortcut guards (ledger exactness, kept-identity,
substrate identity on the opencode pin, row-count, vacuity) verified live and
green on W5a/W5b/W5c/W6/W0/W2. Counter self-test 0/16.

DELIVERABLES:
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/w1/Kb82E06Controls.md
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E06Controls_controls.py
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E06Controls-summary.json
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E06Controls-host-measure.json
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E06Controls-counter-selftest.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E06Controls-world-{W0-base,W1-path-only,W2-pin-only,W3-fake-omp-elf,W4-stdout-stub-gates,W5a-unkept-class,W5b-ledger-extra,W5c-ledger-missing,W6-stray-opencode-pin,W7-path-plus-pin-no-rederivation}.txt
