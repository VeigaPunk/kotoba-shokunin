# Round 49 falsify: NoHarmGates (no-harm battery)

HOLDS-BOUNDED. No check that is green at base a5adc146 is red at head c48793d across the eight-command battery. The bound: the eight named commands plus two R1 self-tests, run on this host today, in three layouts (plain clones, fleet-parent mirrors, byte copy of the lane). Three gates (substrate pins, surfaces, harness claims) are red at both commits from host state, so they certify nothing here.

## Findings (by severity)

1. **No harm found.** No check flips green to red (exit codes). No sub-check flips PASS to FAIL in any output. Table below.

2. **Trap, not harm: plain clones give false reds.** Clones named `base` and `head` make `verify_skill_checklist.py --json` exit 1 at both commits, with three FAIL rows: `trigger.name_directory` ("name 'kotoba-shokunin' != directory 'base'"), `trigger.citation_resolves` (`../.ufo/reports/round-7/kotoba.md`), and `governance.citation_resolves` (908 or 935 `..` citations resolve only from the fleet root). In a mirror (directory named `kotoba-shokunin`; parent holds symlinks to every fleet-root entry except the lane) the same command exits 0 with pass 11, fail 0, at both commits. Any battery run from a plain clone reads these as artifacts. Use the mirror layout.

3. **Real red, present at base and still at head (not harm, not fixed).** `verify_corpus_integrity.py` exits 1 at both. Head: "8/9 checks pass; DRIFT: corpus.pointers.report_dead", observed 2, expected 0. The dead pointers are `corpus/lessons/round-48-verifier-spotcheck.md:9` and `:23`, both written repo-relative as `.ufo/reports/round-48/kotoba.md`. The lane has no `.ufo/reports/round-48/` directory (`ls` returned "No such file or directory"), so this is a real repo-level dead pointer, not a clone artifact. The round's own record (`verifiers/corpus-baseline.json`, key `round49`) states the same and keeps `expect: 0`. Measured: base 4 DRIFT, head 1 DRIFT, which matches that record.
   Residual gate weakness: `corpus/README.md:68` cites the same pointer inside double quotes. `verify_corpus_integrity.py` (docstring lines 61-64; `inside_quotes`) exempts quoted report pointers as context. The exemption is documented, and the two lesson pointers are unquoted and counted, so I found no masking now. But any author can hide a dead pointer by wrapping it in quotes; the gate allows that by design.

4. **Red at base and head from host state (identical output; not harm).**
   - `check_substrate_pins.py` exit 1: `FAIL omp_binary_sha256: expect=fdbc8136… got=85d9daf3…` and `FAIL omp_binary_mtime … delta_ns=61606480536650`. The input is `/home/vgpnk/.local/bin/omp`, outside the repo.
   - `verify_surfaces.py --json` exit 1: `"fail": 2, "pass": 5`; `surfaces.literal_present` and `surfaces.no_uncovered_class` FAIL ("0 loader class(es) extracted from the omp dump").
   - `verify_harness_claims.py --json` exit 1: seven DRIFT verdicts (omp.db.rows, omp.offered.skills, omp.cache.misses, omp.catalogue.total, omp.catalogue.missing_names, omp.cache.verified_skills, oc.roots.names_plus_builtin).
   Every layout reads the same host inputs, so these are not clone artifacts. Outputs are byte-identical at base and head.

5. **Gate gap (calibration).** `verifiers/check_sibling_census.py` is new at head (923 lines, has `--self-test`). It has no entry in `verifiers/floors-registry.json` and no row in `check_assertion_floors.py`. A grep for `census|sibling` in both files returns nothing. Its self-test assertion count is therefore not ratcheted. I did not run it.

6. **Label mismatch in C2 (calibration).** Commit c48793d says boxes dispatch.04 and dispatch.08 are "executed by verify_dispatch_prompts.py". The map `verifiers/checklist-baseline.json` (lines 172 and 196) says `delegated:verifiers/verify_dispatch_prompts.py`, and the skill checklist counts "41 boxes mapped (8 executed, 2 delegated, 31 unexecuted)". The checklist checks that a delegated target exists and has instrument shape (docstring lines 59-62; `is_instrument`, line 911). I saw no code path that runs it. So a PASS from `verify_skill_checklist.py` does not prove those two boxes. Their proof lives only in the separate box-proof command. The commit wording should say "delegated".

7. **R1 repair holds on its self-tests.** `verify_harness_independent.py --self-test`: exit 0 at base (116 assertions, 0 failures) and exit 0 at head (123 assertions, 0 failures). The floor move 116 to 123 in `check_assertion_floors.py` matches. `compare_harness_independent.py --self-test`: exit 0 at both (330 assertions).

## Battery (exit codes and summary lines)

| check | plain base | plain head | mirror base | mirror head | lane copy | base vs head output (mirror) |
|---|---|---|---|---|---|---|
| `verify_skill_checklist.py --json` | 1 | 1 | 0 | 0 | 0 | differ (28 lines): delegated 0 to 2; unexecuted 33 to 31; budget, placeholder, citation, governance counts. Statuses unchanged; `"fail": 0, "pass": 11` both |
| `verify_skill_checklist.py --self-test` | 0 | 0 | 0 | 0 | 0 | identical: "0 failure(s) over 1845 assertions" |
| `verify_corpus_integrity.py` | 1 | 1 | 1 | 1 | 1 | differ: base "5/9 checks pass; DRIFT: tracked_files, unindexed, report_total, report_dead"; head "8/9 checks pass; DRIFT: report_dead" |
| `verify_corpus_independent.py` | 1 | 1 | 1 | 1 | 1 | differ: base unindexed=1 DRIFT, head unindexed=0 PASS; report_dead=2 DRIFT both |
| `check_assertion_floors.py` | 0 | 0 | 0 | 0 | 0 | differ: base 9 PASS lines, head 10 (harness_independent 116 to 123; new dispatch_prompts 32/32). No FAIL |
| `check_substrate_pins.py` | 1 | 1 | 1 | 1 | 1 | identical: "DRIFT 2/3 pins failed: omp_binary_sha256, omp_binary_mtime" |
| `verify_surfaces.py --json` | 1 | 1 | 1 | 1 | 1 | identical: `"fail": 2, "pass": 5` |
| `verify_harness_claims.py --json` | 1 | 1 | 1 | 1 | 1 | identical: 560 lines, 7 DRIFT verdicts |

Lane copy against mirror head: all eight outputs identical except line 1 of `corpus_independent` (the path string).

## Evidence (commands and exit codes)

- Clones: `git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin <scratch>/base`, then `git -C <scratch>/base checkout -q a5adc146a2995dcc5a95a6d8db6e5674f75191ac`; same for head at c48793dbe5eb30cd661f42ecad7399ae94e3d7ad. `rev-parse HEAD` matched both. Stderr empty in every run.
- Battery: `python3 -B <script> [args]` for each of the eight commands, cwd = clone root, stdin from /dev/null. Exit codes are the subprocess return codes.
- Mirrors: `ln -sfn /home/vgpnk/Projects/shokunin/<entry> <scratch>/mirror/<v>/<entry>` for each of the 51 fleet-root entries except `kotoba-shokunin`; the clone sits inside as `kotoba-shokunin`.
- Lane snapshot: `cp -a /home/vgpnk/Projects/shokunin/kotoba-shokunin <scratch>/mirror/lane/` (reads only). The lane itself was not run.
- Lane state, read only: `git --no-optional-locks status --porcelain --ignored=matching` (exit 0): no tracked changes; untracked `.ufo/waves/round-49/falsify-dispatch.json`, `falsify-spec.json`, `falsify-validation.stderr`, `falsify/`; ignored `.jj/`, `.ufo/interactive-sessions/`, `verifiers/__pycache__/`. `git --no-optional-locks rev-parse HEAD` = c48793dbe5eb30cd661f42ecad7399ae94e3d7ad (detached; jj colocated).
- Output diffs, `diff` exit codes, base vs head mirror: skill_json 1, skill_selftest 0, corpus_integrity 1, corpus_independent 1, assertion_floors 1, substrate_pins 0, surfaces 0, harness_claims 0. Head mirror vs lane copy: corpus_independent 1 (path string only), all others 0.
- Write scan (grep of the battery scripts): writes go only to temp fixtures or the clone. I did not diff the fleet root before and after.
- Lane path check: `ls /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/reports/round-48` returned "No such file or directory". `ls /home/vgpnk/Projects/shokunin/.ufo/reports/round-48` lists `kotoba.md`, `kotodama.md`.

## Residual risk and verification gaps

- The lane was not executed directly. The byte copy was taken while other seats were writing `.ufo/waves/round-49/falsify/`; it had the four untracked entries above and matched head mirror output.
- Host-state gates (item 4) depend on the omp binary and session logs. They can change without any repo change.
- Not run: `check_sibling_census.py` (self-test and content guard); `verify_dispatch_prompts.py` (self-test and `--box-proof`); any web source (none used).
- Log naming bug in my scratch: base and head self-test runs of `verify_harness_independent.py` shared one log file name, so the base full output was overwritten. The counts above come from each run's own exit echo line.
- Tools: none installed or updated.
- Scratch root: `/fast/scratch/hyaku/kotoba-r49/falsify/NoHarmGates/` (`base`, `head`, `mirror/{base,head,lane}`, `logs/`).
