# kotoba-shokunin verifiers — what each one checks

Moved verbatim from `SKILL.md` § Sources in round 54 (the bullets stood there from rounds 10–23); the
registry rows (entry command, verdict map, self-test, pinned values, write scope, owner) live in
`SKILL.md` § Gate registry, the lane's registry home under PROTOCOL.md § Gate standard. Paths below are
repo-rooted, as they were in `SKILL.md`, and "this file" in the moved text means `SKILL.md`.

- `verifiers/verify_harness_claims.py` + `verifiers/baseline.json` — the round-10
  executable form of the harness claim set (28 checks, 4 exit codes, `--self-test`);
  the authority for every harness number in this file.
- `verifiers/check_substrate_pins.py` — round 23: enforces the
  `verifiers/baseline.json` `measured_against` pins (omp sha256 + ns-exact mtime,
  opencode sha256; exit 0/1/2/3, '--self-test' builds inline tempdir fixtures (the committed `verifiers/fixtures/pins/` is evidence-only — round 28);
  hashes bytes, never execs; a red guard is fixed by re-record + mechanism note,
  never by weakening the pin).
- `verifiers/verify_corpus_integrity.py` + `verifiers/corpus-baseline.json` — the
  round-11 executable form of the *corpus-internal* citation rules (9 checks over
  tracked `corpus/*.md`: index coverage, lane-report pointers in all four shapes,
  `commit` citations resolve, no non-hash commit token; exit 0/1/2/3, `--self-test`).
  This file's own citations and root `LOG.md`/`SCORECARD.md` citations are instead
  executed by `trigger.citation_resolves` / `governance.citation_resolves` in `verify_skill_checklist.py`.
  Run it before shipping an artifact set; a dead pointer is then a drift report, not a reviewer's memory.
- `corpus/knowledge/corpus-integrity-round11.md` — what the corpus verifier checks,
  the three counting recipes it replaced (why each could not express its class),
  the exclusion shapes it must not report, and the check that was designed and
  rejected (revision pins: digests are not commits).
- `corpus/knowledge/cold-run-round11.md` — the non-author cold run of the corpus
  verifier (runner, tree, command, exit code, spot-checks); the evidence class
  this repo uses when a check must not be its author's only witness.
- `verifiers/verify_corpus_independent.py` +
  `corpus/knowledge/independent-verification-round12.md` — the **second**
  witness, and the right shape for one: a derivation written from the class
  spec by a lane that did not author `verify_corpus_integrity.py` (and did not
  read it), compared check-for-check on two trees (green live, red on a clone at
  `d49dfa5` with the same ten dead-pointer sites). A re-run of the author's
  script is not a second witness — it launders a broken model; the comparison's
  own artefacts this round were two claim/behaviour gaps in the author's script
  (a documented quoted-context rule that could never fire; an index census that
  read more of `README.md` than it claimed) and one shared property (pointer
  resolution is host-anchored, so a clone's green verdict is not hermetic).
- `verifiers/fault_injection_corpus.sh` — the planted-fault harness, in-repo so
  the "the checks fire" claim stops depending on `/tmp` scratch; plants one
  fault per clone and asserts the *class* that must fire, plus a must-not-fire
  equivalent mutation. **Mutating — not a smoke check** (round-8 box-3 cold run,
  break point B2): the default path `git clone --no-hardlinks`s this repo once
  per fault class into `${TMPDIR:-/tmp}/round12-faults.$$` and `rm -rf`s each
  world, so it runs deliberately, never as an "is everything still fine" probe;
  `--self-test` exercises the assertion machinery on fixture worlds without
  cloning the repo (it still creates, and on exit removes, one `${TMPDIR}`
  scratch dir).
