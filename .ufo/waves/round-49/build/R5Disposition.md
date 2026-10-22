# R5Disposition — routed defect R5 (carried): built-in marker join + the frozen oracle's blind shapes

Seat `KotobaR49.R5Disposition` (UFO-FSD scout, leaf, no delegation). Date 2026-10-22. Lane read-only
except this file. No tool installed or upgraded; no pacman transaction attempted. Scratch:
`/fast/scratch/hyaku/kotoba-r49/seats/R5Disposition/` (`probe.py`, fixtures under `probe/`).

## Findings

1. **R5 is two items of different kinds, and only the second is an oracle matter.** (a) is the
   producer/independent *join definition*: the producer adds a binary-marker term
   (`verify_harness_claims.py:479`), the independent side fixes built-ins to 0 by declaration, so no
   case input can move the independent side and no oracle amendment reaches it. (b) is the frozen
   13-case oracle's case coverage (frontmatter-name identity, nested shapes).

2. **The v1 oracle cannot express name identity even in principle.** Its contract says so:
   `contract.scope` — "No new recursion policy, YAML parser, **name-identity rule**, builtin rule,
   producer formula, join modes or scope-out change." Its case schema has exactly six keys
   (`jq -c '[.cases[]|keys]|unique'` → `config_files, expected_base_count, expected_target_count,
   extra_inputs, id, log_sources`) and `materialize()` writes every frontmatter name as
   `path.parent.name` (`config-root-ruler.py:60,68`). So directory name and frontmatter name are equal
   in all 13 cases by construction; the case class is unreachable, not merely untested.

3. **Measured: the 13 frozen cases are invariant under both candidate re-keys**, so the ruler is blind
   to them (why A26's R1–R4 mutants passed it clean): the frontmatter re-key keeps `dir_key == fm_key
   == expected_target_count` 13/13, and a file-only recursive operator moves 0 of 13.

4. **Therefore R1's repair and R5(b) are separable this round.** R1 re-keys configured and log-named
   roots by frontmatter name (S016) and leaves 13/13 green, so it needs **no** oracle change and can
   land against the frozen ruler — but the ruler cannot certify it; the must-fail arm plus S016 do.
   The *case gap* stays open.

5. **Nested shapes are equally unreachable.** Every skill file in the 13 cases sits at a root's direct
   child (`jq -r '.cases[].config_files[]' | awk -F/ '{print NF-2}' | sort -u` → `1`); the only
   non-directory `extra_inputs` entry is `extra/epsilon/SKILL.md`, also one level down. The recursive
   shapes A26 measured (log-root recursion, depth 3, skill-in-skill) have no case to fail on.

6. **Prospective v2 amendment — what it needs.** A new file
   `.ufo/round-N/oracle/config-root-cases-v2.json`, `schema` = `kotoba-configured-root-oracle-v2`,
   same `inputs`/`contract` with two additions: (i) `identity` — a SKILL.md's identity is the
   frontmatter `name` for every root, directory name only as the unreadable-frontmatter fallback, and
   two files with one frontmatter name are one name; (ii) a per-file `names` map (`{path: name}`,
   default = parent dir name) because `config_files` is a bare path list today. Seven new cases,
   measured with the S016 contract as the target (the probe reproduced each value):

   | new case id | input added to the flat fixture | base (a5adc146) | target | rule source for the target |
   |---|---|---|---|---|
   | `cfg-dirname-differs-fm-collides-agent` | `skill/not-alpha/SKILL.md`, name `alpha` | 3 | **2** | S016 `index.ts:125-135` — `state.skills[md.data.name]`, so a configured skill named `alpha` is one slot with the agents `alpha` |
   | `same-fm-name-two-dirs` | `skill/dir-a` + `skills/dir-b`, both name `shared-gamma` | 4 | **3** | same S016 block (one name, one slot; duplicate warning only) |
   | `same-dir-name-two-fm-names` | `skill/gamma` name `gamma-one`, `skills/gamma` name `gamma-two` | 3 | **4** | same S016 block; the directory name is not identity |
   | `cfg-nested-two-deep` | `skill/group/zeta/SKILL.md` | 2 | **2** | v1 `contract.scope` direct-child text (instrument scope; S016 is recursive) |
   | `logroot-nested-two-deep` | `extra/group/deep/SKILL.md`, log root `extra` | 2 | **2** | same scope text, applied to the legacy log-root operator |
   | `cfg-nested-depth-three` | `skill/a/b/c/SKILL.md` | 2 | **2** | same scope text |
   | `cfg-skill-inside-skill` | `skill/solo-s/SKILL.md` + `skill/solo-s/sub/SKILL.md` | 3 | **3** | same scope text |

   Totals for v2: 20 cases, 17 controls, `expected_before_target_failures` = the three identity ids
   (they are red against the dir-keyed BASE consumer), `expected_before_ruler_exit` = 1,
   `expected_candidate_ruler_exit` = 0, `expected_cli_exit_every_case` = 0. `expected_base_count` must
   be the round-49 BASE consumer's reading (`a5adc146`, consumer `f576c23f…`, byte-identical to the
   clean `03f5394` receipt), **not** v1's `197b5a4` — at `197b5a4` the five configured cases read 2
   again and the before-set would change. The four nested rows are *scope* values, not loader
   fidelity: under S016 recursion they would read 3, 3, 3 and 4 (probe column `recursive`), so v2 must
   say which contract it freezes and must not be cited as loader parity. Readable-file discrimination
   (`instrument.json` `unproved_limits`) is left unmeasured; no case is proposed for it here.

7. **It must be a new frozen file, not an edit, for five mechanical reasons.**
   `1d09a38c…` is pinned in `.ufo/round-48/instrument.json` (instrument metadata and the literal parent
   argv), in `plans/round-48.md`'s argv, in all four receipts' `oracle_sha256` field (before
   `8bec447a…` plus three afters), and in the round-48 spot-check. The ruler refuses any other bytes
   (`digest(oracle_bytes) != args.oracle_sha256` → `ValueError`, `config-root-ruler.py:161-163`),
   refuses any other schema (`:165-166`), and requires the baseline receipt to carry the same oracle
   hash (`:179-181`), writing the used hash into every new receipt (`:311`). Editing v1 in place would
   therefore unbind the round-48 before/after pair, convert a pre-registered instrument into a post-hoc
   one (`contract.base_values`: "Main must replace no expected value after measurement"), and still not
   work — v1's ruler rejects a v2 schema, so the package is a triplet: **oracle v2 + ruler v2 + a fresh
   before receipt at the chosen BASE**, with the argv pre-registered before any case runs. v1 stays
   byte-identical and keeps its 5→0 claim.

8. **Item (a) cannot be closed by any oracle case, and not this round.** Three reasons: no case input
   can move a value the independent side declares to zero; the live default join exits 2 at both
   revisions (TOCTOU scope recomputation, `C1JoinDefinitionHistory.md` §6), so there is no live number
   to score; and the definition itself is undecided — S016 supports a third reading nobody froze:
   `index.ts:277-278` "Register the built-in skill BEFORE disk discovery so a user-disk skill with the
   same name can override it", i.e. the built-in is a *name slot* in the same map, so the joined
   expectation is `|names ∪ {customize-opencode}|`, not `10 + 1` by formula and not `10`. On this host
   that is 13 today (12 disk skills carrying SKILL.md, none named `customize-opencode`, measured); the
   producer's own disk count moved 10 → 12 since the round-47 receipt, which is itself the argument for
   a frozen binary-hash carrier rather than a live probe.

9. **A v2-side asymmetry a future round must not miss.** The producer is also directory-keyed
   (`verify_harness_claims.py:470-478`, `{e.name for e in root.iterdir() ...}`). R1 makes the
   independent side frontmatter-faithful while the producer stays directory-keyed; on this host the two
   agree only because all 12 host skills carry frontmatter name == directory name (measured). Neither a
   v2 receipt nor R1 may be cited as join-level loader fidelity.

10. **Closability answer.** Nothing legitimately closes either item this round without editing the
    frozen ruler: (a) needs an operator/Main definition plus a new carrier; (b) needs the v2 triplet
    frozen before outputs. The instrument half of (b) (R1) *is* closable this round and does not touch
    v1. Both items stay carried, and the carry now carries a specified amendment, not a bare note.

## Disposition paragraph (for the round-49 report and LOG; eight lines)

```
R5 (carried) — (a) the built-in marker join and (b) the frozen 13-case oracle's blind shapes.
(a) stays open: the marker disagreement is a join definition, not an oracle input, since the independent
side reads no binary; the live join also exits 2 at both revisions, and S016 index.ts:274-281 supports a
third, unfrozen reading (the built-in is a name slot overridden by a same-name disk skill).
(b) the instrument defect is repaired this round (R1, S016 identity), but the case gap is not: v1's
contract excludes a name-identity rule and all 13 cases carry frontmatter name == directory at a root's
direct child, so 13/13 stays green under the re-key and under a recursive operator (measured). The v2
amendment is specified, not frozen: seven new case ids with expected values and sources, a new hash.
```

## Evidence (commands, exit codes, hashes)

- Lane at `a5adc146a2995dcc5a95a6d8db6e5674f75191ac`; `git status --porcelain` → ` M SCORECARD.md`,
  `?? .ufo/waves/round-49/`, `?? plans/round-49.md` (other seats; untouched).
- `git show a5adc146:verifiers/verify_harness_independent.py | sha256sum` → `f576c23f…` (exit 0);
  `git diff --stat 03f5394 a5adc146 -- verifiers/verify_harness_independent.py` → empty (exit 0), so
  the consumer is byte-identical to the revision whose ruler run was clean (0 target failures).
- `git show a5adc146:.ufo/round-48/oracle/config-root-cases.json | sha256sum` → `1d09a38c…` (exit 0);
  `…/.ufo/round-48/tools/config-root-ruler.py | sha256sum` → `01af33a6…` (exit 0).
- Ruler bindings read at source: `:161-163` hash check, `:165-166` schema check, `:179-181` baseline
  hash equality, `:311` receipt field; `:60,68` fixture name = parent directory.
- Probe (`python3 -B probe.py`, exit 0): 13/13 `dir_key == fm_key == expected_target_count`; proposed
  cases read `fm_key/dir_key/recursive` = `2/3/3`, `3/4/4`, `4/3/3`, `2/2/3`, `2/2/3`, `2/2/3`,
  `3/3/4`; a file-only recursive operator moves 0 of the 13 (second probe cell, exit 0).
- Sampling probe: `jq -c '[.cases[]|keys]|unique'` → the six keys, exit 0; `NF-2` over
  `config_files` → `1` only, exit 0. Host: `ls ~/.agents/skills | wc -l` → 10, `ls ~/.claude/skills |
  wc -l` → 3, `~/.config/opencode/skills` absent; a python pass over both roots → `host skills=12
  name-mismatches=0`; `grep -rl customize-opencode ~/.agents/skills ~/.claude/skills | wc -l` → 0.
- Primary source reopened this session (no fetched code executed):
  `https://raw.githubusercontent.com/anomalyco/opencode/e3c4eb242585dcd77be1a867391b7c25fd47ce52/packages/opencode/src/skill/index.ts`,
  fetched 2026-10-22T09:39:53Z, curl exit 0, 11,843 bytes,
  sha256 `91dce57f590e1ad3103e0555b893500e098a95cde2739422b699233889b205e6`.
  Quotes: `:24` `const OPENCODE_SKILL_PATTERN = "{skill,skills}/**/SKILL.md"` (recursive discovery);
  `:125` `if (state.skills[md.data.name]) {` with `:134` `state.skills[md.data.name] = {` (identity is
  the frontmatter name, one slot per name); `:277-278` "Register the built-in skill BEFORE disk
  discovery so a user-disk skill with the same name can override it."
- Read, not re-executed: `.ufo/waves/round-48/build/C1JoinDefinitionHistory.md` (§1-6; 21/24 vs 20/24,
  join exit 2 both arms), `.ufo/waves/round-48/falsify/A26NestedOracleGap.md` (R1–R4 pass the ruler
  clean), `corpus/lessons/round-48-verifier-spotcheck.md` §§ C2, routed defects, `corpus/lessons/round-48.md`,
  `corpus/lessons/round-47-verifier-spotcheck.md` (item 1: "Never … redefine the original result").

Confidence: the v1 contract/schema/fixture blindness and the ruler's hash/schema bindings are read from
source and measured (high). The seven v2 expected values follow from S016 and the frozen scope text and
were reproduced by the probe against materialized fixtures (high for the identity three, high for the
four scope controls *as scope values*; they are deliberately not loader-faithful). Remaining unknown:
which contract a future round freezes for nested inputs (instrument scope versus loader parity), and
whether Main rules the built-in a name slot or a scope-out — both are operator decisions, not
measurements.
