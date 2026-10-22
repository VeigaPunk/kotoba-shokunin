# A27MistakeRows: falsify of round-48 Mistakes rows M24-M27

Seat: KotobaR48.A27MistakeRows (leaf, no delegation). Judged on: freshness.
Lane: kotoba-shokunin, master 84b9c9b (landing). Base 75f671b. C1 887b6af. C2 d1ae458.
Private work: /fast/scratch/hyaku/kotoba-r48-a2/seats2/A27MistakeRows/ (clone `head`; `git archive` trees `base`, `c1`, `c2`; fixture copies; fetched spec and packager).
Tools: none installed or upgraded (python3 3.14.8, PyYAML 6.0.3, curl, git were present).
Lane writes: none. Lane reads: git show/log/grep/diff, one `git status --porcelain` (may refresh the index stat cache; no content change), ls, grep, and three early read-only producer runs in the lane (verify_harness_claims.py has no write calls; grep found none). Other seats' uncommitted files are untouched.

## Verdicts

| Row | Verdict | Severity | Basis |
|---|---|---|---|
| M24 | CONFIRMED evidence and demo; DEFECT in the fix | Medium | Every quoted command reproduces. Live prose still credits the 500-line rule to vendor-only (SOURCES.md:41). Checker detail still labels the lexical check "stricter". |
| M25 | CONFIRMED evidence and demo; DEFECT in the record | Low | Both sweeps reproduce. The entry has no sweep or novelty wording. Line 151 still states the rule values beside the entry. |
| M26 | Mechanism CONFIRMED; cited number REFUTED today; DEFECT | Medium | Producer reads 12, not 11. The 11 is a round-47 value carried forward. The live gap has a second cause the row does not name. |
| M27 | CONFIRMED (demo uses the retained discarded receipt); DEFECT in the gate | Medium | Replay reproduces e3b0c442 with verdict clean. Nothing guards the class, and captured-by is "none" with no Qnn. |

## M24: rule credited to the wrong authority; lexical approximation as vendor rule

Re-run (all exit 0):
- `git show 75f671b:corpus/SOURCES.md | grep -c 'an Anthropic-only rule the open spec lacks'` gives 1.
- `curl -fsSL https://agentskills.io/specification.md | grep -c 'under 500 lines'` gives 1. Accessed 2026-10-22T08:57:11Z; 7,608 bytes; sha256 9a67de89 (matches the entry's pin). Quote at spec.md:237, under "## Progressive disclosure" (:229): "Keep your main `SKILL.md` under 500 lines."
- `git show 75f671b:SKILL.md | grep -c 'is stricter and refuses any'` gives 1.
- Lane checker, `verify_skill_checklist.py --check trigger.no_xml_tag --json`, all 10 C2 fixtures: identical at 75f671b and 84b9c9b. FAIL (exit 1): f01, f03, f08. PASS (exit 0): f02, f02b, f04, f05, f06, f07, f09. f02 and f08 also match at 887b6af and d1ae458.
- Packager (quick_validate.py at dbd4588; fetched 2026-10-22T08:57:10Z; sha256 67cf5703402013936c8fb75ad6a1afecd8841d45cc5e606b634eb05825fde365, equal to C2's recorded pin). NOT executed, because it is fetched code. Its angle predicate (lines 79-81) was replicated with PyYAML safe_load: f02 parses to '<b>' and is refused; f08 parses to '\\u003cb\\u003e' and is accepted. The packager's full PASS on f08 is not re-run; I have not verified the C2 record.
- Q20 shown-able-to-fail: `sed -n 151p` at 75f671b has no "approximat", "lexical", "parsed value", "counterexample" or entry link (count 0). At 84b9c9b the line has all of them (count 1). CONFIRMED, the demo can fail.
- Supersession rows at 84b9c9b: S018 "supersedes S001"; S019 "supersedes S003 - the 500-line body rule is not Anthropic-only: the open spec states it too"; S020 "supersedes S010". CONFIRMED.
- Entry lines 66-70 carry alias, single-quoted and double-quoted run counterexamples. CONFIRMED.

Defects:
- MEDIUM. The class is still live in the same file. corpus/SOURCES.md:41 (the "Paths" prose; pre-existing, base line 35) still says "the vendor-only rules (no XML tags, third person, 500 lines) that the spec does not carry". spec.md:237 contradicts it, and S019's own supersession text says so. This is prose, not a row, so contract rule 2 does not block the fix.
- LOW. verify_skill_checklist.py:1307-1308 still emits "S003 Anthropic rule, absent from the open spec (S001); Anthropic's packager bans any '<'/'>' and is stricter" on every trigger.no_xml_tag result. "Stricter" is a label. The measured direction is mixed: on f02 the packager is stricter; on f08 the lane is stricter. Q20 forbids labels. The row's fix did not touch the checker.

## M25: coverage sweep searched source names, not rule content

Re-run:
- `grep -rn 'agentskills\|skills-ref' corpus/knowledge SKILL.md`: at 75f671b, zero hits in corpus/knowledge and zero in SKILL.md. At 84b9c9b, the only hit file is the new entry; SKILL.md still has zero.
- `grep -n '1024' SKILL.md` gives line 151 at both commits.
- Content terms in SKILL.md at 75f671b: 'XML tags' gives 1; 'refuses any' gives 1.
- C2UncoveredSweep.md exists and reports the same finding. Shown-able-to-fail: source-name sweep 0, content sweep 1, on the same file. CONFIRMED.

Defects:
- LOW. The row says "the entry's novelty claim now rests on both sweeps". The entry contains no "sweep", "novel", "covered" or "already" wording. The two sweeps live only in .ufo/waves/round-48/build/C2UncoveredSweep.md and the lesson.
- LOW. "SKILL.md:151 points to the entry so the fact keeps one home" is not true. Line 151 still states the rule values (name <=64; description <=1024; no XML tags, Anthropic rule; quoting rule), and entry lines 39-45 restate them in a table. Two homes, which is the duplication that C2UncoveredSweep.md finding 2 warned about.

## M26: repair named after the row, not the cause

Confirmed:
- The byte probe is at verify_harness_claims.py:477-479 at both commits. `git diff --stat 75f671b 84b9c9b -- verifiers/verify_harness_claims.py` is empty, so the change does not touch the producer. OC_BIN (line 56) is identical at both.
- Both configured roots are absent: ~/.config/opencode/skill and ~/.config/opencode/skills.
- Instrument (`verify_harness_independent.py --json --catalogue-carrier empty-carrier`, exit 0 each): oc.roots.names_plus_builtin = 10 at 75f671b, d1ae458 and 84b9c9b. "The row reads 10 before and after" holds for the instrument.
- Demo mechanism: producer and instrument disagree, so a "defect 1 repaired" claim fails Q21. True today.

Refuted or defect:
- MEDIUM. "The producer reads 11" is refuted today. verify_harness_claims.py exits 1 at all three commits and prints `oc.roots.names_plus_builtin observed=12 expected=7`. Recomputed: names 11 (10 in ~/.agents/skills, plus kimi-webbridge in ~/.claude/skills, which the producer unions unconditionally at verify_harness_claims.py:472) + builtin 1 (b"customize-opencode" in opencode.exe) = 12.
- The 11 is a round-47 value (C1HarnessDriftRoot.md:63 and :93; W2DepthNoHarm.md:261), carried into round 48 without re-measurement. Q19 forbids that. kimi-webbridge/SKILL.md is dated 2026-10-22T02:36:39Z; the round-47 spot-check commit 197b5a4 is dated 2026-10-21T18:36:33-03:00.
- MEDIUM. The cause set is incomplete. The live gap of 2 = builtin (1) + one name the instrument never counts. The log names only .config/opencode/{skill,skills}, .opencode/{skill,skills} and Projects/opencodeufo/.opencode/{skill,skills} (zero `.claude/skills` in the `sources=` lines), and nothing else reads ~/.claude/skills. C2 adds only configured roots, so this cause is untouched. Q21 requires the row to name both.
- C1JoinDefinitionHistory's "producer 11" is hand arithmetic: `ls ~/.agents/skills | wc -l` (10) plus builtin 1. It omits ~/.claude/skills. The round's seats fetched at 08:13-08:14Z, after kimi-webbridge existed. It was never a producer run.

## M27: instrument self-hash read through process substitution

Re-run:
- The ruler reads `Path(__file__)` for `ruler_sha256` at config-root-ruler.py:312.
- Committed ruler sha256 01af33a6724cb91d at d1ae458 and at 84b9c9b; working file identical.
- Replay A, committed path (`python3 -B c2/.ufo/round-48/tools/config-root-ruler.py --repo head --revision d1ae458 --consumer-sha256 d67b1b6e --oracle c2/.ufo/round-48/oracle/config-root-cases.json --oracle-sha256 1d09a38c --scratch .../m27-committed --baseline-receipt .../before-configured-root.json --baseline-sha256 8bec447a`): exit 0, ruler_sha256 01af33a6, verdict clean, target_failures [].
- Replay B, process substitution (`python3 -B <(git show 84b9c9b:.ufo/round-48/tools/config-root-ruler.py)`, same arguments): exit 0, ruler_sha256 e3b0c44298fc1c14 (sha256 of empty input), verdict clean, evaluation_errors []. The failure reproduces, and it is silent.
- The discarded receipt is retained: /fast/scratch/hyaku/kotoba-r48-a2/ruler-landed-01/receipt.json, ruler_sha256 e3b0c442, verdict clean, recorded 2026-10-22T08:37:46Z. Compared with the committed hash it MISMATCHES. ruler-landed-02/receipt.json (08:38:10Z) carries 01af33a6 and MATCHES. Shown-able-to-fail: CONFIRMED on the real artifact.
- The retained receipt .ufo/round-48/verification/after-configured-root.json carries top-level ruler_sha256 01af33a6724cb91d. LOG.md:2350 records the discarded run.

Defects:
- MEDIUM. Nothing guards the class. The instrument returns verdict "clean" over a wrong custody field, and the fix is a manual re-run. QUALITY.md has no ruler or self-hash criterion (grep for __file__, self-hash, process substitution and ruler returns nothing). captured-by is "none" with no "-> Qnn", which the table legend requires ("none -> Qnn means nothing caught it and this round adds the criterion").
- LOW. The discarded run's argv is not retained (receipts do not record the ruler's argv). "The first run used process substitution" is INFERENCE from the hash signature and LOG.md:2350.

## Adjacent (outside M24-M27, found while checking captured-by pointers)
- QUALITY.md Q22 cites "M28 Hash match read as custody (corpus/lessons/round-48.md, Mistakes)". The lesson has no M28 row (`grep -c M28` gives 0 at 84b9c9b). Dangling pointer. LOW.

## Residual risk and verification gaps
- The packager was not executed (fetched code is outside my bounds). Only its angle predicate was replicated. The full S012 PASS on f08 and the S012 column for the other fixtures are unverified here.
- The discarded run's exact command is inferred, not archived.
- M26's live numbers are host state as of about 08:54Z-09:00Z on 2026-10-22; they move if ~/.claude/skills changes. Any future M26 claim needs a dated measurement, not a carried one.
- 500-line attribution across the tree: considerthese/2026-10-20.md:48 and the entry at line 46 are correct. SOURCES.md:41 is the only wrong attribution found.
- Not checked: producer roots changed after kimi-webbridge beyond today's listing.
