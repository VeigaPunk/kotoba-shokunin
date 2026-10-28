# Kb81S01Lesson — round lesson draft (round 81, w1)

Seat: scribe (leaf; no spawns, no subagents, no background jobs beyond my own tool calls).
Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`. Base `b284223105f4d106f7e8f56ed4fd296c643cda0e`.
No tool installed or upgraded; pacman not invoked; no host service touched. Scratch
`/fast/scratch/hyaku/kotoba-r81/Kb81S01Lesson/` was created for two read-only arithmetic checks and is
removed before yield; every git call there was `-C`'d and the clone's toplevel asserted.

## Deliverables

- `.ufo/waves/round-81/build/Kb81S01Lesson.md` — the full `corpus/lessons/round-81.md` text, shaped like
  `corpus/lessons/round-80.md`: `## Gate` (C1 base truth, the R1–R6 repair list, erratum E6 as frozen,
  the measured cap arithmetic, the pin-identity timeline and its freeze, the unpinned-manifest residual,
  the C2 S249 admit, the S250/S248 row updates, the C2 control suite, the assimilation disposition, the
  considerthese disposition), `## Mistakes` (table form), `## Sources & frontier`. Both markers were resolved at the L1's request: `{{HASH}}` → `ac62c2df…` (the committed S249 snapshot sha256) and `{{TIP}}` → the integration-commit sentence, since the lane head at draft time is `c15ebe8` (the freeze commit) and no after-value exists to point at.
- `.ufo/waves/round-81/build/Kb81S01Lesson-base-integrity.txt`, `Kb81S01Lesson-base-independent.txt` —
  my own base gate runs (exit 1 each, the five DRIFTs).
- `.ufo/waves/round-81/build/Kb81S01Lesson-instrument-cap.txt` — the composed `instrument-size`
  arithmetic on the patch bytes at 02:36:40Z.
- `.ufo/waves/round-81/build/Kb81S01Lesson-pin-staleness.txt` — the pin-vs-post-image check, with the
  resolution appended after the erratum was republished.
- `.ufo/waves/round-81/build/Kb81S01Lesson-worktree-vs-frozen.txt` — the worktree-vs-frozen plan check
  (`git show e6d48e6:plans/round-81.md` reads 900; the live worktree briefly read 140), receipt for M81-3.
- `.ufo/waves/round-81/build/Kb81S01Lesson-M81-4.patch` — the M81-4 row as a patch against
  `corpus/lessons/round-81.md` at `a597a15d` (single hunk, `git apply --check` rc 0 in a clone).
- `.ufo/waves/round-81/w1/Kb81S01Lesson.md` — this report.

## What I measured first-hand (own exit captured, no pipelines)

| command | result |
|---|---|
| `python3 -B verifiers/verify_corpus_integrity.py --repo .` (lane root) | exit 1, 4/9 checks; DRIFT `tracked_files` 155≠154, `unindexed` 1, `report_total` 111≠109, `report_dead` 1, `commit_unresolvable` 2 |
| `python3 -B verifiers/verify_corpus_independent.py --repo .` | exit 1 |
| `cmp .ufo/wapes .ufo/waves/round-80/build/Kb80C02C2-killproof.txt` | rc 0; both 594 B, sha256 `930e2bd6…`; `.ufo/wapes` untracked (`git ls-files` 0 rows) |
| `grep -c 'Q76' corpus/QUALITY.md` (base) | `0` |
| `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` | `174` |
| `sha256sum .ufo/waves/round-81/snapshots/S249.md` | `ac62c2df…`, 28,395 B; equals the counter's `--print-pins` `SNAPSHOT_PIN` |
| S249 quote in the counter's declared view | 13-word span `occ=1`; the 23-word r80 sentence `occ=0` |
| `git -C clone diff --numstat 072048fa <rev> -- <six battery scripts>`, E01+E02+E04 applied (rc 0 each) | `22 3` + `247 18` + `203 10` = **472/31** at 02:36:40Z (the plan's E6 figure); after E02's revision **402/29** |
| `git -C clone hash-object` on the post-images vs the counter's pin table | integrity `bbee51f2…` = pin; independent `59602942…` ≠ pin `7b37461a…` **at that moment**; after the republished erratum both match |

## Findings (reported, not repaired)

1. **F1 — the C1 base receipt stops one line short of the command's status.** No `exit=` in
   `receipts/tipbattery-base-dot.txt` (r80's carries `exit=1`); the status is code-entailed
   (`verifiers/check_tip_battery.py:399`) and was re-derived, so nothing is lost, but the receipt alone
   cannot be machine-checked for the verdict. Mined as M81-2.
2. **F2 — a live patch moved under the erratum's pins, and the freeze closed it.** E05 pinned the
   independent gate at `7b37461a…`; E02 was revised (sha256 `d8bf88c8…`) and produced `59602942…`, so for
   several minutes the amended counter would have failed `instrument-pin` by name (`guards 4 of 5`).
   E14's audit independently printed the same `FAIL … in_tuple=False`. E05 republished
   (`Kb81E05Erratum.patch` `c15680f8…`), and `.ufo/waves/round-81/receipts/freeze-shas.txt` now binds
   counter post-image `eb00200e…`/`1753b11c…`, `LINE_CAP 900`, pins `bbee51f2…` + `59602942…`, size
   `+402/−29`. Lesson carries the whole timeline, because the *mechanism* (a pin names bytes, and bytes
   move) is the round's calibration content.
3. **F3 — the cap was set from the measurement.** The plan first froze `LINE_CAP` at 140; the wave
   measured `+472` and the erratum was revised to 900 pre-freeze, with the reconciliation to `+402/−29`
   recorded in the freeze receipt. Consequence stated plainly: the size bound no longer constrains
   anything this round; the anti-laundering load is entirely on the tight pin tuples.
4. **F4 — the exemption manifest is unpinned.** `verifiers/external-commits.json`
   (blob `402ac290…`) is recorded as appendix data, explicitly not a pin, because E6 admits exactly two
   new members. The file that decides which absent hashes are exempt is therefore unpinned at the
   measured rev; its evidence is checked by the gates, not by the counter. This is the surface the C1
   critic attacks and the round's declared residual.
5. **F5 — quote reachability is view-relative.** The S249 page wraps `allowed-tools` in a Markdown link;
   the row's 10-word span and the entry's 13-word span both occur once in the declared view, while the
   23-word sentence r80's S248 row quotes occurs zero times there. The inherited quote is recorded as
   unbackable in the new view rather than rewritten (S248 changes only `used-by` this round).
6. **F6 — report-path identity has a declared legacy exemption.**
   `build/Kb81E04Baseline/R09-w10-marker-probe.txt`: the post-convention marker world reads `report_dead=1`
   (good) and the real 8128 B report `dead=0`; at a pre-convention path (round 8, whose real report is a
   120-byte marker) a fake marker still reads `dead=0` on the path arm, while the object arm marks the
   same blob dead. R1 binds identity for post-convention targets only.
7. **F7 — the staged package's id space collides 46-fold (S203–S248)** and five register slice ids
   (S236–S239, S243) name different documents in the lane than in the register. Adoption must key on
   (lane, cited URL), never on the S-id.
8. **F8 — `.ufo/wapes` duplicates a landed receipt**, so R3's move loses no unique bytes; the move must
   preserve sha256 `930e2bd6…` (pinned in the freeze receipt).
9. **F9 — a control-harness bug produced a false FAIL.** E06's smoke2 W1 reaches exactly
   `guards 5 of 5; tip battery exit 0: 4 of 6`, exit 1 (its expectation) but is graded FAIL because the
   harness's detail probe expects JSON from a gate that no longer emits it on that path. The counter's
   verdict and the harness's assertion are different objects; the lesson cites the counter's line.
10. **F10 — the C1 control suite holds on its final run, and the earlier run shows why receipts need a
    re-check.** Final receipt `.ufo/waves/round-81/build/c1_controls.txt` (single run, 2026-10-28T00:06:15,
    counter `1753b11c…`/blob `eb00200e`, `LINE_CAP 900`): `10 measured, 10 PASS, 0 FAIL, 0 ERROR`, every
    world exit 1, none reaching `6 of 6`. W0 4 of 6; W1/W2/W3 4 of 6 with the zero classes named (so no
    proper subset of the repairs suffices); W4 `guards 3 of 5` (size 2626 > 900 and pin FAIL); W5 `guards 4
    of 5` (spotcheck-identity); W6 `commit_nonhash 1` both gates (plan letter says `commit_unresolvable` —
    class differs, still a zero class); W7/W9 `commit_unresolvable 1`; W8 `report_dead 1`, `report_total 112`,
    detail `corpus/lessons/round-79.md:27`. The earlier 23:49 receipt on the same worlds read `3 PASS, 5 FAIL,
    2 ERROR` — harness faults (a detail probe expecting JSON the gates no longer print; two malformed
    fixtures), not counter verdicts. Both receipts stay on disk; the lesson cites the final one and names the
    difference.
11. **F10b — the two corpus gates disagree about `report_dead` at base.** W1's refresh refuses with “gate
    disagreement (not recorded, expectation stays 0): corpus.pointers.report_dead integrity 1 vs independent
    0”, and E10's base receipts show the same split (`06-corpus-integrity` DRIFTs include `report_dead 1`,
    `07-corpus-independent` reports `report_dead 0` for the same token). Two gates that are supposed to
    agree on the same zero class do not; the refresh records the disagreement rather than resolving it.
12. **F11 — plan-vs-implementation discrepancies that the lesson must not smooth.** (a) R1's identity arm
   runs at a `round >= 19` floor; without the floor it costs 10 false positives (`report_dead` 1→11), with
   it 0 — the plan sentence reads as if identity binds every resolved target. (b) E01's `external_binding`
   lacks the receipt-hash condition E02 carries; the gates agree today only because the live receipts
   contain both repository and hash, so the asymmetry is a residual, and expanding the frozen patch was
   declined. (c) Adding `external-commits.json` to `INSTRUMENT_PINS` was rejected post-freeze, which is why
   the laundering surface is recorded as a routed defect with Y01's three worlds (5/5 unmodified, 5/5 with
   one pin row, 4/5 with a laundered second record).
13. **F12 — my own mistake, mined as M81-3.** I quoted `LINE_CAP 40 → 140` from the live worktree plan (and
    from the seat brief) while the author was still editing it; the frozen commit `e6d48e6` declares 900 and
    140 never froze. Receipt `.ufo/waves/round-81/build/Kb81S01Lesson-worktree-vs-frozen.txt`. The fix is
    the one the lesson now states: `git show <freeze-commit>:<path>` is the only authority for a frozen value.

14. **F14 — routed defect R81-D1 is real and its repair was declined.** E01's `external_binding` requires
    the repository in the committed receipt but not the cited hash (`repository.encode() in proof`), while
    E02's `external_commits` requires both (`sha in text and name.lower() in text`); the plan sentence claims
    the receipt proves the repo→hash association. The ready repair
    (`Kb81E01Integrity.hashcheck-DECLINED.patch`, sha256 `0ab1b089…`, +5 lines, self-test 179/0) was ruled
    HOLD because a changed instrument costs a repin and a new freeze entry. Live receipts contain both, so
    the gates agree on the real corpus. Lesson records the exact conditions, the declined patch and the
    mitigation.
15. **F15 — the residual critic's four surviving classes are in the lesson, attributed.**
    `TRUNCATED_COMMIT_RE`/`TRUNCATED_RE` `{7,40}…` class a complete 40-hex token followed by `…` as
    `commit_truncated` (fix: `{7,39}`; the four live instances are genuine 7–8-char prefixes); E01/E02
    rev-prefix grammar skew (`foo.md:15:…`, `HEAD@{1}:…` dead in E01, live in E02); `--carry` is class-level
    and count-unbounded (count only in note prose); `SOFT_CROSS_CHECK` note-stamps a live gate disagreement
    instead of refusing. I verified the two code facts I quote (regexes at the patched lines) and the
    `report_dead` divergence in my own base run; the world-level readings are attributed to C03.
16. **F16 — the lesson carries the L1 rulings verbatim in substance.** E6 is 900 with tight tuples and the
    transient 140 never froze (`e6d48e6`, reconciliation `c15ebe8`); S248 keeps `queued` with an entry-only
    `used-by` (S16 confirmed the landed patch is entry-only, not the lesson path too), and the resulting
    queued-but-used row plus the new `W04` are recorded as findings routed to round 82; the manifest pin is
    declined as a routed defect with its control worlds; the R1 floor is reported as a plan-vs-implementation
    discrepancy rather than smoothed.

17. **F17 — M81-4 (landing) added at the L1's request, with the exact mechanism.** The freeze commit
    `c15ebe8` and G1 `647d13d` were created as detached commits, so the first G1 landing attempt was refused by
    the fleet helper: `jj-lane: HEAD is detached on a non-tip commit — check out <branch> first` (the commit
    guard's own text in `/home/vgpnk/Projects/shokunin/scripts/hyaku/jj-lane.sh`, exit 1). The correction is
    helper-only: `jj-lane.sh recover <lane> --as <id> --revision <full-hash> -- <paths>` after the branch
    ancestry is repaired (or check the branch out before committing), never a raw commit on a detached HEAD.
    Landed state verified by me: `git reflog show master --date=iso` shows `export from jj` at 00:55:53
    `c15ebe8`, 00:56:18 `647d13d`, 00:56:33 `65eaa85`, 00:56:40 `a597a15`; `master` and `origin/master` both
    `a597a15d…`; `merge-base --is-ancestor` confirms all four (4/4); `symbolic-ref -q HEAD` exits 1, so HEAD is
    still detached at the tip. No off-branch claim survives: c15ebe8 → G1 647d13d → G2 65eaa85 → G3 a597a15
    are landed and pushed. The row is in the build draft and in
    `build/Kb81S01Lesson-M81-4.patch`; the landed `corpus/lessons/round-81.md` at G1 predates it and needs the
    L1's follow-up commit.

## Coordination (peers, short-form only)

- `Kb81S07Quality`: confirmed the mistake label `M81-1` for Q76's `grounded in` cell; S07 replied that it
  adopted `M81-1` and that M81-2 is deliberately not cited (verified `grep -c 'M81-2'` → 0 on its row).
- `Kb81E09C2Counter`: told the conjunct-(e) requirement and supplied the S249 pin/quote facts; the lesson
  carries the dedicated `S248 used-by — → corpus/knowledge/allowed-tools-sdk-round81.md` line.
- `Kb81E12Census`: two measured drifts in my draft were reported and both are fixed (31 W04 at base, not
  32; the row's 10-word anchor span vs the entry's 13-word span).
- `Kb81E06Controls`: asked for the counter identity its worlds measured; it confirmed the re-pinned
  erratum and that the worlds measure the frozen bytes.

## Limits

- I did not score any claim after-value: C1's `6 of 6` and C2's `1 of 1` at the landed tip are the L1's
  post-integration measurements.
- I edited no lane file outside `.ufo/waves/round-81/`; `corpus/`, `verifiers/`, `SKILL.md`,
  `PROVINCE.md`, `QUALITY.md` and `plans/` are untouched by me.
- The C1 control table in the lesson is quoted from the control seat's published file with its own exit
  codes and counter sha; where a world's expectation and its harness grading disagree, the lesson says so.
- Scratch removed before yield.

VERDICT: Round-81 lesson final (build draft, marker-free) and the M81-4 landing row delivered as `build/Kb81S01Lesson-M81-4.patch` (applies clean to a597a15d): C1 carries E6 as frozen (900, tight pins, 402/29), the pin-staleness episode and freeze, the manifest-unpinned residual with its declined variant and controls, routed R81-D1, the four C03 residual classes, and the 10/10 control suite with every killer class red and no world at 6 of 6; C2 carries the S249 admit, the S250/S248 API-falsified binding, the queued-but-used invariant and W04, and CONTROLS-HOLD qualified by three conjunct gaps; Mistakes carries M81-1..M81-4 with the landing channel now documented (detached-HEAD creation, helper refusal, helper-only recovery, all four commits landed and pushed).
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S01Lesson.md /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S01Lesson-M81-4.patch /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81S01Lesson.md /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S01Lesson-base-integrity.txt /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S01Lesson-base-independent.txt /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S01Lesson-instrument-cap.txt /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S01Lesson-pin-staleness.txt /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S01Lesson-worktree-vs-frozen.txt
