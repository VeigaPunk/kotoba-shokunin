HOLDS-BOUNDED — C2 counts as the round's learning claim (a stronger entry superseding round-50 finding 4, plus a SKILL.md table, on PROVINCE Core ground "sibling arbitration"), but only if the entry and table carry four bounds: the Claude Code row is labelled carried rather than new, a sentence says no lever is a tie-break, a "held by" column, and an "effect" column. Without them the table reads as a tie-break and claims credit for knowledge the lane admitted in rounds 49 and 50.

Seat: KotobaR51.CriticLearning (critic, build wave, round 51). Base `43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10`. Started 2026-10-22T14:18Z. No tools installed. No lane files written except this report.

## Findings

F1 — Partly new ground, partly a restatement. The Claude Code row is not new.
- The round-49 census already records both remedies on S022's troubleshooting list: "fixed by a more specific description or `disable-model-invocation: true`" (`corpus/knowledge/sibling-overlap-census-round49.md:32`, citing `skills.md:1190-1195`). The round-50 entry's craft paragraph names `disable-model-invocation` and `paths` (`skill-selection-rules-round50.md:54-56`). The round-50 lesson rejects "the only arbitration an author controls is the description" (`corpus/lessons/round-50.md:152-153`).
- Finding 4 cut its own quote short. Its Claude Code citation `skills.md:1194` ("Make the description more specific") is item 1 of a two-item list. Item 2, on the next line, reads "Add `disable-model-invocation: true` if you only want manual invocation" (fetched `cc.md:1194-1195`). So for Claude Code, "superseding finding 4" fixes a citation error the lane had already noted twice and never carried into finding 4 or `SKILL.md:377`.
- What is genuinely new (not in the corpus at `43ca0bfb`; `git grep` counts below):
  (a) six more clients;
  (b) the clients converge on one field the author writes. `disable-model-invocation` is documented by VS Code (`vscode.md:151`) and Copilot CLI (`cliref.md:1278`), and Copilot SDK skill providers are told to map it (`sdk.md:648`). Codex has a renamed equivalent, `policy.allow_implicit_invocation` in `agents/openai.yaml`, which ships inside the skill directory (`codex.md:218`). opencode has `metadata["opencode/autoinvoke"]` (`opencode.md:231`). The corpus has 0 files naming `user-invocable` or `allow_implicit_invocation`;
  (c) the only vendor text that ties a non-wording lever to a conflict: Copilot SDK § Skill conflicts (`sdk.md:805-810`).
- Impacted axes: depth (provenance). Correction: in the new entry, mark the Claude Code row "carried from S022 (census round 49 line 32; round-50 entry lines 54-56)". State the finding-4 truncation as the reason for superseding. Count 6 of 7 rows as new ground. The counter's 7 of 7 still stands, because it counts backing, not novelty.

F2 — No lever answers "two overlapping skills". Each one removes a skill from the candidates. This is the bound the table needs.
- Every lever on the seven opened pages removes one skill from the candidate set, in one of three scopes:
  1. everywhere: Copilot SDK `disabledSkills`; Gemini `/skills disable <name>` "Prevents a specific skill from being used." (`gemini.md:94`); Codex `[[skills.config]] enabled = false` (`codex.md:183-188`); opencode `deny` "Skill hidden from agent, access rejected" (`opencode.md:153`); Claude Code `skillOverrides` `"off"` and `Skill(name)` deny rules;
  2. from automatic choice only, with manual invocation kept: `disable-model-invocation` (Claude Code, VS Code, Copilot CLI), Codex `allow_implicit_invocation: false`, opencode `autoinvoke "false"`;
  3. outside a scope: Claude Code `paths`, "loads the skill automatically only when working with files matching the patterns" (`cc.md:403`), and opencode per-agent permission (`opencode.md:160-170`).
- None ranks two skills that both stay candidates. Where both remain candidates, round-50 finding 1 stands unchanged and the description is still the only lever.
- Strongest counterexample to reading the levers as tie-breaks: the Copilot SDK section is titled "Skill conflicts" but its trigger is "If multiple skills provide conflicting instructions" (`sdk.md:807`). That is a clash in body content after both skills load, not two descriptions matching one prompt. Its remedy is "exclude", which is removal. Claude Code's item 2 is conditional: "if you only want manual invocation" (`cc.md:1195`).
- The effects are not the same across clients. Claude Code says the description is no longer in context (`cc.md:577`). VS Code says only "require manual invocation through the `/` slash command only" (`vscode.md:151`) and makes no statement about context. Codex: "won't implicitly invoke" (`codex.md:218`). A shared "effect" wording must not carry Claude Code's context statement over to the other clients.
- Impacted axes: depth, correctness of `SKILL.md` § Anti-patterns. Correction: one bound sentence directly above the table (text under Draft), and an effect column whose values are exactly `removed everywhere` / `automatic choice off, manual kept` / `outside a scope`. No cell says "wins", "preferred" or "chosen over".

F3 — Who holds the lever decides whether it is craft at all.
- Levers the author holds travel with the skill file: Claude Code (`disable-model-invocation`, `paths`), VS Code and Copilot CLI (`disable-model-invocation`), opencode (`metadata["opencode/autoinvoke"]`), Codex (`agents/openai.yaml` policy).
- Operator-only on the opened pages: Gemini CLI (`/skills disable`, plus `gemini skills disable <name>` in the scribe's copy of `cli-reference.md:130`; `creating-skills.md` frontmatter names only `name` and `description`), and the Copilot SDK (`disabledSkills` is session configuration held by the application developer).
- A table without a "held by" column will be read as "set frontmatter X" for Gemini, where no frontmatter lever is documented.
- Correction: add a `held by` column with values `skill author (file)` or `user/operator (config)`. Where a client has both, list the author-held lever first.

F4 — The lever has a cost: it is not a free substitute for rewriting the description.
- Manual-only or disabled also stops the skill on prompts that only it matches, so it gives up true positives as well as the overlap. `paths` gives them up only outside the glob. A well-split description gives up nothing. VS Code adds that discovery "does not guarantee that it invokes a skill for every relevant prompt" (`vscode.md:64`), so no lever on the other skill guarantees the remaining one fires.
- This sets when to reach for a lever (paragraph below).

F5 — omp, kotoba's own runtime, is not among the 7 pinned clients but honours the same field. This is static evidence; I did not run it.
- In the omp 18.12.6 binary (sha256 prefix `85d9daf3a05fc76e`, matches the pin), `packages/utils/src/frontmatter.ts` rewrites hyphenated keys to camelCase (`e.replace(/-([a-z])/g, (t, r) => r.toUpperCase())`, applied to every key containing "-"; `omp.strings` lines 323879-323900).
- Skill loading sets `hide: B.frontmatter?.hide === true || B.frontmatter?.disableModelInvocation === true` (line 610308). The function that renders the model-facing catalogue starts with `t.filter((i) => !i.disableModelInvocation && !i.hide)` (line 1065981).
- [INFERENCE] So `disable-model-invocation: true` in a SKILL.md removes the skill from omp's model-facing list. omp also accepts an omp-only `hide: true`, and its operator holds `--skills=<glob>` (`omp --help`).
- Not run: confirming the render needs a model call. Route to LeverOmp. It turns the craft rule from portable advice into a capability on the lane's own runtime.

F6 — Risk in the counter (passed to CriticC2Sizing; LeverGuard's code was not visible to me).
- The check "key term appears verbatim in the quote" cannot tell removal from a same-name precedence rule. A row keyed `precedence` that quotes Gemini's "the version from the higher-precedence location is used" (`gemini.md:51-52`) would match. That is the round-50 same-name rule, not an overlap lever.
- Suggested self-test mutant: a row whose quote is a same-name or location precedence sentence must not count.

## Draft — the "What this changes for craft" paragraph I would accept

> Between two skills that both stay candidates, no client documents a rule, so the first fix is still to name the neighbour and the split in the description (`trigger.05`). Every non-wording lever documented here removes one skill from the candidates instead of ranking the two: everywhere (a disable list or deny rule held by the user or operator), from automatic choice only (`disable-model-invocation` in Claude Code, VS Code and Copilot CLI; `allow_implicit_invocation: false` in Codex; `metadata["opencode/autoinvoke"]: "false"` in opencode), or outside a scope (Claude Code `paths`, opencode per-agent permission). Reach for a lever only when the description cannot carry the split: the skill should never fire unasked anyway (side effects, timing), the split is by file location rather than by intent, or you do not own the other skill's file (then the lever is the operator's, not your frontmatter). A manual-only or disabled skill also stops firing on prompts only it matches, and Gemini CLI documents no lever held by the author, so there the description stays the author's only tool.

Bound sentence for directly above the SKILL.md table:

> Each lever removes one skill from the candidates (everywhere, from automatic choice, or outside a path or agent scope); none decides between two skills that both remain candidates, where the description is still the only lever.

Table shape that satisfies the action-cell rule (`SKILL.md:173-177`): `client | lever (action) | held by | effect | quote location`.

## Evidence (commands and exit codes)

- `git -C kotoba-shokunin rev-parse HEAD` → `43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10`, exit 0.
- Count of files at `43ca0bfb` under `corpus SKILL.md PROVINCE.md` naming each term (`git grep -c -F -e <term> 43ca0bfb -- corpus SKILL.md PROVINCE.md | wc -l`), exit 0: `disable-model-invocation` 4, `user-invocable` 0, `allow_implicit_invocation` 0, `disabledSkills` 1 (the spot-check lesson only), `skills disable` 0, `enabled = false` 0.
- Fetches with `curl -sSL -A 'Mozilla/5.0'`, at 2026-10-22T14:19:46Z, into `/fast/scratch/hyaku/kotoba-r51/build/CriticLearning/pages/`, each HTTP 200 (status, bytes, sha256):
  - `https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/skills.md` 200, 35455 B, `64856ff44e5481f3ccb16defbc80180874e463862ac12309ef23b18802d4b9f3` (same bytes as the round-50 spot-check)
  - `https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference.md` 200, 461944 B, `c61997efd7c939324e1f1b846fcb9ed420e5bbfd5eb5319531c6e6210025b5c9`
  - `https://code.visualstudio.com/docs/agent-customization/agent-skills.md` 200, 22871 B, `de5ba34f0c2306af7d1b792581d01f53b4ddd6a912699a19f3a2c958efda3ab5` (matches the S025 recheck)
  - `https://code.claude.com/docs/en/skills.md` 200, 111557 B, `cdfcb0df93072710866de536ba823c06a0804038d488cd27a2ba48ad114cd456` (matches S022)
  - `https://opencode.ai/docs/skills.md` 200, 5365 B, `f10ced73971ce83b85f41395e2e15a683fe5a874e9057fc9d13da5f5a1bf8561` (matches S024)
  - `https://geminicli.com/docs/cli/skills.md` 200, 5763 B, `8e1b4cbe2cd31effa3375aa5d480269ab28bf82c02a42d9b52cbb61e5b248590` (matches S029)
  - `https://developers.openai.com/codex/skills.md` 200, 11035 B, `ed6e324f747d47adf6f60ee1fca13ba469b3671f55f58c3a78f35947af6919d5`
  - Also fetched, not cited above: `cli-plugin-reference.md` 200, 47200 B, `d0d362cc…`; `code.claude.com/docs/en/permissions.md` 200, 86703 B, `b9e93331…`.
- Verbatim quotes, each at most 25 words, by line in the fetched bytes:
  - `sdk.md:807` "If multiple skills provide conflicting instructions:"; `:809` "Use `disabledSkills` to exclude conflicting skills"
  - `cc.md:1194-1195` "Make the description more specific" / "Add `disable-model-invocation: true` if you only want manual invocation"; `:577` "`disable-model-invocation: true` | Yes | Not on its own | Description not in context"
  - `vscode.md:151` "Set to `true` to require manual invocation through the `/` slash command only."
  - `cliref.md:1278` "Prevent the agent from automatically invoking this skill. Default: `false`."
  - `opencode.md:153` "Skill hidden from agent, access rejected"; `:231` "skills set to `\"false\"` are hidden from model-facing guidance"
  - `gemini.md:94` "`/skills disable <name>`: Prevents a specific skill from being used."
  - `codex.md:218` "When `false`, Codex won't implicitly invoke the skill based on user prompt; explicit `$skill` invocation still works."
- `sha256sum /home/vgpnk/.local/bin/omp` → prefix `85d9daf3a05fc76e`; `omp --version` → `omp/18.12.6`, exit 0. `strings -n 8 omp | grep -c -F` → `disableModelInvocation` 7, `disable-model-invocation` 0 (the loop's last grep exited 1 on a 0 count). Full strings dump at `/fast/scratch/hyaku/kotoba-r51/build/CriticLearning/omp.strings`; line numbers above refer to it.
- `timeout 20 omp --help | grep -i -E 'prompt|skill|…'` → shows `--skills=<value> Comma-separated glob patterns to filter skills`, exit 0.
- Not run: any model call or omp render probe, the C2 counter (not landed), and LeverGuard's self-test.
