# ScribeEntryCheck — `g7-span-closure-round65` entry vs the receipts

Seat: scribe, round 65 wave 1 (2026-10-24). Target of the audit:
`corpus/knowledge/g7-span-closure-round65.md`, committed bytes at `0e104f49`
(sha256 `3fc69bca147fe09c6c08632258807a74d430818dc7f511f2a42d24969462ac19`,
identical to the working file), with the row it cites (`corpus/SOURCES.md:132`)
and the receipts it names.

Lane bounds respected: read-only on the lane and fleet repos (only `git
cat-file` / `git archive` / `git ls-tree` / `git log` reads, no jj command at
all); the only lane write is this report; all scratch under `/tmp` (four
processes max, every run well under 120 s); no subagent dispatch; no package
installed or upgraded (nothing was needed — `python3`, `git`, `curl`, `pdfinfo`
were pre-installed).

## Verdict

| Check | Result |
|---|---|
| Provenance trio (`source:` / `verified-at:` / `recheck:`) present | **YES**, L1–L3, same shape as the r64 entry |
| Every command quoted in the entry has a receipt with matching output | **YES** (`--self-test`: `C1-close-measure.txt`; kill battery: `C1-close-kill.txt`), reproduced byte-identical |
| § The measured record matches `C1-close-measure.txt` | **YES**, 6/6 lines, in order (two presentational nits, E6) |
| S121 anchor cells match the row | **YES** on every cell; the row's *own* locator cell is wrong (E2) and its page range disagrees with the artifact's own stamps (E3) |
| Entry claims supported by receipts | all counting claims reproduce; **one disposition is falsified** (E1, M11) and one conformance sentence is not satisfied (E4, Q47) |

## 1. Provenance trio

```
$ nl -ba corpus/knowledge/g7-span-closure-round65.md | sed -n '1,3p'
1  source: S121 — Madeyski, Orzeszyna, Torkar, Józala, … DOI 10.1109/TSE.2013.44
   (from the opened PDF's header line 90); … committed snapshot … sha256 `bad1b681…`) …
2  verified-at: 2026-10-24 — tip `80bb8921`, v32 sha256 `b6cfc764…`: `self-test:
   0 failure(s) over 234 assertions`, exit 0 (re-run on committed bytes via `git
   archive`, receipt `.ufo/waves/round-65/receipts/C1-close-measure.txt`); the span
   branch at `verifiers/check_scoped_rules_v32.py:1055-1067`
3  recheck: 180d — `python3 -B verifiers/check_scoped_rules_v32.py --self-test`:
   all printed predicate lines and the assertion count against § The measured
   record; sooner on any mutation reported surviving this branch
```

Trio present and well-formed; `recheck: 180d` equals the row's `180d` cell. The
180d horizon, the branch anchor and the receipt path all resolve. (E9 and E7
are wording nits inside these lines.)

## 2. Commands quoted in the entry, and their receipts

The entry quotes one command, twice (L44, L3):
`python3 -B verifiers/check_scoped_rules_v32.py --self-test`.

It is the first command in `C1-close-measure.txt`:

```
# C1 measure @ 80bb89211841289bc802fa7b55057f0ef266d19e (committed bytes via git archive)
$ python3 -B verifiers/check_scoped_rules_v32.py --self-test
…
self-test: 0 failure(s) over 234 assertions
exit=0

$ sha256sum verifiers/check_scoped_rules_v32.py
b6cfc7644b609f120f69b638d45d3253f07758f9dfa02e8252e2aeaad2183e8d  verifiers/check_scoped_rules_v32.py
```

Independent re-run, on bytes extracted from the commit (not the live tree):

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
$ git archive 80bb8921 | tar -x -C /tmp/scribe-check
$ cd /tmp/scribe-check && sha256sum verifiers/check_scoped_rules_v32.py
b6cfc7644b609f120f69b638d45d3253f07758f9dfa02e8252e2aeaad2183e8d  verifiers/check_scoped_rules_v32.py
$ python3 -B verifiers/check_scoped_rules_v32.py --self-test; echo "EXIT=$?"
… (world W1–W7 lines, world W0: exit=1, survivor lines) …
worlds reject 7 of 7; eligible rows pass 4 of 4
survivors closed 6 of 6
must-fail E2e guard disabled admits e2e-negated-path-key: yes
must-fail G7 disabled admits e2f-backticked-event-claim: yes
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
self-test: 0 failure(s) over 234 assertions
EXIT=0
```

Line-for-line diff of the receipt's command + 20 output lines against this run:
**identical** (the receipt's `exit=0` is my `EXIT=0`, same value). The
`(sha256, 234)` pair is therefore reproduced from the named commit's bytes:
`b6cfc764…` and `234`.

Kill battery: re-run from the archived rev in `/tmp`, not the lane:

```
$ for f in check_scoped_rules_v32.py check_erratum_absorption.py check_scoped_rules.py; do
    git cat-file -p 80bb8921:verifiers/$f > /tmp/scribe-kill/tree/$f; done
$ cd /tmp/scribe-kill/tree && sha256sum check_scoped_rules_v32.py
b6cfc7644b609f120f69b638d45d3253f07758f9dfa02e8252e2aeaad2183e8d  check_scoped_rules_v32.py
$ time python3 -B ../kb.py            # kb.py = receipts/kill_battery.py, only TREE re-pointed
real 0m8.021s
…
RESULT: ALL OK
KILL_EXIT=0
```

Diff of my run against `C1-close-kill.txt` body (after its two wrapper header
lines): **identical except the receipt's trailing `harness_exit=0` annotation**,
which my shell reported as `KILL_EXIT=0`. Every lane line, every FAIL excerpt,
the baseline, the equivalents, the control world and `RESULT: ALL OK` reproduce.
(Flat-tree reproduction needs the two sibling modules the self-test imports:
`check_erratum_absorption.py` and `check_scoped_rules.py` — recorded so a
rechecker does not read the first `FileNotFoundError` as a red.)

## 3. § The measured record vs `C1-close-measure.txt`

Fence L47–L54, six lines. All six are present in the receipt, in the same
order (scripted check: `ordered-subsequence: True`). Tolerances:

- L53 adds `# exit 0` inside the quoted block; the receipt prints `exit=0` on
  its own line. Value agrees, verbatim form does not.
- The fence is a selective excerpt: `world W1: … W0: exit=1` and the six
  `survivor …` lines sit between `worlds reject …` and `survivors closed 6 of 6`
  in the receipt and are elided without an ellipsis marker.

No line in the fence is absent from, or different from, the receipt's text.

## 4. S121 anchor cells: entry vs row vs the opened artifact

Row under test: `corpus/SOURCES.md:132` (byte-identical at `0e104f49` and in
the working tree; verified with `cmp` of the single row line).

| Cell | Entry (L1) | Row | Artifact (`snapshots/S121.txt`, `S121.pdf`) | Verdict |
|---|---|---|---|---|
| Authors/title | Madeyski, Orzeszyna, Torkar, Józala; full title | same | title lines 3–5, authors line 6 | agree |
| Venue/date | IEEE TSE 40(1):23-42, Jan 2014 | same | line 1 `VOL. 40, NO. 1, JANUARY 2014 (PREPRINT V.2)`, page mark `23` at line 3 | agree (see E3 for the end page) |
| DOI | `10.1109/TSE.2013.44`, "PDF's header line 90" | "from the PDF header line 90" | line 90 `Digital Object Identifier no. 10.1109/TSE.2013.44` | agree |
| Abstract anchor | "PDF text line 64" | "PDF text line 64" | gate quote starts on line 64 (`… The experiment indicated that SOM in general and JudyDiffOp strategy`), continues 65 | agree |
| HOM paragraph anchor | "lines 1174-1176" | "§5 … (PDF text lines 1174-1176)" | support quote at 1174–1176 exactly | entry↔row agree; **row's `§5` is wrong** (E2) |
| Snapshot | `.ufo/waves/round-65/snapshots/S121.pdf`, 1,126,684 B, sha256 `bad1b681…` | same, full digest | `stat` 1,126,684 B; `sha256sum` `bad1b681b1d6…a07418a3`; committed blob at `0e104f49` hashes to the same sha256 (`git cat-file -p … | sha256sum`) | agree |
| Extracted text | `S121.txt` | `S121.txt` | 110,736 B, sha256 `475818a5…`, committed and identical | agree |
| S120 cross-cite | "S120 (the round-64 pinning-method source)" | S120 row cites `corpus/knowledge/g7-span-pinning-round64.md` | r64 entry's `source:` line is S120 | agree |
| Internal evidence | `MutW2M7M22` §5/§8 | — | §5 = M20; §8a = span-iterator; §8b = M11 | agree |

Quote support for the entry's only substantive S121 use ("coupling two
first-order sites … measured to reduce equivalent mutants and test effort"):
S121.txt lines 1110–1117 — "The most promising technique … seems to be higher
order mutation (HOM) … and second order mutation (SOM) in particular. SOM has
potential advantages … e.g. reducing the number of equivalent mutants [30],
[57], [63] and reducing test effort (testing time)". The entry's sentence stays
inside the row's stated scope ("the lane's two-span verifier arm is the lane's
application, not the paper's object") and L1 says the arms' receipts rest on
v32's bytes, not on S121.

## 5. Kill battery: entry's attribution table vs the receipt

The entry's table (L56–L63) was checked lane by lane against
`C1-close-kill.txt` and against my re-run:

- "SM1←arm 1 of the round-64 four, SM2←arm 3, SM3←arm 2, SM5←arm 4 (own
  labels)": the four landed arms appear in that document order
  (`git cat-file … | grep -n 'check("A2 G7'`: 2133, 2139, 2147, 2155), and the
  first FAIL line of each lane names the matching arm. Agree.
- SM4 first via the M17 prefix arm; SM6 first via the pre-existing A2 cell arm:
  agree on first lines (see E8 for the parenthetical).
- M7/M8/M9/M10/M12/M17 each by their own package arm; M14 by the M12 arm:
  agree, first FAIL line in each lane names that arm.
- SPAN_FIRST and SPAN_LAST by their own new arms; M20 by its own new arm:
  agree.
- M11 "by pre-existing collateral with the new arm FAILing as witness": true
  **of the receipt's M11 mutant** — see E1, where the lane the entry cites is a
  different mutation and the arm is its first and only kill.
- "17 named lanes red": 17 kill-set lanes at `exit=1` (SM1–SM6, M7–M10, M12,
  M17, M14, SPAN_FIRST, SPAN_LAST, M20, M11); plus the one control lane
  (`control+M11`, `exit=1`) and 7 `exit=0` lanes. Agree.
- Equivalents M19/M22 green; pkg7 control 230 assertions admitting
  SPAN_FIRST/SPAN_LAST/M20: agree, all reproduced.
- "the six package arms … byte-exact" (L13): scripted comparison of
  `RevC1Predicate` §3's two python fences against the committed file — 52 of 53
  non-empty lines present verbatim and in order; the one absent line is the
  comment `# --- proposed closing arms (RevC1Predicate) ---` (not an arm).
  Claim holds for the arm code.
- Floors registration (L5): `C1-close-measure.txt` has no floors line, but
  `receipts/FLOORS-after.txt` prints `PASS scoped_rules_v32 observed=234
  floor=234` and `exit=0`, `FLOORS-noharm.txt` repeats it at `0e104f49`, and the
  frontier's `floors-registry.json` row is `{"floor": 234, "path":
  "verifiers/check_scoped_rules_v32.py"}` with both in-file guard tables at
  234. Claim holds at the frontier rev (HEAD has moved to 240, round 66).

## 6. Findings (severity ordered)

### E1 — HIGH — the M11 disposition is falsified for the lane the entry itself cites

Entry text under test:

- L39–40: "The arm is a named witness — the M11 lane dies on the pre-existing
  main-world arms first (F7 attribution), in every world."
- L62–63: "M11 by pre-existing collateral with the new arm FAILing as witness."
- L75–77 (Limits): "The M11 arm never becomes the first kill … it does not
  carry the lane today".
- L5 (landing note): "the M11-exact-case arm is a named witness only, the M11
  lane being killed first by pre-existing main-world collateral".

The M11 lane the entry cites is `MutW2M7M22` §2/§8b: mutation "`supported(word,
…)`", i.e. dropping `.lower()` on the call argument in the span branch
(committed `verifiers/check_scoped_rules_v32.py:1061`,
`and not supported(word.lower(), page_words(raw_page))`). I built exactly that
mutant on the landed bytes and ran it, and the pkg7-equivalent control world:

```
$ cd /tmp/scribe-kill/tree   # v32 sha256 b6cfc764…, absorption+counter siblings from 80bb8921
$ python3 - <<'PY'
old = "supported(word.lower(), page_words(raw_page))"      # occurrences: 1
new = "supported(word, page_words(raw_page))"              # MutW2M7M22 §2 M11
# (a) landed 234 bytes + M11: run; (b) pkg7 control (the harness's own slicing) + M11: run
PY

== M11-callsite-unlower (landed 234): exit=1 fails=1
    FAIL A2 G7: a capitalised span word present on the page only as an exact-case token is not rejected: got True, expected False
== CTRL-baseline (230): exit=0 self-test: 0 failure(s) over 230 assertions fails=0
== CTRL+M11-callsite (230): exit=0 self-test: 0 failure(s) over 230 assertions fails=0
```

Two-sided result on the landed bytes: the §8b lane **survives the control world
without the new arms (230, exit 0)** and **dies on the landed suite by the new
M11 arm alone — first and only FAIL (234, exit 1)**. The new arm is therefore
the load-bearing pin for that lane, not a witness; "never becomes the first
kill" and "does not carry the lane today" are false as written.

What the receipt actually measures under the `M11` label is a *different*
mutant: `kill_battery.py` mutates the body of `page_words()`
(`return {w for w in CONTENT_RE.findall(t) if …}` — `.lower()` dropped for
every caller), which breaks the eligible-world fixtures, so it dies by
pre-existing main-world collateral. That collateral kill is reproducible (I
re-ran it: candidate `exit=1`, 7 failures, first `FAIL A2: a cell the cited
line supports passes`; control `exit=1`, 6 failures, no new-arm label first).
The defect is the entry's generalization from the harness's chosen mutation
site to "the M11 lane … in every world", and the "third load-bearing pin"
count in the landing note (L5) is an undercount: there are four.

Recommendation: record the M11 arm as a load-bearing pin for the §8b lane
(control-world survival + first-kill evidence above), and either keep the
harness's `page_words`-body mutant as a separate "M11-body" lane or replace it
with the §2 call-site mutant, which the arm kills directly. The plan's kill
conjunct ("M11-upper exits 1 … with a FAIL line attributed to its pin arm") is
in fact *better* satisfied by the call-site mutant than by the receipt's lane.

This falsifies: C1 landing note "the M11-exact-case arm is a named witness
only"; L39–40 and L75–77. It weakens (does not falsify) the receipt's kill
table, whose numbers reproduce exactly.

### E2 — MEDIUM — the row's S121 locator cell names the wrong section (entry inherits the label)

Row cell: "§5 HOM-generation strategies paragraph (PDF text lines
1174-1176)". The artifact's structure:

```
$ awk 'NR>=1124 && NR<=1129 {print NR": "$0}' snapshots/S121.txt
1124: …
1126: 4
1127:
1128: Higher order mutation testing strategies
$ awk 'NR>=1463 && NR<=1468 {print NR": "$0}' snapshots/S121.txt
1465: 5
1466:
1467: Experimental setup
```

The Polo/SOM paragraph (support quote at 1174–1176) sits in **§4 "Higher order
mutation testing strategies"**; §5 is "Experimental setup". There is no heading
"HOM generation strategies" anywhere in the extracted text (the only
`Generation Strategies` string is the figure label at line 45). The knowledge
entry does not repeat the section number, but L1 repeats the label
("the HOM-generation-strategies paragraph (lines 1174-1176)"); the line anchor
is correct. Row defect; the entry's label paraphrase inherits it without the
section number. Suggested fix:
"§4 Higher order mutation testing strategies, PDF text lines 1174-1176".

### E3 — MEDIUM (anchor/artifact) — citation page range 23-42 vs the artifact's own 22 pages stamped 23-44

```
$ curl -sS 'https://api.crossref.org/works/10.1109/TSE.2013.44' | …
volume: 40 issue: 1 page: 23-42 published-print: 2014-01
$ pdfinfo snapshots/S121.pdf | grep Pages
Pages:           22
# per-form-feed page stamps in S121.txt: 23,24,…,42,43,44 (22 chunks)
```

The entry's and row's `40(1):23-42` matches the publisher record (Crossref), so
the citation is correct; the opened author-hosted preprint's own pagination runs
23→44 (22 pages). [INFERENCE] the preprint's layout paginates two pages past
the published range. No anchor in the entry depends on the end page, but a
rechecker who verifies "23-42" against the snapshot finds 22 pages; the row
should either cite Crossref explicitly for the range (it does for the DOI only)
or note the preprint's 23–44 stamps.

### E4 — MEDIUM — the "Two-sided measure per Q47" sentence is not satisfied as written

L63–66: "Two-sided measure per Q47: the semantics-preserving equivalents M19 …
and M22 … both survive green on the landed bytes, and the set is not a fixed
published list — the witnesses are generated from the branch's own filters."

`corpus/QUALITY.md` Q47: "A mutation-kill measure is two-sided (every declared
mutant killed AND every semantics-preserving equivalent survives) and **its
equivalents** are not a fixed published list: a fixed list is a label a
self-test can key on, so the set is generated at measurement time or **the
measure stays a record, never a claim**."

- Q47's object is the *equivalents* set, not "the witnesses".
- The receipt's equivalents are a fixed two-element list hard-coded in
  `receipts/kill_battery.py` (`SURVIVE = ["M19-sorted-list", "M22-L-guard"]`,
  with the two replacements also literal), and the entry names them.
- No committed generator for witnesses or equivalents exists in the round-65
  receipts; "generated from the branch's own filters" has no receipt.

By Q47's letter the two-sided measure here is a **record, not a claim**, unless
a generator is committed. Either downgrade the sentence or land the generator
and cite it. (The two-sided *result* itself is real — both directions reproduce;
the defect is the conformance sentence.)

### E5 — LOW — the v31 do-nothing number has no round-65 receipt

L71: "the v31 predecessor prints `survivors closed 5 of 6` over 201
assertions." No file under `.ufo/waves/round-65/receipts/` contains that run;
the only committed receipt is `.ufo/waves/round-62/C1-v31-successor.txt`
(`survivors closed 5 of 6`, `self-test: 0 failure(s) over 201 assertions`,
`exit=0`). I re-ran v31 at the measured rev
(`verifiers/check_scoped_rules_v31.py`, sha256 `a07c2269…`, same bytes at
`80bb8921` and the working tree) and got exactly those two lines at `exit=0`,
so the claim is true — but it is asserted in prose with no round-65 receipt
(Q50: another revision's receipt is not tip evidence). Cheapest repair: add the
four-line v31 run to `C1-close-measure.txt` (or cite the round-62 receipt path
in the sentence).

### E6 — LOW — quoting nits in § The measured record

L53 carries `# exit 0` inside the quoted fence (the receipt's `exit=0` is a
separate line), and L47–L54 elides the world/survivor detail lines without an
ellipsis. Every quoted line matches. Note also that `C1-close-measure.txt`
asserts "committed bytes via `git archive`" in its header but shows no archive
command; the procedure is documented in `kill_battery.py`'s header
(`git archive <rev> | tar -x -C /tmp/tree …`) and I reproduced it, so the
provenance step is true but receipt-asserted rather than receipt-shown.

### E7 — LOW — branch anchor is wider than the branch

L2: "the span branch at `verifiers/check_scoped_rules_v32.py:1055-1067`". At
the measured rev the `span_missing` construction is 1055–1061
(`span_missing = sorted({ … and not supported(word.lower(), page_words(raw_page))})`),
1062–1064 is the identifier branch, and 1065–1067 is the span report. A tighter
anchor is 1055–1061 (or 1055–1067 if deliberately covering the report); not
falsifying.

### E8 — LOW — SM4 attribution parenthetical is non-exhaustive

L58–59: "SM4 first via the M17 prefix arm (then the pre-existing `eligible
world` lines)". The receipt's SM4 lane prints the M17 arm first, then the M20
arm, then the M11 arm, then the `eligible world` lines. The "first" claim is
correct; "then the pre-existing … lines" skips two intervening FAILs.

### E9 — LOW — "tip 80bb8921" names the measured rev, not the tip at landing

The entry does not exist at `80bb8921` (`git cat-file -p
80bb8921:corpus/knowledge/g7-span-closure-round65.md` → "exists on disk, but not
in '80bb8921'"); it first appears in `0e104f49`, the round's frontier. The r64
entry uses "base `078eec4`" for the same slot. No factual error about the bytes
(they hash to `b6cfc764` at both `80bb8921` and `0e104f49`), but "tip" is
ambiguous — "measured at" would be exact.

### E10 — LOW — the harness's automated attribution is weaker than "per-arm attribution" reads

`kill_battery.py` asserts a lane's expected label is present *anywhere* in the
output (`if want and want not in out`), and prints only the first four FAIL
lines; first-kill ordering is therefore read off the printed excerpt by the
operator, not machine-checked. The receipt's excerpt does support every "first
via" claim in the entry, but the wording "with per-arm attribution" should not
be read as a machine-verified ordering.

## 7. Conflicts with sibling wave-1 seats (verbatim, for the canonical judge)

`RevReceiptRevs.md` §4 (round-65 w1) accepts the M11 collateral attribution:

> "`RESULT: ALL OK`, `harness_exit=0` — arithmetically consistent with the
> SCORECARD's conjunct and with `MutW2M7M22` F7 (M11 killed by pre-existing
> collateral in every world)."

and its F7 asks only that the label `M11-upper` be made greppable. My E1
measurement conflicts with the parenthetical: for the lane `MutW2M7M22`
§2/§8b defines, the new M11 arm is the first and only kill (234, `exit=1`) and
the lane survives the 230 control (`exit=0`); the collateral kill is a property
of the harness's differently-mutated `page_words`-body lane. E1 is the stronger
statement; the sibling's arithmetic (17+1+7 lanes) is reproduced and not in
dispute.

`ScoutS121Reopen.md` agrees on every S121 anchor cell and records
"[INFERENCE] IEEE TSE 40(1):23-42 publication metadata comes from the PDF
header/preprint itself"; it did not assert the §5 locator or the 22-page
pagination. E2/E3 are additions, not disagreements.

## 8. Claims supported / falsified

Supported (reproduced from the named rev's bytes):
- C1 counted predicate at `80bb8921`: `worlds reject 7 of 7; eligible rows pass
  4 of 4`, `survivors closed 6 of 6`, all three must-fail lines, `0 failure(s)
  over 234 assertions`, exit 0, instrument sha256 `b6cfc764…`.
- `223 → 234` (`controls/C1-before.txt` at `c98d137` prints 223,
  `f8f69cada…`); `+11` = 6 package arms + 1 wrapper + 4 new arms.
- 17 named kill lanes, each red with its arm's label in the first printed FAIL;
  M19/M22 green; pkg7 control at 230 admitting SPAN_FIRST/SPAN_LAST/M20;
  `control+M11` red carrying no new-arm label first.
- Floors registration at 234 (`FLOORS-after.txt`, `FLOORS-noharm.txt`,
  `floors-registry.json` and both guard tables at `0e104f49`).
- Six package arms byte-verbatim from `RevC1Predicate` §3 (52/53 lines; the
  absent line is its comment); wrapper arm body as quoted; the four new arms'
  witnesses match `MutW2M7M22` §8a/§5/§8b descriptions.
- S121 anchors: snapshot bytes/digest/committed blob, extracted text digest,
  DOI line 90, abstract line 64, support quote 1174–1176, venue/date, authors.
- v31 predecessor at the measured rev: `survivors closed 5 of 6`, 201
  assertions, exit 0 (reproduced; receipt path missing — E5).

Falsified:
- C1 landing note (L5) "the M11-exact-case arm is a named witness only …";
- L39–40 "the M11 lane dies on the pre-existing main-world arms first … in
  every world";
- L75–77 Limits "never becomes the first kill … does not carry the lane today".
  (All three: E1. The arm is the load-bearing pin for the `MutW2M7M22`
  §2/§8b lane.)

Not satisfied as written:
- L63–66 "Two-sided measure per Q47 … not a fixed published list" (E4).

Row defects surfaced by the entry audit:
- `corpus/SOURCES.md:132` "§5 HOM-generation strategies" (E2);
- page range vs the preprint's own 22 pages (E3).

## 9. Scratch, hygiene, tooling

- Scratch: `/tmp/scribe-check` (git-archive tree at `80bb8921`, `rerun.txt`),
  `/tmp/scribe-kill` (`tree/` with the three verifier modules from
  `80bb8921`, `kb.py` = the receipt harness with only `TREE` re-pointed,
  `out.txt`), `/tmp/scribe-check/S121-at-frontier.txt` / `S121-working.txt`
  (row comparison). Nothing outside `/tmp` was written except this report.
- Lane bytes touched by nobody: live `verifiers/check_scoped_rules_v32.py`
  sha256 `97d89716…` (round-66 working tree, unchanged by me),
  `corpus/knowledge/g7-span-closure-round65.md` `3fc69bca…`,
  `corpus/SOURCES.md` `02d643da…` before and after every run.
- The kill battery writes its candidate in place; it was run only inside
  `/tmp/scribe-kill/tree`, never in the lane (the harness's own rule).
- No git/jj write: only `git cat-file`, `git archive`, `git ls-tree`,
  `git log`, `git rev-parse`. No jj command was run (a jj command would
  snapshot the working copy).
- Network: one read-only Crossref GET for the DOI's page range.
- Tooling: no install or upgrade (pacman pause untouched); `pdfinfo`, `curl`,
  `python3`, `git` were already present.

Report: .ufo/waves/round-65/w1/ScribeEntryCheck.md
