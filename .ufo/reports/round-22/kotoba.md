# kotoba — round 22 report (2026-10-19)

Lane: `kotoba-shokunin`. Round 22, loop 1 (loop-round 2), dispatched and admitted.
Dispatch HEAD: `b16300f`. Work commit: `<pending — recorded at landing, round-11 precedent>`.
Lane identity for the commits: `kotoba-shokunin <kotoba@shokunin.local>`.
Claims: **B** freshness (SKILL.md ≤600 by verbatim section move; checklist gate fully green) · **A2** adjacency (r16adj escalation via the L0 side channel + live acknowledgment measure) — `.ufo/round-22/claims.json` (its "five packets" wording was a count error — corrected by scouts A2/A4/A7 and in the records).
Swarm: **62 lanes** on `opencode-go-2/deepseek-v4.1-flash` (key 2 of 7); the item list carried 62 of the designed 64 (two lanes merged in design); all 62 completed, zero lost — the deviation is recorded in LOG, not papered over.
Status: **completed craft round, admitted** — every claim verified, no axis harmed.

## Work performed

- **B — the move** (evidence: scouts B01-B10 analysis, S01-S10 /tmp simulations — three independent green runs of exactly this variant: S04, S05, S07):
  - Extracted § Instruction surfaces body (SKILL.md source lines 76-166 at `b16300f`, 91 lines, sha256 `e046a025…` sed-canonical); appended it under a provenance header to the **existing** `corpus/knowledge/instruction-surface-census-round13.md` at EOF (outside `## Class inventory`, S07's constraint); replaced the section with an 8-line stub keeping the `## Instruction surfaces — pick the file before the fix` heading (S05: the heading is load-bearing for a round-12 counting claim).
  - Byte-preservation gates at landing: `sed -n '76,166p' | sha256sum` cross-checked against three scout-measured hashes (S06 `e046a025…` matched); contiguity (body `in` corpus file) PASS; no-duplication (body `not in` SKILL.md) PASS. The table's "All craft below" cell dangles in its new home — kept verbatim, named in the stub and corpus header (B02's only non-portable byte).
- **B — post-move sweep (all green, first since round 18):** checklist live **exit 0, 10 × PASS** — `line_budget evaluated 516 within budget 600 (from box at line 244)`, `box_map 41/41 (8 executed, 0 delegated)`, `command_binary_resolves 13`, `citation_resolves 35`, `governance.citation_resolves 171`; harness 28/28; corpus integrity 9/9 + independent exit 0 (the append drifted nothing — absorb variant, S04-predicted); surfaces 7/7 + self-test 0/75; fault harness OK; both self-tests green. Cost recorded: command subjects 19→13, citation tokens 42→35 — the moved span's subjects move to corpus-gate coverage, no coverage is lost net.
- **A2 — acknowledgment measure:** 0 across every surface for all five siblings — working trees, full git histories (`git log --all`), the fleet aggregator (`AGGREGATE.md`), and L0 (scouts A1-A5, A7; kake's SKILL.md:78 byte-identical since round 16; positive controls prove the greps). Ledger truth: **3 routes / 4 actionable findings** (r16adj-route-kake ← r16adj-03; -kasegi ← r16adj-04/08; -kumitate ← r16adj-12); kagi/kengaku carry findings but no routes.
- **A2 — escalation:** one line appended to `../.ufo/l0-questions.md` (the protocol-designated lane→operator channel): 299 bytes naming the three routes + the five siblings + the round-21 evidence file. Append-only proof: pre-sha `60ccdc9e…` (49 lines / 38356 B) → post-sha `029eebed…` (50 / 38656); `cmp -n 38356` against the HEAD blob = PREFIX-PRESERVED; fleet `git diff --numstat` = 1 insertion, 0 deletions. Named limit: the fleet path is left uncommitted — PROTOCOL gives no lane ownership of it; the integrator commits it.
- **Exploratory (not claimed):** substrate-pin-guard prototype on /tmp (P1-P8) — live pins hold (3/3, ns-exact mtime), all red probes designed exit 1/2; critic (P7) says none of the four prototypes is landable as-is (22 defects) — merge recipe recorded; round 23 claims the capability.
- **Deliberately not done:** no push (divergence debt persists — H1: remote tip `74fc0f1` absent locally, ahead 3); no sibling or fleet-repo commit; no budget raise (S08 pinned the boundary semantics: splitlines count, inclusive at 600 — the gate's own counter is the counting command, never `wc -l`); no capability-table row (the guard stayed /tmp-only).

## Landed changes

- `SKILL.md` — § Instruction surfaces replaced by the 8-line stub; 601 → 516 lines; 41 boxes intact. [LOG § Round 22]
- `corpus/knowledge/instruction-surface-census-round13.md` — round-22 absorption section (provenance + pinned sha + byte gate); 323 → 421 lines.
- `../.ufo/l0-questions.md` — one appended line (fleet root; the round's single out-of-repo write, append-only proved).
- `SCORECARD.md` — freshness row (carried red cleared), adjacency row (escalation + ack measure), coverage-row annotation via README, move-log rows for 22, planned refreshed for round 23.
- `corpus/README.md` — census row annotated with the round-22 absorption.
- `LOG.md` — § Round 22 appended (incl. the 62-of-64 deviation and the named-defect list).
- Intentionally unchanged: `verifiers/*` (no code touched this round), `SHONEN.md`, `PROVINCE.md`, protocol files, sibling repos.

## Before → after measurements

| Claim | Measurement | Before | After (round 22) | Command/evidence |
|---|---|---|---|---|
| B | SKILL.md line count | 601 (gate: `evaluated 601 — exceed budget 600`) | 516 (`evaluated 516 within budget 600`) | `python3 verifiers/verify_skill_checklist.py` — exit 0 |
| B | checklist gate | exit 1 (1 FAIL) since `02302c5` | **exit 0, 10 × PASS** | same |
| B | moved bytes | § at `SKILL.md:75-166` @ `b16300f` | verbatim in census file, sha256 `e046a025…` | sed/byte gate + contiguity + no-dup checks |
| B | box map | 41 mapped | 41 mapped (hashes unchanged) | `box_map_complete` line |
| A2 | sibling acknowledgment | unmeasured since round 16; "no acknowledgment observed" (round 20) | measured **0/5 on all surfaces** with positive controls | scouts A1-A5/A7 grep tables |
| A2 | L0 channel | 49 lines, zero r16adj rows | 50 lines, 1 r16adj line, pure append | `cmp -n 38356`, `git diff --numstat` |

Axis verdicts: **freshness — improved** (score held 8.0: the carried gate red is cleared by content; all six gates green for the first time since round 18); **adjacency — improved** (score held 8.0: escalation on the protocol channel + live 0-acknowledgment measure with evidence); coverage / operability / calibration / depth / consistency — **unchanged** (the coverage row's machine gate `verify_surfaces.py` 7/7 is unaffected — S07 verified on a /tmp copy; the 9-row table citation now points at the corpus home; no depth-9 evidence was touched — § Instruction surfaces is not among SHONEN box 1's exhibits, scout B07). No trade.
Drift handling: every drift found is recorded in LOG § Round 22 (round-21 report's "64/64" fragment overstatement — scout G5; the SCORECARD/LOG clock-wording off-by-one resolved by convention; round-15's non-verbatim frontmatter move — scout S10-D3; plus the A3/G7/C3 named debts).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — unchanged; the round-22 move removed a summary table (not a box-1 exhibit) to the corpus with a verbatim-bytes pin; box-1 evidence untouched (scout B07).
- [~] At least one end-to-end domain task executed and logged in LOG.md — unchanged; rounds 21-22 logged, lane-authored.
- [~] Instructions executable by an agent without oral context — unchanged; the byte-preservation gate added this round is itself an executable recipe in the corpus header.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — unchanged; siblings read-only; the one out-of-repo write (L0 append) is the protocol-designated lane→operator channel, append-only proved, integrator-owned thereafter.
