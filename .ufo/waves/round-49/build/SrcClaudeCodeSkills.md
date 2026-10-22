# Round 49 seat report — SrcClaudeCodeSkills (C1 source row S022)

Scope: open Claude Code's skills documentation myself, record what it says about (a) how Claude
decides which skill to use (the `description`'s role) and (b) what to do when skills conflict or
overlap, check `corpus/SOURCES.md` for an existing row on that URL, and draft one new row (S022)
plus the round-lesson `## Gate` access-record line. Lane base
`a5adc146a2995dcc5a95a6d8db6e5674f75191ac`. Read-only on the lane; only this report was written.

## Findings

**F1 — The URL is not a row; S022 is a new row, not a duplicate.**
`grep -c 'code\.claude\.com' corpus/SOURCES.md` → 0 (exit 1). The only `claude.com` URLs in the
registry are `platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices` (S003 and
its superseding S019) — a different host path and a different document. `grep -c '^| S022 '` → 0
(exit 1), so the id is free; the sibling seat `SrcAgentSkillsOverview.md` took S023 for the
`platform.claude.com` overview page, so no id collision. Round 48 opened this same route and
recorded its hash in `.ufo/waves/round-48/build/C2ClaudeDocs.md:104` but created no row, so
contract rule 1 is satisfied by this round's own fetch.

**F2 — Final URL, redirect, and the `.md` variant.**
`https://code.claude.com/docs/en/skills` does not redirect: `curl -sSL` reports
`FINAL_URL:https://code.claude.com/docs/en/skills`, `HTTP:200`. A markdown variant exists at
`https://code.claude.com/docs/en/skills.md` (`HTTP:200`, 1,234 lines) and is the quotable route;
the HTML route is a 1,233,129-byte JS shell carrying the same prose. Both were fetched twice with
byte-identical results (exit 0 from `cmp`).

| route | accessed (UTC) | HTTP | bytes | sha256 |
|---|---|---|---|---|
| https://code.claude.com/docs/en/skills | 2026-10-22T09:38:48Z, re-fetch 09:42:19Z | 200 | 1,233,129 | `102195341251387cee65e8d8f47809878c3c118a12f53fff64bea966a6c42ee2` |
| https://code.claude.com/docs/en/skills.md | 2026-10-22T09:39:04Z, re-fetch 09:41:02Z | 200 | 111,557 | `cdfcb0df93072710866de536ba823c06a0804038d488cd27a2ba48ad114cd456` |

The `.md` hash is byte-identical to the round-48 fetch of the same route
(`C2ClaudeDocs.md:104` recorded `cdfcb0df…`), so no editorial drift since round 48.

**F3 — (a) The `description` is the routing field, stated twice.**
§ Frontmatter reference, `description` row (`skills.md:389`) says Claude uses it to decide when
to apply the skill; § Create your first skill (`skills.md:114`) says the same in prose. If the
field is omitted the first non-empty line of the body is used instead (`skills.md:389`). The
listing itself is budgeted: the combined `description` + `when_to_use` text is truncated at
1,536 characters in the skill listing, and the listing budget is 1% of the model's context
window, with descriptions dropped starting from the least-invoked skills
(§ Skill descriptions are cut short, `skills.md:1207`).

**F4 — (b) The page has no arbitration vocabulary; its two collision rules are by name and by
origin.** Negative claims with their sweeps over the fetched markdown (all count 0, exit 1):
`grep -ciE 'arbitrat'` → 0; `grep -ciE 'tie-?break'` → 0; `grep -ciE 'ambigu'` → 0;
`grep -ciE 'overlap'` → 0. `grep -niE 'conflict'` → 1 hit, `skills.md:49`, and that line is about
`/doctor prompt-audit` flagging conflicting *instruction files*, not skills. What the page does
give is (i) § Resolve skills that share a name (`skills.md:196-198`): a name clash is settled by
origin, enterprise over personal over project, with plugin skills namespaced so both load; and
(ii) § Troubleshooting → § Skill triggers too often (`skills.md:1190-1195`): when a skill fires
where it should not, make the description more specific, or set `disable-model-invocation: true`
for manual-only invocation. For the sibling-overlap census this is the operative rule: with no
declared-priority field, a sibling lane's description must itself exclude the neighbours'
requests, or be taken out of automatic invocation.

**F5 — Tier A, kind `docs`, for this scope.** The scope is how Claude Code itself selects a
skill and what its own documentation says about collisions; Anthropic's product documentation is
primary and authoritative for that scope (contract tier A: spec/official docs). Following S021's
precedent, the scope cell states the limit: vendor documentation, not a measurement of omp or
opencode.

**F6 — Landing-order constraint (E11), and the row validates clean once the entry exists.**
`corpus/knowledge/sibling-overlap-census-round49.md` does not exist on disk yet (`ls` → exit 2), so
a `mined` row pointing at it trips the census script's E11 (`used-by path missing on disk`) until
the C1 entry lands. The row must be appended **after** that entry exists; the id and the used-by
path are otherwise as specified.

Validated with the fleet's own instrument, in a scratch mirror of the lane registry
(`/fast/scratch/hyaku/kotoba-r49/seats/SrcClaudeCodeSkills/mirror/`, the lane itself untouched):

- `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` on the **unmodified**
  lane registry → exit 0, `kotoba ok`, three W04 warnings (S018, S019, S021) — the plan's stated
  frontier figure, reproduced.
- Draft row appended to a copy of the registry, with the sibling used-by paths materialized and
  the census entry **absent**: exit 1, `E11 S022 missing used-by
  corpus/knowledge/sibling-overlap-census-round49.md` — the only E-code, and the draft row
  provably causes it and nothing else.
- Same mirror with the census entry materialized: exit 0, `mirror ok`, three W04 warnings, **no
  E-code and no new W04** for S022 (its URL is new to the registry). The row is therefore
  contract-clean once the C1 entry lands.

Row shape checked independently: the drafted line splits into 13 pipe-separated fields
(`awk -F'|'`/Python `split('|')` → 13), matching the `NF=13` shape of every existing row and the
header.

## Deliverable 1 — `corpus/SOURCES.md` row (append after S021, before `## Paths`)

```markdown
| S022 | Claude Code — Extend Claude with skills — https://code.claude.com/docs/en/skills | docs | A | How Claude Code decides which of several available skills to use (the `description`'s role) and what the page says about skills that collide (vendor documentation, not a measurement of omp or opencode) | § Frontmatter reference, `description` row (`skills.md:389`); § Create your first skill (`skills.md:114`); § Resolve skills that share a name (`skills.md:196-198`); § Troubleshooting → § Skill triggers too often (`skills.md:1190-1195`); fetched as https://code.claude.com/docs/en/skills.md (200, 111557 B, sha256 `cdfcb0df…`) on 2026-10-22T09:41:02Z, byte-identical to the round-48 fetch of the same route; the HTML route (200, 1233129 B, sha256 `10219534…`) serves the same prose and did not redirect | Claude picks a skill by its `description` alone — the `description` is the field Claude uses to decide whether a skill applies — and the page states no arbitration rule for overlapping descriptions (sweeps: `arbitrat`, `tie-?break`, `ambigu`, `overlap` → 0 each); a name clash is settled by origin (enterprise over personal over project), and a skill that fires where it should not is fixed by making the description more specific or by setting `disable-model-invocation: true` | mined | 2026-10-22 | 90d | corpus/knowledge/sibling-overlap-census-round49.md |
```

## Deliverable 2 — round-lesson `## Gate` access-record line

```markdown
| S022 | https://code.claude.com/docs/en/skills | 2026-10-22T09:41:02Z | "What the skill does and when to use it. Claude uses this to decide when to apply the skill." (§ Frontmatter reference, `skills.md:389`) — seat `.ufo/waves/round-49/build/SrcClaudeCodeSkills.md` |
```

Second located quote, held in reserve for the conflict half of the scope (19 words, verbatim,
heading `§ Resolve skills that share a name`, `skills.md:198`):

> "When two skills share a directory or file name, where each one came from decides which one `/name` runs."

## Evidence (commands, exit codes, paths)

- `grep -c 'code\.claude\.com' corpus/SOURCES.md` → 0, exit 1 (no row on this URL).
- `grep -o 'https://[a-z.]*claude\.com[^ |]*' corpus/SOURCES.md | sort -u` → one URL,
  `platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices` (S003, S019).
- `grep -c '^| S022 ' corpus/SOURCES.md` → 0, exit 1 (id free; sibling seat took S023).
- `curl -sSL -w 'FINAL_URL:...HTTP:...BYTES:...' https://code.claude.com/docs/en/skills` →
  `FINAL_URL:https://code.claude.com/docs/en/skills`, `HTTP:200`, `BYTES:1233129`; sha256
  `102195341251387cee65e8d8f47809878c3c118a12f53fff64bea966a6c42ee2`; second fetch 09:42:19Z,
  byte-identical (`cmp` exit 0).
- `curl -sSL … https://code.claude.com/docs/en/skills.md` → `FINAL_URL:https://code.claude.com/docs/en/skills.md`,
  `HTTP:200`, `BYTES:111557`; sha256 `cdfcb0df93072710866de536ba823c06a0804038d488cd27a2ba48ad114cd456`;
  second fetch 2026-10-22T09:41:02Z byte-identical (`cmp` exit 0). `wc -l` → 1,234 lines.
- Negative sweeps on the fetched markdown, all count 0 / exit 1 unless stated: `grep -ciE 'arbitrat'` → 0;
  `grep -ciE 'tie-?break'` → 0; `grep -ciE 'ambigu'` → 0; `grep -ciE 'overlap'` → 0;
  `grep -niE 'conflict'` → 1 hit at `skills.md:49` (prompt-audit, about instruction files).
- Quoted lines read with `sed -n '<n>p'`: 114, 196-198, 389, 1190-1195, 1207.
- `grep -c 'code\.claude\.com' .ufo/waves/round-48/build/C2ClaudeDocs.md` → 1 hit at line 104
  (round-48 hash record for the same route, matching this fetch).
- `ls corpus/knowledge/sibling-overlap-census-round49.md` → exit 2 (not yet on disk; see F6).
- `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
  /home/vgpnk/Projects/shokunin kotoba` (cwd = lane root, lane registry unmodified) → exit 0;
  `kotoba ok`; W04 for S018, S019, S021.
- Same instrument on the scratch mirror with the draft row appended and the census entry absent →
  exit 1; only `E11 S022 missing used-by corpus/knowledge/sibling-overlap-census-round49.md`.
- Same mirror with the census entry materialized → exit 0; `mirror ok`; three W04; no E-code and
  no new W04 for S022.

## Out of scope

- Editing `corpus/SOURCES.md`, `corpus/lessons/round-49.md` or the census entry: this seat
  delivers drafts only (read-only lane bound; the L1 integrates).
- Measuring omp's or opencode's actual skill arbitration — this row documents Claude Code only,
  and the scope cell says so.
- A `recheck:` script for the census entry (owned by the C1 seat).

## Tooling

None installed or upgraded this session; no tool was needed beyond `curl`, `grep`, `sed`, `cmp`,
`sha256sum` and `date`, all already present. No `pacman`, `uv tool`, `cargo` or `npm -g`
transaction was run.
