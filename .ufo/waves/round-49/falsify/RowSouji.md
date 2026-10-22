# Falsify — C1 census row `souji` and its PROVINCE.md § Adjacent row

HOLDS — applies to the `souji` row in `corpus/knowledge/sibling-overlap-census-round49.md`
(`none`, commit `4edb25dfe262515d0da63224bbba71e02e36cba5`, branch `master`, names kotoba `no`,
arbitration `yes: kagi`, quote at `PROVINCE.md:3`) and to the matching `PROVINCE.md` § Adjacent
row. Every assignment check reproduces; no defect found in the landed bytes. Three minor findings,
none of which moves the row.

## Findings

**F1 (minor — build-seat report accuracy; landed row unaffected).** `CensusSouji.md` §4 cites
"`git grep -n 'souji-landing-gate\.py --root'`, 16 hits, all own lane". At the pin the same
pattern tree-wide matches 82 lines (mostly `.ufo/` wave artifacts and the tool's selftest); across
the scope surfaces SKILL.md + corpus/ it matches 6 (SKILL.md:197 registry template `--root LANE`;
QUALITY.md Q25/Q31 souji's own criteria; round-17.md:52, round-18.md:7,73 — souji's own runs with
`<lane>` notation). "16" is not reproducible as cited. The substantive own-lane conclusion
survives: every operational invocation sampled passes
`--root /home/vgpnk/Projects/shokunin/souji-shokunin`, and souji `PROVINCE.md:95-97` (round 13)
fences evidence-integrity checking to "souji's own receipt/certification fragments". Not a
classification input either way: even a cross-lane pointer-integrity run would not claim kotoba's
craft core.

**F2 (informational — seat ROW line vs landed cell).** `CensusSouji.md`'s ROW line renders
arbitration as "yes (generic integrator clause, no sibling named in it; kagi-shokunin appears only
as an anti-trigger)"; the landed cell is `yes: kagi`. The landed cell is the one the entry's
mechanical rule requires ("which sibling lane names (case-insensitive, whole token) it contains"):
token `kagi` occurs inside `kagi-shokunin` in the frontmatter description (`SKILL.md:2`), the same
hyphenated-name convention as the kotodama row (names-kotoba `yes` from "kotoba-shokunin").
Substantively also correct: souji's description routes credentials to kagi, and `PROVINCE.md:55`
records that split.

**F3 (residual — guard does not re-derive three cells).** `verifiers/check_sibling_census.py`
(`check_census`, lines 329-476) verifies the quote at its pin, commit hex shape, classification
enum, lane-set completeness and the census↔province join; it parses the `branch`, `names kotoba`
and `arbitration` cells but never checks them against sibling bytes. The entry's `recheck:` line
honestly promises only "quote, commit, classification or PROVINCE row", so there is no
overstatement — but those three cells are guard-uncovered fleet-wide. For souji I re-derived all
three by hand (item 4 below); they are correct.

**F4 (trivial — boundary-note abbreviation).** The `PROVINCE.md` § Adjacent souji cell says "fleet
repository hygiene"; souji's own domain is "fleet repository & workspace hygiene (掃除)"
(`PROVINCE.md:3-4`). Abbreviation, not a false statement. The other clause, "no claim on kotoba
ground", is confirmed by the sweep in item 3. The cell cites no line numbers, so no cited-line
check applies.

## Assignment checks

1. **Pin and branch cell.** `git rev-parse master` → `4edb25dfe262515d0da63224bbba71e02e36cba5`
   (exit 0); `rev-parse HEAD` → same; `symbolic-ref -q HEAD` → exit 1 (detached). `master` points
   at the pin, so the `master` cell is right.
2. **Quote.** `git show 4edb25d…:PROVINCE.md` lines 3-4, whitespace-collapsed:
   "**Domain:** fleet repository & workspace hygiene (掃除) — receipt-gated removal of stale,
   duplicate, and already-preserved artifacts." Byte-identical to the census cell after the table's
   mandated wrapping double quotes are stripped (the guard's own `strip_wrapping` rule). Quote
   starts on line 3 (inside ±2), not a heading.
3. **Classification `none` under § Classification rule.** Sweeps at the pin over SKILL.md,
   PROVINCE.md, AGENTS.md, MINT.md, SHONEN.md, corpus/, tools/ (beyond the build seat's four
   top-level docs):
   - `git grep -c -i kotoba <pin> -- <those paths>` → exit 1, 0 hits.
   - `SKILL\.md|AGENTS\.md|frontmatter` hits: all self-referential — souji's own registry rows,
     its own QUALITY criteria, its own knowledge/lesson records, its own tools parsing its own
     SKILL.md. No rule about any other lane's SKILL.md, frontmatter or AGENTS.md class.
   - `\bprompts?\b` hits: souji's own dispatch-integrity records
     (`corpus/lessons/round-1[3-9]*-verifier-spotcheck.md` prompt-fidelity tables of its own
     `.ufo/prompts/souji-round-N.md`), its seat-audit parser over its own wave reports
     (`tools/souji-seat-audit.py`), `MINT.md:16` fleet-root bloat list, and one unrelated rm
     `-I prompts once` source row (corpus/SOURCES.md S024). No claim on prompt wording or craft.
   - Nearest boundaries, all resolving away: `tools/souji-landing-gate.py` reads a SKILL.md only
     for registry-cited-path integrity (LG-MISSING-REG), fenced by `PROVINCE.md:95-97`;
     `tools/souji-seat-audit.py` polices seat write-scopes over `<lane>/SKILL.md` (hygiene, not
     craft); fleet-root round-prompt deletion (MINT demand 1) is receipt-gated artifact lifecycle
     after push, and `PROVINCE.md:42` refuses live lane work products. SKILL.md:341 names `Mori`
     only to disclaim ownership ("outside this tool, not wholesale ownership assigned to Mori"),
     in the body, not the description.
   - Souji's Adjacency (PROVINCE.md:48-56) splits ground only with mori, tsukuroi, kagi — none
     with kotoba. No committed scope surface states a split with kotoba or claims part of kotoba's
     core. `none` stands.
4. **Mechanical columns re-derived** from `git show 4edb25d…:SKILL.md` line 2 — the entire
   frontmatter `description` (frontmatter is lines 1-3; no `name` key). Whole-token,
   case-insensitive scan over all 20 sibling lane names plus `kotoba`:
   exactly one hit — `kagi` (1), inside `kagi-shokunin`; `kotoba` 0. → `no` / `yes: kagi`;
   both match the landed row. Tree-wide SKILL.md scan shows no other sibling token in the
   description.
5. **PROVINCE.md boundary note.** Classification and commit cells match the census row exactly
   (the guard's join inputs); factual clauses checked in F4; no cited lines to verify.

## Evidence (commands and exit codes; all read-only)

- `git -C souji-shokunin rev-parse master` → `4edb25dfe262515d0da63224bbba71e02e36cba5`, exit 0;
  `rev-parse HEAD` → same; `symbolic-ref -q HEAD` → exit 1. `log -1 4edb25d` → 2026-10-21
  18:56:48 -0300, "round-22 verifier spot-check: strict proof unproven, forward policy boundary
  held".
- Token loop over description line 2 (`grep -ciE "(^|[^a-z0-9])T([^a-z0-9]|$)"` for each of the
  21 names) → only "HIT kagi (1)".
- `git grep -c -i kotoba 4edb25d -- SKILL.md PROVINCE.md AGENTS.md MINT.md SHONEN.md corpus tools`
  → exit 1 (0 hits).
- `git grep -iE 'SKILL\.md|AGENTS\.md|frontmatter' 4edb25d -- <same paths>` → exit 0; hits audited
  above, all self-referential. `git grep -iE '\bprompts?\b' …` → exit 0; hits audited above.
- Non-kagi sibling-token scan over SKILL.md → single hit "Mori" at SKILL.md:341 (disclaimer).
- Landing-gate count: pattern tree-wide at pin = 82 lines (grep -cv own-lane-abs-path = 82, exit
  0); over SKILL.md + corpus = 6 lines (SKILL.md 1, QUALITY.md 2, round-17.md 1, round-18.md 2).
- Blob digests at pin (`git show <pin>:<f> | sha256sum`): SKILL.md `dc79dad9…849bd780`,
  PROVINCE.md `3a2364d7…d582bda8` — both match `CensusSouji.md` §6 exactly; `ls-tree --name-only`
  = 17 top-level entries (seat's §1 reproduced). Skill-like files in the tree: top-level
  SKILL.md/PROVINCE.md/AGENTS.md only (plus two `.ufo` wave-report filenames); no
  `skills/<name>/SKILL.md`.
- Judged bytes: working-tree sha256 of `corpus/knowledge/sibling-overlap-census-round49.md`
  (`4ce0a306…`) and `PROVINCE.md` (`9fe4ba1c…`) equal `git show c48793d…:<file>` for both — the
  rows attacked are the judged bytes.
- Quote comparison: census cell vs collapsed `PROVINCE.md:3-4` → identical after stripping the
  cell's wrapping double quotes.
- Guard record at landing ("rows 20 verified 20", lesson `corpus/lessons/round-49.md` § Gate)
  accepted as recorded; not re-run (ground truth, and the three uncovered cells are re-derived
  here instead).

## Residual risk and verification gaps

- souji working tree vs commit blobs not compared (no `git status` by bounds); everything here is
  commit-blob truth at `4edb25d…`, which is what the rows pin.
- Claims living only in souji's `.ufo/`, `results/`, `census/`, `tests/` wave artifacts are
  outside the rule's scope surfaces (census § Limits concedes the same); this seat swept corpus/
  and tools/ in addition to the four top-level docs the build seat used.
- The classification is a judgment call under the entry's rule; the sweep evidence above is the
  whole basis. F1's count inaccuracy shows the seat report's evidence lines can drift from the
  pin; the landed row's own cells do not carry that number.

No tool installs; no writes outside this report file.
