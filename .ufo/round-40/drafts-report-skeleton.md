# kotoba — round 40 report (2026-10-19) — SKELETON v1

> Scribe seat **B1**. Cells filled from seat reports in `.ufo/round-40/scouts/`.
> Shape mirrors `.ufo/reports/round-39/kotoba.md`. Every filled cell carries a
> command + observed output and names the sha it was measured at; unfilled cells
> stay `[PENDING]` — never smoothed. Re-measure at the landing commit.
>
> **Scribe measurement discipline.** Every "before" number below is taken from
> **frozen HEAD bytes** (`git show HEAD:<path>`, HEAD = `1c32b43`) or from frozen
> copies under `.ufo/round-40/drafts/b1/frozen/`; the live tree is recorded
> separately. All probes live under `.ufo/round-40/drafts/b1/probes/` with their
> raw outputs under `.../out/`.

Lane: `kotoba-shokunin`. Round 40, loop A position 4 of 12.
Dispatch HEAD: `1c32b43` (r39's publish commit; `git rev-parse HEAD`).
Work commit: `[PENDING]`.
Claims: **C1** depth (close R1's F-2/F-3 — the surviving value + list channels) · **C2** operability (V3's copy-variant `--script` + path-confinement pair) · **C3** freshness (V4's closer-indent residual) — `.ufo/round-40/claims.json`.
Provider: `devin/deepseek-v4-1-flash-max` (pos-4 plan = hyper/deepseek-v4.1-flash; hyper remaining_credits 0 dry per r38/r39 record → devin fallback, recorded; token-plan key 2 429 until 10-23, amendment 2).
Swarm: `[PENDING]`/40 seats.
Status: `[PENDING]`.

## C0 — dispatch-HEAD state (scribe-measured before any r40 work)

**All 10 gate families are GREEN at `1c32b43`.** Re-run: the loop in
`drafts/b1/out/gate-battery-head.txt` (each `python3 verifiers/<gate>`, `rc`
captured), 2026-10-19, at HEAD `1c32b43`:

```
verify_harness_claims.py        28/28 checks pass                     rc=0
check_assertion_floors.py       8/8 PASS                              rc=0
verify_skill_checklist.py       10 × PASS                             rc=0
verify_corpus_integrity.py      9/9 checks pass                       rc=0
verify_corpus_independent.py    exit 0                                rc=0
verify_surfaces.py              7 × PASS                              rc=0
check_substrate_pins.py         OK 3/3 pins hold (delta 0 ns)          rc=0
verify_harness_independent.py   24 derived, 4 scoped out, 0 unlanded  rc=0
compare_harness_independent.py  exit 0 — all agree, both green        rc=0
fault_injection_corpus.sh       self-test: OK                         rc=0
```

**Floors EXACT 8/8 at dispatch** — re-run `python3 verifiers/check_assertion_floors.py`
(`drafts/b1/out/floors-head.txt`):

```
PASS harness observed=10 floor=10                PASS checklist observed=1597 floor=1597
PASS corpus_integrity observed=129 floor=129     PASS pins observed=62 floor=62
PASS corpus_independent observed=68 floor=68     PASS harness_independent observed=104 floor=104
PASS surfaces observed=87 floor=87               PASS compare_harness_independent observed=97 floor=97
```

All nine `--self-test` counts green, 0 failures each:
`10 / 109 / 1597 / 129 / 68 / 87 / 62 / 104 / 97` (`drafts/b1/out/self-tests-head.txt`).

Comparator at dispatch (`drafts/b1/out/cmp-head.txt`): `protocol 24/24; strict 20/24;
adjudicated rows: 4; disagree: 0; uncovered: 0; unknown: 0; provisional: 0;
scoped-out: 4; secondary 20/24`, exit 0.

Instrument shas at `1c32b43` (`git show HEAD:<path> | sha256sum | cut -c1-16`):

```
compare_harness_independent.py  bb8dcecd65f160d3   verify_harness_independent.py  872993f875338f4f
check_assertion_floors.py       df6ddbc2b6d378e3   verify_corpus_integrity.py     0d062a7bc904934c
verify_corpus_independent.py    42c0062e4fa3b24c   floors-registry.json           dad46fbbf748f4c8
harness-independent-scope.json  fbcdc8d247475a5f
```

### C0.1 — the three r40 residuals, re-measured against frozen HEAD bytes

All three reproduce. Each row names the probe and its observed output.

| # | Residual | Probe (re-run command) | Observed at HEAD bytes | State |
|---|---|---|---|---|
| C1a | **F-2 value channel** | `python3 .ufo/round-40/drafts/b1/probes/c1-value-channel.py --label head` arm `F2a-min` (one row: harvested `expected`, `re_derived`/`value` = `"NOT DERIVED"`) | **exit 0 — `all checks agree, both instruments green`, joined 24/24** | **OPEN** |
| C1b | **F-2 full copy-satisfaction** | same probe, arm `F2b-full` (all 28 records carry the harvested live `expected` as their value; every derived field `"NOT DERIVED"`) | **exit 0 — 24/24**; the comparator's own secondary column reads **28/28** where the control reads 20/24 — the driver is comparing the live expected against itself | **OPEN** |
| C1c | **F-3 list channel — `rows`** | same probe, arm `F3-rows` (`results` clean, `rows` carries `999` for `omp.offered.skills`) | **exit 0 — 24/24** | **OPEN** |
| C1d | **F-3 list channel — `checks`** | same probe, arm `F3-checks` (divergence hidden in the `checks` map; V1's A7 class) | **exit 0 — 24/24** | **OPEN** |
| C1e | *direction control* | same probe, arm `RED-divergent-derived` (plain divergent `re_derived`, no `expected`) | **exit 1 — `disagreements: omp.offered.skills (mode=equal: expected 999, observed 7)`** — the arms are not vacuous | control |
| C2a | **copy-variant `--script`, absolute argv** | `python3 .ufo/round-40/drafts/b1/probes/c2-guard-arms.py --label head` arms `foreign-copy-abs` / `foreign-link-abs` / `foreign-hard-abs` | **all three `rc=0` SILENT-GREEN**, and the guard's own output proves the substitution: `PASS stub observed=5 floor=3` where the row's own stub reads 3 | **OPEN** |
| C2b | *same, relative argv* | same probe, arms `foreign-link-rel` / `foreign-canon-rel` | `rc=2` named — `FAIL registry override repoint: stub -> …/stub-instrument-2.py (canonical instrument for stub2)` | control |
| C2c | **path confinement** | same probe, arms `row-dotdot` (`../outside/…`) and `row-abs-outside` (absolute outside `--repo`) | **both `rc=0`** — `PASS stub observed=3 floor=3`, unenforced | **OPEN** |
| C3a | **closer-indent, unit** | `python3 .ufo/round-40/drafts/b1/probes/c3-closer-indent.py --label head` | `4space-closer` / `tab-closer`: cmark block `1:1-4:4` (row is content) but both gates read the row as unfenced → **MISMATCH**; `0/1/3`-space controls agree | **OPEN** |
| C3b | **closer-indent, end-to-end** | same probe, e2e section (throwaway git world; the only mention of `knowledge/b.md` is the row after the pseudo-closer) | `4space` / `tab`: **`rc=0` on BOTH gates** (`9/9 checks pass` / `exit 0`) where cmark says the row is content → **SILENT-FALSE-PASS**; the three controls read the row as a promise, correctly | **OPEN** |
| C3c | *live incidence* | `drafts/b1/out/corpus-sweep-head.txt` (tracked corpus `.md`, fence-like lines by indent column) | 53 docs, **146** fence-like lines, **0 at column ≥ 4**, **0 with a TAB** | 0 live |

**C3c's 146 vs r39's 144 — named, not smoothed.** r39's report and LOG quote 144
fence-like lines; that count was taken *before* r39's landing commit. The landing
commit `1c32b43` added the reconciled `corpus/knowledge/harness-independent-round37.md`
(`git diff --name-only 1d027f2 1c32b43 -- corpus` → that one file), which carries 2
more fence-like lines: `1d027f2` → 144, `1c32b43` → 146, both 53 docs, both
**0 at column ≥ 4**. Re-run: the `for rev in 1d027f2 1c32b43` loop in
`drafts/b1/out/corpus-sweep-both-revs.txt`.

### C0.2 — live tree state (informational)

At the time of writing, `git status --porcelain` reads `?? .ufo/round-40/` only —
the tree has **not moved** since the r39 publish. All six instrument shas above are
byte-identical live (`drafts/b1/out/live-vs-frozen-head.txt`), so every before-cell
here is simultaneously a live-tree reading. `[PENDING: re-check at the landing commit]`

## Work performed

`[PENDING — one block per claim, filled from seat reports; each block needs a seat
citation and its own command + output]`

- **C1 (depth) — `[PENDING]`.** Declared: (a) the driver must not accept a harvested
  value through `expected`/`expected_value` (drop them from `IND_VALUE_KEYS`, or
  cross-check the value channels so a value present in `expected` but
  absent/`NOT DERIVED` in the derived fields fails closed); (b) `_record_list` must
  reconcile ALL of `results`/`rows`/`checks`, not read-first; R1's F-2/F-3 payloads
  must flip exit 0 → exit 2 class-named while the live comparator still exits 0 24/24
  over the landed scope. *Scribe-measured before-state: all four arms exit 0 24/24
  (§ C0.1 C1a-C1d), with the direction control red (§ C1e).* `[PENDING: after-state
  + the rebuilt probes at the landing commit + live comparator 24/24]`
- **C2 (operability) — `[PENDING]`.** Declared: (a) an absolute-argv symlink/hardlink/
  copy override aimed at another row's target must fail class-named (resolve +
  canonicalize), or the residual is formally declared in the trust boundary with the
  reason recorded; (b) a `--repo` escape / `../` traversal must be rejected class-named
  exit 2; ≥2 new true-discriminator fixtures; self-test grows with floors bumped
  in-step. *Scribe-measured before-state: three copy arms silent-green, both
  confinement arms unenforced (§ C0.1 C2a/C2c).* `[PENDING: after-state + fixtures +
  floors + live 8/8 EXACT byte-invariant]`
- **C3 (freshness) — `[PENDING]`.** Declared: add the `indent <= 3` clause to the
  closer predicate in BOTH `verify_corpus_integrity.py fenced_lines` and
  `verify_corpus_independent.py fenced_line_numbers`; fixture battery for the 4-space
  and tab shapes in both self-tests; live corpus sweep still 0 incidence; live stdout
  byte-invariant. *Scribe-measured before-state: both shapes silent false-PASS on both
  gates, unit and e2e (§ C0.1 C3a/C3b).* `[PENDING: after-state + both self-tests +
  floors + sweep + byte-invariance]`
- **Deliberately not done:** `[PENDING]`

## Landed changes

`[PENDING: work commit sha from the integrator]` — the live tree at this draft's write
is unchanged from `1c32b43` except `.ufo/round-40/`. `[PENDING: full file list at the
landing commit]`

## Before → after measurements

| Claim | Measurement | Before (frozen HEAD `1c32b43` bytes) | After (round 40) |
|---|---|---|---|
| C1 | F-2 min: harvested `expected` + `"NOT DERIVED"` derived fields, one row | **exit 0 — 24/24, `all checks agree`** | `[PENDING]` |
| C1 | F-2 full: all 28 records carry the harvested live `expected` as their value, every derived field `"NOT DERIVED"` | **exit 0 — 24/24** (full copy-satisfaction, zero derivation); the comparator's own secondary column reads **28/28** where the control reads 20/24 — it compares the live expected against itself | `[PENDING: must stay ≤ 20/24 secondary]` |
| C1 | F-3: divergent value in `rows` / in `checks` (read-first channel) | **exit 0 — 24/24 each** | `[PENDING]` |
| C1 | direction control: plain divergent `re_derived` | exit 1 — `disagreements: omp.offered.skills (mode=equal: expected 999, observed 7)` | `[PENDING: must stay exit 1]` |
| C1 | live comparator over the landed scope | exit 0 — protocol `24/24`, strict `20/24`, adjudicated 4, scoped-out 4 | `[PENDING: must stay exit 0 24/24]` |
| C2 | copy / symlink / hardlink of another row's target, absolute argv | **exit 0 SILENT-GREEN** (guard prints `PASS stub observed=5 floor=3` — it ran the foreign file) | `[PENDING: named exit 2, or a declared trust-boundary line]` |
| C2 | relative-argv link / canonical path (control) | exit 2 — `FAIL registry override repoint: stub -> …` | `[PENDING: must stay named]` |
| C2 | `../` traversal + absolute path outside `--repo` | **exit 0 — unenforced** | `[PENDING: named exit 2]` |
| C2 | guard `--self-test` | 109 | `[PENDING]` |
| C2 | live guard stdout | 8/8 PASS rc=0 | `[PENDING: byte-invariance diff vs HEAD stdout]` |
| C3 | 4-space pseudo-closer (unit) | **MISMATCH** — cmark `1:1-4:4`, both gates treat the closer as a closer | `[PENDING]` |
| C3 | 4-space / tab pseudo-closer (e2e, both gates) | **rc=0 SILENT-FALSE-PASS** on both | `[PENDING: unindexed=1 exit 1 fail-safe]` |
| C3 | 0/1/3-space controls (e2e, both gates) | rc=0, row correctly a promise | `[PENDING: must stay rc=0]` |
| C3 | corpus_integrity / corpus_independent self-tests | 129 / 68 | `[PENDING]` |
| C3 | live corpus sweep | 146 fence-like lines, **0 at column ≥ 4**, 0 tabs | `[PENDING: 0 incidence expected to hold]` |
| C3 | live stdout byte-invariance | — | `[PENDING]` |
| gates | 10-gate battery | **all green at `1c32b43`** | `[PENDING: landing-commit re-run]` |
| gates | floors | 8/8 EXACT `10/129/68/87/1597/62/104/97` | `[PENDING]` |

## Axis verdicts

`[PENDING — the landing commit's re-run is the authority]`

- **depth (C1)** — `[PENDING]`. Scribe's measured state: all four attack arms read
  exit 0 24/24 at HEAD with the direction control red, so the F-2/F-3 class is live
  exactly as R1 filed it. `[PENDING: does the closure hold on the rebuilt probes and
  does the live comparator stay 24/24?]`
- **operability (C2)** — `[PENDING]`. Scribe's measured state: three absolute-argv
  copy arms silent-green (proven by the guard's own `observed=5`), both confinement
  arms unenforced; the relative-argv forms already fail closed. `[PENDING]`
- **freshness (C3)** — `[PENDING]`. Scribe's measured state: the 4-space and tab
  shapes are silent false-PASS on both gates at unit and end-to-end level; the
  ≤3-space controls agree with cmark; live incidence 0. `[PENDING]`
- **consistency / coverage / calibration / adjacency** — `[PENDING]`.

Drift handling (must be written into the published report):
- **Shape note for the integrator.** The r39 *published* report carries axis verdicts
  as a bolded paragraph ("Axis verdicts: **depth — unchanged** …") rather than as a
  `##` section; this skeleton keeps a `## Axis verdicts` section so the per-axis cells
  are individually addressable while the round is in flight. Collapse to the published
  shape at integration — the content is the same and no cell may be dropped in the
  collapse.
- **Probe provenance.** `.ufo/round-39/drafts/` was pruned at publish (PRUNE.log kept
  the skeleton, B2's SHONEN block, B2's verdict table and the at-head instrument pins).
  This seat **rebuilt** the C1 value/list-channel probe, the C2 guard arms and the C3
  closer-indent probe from R1's / V3's / V4's own filed descriptions and re-measured
  them; the rebuilds live under `drafts/b1/probes/` with their outputs. A rebuild is
  not the original probe.
- `[PENDING: claim-text corrections, denominator corrections, and any erratum the round owes]`

## SHONEN

> Measured at `1c32b43`. `[PENDING: re-run box counts + floors at the landing commit
> before pasting into the published report]`.

- [~] box 1 (decision tables / error patterns / checklists / cited sources, `SHONEN.md:5`) —
  `git show HEAD:SKILL.md | grep -c "^## "` → **13**; `… | grep -c '^- \[[ x~]\]'` → **41**
  checkbox lines; § Sources → **38** bullets; live gate reads
  `PASS trigger.citation_resolves: evaluated 38 — 38 repo-rooted citation token(s) resolve`;
  `PASS governance.citation_resolves: evaluated 308 — 308 governance citation token(s)
  resolve across 2 files`. Anti-pattern home `corpus/knowledge/fail-closed-and-anti-patterns.md`
  carries 29 pipe rows across two tables (distilled at `:48`, full at `:58`).
  Stale-count defect carried: `corpus/README.md:11` still says "18-row".
- [~] box 2 (end-to-end task executed and logged, `SHONEN.md:16`) —
  `python3 verifiers/verify_harness_claims.py` → `28/28 checks pass` exit 0 (re-run at
  `1c32b43`); the newest non-author cold run on record remains round 11 — nothing this
  round restores `[x]`.
- [~] box 3 (instructions executable without oral context, `SHONEN.md:22`) — all 10 gate
  families run cold and green at `1c32b43` (§ C0); floors 8/8 EXACT; every `--self-test`
  0 failures; `python3 verifiers/verify_skill_checklist.py` → `10 × PASS`
  (`box_map evaluated 41 — 41 boxes mapped (8 executed, 0 delegated, 33 unexecuted)`,
  `line_budget evaluated 521 within budget 600`). `[PENDING: re-run at the landing commit]`
- [~] box 4 (no cross-domain bleed; `PROVINCE.md` accurate, `SHONEN.md:41`) —
  `git log -1 --format="%h %ad %s" --date=short -- PROVINCE.md` →
  `43e0c02 2026-09-28 seed: kotoba shonen` (unchanged); this seat wrote only inside
  `.ufo/round-40/drafts/b1/`.

No `[x]`: no named non-author verifier exists (PROTOCOL: a lane-dispatched subagent is
still the lane). The canonical-form findings on `SHONEN.md` remain named, not smoothed.
