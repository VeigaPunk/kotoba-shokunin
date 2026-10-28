# Kb80S12AssimDisp — assimilation disposition (round 80, w1)

Seat: leaf scribe, no subagents. Deliverable paragraph set for the round-80 lesson `## Gate`:
`/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80S12AssimDisp.md`.

## Provenance of the reads

The two peer reports this seat was told to consume were **absent** when read:
`.ufo/waves/round-80/w1/` held only `swarm-registry.json`, and
`.ufo/waves/round-80/build/` did not exist. So every verdict here was derived by this seat from
the register, the lane bytes and live fetches — **not** copied from `Kb80R06ShokuknowSlice` or
`Kb80K03Considerthese`. Lane HEAD at read time: `c2f69d4` ("round-80: freeze plan F1 + validated
v2 wave (64 seats) + base receipts"); base `398cbe1…` bytes were not needed because nothing was
patched.

No C1 patch was produced by this seat; `Kb80E10Battery` asked for one and was told so directly.

## 1. Quarantine slice — derived, 13 rows, hand-checked, adoption closed

```
awk -F'|' -v l='kotoba' '$2 ~ ("`" l "`") && $3 ~ /round[0-9]+/ && $4 ~ /S[0-9]+/ \
  {print $4, $5}' "$R" > "$A/quarantine-slice"
→ exit=0  rows=13            receipt: $A/quarantine-slice.receipt
```
(`$R` = `/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md`,
`$A` = `.ufo/waves/round-80/assimilation`.) 13 = 7 `payload-absent` + 6 `unreachable`; every line
carries an S-id.

Every cited source was re-opened live 2026-10-27 with the `read` tool (it reports the method per
page: `native`, `text`, `md-suffix`; all pages returned content — this seat has no HTTP status
codes to cite and says so rather than inventing them). Verdicts, one line each, in the
deliverable's table. Counts:

| class | rows | adopted | refused as quotation | reachable, no quote recorded |
|---|---|---|---|---|
| payload-absent | 7 | 0 | 7 | — |
| unreachable | 6 | 0 | — | 6 |
| **total** | **13** | **0** | **7** | **6** |

`unreachable` rows left unreachable this round: **0**. Nothing appended, nothing edited in the
register or any campaign file, no lane corpus row touched.

Per-row substance (fetch date 2026-10-27 in every line):
S151 span is lane prose and the 37–44 / +37.8 figure is on no fetched page; S167/S176 spans are
lane notes about S002 and about the three-tier table; S168's `section:` is a heading-fold
artifact (the page carries the 56% sentence); S172's wording is absent but the fact is present
("the user-level skill will be skipped", 17 words, Troubleshooting); S180's `スキルのインストール`
is absent against the live heading `Gemini エージェント スキルをインストールする`; S185's
`Skill locations` heading no longer exists (`Choose a location`, `Skill Discovery` do);
S169/S236/S237/S238/S239/S243 all fetch today, and none ever had a quote recorded, so they stay
unverifiable **as quotes** — reachable is not adopted.

**Adoption closed** (plan § Frontier: "adoption stays closed — the r79 disposition stands until a
slice verdict flips"). The one row whose flip condition is evidenced is S172 (fact located,
wording not): it may be admitted in a later round only after the row is rewritten around the
located sentence. Unreachable rows do not flip into fabrication claims; they flip into "checked".

### Id-space drift (the reason nothing repairs by id)

All 13 ids return 0 rows in `corpus/SOURCES.md`:
`grep -cE "^ {0,3}\|[[:space:]]*<id>[[:space:]]*\|"` → 0 for each of the 13. The 157-row registry
carries S001–S124 (minus S092, S116), S129, S198–S231; 74 ids below S232 are absent. Four of the
seven cited documents are already held under current ids (S213/S210, S002, S206, S203); three are
held nowhere (vercel blog, skills.sh ×4, code.claude security page — `grep -c` → 0 each). The
register's kotoba ids are pre-renumber ids: re-anchor by document, never by arithmetic.

## 2. `merge/kotoba/` — nothing appended; collision arithmetic re-derived

```
grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md | grep -oE 'S[0-9]+' | sort > reg-ids    # exit=0, 157
grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' $P/merge/kotoba/SOURCES.append.md | grep -oE 'S[0-9]+' | sort > staged-ids  # exit=0, 188
comm -12 reg-ids staged-ids > collisions                                                              # exit=0, 29
```
receipt: `$A/collision.receipt`. Staged ids S203–S390, contiguous, 188 rows, no duplicates;
collisions S203–S231 (29). Nothing staged, transformed or appended — the r77 S04 reading holds.

**Guard proven once** (scratch under `/fast/scratch/hyaku/kotoba-r80/Kb80S12AssimDisp/`, removed
after; `scratch_removed=0`). Fixture `| S001 |` at column 0 plus `  | S210 |` indented:
0–3-space pattern → ids {S001, S210}, collisions = 1 (S210); column-zero-only pattern → ids
{S001}, collisions = 0. The column-zero-only extractor false-greens an indented collision; the
0–3-space form is the one any append must use.

## 3. `considerthese/2026-10-26.md` proposals 2–5 — dispositions, each measured

- **P2** move `## Gate registry` out of `SKILL.md`: `sed -n '445,513p' SKILL.md | wc -c` → **24,897**
  of **78,647** B (`wc -lc` → 590 lines / 78,647 B) = 31.7 %. Open.
- **P3** land the r74-rejected page then audit the description: premise does not hold — the rejected
  entry's source is already held as **S213** (round 74 refused it for duplicate URL). Audit half
  measured: description YAML-parses to **1,021 / 1,024 characters** (3 chars headroom); first
  sentence **151 chars**. Open, restatable as audit-only.
- **P4** close rounds `provisional` until the falsify wave runs: `grep -c -i provisional
  SCORECARD.md` → **2** (`:126` r51, `:365` r47); round 74, the round named, closes admitted with
  the missing wave only in prose (`SCORECARD.md:467`). Open, operator/closure-owned.
- **P5** per-round evidence budget: `.ufo/` = **175,428,954 B** of a **244,774,284 B** tree
  (71.7 %, `du -sb`); window 2026-10-23→2026-10-27 = **3,715 files / 597,617 insertions / 3,089
  deletions / 132 commits** (`git log --since=2026-10-23 --until=2026-10-27 --numstat`).
  Operator-owned; recorded only.

None implemented this round; none used as evidence for a frozen claim.

## Findings handed to the lesson (all reported, none repaired here)

1. **F-Kb80S12-1 — register extraction class.** S151/S167/S176 spans are lane prose lifted out of
   row cells by the campaign's quote extractor; S168's `section:` is a heading-fold artifact. The
   `payload-absent` label therefore mixes "fabrication" with "extractor noise"; a reader must
   distinguish them, and no lane row should be refused on the label alone.
2. **F-Kb80S12-2 — S206 page drift.** S206's quoted sentence "the project-level skill takes
   precedence and the user-level skill is ignored." (11 words) is **not** on
   `junie.jetbrains.com/docs/agent-skills.html` as fetched 2026-10-27 (page `meta-built-on:
   2026-10-27T08:16:42`); the page now says "…the user-level skill will be skipped." Page drift
   after S206's opening, not fabrication — but S206 belongs on the round-80 re-open list.
3. **F-Kb80S12-3 — alias hazard.** Round-80's new rejection rows start at S232; the register's
   stale ids S236–S239 and S243 sit in that space. Once ≥ 4 new rows land, ids alias across the
   two artifacts. Future quarantine passes must key on (lane, cited URL).

## Limits

- Fetch evidence is "the `read` tool returned page content on 2026-10-27, method as reported per
  page"; no HTTP status codes are asserted.
- Word/char counts and byte sizes are from the commands shown, on lane HEAD `c2f69d4`; nothing was
  measured at base `398cbe1` (no claim of this seat depends on it).
- The peer reports were absent, so this seat's per-row verdicts are independent and may differ
  from whatever `Kb80R06ShokuknowSlice` later writes; the closure should prefer the scout's report
  where the two disagree, and both name their fetch date.
- Tooling: nothing installed or upgraded (no pacman, per the host-wide pause).
- Scratch dir removed; no background processes left; no lane file outside `.ufo/waves/round-80/`
  written.

## Artifacts

- Deliverable: `.ufo/waves/round-80/build/Kb80S12AssimDisp.md`, sha256
  `3c704032fbf4a668f847a4caebc2b9f8e5d4370c133a07c0a8078f9318c7687e` (final bytes, after the two
  in-file corrections to the gap list and the S172 word count).
- Receipts: `.ufo/waves/round-80/assimilation/{quarantine-slice,quarantine-slice.receipt,
  reg-ids,staged-ids,collisions,collision.receipt,guard-fixture.md,guard-fixture-ids,
  guard-fixture-collisions}`.

VERDICT: Quarantine slice = 13 rows hand-checked on 2026-10-27 fetches — 0 adopted, 7 refused as quotations, 6 reachable-but-unquotable, 0 unreachable; adoption closed; merge/kotoba appended nothing with 29/29 staged-id collisions re-derived and the 0–3-space guard proven; considerthese P2–P5 dispositioned with their own measures; three findings (register extraction class, S206 page drift, S232+/S236–S243 alias hazard) handed to the lesson.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80S12AssimDisp.md ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/w1/Kb80S12AssimDisp.md ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/assimilation/
