# Kb81R04SiblingScan — sibling-overlap scan for the r81 C2 SDK allowed-tools surface

Date: 2026-10-27. Scope question: does any sibling lane's committed scope surface
(`SKILL.md`/`PROVINCE.md`) touch `allowedTools`, Agent SDK instructions, or skill-craft
surfaces that the round-81 C2 claim (`allowed-tools` documentary matrix extension to the
Claude Agent SDK `allowedTools` query-config channel, entry
`corpus/knowledge/allowed-tools-sdk-round81.md`, source S249
`https://code.claude.com/docs/en/agent-sdk/skills.md`) could collide with?

## STRICT_HITS: 0

The seat-spec sweep, run verbatim and then re-run robustly:

- Spec form: `grep -lE 'allowedTools|agent.sdk|allowed-tools'
  /home/vgpnk/Projects/shokunin/*-shokunin/SKILL.md
  /home/vgpnk/Projects/shokunin/*-shokunin/PROVINCE.md` → matched only
  `kotoba-shokunin/SKILL.md` and `kotoba-shokunin/PROVINCE.md` (the claiming lane itself).
  Exit 2 on the first run was missing-file noise: audio and game-dev-2d have no SKILL.md
  (census: `18 SKILL.md`, `2 NONE`).
- Robust re-run (missing files skipped, per-file test): `allowedTools|agent\.sdk|allowed-tools`
  → same two kotoba paths, zero sibling paths.
- Case-insensitive widening `allowedtools|allowed[-_. ]?tools|agent[-_. ]?sdk`
  → same two kotoba paths, zero sibling paths. A `-`/`_`/`.`/space variant of the
  surface name exists nowhere on a sibling scope surface.
- Bare `\bsdk\b` (case-insensitive) → kaidoku SKILL.md/PROVINCE.md, kake
  SKILL.md/PROVINCE.md, mori SKILL.md. Every hit is an unrelated token, not the agent
  skill-grant surface: kaidoku's are `.NET SDK` tooling and `SDK/ABI-boundary` refusal
  caveats inside Dart-AOT analysis rows (SKILL.md:949,965; PROVINCE.md:113,245,265);
  kake's are `ds4cc-marketplace/apps-sdk` deploy paths and Kimi's injected
  `sdk-seed.js` drift marker (SKILL.md:28,222,243,320,367,428,497,523; PROVINCE.md:78);
  mori's are OMP binary internals `sdk.ts:2284` inside a job-cap refusal reading
  (SKILL.md:681,695). None names the Claude Agent SDK, `allowedTools`, or a skills
  grant channel.

Out-of-set corroboration (beyond the two named files, read-only): a fleet-wide
`grep -rliE 'allowed[-_. ]?tools|allowedTools|agent[-_. ]?sdk'` over every sibling
`corpus/` and `SOURCES.md` hit only (a) game-dev-3d
`corpus/live/r101-sentinel/api_bodies.jsonl` — 4 occurrences, all the captured string
`"You are a Claude agent, built on Anthropic's Claude Agent SDK."` inside recorded LLM
request bodies (data inside a sentinel fixture, not a lane claim), and (b) two vendored
`node_modules/playwright-core/.../SKILL.md` files under tabi `corpus/evidence/round-13`
carrying `allowed-tools` frontmatter — vendored artifact bytes, not tabi's scope
surface. Neither constitutes a sibling domain claim.

Freshness note on the scan: 15 of 20 sibling checkouts sit at detached heads that have
moved past the r74 freeze pins (`.ufo/waves/round-74/receipts/sibling-heads-freeze.tsv`),
e.g. kengaku frozen `f9efce3b` → now `3a548330`, kama `3e6fdbe9` → `2bfe5ada`, tameshi
`a944eb55` → `abae0a04`. The greps above ran on the **current working-tree bytes**, so
the zero-hit result covers post-freeze sibling drift through 2026-10-27, not just the
frozen pins.

## Boundary reasoning (§ Adjacent census, `corpus/knowledge/sibling-overlap-census-round74.md`)

The C2 surface is documentary (what the Agent SDK skills page documents about the
`allowedTools`/`allowed_tools` query-config grant and managed-settings override) — the
same footing as the r80 `allowed-tools` frontmatter matrix, which is kotoba's
"prompt & skill craft" domain (`PROVINCE.md:3`, domain line 34: "Allowed-tools surfaces
by client"). Checked against the r74 census classes and the boundary sentences kotoba's
`PROVINCE.md` § Adjacent carries:

- **kengaku (adjacent, basis mutual)** — owns "measured capability effects of prompt
  format" (kengaku SKILL.md:3; kotoba PROVINCE.md:66). The SDK grant channel is a
  *documented config surface*, not a measured capability effect: kotoba records what
  the page states (sourced, snapshot-pinned), it does not measure whether
  `allowedTools` actually restricts a run — that measurement, if ever claimed, would be
  kengaku's. No collision: the split is documentary-vs-measured, already arbitrated.
- **kama (adjacent)** — owns local model-serving endpoint identity and health; its own
  corpus assigns agent-file model/fallback wording to kotoba
  (`cross-lane-scope.md:29`; PROVINCE.md:64). The Agent SDK docs page is vendor
  documentation of a config key, not an endpoint; no collision.
- **tameshi (adjacent)** — owns the reusable fixture/mutation method; each lane's gate
  stays its own (PROVINCE.md:75). The new counter `check_sdk_allowed_tools.py` is
  kotoba's own gate; no collision.
- **kumitate (adjacent)** — routes "Prompt and skill craft → kotoba" verbatim
  (kumitate PROVINCE.md:28). The SDK allowedTools channel is prompt/skill craft
  documentation; kumitate's own surface cedes it.
- **kotodama (adjacent)** — refuses prompt/skill craft by name (SKILL.md:3).
- **kaidoku / kake / mori / others (`none` or unrelated `adjacent`)** — their only
  `sdk` bytes are Dart-AOT refusals, a Render `apps-sdk` directory, and OMP harness
  `sdk.ts` internals; their scope quotes name reverse engineering, web properties, and
  fleet observability — no skill-craft surface at all.
- **tabi** — its vendored Playwright `allowed-tools` bytes are evidence corpus, not a
  lane claim; census keeps tabi `none`.

Verdict on the assigned question: the Agent SDK `allowedTools` surface falls inside
**kotoba's own stated domain** (prompt & skill craft; the r80 allowed-tools matrix row
is already `PROVINCE.md:34` and `SKILL.md` § Allowed-tools by client), and outside every
sibling's stated domain. The closest sibling, kengaku, is split on the exact axis this
claim rides: documentary surfaces are kotoba's, measured capability effects are
kengaku's — C2 is documentary (S249 located quote, snapshot-pinned), so the r74 split
assigns it to kotoba. No boundary move is needed this round; the § Adjacent table needs
no new or amended row for C2.

## Limits

- Census rows are frozen at r74 heads; the zero-hit scan is current-tree. A sibling
  could have claimed the surface in a *non-scope* file (corpus entry, SOURCES row):
  the fleet-wide corpus/SOURCES sweep above found none — only captured data and
  vendored bytes.
- Boundary reasoning applies the census rule as committed; classification judgement is
  the reviewers' call, not re-adjudicated here.

VERDICT: STRICT_HITS 0 — no sibling SKILL.md/PROVINCE.md touches allowedTools/Agent SDK/allowed-tools; the C2 surface sits inside kotoba's prompt-&-skill-craft domain, clear of kengaku's measured-effects split.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81R04SiblingScan.md
