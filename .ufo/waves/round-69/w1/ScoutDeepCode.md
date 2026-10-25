# ScoutDeepCode — round 69 wave 1, depth scout

Scope: re-open the Deep Code Agent Skills page and verify the S205 row quote and the priority
table, for C1 (skill name-collision precedence). Read-only on the lane: no edit to `SKILL.md`,
`corpus/`, `verifiers/`, `PROVINCE.md`, `plans/`, no lane Git index or jj write.

## Verdict

**FOUND.** The quote `only the highest-priority one is kept` is verbatim in the page's
**Scan Locations** section, and the priority table does order the roots:
`./.deepcode/skills/` → `./.agents/skills/` → `~/.deepcode/skills/` → `~/.agents/skills/` →
`built-in`. C1's S205 conjunct survives re-opening. **One non-source defect found in the draft
entry (§7) that no counter catches.**

## 1. Access record

| field | value |
|---|---|
| URL | `https://deepcode.vegamo.cn/en/docs/configuration/agent-skills` |
| access date | **2026-10-25** |
| HTTP | `200`, `content-length: 163923`, `x-nextjs-cache: HIT`, `etag: "z1mbizw18v3i6c"`, `server: nginx/1.18.0 (Ubuntu)` |
| document | `<html lang="en">`, `<title>Agent Skills | Deep Code Docs</title>` |
| canonical | `https://deepcode.vegamo.cn/en/docs/configuration/agent-skills` (equals fetched URL — no locale redirect) |
| body sha256 | `af207facb7a99386122390e6ce7b6d7c217112e36dd368666694ba7a56e1834c` |

Fetched with `curl -sSL --max-time 60`. `…/agent-skills.md` and `/llms.txt` both return `404` —
there is no markdown or llms route; the HTML is the only served form.

## 2. The quote — exact bytes

Heading: `<h2 id="scan-locations"><a href="#scan-locations">Scan Locations</a></h2>` (h2; the page
TOC gives `{"id":"scan-locations","text":"Scan Locations","level":2}`, between `overview` and
`minimal-skill`).

The section's opening paragraph, server-rendered, byte-exact:

```html
<p>Deep Code scans skills in the following order. If multiple skills resolve to the same <code>name</code>, only the highest-priority one is kept.</p>
```

As flat text: *Deep Code scans skills in the following order. If multiple skills resolve to the
same `name`, only the highest-priority one is kept.*

**Exact quote: `only the highest-priority one is kept` — FOUND**, verbatim as a contiguous
substring, 6 words (≤25). It is immediately preceded by `, ` and followed by `.`.

Appears exactly **once** per rendering, in **three** independent renderings inside the same
response, all of the same single sentence:

| # | offset | rendering |
|---|---|---|
| 1 | 5434 | server-rendered HTML (the DOM a reader sees) |
| 2 | 32618 | MDX/JSX payload (`_components.p`, split by the `name` code span) |
| 3 | 99847 | embedded markdown mirror (`| Priority | Scope | Path | …` pipe table) |

`highest-priority` occurs 3× in the file = those three copies. No second, competing sentence:
`higher-priority` occurs 2× and is a *different* statement (see §4). Nothing in the page states a
name-uniqueness rule, so there is no internal contradiction with the quoted precedence rule.

## 3. The priority table — does it order the roots?

Verbatim header and body, server-rendered:

| Priority | Scope | Path | Purpose |
|---|---|---|---|
| 1 | Project | `./.deepcode/skills/` | Native Deep Code project skills |
| 2 | Project | `./.agents/skills/` | Project skills shared with other agent clients |
| 3 | User | `~/.deepcode/skills/` | Native Deep Code user skills |
| 4 | User | `~/.agents/skills/` | User skills shared with other agent clients |
| 5 | Global | `built-in` | Skills bundled with Deep Code |

**Yes — the table orders the roots** on an explicit, ascending numbered `Priority` column, project
first, and the sentence is bound to it by two wordings: *"scans skills in the following order"* and
*"the highest-priority one is kept"*. The pre-table `<p>` and the table are adjacent siblings, so
the entry's locator ("`the "Scan Locations" section`, the sentence before the priority table") is
exact.

Structural reading of the ordering (derived from the table, stated as such):

- **Scope dominates root.** All `Project` rows (1, 2) precede all `User` rows (3, 4): a project
  shared skill (2) beats a user native skill (3).
- **Within a scope, the native root beats the shared root** (1 > 2, 3 > 4).
- **Bundled skills are last** (5), so any project or user skill shadows a built-in of the same name.

`[INFERENCE, near-certain]` that the low number is the *higher* priority: the column is literally
named `Priority`, numbered 1–5, and the sentence names a "highest-priority" winner; the page never
says "lower number wins" in so many words. The inverted reading is also implausible on its face
(it would let bundled skills shadow the user's own). I record this as an inference, not a quote.

Note for the entry's characterisation: the list is **not** a pure root order and **not** a pure
scope order — it is one ranked list that interleaves both axes. The draft's rule cell ("roots are
scanned in a numbered priority order and one winner is kept per name") is defensible, but the
sharper and fully sourced statement is the three bullets above.

Two precision notes: row 5's `Path` is the token `built-in`, not a filesystem root, so "five scan
roots" is loose (four roots plus one bundled tier); and the table does not say whether two
same-named skills are merged or suppressed — the sentence says one is *kept*, which the entry
correctly renders as "one winner".

## 4. Independent corroboration on the same page (unused by the entry)

The page asserts the same semantics twice more, in other sections — this is corroboration the entry
does not carry:

1. **Troubleshooting → "The skill does not appear in `/skills`"** (`<h3>`, the `troubleshooting`
   h2), checklist item 5: *"A higher-priority skill with the same name is not shadowing it"*. Same
   rule, other vocabulary — `shadowing`, `higher-priority skill with the same name`.
2. **Enable and Disable Skills**, Rules list: *"Setting a skill to `false` hides every scanned skill
   with that resolved name"* and *"Project settings override user settings per skill"*. The first
   confirms that several skills can share one **resolved name**; the second is an independent
   settings-level override axis (orthogonal to scan order, not contradictory).

Also relevant to the collision *key*: SKILL.md Frontmatter says `name` is *"Used as the unique skill
name. If missing, Deep Code uses the directory name and converts `_` to `-`."* So the collision key
is the **resolved** name — frontmatter `name`, else the normalised directory name — which is how two
differently-named directories can still collide. That mechanism is absent from the entry.

## 5. Counter cross-check (not accepted on the plan's word)

Ran in a `git clone --shared` sandbox at `/tmp/k69-scout-deepcode`, never in the lane, with the
lane's working-tree bytes copied in and committed in the sandbox (`SANDBOX_HEAD=46f3f2a5…`):

```
python3 -B verifiers/check_skill_precedence.py --rev HEAD
  measured-rev: 46f3f2a5cdee72996b6e5779a1e9a296cc59a412
  skill precedence backed 5 of 5                      exit 0

… --rev HEAD --fetch
  skill precedence backed 5 of 5
  fetch S203: found   fetch S204: found   fetch S205: found   fetch S206: found   fetch S207: found
  live quotes found 5 of 5                            exit 0

… --rev a5f7459f99bb27bf697e9438362e75ac5833eca8
  skill precedence backed 0 of 5   (entry missing: …skill-name-precedence-round69.md)   exit 1
```

So the S205 conjunct is genuinely counted, the `--fetch` arm really finds the string on the live
page, and the base control reproduces `0 of 5` / exit 1 — the counter is non-vacuous at both ends.

`--fetch` robustness, worth recording because it is load-bearing: `_page_text` replaces **every**
tag with a space and collapses whitespace, so the paragraph becomes `… the same name , only the
highest-priority one is kept.` — with a space before the comma. The chose quote starts *after* that
comma and therefore avoids the inline-`<code>` boundary entirely. A quote drawn as
`same name, only …` would report NOT FOUND under this counter even though it is correct prose. The
current quote is the stable choice; keep it that way.

Separate trap for anyone verifying the *table* rather than the quote: the embedded markdown mirror
(offset 99847) drops inline code, so its `Path` cells render **empty** (`| 1 | Project |  | Native
Deep Code project skills |`). The table's paths exist only in the HTML and JSX renderings. A
fetch/verify arm that parsed the markdown mirror would see three blank roots.

## 6. Lane-state observations (read-only)

- `git rev-parse HEAD` = `a238989a96cb0d2b939679126b832d75b861ca6e` — **not** the plan's declared base
  `a5f7459f99bb27bf697e9438362e75ac5833eca8`. This is *not* a violation: `a238989` is the round-69
  freeze commit ("frozen plan, three counters … and base/junk controls") and `a5f7459` is its
  parent (`git merge-base --is-ancestor a5f7459 HEAD` → yes). The plan's "base lane tip" wording
  means the pre-round-69 tip. Worth stating once so no later seat misreads the divergence.
- Working tree carries the draft: `?? corpus/knowledge/skill-name-precedence-round69.md`, plus
  modified `corpus/SOURCES.md`, `corpus/README.md`, `PROVINCE.md`, `SKILL.md`, `corpus/QUALITY.md`,
  `corpus/knowledge/client-trust-gates-round68.md`, `verifiers/check_r67_routed_repairs.py`.
- S205 row in `corpus/SOURCES.md:146` is an 11-cell `mined` row, `opened 2026-10-25`, `90d`,
  `used-by` = the entry, `B` grade; its anchor cell points at "the `Scan Locations` section, the
  sentence before the priority table; quote … (6 words)" — all of which I confirmed against the
  page byte for byte. Coverage-map index row present at `corpus/README.md:130`.

## 7. Defect found in the draft entry (prose, uncaught by the counter)

`corpus/knowledge/skill-name-precedence-round69.md:46` (also `.ufo/waves/round-69/assimilation/
entry-draft.md:46` and `.ufo/waves/round-69/assimilation/validate/corpus/knowledge/
skill-name-precedence-round69.md:46`) states:

> Five clients, none of them the lane's pinned seven; a pinned client's collision rule is not
> claimed here.

**That is false as written.** The lane's pinned seven, quoted from
`corpus/knowledge/client-trust-gates-round68.md:56-58`, are *"Claude Code, Codex, VS Code, Copilot
CLI, Gemini CLI, **opencode**, Cursor"*. **opencode is one of the entry's five** — so "none of them"
is wrong, and "a pinned client's collision rule is not claimed here" is contradicted by the entry's
own map, which does claim opencode's posture ("no precedence stated: the troubleshooting guidance
asks for names that are unique across every location it loads") and repeats it in § What a skill
author does ("One client states no order at all").

Provenance of the error: the sentence is copied from the r68 entry's Limits, where it was **true**
— r68's five (VT Code, Parallel Works, Kilo Code, Microsoft Agent Framework, Mistral AI Vibe) are
all non-pinned. Copying the boilerplate while swapping the client set inverted its truth value. The
counter cannot see this: it reads provenance trio, ids, rows, quotes and table coherence, never the
Limits prose.

Not a source miss and not a claim failure — it understates the claim. Corrected, the Limits become
*stronger*: the entry holds a **pinned** client's collision posture (opencode), and that posture is
the *absence* of precedence, which is exactly the interesting one for the portable rule. Report
only; I did not edit.

## 8. Depth the entry is missing (report only — no edits made)

1. The **collision key** is the resolved name (frontmatter `name`, else normalised directory name)
   — the mechanism by which two directories collide at all.
2. **Scope dominates root; native beats shared within a scope; bundled last** — the derived
   structure of the table, and the thing that makes the Deep Code row comparable to Roo Code and
   Junie rather than merely listed beside them.
3. The **Troubleshooting** sentence ("A higher-priority skill with the same name is not shadowing
   it") as a second, independent locator for the same rule — useful because it is short, unshaped,
   and uses the client's own word *shadowing*.
4. The **settings override axis** ("Project settings override user settings per skill") as a
   distinct, orthogonal override, so a reader does not conflate `enabledSkills` with scan order.

## 9. Remaining unknowns

- Whether `1` is *documented* as the highest priority anywhere on the site outside this page (I read
  only this page; the page's `configuration_en.md` link was not followed). The inference in §3 is
  strong but is not a quote.
- Whether the page changed between the L1's round-start fetch and mine. My copy's sha256 is
  `af207fac…`; the plan records no hash, so byte-stability across the day is unverified.
- No client behaviour was observed — documentary evidence only, as the plan's bound requires.

## Seat hygiene

No installs (no pacman, no `uv tool`, no `~/.local/bin` writes). One `git clone --shared` sandbox at
`/tmp/k69-scout-deepcode`, outside the lane, used only to execute the C1 counter. No write to any
lane file outside `.ufo/waves/round-69/w1/`. Two throwaway shell bugs of mine, recorded so they are
not mistaken for lane defects: the first sandbox copy put `corpus/SOURCES.md` at the repo root and
the counter correctly reported `no 11-cell row` for all five ids; the first quote-scan regex failed
because the MDX payload escapes its quotes (`\"`) and the content therefore ends in a backslash.
Both were my errors; neither touches the lane.
