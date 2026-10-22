# R1FrontmatterKey — routed defect R1: skill identity is the frontmatter name

Seat: `KotobaR49.R1FrontmatterKey` (leaf executor). Lane `/home/vgpnk/Projects/shokunin/kotoba-shokunin`
(read-only except this report). Private clone
`/fast/scratch/hyaku/kotoba-r49/seats/R1FrontmatterKey/clone` @ base `a5adc146a2995dcc5a95a6d8db6e5674f75191ac`.
Deliverable: `/fast/scratch/hyaku/kotoba-r49/seats/R1FrontmatterKey/r1.patch`
(sha256 `8841827a96ddb62e115b5a5664f02e22d8b86061c80e055a4f99bda723b24e9a`, 323 lines).

## Findings

1. **The defect is real and latent.** `verifiers/verify_harness_independent.py` keyed the configured
   (`--oc-config/skill`, `--oc-config/skills`) and log-named roots by **directory name**
   (`names.add(entry.name)`) while the agents root keyed by **frontmatter name**
   (`skill["frontmatter"].get("name") or skill["dir"]`). S016 (`corpus/SOURCES.md:29`) states opencode's
   own rule: "identity is the frontmatter name, not the directory name". A skill offered by two roots
   under two directory names was therefore counted twice — the round-48 falsify seat's A21 probe (4 -> 5).

2. **Fix (mechanism).** One operator for every root, in `derive()`: each skill is identified by the `name`
   in its SKILL.md frontmatter, and the **directory name is the fallback ONLY when the frontmatter carries
   no name** (empty/absent `name`, or an unreadable SKILL.md). New module helpers `read_frontmatter()`
   and `skill_identity()` carry the rule and its comment. The agents-root branch is unchanged in effect
   (it already keyed by frontmatter with a directory fallback), so the two branches now agree.

3. **Must-fail arm demonstrated in both directions.** The new arm fixture has the agents root offer the
   identity `x` (directory `x`) and `--oc-config/skills/dir-y/SKILL.md` declare `name: x` from a
   *different* directory. Frontmatter operator -> 3 (alpha, beta, x); directory operator -> 4
   (alpha, beta, x, dir-y). On the **base consumer** (the same file with only the derive() keying reverted
   to directory-name) the arm **FAILS**, exit 1; on the candidate it **PASSES**, exit 0.

4. **Four arms, one discriminating.** (a) the alias arm (must-fail); (b) a **control** arm with a
   *different* identity in `dir-y` -> 4 under both operators, so the fix cannot have dropped the
   configured root's skill; (c) a **fallback** arm: a configured SKILL.md with **no** `name` field still
   contributes exactly one name, its directory name; (d) a **log-named-root** arm: a root the opencode log
   names as a source keys its skills by the frontmatter name too (the configured root's `dir-y` is removed
   first so the log-named root is the only contributor beyond the agents root).

5. **Floors bumped in-step (BUMP-IN-STEP rule).** `verifiers/floors-registry.json`
   `harness_independent.floor` 116 -> 123; `verifiers/check_assertion_floors.py` `EXPECTED_INSTRUMENTS`
   and `INSTRUMENTS` rows 116 -> 123; the guard docstring's floor list (line 8) and its round-49 narrative
   sentence. Only the `harness_independent` row was touched, per the seat note (another seat edits the same
   two floors files for a different instrument). The floors guard itself is green: 9 PASS, exit 0.

6. **No live effect on this host, as the round-48 falsify seat predicted.** `oc.roots.names_plus_builtin`
   = **10 at base and 10 at candidate** (default arguments). The two configured roots
   (`~/.config/opencode/skill`, `~/.config/opencode/skills`) do not exist here, and the only log-named root
   that exists (`/home/vgpnk/Projects/opencodeufo/.opencode/skills`) holds `shokunin` and `tower`, whose
   directory names equal their frontmatter names, so both operators agree. The repair is latent-safe: it
   changes nothing that was already right and fixes the case that was wrong.

7. **Every existing self-test arm stayed green.** Base `--self-test`: `0 failure(s) over 116 assertions`,
   exit 0. Candidate `--self-test`: `0 failure(s) over 123 assertions`, exit 0 (+7 assertions: 3 fixture
   premises + the alias arm + the control + the fallback + the log-named-root arm).

## Evidence (commands, exit codes, paths, hashes)

| Measurement | Command | Exit | Result |
|---|---|---|---|
| Base self-test | `python3 -B verifiers/verify_harness_independent.py --self-test` (cwd=baseclone @ a5adc146) | 0 | `0 failure(s) over 116 assertions` |
| Candidate self-test | same (cwd=clone, candidate) | 0 | `0 failure(s) over 123 assertions` |
| **Base-consumer probe** (arm must fail) | base consumer = candidate file with only the derive() keying reverted to `names.add(entry.name)`; `python3 -B verifiers/_r1_base_probe.py --self-test` | **1** | `FAIL round 49: one identity offered by two roots under two directory names is counted once: got 4 want 3` / `FAIL round 49: a log-named root keys its skills by the frontmatter name too: got 4 want 3` / `2 failure(s) over 123 assertions` |
| Candidate self-test (same arms) | `python3 -B verifiers/verify_harness_independent.py --self-test` | 0 | `0 failure(s) over 123 assertions` (no FAIL line) |
| Floors guard | `python3 -B verifiers/check_assertion_floors.py` (cwd=clone) | 0 | `PASS harness_independent observed=123 floor=123` + 8 other PASS rows, no FAIL |
| Live row, base | `python3 -B verifiers/verify_harness_independent.py --json` (cwd=baseclone) | 0 | `oc.roots.names_plus_builtin` = 10, status DERIVED |
| Live row, candidate | same (cwd=clone) | 0 | `oc.roots.names_plus_builtin` = 10, status DERIVED |
| Patch applies to base | `git apply --check` then `git apply` of r1.patch in a fresh clone @ a5adc146 | 0 | `APPLY_CHECK_OK`, `APPLIED`; `git diff --stat` = 3 files, +218/-12 |
| Applied-patch self-test | `python3 -B verifiers/verify_harness_independent.py --self-test` (cwd=applytest) | 0 | `0 failure(s) over 123 assertions` |
| Patch digest | `sha256sum r1.patch` | 0 | `8841827a96ddb62e115b5a5664f02e22d8b86061c80e055a4f99bda723b24e9a` |

Exact base-consumer probe output (the must-fail demonstration), verbatim:

```
FAIL round 49: one identity offered by two roots under two directory names is counted once: got 4 want 3
FAIL round 49: a log-named root keys its skills by the frontmatter name too: got 4 want 3
2 failure(s) over 123 assertions
```

Exact candidate output for the same arms, verbatim:

```
0 failure(s) over 123 assertions
```

## Patch contents (3 files, +218/-12)

- `verifiers/verify_harness_independent.py` — new `read_frontmatter()` / `skill_identity()` helpers with the
  rule and the fallback stated in their docstrings; `derive()`'s root enumeration rekeyed to the
  frontmatter name for the configured **and** log-named roots (the agents-root branch now routes through
  the same helper); the row's evidence string now says "each skill keyed by its SKILL.md frontmatter name,
  the directory name only when the frontmatter has none"; new `build_frontmatter_key_fixture()` and
  `build_frontmatter_fallback_fixture()` builders; four new self-test arms with their fixture-premise
  assertions.
- `verifiers/floors-registry.json` — `harness_independent.floor` 116 -> 123.
- `verifiers/check_assertion_floors.py` — `EXPECTED_INSTRUMENTS` / `INSTRUMENTS` `harness_independent` rows
  116 -> 123 and the guard docstring's floor list plus a round-49 narrative clause. **No other instrument's
  row touched.**

## Risks / notes

- The candidate changes the row's **evidence string** (not its value). The row value is unchanged on this
  host (10 = 10). `compare_harness_independent.py` compares values, not this row's prose, and the
  comparator's committed fixture payload (`verifiers/fixtures/compare-harness-independent/record-map-24-control/independent.json`)
  carries its own older wording, which is comparator input, not an expectation of this row's text — no
  comparator arm asserts on this row's evidence wording.
- The agents-root branch's *fallback* is unchanged in effect, but it now routes through `skill_identity()`;
  a SKILL.md whose frontmatter `name` is a non-string (e.g. a folded block) falls back to the directory
  name, matching the base's `or skill["dir"]` behaviour on falsy values.
- No tools installed or upgraded this session (stock python3/git only).
- Lane bounds honored: the only file written under the lane checkout is this report; no git/jj write in the
  lane, the fleet root, or any sibling lane; all code work happened in the private clone.
- Not run (out of the seat's scope and time bound): `compare_harness_independent.py --json` live join,
  `verify_skill_checklist.py`, `verify_corpus_integrity.py`. The parent's post-integration gate owns those.
