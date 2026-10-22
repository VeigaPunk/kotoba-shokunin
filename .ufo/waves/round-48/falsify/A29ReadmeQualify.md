# A29ReadmeQualify — falsify report, round 48 attempt 2

Seat: KotobaR48.A29ReadmeQualify (leaf). Judged on: freshness.
Target: `corpus/README.md` at 887b6af54d3f4446f1fe51dc16f26b2e83bc82e1. Clauses at lines 38 and 59; index rows at lines 66 and 67.
Lane HEAD moved during the run: 84b9c9b → d28b16b → 2788704 → 48819b9 → eb5a80f (last read 09:04Z). `git diff 887b6af eb5a80f -- corpus/README.md` is empty, so the README findings hold at HEAD too.
Installs: none. Lane writes: this file only. Clones, layouts, fixtures and outputs sit under `/fast/scratch/hyaku/kotoba-r48-a2/seats2/A29ReadmeQualify/`. Lane git commands were read-only, though `git status` may refresh `.git/index` stat data (no staging, no commits). Every verifier ran with `python3 -B`.

## 1. Verdicts

| # | Target | Verdict | Severity |
|---|---|---|---|
| 1 | README:38 "exit 2 false blocker still holds" | CONFIRMED at 887b6af, 2 of 2 runs | — |
| 2 | README:38 "at 75f671b the live join exited 2" | DEFECT: the exit-2 record used an uncommitted instrument; committed 75f671b exits 1 | MEDIUM |
| 3 | README:38 "harness read 21/28" | CONFIRMED: 21 PASS, 7 DRIFT, same seven ids at 75f671b and 887b6af | — |
| 4 | README:38 "re-run the recipe on the tree you cite" | DEFECT: the recipe reads host state, so a tree does not pin the outcome | MEDIUM |
| 5 | README:59 "not a live result" | CONFIRMED | — |
| 6 | README:59 body "remains protocol 24/24 … zero disagreements" | REFUTED: committed joins read 18/24 with 6 disagreements | MEDIUM |
| 7 | README:66 Frontmatter rule authorities row | CONFIRMED; one stale detail string at 887b6af | LOW |
| 8 | README:67 Round-48 lessons row | CONFIRMED with freshness gaps | LOW–MEDIUM |
| 9 | Horizon numbers 2315 and 2343 | CONFIRMED | — |
| 10 | verify_corpus_integrity.py --json at 887b6af | CONFIRMED: exit 0, 9/9 PASS | — |
| 11 | verify_corpus_independent.py --json at 887b6af | CONFIRMED: exit 0, 6 PASS + 3 INFO, counts agree | — |

## 2. What the live join reads now

| run | committed tree | UTC window | exit | result |
|---|---|---|---|---|
| R1 | 887b6af | before 08:53 | 2 | false blocker on omp.catalogue.{found,matched,missing_names,total}: declared candidate_blocks 5860, recomputed 5885 |
| R2 | 887b6af | 08:57:26–08:58:19 | 2 | same four rows: declared 6003, recomputed 6006 |
| R3 | 887b6af, recheck stubbed (diagnostic, not a recipe result) | 09:00:24–09:00:53 | 1 | protocol 18/24, strict 14/24, 6 disagreements, 4 adjudicated, 4 scoped out |
| R4 | 75f671b | 08:54:12–08:55:06 | 1 | no false blocker; same 6 disagreements; protocol 18/24 |
| R5 | 48819b9 | 09:03:49–09:04:40 | 1 | no false blocker; same 6 disagreements; protocol 18/24 |

The six disagreements, independent → live: oc.roots.names_plus_builtin 10→12; omp.cache.misses 3→4; omp.cache.verified_skills 7→11; omp.descriptions.over_cliff 10→11; omp.descriptions.unmodelled 3→0; omp.offered.skills 10→11. They match across R3–R5, minutes apart, so this is not a timing race. Their cause is not isolated here.

Live harness (`verify_harness_claims.py --json`): exit 1 with 21 PASS / 7 DRIFT at 887b6af (08:54Z) and at 75f671b (08:55Z). The seven DRIFT ids match `.ufo/waves/round-48/build/FrReadmeQualify.md` lines 116–117.

Why exit 2 appears: build_meta runs the live leg, then the independent leg, then `check_scope_probes` → `recompute_probe` (compare_harness_independent.py:939–1024, :1147–1154). Any CompareError returns 2 (:2564–2565). The probe reads `$HOME/.omp/agent/sessions` (verifiers/harness-independent-scope.json `probe_contract.target`; verify_harness_independent.py:307–309). That store held 3142 jsonl files at 08:53:18Z, 78 of them modified in the prior two minutes. At 09:03:01Z it held 3212, 64 modified in the prior minute. A 50-second join therefore sees a moved carrier while the fleet runs. SCORECARD.md:104 at HEAD already logs this as standing debt HIGH-3 ("snapshot-pinned carrier for the scoped-out probe").

## 3. Clause at README:38 (round-37 row)

- Exit 2 still holds at 887b6af (R1, R2).
- "at `75f671b` … exited 2": DEFECT. The only base exit-2 record is FrReadmeQualify.md F3 (lines 49–57). Its independent leg was an uncommitted candidate, sha256 2d824c0b…. No commit carries that sha. `git log -- verifiers/verify_harness_independent.py` gives blob hashes 872993f8 (base), d67b1b6e (887b6af), 0f33f600 (48819b9) and two older ones; none is 2d824c0b. A clean clone at 75f671b exits 1 (R4). The clause dates the exit to a commit without disclosing this.
- "re-run on the tree you cite": not a usable remedy. Committed bytes gave exit 1, 2, 2, 1, 1 across R1–R5.
- Pointers: FrReadmeQualify.md and FrCensusAndScorecard.md are not in the 887b6af tree (`git cat-file -e 887b6af:.ufo/waves/round-48/build/FrReadmeQualify.md` fails). Both exist from 84b9c9b on. The second is a bare name with no path. LOW.
- "round-47 frozen-carrier join 21/24 at base, 20/24 at tip": CONFIRMED against corpus/lessons/round-47-verifier-spotcheck.md:34 ("21/24→20/24") and :39 ("exits2 at base and landing").

## 4. Clause at README:59 (round-41 row)

- "not a live result": CONFIRMED (R1–R5; SCORECARD.md:104).
- Body, present tense, not edited in place: "a fresh live producer/join remains protocol 24/24 (strict 20/24 …), with zero disagreements". REFUTED: committed joins read 18/24 protocol, 14/24 strict, 6 disagreements. The 4 adjudicated and 4 scoped-out counts still match.
- "live join exit 2 on 2026-10-22": one of two outcomes. Exit 2 at 887b6af; exit 1 at 75f671b and 48819b9. Name both.
- "round-46 record on its frozen carrier": consistent with LOG.md:2244 (P1 live join evidence). Not re-verified.
- Pointer FrReadmeQualify.md: absent at 887b6af, as above.

## 5. Index row README:66 (Frontmatter rule authorities, round 48)

- File exists and is indexed (integrity: unindexed 0, missing_paths 0).
- Source map matches SOURCES.md and the entry: S018 spec, S017 skills-ref, S019 Anthropic docs, S012 packager, S021 Codex docs, S020 lane check.
- Re-opened today, UTC 09:00–09:03, read-only fetches, no fetched code run:
  - S018 specification.md: 7608 B, sha256 9a67de89… matches; the name-charset sentence is present.
  - S019 best-practices.md: 42169 B, sha256 f0a5d61b… matches; "Cannot contain XML tags" is present.
  - S012 quick_validate.py:79 "# Check for angle brackets"; sha256 67cf5703… matches.
  - S016 index.ts:24 OPENCODE_SKILL_PATTERN matches.
  - S017 validator.py:54 isalnum line matches; sha256 b5ee3d85… matches.
  - S021 "By default, this list uses at most 2% of the model's context window, or 8,000 characters when the context window is unknown." is present.
- Counterexamples, lane column only, reproduced on three scratch fixtures with `verify_skill_checklist.py --check trigger.no_xml_tag` at 887b6af: alias `description: *d` → PASS (exit 0); escaped `\u003cskills\u003e` → FAIL (exit 1); Unicode name `技能-测试` → PASS (exit 0). These match the entry's table. The packager and skills-ref columns were not re-run.
- LOW: at 887b6af the check's own detail strings still cite S001/S003, which the entry calls superseded. HEAD d28b16b corrected them to S018/S019.

## 6. Index row README:67 (Round-48 lessons)

- "LOG.md round-48 entry": absent at 887b6af; present from 84b9c9b on (LOG.md:2345). A forward reference at its own commit. LOW.
- "## Mistakes (M24–M27)": present at 887b6af with the described content. HEAD adds M28 ("Hash match read as custody", d28b16b) and a "Falsify-wave corrections" section. The README row was not updated, so it is incomplete at HEAD. LOW.
- "## Gate" rows S016–S021 with access times: present (S016 08:13:22Z, S017 08:16Z, S018 08:14:16Z, S019 08:16Z, S020 date only, S021 08:13:33Z). "Five routed items": five rows present.
- M26 says the producer "reads 11" on the live row at base and landing. Measured today: live oc.roots.names_plus_builtin = 12 at 75f671b (08:55Z), at 887b6af (08:54Z and 09:00Z) and at 48819b9 (09:04Z). FrReadmeQualify.md:24–25 recorded 12 at 08:19Z. The "11" is stale. LOW–MEDIUM. It sits in the lesson text, not the row.

## 7. Horizon numbers

- verifiers/verify_skill_checklist.py:377, `GOVERNANCE_ERRATA_HORIZON = 2315`, identical at 75f671b, 887b6af and eb5a80f.
- Enforcement: errata_problems rejects any row above min(horizon, len(LOG)) (:1528–1529). The only row, LOG.md:2111 (:378–383), came in with 7ad7fad (2026-10-21, round 47). "Round-47 erratum" is accurate.
- LOG.md lines (`git show <rev>:LOG.md | wc -l`): 75f671b 2343; 887b6af 2343; eb5a80f 2354 (39 lines past the horizon).
- governance.citation_resolves, run in a layout matching the lane's parent depth: PASS 872 at 887b6af; PASS 901 at eb5a80f; FAIL at 48819b9 (SCORECARD.md:112 cited the A24 falsify report, untracked at that commit; eb5a80f tracks it). My first run at clone depth failed on `../` tokens. That was my layout's artifact; I retract it.

## 8. Residual risk and gaps

- Exit codes are host-state samples. Each commit has the readings listed above; a later reading may differ.
- Not run: `--self-test` legs, the packager and skills-ref columns (both need fetched code), any re-join of the round-46 frozen carrier.
- Cause of the six stable disagreements not isolated (live sees 11 offered skills and 4 cache misses; independent sees 10 and 3).
- The lane working tree has uncommitted edits to verify_harness_independent.py, check_assertion_floors.py and floors-registry.json (other seats). My runs used committed bytes in clones only.

## 9. Suggested README edits (not applied; lane is read-only for me)

1. README:38: replace "at 75f671b … exited 2" with the dated run set: exit 2 at 887b6af on 2026-10-22 (two runs); exit 1 with six disagreements and protocol 18/24 at committed 75f671b and HEAD; say the first exit 2 came from an uncommitted candidate.
2. README:38: replace "re-run on the tree you cite" with "the recipe reads $HOME session and skill state; record run time and outcome."
3. README:59: date-stamp the body's "remains protocol 24/24 … zero disagreements" as a record; cite SCORECARD HIGH-3.
4. README:38 and :59: point the build-wave pointers at committed paths (they resolve at HEAD).
5. README:67: add M28 at HEAD; re-point or drop "LOG.md round-48 entry".
6. lessons round-48 M26: change "reads 11" to today's 12, or date it.

## 10. Command log (exit codes)

- compare_harness_independent.py --json: 887b6af → 2 (twice); 75f671b → 1; 48819b9 → 1. Diagnostic with recheck stubbed at 887b6af → 1.
- verify_harness_claims.py --json: 887b6af → 1; 75f671b → 1.
- verify_corpus_integrity.py --json and verify_corpus_independent.py --json at 887b6af → 0 and 0.
- verify_skill_checklist.py --check governance.citation_resolves --json (layout clones): 887b6af → 0; 48819b9 → 1; eb5a80f → 0.
- verify_skill_checklist.py --check trigger.no_xml_tag on fixtures at 887b6af: alias 0, escaped 1, Unicode 0.
- curl -fsSL for S012, S016, S017, S018, S019 → 0 each.
