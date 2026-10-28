# Kb80R06ShokuknowSlice — kotoba slice of the absent-defect register, hand-checked

Seat: Kb80R06ShokuknowSlice (round 80 w1, assimilation duty, read-only).
Register (read-only input): `/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md` (375 lines, sha256 not re-derived here; mtime 2026-10-24 08:37, 83,621 bytes).
Census behind the register: `quote-lint-full-v5.json` (1,841 findings; kotoba verdict histogram: folded 21, no-gate-block 30, ABSENT 11, fetch-failed 6, no-quote-span 1, sweep-found 1).
Date of hand-check: 2026-10-27 (UTC evening). Fetch tool: curl 8.23.0, `-L -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36" --max-time 60`.
Method: each cited source fetched once; HTTP status + byte size + sha256 recorded; quoted anchor searched as an exact substring over the tag-stripped, script/style-removed, HTML-unescaped, whitespace-normalized body. "Found" means the contiguous string occurs in the body as fetched today.

## 1. Slice extraction (round-prompt §6.10 awk)

Command (lane cell, round cell, S-id cell; every emitted line carries an S-id; the `S236'`-style trailing backtick in the register's never-checked table is accepted):

```
awk -F'|' '$2==" `kotoba` " && $3 ~ /^ round[0-9]+ $/ && $4 ~ /^ S[0-9]+`? $/ \
  {printf "%s | %s | %s\n", $2, $3, $4}' \
  /home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md
```

Output (13 rows — 7 payload-absent + 6 never-checked; matches the register's own "## By lane" count `kotoba | 7` for payload-absent):

```
 `kotoba`  |  round3  |  S151
 `kotoba`  |  round4  |  S167
 `kotoba`  |  round5  |  S168
 `kotoba`  |  round5  |  S172
 `kotoba`  |  round5  |  S176
 `kotoba`  |  round6  |  S180
 `kotoba`  |  round6  |  S185
 `kotoba`  |  round10  |  S236`
 `kotoba`  |  round10  |  S237`
 `kotoba`  |  round10  |  S238`
 `kotoba`  |  round10  |  S239`
 `kotoba`  |  round10  |  S243`
 `kotoba`  |  round5  |  S169`
```

Register-format notes (observed, not defects of this slice): the never-checked table is a different 5-column shape (`lane | round | id | why it was not checked | cited source`) under the heading "Rows whose quotes were NEVER CHECKED"; its id cell renders as `S236'` (class cell merged). The payload-absent table is the 7-column `lane | round | id | class | cited source | quote(s) | note`. Multi-line quote cells span physical lines; the awk keys on row-start lines only.

## 2. Per-row verdicts — payload-absent class (register: "fabrication class — verify by hand")

### S151 (round3) — https://agentskills.io/skill-creation/optimizing-descriptions.md
Fetch: HTTP 200, 13,403 bytes, sha256 7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837. Genuine doc ("# Optimizing skill descriptions").
Register quote: `metadata-only routing loses 37–44 points at ~80K skills; the paper says 31–44 percentage points, overall gap +37.8. The replacement text is specified in CANNOT-ANSWER.md — unknown frontmatter fields are ignored (S150). So on the evidence held, Qwen Code is the side that diverges…`
Fragments searched: `metadata-only routing loses` — absent. `37–44` — absent. `80K skills` — absent. `CANNOT-ANSWER` — absent.
**Verdict: absent (confirmed).** Census `line` cells show the span is the kotoba lane's own editorial prose (a `corpus/SOURCES.md` row note about a measurement), not text claimed from this URL. The register class holds at string level; the actionable reading is a lint mis-extraction (lane note linted as a located quote), not a sourced quote that failed.

### S167 (round4) — https://agentskills.io/client-implementation/adding-skills-support.md
Fetch: HTTP 200, 20,446 bytes, sha256 07511caadbe1bad84d81477d0efce87bc2c7eaff562179522c083910586dfb06.
Register quote: `The lane holds this page as S002; this row records only that paragraph, which no lane entry cites. Re-check: refetch the…`
`lane holds this page as S002` — absent (it is lane meta-commentary by construction).
**Verdict: absent (confirmed); lint artifact.** Context: the note discusses this page's `### Trust considerations` paragraph; that heading IS present in the fetched body (verbatim: "Project-level skills come from the repository being worked on, which may be untrusted… only load them if the user has mar[ked]…"). The register quote itself is not source text and was never claimed as such.

### S168 (round5) — https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals
Fetch: HTTP 200, 900,228 bytes, sha256 72e66dc9ff917c8b54b597b0a82c545e1ab670d1ce8e5fed2f41069428c1d792. Full article body present.
Register quote: `section:` — absent as a located string (trivial fragment from the lane row's prose `…reliably" section: "In 56% of eval cases…`).
The lane row's real located quotes from this URL ARE present: `In 56% of eval cases, the skill was never invoked.` — FOUND; `Baseline (no docs) 53%` / `Skill (default behavior) 53%` table — FOUND.
**Verdict: register quote absent (confirmed); lint artifact — the row's substantive quotes verify present.** The defect is in the extraction, not the lane row.

### S172 (round5) — https://junie.jetbrains.com/docs/agent-skills.html
Fetch: HTTP 200, 38,509 bytes, sha256 a44a510e30445815b2f911fbaa77ca42e8f0504b3c4694507f053eb9425e9d21.
Register quote: `If a project-level and a user-level skills share the same name, the project-level skill takes precedence and the user-le` — absent as a contiguous string.
Present on the page (verbatim, tag-stripped): `If a project-level ( <projectRoot>/.junie/skills/<skill-name>/ ) and a user-level ( ~/.junie/skills/<skill-name>/ ) skills share the same name, the project-level skill takes precedence and the user-level skill is ignored.`
**Verdict: absent verbatim (confirmed); substance present with two elided parentheticals.** The recorded quote is a defective elision of text that IS on the page — correctable from the live page, not a fabrication. Register class holds at string level.

### S176 (round5) — https://agentskills.io/client-implementation/adding-skills-support.md (same fetch as S167)
Register quote: `The three-tier progressive disclosure table and the two` — absent (`three-tier progressive` absent; `three-tier` alone FOUND).
**Verdict: absent (confirmed); lint artifact.** The page has `## The core principle: progressive disclosure` with "the same three-tier loading strategy" table; the quoted span is the lane row's editorial prose ("were read in place. Re-check: refetch the `.md`…"), not claimed source text.

### S180 (round6) — https://web.archive.org/web/2026/https://ai.google.dev/gemini-api/docs/coding-agents?hl=ja
Fetch: HTTP 200, 113,443 bytes, sha256 47f486f2d023de0ab57bc801407e3059812bd13fd8e38ab446053d7b8d70760d. Genuine archived Japanese page ("Gemini MCP とスキルを使用してコーディング アシスタントを設定する").
Register quote: `スキルのインストール` — absent. Page headings include `インストールを確認する`, `API 開発スキルを追加する`; no `スキルのインストール` heading or string anywhere in the body.
**Verdict: absent (confirmed).** The staged row's claimed section anchor does not exist on the archived page as fetched today; nearest install-related heading is `インストールを確認する`.

### S185 (round6) — https://docs.roocode.com/features/skills
Fetch: HTTP 200, 71,129 bytes, sha256 fe801910f82e07631b3b5af3a2349fd75950eaabeda0280348b51c1aa92753e2. Full doc body present.
Register quote: `Skill locations` — absent as a heading or string. Page headings: `Skills`, `Why It Matters`, `What Skills Let You Do`, `How Skills Work`, `Creating Your First Skill`, `Directory Structure`, `Override Priority`, `Skill Discovery`, `Troubleshooting`, `Skills vs Custom Instructions vs Slash Commands`, `Skill Specification`, `See Also`.
**Verdict: absent (confirmed).** The location substance exists under `Creating Your First Skill` ("Choose a location — Global skills (available in all projects): …"), but the claimed "Skill locations" anchor is not on the page.

## 3. Per-row verdicts — never-checked class (register: "unverifiable, NOT a fabrication")

All six cited sources fetched HTTP 200 on 2026-10-27; the register carried no quote for these rows ("the cited source could not be fetched, so no quote was checked"). The underlying staged rows live in `/home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md` (read-only); their claimed anchors were checked against today's fetches. Staged-row mapping is by URL + round (each URL appears once in the staged append).

### S236 (round10, staged S316) — https://skills.sh/docs
Fetch: HTTP 200, 43,811 bytes, sha256 7f1798512952cadb88ff35969533fdf1d7980e182a90c5082b7bde1fa6384506.
Claimed anchor: the "How are you securing skills?" section, at the sentence advising installers. `How are you securing skills` — FOUND; `review skills before installing` — FOUND; `own judgment` — FOUND; `cannot guarantee` — FOUND.
**Verdict: now reachable; anchor PRESENT.**

### S237 (round10, staged S317) — https://skills.sh/audits
Fetch: HTTP 200, 483,592 bytes, sha256 0ea32a11a117ef354f6b3c745ebb62fdf246592a0bffdee17d3cfa325a8bbc2b.
Claimed anchor: introductory line above the per-skill table, three named auditors. `Gen Agent Trust Hub` — FOUND; `Socket` — FOUND; `Snyk` — FOUND.
**Verdict: now reachable; anchor PRESENT.**

### S238 (round10, staged S318) — https://code.claude.com/docs/en/security.md
Fetch: HTTP 200, 15,462 bytes, sha256 3d516a197892dc41847431f83ee8bb1357fd819fca3f0c1426c6e095d135586f.
Claimed anchor: trust-verification bullet in the workspace-trust section. `workspace trust` — FOUND; `trust dialog` — FOUND; `untrusted` — FOUND.
**Verdict: now reachable; anchor PRESENT.**

### S239 (round10, staged S319) — https://skills.sh/agent
Fetch: HTTP 200, 69,140 bytes, sha256 011bb18431a71aa79e5e403a709c185ebf334495d616c259134481d8246f9003.
Claimed anchor: introduction above the per-agent list, at the sentence stating the install promise. Page text: "Every AI coding agent that supports the open skills CLI. Install once, use across every s[ession]…" — `install once` FOUND, `every session` FOUND.
**Verdict: now reachable; anchor PRESENT.**

### S243 (round10, staged S323) — https://skills.sh/docs/api
Fetch: HTTP 200, 138,131 bytes, sha256 453ebb4e08d33d552ff7a82fc68d256169770b02a7bdb2cf885e3766aadfdcfe.
Claimed anchor: introductory paragraph above the authentication section. Page text: "Programmatic access to the skills.sh skill catalog, leaderboard, and search. Base URL https://skills.sh All endpoints are under /api/v1/ and served over HTTPS. Responses are JSON. Authentication …" — FOUND.
**Verdict: now reachable; anchor PRESENT.**

### S169 (round5, staged S249) — https://ai.google.dev/gemini-api/docs/coding-agents
Fetch: HTTP 200, 115,366 bytes, sha256 5a18b4a8ed792eb7268eb06a6233c5b3144a04287286d93cf3a2b15fca6d14c9. The staged row recorded a live-URL redirect loop and read from the Internet Archive instead; today the live URL serves 200 directly.
Claimed quote: `Skills come pre-installed in Google AI St…` — `Skills come pre-installed` FOUND.
**Verdict: now reachable (redirect loop no longer reproduces); anchor PRESENT.**

## 4. Count arithmetic

- Register slice: 13 rows = 7 payload-absent + 6 never-checked. Hand-checked this round: 13 of 13 (none left unchecked).
- Payload-absent (7): all 7 confirmed ABSENT as contiguous strings in the cited sources. Decomposition: 3 lint artifacts of lane editorial prose (S151, S167, S176); 2 fragment/elision artifacts whose row substance verifies present on the live page (S168, S172); 2 claimed section anchors that do not exist on the page, substance nearby under different headings (S180, S185). No row reclassifies to present at the quoted-string level; no row requires flipping the r79 disposition on its own.
- Never-checked (6): all 6 NOW REACHABLE (HTTP 200, 2026-10-27) and all 6 claimed anchors PRESENT in today's fetches. The register's "unreachable" stamp was time-of-register; it no longer holds.
- Census cross-check: 11 kotoba ABSENT findings collapse to the 7 payload-absent rows (S151 carries 5 findings); 6 fetch-failed findings map 1:1 to the 6 never-checked rows. Arithmetic reconciles: 7 + 6 = 13.
- Adoption: unchanged and closed (plan §Frontier step, r79 disposition). These verdicts update the register's fact pattern only; nothing here is adopted, appended to `merge/kotoba/`, or dispositioned beyond recording.

## 5. Evidence inventory (fetched bodies, discarded with scratch after hashing)

| register row | URL | http | bytes | sha256 (fetched body) |
|---|---|---|---|---|
| S151 | agentskills.io/skill-creation/optimizing-descriptions.md | 200 | 13,403 | 7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837 |
| S167, S176 | agentskills.io/client-implementation/adding-skills-support.md | 200 | 20,446 | 07511caadbe1bad84d81477d0efce87bc2c7eaff562179522c083910586dfb06 |
| S168 | vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals | 200 | 900,228 | 72e66dc9ff917c8b54b597b0a82c545e1ab670d1ce8e5fed2f41069428c1d792 |
| S172 | junie.jetbrains.com/docs/agent-skills.html | 200 | 38,509 | a44a510e30445815b2f911fbaa77ca42e8f0504b3c4694507f053eb9425e9d21 |
| S180 | web.archive.org/web/2026/https://ai.google.dev/gemini-api/docs/coding-agents?hl=ja | 200 | 113,443 | 47f486f2d023de0ab57bc801407e3059812bd13fd8e38ab446053d7b8d70760d |
| S185 | docs.roocode.com/features/skills | 200 | 71,129 | fe801910f82e07631b3b5af3a2349fd75950eaabeda0280348b51c1aa92753e2 |
| S236 | skills.sh/docs | 200 | 43,811 | 7f1798512952cadb88ff35969533fdf1d7980e182a90c5082b7bde1fa6384506 |
| S237 | skills.sh/audits | 200 | 483,592 | 0ea32a11a117ef354f6b3c745ebb62fdf246592a0bffdee17d3cfa325a8bbc2b |
| S238 | code.claude.com/docs/en/security.md | 200 | 15,462 | 3d516a197892dc41847431f83ee8bb1357fd819fca3f0c1426c6e095d135586f |
| S239 | skills.sh/agent | 200 | 69,140 | 011bb18431a71aa79e5e403a709c185ebf334495d616c259134481d8246f9003 |
| S243 | skills.sh/docs/api | 200 | 138,131 | 453ebb4e08d33d552ff7a82fc68d256169770b02a7bdb2cf885e3766aadfdcfe |
| S169 | ai.google.dev/gemini-api/docs/coding-agents | 200 | 115,366 | 5a18b4a8ed792eb7268eb06a6233c5b3144a04287286d93cf3a2b15fca6d14c9 |

(12 unique URLs for 13 rows — S167 and S176 cite the same page. Fetch run completed 2026-10-27 ~23:14 UTC; all 12 HTTP 200, zero fetch failures.)
