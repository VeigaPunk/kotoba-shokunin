# Kb81S05SourcesEdits — SOURCES.md edit text (round 81, w1)

Seat: leaf, no subagents. Scope: `corpus/SOURCES.md` text only. Base `b284223105f4d106f7e8f56ed4fd296c643cda0e`.
No lane file was edited, no add/commit/stash/checkout in the lane (lane git read-only). Ready-to-apply form:
`build/Kb81S05SourcesEdits.patch` (`git apply --check` and `git apply` exit 0 on a fresh base clone;
`corpus/SOURCES.md` only, 1 file changed, 3 insertions(+), 1 deletion(-); the report carries its sha256).

## (1) S249 — new row, tier A (append after S248 in `## Registry`)

| S249 | Claude Code Agent SDK — Skills — https://code.claude.com/docs/en/agent-sdk/skills.md | docs | A | The Agent SDK's allowedTools/allowed_tools query-configuration grant channel and the managed-settings override that disables it, as the SDK vendor's own statement of that option | § Pre-approve tools for skills, blockquote at line 348 (grant note line 389); snapshot `.ufo/waves/round-81/snapshots/S249.md` and fetch record `.ufo/waves/round-81/snapshots/S249.fetch.json`; fetched 2026-10-28T02:27:26Z, HTTP 200, 28395 B, sha256 ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2 (host-local date 2026-10-27, TZ -03), two fetches byte-identical (cmp rc=0, 0 redirects); located quote "the allowedTools option (allowed_tools in Python) in your query configuration" | In SDK sessions the grant channel is the skill's allowed-tools frontmatter or the query option allowedTools (allowed_tools in Python), and when managed settings set allowManagedPermissionRulesOnly Claude Code ignores both | mined | 2026-10-27 | 90d | corpus/knowledge/allowed-tools-sdk-round81.md, corpus/lessons/round-81.md |

## (2) S250 — supersede row (append after S249)

| S250 | kotoba own work — git ls-remote, GitHub commit API and commit-pinned raw probes, mistralai/mistral-vibe versus badlogic/pi-mono, run 2026-10-27 exit 0 | own-work | A | Which repository commit 7bb48f213ac677f943d5c791199ed3dddf302f00 belongs to, and what pi-mono's head and served page blob are | `git ls-remote https://github.com/mistralai/mistral-vibe refs/heads/main` → `7bb48f213ac677f943d5c791199ed3dddf302f00` rc 0 at 2026-10-28T02:28:05Z; commits API for mistral-vibe at that sha → HTTP 200 with sha equal; `https://api.github.com/repos/badlogic/pi-mono` → HTTP 301 to repository 1035029907 `earendil-works/pi` (1 redirect), and that repository's commits API at the sha → HTTP 422 "No commit found for SHA"; commit-pinned raw at the pi page path → HTTP 404 with 0 redirects (raw.githubusercontent does not follow the rename); commit-pinned raw README at the sha in mistral-vibe → HTTP 200, 77634 B, sha256 `fc48a5db…`; `git ls-remote https://github.com/badlogic/pi-mono refs/heads/main` → `a9228305…` rc 0 (r79 receipt head `bb65e3e4…`, r80 reopen `85c2ee3e…`, path commit `25cc5c7b…`); receipts `.ufo/waves/round-81/build/Kb81S05SourcesEdits-binding.txt` | supersedes S230 — S230's anchor names 7bb48f213ac677f943d5c791199ed3dddf302f00 as pi-mono's main, but that commit is mistralai/mistral-vibe's refs/heads/main (ls-remote 2026-10-28T02:28:05Z) and is absent from the repository now served at the pi page's repository path, `earendil-works/pi` (the GitHub 301 target of `badlogic/pi-mono`; commits API 422 there), while that repository's head moved bb65e3e4 at r79 and 85c2ee3e at the r80 reopen and a9228305 now with the served page blob (sha1 19d2bf28…) unchanged, so no commit of that repository identifies the served bytes | mined | 2026-10-27 | 90d | corpus/knowledge/allowed-tools-surfaces-round80.md, corpus/lessons/round-81.md |

## (3) S248 `used-by` old -> new (one cell, nothing else on the row changes; status stays `queued`)

- old cell (base 174-row file, `corpus/SOURCES.md:189`): `—`
- new cell: `corpus/knowledge/allowed-tools-sdk-round81.md` — the plan's conjunct (e) is "row S248's `used-by` cell names the new entry
  (old→new logged in the lesson)", i.e. the entry alone; a lesson line claiming `entry, lesson` must move,
  not this cell.

Exact S248 line after the edit (for the diff):

| S248 | Claude Code — Agent SDK: Agent Skills — https://code.claude.com/docs/en/agent-sdk/skills.md | docs | B | What the Claude Agent SDK page states about the SKILL.md allowed-tools frontmatter field in SDK sessions | § Pre-approve tools for skills (line 348) and the grant note (line 389); fetched 2026-10-27, HTTP 200, 28395 B, sha256 ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2; located quotes "In SDK sessions, you can pre-approve tools for a project or personal skill with the skill's allowed-tools frontmatter or with the allowedTools option" and "The list pre-approves the named tools rather than restricting the others." | The page states that in SDK sessions the frontmatter field pre-approves the listed tools, as does the allowedTools query option, that managed settings can override both, and that the list pre-approves rather than restricts — a documented surface outside the frozen six, held queued | queued | 2026-10-27 | 90d | corpus/knowledge/allowed-tools-sdk-round81.md |

## Integration notes (measured, not assumed)

1. **Ordering is load-bearing (E11).** With the row text applied but `corpus/knowledge/allowed-tools-sdk-round81.md`
   and `corpus/lessons/round-81.md` absent, `scripts/sources-census.sh validate --file <fixture>/corpus/SOURCES.md`
   exits **1** with exactly three E11 lines (S249 both targets, S250 the lesson). With both targets present
   (placeholders in the fixture), the same command exits **0** and prints `file	ok	…`. So the C2 entry and the
   round-81 lesson must land in the same integration commit as these rows. The C2 counter also needs the
   round-81 lesson to carry one line naming S248, `corpus/knowledge/allowed-tools-sdk-round81.md` and an arrow
   (C2Counter seat, relayed to S01Lesson).
2. **Counts.** Fixture with all three edits: `rows 176` (base 174 + 2), tier.A 137, tier.B 22, tier.C 17,
   status.mined 151, status.queued 8, status.rejected 17; `census` mode exit 0.
3. **W04 warning, expected.** W04 lines go 31 (base receipt `.ufo/waves/round-81/receipts/census-before.txt`,
   which has 32 output lines = 31 W04 + `ok`; the lesson's "32 W04" reading is off by the `ok` line) -> 32;
   the added line is `S249 duplicate url code.claude.com/docs/en/agent-sdk/skills.md across scopes`, the
   census's warning form for a second scope on a held URL (S248 stays `queued` for the frontmatter-scope
   reading). Warnings never change the exit status; no E-code was added.
4. **Schema.** `awk -F'|' 'NF==13'` holds for all three touched rows (11 cells + leading/trailing pipes); no `|`
   inside any cell. Field 2 carries the padded id, field 12 the `used-by` cell.
5. **Tier A justification for S249 (not S248).** The Agent SDK page is the vendor's own statement of its own
   query-configuration option (`allowedTools` / `allowed_tools`) and of the managed-settings override
   (`allowManagedPermissionRulesOnly`, "Claude Code ignores both") — the format authority for *that* surface.
   S248 stays tier B because its subject is the spec-owned `SKILL.md` frontmatter field, for which the open
   spec (S001/S018) is the format authority.
6. **Quote choice for conjunct (d).** The anchor quote is `the allowedTools option (allowed_tools in Python) in
   your query configuration` — 10 words (cap 25), contains `allowedTools`, and is contiguous in the markdown
   text view (backticks deleted, unordered-list markers removed, whitespace collapsed) at the line-348
   blockquote, after the first heading (Q70). The full sentence in raw bytes splits at the inline link
   `` [`allowed-tools`](…/skills#pre-approve-tools-for-a-skill) ``, so a quote spanning it would not be
   contiguous; the chosen span avoids the link. S248's two quoted spans would fail the same test, consistent
   with S248 never having been gated.
7. **Anchor pin form (strict).** The S249 anchor carries exactly one `sha256` token and one contiguous clause
   `fetched 2026-10-28T02:27:26Z, HTTP 200, 28395 B, sha256 <bare 64-hex>` — no parenthetical or short hash
   spliced between the timestamp and the status — because the C2 counter parses that clause and takes the pin
   from it (C2Counter seat: in-file `SNAPSHOT_PIN` equals the same digest). The host-local date sits after the
   digest.
8. **Snapshot.** `.ufo/waves/round-81/snapshots/S249.md` exists with sha256
   `ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2` (28395 B, 519 lines); my own double
   fetch (`.ufo/waves/round-81/build/Kb81S05SourcesEdits-S249.fetch.json`, 2026-10-28T02:28:01Z) is
   `cmp`-identical to it, and the snapshot's own record `S249.fetch.json` carries the same digest at
   2026-10-28T02:27:26Z, the instant the row cites.
9. **S250 binding agrees with E03.** `.ufo/waves/round-81/build/Kb81E03ExtManifest.json` records
   `{"hash":"7bb48f213ac677f943d5c791199ed3dddf302f00","repo":"mistralai/mistral-vibe"}`; my independent probes
   agree (see `build/Kb81S05SourcesEdits-binding.txt`), so no plan discrepancy is recorded.
10. **What changed versus the r80 grammar repair.** The r80 E05 design classified a bare hex as external from a
   *line marker* (`owner/repo@` or a repo URL in the citing row). S250 is a data correction, not a classifier:
   it records which repository the hash actually belongs to, giving the r81 `external-commits.json` binding a
   row to point at instead of relying on S230's wrong anchor. S230 stays append-only as the audit trail; its
   `badlogic/pi-mono commit 7bb48f213…` clause is superseded, while its pi-page observations (label-only, no
   value syntax, page blob sha1 `19d2bf28…`) still stand.
11. **The pi repository path is a rename, not a live repo name.** `https://api.github.com/repos/badlogic/pi-mono`
   answers HTTP 301 to repository 1035029907 whose `full_name` is `earendil-works/pi`, so the "absent from
   pi-mono" statement in S250 is written against that redirect target, and the commit-pinned raw path 404s with
   0 redirects (raw.githubusercontent does not follow the rename). The served page URL keeps working and the
   page bytes are unchanged (`5b980552…`, 4793 B). Recheck stays `90d`: the rename is what a recheck should
   notice.
12. **No token-shape side effect.** The bare 64-hex in the S249/S250 anchors carries no `commit ` prefix, so the
   base instruments' commit classes do not move (Census seat measured `commit_total 46` unchanged and
   `commit_unresolvable` still exactly `corpus/SOURCES.md:171/172`); the `25cc5c7b…` short hash records as the
   green `commit_truncated` INFO class.
