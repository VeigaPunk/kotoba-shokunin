# ExecSrcKimiEn — C1 source opening: Kimi Code CLI (staged S218)

**Verdict.** The page is open, real, markdown, and proves what the staged entry credits it with at
the heading level — but the staged entry's Moonshot row conflates **two official pages that document
different vendor root names and different root lists**, and one of the two anchors it cites for this
page does not exist as a heading. `# Skill discovery` exists (`## Skill discovery`, snapshot:20);
`# Description resolution` does **not** — the page has `**Description resolution**` as a bold
paragraph at snapshot:106, and `grep -n '^#'` lists no such heading. Six of the row's backticked
tokens are ABSENT from this page (they live at S219). Nothing here is fabricated; the defect is
attribution, and it is the same class as the S001 → S018 repair the lane already recorded.

Seat: read-only; no committed lane file touched; no fixture repo, no git write, no lane gate run.
Tooling: nothing installed. Scratch: none — every artifact is under
`.ufo/waves/round-73/w1/build/ExecSrcKimiEn/` (deliverable drafts), no `/tmp` directory left behind.

## 1. Opened, with identity (not a JS shell)

```
$ curl -sL --max-time 60 -A 'Mozilla/5.0' -o raw_skills.md \
    'https://raw.githubusercontent.com/MoonshotAI/kimi-cli/main/docs/en/customization/skills.md'
HTTP=200 BYTES=13528 URL=https://raw.githubusercontent.com/MoonshotAI/kimi-cli/main/docs/en/customization/skills.md
$ sha256sum snapshot.md
5a18c3384e8e91be4cb99570a83b62a046aeddb434d6bed403bab72592b43c52  snapshot.md
$ curl -sIL ... | grep -iE '^HTTP/|^content-type|^content-length'
HTTP/2 200
content-type: text/plain; charset=utf-8
content-length: 13528
```

- No redirect (`URL=` equals the requested URL); the staged URL
  `https://github.com/moonshotai/kimi-cli/blob/main/docs/en/customization/skills.md` is the GitHub
  blob route and answers HTTP 200 with 318,606 B of page shell; the file bytes come from the raw
  route above, which is the same repository file.
- Identity of the fetched bytes against the repository file, not just against the URL:
  `GET https://api.github.com/repos/MoonshotAI/kimi-cli/contents/docs/en/customization/skills.md?ref=main`
  → `200`, `size 13528`, git blob sha `7ddb7d3cb7012787b9586af150124a920a673c46`. Decoding the API
  `content` (base64) is byte-identical to the raw fetch (`identical: True`), and the git blob sha
  recomputed over the fetched bytes equals the API sha. Main tip at access:
  `git ls-remote https://github.com/MoonshotAI/kimi-cli main` → `9ab1286b8fe4e6bcd116949a27ce5e0ac3389c82`.
- Access date `date -I` → `2026-10-25`.
- Not a JS shell: the served bytes are markdown — headings, tables and fenced toml / yaml / sh blocks.
  No secondary source needed.

**Snapshot artifacts (handoff for the L1's manifest — I did not write into `snapshots/`):**

| path | bytes | sha256 |
|---|---|---|
| `.ufo/waves/round-73/w1/build/ExecSrcKimiEn/snapshot.md` (343 lines, whitespace-preserved, identical to the fetch) | 13 528 | `5a18c3384e8e91be4cb99570a83b62a046aeddb434d6bed403bab72592b43c52` |
| `.ufo/waves/round-73/w1/build/ExecSrcKimiEn/snapshot.sha256` | — | the line `5a18c338…  snapshot.md` |

Ready manifest line for `.ufo/waves/round-73/snapshots/MANIFEST.sha256` (L1 to place the file and the
line): `5a18c3384e8e91be4cb99570a83b62a046aeddb434d6bed403bab72592b43c52  sn218-kimi-cli-skills.md`

## 2. What this page actually holds (the ground for a row)

All refs are `snapshot.md` line numbers (`sed -n '<L>p'`).

- **Scope ladder**, snapshot:22 and :24 — "Roots are scanned in priority order … the more specific scope
  wins" / `**Project > User > Extra > Built-in**`.
- **User roots, two mutually exclusive groups**, snapshot:34-41 — brand `~/.kimi/skills/`,
  `~/.claude/skills/`, `~/.codex/skills/`; generic `~/.config/agents/skills/` (recommended),
  `~/.agents/skills/`.
- **Project roots**, snapshot:62-65 — brand `.kimi/skills/`, `.claude/skills/`, `.codex/skills/`;
  generic `.agents/skills/`. Project root = nearest `.git` ancestor (:57-59).
- **Merge behaviour**, snapshot:44 — all existing brand directories load and merge by default, tie
  order `kimi > claude > codex`, controlled by `merge_all_available_skills` default `true` (:44, :48,
  :54), and it applies to project level too (:67).
- **Extra additive roots**, snapshot:70-90 — `--skills-dir` (:69-72) and `extra_skill_dirs` (:77-88).
- **Flat `.md` skills**, snapshot:93-104 — a bare `.md` is a skill, `name` defaults to the filename
  (:95); subdirectory wins a same-name collision (:104).
- **Description resolution chain**, snapshot:106-112 — frontmatter `description:` → first non-empty
  body line truncated at 240 characters → `"No description provided."`.
- **`type: flow`**, snapshot:272-282 — flow skills set `type: flow` and carry a Mermaid/D2 diagram,
  invoked by `/flow:<name>` (:330-341).
- **Env note**, snapshot:115 — `KIMI_SHARE_DIR` "does not affect Skills search paths".

## 3. The staged entry's tokens, tested against this page

Source of the claims: `/home/vgpnk/Projects/shokuknow/merge/kotoba/knowledge/corpus/knowledge/chinese-client-skill-surfaces.md`
`:7` (the S218 source line) and `:23` (the Moonshot row, cited jointly `(S218, S219)`).
Counts are `grep -c -F -- <token> snapshot.md`; `wb` is a word-bounded recount; the last column is the
same token counted in the **S219 probe** I fetched today (§5) and is evidence of *where* the absent
tokens live, not a claim about S218.

| token (as the entry writes it) | grep -c -F on S218 | S218 lines | S218 wb | S219 text count |
|---|---|---|---|---|
| `# Skill discovery` → `Skill discovery` | 1 | 20 | 1 | 0 |
| `# Description resolution` → `Description resolution` | 1 (bold paragraph, **not** a heading) | 106 | 1 | 0 |
| `.kimi-code/skills/` | **0** | — | 0 | 3 |
| `.agents/skills/` | 2 | 40, 65 | 2 | 3 |
| `$KIMI_CODE_HOME/skills/` | **0** | — | 0 | 2 |
| `~/.kimi-code/skills/` | **0** | — | 0 | 2 |
| `~/.agents/skills/` | 1 | 40 | 1 | 2 |
| `name` | 22 | 7, 22, 42, 44, 95, 99, 100, 104, 151, … | 21 | 12 |
| `description` | 12 | 7, 108, 110, 112, 152, 171, 189, 213, 235, 242, 260, 281 | 13 | 5 |
| `type` | 8 (only `:276`/`:282` are the frontmatter field) | 115, 220, 226, 242, 244, 272, 276, 282 | 7 | 4 |
| `prompt` (as a `type` value) | 8 for the word; **0** for `type: prompt` | 7, 87, 91, 147, 254, 262, 303, 335 — all prose, none a `type` value | 9 | 4 |
| `inline` (as a `type` value) | **0** | — | 0 | 1 |
| `flow` | 15 | 3, 15, 192, 259, 272, 274, 276, 281, 282, 286, 330, … (`type: flow` at 282) | 14 | 2 |
| `whenToUse` | **0** | — | 0 | 4 |
| `disableModelInvocation` | **0** | — | 0 | 3 |
| `arguments` | **0** (also `argument` 0, `disable` 0, `invocation` 0) | — | 0 | 5 |

**What the page does NOT say, and the entry claims (ABSENT list):**

1. `.kimi-code/skills/` as a project root — ABSENT. The page's project brand root is `.kimi/skills/` (:62).
2. `$KIMI_CODE_HOME/skills/` and `~/.kimi-code/skills/` as user roots — ABSENT (`KIMI_CODE_HOME` 0
   occurrences in the whole file). The page's user brand root is `~/.kimi/skills/` (:35).
3. The frontmatter keys `whenToUse`, `disableModelInvocation`, `arguments` — ABSENT (0 each).
4. `type: prompt` and `type: inline` — ABSENT; this page states `type: flow` only (:276, :282). The
   entry's `type` (`prompt`/`inline`/`flow`) triad is true of S219, not of S218.
5. The `.claude/skills/`, `.codex/skills/` brand roots and the `merge_all_available_skills` flag are,
   conversely, things **this** page says and S219 does not — the row's joint citation hides both
   directions (S219 counts: `merge_all_available_skills` 0, `.claude/skills` 0, `.codex/skills` 0).

## 4. The anchor defect (same class as S001 → S018)

```
$ grep -n '^#' snapshot.md
1:# Agent Skills
5:## What are Agent Skills
20:## Skill discovery
47:# Default; merges every brand directory that exists.      <- inside a toml fence, not a heading
118:## Built-in skills
125:## Creating a skill
155:## Code Style
182:## Example skills
192:## PPT Creation Workflow
200:## Design Principles
216:## Python Development Standards
238:## Git Commit Conventions
252:## Using slash commands to load a skill
270:## Flow skills
338:# Execute the flow                                        <- inside a sh fence, not a heading
341:# Load as a standard skill                                <- inside a sh fence, not a heading
$ sed -n '106p' snapshot.md
**Description resolution**
```

The entry's `:7` writes `# Description resolution` as if it were a heading of this page; the page's
heading list has no such line, and its depth-2 headings are `##`. The lane already treats a
non-existent heading in a row's anchor as a defect: `corpus/SOURCES.md:31` S018 supersedes S001 because
"the page has no \"Skill metadata table\" heading, so S001's anchor named a heading that does not
exist". The wave-1 repair is to write the S218 anchor as `## Skill discovery` (snapshot:20) and
`**Description resolution**` (bold paragraph, snapshot:106) — the level is part of the anchor, not
decoration.

## 5. Cross-page divergence (the finding this seat adds to C1)

I fetched S219 as a **probe only** (the staged entry's own second Moonshot source, not my assigned
page), so the split claim in §3 is grounded and not inferred:

```
$ curl -sL --max-time 60 -A 'Mozilla/5.0' -o s219.html \
    'https://www.kimi.com/code/docs/kimi-code-cli/customization/skills.html'
S219 HTTP=200 bytes=79788 type=text/html
sha256 e3b314dcff628fc2f88fe6b679e7d6096a209725451957b8ca35360fb5f20989
```

Text-extracted (tags deleted, whitespace collapsed → `s219-snapshot.txt`, 4 330 B; this is the
documented shaping, so quotes from it are quote-equal, not byte-exact). The two official pages agree
on the ladder (`Project > User > Extra > Built-in`, S219 1×) and on `extra_skill_dirs` (S219 2×) and
**disagree on the root set**:

| question | S218 (GitHub, en) | S219 (kimi.com, zh) |
|---|---|---|
| user vendor root | `~/.kimi/skills/` (:35) | `$KIMI_CODE_HOME/skills/`, default `~/.kimi-code/skills/` |
| project vendor root | `.kimi/skills/` (:62) | `.kimi-code/skills/` |
| claude / codex roots | `~/.claude/skills/`, `~/.codex/skills/`, `.claude/skills/`, `.codex/skills/` | none (0 each) |
| merge flag | `merge_all_available_skills`, default `true` (:44) | not mentioned (0) |
| env var named | `KIMI_SHARE_DIR`, "does not affect Skills search paths" (:115) | `KIMI_CODE_HOME`, moves the Kimi-only skills dir |
| extra roots | `--skills-dir`, `extra_skill_dirs` | `extra_skill_dirs` |

Neither page mentions the other's environment variable, so this is not a literal contradiction on one
variable; it is two vendor surfaces describing different vendor-root names and different root lists
for the same client. Host observation (not a vendor claim, and not part of any predicate):

```
$ ls -d ~/.kimi ~/.kimi-code ~/.agents/skills ~/.config/agents/skills ~/.claude/skills ~/.codex/skills
ls: cannot access '/home/vgpnk/.kimi': No such file or directory
ls: cannot access '/home/vgpnk/.config/agents/skills': No such file or directory
/home/vgpnk/.agents/skills
/home/vgpnk/.claude/skills
/home/vgpnk/.codex/skills
/home/vgpnk/.kimi-code
```

This host has `~/.kimi-code` (S219's name) and no `~/.kimi` (S218's name); the lane already holds
`~/.kimi-code/config.toml` as an observed path (`corpus/knowledge/opencode-offer-trace-round8.md:84`,
with `merge_all_available_skills = true`). A row that says "Kimi Code CLI skills live in X" without
naming which page said X is not measurable against a host that follows the other page.

## 6. Does this expand ground the lane already holds?

- `corpus/knowledge/skill-name-precedence-round69.md:52-53`: "A pinned sibling's Kimi-scope rule
  (kumitate `corpus/knowledge/kimi-skills-plugins.md`) is deliberately outside this entry." Kimi's
  name/scope precedence is therefore unheld by the lane's precedence entry — this page holds it
  (`Project > User > Extra > Built-in`, brand group over generic, `kimi > claude > codex`).
- `corpus/knowledge/opencode-offer-trace-round8.md:84` holds `merge_all_available_skills = true` only
  as a host config observation; no lane row attributes the rule to a vendor page.
- `grep -rniE 'kimi|moonshot|merge_all_available_skills|description resolution' corpus SKILL.md
  PROVINCE.md` returns Kimi hits that are all host/transcript evidence (agent-def audit, harness
  router, opencode trace, sibling description rewrites) — **no client-skill-surface row**. Zero
  registry rows naming `github.com/moonshotai/kimi-cli` or `kimi.com/code` (plan § base table, unchanged).
- New to the lane from this page: the **description fallback chain with the 240-character cap**
  (snapshot:108-112) and the **flat `.md` skill form with filename-as-name** (snapshot:93-104).

## 7. Draft registry row (one row, 11 cells, no `|` inside a cell)

```
| S<<id>> | Moonshot — Kimi Code CLI — Agent Skills — https://github.com/moonshotai/kimi-cli/blob/main/docs/en/customization/skills.md | docs | B | Kimi Code CLI's documented skill discovery roots, their scope and merge precedence, the flat-file form, and its description fallback chain (one vendor's own documentation; not a measurement of any local client) | `## Skill discovery` at snapshot:20-22 and the merge paragraph at snapshot:44, `**Description resolution**` at snapshot:106-112 (a bold paragraph, not a heading); quote "By default, **all existing brand directories are loaded and merged**, with same-name skills resolved by priority: kimi > claude > codex." (21 words; the same line's remaining 18 words after `codex.` dropped); fetched 2026-10-25, HTTP 200, 13 528 B, sha256 5a18c338…, git blob 7ddb7d3c… at main 9ab1286b… | Kimi Code CLI merges every existing brand root (`~/.kimi/skills/`, `.claude/skills/`, `.codex/skills/`) by default and breaks a same-name tie kimi > claude > codex ahead of a separate generic group, reads frontmatter `name` and `description` as the identity and routing fields, and falls back for `description` to the body's first non-empty line capped at 240 characters | mined | 2026-10-25 | 90d | corpus/knowledge/chinese-vendor-skill-surfaces-round73.md |
```

```
$ awk -F'|' 'NF!=13{print "BAD NF="NF; exit 1}' row-kimi-s218.md && echo "PARSE OK: 11 cells"
PARSE OK: 11 cells
```

- The quote is byte-exact: `python3` membership test over `snapshot.md` → `present: True words: 21`;
  the dropped bytes are named in the anchor cell (rest of `snapshot.md:44` after `codex.`).
- Tokens carried (predicate (a) shape): roots `~/.kimi/skills/`, `.claude/skills/`, `.codex/skills/`
  (all word-bounded present, snapshot:35-37); keys `name` (wb 21) and `description` (wb 13).
- Tier **B** per item instruction and lane precedent (S215 pi-mono repo docs and S216 hermes docs are
  both a project's own documentation at tier B, `corpus/SOURCES.md:155-156`). If the L1 judges a
  maintainer's own repository file to be a maintainer statement and prefers `A`, that is a one-cell
  change; the frozen predicate (b) accepts A or B. Recorded as a tension, not resolved here:
  this file sits in `MoonshotAI/kimi-cli` itself, i.e. written by the CLI's own maintainers.
- `S<<id>>` stays a placeholder: the lane's ids run to `S216` and `S217`–`S221` are unused
  (`grep -c "| S218 |" corpus/SOURCES.md` → 0), so the L1's by-document renumber is free; the staged
  `S214` is already Factory in this lane (`corpus/SOURCES.md:154`).

## 8. Attacks on the frozen C1 predicate (before any claim data)

1. **(a) is satisfiable by splitting pages.** "each occur word-bounded in the committed page snapshot
   of a source that row cites" lets a row cite two pages and be backed by tokens that no single page
   carries. The staged Moonshot row is exactly that object: `.kimi-code/skills/` is backed only by
   S219, `merge_all_available_skills` only by S218, and the row is green while each page alone refutes
   half of it. Either require a per-source token map in the row (token → source id) that the counter
   can check, or accept the split and require the entry to say which page grounds which token. This is
   a counter defect, not a world defect: it must be settled before data (Q28).
2. **(c)/(d) snapshot unit is unspecified for a page with two routes.** For S218 the blob route is
   318,606 B of HTML and the raw route is 13,528 B of markdown. A located quote of
   "By default, **all existing brand directories are loaded and merged**…" appears in both after
   whitespace collapse (the HTML carries the same code text), so a tamper test that edits the
   markdown snapshot would be caught (sha256) but a *wrong-route* snapshot would still satisfy (d).
   The manifest should pin the raw route and the counter should require it — my snapshot is the raw
   route, byte-identical to the repository blob.
3. **Host truth is outside every clause.** No clause of C1 can fail on the fact that this host has
   `~/.kimi-code` and not `~/.kimi`. The entry must therefore not present S218's root as the root a
   local client reads; if the entry claims a discovery root for Kimi, it needs both pages or an
   explicit "the two vendor pages differ" sentence. Otherwise C1 will be true and misleading.
4. **Vendor distinctness is not required.** (b) constrains hosts per vendor but nothing stops two
   vendor rows citing the same page; with the entry's joint citations that is latent. Recommended
   minimum: each vendor row cites at least one host unique to that vendor's frozen host list (the
   frozen list already achieves this if the counter checks *every* cited row's host, not one of them).

## 9. Risks / blockers

- **Risk (factual, for the entry):** the staged entry's Moonshot cell is correct for S219 and wrong
  for S218 in six tokens. If the L1 appends the row as written with "renumber by document" only, the
  lane inherits a mixed attribution. The fix is in the row's anchor/teaches, not in a new source.
- **Risk (scope):** S218's vendor roots are documentation, not behaviour, and this host contradicts
  S218's root name. Any sentence in `chinese-vendor-skill-surfaces-round73.md` phrased as "Kimi reads
  X" must name the page it read.
- **Blocker:** none. No gate was run (out of this seat's scope), nothing installed, no lane file
  modified, no git or jj write, no process left running.

## 10. Artifacts left in place

Under `.ufo/waves/round-73/w1/build/ExecSrcKimiEn/`:
`snapshot.md` (13 528 B, sha256 `5a18c338…`), `snapshot.sha256`, `raw_skills.md` (identical bytes to
`snapshot.md`; the unmodified fetch), `fetch-log.txt`, `api.json` (GitHub contents API), `row-kimi-s218.md`,
`token-matrix.txt`, and the S219 probe `s219.html` (79 788 B) + `s219-snapshot.txt` (4 330 B, shaping
disclosed in §5). Largest file 79 788 B, under the 300 KB cap.

**Report path:** `.ufo/waves/round-73/w1/ExecSrcKimiEn.md`
