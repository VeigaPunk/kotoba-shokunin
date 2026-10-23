Result: MIXED — All six documented directory attributions survive reopening, but Claude Code needs sharper older-format provenance and the VS Code and opencode W0 quotes are not directly interchangeable with complete frozen-counter backing.

## Scope and axes

CriticCensus; review only, no admission or round judgment. Axes: **depth** (does each directory and quotation teach the actual command surface?) and **calibration** (supported versus deprecated, source identity, and source eligibility versus measured backing). No counter, target, census population, route, or lane product file was changed. C2 remains withdrawn; I read its frozen counter but did not evaluate it.

I reopened all six W0 primary pages. Their bodies have exactly the W0 byte counts and SHA-256 values. “Holds” below means the stated source/directory claim holds, not that an integrated revision has passed C1. No evidence obtained here makes any of the six directory attributions **wrong**. The weak findings are specific, repairable content/representation defects.

## Per-row result

| Client | Review | Finding and smallest correction |
|---|---|---|
| Claude Code | **weak; directory eligibility holds** | The page explicitly calls this the older format, still supported, and prefers skills for new work. Keep the token, but make the Action say **“Older format, still supported; prefer a skill for new work.”** Also disclose that the slash-commands URL is an alias of the already-held skills document, not an independent newly discovered authority. |
| Codex | **holds, with the deprecation qualification** | The directory and 9-word quotation are correct. Calling it the unqualified recommended command location would mislead. The proposed Action already says custom prompts are deprecated and to use skills for new reusable prompts (`build/ScribeSkillSection.md:11`); retain that qualification. This is deprecated, not evidence that the folder no longer loads. |
| VS Code | **weak; directory eligibility holds** | The location is correct for workspace prompt files in **Local** harness sessions, not the Copilot harness generally. The W0 quote is a real 22-word span, but includes four literal table pipes and borrows its outside-token `prompt` word from the subsequent user-level paragraph. Unchanged insertion in the knowledge table breaks the frozen parser. Preserve the raw quote and explicitly losslessly encode its pipes for table transport, or replace it with another properly evidenced quote. Do not silently delete the pipes or omit Local-only scope. |
| Gemini CLI | **holds** | This is the documented global user-command folder, not the project folder. The 8-word W0 quote is exact. TOML files and required `prompt` are independently stated on the same page. Label the scope “user/global”; do not describe this printed `~/` token as the project path. |
| Cursor | **holds, narrowly** | The deeplinks page is a fair first-party source for this directory: its Commands subsection explicitly associates custom commands with the directory and describes creating a named command with user-supplied content and confirmation. It is not merely an incidental URL in an example. The separate current Customize page corroborates Markdown files and `/` invocation. Do not extend this to an undocumented personal path, filename template, full schema, or a claim of deprecation. |
| opencode | **weak in W0's fetch representation; directory eligibility holds** | W0 obtained Markdown using `Accept: text/markdown`, but the frozen fetch supplies no Accept header and receives HTML. The original quotation's final period no longer touches the path after the frozen HTML tag stripping. The source seat has already supplied a suitable pinned raw-docs correction (`build/Srcopencode.md:31-54,60-65`), which I reopened. Use that correction. An even smaller textual repair for the served URL is to end the quote immediately before its final sentence-period byte. |

Paths abbreviated as `build/` or `w0/` in this report are under `.ufo/waves/round-58/`.

### Exact quotes and page context

Quotes below retain the source Markdown bytes; no emphasis or backtick bytes are stripped. Any omitted prefix/suffix is named. Fetched files are under `/fast/scratch/hyaku/kotoba-r58/CriticCensus/`.

1. **Claude Code** — [primary page](https://code.claude.com/docs/en/slash-commands.md), `claude.body:172`, 14 words:

   ```text
   **Command files**: a Markdown file in `.claude/commands/` is the older format and still works.
   ```

   The source list prefix `* ` is outside the selected substring. The same line prefers a skill for new work; `claude.body:17` says custom commands have been merged into skills and existing command files keep working. `:450-451` gives filename and nested-path-to-command-name mappings. Thus an older-but-supported row is factual. Recommending this as the ordinary new-work authoring format would discard the source's advice. The draft's “Prefer a skill for new work” is already directionally correct (`build/ScribeSkillSection.md:10`); explicitly adding “older, still supported” removes the remaining ambiguity without removing the row.

   **Source identity:** I reopened [skills.md](https://code.claude.com/docs/en/skills.md), got the same 114,542 bytes and SHA-256 as slash-commands.md, and `cmp` exited 0 without output. Base SOURCES already has skills URLs at `corpus/SOURCES.md:35,66,78`; S065 at `:78` even says slash-commands.md served the same bytes in round 55. The frozen `url_key()` distinguishes `/skills` from `/slash-commands` (`verifiers/check_command_files.py:494-512`), so this is not a literal base-URL collision. It is nevertheless the same document authority. Smallest safe correction: label S089 as a newly mined command-file detail on a re-opened alias of the skills page. Do not call the alias a new independent source or a second corroborating authority. This does not erase the separately frozen held-token novelty claim.

2. **Codex** — [primary page](https://learn.chatgpt.com/docs/custom-prompts.md), `codex.body:62`, 9 words:

   ```text
   Manage prompts by editing or deleting files under `~/.codex/prompts/`.
   ```

   No bytes inside the selected sentence were changed. `:5-10` explicitly labels custom prompts deprecated, recommends skills, and scopes prompts to local Codex home rather than repository sharing. `:12-18,32-34` still documents authoring and invocation; `:62` limits discovery to top-level Markdown files. Therefore “deprecated” is required reader-facing calibration, but “unsupported” would overstate the evidence. The current draft already supplies the correct qualification.

3. **VS Code** — [primary page](https://code.visualstudio.com/docs/agent-customization/prompt-files.md), `vscode.body:25-28`, 22 words:

   ```text
   `.github/prompts` folder |
   | User profile | Your user data (specific to your VS Code profile) |

   To create a user-level prompt
   ```

   This is an exact contiguous substring beginning inside the Workspace row; it omits the earlier `| Workspace | ` and ends before ` file,` on line 28. Four standalone pipes count among its 22 whitespace-delimited words. The outside-token word is the last `prompt`, belonging to user-level creation, not the workspace row. Context still establishes the actual fact: `:5` defines prompt files; `:17,21,25` establishes Local-only sessions and the workspace directory; `:35` specifies `.prompt.md` files. This is weak quote selection, not a false workspace-directory attribution.

   A rendered HTML excerpt can be clearer contextually, but it must not be reported as an unshaped raw-Markdown substring. The raw W0 quote can instead be transported losslessly as described below. Keep the Local-only Action from `build/ScribeSkillSection.md:12`.

4. **Gemini CLI** — [primary page](https://geminicli.com/docs/cli/custom-commands.md), `gemini.body:12`, 8 words:

   ```text
   **User commands (global):** Located in `~/.gemini/commands/`. These commands
   ```

   The list-number prefix `1.  ` is outside this selected substring. The sentence continues at `:13`; `:14-17` distinguishes the project directory, `:19-21` gives same-name project precedence, and `:39-47` specifies TOML `.toml` files and required `prompt`. The W0 quote is a fragment but is unambiguous about the claimed global folder. A longer complete-sentence selection is already provided by `build/SrcGeminiCLI.md:6,47`; no token change is needed.

5. **Cursor** — [primary page](https://cursor.com/docs/reference/deeplinks.md), `cursor.body:54`, 13 words:

   ```text
   Command deeplinks allow you to share custom commands defined in your `.cursor/commands` directory.
   ```

   This is a complete, unchanged sentence within the Commands paragraph. The same paragraph describes creating a new named command with supplied content and requiring user confirmation. The [current Customize page](https://cursor.com/docs/customize-cursor.md), `cursor-customize.body:31`, defines commands as reusable `/` prompts stored in Markdown files. Together these are fair, scoped primary documentation, not third-party inference from the article title. The [skills reference](https://cursor.com/docs/skills.md), `cursor-skills.body:316-329`, and [skills help](https://cursor.com/help/customization/skills.md), `cursor-help-skills.body:84-91`, document migration of user/workspace commands to explicitly invoked skills. Migration availability alone does not establish deprecation or removal. Do not infer either label, nor import a changelog-only filename pattern into this row.

6. **opencode** — [W0 primary page](https://opencode.ai/v2/docs/commands/), `opencode.body:19`, 10 words:

   ```text
   Put global commands in `~/.config/opencode/commands/` and project commands in `.opencode/commands/`.
   ```

   No bytes are stripped from this sentence. `:3,26,35` establishes authoring, Markdown discovery and prompt-template body; `:32-33` calls the singular directory legacy and recommends the counted plural directory for new files. The plural row must not inherit the singular directory's legacy label. The same exact quote is at `opencode-pinned.body:21` on the [pinned first-party docs source](https://raw.githubusercontent.com/anomalyco/opencode/4e0bc52216d91c3a8d10035837b1b6f9b82fd1d3/services/www/src/docs/content/commands.mdx), with matching content at `:28,34-37`. That pinned raw URL is inside the frozen allowed mirror and is a docs file, not a tracker or changelog.

## Every frozen row-rule conjunct

Authority read before drafting: `plans/round-58.md:24-71` and `verifiers/check_command_files.py:50-182,257-300,568-637,678-738,752-805,824-938`. The frozen C2 counter was also read; no C2 claim is introduced here.

| Client | Normalized token; segments | Regex / dot-led first / final allowed word | Banned segment / non-final internal dot / foreign marker | Raw quote words; outside-token word |
|---|---|---|---|---|
| Claude Code | `.claude/commands`; `.claude`, `commands` | all hold; `commands` | none / none / none | 14; `Command` |
| Codex | `.codex/prompts`; `.codex`, `prompts` after one `~/` | all hold; `prompts` | none / none / none | 9; `prompts` |
| VS Code | `.github/prompts`; `.github`, `prompts` | all hold; `prompts` | none / none / none | 22; final `prompt` (selection weakness above) |
| Gemini CLI | `.gemini/commands`; `.gemini`, `commands` after one `~/` | all hold; `commands` | none / none / none | 8; `commands` |
| Cursor | `.cursor/commands`; `.cursor`, `commands` | all hold; `commands` | none / none / none | 13; `Command`, `commands` |
| opencode | `.opencode/commands`; `.opencode`, `commands` | all hold; `commands` | none / none / none | 10; `commands` |

All six tokens have exactly two non-empty segments after the permitted prefix/trailing-slash normalization. Each first segment has its only dot at position zero. None splits into a banned skill/agent/rule/plugin/extension word. Own client markers are allowed; `.github` contains no frozen foreign marker. All raw quotations hold the case-sensitive token, with an accepted left boundary (backtick or quote start after backtick stripping) and right boundary (backtick, whitespace or punctuation). All original word counts lie within 6–25.

Other conjuncts, separated from those intrinsic token/quote checks:

- **Own documentation / pinned host / docs rather than release material:** all six URLs reopened successfully, without changing effective URL. Each is on its client's frozen pin and has no excluded change-note or tracker path. All bodies are below the frozen 5 MiB cap. Cursor's topic being deeplinks does not make its explicit Commands subsection non-primary.
- **E5 is a table property, not a web-wide ownership claim.** The six normalized tokens above are pairwise distinct. The proposed SKILL table has one row per client and no backticked path in Copilot CLI's command cell (`build/ScribeSkillSection.md:10-16`). This closes the relevant cross-row comparison for that draft. A different client's documentation mentioning the same path does not itself trigger E5. Putting the Claude path into Copilot CLI's command cell would trigger it, even though that row is already foreign-marker-ineligible.
- **Action and table identity:** the draft has the exact frozen heading/header and each eligible Action has at least three words (`build/ScribeSkillSection.md:5,8,10-16`). The counter checks Action length, not whether its advice respects deprecation (`check_command_files.py:782-784`). Consequently syntactic Action eligibility is not evidence of safe advice.
- **E4:** the entry Command files cell must be just the raw token or its exact normalized form. Scope notes and alternatives may follow the first token in SKILL's cell, but must not be copied into the entry token cell (`check_command_files.py:660-663`). This report supplies no claim that all final entry rows have been integrated.
- **New ID, base URL, metadata and Gate:** the clone's SOURCES registry equals the base registry (read-only `git diff --exit-code` below); the assigned S089/S090/S091/S093/S094/S095 IDs are not base rows. None of the six exact source-cell URLs is a base URL under the frozen syntactic normalization. Claude's same-document alias caveat remains. The final rows must still have `docs`, `A`, `mined`, opened `2026-10-23`, one matching ID and a Gate-recorded quote. These are integration obligations, not facts certified by the W0 page census or by this review.
- **With fetch:** the four unchanged Markdown quote/page pairs other than VS Code transport and opencode default-representation concerns are directly supported by the reopened bytes. I did not run the frozen counter. W0's Accept-negotiated opencode body alone does not establish the frozen fetch predicate; see the observed representation difference below. No aggregate F/G value, full-row BACKED result, or C1 exit code is claimed.

## Strongest counterexamples and minimal corrections

### 1. Literal VS Code quote cannot occupy the frozen Quote cell

The frozen parser does `s[1:-1].split("|")` (`check_command_files.py:375-379`), and takes only the fourth cell for the quote (`:695`). A standalone, in-memory diagnostic using that exact split expression, not importing or executing lane code, produced:

```text
Census quote words: 22
literal cells= 8 parsed Quote= '"`.github/prompts` folder' word count= 2
backslash escaped cells= 8 parsed Quote= '"`.github/prompts` folder \\' word count= 3
```

Thus ordinary `\|` escaping does not fix this parser. The quote cell is truncated before the only outside-token `prompt`; it also fails the six-word floor. A future statement that the literal W0 quote already supplies a ready-backed table row would be false.

**Smallest lossless transport correction:** preserve the raw 22-word source quote in a fenced Gate block and disclose that, in the entry table, each of its four U+007C `|` characters is encoded as `&#124;`; fold source whitespace only. Record that same encoded quote in Gate as well, because `quote_in_gate()` is whitespace/backtick-based, not HTML-entity-based (`:653-655`). Do not call the encoded table bytes an unshaped raw quote. No source wording is changed, and the frozen quote normalization already applies `html.unescape()` (`:824-839`). The independent in-memory calculation gave:

```text
Lossless table-transport cells: 4
Quote words after backtick stripping: 22
Whitespace-normalized, HTML-unescaped quote equals source: True
Frozen quote-side normalized strings equal: True
```

This is a representation repair, not a changed counter or a fabricated prose quotation. Its quote-selection quality is still modest because of the user-level tail; the surrounding location section must retain the workspace/Local scope. A cleaner replacement primary excerpt would be preferable if supplied with equally honest provenance. Do not replace the quote with a paraphrase just to remove the pipes.

### 2. opencode's W0 Accept header is not the frozen fetch request

`fetch()` sets only its User-Agent (`check_command_files.py:914-915`). My default-GET capture is HTML; its line 66 is:

```html
<p>Put global commands in <code>~/.config/opencode/commands/</code> and project commands in <code>.opencode/commands/</code>.</p>
```

The frozen tag/whitespace rules turn its end into `.opencode/commands/ .`, not the quotation's `.opencode/commands/.`. A standalone calculation on these displayed bytes produced:

```text
W0 quote in rendered snippet: False
Quote with final period omitted in rendered snippet: True
```

This is consistent with the already-reported actual helper result `False` for the served URL in `build/Srcopencode.md:50-54`; I did not rerun that lane-code helper. **Safe correction already available:** integrate the source seat's pinned raw-docs URL, exact 10-word quotation and corresponding Gate metadata. I independently reopened that pin and verified the sentence at line 21. Alternatively omit only the last U+002E sentence-period byte from the W0 sentence when using the served URL; that remains a contiguous raw-Markdown substring and avoids the HTML punctuation mismatch. No token or rule changes are required.

### 3. A qualifying folder can still produce misleading new-work advice

[INFERENCE] An Action such as “Create all new reusable prompts here” meets the frozen three-word test even for deprecated Codex prompts. No counter output here demonstrates such an adversarial row; the inference follows directly from the Action-length-only implementation and the live deprecation text.

This is a fixable content defect, not a reason to lower the frozen targets or remove a supported older surface. Correct the Action as above. Retaining an unqualified obsolete recommendation merely to advertise broader coverage would trade depth for calibration; that unresolved harm is for the canonical judge to reject, not for this critic to admit. Conversely, calling Claude's older format or Cursor's migratable commands “removed” would introduce a new unsupported claim.

## Reopening receipts

All commands below completed successfully (exit 0). Each primary-page call printed the exact `date -u` line **`Fri 23 Oct 2026 08:09:13 AM UTC`** immediately before curl. Effective URLs equalled the requested URLs. Captures are in the isolated critic clone; nothing was fetched into lane product files.

The six primary calls used this command shape, substituting the listed basename and URL. Only opencode's W0-representation call added `-H 'Accept: text/markdown'`:

```sh
timeout 5 date -u && timeout 90 curl -sSL --max-time 75 --max-redirs 5 -D /fast/scratch/hyaku/kotoba-r58/CriticCensus/<name>.headers -o /fast/scratch/hyaku/kotoba-r58/CriticCensus/<name>.body -w 'HTTP %{http_code}; bytes %{size_download}; URL %{url_effective}\n' <URL> && timeout 5 wc -c /fast/scratch/hyaku/kotoba-r58/CriticCensus/<name>.body && timeout 5 sha256sum /fast/scratch/hyaku/kotoba-r58/CriticCensus/<name>.body
```

| Basename | URL | HTTP; bytes | SHA-256 |
|---|---|---|---|
| claude | https://code.claude.com/docs/en/slash-commands.md | 200; 114542 | `6b070e872dea28905a7ea7f45c4d5960f5bdf28cc73ac808799af6d50435ffbd` |
| codex | https://learn.chatgpt.com/docs/custom-prompts.md | 200; 3357 | `d6f7cf8dd9f31d2faf5604ef3a6f8322132a7b66fa50823109cb681e372a0fa9` |
| vscode | https://code.visualstudio.com/docs/agent-customization/prompt-files.md | 200; 13729 | `4ad1b2bcaf78c9166b1609610f354d9cb8b1ff9c9e7cf643c443fad04dac6685` |
| gemini | https://geminicli.com/docs/cli/custom-commands.md | 200; 12129 | `8f3295e8ca502b0c70bb3bf672f0dc0130ecb868fad4a88d5cac0f36ac6f3872` |
| cursor | https://cursor.com/docs/reference/deeplinks.md | 200; 5972 | `7ceb657892bdfa5d7a32f1168411fcaeb63c2f6ab41a5f0c45116a0a3f3a6bf4` |
| opencode | https://opencode.ai/v2/docs/commands/ | 200; 7220 | `c3dc75fc48071613c359126e7d84e2298afd10c4b83aac83383e94a1489a23dc` |

Additional ordinary curl calls used the same bounded command shape; all exited 0, HTTP 200, effective URL unchanged:

| Basename | URL | Exact `date -u` line | Bytes; SHA-256 |
|---|---|---|---|
| vscode-migration | https://code.visualstudio.com/docs/agent-customization/migrate-customizations.md | Fri 23 Oct 2026 08:10:26 AM UTC | 59037; `a671708e4247448a8128000d5ef3b7c4ebbef15a81d7feccd74d486c1b64941a` |
| cursor-customize | https://cursor.com/docs/customize-cursor.md | Fri 23 Oct 2026 08:10:26 AM UTC | 5200; `9ae0878d97465512ad29459f5406538ec7b427dfbaa39e1cc95d3deb447f363e` |
| cursor-skills | https://cursor.com/docs/skills.md | Fri 23 Oct 2026 08:10:26 AM UTC | 18477; `a642fa96776c247dba126a325e1dd73dac3f532a70060e745fb9bbd5b377602d` |
| opencode-default | https://opencode.ai/v2/docs/commands/ (no Accept; `-A kotoba-shokunin-counter/58`) | Fri 23 Oct 2026 08:10:26 AM UTC | 32304; `32591ac3db0056fdbf3b5e20b78e70514da0d7306707cbf7c412ca19276640e0` |
| claude-skills | https://code.claude.com/docs/en/skills.md | Fri 23 Oct 2026 08:11:41 AM UTC | 114542; `6b070e872dea28905a7ea7f45c4d5960f5bdf28cc73ac808799af6d50435ffbd` |
| vscode-html | https://code.visualstudio.com/docs/agent-customization/prompt-files | Fri 23 Oct 2026 08:13:02 AM UTC | 133911; `9cd80a9a074c3a7f2b1ef2be9b775fdf9aa2c5cf558ca19851954fa9edfc4061` |
| cursor-help-skills | https://cursor.com/help/customization/skills.md | Fri 23 Oct 2026 08:13:25 AM UTC | 6569; `7d551fc7939d4632228c7f178f89475113a1ad503000f890271ee95a4aee3a49` |
| opencode-pinned | https://raw.githubusercontent.com/anomalyco/opencode/4e0bc52216d91c3a8d10035837b1b6f9b82fd1d3/services/www/src/docs/content/commands.mdx | Fri 23 Oct 2026 08:17:10 AM UTC | 7242; `dda6bba03043afff71a0bec4f0cfa40aaac12d53c1b20358df15e557c1a7ec11` |

`vscode-migration.body:168` independently states Copilot sessions do not load prompt files and Local sessions remain supported. `vscode-html.body:1605-1618` contains the same Local-only statement and workspace location table. These corroborate scope, not a second independent authority.

Sandbox setup, exit 0, no output:

```sh
timeout 120 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r58/CriticCensus && timeout 30 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git -C /fast/scratch/hyaku/kotoba-r58/CriticCensus checkout -q 3de87aad29e960c95ed35840442f424c48c29729
```

Read-only registry comparison, exit 0, no output:

```sh
timeout 15 git --no-optional-locks -C /fast/scratch/hyaku/kotoba-r58/CriticCensus diff --exit-code f56f6e191762c27c1aa2af11a204db9e2ca4edec 3de87aad29e960c95ed35840442f424c48c29729 -- corpus/SOURCES.md
```

Claude alias comparison, exit 0, no output:

```sh
timeout 5 cmp /fast/scratch/hyaku/kotoba-r58/CriticCensus/claude.body /fast/scratch/hyaku/kotoba-r58/CriticCensus/claude-skills.body
```

The string diagnostics were bounded Eval calculations on already displayed source strings; they imported no lane code, performed no lane writes, and returned the output transcribed above. No full counter, self-test, build, lint, formatter, model call, browser, or alternate judging runtime was invoked. No tools were installed or updated. No silent-client claim is made, so no Q30 silence sweep is asserted. Only this scoped report was written in the lane.
