# Round 82 addendum 2 — host move: re-declared claims for the Windows attempt

Freezes this attempt's intent before any after-value. Base for this attempt:
`ff3b962561eaef436c6bf77c8ea9bfdc167f87a1` (master, identical to `origin/master`
at intake). Prior attempts on the Linux host: attempt 1 died before a report
(`lane-dead-no-report`); attempt 2 honest-stopped with evidence-only commit
`8cd28ba` (no claim landed, no after-value scored — both frozen predicates from
`plans/round-82.md` remain unlanded, and nothing in that plan's after-state was
measured, so this addendum replaces intent without touching any recorded value).
Addendum 1's ordering correction and battery-pin admission carry over unchanged.

## Host change (Q19 re-measure — every before re-taken)

The round moved hosts. Old host: Linux, lane at
`/home/vgpnk/Projects/shokunin/kotoba-shokunin`, fleet root the lane's parent.
New host: Windows, lane at
`…/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/fleet/kotoba-shokunin`, fleet root with
sibling lanes beside it, python invoked as `python` (3.13.15, no `python3`).
Re-measured at intake (receipts committed with this addendum):

- Checklist self-test: `3 failure(s) over 1863 assertions`, exit 1 on this host
  (`receipts/before-checklist-selftest-win.txt`) — the frozen plan's before was
  `1 failure(s)` on the old host. The two extra failures are environment-shaped:
  the second live governance arm (`LOG.md:2678 erratum is load-bearing`) now
  fails because the live corrections' `../.ufo/...` tokens resolve against the
  lane's parent, which is no longer the fleet root; and the delegated-absolute
  fixture arm fails on a Windows path-repr assertion (single-vs-doubled
  backslashes), not on gate behaviour.
- Tip battery, absolute `--repo` form: `2 of 6`, exit 1 (registry and sweep
  green; floors, checklist, integrity, independent red) —
  `receipts/before-tip-battery-win-abs.txt`. Same shape as the attempt-1 base
  battery, different host.
- Tip battery, `--repo .` relative form: `1 of 6` with four gates reporting
  `absent at <rev>` (`receipts/before-tip-battery-win-dot.txt`). Root cause
  (probe, `scratch` this host, not landed): `build_sandbox` passes the source
  path to `git clone --shared` as given, so a relative `.` produces a sandbox
  whose alternates do not resolve and most blobs never materialize. **Routed,
  not landed**: the fix (resolve the repo path to absolute inside
  `build_sandbox`) edits the frozen counter, and addendum 1 admits exactly one
  counter amendment this round (the checklist blob pin); anything else "requires
  a separate review or stays unlanded". Landed evidence: both receipts above,
  same rev, same host, forms diverge.
- Floors gate detail (this host): most instruments' self-tests degrade on
  Windows (`checklist 3, corpus_integrity 5, corpus_independent 7, pins 2,
  harness_independent 5, alwayson 55, spec_craft 74, sibling_reread 41 …;
  compare_harness_independent summary=missing`). Named debt; only the checklist
  instrument is repaired this round.
- `omp` is absent from PATH and `C:/Users/jpvei/AppData/Local/omp` does not
  exist (`receipts/before-host-skills-shas.txt` header): the frozen C1
  substrate re-pin cannot run on this host (its subject binary does not exist
  here). The lane's substrate pins (`verifiers/baseline.json`) still name
  old-host paths — PROVINCE/LOG record the correction per the absent-surfaces
  rule.

## Declared claims (this attempt)

### C1' — freshness (advisory, tied-lowest axis, score 8): host installed-skill surface census — capability acquisition

New instrument `verifiers/check_host_skill_surfaces.py` (read-only): enumerates
the host skills root's `*/SKILL.md` instruction surfaces, hashes each, matches
by directory name against the fleet root's `<name>/SKILL.md` lane repos, and
prints `host skill surfaces measured N: identical I, drifted D, lane-absent A`
plus one `DRIFT <name> installed=<sha12> lane=<sha12>` line per drifted surface
and one `LANE-ABSENT <name>` per installed copy with no fleet counterpart.
Exit 0 when every installed surface was measured and classified (drift is a
named finding, not an instrument failure — the instrument guards measurability,
not expected identity; expected identity is not pinned anywhere yet, and
pretending otherwise would fake a substrate-pin-guard semantics this surface
does not have); exit 1 when an installed SKILL.md is unreadable; exit 2 usage.
`--self-test` over tempdir fixtures covers identical, drifted, lane-absent,
unreadable, and skills-root-absent worlds and asserts the DRIFT line names both
sha12 prefixes. Sources row S265 (the installed surface, opened this round)
grounds the claim; the capability row enters `SCORECARD.md` § Capabilities this
round; freshness axis evidence cell updates, score held 8 (band move waits on
the non-author closure, per lane precedent).

Before (counting command, this host): the command does not exist —
`python -B verifiers/check_host_skill_surfaces.py --self-test` → cannot open
file; drift is unmeasured outside a manual sha table
(`receipts/before-host-skills-shas.txt`: 6 DIFF, 3 no-lane-repo).
After: self-test `0 failure(s) over N assertions` (N ≥ 12), exit 0; live census
`host skill surfaces measured 9: identical 0, drifted 6, lane-absent 3`, exit 0.
Do-nothing control: the committed before receipts (no instrument, drift
unknown). Sibling bound: audit and report only — the drifted copies belong to
their owning lanes and to the operator's install surface; nothing outside this
lane is edited.

### C2' — operability (advisory, score 8.5): hermetic checklist self-test on the current host

The frozen C2 intent, re-measured and re-shaped for this host. Predicate:
`python -B verifiers/verify_skill_checklist.py --self-test` prints
`0 failure(s) over N assertions` with N ≥ 1863, exit 0, on this host. Changes
landed: (a) the live-read governance arms (`governance: live round-65
corrections land, errata-excused` and `governance: LOG.md:2678 erratum is
load-bearing`) are replaced by isolated fixture arms carrying the same
expectations — a fixture world where two errata and four corrections land reads
PASS with both excused-counts; dropping the load-bearing erratum row or
lowering the horizon below its line turns that fixture world red naming the
row — plus a new isolation arm asserting that mutating the fixture world's
unrelated governance content does not change the guarded run's verdict (the
plan's "modifying unrelated live governance" discriminator, executable without
writing the live repo); (b) the delegated-absolute-target assertion compares
the `repr()` form the gate actually prints, so the arm tests the same rejection
on both path families; (c) `check_governance_citations` itself is untouched —
the public live gate keeps flagging genuinely dead citations (it is red on this
host for the `../`-layout reason; that red is named debt, not silently fixed).
Assertion floor 1863 unchanged (observed only grows); the floors registry is
not edited. Per addendum 1, the post-image blob sha of
`verifiers/verify_skill_checklist.py` is appended to `check_tip_battery.py`'s
`INSTRUMENT_PINS` tuple with an inline round-82 reason, existing pins kept.

Before: `3 failure(s) over 1863 assertions`, exit 1
(`receipts/before-checklist-selftest-win.txt`, this host). After: `0 failure(s)
over N assertions`, N ≥ 1863, exit 0. Do-nothing control: the committed before
receipt. No tip-battery total is claimed (the battery's other reds are debt).

## Ruled out (fresh-start bar), per candidate

- Frozen C1 substrate re-pin (omp 18.14.0 loader re-derivation): the subject
  binary is absent on this host — a do-nothing control reaches the same state;
  the claim is not declarable here. Recorded as host-conditional, not dropped.
- Tip battery 6-of-6 (r79/r80/r81 C1 lineage): killed twice by falsifying
  controls (r80 marker/masking/dead-hash worlds; r81 W-A/W-C 6-of-6 on the
  frozen counter); the residuals (exemption-manifest pin, `{7,39}` ellipsis
  bound, rev-prefix grammar, count-bound carry, SOFT_CROSS_CHECK tolerance,
  plan-trigger staleness) are individually retained open — repairing them on a
  new host without a dedicated falsify wave would re-enter the exact ground two
  closures rejected, and the addendum-1 admission forbids a second counter
  amendment this round. Not declared.
- Old-host attempt-2 wave integration (candidate patches
  `Kb82E01…Kb82E04`): authored against Linux host paths (`omp.real`,
  `/home/vgpnk`); their predicates are unmeasurable here. Not declared; left as
  committed wave evidence.
- The `--repo .` sandbox fix (above): routed, not landed — one amendment per
  round, already spent by the addendum-1 pin admission.

## Routed duties carried this round

S248 opened this round before any status change (routed from r81), the
`queued → mined` flip is an append-only cell change logged in LOG.md; an
appended LOG notice records that `b3449ee25cd097e39d1af4370791fd0add463321`
(r81 D1) is an orphaned detached-HEAD premeasure rev, not a landed revision;
`corpus/lessons/round-82.md` mines the freeze-ordering mistake (attempt 2, not
yet in any lesson) plus this attempt's host-bound before-values mistake.

## Dispatch shape

The old host's wave dispatcher (`w1.ready` files, 64-seat v2 waves) does not
exist here. Mission floor (≥ 8 L2 subagents, one batched call) is attempted
through this host's batched subagent surface for read-only reconnaissance;
if the surface cannot dispatch from a headless round, the attempt and its
refusal are reported, never padded.
