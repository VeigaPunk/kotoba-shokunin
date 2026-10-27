# B01PlanConsistency — round 76, wave w1

Seat: executor (planning data-walk). Base `b7f13f4b39cbd43076a85568adca763a6f674e7a`.
Read: `plans/round-76.md`, `plans/round-76-addendum-1.md`, `.ufo/waves/round-76/w1-spec.json`
(64 items), `.ufo/waves/round-76/w1-dispatch.json`, lane bytes at HEAD `eab64394dba08a47f6797a2e23719be14675b44b`.
Scratch: `/fast/scratch/hyaku/kotoba-r76/B01PlanConsistency/` (shared clones; removed at yield).

VERDICT: 3 defects found (1 blocking, 2 material). The plan's Q73 sweep conclusion is FALSE as
written: the planned touch list DOES edit a section a frozen counter pins. The C1/C2 predicate
sentences are NOT byte-identical across plan / context / SCORECARD — four concrete drifts.

================================================================================
1. BLOCKING — the Q73 sweep conclusion is false: the touch list edits a pinned file
================================================================================

The plan (§No-harm battery) claims:

  "Q73 sweep: `grep -n 'byte-identical\|differs from the base' verifiers/*.py` before freeze —
   the touched sections (SKILL.md § Body craft, § Gate registry, floors registry, lesson files,
   LOG append) are not pinned by any frozen counter at base; the one historical pin
   (`check_province_core.py` § Adjacent) is untouched."

Both halves fail.

(a) THE SWEEP MISSES A PIN ON A FILE THE ROUND EDITS.
The sweep output (run verbatim, 16 matches in 8 files) includes
`verifiers/check_tip_battery.py:50` and `:122`:

    instrument-pin  errata E2: each of the six scripts is byte-identical to the
                    base or to the one reviewed draft blob (INSTRUMENT_PINS)

`verifiers/check_tip_battery.py` is a registered lane gate (SKILL.md § Gate registry, row
`verifiers/check_tip_battery.py`), and its `INSTRUMENT_PINS` pins six instrument scripts
byte-identically, INCLUDING `verifiers/check_assertion_floors.py`:

    INSTRUMENT_PINS = {
        "verifiers/check_gate_registry.py": ("95ffed38…",),
        "verifiers/check_assertion_floors.py": (
            "780f6fe5184ecb94e70f0f79446ae4339d1aec27",
            "50348420260ab41a916ef1ab19d27966565de5af"),
        …

`verifiers/check_assertion_floors.py` is in the plan's Touch list under Edited
("`verifiers/check_assertion_floors.py` (in-file tables + docstring, same change)") — the D4
floors bump. Its current blob at base is `50348420260ab41a916ef1ab19d27966565de5af`, which is in
the allowed set; ANY edit changes the blob and fails the pin.

MEASURED (scratch shared clone at base, one docstring byte changed in
check_assertion_floors.py — the minimal possible D4 edit):

  $ git rev-parse HEAD
  1c68cc3d46c3d4c392a8180b6adbb79ed9684b6c
  $ python3 -B verifiers/check_tip_battery.py --rev 1c68cc3d46c3d4c392a8180b6adbb79ed9684b6c
  guard no-deletions PASS
  guard floors PASS
  guard instrument-size PASS
  FAIL guard instrument-pin: verifiers/check_assertion_floors.py blob
    6095c9f4535631b1eca23e76c3f7b767745e88ff at 1c68cc3d46c3d4c392a8180b6adbb79ed9684b6c
    is not a pinned blob
  guard spotcheck-identity PASS
  … tip battery exit 0: 2 of 6
  EXIT=1

CONTROL — the same command at the UNMODIFIED base:

  $ python3 -B verifiers/check_tip_battery.py --rev b7f13f4b39cbd43076a85568adca763a6f674e7a
  guard no-deletions PASS / floors PASS / instrument-size PASS / instrument-pin PASS /
  spotcheck-identity PASS
  guards 5 of 5; tip battery exit 0: 4 of 6
  EXIT=1

So the D4 floors bump turns the tip-battery `instrument-pin` guard from PASS to FAIL. The
guards go 5 of 5 -> 4 of 5. The round-76 base-battery receipt does not run check_tip_battery.py,
so this breakage is invisible to the plan's own no-harm battery.

Note the `instrument-size` guard passes either way (22 added / 3 deleted lines vs cap 40) — the
guard that fires is specifically the byte-identity pin, which is why the plan's size-cap reasoning
does not cover it.

PRECEDENT FOR THE FIX (the plan does not name it): the same situation was handled at round 72.
`verifiers/check_assertion_floors.py` was edited in the r72 claim-data commit `a0f7f17`
(blob `780f6fe5…` -> `50348420260ab41a916ef1ab19d27966565de5af`), and the pin set was widened in
the SAME lineage to accept the new blob: `git log -S'50348420260ab41a916ef1ab19d27966565de5af' --
verifiers/check_tip_battery.py` -> `30d27da` "round-72: freeze 2 … three counters (… tip battery …)".
Both blobs are present in `INSTRUMENT_PINS` today. The r76 equivalent is to add the D4-edit blob of
check_assertion_floors.py to `INSTRUMENT_PINS` — i.e. `verifiers/check_tip_battery.py` must be in
the Touch list. It currently is NOT (Touch list Edited omits it; Not-touched omits it too).

(b) THE SWEEP ALSO MISSES A SECOND PIN ON A FILE THE ROUND EDITS.
`verifiers/check_tip_battery.py` also carries a `spotcheck-identity` guard: "every
corpus/lessons/*-verifier-spotcheck.md present at the base is byte-identical (same blob SHA) at
<rev>" (lines 53-54, 122, 328). The plan's Touch list edits `corpus/lessons/round-75.md`
(appended correction) — that file is NOT a spot-check file, so this one does not bite. But
`corpus/lessons/round-76.md` is new this round and the round-76 closure will add a
`round-76-verifier-spotcheck.md`; the guard only compares BASE files, so a NEW spot-check file is
reported INFO, never a failure (verified in the run above: "INFO spotcheck added at …"). That path
is safe. The `no-deletions` guard ("no path under corpus/ or verifiers/, and no SKILL.md, tracked at
the base is absent at <rev>") is also satisfied — the round only adds. So (b) is a coverage note,
not a defect; (a) is the defect.

(c) THE PLAN UNDERSTATES ITS OWN SWEEP.
The plan says "the one historical pin (`check_province_core.py` § Adjacent)". The sweep actually
returns 16 matches in 8 files. Classified by what each pins (all verified by reading the code):

  FILE                              WHAT IT PINS                                    ROUND-76 EDIT?  VERDICT
  check_province_core.py:24,108     PROVINCE.md § Frontier and § Adjacent,          no (PROVINCE.md  SAFE
                                    byte-identical to base a5f7459                 not touched)
  check_tip_battery.py:50,122,309   6 instrument scripts byte-identical to          YES — floors   DEFECT
                                    INSTRUMENT_PINS (incl. check_assertion_         registry + floors
                                    floors.py); also 6 scripts +40/-40 lines        guard edited
  check_tip_battery.py:53,122,323   corpus/lessons/*-verifier-spotcheck.md blob     no               SAFE
                                    identity vs base
  check_tip_battery.py:38,254       no corpus//verifiers//SKILL.md base file        no (only adds)  SAFE
                                    deleted at <rev>
  check_tip_battery.py:40,296       no floors-registry.json floor lowered, no       no (only adds)  SAFE
                                    base row dropped
  check_r68_routed_repairs.py:36    historical r68 wave paths, "blob that differs    n/a (r69      N/A
                                    from the base's"                               scope, not r76)
  check_scoped_rules.py:1988        a FIXTURE STRING literal "supersedes S096 —      no             N/A
  check_scoped_rules_v31/v32        byte-identical" inside alias_sha_why()          (string data,
                                                                                  not a pin)
  check_substrate_pins.py:86        a COMMENT about pin-key byte identity           no             N/A
  check_assertion_floors.py:1151    a COMMENT about F9 fixture stubs being           no             N/A
                                    byte-identical

So the plan's sentence is wrong twice: it names one pin where the sweep finds a pin on a file the
round edits, and it describes a sweep that returns 16 matches as if it returned one.

RECOMMENDED FIX (L1 decision, pre-data): add `verifiers/check_tip_battery.py` to the Touch list
(Edited) and add the D4-edit blob of `verifiers/check_assertion_floors.py` to `INSTRUMENT_PINS`,
following the r72 precedent in `30d27da`. Without this, the r76 tip turns a registered lane gate
red. This is a Touch-list edit + one line in a counter's pin table; it moves no predicate.

================================================================================
2. MATERIAL — the plan's base-battery receipt claims green where the gates are RED at base
================================================================================

The plan (§Base battery) and the committed receipt
`.ufo/waves/round-76/base-battery/base-battery.txt` (committed `abd8e5c`, dated 2026-10-27T13:42)
both assert:

  == python3 -B verifiers/verify_corpus_integrity.py --json   exit=0
  == python3 -B verifiers/verify_corpus_independent.py --json exit=0

Both are FALSE at the stated base. Measured on a clean shared clone checked out at b7f13f4:

  $ python3 -B verifiers/verify_corpus_integrity.py --json ; echo $?
  1
  $ python3 -B verifiers/verify_corpus_independent.py --json ; echo $?
  1

The four corpus-integrity DRIFTs at base:

  corpus.index.tracked_files | observed 145 | expected 144
  corpus.index.unindexed     | observed 1   | expected 0 / empty
  corpus.pointers.report_total | observed 101 | expected 99
  corpus.pointers.commit_total | observed 44 | expected 43

Cause: base commit b7f13f4 ADDED `corpus/lessons/round-75-verifier-spotcheck.md` (the r75
closure's spot-check) without adding it to `corpus/README.md`'s index (grep: 0 hits) and without
re-recording `verifiers/corpus-baseline.json` (last touched by `14ab415`, which pre-dates the
spot-check file). Bisection confirms the gate went red exactly at b7f13f4:

  14ab415  tracked=144  integrity_EXIT=0
  ac9f295  tracked=144  integrity_EXIT=0
  b7f13f4  tracked=145  integrity_EXIT=1   <-- base of round 76

This is directly load-bearing for C2. R2 requires receipt
`.ufo/waves/round-76/receipts/noharm-at-tip.txt` to carry "stdout + exit codes of
`verify_corpus_integrity.py --json` and `verify_corpus_independent.py --json` reading green". If
both gates are red at base and the round does not repair them, R2 cannot reach green at the tip
either, and the counter's R2 conjunct fails closed. The Touch list DOES include
`corpus/README.md` (index row) but NOT `verifiers/corpus-baseline.json` — so the baseline
re-record (tracked_files 144->145, report_total 99->101, commit_total 43->44) has no owner and no
touch-list slot. Note the r75 closure had already routed the corpus-baseline staleness (R2 of the
r75 round-75-verifier-spotcheck.md) and the plan's own Trigger section reads "D2 (d5aebcf never
listed …), D3 (no forward pointer …), D4 (check_spec_craft/check_sibling_reread absent …) are
unworked" — it enumerates D2/D3/D4 but misses this D5-class item: the base is already red.

A SECOND, SMALLER INSTANCE: `verifiers/check_tip_battery.py` is red at base too (guards 5 of 5
but "tip battery exit 0: 4 of 6", EXIT=1) — because its own battery re-runs
verify_corpus_integrity.py / verify_corpus_independent.py, which are red at base for the reason
above. This is the same root cause, not an independent defect. It also means the base-battery
receipt's silence on check_tip_battery.py is a real omission, not just a scoping choice.

RECOMMENDED FIX (L1 decision): either (i) add `verifiers/corpus-baseline.json` to the Touch list
and re-record it against b7f13f4 (and add the r75 spot-check to `corpus/README.md`'s index — the
index row slot already exists in the Touch list), or (ii) amend the plan's Base battery section and
R2's wording to say the corpus gates are RED at base and that R2 requires them to reach green at
the tip, making the baseline repair part of R2's work rather than an unowned precondition.

================================================================================
3. MATERIAL — predicate-sentence drift: the frozen sentences are NOT byte-identical
================================================================================

Q26 requires the same sentence in plan, counter receipt and SCORECARD. Measured against the plan
text, the wave context (as every seat received it), and the seat tasks. Four drifts:

DRIFT 3a — C1 counter line: the plan and the context state DIFFERENT strings.
  plan    §C1 : "`python3 -B verifiers/check_desc_craft.py --rev <rev>` prints
                  `description craft backed K of 6` and exits 0 only when all six conjuncts below
                  hold at `<rev>`; at base `b7f13f4…` it prints `description craft backed 0 of 6`
                  and exits 1."
  context (Goal, and the B06 seat prompt) : "prints `description craft backed 6 of 6` exit 0 at
                  tip, `0 of 6` exit 1 at base b7f13f4…"
  seat B06: "a final 'description craft backed K of 6' line; exit 0 iff K=6."
  The plan uses the placeholder "K of 6"; the context states the resolved "6 of 6" and drops the
  "description craft backed" prefix from the base-line ("`0 of 6`" not "`description craft backed
  0 of 6`"). A SCORECARD row drafted from the context (B18 is told to quote "the two frozen
  counter sentences with base->tip placeholders") and a counter receipt drafted from the plan
  (B06 is told to print "K of 6") cannot be byte-identical. Precedent for the right form:
  plans/round-74.md:66 and the r74 counter's docstring (check_spec_craft.py:6-9) are byte-identical
  — "python3 -B verifiers/check_spec_craft.py --rev <rev>  ->  prints \"spec craft pages backed
  N of 3\", exit 0 when N == 3" — with the PLACEHOLDER "N of 3" on both sides, and the concrete
  numbers only in the print line (check_spec_craft.py:1048 `print(f"spec craft pages backed {n}
  of {TOTAL}")`). The r76 plan should adopt that: one frozen sentence with "K of 6", quoted
  verbatim into the counter docstring, the receipt label, and the SCORECARD row.

DRIFT 3b — C2 counter line: same defect, and the plan's own C2 sentence uses a DIFFERENT
placeholder convention than its C1 sentence.
  plan    §C2 : "prints `r75 routed repairs closed 4 of 4` and exits 0 only when all four
                  repairs below hold at `<rev>`; at base `b7f13f4…` it prints `r75 routed repairs
                  closed 0 of 4` and exits 1."
  context        : "prints `r75 routed repairs closed 4 of 4` exit 0 at tip, `0 of 4` exit 1 at
                    base."
  seat B07       : "Print per-repair verdict lines + 'r75 routed repairs closed K of 4'; exit 0 iff
                    K=4."
  Here the PLAN says "4 of 4" (resolved) while the seat prompt says "K of 4" (placeholder) —
  the inverse of the C1 situation, and the two claims in the same plan section use opposite
  conventions. One convention must be chosen for both.

DRIFT 3c — the base revision is stated for C1 but implied for C2.
  plan §C1 names the base explicitly: "at base `b7f13f4b39cbd43076a85568adca763a6f674e7a`".
  plan §C2 names it too, but the CONTEXT's C2 line says only "at base" with no revision — the
  base rev appears in the C1 line of the same context paragraph. A seat reading only the C2 line
  has no base rev. Seat A11MutRedBefore resolves it ("both must print 0 of 6 / 0 of 4 and exit 1
  … at base rev b7f13f4b39cbd43076a85568adca763a6f674e7a"), so no seat is actually misled — but
  the frozen sentence is not self-contained, which is what Q26 asks for.

DRIFT 3d — C1 conjunct (a) was rewritten by the addendum; the seat prompt was not.
  The addendum (§Correction) withdraws the S213-anchor clause and re-pins the digest in four
  places. The addendum states "Counters and seats implementing conjunct (a) must implement this
  corrected form" — but seat B06's prompt (written before the addendum) still reads:
     "(a) snapshot chain (manifest + fetch record + pinned digest table in the counter +
      S213 anchor digest)"
  and seat A02RevHashChain's prompt still reads "…and the S213 anchor update draft".
  Both still name the withdrawn clause. The addendum says "no seat output has been scored against
  the withdrawn clause", but B06 and A02 are the two seats that will IMPLEMENT and ATTACK that
  clause, and their prompts are frozen in `w1-spec.json` (committed `4de12b6`, before the addendum
  `7eed80e`). The addendum is a plan-side file; the seat prompts are what B06/A02 actually read.
  This is the drift with the highest chance of a wrong artifact: B06 could write the counter to
  require the anchor digest (which the addendum withdrew and which `check_sources_append_only.py`
  forbids in place — the anchor cell is a PROTECTED cell; measured below).

The addendum also fixes the render-length convention ("clip-preserving … = 1022 at the r75 tip …
Every receipt that prints the number must print both variants (clip 1022 / stripped 1021) and name
the convention"), which resolves the ambiguity I measured: the folded block renders 1022 with a
trailing newline kept and 1021 without it, and the extraction idiom decides which
(`raw.split('---')[1]` -> 1022; `re.search(r'\A---\n(.*?)\n---\n').group(1)` -> 1021). First
sentence is 151 chars, and this too is extraction-dependent (`.split('. ')[0]` = 150 without the
period; 151 with it; a naive `.split('.')[0]` gives 57 because "SKILL.md" contains a period). The
addendum names the convention for the length but not for the first sentence; the plan's C1 (d)
requires the counter to recompute BOTH. The same convention must be named for the first sentence or
(d) is unmeasurable. Recommend: pin "first sentence = text up to and including the first '.' that
is followed by a space" (yields 151, and does not split "SKILL.md").

================================================================================
4. Seat-implied predicate drift (what each seat's task asserts vs. the plan)
================================================================================

Per-seat implied readings, checked against the plan. Only the material ones are listed.

C1 conjunct (b): ">=4, <=25 words each, verbatim in the optimizing-descriptions snapshot after
its first heading, absent from the other two snapshots" — plan and B04/B06/A01 agree on all four
sub-clauses. OK.

C1 conjunct (c): plan says SKILL.md carries "a description-craft rule row in § Body craft citing
corpus/knowledge/description-craft-round76.md and S213, containing at least two quote fragments
that occur in the optimizing-descriptions snapshot". Seat B13 says the same, plus "two
gate-registry rows … formatted exactly like existing rows". The plan's Touch list names those two
gate-registry rows. Consistent. Verified that adding one such row to § Body craft does not break
the r74 counter: measured `check_spec_craft.py --rev <tip-with-the-row>` -> "spec craft pages
backed 3 of 3", exit 0. SAFE.

C1 conjunct (d): plan says the entry's audit table holds "rendered `description` length and
first-sentence length of `SKILL.md` at `<rev>`" and the counter recomputes them from the measured
revision's committed bytes. Seat B05 is told to write a receipt named
`description-audit-<full-rev>.txt` — i.e. the audit is keyed to a REV, but B05 measures at HEAD,
which moves as the wave lands. The plan says the counter recomputes "at `<rev>`", so the entry's
audit table must equal the value at the TIP rev, not at the rev B05 happened to measure. Because
the round adds a § Body craft row and two § Gate registry rows to SKILL.md but does NOT touch the
frontmatter, the description length is stable across the wave (measured: identical 1022/151 at
b7f13f4, ac9f295 and HEAD) — so this converges. Low risk, but B05's receipt filename should be
re-read at the tip, not trusted from the build tree.

C1 conjunct (f) / provenance: plan requires "source: (naming S213 and the URL), verified-at:,
recheck:" — B12 says "provenance trio first (source: S213 + URL + anchor; verified-at: rev;
recheck:)". B12 adds "anchor" to the source cell. The r74 counter's (a) requires "source: lines
for every cited id, then verified-at: and recheck:" and (c') requires "the 64-hex digest in the
cited registry row's anchor cell" — the ANCHOR is a registry cell, not an entry source field.
B12's "URL + anchor" may read as "put the anchor in the entry's source:" — which is where the
withdrawn S213-anchor clause would land. Worth one line of clarification, but low severity.

C2 R1: plan requires the lesson round-75 correction AND receipt
`.ufo/waves/round-76/receipts/r1-folded-render.txt` "recomputing the render length from the
measured revision's SKILL.md and prints 1022". Seat B07's prompt repeats both. BUT no seat is
tasked to PRODUCE `r1-folded-render.txt` — B07 is the counter AUTHOR (it writes the counter that
READS that receipt), and A29RevengerR1 verifies the correction's method on ac9f295 but is told to
report only. A scan of all 64 prompts for a producer of that path finds none. Same for
`receipts/noharm-at-tip.txt`: B24TipBatteryScript writes `receipts/tip-battery.sh` and
`receipts/tip-battery-base.txt` — different filenames — and B07/A36 only consume
`noharm-at-tip.txt`. Two of C2's four repair inputs therefore have no producing seat in the wave
spec. The L1 must either assign them or produce them at integration.

C2 R3: plan requires note `.ufo/waves/round-76/w2-registry-note.md` (note the path is at the WAVE
root, not under build/). Seat B09 is told to draft it to
`.ufo/waves/round-76/build/w2-registry-note.md` — a different path, and under build/ where the
L1 integrates from. The plan's Touch list covers `.ufo/waves/round-76/**`, so both land. Minor, but
the counter (B07) is told to read the wave-root path; the L1 must place it there. Facts verified:
the r75 w2 results file has 64 entries, R75Attack28's `output` names
"kotoba-shokunin/.ufo/waves/round-75/w2/R75Attack28.md", that file does not exist, and
`.ufo/waves/round-75/w2/*.md` counts 63. The plan's "63 of 64 report files" is right.

C2 R4: plan requires "LOG § Round 75 carries an appended closing line recording the w2 settlement
(64 seats, 0 dead, 63/64 reports, R75Attack28 phantom per R3) after the 'w2 falsify results
pending' text". Verified the anchor text exists: LOG.md:2810 ends "w2 falsify results pending;".
Seat B09 says "w2 settled 64/64 results" — the plan says "64 seats". 64 results vs 64 seats is the
same number but the plan's wording "64 seats" is the odd one (the wave had 64 seats; the results
file has 64 entries). Seat B19 also drafts "the one-line closing append for LOG § Round 75 (R4)
if B09 has not" — two seats on the same line, with an explicit precedence ("if B09 has not"), which
is fine.

C2 counter requirements: plan requires "--self-test with a must-fail arm per repair …; a
token-dump world … must fail; the counter recomputes R1's 1022 from bytes". Seat B07's prompt
matches all three, and adds the base run + C2-W1 control receipt. Consistent.

Wave shape: the plan §Wave shape still says "30 build + 34 attack (attack share 53%)" and lists a
role floor including "labrat 4" and "sonic 1". The dispatched spec has 28 B + 36 A = 56.2%, with
zero labrat and zero sonic seats. The ADDENDUM (§Wave role correction) records the validated mix
(executor 15, scribe 10, reviewer 10, scout 10, critic 6, mutation-tester 4, simplifier 3,
revenger 3, sentinel 2, connector 1 = 64; attack roles 22/64 = 34.4%) and the dispatch commit
message says "34% attack share". Three different attack-share numbers are therefore live: 53%
(plan §Wave shape), 34.4% (addendum), 56.2% (spec prefix count). The addendum explains the
delta (roles validator refused labrat/sonic), so this is a stale-paragraph problem, not a
contradiction in the frozen contract — but §Wave shape was not edited, so a reader of the plan
alone gets the wrong mix. Recommend §Wave shape be annotated to point at the addendum.

Also note the addendum's `## Reason` heading is EMPTY — the text under "## Reason" is the
"## Wave role correction" section, so the two corrections (conjunct (a) and the role mix) sit
under a heading that names neither, and the reason for the conjunct (a) withdrawal (CORPUS.md
rule 2: only status/recheck/used-by change in place) is stated in the body but not under
`## Reason`. Cosmetic.

================================================================================
5. Adjacency — the withdrawn S213-anchor clause is forbidden by a live gate
================================================================================

Measured consequence of the clause the addendum withdrew, for the record: editing S213's anchor
cell in place breaches `verifiers/check_sources_append_only.py`, which is a registered lane gate
(SKILL.md § Gate registry) and an anchor of `check_could_not_evaluate.py`. On a scratch clone at
base, adding a `page sha256 …` to the S213 anchor cell:

  breach 142211d2e S213 anchor: …t ls-remote); quote "A should-trigger query … ->
    …t ls-remote); page sha256 aaaaaaaaaaaaaaaaaa…
  sources append-only breach 6 change(s) in 5 of 29 commits
  EXIT=1

(the same run at the unmodified base reports 5 breaches in 4 of 28 commits — the gate is already
red at base for unrelated r74/r75 rows, so the D-row delta is what the +1 shows). The addendum's
withdrawal was correct and necessary: the r74 precedent (S223's anchor carries a digest) works
because S223 is a NEW row, whereas S213 is an EXISTING row whose anchor cell is protected.

================================================================================
6. What I verified as CONSISTENT (so the L1 does not re-open it)
================================================================================

  * Base rev b7f13f4b39cbd43076a85568adca763a6f674e7a is the real base: HEAD is
    eab64394…, ahead of b7f13f4 by 4 commits (abd8e5c plan, 4de12b6 spec, 7eed80e addendum,
    eab6439 role mix), lane clean apart from the wave's own untracked dirs.
  * The plan commit abd8e5cfd45ea3863b344ac58a187b0c5de620d0 is what A11 names — correct sha.
  * D4 floors values are right: check_spec_craft --self-test -> "0 failure(s) over 250
    assertions" exit 0; check_sibling_reread --self-test -> "0 failure(s) over 47 assertions"
    exit 0. The live working tree's D4 bump (already applied: instrument_total 15->17, spec_craft
    250, sibling_reread 47) makes check_assertion_floors.py itself PASS (exit 0, all six new
    rows PASS). The D4 bump is internally correct; it is only the tip-battery BYTE PIN that
    objects.
  * The two new counters do not exist at base or at HEAD (verifiers/check_desc_craft.py,
    verifiers/check_r75_routed_repairs.py) — so a counter run "at base b7f13f4" must be the
    counter file run WITH --rev b7f13f4, not a checkout of b7f13f4. A11MutRedBefore says "run
    both counters at base rev … in a --shared worktree" — that phrasing reads as checking out
    the base, where the counter does not exist. Worth a one-line clarification to A11/B06/B07.
  * gate registry at base: "gate registry rows conformant 60 of 60 lane verifiers; phantom 0",
    exit 0. Note the universe is every verifiers/*.py and *.sh at the rev (Tree.universe), so
    adding two counters raises the expected count to 62 — the two new registry rows B13/B23 draft
    are needed for that, and the plan's Touch list covers SKILL.md § Gate registry.
  * SKILL.md is 590 lines at HEAD (budget 600), so the +1 § Body craft row and +2 gate-registry
    rows fit (593), but only if B02's anchors hold.
  * R3's facts: r75 w2 results file has 64 entries; R75Attack28's output names a report path that
    does not exist; 63 .md files in .ufo/waves/round-75/w2/. Plan's "63 of 64" is right.
  * R4's anchor text exists at LOG.md:2810 ("w2 falsify results pending;").
  * Census row count 151 and the S213 row's 11 cells are unchanged; the S213 used-by cell is the
    only cell the plan edits, and `used-by` IS a permitted in-place column under CORPUS.md
    rule 2 / check_sources_append_only.py PERMITTED = ("status","recheck","used-by"). The
    addendum's "S213 used-by append only" is consistent with the gate.
  * The plan's Touch list correctly names check_province_core.py and its § Adjacent pin as
    Not-touched, and PROVINCE.md is not in the edited list, so that pin is safe.
  * The no-deletions and floors-never-lower guards of check_tip_battery are satisfied by the
    round's additive-only file set.

================================================================================
Commands run (all read-only on the lane; all scratch clones under
/fast/scratch/hyaku/kotoba-r76/B01PlanConsistency/)
================================================================================

  grep -n 'byte-identical\|differs from the base' /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/*.py
    -> 16 matches in 8 files (full classification in section 1c above)
  git -C <lane> log --oneline -5 ; git -C <lane> status --short ; git -C <lane> rev-parse HEAD
  git -C <lane> diff --stat b7f13f4..HEAD
  git -C <lane> rev-parse b7f13f4:verifiers/check_assertion_floors.py   -> 50348420260ab41a916ef1ab19d27966565de5af
  git -C <lane> hash-object verifiers/check_assertion_floors.py          -> 9cb860bda21ef8d24fcb0603aa85372b96f3ac41 (live D4 blob, unpinned)
  git -C <lane> log -S'50348420260ab41a916ef1ab19d27966565de5af' -- verifiers/check_tip_battery.py  -> 30d27da
  git -C <lane> merge-base --is-ancestor 30d27da a0f7f17               -> rc 0 (pin set created before the r72 floors edit)
  python3 -B verifiers/check_gate_registry.py --rev b7f13f4…            -> "60 of 60 lane verifiers; phantom 0" exit 0
  python3 -B verifiers/check_spec_craft.py --self-test                 -> "0 failure(s) over 250 assertions" exit 0
  python3 -B verifiers/check_sibling_reread.py --self-test             -> "0 failure(s) over 47 assertions" exit 0
  python3 -B verifiers/check_assertion_floors.py                       -> exit 0 (live tree, post-D4)
  python3 -B verifiers/verify_corpus_integrity.py --json              -> exit 1 (live tree AND clean b7f13f4 clone)
  python3 -B verifiers/verify_corpus_independent.py --json            -> exit 1 (clean b7f13f4 clone)
  python3 -B verifiers/verify_corpus_integrity.py --json              -> exit 0 at ac9f295, at 14ab415; exit 1 at b7f13f4, abd8e5c
  python3 -B verifiers/check_tip_battery.py --rev b7f13f4…             -> "guards 5 of 5; tip battery exit 0: 4 of 6" EXIT=1 (scratch clone, fleet-shaped)
  python3 -B verifiers/check_tip_battery.py --rev b7f13f4…             -> same, EXIT=1 (real fleet /home/vgpnk/Projects/shokunin)
  python3 -B verifiers/check_tip_battery.py --rev 1c68cc3d…            -> "FAIL guard instrument-pin: verifiers/check_assertion_floors.py blob
                                                                     6095c9f4… is not a pinned blob"; guards 4 of 5; EXIT=1 (scratch clone,
                                                                     one-byte floors edit)
  python3 -B verifiers/check_spec_craft.py --rev ddeb8ee…             -> "spec craft pages backed 3 of 3" exit 0 (scratch clone + one § Body craft row)
  python3 -B verifiers/check_sources_append_only.py --base 422ffd10… --rev <S213-anchor-edit>
                                                                     -> "breach 142211d2e S213 anchor" ; "6 change(s) in 5 of 29 commits" EXIT=1
  python3 -B verifiers/check_sources_append_only.py --base 422ffd10… --rev b7f13f4…
                                                                     -> "5 change(s) in 4 of 28 commits" EXIT=1 (already red at base)
  python3 (yaml) fold-render extraction matrix on HEAD SKILL.md          -> split('---')[1]=1022 ;
                                                                       regex group(1)=1021 ; lines[1:end]+NL=1022 ; lines[1:end]=1021
  python3 (yaml) first-sentence matrix                                -> 151 (up to and incl. first ". ") ; 150 (without ".") ; 57 (naive split('.')[0])

No installs were performed; no tool was added. No lane file was modified by this seat (the
working-tree D4 change in verifiers/check_assertion_floors.py and verifiers/floors-registry.json
was already present when I arrived — not mine; I did not touch it). No git/jj write was performed.
Scratch removed at yield.

VERDICT: 3 findings — 1 blocking (Q73 sweep conclusion false; D4 floors bump breaks the
check_tip_battery instrument-pin guard, guards 5/5 -> 4/5, tip-battery exit 1, and
verifiers/check_tip_battery.py is in no Touch-list slot), 1 material (the committed base-battery
receipt's corpus-integrity exit=0 and corpus-independent exit=0 claims are FALSE at base b7f13f4;
both gates exit 1 there, which makes C2's R2 "reading green" precondition unsatisfiable as
written), 1 material (four predicate-sentence drifts breaking Q26 byte-identity, incl. the
addendum-rewritten conjunct (a) still contradicted by the frozen B06/A02 seat prompts).
