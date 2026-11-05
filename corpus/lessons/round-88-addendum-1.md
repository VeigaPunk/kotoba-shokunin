author: KotobaR88 (lane L1)
round: kotoba 88 · appended 2026-11-05
scope: the round-87 closure's routed record defects R87-D1..R87-D6, corrected **append-only** (the cited
records are not rewritten). R87-D7 lands in `LOG.md` § Round 88 — R87-D7 correction; R87-D8 is the
instrument defect that this round's C1 v2 counter closes (`plans/round-88.md` § C1).
base: lane `4df1e8005016c75390a5e06b209462df58c95918` (the round-87 closure tip).

Each row names the superseded text, the command that measures the corrected value, and its observed
output. A correction is a second, dated statement beside the record; nothing above is edited in place
(`corpus/QUALITY.md` Q64: a token naming something that no longer exists is carried or left red, never
"corrected" to the record of its replacement).

## R87-D1 — the attempt history is counted, not remembered

The round-87 report's attempt arithmetic ("launched eight times before this attempt: 19:56, 20:35,
20:44, 21:02 …", and "this attempt is the third instance") mixes launch lines with lane-dead lines.
Measured over the fleet driver log at the corrected tip:

    $ grep -c 'launch kotoba round=87'     .ufo/watchdog.log   ->  7
    $ grep -c 'lane-dead-no-report kotoba round=87' .ufo/watchdog.log -> 6
    $ grep -c 'complete kotoba round=87'   .ufo/watchdog.log   ->  1

launch instants: `2026-11-04T19:56:11`, `20:35:59`, `20:44:38`, `22:29:17`, `22:31:27`, `22:32:19`,
`23:51:44` (-03:00). `21:02:56` is a `lane-dead-no-report` instant, not a launch. Round 87 therefore had
**seven launches, six deaths without a report, and one completing run** (the 23:51:44 launch, completed
`2026-11-05T00:35:22`).

## R87-D2 — `.ufo/reports/round-84/kama.md` carries a `## SHONEN` heading

Superseded: `corpus/lessons/round-87.md:86-88` — "another actor's fleet-root artifact that carries no
`## SHONEN` marker".

    $ grep -c '^## SHONEN' /home/vgpnk/Projects/shokunin/.ufo/reports/round-84/kama.md  ->  1
    $ stat -c '%s %y' /home/vgpnk/Projects/shokunin/.ufo/reports/round-84/kama.md
      10856 2026-11-04 22:47:40.415590042 -0300

The sentence was true when written (`e03f9e2`, 21:13); the file landed at 22:47 and the attempt-2 edit to
that lesson did not revisit it. Its red (`corpus.pointers.report_dead`) healed at that landing — which is
the mechanism behind `corpus/QUALITY.md` Q79(b): a **healed** red must not falsify a repair test. The
lesson's `**left red and disclosed**` disposition stands for the base revision it describes; the
present-tense "carries no `## SHONEN` marker" does not.

## R87-D3 — the frozen bound chain excludes `$HOME`

Superseded: `corpus/knowledge/omp-root-semantics-round87.md:46-47` — "frozen chain `/home/u/proj/sub` →
`/home/u/proj` → `/home/u`, stopping there".

    $ sed -n '88,91p' verifiers/check_omp_root_semantics.py
      BOUND_CWD = "/home/u/proj/sub"
      BOUND_HOME = "/home/u"
      FROZEN_CHAIN = (BOUND_CWD, "/home/u/proj")                        # cwd + ancestors below $HOME
      FULL_CHAIN = (BOUND_CWD, "/home/u/proj", "/home/u", "/home", "/")  # the unbounded walk-up

The frozen chain is TWO elements and stops **below** `$HOME`; `/home/u` and above exist only in
`FULL_CHAIN`, the unbounded world the counter is built to refuse. The r87 counter's docstring lists
`/home/u, /home, /` in the same breath and inherits the same confusion; it is the frozen instrument and is
not edited — the v2 counter's docstring states the split (r88 S4 conjunct, `plans/round-88.md` § C1
guard S4).

## R87-D4 — the entry's bound cell for `{cwd}/.omp/skills` has no receipt

Superseded: `corpus/knowledge/omp-root-semantics-round87.md:19` — the cell "project-scoped: session cwd
only".

The r87 counter's conjunct 4 applies one ancestor chain to **every** `{cwd}/` row
(`bound_grounded(pattern, chain)`), so the cell states a distinction the instrument does not make; and the
round's one live bound probe exercised `{cwd}/.agents/skills`, not this row
(`.ufo/waves/round-87/w3/ExecProbeBoundR87.md`). The measured statement is therefore: `{cwd}/.omp/skills`
is walked by `builtin.ts`'s single `dir: fr.join(k, Ou.projectDir, "skills")` join — a per-project single
join that composes no walk-up of its own, so the ancestor chain is the caller's, not the module's. The v2
counter tests the composed expansion set for the row and ExecLiveBound's probe
(`.ufo/waves/round-88/w1/ExecLiveBound/`) is the receipt; the cell's "session cwd only" is not claimed.

## R87-D5 — `SKILL.md` was line-normalized at `e03f9e2`

Superseded: the round-87 report's "`SKILL.md` untouched (`600 of 600` lines)" as a statement about the
round.

    $ git diff --numstat 223ae62 74048151 -- SKILL.md   ->  600  600  SKILL.md
    $ git log --format='%h %ci' 223ae62..74048151 -- SKILL.md  ->  e03f9e2 2026-11-04 21:13:57 -0300

All 600 lines changed but the line count did not: `e03f9e2` rewrote CRLF bytes as LF. The attempt-2 window
(`760e1c5e..3c8902a7`) is empty for this path, so the "untouched" reading holds for attempt 2 only. The
normalization is recorded here as a byte-level change, not a content change; the file's measured size at
the round-88 freeze is 600 lines / 87 772 B (Q78 measurements in `plans/round-88.md`).

## R87-D6 — a landing is not a commit

Superseded: the round-87 report attributing the 22:47 landing of `.ufo/reports/round-84/kama.md` to fleet
commit `5b052020`.

    $ git -C /home/vgpnk/Projects/shokunin log -1 --format='%h %cI' 5b052020
      5b052020 2026-11-04T12:16:01-03:00
    $ stat -c '%y' /home/vgpnk/Projects/shokunin/.ufo/reports/round-84/kama.md
      2026-11-04 22:47:40.415590042 -0300

The commit's date is 12:16:01, the file's arrival on the worktree is 22:47:40. A record that needs both
dates names both: the commit that carries the bytes, and the instant the measured world changed.

## Mistakes (round 88, append-only)

- **M88-1 · seat wrote a ready marker into the fleet root** — `ExecMonotoneD5` wrote `C2_READY` at the
  fleet root from a relative path, then removed it after the content was verified as its own.
  Captured-by: the wave context's absolute-path bound and the L1 misroot sweep (`git -C
  /home/vgpnk/Projects/shokunin status --porcelain` — clean of it at 06:07). Fix: the sweep, run before
  the report, over every seat-writable directory (Q40/Q49); the seat's self-report is the second signal,
  never the first.
- **M88-2 · a control's stated expectation is not a predicate property** — `w_added_red` was specified in
  `plans/round-88.md` § C2 as "an added unresolvable citation → D5 FAIL (ii)", but (ii) is a **name**-level
  monotone test and the added line lands under `corpus.pointers.commit_unresolvable`, already DRIFT at the
  base. The control therefore reads PASS by construction (`ExecMonotoneD5` F1: `commit_unresolvable`
  detail 2 in the added world vs 1 at the tip, DRIFT name set identical). Captured-by: none — no rule
  compares a control's stated expectation with the granularity of the conjunct it exercises. Fix (shown
  able to fail): the round reports the control as **miscalibrated, not passed**, keeps the frozen predicate
  and the failing self-test arm, and routes an instance-aware successor to round 89; a control expectation
  must be derived from the conjunct's own comparison unit before it is frozen.
