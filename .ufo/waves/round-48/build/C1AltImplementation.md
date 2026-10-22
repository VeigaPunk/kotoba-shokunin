# C1AltImplementation — competing implementation of the configured-root contract

Seat: `KotobaR48.C1AltImplementation`. Scope: write an independent implementation of
`.ufo/round-48/oracle/config-root-cases.json` `contract.new_behavior`, measure it with the
committed ruler, then diff it against the scratch candidate. The lane checkout was not
modified except for this report file.

## Findings

1. My independent implementation of the contract passes the committed ruler: verdict `clean`,
   0 target failures, 0 behavioral mismatches, exit 0 over all 13 oracle cases.
2. The base control reproduces the frozen before state exactly: 5 target failures (the five
   ids the oracle predicts) and ruler exit 1.
3. The competing candidate patch also passes the ruler (I re-ran it myself; exit 0, verdict
   `clean`). So the two implementations are behaviourally identical on every axis the oracle
   measures.
4. They differ in three places outside the oracle's measurement, listed in the table below:
   an unreadable root (crash vs graceful degradation), the wording of the row's detail text,
   and the presence of a `--self-test` regression arm. The candidate ships **no** self-test
   arm, so the plan's Q05 ("the fix must ship its own regression arm in the consumer's
   `--self-test`") is unmet by the candidate patch as it stands.
5. Recommendation: land my version, or the candidate's enumeration plus my arm. Reasons in
   "Recommendation" below.
6. Flag for the L1: the lane working tree already carries the candidate implementation as an
   uncommitted modification (`verifiers/verify_harness_independent.py`, +13/-8 versus
   `75f671b`); the file is byte-identical to the candidate commit's file. Landing my version
   means committing a different consumer sha256 and re-running the ruler with it (I did:
   receipt `ruler-1`, exit 0).

## Behavioural differences (mine vs the candidate patch)

| Axis | Candidate | Mine | Observable difference |
|---|---|---|---|
| Readability of a root | `path.iterdir()` unguarded → `PermissionError` aborts the whole derivation | `OSError` caught → the root contributes no names, the run continues | Measured: on an unreadable configured root the candidate raised `PermissionError`, mine returned `oc.roots.names_plus_builtin=3`. The oracle has no unreadable-root case, so neither is wrong there; the contract says "readable", so degrading is the reading that keeps the instrument alive. |
| Symlinks | follows a symlinked root and a symlinked `SKILL.md`; a dangling `SKILL.md` symlink and a *directory* named `SKILL.md` do not count | identical | Measured on one tree carrying all four shapes: both returned 5. No difference. (The harness `verifiers/verify_harness_claims.py:476` uses `.exists()` and only the plural root — a harness-versus-instrument asymmetry that C1 does not claim to close.) |
| Path normalisation | joins the configured roots into the *string* set `sources \| configured`, so a log-named spelling of the same directory is enumerated twice | keeps path objects; the two root families are enumerated separately | No difference in the value: names are a set, so a root reached by two spellings contributes its names once. Only the number of directory listings differs, not the row. |
| Ordering | sorts the union of path strings, then sorts each directory's entries | sorts log sources, then the configured roots in the fixed order `skill`, `skills`; sorts each directory's entries | No difference: the row is a count over a set. |
| Detail text | `"... the configured --oc-config roots (present: %s) ..."` | `"... the configured --oc-config roots (%s) ..."` | Wording only. Both fix the base's mislabelled `"%d configured dirs present: %s"`. The ruler compares row values and statuses only, never the evidence string; no check id, value or status changes in either version. |
| Regression arm | none (the patch touches `derive()` only) | two assertions in `--self-test` over a synthetic configured-root tree | The arm fails on the pre-round-48 code (measured: exit 1, "got 2 want 3"), so it is a real arm and not a tautology. |

## Recommendation

Land mine (patch below), or equivalently the candidate's `derive()` change plus my arm.

- Both satisfy the frozen contract; the choice is not about correctness of the count.
- Mine closes Q05, which the candidate patch leaves open, and the arm is measured to fail on
  the pre-fix code.
- Mine cannot be taken down by an unreadable configured root, which is exactly the input
  class the claim is about ("a skill placed in `--oc-config/skill` ... is invisible").
- The operator lives in one named function used by both root families, so "the same operator
  for every root" is structural rather than a copy that can drift.
- Cost: my version is larger (63 insertions / 13 deletions against 13/8) and the helper's
  docstring is longer than the rule needs. If the L1 prefers the smaller diff, the
  candidate's enumeration plus my 23-line arm is the minimal complete form.

Landing either version changes the consumer sha256, so the ruler must be re-run against the
landed commit with that sha256. The run for my version is already done (exit 0).

## Evidence

Commands, exit codes and hashes (all run in this session):

- Private clone: `git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin work`, then
  `git checkout 75f671b109d8eddd0d64c1429bd6379fe577175a` → exit 0.
- My commit: `ce26e4a71b9fba4cd3ef5a0bad90580f83844e53` on branch `r48-c1-alt` in
  `/fast/scratch/hyaku/kotoba-r48-a2/seats/C1AltImplementation/work`; consumer sha256 at that
  commit `f9aa46801eddbb9e7b384ca32a40f7dcb142f22233a5315efc5c40881bedbc62`.
- Base control, ruler: `python3 -B .ufo/round-48/tools/config-root-ruler.py --repo <clone>
  --revision 197b5a4087bad49a465df7d13d7e821fe4cf227b --consumer-sha256 872993f8…
  --oracle .ufo/round-48/oracle/config-root-cases.json --oracle-sha256 1d09a38c… --scratch
  …/ruler-0-base` → **exit 1**, verdict `failed`, target failures `["singular-unlogged",
  "plural-unlogged", "both-distinct-unlogged", "same-name-both-config-roots",
  "configured-plus-other-log-root"]` (exactly the oracle's `expected_before_target_failures`).
  Receipt `…/ruler-0-base/receipt.json`.
- My implementation, ruler (the assigned command, with the lane's oracle and baseline
  receipt): `--repo …/work --revision ce26e4a71b9fba4cd3ef5a0bad90580f83844e53
  --consumer-sha256 f9aa4680… --oracle …/oracle/config-root-cases.json --oracle-sha256
  1d09a38ce04d6c0ab9a1c4edd7f4255978a0c2b8d44ce037d10fcd37d756b883 --scratch …/ruler-1
  --baseline-receipt .ufo/round-48/verification/before-configured-root.json
  --baseline-sha256 8bec447aa538446e84b7cb87b902c5f1021c42bd7a01f81ea14313262f7e2312` →
  **exit 0**, verdict `clean`, 13 settled cases, `target_failures: []`,
  `behavioral_mismatches: []`, `evaluation_errors: []`; consumer sha256 before and after the
  run identical (`f9aa4680…`). Receipt `…/ruler-1/receipt.json`. Per-case observed counts
  equal the frozen expected counts: control 2, singular-unlogged 3, plural-unlogged 3,
  both-distinct-unlogged 4, configured-duplicates-agent 2, same-name-both-config-roots 3,
  singular-already-logged 3, plural-already-logged 3, configured-plus-other-log-root 4,
  non-skill-child-files 2, skill-named-directory 2, empty-config-roots 2,
  duplicate-log-source 3.
- Competing candidate, ruler (same command against the scratch candidate branch): `--repo
  /fast/scratch/hyaku/kotoba-r48-a2/cand --revision 26035dcec54d8e42f3a8b47ae8ca551c18aec295
  --consumer-sha256 2d824c0b3d4954c9a01868ee7c9b44c72b77bb5054419cf0539f6e4082f1b88a` →
  **exit 0**, verdict `clean`, 0 target failures, 0 mismatches. Receipt
  `…/ruler-2-candidate/receipt.json`.
- Oracle and baseline hashes re-measured in the lane: `1d09a38ce04d6c0ab9a1c4edd7f4255978a0c2b8d44ce037d10fcd37d756b883`
  (oracle) and `8bec447aa538446e84b7cb87b902c5f1021c42bd7a01f81ea14313262f7e2312`
  (before receipt); ruler sha256 `01af33a6724cb91ddcfd09b690fa7ba68114d799cc4552fa65d6519c3f78bd45`.
- Consumer self-test on my tree: `python3 -B verifiers/verify_harness_independent.py
  --self-test` → **exit 0**, "0 failure(s) over 106 assertions".
- Arm falsification: the same file with only the configured-root enumeration removed (pre
  round-48 behaviour) → **exit 1**, "3 failure(s) over 69 assertions", of which two are the
  new arm ("configured roots count without a log mention: got 2 want 3", "a name offered by
  two roots counts once: got 2 want 3"). The third failure ("fixture dir present") is an
  artefact of running the copy outside the repository tree, not of the change.
- Unreadable-root probe (`probe_unreadable_root.py`): candidate → `PermissionError: [Errno
  13] Permission denied`; mine → `oc.roots.names_plus_builtin=3`.
- Symlink probe (`probe_symlink_semantics.py`, tree with a symlinked configured root, a
  symlinked `SKILL.md`, a dangling `SKILL.md` symlink and a directory named `SKILL.md`):
  candidate `3` then `5` (first run used relative symlink targets and was void; re-run with
  absolute targets), mine `5` — identical.
- Patch delivery: `/fast/scratch/hyaku/kotoba-r48-a2/seats/C1AltImplementation/c1-alt.patch`
  (plain diff against `75f671b`; `git apply --check` on a pristine checkout of the base →
  exit 0, and the applied file hashes to `f9aa4680…`), plus `c1-alt-mail.patch`
  (`git format-patch`) for the commit.

## Risks and blockers

- Live-value risk: the instrument now counts the configured roots, while the harness
  (`verifiers/verify_harness_claims.py:472`) counts only `~/.config/opencode/skills` and
  uses `.exists()` rather than `.is_file()`. On this host neither `~/.config/opencode/skill`
  nor `~/.config/opencode/skills` exists, so the live `oc.roots.names_plus_builtin` does not
  move; on a host that has them the two instruments can disagree. That asymmetry is outside
  C1's declared scope (the claim is about the independent instrument's own root set).
- The lane working tree is dirty with the candidate implementation; committing it is the
  L1's decision. I did not touch the lane tree.
- No tooling was installed or upgraded in this seat (no pacman, no uv, no downloads); the
  measurements used only the repository's own Python 3 and the committed ruler.
- I did not read the candidate patch before writing my implementation, as instructed; it was
  read only after my commit and my clean ruler run.
