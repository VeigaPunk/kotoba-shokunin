# Round 70 — plan (hyaku run 6, lane kotoba, attempt 1)

Frozen before any wave seat scored any claim. Base lane tip (branch `master`):
`7d51253f99906b8551b6a0a108761eedac00de74` (`jj-lane.sh state` → `local=7d51253f… remote=7d51253f…
ahead=0 behind=0`; the tip is the r69 closure's spot-check commit, authored `protocol-shokunin`).
The watchdog log shows no `lane-dead-no-report kotoba round=70` line: no earlier attempt.

Round shape: **two v1 waves** (policy `scripts/hyaku/ufo-wave-policy.json`, band 32–64): wave 1
build + first falsifiers; wave 2 falsify only if wave 1 yields ≥32 distinct attack items, else one
residual `task` call of ≤8 reviewer/critic seats. The L1 holds the canonical §3 planner seat (the
validator rejects `planner`); the planning data-walk rides the wave-1 connector and scout items.

**Inherited state.** `git status --porcelain` at round start lists two lane-authored round-69 paths,
modified after the r69 report was filed: `.ufo/waves/round-69/w1/RevFreezeReceipt.md` (blob
`59585ea16261fe4e1a3d930962310541c5327329`) and `.ufo/waves/round-69/w1/ScoutStaleLane.md` (blob
`6f4c23bad11a5aee7aa7ab255dc4e11d44bddd94`) — routed defect K69-5. They are late revisions by the
r69 seats of their own reports (the diffs re-state the r69 commit chain `a02ba7e`…`9ce102b`); they
are committed as-is under this round's entry, never edited.

## Claim declarations (this round declares 2)

### C1 — consistency (calibration sub-axis), the routed round-69 defects

**Axis:** `consistency` (owned, 10). **Surface:** the eleven defects the r69 non-author closure routed
to this lane (`corpus/lessons/round-69-verifier-spotcheck.md` § Routed defects, K69-1…K69-11). Ten
are closable in the lane tree; K69-4 (the report must carry `SHONEN`, **Sources & frontier** and
**Trend verdicts** at filing) is closed by this round's fleet report and is outside the counter.

**Frozen predicate (the same sentence in this plan, in the counter's docstring and in the receipt):**

```
python3 -B verifiers/check_r69_routed_repairs.py --rev <rev>  ->  prints "r69 routed defects closed N of 10", exit 0 when N == 10
```

Items (each reads committed bytes at `--rev`; K69-11 runs the checklist gate in a `git clone
--shared` sandbox, never in the lane):

- **K69-1** `SCORECARD.md` carries a `**Round 69 axis annotations` block naming the three r69 counters
  (`check_skill_precedence.py`, `check_r68_routed_repairs.py`, `check_province_core.py`), the r69
  measured tip `9ce102b9e3f8896d5ed3f050ee896ca90d693a38` and the r69 base `a5f7459f99bb27bf697e9438362e75ac5833eca8`.
- **K69-2** `LOG.md`'s round-69 entry records the off-branch landing: it names the orchestrator
  fast-forward, `9ce102b` and the four round commits `a02ba7e`, `54f4b6c`, `278b9dc`, `9ce102b`.
- **K69-3** the same entry records the report attribution: `4844216b`, `9d9f181e`, `probe` and `0a1199a0`.
- **K69-5** both inherited paths are tracked at `--rev` with exactly the blobs pinned above, and the
  round-70 lesson names both paths.
- **K69-6** `LOG.md` has a heading line beginning `## Round 69` that falls after the base's last line,
  and its entry carries `trigger`, `action`, `outcome` and `pointer` labels.
- **K69-7** the round-69 entry carries both numeric corrections: `10 receipts` (not nine) and
  `23 landed` with `1 dispositioned`.
- **K69-8** `.ufo/waves/round-70/receipts/r69-tip-defense.txt` names `measured-rev:
  9ce102b9e3f8896d5ed3f050ee896ca90d693a38` and carries, for each of the three r69 counters, a
  `command:` line naming it, its verdict line and `exit=0`.
- **K69-9** `corpus/lessons/round-70.md` logs S201's anchor change old→new: one line naming `S201`,
  `(13 words)` and `(14 words)`.
- **K69-10** `corpus/lessons/round-69.md` carries an appended erratum line naming
  `(18 assertions)` and `22 assertions`, after the base's last line.
- **K69-11** `python3 -B verifiers/verify_skill_checklist.py --json` run in a sandbox checkout of
  `--rev` reports `governance.citation_resolves` as `PASS`.

**Kill rule.** At the base the counter must print `r69 routed defects closed 0 of 10` and exit 1
(`controls/C1-base.txt`); a base reading above 0 means the counter or an item is wrong and is fixed
**before** data. The cheapest skip control — a world that appends a bare `## Round 69` heading to
`LOG.md`, a bare `**Round 69 axis annotations**` line to `SCORECARD.md` and nothing else — must stay
below 10 (`controls/C1-skip-control.txt`). A miss is reported as a miss; no item is narrowed after data.

### C2 — depth (the lane's lowest owned axis), sourced, assimilation — skill evaluation artefacts

**Axis:** `depth` (owned, 9). **Surface:** what the open specification and its reference
implementation say about evaluating a skill: the `evals/evals.json` artefact and its generated
siblings, the with/without-skill baseline, evidence-bearing grading, script-checked assertions,
the `should_trigger` query set and its pass rule, and the one place the reference implementation's
rule differs from the specification's wording. The lane holds the skill-creator trigger loop
(S124: 20 queries, 3 runs, 60/40) but no row for the specification's own `skill-creation/`
evaluation pages and no entry on the output-quality artefact (`grep -n 'evaluating-skills\|evals.json'
corpus/SOURCES.md corpus/knowledge/*.md` → nothing at the base). Theme taken from
`/home/vgpnk/Projects/shokuknow/merge/kotoba/` (staged `spec-eval-file-format.md`, rows S234/S231),
re-grounded in-round under CORPUS.md rule 1; the reference-implementation row is lane-opened.

**Frozen predicate (the same sentence in this plan, in the counter's docstring and in the receipt):**

```
python3 -B verifiers/check_skill_evals.py --rev <rev>  ->  prints "skill eval facts backed N of 8", exit 0 when N == 8
```

Fact Fi (F1…F8) is backed when the entry `corpus/knowledge/skill-eval-artefacts-round70.md` at `--rev`
carries exactly one `| Fi |` table row whose id cell names one `S###`, whose quote cell holds a
double-quoted quote of 5–25 words containing every key term pinned for Fi in the counter, the quote
is found verbatim (after stripping Markdown `*` and backticks from the page and collapsing
whitespace) in the committed snapshot pinned for that `S###` (sha256 verified first; a tampered
snapshot is exit 2), the `S###` row in `corpus/SOURCES.md` is an 11-cell `mined` row whose `used-by`
names the entry, and the entry's `source:` line names that `S###`; AND `SKILL.md` at `--rev` cites
the entry path. `--fetch` repeats the quote match on each row's live URL (a second evidence, not
part of N).

**Kill rule.** At the base it prints `skill eval facts backed 0 of 8`, exit 1 (`controls/C2-base.txt`).
The junk control (the entry with every fact row but quotes that lack the key terms — on-page text
from the same snapshots) must print 0 of 8 (`controls/C2-junk-control.txt`); the forged control
(key terms present, quotes absent from the snapshots) must print 0 of 8
(`controls/C2-forged-control.txt`). If any control meets 8, the counter is wrong and is fixed before
data.

## Frontier step

Census before: `.ufo/waves/round-70/receipts/census-before.txt` (exit 0; 134 rows). Rows S209–S211
are opened this round (renumbered by document from the staged S234/S231; S211 lane-opened), each
with URL, access date and located quote in the lesson's `## Gate`. The mined mistake goes to
`corpus/lessons/round-70.md` § Mistakes. C2 is the sourced claim. Assimilation: one theme, one
admitted lane entry, refusals recorded with reason and flip.

## No-harm battery (run at the measured tip)

`verify_skill_checklist.py --json` (SKILL.md ≤ 600 lines), `verify_corpus_integrity.py`,
`verify_corpus_independent.py --json`, `check_gate_registry.py --rev <tip>`,
`check_assertion_floors.py`, and the census `validate` exit 0.
