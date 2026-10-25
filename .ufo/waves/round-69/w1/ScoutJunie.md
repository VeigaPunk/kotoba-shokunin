# ScoutJunie — C1 source depth: the Junie (S206) row

Seat: `L1Kotoba69-2.ScoutJunie` (leaf, no dispatch). Base lane tip read: `a238989a` (descendant of
the plan base `a5f7459f`; `git merge-base --is-ancestor` → yes). Lane working tree was **read only**
except this file; every counter run happened in `/tmp/scoutjunie-r69` (`git clone --shared` + copies).

## 1. The assigned question — FOUND, verbatim

**Source:** https://junie.jetbrains.com/docs/agent-skills.html
**Access date:** 2026-10-25
**Bytes:** 38,509; sha256 `b3c676900e3de8a0d34754bb223685e1734c95ecc635280d8b8b159928f5a915` on two
fetches 2 min apart (byte-identical); `last-modified: Fri, 23 Oct 2026 18:43:22 GMT`;
`etag: "6adbaaca-966d"`.

**Heading:** `Skill location` — `<h3 id="skill-location">`, sole child context of
`<h2 id="how-junie-cli-uses-skills">How Junie CLI uses skills`.

**Exact quote:** `the project-level skill takes precedence and the user-level skill is ignored.`

**FOUND.** Verbatim, and stronger than "present after shaping": it is **contiguous raw HTML bytes**
with no intervening tag, one occurrence in the document (`offset 16068`), and one occurrence in
tag-stripped text. The lane's row is therefore not relying on Q56-shaped equality.

**Containing element (precision note).** The sentence is the closing
`<aside class="prompt" data-type="note" data-title="Scope priority" id="-jqc5nu_95">` note of the
Skill location section — not a standalone `<p>` under the heading. It is inside: `h3
id="skill-location"` at byte 12825 < aside at 15721 < the section close, with the next heading
(`h3 id="skill-directory-structure"`) at 16192 and no heading in between. The aside carries no
`hidden` / `aria-hidden`. So "the Skill location section" is correct, though a stricter locator
would name the note's own title (`Scope priority`).

**Full page sentence** (for a future recheck to re-locate):

> If a project-level ( <projectRoot>/.junie/skills/<skill-name>/ ) and a user-level (
> ~/.junie/skills/<skill-name>/ ) skills share the same name, the project-level skill takes
> precedence and the user-level skill is ignored.

Two parenthetical `<code>` spans precede the quote and the verb reads `skills` (plural). This
matters for §3 F3.

## 2. S206 row and the C1 counter, re-run (not accepted from any seat)

`corpus/SOURCES.md:147` — 11 cells, `kind=docs`, `tier=B`, `status=mined`, `opened=2026-10-25`,
`recheck=90d`, `used-by=corpus/knowledge/skill-name-precedence-round69.md`. Tier is **uniform**: all
five rows S203–S207 are `docs / B / mined / 2026-10-25 / 90d`, so no grading inconsistency.

From `/tmp/scoutjunie-r69` (working-tree copy of the draft):

| arm | result |
|---|---|
| `check_skill_precedence.py` (working tree) | `skill precedence backed 5 of 5`, exit 0 |
| `--rev a5f7459f…` | `0 of 5`, exit 1, `entry missing` |
| `--fetch` | `live quotes found 5 of 5` (`S206: found`), exit 0, 3.7 s |
| `--self-test` | `0 failure(s) over 18 assertions`, exit 0 |

Load-bearing check (my own two mutations, not the shipped self-test): changing one word of the S206
anchor quote in `SOURCES.md` → `0 of 5`, exit 1 (`S206: the per-client table row does not carry the
located quote`); changing one word of the Junie table-row quote → same; restoring → `5 of 5`.

## 3. Findings

**F1 — the anchor's self-reported count is wrong (low; documentation).** The S206 anchor says
`(12 words)`. The quote is **11** words / 78 chars:
`printf '%s\n' 'the project-level skill takes precedence and the user-level skill is ignored.' > q.txt && wc -w q.txt` → `11 q.txt`.
No validator reads this note (counters compute their own `len(q.split())`), and the plan's only
bound is ≤25 words, so nothing is violated — but it is unverified prose of exactly the kind Q54
scopes for lessons, sitting on a surface Q54 does not cover.

**F2 — the located-quote conjunct is satisfiable by a section heading (medium; instrument bound).**
Constructed world W: the S206 `source:` line quotes only the heading (`the "Skill location" section`,
no located-quote clause) and the Junie table-row quote cell holds `"Skill location"`. Result:
`5 of 5`, **exit 0**, and `--fetch` `5 of 5` (`S206: found` — the heading is on the page too).
Mechanism: `_quoted()` (`verifiers/check_skill_precedence.py:155`) accepts any double-quoted span of
1–25 words, and `_row_quote()` (`:178-182`) returns `max(matched, key=len)` over spans that also
appear in the anchor. Because the entry legitimately double-quotes the section name in the same
`source:` line (`the "Skill location" section`), the 2-word heading is an eligible "located quote".
So the counter proves *a shared double-quoted span*, not *a span that states a precedence rule*.
**This does not touch the drafted claim** (the draft uses the substantive sentence and its table row
carries it). Hand this instance to `MutC1Counter`: the self-test's 18 worlds never reduce the quote
to the heading. A tightening would be a word floor on the located quote (≥6 words) or leaving the
section name unquoted in `source:` lines.
Corroboration (not taken on trust): `MutC1Counter` reproduced world W in its own sandbox
(`/tmp/k69-mut-c1`) and reports the adjacent unpinned rule — relaxing the 25-word cap to 400
survives the battery. I re-ran that mutant myself in `/tmp/scoutjunie-r69` (`<= 25` → `<= 400` in
`_quoted`): `self-test: 0 failure(s) over 18 assertions`, and the honest draft still `5 of 5`.
So the same conjunct has two unguarded freedoms, substance and length: no self-test world varies a
quote's substance or drives it past the cap.

**F3 — the S172 `payload-absent` refusal's reason is false; the M111/Q62 class recurs (high;
consistency).** The campaign register row this theme inherits — read-only,
`/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md:111-113` —
records `S172 | payload-absent | https://junie.jetbrains.com/docs/agent-skills.html` with the
reason *"cited source, companion URLs and local artifacts were all checked; the quote is in none of
them"* and this cited span:

```
`If a project-level and a
user-level skills share the same name, the project-level skill takes precedence and the
user-le`
```

The span is **truncated mid-word at `user-le`** and **elides both `<code>` parentheticals**, so it
can never be located on any rendering. I tested the two plausible normalizations against the fetched
page: `If a project-level and a user-level skill share the same name` → absent (raw and
tag-stripped); `… a user-level skills share the same name` → absent (same). The **payload is
present** — the full sentence is on the page, and the lane's narrower S206 quote is contiguous
bytes. So the register's verdict label asserts payload absence where the payload exists; the true
defect is a mangled copy of the span (elision + write-time truncation), i.e. an **anchor defect**,
which is exactly the M111 case Q62 was landed for.

Why this is not already covered: Q62's scope cell is *"source refusals in lessons and SOURCES
rows"*; a campaign register row is a third surface. C2's D6 repair is a **presence floor** (mistake
row + criterion), so no lane instrument rejects this instance — by Q57's absorption test the M111
erratum is **not absorbed on the register surface** one round after it landed. CritC2Repairs adds
that D6 is also *line-granular*: M111's bullet wraps, so `R68-6` and `S201` never share a line and
the repaired tip fails D6 for that reason — so D6 cannot serve even as the presence evidence for
this class without a line-joining fix. `corpus/lessons/round-69.md:91`
("every `payload-absent` row refused (the quoted span was not located on the page this round
fetched)") is literally true of the span but preserves the register's payload-absence framing.
Recommend the lesson record the mechanism — parenthetical `<code>` elision plus mid-word
truncation — so no later round re-derives "the Junie page lacks the precedence rule". Credit where
due: the lane already did the right thing downstream by re-opening under S206 with an unshaped,
contiguous quote.

**F4 — one paraphrase step past the quote (tiny).** The entry's Junie rule cell says the loser is
"ignored **rather than merged**", and `## What a skill author does with this` leans on "not by
merging". The page says only *ignored*; "rather than merged" is [INFERENCE]. Defensible (an ignored
body is not merged) but it is not in the located quote — either drop those four words or mark them
as inference.

## 4. Bounds of this verification

- Documentary only; no observed Junie behaviour. The page documents an order for the **project/user
  pair alone**; it lists `.agents/skills/`, extension, custom-folder and built-in skills with **no
  stated order** among them, so the entry's "scope order" must not be read as covering
  `.agents/skills/`. The entry does not overclaim this.
- One rendering: the `.md` route (`https://junie.jetbrains.com/docs/agent-skills.md`) is **404**
  (`nginx/1.31.7`), so unlike other lane sources I could not cross-check a second representation.
  Single HTML rendering, mitigated by two byte-identical fetches.
- Read-only on the register; I could not inspect the campaign's history to confirm the truncation
  happened at write time. The mid-word cut plus the missing parentheticals is the observed fact.

## 5. Remaining unknowns

- Whether Junie orders `.junie/skills/` against `.agents/skills/` — page silent; not needed for
  S206's claim.
- Who wrote the S172 span and whether `user-le` was a campaign write truncation — needs campaign
  repo history (outside this lane).

## 6. Installs

None. No tool installed or upgraded this seat.
