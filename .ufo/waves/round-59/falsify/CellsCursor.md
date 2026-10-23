Result: BREAKS — every Cursor Events span is a real hook event, but the blanket cloud-agent `sessionStart` exclusion contradicts the same page's self-hosted-worker exception.

## Scope and axes

Reviewed the Cursor row at `SKILL.md:132` and its entry at `corpus/knowledge/hook-files-round59.md:28,50-53`, frozen at `c63ccc6823e1f6a8577acbb43d19551eadbbee9a`. The semantic attack is on field/action meaning, not the frozen counter, predicate, targets, or C1 receipt. The plan's pre-registered semantic review is at `plans/round-59.md:93-98`.

Impacted axes: **depth** (an execution-surface distinction is lost) and **calibration** (the exclusion is broader than its source permits). No source drift was observed: the reopened page matches the committed snapshot digest. This is a fixable documentation defect, not a necessary tradeoff; this report makes no admission, axis-score, or whole-round no-harm judgment.

## Provenance and observed commands

All source reads and fetched bytes used the sandbox `/fast/scratch/hyaku/kotoba-r59/CellsCursor`; no lane code was executed. Sandbox creation command, exit 0, no output:

```sh
unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE; timeout 90 git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r59/CellsCursor && timeout 30 git -C /fast/scratch/hyaku/kotoba-r59/CellsCursor checkout -q c63ccc6823e1f6a8577acbb43d19551eadbbee9a
```

Opened the cited URL by ordinary curl. Command, run with that sandbox as cwd, exit 0:

```sh
timeout 5 date -u && timeout 75 curl -sSL --max-time 60 -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' -H 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8' --dump-header /fast/scratch/hyaku/kotoba-r59/CellsCursor/S101-live.headers --output /fast/scratch/hyaku/kotoba-r59/CellsCursor/S101-live.page --write-out 'HTTP status: %{http_code}\nURL: %{url_effective}\nDownloaded bytes: %{size_download}\n' https://cursor.com/docs/hooks && timeout 5 wc -c /fast/scratch/hyaku/kotoba-r59/CellsCursor/S101-live.page .ufo/waves/round-59/snapshots/S101.page && timeout 5 sha256sum /fast/scratch/hyaku/kotoba-r59/CellsCursor/S101-live.page .ufo/waves/round-59/snapshots/S101.page
```

Observed output:

```text
Fri 23 Oct 2026 09:53:01 AM UTC
HTTP status: 200
URL: https://cursor.com/docs/hooks
Downloaded bytes: 69145
 69145 /fast/scratch/hyaku/kotoba-r59/CellsCursor/S101-live.page
 69145 .ufo/waves/round-59/snapshots/S101.page
138290 total
8436af768468590299c1beab9ea34bff8c5f1e5649ae244a989c28960dd2c88d  /fast/scratch/hyaku/kotoba-r59/CellsCursor/S101-live.page
8436af768468590299c1beab9ea34bff8c5f1e5649ae244a989c28960dd2c88d  .ufo/waves/round-59/snapshots/S101.page
```

`S101-live.headers:1,4` records HTTP/2 200 and `content-type: text/markdown; charset=utf-8`. This digest also equals `corpus/SOURCES.md:113` S101. Below, page line numbers refer to both `.ufo/waves/round-59/snapshots/S101.page` and the reopened `S101-live.page` in this sandbox. No Markdown, backticks, or other bytes were stripped from the quotations. Each quoted excerpt is at most 25 words.

## Exact page evidence

| Evidence | Page line | Verbatim excerpt |
|---|---:|---|
| Q1 | 26 | “- `sessionStart` / `sessionEnd` - Session lifecycle management” |
| Q2 | 27 | “- `preToolUse` / `postToolUse` / `postToolUseFailure` - Generic tool use hooks (fires for all tools)” |
| Q3 | 50 | “If you have hooks defined in `.cursor/hooks.json` at the root of your project, cloud agents pick them up and run them during their work.” |
| Q4 | 102 | “User-level hooks (`~/.cursor/hooks.json`) are not available in cloud agents.” |
| Q5 | 88 | “Deferred while cloud agents can still start in a read-only environment.” |
| Q6 | 104 | “On those workers, `sessionStart` and `sessionEnd` fire when a session claims the worker and when that claim is released.” |
| Q7 | 648 | “`<project-root>/.cursor/hooks.json`” |
| Q8 | 649 | “Project hooks run in any trusted workspace” |
| Q9 | 781 | “- Require the workspace to be trusted to run (for security)” |
| Q10 | 1340 | “Called when a new composer conversation is created.” |
| Q11 | 54 | “Hooks do not run during those turns. They start once the agent has a writable environment.” |
| Q12 | 108 | “Cloud agents run **command-based hooks** only.” |
| Q13 | 862 | “Called before any tool execution.” |
| Q14 | 899 | “Called after successful tool execution. Useful for auditing, analytics, and injecting context.” |

Q6's antecedent is explicit on the same line: Self-Hosted Machines workers, comprising Pools and My Machines, within the page's Cloud agent support section (`:48-108`). It is not an event from another client or a substring match.

## EVERY backticked span in the Events cell

The cell has three backticked spans, including the one inside its parenthetical qualifier. None is ruled `not an event`.

| Span at `SKILL.md:132` | Ruling | Semantic evidence |
|---|---|---|
| `preToolUse` | **event** | Q2 explicitly calls it a generic tool-use hook; `:66` marks cloud support Yes; heading `:860` and Q13 define its before-tool trigger. |
| `postToolUse` | **event** | Q2 calls it a generic tool-use hook; the cited `:67` marks cloud support Yes; heading `:897` and Q14 define its after-success trigger. |
| `sessionStart` | **event** | Q1 identifies session lifecycle management; heading `:1338` and Q10 define its trigger; Q6 additionally defines its worker-claim trigger. Its surrounding cloud exclusion is a separate, failing scope claim. |

Thus the Events-conjunct semantic safeguard holds for identifier identity, but does not establish that the availability qualifier is accurate.

## Every SKILL parenthetical reference and Hook config / Action claim

| Cell / reference | Ruling | Evidence and limit |
|---|---|---|
| Hook config: `.cursor/hooks.json` is project configuration | **supported** | Q3 and Q7 state the project/root location. The printed `S101 :102` supports the user-level exclusion, not this project-location label; adding `:50` would make the locator complete. |
| Hook config: user file unavailable to cloud agents (`S101 :102`) | **supported** | Q4 directly states this, naming the user file. |
| Events: `preToolUse`, `postToolUse` (`S101 :27, :67`) | **supported** | Q2 names both as hook events; `:67` is specifically the cloud-support row for `postToolUse`. `:66` is the adjacent cloud-support row for `preToolUse`. No mistaken event identity or line offset. |
| Events parenthesis: `sessionStart` is not run for cloud agents (`:88`) | **overstated — BREAKS** | Q5 and the heading at `:82` support the default hosted-cloud exclusion, but Q6 explicitly documents the self-hosted-worker exception. Citing `:88` without `:104` turns a surface-specific exclusion into a blanket one. |
| Action: keep cloud-agent checks in the project file (`S101 :649, :781`) | **supported as routing advice, not an exclusive-source or always-run guarantee** | Q3 is direct cloud/project evidence; `:98` lists project hooks as a cloud configuration source. `:649,781` establish project/trust behavior, not cloud-source selection. Other cloud sources at `:99-100` do not contradict the advice because the cell does not say project is the only source. |
| Action: project hooks run only in a trusted workspace (`S101 :649, :781`) | **supported** | Q8 states the positive trusted-workspace case; Q9 explicitly supplies the necessary trust condition. No need to infer “only” from Q8 alone. |

Cloud qualifications must not be read as an unconditional must-run promise: Q11 excludes early read-only exploratory turns (`:54` supplies the antecedent), and Q12 restricts cloud execution to command-based hooks. The Action cell itself does not promise execution on every turn; these are source limits, not a second demonstrated false claim in that cell.

## Entry row and EVERY Cursor-note reference

- `corpus/knowledge/hook-files-round59.md:28`: **supported**. The `.cursor/hooks.json` token is a project hook config; its quote is exactly Q3, unshaped, from page `:50`.
- Entry `:50`, reference `hooks:50`: **supported**. Project hooks are loaded for cloud work (Q3; also page `:98`). This is not evidence that hooks execute in read-only turns.
- Entry `:50-51`, reference `:102`: **supported**. The named `~/.cursor/hooks.json` user file is excluded from cloud agents by Q4.
- Entry `:51`, references `:27,67`: **supported**. Both `preToolUse` and `postToolUse` are hook events, with `postToolUse` cloud support explicitly at `:67`.
- Entry `:51`, reference `:1340`: **supported**. `sessionStart` is a lifecycle event with its creation trigger stated in Q10.
- Entry `:51`, reference `:88`: **overstated — BREAKS**, the same missing self-hosted exception Q6. This copy must be corrected with the SKILL row; leaving one unchanged would preserve contradictory scope guidance.
- Entry `:52-53`, the `.md` URL's HTTP 404 and the alternate URL's same Markdown bytes: **supported as a historical fetch receipt, not page prose**. `.ufo/waves/round-59/build/SrcCursor.md:17,21-22` records the successful `/docs/hooks` fetch/digest and the failed `.md` request, including a subsequent HTTP 404, 389-byte body. I did not rerun that reported failure. My successful alternate-URL fetch above independently matches S101's recorded digest. The source page itself is not evidence for an earlier HTTP response.

## Strongest counterexample and smallest safe correction

**Concrete counterexample:** use Cursor Self-Hosted Machines (Pools or My Machines), rather than the hosted cloud VM surface. The cited page itself says `sessionStart` fires when the worker is claimed (Q6), while both reviewed artifacts tell the reader it is not run for cloud agents. This is a documentation-level counterexample directly present in the pinned snapshot and the reopened page; no runtime hook execution is claimed.

Correct only the overbroad qualifier in **both** copies, preserving event identities and the frozen counter/rule/targets:

- `SKILL.md:132` Events cell: retain `preToolUse`, `postToolUse` and their references; replace the final exclusion with: “hosted cloud omits `sessionStart`, :88; self-hosted workers fire it on session claim, :104”.
- `corpus/knowledge/hook-files-round59.md:51`: replace the exclusion with: “`sessionStart` (`:1340`) is omitted in hosted cloud agents (`:88`), but fires when a self-hosted worker is claimed (`:104`).”
- For precise positive evidence, the Hook config parenthesis can cite `S101 :50,102` and the Action can cite `S101 :50,649,781`; this is locator tightening, not a change to their supported meanings.

The L1 should record the scope correction in the round lesson. Do not remove a genuine event, change the C1 predicate, or treat the counter's lexical event presence as a semantic availability test. No lane files were edited by this seat apart from this report; no counter, tests, probes, or client CLI were run; no tools were installed or upgraded.

Report: .ufo/waves/round-59/falsify/CellsCursor.md
