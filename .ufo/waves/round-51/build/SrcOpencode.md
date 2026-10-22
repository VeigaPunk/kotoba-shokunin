# SrcOpencode — round-51 build, C2 source (frontier step), client: opencode

**Result: HOLDS — opencode's skills page documents four levers other than description wording that take a skill out of the model's choice or out of loading (`permission.skill` = `deny`/`ask` with name patterns, `metadata["opencode/autoinvoke"]: "false"`, `tools: skill: false`, `opencode/slash` user invocation), and documents no tie-break between two matching skills; the best single lever for the C2 table is the permission block's `deny` value.**

Lane kotoba-shokunin at `43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10`. Only lane file written: this report. No `git`/`jj` write in the lane, the fleet repo or a sibling lane; no tool installed or upgraded (curl, python3, git already present); no pacman transaction. Scratch: `/fast/scratch/hyaku/kotoba-r51/build/src-opencode/`.

## Fetch record (fresh, this round; ordinary `curl -sSL`, no bot gate, exit 0)

I quote from the `.md` variant (the site serves the page body as markdown; the HTML route is the same body plus site chrome). Line numbers below are lines in these fetched bytes (230 lines).

| route | HTTP | bytes | sha256 | accessed (UTC) |
|---|---|---|---|---|
| `https://opencode.ai/docs/skills.md` (used) | 200, `text/plain; charset=utf-8` | 5365 | `f10ced73971ce83b85f41395e2e15a683fe5a874e9057fc9d13da5f5a1bf8561` | 2026-10-22T14:19:12Z (byte-identical to the 14:18Z fetch) |
| `https://opencode.ai/docs/skills` | 200, `text/html` | 73201 | `4d96fa569dd25469e085b3743ee7e5a53263792fb919b7591bd7b8397a3404f0` | 2026-10-22T14:19:02Z |
| `https://opencode.ai/docs/config.md` (lead) | 200 | 26060 | `fe28a438a1464cb5a43231a7af56f2ed16b019016731052ddfc2ae86fd54cda8` | 2026-10-22T14:20:51Z |

Freshness: these `.md` bytes are **byte-identical to the pin already on S024** (`f10ced73…`, 5365 B) and to the two round-50 fetches (12:28:29Z, 12:31:20Z) — no drift in ~2 h.

## The documented levers (key token → effect → where set → located quote)

| # | key term | effect | where it is set | located verbatim quote |
|---|---|---|---|---|
| 1 | `deny` (value of `permission.skill`) | **permission deny** — skill hidden from the agent, load rejected; wildcards ok (`internal-*`) | `opencode.json` (`"permission": {"skill": {...}}`); per agent `agent.<name>.permission.skill`; agent frontmatter `permission.skill` | "Check permissions—skills with `deny` are hidden from agents" (`skills.md:230`); table row "Skill hidden from agent, access rejected" (`skills.md:153`) |
| 2 | `ask` (value of `permission.skill`) | user prompt before the skill loads | same three places as `deny` | "User prompted for approval before loading" (`skills.md:154`) |
| 3 | `opencode/autoinvoke` | **hides from the model** — left out of `<available_skills>`, so the model never sees it; still loadable manually by exact name | skill frontmatter `metadata:` map (value `"false"`) | "keep the skill out of model-facing auto-selection guidance" (`skills.md:45`); "They can still be selected manually and loaded by exact name." (`skills.md:129`) |
| 4 | `skill: false` (in the `tools:` block) | **disables entirely** — skill tool off for that agent, `<available_skills>` omitted | agent frontmatter `tools:`; `opencode.json` `agent.<name>.tools` | "When disabled, the `<available_skills>` section is omitted entirely." (`skills.md:219`); the token itself at `skills.md:201` |
| 5 | `opencode/slash` | **user-only invocation** — exposes the skill as a `/name` TUI command (pairs with #3) | skill frontmatter `metadata:` map (value `"true"`) | "set to `\"true\"` to expose the skill as a `/name` command in the TUI" (`skills.md:44`) |

Setting shape, from the page's own JSON (`skills.md:138-148`): `"permission": { "skill": { "*": "allow", "pr-review": "allow", "internal-*": "deny", "experimental-*": "ask" } }`.

**Is a denied skill hidden from the model? Yes, by the page's own words** (`skills.md:153`, `:230`). Corroborated in the pinned release: opencode v1.19.3 `packages/opencode/src/skill/index.ts:314` (sha256 `91dce57f…`, the file round 50 pinned) reads `return list.filter((skill) => Permission.evaluate("skill", skill.name, agent.permission).action !== "deny")` inside `Skill.available(agent)`, and `Skill.fmt` (`:321`+) renders that list as `<available_skills>`. [INFERENCE] that filtered list is what the model sees — I did not locate the call site passing `available` into `fmt` in the files I fetched, so the chain to the prompt is not closed here. Contrast: lever 3 (`opencode/autoinvoke`) is **not** in the v1.19.3 loader (`grep -ci autoinvoke` → 0); `deny` is.

## Does the page say anything about choosing BETWEEN two matching skills? No.

`grep -ciE` over the fetched markdown: `overlap` 0 · `conflict` 0 · `precedence` 0 · `tie[- ]?break` 0 · `tie break` 0 · `priority` 0 · `multiple skills` 0 · `same name` 0 · `invocation` 0 · `unique` 1 · `disable` 3 · `deny` 3 · `permission` 8 · `hidden` 3 · `autoinvoke` 5 · `slash` 3. The page's only collision statement concerns duplicate **names**, not two matching skills: "Ensure skill names are unique across all locations" (`skills.md:229`). No precedence, tie-break or ordering rule of any kind appears.

**Bound, as required:** every lever above **removes a skill from the choice** (or gates its load); none is a documented tie-break. The page documents no rule that picks between two matching skills — deny, ask, autoinvoke and tools subtract, they do not arbitrate. "Deny the neighbour" must not be taught as "opencode prefers this skill".

## Drafts for the C2 tables

**(a) SKILL.md § Anti-patterns → "Overlap levers by client" row.** Header per the counter: `client | lever | row | key term`; the key term is the row's first backticked span, so the lever cell has no backticks.

```
| opencode | permission deny pattern on the skill name in the settings file hides that skill from the agent and rejects the load | S030 | `deny` |
```

**(b) `corpus/knowledge/skill-overlap-levers-round51.md` → § Levers by client row.** Header per the counter: `client | row | lever | quote`; the quote cell must be a double-quoted string followed by a parenthesized location. This pair of rows scores `BACKED opencode` and the quote is found on the live page (below).

```
| opencode | S030 | permission `deny` pattern on the skill name in opencode.json | "Check permissions—skills with `deny` are hidden from agents" (skills.md:230) |
```

**(c) Registry row.** A row exists (S024, `mined`), but its `teaches` is incomplete: it calls name uniqueness and `opencode/autoinvoke` "its only collision controls", while the page also documents the `permission` block and the `tools` block. `/home/vgpnk/Projects/shokunin/CORPUS.md` § SOURCES rule 2 forbids editing `scope`/`anchor`/`teaches` in place ("Only `status`, `recheck` and `used-by` change in place … A correction is a new row whose `teaches` opens `supersedes S0NN —`"), so the contract-clean path is a new row. S001–S029 exist (registry `awk`), so the next free id is **S030**.

```
| S030 | opencode — Agent skills — https://opencode.ai/docs/skills | docs | A | opencode's documented levers that remove a skill from the agent's choice or from loading, and whether the page documents a tie-break between two matching skills (vendor documentation for opencode's current release; not a measurement of omp or of opencode v1.19.3) | § Write frontmatter `skills.md:29-48`; § Recognize tool description `skills.md:108-129`; § Configure permissions `skills.md:133-158`; § Override per agent `skills.md:160-190`; § Disable the skill tool `skills.md:192-221`; § Troubleshoot loading `skills.md:223-231`; fetched as https://opencode.ai/docs/skills.md (200, 5365 B, sha256 `f10ced73…`, text/plain) on 2026-10-22T14:19:12Z, byte-identical to the 12:28:29Z and 12:31:20Z fetches recorded on S024; the HTML route (200, 73201 B, sha256 `4d96fa56…`) carries the same eleven sections | supersedes S024 — S024's teaches calls name uniqueness and `opencode/autoinvoke` the page's "only collision controls"; the page also documents a `permission` block whose `deny` value on a name pattern hides the skill from the agent and rejects the load, `ask` as a user prompt before loading, per-agent `permission.skill` overrides, and a `tools: skill: false` block that omits `<available_skills>` entirely; the page documents no tie-break between two matching skills | mined | 2026-10-22 | 90d | corpus/knowledge/skill-overlap-levers-round51.md |
```

If the L1 cites **S024** instead, S024's `used-by` must be extended in place (rule 2 allows it; log old→new in the lesson): old `corpus/knowledge/sibling-overlap-census-round49.md, corpus/lessons/round-50.md, corpus/knowledge/skill-selection-rules-round50.md` → new adds `, corpus/knowledge/skill-overlap-levers-round51.md`. The `teaches` correction would still need a row (rule 2). Exact old→new cell text for S024, if the L1 rules an in-place edit is allowed (the prompt's requested form; it contradicts CORPUS.md rule 2 — the L1 decides):

- **scope** old: `What opencode's own documentation states about how a skill's description reaches the model, and whether it documents a tie-break between two skills whose descriptions both match (vendor documentation for opencode's current release; not a measurement of omp or of opencode v1.19.3)` → new: `What opencode's own documentation states about how a skill's description reaches the model, which settings remove a skill from the agent's choice or from loading, and whether it documents a tie-break between two skills whose descriptions both match (vendor documentation for opencode's current release; not a measurement of omp or of opencode v1.19.3)`
- **anchor** old: `§ Write frontmatter `skills.md:29-48`; § Follow length rules `skills.md:70-73`; § Recognize tool description `skills.md:108-129`; § Troubleshoot loading `skills.md:223-231`; fetched as https://opencode.ai/docs/skills.md (200, 5365 B, sha256 `f10ced73…`, text/plain) on 2026-10-22T12:31:20Z, byte-identical to the 12:28:29Z fetch; the HTML route (200, 73201 B, sha256 `4d96fa56…`) carries the footer stamp "Last updated: Oct 20, 2026"; sweep `grep -ciE` over the markdown: overlap/ambigu/precedence/tie[- ]?break/conflict/multiple skills/same name/prioriti/truncat → 0 each, 1024 → 1` → new: the same cell with `§ Configure permissions `skills.md:133-158`; § Override per agent `skills.md:160-190`; § Disable the skill tool `skills.md:192-221`;` inserted after § Recognize tool description, the fetch stamp changed to `on 2026-10-22T14:19:12Z, byte-identical to the 12:28:29Z and 12:31:20Z fetches recorded on S024`, and `invocation` added to the sweep list
- **teaches** old: `opencode shows the model one `<available_skills>` list inside the `skill` tool description, each entry being the skill's name and description; `description` is capped at 1-1024 characters; the page documents no tie-break between two skills whose descriptions both match — its only collision controls are name uniqueness across locations and `opencode/autoinvoke: "false"`, which removes a skill from model-facing guidance` → new: `opencode shows the model one `<available_skills>` list inside the `skill` tool description, each entry being the skill's name and description; `description` is capped at 1-1024 characters; the page documents no tie-break between two skills whose descriptions both match — its collision controls are removals, not tie-breaks: name uniqueness across locations, a `permission` block whose `deny` value on a name pattern hides the skill from the agent and rejects the load, `ask` for a user prompt before loading, per-agent `permission.skill` overrides, `metadata["opencode/autoinvoke"]: "false"` which keeps the skill out of model-facing auto-selection while leaving it loadable by exact name, and `tools: skill: false` which omits `<available_skills>` entirely`

## Draft lesson Gate line (contract rule 1: URL, access date, ≤25-word quote, location)

```
| S030 | https://opencode.ai/docs/skills.md | 2026-10-22T14:19:12Z | "Check permissions—skills with `deny` are hidden from agents" (§ Troubleshoot loading, `skills.md:230`) — seat `.ufo/waves/round-51/build/SrcOpencode.md` |
```

## Verification of my own rows against the C2 counter

Private clone of the lane at `43ca0bfb` in scratch plus the counter seat's delivered patch (`/fast/scratch/hyaku/kotoba-r51/build/LeverGuard/patch.diff`, read-only use), with a world holding only my three opencode artefacts (SKILL.md row, S030 registry row, entry row):

- `check_overlap_levers.py --root ../world` → `BACKED opencode`, six `UNBACKED: no SKILL.md row` lines for the other clients, `overlap levers backed 1 of 7 clients`, exit 1 (1 of 7 because the other six clients are not mine; the per-client verdict is the point).
- `check_overlap_levers.py --root ../world --fetch` → `FETCH opencode: quote found (https://opencode.ai/docs/skills)`, `quotes found on live pages 1 of 1`, exit 1 (same reason) — the quote is found on the **live HTML route**, not only on the `.md`.
- `sources-census.sh validate --file mirror/corpus/SOURCES.md --today 2026-10-22` → `file ok …`, exit 0. Only new line: `file W04 S030 duplicate url opencode.ai/docs/skills across scopes` (a warning, same class as the three pre-existing W04s for S018/S019/S021); no E-code — E04 is avoided because the scope cell differs and `teaches` opens `supersedes S024`. Trap found: a registry row separated from the block by a blank line is **not parsed** by the counter (my first mirror insert put it after a blank line → `UNBACKED: source row S030 missing (opencode)`); it must sit directly under S029.

## Findings

1. **opencode is the richest of the seven clients on this axis** — the only one with a *permission* lever (per-skill-name `deny`/`ask`/`allow` with wildcards, global or per agent), and the only one whose docs say outright that a denied skill is hidden from the agent.
2. **Best single lever: `deny`** — it covers both halves of the claim ("chosen by the model **or** loaded at all"); `autoinvoke: "false"` stops the model seeing the skill but leaves it manually loadable.
3. **Correction owed to S024**: its `teaches` understates the page. The round-50 sweep terms (`overlap/ambigu/precedence/tie/conflict/…`) never included `permission`, `deny` or `hidden`, which is why the permission block was missed; the negative finding itself (no tie-break) stands.
4. **`compatibility` is a trap**: listed as an optional frontmatter field and used as `compatibility: opencode` in the example, but the page never says it filters loading — not a client-side scope lever.
5. **`opencode/slash` is not a removal** — it adds a `/name` user route; useful only with `autoinvoke: "false"` (user-only skill).
6. **Lead (not a row)**: `https://opencode.ai/docs/config.md` (200, 26060 B, sha256 `fe28a438…`, 14:20:51Z) mentions skills only in the directory list (`:53`); it adds no second removal setting, so the skills page is the only place the skills permission block is documented.
7. **Out of scope**: no edit to `corpus/SOURCES.md`, `SKILL.md`, `corpus/knowledge/**` or any lesson (read-only seat; the L1 lands the rows and tables), no change to the counter or the other six clients' rows, no sibling lane repo read, no runtime measurement of opencode, nothing here a claim about omp.

## Evidence (commands, exit codes)

```
$ curl -sSL -w 'STATUS=%{http_code} URL=%{url_effective} BYTES=%{size_download} CT=%{content_type}\n' -o skills.md2 https://opencode.ai/docs/skills.md
STATUS=200 URL=https://opencode.ai/docs/skills.md BYTES=5365 CT=text/plain; charset=utf-8      (exit 0)
$ date -u +ACCESS_UTC=%FT%TZ   # 2026-10-22T14:19:12Z ;  sha256sum skills.md2  # f10ced73971ce83b85f41395e2e15a683fe5a874e9057fc9d13da5f5a1bf8561
$ cmp skills.md skills.md2 && echo IDENTICAL_TO_FIRST_FETCH     # IDENTICAL_TO_FIRST_FETCH (exit 0)
$ curl -sSL -w 'STATUS=%{http_code} BYTES=%{size_download}\n' -o skills.html https://opencode.ai/docs/skills
STATUS=200 BYTES=73201 (exit 0)  sha256sum skills.html  # 4d96fa569dd25469e085b3743ee7e5a53263792fb919b7591bd7b8397a3404f0
$ curl -sSL -w 'STATUS=%{http_code} BYTES=%{size_download}\n' -o config.md https://opencode.ai/docs/config.md
STATUS=200 BYTES=26060 (exit 0)  sha256sum config.md  # fe28a438a1464cb5a43231a7af56f2ed16b019016731052ddfc2ae86fd54cda8
$ grep -nE 'permission|deny|hidden|autoinvoke|skill: false|available_skills' skills.md
133:## Configure permissions    143:      "internal-*": "deny",    153:| `deny`     | Skill hidden from agent, access rejected  |
154:| `ask`      | User prompted for approval before loading |    192:## Disable the skill tool    201:  skill: false
219:When disabled, the `<available_skills>` section is omitted entirely.
230:4. Check permissions—skills with `deny` are hidden from agents
231:5. Check `metadata["opencode/autoinvoke"]`—skills set to `"false"` are hidden from model-facing guidance
(exit 0; the 17-term sweep counts are in § "Does the page say anything about choosing BETWEEN two matching skills?")
$ curl -sSL -o skill_index.ts https://raw.githubusercontent.com/anomalyco/opencode/v1.19.3/packages/opencode/src/skill/index.ts   # 200, 11843 B (exit 0)
$ sha256sum skill_index.ts   # 91dce57f590e1ad3103e0555b893500e098a95cde2739422b699233889b205e6 ;  grep -n 'Permission.evaluate' skill_index.ts
314:      return list.filter((skill) => Permission.evaluate("skill", skill.name, agent.permission).action !== "deny")
$ grep -ci autoinvoke skill_index.ts   # 0
$ git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin lane && git -C lane checkout -q 43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10 && git -C lane apply /fast/scratch/hyaku/kotoba-r51/build/LeverGuard/patch.diff   (exit 0)
$ python3 -B verifiers/check_overlap_levers.py --root ../world         # BACKED opencode … backed 1 of 7 clients   (exit 1)
$ python3 -B verifiers/check_overlap_levers.py --root ../world --fetch  # FETCH opencode: quote found … 1 of 1   (exit 1)
$ bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file mirror/corpus/SOURCES.md --today 2026-10-22
file ok …/mirror/corpus/SOURCES.md   (exit 0; one new W04 for S030, same class as the three pre-existing W04s)
```

## Artifacts

`/fast/scratch/hyaku/kotoba-r51/build/src-opencode/`: `skills.md` (5365 B, quoted throughout), `skills.html` (73201 B), `skills_html.txt`, `config.md` (26060 B), v1.19.3 sources (`skill_index.ts`, `permission_index.ts`, `agent.ts`, `config_ts.ts`; corroboration only), `mirror/` (SOURCES.md with the draft S030 row plus the files the census needs), `world/` (my three artefacts as files), `lane/` (private clone with the counter patch applied). This report: `.ufo/waves/round-51/build/SrcOpencode.md`.
