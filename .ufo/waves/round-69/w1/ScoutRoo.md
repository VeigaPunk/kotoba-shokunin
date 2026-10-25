# ScoutRoo — round 69 / wave 1 — C1 source S203 (Roo Code) re-open

Scope: **S203 only** (`docs.roocode.com/features/skills`). The four other C1 clients (S204 Amp, S205
Deep Code, S206 Junie, S207 opencode) belong to peer scouts; nothing here scores them.
Lane root `/home/vgpnk/Projects/shokunin/kotoba-shokunin`, base tip `a5f7459f` + plan commit
`a238989`; working tree read only, no file outside `.ufo/waves/round-69/w1/` written.

## Access evidence (2026-10-25)

```
curl -sSL https://docs.roocode.com/features/skills   -> 200, 71,129 bytes
sha256 fe801910f82e07631b3b5af3a2349fd75950eaabeda0280348b51c1aa92753e2
served as: Docusaurus v3.10.1, docsearch version "current",
           og:title "Skills | Roo Code Documentation",
           `<time datetime="2026-05-15T18:04:45.000Z">` -> "Last updated on May 15, 2026"
https://docs.roocode.com/features/skills.md  -> 404 (HTML page only; unlike Kilo/Mintlify
https://docs.roocode.com/features/skills.mdx -> 404  docs, no markdown source to anchor)
```
Server-rendered text is complete in the HTML body, so a plain `curl`/`urllib` recheck is sufficient
(the counter's `--fetch` arm will work).

## Verdict

**FOUND** — the quote is verbatim, contiguous and unshaped, and it sits in the **Override Control
bullet of the `What Skills Let You Do` section**. There is **no** "Override Control" section or
heading on the page; calling it one would be wrong. S203's own wording ("the 'What Skills Let You
Do' section, Override Control bullet") is correct and survives re-opening.

### Exact quote (8 words, no terminal period)

```
Project skills override global skills, mode-specific override generic
```

- Byte context (single line, no newline inside the quote):
  `<li class=""><strong>Override Control</strong>: Project skills override global skills, mode-specific override generic</li>`
- Occurrences in the whole page: **1**. It is the last `<li>` of the `<ul>` under
  `<h2 id="what-skills-let-you-do">What Skills Let You Do</h2>`; the next node is
  `<h2 id="how-skills-work">`. Only the label *Override Control* carries `<strong>`; the quote
  itself carries **no inline tag**, so nothing had to be stripped (QUALITY Q42 satisfied as written).
- Heading: **`What Skills Let You Do`** (H2, id `what-skills-let-you-do`). `id="override-control"`
  count = **0** — "Override Control" is a bullet label, not an anchor.
- Word count claimed by S203 "(8 words)": **confirmed 8** (`Project|skills|override|global|skills,|
  mode-specific|override|generic`).

### `Roo-specific (higher priority)` label — FOUND, exactly twice, both under `1. Choose a location`

| block | exact line | note |
|---|---|---|
| **Global** (`Global skills (available in all projects)`) | `# Linux/macOS — Roo-specific (higher priority)` | label prefixed with the OS; the Windows pair in the same block (`%USERPROFILE%\.roo\skills\…`) carries **no** priority label, only `# Windows` |
| **Project** (`Project skills (specific to current workspace)`) | `# Roo-specific (higher priority)` | bare label; the sibling line is `# Cross-agent (shared with other agent tools)` |

Counts: `"Roo-specific (higher priority)"` = **2**; line-start `^# Roo-specific (higher priority)$`
= **1** (project block); total `"higher priority"` = **3** (third: Skill Specification bullet
`Roo-specific locations: .roo/skills/, ~/.roo/skills/ (higher priority)`). Distinct string
`"high priority"` = 1 (Directory Structure comment `# Global Roo-specific skills (high priority)`) —
**do not** treat it as the same label.

Markup shaping of the label: both label lines are Docusaurus code-fence comment lines
(`<pre><code>…<span class="token plain"># …</span>`) rendered as bash. Plain text, but they are
**code-block comments, not headings** — the entry's Limits sentence "the unshaped 'Roo-specific
(higher priority)' **heading lines**" is imprecise wording (see ROO-4).

## Qualifying sentences the page states around the order

The page's normative section is **`Override Priority`** (H2, id `override-priority`). It is
**markup-bearing throughout**, which is exactly why S203 quotes the bullet instead of it:

1. "When skills with the same name exist in multiple locations, this priority applies (highest to
   lowest). `.roo/` paths always take precedence over `.agents/` paths **at the same project
   level**:" — 29 words (over the 25-word cap) and `<code>`-shaped.
2. An 8-rung ladder, `<strong>`+`<code>` shaped, rung 1 `Project .roo mode-specific` (highest) …
   rung 8 `Global .agents generic` (lowest). **The ladder is level-first**: all four Project rungs
   outrank all four Global rungs.
3. "A **project** skill always overrides a **global** skill of the same name. Within the same
   project level, `.roo/` overrides `.agents/`." — shaped; the load-bearing qualifier.
4. "Override them per-project when needed (**even with generic skills**)" — unshaped; confirms a
   project *generic* skill beats a global *mode-specific* one.
5. Skill Discovery: "**Mode filtering**: Only skills relevant to the current mode are available" —
   a mode-specific skill is not even a candidate outside its mode.
6. Troubleshooting (`Multiple skills conflict`): "Rely on override priority—project skills override
   global" — unshaped, 7 words, **level axis only**, no mode or root order.
7. Comparison table cell: `Project > Global, Mode > Generic` — unshaped, symbolic fragment.

## Q42 rationale, mechanised (reproduction of the counter's own predicate)

`verifiers/check_skill_precedence.py::_page_text` (lines 243-247) drops tags to a **space** and
`_norm` collapses whitespace; I ran that exact predicate over the fetched bytes:

| candidate | counter predicate | why |
|---|---|---|
| S203 8-word quote (unshaped) | **FOUND** | contiguous plain text |
| `Roo-specific (higher priority)` | **FOUND** | plain text in a code fence |
| Override Priority intro (29 w, `<code>`-shaped) | **NOT FOUND** | over 25 w *and* `.agents/`+space |
| ladder rung 1 (shaped) | **NOT FOUND** | `(` `<code>` `.roo/` `<code>` `)` -> `( .roo/ … )` |
| "A project skill always overrides … `.agents/`." (shaped) | **NOT FOUND** | tag->space yields `.agents/ .` (space before the period) |
| `Rely on override priority—project skills override global` | FOUND | unshaped, but level axis only |
| `Project > Global, Mode > Generic` | FOUND | unshaped, but a fragment, not a sentence |

Conclusion: the unshaped bullet is the **only ≤25-word unshaped *statement* carrying both axes**
(level and mode) on the page. The choice is correct, not merely convenient. Strictly speaking one
further unshaped candidate exists (the table cell, 6 words) — the entry's Limits should say
"sentence-level" if it wants to claim uniqueness.

## Attack items (for critics/executors; none blocks the quote conjunct)

- **ROO-1 (medium, depth).** Neither the registry `teaches` cell nor the entry's table rule cell
  records that the ladder is **level-first**. The quote's two clauses are *not* independent axes:
  `Project .agents generic` (rung 4) outranks `Global .roo mode-specific` (rung 5), so a reader
  applying "mode-specific over generic" to that pair gets the **opposite** of the page's own
  answer. Since the entry's whole subject is "which same-named skill wins", this is a load-bearing
  omission. Fix: one prose sentence in the Roo row / "orders differ in kind" bullet, e.g. "Roo's
  ladder is level-first: every project rung outranks every global rung, so a project generic
  `.agents` skill beats a global mode-specific `.roo` skill." State it in prose **without quotation
  marks** — the qualifier sentences are `<strong>`/`<code>`-shaped and would fail the `--fetch`
  predicate if added as a located quote.
- **ROO-2 (medium, consistency).** Landed vs staged S203 disagree: `corpus/SOURCES.md:144` says
  tier **B** and drops the staged phrase "page as served 2026-10-25";
  `.ufo/waves/round-69/assimilation/append-block.md` and
  `assimilation/validate/corpus/SOURCES.md:144` say tier **A** with the phrase. The change is
  recorded only as fact (`lessons/round-69.md:121` "tier B … at landing"), never with a rationale.
  Tier is scoped to `scope`, and S203's scope cell is the narrow vendor claim ("Roo Code's own
  documented resolution"), for which `SOURCES-CONTRACT-v1.md` line 26-28 says **A = official
  docs**; the lane's own spot-checks applied exactly that rule (r49 `S022`/`S023`, r50 `S028`:
  "It is a vendor reference page, so tier A is correct"). Rounds 67-68 used B for the whole client
  cohort (S198-S202), so B is at least consistent practice — but it is a *cohort convention* running
  against the contract's letter, and the rationale is unstated. Cheapest honest fix: one clause in
  the lesson / row scope ("tier B: the page is primary for Roo's behaviour but secondary for the
  cross-client question") or restore A for all five rows. Not a counter failure — the counter does
  not read tier.
- **ROO-3 (medium, recheck fidelity).** The landed row has no page revision/anchor byte for drift
  detection, and no `.md` source exists (404s above), so the 90 d recheck has to diff rendered HTML.
  The page publishes `Last updated … 2026-05-15T18:04:45.000Z`; record it (plus the sha256 above)
  and pin the recheck to the three byte-exact strings — the 8-word quote, `# Linux/macOS —
  Roo-specific (higher priority)`, `# Roo-specific (higher priority)` — instead of the vague
  "confirm … are unchanged" prose in `lessons/round-69.md:66`. Note the Windows lines carry no
  label, so a recheck that only greps `higher priority` (3 hits) can pass while the POSIX label
  changed.
- **ROO-4 (low, wording).** Entry Limits: "the root label rests on the unshaped 'Roo-specific
  (higher priority)' **heading lines**" — they are code-fence comment lines; the global one is
  prefixed `# Linux/macOS — `. Say "code-fence comment lines" and name both strings.
- **ROO-5 (low, counter fragility, informational).** The entry contains 17 quotes ≤25 words; four
  match S203's anchor cell — the 8-word rule (twice) and `What Skills Let You Do` (5 w) and
  `Roo-specific (higher priority)` (3 w). `_row_quote` picks by **length**, so the rule wins today
  only because it is the longest. Any future edit that quotes a longer phrase already inside the
  anchor silently changes "the row's quote" and can move the table-row requirement. Keep the
  anchor free of new quoted material; keep the rule quote the longest in the anchor.
- **ROO-6 (low, extra qualifier).** The Symlink support section states the collision **key**:
  "The skill name comes from the symlink name (or directory name if not symlinked). The frontmatter
  `name` field must match this name exactly—you can't create aliases …" — Roo resolves on directory
  name and forbids aliases. Worth one clause in the entry (it also contrasts with S207's uniqueness
  rule: Roo has no cross-location uniqueness requirement). Do **not** add it to the row anchor
  (ROO-5); prose only, and note it is `<code>`-shaped around `name` (word-bounded, so it happens to
  normalise under `_page_text`).

## Confidence

- Quote verbatim / location / heading / label / counts / shaping: **observed**, single fetch,
  byte-exact context reproduced above; sha256 recorded for re-run.
- Behaviour of Roo Code at runtime: **not observed** (documentary only, per C1 bound).
- Tier judgement: **inference** from `SOURCES-CONTRACT-v1.md` + spot-check precedent; the counter
  does not test it, so this is a quality finding, not a claim failure.
- Remaining unknowns: whether the L1 intends tier B as a deliberate cohort rule (no rationale
  recorded); whether wave 2 re-checks all five pages against the page mtime anchor.
