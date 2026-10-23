# Scout report — ScoutCopilotMoved (round-55 build wave)

Result: DONE — The old Copilot concept route still moves (no-`.md` 301 → `/en/copilot/concepts/customizations/agent-skills`; old `.md` 404), the moved `.md` page is byte-identical to the bytes the lane already holds (`ed1e2944…`, 2,622 B), the current Copilot CLI skills how-to is `…/copilot-cli/customize-copilot/add-skills` (alias `create-skills` 301s to it), and it states the explicit-name form in one byte-exact sentence (line 125), with a token-bearing example at line 128.

Scope: round-54 routed defect 4 + the session note "the Copilot docs page moved". Read-only: no lane file edited (only this report), no lane code executed, no subagents, no installs. Fetches by plain `curl` (ordinary means); no browser, no bot-challenge tooling. Scratch: `/fast/scratch/hyaku/kotoba-r55/ScoutCopilotMoved/`.

## 0. `date -u` lines (pasted, per fetch run)

```
Thu 22 Oct 2026 11:12:42 PM UTC      (concept-page fetches, A-D)
Thu 22 Oct 2026 11:13:11 PM UTC      (add-skills / create-skills fetches, E-G)
Thu 22 Oct 2026 11:13:27 PM UTC      (command-reference fetch, H)
Thu 22 Oct 2026 11:14:06 PM UTC      (docs source, I)
Thu 22 Oct 2026 11:14:07 PM UTC      (docs source, J)
Thu 22 Oct 2026 11:15:16 PM UTC      (direct HTML add-skills fetch, K; quote byte checks)
Thu 22 Oct 2026 11:15:53 PM UTC      (Accept-header status checks; wc -l)
```

Host clock is UTC-03:00 (scratch file stamps read `Oct 22 20:12`), consistent with the UTC lines above.

## 1. Route-move record (round-54 routed defect 4; for the lesson)

| # | URL (fetched exactly as written) | observed | redirect chain | final body | sha256 of final body |
|---|---|---|---|---|---|
| 1 | https://docs.github.com/en/copilot/concepts/agents/about-agent-skills.md | HTTP/2 404 | none | 502 B | `979615bad4719ae23bf76385ee60de8b1b05c785ce74497dee80ecb54c69c522` |
| 2 | https://docs.github.com/en/copilot/concepts/agents/about-agent-skills | HTTP/2 301 → 200 | `location: /en/copilot/concepts/customizations/agent-skills` | 566,002 B | `24a3779b1c6520586402ea4ea86ea710212e93018917b6ce854df950bc3c31fb` |
| 3 | https://docs.github.com/en/copilot/concepts/customizations/agent-skills | HTTP/2 200 | none | 566,002 B | `24a3779b1c6520586402ea4ea86ea710212e93018917b6ce854df950bc3c31fb` |
| 4 | https://docs.github.com/en/copilot/concepts/customizations/agent-skills.md | HTTP/2 200 | none | 2,622 B | `ed1e29440ec3aeadef2f461d1dc29910eb4014f0a1b451d8f04e73763605d4a7` |

Points a lesson record can state (all observed on rows 1-4, 2026-10-22T23:12:42Z):

- Old route → new route: `concepts/agents/about-agent-skills` 301s to `concepts/customizations/agent-skills` (row 2); the direct new route serves the same 566,002-byte HTML byte-identically (row 3, same sha256 as row 2's final hop).
- The old `.md` route is 404 with a 502-byte body (row 1), not a redirect: docs.github.com's markdown endpoint is not covered by the redirect. The new `.md` route is 200, 2,622 B (row 4).
- Row 4's sha256 `ed1e2944…` equals the bytes recorded in `corpus/lessons/round-50-verifier-spotcheck.md:188` and round-54's fetch row 5 (`SrcCopilotCLI.md` §3): the moved page itself did not change while the route moved.
- The docs source declares the move: `content/copilot/concepts/customizations/agent-skills.md` (github/docs `main`) carries `redirect_from: /copilot/concepts/agents/about-agent-skills` — 200, 3,617 B, sha256 `64d4d9c49638cd2a34b153920cf04bc72986ed5669e16df93b77c4921f35feae`, fetched 2026-10-22T23:14:06Z. Unversioned branch; corroboration only, not a pin.
- Row 4 (2,622 B) still contains no threshold language: `grep -c -iE 'descript|limit|character|truncat|1024'` → 0, exit 1. The round-54 reject reason ("no description threshold") reproduces; my bytes hold no quote for a description-threshold row.

Detail that differs from the round-54 record, recorded not resolved: `SrcCopilotCLI.md` §3 says the old route and `create-skills` "both 302-redirect". I observed HTTP/2 **301** for both, twice (23:12:42Z headers files; 23:15:53Z re-run with curl's default headers and with `Accept: text/html,application/xhtml+xml` — 301 each time). I did not measure at 21:18Z, so I claim no cause and no contradiction beyond the observed code. The round-54 closure's own row (`round-54-verifier-spotcheck.md` §5) gives no code, so it does not conflict.

Sibling move (also re-opened):

| URL | observed | chain | final body | sha256 |
|---|---|---|---|---|
| https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-skills | 301 → 200 | `location: /en/copilot/how-tos/copilot-cli/customize-copilot/add-skills` | 625,849 B | `7ea0851273a35ae4353345d4484f4635f4bb08785b7112af9e5f2b1478a376a7` |
| https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-skills.md | 404 | none | 502 B | `979615ba…` (same 404 body as row 1) |

Docs source `add-skills.md` carries `redirect_from: /copilot/how-tos/copilot-cli/customize-copilot/create-skills` (200, 3,532 B, sha256 `ef7c9bc8510426dfc13c7944ed2d7396e291623a1f8b62951c8f212b738f3baf`, fetched 23:14:07Z).

## 2. Current Copilot CLI skills pages on docs.github.com

- How-to for creating/adding/using skills: https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills — `.md` route 200, 10,057 B, sha256 `989af4981773349a74feaebfe98cdac9895b394707d201545ba55c8f9f4131a0`, 158 lines, no redirect (23:13:11Z); byte-identical to round-54's fetch row 4 at 21:18:04Z, so the page is stable across the two reads. HTML route 200, 625,849 B, sha256 `7ea08512…` (23:15:16Z, same bytes as the redirect target above).
- Concept page (the moved route): `…/concepts/customizations/agent-skills(.md)` — §1. Its "Next steps" links the CLI how-to above.
- Reference page carrying the frontmatter grammar: `…/copilot/reference/copilot-cli-reference/cli-command-reference(.md)` § Skills reference (`H:1265`, 1,944 lines) — 200, 461,944 B, sha256 `c61997efd7c939324e1f1b846fcb9ed420e5bbfd5eb5319531c6e6210025b5c9` (23:13:27Z). Byte-identical to the S031/S038/S056 pins.
- Sweep for a competing skills how-to (three checks): github/docs `main` tree of `content/copilot/how-tos/copilot-cli/` lists exactly one skills how-to, `customize-copilot/add-skills.md` (no skills file under `use-copilot-cli/`, `set-up-copilot-cli/`, `automate-copilot-cli/`); `cli-best-practices.md` mentions skills only as a "Skills exercise" link (`:505`); the concept page's own "Next steps" names only `add-skills` for the CLI. So `add-skills` is the current creating/using how-to.

## 3. Candidate quotes — invoking a named skill explicitly

All four are byte-exact substrings of the fetched bytes (`grep -c -F` → 1 each), ≤25 whitespace-separated words (`awk '{print NF}'`), no markdown stripped:

Fetched bytes E = `add-skills.md` (200, 10,057 B, sha256 `989af498…`):

- Q1 — section `## Using agent skills` (`E:119`), line `E:125`, 20 words:
  `"To tell Copilot to use a specific skill, include the skill name in your prompt, preceded by a forward slash."`
  (The same line continues: `For example, if you have a skill named "frontend-design" you could use a prompt such as:` — the example prompt is Q2.)
- Q2 — line `E:128`, inside a ```` ```copilot ```` fence (`E:127-129`), 12 words:
  `"Use the /frontend-design skill to create a responsive navigation bar in React."`
  Token: `/frontend-design`.

Fetched bytes H = `cli-command-reference.md` (200, 461,944 B, sha256 `c61997ef…`):

- Q3 — section `## Skills reference` (`H:1265`), line `H:1267`, 17 words:
  `"When invoked (via `/SKILL-NAME` or automatically by the agent), the skill's content is injected into the conversation."`
  Token: `/SKILL-NAME`.
- Q4 — frontmatter table row `user-invocable` (`H:1277`), 10 words:
  `"Whether users can invoke the skill with `/SKILL-NAME`. Default: `true`."`
  Token: `/SKILL-NAME`.

Reading (mine, for the entry/reviewer to weigh; the frozen counter does not judge it): Q1 is the how-to's own sentence for explicit invocation by skill name; Q2 is its worked example; Q3 is the reference page's grammar (`/SKILL-NAME` = a skill name with a leading slash, contrasted with automatic invocation); Q4 is the field that gates the `/` form. Q1 alone carries no `[ /$@#]`- or `_`-shaped token ("forward slash" is prose), so as a C1 quote cell it cannot carry a row by itself.

C1 grounding mechanics checked (readings of the frozen counter; [INFERENCE] on the counter's own rules):

- Tokens present in Q2/Q3/Q4 (`/frontend-design`, `/SKILL-NAME`) are new ground inputs: fixed-string `git grep -c` over `SKILL.md` and `corpus/knowledge/*.md` at BASE `f0e5de82` gives no match (exit 1) for `/SKILL-NAME`, `/frontend-design`, `copilot skill enable`, and `preceded by a forward slash`; `/SKILL-NAME` and `/frontend-design` are still absent at tip `a10240c0`. [INFERENCE: this is the counter's new-ground input; the new-ground verdict is the counter's.]
- Host pinning: rows 2-4 and E/H are on `docs.github.com`, which the counter pins for "Copilot CLI". The `raw.githubusercontent.com/github/docs` corroboration is not a pinned host and cannot be a row's first URL.
- Row state: no SOURCES row at `f0e5de82` or `a10240c0` names the CLI how-to (`git grep -F add-skills` hits only S027, the different `…/customize-cloud-agent/add-skills` page, whose teach is different). So a fresh `docs.github.com` row for `…/customize-copilot/add-skills.md` is available for Q1/Q2. The command reference already has S031 and S038 (rows at BASE) and S056 (created round 54, `docs | A | mined | 2026-10-22`, 11 cells — satisfies "not a row at f0e5de82" and "opened 2026-10-22"); reusing S056 would need ENTRY appended to its `used-by` cell and the quote recorded in the round-55 Gate. Both options exist; I edited nothing and formed no row.
- Byte-exactness for `--fetch`: Q2 is plain text (no markup). Q3/Q4 hold backticks exactly as fetched; the counter's live-page check normalizes backticks on both sides, so the token match survives either recorded form, but the entry quote and the Gate string must still be the same double-quoted string.

## 4. Limits and remaining unknowns

- 301 vs the round-54 note's "302": unresolved, no cause claimed (observed 301 twice on 2026-10-22; the earlier fetch was ~2h before, which I cannot re-measure).
- The 301 hop's own body (declared `content-length: 82`) was not saved; the hashed file is the final 200 body. The final-body byte counts in §1 are the saved files, cross-checked by `sha256sum`.
- github/docs `main` is unversioned; its bytes corroborate the redirect declarations and the sweep, they are not a pin named in any row.
- I did not check the Copilot CLI changelog for the route move (it is a docs-site change, not a CLI change), and I make no "documents nothing" statement beyond the threshold grep in §1.
- Q2's page is also the page the `--fetch` step would re-open for a row pinned on the `.md` route; that is [INFERENCE] about which URL such a row would pin, not a measurement.

Tooling: no installs, upgrades or pacman transactions; commands used: `curl`, `sha256sum`, `wc`, `grep`, `gh api` (read-only tree listings), `git grep`/`git show`/`git cat-file` (read-only in the lane).