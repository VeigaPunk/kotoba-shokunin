---
author: kotoba L1 (hyaku run 7, round 72, attempt 1)
date: 2026-10-25
round: 72
lane: kotoba
---

# Round 72 — lesson (kotoba, hyaku run 7)

*Skeleton, wave 1 (build). Every `<<…>>` cell is a value only a later measurement may fill; no
number in this file is estimated. Base `c69711ee08279609374d895bb0f3c8c18ccf15c9`; claims frozen in
`plans/round-72.md` at `7b229a1889bd87d53902150d4f4658dc0c1117b6` (round-start battery table:
`.ufo/waves/round-72/receipts/base-battery.txt`, `measured-rev: c69711e…`).*

## Claims

Three claims on distinct axes. Each predicate sentence is copied from the frozen plan and is not
re-worded; no rule changes after any seat has scored data.

### C1 — depth (owned, 9), sourced + assimilation: author-facing rules reach the audit checklist

Frozen predicate (`plans/round-72.md:76`):

```
python3 -B verifiers/check_author_rules.py --rev <rev>  ->  prints "author-facing rules in SKILL.md N of 4", exit 0 when N == 4
```

Rules and their frozen entries: **A1** name uniqueness — `corpus/knowledge/skill-name-precedence-round69.md`
(S203–S207); **A2** authority level — `corpus/knowledge/instruction-authority-ladder-round67.md`
(S123, S129); **A3** install-path trust — `corpus/knowledge/client-trust-gates-round68.md`
(S198–S202, S208); **A4** rung — `corpus/knowledge/resident-index-and-rungs-round72.md`
(`<<renumbered ids>>`). Insertion surface: `## Trigger-fidelity checklist` (`SKILL.md:253`), which
ends at the next `## ` heading (`SKILL.md:328`); `SKILL.md` is 600 lines / 72,688 B at the base
(`receipts/base-battery.txt`, last line), so each new box frees its own lines first.

- **Do-nothing control (the plan's declaration, not yet measured):** `0 of 4`, exit 1 at `c69711e`
  — receipt `<<receipts/C1-base.txt, measured-rev>>` committed before data.
- **Shortcut controls (Q37, each must score below 4):** token-stuffed boxes citing `queued` rows;
  boxes citing rows whose `used-by` omits the entry; boxes inside an HTML comment or a fence; boxes
  outside the checklist section; an A4 quote absent from its snapshot; an entry without the
  provenance trio; a tail naming an id that resolves in no registry row — `<<paths and scores>>`.
- **After:** `<<N of 4>>`, exit `<<0|1>>` at `<<tip rev>>` — `<<receipt path>>`.

### C2 — freshness (advisory, 8): the host substrate re-derived and re-pinned

Frozen predicate (`plans/round-72.md:118`):

```
python3 -B verifiers/check_substrate_repin_v2.py --rev <rev>  ->  prints "host substrate re-derived: pins OK k/3; surfaces pass p of 7; removal ledger l of l verified", exit 0 when k == 3 and p == 7 and the ledger conjunct holds
```

- **Do-nothing control:** base `c69711e` → `surfaces pass 0 of 7 … pins OK 0/3`
  (`receipts/base-outputs/check_opencode_repin.out:1`; `measured-rev: c69711e…`).
- **Q45 population census (before data, no content written):** `<<k of 7 checks reachable on the
  v2.1.4 dump>>` — `<<census path + command>>`. If the census does not reach 7, the target is
  lowered in a committed addendum to `plans/round-72.md` **before** data, with the margin stated.
- **Shortcut controls (each must not read exit 0):** a re-pin that edits only the baseline shas and
  paths and leaves OC-1…OC-6 unchanged (`p < 7`); a world that ledgers every opencode class (the
  exact-set conjunct fails); a stub file at the pinned opencode path whose sha is pinned (extraction
  vacuity); `omp.real` pinned with `omp_binary_mtime` left at the old value — `<<paths and scores>>`.
- **After:** `pins OK <<k>>/3; surfaces pass <<p>> of 7; ledger <<l>> of <<l>> verified`, exit
  `<<0|1>>` at `<<tip rev>>` — `<<receipt path>>`.

### C3 — consistency (owned, 10): the lane's own tip battery matches the record

Frozen predicate (`plans/round-72.md:153`):

```
python3 -B verifiers/check_tip_battery.py --rev <rev>  ->  prints "tip battery exit 0: N of 6", exit 0 when N == 6
```

- **Do-nothing control:** base `2 of 6`, exit 1. The six frozen commands at `c69711e`:
  `check_gate_registry.py --rev` 1, `check_assertion_floors.py` 1, `verify_skill_checklist.py` 0,
  `verify_corpus_integrity.py` 1, `verify_corpus_independent.py` 1, `check_correction_sweep.py
  --root .` 0 (`.ufo/waves/round-72/receipts/base-battery.txt`).
- **Guards the counter makes itself (Q33):** no tracked `corpus/`, `verifiers/` or `SKILL.md` path
  deleted at `<rev>`; no `verifiers/floors-registry.json` floor lower than the base; the six
  instrument scripts change by at most 40 added lines in total over the base; the non-author
  `corpus/lessons/*-verifier-spotcheck.md` files byte-identical to the base — `<<receipt path>>`.
- **Shortcut controls (each must not read 6):** delete the r71 spot-check file and re-record the
  baseline (no-deletion/identity guard); stub `check_gate_registry.py` with `sys.exit(0)` (size cap);
  lower the checklist floor to the observed 1862 minus its failure (floors guard); bless the five
  DRIFT baseline values without indexing the file (`verify_corpus_integrity.py` stays red) —
  `<<paths and scores>>`.
- **After:** `<<N of 6>>`, exit `<<0|1>>` at `<<tip rev>>` — `<<receipt path>>`.

## Gate

**Id collision result** (re-derived this round, not inherited). The lane registry holds **139** ids
(`.ufo/waves/round-72/assimilation/reg-ids`; the base census agrees — `receipts/census-before.txt`
`rows: 139`), the package stages **188** (`staged-ids`), and their intersection is **11** ids:

```
$ comm -12 <(sort reg-ids) <(sort staged-ids) | tr '\n' ' '
S203 S204 S205 S206 S207 S208 S209 S210 S211 S212 S213
```

All eleven collisions are lane rows of rounds 69–71 that the package numbered before those rounds
landed (r70 § Gate recorded the same hazard for S209–S211). The two theme entries' staged ids —
`S248`, `S254`, `S255`, `S256`, `S261`–`S264` — do not collide; the lane ceiling is `S213`.

**Guard proof** (0–3-space row pattern against the column-zero pattern on the same file):

```
$ grep -cE '^ {0,3}\| S234 \|' assimilation/guard-proof/SOURCES-with-indented-S234.md
1
$ grep -cE '^\| S234 \|' assimilation/guard-proof/SOURCES-with-indented-S234.md
0
```

The fixture is committed (`assimilation/guard-proof/SOURCES-with-indented-S234.md`); its *output*
file is not, so both counts above are this draft's own run (the second `grep` exits 1 on a zero
count by design). `<<L1: commit the output file or keep these two lines as the proof>>`.

**Renumber map, by document** — the URL is the evidence and the id follows it (`CORPUS.md:89`:
"`S` + 3 or more digits, the next unused; never reused"; the next unused at the base is `S214`):

| staged id | document (URL) | lane id |
|---|---|---|
| S248 | `https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals` | `<<S2__>>` |
| S254 | `https://research.trychroma.com/context-rot` | `<<S2__>>` |
| S255 | `https://agentskills.io/skill.md` | `<<S2__>>` |
| S256 | `https://agentskills.io/client-implementation/adding-skills-support.md` (the lane holds this page as **S002**, `corpus/SOURCES.md:15`) | `<<S2__>>` |
| S261 | `https://docs.letta.com/letta-code/skills/` | `<<S2__>>` |
| S262 | `https://docs.factory.ai/cli/configuration/skills` | `<<S2__>>` |
| S263 | `https://raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/docs/skills.md` | `<<S2__>>` |
| S264 | `https://hermes-agent.nousresearch.com/docs/user-guide/features/skills` | `<<S2__>>` |

**Rows opened this round** (`<<count>>`; `CORPUS.md:112-115` — every new row carries its URL, the
access date and a ≤25-word quote with its location grounding `teaches`; every word count carries its
`wc -w` command on the same line, Q54):

| lane id | URL | accessed | located quote (≤25 words) | tier | status | used-by |
|---|---|---|---|---|---|---|
| `<<S2__>>` | `<<url>>` | `<<YYYY-MM-DD>>` | "`<<quote>>`" (`<<n>>` words, `<<wc -w command>>`) | `<<A\|B>>` | mined | `<<repo-relative entry>>` |

**Admitted (`<<n>>` lane entries):** `<<entry filename>>` — **admit**, re-grounded: `<<which
claims were re-opened, on which row, this round>>`. PROVINCE scope: `<<prompt and skill craft |
refused per the reason below>>`. QUALITY: `<<tier, located quotes, count-carrying recheck>>`.

**Refused (reason → flip):** `<<one bullet per refusal; the reason is an observed fact (a quote
absent, an anchor wrong, a scope mismatch), never an assertion about what a source lacks (Q62)>>`.

- `<<staged id / entry>>` — `<<observed fact with its command>>`. Flip: `<<condition>>`.

**Assimilation provenance gap to close on admission** (observed in the staged bytes): staged
`context-rot-and-always-on-context.md` cites S255 at its line 27 and S256 at its line 29, while its
`source:` lines (3–4) name only S254 and S248 — so the admitted entry must gain a `source:` line per
cited id, which is also C1's conjunct (c). `<<carried / corrected at admission>>`

**Quarantine verdict table** — the register slice for `kotoba`, 13 rows
(`assimilation/quarantine-slice-full.txt`, re-derived at round time; no refused row is appended):

| # | campaign id | round | class | URL | verdict | reason / flip |
|---|---|---|---|---|---|---|
| 1 | S151 | round3 | `payload-absent` | `https://agentskills.io/skill-creation/optimizing-descriptions.md` | `<<verdict>>` | `<<r70 hand-check refused S151 — confirm or supersede>>` |
| 2 | S167 | round4 | `payload-absent` | `https://agentskills.io/client-implementation/adding-skills-support.md` | `<<verdict>>` | `<<reason>>` |
| 3 | S168 | round5 | `payload-absent` | `https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals` | `<<verdict>>` | `<<same document as staged S248 — check both claims>>` |
| 4 | S172 | round5 | `payload-absent` | `https://junie.jetbrains.com/docs/agent-skills.html` | `<<verdict>>` | `<<reason>>` |
| 5 | S176 | round5 | `payload-absent` | `https://agentskills.io/client-implementation/adding-skills-support.md` | `<<verdict>>` | `<<reason>>` |
| 6 | S180 | round6 | `payload-absent` | `https://web.archive.org/web/2026/https://ai.google.dev/gemini-api/docs/coding-agents?hl=ja` | `<<verdict>>` | `<<reason>>` |
| 7 | S185 | round6 | `payload-absent` | `https://docs.roocode.com/features/skills` | `<<verdict>>` | `<<reason>>` |
| 8 | S236 | round10 | could not be fetched | `https://skills.sh/docs` | `<<verdict>>` | `<<reason>>` |
| 9 | S237 | round10 | could not be fetched | `https://skills.sh/audits` | `<<verdict>>` | `<<reason>>` |
| 10 | S238 | round10 | could not be fetched | `https://code.claude.com/docs/en/security.md` | `<<verdict>>` | `<<reason>>` |
| 11 | S239 | round10 | could not be fetched | `https://skills.sh/agent` | `<<verdict>>` | `<<reason>>` |
| 12 | S243 | round10 | could not be fetched | `https://skills.sh/docs/api` | `<<verdict>>` | `<<reason>>` |
| 13 | S169 | round5 | could not be fetched | `https://ai.google.dev/gemini-api/docs/coding-agents` | `<<verdict>>` | `<<reason>>` |

**Census gate before the first append:** `<<scratch mirror path + validate exit>>`; round-end census:
`<<receipts/census-after.txt, exit>>`.

**considerthese item 3** (`considerthese/2026-10-25.md:21`, operator-authored, never edited) — "Route
each knowledge entry's 'what a skill author does' bullets into the audit checklist", grounded by
"A knowledge entry that never changes the checklist is depth the agent can't use." (14 words;
`grep -o "A knowledge entry that never changes the checklist is depth the agent can't use."
considerthese/2026-10-25.md | wc -w` → `14`). Implemented this round as C1's four rules.
`<<verdict: implemented / implemented-bounded / not implemented, with the measurement>>`

**For the non-author spot-check:** `<<suggested admit sample and reject sample>>`.

## Mistakes

- **M124 — class: `stale-premise` (record-vs-tree).** Evidence: `plans/round-71.md:171` promised
  `check_gate_registry.py --rev <tip>` "(53 of 53)", and the r71 plan's own battery section names the
  arithmetic ("two blank lines are consumed for the two new registry rows", `plans/round-71.md:169-170`);
  the base reads `gate registry rows conformant 51 of 53 lane verifiers; phantom 0`
  (`.ufo/waves/round-72/receipts/base-outputs/check_gate_registry.out`, last line) and the two rows
  never existed — `git log --oneline -S'check_skill_evals_v2' -- SKILL.md` prints nothing and
  `git show 53d7019:SKILL.md | grep -c 'check_skill_evals_v2\|check_r69_routed_repairs_v2'` prints
  `0`. The promised battery was not run at its own tip either: the r71 report's battery
  (`.ufo/reports/round-71/kotoba.md:53-56`) runs three of the plan's six items and omits
  `verify_corpus_independent.py`, `check_gate_registry.py` and `check_assertion_floors.py`, while
  `SKILL.md` sat at 600 lines / 72,688 B (`receipts/base-battery.txt`, last line) — a row add that
  needed freed lines and freed none. Captured by: `none` in `corpus/QUALITY.md` — Q19 binds a carried
  **before**-value, not a promised **after**-value, and no row required a plan's own battery to be
  run at its own base or a promised row add to be checked against the file's ceiling.
  **Fix (shown able to fail):** this round's battery is run at the base and committed before the
  plan froze (`receipts/base-battery.txt`, `measured-rev: c69711e…`), and C3's counter recomputes the
  six-gate `N` at `--rev` — the six exits in that receipt give `2 of 6` by hand, and the counter's
  own base receipt is `<<C3 base receipt>>`; tip `<<N of 6>>` (`<<tip receipt>>`). The criterion is
  QUALITY **Q65** (drafted this round; row text in
  `.ufo/waves/round-72/w1/build/ScribeLessonSkeleton/Q65-row.md`).
- **M125 — class: `reference-drift` (a self-test arm pinned to a state an erratum changed).**
  Evidence: `verifiers/verify_skill_checklist.py:2522-2525` still asserts `status == "FAIL"` and
  `"LOG.md:2678" in detail`; the r71 errata row at `:406-415` (`GOVERNANCE_ERRATA_HORIZON = 2678`,
  `:400`) excuses that same token, and `check_governance_citations` defaults to the live tuple
  (`:1752`), so the live check returns PASS and the arm is the one failure —
  `FAIL checklist observed=1862 floor=1862 self_test_failures=1`
  (`receipts/base-outputs/check_assertion_floors.out:5`). Both bytes are present at the r71 tip and
  unchanged at the base: `git show 53d7019:verifiers/verify_skill_checklist.py | grep -n
  'GOVERNANCE_ERRATA_HORIZON = \|only LOG.md:2678 red'` → lines 400 and 2522; `git diff --stat 53d7019
  c69711ee08279609374d895bb0f3c8c18ccf15c9 -- verifiers/verify_skill_checklist.py` empty. Captured
  by: QUALITY Q50 — the r71 report states its tip battery as three gates at tip `53d7019`
  (`.ufo/reports/round-71/kotoba.md:51-56`) with no committed receipt for the plan-listed floors gate
  (`plans/round-71.md:172`), so the red had no tip receipt to contradict it (Q36 is adjacent: it
  binds a *cited* receipt's revision, not an omitted gate). **Fix (shown able to fail):** C3's six
  frozen commands include `check_assertion_floors.py`; at the base it exits 1 and C3 reads `2 of 6`,
  and the arm is corrected by `<<the landed diff and its receipt>>` with the assertion count held at
  1862 (`<<receipt>>`).
- **M126 — class: `stale-premise` (Q09: a substrate move left freshness red with no rebaseline).**
  Evidence: at the base five substrate instruments are red — `check_substrate_pins` exit 2
  (`DRIFT 3/3 pins failed`), `verify_surfaces` exit 2 (`opencode binary not found`),
  `verify_harness_claims` exit 2 (`template anchor occurs 0x in /home/vgpnk/.local/bin/omp`),
  `check_opencode_repin` exit 1 (`surfaces pass 0 of 7 … pins OK 0/3`),
  `compare_harness_independent` exit 2 (`receipts/base-battery.txt`; the plan's C2 says "four
  instruments", the battery lists five — `<<reconcile at landing>>`). The last freshness re-pin on
  the card is round 53 (`SCORECARD.md:32`), so the span with no freshness receipt is
  `<<N rounds — the seat brief states 14; this draft derived only "since round 53" and does not
  invent the count>>`. Captured by: QUALITY Q09 — "A substrate rebuild makes freshness red until the
  extraction is re-derived and re-pinned; 'no rebaseline' is open debt, not a pass" (`QUALITY.md:20`);
  the debt was carried as prose across rounds and never ran as a claim. **Fix (shown able to fail):**
  C2's counter recomputes the ledger conjunct; the base red is the r53 counter's line
  `surfaces pass 0 of 7 … pins OK 0/3` (`receipts/base-outputs/check_opencode_repin.out:1`), the new
  counter's own base receipt is `<<C2 base receipt>>`, and the tip reads `<<k/p>>`
  (`<<C2 tip receipt>>`).

## Status changes

- `<<new rows>>` — `mined` at landing (`<<date>>`), tier `<<A|B>>`, recheck `<<cadence>>`, `used-by
  <<repo-relative paths>>`.
- `<<prior row>>` — `<<cell>>` old → new: `<<old>>` → `<<new>>` (an in-place cell `CORPUS.md:116-118`
  allows; logged here).
- `<<entry superseded / withdrawn>>` — `<<what and why>>`.
- No other prior row's cell changed this round (`git diff <base> <tip> -- corpus/SOURCES.md`).
