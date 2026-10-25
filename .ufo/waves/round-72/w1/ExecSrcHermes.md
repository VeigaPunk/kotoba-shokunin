# ExecSrcHermes — source opening, staged row S264 (Hermes Agent skills page)

Wave 1 / build. Read-only on every committed lane file; writes are the two snapshots + pin
manifest under `.ufo/waves/round-72/snapshots/` and this report.

## Verdict

**The source is live and first-party; both staged quotes are verbatim in it; the entry's S264
claims are confirmed, two of them only after naming the shaping.** No fabricated text, no
unreachable source, no paraphrase passed off as a quote.

Four things the L1 needs from this opening:

1. **Confirmed, byte-verbatim after markup strip + line join.** Both quotes in row S264 exist
   word for word in the rendered page *and* in the upstream markdown source. Raw-contiguity
   test: `0` hits in either raw form, `1` hit in each normalized form — the quotes are split by
   hard line wraps and, in Q1, by an `<a>` tag / `[…](…)` link.
2. **C1(d) will fail on S264 as written** unless the counter normalizes markup and newlines, or
   the snapshot is a normalized text export. The quote is *not* a contiguous byte string in the
   committed `.md` or `.html` snapshot (evidence §4).
3. **The 60-char rule has exactly one home on the page.** The `#skillmd-format` section the
   phrase links to states no description-length limit; `60-char` occurs once in the whole page
   (md:123). So an A4/author-facing rule sourced to this page must quote the `/learn` sentence,
   not the format section.
4. **The page states the resident-index rung itself** (md:610-612) — memory holds what should
   "always be in context", skills load "only when relevant" — plus a non-duplication rule
   against the always-loaded `AGENTS.md` (md:636-637) and two quantified budgets (md:641-642).
   The staged entry uses Hermes only for the house standard, so this is new ground for
   `resident-index-and-rungs-round72.md` (A4), not a re-quote of the staged row.

---

## 1. Fetch record

Command (scratch `S=$(mktemp -d /tmp/k72w1-ExecSrcHermes.XXXX)`; scratch deleted before return):

```
curl -sS -A 'Mozilla/5.0' -D hdr.txt -L -o page.html -w 'HTTP=%{http_code} FINAL=%{url_effective} SIZE=%{size_download} CT=%{content_type}\n' \
  'https://hermes-agent.nousresearch.com/docs/user-guide/features/skills'
```

Observed:

```
HTTP=200 FINAL=https://hermes-agent.nousresearch.com/docs/user-guide/features/skills SIZE=206631 CT=text/html; charset=utf-8
sha256: c9afb74f898c2baf177b543aaf102707b7590a7db399e9b785baac18e08c53cd
-rw-r--r-- 1 vgpnk vgpnk 206631 Oct 25 18:36 page.html
2026-10-25T21:36:48Z
```

Headers of record (from `hdr.txt`): `date: Sun, 25 Oct 2026 21:36:48 GMT`,
`last-modified: Sun, 25 Oct 2026 20:30:00 GMT`, `server: Vercel`, `x-vercel-cache: MISS`,
`content-type: text/html; charset=utf-8`. Canonical link in the body:
`rel="canonical" href="https://hermes-agent.nousresearch.com/docs/user-guide/features/skills"`.

Access date: **2026-10-25** (UTC). HTTP 200, no redirect (`FINAL` == requested URL).

Upstream markdown source (found by probing; see §4):

```
curl -sS -A 'Mozilla/5.0' -L -o skills.md -w 'HTTP=%{http_code} ...' \
  'https://raw.githubusercontent.com/NousResearch/hermes-agent/main/website/docs/user-guide/features/skills.md'
HTTP=200 FINAL=...skills.md SIZE=58145 CT=text/plain; charset=utf-8
sha256: fb06e67d35c7aa6b11fd4587395cd3665ee9245d499416fe7928b5fa4c8772f5
1118 lines, 58145 bytes
```

Cross-source check for the entry's "1024" (not on the Hermes page; `grep -c 1024 skills.md` → `0`):

```
curl -sS -A 'Mozilla/5.0' -L -o spec.md 'https://agentskills.io/specification.md'
SPEC HTTP=200 SIZE=7608   sha256 9a67de89132948b2300b8dc87b93817971d47f9be89b644444965881a8dfde16
$ grep -n "1024" spec.md
31:| `description` | Yes | Max 1024 characters. Non-empty. Describes what the skill does and when to use it. |
101:* Must be 1-1024 characters
```

## 2. Snapshots written (the only committed-file-shaped writes outside this report)

Following the in-round convention already set by `S262` (`<ID>-<short-name>.html`,
`<ID>-<short-name>.md`, `<ID>.sha256`):

```
.ufo/waves/round-72/snapshots/S264-hermes-skills.html   206631 B  c9afb74f898c2baf177b543aaf102707b7590a7db399e9b785baac18e08c53cd
.ufo/waves/round-72/snapshots/S264-hermes-skills.md      58145 B  fb06e67d35c7aa6b11fd4587395cd3665ee9245d499416fe7928b5fa4c8772f5
.ufo/waves/round-72/snapshots/S264.sha256                 178 B  (the two lines above, in `sha256sum` format)
```

`cp` + `sha256sum` from the scratch fetch; the pinned values equal the fetched-byte values.

## 3. Located quotes, row S264

Row cell (`SOURCES.append.md:68`), split by `awk -F'|'`:

```
3:[ Hermes Agent Docs — Skills — https://hermes-agent.nousresearch.com/docs/user-guide/features/skills ]
5:[ B ]
7:[ the "Learning a skill from sources" section; quote "house authoring standards (≤60-char description, the standard secti…]
8:[ a **house authoring standard** with a concrete description-length limit of sixty characters — against the specification…]
9:[ mined ]  10:[ 2026-10-23 ]  11:[ 90d — re-fetch and confirm the sixty-character description limit and the house-standard clauses are unchanged (ran 2026-10-23) ]
12:[ corpus/knowledge/skill-vs-always-on-boundary.md ]
```

Section heading: `## Learning a skill from sources (`/learn`)` — md:117; rendered
`<h2 … id="learning-a-skill-from-sources-learn">` at html:68. Section body spans md:117-171
(next `## ` is md:172 `## Progressive Disclosure`). "Learning a skill from sources" occurs twice
in the HTML (heading + sidebar nav); the heading hit is html:68.

### Q1 — `house authoring standards (≤60-char description, the standard section order, Hermes-tool framing, no invented commands)`

**Located: yes.** 14 words. Section: *Learning a skill from sources (`/learn`)*.

Snapshot `.md`, lines 123-125 (pasted from `sed -n '<L>p' S264-hermes-skills.md`):

```
== md 123 ==
that follows the [house authoring standards](#skillmd-format) (≤60-char
== md 124 ==
description, the standard section order, Hermes-tool framing, no invented
== md 125 ==
commands).
```

Dropped bytes: the markdown link wrapper `[` before `house` and `](#skillmd-format)` after
`standards`; the two hard newlines at the end of 123 and 124; the leading `that follows the `
on 123 and the trailing `).` on 125 are outside the quote. Nothing else.

Snapshot `.html`, lines 73-75 (pasted from `sed -n '<L>p' S264-hermes-skills.html`):

```
== html 73 ==
that follows the <a href="#skillmd-format" class="">house authoring standards</a> (≤60-char
== html 74 ==
description, the standard section order, Hermes-tool framing, no invented
== html 75 ==
commands).</p>
```

Dropped bytes: `<a href="#skillmd-format" class="">`, `</a>`, `</p>`, the leading `that follows the `,
the two newlines, trailing `).`. Characters `≤` (U+2264) and `-` are literal in both forms.

### Q2 — `/learn is the fast way to turn something you already know — or a pile of reference material — into a reusable skill, without hand-writing the SKILL.md`

**Located: yes.** 25 words. Same section heading.

Snapshot `.md`, lines 119-121 (pasted from `sed -n '<L>p' S264-hermes-skills.md`):

```
== md 119 ==
`/learn` is the fast way to turn something you already know — or a pile of
== md 120 ==
reference material — into a reusable skill, without hand-writing the
== md 121 ==
`SKILL.md`. It is open-ended: point it at *anything you can describe* and the
```

Dropped bytes: the four backticks around `/learn` and `SKILL.md`; the two newlines; on 121 the
tail after the quote `\`. It is open-ended: point it at *anything you can describe* and the`
(kept out because the quote ends at `SKILL.md`). The em dashes are U+2014 in both forms.

Snapshot `.html`, lines 69-71 (`<p><code>/learn</code> is the fast way…` at html:69;
`reference material — into a reusable skill, without hand-writing the` at html:70;
`<code>SKILL.md</code>. It is open-ended: …` at html:71).

Dropped bytes in HTML: `<p>`, `<code>`, `</code>`, the two newlines, and the same 121 tail.

**Both quotes are ≤25 words; neither is a paraphrase.** Q1 is 14 words, Q2 is 25 words.

## 4. Which form the quote lives in — rendered page vs `.md`

The markdown/raw export **exists** and was fetched (§1). Probes that established the form:

```
https://hermes-agent.nousresearch.com/llms.txt                    -> 200 2934   text/plain
https://hermes-agent.nousresearch.com/docs/user-guide/features/skills.md      -> 404 9379
https://hermes-agent.nousresearch.com/docs/user-guide/features/skills.md.txt  -> 404 9379
https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/index.md -> 404 9379
https://raw.githubusercontent.com/NousResearch/hermes-agent/main/website/docs/user-guide/features/skills.md -> 200 58145
https://hermes-agent.nousresearch.com/llms-full.txt               -> 200 5930392 (sha256 de56c21d…)
```

So the site publishes no per-page `.md`; the authoritative text form is the upstream repo file,
and the site's own `llms.txt` names both `llms-full.txt` (whole docs concatenated) and
`/docs/llms.txt`. In `llms-full.txt` the sentence sits at line 12177 with the same link markup
and the same wrap — i.e. **the `.md` form is the source of the rendered text and they agree**.

Raw-contiguity test (quote Q1, `grep -c -F` then a strip-and-join pass):

```
raw md hits: 0
raw html hits: 0
skills.md normalized hits: 1
page.html normalized hits: 1
RENDERED: 'house authoring standards (≤60-char description, the standard section order, Hermes-tool framing, no invented commands). # A local SDK or doc directory — read w'
```

Q2 the same: `Q2 raw md: 0`, `skills.md normalized hits: 1`, `page.html normalized hits: 1`.

Normalization used: strip `<…>` tags, unwrap `[text](url)` → `text`, unwrap `` `code` `` →
`code`, collapse whitespace runs to one space. **No word was altered.** The quote lives in the
*rendered text* of both forms, not as a contiguous byte run in either.

## 5. Verdicts per claim in `corpus/knowledge/skill-vs-always-on-boundary.md`

The entry cites S264 in one `source:` line (`…:6`) and makes five statements resting on it.

| # | entry claim | verdict | page evidence |
|---|---|---|---|
| 1 | `/learn` "synthesises a skill from arbitrary sources and then holds it to its 'house authoring standards (≤60-char description, the standard section order, Hermes-tool framing, no invented commands)'" | **confirmed** (quote verbatim after shaping, §3) | md:119-125 — "point it at *anything you can describe* and the agent gathers the material with the tools it already has, then authors a skill that follows the house authoring standards (…)" |
| 2 | "A sixty-character description limit against the specification's 1024" | **confirmed** | page md:123 `(≤60-char description, …)`; the 1024 is *not* on this page (`grep -c 1024 skills.md` → `0`) and is confirmed separately against `agentskills.io/specification.md:31` ("Max 1024 characters") |
| 3 | "the clause 'no invented commands' is a safety clause … the generated skill must not name commands the agent cannot run" | **confirmed-after-shaping** | clause present verbatim (md:124); the gloss "must not name commands the agent cannot run" and the comparison "other clients do not state" are the lane's reading, not page text — the page states the clause and explains it nowhere |
| 4 | "the standard section order" | **confirmed-after-shaping** | the phrase is verbatim (md:124); the concrete order is only *shown*, in the format template at md:215-228 — `# Skill Title`, `## When to Use`, `## Procedure`, `## Pitfalls`, `## Verification`. No sentence states an order or that it is mandatory |
| 5 | "Hermes-tool framing" | **confirmed** as page text, **referent undefined on the page** | `grep -n "framing" skills.md` → only md:124; the page never defines what tool framing it means |

**Absent: none. Unreachable: none.** No staged S264 quote is missing from the page, and no entry
claim fails.

Two supporting checks for #2 and for the page's own authority:
- the linked anchor `#skillmd-format` resolves to `## SKILL.md Format` (md:194) and that section
  states **no** description length: `sed -n '194,250p' skills.md | grep -i description` returns
  only `description: Brief description of what this skill does` (the template line) and
  `description: "What this controls"` (a config key). The 60-char rule's only textual home is
  the `/learn` sentence.
- the row's `teaches` cell adds "including a rule that the skill must not invent commands" —
  same shaping as #3.

## 6. Row cell audit (what C1(b) needs)

- 11 content cells: id, source, kind `docs`, tier `B`, scope, anchor, teaches, status `mined`,
  opened `2026-10-23`, recheck `90d — …(ran 2026-10-23)`, used-by
  `corpus/knowledge/skill-vs-always-on-boundary.md`.
- `used-by` names the citing entry path exactly → the (b) conjunct's `used-by` half holds for
  this row as staged.
- `recheck` cell records the run date in parentheses, so a 90-day window from 2026-10-23 stands
  to 2027-01-21.
- The `opened 2026-10-23` date is *not* evidence about this lane (addendum §10) — the page was
  opened here on 2026-10-25 and is unchanged since 2026-10-21 (§9).

## 7. Duplicate detection for the L1

- URL **host + path**: `hermes-agent.nousresearch.com` + `/docs/user-guide/features/skills`.
- Second URL the page's own docs index exposes for the same content:
  `hermes-agent.nousresearch.com/docs/llms-full.txt` (whole-site concatenation; not a row).
- Upstream text form: `raw.githubusercontent.com/NousResearch/hermes-agent` +
  `/main/website/docs/user-guide/features/skills.md`.
- Lane duplicate check: `grep -rn -i "hermes" corpus/ --include=*.md` → **0 hits**;
  `grep -n -i "hermes" SKILL.md` → **0 hits**; `grep -n "^| S264 " corpus/SOURCES.md` → **0
  hits**. The lane holds no Hermes row and no Hermes text anywhere. Staged-id check:
  `.ufo/waves/round-72/assimilation/staged-ids:62:S264`; the `collisions` file lists
  `S203`–`S213` and does **not** list S264, so this id collides with nothing already registered.

## 8. Depth the staged row did not use (candidate material for A4 / `resident-index-and-rungs-round72.md`)

The page states the resident-index rung in its own words, in a section the staged row never
quotes. All four are in the same snapshot, `S264-hermes-skills.md`, same file the L1 will pin.

**(a) The rung, stated as a memory-vs-skill split** — md:610-612, section
`## Agent-Managed Skills (skill_manage tool)` (md:606):

```
== md 610 ==
Skills and memory work together in the self-improvement loop: memory stores
== md 611 ==
small durable facts that should always be in context, while skills store longer
== md 612 ==
procedures that should load only when relevant. The background review can
```

Quote (22 words, dropped: the leading `Skills and memory work together in the self-improvement loop: `
on 610 and the trailing `. The background review can` on 612):
"memory stores small durable facts that should always be in context, while skills store longer
procedures that should load only when relevant". HTML: html:271-272. This is the rung the plan's
A4 needs — resident facts always in context, procedures on demand — and the lane's corpus holds
no Hermes text at all, so it is expansion, not re-quote.

**(b) A non-duplication rule against the always-loaded file** — md:636-637, section
`### What a skill entry looks like` (md:625):

```
== md 636 ==
extended in place rather than accumulated one file per session. Skills also do not
== md 637 ==
restate what is already loaded every turn (the repo's `AGENTS.md`, tool schemas).
```

Quote (16 words, dropped: the leading `extended in place … one file per session. ` and the
backticks around `AGENTS.md`): "Skills also do not restate what is already loaded every turn
(the repo's `AGENTS.md`, tool schemas)". HTML: html:294 (`&#x27;` entity for the apostrophe).
This is a *craft* rule for the rung: the on-demand layer must not duplicate the always-on layer.

**(c) The within-skill version of the same rung** — md:634-635:

```
== md 634 ==
without the story behind it. Always-on rules live in `SKILL.md` itself; `references/`
== md 635 ==
holds a small set of files named by topic (a decision table, a recipe, provider quirks),
```

Quote (16 words, dropped: `without the story behind it. ` and the backticks):
"Always-on rules live in `SKILL.md` itself; `references/` holds a small set of files named by
topic". Useful for A4's "index" token: inside a skill, the body is resident and `references/`
is the index-addressed on-demand tier.

**(d) Two quantified authoring budgets, enforced only as warnings** — md:641-644:

```
== md 641 ==
`incident-log-shape` (a body dense in PR/issue numbers), `references-sprawl` (more
== md 642 ==
than 60 reference files), and `oversized-body` (a `SKILL.md` body past ~24k chars — `skill_view`
== md 643 ==
loads the whole file and it stays in context for the rest of the session). They warn; they never
== md 644 ==
block a write.
```

Quote (≤25 words, dropped: the leading `` `incident-log-shape` (a body dense in PR/issue numbers), `` and
the trailing `— skill_view loads the whole file …`): "`references-sprawl` (more than 60 reference
files), and `oversized-body` (a `SKILL.md` body past ~24k chars". Two numeric budgets an author
can act on, from a vendor that ships them as linter rules.

Also worth one line in the lesson: **"lessons, not logs"** (md:631) with the exclusion list
"Incident narration, PR or issue numbers, dates, and quoted chat are not skill content" (md:632-633)
— a house rule the lane has stated from Anthropic but not from this vendor.

## 9. Freshness (the page did not drift between the staged open and this opening)

```
$ curl -s ... 'https://api.github.com/repos/NousResearch/hermes-agent/commits?path=website/docs/user-guide/features/skills.md&per_page=5'
HTTP=200 SIZE=21572
d7db4d109dd5 2026-10-21T15:14:32Z refactor: OpenClaw migration leaves core too; first-time setup offers the agent-…
097fcaa1deec 2026-10-09T22:59:27Z fix(skills): every turn announces skill changes once, on every surface
18ee4251d8e7 2026-10-09T09:39:43Z fix(skills): hub installs download skill files from raw.githubusercontent.com, n…
8e543411524b 2026-10-03T19:57:33Z docs(skills): state one precedence for duplicate skill names
83097ba0082e 2026-10-02T07:12:14Z fix(desktop): keep the hermes://skill/install deep link through the catalog reve…
```

Newest commit touching the file is **2026-10-21**, two days *before* the staged row's `opened`
date (2026-10-23) and four days before this opening. The rendered page's
`last-modified: 2026-10-25 20:30:00 GMT` is a **build/deploy** timestamp, not a content change —
the deployed text and the `main` file agree word for word on both quotes (§4). So the staged
quotes were accurate when opened and are accurate now; the recheck clock can start from
2026-10-25 without a re-quote.

## 10. Consequence for C1(d), stated for the counter author

C1(d) requires the A4 quote to be "found word-bounded in a committed, sha256-pinned snapshot".
For S264 that fails on the raw bytes:

- `grep -c -F "<Q1>" S264-hermes-skills.md` → `0`; the same on `.html` → `0`; normalized → `1`.
- Cause: markdown link syntax `[house authoring standards](#skillmd-format)` / `<a href=…>`
  and hard newlines inside the sentence at md:123-124 and md:119-121.

Two honest fixes, either acceptable, both to be frozen *before* data:

1. the counter normalizes the snapshot (strip tags, unwrap links/backticks, collapse whitespace)
   before the word-bounded search; or
2. the snapshot set gains a normalized text form (e.g. `S264-hermes-skills.txt`) whose sha256 is
   pinned alongside the two raw forms, and (d) searches that.

Option 1 is cheaper and keeps the snapshot set honest raw bytes. Whichever is chosen, the A4
entry's cited quote cell must stay the 14-word Q1 (the phrase as the page prints it), not the
normalized-looking variant.

## 11. Risks, unobserved, tooling

- **Unobserved:** whether any *other* client states "no invented commands" (entry claim 3's
  comparison). This seat opened S264 only; the claim is not falsified here, it is simply not
  tested. A wave-2 seat holding the other three rows (S261-S263) can settle it.
- **Unobserved:** the rendered page's JS-side search index; not fetched, not needed for the
  quotes (all located in the served HTML).
- **`llms-full.txt` is 5.9 MB** — not snapshotted; only grepped in scratch to establish the form.
  If a later rule wants a whole-site pin, fetch it alone in the background.
- **Risk for the L1:** do not cite `#skillmd-format` as the home of the 60-char rule (§5) — that
  section states no limit and a reviewer will catch it.
- **Tooling:** no installs, no upgrades, no pacman, no git writes. Scratch
  `/tmp/k72w1-ExecSrcHermes.pXAF` deleted before return; no fixture repo needed.
- **Lane state note (not mine to change):** `git rev-parse HEAD` read `e61fd294c2e1cdd16d594b57b310254183ace1e7`,
  not the plan's base `c69711ee…`; `git status --porcelain` showed only untracked
  `.ufo/waves/round-72/w1.ready` and `.ufo/waves/round-72/w1/`. Recorded, not acted on.
