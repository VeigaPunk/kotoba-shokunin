# Kb80E09C2Worlds — C2 control worlds (C0–C8) for kotoba round 80

Seat: leaf (no subagents, no background jobs). Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.
Base `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`. Plan read first:
`plans/round-80.md` § C2 (the counter under test, the six surfaces, the nine
control worlds, the Q71/Q74 split).

**Headline: the round-80 C2 headline `documented N of 6` / exit 0 is NOT
reachable with the bytes as they stand, and the cause is NOT the claim data.**
Two independent, structural facts, each measured on committed bytes:

1. **The counter's Q70 first-heading rule misfires on the msaf HTML snapshot.**
   `S229-msaf.html` names the field exactly once (text-view line 95). The
   counter's `quote_location()` finds "the first heading" as the first text-view
   line starting with `#` — which in that page is a **Python code comment**
   (`# Auto-approve load_skill and read_skill_resource, …`) at text-view line
   168, i.e. *after* the field's only mention. Every window carrying the field
   therefore starts at or before line 95 and is rejected as "quote lies in the
   first-heading block (Q70)". Exhaustive measurement: **14 candidate windows,
   0 admissible.** The page's real `<h1>` is at raw line 675 and the field at
   raw line 817 — the field *is* after the real first heading, so the defect is
   in the counter's heading detection on an HTML page, not in the quote. (This
   corroborates Kb80E08's independent report of the same finding.)
2. **The corpus's own anchor grammar is not the counter's grammar.** The six
   C2 rows as published by the corpus edit seat (`Kb80S05SourcesEdits.patch`,
   applied cleanly to the base tree) render the fetch record as
   ``fetched 2026-10-27, HTTP 200, 7608 B, sha256 `<hex>` `` — a bare date and
   a **backticked** digest. The counter's `FETCHED_RE` wants
   `fetched <date>T<time>Z, HTTP 200, <bytes> B, sha256 <hex>` — a full ISO
   instant and an **unbackticked** digest. Measured: with the corpus rows
   verbatim the count is **0 of 6** (six findings "anchor cell carries no
   'fetched <ISO8601>Z, HTTP 200, <bytes> B, sha256 <hex>' record"); with
   ONLY that rendering normalised (same date, same bytes, same digest) it is
   **5 of 6**, the remaining loss being msaf's Q70 refusal. Two one-line
   renderings apart from a 6-of-6 claim.

Neither is repairable from this seat: the counter is the counter seat's file and
the corpus rows are the corpus edit seat's file. **Both are reported, neither is
narrowed.**

---

## 1. Deliverables

| file | what it is | sha256 |
|---|---|---|
| `.ufo/waves/round-80/build/c2_controls.py` | the control-world generator (the deliverable) | `03ae32724b1234aacac0d44d223668fcc7fda493fd188cdfc51a4e1b5c2b9464` |
| `.ufo/waves/round-80/build/Kb80E09C2Worlds.counter-port.py` | MY port of the round-80 counter (r79 draft + the E07 deltas) — used because the counter seat's own bytes were unfrozen (see §3) | `9aa1af3b17534921d39dcacbbdf51efdb32e92879c06ed619a78a0bb4733f05d` |
| `.ufo/waves/round-80/build/Kb80E09C2Worlds.run.log` | the run receipt (every world's three lines + its own exit) | `38ef609032e057d3eed1e82750ee597ddfd41e67bc08c745516264ce6238b796` |
| `.ufo/waves/round-80/build/Kb80E09C2Worlds.stdout.txt` | the same run's stdout | `38ef609032e057d3eed1e82750ee597ddfd41e67bc08c745516264ce6238b796` |
| `.ufo/waves/round-80/build/Kb80E09C2Worlds.port-selftest.log` | my port's own `--self-test` output | `f068d90edb8f8b3fcd50853c63286aff95636ed5385640731da43c545cc1b873` |
| `.ufo/waves/round-80/build/Kb80E09C2Worlds.diagnostics.py` | the per-surface diagnostics probe (generator world findings + the msaf heading positions) | — |
| `.ufo/waves/round-80/build/Kb80E09C2Worlds.admissibility-probe.py` | the exhaustive per-surface window/admissibility probe | — |

The suite **reproduces byte-identically from a clean state**: a fresh
`git clone --shared` of the lane at the base revision, a fresh `--work` tree and
a fresh run produced identical count lines, generator lines and exit codes
(verified by diff against the published receipt).

`c2_controls.py` is stdlib-only, honours `TMPDIR` and `--work`, and builds every
world as its own isolated scratch git repo (`git init -q`, identity
`scratch-r80`, every git call `-C`'d, `rev-parse --show-toplevel` asserted
equal to the world dir, one `alternates` line to the base clone's object store,
`read-tree` the base tree, fixtures written as blobs, `write-tree` +
`commit-tree -p <base-rev>`). The lane is read-only throughout: the only lane
writes are this seat's two files under `.ufo/waves/round-80/build/` and this
report.

The counter's own constants (`ENTRY`, `SNAPDIR`, `MANIFEST`, `CAPTURE`,
`TARGET`, `SURFACES`) are **read out of the counter file by importing it**, so the
suite follows whatever the counter freezes rather than hard-coding it. The
suite also prints a per-surface admissibility table computed with the counter's
own `quote_location()`.

## 2. The control worlds and their measured verdicts

Measured on MY port (`Kb80E09C2Worlds.counter-port.py`), base
`398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`, scratch clone
`/fast/scratch/hyaku/kotoba-r80/Kb80E09C2Worlds/clone`. Every count is the
counter's own printed line; every exit is the command's own status.

| world | what it breaks | `documented N of 6` | `generator world: M of 6` | exit | verdict |
|---|---|---|---|---|---|
| C0 | base copy, unmodified | 0 of 6 | 0 of 6 | 1 | as-expected |
| C1 | token dump: every token/label, no snapshots, no manifest | (no count line) | (no line) | 2 | as-expected |
| C2 | wrong-page real text (every row quotes another surface's page) | 0 of 6 | 1 of 6 | 1 | as-expected |
| C3 | shared-banner quote (one banner line in all six snapshots) | 0 of 6 | 1 of 6 | 1 | as-expected |
| C4 | **the INDEPENDENT mechanical generator over the committed snapshots** | **5 of 6** | 1 of 6 | 1 | **DIVERGES** (pre-registered 6 of 6) |
| C4b | diagnostic: the corpus's own anchor rendering | 0 of 6 | 1 of 6 | 1 | as-expected |
| C5 | label-only (labels + tokens, no quote) | 0 of 6 | 1 of 6 | 1 | as-expected |
| C6 | sibling host (`…/pi-mono-evil/…`) | 4 of 6 | 1 of 6 | 1 | DIVERGES (pre-registered 5 of 6) |
| C7 | stale snapshot (bytes changed after the pin) | (no count line) | (no line) | 2 | as-expected |
| C7b | wrong sha pin (anchor digest ≠ the snapshot's) | 4 of 6 | 1 of 6 | 1 | DIVERGES (pre-registered 5 of 6) |
| C8 | first-answer baseline (no entry; 6 of 6 asserted in prose) | 0 of 6 | 1 of 6 | 1 | as-expected |
| H0 | oracle: the honest world with each surface's **corpus-recorded** quote verbatim | 4 of 6 | 1 of 6 | 1 | as-expected |
| G0 | generator isolation: a registry carrying only the six C2 rows | 5 of 6 | **4 of 6** | 1 | as-expected |
| S05 | **the corpus edit seat's published `corpus/SOURCES.md` verbatim** | **0 of 6** | 1 of 6 | 1 | as-expected |
| S05b | the same rows with ONLY the anchor rendering normalised | **5 of 6** | 1 of 6 | 1 | as-expected |

Suite: 15 worlds, **3 divergences** (C4, C6, C7b) — all three are the SAME
single cause: the msaf surface cannot be documented at all, so every expected
count that assumed six backable surfaces is one lower. C6 and C7b behave
exactly as designed (each removes exactly one further surface: the sibling host
is refused, the wrong pin is refused); they diverge only in the absolute number
because the baseline is five, not six.

**No world reached 6 of 6.** The plan's C2 kill rule ("any control reaching
6 of 6 … is a counter defect and stops C2") is therefore **not** triggered —
but the claim is blocked for the opposite reason: the honest world itself cannot
reach 6 of 6.

## 3. Which counter bytes were used, and why (provenance)

My seat spec says to use `.ufo/waves/round-80/build/check_allowed_tools.py`
verbatim if it exists. It exists, and I ran the suite against it verbatim
first: **every one of the 15 worlds read `environment error: counter drifted —
the running file is not the frozen counter` (exit 2).** The published file's
`SELF_SHA` is `1f9744c8…` while its own bytes hash (blanked) to `f6569f6b…`:
the file is **unfrozen**, mid-edit by the counter seat (the docstring and the
`documented` / `generator world` / `semantic rider` wording are in place, but
`ENTRY` is still `…round79.md`, `TARGET` is still `5`, and the exit predicate is
still the r79 one).

So I wrote **my own port** of the round-80 counter — the r79 draft with exactly
the six E07 deltas applied and nothing else — and measured against that. The
port is published as `Kb80E09C2Worlds.counter-port.py` (sha256 above) so the
L1 can diff it; it is my instrument, not a proposal for the lane's file.
Deltas applied, all from the counter seat's own brief:

| delta | change |
|---|---|
| D1 | headline `allowed-tools surfaces documented N of 6` |
| D2 | `TARGET = 6`; exit 0 iff `N == 6` and the tree conjuncts hold |
| D3 | third printed line `semantic rider: exploratory — reviewers of record: round-80 non-author closure spot-check` |
| D4 | the generator world's score is printed, never gated |
| D5 | entry path `corpus/knowledge/allowed-tools-surfaces-round80.md`; `BASE_REV` = the round-80 base |
| D6 | the generator world's grant label comes from a **frozen keyword rule** over the quote it derived, not the constant `SCRIPT_LABEL = "unstated"`, so the generator world is scored on the same counter |

The port's own `--self-test` is **green: 0 failures over 233 assertions in 81
worlds** (receipt `Kb80E09C2Worlds.port-selftest.log`). Getting there required
re-coding the r79 arms for D2's exit rule (35 arms that expected exit 0 at five
of six now expect exit 1), replacing the arm D4 makes void ("a script-only world
that reaches the target stops the claim"), and adding the two arms the brief
requires (a 5-of-6 world exits 1; the `generator world:` line is present). D6
also required the generator's quote rule to choose among the windows the
counter's own `quote_location()` accepts — otherwise the generator world
reports a number dominated by its own mechanical choices rather than by
anything about the claim. **The port is a measurement instrument for this
seat's control worlds; the frozen counter is the counter seat's deliverable,
and the L1 must re-run this suite against the frozen bytes.** The suite is
written to take any counter file (`--counter`).

## 4. Findings, each with its receipt

**F1 — msaf admits no admissible quote under the counter's Q70 rule (structural).**
Exhaustive measurement with the counter's own `quote_location()` over every
5..25-word window of the committed page carrying both `allowed-tools` and the
frozen page token: **S226 34 candidates / 25 admissible; S227 1 / 1; S228 27 /
27; S229 14 / 0; S230 21 / 21; S231 21 / 21.** The refusal reason, verbatim
from the counter: `quote lies in the first-heading block (Q70)`. The mechanism:
the counter finds the first heading as the first text-view line starting with
`#`; in `S229-msaf.html` that is a **Python comment** at text-view line 168
(`# Auto-approve load_skill and read_skill_resource, but not run_skill_s…`),
while the field's only mention is at text-view line 95. The page's real
`<h1 id="agent-skills">` is at raw line 675 and the field at raw line 817 — the
field IS after the real first heading, so the reading (not the quote) is at
fault. This is a **counter-side** fix (heading detection for an HTML text view);
it is not repairable by narrowing any quote. Kb80E08 reported the same finding
independently from the entry side.

**F2 — the corpus's own anchor rendering is not the counter's grammar.**
The six C2 rows as published by the corpus edit seat render the fetch record
``fetched 2026-10-27, HTTP 200, 7608 B, sha256 `<hex>` ``; the counter's
`FETCHED_RE` wants `fetched <date>T<time>Z, HTTP 200, <bytes> B, sha256 <hex>`
(ISO instant, digest NOT in backticks). Measured with the corpus rows verbatim:
**0 of 6**, six findings `anchor cell carries no 'fetched <ISO8601>Z, HTTP 200,
<bytes> B, sha256 <hex>' record`. With ONLY that rendering normalised — same
date, same bytes, same digest — **5 of 6**, the one remaining loss being F1's
msaf refusal. So the two defects are independent and each costs exactly one
step toward 6 of 6. The corpus side is a corpus-edit-side fix; the counter side
is a counter-side fix; **the L1 must decide which side moves**, because with
both as they stand the C2 headline cannot reach 6 of 6.

**F3 — the counter's own generator world reads 1 of 6 in most worlds, and 4 of 6
when the registry carries just the six C2 rows (G0).** With the r79 draft's
generator as it stands, the constant `SCRIPT_LABEL = "unstated"` is written into
every row, so only the `vibe` surface (whose frozen label *is* `unstated`) can
pass conjunct (f); the per-surface findings are `spec/claude/factory/msaf/vibe:
<sid>: source cell holds no URL` and `pi: row carries no value-form token` /
`pi: row carries 2 backticked token(s)`. That is the r79 finding 6.2 again. My
port's D6 (a frozen keyword rule for the label, and a quote chosen among the
windows the counter's own `quote_location()` accepts) lifts the generator world
from **1 of 6 to 4 of 6** in the G0 isolation arm — still one short, because
the generator's own msaf quote is the Q70-refused one. **Consequence for the
plan's (i):** the generator-world line is a *report*, and under the r79
mechanics it reports a number dominated by the generator's own mechanical
choices rather than by anything about the claim. The two fixes belong in the
counter seat's file (the label rule, and the generator row's URL-less source
cell). **This is a reading for the L1, not a defect of the claim data.**

**F4 — the published counter bytes are unfrozen.** Every world run against
`.ufo/waves/round-80/build/check_allowed_tools.py` as published reads
`environment error: counter drifted` and exits 2 (24 occurrences in the
verbatim run's log). Its `SELF_SHA` (`1f9744c8…`) does not match its own bytes
(`f6569f6b…` blanked), `ENTRY` is still `…round79.md`, `TARGET` is still `5`,
and the exit predicate is still the r79 one (`n >= TARGET and m < TARGET`).
Until the counter seat freezes its bytes, **no C2 measurement of any kind can
be taken against them.**

**F5 — the corpus's own recorded quotes cannot all be used verbatim in the
ENTRY's surface row.** The H0 oracle (the honest world carrying each surface's
corpus-recorded located quote verbatim, in the entry's row) reads **4 of 6**:
`S230`'s corpus quote is `Experimental pre-approved tool list` — 4 words, under
the counter's 5-word floor, and it carries no `allowed-tools` token — and
`S229`'s is the Q70-refused one. So two of the six corpus quotes are unusable
as entry-row located quotes under the counter's reading: the entry must carry a
different quote for `pi` (any admissible window carrying `allowed-tools` and
`Experimental` — there are 21) and for msaf the Q70 refusal bites first.

**This is NOT counter-load-bearing, and it is NOT repairable in the registry
cell** (both points sharpened by Kb80E08, which reproduced my measurement
independently): the counter reads the located quote from the ENTRY's surface row
(`quote_of(row)` → `row[4]`), never from the registry anchor cell, and no gate
reads a registry anchor's quote at all. The `S230` defect is therefore narrow:
the row's ANCHOR cell records a fragment that is not a located quote under the
counter's reading, and it cannot be corrected in place, because every
admissible `pi` quote necessarily contains a vertical bar (the page names the
field exactly once, inside a markdown table row) and the census splits a
registry row naively on `|` — an in-place edit of that cell was measured to red
the corpus gate with `file E01 S230 fields=12`. The correction path is the
entry row (or an append-only supersede row), never a naive in-place cell edit.
Reported for the entry seat and the L1; no corpus file was edited here.

**F6 — the controls all behave as designed.** C1 exit 2 with `environment
error: no manifest at …` (the token dump cannot be evaluated, never credited);
C2 0 of 6 (every row's quote is another surface's page text); C3 0 of 6 (the
shared banner is refused by the same-line check); C5 0 of 6 (no quote at all);
C6 4 of 6 (the `-evil` sibling host is refused: `pi: S230: no URL on pi's
pinned host(s) ['raw.githubusercontent.com/badlogic/pi-mono']: ['https://raw.githubusercontent.com/badlogic/pi-mono-evil/…']` — Q32's whole-segment prefix holds); C7 exit 2 with `environment error:
snapshot_tampered` (the pin binds the bytes); C7b 4 of 6 (`pi: S230: anchor
sha256 000000000000... is not the snapshot's pin 5b9805525b19...`); C8 0 of 6
(no entry file; the prose assertion earns nothing); C0 0 of 6.

## 5. What C4 shows (and what it does not)

C4 is the **independent** mechanical generator: it reads the six committed
snapshots, scrapes each quote by a fixed window rule (the shortest 5..25-word
window carrying both `allowed-tools` and the surface's frozen page token),
chooses each grant label by a **frozen keyword rule**, derives the tokens from
the quote, and computes the pins from the committed bytes. It reaches **5 of 6**;
the one loss is msaf's Q70 refusal (F1). Its derived quotes, verbatim from the
receipt:

```
S226 allowed-tools | No | Space-separated string of pre-approved tools the skill may use. (Experimental
S227 allowed-tools field grants permission for the listed tools during the turn that invokes the skill, so Claude can use them without prompting you for approval
S228 allowed-tools: Read Grep Glob enabled: true user-invocable: true disable-model-invocation: false license: MIT compatibility: droid version: 1.0.0 metadata
S229 allowed-tools No Space-delimited list of pre-approved tools the skill may use. Experimental
S230 allowed-tools | Experimental pre-approved tool
S231 allowed-tools: read grep ask_user_question ---
```

**This reach is the POINT, not a refutation.** Per Q71/Q74 the round-80
headline is form-level: it says the six surfaces carry committed,
snapshot-pinned, quote-grounded rows. A purely mechanical generator satisfies
that form, so C4's reach does not falsify the headline — it is exactly what
Q71/Q74 predicts, and it is why the grant-semantics rider is exploratory and
assigned to the round-80 non-author closure spot-check rather than to the
counter. **The generator's reach must not be read as evidence that the
grant-semantics matrix is true**; nothing here says `pre-approves` is true of
Claude Code or `metadata-only` of Factory — those are the rider's business.

C4's 5-of-6 also shows the form claim is *nearly* satisfiable mechanically:
a form-complete entry over the committed snapshots exists and is derivable
without judgement. What blocks the headline is the counter's own reading
(F1) and the corpus's own anchor rendering (F2).

## 6. What I did not do (and why)

* **I did not repair the counter.** `verifiers/` is patch-only for the counter
  seat; F1 and F3 are reported to them. My port is a measurement instrument
  in `build/`, clearly named, never proposed as the lane's file.
* **I did not repair the corpus rows.** F2 and F5 are reported to the corpus
  edit seat / entry seat; `corpus/` is outside my write scope.
* **I did not narrow any world to make it pass.** C4 stays at 5 of 6 with the
  msaf refusal named; the plan forbids repairing a counter defect by narrowing,
  and the same rule applies in reverse here.
* **I did not score any claim after-value.** Every number above is a CONTROL
  world or a diagnostic; the plan's no-after-value rule is untouched.
* **I did not run the lane's build/lint/test.** Only the counter, the git
  plumbing and my own scripts ran, each with its own captured exit.
* No network fetch was needed and none was made.

## 7. Coordination

* **Kb80E07C2Counter** (counter seat): their published bytes are unfrozen
  (F4), so every world reads `counter drifted` (exit 2). My port with their six
  deltas is at `build/Kb80E09C2Worlds.counter-port.py` for them to diff
  against their file. **F1 (msaf Q70 on an HTML page) and F3 (the generator
  world's constant label + URL-less source cell) are theirs to fix**; both are
  measured, with the mechanism named.
* **Kb80E08C2Entry** (entry seat): **F5** — the corpus's `S230` quote
  (`Experimental pre-approved tool list`) is 4 words and carries no
  `allowed-tools`, so it cannot be a located quote under the counter's reading;
  `S229`'s corpus quote is Q70-refused (F1). 21 admissible `pi` windows exist.
  Independently, F2 concerns the rows, not the entry.
* **Kb80E05SourcesEdits** (corpus edit seat): **F2** — the six rows' anchor
  rendering (``fetched <date>, HTTP 200, N B, sha256 `<hex>` ``) is not the
  counter's grammar; with the rows verbatim the count is 0 of 6, and with only
  the rendering normalised it is 5 of 6. The L1 must decide which side moves.
* **Kb80E09C2Worlds** (this seat) consumed: the counter seat's published
  bytes (unfrozen, F4) and the corpus edit seat's published
  `Kb80S05SourcesEdits.patch` (read from `build/`, applied in a throwaway
  clone under `--work`; the lane was not touched). No other seat's output was
  consumed.

## 8. Recommended next step for the L1

The C2 headline cannot be established as frozen. In order:

1. the counter seat freezes its bytes (F4) — until then nothing is measurable;
2. the counter seat resolves the msaf Q70 reading (F1) — without it the
   ceiling is 5 of 6 on ANY entry, including a perfect one;
3. the L1 resolves F2 (which side moves on the anchor grammar);
4. re-run this suite against the frozen bytes: `python3 -B
   .ufo/waves/round-80/build/c2_controls.py --counter
   .ufo/waves/round-80/build/check_allowed_tools.py --base-tree <clone> --work
   <scratch>`. The suite reads the counter's own constants, so it follows the
   frozen entry path, snapshot directory, manifest path and target without
   edits.

Until (1) and (2) are done, the honest reading of the round-80 C2 claim is
**"5 of 6 at best, for a reason in the instrument and in the row rendering, not
in the claim data"** — not "6 of 6".

## 9. Cleanup and tooling

Scratch `/fast/scratch/hyaku/kotoba-r80/Kb80E09C2Worlds` (clone, work dirs,
probes) was removed after the receipts were copied into `build/`. No tool was
installed or upgraded; no pacman run; no host service touched.

VERDICT: C2 control suite C0–C8 built and measured on a port of the round-80 counter (the published bytes are unfrozen, so every world read "counter drifted"): no world reached 6 of 6, so the plan's C2 kill rule is not triggered; but the honest mechanical world reaches only 5 of 6 because the counter's Q70 first-heading rule misfires on the msaf HTML page (0 of 14 candidate windows admissible) and the corpus's own anchor rendering is not the counter's grammar (0 of 6 verbatim, 5 of 6 with only that rendering normalised) — both reported to their owning seats, neither narrowed or repaired here.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/c2_controls.py; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E09C2Worlds.counter-port.py; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E09C2Worlds.run.log; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E09C2Worlds.stdout.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E09C2Worlds.diagnostics.py; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E09C2Worlds.admissibility-probe.py; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/w1/Kb80E09C2Worlds.md
