# Round 47 — proposed LOG.md append (reviewer draft, not landed)

Appended at the **tail** of `LOG.md` (append-only; never inserted above the last
line, so no existing line number moves).

The `[fill: …]` markers are substituted by the integrator after the landing
measurement; every marker sits outside a backtick span, so it is never a
citation token.

---

## 2026-10-21 — Round 47 landing (MoriR22R steered round 47): C1 freshness re-pin; C2 operability description-tag rule; C3 calibration erratum registry + corpus index

- Steer and base: the round plan is `plans/round-47.md`; BASE commit `c61a973b2e02e1ded169703ddcb06466f4edd8bd`; the before-measurement summary and its raw outputs are `.ufo/waves/round-47/before/SUMMARY.md` and the sibling files beside it.
- C1 (freshness, lowest non-retired axis): the omp 18.12.5 and opencode 1.19.3 instruction surfaces were re-derived from the frozen dumps and the substrate pins re-cut; before `python3 -B verifiers/check_substrate_pins.py` exited 2 (DRIFT 3/3 — omp sha256 drift, omp mtime drift, opencode binary unreadable) and `python3 -B verifiers/verify_surfaces.py --json` exited 2 (opencode binary not found); after, the same two commands exit 0 at 3/3 pins and 7/7 surface classes. Evidence: `.ufo/waves/round-47/build/C1SurfacesBaselineDiff.json`, `.ufo/waves/round-47/build/C1PinsRepin.md`.
- C2 (operability): `verifiers/verify_skill_checklist.py` gained the `frontmatter.description_no_xml_tag` check and this lane's own description lost its `<skills>` token; before, the frontmatter carried one `<skills>` occurrence and no check existed; after, zero occurrences and the live check passes. The self-test count moved with the new arms and the floor in `verifiers/floors-registry.json` was bumped in the same change [fill: assertion count before -> after]. Evidence: `.ufo/waves/round-47/build/C2CheckImpl.md`, `.ufo/waves/round-47/build/C2SkillRewrite.md`.
- C3 (calibration): `verifiers/citation-errata.json` pins the recorded absence at `LOG.md:2111` by file, line, token and line sha256, and `corpus/README.md` indexes `corpus/lessons/round-46-verifier-spotcheck.md`; before `python3 -B verifiers/verify_skill_checklist.py --json` exited 1 at 9 PASS / 1 FAIL (`governance.citation_resolves`), `python3 -B verifiers/verify_corpus_integrity.py --json` exited 1 (tracked_files 59 != 58, unindexed 1) and `python3 -B verifiers/verify_corpus_independent.py --json` exited 1 (unindexed 1); after, all three exit 0 [fill: checklist 10/10 or 11/11; corpus integrity 0 DRIFT; corpus independent 0 DRIFT]. Evidence: `.ufo/waves/round-47/build/C3ErrataImpl.md`, `.ufo/waves/round-47/build/C3CorpusIndex.md`.
- Not claimed: `verifiers/verify_harness_claims.py` 21/28 at BASE (three host skills without cache rows) stays Q09 debt; the round-46 spot-check residuals (mirror opt-out, missing verdict, NaN/case-variant keys, row `kind`, payload-selectable committed scope-outs, the printed C1 counting command's exit 2) are carried with why-not lines in the wave reports under `.ufo/waves/round-47/build/`.
- Every path token this entry cites resolves at the landing tree, and the entry is appended at the tail of `LOG.md`, so no line above `LOG.md:2111` moves and the erratum entry keyed on that line stays valid.
