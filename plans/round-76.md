# Round 76 — plan (kotoba, hyaku run 10, attempt 1)

Date: 2026-10-27. Base: `b7f13f4b39cbd43076a85568adca763a6f674e7a` (r75 closure spot-check tip; lane clean, `ahead=0`).
Author: L1 `KotobaR76`. Two claims, distinct owned axes: **C1 depth (sourced)**, **C2 consistency (calibration sub-axis)**.
Lowest-axis obligation: owned axes are depth (9) and consistency (10) — depth is the lowest owned axis and C1 works it.

## Trigger

- r75 non-author closure (`corpus/lessons/round-75-verifier-spotcheck.md`) routed defects **R1–R4** to this round (§6).
- Carried check: the r74 closure routed **D1–D5** to round 75; r75's lesson carries no disposition and the r75 closure did not re-route them. Verified against committed bytes at base: D1 done in r75 (w2 dispatched); **D2 (d5aebcf never listed in LOG § Round 74), D3 (no forward pointer in `corpus/knowledge/sibling-overlap-census-round49.md`), D4 (`check_spec_craft`/`check_sibling_reread` absent from `verifiers/floors-registry.json`) are unworked**; D5 is conditional ("if a later freshness claim depends on the judged cells") and none does — recorded, not landed. D2–D4 land this round as disclosed hygiene repairs **outside C2's frozen counter scope**.
- `considerthese/2026-10-26.md` proposal 3 (land the r74-rejected description page and audit kotoba's own description against it; raised 10-24/10-25/10-26) is mined this round and is the motivation of C1. Proposals 1 (byte ceiling) and 2 (gate-registry move) are **not** taken: the 600-line box is a checklist-executed budget (changing it needs a baseline-map change and its own claim) and Q67 routes the registry home to an L0 question, not a round. Proposal 4 (falsify-wave gate) is procedure; proposal 5 (evidence budget) is operator-level. Reasons recorded in the round-76 lesson Gate.
- Assimilation (§10): **none this round.** The description-craft channel is covered by a direct in-round opening (S213); the staged package's `spec-description-trigger-discipline.md` rests on the same page and is refused as a staged artifact (re-grounded in-round instead, per CORPUS.md rule 1). Quarantine register rows for the lane slice are re-verdicted by a scout seat (unreachable/payload-absent families recorded; nothing appended from the staged package).

## Base battery (run at base `b7f13f4`, receipt `.ufo/waves/round-76/base-battery/base-battery.txt`)

corpus integrity exit 0; corpus independent exit 0; gate registry `60 of 60; phantom 0` exit 0; floors all PASS; checklist `pass 11` exit 0; `check_spec_craft` backed 3/3 exit 0; `check_sibling_reread` `20 of 20` exit 0. Census: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` exit 0, `kotoba ok` (151 rows; W04 duplicate-url warning set as at r75). SKILL.md 590 lines (budget 600).

## C1 — depth (sourced): description-craft guidance admitted and turned on the lane's own description

Motivation: considerthese 2026-10-26 item 3; the r75 Gate held description-eval guidance "pending a controlled held-out query experiment" and the r75 closure called that hold "stricter than precedent" — the r74 precedent (`corpus/knowledge/spec-skill-creation-craft-round74.md`, S223–S225) admits specification guide advice as documentary evidence with pinned snapshots and located quotes. This round admits the description-writing half of S213 (`https://agentskills.io/skill-creation/optimizing-descriptions.md`, opened r75, re-opened this round) at that same guide-advice level, acts on it in `SKILL.md`, and audits kotoba's own `description` against it. The eval-fidelity claims (should-trigger measurement) stay held — they are not part of this claim.

Frozen predicate (same sentence in plan, counter receipt label, and SCORECARD row):

> `python3 -B verifiers/check_desc_craft.py --rev <rev>` prints `description craft backed K of 6` and exits 0 only when all six conjuncts below hold at `<rev>`; at base `b7f13f4b39cbd43076a85568adca763a6f674e7a` it prints `description craft backed 0 of 6` and exits 1.

K=6 conjuncts (counter prints one verdict line each; a conjunct fails closed):
- (a) snapshot chain: `.ufo/waves/round-76/snapshots/` holds the optimizing-descriptions, evaluating-skills and best-practices page bytes; every digest appears in `snapshots/MANIFEST.sha256`, in `snapshots/fetch-record.json` with HTTP 200 records, and in the pinned digest table inside `verifiers/check_desc_craft.py`; the optimizing-descriptions digest equals the digest recorded in the S213 row's anchor update.
- (b) located quotes: `corpus/knowledge/description-craft-round76.md` carries ≥4 located quotes from the optimizing-descriptions snapshot, each ≤25 words, each occurring verbatim in the snapshot after the page's first heading, and each absent from the other two snapshots (page-unique, not site chrome).
- (c) act-on: `SKILL.md` carries a description-craft rule row in § Body craft citing `corpus/knowledge/description-craft-round76.md` and S213, containing at least two quote fragments that occur in the optimizing-descriptions snapshot.
- (d) self-audit: the entry carries an audit table whose measured values — rendered `description` length and first-sentence length of `SKILL.md` at `<rev>` — equal the values the counter recomputes from the measured revision's committed bytes (YAML folded-scalar render, whole block).
- (e) registry: row S213's `used-by` lists `corpus/knowledge/description-craft-round76.md`; the old→new change is logged in `corpus/lessons/round-76.md`.
- (f) provenance: the entry opens with `source:` (naming S213 and the URL), `verified-at:`, `recheck:`.

Counter requirements (Q25/Q26/Q48/Q70/Q71): `--self-test` drives `main()` on a satisfying fixture asserting the exact exit-0 line, plus must-fail arms (empty snapshot set; quote from the wrong page of the set; digest mismatch; audit values that disagree with the recomputed ones; missing used-by); the counter recomputes the audit numbers from bytes (a script-only world that reformats numbers can reach (d) — the headline therefore claims admission + backing + an audit table matching recomputed values only; the judgement that the page teaches these rules is assigned to named non-author attack seats and the closure).

## C2 — consistency (calibration sub-axis): r75-closure routed defects R1–R4 closed with committed corrections

Frozen predicate (same sentence in plan, counter receipt label, and SCORECARD row):

> `python3 -B verifiers/check_r75_routed_repairs.py --rev <rev>` prints `r75 routed repairs closed 4 of 4` and exits 0 only when all four repairs below hold at `<rev>`; at base `b7f13f4b39cbd43076a85568adca763a6f674e7a` it prints `r75 routed repairs closed 0 of 4` and exits 1.

Four repairs (counter checks content, not file presence):
- R1: `corpus/lessons/round-75.md` carries an appended correction naming the superseded M75-1 text and the Gate reject candidate, asserting the folded-render measurement of the r75-tip description (renders 1,022 characters; frontmatter block lines 4–18), citing `corpus/lessons/round-75-verifier-spotcheck.md`; AND receipt `.ufo/waves/round-76/receipts/r1-folded-render.txt` recomputes the render length from the measured revision's `SKILL.md` and prints 1022.
- R2: receipt `.ufo/waves/round-76/receipts/noharm-at-tip.txt` names the tip revision on its first line and carries stdout + exit codes of `verify_corpus_integrity.py --json` and `verify_corpus_independent.py --json` reading green; LOG § Round 75 cites the receipt path.
- R3: note `.ufo/waves/round-76/w2-registry-note.md` reconciles `.ufo/waves/round-75/w2-results.json` seat `R75Attack28` (named report absent; 63 of 64 report files) with a machine-checkable excerpt of the results entry; LOG § Round 75 cites the note path.
- R4: LOG § Round 75 carries an appended closing line recording the w2 settlement (64 seats, 0 dead, 63/64 reports, R75Attack28 phantom per R3) after the "w2 falsify results pending" text.

Counter requirements: `--self-test` with a must-fail arm per repair (receipt without the tip rev; correction paragraph naming no superseded text; note absent; closing line absent); a token-dump world (right filenames, forged/empty content) must fail; the counter recomputes R1's 1022 from bytes.

## Controls before data (Q37), committed at freeze

- C1-W1 fabricated: stub entry + empty snapshots → low count exit 1.
- C1-W2 real-text: entry whose quotes come from the held best-practices snapshot (real page bytes, wrong page) → page-unique arm rejects.
- C1-W3 token dump: entry naming all six conjuncts with no content → fails.
- C2-W1 token dump: repair files with forged values → fails.
Receipts under `.ufo/waves/round-76/receipts/` before any data commit; the frozen counters' bytes are hashed into the freeze receipt; no data lands before freeze.

## No-harm battery (Q65/Q72)

Base: all green (above). Post-state: re-run the same battery plus `check_gate_registry.py`, `check_assertion_floors.py`, `verify_skill_checklist.py --json`, census, and the SKILL.md line-budget check on a scratch tree holding the claim files before the report; receipt `.ufo/waves/round-76/receipts/noharm-at-tip.txt` names the final tip. Q73 sweep: `grep -n 'byte-identical\|differs from the base' verifiers/*.py` before freeze — the touched sections (SKILL.md § Body craft, § Gate registry, floors registry, lesson files, LOG append) are not pinned by any frozen counter at base; the one historical pin (`check_province_core.py` § Adjacent) is untouched.

## Wave shape

One v2 wave `w1` under policy v2 (band 64–128): **64 seats** — 30 build + 34 attack (attack share 53%: reviewer, critic, mutation-tester, labrat, sentinel, attack-simplifier seats). Roles route through the host table (never passed here): executor `@m_mim`; scribe/sonic/simplifier/revenger/labrat/sentinel `@m_flash`; critic/scout `@m_kfc`; reviewer `@m_zfl` (primary) with additional reviewer seats on `@m_kfc` per the run-10 map's kfc-heavy attack routing; mutation-tester `@m_zfl`; connector `@m_antigravity`. §3 L2 floor inside the wave: connector 1, executor 14, scribe 7, scout 4, reviewer 9, critic 6, mutation-tester 4, labrat 4, sentinel 2, revenger 2, simplifier 2, sonic 1. The L1 holds the canonical planner seat; a bounded planning data-walk rides `B01PlanConsistency` (executor).

## Touch list (lane repo)

New: `verifiers/check_desc_craft.py`, `verifiers/check_r75_routed_repairs.py`, `corpus/knowledge/description-craft-round76.md`, `.ufo/waves/round-76/**`, `plans/round-76.md`, `plans/round-76-addendum-1.md` (freeze corrections, if any).
Edited (append-only where filed): `SKILL.md` (§ Body craft row + § Gate registry rows, ≤600 lines — 590 at base), `verifiers/floors-registry.json` (+2 rows, bump-in-step with the guard's in-file tables), `verifiers/check_assertion_floors.py` (in-file tables + docstring, same change), `corpus/SOURCES.md` (S213 used-by cell only), `corpus/lessons/round-75.md` (appended correction), `corpus/lessons/round-76.md`, `corpus/QUALITY.md` (Q74), `corpus/README.md` (index row), `LOG.md` (round-75 closing line, round-74 d5aebcf line, round-76 entry), `SCORECARD.md` (round-76 annotation + planned).
Not touched: `verifiers/check_province_core.py` and its § Adjacent pin; `corpus/knowledge/sibling-overlap-census-round49.md` except the D3 forward-pointer append; `considerthese/` (read-only); the staged shokuknow package (read-only).

## Frontier step (§2b)

Census before: exit 0, 151 rows (receipt at base). S213 re-opened this round (fetch record + located quote in the round-76 Gate). Mistakes: M76-1 (folded-scalar block measured as frontmatter lines) → Q74; further rows from the wave. Sourced claim: C1 rests on S213. Assimilation: none (recorded). considerthese: proposal 3 mined; 1/2/4/5 declined with reasons.
