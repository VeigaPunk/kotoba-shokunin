# ScoutSiblingRuleMaps — coverage-map reconnaissance, round 69 wave 1

Seat: coverage reconnaissance only. No file under `SKILL.md`, `corpus/`, `verifiers/`, `PROVINCE.md`,
`plans/` or any committed path was touched; nothing in the lane was checked out, staged or written.
Base measured: `a5f7459f99bb27bf697e9438362e75ac5833eca8` (read-only `git grep <rev>`, `git show <rev>:<path>`).
Live fetches went to `/tmp/scout-siblings/` only. No tool installs.

## Verdict in one line

**4 of 5 clients are new ground; opencode is not** — its exact same-name sentence is already held by
`corpus/knowledge/skill-selection-rules-round50.md`, **and** opencode's *current* (V2) docs carry a
full precedence ladder that the round-69 draft's "no precedence stated" row misses.

## Q1 — is any of the five already covered by another kotoba entry?

Base-rev sweep, `corpus/knowledge/` only:

```
git grep -l -i -E 'roo code|roocode|\broo\b'  a5f7459 -- corpus/knowledge   -> (no files)
git grep -l -i -E '\bamp\b|ampcode'            a5f7459 -- corpus/knowledge   -> (no files)
git grep -l -i -E 'deep ?code|vegamo'          a5f7459 -- corpus/knowledge   -> (no files)
git grep -l -i -E 'junie|jetbrains'            a5f7459 -- corpus/knowledge   -> (no files)
git grep -l -i -E 'opencode'                   a5f7459 -- corpus/knowledge   -> 40 files
```

| client | prior kotoba entry at base | prior SOURCES row | verdict |
|---|---|---|---|
| Roo Code | **none** (0 of 58 entries) | none in the lane registry; campaign row `S185` (`docs.roocode.com/features/skills`) was **refused** in r68 as `payload-absent` (`corpus/lessons/round-68.md:107`) | new client ground |
| Amp | **none** | none | new client ground |
| Deep Code | **none** | none | new client ground |
| Junie | **none** | campaign row `S172` (`junie.jetbrains.com/docs/agent-skills.html`), **refused** r68 (`round-68.md:104`) | new client ground |
| opencode | **40 entries**; the same-name surface is held verbatim by `skill-selection-rules-round50.md` | `S024`, `S039`, `S059`, `S064` | **already covered** |

opencode detail, because it decides how the C1 row should be framed:

- `skill-selection-rules-round50.md` (table row `| opencode | S024 | … | "Ensure skill names are unique
  across all locations" (``skills.md:229``) | name |`) already records **the same sentence the r69 draft
  uses as S207**, already framed as "no winner, a uniqueness rule, keyed on name". The r69 opencode row is
  therefore a **carried row**, not new ground (the same pattern round 51 disclosed for Claude Code, its
  finding 4, `skill-overlap-levers-round51.md`).
- Runtime/implementation dedupe is also already held, independently of docs: `harness-router-models-round9.md:127,165`
  (by-name dedupe **nondeterministic**), `harness-verifier-round10.md:105,128` (`oc.dup.roots_both_sided`,
  last-parsed-wins), `opencode-offer-trace-round8.md:177,185` ("losing duplicate of a same-named skill"),
  `skill-activation-telemetry.md:74` (1,898 `duplicate skill name` WARNs), `instruction-surface-census-round13.md:112,143`
  (first-name-wins for context files), `skill-overlap-levers-round51.md` (permission `deny` keyed on the skill name).
- r68's client set (VT Code, Parallel Works, Kilo Code, Microsoft Agent Framework, Mistral AI Vibe) does not
  overlap r69's five; Kilo Code is a Roo-family fork but a different client and is named on a different surface
  (trust gates), so it is not a cover for Roo Code.

Consequence for C1's grade: the claim is a **4-new-client** coverage move plus one re-carry. That is still a
defensible depth move (four clients named for the first time anywhere in the corpus), but the entry must not
read as five new clients, and the plan's "the lane holds no such ground" is true only of a *precedence* entry —
the lane does hold opencode's uniqueness rule.

## Q2 — does opencode's own docs state precedence beyond the troubleshooting uniqueness check?

**Yes. On `https://opencode.ai/v2/docs/skills/`, § Precedence.** The draft cites `https://opencode.ai/docs/skills/`,
which is the **V1** page and states none.

Both routes are live and are different documents (fetched 2026-10-25T10:17Z, no redirects, both HTTP 200):

| route | bytes | sha256 (first 12) | "Ensure skill names are unique…" | "Precedence" heading |
|---|---|---|---|---|
| `https://opencode.ai/docs/skills/` (V1) | 71,581 | `06a30dceda8d` | present (Troubleshoot loading, item 3) | **absent** |
| `https://opencode.ai/v2/docs/skills/` (V2) | 34,294 | `786c87e66117` | absent | **present** |

V2 § Precedence, tags dropped / entities unescaped (the lane's documented shaping, QUALITY Q42/Q56), in page order:

> "Skills are selected by ID. If two sources define `git-release`, the source registered later supplies the
> skill that OpenCode loads:
> `~/.config/opencode/skills/git-release/SKILL.md  ← lower precedence` / `.opencode/skills/git-release/SKILL.md  ← loaded`"
>
> "Sources are registered from lower to higher precedence: Built-in skills / `.claude/skills`, global first and
> then from the farthest ancestor toward the current directory / `.agents/skills`, global first and then from the
> farthest ancestor toward the current directory / `~/.config/opencode/skills` / Project `.opencode/skills`, from
> the project root toward the current directory / Explicit `skills` config entries, in config priority and array order"
>
> "Avoid duplicate IDs unless you intend to override an earlier skill."

That is a six-tier, later-wins source order — exactly the surface C1 claims to map — and it also names the
override intention, which is stronger than "names must be unique".

The lane already knows this page: **`S064`** is a registry row for `https://opencode.ai/v2/docs/skills`
(2026-10-22, 32,694 B, sha256 `243e8890…`, `skills.mdx:140,160,184`), used by `skill-listing-thresholds-round54.md`
for the description-length sentence only. Its § Precedence was never mined, and `corpus/knowledge/` contains no
mention of the V2 ladder.

### Why this matters to C1 (attack item, not a coverage nicety)

1. The draft's opencode rule cell — "no precedence stated: the troubleshooting guidance asks for names that are
   unique…" — is **true of the cited V1 page and false of opencode's current V2 docs**. The entry names no
   version anywhere, and its § Limits says "Five clients, none of them the lane's pinned seven", which invites
   the reader to treat it as current-client documentation.
2. The headline finding "**One client states no order at all**" and the closing craft rule ("the documented
   remedy is therefore uniqueness") collapse for opencode once V2 is read: opencode documents an order and
   documents uniqueness as the author's *intent* signal.
3. **The counter cannot catch it.** `verifiers/check_skill_precedence.py --fetch` re-opens the URL named in the
   `S207` row (`https://opencode.ai/docs/skills/`), where the quote *is* present — so `skill precedence backed
   5 of 5`, exit 0 is reachable while the opencode rule cell is version-stale. This is the same class the r68
   counter's Q33 trust boundary accepts; it is not a counter bug, it is a claim-scope defect and belongs in the
   entry's `## Limits` or in the row itself.

### Second draft defect, found while checking the same sentence

`skill-name-precedence-round69.md` § Limits: "Five clients, none of them the lane's pinned seven." **False**:
opencode is one of the seven clients in every client map since round 54 (`skill-listing-thresholds-round54.md`,
`explicit-invocation-round55.md`, `agent-definition-files-round56.md`, `plugin-manifests-round57.md`,
`command-files-round58.md`, `scoped-rules-round60.md`) and is the lane's pinned substrate
(`verifiers/baseline.json` → `opencode_binary_sha256 538fcb1b…`, npm `opencode-ai` 1.19.4; S024/S039/S064 are all
opencode rows). The sentence needs to say "four clients outside the pinned seven, plus opencode".

## Coverage-map state at base

- `corpus/README.md` at `a5f7459` carries **no** row naming Roo Code, Amp, Deep Code or Junie, and no
  precedence-specific row (`git show a5f7459:corpus/README.md | grep -iE 'round 69|precedence'` → only the r58
  note).
- The plan's citation of the r58 note is accurate: "…precedence between a command and a same-named skill beyond
  what a page states" is the held-back clause (`README.md:203` at base; `PROVINCE.md` § Core round-58 bullet
  repeats "Client runs and same-name precedence beyond the pages stay unheld").
- Nuance the plan overstates: the map is **not** silent on same-name rules — the round-50 row
  ("How clients choose between skills") already carries a "which one wins rule documented" column for eight
  pages, opencode included. "No row for it" is true only of a *precedence-by-client* row.
- The working tree already carries the L1's draft row (`README.md:130`) and `S203`–`S207` (SOURCES.md
  `:144`–`:148`); at base both counts were 0 (`git show a5f7459:corpus/SOURCES.md | grep -cE '^\| S20[3-7] '` → 0).

## Registry continuity (S185 / S172 → S203 / S206)

The two the campaign quarantined are the same two the draft mines. r68 refused S185 (Roo Code) and S172 (Junie)
as `payload-absent` on the same URLs this round mines (`corpus/lessons/round-68.md:104,107`). The r69 lesson
records the re-open (`corpus/lessons/round-69.md:91`). Not a defect, but a reviewer should confirm the r69 rows
do not silently contradict the r68 refusal: the honest phrasing is "a *different* span was located this round",
since the r68 verdict was about a specific absent quote, not about the page.

## Confidence

- Coverage matrix (4 new / 1 covered): **high** — base-rev `git grep` with word boundaries over all 58 entries,
  plus a working-tree sweep that returns only the r69 draft, r69 lesson, README, SOURCES, plans and the two
  r69 verifiers.
- opencode V1 vs V2 split and the V2 ladder text: **high** — both routes fetched, byte counts + sha256 recorded,
  quote-presence checked per route, `<strong>`/`<code>` shaping dropped the lane's way.
- "opencode is one of the pinned seven": **high** (six client-map entries name it; baseline.json pins its binary).
- `1.19.4` being the V1 line rather than V2: **[INFERENCE]** — the V1 page says "OpenCode 1 does not use
  metadata…", the V2 doc tree is a separate `/v2/docs/` product line with a "Migrate from V1" page, and
  `baseline.json` records the host previously holding a removed `v2.0.26` binary. The page-content split itself
  is observed, not inferred.

## Remaining unknowns

- Whether opencode's V2 ladder applies to the lane's pinned `1.19.4` artifact, or only to the V2 line. Resolving
  it needs either V2 binary strings or the V2 docs' own version statement; the docs pages carry no "applies to
  ≥ x.y" marker.
- Whether the Roo/Amp/Deep Code/Junie pages are unchanged since 2026-10-25 (other wave-1 scouts re-open them;
  this seat did not duplicate that work).
- Whether the campaign register holds any *other* row for these four clients beyond S185/S172 (the quarantine
  slice has 13 rows, 7 `payload-absent`; only Roo and Junie are this theme's).

## What the L1 should change (recommendation, no edit made)

1. Scope the opencode row by version and either (a) add the V2 § Precedence ladder as the fifth *order* client —
   which removes the "one client states no order" headline and makes the craft rule "uniqueness is what V2 asks
   for unless you intend to override" — or (b) keep the V1 uniqueness row and add a Limits sentence naming the
   V2 page (S064) and its ladder. (a) is the larger depth gain; (b) is the honest minimum.
2. Drop or correct "none of them the lane's pinned seven".
3. Mark the opencode row as **carried** from `skill-selection-rules-round50.md` (the sentence, the page and the
   name-keyed framing are identical), the way round 51 disclosed its Claude Code re-carry.
4. Keep the four new clients as the claim's new ground; that part survives this recon unchanged.
