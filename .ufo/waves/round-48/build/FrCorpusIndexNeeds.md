# FrCorpusIndexNeeds — round-48 build, corpus index / baseline / registration needs

## Findings (first)

**This seat is a leaf executor for the round-48 BUILD wave: it reports what the two new corpus files (C2 knowledge entry + round-48 lesson) require from the corpus index, baselines and registrations, plus the `.ufo/round-48/` index question. It writes no corpus files; the L1 integrates.**

1. **At lane HEAD `84b9c9b`, all three corpus gates are green** (measured live, exit codes verbatim below). The required index rows and baseline re-record already landed in `887b6af`. Expected change per new file:
   - `corpus/knowledge/frontmatter-rule-authorities-round48.md` → one Coverage-map row in `corpus/README.md` whose column-2 token is `knowledge/frontmatter-rule-authorities-round48.md` (backticked, corpus-relative).
   - `corpus/lessons/round-48.md` → one Coverage-map row with column-2 token `lessons/round-48.md`. A single row carrying both tokens in column 2 also satisfies both instruments (measured: `unindexed=0` either way).
   - Each row's column-2 token must **exist on disk and be git-tracked** (`git ls-files corpus/`). A token for an untracked-on-disk file trips `stale_patterns` (measured `stale=2` when untracked, `stale=0` once `git add`ed).
2. **Baseline** `verifiers/corpus-baseline.json`: `corpus.index.tracked_files` expect must move 61 → 63 (two new corpus files). This is already re-recorded at `887b6af` (`expect: 63`, observed 63 → PASS). `report_total` stays 40 and `commit_total` stays 30 **only if** the new files add no report pointers and no `commit \`hash\`` citations; the landed lesson (64 lines) adds neither, so 40/30 hold. If later content adds a pointer/commit cite, re-record (command below).
3. **Re-record command** (no `--re-record` flag exists): `python3 -B verifiers/verify_corpus_integrity.py --no-baseline --json` → take the observed values → hand-edit `verifiers/corpus-baseline.json` checks.*.expect and add a `note:` line (matches the round-17 note pattern). `verify_corpus_independent.py` has **no baseline file** (all equal-mode checks are INFO) — it only needs the index rows; exit code depends on the zero-mode checks (unindexed/stale/missing/report_dead/commit_unresolvable/commit_nonhash).
4. **Checklist gate** `verify_skill_checklist.py --json` is unaffected by the two corpus files per se (its baselines maps SKILL.md boxes, not corpus files). It currently has **one FAIL** at HEAD: `governance.citation_resolves | SCORECARD.md:110: '.ufo/reports/round-48/kotoba.md' does not resolve from /home/vgpnk/Projects/shokunin/kotoba-shokunin`. This is a **registration requirement outside the corpus index**: the round-48 report file must exist in the lane repo at `.ufo/reports/round-48/kotoba.md` (closing the SCORECARD cite), like the lane-local reports in rounds 43–45 (rounds 46/47 were fleet-side and were not cited in SCORECARD). Verified in a fleet-shaped scratch: creating `.ufo/reports/round-48/kotoba.md` flips that check to PASS (901 governance tokens resolve). The L1 should land the round-48 report (tracked) to close this.
5. **`.ufo/round-48/` files committed by attempt 1 need NO corpus index entry** — the corpus census is scoped to `git ls-files corpus/`; `.ufo/` is outside it and contributes nothing to `tracked_files`/`unindexed`/`stale`. They need no README row. They need only to exist if cited from governance files (LOG.md cites `.ufo/round-48/verification/after-configured-root.json` — exists, resolves).
6. **Foreign-hash commit citations**: the working-tree SOURCES/C2 drafts initially used `commit \`69ef37e9\`` (upstream opencode/agentskills hashes). That form counts toward `commit_total` and trips `commit_unresolvable` in the lane repo (measured: 3–4 unresolvable → DRIFT). The landed versions avoid it by writing `upstream commit 69ef37e9` (no backtick after "commit"), so `commit_total=30`, `commit_unresolvable=0`. Keep that convention; never write `commit \`<foreign-hash>\`` in corpus files.

## Evidence

- Lane HEAD: `84b9c9b` (git rev-parse HEAD). Baseline re-record landed in `887b6af`.
- Live gates at HEAD (run in the lane checkout, `git stash` to a clean tree, no writes):
  - `python3 -B verifiers/verify_corpus_integrity.py --json` → `ci_exit=0`; observed `{tracked_files: 63, unindexed: 0, stale_patterns: 0, missing_paths: 0, report_total: 40, report_dead: 0, commit_total: 30, commit_unresolvable: 0, commit_nonhash: 0}`; DRIFTs: `[]`.
  - `python3 -B verifiers/verify_corpus_independent.py` → `ind_exit=0` (tail `exit 0`).
  - `python3 -B verifiers/verify_skill_checklist.py --json` → `sc_exit=1`; 10 PASS, 1 FAIL: `governance.citation_resolves | SCORECARD.md:110: '.ufo/reports/round-48/kotoba.md' does not resolve from /home/vgpnk/Projects/shokunin/kotoba-shokunin`.
- Corpus census at HEAD: `{index_patterns: 81, index_tokens_total: 81, corpus_md_files: 62, tracked_files: 63}` (61 → 63 tracked; 60 → 62 md against base 75f671b).
- Base state at 75f671b: tracked_files=61, report_total=40, commit_total=30, index_patterns=79, corpus_md_files=60.
- Scratch experiments (private clones at 75f671b, commit ids in scratch):
  - Placeholders only: `unindexed=2` → DRIFT (needs rows). One row with two column-2 tokens: `unindexed=0`, `stale=0`.
  - Untracked new file with row token: `stale_patterns=2` → DRIFT; after `git add`, `stale=0`.
  - Lesson citing `/home/vgpnk/Projects/shokunin/.ufo/reports/round-48/kotoba.md`: `report_dead=1` → DRIFT (file absent).
  - `commit \`69ef37e9\`` (7-hex, foreign): `commit_unresolvable=1`. `upstream commit 69ef37e9` (no backtick): not counted; `commit_total` unchanged.
  - Fleet-shaped scratch with `.ufo/reports/round-48/kotoba.md` created: governance check PASS (901 tokens; 9 quoted excluded, 3 schematic excluded, 1 recorded absence excused).
- New files (sha256): knowledge entry `72780970966b707ff6e81991c496d69aede786aa12b47282287a92fab6cb9b8e` (104 lines); lesson `41dbfe9d07f29a38d855cc7d5f5d5032b4162f338555d2c3c75f12c0d07d156a` (64 lines); README `c5b5d89a5256a39dfba53dc816db2f95ed2e044d310a1b1be6c4ec499cd246ca`; corpus-baseline.json `616e577a7f3173e88d6cda44d6c3b3c4379178a61a8f1e768f6a6730454d18d6`.

## Risks / blockers

- **Blocker (gate red at HEAD):** `SCORECARD.md:110` cites `.ufo/reports/round-48/kotoba.md`; the file does not exist in the lane. The L1 must land the round-48 report file (tracked) at that path, or amend the SCORECARD cite, before `verify_skill_checklist.py --json` returns 0.
- If round-48 content later adds `report` pointers to corpus files, the pointer target must exist at gate time (`report_dead` is zero-mode).
- Foreign/future commit hashes in corpus files must keep the no-backtick form.
- Lane repo is live and moving (HEAD advanced 75f671b → d1ae458 → 84b9c9b during this seat's run; sibling seats landed C1/C2 work). Re-measure at integration time if the tree changes again.
