Result: HOLDS — draft→freeze→addendum→controls is a linear chain; targets are absent at the draft and enter only at the freeze with the census-consistent values (4, 5); the frozen counter sha256 equals the sha every control receipt names; no C1 content (section, knowledge/lessons entry, rows S096–S102, snapshots) exists at or before `67b68e0f`; census mtimes/fetch times and all control sandbox commits/times sit inside the correct windows.

Reviewer: KotobaR59.ReviewPlanChronology, 2026-10-23 (report clock `date -u` at start of write: 2026-10-23T09:44:02Z). Lane read-only throughout; every git call `git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin …`. No tools installed (none needed). Scratch dumps: /fast/scratch/hyaku/kotoba-r59/ReviewPlanChronology/ only.

## 0. Commit chain (metadata + ancestry)

```
$ git --no-optional-locks show -s --format='%H | parent %P | commit %cI | %s' <each sha>
a975cbbf… parent ed44e0c4… commit 2026-10-23T05:55:16-03:00 (= 08:55:16Z) round-58 verifier spot-check …
a3e70a30… parent a975cbbf… commit 2026-10-23T06:00:07-03:00 (= 09:00:07Z) round-59: plan draft (C1 hook files row rule, targets TBD) …
4b2125c9… parent a3e70a30… commit 2026-10-23T06:19:01-03:00 (= 09:19:01Z) round-59: freeze C1 (census F_max 6, G_max 6; T_F 4, T_G 5; counter … f695d59e) …
67b68e0f… parent 4b2125c9… commit 2026-10-23T06:19:52-03:00 (= 09:19:52/53Z) round-59: freeze addendum — Events conjunct limit …
283124cd… parent 67b68e0f… commit 2026-10-23T06:32:27-03:00 (= 09:32:27Z) round-59: pre-data control receipts (8 controls, none meets the C1 predicate)
```

Ancestry: `merge-base --is-ancestor` → a975cbbf≤a3e70a30 YES, a3e70a30≤4b2125c9 YES, 4b2125c9≤67b68e0f YES, 67b68e0f≤283124cd YES, a3e70a30≤283124cd YES. `rev-list --count` between consecutive hops: 1, 1, 1, 1 (strictly linear, no intermediate commits). Diffstat draft→freeze adds exactly the W0 census reports, w0/ExecC1Counter.md, w0/check_hook_files.py, verifiers/check_hook_files.py (+2429), receipts, SKILL.md (+1), plans/round-59.md (+20/−1). Freeze→addendum: plans/round-59.md only (+7). Addendum→controls: controls-call.json + 8 receipts + SUMMARY.md only.

## 1. Targets absent at the draft, present only at the freeze — HOLDS

- Draft `a3e70a30:plans/round-59.md:63`: `- Targets: `TBD` (set at freeze from the census by the formula above).`
- `grep -nE 'T_F = 4|T_G = 5|TARGET = 4|NEW_TARGET = 5' plan-draft.md` → no matches (`no concrete targets in draft plan (only TBD)`).
- Freeze `4b2125c9:plans/round-59.md:78`: `- **Targets (frozen by the formula): T_F = 4, T_G = 5.** Counter … `TARGET = 4`, `NEW_TARGET = 5``. The draft→freeze plan diff shows exactly `- Targets: `TBD`` → the frozen block.
- Introduction pickaxe up to the controls commit:
  ```
  $ git log --format='%h %cI %s' -S'T_F = 4' 283124cd52af… -- plans/round-59.md
  4b2125c 2026-10-23T06:19:01-03:00 round-59: freeze C1 (census F_max 6, G_max 6; T_F 4, T_G 5 …)
  ```
  One commit only — the freeze. The counter file itself does not exist at the draft (`cat-file -e a3e70a30:verifiers/check_hook_files.py` → absent); first existence is the freeze.

## 2. Draft formula equals frozen values given the census — HOLDS

- Formula, verbatim identical at draft and freeze (`plans/round-59.md:58-59` in both blobs): `T_F = F_max − 2 and T_G = G_max − 1`, where F_max = census count of eligible clients, G_max = eligible tokens with 0 base hits. Guard: `If F_max < 5 or G_max < 2 the claim is redesigned before data` (line 59).
- Frozen census record (`4b2125c9:plans/round-59.md:75`): `F_max = 6; G_max = 6 (every eligible token 0 hits …)`. The census table lists exactly 6 ELIGIBLE clients (Claude Code, Codex, VS Code, Copilot CLI, Gemini CLI, Cursor) with opencode NOT ELIGIBLE — consistent with the W0 reports.
- Arithmetic: 6−2 = 4 = T_F; 6−1 = 5 = T_G. Matches the frozen claim values (F_max 6, G_max 6 → 4, 5). Guard not triggered (6 ≥ 5, 6 ≥ 2).
- Counter constants at the freeze blob: `verifiers/check_hook_files.py:253` `TARGET = 4`, `:254` `NEW_TARGET = 5` (read from `4b2125c9:…`). Plan's counter constants, targets, and census all agree.

## 3. Counter sha at the freeze equals the sha every control receipt names — HOLDS

```
$ git show 4b2125c9…:verifiers/check_hook_files.py | sha256sum
f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71  -
```
Identical at addendum `67b68e0f` and controls commit `283124cd` (no counter drift after freeze). All 8 receipts AND SUMMARY.md contain that sha (`grep -rL '<sha>' controls/` → empty list, i.e. none omits it; each receipt's provenance block shows `git show 67b68e0f…:verifiers/check_hook_files.py | sha256sum` → f695d59e…). Consistency extra: the plan's pre-freeze build hash `cfeb915d…` matches `git show 4b2125c9:.ufo/waves/round-59/w0/check_hook_files.py | sha256sum` → `cfeb915de1597148dce659effb3eb2ebd5f5c25893b5aa9b8d1302fd850c0112` (the `None`-targets build, as the plan states).

## 4. No C1 content at or before `67b68e0f` — HOLDS

Direct checks at the freeze and the addendum (both commits):
- `SKILL.md` grep `Hook files by client` → ABSENT at both.
- `corpus/SOURCES.md` grep `S09[6-9]|S10[0-2]` → ABSENT at both.
- `corpus/knowledge/hook-files-round59.md` → ABSENT at both (`cat-file -e` fails).
- `corpus/lessons/round-59.md` → ABSENT at both (path does not exist; the corpus/lessons tree at the addendum ends at round-58 files).
- `git ls-tree -r --name-only <rev> -- .ufo/waves/round-59/snapshots/` → empty at both.

Pickaxe over the full ancestry of `67b68e0f` (empty = never present at or before):
```
$ git log --format='%h %cI %s' -S'Hook files by client' 67b68e0f… -- SKILL.md        → (empty)
$ git log --format='%h %cI %s' -S'S096' 67b68e0f… -- corpus/SOURCES.md               → (empty)
$ git log --format='%h %cI %s' 67b68e0f… -- '.ufo/waves/round-59/snapshots/'         → (empty)
$ git log --format='%h %cI %s' 67b68e0f… -- corpus/knowledge/hook-files-round59.md   → (empty)
$ git log --format='%h %cI %s' 67b68e0f… -- corpus/lessons/round-59.md               → (empty)
```
Sensitivity control (the queries are capable of finding the content): the same pickaxes over `--all` are also empty — the C1 content is not committed on any ref at all as of 2026-10-23T09:42:28Z (integration still uncommitted; state observation, not a defect). Cross-corroboration: CtlAllFalse's restore table records knowledge/lessons/snapshots ABSENT in the pristine frozen tree at `67b68e0f`.

## 5. Census report mtimes and fetch times — CONSISTENT

Working-tree mtimes (`ls -l --time-style=full-iso .ufo/waves/round-59/w0/`): census reports 06:05:02–06:10:52 -03:00 (= 09:05:02Z–09:10:52Z); ExecC1Counter.md 06:17:53 (= 09:17:53Z) — all ≤ freeze commit 09:19:01Z. All 7 committed census blobs at the freeze are sha256-identical to the working-tree files (e.g. CensusClaudeCode `771bc4b5…`, CensusVSCode `3556dbe7…`) — no post-freeze census edits.

Fetch times recorded inside the committed census files: initial fetches 09:02:19Z (Claude), 09:02:48–09:03:23Z (Gemini), 09:02:50Z (VS Code), 09:02:52–09:04:25Z (opencode), 09:02:56Z (Copilot CLI), 09:03:03Z (Cursor), 09:03:06–09:04:38Z (Codex, incl. 308-redirect recheck); recheck/cross-check fetches to 09:06:13Z (Copilot CLI), 09:07:57Z (VS Code cross-check), 09:08:23Z (opencode `gh api`). All fetches begin after the draft commit 09:00:07Z — matching the draft subject "census start" and "targets TBD … before any census seat returns" — and all end before the freeze 09:19:01Z. Minor wording note: the freeze record says "fetched 09:02–09:05Z", which covers the initial fetch batch; rechecks extend to 09:08:23Z, still pre-freeze. No chronology violation.

## 6. Control receipts: sandbox commits and times — CONSISTENT

Every receipt names the counter sha (§3) and the frozen input `67b68e0f`. Sandbox commits verified read-only in the sibling clones (`git --no-optional-locks show -s --format=%cI/%P <sha>` in /fast/scratch/hyaku/kotoba-r59/<Ctl…>):

| receipt | sandbox commit | commit time (Z) | parent |
|---|---|---|---|
| CtlDoNothing | 2fc6e37ed71a249b… | 09:22:02 | 67b68e0f |
| CtlDoNothing | c0735a874bc04120… | 09:22:16 | 2fc6e37e |
| CtlAllFalse | bb43204d10abaec4… | 09:23:58 | 67b68e0f |
| CtlAllFalse (restoration) | f65870c550266569… | 09:25:27 | bb43204d |
| CtlLabelShortcut | 063faa4b822a25b8… | 09:24:05 | 67b68e0f |
| CtlJunk | b75bdf760b8b9800… | 09:25:20 | 67b68e0f |
| CtlOffTopic | 6809c14643634a44… | 09:25:24 | 67b68e0f |
| CtlFabSnapshot | 2854318355cf29f8… | 09:25:42 | 67b68e0f |
| CtlFabEvents | 39dd1caa7adcc251… | 09:26:23 | 67b68e0f |
| CtlFabSnapshot | cff124a8b6593179… | 09:26:56 | 28543183 |
| CtlFabSnapshot | 76310513bda537e3… | 09:26:57 | cff124a8 |
| CtlNoReader | 6154cab6e106f3e9… | 09:27:14 | 67b68e0f |
| CtlNoReader | 5e88a7413bc15801… | 09:28:34 | 67b68e0f |

All sandbox commits: parented on the freeze addendum `67b68e0f` (or a prior sandbox world of the same receipt), timed 09:22:02Z–09:28:34Z — strictly after the addendum (09:19:53Z) and before the controls commit `283124cd` (09:32:27Z). In-receipt run stamps span 09:22:31Z–09:27:17Z (e.g. CtlFabSnapshot page fetches 09:22:45Z/09:23:23Z; CtlOffTopic `--fetch` 09:25:29Z; CtlAllFalse trace rows 09:26:33–09:26:37Z) — same window. SUMMARY.md (committed at `283124cd`) matches: 8 controls, all exit 1, predicate NOT MET. "Targets and counter committed before the control wave scores them" (plan, commit-order bullet): satisfied — controls build on `67b68e0f`, after `4b2125c9`.

## Supplementary

SKILL.md line counts: base `a975cbbf` 596, draft 596, freeze `4b2125c9` 597, addendum 597 — matches the frozen claim ("597 at the freeze (base 596)"); the freeze's +1 line is within the ≤3-line ExecBudgetMove exemption, so no move-out was owed at the freeze. (Draft commit shows author time == base commit time 05:55:16-03:00 with commit time 09:00:07Z — jj rewrite artifact, not a chronology defect.)

## Residual risk and verification gaps

- The counter was not executed by this seat (chronology scope, no lane-code execution): receipt exit codes/predicate verdicts are taken as recorded data, not independently re-run. ReviewC1Counter owns execution.
- Sandbox commit times were read from the sibling clones via `cat-file` (read-only); a post-hoc mutated clone could in principle carry shifted stamps, but every sandbox time also agrees with timestamps printed inside the committed receipts, and sandbox commit times are attacker-controlled data in this design — the binding evidence is the receipts' own content at `283124cd`.
- Pickaxe screens literal strings (`Hook files by client`, `S096`, `T_F = 4`); differently encoded content could evade it. Mitigated: the direct greps and empty `ls-tree` listings at both commits are the primary absence evidence, and the C1 shapes screened are exactly those the claim fixes.
- The freeze record's "fetched 09:02–09:05Z" understates the census session's recheck fetches (to 09:08:23Z); cosmetic, pre-freeze, no effect on any predicate.
- C1 integration is not yet committed on any ref (as of 09:42:28Z); absence-at-or-before-addendum claims remain true regardless of when integration lands, since integration commits postdate `283124cd`.
