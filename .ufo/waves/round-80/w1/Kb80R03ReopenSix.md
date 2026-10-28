# Kb80R03ReopenSix — w1 seat report (C2 live re-open of S226–S231)

Round 80, wave w1, attempt 1. Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`. Base `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`. Leaf scout seat: no subagents, no background jobs, no lane commit, no lane file written outside `.ufo/waves/round-80/`.

## Assignment

Re-open the six C2 sources live (S226–S231): fetch twice, byte-compare against the r79 committed snapshots, write fresh fetch records under `.ufo/waves/round-80/build/`, confirm the r79 located quotes in the live bytes (offset), resolve the raw-`main` served commits for S230/S231, and record the Akamai byte-variance class for S229 per the r79 sentinel note.

## Behaviour (commands and their own exit statuses)

Scratch dir `/fast/scratch/hyaku/kotoba-r80/Kb80R03ReopenSix` (`TMPDIR` inside it; removed after receipts were copied — see Cleanup). All curls: `curl -sSL -A 'Mozilla/5.0' --max-time 90 -o <body> -D <hdr> -w '<meta>'`, status captured via `-w exitcode` + `echo exit=$?` appended to the meta file.

| # | command | observed | rc |
|---|---|---|---|
| 1 | batch-1 fetch of all six URLs (parallel, 6 curls) | all HTTP 200; S226 7608 B, S227 117962 B, S228→HTML 341384 B, S229 157339 B, S230 4793 B, S231 77634 B | 0 |
| 2 | batch-2 fetch of all six + S228 `.md` route | all HTTP 200, sizes identical to batch 1 | 0 |
| 3 | `cmp S<id>.body S<id>-b.body` for S226/S227/S229/S230/S231 | no output each — fetch1 == fetch2 | 0 |
| 4 | `cmp S<id>.body <r79 snapshot>` | S226/S227/S230/S231 identical (rc=0); S229 differs (rc=1) | 0 / 1 |
| 5 | `cmp S228-md.body <snapshot S228-factory.md>` (both .md fetches) | identical both times | 0 |
| 6 | `git ls-remote https://github.com/badlogic/pi-mono refs/heads/main` | `85c2ee3e761e4fc4f901ff0ed584fb2465aa552e` (23:14Z) | 0 |
| 7 | `git ls-remote https://github.com/mistralai/mistral-vibe refs/heads/main` | `7bb48f213ac677f943d5c791199ed3dddf302f00` (23:14Z) | 0 |
| 8 | commit-pinned raw fetches (S230 at `85c2ee3e…`, S231 at `7bb48f2…`) | both HTTP 200, same sizes/same sha256 as the `main` fetches; `cmp` rc=0 | 0 |
| 9 | `diff <snapshot S229-msaf.html> S229.body` | rc=1, exactly 4 changed line-pairs (8 `<`/`>` lines) — see S229 below | 1 |
| 10 | python quote scan (`bytes.count` / `bytes.find`) on the six fresh bodies | counts 1 each, offsets: S226 1417, S227 45666, S228(.md) 11157, S229 28465, S230 3578, S231 39455 | 0 |
| 11 | `grep -c -F 'does not add tools' S228.body` (HTML route) | 2 (matches the r79 recheck expectation for the canonical URL) | 0 |
| 12 | `grep -c -F 'does not add tools' <snapshot S228-factory.md>` and fresh `.md` | 1 each — snapshot and fresh `.md` agree | 0 |
| 13 | `grep -o 'git_commit_id[^<]*' S229.body` / `<snapshot>` | both `d34f426053dba6703197776e7aad4d30fd4d06f5`; ms.date both `2026-10-23T00:00:00Z` | 0 |
| 14 | S230/S231 body git blob sha1 (`printf 'blob <len>\0' \| cat - body \| sha1sum`) | S230 `19d2bf28910ce49caaaf4dde86d1e96330ca7b31` (= r79 blob); S231 `2386969762b81efe7b14ac231a9d44e92cfcd1ae` | 0 |
| 15 | JSON validation of the six written fetch records | all parse; `fetched_utc` = 2026-10-27T23:13:48Z/23:13:49Z/23:14:06Z | 0 |

## Findings per source

**S226 — agentskills.io/specification.md.** Both fetches and both snapshot comparisons byte-identical (sha256 `9a67de89…`, 7608 B, cmp rc=0). Page unchanged since the r79 pin. Located quote `Space-separated string of pre-approved tools` count=1 at offset 1417 in the fresh bytes. No revision stated by the page (last-modified = request instant; no ETag); r79 upstream substitution (agentskills/agentskills@`217be548…`) not re-derived — recorded as standing r79 evidence.

**S227 — code.claude.com/docs/en/skills.md.** Both fetches and snapshot comparisons byte-identical (sha256 `31623035…`, 117962 B, cmp rc=0). Page unchanged. Located quote `without asking permission during the turn` count=1 at offset 45666.

**S228 — Factory (canonical docs.factory.com/harness/skills).** Redirect chain re-recorded live from the r79 assigned URL: `https://docs.factory.ai/cli/configuration/skills` → 308 `https://docs.factory.com/cli/configuration/skills` → 308 `/harness/skills` (HTML route: 341384 B, sha256 `847e48a3…`). The `.md` route of the assigned URL redirects the same two hops to `docs.factory.com/harness/skills.md` (200, 17567 B, sha256 `81409d89…`); both `.md` fetches byte-identical to the committed snapshot `S228-factory.md` (cmp rc=0 both). The `.md` bytes have not changed since the r79 pin. The ETag rotated (`e322e6b7…` → `b217318d…`) while the bytes stayed identical — recorded as an origin fingerprint change, not content drift. Located quote `does not add tools`: count=1 at offset 11157 in the fresh `.md` bytes (identical to the snapshot count); the HTML route carries it 2×, which is exactly what the r79 recheck line measured against the canonical URL — no discrepancy.

**S229 — learn.microsoft.com/en-us/agent-framework/agents/skills.** The two fetches agreed with each other (both 157339 B, sha256 `20fd76d8…`, cmp rc=0) but differ from the committed snapshot `34016233…` (also 157339 B): `diff` rc=1 with exactly 4 changed line-pairs. Akamai byte-variance class, per the r79 sentinel note (Kb79SN01Sentinel F4/R7): **origin-served volatile instrumentation only, not content** — (i) two Akamai Bot Manager beacon lines whose URL token rotated `41ddb17` → `41ddb15` (the `<script src="…/akam/13/41ddb15" defer>` and the `<noscript>` pixel; the per-client seed `bazadebezolkohpepadr="69065007"` is byte-identical in snapshot and fresh bytes), and (ii) two Microsoft Learn static-asset version strings `0.4.03574.8308-9505b1c8` → `0.4.03585.8328-71cc54cb` (site.css link and index-docs.js src). Content-bearing bytes unchanged: page-stated revision identical to the snapshot (`git_commit_id d34f426053dba6703197776e7aad4d30fd4d06f5`, `ms.date 2026-10-23T00:00:00Z`). Classification consequence (as the sentinel required): this surface's recheck must remain "committed snapshot matches the MANIFEST pin", never fresh-fetch equality; the row anchor's origin-not-byte-stable note stands and this round's observed pair (`34016233…` vs `20fd76d8…`, 2026-10-27) is one more instance of the same class. Located quote `Space-delimited list of pre-approved tools` count=1 at offset 28465 in the fresh bytes.

**S230 — raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/docs/skills.md.** Both fetches and snapshot comparisons byte-identical (sha256 `5b980552…`, 4793 B, cmp rc=0). Served commit resolved: `main` = `85c2ee3e761e4fc4f901ff0ed584fb2465aa552e` (23:14Z) — the branch moved since r79 (`bb65e3e4…`), but the commit-pinned raw URL at `85c2ee3e…` served the same 4793 B / same sha256 (cmp rc=0), so the served blob is unchanged across those two commits. Body git blob sha1 `19d2bf28910ce49caaaf4dde86d1e96330ca7b31` matches the r79-recorded blob. Located quote `Experimental pre-approved tool list` count=1 at offset 3578.

**S231 — raw.githubusercontent.com/mistralai/mistral-vibe/main/README.md.** Both fetches and snapshot comparisons byte-identical (sha256 `fc48a5db…`, 77634 B, cmp rc=0). Served commit resolved: `main` = `7bb48f213ac677f943d5c791199ed3dddf302f00` — **the same commit r79 recorded**, so `main` has not moved; the commit-pinned raw URL serves the same bytes (cmp rc=0). Located quote `allowed-tools:` count=1 at offset 39455.

## Deliverable records (sha256 of the written files)

| record | content sha256 |
|---|---|
| `build/Kb80R03ReopenSix-S226.fetch.json` | `9dd21a5439490413a2c52c1c9e7f1acc5611dda2ab3e95b6b060f255f8fe6e8f` |
| `build/Kb80R03ReopenSix-S227.fetch.json` | `c48dbe56af0a8afe443dad748641859d587c6d4b56f8876232b3c050e100f0ca` |
| `build/Kb80R03ReopenSix-S228.fetch.json` | `a24c6065f0c0bbceb5c1626dff4e765558b0f00e49a633f7544fb207e1c87329` |
| `build/Kb80R03ReopenSix-S229.fetch.json` | `8dc3554aadc27a9fe3169c0bdadaa0dba7433c5801c4a56c2ca5e53964b5f664` |
| `build/Kb80R03ReopenSix-S230.fetch.json` | `daa600ed623e85f996680758b019745f95f76fb14cf63dedc3fd80db3a50ddda` |
| `build/Kb80R03ReopenSix-S231.fetch.json` | `fc4a3f50d4556e12a7f6b863821319b78bab45d171c5594b309bd31b67b2fc94` |

Each record carries the r79 schema (`id`, `url`, `final_url`, `http`, `bytes`, `sha256`, `fetched_utc`, `ua`, `note`) with `fetched_utc` = 2026-10-27 (batch-1 fetch instant) and both fetch instants named in the note. These six records ground the C2 rows' `opened this round` = 2026-10-27 and the `recheck:` cells.

## Untrusted-content handling

All fetched pages were treated as data: the S227 page's imperative text and the S226 reader-directed lines were not followed; no `llms.txt` was fetched; no commands from page content were run; no credentials, cookies or tokens appear in any output (the only `token=` string in the S229 diff is Akamai's bot-detection beacon parameter, named in the variance classification, and it is page instrumentation, not a secret).

## Coordination

Kb80E10Battery addressed a C1 patch-stack inventory request to this seat id; I replied that this seat produces only the six C2 fetch records and named the owning seats (E01–E06).

## Cleanup

Scratch `/fast/scratch/hyaku/kotoba-r80/Kb80R03ReopenSix` removed (`rm -rf`, then `test ! -e` rc=0) after the six records were written and validated in the lane build dir. No tool installs or upgrades were needed. `disk-guard.sh` was not consulted (six sub-200 KB fetches, not a heavy pass).

## Out of scope (deliberately not done)

- Editing `corpus/SOURCES.md`, the C2 entry, rows, or any counter/fixture — L1 integration.
- Re-deriving the S226 upstream mdx substitution (r79 receipt stands).
- Snapshotting any bytes into `.ufo/waves/round-80/snapshots/` — the C2 claim pins the r79 snapshots, and this seat's evidence is the fetch records plus the byte-comparisons recorded here.

VERDICT: Six C2 sources re-opened live 2026-10-27 — five byte-identical to the r79 snapshots (S226/S227/S230/S231 exactly; S228 .md exactly with ETag rotated), S229 differs only in Akamai-bot-manager + MS-asset-version instrumentation with content revision unchanged; all six located quotes confirmed in fresh bytes with offsets; S230 main moved to 85c2ee3e with unchanged blob, S231 main unmoved at 7bb48f2.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80R03ReopenSix-S226.fetch.json /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80R03ReopenSix-S227.fetch.json /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80R03ReopenSix-S228.fetch.json /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80R03ReopenSix-S229.fetch.json /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80R03ReopenSix-S230.fetch.json /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80R03ReopenSix-S231.fetch.json /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/w1/Kb80R03ReopenSix.md
