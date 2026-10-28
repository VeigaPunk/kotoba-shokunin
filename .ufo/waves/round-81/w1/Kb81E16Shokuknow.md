# Seat report — Kb81E16Shokuknow

Round 81 w1 (v2), leaf scout seat. Assignment: assimilation slice re-derivation (read-only) —
re-run the quarantine-register slice exactly as round-prompt §6.10 prescribes, compare with the r80
hand-checked verdicts, hand-check any NEW row, and re-run the staged-id collision check with a guard
proof on a scratch fixture. `merge/kotoba/` and `/home/vgpnk/Projects/shokuknow` stay read-only.

Input: `/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md`,
83,621 B, 375 lines, mtime 2026-10-24 08:37, sha256
`5afe1810a6c3d62f37987b575a954f5b1197daa23005d4bb2f1d982f64bad833` (re-derived this round; the
register is unchanged since the r80 hand-check, so r80's verdicts are checked against identical
bytes, not re-interpreted).

## 1. Slice re-derivation — 13 rows, every line carries an S-id

Command (round-prompt §6.10, verbatim; GNU Awk 5.4.1):

```
R=/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md
awk -F'|' -v l='kotoba' '$2 ~ ("`" l "`") && $3 ~ /round[0-9]+/ && $4 ~ /S[0-9]+/ {print $4, $5}' "$R"
```

exit `0`, **13 lines**, sha256
`0141c203d993e812c85c6d9ee7a8cdf6b44b5d2aca2113bab7ef607de38d7916`
(`.ufo/waves/round-81/build/Kb81E16Shokuknow-slice.txt`):

| # | id | round | class / why-cell |
|---|---|---|---|
| 1 | S151 | round3 | `payload-absent` |
| 2 | S167 | round4 | `payload-absent` |
| 3 | S168 | round5 | `payload-absent` |
| 4 | S172 | round5 | `payload-absent` |
| 5 | S176 | round5 | `payload-absent` |
| 6 | S180 | round6 | `payload-absent` |
| 7 | S185 | round6 | `payload-absent` |
| 8 | S236 | round10 | the cited source could not be fetched, so no quote was checked |
| 9 | S237 | round10 | same |
| 10 | S238 | round10 | same |
| 11 | S239 | round10 | same |
| 12 | S243 | round10 | same |
| 13 | S169 | round5 | same |

**No blank-printing or summary row appeared** — the `## By lane` count row
(`| \`kotoba\` | 7 |`, register line 246) is a 3-cell row whose `$4` is empty, so the pattern cannot
emit it; measured: 13 emitted lines, 13 carrying `S[0-9]+`. The published file is the exact awk
stdout, unedited (the never-checked ids keep the register's trailing-backtick rendering, `S236\``;
stripped only for id arithmetic).

Precision of the lane-cell anchor, measured: the register holds exactly 14 lines carrying
`` `kotoba` `` (13 rows + the by-lane count row), and 15 lines matching the substring `kotoba` — the
15th is line 127, a **`kotodama`** row whose cited URL is `https://kotobank.jp/...`. A `grep kotoba`
sweep would import a foreign row; the `` `kotoba` `` cell anchor does not (`kotodama` cannot match
`\`kotoba\``).

## 2. Comparison with the r80 hand-checked verdicts — identical, no NEW row

- r80's canonical slice bytes `.ufo/waves/round-80/assimilation/quarantine-slice` (620 B) vs today's
  awk stdout: `cmp` exit `0` → **byte-identical**, same 13 ids in the same order as
  `.ufo/waves/round-80/build/Kb80R06ShokuknowSlice.md` §1 (id sets `comm`-diffed: only-in-r81 = ∅,
  only-in-r80 = ∅).
- **No NEW row → no new hand-check is owed, and nothing is adopted or refused this round** (Q62: no
  new observed fact to record). r80's per-row verdicts therefore stand as filed:
  7 payload-absent (3 lint artifacts S151/S167/S176, 2 fragment/elision S168/S172, 2 nonexistent
  section anchors S180/S185) and 6 never-checked rows all reachable with anchors present.

### 2b. Fresh-fetch calibration over the same 13 rows (cheap, done anyway)

The 13 rows cite 12 distinct URLs (S176 reuses S167's); all 12 were re-fetched today with curl 8.23.0
(`-sSL -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36" --max-time 60`), plus one extra
`?hl=ja` live-gemini variant this seat fetched for comparison (cited by no row) — 13 fetches, all HTTP
200. Receipt:
`.ufo/waves/round-81/build/Kb81E16Shokuknow-refetch.txt` (per-URL status, bytes, sha256, r80
reference value, anchor counts).

- 9 of 12 bodies are **byte-identical** to r80's same-day hashes (S151 7cc54fbb…, S167/S176
  07511caa…, S172 a44a510e…, S185 fe801910…, and the five skills.sh / claude / code.claude bodies
  7f179851…, 0ea32a11…, 3d516a19…, 011bb184…, 453ebb4e…).
- 3 bodies **drifted**: S168 vercel blog (900,228 B both times, sha 72e66dc9… → dfaf4401…),
  S180 archive render (113,443 → 113,449 B, 47f486f2… → 6a225155…), S169 live gemini page
  (115,366 → 116,026 B, 5a18b4a8… → 8ce74f3a…).
- Every material predicate was re-tested **on today's bytes** and is unchanged: the four S151
  fragments and S167's `lane holds this page as S002` still 0 matches; S168's `section:` 0 while
  `In 56% of eval cases, the skill was never invoked.` = 1; S172's truncated `…the user-le` 0 while
  the full junie precedence sentence = 1; S176's `three-tier progressive` 0 (`three-tier` = 1);
  S180's `スキルのインストール` 0 while `インストールを確認する` = 1; S185's `Skill locations` 0 while
  `Creating Your First Skill` = 2; S169's `Skills come pre-installed` = 1.
- Unreachable-class premise still false: all six never-checked sources fetch 200 (five via one
  redirect to `www.skills.sh`).

## 3. Staged-id collision check — 46 collisions, and a NEW surface at 5 ids

Recipe (r74/r80 form, 0–3 leading spaces on both sides):

```
git -C <lane> show b284223105f4d106f7e8f56ed4fd296c643cda0e:corpus/SOURCES.md > SOURCES.base.md
grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' SOURCES.base.md | grep -oE 'S[0-9]+' | sort -u > reg-ids
grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' /home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md \
  | grep -oE 'S[0-9]+' | sort -u > staged-ids
comm -12 reg-ids staged-ids > collisions          # exit 0
```

Measured at the r81 base (`corpus/SOURCES.md` worktree == committed bytes at `b2842231`, `diff -q`
exit 0): reg-ids **174**, staged-ids **188** (contiguous S203–S390, `diff` vs `seq` exit 0, no
duplicates on either side), `comm -12` → **46** collisions, `S203`–`S248`
(`.ufo/waves/round-81/build/Kb81E16Shokuknow-collisions.txt`, sha256 `685eade1…`). Lane registry
gaps for reference: S092, S116, S125–S197 absent.

Growth across rounds, each measured in its own wave: r77 **23** (S203–S225) → r80 **29** (S203–S231)
→ r81 **46** (S203–S248). The arithmetical driver is the lane's own row additions (r80 landed
S232–S248 in `9a16e9d`); the count is an id-space measure, not a document-duplication measure.

### 3b. NEW surface: five slice ids now collide with LANDED lane rows

`comm -12` of the 13 slice ids with reg-ids (and separately with staged-ids) → **5 each**:
S236, S237, S238, S239, S243 (`Kb81E16Shokuknow-register-id-collisions.txt`). These five landed in
lane `corpus/SOURCES.md` at commit `9a16e9d` ("round-80: land sourced allowed-tools form entry and
safe partial repairs") — and they mean **different documents**:

| id | register row (never-checked) | landed lane row (`9a16e9d`) |
|---|---|---|
| S236 | skills.sh/docs | GitHub Docs — Agent skills (`docs.github.com/.../about-agent-skills`) |
| S237 | skills.sh/audits | Cursor Docs — Agent Skills (`cursor.com/docs/context/skills`) |
| S238 | code.claude.com/docs/en/security.md | Amp Docs — Skills (`ampcode.com/docs/customize/skills`) |
| S239 | skills.sh/agent | Roo Code Documentation — Skills (`docs.roocode.com/features/skills`) |
| S243 | skills.sh/docs/api | Hermes Agent Docs — Skills |

Consequence, observed not inferred: **id-based adoption of any of those five is unsafe** — the id
now binds a different document. It also strengthens the standing r80 lesson that the register's
kotoba ids are pre-renumber ids to be re-anchored by document, never by arithmetic (the other eight
ids S151/S167/S168/S169/S172/S176/S180/S185 still fall in the lane's unused S125–S197 range).

Arithmetic (marked as arithmetic, **not** measured): the round-81 plan adds lane rows S249 and S250,
both inside the staged range S203–S390, so the collision count at the landed tip should read **48**
(S203–S250). A re-run at the landed tip is the parent's to make.

Document→id mapping for the 13 rows' cited documents (measured by URL match in both files), which is
the only safe key for a later adoption decision:

| cited document | lane ids | staged ids |
|---|---|---|
| agentskills optimizing-descriptions | S210, S213 | S231 |
| agentskills adding-skills-support | S002 | S247, S256 |
| vercel blog agents-md-outperforms-skills | — | S248 |
| junie agent-skills | S206, S241 | S252 |
| ai.google gemini coding-agents | — | S249 (live), S260 (archived ja) |
| roocode features/skills | S203, S239 | S265 |
| skills.sh/docs (+ /audits, /agent, /docs/api) | — | S316, S317, S319, S323/S367 |
| code.claude.com/docs/en/security.md | — | S318 |

Note for the L1 registry: staged S249 and the planned lane S249 are **different documents** (staged
S249 = the gemini coding-agents live row; planned lane S249 = the Agent SDK skills page). That is the
same numeric-collision class, one row further.

### 3c. Guard proof on a scratch fixture (indented colliding row)

Fixture under `/fast/scratch/hyaku/kotoba-r81/Kb81E16Shokuknow/guardproof` (removed after; no lane
file touched), transcript published as `Kb81E16Shokuknow-guardproof.txt`:

- lane fixture `| S001 |` (column 0) + `   | S210 |` (3 spaces) + `  | S211 |` (2 spaces) + `| S212 |`;
  staged fixture `| S210 |`, `| S211 |`, `| S300 |`.
- **0–3-space extractor (guard form)**: lane ids {S001,S210,S211,S212}, staged {S210,S211,S300},
  `comm -12` → **2** (S210, S211). The guard catches indented collisions.
- **column-zero-only extractor** (`^\|`): lane ids {S001,S212} → **0** collisions: a **false green**
  that would have reported a clean append while two id collisions land.
- Residual bound, named: 4-space- and tab-indented `| S…` rows are matched by *neither* pattern under
  the 0–3 form (both fixtures → empty). Live blind spot measured today: **0** rows with 4+ leading
  spaces before `| S` in lane `corpus/SOURCES.md`, **0** non-column-0 id rows in
  `SOURCES.append.md`; the any-indent variant (`^[[:space:]]*\|[[:space:]]*S…`) yields the identical
  174 / 188 ids and the identical **46** collisions, so the 0–3 bound loses nothing on today's bytes.
- No committed guard exists for this check: `grep -rln "SOURCES.append\|staged.id\|collision"
  verifiers/ scripts/` → 2 files, both unrelated matches (`check_infoless_fences.py:679` dirname
  collision; `check_spec_craft.py` staged-row fixtures). The 0–3-space extractor lives only in seat
  reports (r70, r72, r73, r74, r77, r80) — restated by hand each round.

## 4. Register-format observations (named, none of them a slice defect)

1. `## By lane` says `kotoba | 7`; the slice is **13** rows. The summary counts payload-absent rows
   only — the never-checked table (6 rows) carries no per-lane count. A reader who trusts the summary
   undercounts kotoba by 6.
2. The never-checked table is 5-cell (`lane | round | id | why it was not checked | cited source`),
   unlike the 7-cell payload-absent table, so the prescribed `$5` prints the **class prose**, not a
   quote, for rows 8–13. Shape note, not a defect: the class cell is prose by construction, and r80
   correctly refused to treat it as a quotable span.
3. Ids in that table render as `S236\`` (trailing backtick), accepted by the pattern and stripped for
   id arithmetic.
4. Multi-line quote cells (S151, S172, S176) span physical lines; the awk keys row-start lines only,
   so they neither add nor drop rows — verified: 13 rows, 13 ids.

## 5. Assimilation disposition

**Adoption stays closed this round** — same disposition as r79/r80, now with three measured supports:
(a) the slice is byte-identical to r80's, so no new row exists to adopt; (b) five of the thirteen
register ids now bind different documents in the landed lane registry (§3b), so id-keyed adoption
would corrupt rows; (c) eight of the cited documents already have lane homes under other ids, and the
four without lane homes (vercel blog, gemini coding-agents, skills.sh family, claude security) are
staged, not admitted. Nothing was appended, transformed or copied into `merge/kotoba/`; the register
and the staged package were read only.

## 6. Commands and exits (evidence honesty)

| command | exit | result |
|---|---|---|
| `awk -F'|' -v l='kotoba' … absent-defect-register.md` | 0 | 13 lines, sha256 `0141c203…` |
| `cmp <awk stdout> .ufo/waves/round-80/assimilation/quarantine-slice` | 0 | byte-identical |
| `git -C <lane> show b2842231:corpus/SOURCES.md > SOURCES.base.md` | 0 | 174 id rows |
| `diff -q SOURCES.base.md <lane>/corpus/SOURCES.md` | 0 | worktree == committed |
| 0–3-space extractor on both files | 0 | ids 174 / 188, no duplicates |
| `comm -12 reg-ids staged-ids` | 0 | 46 |
| `comm -12 slice-ids reg-ids` / `… staged-ids` | 0 | 5 / 5 |
| `seq -f 'S%03g' 203 390` vs staged-ids `diff -q` | 0 | contiguous S203–S390 |
| 13 curl fetches (12 URLs) | 0 each | all HTTP 200; see refetch receipt |
| anchor greps returning 0 matches | 1 | recorded as the absent-string evidence, not as errors |
| `git -C <lane> log -S 'docs.github.com/en/copilot/…' -- corpus/SOURCES.md` | 0 | `9a16e9d` |

No gate counter was run by this seat (this slice scores no claim). Read-only git only in the lane; no
mutation anywhere outside `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/` and
`/fast/scratch/hyaku/kotoba-r81/Kb81E16Shokuknow/`.

## 7. Coordination, tooling, scratch

- Peer `Kb81S12AssimDisp` (consumes these artifacts) derived the same three numbers independently
  (register sha, 13-row slice, 174/188/46) before my files landed; I sent it the two extras it did
  not carry (the 5-id register↔lane collision from `9a16e9d`, and the roocode/S239 re-anchor).
- Tooling: **no installs or upgrades** this seat. Used curl 8.23.0 (libcurl/OpenSSL 3.6.5),
  Python 3.14.8, git 2.56.0, GNU Awk 5.4.1. pacman untouched.
- Fetched pages were treated as data only; nothing in them was executed or followed, and no
  credential/token material appears in any artifact.
- Scratch `/fast/scratch/hyaku/kotoba-r81/Kb81E16Shokuknow/` removed after the receipts were copied
  into the build dir (`scratch_removed=0`).

## 8. Risks and blockers

- The register is an **external, mutable input** owned by `shokuknow` (mtime 2026-10-24). If it is
  republished mid-wave, the slice and the 13-row verdict set must be re-derived; my pin is sha256
  `5afe1810…`.
- The 46-collision figure is a base-tip measurement and will read 48 (arithmetic) once the planned
  S249/S250 rows land; a stale 46 quoted at the landed tip would be wrong.
- Three fetched bodies drift between same-day fetches (S168, S180, S169). Any future claim that pins
  a **body hash** of those URLs needs a re-fetch step; pinning the **located quote** does not.
- No blocker: every assigned item was executed; the one thing not owed (hand-checking a new row) is
  absent because no new row exists, proven by byte identity.

VERDICT: kotoba slice re-derived 13/13 S-ids (sha256 0141c203…, byte-identical to r80's canonical slice), no NEW row → r80 verdicts carry and adoption stays closed; staged-id collisions 46 (S203–S248, up from 29) plus a NEW 5-id register↔lane collision (S236–S239, S243, all landed in 9a16e9d) proving id-keyed adoption unsafe; the 0–3-space guard is proven necessary on an indented fixture (2 vs 0 collisions) with no live blind spot (174/188/46 identical under any-indent).
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81E16Shokuknow.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E16Shokuknow-slice.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E16Shokuknow-collisions.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E16Shokuknow-register-id-collisions.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E16Shokuknow-guardproof.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E16Shokuknow-refetch.txt
