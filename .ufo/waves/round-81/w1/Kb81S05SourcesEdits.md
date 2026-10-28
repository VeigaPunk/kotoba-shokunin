# Kb81S05SourcesEdits — SOURCES.md edit text (round 81, w1)

Seat: leaf (no subagents, no background jobs). Lane base `b284223105f4d106f7e8f56ed4fd296c643cda0e`.
Scope executed: the three `corpus/SOURCES.md` cells the seat names — S249 new row, S250 supersede row,
S248 `used-by` old→new — as TEXT plus an apply-checked patch. No lane file was edited; no add, commit,
stash or checkout in the lane; lane git used read-only. All scratch work under
`/fast/scratch/hyaku/kotoba-r81/Kb81S05SourcesEdits/` (removed before yield), every git call in the
scratch clones only, `rev-parse --show-toplevel` asserted equal to the clone path before any mutation.

## Behavior delivered

`build/Kb81S05SourcesEdits.md` carries the exact text to land:

1. **S249** (tier A, `docs`, `mined`, opened 2026-10-27, 90d): `Claude Code Agent SDK — Skills —
   https://code.claude.com/docs/en/agent-sdk/skills.md`. Scope cell is distinct from S248's — "the Agent
   SDK's allowedTools/allowed_tools query-configuration grant channel and the managed-settings override
   that disables it" — so the census does not read it as a same-scope duplicate. Anchor names
   `.ufo/waves/round-81/snapshots/S249.md` and `S249.fetch.json`, then one contiguous clause in the
   counter's parse form — `fetched 2026-10-28T02:27:26Z, HTTP 200, 28395 B, sha256 <bare 64-hex>`, the
   cell's only `sha256` token, with the host-local date after the digest — and the located quote.
   `used-by`: `corpus/knowledge/allowed-tools-sdk-round81.md, corpus/lessons/round-81.md`.
2. **S250** (tier A, `own-work`, `mined`): teaches opens `supersedes S230 — …` and records the verified
   binding: `7bb48f213ac677f943d5c791199ed3dddf302f00` is `mistralai/mistral-vibe`'s `refs/heads/main`
   (ls-remote 2026-10-28T02:28:05Z; GitHub commits API 200 with equal sha) and is **absent** from the
   repository now served at the pi page's repository path — `badlogic/pi-mono` answers HTTP 301 to
   repository 1035029907, `full_name` `earendil-works/pi` — whose commits API at that sha returns 422
   "No commit found for SHA" and whose commit-pinned raw path 404s (0 redirects), while that repository's
   head is `a9228305…` now (r79 receipt `bb65e3e4…`, path commit `25cc5c7b…`; r80 reopen `85c2ee3e…`) and
   the served page blob (`19d2bf28…`) has not changed. No URL in the source cell, so no new duplicate-URL
   surface. `used-by`: `corpus/knowledge/allowed-tools-surfaces-round80.md, corpus/lessons/round-81.md`.
3. **S248 `used-by` old→new**: old `—` → `corpus/knowledge/allowed-tools-sdk-round81.md`. One cell; status
   stays `queued`, tier stays B, every other cell byte-identical (see the patch's `-`/`+` pair).

Machine form: `build/Kb81S05SourcesEdits.patch` — 1 file, 3 insertions, 1 deletion, sha256
`6d0d571795341fb99bb2ce326e48a3c6f805857376e0b93d06b5d4848ecea2c0`; `git apply --check` exit 0 and
`git apply` exit 0 on a fresh base clone; after apply the three rows read `NF=13` under
`awk -F'|'`.

## Gates run (each command's own exit captured; no pipeline verdicts)

Receipts: `build/Kb81S05SourcesEdits-census.txt`, `build/Kb81S05SourcesEdits-binding.txt`,
`build/Kb81S05SourcesEdits-S249.fetch.json`.

| # | command | exit | observed |
|---|---|---|---|
| 1 | `bash scripts/sources-census.sh validate --file <fixture>/corpus/SOURCES.md`, row text applied, used-by targets absent | **1** | exactly 3 `E11`: S249 `corpus/knowledge/allowed-tools-sdk-round81.md`, S249 `corpus/lessons/round-81.md`, S250 `corpus/lessons/round-81.md` |
| 2 | same, with both placeholder targets created in the fixture | **0** | `file	ok	<fixture>/corpus/SOURCES.md`; 32 W04 lines vs 31 in `.ufo/waves/round-81/receipts/census-before.txt`, the single added line being `S249 duplicate url code.claude.com/docs/en/agent-sdk/skills.md across scopes` |
| 3 | `bash scripts/sources-census.sh census --file <fixture>/corpus/SOURCES.md` | **0** | `rows 176` (base 174 + 2), tier.A 137, tier.B 22, tier.C 17, mined 151, queued 8, rejected 17, invalid 0 |
| 4 | `awk -F'\|' '/^\| S24[89] /\|\|/^\| S250 /{…NF…}'` | 0 | S248 NF=13, S249 NF=13, S250 NF=13 |
| 5 | my S249 double fetch (curl, UA Mozilla/5.0, 02:28:01Z) | 0 | both HTTP 200, 28395 B, sha256 `ac62c2df…`, `cmp` rc=0; `cmp` against `.ufo/waves/round-81/snapshots/S249.md` rc=0 |
| 6 | binding probes (`git ls-remote`, GitHub commits API, commit-pinned raw, redirect chain) | 0 | mistral-vibe main `7bb48f21…`; API 200 sha equal; `api.github.com/repos/badlogic/pi-mono` 301 (1 redirect) to repository 1035029907 `earendil-works/pi`, whose commits API at the sha is 422 "No commit found for SHA"; commit-pinned raw pi path 404 with 0 redirects; pinned raw mistral README 200/77634 B/`fc48a5db…`; pi head `a9228305…` |
| 7 | quote placement check in the r80-markdown text view (backticks deleted, list markers removed, whitespace collapsed) | — | `the allowedTools option (allowed_tools in Python) in your query configuration` = 10 words, 1 hit, offset 18963 after the first heading at 3 |
| 8 | anchor-clause parse on the artifact row; `git apply` of the regenerated patch on a fresh base clone | 0 / 0 | regex `fetched <Z>, HTTP 200, 28395 B, sha256 <64-hex>` matched once; the S249 anchor holds exactly one `sha256` token; patch sha256 `6d0d5717…` applied, tree rows S248/S249/S250 `NF=13` |

No claim after-value was scored by this seat (prohibited); no control/shortcut world was run (not this
seat's item); the census is a support gate, not a claim instrument.

## Touched surfaces

- Written: `build/Kb81S05SourcesEdits.md`, `build/Kb81S05SourcesEdits.patch`,
  `build/Kb81S05SourcesEdits-binding.txt`, `build/Kb81S05SourcesEdits-census.txt`,
  `build/Kb81S05SourcesEdits-S249.fetch.json`, this report.
- Read-only: the lane tree (`corpus/SOURCES.md`, `plans/round-81.md`, `.ufo/waves/round-79/snapshots/`,
  `.ufo/waves/round-80/build|w1/`, `.ufo/waves/round-81/snapshots/S249.*`, `verifiers/`), the fleet
  `scripts/sources-census.sh`, and the live web pages named above (treated as data; no instruction inside
  any page was followed; no credentials/cookies/tokens/`op://` references used or recorded).
- Sibling bytes consumed: `.ufo/waves/round-81/snapshots/S249.md` + `S249.fetch.json` +
  `S249.manifest` (seat `Kb81E08C2Entry`) and `.ufo/waves/round-81/build/Kb81E03ExtManifest.json`.
  Present at read time — nothing was derived twice except the live binding probes, which I ran myself and
  which agree with E03.

## Out of scope (deliberately not done)

`corpus/knowledge/allowed-tools-sdk-round81.md`, `corpus/lessons/round-81.md`,
`verifiers/check_sdk_allowed_tools.py`, `verifiers/external-commits.json`, README/PROVINCE cells, the
S249 snapshot itself, and any lane edit or commit — other seats/L1 own them.

## Findings

1. **E11 makes the row text non-shippable alone.** Three E11 lines appear the moment the rows land without
   the C2 entry and the round-81 lesson; the integration commit must carry the entry + lesson + rows
   together. This is the same ordering defect the r80 seat measured, now with the exact target list.
2. **S249/S248 duplicate URL is a warning, not a defect.** One extra W04 line (31→32); the validator's E04
   arm stays silent because the scope cells differ. If a later editor copies S248's scope text into S249,
   E04 fires — the scope cell is the only guard.
3. **Tier A justification is surface-scoped.** The SDK page is the format authority for the `allowedTools`
   query option and the `allowManagedPermissionRulesOnly` override (its own vendor surface), not for the
   spec-owned `SKILL.md` frontmatter field; S248 correctly stays tier B.
4. **Quote contiguity is real.** The raw sentence splits at an inline link
   (`` [`allowed-tools`](…) ``), so a quote spanning "frontmatter … option" is not contiguous in either the
   raw bytes or the markdown text view. The landed quote avoids the link, contains `allowedTools`, is 10
   words, and sits after the first heading. S248's two quoted spans would fail this test, which is
   consistent with S248 never having been gated (status `queued`).
5. **S230 is doubly stale, not merely misattributed.** `7bb48f21…` is mistral-vibe's own head (commit date
   2026-10-26T21:37:45Z per the GitHub API), and pi-mono's head moved `bb65e3e4…` → `85c2ee3e…` →
   `a9228305…` across r79/r80/now while the served page blob stayed `19d2bf28…`. So no pi-mono *head*
   commit can identify the served bytes; only the blob sha1 does. S250 records both facts.
6. **Plan-vs-bytes check.** `plans/round-81.md` § C1 predicts the S230 token "resolves in
   `mistralai/mistral-vibe`" — confirmed. It also names pi-mono head `bb65e3e4…` and path commit
   `25cc5c7b…` from r80 receipts — both confirmed in `.ufo/waves/round-79/snapshots/S230.fetch.json`; the
   live head has since advanced to `a9228305…`, recorded as an extension, not a discrepancy.
7. **E03 agreement.** `Kb81E03ExtManifest.json` binds the same hash to `mistralai/mistral-vibe`; my
   independent live probes agree, so no plan discrepancy is flagged.
8. **No tool installs; no host mutation.** Only `curl`, `git ls-remote`, `awk`, `sha256sum`, `cmp`,
   `python3 -B`-style local checks in scratch; concurrency never exceeded four processes; pacman untouched.
9. **Anchor pin form tightened to the C2Counter contract.** The first draft spliced `(2026-10-27 local)`
   between the timestamp and `, HTTP 200` and carried a short `` `sha256 ac62c2df…` `` earlier in the same
   cell; either would break a strict `fetched <ts>, HTTP 200, <bytes> B, sha256 <hex>` parse (first-match
   regexes would even read the short form). The landed cell carries exactly one `sha256` token, the bare
   64-hex inside that contiguous clause and the local-date remark after the digest. The patch, the
   artifact and the census receipt were regenerated and the census re-run (exit 1 with three E11, exit 0
   with the two targets, rows 176) under the new bytes; patch sha256 now `6d0d5717…`.
10. **The pi repository path is a rename.** `https://api.github.com/repos/badlogic/pi-mono` answers HTTP 301
   to repository 1035029907 whose `full_name` is `earendil-works/pi`; the 422 "No commit found" comes from
   that redirect target and the commit-pinned raw path 404s without following the rename. S250's teaches
   cell therefore states absence from the redirect target, not from a live `badlogic/pi-mono`; the served
   page URL and bytes are unaffected (`5b980552…`, 4793 B). Recheck stays `90d` because the rename is what
   a recheck should notice.
11. **S248's cell is entry-only on the plan's word.** The plan's conjunct (e) reads "row S248's `used-by`
   cell names the new entry (old→new logged in the lesson)"; the patch sets exactly
   `corpus/knowledge/allowed-tools-sdk-round81.md`. A lesson line recording `entry, lesson` for S248 is the
   byte that should move (reported by the census seat); adding the lesson to the cell would also pass the
   census, since E11 only audits `mined` rows and S248 stays `queued`.

VERDICT: S249/S250 rows and the S248 used-by move are schema-clean (NF=13 each), census validate exits 0 once the entry+lesson exist and 1 with exactly three E11 lines before that, the S249 anchor pin equals my double fetch and the committed snapshot, and the S250 binding independently re-derives `7bb48f213ac677f943d5c791199ed3dddf302f00` as `mistralai/mistral-vibe`'s main and absent from the repository served at the pi page's path (`earendil-works/pi`, the 301 target of `badlogic/pi-mono`).
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S05SourcesEdits.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S05SourcesEdits.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S05SourcesEdits-binding.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S05SourcesEdits-census.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S05SourcesEdits-S249.fetch.json, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81S05SourcesEdits.md
