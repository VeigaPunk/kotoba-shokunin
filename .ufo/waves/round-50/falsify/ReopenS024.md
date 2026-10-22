# ReopenS024 — round-50 falsify: SOURCES row S024 re-opened

**HOLDS-BOUNDED** — applies to the S024 row (`corpus/SOURCES.md:37`), its Gate line
(`corpus/lessons/round-50.md:58`), and the census bullet
(`corpus/knowledge/sibling-overlap-census-round49.md:202-204`), judged at 956ee1676e4c18480bce8ac3993541462be76e11.
Bytes, sha256, quote, anchors, tier/scope and all ten sweep counts reproduce on both routes,
~62 minutes after the recorded fetch. Two minor wording defects found; neither flips a
claim any round-50 assertion rests on.

No tool was installed or upgraded (curl, sha256sum, grep, git already present; no pacman
transaction). No headless browser; both routes opened by plain `curl -sS -L`, no bot gate.

## Per-check verdicts

1. **Bytes and sha256 — HOLDS, no drift.** Refetch of https://opencode.ai/docs/skills.md at
   2026-10-22T13:33:59Z: HTTP 200, 5365 B, sha256 `f10ced73971ce83b85f41395e2e15a683fe5a874e9057fc9d13da5f5a1bf8561`,
   `text/plain; charset=utf-8` — identical to the row's recorded 5365 B / `f10ced73…` (12:28:29Z and
   12:31:20Z). HTML route at 13:34:01Z: HTTP 200, 73201 B, sha256 `4d96fa569dd25469e085b3743ee7e5a53263792fb919b7591bd7b8397a3404f0`
   — identical to the recorded `4d96fa56…` / 73201 B. The pinned row at the judged commit carries the
   same hash prefix (`git show 956ee16:corpus/SOURCES.md | grep -c f10ced73` → 1).
2. **Quote verbatim, ≤25 words — HOLDS.** Gate line quote "OpenCode lists available skills in the
   `skill` tool description." is character-for-character the text at `skills.md:110` in the fresh
   bytes. 9 words ≤ 25. Cited section § Recognize tool description begins at line 108, as anchored.
3. **Tier and scope — HOLDS.** Tier A matches registry precedent for opened vendor documentation
   (S021/S022/S023/S025-S029 same tier and qualifier). The scope cell honestly carries both
   still-valid reasons from the earlier search-log exclusions (round 47: "tier B at best"; round 48:
   "unversioned, ahead of the 1.19.3 binary"): it pins to "opencode's current release" (page is
   unversioned apart from the HTML footer date) and says "not a measurement of omp or of
   opencode v1.19.3" — keeping v1.19.3 behaviour under S016. Anchor lines verified in fresh bytes:
   § Write frontmatter 29-48 (autoinvoke bullet at 45), § Follow length rules 70-73 (cap at 72),
   § Recognize tool description 108-129 (exclusion at 128), § Troubleshoot loading 223-231
   (uniqueness at 229). HTML footer stamp confirmed: "Last updated: <time datetime=
   \"2026-10-20T22:40:11.000Z\"" with visible text "Oct 20, 2026" (1 hit).
4. **Teaches cell says no more than the page — HOLDS-BOUNDED.** Verified clauses: one
   `<available_skills>` list inside the `skill` tool description (110-119); each entry name +
   description (111); `description` capped at 1-1024 characters (72); no tie-break documented
   between two skills whose descriptions both match (full-page read + all-zero sweep); name
   uniqueness across locations (229); `opencode/autoinvoke: "false"` removes a skill from
   model-facing guidance (45, 128). Defect: the clause "its **only** collision controls are name
   uniqueness … and `opencode/autoinvoke`" is an exhaustive claim the page contradicts — the page's
   own troubleshooting list (223-231) names a third visibility control at item 4 ("skills with
   `deny` are hidden from agents", § Configure permissions) and a fourth (disabling the skill tool
   omits `<available_skills>` entirely). Neither added control is a tie-break, so the load-bearing
   negative finding stands; the word "only" is the defect.
5. **Census bullet matches the page — HOLDS-BOUNDED.** Reproduced exactly: `skills.md`, 5,365 B;
   every arbitration term 0; `1024` 1 at `skills.md:72`; line 110 is the model-facing listing
   sentence; seat name `SrcOpencodeDocs.md` correct. Defect: the bullet's "The model sees **all**
   skills in the `skill` tool description" overstates its own anchor — line 110 says "available
   skills", and line 128 says skills with `opencode/autoinvoke: "false"` are not included in
   `<available_skills>` (permissions `deny` hides more). The no-tie-break finding does not rest on
   the word "all", so severity is minor.
6. **Ten-pattern sweep counts — HOLDS.** Fresh run of the recorded loop over the fresh 5365-B
   markdown gives, in order overlap, ambigu, precedence, `tie[- ]?break`, conflict, multiple
   skills, same name, prioriti, 1024, truncat: `0 0 0 0 0 0 0 0 1 0` — identical to the row, the
   census bullet and the seat report. Same ten counts over the fresh HTML: `0 0 0 0 0 0 0 0 1 0`.

## Findings by severity

- **MINOR (census, `sibling-overlap-census-round49.md:203`):** "The model sees all skills" is
  contradicted by the page's own exclusion at `skills.md:128` (and permissions `deny` at
  `skills.md:160-190`, troubleshooting item 4). Suggested fix if the round owns an edit window:
  "The model sees the available skills — every skill not excluded by `opencode/autoinvoke` or
  permission `deny` — in the `skill` tool description (`skills.md:110,128`)."
- **MINOR (SOURCES row 37 teaches cell):** the exhaustive "only collision controls" enumeration
  omits the two further documented visibility controls (permission `deny`; disabling the skill
  tool). Drop "only" or add "and permission `deny`". No round-50 claim cites the enumeration's
  completeness; C1's negative stands either way.
- **INFO:** `grep -c` exits 1 on a zero count, so the recorded sweep loop exits 1; reproduced here
  (`loop_exit=1`). This is the expected "no match" exit, matching the seat report's note — not a
  tool failure.

## Residual risk and verification gaps

- The page is unversioned apart from the HTML footer stamp ("Last updated: Oct 20, 2026",
  datetime 2026-10-20T22:40:11.000Z); identity rests on content hashes, which is what the row
  records. Drift after 13:34Z today is possible and untested beyond this one refetch.
- I re-ran the sweep on both routes once; I did not vary user-agent or accept-language, so a
  variant served to other clients is unverified (both recorded and fresh fetches used plain curl
  defaults and matched).
- Tier A rests on registry precedent for vendor docs; SOURCES.md states no explicit tier
  rubric, so "honest tier" was judged against S011 (tier C community) and the A-tier vendor rows.

## Evidence (commands, exit codes)

Scratch: `/fast/scratch/hyaku/kotoba-r50/falsify/ReopenS024/`. Lane untouched except this report.

```
$ date -u +%Y-%m-%dT%H:%M:%SZ            # 2026-10-22T13:33:59Z
$ curl -sS -L -D h_md.txt -o skills.md -w '...' https://opencode.ai/docs/skills.md
STATUS=200 BYTES=5365 URL=https://opencode.ai/docs/skills.md TYPE=text/plain; charset=utf-8   (exit 0)
$ sha256sum skills.md ; wc -c < skills.md
f10ced73971ce83b85f41395e2e15a683fe5a874e9057fc9d13da5f5a1bf8561  skills.md
5365
$ curl -sS -L -D h_html.txt -o skills.html -w '...' https://opencode.ai/docs/skills
STATUS=200 BYTES=73201 URL=https://opencode.ai/docs/skills TYPE=text/html                    (exit 0)
$ sha256sum skills.html ; wc -c < skills.html
4d96fa569dd25469e085b3743ee7e5a53263792fb919b7591bd7b8397a3404f0  skills.html
73201
$ for t in 'overlap' 'ambigu' 'precedence' 'tie[- ]?break' 'conflict' 'multiple skills' \
>   'same name' 'prioriti' '1024' 'truncat'; do printf '%-16s -> ' "$t"; grep -ciE "$t" skills.md; done
0 0 0 0 0 0 0 0 1 0        (loop_exit=1: last grep found no match)
$ awk 'NR==110' skills.md
OpenCode lists available skills in the `skill` tool description.
$ awk 'NR==72||NR==111||NR==128||NR==229' skills.md
72:  `description` must be 1-1024 characters.
111: Each entry includes the skill name and description:
128: Skills with `metadata["opencode/autoinvoke"]` set to `"false"` are not included in `<available_skills>`.
229: 3. Ensure skill names are unique across all locations
$ grep -n '^## ' skills.md | awk -F: '$1==29||$1==70||$1==108||$1==223'
29:## Write frontmatter / 70:## Follow length rules / 108:## Recognize tool description / 223:## Troubleshoot loading
$ grep -c 'Oct 20, 2026' skills.html ; grep -o 'datetime="[^"]*"' skills.html | head -1
1 ; 2026-10-20T22:40:11.000Z
$ # same ten patterns over skills.html -> 0 0 0 0 0 0 0 0 1 0
$ git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show 956ee1676e4c18480bce8ac3993541462be76e11:corpus/SOURCES.md | grep -c 'f10ced73'
1
```

Files read for judgment: `corpus/SOURCES.md:37` (row S024), `corpus/lessons/round-50.md:58`
(Gate line) and :28-36 (Gate header), `corpus/knowledge/sibling-overlap-census-round49.md:190-204`
(round-50 section, S024 bullet at :202-204), seat report
`.ufo/waves/round-50/build/SrcOpencodeDocs.md`, `corpus/SOURCES.md:1-26,62-110` (tier precedent,
search-log exclusions), fresh `skills.md` lines 1-231 (full page).

Report: .ufo/waves/round-50/falsify/ReopenS024.md
