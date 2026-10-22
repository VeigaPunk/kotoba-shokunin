# SrcOpencodeDocs — round-50 build, C1 source (frontier step)

**Result: HOLDS — the opencode skills page was opened by ordinary means and documents no tie-break between two skills whose descriptions both match (Q14 sweep: every arbitration pattern → 0).** The page does document how a description reaches the model (`<available_skills>` in the `skill` tool description), a 1–1024 character description cap, one name-uniqueness rule and one per-skill exclusion key (`opencode/autoinvoke`).

Lane: kotoba-shokunin at `f30464660c675d1c1e2851a3bf0366a3aaffe5a8`. Lane files untouched except this report (read-only seat). Scratch: `/fast/scratch/hyaku/kotoba-r50/build/src-opencode-docs/`. No tool was installed or upgraded (none needed); no `sudo`, no pacman transaction.

## Fetch record (both routes, two fetches each, byte-identical)

| route | HTTP | bytes | sha256 | accessed (UTC) |
|---|---|---|---|---|
| `https://opencode.ai/docs/skills.md` | 200 (`text/plain; charset=utf-8`) | 5365 | `f10ced73971ce83b85f41395e2e15a683fe5a874e9057fc9d13da5f5a1bf8561` | 2026-10-22T12:28:29Z (first), 2026-10-22T12:31:20Z (second, identical) |
| `https://opencode.ai/docs/skills` | 200 (`text/html`) | 73201 | `4d96fa569dd25469e085b3743ee7e5a53263792fb919b7591bd7b8397a3404f0` | 2026-10-22T12:28:25Z (first), 2026-10-22T12:31:21Z (second, identical) |

Both routes are served without a bot gate; `curl -sS -L` only, exit 0. The HTML page carries its own revision stamp in the footer: `<time datetime="2026-10-20T22:40:11.000Z">Oct 20, 2026</time>` next to the text `Last updated:`. The `.md` variant carries no date (0 hits for `last updated`), so the two routes are byte-stable but the page is unversioned apart from that footer date.

Structural check: the `.md` and the extracted HTML text agree. The HTML has 13 `<h1>/<h2>/<h3>` (`Agent Skills` = page title, `On this page` = nav, plus the 11 page sections); the markdown has 13 `##` lines — the same 11 section titles, plus `What I do` and `When to use me`, which sit inside the fenced example block rather than being page sections. Every prose line of the HTML body is present in the markdown except site chrome (`Skip to content`, `Select language`, `On this page`, `Found a bug? Open an issue`, `Custom Tools`, the language names). So the markdown is a faithful, complete copy of the page body; quotes below are anchored to the `.md` line numbers and, where given, to the extracted-HTML line numbers.

## Located quotes (all ≤25 words, verbatim)

Line numbers are `skills.md` (the fetched `.md` route, 230 lines); `html.txt` is the tag-stripped text of the HTML route.

| point | quote | location |
|---|---|---|
| how the model sees skills | "OpenCode lists available skills in the `skill` tool description." | § Recognize tool description, `skills.md:110` (html.txt:244) |
| what each entry carries | "Each entry includes the skill name and description:" | § Recognize tool description, `skills.md:111` (html.txt:247) |
| the listing shape | `<available_skills>` / `<skill>` / `<name>` / `<description>` blocks | § Recognize tool description, `skills.md:114-119` |
| description length cap | "`description` must be 1-1024 characters." | § Follow length rules, `skills.md:72` (html.txt:197) |
| the description's role | "Keep it specific enough for the agent to choose correctly." | § Follow length rules, `skills.md:73` (html.txt:198) |
| name collisions | "Ensure skill names are unique across all locations" | § Troubleshoot loading, `skills.md:229` (html.txt:403) |
| per-skill exclusion | "`opencode/autoinvoke`: set to `"false"` to keep the skill out of model-facing auto-selection guidance" | § Write frontmatter, `skills.md:45` |
| exclusion effect | "Skills with `metadata["opencode/autoinvoke"]` set to `"false"` are not included in `<available_skills>`." | § Recognize tool description, `skills.md:128` |
| page revision | "Last updated:" → `Oct 20, 2026` (`datetime="2026-10-20T22:40:11.000Z"`) | HTML footer, `f2.html` |

## Sweep (the negative evidence, Q14)

Command (over the fetched markdown, 5365 B):

```
for t in 'overlap' 'ambigu' 'precedence' 'tie[- ]?break' 'conflict' 'multiple skills' 'same name' 'prioriti' '1024' 'truncat'; do printf '%-16s -> ' "$t"; grep -ciE "$t" f1.md; done
```

| pattern | count |
|---|---|
| `overlap` | 0 |
| `ambigu` | 0 |
| `precedence` | 0 |
| `tie[- ]?break` | 0 |
| `conflict` | 0 |
| `multiple skills` | 0 |
| `same name` | 0 |
| `prioriti` | 0 |
| `1024` | 1 |
| `truncat` | 0 |

The same ten `grep -ciE` calls over the raw HTML route (`f2.html`, 73201 B) give the identical ten counts: `0 0 0 0 0 0 0 0 1 0`. `grep -c` exits 1 on a zero count; the loop's last command therefore exits 1 — that is the expected grep exit for "no match", not a failure of the fetch.

**Plainly: the page documents no tie-break between two overlapping skills.** No arbitration rule of any kind appears: no precedence, no ambiguity handling, no tie-break, no conflict resolution, no priority, no truncation of the list, no "multiple skills" case. The page's own only collision statements are (a) skill **names** must be unique across all locations, and (b) a skill can be pulled out of the model's guidance entirely with `opencode/autoinvoke: "false"`. Note (a) is worded "unique across all locations", not "same name" — the literal phrase `same name` has 0 hits, so the 0 count is not the absence of the topic, only the absence of that wording; the topic is covered by the `unique` wording at `skills.md:229` and by `opencode/autoinvoke` at `skills.md:45` and `:128`. This matches the census entry's existing finding for S022/S023/S018 (no documented tie-break anywhere) and extends it to a fourth client.

## Draft SOURCES row (11-column shape, id per L1 assignment)

The registry at `f3046466` ends at S023 and holds no row for `opencode.ai/docs/skills` (`grep -c 'opencode.ai/docs/skills' corpus/SOURCES.md` → 0), so this is a **new row**, not a re-open. L1 assigns the final id at integration; the draft id below is the placeholder the L1 asked for.

```
| S0NN | opencode — Agent skills — https://opencode.ai/docs/skills | docs | A | What opencode's own documentation states about how a skill's description reaches the model, and whether it documents a tie-break between two skills whose descriptions both match (vendor documentation for opencode's current release; not a measurement of omp or of opencode v1.19.3) | § Write frontmatter `skills.md:29-48`; § Follow length rules `skills.md:70-73`; § Recognize tool description `skills.md:108-129`; § Troubleshoot loading `skills.md:223-231`; fetched as https://opencode.ai/docs/skills.md (200, 5365 B, sha256 `f10ced73…`, text/plain) on 2026-10-22T12:31:20Z, byte-identical to the 12:28:29Z fetch; the HTML route (200, 73201 B, sha256 `4d96fa56…`) carries the footer stamp "Last updated: Oct 20, 2026"; sweep `grep -ciE` over the markdown: overlap/ambigu/precedence/tie[- ]?break/conflict/multiple skills/same name/prioriti/truncat → 0 each, 1024 → 1 | opencode shows the model one `<available_skills>` list inside the `skill` tool description, each entry being the skill's name and description; `description` is capped at 1-1024 characters; the page documents no tie-break between two skills whose descriptions both match — its only collision controls are name uniqueness across locations and `opencode/autoinvoke: "false"`, which removes a skill from model-facing guidance | queued | 2026-10-22 | 90d | — |
```

**Tier reasoning (L1 asked for this explicitly).** Tier A, scoped to *what opencode's documentation states*, matching the registry's own precedent for vendor documentation of a client (S021/S022/S023 are tier A with the scope qualifier "vendor documentation, not a measurement of omp or opencode"). The row is pinned by content hash and by the page's own footer date, so the anchor is reproducible. The round-47 and round-48 search logs excluded this URL as "unversioned, documents keys 1.19.3 lacks; tier B at best, no claim rests on it" (`corpus/SOURCES.md` § Search log, the 2026-10-21 and 2026-10-22 entries). Two of those three reasons still hold and are carried in the scope cell: the page is unversioned and it describes a loader newer than the pinned v1.19.3 (measured: `grep -ci autoinvoke` over `packages/opencode/src/skill/index.ts` at tag v1.19.3 → 0, `grep -ci metadata` → 0; the page documents both). The third reason is now false: C1 requires a row opened this round on how a client presents skill descriptions and on whether it documents a tie-break. Because the scope is bound to the documentation's own statements, the version gap cannot leak into a behaviour claim. If the L1 prefers the earlier reading, the flip is one cell: `A` → `B`, and the row text needs no other change.

**Row shape checked by the fleet validator** (`scripts/sources-census.sh`, read-only, run against a scratch mirror of the lane — the lane file was not touched). With the placeholder id replaced by a numeric one (`S024`, the L1's to assign), the appended row validates clean:

```
$ bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file mirror/corpus/SOURCES.md --today 2026-10-22
file	W04	S018 duplicate url agentskills.io/specification across scopes
file	W04	S019 duplicate url platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices across scopes
file	W04	S021 duplicate url learn.chatgpt.com/docs/build-skills across scopes
file	ok	.../mirror/corpus/SOURCES.md
(EXIT=0)
```

The three W04s are pre-existing: the same three appear when the unmodified `corpus/SOURCES.md` is validated (exit 0, `file ok`). The appended row adds no E-code (no E01 shape, no E05/E06/E07 enum, no E08/E09 date, no E11 missing used-by, and no E04 duplicate URL+scope — `https://opencode.ai/docs/skills` appears in no other row). Census mode on the same file: `rows 24`, `tier.A 23`, `tier.C 1`, `status.mined 14`, `status.queued 9`, `status.rejected 1`, `missing 0` (exit 0). The one E-code that does fire is `E02` on the placeholder id `S0NN` — expected, since the validator requires `S[0-9]{3,}`; it clears as soon as the L1 substitutes the assigned number.

**Status and used-by flip to apply at landing.** Drafted `queued` / `—`. When the L1 lands the census entry's appended section and the `SKILL.md` description edit that cite this row, log old→new in the round lesson per contract rule 2: `status` `queued` → `mined`, `used-by` `—` → `corpus/knowledge/sibling-overlap-census-round49.md, SKILL.md`.

## Draft lesson Gate line (row, URL, accessed UTC, quote, location)

Append to `corpus/lessons/round-50.md` § Gate, in the shape round-49 used:

```
| S0NN | https://opencode.ai/docs/skills.md | 2026-10-22T12:31:20Z | "OpenCode lists available skills in the `skill` tool description." (§ Recognize tool description, `skills.md:110`) — seat `.ufo/waves/round-50/build/SrcOpencodeDocs.md` |
```

## Findings for the L1

1. **The C1 source requirement is satisfiable from this page.** It is the fourth independent client whose documentation states no tie-break between two matching descriptions (after S022 Claude Code, S023 Anthropic overview, S018 open spec), and the fourth whose description cap is 1–1024 characters. The census entry's § "What decides between overlapping skills" can cite this row for the same negative finding without changing its wording.
2. **A documented exclusion exists, and it is not a tie-break.** `opencode/autoinvoke: "false"` removes a skill from `<available_skills>` entirely. This is the first concrete, documented way a client in this registry lets a skill author opt out of being matched — relevant to the `trigger.05` craft box, because it gives a second mechanism beside description wording. It is an exclusion, not an ordering; the census's negative finding stands.
3. **Freshness, measured:** the page footer says `Last updated: Oct 20, 2026`, two days before the fetch, and the bytes are identical across two fetches three minutes apart. The page tracks opencode's current release, not the pinned v1.19.3 loader, whose skill module contains no `metadata` and no `opencode/autoinvoke` at all (both `grep -ci` → 0 over the v1.19.3 `packages/opencode/src/skill/index.ts`, sha256 `91dce57f…`). Any claim about opencode v1.19.3's behaviour must still cite S016, not this row.
4. **Adjacent finding, out of my scope to land:** the docs page's troubleshooting item "Ensure skill names are unique across all locations" (`skills.md:229`) reads as a uniqueness requirement, but the pinned v1.19.3 loader does not refuse a duplicate name — it logs `"duplicate skill name"` as a warning and then overwrites the earlier entry (`packages/opencode/src/skill/index.ts:125-139`), so the last one loaded wins. The docs page and the pinned loader disagree in kind (documented rule versus silent last-wins). This is worth a note in the census entry's appended section or a future row; I did not land it, since it is S016's file and not my item.
5. **The pattern `tie[- ]?break` (this sweep) and `tie[- ]break` (the census, `sibling-overlap-census-round49.md:27`) differ.** Measured on the same three probes (`tiebreak` / `tie-break` / `tie break`): `grep -cE 'tie[- ]break'` → 2, `grep -cE 'tie[- ]?break'` → 3. The census's spelling misses the unhyphenated `tiebreak`; mine does not. No conclusion in the census changes (both sweeps returned 0 on their pages), but the census's spelling is narrower than intended and should be widened in the same edit that appends this round's section.

## Out of scope for this seat

- No edit to `corpus/SOURCES.md`, `corpus/lessons/round-50.md`, `SKILL.md` or the census entry: the lane checkout is read-only for this seat, and the L1 assigns ids and lands rows.
- No C1 description edit, no census appended section, no `check_sibling_census.py` change (other seats own those).
- No `git`/`jj` write in the lane, the fleet repo or any sibling lane repo; no sibling lane repo was read for this seat.

## Evidence (commands, outputs, exit codes)

```
$ date -u +%Y-%m-%dT%H:%M:%SZ                                  # before first fetch
2026-10-22T12:28:25Z
$ curl -sS -L -D headers.txt -o skills.html -w 'HTTP_STATUS=%{http_code}\nBYTES=%{size_download}\nURL=%{url_effective}\n' https://opencode.ai/docs/skills
HTTP_STATUS=200
BYTES=73201
URL=https://opencode.ai/docs/skills
(exit 0)
$ curl -sS -L -D headers_md.txt -o skills.md -w 'HTTP_STATUS=%{http_code}\nBYTES=%{size_download}\nURL=%{url_effective}\n' https://opencode.ai/docs/skills.md
HTTP_STATUS=200
BYTES=5365
URL=https://opencode.ai/docs/skills.md
(exit 0)
$ sha256sum skills.html skills.md
4d96fa569dd25469e085b3743ee7e5a53263792fb919b7591bd7b8397a3404f0  skills.html
f10ced73971ce83b85f41395e2e15a683fe5a874e9057fc9d13da5f5a1bf8561  skills.md
$ cat headers_md.txt
HTTP/2 200
date: Thu, 22 Oct 2026 12:28:29 GMT
content-type: text/plain; charset=utf-8
content-length: 5365
cf-ray: a4e88089cd485c5b-MIA
server: cloudflare
cf-placement: remote-ORD
$ # second fetch, 2026-10-22T12:31:20Z/21Z, both routes
md_http=200 md_bytes=5365 md_type=text/plain; charset=utf-8      (exit 0)
html_http=200 html_bytes=73201 html_type=text/html               (exit 0)
$ sha256sum f1.md f2.html
f10ced73971ce83b85f41395e2e15a683fe5a874e9057fc9d13da5f5a1bf8561  f1.md
4d96fa569dd25469e085b3743ee7e5a53263792fb919b7591bd7b8397a3404f0  f2.html
$ grep -ciE '<pattern>' f1.md        # the ten patterns, in order
0 0 0 0 0 0 0 0 1 0
$ grep -ciE '<pattern>' f2.html      # same ten over the HTML route
0 0 0 0 0 0 0 0 1 0
$ grep -n '1024' f1.md
72:`description` must be 1-1024 characters.
$ grep -niE 'unique|distinct|collision|duplicate' f1.md
229:3. Ensure skill names are unique across all locations
$ grep -ci 'last updated' f1.md
0
$ python3 -c "...extract <time> from f2.html..."
'Last updated: <time datetime="2026-10-20T22:40:11.000Z" ...>Oct 20, 2026</time>'
$ curl -sS -L -o skill_index.ts https://raw.githubusercontent.com/anomalyco/opencode/v1.19.3/packages/opencode/src/skill/index.ts   # (exit 0)
$ sha256sum skill_index.ts
91dce57f590e1ad3103e0555b893500e098a95cde2739422b699233889b205e6
$ grep -ci 'autoinvoke' skill_index.ts ; grep -ci 'metadata' skill_index.ts
0
0
$ awk 'NR==24||NR==205||NR==206||NR==207' skill_index.ts
24: const OPENCODE_SKILL_PATTERN = "{skill,skills}/**/SKILL.md"
205:   const configDirs = yield* config.directories()
206:   for (const dir of configDirs) {
207:     yield* scan(state, dir, OPENCODE_SKILL_PATTERN)
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin && grep -c 'opencode.ai/docs/skills' corpus/SOURCES.md
0
$ cd ... && git show f30464660c675d1c1e2851a3bf0366a3aaffe5a8:SKILL.md | awk 'NR==1&&/^---$/{f=1;next} f&&/^---$/{exit} f' | grep -oiwE 'chousa|kagi|kake|kama|kasegi|kengaku|kotodama|kumitate|tameshi' | sort -u | wc -l
5
```

The last command is the C1 counter at the round-50 base (5 of 9), recorded so the L1 can see the before-value this row supports; it is not my claim and I did not change `SKILL.md`.

## Artifacts

- Fetched bytes and derived text: `/fast/scratch/hyaku/kotoba-r50/build/src-opencode-docs/` — `f1.md` (5365 B), `f2.html` (73201 B), `h1.txt`, `h2.txt`, `times.txt`, `skills_html.txt`, `skills.md`/`skills.html` (first fetch, same hashes), `skill_index.ts` (v1.19.3 source read for finding 3/4).
- This report: `.ufo/waves/round-50/build/SrcOpencodeDocs.md` in kotoba-shokunin.
