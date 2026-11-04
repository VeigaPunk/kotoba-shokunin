# ReviewerC1 — independent C1 attack

Axes: predicate identity, control non-vacuity, rendered-prefix fidelity. Recommendation only; no admission or production edits.

## Findings (severity ordered)

### High — frozen R6 admits a vacuous evaluation set

`plans/round-85.md` § C1 R6 counts rows, not distinct queries. Nine copies of one indirect positive meet both the positive count and the ≥5 indirect-positive floor. With nine negatives satisfying the stated overlap test, the independent oracle reports R6 GREEN (`pos 9 neg 9 indirect 9`). With candidate description and a synthetic structurally qualifying R8 entry, this world scores **8/8**. Inputs: `dup_fixture.tsv`, `candidate.SKILL.md`, `valid_entry.md`; output: `oracle-receipt.txt`, Table B W5. The entry is synthetic test data, NOT an opened-source receipt.

### Medium — R6's lexical near-miss proxy admits irrelevant negatives

Nine irrelevant negatives (haiku, chess, Tetris, birth-date form, etc.) each retain a generic shared token such as `write`, `skill`, or `prompt`. All pass the exact ≥4-character word-overlap rule. Table B W6 scores **8/8**. Input: `irr_fixture.tsv`. This is a weakness of the frozen predicate, not evidence that a not-yet-available counter has deviated from it.

### Medium — R1's literal terminator recognizes abbreviation dots

The attacked description starts `Use this skill when auditing e.g. skill files or prompts whose activation boundaries and listing descriptions require careful restructuring for more reliable discovery.` The literal first `.` followed by space is after `e.g.`: R1 measures 33 characters, though the actual opening sentence extends beyond the 99-character listing prefix. With qualifying auxiliary inputs, Table B W7 scores **8/8**. Input: `eg.SKILL.md`. This follows the plan's explicit period rule; it is not a proposed counter repair.

## Seven-world oracle verdicts

G=green, R=red; positions are R1 through R8. Actual-tree auxiliary files were absent at observation. W5/W6 explicitly substitute their attacked fixtures. Claim-ready column uses the saved synthetic `valid_entry.md` and `valid_fixture.tsv` except where a fixture is attacked. These are hypothetical oracle worlds, not production counter successes.

| World | Actual-tree R1…R8 | Actual total | Claim-ready R1…R8 | Claim-ready total |
|---|---|---:|---|---:|
| Base committed bytes | R G G R G R G R | 4/8 | R G G R G G G G | 6/8 |
| Plan candidate | G G G G G R G R | 6/8 | G G G G G G G G | 8/8 |
| Base cut to 99 characters | G G G R R R G R | 4/8 | G G G R R R G G | 5/8 |
| Trigger/lane token dump, no ownership clauses | G G G R R R G R | 4/8 | G G G R R R G G | 5/8 |
| Nine identical positives | G G G G G G G R | 7/8 | G G G G G G G G | 8/8 |
| Irrelevant negatives with incidental overlap | G G G G G G G R | 7/8 | G G G G G G G G | 8/8 |
| `e.g.` abbreviation description | G G G G G R G R | 6/8 | G G G G G G G G | 8/8 |

**Any non-candidate world reaches 8/8? Yes, conditionally in the claim-ready oracle: duplicate positives, irrelevant overlapping negatives, and abbreviation description.** Largest door: R6 permits nine identical positives to stand in for breadth. No observed production counter 8/8 is claimed. Frozen W0/W1/W2 controls themselves remain below 8/8.

Working-tree SKILL.md remained byte-identical to base `1c8f37edf2e5ac0fb3c2be1c88e32406313fe47b`; candidate had not been applied. Base parsed length is 1021; candidate 876. Inclusive terminating-period counting gives base first sentence 151, versus the plan's 150 (which excludes the period); both fail the 99 bound. Candidate inclusive length is 65.

## Oracle versus counter / predicate identity

Oracle was written and exercised before any counter inspection. `verifiers/check_description_render.py` was absent at all inspections, including final availability receipt. Therefore no per-rule counter outputs exist to compare, and absence is NOT evidence of agreement.

| Exact rule label | Oracle operation | Counter comparison |
|---|---|---|
| R1 first_sentence_le_99 | First period followed by literal space/end; period included; no terminator uses whole text | N/A: file absent |
| R2 prefix_carries_triggers | Case-insensitive substring checks in first 99 characters | N/A |
| R3 spec_max_1024 | 1–1024 parsed characters | N/A |
| R4 imperative_invocation | Case-insensitive imperative substring plus case-sensitive `Triggers:` | N/A |
| R5 sibling_clauses | Actual named sibling instrument, exit 0 plus exact success line | N/A |
| R6 eval_set_shape | Exact header/counts, quoted trigger phrases, indirect floor, negative token overlap | N/A |
| R7 no_xml_tag | Neither angle bracket present | N/A |
| R8 sourced_entry | Structural field/located-short-quote checks; synthetic fixture explicitly identified | N/A |

R5 was not approximated by bare lane-name matching: the actual sibling checker rejects the token dump through ownership/routing-marker clause binding, naming 0/10 qualifying lanes. Base and candidate report 10/10.

## Commands and receipts

- `TMPDIR=/fast/scratch/hyaku/kotoba-r85/ReviewerC1 python3 -B /fast/scratch/hyaku/kotoba-r85/ReviewerC1/oracle.py --scratch /fast/scratch/hyaku/kotoba-r85/ReviewerC1` → exit 0; detailed per-rule lines in `oracle-receipt.txt`. This is a reporting driver, not the production counter's exit contract.
- Oracle internally runs `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round74.md --province PROVINCE.md --skill <world-path>` in the lane. Base/candidate exits 0; token dump and naive cut exit 1.
- `git show 1c8f37edf2e5ac0fb3c2be1c88e32406313fe47b:SKILL.md` → exit 0; raw equality with worktree true. Base fixture and entry lookups exit 128 (absent). `availability-receipt.txt` records these observations.
- Oracle SHA256: `35941bd793ff4b01f4af67b085061086975e7a0c53a6b913697d9bf984ef6c81`.

## Residual risk / verification gaps

Counter agreement, its --rev implementation, exit ladder, diagnostics and actual current-tree 8/8 remain unverified because its file was absent. LSP device unavailable (`read xd://lsp`: `No such tool`), so no semantic references/definition/diagnostics proof is asserted. R8's exact quote-location serialization is unspecified; this oracle uses a `quote:` and `location:` field and does not claim semantic source verification. Synthetic R8 is solely a structural test input. No runtime, routing, resume or saturation claims were changed or assessed; they are outside this C1 assignment.

No tools installed/upgraded; no production or git writes. All durable files are under this seat's wave directory and the required trailer report. Scratch is removed after receipts are copied.


## Append-only follow-up — counter available (2026-11-04T20:14:58Z)

The observations above are preserved as before-availability evidence. L1 subsequently requested comparison after the counter landed. `counter-comparison.txt` supersedes the earlier availability gap for these exercised paths only.

### Oracle/counter table (R1 through R8, G/R)

| Saved claim-ready world | Oracle | Counter | Disagreements |
|---|---|---|---|
| Base | R G G R G G G G (6/8) | R G G R G G G G (6/8) | none |
| Candidate | G G G G G G G G (8/8) | G G G G G G G G (8/8) | none |
| Naive cut | G G G R R R G G (5/8) | G G G R R R G G (5/8) | none |
| Token dump | G G G R R R G G (5/8) | G G G R R R G G (5/8) | none |
| Duplicate positives | G G G G G G G G (8/8) | G G G G G G G G (8/8) | none |
| Irrelevant negatives | G G G G G G G G (8/8) | G G G G G G G G (8/8) | none |
| Abbreviation description | G G G G G G G G (8/8) | G G G G G G G G (8/8) | none |

These are function-level executions with saved world inputs, not claimed committed candidate CLI results. R5 ran the actual staged sibling checker. No repository/fixture git writes were performed. Scratch was recreated at the same authorized path, passed through TMPDIR, and removed in finally.

Canonical CLI executed: `TMPDIR=<seat scratch> python3 -B verifiers/check_description_render.py --rev 1c8f37edf2e5ac0fb3c2be1c88e32406313fe47b` -> exit 1, `description render rules met 4 of 8`. Every per-rule base verdict agrees with the independent base oracle. The counter reads revision inputs through `rev_bytes`/git in evaluate (lines 359–382).

### Additional predicate-identity findings

**High — R8 does not require a located quote.** `verifiers/check_description_render.py:343-348` gathers any double-quoted text anywhere in the entry and checks only its word count. An entry containing `source: S213`, the date, `recheck: later`, and `quote: "A sufficiently long quotation without any location."` passes counter R8; independent R8 rejects it (`no located marker`). The frozen plan explicitly requires a *located* quote. No locator field or adjacent citation is checked.

**Medium — R8 adds an unfrozen minimum quote length.** Counter lines 80 and 344–348 require 3–25 words; the frozen plan says only ≤25 words. A located two-word quote passes the oracle but fails counter R8 (`no located quote of 3-25 words`). Both exercised disagreements are recorded in `counter-comparison.txt`. The plan does not prescribe a particular locator serialization; the tests intentionally make absence/presence unambiguous.

Other implementation differences observed but not asserted as exercised defects: trigger-term extraction stops at sentence end rather than Anti-triggers; R6 additionally requires at least one quoted trigger term and rejects blank queries/rows. No disagreement on the seven assigned worlds. Full YAML generality and every CLI error branch remain outside exercised coverage.

Recommendation remains: do not certify C1 quality from 8/8; preserve the frozen rule sentences and report the false-green attacks plus R8 identity failures. No repairs were made.
