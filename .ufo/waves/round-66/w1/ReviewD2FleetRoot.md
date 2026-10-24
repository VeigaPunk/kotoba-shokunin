# ReviewD2FleetRoot — commit resolver: lane-only, fleet-only, neither, same-token

Seat: reviewer (read-only, leaf). Axis: depth / calibration.
Pinned base: `11385e04e368c1e94ab1a5a89d7439033eb1f855` (`plans/round-66.md`).
Measured tip: lane Git HEAD `2a8eba56b3f9321b70c569fa2816d42237ca49a2`; the checkout was
clean for `corpus/` and `verifiers/` (only `.ufo` peer reports and the wave registry differ in
the jj working copy). A detached clone of HEAD had `git status --porcelain` = 0 lines.
Tested instrument bytes (HEAD, equal to the working-tree bytes and to the receipts' pins):

```
febfa57e64896a37cea740ee080ccd1ea0f994980ade0856fc2dc080c1386534  verifiers/verify_corpus_integrity.py
de51f45750bf31658cb8c0412a94f36e193704aab6e8c056c50de935887d71c9  verifiers/verify_corpus_independent.py
3129c0d7016467d93a3ea45a626dd1237bc92bd20d79bc09499c53c503293141  verifiers/check_r66_routed_repairs.py
0944ae98cbe52dfcc9b7836b68710be8758ad177a3bb8abe1dc476671c827d15  verifiers/corpus-baseline.json
```

Sandbox: `/tmp/r66-commit-resolver.PSifAd` (temporary; harness `harness.py` sha256
`874bbb7fbd4d70dcecabdc67f99c6b7c2eb2a7223f5e6cd768e391d6c28c4176`); git 2.56.0, Python 3.14.8.
No `lsp` device exists on this seat's surface (`read`, `bash`, `edit`, `eval`, `glob`, `grep`,
`write`), so caller/definition checks were made by importing the two resolvers and executing
them against the pinned bytes, not by reading and restating their text. The lane, its Git index
and its jj state were never written to.

## Verdict

The resolver is correct on all four required cases, counts one citation site once regardless of
how many repositories resolve it, keeps `^{commit}` peel semantics, and does not mask a
nonexistent commit. No defect in the resolver itself.

Two non-blocking cross-instrument counting divergences were found (P2, P3), plus one **blocking
C2 calibration gap at the round's final tree** (P1) that is outside the resolver but is measured
by the same commit counter: at HEAD `2a8eba5` the primary gate exits 1 with four DRIFTs while
the frozen routed counter still prints `2 of 2`, because its D2 arm pins the baseline file's
declared values rather than measuring the tree.

## Sandbox and exact commands

Fixture construction (deterministic identities/dates, so the SHAs below reproduce):

```
$ cd /tmp/r66-commit-resolver.PSifAd && python3 -B harness.py
```

The harness itself runs, with `GIT_*_DATE` fixed:

```
$ git init -q seed && printf 'seed\n' > seed/seed.txt
$ git -C seed add -A && git -C seed commit -q -m seed
$ git clone -q seed lane && git clone -q seed fleet          # S is one object in both repos
$ printf 'lane-only\n'  > lane/lane.txt  && git -C lane  add -A && git -C lane  commit -q -m lane-only  # L
$ printf 'fleet-only\n' > fleet/fleet.txt && git -C fleet add -A && git -C fleet commit -q -m fleet-only # F
$ git -C lane tag -a tagcommit -m tc <L> && git -C lane tag -a tagtree -m tt <L^{tree}>
```

```
TOKENS
  same-token(seed,in both) 9330c83fc9b630a1b6f7fd5950d5bded3023e8c5
  lane-only                ae92ed129b1137613ade0f2220cf171d24af2b81
  fleet-only               c20ac02bb8361b5be475786c7d6ea6103c4e35f6
  neither                  ffffffffffffffffffffffffffffffffffffffff
  lane blob                591a99d23933cf71c4cb7c85afa1cca0d1744c60
  lane tree                36b8d566b543be36af9d10494a7df7ac395ab7bc
  fleet blob               4ac9e7449bde0cda53c855bbbc5cc5db37a0818d
  fleet tree               fceeb67ed0bfff434b9191e9e195ddefa1328637
  tag->commit              1cc0c5fb69429ac55340e7114fa5da443156e19d
  tag->tree                4aba3b82b10125455d93813d3a15d8e0fc8a6e02
  cloned commits equal at seed: lane/seed=True fleet/seed=True
```

`fleet/` and `missing-fleet`, `not-a-repo`, `fleet-is-a-file` and `shallow-lane` are additional
sandbox roots used for the negative cases.

## Four required cases (integrity `commit_resolves(hex, repo, fleet_root)`)

```
CASE lane-only                                                  got=True   want=True   PASS
CASE lane-only, fleet missing                                   got=True   want=True   PASS
CASE lane-only, fleet is a file                                 got=True   want=True   PASS
CASE fleet-only                                                 got=True   want=True   PASS
CASE fleet-only, fleet missing                                  got=False  want=False  PASS
CASE fleet-only, fleet is a file                                got=False  want=False  PASS
CASE fleet-only, fleet not a repo                               got=False  want=False  PASS
CASE neither                                                    got=False  want=False  PASS
CASE neither, fleet not a repo                                  got=False  want=False  PASS
CASE same-token (in both)                                       got=True   want=True   PASS
```

Lane-first ordering is observable: a lane-only token still resolves with the fleet root missing
or replaced by a regular file, i.e. the hop is consulted only after the lane query fails.
`fleet_root` failure is never a new failure mode: missing, file and non-repo all read `False`
(the code guards `not fleet_root.is_dir()` at `verify_corpus_integrity.py:591-603`).

The same matrix through the independent resolver (`analyse_commits` with explicit `fleet_root`),
using one sandbox corpus file:

```
unresolvable: exactly [lane blob, lane tree, fleet blob, tag->tree, neither]  PASS
fleet=missing   -> 6 unresolvable (the 5 non-commits + fleet-only), no exception  PASS
fleet=not-a-repo-> 6 unresolvable, no exception                                  PASS
fleet=self(lane)-> 6 unresolvable (abspath self-hop guard skips the fallback)    PASS
SUMMARY: 43 checks, 0 failure(s)                                                 exit=0
```

## `^{commit}` semantics retained

```
$ git -C <lane> cat-file -e <lane blob>            -> exit 0
$ git -C <lane> cat-file -e <lane blob>^{commit}   -> exit 128
$ git -C <lane> cat-file -e <lane tree>            -> exit 0
$ git -C <lane> cat-file -e <lane tree>^{commit}   -> exit 128
$ git -C <lane> cat-file -e <tag->tree>            -> exit 0
$ git -C <lane> cat-file -e <tag->tree>^{commit}   -> exit 128
$ git -C <lane> cat-file -e <tag->commit>          -> exit 0
$ git -C <lane> cat-file -e <tag->commit>^{commit} -> exit 0
$ git -C <lane> cat-file -e <UPPER-40-hex>^{commit}-> exit 0
```

Resolver results:

```
CASE lane blob exists but is not a commit           got=False want=False PASS
CASE lane tree exists but is not a commit           got=False want=False PASS
CASE fleet blob exists but is not a commit          got=False want=False PASS
CASE fleet tree exists but is not a commit          got=False want=False PASS
CASE annotated tag -> commit peels                  got=True  want=True  PASS
CASE annotated tag -> tree does not peel            got=False want=False PASS
CASE 7-char lane abbreviation                       got=True  want=True  PASS
CASE uppercase lane token                           got=True  want=True  PASS
CASE peel arg spelled ^{commit}  got='abc1234^{commit}' want='abc1234^{commit}' PASS
```

Abbreviation keeps the peel: fleet blob prefix `4ac9e74` and fleet tree prefix `fceeb67` are
raw-present (`cat-file -e <prefix>` exit 0) but rejected under `^{commit}` (exit 128), so the
fleet hop cannot launder a nonexistent commit into a tree/blob citation. Integrity lowercases
before resolving (`verify_corpus_integrity.py:530`); git itself accepts uppercase hex, and the
independent resolver (no lowercase call) also returned `True`, so the two agree here.

## One citation, once

```
$ python3 -B -c '...citation_findings / analyse_commits on one-line fixture...'
independent/one same-token citation -> total 1, unresolvable 0      PASS
integrity /one same-token citation -> total 1, unresolvable 0      PASS
independent/two occurrences of one token -> 2                      PASS
independent/same token: 3 textual occurrences counted 3x           PASS
```

So the same-token case (an object present in both repositories) contributes **1** to
`commit_total`, not 2: the count is per citation site, and the lane/fleet hop is a boolean, not
an accumulator. Textual repetition on different sites is still counted per site (census
semantics): e.g. live corpus token `3b029b8` occurs 4 times and contributes 4.

Live tree cross-check at HEAD `2a8eba5` (`git cat-file -e` on every distinct token, all 44
candidate sites over 118 tracked corpus `.md` files):

```
lane-only 19 distinct, both 0, fleet-only 3, neither 4
fleet-only: def4b9f…, 7b370d5…, 1154d57…  (each a real fleet report commit)
neither:    451a02ff (code-span example), cfb894a5 (quoted meta-finding ×2), <hex>, round-N
```

Zero distinct tokens resolve in both repositories today, and every live (non-context) citation
resolves: the gate prints `commit_unresolvable=0 nonhash=0`. The fleet hop is not idle — the
r62/r65/r66 closure spot-checks cite fleet report commits that do not exist in the lane object
database, and `cat-file -e` confirms `lane=no fleet=yes` for them.

## Findings by severity

### P1 (blocking, C2 calibration) — the frozen after-predicate is false at the final lane tree; the routed counter is green anyway

Frozen text (`plans/round-66.md`, C2): *“Independently, `python3 -B
verifiers/verify_corpus_integrity.py` must exit 0 at the final lane tree.”* The tree at HEAD is
not the tree the receipts measured. Exact measurement, fresh detached clone of HEAD:

```
$ git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin head-clone
$ git -C head-clone rev-parse HEAD
2a8eba56b3f9321b70c569fa2816d42237ca49a2
$ cd head-clone && python3 -B verifiers/verify_corpus_integrity.py; echo exit=$?
corpus.index    tracked=119 unindexed=1 stale=0 missing=0  (136 FILE-column patterns over 118 md files)
corpus.pointers report_dead=0/82 commit_total=38 unresolvable=0 nonhash=0 (shapes [relative=1, absolute=44, tilde=1, bare=36], quoted-excluded=6, pointer-excluded=8; sites in --json)
DRIFT   corpus.index.tracked_files: observed=119 expected=118
DRIFT   corpus.index.unindexed: observed=1 expected=0 / empty
DRIFT   corpus.pointers.report_total: observed=82 expected=79
DRIFT   corpus.pointers.commit_total: observed=38 expected=37
5/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.index.unindexed, corpus.pointers.report_total, corpus.pointers.commit_total
exit=1
$ python3 -B verifiers/verify_corpus_independent.py; echo exit=$?
index   tracked_files=119 index_tokens=136 (outside coverage map=18) unindexed=1 stale=0 missing=0
commits candidates=44 citations=38 hex=38 quoted=6 nonhash=0 unresolvable=0
  corpus.index.unindexed                 zero     observed=1 DRIFT
exit=1
```

At `9e75e73` (the tip the closure lesson cites; the receipts themselves measured `fc1b71e`),
the same commands are green:

```
$ git -C head-clone checkout -q --detach 9e75e7345574af59d0585429a0f25b6179aa375d
$ python3 -B verifiers/verify_corpus_integrity.py; echo exit=$?
corpus.index    tracked=118 unindexed=0 stale=0 missing=0  (136 FILE-column patterns over 117 md files)
corpus.pointers report_dead=0/79 commit_total=37 unresolvable=0 nonhash=0 (… bare=33 …)
9/9 checks pass
exit=0
$ python3 -B verifiers/verify_corpus_independent.py; echo exit=$?
commits candidates=43 citations=37 hex=37 quoted=6 nonhash=0 unresolvable=0
exit=0
```

The delta is exactly the round's own last commit, `2a8eba5` (“round-66 verifier spot-check
(integrator, hyaku)”), which adds `corpus/lessons/round-66-verifier-spotcheck.md`: one more
tracked corpus file, **unindexed** (`grep -c "round-66-verifier-spotcheck" corpus/README.md` →
`0`), plus 3 report pointers (`79 → 82`) and 1 live fleet commit citation
(`1154d57a9ebb17faa4c9f8f456a6e53c51c230ae`, `lane=no fleet=yes`), `37 → 38`.

The frozen routed counter is green at that same final tree:

```
$ python3 -B verifiers/check_r66_routed_repairs.py --rev 2a8eba56b3f9321b70c569fa2816d42237ca49a2
control at 11385e04: 0 of 2
D1-r65-registries-committed: PASS
D2-corpus-integrity-reconciled: PASS
r66 routed defects closed 2 of 2
exit=0
```

Mechanism: `check_d2` (`verifiers/check_r66_routed_repairs.py:78-97`) reads
`verifiers/corpus-baseline.json` **at the revision** and compares its declared `expect` values
against the frozen `EXPECTED_COUNTS` (118 / 79 / 37 at line 41); it never measures the tree. A
stale baseline therefore satisfies “reconciled”. The consequence is a binding conflict
([INFERENCE], from the literal comparison at lines 88-92): indexing the spot-check lesson and
re-recording the baseline to the final tree (119 / 0 / 82+ / 38) would flip the frozen counter
to `1 of 2`, while leaving the tree as-is keeps the primary gate red at final. The two frozen
artifacts cannot both hold at HEAD without either a receipt that re-scopes “final lane tree” to
`9e75e73` or a counter re-freeze (which this seat may not do). Also note the round's own D2
method — “re-record observed corpus counts only after all round corpus entries land” — was not
followed: the r66 spot-check lesson is a round-66 corpus entry that landed after
`round66_rerecord` (measured at `daedcdf9`). Lane precedent counts spot-checks as corpus entries
(the same note indexes the r62–r65 spot-checks).

This is a calibration defect, not a resolver defect: the resolver correctly resolved the new
fleet citation and counted it once; the equal-mode pin is what the tree outgrew.

### P2 (non-blocking, counting semantics) — the independent `commit_total` counts non-hash live tokens; the pinned equal-mode count does not

Identical 16-line fixture through both instruments:

```
independent: total=14 hex_total=14 unresolvable=5 nonhash=1 quoted=2 candidates=16
integrity:   total=13                unresolvable=5 nonhash=1 quoted=2
CASE integrity/commit_total (hex live only)  got=13 want=13 PASS
CASE independent commit_total exceeds integrity by the nonhash token  got=1 want=1 PASS
```

Cause: `analyse_commits` appends every non-context citation to `citations` before the hex test
(`verify_corpus_independent.py:483`) and returns `len(citations)` as `commit_total` (line 496),
whereas integrity increments `commit_total` only after the hex gate
(`verify_corpus_integrity.py:526-530`). The independent's own suite pins the divergent
definition: `st.eq(com["commit_total"], 5, "commits: five citations in scope")` on a fixture with
2 hex and 3 non-hash live tokens (`verify_corpus_independent.py:983-986`), and the round-66 arm
pins `commit_total == 6` where only 3 are hex (lines 1014-1016). Today the live corpus has
`nonhash=0`, so both print 37/38 and the receipts' “independent agrees” holds — but agreement is
contingent on that zero, not on identical semantics. Because the independent's `commit_total` is
`observe`/INFO only, no verdict flips; the risk is a future receipt that reads a mismatch as a
drift.

### P3 (non-blocking, grammar divergence on a zero-mode class) — whitespace-bearing commit tokens separate the instruments

```
text: "commit `abc def`\ncommit `   `\ncommit `ab cd ef`\n"
integrity: total=0 nonhash=3 detail=['…:1: abc def', '…:2:    ', '…:3: ab cd ef']
independent tokens: []
```

Integrity's token group is `[^`\n]+` (`verify_corpus_integrity.py:149`); the independent's is
`[^`\s]+` (`verify_corpus_independent.py:125`). A malformed backticked token containing a space
is therefore a `commit_nonhash` violation (zero-mode, exit 1) in the primary and invisible to the
independent re-derivation, whose own `violations()` includes `commit_nonhash`. The class spec
(“token backticked”) does not settle whitespace, so this is a spec gap the two implementations
resolved differently; the primary is the fail-closed reading. No live corpus token contains
whitespace, so no number moves today.

### P4 (residual risk, no action requested)

- The “resolves in both is one citation, counted once” clause is prose only in both instruments.
  Neither suite has a both-repo fixture: the integrity self-test's `commit-hop/lane-first` gives
  `lane_git` only `lane_hex` and `fleet_git` only `fleet_hex`
  (`verify_corpus_integrity.py:1057-1059`),
  and the round-66 independent arm says “the lane and fleet objects are distinct” (line 1003).
  A future mutation that double-counts a both-repo token would not be caught by either suite;
  the property does hold in the sandbox (1, not 2).
- The independent self-test's first commit arm uses the **host** fleet root by default
  (`analyse_commits(croot, corpus_markdown(croot))`, line 983), so its “`deadbeef`
  unresolvable” assertion depends on `/home/vgpnk/Projects/shokunin` containing no object with
  that prefix (`git cat-file -e deadbeef` → absent today). The round-66 arm is hermetic because
  it passes its own `fleet_root` (line 1014).
- Object presence is not reachability. A commit removed from every ref but still in the object
  database resolves: in the sandbox, the dangling commit
  `faf772a3a4ff95c982113d9ed430a5fab08ecbf6` (fsck: 1 dangling, no branch contains it) returns
  `commit_resolves(...) = True`. Consistent with “name a commit object”, but it means the hop alone
  does not prove the citation names a report revision. Likewise a truncated lane clone is
  masked: a `--depth 1` clone that lacks the seed commit still resolves it through the fleet
  object database (`commit_resolves(S, shallow-lane, fleet) = True`; with `missing-fleet`
  → `False`).
- Neither gate exposes a `--fleet-root` override; both bind the absolute host path
  (`FLEET_ROOT = /home/vgpnk/Projects/shokunin`), so a re-run on another host would read every
  fleet-only citation unresolvable by construction.
- Not tested: a genuine 7-hex prefix collision between a lane object and a fleet object
  (constructing one requires brute force); the abbreviated non-commit cases above are the
  nearest observable masking test.

## Verification gaps

- This seat ran no lane gate as proof of the claim and changed no claim, counter, threshold,
  plan, receipt, or source file; the only write is this report.
- The independent resolver was exercised through `analyse_commits` with an explicit fleet root
  and through its CLI at HEAD/`9e75e73`; `commit_resolves` internals were exercised through the
  integrity function and through raw git. No `lsp` server was available to this seat.
- Prefix-collision behavior, and the fleet hop under a re-run on a host without the fleet
  repository, remain unmeasured.

## Exact self-test tallies observed at HEAD (control context only)

```
check_r66_routed_repairs.py --self-test   -> 0 failure(s) over 14 assertions, exit 0
verify_corpus_integrity.py --self-test    -> 0 failure(s) over 161 assertions, exit 0
verify_corpus_independent.py --self-test  -> 103 assertions, 0 failures, exit 0
```

These are green at HEAD; they do not measure the tree, which is the P1 gap.
