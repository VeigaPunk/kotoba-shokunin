# kotoba — round 24 report (2026-10-19)

Lane: `kotoba-shokunin`. Round 24, loop 1 (loop-round 4), dispatched and admitted **on scout-corrected claims**.
Dispatch HEAD: `b889e78`. Work commit: `<pending — recorded at landing, round-11 precedent>`.
Lane identity for the commits: `kotoba-shokunin <kotoba@shokunin.local>`.
Claims: **E** freshness (documentary errata) · **H** operability (checklist self-test export hermeticity) — `.ufo/round-24/claims.json`, **both put on HOLD as filed by scout C1; landed on C1's corrections** (filed texts stand; corrections recorded in LOG § Round 24 and here).
Provider: hyper `402 out of credits` on all lanes at dispatch → the stated fallback applied verbatim: `devin/deepseek-v4-1-flash-high`, 48 items, all fragments on disk (45 in the summary; three landed late).
Status: **completed craft round, admitted** — both claims verify on the corrected terms; no axis harmed.

## Work performed

- **E — the corrected errata set** (drafts: scouts E1-E8; re-targeting: C1 defects 1-4, 9):
  - census `instruction-surface-census-round13.md`: 9→5 opencode ids (:288), seven→six rules (:28, :287), 72→75 assertions (:272), 41→38 extra-row findings (:293); the third 'seven' (:337) is **inside the sha-pinned round-22 block** — preserved byte-verbatim, corrected by an append-only erratum beside the block (E1's recommendation; contiguity re-verified: `e046a025…` reproduces).
  - `harness-verifier-round10.md`: 27→28 checks (:15), 27/27→28/28 (:186) + vacuity note (6 of 11 opencode checks read 0 against the v2.0.26 grammar — scout R3 reproduced).
  - `independent-verification-round12.md`: append-only round-24 erratum — W0 `10/19` reads **19/19** on this host (the 10 was the round-12 host's lowercase `/home/vgpnk/projects` base, reconstructed in `unshare -rm`); §2's `43=37` glues two tree states (`43 = 43` at either).
  - SHONEN (:7, :46) + README (:49 — the third occurrence claim E missed): `PROTOCOL.md:34-39` → `:65`; SHONEN's embedded awk output 14→15.
  - SKILL.md present-tense :109/:461: 27→28. **Kept as dated records (C1 defects 1-2):** SKILL.md:456, both SCORECARD '4 checks' cells.
- **H — Fix A** (the mechanism C1's verdict substituted for the filed Fix B): two hunks pinning `--repo str(DEFAULT_REPO)` in the self-test fixture argv (`:1341`, `:1555`). Verified at landing: archive-export self-test `0 failure(s) over 1504 assertions` (was 108/1504; count exact per C1-H4's anti-shrink observable); live gate + self-test byte-invariant; probe-dir removal → 2 failures; box tamper → box_map FAIL; pinned-block contiguity holds. **Fix B deferred** — it changes live CLI behavior (foreign `--skill`: FAIL governance → N/A) and needs three docstring edits (`:142`, `:180-181`, `:1707-1708`); named debt.
- **Pin supersession (C1-H3):** checklist sha `02ccf1b3…` → `15d0aa16…`; the routing-16 JSON pin updated (`sha_superseded_from` note); the historical prose pins superseded by the LOG entry, not rewritten.
- **Adjacency (held):** ack still 0 across siblings; L0 round-22 line still uncommitted (integrator-owned).
- **Deliberately not done:** no Fix B; no dated-record rewrites; no push (ahead 8+); no SHONEN mark changes.

## Landed changes

- Six corpus/doc errata + SHONEN/README/SKILL corrections + the census append-only erratum [LOG § Round 24].
- `verifiers/verify_skill_checklist.py` — Fix A (2 hunks) [LOG § Round 24].
- `corpus/knowledge/sibling-citation-routing-round16.json` — instrument pin updated to `15d0aa16…` with supersession note.
- `SCORECARD.md` — freshness + operability rows annotated, move-log rows, planned refreshed.
- `LOG.md` — § Round 24 appended.
- Intentionally unchanged: the dated records C1 classified keep; the five instruments' check semantics; sibling repos; protocol files.

## Before → after measurements

| Claim | Measurement | Before | After (round 24) | Command/evidence |
|---|---|---|---|---|
| E | census counts | 9 ids / 7 rules / 72 assertions / 41 rows | 5 / 6 / 75 / 38 (in-block 'seven' errata'd, bytes frozen) | scouts E1 + live re-measure |
| E | harness-doc count | 27 checks / 27/27 | 28 / 28/28 + vacuity note | scout E2 + live run |
| E | round-12 W0 | 10/19 recorded | 19/19 on this host (host-conditional erratum) | scout E3 + unshare repro |
| E | stale PROTOCOL anchor | `34-39` ×3 + awk 14 | `:65` ×3 + awk 15 | scouts E4/C1 greps |
| H | export self-test | 108/1504 exit 1 | 0/1504 exit 0 (count exact) | git-archive of `git write-tree` |
| H | live behavior | 10 × PASS, 0/1504 | byte-identical | output diff + red probes |

Axis verdicts: **freshness — improved** (score held 8.0: recorded counts now reproduce; dated records preserved); **operability — improved** (score held 8.5: the self-test is portable to any checkout/export, anti-shrink encoded); adjacency / coverage / calibration / depth / consistency — **unchanged**. No trade.
Drift handling: claims corrected per C1 **before** landing (the filed texts stand; the corrections are the round's record); pin supersession acknowledged (C1-H3); hyper exhaustion recorded with the devin fallback; three late fragments noted.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — unchanged by the errata (two present-tense counts corrected; dated records kept; the file's evidence base intact).
- [~] End-to-end domain task executed and logged — unchanged; rounds 21-24 logged, lane-authored.
- [~] Instructions executable without oral context — strengthened: the self-test now runs green in a bare `git archive` export (the exact bar a fresh clone elsewhere imposes).
- [~] No cross-domain bleed — unchanged; siblings read-only; no fleet-path writes.
