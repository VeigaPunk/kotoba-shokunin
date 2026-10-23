Result: MIXED — C1 is correctly a depth claim named by its surface, the plugin Frontier row is genuinely untouched by rounds 53–56, the owned-axes reading is applied and disclosed, no v2 control reaches the target, and withdrawing C2 was the correct §9 branch; two calibration gaps remain: the plan's summary of rounds 53–56 is false for round 53, and the zero-margin F>=5 configuration is undisclosed.

Seat: KotobaR57.CriticAxisFit (critic, leaf). Lane cwd `/home/vgpnk/Projects/shokunin/kotoba-shokunin`. Read-only; no lane writes except this report. Sandbox created: none (no code executed; counters read from committed bytes). No tool installs or upgrades.

## 1. Is C1 correctly a depth claim when named by the surface? — YES

- `AXES.md:11` defines depth as "Verifiable technical detail — decision tables with real thresholds, named error signatures, cited sources". C1's surface is a new `SKILL.md` decision table `### Plugin manifests by client` plus a cited entry and SOURCES rows (`plans/round-57.md:25`). That is the depth signal itself, not an inference from a number.
- The axis is named by surface in the plan (`plans/round-57.md:25`, "Surface: a new `SKILL.md` decision table …"), not by the score. The number 9 appears only to select which axis the lowest-axis duty requires (`plans/round-57.md:10-11`), which is the duty's rule, not axis naming (`/home/vgpnk/Projects/shokunin/.ufo/prompts/kotoba-round-57.md:361`).
- The lane's own line between depth and coverage supports the label. Round 52's MCP `instructions` claim was booked coverage (`SCORECARD.md:30`) and landed a paragraph at `SKILL.md:86`, not a table; rounds 54/55/56 booked `### … by client` tables as depth (`SCORECARD.md:28`). C1 falls on the depth side of that line.
- Residual (calibration, small): the same table also advances coverage's surface fraction (a new edge class: plugin-delivered instruction files). The plan does not say so. One clause in the round report — "booked as depth (the SKILL.md decision table); the surface-fraction advance is not claimed" — closes the axis-shopping read. No predicate or plan change.

## 2. Is either claim 'quality work' mislabelled? — NO

Definition: re-scoring a rule the lane already holds on new inputs, or counting rows a sourceless fixture also counts (`…/kotoba-round-57.md:361-363`).

- C1 lands new ground. Base held-ground count for the eight plugin tokens is 0: `git --no-optional-locks grep -F -o -e '.claude-plugin' -e '.codex-plugin' -e '.cursor-plugin' -e 'gemini-extension.json' -e 'plugin.json' -e '.opencode/plugin' -e '.github/plugin' -e 'marketplace.json' 47c05558 -- . ':!.ufo' | wc -l` → `0`, exit 0. So no held rule is being re-scored; the counter's held-ground guard (v2 E2, `verifiers/check_plugin_manifests.py:22-27` @ `01312a77`) is the mechanism that keeps a future round from doing so.
- Partial caveat: the SKILL.md "What a plugin can ship" column may restate held facts (MCP servers are held at r52, S032–S037). The frozen predicate counts manifest tokens only, so the label is unaffected; the report must not bank the shipped-parts cell as new ground (see §5 Residual B).
- C2 was withdrawn before data and carries no axis label at all (`plans/round-57.md:124-132`), so it cannot be mislabelled as quality work.

## 3. Does the round work a different Frontier area? — YES, with one false sentence in the plan

- Row verified untouched: `corpus/README.md:102` (round-52 append: "still not held: plugin surfaces"). Rounds 53–56 knowledge entries are always-on rule files, description thresholds, explicit invocation and agent-definition files (`ls corpus/knowledge/ | grep -E 'round5[3-6]'`); none covers plugin manifests. Base grep above is 0.
- Defect (calibration, small): `plans/round-57.md:12` says "rounds 53–56 worked skill-listing and agent-definition surfaces". That is false for round 53, whose claims were loader-rule freshness (`SCORECARD.md:32`) and always-on checklist boxes (`SCORECARD.md:31`). The anti-loop conclusion survives because neither of those is the plugin or command row; the sentence should read "rounds 54–56 …; round 53 worked loader freshness and the always-on checklist". Report/plan prose only.
- After Erratum 1 the round works one Frontier row, not two. The report must not cite Command extraction as worked this round; the anti-loop sentence at `plans/round-57.md:12-16` claims two rows.

## 4. Is the owned-axes lowest-axis reading applied correctly and disclosed? — YES

- Base scores verified exactly as stated: `git --no-optional-locks show 47c05558:SCORECARD.md` → depth 9, consistency 10, coverage 8.5, operability 8.5, freshness 8, calibration 8.5, adjacency 8.0; matches `plans/round-57.md:10`.
- Owned axes are depth + consistency (`SCORECARD.md:3`), with consistency a calibration sub-axis (`SCORECARD.md:11-13`). Lowest owned = depth 9 vs consistency 10 → the reading is applied correctly.
- The all-axes lowest (freshness 8 and adjacency 8.0, tied) is disclosed as not worked (`plans/round-57.md:11-12`), matching the round-56 closure record (`corpus/lessons/round-56-verifier-spotcheck.md:165`) and the round-47 ruling that the ambiguity is carried, not waived. Correct not to decide the open L0 question.
- The stagnation waiver is correctly not invoked: the nudge is dormant (`SCORECARD.md:310-316`, depth 9 below the 10.0 line) and `AXES.md:66-71` waives only when every owned axis sits at or above the line and no capability entered within the window.
- Nit: `plans/round-57.md:11` says "neither claim works them"; after Erratum 1 it is one claim.

## 5. Could a do-nothing control reach C1's target under counter v2? — NO on the committed evidence; two residuals

Evidence:

- Base: `.ufo/waves/round-57/controls/C1-base-v2.txt` → `plugin manifests found on the live page 0 of 0; new ground 0`, exit 1; `--self-test` → `0 failure(s) over 235 assertions`, exit 0; counter sha256 `bf11a4ef…` as frozen.
- v2 re-scores (all with `--fetch`, unmodified v2): best hollows are `F=1/7` (`CtlC1DoNothingJunk.md:198`), `F=1/6` (`CtlC1KeyedLabels.md:189`), `0/4` (Fabricated), `0/0` (`CtlC1RealNoForm.md:122`). Strongest is a real-token adaptation: `F=3 of K=3; G=3`, exit 1, blocked only by F<5 (`CtlC1HeldVariant.md:70`). No control reaches F>=5, G>=3.
- Timeliness: the v2 re-scores were committed at `27af04a` (04:46Z), before the build dispatch; the build directory holds no C1 data at tip (`git ls-tree -r --name-only HEAD | grep round-57/build` → dispatch/spec/validation only). Nothing was scored before the re-scores landed.

Residual A — zero margin, not disclosed. F>=5 is satisfiable in exactly one five-client configuration on the current pinned pages. My probes (2026-10-23T04:49–04:51Z, ordinary curl, no browser):

- Codex: `https://developers.openai.com/plugins/build/plugins` → HTTP 200, 530,153 B, sha256 `c0dae0a9c8520217…`; the page carries `.codex-plugin/plugin.json` (and a root `plugin.json` that v2's single-segment rule rejects). Codex's plugin docs pages themselves name no `.json` path: `developers.openai.com/codex/plugins.md` → 308 → `learn.chatgpt.com/docs/plugins.md`, 200, 14,241 B, sha256 `612ebfed2779c4aa…`, no `.json` token; `learn.chatgpt.com/docs/build-plugins.md` 200, 13,963 B, no `.json` token; `raw.githubusercontent.com/openai/codex/main/docs/plugins.md`, `plugins/README.md`, `docs/plugin.md` → 404.
- Copilot CLI: `https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference` → 200, 871,480 B, sha256 `2b138335c83e29c1…`; names `.plugin/plugin.json` (2 segments, v2-valid), plus `.claude-plugin/plugin.json` (foreign marker, correctly rejected for Copilot CLI) and `marketplace.json` (marketplace segment, rejected).
- Claude Code `.claude-plugin/plugin.json`, Gemini CLI `gemini-extension.json`, Cursor `.cursor-plugin/plugin.json` come from the control's own live scan (`CtlC1HeldVariant.md:70`).
- VS Code's extension manifest is `package.json` (no extension word in a path segment) and opencode's plugins are code modules, so both are honest omissions under the round's own rule, lowering K rather than F.

Consequence: K = 5 and F>=5 requires 5 of 5 found with grounded quotes, zero slack. One redirect, one changelog-landing URL or one sub-6-word quote turns the round into an honest miss. The plan should state this configuration and the round report should carry the K census with the per-client reason (this is exactly the "report that honestly" case in the wave context). No predicate change: the target cannot be narrowed after data (`…/kotoba-round-57.md:351`).

Residual B — the predicate measures only the manifest half. A world with these five real tokens and junk "What a plugin can ship" cells would pass; the declared Q31 bound (`plans/round-57.md:33-35`) covers it, so it is a known bound, not a breach. The round report must not claim the shipped-parts column as verified, and the falsify reviewer reading is its only check.

## 6. Was withdrawing C2 the right branch of §9, versus amending its counter? — YES, withdrawal was right

- The v1 counter was met by hollow worlds that do no fence work: a generator-keyed patch (120/120 on six seeds), a patch keyed on the extraction path with a byte-identical live run, a character-skip with an echo fallback, and a 50-line stub that replaces the whole gate. `MutC2Counter.md:1` → `Result: BREAKS — 35 of 96 single-point mutants of the frozen C2 counter survive its --self-test … and the unmutated frozen counter scored a 50-line stub`, with 14 survivors shown to let a hollow world exit 0 (`MutC2Counter.md:5-8`).
- The flaw is structural, not a missing case class: the counter answers a standalone instrument on inputs it makes itself, so any instrument — including one that deletes the gate — can satisfy it. The erratum's v2 (`w0/check_infoless_fences_v2.py`, committed at `01312a77`) only widens the case set (base `168 of 264`, exit 1) and, by the erratum's own words, still lacks the gate-deletion conjunct and was not re-controlled (`plans/round-57.md:129-131`). Freezing it would violate prompt:352 ("build the cheapest control that skips the claimed work … before freezing") and the rule that the claim is judged on the predicate declared before data.
- Amending again would be counter-of-the-gaps against known hollow worlds — the round-55 M49 failure mode — and the fix that would close it (require the real gate path to participate, prove deleting the fix fails, and prove the live checklist output unchanged) is a redesign, not an amendment. Withdrawal before data is the honest branch, matches the round-56 precedent, and keeps the redesign inputs un-pre-scored.
- Confirmed no seat pre-scored the later claim: `git --no-optional-locks diff --stat 47c05558..27af04a -- verifiers/` → only the two new counters (`check_infoless_fences.py`, `check_plugin_manifests.py`); `verifiers/verify_skill_checklist.py` is untouched.

## Impacted axes and harm

- depth: C1 moves as declared; no harm. consistency/calibration: the two prose defects above are record precision, not claim scope; no score change argued. operability: C2's withdrawal leaves it untouched (holds 8.5), no harm. freshness/adjacency: untouched, as disclosed.
- The round does not claim saturation; depth stays 9 below the 10.0 line, so the nudge correctly stays dormant.

## Smallest safe corrections (report-level; no frozen byte changes)

1. Round report: state that C1 is booked as depth for the `SKILL.md` decision table, and that its coverage-surface advance is not claimed (one clause).
2. Round report: carry the K census — five count-eligible clients (Claude Code, Codex, Copilot CLI, Gemini CLI, Cursor) and two honest omissions (VS Code, opencode) — and state that F>=5 therefore requires 5 of 5.
3. Round report/plan prose: correct `plans/round-57.md:12` ("rounds 53–56") to exclude round 53, and say the round works one Frontier row after C2's withdrawal.
4. Falsify wave: read the "What a plugin can ship" cells against their quotes, since the predicate cannot.

## Commands run (all read-only; exit codes as shown)

- `git --no-optional-locks show 47c05558:SCORECARD.md` (axis rows) — exit 0.
- `git --no-optional-locks grep -F -o … 47c05558 -- . ':!.ufo' | wc -l` → `0` — exit 0.
- `git --no-optional-locks show 01312a77:verifiers/check_plugin_manifests.py` (docstring, HOSTS, summary) — exit 0.
- `git --no-optional-locks log --format=… -- .ufo/waves/round-57/controls/` → `27af04a` then `01312a7` then `ee50d8f` — exit 0.
- `git --no-optional-locks diff --stat 47c05558..27af04a -- verifiers/` → the two new counters only — exit 0.
- `python3` not run (counters only read). curl probes above: HTTP 200/308/404 as listed; byte counts and truncated sha256 recorded.
