# ScoutStaleLane — stale-lane actuator facts, round 69 (kotoba, hyaku run 6, attempt 2)

Seat: scout (depth/recon), no edits outside this file, no subagents.
Observed at: **2026-10-25T07:16:02 → 07:17:20 -03:00** (host clock; all timestamps below are the
files' own `-03:00` local stamps). Read-only git in the lane; every executing check ran in
`/tmp/scout69-c1` (`git clone --shared` of the lane at `a238989`); nothing executed in the lane.

## 1. The earlier-attempt line — EXISTS, exactly one

`grep -n 'lane-dead-no-report kotoba round=69' .ufo/watchdog.log` →
**line 1309** (file: `/home/vgpnk/Projects/shokunin/.ufo/watchdog.log`), one match only:

```
2026-10-25T06:59:59-03:00 lane-dead-no-report kotoba round=69; retry same round (hyaku-inline attempt=1: run-6: L1 died 13m in on Cursor PROVIDER_ERROR (m_flash fallback chain reached cursor/default))
```

Duration check: launch 06:46:36 → dead 06:59:59 = **13m23s**, consistent with the line's "13m in".
The cause is the launcher's own wording; no provider-side evidence exists in the lane repo
(see §7).

## 2. This round's launch lines — BOTH attempts present, no completion line

```
1304:2026-10-25T06:46:36-03:00 launch kotoba round=69 pgid=2607660 driver=hyaku-inline attempt=1
1309:2026-10-25T06:59:59-03:00 lane-dead-no-report kotoba round=69; retry same round (hyaku-inline attempt=1: ...)
1310:2026-10-25T07:00:36-03:00 launch kotoba round=69 pgid=3244947 driver=hyaku-inline attempt=2
```

`grep -c 'complete kotoba round=69'` = **0**: attempt 2 has not completed (correct as of 07:17).
Launcher state (`~/.local/state/shokunin-hyaku/claims/kotoba/`, mtimes 06:46 / 07:00) agrees:

```
round: 69          attempt: 2
base: a5f7459f99bb27bf697e9438362e75ac5833eca8
dispatched: 2026-10-25T07:00:34-03:00   owner: inline   (dir mtime 07:10)
```

`scripts/hyaku/hyaku.env:13` → `MAX_ATTEMPTS=3`: attempt 2 is the second of three; one more
`lane-dead-no-report kotoba round=69` blocks the lane (`$STATE/blocked/kotoba`). Blocked lanes at
07:16: kagi, kaidoku, tsukuroi — kotoba not among them.

Dispatch evidence commits in the fleet repo (prompt = template + addendum, `attempt` substituted):
`ecfb7481` 06:46:34 attempt 1, `7f42a887` 07:00:34 attempt 2; the diff between them is the attempt
number plus a new "Dispatch bridge (run 6)" paragraph and the sentence "A return without a landed
report is a failed attempt — finish the round end to end (run 6: two L1s returned mid-round with
nothing landed)". So the *prompt* attempt 2 received does disclose the earlier attempt
(`lane-addendum.md`: "if `.ufo/watchdog.log` shows a `lane-dead-no-report {{LANE}} round={{ROUND}}`
line … Its uncommitted outputs … are inherited: reuse what you re-verify, discard what you do not,
and name both in the report").

## 3. `pgid=` in a launch line is the driver shell's PID, not a process group

`scripts/hyaku/inline.sh:103`:

```
log "launch $lane round=$n pgid=$$ driver=hyaku-inline attempt=$a"
```

`$$` is the `inline.sh` process ID; the `dispatch` branch prints the prompt path and returns, so the
logged number dies immediately. Measured: `ps -p 3244947` → no such process; no live process has
pgid 3244947 either. **This is not evidence that attempt 2 is dead** — the lane is demonstrably
live (wave-1 registry `.ufo/waves/round-69/w1/swarm-registry.json` created 07:10:56, this seat
dispatched, `recapture/` written 07:11:55, `verifiers/check_r67_routed_repairs.py` touched
07:14:12). Consequence for any seat or closure: do not probe liveness from the `pgid=` field, and
never `kill -- -<pgid>` on it; use the claim state (`attempt`, `dispatched`), the `complete` line,
and mtimes.

## 4. The lane's open L0 lines (`.ufo/l0-questions.md`)

File: 110,935 B, 158 lines, mtime **2026-10-25 04:04:45.767 -03:00** — i.e. last written *before*
kotoba's round-69 launch (06:46:36) and before attempt 2 (07:00:36). Entries carry **no per-line
timestamp**; only the round number. Resolution convention in this file is an inline
`RESOLVED-BY-RULING (…)` prefix (see line 77, tabi r19); **none of kotoba's 11 lines carries one**,
so all are open. `grep -n 'kotoba' | tail -5` →

**line 101** (447 B):
```
kotoba | round-49 | Retire the eight round-1 .ufo/prompts/*-L1.md files? No live dispatcher reads them (scripts/hyaku/inline.sh writes and reads <lane>-round-<N>.md only). Six (kake, kasegi, kengaku, kotoba, kumitate, protocol) carry the report path .ufo/reports/round-1/<lane>.md, so kotoba's verifiers/verify_dispatch_prompts.py fails dispatch.04 on them on every live run. Fleet-owned files; kotoba records the failure and edits nothing there.
```

**line 105** (603 B):
```
kotoba | round-50 | Integrator ruling requested on kotoba's own boundary rule (lane corpus/knowledge/sibling-overlap-census-round49.md, round-50 precedence sections): "contested" = a sibling's scope surfaces claim an element of kotoba's PROVINCE Core over text another fleet lane owns; a claim wins unless the sibling itself states a split assigning that element to someone other than the claimant. Under it kotoba closed the three round-49 open items (kama, kengaku, tameshi stay adjacent) and kept mado and game-dev-3d none. Accept, or rule otherwise? kotoba keeps this as its reading until answered.
```

**line 117** (1,366 B):
```
kotoba | round-55 | Ratify as recorded history or correct the 12 earlier in-place corpus/SOURCES.md protected-cell rewrites plus the already-routed e792607e S050 edit: verifiers/check_sources_append_only.py at f0e5de82 exits 1 with "13 change(s) in 4 of 17 commits" — bfd5a583a S022 teaches (1); 542f51567 S019 scope/anchor/teaches and S022 scope/anchor/teaches (6); bf109cacc S019 teaches, S022 teaches, S026 scope/teaches, S028 teaches (5) — 12 changes in three round-49/50 falsify-correction commits that the round lessons disclose only as cells that "gain anchor, scope and teaches text" with "No other row moved" (round-49.md:50-51, round-50.md:76-78), while round 51 refused the same edit citing contract v1 rule 2 ("forbids editing `teaches` in place", round-51.md:64-67); e792607e's S050 anchor rewrite is the round-53 spot-check's routed defect 3 with correction row S061 on record. CORPUS.md:116 rule 2 permits only status/recheck/used-by in place and requires a correction to be a new row opening "supersedes S0NN —"; the registered gate command is green on its pinned --base 422ffd10 range but the full-history scan is red. Operator ruling: (a) leave all 13 as recorded history (state any terms), or (b) file one correction row per change? Evidence: kotoba-shokunin/.ufo/waves/round-55/build/ScoutL0Sources.md. No lane action is taken until ruled.
```

**line 130** (459 B):
```
kotoba | round-61 | r60 fleet report (.ufo/reports/round-60/kotoba.md) still reads "32 reports, 0 dead" and names neither plans/round-60.md nor considerthese/2026-10-23.md — the closure routed those corrections but the lane write scope covers only its own round report; authorize a fleet erratum append to the r60 report (Option A) or rule the lane LOG+report naming sufficient (Option B). Lane correction rides LOG.md erratum + round-61 report regardless.
```

**line 142** (481 B):
```
kotoba | round-67 | Kimi weekly quota killed 14 of 32 wave-1 seats with `provider.api_error: 429 weekly (7-day) usage limit`; the lane reports a 32–35-seat wave on one provider key is not survivable here. Operator ruling wanted: a per-key seat cap, a second key, or another host-routing remedy. Evidence: .ufo/reports/round-67/kotoba.md, fleet commit 33953ff54fec145181c845b0fd06899c89b98562. The lane did not append this line; the orchestrator is filing it for durability only.
```

Freshness facts about this queue:
- The newest kotoba L0 line is **round-67 (line 142)**. There is **no round-68 or round-69 kotoba
  L0 line** (all 11: 11/13, 40/16, 50/22, 84/47, 85/47, 100/49, 101/49, 105/50, 117/55, 130/61,
  142/67). Round 68 routed nothing to L0; r68's defects live in
  `corpus/lessons/round-68-verifier-spotcheck.md` (C2's scope), not here.
- The file's neighbours at its tail are other lanes' newer entries (kotodama round-69, kagi
  round-28), so its 04:04:45 mtime is a whole-file stamp, not kotoba activity.

## 5. Where the lane's *written* facts are now stale (the actual actuator finding)

### 5a. `plans/round-69.md:17` is false for the attempt that is running

Plan line 17, verbatim:

```
The watchdog log shows no `lane-dead-no-report kotoba round=69` line: no earlier attempt.
```

At read time (07:16) the dead line exists (watchdog:1309). Provenance of the frozen plan:
`git log -1 --format='%h author=%ad committer=%cd'` on `a238989` →
**author=2026-10-25 03:31:26 -0300, committer=2026-10-25 06:57:22 -0300**; `plans/round-69.md`
mtime **06:57:13**; every base/junk control it commits is stamped 06:50–06:56. So the plan was
**committed at 06:57:22 — 2m37s before attempt 1 was declared dead**, and it is attempt 1's own
output (its title line says "attempt 1"; the jj working-copy author date 03:31 is preserved by
`jj commit`, which keeps `@`'s author). Timeline bound exactly: attempt 1's launch line is watchdog
**1304 at 06:46:36** (the 06:56:04 `launch … round=69` on line 1306 is **revenger**, not kotoba —
a neighbour that reads like a kotoba line in a `grep -n 'round=69'` dump and must not be cited as
kotoba's), so the plan was committed **10m46s after** attempt 1 began and **2m37s before** it was
declared dead. Classification: **superseded frozen prose**, not a false observation at freeze — the
sentence was true at 06:57:22 and went stale at 06:59:59; attempt 2 inherits it unamended, and the
correct fix is an erratum/lesson sentence, not a plan edit (the plan is frozen). Mitigation in the
lane's own words, `corpus/lessons/round-69.md`
(lines 9–16, authored "attempt 2"):

```
Attempt 1 died 13 minutes in on a provider error (watchdog
`lane-dead-no-report kotoba round=69`). Its uncommitted outputs were inherited: the frozen plan
commit `a238989a` (claims, three counters, base/junk controls, freeze receipt), the assimilation
scratch under `.ufo/waves/round-69/assimilation/` (append-block, entry draft, validate receipt,
collision files), and the control receipts under `.ufo/waves/round-69/controls/`. They were
re-verified and reused; nothing else from attempt 1 was carried.
```

So: the plan file contradicts the watchdog; the lesson discloses the inheritance correctly. Seats
that cite the plan's "no earlier attempt" sentence as evidence will state a falsehood.

### 5b. The freeze receipt's C1 `--self-test` line is a pre-entry capture (exit 2)

`.ufo/waves/round-69/controls/freeze-receipt.txt` (mtime 06:57):

```
== check_skill_precedence --self-test
selftest setup failed: the entry is not present in the working tree
exit=2
== check_r68_routed_repairs --self-test
self-test: 0 failure(s) over 23 assertions
exit=0
== check_province_core --self-test
self-test: 0 failure(s) over 10 assertions
exit=0
```

This is faithful to 06:57:18 (exact mtime `2026-10-25 06:57:18.028115875`; the C1 entry did not
exist yet; it was written at 07:08:07). **The exit 2 is by design, not a contract violation**:
`verifiers/check_skill_precedence.py:292-300` — `selftest()` begins `if not (repo / ENTRY).is_file():
print("selftest setup failed: …"); return 2`. The docstring's "a MISSING ENTRY is a content verdict
(`0 of 5`, exit 1)" governs the *measurement* path (`check()` under `main()`), which the self-test
itself asserts as a PASS ("missing-entry classification: backed 0 (content verdict)", built from
`_world(repo, drop_entry=True)`) — as a **count, not an exit code**: `selftest()` never drives
`main()`, so the exit-1 arm of that classification is not exercised anywhere (§5c). A peer reading
of the bare `exit=2` as contradicting the
counter's own contract is therefore not supported by the code; what the docstring does lack is a
one-clause carve-out for the `--self-test` fixture gate, which is why it can be misread.

The predicate in the plan (`--self-test` kills one broken world per conjunct) therefore has **no
green receipt anywhere in the round**. Checked independently: `.ufo/waves/round-69/recapture/`
(10 files, mtimes 07:11:55) contains **no `check_skill_precedence.py` receipt at all** — its
`C1-base.txt`, `C1-after.txt`, `C1-fetch.txt`, `C1-selftest.txt` are the **r68**
`check_client_trust_gates.py` receipts (D1's set, measured at `e94ae32` base and `2cf0d99` after;
`C1-selftest.txt` in full: `command: python3 -B verifiers/check_client_trust_gates.py --self-test`,
`measured-rev: 2cf0d99a6d5a3e1cb0b73e3b71cb495fd1eadc6f`, `PASS honest world: backed 5 of 5`, …,
`self-test: 0 failure(s) over 12 assertions`, `exit=0`), and `r67-repairs-base.txt` (07:15) is
D3's. This is a live false-green trap: the filename `recapture/C1-selftest.txt` matches what a
grep for the round-69 C1 self-test receipt would find, and it reports a passing 12-assertion
self-test with `exit=0` — for a different counter at a different revision.

Measured in `/tmp/scout69-c1` (`git clone --shared`, HEAD `a238989`; rows below use the **committed**
counter, md5 `00bd800a…` — the live counter's figure is the 07:22 note above):

| sandbox state | command | result |
|---|---|---|
| clean clone (no entry) | `check_skill_precedence.py --self-test` | `selftest setup failed: the entry is not present in the working tree`, **exit 2** (designed) |
| entry + lane's working-tree `corpus/SOURCES.md` + `corpus/README.md` copied in | same | `self-test: 0 failure(s) over 18 assertions`, **exit 0** |
| entry only (rows/index absent) | same | **uncaught `KeyError: 'S203'` at `verifiers/check_skill_precedence.py:315` (`row = rows[first]`), exit 1** |

Findings for the C1 seats: (i) capture the round-69 C1 self-test **post-entry** into `recapture/`
under a name that cannot be confused with `check_client_trust_gates`'s `C1-*` receipts (the plan's
D1 list already reuses `C1-*` for the r68 counter), and cite that, not the freeze receipt;
(ii) the self-test cannot be run from the committed tip until the entry is committed — a reviewer
cloning the lane at `a238989` and running `--self-test` gets exit 2 and must not read that as a
counter defect; (iii) an entry-without-registry state (reachable while the round writes
07:08:07 → 07:08:11, and by any partial-state harness) raises rather than classifying — a
robustness fact, low severity, worth a line in the mistake candidates. **Detected 07:22:** the live
working-tree counter (md5 `57db6f8e5b37fd6b48b92c2dc683dac9`; committed bytes are
`00bd800acc5dc7a991d14df11675841d`) already fixes exactly this — `rows.get(first)` plus a
`row_line is None` guard now print `selftest setup failed: the first cited id has no registry row in
the working tree` and `return 2`. So (iii) holds for the committed tip only; the lane repaired it
inside the round.

### 5c. The lesson changed mid-round (07:17:50) and its new paragraph carries two defects

`corpus/lessons/round-69.md` was rewritten **while seats were reading it**: mtime
`2026-10-25 07:17:50.679103452` (= 10:17:50Z), md5 **`dbd377427e74f55394f2d8a92bf959d3`**, 9,234 B —
34 s after this report's first write, and the region quoted in §5a (lines 9–16) is unchanged. New
lines 17–24:

```
**Freeze receipt explanation (checks the entry-absent exit 2).** The freeze receipt
(`.ufo/waves/round-69/controls/freeze-receipt.txt`) records `check_skill_precedence --self-test`
exit 2 (`selftest setup failed: the entry is not present in the working tree`) at freeze time.
That is a setup artifact, not a defect verdict: the counter's `--self-test` builds its honest world
from the working-tree entry (QUALITY Q48), which only exists after C1's content lands. The content
verdict for a missing entry is the measurement path (`--rev` → `0 of 5`, exit 1), which the base
control exercises. At the committed round-69 tip, with the entry present, `--self-test` exits 0
(18 assertions).
```

- **Line 23 is false as written.** The committed tip `a238989` does not carry the entry (it is
  untracked), so a clean checkout of that tip has no entry and exits 2 — re-measured 07:22 in
  `/tmp/scout69-c1` after `git checkout -- corpus/SOURCES.md corpus/README.md && rm entry`:
  `selftest setup failed: the entry is not present in the working tree`, **exit 2**, clean
  `git status`. Exit 0 (18 assertions) is a *working-tree* state — tip + the uncommitted entry
  overlaid. "At the committed round-69 tip, with the entry present" describes a state that cannot
  be materialized from the tip alone: the same working-tree-vs-committed conflation as R68-7, now
  inside the lesson that will be committed. Correct phrasing: "with the working-tree entry overlaid
  on the tip (not a committed state)". **The assertion count is stale too:** at 07:22 the live
  counter (md5 `57db6f8e…`, see §5b) reports `self-test: 0 failure(s) over 22 assertions`, exit 0,
  measured in the sandbox with the live counter + live entry + `SOURCES.md` + `README.md` — the
  lesson's "18 assertions" was true only for the counter bytes of ~07:08–07:17.
- **Line 21's `(QUALITY Q48)` mis-cites the criterion.** `corpus/QUALITY.md:59` defines Q48 as: a
  counter's self-test **drives its public `main()`** on a satisfying fixture and asserts **exit 0
  with the exact printed line**, beside one **broken-conjunct world asserting exit 1**; "helper-only
  checks and failure-only calls do not cover the measurement path". `check_skill_precedence.py`'s
  `selftest()` calls the `check()` helper and counts (`n != TOTAL`, then
  `return 1 if failures else 0` at line 369); the only `main()` call is
  `sys.exit(main())` under `__main__` (line 408). So the citation is wrong *and*, read properly,
  the r69 self-test **does not satisfy Q48** — the exit-0/exit-1 arms through `main()` are absent,
  which is exactly why the docstring's classification (missing entry → exit 1) is never exercised
  as an exit code. That is a consistency fact C1/C2 reviewers should score, not a documentation nit.
  The exit-1 side is evidenced elsewhere and should be cited there: `controls/C1-base.txt` at
  `a5f7459` — `skill precedence backed 0 of 5` / `- entry missing:
  corpus/knowledge/skill-name-precedence-round69.md` / `exit=1` — not by the self-test.
  **Holds live at 07:22:** the edited counter still has no `main()`-driving arm (only
  `def main` at 404 and `sys.exit(main())` at 443) and its 22 arms still assert counts, so Q48 is
  unsatisfied by both the committed and the live bytes.

### 5d. The plan's inherited-state census is short by 18 paths

Plan: "`git status --porcelain` lists 24 lane-authored round-68 wave paths". Current census
(07:16, `git status --porcelain | wc -l` = **42**):

- 24 `.ufo/waves/round-68/…` — matches the plan (C2/D7's set).
- 9 `.ufo/waves/round-69/…` untracked — `assimilation/append-block.md` (06:58:20),
  `assimilation/entry-draft.md` (06:58:33), `assimilation/validate/` (06:59:09),
  `assimilation/validate-census.txt` (06:59:09) — attempt 1; `w1-spec.json` (07:10:54),
  `w1-dispatch.err` (07:10:56, empty), `w1-dispatch.json` (07:10:56), `w1/` (07:10:56, holds only
  `swarm-registry.json`), `recapture/` (07:11:55) — attempt 2.
- 9 content/tool paths, all written after the plan was frozen: `corpus/knowledge/skill-name-precedence-round69.md`
  (07:08:07), `corpus/SOURCES.md` (07:08:11), `corpus/README.md` (07:08:15), `PROVINCE.md`
  (07:08:19), `SKILL.md` (07:08:32), `corpus/knowledge/client-trust-gates-round68.md` (07:08:40),
  `corpus/QUALITY.md` (07:08:42), `corpus/lessons/round-69.md` (07:08:50),
  `verifiers/check_r67_routed_repairs.py` (07:14:12).

Consequence for C2: the plan's "before" receipts were captured on a tree that no longer exists.
`C2-base-integrity.txt` (06:50, `verify_corpus_integrity.py`, exit 1, DRIFT `tracked_files
125≠124`, `unindexed 1`, `report_total 87≠85`) reads the **working tree**, and between 06:50 and
07:14 the tree gained the nine content paths above plus one modified verifier — any seat re-running
that command now is measuring a different world than the receipt. `C2-base.txt` (06:56) and
`C3-base.txt` / `C1-base.txt` (06:56) are `--rev a5f7459f…` measurements and are unaffected by
working-tree drift, which is the right shape; the integrity receipt is not.

### 5e. The claim instruments diverged from the freeze receipt (07:21:28, 07:22:44)

Measured 07:24–07:26 with `sha256sum` + `stat` against `controls/freeze-receipt.txt`:

| counter | receipt sha256 | live sha256 | live mtime | live `--self-test` |
|---|---|---|---|---|
| `verifiers/check_skill_precedence.py` | `9c796574…da48` | **`dc9f1507…c246`** | 07:21:28.354 | 22 assertions, exit 0 |
| `verifiers/check_r68_routed_repairs.py` | `3202549…dcf2` | **`9cf97497…8279`** | 07:22:44.685 | 25 assertions, exit 0 |
| `verifiers/check_province_core.py` | `c85f9d75…6c5a` | `c85f9d75…6c5a` (unchanged) | 06:56:05.645 | 10 assertions, exit 0 |

`git show a238989:verifiers/<each> | sha256sum` reproduces both receipt hashes exactly, so the
receipt is **still true of the committed tip** — the divergence is working-tree only, and the
receipt has become a description of bytes the lane is no longer shipping. The plan's own sentence
("Counter semantics (frozen with this plan; sha256 recorded in the plan commit's receipt)") is
therefore stale from 07:21:28 as of 07:24, with no re-freeze artifact anywhere in
`.ufo/waves/round-69/`. Practical consequences: cite the receipt only as *frozen bytes at
`a238989`*; a receipt that cites it for the live counters fails QUALITY Q24 ("a receipt's recorded
instrument hash is checked against the committed instrument bytes before the receipt is cited");
and the round's final claim measurement will run whichever counter is committed at the tip, so the
frozen semantics text and the judging instrument have to be reconciled before the gate.

**Controls cannot be re-measured.** The cheapest controls' `measured-rev:` values are sandbox-only
commits that do not exist in the lane object database — `git cat-file -e` → **ABSENT** for
`95651d4d…` (C1 junk control), `bf69a719…` (C2 cheap control), `00b5ddea…` (C3 cheap control);
only the r68-era revisions (`e94ae32`, `2cf0d99`) are present. So no later seat or closure can
re-open the junk/cheap controls: their receipts are assertions, not reproducible measurements, and
a re-capture on lane-present revisions is required before those controls can be cited again.

**A live constant with no receipt.** The C2 counter edit adds `R68_INS, R68_DEL = 4081, 251` and
fails D7 when the `--numstat` diff over the 24 r68 paths differs from it. That pair was measured
during the edit; nothing in `controls/` records the command or the revision it was taken at, so any
later content change under those paths silently flips D7.

## 6. Current-currency summary a seat can cite

- Round: kotoba 69, **attempt 2 of ≤3**; launched **2026-10-25T07:00:36-03:00**; attempt 1 launched
  06:46:36 and was declared dead 06:59:59 on a provider error; no completion line yet.
- Lane tip at read: **`a238989a96cb0d2b939679126b832d75b861ca6e`** ("round-69: frozen plan, three
  counters …"), a single-parent child of the plan's declared base
  **`a5f7459f99bb27bf697e9438362e75ac5833eca8`** (`git merge-base --is-ancestor` = yes; `a5f7459..HEAD`
  is exactly that one commit). The plan's base statement is accurate; a reader who runs
  `git rev-parse HEAD` and expects `a5f7459` is reading the parent, not the base.
- Content draft landed on attempt 2's clock: entry 07:08:07, SOURCES/README/PROVINCE/SKILL/QUALITY
  07:08:11–07:08:42, lesson 07:08:50, verifier edit 07:14:12.
- Wave 1: registry `createdAt`/`updatedAt` `2026-10-25T10:10:56.516Z` (= 07:10:56 -03:00).
- L0: five tail lines quoted above (rounds 49, 50, 55, 61, 67), all open, none appended this round.
- Fleet report `.ufo/reports/round-69/kotoba.md`: **absent** (dir holds audio.md, game-dev-2d.md,
  kotodama.md only) — the round is in flight.
- **The working tree is moving under the seats.** Between 07:16 and 07:26: `git status` went 42 →
  44 collapsed paths (`-uall` shows 10+ files under `w1/`), `corpus/lessons/round-69.md` changed
  (md5 `dbd37742…`), and two of the three counters moved off the freeze receipt — C1
  `9c796574…`→`dc9f1507…` at 07:21:28, C2 `3202549…`→`9cf97497…` at 07:22:44 (§5e). Any receipt a
  seat writes must name the **revision and the file sha256/md5** it measured; "the working tree" is
  not a measurement target this round. My sandbox results in §5b are pinned to committed `a238989`
  (counter md5 `00bd800a…`) except where marked live.

## 7. Unknowns (not resolvable from lane or fleet bytes)

- The watchdog's PROVIDER_ERROR attribution ("m_flash fallback chain reached cursor/default") is
  the driver's claim; no provider log, retry trace, or seat log from attempt 1 survives in the lane
  (`.ufo/waves/round-69/` holds attempt-1 controls/assimilation/receipt only — no `logs/`).
- Whether attempt 1's assembly draft was "re-verified" (lesson's word) is not independently
  checkable: no attempt-1 transcript exists in the fleet or the lane. Only the byte-identity of the
  inherited files (they are the ones the plan commit carries) is verifiable.
- Why `a238989`'s author date (03:31:26) precedes its committer date by 3h25m56s: consistent with
  `jj commit` preserving `@`'s author and `jj-lane.sh` stamping only the committer
  (`jj-lane.sh:694-698` `metaedit --update-author` on the working copy), but the 03:31:26 working-copy
  change itself is not visible in lane git history (single commit touches `plans/round-69.md`), so
  "authored at 03:31, finalized at 06:57" is inference from the two dates, not an observed event.

## 8. Peer corroboration and corrections (RevFreezeReceipt, IRC, ~07:20)

Peer `RevFreezeReceipt` independently corroborated the sandbox result in its own `/tmp` shared clone
at `a238989` (clean → exit 2; entry + worktree `SOURCES.md`/`README.md` → 18 assertions, exit 0,
also against the current draft bytes), and confirmed receipt mtime 06:57:18 vs entry 07:08:07. I
re-verified both against bytes, not the claim:

- **Accepted — no round-69 C1 receipt exists at all.** `recapture/` holds 10 files, none invoking
  `check_skill_precedence.py`; `C1-*.txt` are the r68 `check_client_trust_gates.py` receipts
  (`e94ae32` base, `2cf0d99` after) and `r67-repairs-base.txt` (07:15) is D3's. Strengthened in
  §5b, with the false-green hazard named (a grep for `C1-selftest` returns the r68 counter's
  `PASS honest world: backed 5 of 5`).
- **Accepted with correction — "superseded frozen prose" is the right classification**, and the fix
  belongs in the lesson/erratum, not a plan edit. But the peer's timeline cites "attempt-1 launch
  line 06:56:04": that is watchdog **1306, `launch revenger round=69`**. Kotoba's attempt-1 launch is
  **1304 at 06:46:36**. Corrected durations: plan committed **10m46s after** attempt 1 began,
  **2m37s before** the death line (06:59:59). §5a updated.
- **Rejected — the bare `exit=2` does not read against the counter's own contract.**
  `check_skill_precedence.py:292-300`: `selftest()` returns 2 explicitly when the entry fixture is
  absent, and the docstring's missing-entry-exit-1 classification is implemented on the measurement
  path (`check()`), and the self-test asserts that world's **count** is 0 (not its exit code — see
  §5c). The peer's reading came from the classification paragraph lacking a
  `--self-test` carve-out; that docstring gap is real and named in §5b, but it is a documentation
  fact, not a code-vs-contract violation, and must not be routed as a counter defect.

Second IRC message (RevFreezeReceipt, received ~07:21) reported the lesson rewrite. Verified by
bytes at ~07:22:

- **Accepted — the lesson changed mid-round.** `corpus/lessons/round-69.md` mtime
  `2026-10-25 07:17:50.679103452` (= **10:17:50Z**, not 10:21Z — that is when the peer re-read it),
  md5 `dbd377427e74f55394f2d8a92bf959d3`, 9,234 B; new lines 17–24; §5a's quoted region unchanged.
  The paragraph's explanation of the exit 2 as a setup artifact agrees with §5b.
- **Accepted — line 23's exit-0 claim is a working-tree-vs-committed conflation.** Re-measured at
  07:22 in `/tmp/scout69-c1` with the tree restored to a clean `a238989` checkout: exit **2**, clean
  `git status`. Exit 0 requires the uncommitted entry overlaid, i.e. not the committed tip. Named in
  §5c with corrected phrasing.
- **Accepted — `(QUALITY Q48)` mis-cites.** `corpus/QUALITY.md:59`: Q48 requires the self-test to
  drive public `main()` on a satisfying fixture asserting exit 0 with the exact printed line, plus
  a broken-conjunct world asserting exit 1. `selftest()` calls `check()` only
  (`return 1 if failures else 0`, line 369); the sole `main()` call is `sys.exit(main())` at line
  408. So the citation is wrong and the r69 self-test does not satisfy Q48 — recorded in §5c as a
  consistency fact, not a docstring nit.
- **Convergence recorded.** The peer's final filing matches this report's split: its F2b is LOW
  doc-clarity (a `--self-test` carve-out sentence; no route against the counter, consistent with my
  rejection above), its F3 is the Q48 mis-citation above, and its evidence-substitution finding is
  §5b's false-green trap. Its remaining correction to me — that the missing-entry self-test arm
  asserts `n == 0` from `check()` and never an exit code on either path, so `exit=1` is evidenced by
  `controls/C1-base.txt` and not by the self-test — is right and is now stated that way in §5b/§5c.

Third IRC message (RevFreezeReceipt, received ~07:24) — instrument divergence. Verified by
`sha256sum`/`stat` at 07:24–07:26:

- **Confirmed exactly.** C1 counter `dc9f1507…` mtime 07:21:28; C2 counter `9cf97497…` mtime
  07:22:44; province counter still `c85f9d75…` (§5e table). Live self-tests reproduce their numbers:
  C1 22 assertions / exit 0, C2 25 / exit 0, C3 10 / exit 0.
- **Q24 framing refined.** The freeze receipt is *not* invalid: `git show a238989:verifiers/… |
  sha256sum` reproduces `9c796574…` and `3202549…` byte-exactly, so it remains a true receipt of the
  committed instruments. What broke is that the lane is no longer shipping those bytes. Cite it as
  "frozen at `a238989`", and the cure is the peer's own: re-freeze (new sha256 lines + findings note
  + re-captured controls) or commit the frozen bytes and carry the strengthening to round 70.
- **New fact beyond F5.** The three cheapest controls cite revisions absent from the lane object
  database (`git cat-file -e` → ABSENT: `95651d4d…`, `bf69a719…`, `00b5ddea…`), so they cannot be
  re-measured at all; a re-freeze must re-capture them on lane-present revisions, not just re-hash
  the counters.
- **Unverifiable.** The intermediate copies (`fdafd542…` NameError, `5be7f1e1…` 6-of-8) are gone
  with the editing process; only the settled 25-assertion result is checkable, and it is green.
- **Adjacent, same section.** The live C2 counter hard-codes `R68_INS, R68_DEL = 4081, 251` with no
  receipt line (§5e); that pair should be re-derived against a named revision before it gates D7.
