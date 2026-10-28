# Kb80G01Revenge — revenger seat, round 80 w1 (kotoba)

Task: re-derive the r79 C2 rejection myself, then test whether the r80 design
answers it. Base `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`. Nothing in the lane
was edited; every measurement is in a `--shared` scratch clone under
`/fast/scratch/hyaku/kotoba-r80/Kb80G01Revenge` (removed after delivery).

## 0. Bottom line

The r80 design answers the r79 rejection **in form** (it stops resting the claim
on a number a script can reach, prints the generator's score, and moves the
judgement to the non-author closure) but it does **not** answer it in a landable
form: the frozen after-value `documented 6 of 6` is unreachable on the committed
snapshots. The r79 draft counter's Q70 conjunct rejects the only admissible
Microsoft Agent Framework quote because its text view does not recognise HTML
headings, so the honest world caps at **5 of 6** (measured) and the same wall
caps the "generator world" score the plan says is "expected 6". Verdict below.

## 1. The r79 rejection, re-derived

The rule the r79 attempt failed (corpus/QUALITY.md, verbatim):

> **Q74** — "Before admitting a semantic claim whose evidence cells a script can
> populate from page bytes, score an independent mechanical generator that
> writes the complete proposed evidence shape on the same frozen counter; if it
> reaches the target, the counter measures form rather than the claimed
> semantics and the claim is not admitted on that number. The generator is
> separate from the counter's in-file script-only fixture and may not hardcode
> an unreported score."

> **Q71** — "A counter whose cells a script can recompute names, beside its
> target, the measured score of the script-only world scored on the same frozen
> counter; the headline asserts only what that world cannot reach, and a claim
> whose script-only world reaches the target says so in the headline and
> assigns the judgement to named non-author seats."

M79-1 (corpus/lessons/round-79.md § Mistakes) records how r79 got there: its
in-file script-only fixture read `1 of 6`, so the author believed the predicate
was safe; an independent generator (C4) then reached `6 of 6`, exit 0, and the
claim was refused on that number.

**I re-ran the r79 C4 world myself** (their script, their fixed text), against
the same draft counter, in my clone:

    python3 -B .ufo/waves/round-79/build/c2_controls.py \
      --counter $C/verifiers/check_allowed_tools.py --base-tree $C \
      --base-rev b10bcbc6... --work $S/work --only C4 --verbose
    -> === C4 === allowed-tools surfaces backed 6 of 6 ; counter exit: 0
       pre-registered: N in (6,) exit in (0,) — as-expected

That confirms the r79 verdict on its own terms. But their receipt states the
qualification in its own first paragraph — "No network was used by any world
(every page is a fixed synthetic text in c2_controls.py)" — and the replay's
own notes show it ("derived S229: allowed-tools Space-delimited list of
pre-approved tools. Experimental, support may vary…" is a paraphrase, not the
page's bytes: the page says "…Experimental - support may vary…"). So the r79
6-of-6 is a **synthetic-page** result: it proves the counter's shape logic is
mechanically satisfiable, not that the committed evidence satisfies it.

Re-derived independently, on committed bytes, with my own generator (see §2):
the ceiling is **5 of 6**, and the sixth failure is a counter defect, not an
evidence defect (§4). Neither the r80 author nor the wave has noticed this in
the plan text.

## 2. Independent reconstruction of the C4 mechanism (my own generator)

I wrote a generator that does exactly what Q74 describes — writes the complete
proposed evidence shape from the committed snapshots with no judgement — and
scored it on the same draft counter (r80 build had no redesigned counter yet:
see §3.0). Generator: `.ufo/waves/round-80/build/Kb80G01Revenge-gen_c4.py`
(sha256 `b97dd7616bab8516…`). It emits: six 5-cell entry rows under the frozen
header; six 11-cell registry rows (status `mined`, tier A/B, `used-by` = the
entry, anchor with a `fetched … HTTP 200, <n> B, sha256 <hex>` record);
`MANIFEST.sha256` over the committed snapshot bytes; one `PROVINCE.md` `## Core`
bullet; one `SKILL.md` rule line and gate-registry row. The frozen grant label
and page token per surface are read from the counter's own frozen table (that is
the mechanism: they are public constants, not judgements); the quote is a
mechanical 5–25-word window containing `allowed-tools` and the page token; the
value token is the first bare-name word after the field in the text view.

Draft counter under test: `.ufo/waves/round-79/build/check_allowed_tools.py`,
sha256 `74e067ccad7813d9…`, `TARGET = 5`, `BASE_REV = b10bcbc6…`.

| world | pages | result | exit |
|---|---|---|---|
| base do-nothing | r79 base `b10bcbc6` | `backed 0 of 6`, entry absent | 1 |
| **A — real committed snapshots** | S226–S231 as committed | **`backed 5 of 6`**, one finding: `msaf: S229-msaf.html: quote lies in the first-heading block (Q70)` | 0 (T=5) |
| B — A + synthetic S229 only | five real, msaf synthetic `h1`+paragraph | `backed 6 of 6` | 0 |
| C — A + heading-model repair only | six real; counter's `.html` branch maps `<h1..h6>` to `# ` | `backed 6 of 6` | 0 |

World A also printed `script-only world: 0 of 6`, `opened this round 6 of 6`,
`province surfaces named 6 of 6`, rule ok, registry home ok — i.e. every other
conjunct passes mechanically. World A's commit `304d4cbb…`, B `375d9fa7…`,
C `1fb5710b…`; receipts `Kb80G01Revenge-worldA-real.txt` `…worldB…` `…worldC…`.

So: the C4 mechanism is confirmed (B reproduces 6 of 6), **and** the real-bytes
ceiling is 5 of 6 under the r79 draft's own conjunct (d) — for any entry,
mechanical or authored (§4).

## 3. The r80 design against that rejection

### 3.0 What "the r80 counter" was at measurement time

`.ufo/waves/round-80/build/check_allowed_tools.py` is byte-identical to the
r79 draft (sha256 `74e067ccad7813d9…`, `TARGET = 5`, `ENTRY = …-round79.md`,
`BASE_REV = b10bcbc6…`) and contains no `generator world:`, `documented` or
`semantic rider:` string. The r80 predicate therefore does not exist yet in
bytes; checks 1–3 below are against the plan text (`plans/round-80.md`) and the
counter seat's dispatch delta (`.ufo/waves/round-80/w1-spec.json`, item
`Kb80E07C2Counter`). I score the frozen predicate's reachability on the draft
counter, whose six per-surface conjuncts the plan carries unchanged.

### 3.1 Does the r80 claim REST on beating the generator? (must not) — NO

Plan line 42, verbatim: "C4 the independent mechanical generator (Q74 — its
score is printed; the claim does not rest on beating it)". Plan line 36:
"The headline asserts FORM-LEVEL documentation only … what the mechanical
generator reaches (M of 6) is printed beside the headline, and the judgement
part of the claim is the exploratory rider below." Counter delta (4): "the exit
predicate NO LONGER conditions on the script-only world being below target —
instead the generator world's score M is printed … so M is expected 6 and
printed, never gated". The usual failure (claim survives only because the
generator is weaker) is absent: r80 explicitly admits M may equal N.

### 3.2 Does the counter PRINT the generator's score? (must) — YES in design

Plan line 36 fixes the printed line `generator world: M of 6` beside
`allowed-tools surfaces documented N of 6`; line 38 (i) repeats it: "(i) the
counter prints the generator world's score (Q71/Q74 — the generator is built
from the committed snapshots mechanically, scored on the same frozen counter,
and may not hardcode an unreported score)". Not yet verifiable in bytes (§3.0);
E07 must show the line in the self-test and in the base receipt.

One delivery condition, not a design defect: the printed M must be the
full-shape generator's score. The r79 draft's in-file `script_only_world` scores
0–1 of 6 on real bytes (World A: `script-only world: 0 of 6`) because it picks
the first host-matching registry row and writes the label `unstated` for every
surface; printing that number as `generator world:` would understate the reach
by five surfaces and would misreport Q74. E07's "M is expected 6" implies the
full-shape builder, which is what §2 built.

### 3.3 Is the semantic rider the only part claiming what the generator cannot reach? (must be) — YES

The measured part is exactly the mechanical set: entry shape, 11-cell mined
rows, host/path pins, manifest-equals-anchor sha, located quote, `opened` ==
`verified-at` == date, tree conjuncts. My World B is a proof by construction
that this whole set is reachable without judgement. The only semantic content in
the plan is the exploratory rider (grant-semantics matrix + the cross-client
conflict reading), declared "exploratory — real, not countable" (line 40) and
consistent with AXES.md's exploratory class. No plan sentence claims semantics
from the number.

### 3.4 Are the reviewers of record non-author — and named? — NON-AUTHOR YES, NAMED NO (role, not identity)

AXES.md (fleet root, lines 43–50): an exploratory claim "verifies only as
`unprovable-but-better` **with a named non-author reviewer on record** (reasons
included; a dispatched subagent does not count) … Without that judgment it lands
`unprovable`". Plan line 40: "reviewers of record: the round-80 non-author
closure spot-check (a dispatched subagent does not count; the closure is not the
author)".

- Non-author: correct by construction. The closure spot-check is a separate
  governance agent that writes `corpus/lessons/round-80-verifier-spotcheck.md`
  (`role: non-author closure spot-check`, the convention of rounds 62 and 76–79),
  and the plan reproduces AXES' exclusion clause verbatim.
- Named: **not met as written**. The plan names a *role and a round*, not a
  reviewer identity. The lane's one landed precedent carries an identity:
  `corpus/lessons/round-60-verifier-spotcheck.md:60` — "named non-author
  reviewer: hyaku round-60 closure session (@m_kfc)". Q71 says "named non-author
  seats"; a role string is a hope until the identity is on record (the same
  reading the wave's own critic reached independently, `Kb80C02C2.md` F3).
  Fix at integration: record the closure session's handle and reasons in the
  SCORECARD row, and make "closure declines / reviews form only" the declared
  honest-stop branch.

## 4. The blocking gap: `documented 6 of 6` is unreachable on committed bytes

Structural facts, measured (receipt `Kb80G01Revenge-receipts.txt` §R6):

- `S229-msaf.html` (committed at base) contains exactly **one** occurrence of
  `allowed-tools` (raw offset 28377). In the counter's text view it is line 95.
- The page's first real heading is `<h2>Agent Skills</h2>` at raw offset 23083 —
  **before** the field row. So the quote is after the page's first heading, as
  Q70 intends.
- But the counter's `.html` text view strips all tags, so no heading marker
  survives. The first line starting with `#` in the view is line 168, a Python
  comment in a code sample ("# Auto-approve load_skill and read_skill_resource,
  but not run_skill_script."). `quote_location()` rejects any quote at
  `idx <= first_head + 1` → `95 <= 169`, so **every** admissible msaf quote is
  refused. There is no second occurrence to quote.
- Consequence: for any entry — mine, the r80 entry, or a human's — msaf cannot
  count. The honest world reads `documented 5 of 6`, exit 1 under the plan's
  `N == 6`, and the generator world hits the same wall (it is scored by the same
  counter on the same snapshots), so `generator world: 6 of 6` is also
  impossible on committed bytes. The plan's "M is expected 6" is unreachable
  exactly as the N it accompanies.
- The defect is in the counter's heading model, not in the evidence: the msaf
  row is fully supportable (quote, `Experimental` page token, `Space-delimited`
  value token and pin all exist at view lines 95–97), and World C —
  where the only change is that the `.html` branch maps `<h1..h6>` to `# ` —
  reads `6 of 6`, exit 0. Red-before/green-after is therefore on record:
  A = 5/6 (Q70 finding), C = 6/6.

Why this is a gap in the *design*, not an implementation detail: the plan
freezes conjuncts (a)–(f) "as the r79 plan § C2" including "after the first
heading per Q70" (line 38) and promises `6 of 6` before any data. The counter
seat's delta list (E07) does not mention the heading model, so the wave as
dispatched will either discover the wall late or, worse, "fix" it by relaxing
the Q70 check — which is the exact narrowing the plan's own kill rule forbids
("any world making the exit predicate lie … is a counter defect and stops C2").
The honest path is a **declared erratum before the freeze** in the E5 style:
recognise `h1`–`h6` in the `.html` branch, keep the Markdown branch unchanged,
keep the banner/first-heading semantics (which the repair *restores*: the quote
was after the page's real first heading all along), and carry a red-before arm
on the r79 snapshot. This is a repair of a demonstrable defect, not a target
change; the target stays `N == 6`.

## 5. Convergence (independent, not borrowed)

The C2 critic seat reached Finding 1 independently in `Kb80C02C2.md` ("KILLED as
drafted … Q70 first-heading-block rule hard-fails the honest S229/msaf row on
committed bytes (5 of 6…)"), with its own kill-proof receipt on the same bytes.
I derived it from my own generator run (World A) and the structural sweep; the
two derivations agree on the number (5 of 6), the cause (view line 95 vs first
`#` line 168) and the repair (HTML heading synthesis). That agreement is the
strongest calibration signal in this report: two seats, different methods, same
defect.

## 6. Named residuals and confidence

- **Headline disclosure (medium).** Q71's second clause says a claim whose
  script-only world reaches the target "says so in the headline". The plan says
  it about the headline ("what the mechanical generator reaches … is printed
  beside") rather than in it. The SCORECARD row (Kb80S03Scorecard) is the
  headline carrier; it must state that the generator reaches the target and
  that the judgement is the closure's, or Q71's condition is unmet on the record
  readers see.
- **Reviewer identity (§3.4, medium).** Role named; identity not. Cite the
  closure handle at integration.
- **Freshness (not re-derived here).** `Kb80C02C2.md` F4 reports that conjunct
  (e) binds the string `2026-10-27` and the anchor sha, never the fetch record's
  timestamp/bytes, so r79 rows pass "opened this round" with no r80 fetch. I did
  not re-derive that; it is the critic's receipt, and it bears on the plan's
  claim that "the six pages are re-opened live this round".
- **Confidence.** High on §2 and §4 (measured, replayed, two derivations); high
  on the plan quoting in §3 (exact strings, line numbers); medium on the
  "named" reading in §3.4 (governance judgement; the r60 precedent is the only
  landed instance in this lane).
- **Not checked:** the wave's six re-open receipts' live fetches (another seat's
  item), the r80 SCORECARD row (not drafted when I measured), and any statement
  about clients beyond the committed snapshot bytes.

## 7. Tooling and scratch

No install, upgrade or package-manager call; no pacman; no host service touched;
at most two concurrent processes (generator + counter). Scratch peak ~7 MB
(`--shared` clones). `S=/fast/scratch/hyaku/kotoba-r80/Kb80G01Revenge` is removed
before delivery; receipts were copied to `.ufo/waves/round-80/build/` first.

## 8. Addendum — cross-claim check (C1 stack × the C2 entry), measured

Prompted by Kb80E10Battery's and Kb80V03Instruments' broadcasts; C2-adjacent, so
recorded here rather than left to the C1 seats.

- The published C2 entry `.ufo/waves/round-80/build/allowed-tools-surfaces-round80.md`
  (sha256 `b89f0637ac66b60d…`) no longer carries a full-hex `commit`-grammar
  citation: its line 125 now names the page's fetch record (`S231.fetch.json`)
  instead of the mistral-vibe commit, so the hazard Kb80E10Battery flagged
  ("landing the entry adds a third unresolvable") is closed in the current
  bytes. I did **not** run the gate on the earlier bytes that carried the hex.
- Measured on the current entry, tracked into a `--shared` clone at base
  `398cbe1` (`verify_corpus_integrity.py --repo <clone> --no-baseline --json`,
  receipt `Kb80G01Revenge-integrity-withC2entry.json`): `tracked_files` 152→153,
  `commit_total` 46→46, `commit_unresolvable` 2→2 (detail is exactly
  `corpus/SOURCES.md:171` and `:172`, hash `7bb48f21…` — the S230/S231 anchor
  cells, not the plan-named gemini/zed tokens; that hash is mistral-vibe's
  commit and the S230 cell misattributes it, §9), `report_dead` 1→1,
  `unindexed` 1→2 (the entry itself).
- So the C2 entry adds no unresolvable token and no dead pointer; it adds one
  unindexed corpus file, which is C1 repair 3's coverage row, not a
  grammar-class question. If any later revision of the entry reintroduces a bare
  `commit `<hex>`` for a third repository, only a line-scope class (bare repo
  name, or a quoted/marked form) will keep the battery green — the in-token
  `owner/repo@<hex>` shape does not match `resolve to \`owner/repo\` commit
  \`<hex>\`` lines.

## 9. Base defect found while verifying §8: the S230 anchor cites another repository's commit

Verified from the committed bytes (no claim adopted from the peer reports):

- `corpus/SOURCES.md:171` (S230, pi-mono) anchor cell reads, verbatim: "page
  revision `main` resolved to `badlogic/pi-mono` commit
  `7bb48f213ac677f943d5c791199ed3dddf302f00`".
- `.ufo/waves/round-79/snapshots/S231.fetch.json` (mistral-vibe) records:
  "'main' resolved to commit `7bb48f213ac677f943d5c791199ed3dddf302f00` by git
  ls-remote at 2026-10-27T21:43:03Z". So the digest in the S230 cell belongs to
  **mistralai/mistral-vibe**, and the S231 cell (`:172`) cites it correctly.
- `.ufo/waves/round-79/snapshots/S230.fetch.json` records pi-mono's own head:
  "main at fetch time = `bb65e3e49710fbd14f10c7792d0eaa6e2b2c5923` (commit date
  2026-10-27T21:31:47Z, GitHub commits API); the last commit touching this path
  is `25cc5c7bf4cbc76b2e134c729eb8d57d521ed749` (2026-09-22 …), so the served
  blob is older than main head."
- The row's snapshot and pin are unaffected (fetch record sha `5b980552…` ==
  row sha == `MANIFEST` pin once written). What is wrong is the *attribution*:
  S230 names pi-mono and quotes a mistral-vibe commit.

Impact, stated narrowly:

- **My C2 measurement is unaffected.** The counter reads the anchor cell only
  through `FETCHED_RE` and compares group 3 (sha256) to the manifest pin; it
  never resolves a commit. The pi quote, tokens and pin are all correct
  (S230's text view: one `allowed-tools` occurrence, line 78, as B and C
  show). So the 5/6 → 6/6 finding stands.
- **The C1 grammar class is unaffected in shape but the token is now doubly
  wrong**: `7bb48f21…` is unresolvable in lane+fleet because it is a third
  repository's commit (mistral-vibe), and on the S230 line that repository is
  not the one named. An external-citation class clears the gate; it does not
  make the cell true.
- **Disposition.** `corpus/SOURCES.md` anchor cells are frozen for this round
  (frontier step: the six rows are re-opened, `used-by` moves, "no other cell
  changes"). The honest fix is an erratum line in `corpus/lessons/round-80.md`
  § Gate / § Mistakes naming S230's real head (`bb65e3e4…`, fetch record) and
  the misattributed digest, with the cell corrected at the next round that owns
  the row — not a silent edit now, and not the M45 pattern (rewriting a row to
  quiet a gate).

VERDICT: NOT-ANSWERED — the r80 form/semantics split answers M79-1/Q74 in form (claim no longer rests on beating the generator; `generator world: M of 6` is printed and never gated; semantics is rider-only; the reviewer is the non-author closure), but the measured part cannot reach its frozen after-value on committed bytes: S229-msaf.html's only `allowed-tools` occurrence precedes the counter's first `#` line (a Python comment), so any entry caps at `documented 5 of 6` (measured; 6 of 6 only after an HTML heading-model repair or on synthetic pages, which are also why r79's C4 read 6 of 6), and the same wall makes `generator world: 6 of 6` unreachable; additionally the reviewer is named by role, not identity (AXES/Q71 + the r60 precedent). Gap to close before the freeze: declare the HTML heading-model erratum with a red-before arm (A 5/6 → C 6/6), state the generator's reach in the SCORECARD headline, and record the closure handle.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/w1/Kb80G01Revenge.md; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80G01Revenge-receipts.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80G01Revenge-gen_c4.py; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80G01Revenge-worldA-real.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80G01Revenge-worldB-synthetic-msaf.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80G01Revenge-worldC-heading-repair.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80G01Revenge-base-r79.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80G01Revenge-c4-replay.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80G01Revenge-c4-replay.log; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80G01Revenge-integrity-base.json; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80G01Revenge-integrity-withC2entry.json
