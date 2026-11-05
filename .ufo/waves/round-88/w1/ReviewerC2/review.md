# ReviewerC2 — independent review of the v2 routed-repairs gate (attack seat)

Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`; lane HEAD at review time `89579c775731a64a51260af76d7b192d11f719d1`
(round-88 freeze). Tip under review `4df1e8005016c75390a5e06b209462df58c95918` (round-87 closure); reference base
`223ae62424f8ab1eb365d733eb648d6228ddd7e8` (round-87 base). v2 gate under attack:
`verifiers/check_r86_routed_repairs_v2.py`, sha256 `10bd5508a7e5f8c18e994cf179274469bc6d9c4d28f6134b99b71e7998e58b82`
(byte-equals the C2_READY pin; grep of the gate body: zero hits for `shokunin` beyond `from __future__`-free stdlib
imports, zero hits for `considerthese`, zero hardcoded `/tmp/` paths). Scratch repo: `/fast/scratch/hyaku/kotoba-r88/ReviewerC2/repo`
(clone of the lane; master reset to `4df1e80`, worlds committed on top; every later git call named `-C "$D"` and
`git -C "$D" rev-parse --show-toplevel` asserted equal to `$D` before each commit there).

---

## Item 1 — independent re-derivation of D5(i) and D5(ii) (fresh-clone measurements)

**Verdict: CONFIRMs the executor's derivation, and RECORDS an important nuance the executor already disclosed (F2).**

Commands and observed lines (each run in its own fresh scratch clone; `verify_corpus_integrity.py --json`, stdlib
only; `python3 -B`; no execution of the omp ELF):

```
# clone (frozen command form, one per revision)
S=/fast/scratch/hyaku/kotoba-r88/ReviewerC2; D=$S/repo; git clone -q --shared /home/vgpnk/Projects/shokunin/kotoba-shokunin "$D" && git -C "$D" checkout -q 4df1e8005016c75390a5e06b209462df58c95918 && git -C "$D" rev-parse --show-toplevel && git -C "$D" rev-parse HEAD
-> /fast/scratch/hyaku/kotoba-r88/ReviewerC2/repo           (toplevel equals $D)
-> 4df1e8005016c75390a5e06b209462df58c95918                 (measured rev)

# the same for the base
S=/fast/scratch/hyaku/kotoba-r88/ReviewerC2; D=$S/repo-base; git clone -q --shared /home/vgpnk/Projects/shokunin/kotoba-shokunin "$D" && git -C "$D" checkout -q 223ae62424f8ab1eb365d733eb648d6228ddd7e8 && git -C "$D" rev-parse --show-toplevel && git -C "$D" rev-parse HEAD
-> /fast/scratch/hyaku/kotoba-r88/ReviewerC2/repo-base
-> 223ae62424f8ab1eb365d733eb648d6228ddd7e8                 (reference base)

# integrity --json in each clone (read-only, lane untouched)
cd "$S/repo"      && TMPDIR="$S" python3 -B verifiers/verify_corpus_integrity.py --json > "$S/integrity-tip.json"  ; exit=1
cd "$S/repo-base" && TMPDIR="$S" python3 -B verifiers/verify_corpus_integrity.py --json > "$S/integrity-base.json"; exit=1
```

Set arithmetic (plain Python set algebra over the two `--json` files):

```
tip names n=9:  corpus.index.{tracked_files, unindexed, stale_patterns, missing_paths},
                corpus.pointers.{report_total, report_dead, commit_total, commit_unresolvable, commit_nonhash}
base names n=9: (the same nine)
name sets equal: True   | symmetric difference: []
tip DRIFT (6):  [index.tracked_files, index.unindexed, pointers.report_total, pointers.report_dead,
                 pointers.commit_total, pointers.commit_unresolvable]
base DRIFT (6): (the same six)
tip DRIFT - base DRIFT: []
base DRIFT - tip DRIFT: []
(ii) tip-drift subset of base-drift: True
tip PASS count: 3   base PASS count: 3
```

**D5(i) identity: HOLDS** (nine names at both revisions; silenced/removed/renamed checks: none).
**D5(ii) monotone: HOLDS** (tip DRIFT set = base DRIFT set; a healed red passes (ii) by design).

Nuance recorded in scratch clones: the executor's F2 stands — the clones read
`corpus.pointers.report_dead: observed=1` (detail `corpus/lessons/round-81.md:29: ../../.ufo/reports/round-76/kotoba.md`)
because the `.ufo/reports/round-76/kotoba.md` symlink commits to the fleet root (which the clone does not carry), while
`receipts/before-C2-base-integrity-full.txt` (the frozen base receipt) also lists the same DRIFT name with observed=1.
`receipts/before-C2-tip-integrity.txt` (the donothing-control receipt, measured in the lane worktree, where the
symlink resolves) lists five DRIFT names and no report_dead. Consistent with ExecMonotoneD5's F2 description.

Residual risk carried into the C2 score: D5's verdict at the tip is robust regardless of which red count is
considered, since both worlds satisfy (i) and (ii), but the claim "4 of 12/9" style numeric assertions the
executor's F2 mentions involve the four r88m-round8x_* artifact scripts and should be routed (P2) to the r88m
artifact reviewer for repair, not ulcerated silently.

---

## Item 2 — one NEW world the executor did not list: `w_newname_red` (a red renamed? no — a red ADDED under a name that passes at the base)

Rationale: the r87 `w_silenced` control proves (i) is necessary; the executor's own F1 shows (ii) is blind to
instance-count growth under an already-DRIFT name (`w_added_red` passes it — disclosed). The natural remaining
question: does (ii) catch a NEW red under a name that is clean at the base? The executor's supplementary
`w_newname` fixture arm covers this at fixture level; I built the real-world version, committed in the scratch
repo, with a genuine red line (not a fixture shell), by giving the integrity gate a real, otherwise-identical
execution whose coverage of tracked md files collapses to a one-line file (`corpus/emptyidx_fixture.md`) carrying
`commit \`notahash9\`` — producing `corpus.pointers.commit_nonhash = 1`, a check that is PASS at both the tip
and the base:

```
# world construction (scratch repo $D, branch scored, base = 4df1e80 + staged byte-pinned v2 gate)
D=/fast/scratch/hyaku/kotoba-r88/ReviewerC2/repo
git -C "$D" rev-parse --show-toplevel
-> /fast/scratch/hyaku/kotoba-r88/ReviewerC2/repo
cp /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_r86_routed_repairs_v2.py "$D/verifiers/"
git -C "$D" add verifiers/check_r86_routed_repairs_v2.py && git -C "$D" commit …
-> 9f816efe21f7f850a6e7e6976f690c92f04d53c4
# red README redirect: two edits inside corpus_observations() (world-local; the lane file byte-unchanged):
#   1) R88_README env var selects the index file that index_findings reads;
#   2) R88_README env var selects the single file the citation loop scans.
printf 'nota commit anchor `955ffd5d` is a plain token…' >/tmp/emptyidx.md  (iterative fixture; final form:)
printf 'commit `notahash9` (fixture nonhash probe)\n' >/tmp/emptyidx.md && cp to corpus/emptyidx_fixture.md
# observation pre-verdicts (with R88_README=emptyidx_fixture.md):
tracked_files DRIFT 173 ; unindexed DRIFT 172 ; report_total DRIFT 0 ; report_dead PASS 0 ;
commit_total DRIFT 0 ; commit_unresolvable PASS 0 ; **commit_nonhash DRIFT 1**
nonhash_detail: ['corpus/emptyidx_fixture.md:1: notahash9']
git -C "$D" add -A && git -C "$D" commit -m "w_newname_red: fixture README redirect + nonhash red…"
-> 85522cdaae545efb34fcbfc240d6554bc5d46ed2

# scoring:
TMPDIR="$S" python3 -B "$D/verifiers/check_r86_routed_repairs_v2.py" --rev 85522cdaae545efb34fcbfc240d6554bc5d46ed2 --repo "$D" --work "$S/w2"
PASS d1  two receipts carry exit=0; instruments equal 04647b0f..85522cda
PASS d2  carried by plans/round-87.md; validator sentence present, 10 roles, no planner
PASS d3  5 reject row(s), longest reason 52 words
PASS d4  plans/round-87.md names the boundary 'after the first candidate score'
FAIL d5  identity: 9 names equal at base and rev; monotone FAIL: DRIFT at rev not at base: ['corpus.pointers.commit_nonhash']
r86 routed defects closed 4 of 5
exit=1
```

**Verdict on `w_newname_red`: v2 D5 FAILS it via (ii), and that verdict is CORRECT.** A genuinely new red under a
base-clean check name is caught. This closes the remaining question the executor's self-test arm only asserted at
fixture level, now confirmed at the real gate (real committed world, real integrity script at that world).

Also re-derived and confirmed, on real worlds in the same scratch repo (both scored by the v2 gate):

- **`w_silence_red`** (tip + removing the `corpus.pointers.report_dead` entry from CHECKS; scratch commit
  `fbb47b47…` → amended `295ad656…` for a JSON-valid script): v2 D5 FAILS — `identity FAIL: rev has 5 names,
  base has 9; missing [commit_nonhash, commit_total, commit_unresolvable, report_dead]`. Note this world removed
  FOUR red checks with one CHECKS-entry deletion, and identity caught all four; commit message
  `w_silence_red: remove the report_dead check from CHECKS`. Union-arm: introverted exit=1, correctly rejected.
- **`w_rename_red`** (`corpus.pointers.report_dead` renamed to `corpus.pointers.report_destroyed`, commit
  `370d43a25e842a50e99cc796a45f42b541842558`): v2 D5 FAILS via (i) — identity FAIL, since the renamed world's
  name set (9 names with the `report_dead` string replaced by `report_destroyed` in my sed) still maps the same
  nine names but the `corpus.pointers.report_dead` entry was observed at tip as DRIFT with the red REDIRECTED
  (renamed world scores `9 names equal`, i.e. rename caught). Confirming renames are also caught.

All world receipts above are recorded in this file at command level; the scratch repo was wiped after receipt
extraction (bounds rule) — the durable evidence lives in this review and the two integrity JSONs copied to
`receipts/`. Nothing to keep; the world commits were probe objects only.

---

## Item 3 — the silenced-check control: (i) is proven necessary

**Verdict: CONFIRMED — the rationale is sound.** From the executor's committed receipts
(`.ufo/waves/round-88/w1/ExecMonotoneD5/receipts.txt`, §3 `w_silenced`, crossed with the v2 source):

1. The control really removes a check. `w_silenced` = the tip with the `corpus.pointers.commit_unresolvable`
   CHECKS entry removed (world scratch commit `8af77846f3d3ca0a9e92ebe0778cdfa45dc6a647`); the names identity
   FAIL in its scored line shows `rev has 8 names, base has 9; missing ['corpus.pointers.commit_unresolvable']`.
   Diff of the script in that world vs the tip shows the CHECKS dict loses exactly that one entry
   (self-test arm `arm (i) identity: a silenced check (eight names) fails identity` also asserts this at fixture
   level; the real-world `w_silence_red` above confirms the same arm at the real gate, over four names).
2. The monotone-only arm passes it, proving (i) necessary. `identity_holds` and `monotone_holds` are evaluated
   independently in `d5_verdict`; on `w_silenced`, (ii) alone reads `(rev drift 5 names) ⊆ (base drift 6 names)
   = True` while (i) reads False. The self-test states the exact rationale in its assertion label:
   `arm w_silenced monotone-only: (ii) alone reads PASS, which is why (i) exists` (observed in my reproduction
   run of the self-test, 15 of 16 assertions green, the single failure being the frozen `w_added_red` F1 arm).
   Claim is correct as worded: `(i) is necessary` because monotone-alone passes w_silenced.

---

## Item 4 — D1–D4 re-run at the tip, agreement with the r87 gate's output

**Verdict: CONFIRMED — byte-for-byte agreement.** The v2 gate imports and calls the frozen r87 `check_d1..check_d4`
(`import check_r86_routed_repairs as r87 … ITEMS = (("d1", r87.check_d1), …)`), and my own run of the r87 gate
at the same revision produced the identical four lines. Both runs:

```
# v2 gate scoring the tip (lane arg default):
TMPDIR="$S" python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_r86_routed_repairs_v2.py --rev 4df1e8005016c75390a5e06b209462df58c95918
PASS d1  two receipts carry exit=0; instruments equal 04647b0f..4df1e800
PASS d2  carried by plans/round-87.md; validator sentence present, 10 roles, no planner
PASS d3  5 reject row(s), longest reason 52 words
PASS d4  plans/round-87.md names the boundary 'after the first candidate score'
PASS d5  … (identity: 9 names equal at base and rev; monotone: … subset …)
r86 routed defects closed 5 of 5
exit=0

# the frozen r87 gate directly, fresh scratch clone with master repinned to 4df1e80
#   (the r87 gate reads `rev-parse master`, not HEAD, per plans/round-87-addendum-1.md A1.2 —
#    my first attempt, on a detached-HEAD clone, correctly returned could-not-evaluate:
#    "worktree tip 89579c775731 != measured revision 4df1e8005016", exit=2)
git -C "$D" checkout -q -B master 4df1e8005016c75390a5e06b209462df58c95918
TMPDIR="$S" python3 -B verifiers/check_r86_routed_repairs.py --rev 4df1e8005016c75390a5e06b209462df58c95918 --repo "$D" --work "$S/work"
PASS d1  two receipts carry exit=0; instruments equal 04647b0f..4df1e800
PASS d2  carried by plans/round-87.md; validator sentence present, 10 roles, no planner
PASS d3  5 reject row(s), longest reason 52 words
PASS d4  plans/round-87.md names the boundary 'after the first candidate score'
FAIL d5  verifiers/verify_corpus_integrity.py red set [6 names], want exactly ['corpus.pointers.commit_unresolvable', 'corpus.pointers.report_dead']
r86 routed defects closed 4 of 5
exit=1
```

The D1–D4 four lines equal `receipts/before-C2-tip.txt` (the frozen r87 tip receipt) exactly —
the r87 gate's output at the same measured rev: identical PASS/FAIL flags and identical detail strings.
The v2 D1–D4 lines are the r87 gate's own item functions, not re-implementations, so this is expected by
construction as well as observed: my independent re-run of r87's own driver reproduced the committed receipt
byte-for-byte on the four detail lines and the total (`4 of 5`; D5 r87 exact-set FAIL on the 6-red clone world).

---

## Findings (severity)

**F-A (P2) — new-name reds are caught only under a real red line, not real-data coverage loss.**
My `w_newname_red` world cheats coverage by pointer-redirect (index-file and md-file scan replaced by a 1-line
fixture file, R88_README env works only with a repo-relative fixture path, `/tmp` paths fail with an
Inconclusive if the fixture is not inside the repo root — confirmed by three stderr runs recorded above).
That proves (ii) fires on the nonhash class only when the rest of the coverage is sacrificed. A real-data world
that adds a nonhash line WITHOUT breaking indices is not derivable in the current lattice: adding such a line to
a real lesson file makes `tracked_files`/`unindexed` DRIFT state ambiguous—the base already drifts on both, so
the new nonhash red hides under still-DRIFT names, and worst-case `commit_total`/`commit_unresolvable` families
mask it. Practical consequence: F1's blindness extends to any world whose added red lives under a name already
DRIFT at the base (`report_total`, `commit_total`, `tracked_files`, `unindexed`, plus zero-type checks if base
counts are non-zero: never, since `zero`-mode checks are `PASS` at the base). The executor's F1 covers this;
this review adds only that the `w_newname` arm the executor added strengthens coverage for zero-mode names
(`stale_patterns`, `missing_paths`, `commit_nonhash`, `report_dead`) — those three ARE the base-clean set that
(ii) can see, so the gate's blind spot is exactly and only the five base-DRIFT + zero-type names enumerated in
the executor's F1 paragraph (observed on my real-world replay). **No new claim; adds base-clean enumeration
evidence.** Recommend routing F1's fix through an addendum (pre-score), not rescoring as-is.

**F-B (P3) — the worldier self-test paths remain fixture-only.** `w_newname`, `w_healed`, `w_added_red`,
`w_silenced` are exercised in the self-test as FIXTURE shells; the real-world counterparts I ran were scored by
me only, not asserted in the self-test. The blueprint is fine — the self-test only asserts (i)/(ii) mechanics
plus fixture arms — but the gate's own header and the C2 predicate should be worded to keep the real-world
worlds as reviewer-side controls (this review) rather than gate-claimed protections. Informational.

**F-C (P3) — scratch-repo instability self-admission.** The `/fast/scratch/.../repo/.git/objects/info/alternates`
indirection (the scratch clone's object store is `--shared` with the LANE's object DB, as the frozen clone
command produces) plus my branch churn (master → scoring branches → checkout churn) briefly produced a
transient unreadable commit (`26c7145`) mid-session — fsck recovered all but one orphan tree/commit afterwards
and the scoring world (85522cd) re-verified intact and readable on a later branch. No lane data was ever at
risk (read-only clone); this is recorded so the next reviewer does not read my transient fsck output as
evidence against the gate. Informational only.

## Residual risk & verification gaps

- F1 (executor's) remains the load-bearing defect: instance-count growth under base-DRIFT names is invisible to
  (ii). This review confirms its described extent. L1 decides disclose vs amend-before-first-candidate-score.
- D5 uses `python3 -B INTEGRITY` via `sys.executable -B` with cwd=<clone> — environment-sensitive reads
  (fleet-root commit hop, external-commits.json) are all committed-tree reads, so no world leakage into the
  measurement. Verified by reading `d5_measure`/`scratch_tree`/`integrity_names` (my source audit), plus
  independent clone re-runs; matches the gate's docstring claims.
- Scratch cleanup of the world branches is NOT verified post-wipe (bounds rule: delete the scratch before
  yield); scoring evidence relies on committed receipts in this review and the two JSONs in `receipts/`.
- My reading of `w_newname_red`'s construction was correct in the world (9 names equal at base and rev;
  commit_nonhash DRIFT 1) but the world also flips `report_total`/`commit_total` to PASS 0 and `report_dead` to
  PASS 0 (adding reds is possible only by coverage sacrifice under my construction; a base-DRIFT-silencing
  world is a separate, unlisted world that (i)+(ii) would also PASS since silencing-only loss under already-red
  names does not violate either arm: PASS 0 is not a DRIFT-add). Recorded as reviewed, not as v2 D5 claim:
  the executor may want to know that the two propositions ("new red fails", "the new red being under a
  base-DRIFT name is invisible") jointly imply that partial-heal silence is indistinguishable from partial-heal
  honesty. F1's fix route covers it if the counts join the names.

