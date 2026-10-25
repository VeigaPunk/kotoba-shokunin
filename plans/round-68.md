# Round 68 — plan (hyaku campaign, lane kotoba, attempt 1)

Frozen before any wave seat scored either claim, and before any seat wrote round-68 content.
Base lane tip (branch `master`): `e94ae32a5cd8dc3ee8e2d247816784bec2750cc0` (read with
`jj-lane.sh state`; git HEAD is detached after the helper commits — the branch tip is the
pinned base).

Round shape: **two v1 waves** (policy `scripts/hyaku/ufo-wave-policy.json`, band 32–64):
wave 1 build, 32 seats, dispatched first; wave 2 falsify, 32 seats, dispatched only if wave 1
yields ≥32 distinct attack items. Both waves are validated before dispatch and dispatched as ONE
batched call each. The L1 holds the canonical §3 planner seat (the validator rejects a `planner`
seat); the planning data-walk rides the wave-1 scout/connector items.

**Inherited state.** The lane working tree carries exactly one untracked path from round 67 —
`.ufo/waves/round-67/w1/controls/junk-world/` (254 MB, the C2 junk-world control mirror). It is
routed defect R67-3; it is disclosed and removed in this round (see C2). Nothing else is
inherited. Round 67's wave-2 seat reports that landed after its report are inherited state; they
are read, never edited.

**Weekly-quota L0 (already filed; not duplicated).** The `kimi` provider's weekly (7-day) usage
limit killed 14 of round 67's 32 wave-1 seats. This round dispatches the band anyway and records
every dead seat with its error text; a smaller wave is honest only if the route refuses it, and
no settlement is fabricated.

## Claim declarations (1–3 claims; this round declares 2)

### C1 — depth (the lane's lowest owned axis) — client trust gates

**Axis:** `depth` (owned). **Surface:** the instruction/trust boundary a skill body crosses —
what a client documents about an **untrusted** skill body (this is the half the r67 authority
ladder does not cover: r67 holds *who outranks whom*, not *what happens to a body the client
does not trust*).

**Why this is the lowest-axis obligation.** The lane's owned axes are `depth` (9) and
`consistency` (10); depth is the lowest. The all-axes reading (freshness/adjacency 8.0, advisory)
remains the lane's open L0 question and is not settled here; this round works the owned reading
and states both, as rounds 47–67 did.

**Frozen predicate (one sentence, same in this plan, in the counter's code and in the receipt):**

```
python3 -B verifiers/check_client_trust_gates.py --rev <rev>  ->  prints "client trust gates backed N of 5", exit 0 when N == 5
```

with two further conjuncts that make the counter non-vacuous:

```
python3 -B verifiers/check_client_trust_gates.py --rev <base> ->  prints "client trust gates backed 0 of 5", exit 1
python3 -B verifiers/check_client_trust_gates.py --fetch       ->  finds each of the 5 located quotes on its live page
```

**Before (measured at the base `e94ae32a`):** the instrument does not exist and the lane holds no
trust-gate ground: `corpus/knowledge/` has no trust-gate entry, `corpus/README.md`'s coverage map
has no trust row, and `corpus/SOURCES.md` holds none of the five client URLs
(`vtcode`/`parallelworks`/`kilo.ai`/`agent-framework`/`mistral-vibe`: 0 hits each). The
do-nothing control — the base tree read by the frozen counter — cannot reach `5 of 5`; it reaches
`0 of 5` and exits 1.

**Landed shape.** One knowledge entry `corpus/knowledge/client-trust-gates-round68.md` carrying a
per-client table (client · what the client documents about an untrusted skill body · the located
quote · the source id), the five `corpus/SOURCES.md` rows it cites (appended, never edited),
one `SKILL.md` pointer line, and the new counter `verifiers/check_client_trust_gates.py` with a
`--self-test` that breaks each conjunct.

**Counter semantics (the r67 lesson, applied from the start).** The r67 counter classified a
missing entry as an *environment* error (exit 2) instead of a *not-grounded* verdict (exit 1);
that is routed defect R67-1. The r68 counter is built with the corrected classification from the
start: a **missing entry** is `0 of 5`, exit 1 (a content verdict); a genuinely unreadable
**environment** (unknown revision, unreadable repo) stays exit 2. The r67 counter is NOT modified
— its frozen claim stands a miss, corrected by an appended erratum (see C2).

**Bound (named before data).** Documentary evidence, not observed runtime behaviour; the counter
reads the measured revision's own bytes (QUALITY Q33), so the verdict also rests on the base
control, the junk-entry control, the mutation battery and the `--fetch` measurement. No band move
is claimed; the score stays at `depth | 9` pending the non-author closure.

### C2 — consistency (this lane's calibration sub-axis) — the routed r67 repairs

**Axis:** `consistency` (owned). **Routed cause:** the r67 closure's spot-check
(`corpus/lessons/round-67-verifier-spotcheck.md`, written by the hyaku closure, never edited by
the lane) routes four defects to round 68.

**Frozen predicate (three conjuncts, one command each):**

```
python3 -B verifiers/verify_corpus_integrity.py        ->  prints "9/9 checks pass", exit 0
python3 -B verifiers/verify_corpus_independent.py --json ->  exit 0
python3 -B verifiers/check_r67_routed_repairs.py --rev <rev> ->  prints "r67 routed defects closed 4 of 4", exit 0
```

**Before (measured at the base `e94ae32a`, receipt `controls/C2-base-integrity.txt`):**
primary `6/9 checks pass`, exit 1 —
`DRIFT corpus.index.tracked_files: observed=122 expected=121`,
`DRIFT corpus.index.unindexed: observed=1 expected=0 / empty`
(`unindexed: corpus/lessons/round-67-verifier-spotcheck.md`),
`DRIFT corpus.pointers.report_total: observed=85 expected=82`;
the independent gate exits 1; `check_r67_routed_repairs.py` does not exist (0 of 4).

**The four routed defects and their repairs.**

- **R67-1 (dishonest before-line).** The r67 report, `LOG.md` and `SCORECARD.md` state that the
  r67 C2 base prints `authority ladder grounded 0 of 1`. The committed receipt
  (`.ufo/waves/round-67/receipts/C2-authority-measure.txt`) and a re-run at the base show exit 2
  and `environment error: cannot read corpus/knowledge/instruction-authority-ladder-round67.md at
  2a8eba56…`. **Repair:** an appended erratum (never a rewrite) in `LOG.md`, `SCORECARD.md`,
  `corpus/lessons/round-68.md` and the round-68 report, naming the observed line and stating that
  the r67 claim stands a **miss as declared**. The r67 report itself is not edited.
- **R67-2 (wrong receipt path).** The r67 report cites
  `.ufo/waves/round-67/w1/controls/census-validate-append.txt`; the bytes are at
  `.ufo/waves/round-67/controls/census-validate-append.txt`. **Repair:** the erratum names the
  real path; the r67 report is not edited.
- **R67-3 (undisclosed 254 MB).** `.ufo/waves/round-67/w1/controls/junk-world/` is an untracked
  control mirror left in the lane working tree. **Repair:** disclosed in the round-68 report and
  lesson, and **removed** from the working tree (it is control scratch, not round evidence).
- **R67-4 (unindexed closure file).** **Repair:** one coverage-map index row for
  `corpus/lessons/round-67-verifier-spotcheck.md` in `corpus/README.md` **plus** a re-record of
  `verifiers/corpus-baseline.json` to the values re-derived by the gate's own measurement
  (the lane's established mechanism: rounds 11, 12, 23, 46, 66, 67). The repair moves the CAUSE
  (the unindexed file) and not only the symptom (the stale expectation).

**Do-nothing controls (K2/K3, the r67 shape re-used):** the index row alone and the baseline
re-record alone each leave the primary gate red — the counter reaches neither `9/9` nor `4 of 4`.

## Frontier step (§2b) — rides inside the two claims, adds no claim slot

1. **Curate `corpus/SOURCES.md`.** Rows are written only after the source is opened **this
   round**; the lesson's `## Gate` records the URL, the access date and a ≤25-word located quote
   for every new row. Rejections stay as rows with reason and flip.
2. **Census before → after.** `scripts/sources-census.sh validate --root
   /home/vgpnk/Projects/shokunin kotoba` at round start and round end; exit 0 required at round
   end.
3. **Mine one mistake** into `corpus/lessons/round-68.md` `## Mistakes`: class · evidence ·
   captured-by · fix, with the fix shown able to fail.
4. **At least one sourced claim** — C1 rests on rows opened this round.

## Item 10 — assimilation (operator directive of 2026-10-24; rides inside §2b)

- **Source repo read-only.** `/home/vgpnk/Projects/shokuknow` is read, never written; no campaign
  tool is run there.
- **One theme:** *client trust gates* — what a client documents about an untrusted skill body.
  At most 1–3 knowledge entries from `merge/kotoba/` are adopted; every cited source is re-opened
  in-round (my access date, my located quote).
- **Id collision check in scratch** before any append, with the census parser's 0–3-leading-space
  pattern; the guard is proved non-vacuous on a scratch fixture first. A nonempty collision file is
  fixed in scratch only, and every adopted citation is re-pointed **by document**, never by
  arithmetic.
- **Scratch transformation and validation before any append:** the append block is built in
  scratch from the rows the admitted entries cite, normalized to the lane's 11-column schema
  (`recheck` a valid ISO date / `NNd` / symbolic cadence, no literal or escaped `|` in any cell,
  `used-by` exactly the admitted entries citing the row, `status mined`), mirrored over a copy of
  the lane's `corpus/` and gated by `sources-census.sh validate --file …` (exit 0) **before** the
  first registry append.
- **Quarantine:** the lane's slice of the campaign's absent-defect register is derived in scratch
  (13 rows: 7 `payload-absent`, 6 `unreachable`); every row is hand-checked this round — fetch the
  cited source and locate the quote; absent → refuse the row (fabrication class) with reason and
  flip; present → adopt with the anchor located; `unreachable` is unverifiable, never fabrication.
- **considerthese:** at most ONE still-unimplemented proposal from the latest file is mined
  (never edited), grounded through the lane's own bar — the reflection is a pointer, not evidence.

## Round mechanics

- Lane commits and pushes only through `scripts/hyaku/jj-lane.sh`; the report lands last through
  `scripts/hyaku/fleet-commit.sh --as kotoba`. Only the helper's final `landed <hash>` is
  citable.
- Seats never mutate the fleet repo, a sibling lane, the lane's jj state or the lane's Git index;
  every seat writes under `/home/vgpnk/Projects/shokunin/kotoba-shokunin/`.
- Tool installs: permitted only under `/home/vgpnk/.omp/agent/RULES.md`; **all pacman
  transactions are paused host-wide** — install via `uv tool` / `npx` / an official binary in
  `~/.local/bin`, or file an L0 question.
