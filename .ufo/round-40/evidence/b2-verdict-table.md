# Round-40 per-axis verdict table — seat B2|scribe-shonen

> Dispatch HEAD `1c32b43`. Measured 2026-10-19 15:02-15:30Z. **The tree moved twice mid-seat**, so
> the before-column is split: rows marked **[HEAD bytes]** were re-verified against frozen bytes in
> `drafts/b2/pin/` (re-runnable after the round lands); rows marked **[live]** were read off the
> worktree at the timestamp given.

Frozen pin (`drafts/b2/pin/`, all from `git show 1c32b43:`):
`compare_harness_independent.py bb8dcecd65f160d3…` · `verify_harness_independent.py 872993f875338f4f…` ·
`check_assertion_floors.py df6ddbc2b6d378e3…` · `verify_corpus_integrity.py 0d062a7bc904934c…` ·
`verify_corpus_independent.py 42c0062e4fa3b24c…` · `floors-registry.json dad46fbbf748f4c…`.

| Claim | Axis | Measurement | Before (dispatch) | After / live (round 40) |
|---|---|---|---|---|
| C1-F2 | depth | harvested value in `expected`, derived fields `"NOT DERIVED"` — 1 row | **[HEAD bytes]** exit 0, `24/24` | live `727ec676`: exit 0 (fix not landed) |
| C1-F2 | depth | same on **all 24 joined rows** (`probe-m2-full-copy-satisfaction.json`) | **[HEAD bytes]** exit 0, `24/24`, **strict `24/24`**, `adjudicated rows: 0` — a full copy-satisfaction with zero derivation | live `727ec676`: identical |
| C1-F3 | depth | `rows` carries `999` for `omp.offered.skills`, `results` clean | **[HEAD bytes]** exit 0, `24/24` | live: identical |
| C1-F3 | depth | `checks` (dict) carries `999`, `results` clean | **[HEAD bytes]** exit 0, `24/24` | live: identical |
| C1 | depth | control: unmutated live IND payload | **[HEAD bytes]** exit 0, `24/24`, strict 20/24 | live: exit 0, strict 20/24 |
| C1 | depth | live IND emits `expected`/`expected_value` in **0 of 28** records | premise confirmed: the accepted-first key is one the instrument never produces | unchanged |
| C1 | depth | source `IND_VALUE_KEYS` `:119`, consumed `:267`; `_record_list` `:230-237` reads first of `results`/`rows`/`checks` | both defects present | **`_record_list` and `IND_VALUE_KEYS` unchanged at `727ec676`**; a new `fixtures/rows-shadow` fixture exists and is red (`FAILED: fixtures/rows-shadow: named failure`) |
| C1 | depth | comparator self-test, live | exit 0, 97 assertions | **`2daeee7a`: still RED — `FAILED: fixtures/expected-launder` (3 failures / 118)** |
| C1 | depth | **F-2 minimal form** at the last live sha `2daeee7a` (substrate-fresh capture, control green) | **[HEAD bytes]** exit 0 | **still exit 0, `24/24`** — F-2 has NOT closed |
| C1 | depth | **F-3 shadow arms** at `2daeee7a` (rows with the read key mutated; checks mutated) | **[HEAD bytes]** exit 0 both | **exit 2 both**, class-named `channel divergence …` — F-3 closes |
| C1 | depth | caveat: my `m2` arm at `2daeee7a` reads exit 2 | — | fires on the divergence the **arm itself** created (mutating `results` alone) — F-3's door, **not** evidence F-2 closed |
| C2 | operability | `--script harness=<abs-argv COPY of corpus_integrity>` | **[HEAD bytes]** exit 0, **silent-green** — `PASS harness observed=129 floor=10` | live: not re-measured post-landing |
| C2 | operability | same with a **symlink** | **[HEAD bytes]** exit 0, **silent-green** | — |
| C2 | operability | control: the world's own canonical corpus_integrity path as abs argv | **[HEAD bytes]** exit 2 `registry override repoint: harness -> … (canonical instrument for corpus_integrity)` | — |
| C2 | operability | confinement: guard table **and** registry agree on an absolute path **outside** `--repo` | **[HEAD bytes]** **exit 0, 8 × PASS** | — |
| C2 | operability | confinement: both agree on `../../../tmp/b2-escape-target/…` (existing outside file) | **[HEAD bytes]** **exit 0, 8 × PASS** | — |
| C2 | operability | confinement via argv: `--script harness=<outside path>` | **[HEAD bytes]** **exit 0, 8 × PASS** | — |
| C2 | operability | control: unmutated version-matched world | **[HEAD bytes]** 8 × PASS exit 0 | — |
| C2 | operability | source `override_drift` `:279-301`: canonical `.resolve()`d, argv kept **raw**; **no check compares any path to `--repo`** | mechanism confirmed | unchanged at live `3d7e6f38` |
| C3 | freshness | end-to-end world, cmark 0.31.2 oracle: **4-space** pseudo-closer | **[HEAD bytes]** **SILENT-FALSE-PASS** — both gates `rc=0 unindexed=0` | **LIVE: AGREE (fail-safe)** — both gates `rc=1 unindexed=1` |
| C3 | freshness | same with a **tab** pseudo-closer | **[HEAD bytes]** **SILENT-FALSE-PASS** | **LIVE: AGREE (fail-safe)** `rc=1 unindexed=1` |
| C3 | freshness | controls: legal 3-space closer + plain live row | **[HEAD bytes]** both AGREE | both AGREE (unchanged) |
| C3 | freshness | totals | **[HEAD bytes]** `shapes=4 silent-false-pass=2 agree=2` | **LIVE** `shapes=4 silent-false-pass=0 agree=4` |
| C3 | freshness | source `FENCE_RE` | `^[ \t]*(`{3,}|~{3,})(.*)$` (`integrity:158`, `independent:109`) | **`^ {0,3}(`{3,}|~{3,})(.*)$`** (`integrity:165`, `independent:113`) — landed live |
| C3 | freshness | live stdout byte-invariance (both gates) | HEAD bytes: `c5eaf1a5…` / `4d911061…` | **live: byte-identical** (`cmp` clean) |
| C3 | freshness | self-test counts | 129 / 68 | **145 / 86** |
| gates | — | 8-instrument battery, dispatch state | ALL GREEN, floors `10/129/68/87/1597/62/104/97` EXACT | **after C3: `10/145/86/87/1597/62/104/…`**; at write time `compare_harness_independent` reads `117/117` with **9 self-test failures** (C1 mid-landing) → guard exit 1 |
| gates | — | nine `--self-test` runs, dispatch state | all rc=0 (`10 / 1597 / 109 / 129 / 68 / 87 / 62 / 104 / 97`) | live: 8 of 9 rc=0; `compare_harness_independent` **9 failures / 117** |
| box3 | — | doc §6 predicate-arm legs | 4 × `INCONCLUSIVE: opencode log not found` (`.ufo/round-39/drafts/p2/` pruned), block still exit 0 | **FIXED in-flight by seat W1** — legs now rebuild their inputs; re-run: 0 INCONCLUSIVE, exit 0 |
| box3 | — | doc §4/§6 blindness quotes | `harness_pin_residual_count=4`, `tree_files=338` | live re-run prints **5** and **340**; §4 was updated in-flight, §6's tail still carries 338/4 |

## Per-axis verdicts (scribe's reading; the landing-commit re-run is the authority)

- **depth (C1) — `[PENDING]`, and the before-state is *worse* than the r39 report records.**
  R1's F-2 reproduces in both forms; `m2` scores `24/24` with **strict `24/24`** and
  `adjudicated rows: 0` over a payload with zero derivation. The strict column — the red-team view —
  is *higher* for the copy payload (24/24) than for the honest one (20/24), because a copier's values
  agree exactly. F-3 reproduces on both `rows` and the `checks` dict. **At write time the fix was
  mid-landing and red** (`727ec676`: `IND_VALUE_KEYS` and `_record_list` unchanged; self-test
  `9 failure(s) over 117`, `FAILED: fixtures/rows-shadow`), so no `improved` is claimable here —
  and the integrator must re-run the probes against whatever comparator sha lands.
- **operability (C2) — `[PENDING]`.** Both of V3's residuals reproduce on copies of the **pinned**
  guard in version-matched worlds whose control is green: the absolute-argv copy/symlink override is
  silent-green (`PASS harness observed=129 floor=10`), and no path is ever checked against `--repo`
  (both-tables-agree outside absolute path, and a `../` traversal to an existing outside file, each
  read 8 × PASS exit 0). The arm's control (canonical path as argv → exit 2 `override repoint`)
  localizes the defect to the un-resolved argv path.
- **freshness (C3) — `[PENDING]` as a verdict, but the before/after pair is measured and clean.**
  On identical worlds with cmark 0.31.2 as oracle: HEAD bytes → 2 silent false-PASS (4-space, tab),
  2 controls agree; live bytes → **0 silent false-PASS**, both shapes flip to `rc=1 unindexed=1`
  fail-safe. Both gates' live stdout is byte-identical to the HEAD-byte run. Self-tests 129→145 and
  68→86, floors bumped in step. The verdict stays `[PENDING]` for the integrator to award at the
  landing commit; the evidence this seat contributes is the pair, not the score.
- **consistency / coverage / adjacency — held.** **calibration — improved in-flight but not clean:**
  the box-3 pointer defect this seat found (§6's four pruned-path legs behind an exit 0) was fixed
  by seat W1 during this seat; one stale quote (`tree_files=338`, `residual=4`) still survives in §6's
  tail against the live 340/5.
- **SHONEN — 4 × `[~]`, no `[x]`**; block at `drafts/b2/shonen-section.md`.

## Reproduce

```bash
cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
bash .ufo/round-40/drafts/b2/write-time-pin.sh   # box numbers, one shot

# C1. The driver recomputes a census probe against LIVE substrate, so a payload captured
# earlier can fail its own CONTROL as that substrate moves. c1-fresh.py captures IND+HAR and
# runs every arm in one process, so the battery shares one instant. B2_CMP selects the
# comparator: the pinned HEAD bytes (default) or verifiers/… for the live one.
python3 .ufo/round-40/drafts/b2/c1-fresh.py                                    # HEAD bytes: all four doors open
B2_CMP=verifiers/compare_harness_independent.py python3 .ufo/round-40/drafts/b2/c1-fresh.py  # live
python3 .ufo/round-40/drafts/b2/f23-probe.py     # the m1..m4 arms on a saved payload (same caveat)

python3 .ufo/round-40/drafts/b2/c2-arms.py       # C2 copy-variant + registry-vs-table (pinned)
python3 .ufo/round-40/drafts/b2/c2-confine.py    # C2 confinement arms (pinned)
python3 .ufo/round-40/drafts/b2/c3-pair.py       # C3 before/after pair, cmark oracle
bash .ufo/round-40/drafts/b2/s6-block-v2.sh      # box3 pointer: the doc's §6, verbatim
```
