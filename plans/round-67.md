# Round 67 — plan (hyaku campaign, lane kotoba, attempt 1)

Frozen before any wave seat scored either claim. Base lane tip (branch `master`):
`2a8eba56b3f9321b70c569fa2816d42237ca49a2` (read with `jj-lane.sh state`; git HEAD is
detached after the helper commits — the branch tip is the pinned base).

Round shape: **two v1 waves** (policy `scripts/hyaku/ufo-wave-policy.json`, band 32–64),
wave 1 build 32 seats, wave 2 falsify 32 seats dispatched only if wave 1 yields ≥32 distinct
attack items. Both waves are validated before dispatch and dispatched as ONE batched call each.
The L1 holds the canonical §3 planner seat (the validator rejects a `planner` seat).

## Claim declarations (1–3 claims; this round declares 2)

### C1 — consistency (calibration sub-axis) — the routed r66 index repair

**Axis:** `consistency` (this lane's declared sub-axis of `calibration`; owned).
**Routed cause:** the hyaku run card
`/home/vgpnk/Projects/shokunin/.ufo/waves/hyaku/inline-run-20261023.md:181-185` records that
kotoba r66's post-closure corpus-integrity observation is red at tip `2a8eba56` "because the
closure spot-check is an unindexed corpus file", and routes the issue to r67 ("not retroactively
applied"). The unindexed file is `corpus/lessons/round-66-verifier-spotcheck.md` (written by the
hyaku closure, never edited by the lane).

**Frozen predicate (two conjuncts, one command each, same sentence in this plan, in the counter's
code and in the receipt):**

```
python3 -B verifiers/verify_corpus_integrity.py      -> prints "9/9 checks pass", exit 0
python3 -B verifiers/verify_corpus_independent.py --json -> exit 0
```

**Before (measured at the base `2a8eba56`, receipt `controls/C1-base.txt`):**
primary `5/9 checks pass`, exit 1 —
`DRIFT corpus.index.tracked_files: observed=119 expected=118`,
`DRIFT corpus.index.unindexed: observed=1 expected=0 / empty`,
`DRIFT corpus.pointers.report_total: observed=82 expected=79`,
`DRIFT corpus.pointers.commit_total: observed=38 expected=37`,
and `unindexed: corpus/lessons/round-66-verifier-spotcheck.md`;
independent gate exit 1.

**Repair (the only admitted shape):** one coverage-map index row for the r66 closure spot-check in
`corpus/README.md` (same shape as the r60/r61 rows already there, which name the closure author
and the round) **plus** a re-record of `verifiers/corpus-baseline.json` to the census values
re-derived by running the gate's own measurement — the lane's established mechanism (rounds 11,
12, 23, 46, 66). No existing row is edited; `corpus/SOURCES.md` gains rows by append only.

**Do-nothing controls (pre-data, committed under `controls/`):**

| control | world | expected verdict |
|---|---|---|
| K1 | the base tree, no repair | red (exit 1, `unindexed=1` + 3 drifts) |
| K2 | index row added, baseline NOT re-recorded | still red (3 census drifts remain) |
| K3 | baseline re-recorded, index row NOT added | still red (`corpus.index.unindexed observed=1`) |

K2 and K3 each hold half the repair and fail the predicate, so neither half alone — and no
"do nothing" world — reaches `9/9` + exit 0.

**Kill rule:** if either conjunct is false at the measured tip, C1 is a **miss as declared** and
is reported as such. No post-hoc predicate change (AXES/§9; QUALITY Q28).

**Bound:** the counters are the lane's own gates; they read committed bytes plus the working
tree. The baseline re-record is derived from the gate's own printed measurement, not hand-set.

### C2 — depth (the lane's lowest owned axis) — the instruction authority ladder, sourced

**Axis:** `depth` (owned; lowest owned axis — `consistency` is 10, `depth` is 9; both are owned,
so the lowest owned axis is `depth`. The all-axes reading — freshness/adjacency 8.0 — remains the
lane's open L0 question and is not resolved by this round; the round states both readings).

**Target surface:** the instruction-authority layer — what a skill body may assert and at whose
authority level — a craft layer the lane's corpus did not hold before this round. It lands as a
knowledge entry plus the `corpus/SOURCES.md` rows it cites, re-grounded in-round (every cited
source re-opened by this round, with this round's access date and a ≤25-word located quote).

**Frozen predicate (one command over committed bytes, same sentence in plan, code and receipt):**

```
python3 -B verifiers/check_instruction_authority.py --rev <rev>
   -> prints "authority ladder grounded 1 of 1", exit 0
   -> at the base 2a8eba56b3f9321b70c569fa2816d42237ca49a2: prints "authority ladder grounded 0 of 1", exit nonzero
```

**What the counter reads (content, not names — QUALITY Q25/Q26):** for
`corpus/knowledge/instruction-authority-ladder-round67.md` at `<rev>` — (1) the file exists;
(2) it opens with `source:` lines naming at least one `S###` id; (3) every cited id resolves to a
row in `corpus/SOURCES.md` at `<rev>` whose `status` is `mined`; (4) each cited row's `source`
URL occurs verbatim in the entry's `source:` line for that id; (5) the entry carries a
`verified-at:` line dated `2026-10-24` and a `recheck:` line; (6) the entry's located quote
(≤25 words) for each cited id occurs in that SOURCES row's `anchor` cell; (7) the entry is
indexed in `corpus/README.md`'s coverage map at `<rev>`.

**Do-nothing control (pre-data, committed under `controls/`):** a junk entry — real bytes at the
same path shape, but with no resolvable `S###` id, no `verified-at:` line and no coverage-map
index row — is rejected by the same counter (exit 1). A copied file therefore cannot meet the
predicate.

**Kill rule:** if the counter does not print `1 of 1` at the measured tip, or if the base control
does not print `0 of 1`, C2 is a **miss as declared**.

**Sourced claim (CORPUS/§2b):** the entry cites the `S###` rows opened this round; those rows
carry this round's access date, the ≤25-word located quote and the anchor.

**Bound:** the counter checks admission shape and citation resolution, not the truth of the
prose; the prose's correctness is the review seats' and the outside closure's judgement.

## Frontier step (§2b of the canonical contract)

- **SOURCES curation:** rows are written only for sources opened this round. The round's new rows
  are the assimilated package's rows, re-grounded by this round (access date `2026-10-24`, quote
  located by this round). Every `status` / `recheck` / `used-by` change is logged old→new in the
  lesson.
- **Census before → after:** `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`,
  run at round start and round end; both outputs and exit codes are pasted into the report.
  Before: `.ufo/waves/round-67/census-before.txt`, exit 0, 120 rows, 16 W04 notices.
- **Mined mistake:** `corpus/lessons/round-67.md` `## Mistakes` — class · evidence pointer ·
  captured-by · fix; a fix counts only once shown able to fail.
- **Sourced claim:** C2 (above).

## Assimilation (item 10 of the round prompt) — one theme

- **Theme:** the instruction-authority ladder and the boundary it draws around skill bodies.
- **Package (read-only):** `/home/vgpnk/Projects/shokuknow/merge/kotoba/` — `MERGE-REPORT.md`
  (164 staged rows, first staged id `S123`; the lane registry holds 120 rows), `SOURCES.append.md`,
  `knowledge/corpus/knowledge/*.md`. Nothing in that tree is written, committed or run.
- **Entries admitted:** 1–3 entries on that one theme, each gated by PROVINCE.md scope and
  QUALITY.md, each re-grounded in-round.
- **Rows appended:** only the rows the admitted entries cite, transformed to the fleet schema
  (recheck → a valid ISO date / `NNd` / symbolic cadence; the stripped prose is recorded in the
  lesson's Gate block; no literal or escaped `|` in any cell; `used-by` lists exactly the admitted
  entries citing the row; status `mined`).
- **Id collision check in scratch**, with the 0–3-space pattern, before any append:
  `grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}'` over the registry and the staged set; `comm -12`
  gives the collisions; a nonempty set is renumbered in scratch and every adopted citation is
  re-pointed **by document** (the URL/anchor is the evidence; the id follows it).
- **Validate before append:** the append block is built in scratch, the lane is mirrored in scratch
  and gated with `scripts/sources-census.sh validate --file <scratch>/corpus/SOURCES.md`; exit 0
  (warnings allowed) before the first registry append.
- **Quarantine:** kotoba is not one of the wave-4 quarantine-first lanes (tabi, revenger, chousa,
  kotodama), so this round is a normal assimilation round. The absent-defect register slice for
  kotoba is derived in scratch for the record; no register row is appended this round, so no
  register row is hand-checked and adopted.
- **considerthese:** at most one still-unimplemented proposal is mined from the latest file
  (`considerthese/2026-10-23.md`), grounded through the lane's own bar, and lands as a
  QUALITY.md criterion or lesson citing that file and date. The file is never edited.

## Round shape and honesty

- Wave 1 (build, 32 seats, v1 band 32–64): executor 7, scout 8, scribe 4, reviewer 4, critic 3,
  connector 2, mutation-tester 2, sentinel 1, revenger 1. Attack roles 10 of 32 (31%).
- Wave 2 (falsify, 32 seats, v1 band 32–64): dispatched only if wave 1 yields ≥32 distinct attack
  items; seats are fresh and each names what it attacks.
- Actual seats, reports, roles and dead seats are recorded as observed; a prepared wave is never
  counted as dispatched.
- The wave context carries the absolute-path rule, the `Report:` trailer rule, the write-scope
  bound, the tool-install rule (`/home/vgpnk/.omp/agent/RULES.md` first) and the paused-pacman
  guard, verbatim.

## Inherited state (resolved under this round's entry, named in the report)

- `.ufo/waves/round-65/w1/*.md` and `.ufo/waves/round-66/w1/*.md` — lane-authored seat reports
  left untracked by their rounds. Committed here as wave evidence; their content is not edited.
- `.ufo/waves/round-65/w1/swarm-registry.json`, `.ufo/waves/round-66/w1/swarm-registry.json` —
  the `record` step's agent-id fill-in, a content change on tracked lane evidence. Committed here.
- `.ufo/round-46/**` and `SKILL.md` — working-tree mode drift (100644 → 100755) with no content
  change; reverted by rewriting the file mode from the branch tip, not committed.
