# ExecSrcPi — staged row S263 opened (round 72, wave 1 build)

**Verdict: the S263 source is live and both sentences the row and the entry quote are located
verbatim in it — the pi page states the middle rung in the exact words the row attributes to it.
Two things the entry carries are *not* on the page: the word "MCP" (0 occurrences; the page's own
third rung is "executable integration point", defined in the sibling `docs/extensions.md` as
"TypeScript modules that add executable behavior"), and any mention of `AGENTS.md` or an always-on
file (0 occurrences), so pi supports the *middle* rung and the *resident index* but not the
"not in `AGENTS.md`" half of the entry's title. The source is fresh at the byte level: the last
commit touching the path is 2026-09-22, before the staged retrieval of 2026-10-23, so nothing
changed between the package's `opened` date and today. Two defects handed to the L1: the cited URL
is a legacy repo alias (`badlogic/pi-mono` → `earendil-works/pi`, GitHub HTML 301, raw path serves
identical bytes), and the entry's "round 6's S268" is a staged-package id, not a lane id (the lane
has 139 rows, max `S213`).**

Deliverables: snapshots under `.ufo/waves/round-72/snapshots/` (pins in `S263.sha256`), the
append-ready block at `.ufo/waves/round-72/w1/build/ExecSrcPi/a4-source-block.md`, this report.
No lane file was modified; no git write; no jj command; scratch `/tmp/k72w1-ExecSrcPi.3CA8`
deleted before return.

## 1. Fetch record

Command (from `/tmp`, scratch `mktemp -d /tmp/k72w1-ExecSrcPi.XXXX`):

```
curl -fsSL -A 'Mozilla/5.0' -w 'HTTP_STATUS=%{http_code}\nFINAL_URL=%{url_effective}\nBYTES=%{size_download}\n' \
  'https://raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/docs/skills.md' -o "$S/pi-skills.md"
```

Observed:

```
HTTP_STATUS=200
FINAL_URL=https://raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/docs/skills.md
BYTES=4793
EXIT=0
5b9805525b194474ef1fe5455a0917ef15ed7f710aa9bec2eee11879556469e5  /tmp/k72w1-ExecSrcPi.3CA8/pi-skills.md
2026-10-25T21:37:01Z
  93 4793 /tmp/k72w1-ExecSrcPi.3CA8/pi-skills.md
```

- URL host + path: `raw.githubusercontent.com` / `/badlogic/pi-mono/main/packages/coding-agent/docs/skills.md`.
- Access date 2026-10-25 (UTC 21:37:01Z), HTTP 200, no redirect on the raw host, 4 793 B, 93 lines,
  sha256 `5b9805525b194474ef1fe5455a0917ef15ed7f710aa9bec2eee11879556469e5`.
- Snapshot: `.ufo/waves/round-72/snapshots/S263-pi-skills.md` (same sha256, verified after copy).

## 2. Every sentence the row or the entry quotes — located

Both quoted sentences are in the file's preamble under the H1 `# Skills`; the next heading is
`## Create a skill` at line 9 (`grep -n "^#"` on the snapshot gives `1:# Skills`, `9:## Create a skill`).

| quoted by | located | heading | line | words |
|---|---|---|---|---|
| row S263 quote cell, and entry § *Four vendors* bullet 2 (second half) | yes | `# Skills` (preamble) | 3 | 21 |
| row S263 quote cell ("also"), entry § *Four vendors* bullet 2 (first half) | yes | `# Skills` (preamble) | 5 | 22 |

Evidence, pasted from `sed -n '<L>p' .ufo/waves/round-72/snapshots/S263-pi-skills.md`:

line 3 (219 chars; quote at chars 92–218):

```
Skills give Pi specialized instructions and supporting files for a particular kind of work. Pi advertises each available skill by name and description, then loads its full instructions only when the task calls for them.
```

Quote used: `Pi advertises each available skill by name and description, then loads its full instructions only when the task calls for them.`
(21 words). Dropped bytes: the preceding sentence `Skills give Pi specialized instructions and
supporting files for a particular kind of work.` plus one space; nothing dropped after the quote.
Word-bounded occurrences of the quote in the snapshot: 1 (Python `re` with `(?<![\w-])…(?![\w-])`).

line 5 (203 chars; quote at chars 0–122):

```
Use a skill when a workflow needs more context than a prompt template but does not need a new executable integration point. Skills can bundle scripts, references, and assets alongside their instructions.
```

Quote used: `Use a skill when a workflow needs more context than a prompt template but does not need a new executable integration point.`
(22 words). Dropped bytes: ` Skills can bundle scripts, references, and assets alongside their
instructions.` after the quote; nothing dropped before it. Word-bounded occurrences: 1.

Both quotes are pure ASCII on their own lines (non-ASCII set of the whole file is
`’ “ ” ─ │ └ ├`; line 3 and line 5 contain none — checked per line).

No other string in the row or the entry is presented as a quotation from this page. The row's
`teaches` cell ("a skill is for a workflow that needs more context than a prompt template but not
a new executable integration point — between a prompt and an MCP tool") and the entry's "The
ladder, in the same form, with the third rung named as an MCP-style executable integration" are
paraphrase, not quote — see § 4.

## 3. Which form the quote lives in — rendered page and `.md`

The cited URL *is* the raw markdown, so the `.md` is the primary form. A rendered form exists and
carries the same text:

```
curl -fsSL -A 'Mozilla/5.0' 'https://pi.dev/docs/latest/skills' -o "$S/pi-docs-skills.html" -w 'HTTP=%{http_code} …'
HTTP=200 FINAL=https://pi.dev/docs/latest/skills TYPE=text/html; charset=UTF-8 BYTES=60383
1e9de5d74c7f2fe210c96786ed4950e38ffb5eb4d1a6a33ec48bea16327d438e
```

`https://pi.dev/docs/skills` and `https://pi.dev/docs/skills.md` are 404; the route is
`/docs/latest/skills`, linked from `/docs/latest` (`href="/docs/latest/skills"`). The page's own
"Edit this page" link points at
`https://github.com/earendil-works/pi/edit/main/packages/coding-agent/docs/skills.md`.

Parity probe — after stripping tags and unescaping entities, seven probe sentences from the
snapshot all appear contiguously in the rendered HTML (`FOUND` for all seven): line 3, line 5,
line 43 (`It does not add the full instructions.`), line 45, line 65, line 83, line 85. So the
row's rationale ("the raw file is cited because it is the text the rendered page serves") is
observed true today, not merely asserted. The GitHub blob view also carries the sentence
(`https://github.com/badlogic/pi-mono/blob/main/…` → 301 → `earendil-works/pi`, HTTP 200,
`grep -c "executable integration point"` = 2 matching lines, 3 occurrences, in the rendered HTML).

Snapshot of the rendered form: `.ufo/waves/round-72/snapshots/S263-pi-docs-skills.html`
(60 383 B, sha256 `1e9de5d7…`).

## 4. Verdict per claim in the entry that rests on this source

Entry read: `/home/vgpnk/Projects/shokuknow/merge/kotoba/knowledge/corpus/knowledge/skill-vs-always-on-boundary.md`
(`source: S263` line 5; § *Four vendors, one ladder…* bullet 2; § *What this gives the lane*).

1. **"pi: 'Use a skill when a workflow needs more context than a prompt template but does not need
   a new executable integration point.'"** — **confirmed**, verbatim at snapshot line 5, 22 words,
   one occurrence. The entry's typographic rendering (straight quotes, no ellipsis) matches the
   bytes exactly.
2. **"The ladder, in the same form, with the third rung named as an MCP-style executable
   integration."** — **confirmed-after-shaping**. "executable integration point" is the page's
   phrase (line 5); "MCP" is not: `grep -ci mcp` on the snapshot = 0, and the page's sibling
   `docs/extensions.md` line 3 defines that rung in its own words —
   `Extensions are TypeScript modules that add executable behavior to Pi. Use one when a workflow needs tools, commands, event handlers, model providers, session state, or terminal UI rather than instructions alone.`
   (31 words, so above the 25-word quote-cell cap; its first sentence is 10 words:
   `Extensions are TypeScript modules that add executable behavior to Pi.`)
   The shaping is the corpus naming the executable rung "MCP-style"; the source never does.
   Freshness of that gloss is *worse* than stale: pi announced MCP support on 2026-09-29
   (`https://earendil.com/posts/you-said-no-mcp/`: "If you went to pi.dev in the past, you found a
   proud declaration that Pi does not support MCP"), seven days *after* the last edit to
   `skills.md` (2026-09-22), so the doc predates the reversal and still says neither.
3. **The entry's title frame — "what belongs in a skill and not in `AGENTS.md`" — and the plan's
   A4 wording "versus an always-on file"** — **absent from this source**. `grep -c 'AGENTS.md'` = 0,
   `grep -ci 'always-on\|always on'` = 0. The only resident-surface word on the page is "system
   prompt" (line 43). pi's ladder is prompt template → skill → executable integration point; the
   always-on rung must be carried by S262 (Factory: "Use skills when instructions are too specific
   for always-on AGENTS.md") or by the corpus's own rung text. The entry as written puts pi under a
   heading pi does not support.
4. **Row S263 `teaches` cell, "the same decision boundary as S262 from a different vendor"** —
   **confirmed-after-shaping**: both vendors put the skill in the middle, but they bound different
   sides. S262 bounds the skill against an always-on file; pi bounds it against a prompt template
   below and an executable integration point above. "Same decision boundary" is true only for the
   middle-rung assertion, not for the boundary's other edge.
5. **Row S263 `anchor` cell, "the '# Skills' heading of the file"** — **confirmed**: both sentences
   sit under the H1 `# Skills` with no intervening heading until line 9.
6. **Entry's other sources (S261 Letta, S262 Factory, S264 Hermes, S268 Anthropic-JP, round-5
   Vercel)** — not this seat's source; no verdict given here. One cross-reference defect is visible
   from my side and is reported in § 7.

## 5. Freshness — the staged bytes are still current, and the pin is available

```
curl -fsSL 'https://api.github.com/repos/badlogic/pi-mono/commits?path=packages/coding-agent/docs/skills.md&per_page=100'
commits touching path: 31
25cc5c7bf4cb 2026-09-22T14:48:19Z docs(coding-agent): refresh documentation (#9898)
1d6dbf9e3d60 2026-09-03T09:08:26Z fix(coding-agent): keep skills available with bash-only tools (#8552)
…
09bca9672fcf 2025-12-12T17:24:52Z Add skills system with Claude Code compatibility (#171)
```

Newest commit touching the path: 2026-09-22, i.e. **before** the staged retrieval date
2026-10-23. Nothing changed between the package's `opened` date and 2026-10-25, so the staged
quotes are current at the byte level and the row's `mined` / `90d` status is honest.

Pinnable identity for a lane row (the lane pins upstream commits for S209/S212-style rows):

```
GET /repos/earendil-works/pi/contents/packages/coding-agent/docs/skills.md?ref=main
blob sha 19d2bf28910ce49caaaf4dde86d1e96330ca7b31 ; size 4793
```

## 6. Duplicate-URL input for the L1

- Cited form: `raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/docs/skills.md`.
- Live canonical form: `raw.githubusercontent.com/earendil-works/pi/main/packages/coding-agent/docs/skills.md`
  — same bytes today (`cmp` → `IDENTICAL`, both sha256 `5b980552…`).
- Rendered: `pi.dev/docs/latest/skills`.
- Repo move evidence: `curl -sSI https://github.com/badlogic/pi-mono` → `HTTP/2 301`,
  `location: https://github.com/earendil-works/pi`. The raw host serves the old path with a
  straight 200 (no `location:` header), so the alias will keep working silently while the
  canonical path is the one the repo itself now links (`packages/coding-agent/README.md`:
  `git clone https://github.com/earendil-works/pi`).
- Inside the staged package the URL occurs twice: row `SOURCES.append.md:67` and the citing entry
  line 5 — no staged duplicate. In the lane, `grep -rn "pi-mono\|badlogic\|pi coding agent"` over
  `*.md`/`*.json`/`*.py` outside the round-70/72 wave dirs returns nothing: no lane duplicate.

## 7. Defects handed to the L1 (not mine to fix)

1. **Alias pin.** A row pinned at `badlogic/pi-mono` pins a repo name that GitHub already 301s.
   Recommend the canonical `earendil-works/pi` path plus the blob sha `19d2bf28…`, and the alias
   named in the anchor cell so a future re-fetch does not read the move as content drift.
2. **`S268` cross-reference in the entry.** The entry's § *Four vendors* bullet 3 says
   "Anthropic's own Japanese page, from round 6's S268". The lane's registry has 139 rows and its
   highest id is `S213` (`grep -o "^| S[0-9]*" corpus/SOURCES.md | sort -u | tail -3` → `S211`,
   `S212`, `S213`); there is no lane `S268`, and `grep -n "S268" corpus/SOURCES.md
   corpus/knowledge/*.md` returns nothing. `S268` in the staged package is
   `SOURCES.append.md:72` = Claude Platform 日本語 Agent Skills — the right *referent*, the wrong
   *namespace*: "round 6" is not where that id came from, and after the append the lane id will be
   different again. The entry text dangles as written; it should name the URL, not a round-scoped id.
3. **"MCP-style" and "not in `AGENTS.md`"** as in § 4.2 and § 4.3 — the A4 entry should quote the
   page's own words (`prompt template` / `executable integration point` / system-prompt index) and
   take the always-on clause from S262.

## 8. What the page gives the A4 rule (token set `prompt`, `always-on`, `skill`, `index`)

- `prompt` — line 5, verbatim "a prompt template".
- `skill` — lines 1, 3, 5, verbatim.
- `index` — the mechanism is stated at line 43 even though the word is absent (`grep -c index` = 0):
  `Pi scans configured skill locations and adds each skill’s name, description, and path to the system prompt.`
  (17 words, one occurrence; note U+2019 in `skill’s`, line 43 is the only one of the quoted lines
  with a non-ASCII byte).
- `always-on` — not on this page (0 occurrences of `AGENTS.md`, 0 of `always-on`).

Additional verbatim material on the page that neither the row nor the entry cites, offered so the
L1 does not have to re-open the source (all word-bounded, one occurrence each, line numbers from
the snapshot):

| line | words | sentence |
|---|---|---|
| 45 | 11 | `This keeps detailed guidance out of context until it is needed.` |
| 45 | 18 | `A model might fail to load a relevant skill, so use `/skill:name` when you need to force it.` |
| 65 | 11 | `Review unfamiliar skills and their supporting files before granting project trust.` |
| 85 | 11 | `Name collisions keep the first discovered skill and produce a warning.` |
| 83 | 14 | `Pi neither requires nor warns when the declared name differs from the parent directory.` |

The last two are a *third* collision-resolution shape next to the lane's existing A1 sources
(Junie: project beats user; Roo: native root beats shared root): pi keeps the **first discovered**
and warns. If the L1 wants a fifth A1 witness, it is here and costs one row, not a re-fetch.

## 9. Integration constraints observed in the live tree (read-only, for the C1 landing)

- `wc -l -c SKILL.md` → `600 72688`: at the ceiling; a new box must free lines first (plan says so;
  re-measured here).
- `verifiers/checklist-baseline.json`: `box_total 41`, sections `['Agent-definition fidelity
  checklist', 'Always-on constraint-file checklist (AGENTS.md-class)', 'Dispatch-prompt fidelity
  checklist', 'Trigger-fidelity checklist']`, trigger-section boxes `15`, dispositions `{'executed':
  8, 'delegated': 4, 'unexecuted': 29}`. The file pins each box by normalized-text sha256, so the
  four A4 boxes need new `box_id`s + hashes + `box_total` in the same change.
- `verifiers/check_assertion_floors.py` reads `checklist observed=1862 floor=1862` at the base
  (plan table); the floors registry carries a BUMP-IN-STEP RULE for exactly this case.

## 10. Risks and blockers

- No blocker. The source is reachable, current, and pinnable; every quoted sentence is located.
- Risk if the entry lands as drafted: a lane reader would believe pi names MCP and `AGENTS.md`.
  Both are 0-occurrence in the snapshot; the fix is wording in the entry, not a new fetch.
- Risk if the row lands on the `badlogic/pi-mono` URL without the alias note: a future re-fetch
  after GitHub retires the alias would read as `source-unreachable` and be mis-filed as drift.
- Tooling: nothing installed or upgraded this seat (no `pacman`, no `uv`, no `npx`). Commands used:
  `curl`, `sha256sum`, `cmp`, `sed`, `grep`, `awk`, `python3` — all pre-existing on the host.
- Process: no long-running command; every call finished in ≤2 s wall, no background jobs, no PIDs
  left. Scratch `/tmp/k72w1-ExecSrcPi.3CA8` removed.
