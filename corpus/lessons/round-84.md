# Round 84 — kotoba (attempt 1, Windows host)

Base for this attempt: `ae09f71fc8262b003d69f9e35d998e74d48b6c40` (master).
FRESH-START continuity: the r79/r80/r81 rejected closures were spot-checked
last round (lesson `round-83.md` intro) and the ruled-out list is re-affirmed
and extended below (§ Ruled out). Carry-in landed first: **R83-V1** — the
r83 counter-base receipt regenerated at the correct base revision. Two
claims on distinct axes: **C1 coverage** — the second host skills root
`C:/Users/jpvei/.agents/skills` is enumerated and governed (census receipt,
PROVINCE § Core row); **C2 freshness** (lowest axis under the all-axes
reading the r82/r83 non-author closures used — freshness 8 and adjacency
8.0 tie low; the owned-axes two-readings L0 question stays open and is
routed around, not assumed) — the round-72 A1 name-uniqueness rule
re-verified against the live installed surfaces, finding 2 duplicate-name
pairs, grounded in a source opened this round (S254).

## Gate

- **Round-start census** `bash <fleet root>/scripts/sources-census.sh
  validate --root <fleet root> kotoba` → `kotoba ok`, exit 0, 179 data
  rows, the known W04 duplicate-URL warnings (32 rows flagged, including
  S065 for this round's URL) (`.ufo/waves/round-84/receipts/
  census-round-start.txt`, run before any lane change). **Round-end
  census** same command → `kotoba ok`, exit 0 (receipt
  `.ufo/waves/round-84/receipts/census-round-end.txt`; the census
  validates the fleet root's kotoba copy, which syncs at orchestrator
  wrap-up — the lane's committed `corpus/SOURCES.md` is the round's
  source of truth, and the lane file itself was validated directly with
  `--file`, exit 0, after S254 landed). Row-count command on the lane
  file: `grep -cE '^ {0,3}\| S[0-9]{3}' corpus/SOURCES.md` → 179 before,
  180 after. Rows added: S254 (Claude Code same-name resolution, opened
  this round). Rows touched: none. Frontier rows advanced: 0. One new W04
  warning joins the known class (S254 shares its URL with S053/S065,
  which hold other aspects of the same page — disclosed in the row).
- **S254 (tier A, mined).**
  https://code.claude.com/docs/en/skills.md — fetched 2026-11-01, HTTP
  200, 118879 B, sha256
  `d2a5d07c0d1cef1d1edcf30f38f6b2712ff70ac050e3d50601cd3dadb42f9097`
  (`.ufo/waves/round-84/receipts/code-claude-com-skills.fetch.md`).
  Located quote (line 207 of the fetched bytes): "When two skills share a
  directory or file name, where each one came from decides which one
  `/name` runs." — 19 words (`cut -d' ' -f1-19` of `sed -n '207p'` piped
  to `wc -w`, 2026-11-01). Companion (line 439, 27 words): "In a personal
  or project skill directory, `name` sets the command that the `/` menu
  shows and that you type, unless another command already uses that
  name." Command: `curl -sL -o <fetch> -w "HTTP %{http_code} size
  %{size_download}\n" https://code.claude.com/docs/en/skills.md`.
- **Carry-in R83-V1 closed (receipt regenerated; the filed capture stays
  as filed).** The committed `.ufo/waves/round-83/receipts/
  r83-counter-base.txt` reads `2 of 6` with `FAIL d2-anchor-consistency`,
  contradicting its own header ("must score exactly 3 of 6"), the r83
  report and lesson, and the non-author spot-check's re-run — a stale
  development-era capture, never regenerated when the counter's predicate
  was finalized. Regenerated 2026-11-01 from the frozen tip counter (blob
  `b299c265aec14d705b4eb3391a70af27234dcd53`; working-tree copy == HEAD
  blob at `ae09f71`, `git hash-object` verified) at the pinned base
  `4c95c456778baa4d61fc58a2642850c4a8b06b81`:
  `python -B verifiers/check_r83_routed_repairs.py --rev 4c95c45… --repo
  <lane>` → `r82 routed defects closed 3 of 6`, with only the three D1
  correction checks failing, exit 1
  (`.ufo/waves/round-84/receipts/r84-counter-base-regenerated.txt`);
  self-test at the same blob `0 failure(s) over 20 assertions`, exit 0.
  Header, bytes and claim now agree. Correction block appended to
  `corpus/lessons/round-83.md` (## Correction, round 84, append-only).
- **C1 coverage — the second host skills root governed.** The host
  presents a second skills root, `C:/Users/jpvei/.agents/skills` (the
  spec-tutorial `.agents/skills/` shape recorded as documentary evidence
  in round 74, live here with 15 installed `*/SKILL.md` surfaces). Before:
  zero references to its path anywhere in the lane tree at the round base
  — `git grep -l 'jpvei/\.agents' ae09f71` prints nothing over the whole
  tree; PROVINCE § Core named one host root (before-receipt
  `.ufo/waves/round-84/receipts/before-c1-c2.txt`). After: the r82 census
  instrument runs against it unchanged — `python -B
  verifiers/check_host_skill_surfaces.py --skills-root
  C:/Users/jpvei/.agents/skills --fleet-root <fleet root>` → `host skill
  surfaces measured 15: identical 0, drifted 0, lane-absent 15`, exit 0
  (`.ufo/waves/round-84/receipts/r84-agents-root-census.txt`; counting
  command `grep -c '^LANE-ABSENT'
  .ufo/waves/round-84/receipts/r84-agents-root-census.txt` → 15 — a count
  no base-rev artifact can print, because none names the root), and the
  PROVINCE § Core row landed (round-84 bullet beside the round-82 row).
  All 15 directory names are non-fleet, hence lane-absent; the class
  split is the finding, not an instrument failure (the census guards
  measurability, not expected identity). Bounds: classification only — no
  installed copy edited, no drift repaired (the r82 sibling bound
  stands); the census instrument is unchanged (no counter amendment; the
  capability generalized over roots by design, so this is a coverage
  move, not operability).
- **C2 freshness — the round-72 A1 name-uniqueness rule re-verified
  against the live installed surfaces (lowest axis: freshness 8, tied
  with adjacency 8.0 under the all-axes reading; the owned-axes
  two-readings L0 stays open, routed around).** The A1 checklist rule
  ("`name` is unique among the skills likely installed alongside it",
  SKILL.md Trigger-fidelity checklist) had never been measured against
  this host's installed surfaces. Method: extract the frontmatter `name`
  from every installed `*/SKILL.md` in both roots (24 surfaces), count
  name pairs appearing more than once. After: 2 duplicate-name pairs,
  both inside `C:/Users/jpvei/.agents/skills` — `godspeed` and `ufo`,
  each a live directory plus a dated `.pre-adapt-backup-20260927` copy
  carrying the same `name:` value; cross-root collisions 0; the `.zcode`
  root's 9 names are collision-free. Counting command: `for r in
  C:/Users/jpvei/.agents/skills C:/Users/jpvei/.zcode/skills; do for f in
  "$r"/*/SKILL.md; do n=$(sed -n '1,12{s/^name:[[:space:]]*//p}' "$f");
  echo "$n"; done; done | sort | uniq -c | awk '$1>1' | wc -l` → 2
  (ledger `.ufo/waves/round-84/receipts/r84-name-collisions.txt`;
  `grep -c 'NAME-COLLISION'
  .ufo/waves/round-84/receipts/r84-name-collisions.txt` → 2; before:
  `git grep -c 'NAME-COLLISION' ae09f71` finds no match — the class was
  never measured on this host). Grounded in S254: the harness documents
  the collision class (same-name precedence table) and the command rule
  ("`name` sets the command ... unless another command already uses that
  name"), so the two pairs are a grounded live violation of the lane's
  own rule — not an anecdote. Bounds: the colliding surfaces are flagged
  read-only, never repaired from this lane (installed copies are the
  operator's surface); the A1 box text is untouched (frozen tokens of
  `check_author_rules.py`); SKILL.md is unchanged this round; no
  behavioral claim is made about which copy the host loader favors on
  this host (S254 documents Claude Code's rule; this host's loader
  behavior is not measured here).
- **Dispatch:** the ≥8-L2 floor — this host's batched subagent surface is
  not reachable from a headless round session (fleet `.ufo/l0-questions.md`
  line 249, open since r82); the phantom-index question (line 177 —
  `baseline.json` pins the round-18 catalogue, `compare_harness_independent`
  cannot evaluate here) also stays open. Both routed around, never treated
  as answered. No wave was dispatched and none was padded.
- **Assimilation:** `considerthese/` inspected (newest digest
  2026-10-26; nothing new since the r83 check). The two claims are
  grounded in this round's own intake findings (the unenumerated second
  root; the S254 collision class); no proposal adopted.
  Assimilation: none — shokuknow unreachable.

## Mistakes

| class | evidence pointer | captured-by | fix |
|---|---|---|---|
| a claim-cited receipt captured during development was committed without being regenerated after the instrument's predicate was finalized — the committed bytes contradict the very claim they are cited for (found r83, closed this round): `r83-counter-base.txt` reads `2 of 6` with `FAIL d2-anchor-consistency` while its own header demands "exactly 3 of 6", and the frozen counter's re-run at the same pinned rev prints `3 of 6` with only the three D1 FAILs | `.ufo/waves/round-83/receipts/r83-counter-base.txt` (the stale capture, stays as filed) vs `.ufo/waves/round-84/receipts/r84-counter-base-regenerated.txt` (the re-capture at the same rev from the same blob); non-author spot-check defect R83-V1 | captured by the non-author closure judge (2026-11-01), re-proven by this round's regeneration run | landed this round: the regenerated receipt, the append-only correction block in `corpus/lessons/round-83.md`, and the going-forward rule — a receipt cited by a claim is re-captured from the frozen instrument at the frozen rev whenever the predicate changed after the capture, and the re-capture lands in the same round as the predicate freeze |

## Ruled out (fresh-start bar, this round)

- The floors-gate Windows-degraded set (10 FAIL instruments at the r83
  tip receipt `after-floors-gate-r83.txt`): real, but a "fix the floors"
  claim this round would either touch the phantom-index subject
  (`compare_harness_independent` missing / 0-vs-330 is exactly L0 line
  177 — routed around, not assumed answered) or sprawl across ten
  instruments in one round (each needing r82-C2'-scale hermeticity work).
  Named debt, unchanged; per-instrument scoped repairs remain available
  future claims.
- The tip-battery 6-of-6 lineage (r79/r80/r81 C1): the r83 ruling stands
  — killed twice by falsifying controls on the old ground; the `2 of 6`
  tally and its red gates stay named debt.
- Repairing the 6 drifted installed copies (`.zcode` root, r83 ledger)
  or the 2 colliding backup dirs (this round's finding): installed
  surfaces belong to the owning lanes and the operator's install surface
  — read-only bound (r82 ruling, stands); this round flags, never fixes.
- Substrate re-pin (omp): the subject binary does not exist on this host
  (r82 ruling, unchanged); `verifiers/baseline.json` stays the
  Linux-host record.
