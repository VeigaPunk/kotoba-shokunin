# RevenGovRule — round 70 w1 — `governance.citation_resolves` vs the K69-11 notices (LOG.md:2723-2724)

Seat: revenger (read-only). Rev measured: lane `HEAD` = `16b212a390c7ce68b6bce49b2c3766b154fbcbae`; base `7d51253f99906b8551b6a0a108761eedac00de74`.
Scratch: `/tmp/k70w1-RevenGovRule.deUQ` (a `git clone --shared` sandbox plus two probe scripts). It is deleted, and no lane file other than this report was written.
Tool installs: none. LSP: none was used, because this is a single-file Python reconstruction; the code paths were read directly at the cited line numbers and confirmed by importing and executing the module's own functions.

## Verdict

1. **Q1 (stale tokens excluded as same-line double-quoted meta-findings?): no — the premise is false.** The tokens on LOG.md:2723-2724 are never subjects at all. They sit in plain double quotes with **no backtick span** on either line, and the scanner only reads backtick spans. They are therefore outside the scanner's domain, not counted as quoted exclusions. The quoted-meta count is 10 at the base and 10 at HEAD, so the notices add nothing to it.
2. **Q2 (corrected tokens checked?): only by the row validator, and only for existence.** `correction_problems` runs `citation_resolve(corrected)` on the pinned row's corrected token (verify_skill_checklist.py:1738). The scanner never checks the corrected token as a subject. Nothing ties the corrected token to the stale artefact: substituting any existing file still excuses LOG.md:2678 (mutation below).
3. **Q3 (is LOG.md:2678 → `corpus/lessons/round-68.md` within GOVERNANCE_CORRECTIONS' round-65 intent?): no. It launders an absence through the correction shape.** Row 2723 (census receipt → its real location) is in intent. Row 2724 is not:
   - The junk-world directory exists nowhere.
   - `corpus/lessons/round-68.md` is a record of its removal, not its corrected address.
   - Round 65 built CORRECTIONS explicitly as a *separate class* from recorded absence.

   However, GOVERNANCE_ERRATA **as written cannot carry it either**. LOG.md:2678 is past the errata horizon of 2315, and it carries no absence wording on its own line. The honest owner of this subject is an explicit, reviewed extension of errata, or the subject stays red. Disclosure is honest: notice 2724's prose says the mirror "was removed … and never tracked". So this is mechanism misuse, not concealment.

Confidence: high on Q1 and Q2 (executed). Q3 rests on documented intent: high that row 2724 departs from the round-65 intent. The remedy choice is `[INFERENCE]`.

## Reconstructed contract (governance.citation_resolves)

- **Subject extraction.** Only words inside backtick spans are candidates: `INLINE_SPAN_RE = re.compile(r"`([^`\n]+)`")` (verify_skill_checklist.py:350), iterated at :1620-1624. A word must start with `CITATION_ROOTS` (:393, :1639).
- **Quoted exclusion.** It applies only to a backtick-span word that sits inside an unescaped double-quote run opened before it and closed on the same line (:1626-1630, :1647-1649; quote state at :1549-1562). It never applies to text outside backticks.
- **Errata (recorded absence).** A pinned errata row needs:
  - the line at or below `GOVERNANCE_ERRATA_HORIZON = 2315` (:400, :1691);
  - a matching SHA-256 (:1695);
  - the absence wording `quote` on *that* line (:1697);
  - a subject on that line (:1699);
  - a path that is still dead (:1701).

  The docstring scope is "lines that record a cited path's absence but predate the same-line quote convention" (:396-399, :202-205).
- **Corrections (round 65).** A pinned correction row needs:
  - a horizon of `GOVERNANCE_CORRECTIONS_HORIZON = 2724` (:415, :1726);
  - a matching SHA-256 (:1730);
  - stale and corrected substrings both on the notice line (:1732);
  - the subject live (:1734) and still red (:1736);
  - a corrected token that resolves (:1738).

  Corrections are applied after errata (:1781-1789).
- **Everything else** must resolve at HEAD, and evaluated == 0 is a FAIL (:1799-1806).

## Evidence chain

**E1 — the notice lines carry no backtick span; the tokens are double-quoted only.**
`sed -n '2723,2724p' LOG.md` shows:
`  - LOG.md:2676 token ".ufo/waves/round-67/w1/controls/census-validate-append.txt" -> ".ufo/waves/round-67/controls/census-validate-append.txt" (…)`
`  - LOG.md:2678 token ".ufo/waves/round-67/w1/controls/junk-world/" -> "corpus/lessons/round-68.md" (…)`
In the probe (the module imported and `citation_subjects(..., exclude_quoted=True, exclude_schematic=True)` run on lane LOG.md):
```
line 2676 subjects: ['.ufo/waves/round-67/w1/controls/census-validate-append.txt'] quoted-excl: [] schem-excl: []
line 2678 subjects: ['.ufo/waves/round-67/w1/controls/junk-world/'] quoted-excl: [] schem-excl: []
line 2723 subjects: [] quoted-excl: [] schem-excl: []
line 2724 subjects: [] quoted-excl: [] schem-excl: []
INLINE spans on 2723/2724: [[], []]
```
At base `7d51253` (sandbox checkout) the probe printed `base quoted-excluded 10 LOG lines 2696 horizon 2621`. At HEAD the check prints `10 quoted meta-finding(s)`. The count is unchanged, so the notices are not quoted exclusions.

This form is deliberate. Round-65 lesson M100 (corpus/lessons/round-65.md:63-72) records that backticked notices "became a new dead subject", and the fix was to "quote the tokens in double quotes (not a scanned span)". The verifier docstring at :199-200 ("A token fully enclosed by double quotes on its own line is a historical/meta finding") describes the *backtick-inside-quotes* exclusion, which these lines do not use. Calling these tokens "excluded as same-line double-quoted meta-findings" mislabels the mechanism.

**E2 — the live gate PASSes only through the two new rows.** Lane HEAD, read-only:
```
live: ('PASS', 1253, '… 10 quoted meta-finding(s), 3 schematic token(s) excluded, 1 recorded absence(s) excused, 5 recorded correction(s) excused')
no-corrections: ('FAIL', 1258, "LOG.md:2533 … LOG.md:2580 … LOG.md:2676 … LOG.md:2678 … (+1 more) …")
minus-2724-row: ('FAIL', 1254, "LOG.md:2678: '.ufo/waves/round-67/w1/controls/junk-world/' does not resolve …; … 4 recorded correction(s) excused")
```
Row 2724 alone turns the check from FAIL to PASS.

**E3 — the corrected token is checked only for existence; any existing file excuses the subject.** In the sandbox, `correction_problems` was called with row 2724, the notice line rewritten, and the SHA re-pinned:
```
live 2724 row: ([], {('LOG.md', 2678, '.ufo/waves/round-67/w1/controls/junk-world/')})
mutant corrected=corpus/SOURCES.md: ([], {('LOG.md', 2678, '.ufo/waves/round-67/w1/controls/junk-world/')})
mutant corrected=verifiers/verify_skill_checklist.py: ([], {('LOG.md', 2678, '.ufo/waves/round-67/w1/controls/junk-world/')})
```
No problems are raised and the subject is excused in every case. The guard (:1738) cannot tell "the same artefact at its real address" from "an unrelated existing file". The self-test's only corrected-token arm is "corrected token dead" (:2484), so this gap has no arm.

**E4 — the path facts.** `ls -d .ufo/waves/round-67/w1/controls/junk-world …` → `No such file or directory`. `git ls-tree -r --name-only HEAD -- .ufo/waves/round-67/ | grep -c junk-world` → `0`. The probe gives `resolve corpus/lessons/round-68.md True` and `resolve .ufo/waves/round-67/controls/census-validate-append.txt True`.

The round-68 lesson M109 (corpus/lessons/round-68.md:154-159) says the mirror was removed: "removes it from the working tree; it was control scratch". So the junk-world subject is an **absence**: the artefact has no corrected location. Row 2723's corrected token is the same file at its real location, which is a genuine correction.

**E5 — the round-65 intent of GOVERNANCE_CORRECTIONS is re-addressing, distinct from absence.**
- verify_skill_checklist.py:407-411: "A stale citation cell … is fixed by an appended LOG.md notice … names the subject … and its **replacement**, and the replacement must resolve."
- plans/round-65.md:85-91: "a recorded-correction excusal **beside** GOVERNANCE_ERRATA … the three red cells are corrected by appended LOG.md notices **rewriting the tokens to the lane's documented fleet convention `../.ufo/…`**". That is the same artefact, a different base.
- corpus/lessons/round-65.md:100-102: "the checker's own `GOVERNANCE_ERRATA` precedent … **extended from recorded-absence to recorded-correction**". Correction is defined as the class that is *not* absence.
- The three original round-65 notices (commit `80bb892`, `git show 80bb892 -- LOG.md`) all map a token to the same file under `../`.

Row 2724 maps a removed directory to a lesson that *records the removal*. That is a recorded absence in correction form. → **Divergence D1.**

**E6 — GOVERNANCE_ERRATA, as written, cannot carry LOG.md:2678 either.** Sandbox probe:
```
errata horizon 2315 line 2678 <= horizon: False
wording 'removes it from the working tree' on 2678: False
wording '254 MB' on 2678: True
errata row as-is: (["erratum LOG.md:2678 '…junk-world/' is past horizon 2315 or absent"], set())
errata row horizon 2724: ([], {(2678, '.ufo/waves/round-67/w1/controls/junk-world/')})
```
- Errata are scoped to lines that "predate the same-line quote convention" (:396-397). LOG.md:2678 was written in round 68 (commit `605b84b`), long after that convention.
- The line's absence wording ("removes it from the working tree") sits on LOG.md:2681-2682, not on 2678. A row would have to pin non-absence text such as "254 MB" to pass. That would launder errata the same way: the guard checks only that the substring is present (:1697).

The root cause is a round-68 authoring defect: a disclosure line cited a deliberately removed path in a live backtick span instead of the same-line `"`…`"` meta form. LOG.md is append-only, so the line cannot be re-quoted.

## Divergences

- **D1 (intent).** Row 2724 (verify_skill_checklist.py:434-437) uses the CORRECTIONS mechanism for a subject with no corrected location. This departs from the round-65 contract (E5). The docstring at :206-211 is not updated to admit "pointer to the record of an absence" as a correction.
- **D2 (instrument gap).** The corrected-token guard is existence-only (E3). Any existing repo-rooted path launders any red subject that has a pinned notice. No self-test arm covers an unrelated corrected token.
- **D3 (labeling).** Describing the 2723-2724 tokens as "same-line double-quoted meta-findings" is wrong. They are unscanned plain-quote text (E1), and the quoted-exclusion count does not move.
- **No divergence on row 2723.** The census receipt is the same file at its real path. Note: the R67-2 erratum on LOG.md:2675-2677 already named that path in a backtick span (2677), and it resolves.

## Remedy options (`[INFERENCE]` — not judged here)

1. Add an explicit, documented errata extension for post-convention disclosure lines, where the absence wording may sit within the same bullet. This needs a docstring and plan change, plus its own fail-closed arms.
2. Leave LOG.md:2678 red and record it as an inherited miss.

Either way, row 2724 as a "correction" should not stand under the round-65 contract.
