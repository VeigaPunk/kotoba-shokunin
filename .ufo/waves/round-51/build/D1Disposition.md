# D1Disposition — routed defect D1: the round-50 seat record and the after-the-last-WRITE sweep

Seat: `KotobaR51.D1Disposition` (build wave, round 51). Lane `/home/vgpnk/Projects/shokunin/kotoba-shokunin`,
read-only; my only lane write is this report. Base `43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10`.
Scratch: `/fast/scratch/hyaku/kotoba-r51/build/D1Disposition/lane` (private clone at the base commit).
No tool installed. No jj or git write command run in the lane, the fleet root, or a sibling lane.

## Result

**D1 holds as routed and is fully disposable with one commit, one addendum and one sweep command.**
The D1 defect has three separable parts, and each has exactly one correct answer:

1. **DescDraft.md** — commit it byte-exact as wave evidence with a one-line disposition. It carries no
   claim; its own recommendation is to keep the landed description; and it misdates the landing hash
   (`956ee167` for the description, which actually landed at `542f515`).
2. **Seat accounting** — the round-50 report's "2 cancelled" line is wrong, but the wrongness is
   narrower and stranger than the defect text says: **both** seats the report calls cancelled did write
   reports, and one of them (`D2D4Wording`) was *already committed* by the L1. The corrected count of
   seats that returned a report is 71 of 71, not 69 of 71.
3. **Sweep timing** — the sweep must run after the last seat **write**, not the last seat return. The
   exact command is in § Sweep command below; it is read-only, covers the lane and the fleet root, and
   re-runs itself if a seat writes during the sweep.

## 1. Disposition of `DescDraft.md` — one sentence

> **Commit `.ufo/waves/round-50/build/DescDraft.md` byte-exact as round-50 wave evidence with the
> disposition line "round-50 build seat `KotobaR50.DescDraft` output, not claim-bearing: it recommends
> keeping the landed description and its own draft was not used; it misdates the C1 landing as
> `956ee167` when the description landed at `542f515`" — the file changes no claim, no counter and no
> landed text.**

Why byte-exact and why "not claim-bearing", with the command that shows it:

- The file is currently **untracked** in the lane and has never been committed:
  `git -C kotoba-shokunin log --all --format='%H' -- .ufo/waves/round-50/build/DescDraft.md | wc -l`
  → `0`; `git -C kotoba-shokunin status --porcelain --untracked-files=all -- .ufo/waves/`
  → `?? .ufo/waves/round-50/build/DescDraft.md` (exit 0). It is the **only** uncommitted round-50 seat
  report: 70 of 71 wave `.md` files are committed (`git ls-files '.ufo/waves/round-50/build/*.md'
  '.ufo/waves/round-50/falsify/*.md' | wc -l` → `70`; on disk `ls .ufo/waves/round-50/build/*.md
  .ufo/waves/round-50/falsify/*.md | wc -l` → `71`). Every other round-50 seat report is in the tree.
- **It carries no claim.** Its own Result paragraph recommends the opposite of a change: "Recommendation:
  keep the landed description … the draft is delivered as a verified alternative, not as a request to
  replace the landed text" (`DescDraft.md:12`). The landed description is the L1's — `LOG.md:2391` and
  `LOG.md:2409` both record `DescDraft` as a seat whose output the L1 did not use. The draft is also
  *not* the landed text: it drops the `kengaku` word "measured capability" that the falsify wave
  required (`CriticC1Landed.md` F3; `ReviewDescAccuracy.md` F1), so landing it would re-open a
  corrected defect.
- **Its landing hash is misdated**, and this is the reason a disposition line is needed at all: the file
  says the L1 "landed a different description at `956ee167`" (`DescDraft.md:11`, and `:71`, `:74`, `:106`
  use `956ee167` as the baseline). `956ee167` did not touch `SKILL.md` at all —
  `git show --stat --format='' 956ee167 -- SKILL.md` → empty. The description landed at **`542f515`**
  (`git show --stat --format='' 542f515 -- SKILL.md` → `SKILL.md | 14 ++++++++------`). The file's own
  length arithmetic is also one commit stale: it measures the landed text at 1,009 parsed / 1,008 by the
  guard reader, but the head text (`43ca0bfb`) parses to 1,020 / 1,019 because `a78fec1` narrowed the
  `kengaku` clause. Its draft still passes the guard on its own terms (9 of 9, 1,018 of 1,024, exit 0),
  so it is a valid alternative — just not the landed one, and not a correction to it.
- Byte-exactness: the L1 must copy the file without edits. `sha256sum` →
  `0181a45953242fcff7595a91d8c1036b10dc4dc7aaae5303baa1cb445c3d2348`, 10,079 B. Any re-typed text
  breaks the "byte-exact" condition the defect sets.

**Note on where the disposition line goes.** The round-50 report is a *fleet* file
(`/home/vgpnk/Projects/shokunin/.ufo/reports/round-50/kotoba.md`) and it is **append-only**: its line 4
is frozen and every later fact goes in an appended `## Addendum` block at the end. So the disposition
line belongs in a new addendum block in the fleet report, and the `DescDraft.md` file itself goes into
the **lane** tree (`.ufo/waves/round-50/build/DescDraft.md`). Two different repositories; the L1 owns
both. I am read-only on both and wrote neither.

## 2. Seat-accounting correction (appended to the round-50 record)

The defect says: "the report calls `DescDraft` and `D2D4Wording` cancelled, but both wrote reports
later." That is true, and the correction has a sharper shape than the defect text suggests.

**The offending line** — `.ufo/reports/round-50/kotoba.md:96-97`:

> "0 died; 2 cancelled by the L1 after an hour without a report (`DescDraft`, `D2D4Wording`; their work
> was done by the L1); `FloorsRegister` and `PrecedenceDraft` returned late and were superseded."

**What the evidence shows, with times.**

| seat | report file mtime (-0300) | in the lane tree? | evidence |
|---|---|---|---|
| `D2D4Wording` | **10:51:16.487** | **yes — committed** | `git log --format='%H %cI %s' -- .ufo/waves/round-50/build/D2D4Wording.md` → `2abd290e… 2026-10-22T10:51:22-03:00` and `1cb2e65e… 2026-10-22T10:51:01-03:00`; the working copy is byte-identical to HEAD (`git hash-object` → `c26b2465…` = `git rev-parse HEAD:…` → `c26b2465…`) |
| `DescDraft` | **10:52:19.555** | **no — untracked** | `git log --all -- …/DescDraft.md \| wc -l` → `0`; `git status --porcelain --untracked-files=all -- .ufo/waves/` → `?? .ufo/waves/round-50/build/DescDraft.md`; `sha256sum` → `0181a459…`, 10,079 B |
| `FloorsRegister` | 10:47:49.052 | yes — committed | `git log -- …/FloorsRegister.md` → `1cb2e65e… 2026-10-22T10:51:01-03:00` |
| `PrecedenceDraft` | 10:39:45.333 | yes — committed | `git log -- …/PrecedenceDraft.md` → `bf109cac… 2026-10-22T10:41:43-03:00`, `a78fec1f… 2026-10-22T10:39:10-03:00` |

The last lane commit of round 50 is `2abd290eac782972df6a943fa8fcf8a18a41d4f2`, **10:51:22 -0300**
(`git log -1 --format='%H %cI' 2abd290e…`). `D2D4Wording` wrote **6 s before** it and the L1 committed
that write in the same commit. `DescDraft` wrote **57 s after** it — the "57 s" in the defect text — and
is still untracked.

**The corrected counts.**

- Seats that **returned a report**: **71 of 71** (33 build + 38 falsify), not 69 of 71. Every seat in
  both specs has its report file on disk, and the only one missing from the tree is `DescDraft.md`
  (which is what part 1 commits). Command:
  `python3 -c "import json,os;[print(w,len([i['name'] for i in json.load(open(f'.ufo/waves/round-50/{w}-spec.json'))['items']]),len([f for f in os.listdir(f'.ufo/waves/round-50/{w}') if f.endswith('.md')])) for w in ('build','falsify')]"`
  → `build 33 33`, `falsify 38 38` (exit 0).
- Seats **cancelled**: **0**. Both named seats produced a report; `D2D4Wording`'s is committed.
- Seats that **died**: **0** (the report already says this; it is correct).
- Seats whose report **arrived after the L1 had already done their work** — the honest category, and it
  covers four seats, not two: `PrecedenceDraft` (10:39:45, after the rule landed at `956ee167`),
  `FloorsRegister` (10:47:49, after the registration landed at `542f515`), `D2D4Wording` (10:51:16,
  after the qualifiers landed at `956ee167`/`a78fec1`), `DescDraft` (10:52:19, after the description
  landed at `542f515`). The report's "2 cancelled" and "2 returned late" split is the wrong axis: the
  four seats share one fact — the L1's work was already landed when their report landed — and the
  difference between them is only whether the L1 committed it.
- Reports **committed**: 70 of 71 before this round; 71 of 71 after part 1.

**The text to append.** The round-50 report is append-only (`ReviewD1D5Facts.md`: line 4 is frozen, each
addendum is a new `## Addendum` block at the end, and the current lane head goes *inside* the addendum).
Append at the end of `/home/vgpnk/Projects/shokunin/.ufo/reports/round-50/kotoba.md`:

```
## Addendum (seat accounting, routed defect D1; lane head 43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10 at this addendum)

- Seat accounting corrected. The line above that "2 cancelled by the L1 after an hour without a report
  (`DescDraft`, `D2D4Wording`)" is wrong: no seat was cancelled and no seat died. All 71 seats
  (33 build + 38 falsify) returned a report; every seat report is on disk under
  `.ufo/waves/round-50/`, and 70 of 71 are committed in the lane. The four build seats whose reports
  arrived after the L1 had already landed the same work are `PrecedenceDraft` (10:39:45), `FloorsRegister`
  (10:47:49), `D2D4Wording` (10:51:16) and `DescDraft` (10:52:19), local time -0300; the last lane commit
  of the round is `2abd290e` at 10:51:22. `D2D4Wording`'s report is committed (`2abd290e`);
  `DescDraft`'s was not, and is committed byte-exact with this addendum, with the disposition line
  "round-50 build seat `KotobaR50.DescDraft` output, not claim-bearing: it recommends keeping the landed
  description and its own draft was not used; it misdates the C1 landing as `956ee167` when the
  description landed at `542f515`".
- Sweep. The misroot and leftover sweep is run after the last seat WRITE, not after the last seat
  return (M32's class, now inside the lane); the round-50 sweep line above was filed after the last
  return and missed the `DescDraft` write 57 s after the last lane commit.
```

The same correction belongs in the lane's `LOG.md` round-50 landing-pin entry — the line
`LOG.md:2409` ("Build seats without a usable report at landing: `FloorsRegister` … `DescDraft` … `D2D4Wording` …
`PrecedenceDraft` returned after …") already names the four seats and is correct as far as it goes, but
`LOG.md:2391` says only "`FloorsRegister` and `DescDraft` were overtaken". Those two lines disagree about
how many seats were overtaken; the addendum above settles it. I did not edit `LOG.md` (lane read-only
for this seat).

## 3. Sweep command for this round — after the last seat WRITE, not the last return

The defect's instruction is the point: a seat can return (its process exits, the driver records the
return) and *then* write its file, or write it after the L1's last commit. `DescDraft` did exactly that
— 10:52:19, 57 s after the last lane commit, and the round-50 report was filed at 10:52:08. A sweep keyed
to the last return cannot see it. The command below is keyed to file **mtime** under the wave trees, so
it detects a write that lands after every seat has returned, and it re-runs itself if a seat writes
while the sweep is running.

Read-only, and it touches neither repository: `git status` and `find` only, `--no-optional-locks` so no
index lock is taken and no `.git/index` write occurs (verified: the fleet `.git/index` mtime is
unchanged across the run).

```bash
# D1 sweep — run after the LAST seat WRITE (mtime), not after the last seat return.
# Read-only. Lane + fleet root. Re-runs itself if a seat writes during the sweep.
LANE=/home/vgpnk/Projects/shokunin/kotoba-shokunin
FLEET=/home/vgpnk/Projects/shokunin
WAVES="$LANE/.ufo/waves $FLEET/.ufo/waves"
newest() { find $WAVES -type f -printf '%T@ %TY-%Tm-%TdT%TH:%TM:%TS %p\n' 2>/dev/null | sort -n | tail -1; }
for pass in 1 2 3 4 5; do
  T0=$(date +%s)
  echo "===== D1 sweep pass $pass  (lane HEAD $(git -C "$LANE" rev-parse --short HEAD))  start epoch $T0"
  echo "-- (1) last seat WRITE anywhere under the wave trees (mtime, not return):"; newest
  echo "-- (2) LANE: untracked under .ufo/waves/  [leftover seat write never committed]"
  git -C "$LANE" --no-optional-locks status --porcelain --untracked-files=all -- .ufo/waves/ \
    | while read -r st f; do printf '   %s  mtime %s  %s\n' "$st" "$(stat -c '%y' "$LANE/$f")" "$f"; done
  echo "-- (3) FLEET ROOT: untracked anywhere     [misroot, M32 class]"
  git -C "$FLEET" --no-optional-locks status --porcelain --untracked-files=all | grep -E '^\?\?' || echo "   (no untracked files)"
  echo "-- (4) files written DURING this pass (a seat writing now -> re-run):"
  find $WAVES -type f -newermt "@$T0" 2>/dev/null | sed 's/^/   /'
  a=$(newest); sleep 2; b=$(newest)
  if [ "$a" = "$b" ]; then echo "== FIXED POINT: no seat wrote during the sweep; the sweep is valid"; break; fi
  echo "== a seat wrote during the sweep; re-running"
done
```

Why each part, and what it is for:

- **(1) and the fixed-point loop** are the fix for the defect's third clause. The sweep is valid only
  when the newest wave-file mtime is unchanged across the whole pass; a seat that writes *during* the
  sweep changes it and the loop re-runs. The loop is capped at 5 passes, so a permanently writing seat
  ends the loop with an explicit "a seat wrote during the sweep; re-running" on the last pass rather
  than a false "FIXED POINT".
- **(2) LANE untracked under `.ufo/waves/`** is the class the defect is actually about — a seat report
  written into the lane and never committed. `DescDraft.md` is the round-50 instance: it shows as
  `?? .ufo/waves/round-50/build/DescDraft.md` with mtime 10:52:19, and it is the only round-50 wave file
  still uncommitted. The mtime is printed so the L1 can see *when* each file was written, not just that
  it exists. The `while read` loop needs the status output unquoted; `--porcelain` gives `XY path` with
  one space, so `read -r st f` splits correctly (verified: every line printed with a real mtime).
- **(3) FLEET ROOT untracked anywhere** is the M32 misroot class. Round 49's instance was
  `.ufo/waves/round-49/falsify/RowGameDev2d.md` sitting in the fleet root. The fleet root's
  `.gitignore` has `*-shokunin/`, so a lane's own directory is invisible there — the misroot shows up as
  an untracked path under the fleet's `.ufo/waves/`. The grep keeps the operator's own fleet-root noise
  (`.ufo/state/*`, `watchdog.log`, the staged `write` file — 18 paths today, none of them untracked) out
  of the seat signal while still printing any `??` path. Run without the grep if the L1 wants the full
  fleet-root list.
- **(4)** lists files written since the pass start, so a write landing mid-sweep is visible even if its
  path is already tracked.

Verified on this host, exit 0, `FIXED POINT` reached on pass 1, fleet root clean
(`(no untracked files)`), lane showing `?? .ufo/waves/round-50/build/DescDraft.md` (mtime 10:52:19) plus
the round-51 wave files still in flight. The command was also run against a probe file planted in a
private clone's `.ufo/waves/round-51/build/` and printed it — the detection works, and the probe was
removed (`git status --porcelain --untracked-files=all -- .ufo/waves/` → empty afterwards).

**Timing instruction for the L1.** Run this sweep **after the last seat has written its file**, not when
the last seat returns. The operational test is (1): if the newest wave-file mtime is older than the
moment the last seat reported, the sweep is running against a settled tree. Run it again after the
final landing commit as well, because a landing commit can be what makes a leftover visible.

## Findings

1. **The defect's "both wrote reports later" understates it for `D2D4Wording`.** That seat's report is
   *committed* — `2abd290e`, the L1's own last round-50 commit, 6 s after the seat's write. The
   cancellation label is contradicted by the lane tree itself, not merely by a file on disk. The
   corrected count is 71 of 71 seats returning, 0 cancelled, 0 died.
2. **The report's "2 cancelled / 2 returned late" split is the wrong axis.** All four late build seats
   share one fact (the L1's work was already landed when their report landed) and differ only in
   whether the L1 committed it. Recounting on the "returned a report" axis gives 71 of 71; recounting on
   the "committed" axis gives 70 of 71 before this round's part 1 and 71 of 71 after.
3. **`LOG.md:2391` and `LOG.md:2409` disagree about the same fact.** Line 2391 names two seats overtaken
   ("`FloorsRegister` and `DescDraft` were overtaken"); line 2409 names four ("Build seats without a
   usable report at landing: `FloorsRegister` … `DescDraft` … `D2D4Wording` …; `PrecedenceDraft` returned
   after …"). The addendum in § 2 settles both onto four.
4. **`DescDraft.md`'s length arithmetic is one commit stale**, independent of its misdated hash: it
   measures the landed description at 1,009 parsed / 1,008 by the guard reader, while the head text
   (`43ca0bfb`) is 1,020 / 1,019 after `a78fec1` narrowed the `kengaku` clause. Its draft (1,019 / 1,018)
   and the head text are within one character of each other, not the 11 the file claims.
5. **The draft would re-open a corrected defect if landed.** It writes `kengaku owns prompt-format
   effects`, dropping the "measured capability" the falsify wave required
   (`CriticC1Landed.md` F3, `ReviewDescAccuracy.md` F1; fixed at `a78fec1`). This is a second reason
   the disposition is "evidence, not change" — independent of the seat's own recommendation.
6. **The round-50 census line pin is off by one and still uncorrected.** `DescDraft.md:128-131` reports
   it: `corpus/knowledge/sibling-overlap-census-round49.md:243-244` says the round-50 description moved
   the discovery-root note to lines 15-17, but at `43ca0bfb` the note is at lines 16-18
   (`grep -n "Note:\|omp skill discovery roots\|omp router" SKILL.md` → 16, 17, 18). At `956ee167` the
   note *was* at 15-17; `a78fec1` shifted it down one line and nothing updated the pin. The census entry
   is append-only, so the fix is an appended correction, not an edit of lines 243-244. This is a
   different seat's file; I did not edit it.
7. **The round-50 report's frozen header is already stale in a way D1 covers.** Line 4 names
   `2abd290e`; the lane head is now `43ca0bfb` (the closure commit). Per `ReviewD1D5Facts.md`, the
   current head goes *inside* an appended addendum, never as a rewrite of line 4. The addendum in § 2
   carries it.

## Evidence (commands, exit codes verbatim)

```
git -C kotoba-shokunin rev-parse HEAD                                    → 43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10
git -C kotoba-shokunin log --format='%H %ci %s' f3046466..43ca0bfb        → 8 commits, 10:25:02 → 11:04:58
stat -c '%y %s %n' .ufo/waves/round-50/build/DescDraft.md                 → 2026-10-22 10:52:19.554935837 -0300 10079
stat -c '%y %s %n' .ufo/waves/round-50/build/D2D4Wording.md               → 2026-10-22 10:51:16.487390231 -0300 18592
sha256sum .ufo/waves/round-50/build/DescDraft.md                         → 0181a45953242fcff7595a91d8c1036b10dc4dc7aaae5303baa1cb445c3d2348
git log --all --format='%H' -- .ufo/waves/round-50/build/DescDraft.md | wc -l   → 0
git status --porcelain --untracked-files=all -- .ufo/waves/               → ?? .ufo/waves/round-50/build/DescDraft.md  (+ 33 round-51 files)
git ls-files '.ufo/waves/round-50/build/*.md' '.ufo/waves/round-50/falsify/*.md' | wc -l   → 70
ls .ufo/waves/round-50/build/*.md .ufo/waves/round-50/falsify/*.md | wc -l               → 71
git log --format='%H %cI %s' -- .ufo/waves/round-50/build/D2D4Wording.md → 2abd290e… 2026-10-22T10:51:22-03:00 / 1cb2e65e… 10:51:01-03:00
git hash-object .ufo/waves/round-50/build/D2D4Wording.md                  → c26b2465514d68c072f7ebd2b41655aff876dc00
git rev-parse HEAD:.ufo/waves/round-50/build/D2D4Wording.md              → c26b2465514d68c072f7ebd2b41655aff876dc00  (identical)
git log --format='%H %cI %s' -- .ufo/waves/round-50/build/FloorsRegister.md   → 1cb2e65e… 2026-10-22T10:51:01-03:00
git log --format='%H %cI %s' -- .ufo/waves/round-50/build/PrecedenceDraft.md → bf109cac… 10:41:43-03:00 / a78fec1f… 10:39:10-03:00
git log -1 --format='%H %cI' 2abd290eac782972df6a943fa8fcf8a18a41d4f2   → 2abd290e… 2026-10-22T10:51:22-03:00
python3 (spec items vs report .md on disk, build then falsify)            → build 33 33 ; falsify 38 38 ; missing [] []   (exit 0)
git -C /home/vgpnk/Projects/shokunin log -1 --format='%H %ci %s' cc7d6420 → cc7d6420… 2026-10-22 10:52:09 -0300  (round-50 kotoba report filed)
stat -c '%y %n' /home/vgpnk/Projects/shokunin/.ufo/reports/round-50/kotoba.md → 2026-10-22 10:52:08.988899180 -0300
git show --stat --format='' 956ee167 -- SKILL.md                         → (empty — 956ee167 did not touch SKILL.md)
git show --stat --format='' 542f515 -- SKILL.md                         → SKILL.md | 14 ++++++++------  (1 file changed)
git show 956ee167:SKILL.md | python3 yaml → parsed 1009 stripped 1008
git show 43ca0bfb:SKILL.md | python3 yaml → parsed 1020 stripped 1019
git show a78fec1:SKILL.md | grep -o "kengaku owns[^;]*;"   → kengaku owns measured capability effects of prompt format;
git show 542f515:SKILL.md | grep -o "kengaku owns[^;]*;"   → kengaku owns measured effects of prompt format;
python3 (DescDraft.md yaml block)                           → parsed 1019 stripped 1018
python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md \
  --province PROVINCE.md --skill <head SKILL.md>            → rows 20 verified 20 / province rows 20 matched 20 /
                                                             skill description names 9 of 9 non-none lanes /
                                                             skill description length 1019 of 1024   (exit 0)
python3 -B verifiers/check_sibling_census.py … --skill <DescDraft draft>  → same 9 of 9; length 1018 of 1024   (exit 0)
grep -n "Note:\|omp skill discovery roots\|omp router" SKILL.md             → 16, 17, 18
grep -n "moved that note to lines" corpus/knowledge/sibling-overlap-census-round49.md → 244
git show 956ee167:SKILL.md | grep -n "Note:\|omp skill discovery roots\|omp router" → 15, 16, 17
git -C /home/vgpnk/Projects/shokunin status --porcelain --untracked-files=all | grep -E '^\?\?'  → (no output; exit 1)
git -C /home/vgpnk/Projects/shokunin status --porcelain --untracked-files=all  → 18 paths, 0 of them `??` (operator's own)
stat -c '%y %n' /home/vgpnk/Projects/shokunin/.git/index  before/after the sweep → unchanged
```

## Out of scope / not done

- **No lane file was edited** except this report. `DescDraft.md` is not committed by me (lane is
  read-only for this seat; the L1 owns the commit). `LOG.md`, the census entry and the fleet report are
  other owners' files; § 2 gives the exact text to append.
- **The sweep command was not run against the fleet root's full `git status` output** for the final
  report — the grep filter is in the shipped command by design (see § 3).
- The census line-pin finding (finding 6) is a different seat's file and is not fixed here.
- No web sources opened. No tool installed or upgraded (`~/.omp/agent/RULES.md` read; no pacman, `uv`,
  `cargo` or `npm` transaction was needed — the seat needed only `git`, `find`, `stat` and `python3`,
  all present at git 2.56.0).
- Bounds honoured: no git write command and no mutating `jj` command in the lane, the fleet root or any
  sibling lane; `jj` was not invoked anywhere; the fleet root was read with `git` only
  (`--no-optional-locks`, no index write).

## Report

`.ufo/waves/round-51/build/D1Disposition.md`
