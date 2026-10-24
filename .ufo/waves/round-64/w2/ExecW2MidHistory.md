# ExecW2MidHistory — round 64, wave 2

## Finding

C2 returned `0 of 4` (nonzero) at both requested mid-history revisions, before the round-64 header. In an isolated scratch clone of measured tip `c019919c97ab5fe98e87a7754b4449ea4e699c99`, I moved only the two counted LOG lines (C2 checks 2 and 3) above the round-64 header and committed that change. At that scratch commit, those two checks failed while checks 1 and 4 passed: the counter returned `2 of 4`, exit 1. This demonstrates the suffix anchor is load-bearing on the round's real LOG bytes.

## Exact counter runs

```text
$ python3 -B verifiers/check_r64_routed_repairs.py --rev c04fffbeafcaf810897258d56f99cca736ed3a91
FAIL seat-edit-committed    marker=False added-marker=False added-lines=0 (need >=60)
FAIL control-revs-named     no round-64 LOG line names both committed control basenames, computed revisions, and computed base
FAIL lowest-axis-corrected  round-64 LOG suffix lacks lowest/depth/consistency and both computed scores
FAIL assertion-count-named  runtime 23 matches static 17 fixed + 2 loop sites x 3 arms = 23; no BASE_REV-added patch line names 23 assertions
r63 routed defects closed 0 of 4
exit=1

$ python3 -B verifiers/check_r64_routed_repairs.py --rev 5613392d5a4a14a50753ab0ed5545fe7d85f3d9f
FAIL seat-edit-committed    marker=False added-marker=False added-lines=0 (need >=60)
FAIL control-revs-named     no round-64 LOG line names both committed control basenames, computed revisions, and computed base
FAIL lowest-axis-corrected  round-64 LOG suffix lacks lowest/depth/consistency and both computed scores
FAIL assertion-count-named  runtime 23 matches static 17 fixed + 2 loop sites x 3 arms = 23; no BASE_REV-added patch line names 23 assertions
r63 routed defects closed 0 of 4
exit=1

$ python3 -B verifiers/check_r64_routed_repairs.py --rev e041971d4ed63feaf88730f21722c1370ecb574b
PASS seat-edit-committed    marker=True added-marker=True added-lines=82 (need >=60)
FAIL control-revs-named     no round-64 LOG line names both committed control basenames, computed revisions, and computed base
FAIL lowest-axis-corrected  round-64 LOG suffix lacks lowest/depth/consistency and both computed scores
PASS assertion-count-named  runtime 23 matches static 17 fixed + 2 loop sites x 3 arms = 23; added patch line names 23 assertions
r63 routed defects closed 2 of 4
exit=1
```

## Scratch commit evidence

Scratch clone: `/tmp/kotoba-r64-c2-mid-history-attack`, checked out at `c019919c97ab5fe98e87a7754b4449ea4e699c99`. The staged/committed change was only `LOG.md`; the observed `git diff --numstat -- LOG.md` output was `2  2  LOG.md` (exit 0), and the unified diff showed the two `Counted citation line (C2 check 2)` / `Counted axis line (C2 check 3)` lines inserted immediately before the round-64 heading and removed from under it (diff exit 0). Commit exit 0; scratch commit: `e041971d4ed63feaf88730f21722c1370ecb574b`.

## Scope, risks, blockers

- No lane production files, lane index/state, or external substrates were written; scratch clone and commit were under `/tmp`.
- The moved lines were intentionally displaced in this falsification world. The result specifically exercises C2's suffix anchoring; it is not a broader counter or round acceptance audit.
- No blockers. No tools installed or updated.
