Result: DONE — the dated-text rule is stated by Anthropic for Skill content and by no authority for AGENTS.md/CLAUDE.md always-on files, so box `alwayson.04` is a lane extension of a sourced principle whose docstring must carry that split; eight SOURCES rows are drafted below (one superseding S004), and a literal date scan already hits two of the five live depth-≤2 rule files.

Round 53, wave 1 (build), C2 source basis of `alwayson.04`. Seat `KotobaR53.ScribeDatedAuthority`. Lane base `e78dff667237fba2e3cf9eccb802eff5bc9ea302`; plan commit `3bb0a7a33e6eb585a83a1a55dee30b26079b1e36`. Nothing in the lane was written except this file; all fetched bytes live under `/fast/scratch/hyaku/kotoba-r53/ScribeDatedAuthority/fetch/`. No tool was installed or upgraded; no model call of any kind was made.

## 1. Scope and method

Target box, verbatim from `SKILL.md:371`:

- [ ] No dated or transient text; dates and live-state go to status files.

The counter that scores it is frozen at the plan commit: `verifiers/check_alwayson_boxes.py:10-11` restates the box and `:66-75` pins six cases (2 PASS controls: plain rules, a version number; 4 FAIL: ISO date, ISO timestamp, month-day date, dated `CLAUDE.md`). The counter's docstring says nothing about the rule's provenance; only the `alwayson.07` paragraph (`:15-22`) attributes a rule to a vendor. That silence is what this seat was asked to fill or refute.

Method: every authority was opened with plain `curl -sS -o <file> -w '%{http_code} %{size_download}'` in the scratch directory, hashed with `sha256sum`, and grepped for the rule's terms (`date`, `dated`, `transient`, `ephemeral`, `stale`, `outdated`, `time-sensitive`, `become outdated`, `expire`, `status`, `concise`, `short`, `avoid`). Quotes are against the fetched bytes with line numbers in those bytes; the one page served as single-line HTML (agents.md) is cited by byte offset. Fetch manifest in §8.2.

I read two sibling wave-1 reports before writing, so the record agrees with them rather than contradicting them: `.ufo/waves/round-53/build/ScoutClaudeBehaviour.md` (Claude Code binary and its model-free surfaces; same `memory.md` fetch hash) and `.ufo/waves/round-53/build/ScribeCopilotCli.md` (Copilot CLI source basis, whose §2.5 and §3.3 reach the same Copilot conclusion independently).

## 2. What each authority actually says

### 2.1 Anthropic — Agent Skills best practices: the rule exists, for skill content

`https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices.md`, fetched 2026-10-22T20:10:36Z, 200, 42,169 bytes, sha256 `f0a5d61b67123a31527e64aae7c5cfc05c4c7e27fff16f5b35ea14b135423960` (byte-identical to this lane's S019 fetch of the same route):

- `:572` — `## Content guidelines`
- `:574` — `### Avoid time-sensitive information`
- `:576` — "Don't include information that will become outdated:" (7 words)
- `:578` — "**Bad example: Time-sensitive** (will become wrong):"
- `:581` — "If you're doing this before August 2025, use the old API." (12 words)
- `:582` — "After August 2025, use the new API." (7 words)
- `:585` — "**Good example** (use "old patterns" section):"
- `:603` — "The old patterns section provides historical context without cluttering the main content." (12 words)

This is the only located statement of the rule in any authority opened this round. **Its scope is Skill content, not always-on rule files.** The page is Anthropic's authoring guide for `SKILL.md`, and the body of a skill loads when the skill activates; the companion open-format page says so: `agentskills.io/skill-creation/best-practices.md:50` — "Once a skill activates, its full `SKILL.md` body loads into the agent's context window" (15 words).

### 2.2 Anthropic — Claude Code memory docs: the always-on scope, no date rule

`https://code.claude.com/docs/en/memory.md`, fetched 2026-10-22T20:05:00Z, 200, 51,971 bytes, 638 lines, sha256 `971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff`; same hash as `ScoutClaudeBehaviour`'s independent fetch at 20:04:37Z:

- `:24` — "Claude treats them as context, not enforced configuration." (8 words)
- `:51` — "Keep it to facts Claude should hold in every session: build commands, conventions, project layout, "always do X" rules." (19 words)
- `:88` — Size bullet: "target under 200 lines per CLAUDE.md file." and "Longer files consume more context and reduce adherence."
- `:90` — Consistency bullet: "periodically to remove outdated or conflicting instructions" (6 words)
- `:94` — "Claude looks for problems such as instructions written for older models, references to files or commands that don't exist" (19 words)
- `:549` — auto-memory index: "keep one line per entry, move detail into topic files, and merge or drop stale entries" (17 words)

Nearest neighbour for `alwayson.07` (the plan asks for the Gate quote from this page):

- `:357` table row — with both files present, "Your `CLAUDE.md` files only" (5 words)
- `:436` — "A `CLAUDE.md` that tells Claude in words to read `AGENTS.md`" (13 words) and "Claude sees `AGENTS.md` only if it decides to open the file." (12 words) — the prose mention is not an import
- `:442` — "keep it as the one file every tool shares by putting an `@AGENTS.md` import in a `CLAUDE.md`" (20 words)
- `:452` — "If you don't need Claude-specific content, a symlink also works:" (11 words); `:455` code line `ln -s AGENTS.md CLAUDE.md`

No line on this page forbids dates or live state. The page's staleness vocabulary is "outdated or conflicting" and "don't exist" (dead references), not "dated".

### 2.3 Anthropic — Claude Code best practices and error reference

`https://code.claude.com/docs/en/best-practices.md`, fetched 2026-10-22T20:05:01Z, 200, 36,360 bytes, sha256 `b225977e2892002cc91ff4dfe2d6a7e2324fd455aa6325c889cecb009ca76052`:

- `:168` — "CLAUDE.md is loaded every session, so only include things that apply broadly." (13 words)
- `:170` — "Keep it concise. For each line, ask: *"Would removing this cause Claude to make mistakes?"* If not, cut it." (19 words)
- `:182` — "review it when things go wrong, prune it regularly" (8 words)

`https://code.claude.com/docs/en/errors.md`, fetched 2026-10-22T20:10:35Z, 200, 549,839 bytes, sha256 `99b041134be25cef79acbb97c04c034dbf0818c96dd23e393d0c2e8db1000dd1`:

- `:6005` — "large or outdated `CLAUDE.md` files and MCP tool definitions consume context and can steer responses" (17 words)

Both are scope and pruning rules. Neither says a date must not appear.

### 2.4 OpenAI — Codex AGENTS.md guidance

`https://learn.chatgpt.com/docs/agent-configuration/agents-md.md` (the `developers.openai.com/codex/guides/agents-md.md` route redirects here), fetched 2026-10-22T20:05:36Z, 200, 9,149 bytes, sha256 `9d1f87a2d1cb55b4782b95abe710692b35b9659789c2db31a22c7074a3383e8e`:

- `:11-13` — discovery: global `AGENTS.override.md` then `AGENTS.md`; project walk from root to cwd; "Codex includes at most one file per directory." (9 words); merge order root-down
- `:15` — "stops adding files once the combined size reaches the limit defined by `project_doc_max_bytes` (32 KiB by default)" (18 words)
- `:206` — troubleshooting, the only "stale" line: "If instructions look stale, restart Codex in the target directory." — a cache statement about the loader, not about content

`https://learn.chatgpt.com/docs/customization/overview.md`, fetched 2026-10-22T20:08:23Z, 200, 9,482 bytes, sha256 `e4f466bb13521bc8d4e193962192c45319d5abc0cb58875d4a7eed2a9f9a20d6`:

- `:9` — "**Project guidance (`AGENTS.md`)** for persistent instructions"
- `:21` — "`AGENTS.md` gives Codex durable project guidance that travels with your repository and applies before the agent starts work. Keep it small." (22 words)
- `:30` — "correct them in `AGENTS.md` and ask the agent to update `AGENTS.md` so the fix persists. Treat it as a feedback loop."
- `:34-40` — § When to update `AGENTS.md`: repeated mistakes, too much reading, recurring PR feedback, and "**Automate drift checks**: Use scheduled tasks to run recurring checks (for example, daily) that look for guidance gaps"

The word "durable" is the vendor's scope adjective for the file, and the update triggers are behavioural, not calendar-based. No line forbids dated text.

### 2.5 agents.md — the open format

`https://agents.md/`, fetched 2026-10-22T20:05:01Z, 200, 81,690 bytes (single-line HTML, no newlines), sha256 `06b65de9018141350fe45cdd9fccafa59787badc46f30d92a06c07e612713979`; README `https://raw.githubusercontent.com/openai/agents.md/main/README.md` (GitHub redirects the org to `agentsmd`), fetched 2026-10-22T20:07:40Z, 200, 2,015 bytes, sha256 `60ec51c226560aaf2c49a0b8a2452c8cf24459c37a816764979dc917076c7afb`:

- README `:7` — "Think of AGENTS.md as a README for agents: a dedicated, predictable place" (13 words)
- byte offset 66192 in the HTML — "Are there required fields" (FAQ heading)
- byte offset 67214 — "Treat AGENTS.md as living documentation" (6 words)

The FAQ's conflict rule (S004's teach) is unchanged: "The closest AGENTS.md to the edited file wins; explicit user chat prompts override everything." (15 words). The format states no dated-text rule and, in the FAQ, actively frames the file as something you keep updating. "Living documentation" is not a prohibition on dates; it is the opposite emphasis, and it must be reported as such rather than bent toward the box.

### 2.6 GitHub Copilot — custom-instruction guidance

Peer evidence first: `ScribeCopilotCli.md` §2.5 and §3.3 already answer this client for Copilot CLI and record the absence with its three Q30 legs. I re-opened the two cross-surface pages independently:

`https://docs.github.com/en/copilot/concepts/prompting-and-context/custom-instructions.md`, fetched 2026-10-22T20:08:42Z, 200, 14,669 bytes, sha256 `6e7964dc1951c64c1b740b70e0353e56de6ae100805347b99440f050416de933`:

- `:95` — "most effective when they are short, self-contained statements" (7 words)
- `:126` — "Because the instructions are sent with every chat message, they should be broadly applicable to most requests" (18 words)

`https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions.md` (canonical route; the brief's `how-tos/configure-custom-instructions/...` path is a 404 as `.md`), fetched 2026-10-22T20:07:01Z, 200, 22,858 bytes, sha256 `c29d67f0a342f2ae8de6bda04b8c7e7ce9a1341d61eaffdeee9a4fc8c9ced635`; source in `github/docs` at `content/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions.md`, 13,608 bytes, sha256 `04cf53d3969c4fe03988f0d25d7bc24e8590320f7e6c28041b1931105ba2c3a4`:

- canonical `.md:63` — "Instructions must be no longer than 2 pages." (9 words)
- canonical `.md:64` — "Instructions must not be task specific." (6 words)
- both lines sit inside the copyable `<Limitations>` block of the generation prompt (`:44-121`), addressed to the agent that writes the file

VS Code's Copilot documentation (supporting only, not admitted as a row because the page is single-line HTML): `https://code.visualstudio.com/docs/copilot/customization/custom-instructions`, fetched 2026-10-22T20:06:41Z, 200, 162,008 bytes, sha256 `dc87f7c2a0c19e731bb2902306f505740bef05dc78df1214a1fbc67a374b7ab0`; text extraction § Tips for writing effective instructions — "Keep your instructions short and self-contained. Each instruction should be a single, simple statement." (12 words). No date rule.

### 2.7 Agent Skills open format — spec and creator best practices

`https://agentskills.io/specification.md`, fetched 2026-10-22T20:05:02Z, 200, 7,608 bytes, sha256 `9a67de89132948b2300b8dc87b93817971d47f9be89b644444965881a8dfde16` — byte-identical to S018; `:229` `## Progressive disclosure`, `:237` "Keep your main `SKILL.md` under 500 lines." No date rule.

`https://agentskills.io/skill-creation/best-practices.md`, fetched 2026-10-22T20:05:36Z, 200, 14,884 bytes, sha256 `05173180a1be5ef1ca2e06cb79a1b38067763a4a8bc9a2eb1a989abcc0e37626`; source `docs/skill-creation/best-practices.mdx` at `main`, 14,608 bytes, sha256 `a729bc1d746366ecb8c5056b100439fbf760007a0f836e089c0f3aff9ce5c2f8`:

- `:78` — "Would the agent get this wrong without this instruction?" If the answer is no, cut it. (17 words)
- `:86` — "Concise, stepwise guidance with a working example tends to outperform exhaustive documentation." (12 words)

No date rule here; the explicit "Avoid time-sensitive information" section is Anthropic's platform page (§2.1), not the open format's.

## 3. The answer to the assignment

**No authority opened this round states the rule for AGENTS.md/CLAUDE.md always-on files.** One authority states the underlying rule for Skill content (Anthropic, §2.1). The always-on application and the destination clause ("dates and live-state go to status files") are the lane's own.

Consequences, in the order the C2 work needs them:

1. `alwayson.04` cannot be attributed to a vendor as written. The closest located authority statement is Anthropic's skills guideline, quoted in §2.1, and it governs `SKILL.md`, not the always-on class. The box's own grounding is the round-7 audit: `corpus/knowledge/alwayson-checklist-round7.md:16` states the item, and `:30` records the application — 6/6 shokunin repo files PASS, the host `~/.agents/AGENTS.md` FAIL with "dated text (:48,:51 = 2026-09-06 attestations)" in its 75-line form.
2. The "status files" destination is a lane convention with no source. Nothing in §2 names a status-file class; the nearest vendor mechanism is Codex's advice to run scheduled drift checks outside the file (`customization/overview.md:40`), which is adjacent, not the same rule.
3. Therefore the instrument's docstring must say three things (Q23): the located authority quote and its skills-only scope; that the always-on application is the lane's rule with the round-7 evidence above; and what the check approximates (§4). It must not say "Anthropic requires AGENTS.md to contain no dates".

Proposed docstring paragraph for `verifiers/verify_alwayson.py` (the executor may polish wording, but not the facts):

> `alwayson.04` restates a lane rule (`SKILL.md:371`, grounded in `corpus/knowledge/alwayson-checklist-round7.md:16` and its application row `:30`). The closest authority statement is Anthropic's Agent Skills best practices, § Content guidelines → § Avoid time-sensitive information (`best-practices.md:574-583`, sha256 `f0a5d61b…`): "Don't include information that will become outdated". That page governs Skill content, not AGENTS.md or CLAUDE.md; no authority opened this round forbids dated or transient text in always-on files (sweep: `.ufo/waves/round-53/build/ScribeDatedAuthority.md` §5). The check approximates the rule with a date-literal detector: it flags ISO dates, ISO timestamps and month-name dates, passes dotted version numbers, cannot distinguish a provenance stamp from an expiring fact, and does not see undated transient text (relative or periodic phrasing). The destination clause ("status files") is a lane convention with no vendor source.

## 4. What the check approximates, in both directions (Q20/Q23 input)

The pinned cases fix six behaviours (frozen; not to be widened by a seat). Beyond them, a candidate date-literal detector was run on 12 strings to measure the directions. This is a probe of the candidate pattern, **not** the instrument; the executor still owes the measured table for the pattern it ships.

Candidate patterns used for the probe (scratch, not product):

```
ISO date      \b\d{4}-\d{2}-\d{2}\b
ISO timestamp \b\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(?::\d{2})?Z?\b
month-day     \b(January|...|December)\s+\d{1,2}\b
```

| Input | Probe | What it teaches |
|---|---|---|
| `- Use Python 3.12 or later.` (pinned PASS) | pass | dotted versions stay green |
| `- Until 2026-11-01, route builds to the staging runner.` (pinned FAIL) | FLAG | ISO date caught |
| `- Deploy freeze started 2026-10-22T19:37Z.` (pinned FAIL) | FLAG | timestamp caught |
| `- Until November 1, do not deploy on Fridays.` (pinned FAIL) | FLAG | month-day caught |
| `If you're doing this before August 2025, use the old API.` (Anthropic's own bad example) | **pass** | a month-day-only rule **misses the authority's bad example**: month-year is not pinned |
| `<summary>Legacy v1 API (deprecated 2025-08)</summary>` | **pass** | year-month markers missed |
| `- Currently the staging runner is down.` | **pass** | undated live state missed |
| `- This quarter, prefer pnpm.` | **pass** | periodic text missed |
| `- Freeze ends 10/22/2026.` | **pass** | locale numeric dates missed |
| `- Pin claude-sonnet-4-5@20250929 in provider config.` | **pass** | date-suffixed identifiers missed (desirable here) |
| `# Operator tooling directive — 2026-10-19` | **FLAG** | a provenance heading is flagged: over-flag direction |
| `- Migrate after 2026.` | **pass** | bare years missed |

Cross-check: `python3 -B - <<EOF` with the three patterns, 12 inputs, printed the table above (exit 0).

Two directions are therefore measured and must be stated in the docstring: the check **misses** the authority's own bad example (month-year) and all undated transient wording, and it **over-flags** provenance stamps (a date that never expires). The box's wording ("No dated or transient text") covers the provenance stamp as written; no authority states which of the two directions the rule intends, which is exactly why the docstring must name them as approximation rather than as a vendor rule.

Live population, measured (mechanical scan only — this is not a box verdict and not the instrument):

| File | Line | Text | Class |
|---|---|---|---|
| `/home/vgpnk/.agents/AGENTS.md` | 1 | `# Operator tooling directive — 2026-10-19` | dated title (provenance) |
| `/home/vgpnk/Projects/ufo-fsd-alpha/AGENTS.md` | 87 | `## Routing authority (2026-09-20 cutover; 2026-09-21 redelegation)` | dated section heading |
| same | 139 | `## NC2 fleet dispatch protocol (standard, 2026-09-20)` | dated section heading |
| same | 268 | `## Commit-trail doctrine (2026-09-21, operator directive)` | dated section heading |

`wc -l /home/vgpnk/.agents/AGENTS.md` → 14. `sed -n '1,3p'` prints the dated title above. `grep -n -E '[0-9]{4}-[0-9]{2}-[0-9]{2}'` over `kimi-code/AGENTS.md`, `opencodeufo/AGENTS.md`, `shokunin/AGENTS.md` → no match (exit 1). So 2 of the 5 depth-≤2 rule files carry ISO dates, and both are headings rather than expiring rules. A live run of the instrument will FAIL on them; `ScoutAlwaysOnPop` recorded the same hits independently and flagged that the round-7 pointers `:48` and `:51` are dead in the 14-line file.

## 5. Q30 sweeps

Every negative below names its three legs: the vendor's changelog or release notes, the current docs source tree (not only a rendered page), and a grep of the lane corpus. Coverage limits are stated where a leg is a window.

### 5.1 Anthropic Claude Code — no dated-text rule for CLAUDE.md/AGENTS.md

- **Changelog.** `https://code.claude.com/docs/en/changelog.md`, fetched 2026-10-22T20:06:36Z, 200, 1,090,388 bytes, sha256 `c719b69d151d30d7db0f80b3a45a53e978e2b380118e1392e9170caa77f1e7d6`. `grep -c -i 'time-sensitive'` → 0. `grep -n -i -E 'transient|ephemeral|stale|outdated'` → network, retry, plugin and cache items only (reviewed in a 30-line cut). The two `prompt-audit` entries are about stale *references*: `:1999` "audit your CLAUDE.md files, skills, agents and commands for prompting patterns written for older models"; `:2034` "stale paths, stale commands and contradicting instruction files now lead the report". No entry introduces a date rule.
- **Docs source tree.** Claude Code's docs are published as rendered pages plus `.md` routes; there is no public docs repository. The closest available full tree is the vendor's own bundle `https://code.claude.com/docs/llms-full.txt`, fetched 2026-10-22T20:07:38Z, 200, 9,614,681 bytes, sha256 `1a5816202ca5cb4378a2ea8afad80d1d0102e83fe387096ffe0ca89f80fe563a`, indexed by `https://code.claude.com/docs/llms.txt` (200, 63,682 B, `b7064ac5…`). Measured over the bundle: `grep -c -i 'time-sensitive'` → **1**, and it is unrelated (`:62088` "Time-sensitive work with tight deadlines", a use-case bullet); `grep -c -i 'become outdated'` → 0; `grep -n -i -E '\bdated\b'` → 11 hits, every one a model ID or a backup file name; `transient` hits are network retries only. The same terms over `memory.md`, `best-practices.md` and `errors.md` → 0 (the only staleness vocabulary is "outdated", "stale instructions", "don't exist").
- **Lane corpus.** `grep -rn -i -E "time-sensitive|time sensitive|become outdated|expiring facts|dated text" corpus/ SKILL.md PROVINCE.md README.md verifiers/` (lane root, 2026-10-22) → two hits, both the lane's own rule: `corpus/knowledge/alwayson-checklist-round7.md:16` and `SKILL.md:371`. No corpus file attributes a dating rule to Claude Code.
- **Verdict.** Not "silent": the docs state the *scope* of the file (facts for every session) and the *repair* (remove outdated instructions). They do not state the dated-text prohibition for this file class. This is an absence with its sweep.

### 5.2 Anthropic Agent Skills — the rule is stated (positive)

Not a negative. The page in §2.1 states it for Skill content. Its own docs tree: the platform docs are `.md`-served with no public repo; the same page's bytes were compared to S019's pin (`f0a5d61b…`) and match. Its spec sibling (agentskills.io) is a different authority and states nothing (§5.6).

### 5.3 OpenAI Codex — no dated-text rule

- **Changelog.** Three legs, all narrow and said to be narrow: `https://raw.githubusercontent.com/openai/codex/main/CHANGELOG.md` (200, 330 bytes, `c8458f99…`) is a pointer to the releases page plus one unreleased item; `https://github.com/openai/codex/releases.atom` (200, 6,046 bytes, `80dafdc7…`) carries 10 entries, all stamped 2026-10-22; `https://github.com/openai/codex/releases` (200, 387,795 bytes, `a6febe28…`) grepped for `AGENTS.md` and `instruction` → no match. Coverage limit: the feed and page show the recent window only, so this leg cannot exclude a rule retired long ago; the docs-tree leg below is the compensating full check.
- **Docs source tree.** `https://learn.chatgpt.com/llms-full.txt`, fetched 2026-10-22T20:07:38Z, 200, 2,549,875 bytes, sha256 `3499a408f770d7c0051bdb018f7974685fd45565fe2bc42bcbf60698542d0eb3`, indexed by `https://learn.chatgpt.com/llms.txt` (200, 33,447 B, `fc7b20ea…`). Measured over the bundle: `time-sensitive` → 0, `become outdated` → 0, `dated` → 0, `transient`/`ephemeral` hits are thread and session API fields. The repository's own `docs/agents_md.md` (200, 126 bytes) is a pointer to the site page.
- **Lane corpus.** Same grep as §5.1 → no Codex attribution.
- **Verdict.** Absent for this client, within a stated changelog window; the docs bundle is the full-corpus leg.

### 5.4 agents.md — no dated-text rule (scoped)

- **Release notes.** `https://github.com/openai/agents.md/releases.atom` (GitHub redirects to `agentsmd/agents.md`), fetched 2026-10-22T20:07:40Z, 200, 522 bytes, sha256 `b9578d2ff3824fcc7c69a0ea16eb57a85e3c608035139c367caf74b149865c7f`, `grep -c '<entry>'` → 0: the project publishes no releases.
- **Docs source tree — partial.** Opened: the README at `main` (2,015 bytes, `60ec51c2…`) and the rendered site (81,690-byte HTML, `06b65de9…`). Not opened: the site's page component — `raw.githubusercontent.com/agentsmd/agents.md/main/app/page.tsx` → 404, the `openai/agents.md` spelling of the same path (`app/page.mdx`) → 404, and both GitHub tree/contents API calls → 403 (unauthenticated rate limit). Because one leg is partial, this client is recorded **not checked** for a full negative and the claim is scoped: *the published site text and README state no dated-text rule*.
- **Lane corpus.** No agents.md attribution for this rule; S004's conflict-rule teach is the only row for the source.
- **Verdict.** No rule in the published text; the format's own FAQ says "Treat AGENTS.md as living documentation" (byte 67214), which is the opposite emphasis.

### 5.5 GitHub Copilot — no dated-text rule

- **Changelog.** My leg: `https://github.blog/changelog/label/copilot/feed/`, fetched 2026-10-22T20:08:50Z, 200, 46,175 bytes, sha256 `10e7600ce5ca066bd05c21afd26da183cc814f95ced5fb546af9600052e8d633`, 10 items, no instruction-file title (`grep -o '<title>...'` list reviewed). Stronger leg, peer: `ScribeCopilotCli.md` §3.3 uses the pinned full changelog (`7ea98dfc…`, 289,859 B, `c4b793bd…`, 3,569 lines), greps the 52 instruction lines and finds no dating rule.
- **Docs source tree.** `github/docs` raw markdown for the concept page (10,515 bytes, `0ad782dd…`) and the how-to (13,608 bytes, `04cf53d3…`), plus the canonical `.md` routes (14,669 and 22,858 bytes); the peer's source-tree inventory covers the CLI page (5,684 bytes, `ed823a4f…`) and the reusable snippet (329 bytes, `ee14953c…`). `grep -n -i -E '\b(date[sd]?|transient|ephemeral|stale|outdated|expire|time-sensitive|as of|status)\b'` over the concept page → only `:48` "avoid overloading" and `:95` "avoid providing conflicting sets"; no dating rule.
- **Lane corpus.** Same grep → no Copilot attribution.
- **Verdict.** Absent, with the peer's full-changelog leg as the wide window.

### 5.6 Agent Skills open format — no dated-text rule

- **Release notes.** `https://github.com/agentskills/agentskills/releases.atom`, fetched 2026-10-22T20:07:40Z, 200, 539 bytes, sha256 `86e3ba2866781925fc781b306f90eae42e0fc3b938bc66cfa012257151a6bd3b`, `grep -c '<entry>'` → 0; `docs/changelog.mdx` → 404.
- **Docs source tree.** `docs/specification.mdx` (7,166 bytes, `b9079c0c…`) and `docs/skill-creation/best-practices.mdx` (14,608 bytes, `a729bc1d…`) at `main`. `time-sensitive` → 0 in both; `dated`/`stale`/`expired` → 0 in the instruction prose.
- **Lane corpus.** Same grep → no agentskills attribution.
- **Verdict.** Absent in spec and creator guide.

### 5.7 Summary table

| Authority | States the dated-text rule for always-on files? | What it does state | Best located quote |
|---|---|---|---|
| Anthropic Agent Skills best practices | No (rule exists for Skill content only) | don't include information that will become outdated | `best-practices.md:576` |
| Anthropic Claude Code memory | No | facts for every session; remove outdated/conflicting instructions; stale references | `memory.md:51`, `:90`, `:94` |
| Anthropic Claude Code best practices / errors | No | include only broadly applicable text; prune; stale files steer responses | `best-practices.md:168`, `:170`; `errors.md:6005` |
| OpenAI Codex | No | "durable project guidance", keep it small; update on repeated mistakes | `customization/overview.md:21`, `:34-40` |
| agents.md | No | living documentation; nearest file wins | FAQ byte 67214 |
| GitHub Copilot | No | short, self-contained, broadly applicable; not task specific | concept `:126`; how-to `:64` |
| Agent Skills open format | No | cut what the agent would not get wrong; moderate detail | best-practices `:78`, `:86` |

## 6. Drafted SOURCES rows

Column shape copied from `corpus/SOURCES.md:12` (11 columns). Numbers `S043`–`S050` are the next unused after S042; the L1 assigns final ids. Cells contain no `|`. `used-by` names the knowledge entry C2 is expected to add; if the entry is named differently, retarget the cell rather than dropping it.

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S043 | Claude Code Docs — How Claude remembers your project — https://code.claude.com/docs/en/memory.md | docs | A | Which always-on instruction files Claude Code reads, when AGENTS.md and CLAUDE.md shadow each other, the two redirect forms, and the vendor's bounds on what belongs in CLAUDE.md (vendor documentation, not a measurement of Claude Code) | § When to add to CLAUDE.md `memory.md:51`; § Write effective instructions `:86-90`; § Audit your instruction files `:92-94`; § AGENTS.md table `:353-358`; § Share one file with other coding tools `:440-455`; fetched 2026-10-22T20:05:00Z (200, 51,971 B, sha256 `971d75bf…`), same bytes as the 20:04:37Z fetch in ScoutClaudeBehaviour.md | Keep CLAUDE.md to "facts Claude should hold in every session"; remove "outdated or conflicting instructions"; with both files present Claude reads "Your CLAUDE.md files only"; a redirect is an `@AGENTS.md` import or a symlink; a CLAUDE.md that "tells Claude in words" is not one; no dated-text rule is stated for this file class | mined | 2026-10-22 | 90d | corpus/knowledge/alwayson-source-basis-round53.md (proposed) |
| S044 | Claude Code Docs — Best practices for Claude Code — https://code.claude.com/docs/en/best-practices.md | docs | A | What Anthropic says to put in CLAUDE.md and how to prune it (vendor authoring guidance, not a measurement of Claude Code) | `best-practices.md:168` and `:170`; `:182`; fetched 2026-10-22T20:05:01Z (200, 36,360 B, sha256 `b225977e…`) | CLAUDE.md "is loaded every session, so only include things that apply broadly"; cut each line whose removal would not cause mistakes; prune regularly. Nothing about dates or live state | mined | 2026-10-22 | 90d | corpus/knowledge/alwayson-source-basis-round53.md (proposed) |
| S045 | Claude Docs — Agent Skills best practices — https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices.md | docs | A | Anthropic's content guidelines for skill instructions, including time-sensitive information (vendor authoring guidance for SKILL.md, not always-on files) | § Content guidelines → § Avoid time-sensitive information `:572-583` (`:576`, `:581-582`, `:603`); fetched 2026-10-22T20:10:36Z (200, 42,169 B, sha256 `f0a5d61b…`, byte-identical to S019); same source as S019, adding a section its scope did not cover | "Don't include information that will become outdated"; the bad example is a dated API switch ("before August 2025"), the good pattern keeps historical notes under an old-patterns heading. Scope is Skill content; it does not extend to CLAUDE.md or AGENTS.md | mined | 2026-10-22 | 90d | corpus/knowledge/alwayson-source-basis-round53.md (proposed), SKILL.md |
| S046 | OpenAI — Custom instructions with AGENTS.md (Codex) — https://learn.chatgpt.com/docs/agent-configuration/agents-md.md | docs | A | Which AGENTS.md files Codex reads, in what order, with which fallbacks and size cap (vendor documentation for Codex, not a measurement of the binary) | § How Codex discovers guidance `:7-15`; § Create global guidance `:17-47`; § Customize fallback filenames `:145-160`; § Verify your setup and Troubleshoot `:201-213`; fetched 2026-10-22T20:05:36Z (200, 9,149 B, sha256 `9d1f87a2…`) | Global `AGENTS.override.md` then `AGENTS.md`; per-directory walk root to cwd with `AGENTS.override.md`, `AGENTS.md`, then fallbacks; "Codex includes at most one file per directory"; concatenates root-down; stops at `project_doc_max_bytes` (32 KiB by default). No dated-text rule | mined | 2026-10-22 | 90d | corpus/knowledge/alwayson-source-basis-round53.md (proposed) |
| S047 | OpenAI — Customization (Codex), AGENTS Guidance — https://learn.chatgpt.com/docs/customization/overview.md | docs | A | What OpenAI says AGENTS.md is for and when to change it (vendor documentation, not a measurement of the binary) | § AGENTS Guidance `:21`; `:30`; § When to update AGENTS.md `:34-40`; fetched 2026-10-22T20:08:23Z (200, 9,482 B, sha256 `e4f466bb…`) | "AGENTS.md gives Codex durable project guidance that travels with your repository and applies before the agent starts work. Keep it small"; update it on repeated mistakes and recurring review feedback; run scheduled drift checks outside the file. No dated-text rule | mined | 2026-10-22 | 90d | corpus/knowledge/alwayson-source-basis-round53.md (proposed) |
| S048 | AGENTS.md — open format site and repository — https://agents.md/ | spec | A | The open format's own answers about required fields, conflict order and maintenance, including what it does not require (format documentation, not a client measurement) | FAQ "Are there required fields" at byte 66192 and "Treat AGENTS.md as living documentation" at byte 67214 of the fetched 81,690 B HTML (single line, so byte offsets); README `:7`; fetched 2026-10-22T20:05:01Z (200, 81,690 B, sha256 `06b65de9…`) and README at 20:07:40Z (200, 2,015 B, sha256 `60ec51c2…`); supersedes S004 | No required fields, any headings; "The closest AGENTS.md to the edited file wins; explicit user chat prompts override everything" (S004's teach, unchanged); the format states no dated-text rule and calls the file living documentation, so it endorses updating rather than pruning dates | mined | 2026-10-22 | 90d | corpus/knowledge/alwayson-source-basis-round53.md (proposed) |
| S049 | GitHub Docs — Adding repository custom instructions for GitHub Copilot — https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions.md | docs | A | GitHub's authored limitations for the file it generates for Copilot, on the canonical route (vendor documentation, not a measurement of any client) | The `<Limitations>` block inside the generation prompt `:63-64` of the canonical `.md` (200, 22,858 B, sha256 `c29d67f0…`, fetched 2026-10-22T20:07:01Z); source file `github/docs` `content/.../add-repository-instructions.md` `:74-75` (200, 13,608 B, sha256 `04cf53d3…`); the brief's `how-tos/configure-custom-instructions/...` route is a 404 as `.md` | "Instructions must be no longer than 2 pages" and "Instructions must not be task specific". Both are inside the prompt that asks the agent to write the file; neither is a loader rule. No dated-text rule | mined | 2026-10-22 | 90d | corpus/knowledge/alwayson-source-basis-round53.md (proposed) |
| S050 | Agent Skills — Best practices for skill creators — https://agentskills.io/skill-creation/best-practices.md | docs | A | How much instruction content a skill file should carry and how to decide what to cut (open-format authoring guidance, not a client measurement) | § Spending context wisely `:48-52`; § Add what the agent lacks `:78`; § Aim for moderate detail `:84-86`; fetched 2026-10-22T20:05:36Z (200, 14,884 B, sha256 `05173180…`); source `docs/skill-creation/best-practices.mdx` at main (14,608 B, sha256 `a729bc1d…`) | Ask "Would the agent get this wrong without this instruction?" and cut it if not; concise stepwise guidance beats exhaustive documentation; a skill body loads on activation, so every token competes. No dated-text rule, and the specification re-opened byte-identical to S018 states none either | mined | 2026-10-22 | 90d | corpus/knowledge/alwayson-source-basis-round53.md (proposed) |

Notes for integration:

- S045 shares its URL and bytes with S019. If the L1 prefers one row per source, fold `:572-583` into S019's `scope` and `teaches` (and keep its frontmatter teaches) instead of landing S045; both options preserve the quote.
- S048 supersedes S004, whose teach (conflict order) is carried in the new `teaches` cell; `status` moves from `queued` to `mined`.
- `ScribeCopilotCli.md` §5 drafts a row for the Copilot concept page (`custom-instructions.md`, `6e7964dc…`). My fetch of that page at 20:08:42Z is byte-identical to theirs, so that row needs no second draft; S049 covers the how-to's limitations block instead.
- The source rows for the Claude Code changelog, Codex releases, agents.md releases and the GitHub Copilot changelog are **not** drafted: they are sweep evidence for a negative, not admitted teaching sources. Their hashes are in §8.2.

## 7. Findings for the L1

1. **Attribution split (main finding).** The dated-text rule is stated by Anthropic for Skill content (`best-practices.md:576`) and by no authority for always-on files (§5). The box may not be credited to a vendor as written; the docstring paragraph in §3 is the fix. This also means the `alwayson.04` detail string must not say "vendor rule" anywhere.
2. **The pinned case set cannot catch the authority's own bad example.** The counter pins a month-**day** FAIL (`November 1`) but not month-**year** (`August 2025`), which is Anthropic's bad example, and not year-month (`2025-08`). A detector built to the pinned cases will pass the authority's own example. This is not a counter defect (the counter is frozen and does not claim coverage) but it is a docstring fact: the check approximates the rule and misses month-year.
3. **Over-flag direction measured live.** A literal detector flags provenance headings: `~/.agents/AGENTS.md:1` and `ufo-fsd-alpha/AGENTS.md:87,:139,:268`. Those are dated labels, not expiring rules; the box's wording still covers them ("No dated ... text"), so the live population fails the box today. The L1 should decide whether the C2 record reports this as an observation (the plan says a live run is an observation, not the claim) and whether the host file's dated title is the intended target of the rule.
4. **The round-7 evidence is historical.** `corpus/knowledge/alwayson-checklist-round7.md:30` locates the FAIL at host-file lines 48 and 51 in a 75-line file; the file today is 14 lines (`wc -l` → 14) and those lines do not exist. `ScoutAlwaysOnPop.md` §7 found this first; I re-verified the line count and the current line 1. The disposition string in `verifiers/checklist-baseline.json` (all 8 boxes) repeats the dead pointers; that is routed-defect material, not this seat's to edit.
5. **The `alwayson.07` Gate quote is on the same page** (`memory.md:436`, `:442`, `:452`, `:455`), including the vendor statement that a prose instruction is not an import. The C2 counter's `prose-mention` FAIL case rests on `:436`; the `two-rule-files` FAIL rests on `:357`; the `symlink-redirect` PASS rests on `:452-455`.
6. **Source stability (Q10).** Three byte-identity checks passed between independent fetches: `memory.md` `971d75bf…` (mine 20:05:00Z vs ScoutClaudeBehaviour 20:04:37Z), `agentskills.io/specification.md` `9a67de89…` (vs S018), platform `best-practices.md` `f0a5d61b…` (vs S019). No source moved during the sweep.
7. **Old-path hazard confirmed for Copilot.** The brief's `how-tos/configure-custom-instructions/...` route serves 200 HTML (708,144 B) but 404 as `.md`; the canonical route is `how-tos/copilot-on-github/customize-copilot/add-custom-instructions/...`. This is the Q30 "old path" failure mode, avoided in every quote above.

## 8. Gates, commands, artifacts

### 8.1 Commands run (with exit codes and observed output)

1. `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin log -1 --format='%H %cI'` → `3bb0a7a33e6eb585a83a1a55dee30b26079b1e36 2026-10-22T16:54:40-03:00`.
2. `unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE; python3 -B verifiers/check_alwayson_boxes.py --rev e78dff667237fba2e3cf9eccb802eff5bc9ea302` (lane root) → exit **1**:
   ```
   always-on boxes executed and discriminating 0 of 8
     alwayson.04: not counted (disposition unexecuted)
     alwayson.07: not counted (disposition unexecuted)
   ```
3. `git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r53/ScribeDatedAuthority/clone && git -C clone checkout -q 3bb0a7a3…` → `clone ok 3bb0a7a33e6eb585a83a1a55dee30b26079b1e36`.
4. All fetches in §8.2 used `curl -sSL --max-time N -A 'kotoba-research/1.0' -o <file> -w '%{http_code} %{size_download}'`; the manifest records each status and byte count.
5. `grep -rn -i -E "time-sensitive|time sensitive|become outdated|expiring facts|dated text" corpus/ SKILL.md PROVINCE.md README.md verifiers/` (lane root) → 2 hits (the lane's own rule: `corpus/knowledge/alwayson-checklist-round7.md:16`, `SKILL.md:371`).
6. `grep -rn -i -E "alwayson\.04|dated or transient" --include='*.md' --include='*.json' --include='*.py' .` (lane root, `.git` excluded) → `verifiers/checklist-baseline.json:223`, `verifiers/check_alwayson_boxes.py:10,66`, `plans/round-53.md:42,45,58`, `SKILL.md:371`, plus sibling reports.
7. `grep -c -i 'time-sensitive'` per authority bundle → Claude Code docs 1 (unrelated, `llms-full.txt:62088`), Codex docs 0, Copilot concept 0, agentskills spec 0, agentskills best-practices 0, agents.md 0, `memory.md` 0, `best-practices.md` 0, Claude Code `changelog.md` 0.
8. `grep -c -i 'become outdated'` over the same set → 1 total, on the Anthropic platform skills page (`:576`).
9. Candidate-date-pattern probe (`python3 -B` heredoc, 12 inputs, three patterns) → table in §4, exit 0.
10. `wc -l /home/vgpnk/.agents/AGENTS.md` → `14`; `sed -n '1,3p'` → the dated title in §4; `grep -n -E '[0-9]{4}-[0-9]{2}-[0-9]{2}'` over `kimi-code/AGENTS.md`, `opencodeufo/AGENTS.md`, `shokunin/AGENTS.md` → no match, exit 1.

### 8.2 Fetch manifest (scratch `fetch/`, filenames sanitized)

| URL | UTC | status | bytes | sha256 (first 8) |
|---|---|---|---|---|
| https://code.claude.com/docs/en/memory.md | 2026-10-22T20:05:00Z | 200 | 51,971 | `971d75bf` |
| https://code.claude.com/docs/en/best-practices.md | 2026-10-22T20:05:01Z | 200 | 36,360 | `b225977e` |
| https://agents.md/ | 2026-10-22T20:05:01Z | 200 | 81,690 | `06b65de9` |
| https://agentskills.io/specification.md | 2026-10-22T20:05:02Z | 200 | 7,608 | `9a67de89` |
| https://learn.chatgpt.com/docs/agent-configuration/agents-md.md | 2026-10-22T20:05:36Z | 200 | 9,149 | `9d1f87a2` |
| https://agentskills.io/skill-creation/best-practices.md | 2026-10-22T20:05:36Z | 200 | 14,884 | `05173180` |
| https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions (HTML, old path) | 2026-10-22T20:05:36Z | 200 | 708,144 | `4f0dbd79` |
| https://code.claude.com/docs/en/changelog.md | 2026-10-22T20:06:36Z | 200 | 1,090,388 | `c719b69d` |
| https://learn.chatgpt.com/llms.txt | 2026-10-22T20:06:40Z | 200 | 33,447 | `fc7b20ea` |
| https://code.claude.com/docs/llms.txt | 2026-10-22T20:06:41Z | 200 | 63,682 | `b7064ac5` |
| https://raw.githubusercontent.com/openai/codex/main/CHANGELOG.md | 2026-10-22T20:06:41Z | 200 | 330 | `c8458f99` |
| https://raw.githubusercontent.com/agentskills/agentskills/main/docs/specification.mdx | 2026-10-22T20:06:41Z | 200 | 7,166 | `b9079c0c` |
| https://raw.githubusercontent.com/agentskills/agentskills/main/docs/skill-creation/best-practices.mdx | 2026-10-22T20:06:41Z | 200 | 14,608 | `a729bc1d` |
| https://code.visualstudio.com/docs/copilot/customization/custom-instructions | 2026-10-22T20:06:41Z | 200 | 162,008 | `dc87f7c2` |
| https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions.md | 2026-10-22T20:07:01Z | 200 | 22,858 | `c29d67f0` |
| https://code.claude.com/docs/llms-full.txt | 2026-10-22T20:07:38Z | 200 | 9,614,681 | `1a581620` |
| https://learn.chatgpt.com/llms-full.txt | 2026-10-22T20:07:38Z | 200 | 2,549,875 | `3499a408` |
| https://raw.githubusercontent.com/github/docs/main/content/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions.md | 2026-10-22T20:07:40Z | 200 | 13,608 | `04cf53d3` |
| https://raw.githubusercontent.com/openai/agents.md/main/README.md | 2026-10-22T20:07:40Z | 200 | 2,015 | `60ec51c2` |
| https://github.com/openai/agents.md/releases.atom | 2026-10-22T20:07:40Z | 200 | 522 | `b9578d2f` (0 entries) |
| https://github.com/agentskills/agentskills/releases.atom | 2026-10-22T20:07:40Z | 200 | 539 | `86e3ba28` (0 entries) |
| https://github.com/openai/codex/releases.atom | 2026-10-22T20:07:40Z | 200 | 6,046 | `80dafdc7` (10 entries) |
| https://learn.chatgpt.com/docs/customization/overview.md | 2026-10-22T20:08:23Z | 200 | 9,482 | `e4f466bb` |
| https://www.anthropic.com/engineering/claude-code-best-practices | 2026-10-22T20:08:23Z | 200 | 770,825 | `020790cc` |
| https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | 2026-10-22T20:08:23Z | 200 | 240,108 | `ecc55d99` |
| https://docs.github.com/en/copilot/concepts/prompting-and-context/custom-instructions.md | 2026-10-22T20:08:42Z | 200 | 14,669 | `6e7964dc` |
| https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md | 2026-10-22T20:08:42Z | 200 | 8,730 | `00e45ea5` |
| https://raw.githubusercontent.com/github/docs/main/content/copilot/concepts/prompting-and-context/custom-instructions.md | 2026-10-22T20:08:43Z | 200 | 10,515 | `0ad782dd` |
| https://github.blog/changelog/label/copilot/feed/ | 2026-10-22T20:08:50Z | 200 | 46,175 | `10e7600c` (10 items) |
| https://code.claude.com/docs/en/errors.md | 2026-10-22T20:10:35Z | 200 | 549,839 | `99b04113` |
| https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices.md | 2026-10-22T20:10:36Z | 200 | 42,169 | `f0a5d61b` |
| https://docs.github.com/llms.txt | 2026-10-22T20:11:14Z | 200 | 28,642 | `c10af0cd` |
| https://github.com/openai/codex/releases | 2026-10-22T20:14:47Z | 200 | 387,795 | `a6febe28` |

Probes that returned no bytes worth keeping (each recorded because it shapes the sweep):

- https://developers.openai.com/codex/guides/agents-md.md → 200, redirect to the `learn.chatgpt.com` URL in the manifest;
- https://developers.openai.com/codex/agents-md.md → 404, 9 B; https://learn.chatgpt.com/docs/agents-md.md → 404, 9 B;
- https://learn.chatgpt.com/docs/changelog.md → 404, 9 B; https://developers.openai.com/codex/changelog.md → 404, 9 B;
- https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions.md → 404, 502 B;
- https://docs.github.com/en/copilot/concepts/custom-instructions → 404, 502 B; .../concepts/response-customization.md → 404, 502 B; .../concepts/about-customizing-github-copilot → 404, 502 B;
- https://raw.githubusercontent.com/github/docs/main/content/copilot/how-tos/configure-custom-instructions/add-repository-instructions.md → 404, 14 B;
- https://raw.githubusercontent.com/openai/agents.md/main/app/page.mdx → 404, 14 B; `agentsmd/agents.md` `app/page.tsx` → 404, 14 B;
- https://raw.githubusercontent.com/agentskills/agentskills/main/docs/changelog.mdx → 404, 14 B;
- https://api.github.com/repos/openai/agents.md/git/trees/main?recursive=1 and https://api.github.com/repos/github/docs/contents/... → 403, 280 B ("API rate limit exceeded for 179.218.13.209").

### 8.3 Artifacts

- Report (this file): `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-53/build/ScribeDatedAuthority.md`.
- Scratch clone: `/fast/scratch/hyaku/kotoba-r53/ScribeDatedAuthority/clone` at `3bb0a7a3…`.
- Fetched bytes and probes: `/fast/scratch/hyaku/kotoba-r53/ScribeDatedAuthority/fetch/` (the manifest filenames are the sanitized URL forms; the date-probe was run from `/fast/scratch/hyaku/kotoba-r53/ScribeDatedAuthority`).
- Independent records reused: `.ufo/waves/round-53/build/ScoutClaudeBehaviour.md` (§2 fetch hash, §6 prompt-audit is model-backed), `.ufo/waves/round-53/build/ScribeCopilotCli.md` (§2.5, §3.3, §5), `.ufo/waves/round-53/build/ScoutAlwaysOnPop.md` (§6–§7 population drift and dead pointers).

## 9. Out of scope and not claimed

- No instrument was written, run, or designed here; §4's probe is a candidate regex on strings, not the check. The counter still prints 0 of 8 (§8.1 item 2).
- No lane file was edited: not `SKILL.md`, not `verifiers/checklist-baseline.json`, not `corpus/SOURCES.md`, not the knowledge entry. The rows in §6 are drafts for the L1.
- No live box verdict is claimed. The population scan in §4 is mechanical, and `ScoutAlwaysOnPop` reached the same hits independently.
- Other clients' always-on records (opencode, Gemini CLI, omp) are other seats' scope; this report covers the five authorities its target names plus the Copilot surfaces a sibling already opened.
- The `alwayson.07` rule's own source basis was not re-derived beyond the quotes in §2.2; the plan's C2 statement cites the same page.
- Nothing was pushed, committed or staged anywhere; the sandbox clone was created and checked out, nothing else.
