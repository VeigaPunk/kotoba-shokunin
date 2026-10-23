Result: HOLDS — S098 (VS Code hooks) survived re-open: live fetch is byte-identical to the committed snapshot and matches the row's sha256, and every anchor line the row cites says what the `teaches` cell says.

# ReopenS098 — VS Code hooks row, snapshot, quote (seat report)

Seat: `KotobaR59.ReopenS098` (leaf; no subagents spawned). Sandbox used for all lane-code execution:
`/fast/scratch/hyaku/kotoba-r59/ReopenS098` at `c63ccc6823e1f6a8577acbb43d19551eadbbee9a` (`git clone -q` of the lane + `checkout -q c63ccc6…`; sandbox HEAD = `c63ccc6823e1f6a8577acbb43d19551eadbbee9a`). Lane rev read-only. No tools installed (tooling directive: no install needed; git/curl/python3 already present).

## 1. Live fetch at the row's URL (re-open)

URL from `corpus/SOURCES.md` S098 row at c63ccc6: `https://code.visualstudio.com/docs/agent-customization/hooks.md`.

Command (browser UA, curl -sSL, headers to /tmp/s098_headers.txt):
`timeout 120 curl -sSL -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36" -D /tmp/s098_headers.txt -o /tmp/s098_live.md https://code.visualstudio.com/docs/agent-customization/hooks.md`

Observed (pasted):
- `curl_exit=0`
- `Fri 23 Oct 2026 09:53:21 AM UTC` (`date -u`)
- `HTTP/2 200` (from headers file)
- `15152 /tmp/s098_live.md` (`wc -c`)
- `98c5be6b693a19ccd10c79b933d56e010101cef5a0eed699bd25e80289461e08  /tmp/s098_live.md` (`sha256sum`)
- `CMP_IDENTICAL` (`cmp /tmp/s098_live.md .ufo/waves/round-59/snapshots/S098.page`)

Row claim vs live: row says fetched 2026-10-23T09:35:04Z, HTTP 200, 15,152 B, sha256 `98c5be6b693a19ccd10c79b933d56e010101cef5a0eed699bd25e80289461e08`, exact bytes in snapshot `.ufo/waves/round-59/snapshots/S098.page` — all three quantities (status 200, 15152 B, sha256) reproduce at my fetch; the live body is byte-identical to the committed snapshot. Snapshot size `wc -c` = 15152 in the sandbox too.

## 2. Snapshot vs row sha256

`sha256sum .ufo/waves/round-59/snapshots/S098.page` = `98c5be6b693a19ccd10c79b933d56e010101cef5a0eed699bd25e80289461e08` = row sha256 (SOURCES.md:110). No drift.

## 3. Entry quote and Gate quote at stated lines

- Entry quote (knowledge entry `corpus/knowledge/hook-files-round59.md:25`):
  `Automation shared with a repository &#124; `.github/hooks/*.json` at the repository root &#124; &#124; Hooks`
  This is the fold of snapshot lines 59–60 (`| Automation shared with a repository | `github/hooks/*.json` at the repository root |` + next row `| Hooks …`), with the three literal `|` bytes written `&#124;` so the quote stays in one Markdown cell (entry lines 63–64 "Quote shaping"; lesson `corpus/lessons/round-59.md:12` records the same quote and fold). Quote is byte-faithful modulo that documented, per-cell escape; it is not a paraphrase.
- Gate quote (SKILL.md § Hook files by client, `SKILL.md:123`): `hooks act "without relying on the model to request the action" (S098 `:6`)`.
  Snapshot line 6 contains verbatim: `…or record an event without relying on the model to request the action.` — the quoted span exists. Also recorded in lesson line 18.

## 4. Anchor lines vs `teaches` cell

Row S098 `teaches` (SOURCES.md:110): "VS Code names `.github/hooks/*.json` for repository-shared hooks, distinguishes personal, settings, plugin and agent-scoped sources, and documents lifecycle events; the experience is Preview".

| teaches claim | anchor cited | snapshot line content | holds |
|---|---|---|---|
| `.github/hooks/*.json` for repository-shared hooks | `hooks.md:59` | `| Automation shared with a repository | `.github/hooks/*.json` at the repository root |` | yes |
| personal / settings / plugin / agent-scoped sources | `hooks.md:58-62` (cited by SKILL.md:129; row cites :59) | 58 `User hook files in ~/.copilot/hooks/`; 59 repo root; 60 inline `hooks` map in a supported Copilot settings file; 61 Agent plugins; 62 Agent-scoped hooks | yes |
| documents lifecycle events | § Events and payloads `hooks.md:122-139` | event table 128 `sessionStart`, 129 `userPromptSubmitted`, 130 `preToolUse`, 131 `postToolUse`, 132 `preCompact`, 133 `subagentStart,subagentStop`, 134 `agentStop`, 135 `sessionEnd`; 137 event-reference pointer; 139 payload/alias note | yes |
| experience is Preview | title + Preview note `hooks.md:4,11` | 4 `# Configure agent hooks in Visual Studio Code (Preview)`; 11 `> The VS Code hooks experience is in Preview.` | yes |

Gate row anchors SKILL.md:129: `:58-62` (sources), `:130` (`preToolUse`), `:128` (`sessionStart`), `:4` (Preview), `:202` (executable code). Verified against snapshot: 130 = `| Inspect or make a decision about a tool call | `preToolUse` |`; 128 = `| Add context when a session starts or resumes | `sessionStart` |`; 202 = `> Hook configuration and scripts are executable code. Review them before use…` — all support the cells they are cited for. (202 falls in `> [!CAUTION]` block, not the "Security considerations" body; the quote is accurate.)

## 5. Frozen-counter judgment for S098 (ran in sandbox, read-only)

`timeout 900 python3 -B verifiers/check_hook_files.py --rev c63ccc6823e1f6a8577acbb43d19551eadbbee9a --fetch` → exit `0`, output:
```
hook files backed on committed snapshots 6 of 6; found on the live page 6 of 6; new ground 6
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev c63ccc6823e1f6a8577acbb43d19551eadbbee9a
reject opencode: SKILL.md hook config cell holds no backticked token; no entry row names the client
```
Counter sha256 matches the frozen hash named in the assignment (`f695d59e…`). Per-client judge for VS Code (in-process, same code): `{"client": "VS Code", "row": "S098", "url": "https://code.visualstudio.com/docs/agent-customization/hooks.md", "quote": "Automation shared with a repository &#124; `.github/hooks/*.json` at the repository root &#124; &#124; Hooks", "token": ".github/hooks/*.json", "norm": ".github/hooks/*.json", "in_k": true, "events": ["preToolUse", "sessionStart"], "backed": true, "why": []}` — no rejection reason.

## Findings (by severity)

None. Row, snapshot, and quote all HOLDS; every claimed line is quotable and supports the teaches cell; no counterexample found. The only "reject" line in the counter run is opencode, which is out of this seat's scope (S098 is VS Code) and matches the counter's design (opencode has no hook config file).

## Residual risk / verification gaps

- Fetch access time differs from the row's recorded fetch time (09:53:21Z vs 09:35:04Z) — expected for a re-open; content hash and size are invariant across the two fetches.
- Live fetch used one browser UA; the row's original fetch UA is not recorded, but byte-identity of body + sha256 is UA-independent evidence.
- Anchor verification is line-level text evidence on the snapshot; `teaches` wording is a faithful summary, not a quote, so minor wording differences are not defects.

## Evidence pointers

- SOURCES.md S098 row: `corpus/SOURCES.md:110` (full raw).
- Knowledge entry row + quote: `corpus/knowledge/hook-files-round59.md:25`, quote shaping `:63-64`.
- Gate prose quote: `SKILL.md:123`; gate table row: `SKILL.md:129`.
- Lesson records: `corpus/lessons/round-59.md:12,18`.
- Snapshot: `.ufo/waves/round-59/snapshots/S098.page` (15152 B; lines 4, 6, 11, 58-62, 122-139, 128, 130, 202).
- Counter: exit 0, counter sha256 `f695d59e…` (matches assignment), 6/6 backed + 6/6 found live, new ground 6.
