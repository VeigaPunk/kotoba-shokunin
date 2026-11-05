# ReviewD1D5R87 — independent read-only re-check of C2's five items at 760e1c5

Seat: w3 reviewer, round 87 attempt 1 measurement lane. Treats the frozen
counter `verifiers/check_r86_routed_repairs.py` (sha256 `26daaa13`) as a
finding-source only — every item re-derived from committed bytes, never by
trusting the counter. The counter was mutating where it *reports* D5(iii);
int Experienced no committed byte of the lane is changed by this check.

Measured 2026-11-05 03:10-03:30 UTC. Lane tip verified FIRST:
`git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse master` →
`760e1c5edfdefb4767420f711d08f669952de013` (spec-named tip; matched).

## Result table

| item | verdict at tip | evidence (commands + observed) | delta vs round's after-receipt (5/5 at 35a395a9) |
|---|---|---|---|
| **D1** | PASS | blobs: `git rev-parse 760e1c5e:.ufo/waves/round-86/receipts/{tip-catalogue.txt,tip-registry.txt}` → `d910e20943704fe764b272197ced7af9235f23bc`, `71cacc1aee3034e7036ed3a01638c53cfc35952e` (both exist). Receipts name measured revision `9b040edb6c3fb129596e12d4e634bb2fb04ab067`, carry `exit=0` and the required lines (`omp catalogue lines reproduced 215 of 215`; `gate registry rows conformant 67 of 67`). Instruments byte-identical: `check_omp_catalogue_repro.py` = `7c233c8a85e4288d472a04c7d59734c172c605d4`, `check_gate_registry.py` = `95ffed389f483c3d6f93db3c08dcfdb9a2240576`, equal at `04647b0f` and tip. Independently: `9b040ed` resolves, is an ancestor of the tip (`merge-base --is-ancestor` rc 0), and carries the same instrument blobs → structurally the D1 the docstring describes. No trust in the counter bundled in. | none — D1 state unchanged (same PASS, no instrument drift) |
| **D2** | PASS | Lane mirror: `plans/round-87.md:116` `planner/distiller/labrat/Main are frozen-topology seats and can never be` + `:117` `swarm lanes.` → joined word sequence identical to the frozen sentence (this is the exact substring the counter asserts). Validator file: `/home/vgpnk/Projects/ufo-fsd-alpha/scripts/ufo-swarm-wave.mjs` (exists); `//`-comment mirror at lines 263-264: `planner/distiller/labrat/Main are` / `frozen-topology seats and can never be swarm lanes.` (line 264 is verbatim as a standalone line too). `SWARM_ROLES` set literal at :265 parsed literally: `["scout","reviewer","critic","connector","sentinel","executor","mutation-tester","revenger","simplifier","scribe"]` — 10 members, no `planner`. Independent agreement with the counter without using it. | none — unchanged |
| **D3** | PASS (5 rows, longest reason 52 words) | `corpus/lessons/round-87.md` `## Gate` (line 33) holds **5 reject rows** with ≥8-word reasons. Longest (52 words, matching the counter's count): "the quote is a config-directory constant that names no `plugins`, no `node_modules` and no `skills`; the round-86 closure's CF1 already found that no such quote can satisfy the dot rule, and the reader is `dir: Zo.join(R.path, \"skills\"),` — recorded in the new ledger's `reader_quote` cell, with the old quote kept only as `binary_quote`". All five quoted verbatim in Receipts § 1. | none — unchanged |
| **D4** | PASS (verbatim, 5 independent spots) | `plans/round-87.md` carries `after the first candidate score` verbatim at lines 152, 171, 199, 207, 217. Longest quoted context (line 171): `A counter, its ledger/fixture or its pins changed **after the first candidate score** kills that claim; an amendment committed **before** the first candidate score is an addendum...` — this is the frozen sentence plus its operative predicate (`kills that claim`), not a paraphrase. | none — unchanged |
| **D5(i)/(ii)** | PASS | blobs at tip equal blobs at base `223ae624`: `round-86-verifier-spotcheck.md` `ae3f49a3685e796ae5154cf9a4b055132a8c25b0`, `round-81.md` `315c0ec68075e9c7c4037b8f42617e3eee0a434b`. Verified by `git rev-parse` blob comparison directly. | none — unchanged |
| **D5(iii)** | **FAIL at tip, gate-side** | (a) `python3 -B verifiers/verify_corpus_integrity.py --json` (tip worktree) → exit 1, tally **7/9**, red set exactly `{corpus.pointers.commit_unresolvable}` (detail `corpus/lessons/round-81.md:8: 8b1cc1b00a9322cd8e231d87e015e1d75d20adc1`). `report_dead` reads **0**, its detail empty. (b) frozen counter at tip prints: `FAIL d5  verifiers/verify_corpus_integrity.py red set ['corpus.pointers.commit_unresolvable'], want exactly ['corpus.pointers.commit_unresolvable', 'corpus.pointers.report_dead']` then `r86 routed defects closed 4 of 5`, exit **1**. (c) frozen counter at the round's after-receipt `35a395a9aabfe2c849628bb4cfe9b25f176de411` prints: `could-not-evaluate: worktree tip d1c031833c37 != measured revision 35a395a9aabf (plans/round-87-addendum-1.md A1.2)` then exits **2** — reproduced in a dedicated `git clone --shared` bound to `35a395a9` (`rev-parse --show-toplevel` == that clone == worktree tip `d1c031833c37`, the CURRENT master, differs), so the refusal is the A1.2 pin, exactly as specified in addendum 1. | round's after-receipt was 5/5 PASS; now 4/5 FAIL on the same item — **corpus drift**, not instrument drift |

Closing line: **`C2 at tip: 4 of 5; defect class: work-regression`** — D1–D4
and D5(i)/(ii) hold unchanged; D5(iii) fails because the corpus's real state
differed from the counter's due-diligence expectation (`report_dead` healed to
0 by an external-file heal on `round-84/kama.md`). No counter or instrument
defect was found in five independent item re-implementations.

## D5(iii) conjunct analysis (from `check_d5`, counter lines 422-475)

`check_d5` returns PASS iff all of:
- **(i)+(ii)** blob of `corpus/lessons/round-86-verifier-spotcheck.md` == base
  `223ae624` AND blob of `corpus/lessons/round-81.md` == base. **At tip: PASS** (see table).
- **(iii-a)** worktree tip pin, else exit 2 (`could-not-evaluate`, per A1.2).
- **(iii-b)** `verify_corpus_integrity.py` (`--json`) exits 0 or 1 (else exit 2).
- **(iii-c)** parsed red set == exactly `{corpus.pointers.report_dead,
  corpus.pointers.commit_unresolvable}`. **At tip: FAIL** here — set is
  `{corpus.pointers.commit_unresolvable}`. Under the **frozen predicate** a
  red `report_dead` is required; its surprise absence is a measured
  *classification* of extra openness (an improved corpus), so the counter's
  answer is difference-of-object, not corruption.
- **(iii-d)** detail lists must name `…spotcheck.md:33` and `…round-81.md:8`
  respectively. Moot at tip (not reached; would pass — `commit_unresolvable_detail`
  does name the site).
- **(iii-e)** tally `7/9 checks pass`. Moot at tip (tally is 7/9 but (iii-c)
  already failed).
- **(iv)** lesson names both sites and states `left red and disclosed`. **At
  tip: PASS** (lesson carries both `file:line` strings verbatim).

**Each reading's producing conjunct, matched against the code path:**
- Old reading (5/5 at 35a395a9): conjunct (i)+(ii)+(iii-a-pinned)+(iii-c-two-reds-met)+(iv) all held.
- New reading (4/5 at tip): conjunct (i)+(ii) still hold, (iii-a) still holds
  (run at the actual tip), only **(iii-c)** fails because `report_dead` is no
  longer red — one conjunct, zero instrument change.

**Improvement or regression?** In the **corpus** — an **improvement that a
defect-classed as a work-regression by the frozen predicate**. The gate's own
honesty standard ("EXACTLY the two disclosed DRIFTs") is satisfied only when
the corpus still carries the two disclosed reds; healing one red
(`report_dead`) while the other stands means the round's frozen disclosure is
no longer the corpus's actual disclosure. The counter classifies this as a
defect in *the work under review* (`work-regression`), which is the honest
classification for an instrument whose job is to catch a record that no longer
matches its own claim. It is **not** a laundering upgrade (no D5(i)/(ii)-caught
rewrite occurred; blobs unchanged) — the healing came from an external file
(`round-84/kama.md`) landing in the worktree, which no lane predicate controls.

## Attack notes (what I tested and rejected)

- **D1 receipt identity/test-shape:** no manipulation of the counter's
  `_named_rev`/`carries` logic was needed — the receipts pass on the docstring's
  own mechanical reading (resolver, ancestor check, instrument-blob equality),
  all of which I reproduced independently. No cheat-shape or stale-receipt
  acceptance found.
- **D2 sentence:** no counter trust required; the exact word-sequence
  match is verified by eye against both carriers and the validator file
  itself (`//`-comment mirror at :263-264, set-literal :265-…, no `planner`).
  I confirmed the counter's regex is not grepping a coincidental substring —
  the SWARM_ROLES set literal is real, read directly from the file at
  `~/Projects/ufo-fsd-alpha/scripts/ufo-swarm-wave.mjs`.
- **D3 `_table`:** `_table` treats rows starting `|` as cells split on `|` —
  embedded `\\|` escapes are not the counter's concern here; all five reject
  rows are plain-text cells, no counter-side edge case affects the 52-word count.
- **D5(iii) `report_dead` "healed" via external file:** inspected
  `/home/vgpnk/Projects/shokunin/.ufo/reports/round-84/kama.md` (mtime
  2026-11-04 22:47, 2× `SHONEN` matches) and fleet commit `5b052020`
  ("round-84: kama report", 2026-11-04 12:15:30 -0300). This external actor's
  file healing the lane's `report_dead` red is outside the lane's own area of
  control — it is exactly the "same bytes, world-dependent verdict" instability
  the L1's `q79-control.txt` names. No edit was made by this seat in response.

## Residual risk and verification gaps

- The counter could not be evaluated at `35a395a9` (A1.2 pin), so the
  "delta vs after-receipt" column rests on my own item re-derivations plus the
  two committed after-receipts (`c2-after.txt`/`c2-final.txt` show 5/5 PASS at
  their time of record) *and* the fleet's fresh attempt-2 record
  (`d1c031833c37`, commit subject "…the C2 D5(iii) drift measured at the tip
  (healed by a fleet report)…") which converges with this seat's independent
  measurement. This is a documented closure state, not a verified number —
  hence the effort to independently re-derive every item here.
- Whether the unique causes of `report_dead`'s healing (the external kama.md
  file) or other future healing events could make D5(iii) permanently
  unsatisfiable is a **liveness risk for the frozen predicate**, not a
  counter defect — the frozen object is "the corpus still carries exactly the
  disclosed reds", and the validator fleet has already converged on naming it
  drift. No further action by this seat.
- Fleet tip moved during this check: `760e1c5edfde` → `d1c031833c37`
  (attempt-2 records + wave r87-w3 spec/dispatch). My item verdicts are pinned
  to the spec-named tip `760e1c5e`; a second-pass revision would need re-measure
  at the new master.

## Receipts under `w3/ReviewD1D5R87/`

1. `integrity-tip.json` — full `--json` capture of the gate at the tip.
2. Annotated quotations cited above (D1 blob ids, D2 word-sequence join, D3
   longest reason, D4 all five sites, D5 allergy sites) — no committed-byte
   edit was made to the lane; this report and the receipts dir are the only
   writes by this seat.
