# C1 instrument discrimination (target side) — wrong-candidate mutants vs the committed ruler

Seat: `C1RulerTargetMutants` (leaf, no delegation). Lane base `75f671b109d8eddd0d64c1429bd6379fe577175a`.
Detector: lane-committed `.ufo/round-48/tools/config-root-ruler.py` (sha256 `01af33a6…`), oracle
`config-root-cases.json` (sha256 `1d09a38c…`), baseline receipt `before-configured-root.json`
(sha256 `8bec447a…`). Private clone: `/fast/scratch/hyaku/kotoba-r48-a2/seats/C1RulerTargetMutants/clone`.

## Findings

**F1 — FINDING AGAINST THE INSTRUMENT (surviving mutant).** A recursive implementation of the
configured-root enumeration passes the ruler clean. Mutant `c1` replaces the direct-child operator
with `path.rglob("SKILL.md")` + `match.is_file()` + `names.add(match.parent.name)`; the ruler
returns `verdict=clean`, exit `0`, 13/13 cases settled, 0 target failures, 0 behavioral mismatches,
0 evaluation errors. Its 13 observed target values are identical to the pristine candidate's, so the
frozen matrix cannot distinguish "direct child only" (the contract's own scope wording: *"Direct-child
disk-root enumeration only … No new recursion policy"*) from "any depth". The divergence is real, not
hypothetical: on a synthetic input outside the matrix — `config/skill/group/zeta/SKILL.md`, i.e. a
skill two levels below the configured root — the pristine candidate derives
`oc.roots.names_plus_builtin = 2` and mutant `c1` derives `3` (nested skill name `zeta` counted).
Coverage gap: the matrix has no case with a skill nested below a configured root. Owner decision
(L1): add a nested-skill case to the oracle (this changes the oracle file and its pinned sha256, so
it needs a prospective amendment) or record the direct-child scope as unpinned.

**F2 — instrument discriminates the rest.** Six of the seven requested wrong candidates plus one
extra are killed (red target cases listed below). Root-family (singular vs plural), SKILL.md
presence, and set-vs-list duplicate semantics are all pinned by the matrix.

**F3 — single-case dependency.** Mutant `c2` (recursive glob *without* the file-type check) is
killed only by `skill-named-directory`; every other case is blind to it. The recursive family is
therefore pinned only by the narrower "directory named SKILL.md" fixture, not by any depth case.

**F4 — observation, not mine.** The lane working tree carries an uncommitted modification of
`verifiers/verify_harness_independent.py` (byte-identical to candidate commit `26035dce`, consumer
sha256 `2d824c0b…`). It was present before this seat ran and was left untouched. Lane HEAD is still
`75f671b`; the committed consumer at `75f671b` is still the pre-repair (base) behavior.

## Mutants and verdicts (base = candidate commit `26035dce`, consumer sha256 `2d824c0b…`)

| # | Mutant | Wrong behavior | Commit | Consumer sha256 | Ruler verdict / exit | Red target cases |
|---|--------|----------------|--------|-----------------|----------------------|------------------|
| 0 | pristine | none (control) | `26035dce` | `2d824c0b…` | clean / 0 | – |
| a | singular root only | enumerates `--oc-config/skill`, never `--oc-config/skills` | `d0b9976` | `0f8357f4…` | failed / 1 | plural-unlogged, both-distinct-unlogged, configured-plus-other-log-root |
| b | plural root only | enumerates `--oc-config/skills`, never `--oc-config/skill` | `8f11162` | `940ca253…` | failed / 1 | singular-unlogged, both-distinct-unlogged |
| c1 | recursive glob (file check) | `rglob("SKILL.md")` at any depth | `be3ba2e` | `9d06530e…` | **clean / 0 (SURVIVED)** | – |
| c2 | recursive glob (no file check) | `rglob("SKILL.md")`, matches a *directory* named SKILL.md too | `fb689fd` | `c083b231…` | failed / 1 | skill-named-directory |
| d | any child directory counts | counts child dirs without requiring SKILL.md | `bb90166` | `5875042e…` | failed / 1 | non-skill-child-files, skill-named-directory |
| e | list instead of set | names and roots as lists → duplicates add twice | `11caf5f` | `34af913a…` | failed / 1 | configured-duplicates-agent, same-name-both-config-roots, singular-already-logged, plural-already-logged, duplicate-log-source |
| e2 | list incl. log sources | as `e`, plus log sources kept as a list | `cac5a49` | `9e5add75…` | failed / 1 | same five as `e` |
| f | root names counted as skills | adds `skill`/`skills` root dir names to the name set | `e94b9ba` | `1c6ed455…` | failed / 1 | 12 of 13 (all but control-agents-only) |

Observed target counts (expected values in brackets) for the two decisive columns:

```
case                             exp  pristine  a       b       c1      c2      d       e       e2
control-agents-only               2      2        2       2       2       2       2       2       2
singular-unlogged                 3      3        2       3       3       3       3       3       3
plural-unlogged                   3      3        3       2       3       3       3       3       3
both-distinct-unlogged            4      4        3       3       4       4       4       4       4
configured-duplicates-agent       2      2        2       2       2       2       2       3       3
same-name-both-config-roots       3      3        3       3       3       3       3       4       4
singular-already-logged           3      3        3       3       3       3       3       4       4
plural-already-logged             3      3        3       3       3       3       3       4       4
configured-plus-other-log-root    4      4        3       4       4       4       4       4       4
non-skill-child-files             2      2        2       2       2       2       3       2       2
skill-named-directory             2      2        2       2       2       3       3       2       2
empty-config-roots                2      2        2       2       2       2       2       2       2
duplicate-log-source              3      3        3       3       3       3       3       4       5
```

## Evidence (commands, exit codes, custody)

- Pristine control run first, so kills are attributable to the mutation, not to a red baseline:
  `python3 -B .ufo/round-48/tools/config-root-ruler.py --repo <clone> --revision 26035dce… --consumer-sha256 2d824c0b… --oracle .ufo/round-48/oracle/config-root-cases.json --oracle-sha256 1d09a38c… --scratch …/ruler-0 --baseline-receipt .ufo/round-48/verification/before-configured-root.json --baseline-sha256 8bec447a…`
  → `{"verdict":"clean","target_failures":[],"behavioral_mismatches":[],"evaluation_errors":[],"settled_cases":13}`, exit `0`.
- Every mutant run used the same command with its own `--revision`, `--consumer-sha256` and
  `--scratch ruler-<n>`; the receipt for each run is at
  `/fast/scratch/hyaku/kotoba-r48-a2/seats/C1RulerTargetMutants/ruler-<n>/receipt.json`
  (n = 1…8). Exit codes: `RULER_EXIT=1` for a/b/c2/d/e/e2/f, `RULER_EXIT=0` for c1 (the survivor).
- Custody: in all 9 receipts `consumer_sha256_before == consumer_sha256_after`, `evaluation_errors`
  empty, `behavioral_mismatches` empty (except where target failures are reported), 13/13 cases
  settled, and each case's `inputs_before == inputs_after` (the synthetic substrate was not mutated).
- Baseline compatibility: each run passed the committed before receipt; the ruler accepted it
  (`baseline_receipt_sha256` matched) and reported no baseline population drift.
- Surviving-mutant evidence: `ruler-3/receipt.json` → verdict `clean`, exit `0`; per-case
  `observed_count` for all 13 cases equals the pristine run's values.
- Divergence proof (outside the frozen matrix, no matrix file touched): `nested-probe.py` reuses the
  ruler's own `materialize()` to build the substrate, then runs both consumers on
  `config/skill/group/zeta/SKILL.md`:
  `{"a_target": 2, "b_target": 3, "diverge": true}` — pristine `2`, mutant c1 `3`. Probe sources:
  `pristine-consumer.py` (sha256 `2d824c0b…`) and `c1-mutant-consumer.py` (sha256 `9d06530e…`),
  both exported from the clone.
- Restoration: the clone's `verifiers/verify_harness_independent.py` was restored to the pristine
  candidate bytes after every mutant and at the end — final sha256
  `2d824c0b3d4954c9a01868ee7c9b44c72b77bb5054419cf0539f6e4082f1b88a` (equals `git show 26035dce:…`),
  restoration commit `3323252`. All mutant commits remain in the private clone's history
  (`d0b9976, 8f11162, be3ba2e, fb689fd, bb90166, 11caf5f, cac5a49, e94b9ba`); branch `mutants`.
- Lane untouched: `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin status --porcelain` before and
  after this seat shows the same three lines (` M verifiers/verify_harness_independent.py`,
  `?? .ufo/waves/round-48/`, `?? plans/round-48.md`); HEAD stayed `75f671b`. The only file this seat
  wrote in the lane is this report. No `jj`/git write was run in the lane, the fleet repo, or any
  sibling lane; all commits live in the private scratch clone.
- Tooling: no install or upgrade was needed or performed. `python3 3.14.8`, `git 2.56.0` (already
  present). No web source was opened this session, so no SOURCES row is owed by this seat.
