# Round 49 seat report — SrcAgentSkillsOverview (C1 source row S023)

Scope: open Anthropic's Agent Skills overview page myself, record how skill metadata (name,
description) is loaded at startup and used to decide whether a skill applies, check
`corpus/SOURCES.md` for an existing row on that URL, and draft one new row (S023) plus the
round-lesson `## Gate` access-record line. Lane base `a5adc146a2995dcc5a95a6d8db6e5674f75191ac`.

## Findings

**F1 — No existing row covers this URL, so S023 is a new row, not a duplicate.**
Sweeps in the lane (commands and exit codes in § Evidence): `grep -c 'agent-skills/overview'
corpus/SOURCES.md` → 0 (exit 1); `grep -n 'platform.claude.com' corpus/SOURCES.md` → exactly two
hits, S003 and S019, and both are the **best-practices** URL
(`.../agent-skills/best-practices`). S014 is the Anthropic Engineering blog post
(`anthropic.com/research/equipping-agents-for-the-real-world-with-agent-skills`) — a third
document, also not this URL. `grep -c '^| S023 ' corpus/SOURCES.md` → 0 (exit 1); the id is free.
The round-48 search log already lists "Anthropic's best-practices and overview pages" as opened,
and round-48's seat report `C2ClaudeDocs.md:103` records this exact `.md` route's bytes and
hash — but round-48 created no row for it, so contract rule 1 (a row exists only for a source its
author opened in the round that writes the row) is satisfied by this round's own fetch.

**F2 — The page states the level-1 metadata model directly, under its own heading.**
`overview.md:48` is the heading `### Level 1: Metadata (always loaded)`; the load-and-match
sentences are at `overview.md:59`; the level table row is at `overview.md:106`
(`Level 1: Metadata` | `Always (at startup)` | `~100 tokens per Skill` | `name` and `description`
from YAML frontmatter). The trigger-to-load step is at `overview.md:82` (§ Level 2: Instructions
(loaded when triggered)). The `§ Skill structure` field requirements (`name` max 64 characters,
`description` max 1,024 characters, no XML tags) are also on this page, overlapping S019's scope;
the row's scope is deliberately the loading/trigger model, not the field rules, so the two rows do
not compete.

**F3 — Tier is A, kind `docs`, for this scope.** The scope is "how Anthropic's own Claude loads
skill metadata and decides a skill applies", and Anthropic's platform documentation is the
primary and authoritative source for its own product behaviour (`CORPUS.md:93` — tier A: primary
or authoritative for that scope, spec/official docs). The page is vendor documentation, not a
measurement of omp or opencode; that limit is stated in the row's `scope` cell, following S021's
precedent.

**F4 — The page documents no arbitration rule for overlapping descriptions (negative claim with
its sweep).** Sweep over the fetched markdown (all exit 1, count 0): `tie[- ]break`, `overlap`,
`ambigu`, `multiple skills`, `one skill`, `arbitrat`, `conflict`, `both skills`, `select`. What
Anthropic documents is a single match rule — the description is matched against the request —
and nothing about what happens when two installed skills match equally. For the C1 census this
means the overview page can ground the *trigger* half of sibling arbitration but not the
*tie-break* half; the census must not present it as documenting arbitration.

**F5 — No drift.** This round's fetch of `.../overview.md` is byte-identical to round-48's fetch
of the same route: 21,840 B, sha256 `7913d455…` (round-48 record: `.ufo/waves/round-48/build/
C2ClaudeDocs.md:103`). The HTML route at the canonical URL is 557,288 B, sha256 `0c1d8f68…`; it
is server-rendered (the quoted sentence is present in the HTML) but is a large app shell, so the
`.md` route is the reproducible, quotable artifact and the hash recorded on the row.

**F6 — One dependency the L1 must land.** The row's `used-by` is
`corpus/knowledge/sibling-overlap-census-round49.md`, which does not exist in the lane yet. The
census validator emits **E11 (used-by path missing on disk)** for a mined row whose `used-by`
path is absent, so the C1 seat's entry must land before the round's census run, or the row must
hold `status: queued` until it does. I did not create the file (lane read-only except this report).

**F7 — The HTML route and the `.md` route are separate URLs.** The canonical page URL is
`https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview` (200, no redirects,
final URL identical to the request); `.../overview.md` is the reader route (200, `text/markdown`).
Both were fetched this round; the row's `source` cell uses the canonical page URL, the `anchor`
cell records the `.md` fetch with its bytes and hash.

## Deliverable 1 — `corpus/SOURCES.md` row (append after S021, before `## Paths`)

```
| S023 | Claude Docs — Agent Skills overview — https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview | docs | A | Anthropic's documented progressive-disclosure loading model for Claude: how a skill's `name` and `description` enter the system prompt at startup, and how the description decides whether the skill applies (vendor documentation, not a measurement of omp or opencode) | § Level 1: Metadata (always loaded) (`overview.md:48`, text at :59), § Level 2: Instructions (loaded when triggered) (`overview.md:82`), § How Skills work level table (`overview.md:106`); fetched as .../agent-skills/overview.md (200, 21840 B, sha256 `7913d455…`) on 2026-10-22T09:38:50Z, byte-identical to the round-48 fetch of the same route; the HTML route (200, 557288 B, sha256 `0c1d8f68…`) carries the same sentences inside a client app shell | Name and description are the only skill text in context before a trigger: the metadata is loaded at startup into the system prompt and the description is what the request is matched against, so the description decides whether a skill applies; the page states no rule for choosing between overlapping descriptions | mined | 2026-10-22 | 90d | corpus/knowledge/sibling-overlap-census-round49.md |
```

## Deliverable 2 — `corpus/lessons/round-49.md` `## Gate` access-record line

Shape follows the round-48 `## Gate` table (`corpus/lessons/round-48.md` § Gate): one row per new
row, URL, access time (UTC), a ≤25-word quote with its location, and the seat report.

```
| S023 | https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview | 2026-10-22T09:38:50Z | "Claude loads this metadata at startup and includes it in the system prompt." (§ Level 1: Metadata (always loaded), `overview.md:59`) — seat `.ufo/waves/round-49/build/SrcAgentSkillsOverview.md` |
```

Second located quote, for the `teaches` cell and for the census's trigger half (same heading,
`overview.md:59`, verbatim):

> The `description` is what Claude matches your request against when determining whether to trigger the Skill

(16 words, § Level 1: Metadata (always loaded).)

Third located quote, for the load-on-trigger half (`overview.md:82`, § Level 2: Instructions
(loaded when triggered)):

> When you request something that matches a Skill's description, Claude reads `SKILL.md` from the filesystem using bash.

(19 words.)

## Evidence

Fetch (scratch `/fast/scratch/hyaku/kotoba-r49/seats/src-agent-skills-overview/`):

- `curl -sSL -o overview.html -w 'final_url=%{url_effective} http_code=%{http_code} size=%{size_download}
  content_type=%{content_type} num_redirects=%{num_redirects}' -A 'Mozilla/5.0'
  'https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview'` → exit 0;
  `final_url=https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview`,
  `http_code=200`, `size=557288`, `content_type=text/html; charset=utf-8`, `num_redirects=0`.
- `date -u +access_time_utc=%Y-%m-%dT%H:%M:%SZ` → `2026-10-22T09:38:50Z`.
- `sha256sum overview.html` → `0c1d8f6888ead5eda576597e6a902e6e25c9a1c2bc41f4d4845dcda120992c80`;
  `wc -c overview.html` → `557288`.
- Same four commands against `.../overview.md` → exit 0; `final_url=.../overview.md`,
  `http_code=200`, `size=21840`, `content_type=text/markdown; charset=utf-8`, `num_redirects=0`;
  `date -u` → `2026-10-22T09:38:50Z`; `sha256sum overview.md` →
  `7913d4556c014c6bf7f23e186efded1b36da63d7b29d73898267ebe8d2f6258f`; `wc -c overview.md` → `21840`.
- `grep -c 'Level 1: Metadata' overview.html` → 3; `grep -o 'loads this metadata at startup and
  includes it in the system prompt' overview.html` → 1 hit (HTML carries the text).
- `grep -n 'Level 1: Metadata\|loads this metadata at startup\|matches your request against\|only
  its name and description occupy context\|Level 2: Instructions' overview.md` → lines 48, 59, 59,
  59, 61, 106, 107.
- `grep -n 'When you request something that matches' overview.md` → line 82.
- Arbitration sweep (F4): nine `grep -ci` patterns, each count 0, each exit 1.

Lane sweeps (read-only, in `/home/vgpnk/Projects/shokunin/kotoba-shokunin`):

- `grep -c 'agent-skills/overview' corpus/SOURCES.md` → 0 (exit 1).
- `grep -n 'platform.claude.com' corpus/SOURCES.md` → 2 hits (lines 16 and 32: S003 and S019,
  best-practices URL), exit 0.
- `grep -c '^| S023 ' corpus/SOURCES.md` → 0 (exit 1).
- `awk -F'|' '/^\| S0[12][0-9] /{print NF}' corpus/SOURCES.md` → 12 rows, each `13`
  (11 columns + the two edge empties) — the drafted row has the same shape.
- `git rev-parse HEAD` → `a5adc146a2995dcc5a95a6d8db6e5674f75191ac`.

Cross-check of the drafted row against the census validator's rules (read from
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh`): `kind=docs` in the enum; `tier=A` in
`^[ABC]$` and kind is not `community` (no E10); `status=mined` in `queued|mined|rejected`;
`opened=2026-10-22` is a valid ISO past-or-present date; `recheck=90d` is a valid cadence;
NF=13 with no `|` inside any cell; no duplicate URL+scope pair (no E04); `used-by` names one
repo-relative path (E11 applies only until the C1 entry lands — F6).

## Not done / limits

- I did **not** edit `corpus/SOURCES.md` or `corpus/lessons/round-49.md`: the lane checkout is
  read-only for this seat except this report file. Both deliverables are drafts for the L1.
- No tool was installed or upgraded this session; the fetch used the pre-existing `curl`,
  `sha256sum`, `grep`, `awk`, `git` (read-only commands only). No `jj` command was run.
- The page is Anthropic's product documentation, so it describes Claude's behaviour only; it is
  not evidence about omp, opencode, or any sibling lane's host (F3, F4).
- No negative claim is made about sibling lanes here; the census's own rows and sweeps are the
  C1 seats' scope.
