# CriticDoNothingTarget — round 66 w1

**Seat:** critic (do-nothing control vs frozen C1/C2 targets). **Lane:** kotoba only.
**Base:** `11385e04e368c1e94ab1a5a89d7439033eb1f855`. All mutations ran in throwaway git clones under `/tmp` (`/tmp/r66-sb`, `/tmp/r66-orphan`); no lane bytes, claims, counters, or receipts touched. Counter used is the lane-tip file (sha256 `3129c0d7…3141`), which does not exist at base — it reads `--rev` blobs, so running it against the base rev is the intended control mode.

## Question

Can the base, or a receipt-only change, reach C1's `240 assertions` or C2's `2 of 2` without the claimed repairs?

## C1 — no loophole at the honest level; headline number is not self-authenticating

Observed at base clone:

- `g9_conjunct` one-word off-citation tail returns `[]`; `check_scoped_rules_v32.py --self-test` → `0 failure(s) over 234 assertions` (counter sha `b6cfc764…`). Matches `controls/C1-one-word-control.txt`.
- Committed a receipt-only commit (added `.ufo/waves/round-66/receipts/fake.txt` and `corpus/knowledge/fake-r66.md`): still `234`, still `[]`. The self-test count is fixture-internal; no repo-resident data file feeds it. **No committed-byte or worktree-only change can move the count.**

Residual exposure, stated for calibration: the only route to the literal string "240" is editing the verifier — e.g., padding six trivial assertions. `check_assertion_floors.py` fails on `observed < floor`, so inflation is unguarded there. But the frozen predicate is conjunctive (one-word must-fail, retained worlds/survivors/must-fail lines, floor pinned at lengths 1–3 with mutant attribution), and `C1-kill.txt` already shows all five floor mutants die on the named witness. A padded verifier cannot satisfy the retention clauses without implementing the coupling. **Verdict: target unreachable by do-nothing; the bare count must never be read alone.**

## C2 — counter-level loophole found and demonstrated; companion gate is the real defense

Reproduced control: tip counter at `--rev 11385e04` → `0 of 2`, exit 1.

**Loophole 1 — byte-shape certification.** Committed a descendant of base carrying *only* fabricated shapes: stub registries `{"wave":"w1","members":[]}` / `{"wave":"w2","members":[]}`, four index-row lines in `corpus/README.md`, `corpus-baseline.json` expects overwritten to the seven pins plus a `round66_rerecord` note, and the four marker strings appended to `verify_corpus_integrity.py` **inside a `#` comment** (zero semantic change). Result: `r66 routed defects closed 2 of 2`, exit 0 — while no repair exists.

**Loophole 2 — no provenance.** Built a *parentless* commit in a scratch repo (`git commit-tree`, six blobs only: `.ufo/waves/round-65/w{1,2}/swarm-registry.json`, `corpus/README.md`, `corpus-baseline.json`, `verify_corpus_integrity.py`), fetched only the base object in, and ran `check_r66_routed_repairs.py --rev <orphan> --root <scratch>`: `2 of 2`, exit 0. `merge-base --is-ancestor` confirms the certified commit is **not a descendant of base** — the counter never checks ancestry, ref membership, or that the tree is a lane tree at all.

**Structural weaknesses behind both:** (a) D2 is literal substring matching — comments satisfy `COMMIT_HOP_MARKER`, `def commit_resolves(`, `inside_code_span`, `commit_resolves(hex_id`; the def line alone satisfies the call-site string; (b) D1 accepts any nonempty JSON dict — no schema, no check the blobs are generated wave artifacts; (c) baseline `expect` values are self-asserted — the landing writes both the assertion and the asserted number; (d) index rows need the path *string* in README, not a checked index/file consistency (the four lesson blobs do exist at base, but the counter doesn't require it); (e) no ancestry constraint on `--rev`.

**Backstop observed:** the fabricated descendant tree still fails `verifiers/verify_corpus_integrity.py` (exit 1: `unindexed=5`, `commit_unresolvable=3`, `tracked_files`/`commit_total` DRIFT), and fitting the baseline to drifted observeds would satisfy that gate but fail the counter's pinned expects — the two instruments use disjoint modes (equal vs zero), so neither alone can be quietly fitted. The frozen predicate's second conjunct is what rejects the fabrication; **the `2 of 2` line alone is forgeable.**

## Verdict

- Do-nothing base: both targets unmet (confirmed).
- Receipt-only change: C1 unreachable entirely; C2's *counter line* reachable by fabrication — a real loophole at counter granularity, closed only by the conjunctive frozen predicate, not by the counter itself.
- Fixable defect, not a judge-rejecting tradeoff: the counter is deliberately a committed-byte predicate, but its calibration claim ("2 of 2" ⇒ repairs landed) fails. A scorer reading only that line admits a fabricated landing.

## Smallest safe corrections (advisory, frozen predicates unchanged)

1. In `main()`: `git merge-base --is-ancestor BASE_REV <rev>` plus a lane-tree sanity check (e.g., `SKILL.md` + `verifiers/` present at `--rev`) — kills orphan/foreign-tree certification.
2. In `check_d2`: strip `#`-comment lines before substring tests; require `commit_resolves(` on a non-def line; `show()` each `SPOTCHECKS` blob at `--rev` so indexed paths must exist.
3. In `check_d1`: require a schema marker the real generator emits (e.g., `ufo-swarm-wave` key) rather than any nonempty dict.
4. Cheapest airtight option: have the counter export `--rev` to a temp worktree and execute `verify_corpus_integrity.py` there, unifying the two conjuncts in one command.

## Evidence

All outputs above are observed runs in `/tmp/r66-sb` (clone of the lane at base, plus two test commits) and `/tmp/r66-orphan` (scratch repo, parentless commit `8c514814`). No installs performed (RULES.md read; pacman paused, nothing needed).
