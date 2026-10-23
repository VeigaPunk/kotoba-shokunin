Result: DONE — GitHub's Copilot CLI how-to documents a slash-prefixed explicit skill request; the frozen C1 self-test passed in the sandbox.

## Finding

GitHub Docs' current Copilot CLI how-to states that a user can ask for a specific skill by prefixing its name with `/`, then gives a concrete prompt example. In the fetched bytes, line 125 describes that rule and line 128 gives the exact form used below. The quote is the body text inside a fenced `copilot` example; the fence is omitted, and the quoted body text is byte-exact.

Quote (12 words): “Use the /frontend-design skill to create a responsive navigation bar in React.” — `add-skills.md:128`.

The page also distinguishes explicit request from automatic selection: “When performing tasks, Copilot will decide when to use your skills based on your prompt and the skill's description.” (`add-skills.md:121`).

## Draft C1 records

Draft SOURCES row (11 cells; `S0NN` is a placeholder):

| S0NN | GitHub Docs — Adding agent skills for GitHub Copilot CLI — https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills.md | docs | A | GitHub Copilot CLI prompt syntax for requesting one named skill | § Using agent skills, directions and example (`add-skills.md:125-129`); fetched 2026-10-22T23:12:41Z (HTTP 200, 10,057 B, sha256 `989af4981773349a74feaebfe98cdac9895b394707d201545ba55c8f9f4131a0`) | The example prompt asks Copilot to use `/frontend-design` to create a responsive navigation bar | mined | 2026-10-22 | 90d | corpus/knowledge/explicit-invocation-round55.md |

Draft entry row:

| Copilot CLI | S0NN | "Use the /frontend-design skill to create a responsive navigation bar in React." | add-skills.md:128 | The slash-prefixed skill name in the prompt tells Copilot to use that named skill. |

Draft SKILL.md decision row:

| Copilot CLI | `/frontend-design` | The prompt asks Copilot to use the named skill. | Set aside turns using this explicit slash form when measuring implicit, description-routed activation. |

The action applies the Frontier distinction to turns where the user names the skill explicitly; it does not claim that the skill was actually loaded in any observed CLI run.

## Blocking automatic invocation

The cited how-to does not document a switch for preventing automatic invocation; a search of its fetched bytes for `disable-model-invocation`, `user-invocable`, and automatic invocation controls returned `No matches found`.

The separately fetched CLI command reference does document both controls. At line 1277 it says: “Whether users can invoke the skill with `/SKILL-NAME`. Default: `true`.” At line 1278 it says: “Prevent the agent from automatically invoking this skill. Default: `false`.” Thus, setting `disable-model-invocation` while leaving `user-invocable` at its default retains user invocation while stopping automatic invocation. [INFERENCE: the last sentence combines the two separate frontmatter descriptions; the page does not state that combined outcome in one sentence.]

## Source checks and provenance

All fetches below used `curl -L -sS` and saved bytes under the sandbox clone. Each shell call ran `date -u`, then `curl` with HTTP status/downloaded byte reporting, `wc -c`, and `sha256sum`. The exact UTC line printed for each was `Thu Oct 22 11:12:41 PM UTC 2026` (2026-10-22T23:12:41Z). Each fetch returned HTTP 200 and the sizes and full hashes are recorded below. The wrapper did not print curl's process exit code separately; no fetch error was reported.

- How-to: `https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills.md` — 10,057 B; sha256 `989af4981773349a74feaebfe98cdac9895b394707d201545ba55c8f9f4131a0`. This page is not already a SOURCES row: the exact-URL search of lane `corpus/SOURCES.md` returned `No matches found`. The existing S027 row is a different, cloud-agent how-to route.
- Skills concept page at the moved route: `https://docs.github.com/en/copilot/concepts/customizations/agent-skills.md` — 2,622 B; sha256 `ed1e29440ec3aeadef2f461d1dc29910eb4014f0a1b451d8f04e73763605d4a7`. It links to the CLI how-to (`agent-skills.md:37-40`) but does not give an invocation token in the inspected text.
- CLI command reference: `https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference.md` — 461,944 B; sha256 `c61997efd7c939324e1f1b846fcb9ed420e5bbfd5eb5319531c6e6210025b5c9`. It documents `/SKILL-NAME`, `user-invocable`, and `disable-model-invocation` (`cli-command-reference.md:1267-1278`). This URL already has SOURCES rows at base (including S031, S038 and S056), so it is not used for the new source row.
- Official repository README: `https://raw.githubusercontent.com/github/copilot-cli/main/README.md` — 7,740 B; sha256 `33657f2e7383f2167b47d5f8c549a6071905a5c93d5d67d17e5c5399f126f07b`. The fetched README introduces the CLI and links to official docs (`README.md:1-20`); the invocation search found no skill form there. This checks the README only, not the complete repository source tree.

The fetch commands were:

```sh
timeout 900 bash -lc 'date -u; curl -L -sS -o /fast/scratch/hyaku/kotoba-r55/SrcCopilotCLI/add-skills.md -w "HTTP %{http_code}\nDOWNLOADED %{size_download}\n" https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills.md; wc -c /fast/scratch/hyaku/kotoba-r55/SrcCopilotCLI/add-skills.md; sha256sum /fast/scratch/hyaku/kotoba-r55/SrcCopilotCLI/add-skills.md'
timeout 900 bash -lc 'date -u; curl -L -sS -o /fast/scratch/hyaku/kotoba-r55/SrcCopilotCLI/cli-command-reference.md -w "HTTP %{http_code}\nDOWNLOADED %{size_download}\n" https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference.md; wc -c /fast/scratch/hyaku/kotoba-r55/SrcCopilotCLI/cli-command-reference.md; sha256sum /fast/scratch/hyaku/kotoba-r55/SrcCopilotCLI/cli-command-reference.md'
timeout 900 bash -lc 'date -u; curl -L -sS -o /fast/scratch/hyaku/kotoba-r55/SrcCopilotCLI/agent-skills.md -w "HTTP %{http_code}\nDOWNLOADED %{size_download}\n" https://docs.github.com/en/copilot/concepts/customizations/agent-skills.md; wc -c /fast/scratch/hyaku/kotoba-r55/SrcCopilotCLI/agent-skills.md; sha256sum /fast/scratch/hyaku/kotoba-r55/SrcCopilotCLI/agent-skills.md'
timeout 900 bash -lc 'date -u; curl -L -sS -o /fast/scratch/hyaku/kotoba-r55/SrcCopilotCLI/copilot-cli-README.md -w "HTTP %{http_code}\nDOWNLOADED %{size_download}\n" https://raw.githubusercontent.com/github/copilot-cli/main/README.md; wc -c /fast/scratch/hyaku/kotoba-r55/SrcCopilotCLI/copilot-cli-README.md; sha256sum /fast/scratch/hyaku/kotoba-r55/SrcCopilotCLI/copilot-cli-README.md'
```

Sandbox preparation (no output; the command completed without a reported error):

```sh
timeout 900 bash -lc 'unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE; git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r55/SrcCopilotCLI && git -C /fast/scratch/hyaku/kotoba-r55/SrcCopilotCLI checkout -q a10240c0940f770a5f2a5f32a7e3c363dd5d40c'
```

## Self-test and scope

Ran in `/fast/scratch/hyaku/kotoba-r55/SrcCopilotCLI`, at plan commit `a10240c0940f770a5f2a5f32a7e3c363dd5d40c`:

```sh
timeout 900 bash -lc 'python3 -B verifiers/check_explicit_invocation.py --self-test; rc=$?; printf "exit=%s\n" "$rc"; exit "$rc"'
```

Observed: `self-test: 0 failure(s) over 29 assertions`; `exit=0`.

Affected surfaces: this report is the only file written in the lane. The four fetched pages and the self-test run were in the sandbox clone; no product files, counters, SOURCES registry, knowledge entry, lesson, or SKILL.md were changed. The C1 live-page predicate (`--rev ... --fetch`) and C2 checks were not run. No Copilot CLI behavior was exercised. No tools were installed or updated.

Artifacts: `.ufo/waves/round-55/build/SrcCopilotCLI.md`; fetched bytes at `/fast/scratch/hyaku/kotoba-r55/SrcCopilotCLI/{add-skills.md,cli-command-reference.md,agent-skills.md,copilot-cli-README.md}`.