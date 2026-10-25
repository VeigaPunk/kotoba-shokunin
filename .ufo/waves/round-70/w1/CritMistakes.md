# CritMistakes — round 70 w1 — attack on `corpus/lessons/round-70.md` § Mistakes (M113–M116)

Seat: `L1Kotoba70.CritMistakes` (critic, read-only). Measured tip `16b212a390c7ce68b6bce49b2c3766b154fbcbae`.
Scratch: `/tmp/k70w1-CritMistakes.J1qk` (deleted before return). Tools installed/updated: none.

## Verdict

**Two of four rows are defective as filed, and none of the four has a committed fix that is shown able to fail in the CORPUS.md L1 sense, meaning the same command, red before, green after, with the fix as the only delta.**

- **Classes.** M114 `number-drift`, M115 `landing` and M116 `vacuous` are correct. M113 is half wrong: K69-3 belongs under **`attribution`**, not `landing`.
- **Fixes.** Only the K69-2 half of M113 has a same-command red/green pair. That pair has an unpinned input which lets the K69-2 world pass.
  - M114's repair is a constant-token comparison, which the lane's own Q58 says does not close a defect. A mutant restating the wrong numbers still closes.
  - M115's fix is weaker than the existing Q49 and has no committed red-before.
  - M116 names `Captured by: none` where Q48 applies. Its key PASS assertion at `8edeb49` has no receipt at that revision.
- **The questions asked.**
  - K69-3: **yes**, it is better classed `attribution` (D1).
  - All cited receipts exist in the tip tree (listing below). Existing is not the same as showing the fix can fail (D2–D7).

Impacted axes: calibration (class and captured-by accuracy), consistency (Q48/Q49/Q58 contradicted by the lesson that cites the rules around them), depth (none).

## Receipts tree (existence check)

```
$ git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin ls-tree -r --name-only 16b212a… -- .ufo/waves/round-70/
… controls/C1-base.txt  controls/C1-skip-control.txt  controls/M113-prereport-gate.txt
  controls/freeze-receipt.txt  receipts/C1-measure.txt  receipts/K69-11-inplace.txt …   (26 paths)
```

Every receipt cited by M113–M116 is present: `controls/M113-prereport-gate.txt`, `controls/C1-base.txt`, `receipts/C1-measure.txt`, `receipts/K69-11-inplace.txt`.

The class vocabulary comes from `/home/vgpnk/Projects/shokunin/CORPUS.md:172-176`. The class definitions are in `/home/vgpnk/Projects/shokunin/.ufo/waves/kaika-w1/mistakes.md` §2:

- C09 "Evidence landing — marker, missing SHONEN, placeholder, overwrite"
- C10 "Write-scope / attribution", capture "pathspec-limited commits, lane identity"
- C04 "Vacuous or inert verification"

## D1 — M113: K69-3 is `attribution`, and M113's fix cannot detect it (HIGH, calibration)

**Counterexample.** The protocol itself names K69-3's class: `PROTOCOL.md:125-128`, "Landed also means landed *by the lane*: the commit that adds `.ufo/reports/round-<N>/<id>.md` carries the lane identity … history is never rewritten to fix attribution — but the integrator records the **attribution defect** in the round notes." The vocabulary source agrees:

- C10's capture is "lane identity".
- Its exemplar M076 is "fleet commits combined report + MANIFEST append under lore identity" (`mistakes.md` §3 C10). That is the same shape as K69-3.

**Evidence.**

```
$ git -C /home/vgpnk/Projects/shokunin log -1 --format='%h %an <%ae> | %cn' 4844216b   → 4844216b probe <probe@example.invalid> | probe
$ … 9d9f181e                                                                            → 9d9f181e probe <probe@example.invalid> | probe
$ … 0a1199a0                                                                            → 0a1199a0 kotoba-shokunin <kotoba@shokunin.local> | kotoba-shokunin
```

M113's only fix is `git ls-remote origin refs/heads/<branch>` equal to the lane tip (`controls/M113-prereport-gate.txt`). That gate reads the lane remote. The defect is the identity on a fleet-repo commit. In a world where every lane commit is pushed correctly but the report is committed with plain git as `probe`, the gate exits 0. So no red-before exists for K69-3.

The defensible reading for `landing` is that PROTOCOL files the identity sentence under its "lands last" paragraph. The lesson vocabulary is the mistakes.md taxonomy, though, and PROTOCOL's own noun is "attribution defect".

**Smallest safe correction.** Split M113:

- Keep M113 as `landing (K69-2)`.
- Add a row `class: attribution (K69-3)` with the gate `git -C /home/vgpnk/Projects/shokunin log -1 --format='%an <%ae>' -- .ufo/reports/round-70/kotoba.md` = `kotoba-shokunin <kotoba@shokunin.local>`, run after `fleet-commit.sh --as kotoba`.
- Use the red-before that is already committed history: the same format on `4844216b` prints `probe <probe@example.invalid>`.

## D2 — M113: the pre-report gate's "final lane hash" is unpinned, and the bookmark reading passes the K69-2 world (MEDIUM)

**Counterexample.** I built a sandbox with a bare origin, `master` pushed, then a commit on a detached HEAD (the K69-2 world):

```
HEAD=55a17e68… branch=1be28302… ls-remote=1be28302…
gate(LANE_TIP=HEAD) exit=1
gate(LANE_TIP=branch ref) exit=0
```

- The lesson (`round-70.md:118-119`) and the prompt (`.ufo/prompts/kotoba-round-70.md:340-341`) both say "the final lane hash" without saying which hash.
- `jj-lane.sh state` reports `local=` (the bookmark) separately from `head=detached`. The r69 closure quotes `local=9ce102b… remote=9ce102b… head=detached`.
- An L1 that takes `local=` as "the lane hash" gets exit 0 in exactly the r69 world.
- The committed control used the detached commit (`lane tip 1789f48…`), so it tested only the favourable reading.

**Correction.** Pin `LANE_TIP` in M113's fix to the round's last commit (`git rev-parse HEAD`, or jj `@-`), never the bookmark.

## D3 — M113 control receipt is not reproducible (LOW)

```
$ git cat-file -e 1789f48c…^{commit}  → exit=128 ;  git cat-file -e 56f31c36…^{commit} → exit=128
$ git show 16b212a:.ufo/waves/round-70/controls/M113-prereport-gate.txt | rg -c 'sandbox|/tmp'  → 1   (line 1, "sandbox only")
```

The receipt has no commands that build the world, no clone path, and `$LANE_TIP` is undefined in it. This is Q41's sandbox-hash labelling rule in spirit: the word `sandbox` and the clone path belong on the hash line.

How the receipt was produced is unobserved by me; its content is plausible, and my own D2 sandbox reproduces the HEAD-reading outcome.

## D4 — M114: the repair is a constant comparison (Q58), a wrong-number mutant still closes, and the named-reason red is uncommitted (MEDIUM)

**Class `number-drift`: correct.** C02 covers "unreproducible, stale or wrong count". The counts check out:

```
$ git ls-tree -r --name-only 16b212a -- .ufo/waves/round-69/recapture/ | wc -l   → 10
$ git show --name-status --format= a02ba7e | rg -c '\.ufo/waves/round-68'        → 23
$ git show 16b212a:corpus/lessons/round-69.md | sed -n 24p                       → (18 assertions).
```

**The fix is not a closure under the lane's own bar.** Q58 (`corpus/QUALITY.md:70`): "closed only when a committed counter recomputes the corrected value from the measured revision's bytes; … a constant comparison … does not close it."

- `k7_numeric` checks the literal tokens `"10 receipts"`, `"23 landed"` and `"1 dispositioned"`.
- `k10_erratum` checks the literals `"(18 assertions)"` and `"22 assertions"`.
- `git show 16b212a:verifiers/check_r69_routed_repairs.py | rg -c 'ls-tree|recapture|numstat|name-status'` prints nothing (0 matches). Nothing is recomputed.

**Surviving mutant.** In a sandbox clone at `16b212a` I appended one line to the round-69 LOG entry: `- outcome (mutant): the r69 report's nine receipts and "all 24 landed" stand as filed.` (sandbox commit `1dd5cfc5…`, clone `/tmp/k70w1-CritMistakes.J1qk/tmpclone`):

```
$ python3 -B verifiers/check_r69_routed_repairs.py --repo <sandbox> --rev 1dd5cfc5…
r69 routed defects closed 9 of 10
  K69-11: governance.citation_resolves FAIL        (K69-7 counted closed)
exit=1
```

**Red-before reason.**

- At the base, K69-7 fails for "no appended `## Round 69` LOG.md entry" (`controls/C1-base.txt`), which is a missing entry, not a wrong number.
- The named-reason red is the self-test world "K69-7 nine receipts". Only the summary line is committed (`controls/freeze-receipt.txt`: "self-test: 0 failure(s) over 17 assertions"). CORPUS.md:180-182 requires "the observed failure text is committed".
- I re-ran the self-test: `PASS broken world rejected: K69-7 nine receipts` and `PASS broken world rejected: K69-10 erratum not appended`. Both are real but uncommitted.
- No self-test world tests the second wrong number (`24`).

**No recurrence fix.** Captured-by is "Corrections sweep every mention … not run" (`PROTOCOL.md:363`). The fix repairs the two instances but adds no gate that makes the sweep run.

**Correction.**

- Recompute `10` from `git ls-tree` of the recapture tree and `23` from the name-status of `a02ba7e`.
- Reject an entry that restates `nine receipts` or `all 24`.
- Commit the per-world self-test lines.

## D5 — M115: captured-by omits Q49, and the fix is weaker than Q49 (MEDIUM)

**Class `landing`: correct.** C09's M068 ("Mirror lessons left uncommitted") and M069 have the same shape.

**Captured-by is incomplete.** Q49 (`corpus/QUALITY.md:60`): "return or cancellation does not close its output window, and the recorded final misroot sweep covers every seat-writable directory only after the last seat settles. Any report the sweep finds … before the round report, either committed …". K69-5 is a Q49 breach, yet M115 cites only PROTOCOL "landed means committed" and M112.

**The fix contradicts Q49.** M115's fix runs the sweep "only after every wave seat has returned". Q49 says return does not close a seat's output window. The r69 late writes (07:35:59 and 07:36:54, after `07:34:22 complete`) are the case where "returned" is not enough.

**No committed red-before.**

- No round-70 file carries a round-start porcelain listing. Searching every `.ufo/waves/round-70/` blob for `porcelain|RevFreezeReceipt` hits only `C1-base.txt` and `C1-skip-control.txt` (blob-mismatch lines) and `K69-11-inplace.txt`, whose porcelain is its own write at `ac3c0f1`.
- The cited red-before is prose (`plans/round-70.md` § Inherited state).
- The C1 K69-5 failure at the base proves the instance repair (pinned blobs, committed at `8edeb49`: `RevFreezeReceipt.md | 153`, `ScoutStaleLane.md | 129`). It does not test the sweep-timing fix.

Also low: "the M112 class recurring" refers to a class M112 never had in the vocabulary. M112's class cell reads "uncommitted round-68 wave paths" (`corpus/lessons/round-69.md:149`).

**Correction.**

- Cite Q49 as captured-by.
- State the fix as Q49's settle rule.
- Commit the final porcelain output, taken after the last seat settles and immediately before the report, as the receipt.

## D6 — M116: `Captured by: none` is wrong; Q48 is the rule, and the lesson misstates it (MEDIUM, reference-drift inside the lesson)

**Class `vacuous`: acceptable.** C04 is "Vacuous or inert verification", and it includes a false-negative exemplar (M035, a parser rejecting valid files). A constant-FAIL item is inert. I confirmed it is constant in `/tmp`:

```
/tmp clone, verify_skill_checklist.py --json, governance.citation_resolves:
7d51253 FAIL · 8edeb49 FAIL · ac3c0f1 FAIL
8edeb49 detail: 3 × "corrected token '../.ufo/…' does not resolve" + "LOG.md:177 … (+30 more)"
```

So the lesson's "three round-65 corrected tokens and 30+ other" is accurate.

**Counterexample to `none`.** Q48 (`corpus/QUALITY.md:59`): "A counter's self-test drives its public `main()` on a satisfying fixture and asserts exit 0 … helper-only checks … do not cover the measurement path."

- The C1 self-test calls `check(FakeRepo(...))` and never `main()` (`check_r69_routed_repairs.py` `selftest`/`_run`).
- `FakeRepo.checklist()` replaces the sandbox gate path, which is exactly the path that was broken.
- The lesson's gloss, "Q48/Q45 ask for controls and a census before a target, and the controls here were all below-target worlds", misstates Q48. Q48 demands an **above-target** honest run through `main()`.
- In the same pre-data commit `a647fa7` the lane ran an honest sandbox world for C2 (`controls/C2-honest-sandbox.txt`: "skill eval facts backed 8 of 8 / exit=0") but none for C1. The step was known and practised in-round.

**Correction.**

- Set `Captured by: Q48 (self-test never drove main(); FakeRepo bypassed the sandbox gate path)`.
- Put M116's fix as an extension of Q48 (an arm that runs a sandboxed lane gate on an honest world), not as a free-standing rule.

## D7 — M116: the fix is not shown able to fail, and the `8edeb49` PASS is unreceipted (LOW–MEDIUM; claims are true)

**What is missing.**

- **The 8edeb49 PASS.** The lesson asserts the gate "run in the clean lane tree at that commit reads 11/11 PASS" at `8edeb49`. The only in-place receipt names `measured-rev: ac3c0f1…` (`receipts/K69-11-inplace.txt`). That is the Q50/Q60 pattern: a revision cited for a result whose receipt is for another revision.
- **The base FAIL.** The receipt's base comparison is prose: "the L1's round-start run printed exit_code 1 …".
- **No same-command pair.** `C1-measure.txt` (9 of 10) is a red of the defect, not of the fix. The in-place receipt runs a different command, and no green run of the same command exists.

**Discriminating world (my reproduction).** I cloned the lane under a fleet-shaped parent: symlinks to every fleet-root entry, plus a `--shared` clone named `kotoba-shokunin`.

```
7d51253 exit=1  FAIL LOG.md:2676 '.ufo/waves/round-67/w1/controls/census-validate-append.txt' … LOG.md:2678 '…/junk-world/' …   10 pass of 11
8edeb49 exit=0  PASS 1253 governance citation token(s) resolve …                                                                11 pass of 11
aa9c9ad exit=0  PASS (same)                                                                                                     11 pass of 11
ac3c0f1 exit=0  PASS (same)                                                                                                     11 pass of 11
```

Both prose assertions are true, so this is a provenance gap, not a false claim. The K69-11 item therefore discriminates when the sandbox's parent is fleet-shaped, and is constant only because of the `/tmp` location.

The frozen counter cannot be rescued with an environment setting. `tempfile.TemporaryDirectory` puts the clone at `<random>/clone`, so `../` always resolves to the random directory, even with `TMPDIR` set. "FAIL at every revision" therefore holds for the frozen predicate, and "miss as declared" is the correct call.

**Correction.**

- Commit the fleet-shaped-parent pair (base FAIL, `8edeb49` PASS) as M116's red-before/green-after, outside claim C1.
- Fix the lesson's `8edeb49` sentence so it cites the receipt's actual revision.

## Observation (outside M113–M116, LOW)

Two routed defects are unmined:

- K69-4 (SHONEN, Sources & frontier and Trend verdicts absent at filing) is the canonical C09 `landing` exemplar (M065/M067).
- K69-8 (no tip receipt) is the Q50 class.

The lesson routes K69-4 to the report and K69-8 to the C1 counter, but gives neither a Mistakes row. CORPUS does not require one per routed defect, so this is a coverage note, not a defect.

## Commands run (all read-only on the lane; git writes only in scratch clones)

`git ls-tree`/`show`/`log`/`cat-file` on the lane and fleet; `rg` over `CORPUS.md`, `PROTOCOL.md`, `QUALITY.md`, `mistakes.md`; `python3 -B verifiers/check_r69_routed_repairs.py --self-test` and `--repo <sandbox> --rev 1dd5cfc5…` in `/tmp/k70w1-CritMistakes.J1qk/tmpclone`; `python3 -B verifiers/verify_skill_checklist.py --json` in the `/tmp` clone and the fleet-shaped clone at 7d51253/8edeb49/aa9c9ad/ac3c0f1; the D2 bare-origin sandbox. Scratch deleted on return.
