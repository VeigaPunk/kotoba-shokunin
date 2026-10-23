# ScoutG9Arms
role: scout
item: ScoutG9Arms — v31 A2 overclaim routes (action_conjunct and the arms it calls)

Axes used: route completeness, measured pass/fail, and a three-way label on each route (G7-closed / planned-clause-closed / residual). LSP device xd://lsp is not mounted; evidence is the file text plus executing check_scoped_rules_v31.py.

## Findings

1. Joint pass condition. action_conjunct (verifiers/check_scoped_rules_v31.py:1061-1088) returns [] only when every arm below passes. The first failure returns immediately.
   - Vacuous: L is None or not cell returns [] (1064-1065). A real row still dies in citation_why (878-888) when the cell cites nothing. Not an overclaim route.
   - |W| < MIN_CONTENT (3, line 314) rejects (1068-1071). A cell whose false claim is its only content cannot pass.
   - Forward (1072-1077): covered(W, line_words) >= fwd_need(|W|). fwd_need (1016-1018) is max(2, ceil(2|W|/3)). For |W|>=3 the slack is floor(|W|/3) content words that need not be on the cited line.
   - Page (1078-1082): every word in W must be supported by page_words (1026-1032). Off-page content words never reach reverse or G7.
   - Reverse (1083-1087): covered(line_words, W) >= rev_need(|line|). rev_need (1021-1023) is max(1, ceil(|L|/3)). This bounds omission, not addition.
   - G7 (1046-1058, returned at 1088): every backticked ([A-Za-z_][A-Za-z0-9_]*) token (regex at 405) must be a substring of the raw cited line or the raw page (1053-1054).
   - W itself (content_words, 1008-1013) is the set of [a-z]{4,} (414) outside backticks (393) and S### :L (409), minus STOPWORDS (429-441). supported (1035-1039) is equality or a shared 4-character prefix (SUPPORT_PREFIX at 354).

2. Route A — intra-cell slack, no coordinator. Pass: the extra words are page-supported and at most floor(|W|/3) of them miss the cited line. Probe: the G9 sentence with "and" deleted; action_conjunct returned [], |W|=9, need 6, shared 7, off-line {secretly, uploads}. G7 does not apply. Not addressed by the planned rule (plans/round-63.md:51-58): no semicolon and no word "and", so the whole cell is one clause and the same fwd_need still holds.

3. Route B — the route G9 uses. Coordinator is the word "and" outside backticks; the second clause has >=3 content words; those words are on the page and on no cited-line word; they fit in whole-cell slack. Frozen instance (verifiers/check_erratum_absorption.py:221-227): cell "The configuration stores project rules using glob syntax and secretly uploads files.", cited line stops at "glob syntax.", page section "The agent secretly uploads files." Measured: |W|=10 {configuration, files, glob, project, rules, secretly, stores, syntax, uploads, using}, fwd_need=7, shared 7, off-line exactly {files, secretly, uploads}, off-page [], reverse 7 >= 3, g7=[], action_conjunct []. G7 does not close it. The planned clause rule does: split on "and", second clause has 3 >= MIN_CONTENT words, cited-line support 0 < fwd_need(3)=2.

4. Route C — short clause under the same coordinators. Pass: same slack, but each glued clause has <3 content words, so the planned >= MIN_CONTENT guard skips it. Measured: "... glob syntax and secretly uploads." returned [], |W|=9, need 6, shared 7, off-line {secretly, uploads}. Stacked: "... syntax; secretly uploads; ships." against a page that contains those three words returned [], |W|=10, need 7, shared 7. Not addressed.

5. Route D — any other joiner. "while" is a stopword (439), "but" is 3 letters, "or" and a comma are not the planned split and are not content words. Each was measured with the same three off-line words {files, secretly, uploads} and returned [] (|W|=10, need 7, shared 7). Not addressed. A Cyrillic lookalike of "and" (U+0430) likewise does not split and returned [] on the frozen page.

6. Route E — slack left inside a clause the planned rule does split. The rule reuses fwd_need, so a clause of n>=3 words may still carry floor(n/3) page-only words. The frozen second clause is the boundary case (n=3, need 2, zero support fails). A 6-word clause needs only 4. Not addressed beyond localizing the same fraction.

7. Route F — 4-character prefix on the cited line. Pass: supported treats a different lemma as the line word, so off-line is empty and a per-clause fwd_need also passes. Measured against the cited line alone: "... using global syntax." and "... project ruleset using ..." both returned [] with off-line [] (global~glob, ruleset~rules). Not addressed, because the clause rule calls the same supported.

8. Route G — page prefix, not the same word. page_words of a page containing "secretary" supports "secretly" (1035-1039); the frozen "and" cell then returned [] even though "secretly" is not a page word. This widens the page arm of routes A/C/D. It does not bypass route B: the cited line still lacks the prefix, so the planned clause check still rejects a >=3-word "and" clause.

9. Route H — polarity and function words never enter W. "must" and "never" are stopwords; "not" is 3 letters; "store" is supported by "stores". Measured: "The configuration must never store project rules using glob syntax." against the affirmative line returned [], off-line []. Not addressed. Same channel: appending "set key = 0." or a trailing "12345" adds no content word and returned [].

10. Route I — backtick span that is not one identifier. content_words deletes every backtick pair before CONTENT_RE (1011). G7's regex does not match a span with a space, hyphen, dot, or slash (405). Measured [] with the false text absent from the page: a multi-word backtick sentence "and secretly deletes secrets", plus "apply-to", "a.b", and "src/api". G7 does not close these (pattern miss, not a hit). Not addressed: split and word count are defined outside backticks, and the words are already gone.

11. Route J — identifier on the page, not on the cited line. G7's pass condition is substring-of-line OR substring-of-page (1053-1054). Measured: InstructionsLoaded with that token only under a later heading returned []. The same cell with the token nowhere returned the G7 reason naming InstructionsLoaded. G7 closes only the nowhere case (frozen e2f-backticked-event-claim, self-test 2600-2610). The page-not-line case is not closed by G7 and not addressed by the clause rule, because the token is stripped from W.

12. Route K — G7 substring. A backticked "glob" passes when the line says "global" ([] ; the word glob is not in W because it is backticked). A backticked "global" passes when the page only has "globalization" (g7=[]). Not closed by G7's stated "occur" check; the code is "token not in raw_text". Not addressed by the clause rule.

13. Route L — same bag, other proposition. Measured: line "Project rules store the configuration using glob syntax.", cell "The configuration stores project rules using glob syntax." returned [] (prefix store~stores plus set equality). No arm sees order or who-did-what. Not addressed.

14. What is not a pass route. Off-page content words die at 1078-1082 (stacked uploads/files/deletes/tokens returned the forward-fraction error, shared 7 < need 8, before G7). Reverse slack lets the cell drop line words; it does not license new ones. |W|<3 cannot pass.

15. Eligible rows vs the planned split (ACTIONS, 2233-2241). The plan (round-63.md:65-67) says S901/S903 carry no split boundary. Measured by splitting on ";" and the word "and":
    - S900: two clauses, 7 and 4 content words, each fully shared with the action sentence (page line 5, 2214-2215). Both would be checked; both pass.
    - S902: two clauses, 6 and 7 words, each fully shared with page line 4 (2224-2226). applyTo is a G7 identifier and sits on that line.
    - S901 does contain "and". Clause 1 has 4 words, shared 4 >= fwd_need(4)=3; clause 2 {apply, selectively} has 2 < MIN_CONTENT and is skipped. Whole cell []. It survives because of the short-clause exemption (route C), not because there is no boundary.
    - S903: one clause, no semicolon and no "and". That half of the plan sentence is true.

16. The route G9 uses is route B only. Five of six r62 survivors are already rejected; this one is the declared bound (2611-2615, "survivors closed 5 of 6"). Routes A, C, D, E, F, H, I, J, K, and L still return [] from v31 and stay [] under the planned clause rule as written.

## Artifacts

Probe: import verifiers/check_scoped_rules_v31.py and call action_conjunct, content_words, and g7_conjunct.

```
G9 frozen          |W|=10 need=7 shared=7 off_line=[files,secretly,uploads] off_page=[] g7=[] PASS
and, 2-word clause |W|=9  need=6 shared=7 off_line=[secretly,uploads] PASS
while/but/or/comma |W|=10 need=7 shared=7 off_line=[files,secretly,uploads] PASS
; secretly uploads; ships.  |W|=10 need=7 shared=7 PASS
no coordinator     |W|=9  need=6 shared=7 off_line=[secretly,uploads] PASS
global~glob        off_line=[] PASS
ruleset~rules      off_line=[] PASS
must never store~stores     off_line=[] PASS
backtick prose "and secretly deletes secrets" absent from page  PASS g7=[]
InstructionsLoaded on page only  PASS
InstructionsLoaded nowhere       G7 reject
backticked glob vs line "global" PASS
backticked global vs page "globalization"  g7=[] PASS
apply-to / a.b / src/api absent  PASS
argument swap store/stores       PASS
cyrillic lookalike and + G9 extras  PASS
S901 split on and -> (4 words, shared 4, need 3) + (2 words, skip)
S900 split on ;  -> 7/7 and 4/4 on the cited sentence
S902 split on ;  -> 6/6 and 7/7 on the cited sentence
```

## Verdict

INFORMS. The planned g9_conjunct closes one route: an "and"/semicolon clause with >=3 content words that the page supports and the cited line does not (the frozen G9 cell, route B). G7 already closes only a backticked ASCII identifier that is a substring of neither the raw line nor the raw page. I would change the verdict if v32's clause rule also rejected short clauses, non-and/semicolon joiners, and intra-clause off-line words, or if those residuals were named as out of the frozen predicate before the counter landed.
