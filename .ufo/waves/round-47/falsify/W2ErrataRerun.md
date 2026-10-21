verdict: PARTIAL — the round-47 C3 governance erratum re-runs green and fail-closed at 7ad7fad (PASS, exit 0, 848 evaluated, 9 mutants all red), but the landed LOG record's "governance evaluated 804" is the BASE-population count and is falsified by its own commit's after-battery receipt (848).

Lane: W2ErrataRerun (leaf, no dispatch). Target: `verifiers/verify_skill_checklist.py` → `governance.citation_resolves` at `7ad7fadfc09354b74fb66605dfb0c1182c115a2f` (BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd`). All lane-repo access was read-only; every mutation ran in the canonical-layout scratch clone `/fast/scratch/kotoba-r47/w2/W2ErrataRerun/kotoba-shokunin` (clone of the lane at 7ad7fad, fleet siblings symlinked one level up). Artifacts: `W2ErrataRerun.mut.txt`, `W2ErrataRerun.mut.json`, `W2ErrataRerun.audit.txt`, `W2ErrataRerun.counts.json`, `W2ErrataRerun.commands.txt` (same directory). No tools installed or updated; no pacman transaction; the `~/.local/bin/opencode` wrapper was never executed; no omp session launched.

## F1 — MEDIUM (calibration): the landing record's governance count is stale by 44 inside the commit that records it

`LOG.md:2323` (round-47 landing entry, C3 bullet) ends: "Checklist `--json` exit 1, 9 PASS / 1 FAIL → exit 0, 11/11 (**governance evaluated 804**, 1 recorded absence excused)". At the landing commit the live value is **848**, and the *same commit* ships the receipt that says so: `.ufo/waves/round-47/after/verify_skill_checklist.json:64` → `"848 governance citation token(s) resolve across 2 files; 9 quoted meta-finding(s), 3 schematic token(s) excluded, 1 recorded absence(s) excused"`.

Re-run (lane repo, read-only), exit 0:

```
$ python3 -B verifiers/verify_skill_checklist.py --json --check governance.citation_resolves
{"checks":[{"detail":"848 governance citation token(s) resolve across 2 files; 9 quoted meta-finding(s), 3 schematic token(s) excluded, 1 recorded absence(s) excused","evaluated":848,"id":"governance.citation_resolves","status":"PASS"}],"exit_code":0,"fail":0,"na":0,"pass":1}
```

Repro of the *number* (why 804 and 848 differ) — scratch clone, each step restored:

```
cd /fast/scratch/kotoba-r47/w2/W2ErrataRerun/kotoba-shokunin
git show c61a973:LOG.md > /tmp/base_LOG.md ; git show c61a973:SCORECARD.md > /tmp/base_SCORE.md
cp LOG.md /tmp/tip_LOG.md ; cp SCORECARD.md /tmp/tip_SCORE.md
head -n 2315 /tmp/tip_LOG.md > LOG.md            # drop the landing entry only
python3 -B verifiers/verify_skill_checklist.py --json --check governance.citation_resolves   # -> 815
cp /tmp/base_LOG.md LOG.md ; cp /tmp/base_SCORE.md SCORECARD.md
python3 -B verifiers/verify_skill_checklist.py --json --check governance.citation_resolves   # -> 804   <-- LOG.md:2323
cp /tmp/tip_LOG.md LOG.md ; cp /tmp/tip_SCORE.md SCORECARD.md
python3 -B verifiers/verify_skill_checklist.py --json --check governance.citation_resolves   # -> 848   <-- 7ad7fad
```

Population reconciliation (exact, independently re-derived): BASE population 817 = 9 quoted + 3 schematic + 805 checked (−1 excused = **804** evaluated); TIP population 861 = 9 quoted + 3 schematic + 849 checked (−1 excused = **848** evaluated). The +44 are the landing entry's own 33 new `LOG.md:2316-2326` subjects plus 11 new `SCORECARD.md` subjects — all live, none dead, none newly excluded. So 804 is the count C3 measured against the *BASE governance prefix* (`.ufo/waves/round-47/build/C3CriticDesign.md:119` and `.ufo/waves/round-47/build/C3SentinelErrata.md:37` both scope 804 to BASE); the landing entry transplanted that pre-append number into a tip-scoped sentence, and the landing entry's own citations invalidated it.

Impact: the gate is green and correct, but the C3 record — the calibration record — states a number that no re-run at its own commit reproduces, and the same commit's receipt contradicts it. The assignment's stated expectation ("PASS evaluated 804") is therefore not reproducible at the tip either. This is the repo's own named debt class ("LOG records falsified at their own commits", `LOG.md:1213`). Correction is the integrator's to make (state the after-receipt's 848, or scope the number to the BASE prefix); I did not edit any production file.

Note: `SCORECARD.md:33` (round-47 calibration cell) and `SCORECARD.md:106-108` contain **no** count, so the stale number lives only in `LOG.md:2323`. `grep -rn "804" LOG.md SCORECARD.md PROVINCE.md plans/round-47.md corpus/` finds no other governance-count use.

## F2 — INFO (holds): the erratum is load-bearing and fails closed under 9 mutants

Harness `W2ErrataRerun.mut.txt`, raw results `W2ErrataRerun.mut.json` (scratch clone, verifier restored between arms):

| mutant | exit | observed reason |
|---|---|---|
| BASELINE (unmutated) | 0 | PASS, 848 evaluated, 1 excused |
| M1 `GOVERNANCE_ERRATA_HORIZON = 2315` → `2110` | 1 | "erratum LOG.md:2111 … is past horizon 2110 or absent" |
| M2 pinned line sha256 falsified | 1 | "line text drifted" |
| M3 pinned absence wording falsified | 1 | "absence wording not on the line" |
| M4 pinned line 2111 → 2112 | 1 | "line text drifted" |
| M5 pinned token → `corpus/nope.md` | 1 | "names no subject on the line" |
| M6 row removed (`GOVERNANCE_ERRATA = ()`) | 1 | "LOG.md:2111: '.ufo/round-45/drafts/v10/post-r44-hunt.py' does not resolve" |
| M7 the excused path created on disk | 1 | "stale, the path now resolves" |
| M8 one LOG line inserted above 2111 | 1 | "line text drifted" + "LOG.md:2112 … does not resolve" |
| M9 `LOG.md:2111` text edited (1 word) | 1 | "line text drifted" |

Anchors: `verifiers/verify_skill_checklist.py:377` (horizon 2315), `:378-383` (`GOVERNANCE_ERRATA` row: line 2111, digest `7dcbf123…0135`, token `.ufo/round-45/drafts/v10/post-r44-hunt.py`, wording "each exited 2 because the referenced runners are absent"), `:1519` (`errata_problems`), `:1545` (`check_governance_citations`). The row's digest reproduces: `sha256(LOG.md line 2111)` = `7dcbf123313d46c469cab9f5dac2daa7567e54ac1ddf7cffdd1fd38c74200135` (sha256 of the line *without* the trailing newline; `sed -n '2111p' LOG.md | sha256sum` differs by that newline and is not the pinned form). The excused path is genuinely absent from HEAD (`git ls-tree -r HEAD --name-only | grep round-45/drafts` → only `drafts-report-skeleton.md`) and from the worktree. Every row field is load-bearing; none is a rubber stamp.

## F3 — INFO (holds): the new LOG/SCORECARD text adds no dead citation and hides nothing

Independent audit (`W2ErrataRerun.audit.txt`) re-implements the documented subject rule (`verifiers/verify_skill_checklist.py:187-197`) *without importing the verifier*, over the `c61a973 → 7ad7fad` diff, line-attributed with `difflib`:

- `LOG.md:2316-2326` (11 new lines): 33 new subjects, **0 dead**, 0 same-line-quoted, 0 schematic/ellipsis.
- `SCORECARD.md` (3 replaced + 4 added lines): 11 new subjects (multiplicity), **0 dead**, 0 quoted, 0 schematic.
- The independent population (861) equals the verifier's (848 + 9 + 3 + 1) exactly — the tool's arithmetic and its subject extraction agree with a second implementation.
- Exclusion identity is unchanged base→tip: the same 9 quoted rows (`LOG.md:462,722,757,769,834,843,1130,1282`, `SCORECARD.md:118→122`) and the same 3 schematic rows (`LOG.md:280,370`, `SCORECARD.md:129→133`). The landing text adds **no** new exclusion — the 804→848 delta is entirely 44 newly live citations, not newly hidden ones.
- Trackedness: every new `.ufo/`/`corpus/`/`verifiers/` token cited by `LOG.md:2316-2326` is present in `git ls-files` at 7ad7fad, so the new text does not depend on untracked worktree files. This closes the design's own disclosure risk (`.ufo/waves/round-47/build/C3CriticDesign.md`, "Whether round-47 LOG appends that cite untracked `.ufo/waves/round-47/…` would die in a clean canonical clone") — it does not materialize: the clean scratch clone reproduces 848.

## F4 — LOW (scope note): the C3 design's own falsification criterion is not literally reusable at the tip

`.ufo/waves/round-47/build/C3CriticDesign.md:119` states the after-target as "PASS, evaluated **exactly 804** … C3 is falsified if evaluated is below 804, or if the quoted or schematic counts over the BASE prefix change", and `:75,95,97,98` tabulate "PASS, 804" for the C3-only / C2+C3 / C3+C2 trees — all measured on the BASE governance prefix. At the tip the value is 848, i.e. above 804, so the criterion's literal falsification condition does not fire; but any future round that reuses "804" as an expected literal will report a false drift. The criterion needs a population anchor (subject population, or "≥ the BASE-prefix value"), not a live count. Not a defect in the landed gate.

## Confirmations that survive the attack

- `python3 -B verifiers/verify_skill_checklist.py --json --check governance.citation_resolves` → **exit 0**, PASS, evaluated 848, "9 quoted … 3 schematic … 1 recorded absence(s) excused" — in the lane repo **and** in a clean canonical-layout clone at 7ad7fad (location-independent).
- Whole checklist → exit 0, 11 PASS / 0 FAIL, per-check-id identical to `.ufo/waves/round-47/after/verify_skill_checklist.json` (zero DIFF rows) — the landing receipt is reproducible.
- `python3 -B verifiers/verify_skill_checklist.py --self-test` → exit 0, "0 failure(s) over 1845 assertions" (matches the LOG claim 1597 → 1845).
- `git show c61a973:LOG.md | cmp - <(head -n 2315 LOG.md)` → **exit 0**; `git diff c61a973 -- LOG.md | grep -c '^-[^-]'` → **0** (append-only prefix intact; `LOG.md` is 2326 lines at the tip).
- `python3 -B verifiers/verify_corpus_integrity.py --json` → exit 0; `python3 -B verifiers/verify_corpus_independent.py --json` → exit 0 (C3's corpus-index half at the exit-code level).
- The gate is a genuine improvement over BASE, not a weakening: at BASE the same check FAILs on the one dead subject (`LOG.md:2111`), and under BASE the in-place launderings the design names (de-rooting, quote-wrapping, ellipsis-swapping on that line) pass; under the landed erratum every one of them FAILs (M2/M3/M8/M9 above, plus M1/M4/M5/M6/M7).

## Residual risk

1. The erratum is a *reviewed exception, not an authentication* (stated in the verifier's own docstring, `verifiers/verify_skill_checklist.py:234-238`, and in `C3CriticDesign.md`). An author who edits `LOG.md:2111` **and** the row's digest/wording/token in one reviewed verifier diff can excuse a new dead token; the still-dead test (M7) bounds the exemption to a genuinely absent path, and the "still dead" + line-hash pair is what makes it fail closed.
2. The absence-wording test is a substring test (`quote not in text`, `:1519`): a line that retains the phrase while inverting the claim stays excused. Bounded by the still-dead test, but the wording is a reader affordance, not a proof.
3. Systemic: a live count quoted inside an append-only record goes stale as soon as that record's own text adds citations — exactly F1. Any future landing entry that inlines a live gate count will reproduce this; the durable form is to cite the after-battery JSON (`.ufo/waves/round-47/after/verify_skill_checklist.json:64`) instead of the number.
4. Scope coupling: `GOVERNANCE_ERRATA_HORIZON = 2315` is a hard-coded constant tied to the current `LOG.md` length; it only works because LOG is append-only. M8 shows the mechanism fails closed if that convention is ever broken — but a future non-append edit above line 2111 turns the gate red, not silently green.

## What I did NOT check

- The other two C3 halves beyond their exit codes: `corpus/README.md` indexing of `corpus/lessons/round-46-verifier-spotcheck.md` and `corpus/lessons/round-47.md`, and `verifiers/corpus-baseline.json` tracked_files 58 → 60 (I confirmed integrity/independent exit 0; I did not re-derive the 58/59/60 arithmetic or the README rows).
- C1 (omp 18.12.5 / opencode 1.19.3 re-derivation and re-pinning) and C2 (`trigger.no_xml_tag`) — other lanes' scope; the only thing I verified is that the whole checklist (which contains C2's check) is 11/11 green at the tip.
- Each of the 9 quoted and 3 schematic exclusions for substantive legitimacy: I compared exclusion *identities* base↔tip (identical) and proved the landing text adds none, but I did not re-adjudicate whether the 12 pre-existing exclusions are each honest.
- The `../` fleet-hop resolution semantics of pre-existing subjects (the new text contains no `../` token — `grep -c '`\.\./' LOG.md:2316-2326` → 0).
- `verifiers/verify_harness_claims.py` (21/28, explicitly not claimed by the landing entry) and the frontier corpus rows S012–S015 / M20–M22 / Q19.
- Non-canonical clone layouts (the design notes a plain clone yields artifact counts, 7/3); all my runs used the canonical-layout clone or the production lane.
- I did not read the sibling lane's `W2ErrataLaunder.md` report; my mutation arms were derived independently from the verifier source, and there is overlap (drop-horizon / drop-sha / still-dead / line-shift / quote-wrap / de-root / ellipsis) between the two lanes' arms.

## Overlap note

A sibling lane (`W2ErrataLaunder`) is attacking the same erratum's laundering vectors. My arms are listed in F2 with their reasons; the erratum was not mutated in the lane repo, and my mutants ran only in the scratch clone, so the two lanes do not interfere.
