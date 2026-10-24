# ScoutW2R62SpotcheckSweep

role: scout
item: ScoutW2R62SpotcheckSweep — line sweep of `corpus/lessons/round-62-verifier-spotcheck.md` §6 against committed bytes at `cbbee56e9a3589b0b46736ad36f1b77701def80e`
axes: calibration (self-assessment vs committed bytes). Citation fidelity, then completeness. A counter pass is not a §6 closure.

Lane tip during the sweep: `cbbee56e` (ancestor of HEAD; this commit). Comparisons use `35d44b4b4dcdda234b5dbff7af37e432fec55f05` (r62 spot-check tip, the C2 before-rev). No installs. No production edits.

## Attack

```text
$ git rev-parse HEAD
cbbee56e9a3589b0b46736ad36f1b77701def80e

$ git ls-tree -r cbbee56e9a3589b0b46736ad36f1b77701def80e -- .ufo/waves/round-62/w2/FalsifyC2HonestH1.md
100644 blob f48861bff4a44d9501b8519f54a53b2c850bd5c9	.ufo/waves/round-62/w2/FalsifyC2HonestH1.md

$ git show cbbee56e9a3589b0b46736ad36f1b77701def80e:.ufo/waves/round-62/C2-successor-measure.txt | sed -n '2p'
receipt_rev=3f911504ce76d9ca186f297d6d4a9cd8ed77508a

$ python3 - << 'PY'
# wc -l / wc -w of the entry blob; LOG prefix vs 35d44b4b
PY
wc-l 64 wc-w 1044 bytes 8838 endswith_nl True
prefix True base_len 514498 tip_len 517352 delta_bytes 2854
base lines 2566 tip lines 2575

$ git diff --numstat 35d44b4b4dcdda234b5dbff7af37e432fec55f05 cbbee56e9a3589b0b46736ad36f1b77701def80e -- \
    corpus/lessons/round-62.md corpus/knowledge/erratum-absorption-round62.md \
    verifiers/check_routed_repairs_v2.py SHONEN.md LOG.md corpus/QUALITY.md
UNCHANGED  corpus/lessons/round-62.md
UNCHANGED  corpus/knowledge/erratum-absorption-round62.md
UNCHANGED  verifiers/check_routed_repairs_v2.py
UNCHANGED  SHONEN.md
9 0        LOG.md
2 1        corpus/QUALITY.md

$ git merge-base --is-ancestor d519047c e53b6e5c0aaa1ef2b0861b9399fef44f8b907f02
ancestor_exit:0
$ git log -1 --oneline -- .ufo/waves/round-62/w2/FalsifyC2Mutants.md
d519047 round-62: fourth sweep — FalsifyC2Mutants final wording ...
$ git log --oneline e53b6e5c0aaa1ef2b0861b9399fef44f8b907f02..cbbee56e9a3589b0b46736ad36f1b77701def80e -- .ufo/waves/round-62/w2/FalsifyC2Mutants.md
(empty)
$ git rev-list --parents cbbee56e9a3589b0b46736ad36f1b77701def80e | awk parent==e53b6e5c
35d44b4b4dcdda234b5dbff7af37e432fec55f05 e53b6e5c0aaa1ef2b0861b9399fef44f8b907f02
# descendants of e53b6e5c on this first-parent line, besides that child:
# 8c4cefa8e1b751d5f93dbcc65349b8e985b102d8, cbbee56e9a3589b0b46736ad36f1b77701def80e

$ python3 -B verifiers/check_r63_routed_repairs.py --rev cbbee56e9a3589b0b46736ad36f1b77701def80e
PASS late-write-tracked   tracked at cbbee56e9a3589b0b46736ad36f1b77701def80e
PASS receipt-rev-named    LOG names 3f911504ce76d9ca186f297d6d4a9cd8ed77508a on 1 line(s)
PASS entry-size-named     LOG states 64 lines / 1044 words on 1 line(s)
PASS append-only          prefix=True grew_by=9 line(s)
PASS noharm-arms-named    LOG names reg_gate 36 of 38 + corpus-idx on 1 line(s)
r62 routed defects closed 5 of 5
EXIT:0

$ python3 -B verifiers/check_gate_registry.py --rev 35d44b4b4dcdda234b5dbff7af37e432fec55f05
gate registry rows conformant 39 of 39 lane verifiers; phantom 0
EXIT:0
```

`SHONEN.md` at this rev: `[x]` count 0, four box marks `[~]` at lines 5, 7, 9, 11 (a fifth `[~]` is prose inside line 10, not a fifth box).

## Crosswalk (§6 → cbbee56e)

Quotes are ≤15 words, taken from `corpus/lessons/round-62-verifier-spotcheck.md:161-177`. "Prose-only" means the disposition's only committed evidence is a narrative sentence, with no artifact that instantiates the obligation.

| id | obligation (≤15 words) | disposition at cbbee56e | status | prose-only |
|---|---|---|---|---|
| 1a | Commit or revert the untracked late seat write. | `LOG.md:2574`; blob `f48861bf` at `.ufo/waves/round-62/w2/FalsifyC2HonestH1.md` (finding `:60-121`) | CLOSED | no |
| 1b | Fold H1-narrowness into the entry/Q57, or fix regexes. | Bound inserted in `corpus/QUALITY.md:68` (grounded-in cell, not a bound column). Entry `corpus/knowledge/erratum-absorption-round62.md` unchanged (`## Limits` `:54-64` has no H1 sentence). `verifiers/check_routed_repairs_v2.py` unchanged, so the regex alternative was not taken. | OPEN | no for the M-* rate bound (the Q57 cell is an artifact); yes for the `**not**` mechanism — it is not in `:68` |
| 2a | Fix the C2 receipt_rev to the receipt's token. | Receipt `.ufo/waves/round-62/C2-successor-measure.txt:2` is `receipt_rev=3f911504ce76d9ca186f297d6d4a9cd8ed77508a`. `LOG.md:2570` names that exact token and `e424f2a4`. | CLOSED | no |
| 2b | Name the entry size, 64 lines and 1044 words. | `LOG.md:2571`. Independent `wc` of the entry blob at this rev: `64` newlines, `1044` words. | CLOSED | no |
| 2 method | Prefer appended LOG corrections over in-place rewrites. | `35d44b4b:LOG.md` is a byte-prefix of `cbbee56e:LOG.md`; growth is 9 lines (`LOG.md:2568-2575`). `corpus/QUALITY.md` Q57 was still rewritten in place (`2` insertions, `1` deletion). | CLOSED for LOG; Q57 in-place is outside this sentence's LOG target | no |
| 2c | Correct the false post-report child-commit claim. | `LOG.md:2572` denies a sweep child. True half: only direct child of `e53b6e5c` is `35d44b4b`; `FalsifyC2Mutants.md` last change `d519047` is an ancestor; no later commit on this line touches it. False half of the same bullet: "nothing else descends from `e53b6e5c`" — `8c4cefa8` and `cbbee56e` do. | OPEN | the false clause is prose with no supporting artifact |
| 3a | Re-probe both Accept forms for the Cursor `.md` URLs. | `.ufo/waves/round-63/w1/ExecSourceProbe.md:8-10` and artifacts `:14-170` (rules.md and `reference/plugins.md`; `text/markdown`, `*/*`, and default). `corpus/lessons/round-63.md:31-32` records rules.md only. | CLOSED | no |
| 3b | Name the Accept condition in the lesson Gate. | Named for rules.md at `corpus/lessons/round-63.md:31` and `corpus/SOURCES.md:231-232`. Plan target `plans/round-63.md:127-129` ("corrected in the round-62 lesson's Gate") missed: `corpus/lessons/round-62.md:19` is byte-unchanged and still says both `.md` forms are "dead URLs", with no supersession pointer. `plugins.md` is absent from the r63 Gate (`:26-34`) and the SOURCES note (`:221-235`). | OPEN | the r62 Gate sentence is the unqualified rejection; the errata does not point at it |
| 3c | Say whether the `.md` URL is minable, or why `/docs/rules` stays canonical. | Stated reason, three times: `LOG.md:2575`, `corpus/lessons/round-63.md:34`, `corpus/SOURCES.md:234` — "S108 already re-opens S049 at the same URL". False. S049 is `https://cursor.com/docs/rules.md` (`corpus/SOURCES.md:62`). S108 is `https://cursor.com/docs/rules` (`:120`). S115 is the same extensionless URL (`:127`), which is the spot-check's actual hold (`round-62-verifier-spotcheck.md:133`). `reference/plugins.md` is already mined as S088 (`corpus/SOURCES.md:101`, 30,324 B, sha256 `3bbf36f3…`), matching `ExecSourceProbe.md:141-142`. | OPEN | the "same URL" sentence is prose contradicted by the rows |
| 4 | Record both interim reds as fixed at the tip. | `LOG.md:2573` names `FAIL reg_gate`, `36 of 38`, `3e7aed9b`, and `FAIL corpus-idx` (round-61 spot-check). Receipt still `.ufo/waves/round-62/noharm-tip.txt:1` `3e7aed9b…`, `:12` `FAIL reg_gate`, `:15` `36 of 38`, `:17` `FAIL corpus-idx` … `round-61-verifier-spotcheck.md`. Fixed-at-tip artifacts: this seat's re-run of the cited registry command (39 of 39, exit 0, above); `corpus/README.md:108` indexes that lesson; `.ufo/waves/round-62/w2/FalsifyGateRegress.md:26` records `corpus-idx` unindexed 1→0 at `e6da78b`. r62 summary `LOG.md:2566` was not rewritten (append, not edit). | CLOSED | no. Bound: this seat did not re-run the corpus-idx battery arm; the index line and the r62 seat receipt are the artifacts |
| 5 | Leave four SHONEN boxes `[~]`; promotion is operator-owned. | `SHONEN.md:5,7,9,11` still `[~]`; zero `[x]`; file unchanged vs `35d44b4b`. | CLOSED | no |

## What `5 of 5` does not close

`verifiers/check_r63_routed_repairs.py:80-168` scores path-tracked, receipt-token presence, entry `wc` presence, LOG prefix-and-growth, and `reg_gate`/`corpus-idx`/`36 of 38` presence. It does not read the H1 finding, does not check a post-report child, does not read the Cursor Gate, and does not read `SHONEN.md`. Q58 (`corpus/QUALITY.md:70`) already says a token linkage does not prove the prose around it. This sweep is that case: the counter prints `5 of 5` exit 0 while 1b, 2c, 3b, and 3c are open.

## Smallest safe corrections

Do not rewrite `corpus/lessons/round-62.md:19`, `LOG.md:2566`, the S049 row, or the historical receipts. Append, or replace only the false clause.

1b. In the Q57 bound sentence at `corpus/QUALITY.md:68`, replace:

`while honest variants M-a/M-b/M-e/M-f/M-j of the same repairs fail its R-c/ancestry regexes`

with:

`while honest variants M-a/M-b/M-e/M-f/M-j, and the lane's own R-c bullet whose \`**not**\` emphasis fails \`C1_DENIED_RE\`, fail its R-c/ancestry regexes (\`**not**\` needs whitespace after \`not\`, FalsifyC2HonestH1.md:65-71; M-e is the sentence-final period; M-a/M-j are the 2-line window; M-f is the ancestry comment)`

2c. In `LOG.md:2572`, replace:

`nothing else descends from \`e53b6e5c\``

with:

`that commit is the only direct child; \`8c4cefa8\` and \`cbbee56e\` descend through it and do not touch \`FalsifyC2Mutants.md\` (last change \`d519047c\`, an ancestor of \`e53b6e5c\`)`

3b–3c. Append under `corpus/lessons/round-62.md` `## Gate`, and correct the three "same URL" sentences (`LOG.md:2575`, `corpus/lessons/round-63.md:34`, `corpus/SOURCES.md:234`) to this text:

`Appended (round 63; the dead-URL sentence above is not rewritten). The Cursor \`.md\` HTTP 404 is conditional on \`Accept: text/markdown\`. Under \`Accept: */*\` and the default Accept, \`https://cursor.com/docs/rules.md\` returns HTTP 200 \`text/markdown\` (17,252 B, sha256 \`dae9d3ec…\`) and \`https://cursor.com/docs/reference/plugins.md\` returns HTTP 200 (30,324 B, sha256 \`3bbf36f3…\`). They are not dead URLs. \`/docs/rules\` stays canonical because S115 (\`corpus/SOURCES.md:127\`) already holds \`https://cursor.com/docs/rules\`, which is not S049's \`.md\` URL (\`corpus/SOURCES.md:62\`). S108 (\`corpus/SOURCES.md:120\`) is that same extensionless URL, not S049. \`reference/plugins.md\` is already mined as S088 (\`corpus/SOURCES.md:101\`).`

## Verdict

ATTACKS the reading that `r62 routed defects closed 5 of 5` closes §6. At `cbbee56e`, 1a, 2a, 2b, the LOG append, 3a, 4, and 5 are closed on committed bytes. 1b, 2c, 3b, and 3c are open: the H1 bound omits the `**not**` case and never touches the entry; the child-commit correction denies the sweep and then falsely says nothing descends from `e53b6e5c`; the Cursor errata leaves `round-62.md:19` unqualified and states a same-URL reason the SOURCES rows contradict. I would close 1b if the Q57 sentence named the `**not**` mechanism, 2c if the descendant clause matched `git rev-list --parents`, and 3 if the r62 Gate carried the appended Accept note and the canonical hold cited S115/S088 instead of "S108 at the same URL".

Report: `.ufo/waves/round-63/w2/ScoutW2R62SpotcheckSweep.md`
