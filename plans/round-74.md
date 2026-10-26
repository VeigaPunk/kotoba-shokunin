# Round 74 — plan (hyaku run 7, lane kotoba, attempt 1)

Frozen before any wave seat scored any claim. Base lane tip (branch `master`):
`1e03d1991bc02281b00a5b7a5e00c9d5d5d72908` (`jj-lane.sh state` → `local=1e03d19… remote=1e03d19… ahead=0
behind=0 tracked=0 untracked=0`; the tip is the r73 non-author closure's spot-check commit, authored by
`protocol-shokunin`). `.ufo/watchdog.log` shows one `launch kotoba round=74` line and no `lane-dead-no-report
kotoba round=74`: no earlier attempt; `.ufo/waves/round-74/` did not exist at round start (no inherited work).
The L1 holds the canonical §3 planner seat (the validator rejects `planner`); the planning data-walk rides the
wave-1 scouts and connectors. Seats write only under `.ufo/waves/round-74/`; the L1 is the one integration
owner and lands everything through `scripts/hyaku/jj-lane.sh`. Seat names carry the suffix `R74` (Q69: seat
names are unique across lanes running concurrently; the dispatcher keys handles by seat name).

Round shape: **two v1 waves** (policy `scripts/hyaku/ufo-wave-policy.json`, band 32–64 each), total 64–100.
Wave 1 — build, source opening, counter and control construction, plan attacks. Wave 2 — falsify (fresh
reviewer/critic/mutation-tester/executor seats re-run every counting command, re-open every new source row,
attack every claim and every new gate). Routing is the host role table (never a `model` argument). The run-7
dispatcher takes a `<wave>.ready` file; seats spawn in the orchestrator session.

## Before-values re-measured at round start (Q19, Q65) — base `1e03d19`, committed receipts

Receipts under `.ufo/waves/round-74/receipts/` and `assimilation/`:

| item | command | observed at base |
|---|---|---|
| census | `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` | exit 0; 148 rows `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`; 20 W04 duplicate-URL warnings (`receipts/census-before.txt`) |
| tip battery | `python3 -B verifiers/check_tip_battery.py --rev master` (L1 run, 236.6 s, `receipts/base-battery-l1.txt`) | **`tip battery exit 0: 4 of 6`, exit 1** — corpus integrity exit 1 and corpus independent exit 1 (the r73 closure's spot-check was indexed nowhere; `unindexed 1`); registry 0, floors 0 (215.5 s), checklist 0, correction sweep 0; guards 5 of 5 |
| SKILL.md weight | `wc -lc SKILL.md`; `awk 'length>300' SKILL.md \| wc -l` | 570 lines, 74,174 B, 74 lines over 300 characters (`receipts/base-sweeps.txt`) |
| sibling pins (C2) | for every `## Adjacent` row of `PROVINCE.md`: `git -C <lane>-shokunin diff --shortstat <pin> <branch> -- SKILL.md PROVINCE.md` (`receipts/sibling-staleness-base.tsv`) | 20 rows; **15 of 20 siblings' `SKILL.md` or `PROVINCE.md` differ between the row's pinned commit and the lane's branch head**; 5 are byte-equal (audio, game-dev-2d, game-dev-3d, lore, kagi); pins are 50–312 commits behind for the 15 |
| spec craft pages (C1) | `grep -nE 'agentskills\.io/skill-creation/(best-practices\|using-scripts\|quickstart)' corpus/SOURCES.md` and the rule-phrase sweep in `receipts/base-sweeps.txt` | 0 registry rows; 0 hits of `calibrating control`, `defaults, not menus`, `favor procedures`, `fragility of the task`, `one-off commands`, `pipx run`, `uvx ruff` in `corpus SKILL.md PROVINCE.md` |
| package id collision | `assimilation/{reg-ids,staged-ids,collisions}` (0–3-space pattern) | lane 148 ids, package 188 ids, **20 collisions `S203`–`S222`** (the lane's own r69–r73 rows, which the package numbered earlier); quarantine slice 13 data rows (`assimilation/quarantine-slice`) |
| harness claims (information, not a claim) | `python3 -B verifiers/verify_harness_claims.py` (126 s) | 17 of 28 checks pass, 11 DRIFT: the baseline expects the round-18 catalogue of 7 skills, the host now offers 75 (216 cache rows). `compare_harness_independent.py` times out above 250 s at 100+ CPU-minutes. Not a claim this round; recorded for the report (a volatile host fact pinned as a constant) |

## Inherited routed defects (r73 spot-check, `corpus/lessons/round-73-verifier-spotcheck.md` § 6)

1. **Falsify wave** (second time asked): wave 2 of this round, seat names ending `R74`, round total ≥ 64.
2. **Index the closure file in the first commit** — done in the plan commit (`corpus/README.md` row).
3. **D2 and D3 corrected by appended notes, never rewrites:** SKILL.md is 570 lines not 572 (command carried);
   the r73 report's M128 "green-after cited" sentence is corrected in the r74 report; `check_report_pointers.py`
   is run on the r74 report and `unresolved 0` cited.
4. **M129 structural guard:** not built this round; the "fix" label is retracted in the r74 lesson (a fix is
   counted only once shown able to fail — CORPUS additional rules).
5. **Fold C1 (r73) into `SKILL.md`:** one decision row on the cross-vendor `.agents/skills/` root and a resolvable
   path for the read-only package (`/home/vgpnk/Projects/shokuknow/merge/kotoba/`). Landed as a routed item, not a claim.
6. **`compare_harness_independent.py` exit 2:** diagnosed above (volatile host constant); L0 question appended, not a claim.
7. SHONEN boxes stay `[~]`; no non-author verifier is available to this lane.

## Claim declarations (this round declares 2, on two distinct axes)

### C1 — depth, SOURCED + assimilation: the Agent Skills `skill-creation/` guides' body-craft rules reach `SKILL.md`

**Axis:** `depth` (owned, 9; `AXES.md`: "a reader can act on SKILL.md alone; no filler"). **Surface:** the
specification's own authoring guides — `agentskills.io/skill-creation/best-practices.md`, `using-scripts.md`,
`quickstart.md` — which the lane does not hold (0 registry rows, 0 phrase hits at base; the lane holds the
sibling pages `evaluating-skills.md` S212 and `optimizing-descriptions.md` S213). **Assimilation (addendum §10):**
theme from the read-only package `/home/vgpnk/Projects/shokuknow/merge/kotoba/` — staged entry
`knowledge/corpus/knowledge/spec-script-craft-rules.md` (staged S236, S237) and the S232 best-practices row
(staged `spec-description-trigger-discipline.md` cites it); every cited page is re-opened this round and the
Gate block carries the lane's own access date and located quotes. **considerthese** (`considerthese/2026-10-25.md`
§ Self-improvement suggestions item 4, the SKILL.md frame "the two harnesses here"): worked in the same `SKILL.md`
edit as one frame sentence; recorded in the lesson, never counted by the counter. The depth move is the
consideration's own point: a knowledge entry that never reaches `SKILL.md`'s guidance is depth the executing agent cannot use.

**Frozen predicate (the same sentence in this plan, in the counter's docstring and in the receipt):**

```
python3 -B verifiers/check_spec_craft.py --rev <rev>  ->  prints "spec craft pages backed N of 3", exit 0 when N == 3
```

Page `P` ∈ {`best-practices`, `using-scripts`, `quickstart`} is **backed** at `--rev` iff all of (committed bytes
only; no network at measurement):

- **(a)** the entry `corpus/knowledge/spec-skill-creation-craft-round74.md` (frozen path) opens with `source:`
  lines for every cited id, then `verified-at:` and `recheck:`, and has exactly one row for `P` in its rule table
  carrying at least two rule tokens (backticked commands or paths, or double-quoted rule sentences of at least
  five words), each located word-bounded in the committed snapshot of `P`'s source;
- **(b)** `P`'s cited `S###` is an 11-cell registry row, status `mined`, tier `A`, host `agentskills.io`, `opened`
  equal to a round-74 date, `used-by` naming the entry, and the registry is census-conformant at `--rev`;
- **(c)** `P`'s snapshot under `.ufo/waves/round-74/snapshots/` has a sha256 equal to the pin in the committed
  manifest `snapshots/MANIFEST.sha256` (missing or tampered snapshot is exit 2);
- **(d)** the row's located quote (5–25 words) is found in `P`'s snapshot after whitespace collapse only;
- **(e)** *acted on:* the `SKILL.md` subsection `### Body craft — the specification's skill-creation guides` has at
  least two table rows citing `P`'s `S###`, each with an action cell of at least five words and at least one rule
  token that occurs in `P`'s snapshot (a row that cites a page without a token of it does not count);
- **(f)** `PROVINCE.md` § Core names the entry.

The counter also prints `held at base: 0` (the phrase sweep above), the do-nothing figure.
**Q45 census (wave 1, before data):** a seat opens the three pages and counts how many of them carry at least
two rule tokens the entry can quote; the target stays `N == 3` only if the census reaches 3, else it is lowered
**before data** in a committed addendum stating the census command and margin; lowering after data is a miss.

**Do-nothing control:** base scores `0 of 3`, exit 1 (receipt committed before data). **Shortcut controls
(committed worlds, each must score below 3):** the staged entry copied unchanged with staged ids and no registry
rows; rows appended with status `queued`; a rule token invented and absent from its snapshot; a snapshot
hand-edited with the manifest hash left; `SKILL.md` rows citing a page with tokens that occur only in a different
page's snapshot (Q37 real-text shortcut); a token-stuffed row; the entry outside `corpus/knowledge/`; staged rows
appended as-is (campaign schema — the census must reject); `SKILL.md` rows without the entry. **Kill rule:** any
shortcut world scoring 3 means the counter is wrong; fixed before data; no rule changes after any seat has scored data (Q28).
**Bound (Q26, Q51):** form, sources and tokens are counted; whether a rule sentence is true of the page is a
reviewer judgement no counter makes — assigned to named non-author wave-2 seats, their committed reviews cited.

### C2 — freshness (the lowest non-retired axis, 8; advisory): the sibling census is re-pinned and re-read at the frozen fleet heads

**Axis:** `freshness` (advisory, 8; `AXES.md`: "drift detection — skill claims re-verified against live surfaces;
stale items flagged or fixed"). **Surface:** `PROVINCE.md` § Adjacent and `corpus/knowledge/sibling-overlap-census-round49.md`
state each sibling lane's boundary at a commit pinned at round 49–50; **15 of 20** of those siblings' `SKILL.md`
or `PROVINCE.md` have since changed (`receipts/sibling-staleness-base.tsv`: kake +955, tsukuroi +872, revenger
+618 where its row says "no skill file at the pin", mori +462, kama +417, …). The Adjacent table is a claim about
today's siblings read from yesterday's bytes. Named by the surface it changes (drift detection on a pinned
record), not by the number it produces; it moves no coverage ground and adds no new knowledge ground.

**Frozen predicate:**

```
python3 -B verifiers/check_sibling_reread.py --rev <rev>  ->  prints "sibling rows re-pinned and re-read N of 20", exit 0 when N == 20
```

The frozen pins are `receipts/sibling-heads-freeze.tsv` (written by the L1 before any wave-1 seat ran; lane,
branch, head40, `SKILL.md` blob, `PROVINCE.md` blob per lane, 20 lanes). Lane `L` is **re-pinned and re-read** at
`--rev` iff all of:

- **(a)** the entry `corpus/knowledge/sibling-overlap-census-round74.md` (frozen path) has exactly one row for `L` in the
  round-49 row shape and that row passes the **base's** `check_sibling_census.py` row checks (every cell non-empty;
  quote ≥ 6 words re-read at the pinned commit within ±2 lines of its `path:line`; skill-file, names-kotoba and
  arbitration cells recomputed from the pinned `SKILL.md`; a `none` row names no `kotoba` in the sibling's
  description or `PROVINCE.md`), run from the base copy of that checker (sha256-pinned in the counter), not from
  the measured revision (Q33: the measured revision supplies bytes, not code);
- **(b)** the row's commit cell equals `L`'s head in the freeze file, and that commit is an ancestor of the lane's
  branch head at measurement;
- **(c)** the row's `delta` cell equals the counter's recomputation of `git diff --shortstat <r49 pin> <freeze head>
  -- SKILL.md PROVINCE.md` for `L` (the r49 pin is the commit in the base-revision `PROVINCE.md` row); an
  unchanged lane reads `none`;
- **(d)** `PROVINCE.md` § Adjacent at `--rev` carries `L`'s row with the same commit and classification as the entry;
- **(e)** no `none` row exists for a lane whose pinned `SKILL.md` or `PROVINCE.md` contains the whole word `kotoba`
  (recomputed by the counter).

**Do-nothing control:** base scores `0 of 20`, exit 1 (the entry does not exist). **Shortcut controls (committed
worlds, each must score below 20):** the r49 entry copied with every commit cell bumped to the freeze heads and
nothing else (quotes die at moved lines for the changed lanes); the same plus `delta` cells computed by script (a
pure carry-forward: the quotes of unchanged text re-located — this world is *measured and reported*, not
asserted below 20, because a mechanical re-pin with recomputed cells is the lowest honest re-verification of the
mechanical facts; the semantic judgments are the wave-2 seats' and carry no count); a lane row missing; a
duplicated row; a commit cell on a commit that is not the freeze head; a quote absent at the pin; `PROVINCE.md`
unchanged; a `none` row for a lane whose bytes name kotoba. **Kill rule:** any of the non-carry-forward worlds
scoring 20 means the counter is wrong; fixed before data; no rule changes after data (Q28).
**Bound (Q26, Q51):** the counter measures pin, delta, cells, quote location and the mechanical `none` rule; it does
**not** measure whether `adjacent`/`contested`/`none` is the right classification or whether a boundary sentence
reads correctly — that judgement is assigned to named non-author wave-2 seats (≥ 10 lanes independently
re-derived), disagreements recorded verbatim (Q16). Siblings keep moving after the freeze; the entry says so and
the rows are valid at their pins, not at the round end.

## Axis separability and no-harm

Distinct axes (`depth`, `freshness`); neither counter reads the other's files: C1 touches `SKILL.md` (a new
subsection and one frame sentence), `PROVINCE.md` § Core, `corpus/SOURCES.md`, `corpus/knowledge/`; C2 touches
`PROVINCE.md` § Adjacent and its entry. Each verifies with the other not landed (commit order proves it: the C2
commit is made first and measured at its own revision). No-harm battery at the tip (Q50, Q65): `python3 -B
verifiers/check_tip_battery.py --rev <tip>` in both invocation forms (`6 of 6`), census exit 0, `check_gate_registry.py`
(two new gate rows, `60 of 60`), `check_sibling_census.py` on the r49 entry and `--province`, `SKILL.md` ≤ 600 lines
(570 at base; budget stated before the edit: +14 lines for C1, +2 registry rows, +4 for routed item 5 → 590).

## Frontier step

- `corpus/SOURCES.md`: rows opened this round get the next ids after S222, renumbered **by document**; rows only
  for pages an admitted entry cites (CORPUS rule 4). Staged rows are campaign-schema and are normalised in
  scratch under `assimilation/` before any append (collision guard proved once, 0–3-space pattern).
- Quarantine slice (13 data rows): any row an admitted entry cites is hand-checked this round.
- Mined mistake: from this round or earlier, chosen at lesson time with its evidence; `captured-by` honest (Q62).
- Sourced claim: C1 (rows opened this round, `## Gate` carries URL, access date, ≤25-word located quote).

## Seat plan (L1 = planner; mapping recorded in the report)

Wave 1 — 35 seats: executors (sources ×3, counters ×2, controls ×2, heads/rows ×4, assimilation ×2, base) 16 ·
scribes 4 · scouts 11 (10 sibling readers + 1 Q45 census) · connectors 2 · critic/reviewer 2. Wave 2 — ≥ 32 seats:
reviewers, critics, mutation-testers, executors (re-run), scouts (re-open), connectors, scribes. Total ≥ 67.
