# R73 wave 1 — ScribeEntryCn (C1 coverage: Chinese-vendor skill surfaces, entry draft)

**Verdict.** Entry drafted at `.ufo/waves/round-73/w1/build/ScribeEntryCn/entry.md` (18 427 B, 93 text lines),
with six text-extracted snapshots, a `MANIFEST.sha256` that verifies, and a fetch log. All 24 record
quotes were re-grounded against my own fetches (0 unbacked); every backticked token in every vendor-table
row occurs word-bounded in a page that row cites (TRAE 5, CodeBuddy 8, Kimi 11, Zhipu 3). **The Q45 census
reaches 4 of 4 vendors on the live pages, so C1's target stays `N == 4` — no lowering needed.** The staged
entry is wrong in two of its three "shared" patterns and carries one unsupported root token; both are
repaired below, not copied.

## Artifacts (all under `.ufo/waves/round-73/w1/build/ScribeEntryCn/`)

| file | bytes | note |
|---|---|---|
| `entry.md` | 18 427 | the draft; `S<<TRAE>>`-style id placeholders for the L1 to renumber |
| `snapshots/cn-trae-skills.md` | 13 302 | text-extracted snapshot |
| `snapshots/cn-codebuddy-ide-skills.md` | 4 768 | " |
| `snapshots/cn-codebuddy-cli-skills.md` | 28 773 | " |
| `snapshots/cn-kimi-zh-skills.md` | 8 321 | " |
| `snapshots/cn-kimi-en-skills.md` | 13 434 | raw markdown, whitespace-collapsed |
| `snapshots/cn-zhipu-skills.md` | 7 365 | raw markdown |
| `snapshots/MANIFEST.sha256` | 529 | `sha256sum -c` → all six OK |
| `fetch-log.tsv` | 2 388 | URL, status, date, bytes, sha256 (raw + snapshot) |
| `extract_html.py` | 1 119 | the extraction used for the four HTML pages |

Install for the L1: `cp entry.md corpus/knowledge/chinese-vendor-skill-surfaces-round73.md`;
`cp snapshots/*.md snapshots/MANIFEST.sha256 .ufo/waves/round-73/snapshots/`; replace `S<<TRAE>>` →
the registry id per source and add the six 11-cell rows (drafts in § Registry rows).

## Q45 census before data — 4 of 4 reachable

| vendor | root/placement token (count) | keys (count) | verdict |
|---|---|---|---|
| TRAE | `.trae/skills/` 3, `~/.trae-cn/skills` 1 | `name` 2, `description` 1 | backed |
| CodeBuddy | `.codebuddy/skills/` 2, `~/.codebuddy/skills/` 3 | `name`, `description`, `allowed-tools` 14, `disable-model-invocation` 1, `user-invocable` 6 | backed |
| Kimi Code | `.kimi-code/skills/` 2, `$KIMI_CODE_HOME/skills/` 1 (zh page) | `name` 9, `description` 5, `type` 4, `whenToUse` 4, `disableModelInvocation` 3, `arguments` 4 | backed |
| Zhipu | `/workspace/skills/<目录名>/` 1 | `name` 3, `description` 1 | backed, **exactly 3 tokens — no margin** |

Command (per-file counts, `grep -c -F`, order TRAE, CB-IDE, CB-CLI, Kimi-zh, Kimi-en, Zhipu):

```
$ for t in '.agents/skills/' 'allowed-tools' 'whenToUse' 'disableModelInvocation' 'license' '项目'; do printf '%-24s' "$t"; for f in cn-trae-skills.md cn-codebuddy-ide-skills.md cn-codebuddy-cli-skills.md cn-kimi-zh-skills.md cn-kimi-en-skills.md cn-zhipu-skills.md; do printf ' %3s' "$(grep -c -F -- "$t" "$f")"; done; echo; done
.agents/skills/            9   0   0   3   2   0
allowed-tools              0   1  14   0   0   0
whenToUse                  0   0   0   4   0   0
disableModelInvocation     0   0   0   3   0   0
license                    0   0   0   0   1   0
项目                       16   1  19   7   0   0
```

## Findings (each with its command)

**F1 — the staged pattern "all four now read the cross-vendor `.agents/skills/` root" is refuted: 2 of 4.**
The matrix above: TRAE 9, CodeBuddy IDE 0, CodeBuddy CLI 0, Kimi zh 3, Kimi en 2, Zhipu 0. TRAE reads it
behind a switch (`cn-trae-skills.md:389` "在 导入设置 部分，打开 启用 .agents 技能目录 开关。") and lets
`.trae/skills/` win a collision (`:375`); Kimi reads it at both scopes; CodeBuddy and Zhipu never name it.

**F2 — the staged pattern "all four separate a project scope from a user scope" is refuted.** Zhipu's page
never names a project scope (`项目` 0 hits, `~/` 0, `.agents` 0). Two vendors publish a scope order
(CodeBuddy `cn-codebuddy-cli-skills.md:1398` "Skill 来源：项目级 Skills 优先于用户级 Skills";
Kimi `cn-kimi-zh-skills.md:273` "Project > User > Extra > Built-in"), TRAE publishes only a root
collision order, Zhipu none. The entry states exactly that.

**F3 — TRAE's staged international root is unsupported and was dropped.** `grep -c -F '~/.trae/skills'
cn-trae-skills.md` → `0`; `grep -c -F '~/.trae-cn/skills'` → `1`. The page's string carries no trailing
slash, so the staged `~/.trae-cn/skills/` form would also fail a literal check; the row uses the page's
exact `~/.trae-cn/skills`.

**F4 — Kimi's own two pages contradict each other on roots and on vocabulary.** zh page
`cn-kimi-zh-skills.md:277-285` documents `.kimi-code/skills/`, `$KIMI_CODE_HOME/skills/`,
`~/.agents/skills/`, `.agents/skills/`; the GitHub page `cn-kimi-en-skills.md:34-42,61-65` documents
`~/.kimi/skills/`, `~/.claude/skills/`, `~/.codex/skills/`, `~/.config/agents/skills/`, `.agents/skills/`.
Counts: `.kimi-code/skills/` → `2 0`, `.kimi/skills/` → `0 2` (zh, en). Keys: `whenToUse` 4/0,
`disableModelInvocation` 3/0; the GitHub table lists `license`, `compatibility`, `metadata` instead
(`:168-174`). This is the entry's sharpest hazard and it is recorded as a contradiction, not resolved.

**F5 — CodeBuddy's own two surfaces contradict each other on required fields.** IDE page
`cn-codebuddy-ide-skills.md:157,174` presents `name`/`description` as required matter; CLI page
`cn-codebuddy-cli-skills.md:969` "| `name` | 否 | Skill 名称，未指定时使用目录名". Kimi's zh page
(`:255`) makes omission of either a parse failure. Required-ness is page-specific, not format-specific.

**F6 — Zhipu's `type:zai` / `type:custom` is not a SKILL.md key.** The frontmatter sentence is
`cn-zhipu-skills.md:37` "SKILL.md frontmatter 写 name 和非空 description"; `type` appears as the catalog
kind `:27-28` and as the mount-table field `:79` "| type | zai 或 custom |". The staged entry listed it
among "distinctive frontmatter"; the draft corrects that.

**F7 — the allowlist key is CodeBuddy-only among the four.** `allowed-tools` counts 0/1/14/0/0/0 (order
above); TRAE and Zhipu have no allowlist key at all. The only documented spelling tolerance is Kimi's own
alias list (`cn-kimi-zh-skills.md:249`, three spellings of `disableModelInvocation`; `:247` for
`whenToUse`). No page says it reads another vendor's spelling.

**F8 — the Qwen `allowedTools` sentence re-grounds but was not adopted.** The staged parent's sentence is
verbatim on the Qwen page, line 1020: "Qwen Code reads the `allowedTools` frontmatter field. An
`allowed-tools` field written for another agent is ignored." It is not in the entry: C1's predicate (b)
requires every cited id's host to be one of the four frozen hosts, so a fifth id would move the frozen set
(see P1). Flagged for the L1 rather than smuggled in.

**F9 — host existence check (observation, in the entry's hazard section).**
`ls -d ~/.kimi-code/skills ~/.agents/skills ~/.kimi/skills ~/.config/agents/skills ~/.codebuddy ~/.trae ~/.trae-cn`
prints `/home/vgpnk/.agents/skills` and `/home/vgpnk/.kimi-code/skills` and errors on the other five. It is
evidence about one host on 2026-10-25 for the zh page's roots and against the GitHub page's; the entry says
exactly that and claims nothing about discovery.

**F10 — no sibling lane holds these four vendors.** `grep -rlniE 'trae|codebuddy|bigmodel|zhipu'
--include=*.md */corpus/knowledge` from `/home/vgpnk/Projects/shokunin` → no output. The one adjacent lane,
kumitate, holds the host's Kimi skills plane (`kumitate-shokunin/corpus/knowledge/kimi-skills-plugins.md`,
an `ls`-and-`readlink` observation of `~/.kimi-code/skills/` read 2026-10-13); the entry's Limits names the
boundary and adopts none of it.

## Plan attacks (C1-relevant, for the L1)

**P1 — predicate (b)'s host set forbids a fifth vendor id.** "(b) every cited `S###` … a URL whose host is
one of `V`'s hosts (frozen: …)". A Qwen row in this entry would be a cited id whose host
(`qwenlm.github.io`) is not in that set, so the counter must read 3 of 4 or exit 2. Either the Qwen
comparison stays out (this draft's choice) or the predicate is amended **before** claim data; adopting it
after data is a miss.

**P2 — Zhipu's row has exactly the minimum tokens.** (a) wants "at least three, at least one root or
placement token and at least two keys": `/workspace/skills/<目录名>/` + `name` + `description` is exactly
3. Any trimming (e.g. dropping `description` because the page says "非空") drops the row below the floor.
Do not compress that row.

**P3 — the Kimi row must rest on the zh page.** The GitHub page alone would satisfy (a) (`.kimi/skills/` +
`name` + `description`) but would state roots that do not exist on this host and would lose both camelCase
keys; the draft cites zh for the row and GitHub only for the contradiction.

**P4 — snapshot plumbing.** (c) expects `.ufo/waves/round-73/snapshots/` and
`snapshots/MANIFEST.sha256`. My manifest lives in the build dir and was generated with bare names
(`sha256sum cn-*.md > MANIFEST.sha256`); copying the six files plus the manifest keeps `sha256sum -c`
passing. `sha256sum -c MANIFEST.sha256` → six `OK` lines (verified).

**P5 — the recheck line needs the browser user agent.** `curl -fsSL https://docs.trae.cn/ide_skills` without
`-A` returns `curl: (22) The requested URL returned error: 400`, so a recheck written without it prints `0`
for TRAE and would read as a moved page. The entry's recheck prints `3 2 3 2 2 1` (run verbatim from the
entry; the command is in the file).

## Tokens and claims dropped or corrected (explicit)

| staged item | disposition | evidence |
|---|---|---|
| TRAE `~/.trae/skills/` (international root) | dropped | `grep -c -F '~/.trae/skills'` → `0` |
| TRAE `~/.trae-cn/skills/` (trailing slash) | reshaped to the page's `~/.trae-cn/skills` | page prints no slash; `grep -c -F` → 1 |
| Zhipu `type:zai` / `type:custom` as frontmatter keys | reclassified as catalog/mount kinds | `cn-zhipu-skills.md:37` vs `:27-28,79` |
| "all four separate a project scope from a user scope" | corrected to 2 scope orders, 1 root order, 1 none | `项目` 0 hits on Zhipu |
| "both TRAE and Kimi make the scope a precedence rule" | TRAE publishes a root collision rule only | `cn-trae-skills.md:375` |
| "all four now read the cross-vendor `.agents/skills/` root" | corrected to 2 of 4 | matrix § Q45 |
| Qwen `allowedTools` sentence | re-grounded, not adopted | P1 |

## Commands (exact, with observed output)

1. Fetch, six pages, all `200` (`curl -sL --max-time 60 -A 'Mozilla/5.0' -o <f> -w '%{http_code}'`):
   `trae 200 112442`, `cb-ide 200 36633`, `cb-cli 200 217520`, `kimi-zh 200 79788`,
   `kimi-en 200 13528`, `zhipu 200 7381`; sha256s in `fetch-log.tsv`.
2. Quote audit (`python3`, entry text vs collapsed snapshots): `quotes 24 unbacked 0`; source-line
   quotes 6–10 whitespace tokens each (predicate (d) wants 5–25).
3. Row-token audit (word-bounded `re.search(r'(?<!\w)T(?!\w)')` per cited snapshot): TRAE 5/5,
   CodeBuddy 8/8, Kimi 13/13, Zhipu 3/3.
4. `sha256sum -c MANIFEST.sha256` → `cn-codebuddy-cli-skills.md: OK` … `cn-zhipu-skills.md: OK` (6 OK).
5. Lane ground sweep: `grep -rniE 'trae|codebuddy|kimi code|kimi-code|zhipu|bigmodel|moonshot' corpus
   SKILL.md PROVINCE.md` → 1 line (`corpus/knowledge/opencode-offer-trace-round8.md:84`), `wc -l` → `1`.
6. Recheck run verbatim from the entry → `3 2 3 2 2 1`.

## Registry rows (draft, for the L1 only — not landed)

Eleven cells `id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by`;
`kind` `docs` for the five doc pages and `repo` for the GitHub markdown (tier B, vendor documentation, as
Factory/pi in round 72). `used-by` must name `corpus/knowledge/chinese-vendor-skill-surfaces-round73.md`
exactly; `status` `mined`; `opened` `2026-10-25`; `recheck` `30d`. Six rows (TRAE, CB-IDE, CB-CLI, KIMI-ZH,
KIMI-EN, ZHIPU) with the URLs from the entry's `source:` lines and the located quotes already verified.

## Contract compliance

- Writes: only inside `.ufo/waves/round-73/w1/build/ScribeEntryCn/` and this report; scratch
  `/tmp/k73w1-ScribeEntryCn.*` deleted before returning. No lane file, no fleet repo, no sibling lane,
  no git index, no jj state touched.
- No gate run (not this seat's item, and `verifiers/check_cn_vendor_surfaces.py` does not exist at the
  current tip `ac8fc59` — `ls` → `No such file or directory`); no tool installed or upgraded; every command
  under the 120 s contention bound (longest: the six fetches, 4.5 s; the recheck, 6.9 s).
- Quotes ≤25 words, single-line, each found in its snapshot after whitespace collapse only; no credential
  material, no session URLs, no cookies.
