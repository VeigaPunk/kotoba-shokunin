# SimpW2Entry — wave-2 dead-weight review of `corpus/knowledge/compound-clause-citation-round63.md`

role: simplifier (UFO-FSD simplifier posture; leaf member, no subagent dispatch)
item: Review the entry for dead weight — sentences that restate a frozen predicate
line, duplicate the lesson, or carry no load-bearing byte; propose at most three
concrete deletions as line-anchored diffs; verify no criterion text is lost
(QUALITY Q57/Q58 cross-references must survive).
axis judged: depth (dead bytes dilute the entry that carries the G9 receipt).
Lane tip audited: `cbbee56e9a3589b0b46736ad36f1b77701def80e`.

## Verdict on the committed bytes

The worktree file is byte-identical to the tip blob
(sha256 `0754f18abbe569678e762fb39bfbfccd7c6b8ae5b690f69de539c507ec43cb75` on both;
`git diff cbbee56e… -- corpus/knowledge/compound-clause-citation-round63.md` → empty).
After a sentence-by-sentence trace, the entry carries exactly **one** cut surface:
its §2 duplicates the two S119 located quotes that the frozen plan already
designates to the round-63 lesson Gate ("a ≤25-word located quote in the
round-63 lesson `## Gate`", plans/round-63.md § Sources). Everything else carries
load: commands and measured values (never cut per the lane's own trim rule,
`anatomy-and-compression.md` compression rule 2 / `SimplEntry62`'s applied rule),
bounds (§ Limits), protected provenance (§ Method provenance), and verification
receipts (house shape — the r62 sibling entry carries the same receipt tokens,
and this round's `check_r63_routed_repairs.py` check 3 literally consumes an
entry's `wc -l`/`wc -w` facts).

Counting commands re-run (all receipts verbatim, from the lane root):

```text
$ python3 -B verifiers/check_scoped_rules_v32.py --self-test
worlds reject 7 of 7; eligible rows pass 4 of 4
survivors closed 6 of 6
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
self-test: 0 failure(s) over 208 assertions
exit=0
$ python3 -B verifiers/check_r63_routed_repairs.py --rev cbbee56e9a3589b0b46736ad36f1b77701def80e
r62 routed defects closed 5 of 5
exit=0
$ python3 -B verifiers/check_r63_routed_repairs.py --rev 35d44b4b4dcdda234b5dbff7af37e432fec55f05
r62 routed defects closed 0 of 5
exit=1
```

All three match the committed claim's predicate; no verifier defect surfaced from
this seat's angle.

## Proposed deletion D1 (one of ≤3; the only one that survives the trim rules)

Lines 19–21 restate, verbatim, the two S119 quotes whose authoritative homes are
already committed twice: `corpus/lessons/round-63.md` § Gate (quotes at `:170`
16 words and `:172` 7 words, with snapshot sha `d76af0c0…` and the Q56
not-`byte-exact` note) and the `S119` row's teaches cell in `corpus/SOURCES.md:131`
(snapshot `.page:170-174`). The entry keeps the load-bearing part — the S119
anchor and the `:170,172` pointer — so compression rule 2 ("one authoritative
home per fact; keep the pointer") applies to the quoted spans only.

Line-anchored diff (produced by `diff -u pristine.md entry.md` on a /tmp copy;
nothing in the lane was edited):

```diff
--- corpus/knowledge/compound-clause-citation-round63.md (at cbbee56e, line 17ff)
+++ proposed
@@ -16,9 +16,7 @@
 
 2. **A committed record is corrected by an appended notice that names the
    measured value, not by rewriting the record in place.** S119 (ICMJE) states
-   the practice for a published article: publish "a correction notice as soon as
-   possible detailing changes from and citing the original publication" and
-   "archive all prior versions of the article" (`S119.page:170,172`). It grounds
+   the practice for a published article (`S119.page:170,172`). It grounds
    the *direction* of the repair; it does not mandate literal append-only files,
    and this lane's choice to append to `LOG.md` rather than edit it is the lane's
    own discipline, tested by a byte-prefix check, not by S119.
```

Exact proposed text for the replacement line (old line 19 → new single line):

```
   the practice for a published article (`S119.page:170,172`). It grounds
```

Word count before/after (`wc -w` on the whole file): **990 → 966** (−24 words;
`wc -l` 109 → 107). −24 decomposes as: `publish` + 15-word `:170` quote + `and` +
7-word `:172` quote = 24. No other byte changes.

### Deletion-safety evidence (scratch copy only)

- Q57 cross-reference survives: `grep -c 'Q57'` → **1** after the deletion (the
  only Q57 mention, § Method provenance line 60, is outside the hunk).
- Q58: the entry carries **zero** Q58 cross-references both before and after
  (`grep -c 'Q58'` → 0 on the pristine copy and on the edited copy) — the
  Q58-flavoured token-linkage bound lives in § Limits bullet 5 without naming the
  criterion row; that bullet is untouched, so no criterion text is lost.
- Both quoted spans are absent from the edited copy (`grep -c` → 0 each) while
  surviving in the designated homes (lesson Gate, SOURCES `:131`, snapshot
  `S119.page:170,172`), so no fact is orphaned.
- No machine caller consumes the entry's prose: `grep 'compound-clause-citation'
  verifiers/` → no matches; the census's `E11` check is existence-only
  (`scripts/sources-census.sh:566-568`, `[ -e "$dir/$path" ]`), and the file still
  exists, so S119's `used-by` census stays 17 W04 / exit 0.
- LSP note: no language-server device answered for this Markdown file in this
  session (no `lsp` device available), so the semantic-caller proof above is the
  recorded text-grep fallback, not server-backed reference evidence.

## Candidates considered and rejected (explicit bounds, with reasons)

1. § Verification bullet 1's mutant sentence ("Four G9 assertions discriminate the
   mutants MutG9Guard named …") — reads like wave evidence, but it is the receipt
   that MutG9Guard's missing-assertion finding was closed (its report shows the
   pre-fix shipped bytes fail to kill M2/M3/M6; 208 assertions post-fix). It is a
   measured kill claim other wave-2 mutation seats will attack, not restatement.
   Keep.
2. "The frozen instance needs no special case: …" (lines 39–41) — measured
   arithmetic (10 content words, `fwd_need` 7, shared 7; 0 of 3 vs 3 of 3) and the
   anti-overfit claim behind the "One frozen instance" bound. Never cut a measured
   value. Keep.
3. § Method provenance duplication with the lesson's § Method provenance —
   near-verbatim overlap exists, but provenance is explicitly marked; deleting
   either side would break the lane convention shared with
   `erratum-absorption-round62.md`. Protected; keep. (Flagged here only as an
   observation for the L1, no correction proposed.)
4. § Limits bullets and § 2's scope clause ("does not mandate literal append-only
   files") — bounds; never cut. The rule-section restatement of Q58-style negative
   conditions is the entry's durable rule statement; QUALITY Q58 owns the
   criterion row, so both exist by structural convention. Keep.

## Tradeoff and bound

D1 trades self-containedness (the entry no longer quotes S119 inline) for
single-homing the verbatim quotes. If the L1 wants the entry readable without a
lesson lookup, the alternative is keeping D1 out entirely — the loss is −24 of
990 words, so skipping it harms only the depth/economy axis marginally. Smallest
safe correction remains D1 as diffed above, applied by the L1 (this seat writes
no production bytes). No tools were installed or upgraded; no pacman/uv/npx use.
Lane integrity at hand-off: shared tree byte-identical to cbbee56e
(`git diff --stat cbbee56e…` → 0 lines; entry sha unchanged pre/post probes);
seat writes were `/tmp/simp-w2-entry/*` (scratch) and this report only.
