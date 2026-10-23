Result: DONE — Gemini CLI documents `activate_skill` as model-side, description-routed loading, but no user-typed direct invocation on the pages checked.

## Findings

- **Documented activation form:** Gemini's tutorial describes a user asking a relevant question, then says Gemini matches the request to a skill description and calls `activate_skill`. The form is a model-side tool call, not a documented slash command or other user-typed direct invocation. The tutorial's example request is ordinary task language, not a skill-name command. Pinned source: `docs/cli/tutorials/skills-getting-started.md:123-130`.
- **Classification limit for implicit-intent measurement:** the same sequence places the tool call after description matching. The source supports `activate_skill` as the loading tool, but a tool call alone does not establish that the user explicitly named or requested the skill. Draft action below preserves that distinction rather than treating every description-routed activation as user-explicit.
- **User commands on pages checked:** the skills page and usage guide list `/skills` commands for listing, linking, disabling/enabling and reloading skills; none is documented there as directly invoking one named skill. The tutorial does not give a direct user-typed skill invocation form.
- **Blocking implicit while keeping explicit:** no such selective setting is documented on the pages checked. The usage guide says `/skills disable <name>`: “Prevents a skill from being triggered.” (`using-agent-skills.md:33`). It does not say explicit invocation remains available. The skills page also describes `/skills disable <name>` as preventing a skill from being used (`skills.md:94`).
- **Scope limit:** this is not a claim that no other Gemini CLI page documents a user-typed form. I checked the skills page, its linked usage guide and tutorial, and the corresponding pinned repository documentation. I did not run the full Q30 changelog/release-notes + docs-tree + lane-corpus sweep because a model-side activation tool is documented; no client-wide silence claim is made.

## Quote and draft rows

Byte-exact quote from the pinned source (Markdown backticks retained; quote is the exact text after the source line's four-space indentation):

> description and calls the `activate_skill` tool.

Location: `docs/cli/tutorials/skills-getting-started.md:128` (context at lines 126–129). Six whitespace-separated words; contains the form token verbatim.

Draft SOURCES row (11 cells; `S0NN` is the requested placeholder):

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S0NN | Gemini CLI docs — Get started with Agent Skills (google-gemini/gemini-cli at `a713410aba5d594594e20d5c822e3aab8f822089`) — https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/tutorials/skills-getting-started.md | docs | A | Gemini CLI's documented path from a relevant request to loading a named skill | § How to use the skill (`skills-getting-started.md:121-129`); pinned at upstream main commit `a713410aba5d594594e20d5c822e3aab8f822089`; fetched 2026-10-22T23:15:25Z (200, 5,855 B, sha256 `111e8bfa1b99c2d2e2728864d092728334f73eb4fc9ce2998f6cf6ba3ca1c167`) | The description clause says to call the `activate_skill` tool | mined | 2026-10-22 | on-release | corpus/knowledge/explicit-invocation-round55.md |

Draft entry row:

| client | row | quote | location | reading |
|---|---|---|---|---|
| Gemini CLI | S0NN | "description and calls the `activate_skill` tool." | `docs/cli/tutorials/skills-getting-started.md:127-129` | Model-side tool call after the request matches a skill description; the tutorial then asks the user for activation consent. |

Draft SKILL.md row:

| Client | Explicit form | What it does | Action |
|---|---|---|---|
| Gemini CLI | `activate_skill` | The model calls this tool after matching a request to a skill description; the tutorial then presents an activation-consent prompt. | Do not infer user-explicit intent from this tool call alone; the documented sequence is description match, then model tool call. |

## Fetch and command evidence

All network commands were ordinary `curl` GETs, wrapped with `timeout 900`; files were stored only in the sandbox clone. Each `date -u` line below is pasted from the corresponding run.

- Sandbox preparation: `timeout 900 bash -lc 'unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE; git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r55/SrcGeminiCLI && git -C /fast/scratch/hyaku/kotoba-r55/SrcGeminiCLI checkout -q a10240c0940f770a5f2a5f32a7e3c363dd5d40c0'` → exit 0; no output. Self-test therefore ran from the plan commit in the isolated clone.
- Revision pin: `git ls-remote https://github.com/google-gemini/gemini-cli.git refs/heads/main` → `a713410aba5d594594e20d5c822e3aab8f822089 refs/heads/main`; date line: `Thu Oct 22 11:12:37 PM UTC 2026`.
- URL `https://geminicli.com/docs/cli/skills.md`; command `curl -LsS --output /fast/scratch/hyaku/kotoba-r55/SrcGeminiCLI/gemini-skills.md --write-out "HTTP %{http_code}\n" https://geminicli.com/docs/cli/skills.md` → date `Thu Oct 22 11:12:14 PM UTC 2026`, HTTP 200, curl exit 0, 5,763 B, sha256 `8e1b4cbe2cd31effa3375aa5d480269ab28bf82c02a42d9b52cbb61e5b248590`. This route is already cited by S029; its activation sentence is at line 24.
- URL `https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/skills.md`; command `curl -LsS --output /fast/scratch/hyaku/kotoba-r55/SrcGeminiCLI/github-skills.md --write-out "HTTP %{http_code}\n" https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/skills.md` → date `Thu Oct 22 11:12:14 PM UTC 2026`, HTTP 200, curl exit 0, 5,740 B, sha256 `51e8573ef4c068dbdef5f73bd665c47ab16718aefe4edba365fe333b2d85f96d`.
- URL `https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/skills.md`; command `curl -LsS --output /fast/scratch/hyaku/kotoba-r55/SrcGeminiCLI/github-skills-pinned.md --write-out "HTTP %{http_code}\n" https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/skills.md` → date `Thu Oct 22 11:12:42 PM UTC 2026`, HTTP 200, curl exit 0, 5,740 B, sha256 `51e8573ef4c068dbdef5f73bd665c47ab16718aefe4edba365fe333b2d85f96d`.
- URL `https://geminicli.com/docs/cli/using-agent-skills.md`; command `curl -LsS --output /fast/scratch/hyaku/kotoba-r55/SrcGeminiCLI/using-agent-skills.md --write-out "HTTP %{http_code}\n" https://geminicli.com/docs/cli/using-agent-skills.md` → date `Thu Oct 22 11:14:48 PM UTC 2026`, HTTP 200, curl exit 0, 3,052 B, sha256 `9e61fb7cb289263a102e937849f7019efc860e961da1dbcdf3ce36056e9df708`.
- URL `https://geminicli.com/docs/cli/tutorials/skills-getting-started.md`; command `curl -LsS --output /fast/scratch/hyaku/kotoba-r55/SrcGeminiCLI/skills-getting-started.md --write-out "HTTP %{http_code}\n" https://geminicli.com/docs/cli/tutorials/skills-getting-started.md` → date `Thu Oct 22 11:14:48 PM UTC 2026`, HTTP 200, curl exit 0, 5,866 B, sha256 `b4169fbdc042c4e4b5e02cd215af08035a95e1670d4416d0f624cf7845329f05`.
- Cited URL `https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/tutorials/skills-getting-started.md`; command `curl -LsS --output /fast/scratch/hyaku/kotoba-r55/SrcGeminiCLI/github-skills-tutorial-pinned.md --write-out "HTTP %{http_code}\n" https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/tutorials/skills-getting-started.md` → date `Thu Oct 22 11:15:25 PM UTC 2026`, HTTP 200, curl exit 0, 5,855 B, sha256 `111e8bfa1b99c2d2e2728864d092728334f73eb4fc9ce2998f6cf6ba3ca1c167`. The excerpt at lines 126–129 matches the served tutorial excerpt at the same line numbers.
- Lane citation check: searched `corpus/SOURCES.md` for `skills-getting-started.md|docs/cli/tutorials/skills-getting-started`; no matches. The draft uses a different page from the already-cited S029 skills page.
- Required sandbox check: command `timeout 900 bash -lc 'timeout 900 python3 -B /fast/scratch/hyaku/kotoba-r55/SrcGeminiCLI/verifiers/check_explicit_invocation.py --self-test; rc=$?; printf "exit code %s\n" "$rc"; exit 0'` → `self-test: 0 failure(s) over 29 assertions`; inner command exit code 0.

## Gates, touched surfaces, and limits

- **Gate exercised:** only `check_explicit_invocation.py --self-test` in the sandbox, exit 0. The C1 `--fetch` predicate was not run; no predicate pass is claimed.
- **Touched lane surface:** this report only: `.ufo/waves/round-55/build/SrcGeminiCLI.md`.
- **Sandbox artifacts:** clone at `/fast/scratch/hyaku/kotoba-r55/SrcGeminiCLI/` (plan commit `a10240c0940f770a5f2a5f32a7e3c363dd5d40c0`), fetched documents listed above, and self-test execution. No lane code, counter, `SKILL.md`, `corpus/SOURCES.md`, knowledge entry, lesson, or Git state was edited. No package was installed or updated.
- **Out of scope:** no full Q30 sweep, no C1 `--fetch` run, and no conclusion about Gemini CLI behavior beyond the official documentation pages fetched above.

Artifact: `.ufo/waves/round-55/build/SrcGeminiCLI.md`
