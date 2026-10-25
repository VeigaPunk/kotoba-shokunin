# ScoutOpencode — round 69 / wave 1 — C1 source S207 (opencode) re-open

Scope: **S207 only** (`https://opencode.ai/docs/skills/`). S203 Roo Code, S204 Amp, S205 Deep
Code, S206 Junie belong to peer scouts; nothing here scores them. Lane root
`/home/vgpnk/Projects/shokunin/kotoba-shokunin`, base tip `a5f7459f` + plan commit `a238989`
(= current `HEAD`), working tree read only; the only file written is this report.

## Verdict on the assigned question

**FOUND.** The quote is verbatim, contiguous, unshaped and unmangled on the served page, and it
sits inside the `Troubleshoot loading` section as **check 3 of 4**.

| field | value |
|---|---|
| access date | **2026-10-25** (`date -u` = 2026-10-25T10:14:38Z; response `date:` header `Sun, 25 Oct 2026 10:14:39 GMT`) |
| heading | **`Troubleshoot loading`** (H2, HTML anchor `troubleshoot-loading`) |
| exact quote | **`Ensure skill names are unique across all locations`** |
| position | third item of the four-item ordered list beginning "If a skill does not show up:" |
| verdict | **FOUND** |

### Exact quote and its context

```
## Troubleshoot loading

If a skill does not show up:

1. Verify `SKILL.md` is spelled in all caps
2. Check that frontmatter includes `name` and `description`
3. Ensure skill names are unique across all locations
4. Check permissions—skills with `deny` are hidden from agents
```

- HTML byte context: `<li>Ensure skill names are unique across all locations</li>` — one bare
  `<li>`, **no inline markup inside the quote**, no terminal period.
- `od -c` on the extracted fragment: 63 bytes, terminating `s \n` (the `\n` is the extraction
  line-join, not page text).
- Occurrences page-wide: **1** (HTML), **1** (`.md` route). It is not duplicated in nav, sidebar
  or an embedded data blob — the hit is the rendered article `<li>`, flanked by the rendered
  items 2 and 4.
- Word count: **8**, which matches the registry's own claim `(8 words)` at
  `corpus/SOURCES.md:148` and the attenuation `"the third check"` in the same cell. The anchor's
  location claim is therefore **accurate as written**.
- `.md` route line numbers today: `## Troubleshoot loading` at **210**, the quote at **216**
  (useful only as drift evidence — see S207-4).

### Access evidence (re-runnable)

```
curl -sSL https://opencode.ai/docs/skills/     -> HTTP/2 200, 71,581 B
  sha256 06a30dceda8db8f5695ae1d692a6633a42cfdc05f535d1f92e28823541e482ff
curl -sSL https://opencode.ai/docs/skills.md   -> 200, 4,630 B (text/markdown)
  sha256 26dcb24c030c7fc2c05ea3e60d89bdd81f47ff06437f344ec6a49f647f408f0a
curl -sSI https://opencode.ai/docs/skills/     -> date: Sun, 25 Oct 2026 10:14:39 GMT, cf-cache-status: HIT
```

No tool was installed for this seat; all work used `curl`, `python3` and coreutils already present.

### Counter predicate, mechanised (not eyeballed)

I imported the counter's own shaping (`verifiers/check_skill_precedence.py::_page_text`, `_norm`)
and ran it over the fetched bytes:

| route | `q in _page_text(body)` | `q in _norm(body)` |
|---|---|---|
| HTML | **True** | **True** |
| `.md` | **True** | **True** |

Then the real arms, on a sandbox copy (`/tmp/k69v2/after`, never the lane):

```
python3 -B verifiers/check_skill_precedence.py --repo /tmp/k69v2/after
  measured-rev: working-tree / skill precedence backed 5 of 5                    exit 0
... --fetch
  fetch S203 found / S204 found / S205 found / S206 found / S207 found
  live quotes found 5 of 5                                                       exit 0
... --self-test
  self-test: 0 failure(s) over 18 assertions                                     exit 0
```

So the quote conjunct is satisfied for S207 by the counter's own definition, live, today.

---

## Deep findings (attack items; none falsifies the quote)

### S207-1 (high, semantic, depth) — opencode's **V2** docs page states the precedence ladder the entry says opencode lacks

The C1 entry's opencode row (`corpus/knowledge/skill-name-precedence-round69.md:25`) reads
"no precedence stated: the troubleshooting guidance asks for names that are unique across every
location it loads", and `corpus/SOURCES.md:148` teaches "opencode states no precedence between
same-named skills; its only guidance is a uniqueness rule across every location it loads". That is
true of the **v1** page. It is false of opencode as a documented client, because the V2 page —
already in this registry as **S064** — carries a dedicated `Precedence` section:

```
curl -sSL https://opencode.ai/v2/docs/skills   -> HTTP/2 200, 34,294 B
  sha256 786c87e66117f97074e5fa8a688ca93ae943ab17819016d8e11f399b97a4f189   (2026-10-25; S064 recorded 32,694 B on 2026-10-22 — the page has also moved)

## Precedence
Skills are selected by ID. If two sources define git-release, the source registered later
supplies the skill that OpenCode loads:

~/.config/opencode/skills/git-release/SKILL.md  ← lower precedence
.opencode/skills/git-release/SKILL.md           ← loaded

Sources are registered from lower to higher precedence:
  Built-in skills
  .claude/skills            — global first, then farthest ancestor → current directory
  .agents/skills            — global first, then farthest ancestor → current directory
  ~/.config/opencode/skills
  Project .opencode/skills  — project root → current directory
  Explicit skills config entries — config priority and array order

Avoid duplicate IDs unless you intend to override an earlier skill.
```

This is exactly the surface C1 claims is unheld: which of two same-named skills wins. V2 answers it
with a six-rung ladder and says duplicates are an *override mechanism*, whereas v1 item 3 says make
names unique. The two generations contradict each other; both are served today.

Verbatim candidates that pass the counter's shaping (≤25 words, contiguous, all `True` on both
`_page_text` and `_norm`):

- `the source registered later supplies the skill that OpenCode loads` — **10 words**, the rule;
- `Sources are registered from lower to higher precedence` — **8 words**, the ladder's header;
- `Avoid duplicate IDs unless you intend to override an earlier skill.` — **11 words**, the intent.
- (Not usable: a quote spanning `git-release` fails — the `<code>` becomes a space and yields
  `define git-release , the source`.)

Impact on the round's deliverable. `corpus/knowledge/skill-name-precedence-round69.md` ends with
"**Four of five clients resolve a collision by order, not by merging.**" Count opencode's V2 page and
it is **five of five**; the entry's single contrast case disappears, and a reader who takes
"opencode states no precedence" at face value is misinformed about the client the lane covers most
(S024, S039, S045, S059, S064, S109 are all opencode rows). The frozen C1 *claim* still stands —
the plan's surface explicitly allows "or that names must be unique" — but the delivered entry
overgeneralizes.

Cheapest honest fix (no new fetch needed, bytes are above). Note **`CORPUS.md` rule 2 is
append-only**: `anchor` cannot be edited in place, so S064 must **not** be retro-fitted with
`§Precedence`. Either:

1. add one new row (next unused id, `S209`) for the V2 page's `§Precedence` with the 10-word quote,
   and make the entry's opencode cell read "v1 page: uniqueness only; V2 page: an explicit ladder in
   which the later-registered source wins (project `.opencode/skills` over `~/.config`, explicit
   config entries highest)"; **or**
2. if the entry's scope is deliberately the served v1 page, say so in the cell and in S207's
   `scope` ("the v1 page at `/docs/skills/`"), so the two-generation split is not silently flattened.

Option 1 is the only one that answers the theme's question; option 2 is defensible only if the round
records why the V2 page is out of scope after having been opened in round 54.

### S207-2 (medium, consistency) — the landed tier (`B`) contradicts the staged record (`A`) and the contract (`A`)

Five artifacts disagree on one field:

| artifact | S203–S207 tier |
|---|---|
| `corpus/SOURCES.md:144-148` (landed) | **B** |
| `.ufo/waves/round-69/assimilation/validate/corpus/SOURCES.md:144-148` (mirror) | **A** |
| `.ufo/waves/round-69/assimilation/append-block.md:1-5` (record) | **A** |
| `corpus/lessons/round-69.md:121` ("tier B … at landing") | **B** |

`mtime` ordering is unambiguous: `append-block.md` 06:58:20, mirror 06:58:41, `corpus/SOURCES.md`
07:08:11, `lessons/round-69.md` 07:17:50. The tier changed to `B` **after** the record was written
and the record was never reconciled — so `append-block.md` no longer reproduces the bytes it claims
to record, which is the same class as the r68 record-fidelity defect R68-7.

Which value is contract-correct: **A**. `CORPUS.md:93-96` (identical to
`.ufo/waves/kaika/SOURCES-CONTRACT-v1.md:26-28`) defines A as "primary or authoritative for that
scope (… **official docs** …)" and B as "strong secondary (expert write-up…, survey, textbook)". A
vendor's own page describing its own loader is official docs for exactly the narrow scope S207
claims ("opencode's own documented guidance on same-named skills"). The lane's own precedent agrees:
`docs/A` = 98 rows vs `docs/B` = 13, and the opencode rows that make up the A side include **S059,
"opencode — Agent skills (**served docs**)"**, i.e. the identical source class at A. The 13
`docs/B` rows are S037 (a vendor blog), S117 (a sibling lane), **S198–S202** (r68 client rows),
**S203–S207** (this round) and S208 — so five of the thirteen are this round's, and `B` is a
round-67/68/69 *cohort convention* that runs against the contract's letter, with no recorded
rationale.

Recommendation: land **A** for S203–S207 (matching the staged record and the contract), or keep `B`
and record the one-clause rationale in the lesson **and** re-write `append-block.md` +
`assimilation/validate/corpus/SOURCES.md` so the record matches. Not a counter failure — the C1
counter never reads `tier`, and `B` is admissible (only `C` is barred as sole support for an entry).
This corroborates `ScoutRoo.md` ROO-2 independently; two seats, same split, same direction.

### S207-3 (medium, census) — the after-census must be re-taken: 18 W04, not the recorded 17

I re-ran the fleet census against `HEAD` and against the working tree in `/tmp` mirrors whose
registry sits at `<root>/corpus/SOURCES.md` (with `--file` the lane dir is
`dirname(file)/..`, so a registry copied to a tree root makes every `used-by` path dangle and the
run exits 1 — that is a harness artefact, not a lane defect; see the note under Confidence):

```
base (git show HEAD:corpus/SOURCES.md)     16 W04, 0 E-codes, "ok", exit 0
after (working tree corpus/SOURCES.md)     18 W04, 0 E-codes, "ok", exit 0
```

This reproduces the lane's own `controls/census-before.txt` **exactly** (16 W04, `exit=0`). The two
new warnings are:

```
file  W04  S207 duplicate url opencode.ai/docs/skills across scopes
file  W04  S208 duplicate url learn.microsoft.com/en-us/agent-framework/agents/skills across scopes
```

`S207` fires because `scripts/sources-census.sh::url_of()` normalises with `sub(/\/$/,"",u)`
(line ~602), so the row's trailing-slash `https://opencode.ai/docs/skills/` collapses onto the URL
already held by S024/S039/S059 — it is *not* an `E04` only because S207's `scope` cell differs from
theirs (`E04` = duplicate URL **within** scope; `W04` = same URL **across** scopes). `S208` fires
because it re-states the same `learn.microsoft.com/en-us/agent-framework/agents/skills` URL already
held by `S201` (`corpus/SOURCES.md:142`) under a different scope — expected for an anchor-correction
row, but still a new warning the closure must name.

`.ufo/waves/round-69/assimilation/validate-census.txt` records only **17** W04 (`S018…S118` + `S207`)
and declares its mirror "at base a238989a". Both facts are correct for the moment it was taken but
stale for the landed tree: the mirror predates the `S208` append and its `S207` W04 is already
anticipated. So the S207 warning is **disclosed, not hidden** — but the round's final after-census
must be re-run at the landing tip and must show **18**, naming S207 and S208, or the closure records
a number the tree cannot reproduce. The plan freezes only the *before* figure ("census before
(… 16 W04) and after"), so this is not a plan violation; it is a recording obligation.

### S207-4 (low, drift, informational) — the v1 page moved under the older opencode anchors

Today's `/docs/skills.md` is **4,630 B**, sha256 `26dcb24c…`; S024/S039/S059 recorded **5,365 B**,
sha256 `f10ced73…` on 2026-10-22, and S024 recorded the HTML route as 73,201 B / `4d96fa56…`
against today's 71,581 B / `06a30dce…`. Consequently S024's line anchor `skills.md:223-231` and
S039's `Troubleshoot loading, item 4 (skills.md:230)` no longer resolve: the section now starts at
**210** and item 4 is at **217** (≈13 lines of drift). S207 is immune because it anchors by
heading + item ordinal rather than by line number — a good choice that the older rows should copy
at their 90 d recheck. Out of my slice; flagged for whoever verifies S024/S039/S059.

### S207-5 (low, counter bound, informational) — `--fetch` cannot verify the claimed *section*

`verifiers/check_skill_precedence.py:269` accepts the quote if it appears **anywhere** on the page
(`if quote in _page_text(body) or quote in _norm(body)`), and `_row_quote` only asks that the row's
anchor carry some ≤25-word quote. The 18-world `--self-test` battery never touches a live page, and
`--fetch` runs only when the content score is already 5/5. Net: **no machine check can catch a
wrong `Troubleshoot loading` / `the third check` claim** — if this quote sat under `Validate names`
or in a nav blob, the counter would still print "found". This seat's re-open is the only evidence
for S207's location claim, and it holds (item 3 of 4, one occurrence page-wide). The closure record
should state that bound explicitly rather than implying `--fetch` covers it.

### S207-6 (positive) — the draft is counter-clean today

Sandbox run: content **5 of 5** exit 0, live `--fetch` **5 of 5 found** exit 0, self-test **0
failures over 18 assertions**. S207's row (`corpus/SOURCES.md:148`), the entry's `source:` line
(`…round69.md:5`) and the entry's table row (`:25`) all carry the quote, and the source cell is a
substring of the entry's `source:` line as the counter requires.

---

## Confidence

- Quote verbatim / heading / item ordinal / counts / absence of inline markup / both routes: **observed**, byte-exact above, hashes recorded for re-run; independently confirmed by the counter's own live `--fetch` arm.
- V2 `§Precedence` content and the six-rung ladder: **observed** in the rendered prose of a 200 response today (hash recorded); S064 proves the page's lineage, not that its 2026-10-22 text said the same — the ladder is today's text.
- Tier judgement: **inference** from `CORPUS.md:93-96` + the lane's own `docs/A` precedent; no counter reads `tier`, so this is a quality finding, never a claim failure.
- Census figures: **observed** (`16`/`18`, both `exit 0`, `E`-code count `0`). The `used-by`-dangling noise in a first attempt was my mirror layout (`--file` sets the lane dir to `dirname(file)/..`), and is **not** a lane defect — full-tree layout reproduced `ok`/`exit 0`.
- Runtime behaviour of opencode: **not observed** (documentary only, per the C1 bound).
- Remaining unknowns: (a) whether the L1 intends `B` as a deliberate cohort rule or it is a landing slip — nothing in `lessons/round-69.md` records a rationale; (b) whether wave 2 will accept a V2 row or narrow S207's scope to the v1 page; (c) whether `S208`'s W04 was ever disclosed anywhere (it is absent from `validate-census.txt`).
