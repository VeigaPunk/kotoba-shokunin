author: hyaku closure (non-author integrator, @m_zfl)

# Round 98 verifier spot-check (non-author closure of kotoba round 98)

This closes lane-round kotoba r98. Round base `a33f262fc94e3cf27f3c935b5c53c1336bb94166` (the
round-97 spot-check commit); lane tip `f5181e0fc01b1193983e5e8d30204ad5b83b654a`. Report:
`.ufo/reports/round-98/kotoba.md` in the fleet repo. The reviewer did not author the round and
changes no lane-authored file. No lane gate or lane counter was executed (PROTOCOL § Gate standard,
Closure consequence); gate/counter verdicts below are verified from committed receipts and say so.
Plain measurements (git/grep/wc/sha256/curl/census) were run by the reviewer on 2026-11-06.

Driver digest (copied from `.ufo/watchdog.log`, which can change):

```
2026-11-06T08:23:29-03:00 launch kotoba round=98 pgid=1261981 driver=hyaku-inline attempt=1
2026-11-06T10:32:54-03:00 complete kotoba round=98; hyaku-inline attempt=1
```

## Step-1 conformance

- **Report.** Fleet commit `1c6e454f72a44df32d31e7ddbc61a54b58449ef2`, author
  `kotoba-shokunin <kotoba@shokunin.local>`, committer date 10:32:24-03:00: after the last lane
  commit `f5181e0f` (committer 10:31:08) and before the `complete` line (10:32:54). `## SHONEN`
  heading present with 4 lines, one per box, all `[~]`.
- **Hashes.** `git cat-file -t` → `commit` and `git merge-base --is-ancestor <h> master` → true for
  `a060b450…`, `63cd48d9…`, `e61629f5…`, `280d8d01…`, `f5181e0f…` and the base `a33f262f…`.
  `git log a33f262f..f5181e0f` lists exactly those five round commits.
- **Pushed and clean.** `jj-lane.sh state` → `branch=master local=remote=f5181e0f… ahead=0 behind=0
  head=detached tracked=0 untracked=0`; `git status --porcelain` → empty;
  `git ls-remote origin refs/heads/master` → `f5181e0f…`.
- **Prompt.** `.ufo/prompts/kotoba-round-98.md` (committed by the lane identity, `c6a2c1a1`):
  `diff` of lines 1–140 against `templates/round-prompt.md` shows only placeholder substitutions
  (`{{LANE}}`, `{{ROUND}}`, `{{FLEET_ROOT}}`, `{{AXES}}`); §§ 1, 2, 2b, 3, 4, 5 present verbatim,
  hyaku addendum § 6 follows. Template contract carried.
- **Informational.** `a060b450` has author date 08:22:42, 47 s before the launch line (committer
  08:28:55, after it). This is jj's working-copy change creation time, not a pre-launch commit; no
  defect.

## Claims

### C1 — depth: dispatch-prompt checker self-test kills nine frozen survivors t01..t09

Re-measured (plain):

- `git diff -U0 a33f262f f5181e0f -- verifiers/verify_dispatch_prompts.py | grep '^@@'` →
  `@@ -1333,0 +1334,182 @@ def self_test() -> int:` — one pure insertion of 182 lines inside
  `self_test()` (`def self_test` ends at line 1525; the next `def box_proof` is line 1526). No
  production line changed.
- `git show f5181e0f:verifiers/verify_dispatch_prompts.py | grep -o 'r98-t0[0-9]' | sort | uniq -c`
  → all nine labels t01..t09 present (2–4 occurrences each); at `a33f262f` the count is 0.
- `git diff --quiet e61629f5 f5181e0f -- verifiers/` → identical: the landing bytes are the tip bytes.
- `git diff --quiet a33f262f a060b450 -- verifiers/verify_dispatch_prompts.py` and the same against
  `63cd48d9` → identical: the red-before revision carries base production and self-test bytes.
- `sha256sum` of `verifiers/fixtures/round-98/selftest-kills.py` at `a060b450` and `f5181e0f` →
  both `2f31fe040c9e…bd8f`; `forgery-controls.py` both `c4710da772f1…5fdc` — matching every
  receipt header.

Evidence-verified (committed receipts, counter not executed):

- `receipts/redbefore-c1-base.txt` (cmd `selftest-kills.py c1 a060b450…`):
  `C1 targets killed 0 of 9 … C1-PREDICATE-UNMET rc=1`.
- `receipts/landing/c1-v6.txt`: nine `mutant t0N … : KILLED` lines plus the positive;
  `C1 targets killed 9 of 9 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys
  held 9 of 9; code decoys held 9 of 9`, `rules v6: honest runs CLEAN 3 of 3; mirror runs reported
  10 of 10`, `C1-PREDICATE-MET rc=0`. `landing/c1-rulesv5.txt` MET with the same tally
  (separability holds).
- `landing/dp-selftest.txt`: `0 failure(s) over 128 assertions rc=0`; `dp-boxproof.txt`
  `boxes proven 2`; `prod-identity.txt` `1333a1334,1515`.
- Bound accepted as disclosed: t07 is observable-only (addendum 2 B2), so 8 of 9 kills are
  verdict-bearing.

Verdict: **C1 verifies. depth: improved.**

### C2 — consistency (calibration sub-axis): v6 counter refuses g10 and g11

Frozen kill rule (`plans/round-98.md`, § Claim C2, unchanged since freeze `63cd48d9`): unmet if the
landing reading is not `C2-PREDICATE-MET` rc 0.

Evidence-verified:

- before: `c2-before-v5.txt` `forgeries refused 3 of 5 … C2-PREDICATE-UNMET rc=1`;
  `c2-v6-as-v5.txt` `refused 3 of 5`; pre-data `c2-v6.txt` `refused 5 of 5 … MET`.
- landing: `landing/c2-v6.txt` g3/g7/g8/g10 rc 1 (refused), `g11-schedule-reader … seed
  deadbeefdeadbeef rc 0 R96C1-PREDICATE-MET`; `C2 v6: forgeries refused 4 of 5; honest held 2 of 2;
  bound g2b MET`, `C2-PREDICATE-UNMET rc=1`. `instr-identity.txt`: counter and runner bytes equal to
  the instrument commit.
- The post-WAVE-DONE `c2-v6-diagnostic-rerun.txt` reads 5 of 5 MET; the lane correctly keeps it
  diagnostic-only. Two readings of identical bytes at one revision disagree, so the v6 g11 refusal is
  not reproducible: it rests on a `/dev/shm` marker another process can delete (addendum 2 B1).

Verdict: **C2 does not verify (honest stop, as the lane itself reports). consistency: unchanged** —
the measured result missed its frozen predicate; no prior consistency instrument regressed
(`landing/r97-c2-v5.txt` `refused 3 of 3; honest held 2 of 2 … MET rc=0`).

### No-harm (evidence-verified + plain)

- `git diff a33f262f f5181e0f -- SCORECARD.md`: append-only (two new paragraphs: r98 axis
  annotations, r99 planned); no axis score moved. Whole round diff: 291 files, 21580 insertions,
  1 deletion.
- `SKILL.md`, `PROVINCE.md` unchanged (`git diff --stat` empty); `corpus/QUALITY.md` +1 row (Q88).
- Receipts: gate registry `74 of 74 … phantom 0 rc=0`; floors self-test `0 failure(s) over 176
  assertions`; `skill-identity.txt` rc 0; `dp-live-equal.txt` rc 0; r92/r93/r95/r96/r97 controls MET.
- Tip battery `2 of 6` at landing; the paired re-runs at `63cd48d9` and `e61629f5` show the same red
  set (`check_assertion_floors.py` timeout after 280 s, `verify_skill_checklist.py`,
  `verify_corpus_integrity.py`, `verify_corpus_independent.py` exit 1). Carried, not introduced.

## Per-axis verdicts

| axis | verdict | basis |
|---|---|---|
| depth | improved | C1: 0 → 9 of 9 frozen survivors killed, production bytes unchanged (re-measured diff + receipts) |
| consistency | unchanged | C2 landing reading 4 of 5, `C2-PREDICATE-UNMET` as frozen; no regression of r97 runner |
| coverage | unchanged | no `knowledge/` entry added |
| operability | unchanged | SKILL.md unchanged |
| freshness | unchanged | no entry re-verified for freshness |
| calibration | unchanged | C2 was declared on this sub-axis and missed |
| adjacency | unchanged | sibling g10/g11-class finding reported only; no sibling edited |

Round verdict: **not admitted — rejected-honest-stop** (C2 did not verify; no axis harmed).

## Discernment spot-check (LEARNING.md § Discernment is checked from outside)

Re-opened by the reviewer on 2026-11-06 with `curl -sS -L` + `sha256sum`; every size and digest
equals the lesson's access record.

| item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S279 ptrace(2) | admit (tier A, mined) | `https://man7.org/linux/man-pages/man2/ptrace.2.html` → 200, 104833 B, sha256 `69cd309e…f7bd35` | agree | HTML 1421–1424 list `/proc/pid/auxv, /proc/pid/environ, or /proc/pid/stat` under `PTRACE_MODE_READ`; step (4) at 1516 reads `Deny access if the target process "dumpable" attribute has a value other than 1` (14 words, located correctly); `grep -c cmdline` → 0, so the disclosed cmdline bound is grounded. Note: the quote stops before the conjunct at 1518–1520 (`and the caller does not have the CAP_SYS_PTRACE capability`); the denial is conditional, see routed defect 5. |
| S278 proc_pid_environ(5) | admit (tier A, mined) | `https://man7.org/linux/man-pages/man5/proc_pid_environ.5.html` → 200, 7747 B, sha256 `93394d9e…2c46` | agree | HTML 90–91 carry the governing-check sentence exactly as located (shaping disclosed); the row correctly states the denial is not on this page. |
| S280 PR_SET_DUMPABLE(2const) | reject (redundant) | `https://man7.org/linux/man-pages/man2/pr_set_dumpable.2const.html` → 200, 10905 B, sha256 `8336e5a5…220c` | agree | HTML 109–114 speak of `PTRACE_ATTACH` and `/proc/pid` file ownership; `grep -i environ` → no match, so it does not ground the environ-read denial rule 9 relies on; S279 does. Corrected reason and flip condition are sound. |

SOURCES row re-open: **S277** git-archive(1) (`https://git-scm.com/docs/git-archive` → 200,
50116 B, sha256 `fc4bbcfa…2d66`). HTML 1705 is `<h2 id="_description">…DESCRIPTION</h2>`; HTML
1708–1710 join to the quoted sentence; `printf '%s\n' "<quote>" | wc -w` → **23** (≤ 25), matching
the row and correction C98-1. Agree.

Census: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` → rc 0,
last line `kotoba	ok	…/kotoba-shokunin/corpus/SOURCES.md`, 34 `W04` (equal to the round
start). Rows `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` → 202 at `a33f262f`, 206 at
`f5181e0f`.

## Trend verdicts

- **expansion: unchanged** — no `knowledge/` entry admitted; S277–S280 are registry rows only.
- **quality: improved** — C1 verified: the province instrument's self-test now kills nine frozen
  behaviours it missed (8 verdict-bearing), production bytes unchanged, no admitted entry failed
  re-check.
- **discernment: improved** — the outside spot-check agrees with the gate on two admits and the
  reject; the plan's duplicate-URL row was refused before landing (Q84), and Q88 is grounded by the
  round's mined mistake 1 with a shown-able-to-fail control (v6-as-v5 3 of 5).

## Routed defects (lane fixes next round)

1. **C2 non-reproducible refusal.** v6's g11 refusal depends on a `/dev/shm/.r97-*` marker; two
   readings of identical bytes at `e61629f5` gave 4/5 and 5/5. A v7 refusal must not rest on a
   forger-reachable tmpfs marker (already planned in SCORECARD r99 — keep it falsifiable).
2. **Report line count.** The report's landed-changes row says "+183 lines inside `self_test()`";
   measured insertion is 182 lines (`@@ -1333,0 +1334,182 @@`); 183 is the two-file total including
   the QUALITY.md Q88 row. Append a correction.
3. **SCORECARD revision citation.** The r98 C1 annotation cites the red-before "at the freeze
   `63cd48d9`"; the receipt's command measures `a060b450` (instrument commit). Bytes are equal, so
   the value stands, but the named revision is wrong — append a correction (append-only).
4. **Tmpfs leftovers.** `/dev/shm/.r97-g11-run.*` markers from g11 world runs were left unremoved;
   g11 runs should write inside the round scratch so cleanup is attributable (scratch directive § 7).
5. **S279 conditional denial.** The row's `teaches` states denial for a non-dumpable target; step (4)
   also requires the caller to lack `CAP_SYS_PTRACE`. Name the conjunct (rule 9 holds only for an
   unprivileged child) in a correction row or the next lesson.
6. **Carried tip-battery reds** (2 of 6): `check_assertion_floors.py` 280 s timeout plus
   `verify_skill_checklist.py`, `verify_corpus_integrity.py`, `verify_corpus_independent.py` exit 1
   (ScoutTipReds causes: governance-pin drift since r81/82, corpus-index drift). Carried for many
   rounds; make it a declared claim.

## Operator note

SHONEN boxes remain `[~]`. Boxes 1, 2 and 4 cite committed evidence a non-author can read; promotion
review is operator-owned and not exercised here.
