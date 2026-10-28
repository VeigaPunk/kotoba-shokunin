# Kb81S12AssimDisp — assimilation + considerthese disposition (round 81, w1)

Leaf scribe seat, no subagents, no background jobs. Assignment: consume
`build/Kb81E16Shokuknow-slice.txt` + `build/Kb81E16Shokuknow-collisions.txt` and
`considerthese/2026-10-26.md`, and write the lesson-`## Gate` paragraph set covering the
quarantine slice verdict, the `merge/kotoba/` collision arithmetic, and proposals 2–5 (1 already
dispositioned in round 79).

## Behavior

1. Read `plans/round-81.md` first (line 49 is the authoritative assimilation bullet: adoption
   stays closed, "a scout re-derives the slice", "no newer file exists → no proposal is
   implemented this round and the lesson says so").
2. Read the two named build inputs → **absent** (`.ufo/waves/round-81/build/` was empty at 23:18
   and again at 02:28 UTC). Derived everything from the register, the lane bytes and live fetches;
   said so in the deliverable. `Kb81E16Shokuknow` published both files after the deliverable was
   written, and they reconcile byte-for-byte: `diff Kb81E16Shokuknow-slice.txt
   Kb81S12AssimDisp-quarantine-slice` → exit 0 (both sha256 `0141c203…`), `diff
   Kb81E16Shokuknow-collisions.txt Kb81S12AssimDisp-collisions` → exit 0 (both sha256
   `685eade1…`). The scout's S185→S239 document observation is incorporated.
3. Read `considerthese/2026-10-26.md` (newest; `ls considerthese/ | sort | tail -1` →
   `2026-10-26.md`), then measured proposals 1–5 on today's bytes rather than restating round 80.
4. Wrote the paste-ready Gate block plus provenance/findings, receipts, and this report. Removed
   scratch.

## Commands and outcomes (all at lane head `b284223105f4d106f7e8f56ed4fd296c643cda0e`)

Slice:
- `sha256sum <register>` → `5afe1810a6c3d62f37987b575a954f5b1197daa23005d4bb2f1d982f64bad833`;
  `stat` → 83,621 B, mtime 2026-10-24 08:37:00.746072780 -0300.
- `awk -F'|' -v l='kotoba' '$2 ~ ("`" l "`") && $3 ~ /round[0-9]+/ && $4 ~ /S[0-9]+/ {print $4, $5}' <register>`
  → exit 0, **13 rows** (S151 S167 S168 S169 S172 S176 S180 S185 S236 S237 S238 S239 S243).
- `diff .ufo/waves/round-80/assimilation/quarantine-slice <r81 slice>` → **exit 0**; both
  sha256 `0141c203d993e812c85c6d9ee7a8cdf6b44b5d2aca2113bab7ef607de38d7916` → no new row.
- Payload-absent rows unchanged: `git diff c2f69d4 b284223 -- corpus/SOURCES.md | grep -cE '^[+-]\| *S(151|167|168|172|176|180|185) '`
  → `0` (exit 1 from the zero-match grep, recorded as evidence, not error).
- Re-fetch of the six never-checked sources, `curl 8.23.0 -sSL --max-time 40` → **6 of 6 HTTP 200**
  (43,811 / 483,592 / 15,462 / 69,140 / 138,131 / 116,030 B; four `skills.sh` URLs now answer on
  `www.skills.sh`). Per-body sha256 in the receipt.

Collisions:
- `grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md | grep -oE 'S[0-9]+' | sort` → 174.
- same over `/home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md` → 188 (188 unique,
  S203–S390 contiguous).
- `comm -12 reg-ids staged-ids` → **46** (S203–S248), exit 0; `comm -13` against the r80 receipt →
  exactly **17 new** (S232–S248), `comm -23` → **0 removed**. Round 80's receipt: 29 (S203–S231).
- `S249` in the lane: `grep -cE '^\| *S249 ' corpus/SOURCES.md` → `0`; `S248` → `1`.
- Guard fixture `| S001 |` + two-space `  | S210 |`: strict `^\|` → {S001}; `^ {0,3}\|` →
  {S001, S210}. Real bytes: strict 174/188 vs 0–3-space 174/188 (0 indented rows either file).

Alias hand-check: register lines 327–331 (S236 `skills.sh/docs`, S237 `skills.sh/audits`,
S238 `code.claude.com/docs/en/security.md`, S239 `skills.sh/agent`, S243 `skills.sh/docs/api`) vs
lane rows 177–180/184 (GitHub Copilot, Cursor, Amp, Roo Code, Hermes);
`grep -nE '^\| *S169' corpus/SOURCES.md` → no match, exit 1.

considerthese: `wc -lc SKILL.md` → 596 / 80,920; `awk 'length>120' | wc -l` → 151;
`length>300` → 81; longest 1,095. `sed -n '448,519p' SKILL.md | wc -c` → 26,308 (32.5 % of
80,920; round 80: 24,897/78,647, 31.7 %). Description: 1,021 of 1,024 chars, first sentence 151;
page already held as S213 (`corpus/SOURCES.md:153`, tier A). `grep -c -i provisional SCORECARD.md`
→ 2 (lines 126, 367); round 80 closes at `SCORECARD.md:476` as "honest stop; no axis score
change" with no provisional marker; round 81 attack = 17/64 = 26.6 % in-wave (plan). `du -sb .ufo`
→ 189,565,680 of 263,959,474 B (71.8 %); window `git log --since=2026-10-23 --until=2026-10-28
--numstat` → 4,479 files / 699,969 ins / 3,107 del / 142 commits. `.ufo` moved 153,824 B between
two reads 40 s apart (sibling seats writing live) — recorded as a limit of the measurement.

## Touched surfaces

- Written: `.ufo/waves/round-81/build/Kb81S12AssimDisp.md` and eight receipts
  (`Kb81S12AssimDisp-{quarantine-slice,slice.receipt,reg-ids,staged-ids,collisions,collision.receipt,fetch.txt,alias-rows.txt,consider-measures.txt}`),
  plus this seat report. Nothing else in the lane was written; no patch was produced (this seat
  lands no code).
- Read-only: `plans/round-81.md`, `corpus/SOURCES.md`, `SKILL.md`, `SCORECARD.md`,
  `corpus/lessons/round-{79,80}.md`, `.ufo/waves/round-80/assimilation/*`,
  `considerthese/2026-10-26.md`, `/home/vgpnk/Projects/shokuknow/**`.
- Scratch `/fast/scratch/hyaku/kotoba-r81/Kb81S12AssimDisp` (866,194 B) removed; `test -e` → exit 1.
- Tooling: nothing installed or upgraded; pacman untouched per the host pause.

## Out of scope / not claimed

- No claim after-value was scored: C1's tip battery and C2's SDK counter are the L1's
  post-integration measurements. No control world was built by this seat.
- No patch, no lane edit, no registry row, no `merge/kotoba/` write, no `considerthese/` edit.
- The r80 alias hazard is reported as landed, not repaired: this seat cannot renumber either id
  space.

## Findings

1. **F-Kb81S12-1 — the r80 alias prediction is fact.** 17 new collisions (S232–S248) landed with
   round 80's rows; five register ids (S236–S239, S243) now resolve to five different documents,
   and register row S185 cites a document the lane holds as S239. Adoption must key on
   (lane, cited URL).
2. **F-Kb81S12-2 — register class labels decay.** All six "could not be fetched" rows answer
   HTTP 200 today; only the "no quote recorded" half of the label is still true.
3. **F-Kb81S12-3 — P5's evidence cap cannot be measured during a wave.** 153,824 B of the `.ufo`
   figure came from sibling seats inside a 40 s window.

## Artifacts

- Deliverable (paste block + provenance): `.ufo/waves/round-81/build/Kb81S12AssimDisp.md`,
  9,458 B, sha256 `afa5a4505d90b1c74b61a3f82cf41b38260e765b2f6ff5d1fed1e23531a24c96` (after the
  reconciliation paragraph and the redirect-wording correction).
- Receipts (sha256): `Kb81S12AssimDisp-quarantine-slice` `0141c203…`, `-reg-ids` `b3d98bdc…`,
  `-staged-ids` `02a40988…`, `-collisions` `685eade1…`, `-slice.receipt` `00b104c0…`,
  `-collision.receipt` `2d9f24ed…`, `-fetch.txt` `00d0214c…`, `-alias-rows.txt` `c26271e7…`,
  `-consider-measures.txt` `8cb906ad…`.

VERDICT: Quarantine slice re-derived 13 rows and byte-identical to r80's receipt (0 new rows; register sha `5afe1810…` unchanged) — adoption closed, 0 adopted, 6/6 cited sources HTTP 200 today but 0 quotes; collisions 29→46 (S203–S248, +17 = r80's rows) with 5 slice ids now aliasing different documents; `merge/kotoba/` appended nothing; considerthese P1 `none implemented`, P2–P5 restated with today's measures (P2 26,308/80,920 B = 32.5 %, P3 page already S213 + description 1,021/1,024, P4 2 provisional + in-wave attack 26.6 %, P5 189.6 MB/264.0 MB = 71.8 %); inputs E16 absent → derived independently and corroborated by the peer.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S12AssimDisp.md ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S12AssimDisp-{quarantine-slice,slice.receipt,reg-ids,staged-ids,collisions,collision.receipt,fetch.txt,alias-rows.txt,consider-measures.txt} ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81S12AssimDisp.md
