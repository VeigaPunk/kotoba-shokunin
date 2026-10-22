# ReopenS025 — re-open of SOURCES row S025 (VS Code, Use Agent Skills)

FAILS, narrow. It applies to two items: the census entry's round-50 S025 bullet (it calls the `multiple skills` hit a duplicate-name hit, which is false) and the row's Last-Modified cell (not reproduced today, so the "one day old" freshness basis is unsupported). HOLDS for the `.md` bytes and sha256, the quote at line 302, the teaches, tier and scope cells, the lesson Gate row, the validator result and all ten sweep counts. The HTML byte drift is explained (rotating site banner, finding 3).

Scope: row S025 only, at lane master 956ee1676e4c18480bce8ac3993541462be76e11 (claims at 542f5156). Fetches by this seat: 2026-10-22T13:32:46Z to 13:34:34Z UTC. Scratch: /fast/scratch/hyaku/kotoba-r50/falsify/ReopenS025/ (fetch/, lane/). Other items of the round (C1, C2, D1–D6, S024 and S026–S029, Q26) are other seats' work.
Axes: adjacency HOLDS on this page (no two-skill tie-break on a full read). Freshness: content current; the recorded date metadata does not reproduce.

## Findings, by severity

1. MEDIUM, census bullet is wrong. `corpus/knowledge/sibling-overlap-census-round49.md:205-206` says `precedence` 1, `same name` 1 and `multiple skills` 1 are "all about duplicate names". The only `multiple skills` line is `agent-skills.md:15`: "Combine multiple skills to build complex workflows" (under "Compose capabilities"). Row S025's own teaches cell says "multiple skills 1 (composing skills)", so the census and the row disagree. The bullet also omits the `1024` hit (1, at :148, the length cap) and lists 7 of the 10 terms. Q26 (`corpus/QUALITY.md`): a count cannot say what a matching line is about, so "all about duplicate names" says more than the count measures, and for one hit it is false. Fix: name each hit by line and list all ten terms.

2. MEDIUM (freshness), recorded date does not reproduce. `SOURCES.md:38` records "page Last-Modified Wed, 21 Oct 2026 06:19:42 GMT", and the seat report (`.ufo/waves/round-50/build/SrcVSCodeSkills.md`, F2) concludes the page "is one day old at access". Today the same `.md` route answers `last-modified: Thu, 22 Oct 2026 09:16:14 GMT` (`fetch/md1.hdr`). Its ETag `W/"5957-1a162e58f30"` carries the same time: 0x1a162e58f30 ms = 1792660574000, which is 2026-10-22T09:16:14Z; 0x5957 = 22,871 bytes. The bytes did not change (check 1). The seat did not keep its response headers, so the cause cannot be proved from here. [INFERENCE] The seat may have received a cached copy stamped 21 Oct, or the origin was re-saved at 09:16:14 UTC with identical bytes. Fix: record the 13:32Z header as a dated observation, drop "one day old", and rest content identity on the sha256 and the upstream `DateApproved: 10/21/2026`.

3. LOW, drift explained. `SOURCES.md:38` records the HTML route as "200, 157298 B, sha256 9118c27c…". The seat's stored artifact reproduces that (`/fast/scratch/hyaku/kotoba-r50/build/src-vscode-skills/fetch2/new_html`). A fresh fetch today gives 156,890 B, sha256 914a5712…, identical on three fetches. `diff` of the two renderings, split at `>` with `tr`, gives 20 lines, all in the rotating announcement banner (split-copy lines 410 and 415–426: `2026-09-09-vscode-documentary-agent-host` → `2026-10-21-gh-universe`). The page prose is outside the diff. The claim holds as a dated snapshot.

4. LOW, scope precision. The anchor and scope cells omit two qualifiers the page states: (a) `agent-skills.md:64` ("If skills in `.github/skills/` have duplicate names across workspace roots, the primary root takes precedence.") sits inside the NOTE at :61–66 about the experimental OpenAI Codex integration; (b) the Marketplace heading at :119 reads "(Experimental)". The teaches parenthetical "precedence 1 (duplicate names across workspace roots)" does not carry the Codex limit. Not false, but a reader could take :64 as a general VS Code rule. Fix: say "inside the experimental Codex integration NOTE" and keep "(Experimental)".

5. NIT, wording. Teaches says the description "must say what the skill does and when to use it". The page says "Required: Yes" and describes the field as "A description of what the skill does **and when to use it**" (:148). "must" reads "Required: Yes" as an obligation. Accepted as a paraphrase, not an extra claim.

6. NIT, seat report. `SrcVSCodeSkills.md:103` reserve quote is called 19 words; it has 20 (`Be specific … Maximum 1024 characters.`). It is in neither the row nor the lesson. No effect.

Out of scope, noticed (for the S024 check): `SOURCES.md:96` (an excluded-sources entry from an earlier round) calls the opencode skills docs "tier B at best". Row S024 (`SOURCES.md:37`) is tier A, and the lesson's status log (`corpus/lessons/round-50.md:75–78`) records no tier change. Not checked further.

## Verdict per check

| # | check | verdict | evidence |
|---|---|---|---|
| 1 | `.md` bytes and sha256 match the recorded fetch | HOLDS | 200, 22,871 B, sha256 de5ba34f… on two fetches (13:32:56Z, 13:32:57Z); `cmp` exit 0; seat artifact `new_md` has the same sha |
| 2 | upstream repo file (`repo_raw`) | HOLDS | 200, 24,087 B, sha256 bae0c84d…; `DateApproved: 10/21/2026` at line 3 |
| 3 | HTML route bytes | DRIFT, explained (F3) | 156,890 B today vs 157,298 B recorded; banner-only diff |
| 4 | Last-Modified cell | NOT REPRODUCED (F2) | today `Thu, 22 Oct 2026 09:16:14 GMT` |
| 5 | requested route answers 301 to the final route | HOLDS | `curl` without -L: 301, 72 B, `location: /docs/agent-customization/agent-skills`, exit 0 |
| 6 | requested route's `.md` variant is 404 (seat claim) | HOLDS | 404, 9 B, sha256 0019dfc4… |
| 7 | quote verbatim at cited location, at most 25 words | HOLDS | `agent-skills.md:302`: "Copilot reads the skill's `name` and `description` from the YAML frontmatter." 11 words |
| 8 | tier cell honest | HOLDS | `.ufo/waves/kaika/SOURCES-CONTRACT-v1.md:26–30`: A = primary or authoritative for the scope (official docs included); "community is never A". The row is the vendor's own docs |
| 9 | scope cell honest | HOLDS (F4 precision) | states "vendor documentation, not a measurement of omp or opencode" |
| 10 | teaches says no more than the page | HOLDS (F5 wording) | :302 "matches this to the `webapp-testing` skill based on its description"; :148 cap 1024; no two-skill rule on a full read |
| 11 | census S025 bullet matches the page | FAILS (F1) | size, the zeros for overlap, ambigu, tie-break and conflict, and the quote hold; "all about duplicate names" is false; `1024` omitted |
| 12 | ten-pattern sweep counts reproduce | HOLDS | table below |
| 13 | lesson Gate row S025 | HOLDS | accessed 12:29:33Z, quote, `agent-skills.md:302`, seat path all present (`lessons/round-50.md` line 58 at 956ee167; line 59 in the working copy) |
| 14 | row structure and used-by paths | HOLDS | validator exit 0, `ok`, W04 ×3 only (S018, S019, S021), no E-code for S025; 11 cells; both used-by paths exist |
| 15 | content unchanged between seat fetch and now | HOLDS | `.md` sha256 identical at 12:29:33Z (seat) and 13:32:57Z (this seat) |

Sweep, command `grep -ciE "<term>" fetch/md1.md` (22,871 B, sha256 de5ba34f…):
overlap 0 (exit 1) · ambigu 0 (exit 1) · precedence 1 (exit 0, :64) · tie[- ]?break 0 (exit 1) · conflict 0 (exit 1) · multiple skills 1 (exit 0, :15) · same name 1 (exit 0, :129) · prioriti 0 (exit 1) · 1024 1 (exit 0, :148) · truncat 0 (exit 1). Also `ambig` 0 (exit 1). All ten reproduce.

## Evidence (commands, exit codes)
- `curl -sS -D fetch/nofollow.hdr -o fetch/nofollow.body -w '%{http_code} %{size_download}' https://code.visualstudio.com/docs/copilot/customization/agent-skills` → `301 72`, exit 0, at 13:32:46Z.
- `curl -sS -D fetch/md1.hdr -o fetch/md1.md …/docs/agent-customization/agent-skills.md` → `200 22871`, exit 0, at 13:32:56Z; repeat → `200 22871`, exit 0, at 13:32:57Z; `cmp fetch/md1.md fetch/md2.md` → exit 0; `sha256sum` → de5ba34f0c2306af7d1b792581d01f53b4ddd6a912699a19f3a2c958efda3ab5 on both; `wc -c -l` → 22871 bytes, 395 lines.
- HTML: `curl -sS -L …/copilot/customization/agent-skills` → `200 156890`, exit 0, at 13:33:06Z; two more at 13:34:34Z → `200 156890` each, exit 0; sha256 914a5712… three times; `cmp` exit 0; `diff` of the tag-split copies → 20 lines, all at 410 and 415–426.
- Old `.md` route: `404 9`, exit 0, at 13:33:07Z. Upstream raw: `200 24087`, exit 0, at 13:33:08Z, sha256 bae0c84d….
- Seat artifacts (read only) in `fetch2/`: new_html 157298 9118c27c…; new_md 22871 de5ba34f…; old_md 9 0019dfc4…; repo_raw 24087 bae0c84d….
- Judged bytes: `git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin <scratch>/lane` → exit 0; `git -C <clone> checkout -q 956ee1676e…` → exit 0; `rev-parse master` → 956ee1676e…. `cmp` of `corpus/SOURCES.md` and the census file against the lane working copy → identical. `corpus/lessons/round-50.md` differs by one line (line 18, the M32 row, present only in the working copy). The S025 gate line is identical in both. `grep -c '^| S0' corpus/SOURCES.md` (clone) → 29.
- ETag decode: `printf '%d' 0x1a162e58f30` → 1792660574000; `date -u -d @1792660574` → 2026-10-22T09:16:14Z.
- Validator: `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --today 2026-10-22 --file corpus/SOURCES.md` run in the clone → exit 0, `ok`, W04 ×3 (S018, S019, S021).
- Row cells: `python3 -B` split of row S025 → 11 cells; tier A, kind docs, status mined, opened 2026-10-22, recheck 90d.
- Contract: `find /home/vgpnk/Projects/shokunin -maxdepth 4 -name 'SOURCES-CONTRACT*'` → exit 0, `.ufo/waves/kaika/SOURCES-CONTRACT-v1.md`; tier text read at lines 26–30.
- Full page read (`fetch/md1.md` lines 1–395 via the read tool) for any rule on two matching skills: none found.

## Verification gaps and residual risk
- The seat's own response headers were not saved; F2's cause stays [INFERENCE].
- Only this page was checked. The row's negative claim covers this page only, as the row's scope says.
- The HTML banner rotates, so the HTML sha256 will move again. The row's recheck is 90d.
- The lane working copy is one lesson line ahead of 956ee167 (the M32 row). Not judged here.

## Tooling
No install or upgrade. Used already-present curl 8.23.0, git 2.56.0, python3 3.14.8, sha256sum, cmp, diff and find. No pacman, uv tool, cargo or npm transaction was run. Writes: the scratch directory and this report only.
