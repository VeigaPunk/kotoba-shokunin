# Round-48 C1 instrument validity review (read-only)

reviewer: C1InstrumentReview seat, hyaku round-48 attempt 2, 2026-10-22
scope: `.ufo/round-48/tools/config-root-ruler.py` (sha256 `01af33a6…bd45`), `.ufo/round-48/oracle/config-root-cases.json` (`1d09a38c…b883`), `.ufo/round-48/instrument.json` (`8ef3c74f…8f94`), all at lane `master` 75f671b. Method: static hand-derivation only; the ruler was never executed (parent-only execution honored). All commands below ran against committed blobs (lane tree clean for `.ufo/round-48`; working-tree bytes equal blob bytes).

## Verdict

Instrument is fit for the parent's one BASE run and the candidate freeze: the 13 oracle expectations are correct against the base consumer code, the trust chain holds, and no defect found can make the ruler print a false `clean`. Findings below are hardening/robustness items, none blocking, none score-relevant.

## Hand-derived counts (all 13 cases)

Base semantics, `verifiers/verify_harness_independent.py` at 75f671b (= blob `06322fc5`, sha256 `872993f8…`, byte-identical to 197b5a4 per `git diff 197b5a4 75f671b -- <path>` → 0 lines): `names` = frontmatter/dir names of `offered` (592-593) — direct children of the agents root with a readable SKILL.md (:196-211), here exactly `alpha`,`beta`; `sources` = only log `directory:…` roots (594-597); per source dir, direct child dirs holding a `SKILL.md` **file** are added (:598-603); `len(names)` (:604). Candidate target adds the same direct-child operator over `--oc-config/skill` and `/skills` themselves.

| # | case | base inputs | base | target | matches oracle |
|---|------|-------------|------|--------|----------------|
| 1 | control-agents-only | no config files, no log | 2 | 2 | yes |
| 2 | singular-unlogged | skill/gamma/SKILL.md, unlogged | 2 | 3 | yes |
| 3 | plural-unlogged | skills/gamma/SKILL.md, unlogged | 2 | 3 | yes |
| 4 | both-distinct-unlogged | skill/gamma + skills/delta | 2 | 4 | yes |
| 5 | configured-duplicates-agent | skill/alpha/SKILL.md (name dup of agents root) | 2 | 2 | yes |
| 6 | same-name-both-config-roots | skill/gamma + skills/gamma | 2 | 3 | yes |
| 7 | singular-already-logged | skill/gamma + log names config/skill | 3 | 3 | yes |
| 8 | plural-already-logged | skills/gamma + log names config/skills | 3 | 3 | yes |
| 9 | configured-plus-other-log-root | skills/gamma + log names extra/ (epsilon) | 3 | 4 | yes |
| 10 | non-skill-child-files | skills/gamma/README.md only | 2 | 2 | yes |
| 11 | skill-named-directory | config/skills/gamma/SKILL.md created as a *directory* | 2 | 2 | yes |
| 12 | empty-config-roots | config/skill + config/skills created empty | 2 | 2 | yes |
| 13 | duplicate-log-source | skills/gamma + same log source twice | 3 | 3 | yes |

Derivation notes: 1,5 dedup against agents names and legacy coverage; 7/8 the legacy log operator already counts it and the union cannot double-add; 9 legacy epsilon + new gamma; 10 child lacks SKILL.md; 11 SKILL.md-as-dir fails `.is_file()`; 12 no children; 13 `sources` set dedups. Base {base≠target} = exactly the five `expected_before_target_failures` (verified programmatically: `equal: True`).

Empirical cross-check: the committed before receipt `.ufo/round-48/verification/before-configured-root.json` (measured on real BASE, recorded 2026-10-22T01:15:33Z, `revision` 197b5a4, `oracle_sha256` 1d09a38c, `ruler_sha256` 01af33a6, `consumer_sha256_after` = `consumer_sha256_before` = 872993f8) shows observed counts **2,2,2,2,2,2,3,3,3,2,2,2,3** in oracle case order, `base_prediction_met` true ×13, `target_failures`/`behavioral_mismatches`/`evaluation_errors` = declared-fives/[]/[], `remaining_not_observed` []. Every prediction is confirmed by an independent measurement; none is a tautology.

## Required trust-chain checks — all confirmed

- **Consumer from committed revision, not working tree:** ruler :174-177 `git -C <repo> show <40-hex-revision>:<oracle consumer path>`; the tree is consulted only via `git show`. Hash-checked at :171-172 against `--consumer-sha256`; receipt stores `source_command` + before/after custody hashes (:308-312). Verified empirically: consumer blobs at 197b5a4 and 75f671b are identical (diff 0, both sha 872993f8), matching oracle `consumer_sha256` and instrument.json `consumer.git_blob` `06322fc5` (`git ls-tree` match).
- **Hashes:** oracle (:171-172 of args; :169-170 of bytes), consumer (:171-172), baseline receipt bytes and revision+oracle linkage (:184-192), consumer custody re-digest after the run (:302-310), ruler self-hash in receipt (:312). Baseline required for any non-BASE revision (:194-195); hash without receipt and receipt without hash both rejected (:186-192).
- **Cannot pass on a missing case:** loop iterates every oracle case; `remaining` empties only if all were observed (any interruption → both handlers append to errors, :282-305; uncaught-at-inner exceptions re-caught at :327-331 → 2). Missing target id → `mismatches`+failed (:247-251); CLI exit ≠0 or input mutation → errors (:238-242); unparseable channels → errors (:243-250); baseline lacking a case id → KeyError (:268) → 2. Non-int strict target refuses bools/strings (`type(v) is int`, :256). A no-op consumer also fails: its legacy values leave the five unlogged config cases at base counts ≠ frozen targets (:254-257). `return 2 if errors else 1 if failed or mismatches else 0` (:332) ⇒ exit 0 implies all 13 observed with targets met and populations preserved.

## Findings

Seriousness is rated per governed invocation (parent-owned, hash-pinned oracle 1d09a38c); none blocks or affects admission scoring.

1. **`config-root-ruler.py:315` `remaining_not_observed` is reported, never asserted before exit.** In the present flow it is provably empty at return 0 (all interruption paths add to errors → exit 2, :282-305/332), so no false pass. But nothing in code keeps that invariant if the loop structure changes, and a non-empty `remaining` with empty `errors` would exit 0/1 with the receipt honestly listing the gap while `verdict` could read `clean`. Defensive `if remaining: errors.append(...)` would harden. (low)
2. **`config-root-ruler.py:327-331` module-level handler omits `TypeError` (also `IndexError`, `sqlite3.Error`), which are reachable outside the inner loop try.** E.g. `remaining = [case["id"] for case in oracle["cases"]]` (:201) or `baseline_cases` building (:199) sit before the inner try; `baseline["cases"]` malformed → `TypeError` escapes the inner handler (:282-305 catches it inside the loop only) and also the module handler → Python traceback, exit **1**, indistinguishable from a behavioral `failed` verdict, with no receipt written. Unreachable with the hash-pinned oracle/mitigated by exit≠0 never equaling `expected_candidate_ruler_exit` 0, but it violates the documented "1 = measured contract failure" contract. (low)
3. **`config-root-ruler.py:218-220` case `id` is used unvalidated as a path component** (`root = scratch / case["id"]`) while every other external string passes `relative()` (:29-33). A hostile oracle id (`../`) could escape the scratch root. Unreachable for the frozen 13 literal slugs (ids verified unique and slug-safe). Hardening note. (low)
4. **Oracle field `consumer_sha256` (oracle line 5) is never cross-checked against the `--consumer-sha256` argument**; the CLI value is the only enforcement (and the committed receipt and instrument.json agree on 872993f8). Any CLI/oracle divergence still fails hard via :171-172 (exit 2), so no false pass. Oracle `expected_before_ruler_exit`/`expected_candidate_ruler_exit`/`expected_cli_exit_every_case` likewise inform parent assertions, not ruler logic. (informational)
5. **`expected_before_target_failures` exactness and `base_prediction_met` are carried into the receipt (:316, :226, :257) but not enforced by the ruler.** By design (F2: "Candidate ruler must not require old BASE counts", instrument.json :20-24); the exact five-set discrimination on the before run is a parent duty, and the receipt provides every datum needed (target_failures list, per-case base_prediction_met). (informational)
6. **No-harm net covers values+statuses but not row `evidence` text or the five other channels** (landed/unlanded/scoped_out/scoped_out_probes/alternatives) — ruler :258-277 consumes only value/status; instrument.json `unproved_limits` declares the five channels unproved. E.g. the target row's "built-in names: 0 by declaration" phrase is not re-verified by the instrument. Documented residual, consistent with the frozen scope. (informational)
7. **`INV1` is enforced only as exit≠0 by the ruler; the receipt carries all discriminating fields** (`target_failures`, per-case `base_prediction_met`). Parent must diff the exact five set when reading the before receipt, per F2. (informational, restating governance)

## Residual risk and verification gaps

- Static-only: I did not execute the ruler (parent-only); runtime behavior beyond the committed before receipt is unobserved. All exit-path claims above are code-derived, receipt-corroborated where data exists.
- `omp.offered.skills == 2` assumed at base (receipt-backed only; numeric INV2/INV3 offered-scale sweep out of scope).
- The five metadata channels' contents, recursive-loader parity, frontmatter-name-vs-dirname discrimination and universal no-harm remain declared unproved (instrument.json `unproved_limits`); nothing here changes them.
- Before-receipt scratch provenance (`/fast/scratch/hyaku/kotoba-r48-author-handoff/parent-before-root-matrix-01/` scratch dirs still on disk, mtime 2026-10-21 22:15 local -03 = 2026-10-22 01:15 UTC, matching receipt.recorded_at); lane-side ruler/oracle/consumer hashes equal the receipt's recorded hashes at this commit.

## Evidence (commands, exit codes)

- `git rev-parse HEAD` → `75f671b109d8eddd0d64c1429bd6379fe577175a`; `git status --porcelain -- .ufo/round-48` → empty (0 lines).
- `sha256sum` four files → `01af33a6…bd45`, `1d09a38c…b883`, `8ef3c74f…8f94`, `8bec447a…2312`; `git cat-file -p HEAD:<oracle> | sha256sum` → identical (exit 0).
- `git show 197b5a4:verifiers/verify_harness_independent.py | sha256sum` → `872993f8…`; same for 75f671b → `872993f8…`; `git diff 197b5a4 75f671b -- verifiers/verify_harness_independent.py | wc -l` → `0`.
- `git ls-tree 197b5a4 -- verifiers/verify_harness_independent.py` → `100644 blob 06322fc5b0231d9bdc6cb4128c336cc5f1d53597` (matches instrument.json).
- `python3 -m py_compile .ufo/round-48/tools/config-root-ruler.py` → OK (exit 0).
- Oracle parse: `n_cases: 13`, `unique ids: True`, all cases carry both counts, derived mismatch-set == declared five (`equal: True`).
- Before-receipt extraction (exit 0): 13 cases, observed 2,2,2,2,2,2,3,3,3,2,2,2,3 in oracle case order; `base_prediction_met` true ×13; `target_failures` = declared five; mismatches/errors []; `remaining_not_observed` [].
