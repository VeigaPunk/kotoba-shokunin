# ScoutW2SiblingOverlap

role: scout (leaf member — no subagent dispatch)
item: Sibling-overlap scan for round 63's two new ground items — (1) correction/errata practice for a published record (S119, ICMJE); (2) compound-clause citation support checking (G9). Owning-province question only. Report only; no production edit.
tools installed: none

Axes named: **adjacency** (this seat). The bound below must not move depth (C1's G9 predicate) or calibration (C2's five-check counter).

## Attack

Live tree, read-only, 2026-10-23. Not the round-49 census pins. Home lane `kotoba-shokunin` excluded from the sibling set. `aggregator-shokunin` is not a directory under `/home/vgpnk/Projects/shokunin` or `/home/vgpnk/Projects` (`NONE`).

Command (python3, stdlib only):

```text
test aggregator-shokunin; list *-shokunin;
strict scan of every sibling SKILL.md and PROVINCE.md
(pattern: ICMJE | published record | compound-clause | compound clause |
 \bG9\b | g9_conjunct | forward-support | errata practice |
 correction practice | correction/errata, case-insensitive)
```

Verbatim result of that scan:

```text
aggregator-shokunin: ABSENT
aggregator dirs under Projects or shokunin: NONE
LANE_COUNT 21
SIBLING_FILES 37
MISSING
audio-shokunin/SKILL.md
game-dev-2d-shokunin/SKILL.md
revenger-shokunin/SKILL.md
--- STRICT HITS ---
STRICT_HITS 0
```

The 20 siblings scanned: audio, chousa, game-dev-2d, game-dev-3d, kagi, kaidoku, kake, kama, kasegi, kengaku, kotodama, kumitate, lore, mado, mori, revenger, souji, tabi, tameshi, tsukuroi. 37 boundary files present; the three MISSING rows are lanes with no `SKILL.md`.

A prior pass over the same 37 files also searched boundary windows for `claim-vs-source`, `citation chain`, `citation support`, `Errata append-only`, and a bare `S119` token. Those hits are quoted under Nearest lines. None of them is an **Owns** / **Domain** claim on either item. Bare `S119` is a homonym (see below); it was kept out of the strict pattern on purpose.

## Verdict on the committed bytes

`kotoba-shokunin/PROVINCE.md:27` (tip `cbbee56e`) puts both items in Core in one bullet: Action-cell clause support counted by `verifiers/check_scoped_rules_v32.py --self-test`, and an appended notice on a committed record (S119) counted by `verifiers/check_r63_routed_repairs.py`. Closing clause: "This is the documented rule and its counter, not a measured client behaviour."

**No sibling claims either item.** `contested` does not arise. `STRICT_HITS 0` is the negative. Candidate provinces, on their own boundary text:

- **chousa** (research method) — nearest, not an owner. `PROVINCE.md:5-6` owns "citation chaining and hop resolution; claim-vs-source verification" as the research method. It does not name compound clauses, Action cells, a forward-support fraction, G9, ICMJE, or published-record correction. `SKILL.md:517-518` says the opposite of owning citation support: that screen is not complete, and "citation support and truth still require QUALITY6–8 and a reviewer."
- **tameshi** (fixture/mutation method) — `PROVINCE.md:3-5` owns hermetic suites and mutation testing. `PROVINCE.md:14-15` refuses the product gate: "every lane's gate remains its own; tameshi owns only the reusable craft." G9's must-fail arm is kotoba's own verifier. Not a claim on the predicate.
- **kengaku** (calibration) — `SKILL.md:3` triggers on "eval calibration" and "interval-calibrated verdicts" and states "kotoba owns prompt and skill craft (kengaku keeps only measured capability effects)." `PROVINCE.md:137` routes claim-vs-source to chousa. `PROVINCE.md:139` routes fleet closeout gates to "protocol / aggregator". That is model-eval calibration and a fleet-process referral, not S119 and not G9.
- **aggregator** (cross-lane) — no `SKILL.md` and no `PROVINCE.md`, because there is no `aggregator-shokunin` directory. Nothing under the mandated sweep root can own either item.

Wave-1 `ConnSibling.md` routed both moves to kotoba off census pins. This live re-scan does not falsify that routing. It does falsify two narrower readings of that report: (i) a bare `S119` grep is not evidence of this row; (ii) "Errata append-only" standing rules exist in more than the one tameshi line that report quoted, and they are still not domain claims.

## Nearest lines (not contested scope)

Exact sibling text a later reader could mistake for a claim:

```text
chousa-shokunin/PROVINCE.md:5-6
**Owns:** question framing; source hierarchy (primary / secondary / aggregator /
unsourced); citation chaining and hop resolution; claim-vs-source verification;

chousa-shokunin/SKILL.md:517-518
URL/anchor sufficiency, source tier/scope, actual opening, citation support
and truth still require QUALITY6–8 and a reviewer.

tameshi-shokunin/PROVINCE.md:14-15
**Refuses:** product domains — every lane's gate remains its own; tameshi
owns only the reusable craft (a pattern is admitted from evidence in TWO

tameshi-shokunin/SKILL.md:24
- Errata append-only; rejections kept.

tabi-shokunin/SKILL.md:10
knowledge. Observation / inference / unknown stay separate; errata append-only.

tsukuroi-shokunin/SKILL.md:18
- Errata append-only; rejections kept.

mado-shokunin/SKILL.md:38
- Errata append-only; rejections kept.

kengaku-shokunin/PROVINCE.md:137-139
| **chousa** | research method — … citation-chain → claim-vs-source method stays chousa's
| **kotoba** | prompt- and skill-craft rules — … reusable craft implications route out
| **protocol / aggregator** | fleet process — a fleet-wide preregistration/replay-gate standard and closeout carry-over gates were referred round 11/12–14, not imposed

kumitate-shokunin/PROVINCE.md:27
- Local model serving and endpoints → kama. Prompt and skill craft → kotoba. Research method → chousa.

kama-shokunin/SKILL.md:1107
… | S119 |
(row E26-06, llama.cpp pooling-type refusal. That lane's own source id.)

mado-shokunin/SKILL.md:1970
… S119 supersedes the module-list inference, and S120 binds the annotation decision …
(round-21 Python annotation note. That lane's own source id.)
```

Other **Owns** / **Domain** heads scanned and not quoted in full because they name a different domain (audio game-audio, game-dev-2d/3d production, kagi secrets, kaidoku/revenger shipped-artifact RE, kake publishing, kama endpoints, kasegi bounties, kotodama worldbuilding — and kotodama `PROVINCE.md:19-20` refuses "prompt/skill craft (kotoba)" — lore records, mado compositor, mori observability, souji hygiene, tabi browsers, tsukuroi host repair). None of those heads contains the strict pattern.

## Smallest safe correction (bound; do not edit the predicate)

`PROVINCE.md:27` is not false. Its heading, "Compound-clause citation and correction practice", is wider than the bullet's own instruments and wider than any sibling line. Standing "Errata append-only" rules and chousa's claim-vs-source sentence sit next to that width. Narrow the subject; leave both counters and both frozen predicates untouched.

Replace only the bullet's opening noun phrase. Exact proposed text:

```text
- Compound-clause citation on this lane's scoped-rule Action cells, and appended correction of this lane's own committed record (round 63):
```

The rest of line 27 stays. After its existing closing sentence, append this one sentence:

```text
Sibling bound: no sibling SKILL.md or PROVINCE.md under /home/vgpnk/Projects/shokunin/*-shokunin/ owns either item (37 files, 2026-10-23, strict hits 0; aggregator-shokunin absent). chousa PROVINCE.md:5-6 owns claim-vs-source verification as research method and is cited, not re-derived; chousa SKILL.md:517-518 leaves citation support to a reviewer. tameshi PROVINCE.md:14-15 keeps every lane's gate its own. Append-only errata lines in sibling skills are each lane's record discipline. A sibling token S119 (kama SKILL.md:1107, mado SKILL.md:1970) is that lane's source id, not this row.
```

## Risks

- Reading chousa `PROVINCE.md:5-6` as owning G9 would re-derive the research method. The bound forbids that reading; the G9 predicate stays an Action-cell check on this lane's scoped-rule rows.
- Reading tameshi `PROVINCE.md:3-5` as owning the must-fail arm would absorb the mutation method. The arm stays a mutation of kotoba's gate, which tameshi's own refusal already assigns to the product lane.
- Treating kama/mado `S119` as this round's ICMJE row would invent a contest. They are homonyms.
- The bound does not change `survivors closed 6 of 6` or `r62 routed defects closed 5 of 5`.

## Verification (for the L1; not run here as a production edit)

1. Re-run the strict scan above. Expect `STRICT_HITS 0` and `aggregator-shokunin: ABSENT`.
2. After the noun-phrase edit only, `PROVINCE.md:27` must still name `verifiers/check_scoped_rules_v32.py --self-test` and `verifiers/check_r63_routed_repairs.py`.
3. Do not treat this bound as a change to either frozen predicate.
