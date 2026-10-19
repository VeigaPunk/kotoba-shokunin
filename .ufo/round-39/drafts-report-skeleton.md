# kotoba — round 39 report (2026-10-19) — SKELETON v1

> Scribe seat **B1**. Cells filled from seat reports in `.ufo/round-39/scouts/`.
> Shape mirrors `.ufo/reports/round-38/kotoba.md`. Every filled cell carries a
> command + observed output and names the sha it was measured at; unfilled cells
> stay `[PENDING]` — never smoothed. Re-measure at the landing commit.
>
> **Scribe measurement discipline.** The working tree moved continuously under
> this seat (sibling seats landed C1/C2/C3 edits live). Every "before" number
> below is taken from **frozen HEAD bytes** (`git show HEAD:<path>`); the live
> tree is recorded separately in § C0.1 as mid-flight sibling work.

Lane: `kotoba-shokunin`. Round 39, loop A position 3 of 12 (operator's fresh 3-loop regimen).
Dispatch HEAD: `1d027f2`. Work commit: `[PENDING]`.
Claims: **C1** depth (close R1-D1/D2/D3) · **C2** operability (V4's None-path + malformed-field arms) · **C3** freshness (corpus-gate CommonMark fence fix) — `.ufo/round-39/claims.json`.
Provider: `devin/deepseek-v4-1-flash-max` (operator amendment 2; token-plan key 2 re-probed 429 at dispatch, resets 10-23).
Swarm: `[PENDING]`/24 seats.
Status: `[PENDING]`.

## C0 — dispatch-HEAD state (scribe-measured before any r39 work)

**All 9 gates are GREEN at `1d027f2`** — the r38 carried reds are gone (contrast
r38's 5/8). `python3 verifiers/<gate>` at `1d027f2`, 14:11:39Z
(`drafts/b1/gate-battery-baseline-r39.txt`):

```
verify_harness_claims.py        28/28 checks pass                     rc=0
check_assertion_floors.py       8/8 PASS                              rc=0
verify_skill_checklist.py       PASS governance.citation_resolves 299  rc=0
verify_corpus_integrity.py      9/9 checks pass                       rc=0
verify_corpus_independent.py    exit 0                                rc=0
verify_surfaces.py              7 × PASS                              rc=0
check_substrate_pins.py         OK 3/3 pins hold (delta 0 ns)          rc=0
verify_harness_independent.py   24 derived, 4 scoped out, 0 unlanded  rc=0
compare_harness_independent.py  exit 0 — all agree, both green        rc=0
fault_injection_corpus.sh       self-test: OK                         rc=0
```

**Floors EXACT 8/8 at dispatch** — the r38 D5 headroom class is closed at HEAD
(`drafts/b1/floors-and-selftests-r39.txt`):

```
PASS harness observed=10 floor=10          PASS checklist observed=1597 floor=1597
PASS corpus_integrity observed=119 floor=119   PASS pins observed=62 floor=62
PASS corpus_independent observed=59 floor=59   PASS harness_independent observed=86 floor=86
PASS surfaces observed=87 floor=87         PASS compare_harness_independent observed=83 floor=83
```

All 8 `--self-test` counts green: `10 / 68 / 1597 / 119 / 59 / 87 / 62 / 86`.

Comparator at dispatch: `protocol 24/24; strict 19/24; adjudicated rows: 5;
disagree: 0; uncovered: 0; scoped-out: 4`, exit 0.

### C0.1 — the six r38 residuals, re-measured against frozen HEAD bytes

All six reproduce. Each row names the probe and its observed output; probes are
rebuilt from the r38 scout descriptions because `.ufo/round-38/drafts/` was
pruned at publish (see § Drift handling).

| # | Residual | Probe | Observed at HEAD bytes | State |
|---|---|---|---|---|
| C1a | **R1-D1 laundering hole** | `drafts/b1/probes/d1-laundering.py` arm 6 — keep the 4 real catalogue scope-outs, add the disputed `omp.offered.skills` as self-declared `SCOPED_OUT` | arm 1 (disagreement, no scope-out) **rc=1**; arm 6 (same disagreement + self-declared scope-out) **rc=0 — "all checks agree, both instruments green"** | **OPEN** |
| C1b | **R1-D2 predicate** | `grep -n init_count_monotone verifiers/verify_harness_independent.py` (HEAD bytes) | `:451-452` reads `sum(1 for v in init_counts.values() if v > 1)` — the "exceeds one" predicate, not the decrease test; the self-test asserts `1` where the predicate requires the empty list | **OPEN** |
| C1c | **R1-D3 doc/ledger** | doc §6 block run verbatim + `grep -n "a1-adjudication-ledger"` + sha cross-check | §6's 8 lines: 3 run (`--write-freeze` → sha `09fb71ca5e79d7f1…`, matching the doc; comparator → `24/24 exit 0`); **5 fail with `No such file or directory`** — the mutant leg, blind-tree script, `null_echo.py` control, `ind-bad-scope.json`, and the four-number-blocks script all point at the pruned `.ufo/round-38/drafts/w1/`. `grep` for the ledger → **rc=1, no reference**. §1/§5's *headline* is **not** stale (both already read `24/24 … exits 0`); what is stale is the **sha stamp**: lines 24/34 quote IND `82ad9700…` while live reads `e72d1e87…`, and line 213's "pre-existing red" (checklist exits 1 on `SCORECARD.md:131-133`) is now **green** (`checklist rc=0`) | **OPEN** |
| C2a | **None-path crash** | `drafts/b1/probes/c2-guard-arms.py --bytes head` arm P (`pins` row path → `None`) | **rc=1, uncaught `TypeError`** at the guard's `main()` — not the named exit 2 the pre-r38 guard produced | **OPEN** |
| C2b | **malformed FIELD** | same probe, arms H2/H4 | H2 (`floor=(62,)`): rc=2 with **2 FAIL lines** incl. the self-contradictory `FAIL registry floor drift: pins registry=62 expected=62 row=(62,)`. H4 (`floor=True`): rc=2, 2 FAIL lines incl. `floor drift: pins registry=62 expected=62 row=True` | **OPEN** |
| C3 | **fence false-PASS** | `drafts/b1/probes/c3-fence-exploit.py --bytes head`, cmark 0.31.2 as oracle, both gates | `short-closer` / `info-closer` / `closer-trailing`: cmark says the row is **fenced content**, both gates report `unindexed=0` / **exit 0** — silent false-PASS. `control-3backtick` and `foreign-char` are fail-safe | **OPEN** |

Control for C2: the unmutated guard in the same isolated world exits 0 with 8
PASS — the world is well-formed, so the arms measure the mutation, not the harness.

### C0.2 — live tree state (mid-flight sibling landings, informational)

The tree was dirty throughout this seat; three instruments moved under
measurement (`drafts/b1/midflight-snapshot.txt`, 14:16:27Z):

| Instrument | HEAD | live at 14:16Z | Effect observed |
|---|---|---|---|
| `verify_corpus_integrity.py` | `e6ddb217…` | `0d062a7b…` | C3 fix landed live — the 5-shape matrix now reads **fail-safe on all five** |
| `verify_corpus_independent.py` | `094d4673…` | `42c0062e…` | same; self-test 59 → **68** |
| `verify_harness_independent.py` | `82ad9700…` | `e72d1e87…` | C1b fix landed live — predicate is now the decrease list; self-test 86 → **93** |
| `check_assertion_floors.py` | `eaf5bf46…` | `c011f2cd…` (moved 3× in 4 min: `a26e8e80` → `6ca1cbbb` → `c011f2cd`) | C2 arms repaired live — **all three arms now close** (arm P named exit 2; H2/H4 single named line, no contradiction); self-test 68 → **105** |

**C2's three arms close on live bytes** (same probe, `--bytes live`,
`drafts/b1/probes/out-c2-guard-arms-live.txt`):

```
arm P  None path     rc=2  named exit 2 (CLOSED)
arm H2 nested floor  rc=2  FAIL lines=1  "FAIL registry malformed row: pins (non-integer floor (62,))"
arm H4 bool floor    rc=2  FAIL lines=1  "FAIL registry malformed row: pins (non-integer floor True)"
```

**The C1a laundering hole does NOT close on live bytes** — re-run against the
live comparator (`9a8c4cb4…`, unchanged) and live IND (`e72d1e87…`): arm 6 still
reads **exit 0**. Arms 1/3/4/7 are fail-closed (`rc=1 / 2 / 2 / 2`).

**Headroom transiently re-opened and re-closed mid-flight:** at 14:16Z the guard
read `PASS harness_independent observed=93 floor=86` — **SLACK**, the r38 D5
class — because the C1b self-test grew 86→93 before its registry floor was
bumped. By 14:19Z the sibling had bumped it in-step (`observed=93 floor=93`,
registry `93`), so **floors are EXACT 8/8 again on live bytes**. Recorded because
it is the exact class the round is closing; it was mid-flight, not a landing.

**The doc is unchanged at the HEAD measurement** (`2783b9f3…` live == HEAD at
14:16Z), so C0.1's R1-D3 findings hold for the before-state.

**LATE UPDATE (14:22Z–14:29Z) — C1 landed mid-seat, and R1-D1 now closes.**
After this skeleton's C0 sections were written, siblings landed the C1 fixes:

- `compare_harness_independent.py` `9a8c4cb4…` → `95b29991…` → **`f8e0079b…`**.
  The D1 fix is now the shape R1 recommended: a **committed**
  `verifiers/harness-independent-scope.json` (schema
  `kotoba-harness-independent-scope-v1`, "the AUTHORITATIVE scope-out set. The
  comparator reads it from here, never from the payload under test") plus a
  recomputable `probe_contract`. Re-run of my probe against it:
  **arm 6 `rc=0` → `rc=2` "FAILS CLOSED"**; arms 1/2/3/4/7 all fail-closed
  (arm 1 exit 1 = the disagreement is named).
- The new comparator also carries a **channel-split check** that caught a flaw in
  my own arm 1 (records marked `SCOPED_OUT` while the map omitted them). My probe
  bug, fixed; arm 1 then reads the correct exit 1.
- `corpus/knowledge/harness-independent-round37.md` `2783b9f3…` → `cf73c668…` →
  **`f68c9665…`** (+110/−31): the ledger is referenced (2×) and **§6's block now
  runs green verbatim** — 90 lines, **rc=0, 240 lines of output**, every
  `w1/`-dependent line replaced by an inline rebuild. The 3 remaining `w1/`
  mentions are prose/comment, not dead commands.
- `verify_harness_independent.py` → `1e50a54d…` (predicate = decrease list);
  `check_assertion_floors.py` → `d2bbe432…`; floors `…/104/93`.

`[PENDING: landing-commit re-run of all of the above — the mid-flight shas are
evidence of direction, not of the landed state]`

## Work performed

`[PENDING — one block per claim, filled from late-arriving seat reports; each block needs a seat citation and its own command + output]`

- **C1 (depth) — `[PENDING]`.** Declared: close R1-D1 (machine-checkable scope-out discriminator, or read the scope-out set from a committed corpus file), R1-D2 (`init_count_monotone` predicate + `init_count_max` adjudication re-filed with fixtures), R1-D3 (doc/ledger reconciliation with fresh sha-stamped numbers and a §6 block that runs green verbatim). *Scribe-measured before-state: all three open (§ C0.1).* Live mid-flight evidence that D2's predicate fix is landing (`e72d1e87…`). `[PENDING: after-state + R1's counter-probe re-run at the landing commit]`
- **C2 (operability) — `[PENDING]`.** Declared: (a) `path=None` must name exit 2; (b) malformed-FIELD arms (`floor=(62,)`, `floor=True`) must fail named without the contradiction line; ≥3 new true-discriminator fixtures; floors bumped in-step; V4's full hunt list re-run with no new regression. *Scribe-measured before-state: all three open (§ C0.1).* `[PENDING: after-state + V4 hunt-list re-run]`
- **C3 (freshness) — `[PENDING]`.** Declared: apply the minimal CommonMark 4.5 closer rule to `fenced_lines` / `fenced_line_numbers` in **both** corpus instruments; three exploit shapes flip to fail-safe; fixtures pin them in both self-tests; live corpus sweep confirms 0 incidence; both replays green. *Scribe-measured before-state: 3 silent false-PASS shapes reproduced end-to-end (§ C0.1); live mid-flight the fix is already in and all 5 shapes are fail-safe.* `[PENDING: landing-commit confirmation + the 0-incidence sweep + floors in-step]`
- **Deliberately not done:** `[PENDING]`

## Landed changes

`[PENDING: work commit sha from the integrator]` — the live tree at this draft's
write carries sibling edits to `verifiers/check_assertion_floors.py`,
`verifiers/verify_corpus_integrity.py`, `verifiers/verify_corpus_independent.py`,
`verifiers/verify_harness_independent.py`, `verifiers/floors-registry.json`,
plus `.ufo/round-39/`. `[PENDING: full file list at the landing commit]`

## Before → after measurements

| Claim | Measurement | Before (frozen HEAD `1d027f2` bytes) | After (live tree at scribe write time) |
|---|---|---|---|
| C1 | R1-D1 arm 6 (self-declared scope-out) | **exit 0 — laundered** (exit 1 without the declaration) | **exit 0 at 14:19Z (OPEN) → exit 2 at 14:22Z (CLOSED)** as the C1 landing moved the comparator to `95b29991…` |
| C1 | R1-D1 arms 1/3/4/7 (disagreement / empty declaration / undeclared deletion / scoped_out naming a DERIVED row) | exit 1 / exit 2 / exit 2 / exit 2 | unchanged — fail-closed |
| C1 | `init_count_monotone` predicate | `v > 1` at `:451-452`; self-test asserts `1` | live `e72d1e87…` reads the **decrease list** (`[f"{init_values[i-1]}->{init_values[i]}" …]`); self-test 86 → **93** `[PENDING: fixture-backed mutant arms at the landing commit]` |
| C1 | doc §6 verbatim | **3/8 lines run; 5/8 dead** (pruned `drafts/w1/` paths) | **rc=0** — the rewritten block rebuilds every pruned input inline (90 lines, 240 output lines) |
| C1 | doc ↔ ledger | no reference to `a1-adjudication-ledger.md` (grep rc=1) | **2 references** after the doc rewrites to `f68c9665…` |
| C1 | doc §6 verbatim | **3/8 lines run; 5/8 dead** (pruned `drafts/w1/` paths) | **rc=0 — 90 lines, 240 output lines, every `w1/`-dependent line rebuilt inline** |
| C1 | doc sha stamps | quotes IND `82ad9700…` (lines 24/34) | live IND `e72d1e87…` — **stale**; line 213's "pre-existing red" (checklist rc=1) is now **green** (rc=0) |
| C1 | floors | 8/8 EXACT (`…/62/86/83`) | live 8/8 EXACT (`…/62/93/83`) after the in-step bump — a transient `93/86` SLACK was observed at 14:16Z and closed by 14:19Z |
| C2 | `pins` row path=None | **rc=1 uncaught TypeError** | **rc=2 named exit 2 (CLOSED)** |
| C2 | `floor=(62,)` nested tuple | rc=2, 2 FAIL lines incl. contradiction | **rc=2, 1 FAIL line — `malformed row: pins (non-integer floor (62,))`** (contradiction gone) |
| C2 | `floor=True` bool floor | rc=2, 2 FAIL lines incl. contradiction | **rc=2, 1 FAIL line — `malformed row: pins (non-integer floor True)`** |
| C2 | guard `--self-test` | 68 | **105** |
| C2 | live guard stdout | 8/8 PASS rc=0 | 8/8 PASS rc=0 `[PENDING: byte-invariance diff vs HEAD stdout]` |
| C3 | 5-shape fence matrix (cmark 0.31.2 oracle) | **3 silent false-PASS** on both gates | **0 silent false-PASS — all 5 shapes fail-safe** on both gates |
| C3 | corpus_integrity / corpus_independent self-tests | 119 / 59 | **129 / 68** |
| C3 | live corpus incidence sweep | 0 expected (V6b F6) | **0 incidence confirmed**: 53 corpus docs, 144 fence-like lines, **0 at column 4+** (`drafts/b1/` sweep, live bytes) |
| C3 | live stdout byte-invariance | — | **IDENTICAL**: both gates produce the same stdout sha under `--repo .` from HEAD bytes and live bytes (`integrity c5eaf1a5…`, `independent ff1da383…`) |
| gates | 9-gate battery | **all green at `1d027f2`** | **all green on live bytes** (re-measured 14:19Z) `[PENDING: landing-commit re-run]` |

## Axis verdicts

`[PENDING — the landing commit's re-run is the authority]`

- **depth (C1)** — `[PENDING]`. Scribe's measured state, by leg: **D2 fixed** (predicate = decrease list, `1e50a54d…`; self-test 86→93→104). **D1 closed** — the comparator now reads the scope-out set from a **committed** `verifiers/harness-independent-scope.json` with a recomputable `probe_contract` (`f8e0079b…`), and my laundering arm 6 reads **exit 2, fail-closed** where it read exit 0 at HEAD; arms 1/2/3/4/7 all fail closed. **D3 satisfied** — the doc (`f68c9665…`) references A1's ledger twice and its §6 block now **runs green verbatim (rc=0, 90 lines, 240 output lines)**, with every pruned `w1/` input rebuilt inline. The mechanism is otherwise sound: comparator `24/24` protocol / `19/24` strict, 4 rows scoped out by name. **Scribe's caveat:** every "before" number rests on a *rebuilt* probe set (the r38 drafts were pruned), and all three legs' fixes are **mid-flight evidence** — the landing commit's re-run is the authority, and the round's counting clause should be read against a rebuilt counter-probe set.
- **operability (C2)** — `[PENDING]`. Scribe's measured state: **all three arms close** (named exit 2 for the None path; single named line, no contradiction, for both malformed-field arms); guard self-test 68 → 105; live guard 8/8 PASS rc=0. Residual from V4 not re-measured this seat: copy-variant matrix 1/30 green, path confinement unenforced.
- **freshness (C3)** — `[PENDING]`. Scribe's measured state: the 3 silent false-PASS shapes reproduce at HEAD and are **closed on live bytes** (all 5 fail-safe, cmark as oracle); self-tests 119→129 and 59→68. Remaining: the 0-incidence live sweep and the floors/byte-invariance confirmation.
- **consistency / coverage / calibration / adjacency** — `[PENDING]`.

Drift handling (must be written into the published report):
- **Probe provenance.** `.ufo/round-38/drafts/` was pruned at publish, so every r38 counter-probe named in the r38 scouts is gone. This seat **rebuilt** the D1 laundering probe, the C2 guard arms, and the C3 fence exploit from the scouts' own descriptions (`R1.md` F-2, `V4.md` §3/§4, `V6b.md` F5) and re-measured them; the rebuilds live under `drafts/b1/probes/` with their outputs. A rebuild is not the original probe — numbers may differ in the arms' incidental details, and no r38 number is quoted here as re-verified.
- **Shape traps found while rebuilding** (recorded, not smoothed): (i) the comparator's `parse_independent` / `_record_list` returns the **first** of `("results", "rows", "checks")` — IND publishes both `results` and `rows`, so a probe mutating only `rows` measures nothing (arm 5 of the D1 probe: rc=0 while `rows` said 5 and live said 7); (ii) the corpus gates require a **git repo** and read only **backticked column-2 tokens inside the coverage section** — a throwaway world without them reads `unindexed=3` and a naive probe reports a false "fail-safe"; (iii) `verify_corpus_integrity.py` returns **rc=3** when no baseline is present while still naming the unindexed rows, so `rc` alone is not the verdict signal.
- `[PENDING: claim-text corrections, denominator corrections, and any erratum the round owes]`

## SHONEN

> Measured at `1d027f2`. `[PENDING: re-run box counts + floors at the landing commit before pasting into the published report]`.

- [~] box 1 (decision tables / error patterns / checklists / cited sources, `SHONEN.md:5`) —
  `SKILL.md` at HEAD: **13 `##` sections, 41 checkbox lines**; § Sources = **38 bullets**, and
  `PASS trigger.citation_resolves: evaluated 38 — 38 repo-rooted citation token(s) resolve`;
  `PASS governance.citation_resolves: evaluated 299 — 299 … across 2 files`.
  Anti-pattern home `corpus/knowledge/fail-closed-and-anti-patterns.md` carries the table
  (`corpus/README.md:11` still says "18-row" — the stale-count defect carried from r38, not fixed this round).
- [~] box 2 (end-to-end task executed and logged, `SHONEN.md:16`) —
  the round is an e2e craft task; `python3 verifiers/verify_harness_claims.py` → `28/28 checks pass` rc=0 (re-run at `1d027f2`).
  The newest non-author cold run remains round 11 — nothing this round restores `[x]`.
- [~] box 3 (instructions executable without oral context, `SHONEN.md:22`) —
  all 9 gates run cold and green at `1d027f2` (§ C0); the comparator, the corpus doc's §6, and the guard are committed and re-runnable.
  **Caveat this round:** the corpus doc's §6 is **5/8 dead** at HEAD (§ C0.1 C1c) — box 3's pointer is weakened until C1 lands.
- [~] box 4 (no cross-domain bleed; `PROVINCE.md` accurate, `SHONEN.md:41`) —
  `git log -1 --format="%h %ad %s" --date=short -- PROVINCE.md` → `43e0c02 2026-09-28 seed: kotoba shonen` (unchanged); this seat wrote only inside the lane repo.

No `[x]`: no named non-author verifier exists (PROTOCOL: a lane-dispatched subagent is still the lane).
