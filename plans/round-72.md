# Round 72 — plan (hyaku run 7, lane kotoba, attempt 1)

Frozen before any wave seat scored any claim. Base lane tip (branch `master`):
`c69711ee08279609374d895bb0f3c8c18ccf15c9` (`jj-lane.sh state` → `local=c69711e… remote=c69711e…
ahead=0 behind=0 tracked=0 untracked=0`; the tip is the r71 non-author closure's spot-check commit).
`.ufo/watchdog.log` shows one `launch kotoba round=72` line and no `lane-dead-no-report kotoba
round=72` line: no earlier attempt, no inherited uncommitted lane work (`git status --porcelain`
empty at round start).

Round shape: **two v1 waves** (policy `scripts/hyaku/ufo-wave-policy.json`, band 32–64 each),
total 64–100. **Wave 1 — build** (recon, source opening, quarantine hand-checks, counter and
control-world drafts); **wave 2 — falsify** (fresh reviewer/critic/mutation-tester seats attack what
wave 1 produced and the L1 integrated). The L1 holds the canonical §3 planner seat (the validator
rejects `planner`); the planning data-walk rides the wave-1 scout and connector items. Seats write
reports under `.ufo/waves/round-72/w1/` and `.ufo/waves/round-72/w2/` (absolute paths in every seat
item); executors may also write counter/control drafts under `<wave>/build/<SeatName>/`. No seat
edits a committed lane file: the L1 is the one integration owner and lands everything through
`scripts/hyaku/jj-lane.sh`.

## Before-values re-measured at round start (Q19) — base `c69711e`, committed receipts

Receipts: `.ufo/waves/round-72/receipts/base-battery.txt`, `receipts/base-outputs/`,
`receipts/census-before.txt`. Observed at the base, each from the lane root:

| gate | command | exit at base |
|---|---|---|
| gate registry | `python3 -B verifiers/check_gate_registry.py --rev c69711e` | 1 — `conformant 51 of 53 lane verifiers`; no row names `check_r69_routed_repairs_v2.py` or `check_skill_evals_v2.py` |
| assertion floors | `python3 -B verifiers/check_assertion_floors.py` | 1 — `FAIL checklist observed=1862 floor=1862 self_test_failures=1`: the checklist self-test arm "live round-65 corrections land, only LOG.md:2678 red" expects a red the r71 errata row removed (live now `PASS … 2 recorded absence(s) excused`) |
| corpus integrity | `python3 -B verifiers/verify_corpus_integrity.py` | 1 — 5 DRIFT (`tracked_files 133` vs 132, `unindexed 1` = `corpus/lessons/round-71-verifier-spotcheck.md`, `report_total 93` vs 91, `commit_total 41` vs 40, `commit_nonhash 2`) |
| corpus independent | `python3 -B verifiers/verify_corpus_independent.py` | 1 (same unindexed + nonhash cause) |
| checklist | `python3 -B verifiers/verify_skill_checklist.py` | 0 (11/11) |
| correction sweep | `python3 -B verifiers/check_correction_sweep.py --root .` | 0 |
| substrate pins | `python3 -B verifiers/check_substrate_pins.py` | 2 — `DRIFT 3/3 pins failed` (omp wrapper script at `~/.local/bin/omp`; npx opencode path gone) |
| surfaces | `python3 -B verifiers/verify_surfaces.py` | 2 — `opencode binary not found` |
| harness claims | `python3 -B verifiers/verify_harness_claims.py` | 2 — `template anchor occurs 0x in /home/vgpnk/.local/bin/omp` |
| r53 re-pin counter | `python3 -B verifiers/check_opencode_repin.py --rev c69711e` | 1 — `surfaces pass 0 of 7 … pins OK 0/3` |
| census | `sources-census.sh validate --root … kotoba` | 0 (139 rows, 20 W04 duplicate-URL warnings) |

Host facts behind the substrate rows (observed 2026-10-25): `~/.local/bin/omp` is a 1,680-byte
Bourne wrapper (installed 2026-10-23) and the real binary is `~/.local/bin/omp.real` with the
**same** sha256 (`85d9daf3…`) and ns-exact mtime the lane pinned in r51 (so the omp half is a path
drift, not a rebuild); the host opencode is `~/.opencode/bin/opencode` v2.1.4 (sha256
`ca9b3ee2…`), no longer npm 1.19.4. With `--omp-binary omp.real --opencode-binary
~/.opencode/bin/opencode`, `verify_surfaces.py` reads `pass 5 fail 2` (opencode extraction 0 classes
from 7 rules; literal `CONTEXT.md` absent from the v2.1.4 dump). `SKILL.md` is **600 of 600
lines** and 72,688 bytes at base: any added row or box must free lines first.

## Inherited routed defects (r71 spot-check, `corpus/lessons/round-71-verifier-spotcheck.md` § Routed)

Worked this round, none a claim: (1) report filed complete at first filing — `## SHONEN`,
`## Sources & frontier`, `## Trend verdicts`, `Work performed`, `Before → after measurements`;
(2) round shape, wave seat counts, role mix, dead seats, round total recorded, wave specs/registries/
seat reports committed under `.ufo/waves/round-72/`; (3) a committed receipt for every no-harm
battery item (C3 below runs the battery under receipts); (4) the Gate block records rejected
candidates; (5) the Landed list cites the actual lane HEAD; (6) `Assimilation:` and the
considerthese result are stated; (7) located quotes stay verbatim from the cited surface and any
normalization is named (Q42, Q56).

## Claim declarations (this round declares 3)

### C1 — depth (the lane's lowest owned axis, 9), SOURCED + assimilation: author-facing rules reach the audit checklist

**Axis:** `depth` (owned, 9). **Surface:** four rules an executing agent can act on, in
`SKILL.md` § Trigger-fidelity checklist — three from entries already held (name uniqueness:
`corpus/knowledge/skill-name-precedence-round69.md`, S203–S207; authority level:
`corpus/knowledge/instruction-authority-ladder-round67.md`, S123 and S129; install-path trust:
`corpus/knowledge/client-trust-gates-round68.md`, S198–S202 and S208) and the
assimilated rung rule (what belongs in a skill versus an always-on file versus a one-off prompt)
from rows opened this round. Source: `considerthese/2026-10-25.md` § Self-improvement
suggestions item 3 ("Route each knowledge entry's 'what a skill author does' bullets into the
audit checklist"); the one considerthese proposal worked this round.

**Frozen predicate (the same sentence in this plan, in the counter's docstring and in the receipt):**

```
python3 -B verifiers/check_author_rules.py --rev <rev>  ->  prints "author-facing rules in SKILL.md N of 4", exit 0 when N == 4
```

Rule `Ai` holds at `--rev` iff all of (committed bytes only, no instrument executed):

- **(a)** the rendered `SKILL.md` (HTML comments and fenced blocks removed) has exactly one
  checklist box — a `- [ ] ` line plus its indented continuation lines — inside `## Trigger-fidelity
  checklist` (up to the next `## ` heading) whose joined text carries the rule's token set as whole
  words (frozen: **A1 name uniqueness** `name`, `unique`, `precedence`; **A2 authority level**
  `authority`, `level`, `body`; **A3 install-path trust** `install`, `trust`, `command`; **A4 rung**
  `prompt`, `always-on`, `skill`, `index`) and ends with the tail `(sourced: S###[, S###…]; entry:
  <repo-relative path>)` naming that rule's frozen entry (A1 the round-69 entry, A2 the round-67 entry,
  A3 the round-68 entry, A4 `corpus/knowledge/resident-index-and-rungs-round72.md`) and at least one
  id from that entry's own `source:` lines;
- **(b)** every cited `S###` is an 11-cell registry row at `--rev` with status `mined`, tier `A`
  or `B`, and a `used-by` cell that lists the cited entry path;
- **(c)** the entry exists at `--rev`, opens with `source:` lines naming every cited id, then
  `verified-at:` and `recheck:`;
- **(d)** (A4 only) each cited row's located quote (the quote cell, 5–25 words) is found
  word-bounded in a committed, sha256-pinned snapshot of the cited page under
  `.ufo/waves/round-72/snapshots/` — a missing or tampered snapshot is exit 2.

**Do-nothing control:** the base tree scores `0 of 4`, exit 1 (committed receipt before data).
**Shortcut controls (Q37, committed bundles + receipts before data, each must score below 4):**
token-stuffed boxes citing `queued` rows; boxes citing rows whose `used-by` omits the entry; the
boxes inside an HTML comment or a fence; the boxes placed outside the checklist section; an A4 quote
absent from its snapshot; an entry without the provenance trio; a box whose tail names an id that
resolves in no registry row. **Kill rule:** if any shortcut world reads 4 the counter is wrong and
is fixed before data; no rule changes after any seat has scored data (Q28).

### C2 — freshness (the lowest axis by score, 8; advisory): the host substrate re-derived and re-pinned

**Axis:** `freshness` (advisory, 8 — the lowest score on the card; recorded here because the r71
plan reading "lowest owned" left it unworked since round 53). **Surface:** the Loader-rule
freshness Frontier row (`corpus/README.md` § Frontier): four instruments are red on a host drift
(Q09: a substrate move makes freshness red until re-derived and re-pinned; "no rebaseline" is open
debt). The omp half is a path move onto `omp.real` (identical bytes); the opencode half is a new
binary lineage (v2.1.4) whose loader the census rules OC-1…OC-6 must be re-derived on.

**Frozen predicate:**

```
python3 -B verifiers/check_substrate_repin_v2.py --rev <rev>  ->  prints "host substrate re-derived: pins OK k/3; surfaces pass p of 7; removal ledger l of l verified", exit 0 when k == 3 and p == 7 and the ledger conjunct holds
```

The counter extracts `<rev>`'s tree (`git archive`), runs that tree's `verify_surfaces.py --json`
and `check_substrate_pins.py --json` at **their own default paths** (no path flags), and recomputes
the ledger conjunct itself: every opencode class declared at the base `c69711e` is either kept
(same `class_id`, `literal`, `context_kind`, `verdict` at `<rev>`) or listed in
`verifiers/census-removals.json`; the ledger must equal **exactly** the set of base classes whose
literal the counter finds absent from the live opencode dump (count 0 by its own `strings -n 4`
pass) — a present literal cannot be ledgered, an absent one cannot stay declared `governed`.
**Q45 population census (wave 1, before data):** a seat that writes no content counts which of the
7 checks honest derivation can pass on the v2.1.4 bytes; the target stays `p == 7` only if that
census reaches 7, else it is lowered **before data** in a committed addendum to this plan stating
the census command and the margin; a lowering after data is a miss.

**Do-nothing control:** base `c69711e` → `surfaces pass 0 of 7 … pins OK 0/3` (the existing r53
counter; committed in `receipts/base-battery.txt`). **Shortcut controls (committed worlds):** a
re-pin that edits only the baseline shas and paths and leaves rules OC-1…OC-6 unchanged (must read
`p < 7`); a world that ledgers every opencode class (must fail the exact-set conjunct); a stub file
at the pinned opencode path whose sha is pinned (must fail extraction vacuity); a world that pins
`omp.real` but leaves `omp_binary_mtime` at the old value. **Kill rule:** any shortcut world that
reads `exit 0` means the counter is wrong; fixed before data.

### C3 — consistency (calibration sub-axis, owned, 10): the lane's own tip battery matches the record

**Axis:** `consistency` (owned, 10; held). **Surface:** the base's own gates contradict the r71
record: the r71 plan promised `check_gate_registry.py` `53 of 53` and a battery run, and the r71
report lists `Corpus gates … green`; at the base four of the six battery gates exit 1 (table
above). A calibration claim counts mismatches between the lane's self-assessment and observed repo
state (§9): the r71 `plans/round-71.md` § No-harm battery lists five gates plus the census; the
observed state is the table above.

**Frozen predicate:**

```
python3 -B verifiers/check_tip_battery.py --rev <rev>  ->  prints "tip battery exit 0: N of 6", exit 0 when N == 6
```

The counter builds a fleet-shaped sandbox of `<rev>` (a clone named `kotoba-shokunin` under a parent
that symlinks every fleet-root entry — the r71 K69-11 construction; Q63: the first run is on an
honest real world, receipt committed before the counter is frozen) and runs, from its root, the six
frozen commands: `check_gate_registry.py --rev <rev>`, `check_assertion_floors.py`,
`verify_skill_checklist.py`, `verify_corpus_integrity.py`, `verify_corpus_independent.py`,
`check_correction_sweep.py --root .`; N is the number that exit 0. Guards the counter makes itself
(Q33): no path under `corpus/`, `verifiers/` or `SKILL.md` tracked at the base is deleted at
`<rev>`; no assertion floor in `verifiers/floors-registry.json` is lower than at the base; the six
instrument scripts change by at most 40 added lines in total over the base (a stub `exit 0`
replacement fails this cap by size, and by the floors guard); the non-author
`corpus/lessons/*-verifier-spotcheck.md` files are byte-identical to the base.

**Do-nothing control:** the base scores `2 of 6`, exit 1 (measured by hand above; the counter's own
receipt is committed before data). **Shortcut controls (committed worlds):** delete the r71
spot-check file and re-record the baseline (must fail the no-deletion/identity guard); replace
`check_gate_registry.py` by a stub `sys.exit(0)` (must fail the size cap); lower the checklist
floor to the observed 1862 minus its failure (must fail the floors guard); bless the five DRIFT
baseline values without indexing the file (must leave `verify_corpus_integrity.py` red).
**Kill rule:** any shortcut world scoring 6 means the counter is wrong; fixed before data.

## Frontier step

Census before: `.ufo/waves/round-72/receipts/census-before.txt` (exit 0; 139 rows; 20 W04). C1 is
the sourced claim: its A4 rule rests on rows opened this round (the lesson's `## Gate` records URL,
access date and a ≤25-word located quote per row). The mined mistake goes to
`corpus/lessons/round-72.md` § Mistakes (class `stale-premise` / record-vs-tree: the r71 plan
promised `53 of 53` and a battery that its own base never ran — evidence = the table above).
Q-candidate: a plan's no-harm battery is run at its own base before the plan freezes, and a
promised row add is checked arithmetically against a stated budget (600 lines) — C3's counter is
the fix shown able to fail (`2 of 6` at base).

**Assimilation (addendum §10).** One theme from the read-only package
`/home/vgpnk/Projects/shokuknow/merge/kotoba/`: **the resident-index versus on-demand rung** — two
staged entries, `skill-vs-always-on-boundary.md` (staged S261–S264) and
`context-rot-and-always-on-context.md` (staged S248, S254, S255, S256). Per-entry gates: PROVINCE
scope (the second entry's measured degradation curve is capability measurement, `kengaku`'s
adjacent ground — expected refusal with reason + flip unless the craft rule survives without it),
QUALITY bar, expansion only on ground the coverage map did not hold. Id collision check, guard
proof, normalized append block and the validated scratch mirror under
`.ufo/waves/round-72/assimilation/`. Quarantine: the register slice for `kotoba` (13 rows,
`awk` command in the prompt; re-derived at round time) is hand-checked row by row in wave 1 and
every verdict lands in the lesson; no refused row is appended.

## No-harm battery (run at the measured tip, receipts committed)

`verify_skill_checklist.py --json` (SKILL.md ≤ 600 lines), the six C3 gates, `check_substrate_pins.py`,
`verify_surfaces.py`, `verify_harness_claims.py`, `compare_harness_independent.py`,
`check_province_core.py`, `check_sibling_census.py` against the census file, census `validate`
exit 0; every one run once at the measured tip and its output committed with `measured-rev`.
