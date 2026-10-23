Result: HOLDS — SOURCES row S071 and all four of its uses at tip `f0e6b695` are grounded in the live page (refetched byte-identical), with one minor imprecision in the SKILL.md what-it-does cell (`autoinvoke: false` vs the documented `opencode/autoinvoke` key) and lane-drift notes below.

Scope: row S071 (opencode) and its uses; judged at tip `f0e6b695b746775823b65a8c45de7d50ea33e84f`. Read-only; no lane file edited; no tool installed; no subagent spawned; no lsp server applies (docs review, no code surface).

## Refetch (my own)

```
Fri 23 Oct 2026 12:10:53 AM UTC          (2026-10-23T00:10:53Z, within the counter's OPENED window days)
curl -sS -w 'HTTP %{http_code} downloaded %{size_download} bytes\n' -o s071.mdx \
  'https://raw.githubusercontent.com/anomalyco/opencode/3d213123cdf574e55f88711554edfe6fd66a95ad/services/www/src/docs/content/skills.mdx'
→ HTTP 200 downloaded 9187 bytes; sha256
  931b5425fffc7339913327fbd5f54416397d664311407eeaaae9e349300da27b
```

Byte-identical to the row's fetch record (`corpus/SOURCES.md:84`), the lesson Gate row (`corpus/lessons/round-55.md:20`), and seat `.ufo/waves/round-55/build/Srcopencode.md`. Host pin: `raw.githubusercontent.com/anomalyco/opencode` is in the frozen `HOSTS["opencode"]` (`verifiers/check_explicit_invocation.py:124-137`); the next path segment is the 40-hex commit (no `.`/`..`), so the pin rule is met.

## Cell verdicts (all at tip `f0e6b695`)

**Lesson Gate quote — HOLDS.** `"To load a skill yourself, mention it in your prompt as @skill-id."` is on my fetched bytes at line 201 (`grep -n` → `201:To load a skill yourself, mention it in your prompt as \`@skill-id\`.`), byte-exact after only the stated normalisation (the inline backticks around `@skill-id`, which the counter's page normalisation also drops — disclosed in the Gate row, the entry location cell, and `lessons/round-55.md:22-23`); my backtick-strip + whitespace-collapse substring check returned True. 12 words, holds the token verbatim, holds the word `skill`; opened/bytes/sha match the refetch.

**SOURCES `teaches` cell — HOLDS.** 22 words (≤25). Clause 1 "lets a user load a skill by mentioning `@skill-id` in the prompt" = page :201. Clause 2 "the model loads skills through the `skill` tool" = page :186 "The model loads a skill by calling the `skill` tool with its exact ID" (also :21). Row: 11 cells (awk NF−2), tier `A`, kind `docs`, status `mined`, opened `2026-10-22`, used-by names the entry and the lesson. Location cells verified: quote `:201`, model tool call `:186`, frontmatter sentence `:142`. Not a row at base: `git show f0e5de82…:corpus/SOURCES.md | grep -c S071` → 0.

**Entry row (`corpus/knowledge/explicit-invocation-round55.md:28`) — HOLDS.** Quote string is md5-identical to the Gate quote. Reading cell: "A user mention of the skill's ID loads it" (:201) and "`opencode/autoinvoke: false` hides it from the model's list but keeps this path (`:142`)" (:142 "`opencode/autoinvoke: false` only hides the skill from the model's available list. The skill remains registered and can still be loaded explicitly by ID." — 23 words). Nothing over-wide.

**SKILL.md row (tip `:205`; header `| Client | Explicit form | What it does | Action |`) — HOLDS, with one minor finding.**
- Form `` `@skill-id` ``: matches frozen `TOKEN_RE` (`@` + letter + `[A-Za-z0-9<>_-]`), sigil-stripped `skill-id` is not in `BUILTINS`, verbatim in the quote, recorded in the Gate.
- What it does: substance grounded (:201 load; :142 hide-from-model + keep manual path). **Minor finding:** the cell writes "the `autoinvoke: false` metadata key", but the page documents the key as `` `metadata.opencode/autoinvoke` `` (:137) / `opencode/autoinvoke: false` (:142); the same round's entry and SOURCES cells, and SKILL.md:431 (`metadata["opencode/autoinvoke"]`), all use the full name. As frontmatter, `autoinvoke: false` is not the documented spelling (the page models it as a `metadata` sub-key). Precision defect only — not over-wide, no counter effect (the counter reads the form cell, not this one).
- Action: "prompt holds `@` plus a skill ID" grounded as classifier (:201); "the model's own `skill` tool calls are the implicit ones" is a reading the frozen counter explicitly does not judge (docstring, Q31), and the page anchors it: the model-facing list is description-driven (:184), the model loads via the `skill` tool (:186), and the page itself calls only the user path "explicitly" (:142). "Own" correctly scopes out tool calls prompted by a user mention. Entry Finding 4 further bounds mechanism-vs-origin. HOLDS.

Counter-rule conformance (for the record): the row satisfies every frozen backing condition I can check statically — new row (not at base), 11 cells with the required enums, pinned host, quote 3–25 words holding the token, Gate-recorded verbatim, token new at base (`git grep skill-id f0e5de82 -- SKILL.md corpus/knowledge` → none).

## Findings by severity

1. **Minor** — SKILL.md what-it-does cell abbreviates the documented key to `autoinvoke: false` (evidence above). Suggested repair (integration seat's call): widen to `opencode/autoinvoke: false`.
2. **Info (drift)** — the lane has moved under me: HEAD is now `722e474` ("SCORECARD and LOG entries, C2 declared measurement receipt"), and the working tree carries uncommitted edits to `SKILL.md` and `corpus/knowledge/explicit-invocation-round55.md`. The worktree SKILL.md opencode row gains a "V2 docs:" prefix and "; the V1 page states loading by exact name only" (absent at tip `f0e6b695`). I verified the added clause against a fresh fetch of the V1 page (S059's URL): `Fri 23 Oct 2026 12:15:00 AM UTC`, HTTP 200, 5,365 B, sha256 `f10ced73971ce83b85f41395e2e15a683fe5a874e9057fc9d13da5f5a1bf8561` (matches the seat's record); V1 :129 "They can still be selected manually and loaded by exact name." with autoinvoke-exclusion at :128 — clause supported. SOURCES and lesson bytes are identical tip↔worktree; the tip entry row :28 equals the worktree row I quoted.
3. None material otherwise: no over-wide phrase found in any S071 cell (Q31/Q26 clean).

## Residual risk / verification gaps

- I did not run `check_explicit_invocation.py` itself: wave bounds put counter execution in a sandbox and the counter re-run is seat W2RerunC1's item; my `--fetch`-relevant check (quote substring after the stated normalisation) was reproduced manually on my own fetched bytes.
- The SOURCES note "the served V2 page carries the same sentence" rests on the seat's fetch of `https://opencode.ai/v2/docs/skills` (HTML line 289, sha `243e8890…`); I re-opened the row's own URL, not the served page. [INFERENCE from seat record, not my observation]
- Verdicts are for tip `f0e6b695` bytes; the uncommitted worktree edits (finding 2) will change the SKILL.md row text if integrated as-is (the change is an improvement; the minor key-name finding survives it).
