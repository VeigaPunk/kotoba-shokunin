# Round-49 build — Q19 before-value re-measure (seat BeforeRemeasure)

Date 2026-10-22. Base `a5adc146a2995dcc5a95a6d8db6e5674f75191ac`. Every before-value in
`plans/round-49.md` was re-measured at that commit via `git show <base>:<path>` (never the
working tree), per Q19 ("re-measured at round start and printed with its command and commit").
Reading channel: private clone at `/fast/scratch/hyaku/kotoba-r49/seats/BeforeRemeasure/clone`,
checked out at base; blob byte-identity proven below. Lane untouched except this report file.
No tools installed (none needed).

## Findings

**Zero divergences: all re-measured before-values match the plan.**

- F1 (referent note, no action): the plan's "`.ufo/watchdog.log`" is the **fleet-root** log
  `/home/vgpnk/Projects/shokunin/.ufo/watchdog.log`; the lane repo has no `.ufo/watchdog.log`
  at base (base `.ufo/` holds only reports/round-20..48/waves). The claim itself holds (below).
- F2 (live-ledger note, no action): fleet `MANIFEST.json` `.rounds` length is now **444**
  (last entry = mori round 24, appended after plan writing). `rounds[442]` is still exactly the
  kotoba round-48 closure entry, `"admitted":true` — the plan's claim holds as cited.
- F3 (caveat): the census validate command runs on the fleet working tree. Kotoba's
  `corpus/SOURCES.md` is clean vs base (`git status --porcelain` shows only
  `M SCORECARD.md`, `?? .ufo/waves/round-49/`, `?? plans/round-49.md`), so the kotoba-side
  input equals base bytes; sibling lanes' working trees were not audited (the three W04s are
  cross-lane URL sightings).
- F4 (observation): the lane working tree carries this round's build in flight
  (`M SCORECARD.md` + untracked plan/waves files). No base read used it.

## Re-measured values (command → output → exit code)

1. **Base identity.** `git -C <lane> rev-parse master` → `a5adc146a2995dcc5a95a6d8db6e5674f75191ac`;
   `git log -1 --format='%H %ci %s' a5adc14…` → `a5adc146a2995dcc5a95a6d8db6e5674f75191ac
   2026-10-22 06:28:59 -0300 round-48 verifier spot-check (integrator, hyaku): non-author
   admit/reject`. EXIT:0.

2. **C1 before = 10 of 20 (expected 10) — MATCH.**
   `git -C <lane> show a5adc146…:PROVINCE.md | awk '/^## Adjacent/,0' | grep -oE
   '\b(audio|chousa|game-dev-2d|game-dev-3d|kagi|kaidoku|kake|kama|kasegi|kengaku|kotodama|kumitate|lore|mado|mori|revenger|souji|tabi|tameshi|tsukuroi)\b'
   | sort -u | wc -l` → `10`, EXIT:0.
   Names: chousa, kama, kasegi, kengaku, kotodama, kumitate, mado, mori, revenger, tameshi.
   `## Adjacent` occurs exactly once at base (`PROVINCE.md:25`), so the awk range is unambiguous.
   Denominator: `ls -d /home/vgpnk/Projects/shokunin/*-shokunin | wc -l` → `21` dirs incl.
   kotoba → **20 siblings**. EXIT:0.

3. **C2 before = 0 of 9 (expected 0) — MATCH.**
   `git -C <lane> show a5adc146…:verifiers/checklist-baseline.json | jq
   '[.boxes[]|select((.box_id|startswith("dispatch.")) and
   (.disposition|test("^(executed|delegated):")))]|length'` → `0`, EXIT:0.
   Denominator: 9 dispatch boxes (dispatch.01–dispatch.09; 41 boxes total), **all nine**
   `unexecuted:` at base — the "of 9" half holds literally.

4. **Census start — MATCH (exit 0, `kotoba ok`, exactly three W04: S018, S019, S021).**
   `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
   /home/vgpnk/Projects/shokunin kotoba` →
   `kotoba  W04  S018 duplicate url agentskills.io/specification across scopes`
   `kotoba  W04  S019 duplicate url platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices across scopes`
   `kotoba  W04  S021 duplicate url learn.chatgpt.com/docs/build-skills across scopes`
   `kotoba  ok    /home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md`
   EXIT:0. W04 = "same URL across scopes (warnings do not affect clean lanes)"
   (`scripts/sources-census.sh:33`, emit at `:644-645`).

5. **SCORECARD axes at base — freshness 8, adjacency 8.0 are the two lowest non-retired — MATCH.**
   Base axes table (blob sha `b7391dee…`): depth 9 · consistency (calibration sub-axis) 10 ·
   coverage 8.5 · operability 8.5 · freshness 8 · calibration 8.5 · adjacency 8.0 — was 7.5.
   `## retired` (line 129-131): "None. No saturation or wrong-fit evidence." So the two lowest
   non-retired are freshness 8 and adjacency 8.0; next band 8.5 (coverage/operability/calibration).
   C1 works adjacency (one of the two lowest) as the plan states.

6. **Stagnation nudge does not apply — HOLDS.**
   `/home/vgpnk/Projects/shokunin/AXES.md:66-71` (§ The stagnation nudge): fires only "When
   **every** axis the lane owns sits at or above the lane's saturation line **and** no capability
   has entered the table within the lane's stagnation window". Base `SCORECARD.md` § Saturation
   (lines 252-262): "**Saturation line: 10.0 on the owned axes** (depth and the
   consistency/calibration sub-axis …) … consistency 10 (criterion met), depth 9 — depth sits
   below the line, so **the nudge is dormant**." Owned depth 9 < 10.0 → first condition fails →
   nudge does not apply, exactly as the plan claims.

7. **No earlier round-49 attempt — HOLDS.**
   `grep 'lane-dead-no-report kotoba round=49' /home/vgpnk/Projects/shokunin/.ufo/watchdog.log`
   → No matches found. Log is current: line 641 `2026-10-21T20:38:04-03:00 launch kotoba
   round=48 … attempt=1`, line 650 `lane-dead-no-report kotoba round=48` (superseded attempt),
   line 668 `2026-10-22T06:19:11-03:00 complete kotoba round=48; hyaku-inline attempt=2`.
   (Round-48 dead lines exist for superseded attempts; the plan claims only round=49 absence.)

8. **Round 48 admitted, MANIFEST rounds[442] — HOLDS.**
   `jq '.rounds[442]' /home/vgpnk/Projects/shokunin/MANIFEST.json` → `{"round":48,
   "date":"2026-10-22","type":"closure","lane":"kotoba","lane_round":48,"lanes":{"kotoba":"ok"},
   …,"admitted":true,"verdict":"admitted",…,"report":".ufo/reports/round-48/kotoba.md",
   "verification":{"reviewer":"hyaku-closure (@m_opus session, non-author)",
   "spotcheck":"kotoba-shokunin/corpus/lessons/round-48-verifier-spotcheck.md@a5adc146…",…}}`.
   Array length now 444 (F2). EXIT:0.

## Reading-channel byte identity (clone == git-show blob)

```
git show a5adc146…:SCORECARD.md | sha256sum            b7391dee211a11ca… == clone/SCORECARD.md
git show a5adc146…:PROVINCE.md | sha256sum             02740235b0f0d8dc… == clone/PROVINCE.md
git show a5adc146…:verifiers/checklist-baseline.json   82bf86d60b72f7e1… == clone/verifiers/checklist-baseline.json
```

All `echo EXIT:$?` → `EXIT:0`.

## Residual risk / verification gaps

- Census validate (item 4) is a working-tree measurement by design; sibling SOURCES.md state at
  run time was not audited, so the three W04 rows are not pinned to base blobs (kotoba's own
  input is base-identical).
- "20 sibling lanes" is the directory census this session; pinned per-sibling commits are C1's
  census content, not re-measured here (out of this seat's scope).
- Bounds kept: read-only on the lane/fleet/siblings (no git/jj writes, no jj at fleet root);
  only this report file written in the lane.
