verdict: PARTIAL — the two owned depth instruments are byte-identical at BASE and TIP and both self-tests hold exactly (330 and 104 assertions, exit 0); but the round-47 landing changed the *live* column they are joined against (`verify_harness_claims.py` OC_BIN), which adds a fourth disagreement to the comparator's live join (21/24 → 20/24) and the corpus still advertises the now-unreachable "live 24/24, exit 0".

Lane: KotobaR47-2.W2DepthNoHarm-2 (leaf; no subagents dispatched).
Target: `verifiers/compare_harness_independent.py` + `verifiers/verify_harness_independent.py` at
`7ad7fadfc09354b74fb66605dfb0c1182c115a2f` (TIP) vs `c61a973b2e02e1ded169703ddcb06466f4edd8bd` (BASE).
Scratch (canonical layout, symlinked siblings, `--no-hardlinks` clone):
`/fast/scratch/kotoba-r47/w2/W2DepthNoHarm/{kotoba-shokunin=7ad7fad, base=c61a973}`.
No tool installed or upgraded this lane (stock python3 + coreutils sufficed); no pacman
transaction was attempted; no `~/.local/bin/opencode` wrapper was executed (the npx ELF was
read as bytes only).

---

## 0. The axes, named

- **A1 freshness** — are the two owned instruments still the round-46 instrument? (byte identity + self-test counts)
- **A2 operability** — does the comparator's *live* join still run and still produce a verdict at TIP?
- **A3 calibration** — does the corpus record of this axis still match what the instruments do?

---

## 1. What round 47 actually touched (the no-harm surface)

`git diff c61a973 7ad7fad --stat` → 273 files, +46865/−359. For the two owned files and the
committed scope file:

```
verifiers/compare_harness_independent.py base=778b367e5e5f94fc tip=778b367e5e5f94fc same=YES
verifiers/verify_harness_independent.py  base=872993f875338f4f tip=872993f875338f4f same=YES
verifiers/harness-independent-scope.json  base=3d8500ed1757b6da tip=3d8500ed1757b6da same=YES
verifiers/verify_harness_claims.py       base=29e71b9a662e4aef tip=d9d9eb663f69cb36 same=NO
```

**The two owned instruments and the committed scope file are byte-identical at BASE and TIP.**
`verifiers/verify_harness_claims.py` (the *live* column the comparator joins against) is the one
that moved — 5 lines, of which the load-bearing one is:

- `verifiers/verify_harness_claims.py:56` — `OC_BIN = HOME / ".npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe"`
  (was `HOME / ".opencode/bin/opencode"`), plus the docstring line `:19`.
- `verifiers/baseline.json:12` gained `round47_note`; the `checks` block is unchanged.

Everything else round 47 touched (checklist `trigger.no_xml_tag`, `verify_surfaces.py`,
`verify_skill_checklist.py`, `corpus/*`, `SKILL.md`) is **outside** the two owned files and outside
the join's substrates.

---

## 2. A1 — freshness of the owned instruments: **HOLDS**

### 2.1 Self-tests at TIP (the acceptance)

```
cd /fast/scratch/kotoba-r47/w2/W2DepthNoHarm/kotoba-shokunin
python3 verifiers/compare_harness_independent.py --self-test   → EXIT 0
    "self-test: 0 failure(s) over 330 assertions"     (330 assertions, 0 failures)
python3 verifiers/verify_harness_independent.py --self-test    → EXIT 0
    "0 failure(s) over 104 assertions"                 (104 assertions, 0 failures)
```

The task brief's `(330, 104)` is confirmed **exactly** at TIP.

### 2.2 Self-tests at BASE (the no-harm control)

```
cd /fast/scratch/kotoba-r47/w2/W2DepthNoHarm/base/kotoba-shokunin
python3 verifiers/compare_harness_independent.py --self-test   → EXIT 0, 0 failure(s) over 330 assertions
python3 verifiers/verify_harness_independent.py --self-test    → EXIT 0, 0 failure(s) over 104 assertions
```

**330 = 330, 104 = 104, exit 0 = exit 0.** No drift, no assertion added or lost. Consistent with
the byte-identity in §1.

### 2.3 The floors guard agrees (and pins the counts)

```
cd /fast/scratch/kotoba-r47/w2/W2DepthNoHarm/kotoba-shokunin
python3 -B verifiers/check_assertion_floors.py   → EXIT 0
PASS harness_independent observed=104 floor=104
PASS compare_harness_independent observed=330 floor=330
PASS harness observed=10 floor=10
PASS corpus_integrity observed=150 floor=150
PASS corpus_independent observed=91 floor=91
PASS surfaces observed=99 floor=99
PASS checklist observed=1845 floor=1845
PASS pins observed=62 floor=62
PASS floors_guard observed=150 floor=150
```

`verifiers/floors-registry.json:9-11` (`compare_harness_independent`, floor 330) and the
`harness_independent` floor 104 are unchanged in the round-47 diff (`verifiers/floors-registry.json`
diff touches only `checklist` 1597→1845 and `surfaces` 87→99). The 330/104 floors are therefore
still exact, not lowered.

> Note for the record: an earlier invocation of the same command piped into `tail` returned
> `143`; that is SIGPIPE (141+2) from the closed pipe, not a floors failure. Re-run without the
> pipe: **EXIT 0**.

### 2.4 The independent instrument's 28 rows are byte-identical BASE → TIP

```
python3 verifiers/verify_harness_independent.py --json   (both clones)  → EXIT 0
independent rows differing base->tip: NONE (all 28 identical)
row count base/tip: 28 28
base statuses: ['DERIVED', 'SCOPED_OUT']
tip  statuses: ['DERIVED', 'SCOPED_OUT']
```

The 4 `SCOPED_OUT` rows and 24 `DERIVED` rows are the same set with the same values and the same
statuses at both commits. The source-blind re-derivation did not move.

**A1 verdict: HOLDS.** The owned depth instruments are unchanged and their self-models are green
at the exact recorded counts.

---

## 3. A2 — operability of the comparator's live join: **BROKEN at default resolution** (pre-existing), and **REGRESSED at TIP** once the probe race is removed

### 3.1 The live join does not run at default resolution (both BASE and TIP)

```
cd .../kotoba-shokunin        # TIP
python3 verifiers/compare_harness_independent.py --json --no-stamp   → EXIT 2
compare_harness_independent: ERROR: false blocker: scoped row omp.catalogue.found declares
observable {"candidate_blocks": 23854, ...} but recomputation gives {"candidate_blocks": 23871, ...};
(same for omp.catalogue.matched, omp.catalogue.missing_names)

cd .../base/kotoba-shokunin    # BASE
python3 verifiers/compare_harness_independent.py --json --no-stamp   → EXIT 2
compare_harness_independent: ERROR: false blocker: scoped row omp.catalogue.found declares
observable {"candidate_blocks": 24030, ...} but recomputation gives {"candidate_blocks": 24031, ...}
```

**This is a TOCTOU race, not a round-47 regression: BASE fails identically.** The committed scope
file pins the probe target to `$HOME/.omp/agent/sessions` (`verifiers/harness-independent-scope.json`,
`probe_contract.target`), and that tree is *live and growing* — 15,133 `*.jsonl` files, 14 GB — so
the independent instrument's census (`verifiers/verify_harness_independent.py:316` `catalogue_probe`,
memoised at `:338-339`) and the driver's own recomputation
(`verifiers/compare_harness_independent.py:939` `recompute_probe`, called at `:1147`) read the tree
at two different instants and disagree. The driver then fails closed at
`verifiers/compare_harness_independent.py:1151-1155`:

```python
if declared != recomputed["observable"]:
    problems.append(
        "false blocker: scoped row %s declares observable "
        "%s but recomputation gives %s" % (cid, show(declared), show(recomputed["observable"])))
```

Note the failure *mode* is arguably right (fail-closed, named) but the *class name* is wrong: the
blocker is not a "false blocker" (the declared observable was true when written); it is a
**stale-snapshot race** between two reads of a mutating tree. `verifiers/compare_harness_independent.py:1161-1165`
adds a third guard ("every blind-plausible rule agrees on one total → the row is derivable"), which
would also mis-fire here. Since the corpus and the SCORECARD depth row both advertise a *live*
join number, this race means the advertised live-join figure cannot be reproduced by a reader at
either commit without a frozen carrier.

**Repro (no-harm, BASE == TIP):** the two commands above. Base and tip both exit 2 with the same
error class and the same three row ids.

### 3.2 With the race removed (frozen carrier), the join runs — and TIP is **one row worse than BASE**

Because the probe race masks the join, I neutralised it the only way the instrument permits: point
both the independent instrument and the committed scope file at a frozen carrier. The scope file's
`probe_contract.target` was rewritten to a 2-file synthetic tree
(`W2DepthNoHarm.scope-frozen.json`; `a.jsonl` = 10 entries, newer mtime; `b.jsonl` = 3 entries,
older mtime → `distinct_totals` = {7,10}, non-vacuous, two rules disagreeing).

**TIP (7ad7fad):**
```
python3 verifiers/compare_harness_independent.py \
  --independent-cmd "python3 verifiers/verify_harness_independent.py --json --catalogue-carrier <frozen>" \
  --scope-file <scope-frozen.json> --no-stamp
→ EXIT 1
agreement: 20/24 (mode-aware protocol headline; 28 live checks, 4 scoped out by the independent instrument)
columns: protocol 20/24; strict 17/24; adjudicated rows: 4; un-adjudicated modes: 0
disagree: 4; uncovered: 0; unknown: 0; provisional: 0; scoped-out: 4
verdict: exit 1 — disagreements: oc.roots.names_plus_builtin (mode=equal: expected 10, observed 11),
  omp.cache.misses (mode=zero: expected 3, observed 3), omp.cache.verified_skills (mode=equal: expected 7, observed 10),
  omp.descriptions.unmodelled (mode=zero: expected 3, observed 0)
```

**BASE (c61a973), same frozen carrier:**
```
→ EXIT 1
agreement: 21/24 (mode-aware protocol headline; 28 live checks, 4 scoped out by the independent instrument)
columns: protocol 21/24; strict 18/24; adjudicated rows: 4; un-adjudicated modes: 0
disagree: 3; uncovered: 0; unknown: 0; provisional: 0; scoped-out: 4
verdict: exit 1 — disagreements: omp.cache.misses (mode=zero: expected 3, observed 3),
  omp.cache.verified_skills (mode=equal: expected 7, observed 10),
  omp.descriptions.unmodelled (mode=zero: expected 3, observed 0)
```

**The delta is exactly one row: `oc.roots.names_plus_builtin` (live 10 → 11).** All other 23
joined rows, the 4 scoped-out rows, the 4 adjudicated rows, the uncovered=0/unknown=0 shape and the
secondary join (14/24 at both) are identical.

### 3.3 Attribution: the new disagreement is caused *solely* by round 47's `OC_BIN` move

A 2×2 code×binary matrix isolates it. `verifiers/verify_harness_claims.py:477-479`:

```python
builtin = 0
if binary.is_file():
    builtin = 1 if b"customize-opencode" in binary.read_bytes() else 0
```
and `:504` `"roots_plus_builtin": len(names) + builtin`.

| live instrument code | `--oc-bin` | `oc.roots.names_plus_builtin` observed |
|---|---|---|
| BASE (c61a973) | default (dead `~/.opencode/bin/opencode`, absent) | **10** |
| BASE (c61a973) | forced to the npx ELF | **11** |
| TIP (7ad7fad) | forced to the dead BASE path | **10** |
| TIP (7ad7fad) | default (npx ELF) | **11** |

Measured:
```
# TIP live, --oc-bin forced to the BASE (nonexistent) path
observed= 10 expected= 7 verdict= DRIFT   builtin_names= 0
# BASE live, --oc-bin forced to the TIP npx path
observed= 11 expected= 7 verdict= DRIFT   builtin_names= 1
```

The npx ELF is byte-identical to the frozen snapshot and does carry the marker:
```
frozen 1.19.3 customize-opencode: 3
npx ELF customize-opencode: 3
same bytes: True
```

**Counterexample (the new disagreement is removable at TIP by reverting one constant):**
```
cd .../kotoba-shokunin   # TIP
python3 verifiers/compare_harness_independent.py \
  --live-cmd "python3 verifiers/verify_harness_claims.py --json --oc-bin /home/vgpnk/.opencode/bin/opencode" \
  --independent-cmd "python3 verifiers/verify_harness_independent.py --json --catalogue-carrier <frozen>" \
  --scope-file <scope-frozen.json> --no-stamp
→ EXIT 1
disagree: 3; ...  verdict: exit 1 — disagreements: omp.cache.misses, omp.cache.verified_skills,
  omp.descriptions.unmodelled
```
i.e. TIP with the BASE binary path reproduces BASE's 3-disagreement set exactly (21/24).

### 3.4 Why this is a *depth-axis* harm and not a wash

`verifiers/verify_harness_independent.py:611-618` derives `oc.roots.names_plus_builtin` as
`len(names)` over the skill roots and **declares the built-in term to be 0 by declaration**:

```python
rows.append(row("oc.roots.names_plus_builtin", len(names),
                "distinct skill names enumerated under the roots the "
                "opencode log names as sources ... plus the shared agents root (%d names); "
                "built-in names: 0 by declaration" % ...))
```

So the two columns now disagree on the same id for a *definitional* reason that only round 47
exposed: before, the live side read a dead path and silently reported `builtin_names=0`, which
*accidentally agreed* with the independent side's declared 0. Round 47 made the live side honest
(`builtin=1`) and thereby exposed that the independent instrument's `0 by declaration` is a
definitional choice, not a measurement. The wave-1 artifact already named this exact trap:

> `.ufo/waves/round-47/build/C1HarnessDriftRoot.md:63` — *"**`oc.roots.names_plus_builtin` at BASE = 10 is hollow.** The default `OC_BIN` is `~/.opencode/bin/opencode` (`verify_harness_claims.py:55`), which does not exist; `oc_observations` then reports `builtin_names=0` (`:478`) — "unreadable" silently becomes "absent". With the npx ELF ... the same run gives `builtin 1`, `roots_plus_builtin 11` ... Pinning 10 records the dead-path artifact; pin 11 with a resolver, or leave it unobservable and say so."*

and its recommendation (`:88`) was a `resolve_oc_bin()` helper plus a baseline re-record to 11.
**The landed tree took the first half (the honest `OC_BIN`) and not the second (the resolver /
re-record / independent-side adjudication).** The result is a live join that is one row redder than
BASE with no note in `LOG.md`, `SCORECARD.md` or `PROVINCE.md`.

### 3.5 The corpus record does not match what the instruments do

- `corpus/README.md:38` still advertises the round-37 result as present tense:
  *"**live 24/24 over the landed scope, exit 0**"*. At neither BASE nor TIP is the live join
  24/24 (BASE 21/24, TIP 20/24 with a frozen carrier; both exit 2 at default resolution). The
  "24/24, exit 0" was measured on 2026-10-19 against a **7-skill** host; the host now carries 10
  (`~/.agents/skills`: `create-toolset`, `unreal-mcp`, `unreal-skill` born 2026-10-20). This row
  was **not touched by round 47** — it is pre-existing staleness, but it is the row a reader lands
  on for this axis, and round 47's wave-1 explicitly flagged it (`build/C1HarnessDriftRoot.md:59`:
  *"oc.roots.names_plus_builtin 7 → 11 ... Pinning 10 records the dead-path artifact"*).
- `corpus/SOURCES.md:22` (S009) records the comparator's self-test as
  *"Final line 'self-test: 0 failure(s) over 328 assertions'; commit 78ee57e"* while its own
  "Supports" cell names *"the round-46 landing commit"*. Those are two different commits:
  `78ee57e` is an `origin/master` merge (2026-10-19 17:09) whose comparator prints **328**; the
  round-46 **landing** is `f2f9ee1` (2026-10-19 19:29, *"328->330"*), whose comparator prints
  **330**. Verified by running each tree:
  ```
  /tmp/s009  (78ee57e) → self-test: 0 failure(s) over 328 assertions   EXIT 0
  /tmp/r46   (f2f9ee1) → self-test: 0 failure(s) over 330 assertions   EXIT 0
  ```
  So S009's observation cell is measured at the wrong commit for its own claim cell. Round 47
  *appended* S012–S015 to this same table (`corpus/SOURCES.md:25-28`) and left the stale
  comparator row untouched — an in-round opportunity that was not taken. (S009 itself predates
  round 47; it was added at `f2f9ee1`.)

**A2 verdict: the two owned instruments are operable and their self-models are green
(§2); the *live join* is blocked at default resolution at both commits by a pre-existing TOCTOU
race (§3.1), and once that race is removed round 47 makes the join one row redder than BASE
(21/24 → 20/24) via a single constant move (§3.2–§3.4).**

---

## 4. A3 — calibration of the depth-axis record: **two rows overclaim**

| # | Severity | Where | Claim | Measured at TIP |
|---|---|---|---|---|
| C-1 | MED | `corpus/README.md:38` | "live 24/24 over the landed scope, exit 0" | 20/24 with frozen carrier (exit 1); exit 2 at default resolution. Never 24/24 at TIP or BASE. |
| C-2 | LOW–MED | `corpus/SOURCES.md:22` (S009) | comparator self-model "at the round-46 landing commit", observed line quotes "328 assertions" | landing `f2f9ee1` prints **330**; 328 is `78ee57e` (a pre-landing merge). Round 47 appended S012–S015 to this table and left S009 stale. |

Neither is *caused* by round 47; both are records this round had in hand (round 47 edited
`corpus/README.md` and `corpus/SOURCES.md`) and did not correct, and C-1 is the row a reader
lands on for the depth axis.

**A3 verdict: BROKEN on two rows.**

---

## 5. Summary table

| measurement | BASE c61a973 | TIP 7ad7fad | moved? |
|---|---|---|---|
| `compare_harness_independent.py` sha256 (16) | `778b367e5e5f94fc` | `778b367e5e5f94fc` | no |
| `verify_harness_independent.py` sha256 (16) | `872993f875338f4f` | `872993f875338f4f` | no |
| `harness-independent-scope.json` sha256 (16) | `3d8500ed1757b6da` | `3d8500ed1757b6da` | no |
| comparator `--self-test` | exit 0, **330** assertions, 0 failures | exit 0, **330** assertions, 0 failures | **no** |
| independent `--self-test` | exit 0, **104** assertions, 0 failures | exit 0, **104** assertions, 0 failures | **no** |
| independent `--json` rows | 28 (24 DERIVED + 4 SCOPED_OUT) | 28 (24 DERIVED + 4 SCOPED_OUT) | **no** |
| independent row values BASE→TIP | — | **all 28 identical** | no |
| floors guard | — | exit 0, 9/9 PASS (330 & 104 exact) | no |
| comparator live join, default resolution | **exit 2** (false blocker, 3 rows) | **exit 2** (false blocker, 3 rows) | no (pre-existing race) |
| comparator live join, frozen carrier | **21/24** protocol, strict 18/24, disagree 3, exit 1 | **20/24** protocol, strict 17/24, disagree 4, exit 1 | **YES −1 row** |
| new disagreement row | — | `oc.roots.names_plus_builtin` (live 11 vs indep 10) | **new** |
| live harness DRIFT id set | 7 ids (21/28 pass) | 7 ids, identical (21/28 pass) | no |

---

## 6. Counterexamples, with repro

1. **TIP join is one row redder than BASE, and the cause is one constant.**
   Repro: the two `--scope-file <scope-frozen.json>` runs in §3.2 (21/24 vs 20/24), then the
   2×2 matrix in §3.3, then the "force `--oc-bin` to the dead BASE path at TIP" run (back to 3
   disagreements / 21/24).
2. **The live join is not runnable at default resolution at either commit.**
   Repro: `python3 verifiers/compare_harness_independent.py --json --no-stamp` in each clone →
   exit 2, `false blocker: scoped row omp.catalogue.found declares observable
   {"candidate_blocks": 23854…} but recomputation gives {"candidate_blocks": 23871…}` (TIP) /
   `24030` vs `24031` (BASE).
3. **`corpus/README.md:38` "live 24/24, exit 0" is unreachable.**
   Repro: the frozen-carrier join at TIP → "agreement: 20/24 … verdict: exit 1".
4. **S009's comparator row measures the wrong commit for its own claim.**
   Repro: `git archive 78ee57e verifiers | tar -x -C /tmp/s009 && python3 /tmp/s009/verifiers/compare_harness_independent.py --self-test`
   → `328 assertions`; `git archive f2f9ee1 verifiers | tar -x -C /tmp/r46 && …` → `330 assertions`.
   The row's claim cell names the landing (`f2f9ee1`); the observation cell quotes `78ee57e`.

---

## 7. What I did NOT check (residual risk / verification gaps)

- **I did not run the comparator's live join at TIP with the *real* session carrier successfully** —
  it exits 2 (§3.1). All live-join numbers above use a **synthetic frozen carrier** and a
  **rewritten `probe_contract.target`**. That rewrite changes the scope file's committed contract,
  so my TIP/BASE join comparison is an *equivalence* measurement (same harness on both sides), not
  a re-derivation of the committed 24/24 claim. A reviewer should treat the 20/24 vs 21/24 delta as
  solid (the disputed row is isolated and reproduced by a 2×2) and the absolute numbers as
  carrier-dependent.
- **I did not verify the corpus/SOURCES contract's own rules** (row-count, schema, the "queued"
  column semantics) — I only checked whether S009's quoted observation matches the commit it
  names. Whether a stale observation in a `queued` row is a contract violation is
  `corpus/SOURCES-CONTRACT-v1.md`'s call, and I did not read that contract.
- **I did not check the `--receipt` freeze-before-compare path** at TIP with a real receipt, nor
  `--report`/`--json` markdown rendering against the landing receipt.
- **I did not check the `--freeze` / `--write-freeze` drift mode** of
  `verifiers/verify_harness_independent.py` against a committed freeze file (none is committed).
- **I did not run `verifiers/fault_injection_corpus.sh`** or the corpus integrity/independent
  gates — those belong to the C3 lane; I confirmed only that the two depth floors still hold.
- **I did not audit the opencode 1.19.3 loader lineage or the omp 18.12.5 callee allowlist**
  (`lq`/`Xl`/`Fo`); I only read the npx ELF's bytes to confirm the `customize-opencode` marker.
- **I did not re-derive the four `SCOPED_OUT` rows' probe *observables*** at the real carrier — the
  race in §3.1 prevented it, and the scope file's committed target is the live tree by design.
- **I did not execute the `~/.local/bin/opencode` npx wrapper** (per lane contract); the ELF was
  read as bytes only, and I never ran the binary.
- **I did not check whether other lanes' reports (`W2HarnessNoHarm.md`) already cover §3.3–§3.4.**
  I read `W2HarnessNoHarm.md` after forming my own findings; its F-1 covers the same
  `oc.roots.names_plus_builtin` observation change from the `verify_harness_claims.py` side, and my
  contribution is the **depth-axis consequence** (the join delta) plus the corpus-record rows, which
  that report does not cover. Our measurements agree.

---

## 8. Verdict in one line

**PARTIAL.** The two owned instruments are provably untouched (identical bytes; 330 and 104
assertions, exit 0 at both commits; floors exact), so nothing round 47 did broke them — but round
47 moved the live column they are joined against, which adds a fourth disagreement
(`oc.roots.names_plus_builtin`, live 11 vs independent 10 — a definitional mismatch the
independent side declares as `0 by declaration`) and drops the comparator's live join from 21/24 to
20/24, while `corpus/README.md:38` still advertises an unreachable "24/24, exit 0" and
`corpus/SOURCES.md:22` (S009) still attributes 328 assertions to a commit that is not the round-46
landing.

---

## 9. Artifacts

- `.ufo/waves/round-47/falsify/W2DepthNoHarm.captures.json` — base/tip live + independent row
  tables, and the two diffs (live: 1 row changed; independent: 0 rows changed).
- `.ufo/waves/round-47/falsify/W2DepthNoHarm.scope-frozen.json` — the scope-file variant with
  `probe_contract.target` pointed at the frozen carrier (the only mutation used to get past the
  TOCTOU race).

Scratch clone: `/fast/scratch/kotoba-r47/w2/W2DepthNoHarm/` (tip + base), left in place for
reproduction; helper `join_sim.py` there replays the comparator's join step on captured payloads.
