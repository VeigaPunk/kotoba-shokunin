# RevW2Entry — C1 knowledge entry (`corpus/knowledge/g7-span-pinning-round64.md`) at c019919c

Seat: wave-2 falsify, one seat, leaf. Read-only outside this file; scratch in `/tmp`.
Tip context: `git rev-parse HEAD` = `b99fb79c27042e0f8a598cbbb4d81479a806b518`; the entry is
**unchanged** between the measured tip and HEAD (`git diff --stat c019919c HEAD -- <entry>` empty,
blob `82f6e52d2689cb41c3af1e61ad6c85fef70e57db` at both). No tool installed; pacman untouched.

**Verdict: the counted predicate and every pin I could re-run reproduce; the entry has one
record-accuracy defect that its own cited receipt falsifies, plus two checkability defects and
four citation-precision defects.** No finding breaks the declared predicate (`223`, exit 0,
`(sha256,223)` receipt, all six SM mutants exit 1).

## What reproduced (positive verification)

```
$ python3 -B verifiers/check_scoped_rules_v32.py --self-test | tail -1
self-test: 0 failure(s) over 223 assertions
$ python3 -B verifiers/check_scoped_rules_v32.py --self-test >/dev/null 2>&1; echo rc=$?
rc=0
```
Four frozen lines present and identical to the entry: `worlds reject 7 of 7; eligible rows pass 4 of 4`
/ `survivors closed 6 of 6` / `must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes`
/ `self-test: 0 failure(s) over 223 assertions`.

- Landed counter sha256 `f8f69cada703c8d821690fe01539b433afb7e92e9cdf1752b3365745a7d1113d`, identical to
  `C1-span-measure.txt` and `C1-span-kill.txt`. Diff `078eec4..c019919c -- verifiers/check_scoped_rules_v32.py`
  is **+34 lines, 0 deletions, exactly four `check(` calls** appended at v32:2131-2161 → the 219→223 delta is
  correctly attributed.
- Before-state at base, extracted with `git archive 078eec4 verifiers | tar -x -C /tmp/base_verif`:
  sha256 `12d093a1cdbba4e0c57437e79bc1121708f522f84f81d00a4343bbbbf4c70f43`, `self-test: 0 failure(s) over
  219 assertions`, rc=0. Matches `verified-at:`.
- `grep -c 'A2 G7:'` = **7** at the tip, **3** at base — the entry's stated counts.
- SM1 on the base bytes (branch body replaced by `span_missing = []`): rc=0,
  `self-test: 0 failure(s) over 219 assertions` → survives; the evasion cell
  `The configuration stores project rules using glob syntax and \`exfiltrates credentials\`.`
  is **ADMITTED** (`action_conjunct` → `[]`, `g7_conjunct` → `[]`). The entry's central claim holds.
- Snapshot: `wc -c` = 571600, sha256 `15963c3e67b577182fb40318960ca654d70951ddc8827529de82d7f563cc79e8`.
  §1 quote at line 324 verbatim (`However, code coverage alone might be misleading, in particular` /
  `when program statements are covered but the expected program outcome is not asserted` / `upon <cite>[2],[3]</cite>`),
  and the §3.2.2 sentence begins at **line 780**.
- Code claims: `content_words()` strips backticked spans (v32:1008-1012); `action_conjunct` runs A2 page
  containment before `g7_conjunct` (v32:1151-1180); `supported()` uses `SUPPORT_PREFIX = 4` (v32:354,1035);
  `STOPWORDS` contains `because` and `otherwise`; `span_missing` at 1055, `return []` at 1068 → the entry's
  `:1055-1067` vs plan `:1055-1068` distinction is accurate.
- Arms 1–3 at v32:2133-2152 are byte-identical to `MutW2V32.md` §11. Arm 4's wrapper witness reproduces
  exactly: landed `action_conjunct` → `[]`, SM5 → `['A2 G7: backticked span word(s) mode occur in neither
  the cited line nor the committed snapshot']`.
- §11-attributed numbers check against §11 text: `landed_plus_spanfix7` sha `ae84673e…`, 223 assertions,
  `sib_M1..M8 … KILLED (all nine)`, `4 of 4`, `committed == LANDED+4assertions: True`.
- Entry is indexed (`corpus/README.md:114`); `MutW2V32.md` exists at c019919c
  (`git cat-file -e` rc=0); the entry itself is committed at c019919c.

## Findings (by severity)

### 1. HIGH — SM6's kill is misattributed; the entry contradicts its own cited receipt

Entry locations: line 5 (landing note), lines 67-68 ("kill rule"), line 85 (measured-record table),
lines 106-108 (`Limits`).

- entry:67-68 — “SM4 and SM6 are red only through `FAIL eligible world: the four counted rows are backed`”
- entry:85 — `| + the four arms | 223 | 0 | … | red (eligible world) | … | red (eligible world) |`
- entry:106-108 — “SM4 and SM6 are killed by the eligible-world arm, not by any of the four; the page-check
  and always-fires semantics of the branch still have no G7 arm.”

The committed receipt the entry cites for the landed pair, `.ufo/waves/round-64/receipts/C1-span-kill.txt`,
already lists a **G7** FAIL line for SM6:

```
SM6_branch_always_fires: exit=1 | FAIL A2: a cell the cited line supports passes: got ['A2 G7: backticked span word(s)  occur in neither the cited line nor the committed snapshot'], expected []; FAIL A2 G7: a backticked span made only of stopwords is not rejected: got True, expected False
```

The receipt truncates each mutant's FAIL list to its first two lines (SM4's full run has five), which hid
the rest. Re-running the same mutation (`if span_missing:` → `if True:`) on a `/tmp` copy of the landed
bytes (sha `f8f69cad…`, verified above) gives **ten** failures, three of them G7 arms:

```
$ python3 -B verifiers/check_scoped_rules_v32.py --self-test   # SM6 mutant, landed bytes
FAIL A2: a cell the cited line supports passes: got ['A2 G7: backticked span word(s)  occur in neither the cited line nor the committed snapshot'], expected []
FAIL A2 G7: a backticked span made only of stopwords is not rejected: got True, expected False
FAIL A2 G7: a backticked span word shorter than four characters is not rejected: got True, expected False
FAIL A2 G7: a backticked span word present in the cited line is not rejected even when the page lacks it: got True, expected False
FAIL eligible world: the four counted rows are backed: got [], expected ['Claude Code', 'Copilot CLI', 'Cursor', 'VS Code']
… (10 failure(s) over 223 assertions), rc=1
```

At the r63 bytes the same mutation's first red line is `FAIL A2: a cell the cited line supports passes`
(rc=1, 7 failures over 219), so the table's r63 cell for SM6 (`red (eligible world)`) is incomplete too.
By contrast **SM4's attribution is correct**: my SM4 re-run on the landed bytes is red **only** through
`FAIL eligible world` (5 failures, all `eligible world`/predicate lines).

Consequence: (a) “SM6 … red only through `FAIL eligible world`” and “not by any of the four” are false;
(b) the `Limits` sentence “the page-check and **always-fires** semantics of the branch still have no G7 arm”
is false for always-fires — arm 2 (stopwords negative witness), and also arms 3 and 4, kill it. The
teaching claim “red is not discriminating” survives only for SM4. The entry under-claims protection that
its own receipt demonstrates, in a knowledge entry whose subject is kill-witness attribution. No predicate
failure follows (all six mutants still exit 1; the `(sha256,223)` pair, the four lines and exit 0 all hold).
Note `SCORECARD.md:375` carries the same wave-1 attribution (“SM4/SM6 via the pre-existing `eligible world`
arms”) — out of my write scope; the L1 may want an append-only repair with the same evidence.

### 2. MEDIUM — the 3 607 divergence figure is presented as measured although this round's own replicate says it is not reproducible

Entry line 101: “over 20 000 random cells SM2 differs on **3 607**”.

`.ufo/waves/round-64/w1/MutSpanArms.md` §5 (wave 1 of this round, committed) measures the same quantity
with two independent generators:

```
| SM2 verdict divergence | 3 567 / 20 000 (17.8 %) | 3 505 / 20 000 (17.52 %) | 3 607 / 20 000 (18.0 %) |
```
and states: “§11's figure (3 607) is **not exactly reproducible** — the generator is not recorded in §11”.

So the bar “every quoted number re-verifiable” fails here: the number is only *attributable* to §11, and the
lane's own replicate disagrees by 40–102 cells. The entry neither cites §5 nor carries the bound. It should
either quote the replicate range (3 505–3 567, same mechanism, same conclusion) or label 3 607
non-reproducible. The non-equivalence conclusion itself is unaffected.

### 3. MEDIUM — the entry's own re-run idiom cannot falsify the frozen predicate

Entry line 121: `python3 -B verifiers/check_scoped_rules_v32.py --self-test | tail -1   # 223 assertions`
(recheck line 3 relies on the same command without the pipe).

`tail -1` discards the verifier's exit status and three of the four frozen lines, while the frozen predicate
is “prints all four lines … and exits 0” (`plans/round-64.md:41-50`). Demonstrated on the SM6 mutant:

```
$ python3 -B verifiers/check_scoped_rules_v32.py --self-test | tail -1
self-test: 7 failure(s) over 219 assertions
pipeline_exit=0          <-- the verifier exited 1
real_exit=1
```

The first command in "How to re-run" should be the bare `python3 -B … --self-test` (as the recheck line's
prose implies); the surface form as written reports success on failure.

### 4. LOW-MEDIUM — the source line carries no URL, against the declared provenance bar

Entry line 1 cites S120 by citation, DOI and arXiv id, but not by URL. The registry row it names carries
`https://arxiv.org/html/2102.11378` (`corpus/SOURCES.md:132`), and the sibling r63 entry embeds its URL
inline (`corpus/knowledge/compound-clause-citation-round63.md:1`). A reader of the entry alone cannot reach
the page; “cites S120” is satisfied only via a second file. Fix: inline the arXiv HTML URL (and keep the
DOI; note the HTML-vs-PDF distinction the row records).

### 5. LOW — §3.2.2 snapshot line anchor is off by one

Entry line 1: “§3.2.2 (`S120.page:S3.SS2.SSS2.p1.1`, line 781)”. The quoted sentence begins at line **780**
(`grep -n 'Equivalent mutants, which are' …` → `780:`); line 781 is its continuation. The entry's own
source row records “lines 780-782” (`corpus/SOURCES.md:132`). The r63 spot-check routed citation imprecision
as a defect class (M95), so an off-by-one line pin in the corpus is worth correcting. The §1 anchor
(line 324) is exact.

### 6. LOW — “texts byte-for-byte as measured in MutW2V32.md §11” is false for arm 4

Entry line 36. Arms 1–3 are byte-identical (§11 vs v32:2133-2152). Arm 4 is not: §11's cell is
`The tool writes mode quota nightly and \`mode quota\`.` with page `The tool writes quota nightly.…`, while
the landed arm (v32:2155-2161) uses the hardened `The tool writes quota nightly and \`mode quota\`.`, per
`MutSpanArms.md` §6. The entry discloses this at lines 5 and 50-55, so the blanket “byte-for-byte” claim
contradicts its own landing note. Fix: “arms 1–3 byte-for-byte; arm 4 hardened per MutSpanArms §6”.

### 7. LOW — “at the judge level too” overstates the measurement

Entry lines 5 and 53. The only committed measurement is through `action_conjunct`
(`C1-span-kill.txt`, “wrapper witness (hardened arm-4 fixture through action_conjunct): landed = [] |
SM5 = […]”), which I reproduced exactly. No `judge()` run on that fixture appears in any receipt, and plan
E3 item 3 itself defers the wrapper-level SM5 witness arm. “At the A2-conjunct (wrapper) level” is what was
measured; `judge()` was not.

### 8. LOW — “MutW2V32 scanned for a committed action cell that trips the evasion and found none” is not located in the named artifact

Entry line 112. MutW2V32 §8 (“Reachability of **the two holes** on the committed corpus”, lines 649-673)
scans for the unpaired-backtick and hyphen-adjacent-`and` holes; its 7-cell replay runs “under pristine and
all four surviving/fixed variants” (the M7/M8 family of §2–§3). §11 (lines 860-1010) reports **no**
committed-cell scan for the span-fabrication evasion; its no-harm comparison is committed vs LANDED vs
LANDED+arms. So the “class was latent” claim is asserted, not backed by the named sections.
[INFERENCE] It may have been intended as §8's replay, but that replay predates the SM battery and does not
include SM1. Cheapest repair: cite §8 explicitly and say the span class was not scanned, or add the scan.

## Residual risk and verification gaps

- `ae84673e…` (`landed_plus_spanfix7`, r63 `/tmp` artifact) is not re-derivable at the tip; only §11's text
  attests it. The same state was independently re-measured this round on the landed bytes (223, exit 0), so
  the claim is sound but the pin is not re-verifiable.
- 3 607 is not reproducible (finding 2); the SM5 divergence figure (0.96 % in MutSpanArms §5) and the
  SM3 figure are not in the entry at all — no over-claim there.
- The two receipts are **not present at c019919c** (`git cat-file -e c019919c:.ufo/waves/round-64/receipts/C1-span-{measure,kill}.txt`
  → rc=128); they were committed at `b99fb79`, one commit after the entry. Their headers name c019919c, so
  the chain closes, but the entry landed before its own evidence. Not counted as a finding under the bar
  (“a named committed artifact” — it is committed), flagged so the L1 can decide whether entry→receipt
  freshness needs its own note.
- I re-ran SM1, SM4 and SM6 on the exact bytes and SM5 through both call sites; SM2/SM3 were taken from §11
  and the receipt, not re-derived.
- Working tree at HEAD shows `.ufo/waves/round-64/receipts/noharm-tip.txt` modified and
  `.ufo/waves/round-64/w2/` untracked — live wave-2 writes, not this seat's; I wrote only this file.
- Recorded unavailability: this seat's toolset exposes no `lsp` device, so `references`/`definition`/
  `diagnostics` could not run and text grep is the literal fallback — it is not presented here as semantic
  proof. Every claim was instead verified by executing the pinned commands, importing the module and calling
  the pinned functions, or byte-level diff/hash.
