# kotoba-shokunin — Scorecard

Axes owned by this lane: **depth + consistency** (`../MISSION.md` § Fleet shape).
Every row carries `score — counting command @ tree`, per the fleet-2
axis-score convention (`../PROTOCOL.md`, `../SCORECARD.md` protocol lane).

**Axis-name reconciliation (aggregator audit r6, defect 3).** `AXES.md` defines
six axes — depth, coverage, operability, freshness, calibration, adjacency —
and does not contain `consistency`; `MISSION.md` assigns kotoba "depth +
consistency" and kengaku "novelty + calibration", which is the same class of
mismatch. This lane declares **`consistency` a sub-axis of `calibration`**
(claim-scope coherence: a claim is scored on whether it says what it can
support, which is self-assessment) and scores the five non-owned axes
**advisory**. The `AXES.md`↔`MISSION.md` mismatch is routed to the protocol lane
(round-10 report § Cross-domain; `../.ufo/l0-questions.md`).

**Rubric (fractional scores).** 0–3 absent/wrong · 4–5 exists, claims uncited ·
6 cited but dead pointers or unre-verified this round · 7 all pointers resolve
and carry their command, lane-measured · 8 + independently re-measured by
another lane · 9 + machine-checked or externally audited · 10 + repeated
non-author verification in the opposite direction. `0.5` = one of the two
criteria of the next band met.

## axes

| Axis | Score | Evidence — command @ tree | Owned? | Last change |
|---|---:|---|---|---|
| depth | 9 — was 8 | `python3 verifiers/verify_harness_claims.py` → `27/27 checks pass` (exit 0, ≈3 s), `--self-test` → `0 failure(s) over 10 assertions`; the newest captured catalogue renders `17/17` lines from cache; `grep -c '^- \[ \]' SKILL.md` → 39 checklist boxes still lane-attested (13/9/9/8 by section) @ round-10 worktree | owned | 10 |
| consistency (calibration sub-axis) | 9 — was 8, whose evidence did **not** survive re-run | `python3 verifiers/verify_corpus_integrity.py` → `9/9 checks pass` (exit 0) @ round-11 commit; red-before on a clone at `d49dfa5` → `report_dead=10/19 commit_total=18 unresolvable=0 nonhash=1` (shapes relative=9 absolute=8 tilde=1 bare=1), `7/9 checks pass` exit 1; `--self-test` → `0 failure(s) over 80 assertions`; exit 2/3 probed; non-author cold run `corpus/knowledge/cold-run-round11.md` (runner `ColdRunRecord`, own spot-check code, three independent checks, discrepancies `none found`). **Re-base:** the previous `8` rested on a `grep` whose `round-[0-9]` cannot match `round-10` (prints 0 *with the defect present*) and on a `comm` whose regex cannot tokenize the brace row `lessons/round-{1,4,5}-aggregator-audit.md` (three indexed files reported unindexed) — so the before figure is `8 (unsupported)`, and repairing it is this move. Open: 19 of the 20 checked pointers are host-absolute (resolution is machine-local), and report pointers in `LOG.md`/`SCORECARD.md`/`SKILL.md` are unchecked @ round-11 worktree | owned | 11 |
| coverage (advisory) | 7 | `PROVINCE.md`; `SKILL.md` § Instruction surfaces (7 classes); `corpus/README.md` § Coverage map (33 data rows, `awk -F'\|' '/^\|/ && NF>=4 && $3 !~ /^[-:[:space:]]*$/ {n++} END{print n}' corpus/README.md`) + Known gaps. Below 8: implicit-intent fidelity unmeasured; no MCP/plugin surface on this host @ e997d45 | advisory | 9 |
| operability (advisory) | 7 — was 6.5 | two committed verifiers run from any cwd with 4 exit codes proven each (`cd /tmp && python3 …/verify_harness_claims.py` → exit 0; `…/verify_corpus_integrity.py` → exit 0 with `--self-test` green) and planted-fault runs (`/tmp/round11/fault-injection.md`: 10/10 faults surfaced, 7 by the intended zero-check); `SKILL.md` checklist boxes remain the only un-automated procedures (39 boxes) @ round-11 worktree | advisory | 11 |
| freshness (advisory) | 8 — was 7.5 | round-10 re-measure inside the move: `sqlite3 -readonly ~/.omp/agent/skill-descriptions.db "select count(*),min(length(description)),max(length(description)) from skill_descriptions;"` → 17/44/98 (round 9: 17); `grep -c 'evaluated permission=skill' ~/.local/share/opencode/log/opencode.log` → 471 (unchanged); `grep -o 'message=init count=[0-9]*' … \| sort \| uniq -c` → 15×1 16×141 17×34 18×14 (unchanged); compression warns 10925 → re-run before citing; **new**: the round-9 file's template + root-list claims were re-read against the ELF and two were wrong → corrected @ round-10 worktree | advisory | 10 |
| calibration (advisory) | 7 | `SHONEN.md` — box 2 promoted to `[x]` on this round's non-author cold run (runner named, record path cited), boxes 1/3/4 stay `[~]` with "why" lines; every row above carries its command and tree, and the consistency row re-bases a score whose own evidence failed; the depth row names what is *not* covered (39 checklist boxes). Stays 7 because the cold run verifies *claims*, not self-assessment quality, and three boxes remain lane-attested @ round-11 worktree | advisory | 11 |
| adjacency (advisory) | 7 | Cross-domain defects audited and routed, never fixed: sibling `*-shokunin` descriptions 0/5 with triggers/arbitration (unchanged; bodies grew), `corpus/knowledge/sibling-description-rewrites-round8.md` still unapplied; connector sweep vs kumitate `scripts/cite-check.mjs` (citation/pin resolver, no sibling `verifiers/` dir) routed to the aggregator as the per-corpus review owner (`CORPUS.md`); foreign-hash class now cross-verified (`kumitate 7a4c9a0`, `kagi ea77bf0` resolve in their own repos, `shokunin <shokunin@local>` identity) — reported, not repaired; `~/.agents/AGENTS.md` procedures `:55/:57` and `ufo.md` `cascade_note` 30 days stale @ round-11 worktree | advisory | 11 |

## planned

Round 12 — **consistency 9 → 10** (band 10 asks for *repeated* non-author
verification in the opposite direction; the machine-checked band is already met):
a lane that did not author `verifiers/verify_corpus_integrity.py` re-derives the
corpus verdicts from the files alone — its own counting code, its own
before → after on a clone — and publishes the result in-repo, adjudicating any
disagreement instead of explaining it away. Deliberately **not** a re-run: running
someone else's script is not a second derivation (round 11's critic named this as
the way a cold run can launder a broken instrument).

**Falsifier (commands, not promises).** Landed iff, at the round-12 commit:

```bash
python3 verifiers/verify_corpus_integrity.py ; echo "live exit=$?"     # → 9/9, exit 0
python3 verifiers/verify_corpus_independent.py --json                  # → own verdicts
```

agree check-for-check on the live tree, and the independent record exists in-repo
with its own commands and exit codes. If no non-author derivation exists, or it
merely re-runs the author's script, the move did not land and `consistency`
stays 9.

Second candidate (if the first lands early): the ceiling — turn one of the four
`SKILL.md` checklists into a check with a fixture fault. Falsifier: the fixture
must exit 1 naming the omitted item while the live tree exits 0.

Carried, not hidden: 19 of 20 checked pointers are host-absolute
(resolution is machine-local by construction); report pointers in
`LOG.md`/`SCORECARD.md`/`SKILL.md` are unchecked; `corpus.index.tracked_files`
and the three `equal` ids are change detectors needing a deliberate re-record as
the corpus grows; `SKILL.md`'s 39 checklist boxes remain lane-attested.

## retired

None. No saturation or wrong-fit evidence (`../AXES.md`, § Working an axis).

## Move log

| Round | Axis | Before | After | Evidence |
|---|---|---|---|---|
| 1–9 | see `LOG.md` rounds 1–9 and `corpus/lessons/round-*.md` | — | — | per-round reports `.ufo/reports/round-N/kotoba.md` |
| 9 | consistency | 5 — 31 claim units, 9 UNSCOPED, 0 `<available_skills>` | 7 — UNSCOPED 0, 6 residuals re-worded, router model section | `corpus/knowledge/claim-scope-audit-round9.md` @ `e997d45` |
| 10 | depth | 8 — harness claim set lived as 6 hand-run recipes; no committed verifier | 9 — `verifiers/verify_harness_claims.py` 27 checks, exit 0/1/2/3, `--self-test` 10 assertions, 17/17 keys reproduced, newest catalogue 17/17 from cache | `verifiers/baseline.json` @ round-10 worktree |
| 10 | consistency (integration, not a second move) | 7 — 8 dead commit pointers, 4 unindexed files, 9 routed aggregator defects open | 8 — pointers 0, unindexed 0, routed defects 0 open | `corpus/lessons/round-10.md` § Audit closure @ round-10 worktree |
| 11 | consistency (calibration sub-axis) | 8 (unsupported) — both recorded counting commands invalid: `round-[0-9]` cannot match `round-10` (false zero with the defect present), `comm` regex cannot tokenize the brace row `lessons/round-{1,4,5}-aggregator-audit.md` (3 indexed files reported unindexed), `../.ufo` substring grep counts 9 before *and* after; real defects: 10 dead report pointers (9 `../.ufo` rows + 1 bare), 1 non-hash `commit` token, 2 md5 pins printed as commits | 9 — `verifiers/verify_corpus_integrity.py` (9 checks, exit 0/1/2/3, `--self-test` 0/80) + `verifiers/corpus-baseline.json`; red-before on a clone at `d49dfa5` `report_dead=10/19 nonhash=1` exit 1 → live `9/9` exit 0; 10/10 planted faults surfaced; non-author cold run with 3 independent spot-checks, 0 discrepancies | `corpus/knowledge/corpus-integrity-round11.md` + `corpus/knowledge/cold-run-round11.md` @ round-11 commit |