# RevReRf — audit of routed repairs R-e and R-f against closure defect 5 and M90

Seat: kotoba-r61-wave-RevReRf (reviewer, leaf — no dispatch). Date: 2026-10-23.
Base: `f3246d1493b60ea1c0d947a19c39f9e08e92f326`. Lane read-only; every command below ran
against committed bytes (`git show` / file reads / the frozen checker with `--rev`); no lane,
fleet, sibling, `.ufo/state`, or jj/git-index file was written by this seat. Scratch: none used.

Scope assigned: audit R-e/R-f (frozen in `plans/round-61.md` §C2 and counted by the committed
`verifiers/check_routed_repairs.py`) against closure defect 5 (`corpus/lessons/round-60-verifier-spotcheck.md`
§7 item 5) and M90 (`corpus/lessons/round-60.md:62`); verify the `&#124;` escape claim; fix the
R-e wording bar and the R-f receipt format; state what the L1 must do at integration for R-f to
be true.

## 1. Verified ground (my own measurements)

### 1.1 The `&#124;` escape claim (S106) — VERIFIED, byte-level

Command (run 2026-10-23, cwd `/home/vgpnk/Projects/shokunin/kotoba-shokunin`, reads only):

```
python3 - <<'EOF'   # extracts S106.page:18 and the entry's Copilot CLI quote cell, compares
import html, re, sys
page = open('.ufo/waves/round-60/snapshots/S106.page', encoding='utf-8').read().splitlines()
entry = open('corpus/knowledge/scoped-rules-round60.md', encoding='utf-8').read().splitlines()
src = page[17]                       # S106.page line 18, 1-indexed
i = src.find('`'); j = src.find('locations') + len('locations')
src_slice = src[i:j]
row = next(l for l in entry if l.startswith('| Copilot CLI |'))
cell = row.split('|')[4].strip()
unescaped = cell.replace('&#124;', '|')
print("unescape(quote) == source slice:", unescaped == src_slice)
print("raw quote with &#124; is literal substring of page line:", cell in src)
m = re.search(r'`(\s+)\|', src_slice);  print("spaces token->pipe in source:", len(m.group(1)))
m2 = re.search(r'`(\s+)\&#124;', cell); print("spaces token->&#124; in entry:", len(m2.group(1)))
p107 = open('.ufo/waves/round-60/snapshots/S107.page', encoding='utf-8').read().splitlines()
q107 = "The CLI searches for `GEMINI.md` files in your configured workspace directories and their parent directories."
ws_join = re.sub(r'\s+', ' ', (p107[24] + ' ' + p107[25]).strip())
print("S107 quote reproduced by dropping list marker and joining 25-26:", q107 in ws_join)
print("S107 quote exact substring of raw line 25 or 26:", q107 in p107[24] or q107 in p107[25])
EOF
echo "exit=$?"; date -u
```

Pasted output:

```
S106.page:18 = '| `.github/instructions/**/*.instructions.md`              | Modular repository instructions, discovered in the standard locations but not intermediate director'
source slice from first backtick through 'locations': '`.github/instructions/**/*.instructions.md`              | Modular repository instructions, discovered in the standard locations'
entry quote cell: '`.github/instructions/**/*.instructions.md`              &#124; Modular repository instructions, discovered in the standard locations'
unescape(quote) == source slice: True
raw quote with &#124; is literal substring of page line: False
run of spaces between token and pipe in source: 14
run of spaces between token and &#124; in entry: 14
entry pipe entity present: True | literal pipe inside quote cell: False
S107.page:25 = '    - **Location:** The CLI searches for `GEMINI.md` files in your configured'
S107.page:26 = '      workspace directories and their parent directories.'
S107 quote reproduced by dropping list marker and joining 25-26 with one space: True
S107 quote exact substring of raw line 25 or 26: False
exit=0
Fri 23 Oct 2026 07:14:24 PM UTC
```

Facts established (these are the S106/S107 shaping facts Q56 must cite):

- **S106**: the entry Quote cell is a contiguous prefix of `S106.page:18` from the token's
  opening backtick through `locations` (it drops the trailing " but not intermediate
  directories."); the source's 14-space run before the pipe is kept byte-for-byte; the one
  pipe inside the slice is written `&#124;` so the entry's Markdown table keeps four columns.
  After entity unescape the quote is **byte-identical** to the source slice; the raw `&#124;`
  form is **not** a literal substring of the page bytes — so "byte-exact" is literally false
  for this quote, exactly as defect 5 says. The counter unescapes it: `quote_why` compares
  `norm(quote)` against `norm_page(page)` and both route through `page_plain`, whose first
  line is `html.unescape` (`verifiers/check_scoped_rules.py:935-941,957-960`) — the entry's
  "(the counter unescapes it)" note (`corpus/knowledge/scoped-rules-round60.md` § Quote
  shaping, S106 bullet) is true.
- **S107**: the Gate-recorded quote (`corpus/lessons/round-60.md:14`, which discloses the
  shaping: "list marker `- **Location:**` and the line break dropped") is **not** a literal
  substring of `S107.page:25-26`; it is reproduced only after dropping the 4-space-indented
  list marker `    - **Location:** ` and folding the line break — i.e. whitespace
  normalization. Defect 5's second fact verified.

Where each fact is disclosed today: S106 → `corpus/knowledge/scoped-rules-round60.md` § Quote
shaping (S106 bullet) and `corpus/lessons/round-60.md:13`; S107 → `corpus/lessons/round-60.md:14`.
The overstating sentence is in the fleet report `.ufo/reports/round-60/kotoba.md:36`:
"… entry quotes **byte-exact**, the three negative pages byte-identical live …". (The
"byte-identical live" half is a different claim — sha256 equality over whole pages, pinned in
SOURCES — and is not the target of defect 5; Q56's scope should stay on quote-equality wording.)

### 1.2 The committed C2 base control — re-confirmed at the plan base

Command + pasted output (run 2026-10-23, read-only):

```
$ git rev-parse --verify f3246d1493b60ea1c0d947a19c39f9e08e92f326^{commit}
f3246d1493b60ea1c0d947a19c39f9e08e92f326
$ python3 -B verifiers/check_routed_repairs.py --rev f3246d1493b60ea1c0d947a19c39f9e08e92f326
R-a count correction: missing
R-b landed-scope names: missing
R-c base-measure pointer: missing
R-d census-after file: missing
R-e byte-exact criterion + M91: missing
R-f controls-ancestry receipt: missing
routed repairs verified 0 of 6
exit=1
$ git show f3246d14…:corpus/QUALITY.md | grep -cF 'byte-exact'   → 0
$ git show f3246d14…:corpus/QUALITY.md | grep -cF 'Q56'          → 0
Fri 23 Oct 2026 07:16:03 PM UTC
```

Matches the committed `.ufo/waves/round-61/controls/C2-base.txt` (`0 of 6`, `base-exit=1`).
R-e is genuinely false at base (neither `Q56` nor `byte-exact` occurs in the base QUALITY blob),
so the fix is shown able to fail — the plan's claim holds; I did not need to trust the receipt.

## 2. R-e audit — Q56 / M91 vs closure defect 5

### 2.1 What the frozen arm enforces (`verifiers/check_routed_repairs.py:95-101`)

```
re_ = (
    "Q56" in quality
    and "byte-exact" in quality
    and lesson is not None
    and "M91" in lesson
)
```

This is a **floor, not the repair**: three substrings and one file's existence. A QUALITY line
reading `Q56: byte-exact` with no criterion, or the checker's own self-test one-liner
`"Q56: byte-exact reserved for literal equality"` (`check_routed_repairs.py:165`), would score
R-e. Per the checker's own docstring and Q31, the substance is the reviewers' job — which is
this audit. The counter is frozen (Q28); it must NOT be edited to chase semantics this round.

### 2.2 The wave draft (ScribeQuality) judged against the bar

`.ufo/waves/round-61/wave/ScribeQuality.md:12` drafts Q56 as:

> | Q56 | Reserve `byte-exact` for literal byte-for-byte equality between the recorded quote and the cited source bytes; when an HTML-entity escape or whitespace normalization is required, describe the result as `quote-equal after documented shaping`, never `byte-exact`. | report, lesson, and knowledge-entry descriptions of quote/source equality | M91 `report-evidence-overclaim` (`corpus/lessons/round-61.md` § Mistakes); round-60 verifier spot-check §7 defect 5 …

Verdict: **close, one gap.** It reserves the word, names both shaping classes, supplies the
replacement phrase, and its grounding cell points at M91 + the spot-check. Gap: the criterion
cell never names **S106 / S107** — the two canonical shaped quotes this round actually shipped.
The assignment bar ("cite the S106/S107 shaping facts") and the house style (Q41/Q46/Q47 embed
the concrete mechanism or command in the criterion cell) both want the facts in the criterion
itself, not one hop away. Also: the draft as shown is truncated before the table's fifth
column; the landed row must carry the trailing `| — |` cell like Q54/Q55 (`corpus/QUALITY.md:65-66`,
append after the Q55 row, before the "Rejections are recorded…" paragraph at :68).

### 2.3 Recommended final Q56 row (supersedes the draft's cell text; everything else identical)

Exact target path: `corpus/QUALITY.md` (append one row after the `Q55` row):

```
| Q56 | Reserve `byte-exact` for literal byte-for-byte equality between the recorded quote and the cited source bytes; a match that required shaping — the S106 quote's `&#124;` pipe escape (unescaped by the counter before comparison) or the S107 quote's dropped `- **Location:**` list marker and folded line break, and likewise any entity unescape, whitespace normalization, or prefix/slice truncation — is described as `quote-equal after documented shaping`, never `byte-exact`. | report, lesson, and knowledge-entry wording that calls a quote or byte comparison exact | M91 `report-evidence-overclaim` (`corpus/lessons/round-61.md` § Mistakes); round-60 verifier spot-check §7 defect 5 (`corpus/lessons/round-60-verifier-spotcheck.md`); shaping facts verified against `.ufo/waves/round-60/snapshots/S106.page:18` and `S107.page:25-26` | — |
```

### 2.4 M91 entry (ScribeQuality draft) — accepted with one binding requirement

The drafted M91 (`ScribeQuality.md:18`) correctly folds the three overstatements (count 32/29,
pointer, byte-exact) with the spot-check citation; the plan defines M91 as the overstatement
class, so the fold is in scope. Binding requirement: the landed `corpus/lessons/round-61.md`
must contain the literal token `M91` — the checker's self-test proves a lesson without it fails
the arm (`empty` fixture → 5 of 6, `check_routed_repairs.py:191-193`), and the reciprocal
Q56↔M91 pointers must both resolve (Q56's grounding cell → the lesson; M91's used-by → Q56).

### 2.5 R-e residual

Even with the strengthened row, the frozen arm cannot tell the full row from the substring
`Q56 … byte-exact`; the L1 must land the full row text of §2.3 (not a token line) and the
residual-review seats must diff the landed QUALITY row against §2.3. Defect 5 is then closed:
the word is reserved, the two shipped shaping facts are named inside the criterion, and the
overstating sentence's successor wording in the round-61 report must use the reserved phrase.

## 3. R-f audit — controls-ancestry receipt vs M90

### 3.1 What M90 routed and what R-f can prove

M90 (`corpus/lessons/round-60.md:62`): `CtlWrongKey`/`CtlInventedAction` were cancelled at the
settle deadline with no committed world, and the build wave was dispatched while controls were
still scoring; fix: "a control seat commits its world and a first receipt before any optional
probing, and the L1 cancels at 45 min". R-f's ancestry receipt proves **commit-DAG chronology**
(controls commit precedes C1 data commit) — it cannot prove **dispatch chronology** (that data
seats were dispatched after controls completed). CriticC1Scope already drew this line
(`.ufo/waves/round-61/wave/CriticC1Scope.md:97,124,133,144`: "A historical ordering violation
cannot be repaired by wording"). The round-61 report must therefore claim exactly what R-f
shows — "the C1 controls commit is an ancestor of the C1 data commit" — and must not write
"controls completed before data seats ran" unless wave-dispatch/watchdog chronology evidence
is independently cited.

### 3.2 The frozen arm is falsifiable-by-cosmetics — established by two sibling seats, confirmed

- `check_routed_repairs.py:103-110`: `rf = ancestry is not None and "merge-base --is-ancestor"
  in ancestry and "exit 0" in ancestry`. No hash syntax, no resolvability, no role binding.
- CriticC2Axis (`CriticC2Axis.md:88-93,101-106`) built the disclaimer world
  `Not executed: merge-base --is-ancestor` / `exit 0` — both tokens present, zero substance —
  and showed `check_repairs()` scores it.
- MutC2 (`MutC2.md:85,328`, finding F3): deleting the `merge-base --is-ancestor` conjunct from
  the production arm **survives** the self-test (m5 SURVIVED) — the frozen counter alone
  accepts any blob containing `exit 0`.

The counter is frozen at the plan commit (Q28: a later change is a second measurement, never
the declared one) — so the cosmetics gap is **not** fixed by editing the checker. It is fixed
at integration by the receipt format below plus reviewer re-runs (the Q31 split).

### 3.3 Required receipt format (what the L1 must land)

Exact target path: `.ufo/waves/round-61/receipts/controls-ancestry.txt`. Full text template —
`<CTL>` = the controls commit (counter v3 + seven world fixtures + world/self-test receipts),
`<DATA>` = the C1 data commit (the `--fetch` measurement receipts), both full 40-hex lowercase:

```
# round-61 R-f / M90 receipt: the C1 controls commit precedes the C1 data commit
# lane: /home/vgpnk/Projects/shokunin/kotoba-shokunin (all commands run in the lane worktree)
# recorded: <date -u>
# <CTL> = control-receipts commit: verifiers/check_scoped_rules.py v3 + .ufo/waves/round-61/worlds/* + self-test/world receipts
# <DATA> = C1 data commit: .ufo/waves/round-61/C1-measure.txt (+ companion fetch receipts)

$ git rev-parse --verify <CTL>^{commit}
<CTL>
$ git rev-parse --verify <DATA>^{commit}
<DATA>
$ git log -1 --format='%H %s' <CTL>
<CTL> <subject>
$ git log -1 --format='%H %s' <DATA>
<DATA> <subject>
$ test "<CTL>" != "<DATA>"; echo "exit $?"
exit 0
$ git merge-base --is-ancestor <CTL> <DATA>; echo "exit $?"
exit 0
$ git merge-base <CTL> <DATA>
<CTL>
```

Why this is unfalsifiable-by-cosmetics (to any reviewer who re-runs):

- **Real hashes**: both hashes must resolve as commits at the measured rev
  (`rev-parse --verify ^{commit}`); invented or foreign-repo hashes fail the re-run.
- **Role binding**: the `%H %s` lines tie each hash to its role; a reviewer confirms `<CTL>`'s
  diff carries the fixtures/receipts (`git show --stat <CTL>`) and `<DATA>`'s carries the C1
  measurement — two old r60 hashes that trivially satisfy ancestry do not survive this.
- **Distinctness**: `--is-ancestor A A` exits 0, so equal hashes would trivially "pass"; the
  `test` line pins CTL ≠ DATA.
- **Argument order**: swapped arguments of `--is-ancestor` exit 1 when DATA precedes CTL; the
  command is spelled out with hashes substituted, so order is checkable, not implied.
- **Positive self-checking output**: `git merge-base <CTL> <DATA>` prints `<CTL>` itself iff
  CTL is an ancestor of DATA and CTL ≠ DATA — the receipt carries output whose bytes must
  equal the recorded control hash, which the disclaimer world of CriticC2Axis has no analog of.
- **Frozen-arm compatibility (trap, see §3.4)**: the transcript emits `exit 0` (space form),
  the literal the frozen arm greps.

Reviewer falsification protocol (post-integration, residual seats): re-run the six commands at
the measured tip in the lane; every output line must match the receipt byte-for-byte except the
header comment block; additionally `git show --stat` both hashes for the role check. Any
mismatch → R-f is not landed, whatever the frozen counter prints.

### 3.4 Integration traps (concrete, would break an honest landing)

1. **`exit 0` vs `exit=0` (HIGH).** The frozen arm greps `"exit 0"` **with a space**
   (`check_routed_repairs.py:107`; the self-test fixture likewise: `"$ git merge-base
   --is-ancestor $CTL $DATA\nexit 0\n"`, `:175-176`). An honest receipt written in the
   `exit=0` style of the census-after file (R-d) **fails** the arm → 5 of 6, C2 exit 1,
   despite real evidence. The receipt MUST emit the space form (`echo "exit $?"`).
2. **Order of operations (HIGH, this is "what the L1 must do for R-f to be true").**
   - Step 1: integrate counter v3 + fixtures + world/self-test receipts; **commit** → this is
     `<CTL>`. M90/plan: nothing `--fetch` before this commit exists ("receipts committed
     before any `--fetch` data measurement, M90", `plans/round-61.md` §C1).
   - Step 2: run the C1 measurement (`--rev <tip> --fetch`); write the measurement receipts;
     **commit** → `<DATA>`.
   - Step 3: run the §3.3 command block in the lane worktree (at or after `<DATA>`), paste
     verbatim into `.ufo/waves/round-61/receipts/controls-ancestry.txt`. The receipt
     necessarily rides a later integration commit (it references `<DATA>`, which does not
     exist before Step 2) — that is correct; what R-f claims is the DAG relation, and the DAG
     now carries it.
   - Step 4: report wording limited per §3.1 (ancestry ≠ dispatch order).
   - Step 5: hand the §3.3 falsification protocol to the residual seats.
   The hashes must be the real landed ones — never regenerated, never shortened, never
   replaced by `HEAD`/branch names (aliases repoint; that is the cosmetics vector).
3. **Don't edit the frozen checker (MEDIUM).** MutC2's surviving mutants (m5, m7) are findings
   about the frozen counter's floor. The repair is the substantive receipt + reviewer re-run,
   not a checker patch mid-round (Q28).

## 4. Findings by severity

- **HIGH — R-f receipt exit-string trap**: frozen arm requires literal `exit 0` (space); the
  house `exit=0` style fails an honest receipt. Format in §3.3 pins the space form.
  Evidence: `check_routed_repairs.py:103-110,175-176`; committed `C2-base.txt` labels.
- **HIGH — R-f is cosmetic-fakeable at the counter floor**: disclaimer world scores
  (`CriticC2Axis.md:88-106`); deletion of the merge-base conjunct survives the self-test
  (`MutC2.md:85`, F3). Closure is procedural, not a checker edit: §3.3 format + §3.4 steps +
  reviewer re-run protocol.
- **MEDIUM — R-f overclaim risk**: ancestry receipt proves commit-DAG chronology only; M90's
  dispatch-order conjunct needs separate chronology evidence or must not be claimed
  (`CriticC1Scope.md:124,133,144`; M90 at `corpus/lessons/round-60.md:62`).
- **MEDIUM — R-e draft gap**: ScribeQuality's Q56 reserves the word but does not name the
  S106/S107 facts in the criterion cell, and must land with the trailing `| — |` table cell;
  final row in §2.3. (Verified base is clean: `Q56`/`byte-exact` count 0 at `f3246d14`.)
- **LOW — R-e lesson-token binding**: `corpus/lessons/round-61.md` must exist and carry the
  literal `M91` at the measured rev; absence fails the arm by design (self-test `empty`
  fixture). L1 must land the full ScribeQuality M91 text, not a stub.
- **INFO — both shaping claims verified true**: S106 `&#124;` escape verified byte-level
  (unescape ⇒ byte-identical contiguous slice; raw form absent from page bytes; 14-space run
  kept; counter unescapes via `html.unescape` in `page_plain`); S107 verified as
  list-marker-drop + line-break fold (`S107.page:25-26`). The r60 "byte-exact" word was false;
  defect 5 is real and correctly routed.

## 5. Residual risk and verification gaps

- The R-f receipt, Q56 row, M91 entry, counter v3, fixtures, and `round-61.md` do not exist
  yet (glob of `.ufo/waves/round-61/`: only `census-before.txt`, `wave/`, `controls/C2-base.txt`,
  `wave-dispatch.json`, `wave-spec.json`); this audit verifies the frozen arms, the ground
  facts, the drafts, and the integration procedure — not the landed bytes. The §3.3 reviewer
  protocol and the §2.3/§2.4 diffs are the post-integration checks.
- The frozen C2 counter cannot judge substance by construction (its own docstring; Q31); my
  "unfalsifiable-by-cosmetics" claim is about the receipt format under the reviewer re-run,
  not about the counter.
- I did not inspect wave-dispatch chronology for the current wave; the single-v2-wave
  co-dispatch is by design and the M90 operating rule binds integration, not the wave.
- Checker `--self-test` was not re-run by this seat (siblings MutC2/ScribeLogScore recorded
  `0 failure(s)`; the arms were read in source); everything I state as measured above carries
  its own pasted output.

Installs: no installs (pacman paused per orchestrator ruling; none needed).
Blockers: none.
Produced: byte-level verification of the S106 `&#124;` escape and S107 shaping claims, the
final Q56 row and R-f receipt format with integration procedure, and the audit of R-e/R-f
against closure defect 5 and M90 — reported at `.ufo/waves/round-61/wave/RevReRf.md`.
