# Kb82C02Hermetic — C2 hermetic-checklist self-test: attack on the patch design

Seat role: critic (attack). Scope: C2 operability only (`verifiers/verify_skill_checklist.py --self-test`).
Base: `47dbe8781657de563ff867caca6244d28e3db504`. All work in scratch clone
`/fast/scratch/hyaku/kotoba-r82/Kb82C02Hermetic/clone` (pristine verifier sha256
`b7d7b0fca8be17cfa18e75fe4d130a0d429e34f5f4e1a30fdc5fb22a70539615`, restored and
re-verified after every experiment; no commits, no fleet/lane mutations).

## Headline

The numeric predicate alone (`0 failure(s) over N assertions`, N >= 1863, exit 0) is
defeated by all three proposed attack moves, singly or composed, in every tested
world. The predicate's second clause — the named arm is "replaced by isolated fixture
evidence, not deleted or remapped to success" — is the only load-bearing rejection,
and it must be enforced as a code/contract audit plus a red/green guard pair, not
inferred from the pass line.

## Worlds (all hermetic, scratch-only)

- **W_before** — clone at base, scratch parent symlinks replicating the production
  fleet-root layout (sibling lanes + `.ufo`). Pristine self-test:
  `1 failure(s) over 1863 assertions`, exit 1, failing arm
  `governance: live round-65 corrections land, errata-excused` with detail naming
  `SCORECARD.md:480 '.ufo/wapes'`, `:482 'corpus/lessons/round-80-verifier-spotcheck.md:30,37'`,
  `:484 '.ufo/reports/round-81/kotoba.md'` x2 and "2 recorded absence(s) excused,
  4 recorded correction(s) excused" — byte-for-byte the committed before receipt
  `.ufo/waves/round-82/receipts/before-checklist-selftest.txt`. Do-nothing control
  reproduced exactly. (`runs/w0-base-selftest.txt`)
- **W_drift** — W_before + 3 more dead rows appended to clone `SCORECARD.md`. Named
  arm fails with "(+3 more)"; the `LOG.md:2678 erratum is load-bearing` arm still
  passes: its assertions are relative (dropping the 2678 erratum / horizon 2677 must
  go red), invariant under append-only drift. (`runs/w1-drift-selftest.txt`)
- **W_driftline** — tamper of a sha-pinned line in live `LOG.md`.
- **W_bare** — clone whose parent does NOT mirror the fleet root. Pristine self-test:
  `2 failure(s) over 1863` (named arm + load-bearing arm): the `../` corrected
  tokens (`../.ufo/reports/round-60/kotoba.md`, `../.ufo/watchdog.log`) and `../`
  live subjects resolve against the repo's *parent directory*. Second, independent
  non-hermeticity: the self-test at base is host-layout-sensitive.
  (`runs/base-selftest.txt`)

## Attack matrix (each patch applied to pristine, run in W_before and W_drift, restored)

| Variant | Move | W_before | W_drift | Drift-invariant | N |
|---|---|---|---|---|---|
| A-nopad | delete named arm, no pad | exit 0 | — | — | **1862 < floor → target missed** (`runs/attackAnopad.txt`) |
| **A** | delete named arm + 1 constant-True pad | exit 0, 0/1863 | exit 0, 0/1863 | yes (outputs sha-identical) | 1863 |
| **B** | mock the live call to constant `("PASS", … "2 recorded absence(s) excused, 4 recorded correction(s) excused")` | exit 0, 0/1863 | exit 0, 0/1863 | yes | 1863 |
| **C** | skip `LOG.md:2678` load-bearing rec + pad | exit 1, 1/1863 (named arm still fails) | — | — | 1863 |
| **ABC** | A + C (no live reads remain; `grep -c live_repo` = 0) | exit 0, 0/1863 | exit 0, 0/1863 | yes | 1863 |

Receipts: `runs/attack{A,B,C,ABC}-*.txt`. Patches: `build/Kb82C02Hermetic.attack-*.patch`.

Key mechanics the attacks exploit:
- The named arm's rec asserts only `status == "PASS"` plus two detail substrings; a
  fabricated tuple satisfies it (B). `evaluated` is not asserted.
- The load-bearing arm never inspects the live call's verdict on current data; it
  only checks that synthetic variations (erratum dropped, horizon 2677) go red. It is
  drift-invariant, so B leaves it green and C is neither necessary nor sufficient.
- The N>=1863 floor catches naive deletion (A-nopad, 1862) but is numerically defeated
  by one `rec("pad: …", True, None)` constant-True assertion per deleted arm.
- All attacks confine edits to `self_test()`; the public live gate still reports
  `FAIL governance.citation_resolves: evaluated 1363` naming the genuinely dead
  citations (`runs/live-gate-clone.txt`) — a cosmetic self-test pass coexists with an
  honest live gate.

## Reference fix R and the discriminating discriminators

I implemented the minimal honest replacement to test the plan's required
discriminators (patch: `build/Kb82C02Hermetic.ref-fix-committed.patch`, fixtures:
`build/Kb82C02Hermetic.fixture-{LOG,SCORECARD}.md`):

- Build a synthetic governance repo in the existing tempdir world: 2723-line
  `LOG.md` / 158-line `SCORECARD.md` carrying the byte-pinned lines (errata 2111,
  2678; subjects 2533, 2580, 2676; notices 2619–2621, 2723; SCORECARD 158), one
  resolving subject (`corpus/live.md`), corrected-token targets created inside the
  fixture (including parent-level `../.ufo/...` targets, so no host-layout
  dependence). Arms: `governance: fixture round-65 corrections land, errata-excused`
  (PASS + 2 absences + 4 corrections excused) and the same load-bearing 2678 arm
  against the fixture.
- Two source variants: **R-runtime** (fixture texts copied from live files at run
  time) and **R-committed** (fixture texts committed under
  `verifiers/fixtures/checklist/governance-live/`).

Results:

| Test (plan discriminator) | A/B/ABC | R-runtime | R-committed |
|---|---|---|---|
| fixture valid correction green / missing correction red / restored-stale red / unrelated-dead-subject red (existing tempdir battery, real `check_governance_citations`) | pass (untouched) | pass | pass |
| modifying unrelated live governance (W_drift) does not change results | pass | pass (green, drift-invariant) | pass (green) |
| N >= 1863, no floor reduction | pass (pad) | 1863 | 1863 |
| disable the replacement guard → corresponding fixture fails | **n/a — nothing to disable; arm deleted or fabricated** | tamper pinned notice line 2619 in live LOG.md → exit 1, "line text drifted" (`runs/fixR-noticedrift.txt`) — guard load-bearing BUT the runtime copy retains a live-file dependence | tamper committed fixture notice → exit 1, "line text drifted" (`runs/fixRc-fixturetamper.txt`); tamper the LIVE notice line → still 0/1863 (`runs/fixRc-livetamper.txt`) |
| host-layout independence (W_bare) | n/a (attacks keep live reads except ABC, which is layout-free but evidence-free) | green (`runs/fixR-barelayout.txt`) | green |

Counterexample found while testing R: a minimal fixture with only the 6 excused
subjects trips the checker's own fail-closed `evaluated == 0` guard
("no checked governance citation subjects; … 2 recorded absence(s) excused, 4
recorded correction(s) excused") — a zero-subject cosmetic pass is impossible by
construction; the fixture must carry at least one resolving subject.
(`runs/fixR-wbefore.txt` first iteration.)

## Smallest safe correction (what the canonical judge must enforce)

1. **Named-arm provenance audit** — the rec `governance: live round-65 corrections
   land, errata-excused` must be replaced by a fixture-derived arm whose
   `(status, evaluated, detail)` comes from a real `check_governance_citations` call
   on an isolated world; reject any constant tuple (B) or a constant-True rec
   inventory diff showing `True, None` pads (A). N>=1863 alone never discriminates:
   both the 1:1 replacement and padded deletion yield exactly 1863.
2. **Disable-guard red/green pair on the committed fixture** — corrupting the
   replacement fixture (notice-line tamper or corrected-token deletion) must turn
   exactly that arm red and nothing else; deleting or mocking the arm must leave no
   guard to disable (A/B rejected by absence).
3. **Drift-invariance across W_drift** — necessary, not sufficient (A/B/ABC also
   pass); run the self-test, append dead rows to live governance, re-run, require
   byte-identical output.
4. **Committed, not runtime-copied, fixture texts** — R-runtime still fails when a
   pinned live line is tampered; copying pinned lines at run time keeps a live read
   (and a hard failure if the file is unreadable). The fixture is data and must be
   committed like the round-37 fence battery.
5. **Live gate untouched** — `--check governance.citation_resolves` must still FAIL
   on genuinely dead live citations (verified on the clone); any fix that mocks
   inside `check_governance_citations` itself breaks this and has a wider blast
   radius than the predicate allows.

## Impacted axes

- **Operability (C2)**: primary. The numeric self-test predicate is cosmetic against
  delete/pad/mock; the contract clause + guard pair carry the real weight.
- **Freshness (C1)**: none — C2 does not read the host extraction gates; no C1 files
  touched.

## Evidence inventory (all under build/)

- `Kb82C02Hermetic.runs/` — 21 run receipts + SHA256SUMS. Pivotal:
  `w0-base-selftest.txt` (before receipt reproduced, 1/1863), `attackA/B/ABC-*.txt`
  (0/1863 drift-invariant attacks), `attackAnopad.txt` (floor teeth, 1862),
  `fixRc-fixturetamper.txt` vs `fixRc-livetamper.txt` (guard red/green + hermeticity),
  `live-gate-clone.txt` (live gate still red).
- `Kb82C02Hermetic.attack-{A-delete-plus-pad,B-mock-constant-pass,C-skip-LOG2678,ABC-composite}.patch`
- `Kb82C02Hermetic.ref-fix-committed.patch` + `Kb82C02Hermetic.fixture-LOG.md` +
  `Kb82C02Hermetic.fixture-SCORECARD.md` (reference replacement, satisfies every
  plan discriminator; not for landing — L1 owns integration)

No installs/upgrades performed (none needed). Pacman untouched. Scratch clone left
pristine at base sha `b7d7b0f…` and deleted on exit after receipt copy.

VERDICT: the proposed C2 patch design (remove arms / mock PASS / skip LOG2678 bound)
meets the numeric predicate `0 failure(s) over 1863 assertions` in all worlds while
being pure cosmetics; only the contract clause "replaced by isolated fixture
evidence" plus a committed-fixture disable-guard red/green pair and a constant-True
pad audit reject it. Reference replacement patch provided that satisfies every
plan-required discriminator including drift-invariance, guard red/green, live-gate
preservation, and host-layout independence.

DELIVERABLES:
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/w1/Kb82C02Hermetic.md
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C02Hermetic.runs/ (21 receipts + SHA256SUMS)
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C02Hermetic.attack-A-delete-plus-pad.patch
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C02Hermetic.attack-B-mock-constant-pass.patch
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C02Hermetic.attack-C-skip-LOG2678.patch
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C02Hermetic.attack-ABC-composite.patch
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C02Hermetic.ref-fix-committed.patch
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C02Hermetic.fixture-LOG.md
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C02Hermetic.fixture-SCORECARD.md
