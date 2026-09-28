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
| depth | 9 — was 8 | `python3 verifiers/verify_harness_claims.py` → `27/27 checks pass` (exit 0, ≈3 s), `--self-test` → `0 failure(s) over 10 assertions`; the newest captured catalogue renders `17/17` lines from cache; `grep -c '^- \[ \]' SKILL.md` → 40 checklist boxes still lane-attested (14/9/9/8 by section — round 12 added the second-witness box) @ round-12 worktree | owned | 12 |
| consistency (calibration sub-axis) | 10 — was 9 | second instrument: `python3 verifiers/verify_corpus_independent.py` (L2 lane `ExecIndependentVerifier`, sha256 `430fe289…`; authored neither the author's script nor its baseline, never read its source) agrees **check-for-check** with `python3 verifiers/verify_corpus_integrity.py` on the landed tree — same nine numbers, the same eight excluded sites and the same quoted-context sites (2 after the census file landed), exit 0 both — and both exit 1 on a clone at `d49dfa5` with the **same ten dead-pointer sites** and the same non-hash site; agreement stable across three live tree states. Evidence: `corpus/knowledge/independent-verification-round12.md` (including §3's seven adjudicated definitional differences and §3b's shared blind spot), `verifiers/fault_injection_corpus.sh` (10 classes, both instruments gated, `--self-test` 4 probes, exit 0), `/tmp/round12/ExecIndependentVerifier/compare.md`. **Band 10 = repeated non-author verification in the opposite direction:** leg 1 was round 11's cold run (non-author checking the author's numbers), leg 2 is this derivation (non-author deriving the verdicts, the author's instrument required to agree); it produced two repairs to the author's script (a documented quoted-context rule that could never fire; an index census reading more of `README.md` than its docstring claimed). The old `19 of 20 host-absolute` clause is retagged: 24 of 25 checked pointers are host-absolute (resolution is machine-local; a clone's green is not hermetic — measured, both instruments). Residual: expectations (the baseline) stay authorial — `corpus/knowledge/independent-verification-round12.md` §6 | owned | 12 |
| coverage (advisory) | 7 | `PROVINCE.md`; `SKILL.md` § Instruction surfaces (7 classes); `corpus/README.md` § Coverage map (38 data rows, `awk -F'\|' '/^\|/ && NF>=4 && $3 !~ /^[-:[:space:]]*$/ {n++} END{print n}' corpus/README.md`) + Known gaps. Below 8: implicit-intent fidelity unmeasured; no MCP/plugin surface on this host @ round-12 worktree | advisory | 12 |
| operability (advisory) | 7.5 — was 7 | two committed verifiers run from any cwd with 4 exit codes proven each (`cd /tmp && python3 …/verify_harness_claims.py` → exit 0; `…/verify_corpus_integrity.py` → exit 0 with `--self-test` green; `…/verify_corpus_independent.py` → exit 0, 3 exit codes) and a **committed** fault harness (`verifiers/fault_injection_corpus.sh`: 10 fault classes, each asserted on JSON against both instruments, `--self-test` 4 probes, exit 0/1/2 — replaces the round-11 `/tmp` fault table that was not re-runnable); `SKILL.md` checklist boxes remain the only un-automated procedures (40 boxes) @ round-12 worktree | advisory | 12 |
| freshness (advisory) | 8 | round-12 re-measure inside the move (unchanged from round 11, so no drift to report): `sqlite3 -readonly ~/.omp/agent/skill-descriptions.db "select count(*),min(length(description)),max(length(description)) from skill_descriptions;"` → 17/44/98; `grep -c 'evaluated permission=skill' ~/.local/share/opencode/log/opencode.log` → 471; `grep -o 'message=init count=[0-9]*' … \| sort \| uniq -c` → 15×1 16×141 17×34 18×14; compression warns 10925; `python3 verifiers/verify_harness_claims.py` → 27/27 exit 0; **new**: the round-9 file's template + root-list claims were re-read against the ELF and two were wrong → corrected @ round-10 worktree | advisory | 12 |
| calibration (advisory) | 7.5 — was 7 | `SHONEN.md` — box 2 `[x]` on round 11's non-author cold run, boxes 1/3 `[x]` on round 12's non-author checks (reviewer lane named per box; box 4 stays `[~]`); the *command* in box 1 was itself the fourth instance of the round-11 defect class (an `awk` that printed an empty line while claiming `13/9/9/8`) and now reproduces its numbers when run as written; the depth row names what is *not* covered (40 checklist boxes, none executed); every row carries its command and tree, and two rows this round were re-based on evidence that had moved @ round-12 worktree | advisory | 12 |
| adjacency (advisory) | 7.5 — was 7 | Cross-domain defects audited and routed, never fixed: sibling `*-shokunin` descriptions 0/5 with triggers/arbitration (re-verified round 12 by the sentinel lane, same command), `corpus/knowledge/sibling-description-rewrites-round8.md` still unapplied; kumitate `scripts/cite-check.mjs` is complementary (not a consolidation candidate) and **kengaku already ships the pattern this lane moved to** — a non-author oracle (`corpus/evidence/round10-fleet/probe_ref.py`) re-derived its evidence and returned `ALL LAYERS AGREE`, so "second derivation" is a fleet pattern, not an invention here; two sibling **stale-count** defects found and routed with reproducers (kake `corpus/knowledge/ops-automation.md:22-30` → 11/77 probe rows violate `total-ok == violated+errors`; kasegi `corpus/knowledge/mission-ledger.md:32-34` → 8/718 rows lack `transition`); fleet commit identity: both hashes resolve in their own repos and are authored `shokunin <shokunin@local>` (resolvability fixed, lane-identity defect reported); `~/.agents/AGENTS.md` procedures `:55/:57`, dated TAC text `:48/:51`, `ufo.md` `cascade_note` ~30 days past expiry @ round-12 worktree | advisory | 12 |

## planned

Round 13 — **depth at the ceiling**: no verifier in this repo *runs* a checklist box
(40 boxes are counted, never executed). Candidate move: make one box executable —
`skill.trigger.name_directory` (a `SKILL.md` frontmatter `name` must equal its
directory name; 6/6 lanes match today, so the live tree is a genuine green case) —
as `verifiers/verify_skill_checklist.py` with check ids, exit codes and a fixture
world where the name is missing. Deliberately overfit first: prove the mechanism on
that one box before generalizing, and count how many of the 40 boxes can never be
automated (semantic judgments such as trigger quality and sibling arbitration).

**Falsifier (commands, not promises).** Landed iff, at the round-13 commit: the
fixture world exits 1 naming the missing-name item, the live tree exits 0, and the
new checker's `--self-test` fails on a deliberately broken fixture. If the live tree
needs the check softened to pass, the box was not mechanical and the move did not
land.

Second candidate, carried from this round's own residual: a **derivation-owned
expected census** — the `equal` ids still compare against a baseline only this lane
records; the independent derivation publishes observations, not expectations. Falsifier:
the two instruments disagree on a count class that no baseline is involved in.

**Axis-bookkeeping proposal (for the protocol lane).** Round 13's plan (scratch,
`/tmp/round12/PlanRound13/plan.md`, not citable as in-repo evidence) recommends
folding `consistency` back under `calibration` now that its band-10 criterion is met
and its measurement lives as component evidence in `corpus/knowledge/independent-verification-round12.md`,
unless the `AXES.md` ↔ `MISSION.md` mismatch is formally reconciled. Recorded here as
a proposal, not acted on: a lane does not retire an axis the mission assigns without
the protocol lane's word.

Carried, not hidden: 24 of 25 checked pointers are host-absolute (resolution is
machine-local by construction, so a clone's green is not hermetic — measured on both
instruments); report pointers in `LOG.md`/`SCORECARD.md`/`SKILL.md` are unchecked by
either instrument; `corpus.index.tracked_files` and the three `equal` ids are change
detectors needing a deliberate re-record as the corpus grows (this round re-recorded
them into `verifiers/corpus-baseline.json` with every move explained); the shared
class blind spot (`verifiers/fault_injection_corpus.sh` fault (f)) — a pointer that
leaves the `.ufo/reports/round-N/` grammar is invisible to both tokenizers and only
the count detector notices; `SKILL.md`'s 40 checklist boxes remain lane-attested
(per-round records keep their round's value by design).

## retired

None. No saturation or wrong-fit evidence (`../AXES.md`, § Working an axis).

## Move log

| Round | Axis | Before | After | Evidence |
|---|---|---|---|---|
| 1–9 | see `LOG.md` rounds 1–9 and `corpus/lessons/round-*.md` | — | — | per-round reports `.ufo/reports/round-N/kotoba.md` |
| 9 | consistency | 5 — 31 claim units, 9 UNSCOPED, 0 `<available_skills>` | 7 — UNSCOPED 0, 6 residuals re-worded, router model section | `corpus/knowledge/claim-scope-audit-round9.md` @ `e997d45` |
| 10 | depth | 8 — harness claim set lived as 6 hand-run recipes; no committed verifier | 9 — `verifiers/verify_harness_claims.py` 27 checks, exit 0/1/2/3, `--self-test` 10 assertions, 17/17 keys reproduced, newest catalogue 17/17 from cache | `verifiers/baseline.json` @ round-10 worktree |
| 10 | consistency (integration, not a second move) | 7 — 8 dead commit pointers (`git grep -h -o -E "commit \`round-[0-9]+\`" e997d45 -- 'corpus/*.md' \| wc -l` → 8), **4** unindexed files (that count carries no recorded command; a round-12 brace-aware `comm` reconstruction at `e997d45` yields 7 — the round-12 census could not reproduce the 4), 9 routed aggregator defects open | 8 — pointers 0, unindexed 0, routed defects 0 open | `corpus/lessons/round-10.md` § Audit closure @ round-10 worktree |
| 11 | consistency (calibration sub-axis) | 8 (unsupported) — both recorded counting commands invalid: `round-[0-9]` cannot match `round-10` (false zero with the defect present), `comm` regex cannot tokenize the brace row `lessons/round-{1,4,5}-aggregator-audit.md` (3 indexed files reported unindexed), `../.ufo` substring grep counts 9 before *and* after; real defects: 10 dead report pointers (9 `../.ufo` rows + 1 bare), 1 non-hash `commit` token, 2 md5 pins printed in commit notation (1 in-repo — `corpus/knowledge/claim-scope-audit-round9.md:15` — plus 1 outside the repo, not locatable by the round-12 census) | 9 — `verifiers/verify_corpus_integrity.py` (9 checks, exit 0/1/2/3, `--self-test` 0/80 as landed; 86 after the round-12 repair) + `verifiers/corpus-baseline.json`; red-before on a clone at `d49dfa5` `report_dead=10/19 nonhash=1` exit 1 → live `9/9` exit 0; 10/10 planted faults surfaced (record not re-runnable — /tmp wiped; a committed harness lands in round 12); non-author cold run with 3 independent spot-checks, 0 discrepancies | `corpus/knowledge/corpus-integrity-round11.md` + `corpus/knowledge/cold-run-round11.md` @ `4dd7753` || 12 | consistency (calibration sub-axis) | 9 — verdicts were author-only: one non-author act existed (round 11's cold run), and it re-ran the author's script; the author's docstring promised a quoted-context rule its tokenizer could not fire, and its index census read more of `README.md` than it claimed | 10 — a second instrument (`verifiers/verify_corpus_independent.py`, non-author, source-blind) agrees check-for-check on the landed tree (exit 0 both, identical counts/shapes/detail sites) **and** on a clone at `d49dfa5` (exit 1 both, the same ten dead sites + the same non-hash site); the comparison forced the two author-script repairs; `verifiers/fault_injection_corpus.sh` gates both instruments across 10 fault classes; the claim census (84+ rows, landed in-repo) repaired 24 stale numbers, 4 false claims, 9 unexpressible ones and adopted the claim-scope rule | `corpus/knowledge/independent-verification-round12.md`, `corpus/knowledge/claim-census-round12.md`, `corpus/lessons/round-12.md` @ round-12 landing |
