Result: HOLDS — The landed VS Code/Copilot CLI split is honest under frozen E5; it does not establish independent harnesses, and dropping Copilot would leave F=5, G=5 under unchanged live results.

## Scope and axes

Seat `KotobaR59.CriticCopilotE5`; recipient/integrator `KotobaR59` only. Scoped falsification, not claim admission or a native-judge verdict.

Reviewed data revision `c63ccc6823e1f6a8577acbb43d19551eadbbee9a`, including `.ufo/waves/round-59/build/CriticCensus.md:28-44` and lesson M84 (`corpus/lessons/round-59.md:51-60`). Axes: **depth** (correct, actionable configuration destinations), **calibration** (token count versus implementation count; census provenance), **operability** (session target and user/repository scope). No counter, rule, target, or client-population change is proposed.

## E5-1 — Duplicate-first-token attack: HOLDS

The actual leads at `SKILL.md:129-130` are:

| Row | First Hook config token | casefold(normalise(token)) |
|---|---|---|
| VS Code | `.github/hooks/*.json` | `.github/hooks/*.json` |
| Copilot CLI | `~/.copilot/hooks/*.json` | `.copilot/hooks/*.json` |

These keys are unequal. `verifiers/check_hook_files.py:774-783` collects only each Hook config cell's first backticked span; `:891-909` disqualifies rows sharing that normalized first token. `:633-644` removes the leading `~/`, not the `.copilot` segment. The entry uses those same respective leads (`corpus/knowledge/hook-files-round59.md:25-26`).

Naming the shared repository folder in plain words is not hiding a second counted key: even an additional backticked occurrence after the CLI personal lead would not participate in this first-token rule. The landed CLI cell explicitly admits the shared repository pattern, and the entry explains the choice (`SKILL.md:130`; entry `:44-46`; lesson `:24`). Both chosen paths are documented configuration inputs, not aliases for one filesystem path: one is repository scope, the other user scope. The frozen row rule does not require either location to be client-exclusive.

**Smallest safe correction:** none to the leads or E5 accounting. Do not replace the CLI lead with the repository glob: that would create the exact collision E5 rejects.

## E5-2 — Independent/shared-surface attack: MIXED, with a concrete counterexample to exclusivity

The strongest local counterexample is the VS Code vendor page itself. Independently fetched bytes equal committed S098 exactly. Verbatim contiguous excerpts below retain all Markdown bytes within each excerpt; no bytes were stripped:

- S098 / `critic-vscode.page:18`: “VS Code, the GitHub Copilot app, and GitHub Copilot CLI share this harness and its hook format.”
- S098 / `critic-vscode.page:58`: “User hook files in `~/.copilot/hooks/`”
- S099 / `critic-copilot.page:28`: “Copilot CLI also supports personal hooks in `~/.copilot/hooks/*.json`.”

S098 `:59` documents the repository glob, while S099 `:28` documents that same repository glob before the personal one. Therefore the personal hook source is not exclusive to the CLI, and the repository source is not exclusive to VS Code. The foreign-name guard rejecting `.copilot` in a VS Code lead (`check_hook_files.py:624-629`) is lexical, not an ownership or runtime-identity test.

This defeats an interpretation of G=6 as six independent hook implementations or six client-exclusive surfaces. It does **not** defeat the declared metric, which counts distinct new lead-token keys across eligible client rows. The landed entry discloses the overlapping repository source, rather than claiming exclusivity; `corpus/SOURCES.md:110` also explicitly scopes VS Code to the Copilot harness. Thus this is not one identical path counted twice under E5.

**Smallest safe presentation correction:** carry the already-recorded source scope into the compact skill row: change the VS Code parenthetical to begin “Copilot session target; repository-shared”, and add one sentence to the per-client notes: “VS Code's Copilot target and Copilot CLI share the Copilot harness; these rows select repository and personal scopes, not exclusive implementations.” S098 `:16-30` explicitly distinguishes other session targets. Keep both leads and the frozen predicate unchanged. This is a fixable depth/calibration/operability clarification, not grounds to trade correctness for a green counter. Any assertion of independent implementations would remain unsupported regardless of F/G.

## E5-3 — M84/census provenance attack: MIXED, not a current row failure

M84 correctly preserves the mismatch: W0 VS Code scored `.github/hooks/audit.json`, and rejected the wildcard conditionally on Copilot leading with that same wildcard (`w0/CensusVSCode.md:1-3,76-85`). W0 Copilot actually selected the personal glob (`w0/CensusCopilotCLI.md:1-3,9`). Therefore W0's premise for rejecting the wildcard is not the landed pairing.

The build rescore is real but later: `build/SrcVSCode.md:60-90` records snapshot/live quote and event checks using the frozen counter, and explicitly does not claim a full predicate run. Lesson M84 `:55-58` names the post-freeze rescore and future pre-freeze prevention rule. The L1 measurement receipt then records the full landed result. These later checks support current row correctness; they cannot make the original substituted census token a seat-rescored pre-freeze token.

**Smallest safe correction:** retain M84 and the original W0 record; describe the wildcard validation as post-freeze remediation, never retroactive pre-freeze approval. No rewriting the freeze, changing targets, or treating this review as a new census. The historical provenance defect is separate from the present E5 result.

## E5-4 — Remove-Copilot sensitivity: HOLDS for the frozen arithmetic

The existing L1 receipt `.ufo/waves/round-59/C1-measure.txt:3-12` names data revision `c63ccc6823e1f6a8577acbb43d19551eadbbee9a`, records F=6 and G=6, and records exit 0. This is cited evidence, not a rerun by this seat.

`check_hook_files.py:253-254` fixes TARGET=4 and NEW_TARGET=5. Found rows contribute individually to F (`:2383-2398`); G is distinct casefolded normalized found tokens without held occurrences (`:1254-1260,2398-2409`). Removing the CLI row removes its one distinct key and cannot introduce a duplicate among remaining first tokens.

**[INFERENCE — static deletion analysis, not an executed mutant; other live results held fixed]:**

| Population | F | G | Frozen numerical predicate |
|---|---:|---:|---|
| Recorded six found rows | 6 | 6 | 6 >= 4 and 6 >= 5 |
| Same result without Copilot CLI | 5 | 5 | 5 >= 4 and 5 >= 5 |

So **both F and G decrease by one**, but the numerical predicate still holds; G is then exactly on its floor. The CLI split is not necessary to cross the frozen thresholds. This does not prove a fresh live run, erase M84, demonstrate saturation, or admit the claim. No row removal is recommended or applied.

## Access and command evidence

All scratch paths are under `/fast/scratch/hyaku/kotoba-r59/CriticCopilotE5/`. No sandbox commit was made.

Setup command, combined exit 0, no output:

```sh
timeout 120s env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r59/CriticCopilotE5 && timeout 30s env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git -C /fast/scratch/hyaku/kotoba-r59/CriticCopilotE5 checkout -q c63ccc6823e1f6a8577acbb43d19551eadbbee9a
```

Fetch command form, executed once for each URL below from that clone; combined shell exit 0. No browser, challenge bypass, or access-control workaround:

```sh
timeout 5s date -u && timeout 45s curl -sSL --max-time 35 -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' -H 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8' -o <file> -w '\nHTTP %{http_code}; final %{url_effective}; bytes %{size_download}\n' <URL> && timeout 10s sha256sum <file> && timeout 10s wc -c <file>
```

`date -u` printed the following line immediately before **each** fetch:

```text
Fri 23 Oct 2026 09:52:33 AM UTC
```

| File | Requested and final URL | HTTP | curl/wc bytes | sha256 |
|---|---|---:|---:|---|
| critic-vscode.page | https://code.visualstudio.com/docs/agent-customization/hooks.md | 200 | 15152 | 98c5be6b693a19ccd10c79b933d56e010101cef5a0eed699bd25e80289461e08 |
| critic-copilot.page | https://docs.github.com/en/copilot/concepts/customizations/hooks.md | 200 | 8428 | 23370e092d2e2e81587b84038d0be116d99243a83c810b8e8cd41cf8734a10f4 |

Read-only fact command, combined exit 0, cwd the clone:

```sh
timeout 10s git --no-optional-locks rev-parse HEAD && timeout 10s sha256sum verifiers/check_hook_files.py .ufo/waves/round-59/snapshots/S098.page .ufo/waves/round-59/snapshots/S099.page && timeout 10s cmp critic-vscode.page .ufo/waves/round-59/snapshots/S098.page && timeout 10s cmp critic-copilot.page .ufo/waves/round-59/snapshots/S099.page
```

Observed output (both cmp commands emitted nothing):

```text
c63ccc6823e1f6a8577acbb43d19551eadbbee9a
f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71  verifiers/check_hook_files.py
98c5be6b693a19ccd10c79b933d56e010101cef5a0eed699bd25e80289461e08  .ufo/waves/round-59/snapshots/S098.page
23370e092d2e2e81587b84038d0be116d99243a83c810b8e8cd41cf8734a10f4  .ufo/waves/round-59/snapshots/S099.page
```

Only this report was written in the lane. No lane code, counter, mutation, self-test, build, lint, formatter, native judge, or other agent/runtime was invoked. No tool installed/updated, subagent dispatched, paid model call, Git/jj write in the lane, push, fleet-root/sibling write, load test, or shared-process kill. Recommendations are text for the sole integrator, not applied edits.

Report: .ufo/waves/round-59/falsify/CriticCopilotE5.md
