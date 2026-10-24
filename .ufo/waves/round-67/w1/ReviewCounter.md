# Round 67 wave 1 — C2 counter honest-measurement review

## Evidence state

- The assigned draft, `.ufo/waves/round-67/w1/drafts/check_instruction_authority.py`, was absent on three direct read attempts. Each returned `does not exist`. There is therefore no implementation or self-test here to execute or inspect.
- This reviews the seven conjuncts in `plans/round-67.md:64-104` instead. No counter command was run, no temporary sandbox was created, and no measured tip is claimed. The full base hash `2a8eba56b3f9321b70c569fa2816d42237ca49a2` is pinned context, not a revision measured by this seat.
- Reference discovery used literal text search, followed by direct reads. Literal hits are not treated as semantic proof. The attack worlds below follow from the written conditions; no unobserved exit code or printed line is asserted.

## Findings

### High — H1: a metadata-only stub can satisfy all seven conjuncts without an instruction-authority ladder

**Evidence.** The headline is an “instruction-authority ladder” knowledge entry (`plans/round-67.md:64-73`), but the seven checks read existence, provenance lines, registry linkage, dates, quotes, and the index (`:83-90`). None reads a ladder body or even requires non-provenance body content. The bound at `:103-104` expressly excludes prose truth, but excluding prose truth does not require excluding the presence of the claimed artifact altogether.

A target file can consequently have valid opening `source:` lines, a current `verified-at:`, a `recheck:`, matching registry URL/anchor text, and a coverage row while its remaining body is empty or unrelated. Removing the entire ladder while preserving those metadata bytes does not falsify any written conjunct. The planned junk control (`:92-95`) does not close this hole: it removes an id, a date, and an index row, not the claimed ladder content alone. This leaves Q25's claimed-content-removed mutant without a specified red arm and Q26's headline clause without a measurement.

**Conjunct/claim let through:** the C2 **instruction-authority-ladder content** clause; conjunct (1) is existence-only, and (2)–(7) can remain satisfied with the ladder removed. An unrelated mined row also satisfies the written citation-shape conditions, so (3)/(6) do not establish topical relevance.

**Required disposition:** either the declared measurement needs a minimal content guard plus a body-removed mutant, or its headline/receipt must be narrowed to provenance-and-citation shape and must not carry the depth/content claim alone. A minimal structure check would still not be prose-truth verification.

### High — H2: “sources re-opened THIS round” is not measured; a stale mined row fits the seven checks

**Evidence.** The target requires every cited source to be re-opened this round with this round's access date (`plans/round-67.md:70-73,100-101`). Conjunct (3) checks only `status == mined`; conjunct (5) checks the **entry's** `verified-at:` date. None of (1)–(7) checks the cited row's `opened` cell, although that is a distinct registry column (`corpus/SOURCES.md:12-14`; `/home/vgpnk/Projects/shokunin/CORPUS.md:103-115`). No fetch/access evidence is part of the predicate either.

Thus an already-mined row with an older `opened` date can be cited by a newly dated entry and meet every written condition. Changing only the entry's date is not evidence that its source was re-opened.

**Conjunct/claim let through:** the **re-opened THIS round / current access-date** clause through (3) and (5); (6) checks quote text agreement, not access recency.

**Required disposition:** keep this clause out of the counter's claimed coverage unless a guard checks every cited row's current-round `opened` value, and cite independent access/fetch evidence for the actual re-opening. A date cell alone is not proof of the fetch. If this requires a post-freeze counter change, Q28 requires a separately labelled measurement rather than silently replacing the declared one.

### High — H3: conjunct (6) proves two lane-controlled strings agree, not that a quote is grounded in its source

**Evidence.** Conjunct (6) compares the entry's quote with the cited SOURCES row's `anchor` cell (`plans/round-67.md:88-90`). It reads no cited-source bytes and no committed page snapshot. The same invented or misplaced quotation of at most 25 words can be put in both files and satisfy the written comparison. Q26 requires the sourced/grounded clause to be turned on by the counter or a cited guard; Q51 (`corpus/QUALITY.md:62`) likewise distinguishes committed source evidence from a report's say-so.

The plan's bound (`plans/round-67.md:103-104`) is therefore important and honest, but it means the unbounded word “grounded” cannot rest on this predicate alone.

**Conjunct/claim let through:** **located-in-the-cited-source / source-grounded quote** through (6); the conjunct establishes only entry↔registry consistency.

**Required disposition:** describe (6) exactly as an entry-to-anchor comparison (Q31), and bind actual source location/authenticity and re-opening to named source-review evidence or an independent source-byte guard. Do not credit the counter with page validation it does not perform.

### High — H4: the written “occurs in” comparisons violate Q32's exact-identity requirement

**Evidence.** Conjunct (4) says the row URL “occurs verbatim” in the entry line, and (6) says the entry quote “occurs in” the anchor (`plans/round-67.md:86-90`). Q32 requires exact source/quote identity and explicitly requires must-fail arms for a sibling host and a fragment quote (`corpus/QUALITY.md:43`).

A raw substring implementation admits a canonical URL as a prefix of a longer, different token/path. For example, the opened staged S123 URL ends in `/2026-08-18`; appending `.evil` still contains the original URL verbatim but identifies different text. Likewise, `Instructions with higher authority` is only a fragment of the staged S123 anchor quotation `Instructions with higher authority override those with lower authority.` (`/home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md:7`), yet a substring test accepts the fragment. An empty extracted quote is the degenerate substring case unless explicitly rejected.

**Conjunct/claim let through:** (4) **same cited URL**, and (6) **the row's located quote**, by URL-token/path prefix, quote fragment, or empty-quote containment.

**Required disposition:** parse the entry's URL token and compare source identity exactly, with host equality and path-segment boundaries; extract the anchor's whole recorded quote and compare the complete quote, requiring nonempty text and the 25-word ceiling. Q48 arms must include sibling-host, same-host/path-extension, fragment-quote, and empty-quote worlds. This implements Q32's existing meaning; it is not license to relabel substring agreement as exact identity.

### Medium — M1: conjunct (5) accepts a non-runnable or meaningless `recheck:` value

**Evidence.** The plan requires only the presence of “a `recheck:` line” (`plans/round-67.md:88-89`). Q12 requires a `recheck:` that runs, and Q04 requires source/recheck commands to resolve and run (`corpus/QUALITY.md:15,23`). `recheck: someday`, a prose sentence, or a dead command meets the written presence condition.

**Conjunct/claim let through:** (5) **actionable/runnable recheck**, and therefore knowledge-admission compliance if this counter is cited for Q12/Q04.

**Required disposition:** either independently execute/validate the recheck and cite that guard, or limit prose to “a recheck field is present” and do not claim Q12/Q04 from this counter. A broken-recheck world must stay red in whichever guard owns that clause.

### Medium — M2: the planned compound junk world cannot detect a deleted individual conjunct; Q48 has no artifact-backed evidence

**Evidence.** The junk world simultaneously lacks a resolvable id, `verified-at:`, and a coverage row (`plans/round-67.md:92-95`). If an implementation omitted conjunct (4), for example, that same junk world would still be rejected for its other defects, so the control would not expose the omission. Q48 requires the public `main()` measurement path to have a satisfying exact-output arm and broken-conjunct rejection (`corpus/QUALITY.md:59`). The executor instruction also calls for isolated broken worlds (`.ufo/waves/round-67/w1-spec.json:19`), but the assigned script is absent, so none of this is demonstrated.

**Conjunct/claim let through:** whichever of (1)–(7) is accidentally omitted or disconnected from `main()`; the compound control can remain red regardless. In the concrete omitted-URL-check example, (4) is let through.

**Required disposition:** run a committed satisfying fixture through public `main()`, assert exit 0 and exactly `authority ladder grounded 1 of 1` on stdout, then run one broken world per conjunct with only that conjunct changed and assert exit 1 plus `authority ladder grounded 0 of 1`. Add H1's content-removed arm and H4's exact-identity arms; helper-only tests do not cover the measurement path.

### Medium — M3: the plan does not name the measured-revision instrument trust boundary

**Evidence.** The frozen command invokes `verifiers/check_instruction_authority.py` while `--rev` selects the measured bytes (`plans/round-67.md:75-81`). When the measured tip also supplies that script, a revision can weaken the instrument itself and make every conjunct's reported result unreliable. The plan contains no Q33 trust-boundary statement or outside guards; Q33 requires that boundary plus an instrument diff-scope check, independently constructed input, and output row check (`corpus/QUALITY.md:44`).

**Conjunct/claim let through:** potentially all of (1)–(7), and both the `1 of 1` and base `0 of 1` observables, if the measured revision controls the instrument without an external guard.

**Required disposition:** name the execution identity explicitly. If the measured revision supplies the script, add the Q33 outside evidence; alternatively run a separately pinned instrument copy and report that as a distinct measurement arrangement. Do not assume `--rev` on input files also pins the executing code.

## Residual risk and Q31 bounds

- Even a correct implementation of the seven written checks proves admission shape and entry↔registry↔index consistency only. It does **not** read `SOURCES.scope`, `teaches`, or `used-by`; does not establish topical relevance or reciprocal `used-by` membership; does not fetch source pages; and does not judge the ladder's correctness. Receipts, SCORECARD cells, and entry Limits must not credit it with those surfaces (Q31). In particular, `status: mined` alone does not show that the row's `used-by` names this target.
- The plan's statement that the counter reads the entry, SOURCES, and README “at `<rev>`” is the right contract (`plans/round-67.md:83-90`), but there is no code to show that it honors the contract. The same applies to the exact output sentence at `:75-81` and to Q48's public-`main()` requirement.
- No tool was installed or upgraded. No production file, draft, control, Git index, or jj state was changed; this report is the seat's only write.

## Verification gaps / required run evidence when the draft exists

1. **Committed-byte identity:** use a temporary repository with committed fixtures and public `main()`. Poison the working-tree versions of the entry, SOURCES, and README independently: a green committed revision must stay green despite red working-tree bytes, and a red committed revision must stay red despite green working-tree bytes. A valid base missing only the entry must produce the declared `0 of 1` result; an unknown revision must be an evaluation error, not silently treated as that base.
2. **Exact observable contract:** capture stdout and assert the single line `authority ladder grounded 1 of 1` with exit 0, or `authority ladder grounded 0 of 1` with exit 1. Keep diagnostics off stdout. Record the actual command, full revision, output, and exit code; none is available from this review.
3. **Fault isolation:** retain one satisfying fixture and one single-conjunct mutant for each of (1)–(7). Include wrong-README-section and wrong-table-cell arms for (7), multi-citation arms where only the second citation is broken, 25/26-word quote boundaries, and the H1/H4 mutants above. Ensure deleting a check in a scratch mutant makes the self-test fail.
4. **Claim-bound evidence:** if the headline retains actual source re-opening, source-location authenticity, a runnable recheck, or ladder content, cite the independent guard/review whose result changes when that clause is falsified. Otherwise bound the headline to what the seven checks actually read.
