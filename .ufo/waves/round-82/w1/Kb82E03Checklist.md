# Kb82E03Checklist — C2 hermetic checklist self-test (round 82)

Seat: C2 code owner. Base: `47dbe8781657de563ff867caca6244d28e3db504`. Scope:
`verifiers/verify_skill_checklist.py` self_test live_repo governance arms → hermetic
fixture replay. No production edits; all work in scratch clone
`/fast/scratch/hyaku/kotoba-r82/Kb82E03Checklist/clone` (shared clone, base checkout,
every git call `-C`, toplevel asserted), `TMPDIR` under the seat root.

## What the patch does

`build/Kb82E03Checklist.patch` (single file, one hunk region +109/−15):

- **Removes** the two live-repo arms: `governance: live round-65 corrections land,
  errata-excused` (the failing named arm, base lines ~2519–2527) and the live half of
  `governance: LOG.md:2678 erratum is load-bearing`. Both read the evolving repo — the
  before receipt shows the landing arm red because live `SCORECARD.md` grew genuinely
  dead citations (`.ufo/wapes`, `corpus/lessons/round-80-verifier-spotcheck.md:30,37`,
  `.ufo/reports/round-81/kotoba.md`), and in a non-fleet-layout clone both arms are also
  red because the corrections' `..`-hop tokens only resolve against the fleet root.
- **Adds** a hermetic fixture replaying the identical pinned rows — the same
  `GOVERNANCE_ERRATA` / `GOVERNANCE_CORRECTIONS` constants — inside the existing
  `kotoba-governance-` tempdir: fixture repo `round-82-mirror/` with `LOG.md` (2800
  lines) and `SCORECARD.md` (200 lines) whose recorded lines are embedded as byte
  literals (LOG.md:2111, 2533, 2580, 2619, 2620, 2621, 2676, 2678, 2723;
  SCORECARD.md:158, all sha256-verified against the row digests at base and at live
  HEAD). Corrected-token `..` hop targets (`../.ufo/reports/round-60/kotoba.md`,
  `../.ufo/watchdog.log`) are created one level up, still inside the tempdir, so the
  world is hermetic in any layout. Six fixture arms:
  1. `governance: fixture recorded lines are the pinned rows` — replacement guard:
     every embedded literal's sha256 equals its row digest AND the replayed row tuples
     equal `GOVERNANCE_ERRATA`/`GOVERNANCE_CORRECTIONS` exactly, so any re-pin or
     table extension (e.g. seat Kb82E04Governance's planned +3 corrections rows) trips
     this guard until the literal table is extended.
  2. `governance: fixture round-65 corrections land, errata-excused` — direct
     replacement of the deleted live arm: PASS with `2 recorded absence(s) excused`
     and `4 recorded correction(s) excused` (same needles, same semantics).
  3. missing correction → red (stale subjects named).
  4. restored stale target → red (`stale`, correction never launders a restored path).
  5. unrelated dead citation → red while both excusal counts stay intact — the exact
     live failure mode, now fixture-local.
  6. `governance: LOG.md:2678 erratum is load-bearing` — same name, same assertion,
     replayed hermetically against the real recorded 2678 row (drop-the-row and
     horizon-2677 sub-checks, boundary still a literal).

The public live gate (`governance.citation_resolves` via `main()`) is untouched and
still flags genuinely dead citations (evidence below). Assertion count: 1863 − 2
removed + 6 added = **1867 ≥ 1863**, no floor reduction.

## Evidence (all runs command-owned exit, sandbox clone unless noted)

- **Original red (live tree, committed before receipt)**
  `.ufo/waves/round-82/receipts/before-checklist-selftest.txt`:
  `1 failure(s) over 1863 assertions`, exit 1, failing arm =
  `governance: live round-65 corrections land, errata-excused` (live SCORECARD dead
  citations; excusal semantics intact at `2 recorded absence(s) / 4 recorded
  correction(s)`).
- **Original red (sandbox, unpatched verifier @ base)**
  `build/Kb82E03Checklist-selftest-base-red.txt`: `2 failure(s) over 1863 assertions`,
  exit 1 — both live arms red outside the fleet layout (extra `..`-hop dependence of
  the same arms; cured by the same patch).
- **Patched green** `build/Kb82E03Checklist-selftest-green.txt`:
  `0 failure(s) over 1867 assertions`, exit 0.
- **Hermeticity / live-governance invariance**
  `build/Kb82E03Checklist-selftest-mutated-identical.txt`: appended dead-citation
  drift lines to the clone's live `SCORECARD.md` (the exact live failure tokens),
  re-ran: result byte-identical, `0 failure(s) over 1867 assertions`, exit 0. The
  do-nothing control (base red above) misses the target; the fixture does not.
- **Guard disabled → corresponding fixture fails**
  `build/Kb82E03Checklist-guard-disabled-red.txt`: mutant with the replacement guard
  neutralized (`True`) and one embedded recorded line literal drifted
  (`lane root` → `LANE root`): `governance: fixture round-65 corrections land,
  errata-excused` FAILs with `line text drifted`, `2 failure(s) over 1867
  assertions`, exit 1. With the guard enabled the same drift trips the guard arm
  instead — the pin is load-bearing either way.
- **Live check not weakened**: on the drifted tree the public gate stays red —
  `FAIL governance.citation_resolves: evaluated 1369 … exit=1` (run in sandbox;
  additionally flags the fleet-layout `..` hops that resolve in the real fleet).
  The self-test no longer gates on live governance state; the live gate still does.
- Dry-check during authoring: fixture world PASS, `evaluated 2`, both resolving
  subjects green, before the patch was spliced.
- Patch integrity: `git apply --check --reverse` OK in the base clone; single file
  touched (`git status` clean otherwise).

## Blob ids / checksums (for L1 predata admission of the reviewed postimage)

- base blob `verifiers/verify_skill_checklist.py`: `6aab16849bd6d71ded8f3bcb3f95668f14f6a78f`
- postimage blob: `bc3674e4854e7c4b87435289884687dbde6745a3`
- patch sha256: `d2e684bb847ac4b1c55eb19c9fadce03789a90ac8f7ba828d7e4beeee3ee48f6`
- patched file sha256: `24fec2837ce5618ac0deeb62e0d8b1a3d7253f775aa50efda4038fdf166ffb56`
- also recorded in `build/Kb82E03Checklist-blob.txt`

## Coordination

- `Kb82E04Governance` (+3 `GOVERNANCE_CORRECTIONS` rows, horizon bump, 3 LOG notice
  lines) confirmed it will not touch the self-test. If both land in one revision, the
  fixture guard (arm 1) goes red until the (row, literal-line) table gains its 3
  entries; E04 ships the literal notice lines and a rebase script, so the update is
  mechanical. Sequencing preference: this fixture first at current constants.
- L1 asked for the postimage blob id + patch sha for predata admission into the
  historical `check_tip_battery` checklist tuple; supplied above.

## Risks / blockers

- The fixture embeds nine recorded line texts (~4 KB literals). If LOG.md history is
  ever rewritten (it is append-only by protocol), the guard catches the drift loudly.
- Sandbox reds differ from the live before receipt in count (2 vs 1) purely because
  the sandbox lacks the fleet-root `..`-hop targets; both reds are the same live arms
  and both are cured by the patch (green + mutated-identical receipts).
- No production files touched; scratch clone deleted after receipts copied.

VERDICT: C2 predicate met hermetically — patched `--self-test` prints
`0 failure(s) over 1867 assertions` (N ≥ 1863), exit 0, in sandbox; original red
reproduced (live before receipt 1/1863; sandbox base 2/1863); live governance gate
kept red on genuinely dead citations; LOG.md:2678 load-bearing arm preserved
meaningfully (real recorded rows, literal boundary) inside the fixture.

DELIVERABLES:
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/w1/Kb82E03Checklist.md
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E03Checklist.patch
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E03Checklist-selftest-base-red.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E03Checklist-selftest-green.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E03Checklist-selftest-mutated-identical.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E03Checklist-guard-disabled-red.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E03Checklist-blob.txt
