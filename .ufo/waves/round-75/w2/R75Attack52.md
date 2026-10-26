# R75Attack52 — attack on R75Facet52

## Verdict

**Underlying Q70 enforcement gap survives, but the facet’s account of current gate behavior is materially wrong.** At its stated revision `65a5c7a663249e0522cc49e4a148424200d9ddfe`, the counter the entry names does not back eight facts: it returns **1 of 8**, exit 1. F1–F7 name S212/S213, which are absent from the v1 counter’s `SNAPSHOTS` map; those seven rows fail before the quote/snapshot check. Thus the report’s “eight facts pass … by construction” table is not evidence that the measured gate currently evaluates those rows, and its cited `8 of 8` SKILL registry description is stale relative to the committed entry. The narrower finding—that v1 does not enforce Q70’s shared-page uniqueness/quote-position/registry-digest/fetch-record conjuncts—remains substantiated by the code and data. No proposed source change is judged here.

## Independent evidence at the measured revision

- `git rev-parse HEAD` returned `65a5c7a663249e0522cc49e4a148424200d9ddfe`. `git show <rev>:corpus/knowledge/skill-eval-artefacts-round70.md` confirms F1–F7 cite S212/S213, while F8 cites S211; the entry’s committed `recheck:` names `check_skill_evals.py --rev <rev> --fetch` (`corpus/knowledge/skill-eval-artefacts-round70.md:1-8`).
- `verifiers/check_skill_evals.py:46-56` maps only S209, S210 and S211. Its `check()` rejects unrecognized source IDs at `:157-159`, before calling `Repo.snapshot()` (`:160`).
- I ran `python3 -B verifiers/check_skill_evals.py --rev 65a5c7a663249e0522cc49e4a148424200d9ddfe`: output was `skill eval facts backed 1 of 8`, seven findings `S212/S213 has no pinned snapshot`, exit 1. F8/S211 is the single backed fact. This directly contradicts the report’s assertion that the named counter currently evaluates eight facts.
- `SKILL.md:503` still advertises `8 of 8` at measured rev and `0 of 8` at base. `SKILL.md:505` separately registers v2 as a round-71 successor; the entry’s own recheck still points to v1. The reported mismatch is therefore an actionable registry/entry-gate inconsistency, alongside (not instead of) the Q70 gap.
- Source checks agree with the report’s core Q70 evidence: v1 checks only quote membership after the configured snapshot hash (`check_skill_evals.py:89-97,160`); `live_fetch()` only counts quote presence and records no status/digest (`:178-194`). The S212/S213 rows at `corpus/SOURCES.md:152-153` carry upstream commit anchors, not the snapshot digest. Q70 `corpus/QUALITY.md:86` explicitly requires the digest in the counter, cited row anchor, and HTTP-200 fetch record, plus page uniqueness and quote position. These facts support a gap finding, although the named v1 gate does not pass the present entry’s seven rows.

## Bounded detector and mutation probe

Ran the v1 `--self-test` offline on an isolated copy sourced from the measured commit (no network): pristine output `self-test: 0 failure(s) over 13 assertions`, exit 0. In that scratch copy, the single-point mutant replaced the actual snapshot digest comparison at `Repo.snapshot()` line 95 with `if False:` (disabling digest-tamper rejection). The **same** `python3 -B check_skill_evals.py --self-test` still returned `self-test: 0 failure(s) over 13 assertions`, exit 0. The fake-repo test only makes `snapshot()` raise when its fixture value is absent; it does not exercise the real hash comparison. This mutant **survived**: the self-test is not a behavioral control for the digest guard, despite its “tampered snapshot” assertion.

Restored the exact measured-commit file bytes and reran the same detector: it again returned 0 failures. SHA-256 before and after restoration was `fc768197e10b152c444985a8fe41cf1c62f6d1c0605251d198d921dc35b68db2`; mutated scratch bytes were `82652f6eb7acdca36ff84e263449d2eee5fceb710ee19ebef836b273a9991c04`. The scratch directory was removed. No lane source was modified.

## Control assessment / limits

The report’s proposed committed-bytes grep audit is a direct structural check and is not vacuous for the stated missing row digests/record. Its suggested future fixture arms are proposals, not evidence of existing coverage. The existing v1 self-test is insufficient for the counter-locus hash behavior, as the surviving mutant demonstrates. I did not run `--fetch` or make network requests.

The checkout had a working-tree modification to `corpus/knowledge/skill-eval-artefacts-round70.md` (an appended round-75 correction); I used `git show` at the measured revision for the committed-byte check above. This does not change the measured-revision result, but means the facet’s blanket working-tree-clean statement was not true at the time of this attack.

## Evidence paths

All paths below are relative to the kotoba lane.

- `.ufo/waves/round-75/w1/R75Facet52.md`
- `corpus/QUALITY.md:86`
- `corpus/SOURCES.md:152-153`
- `corpus/knowledge/skill-eval-artefacts-round70.md:1-8`
- `SKILL.md:503,505`
- `verifiers/check_skill_evals.py:46-56,89-97,157-160,178-194,253-313`
- `verifiers/check_skill_evals_v2.py:35-40,78-86,295-308,321-340`
