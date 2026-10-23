Result: DONE — all six eligible clients document a hook-safety control on the pinned host; only Claude Code and Gemini CLI say the hook runs with the user's permissions, and only Claude Code, Codex, VS Code, and Gemini CLI print a review-before-use sentence.

Seat ScoutHookSecurity. No lane file edited except this report. No tool installed. No model call. Fetches used the counter's curl header set (`verifiers/check_hook_files.py:316-318`): `curl -sSL --max-time 30 -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' -H 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8'`. `date -u` at start: `Fri 23 Oct 2026 09:35:19 AM UTC`. End: `Fri 23 Oct 2026 09:35:21 AM UTC`. Bodies saved under `/fast/scratch/hyaku/kotoba-r59/ScoutHookSecurity/`. Word counts below are `str.split()` on the quoted bytes (a backtick stays inside its token). A quote is a contiguous slice; anything outside the slice is named.

opencode is not eligible (census). Not fetched for this seat.

These quotes are for the Action cell. They are not proposed `SOURCES.md` quotes. None of the slices below contain `<…>` text. Cursor's longer project-hook sentence (line 771) does (`<project-root>`), so it is not quoted.

## What can go in an Action cell

The frozen Action cell only has to be at least three words. "review before enabling" is the author's gloss. Use it only where the client's own page prints a review-before-use sentence. Where the page prints a trust gate instead, the cell should say that gate, not the gloss.

| Client | Action cell grounded in the page | Do not write |
|---|---|---|
| Claude Code | review and test hook commands before adding them | — |
| Codex | review and trust non-managed hooks before they run | "runs with the user's permissions" (not on this page) |
| VS Code | review hook configuration and scripts before use | "runs with the user's permissions" (not on this page) |
| Copilot CLI | repository hooks need workspace admission; policy hooks are admin-installed | "review before enabling" (not printed) |
| Gemini CLI | verify the source of project hooks before enabling them | — |
| Cursor | project hooks run only in a trusted workspace | "review before enabling"; "runs with the user's permissions" (neither printed) |

## Fetches

| File | URL | HTTP | Bytes | sha256 |
|---|---|---|---|---|
| `claude-hooks.md` | https://code.claude.com/docs/en/hooks.md | 200 | 274129 | `c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8` |
| `codex-hooks.md` | https://learn.chatgpt.com/docs/hooks.md | 200 | 47133 | `57166ef03e7059732dd90925d5c42dd4d187eb2625d66cc154d0fbd2edb65f92` |
| `vscode-hooks.md` | https://code.visualstudio.com/docs/agent-customization/hooks.md | 200 | 15152 | `98c5be6b693a19ccd10c79b933d56e010101cef5a0eed699bd25e80289461e08` |
| `vscode-enterprise.md` | https://code.visualstudio.com/docs/enterprise/manage-ai-settings.md | 200 | 33047 | `49894046232ff57b4b964550f962cbc4a9a975930e910398b9dcb540960f073f` |
| `copilot-concepts.md` | https://docs.github.com/en/copilot/concepts/customizations/hooks.md | 200 | 8428 | `23370e092d2e2e81587b84038d0be116d99243a83c810b8e8cd41cf8734a10f4` |
| `copilot-reference.md` | https://docs.github.com/en/copilot/reference/hooks-reference.md | 200 | 72175 | `7ad7c168f319ce390802289ededf8dead2742959b18b5ccf6f41c2342cbf1c97` |
| `gemini-hooks.md` | https://geminicli.com/docs/hooks.md | 200 | 8341 | `a06a92438d3110690e875d61feef49a850d82eda618bb837146a1a7ff7a4c8d9` |
| `gemini-best.md` | https://geminicli.com/docs/hooks/best-practices.md | 200 | 17650 | `fb44fbcfaccc3cdb7895d989f3808bed66cfa6516411535c4c4d9077d242e7bc` |
| `cursor-hooks.md` | https://cursor.com/docs/hooks.md | 404 | 389 | `4f98eb063d1914a3100f2c7e6bab3a449877d33da375eb3c05edc3a61e78afb1` |
| `cursor-hooks-nomd.md` | https://cursor.com/docs/hooks | 200 | 69145 | `8436af768468590299c1beab9ea34bff8c5f1e5649ae244a989c28960dd2c88d` |

The six hooks-page hashes match the 09:02–09:21Z census and control fetches. Cursor line numbers below are from `https://cursor.com/docs/hooks` (the `.md` route is the 404 above, same sha the control recorded). Final URL on every 200 was the URL requested.

## Claude Code — code.claude.com

Page: https://code.claude.com/docs/en/hooks.md. Section `## Security considerations` starts at line 4140.

Permissions (line 4146, contiguous slice; the leading `> ` of the warning block is outside the slice). 10 words:

> Command hooks execute shell commands with your full user permissions.

Review before adding (same line, later slice). 12 words:

> Review and test all hook commands before adding them to your configuration.

Workspace trust (line 4150, whole line). 23 words:

> Claude Code checks workspace trust before it runs any hook from a settings file. What counts as trusted depends on the session type:

The next bullet (line 4153) is the exception that matters for an Action cell. Contiguous slice, 13 words:

> hooks committed in a repository's `.claude/settings.json` run in a folder you've never trusted

That slice is inside the `-p` or SDK bullet: Claude Code never shows the trust dialog in those sessions. "Review before enabling" does not cover a `-p` run over a repository the user did not write.

Managed policy (line 257, whole line). 12 words. The two markdown links are single tokens except `[managed settings](…)`, which splits on the space:

> Administrators can use [`allowManagedHooksOnly`](/docs/en/settings-reference#allowmanagedhooksonly) in [managed settings](/docs/en/managed-settings.md) to restrict which hooks run:

## Codex — learn.chatgpt.com

Page: https://learn.chatgpt.com/docs/hooks.md. `## Review and trust hooks` is line 62.

Review before they run (line 19, whole line, list hyphen kept). 11 words:

> - Non-managed hooks must be reviewed and trusted before they run.

Project trust (line 58, first sentence only; the line continues ` In`). 11 words:

> Project-local hooks load only when the project `.codex/` layer is trusted.

Managed policy (lines 73–74, both lines, newline kept as whitespace). 25 words, at the cap:

> Managed hooks from system, MDM, cloud, or `requirements.toml` sources are marked
> as managed, trusted by policy, and can't be disabled from the user hook browser.

A search of this file for `privileges`, `full user`, `your user`, `user permissions`, `arbitrary code`, `executable code`, `same shell`, and `your machine` returned no line. Codex documents review-and-trust and managed policy, not "hooks run with the user's permissions".

## VS Code — code.visualstudio.com

Page: https://code.visualstudio.com/docs/agent-customization/hooks.md. `## Security considerations` is line 199.

Review before use (line 202, whole line, blockquote marker kept). 23 words:

> > Hook configuration and scripts are executable code. Review them before use, including hooks bundled in plugins or stored in a shared repository.

Organization control, on the same page (line 14, first sentence; the leading `> ` is outside the slice). 8 words:

> Your organization might restrict which hooks can run.

The same line points at `/docs/enterprise/manage-ai-settings.md`, which was fetched (row above). Two controls there, each a contiguous slice:

Line 273, 9 words: `Set the `ChatHooks` policy to `false` to disable hooks.` That sentence is under the note "For Local harness sessions" and the rest of the line says it does not apply to Copilot harness sessions. The whole line is 26 words, so only this sentence is quoted.

Line 294, first sentence, 14 words:

> Set `ChatAllowManagedHooksOnly` to allow hooks only from enterprise-managed sources and plugins that policy force-enables.

Line 286, first sentence, 11 words: `Copilot policy hooks run on the host, outside the session sandbox.`

Trusted workspace for the old Local harness is on the hooks page, line 183, whole line, 25 words:

> * Local agent-scoped hooks require a trusted workspace and `chat.useHooks`. A scoped `Stop` hook is treated as `SubagentStop` when the agent runs as a subagent.

The same absence search as Codex, on `vscode-hooks.md`, found no "user permissions" sentence. The page says the configuration is executable code.

## Copilot CLI — docs.github.com

Two pages. The concepts page is the census quote page. The reference page holds the trust and policy controls.

Concepts, https://docs.github.com/en/copilot/concepts/customizations/hooks.md, `## Security considerations` line 150. Line 154, whole line, 17 words. This is about sanitizing hook input, not about the user reviewing a hook before enabling it:

> * **Always validate and sanitize the input processed by hooks**. Untrusted input could lead to unexpected behavior.

Reference, https://docs.github.com/en/copilot/reference/hooks-reference.md.

Where commands run (line 17, contiguous slice). 14 words:

> hooks run on the developer's local machine in the same shell as the CLI.

That is the closest sentence to "the user's permissions". It does not say permissions.

Folder trust does not cover policy hooks (line 21, contiguous slice). 14 words:

> They cannot be disabled by `disableAllHooks` and are available regardless of folder trust state.

Enterprise install (line 48, first sentence). 16 words:

> Policy hooks are intended for use by enterprise IT administrators and require elevated privileges to install.

"Elevated privileges" here is the privilege required to install the policy file, not the privilege the hook runs with. The next sentences on that line (not quoted; the whole line is 37 words) say end users cannot modify policy hooks and that they run on the host even when the session sandbox is on.

Workspace admission (line 75, Trust cell, contiguous slice). 7 words:

> Repository and inherited-agent hooks require workspace admission.

No line on the concepts page matched `privileges`, `user permissions`, `arbitrary code`, `executable code`, or `your machine`. The reference does not print "review before enabling".

## Gemini CLI — geminicli.com

Permissions warning, https://geminicli.com/docs/hooks.md lines 150–152, all three lines, the three `>` markers kept. 25 words, at the cap:

> > Hooks execute arbitrary code with your user privileges. By
> > configuring hooks, you are allowing scripts to run shell commands on your
> > machine.

Untrusted projects (line 154, whole line). 9 words:

> **Project-level hooks** are particularly risky when opening untrusted projects.

Review before enabling is on the best-practices page, which is also the census quote page (https://geminicli.com/docs/hooks/best-practices.md). Line 442, whole line, 12 words:

> **Verify the source** of any project hooks or extensions before enabling them.

System settings as the admin tier (line 406, whole table row). 17 words:

> | **System**                    | Configured by system administrators (for example, `/etc/gemini-cli/settings.json`, `/Library/...`). Assumed to be the **safest**. |

Project hooks on that same table (line 409, whole row, 18 words) are marked `Untrusted by default.`

## Cursor — cursor.com

Page fetched: https://cursor.com/docs/hooks (HTTP 200). https://cursor.com/docs/hooks.md with this header set was HTTP 404, body `# Page not found` (10 lines).

Trusted workspace (line 649, whole line). 17 words:

>   - Project hooks run in any trusted workspace and are checked into version control with your project

The security reason (line 781, whole line). 11 words:

> - Require the workspace to be trusted to run (for security)

Once the workspace is trusted, loading is automatic (line 771, contiguous slice that stops before `<project-root>`). 18 words:

> When team members open the project in a trusted workspace, Cursor automatically loads and runs the project hooks.

Enterprise / MDM (line 798). Two slices, because the whole line is 38 words:

> Cursor does not deploy or manage files through your MDM solution.

11 words. Then:

> Ensure your internal IT or security team handles configuration, deployment, and updates in accordance with your organization's policies.

18 words. Enterprise and team hook paths are listed at lines 641–646 (`/etc/cursor/hooks.json` on Linux; team hooks are "enterprise only").

The absence search on this body found no "user permissions", "arbitrary code", or "review before" sentence.

## kasegi

kasegi is adjacent as bounty and security research (kotoba `PROVINCE.md:53`); these six warnings are the clients' own docs, not a kasegi source, and the only hook hit seen in kasegi's tree is the already-disclosed CWE-78 in Anthropic `plugin-dev` `test-hook.sh` (`kasegi-shokunin/corpus/knowledge/operator-queue.md:21-29`).

## Limits

Not a whole-host sweep. Each client's hooks page was fetched and searched; VS Code's enterprise page was fetched because the hooks page links it. Changelogs were not opened. A phrase reported as absent was absent from the fetched hooks page, which is not a claim that no other page on that host prints it.
