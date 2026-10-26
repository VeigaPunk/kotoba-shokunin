# ExecQuarR74 — quarantine hand-check (addendum §10), round 74 wave 1

**Verdict: 13 of 13 kotoba quarantine rows re-checked with fresh fetches on 2026-10-25 —
8 `adoptable`, 5 `refused` as quotes, 0 `unverifiable`.** All 13 cited pages answered HTTP 200; no row
is a fabrication of page content, and **every** row's *payload* quote (the span the staged row
actually carries) is locatable at a `path:line` — the 5 refusals are the register's flagged
fragment, not the payload: S151 is the lane's own SkillRouter bullet re-attributed to an
agentskills page, S167/S176 are prose/paraphrase fragments, S180/S185 name page sections that do
not exist. Compared with round 72, **6 verdicts change** (S236, S237, S238, S239, S243, S169:
`unverifiable` → `adoptable`, with the located spans), 0 change toward fabrication. Both C1
priority pages got an independent fetch and both staged quotes locate (using-scripts 12 078 B,
quickstart 4 080 B — byte counts equal to the staged ones).

Seat: `ExecQuarR74`. Lane `kotoba-shokunin`, base `1e03d19`, plan `329e7d9`. No parent/fleet/jj lane
state touched; no tool installed (nothing needed). Scratch `/tmp/k74w1-ExecQuarR74.8VNA` deleted.

---

## 1. Method (reproducible)

Slice re-derived and diffed, identical (13 data rows):

```
R=/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md
awk -F'|' -v l='kotoba' '$2 ~ ("`" l "`") && $3 ~ /round[0-9]+/ && $4 ~ /S[0-9]+/ {print $4, $5}' "$R" \
  > /tmp/k74w1-ExecQuarR74.8VNA/rederived.txt
diff /tmp/k74w1-ExecQuarR74.8VNA/rederived.txt \
  .ufo/waves/round-74/assimilation/quarantine-slice
```
→ no diff output, `wc -l` = 13.

Because the register's ids collide with the package's (finding F1), every row is matched **by URL**:
register row → URL → staged row in `/home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md`
→ lane row in `corpus/SOURCES.md` (where one exists). Each URL fetched with
`curl -sL --max-time 60 -A 'Mozilla/5.0'`, HTTP status / bytes / sha256 / effective URL / date
recorded in `.ufo/waves/round-74/w1/build/ExecQuarR74/fetch-log.tsv`; text-extracted snapshots
(HTML pages only; `.md` pages kept verbatim) under `.../build/ExecQuarR74/snap/`.
All fetches 200. Two raw bodies exceeded the 300 KB snapshot cap (vercel 901 177 B,
skills.sh/audits 484 518 B): bytes and sha256 were taken and the raw deleted; extracted text kept.

## 2. Row verdicts

`register_id` is the register's own numbering; `package_row` is the staged row found by URL.
Evidence paths are `build/ExecQuarR74/snap/<file>:<line>`.

| reg. id | class | URL | pkg row | lane row | verdict | located |
|---|---|---|---|---|---|---|
| S151 | payload-absent | agentskills.io/skill-creation/optimizing-descriptions.md | S231 | S213 | **refused** (span absent) | payload quotes at `optimizing-descriptions.txt:9,41,19` |
| S167 | payload-absent | agentskills.io/client-implementation/adding-skills-support.md | S247 | S002 | **refused** (span is prose) | payload `adding-skills-support.txt:93` |
| S168 | payload-absent | vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals | S248 | — | **adoptable** (heading fold) | `vercel-agents-md.txt:119,120,97` |
| S172 | payload-absent | junie.jetbrains.com/docs/agent-skills.html | S252 | S206 | **adoptable** (2 code-span fold) | `junie-agent-skills.txt:72-74` |
| S176 | payload-absent | agentskills.io/client-implementation/adding-skills-support.md | S256 | S002 | **refused** (paraphrase) | payload `adding-skills-support.txt:143` |
| S180 | payload-absent | web.archive.org/…/ai.google.dev/gemini-api/docs/coding-agents?hl=ja | S260 | — | **refused** (section label absent) | payload `google-ja-archive.txt:196,200` |
| S185 | payload-absent | docs.roocode.com/features/skills | S265 | S203 | **refused** (section label absent) | payload `roocode-skills.txt:81,89` |
| S236 | unreachable→unverifiable | skills.sh/docs | S316 | — | **adoptable** | `skillssh-docs.txt:30,32` |
| S237 | unreachable→unverifiable | skills.sh/audits | S317 | — | **adoptable** | `skillssh-audits.txt:6,8-11` |
| S238 | unreachable→unverifiable | code.claude.com/docs/en/security.md | S318 | — | **adoptable** | `claude-security.txt:62` |
| S239 | unreachable→unverifiable | skills.sh/agent | S319 | — | **adoptable** | `skillssh-agent.txt:6` |
| S243 | unreachable→unverifiable | skills.sh/docs/api | S323 | — | **adoptable** | `skillssh-api.txt:6,11` |
| S169 | unreachable→unverifiable | ai.google.dev/gemini-api/docs/coding-agents | S249 | — | **adoptable** | `google-coding-agents.txt:200,224` |

Counts: `awk -F'\t' 'NR>1{print $6}' build/ExecQuarR74/verdicts.tsv | sort | uniq -c`
→ `8 adoptable`, `5 refused`, `0 unverifiable`.

### 2a. The five refusals, each with its sweep

**S151 — refused.** The flagged span is not on the page, and it is the lane's own text:

```
$ grep -nE '37|44 point|metadata' snap/optimizing-descriptions.txt ; echo exit=$?
exit=1
$ grep -nF 'metadata-only routing loses 37–44 points at' corpus/SOURCES.md
255:- SkillRouter (arXiv 2603.22455) — metadata-only routing loses 37–44 points at ~80K skills.
297:- SkillRouter (arXiv 2603.22455) — metadata-only routing loses 37–44 points at ~80K skills.
```
The census paired a lane-corpus bullet with the row's cited *URL* (the row's three real quotes —
`optimizing-descriptions.txt:9,41,19` — are present, so S231 is usable as staged). r72's
`ExecQuar01.md` traced the same span to arXiv 2603.22455 and to the lane's own bullet at
`corpus/SOURCES.md:238,280` (r72's base); at base `1e03d19` the same bytes sit at `:255,297`,
duplicated. Same finding, current line numbers.

**S167 — refused.** Flagged span `The lane holds this page as S002; this row records only that`.

```
$ grep -cF 'The lane holds this page as S002' corpus/SOURCES.md
0
$ grep -cF 'The lane holds this page as S002' /home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md
0
$ grep -cF 'this row records only that' SOURCES.append.md
1
```
Not page text, not even verbatim row text: an assembled fragment of the staged row's scope/`used-by`
prose. The page's own trust sentence is present at `adding-skills-support.txt:93`:
"Project-level skills come from the repository being worked on, which may be untrusted" … dropped
bytes (same line, 28 words): "…(e.g., a freshly cloned open-source project). Consider gating
project-level skill loading on a trust check — only load them if the user has marked the project
folder as trusted." — and the quoted tail "This prevents untrusted repositories from silently
injecting instructions into the agent's context." (11 words).

**S176 — refused.** Flagged span `The three-tier progressive` occurs in neither file
(`grep -cF` lane 0 / package 0); `three-tier` occurs once in the package's S256 locator. The page
carries the referent, `adding-skills-support.txt:22`: "Every skills-compatible agent follows the
same three-tier loading strategy:" — a paraphrase, not a quote. Payload quote present at :143:
"The lenient approach above deliberately relaxes these to improve compatibility with skills authored
for other clients." (16 words; the line's leading spec-link clause dropped).

**S180 — refused.** Flagged span `スキルのインストール` is a section name the page never had:

```
$ grep -c 'スキルのインストール' snap/google-ja-archive.txt snap/google-ja-live.txt
snap/google-ja-archive.txt:0
snap/google-ja-live.txt:0
$ grep -nE 'インストール' snap/google-ja-archive.txt | head
206:skills.sh でインストールする
231:インストールを確認する
```
The archived (2026-09-08) page's install sections are 「API 開発スキルを追加する」,
「skills.sh でインストールする」, 「インストールを確認する」, 「スキルの検証」. The *payload* is
present: the MCP-fallback sentence at `:196` (matched after whitespace collapse) and
「skills.sh : 推奨。ポータブル エージェントの動作に関するオープン標準。」 at `:200`.

**S185 — refused.** Flagged span `Skill locations` is a section name the page does not have:

```
$ grep -nc 'Skill locations' snap/roocode-skills.txt
0
$ sed -n '79p' snap/roocode-skills.txt
1. Choose a location
```
The payload is present and is the load-bearing text, `:81` / `:89`:
"# Linux/macOS — Roo-specific (higher priority)" (5 words) and the scope line
"Project skills override global skills, mode-specific override generic".

### 2b. The two fold cases (adoptable, corrected not refused)

**S168.** Flagged span `section:` is a fold artifact — the page's H2 is real:
`grep -c 'section:' raw (before deletion) → 0`; the rendered heading is
`vercel-agents-md.txt:119` "Copy link to heading Skills weren't being triggered reliably", and the
payload is `:120` "In 56% of eval cases, the skill was never invoked." (10 words).

**S172.** The staged quote is complete only after dropping the two inline `<code>` parentheticals
(they carry the paths, and the extractor breaks lines at them):

```
$ sed -n '72-74p' snap/junie-agent-skills.txt
If a project-level ( <projectRoot>/.junie/skills/<skill-name>/
) and a user-level ( ~/.junie/skills/<skill-name>/
) skills share the same name, the project-level skill takes precedence and the user-level skill is ignored.
```
Quoted tail: ") skills share the same name, the project-level skill takes precedence and the
user-level skill is ignored." (16 words). Raw HTML confirms one occurrence
(`grep -c 'takes precedence' raw → 1`).

### 2c. The six previously-unverifiable rows (now located)

| row | command | output (quoted ≤25 words) |
|---|---|---|
| S236 | `sed -n '30p;32p' snap/skillssh-docs.txt` | "How are you securing skills?" / "We encourage you to review skills before installing and use your own judgment." |
| S237 | `sed -n '6p' snap/skillssh-audits.txt` | "Combined security audit results from Gen Agent Trust Hub, Socket, and Snyk." (columns `Gen`/`Socket`/`Snyk` at `:8-11`) |
| S238 | `sed -n '62p' snap/claude-security.txt` | "Claude Code shows the workspace trust dialog when you start it in a folder you haven't trusted" |
| S239 | `sed -n '6p' snap/skillssh-agent.txt` | "Install once, use across every session." |
| S243 | `sed -n '6p;11p' snap/skillssh-api.txt` | "Programmatic access to the skills.sh skill catalog, leaderboard, and search." / "Authentication" |
| S169 | `sed -n '200p;224p' snap/google-coding-agents.txt` | "Summary of agent resources" / "Install Gemini agent skills" |

Two calibration notes on these:
- **S238's locator cell is wrong about the section** — the page has no "workspace trust" section;
  the bullet sits under `### Additional safeguards` (`claude-security.txt:58`). The quote is real.
- **S243's "not anonymously reachable" is an inference**, not a page sentence: the auth section
  (`:11-13`) describes Vercel OIDC auth and never states that unauthenticated calls are refused.
  Usable, but a wave-2 reviewer should not treat that clause as quoted.

## 3. C1 priority pages — independent verdicts (my own fetches)

These two pages are **not in the register at all** (`grep -cE 'using-scripts|quickstart'` on the
register → `0`), so they are not quarantine rows; the assignment's "S236/S237" for them are the
**package's** ids. Independent verdicts:

- **package S236 — agentskills.io/skill-creation/using-scripts.md → adoptable.** HTTP 200,
  12 078 B (equal to the staged byte count), sha256 `2cd7727…`:
  ```
  $ sed -n '9p' snap/using-scripts.txt
  Skills can instruct agents to run shell commands and bundle reusable scripts in a `scripts/` directory.
  ```
  18 words of a line whose remaining 20 words ("This guide covers one-off commands, self-contained
  scripts…") were dropped. Section `## One-off commands` at `:11`. Rule-token availability on the
  page (mechanical counts, `grep -cF`): `pipx run` 3, `npx eslint@9` 2, `uvx ruff` 1,
  `scripts/` 23.
- **package S237 — agentskills.io/skill-creation/quickstart.md → adoptable.** HTTP 200, 4 080 B
  (equal to staged), sha256 `7c480b4…`:
  ```
  $ sed -n '21p' snap/quickstart.txt
  A skill is a folder containing a `SKILL.md` file. VS Code looks for skills in `.agents/skills/` by default. Create `.agents/skills/roll-dice/SKILL.md` in your project:
  $ sed -n '17p' snap/quickstart.txt
  > This tutorial uses VS Code, but Agent Skills are an open format. The same skill works in any compatible agent, including Claude Code and OpenAI Codex.
  ```
  Quoted: 18 words from `:21` (trailing "Create … project:" dropped) and 14 words from `:17`
  (leading clause dropped). Sections `## Prerequisites` `:11`, `## Create the skill` `:19`.
- **Context for the Q45 census (not my claim):** `best-practices.md` also fetches 200, 15 060 B
  (sha256 `ab9f3b6…`) and carries section headings that are quotable rule tokens, exact case:
  `## Calibrating control` `:94`, `### Match specificity to fragility` `:98`,
  `### Provide defaults, not menus` `:127`, `### Favor procedures over declarations` `:145`.
  The plan's base sweep probed lowercase `calibrating control` / `favor procedures`; the page's
  headings capitalise, so a case-sensitive sweep of the page will show 0 for those two unless the
  census seat matches case-insensitively or quotes the headings as printed.

## 4. Differences from round 72 (labels vs substance)

The r74 rubric asks whether the **staged quote locates**. r72's rule (`ExecQuar08.md`, "Verdict") was
that a prose class cell leaves "no source span in the row to locate", so those rows stay
`unverifiable` even when the page fetches and the anchor is found. That is the whole of the label
difference; I opened r72's per-row files rather than its summary line:

| row | r72 (`w1/ExecQuarNN.md`) | r74 | what actually differs |
|---|---|---|---|
| S236 | `unverifiable-class` (08) | **adoptable** | 08 already recorded the served body byte-identical (`sha256 54828058…` — my fetch equals it) and the anchor; the label stayed `unverifiable` for lack of a register span. I pin `:30,:32` |
| S237 | `unverifiable-class` (09) | **adoptable** | 09 recorded HTTP 200, 484 518 B and the "Combined security audit results…" text but pinned no quote; I pin `:6` and the three columns `:8-11` |
| S238 | `unverifiable-class` (10) | **adoptable** | 10 recorded 200 / 15 462 B and located the staged S318 anchor bullet; label-only. I pin `claude-security.txt:62` and note the staged "workspace-trust section" label is wrong (the bullet sits under `### Additional safeguards`) |
| S239 | `unverifiable-class` (11) | **adoptable** | 11 recorded 200 and the staged `S319` mapping; label-only. I pin `:6` |
| S243 | `unverifiable-class` (12) | **adoptable** | 12 retired the row as superseded by staged `S323` without pinning a line; I pin `:6,:11` and flag the "not anonymously reachable" clause as inference |
| S169 | `unverifiable-class` (13) | **adoptable** | 13 already said 200, no redirects, "carries the exact sentence the staged sibling row S249 quotes"; label-only. I pin `:200,224` |
| S151 | refuse, fabrication class (01) | refused | same; 01 traced the span to arXiv 2603.22455 and to the lane's own bullet at `corpus/SOURCES.md:238,280` (r72's base). At base `1e03d19` that bullet reads `:255,297` — same bytes, later lines |
| S167, S176 | refuse (02, 05) | refused | same labels; both payload quotes located (`:93`, `:143`) |
| S180 | refuse, fabrication class (06) | refused | same; 06 swept live ja, `.md` export and other snapshots; I re-swept the 2026-09-08 archive and the live ja page (0 hits each) |
| S185 | refuse (07) | refused | same; 07 already called the staged anchor bad and the payload present; I pin `:81,:89` and record the redirect |
| S168, S172 | corrected / adoptable (03, 04) | adoptable | unchanged |

**Net: 6 labels change, 0 of r72's observed facts are contradicted, and most of the located
spans were already in r72's files** — the r74 rubric (does the staged quote locate?) is what moves
the labels, not new evidence. Genuinely new this round: (a) all 17 bodies re-fetched and
sha256-pinned on 2026-10-25 (r72 kept hashes only for some); (b) the live Japanese page has been
*reworded* since the 2026-09-08 archive (F3b) — r72 checked it only for the absent heading;
(c) the id chain is pinned from the package's own `ID-REMAP.md` (F1); (d) two calibration flags on
staged locators (S238's wrong section name, S243's inference clause).

## 5. Findings for the L1 (not claims)

**F1 — three id epochs, and the slice sits in the wrong one for positional lookup.** The register's
kotoba ids (S151…S243) are neither the lane's registry ids nor the package's staged ids:

```
$ grep -oE '^\s*\|\s*S[0-9]{3,}\s*\|' corpus/SOURCES.md | grep -oE 'S[0-9]+' | sort -u | sed -n '1p;$p'
S001
S222
$ grep -nF 'junie.jetbrains.com' corpus/SOURCES.md
147:| S206 | Junie — Agent Skills — …
$ grep -nE 'S23[5-9]|S24[0-3]|epoch' /home/vgpnk/Projects/shokuknow/lanes/kotoba/ID-REMAP.md | head
24:| round10 | `S242` | `S315` |
25:| round10 | `S243` | `S316` |
121:| round3 | `S162` | `S235` |
122:| round4 | `S163` | `S236` |
```
Register S172 (junie URL) is lane **S206**; S151 (optimizing-descriptions) is lane **S213** (`:153`);
S185 (roocode) is lane **S203** (`:144`); S167/S176 (adding-skills-support) are lane **S002**
(`:15`). Register S236/S237 (round10, skills.sh docs/audits) are package **S316/S317** via
`ID-REMAP.md:25-26`; the package's *current* S236/S237 — the two agentskills pages the C1 entry cites
— are round4 rows (`ID-REMAP.md:122-123`), a different epoch. So the assignment's
"S236 (using-scripts), S237 (quickstart)" and the register's S236/S237 name **different pages**;
both were checked above and both resolve adoptable, but a positional hand-check would silently
swap them. The plan's collision note (S203–S222) understates the problem: an id alone is not a key.

**F2 — several flagged spans are citation fragments, not page quotes.** S151 is the lane's own
corpus bullet; S167 is assembled row prose; S176 is a paraphrase; S180 and S185 are section labels.
A census that extracts *all* quoted/backticked spans from a registry row will keep producing
`payload-absent` rows that are not payloads. The register lost no real quote: every one of the 13
rows' actual payload spans is locatable, with three documented folds (heading, two code spans,
whitespace).

**F3a — package row S249's "redirects in a loop" premise is false today** (r72's `ExecQuar13.md`
already observed this):

```
$ curl -s -o /dev/null -w '%{http_code} %{url_effective} redirects=%{num_redirects}\n' -L --max-time 30 \
    -A 'Mozilla/5.0' 'https://ai.google.dev/gemini-api/docs/coding-agents'
200 https://ai.google.dev/gemini-api/docs/coding-agents redirects=0
$ curl … '…?hl=ja'  → 200 …?hl=ja redirects=0 (122 506 B)
```
The English live page carries the staged quotes (`:200,224`, fallback sentence matched after
whitespace collapse) and the extracted text is identical to the 2026-10-23 archive snapshot on the
checked band (`diff <(sed -n '190,240p' live) <(sed -n '190,240p' archive)` → empty), so S249's
re-point needs an appended correction rather than a removal (never a rewrite, per r73 item 3).

**F3b — the Japanese page has been reworded since S260's archive pin** (new this round; r72 checked
the live ja page only for the absent heading). The live page is reachable — `?hl=ja` → `200`,
`redirects=0`, 122 506 B — but its install section now reads differently:

```
$ sed -n '220p' snap/google-ja-live.txt
Gemini エージェント スキルをインストールする
$ grep -n 'llms.txt' snap/google-ja-live.txt | head -2
216:クリーンな Markdown ページと llms.txt
222:スキルは Gemini Docs MCP サーバーと連携して動作します。エージェントに MCP サーバーがインストールされていない場合、スキルは llms.txt
```
The archived (2026-09-08) page says 「スキルのインストール」-free headings 「API 開発スキルを追加する」
/ 「インストールを確認する」 and the fallback sentence 「…フォールバックとして ai.google.dev から
llms.txt を取得します。」 (`google-ja-archive.txt:196`). So S260's archived quote is still the only
carrier of its exact archived wording, and its "live not reachable" premise is stale in a second
way: reachable *and* changed.

**F4 — `docs.roocode.com` now redirects.** `docs.roocode.com/features/skills` → `200
https://roocodeinc.github.io/Roo-Code/features/skills/` (71 129 B). The staged locator's "Skill
locations" section does not exist under either address; the payload does.

**F5 — `skills.sh` redirects to `www.skills.sh`** (`/docs`, `/audits`, `/agent`, `/docs/api` all
200 on `www`). Staged rows cite the apex; content is served. If a counter pins URLs, apex vs `www`
is a live difference, not a stale source.

## 6. Bounds (what this seat did not observe)

- No payload span was judged for *truth* or for boundary correctness — that is the wave-2 reviewers'
  call; I only located spans.
- The quoted Japanese section name may exist under a variant I did not normalise (I tried NFKC +
  whitespace-stripped search on both snapshots; 0). The sweeps are my evidence, not a claim of
  universal absence.
- `using-scripts` and `quickstart` content equality with the 2026-10-23 fetch is unobserved — the
  package holds no snapshots (`ls` shows only `MERGE-REPORT.*`, `SOURCES.append.md`, `knowledge/`);
  only the byte counts match.
- r72's per-row files were opened for rows 01, 06, 07, 08, 09, 10, 11, 12 and 13; rows 02–05 were
  taken from the lesson summary and this round's own re-fetch.

## 7. Evidence written

- `.ufo/waves/round-74/w1/build/ExecQuarR74/fetch-log.tsv` — 17 fetches: URL, HTTP, bytes, sha256,
  effective URL, date, notes.
- `.../build/ExecQuarR74/verdicts.tsv` — the 13-row table above, machine-readable.
- `.../build/ExecQuarR74/evidence.txt` — sweep transcripts (exit codes included).
- `.../build/ExecQuarR74/snap/*.txt` — text-extracted snapshots (all ≤300 KB);
  `.../build/ExecQuarR74/raw/*.raw` — raw bodies kept where ≤300 KB (junie kept for the code-span
  fold; vercel and audits raws deleted after sha256 was taken).
- Report: `.ufo/waves/round-74/w1/ExecQuarR74.md` (this file).

Nothing outside `.ufo/waves/round-74/` was written; no committed lane file, no `merge/kotoba`, no
register file touched; no gate was run (wave-1 editing rules), no tool installed.
