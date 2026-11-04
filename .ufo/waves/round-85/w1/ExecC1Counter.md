# ExecC1Counter -- round 85 C1 counter (depth, description render rules)

Seat: ExecC1Counter. Scope: `verifiers/check_description_render.py` and
`verifiers/fixtures/description-render/` (owned). Base: 1c8f37edf2e5ac0fb3c2be1c88e32406313fe47b.
SKILL.md, the production eval TSV and the S213 corpus entry were not touched.

## Status

The counter is authored to the frozen plan section C1 (R1..R8, exact labels and
conditions) and is faithful to the frozen predicate. It is not a claim of 8/8.
The production candidate remains wave-only per the L1's kill-before-data
disposition (KotobaR85). No after-value was scored against the production tree.

## Base measurement (`--rev 1c8f37edf2e5ac0fb3c2be1c88e32406313fe47b`)

    R1 first_sentence_le_99: fail first sentence 151 chars (cap 99)
    R2 prefix_carries_triggers: ok first 99 chars: 'skill' yes, 'prompt' or 'SKILL.md' yes
    R3 spec_max_1024: ok description 1021 chars (1-1024)
    R4 imperative_invocation: fail 'use this skill when' no, literal 'Triggers:' yes
    R5 sibling_clauses: ok census exit 0, 'skill description names 10 of 10 non-none lanes'
    R6 eval_set_shape: fail eval set absent: verifiers/fixtures/description-eval-round85.tsv
    R7 no_xml_tag: ok no '<' or '>'
    R8 sourced_entry: fail absent at rev: corpus/knowledge/description-trigger-discipline-round85.md
    description render rules met 4 of 8
    exit=1

Receipt: `.ufo/waves/round-85/w1/ExecC1Counter/base-receipt.txt`.
Observed deviation from the plan's wording: the plan says the first sentence is
150 characters; the counter measures 151 including the terminal dot (the R1
rule counts the sentence including its dot). R1 is red under either count.

## Self-test

    0 failure(s) over 43 assertions   (exit 0)

Receipt: `.ufo/waves/round-85/w1/ExecC1Counter/self-test.txt`.

The self-test builds throwaway git worlds under TMPDIR (toplevel asserted before
writing), each with the sibling census, PROVINCE.md and the census script copied
from the working tree, and then scores them. It covers:

- Controls: a perfect fixture world (the candidate fixture bytes on every input,
  reads 8 of 8 -- a self-test world, not a production claim); W0 the base commit
  (reads 4 of 8 with R1, R4, R6, R8 red); W1 naive 99-char cut of the base
  description (below 8, R4 red); W2 token dump (below 8, R5 red).
- Red arms, one per rule: R1 first sentence 100 chars; R2 first 99 characters
  free of 'skill' and 'prompt'; R3 description over 1024; R4 'use this skill
  when' removed; R5 sibling clause removed; R6 two should-trigger rows removed
  (7 rows); R7 '<' inserted; R8 recheck line removed.
- Missing eval set (R6 red, 7 of 8); `--eval PATH` supplies R6 when the revision has none.
- Exit ladder: perfect 0, naive cut 1, non-checkout 2, unknown revision 2,
  unreadable `--eval` 2; `--json` emits one object.

## Frozen rules, as implemented

- R1 `first_sentence_le_99`: text up to and including the first `.` followed by
  whitespace or the end, length <= 99.
- R2 `prefix_carries_triggers`: first 99 characters, lower-cased, contain `skill`
  and (`prompt` or `skill.md`).
- R3 `spec_max_1024`: 1 <= length <= 1024.
- R4 `imperative_invocation`: `use this skill when` (case-insensitive) and literal `Triggers:`.
- R5 `sibling_clauses`: census round74 run as a subprocess on the revision's bytes
  (`--province`, `--skill` from the revision); exit 0 and the line
  `skill description names 10 of 10 non-none lanes`.
- R6 `eval_set_shape`: header exactly `label<TAB>query`; 8..10 rows per label;
  >= 5 should-trigger rows containing none of the declared trigger terms; every
  should-not-trigger row shares >= 1 lower-cased alphanumeric word of >= 4 characters
  with the description. Trigger terms: the quoted strings of the `Triggers:` clause.
  Frozen and not strengthened (per KotobaR85).
- R7 `no_xml_tag`: no `<` or `>` in the description (and a non-empty description).
- R8 `sourced_entry`: `source:` naming S213, `verified-at: 2026-11-04`, a
  `recheck:` with a value, and a double-quoted span of 3..25 words.

Parsing: `description_of` mirrors `check_sibling_census.description_of`
(whitespace collapsed first, then the block-scalar indicator dropped, value ends
at any column-0 line).

## Interface

- `--rev` defaults to HEAD. The plan writes the default as `.`; I read that as the
  --repo default (the checkout holding the script) and used HEAD for the revision.
- `--repo DIR` defaults to the lane checkout. `--eval PATH` reads R6 from disk.
- Exit 0 iff N == 8; 1 content; 2 environment or usage.

## Fixtures (test data only)

`verifiers/fixtures/description-render/`:
- `candidate-SKILL.md`: the plan's 876-character candidate description (measured 876).
- `candidate-eval.tsv`: 9 should-trigger and 9 should-not-trigger self-test rows.
- `candidate-knowledge.md`: the R8 shape citing S213's located quote (17 words), a fixture and not the corpus entry.

These fixtures are not the production eval TSV or the corpus entry, and they are
not written to the production paths.

## Tooling and writes

- Stdlib only; Python 3 with `-B`. No package installs.
- Read-only git in the lane (`cat-file`, `show`, `rev-parse`). The self-test runs
  `git init`/`add`/`commit` only inside throwaway temp worlds.
- The only lane writes are: the counter, the fixtures directory, and this wave's receipts.
- Scratch under /fast/scratch/hyaku/kotoba-r85/ExecC1Counter, removed.

## Observations (not claimed, for the L1)

- The counter's R6 is exactly the frozen predicate. Per ReviewerC1-15's oracle
  (duplicate positives and generic-word near-misses reaching 8/8), the predicate
  is gameable; that finding stands as the frozen kill, and the instrument was not strengthened.
- `grep -c $'\r' corpus/SOURCES.md` returns 0 in the working tree. The plan
  says the registry is CRLF; this probe does not confirm that, which matters for
  the census-registry repair (ScribeSources).
- R5 uses the census script's own default fleet root (`/home/vgpnk/Projects/shokunin`)
  and reads sibling repos there; it is environment-dependent by design.
- R8 checks the quote lexically (present, 3..25 words) and does not locate it in a snapshot.

## Checks for the main agent

- `python3 -B verifiers/check_description_render.py --self-test` -> `0 failure(s) over 43 assertions`.
- `python3 -B verifiers/check_description_render.py --rev 1c8f37edf2e5ac0fb3c2be1c88e32406313fe47b` -> `4 of 8`, exit 1.
- sha256 of the counter: `79b8273c5a952a865e5182c4d348f594f6b4881c2221121c8b89eeb47b69957a`.
