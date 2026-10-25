# Round 73 — plan (hyaku run 7, lane kotoba, attempt 1)

Frozen before any wave seat scored any claim. Base lane tip (branch `master`):
`072048fa8e8a52c707d25f7079772fa317244eb7` (`jj-lane.sh state` → `local=072048f… remote=072048f…
ahead=0 behind=0 tracked=0 untracked=0`; the tip is the r72 non-author closure's spot-check commit).
`.ufo/watchdog.log` shows one `launch kotoba round=73` line and no `lane-dead-no-report kotoba round=73`
line: no earlier attempt; `.ufo/waves/round-73/` did not exist at round start (no inherited work). The L1
holds the canonical §3 planner seat (the validator rejects `planner`); the planning data-walk rides the
wave-1 scouts and connectors. Seats write only under `.ufo/waves/round-73/`; the L1 is the one integration
owner and lands everything through `scripts/hyaku/jj-lane.sh`.

Round shape: **two v1 waves** (policy `scripts/hyaku/ufo-wave-policy.json`, band 32–64 each), total 64–100.
Wave 1 — build and first falsifiers of the frozen plan; wave 2 — falsify (fresh reviewer/critic/
mutation-tester/executor re-run seats attack what wave 1 and the L1 landed). Routing is the host role
table (never a `model` argument).

## Before-values re-measured at round start (Q19, Q65) — base `072048f`, committed receipts

Receipts under `.ufo/waves/round-73/receipts/`: `census-before.txt`, `c3-base-battery-counter.txt`,
`base-sweeps.txt`. Observed at the base, from the lane root:

| item | command | observed at base |
|---|---|---|
| census | `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` | exit 0; 142 rows `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`; 20 W04 duplicate-URL warnings |
| tip battery (C3) | `python3 -B verifiers/check_tip_battery.py --rev 072048f… --repo .` | **`tip battery exit 0: 2 of 6`, exit 1** — floors exit 1 (128 s), checklist exit 1 (4.6 s), corpus integrity exit 1, corpus independent exit 1 (the r72 spot-check is unindexed), gate registry exit 0, correction sweep exit 0; guard `instrument-size` FAIL (76 > 40, measured against the r72 base `c69711e`) |
| checklist by hand | `python3 -B verifiers/verify_skill_checklist.py` in the lane and in a fleet-shaped `git clone --shared` sandbox of `072048f` | exit 0 in both, run by the L1 (the sandbox exit-1 reading of the counter is not reproduced by hand: M127) |
| SKILL.md weight (C2) | `wc -lc SKILL.md`; `awk '/^## Gate registry/{p=1} /^## Sources/{p=0} p' SKILL.md \| wc -lc` | 568 lines, 72,715 B; the registry block is 65 lines, 21,288 B (29% of bytes); 56 registry rows `grep -cE '^\| \`' SKILL.md` |
| vendor surfaces (C1) | `grep -rniE 'trae\|codebuddy\|kimi code\|kimi-code\|zhipu\|bigmodel\|moonshot' corpus SKILL.md PROVINCE.md` | 1 hit: a host config path in `corpus/knowledge/opencode-offer-trace-round8.md:84` (not a skill-surface row); registry rows naming `docs.trae.cn`, `codebuddy.ai`, `kimi.com/code`, `moonshotai/kimi-cli`, `docs.bigmodel.cn`: 0 |
| package id collision | `.ufo/waves/round-73/assimilation/{reg-ids,staged-ids,collisions}` | lane 142 ids, package 188, **14 collisions `S203`–`S216`** (the lane's own r69–r72 rows, which the package numbered earlier) |

## Inherited routed defects (r72 spot-check, `corpus/lessons/round-72-verifier-spotcheck.md` § 6)

1. M127 sandbox-vs-hand discrepancy and the honest `instrument-size` cap → **C3**.
2. The falsify wave r72 skipped → this round's wave 2 (≥25% attack share).
3. `corpus/SOURCES.md:209-215` search-log damage → an appended correction entry (never an in-place rewrite
   of filed bytes), `census validate` exit 0 before and after.
4. `corpus/knowledge/resident-index-and-rungs-round72.md:45` ("format's,.") → a one-line repair logged in
   `LOG.md` (a lane-authored entry typo, not a claim edit; the verified-at/quote lines are untouched).
5. Receipt filenames cited by the r72 report/SHONEN (`tip-check_*` → `tip-tip_battery*`,
   `tip-substrate_repin_v2`) → a correction line in this round's report, never a rewrite of the r72 report;
   the fix that must be able to fail is the pointer gate below.
6. SHONEN boxes stay `[~]` (operator note; promotion is operator-owned).

## Claim declarations (this round declares 3, on three distinct axes)

### C1 — coverage (owned reading: advisory; frontier → core), SOURCED + assimilation: four Chinese-vendor skill surfaces

**Axis:** `coverage` (8.5). **Surface:** client skill surfaces the lane's maps (`PROVINCE.md` § Core: plugin
manifests, agent definitions, command files, hook files, scoped rules, trust gates, name precedence) do not
hold: TRAE (ByteDance), CodeBuddy (Tencent), Kimi Code (Moonshot) and Zhipu managed agents — discovery roots,
frontmatter vocabulary and where each places a skill body. **Assimilation (addendum §10):** one theme from
the read-only package `/home/vgpnk/Projects/shokuknow/merge/kotoba/` — staged entry
`knowledge/corpus/knowledge/chinese-client-skill-surfaces.md` (staged S214, S216, S217, S218, S219, S221;
renumbered by document into the lane's registry, collisions in the table above). Every cited page is
re-opened this round; the entry's Gate block carries the lane's own access date and located quotes.

**Frozen predicate (the same sentence in this plan, in the counter's docstring and in the receipt):**

```
python3 -B verifiers/check_cn_vendor_surfaces.py --rev <rev>  ->  prints "vendor skill surfaces backed N of 4", exit 0 when N == 4
```

Vendor `V` ∈ {TRAE, CodeBuddy, Kimi Code, Zhipu} is **backed** at `--rev` iff all of (committed bytes only;
no network at measurement):

- **(a)** the entry `corpus/knowledge/chinese-vendor-skill-surfaces-round73.md` (frozen path) opens with
  `source:` lines for every cited id, then `verified-at:` and `recheck:`, and has exactly one row for `V` in
  its vendor table whose backticked tokens (paths and frontmatter keys; at least three, at least one root or
  placement token and at least two keys) each occur word-bounded in the committed page snapshot of a source
  that row cites;
- **(b)** every cited `S###` is an 11-cell registry row with status `mined`, tier `A` or `B`, a `used-by`
  cell naming the entry, and a URL whose host is one of `V`'s hosts (frozen: TRAE `docs.trae.cn`; CodeBuddy
  `www.codebuddy.ai`; Kimi Code `github.com/moonshotai/kimi-cli` or `www.kimi.com`; Zhipu `docs.bigmodel.cn`);
- **(c)** each cited row has a snapshot under `.ufo/waves/round-73/snapshots/` whose sha256 equals the pin in
  the committed manifest `snapshots/MANIFEST.sha256` (a missing or tampered snapshot is exit 2);
- **(d)** each cited row's located quote (5–25 words) is found in its snapshot after whitespace collapse only.

The counter also prints `held at base: 0` (host strings in the base registry), the do-nothing figure.
**Q45 census (wave 1, before data):** a seat opens all pages and counts which vendors the live pages can back;
the target stays `N == 4` only if the census reaches 4, else it is lowered **before data** in a committed
addendum stating the census command and margin; lowering after data is a miss.

**Do-nothing control:** the base scores `0 of 4`, exit 1 (receipt committed before data). **Shortcut controls
(committed worlds, each must score below 4):** the staged entry copied unchanged with staged ids and no
registry rows; rows appended with status `queued`; a root path invented and absent from the snapshot; a
snapshot hand-edited with the manifest hash left; a token-stuffed row; the entry outside `corpus/knowledge/`;
staged rows appended as-is (campaign schema — the census must reject). **Kill rule:** any shortcut world
scoring 4 means the counter is wrong; fixed before data; no rule changes after any seat has scored data (Q28).

### C2 — depth (the lowest owned axis, 9): the gate registry leaves the guidance file

**Axis:** `depth` (owned, 9; `AXES.md`: "a reader can act on SKILL.md alone; no filler"). **Surface:**
`SKILL.md` § Gate registry — 65 lines, 21,288 B of reference table the executing agent never needs to audit a
skill — moves to `verifiers/REGISTRY.md` with a pointer. **Source:** `considerthese/2026-10-25.md` §
Self-improvement suggestions item 2 (the one proposal worked this round; its item 1 appears only as this
claim's byte threshold, not as a standing guard, and items 4–5 stay open).

**Frozen predicate:**

```
python3 -B verifiers/check_skill_weight.py --rev <rev>  ->  prints "SKILL.md weight B bytes (ceiling 56000); registry rows R of R conformant; boxes K of 45; sections S of S", exit 0 when B <= 56000 and every count is full
```

At `--rev`: `B` is the byte size of `SKILL.md`; `R` counts rows of `verifiers/REGISTRY.md` for which the tree's own
`check_gate_registry.py --rev <rev>` reports a conformant row (the counter runs that gate from a `git
archive` extraction and recomputes row/file coverage itself: every `verifiers/check_*.py` and gate script the
base registry named has a row, no phantom row); `K` counts `- [ ]` boxes of `SKILL.md` that the base's 45
box texts (`verifiers/checklist-baseline.json`) still match; `S` counts the base's `## ` headings still
present (the `## Gate registry` heading stays with a pointer body of at most 3 lines). Rows the round adds for
its own new gates count in `R`.

**Do-nothing control:** base scores `B = 72715 > 56000`, exit 1 (receipt committed before data).
**Shortcut controls (committed worlds, each must read below full):** delete the registry block (bytes drop,
`R` reads 0); move it to a file the gate does not read (`R` reads 0 of 56); delete 17 KB of guidance instead
(`K` or `S` drops); minify whitespace to the ceiling (`K` drops); keep the block and add a pointer (B stays
high). **Kill rule** as C1.

### C3 — consistency (calibration sub-axis, owned, 10): the tip battery counter agrees with the hand run

**Axis:** `consistency` (owned, 10; held). **Surface:** `verifiers/check_tip_battery.py` and the gates it runs —
the r72 receipts record `4 of 6` while the same gates by hand exit 0 (M127), a counter that disagrees with
its own gates is not a measurement (`corpus/lessons/round-72-verifier-spotcheck.md` § 6.1).

**Frozen predicate:**

```
python3 -B verifiers/check_tip_battery.py --rev <rev>  ->  prints "tip battery exit 0: N of 6", exit 0 when N == 6 and every guard passes, in each of two consecutive runs on fresh sandboxes
```

The six frozen commands are the r72 set (`check_gate_registry.py --rev <rev>`, `check_assertion_floors.py`,
`verify_skill_checklist.py`, `verify_corpus_integrity.py`, `verify_corpus_independent.py`,
`check_correction_sweep.py --root .`), run from a fleet-shaped sandbox of `<rev>`. **The measured cause** of the
`2 of 6` base reading is named by wave 1 (the cause, a red-before command and the one-line delta that clears
it, Q63/M116 — a fix counts only once shown able to fail); the `instrument-size` guard, whose cap measured
against the r72 base punishes an honest repair, is re-set by a committed addendum before any C3 data with the
arithmetic stated (Q65) — the weakening-resistance stays in the `instrument-pin`, `floors`, `no-deletions`
and `spotcheck-identity` guards plus the per-gate red anchors the shortcut worlds exercise.

**Do-nothing control:** the base scores `2 of 6`, exit 1 (`receipts/c3-base-battery-counter.txt`).
**Shortcut controls (committed worlds):** delete the r72 spot-check and re-record the baseline (must fail the
identity guard); replace a gate by a stub `sys.exit(0)` (must fail the pin guard); lower a floor to hide a red
self-test (must fail the floors guard); bless the corpus DRIFT values without indexing the spot-check file
(must leave integrity red); raise the gate timeout / skip the failing gate in the counter (must read `N < 6`
or exit 2); a counter run whose second sandbox disagrees with its first (must not count the gate).
**Kill rule** as C1.

## Frontier step

Census before: `receipts/census-before.txt` (exit 0; 142 rows; 20 W04). C1 is the sourced claim (rows opened this
round, Gate quotes in `corpus/lessons/round-73.md`). **Mined mistake** (`corpus/lessons/round-73.md` §
Mistakes): the r72 report and SHONEN cited receipt files that do not exist and the r72 search-log note was
split mid-sentence — class `reference-drift`, captured by none for report files (`verify_corpus_integrity.py`
resolves lane-tree citations, not the fleet report's); the fix is `verifiers/check_report_pointers.py` — it
resolves every backticked `.ufo/waves/…`, `receipts/…`, `corpus/…`, `verifiers/…` token of a report against the
lane tree at a revision — shown able to fail by running it on the **r72 report at the r72 tip** (exit 1,
naming the `tip-check_*` tokens) before it is run on the r73 report at the r73 tip (exit 0).

**Assimilation:** theme = four Chinese-vendor skill surfaces (C1). Id collision check, guard proof, normalized
append block and validated scratch mirror under `.ufo/waves/round-73/assimilation/`; renumber **by document**.
Per-entry gates: PROVINCE scope (client skill surfaces and frontmatter are Core; translation or market
commentary is not), QUALITY bar, expansion only on ground the coverage map did not hold. A second staged entry
is admitted only if its rows are cited and survive the same gates. Quarantine: the kotoba register slice
(13 rows, re-derived at `assimilation/quarantine-slice`; hand-checked in r72, verdicts in
`corpus/lessons/round-72.md` § Gate) holds no row any admitted entry cites — none is appended.
**considerthese:** C2 (item 2 above). Never edited.

## No-harm battery (run at the measured tip, receipts committed)

The six C3 gates, `check_substrate_pins.py`, `verify_surfaces.py`, `compare_harness_independent.py`,
`check_province_core.py`, `check_sibling_census.py` against the census file, `check_author_rules.py`,
`check_substrate_repin_v2.py`, `sources-census.sh validate` exit 0, SKILL.md under its line budget; each run
once at the measured tip, output committed with `measured-rev`.
