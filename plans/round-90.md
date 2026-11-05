# Round 90 — plan (frozen before any candidate score)

Author: KotobaR90 (L1). Base: `0c20d8ab65587aee0e97b7d14c801ae6dc44c2e5` (lane tip = pushed `master`
tip at round start, `jj-lane.sh state`: ahead 0 / behind 0). Linux host, omp 18.15.0.
Round-start census: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
/home/vgpnk/Projects/shokunin kotoba` → exit 0, `kotoba  ok`, 33 pre-existing W04 duplicate-URL
warnings (unchanged class), 185 rows (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
corpus/SOURCES.md` → 185). Receipt: `.ufo/waves/round-90/receipts/census-before.txt`.

Q19 re-measure of the carried before-values used below: the r89 spot-check routed notes (note 1
S258 digest class, note 2 carried battery/duplicate-name/symlink items, note 3 scribe seat deaths)
were re-read from `corpus/lessons/round-89-verifier-spotcheck.md` at the base; the base no-harm
battery was re-run fresh at the base (receipts below), not copied from r89.

## Claims (frozen)

### C1 — depth (owned lowest, score 9 held; claim type: capability acquisition)

Surface: the lane's two round-89 gate instruments (`verifiers/check_freeze_gate.py`,
`verifiers/check_r86_routed_repairs_v3.py`) at their final committed (post-A2) bytes; closes the
r89 routed item "mutation battery re-run on final (post-A2) bytes"
(`corpus/lessons/round-89-verifier-spotcheck.md` § routed notes, item 2).

**Frozen predicate (one sentence, identical in counter docstring and receipts):**
`python3 -B verifiers/check_mutation_battery.py --rev <rev> --work <scratch-dir>` prints
`mutation battery killed K of M kill-set; equivalents survived E of E; disclosed survivors S of S`
and exits 0 iff K == M and E == E and S == S_declared and guards G1–G3 PASS, where M, E and
S_declared are the class counts of the committed manifest
`verifiers/fixtures/mutation-battery/manifest.tsv` (classes `kill`, `equivalent`, `survivor`).

- Counting command before: `git grep -n 'mutation_battery' 0c20d8ab65587aee0e97b7d14c801ae6dc44c2e5 -- verifiers plans`
  → no matches, exit 1 (receipt `.ufo/waves/round-90/receipts/before-c1-absence.txt`).
- Counting command after: the predicate run at the landing revision, plus
  `python3 -B verifiers/check_mutation_battery.py --self-test` → `0 failure(s) over N assertions`,
  exit 0 (Q48 arm: the self-test drives `main()` on a satisfying fixture asserting exit 0 and the
  exact printed line, beside one broken-conjunct world asserting exit 1).
- Target: at the landing revision K == M, E == E, S == S_declared, exit 0, self-test green, and
  `verifiers/check_gate_registry.py --rev <rev>` names the new `check_mutation_battery.py` row
  conformant (guard G3).
- Two-sided (Q47): every `kill`-class mutant is killed (its probe exit flips away from the frozen
  baseline) AND every `equivalent`-class mutant survives; the equivalent class is generated at
  measurement time (docstring/whitespace/comment rewrites applied by the battery at run time), not
  a fixed published list. `survivor`-class mutants are recorded with a committed disposition reason
  each (the r89 recorded survivor `d5-m1a-d5iii-leg-only` enters this class with its reason).
- Guards: G1 revision identity — every probe reads the target through `git show <rev>:<path>`
  bytes copied to scratch, never the working tree; G2 manifest integrity — the battery verifies
  the sha256 it recorded for each mutated file against the revision bytes and refuses a mismatch
  (`could-not-evaluate`); G3 registry presence — the gate registry row must name the battery.
- Controls (pre-data, executed through the r89 freeze gate before any candidate score): see
  `plans/round-90-controls.md` — ctl-c1-absence, ctl-c1-r89harness, ctl-c1-stub.
- Kill rule: no counter or manifest amendment after any scored reading; a defect found post-score
  is a finding, routed, never repaired into the frozen bytes.
- Sourced: the knowledge entry `corpus/knowledge/mutation-battery-round90.md` cites S260 (external,
  opened this round) and S261 (own-work, the r89 MutTesterGates committed bytes).

### C2 — freshness (advisory; tied-lowest 8 under the all-axes reading; type: measured axis-move)

Surface: the round-82/84 installed-skill census claims, stored against Windows host roots
(`C:/Users/jpvei/.agents/skills`), re-verified against this host's live skills root
`/home/vgpnk/.agents/skills` (83 installed `*/SKILL.md` directories measured at plan time —
`ls /home/vgpnk/.agents/skills | wc -l` → 83), plus the round-72 A1 name-uniqueness rule the
round-84 C2 claim re-verified on the other host.

**Frozen predicate (one sentence, identical in receipts):**
`python3 -B verifiers/check_host_skill_surfaces.py --skills-root /home/vgpnk/.agents/skills
--fleet-root /home/vgpnk/Projects/shokunin` exits 0 printing
`host skill surfaces measured N: identical I, drifted D, lane-absent A` with I + D + A == N == 83
at the measured run, and the committed receipts `.ufo/waves/round-90/receipts/c2-host-census.txt`
(the run transcript naming the measured revision and the root) and `c2-name-collisions.txt` (the
A1 name-extraction ledger; its `NAME-COLLISION` count stated with the `grep -c` command) exist at
the landing revision.

- Counting command before: the absence sweep
  `git grep -l 'home/vgpnk/\.agents/skills' 0c20d8ab65587aee0e97b7d14c801ae6dc44c2e5 -- .ufo/waves corpus verifiers receipts`
  → historical scout notes only, no census receipt (receipt `.ufo/waves/round-90/receipts/before-c2-sweep.txt`),
  and the stored r84 receipts name the Windows roots (`git grep -c 'jpvei'` over
  `.ufo/waves/round-84/receipts/` ≥ 1), which resolve on no path on this host.
- Counting command after: the census run (transcript receipt) + `grep -c 'NAME-COLLISION'
  .ufo/waves/round-90/receipts/c2-name-collisions.txt` (the count stated beside it).
- Findings duty: every `drifted` or `identical` finding and every NAME-COLLISION is named in the
  report as a read-only finding routed to the owning lane; this lane fixes nothing outside its
  repo. The census guards measurability, not expected identity (no pin exists for installed
  copies) — an honest all-clear is a valid outcome.
- Controls (pre-data): see `plans/round-90-controls.md` — ctl-c2-windows, ctl-c2-empty, ctl-c2-fake.
- Kill rule: as C1.
- Q66 bound: the census gate derives no path from a relative argument in this predicate (both
  paths are absolute); a relative-form probe is a finding, not the predicate.

### Lowest-axis obligation

Owned reading: depth 9 < consistency 10 → C1 works the lowest owned axis. All-axes reading:
freshness 8.0 and adjacency 8.0 tied lowest → C2 works freshness. The readings L0 stays open
(fleet `.ufo/l0-questions.md`, kotoba round-50 line); both readings are stated and both are
worked, so the round satisfies the duty under either reading.

## Controls, executed before data (plans/round-90-controls.md)

Run through the r89 capability (`python3 -B verifiers/check_freeze_gate.py --plan
plans/round-90-controls.md`) — expected `freeze gate: 6 control(s) held`, exit 0, receipt
`.ufo/waves/round-90/receipts/freeze-gate-r90.txt`. Each control script exits 0 iff its world
MEETS the claim predicate; the frozen declaration expects exit 1 (no shortcut reaches the target):
ctl-c1-absence (no instrument at base), ctl-c1-r89harness (the r89 wave harness is not a
registered lane verifier; predicate unmet), ctl-c1-stub (a scratch stub printing the success line
without a manifest fails the manifest-count guard), ctl-c2-windows (the r84 Windows-root form
exits 2 here), ctl-c2-empty (empty root → measured 0 ≠ 83), ctl-c2-fake (one-file root → 1 ≠ 83).

## No-harm battery (Q65 at base, Q72 on the post-state)

Base receipts land in `.ufo/waves/round-90/receipts/base-*.txt`; the same commands re-run at the
landing as `landing-*.txt`. Reds at base are named red, never summarized away:

| command | base reading |
|---|---|
| `python3 -B verifiers/check_assertion_floors.py` | FAIL — `registry size drift: instrument_total=18 but 19 entries`; `registry row vanish: freeze_gate` (the r89 half-bump, carried red; this round completes the bump) |
| `python3 -B verifiers/verify_corpus_integrity.py --json` | `unindexed 1` — `corpus/lessons/round-89-verifier-spotcheck.md` (this round adds the index row) |
| `python3 -B verifiers/check_r86_routed_repairs_v3.py --base-receipt .ufo/waves/round-89/receipts/d5v3-base-receipt.json` | `closed 4 of 5, instance drift 4` (Q79 path dependence; the r90 freeze writes its own receipt) |
| `python3 -B verifiers/check_gate_registry.py --rev <base>` | `73 of 73 lane verifiers; phantom 0`, exit 0 |
| `python3 -B verifiers/check_tip_battery.py --rev <base>` | `guards 4 of 5; tip battery exit 0: 2 of 6` |
| `python3 -B verifiers/verify_skill_checklist.py --json` | `governance.citation_resolves` red (dead historical LOG citations), carried |
| `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md` | `province rows 20 matched 4` (tameshi commit, tsukuroi classification), carried red, disclosed |
| sources census | exit 0 |

## Touch list (Q73 sweep) and budget (Q78)

- `verifiers/floors-registry.json` `instrument_total` 18 → 19 and the `freeze_gate` row enter the
  guard tables in ONE change: the floors guard self-test pins the literal
  `"instrument_total": 18` in its F6 size-drift arm, so the same change updates that literal;
  sweep at freeze: `grep -n 'instrument_total' verifiers/check_assertion_floors.py`.
- `SKILL.md` is 600/600 lines (Q78): one new registry row (`check_mutation_battery.py`) enters
  only with ≥1 line saved by joining wrapped lines in the registry intro (r89 precedent). The
  freeze states bytes, lines, lines > 120 chars, longest line; the landing re-states them.
- `corpus/README.md`: one index row for `corpus/lessons/round-89-verifier-spotcheck.md` (an index
  row is a claim: the file exists), plus append-only Frontier/notes rows; no section a historical
  counter pins byte-identical is touched.
- New files: `verifiers/check_mutation_battery.py`, `verifiers/fixtures/mutation-battery/*`,
  `verifiers/fixtures/round-90/*` (control sims), wave evidence under `.ufo/waves/round-90/`.
- `plans/round-90.md`, `plans/round-90-controls.md`: this plan and the controls; the plan is
  frozen at the pre-data commit — seat findings amend nothing here; amendments land as
  `plans/round-90-addendum-*.md` before any scored reading.

## Frontier step (§2b)

- SOURCES: S260 (external — the mutation-testing practice source opened this round by the scout
  seat; tier per contract) and S261 (own-work — the r89 MutTesterGates committed bytes). ≥1
  rejection is recorded in the lesson `## Gate` (route or mirror rejected with reason + flip).
- Census before → after pasted with commands and exit codes (185 → expected 187).
- One mistake mined into `corpus/lessons/round-90.md` `## Mistakes`: the r89 floors half-bump
  (class `number-drift`/`landing`: a floors-registry row landed without the guard tables and the
  `instrument_total` bump; captured-by: the registry's own bump-in-step rule and the guard anchor,
  which caught it — the anchor outside the edited file did its job); fix shown able to fail: the
  half-bump world re-built in scratch reads the same two FAIL lines (regression arm receipt).
- Sourced claim: C1 cites S260 (opened this round).
- Assimilation: none — L0 `kotoba | round-88` (renumber-or-retire) stays open; the package stays
  unadopted (55 collisions stand as measured in r89).
- Considerthese (`considerthese/2026-10-26.md`): proposal 5 (per-round evidence budget) is mined
  this round as QUALITY criterion Q82 (extends Q11/M15 with a per-round wave-evidence byte budget
  measured at landing); proposals 3 and 4 stay carried (3 needs the description self-audit round
  shape; 4 is answered structurally by this round's Q47 two-sided battery and stays a shape rule).
- The kotoba slice of the absent-defect register (13 rows) is NOT adopted and NOT verdict-landed
  this round: adoption is L0-blocked; the slice re-derivation is carried, not silently dropped.

## Wave shape

ONE v1 wave `r90-w1` of 13 seats under policy v1 (band 8–16): attack seats ReviewerRepairs,
ReviewerBattery, CriticClaims, MutTesterBattery, SentinelScope = 5/13 ≈ 38 % (≥ 25 %); connector
1 (≤ 2); L2 floor roles met (3+ executor, scribe, scout, reviewer, critic, connector; the L1
holds the planner seat — the validator excludes `planner`, disclosed per the standing note).
Residual calls: none planned; any residual is one ordinary task call ≤ 8 seats, counted in the
round total.
