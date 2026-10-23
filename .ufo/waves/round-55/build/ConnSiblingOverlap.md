Result: DONE — The sibling scan found relevant transport, evaluation and editor-skill knowledge; one bounded C1 clarification would separate invocation mechanism from request origin without absorbing neighbouring domains.

## Scope and evidence basis

This is an advisory adjacency report, not a C1/C2 verdict or an integration. The frozen assignment and `plans/round-55.md:18-41` were read first. No product file, sibling file, counter, Git index or JJ state was changed. Only this report was written.

All evidence paths below are relative to `/home/vgpnk/Projects/shokunin/`, unless a command explicitly declares another cwd. Sibling evidence is the local document content inspected, not a fresh replay of its historical observations. Current-round source reports are proposal evidence, not independently reopened sources.

Enumeration used `functions.glob` with `path=/home/vgpnk/Projects/shokunin/*-shokunin/SKILL.md`, `hidden=true`, `gitignore=false`. The sibling search covered each enumerated lane's `SKILL.md` and recursive `corpus/knowledge/`:

- kotodama, kengaku, tameshi;
- kake, kumitate, kaidoku;
- chousa, mado, kama;
- tsukuroi, mori, souji, kagi;
- tabi, lore, kasegi, game-dev-3d.

Kotoba's own relevant entries and the round-55 build cache were read separately. An initial fleet-wildcard grep timed out after 30 seconds; that result was not treated as absence. Searches were reissued against the explicit lane paths in the groups above with `gitignore=false`, then relevant matches were read with line selectors. The focused passes returned no pagination footer requiring continuation.

Principal search pattern:

```text
(?i)(explicit.{0,50}(invok|invoc|activat|trigger)|implicit.{0,50}(invok|invoc|activat|trigger|measur)|slash.command|skill.tool|use_skill|activate_skill|\$skill|@skill|(?-i:/skills?(?:[ :`]|$))|\bskill\s*\()
```

Follow-up searches covered `mention` near `skill`/client names, `allow_implicit_invocation`, `disable-model-invocation`, `read_skill`, `get_skill`, `list_skills`, `AgentSkillToolset`, `$ufo`, and generic `$<...>` / `@<...>` / `#<...>` shapes. These are bounded lexical searches, not proof that differently worded knowledge cannot exist.

## Which lane holds what

| Lane | Located knowledge | Evidence and limit |
|---|---|---|
| **kumitate** | Substrate-specific slash entry points: OMP `/skill:swarm`, Devin `/swarm`, Kimi `/tower.swarm`; the parent may read a child skill rather than recursively discovering it. | `kumitate-shokunin/corpus/knowledge/kimi-modes-machinery.md:75-88`. Its own evidence legend at `:7-14` explicitly distinguishes skill-document statements from observed runtime execution. These forms are not interchangeable client syntax. |
| **kumitate** | Invocation text can be injected by transport: a fresh spawn receives `/skill:godspeed`; resume is distinguished. The wave producer names that prefix `GODSPEED_INVOCATION`. | `kumitate-shokunin/corpus/knowledge/kimi-modes-machinery.md:145-149`; `kumitate-shokunin/corpus/knowledge/swarm-wave-lifecycle.md:85-92`. These are local records of their cited substrate revisions, not a new observation that the present hooks ran. Ownership is orchestration/tooling (`kumitate-shokunin/SKILL.md:2-10`). |
| **kumitate** | A skill author's trigger text names both `/ufo` and `$ufo`. It separately records discovery precedence and name deduplication. | `kumitate-shokunin/corpus/knowledge/kimi-skills-plugins.md:130-139,424-453`; `kimi-modes-machinery.md:281-286`. The dollar form is quoted **frontmatter trigger language**, not first-party proof of a universal client parser. Listing precedence is not invocation-origin measurement. |
| **kengaku** | A model can emit a `skill` tool request under `tool_choice:auto`; the recorded repeat probe emitted `skill(name="min_stack")`. Changing system/tools changes the observed output class. | `kengaku-shokunin/corpus/knowledge/bench-arena-round7-scaffold-ablation.md:15-25,54-67`. The note says the original runner saved only `content`, so original per-cell call names were inferred from `finish_reason`; the repeat probe supplied the concrete name. This does not establish a successful load or a user-issued explicit request. `kengaku-shokunin/SKILL.md:299-310` distills the harness warning; its frontmatter `:3` reserves prompt/skill craft to kotoba and keeps measured capability effects in kengaku. |
| **game-dev-3d** | Unreal project skills have a separate namespace: discover with `AgentSkillToolset.ListSkills`, then load relevant instructions with `AgentSkillToolset.GetSkills` through `call_tool`. The documented selection is based on relevance of the description. | `game-dev-3d-shokunin/corpus/knowledge/unreal-mcp/upstream/skills/unreal-mcp/SKILL.md:36-46`. The companion explicitly distinguishes these from Claude Code harness skills at `upstream/skills/unreal-skill/SKILL.md:3`, and distinguishes description from instruction payload at `:37-45`. The subtree is read-only documentation, not a live-editor integration (`unreal-mcp/README.md:8-10,23-29`). |
| **kaidoku** | A historical provenance investigation records an actual user prompt containing `/write-goal` and `/skill:godspeed`. | `kaidoku-shokunin/corpus/knowledge/2026-10-13-r3-jq-provenance.md:24-33,124-135`. This is a retained account of a Kimi session, not a client-invocation reference or an implicit-trigger evaluation. Keep the installation-provenance question in kaidoku. |
| **kotodama** | The similar name is explicitly disambiguated: linguistic-cultural worldbuilding is its domain, and prompt/skill craft routes to kotoba. | `kotodama-shokunin/SKILL.md:3,8-18`. Search hits for ancient divine “invocation” are not agent-skill knowledge. This routing agrees with `kotoba-shokunin/SKILL.md:10-18`; no ownership contradiction was found. |
| **tameshi** | Owns hermetic suites, mutation testing and gate fixtures, not a located client invocation inventory. | `tameshi-shokunin/SKILL.md:3`. Its “explicit child invocation” hit at `:1612` concerns a verifier's child process, not a named agent skill. Any new reusable classifier-fixture method would belong there, but no such work is proposed here. |

The bounded searches did not locate a relevant explicit-skill-form or implicit-versus-explicit activation-measurement entry in **kake, chousa, mado, kama, tsukuroi, mori, souji, kagi, tabi, lore or kasegi**. Hits there concerned other meanings of invocation, skill-file paths, generic mention sweeps or unrelated tool processes. This is a corpus-search result, not a claim that any client is silent, and not a Q30 docs/release/source-tree silence sweep.

The follow-up glyph search also surfaced important non-examples: `@agent_skill` is a Python decorator (`game-dev-3d-shokunin/corpus/knowledge/unreal-mcp/upstream/skills/unreal-skill/SKILL.md:53,68`); `@<l1Alias>` is a model-route placeholder (`kumitate-shokunin/corpus/knowledge/native-trial-launch.md:116`). Neither is a user skill mention. No sibling evidence located here supplies C1's new per-client source rows.

## Compatibility and explicit tensions with C1

1. **No demonstrated syntax contradiction in the inspected user-form drafts.** The current cache proposes Claude Code `/skill-name` (`kotoba-shokunin/.ufo/waves/round-55/build/SrcClaudeCode.md:15-17`), Codex `$setup-demo-app` (`SrcCodex.md:25-31`), VS Code `/webapp-testing` (`SrcVSCode.md:37-41`), Copilot CLI `/frontend-design` (`SrcCopilotCLI.md:21-25`), Cursor `/skill-name` (`SrcCursor.md:38-41`), and opencode V2 `@skill-id` (`Srcopencode.md:23-27`). These are peer-proposed records; this seat did not fetch their pages or verify their predicates. There was no Gemini source report in the inspected source-report enumeration, so no Gemini row is assessed here.

2. **Old model-call syntax is not a counterexample to a new user form.** Kengaku's historical `skill(name=...)` and C1's proposed opencode V2 `@skill-id` concern different layers and eras. The current source report itself distinguishes V2's `id` input from V1's `name` example (`Srcopencode.md:5-7`). Do not replace the user form with the old call shape or treat the difference as a broken contract.

3. **Invocation mechanism and selection origin must not be collapsed.** The frozen C1 docstring permits either a user-typed form or a model-called tool (`kotoba-shokunin/verifiers/check_explicit_invocation.py:5-9,27-29`), but the learning question is implicit, description-routed activation. [INFERENCE] A model's skill-load call can implement description-based selection; its existence alone does not establish that the user explicitly requested the skill. The Unreal document gives a concrete description → GetSkills workflow, while kengaku demonstrates a model-generated request with incomplete execution evidence. Thus a blanket action “exclude every skill-tool call as user-explicit” would conflict with the measurement question. The currently inspected user-form actions do not make that blanket claim.

4. **Transport-explicit is not human-selected, and neither is an implicit-routing success.** Kumitate's injected prefix means a slash token can originate outside the human request. Kotoba already encountered this contamination: its round-6 method stripped invocation tokens and injected directives after an injected blob caused a false token cluster (`kotoba-shokunin/corpus/knowledge/trigger-miss-proxy-round6.md:11-20`). That historical method still calls implicit-intent fidelity unmeasured and warns that per-session is not per-prompt (`:69-79`). A new documentation inventory must not be described as closing that measurement gap.

5. **Tool request is not observed completion.** Kotoba's existing telemetry uses `tool='skill'` rows as the load signal (`kotoba-shokunin/corpus/knowledge/skill-activation-telemetry.md:50-58`). Kengaku's emitted request and Unreal's documented loading API cannot independently certify that same runtime event. [INFERENCE] Excluding every such row merely because it uses a tool would remove the existing observation channel, not identify the desired denominator.

6. **“New ground” is lane-local, not fleet-global novelty.** The frozen definition scans kotoba's base `SKILL.md` and `corpus/knowledge/*.md` for the matched token (`check_explicit_invocation.py:50-52`; `plans/round-55.md:33-34`). Sibling `/skill:…`, `$ufo` or editor-tool knowledge neither changes that predicate nor licenses a claim that nobody in the fleet held invocation knowledge before round 55.

These are separate compatibility statements and measurement tensions, not a combined score. The counter's acknowledged semantic limit remains unchanged (`check_explicit_invocation.py:54-68`).

## One bounded proposed move

**Attach one shared request-origin rule to C1's table, rather than treating the form column as an activation classifier.** Suggested wording for L1 consideration:

> These forms identify invocation mechanisms, not selection origin: set aside turns explicitly requesting a named skill, including transport-injected directives; a model skill-load call alone does not establish explicit user intent or successful loading. Dispatch provenance belongs to kumitate; this table inventories documentation, not measured implicit activation.

This is a proposal, not an applied rule or a new claim predicate. Keep the existing client rows and frozen four-column header. If a model-tool row is used, its Action should refer to this distinction rather than automatically excluding every tool call. A quoted example, a decorator or a tool definition is not itself an invocation request.

**Should the table name a neighbour?** Yes: name **kumitate** once in this shared action note for transport provenance, not as another client row. Keep **kengaku** (harness/capability effects) and **game-dev-3d** (in-editor project-skill namespace) as located adjacency pointers in this report or the entry's limits, not copied protocols or new client forms. **Kotodama needs no C1 row**: its existing anti-trigger already routes this work to kotoba. No sibling corpus is absorbed and no ownership transfer is implied.

The note should replace equivalent introductory/action boilerplate rather than force extra SKILL lines: the plan pins the 600-line ceiling (`plans/round-55.md:12-14`). No new column, fixture implementation, runtime integration, source-row substitution or verifier change is part of the move.

## Affected axes and second-order effects

| Surface | Expected effect and boundary |
|---|---|
| **Adjacency; C1 depth** | [INFERENCE] A named transport owner and an actionable origin distinction improve the usefulness of C1 without importing orchestration or editor-skill work. No axis gain was measured here. |
| **Consistency and calibration** | [INFERENCE] Preserves the distinction among documentation, request, load signal and intent attribution; avoids promoting a seven-client inventory into measured implicit fidelity or fleet-global novelty. |
| **Runtime** | No client command, model call, editor connection or dispatch is added. Kengaku's historical calls and Unreal's documentation remain evidence of their stated scopes, not newly executed behavior. |
| **Contract** | C1's clients, table anchors, targets, new-row/quote rules and frozen counter remain untouched. Neighbours are not extra client rows. Both claims remain causally separate. |
| **Substrate** | OMP/Kimi transport syntax and Unreal project-skill tools remain outside the seven-client table. Different request origins and tool namespaces are not unified into a synthetic portable API. |
| **Verification / C2 operability** | The same C1 predicate still measures sourced records and quote presence, not classification. No C2 gate, judging line, self-test, counter or `verify_surfaces.py` change follows. A C2 pass is not claimed. |

Risks: the added note can consume scarce SKILL lines; neighbour documents are revision-bound and must not become fresh client guarantees; a text-only rule still does not implement origin attribution; and merely seeing an invocation-shaped token in a quoted passage is not a request. No freshness or broader coverage improvement is claimed.

## Verification and handoff

Performed: local `glob`, `grep` and ranged `read` inspection, plus bounded `date`/`sha256sum` fact commands. No lane code, gate, self-test, classifier, C1/C2 counter or runtime was executed, so no sandbox clone was needed. No external source was fetched; HTTP status, fetched-page byte count and external-source access hashes are therefore not applicable to this seat. No tools were installed or updated.

Observed time command, cwd `kotoba-shokunin/`:

```text
timeout 10 date -u
Thu 22 Oct 2026 11:15:28 PM UTC
```

The successful fact calls did not print numeric exit codes; none is asserted for them. An attempted explicit-status wrapper was unavailable and supplied no date result:

```text
timeout 15 /usr/bin/time -f 'exit=%x' date -u
error: command not found: /usr/bin/time
Command exited with code 127
```

That optional helper was not installed; its absence does not block document inspection. No process started by this seat remains running.

Selected local evidence-byte pins, from `timeout 30 sha256sum` on these exact paths with cwd `kotoba-shokunin/`:

```text
1b4efe0f83fafe57c208076a23c9a42b111e2c1de4688c342215938c9fe8fd53  ../kotodama-shokunin/SKILL.md
d904b0d21a87453e12b3ad83fdb91040f09836c13a9f86313f983bfb756fddc7  ../kumitate-shokunin/corpus/knowledge/kimi-modes-machinery.md
4a4c0855749555ab6273ff55768640d7b2d5d89566645c64ab16613e099fd9b1  ../kumitate-shokunin/corpus/knowledge/kimi-skills-plugins.md
e510cc2fbadede89f0317147a8aadf41e14c90251ec114246fb7265c3791222f  ../kumitate-shokunin/corpus/knowledge/swarm-wave-lifecycle.md
b1c9bd99a3a973c982021c84e27ffea0f12b4bc359dc5b17ee1096144dc815d0  ../kengaku-shokunin/corpus/knowledge/bench-arena-round7-scaffold-ablation.md
6d5c211bca9700530ed8029941090a518d13f9ad7c42853192f2320835471bc2  ../kaidoku-shokunin/corpus/knowledge/2026-10-13-r3-jq-provenance.md
7ef8b991a82f591c5776bb5fa167c2bc2269fd00338ed3e8534eacc551d038fa  ../game-dev-3d-shokunin/corpus/knowledge/unreal-mcp/upstream/skills/unreal-mcp/SKILL.md
7a0af781c458c7d192d6b23c16b5737922dc482470e2e4ef617bcda80f435087  ../game-dev-3d-shokunin/corpus/knowledge/unreal-mcp/upstream/skills/unreal-skill/SKILL.md
```

**Main's verification if integrating the proposed note (not run here):**

- Read the integrated Action cells against four distinct cases: actual user command/mention; transport-injected invocation; model-selected skill-tool request; token quoted as documentation. The wording must not silently equate those cases or claim a successful load without its observation.
- Check that the table still contains only the seven frozen clients, the four-column header remains exact, and the SKILL line ceiling is respected.
- Run the unchanged frozen C1 `--rev <integrated-rev> --fetch` predicate in Main's own permitted sandbox, under `timeout 900`, and record its actual exit and F/K/G output. A green result would still not verify request-origin classification.
- Keep C2 judging surfaces, both counters, neighbouring files and `verifiers/verify_surfaces.py` intentionally unchanged by this proposal.

Report: .ufo/waves/round-55/build/ConnSiblingOverlap.md
