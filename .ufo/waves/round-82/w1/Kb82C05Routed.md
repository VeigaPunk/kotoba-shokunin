# Kb82C05Routed — W-A/W-C reproduction and maintenance-closure audit

Seat: Kb82C05Routed (critic, leaf). Base: `47dbe8781657de563ff867caca6244d28e3db504`.
Question assigned: reproduce W-A/W-C from the r81 committed attack receipts and test
whether maintenance incorrectly calls them closed. No 6/6 claim is made this round.

## Answer

**Both classes remain open on the round-82 base bytes, and no maintenance text —
committed or in-flight — calls them closed.** The reproduction is not just honest
retention: the acceptance arms in both corpus gates still green the exact r81
counterexamples (re-run here at r82 base, receipts below). The r81 kill therefore
still stands on live bytes, and the retained-open dispositions in the maintenance
record are accurate, not stale.

## Reproduction setup

- One scratch clone at base `47dbe87`, placed in a fleet-shaped sandbox
  (`sandbox/kotoba-shokunin` with every fleet-root entry — dot entries included —
  symlinked beside it), `TMPDIR` under the seat scratch root. Counter bytes at base:
  `verifiers/check_tip_battery.py` sha256 `1753b11c11c6f907be838cb28842e28d01e7935e19d5afb3a6b46afdac51d660`
  — byte-identical to the r81 freeze post-image; the two corpus-gate blob pins
  (`bbee51f2…`, `59602942…`) hold, and the counter's `instrument-pin` guard passed
  in both battery runs. Fixture-only commits in the asserted sandbox with scratch
  identity.
- W-A fixture mirrors r81 exactly: the forged hash `8b1cc1b00a9322cd8e231d87e015e1d75d20adc1`
  re-verified absent from the production lane (`cat-file -e …^{commit}` rc 128) and the
  fleet (rc 128); a manifest row in `verifiers/external-commits.json` binding it to
  `wrong-owner/wrong-repo`; a test-authored receipt
  `.ufo/waves/round-82/build/Kb82C05Routed-wa-fixture.fetch.json`
  (sha256 `5cc6c69b…`, byte-identical to the r81 fixture receipt). The base tree already
  cites this hash at `corpus/lessons/round-81.md:8` (the r81 lesson records it as the
  W-A world hash), so no new citation was needed — commit_total stays 50.
- W-C fixture mirrors r81 exactly: the 816-byte padded marker at
  `.ufo/reports/round-77/kotoba.md` **recovered byte-exact**
  (sha256 `1fa0e2c81fe5028576bdf80bbeb2b95b5ef64bb0e54ef5cd4bbce8296b27bfdd`,
  matching the r81 measured blob) plus the pointer line
  ``Padded marker object control: `HEAD:.ufo/reports/round-77/kotoba.md`.`` in
  `corpus/lessons/round-80-verifier-spotcheck.md`.

## W-A — forged repository binding: STILL OPEN

| Stage | Rev | Integrity | Independent |
|---|---|---|---|
| attack-only | `f5f875e9…` | exit 1; `commit_unresolvable 1→0`, forged hash in `commit_external_detail` (`corpus/lessons/round-81.md:8`) | exit 1; `commit_external 3` incl. the forged hash, `commit_unresolvable 0` |
| world-end (index hygiene + baseline refresh, no carry) | `580a8324…` | **exit 0** | **exit 0** |

Counter battery at `580a8324…`: `guards 5 of 5; tip battery exit 0: 4 of 6`, counter
exit 1 — `build/Kb82C05Routed-wa-end-tipbattery.txt`. Reds: `check_assertion_floors`
(`FAIL checklist observed=1863 floor=1863 self_test_failures=2`) and
`verify_skill_checklist` — both the C2 before-value debt, unrelated to W-A. Greens:
registry, **corpus integrity, corpus independent**, correction sweep. A tree whose
external provenance is fabricated now passes both corpus gates at r82 base.

## W-C — padded non-report: STILL OPEN

| Stage | Rev | Integrity | Independent |
|---|---|---|---|
| attack-only | `945d98b0…` | exit 1; `report_dead 0`, `report_total 117→118` (impostor accepted) | exit 1; `report_dead 0`, `report_total 118` |
| world-end (+ baseline refresh, `--carry corpus.pointers.commit_unresolvable`) | `71b750be…` | exit 1 with the **single** NONPASS `corpus.pointers.commit_unresolvable` DRIFT (observed 1, expected 0 — carried) | exit 1; `report_dead 0`, `report_total 118`, `commit_unresolvable 1` (same carried class) |

Counter battery at `71b750be…`: `guards 5 of 5; tip battery exit 0: 2 of 6`, counter
exit 1 — `build/Kb82C05Routed-wc-end-tipbattery.txt`. Reds: floors and checklist (C2
debt), corpus integrity and independent red **only** on the carried pre-existing
unresolvable citation (`corpus/lessons/round-81.md:8` cites the W-A hash, which no
landed manifest binds). The W-C attack surface — report identity — is fully green in
both gates: a padded 816-byte blob with `## SHONEN` and no report content counts as a
live report.

## Why the battery cannot print 6/6 at r82 base (and why that does not weaken the kill)

At r82 base the committed before battery reads `2 of 6`
(`.ufo/waves/round-82/receipts/before-tip-battery.txt`): the checklist self-test fails
(`1 failure(s) over 1863 assertions`, the C2 declared before-value; in a scratch clone
the same arms read 2 failures because the live `../.ufo/…` governance tokens do not
resolve outside the fleet-shaped layout — environment-sensitive live reading, exactly
the defect C2's fixture repair targets), and the floors guard reds on that same
failure (`FAIL checklist … self_test_failures`). Additionally the r81 closing records
left routed drift debt (`corpus.index.unindexed 1` for the spotcheck lesson;
`commit_unresolvable 1` from the lesson's citation of the W-A hash). So the r81 6/6
kill-line is not re-printable at r82 base even with the corpus gates accepting the
forgeries: two debt gates are red before any world is built. This narrows nothing:
the r81 kill receipts remain committed, this round declares no 6/6 claim, and the
class-level acceptance shown above is the operative fact for maintenance — a repair
must close these arms, and none has.

## Maintenance-closure audit (the assigned test)

Audited every maintenance surface that could call W-A/W-C closed:

| Surface | Disposition | Correct? |
|---|---|---|
| `corpus/lessons/round-81-verifier-spotcheck.md` (r81 closure, routed defect 6) | "W-A/W-C classes remain open by design … The kill stands until a round repairs and re-measures." | yes — matches this reproduction |
| `plans/round-82.md` (frozen at `006a834`) | "individually investigated and either repaired with red/green evidence or explicitly retained open; no 6/6 tip-battery claim" | yes |
| `w1/Kb82R06Routed.md` rows 6a/6b | "Unclaimed maintenance; retained open unless independently demonstrated repaired." | yes — this seat is the independent demonstration: still open |
| `w1/Kb82S01Lesson.md`, `w1/Kb82S04Scorecard.md`, `w1/Kb82S09Report-draft.md`, `w1/Kb82S12Receipts.md`, `build/Kb82K02Mistakes-evidence.json` ("open_residue") | all carry W-A/W-C as open residuals/candidates | yes |
| r82 build patches (`ls build/`) | no patch touches `verify_corpus_integrity.py`, `verify_corpus_independent.py`, or `external-commits.json`; the W-A/W-C siblings present (`Kb82V04Governance-wa-forge/wc-pad-*.json`) are probes, not repairs | yes |
| r82 freeze commit `006a834` diff | receipts + plan only; no verifier or manifest change | yes |

No surface — committed, frozen, or in-flight at audit time — calls W-A/W-C closed,
repaired, or superseded. Retained-open is honest; the false-green remains documented
by the r81 kill receipts and is now re-documented on r82 base bytes by this seat.

## Additional findings

1. **r81 artifact discrepancy**: the committed r81 fixture patch
   `Kb81C01C1-world-c-padded-marker.patch` carries 6 padding rows (945 bytes), but the
   r81 world receipt measured an 816-byte blob (sha256 `1fa0e2c8…`). The 816-byte form
   was recovered byte-exact here; the r81 patch file has one row more than the blob it
   documents. Class conclusion unaffected (both forms satisfy marker+≥400 B).
2. **Self-referential debt**: the r81 lesson's own citation of the W-A forged hash now
   keeps `commit_unresolvable 1` at r82 base — the kill's evidence hash is itself an
   unresolvable citation until a maintenance round either binds it with real evidence
   (impossible for a fabricated hash) or classifies the self-reference arm. The W-C
   world carried it via the refresh script's sanctioned `--carry`.
3. **Fleet-shape pitfall for reproducers**: run outside a fleet-shaped parent, both
   corpus gates read `report_dead 1` for `../../.ufo/reports/round-76/kotoba.md`
   (an artifact, not a finding); a sibling probe in `build/Kb82V04Governance-*` shows
   exactly this. All receipts reported here are from the fleet-shaped sandbox.

## Boundaries

Read-only on the production lane and fleet (cat-file/ls only); all writes in the
asserted scratch sandbox and the seat's unique build/report paths. No installs, no
pacman, no subagents, no production gate runs as scoring evidence (the base numbers
are the committed before receipts; every world run is a control world). Bounded heavy
gates, elapsed: floors in base clone 143 s; counter batteries 157 s (W-A) and 208 s
(W-C); load recorded by the harness. Scratch sandbox deleted after receipts copied.

VERDICT: W-A and W-C both reproduce at round-82 base — both corpus gates still accept the r81 forged-repository binding (exit 0 world-end) and the padded non-report (report_dead 0 in both gates) — so the classes are genuinely retained-open; the maintenance record (r81 spotcheck routed defect 6, r82 frozen plan, and every in-flight r82 seat text audited) correctly retains them open and no maintenance incorrectly calls them closed; the r81 6/6 kill-line is not re-printable at r82 base only because of independent C2 checklist/floors debt plus routed drift debt, and no 6/6 claim is made.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/w1/Kb82C05Routed.md; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C05Routed-identity-evidence.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C05Routed-world-matrix.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C05Routed-wa-attack-integrity.json; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C05Routed-wa-attack-independent.json; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C05Routed-wa-end-integrity.json; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C05Routed-wa-end-independent.json; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C05Routed-wa-end-tipbattery.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C05Routed-wc-attack-integrity.json; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C05Routed-wc-attack-independent.json; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C05Routed-wc-end-integrity.json; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C05Routed-wc-end-independent.json; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C05Routed-wc-end-tipbattery.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C05Routed-SHA256MANIFEST.txt
