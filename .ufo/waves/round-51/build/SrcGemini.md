# SrcGemini — round-51 C2 source seat (client: Gemini CLI)

Result: **HOLDS** — the Gemini CLI skills page is fresh (markdown re-fetched 2026-10-22T14:23:02Z and
14:43:23Z is byte-identical to the bytes S029 records) and it documents a per-name removal lever other
than description wording: the session command `/skills disable <name>` ("Prevents a specific skill
from being used", `skills.md:94`), with the scope note "`/skills disable` and `/skills enable` default
to the `user` scope" (`skills.md:75`). The drafted SKILL.md row, entry row and registry edit were
dry-run against the delivered counter `verifiers/check_overlap_levers.py` and come out `BACKED Gemini
CLI`, with the quote found on the live page by `--fetch`. **The page documents no tie-break between
two differently named skills whose descriptions both match** — a disable lever removes a skill from
the choice; it does not arbitrate between two.

Scope: open the page by ordinary means (curl; the site serves a `.md` variant), record URL / UTC access
time / HTTP status / bytes / sha256, locate verbatim quotes for every documented non-wording lever, run
the required `grep -niE` sweep, and draft the three C2 artifacts. Read-only on the lane; the only file
written there is this report. Scratch `/fast/scratch/hyaku/kotoba-r51/build/src-gemini/`. No package
installed or upgraded (curl, sha256sum, grep, python3 stdlib only).

## Fetch record (ordinary means: `curl -sSL`)

| route | accessed (UTC) | HTTP | bytes | sha256 (16) |
|---|---|---|---|---|
| https://geminicli.com/docs/cli/skills.md | 2026-10-22T14:23:02Z, again 14:43:23Z | 200 | 5,763 | `8e1b4cbe2cd31eff` |
| https://geminicli.com/docs/cli/skills/ (HTML) | 2026-10-22T14:18:53Z | 200 | 114,148 | `b17895012da7cbef` |
| https://geminicli.com/docs/cli/skills (no trailing slash) | 2026-10-22T14:43Z | 200 | 114,148 | `b17895012da7cbef` |
| https://geminicli.com/docs/cli/skills/.md | 2026-10-22T14:19Z | **404** | 31,633 | — |
| https://google-gemini.github.io/gemini-cli-docs/docs/cli/skills/ (former host) | 2026-10-22T14:43Z | **404** | 9,115 | — |

The `.md` route is the canonical fetch (`text/markdown`); `Last-Modified: Fri, 16 Oct 2026 02:36:07
GMT` on every Gemini page fetched. **Freshness: the bytes are unchanged since the round-50 fetch** —
the `skills.md` digest equals the one S029 records, so this row needs no re-derivation, only a
`used-by`/new-row edit. URL trap: the registry cell for S029 holds the **trailing-slash** form and
appending `.md` to it 404s; the counter's `--fetch` falls back to `url.rstrip("/") + ".md"`, which
resolves. Companion pages fetched in the same minute (all 200, same Last-Modified):
`skills-best-practices.md` 3,257 B `612c3b8396fdc666`; `using-agent-skills.md` 3,052 B
`9e61fb7cb289263`; `cli-reference.md` 16,561 B `2d445008576bc095`; `reference/configuration.md`
102,704 B `4fb90004ef3e4aeb`; `reference/policy-engine.md` 19,413 B `0caa715d2a1a1bc1`;
`reference/tools.md` 18,061 B `6b92328b478daae8`; `tools/activate-skill.md` 1,514 B `780be95b02937cd7`.

## Levers this client documents (other than description wording)

Every row is a **removal** lever: it takes one named skill out of what the model can be offered or
load. None is a tie-break between two matching skills.

| # | key term (code token) | what it does | where it is set | located verbatim quote (≤ 25 words, file:line) |
|---|---|---|---|---|
| 1 | `/skills disable` (and `/skills disable <name>`) | **disables entirely** — the skill is not used, and because discovery injects "all **enabled** skills" into the system prompt, a disabled skill is never offered to the model | interactive session command; scope `user` by default, `--scope workspace` for project scope | "`/skills disable` and `/skills enable` default to the `user` scope." (`skills.md:75`); "- `/skills disable <name>`: Prevents a specific skill from being used." (`skills.md:94`); "- `/skills disable <name>`: Prevents a skill from being triggered." (`using-agent-skills.md:33`) |
| 2 | `gemini skills disable <name>` / `gemini skills disable --all` | **disables entirely**, from the terminal rather than a session | terminal command; `--all` disables every skill at once | "| `gemini skills disable <name>`   | Disable an agent skill                | `gemini skills disable my-skill`                  |" (`cli-reference.md:130`); "| `gemini skills disable --all`    | Disable all skills                    | `gemini skills disable --all`                     |" (`cli-reference.md:132`) |
| 3 | `skills.disabled` | **disables entirely**, persistently, for a named skill — a list in the user's or project's `settings.json` | settings file (`~/.gemini/settings.json`, `.gemini/settings.json`); requires a restart | "- **`skills.disabled`** (array):" / "  - **Description:** List of disabled skills." (`configuration.md:2295-2296`) |
| 4 | `admin.skills.enabled` | **disables entirely**, for every skill, org-wide | admin settings (`admin.skills.enabled` = false) | "- **`admin.skills.enabled`** (boolean):" / "  - **Description:** If false, disallows agent skills from being used." (`configuration.md:2487-2488`) |
| 5 | `skills.enabled` | **disables entirely**, the whole feature | settings file | "- **`skills.enabled`** (boolean):" / "  - **Description:** Enable Agent Skills." (`configuration.md:2289-2291`) |

Lever 1 is the one the counter's pinned reviewed list names for this client
(`REVIEWED_LEVERS["Gemini CLI"] = {"/skills disable", "skills disable"}`) and the best table lever: it
is per-skill, needs no config file, and the same page says why it removes the skill from the model's
choice — "At the start of a session, Gemini CLI scans the discovery tiers and injects the name and
description of all enabled skills into the system prompt." (`skills.md:20-22`). **[INFERENCE]** that a
disabled skill's metadata is not injected: the page says discovery injects "all **enabled** skills"
and separately that `/skills disable` "prevents a specific skill from being used"; no single sentence
states the exclusion. The two sentences together carry it, but the chain is mine.

Levers 4 and 5 turn the feature off wholesale and `gemini skills disable --all` disables every skill,
so none of the three can separate two overlapping skills. The policy engine adds a sixth,
different-shaped lever — a `deny` decision on the `activate_skill` tool ("`deny`: The tool call is
blocked and is not executed… tools that are denied are **completely excluded from the model's
memory**… the model will not even see the tool as an option", `policy-engine.md:112-115`) — which
removes the *tool*, hence all skills, not one named skill. Recorded for completeness; not proposed.

## Does the page say anything about choosing BETWEEN two matching skills? No.

The required sweep over the fetched markdown `skills.md` (5,763 B) — 8 lines, all located:

```
31:      it permission to read any bundled assets.
38:of precedence (lowest to highest):
49:### Precedence and aliases
51:If multiple skills share the same name, the version from the higher-precedence
53:`.agents/skills/` alias takes precedence over the `.gemini/skills/` directory.
75:> `/skills disable` and `/skills enable` default to the `user` scope. Use
94:- `/skills disable <name>`: Prevents a specific skill from being used.
95:- `/skills enable <name>`: Re-enables a disabled skill.
```

Per-term counts: `overlap` 0 · `conflict` 0 · `deny` 0 · `hidden` 0 · `invocation` 0 · `precedence` 4
· `disable` 3 · `permission` 1 (that hit is file-path permission, `skills.md:31`, not skill choice).
Every `precedence` hit is **discovery-tier** precedence keyed on the **name**: "If multiple skills
share the same name, the version from the higher-precedence location is used." (`skills.md:51-52`) and
"the `.agents/skills/` alias takes precedence over the `.gemini/skills/` directory" (`skills.md:52-53`);
the tiers are built-in < extension < user < workspace (`skills.md:37-47`). The only "overlap" sentence
in the whole Gemini CLI skills documentation is author advice, not a runtime rule — "**Avoid
overlap**: Ensure your skill descriptions are distinct from one another and from the general
capabilities of the model." (`skills-best-practices.md:16-17`).

**Bound, as the assignment requires:** a disable lever *removes* a skill from the choice; it is not a
documented tie-break. The page says nothing otherwise — it documents no rule at all for choosing
between two skills whose descriptions both match, and nothing on it should be taught as "Gemini CLI
prefers this skill".

## Drafts for the C2 integrator

The delivered counter (after the CriticC2Sizing fixes) reads a **six-column** SKILL.md table and a
four-column entry table, so the drafts below use those shapes.

**(a) `SKILL.md` § Anti-patterns → "Overlap levers by client" table row.** The table must sit inside
the `## Anti-patterns` section (the verifier blanks HTML comments and fenced blocks and stops at the
next `## ` heading) and the header must be exactly
`| client | lever | held by | effect | row | key term |`. `held by` = `user or operator` (the session
command is run by the person operating the CLI, not shipped with the skill); `effect` = `removed
everywhere` (the skill is neither offered nor usable, not merely deprioritised).

```
| Gemini CLI | Disable one named skill so the model is never offered it | user or operator | removed everywhere | S030 | `/skills disable` |
```

**(b) `corpus/knowledge/skill-overlap-levers-round51.md` → "## Levers by client" table row.** Header
`| client | row | lever | quote |`; the quote cell starts with a double-quoted string followed by a
parenthesised location; the quote contains the key term as an exact code span. The quote is 10 words,
a verbatim raw substring of the fetched `skills.md` bytes at offset 3405 (line 75), and contains the
code span `/skills disable` exactly.

```
| Gemini CLI | S030 | `/skills disable` (session command; `user` scope by default) | "`/skills disable` and `/skills enable` default to the `user` scope." (skills.md:75) |
```

**(c) `corpus/SOURCES.md` — the registry change.** S029 already exists with `status=mined`,
`kind=docs`, `tier=A` and the first https URL under the counter's pinned Gemini prefix
`https://geminicli.com/docs/`; its `used-by` currently reads `corpus/knowledge/sibling-overlap-census-round49.md,
corpus/lessons/round-50.md, corpus/knowledge/skill-selection-rules-round50.md`. The contract-clean
shape (CORPUS.md § SOURCES rule 2: a correction is a **new** row whose `teaches` opens
`supersedes S0NN —`) is a new row that supersedes S029, plus an in-place `used-by` append on S029.
**The id is the L1's to assign**: S030 is claimed by two sibling seats in this wave
(`SrcCopilotSdk.md` and `SrcOpencode.md` both draft `S030` for their own row), so `S0NN` below is a
placeholder — the L1 must allocate a free id and rewrite it in all three artifacts (the registry ends
at S029: `grep -c '^| S' corpus/SOURCES.md` → 29). New row (11 cells, no `|` inside any cell):

```
| S0NN | Gemini CLI — Agent Skills — https://geminicli.com/docs/cli/skills/ | docs | A | How Gemini CLI discovers and activates skills (the `description`'s role) and what its documentation says about skills that collide (vendor documentation, not a measurement of omp or opencode) | § How it works (`skills.md:20-24`); § Discovery tiers (`skills.md:37-47`); § Precedence and aliases (`skills.md:49-53`); § Key benefits, scope note (`skills.md:75-76`); § Managing skills (`skills.md:81-97`, `/skills disable <name>` at `:94`); § Design for discovery (`skills-best-practices.md:8-17`); fetched as https://geminicli.com/docs/cli/skills.md (200, 5763 B, sha256 `8e1b4cbe…`) on 2026-10-22T12:28:45Z, byte-identical on re-fetch at 12:34:04Z and again at 14:23:02Z, page Last-Modified 2026-10-16; the HTML route (200, 114148 B, sha256 `b1789501…`) carries the same prose | supersedes S029 — the `description` is the only skill text in context before a trigger; the only collision rule the page states is by name — two skills sharing a name resolve by discovery-tier precedence (built-in < extension < user < workspace), with `.agents/skills/` beating `.gemini/skills/` inside a tier; the page states no tie-break between two skills with different names and overlapping scope; the page also documents a per-name removal lever, `/skills disable <name>`, which prevents a specific skill from being used, and since discovery injects only the enabled skills into the system prompt (`skills.md:21`), a disabled skill is never offered to the model | mined | 2026-10-22 | 90d | corpus/knowledge/skill-overlap-levers-round51.md |
```

The `scope` cell is byte-identical to S029's, so the census's duplicate-URL rule sees one scope (a
*different* scope string for the same URL raises a `W04` warning). The `teaches` cell opens
`supersedes S029 —` as rule 2 requires and adds the new fact. In-place edit on S029 (rule 2 allows
`status`, `recheck`, `used-by` in place only) — `used-by` old:
`corpus/knowledge/sibling-overlap-census-round49.md, corpus/lessons/round-50.md, corpus/knowledge/skill-selection-rules-round50.md`
→ new: that string plus `, corpus/knowledge/skill-overlap-levers-round51.md`. Leave `status`
(`mined`), `kind` (`docs`), `tier` (`A`), `opened` (`2026-10-22`) and `recheck` (`90d`) unchanged.
**Do not edit S029's `scope`/`anchor`/`teaches` in place** — rule 2 forbids it; the new row carries
the correction. The counter also requires the row id to appear under `## Gate` in
`corpus/lessons/round-51.md` (that file does not exist yet; this seat does not own it), and the
census requires the entry file to exist on disk before the row is `mined` (census `E11`) — create the
entry file **before** running the census.

## Dry run against the delivered counter (evidence that the drafts pass)

Lane mirror in scratch with only this seat's three artifacts applied
(`/fast/scratch/hyaku/kotoba-r51/build/src-gemini/laneD/`: real `SKILL.md` with the row inserted in
§ Anti-patterns, real `corpus/SOURCES.md` with the new row and the `used-by` append, the entry file,
the lesson Gate row):

- `python3 -B verifiers/check_overlap_levers.py --root .` → `BACKED Gemini CLI`, `overlap levers backed 1 of 7 clients`, exit 1 (the other six clients have no rows in this one-client world, so they are correctly unbacked).
- `python3 -B verifiers/check_overlap_levers.py --root . --fetch` → `FETCH Gemini CLI: quote found (https://geminicli.com/docs/cli/skills/)`, `quotes found on live pages 1 of 1`, exit 1 (same reason).
- `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file corpus/SOURCES.md --root . --today 2026-10-22` → the same three pre-existing `W04` lines (S018, S019, S021) and `file ok`, exit 0 — **no new W04**, because the new row's `scope` cell matches S029's; same on the in-place-only variant (`laneA/`, no new row), exit 0.

Two traps measured, worth passing on: **the SKILL.md table needs six columns** — a four-column table
(`| client | lever | row | key term |`, the shape the build brief quotes) is rejected outright with
`UNBACKED: SKILL.md table absent (Gemini CLI)` because the verifier's header check is an exact
six-cell match (measured in `fixture4/`); and **the lesson Gate row must name the row id** — with the
Gate naming S029 and the table naming S030 the counter says `UNBACKED: no round-51 Gate record for
S030 (Gemini CLI)`, so the Gate row must carry the **same** id the table cites.

## Out of scope / not done

No lane file was edited except this report; no product code, no registry row, no knowledge entry and no
lesson file was written by this seat — the drafts above are text for the L1 to integrate. The
S029-in-place vs. new-superseding-row choice is the L1's call; this seat measured both (both exit 0 on
the census; the new-row form is what rule 2 asks for). No tool was installed or upgraded; no subagent
was dispatched; no peer message was sent.

## Evidence (commands and exit codes)

- `curl -sSL -o skills.md https://geminicli.com/docs/cli/skills.md` → exit 0, 200, 5,763 B, sha256 `8e1b4cbe2cd31effa3375aa5d480269ab28bf82c02a42d9b52cbb61e5b248590`; `curl -sSL -o skills.html https://geminicli.com/docs/cli/skills/` → exit 0, 200, 114,148 B, sha256 `b17895012da7cbef…`; `curl -sSL https://geminicli.com/docs/cli/skills/.md` → 404; the former `google-gemini.github.io` host → 404.
- `grep -niE 'overlap|conflict|precedence|disable|deny|permission|hidden|invocation' skills.md` → exit 0, 8 lines (md:31, 38, 49, 51, 53, 75, 94, 95); per-term counts as tabulated above.
- quote offsets and word counts against the fetched bytes: `skills.md:75` offset 3405 (10 words, span `/skills disable`); `skills.md:94` offset 4068 (11 words, span `/skills disable <name>`); `cli-reference.md:130` (16 words); `cli-reference.md:132` (15 words); `configuration.md:2295` (3 words, span `skills.disabled`); `configuration.md:2487` (3 words, span `admin.skills.enabled`); `policy-engine.md:112` (11 words, span `deny`).
- exact code spans present on the fetched pages: `/skills disable` (skills.md:75), `/skills disable <name>` (skills.md:94), `gemini skills disable <name>` and `gemini skills disable my-skill` (cli-reference.md:130), `gemini skills disable --all` (cli-reference.md:132), `skills.disabled` (configuration.md:2295), `admin.skills.enabled` (configuration.md:2487), `skills.enabled` (configuration.md:2289), `deny` (policy-engine.md:51, 112, 117, 121, 123, 434), `activate_skill` (skills.md:24, tools.md:121, 175, activate-skill.md:1, 3, 15, 22).
- counter dry runs on the lane mirror: `--root .` → `BACKED Gemini CLI`, exit 1; `--root . --fetch` → `quote found`, exit 1; the four-column variant → `UNBACKED: SKILL.md table absent (Gemini CLI)`, exit 1; the Gate-id-mismatch variant → `UNBACKED: no round-51 Gate record for S030 (Gemini CLI)`, exit 1.

Report: .ufo/waves/round-51/build/SrcGemini.md
