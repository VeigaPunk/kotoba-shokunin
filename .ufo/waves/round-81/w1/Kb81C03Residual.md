# Kb81C03Residual — falsify the residual stack (what C1 does NOT repair)

Seat: critic, leaf. Lane base `b284223105f4d106f7e8f56ed4fd296c643cda0e`. All gates were run
first-hand; scratch `…/Kb81C03Residual/{clone,clean}` (probe worlds committed locally). The r81
instrument patches measured are `build/Kb81E01Integrity.patch` (post-image `bbee51f2`),
`build/Kb81E02Independent.patch` (post-image `59602942`), `Kb81E03ExtManifest.json`,
`Kb81E04Baseline.patch`, `Kb81E05Erratum.patch` (LINE_CAP 40→900 per the plan's revised E6 —
my task text still says 140; the plan line is authoritative and says 900 with tight tuples).
Raw numbers: `build/Kb81C03Residual-receipts.txt`.

## (a) Other `report_dead`-class tokens the gate misses — R03's inventory minus the fixed one

Sweep (`git grep -E '[^\s`"()\[\],;:]*\.ufo/' corpus/*.md`, plus rev-prefixed forms): **exactly
one** `<rev>:<path>` token exists inside the `.ufo/reports/` grammar — the fixed
`HEAD:.ufo/reports/round-77/kotoba.md`. All other `<rev>:<path>` tokens (`git show
b1be35f:.ufo/round-40/claims.json` etc.) point at `.ufo/waves|round-N` trees — the
`.ufo/reports/round-\d+/…\.md` grammar correctly never sees them. Inventory exhausted.

Residual miss-classes (pre-existing, C1 does not repair, each measured live):

1. **Rev-prefixes the glue grammar cannot attach are silently downgraded to bare-path claims
   and now diverge between the gates.** E01 partitions on the first `:` (any head counts);
   E02's `REV_PREFIX_RE` only glues a ref-name starting with a letter or 7–40 hex ending in
   `:` at token start. World D (committed fixture):
   - `foo.md:15:.ufo/reports/round-77/kotoba.md` → E01 `report_dead`, E02 LIVE (bare path →
     fleet hop). A line-reference-shaped prose citation masks a `rev:`-form promise.
   - `HEAD@{1}:.ufo/reports/round-77/kotoba.md` → E01 `report_dead`, E02 LIVE (same hop).
     A *valid git revspec* E02 cannot see, so an object-level lie (`@{1}` is not the report's
     revision) resolves under the weaker existence claim. Both readings are live in the
     receipts; the fix belongs in E02's `REV_PREFIX_RE`/`report_target` divergence arm, or in a
     routed defect naming the grammar skew.
2. **Directory/report-path claims outside `…/*.md` stay invisible** (`.ufo/reports/round-8/`
   tokens in corpus are never harvested — pre-existing grammar bound, unchanged by R1/R2;
   corpus README already discloses this blind spot).
3. **Quoted pointers** (11 corpus sites, e.g. README:68) remain exempt from both existence and
   the new identity arm — documented context rule, still the masking surface it was.
4. **Plan-trigger staleness (calibration note, not a gate defect):** the plan §Trigger records
   independent `report_dead 1` at base; the live reading is `0` — the fleet file
   `.ufo/reports/round-77/kotoba.md` exists on disk today (landed 17:49 by `5d1f2e5a`, after the
   plan's receipt capture). E15Order §1 has the same corrected fact. Nobody may quote the
   plan's `1` as the independent base value.

## (b) `commit_truncated` / `commit_quoted` — did E01/E02 weaken the arms?

**No.** Diffed both code paths and measured: arm order is preserved in both patches —
quoted → truncated → nonhash → resolve → *then* the external reclassification, which attaches
only at the unresolvable point (`citation_findings` E01: `commit_resolves` first,
`commit_external` only on failure; `analyse_commits` E02: `token.lower() in externals` only at
the unresolved append). The superseded r80-E05 arms (`EXTERNAL_RE.match(token)` at nonhash,
`EXTERNAL_RE.search(line)` at unresolvable) are **gone** — a line marker no longer exempts.
Control readings: `commit `o/r@x`` → `nonhash` (not external); `deadbee` inside quotes →
`commit_quoted`; `7bb48f21…` → `commit_external=2` in both gates.

**But one laundering arm is still open in both gates (residual defect):**
`commit `<40 full hex>…`` classifies `commit_truncated` (context) — measured world B:
`deadbee0deadbee0deadbee0deadbee0deadbee0…` → `commit_truncated` in E01 and E02, while the
same hash without `…` → `commit_unresolvable` (red). `TRUNCATED_COMMIT_RE`/`TRUNCATED_RE` =
`[0-9a-fA-F]{7,40}…` treats a *complete* hash as a "prefix". Any dead external hash can be
cited with a trailing `…` and never reach `commit_unresolvable`. Smallest safe correction:
bound the hex prefix to `{7,39}` — all 4 existing corpus instances are genuine 7–8-char
prefixes (`fb6a28ee…`, `955ffd5d…`, `661e538…`, `56b0764e…`), so the tightening changes no live
number. Out of C1's declared repairs; route it.

## (c) Baseline refresh `--carry` — can a nonzero zero-class be smuggled?

**No nonzero `expect` can be recorded.** Read the r81 build copy (byte-identical to r80's,
per E15Order §1): `row["expect"] = 0` executes unconditionally for every zero-mode row before
any carry consult (line ~286); a nonzero observation *without* `--carry` exits 2 (`refused:
zero-mode … observed N` — measured). Index classes can never be carried (hard refuse).
Post-write re-check fails (exit 3) on any remaining DRIFT not in the carried set.

Residuals measured, none blocking but worth the routed note:

- **Carry is class-level and count-unbounded.** `--carry corpus.pointers.report_dead` permits
  N dead pointers where the known residual was 1; the count lands only in the
  `measured_against.note` prose, so a second defect in a carried class has no gate-visible
  signature. Smallest correction: carry `(check_id, expected_count)` pairs and refuse on a
  count mismatch.
- **SOFT_CROSS_CHECK tolerates live disagreement.** Measured: `gate disagreement …
  report_dead integrity 2 vs independent 0` printed, refresh proceeded to the unindexed
  refusal. With `--carry` + green index classes the write would succeed *while the gates
  disagree on a zero class* — the divergence is note-stamped, not refused.
- Dirty-tree refuse covers `--untracked-files=all`, so no uncommitted laundering path.

## (d) New red class introduced by the repairs — clean-stack reading

Instrument-only stack (base + E01 + E02, scratch `c15ebe88`): integrity zero classes all PASS
(`report_dead 0`, `commit_unresolvable 0`, `commit_nonhash 0`); the only DRIFTs are the
expected equal-mode/index rows (`tracked_files 155`, `report_total 111`, `unindexed 1`) that
R4 re-records. Independent: `report_dead 0`, `unresolvable 0`, `external 2` INFO.
**`commit_external` is added to `obs`/`DETAIL_KEYS` but not to `CHECKS` — INFO, never a
zero-mode verdict, consistent with the plan.** No new red class on the real corpus.

New binding-rule divergences introduced *between* the two repaired gates (asymmetry
findings — same corpus, different verdicts on edge classes):

- `external_binding` (E01) requires `receipt_sha256` (missing ⇒ fail closed) and 40-lower-hex
  manifest hash; `external_commits` (E02) makes the pin optional and admits 7–40 hex,
  `repo`/`evidence` alias keys, and hash-absent receipts. E01 binds fewer manifests; a crafted
  manifest could make E02 read `external` where E01 reads `unresolvable`. The committed
  manifest is well-formed so the real corpus agrees (both bind `7bb48f21…`), but the arms are
  not identical — worth pinning the stricter semantics (E01's) in both.
- `rev:` glue divergence from (a) — E01's looser partition catches revspecs E02 cannot
  (`HEAD@{n}:`, `<word>:<digits>:`), so an object claim reads DEAD in one gate and LIVE in the
  other.
- Path-object subtlety (pre-existing, now sharper): `.ufo/reports/round-76/kotoba.md` is a
  git symlink (blob `120000`, 43 B). `cat-file blob` returns link text, so a `rev:` object
  pointer to a symlinked report fails `## SHONEN`+400 B while a path pointer dereferences it —
  asymmetric kill coverage by design, no live corpus token affected (measured: only my planted
  probes flag).
- Full battery on the integrated stack: not re-run here (105 s; the corpus-gate delta above
  is the repair surface and E15Order/E06 measured the G1 stack battery `4 of 6` + controls).
  Unrun item, named.

## Verdict on C1's residual stack

The strengthened R1+R2 fix the W8/W9/W10 classes on both gates (verified by world), keep
`truncated`/`quoted`/`nonhash` arms intact, and the carry path cannot write a nonzero zero
class. The residuals that survive are: the `…`-after-full-hash laundering arm (both gates,
pre-existing, measured), the two-gate grammar/strictness divergences E01↔E02 (new this round),
class-level unbounded carry, and the stale plan-trigger number (independent `report_dead`
was 0, not 1). None reaches `6 of 6`; none is repaired by narrowing — each is a routed
correction or a named asymmetry.

VERDICT: residual stack falsified at three live points (full-hash-ellipsis laundering, E01/E02 rev-grammar + binding-strictness divergence, class-level carry); C1's repairs otherwise hold — no new red class, arms intact, external binding verified.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81C03Residual.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81C03Residual-receipts.txt
