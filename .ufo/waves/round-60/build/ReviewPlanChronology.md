Result: MIXED — controls/data ordering and counter byte-identity are clean (three YES answers), but the final formula was fixed after five census reports existed, and the superseded A1 plan version carried a clock stamp 2m18s after its own commit (R3 defect, corrected at the freeze).

Reviewed at tip `49f7ff22a3c93a80d649611e9f6e4b8a4b43af35` (2026-10-23T12:16:29Z `date -u`), lane /home/vgpnk/Projects/shokunin/kotoba-shokunin, read-only (`git --no-optional-locks` only). All lane commits below carry offset -03:00; Z equivalents given where they matter. No tools installed (tooling directive: record — none needed).

## Anchor commits

```
$ git --no-optional-locks log --format='%H %cI %s' -n 5
49f7ff22a3c93a80d649611e9f6e4b8a4b43af35 2026-10-23T09:11:51-03:00 round-60: erratum E2 — C1 declared exploratory before data (two v2 controls met the predicate by forged provenance)
f9f12681e53a8ca48d28837b9d12fb9fac4cd1a5 2026-10-23T09:08:41-03:00 round-60: v1 control summary (6 receipts NOT MET, 2 cancelled at deadline)
56a611d6675662ce389338118c1df87e58437647 2026-10-23T09:05:07-03:00 round-60: freeze-2 sandbox receipt, CtlNoReader v1 receipt, controls-v2 call
b1cd64bb45eee744c4ec93be8631f1eddb28fddd 2026-10-23T08:06:46-03:00 round-60: erratum E1 before data — counter v2 (re-open of held rows; sha ca2585a4), re-census w0b, v1 control receipts
49c3e87d4fb5677783c55f8225c9e4f892273879 2026-10-23T07:44:07-03:00 round-60: C1 freeze (census F_max 4, T_F 3; counter check_scoped_rules.py sha 6aea3be0)
bfe8cc2b26503aba1dd7cb9eabb4316dc0f13584 2026-10-23T07:33:42-03:00 round-60: plan draft amendment A1 (scope-key and action conjuncts tightened before freeze; CensusCursor wrong-key finding)
b8b2a7a271fa2dab7b679c7f3968a9e4705a1397 2026-10-23T07:28:00-03:00 round-60: plan draft (C1 scoped rule files; semantic conjuncts; target TBD)
```

Author vs committer (`git show -s --format='%H%n author %aI%n committer %cI'`): identical except b8b2a7a2 (author 07:22:51-03, committer 07:28:00-03) and b1cd64bb (author 08:06:43, committer 08:06:46). No author-after-committer skew.

## Q1 — Was the formula fixed before any census report existed?

**Partially. Draft formula: YES. Final (A1) formula: NO.**

- The draft `b8b2a7a2` (committed 10:28:00Z) already fixes the scoring formula. From `git show b8b2a7a2:plans/round-60.md`:
  - line 6: "(this text: row rule, semantic conjuncts and target formula fixed, C1 target `TBD`) before any census seat returns"
  - line 32: "**Semantic conjuncts (the point of this round).**", line 35 Scope key cell, line 42 Action cell, lines 65–66/73 the found/backed predicate.
- Census artifacts (birth times from `stat -c '%n | mtime=%y | btime=%w' .ufo/waves/round-60/w0/*.md`, btrfs birth time):
  - ConnSiblingScoped.md btime 10:31:25Z, CensusClaudeCode.md 10:31:31Z, CensusVSCode.md 10:32:46Z, CensusCursor.md 10:32:48Z, CensusCopilotCLI.md 10:32:51Z, CensusCodex.md 10:33:13Z (mtime 10:33:27Z), CensusGeminiCLI.md 10:33:15Z, Censusopencode.md 10:34:12Z; ExecR1Recount.md btime 10:31:22Z.
  - All eight census reports + 2 companion reports postdate the draft commit (10:28:00Z) by 3–6 min → the drafted formula predates every census report.
- But amendment A1 `bfe8cc2b` (committed 10:33:42Z) tightened the conjuncts (`git diff b8b2a7a2 bfe8cc2b -- plans/round-60.md` → "21 insertions"), AFTER five census reports existed (VSCode 10:32:46Z, Cursor 10:32:48Z, Copilot 10:32:51Z, Codex 10:33:13Z, Gemini 10:33:15Z), and its added text cites `.ufo/waves/round-60/w0/CensusCursor.md:94-108`. So the frozen formula's final shape was fixed in response to census output — by design a pre-freeze/pre-control/pre-data amendment, but not "before any census report existed".

## Q2 — Was A1 committed before any control scored and before any C1 data?

**YES to both.**

- Controls: A1 committed 10:33:42Z. Earliest control artifact is the dispatch record `.ufo/waves/round-60/controls-call.json` (btime 10:45:19Z), first scored control report `controls/CtlDoNothing.md` (btime 10:50:43Z, mtime 10:50:50Z). All control artifacts postdate A1: CtlDoNothing 10:50:43Z, CtlJunk 10:51:29Z, CtlAllFalse 10:51:34Z, CtlLabelShortcut 10:52:45Z, CtlFabSnapshot 10:53:01Z, CtlNoReader 11:38:35–56Z, SUMMARY.md 12:08:40Z (stat birth times). Margin ≥ 11½ min.
- C1 data: none exists even now. `controls-v2/` is empty (dir created 11:10:23Z), `receipts/` holds only the two freeze selftests (10:45:41Z, 11:39:31Z), `snapshots/` holds source pages S103–S109 (not data), `w0/ExecC1Counter.md` is the counter-authoring report (btime 10:43:31Z), `w0b/` is the re-census. No round-60 C1 measure receipt exists; the tip commit itself records "C1 declared exploratory **before data**" (49f7ff22). Vacuously YES — and A1 precedes every artifact that does exist.
- Chronology note: the five v1 control reports (10:50–10:53Z) were scored against counter v1 (freeze `49c3e87d` 10:44:07Z, sha 6aea3be0); erratum E1 `b1cd64bb` (11:06:46Z) swapped in counter v2 and committed the v1 receipts — supersession landed before any C1 measurement, consistent with the "before data" labels in both erratum messages.

## Q3 — Are counter bytes identical from freeze to now?

**YES.**

```
$ for r in b8b2a7a2… bfe8cc2b… 49c3e87d… b1cd64bb… 56a611d6… f9f1268…; do git show $r:verifiers/check_scoped_rules.py | sha256sum; done; sha256sum verifiers/check_scoped_rules.py
b1cd64bb45eee744c4ec93be8631f1eddb28fddd → ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a
56a611d6675662ce389338118c1df87e58437647 → ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a
f9f12681e53a8ca48d28837b9d12fb9fac4cd1a5 → ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a
49f7ff22a3c93a80d649611e9f6e4b8a4b43af35 (tip at 12:16:29Z) → ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a
worktree → ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a  verifiers/check_scoped_rules.py
```

Identical from the assignment's freeze `b1cd64bb` through the current tip and worktree, and equal to the hash in the claim. E2 (49f7ff22) touched only `plans/round-60.md` (+15 lines; `git log b1cd64bb..HEAD --name-only -- plans/round-60.md verifiers/check_scoped_rules.py`).

Caveats, for the record:
- The same-day earlier freeze `49c3e87d` (10:44:07Z) shipped counter v1, sha256 `6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440`; E1 replaced it before any C1 run.
- The counter does not exist at `b8b2a7a2`/`bfe8cc2b` (`git cat-file -e <rev>:verifiers/check_scoped_rules.py` → exit 128 both).
- Honesty note: my first hash pass at those two pre-counter revs piped `git show … 2>&1 | sha256sum` and hashed git's fatal message (outputs `de54c9be…`/`ec62f7e0…`) — those are NOT counter bytes; the `cat-file -e` checks above supersede them.

## Q4 — Does any timestamp in the plan postdate the commit that ships it (lesson R3)?

**YES in one superseded version; NO in the current version.**

- Defect (corrected at the freeze): the plan version shipped by `bfe8cc2b` (committed 10:33:42Z) contains, at blob line 47: `**Draft amendment A1 (10:36Z, before the freeze, before any control or C1 data; the rule is tightened, never loosened).**` — a claimed clock time 10:36:00Z, i.e. 2 min 18 s AFTER the commit that carries it. Impossible authoring order; [INFERENCE] cause: a seat-report receipt time or a UTC/local slip substituted for the amendment time. `b1cd64bb` rewrote the line to `**Draft amendment A1 (committed \`bfe8cc2b\`; before the freeze, before any control or C1 data; …)**` (seen in `git diff bfe8cc2b b1cd64bb -- plans/round-60.md`), removing the wall clock.
- Current version (49f7ff22 blob; ship commit 12:11:51Z) timestamps (grep `20[0-9]{2}-[0-9]{2}-[0-9]{2}|[0-9]{2}:[0-9]{2}`): line 3 "dispatched 10:24Z", line 4 "freeze 12:24Z, hard stop 13:24Z", line 16 R3 row "Closed 10:12Z" / "(10:10:35Z)" (round-59 history), line 99 "fetched 10:29–10:34Z", line 158 "2026-10-22" (round-53 scratch reference). All recorded events precede 12:11:51Z. The only later times are the declared schedule anchors "freeze 12:24Z, hard stop 13:24Z" — future deadlines, not event claims; under R3's own wording (plan line 16: "no clock time later than a `date -u` line taken before the fleet commit") they are not violations. The `10:36Z` string is absent from the current blob.
- Corroboration of ordering inside the A1 citation: `w0/CensusCursor.md` line 9 records `date -u` `Fri 23 Oct 2026 10:29:16 AM UTC` (response 10:29:16 GMT; second fetch 10:31:37 GMT at line 150) — its internal stamps precede its btime 10:32:48Z and A1's commit 10:33:42Z, so the wrong-key finding A1 cites genuinely existed before A1 landed.

## Findings by severity

1. MEDIUM (historical, already corrected): R3 violation in the `bfe8cc2b` plan version — "10:36Z" postdates its own commit 10:33:42Z (evidence above). Corrected in `b1cd64bb`; absent from the current plan. No action needed beyond this record; the lesson M85/R3 count for round 60 may cite it.
2. LOW (calibration): the frozen formula's final shape (A1 conjuncts) postdates five census reports and cites CensusCursor.md:94-108. The round's own texts label this correctly ("tightened before freeze; before any control or C1 data"), so no contract breach — but no downstream text may claim the frozen formula predates the census.
3. LOW (process): two freeze events in one round with a counter swap between them (49c3e87d/6aea3be0 → b1cd64bb/ca2585a4), v1 controls scored in between against v1. Both errata are labeled "before data"; anyone citing "the freeze" must name the commit — `b1cd64bb` is the operative freeze per the assignment.
4. INFO: the tip moved during this review (f9f1268 → 49f7ff22, E2 at 09:11:51-03: C1 declared exploratory after two v2 control worlds met the predicate via forged provenance). Counter bytes unaffected; all findings re-verified at 49f7ff22; worktree clean for `plans/round-60.md` and the counter (status porcelain empty).

## Residual risk and verification gaps

- mtimes/btimes are filesystem claims; I did not audit for clock forgery beyond internal consistency (CensusCursor's internal `date -u`/response stamps cohere with its btime and A1's commit). The other seven census reports were not cross-checked the same way.
- The two v2 control runs named in E2 (`CtlReopenForged` variant d, `CtlReopenHeldKey` b) have no on-disk receipts yet (`controls-v2/` empty at 12:16Z) — consistent with "v2 seats still running"; their chronology is unverified by me.
- jj state not inspected (git evidence sufficient; read-only bounds honored — no git writes, no lane mutations).
