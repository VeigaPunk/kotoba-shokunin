# ScoutAmp — S204 (Amp) re-open, round 69 wave 1

**Question (scoped):** re-open `https://ampcode.com/docs/customize/skills`, verify the S204 row quote
`"Local skills mask repository skills with the same name."` is verbatim in the section *Skill Sources
and Precedence*, capture the full ordered source list, and report heading + access date + FOUND/NOT FOUND.

**Verdict: FOUND — verbatim.** Access date **2026-10-25**. Heading **Skill Sources and Precedence**
(`<h2 id="skill-sources-and-precedence">`, an `h2`). The quote is the **first sentence of the paragraph
immediately after the section's 11-item ordered list**. Byte-exact, one occurrence on the page, **no
inline markup inside the quote**, and **no newline inside the quote** (it sits on one source line), so
the counter's tag-dropping shaping never has to bridge an element boundary for it.

Lane measured: HEAD `a238989a96cb0d2b939679126b832d75b861ca6e` (the plan commit, on base
`a5f7459f99bb27bf697e9438362e75ac5833eca8`); all lane reads were read-only, all execution ran from
`/tmp` copies.

## Evidence

Fetch (2 independent fetches, 2026-10-25):

```
curl -sSL https://ampcode.com/docs/customize/skills
  -> HTTP 200  text/html  102527 bytes  etag: "1ux46kv"  x-sveltekit-page: true
curl -sSL https://ampcode.com/docs/markdown/customize/skills
  -> HTTP 200  text/markdown; charset=utf-8  8357 bytes   (listed by https://ampcode.com/llms.txt line 64)
```

Raw HTML, the list tail + the paragraph (verbatim bytes, tags shown):

```
<li>Official Amp skills</li></ol> <p>Local skills mask repository skills with the same name. A personal skill masks a workspace skill
with the same name, and both mask official Amp skills. Set <code>amp.skills.disableClaudeCodeSkills</code> in …</p>
```

Greps: `"Local skills mask"` → **1** hit (offset 80803 of 102489, inside the section);
`"A personal skill masks a workspace skill"` → 1; `"mask"` → 3 (all three in that one paragraph);
the page contains **no** other skills-precedence statement (`"first skill"` → 1, in the lead-in
sentence). The only `"takes precedence"` on the page is about **MCP servers** ("If a server with the
same name is also supplied by a CLI flag or direct configuration, that source takes precedence"), not
skills — it must not be cited for S204.

Word count of the row's quote: **9** (`Local skills mask repository skills with the same name.`) —
matches the row's `(9 words)`. The row's anchor description "the sentence after the ordered source
list" is accurate; the quote is the first sentence of the following paragraph.

## The full ordered source list (11 items, first wins)

Lead-in, verbatim: **"Amp uses the first skill with a given frontmatter `name`. The order is:"**

| # | source | tier |
|---|---|---|
| 1 | `~/.config/agents/skills/` | local |
| 2 | `~/.agents/skills/` | local |
| 3 | `~/.config/amp/skills/` | local |
| 4 | `.agents/skills/` in the project and searched parent directories | local (project) |
| 5 | `.claude/skills/` in those directories | local (project) |
| 6 | `~/.claude/skills/` | local |
| 7 | `~/.claude/plugins/cache/` | local |
| 8 | Directories in `amp.skills.path`, in the order they are configured | local, config-dependent |
| 9 | Your personal skills repository | repository |
| 10 | Your active workspace skills repository | repository |
| 11 | Official Amp skills | vendor |

Tie-break paragraph, verbatim in full: *"Local skills mask repository skills with the same name. A
personal skill masks a workspace skill with the same name, and both mask official Amp skills."*
(then two opt-outs: `amp.skills.disableClaudeCodeSkills` skips the Claude-compatible locations;
`amp.skills.disableGlobalAgentsSkills` skips items 1–2.)

So the documented tiers are **local directories (1–8) > personal repository (9) > workspace repository
(10) > official Amp skills (11)**.

## Cross-check against the lane (read-only)

- `corpus/SOURCES.md` row S204 has **11 cells**; `[5]` anchor carries the quote; `[6]` rule cell
  "Amp resolves a name collision by a fixed source order in which a local skill masks a repository
  skill of the same name"; `[7] mined`, `[8] 2026-10-25`, `[9] 90d`, `[10]` names
  `corpus/knowledge/skill-name-precedence-round69.md`. ✓
- `corpus/knowledge/skill-name-precedence-round69.md` line 2 carries the same quote in its `source:`
  line and its `| Amp |` table row carries client + rule + the same quote. ✓
- **Counter shaping simulated, not assumed.** I copied `verifiers/check_skill_precedence.py` to
  `/tmp/k69sim/` (lane untouched, `python3 -B`) and ran its own `_page_text` / `_norm` on my saved
  page: `quote in _page_text(html)` → **True**; on the markdown twin → **True**. S204 would count as
  `found` under `--fetch`; the `--fetch` arm is not at risk from this source.

## Depth findings (attack surface for the falsifier seats)

**F1 — the assignment's shorthand is a trap; the page's "workspace" is NOT the project directory.**
`"A personal skill masks a workspace skill"` reads like "personal beats project", and it does **not**.
Item 4 (`.agents/skills/` in the project) is a *local* source ranked **above** the personal repository
(9). Evidence on the same page, § Skill Repositories: *"Workspace admins manage workspace skills, which
are available to everyone in the workspace"* (`amp-skills.md:80–81`), and
`customize/global-plugins-and-skills` renders the same distinction: `Personal | You | Everywhere you
use Amp` vs `Workspace | Everyone in the workspace`. Consequence: **a skill committed in the project's
`.agents/skills/` masks a same-named skill from the user's personal repository.** The entry's and the
row's choice of the *first* sentence ("local masks repository") is therefore the **correct** one; a
critic who "improves" the Amp row to "a personal skill masks a workspace skill" would introduce a false
claim about project skills. If the refinement is added at all, it must be scoped as *within repository
skills*.

**F2 — "fixed" is a mild over-read (wording, not a falsification).** `SOURCES.md` `[6]` says "a fixed
source order" and the entry says "a fixed ordered list". Item 8 is *"in the order they are
configured"* and items 9–10 exist only if those repositories exist, so the order is **documented and
ranked**, not immutable. "documented"/"numbered" would be exact; the current wording is defensible
because the *rank* is fixed. Do not treat this as a counter failure.

**F3 — the HTML page's sha256 is not a stable provenance anchor.** Two fetches on the same day: content
identical, 4 differing lines, all `<script nonce="…">` (102489-byte body, hash
`0a8c58ec9e7ea5544ffa21b6c6831d569f59851db4f0f6981b3d1d97b39f258f` vs
`b322f8b0b41dc0dd90f9fef1da2a21d5dd6e8501b3aac43320f90394e28fb9ee`). The **markdown twin is
byte-stable**: `d63339eccf6e04f6e038926a395b58047f3f4bd32c248cf50219a7390e93c8b8` on two fetches.
If any receipt wants a page digest, pin the twin (`…/docs/markdown/customize/skills`), not the HTML.
The lane's row cites the HTML URL — correct for `--fetch` (quote-in-text passes), just not hashable.

**F4 — `?format=md` is not a markdown channel.** `…/skills?format=md` → **200 text/html, 102527
bytes** (the same HTML). Only `/docs/markdown/<path>` serves `text/markdown`. A receipt claiming a
`format=md` fetch would be wrong.

**F5 — `_row_quote` longest-match matters for S204 and happens to resolve correctly.** The S204 anchor
cell contains **two** double-quoted strings the entry also carries: `"Skill Sources and Precedence"`
(4 words, from the entry's `source:` line) and the 9-word quote. `_row_quote` returns the **longest**
match, so the located quote is the 9-word one — verified by running the function on the real row.
Had it matched the heading instead, `--fetch` would still have passed (the heading is on the page), so
the `--fetch` arm alone does not discriminate this row: rule 5's anchor containment is what carries it.

**F6 — a stronger quote is available if the row wants the refinement.** The second sentence
(`A personal skill masks a workspace skill with the same name, and both mask official Amp skills.`) is
**17 words** (≤25), verbatim on both the HTML page and the markdown twin, so it is admissible under
rule 5/rule 6 — but it would have to be carried in **both** the entry and the row's anchor cell
(rule 5 requires quote ∈ anchor), and (per F1) must be explained as *repository-internal*.

**F7 — no conflicting statement found.** `mask` / `first skill` / `same name` / `precedence` produce no
skills statement on `customize/global-plugins-and-skills` (0 hits). The page's remaining skill-scan
rules are adjacent, not contradictory: recursive search up to five directories below each root;
personal/workspace repositories use a one-level layout; a bundled plugin skill is namespaced
`<plugin-name>:<skill-name>` so it *"does not compete with the bare skill names above"* — that
namespacing sentence is the page's only *uniqueness* mechanism and is **not** cited by S204 (the row
claims precedence only, correctly).

## Bound

Documentary evidence: what Amp's docs state on 2026-10-25, not observed Amp behaviour. One client's
documented rule; the row's `[4]` already disclaims any other client. No band move claimed; depth rests
with the L1's closure.

## Provenance (copy-ready)

```
S204  Amp — Agent Skills   https://ampcode.com/docs/customize/skills        accessed 2026-10-25  HTTP 200 text/html 102527B
      section: "Skill Sources and Precedence" (h2, id=skill-sources-and-precedence)
      located quote: "Local skills mask repository skills with the same name."   (9 words, unshaped, one line)
      twin: https://ampcode.com/docs/markdown/customize/skills  eval "2026-10-25"  HTTP 200 text/markdown 8357B  sha256 d63339ec…
```

## Remaining unknowns

- Whether Amp's runtime order matches the documented order (unobserved; out of bound).
- Whether Amp's other surfaces (Puck, orb) restate the same order — not checked, not claimed.
- Whether two directories inside one `amp.skills.path` entry can tie on a name (the docs give an order
  *between* entries, not within one) — not claimed.
