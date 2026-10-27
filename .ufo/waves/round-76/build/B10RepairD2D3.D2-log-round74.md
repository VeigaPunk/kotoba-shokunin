# D2 — LOG § Round 74 line for the orchestrator snapshot `d5aebcf` (DRAFT, not applied)

Seat `B10RepairD2D3`, round 76, one v2 wave. Routed defect: `corpus/lessons/round-74-verifier-spotcheck.md`
§ Conformance defects **D2** (`d5aebcf` sits between `d919179` and `2c81137` but is absent from the report's Landed
changes table and from `LOG.md`, `grep -c d5aebcf` → 0 in both) and § Routed defects item 2 ("List the orchestrator
snapshot `d5aebcf` in the round-74 record (LOG appended correction) as a non-landing commit").

Two forms are drafted and both are measured; **FormA is a line inside § Round 74** (what this seat's prompt names),
**FormB is a tail-append correction section** (the convention `corpus/knowledge/sibling-overlap-census-round49.md`
uses for its round-50/round-51 corrections, and the only form that keeps `LOG.md` byte-append-only). The integrator
picks one; the patches are `B10RepairD2D3.formA.patch` and `B10RepairD2D3.formB.patch` beside this file.

## Verified before drafting (bytes, at `4de12b6`, 2026-10-27)

```
$ git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin log -1 --format=%B d5aebcf | cat -A
hyaku run 7 interrupted: in-flight snapshot committed by the orchestrator (not a landing); lane L1 resumes from here$
$
$ git -C … show --name-only --format='' d5aebcf | grep -c .      → 394
$ git -C … log -1 --format='%H %P' d5aebcf
d5aebcf51c394435e768461001a2d0cc8f67fe3a d919179c63925e27f0d047ccccfc30b49cfe9766
$ git -C … log -1 --format='%an|%ad' d5aebcf                    → kotoba-shokunin|Sun Oct 25 23:16:44 2026 -0300
$ git -C … merge-base --is-ancestor d919179 d5aebcf; echo $?    → 0
$ git -C … merge-base --is-ancestor d5aebcf 2c81137; echo $?    → 0
$ git -C … grep -n d5aebcf HEAD -- LOG.md; echo $?              → 1 (no hits)
```

The commit message is a **single line** (empty body), so the quoted sentence is the whole subject. `d5aebcf` is not
reachable in `LOG.md` at `4de12b6` (`grep` exit 1); it is referenced only by `corpus/lessons/round-74-verifier-spotcheck.md`
(§ D2, § Routed defects) and by r74 wave reports.

## Form A — one bullet inside § Round 74 (primary; two inserted lines)

Anchor at `4de12b6`: `LOG.md:2801` `## Round 74`, `:2803` the round-74 paragraph, `:2804` blank, `:2805`
`## Round 75 …`. Insert **after line 2803** (blank line, then the bullet):

```markdown

- **Orchestrator snapshot, not a landing (routed defect D2).** `d5aebcf` ("hyaku run 7 interrupted: in-flight snapshot committed by the orchestrator (not a landing); lane L1 resumes from here"; 394 files, author `kotoba-shokunin`, committed 2026-10-25 23:16:44 -0300) sits between `d919179` (counters and errata E1) and `2c81137` (data) on the round-74 chain: it is the orchestrator's in-flight snapshot of the interrupted run 7, not lane work, and it is listed here so that every commit this round put on `master` has a LOG line. Bytes: `git log -1 --format=%B d5aebcf`; ancestry both ways: `git merge-base --is-ancestor`. Routed in `corpus/lessons/round-74-verifier-spotcheck.md` (§ Conformance defects, D2; § Routed defects, item 2).
```

Measured consequences (scratch clone at `4de12b6`, commit `fe3ef00`):

| property | value |
|---|---|
| `LOG.md` lines | 2810 → 2812 (2 inserted, nothing removed) |
| lines ≥ 2804 | shift by +2 (`## Round 75` moves 2805 → 2807) |
| pinned `LOG.md:2111` sha256 (first 16) | `7dcbf123313d46c4` before **and** after |
| pinned `LOG.md:2678` sha256 (first 16) | `d7f442ed89197de3` before **and** after |
| `verify_skill_checklist.py --json` | `exit 0, pass 11, fail 0`; `governance.citation_resolves` 1301 → **1302** subjects, all resolve |
| `LOG@b7f13f4` is a byte-prefix of the edited `LOG.md` | **False** (first difference at byte 560524; insertion breaks append-only for the r76 base) |
| `LOG@35d44b4` / `@078eec4` / `@7d51253` / `@65a5c7a` prefix | True, True, True, True (older bases are shorter than the insertion offset) |

**Hazard for the integrator.** Form A is *not* a tail append: it breaks "LOG at the round-76 base is a byte-prefix of
LOG at the tip" for `b7f13f4`/`4de12b6`. No committed counter in `verifiers/` keys a line above 2803 (`grep -rn
'LOG\.md:2[89][0-9][0-9]'` → no hits), and `check_r63_routed_repairs.py`'s `append-only` conjunct stays `PASS
prefix=True` (its base is `35d44b4`), but if the round-76 freeze's C2 counter (or a reviewer) asserts a base→tip
prefix for `LOG.md` at this round's base, Form A fails it and **Form B does not**.

## Form B — tail correction section (append-only)

Appended at the end of `LOG.md` (after the current tail, § Round 75's Pointer bullet), leaving every existing byte
in place:

```markdown

## Round 74 correction (append-only, routed D2)

`d5aebcf` ("hyaku run 7 interrupted: in-flight snapshot committed by the orchestrator (not a landing); lane L1 resumes from here"; 394 files, author `kotoba-shokunin`, committed 2026-10-25 23:16:44 -0300) sits between `d919179` (counters and errata E1) and `2c81137` (data) on the round-74 chain and is the orchestrator's in-flight snapshot of the interrupted run 7, not lane work. The Round 74 record above lists `d919179` and `2c81137` and not this commit; it is listed here so every commit that round put on `master` has a LOG line. Bytes: `git log -1 --format=%B d5aebcf`; ancestry both ways: `git merge-base --is-ancestor`. Routed in `corpus/lessons/round-74-verifier-spotcheck.md` (§ Conformance defects, D2; § Routed defects, item 2).
```

Measured (commit `47a2f92`): `LOG@b7f13f4` and `LOG@4de12b6` are byte-prefixes of the edited `LOG.md` (**True/True**);
`check_r63_routed_repairs.py --rev <tip>` → `PASS append-only prefix=True grew_by=248`, `r62 routed defects closed 5 of
5`; `verify_skill_checklist.py --json` → `exit 0, pass 11, fail 0`, `governance.citation_resolves` 1302, all resolve.

**Ordering note.** The round-76 LOG entry (seat `B19LogScribe`, `.ufo/waves/round-76/build/log-draft.md`) is itself a
tail append. With Form B the two tail sections can be applied in either order (`git apply` tolerates the offset);
records should read § Round 75 → round-76 entry → round-74 correction, or round-74 correction → round-76 entry — both
are append-only, only the reading order differs. With Form A the position is independent of the entry.

## Both forms — no delta on the gates that read these files

Measured at `4de12b6` (base), `fe3ef00` (Form A) and `47a2f92` (Form B) in the same scratch clone with a fleet-layout
shim:

| gate | base | Form A | Form B |
|---|---|---|---|
| `verify_corpus_integrity.py --json` | exit 1, 4 DRIFT | exit 1, same 4 | exit 1, same 4 |
| `verify_corpus_independent.py --json` | exit 1, same 4 | exit 1, same 4 | exit 1, same 4 |
| `verify_skill_checklist.py --json` | exit 0, 11 pass | exit 0, 11 pass | exit 0, 11 pass |
| `check_sibling_reread.py`-class census r74 | exit 0, 20/20 | exit 0, 20/20 | exit 0, 20/20 |
| `check_r67_routed_repairs.py` | 3 of 4 (D4 baseline) | 3 of 4 | 3 of 4 |
| `check_r69_routed_repairs.py` | 9 of 10 (K69-11) | 9 of 10 | 9 of 10 |
| `check_r69_routed_repairs_v2.py` | 8 of 10 (K69-3, K69-11) | 8 of 10 | 8 of 10 |

The 4 corpus DRIFTs are **pre-existing at the declared base** `b7f13f4` and are not caused by this fragment:
`corpus.index.tracked_files 145 vs 144`, `corpus.index.unindexed 1 vs 0`
(`corpus/lessons/round-75-verifier-spotcheck.md`), `corpus.pointers.report_total 101 vs 99`,
`corpus.pointers.commit_total 44 vs 43`. Detail and the base-battery receipt discrepancy: `B10RepairD2D3.measurements.txt`.

## Landing instructions

1. `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin apply --check .ufo/waves/round-76/build/B10RepairD2D3.formA.patch`
   (or `…formB.patch`); both apply cleanly to `4de12b6` and are line-anchored on the round-74 paragraph.
2. Apply one form only. Applying both would put the same sentence in § Round 74 and again in a correction section.
3. Re-run `python3 -B verifiers/verify_skill_checklist.py --json` (expect `pass 11`, `governance.citation_resolves`
   1302 with all subjects resolving) and `python3 -B verifiers/check_r63_routed_repairs.py --rev <tip>` (expect
   `r62 routed defects closed 5 of 5`, `append-only prefix=True`).
4. No new file, no registry row, no `SKILL.md` line: the fragment is content-only, so no counter that counts files
   (`tracked_files`, `report_total`, `commit_total`) moves — measured, not assumed.
