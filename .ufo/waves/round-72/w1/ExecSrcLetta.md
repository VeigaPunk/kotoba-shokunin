# ExecSrcLetta — S261 source opening (Letta Code skills page)

Wave 1 (build), round 72, lane `kotoba-shokunin`. Read-only seat: no committed lane file was
modified; the only lane writes are the S261 snapshots + pin manifest, this seat's build directory
and this report.

## Verdict

**Source reachable and opened (HTTP 200).** Every sentence the staged row and the two citing
entries quote is located on the live page. **One entry claim is unsupported: the entry says
"six named agents"; the page names five** (`skill-vs-always-on-boundary.md:44`). Two further claims
are confirmed only after shaping (`shared .agents/skills/ root`; `three scopes` against a page whose
own table lists four Location rows). The staged URL is a **redirect** — canonical host+path is
`docs.letta.com` + `/configuration/skills` — and the lane holds **no** `letta` row, so S261 is new
ground and not a duplicate.

| claim (file:line) | verdict |
|---|---|
| row S261 quote 1, the standard sentence (`SOURCES.append.md:65`) | confirmed-after-shaping (anchor markup dropped; verbatim in the rendered page) |
| row S261 quote 2, the portability sentence (`SOURCES.append.md:65`) | **confirmed** (byte-exact in raw `.md` and raw `.html`) |
| row S261 scope labels 「Project-scoped」/「Agent-scoped (MemFS)」/「Computer-scoped」 | confirmed (as flowchart labels and as `###` headings); the 「」 brackets are schema markers, not page bytes |
| entry quote pair (`skill-vs-always-on-boundary.md:41-43`) | confirmed-after-shaping (one anchor between the two sentences) |
| "Portability across **six named agents**" (`skill-vs-always-on-boundary.md:44`) | **absent** — the page names five |
| "Letta registers skills from **three scopes** rather than two" (`skill-paths-and-precedence.md:38-39`) | confirmed-after-shaping (page's own table has a fourth Location class, `Built-in`) |
| "project scope at the **shared** `.agents/skills/` root" (`skill-paths-and-precedence.md:39`) | confirmed-after-shaping (page says "Primary project-local location…"; "shared" is the lane's word) |
| "**agent-scoped** tier stored inside the agent's own memory filesystem" (`:40`) | confirmed (page: "stored inside that agent's git-backed memory filesystem") |
| "computer-scoped bundle under `~/.letta/skills/`" (`:41`) | confirmed |
| "A skill can therefore belong to a particular agent rather than to a user or a project" (`:41-42`) | confirmed (identity + "cloned to whatever computer the agent is currently working on") |

## Source opened — exact fetch

```
curl -fsSL -A 'Mozilla/5.0' -w 'HTTP=%{http_code} FINAL=%{url_effective} SIZE=%{size_download}\n' \
  'https://docs.letta.com/letta-code/skills/' -o letta-skills.html
HTTP=200 FINAL=https://docs.letta.com/configuration/skills SIZE=92885
```

Redirect chain (headers, `curl -D -`):

```
HTTP/2 308  location: /letta-code/skills      server: Vercel
HTTP/2 308  location: /configuration/skills   server: Vercel
HTTP/2 200  content-type: text/html; charset=utf-8  content-length: 92885
```

- Access date: **2026-10-25** (UTC; first fetch 21:36:56Z).
- Canonical URL for the L1's registry row: `docs.letta.com` + `/configuration/skills`.
- Rendered page: 92,885 bytes, sha256 `37d17d389fad15eb242c841870f337b4ed04ad9fe8f5f0aee1f505e1cae9556b`,
  etag `d13b4c1fbfe8b7cf1015ca1bfac31ea7`, `last-modified Tue, 20 Oct 2026 02:34:27 GMT`.
- Markdown export: `https://docs.letta.com/configuration/skills.md` → 200, 8,023 bytes,
  sha256 `20cda226c847d639f642a8d21583d49f2603c3ae07a56844bfc4164214617fbe`, etag
  `25f4bbfaba2c7ccd77f3959c28b1d568`. `…/skills/index.md` is **byte-identical** (`cmp` silent).
- `/letta-code/skills.md` → **404** (the `.md` suffix only works on the canonical path).
- `llms.txt` and `llms-full.txt` are **byte-identical** on this host (both 28,059 bytes, sha256
  `9815ce9c…`), so `llms-full.txt` is not a superset crawl source.
- Both forms are byte-stable across two fetches in the same minute (same sha256 for md2/html2).

## Snapshots written (only committed-file-shaped write outside the build dir)

```
.ufo/waves/round-72/snapshots/S261-letta-skills.md             8023  sha256 20cda226c847d639f642a8d21583d49f2603c3ae07a56844bfc4164214617fbe
.ufo/waves/round-72/snapshots/S261-letta-skills.html          92885  sha256 37d17d389fad15eb242c841870f337b4ed04ad9fe8f5f0aee1f505e1cae9556b
.ufo/waves/round-72/snapshots/S261-letta-skills.rendered.txt   9428  sha256 a570d39b49d7b0628472d77162506c066cb212220e7e29cc599ed86dd0cc6164
.ufo/waves/round-72/snapshots/S261.sha256                             (sha256sum-style manifest, same shape as the sibling S262.sha256)
```

`S261-letta-skills.rendered.txt` is **derived, not fetched**: `python3 -B
.ufo/waves/round-72/w1/build/ExecSrcLetta/render_text.py --write` (drop `<script>`/`<style>`, strip
tags, unescape entities; no whitespace rewriting). Re-running it reproduces `a570d39b…` byte for
byte. It exists for exactly one reason: the row's own first quote is split by an anchor element in
both raw forms, so it is locatable word-bounded **only** in the rendered text. The raw `.md` and
`.html` remain the snapshots of record; if the L1 prefers raw-only snapshots, delete the derived
file and use quote cell **Q2** below.

## Which form each quote lives in

| quote | raw `.md` | raw `.html` | rendered text |
|---|---|---|---|
| Q1 "The Letta agent harness implements the open Agent Skills standard." (10 words) | **no** — split by `[Agent Skills](https://agentskills.io)` | **no** — split by `<a href="https://agentskills.io">Agent Skills</a>` | **yes**, byte offset 1907 |
| Q2 "Skills are portable across Letta, Codex, Claude Code, Hermes Agent, OpenClaw, and other compatible agents." (15 words) | **yes**, line 15, offset 315 | **yes**, line 162, offset 64549 | yes, offset 1974 |
| Q1+Q2 as the entry prints them (25 words) | no | no | yes, offset 1907 |
| Q10 three-scope prose span (21 words) | yes, line 25, offset 1444 | yes, line 168, offset 66510 | yes, offset 3054 |
| Q5 / Q6 / Q11 (table-cell text) | yes (lines 48/49/50) | yes (line 215) | **no** — cells concatenate without whitespace |

Dropped bytes, named: for **Q1** the `.md` drops `[Agent Skills](https://agentskills.io)` (38 bytes)
in favour of `Agent Skills` (12 bytes) — 26 bytes of markup; the `.html` drops
`<a href="https://agentskills.io">Agent Skills</a>` (49 bytes) in favour of the same 12 bytes — 37
bytes of markup. The rendered text drops nothing but tags. For every other quote no bytes are
dropped: the quote is a literal substring of the raw bytes.

## Located quotes (per quote: located, heading, line, quote pasted from the snapshot)

Line numbers are 1-based in `S261-letta-skills.md`; `sed -n '<L>p'` output is pasted. Quotes are
≤25 words; where a line is longer, the quote is the named span of it.

1. **Q1 — located (rendered only).** Section: page intro, before `## Skill scopes` (`md:15`).
   `sed -n '15p'` → `The Letta agent harness implements the open [Agent Skills](https://agentskills.io) standard. Skills are portable across Letta, Codex, Claude Code, Hermes Agent, OpenClaw, and other compatible agents.`
   Quote (10 words): "The Letta agent harness implements the open Agent Skills standard." Located in
   `S261-letta-skills.rendered.txt` byte 1907; **not** in raw md/html (see dropped bytes above).
2. **Q2 — located yes, all three forms.** Same line 15.
   Quote (15 words): "Skills are portable across Letta, Codex, Claude Code, Hermes Agent, OpenClaw, and other compatible agents."
   Byte-exact contiguous in the raw bytes (md offset 315, html offset 64549).
3. **Q3a/b/c — located yes.** Section `## Skill scopes` (`md:23`), flowchart fence.
   `sed -n '29p'` → `    subgraph Project["Project-scoped"]`
   `sed -n '33p'` → `    subgraph AgentScope["Agent-scoped (MemFS)"]`
   `sed -n '37p'` → `    subgraph Bundled["Computer-scoped"]`
   The row writes them inside 「」 (CJK corner brackets, the campaign schema's quote markers) — those
   brackets are **not** page bytes. The same three words also head `### Project-scoped skills`
   (`md:57`), `### Agent-scoped skills` (`md:53`), `### Computer-scoped skills` (`md:61`).
4. **Q10 — located yes (row's three-scope model, 21 words, contiguous prose).**
   `sed -n '25p'` → `Agents are able to use skills from the current project (project-scoped skills), their own memory (agent-scoped skills), and skills provided automatically by the Letta harness (bundled skills). Letta automatically registers skills from the current project (`.agents/skills`), current computer (`~/.letta/skills`), and current agent.`
   Quote (21 words): "from the current project (project-scoped skills), their own memory (agent-scoped skills), and skills provided automatically by the Letta harness (bundled skills)".
5. **Q5 — located yes (agent-scoped tier).** Section `## Skill scopes`, table (`md:48`).
   `sed -n '48p'` → `| `${MEMORY_DIR}/skills/`   | Agent    | Persistent skills specific to one Letta agent, stored inside that agent’s git-backed memory filesystem |`
   Quote (7 words): "stored inside that agent’s git-backed memory filesystem".
6. **Q6 — located yes (project scope).** `sed -n '49p'` → `| `.agents/skills/`         | Project  | Primary project-local location for interactive client-side skills                                      |`
   Quote (7 words): "Primary project-local location for interactive client-side skills".
7. **Q11 — located yes (computer scope).** `sed -n '50p'` → `| `~/.letta/skills/`        | Computer | Skills shared across all Letta agents running on this machine                                          |`
   Quote (10 words): "Skills shared across all Letta agents running on this machine".
8. **Q7 "six named agents" — located NO** in all three forms; `grep -c six S261-letta-skills.md`
   → `0`. See defect 1.
9. **Q8 "three-scope" / Q9 "Letta registers skills from three scopes rather than two" — located
   NO** as strings; both are the lane's/campaign's labels for the page's model, not page sentences.

## Defects found (each with the command that shows it)

1. **`skill-vs-always-on-boundary.md:44` overcounts the portability list.** The entry writes
   "Portability across six named agents". The page names **five**: `grep -o 'Letta, Codex, Claude
   Code, Hermes Agent, OpenClaw'` on `md:15` returns exactly that run, and the sentence then says
   "and other compatible agents" — an unnamed remainder, not a sixth name. `grep -c six
   S261-letta-skills.md` → `0`. A scan for other client names on the page
   (`Cursor Windsurf Roo goose Copilot Gemini Zed Continue`) returns `0` each. **Fix for the L1:
   "five named agents, plus unnamed 'other compatible agents'"**, or drop the count.
2. **`skill-paths-and-precedence.md:39` calls `.agents/skills/` "the shared … root"; the page does
   not.** The page's words are "Primary project-local location for interactive client-side skills"
   (`md:49`). "Shared" is a cross-vendor lane fact (goose/opencode), not a Letta claim — the entry
   should attribute it, not quote it as Letta's.
3. **"three scopes" vs the page's four Location rows.** `sed -n '46,51p'` shows a table with
   `Agent`, `Project`, `Computer` **and** `Built-in` ("Skills that ship with Letta Code (always
   available to any Letta agent)"), and `md:25`'s own prose lists the third as *bundled*, not
   *computer*. The flowchart has three subgraphs but labels the third `Bundled["Computer-scoped"]` —
   the page's own label/id mismatch. The three-scope model is defensible as the *user-controllable*
   scope axis; it is not the whole of what the page lists. Any A4 rule sentence that says "Letta has
   three scopes" must not imply the page lists only three.
4. **The staged URL is a redirect (two 308 hops).** Canonical: `docs.letta.com` +
   `/configuration/skills`. If the registry row records the staged `/letta-code/skills/` form, a
   future re-fetch depends on Letta keeping the alias; the `.md` export **404s** on the alias path
   today, so a re-pin that appends `.md` to the staged URL will fail.
5. **Freshness datum for C2/re-pin:** the `.md` export's `last-modified` is request-time
   (21:37:10Z, after the HTML's 2026-10-20T02:34:27Z build) and does not move on refetch — it cannot
   serve as a change signal. Pin the sha256/etag. The HTML build date (2026-10-20) predates the
   package's `opened` date (2026-10-23), which is consistent with the package quoting this build.

## Lane-duplicate check (for the L1)

Host + canonical path: `docs.letta.com` + `/configuration/skills` (redirect source
`/letta-code/skills`). `grep -rin 'letta' corpus/SOURCES.md corpus/knowledge/ SKILL.md` returns **no
match**, and `corpus/README.md` has none: S261 is new ground, no lane duplicate, and no other row in
the lane points at this host.

## Recommendation for C1's A4 row (`corpus/knowledge/resident-index-and-rungs-round72.md`)

- **Use Q2 as the S261 quote cell** (15 words, contiguous in raw `.md` *and* raw `.html`). If the row
  needs the three-scope model quoted, use **Q10** (21 words, contiguous in all three forms).
- Do **not** use Q1 as a quote cell unless the derived rendered snapshot is accepted: in both raw
  forms the sentence is split by one anchor. Predicate (d)'s word-bounded check would read it absent.
- **Counter caution:** a word-bounded check against `S261-letta-skills.rendered.txt` will *falsely
  fail* table-cell quotes (Q6, Q11) because rendered cells concatenate with no separator
  (`…skills/ProjectPrimary project-local…`). Table-derived quotes must be checked against the `.md`.
- The row's anchor cell should keep the page's own label `Agent-scoped (MemFS)`; the 「」 brackets are
  schema markers, so the counter must not search for them.
- The staged row is a clean 11-cell row (`SOURCES.append.md:65`: 11 cells by pipe-split, no escaped
  pipe) with status `mined`, tier `B`, `used-by` naming both
  `corpus/knowledge/skill-paths-and-precedence.md` and
  `corpus/knowledge/skill-vs-always-on-boundary.md` — predicate (b) inputs are intact; the A4 entry
  itself does not exist yet at the base (`ls corpus/knowledge/resident-index-and-rungs-round72.md` →
  absent), so predicate (c) is the L1's to satisfy.

## Files written

- `.ufo/waves/round-72/snapshots/S261-letta-skills.md`, `S261-letta-skills.html`,
  `S261-letta-skills.rendered.txt`, `S261.sha256`
- `.ufo/waves/round-72/w1/build/ExecSrcLetta/locate_quotes.py` (re-runnable locator, 12 quotes × 3
  forms), `located-quotes.txt` (its output), `render_text.py`, `provenance.txt`
- `.ufo/waves/round-72/w1/ExecSrcLetta.md` (this report)

No tool was installed or upgraded. Scratch dir `/tmp/k72w1-ExecSrcLetta.*` deleted before return. No
committed lane file, fleet repo, sibling lane, `shokuknow` package, jj state or git index was
modified.

## Risks / blockers

- None blocking. One risk: if the L1 commits only the raw snapshots, Q1 (the row's own first quote)
  cannot pass predicate (d) — either commit the derived rendered form or set the row's quote cell to
  Q2/Q10.
- Unobserved: I did not run any lane gate (out of scope for this seat), and I did not check whether
  the page changed between the package's 2026-10-23 `opened` date and today beyond the HTML build
  date and the byte-stability refetch — no archived 2026-10-23 copy was fetched.
