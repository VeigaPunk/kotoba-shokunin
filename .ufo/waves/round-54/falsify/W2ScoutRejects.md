Result: HOLDS — all three reject reasons in `corpus/lessons/round-54.md` § Gate → Rejected (lines 40-42, identical at `5a097e12` and tip) are reproduced by fresh fetches; the reject decisions stand, with three record-calibration defects in the reject table that change no decision.

Seat: `KotobaR54.W2ScoutRejects` (scout, round-54 falsify wave). No lane edits; all fetches in
`/fast/scratch/hyaku/kotoba-r54/W2ScoutRejects/fetch/`; sandbox clone at `58db81c4` created but not used
(no code run needed). No installs, no paid model calls, no browser.

## Fetch records (ordinary `curl`, host clock UTC, no browser)

| # | URL | UTC | HTTP | bytes | sha256 | note |
|---|---|---|---|---|---|---|
| 1 | `https://docs.github.com/en/copilot/concepts/agents/about-agent-skills.md` (the rejected URL) | 2026-10-22T21:52:06Z | 404 | 502 | `979615bad4719ae23bf76385ee60de8b1b05c785ce74497dee80ecb54c69c522` | text/html; body is GitHub Docs' "Page not found." page |
| 1b | same URL, refetch | 2026-10-22T21:54:33Z | 404 | 502 | `979615bad4719ae23bf76385ee60de8b1b05c785ce74497dee80ecb54c69c522` | identical bytes |
| 2 | `https://docs.github.com/en/copilot/concepts/agents/about-agent-skills` (no `.md`) | 2026-10-22T21:52:09Z | 301 → 200 | 566,002 | `24a3779b1c6520586402ea4ea86ea710212e93018917b6ce854df950bc3c31fb` | 1 redirect, effective `.../concepts/customizations/agent-skills` |
| 3 | `https://docs.github.com/en/copilot/concepts/customizations/agent-skills.md` | 2026-10-22T21:52:42Z | 200 | 2,622 | `ed1e29440ec3aeadef2f461d1dc29910eb4014f0a1b451d8f04e73763605d4a7` | text/markdown, 41 lines; **same bytes/sha as seat `SrcCopilotCLI` row 5 at 21:24:08Z** |
| 4 | `https://cursor.com/changelog.md` (the rejected URL) | 2026-10-22T21:52:09Z | 200 | 186,629 | `939ff9cfe69790923b557a276b5e42063201737590934c12d7d81f7b7689eee7` | text/html |
| 4b | same URL, refetch | 2026-10-22T21:56:31Z | 200 | 186,633 | `42379a9c77b588ded15c490cd863462c621ae61fd5d5ad5e29dba21b0321a70a` | bytes move (4 B in 4 min) |
| 5 | `https://cursor.com/changelog` (no `.md`) | 2026-10-22T21:52:32Z | 200 | 204,106 | `ccadc4b62919ac11c68453448c5df77aae26585717a28533cfd6daf99c694f78` | text/html, server-rendered entry headings present |
| 6 | `https://cursor.com/docs/release-notes.md` | 2026-10-22T21:52:32Z | 200 | 301,193 | `fd4d830aa5b02cd79d4c3ac485eb01d31ebb7436f152e27496e7cb02a23d82cd` | text/markdown; **identical to S058's record** |
| 7 | `https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference.md` | 2026-10-22T21:52:17Z | 200 | 47,200 | `d0d362cc5aa2ef84775145e499596c7e6529531c7b29972ae29f547b5da220d0` | text/markdown, 471 lines |
| 7b | same URL, refetch | 2026-10-22T21:56:31Z | 200 | 47,200 | `d0d362cc5aa2ef84775145e499596c7e6529531c7b29972ae29f547b5da220d0` | identical; also identical to S028 (`12:31:51Z`) and seat row 6 (`build/SrcCopilotCLI.md:36`, `21:16:34Z`) |
| 8 | `https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference.md` | 2026-10-22T21:52:17Z | 200 | 461,944 | `c61997efd7c939324e1f1b846fcb9ed420e5bbfd5eb5319531c6e6210025b5c9` | text/markdown; **identical to S056's record** |

Commands were `curl -sS -L --max-time 60 -A '<UA>' -o <file> -w 'STATUS=%{http_code} BYTES=%{size_download} TYPE=%{content_type} EFFECTIVE=%{url_effective} REDIRECTS=%{num_redirects}\n' <url>` followed by `sha256sum` and `wc -c`; a `date -u +%Y-%m-%dT%H:%M:%SZ` stamp was printed immediately before and after each fetch (the pair spans at most one second; the stamp shown in the table is the start). The redirect status without `-L` was captured twice, with a browser UA and with the lane's `Mozilla/5.0 kotoba-research/54` UA: `FIRST_STATUS=301 REDIRECT_URL=https://docs.github.com/en/copilot/concepts/customizations/agent-skills` (21:52:58Z and 21:54:33Z).

## Reject 1 — `docs.github.com/.../about-agent-skills.md` ("HTTP 404, 502 B: no page at that route, so nothing to quote")

**HOLDS**, and the operative conclusion is stronger than the record states: the live concept page carries no number at all.

- The named `.md` URL is 404 with exactly 502 B and a stable sha (`rows 1, 1b`); the body says "Page not found." and nothing else. The documented reason's first clause reproduces byte for byte.
- The concept page is not gone: the same path without `.md` 301-redirects to `/en/copilot/concepts/customizations/agent-skills` (200), and the canonical `.md` returns 2,622 B, the same bytes the round-54 seat `SrcCopilotCLI` had already fetched at 21:24:08Z (`build/SrcCopilotCLI.md:35` row 5; its route note at `:42` explains the redirect). So the seat was not missing the page.
- The live page cannot back a C1 row: `grep -o -E '[0-9]+'` on the 2,622-byte markdown returned no output (zero digits in the whole page), and `grep -o -i -E 'description|frontmatter|1024|1,024|characters|limits'` on the same file returned no output. The rendered HTML route likewise has 0 occurrences of `1024` (`grep -c` → `0`, exit 1) and of `characters` (`grep -c -i` → `0`, exit 1). "Nothing to quote" is correct on the strongest reading.
- **Calibration defect D1 (record, not decision):** the reason says "no page at that route", which is true only of the `.md` URL; the concept page exists at the renamed path. And the flip cell "a live route for the concept page" was already satisfied by the time the lesson was committed (`5a097e12`, committer time 2026-10-22T21:38:22Z; the seat's own row 5 fetch is 21:24:08Z). A stricter record would read: reason "no markdown page at the stale path (404, 502 B), and the live concept page (2,622 B, sha `ed1e2944…`) states no numeric skill-description limit"; flip "a concept page that states a numeric skill `description` limit".
- Minor unexplained: `build/SrcCopilotCLI.md:42` records the pre-redirect path as a **302**; I observed **301** twice today. Not claim-bearing (the lesson row records no code), but the 302 is not reproducible.

## Reject 2 — `cursor.com/changelog.md` ("served HTML with 0 bytes of 'skill'; the skill-limit sentence is on `release-notes.md:122` (S058) instead, so this route would record a false silence")

**HOLDS**, on both clauses.

- Route bytes: 200, text/html, 186,629 B, sha `939ff9cf…`; a refetch four minutes later is 186,633 B, sha `42379a9c…` — the bytes move, corroborating the round-53 spot-check (`corpus/lessons/round-53-verifier-spotcheck.md:161`: 186,579 B "Next.js shell").
- `grep -c -i 'skill' cursor-changelog-md.html` → `0`, exit 1, on both copies; the search covers the full bytes including script payloads.
- The route is an app shell: after stripping `<script>`/`<style>`/tags (Python `re`, run in the seat scratch), the visible text is 77 characters, only the page title `Cursor - The best way to code with AI`. Entry names appear 0 times each ("canvas", "marketplace", "remote control"); the only matches in the whole 186,629 bytes are "Cloud Agent" ×1 and "Environment" ×2, against 35 `self.__next_f` markers in the `/changelog` route. So this URL carries no changelog entries at all, and a silence recorded from it would indeed be false.
- The number is where the record says: `cursor.com/docs/release-notes.md:122` (200, 301,193 B, sha `fd4d830a…`, byte-identical to S058), inside `## v2026.10.08` (`:110`) → `### Skills` (`:120`): "- **`/skills` flags skills that break the Agent Skills limits.** … a description over 1,024 characters …". The rejected route's flip is about a route property, not this sentence.
- **Calibration defect D2 (record, not decision):** the flip "server-rendered changelog entries" is already true at `https://cursor.com/changelog` (no `.md`; fetch-table row 5: 204,106 B, server-rendered `<h1>`/`<h2>` entries, still zero `skill` matches on a case-insensitive grep of the fetched bytes). The flip cannot distinguish "revisit" from "already checked and still silent"; it should be content-based: "a changelog entry that states a skill `description` limit". The reject itself remains right: the client documents the number on a different route, so a changelog sweep that stopped here would mislabel Cursor silent.

## Reject 3 — Copilot CLI plugin reference, `cli-plugin-reference.md:195,349` "Max 1024 chars" ("the caps are on plugin manifest and marketplace metadata, not on a skill's `description`; admitting them would count a number in another sense")

**HOLDS**, exactly as recorded.

- Page reproduces the admitted byte record: 200, 47,200 B, 471 lines, sha `d0d362cc…`, identical on two fetches today and to S028 (`corpus/SOURCES.md:41`, opened 2026-10-22T12:31:51Z) and to seat row 6 (`build/SrcCopilotCLI.md:36`).
- `grep -n '1024'` → exactly two lines, both plugin fields:
  - `:195` under `### Legacy manifest fields` (`:183`) → `#### Optional metadata fields` (`:191`): "| `description` | string | Brief description. Max 1024 chars. |" — a `plugin.json` manifest description.
  - `:349` under `## marketplace.json` (`:286`) → `### marketplace.json fields` (`:332`) → `#### Plugin entry fields (objects within the `plugins` array)` (`:343`): "| `description` | string | No | Plugin description. Max 1024 chars. |" — a marketplace plugin-entry description.
- No skill cap exists on this page: every `skill` line is a path, location or precedence rule (`:28, :62, :109, :130, :145, :148, :212, :360, :405, :413-417, :447-456`); the skill cap is on the other page, `cli-command-reference.md:1274` under `### Skill frontmatter fields` ("What the skill does and when to use it. Max 1024 characters."), whose bytes match S056 (`c61997ef…`).
- Why the reject is load-bearing rather than cosmetic: S028 is tier A, kind `docs`, status `mined`, opened 2026-10-22 on `docs.github.com` — so the frozen C1 counter would accept a quote of `:195`/`:349` as Copilot CLI's number if the entry were added to S028's `used-by` cell (an allowed in-place change) and the quote were recorded in the lesson Gate, because the counter does not test what object the number limits (`plans/round-54.md` erratum 3; `verifiers/check_description_thresholds.py` docstring rule list). The reject is the only thing keeping a plugin-metadata cap out of the Copilot CLI row. The entry row correctly cites S056 instead (`corpus/knowledge/skill-listing-thresholds-round54.md` § Per-client record, Copilot CLI).

## Cross-cutting calibration notes

- Two of the three flip cells ("a live route for the concept page"; "server-rendered changelog entries") describe route states that already hold, so they cannot mark a future revisit; only the plugin-reference flip is a content test. The reject decisions are unaffected, but the flip column does not do the work it appears to do. Suggested replacement text, in order: "a concept page that states a numeric skill `description` limit"; "a changelog entry that states a skill `description` limit"; unchanged for the plugin reference.
- The record's "0 bytes of 'skill'" is an occurrence statement (0 occurrences, hence 0 bytes of the token); no defect, but "0 occurrences" is the precise form.
- Not verified, stated as unknown: whether the docs.github.com path rename predates the L1's 21:06Z screen (only the 21:52Z/21:54Z 404s are mine); why the rename redirect answers 301 when the seat recorded 302; whether cursor's changelog app renders skill entries with JavaScript enabled (a browser is forbidden by the bounds, so this stays unmeasured).
- No admitted client row is missing a number because of these rejects: the live concept page has zero digits, the changelog route has zero "skill" bytes, and the plugin caps are plugin-level.

Remaining unknowns are the three listed above; confidence is high for every verdict (each source either reproduced byte for byte or was refetched to the same hash, and the plugin reference matched four independent fetches: S028's `12:31:51Z`, seat row 6's `21:16:34Z`, and my two).
