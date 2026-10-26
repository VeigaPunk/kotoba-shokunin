# R75Facet54 — the `description ≤1024` half of the portability floor is stated on a file it never measures

Seat: R75Facet54 (read-only research). Lane: kotoba-shokunin. Measured tree: `65a5c7a6` (`SKILL.md`
clean; `git diff ec2c1d3 HEAD -- SKILL.md` → empty, so the file is the round-74 tip's bytes).
Scratch: `/fast/scratch/hyaku/kotoba-r75/R75Facet54` (removed at exit). No installs, no network, no
edits to lane files, no commits.

Facet 54 of the bounded question: one **rule** in `SKILL.md` assessed for factual support,
falsifiability, scope and control weakness.

## 1. The rule under test

`SKILL.md:162` (Portability floor, sources S018, S002, S019, S008):

> `` `name` ≤64 lowercase letters, digits and single hyphens, equal to the directory … ;
> `description` ≤1024 chars, no XML tags (Anthropic rule), quoted when it holds `: ` or ` #` ``

The same paragraph names exactly one approximation and its control (`trigger.no_xml_tag`, the XML
half). The two **numeric** bounds in that sentence — `name` ≤64 + charset, `description` ≤1024 —
are stated as binding on this file and have no executed check behind them. That is the facet.

## 2. Observations (measured, not inferred)

| # | observation | command | result |
|---|---|---|---|
| O1 | live description length, YAML-loaded value (the convention the file itself prescribes at `SKILL.md:562-565`) | `python3 -c "import yaml; d=yaml.safe_load(open('SKILL.md').read().split('---')[1])['description']; print(len(d), len(d.encode()), len(d.strip()))"` | `1022` chars, `1026` UTF-8 bytes, `1021` stripped |
| O2 | live description length as the lane's checklist prints it | `python3 -B verifiers/verify_skill_checklist.py --check trigger.frontmatter_parses` | `PASS … description 1021 chars` |
| O3 | that print is the *only* thing the checklist does with the length | `verifiers/verify_skill_checklist.py:1385-1400` | `check_frontmatter` tests non-empty `name:`/`description:` and returns `len(fields["description"].strip())` in the evidence string; no comparison to 1024 |
| O4 | no executed box covers the length | `verifiers/checklist-baseline.json` dispositions | 8 executed boxes: `trigger.01 frontmatter_parses`, `.02 name_directory`, `.03 literal_trigger_string`, `.04 anti_trigger_clause`, `.09 command_binary_resolves`, `.11 citation_resolves`, `.14 line_budget`, `.15 no_placeholder` — none is a length or charset bound |
| O5 | the `name` half is unchecked too | `verifiers/verify_skill_checklist.py:1403-1415` | `check_name_directory` returns PASS iff `name == basename(dirname(skill_path))`; no length, no charset |
| O6 | the 1–1024 rule *is* implemented, but only over other lanes | `verifiers/check_sibling_census.py:418` (`SKILL_DESCRIPTION_MAX = 1024`), `:380-400` (`description_of`), `:502-563` (`skill_description_failures`, G4) | applied to the 20 sibling census lanes' `SKILL.md`; kotoba's own file is not a census row |
| O7 | no other committed gate compares this file's description length | `grep -rn "1024\|len(.*description" verifiers/*.py` | only `check_sibling_census.py` (G4) and `MAX_BYTES = 5*1024*1024` body caps; `verify_harness_independent.py:535` measures the *offered* installed skills' preview cliff, not this file |
| O8 | the file's own line budget still binds and passes | checklist print / `wc -l SKILL.md` | `590` lines, `PASS trigger.line_budget … within budget 600 (from box at line 285)` |
| O9 | description first sentence (supporting the `considerthese` sizing claim) | `re.split(r'(?<=[.!?])\s', …)` on the loaded value | 151 chars; omp's 99-char cut lands mid-word: `…AGENTS.md / dispatch prompts / syste` |

## 3. The control gap, measured

Mutant in the scratch export of the committed tree (`git -C <lane> archive HEAD | tar -x`):
appended `" PROBEWORD0123456789"` (20 chars) inside the description block, then ran the real
committed checker.

| world | `verify_skill_checklist.py --check trigger.frontmatter_parses --check trigger.line_budget --check trigger.no_xml_tag` | `check_sibling_census.skill_description_failures` on the same bytes |
|---|---|---|
| base (`SKILL.md` @ `65a5c7a6`) | `PASS` ×3, `description 1021 chars`, **exit 0** | `length 1021`, no length failure |
| mutant (1 042 loaded / 1 041 printed chars) | `PASS` ×3, `description 1041 chars`, **exit 0** | `FAIL` — `skill description length 1041 is outside 1-1024 characters (S018: …)` |

So the rule at `SKILL.md:162` **cannot fail on the file that states it**: a description 18 chars
over the cap keeps every checklist verdict green. The error message that would fire exists in the
lane, in an instrument the lane never points at its own `SKILL.md`.

The same is true of the name half, measured through the committed function
(`check_name_directory` with a matching directory):

- name `'a'*70` → `('PASS', 1, "name 'aaa…' == directory 'aaa…'")`
- name `'A_b'*10` (uppercase, underscore) → `('PASS', 1, …)`

Both violate `SKILL.md:162`'s `≤64` / `lowercase letters, digits and single hyphens`, and both pass.

## 4. Calibration of the number the round carries

Three conventions exist for the same bytes, and the lane currently reports them as if one:

| convention | value | where it is produced |
|---|---|---|
| YAML-loaded value (trailing newline kept — the convention `SKILL.md:562-565` states: "the description is hashed as the YAML loader yields it (`>`/`|` keep a trailing newline … so a ws-strip-only check under-reports coverage") | **1022** | my PyYAML read (O1) |
| whitespace-stripped print of the checklist (`:1400`) | **1021** | `corpus/lessons/round-74-verifier-spotcheck.md:76` ("1,021 characters (cap 1,024)"); commit `559ee76` subject ("description 1021 characters"); `considerthese/2026-10-26.md:17` ("1,021 of 1,024 chars") |
| collapapsed census helper (`check_sibling_census.description_of`, G4) | **1021** | O6 |

Verdict impact: none today — 1 021 and 1 022 are both under 1 024. Headroom impact: **2 chars under
the convention the file itself prescribes (not 3)**, and 1 026 UTF-8 bytes. Adding a single lane
name to the arbitration clause (~8 chars plus a space) breaches the cap under every convention, with
no lane gate turning red (O3/O4/O7). That is the round-75 exposure: any description edit — e.g. a
new sibling named in the description — is a silent 1024 breach waiting to happen, and the published
headroom figure is one char optimistic.

## 5. In-flight premise check (adjacent, reported not judged)

`corpus/lessons/round-75.md:5` (untracked, this round) states: *"Candidate reject: any claim that the
1021-character description size reported in `considerthese/2026-10-26.md` remains current; current
frontmatter is materially shorter."*

Measured against committed bytes: `git diff ec2c1d3 HEAD -- SKILL.md` is empty and the loaded
description is 1 022 chars (O1). The current frontmatter is **not** materially shorter — it is the
same 1 021/1 022-character description the note says is stale. That candidate reject rests on a
premise the tree contradicts; it must be re-measured (same command as O1) before it freezes, or it
enters the round as a false negative claim.

## 6. Concrete check / control for round 75

Add an **executed** check rather than prose (the box text and the baseline are the contract, `SKILL.md:224-229`):

1. New check id `trigger.description_length` in `verifiers/verify_skill_checklist.py`
   (`CHECK_IDS`, `:327-338`), bound on the **loaded** value via the same YAML load the file
   prescribes, printing both counts:
   `PASS/FAIL trigger.description_length: description loaded N chars (collapsed M), cap 1024 from box at line L`.
   Bound: `1 ≤ loaded ≤ 1024`; `collapsed` is informational so the ±1 divergence in §4 is visible
   instead of silent (QUALITY Q20: name the approximation and carry both directions).
2. New box in § Trigger-fidelity checklist (`SKILL.md`, after `:236`): "`description` is 1–1 024
   characters as the loader yields it, and `name` is ≤64 characters of `[a-z0-9-]` with no leading,
   trailing or doubled hyphen. (executed: `trigger.description_length`)".
3. Self-test arms that must exist (frozen with the counter):
   a. loaded 1 024 → PASS;
   b. loaded 1 025 → FAIL;
   c. `>`-block whose collapsed length is 1 024 and loaded length is 1 025 → FAIL (the ±1 boundary
      the lane's strip convention would miss);
   d. live `SKILL.md` → PASS at 1 022 (pins the current value; a drift past 1 024 turns it red);
   e. the measured mutant above (1 042 loaded) → FAIL — the arm that today flips nothing;
   f. name arms: 65-char name → FAIL, `A_b` → FAIL, `kotoba-shokunin` → PASS.
4. Arithmetic the plan must ledger before the freeze (QUALITY Q65/Q72/Q73):
   `SKILL.md:224` says "Eight of the nineteen boxes are executed" — § Trigger-fidelity checklist
   holds exactly 19 boxes today (`awk` count), so adding one makes it 20 and the sentence must be
   re-derived, not left stale; the file is 590 lines (O8), the new box + prose ≈ +4–6 lines → 594–596
   ≤ 600, so the 600-line cap survives.
   `checklist-baseline.json` must gain the box (text-hash pin) and drop `trigger.01`'s coverage
   claim of being the frontmatter authority only for presence; `verifiers/check_assertion_floors.py`
   needs the new assertion count.
5. Run it where its citations resolve: the fleet-shaped sandbox, never `/tmp` (QUALITY Q63). My
   scratch export reproduced Q63 exactly — `verify_skill_checklist.py` in a non-fleet copy reads
   `FAIL trigger.citation_resolves` / `FAIL governance.citation_resolves` on `../.ufo/...` tokens.

## 7. Risks and limits

- **Two counters, ±1 apart.** If the new check bounds the loaded value (1 022) while census G4 keeps
  its collapsed count (1 021), a file at exactly 1 024 loaded reads PASS from one and FAIL from the
  other. Freeze the bound on the loaded value and say so in both places (Q20).
- **Bytes vs characters.** The value is 1 026 UTF-8 bytes against a 1 024-character cap (two
  em dashes). `[INFERENCE]` no observed source in this lane or its checked clients counts bytes; if
  any validator does, the file is already 2 over. Worth one line in the check's evidence string.
- **Description edits have a second cost.** A changed description misses its omp compressor-cache key
  (`SKILL.md:562-565`), so the skill reverts to the 99-char truncator until a new row lands
  (O9 shows the cut lands mid-word). Any round-75 description edit should be sized against both.
- **Scope of this report.** `considerthese/2026-10-26.md` and `corpus/lessons/round-75.md` are
  read-only inputs; §5 reports their measured premise, it does not fix them. `corpus/lessons/round-75.md`
  is untracked at the time of writing, so its line number is a point-in-time citation.
- No gate run was used as evidence of the lane's health: the only whole-gate runs I made were on a
  scratch export, whose footer reds are the Q63 class and not a lane finding.

## 8. Observation vs inference

| statement | status |
|---|---|
| loaded 1 022 / stripped 1 021 / 1 026 bytes / 590 lines / first sentence 151 chars | observation (O1, O2, O8, O9) |
| checklist has no length bound; census G4 has one, scoped to siblings | observation (O3–O7) |
| a 1 042-char description passes every checklist check | observation (§3 mutant, exit 0) |
| a 70-char and an `A_b` name pass `trigger.name_directory` | observation (§3, committed function) |
| "one added lane name breaches 1 024" | inference from O1 (2-char headroom, ~9 chars per added name) |
| "some client may count bytes and reject 1 026" | `[INFERENCE]` — no source states it |

## 9. Commands run (exact)

```
cd kotoba-shokunin
wc -l SKILL.md                                          → 590
python3 -c "import yaml; d=yaml.safe_load(open('SKILL.md').read().split('---')[1])['description']; print(len(d), len(d.encode()), len(d.strip()))"
                                                        → 1022 1026 1021
git diff ec2c1d3 HEAD -- SKILL.md                       → (empty)
git -C kotoba-shokunin archive HEAD | tar -x -C /fast/scratch/hyaku/kotoba-r75/R75Facet54/full/kotoba-shokunin
cd /fast/scratch/hyaku/kotoba-r75/R75Facet54/full/kotoba-shokunin
python3 -B verifiers/verify_skill_checklist.py --check trigger.frontmatter_parses --check trigger.line_budget --check trigger.no_xml_tag
                                                        → PASS ×3, exit 0 (base)
# mutant: +" PROBEWORD0123456789" in the description block
python3 -B verifiers/verify_skill_checklist.py --check trigger.frontmatter_parses --check trigger.line_budget --check trigger.no_xml_tag
                                                        → PASS ×3, "description 1041 chars", exit 0
python3 - <<'EOF'  # loads verifiers/check_sibling_census.py, calls skill_description_failures / description_of
                                                        → base len 1021 (no failure); mutant len 1041 (length failure)
                     # and verify_skill_checklist.check_name_directory on 70-char and 'A_b' names → PASS, PASS
EOF
cd kotoba-shokunin && python3 -B verifiers/verify_skill_checklist.py --json   → all PASS at the tip
grep -rn "1024\|len(.*description" verifiers/*.py       → G4 only (check_sibling_census.py)
```

Not run: no lane gate as a lane-health verdict, no network, no install, no mutation outside
`/fast/scratch`. Scratch removed on exit.
