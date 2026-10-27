# F10CheckviewS213 — round-77 w2 falsification: S213 used-by append-only compliance

Seat: F10CheckviewS213 (reviewer, leaf — no subagents, no background jobs, no installs).
Measured lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`, HEAD `6523aced1ee0ebe07dca996213bdc645a6acbd1e` (round-77 freeze).
Scratch: `/fast/scratch/hyaku/kotoba-r77/F10CheckviewS213` (shared clone; removed before yield).
Method note: no LSP server/device is available in this session, so caller/definition checks were done at git/text level as the literal fallback. Read-only git only on the lane; scratch commits made only after `git rev-parse --show-toplevel` asserted the clone root. Pacman never run; nothing installed.

## 0. Round-level blocker

The landed r77 tip `6523ace` is the **freeze commit only** (`git show --stat 6523ace`: plans/round-77.md + 4 receipts, 130 insertions). **No claim data is committed**: `git status --porcelain` shows every r77 artifact (entries, SKILL row, SOURCES used-by, lessons, R1–R4 repairs, index/baseline) as untracked under `.ufo/waves/round-77/`. Neither C1 nor C2 is verifiable at any landed revision; this seat verified the frozen counters at base/freeze and the w1 draft artifacts the L1 will integrate, and reports the used-by axis on those drafts. No landed claim is called verified.

## 1. Frozen counter reproduction (all exits are the command's own, never a pipeline's)

Counter bytes vs plan pins: `sha256sum` → `cf3c45d9e3985f11889816f4bb371dc0d5541c10c09ce2ab3966a4bff4603b9e` (check_desc_craft.py), `989203c40e1aab55fc14ee1d444dd4fa8b49fe01144b2dcdeaa6a27fa39f4a63` (check_r75_routed_repairs.py) — both equal the round-77 plan table.

| gate | command (in `$S/clone`) | result |
|---|---|---|
| C1 @ r77 base | `python3 -B verifiers/check_desc_craft.py --repo $S/clone --rev 2f675548eaad2a037a899d39247c1fd7a88aaf48` | `description craft backed 0 of 6`, `exit=1`; conjunct/finding lines match committed receipt `.ufo/waves/round-77/receipts/c1-base-2f675548….txt` incl. `(e) row S213's used-by cell does not list corpus/knowledge/description-craft-round76.md` |
| C1 @ freeze | same, `--rev 6523aced1…` | `description craft backed 0 of 6`, `exit=1` |
| C1 self-test | `python3 -B verifiers/check_desc_craft.py --self-test` | `0 failure(s) over 53 assertions`, `exit=0` |
| C2 @ base | `python3 -B verifiers/check_r75_routed_repairs.py --repo $S/clone --rev 2f675548… --work $S/work` | `r75 routed repairs closed 0 of 4`, `exit=1` |
| C2 @ freeze | same, `--rev 6523aced1…` | `r75 routed repairs closed 0 of 4`, `exit=1` |
| C2 self-test | `python3 -B verifiers/check_r75_routed_repairs.py --self-test` | `0 failure(s) over 27 assertions`, `exit=0` |

The counter's `OLD_USED_BY` constant (`check_desc_craft.py:124`) equals the real base cell bytes, so the self-test world and the lane agree.

## 2. S213 used-by append-only compliance — history (PASS)

- `corpus/SOURCES.md` is touched by **45 commits**; the S213 row exists in exactly 4 (`bf98d2837` r71 creation, `a0f7f174e` r72, `0f3e8ad75` r73, `2c81137ba` r74) plus HEAD. The full row line is **byte-identical** in all 5: sha256 `5ad7e48b711589d2238621d429140a7d189890f35a677ede6641c29521608806`. The used-by cell has **never changed** since row creation; no member was ever removed; the r71 creation diff removes no S213 line (`grep -c '^-| S213 '` = 0).
- My member-level audit over all rows and all 45 commit pairs (scratch script, `usedby-audit.txt`): used-by member removals = 3 — `d28b16b64` S001 and S003 (`SKILL.md` → round-46 entry), `55973a20a` S004 (placeholder `—`). The frozen gate `verifiers/check_sources_append_only.py` classifies all three as `log` (CORPUS rule 2 permits in-place `used-by`), and its 18 `breach` lines are non-used-by cells (teaches/scope/anchor of S019/S022/S026/S028/S050/S120/S201/S207/S209/S210), **none on S213**. Gate at base: final line `sources append-only breach 18 change(s) in 8 of 44 commits`, `exit=1`; self-test `0 failure(s) over 21 assertions`, `exit=0`.
- So: S213-specific append-only compliance **holds historically**, and gate-level "0 used-by breaches" holds lane-wide. Note for the lesson prose: `used-by` append-only is this round's seat discipline, not what the gate enforces (the gate permits in-place used-by moves; S001/S003 are precedent).

## 3. The drafted append (E08) — pure append, gate-legal, counter-satisfying (PASS)

- `E08SourcesUsedBy.SOURCES.patch`: sha256 `2a05870c2064c015d410e1a6587f506b2964bb85376eccc619e4385a08b8f564`, 6760 B (matches the draft's claim); `git apply --check` at `6523ace` → exit 0; applied → exit 0.
- Cell-level diff of line 153 (base `6523ace` vs my arm `cf810d425`): 11 cells both sides; **only cell index 10 (used-by) differs**; old value is an exact prefix; added suffix is exactly `, corpus/knowledge/description-craft-round76.md` (comma+space, the census split char). Registry rows 151, S213 ordinal 138, multi-member used-by rows 58 → 59 (E08's claims reproduced).
- Frozen C1 on my arm `cf810d425` (patch + the E08 lesson bullet as the only lesson content): `(e) registry: pass`, `description craft backed 1 of 6`, `exit=1` — matches E08's `desccraft-E-logline.txt`.
- Frozen append gate on my arm: `log  cf810d425 S213 used-by: …cts-round70.md -> …cts-round70.md, corpus/k…` (logged, not a breach); breaches stay 18 → the draft's "0 new" holds; final line `sources append-only breach 18 change(s) in 8 of 45 commits`, `exit=1`.
- Landing constraint **reproduced**: my entry-less arm trips the census — `file E11 S213 missing used-by corpus/knowledge/description-craft-round76.md`, `exit=1` — so used-by and the entry must land in the **same commit** (E08's constraint is real; the L1 must honour it).
- Stale-draft risk closed: the r76 build draft `round-76/build/sources-patch.md` (B14, measured at `4de12b6`) carries a "New line 153" that is **byte-identical** to the E08 arm row — no divergence if the L1 lifts the r76 text instead of the E08 patch.

## 4. Findings

- **LOW-1 (wording, harms no axis):** `E08SourcesUsedBy.lesson-line.md` ends "…18 pre-existing breaches in 8 of 45 commits, 0 new." At base the gate's own final line is "8 of **44**" (45 commits = 44 pairs); "8 of 45" is only true after the append lands. Minimal repair: quote the gate line with its measured revision, e.g. "(pre-append: `18 change(s) in 8 of 44 commits`; at the landed tip: `… 8 of 45 commits`)". The C1 counter does not read this number, so no predicate moves.
- **LOW-2 (integration coordination):** two differently worded but counter-satisfying lesson texts exist for the same change — the E08 bullet (verified: `(e) registry: pass`) and `SC01Lesson76.round-76.md` § Status changes bold format (verified on a second arm: `(e) registry: pass`, `backed 1 of 6`, `exit=1`). Land **exactly one** § Status changes entry; landing both double-logs the same old→new.
- **INFO:** "append-only" for `used-by` is discipline, not gate enforcement (see §2); phrase the lesson accordingly.

## 5. Residual risk / verification gaps

- Conjuncts (a)–(d),(f) drafts (snapshots, quotes, SKILL row, audit, provenance) are other seats' scope; not verified here. E08's own `desccraft-B.txt` shows (a) failing on the r76 lesson draft's Gate quote — rides with the quote reviewers.
- My two partial-tree census invocations (archive/tmp) produced spurious E11s (S224/S225, S115) — method artifacts of resolving used-by members outside a full tree; not cited as evidence. Valid census evidence: committed `receipts/census-before.txt` (`kotoba ok`, `exit=0`, 20×W04 incl. pre-existing S213 duplicate-url) and my full-clone arm census (E11-on-entry, expected).
- Gate outputs quoted above were captured to scratch files; scratch (and those files) are removed at yield — the outputs are pasted here verbatim in condensed form, per the report being the citable artifact.

VERDICT: S213 used-by append-only compliance holds historically and in the E08 draft (pure append, gate-logged, (e) passes, E11 same-commit constraint real); two LOW wording/integration defects and the round-level fact that no claim data is committed at 6523ace — C1/C2 remain unverified at every landed revision, base redness reproduced exactly.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w2/F10CheckviewS213.md
