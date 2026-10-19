# C1 adjudication protocol — source-blind harness re-derivation (round 37)

**Status:** draft artifact, owned by seat A1. To be landed (by the C1 integrator or
scribe) into `corpus/knowledge/harness-independent-round37.md` as that file's
§ Adjudications rules; section numbering below mirrors
`corpus/knowledge/independent-verification-round12.md` so the lineage is obvious.

**Authority:** r12's adjudication precedent (`independent-verification-round12.md`)
plus the round-37 claim C1 (``.ufo/round-37/claims.json``): *"disagreements are
adjudicated by a third seat and recorded, not smoothed"*. This protocol does not
modify the claim; it operationalizes that sentence.

---

## 0. Scope

Governs every disagreement or asymmetry the C1 comparison produces between

- **IND** — `verifiers/verify_harness_independent.py` (builder seats; blinded to
  `verify_harness_claims.py`, `baseline.json` harness rows, and corpus docs quoting
  them), and
- **HAR** — `verifiers/verify_harness_claims.py` (author instrument), and
- the **live substrate** (omp binary/db/sessions, opencode log/binary/roots),

on the 28 pinned checks, on the mutant tree's exit-1 naming set, and on the
instruments' self-tests. It does not govern ordinary review of the new instrument's
code, which follows the lane's normal critic path.

## 1. Roles and standing

| role | does | may not |
|---|---|---|
| builder (IND) | derives, freezes, compares, declares blindness | adjudicate any row about IND's own derivations |
| author (HAR) | defends the claim set; supplies HAR outputs | adjudicate rows about HAR's own checks |
| adjudicator | probes the substrate; rules each row | be a builder or author of either side; rule a row it authored a fix for |
| critic/reviewer | red-teams; a counter-probe re-opens a settled row | overwrite a ruling (supersede it, §8) |
| integrator | applies rulings, lands fixes/docs, runs the battery | silently drop a row |

The adjudicator **may read both sides' sources** when classifying — that is the
role — and must disclose per row which sources it read (§9 `blind:` field). What
stays blind is the *derivation act*, not the *adjudication act*.

## 2. Frozen comparison surface

The surface is the 28 ids in HAR's own live output (`--json`; an output channel,
not source). Mode partition, measured live at HEAD `041f6ba`
(`python3 .ufo/round-37/drafts/a1/agreement_predicates.py …/harness-live.json`
→ `ids=28 modes={'equal': 17, 'positive': 1, 'zero': 10}` `coverage: OK`):

| mode | n | agreement predicate |
|---|---:|---|
| equal | 17 | value equality IND == HAR-observed |
| zero | 10 | both readings empty (0 / [] / false / {}) |
| positive | 1 | inequality direction preserved (HAR-observed >= pinned); a "value disagreement" is not available for it |

`at_least` is referenced in HAR's evaluation dispatch but no id uses it — record it
in the ledger as a **latent mode**, so a fourth mode cannot enter the comparison
un-adjudicated.

Scope-sensitivity pre-registration (freeze first, rule later): every id whose name
selects a *population* (`offered`, `dangling`, `roots`, `dup`, `permission`,
`catalogue`) is scope-sensitive — a value difference there is D2 until a probe
proves otherwise (§4). Every id naming a *byte string or count* (`template_sha256`,
`template_bytes`, `db.rows`, `*_max`) is method-sensitive — a difference there is
D1 first. Pre-registration is the anti-smothing device: the classification cannot
be chosen after seeing which side looks better.

## 3. Disagreement taxonomy

Each row is built from a **four-number block**: `ind` (IND's derived value),
`har` (HAR live observed), `pin` (HAR pinned expect — ledger-only; builders never
see this file), `hand` (the adjudicator's own substrate probe). One row per
check id, per naming set, or per class-level finding.

| class | shape | ruling default |
|---|---|---|
| **D1** value mismatch, same population | ind ≠ har; hand probe decides | **real defect** on the side that misses the substrate |
| **D1a** representation/type mismatch | canon-strict inequality (1 ≠ True, 7 ≠ 7.0, list order significant) with the same population and equal meaning | **not definitional**: a defect on the side whose type misses the substrate's natural type for the id (count → int, flag → bool); fix the type, never widen the comparator |
| **D2** scope/definitional difference | both reproducible; different populations, same verdict | **definitional** — the id's spec sentence governs; record both scopes |
| **D3** claim/behaviour gap | docstring/claim says X, code does Y | **real defect even at delta 0** (latent failure mode; r12 §4a/§4b) |
| **D4** presence asymmetry | a quantity only one side publishes; invisible vs excluded-with-reason | **bookkeeping if the population is empty or delta 0 — but it MUST be named** (silence must not read as a pass; r12 adjudication 4); nonzero delta escalates to D1/D2 |
| **D5** cosmetic | key name, annotation text, extra counters whose sums reproduce | **cosmetic**; one recorded line, no action (r12 5–7) |
| **D6** shared property | both sides agree, and the spec says both are wrong | not a disagreement: a **finding** in §3b, with the detector that does notice + the safe invocation (r12 §3b (f)) |
| **D7** falsified premise | a mutant class / fault premise is wrong | **correction**; claim narrowed; predecessor wording judged "incomplete, not false" if so (r12 §3b (h)) |
| **U** unresolved | no probe decides within the cap | recorded with both readings + the discriminator that would settle it; **never averaged, never smoothed** |

## 4. The four tests that separate defect from definitional

Ordered; the first test that answers, rules.

- **A. Population identity.** Can each side reproduce its reading from the substrate
  by a stated command (its probe block)? If IND cannot produce a probe, its reading
  is not a disagreement — it is a drafting defect in IND, recorded as such.
- **B. Delta.** Do the two readings select different objects? Measure the delta on
  the live substrate. **Nonzero delta on an id whose spec sentence names that
  population ⇒ D1 defect.** Zero delta / empty population ⇒ D2 or D4, named.
- **C. Latent failure.** Does one reading have a future tree (or headless/edge state)
  where it hides or flips a class the check exists to detect? **Yes ⇒ D3 defect even
  with today's delta 0**; the fixture carries the proof because live effect is zero.
- **D. Naming/gating/annotation only.** Same population, different key name, gate
  set, wording, or extra counters? **⇒ D2/D5; no code change**; where the number is
  compared, state the exact scope (r12 §4c's baseline-note idiom).

## 5. Who wins — authority ordering

    hand substrate probe  >  the id's spec sentence  >  observed behaviour  >  key name / wording

- Neither instrument wins by authorship. The author instrument gets **no deference**
  — in r12 the author's script was the thing that had to agree, and the comparison
  forced two repairs to it (its quoted-context rule could not fire; its index census
  read more of `README.md` than its docstring claimed).
- A **spec ambiguity** (the id's scope genuinely underdetermined) is decided by the
  adjudicator and the decision is written forward — into the round doc always, and
  into the harness docstring/baseline note when cheap.
- A defect ruling names the **losing side and its exact line**, and lands with a
  **red-before fixture**; if the live delta was 0, the fixture is the whole proof.
- A definitional ruling **requires both scopes' probe blocks**. No probe block ⇒ §U,
  never a definitional label (this is the anti-relabelling rule).

## 6. Ruling procedure (bounded)

1. Build the four-number block for the row. If nothing disagrees, run test C only
   (the shared-blind-spot scan).
2. ≤ 2 substrate probes per row. Each probe is a command + raw output, saved under
   `.ufo/round-37/drafts/<adjudicator-seat>/`.
3. Apply §4's tests; assign exactly one class; write the ruling, action, and `blind:`.
4. If settled, mark `settled`; if not, §U with the discriminator named.

**Freeze-before-compare receipt** (new, owed to r12 §6's "authorship is attested,
not verifiable"): builders commit their derived values (`ind-values.json`) and its
sha256 **before** the comparison run, and record the comparison invocation (plain
stdout or `--json`) per run. HAR's `--json` output publishes pinned `expected`
values, so "source-blind" must cover the output channel: a builder that reads the
per-check table before freezing has contaminated its own derivation. The freeze
receipt is a *narrowing*, not a proof — the residue stays in §6-style honesty.

## 7. What gets recorded in `corpus/knowledge/harness-independent-round37.md`

Mirror r12's section map so the corpus reads as one lineage:

1. **§1 The claim** — the landed tree's raw agreement line: `N/28` + the per-mode
   breakdown + the adjudication count; disagreements are listed, never folded in.
2. **§2 Agreement, check for check** — the four-number table for the 28 ids (IND
   column + HAR column + agree flag); raw populations where they exist.
3. **§3 Adjudications** — one numbered row per D1–D5/U, **including zero-delta
   definitional differences**; each row: class, readings, probe command+output,
   ruling, action, `blind:`. A row without a probe is not a ruling.
4. **§3b Shared properties / mutant behaviour** — D6 findings + the mutant tree's
   naming set (expected-firing set decided by the mutant's author *before* the run;
   a mismatch between expected set and either instrument's naming set is itself an
   adjudicated row).
5. **§4 Repairs forced** — D1/D3/D7 outcomes: red-before fixture, landed diff,
   new self-test assertions, floors bump if counts moved.
6. **§5 Residuals** — §U rows; r12 §6 inheritance (agreement falsifies
   implementations, never specs; blindness attested-not-verified); which rows needed
   adjudicator source-reading.
7. **§6 Reproduce** — both instruments' commands, exit codes, counts in both
   directions (live tree AND the mutant tree), the freeze receipt shas.

## 8. Append-only and correction idiom

- Prior rounds' files keep their text; corrections to an earlier sentence live in
  the current round's doc, worded "incomplete, not false" when that is the truth
  (r12's (f) repair is the model).
- Ledger rows are never edited in place: a superseded ruling gets a new numbered
  erratum row citing the old one.
- Corrections to the *claim* itself (e.g. the mutant premise was wrong) are D7 and
  recorded as the round's own correction, not forced through.

## 9. Blindness — declaration and disclosure (ledger field `blind:`)

| value | meaning |
|---|---|
| `outputs-only` | row settled from both instruments' outputs + hand probe |
| `source-read(author)` | adjudicator additionally consulted HAR source/docstring to classify |
| `source-read(builder)` | adjudicator additionally consulted IND source |
| `none` | no probe possible (must then be §U, not a ruling) |

The builder's declaration to be signed verbatim in §5 of the report:
*"I did not open `verify_harness_claims.py`, `verifiers/baseline.json`, or any
corpus doc quoting them; my extractor is my own construction; my derived values
were frozen (sha256 recorded) before my first comparison run."* Keep r12 §6's
honesty tag: this is attested, and the only *evidence* of independence the corpus
can hold is structural — differing internals/bugs and the freeze receipt.

## 10. Retrodiction — r12's own rulings replay through this taxonomy

Validation that the taxonomy is the lane's own, not invented
(`independent-verification-round12.md` line cites; receipt:
`grep -n "^[0-9]\+\. \*\*\|^\*\*Shared property" …` → items at :77 :84 :90 :96
:101 :104 :106 :110, §3b at :118):

| r12 row (line) | class | ruling this protocol yields | matches r12? |
|---|---|---|---|
| 1 `commit_total` semantics (:77) | D2 | same population, different key name; baseline note states scope; no code change | yes |
| 2 counting-mode gating (:84) | D2 | different gate sets, same corpus verdict; both sentences true of different questions | yes |
| 3 index scan scope (:90) | D3 | claim/behaviour gap; 0-delta but latent ⇒ code scoped + fixtures | yes |
| 4 glob token invisible (:96) | D4 | bookkeeping (0 live) but named so silence ≠ pass | yes |
| 5 annotations (:101) | D5 | cosmetic | yes |
| 6 quoted-context bookkeeping (:104) | D5 | cosmetic | yes |
| 7 raw-candidate counters (:106) | D5 | cosmetic (sums reproduce) | yes |
| (f) pointer leaves grammar (:134) | D6 | shared property; safe invocation adopted (default mode) | yes |
| (h) premise false (:136) | D7 | correction recorded; claim narrowed | yes |

All nine replay. The taxonomy therefore contains no class the lane has not already
used and needed; C1 adds only the mode-aware predicate (§2) and the freeze receipt
(§6), both forced by the harness surface being *pinned values* rather than the
corpus's *verdict classes*.

## 11. Failure modes this protocol exists to prevent (all four are r12-measured)

1. **Smoothing** — a disagreement averaged or explained into a pass. Blocked by
   §7.1's raw `N/28 + adjudication count` and §8's erratum rows.
2. **Silence-as-pass** — an invisible check reading as agreement (r12 adjudication
   4). Blocked by D4's must-name rule.
3. **Post-hoc relabelling** — calling a defect "definitional" after seeing it.
   Blocked by §2 pre-registration and §5's no-probe-no-definitional rule.
4. **Hereditary unverifiability** — "we didn't look" as an unassailable claim.
   Bounded by §6's freeze receipt and §9's per-row disclosure; residue stated.

## 12. Comparator alignment (amendments, seat P4's driver landed mid-round)

`verifiers/compare_harness_independent.py` (seat P4; untracked at this draft's
write time) is the C1 join driver. Its discipline is read off its own docstring +
self-test output (`--self-test` → `0 failure(s) over 32 assertions`), and this
protocol adopts it, amending §2/§3/§6:

- **Headline join** = IND re-derived *expected* vs HAR live *observed* — the
  uncontaminated direction. **Secondary join** = IND vs HAR's *published* `expected`
  (the `--json` output channel) — adjudicator-facing only, **never the headline**
  (it is the pinned-value exposure §6 warns about).
- **Value keys** IND may publish: `expected | expected_value | re_derived | value |
  observed`, records keyed `check | id | name`. Any other shape is a loud error —
  so a shape mismatch is **D4/U before any N/28 is quoted**, never a silent pass.
- **canon()** is strict and type-tagged (1 ≠ True, 7 ≠ 7.0, list order significant,
  dict order insignificant) — hence the new **D1a** class above.
- **Uncovered / unknown ids ⇒ driver exit 2 naming them**; `--expect-n 28` fails the
  run if the live check set shrinks. An id present on one side only is therefore
  adjudicated (§3 D4) *before* agreement is reported; it can never fold into N/28.
- **Instrument-red guard**: a clean join over a red instrument exits 3 named — the
  protocol's §7.1 line must quote the driver's exit reason, not only its count.
- **Freeze receipt, executable**: capture IND with `--independent-json <file>`,
  record the file's sha256 in the builder's scout report, then join. The captured
  file predates the join; combined with the invocation record (§6) this is the
  strongest blindness evidence the corpus can hold short of source-level proof.