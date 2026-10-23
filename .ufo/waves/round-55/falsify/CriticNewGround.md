Result: MIXED — the counter's `new ground 4` at f0e6b695 holds literally (exit 0), but two of the four counted tokens (`$setup-demo-app` for Codex, `/frontend-design` for Copilot CLI) are renamed examples of forms the lane already held at f0e5de82; only `@skill-id` (opencode) is a new form, and `/skill-name` (Cursor) adds a new client but not a new form, so in substance G is 2 by client and 1 by form.

Seat: KotobaR55.CriticNewGround (critic, wave 2 FALSIFY). Read-only on the lane. The counter and the probe were run in sandbox clone `/fast/scratch/hyaku/kotoba-r55/CriticNewGround` at f0e6b695b746775823b65a8c45de7d50ea33e84f. Base B = f0e5de820a60ec44ff7e5b7c88ac8c8d463dde0c. No tools installed or updated.

## Receipt: the counter as it scores the tip

```
$ date -u   ->  Fri 23 Oct 2026 12:08:32 AM UTC
$ timeout 300 python3 -B verifiers/check_explicit_invocation.py --rev f0e6b695b746775823b65a8c45de7d50ea33e84f --fetch --json
user-typed invocation forms found on the live page 5 of 5; new ground 4
exit=0
```

JSON per client: Claude Code `/skill-name` found, new_ground false (S065's URL is a base row URL); Codex `$setup-demo-app` new_ground true; VS Code not backed (its quote lacks the word `skill`); Copilot CLI `/frontend-design` new_ground true; Gemini CLI not backed (no token); Cursor `/skill-name` new_ground true; opencode `@skill-id` new_ground true. G = 4 distinct case-folded tokens.

How it works (counter at tip, `verifiers/check_explicit_invocation.py:438-446`, `:621-623`): a token is new ground if its lower-cased string is not a substring of base `SKILL.md` or any base `corpus/knowledge/*.md` file, and its row URL is not a base row URL. The haystack leaves out base `corpus/SOURCES.md` (whose teaches cells are corpus content) and base seat reports. The test is a literal substring check, so renaming the example skill name inside a held form makes it "new".

## Per-token verdict

| token (client, row) | verdict | where the lane already held it at B |
|---|---|---|
| `$setup-demo-app` (Codex, S066) | **held in substance** | `corpus/knowledge/skill-overlap-levers-round51.md:26` quotes S021 `build-skills.md:218`: "explicit `$skill` invocation still works"; S021 is base row `corpus/SOURCES.md:34`. The tip entry admits it: `corpus/knowledge/explicit-invocation-round55.md:53-54` ("including Codex's "explicit `$skill` use still works" (S021)") and `:67-68` ("the general `$` rule is stated in S021 (round 51), whose page was already a row at base"). `setup-demo-app` is a demo skill name in a vendor eval blog prompt (`eval-skills.md:148`). The form `$` plus the skill name is the held one; the only new thing is one example of it. |
| `/frontend-design` (Copilot CLI, S068) | **held in substance** | Base `corpus/SOURCES.md:44` (S031, Copilot CLI command reference), teaches cell: "prevents the agent from automatically invoking the skill while `/SKILL-NAME` stays available". Seat `.ufo/waves/round-51/build/SrcCopilotCli.md:29` ("while `/SKILL-NAME` user invocation remains"); `.ufo/waves/round-51/falsify/ReopenS031.md:43` quotes the page: invocation is "via `/SKILL-NAME` or automatically by the agent". I fetched it again: `https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference.md`, 2026-10-23T00:10:37Z, HTTP 200, 461,944 B, sha256 `c61997efd7c939324e1f1b846fcb9ed420e5bbfd5eb5319531c6e6210025b5c9` (the same bytes as the round-51 pin); `:1267` "When invoked (via `/SKILL-NAME` or automatically by the agent)", `:1277` "Whether users can invoke the skill with `/SKILL-NAME`." `frontend-design` is the example name on `add-skills.md:125-128` (fetched 00:10:37Z, HTTP 200, 10,057 B, sha256 `989af4981773349a74feaebfe98cdac9895b394707d201545ba55c8f9f4131a0`). The one real addition is small: `:125` says the slash name goes *inside* the prompt ("include the skill name in your prompt, preceded by a forward slash"), which supports the action cell's "holds" rather than "starts with". |
| `/skill-name` (Cursor, S070) | **new for Cursor; the token itself is held** | Base gives Cursor no invocation form: `git grep -i -E 'cursor.{0,80}(/skill-name\|invok\|slash command)' B` returns nothing. Base Cursor rows cover rules (S049, S052) and the `/skills` warning set (S058, `SKILL.md:190`), and the round-51 lever table has no Cursor row (`skill-overlap-levers-round51.md:18-26`). So "Cursor documents `/skill-name` and `disable-model-invocation`" is new. The token string, though, is a generic placeholder the lane already held for other clients: lower-cased it occurs in base `corpus/SOURCES.md:44` (`/SKILL-NAME`, Copilot CLI); as `/skill-name` it occurs in `.ufo/waves/round-51/falsify/CriticLearningLanded.md:43` (Claude Code `skills.md:347`); and as `/name` it occurs in base `SKILL.md:433` and `skill-overlap-levers-round51.md:23` (Claude Code), and in `sibling-overlap-census-round49.md:31`. At the tip, the Claude Code row uses the identical token `/skill-name` (`SKILL.md:199`) and the counter scores it as held; the same token is counted as new only because Cursor's row has a new URL. |
| `@skill-id` (opencode, S071) | **new form, scoped to opencode V2** | `git grep -n -i -F '@skill' B` over the whole base tree finds 0 hits; no base text gives an `@` mention for loading a skill. The underlying fact was held: base `SKILL.md:434` ("still loadable by exact name"), `skill-overlap-levers-round51.md:24`, and seat `.ufo/waves/round-51/build/SrcOpencode.md:25` quoting `skills.md:129` "They can still be selected manually and loaded by exact name." The base row's live V1 page (`https://opencode.ai/docs/skills`, 2026-10-23T00:10:08Z, HTTP 200, 73,201 B, sha256 `1f918b527340f86c53d5866e11ab837e87e9e245f8550f3f3eee98190a06460c`) still has that sentence at line 148, and 0 matches for `@skill`. The `@skill-id` sentence is only in the V2 docs source (S071, re-fetched 00:10:08Z, HTTP 200, 9,187 B, sha256 `931b5425…a27b`, line 201, the same bytes the row pins). |

Substance count. By new form (a sigil and shape the lane did not hold for any client), there is 1: `@skill-id`. By new client attribution, there are 2: Cursor and opencode. Codex and Copilot CLI add nothing beyond example names and one placement detail. The frozen predicate needs G ≥ 2, so it survives in substance only under the client-attribution reading, and with no margin.

## Counterexample probe (sandbox; counter's own `new_ground`, imported and not edited)

```
$ cd /fast/scratch/hyaku/kotoba-r55/CriticNewGround && timeout 120 python3 -B - <<'EOF' ... EOF
$skill               new_ground(haystack=SKILL+knowledge)=False  (+base SOURCES.md)=False
$setup-demo-app      new_ground(haystack=SKILL+knowledge)=True  (+base SOURCES.md)=True
/name                new_ground(haystack=SKILL+knowledge)=False  (+base SOURCES.md)=False
/skill-name          new_ground(haystack=SKILL+knowledge)=True  (+base SOURCES.md)=False
/SKILL-NAME          new_ground(haystack=SKILL+knowledge)=True  (+base SOURCES.md)=False
/frontend-design     new_ground(haystack=SKILL+knowledge)=True  (+base SOURCES.md)=True
@skill-id            new_ground(haystack=SKILL+knowledge)=True  (+base SOURCES.md)=True
exit=0
```

The pairs `$skill`/`$setup-demo-app` and `/name`/`/skill-name` hold the same form and get opposite verdicts. This is the round-55 W3 case-flip shortcut (plan Erratum 1) in a more general shape: v2 closed the case flip but not a placeholder rename. With base `SOURCES.md` added to the haystack, `/skill-name` becomes held and G would drop to 3. No placeholder-aware check is possible without a reviewer, so G cannot measure form novelty on its own.

## Findings

1. **G = 4 overstates new ground (impacted axis: depth; calibration of the C1 claim).** Two of the four tokens are held in substance (Codex and Copilot CLI; evidence in the table). This is a weakness of the frozen counter and is reported here, not fixed. It is a tradeoff the judge has to weigh, not a defect a seat can repair this round: the predicate is literal and is met. Smallest safe correction: any round-55 receipt or lesson that cites `new ground 4` should add the reviewer reading "new in substance: Cursor and opencode (client); `@skill-id` (form); Codex and Copilot CLI held at B (S021, S031)". Route the counter weakness to the next counter revision: add base `corpus/SOURCES.md` to the haystack, and count new ground per client form (sigil plus client), not per example token.
2. **False provenance in the entry (impacted axis: consistency; it is the over-wide record defect again).** `corpus/knowledge/explicit-invocation-round55.md:54-55` says round 51 "did not hold … the Copilot CLI, VS Code, Cursor and opencode forms". Copilot CLI's `/SKILL-NAME` was held (base `corpus/SOURCES.md:44`, S031). VS Code's `/` command was held (base `SKILL.md:432` "manual `/` invocation only"; `skill-overlap-levers-round51.md:22` "the `/` command still works", `:32`). opencode's load by exact name was held (base `SKILL.md:434`), though not its `@` form. Smallest safe correction (text for the L1): "It did not hold the per-client explicit form as a classifier for measurement, nor the Cursor form or opencode V2's `@` mention; Copilot CLI's `/SKILL-NAME` (S031), VS Code's `/` command (S025) and opencode's load-by-exact-name (S024) were held only as side notes to the round-51 levers."
3. **The opencode row is wider than its source (impacted axis: depth; identity of the client version).** Tip `SKILL.md:205` says `opencode | @skill-id` without saying which version. The entry (`:34`, "opencode V2 (S071)") and the S071 teaches cell (tip `corpus/SOURCES.md`, row S071) both scope it to V2, and the served V1 page (the base S024/S059 page) has no `@skill` form (0 matches; fetch record above). [INFERENCE] The lane's pinned opencode is 1.19.x, which follows the V1 page; I did not run the binary. Smallest safe correction: write the SKILL.md client cell as `opencode (V2 docs)`, or add "V2" to the action cell.
4. **Context, low weight: the measurement step was partly held.** Base `corpus/knowledge/trigger-miss-proxy-round6.md:14-16` already stripped slash-command tokens (`/skill:godspeed`, `/ufo`) from user intent text as "invocation verbs, not router intent". The tip entry's `:14-16` describes that proxy only as covering "prompts that name a skill". The round-6 proxy removed tokens rather than setting whole turns aside, so the per-client table still adds something. The entry should not imply that setting explicit invocations aside is wholly new.

## Not checked

- I did not re-check that the five counted quotes are verbatim on their live pages beyond the counter's `--fetch` (seat W2RerunC1 owns that).
- No client behaviour was run.
- I did not open the Cursor page; the Cursor verdict rests on the base sweep (no base Cursor invocation text) and the counter's `found` result.

Process hygiene: every command was capped with `timeout` or finished in seconds; no background processes were left running. Scratch files are only under `/fast/scratch/hyaku/kotoba-r55/CriticNewGround/`.
