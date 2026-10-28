# Kb81Y01Simplify — YAGNI audit of the r81 C1 repair stack (kotoba round 81, wave w1)

Seat: simplifier (leaf, no dispatch). Base `b284223105f4d106f7e8f56ed4fd296c643cda0e`; scratch
`/fast/scratch/hyaku/kotoba-r81/Kb81Y01Simplify` (removed at yield). No tool installs or upgrades were needed.

**What I audited, and when.** At seat start `.ufo/waves/round-81/build/` held no E01–E04 designs and the worktree
plan carried the earlier E6 revision (`LINE_CAP` 40→140, "estimated 60–120 added lines"). I measured the plan's
stack from its text. Mid-seat the reviewed patches landed (23:37–23:43), `receipts/freeze-shas.txt` was written,
and the plan was revised and committed (`e6d48e6`; worktree sha256 `d6bd43eb…`) to `LINE_CAP = 900` anchored on a
measured composed **+402/−29** (E01 +210/−10, E02 +170/−16). R1's identity *sentence* is unchanged between the two
revisions. Everything below is re-derived against the **frozen blobs** (E01 `bbee51f…`, E02 `5960294…`, E05
`eb00200…`), so it is a pre-data audit of the bytes the claim will ship.

Read: `plans/round-81.md`, both revisions; `Kb81E01Integrity.patch`, `Kb81E02Independent.patch`,
`Kb81E03ExtManifest{,-superseded}.txt`, `Kb81E04Baseline.patch`/`.md`, `Kb81E05Erratum.*`,
`receipts/freeze-shas.txt`; `verifiers/{verify_corpus_integrity,verify_corpus_independent,check_tip_battery,
check_gate_registry,check_report_pointers,check_sources_append_only,check_correction_sweep,verify_skill_checklist}.py`;
`corpus/SOURCES.md:171-172`; `corpus-baseline.json`; `floors-registry.json`; `scripts/sources-census.sh`; r80
`Kb80E04DeadPointer.patch`, `w1/Kb80E05GrammarFix.md`, `w1/Kb80Y01Simplify.md`, `w1/Kb80E15BaselineOrder.md`.

## 0. Headline

1. **The frozen implementation is right and the frozen sentence is wrong.** E01/E02 assert report identity only
   from report round **19** (`IDENTITY_FROM_ROUND = 19`); the plan's R1 sentence asserts it for *every* resolved
   report target ("path *or* object"). Measured on the real corpus: the sentence as written costs **10 new false
   positives** (`report_dead` 1→11); the floor costs **0**. E04Baseline's R10/R11 independently measured the same
   11-vs-0. Fix the **sentence**, not the blob — it is what the receipt label and the SCORECARD row will repeat.
2. **One real removal in the frozen bytes, already disclosed and correctly deferred:**
   `verifiers/verify_corpus_independent.py` defines `_committed_blob` **twice, consecutively** — the first
   definition is dead under Python's own binding rule (−7 added lines, zero behaviour change). E02 has it as
   residual R6; deleting it now would turn the tight pin into a certain `instrument-pin` FAIL, so route it to w2
   unless the L1 orders a repin with E05 (§2).
3. **The manifest is the only authority in the stack that no guard reads.** Proven with three battery runs: adding
   it leaves `guards 5 of 5`; **one pin line** turns widening into `FAIL guard instrument-pin`. E05's frozen pin
   table does not include it. The L1 **declined** the pin for this round as post-freeze scope ("changing to add a
   data-manifest pin is post-freeze scope … Record manifest-unpinned as an explicit residual/routed defect with the
   simplifier's controls"), so it ships as a **declared residual** with its landing shape retained — §3.
4. **The two gates implement the same binding with different strength** (E01: receipt must name the *repository*;
   E02: receipt must name the repository *and the hash*). Both satisfy the live record; they can disagree only
   under an adversarial manifest record. One condition in E01 closes it.

The three questions in my brief are answered in §5 (manifest vs per-line), §6 (`## SHONEN`+400 B minimality),
§7 (S250). The `+402` question is §8.

## 1. Identity: the sentence overclaims, the blob is correct (blocking, declaration-side)

Method, independent of the seats: in the scratch clone I replaced the base gate's `report_pointer_exists()` with
object resolution (`<rev>:<path>` via `git cat-file -e`, then `git show`, lane then fleet) **plus** each candidate
identity predicate on **both** arms, and ran the real gate over the base corpus bytes
(`verify_corpus_integrity.py --repo <clone> --no-baseline --json`). `report_total` is 111 for every variant, so the
delta is pure classification.

| variant | identity predicate | `report_dead` | new false positives |
|---|---|---|---|
| V0 | as-shipped base (no rev arm, no identity) | 1 | — |
| **V1** | **`## SHONEN` and ≥400 B, every target — the plan's sentence, verbatim** | **11** | **10** |
| V2 | `## SHONEN` only | 11 | 10 |
| V3 | ≥400 B only | 2 | 1 (`round-8`, 120 B) |
| V4 | one markdown heading + ≥64 B | 0 | 0 |
| V5 | ≥64 B only | 0 | 0 |
| V7 | ≥2 headings | 2 | 1 (`round-8`) |
| V9 | an H1 line (`^# `) + ≥64 B | 0 | 0 |
| **frozen E01/E02** | **`## SHONEN` and ≥400 B from report round 19** | **0** (measured, both gates) | **0** |

V1's ten sites are all real, committed, unquoted citations: `corpus/README.md:24,26,28,49`,
`corpus/knowledge/checklist-execution-round15.md:70`, `corpus/lessons/round-1.md:4`,
`round-1-aggregator-audit.md:9`, `round-4.md:4`, `round-5.md:4`, `round-8.md:5`,
`round-9-aggregator-corpus-verdict.md:24` (full list in `Kb81Y01-identity-variants.json`). Root cause: `## SHONEN` is
not a property of the report corpus — it is contractual only from the current prompt generation
(`.ufo/prompts/*.md:48`); fleet `round-1` (3365 B), `round-4`, `round-5`, `round-14` (9463 B) and `round-8`
(120 B, a respawn stub its own lesson documents as "120 B, a respawn") predate it. This is easy to miss because the
*lane's* `.ufo/reports` (rounds 20–45) all carry the marker while the gate resolves against the *fleet* root
(rounds 1–80). My first reading made exactly that mistake; the probe corrected it.

The frozen blobs **already fix this**, and their justification matches my measurement (`Kb81E01Integrity.patch`:
"`## SHONEN` is uniform from round 19 on (rounds 19-80 all carry it; rounds 1-17 predate it and round 8's 120 B
respawn marker is cited as a marker), so identity is asserted at round >= 19 and existence is all the gate
promises below it — measured, not a per-report judgment (Kb81E04Baseline R10/R11)"). E04's R10/R11 report the same
11-vs-0 and the same uniformity sweep (rounds 19–80, minimum 3166 B). Two independent methods, same numbers.

Measured, not inferred, for the frozen row of the table: applying **both** frozen patches to the base tree in the
scratch clone (`git apply` exit 0 each; a W2/W3-class *control* world, **not** the claim's after-value) gives, at
rev `e87d6c2`, `verify_corpus_integrity.py`: `report_total 111, report_dead 0, commit_total 46,
commit_unresolvable 0, commit_external 2, unindexed 1, tracked_files 155`, exit 1; and
`verify_corpus_independent.py`: the same `report_dead 0 / commit_unresolvable 0 / commit_external 2 / commit_total
46 / unindexed 1 / tracked_files 155`, exit 1. So the floor yields zero report false positives, both gates agree
class-for-class including E02's stricter receipt rule, and everything still red is exactly R4's territory.

**The defect that remains is the sentence.** R1 says: *"A resolved report target — path **or** object — must bind
report content identity: the resolved bytes contain `## SHONEN` and the file is ≥400 bytes."* Under the frozen bytes
that is false for rounds 1–17 (existence-only by design) — which is precisely the discrimination that makes the
repair shippable. **Ask (L1, pre-data, one sentence):** state the floor in the predicate sentence, e.g. *"a target of
report round ≥19 (where `## SHONEN` is uniform) must carry the marker and ≥400 bytes; earlier targets predate the
convention and stay existence-only."* This is a declaration edit, not guard logic; the kill rule's "no guard logic
edited" condition is untouched. If the sentence ships as written, a reviewer comparing it to E01 reads an
unimplemented conjunct and the claim's own text is falsifiable — on the **consistency** axis this claim owns.

Independent check of the boundary from the cited set (measured): cited targets with round ≥19 are 21, 23, 37, 45
(absent at the fleet root, so already excluded/quoted upstream — `report_pointers_excluded 8`, `quoted 2`) and
47–80 (all carry `## SHONEN`, ≥4377 B). No cited target falls in rounds 15–18. So floor 19 is safe with margin; the
floor is not knife-edge.

**Withdrawn, for the record:** my first frame recommended replacing `## SHONEN`+400 B with an H1+≥64 B shape test,
because the unscoped arm cost 10 false positives and H1+64 B cost 0. With the round floor, `## SHONEN`+400 B also
costs 0 *and* keeps the repo's own contract marker, so the replacement is not recommended. Forgery resistance is
symmetric either way (measured: a 430 B `## SHONEN` filler passes the marker test; a 429 B `# report` filler passes
the H1 test; the 7-byte marker and the real 594 B `.ufo/wapes` probe artifact fail both). Identity here promises
"this is a report-shaped document", not authenticity — see §9.

One zero-cost consistency note: both gates apply identity **unconditionally** to `<rev>:` tokens (E01's rev arm is
`always`; E02's `report_identity_ok` triggers when the first path segment carries `:`). Only one such token exists
today (`HEAD:.ufo/reports/round-77/kotoba.md`, round 77, 8547 B) and it passes. But a future lesson citing
`HEAD:.ufo/reports/round-5/kotoba.md` would red in both gates although the file is legitimate. The token text
already carries `round-N`, so applying the same floor to rev tokens is a condition change, not new code — optional,
and only worth doing if the L1 wants symmetry between the two arms.

## 2. The one removal in the frozen bytes: a duplicate `_committed_blob` in E02

`Kb81E02Independent.patch` adds `def _committed_blob(repo, rel)` **twice, consecutively** (patch lines 123 and 132,
two blank lines apart), with different bodies:

- first: `git ls-files --error-unmatch -- <rel>` gate, then `cat-file blob HEAD:<rel>`;
- second: `cat-file blob HEAD:<rel>` only, "working-tree bytes are no evidence".

Python binds the **last** definition, so the first is dead by the language's own rule — not by a grep. Behaviour is
unchanged by deleting it: `cat-file HEAD:<rel>` already fails for an untracked path, which is the only thing the
`ls-files` gate added. Cost: 7 added lines (def, docstring, 2 body lines, 3 blanks). Counts: `grep -c "def
_committed_blob"` → 2; E01 has no duplicated added def (every added name appears once).

**Disposition (after peer confirmation).** The E02 seat confirms the duplicate and has **already disclosed it** as
residual R6 in `w1/Kb81E02Independent.md` (independently raised by `Kb81C05Closure`), so "shipping it silently" is
not what is happening. Do **not** respin at freeze: the counter's `INSTRUMENT_PINS` tuple is tight
(`("edac0df…", "5960294…")`), so deleting the duplicate turns the measured tip into a certain `instrument-pin`
FAIL until E05 republishes and re-records the freeze sha — trading a guaranteed pin-red for a cosmetic dedupe
against the plan's own rule that a stale pin is the failure signal. **Route it to w2:** respin only on an explicit
L1 order, in which case the deletion is exactly the 7 lines above and E05 takes the new `(patch sha256,
post-image blob)` pair; the self-test should stay at 109 assertions / 0 failures. This is the same call for any
purely cosmetic cleanup found after the freeze: the pin is the instrument that must stay honest, not the prose.

## 3. The exemption manifest is the only authority no guard reads (unchanged by the landed stack)

Three commits in the scratch clone, three real battery runs
(`check_tip_battery.py --repo <clone> --rev <rev> --fleet /home/vgpnk/Projects/shokunin`, 107–113 s each):

| rev | world | result |
|---|---|---|
| A `fee99e0` | `verifiers/external-commits.json` added, one record, **no pin** | `guards 5 of 5; tip battery exit 0: 4 of 6` (the 4 is the base deficit) |
| B `b4c4a7d` | A + **one** `INSTRUMENT_PINS` line naming the manifest blob | `guards 5 of 5` |
| C `b7812b5` | B + a second, laundered record | `FAIL guard instrument-pin: verifiers/external-commits.json blob 56ce95a… is not a pinned blob`; `guards 4 of 5` |

Mechanism, from the guard code: `no-deletions` sees only *base* paths (a new file is invisible); `instrument-size`
diffs only the six `BATTERY` scripts (numstat over them for the added manifest was empty); `instrument-pin` iterates
`INSTRUMENT_PINS` keys — and the pin loop is BATTERY-independent, which rev B proves. The frozen pin table
(`freeze-shas.txt`) lists the two gates only; E05's patch adds exactly those two rows.

Why it matters here specifically: E01 binds a record via a receipt whose **declared sha256** is verified, so a
laundered record needs a same-revision receipt file — which any seat can write and fill the digest for. The result
is a fabricated hash classified `commit_external` instead of `commit_unresolvable` (**the W6 class**) with **no
guard firing**. E01's `external_binding` itself is tight — 40-hex exact, exactly one claim, `REPO_ID_RE`,
`SHA256_RE`, relative traversal-free receipt path, receipt read at HEAD, digest match — each condition closing a
named failure mode. Do not trim it. The gap is the manifest's own blob.

**Status: DECLINED for this round; recorded as an explicit residual.** The L1 ruled that adding a data-manifest pin
is post-freeze scope (E6's frozen line set allows exactly the two reviewed r81 gate instrument blobs) and directed
that manifest-unpinned be recorded as an explicit residual/routed defect carrying this seat's controls. I agree the
ruling is right on its own terms: the freeze exists so a claim cannot widen its own declared line set after the bytes
are pinned, and my probe is the reason the gap is *known*, not a licence to spend it. What ships: the frozen triple
untouched (patch `c15680f8…`, counter `1753b11c…`, pins `bbee51f2…`/`59602942…`), and
`build/Kb81E05Erratum.manifest-pin-variant.patch` **retained as a CONTROL, not a landable artifact** (sha256
`89932a03…` = the frozen erratum plus exactly one row, 28 added / 16 deleted vs the frozen 24/16), so a later round
can land the shape in one step. I verified it from primary bytes rather than relaying an id: applying
`Kb81E01Integrity.patch` (`6bbb304b…`) to `b2842231` and running `git hash-object verifiers/external-commits.json`
yields `402ac290baef66e19a4ac6bcc3b801e78ca5a035` (1176 B, 11 lines, sha256 `326fab4c…`) — an exact match.

What the residual actually costs, stated precisely so it is not over-read in either direction: (i) the attack the plan
names is unaffected — W6 (a lane-created commit masked with an `owner/repo@` marker and **not** in the manifest) still
reads `commit_unresolvable`, and W9 is enforced by *code*, not by the pin, because `external_binding` fails closed on
a missing or mismatched receipt digest; (ii) what stays open is **widening with an internally consistent record +
receipt pair**, which any seat can commit — visible in review as a one-file diff, invisible to all five guards; (iii)
the standing mitigation is comparison, not enforcement: the manifest blob `402ac290…` is recorded in
`build/Kb81E05Erratum.counter-sha256.txt`, so a later edit can be diffed against a recorded value by hand
(`git hash-object`). Route it as an r82 defect. Two notes that outlive this round: the counter's `--self-test` zeroes
`INSTRUMENT_PINS`, so it is silent on roster membership by construction and proves nothing about this gap — my
three-run live probe is the evidence; and I deliberately did **not** re-run the battery on the variant, since at this
point that would approach a claim after-value.

## 4. Cross-gate asymmetry in the binding (consistency axis)

- E01 requires `repository.encode() in proof` — the receipt must name the **repository**.
- E02 requires `sha in text and name.lower() in text` — the receipt must name the **hash and the repository**, and
  contradictory duplicates fail closed.

The plan's sentence is "the committed fetch/ls-remote receipt that proves the repo→hash association", so E02 is the
faithful implementation and E01 is weaker: a record whose receipt names the repo and a *different* hash classifies
`external` in E01 and `unresolvable` in E02 — the gates disagree, which is exactly what this claim's consistency
axis exists to prevent. Measured on the live record, there is no divergence: the single record's receipt
(`.ufo/waves/round-79/snapshots/S231.fetch.json`, 866 B, committed blob sha256
`e75f057a…` = the record's `receipt_sha256`) contains `mistralai/mistral-vibe` ×1 **and**
`7bb48f213ac677f943d5c791199ed3dddf302f00` ×1, so both rules bind it. **Ask:** add the one hash-membership
condition to E01 (1 line) — or narrow the plan sentence to "the receipt names the repository". The condition is
cheaper and matches the declared promise.

## 5. Is `external-commits.json` justified for one entry, versus a per-line verified-citation rule?

Yes. The live exemption surface is **2 lines / 1 hash** (`corpus/SOURCES.md:171` and `:172` both cite
`7bb48f213ac677f943d5c791199ed3dddf302f00`), so the manifest holds one record; a per-line rule would hold two
receipts for one fact. Structural reasons, all checkable:

1. **The 11-cell contract leaves no room for per-row evidence.** `sources-census.sh` E01 fails any row with
   `NF != 13` (11 columns). There is no receipt column, so a per-line rule must parse prose inside `anchor`/`teaches`
   — a validator for prose, not for evidence.
2. **Per-line is more code in the gate that must stay independent.** `verify_corpus_independent.py` has a
   `coverage_cells` parser for `corpus/README.md` only; it has no SOURCES row parser. Per-line structured evidence
   means a SOURCES table parser in **both** gates, versus `json.loads` + membership. The frozen binding is ~30
   lines per gate and strongly checked; per-line would add a parser on top.
3. **Closure is the whole property.** "Absent from the manifest → red" is what W6 tests. Per-line is open by
   construction: a new citation line carrying a marker plus a receipt exempts itself, which is the laundering the
   r80 class was killed for.
4. **Two independent implementations, one shared evidence file.** Both gates read the manifest and verify it
   independently, so agreement across gates remains meaningful evidence (they do not share code; the manifest is
   data). Duplicating a hand-maintained allowlist in both files is the drift that `verify_corpus_independent.py`'s
   contract ("own tokenizer, own counting code … does not import, read or copy") exists to prevent.

Keep the schema minimal and refuse to generalise it: `{hash, repository, receipt, receipt_sha256}` per record, one
record today, no wildcards, no repo-level/class-level records, no free-text `reason`. W9's "record with no
committed receipt proof → red" stays.

## 6. Is `## SHONEN` + 400 B the minimal sufficient identity?

Inside the frozen round floor, **yes** — and the floor is the part that makes it sufficient. Measured against the
marker class with real bytes (in-process, same two arms):

| world | bytes | `## SHONEN`+400 B | H1+64 B |
|---|---|---|---|
| seven-byte marker (the r80 W10 class) | 7 | dead | dead |
| the repo's real `.ufo/wapes` probe artifact | 594 | dead | dead |
| real fleet `round-76/kotoba.md` | 8128 | alive | alive |
| real fleet `round-8` (cited, 120 B) | 120 | dead **if unscoped** | alive |
| forged 430 B `## SHONEN` filler | 430 | **alive (bypass)** | dead |
| forged 429 B `# report` filler | 429 | dead | **alive (bypass)** |

Two conditions (one substring, one integer) buy exactly what a simpler content check buys; a "simpler check" is
available (an H1 line) but it is defeated by a two-line forgery of *its* mark just as the marker is defeated by a
two-line `## SHONEN`, while losing the repo's contractual section. So: **keep `## SHONEN` + 400 B, keep the round
floor, fix the sentence (§1)**. The 400 B number should be read against the corpus, not as a magic constant: the
smallest report at round ≥19 is 3166 B (E04 R11), so 400 is a floor at ~13 % of the smallest genuine document —
generous, and it kills every marker-sized file.

## 7. Is S250 needed for green?

**No — and it is not redundancy either.** Sweep (`grep -c supersed`): `verify_corpus_integrity` 0,
`verify_corpus_independent` 0, `check_tip_battery` 0, `check_gate_registry` 0, `check_assertion_floors` 0,
`check_correction_sweep` 2 (docstring only), `verify_skill_checklist` 3 — and those three are its
**LOG.md/SCORECARD.md** governance-correction registry (`GOVERNANCE_FILES = ("LOG.md", "SCORECARD.md")`), not
SOURCES. `check_sources_append_only.py` reports changes to the three permitted cells and never requires a
correction row; `check_correction_sweep.py`'s `REGISTRY` is a hardcoded tuple list, not derived from SOURCES. So no
gate reds whether S250 exists or not. It is also not in the landed stack — `Kb81E04Baseline.patch` touches only
`.ufo/waves/round-81/dispositions/wapes.txt` (R3, landed) and `corpus/README.md`; no patch touches
`corpus/SOURCES.md`.

Keep it as the rule-2 / Q21 audit row: the manifest decides *classification legality*, S250 records *provenance
correction* (`7bb48f21…` resolves in `mistralai/mistral-vibe`, not `badlogic/pi-mono`; S230 stays append-only). It
follows the repo's existing correction precedent (the checklist's "appended, byte-pinned notice naming the stale and
corrected tokens"), so no new convention. Three operability traps for the seat that writes it, each a gate exit:
kind must come from `spec|docs|paper|code|tool|dataset|talk|book|community|own-work` (no `correction` → E05);
`used-by` must name an existing path (E11) or be `—` (W03 warning, exit 0); and write the hash **without** the
`commit` keyword (or rely on the single manifest record) so it does not add a third citation site — then refresh the
baseline last (R4).

R3 (`.ufo/wapes`) is likewise non-load-bearing: `grep -rl wapes verifiers/ scripts/` → 0, and it is untracked, so no
gate can read it. It has landed as a disposition; keep it as housekeeping, not as part of reaching `6 of 6`.

## 8. Is +402 lines the minimal sufficient instrument delta? (mostly yes; one removal, one note)

Measured split of the frozen patches (added lines, arms = from the first hunk whose context is `def self_test`):

| patch | added | new data | production/doc | red-before arms |
|---|---|---|---|---|
| `Kb81E01Integrity.patch` | 221 | 11 (the manifest) | 122 | 88 (39 %) |
| `Kb81E02Independent.patch` | 170 | — | 145 | 25 (15 %) |
| total | 391 instrument | | 267 | 113 (29 %) |

Verdict: **defensible in kind.** The growth over r80's 59 lines for the same two gates is attributable to the
strengthened predicate (object resolution, round-scoped identity, receipt-digest binding, fail-closed duplicate
handling, ten new class arms), not to generalisation — E01's binding is 30 lines of conditions each of which closes a
named failure mode, and E02 re-implements it independently (required, not duplication). The arms are 29 % and are the
plan's own conjunct ("with its red-before regression arm"), so I recommend no arm removal. Removals I did find are
§2 (7 lines, routed to w2 rather than respun) plus the `.git` parents-walk below.

**`.git` walk in E01's rev arm (2–3 lines).** E01 keeps
`lane = next((p for p in (at, *at.parents) if (p / ".git").exists()), None)` and then `[lane] if lane else [] +
[fleet_root]`. It is subsumed: `git -C <subdir>` resolves the repository upward itself — measured
`git -C <clone>/corpus cat-file -e HEAD:README.md` exits 0 and `rev-parse --show-toplevel` returns the clone root.
E02's independent implementation already shows the leaner form (it is handed `repo` and calls `git -C repo`), so
deleting the walk also removes a gratuitous divergence between the two gates. My probe used `(base, fleet_root)`
directly and reproduced the intended verdict, including repairing the sole dead pointer from the fleet hop.

**On `LINE_CAP = 900`:** my earlier objection (the ticket summary and the first plan revision said 140 with no
measured basis) no longer applies — the frozen revision anchors the cap on the measured +402/−29, leaving 498
headroom, and the plan correctly states the pin carries the anti-laundering load with the cap as the outer bound.
Because the pin rows are tight (base blob + exactly one reviewed r81 blob per gate), the headroom is acceptable.
The one thing the headroom does *not* cover is §3: the unpinned exemption manifest, not the cap, is the soft
surface, so the later-round fix is to pin it (§3, declined for this round) rather than to tighten the cap now.

## 9. Named limits and residuals (not repaired here)

- **Manifest unpinned — declined this round, routed to r82.** `verifiers/external-commits.json` is the only input in
  the stack that no guard reads; widening it with an internally consistent record + receipt pair is review-visible
  but guard-invisible (§3, three-run probe). The L1 declined the pin as post-freeze scope and directed it be recorded
  as an explicit residual; the frozen triple is untouched, the landing shape is retained as
  `build/Kb81E05Erratum.manifest-pin-variant.patch`, and the recorded blob `402ac290…` in
  `build/Kb81E05Erratum.counter-sha256.txt` lets a later edit be compared by hand.

- **Identity is report-shape, not authenticity.** A forged `## SHONEN` + ≥400 B document (430 B measured) passes. The
  arm's promise is "a substituted marker reads dead", which it keeps for the seven-byte marker and the real 594 B
  probe artifact. Do not add anti-forgery conjuncts; that is over-building.
- **Manifest + receipt is review-time evidence.** A record plus a same-revision fabricated receipt passes W9's
  "committed receipt proof". The pin (§3) makes any *widening* visible; it does not authenticate provenance.
- **Sibling authority with weaker semantics:** `check_report_pointers.py` (the Q68 no-harm gate) resolves report
  targets by tree/blob existence only and passes a seven-byte marker today (its `check_report` counts blob
  existence). It is not one of the six battery gates and not part of C1's predicate; closing the W8 class there is a
  ~3-line change with no E6 amendment, but it is out of this claim's declared repair set. Named, not repaired.
- **Identity coverage is round-shaped report paths.** E01 applies the floor only when
  `round-(\d+)/` matches the token, so a non-round `.ufo/reports/<name>.md` target would be existence-only. No such
  target exists today (all 51 distinct cited targets are round-shaped — measured).
- **I did not measure the integrated tree, the C2 counter, or any after-value.** The clone was restored
  byte-identically (`sha256(clone verify_corpus_integrity.py) == sha256(lane …)` → True, `git status --porcelain`
  empty). One receipt was withdrawn: probe C run 1 invoked the lane counter instead of the clone's, so it never
  exercised the pin; that file is deleted and the retained `Kb81Y01-probeC-laundering.txt` is the clone-counter run.

VERDICT: The frozen stack is close to minimal and should ship with one pre-data edit, one routed cleanup and one declared residual — state the round-19 identity floor in the R1 sentence (the blob is right; the sentence as written measures 10 false positives against 0 for the floor, corroborated independently by E04 R10/R11 and by my control world where both gates read report_dead 0 / commit_unresolvable 0 / commit_external 2), add the hash-membership condition E01 lacks so both gates implement the plan's repo→hash promise, and record manifest-unpinned as the explicit residual the L1 directed (widening with a consistent record+receipt pair stays review-visible only, while W6 still reds and W9 is code-enforced by `external_binding` failing closed; blob 402ac290… verified here from primary bytes, landing shape retained as build/Kb81E05Erratum.manifest-pin-variant.patch, mitigation is comparison against Kb81E05Erratum.counter-sha256.txt); E02's shadowed duplicate `_committed_blob` (its residual R6, −7 lines, zero behaviour change) is routed to w2 rather than respun at freeze because the tight pin would turn a unilateral dedupe into a certain `instrument-pin` red; the one-entry manifest is justified (the 11-cell SOURCES contract, the independent gate's missing parser, closure, and shared evidence with independent readers), `## SHONEN`+400 B is minimal *given* the floor, and S250 is not a predicate conjunct (swept: no battery gate reads SOURCES supersessions) yet belongs as the rule-2 audit row.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81Y01Simplify.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81Y01-receipts.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81Y01-identity-variants.json, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81Y01-control-R1R2-corpus-gates.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81Y01-probeA-manifest-unpinned.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81Y01-probeB-manifest-pinned.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81Y01-probeC-laundering.txt
