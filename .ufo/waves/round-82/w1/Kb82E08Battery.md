# Kb82E08Battery — round-82 base no-harm battery

Seat: Kb82E08Battery (leaf; no subagent dispatch, no background fleet work of my own beyond
this seat's measured gates). Date: 2026-10-30. Lane: kotoba-shokunin.

- Base measured: `47dbe8781657de563ff867caca6244d28e3db504` (round-82 base; master at intake).
- Scratch: `/fast/scratch/hyaku/kotoba-r82/Kb82E08Battery/` with `TMPDIR` exported to
  `<scratch>/tmp` for every command; scratch deleted on exit after receipts were copied.
- Sandbox A (plain shared clone): `<scratch>/clone`, `git clone --shared` of the lane,
  `checkout 47dbe87…`; toplevel asserted (`git rev-parse --show-toplevel` ==
  `/fast/scratch/hyaku/kotoba-r82/Kb82E08Battery/clone`) before any git use.
- Sandbox B (fleet-shaped): `<scratch>/fleetbox/` — every entry of fleet root
  `/home/vgpnk/Projects/shokunin` except `kotoba-shokunin` symlinked, plus a fresh
  `git clone --shared` checkout of the base at `fleetbox/kotoba-shokunin` (toplevel asserted).
- Disk guard checked before work: `disk-guard.sh status` exit 0 (`/fast/scratch/hyaku` 46% used).
- Tooling installs/upgrades: none needed, none performed (pacman host-wide pause respected).
- No production writes; no lane/fleet git or jj state touched; no commits; no fixture commits
  needed. All commands read-only on the lane; tip battery's own sandbox writes went to `$TMPDIR`.

## Direct battery (fleet-shaped sandbox B, cwd `fleetbox/kotoba-shokunin`)

Command-owned exits, no pipelines:

| # | Command (as run) | Exit | Key output (exact) |
|---|---|---|---|
| 1 | `python3 -B verifiers/check_gate_registry.py --rev 47dbe8781657de563ff867caca6244d28e3db504` | 0 | `gate registry rows conformant 64 of 64 lane verifiers; phantom 0` |
| 2 | `python3 -B verifiers/check_assertion_floors.py` | 1 | `FAIL checklist observed=1863 floor=1863 self_test_failures=1` (all other 15 rows PASS, e.g. `PASS pins observed=62 floor=62`, `PASS corpus_integrity observed=178 floor=164`) |
| 3 | `python3 -B verifiers/verify_skill_checklist.py --json` | 1 | `{"exit_code": 1, "pass": 10, "fail": 1, "na": 0}`; sole FAIL `governance.citation_resolves` |
| 4 | `python3 -B verifiers/verify_corpus_integrity.py --json` | 1 | DRIFT rows: `corpus.index.tracked_files 158 exp 157`, `corpus.index.unindexed 1 exp 0 / empty`, `corpus.pointers.report_total 117 exp 113`, `corpus.pointers.commit_total 50 exp 47`, `corpus.pointers.commit_unresolvable 1 exp 0 / empty`; PASS: `report_dead 0`, `stale_patterns 0`, `missing_paths 0`, `commit_nonhash 0` |
| 5 | `python3 -B verifiers/verify_corpus_independent.py --json` | 1 | independent derivation agrees: DRIFT `corpus.index.unindexed 1`, `corpus.pointers.commit_unresolvable 1`; PASS `report_dead 0`, `stale_patterns 0`, `missing_paths 0`; INFO counts tracked 158 / reports 117 / commits 50 |
| 6 | `python3 -B verifiers/check_correction_sweep.py --root .` | 0 | `correction sweep: 0 stale block(s)` |

Same six commands in plain sandbox A (directory named `clone`, parent not fleet-shaped) add
three shape artifacts that disappear in fleet shape: checklist `trigger.name_directory`
(`name 'kotoba-shokunin' != directory 'clone'`), checklist `trigger.citation_resolves`
(`../.ufo/reports/round-7/kotoba.md` does not resolve), and both corpus gates'
`report_dead 1` (`corpus/lessons/round-81.md:29: ../../.ufo/reports/round-76/kotoba.md` —
the target exists in the fleet root). Sandbox B is the faithful base form; sandbox A receipts
are kept for contrast.

## C2 self-test before-value (named in plan; authorized selftest)

In sandbox B: `python3 -B verifiers/verify_skill_checklist.py --self-test` → exit 1,
final line `1 failure(s) over 1863 assertions`. Failing arm (exact):
`governance: live round-65 corrections land, errata-excused` — the fixture-only arm reads the
live SCORECARD and flags dead citations (`.ufo/wapes` typo, `corpus/lessons/round-80-verifier-spotcheck.md:30,37`, `.ufo/reports/round-81/kotoba.md`). This reproduces the plan's declared
before (`1 failure(s) over 1863 assertions`, exit 1). Assertion count N=1863 ≥ 1863; no floor
reduction observed. Discriminators and fixture isolation are C2's repair scope, not this seat's.

## Tip battery, both repo forms (`--rev 47dbe8781657de563ff867caca6244d28e3db504`, fleet root pinned `/home/vgpnk/Projects/shokunin`)

- Form 1 (relative repo): `python3 -B verifiers/check_tip_battery.py --rev <base> --repo . --fleet /home/vgpnk/Projects/shokunin` from sandbox A root.
- Form 2 (absolute repo): same with `--repo /fast/scratch/hyaku/kotoba-r82/Kb82E08Battery/clone`.
- Both exit 1; outputs byte-identical (diff clean). Frozen line (exact, both):
  `fleet root /home/vgpnk/Projects/shokunin; guards 5 of 5; tip battery exit 0: 2 of 6`.
- Guard tally: `no-deletions PASS`, `floors PASS`, `instrument-size PASS` (402 added / 29 deleted vs pinned r73 base, cap 900), `instrument-pin PASS`, `spotcheck-identity PASS`; 9 INFO lines name round-73…round-81 spot-checks as not-base files.
- Gate exits inside the battery: registry 0; assertion_floors 1 (145.2 s); skill_checklist 1; corpus_integrity 1; corpus_independent 1; correction_sweep 0. Battery wall 148.4 s per form — inside the 280 s per-gate timeout, no timeouts.

No 6/6 tip-battery claim is made or implied: base reads 2 of 6, and the four reds are the
named debts below.

## Named base reds (debt, not new passing evidence)

1. C2 checklist self-test: `1 failure(s) over 1863 assertions` (arm reads live SCORECARD).
2. `governance.citation_resolves` live-gate FAIL (SCORECARD dead citations incl. `.ufo/wapes`).
3. `corpus.pointers.commit_unresolvable 1`: `corpus/lessons/round-81.md:8` cites
   `8b1cc1b00a9322cd8e231d87e015e1d75d20adc1`, which does not resolve even against the
   shared object store (`git cat-file -t` exit 128) — genuine at the base.
4. Corpus equal-count drift vs stale baseline (`tracked_files 158/157`, `report_total 117/113`,
   `commit_total 50/47`, `unindexed 1` = `corpus/lessons/round-81-verifier-spotcheck.md`) —
   the routed re-baseline duty, unchanged at the base.

## Receipts and integrity

27 receipt files (named command, cwd, HEAD, exact stdout/stderr, command-owned `.exit`) plus
`SHA256SUMS.txt` (30 rows, manifest sha256 `b162ecec919f31b5d23f4c54fad2c38a092c0912141b8457d76afee472a1370e`),
copied to the build dir before scratch deletion. Tip-battery exit files: `1`.
Red base gates remain named red; nothing here is an after-value and no production data was
scored.

## Risks / blockers

- Sandbox A vs B divergence is fully explained by shape (directory name, parent pointers);
  fleet form B matches the frozen commands' intent. L1 should quote fleetbox (B) numbers.
- The round-81 spot-check file is unindexed at base (INFO in battery, DRIFT in corpus gates);
  known routed maintenance, flagged for the re-baseline seat.
- No blockers. No peer-file dependencies were polled.

VERDICT: Base no-harm battery complete at 47dbe8781657de563ff867caca6244d28e3db504 in fleet-shaped scratch — gate registry 64/64 exit 0, correction sweep exit 0; named base reds retained red: checklist self-test 1/1863 failures, governance.citation_resolves FAIL, corpus commit_unresolvable 1, equal-count drift; tip battery (both repo forms, identical) guards 5/5, battery 2 of 6, exit 1 — no 6/6 claim; no production changes.

DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/w1/Kb82E08Battery.md ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E08Battery-receipts/
