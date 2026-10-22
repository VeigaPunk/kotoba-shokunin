# SrcCodex — round-51 C2 source seat (client: Codex)

Result: HOLDS — the Codex skills page is fresh (markdown bytes re-fetched 2026-10-22T14:22:21Z are byte-identical to the revision S021 records) and it documents four levers other than description wording that take a skill out of the model's choice; the best lever for the table is `allow_implicit_invocation`, and the drafted rows were dry-run against the delivered verifier and come out `BACKED Codex` with the quote found on the live page.

## Fetch evidence (ordinary means: `curl -sSL`)

| variant | URL | UTC access | HTTP | bytes | sha256 |
|---|---|---|---|---|---|
| markdown (used for every quote below) | `https://learn.chatgpt.com/docs/build-skills.md` | 2026-10-22T14:22:21Z | 200, `text/markdown; charset=utf-8` | 11,035 (232 lines) | `ed6e324f747d47adf6f60ee1fca13ba469b3671f55f58c3a78f35947af6919d5` |
| html | `https://learn.chatgpt.com/docs/build-skills` | 2026-10-22T14:22:21Z | 200, `text/html; charset=utf-8` | 417,112 | `b794ed62e3630f52029575a3643c486deb7e9ab6a16b4e6fee840c2be749b955` |
| legacy entry point | `https://developers.openai.com/codex/skills` | 2026-10-22T14:19Z | 308 → `https://learn.chatgpt.com/docs/build-skills` → 200 | — | — |

Which variant: the site serves markdown by appending `.md` (the page says so: "Markdown versions of documentation pages are available by appending `.md` to the page URL." — `build-skills.md:3`). All quotes and line numbers below are line numbers in the **markdown** bytes (`build-skills.md`, 232 lines), the same unit S021 already uses.

Freshness: the markdown sha256 equals the revision S021 records (`ed6e324f…`, 11,035 B, 232 lines) and the round-47 fetch, so the content did not move. The HTML `Last-Modified` did move (`Thu, 22 Oct 2026 14:01:49 GMT`, against the `2026-10-21T15:05:00Z` recorded in S013) — page chrome moves, text does not. S021's `recheck` of `90d` can stay; the pin was re-checked today.

Caveat on the assignment's hint: the "disabled" hits at HTML lines 41 and 54 are page chrome (`:disabled` in CSS, `aria-disabled="false"` on a select trigger), not content. The markdown uses "disable" twice.

## Levers this client documents (all on this one page)

| # | key term (code token) | what it does | where it is set | located verbatim quote |
|---|---|---|---|---|
| 1 | `allow_implicit_invocation` | keeps the model from ever picking the skill on its own; the user can still invoke it explicitly | per-skill metadata file `agents/openai.yaml`, under `policy:` | "`allow_implicit_invocation` (default: `true`): When `false`, Codex won't implicitly invoke the skill based on user prompt; explicit `$skill` invocation still works." (`build-skills.md:218`, 20 words) |
| 2 | `enabled = false` (inside `[[skills.config]]`) | disables the skill outright for that Codex install, without deleting it | settings file `~/.codex/config.toml` | "Use `[[skills.config]]` entries in `~/.codex/config.toml` to disable a skill without deleting it:" (`build-skills.md:183`, 12 words) |
| 3 | `[[skills.config]]` | the TOML table that carries lever 2, with `path = "/path/to/skill/SKILL.md"` and `enabled = false` | settings file `~/.codex/config.toml` | "`[[skills.config]]`" (`build-skills.md:186`, TOML block) / "enabled = false" (`build-skills.md:188`) |
| 4 | `.agents/skills` | scopes by path: Codex scans it from the working directory up to the repository root, so a skill placed in a narrower scope is not offered outside it | directory location of the skill folder | "Codex scans `.agents/skills` in every directory from your current working directory up to the repository root." (`build-skills.md:138`, 16 words) |

Two weaker levers, listed for completeness and not for the table: `skills.max_context_tokens` (`build-skills.md:43`) changes the initial-list budget, and over budget "Codex may omit some skills from the initial list and show a warning." (`build-skills.md:41`, 14 words) — that removes skills from the offer as a side effect of crowding, not as a targeted per-skill lever.

## Does the page say anything about choosing BETWEEN two matching skills?

No. `grep -niE 'overlap|conflict|precedence|disable|deny|permission|hidden|invocation' build-skills.md` returned 7 lines (exit 0): md:95, md:98, md:181, md:183, md:195, md:207, md:218 — every one of them is lever text already listed above; nothing more was found. Per-term counts on the markdown: `overlap` 0, `conflict` 0, `precedence` 0, `deny` 0, `permission` 0, `hidden` 0, `disable` 2, `invocation` 5.

The nearest the page comes to a selection rule is the description-keyed matching S021 already records ("Implicit invocation: ChatGPT or Codex can choose a skill when your task matches the skill `description`." — md:98-99) and the authoring advice "Because implicit matching depends on `description`, write concise descriptions with clear scope and boundaries." (md:101-102). The one collision statement is about names, not matches: "If two skills share the same `name`, Codex doesn't merge them; both can appear in skill selectors." (md:138). "Keep each skill focused on one job." (md:222) is authoring advice, not a runtime rule.

**Bound (as the assignment requires):** levers 1–4 take a skill out of the choice or out of the client's load; none of them is a documented tie-break between two matching skills. The page does not say otherwise — it documents no rule at all for choosing between two skills whose descriptions both match.

## Drafts for the C2 integrator

### (a) `SKILL.md` § Anti-patterns — "Overlap levers by client" table row

The table must live inside the `## Anti-patterns` section (the verifier blanks HTML comments and fenced blocks and stops at the next `## ` heading), and the delivered counter's header is six columns: `| client | lever | held by | effect | row | key term |`, with `held by` one of `skill author` / `user or operator` / `app developer` and `effect` one of `removed everywhere` / `automatic choice off` / `outside a scope`.

```
| Codex | Turn off implicit invocation for that skill so the model never picks it; explicit use still works | skill author | automatic choice off | S021 | `allow_implicit_invocation` |
```

Why this lever: it is the only one of the four that stops the *model's* choice while leaving the skill usable, it is per-skill and ships with the skill (`agents/openai.yaml`), and it is in the counter's pinned `REVIEWED_LEVERS["Codex"]` (`allow_implicit_invocation`, `enabled = false`, `enabled`). The harsher alternative, if the table prefers removal over choice, is:

```
| Codex | Disable that skill for this Codex install, in the user's own config | user or operator | removed everywhere | S021 | `enabled = false` |
```

Its matching entry row (quote "`enabled = false`", `build-skills.md:188`, 3 words, verbatim at byte offset 9213):

```
| Codex | S021 | Disable that skill for this Codex install, in the user's own config | "`enabled = false`" (build-skills.md:188) |
```

### (b) `corpus/knowledge/skill-overlap-levers-round51.md` — "## Levers by client" table row

Header: `| client | row | lever | quote |`; the quote cell must start with a double-quoted string followed by a parenthesised location, be at most 25 words, and contain a backticked code span exactly equal to the key term.

```
| Codex | S021 | Turn off implicit invocation for that skill so the model never picks it; explicit use still works | "`allow_implicit_invocation` (default: `true`): When `false`, Codex won't implicitly invoke the skill based on user prompt; explicit `$skill` invocation still works." (build-skills.md:218) |
```

The quote is 20 words, contains the code span `allow_implicit_invocation`, contains no `"` and no `|`, and is a verbatim raw substring of the fetched markdown bytes at offset 10085.

### (c) `corpus/SOURCES.md` — S021 cell edits (no new row needed)

S021 already exists, has status `mined`, kind `docs`, tier `A`, and its first https URL (`https://learn.chatgpt.com/docs/build-skills`) is under the counter's pinned Codex prefix `https://learn.chatgpt.com/docs/`. S013 is still `queued` with `used-by` `—`, so S013 cannot satisfy the counter. The counter also needs S021 named in `corpus/lessons/round-51.md` under its `## Gate` section. Exact cell texts, old -> new (fenced so they copy byte-exactly; none contains a pipe):

`scope`

old:
```
Documented Codex and ChatGPT skill-list budget and implicit invocation (vendor documentation, not a measurement of omp or opencode)
```
new:
```
Documented Codex and ChatGPT skill-list budget, implicit invocation, and the per-skill levers that keep a skill out of the model's choice (`allow_implicit_invocation`) or out of the client entirely (`[[skills.config]]` with `enabled = false`) (vendor documentation, not a measurement of omp or opencode)
```

`anchor`

old:
```
page intro md:37-40 (budget, shortening, may omit skills); md:43-44 override; § How ChatGPT and Codex use skills md:91, implicit-invocation bullet md:98-99; revision = build-skills.md sha256 `ed6e324f…` (11,035 B, 232 lines), fetched 2026-10-22T08:13:33Z, byte-identical to the round-47 fetch while the HTML Last-Modified moved
```
new:
```
page intro md:37-40 (budget, shortening, may omit skills); md:43-44 override; § How ChatGPT and Codex use skills md:91, implicit-invocation bullet md:98-99; § Enable or disable local Codex skills md:181-191 (`[[skills.config]]`, `enabled = false`); § Optional metadata md:193-218 (`policy.allow_implicit_invocation`, yaml at md:206-207, definition at md:218); § Where Codex loads local skills md:136-149 (scope rows, `.agents/skills` at md:138); revision = build-skills.md sha256 `ed6e324f…` (11,035 B, 232 lines), fetched 2026-10-22T08:13:33Z and re-fetched 2026-10-22T14:22:21Z, byte-identical to the round-47 fetch while the HTML Last-Modified moved
```

`teaches`

old:
```
supersedes S013 — by default Codex's initial skill list uses at most 2% of the context window, or 8,000 characters when the window is unknown, may omit skills and shortens descriptions first; `skills.max_context_tokens` overrides it (up to 10,000 tokens); implicit invocation is stated for ChatGPT or Codex and keys on the description
```
new:
```
supersedes S013 — by default Codex's initial skill list uses at most 2% of the context window, or 8,000 characters when the window is unknown, may omit skills and shortens descriptions first; `skills.max_context_tokens` overrides it (up to 10,000 tokens); implicit invocation is stated for ChatGPT or Codex and keys on the description; a skill can be kept out of the model's choice with `policy.allow_implicit_invocation: false` in its `agents/openai.yaml` (explicit `$skill` still works) and can be removed from the client with `[[skills.config]]` `enabled = false` in `~/.codex/config.toml`
```

`used-by`

old:
```
corpus/knowledge/frontmatter-rule-authorities-round48.md
```
new:
```
corpus/knowledge/frontmatter-rule-authorities-round48.md, corpus/knowledge/skill-overlap-levers-round51.md
```

Leave `status` (`mined`), `kind` (`docs`), `tier` (`A`), `opened` (`2026-10-22`) and `recheck` (`90d`) unchanged.

## Dry run against the delivered counter (evidence that the drafts pass)

The counter `verifiers/check_overlap_levers.py` was delivered by the `LeverGuard` seat and has since grown past its first patch (the SKILL.md table is now six columns with `held by` and `effect`, and the lesson `## Gate` is checked). The rows drafted above were dry-run in a scratch world (`/fast/scratch/hyaku/kotoba-r51/build/SrcCodex/world`, the real SOURCES.md with only S021's `used-by` changed, one fake row for each of the other six clients):

- `python3 -B /fast/scratch/hyaku/kotoba-r51/build/LeverGuard/lane/verifiers/check_overlap_levers.py --root world` → `BACKED Codex`, `overlap levers backed 1 of 7 clients`, exit 1 (the other six are fake rows with no registry row, so they are correctly unbacked).
- the same command with `--fetch` → `FETCH Codex: quote found (https://learn.chatgpt.com/docs/build-skills)`, `quotes found on live pages 1 of 1`, exit 1.
- the same world rebuilt with the fallback rows (`world2`: key term `enabled = false`, quote "`enabled = false`" at md:188) → `BACKED Codex` and `FETCH Codex: quote found`, exit 1 for the six fake clients. Both candidate levers pass the counter.

So the Codex row, the entry row and the S021 `used-by` edit are consistent with the counter as delivered; what is still missing for Codex is the `## Gate` mention of S021 in `corpus/lessons/round-51.md` (a lesson file this seat does not own).

## Out of scope / not done

- No lane file was edited except this report; no product code, no registry row, no knowledge entry was written by this seat.
- No other Codex page (config reference, permissions) was opened: that is the `LeverOtherPages` scout's item; this seat answers for `build-skills` only.
- No tool was installed or upgraded; no subagent was dispatched; no peer message was sent.

## Evidence (commands and exit codes)

- `curl -sSL -o build-skills.md https://learn.chatgpt.com/docs/build-skills.md` → exit 0, status 200, 11,035 bytes, sha256 `ed6e324f747d47adf6f60ee1fca13ba469b3671f55f58c3a78f35947af6919d5` (2026-10-22T14:22:21Z).
- `curl -sSL -o codex-skills.html https://learn.chatgpt.com/docs/build-skills` → exit 0, status 200, 417,112 bytes, sha256 `b794ed62e3630f52029575a3643c486deb7e9ab6a16b4e6fee840c2be749b955`.
- `curl -sSIL https://developers.openai.com/codex/skills` → exit 0, `HTTP/2 308`, `location: https://learn.chatgpt.com/docs/build-skills`, then `HTTP/2 200`, `last-modified: Thu, 22 Oct 2026 14:01:49 GMT`, `content-length: 417112`.
- `grep -niE 'overlap|conflict|precedence|disable|deny|permission|hidden|invocation' build-skills.md` → exit 0, 7 lines (md:95, 98, 181, 183, 195, 207, 218).
- per-term counts → `overlap` 0, `conflict` 0, `precedence` 0, `deny` 0, `permission` 0, `hidden` 0, `disable` 2, `invocation` 5.
- quote offsets/word counts against the fetched bytes: md:218 offset 10085 (20 words), md:207 offset 9844 (2 words), md:183 offset 9055 (12 words), md:188 offset 9213 (3 words), md:41 offset 1845 (14 words), md:138 offset 4793 (28 words, so the quoted 16-word half is used).
- drafted cell texts checked against the live registry row: all four `old` texts equal the current S021 cells byte-for-byte; no `new` text contains a pipe (the registry table stays 11 columns).
- dry run of the delivered counter: `--root world` → `BACKED Codex` (exit 1, other six fake); `--root world --fetch` → `FETCH Codex: quote found` (exit 1, other six fake); `--root world2 --fetch` (fallback `enabled = false` rows) → `BACKED Codex`, `FETCH Codex: quote found` (exit 1, other six fake).

Report: .ufo/waves/round-51/build/SrcCodex.md
