# Round 65 plan (kotoba, hyaku run 5, attempt 1 of the 02:24 relaunch)

Lane tip at plan: `c98d1378236bae56d9d2ecacd5db59a4cc142e1e` (clean, ahead=0; r64 close).
Base for all before-measurements: `c98d137` (the tip; before-values re-measured at
round start per Q19, never copied — all runs below executed 2026-10-24).

## Before-state (re-measured this round)

- `python3 -B verifiers/check_scoped_rules_v32.py --self-test` → exit 0,
  `self-test: 0 failure(s) over 223 assertions`, sha256 of the instrument
  `f8f69cada703c8d821690fe01539b433afb7e92e9cdf1752b3365745a7d1113d`
  (saved: `.ufo/waves/round-65/controls/C1-before.txt`).
- `python3 -B verifiers/verify_skill_checklist.py --json` → exit 1, 10 pass / 1 fail;
  the fail is `governance.citation_resolves` over three cells — `LOG.md:2533`
  `.ufo/reports/round-60/kotoba.md`, `LOG.md:2580` `.ufo/watchdog.log`,
  `SCORECARD.md:158` `.ufo/reports/round-60/kotota.md`-form bare fleet-relative
  tokens that do not resolve from the lane root (saved: `controls/C2-before.txt`).
- `python3 -B verifiers/check_assertion_floors.py` → exit 0, 14 of 14 (v32 not
  registered — the r62 F17 debt re-found by `RevC1Predicate` Q2).
- Census: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`
  → exit 0, 16 W04, 118 rows (`.ufo/waves/round-65/census-before.txt`).

## Claim C1 — depth (lowest owned axis; depth 9 below consistency 10)

**Surface moved:** `verifiers/check_scoped_rules_v32.py`'s `self_test()` pinning
suite and `verifiers/floors-registry.json` (+ the floors guard's two in-file
tables and docstring, bump-in-step).

**What lands** (all deferred from round 64, SCORECARD "Next: round 65" and lesson
row (f)/(p), wave-2 verified):
1. The six measured closing arms of `RevC1Predicate` §3 "Closing package",
   byte-exact as quoted there and re-measured by `MutW2M7M22` §4 (counts
   reproduce at 229 assertions; the quoted shas `f3c82574…`/`b614e8b1…` do NOT
   reproduce and are dropped — land the bytes, recompute the pin at landing).
2. The wrapper-level SM5 arm (the 7th arm, `pkg7`) — a component-level pin per
   the corrected E1.3/E3.3 disposition (`MutW2M7M22` §2b: SM5 is judge-equivalent;
   the pin stands as component-level, like the M12 arm).
3. Three NEW arms for the judge-level lanes the package leaves open
   (`MutW2M7M22` §5/§8):
   - SPAN_FIRST/SPAN_LAST (§8a, judge-level admission): a two-span cell whose
     first span is honest and second fabricated must still be rejected. Arm:
     "a fabricated second backticked span is rejected when an honest first span
     precedes it" (expected: rejected).
   - M20 (§5, judge-level over-rejection): a single-content-word backticked span
     whose only page support is a backticked occurrence must NOT be rejected.
     Arm: "a span word whose only page occurrence is inside backticks is not
     rejected" (expected: admitted).
   - M11-uppercase (§8b, judge-level over-rejection): a capitalised span word
     whose exact-case occurrence is on the page (and not on the cited line)
     must NOT be rejected. Arm: "a capitalised span word present on the page
     only as an exact-case token is not rejected" (expected: admitted).
4. A `floors-registry.json` row for `check_scoped_rules_v32.py` at the landed
   assertion count, with the guard's INSTRUMENTS + EXPECTED_INSTRUMENTS tables
   and docstring bumped in-step (F17 close: without the row the round-64 arms
   can be deleted with every gate green).

**Frozen counted predicate (the same sentence in plan, counter, receipt):**
`python3 -B verifiers/check_scoped_rules_v32.py --self-test` prints
`worlds reject 7 of 7; eligible rows pass 4 of 4` AND `survivors closed 6 of 6`
AND `self-test: 0 failure(s) over N assertions` with exit 0, where N is the
assertion count measured at landing; AND
`python3 -B verifiers/check_assertion_floors.py` exits 0 with the v32 row
registered at floor N; AND the kill conjunct holds — each of SM1–SM6, M7, M8,
M9, M10, M12, M17, M14, SPAN_FIRST, SPAN_LAST, M20, M11-upper exits 1 on the
landed bytes with a FAIL line attributed to its pin arm (SM4/SM6 attribution
per the R64-M9 rule: pre-existing `eligible world` / A2 cell arms respectively).

**Do-nothing control (§9):** v31 prints `survivors closed 5 of 6` over 201
assertions at the r64 tip (`.ufo/waves/round-64/controls/C1-before.txt` records
the 219-assertion predecessor; the 223 landed form cannot be reached without
the pinning content — padding alone cannot satisfy the kill conjunct, and a
padding-only patch is falsified by the kill battery). The honest-arm
requirement is enforced by the kill table: each named lane must die by its own
arm's label.

**Q28 freeze:** the receipt's pin is `(sha256, N)` recomputed from the landed
bytes at the measured rev; the predicate sentence above is frozen in this plan
before any after-measurement.

## Claim C2 — consistency (calibration sub-axis)

**Surface moved:** `verifiers/verify_skill_checklist.py`'s governance citation
machinery + three appended correction notices in LOG.md (append-only clean).

**What lands:** a recorded-correction excusal beside GOVERNANCE_ERRATA:
`GOVERNANCE_CORRECTIONS` — appended LOG.md lines of a strict shape (below the
existing horizon bound), each line-sha256-pinned, naming (file, line, token)
plus a corrected token that MUST resolve via `citation_resolve`; the check then
excuses the superseded subject. The three red cells are corrected by appended
LOG.md notices rewriting the tokens to the lane's documented fleet convention
`../.ufo/…` (the checker's own `citation_resolve` hops `..` against repo
ancestors — "the fleet's lane-report convention"). Self-test arms (each shown
able to fail): corrected-token-does-not-resolve; correction names no subject on
the named line; the named (line, token) is not actually red at HEAD; the
correction line's text drifted (sha mismatch); a correction that excuses a
never-red subject; the pre-existing GOVERNANCE_ERRATA absence-excusal still
works (regression arm); the 3 live corrections land and the check prints PASS.

**Frozen counted predicate:** `python3 -B verifiers/verify_skill_checklist.py
--json` prints `"fail": 0`, exit 0 (11/11) at the measured rev, with
`governance.citation_resolves` PASS — before: `"fail": 1`, exit 1 @ `c98d137`
(10/1). The checklist floor moves 1852 → M (bump-in-step: guard tables,
registry, docstring).

**Do-nothing control (§9):** appending the three LOG.md correction notices
WITHOUT the gate change leaves the check FAIL (the subjects are re-scanned from
the stale lines); changing the gate to excuse subjects named in ANY appended
line without the resolve/shape/sha guards fails the arms above. A do-nothing
run cannot reach 11/11 because the three base cells are genuinely red.

## Frontier step

- Census before → after (command above; before exit 0 saved).
- S121 opened this round: Madeyski, Orzeszyna, Torkar, Józala, "Overcoming the
  Equivalent Mutant Problem: A Systematic Literature Review and a Comparative
  Experiment of Second Order Mutation", IEEE TSE 40(1), 2014, author-hosted
  preprint v.2 PDF (opened 2026-10-24, HTTP 200, 1,126,684 B, sha256
  `bad1b681b1d6d6cea09f0c1e4701618b88dc175b713689c2a6ac43aba07418a3`,
  DOI 10.1109/TSE.2013.44 read from the PDF header; snapshot
  `.ufo/waves/round-65/snapshots/S121.pdf` + extracted text `S121.txt`).
  Gate quote (abstract, ≤25 words): "The experiment indicated that SOM in
  general and JudyDiffOp strategy in particular provide the best results".
  The plan's first candidate (arXiv:1309.4818) was opened and REJECTED — it is
  a mathematics paper (Carlson's ε-numbers); the row cites the artifact
  actually opened (M97 discipline, recorded in the search log).
- Sourced claim: C1's knowledge entry `corpus/knowledge/g7-span-closure-round65.md`
  cites S121 for the second-order (two-span) witness design + S120 for the
  pinning method.
- Mistakes: mined from this round's own runs into `corpus/lessons/round-65.md`.

## Round shape (accepted host mapping)

This seat holds NO dispatch tool (accepted host mapping, operator 2026-10-23):
the L1 executes the lane-scope work with its own tools and PREPARES the L2
waves under `.ufo/waves/round-65/` — spec + validator `plan` + rendered
`taskCall` payload per wave — itemized in the report's receipts; the
orchestrator dispatches prepared waves between rounds. Two v1 waves prepared
(build 32 + falsify 32, policy v1, band 32–64 each, together ≤128):
- W1 build (32 seats): source opening + row/entry drafting, C1 arm landing
  probes, C2 mechanism probes, tooling, first falsifiers. §3 L2 floor inside
  W1: connector 1, executor 3, scribe 1, scout 1, reviewer 1, critic 1
  (planner = L1, recorded).
- W2 falsify (32 seats, prepared against W1's output): reviewers/critics/
  mutation-testers/scouts re-run every counting command, attack each new arm,
  mutation-test the governance mechanism, re-open S121.
Executed this round by the L1 directly (all W1/W2 items as L1 work items, the
same content, self-verified with kill batteries); prepared waves itemized in
the report. Dead seats: none (no dispatch). Residual call: none.

## Commit order

plan freeze (this file + census-before + controls) → C1/C2 implementation +
receipts → lesson/SOURCES/knowledge + measurements → wave specs + report.
