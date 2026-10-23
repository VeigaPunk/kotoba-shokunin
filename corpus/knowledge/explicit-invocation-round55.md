source: S065 (https://code.claude.com/docs/en/skills.md, `skills.md:547`), S066 (https://developers.openai.com/blog/eval-skills.md, `eval-skills.md:148`), S067 (https://code.visualstudio.com/docs/agent-customization/agent-skills.md, `agent-skills.md:287`), S068 (https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills.md, `add-skills.md:128`), S069 (https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/tutorials/skills-getting-started.md, `skills-getting-started.md:127-129`), S070 (https://cursor.com/docs/skills.md, `cursor-skills.md:175`), S071 (https://raw.githubusercontent.com/anomalyco/opencode/3d213123cdf574e55f88711554edfe6fd66a95ad/services/www/src/docs/content/skills.mdx, `skills.mdx:201`)
verified-at: 2026-10-22
recheck: python3 -B verifiers/check_explicit_invocation.py --rev <rev> --fetch

# Explicit invocation by client (round 55)

What seven clients' own documentation says a user types to invoke one named skill directly — or, for
Gemini CLI, the tool the model calls to load one — and what that means for a measure of implicit
(description-routed) activation. Every row quotes a page opened on 2026-10-22 in round 55
(`../SOURCES.md` S065–S071; fetch records in `../lessons/round-55.md` § Gate and the seat reports
`../../.ufo/waves/round-55/build/Src*.md`). These are documentation statements, not measured client
behaviour.

Frontier row: *Implicit-intent fidelity* (`../README.md` § Frontier). The lane's literal-trigger proxy
(`trigger-miss-proxy-round6.md`) covers only prompts that name a skill; an implicit-intent measure has to
set those turns aside first, and the per-client form below is what identifies them.

## Per-client record

| client | row | quote | location | reading |
|---|---|---|---|---|
| Claude Code | S065 | "You can type `/skill-name` to invoke it directly, and Claude can load it automatically when relevant to your conversation." | `skills.md:547` | Typing the slash form invokes the named skill directly; the same sentence says Claude may also load it automatically. |
| Codex | S066 | "Use the $setup-demo-app skill to create the project in this directory." | `eval-skills.md:148` (inside a `codex exec` prompt string) | The prompt names the skill with `$`; the page calls this an explicit-invocation prompt (`:171-172`). |
| VS Code | S067 | "You can add extra context after the slash command. For example, `/webapp-testing for the login page` or `/github-actions-debugging PR #42`." | `agent-skills.md:287` | Selecting or typing the skill's slash command invokes it (`:285`); extra task context may follow the command. |
| Copilot CLI | S068 | "Use the /frontend-design skill to create a responsive navigation bar in React." | `add-skills.md:128` (body of a fenced example; direction at `:125`) | The slash-prefixed skill name in the prompt tells Copilot to use that skill (`:125`); otherwise Copilot decides from the prompt and the skill's description (`:121`). |
| Gemini CLI | S069 | "description and calls the `activate_skill` tool." | `skills-getting-started.md:127-129` | The model calls the tool after the request matches a skill description; the tutorial then asks the user to consent. It is not a user-typed form. |
| Cursor | S070 | "When `true`, the skill is only included when explicitly invoked via `/skill-name`. The agent will not automatically apply it based on context." | `cursor-skills.md:175` | Typing `/` plus the skill name in Agent chat invokes it for one message (`:29`); with the flag set the agent will not apply it from context, though the same page lets any skill back a Custom Mode that keeps it in context all session (`:218`, falsify seat `ReopenS070`). |
| opencode | S071 | "To load a skill yourself, mention it in your prompt as @skill-id." | `skills.mdx:201` (the source wraps `@skill-id` in backticks; stripped here as the counter's page normalisation does) | A user mention of the skill's ID loads it; `opencode/autoinvoke: false` hides it from the model's list but keeps this path (`:142`). |

## Findings

1. **Six clients document a user-typed form; they use three sigils.** A `/` before the skill name in
   Claude Code (S065), VS Code (S067), Copilot CLI (S068) and Cursor (S070); a `$` mention in Codex (S066);
   an `@` mention of the skill ID in opencode V2 (S071). VS Code and Copilot CLI show task text after the
   name in the same turn, so "starts with `/name`" and "holds `/name`" differ: the action cells say which.
2. **Gemini CLI's documented form is the model's tool call, not the user's.** The tutorial's sequence is a
   description match, then the model calls `activate_skill`, then the user is asked to consent (S069). A
   transcript that shows `activate_skill` therefore records a consent-gated load request, and says nothing by itself about
   whether the user named the skill. The pages the seat read (`skills.md`, `using-agent-skills.md`, the
   tutorial) show no user-typed invocation form; that is "not found on those pages", not a Q30 negative —
   the changelog sweep was not run.
3. **Six of seven clients pair the explicit form with an automatic-invocation switch that keeps it** (Copilot CLI's `disable-model-invocation`, S031 `:1278`, and Codex's below were held at base; only Gemini CLI has none in the pages read). Claude Code
   `disable-model-invocation: true` (S065 `:577`), VS Code `disable-model-invocation: true` (S067 `:151`),
   Cursor `disable-model-invocation: true` (S070 `:175`) and opencode `opencode/autoinvoke: false` (S071
   `:142`); Codex's `allow_implicit_invocation: false` (S021, round 51) does the same. A skill with that switch
   set can only appear in explicit turns, so it belongs outside any implicit-trigger denominator.
4. **The form is a mechanism, not the request's origin** (sibling scan, `ConnSiblingOverlap.md`): an
   orchestrator or an injected dispatch directive can put `/name` into a turn too. The table identifies turns where the
   skill was named; who named it is a separate question this entry does not answer.

## Relation to what the lane already held

Round 51 held the switches that remove a skill from automatic choice (`skill-overlap-levers-round51.md`)
and, with them, four of the forms: Codex's "explicit `$skill` invocation still works" (S021), Copilot CLI's
`/SKILL-NAME` (S031, `SOURCES.md:44` at `f0e5de82`), and VS Code's "manual `/` invocation only" and Claude
Code's "`/name` still works" (`SKILL.md:432-433` at `f0e5de82`). Round 6 already stripped slash tokens as
"invocation verbs, not router intent" (`trigger-miss-proxy-round6.md:14-16`). New here (falsify seat
`CriticNewGround`): Cursor's form (S070), opencode V2's `@skill-id` mention (S071; the V1 page states only
loading by exact name), Copilot CLI's slash name inside a prompt rather than at its start (S068 `:125`), the
Gemini CLI distinction between a model load call and a user-typed form, and the per-client form used as a
classifier for measurement. The counter's `new ground 4` counts example tokens; in substance the new forms
are Cursor's and opencode V2's.

## Limits

- The counter (`../../verifiers/check_explicit_invocation.py`, v2 after plan erratum 1) checks that each SKILL.md
  row's backticked token is one user-typed segment after `/`, `$` or `@` and not a client built-in or listing
  command, that it occurs verbatim in a quote holding the word `skill` and recorded in the lesson Gate, from a
  new tier-A row on a pinned host, and with `--fetch` that the quote is on the live page. It does not judge
  whether a form is explicit invocation; that is the reading above and reviewer judgment (Q31). Two rows are
  not counted by it: Gemini CLI (a model tool call, not a user-typed token) and VS Code (its quote holds the
  token but not the word `skill`); both stay in the table on the reading above.
- Codex's quote is an example inside vendor guidance on evals, not a reference page; the general `$` rule
  is stated in S021 (round 51), whose page was already a row at base.
- No client behaviour was run or measured; the seven clients are the lane's pinned set, not all clients.
- opencode's quote strips the source's inline backticks; Gemini CLI's quote is a clause from a numbered
  step. Both are stated where quoted.
