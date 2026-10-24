# Round 66 — frozen claim plan

Base: `11385e04e368c1e94ab1a5a89d7439033eb1f855` (current lane tip at round start; includes the r65 non-author spot-check). The initial diagnosis preceded this committed freeze; no swarm seat has scored either claim. Counters and controls below are frozen before claim landing.

## C1 — depth (lowest owned axis; score 9)

**Move:** G9 clause support in `verifiers/check_scoped_rules_v32.py`, specifically the one-content-word tail that the current `MIN_CLAUSE = 2` exemption skips.

**Before:** `python3 -B verifiers/check_scoped_rules_v32.py --self-test` → `0 failure(s) over 234 assertions`; the control `g9_conjunct([line], cell, 1, page)` for `cell = line + " and exfiltrates."` returns `[]` although the word occurs only elsewhere on the page.

**Frozen after predicate:** the same self-test prints `0 failure(s) over 240 assertions` and retains `worlds reject 7 of 7; eligible rows pass 4 of 4`, `survivors closed 6 of 6`, and the existing G9 must-fail line. The former one-word exemption becomes a must-fail witness; a one-word tail supported by the cited line remains accepted; the coupled clause floor is pinned at lengths 1, 2, and 3, with uncoupled and zero-floor mutations admitting the witness. The counted value is 240; score remains 9 pending the non-author closure's rubric ruling.

**Do-nothing control committed before landing:** `.ufo/waves/round-66/controls/C1-one-word-control.txt` — one-word fabrication returns `[]` on the base bytes, while the existing suite remains at 234; target unmet.

## C2 — consistency (calibration sub-axis; score 10)

**Move:** close r65 closure-routed D1 and D2 in one counted repair pair. D1: commit both generated r65 `swarm-registry.json` blobs. D2: index the four closure-owned r62–r65 spot-check lessons; resolve fleet report commits in the fleet repository and classify code-span meta-findings as context; re-record observed corpus counts only after all round corpus entries land.

**Before:** pinned base `11385e04e368c1e94ab1a5a89d7439033eb1f855`; `verifiers/check_r66_routed_repairs.py --rev <base>` → `r66 routed defects closed 0 of 2`, exit 1. The sandbox re-run of `verify_corpus_integrity.py` at that base prints 4/9 checks pass and DRIFT for tracked files 116/81, unindexed 4, report pointers 79/51, commit citations 38/32 and unresolvable commits 3; exit 1.

**Frozen after predicate:** `python3 -B verifiers/check_r66_routed_repairs.py --rev <round-66-tip>` prints `r66 routed defects closed 2 of 2`, exit 0, while its pinned base remains 0 of 2. The counter's committed-byte predicate requires both nonempty registry JSONs and the D2 index, integrity-source hop, and measured baseline pins: tracked_files 118, unindexed 0, report_total 79, report_dead 0, commit_total 37, commit_unresolvable 0, commit_nonhash 0. Independently, `python3 -B verifiers/verify_corpus_integrity.py` must exit 0 at the final lane tree. Score remains 10 pending closure.

**Do-nothing control committed before landing:** `.ufo/waves/round-66/controls/C2-before.txt` — pinned-base counter result and sandbox integrity-gate output; target unmet.

## Frontier / source binding

S122 (FORCE11 Software Citation Principles, opened 2026-10-24) will support C2's scoped note that a commit hash is version-specific evidence only when interpreted with its repository context, not a durable software citation by itself. The round lesson will carry the located source quote and the admitted knowledge entry will cite S122.

## L2 preparation

The L1 holds the planner seat. Prepare one v1 build wave and one v1 falsify wave under `.ufo/waves/round-66/`; this seat has no task/AgentSwarm dispatch surface, so the specs are preparation evidence and remain undispatched for the orchestrator. No wave seat has scored data.

## Post-freeze execution note (frozen claim predicates unchanged)

- Wave shape correction: the prepared evidence is one policy-v1 wave (`w1-spec.json`, 35 distinct seats), not a prepared wave 1 plus wave 2. No task call was dispatched from this L1 seat; no wave-1 output exists, so the v1 rule requiring at least 32 distinct returned attack items does not authorize a wave 2. The L1 still holds the planner seat; no seat has scored the claims.
- No-harm follow-through: after the primary corpus-integrity gate and C2 counter were measured at the pinned tip, `verify_corpus_independent.py --json` exposed the same three pre-existing commit-context rows. The independent implementation is extended with its own lane/fleet lookup and code-span context tests; the C2 frozen 2-of-2 predicate and values are unchanged. Its before/after gate evidence is recorded separately.
