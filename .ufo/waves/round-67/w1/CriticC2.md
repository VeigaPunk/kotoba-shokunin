# Critic C2 — cheap worlds that satisfy the frozen predicate

## Scope and measurement identity

Axes attacked: **depth** (whether any authority-ladder knowledge or new ground exists),
**consistency** (source/date/back-link/index coherence), and the **calibration** sub-axis
(whether the counter and its base control discriminate honest bytes from junk).

Measured revision: pinned base `2a8eba56b3f9321b70c569fa2816d42237ca49a2` (also the observed
`HEAD`). No candidate commit or temporary sandbox was measured. During this review neither
`verifiers/check_instruction_authority.py` nor
`.ufo/waves/round-67/w1/drafts/check_instruction_authority.py` existed. Therefore the green
lines below are **predictions from the seven frozen conjuncts**, not fabricated executions of an
unavailable counter. The implementation-dependent rows say so separately.

The literal base command was run from the lane root:

```text
$ python3 -B verifiers/check_instruction_authority.py --rev 2a8eba56b3f9321b70c569fa2816d42237ca49a2
python3: can't open file '/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_instruction_authority.py': [Errno 2] No such file or directory
exit=2
```

It printed no `authority ladder grounded 0 of 1`. A base receipt therefore has to invoke the
**candidate instrument** with `--rev 2a8eba56…`; merely running the literal command in a base
checkout does not satisfy the printed-line half of the control.

`git cat-file -e 2a8eba56…:corpus/knowledge/instruction-authority-ladder-round67.md` exited 128
and reported that the path exists on disk but is absent from that committed revision. Thus a content-reading candidate counter can get the
base to zero through target-path absence alone; that says nothing about equivalent content held
under another base path.

## Strongest cheap world: no new source row and no ladder content

The base already contains S004 (`corpus/SOURCES.md:17`, confirmed with `git show` at the full base
SHA): status `mined`, URL `https://agents.md/`, anchor containing the four-word quote
`"What if instructions conflict?"`, opened `2026-10-19`, and used by
`corpus/knowledge/alwayson-rule-files-round53.md`, not the round-67 target.

Construct a candidate containing only the target below (with the per-id quote represented in
whatever syntax the eventual counter chooses), an exact File-cell row for it in README's
`## Coverage map`, and **no SOURCES change**:

```markdown
source: S004 — https://agents.md/ — § FAQ
verified-at: 2026-10-24
recheck: whenever convenient

# This is not an instruction-authority ladder

## Located quotation
| id | quote | location |
|---|---|---|
| S004 | "What if instructions conflict?" | § FAQ |
```

This meets all seven frozen tests: target exists; opening source line has an id; that id is mined;
its row URL occurs verbatim; both metadata lines exist; the located quote is at most 25 words and
occurs in S004's anchor; and the target is indexed. **Expected output:
`authority ladder grounded 1 of 1`, exit 0.** The same candidate can have an empty or copied body.
It has no authority-ladder content, no source opened this round, no source-row back-link, and no
valid recheck cadence. This one world directly falsifies the inference from the frozen output to
“instruction-authority ladder, sourced” or to new depth.

The plan also under-specifies the machine grammar that associates a quote with an id. The grammar
must be frozen (for example, exactly one `| S### | "quote" | location |` row per opening source id);
otherwise an implementation and an honest entry can choose different syntax, and a loose
implementation can associate a quote with the wrong source.

## A. Green worlds permitted by the frozen seven conjuncts

Every row in this table has the same expected result at the candidate:
`authority ladder grounded 1 of 1`, exit 0. With the target absent at the base, the base half can
also print `authority ladder grounded 0 of 1` and exit nonzero. These are distinct single-defect
variants; fixing only the combined S004 example does not close the other rows.

| id | cheap world | why it passes / smallest safe correction that must be added |
|---|---|---|
| A1 | **Renamed admitted entry.** Copy an existing admitted knowledge body to the target. If necessary, replace only its provenance header with a conforming current-date header and add the coverage row. | Nothing compares the body with base knowledge or requires any ladder proposition. Add a normalized-body comparison against all base knowledge blobs (excluding only the provenance header), plus the structured ladder-content check in A2. A whole-file hash alone is insufficient because changing the date evades it. |
| A2 | **Empty or unrelated stub.** Use the S004 construction above, or cite any other row whose topic does not support the body. | The counter reads metadata, not the claimed thing. Add a required, located ladder record: the authority levels in their stated order, the override relation, and the skill-body boundary, each bound to its source id and located quote. Also require non-author semantic review for relevance and prose truth; a keyword list is only another cheap token target, not a depth proof. |
| A3 | **Old source sold as re-opened this round.** S004 has `opened 2026-10-19`; every other structural field can be mirrored correctly. | Conjunct 3 checks only `mined`, and conjunct 5 checks only the entry's self-declared date. For every cited row require `opened == 2026-10-24` and the current-round access evidence; if an old row is deliberately revalidated, require a current-round `## Gate` re-open record instead. `verified-at:` alone cannot establish access. |
| A4 | **Copied placeholder quote.** Copy the quote out of the cited row's anchor and write `verified-at: 2026-10-24` without opening any page. | Conjunct 6 compares two lane-authored strings only. Require the exact same quote in the current-round lesson `## Gate` and in a committed current-round source snapshot whose hash and locator are checked; optionally add a live-fetch witness. Q51 forbids presenting an unsnapshotted live fetch alone as page evidence. |
| A5 | **Wrong or absent `used-by` back-link.** S004 names the always-on entry, not this target; a newly minted row can likewise say `used-by: —` while claiming `mined`. | The `used-by` cell is unread. Require every cited row's parsed `used-by` list to contain exactly the repo-relative target path among its actual citing entries, and reject `mined` with `—`. Keep this consistent with the append-only/status-change receipt. |
| A6 | **Fully fabricated source/entry mirror.** Add a new row with an arbitrary URL, `status mined`, current `opened`, target `used-by`, and an invented anchor quote; copy those values into the target. | Even adding date, tier, and back-link checks does not establish that an external source exists. Require fetched source bytes, a content hash, an exact located-quote match at the declared source location, and named non-author re-opening. Otherwise `grounded` remains a self-consistency assertion, not provenance. |
| A7 | **Empty or fragment quote.** Use a one-word fragment such as `"Instructions"`, or the empty string if the extractor permits it, provided it is a substring of the anchor. | “Occurs in the anchor” plus “at most 25 words” accepts fragments and possibly zero words. Extract each complete quote recorded in the anchor and require non-empty **exact equality**, not substring containment. Q32 specifically requires this and a must-fail fragment arm. |
| A8 | **URL containment rather than source identity.** Put `https://model-spec.openai.com/2026-08-18` inside `https://evil.invalid/?next=<that URL>`, or use a path-extended lookalike. The registry URL still occurs verbatim. | Parse the entry's actual URL and require canonical equality with the row's declared source URL (with any explicitly allowed `.md`/redirect aliases normalized); never use substring containment. Add evil-query, suffix-path, and sibling-host arms. If fetching, validate redirect targets too. |
| A9 | **Sentence or empty recheck.** `recheck: whenever convenient` satisfies the only frozen requirement: a line exists. | Require a non-empty valid ISO date/cadence (`NNd` or the allowed symbolic cadence) and, for Q12's knowledge-entry requirement, a resolvable runnable recheck command executed fail-closed with a timeout. A cadence regex alone fixes only the sentence variant, not Q12's “that runs.” |
| A10 | **Inadmissible authority tier.** Mint or cite a `community` / tier-C row, mark it `mined`, and mirror its anchor. | Only `status` is checked. Enforce strict 11-cell registry rows, allowed `kind`/`tier`, and the corpus rule that tier C/community cannot be the sole support for an admitted entry. S129 shows that tier B must remain possible; this is not an A-only correction. |
| A11 | **One good citation launders unsupported prose.** Keep one fully valid S123 citation, then add fabricated authority rules, a claim about another client, or body references to S125/S129 without opening provenance. | The seven checks do not measure claim-by-claim support or Q23's other-authority sweep. Require every authority-attributed rule to carry its located quote and sweep, resolve every S### reference in the body as well as the header, and assign uncited prose to named non-author review. Otherwise bound the headline to citation shape. |
| A12 | **Held knowledge renamed as “new ground.”** The base can already contain the same ladder under another filename; target-path absence still yields the required base zero. | Compare the claimed normalized ladder propositions/forms against the whole base tree outside `.ufo/`, as Q38 requires for new-ground claims, or narrow the claim to “a file was added at this path.” The base `0 of 1` is not a content-novelty control. |
| A13 | **The measured revision rewrites the counter.** A script that ignores all blobs and prints `1 of 1` for the candidate and `0 of 1` when the argument equals the base satisfies both output/exit clauses. | Do not let the measured revision supply the trusted instrument. Execute the frozen counter bytes from an independent location, pin/check their hash and diff scope, provide independent junk inputs, and row-check the printed result (Q33). A self-test supplied by the same revision is not an independent guard. |
| A14 | **No actual recheck or source freshness despite a fresh-looking receipt.** A commit created later can carry hand-written `verified-at`, `opened`, and a quote copied from an earlier round. | Require revision-bound receipts naming the measured rev and actual fetch/run results, not just dates in Markdown. The counter can check receipt existence, hash, revision, quote and exit code; it cannot infer the real date from the date string alone. |

A4 has an important boundary: a quote copied from row A but **absent** from cited row B's anchor is
already rejected by conjunct 6 in a conformant implementation. The green cheat is to cite A (while
writing unrelated prose), copy A's own anchor quote, or also inject the quote into B's anchor. The
former mismatch should remain a negative control; it must not be misreported as a passing world.

## B. Implementation-dependent junk that needs explicit must-fail arms

These are not automatic holes in the written seven conjuncts. A correct implementation can reject
them, but a whole-file regex/dictionary implementation can print
`authority ladder grounded 1 of 1`, exit 0. Each therefore needs a public-`main()` red arm and an
honest green arm. After the stated correction, each must print `authority ladder grounded 0 of 1`
and exit nonzero.

| id | cheap world | required counter behavior |
|---|---|---|
| B1 | Put `knowledge/instruction-authority-ladder-round67.md` only in `## Frontier`, `## Known gaps`, a code fence, or a coverage row's **Basis** cell rather than its **File** cell. | Parse only `## Coverage map` up to the next level-two heading and require one table row whose File cell is exactly the target. A whole-README substring check would wrongly go green; the written conjunct 7 itself requires red. |
| B2 | Put an S###-looking table in `## Leads (unopened)`, or use a malformed row whose shifted cell happens to say `mined`. | Parse only the `## Registry` table and require exactly 11 cells with the status in column 8 of the row's 11 fields. Do not scan arbitrary Markdown for `S###` and `mined`. |
| B3 | Duplicate a cited S### id with conflicting URL/anchor/status, or duplicate the entry's source lines so one good line can rescue a bad one through `any()`. | Require exactly one registry row and exactly one opening source binding per cited id; reject conflicting duplicates rather than silently using first/last/any. |
| B4 | Hide `source:`, `verified-at:` or `recheck:` in comments/fences, put them after unrelated prose, or include conflicting duplicate dates. | Parse a real opening provenance block, excluding comments/fences; require exactly one non-conflicting verified-at and recheck and one source binding per id. |
| B5 | Let `--rev` select only a label while the entry, SOURCES, or README is read from the working tree. Opposite working-tree/candidate states can then counterfeit either half. | Validate a full 40-hex commit and read **all three** inputs with read-only `git show <rev>:<path>`. Add opposed-working-tree arms for each input, and a base-missing-entry arm asserting the exact zero line. |
| B6 | Place a valid quote under the wrong S### id, or let a quote anywhere in the entry satisfy every cited id. | Freeze the per-id quote grammar and require one distinct exact quote for every opening source id. Include swapped-id and one-quote-for-two-ids arms. |
| B7 | Use a symlink or another non-regular Git object at the target and follow it to an admitted file. | In `--rev` mode inspect the Git object type and require a regular blob; do not follow working-tree links. This arm is unnecessary only if the implementation's `git show` path already proves symlink text cannot satisfy the content grammar. |

Impacted axes: A1/A2/A11/A12 strike **depth**; A3–A10/A14 and B1–B4 strike
**consistency**; A13, B5, and the base/output controls strike **calibration**. The corrections
below are fixable instrument defects; semantic truth remains a separate review boundary.

## Smallest safe correction set

1. **Make the parser exact:** freeze per-id quote syntax; parse the coverage and registry sections;
   enforce unique rows/bindings, exact URL identity, non-empty exact quote equality, and committed
   bytes at the named rev. These are cheap and improve consistency without narrowing honest sources.
2. **Close the provenance fields already present in the contract:** current-round `opened` or a
   current Gate re-open record, `used-by`, tier/kind, a valid/runnable recheck, and current-round
   snapshot-plus-quote evidence. The established mechanisms in
   `verifiers/check_mcp_instructions.py:23-39` and
   `verifiers/check_command_files.py:146-160` already provide local patterns for opened dates,
   back-links/structured rows, Gate quotes and source fetching.
3. **Measure the claimed content, not just its container:** require the ladder/override/skill-body
   record and compare claimed new ground with base content. Keep named non-author semantic review
   for source relevance, unsupported prose, and the actual authority ordering. If that is outside
   the counter, Q26 requires bounding “grounded” to the smaller admission-shape result rather than
   claiming sourced depth from `1 of 1`.
4. **Pin the instrument and run every world above through public `main()`:** each green junk world
   must become red while honest source variants remain green, with the exact success and failure
   lines recorded. The existing do-nothing S999 control has no resolvable id, no verified-at and no
   index; it kills only the easiest world and does not cover any row above.

If these checks are added after the counter was frozen, Q28 requires treating them as a new or
re-frozen measurement before scoring, not silently substituting a widened counter. The residual
tradeoff is real: no lexical counter alone proves truthful prose or actual human source access.
That residual must remain bounded and independently reviewed; it is not evidence of depth merely
because the structural counter is green.
