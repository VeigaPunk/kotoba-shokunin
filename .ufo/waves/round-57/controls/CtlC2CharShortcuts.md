Result: MIXED — no literal contains-anywhere character-set skip meets C2's predicate (measured ceiling 96 of 120), but the same union plus a ~7-line empty-fence fallback measures 120 of 120, exit 0, while still FAILing a command-free table fence and PASSing every real missing command that shares a fence with a resolvable line.

# C2 pre-freeze control — character-presence shortcuts in info-less fences

Seat: KotobaR57.CtlC2CharShortcuts. Lane read only; every commit below is a sandbox commit in
`/fast/scratch/hyaku/kotoba-r57/KotobaR57.CtlC2CharShortcuts`, checked out at
`ee50d8fa7b5d260fff8bc332f4a90513bee518ff`. Counter: the file committed at that revision, sha256
`b3dbe72fd9383b6d404160a7f81a7630f3bfe915520dad85a7f1e008faf5d1ac`; every run prints that sha and the
copy inside every measured tree hashes to it (verified with `git show <rev>:verifiers/check_infoless_fences.py |
sha256sum`). Raw counter output: `.ufo/waves/round-57/controls/CtlC2CharShortcuts.txt` (659 lines, sha256
`bf9b701f1b9529fb89f839741ffc797aaafc8e96282454e2395a61ca61eebc92`). Patch surface: `verifiers/verify_skill_checklist.py`
only; the counter was never edited. Fix target of the claim read first: `plans/round-57.md` § C2;
instrument rule at `verifiers/verify_skill_checklist.py:778` (`fenced_regions`, info in
`{'', bash, sh, shell, console}`) and `:1084` (`command_subjects`).

## 1. Scores (frozen counter, default seeds 11 22 33, 120 cases)

Each row is a separate sandbox commit; the measured revision's `verifiers/` tree was archived by the counter.

| variant | skip rule (info-less fences only) | correct | P / H | exit | wrong classes | sandbox rev |
|---|---|---|---|---|---|---|
| BASE (do-nothing) | none | 48/120 | 0/60, 48/60 | 1 | P1–P5, H3 | `ee50d8fa` |
| PIPE | any line containing `|` | 60/120 | 12/60, 48/60 | 1 | P2–P5, H2 (N/A), H3 | `6f3d177` |
| COLON | any line containing `:` | 48/120 | 12/60, 36/60 | 1 | P1–P4, H3, H4 (N/A) | `9159a5b` |
| ARROW | any line containing `→` | 60/120 | 12/60, 48/60 | 1 | P1,P2,P3,P5, H3 | `ab46142` |
| PLUS | any line containing `+` | 48/120 | 0/60, 48/60 | 1 | P1–P5, H3 | `1afaf2c` |
| NONASCII | any non-ASCII char | 72/120 | 24/60, 48/60 | 1 | P1,P3,P5, H3 | `646072a` |
| DASHRUN | `--` anywhere | 24/120 | 0/60, 24/60 | 1 | P1–P5, H1 (N/A), H3, H4 (N/A) | `1e4eca7` |
| UNION | `| : → +` or non-ASCII | 96/120 | 60/60, 36/60 | 1 | H2 (N/A), H4 (N/A) | `590d214` |
| UNION−COLON | `| + →` or non-ASCII | 96/120 | 48/60, 48/60 | 1 | P5, H2 (N/A) | `beb7c5c` |
| **UNION+EMPTY** | UNION + empty-fence fallback | **120/120** | 60/60, 60/60 | **0** | — | `93c9610` |
| STRUCT (refined) | pipe count ≥2 / first token ends `:` / `+` / non-ASCII | 120/120 | 60/60, 60/60 | 0 | — | `43bf2dd` |
| LEADING (refined) | leading `|`/`+`/U+2500–257F / `→` / first token ends `:` | 120/120 | 60/60, 60/60 | 0 | — | `f5505ff` |

All sandbox hashes are labelled `sandbox <hash> (/fast/scratch/hyaku/kotoba-r57/KotobaR57.CtlC2CharShortcuts)`.
Instrument sha256 per measured revision (counter-printed): PIPE `c46615b3…`, COLON `ed250193…`, ARROW `3cf03767…`,
PLUS `6a0460d5…`, NONASCII `88bf62a5…`, DASHRUN `a9a95849…`, UNION `0646fbaa…`, UNION+EMPTY `8e2af3dc…`,
STRUCT `a25d1b3f…`, LEADING `104ce911…`, UNION−COLON `718e3ed4…`. The instrument's own `--self-test` is 0 failures over 1852 assertions for every variant, including UNION+EMPTY (run
in a full checkout: a verifiers-only extract reports 18 spurious failures even for the unpatched base, so a seat
running the self-test from an extracted tree will misread it as a regression). The self-test does not catch any of
these shortcuts.

## 2. Why the literal family cannot meet (ceiling 96)

Every PASS case carries one surviving real command, so a class is passed only if all its decorative lines are skipped:

- P1 (table) needs `|` (`| w | w |` has no other special char).
- P1 and H3 need the table rows skipped for the four-item detail cap to stop hiding H3's bogus head.
- P3 needs `|` (`| tok |`) **and** `+` (`+------+`).
- P5 needs `:` (`ALPHA: beta`); P2/P4 need non-ASCII (U+2500–257F / U+2192).
- H2 is the single-line fence `ls | <bogus>`: any `|` skip empties it and the check returns N/A, never FAIL.
- H4 is the single-line fence `<bogus> --opt=<tok>:<tok>`: any `:` skip empties it, same N/A.
- Dash runs are fatal in every form: `ls -la` and `git --version` carry `-`, so a single-dash skip loses all 60 P
  cases; `--` also kills H1 and H4 (DASHRUN 24/120).

`|` is mandatory (P1, P3, H3) and fatal (H2); `:` is mandatory for P5 and fatal for H4; the two trade exactly:
UNION loses H2+H4 (96), UNION−COLON keeps H4 and loses P5 (96). No subset of `{| : → + -runs non-ASCII}` can exceed 96.

## 3. The control that meets the predicate, exactly how

Sandbox `93c9610` (`/fast/scratch/.../KotobaR57.CtlC2CharShortcuts`): in an info-less fence, skip every line whose
text contains `|`, `:`, `→`, `+` or any char > U+007F anywhere; then, if a fence contributed zero segments and at
least one line was skipped, append one subject whose `head` is that first skipped line's text. `check_commands` then
returns FAIL and the detail embeds the line verbatim. The counter's hard-negative rule is a raw substring test —
`verifiers/check_infoless_fences.py:455` `return status == "FAIL" and case.head in detail` — so H2's `bogus` and H4's
`bogus` are found inside the quoted whole line, and both classes flip from wrong to correct. The counter's frozen
score: `info-less fence cases correct 120 of 120 (pass-expected 60 of 60; hard negatives 60 of 60)`, exit 0.

Delta over the strict union: the fallback is 7 lines (`EMPTY_FALLBACK = …` plus the `if (EMPTY_FALLBACK …)` block at
sandbox `93c9610` `verifiers/verify_skill_checklist.py:1204-1208`); the block was committed gated with the union
member, so `git diff 590d214..93c9610 -- verifiers/` shows only the constant. Whole control vs base: 59 insertions,
7 deletions, one file (fence-info threading at `:791,836,809,815,842`, skip at `:1143-1146`, fallback at
`:1204-1208`).

## 4. Hidden regressions (direct instrument probes, not the counter)

Each row is one info-less fence in a generated case dir, run with the measured tree's instrument and
`--check trigger.command_binary_resolves --json`; the harness is `scratch/probe.py` in the sandbox
(output `scratch/probes.txt`). Status is the check's; the claim's own requirement is in the last column.

| probe fence | BASE | UNION+EMPTY | STRUCT | LEADING | claim requires |
|---|---|---|---|---|---|
| `\| name \| value \| / \|---\| / \| alpha \| 1 \| / \| beta \| 2 \|` (no command) | FAIL | **FAIL** | N/A | N/A | stop the false FAIL (P1-type table) |
| `ALPHA: beta` / `GAMMA:    delta/epsilon` | FAIL | **FAIL** | N/A | N/A | stop the false FAIL (key: value) |
| `ls -la` + `ls \| bogusxyz` | FAIL (names bogusxyz) | **PASS** | FAIL | FAIL | missing command in a pipeline FAILs |
| `ls -la` + `bogusxyz --opt=alpha:beta` | FAIL | **PASS** | FAIL | FAIL | colon in an argument still FAILs |
| `ls -la` + `bogusxyz --opt=a+b` | FAIL | **PASS** | **PASS** | FAIL | (no line in the counter probes this) |
| `ls -la` + `bogusxyz --name=café` | FAIL | **PASS** | **PASS** | FAIL | (no line in the counter probes this) |
| `ls -la` + `bogusxyz trel (bando)    → quosk/vint.json` | FAIL | **PASS** | **PASS** | **PASS** | (no line in the counter probes this) |
| `┌──┐ / │ tok │ / └──┘` + `ls -la` | FAIL | PASS | PASS | PASS | stop the false FAIL (P2-type box) |

So the meeting control is **worse than base on the claim's own acceptance conditions**: it turns the pipeline and
colon-in-argument FAILs into false PASSes, leaves both command-free fences FAILing (the exact false FAIL C2 exists to
remove), and adds two unchecked-command holes (`+`, non-ASCII). The refined LEADING rule keeps pipeline/colon/`+`/
non-ASCII failing and clears both command-free fences, with one remaining hole: a checked line carrying `→`.

## 5. Counter blind spots this exposes

1. Every P case injects one real command, so a command-free fence can never be a P case: a rule that FAILs all
   command-free fences is invisible (UNION+EMPTY scores it FAIL, the claim requires no FAIL).
2. Every FAIL class but H3 is a single-line fence: a "fail when the fence is emptied" rule repairs H2 and H4 exactly,
   with no other effect. The rule was never forbidden by the frozen spec.
3. No hard negative puts `+`, a non-ASCII char, or `→` in a command line that shares a fence with a resolvable line,
   so a character-anywhere skip's escape holes are unprobed. H3 is the only shape that punishes blanket skipping, and
   any `|` skip satisfies it.
4. `case.head in detail` is a substring test on free text: naming the whole line satisfies H2 and H4 while the check
   never resolves a head token. A token-boundary or "head equals detail token" rule would close this.

## 6. Impacted axes and smallest safe correction

Impacted: operability (C2's axis) — the predicate is met by a control that operators would not accept, so its PASS
does not certify operability; calibration — the control family in `plans/round-57.md` (skip `|`/`:`/`→`/box chars) is
strictly weaker than the family tested here (ceiling 96), and the meeting member (fallback) is not on that list;
adjacency is untouched (C1 not worked, no real plugin content written). Depth/consistency/freshness unaffected.

Smallest safe corrections, in order of preference:

1. Instrument: skip by line *shape*, not character presence — first non-space char in `| + U+2500–257F`, or first
   token ends with `:`, or the line carries `→` (measured LEADING: 120/120, exit 0, self-test 0/1852, and no false
   PASS on pipeline / colon-arg / `+` / non-ASCII with a sibling command). Do **not** adopt the empty-fence fallback:
   it reintroduces the false FAIL on a command-free table, which is the claim's reason to exist.
2. Counter (frozen, so erratum before data per `plans/round-57.md` "Pre-freeze controls"): add, from the same
   generator, H6 `<bogus> --<tok>=<tok>+<tok>` after `ls -la`, H7 `<bogus> <tok_nonascii>` after `ls -la`, H8
   `ls | <bogus>` after `ls -la`, H9 `<bogus> --opt=<tok>:<tok>` after `ls -la`, and P6 a command-free table fence
   that must not FAIL. The four H shapes hold on the base instrument (probe table; H6 was probed as
   `bogusxyz --opt=a+b`, the same path its generated form takes) and all four fail under UNION+EMPTY (and H6/H7 also
   under STRUCT). P6 does *not* hold at base — base FAILs the
   command-free table, which is the C2 defect — so P6 enters with the real fix and its must-fail arm is UNION+EMPTY
   (and any skip that empties a fence). None of these needs new tokens or classes beyond the existing generator.
3. If neither is done, C2's predicate should be withdrawn rather than trusted: the control meets it with a patch that
   fails the claim's stated acceptance cases.

## 7. Receipts and limits

Raw counter output (all 12 runs, counter sha and measured rev per run, exit codes):
`.ufo/waves/round-57/controls/CtlC2CharShortcuts.txt`. Commit map (`sandbox …`, base `ee50d8fa`): `6f3d177` PIPE,
`9159a5b` COLON, `ab46142` ARROW, `1afaf2c` PLUS, `646072a` NONASCII, `1e4eca7` DASHRUN, `590d214` UNION, `beb7c5c`
UNION−COLON, `93c9610` UNION+EMPTY, `43bf2dd` STRUCT, `f5505ff` LEADING. Probes: sandbox `scratch/probe.py`,
`scratch/probes.txt`, extracted trees `scratch/trees/{base,UNION_EMPTY,STRUCT,LEADING}`. No tool installs or upgrades
were needed; no pacman transaction was run; no model call was made. No writes in the lane except this report and the
raw file; no git/jj writes outside the sandbox clone; no C1 content and no fix to the C2 instrument written for
landing. [INFERENCE] The "cheapest" ordering (fallback over shape rule) is by changed lines in my harness, not by
effort: the fallback is 7 lines, the shape rule is 4 conditions; both are far cheaper than the real fix's fixture
work.
