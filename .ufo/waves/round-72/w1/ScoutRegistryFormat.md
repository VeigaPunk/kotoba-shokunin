# ScoutRegistryFormat — round-72 wave-1 report

**Verdict: the five gate-registry rows draft clean and are proven conformant.**
`check_gate_registry.py --rev` at the base `c69711e` reads `51 of 53` (the two
v2 rows missing); with the five drafted rows plus the three new verifier files
present in a scratch fleet-shaped sandbox commit, it reads `56 of 56`, exit 0,
phantom 0. The five rows need **5 physical lines**: SKILL.md goes from
600/600 to 605 lines against the checklist budget (trigger.line_budget FAIL
`605 lines exceed budget 600`), so the L1 must free ≥5 lines elsewhere in
SKILL.md before landing the rows.

## Evidence

### Before (base `c69711e`, lane clone in fleet-shaped sandbox)

Command: `python3 -B verifiers/check_gate_registry.py --rev c69711e` (cwd =
sandbox lane root). Observed (excerpt; all other 51 rows `OK`):

```
verifiers/check_r69_routed_repairs_v2.py     no registry rows naming it: 0 (need 1)
verifiers/check_skill_evals_v2.py            no registry rows naming it: 0 (need 1)
gate registry rows conformant 51 of 53 lane verifiers; phantom 0
```
Exit 1 — matches the plan's base receipt.

Checklist at base: `python3 -B verifiers/verify_skill_checklist.py --json`
→ 11/11 PASS, exit 0; `trigger.line_budget PASS 600 - 600 lines within budget
600 (from box at line 320)`.

### After (sandbox commit `b753a8471528b842ebcdc5af305586cbbeb9440a`, base tree + 5 rows + 3 placeholder verifier stubs)

Command: `python3 -B verifiers/check_gate_registry.py --rev b753a8471528b842ebcdc5af305586cbbeb9440a`.
Observed (all 56 rows `OK`, including the five drafted; exit 0):

```
verifiers/check_author_rules.py              OK
verifiers/check_substrate_repin_v2.py        OK
verifiers/check_tip_battery.py               OK
gate registry rows conformant 56 of 56 lane verifiers; phantom 0
```

Checklist at the draft: `python3 -B verifiers/verify_skill_checklist.py
--json` → 10 PASS, 1 FAIL (only `trigger.line_budget`), exit 1:
```
trigger.line_budget FAIL 605 - 605 lines exceed budget 600 (from box at line 320)
```
All other triggers pass, including `trigger.citation_resolves PASS 194`,
`trigger.command_binary_resolves PASS 37`, `governance.citation_resolves
PASS 1272`.

**Line cost: 5 lines** (600 → 605). Sandbox `wc -l SKILL.md` = 605.

## The five drafted rows (verbatim, table column order; insert after the `check_skill_evals.py` row, before the blank line that closes the table — currently lines 523–527 of a 600-line SKILL.md, i.e. 605 lines in the drafts)

```
| `verifiers/check_r69_routed_repairs_v2.py` | gate | `python3 -B verifiers/check_r69_routed_repairs_v2.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate — round-71 C1 successor counter: redesigned against the round-70 closure's routed defects (base-prefix byte integrity, exact headings, whole-word/digit-bounded tokens, ordered old→new values, pinned blob SHAs, git-object recomputation, real re-runs of the receipt's three counters at the pinned rev, fleet-shaped sandbox); K69-11 passes on the GOVERNANCE_ERRATA-recorded absence; `r69 routed defects closed N of 10` frozen target | `--self-test` | in-file | temporary sandbox clone under `$TMPDIR` (removed) | kotoba |
| `verifiers/check_skill_evals_v2.py` | gate | `python3 -B verifiers/check_skill_evals_v2.py --rev <rev> --fetch` | 0=clean, 1=failed, 2=could-not-evaluate (incl. a tampered snapshot) — round-71 C2 successor counter (depth): exactly-4-cell fact rows; HTML comments and fenced blocks stripped from the entry, SKILL.md and SOURCES.md; word-bounded quotes; `used-by` EXACTLY the entry path; census-validate over the revision's registry; superseding agentskills.io rows carry an upstream-commit anchor; SELF_SHA drift = exit 2; `skill eval artefacts verified N of 10` frozen target | `--self-test` | in-file; `.ufo/waves/round-70/snapshots/` | none (read-only); `--fetch` reads the three live URLs | kotoba |
| `verifiers/check_author_rules.py` | gate | `python3 -B verifiers/check_author_rules.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate — round-72 C1 counter (depth): four author-facing rules in SKILL.md § Trigger-fidelity checklist (A1 name uniqueness, A2 authority level, A3 install-path trust, A4 resident-index rung), each a rendered checklist box carrying its frozen token set and ending `(sourced: S###…; entry: <repo-relative path>)`; every cited S### is an 11-cell `mined` tier-A/B row whose `used-by` lists the entry; the entry opens `source:` naming each cited id, then `verified-at:` and `recheck:`; A4 quote words found in sha256-pinned snapshots (missing/tampered = exit 2); `author-facing rules in SKILL.md N of 4` frozen target | `--self-test` | in-file | none (read-only) | kotoba |
| `verifiers/check_substrate_repin_v2.py` | gate | `python3 -B verifiers/check_substrate_repin_v2.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate — round-72 C2 counter (freshness): extracts `<rev>`'s tree and runs its verify_surfaces.py and check_substrate_pins.py at their own default paths, and recomputes the removal ledger itself — every opencode class declared at the base `c69711e` is kept (same class_id/literal/context_kind/verdict) or ledgered, and the ledger equals exactly the base classes whose literal is absent from the live opencode dump (`strings -n 4`); `host substrate re-derived: pins OK k/3; surfaces pass p of 7; removal ledger l of l verified` frozen target | `--self-test` | `verifiers/baseline.json`, `verifiers/surfaces-baseline.json` | temporary trees under `$TMPDIR` (removed) | kotoba |
| `verifiers/check_tip_battery.py` | gate | `python3 -B verifiers/check_tip_battery.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate — round-72 C3 counter (consistency): builds a fleet-shaped sandbox of `<rev>` and runs the six frozen commands (gate registry, assertion floors, skill checklist, corpus integrity, corpus independent, correction sweep), N = number exiting 0; guards: no base-tracked corpus/verifiers/SKILL.md deletion, floors never lower than base, the six instrument scripts grow at most 40 added lines total, non-author spot-check lessons byte-identical to base; `tip battery exit 0: N of 6` frozen target | `--self-test` | in-file | temporary fleet-shaped sandbox under `$TMPDIR` (removed) | kotoba |
```

## Notes for the L1

- Self-test flags were read from the scripts' own `argparse`:
  `check_r69_routed_repairs_v2.py` (line 783) and `check_skill_evals_v2.py`
  (line 646) both declare `--self-test`; both v2 frozen-predicate prints are
  `r69 routed defects closed N of 10` / `skill eval artefacts verified N of 10`
  (TOTAL = 10 in both). The three not-yet-written scripts (`check_author_rules.py`,
  `check_substrate_repin_v2.py`, `check_tip_battery.py`) have no argparse to read;
  their rows use the standard gate shape (`--rev <rev>` entry, `--self-test`
  cell) per the round-72 plan's frozen predicates.
- The registry judge requires every gate row's self-test flag to have an exact
  `add_argument` handler in the file, so the three landing verifier scripts MUST
  declare `--self-test` (and `--rev`) in their argparse, and they MUST be
  committed in the same commit as the rows (a row naming a `verifiers/` file
  absent at `--rev` is a phantom → exit 1).
- Pinned-value cells: `check_skill_evals_v2.py` keeps the v1 row's pinned
  snapshots tree `.ufo/waves/round-70/snapshots/` (present at base, confirmed by
  the passing judge); `check_substrate_repin_v2.py` pins `verifiers/baseline.json`
  + `verifiers/surfaces-baseline.json` (both exist at base). Do NOT name
  unlanded paths (e.g. `verifiers/census-removals.json`) as backticked tokens in
  row prose: `trigger.citation_resolves` flags dead backticked paths (observed in
  an intermediate draft; removed, final draft passes).
- Sandbox proof: fleet-shaped `$P` (symlinked fleet-root entries incl. `.ufo`),
  `git clone --shared` of the lane, checkout `c69711e`, draft commit on a local
  branch, gates run from `$P/kotoba-shokunin`. Initial sandbox without `.ufo`
  symlink reproduced the known dead-`../` artifacts (citation failures) — the
  final sandbox includes `.ufo` and shows 11/11 at base.
- Lane repo untouched: no committed lane file modified; only untracked wave-1
  `w1/` files exist (L1's own dispatch). Sandbox removed after proof.
