Result: HOLDS — SOURCES rows S032–S038 at c8407a4 are well-formed (11 cells each, valid enums, legal statuses/rechecks), every used-by path exists and cites the row, every anchor is line-level with a dated/hashed fetch revision, the tier-B choice on S037 is contract-conformant, S038 uses the required `supersedes S031 —` form, and S001–S031 are byte-untouched; the only live-page issue is post-claim drift on the Claude Code docs page, which the sha256-recorded anchor still covers.

Seat: KotobaR52a2.ReviewSourcesRows (coverage). Scope: corpus/SOURCES.md rows S032–S038 at c8407a453788df964df5a7b835dd0ce1360de882; census contract `/home/vgpnk/Projects/shokunin/CORPUS.md` § SOURCES.md; commands run on the lane checkout (git rev-parse HEAD = c8407a4…; `git status --porcelain corpus/SOURCES.md` clean). Re-fetches saved under /fast/scratch/hyaku/kotoba-r52a2/ReviewSourcesRows/; all opens by plain curl, no auth. Fetch time ~2026-10-22T17:59–18:00Z. Tools: no installs; stock curl/gawk/coreutils/python3 sufficed.

## Frozen census (CORPUS.md § Census) — lane corpus/SOURCES.md, working tree = c8407a4

```
rows:            38                      (grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|')
malformed rows:  0                       (NF!=13 count)
tier:            A=36 B=1 C=1
status:          mined=29 queued=8 rejected=1
duplicate ids:   (empty)
enum/tier-inflation: (empty)
mined used-by missing on disk: (empty)
```

Base rev c8579a4 (`git show c8579a4c…:corpus/SOURCES.md`): 31 rows, `A=30 C=1`, `mined=22 queued=8 rejected=1`. Delta = +7 rows, +6 A +1 B, +7 mined — exactly the seven new rows; the base histogram is otherwise preserved. All 38 ids contiguous S001–S038 (verified by numeric sort, no gaps).

## Maintained script

```
$ bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba
kotoba	W04	S018 duplicate url agentskills.io/specification across scopes
kotoba	W04	S019 duplicate url platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices across scopes
kotoba	W04	S021 duplicate url learn.chatgpt.com/docs/build-skills across scopes
kotoba	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md
EXIT=0
```

Identical to the plan's recorded census-before (`W04 S018, S019, S021; kotoba ok` — plans/round-52.md:79-80). No E04 on the S031/S038 duplicate URL+scope: scripts/sources-census.sh:646-648 exempts a teaches cell matching `supersedes S[0-9]{3}`, and S038's opens `supersedes S031 —`.

## Per-row cell check (each row NF=13 = 11 cells)

| row | kind | tier | status | opened | recheck | verdict |
|---|---|---|---|---|---|---|
| S032 | spec | A | mined | 2026-10-22 | on-release | holds |
| S033 | docs | A | mined | 2026-10-22 | 90d | holds (live page drifted; see below) |
| S034 | docs | A | mined | 2026-10-22 | on-release | holds |
| S035 | docs | A | mined | 2026-10-22 | 90d | holds |
| S036 | docs | A | mined | 2026-10-22 | 90d | holds |
| S037 | docs | B | mined | 2026-10-22 | 180d | holds |
| S038 | docs | A | mined | 2026-10-22 | 90d | holds |

- Enums: all kind/tier/status inside the contract lists; no community at A; no `|` inside any cell (any stray pipe would have shown as NF≠13).
- used-by: S032–S037 → `corpus/knowledge/mcp-server-instructions-round52.md, corpus/lessons/round-52.md`; S038 → `corpus/lessons/round-52.md`. All files exist; grep confirms each file actually cites the S-ids (entry :1 `source:` trio cites S032–S037 with anchors; lesson § Gate bullets :17-40 record S032–S038; entry :53 cites S037; S038's row is cited in lesson :35,62,75). `mined` status is justified by ≥1 used-by path for every row.
- Anchors: S032 `schema.md:461-463` + spec revision 2025-11-25; S033 `mcp.md:1468, :1476-1493`; S034 HTML lines 1113-1114 + version 1.104; S035 `mcp.md:197-199`; S036 `mcp-server.md:1311-1315`; S038 `cli-command-reference.md:1278, :1300, :1324`; S037 names two exact section headings (no line numbers) — `§ A Note for Client Implementers`, `§ Currently Supported Host Applications`. Every anchor carries a fetch timestamp + byte count + sha256; contract asks "exact section/heading/page/line plus revision", and the hashed fetched bytes act as revision where the source carries no version field. Both S037 headings exist verbatim in the fetched page (49,781 B, sha256 `96794ff9…` matching the recorded value).
- S037 tier B holds: scope is explicitly "explanatory, not normative spec text"; B = strong secondary is a correct, conservative tier for a maintainers' blog under that scope (lesson :32 records the rationale "tier B: maintainers' blog, explanatory"). Understating trust is not a contract defect.
- S038 supersede form holds: `supersedes S031 —` opens the teaches cell, names the real field `disable-model-invocation`, `ignoredSkillsLocations`, `copilot skill disable`, and records `disabledSkills` 0 occurrences — all confirmed live: fetched copilot-cli.md is 461,944 B sha256 `c61997ef…`, byte-identical to both the S031 and S038 recorded fetches; `grep -c disabledSkills` = 0, `disable-model-invocation` = 2, `ignoredSkillsLocations` = 1, `copilot skill disable` at :1324; lines :1278/:1300/:1324 contain exactly the cited material.
- Append-only: `git diff c8579a4… c8407a4… -- corpus/SOURCES.md` = 7 insertions, 0 deletions; S031 and all earlier rows byte-untouched, and no `status`/`recheck`/`used-by` in-place change either, so no old→new lesson logging was owed (lesson :60-62 records this).

## Live re-open verification (fetches ~17:59–18:00Z)

Byte/sha identical to the recorded anchors: S032 (130,800 B `5ab7cfcd…`), S035 (26,995 B `c78df8c7…`), S036 (43,656 B `4aefc4dc…`), S037 (49,781 B `96794ff9…`), S038 (461,944 B `c61997ef…`). Content at cited lines verified verbatim: `schema.md:461` `instructions?: string` in `InitializeResult` and :463 "Instructions describing how to use the server and its features" (teaches text accurate); codex `mcp.md:197-199` bullet + 512-char paragraph; gemini `mcp-server.md:1311-1315` § Instructions "appended to the system instructions"; vscode HTML :1113 `<h3>Support for server instructions</h3>`, claim sentence present (the `.md` variant is indeed a 404 page — re-fetched HTTP 404, 19,510 B, exactly the lesson's recorded 19,510 B).

Entry's negative sweeps re-verified live: opencode `mcp-servers.md` 13,941 B (recorded bytes identical) `grep -ci instructions` = 0; Copilot CLI `add-mcp-servers.md` 14,240 B (recorded bytes identical) one `instructions` hit at line 22, about installation instructions only; `concepts/context/mcp.md` → HTTP 404 502 B (recorded 502 B). The lesson's honest non-claim ("source code was not read") is correctly bounded.

Gate records conform to rule 1: each new row in `corpus/lessons/round-52.md` § Gate carries URL, ISO access timestamp, byte count, full sha256, located ≤25-word quote (S033's quote is 22 words; S037's 21; all ≤25). Rejections carry the sweep command and flip conditions; no S-id was spent on them, matching "a lead is not evidence and never a row".

## Findings

1. **(Informational / low) S033 and S034 pages drifted after the recorded fetches.** Live `code.claude.com/docs/en/mcp.md` is now 128,298 B (recorded 127,022 B, sha `9a42e98f…` no longer reproducible); the cited section was renamed `## Scale with MCP tool search` and moved to :1486/:1494 — yet the quoted claim and the 4,096-char limit survive verbatim (:1488, :1504-1507). Live VS Code v1_104 is 179,457 B (recorded 179,440 B) with the quoted sentence now at :1115 (recorded anchor "HTML lines 1113-1114", lesson quote "line 1114"). The anchors are honestly pinned to the fetched bytes by sha256 — this is documented-drift behavior, not an authoring error; the row's `revision` component (bytes+sha) remains exact, though a reader re-opening today cannot byte-reproduce S033's or S034's anchor. Not a contract violation; noted for the closure's freshness sweep.
2. **(Out of scope, noted) The milestone's "S024 superseding row" is not in this diff and nowhere in S032–S038** — the lesson (:75) honestly logs it as carried-not-worked (seat-grant starvation + route outage, M37), consistent with the attempt-1 failure mode described in the round brief. The registry itself does not claim it. No defect in the rows judged.

## Corroboration

`python3 -B verifiers/check_mcp_instructions.py --rev c8407a453788df964df5a7b835dd0ce1360de882` → `MCP specification BACKED / Claude Code BACKED / VS Code BACKED / Codex BACKED / Gemini CLI BACKED / opencode 0 / Copilot CLI 0`, `mcp instructions backed 5 of 7 clients`, exit 0. The row set feeds the C2 claim exactly as printed: five tier-A mined rows for five backed clients, exclusions consistent with the recorded sweeps. S037 correctly does not count as a client row (the statement requires tier-A); S038 is scoped to skill levers, not instructions, and is correctly not counted.
