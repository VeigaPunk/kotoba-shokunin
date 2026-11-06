# ReviewerCounterV4 — frozen v4 counter and control receipts

Seat: ReviewerCounterV4 (reviewer, r96-w1, leaf — no subagent dispatch).
Scope (read-only): `verifiers/fixtures/round-96/selftest-kills.py` and
`verifiers/fixtures/round-96/build-forgeries.py` at `679775abb9277a7b8d17f060b0f5b4ced2b127b6`,
against `plans/round-96.md` and the committed pre-data receipts. No lane file was written; the only
writes are this report and my scratch.
Scratch: `/fast/scratch/hyaku/kotoba-r96/ReviewerCounterV4` (`TMPDIR` + `HYAKU_SCRATCH`; removed
before yield). Scratch clone `$S/repo` at `679775abb9…`; `git -C $S/repo rev-parse --show-toplevel`
== `$S/repo`. Every counter run below used `$S/repo` as REPO, so the lane was never read as a clone
source or written.

## Verdict

**No blocking finding.** The v4 counter and the control-world builder reproduce every committed
pre-data receipt in my own scratch: base `c1` 0 of 11 UNMET rc 1; `r95c1` 3 of 3 MET rc 0; all five
forgery worlds UNMET with the plan's exact tallies. The three plan-named v4 rule changes are present
and the `r95c1` anchors are byte-identical to the round-95 `c1` anchors. Two low-severity
documentation/scope inconsistencies in the frozen plan are reported below; neither is a counter
defect and neither changes C1's predicate.

## Evidence (commands and observed lines)

### 1. Freeze identity

```
sha256sum verifiers/fixtures/round-96/selftest-kills.py   -> 1711b68fd9f443b53aa6878fdd367c8dc1cc6c38f4ec750d6725f0a0ab13b2b2
sha256sum verifiers/fixtures/round-96/build-forgeries.py  -> 61d813769f9fa62cd84fc58e1869e83fb70457df961438a21670dafe9b959c57
sha256sum verifiers/verify_dispatch_prompts.py            -> de9602710a67a3a54ca7ede0e64fcc8047410071b5df8f853e5cb401cc4adc2b
```
All three equal `receipts/freeze-shas.txt`; the five committed forgery patches also match their
recorded sha256. `git diff --stat 0f66016a 679775a -- verifiers/fixtures/round-95/
verifiers/fixtures/round-94/` is empty (the v3 counter is unchanged). `git status --porcelain -- verifiers/fixtures/round-96 verifiers/verify_dispatch_prompts.py plans/round-96.md`
is empty (frozen bytes are the lane bytes).

### 2. Base reading re-run (`c1` at 0f66016a)

```
HYAKU_SCRATCH=… python3 -B repo/verifiers/fixtures/round-96/selftest-kills.py c1 0f66016a… repo
honest rc 0 CLEAN: 0 failure(s) over 56 assertions
C1 targets killed 0 of 11 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 11 of 11; code decoys held 11 of 11
C1-PREDICATE-UNMET            (rc 1)
```
`diff` against `receipts/redbefore-c1-base.txt`: only the `repo` path on the claim line differs.

### 3. `r95c1` positive control re-run (at 0f66016a)

```
honest rc 0 CLEAN: 0 failure(s) over 46 assertions
R95C1 targets killed 3 of 3 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 3 of 3; code decoys held 3 of 3
R95C1-PREDICATE-MET           (rc 0; ~103 s)
```
`diff` against `receipts/poscontrol-r95c1-base.txt`: only the `repo` path differs.

### 4. Forgery worlds rebuilt with the frozen builder at 0f66016a

`python3 -B repo/verifiers/fixtures/round-96/build-forgeries.py 0f66016a… "$S/forgeries"` produced
five worlds whose `.patch` files are **byte-identical** (`cmp`) to the committed
`verifiers/fixtures/round-96/forgeries/*.patch`. Counter readings (each compared line-for-line with
its committed receipt; only the claim/rev/repo line differs):

| world | observed tally | receipt |
|---|---|---|
| f1-text-sniff | killed 0 of 11; comment 0/11; code 0/11; UNMET | matches |
| f2-crash-signal | killed 0 of 11 (run errors 1); decoys 11/11; UNMET | matches |
| f3-summary-no-line | killed 0 of 11 (run errors 1); decoys 11/11; UNMET | matches |
| f4-honest-trip | killed 11 of 11; honest REPORTED-FAILURE; decoys 0/11; UNMET | matches |
| f5-label-only | killed 0 of 11; decoys 11/11; UNMET | matches |

### 5. Honest run vs a normal `--self-test` run

```
normal : python3 -B verifiers/verify_dispatch_prompts.py --self-test   (cwd = clone) -> rc 0, "0 failure(s) over 56 assertions"
runner : v4.run_selftest(clone, instrument, env, original, src)                       -> rc 0, same last line
byte-identical stdout: True
```
The runner sets `__file__` = the instrument path, `sys.argv = [path, '--self-test']`,
`sys.path[0]` = the instrument's directory, cwd = the clone; the instrument's only path lookups are
`Path(__file__).resolve().parent(.parent)` (`DEFAULT_REPO`/`VERIFIERS_DIR` L92–93, SKILL.md L861) and
its own tempdir, and it imports stdlib only — so the honest run cannot differ.

### 6. `classify()` prefix conjunct, proved on the M2 shape

f3 world cloned at its commit, the `t04` mutation applied on disk, instrument run directly:

```
rc=1; last line "1 failure(s) over 57 assertions"; lines starting "self-test FAIL: " = 0
classify(1, out, 'self-test FAIL: ') = RUN-ERROR
```
So the prefix conjunct (not the exit code or the summary) is what classifies f3's `t04` as a
RUN-ERROR, i.e. not a kill. Across all seven committed receipts, 214 run lines (6 × 34 + 10) are
consistent with what `classify` can derive from `(rc, last summary)`; the only conjunct not visible
in a receipt is the prefix line, resolved by the re-runs above.

### 7. Exit ladder and scratch hygiene

bad claim -> rc 2 (usage on stderr); bad REV -> rc 2 (`C1-NOT-EVALUATED: REV deadbeef is not a
commit of …`); too many args -> rc 2. The counter's work root is empty after every run
(`shutil.rmtree` in `finally`).

### 8. Anchors, predicate, and the three named changes

- `r95c1` table vs v3 `c1` table (tuples compared after import): **identical** (targets and
  positive); `v3.PIN == v4.MB_PIN`; instrument string identical (`verifiers/check_mutation_battery.py`).
- Predicate: the normalised sentence (`<C>-PREDICATE-MET iff (honest) … HOLDS.`) is found verbatim in
  both `plans/round-96.md` and the counter header.
- The three named rule changes are present: claim table with `instrument` + `fail_prefix`
  (L80–81, L110–111, L132–137, L229–230), the `elif`-chain climb (L188–204), the `# r96-decoy`
  marker and `kotoba-r96` scratch (L23, L59, L240, L296). Code semantics outside these are unchanged
  from v3 (`classify` L132–137, `run_selftest` L161–171, `code_decoy` L174–218, `main` L223–321).

### 9. `code_decoy` climb probes (synthetic + real anchors)

| probe | result |
|---|---|
| three-`elif` chain, 3rd arm mutated | compiles; whole chain carried under one guard; executed output identical (`[4, 1, 2, 3, 4, 4]`) |
| 2nd arm mutated | compiles |
| two arms of the same chain in one mutant | compiles; spans dedup to one guard |
| statement in an `else:` body | compiles; no climb |
| `else:` line rewritten to `elif` (fail-closed probe) | SyntaxError -> `NotEvaluated` (exit 2, never a kill) |
| two sibling chains | compiles; two guards |
| nested chain | compiles |
| outer + nested changed in one mutant | compiles; two guards; original chain intact |
| real `t05` / `t07` anchors | compile (+7 / +13 lines); mutated token present |

The guard `if __name__ == "__decoy__":` is false both under the runner (`__name__ == "__main__"`)
and under any import, so the inserted block is dead code; the original chain follows it unchanged.

### 10. Landing corroboration (peer receipt, not re-run by me)

`ExecArmsR96/c1-counter.txt` at candidate `443430a6…` reads `C1 targets killed 11 of 11 (run errors
0); positive killed 1 of 1; honest CLEAN; comment decoys held 11 of 11; code decoys held 11 of 11`
and `C1-PREDICATE-MET`, with `0 failure(s) over 78 assertions`; `r95c1` still MET. This is
consistent with the counter's design (it does not hardcode the assertion count, and the decoy
machinery survives a +128-line insertion inside `self_test()`). I did not re-run the candidate.

## Findings (severity order)

### F1 (LOW, plan precision) — the v4 counter drops the `r94c1` claim table; the plan says "v4 changes are exactly" the three

- Evidence: v3 `CLAIMS` keys are `['c1', 'r94c1']`; v4 keys are `['c1', 'r95c1']`. The v3 `r94c1`
  block (`k1-worktree-manifest`, `k2-label-every-cne`, `k3-accept-added-rows`, positive
  `k0-accept-any`) is deleted. The plan §Counting command says "The three v3 rules are kept; v4
  changes are exactly: 1. … 2. … 3. …" — the removal is not among them.
- Impact: none for C1. The plan's no-harm battery routes `r94c1` to the round-95 counter
  (`selftest-kills.py c1|r94c1 <rev>`), and no round-96 script calls the v4 file with `r94c1`
  (`grep -rn r94c1` finds only round-95 material). A caller who tries `r94c1` on the v4 file gets
  the usage error (exit 2), not a wrong reading.
- Disposition: record in the round-96 lesson as a plan-precision note (the plan is frozen and the
  reading is already taken; an addendum now would be after scoring). Do not edit the counter.

### F2 (LOW, plan/receipt inconsistency) — "22 hand mutants, 17 survive" vs the receipt's 18 survivors

- Evidence: `awk -F'\t' '/^m-/{n++; if ($2 ~ /rc 0/) s++; else k++} END{print n, s, k}'` on
  `receipts/recon-sweep.txt` -> `22 18 4`. The four non-zero are `m-legacy-as-baseline` (1 failure),
  `m-l1-in-08` (`TypeError`), `m-md-strip` (5 failures), `m-file-na-over-fail` (10 failures), i.e.
  3 reported failures + 1 crash; 18 mutants exit 0 and survive. The plan's C1 bullet says "22 hand
  mutants, 17 survive the 56-assertion self-test".
- The 11 frozen targets are all among the 18; the claim "the self-test does not observe these
  behaviours" is unaffected. If the L1 intended to exclude an equivalent mutant
  (`m-placeholder-re-angle`, `<[^<>]*>` -> `<[^<>]+>`, which differs only on the empty `<>`),
  18 − 1 = 17 — but the plan does not say so.
- Related: the plan's disclosed bound names three "other survivors" (sentence-final `.`, empty
  baseline, fleet-root stem); the receipt has seven others not in the set
  (`m-rstrip-dot`, `m-fleetroot-no-baseline`, `m-fleetroot-stem-pass`, `m-empty-baseline-pass`,
  `m-noreport-08-pass`, `m-placeholder-re-angle`, `m-stem-sibling-pass`). Read as examples the
  sentence is fine; read as exhaustive it undercounts.
- Disposition: correct the number (and, if intended, state the equivalent-mutant exclusion) in the
  round-96 lesson / LOG. No counter change.

## Answers to the assigned questions

1. **Are the changes exactly the three the plan names?** The three *rule* changes are present and
   are the only rule changes (`classify` gains `fail_prefix`; `run_selftest` gains `instrument`;
   `code_decoy` gains the parent map + climb; marker/scratch renamed). The file diff additionally
   removes the `r94c1` claim table, which the plan's "exactly" does not name -> F1.
2. **Do the `r95c1` anchors equal the round-95 `c1` anchors byte-for-byte?** Yes — targets and
   positive tuples compare equal, and `PIN`/`MB_PIN` are the same literal.
3. **Is the `elif` climb behaviour-neutral and fail-closed?** Yes. Behaviour-neutral: the guard is
   false at run time and the original chain is preserved; an executed behaviour comparison is
   identical. Fail-closed: any shape the climb does not cover (e.g. an `else:` line rewritten to
   `elif`) fails the compile guard -> `NotEvaluated` -> exit 2, never a kill. A three-`elif` chain,
   two arms in one chain (dedup), two sibling chains, nested chains, and `else:`-body statements all
   compile; the real `t05`/`t07` decoys compile with the mutated token present.
4. **Does `classify()` with the `self-test FAIL: ` prefix classify every committed receipt line
   correctly?** Yes. 214 receipt run lines are consistent with the `(rc, last summary)` derivation;
   the f3 probe isolates the prefix conjunct (rc 1 + `1 failure(s) over 57 assertions` + 0 prefix
   lines -> RUN-ERROR). All seven readings re-run and match.
5. **Can the honest run differ from a normal `--self-test` run?** No — byte-identical stdout and rc;
   the `__file__`-relative SKILL.md lookup and `sys.path[0]` resolve to the same clone paths, and
   the instrument imports stdlib only.
6. **Re-runs vs the committed receipts?** Base, `r95c1`, and all five forgery worlds match (only the
   repo path on the claim line differs).
7. **Is the predicate sentence identical in the plan and the counter header?** Yes, verbatim after
   normalising markdown emphasis and whitespace.

## Residual risk and verification gaps

- The counter-mutation matrix is `MutTesterCounterV4`'s item, not mine. From reading the counter, the
  committed controls do not expose at least: a counter forcing `pos = 1` (M8 shape), weakening
  `found != count` to `<` (M12), removing the restore guard (M13), or reading the first summary
  instead of the last (M14). The plan explicitly does not claim counter-mutation coverage; these are
  gaps in the counter's *own* control battery, not in C1.
- The v3 code-object-sniffer bound is disclosed and unchanged; I did not build a code-object
  sniffer, and the adversarial side is `ExecCounterForgeryR96`'s item.
- Forgery-world commit hashes differ from the committed receipts (timestamps); I compared readings
  and rebuilt patches byte-for-byte, not commit hashes.
- The candidate reading at `443430a6…` is ExecArmsR96's receipt; I did not re-run the counter at
  that revision.
- One residual landing risk for the L1: the counter requires each frozen anchor to match exactly
  once (`found != count` -> could-not-evaluate). The arms candidate's receipt shows all 11 mutants
  ran, so the anchors are still unique there; any later edit to `verify_dispatch_prompts.py` must
  preserve that.

## Tooling

No tools installed or upgraded. Runs used the host `python3` (stdlib only) and `git` read-only
operations plus scratch-clone commits inside `$S/repo`; no pacman/uv/npx action was needed.
