# RevRa — R-a count-correction audit vs r60 closure defect 3 (kotoba round 61, wave seat)

Seat: kotoba-r61-wave-RevRa · Date: 2026-10-23 · Base: `f3246d1493b60ea1c0d947a19c39f9e08e92f326` ·
Scope: audit repair R-a against the exact defect-3 wording in `corpus/lessons/round-60-verifier-spotcheck.md` §7,
verify the committed count NOW, and check the correction's placement. Read-only elsewhere; no installs; no pacman.

---

## 1. The two requested count commands, pasted

### 1a. `git ls-tree` at the r60 build/close commit `79cf2638` — pasted in full

Command (run 2026-10-23, cwd `/home/vgpnk/Projects/shokunin/kotoba-shokunin`):

```
git ls-tree -r --name-only 79cf263800552812ce6a45f4bb0313668b576749 -- .ufo/waves/round-60/build/
```

Output (33 entries, exit 0):

```
.ufo/waves/round-60/build/ConnSiblingContradict.md
.ufo/waves/round-60/build/CriticAxisFit.md
.ufo/waves/round-60/build/CriticCensus.md
.ufo/waves/round-60/build/CriticKeyRule.md
.ufo/waves/round-60/build/CriticNegativeRows.md
.ufo/waves/round-60/build/ExecIndexCorpus.md
.ufo/waves/round-60/build/ExecIndexCorpus.patch
.ufo/waves/round-60/build/ExecKeyForms.md
.ufo/waves/round-60/build/ExecNoHarmBase.md
.ufo/waves/round-60/build/ExecWordCountCheck.md
.ufo/waves/round-60/build/MutC1Counter.md
.ufo/waves/round-60/build/ReviewC1Counter.md
.ufo/waves/round-60/build/ReviewPlanChronology.md
.ufo/waves/round-60/build/ReviewR1Correction.md
.ufo/waves/round-60/build/ScoutUnscopedDefault.md
.ufo/waves/round-60/build/ScribeEntry.md
.ufo/waves/round-60/build/ScribeFrontier.md
.ufo/waves/round-60/build/ScribeMistakes.md
.ufo/waves/round-60/build/ScribeQuality.md
.ufo/waves/round-60/build/ScribeR4S096.md
.ufo/waves/round-60/build/ScribeR4S097.md
.ufo/waves/round-60/build/ScribeSkillSection.md
.ufo/waves/round-60/build/SentinelContexts.md
.ufo/waves/round-60/build/SrcClaudeCode.md
.ufo/waves/round-60/build/SrcCodex.md
.ufo/waves/round-60/build/SrcCopilotCLI.md
.ufo/waves/round-60/build/SrcCursor.md
.ufo/waves/round-60/build/SrcGeminiCLI.md
.ufo/waves/round-60/build/SrcVSCode.md
.ufo/waves/round-60/build/Srcopencode.md
.ufo/waves/round-60/build/check_word_counts.fixture.md
.ufo/waves/round-60/build/check_word_counts.py
.ufo/waves/round-60/build/swarm-registry.json
```

Count: 33 entries total; 30 `.md`; **29 seat reports** after excluding `check_word_counts.fixture.md`
(a checker fixture, not a seat report). Per-prefix census: Conn 1 + Critic 4 + Exec 4 + Mut 1 +
Review 3 + Scout 1 + Scribe 7 + Sentinel 1 + Src 7 = 29. The three defect-3 absentees
(`ExecBudgetMove`, `ExecGateRegistry`, `ExecShonenPointer`) are absent at both r60 commits
(verified: neither appears in `git ls-tree` at `7b80ae80` or `79cf2638`).

Note on "the r60 build commit": the build reports landed across two commits —
`7b80ae80cda69a95b6fc90879395113a99a57912` (C1 data, 2026-10-23 09:28 -03) has 31 entries /
28 `.md`, all seat reports = 28; the 29th (`ExecWordCountCheck.md`, an attempt-1 leftover) and
the fixture landed only at the close commit `79cf263800552812ce6a45f4bb0313668b576749`
(2026-10-23 15:04 -03), where the seat-report count is 29. The "committed 29" figure is the
count at the r60 close tip, not at the data commit.

### 1b. `ls …*.md | wc -l` at the current tip — pasted

```
$ ls .ufo/waves/round-60/build/*.md | wc -l
30
```
(2026-10-23 07:09:17 UTC; exit 0.) The raw glob yields **30**, not 29 — it includes
`check_word_counts.fixture.md`. Counting-command sweep, same timestamp, all exit 0:

| command | result |
|---|---|
| `ls .ufo/waves/round-60/build \| wc -l` | 33 |
| `ls .ufo/waves/round-60/build/*.md \| wc -l` | 30 |
| `ls .ufo/waves/round-60/build \| grep -cE '^(Conn\|Critic\|Exec\|Mut\|Review\|Scout\|Scribe\|Sentinel\|Src)[A-Za-z0-9]+\.md$'` | **29** |
| `ls .ufo/waves/round-60/build/*.md \| grep -vc check_word_counts.fixture` | **29** |

**Verdict: 29 is the true committed seat-report count NOW.** The build directory is
byte-identical from `79cf2638` to the round-61 freeze tip `7827628a939b0333c89892dfcedc72e390ccfb60`
(`git diff --stat 79cf2638 7827628a -- .ufo/waves/round-60/build/` is empty, exit 0), so nothing
landed this round changed it. But both naive commands overcount (33 / 30): any R-a correction
line that names one of them as "the counting command" will not reproduce the corrected count.

## 2. Defect 3 exact wording (round-60-verifier-spotcheck.md §7, item 3)

> "**Seat-report count (Medium).** Report says build wave "32 reports, 0 dead"; only 29 build
> reports are committed (ExecBudgetMove, ExecGateRegistry, ExecShonenPointer absent) — 59/65
> seat reports committed overall. The 65-seat dispatch total is arithmetically consistent with
> the committed call files and LOG.md; the report should not claim committed reports it cannot
> cite."

Routing (§8): "reconcile "reports, 0 dead" claims against committed report counts".
Plan C2 freezes R-a as: "LOG.md carries the corrected build-report count (claimed 32 vs
committed 29) with its counting command". My assignment adds the placement requirement: the
correction must live where a reader of the r60 report will find it (LOG.md round-61 entry +
round-61 report).

## 3. Findings by severity

### F1 — Medium (predicate trap): the checker's canonical R-a line names a counting command that yields 33, not 29
`verifiers/check_routed_repairs.py` self-test fixture `full_log` (lines 162–166) is the only
in-repo example of a conforming R-a line, and it cites
`` `ls .ufo/waves/round-60/build | wc -l` `` — which prints **33** (it counts
`ExecIndexCorpus.patch`, `check_word_counts.py`, `check_word_counts.fixture.md`,
`swarm-registry.json`). If the integrated LOG.md entry copies the exemplar, the landed
"correction" cites a command that provably does not produce the corrected count — the exact
failure mode defect 3 routed ("the report should not claim committed reports it cannot cite"),
now one level down. The counter cannot catch this: it never executes the named command. The
self-test arm `ra-without-command` (expects 5 of 6) tests only that the path substring
`.ufo/waves/round-60/build` disappears when the command is removed — not that the command is
correct. Evidence: §1 sweep row 1 (33).

### F2 — Medium (predicate weaker than the plan, and the second placement is unguarded)
- (a) Plan C2 says the count lands "with its counting command"; the frozen code
  (check_routed_repairs.py:69–73) requires only the substrings `build reports`, `claimed 32`,
  `committed 29`, and the counting **path** `.ufo/waves/round-60/build` anywhere in LOG.md. A
  line naming the path with no command at all passes R-a.
- (b) Placement: the assignment (and defect-3 discoverability) requires the correction in the
  LOG.md round-61 entry **and** the round-61 report. The checker reads only lane `LOG.md`
  (`LANE = Path(__file__).resolve().parent.parent`; `git show <rev>:LOG.md`). Nothing committed
  checks the fleet-side round-61 report (`/home/vgpnk/Projects/shokunin/.ufo/reports/round-61/kotoba.md`
  does not exist yet as of 2026-10-23; the dir already holds sibling lanes' `game-dev-2d.md`,
  `kotodama.md`, `revenger.md`). The r60 report itself is fleet-side (commit `93db1a8`,
  fleet repo), so a reader starts in a different repo than the one the checker guards — the
  round-61 report prong rides on reviewer diligence only.

### F3 — Low (docstring/code mismatch): "on one line" is not enforced for R-a
Docstring: "LOG.md holds the corrected round-60 build-report count **on one line**". Code:
whole-blob substring checks (`ra = "build reports" in log and …`) — unlike R-c, which does
per-line matching (`any(... for line in log.splitlines())`). A multi-line scatter of the four
substrings passes while violating the written contract.

### F4 — Low (count nuance the correction should state): "committed 29" is revision-anchored
At the C1-data commit `7b80ae80` only 28 seat reports existed; 29 holds from the close commit
`79cf2638` onward. A correction line that says "committed 29" without naming the revision
invites a reader to re-run at `7b80ae80` and get 28. Name the revision (or "at close
`79cf2638`, unchanged through tip") next to the command.

### F5 — verified-fact note (no defect): the r60 claim sentence and its arithmetic
The overstatement is real and located: fleet `.ufo/reports/round-60/kotoba.md` line 65
(commit `93db1a8`): "build wave — one validated v1 wave, 32 seats (scribe 14, executor 7,
critic 4, reviewer 3, scout 1, mutation-tester 1, sentinel 1, connector 1), 32 reports,
0 dead". The arithmetic closes exactly against committed bytes: claimed "scribe 14" =
7 `Scribe*` + 7 `Src*` committed; claimed executor 7 − 4 committed = the 3 named absentees;
32 claimed − 3 = 29. Overall 59/65 also reconciles: 29 build + 10 w0 + 3 w0b + 6 controls
(7 .md incl. SUMMARY.md) + 3 controls-v2 (4 .md incl. SUMMARY.md) + 8 residual = 59 committed
seat-report `.md` vs 65 dispatched (32 + 11 + 3 + 8 v1 controls incl. 2 cancelled + 3 v2 + 8).
Defect 3's numbers are honest; only the placement and the counting command need care.

## 4. What passes cleanly (checker behavior reproduced live)

- `python3 -B verifiers/check_routed_repairs.py --self-test` → `self-test: 0 failure(s)`, exit 0
  (2026-10-23 07:14 UTC).
- `python3 -B verifiers/check_routed_repairs.py --rev f3246d1493b60ea1c0d947a19c39f9e08e92f326`
  → `routed repairs verified 0 of 6`, exit 1 — matches the committed control receipt
  `.ufo/waves/round-61/controls/C2-base.txt` line for line (`R-a count correction: missing` …
  `0 of 6`, `base-exit=1`).
- LOG.md at tip (`7827628a`): zero round-61 mentions, zero `claimed 32` / `committed 29` — R-a
  not yet landed, as expected pre-integration (integration rides the L1).

## 5. Recommendation to the L1 (concrete, survives this audit)

Land the round-61 LOG.md entry correction as ONE physical line that (i) contains the four
checker substrings, (ii) names a command that actually prints 29, and (iii) anchors the
revision — e.g. (verified: prints 29, exit 0, 2026-10-23 07:14:17 UTC):

```
round-60 build reports: claimed 32, committed 29 — counted at 79cf2638 (unchanged through tip) with `ls .ufo/waves/round-60/build | grep -cE '^(Conn|Critic|Exec|Mut|Review|Scout|Scribe|Sentinel|Src)[A-Za-z0-9]+\.md$'` (=29; plain `ls | wc -l` gives 33 and `ls *.md | wc -l` gives 30 because check_word_counts.fixture.md, check_word_counts.py, ExecIndexCorpus.patch and swarm-registry.json are not seat reports); absent: ExecBudgetMove, ExecGateRegistry, ExecShonenPointer.
```

Do NOT copy the self-test exemplar `` `ls .ufo/waves/round-60/build | wc -l` `` (yields 33).
Mirror the correction in the fleet round-61 report (`.ufo/reports/round-61/kotoba.md`) when it
is written — no committed check covers that prong.

## 6. Residual risk and verification gaps

- The round-61 report does not exist yet, so the "reader of the r60 report finds the correction
  there" prong is unverifiable today — pending L1 integration; only the LOG.md prong is
  checker-guarded at all (F2b).
- Whether the L1's eventual LOG.md line names a correct command is unknowable pre-integration;
  F1 is a trap warning, not a landed defect.
- The checker intentionally does not judge substantive honesty (docstring, Q31); command
  correctness is reviewer-owned — this file is that review for R-a.
- I verified the count and checker over committed bytes and the working tree only; I did not
  execute any gate owned by another seat, mutate git/jj, or dispatch.

---

Installs: no installs. Blockers: none. Attacked/produced: audited R-a against r60 closure
defect 3 — proved 29 is the true committed seat-report count (33/30/29 command sweep, pasted),
and found the frozen checker's own exemplar counting command yields 33 plus two
predicate-strength gaps and one doc/code mismatch.
