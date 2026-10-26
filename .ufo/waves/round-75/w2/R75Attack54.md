# R75Attack54 — falsification of R75Facet54

## Axes
Factual accuracy; control efficacy; scope/actionability; probe operability and byte restoration.

## Verdict
**Partially survives; central missing-self-check claim is supported, but several consequential details/control prescriptions are overstated or insufficiently tested.** The current checklist has no length or charset enforcement for its own frontmatter. The report's proposed new check is not the only possible control and the user-visible invariant is broader than the stated report's numeric half; however, the report correctly exposes the coverage gap. Its claimed successful mutation experiment is plausible and consistent with the committed checker, but I did not independently reproduce the exact mutant because my insertion scripts failed to locate its YAML marker after the first attempt had already altered scratch bytes. I therefore do not claim a successful mutant kill/survival experiment of my own.

## Independent evidence at measured revision
Lane `HEAD` is `65a5c7a663249e0522cc49e4a148424200d9ddfe`. The working tree has user changes (`SKILL.md` modified among others); I treated these as out-of-scope and used `git archive HEAD` for scratch. The committed `SKILL.md:162` explicitly states both `name ≤64` plus charset and `description ≤1024` constraints. The committed checker has `check_frontmatter` at `verifiers/verify_skill_checklist.py:1385-1400`, which only checks parsed fields are present and reports `len(fields["description"].strip())`; `check_name_directory` at `:1403-1415` checks only equality with the directory basename. No length/charset assertions appear in those functions. `check_sibling_census.py:417-418,502-563` sets a 1–1024 cap but the helper is for census lane rows, not the current lane's own checklist assertion.

A pristine scratch archive with its directory named `kotoba-shokunin` ran:
`python3 -B verifiers/verify_skill_checklist.py --check trigger.frontmatter_parses --check trigger.name_directory --check trigger.no_xml_tag`
Output: `PASS` for all three; frontmatter reports 1021 stripped chars. This confirms baseline operability at the right repo-relative location. The checker run from a scratch parent named `R75Attack54` instead failed `trigger.name_directory` (expected path-dependent behavior, not counterevidence).

I directly invoked the committed `check_name_directory` function with directory-matching names: 70 lowercase `a` characters returned PASS; a 30-character repeated `A_b` string returned PASS; `kotoba-shokunin` returned PASS. Thus the report's name-bound counterexample is independently reproduced at the function/control level.

## Attack and limitations
- The facet's core inference — the stated two portability constraints are not checked by the self-checklist checks it describes — survives source inspection. Citation/line claims for the relevant functions are accurate.
- Its broader phrase “no executed check behind them” should be read as “no check that enforces these bounds on kotoba's own SKILL.md.” A sibling-census check does enforce a 1–1024 description bound on other lanes, as the report itself notes. This is a useful qualification, not a refutation.
- The report's own mutant outcome (description +20, checks still PASS; census fails) was not independently rerun by this seat. My first scratch edit accidentally put text after the YAML `>` indicator and caused PyYAML parsing to fail, though the checklist parser still printed PASS; the attempted fix then failed its marker assertion. I restored pristine archived bytes immediately afterward, before any claim of a controlled mutated frontmatter test. This failed attempt is excluded as detector evidence.
- The proposal binds loaded YAML length, but assumes `PyYAML` semantics are the controlling authoring convention. SKILL.md:562-565 is cited by the report for the hashing convention; that establishes the value convention for compressor-cache hashes, not necessarily an external portability spec's count convention. The correct cap/measurement semantics require deriving from the named authority (S018) rather than treating the cache convention as dispositive. The checker itself currently strips whitespace; the report's proposed stricter bound is actionable only if explicitly sourced and aligned to the target rule.
- A missing enforcement check is materially actionable only if this file is intended to be subject to its own portability rule. Here it explicitly states a lane portability floor and the description currently sits close to its bound, so adding a self-check is reasonable. The suggested “new check + baseline box + assertion count + arithmetic” is implementation planning beyond what falsification establishes; no need to accept every prescribed detail from this finding.

## Detector output / verdict
Expected detector: on pristine bytes, selected frontmatter/name/XML checks PASS; on a structurally valid >1024-description mutant, existing selected checks remain PASS (finding's predicted survivor); a new length check would FAIL that mutant. Actual outputs: pristine PASS×3, path-mismatched scratch FAIL name equality, and independently exercised name-bound cases PASS/PASS/PASS. The overlength mutation detector result is **inconclusive for this seat** due to failed scratch mutation setup. Finding verdict: **supported with qualification** on missing self-coverage; specific proposed control semantics and its claimed exact mutant differential are not independently verified here.

## Restoration evidence
Scratch archive pristine `SKILL.md` SHA-256 before cleanup: `1b2804fbab784b2c523681259f37d783238f65b2ca21c69b01a5a041bd13155f`, exactly matching `git show HEAD:SKILL.md` SHA-256. Scratch directory `/fast/scratch/hyaku/kotoba-r75/R75Attack54` removed. Lane working-tree `SKILL.md` is user-modified and was not restored or edited; its SHA-256 was `7b1263b5ccbe2ba8b6ffd5d0f4c87ffc5ab3292c9ce792aeee96de283a06464a`.

Trailer path: `.ufo/waves/round-75/w2/R75Attack54.md`
