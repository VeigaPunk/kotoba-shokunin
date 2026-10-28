# Kb81G01Revenge — the r80→r81 lineage map (revenger, round 81 w1)

Seat: revenger, leaf (no spawns, no subagents, no background jobs). Lane:
`/home/vgpnk/Projects/shokunin/kotoba-shokunin` (read-only). Base for every byte I
read: `b284223105f4d106f7e8f56ed4fd296c643cda0e` (`git rev-parse HEAD`, exit 0).
No claim after-value is scored here; no control world is scored. Scratch
`/fast/scratch/hyaku/kotoba-r81/Kb81G01Revenge/` (probe scripts + fixture tree),
removed before this yield; receipts copied into
`.ufo/waves/round-81/build/Kb81G01Revenge-*` first. No tool was installed or
upgraded; pacman was not invoked; at most two concurrent processes.

## 0. What this seat is for

The r80 wave built a C1 repair stack (E04 report-pointer resolver, E05 external-commit
grammar class, E06 counter erratum, E01/E02/E03 supporting repairs) and the round ended
as an **honest stop**: `.ufo/reports/round-80/kotoba.md:9` — "C1 was falsified by critic
C01: three new shortcut worlds each reached 6 of 6 on the frozen amended counter … The
kill rule fired; the unsafe E04/E05/E06 C1 stack was not landed." Round 81 declares a
different C1 design (R1–R6 + erratum E6). This seat answers one question, on bytes:
**what of r80 is continued, what is genuinely new, and what did r80 learn that r81 does
not carry?**

Three findings change decisions, stated up front (details in §5, §6):

1. **R1 closes the r80 kill world's instance, not its class.** The r80 W10 marker world
   was scored at `.ufo/reports/round-76/kotoba.md` — a path the *corpus* gate reads
   (measured), so R1 reaches it. But 22 report paths are cited by LOG/SCORECARD/SKILL
   and never by `corpus/` (measured sweep), and the battery's other report reader —
   `verify_skill_checklist.py`'s `governance.citation_resolves` — is **existence-only**
   (measured on a 7-byte marker, §4.4). One of those 22 paths (`round-16`, cited as
   `../.ufo/reports/round-16/kotoba.md` at `SCORECARD.md:31`) is absent from the lane and
   resolved through the fleet. A marker there is accepted by the checklist and invisible
   to both corpus gates. **[INFERENCE]** the battery then reads 6 of 6 at a tip where
   R1–R6 have landed — i.e. the r80 W8/W10 class is still control-reachable, one path
   over. The r81 W8 declaration does not cover the checklist-only arm.
2. **Two r80 calibration residuals are silently carried, not re-owned**: the moving-ref
   `HEAD:` resolution (E04 residual 1 — the C1 kill report asked for a *pinned digest*,
   not a content class), and assertion-floor coverage (E04 residual 4 / E06 §9.3 — the
   counter has no `floors-registry.json` row at all; measured).
3. **The r81 C1 arithmetic does not come from bytes.** The kill rule's "40 base-spent"
   and the base truth are different numbers: the six-instrument spend against the
   counter's pinned base `072048fa` is **22 added / 3 deleted** at `b2842231` (measured,
   §2). With the plan's own "estimated 60–120 added lines", the estimate's top (120)
   exceeds the budget the declared arithmetic implies (100). The direction is
   safe (it can only stop the claim early), but the number an integrator will read as
   authoritative is wrong — and r80's E15 runbook called this figure "the single most
   important number in this runbook".

## 1. Method

Three kinds of evidence, kept separate:

- **Committed bytes at the base** — blob ids, numstat, file existence, registry/floors
  contents. Receipt: `.ufo/waves/round-81/build/Kb81G01Revenge-base-state.txt`
  (collector script `collect-base-state.sh`, every command prints its own `[exit=…]`).
- **Gate readings at the base** — my own runs of both corpus gates (`integrity exit=1`,
  `independent exit=1`) with the JSON documents kept: `Kb81G01Revenge-base-integrity.json`,
  `Kb81G01Revenge-base-independent.json`. Receipt:
  `.ufo/waves/round-81/build/Kb81G01Revenge-scope-sweep.txt` §G.
- **Function-level probes of the lane's own instruments** (the lane is read, never
  written; throwaway fixtures under TMPDIR): which report paths the corpus gate counts
  (`Kb81G01Revenge-probe-round76-token.py` / `.txt`), and whether the checklist's
  citation predicate accepts a 7-byte marker
  (`Kb81G01Revenge-probe-checklist-marker.py` / `.txt`).

Peer artifacts consumed read-only from `.ufo/waves/round-80/` (all present; the r80
build dir is tracked: 697 files, 64 w1 seat reports — measured in the base-state
receipt §I): `Kb80E04DeadPointer.patch` + `Kb80E04DeadPointer.composed-blob.txt` +
`w1/Kb80E04DeadPointer.md`, `Kb80E05GrammarFix.patch` + `w1/Kb80E05GrammarFix.md`,
`Kb80E06CounterErratum.patch` + `w1/Kb80E06CounterErratum.md`,
`Kb80E13FixtureGuard.md`, `Kb80E15BaselineOrder.md`, `Kb80E16PinAudit.txt`,
`w1/Kb80C01C1.md` + its canonical receipts, `w1/Kb80G01Revenge.md`, plus
`corpus/lessons/round-80-verifier-spotcheck.md` and `plans/round-80.md`.

Nothing from those files was executed as an instruction; they are data.

## 2. The r80 stack, byte by byte: what actually landed at `b2842231`

The r80 report says the unsafe E04/E05/E06 stack was not landed and the "safe partial
repairs and C2 documentary artifacts" were. That is exactly what the bytes show.

| r80 artifact | intent | state at `b2842231` | evidence |
|---|---|---|---|
| `Kb80E01Registry.patch` | SKILL.md § Gate registry rows for two withdrawn verifiers + the new C2 counter | **LANDED** (rows 63; registry gate exit 0 in the base battery receipt) | `grep -c '^\| \`verifiers/' SKILL.md` → 63 |
| `Kb80E02Symlink.patch` | `.ufo/reports/round-76/kotoba.md` symlink to the fleet report | **LANDED** as mode `120000` | `git ls-tree HEAD .ufo/reports/round-76/` |
| `Kb80E03IndexBaseline.patch` | coverage rows + baseline refresh | **PARTIAL**: baseline re-recorded at r80 close, but the closure's own lesson is unindexed and the recorded counts are stale | base integrity: `unindexed 1`, `tracked_files 155`, `report_total 111` vs baseline expectations 154/109 |
| `Kb80E04DeadPointer.patch` | `<rev>:<path>` report-pointer resolution (lane → fleet) | **NOT LANDED** | `HEAD:verifiers/verify_corpus_integrity.py` = `e470eaa…` = the r80 base blob (E16 §2) |
| `Kb80E05GrammarFix.patch` | external-commit class, grammar + line-scope arms | **NOT LANDED** | `HEAD:verifiers/verify_corpus_independent.py` = `edac0df…` = r80 base blob; no `commit_external` key in `observed.corpus` (measured: `None`) |
| `Kb80E06CounterErratum.patch` | `LINE_CAP` 40→60 + two pins + constants | **NOT LANDED** | `sha256sum verifiers/check_tip_battery.py` = `e33b17d7…` = the r79/r80 frozen counter; `LINE_CAP = 40` at `:111` |
| `Kb80E07C2Counter` | r80 C2 counter | **LANDED** (`verifiers/check_allowed_tools.py`, 118313 B; `TARGET=6`, `ENTRY=…round80.md`, `CAPTURE="2026-10-27"`, `SELF_SHA` at `:324`) | base-state receipt §D |
| `Kb80E08C2Entry` / S08 / S09 / S10 | C2 entry, README rows, SKILL rule, PROVINCE bullet | **LANDED** (`corpus/knowledge/allowed-tools-surfaces-round80.md`, 25465 B; `corpus/lessons/round-80.md`, 20329 B) | base-state receipt |
| E13 **F2** (missing `MANIFEST.sha256`) | C2 pin manifest | **CLOSED** (`.ufo/waves/round-79/snapshots/MANIFEST.sha256`, blob `37d44e33…`, 575 B) | base-state receipt §C |
| E13 **F10** / G01 §4 (Q70 heading model) | HTML heading synthesis for the text view | **CLOSED in the landed counter** (`view_with_headings` at `:396`; docstring at `:145-153` records the msaf defect) | base-state receipt §D |
| `Kb80Y01Simplify.patch`, `Kb80E10Battery.stack*.patch`, `Kb80S07Quality-world`, `Kb80L02Ctl.*` | candidate stacks, alternative bundles, control-world patches | **SUPERSEDED** — never landed, and correctly so: the L1 ruled the canonical E05 class, and E06 §4 records the Y01 pins as provisional | E06 §4 |
| `Kb80E13FixtureGuard` **F7** | new-class silent-drop trap in the integrity gate | **STILL A LIVE TRAP** for any r81 patch that adds a class (see D4, §5) | E13 F7 + base `corpus_observations()` key lists |
| `Kb80E13FixtureGuard` **F1** | `check_mcp_instructions.py` writes a scratch dir inside the lane tree | **OPEN** at base (`verifiers/check_mcp_instructions.py:274`, `dir=LANE`) | read at base |

Two consequences an integrator should not have to rediscover:

- The r81 base is **r80-minus-the-unlanded-stack**: same instrument blobs as the r80
  base (`e470eaa…`/`edac0df…`/`e33b17d7…`), so every r80 patch applies to it with the
  same context it was built against — *except* that r81 will not replay them, it will
  write new ones against these blobs. Port or rewrite, nothing is pre-applied.
- `check_allowed_tools.py` at base has `BASE_REV = "398cbe1…"` and `CAPTURE =
  "2026-10-27"`; it is a round-80 instrument that r81 inherits and does not re-measure
  (§5 D6).

## 3. What the kill worlds proved the designs needed

The r80 kill (`.ufo/waves/round-80/w1/Kb80C01C1.md`) is the design brief r81 is
answering. Each world isolates one requirement:

| r80 world | measured bypass (own exit 0 in the receipt) | what it proves a repair needs |
|---|---|---|
| **W8** — `commit \`kotoba-shokunin/kotoba-shokunin@56b0764e…\`` (a real commit created in an isolated lane clone, absent from the measured lane and fleet) | `commit_external=3`, `commit_unresolvable=0`; battery `6 of 6`, exit 0 (`Kb80C01C1-canonical-lane-at-tipbattery.txt`) | a line marker can name **the lane itself**; exemption must be an out-of-band, reviewed, hash→repository binding |
| **W9** — a SOURCES row naming the lane's own GitHub URL and carrying the same dead hash | same: `commit_external=3`; battery `6 of 6` (`…-lane-url-tipbattery.txt`) | a URL in the row is not evidence of *which* repository owns the digest |
| **W10** — seven-byte `marker` committed at the fleet report path | battery `6 of 6`, exit 0 (`…-fleet-marker-default.txt`, real `a025051d…` vs marker `d4169ac5…`) | resolving a report target is not verifying it: existence ≠ a report |

The design inversion r81 states (`plans/round-81.md`
§ C1 repairs 1–2) is the correct answer to W8/W9: classification now requires
`absent from lane + fleet` **and** a manifest entry with proof; a marker alone never
exempts. For W10 the answer is weaker: a *content class* (`## SHONEN` and ≥400 B), which
distinguishes a marker from a report but not one report from another. C01's own
recommendation was "validate the target's pinned digest/report identity, not only
`is_file()`" (`Kb80C01C1.md` § "Symlink control and smallest safe correction"). r81
adopts the digest/manifest mechanism for *commits* (R2) and the shape test for
*reports* (R1). That asymmetry is the single most important design fact in this
lineage, and §5 D1/C3/C6 are its consequences.

Why r80 could not simply narrow: its own trade was recorded — E05's line-scope arm was
the only arm that could reach `SOURCES.md:172`, because that row names
`mistralai/mistral-vibe` only in the row URL and title, not on the token (`Kb80E05GrammarFix.md`
§ "What the class is"; `Kb80L01Grammar.md` finding 3). r81's manifest escapes that
constraint entirely: the binding lives in a new file, so the row need not be edited and
the token need not carry a marker. This is the part of the design that is *better* than
anything r80 had, and it is why R2 is a new design rather than a port.

## 4. The lineage map, repair by repair

### 4.1 R1 — report-pointer resolution + report content identity → continues E04, adds a new arm

- **Continued from E04** (byte-identical design, r79→r80): partition the token on `:`,
  resolve `<rev>:<path>` as a git object expression, citing repo first then fleet
  (`git cat-file -e`); the self-test arm with the two dead tokens and one
  unresolvable revision; the "uncommitted working-tree file must not satisfy a
  revision" property (E04 §5 class C).
- **New in r81**: the resolved target must also *look like a report* — bytes contain
  `## SHONEN`, size ≥400 B — applied to path **and** object resolutions. This is the
  direct answer to W10.
- **What r81 says it supersedes**: "the r80 E04 design" (plan § C1 repair 1). Precisely,
  it supersedes E04's *existence* predicate; it keeps E04's resolution mechanism.
- **Not carried**: E04 §9 residual 1 (the fleet hop resolves `HEAD:` at measurement
  time — a moving ref, not a pinned commit) is neither repaired nor named in the r81
  plan. §5 D1.
- **Carried implicitly**: E04 §9 residual 3 (both gates' final blobs must be measured
  *after* all hunks compose, and the pin must name the composed blob) — r81's E6 (b)
  repeats the one-blob-per-path rule, and the freeze-before-data discipline is the same.
- **Scope note**: R1 is declared for `verify_corpus_integrity.py` only. That is
  sufficient for the *claim* (measured: the independent gate reads `report_dead 0` at
  base, so only integrity is red on that class), but it leaves the checklist arm
  existence-only. §6 C6.

### 4.2 R2 — external-commit verified binding → supersedes E05's mechanism, keeps its purpose

| dimension | r80 E05 (unlanded) | r81 R2 (declared) |
|---|---|---|
| trigger | absent from lane+fleet **and** a third-repo marker on the citing line, **or** a `o/r@<hex>` grammar token | absent from lane+fleet **and** present in `verifiers/external-commits.json` with a committed fetch/ls-remote receipt |
| who grants the exemption | the citing line's prose | a reviewed, committed evidence file |
| spoofability | proven spoofable (W8, W9) | not spoofable by editing a citation line; spoofable only by fabricating the receipt (a review property, see C5) |
| grammar arm | `commit \`owner/repo@<hex>\`` intercepted before the non-hex branch | dropped (measured: 0 such tokens in `corpus/`, base-state receipt §H — E05 residual R4 still true) |
| provenance | cannot detect a false attribution (E05 R2) | still cannot *detect* it; the S230/S231 hashes are now bound to mistral-vibe in the manifest and the correction is a supersede row (R5) |
| live effect at base | `commit_unresolvable` 2 → 0, `commit_external` 2 | same intended effect, but the two tokens must first exist as manifest entries with proof |

So: **same purpose, inverted mechanism**. R2 is the one r81 repair with no r80
precedent in kind — the manifest is new. Two obligations follow that the plan's prose
states but its control list does not bind: the receipt must be *content*-checked for the
hash (C4), and the manifest should carry a freshness field (C5).

### 4.3 R3 — `.ufo/wapes` disposition → new repair, continuing an r80 routed disposition

The file is still at the lane root at base: 594 B, sha256 `930e2bd6…`, mtime 20:17
(base-state receipt §E). It is untracked, so no r80 artifact "owns" it; three r80 seats
independently flagged it (E06 §9.4, E15 §2, closure R80-D2) and none could delete
another seat's file. R3 is the first owner. Note the plan's own wording ("moves to
`.ufo/waves/round-81/dispositions/wapes.txt`") makes the disposition *committed
evidence*, which is the right shape: the content is probe output, and the provenance —
not the bytes — is what the record needs.

### 4.4 R4 — index + baseline → continues E03/E15/E06

- Same script, same refusal order, same "commit → refresh → commit" sequence as
  E15 §3 G7 and E06 §5c. The r81 plan compresses this to one sentence
  ("then `refresh-corpus-baseline.py` … re-records … at the final pre-report commit,
  every zero class reading 0"). The trap that compression loses is E06 §5c's: the
  baseline's `head` field makes the file **not** a pure function of the tree, and an
  exit-3 refresh has *already written* the baseline (E15 §4). §5 D7.
- New content for this round: the coverage row for
  `corpus/lessons/round-80-verifier-spotcheck.md`, which landed at `b284223` without one
  (base measured: `unindexed 1`, exactly that file) — the plan says "indexed, never
  edited", which is the correct disposition of a closure-owned file.

### 4.5 R5 — S230 supersede row → new mechanism, pursuing the r80-recommended disposition

r80's disposition was explicit and correct: `corpus/SOURCES.md:171` (S230, pi-mono) cites
mistral-vibe's `7bb48f21…`; `S230.fetch.json` records pi-mono's head as `bb65e3e4…` and
the last path commit as `25cc5c7b…`; `S231.fetch.json` binds `7bb48f21…` to
mistralai/mistral-vibe (`Kb80G01Revenge.md` §9; E13 F9; E05 residual R2). r80's
conclusion: "the honest fix is an erratum line … with the cell corrected at the next
round that owns the row — not a silent edit now, and not the M45 pattern". r81 R5 does
exactly that, but with an append-only **supersede row** rather than a cell rewrite —
stronger than r80 proposed, and consistent with CORPUS rule 2. Residual: the live row
still states the wrong repository; a reader who stops at S230 is still misled. That is a
record-quality cost the supersede row accepts, not a gate cost.

### 4.6 R6 — registry row for the new C2 counter → continues E01/S09 + E15 G2/G3

Same pattern r80 landed (`check_allowed_tools.py` has its row; 63 rows at base), same
adjacency requirement (E15: row-before-file = PHANTOM, file-before-row = non-conformant;
both exit 1). r81's plan states the adjacency ("lands with the counter file in the same
commit") and adds the stop condition ("if C2 stops, no row and no counter ship"), which
is the right coupling.

### 4.7 Erratum E6 — continues E5 in shape, changes the number

r80's E5 had five declared items (E06 §2): (1) `LINE_CAP` 40→60; (2) two pin members;
(3) the two self-test fixture constants re-anchored to derive from `LINE_CAP`; (4) the
docstring/comment cap mentions updated; (5) *optional extra*: the pin arm widened from
2 to 41 lines so the pin alone rejects an in-cap gain. r81's E6 declares (a)–(d), which
map to (1)–(4) exactly — including (d) "comment cap mentions updated so text does not
contradict the bound", which is the item r80 added only after its own docstring went
stale. The only r80 item not declared is (5); under a 140-line cap the base 2-line pin
arm still passes the size guard and fails the pin, so the arm's *semantics* survive, and
its *demonstration* ("just under the cap") is simply weaker. No material loss.

What does change materially is the arithmetic (§6 C1) and the size headroom the cap
buys: r80 landed at "exactly at the cap, zero headroom" (60 = 60). r81 moves to 140
against a measured spend of 22, so the reviewed repair has ~118 lines of room. The
plan's stated estimate is 60–120 — which is *larger than the budget the plan's own
sentence implies*. A seat that measures 120 added lines and applies the kill rule
literally ("40 base-spent + measured added ≤ 140" → 120 > 100) would stop a claim that
the counter's actual arithmetic (22 + 120 = 142 > 140) also stops, but for a different
reason by 2 lines. Both roads stop; the numbers should have been reconciled before data.

## 5. r80 intents this round does not carry (named, with owner and severity)

D1 — **E04 residual 1: moving-ref resolution / no digest pin** (medium; unowned).
`report_pointer_exists` still resolves `HEAD:` at measurement time. The content class
closes "any file" but not "the wrong report": a different real report (≥400 B,
`## SHONEN`) at the cited path passes. C01 asked for a pinned digest. The r81 plan does
not name this residual, and no r81 control tests it (W8 substitutes a 7-byte marker
only). Owner: R1's next revision; a one-paragraph declaration in the plan would keep it
from being rediscovered as a kill.

D2 — **assertion floors** (low-medium; unowned). `verifiers/floors-registry.json` has
17 rows; `corpus_integrity` floor 164, `corpus_independent` 105, `checklist` 1863,
`correction_sweep` 25 — and **no row for `check_tip_battery.py`** (measured; E06 §9.3,
E04 §9.4). r81 adds self-test arms to the two corpus gates and rewrites the counter's
self-test constants; the added arms will not be floored, and the counter's own self-test
remains entirely unfloored, so a later dropped arm reads PASS. Not a claim blocker; a
calibration hole that r80 measured and r81 does not mention.

D3 — **E05 residual R2: provenance is not detected** (declared via R5, not repaired).
`commit_external` still certifies "absent from lane+fleet and in the manifest", not
"the citing line names the right repository". The lesson/SCORECARD must not read the
class count as provenance. r81's R5 makes the truth discoverable; it does not make the
gate able to see it.

D4 — **E13 F7: silent observation loss in `verify_corpus_integrity.py`** (medium;
undeclared trap for R2's author). `corpus_observations()` aggregates through explicit
`agg`/`details` key lists (base: `agg` at `:643`, `details` at `:655`, aggregate loops at
`:678` and `:682`; E13 F7 cited the same construct at `:645-690` on its own base), so a class
returned by `citation_findings()` but not registered in both lists is **silently
dropped** — "the gate still prints a plausible number". E05 hit it and fixed it; r81's
R2 rewrites the same region from base bytes. The plan does not say "register the class in
both lists", and no r81 control checks that the two gates agree on the class. A
reviewer's one-line check: `observed.corpus.commit_external` must exist in the integrity
JSON **and** equal the independent gate's count.

D5 — **E13 F1: scratch dir inside the lane tree** (low; unowned, not a claimed repair).
`verifiers/check_mcp_instructions.py:274` still uses
`tempfile.TemporaryDirectory(prefix="mcp-self-test-", dir=LANE)`. The suggested repair is
one argument; nobody owns it in r80 or r81. It is the same *class* as R80-D2 (a tool
writing inside the measured tree), which makes it worth a routed line.

D6 — **the r80 C2 counter is outside the r81 no-harm battery** (low-medium; operability).
`plans/round-81.md` § No-harm battery lists eight gates; `check_allowed_tools.py` is not
among them. It is a lane verifier with a registry row and a round-bound `CAPTURE`, and
r81 changes `corpus/SOURCES.md` (new S249, new supersede row, S248 `used-by`), the exact
cell class it reads. If a row edit reds it, nothing in the battery says so. Its
`SELF_SHA`/`--print-self-sha` self-drift convention (E15 §6 #12, E07's landing
condition) is also not required by the r81 C2 predicate (conjuncts (a)–(e) say nothing
about instrument self-verification) — a pattern r80 built and r81 does not ask for.

D7 — **refresh discipline** (low; runbook-level). E06 §5c and E15 §2/§4 carry three
non-obvious facts: the refresh refuses on *untracked* files (so the wave evidence must
be committed first, and `.ufo/wapes` must be gone), the baseline embeds the commit it was
refreshed at (hence commit → refresh → commit, no amend), and exit 3 means the baseline
was already written (inspect/restore, never commit). The r81 plan states only the
outcome.

D8/D9 — **immaterial drops**. E05's grammar arm (0 live tokens, measured) and E06's
optional pin-arm widening (semantics survive under cap 140). No action.

## 6. Calibration findings on r81's own declarations

C1 — **base-spend arithmetic**. Plan kill rule: "the reviewed instrument patches'
combined added lines exceed the declared cap arithmetic (40 base-spent + measured added
≤ 140)". Measured: `git diff --numstat 072048fa… HEAD -- <six instruments>` →
`22 3 verifiers/check_assertion_floors.py`, nothing else. So the base spend is 22, not
40, and the sentence's budget for this round's additions is 100 (or 118 under the
measured spend). The declared estimate is 60–120. Recommend restating the sentence with
the measured 22 before the freeze so the honest-stop test is unambiguous.

C2 — **base gate truth**. Plan line 9 says `verify_corpus_independent.py` exits 1 on
"the same `commit_unresolvable` 2 plus `report_dead` 1". Measured: independent reads
`report_dead 0`, `report_total 111`, `commit_unresolvable 2` (receipt §G), i.e. it is red
on the commit class only. This matters because it is the sentence that justifies R1's
one-gate scope — the scope is right, the stated reason is off by one class.

C3 — **R1's strength, stated honestly**. The plan calls the arm "a report-marker
distinction arm, not a completeness judgment" — accurate, and it should stay in the
headline. The phrase "report content identity" in the repair title reads stronger than
the predicate. A controlled world that survives it as written: a 400-byte file
containing `## SHONEN` (any report, hand-written or copied) at a cited path.

C4 — **R2's control set has one arm where it needs two**. W9 is "a manifest entry with
no committed receipt proof". The W10-analogue for R2 is "a manifest entry whose receipt
path exists but whose bytes do not contain the hash" — existence vs content one level
down. The plan's prose requires proof ("the committed fetch/ls-remote receipt that
proves the repo→hash association"); the declared world does not test it. Add the second
arm, or the same class can be reproduced inside the new mechanism.

C5 — **the manifest is static evidence**. No `verified-at`/`recheck` field is declared
(contrast the C2 entry, which the plan requires to carry `verified-at` and `recheck`),
and the counter cannot distinguish a fabricated in-tree receipt. The class's strength
rests on the word "reviewed" in the plan. That is defensible, but it should be written
down as the load-bearing assumption, and a recheck field costs nothing.

C6 — **R1 does not reach the checklist arm, and the class it closed is still reachable
through it** (the seat's principal finding). Measured:
`verify_skill_checklist.py`'s `citation_resolve` (`:1529`) is an existence test —
`safe_resolve(...)` / `(base / path).exists()` — and my function-level probe returns
`True` for a **7-byte marker** at the fleet path and `False` once the marker is removed
(`Kb81G01Revenge-probe-checklist-marker.txt`); W10 already showed the gate-level
consequence (`governance.citation_resolves` PASS with a marker substituted for the fleet
report). Its citation roots include `.ufo/` and `../` (`:393`), so it evaluates
fleet-resolved report tokens — verified end-to-end for the path I use below: the
checklist's own subject extractor returns 426 subjects for `SCORECARD.md`, and the
`round-16` token is one of them (`{'line': 31, 'token':
'../.ufo/reports/round-16/kotoba.md'}`, `Kb81G01Revenge-probe-checklist-subjects.txt`). Scope sweep: 34 report paths are cited by
LOG/SCORECARD/SKILL, 50 by `corpus/`, **22 by the former only**; 21 of those 22 have
lane-committed regular files (so their resolution never crosses into the fleet), and one
— `round-16` — is absent from the lane, cited as `../.ufo/reports/round-16/kotoba.md`
at `SCORECARD.md:31`, and present in the fleet. Meanwhile the corpus gates read
`round-76` (probe: `report_total 1`, the token at `round-76-verifier-spotcheck.md:14`)
but never `round-16` (0 corpus files). At a tip where R1–R6 have landed, the checklist
gate passes on the marker, the corpus gates never see the path, and the battery reads
6 of 6 — **[INFERENCE]**, contingent on the tip's other classes being green, which is
the claim's own premise.

What this does and does not mean: the r81 declaration is not wrong — W8 as written
("a marker file substituted at the fleet report path (expect `report_dead` → red)") will
read red *if* the critic substitutes at `round-76`, because R1 covers the corpus-cited
path. It means the class was narrowed **by path choice**, not by predicate, and the
declared control cannot see the difference. Two honest continuations, both pre-data:
run W8 twice (corpus-cited path and checklist-only path) and let the second arm stop C1
under the plan's own kill rule; or declare a second erratum extending the identity arm
to `verify_skill_checklist.py` — which costs a pin and size budget E6 does not cover, so
it cannot be done silently.

## 7. What the C2 lineage looks like (thin, but correctly joined)

r80's C2 landed its form backbone and its counter; r81 C2 adds a seventh surface (the
Agent SDK `allowedTools` query channel) as a **new entry + new counter + S249 row**, and
updates S248's `used-by`. The joins to r80 that hold:

- The Q70 heading rule that r80's revenger found broken for HTML snapshots
  (`Kb80G01Revenge.md` §4) is repaired in the *landed* r80 counter
  (`view_with_headings`), and S249's page is Markdown (`…/skills.md`), where conjunct (d)
  needs only the `#` arm — so the r81 surface does not reopen that defect. If the r81
  counter is derived from `check_allowed_tools.py` it inherits the repair; if it is
  written fresh, it must not reintroduce tag-stripping without heading synthesis.
- r80's C2 predicate was "6 of 6 with a printed generator score"; r81's is "1 of 1".
  The generator/script-only control duty (Q74) is correspondingly smaller but not
  waived: the r81 control set C0–C4 is declared, and C4 ("assert `1` with no files —
  must print 0") is the first-answer baseline.
- The one r80 C2 *deliverable* that r81 must not let rot is the counter itself (D6).

## 8. Operability — the short list for the integrating L1

1. **Do not replay the r80 patches.** They target blobs identical to the base, so they
   apply, but landing E05's marker grammar would re-open W8/W9. R2 replaces it.
2. **Pin after composition.** The r81 E6 pins must name the final blobs of
   `verify_corpus_integrity.py` (R1 ∘ R2) and `verify_corpus_independent.py` (R2) as
   committed — the E04 residual 3 lesson; the freeze receipt must be written before any
   after-value.
3. **Register any new class in both integrity lists** (D4), then check both gates agree
   on `commit_external`.
4. **Run W8 in both path classes** (C6); if the checklist-only arm reads 6 of 6, stop.
5. **Refresh clean, commit alone, no `--carry`, no amend** (D7), and delete/move
   `.ufo/wapes` before the clean-tree check (R3).
6. **Measure the base spend yourself** (C1) and state it in the freeze receipt.
7. Keep `check_allowed_tools.py` in the final battery sweep (D6), and keep S249's
   snapshot pin out of the `..`-hop prose rule (E15 §7.8).

## 9. Confidence, and what I did not measure

- **High**: the landed/unlanded inventory (blob ids, numstat, tree modes), the base gate
  readings (own exit statuses), the report-path scope sweep, the checklist predicate
  probe, the floors row list, the `.ufo/wapes` bytes, E6's declared line set (read in
  full, including (d)).
- **Medium**: C1's arithmetic criticism (depends on reading "base-spent" as spend; both
  readings keep the direction safe but differ by 18 lines); C6's battery-level 6 of 6
  (the predicate and path facts are measured; the composite score is inference).
- **Not measured / not claimed**: the r81 instrument bytes (none published under
  `.ufo/waves/round-81/build/` at my read — only `run-battery.sh` and S12 artifacts),
  the C2 counter, any seat's R1/R2 patch, the tip battery at a future r81 tip, whether
  an r81 reviewer will find the F7 trap, and the live pages behind S248/S249.
- **Not scored**: any claim after-value; any control world. Worlds are the critics'
  instrument; this seat maps the frontier they should walk.

## 10. Receipts (all under `.ufo/waves/round-81/build/`)

| file | what it is |
|---|---|
| `Kb81G01Revenge-base-state.txt` | collector output: rev, blob ids, numstat, symlink mode, registry count, C2-counter constants, `.ufo/wapes` hash, floors rows, cap-40 docstrings, grammar-token sweep, r80 file inventory |
| `Kb81G01Revenge-scope-sweep.txt` | path-set sweep (34/50/22), lane presence per path, the only `.ufo/reports` symlink, `CITATION_ROOTS`, ancestor-hop citations, the corpus-read probe, base gate readings |
| `Kb81G01Revenge-base-integrity.json`, `Kb81G01Revenge-base-independent.json` | the two gate documents at `b2842231` |
| `Kb81G01Revenge-probe-round76-token.py` / `.txt` | function-level probe: the corpus gate counts the `round-76` path (`report_total 1`) |
| `Kb81G01Revenge-probe-checklist-marker.py` / `.txt` | function-level probe: the checklist predicate returns `True` for a 7-byte marker at the fleet path, `False` without it |
| `Kb81G01Revenge-probe-checklist-subjects.py` / `.txt` | function-level probe: the `round-16` fleet token is in the checklist's evaluated subject set (426 subjects for `SCORECARD.md`, hit at line 31) and resolves today |

VERDICT: The r81 repair set continues r80 in exactly three places (R1 keeps E04's resolver and adds a content-class arm; R2 keeps E05's purpose and inverts its mechanism to a reviewed manifest; E6 keeps E5's shape with 140 instead of 60), lands two genuinely new mechanisms (R2's manifest binding; R5's append-only supersede row) and one new repair for an r80 routed defect (R3), while four r80 lessons go unowned — the moving-ref report resolution C01 asked to pin, the unfloored counter/gate arms, the F7 silent-class-drop trap R2's patch must re-satisfy, and the checklist's existence-only report predicate, through which the r80 W10 marker class survives at a measured path (`round-16` via `../` in `SCORECARD.md:31`, 0 corpus citations, predicate returns True on a 7-byte marker) so the declared W8 control must be run in both path classes or the claim can be reached at 6 of 6 with a marker; the r81 arithmetic also misstates the base spend (measured 22/3 against `072048fa`, declared as 40) and its estimate's top exceeds the budget that arithmetic implies.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81G01Revenge.md; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81G01Revenge-base-state.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81G01Revenge-scope-sweep.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81G01Revenge-base-integrity.json; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81G01Revenge-base-independent.json; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81G01Revenge-probe-round76-token.py; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81G01Revenge-probe-round76-token.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81G01Revenge-probe-checklist-marker.py; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81G01Revenge-probe-checklist-marker.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81G01Revenge-probe-checklist-subjects.py; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81G01Revenge-probe-checklist-subjects.txt
