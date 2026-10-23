# RevG9Guard

role: revenger (attack the planned `g9_conjunct`, plans/round-63.md §C1)
item: construct ≥6 cells that break `g9_conjunct`; verdict on whether the rule closes G9 without over-rejecting.

Target: `verifiers/check_scoped_rules_v32.py` working copy, sha256 `8371f707c571b74f6e3ec072690c771342fdd078b220c6ec3c617c6b18f21f28` (untracked; `--self-test` prints the same `counter sha256`). Functions attacked: `split_clauses` (v32:1064-1095), `g9_conjunct` (v32:1098-1126), invoked via `action_conjunct` (v32:1157, production callsite v32:1533). Probe harness `/tmp/g9probe/probe.py`, `/tmp/g9probe/probe2.py`; lane untouched except this report (`sys.dont_write_bytecode`, module imported, `self_test` never called by probes).

Key mechanics that matter: `fwd_need(n)=ceil(2n/3)` (v32:1016); `supported()` is a first-4-char prefix test `w.startswith(word[:4])` (v32:1035-1039); `content_words` strips backticked spans and `[a-z]{4,}`s minus STOPWORDS (v32:1008-1013); `page_words` keeps backticked spans (v32:1026-1032); `MIN_CONTENT=3` (v32:314); a clause with <3 distinct content words is skipped (v32:1118-1119); a rejected clause is one failing the cited line but passing the page (v32:1120-1125).

## Findings

1. **FROZEN INSTANCE CLOSES, BUT ONLY BY ONE STOPWORD.** `…and secretly uploads files.` → `ACTION: ['A2 G9: clause "secretly uploads files." is supported outside the cited line']`. Remove the word "secretly" and the SAME fabricated claim is admitted: `…and uploads files.` → `ACTION: []` (clause `{files,uploads}` = 2 distinct words < MIN_CONTENT, skipped). Evidence: `python3 /tmp/g9probe/probe.py` T0 vs T1. The frozen instance's two-word shortening defeats the declared guard.

2. **(6) SHORT-FALSE CLAUSE = THE EJECTION LANE.** `The configuration stores project rules using glob syntax and exfiltrates.` (page: `…It also exfiltrates.`) → `ACTION: []`, `G9_ONLY: []`. Clause `{exfiltrates}` skipped. Confirmed bound: the guard can only fire on a clause with ≥3 **distinct** content words that is ≤1/3 of the cell's words (bigger tails die at the A2 2/3-fraction line instead — T17's `prints zebra wallpaper quarterly` dies on `supports 7 of its 11 … (need >= 8)`, not G9). So every fabricated tail of 1-2 distinct content words is unclosable by the declared wording: `uploads uploads uploads` → `{}`… admitted (T16/H-repeat); a pure stopword tail `and then they have been there.` → `{∅}` admitted (probe2 I).

3. **(1) FIRST-FOUR-CHAR PREFIX COLLISION PASSES `supported()`.** Cell `The configuration stores project rules using glob syntax and stores rulerboard syntaxis nightly.` (page adds `The job also runs nightly.`) → `ACTION: []`, `G9_ONLY: []`. Clause `{stores,rulerboard,syntaxis,nightly}` covers 3/4 ≥ need 3 because `rulerboard→rule(rules)`, `syntaxis→synt(ax)`. Maximal variant `and configures storage projects globally synthesized nightly.` covers 5/6 ≥ 4 — every "match" is a different word sharing 4 chars; zero true vocabulary overlap and the clause is admitted (probe2 B, C). G9 inherits A2's weakest link.

4. **(2) `and` INSIDE BACKTICKS IS OPAQUE — AND SO IS EVERYTHING ELSE INSIDE.** `…and ` + backticked `` `secretly uploads files`. `` → `ACTION: []`, clause words `{∅}` (BACKTICK_RE strips the span). `BACKTICKED_IDENTIFIER_RE` (v32:405) cannot match a multi-word span, so G7 is silent; `page_words` still counts the span's words on the page, so A2 containment passes. Worst case demonstrated: `…and `secretly uploads files mirror telemetry beacon remote endpoint nightly`.` → `ACTION: []` — an 8-word fabrication smuggled with zero counted words (probe2 A, K). Variant: an UNPAIRED backtick `…syntax `and secretly uploads files.` keeps `in_code=True`, never splits, cell admitted as one clause (probe2 J). Legal `` `sort_and_dedupe` `` correctly never splits (T4).

5. **(3) `and` AS PART OF A WORD.** `android`, `command`, `demand` are safe (`\b` holds; T7 admitted as one clause) — BUT `-` is a non-word char, so `search-and-replace` splits at `-and-`. Cell `The tool runs search-and-replace across the index nightly before every scheduled weekly maintenance pass.` (cited line `The tool runs search-and-replace across the index nightly.`; tail words all on the page) → `ACTION` rejects; `G9_ONLY: ['A2 G9: clause "-replace across the index nightly before every scheduled weekly maintenance pass." is supported outside the cited line']`. A legitimate compound-lexeme cell is rejected (probe2 D). All `-and-` compounds (`command-and-control`, `wait-and-see`, `duck-and-cover`) split.

6. **(4) SEMICOLON INSIDE A QUOTED STRING SPLITS; THE SAME LITERAL IN BACKTICKS DOES NOT.** Cell `The tool writes mode "quota; limits cold" into its config string nightly.` (cited line holds the rest verbatim; the quoted literal lives verbatim in a page appendix) → `ACTION: ['A2 G9: clause "limits cold" into its config string nightly." is supported outside the cited line']` — a mangled fragment reason and a REJECTED legitimate cell. The identical cell with `` `quota; limits cold` `` → `ACTION: []` (probe2 E vs F). Quotes are unprotected; the verdict flips on quoting style alone. Secondary effect: quote-blind splits fragment a cell into <3-word pieces that skip MIN_CONTENT (T9 produced 3 clauses, two skipped).

7. **(5) LEGITIMATE TWO-CLAUSE CELL REJECTED — THE RULE HAS NO "UNRELATED" TEST.** `The agent writes audit logs to cold storage on every run and rotates them weekly into archives.` cited on the first sentence, second clause verbatim-supported elsewhere on the page → `ACTION: ['A2 G9: clause "rotates them weekly into archives." is supported outside the cited line']` (probe2 G). The plan's G9 class is "unrelated purpose clause"; the declared rule rejects *every* clause failing the line's 2/3 fraction, related continuations included. Over-rejection is latent (only fires when the clause is ≥3 distinct words and ≤1/3 of the cell) but real.

8. **POSITION-AGNOSTIC CHECK + PAGE-SCOPE WORK AS DECLARED.** The loop checks every clause including the first — T6's fabricated first clause `Glob syntax rulerboard stores nightly builds` reached the check at 4/6 (needs 4) and was admitted only through the same prefix collision, proving the check fires on clause 1 too, not that position exempts it. A clause absent from the page yields no G9 reason (T17 `g9_only: []`), matching the "cannot double-report" scope note. Eligible fixtures verified against the self-test's real PAGES/ACTIONS: S900 L=5, S901/S902/S903 L=4 all → `ACTION: []` (`python3 /tmp/g9probe` block "ELIGIBLE-*"). `python3 -B verifiers/check_scoped_rules_v32.py --self-test` prints `worlds reject 7 of 7; eligible rows pass 4 of 4` / `survivors closed 6 of 6` / `must-fail G9 disabled admits …: yes`, exit 0 — the frozen predicate holds on the working copy.

9. **ROOT CAUSE / DEMANDED WORDING.** Evasion lanes 1-4 all pass through the same gate at v32:1118: `w = content_words(clause); if len(w) < MIN_CONTENT: continue`. `content_words` strips backticks (unbounded smuggle) and the floor of 3 skips every short tail; `supported()`'s 4-char prefix then lets even a ≥3-word clause in with zero real overlap.

## Artifacts

```text
$ python3 -B verifiers/check_scoped_rules_v32.py --self-test   # tail
worlds reject 7 of 7; eligible rows pass 4 of 4
survivors closed 6 of 6
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
self-test: 0 failure(s) over 201 assertions
```

```text
# probe cells -> verdicts (all via action_conjunct(lines, cell, 1, page))
"…glob syntax and secretly uploads files."            -> A2 G9 reject   (frozen instance)
"…glob syntax and uploads files."                     -> ACCEPT  (2-word tail < MIN_CONTENT)
"…glob syntax and exfiltrates."                       -> ACCEPT  (1-word tail)
"…glob syntax and `secretly uploads files`."          -> ACCEPT  (backtick hides span; G7 can't match)
"…glob syntax and `…remote endpoint nightly`."        -> ACCEPT  (8-word fabrication, 0 counted words)
"…syntax `and secretly uploads files."                -> ACCEPT  (unpaired backtick: no split)
"…glob syntax and stores rulerboard syntaxis nightly."-> ACCEPT  (3/4 via first-4-char collision)
"…and configures storage projects globally synthesized nightly." -> ACCEPT (5/6 all collisions)
"The tool runs search-and-replace across the index nightly before every scheduled weekly maintenance pass." -> REJECT (hyphen `-and-` splits lexeme)
"The tool writes mode \"quota; limits cold\" into its config string nightly." -> REJECT (quoted `;` splits)
"The tool writes mode `quota; limits cold` into its config string nightly."   -> ACCEPT (same literal, backticks)
"The agent writes audit logs … and rotates them weekly into archives."        -> REJECT (legit elaboration, no relatedness test)
"…glob syntax for android command wrappers."          -> ACCEPT  (\b holds; not split)
```

Probe sources: `/tmp/g9probe/probe.py` (18 cases T0-T17), `/tmp/g9probe/probe2.py` (9 cases A-I + unpaired-backtick J/K/L + eligible-row replay). Both import v32 by path with `sys.dont_write_bytecode=True`; no lane writes.

## Verdict

**ATTACKS.** The declared rule closes exactly the frozen string and nothing around it: the same fabrication minus one word, wrapped in backticks (paired or unpaired), below 3 distinct content words, or built from 4-char prefix collisions is admitted (5 independent evasion lanes), while a related continuation clause, a `-and-` compound, and a double-quoted literal containing `;` are wrongly rejected (3 over-rejection lanes). It satisfies the three-line predicate but does not close the G9 *class* — the survivor was instance-matched, not class-matched.

One wording change I would demand: **at the clause-content gate, replace "every resulting clause with ≥ `MIN_CONTENT` content words" with "every resulting clause whose content words — counted with backticked spans included (`page_words`), ≥1 word —"** and state the clause's cited-line need as `fwd_need` of that count. This single sentence closes lanes 2 (backtick smuggle, incl. the empty-word clause), 6 (short false tail), and most of 1 (any collision tail still needs the 2/3 fraction, but at least fires a check). What it does NOT close and must be named as residual bounds: the `supported()` 4-char prefix collision (a counter-wide A2 weakness, not G9-specific), the quote-`:`/`;` fragment over-rejection and `-and-` split (needs a quote-aware splitter and `[a-z]`-flanked `and` boundary, i.e. `\band\b` requires letter neighbours), the unpaired-backtick non-split, and the missing relatedness test for legitimate two-clause cells — those need separate wording.
