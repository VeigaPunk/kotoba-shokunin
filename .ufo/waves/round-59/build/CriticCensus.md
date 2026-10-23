Result: MIXED — All six frozen lead tokens are documented hook-configuration locations, but E5 does not establish independent client surfaces, opencode's exclusion rationale overstates exclusivity, and real vendor pages support stronger semantic/provenance counterexamples than the controls exercised.

# Scope and axes

Seat: `KotobaR59.CriticCensus`; recipient/integrator: `KotobaR59` only. This is a scoped attack report, not a claim-admission or native-judge verdict.

Reviewed the C1 census at freeze `4b2125c91ea1868a83b7b28eb4bbbacc35f469fe`, the addendum at `67b68e0f9a0c48e5aa5ced63e6117cfca69da491`, the frozen counter source, all seven W0 census reports, and the relevant controls. The census table is `plans/round-59.md:63-81`; those lines are unchanged by the addendum. Counter SHA observed in my freeze clone: `f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71`; targets at `verifiers/check_hook_files.py:253-254` remain 4 and 5.

Axes considered: **depth** (the assigned claim: actionable, technically correct configuration detail); **calibration** (what the census/counter actually establishes); **operability** (scope/runtime/trust distinctions); **freshness** (exact live URL and fetched bytes). These are impact labels, not additional round claims or scores. No counter, rule, target or client population change is proposed.

All scratch paths below are under `/fast/scratch/hyaku/kotoba-r59/CriticCensus/` unless explicitly labelled W0 evidence. Only this report was written in the lane. No lane code, counter, self-test, native judge or other agent/runtime was invoked. The falsifier below is static analysis, explicitly not a measured counter run.

# 1. Each ELIGIBLE row: documented location versus specimen

Page aliases below name the independently fetched bytes whose full receipts appear in section 6. Quoted excerpts retain their Markdown bytes and are at most 25 words each.

| Named attack | Frozen token | Evidence and outcome | Smallest safe correction / impacted axes |
|---|---|---|---|
| **CC-1: Example laundering** | Claude Code `.claude/settings.json` | **Attack does not defeat eligibility.** `critic-claude.page:225` states hooks are defined in JSON settings files; the explicit Hook locations table at `:237-249` names the project file at `:244`. The census quote at `:910` introduces an example hook, but the file itself is not an invented example filename. | Keep the token; identify it as project settings containing a `hooks` map, not the script directory and not an unconditional enforcement guarantee. Depth, operability. |
| **CX-1: Dedicated-file invention** | Codex `~/.codex/hooks.json` | **Attack does not defeat eligibility.** `critic-codex.page:30-52` explicitly describes discovery beside active config layers, standalone `hooks.json` and inline TOML, then names this user file at `:44`. It is not merely an arbitrary script name. | Keep the token and user scope; do not imply it is the sole representation. `:64-67` says changed/non-managed definitions are skipped until trusted. Depth, operability. |
| **VS-1: Tutorial filename promoted to default** | VS Code `.github/hooks/*.json` | **Freeze already avoids the defect.** The W0 lead `.github/hooks/audit.json` is a tutorial-created filename (`critic-vscode.page:73-77`). The frozen glob is the repository source in the actual source-selection table (`:52-60`, token `:59`). It describes a discovered set of JSON configurations, not a filename the reader must literally create. | Retain the frozen glob, Preview status, repository scope and **Copilot session target**. Do not revert to `audit.json` as the default or generalize to every VS Code harness. Depth, calibration, operability. |
| **CP-1: Invented personal glob** | Copilot CLI `~/.copilot/hooks/*.json` | **Attack does not defeat eligibility.** `critic-copilot.page:28`: “Copilot CLI also supports personal hooks in `~/.copilot/hooks/*.json`.” The exact pattern is printed in vendor prose; it was not synthesized from a directory and wildcard. E5 limitations are separate below. | Keep the user-level label; show the shared repository location as context, not a second first-token row. Depth, calibration. |
| **GM-1: Script folder mistaken for settings** | Gemini CLI `.gemini/settings.json` | **Attack does not defeat eligibility.** `critic-gemini.page:413`: “When you open a project with hooks defined in `.gemini/settings.json`:”. W0 configuration reference bytes independently name project/user/system layers at `/fast/scratch/hyaku/kotoba-r59/CensusGeminiCLI/geminicli.com_docs_hooks.md.body:94-100`; `:114` is a command script path, not discovery configuration. | Keep project settings, not `.gemini/hooks/`. Do not imply that defining a hook makes it immune to disabling/security settings (`critic-gemini.page:415-422`). Depth, operability. |
| **CU-1: Cloud example mistaken for universal path** | Cursor `.cursor/hooks.json` | **Attack does not defeat eligibility.** `critic-cursor.page:98` identifies Project hooks; `:112` describes project/home configuration levels. The census cloud paragraph at `:50` therefore has independent configuration-location support. | Keep project scope. Do not extrapolate every event on the page to cloud agents: `:82-104` distinguishes unsupported cloud events and self-hosted exceptions. Use the working `/docs/hooks` URL, not the previously failed `.md` route. Depth, operability, freshness. |

Important quote limitation: the 8-word VS Code control quote crosses `critic-vscode.page:59-60`; its `Hooks` word belongs to the next table row, not a sentence asserting the glob's meaning. The full row/header establishes meaning, but the counter's short quote alone does not. Encoding table pipes as `&#124;` is a disclosed storage transformation, not additional semantic evidence (`controls/CtlFabEvents.md:138-141`). Likewise the repaired Codex control quote at `controls/CtlFabSnapshot.md:184-194` joins plugin prose to a user-location bullet. Retain wider location context/anchors in the entry; do not present either clipped quote as a complete semantic proof.

# 2. E5 attacks: honest location choice, not independent identity

## E5-1 — Scope-switching can manufacture apparent differentiation

**Counterexample:** the same VS Code page that supplies the frozen repository glob also documents personal hooks in `~/.copilot/hooks/` (`critic-vscode.page:58`). At `:18` it explicitly says the editor, Copilot app and Copilot CLI share the Copilot harness and hook format. Copilot's own page documents both repository and personal locations in the same paragraph (`critic-copilot.page:28`). This is not evidence for two independent hook mechanisms or client-exclusive locations.

**What the frozen rule actually says:** E5 compares first backticked row tokens after casefold/normalisation, not the intersection of documented locations or runtime ownership (`verifiers/check_hook_files.py:774-783,891-909`). The foreign-name guard rejects `~/.copilot/hooks/` for VS Code even though VS Code documents it (`:624-629`; W0 `CensusVSCode.md:91-93`). A lexical client marker is not proof of exclusive ownership.

**Answer:** choosing the CLI personal glob is honest under the frozen exact-token E5 rule: it is real, its user scope differs from a repository glob, and the selection/motivation was disclosed before scoring at `plans/round-59.md:69-70`. It becomes a label game if the delivered prose says these are distinct client defaults, independent harnesses, or six exclusive hook locations. Absence of the *exact glob spelling* from the VS Code page does not make the personal directory CLI-exclusive.

**Smallest safe correction:** keep both frozen leads unchanged; explicitly say “VS Code — Copilot target, repository scope” and “Copilot CLI — personal/user scope”, with one shared-harness/shared-location note. Other VS Code targets require their own references (`critic-vscode.page:22-30`). No target recalculation or post-freeze E5 reinterpretation.

Impacted axes: depth, calibration, operability. This is a fixable presentation defect if clarified; asserting independence despite the shared-harness evidence is a substantive trade, not something a green counter can excuse.

## E5-2 — Six new strings is not six new runtime/file classes

`normalise()` deliberately strips one leading `~/` or `./` (`verifiers/check_hook_files.py:633-643`); Claude, Gemini and Cursor user/project spellings can therefore collapse to the same key despite different scopes. Conversely the selected Copilot personal pattern differs from the VS Code repository pattern despite the shared harness. The census is a reachable population under this token rule, not a natural taxonomy of distinct implementations. Do not use G=6, if measured later, as a saturation or full-hook-coverage claim.

# 3. opencode attacks

## OC-1 — “Only in these folders” is false; the exclusion itself still has support

The frozen rationale at `plans/round-59.md:73` says hook code lives **only** in the two banned discovery directories. Current docs source directly supplies a counterexample: `critic-opencode-v2.page:5-34` allows explicitly configured local plugin directories, including relative, absolute and `file://` entries. Exact excerpt at `:31` (10 words):

> Relative paths resolve from the config file containing the entry.

The same page differentiates those configured paths from automatic `.opencode/plugins/` discovery (`:44-64`). Even the rendered v1 page describes npm plugin installations and their cache (`critic-opencode.page:24-45`), not only those two local discovery folders. Thus “only” confuses default discovery roots with every place plugin code can reside.

**What holds:** the examined own docs describe hooks implemented/registered by plugin modules, not a dedicated settings-like hook-definition file. The named automatic roots contain the frozen banned `plugin`/`plugins` word. The v2 configured-path examples do not supply a qualifying dot-led, unbanned documented hook-config token. I found no evidence requiring a census promotion. The W0 negative is not based solely on guessed hooks URLs: `w0/Censusopencode.md:9,25-36,127-129` records its pinned current docs source, changelog and corpus legs. I also read that source/changelog evidence and searched the lane's existing plugin entry (`corpus/knowledge/plugin-manifests-round57.md:14-15,38,60`). This is not a claim that opencode lacks hooks.

**Smallest safe correction:** retain NOT ELIGIBLE under the frozen grammar; append/note a correction to the rationale: “documented hooks are plugin APIs; the named automatic discovery roots contain banned plugin segment words; configured/plugin-package alternatives do not provide a qualifying hook-config token in this census.” Do not rewrite the historical freeze, invent a hooks file, or change the target.

Impacted axes: depth and calibration. The exclusion and the overbroad explanation are separate propositions.

## OC-2 — The counter could promote an ordinary config file the census correctly rejected

`critic-opencode.page:51-53` offers this exact 20-word excerpt:

```text
Plugins are loaded from all sources and all hooks run in sequence. The load order is:

1. Global config (`~/.config/opencode/opencode.json`)
```

The token is grammatically admissible, `hooks` occurs outside it, and real identifiers `tool.execute.before` / `tool.execute.after` occur at `:192-193`. The actual role of the file is selecting plugin packages (`:24-32`); the modules return hooks (`:64-65`). Calling it the hook-definition file would launder a load-order mention into a semantic claim.

[INFERENCE, not executed] With a new source id, the genuine fetched page/pin, the excerpt in Gate, aligned cells and real events, the counter has no hook-config-role test that rejects this row. `https://opencode.ai/docs/plugins.md` is not the raw pinned URL used by base S087; it is a different URL key. The token is already held, so this is not evidence of additional new ground. It is evidence that the census's semantic exclusion is stronger than the mechanical checks.

Smallest safe correction: keep opencode excluded; make source reviewers check *what the path configures*, not just hook-word proximity. Depth, calibration.

# 4. Strongest real-input shortcut: wrong destinations on real vendor hosts

## HOST-1 — An official hooks page can mechanically back a non-config token

All following pages were independently opened successfully. These are exact excerpts, with no Markdown bytes stripped; every excerpt is 6–25 words. Each token passes the frozen path/foreign-marker grammar. Every page also prints the listed **real hook events**, so the pre-freeze event-semantics addendum does not address this attack.

| Client | False “Hook config” lead | Actual role | Real Events pair | Page/quote lines |
|---|---|---|---|---|
| Claude Code | `.claude/hooks/no-rm.sh` | Example executed script in an error message | `PreToolUse`, `PostToolUse` | `critic-claude.page:848`; events `:37,40` |
| Codex | `~/.codex/hooks/session_start.py` | A command handler's Python script | `PreToolUse`, `SessionStart` | `critic-codex.page:96-99`; events `:25,27` |
| VS Code | `.github/hooks/log-tool-use.cjs` | JavaScript invoked by the hook config | `sessionStart`, `preToolUse` | `critic-vscode.page:82-86`; events `:128,130` |
| Gemini CLI | `.gemini/hook-cache.json` | Cached results explicitly described as cache | `BeforeTool`, `AfterModel` | `critic-gemini.page:386-387`; events `:31` |
| Cursor | `~/.cursor/hooks/format.sh` | Hook script, explicitly not `hooks.json` | `preToolUse`, `postToolUse` | `critic-cursor.page:127`; events `:860,897` |

Claude excerpt, 10 words:
```text
PreToolUse:Bash hook error: [${CLAUDE_PROJECT_DIR}/.claude/hooks/no-rm.sh]: Blocked: rm commands are not allowed
```
Codex excerpt, 8 words:
```text
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.codex/hooks/session_start.py",
```
VS Code excerpt, 10 words:
```text
  "hooks": {
    "preToolUse": [
      {
        "type": "command",
        "command": "node .github/hooks/log-tool-use.cjs",
```
Gemini excerpt, 7 words:
```text
# Ignore hook cache and logs
.gemini/hook-cache.json
```
Cursor excerpt, 6 words:
```text
Create your hook script at `~/.cursor/hooks/format.sh`:
```

Why these are stronger than the controls: `entry_row_verdict()` checks token/word proximity, metadata labels, Gate and matching snapshot bytes (`verifiers/check_hook_files.py:786-866`); `page_why()` checks only text/token/event presence (`:1022-1055`). Neither checks whether the path is the configuration loaded by the client. The action cell only needs three words (`:912-914`). Each false row can use the actual complete vendor page as its snapshot, with its honest digest, and the same new hook-page URL as the intended row. No counterfeit host, fabricated event, nonexistent URL or altered counter is needed.

Observed base search: case-insensitive fixed-string search for all five false destinations against `a975cbbf` outside `.ufo` returned no matches, exit 1 (command below). The six original census keys likewise returned no matches, exit 1. Therefore these five paths are not blocked by held-token occurrence, including case variants.

[INFERENCE, not executed] Substitute these five false destinations/quotes into an otherwise format-complete six-row world, retaining the real Copilot CLI personal row and genuine snapshots/events. Every apparent F/G member is still novel and distinct; the frozen code predicts F=6, G=6 although five cells misidentify the configuration destination. This is a static counterexample, **not** a claimed passing mutation receipt. `controls/CtlOffTopic.md:145-158` explicitly limits its own off-topic control to banned command/prompt tokens (K=0) and no live counter fetches; it does not rule out this real-page shortcut.

**Smallest safe correction:** do not change the counter. Extend the existing human cell review to the Hook config cell: require the full source context to identify the path as hook-definition/discovery input, classify config versus executed script/cache/log/import list, and record the decision. The actual six frozen leads survive that review; the counter must not be described as proving this semantic property. The canonical judge, not this seat, decides whether the residual measurement gap is acceptable.

Impacted axes: depth primarily; calibration and operability if the wrong destination is accepted. A green predicate over these wrong destinations would not repair the reader-facing defect.

# 5. Fabricated-source provenance attacks

## PROV-1 — Matching text does not authenticate the complete snapshot

Observed control evidence, not re-run here: `controls/CtlFabSnapshot.md:86-117` records fabricated pages accepted offline (S=6) and rejected live (F=0) because their **invented quotes** were absent; its restored world passed at `:134-145`. That establishes the invented-quote detector, not byte-for-byte snapshot provenance.

[INFERENCE, not executed] A stronger counterfeit snapshot preserves an actual vendor quote plus the actual two event names, fabricates all remaining bytes (or uses a tiny synthetic wrapper), and self-pins its digest in SOURCES. `entry_row_verdict()` checks that self-pin against the committed snapshot; live `fetch()` and `page_why()` check the real page for the shared quote/token/events, not equality to the snapshot digest (`verifiers/check_hook_files.py:848-865,1042-1055,1085-1106`). All six genuine pages provide those strings. Such a constructed snapshot is not a fetched page merely because both textual checks can succeed.

Smallest safe correction: independently match every committed S096–S101 snapshot and SOURCES digest to the raw bytes recorded by its ordinary fetch receipt; retain the capture's UTC/URL/status/byte-count/digest. Keep the counter unchanged and state that capture provenance is reviewed separately. Do not strengthen the control summary's “live conjunct rejects fabricated worlds” into “live conjunct authenticates the full snapshot.” Depth, calibration, freshness.

## PROV-2 — `docs`/`A` labels do not make an arbitrary claim authoritative

The source parser tests declared kind/tier/status/date and host/path rules; it does not evaluate the source row's scope, anchor or teaches proposition (`verifiers/check_hook_files.py:825-847`). `host_ok()` admits pinned-host paths (and subdomains for bare host pins), not a semantic documentation class (`:580-593`). A fabricated teaches assertion can therefore accompany a genuine hook quote, or a real page can be made off-topic by the false path roles in HOST-1.

This is **not** evidence that an arbitrary invented URL passes: HTTP 200 and live matching remain required, and the fabricated-quote control failed as intended. No hostile subdomain or unauthorized hosted content was discovered or attempted. The concrete evidence is real official pages with irrelevant path/event interpretations, not a speculative host takeover.

Smallest safe correction: source reviewer verifies the whole scoped teaches claim and its anchor against context, not just host/quote/hash. Report the counter's actual extent per Q31, not blanket anti-fabrication coverage. Depth, calibration.

# 6. Reproducible access and command evidence

Clone command, exit 0; no sandbox commit made:
```sh
timeout 120s env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r59/CriticCensus && timeout 30s env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git -C /fast/scratch/hyaku/kotoba-r59/CriticCensus checkout -q 4b2125c91ea1868a83b7b28eb4bbbacc35f469fe
```

Fetch command form, one invocation per URL, cwd the clone; each complete command exited 0 and the final URL equalled the requested URL:
```sh
timeout 5s date -u && timeout 40s curl -sSL --max-time 30 -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' -H 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8' -o <file> -w '\nHTTP %{http_code}; final %{url_effective}; bytes %{size_download}\n' <URL> && timeout 10s sha256sum <file> && timeout 10s wc -c <file>
```

Literal `date -u` output lines:
- First four fetches: `Fri 23 Oct 2026 09:35:55 AM UTC`
- Gemini, Cursor and rendered opencode: `Fri 23 Oct 2026 09:36:10 AM UTC`
- Pinned v2 opencode source: `Fri 23 Oct 2026 09:38:25 AM UTC`

| File | Requested/final URL | HTTP | curl bytes = wc bytes | sha256 |
|---|---|---|---|---|
| critic-claude.page | https://code.claude.com/docs/en/hooks.md | 200 | 274129 | c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8 |
| critic-codex.page | https://learn.chatgpt.com/docs/hooks.md | 200 | 47133 | 57166ef03e7059732dd90925d5c42dd4d187eb2625d66cc154d0fbd2edb65f92 |
| critic-vscode.page | https://code.visualstudio.com/docs/agent-customization/hooks.md | 200 | 15152 | 98c5be6b693a19ccd10c79b933d56e010101cef5a0eed699bd25e80289461e08 |
| critic-copilot.page | https://docs.github.com/en/copilot/concepts/customizations/hooks.md | 200 | 8428 | 23370e092d2e2e81587b84038d0be116d99243a83c810b8e8cd41cf8734a10f4 |
| critic-gemini.page | https://geminicli.com/docs/hooks/best-practices.md | 200 | 17650 | fb44fbcfaccc3cdb7895d989f3808bed66cfa6516411535c4c4d9077d242e7bc |
| critic-cursor.page | https://cursor.com/docs/hooks | 200 | 69145 | 8436af768468590299c1beab9ea34bff8c5f1e5649ae244a989c28960dd2c88d |
| critic-opencode.page | https://opencode.ai/docs/plugins.md | 200 | 9357 | c76613823185b6bf7f6a164211bcdc7bba3bc738aba1cc927b51189f8da8681e |
| critic-opencode-v2.page | https://raw.githubusercontent.com/anomalyco/opencode/74f8d4860f49c563909e6b039b0cc8b454ebce72/services/www/src/docs/content/plugins.mdx | 200 | 4371 | 39afa29948069c9e8d95ba812ee1701535912a7e5ce3ed7fef5d4ba6d7521fd3 |

No response challenge was passed or browser used. The failed Cursor `.md` route was not retried to reconfirm the reported failure; the known plain route was opened directly. All seven rendered-page hashes equal the relevant W0/control capture hashes; the v2 hash equals the W0 pinned-source capture.

Read-only command receipts:
- `timeout 30s git --no-optional-locks show 4b2125c91ea1868a83b7b28eb4bbbacc35f469fe:plans/round-59.md` in lane: exit 0, census/targets reproduced.
- `timeout 30s git --no-optional-locks show 67b68e0f9a0c48e5aa5ced63e6117cfca69da491 -- plans/round-59.md` in lane: exit 0, only the pre-data Events-semantics addendum shown.
- `timeout 10s sha256sum verifiers/check_hook_files.py` in clone: exit 0, `f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71  verifiers/check_hook_files.py`.

Normalized original-token search, cwd lane, exit 1, stdout/stderr empty:
```sh
timeout 30s git --no-optional-locks grep -inF -e '.claude/settings.json' -e '.codex/hooks.json' -e '.github/hooks/*.json' -e '.copilot/hooks/*.json' -e '.gemini/settings.json' -e '.cursor/hooks.json' a975cbbf00534443c49bf02e29c813a3db0bf0f8 -- . ':!.ufo'
```
Stronger shortcut-token search, cwd lane, exit 1, stdout/stderr empty:
```sh
timeout 30s git --no-optional-locks grep -inF -e '.claude/hooks/no-rm.sh' -e '.codex/hooks/session_start.py' -e '.github/hooks/log-tool-use.cjs' -e '.gemini/hook-cache.json' -e '.cursor/hooks/format.sh' a975cbbf00534443c49bf02e29c813a3db0bf0f8 -- . ':!.ufo'
```
These are read-only occurrence searches, not counter executions; zero case-insensitive literal matches is stronger than needing zero boundary-qualified matches for these exact normalized keys.

No tools installed or updated. No subagents dispatched; no paid model calls, lane Git/jj writes, pushes, fleet-root/sibling writes, load tests or shared-process kills. Counter/build/lint/test verification was not run. No S102 supporting row is needed for this review. Corrections above are recommendations for the sole integrator; this report applies none.

Report: .ufo/waves/round-59/build/CriticCensus.md
