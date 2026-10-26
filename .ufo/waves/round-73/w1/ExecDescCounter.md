# ExecDescCounter — round 73 wave 1 (C2 replacement, seat report)

`Report:` `.ufo/waves/round-73/w1/ExecDescCounter.md`

Verdict: the replacement-C2 counter is drafted, self-tested (71 assertions, 0 failures) and reads the
frozen do-nothing value at the round base — `own-description rules held 1 of 3`, exit 1 (`R3` only).
The M127 cause is **confirmed independently**, with one correction to its stated mechanism: `--repo .`
loses both the fleet root *and* the link targets, and the citation targets it needs exist only at the
fleet root, so absolutising the symlink targets alone would not repair it. One calibration delta found
and measured: under the frozen R1 definition the base first sentence is **150** characters, not the
addendum's 151 (the addendum counts the terminal period). The verdict is unchanged (both are outside
40–99), but the receipt text must carry the reading the counter prints.

Deliverable: `.ufo/waves/round-73/w1/build/ExecDescCounter/check_own_description.py` (draft; the L1
installs it at `verifiers/check_own_description.py` before freeze 2). No committed lane file was
modified by this seat; the only writes are the draft, this report, and `/tmp` sandboxes.

## 1. The counter and its frozen lines

Frozen predicate, carried verbatim in the module docstring:

```
python3 -B verifiers/check_own_description.py --rev <rev>  ->  prints
"own-description rules held N of 3", exit 0 when N == 3
```

Printed at the base (last line is the frozen line; `first sentence`, `first 99 characters`, `triggers`,
`R1/R2/R3`, `frontmatter lines` precede it):

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-73/w1/build/ExecDescCounter
$ python3 -B check_own_description.py --rev 072048fa8e8a52c707d25f7079772fa317244eb7 ; echo EXIT=$?
own-description rev 072048fa8e8a52c707d25f7079772fa317244eb7 (lane /home/vgpnk/Projects/shokunin/kotoba-shokunin, base 072048fa8e8a52c707d25f7079772fa317244eb7)
description 1019 characters (R3 ceiling 1024)
first sentence 150 characters: Prompt & skill craft — audits, writes, and rewrites SKILL.md / AGENTS.md / dispatch prompts / system prompts for trigger fidelity and decision density
first 99 characters: Prompt & skill craft — audits, writes, and rewrites SKILL.md / AGENTS.md / dispatch prompts / syste
triggers (8): "skill file", "SKILL.md", "frontmatter description", "trigger words", "prompt craft", "write a skill", "audit this skill", "skill quality"
R1 fail: first sentence 150 characters is outside 40-99
R2 fail: whole words skill+prompt yes; no quoted trigger in the first 99 characters
R3 pass: description 1019 <= 1024; verifiers/check_sibling_census.py exit 0
frontmatter lines 19->19 (inserted 0, deleted 0 inside the frontmatter)
own-description rules held 1 of 3
EXIT=1
real	0m1.602s
```

`1 of 3` is the do-nothing value the addendum fixes (`R3 only; R1: the first sentence is 151
characters; R2: no quoted trigger in the first 99`). Two of the addendum's three clauses match the
measurement exactly; the third is the delta below.

Reader parity, measured: the counter's folded `D` is 1019 characters, and the tree's own census gate
prints `skill description length 1019 of 1024` for the same revision — two independent readers of the
same frontmatter agree on the byte count. The counter copies `description_of` from
`verifiers/check_sibling_census.py:380-401` rather than importing it (the census gate is run as a
subprocess from the sandbox, so importing would read the *counter's* tree, not `<rev>`'s).

### 1.1 Calibration delta: 150 vs 151

Frozen R1: "the text before the first `. ` or `: ` followed by an uppercase letter". In the base `D`
the first such match is `density. Triggers`; `D[:150]` is the sentence, so the length is 150, and the
"151" in the addendum/considerthese is that sentence **plus its full stop**.

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin && python3 -c '
import re,subprocess
t=subprocess.run(["git","-C",".","show","072048fa8e8a52c707d25f7079772fa317244eb7:SKILL.md"],capture_output=True,text=True).stdout
f=t.split("\n---",1)[0]
d=re.sub(r"\s+"," ",re.search(r"^description:(.*?)(?=^\S|\Z)",f,re.S|re.M).group(1)).strip().lstrip(">").strip()
m=re.search(r"\. (?=[A-Z])|: (?=[A-Z])",d)
print("len(D)",len(d),"sentence",len(d[:m.start()]),"with period",len(d[:m.start()])+1)'
len(D) 1019 sentence 150 with period 151
```

Observed, from the counter's own lines above: `first sentence 150 characters`. Arithmetic: 150 + 1
(the `.` that the definition excludes) = 151. Both values fail R1 (151 > 99 either way, and the
distance to the 99-character boundary is 51 or 52 characters), so the rule verdict, the `1 of 3`, and
the exit code are unaffected. Recommendation to the L1: the receipt for C2's do-nothing control should
say **150 characters under the frozen definition** (151 with the terminal period) so the receipt and
the counter cannot be read as disagreeing.

## 2. Self-test — 71 assertions, isolated fixtures

```
$ python3 -B check_own_description.py --self-test ; echo EXIT=$?
self-test: 0 failure(s) over 71 assertions
EXIT=0
real	0m2.39s
```

Every arm builds a throwaway `fleet/{kotoba-shokunin,alpha-shokunin}` pair under a
`tempfile.TemporaryDirectory`, commits inside it (`git init` + `-C`), and drives `main()` in-process.
No live-tree write; the only live read is the census gate copied into the fixture lane
(`REAL_GATE = LANE/verifiers/check_sibling_census.py`), so `R3` exercises the tree's own gate rather
than a mock, plus stub-gate arms for the plumbing.

Coverage against the addendum's shortcut worlds (each must read below 3):

| addendum shortcut world | self-test arm | observed |
|---|---|---|
| 99-character first sentence, no quoted trigger | `r2-noquote` | 2 of 3, `R1 pass: first sentence 99 characters`, R2 names "no quoted trigger" |
| first sentence under 40 characters | `len-39` | 2 of 3 |
| quoted string not in the Triggers list | `r2-foreign` | 2 of 3, names `"not a trigger"` |
| cut to ≤ 99 dropping Triggers + sibling clauses | `r3-cut` (47 chars) | 1 of 3; gate refuses `does not name the non-none census lane alpha` |
| description over 1,024 characters | `r3-over` (1025) | 2 of 3, `description 1025 characters`, R3 fail |
| period inserted mid-phrase, old sentence continues | `r1-midphrase` | 2 of 3; `first sentence 22 characters: Prompt and skill craft`, R2 pass, printed for the non-author reviewer |

Boundary arms: first sentence 40 and 99 read 3 of 3 (exit 0); 39 and 100 read 2 of 3 (exit 1);
description exactly 1024 reads 3 of 3, 1025 reads 2 of 3. Reader arm: a column-0 `Triggers:` line
after an indented description block is not swallowed (`triggers (0): none`, 2 of 3) — the round-50
m8 termination rule; the swallow-everything reader would have scored 3. No-frontmatter arm: 0 of 3,
exit 1. Could-not-evaluate arms: unknown revision, missing census gate, missing fleet root,
fleet-root==lane (M127), and a directory that is not a git top level all exit 2 with
`could-not-evaluate:` on stderr and **no** rule line on stdout. Sandbox arms: the parent holds
exactly the fleet's sibling lanes, the clone's `HEAD` is the measured revision, and the sandbox
`SKILL.md` is the revision's. Guard arms: a line added outside the frontmatter prints
`inserted 0, deleted 0 inside the frontmatter` and keeps 3 of 3; a description line split in two
inside the frontmatter prints changed `frontmatter lines` and inserted > 0 and **still** reads 3 of 3
— the guard is printed, never counted, as the addendum requires.

## 3. M127 — confirmed, with a sharper mechanism

Cause line (`sed -n '606,612p' verifiers/check_tip_battery.py`):

```
    repo = Path(args.repo)
    fleet = Path(args.fleet) if args.fleet else repo.parent
```

With `--repo .`, `repo = Path(".")` and `Path(".").parent == Path(".")`:

```
$ python3 -c "from pathlib import Path; print(repr(str(Path('.').parent)))"
'.'
$ python3 -c "from pathlib import Path; print(repr(str(Path('.').resolve().parent)))"
'/home/vgpnk/Projects/shokunin'
```

Two separate failures follow, and my probe separates them. Built the sandbox exactly as
`build_sandbox` does for a `Path(".")` fleet root (relative entries from `Path(".").iterdir()`,
`symlink_to(relative)`), then ran the r72 checklist gate in it:

```
broken sandbox links: {'corpus': ('corpus', False), '.ufo': ('.ufo', False), 'verifiers': ('verifiers', False)}
broken gate exit 1
FAIL trigger.citation_resolves: evaluated 187 — line 558: '../.ufo/reports/round-7/kotoba.md' does not resolve from /tmp/k73w1-m127-broken.43kojkki/kotoba-shokunin
correct gate exit 0
PASS trigger.citation_resolves: evaluated 187 — 187 repo-rooted citation token(s) resolve from the repo root
```

`readlink` shows the links carry **relative** targets (`corpus` → `corpus`), and a relative target
resolves against the link's own directory, so every link dangles (`exists False`), not merely points
into the lane. The second half is why "the sandbox symlinks the lane's own entries" is not the whole
cause: the citation targets the lane cites are at the *fleet* root and absent from the lane —

```
$ ls -l /home/vgpnk/Projects/shokunin/.ufo/reports/round-7/kotoba.md      -> 8037 bytes
$ ls /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/reports/round-7/kotoba.md
ls: cannot access '...': No such file or directory
```

so a lane-as-fleet-root sandbox fails even with absolute link targets — measured, not inferred:

```
lane-as-fleet-root with ABSOLUTE link targets, then the same gate in the same shape:
links resolve: {'corpus': True, '.ufo': True}
lane-as-fleet, absolute targets: gate exit 1
FAIL trigger.citation_resolves: evaluated 187 — line 558: '../.ufo/reports/round-7/kotoba.md' does not resolve …
```

Both halves are load-bearing: the fleet root must be the fleet root *and* the links must point at it.
The repair restores the fleet root (`repo.resolve().parent`), which is what the counter does; the
counter additionally refuses a fleet root equal to the lane
(`fleet root <path> is the lane itself: a sandbox shaped from it is not fleet-shaped (M127)`, exit 2)
so the shape cannot regress silently.

## 4. Fix shape for C3 (for the C3 seats; not applied here)

One line in `check_tip_battery.py:609-610`:

```
-    repo = Path(args.repo)
-    fleet = Path(args.fleet) if args.fleet else repo.parent
+    repo = Path(args.repo).resolve()
+    fleet = Path(args.fleet).resolve() if args.fleet else repo.parent
```

Red-before (reproduced here, §5): `--repo .` → `2 of 6`; `--repo <absolute>` → `4 of 6` on the same
revision, so the one-line delta clears exactly the two gates that read `../` citations (floors and
checklist) and nothing else. The two corpus-integrity reds and the `instrument-size` guard are separate
defects C3 must own; the one-line delta must not be credited with them. Evidence that `--repo .` is the
only trigger: the self-test's `--repo .` arm resolves to the lane and its parent fleet
root and reads the same verdict as the absolute path.

## 5. M127 end to end at the round base — the red-before/green-after pair

Two runs, each alone on the host (85 s each, under the 300 s cap), same revision `072048f`, differing
only in the `--repo` argument. Output tails pasted as observed:

```
$ python3 -B verifiers/check_tip_battery.py --rev 072048fa8e8a52c707d25f7079772fa317244eb7 --repo .
guard floors PASS
FAIL guard instrument-size: instruments gain 76 lines > 40
guard instrument-pin PASS
guard spotcheck-identity PASS
gate verifiers/check_gate_registry.py exit 0 wall 0.7s
gate verifiers/check_assertion_floors.py exit 1 wall 79.0s
gate verifiers/verify_skill_checklist.py exit 1 wall 2.5s
gate verifiers/verify_corpus_integrity.py exit 1 wall 0.5s
gate verifiers/verify_corpus_independent.py exit 1 wall 0.9s
gate verifiers/check_correction_sweep.py exit 0 wall 0.1s
wall 85.5s
tip battery exit 0: 2 of 6
EXIT=1
```

```
$ python3 -B verifiers/check_tip_battery.py --rev 072048fa8e8a52c707d25f7079772fa317244eb7 \
      --repo /home/vgpnk/Projects/shokunin/kotoba-shokunin
guard floors PASS
FAIL guard instrument-size: instruments gain 76 lines > 40
guard instrument-pin PASS
guard spotcheck-identity PASS
gate verifiers/check_gate_registry.py exit 0 wall 0.7s
gate verifiers/check_assertion_floors.py exit 0 wall 79.9s
gate verifiers/verify_skill_checklist.py exit 0 wall 2.4s
gate verifiers/verify_corpus_integrity.py exit 1 wall 0.3s
gate verifiers/verify_corpus_independent.py exit 1 wall 0.9s
gate verifiers/check_correction_sweep.py exit 0 wall 0.1s
wall 85.3s
tip battery exit 0: 4 of 6
EXIT=1
```

The delta is exactly floors + checklist, the two gates whose checks resolve `../` citations
(`verify_skill_checklist.py` line 558; the floors gate counts the same checklist self-test failures).
`2 of 6` at the round base is reproduced, and it matches the plan's base table
(`floors exit 1 (128 s), checklist exit 1 (4.6 s), corpus integrity exit 1, corpus independent exit 1,
gate registry exit 0, correction sweep exit 0`) — the wall times differ (79.0/2.5 s here vs 128/4.6 s
in the plan's receipt), which is host load, not a rule change. Residual reds at base are *not* the
sandbox cause: `verify_corpus_integrity.py`, `verify_corpus_independent.py` (the r72 spot-check is
unindexed) and the `instrument-size` guard (`instruments gain 76 lines > 40`) stay red under the
absolute path.

Note for the C3 seat: the one-line delta gets the base from `2 of 6` to `4 of 6`, not to `6 of 6`.
Reaching `6 of 6` needs the two integrity reds cleared and the `instrument-size` cap re-set by the
committed addendum the plan promises (Q65) — otherwise a correct repair cannot pass the battery.

## 6. CLI paths (the counter, not the self-test)

```
$ python3 -B check_own_description.py --rev 072048f                # default --repo = the lane
frontmatter lines 19->19 (inserted 0, deleted 0 inside the frontmatter)
own-description rules held 1 of 3
EXIT=1

$ python3 -B check_own_description.py --rev 0000000000000000000000000000000000000000
could-not-evaluate: revision 0000000000000000000000000000000000000000 is not a commit in /home/vgpnk/Projects/shokunin/kotoba-shokunin
EXIT=2

$ python3 -B check_own_description.py --rev 072048f --fleet /tmp/does-not-exist-k73
could-not-evaluate: fleet root not found: /tmp/does-not-exist-k73
EXIT=2

$ python3 -B check_own_description.py --rev 072048f --fleet /home/vgpnk/Projects/shokunin/kotoba-shokunin
could-not-evaluate: fleet root /home/vgpnk/Projects/shokunin/kotoba-shokunin is the lane itself: a sandbox shaped from it is not fleet-shaped (M127)
EXIT=2
```

A short rev prefix resolves to the same measurement, the frozen line is the last line in every
measured case, and no exit-2 path prints a rule line (checked in the self-test too: "an unknown
revision prints no rule line", "a missing gate prints no rule line").

Install shape (script under a `verifiers/` directory, lane passed explicitly — the deployed layout):

```
$ T=$(mktemp -d) && mkdir -p "$T/verifiers" && ln -s <lane>/SKILL.md "$T/SKILL.md" \
    && cp check_own_description.py "$T/verifiers/" && cd "$T" \
    && python3 -B verifiers/check_own_description.py --rev 072048f --repo <lane>
R3 pass: description 1019 <= 1024; verifiers/check_sibling_census.py exit 0
frontmatter lines 19->19 (inserted 0, deleted 0 inside the frontmatter)
own-description rules held 1 of 3
EXIT=1
```

## 7. Risks, deviations, and what the L1 must do

1. **`--fleet` on the census-gate invocation.** R3 runs the tree's own gate from the sandbox clone as
   `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md
   --province PROVINCE.md --skill SKILL.md --fleet <fleet>`. The frozen command as printed has no
   `--fleet`; the counter passes the fleet root it shaped the sandbox from, which for the lane run is
   the gate's own `DEFAULT_FLEET` (`/home/vgpnk/Projects/shokunin`), so the live reading is identical.
   The flag exists so fixture worlds can supply their own census/province/sibling repos without
   reading the live fleet. If a reviewer wants literal fidelity, the alternative is to run with
   `cwd=<sandbox clone>` and no `--fleet`; in the live run the two are the same root, and the
   self-test proves the sandbox parent carries exactly the fleet's sibling lanes.
2. **`--base`.** Defaults to the pinned `072048f…` (the addendum's base) and prints a `note:` line when
   overridden, mirroring `check_tip_battery.py`. The frontmatter-line guard is print-only, so a bad
   base can never change `N`.
3. **`_lane_root()`.** Drafted under `.ufo/waves/round-73/w1/build/ExecDescCounter/`, so the module
   resolves the lane by walking up to the nearest ancestor holding `SKILL.md` and `verifiers/`. Once
   installed at `verifiers/check_own_description.py` the first branch applies
   (`parent.parent` is the lane) and the fallback is dead.
4. **Self-test's live read.** The self-test copies the tracked `verifiers/check_sibling_census.py` into
   each fixture world (read-only), so `R3` runs a real gate over fixture bytes. Two arms assert the
   gate's own failure wording (`does not name the non-none census lane alpha`); if that gate's text
   changes, those two arms fail loudly rather than silently passing.
5. **Not done here, by scope.** Installing the file under `verifiers/` (the L1 owns the commit), the
   freeze-2 commit, the description rewrite claim data, and any C1/C3 counter work. The C3 fix in §4
   is a proposal with its red-before measured, not an applied change: this seat never edits a
   committed lane file.
6. **No tool installs.** Nothing was installed or upgraded for this seat; every command used `git`,
   `python3` and the lane's own scripts.

