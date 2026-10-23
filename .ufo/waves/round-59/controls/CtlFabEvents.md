Result: DONE — CtlFabEvents: S 0 of 6; F 0 of 6; G 0; exit 1; predicate NOT MET

# Control `CtlFabEvents` — events-fabricated world, claim C1 (round 59)

Control name: **CtlFabEvents**. World: real census tokens, real URLs, real quotes, real committed page snapshots; every
`SKILL.md` Events cell holds invented event names. Built and scored in the sandbox clone only; the lane was not touched.

## Receipt

- Control: `CtlFabEvents`
- Sandbox commit: `sandbox 39dd1caa7adcc2511b8b6a96a1e7cf13f1083421 (/fast/scratch/hyaku/kotoba-r59/CtlFabEvents)`
  (parent `67b68e0f9a0c48e5aa5ced63e6117cfca69da491`; one commit, 11 files, +8413/−0)
- Counter sha256, pasted from the clone:

```
$ sha256sum verifiers/check_hook_files.py
f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71  verifiers/check_hook_files.py
```

  Equal to the frozen sha256 (`git show 67b68e0f…:verifiers/check_hook_files.py | sha256sum` → same hex). `TARGET = 4`,
  `NEW_TARGET = 5` read from that committed file at lines 253-254.
- Exact command (run from the clone root, `timeout 900`):

```
timeout 900 python3 -B verifiers/check_hook_files.py --rev 39dd1caa7adcc2511b8b6a96a1e7cf13f1083421 --fetch
```

- Full stdout, exit code `1`:

```
hook files backed on committed snapshots 0 of 6; found on the live page 0 of 6; new ground 0
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev 39dd1caa7adcc2511b8b6a96a1e7cf13f1083421
reject Claude Code: entry row S096: snapshot .ufo/waves/round-59/snapshots/S096.page: event 'BeforeHookRun' is not on the page; snapshot .ufo/waves/round-59/snapshots/S096.page: event 'afterSessionPing' is not on the page
reject Codex: entry row S097: snapshot .ufo/waves/round-59/snapshots/S097.page: event 'preHookResolve' is not on the page; snapshot .ufo/waves/round-59/snapshots/S097.page: event 'onHookFire' is not on the page
reject VS Code: entry row S098: snapshot .ufo/waves/round-59/snapshots/S098.page: event 'afterToolSettle' is not on the page; snapshot .ufo/waves/round-59/snapshots/S098.page: event 'BeforeHookRun' is not on the page
reject Copilot CLI: entry row S099: snapshot .ufo/waves/round-59/snapshots/S099.page: event 'prePromptHook' is not on the page; snapshot .ufo/waves/round-59/snapshots/S099.page: event 'afterAgentIdle' is not on the page
reject Gemini CLI: entry row S100: snapshot .ufo/waves/round-59/snapshots/S100.page: event 'BeforeHookRun' is not on the page; snapshot .ufo/waves/round-59/snapshots/S100.page: event 'postHookSweep' is not on the page
reject Cursor: entry row S101: snapshot .ufo/waves/round-59/snapshots/S101.page: event 'preHookResolve' is not on the page; snapshot .ufo/waves/round-59/snapshots/S101.page: event 'afterSessionPing' is not on the page
reject opencode: SKILL.md hook token '.opencode/plugins/' is not well-formed; entry row S102: quote holds no hook/hooks word outside the token; snapshot .ufo/waves/round-59/snapshots/S102.page: event 'BeforeHookRun' is not on the page; snapshot .ufo/waves/round-59/snapshots/S102.page: event 'afterSessionPing' is not on the page
```

- Same command without `--fetch`, exit code `1`:

```
hook files backed on committed snapshots 0 of 6; live not run; new ground 0
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev 39dd1caa7adcc2511b8b6a96a1e7cf13f1083421
reject Claude Code: entry row S096: snapshot .ufo/waves/round-59/snapshots/S096.page: event 'BeforeHookRun' is not on the page; snapshot .ufo/waves/round-59/snapshots/S096.page: event 'afterSessionPing' is not on the page
reject Codex: entry row S097: snapshot .ufo/waves/round-59/snapshots/S097.page: event 'preHookResolve' is not on the page; snapshot .ufo/waves/round-59/snapshots/S097.page: event 'onHookFire' is not on the page
reject VS Code: entry row S098: snapshot .ufo/waves/round-59/snapshots/S098.page: event 'afterToolSettle' is not on the page; snapshot .ufo/waves/round-59/snapshots/S098.page: event 'BeforeHookRun' is not on the page
reject Copilot CLI: entry row S099: snapshot .ufo/waves/round-59/snapshots/S099.page: event 'prePromptHook' is not on the page; snapshot .ufo/waves/round-59/snapshots/S099.page: event 'afterAgentIdle' is not on the page
reject Gemini CLI: entry row S100: snapshot .ufo/waves/round-59/snapshots/S100.page: event 'BeforeHookRun' is not on the page; snapshot .ufo/waves/round-59/snapshots/S100.page: event 'postHookSweep' is not on the page
reject Cursor: entry row S101: snapshot .ufo/waves/round-59/snapshots/S101.page: event 'preHookResolve' is not on the page; snapshot .ufo/waves/round-59/snapshots/S101.page: event 'afterSessionPing' is not on the page
reject opencode: SKILL.md hook token '.opencode/plugins/' is not well-formed; entry row S102: quote holds no hook/hooks word outside the token; snapshot .ufo/waves/round-59/snapshots/S102.page: event 'BeforeHookRun' is not on the page; snapshot .ufo/waves/round-59/snapshots/S102.page: event 'afterSessionPing' is not on the page
```

- `C1 predicate: --fetch exit 0 (F>=TARGET, G>=NEW_TARGET) — NOT MET`

## What the world contains

`SKILL.md` gains `### Hook files by client` with the frozen header `| Client | Hook config | Events | Action |`, one row
per census client, the census token as the first backticked span of the Hook config cell, an action cell of >= 3 words,
and an Events cell of two invented identifiers:

| Client | token (census) | Events cell (invented) |
|---|---|---|
| Claude Code | `.claude/settings.json` | `BeforeHookRun`, `afterSessionPing` |
| Codex | `~/.codex/hooks.json` | `preHookResolve`, `onHookFire` |
| VS Code | `.github/hooks/*.json` | `afterToolSettle`, `BeforeHookRun` |
| Copilot CLI | `~/.copilot/hooks/*.json` | `prePromptHook`, `afterAgentIdle` |
| Gemini CLI | `.gemini/settings.json` | `BeforeHookRun`, `postHookSweep` |
| Cursor | `.cursor/hooks.json` | `preHookResolve`, `afterSessionPing` |
| opencode | `.opencode/plugins/` | `BeforeHookRun`, `afterSessionPing` |

Everything else is real and checked by the counter: `corpus/knowledge/hook-files-round59.md` (entry table
`| Client | Hook config | Source | Quote |`, one quote per row, 8–24 words), seven `corpus/SOURCES.md` rows S096–S102
(`docs` / `A` / `mined` / `2026-10-23`, new URL per `url_key`, no change-note or tracker path, full 64-hex sha256 in the
row), `corpus/lessons/round-59.md` `## Gate` recording every quote, and seven committed snapshots
`.ufo/waves/round-59/snapshots/S096.page` … `S102.page` whose sha256 equals the row sha256 (`git cat-file -p
HEAD:.ufo/waves/round-59/snapshots/S096.page | sha256sum` → `c6ef9d21…`; `S101.page` → `8436af76…`).

## Evidence that the Events conjunct is the only failure

Every reject reason for the six rows in K is the Events conjunct, nothing else: no token, quote, source, gate or snapshot
reason appears. opencode is out of K by the frozen census (its token holds the banned segment `plugins`), so its extra
reasons are expected and outside the control's scope.

Because the counter fetches only rows that are already backed, the `--fetch` run above issued **zero HTTP requests** —
measured, not inferred: a re-run with a logging `curl` shim first on `PATH` (it appends every invocation to a log and
exits 1) printed the same summary line and left no log at all (`wc -l` on the log → absent = 0 invocations), exit 1.
So `found 0 of 6` is not evidence about the live pages. The live side was checked separately by applying the
counter's own `page_why` / `event_text` to the bytes fetched for the snapshots — i.e. the live bodies:

```
Claude Code  S096 words=21 live quote+token -> []  live events -> ["event 'BeforeHookRun' is not on the page", "event 'afterSessionPing' is not on the page"]
Codex        S097 words=22 live quote+token -> []  live events -> ["event 'preHookResolve' is not on the page", "event 'onHookFire' is not on the page"]
VS Code      S098 words=24 live quote+token -> []  live events -> ["event 'afterToolSettle' is not on the page", "event 'BeforeHookRun' is not on the page"]
Copilot CLI  S099 words= 8 live quote+token -> []  live events -> ["event 'prePromptHook' is not on the page", "event 'afterAgentIdle' is not on the page"]
Gemini CLI   S100 words=10 live quote+token -> []  live events -> ["event 'BeforeHookRun' is not on the page", "event 'postHookSweep' is not on the page"]
Cursor       S101 words=24 live quote+token -> []  live events -> ["event 'preHookResolve' is not on the page", "event 'afterSessionPing' is not on the page"]
opencode     S102 words=14 live quote+token -> []  live events -> ["event 'BeforeHookRun' is not on the page", "event 'afterSessionPing' is not on the page"]
```

So the world would be backed and found on every in-K row if the Events cells held names the pages print; the invented
names alone take S, F and G to 0.

## Fetches (one per page, ordinary curl, no challenge, no browser)

`date -u` at fetch start: `Fri 23 Oct 2026 09:21:27 AM UTC`; end `Fri 23 Oct 2026 09:21:31 AM UTC`; Cursor re-route
`09:21:45 AM UTC`. Command form: `curl -sSL --max-time 30 -A '<Chrome 130 UA>' -H 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8' -o <file> -w '%{http_code} %{url_effective} %{size_download}' <url>` (the counter's own header set).

| row | URL | HTTP | bytes | sha256 |
|---|---|---|---|---|
| S096 | https://code.claude.com/docs/en/hooks.md | 200 | 274129 | `c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8` |
| S097 | https://learn.chatgpt.com/docs/hooks.md | 200 | 47133 | `57166ef03e7059732dd90925d5c42dd4d187eb2625d66cc154d0fbd2edb65f92` |
| S098 | https://code.visualstudio.com/docs/agent-customization/hooks.md | 200 | 15152 | `98c5be6b693a19ccd10c79b933d56e010101cef5a0eed699bd25e80289461e08` |
| S099 | https://docs.github.com/en/copilot/concepts/customizations/hooks.md | 200 | 8428 | `23370e092d2e2e81587b84038d0be116d99243a83c810b8e8cd41cf8734a10f4` |
| S100 | https://geminicli.com/docs/hooks/best-practices.md | 200 | 17650 | `fb44fbcfaccc3cdb7895d989f3808bed66cfa6516411535c4c4d9077d242e7bc` |
| S101 | https://cursor.com/docs/hooks.md | **404** | 389 | `4f98eb063d1914a3100f2c7e6bab3a449877d33da375eb3c05edc3a61e78afb1` |
| S101 | https://cursor.com/docs/hooks (the URL the row cites) | 200 | 69145 | `8436af768468590299c1beab9ea34bff8c5f1e5649ae244a989c28960dd2c88d` |
| S102 | https://opencode.ai/docs/plugins.md | 200 | 9357 | `c76613823185b6bf7f6a164211bcdc7bba3bc738aba1cc927b51189f8da8681e` |

The Cursor row cites `https://cursor.com/docs/hooks`: the `.md` route answered 404 to the counter's header set at
09:21:27Z, and the non-`.md` route returned the markdown body byte-identical to the census's `hooks.md` bytes
(`8436af76…`, the census saved the same sha256). Under `url_key` the two routes are one URL.

## Findings for the L1 (no rule changed, no lane edit)

1. **Events conjunct works as the control intended.** Invented identifiers are rejected on the snapshot and on the live
   body; the six otherwise-valid rows all fail on exactly that conjunct.
2. **`--fetch` never fetches an unbacked row.** The live check is downstream of backing, so a control (or a build) whose
   rows fail any static conjunct cannot be distinguished from one that fails live; the live page has to be checked
   separately, as done above.
3. **A quote cannot carry an HTML-tag-shaped token.** `norm_page_case` drops `</?[A-Za-z][^>]*>`, while `norm(quote)`
   keeps angle-bracket text. The Codex page's token line sits after the bullets `<repo>/.codex/hooks.json` and
   `<repo>/.codex/config.toml`, so any quote containing those bullets is "not on the page". The S097 quote therefore
   starts before them (`a default `hooks/hooks.json` file. … - `~/.codex/hooks.json``, 22 words) and stops at the token.
   The build wave must avoid quoting any `<…>` text.
4. **VS Code's census token lives only inside a table row.** `.github/hooks/*.json` occurs once, in the "Choose a hook
   source" table, and the nearest hook word outside the token is in an adjacent row, so the S098 quote spans the row
   boundary with the pipes written `&#124;` (the counter unescapes them). Any future VS Code quote on that page has the
   same constraint.
5. **opencode stays out of K** (token segment `plugins` is banned); its row is present for completeness and carries an
   invented Events cell like the others.

## Files written in the sandbox (commit `39dd1caa`)

- `SKILL.md` (+14: the `### Hook files by client` section)
- `corpus/knowledge/hook-files-round59.md` (new, 39 lines)
- `corpus/SOURCES.md` (+8: rows S096–S102)
- `corpus/lessons/round-59.md` (new, 25 lines, `## Gate`)
- `.ufo/waves/round-59/snapshots/S096.page` … `S102.page` (new, the fetched bytes)

Nothing was written in the lane, the fleet root or a sibling lane. No tool was installed or upgraded. No lane git/jj
write was made; the only git writes are the one sandbox commit and the sandbox `add` that preceded it.
