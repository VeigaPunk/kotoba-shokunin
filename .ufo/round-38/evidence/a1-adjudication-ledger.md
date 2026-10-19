# Adjudication ledger — round-37 C1 open rows (seat A1 witness, round 38)

**Authority:** `.ufo/round-37/evidence/a1-adjudication-protocol.md` (protocol §3 classes,
§4 four tests, §5 authority ordering, §9 `blind:`). Written by the r38 A1 witness, whose
standing is §1's **adjudicator**: it may read both sides' sources and must disclose per row.

**Freeze receipt:** `.ufo/round-38/drafts/a1/freeze-receipt.txt` — IND capture sha
`01fd40ef1939…`, HAR capture sha `f25e960303d3…`, instrument shas recorded before the join.

**Scope of this ledger:** the 5 rows the r37 comparator names as disagreements, plus the 6
rows it names as strict-unequal-but-adjudicated (the strict 17/28 column). It does not
re-adjudicate the 17 rows where both columns already agree.

---

## §1 Agreement line (unsmoothed, both pinned states)

The instruments changed sha 10+ times during this seat (see `final-state.txt`). Both ends
of the walk are quoted; nothing in between is a quotable state.

    AT DISPATCH (IND 27ae80ae…, CMP de2bd8ab…) — the state the round brief describes:
      IND agrees 23/28 (protocol) — strict 17/28 — adjudicated rows: 6
      disagreements: 5 — scoped out: 0 — exit 1

    AT SETTLE (IND 82ad9700…, CMP d37219bc…) — the state this ledger rules on:
      IND agrees 24/24 over the JOINED scope (28 live checks, 4 scoped out by name)
      protocol 24/24 — strict 19/24 — adjudicated rows: 5 — disagreements: 0 — exit 0

The denominator moved because the four `omp.catalogue.*` rows left the join by name
(adj-r38-04). A reader comparing the two lines must not read `24/24` as "28 rows now agree":
24 of 28 are joined, 4 are scoped out, and the strict column is 19/24.

---

## §3 Adjudications

### adj-r38-01 — `oc.log.skills_tag_hits`

```yaml
- row: adj-r38-01
  checks: [oc.log.skills_tag_hits]
  class: D1
  readings: {ind: 13, har: 0, pin: 0, hand: 0}
  probe: "python3 -c \"import pathlib;print((pathlib.Path.home()/'.local/share/opencode/log/opencode.log').read_text(errors='replace').count('<skills>'))\" -> 0 | python3 -c \"...sum(l.count('skills=\\\"') for l in t.splitlines())\" -> 13 | grep -c 'skills rescanned' -> 13 (saved drafts/a1/probe-four-number-blocks.txt)"
  ruling: defect(independent)
  authority: hand-substrate
  action: "verify_harness_independent.py:394 — count the literal '<skills>' the id names, or rename the id; red-before fixture drafts/a1/fixtures/oc-log-planted.log"
  blind: source-read(author)+source-read(builder)
  status: settled
```

The losing side and its exact line: `verifiers/verify_harness_independent.py:394`,
`sum(line.count('skills="') for line in lines)`. Its own docstring on the next line
concedes "the harness counts a `skills` tag" and then counts a different token.

**§4-C latent-failure proof (this is the deciding test, live delta notwithstanding):**
planting 3 literal `<skills>` lines into a copy of the live log moves HAR 0→3 (DRIFT)
while IND's number stays 13 — IND cannot detect the class the id exists to detect.
Evidence: `.ufo/round-38/drafts/a1/probe-latent-failure.txt`.

### adj-r38-02 — `oc.dup.roots_both_sided`

```yaml
- row: adj-r38-02
  checks: [oc.dup.roots_both_sided]
  class: D1
  readings: {ind: 3, har: 0, pin: 0, hand: 0}
  probe: "grep -c 'duplicate skill name' <log> -> 0 | grep -c 'existing=' -> 0 | grep -c 'duplicate=' -> 0 (drafts/a1/probe-four-number-blocks.txt)"
  ruling: defect(independent)
  authority: hand-substrate
  action: "verify_harness_independent.py:436 — parse the duplicate-root warning grammar; red-before fixture drafts/a1/fixtures/oc-log-planted2.log"
  blind: source-read(author)+source-read(builder)
  status: settled
```

Losing side: `verifiers/verify_harness_independent.py:436`, which counts skill names
appearing in more than one *rescan array* — a different population from the id's own
(duplicate-root warning lines, which number 0 on the live log).

**§4-C latent-failure proof:** planting 3 `duplicate skill name` lines spanning 2 shared
root keys moves HAR 0→2 (DRIFT, exactly its own `_root_key` rule) while IND stays 3.
Evidence: `.ufo/round-38/drafts/a1/probe-latent-failure-2.txt`.

### adj-r38-03 — `oc.log.init_count_monotone` (strict-unequal, adjudicated row)

```yaml
- row: adj-r38-03
  checks: [oc.log.init_count_monotone]
  class: D1
  readings: {ind: 0, har: [], pin: [], hand: []}
  probe: "planted copy with init counts 1,2,3 (strictly increasing): IND -> 1, HAR -> [] (drafts/a1/probe-latent-monotone.txt)"
  ruling: defect(independent)
  authority: hand-substrate
  action: "verify_harness_independent.py:388 — the predicate is 'count exceeds one', the id is 'monotone violations' (decreases); red-before fixture drafts/a1/fixtures/oc-log-monotone.log"
  blind: source-read(builder)
  status: settled
```

Live delta is 0 — the fixture is the whole proof (protocol §5: "if the live delta was 0,
the fixture is the whole proof"). This row is *not* a D1a representation row despite
`[]` vs `0`: the two readings are produced by different predicates, not by different
types for the same measurement.

### adj-r38-04 … adj-r38-07 — `omp.catalogue.*` (scoped OUT by name)

```yaml
- row: adj-r38-04
  checks: [omp.catalogue.found, omp.catalogue.total, omp.catalogue.matched, omp.catalogue.missing_names]
  class: D4 (presence asymmetry, nonzero delta) -> scoped OUT
  readings: {ind: null, har: "True / 7 / 7 / []", pin: "True / 7 / 7 / []", hand: rule-dependent}
  probe: "drafts/a1/probe-catalogue-spread.py -> 763 session files, 620 carry a '<skills>' block, 678 candidate blocks, 534 pass the harness's own gate; totals over 5 candidate selection rules = {2, 7} (saved probe-catalogue-spread.txt)"
  ruling: scoped-out-by-name
  authority: hand-substrate
  action: "corpus doc names all four ids as OUTSIDE the independent scope; the comparator's disagreement line is the honest state, not a defect to be fixed"
  blind: source-read(author)
  status: settled
```

The substrate **does** carry the surface (620 files, 534 qualifying blocks) — so this is
not D4's empty-population bookkeeping. It is stronger: the *value* is rule-dependent, and
the rule (newest ISO stamp among gated blocks, `min(10, len(known))` entry floor) lives at
`verifiers/verify_harness_claims.py:369-441` — inside the harness's own source, which the
blindness rule forbids IND to read. A rule-blind builder reproduces `2` under one plausible
rule and `7` under four others. Per protocol §5 (no-probe-no-definitional) this row *has*
probes, and per §7.2 the honest recording is a named scope-out, never a fold into N/28.

### adj-r38-08 … adj-r38-13 — the six D1a representation rows

```yaml
- row: adj-r38-08
  checks: [oc.dup.onesided_roots, oc.log.init_count_monotone, omp.descriptions.missing, omp.names.mismatches, oc.roots.plugins_cache]
  class: D1a
  readings: {ind: "0 / 0 / 0 / 0 / 0", har: "[] / [] / [] / [] / False"}
  probe: "drafts/a1/probe-four-number-blocks.py -> identity len(har)==ind on the four list rows; bool(ind)==har on plugins_cache (saved probe-four-number-blocks.txt)"
  ruling: definitional (representation) — named, not a defect
  authority: observed-behaviour
  action: "none; the comparator's zero-mode predicate already adjudicates them and they do not fail the run"
  blind: outputs-only
  status: settled
```

`oc.log.init_count_monotone` appears in this list in the comparator's `adjudicated_rows`
array; adj-r38-03 supersedes it for that id — the identity proof is real (len([])==0) but
the underlying predicates differ, so the D1a label alone would be the smoothing the
protocol exists to prevent. Recorded as an erratum to the comparator's own label, not as
an edit to it.

**Erratum adj-r38-14 (same class, discovered by this seat's own probe):**
`oc.roots.plugins_cache` — both sides read *different paths*. HAR
(`verify_harness_claims.py:511`) tests `HOME/.claude/plugins/cache`; IND
(`verify_harness_independent.py:463`) counts entries under `oc_config.parent.parent/
.cache/opencode`. Live: HAR path absent, IND path exists with 0 skill-bearing entries —
both read 0/False, so the row agrees by coincidence of two different populations, not by
agreement of one. Planting HAR's path (fake HOME + all substrate overrides) moves HAR to
`True` (DRIFT) while IND's number is computed elsewhere and cannot see it. This is a **D1
defect on both sides** (neither reading is the id's population) that the zero-mode
predicate has been silently passing. Evidence:
`.ufo/round-38/drafts/a1/probe-har-plugins-plant.txt`. Status: settled, no fix applied by
this seat (witness role).

---

## §5 Residuals

- **Blindness is attested, not proven** (r12 §6 inheritance). The freeze receipt narrows
  the output-channel leak (r37 A1-D1) but cannot prove a negative.
- **This ledger's own limit:** the adjudicator read both instruments' sources to classify
  (§9 disclosure per row). Per protocol §1 that is the role, not a violation — but it
  means these rulings are source-informed, and a reader who wants a source-blind
  reproduction has only the raw probes.
- **adj-r38-14 is unclosed.** Fixing it changes a row that currently reads as agreement,
  which would move the headline; that is the integrator's call, not the witness's.

## §6 Reproduce

    python3 verifiers/verify_harness_independent.py --json   # exit 0
    python3 verifiers/verify_harness_claims.py --json        # exit 0
    python3 verifiers/compare_harness_independent.py         # exit 1, 23/28, 5 disagreements
    python3 .ufo/round-38/drafts/a1/probe-four-number-blocks.py
    python3 .ufo/round-38/drafts/a1/probe-latent-failure.py
    python3 .ufo/round-38/drafts/a1/probe-catalogue-spread.py

The comparator line above reproduces the **dispatch state** and needs the instrument as it
was then (IND `27ae80ae…`). At the settle state (IND `82ad9700…`) the same command prints
`24/24`, `disagree: 0`, `exit 0`. Both states are pinned in `final-state.txt` and
`freeze-receipt.txt`; the drafts directory keeps the frozen captures the dispatch state was
computed from (`ind-freeze.json` sha `01fd40ef1939…`, `har-live.json` sha `f25e960303d3…`).
