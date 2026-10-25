# ScoutClientRuns — round 70 wave 1

Seat: `L1Kotoba70.ScoutClientRuns` (scout, read-only). Lane tip read: `16b212a390c7ce68b6bce49b2c3766b154fbcbae`.
Target: `corpus/knowledge/skill-eval-artefacts-round70.md:60-61` — "No claim is made that any client *runs* `evals/evals.json` automatically — none of the three sources says so, and the lane has not observed it."

## Verdict

**The negative holds as worded, but it needs a qualification.** None of the seven clients reads or executes `evals/evals.json` or a `should_trigger` file natively or automatically. No doc page or client source says so, and grepping four open-source client trees found zero matches.

There is one documented near-miss that the entry should name:

- **The `skill-creator` plugin.** Claude Code's own skills page documents an official Anthropic plugin, `skill-creator@claude-plugins-official`. It "automates the comparison loop inside Claude Code": it stores test cases in `evals/evals.json` and generates should-trigger and should-not-trigger sets.
  - It is a plugin, not native Claude Code behaviour. It runs only after the user installs it and asks for it.
  - Its trigger runner is byte-identical to S211, sha256 `43e3b8f8…`. The runner launches `claude -p` once per query.
- **The native `claude plugin eval` command.** Claude Code also ships this native eval runner. It uses a different, per-case directory format, and the docs say "neither tool reads the other's case files."

A reader who takes "client runs evals.json" broadly, meaning "an official, client-documented component executes it," would count this as counter-evidence. The current justification ("the lane has not observed it") is now the weaker half of the sentence. The suggested wording is under Recommendation.

## Counter-evidence and qualifying evidence (URL + located quote)

| # | Client | URL | Quote (snapshot line) | Reading |
|---|---|---|---|---|
| E1 | Claude Code | https://code.claude.com/docs/en/skills.md | "For iterating on a single skill inside a Claude Code conversation, the skill-creator plugin below runs a similar loop with its own `evals/evals.json` format. The two formats aren't interchangeable." (`cc-skills.md:964`) | **Qualified counter-evidence.** A client's official docs say an official plugin runs an `evals.json` loop. |
| E2 | Claude Code | same | "The [`skill-creator` plugin] automates the comparison loop inside Claude Code." (`:968`) · "**Test cases**: stores prompts, input files, and expected behavior in `evals/evals.json` inside the skill directory" (`:981`) · "**Description tuning**: generates should-trigger and should-not-trigger prompts, measures the hit rate" (`:986`) | Same plugin. It is user-invoked: "ask Claude to evaluate an existing skill, for example `evaluate my summarize-changes skill with skill-creator`" (`:979`). It is not automatic on load. |
| E3 | Claude Code (native) | https://code.claude.com/docs/en/plugin-evals.md | "the skill-creator plugin runs a similar comparison with its own `evals/evals.json` format, and neither tool reads the other's case files." (`cc-plugin-evals.md:19`) | **Supports the negative** for native Claude Code. `claude plugin eval` reads `evals/<case>/prompt.md`, `case.yaml` and `graders/`, not `evals.json`. |
| E4 | Claude Code plugin source | https://github.com/anthropics/claude-plugins-official/tree/58267944f92187b7d6a1c822165c96c81c864806/plugins/skill-creator | `SKILL.md:145` "Save test cases to `evals/evals.json`." · `SKILL.md:343` `{"query": "the user prompt", "should_trigger": true}` · `scripts/run_eval.py:232` `did_pass = trigger_rate >= trigger_threshold` · `:261` `--eval-set ... required=True` | The plugin's runner takes an explicit `--eval-set` path. Nothing auto-discovers the file. `sha256(run_eval.py)` = `43e3b8f80dbf…` for both the plugin and S211 at `dbd4588`, so they are byte-identical. |
| E5 | Claude (platform docs) | https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices.md | "There is not currently a built-in way to run these evaluations. You can create your own evaluation system." (`plat-bp.md:778`) | **Supports the negative.** This covers Anthropic's own evaluation-structure example, which is not the `evals.json` schema. |
| E6 | Codex | https://developers.openai.com/blog/eval-skills (already lane row S066) | "an initial `evals/setup-demo-app.prompts.csv` might look like this: `id,should_trigger,prompt`" · "use `codex exec --json` so your eval harness can score what actually happened" · "For each prompt, run `codex exec --json --full-auto "<prompt>"`" | **Supports the negative.** `should_trigger` lives in a user CSV that a user-written harness reads. Codex itself does not read it. |
| E7 | agentskills.io (spec owner) | https://github.com/agentskills/agentskills/issues/238#issuecomment-4068218457 (jonathanhefner, 2026-03-16) | "the evals guide … is intended to be non-normative. So `evals/evals.json` isn't officially a part of the specification" | **Supports the negative.** A conforming client has no obligation to read the file. |
| E8 | agentskills.io (S209 itself) | https://agentskills.io/skill-creation/evaluating-skills.md | "The `skill-creator` Skill automates much of this workflow — running evals, grading assertions, aggregating benchmarks" (`as-eval.md:300`). S210 `as-opt.md:167` says the same for the trigger loop. | **Wording risk.** S209 and S210 do say the runs are automated, but by a *skill*, not a client. "None of the three sources says so" stays true only on the skill/client distinction. |

No counter-evidence was found for VS Code/Copilot, Cursor, Gemini CLI or opencode. See the sweep below.

## Sweep log

Scratch: `/tmp/k70w1-ScoutClientRuns.AU41`, deleted before return. Fetched 2026-10-25 ~11:57–12:10Z with `curl -sSL -A Mozilla/5.0`. HTML was converted to text by stripping tags. Hits were counted with `rg -c -i`.

### A. Official docs fetched (33 distinct pages)

Columns: hits for `evals\.json` / `should[_-]trigger` / `\beval`.

| Client | Page (HTTP 200, bytes) | json | trig | eval | Screen |
|---|---|---|---|---|---|
| agentskills.io | llms.txt (1 374), home (3 225), specification (7 608), clients (282), quickstart (4 080), best-practices (15 060), using-scripts (12 078), adding-skills-support (20 446) | 0 | 0 | 0–4 | `eval` hits are cross-links to the eval guide plus one `scripts/evaluate.py` example path. The client-implementation guide never mentions evals. |
| agentskills.io | evaluating-skills (16 973, sha `a799805f…` = S209 snapshot) | 6 | 0 | 33 | Authoring guidance. A skill (skill-creator) automates it (E8). |
| agentskills.io | optimizing-descriptions (13 403, sha `7cc54fbb…` = S210) | 0 | 14 | 8 | Same as above. |
| Claude Code | llms.txt (63 682), skills.md (118 172, sha `acb1f138…`), plugin-evals.md (63 948, sha `4505c07d…`), plugins-reference.md (43 117), cli-reference.md (51 769), whats-new/2026-w37.md (4 925) | 2 / 1 on skills.md; 1 on plugin-evals | 1 on skills.md | 1–79 | **E1–E3** |
| Claude (platform) | agent-skills/best-practices.md (42 155, sha `a1145a06…`), agent-skills/overview.md (21 852) | 0 | 0 | 10 / 0 | **E5** |
| Anthropic blog | claude.com/blog/improving-skill-creator-… (585 760) | 0 | 0 | 15 | "available now in Claude.ai and Cowork, as a plugin for Claude Code". A plugin, consistent with E2. |
| Codex | llms.txt (33 664), /codex/skills HTML (418 399) + skills.md (11 035, sha `ed6e324f…`), blog/eval-skills (387 509, sha `b412d001…`) | 0 | 0 on skills; 2 on blog | 0–7 | The `eval` hits on the skills page are sidebar links to OpenAI platform Evals. **E6** |
| VS Code / Copilot | code.visualstudio.com/docs/agent-customization/agent-skills (157 088, sha `62ff3a26…`; the old `/docs/copilot/customization/agent-skills` URL served the identical byte count), docs.github.com/en/copilot/concepts/customizations/agent-skills (566 002) | 0 | 0 | 0 | No eval feature documented. |
| Cursor | llms.txt (24 919), docs/context/skills (487 868, sha `1f6ced7d…`), docs/agent-sdk/evals.md (7 553, sha `54c380fe…`; redirected from `/docs/bdk/evals`) | 0 / 0 / 1 | 0 | 0 / 0 / 40 | Excluded. The Agent SDK `bdk eval` reads `evals/*.eval.ts` ("Evals live in the project-root `evals/` directory, beside `bot/`", `:39`), and its one `evals.json` is CI *output* (`> reports/evals.json`, `:170`). It does not evaluate skills. |
| Gemini CLI | geminicli.com/docs/cli/skills/ (114 148, sha `b1789501…`), llms.txt (968 590) | 0 | 0 | 2 / 65 | Excluded. All `evals/` hits are Gemini CLI's own Vitest behavioural evals (`evals/<name>.eval.ts`, llms.txt:1522-1679), not skill evals. No line combined `eval` with `skill`. |
| opencode | opencode.ai/docs/skills/ (71 581), /v2/docs/skills/ (34 294), llms.txt (3 999) | 0 | 0 | 0 | No eval feature documented. |

### B. Client source trees (shallow clones at HEAD on 2026-10-25)

Command: `rg -l -i --hidden -g '!.git' <term>` per repo. Files matched:

| Repo @ commit | `evals\.json` | `should_trigger` | `shouldTrigger` | `should-trigger` | `evals/evals` |
|---|---|---|---|---|---|
| openai/codex @ `970111f6` | 0 | 0 | 0 | 1 | 0 |
| google-gemini/gemini-cli @ `cd1b45c2` | 0 | 0 | 1 | 0 | 0 |
| anomalyco/opencode @ `49a112f1` | 0 | 0 | 1 | 0 | 0 |
| microsoft/vscode @ `4f383697` (contains `extensions/copilot`; `microsoft/vscode-copilot-chat` is archived) | 0 | 0 | 5 | 0 | 0 |

All 8 files screened out as unrelated identifiers:

- `codex-rs/app-server-test-client/src/lib.rs:872`: `touch /tmp/should-trigger-approval`.
- gemini-cli `mcp-client.ts:2010`: `shouldTriggerOAuth`.
- opencode `onboarding/index.tsx:28`.
- vscode: `virtualToolGrouper.ts:53` `shouldTriggerBuiltInGrouping`, plus the terminal-suggest, TypeScript-completions/refactor and `chatTipContentPart.ts` autocomplete and setup triggers.

Built-in `skill-creator` skills shipped by clients:

- **Codex** (`codex-rs/skills/src/assets/samples/skill-creator/`): no `evals.json`. It recommends optional "Independent Forward-Testing" with a subagent: "Ordinary creation or small edits do not automatically require subagents" (`SKILL.md:~219`).
- **Gemini CLI** (`packages/core/src/skills/builtin/skill-creator/`): scripts are `init_skill.cjs`, `package_skill.cjs` and `validate_skill.cjs`. There are no eval files. The `trigger` hits concern description wording only.

Cursor is closed-source, so it was checked through docs only.

### C. Web queries (Cursor WebSearch, 7 queries, 5 results each)

1. `"evals.json" skill Claude Code docs`
2. `Codex agent skills evals "evals.json" OR "should_trigger" developers.openai.com`
3. `VS Code Copilot agent skills evaluate skill "evals.json" code.visualstudio.com`
4. `Cursor agent skills evals "evals.json" cursor.com docs`
5. `Gemini CLI agent skills evals "evals.json" OR "should_trigger" geminicli.com`
6. `opencode skills eval "evals.json" opencode.ai docs`
7. `agentskills.io "evals.json" client runs evals automatically`

### Counts

- **Identified:** 33 official doc pages + 5 source trees (four clients and `claude-plugins-official`) + 35 web results. The web results are 31 distinct URLs after removing four duplicates: AgentV v4 ×2 extra, AgentV docs ×1 extra, NVIDIA ×1 extra.
- **Screened:** all 33 pages, 5 trees and 31 URLs.
  - 15 web URLs were excluded as third-party or off-topic. They are not one of the seven named clients: jamie-bitflight/claude_skills, melodic-software, heshamfs, agentevals.io, shapediver EVALS.md, rlespinasse, snapsynapse, agentv.dev ×2, docs.nvidia.com SkillEvaluator, stackhawk, wpro-eng (jsDelivr), PedroHBO, npm agent-skills-eval, and the OpenAI cookbook.
  - The remaining 16 official URLs are covered by section A or B.
- **Included:** 8 evidence items (E1–E8). Two are qualified counter-evidence (E1, E2, with E4 as the source proof). Four support the negative (E3, E5, E6, E7). One is a wording risk (E8).

### Out of scope, recorded

Some third-party *eval runners* do execute `evals.json` directly, but none of them is an agent client:

- **AgentV:** "AgentV natively supports `evals.json`… `agentv eval evals.json --provider claude`" (https://agentv.dev/docs/v4.42.4/integrations/agent-skills-evals/).
- **NVIDIA SkillEvaluator:** `tier3 evaluate`; "`evals/evals.json` | The eval dataset. Without it, live evaluation cannot run." (https://docs.nvidia.com/skills/skillevaluator/eval-datasets).
- **npm `agent-skills-eval`.**

One more pattern is user-prompted rather than a client feature. ShapeDiver's EVALS.md tells users to prompt VS Code Copilot agent mode to "read evals.json and eval_queries.json".

## Recommendation for the entry (not applied; seat is read-only)

Replace "none of the three sources says so, and the lane has not observed it" with a sourced boundary such as:

> no client runs it natively — Claude Code's own `claude plugin eval` uses a different case format and "neither tool reads the other's case files" (plugin-evals.md); the `evals.json` loop runs only through the user-invoked skill-creator skill or plugin (S209 § Next steps; Claude Code skills.md § Run evals with skill-creator).

That would need new SOURCES rows for `code.claude.com/docs/en/plugin-evals.md` and the skill-creator section of `skills.md` (S065 is an older fetch of the same page). Whether the C2 gate counts this as a scope change is a question for the closure seat. It does not alter F1–F8.

## Tooling

No installs or updates. Used the existing curl, git, rg, fd, gh (authenticated as VeigaPunk), python3, and the Cursor WebSearch tool.
