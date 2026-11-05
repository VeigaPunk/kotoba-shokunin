# Round 90 — ConnectorOverlap (kotoba, seat ConnectorOverlap)

Read-only scan across sibling lanes for the two round-90 surfaces: C1 (mutation battery over kotoba's
round-89 gates) and C2 (host installed-skill census). Nothing outside this file was written.
Pins at scan time: tameshi-shokunin HEAD `f256302b394ae3253df014fe1131e2c20e2c16b6` (2026-11-05 05:17:09 -0300);
kotoba-shokunin HEAD `6fa5bb6d4ceeb51f0455e512a52d8b75628f404c`; round base `0c20d8ab65587aee0e97b7d14c801ae6dc44c2e5`;
plan commit `6af71591e7232a7eebbaff78e7db653a70c7218b` is an ancestor of kotoba HEAD (`git merge-base --is-ancestor` → true).

## 1. Mutation method — tameshi overlap and boundary

Evidence:
- `git -C tameshi-shokunin` read-only: `tools/mutate-and-run.sh` is the generic mutation runner (r3-2 → r51). Its `--regression`
  ledger replays ten measured legs at pinned revisions, materialized from `git show <rev>:<path>`:
  `js-kimi-census`, `js-round-gate`, `js-sources-check`, `js-cite-check`, `js-claims-check`, `bash-surface-census`,
  `bash-tsukuroi-census`, `bash-mado-verify`, `bash-checklist-run`, `bash-drift-pins`.
  `grep -c -i kotoba tools/mutate-and-run.sh` → `0`. No kotoba gate is a tameshi leg; no tameshi mutation-case note names kotoba.
- `PROVINCE.md` (Owns / Refuses): tameshi owns "the reusable craft (a pattern is admitted from evidence in TWO independent lanes
  before it is claimed general)"; "every lane's gate remains its own"; "Out of province → report, never absorb".
- kotoba's C1 (`plans/round-90.md:44-48`, frozen) mutates only kotoba's own two round-89 instruments
  (`verifiers/check_freeze_gate.py`, `verifiers/check_r86_routed_repairs_v3.py`), reads through `git show <rev>:<path>`, and
  ships `verifiers/check_mutation_battery.py` as a new in-lane file. The r89 harness
  (`.ufo/waves/round-89/w1/MutTesterGates/harness.py`) already uses the same method in-lane (pristine copy, one exact edit per mutant,
  `rep()` uniqueness assert, `ANCHOR-MISS` refusal).

Boundary sentence (also written to CONNECTOR_READY): kotoba's C1 adds a committed, in-lane mutation run over kotoba's own
two round-89 gates, reusing tameshi's method on revision-pinned scratch copies without importing tameshi's legs,
`mutate-and-run.sh`, or its `--regression` ledger. It does not absorb tameshi's ten recorded legs or any sibling gate, and each lane's
gate stays its own.

Overlap verdict: method-level only (shared technique, zero shared code or gates). Routing: none required now; if tameshi wants the
kotoba run as a second independent instance of the method, that is a finding to route to tameshi in the round report, not an
absorption from kotoba.

## 2. Host installed-skill census — sibling claims

Evidence: `grep -rl -i 'host skill surface\|installed-skill\|installed skill\|\.agents/skills' */corpus` returns many lanes, but
`grep -rn -i 'host skill surface' */corpus` returns only kotoba: `corpus/lessons/round-82.md:35`,
`corpus/lessons/round-82-verifier-spotcheck.md:37`, `corpus/lessons/round-84-verifier-spotcheck.md:50`. No other lane claims the
census surface (all-83 `*/SKILL.md` at the host root against fleet lane copies).

Overlapping owner found (partial, different surface):
- kaidoku-shokunin owns the REA skill identity on the same root: `kaidoku-shokunin/corpus/README.md:353` ("R4 recheck reports
  `skill:identity` as `config_drift` (`37/170/stale`): the shared `~/.agents/skills` copy matches the bundled v37 skill
  byte-for-byte … destination drift"), `corpus/knowledge/2026-10-13-rea-skill-contract.md` (studied artifact
  `~/.agents/skills/reverse-engineer-anything/`), `corpus/knowledge/2026-10-13-mcp-registrations.md`.
  game-dev-3d-shokunin `corpus/knowledge/rea.md:6` also names the same installed REA source (reference, not a claim on identity).
- Consequence for C2: kotoba's census verdict `lane-absent` for an installed skill that has no fleet-root `<name>/SKILL.md` is a
  measurability classification, not an identity claim. Any REA-identity reading stays owned by kaidoku. kotoba's census must not
  be cited as REA identity evidence, and kaidoku's destination-drift finding is not kotoba's to fix.
- Measured: `ls /home/vgpnk/.agents/skills | wc -l` → `83` (matches plan). Fleet-root top-level `*/SKILL.md` directories exist
  for `chousa-shokunin`, `game-dev-3d-shokunin`, `kagi-shokunin`, … (lane-root SKILL.md, not `<name>/SKILL.md` children, so the
  census's name-match is by subdirectory of the fleet root only).

kotoba's r82 precedent stands: drift findings route to the owning lane, never fixed from kotoba.

## 3. Newest sibling lessons — routed items touching kotoba's two surfaces

Titles scanned from `ls -t */corpus/lessons/round-8*.md` (top eight: kotoba r88/r89 + spot-checks, mado r87, kama r87).
Routed items skimmed:

| lane / file | routed item | touches kotoba surface? |
|---|---|---|
| kama `corpus/lessons/round-87-verifier-spotcheck.md:54` | MT02 battery `mutants=7 killed=7 escaped=0` is **not** kill evidence: its own pristine check read `not-ok` on the default copy; not counted | **Yes — C1.** kotoba's C1 counts a kill as "probe exit flips away from the frozen baseline" (`plans/round-90.md:41`). The frozen G1–G3 guards do not require the unmutated baseline to be green (`plans/round-90.md:46-48`). The r89 harness has a pristine copy but the predicate does not name it. Finding for the round report: a pristine-baseline guard is absent from the frozen predicate; route, do not amend (plan is frozen). |
| mado `corpus/lessons/round-87-verifier-spotcheck.md:117` (R4) | declaration hygiene: carry the sha pin in the declared command from the freeze | Adjacent — the freeze gate's declarations (`plans/round-90-controls.md`) carry no sha pin per control; mado's routed note is mado's own. Informational. |
| kotoba `corpus/lessons/round-89-verifier-spotcheck.md:110` (routed 2) | "mutation battery re-run on final (post-A2) bytes" | Yes — already C1's surface (kotoba-owned, in plan). No sibling claim. |
| kengaku `corpus/lessons/round-89-verifier-spotcheck.md:110` | frozen Move element (d) unimplemented; route to round 90 as a counter-side extension | No — kengaku claims-figure surface. Not kotoba's. |
| tameshi `corpus/lessons/round-87-verifier-spotcheck.md` | pinned-measure re-execution discipline | No routed defect against kotoba. |

No sibling routed item asks for a change to kotoba's census instrument or to the host skills root.

## Evidence commands (re-runnable, read-only)

- `git -C /home/vgpnk/Projects/shokunin/tameshi-shokunin rev-parse HEAD` → `f256302b394ae3253df014fe1131e2c20e2c16b6`
- `grep -c -i kotoba /home/vgpnk/Projects/shokunin/tameshi-shokunin/tools/mutate-and-run.sh` → `0`
- `grep -rn -i 'host skill surface' /home/vgpnk/Projects/shokunin/*/corpus` → kotoba lessons only (rounds 82, 84)
- `grep -n 'skill:identity' /home/vgpnk/Projects/shokunin/kaidoku-shokunin/corpus/README.md` → line 353
- `ls -t /home/vgpnk/Projects/shokunin/*/corpus/lessons/round-8*.md | head -8` → kotoba r88/r89, mado r87, kama r87
- `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin merge-base --is-ancestor 6af71591e7232a7eebbaff78e7db653a70c7218b HEAD` → exit 0
- `ls /home/vgpnk/.agents/skills | wc -l` → `83`

## Risks

1. C1 predicate lacks a pristine-baseline guard (section 3, kama row). A kill can be counted against a broken baseline. Finding only.
2. C2 `lane-absent` may be misread as identity drift for REA; kaidoku owns that identity surface.
3. tameshi method reuse is shared technique; if tameshi later absorbs kotoba's battery as a leg, that would violate PROVINCE "each lane's gate stays its own" unless it is re-admitted as a second independent instance.

No install, no kernel or host setting touched, no sibling written, no git write.
