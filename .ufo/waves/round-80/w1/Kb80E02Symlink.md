# Kb80E02Symlink — C1 repair 2 of 5: the dead LOG citation (relative symlink)

Item: round 80, wave w1, C1 consistency (calibration sub-axis), repair 2 — port the r79 reviewed
symlink patch (`Kb79E02LogCitation.patch`) to the r80 base `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`.
Leaf seat: no subagents, no background jobs beyond my own tool calls; the scratch tree is removed at
yield (§9).

## 1. The red I was sent to repair, reproduced

At the r80 base, in a fleet-shaped scratch clone (`…/parent/kotoba-shokunin`, every other fleet-root
entry symlinked into the parent, exactly the shape `check_tip_battery.py:build_sandbox` builds):

    $ python3 -B verifiers/verify_skill_checklist.py        # rc=1
    ...
    FAIL governance.citation_resolves: evaluated 1319 — LOG.md:2818:
      '.ufo/reports/round-76/kotoba.md' does not resolve from …/parent/kotoba-shokunin;
      10 quoted meta-finding(s), 3 schematic token(s) excluded,
      2 recorded absence(s) excused, 4 recorded correction(s) excused

    $ python3 -B verifiers/check_assertion_floors.py         # rc=1
    FAIL checklist observed=1863 floor=1863 self_test_failures=1
    (… 16 other rows PASS …)                                # wall 112.3 s

Receipts `build/Kb80E02-base-checklist.txt`, `build/Kb80E02-base-floors.txt` (each file ends with its
own `exit=` line — the command's own status, never a pipeline's).

`LOG.md:2818` (base tree, `git show 398cbe1:LOG.md`, line 2818) is the round-77 entry's **Pointer:**
line, which cites the round-76 report by its lane-relative bare path. The round-76 report is a
**fleet** artefact — `/home/vgpnk/Projects/shokunin/.ufo/reports/round-76/kotoba.md`, 8,128 bytes,
sha256 `a025051d389368ea3a1078b7a64d3847c1e6ff25328fc1645a7be34f30e3f78f` (sha computed here, not
copied from the r79 report) — so the lane-relative address misses.

One cause, two red gates: `check_assertion_floors.py` is red only because
`verify_skill_checklist.py`'s **live** self-test arm re-reds on the same subject
(`self_test_failures=1`, `build/Kb80E02-base-checklist-selftest.txt`:
`self-test FAIL: governance: live round-65 corrections land, errata-excused: got ('FAIL', 1319,
"LOG.md:2818: '.ufo/reports/round-76/kotoba.md' does not resolve …")`; `1 failure(s) over 1863
assertions`). No floor moved, and the base floors row for `checklist` is 1863 in
`verifiers/floors-registry.json` — unchanged by this repair.

## 2. The repair delivered

`build/Kb80E02Symlink.patch` — one path, mode 120000 (git symlink), 1 insertion, 0 deletions:

    .ufo/reports/round-76/kotoba.md  ->  <four parent hops>/.ufo/reports/round-76/kotoba.md

(The literal target string is deliberately NOT written here: it is a four-hop `..` chain, and writing
it backticked would be a fresh governance red — §6. The exact bytes are in the patch file and in
`build/Kb80E02-symlink-identity.txt`, which record it as the symlink's `readlink` output.)

The four hops are counted from the symlink's own directory (`.ufo/reports/round-76/`): `reports` →
`.ufo` → the lane root → the fleet root. The target therefore IS the fleet artefact, addressed from
the lane root — one artefact, one byte-stream, no copy, no paraphrase, no record edit, and
`LOG.md:2818` is not touched. It fails closed: a lane tree that is not one level under a fleet root
leaves the link dangling (measured below), exactly like the `../` fleet citations already in
`LOG.md`/`SCORECARD.md`.

Identity evidence (the gate tests existence, not identity; this is the identity part) —
`build/Kb80E02-symlink-identity.txt`:

| what | value |
|---|---|
| fleet file sha256 (computed by this seat) | `a025051d389368ea3a1078b7a64d3847c1e6ff25328fc1645a7be34f30e3f78f` (8,128 B) |
| resolved-target sha256 in the fleet-shaped lane | `a025051d389368ea3a1078b7a64d3847c1e6ff25328fc1645a7be34f30e3f78f` — equal |
| `realpath` in the fleet-shaped lane | `/home/vgpnk/Projects/shokunin/.ufo/reports/round-76/kotoba.md` |
| git blob of the symlink (mode 120000) | `bf7c7e0c0c39a57c49224c87348afc74dca14db4` |
| patch sha256 | `0f3202409299e0ef2e29242d80c8816f23f9cf04502a370925142d27564bf35b` |

**Port provenance.** The patch is **byte-identical** to the r79 reviewed draft
`.ufo/waves/round-79/build/Kb79E02LogCitation.patch` (same sha256 `0f320240…`; `cmp` → IDENTICAL).
So the port needed no re-anchoring: the r79 draft adds a NEW path with no context lines, and the
path is still absent at the r80 base (`git ls-tree -r 398cbe1 -- .ufo/reports/` lists only
round-20…round-45, all mode 100644; the round-76 directory does not exist in the lane). Apply
checks: `git apply --check --binary` → rc=0 on a clean clone at `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`
and rc=0 at the lane tips `c2f69d4` and `308bff9` (the lane moved while this seat ran — `308bff9`
is a plans-only commit, "pre-data freeze clarification — erratum E5 exact amended line set", which
touches no file this patch touches; the symlink is still absent at that tip: `git ls-tree -r HEAD --
.ufo/reports/round-76/` returns nothing). The applied result is the symlink above; applied in a
plain (non-fleet-shaped) clone, `sha256sum` on the path errors with "No such file or directory" —
the dangling, fails-closed property, measured.

## 3. The gates this repair moves (each command's own exit status)

| world | checklist | checklist --self-test | floors | tip battery |
|---|---|---|---|---|
| base `398cbe1` | exit 1 — 10 PASS / 1 FAIL | exit 1 — 1 failure over 1863 assertions | exit 1 — `FAIL checklist … self_test_failures=1` | exit 1 — `guards 5 of 5; tip battery exit 0: 1 of 6` (plan's base receipt, `--repo .` form) |
| **base + this patch (measured)** | **exit 0 — 11 PASS / 0 FAIL** (`PASS governance.citation_resolves: evaluated 1319 — 1319 governance citation token(s) resolve across 2 files`) | **exit 0 — `0 failure(s) over 1863 assertions`** | **exit 0 — `PASS checklist observed=1863 floor=1863`** (17/17 rows PASS, wall 106.4 s) | **exit 1 — `guards 5 of 5; tip battery exit 0: 3 of 6`** |

Note on the checklist count: the seat brief asked for "10 pass exit 0". Measured counts are
10 PASS / 1 FAIL at base and **11 PASS / 0 FAIL** at the repaired world — the eleventh check is
`governance.citation_resolves`, the one this repair flips; the gate's own totals (evaluated 1319
governance tokens, 205 trigger tokens) are identical on both sides.

Tip-battery detail on the repaired world (`build/Kb80E02-sym-tipbattery.txt`; counter bytes =
the lane's current `verifiers/check_tip_battery.py`, sha256 `e33b17d74f5935a43b04272baf2d88d1d4cf4f879ee9cfa48bb25f89e744bc4a`,
i.e. the round-72 frozen counter — the E5-amended round-80 counter is seat Kb80E06CounterErratum's
deliverable and was not available to this seat):

    guard no-deletions PASS | floors PASS | instrument-size PASS | instrument-pin PASS | spotcheck-identity PASS
    gate verifiers/check_gate_registry.py       exit 1  wall 0.3s
    gate verifiers/check_assertion_floors.py    exit 0  wall 107.1s
    gate verifiers/verify_skill_checklist.py    exit 0  wall 1.5s
    gate verifiers/verify_corpus_integrity.py   exit 1  wall 0.2s
    gate verifiers/verify_corpus_independent.py exit 1  wall 0.6s
    gate verifiers/check_correction_sweep.py     exit 0  wall 0.0s
    fleet root …/parent; guards 5 of 5; tip battery exit 0: 3 of 6

Two of the six battery gates go green on this repair alone; the three remaining reds (registry,
corpus integrity, corpus independent) are other seats' items and are unchanged by it (§5). All five
structural guards still hold — this repair adds **no** line to any of the six instrument scripts,
so the `LINE_CAP` arithmetic and every `INSTRUMENT_PINS` blob are untouched by it.

The same counter run again with `--fleet /home/vgpnk/Projects/shokunin`, so that the counter builds
its **own** fleet-shaped sandbox from the real fleet root rather than from my scratch parent
(`build/Kb80E02-sym-tipbattery-fleetwork.txt`): `fleet root /home/vgpnk/Projects/shokunin; guards
5 of 5; tip battery exit 0: 3 of 6` — floors exit 0 (wall 112.9 s), checklist exit 0 (1.5 s),
correction_sweep exit 0, registry / corpus_integrity / corpus_independent exit 1. Same verdict from
the real fleet root as from my scratch parent.

## 4. No collateral change (measured, base vs repaired world)

- `python3 -B verifiers/verify_corpus_integrity.py --json`: the two JSON files are **byte-identical**
  (`diff` → no differences; `build/Kb80E02-integrity-diff.txt` holds `diff_rc=0`). The six base
  DRIFTs are unchanged: `tracked_files 152≠144`, `unindexed 1`
  (`corpus/lessons/round-79-verifier-spotcheck.md`), `report_total 109≠99`, `report_dead 1`
  (`corpus/lessons/round-77-verifier-spotcheck.md:15: HEAD:.ufo/reports/round-77/kotoba.md` — the
  `<rev>:` pointer form, seat Kb80E04DeadPointer's item), `commit_unresolvable 2`
  (`corpus/SOURCES.md:171,172`) and the `commit_total` drift. My patch adds a tracked file under
  `.ufo/`, which the corpus index does not count (`git ls-files corpus/`), and it resolves no corpus
  pointer, so no count moves.
- `python3 -B verifiers/verify_corpus_independent.py`: outputs identical apart from the `HEAD …`
  header line (`build/Kb80E02-base-independent.txt` vs `-sym-independent.txt`; `diff` shows only
  that line).
- `git diff --stat 398cbe1..HEAD` in the repaired world: one file, one insertion.

## 5. What this repair does NOT do (declared limits)

- **Existence ≠ identity.** The governance predicate is an existence test over the tree, so a link to
  a *wrong* file would also pass. The sha256 equality in §2 is the identity evidence the gate does
  not give; keep it in the round's receipt set.
- **Dangling outside the fleet tree.** A clone of the lane with no fleet parent resolves the link to
  nothing — measured ("No such file or directory" on `sha256sum`). This is the same declared limit
  as every `../` citation in `LOG.md`/`SCORECARD.md`, and the reason the tip battery's sandbox is
  fleet-shaped by construction.
- **Depth assumption.** The four hops are correct while the lane sits exactly one level under the
  fleet root (today: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`). A lane moved deeper would
  need the hop count re-derived.
- **The lane's other `.ufo/reports/round-N/kotoba.md` files are regular 100644 copies** (25 of them,
  round-20…round-45). This repair adds a *different* kind of object (120000) at a path that had no
  lane-side file at all. The lane therefore now holds two kinds of lane-report address; that is
  deliberate here (the r79 seat's §5 weighed a byte copy against the symlink and chose the symlink
  for one-address/one-byte-stream and fail-closed behaviour), but the L1 should know the two kinds
  coexist.
- **The instrument inconsistency stays** (r79 §6, not this item): the corpus verifier resolves a
  bare `.ufo/reports/…` token against the fleet root while the governance verifier is
  lane-relative with a 3-hop cap. Aligning them is a predicate change inside a pinned blob — a
  post-freeze erratum, not this wave.
- **Not measured here** (outside this item): `check_report_pointers.py` (needs the round-80 report),
  the census, `check_gate_registry.py`, the E5 counter amendment, the grammar-class corpus-gate
  change, and the index/baseline refresh — all other seats' items.

## 6. Landmine sweep (the four-hop token must never be written backticked)

`verify_skill_checklist.py:citation_resolve` allows at most **3** leading `..` hops, so a backticked
four-hop path in live prose would be a fresh red. Sweeps run here (all over the **tracked** tree):

- A literal four-hop `git grep -n -F` sweep over tracked `*.md` at the base → 6 lines (all
  pre-existing). The sweep's own counts are summarised in `build/Kb80E02-receipts.txt`; that receipt
  is a `.txt` (not a scanned `*.md`) and does carry the literal target string once, in its
  applied-result section, because the target bytes are the evidence for this repair.
- A backticked-multi-hop sweep over the **gate-scanned** files (LOG.md, SCORECARD.md, SKILL.md,
  `corpus/*.md`) at the base → 2 lines, both pre-existing and both **not** four-hop:
  `corpus/knowledge/harness-independent-round37.md:469` (a `$VAR`-prefixed four-hop chain the token
  extractor rejects, because a `$` disqualifies a citation token) and
  `corpus/lessons/round-8-aggregator-box3-coldrun.md:113` (a three-hop chain plus an ellipsis — a
  schematic the corpus gate excludes).
- The same four-hop sweep over the **repaired** world: the same 6 lines, only the rev prefix differs
  (`diff` shows no new line) — **my patch adds no four-hop token to any tracked `*.md`**.
- The four hops live only in the symlink's own blob, and `git grep` does not match symlink blob
  content (measured: plain, `-a` and `--textconv` all report no match for the symlink path) — so the
  sweep cannot see it even by accident.
- Pre-existing four-hop backticked hits in tracked `*.md` (all outside the gate-scanned scope —
  `GOVERNANCE_FILES = ("LOG.md", "SCORECARD.md")`, and the corpus gates scan `corpus/` only):
  `.ufo/round-38/scouts/V2.md:172` (5 hops), `.ufo/round-46/scouts/w2-critic.md:30` (8 hops),
  `.ufo/waves/round-53/falsify/W2SentinelAlwaysOn.md:23` (7 hops), and
  `.ufo/waves/round-79/w1/Kb79E02LogCitation.md:155` (exactly 4 hops — the r79 seat report naming
  the landmine in prose). They are inert for the gates: the repaired world's checklist evaluates
  1319 governance tokens and every one resolves. **They are still a landmine for the L1's own prose**:
  never write the four-hop target backticked in `LOG.md`, `SCORECARD.md`, `SKILL.md` or a corpus
  file. This report deliberately does not contain the four-hop string backticked.
- Note for the L1's report text: cite the link as the lane-relative path
  `.ufo/reports/round-76/kotoba.md` (which now resolves) and describe the target in prose.

## 7. Deliverables and how to apply

| file | what it is |
|---|---|
| `.ufo/waves/round-80/build/Kb80E02Symlink.patch` | the repair: plain `git diff --binary`, ONE new path, mode 120000 |
| `.ufo/waves/round-80/build/Kb80E02-symlink-identity.txt` | sha256 / realpath / blob / diffstat identity receipt |
| `.ufo/waves/round-80/build/Kb80E02-receipts.txt` | consolidated receipts (all gate exits, one `exit=` line per file) |
| `.ufo/waves/round-80/build/Kb80E02-{base,sym}-checklist.txt` | `verify_skill_checklist.py`, base vs repaired (10 PASS/1 FAIL → 11 PASS/0 FAIL) |
| `.ufo/waves/round-80/build/Kb80E02-{base,sym}-checklist-selftest.txt` | `verify_skill_checklist.py --self-test` (1 failure/1863 → 0 failures/1863) |
| `.ufo/waves/round-80/build/Kb80E02-{base,sym}-floors.txt` | `check_assertion_floors.py` (exit 1 → exit 0) |
| `.ufo/waves/round-80/build/Kb80E02-sym-tipbattery.txt` | `check_tip_battery.py --rev <repaired commit> --repo <fleet-shaped scratch>` (guards 5 of 5, 3 of 6) |
| `.ufo/waves/round-80/build/Kb80E02-sym-tipbattery-fleetwork.txt` | the same counter with `--fleet /home/vgpnk/Projects/shokunin` — the counter's own fleet-shaped sandbox (fleet root `/home/vgpnk/Projects/shokunin`; guards 5 of 5; `tip battery exit 0: 3 of 6`; floors exit 0 wall 112.9 s, checklist exit 0 wall 1.5 s, correction_sweep exit 0; registry/corpus_integrity/corpus_independent exit 1) |
| `.ufo/waves/round-80/build/Kb80E02-{base,sym}-integrity.json`, `-independent.txt`, `Kb80E02-integrity-diff.txt` | no-collateral evidence |

Apply with `git apply --binary` (not `git am` — the file is a bare diff, no mail headers).

## 8. Coordination

- `Kb80E10Battery` (C1 battery runner): told the file name, the apply command, the patch sha256 and
  the applied-result sha256, the fleet-shaped-tree requirement, the measured 3-of-6 effect and the
  landmine note.
- `Kb80E14C1Worlds` (C1 control worlds): told that the E5 counter amendment and the grammar-class
  corpus-gate patches are **not** mine to publish (seats Kb80E06CounterErratum / Kb80E05GrammarFix),
  that deriving them from the plan text is correct if they are not published, and given this item's
  file name, shas, apply command and measured effects so their worlds can use it.
- I did not consume any other seat's build output for this item: the patch is a byte-identical port
  of the r79 reviewed draft, and every measurement above is my own scratch work.

## 9. Cross-check of the C1 stack assembly (measurement only — not my item)

Asked of me mid-wave by `Kb80E10Battery` and `Kb80E08C2Entry`; the full receipt is
`build/Kb80E02-crosscheck-c1-stack.txt`. No corpus file and no verifier was edited by me; every number
below is from my own scratch clones at base `398cbe1`.

**The cap arithmetic is confirmed, and the published grammar candidate cannot fit it.** The
instrument-size guard diffs the six battery scripts against the counter's **pinned** r72 base
`072048fa8e8a52c707d25f7079772fa317244eb7`, not against `398cbe1`: `git diff --numstat 072048fa
398cbe1 -- <the six scripts>` gives **22 added / 3 deleted, all of it in
`verifiers/check_assertion_floors.py`**. E04 costs **17** added on `verify_corpus_integrity.py`, so
39 of the 60 are spent and **21 remain**. The only published grammar candidate
(`build/Kb80S07Quality-world.patch`) costs **96 + 75 = 171** added — it cannot fit the amended cap of
60 at any arrangement (measured).

**But a class that does fit exists, and I measured one.** In a scratch clone (base + E04 + a compact
line-scope class in both corpus gates with a red-before arm in each gate's self-test) the total over
the pinned base is **60 added / 6 deleted — exactly at the cap**, with
`verify_corpus_integrity --self-test` → *0 failure(s) over 166 assertions* and
`verify_corpus_independent --self-test` → *106 assertions, 0 failures*, and the two real blockers
moving into the new INFO class. The shape that fits: one regex per gate matching an owner/repo token
**or** a raw.githubusercontent.com/github.com URL anywhere on the cited line; one branch at the existing
`not commit_resolves(...)` site routing a marked token to a new `external` list; the class registered
in the observation dict so it is *visible*; and the red-before arm placed so it does **not** shift the
shared self-test counters (its own fixture root) — otherwise five to seven counter expectations move
and the budget blows. The published candidate misses on two counts: 35 of its 171 lines are comments,
and its arm sits in the shared fixture, which shifts five counter expectations in the independent
gate. The candidate's blob ids (which an E5 pin table would have to name) are **not** the ids of any
published artifact — they identify my scratch bytes only.

**The real unresolvable pair is `corpus/SOURCES.md:171` and `:172`**, both
`7bb48f213ac677f943d5c791199ed3dddf302f00` (rows S230 badlogic/pi-mono, S231 mistralai/mistral-vibe);
`google-gemini/gemini-cli@451a02ff` and `zed-industries/zed@cfb894a5` are quoted context in both
gates. The line shape is "resolved to `badlogic/pi-mono` commit `7bb48f21…`" — the third-repo name
is a separate backticked token on the line and the hex is bare — so the plan's
"(or otherwise an explicit third-repository citation)" clause (line scope) is the load-bearing one,
not an in-token `owner/repo@<hex>` key.

**A base defect the grammar class would hide, not fix.** `.ufo/waves/round-79/snapshots/S230.fetch.json`
(pi-mono) records `main` at `bb65e3e49710fbd14f10c7792d0eaa6e2b2c5923` (blob sha1
`19d2bf28910ce49caaaf4dde86d1e96330ca7b31`, last commit touching the path
`25cc5c7bf4cbc76b2e134c729eb8d57d521ed749`), while `S231.fetch.json` (mistral-vibe) records
`7bb48f21…`. `corpus/SOURCES.md:171` — the S230 row — cites `7bb48f21…`, the **mistral-vibe** commit,
for the pi-mono row: the row names one repository and cites the other repository's commit. A
line-scoped class labels that line `repo badlogic/pi-mono` and clears it as INFO, which *hides* the
anchor defect. The cell is a `corpus/SOURCES.md` row — out of the grammar seat's write scope and out
of mine — so it belongs in the round-80 lesson as an erratum line (`Kb80E08C2Entry` reached the same
conclusion independently).

**The C2 entry's own citation hazard was real and is now closed by the entry owner's fix.** Against
the entry as first published, the class applied and the entry landed, I measured
`commit_unresolvable` **2 → 3** with the entry's line 125 as the third; the line read "The
mistral-vibe README was served from commit `7bb48f21…`", whose only repo hint is the bare name
`mistral-vibe` (no owner/repo token, no URL on the line) — so the class cannot key on it. The entry
owner's current bytes (sha256 `caadf57d6ba02de6ffdcd5d2d8bea33f0dbe79dadc85d7d33ef075251ad1df15`, 24,865 B, 159 lines)
carry **0** commit-shaped citations under the gates' own `COMMIT_RE` (only the in-set lane base
`398cbe1`), and with the class applied and that current entry landed I measured
`commit_unresolvable=0`, `commit_total=46` — the entry adds nothing to the red path. The fix landed
in the entry, which is cleaner than teaching the class to recognise a bare repo name.

**The cap-60 counter agrees, on my candidate bytes.** Running the published provisional cap-60
counter (`build/Kb80E06CounterErratum.cap60-provisional.py`) against my candidate world reads
*instruments added 60 / deleted 6 lines (cap 60)* with `instrument-size PASS`, `no-deletions
PASS`, `floors PASS`, `spotcheck-identity PASS`; the only guard that reds is `instrument-pin`,
which is expected (my scratch blobs are in no pin table — E5 must pin the reviewed bytes, which
will be the grammar seat's, not mine). That is the decisive number for the L1: a class that
clears both real blockers and carries a red-before arm in each gate **can** be written inside
the amended cap of 60; what remains is the pin table naming the right blobs.

**In the full stack world, the corpus gates' RED classes are all green.** Measured on
base + E04 + a compact grammar class + the current C2 entry + my symlink, with the published
provisional cap-60 counter: `instrument-size PASS` at exactly 60 added / 6 deleted, the only
structural guard red being `instrument-pin` (my scratch blobs are in no pin table — E5 must pin the
reviewed bytes, which will be the grammar seat's). The corpus gates read
`report_dead observed=0 PASS` (E04's `<rev>:` fix works) and `commit_unresolvable observed=0 PASS`
(the class works on the two real blockers); what still DRIFTs is the index/baseline pair —
`tracked_files 153`, `unindexed 2` (`corpus/lessons/round-79-verifier-spotcheck.md` and the new
`corpus/knowledge/allowed-tools-surfaces-round80.md`), `report_total 109`, `commit_total 46` — which
is seat Kb80E03IndexBaseline's coverage-map + refresh work, plus seat Kb80E01Registry's rows. On this
evidence the C1 stack's remaining work is the pin table, the index/baseline refresh and the registry
rows — the grammar class itself does not need to be bigger than 60 added lines.

**The runner's published stack reaches 6 of 6, and my symlink is load-bearing for two of the six
gates.** I applied `build/Kb80E10Battery.stack.patch` (sha256 `b82787f9…`) to a clean base clone and
measured it with the stack's *own* E5-amended counter (`verifiers/check_tip_battery.py` sha256
`ae29fc7b13971efd7adb115e1b54ebb76600c865c4a51471c9a93030a1ce7d08`, `LINE_CAP = 60`) at scratch commit
`0f46ee11…`: **both** required invocation forms — `--repo <absolute clone>` and `--repo .` from the
lane root — read `guards 5 of 5; tip battery exit 0: 6 of 6` with all six gates exiting 0 and the
counter exiting 0. The cap fits: numstat over the pinned base for the six scripts is 22/3 + 27/4 +
10/3 = **59 added / 10 deleted**, inside the cap of 60 — the runner's class is the lean shape, not the
171-line published candidate. Then the ablation: I removed **only** my
`.ufo/reports/round-76/kotoba.md` from that stack (commit `75da6b6e…`) and re-measured — **4 of 6,
exit 1**, with `verify_skill_checklist.py` and `check_assertion_floors.py` going red (the latter
because the checklist's live self-test arm re-reds on the same LOG.md:2818 token). With my symlink the
stack is 6 of 6; without it, 4 of 6. Nothing else in the stack substitutes for it. (This is a
stack-world measurement on the runner's published bytes at a scratch commit — the claim after-value at
the lane tip remains the L1's to record.)

**Independent corroboration of my item from seat `Kb80L03Symlink`** (their published worlds, which
measure my design without me): W1, my symlink in a **fleet-absent** parent, reads 1 of 6 — the link
dangles and **fails closed**, as I declared; W2, the same path as a **three-hop** symlink, reads 1 of
6 because the target lands on the link itself (a self-loop `ELOOP`) — the four-hop depth is not
cosmetic; W3, the same path as a **regular file** copied from the fleet file (bytes sha256
`a025051d…`), also greens the two gates at 3 of 6 but creates a second address for one artefact with
nothing keeping it equal to the fleet original; W4, my symlink plus a `../` rewrite of LOG.md:2818,
reads checklist exit 0; and W5, my symlink plus a **four-hop** rewrite of LOG.md:2818, reads checklist
exit 1 with `FAIL governance.citation_resolves … does not resolve` — the landmine confirmed by
another seat, from the other direction.

**My item is orthogonal to all of it**: `Kb80E02Symlink.patch` touches one path
(`.ufo/reports/round-76/kotoba.md`, mode 120000), adds **0** lines to the six battery scripts, and
leaves `verify_corpus_integrity --json` byte-identical before and after.

One observation about the lane tree, **not mine and not removed by me**: an untracked stray file
`.ufo/wapes` (594 B, created 2026-10-27 20:17, outside any seat's write scope) holds C2 quote-probe
output (`words=11 ok=False why='quote lies in the first-heading block (Q70)' …`). It is another seat's
probe writing to the lane root; it is untracked, so it does not affect the tracked tree or any gate,
and I did not create or delete it — I only note it, because a stray file at the lane root is exactly
the kind of thing a later sweep should see. My own writes are confined to
`.ufo/waves/round-80/build/` and `.ufo/waves/round-80/w1/`.

## 10. Tooling and scratch

No installs or upgrades were needed; no `pacman`, no host service changes — only `git`, `python3` and
coreutils, all present. Disk guard read once before the heavy passes
(`/home/vgpnk/Projects/shokunin/scripts/hyaku/disk-guard.sh status`: `/fast/scratch/hyaku` 27 %, 592.6 G
free). Scratch: `/fast/scratch/hyaku/kotoba-r80/Kb80E02Symlink/` — two fleet-shaped sandboxes
(`parent/` for the repaired world, `baseparent/` for the base world), each a `git clone --shared` of
the lane with every other fleet-root entry symlinked into the parent, plus `minclone/` for the §9
cross-check worlds and `tmp/` for `TMPDIR`; removed before yielding. No lane file outside `.ufo/waves/round-80/{build,w1}/` was written; no
commit, checkout, add or index operation in the lane (read-only git there only).

VERDICT: the ported one-path relative symlink `.ufo/reports/round-76/kotoba.md` (mode 120000, target four hops up = the fleet root, resolved sha256 equal to the fleet file's a025051d…) flips the checklist gate from exit 1 (10 PASS / 1 FAIL on LOG.md:2818) to exit 0 (11 PASS / 0 FAIL), the checklist self-test from 1 failure to 0 over 1863 assertions, the floors gate from exit 1 to exit 0, and the tip battery from 1 of 6 to 3 of 6 with all five guards still holding; corpus integrity and corpus independent outputs are byte-identical before and after, and the patch adds no backticked four-hop token to any tracked markdown.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E02Symlink.patch; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E02-symlink-identity.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E02-receipts.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E02-base-checklist.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E02-sym-checklist.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E02-base-checklist-selftest.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E02-sym-checklist-selftest.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E02-base-floors.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E02-sym-floors.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E02-base-integrity.json; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E02-sym-integrity.json; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E02-base-independent.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E02-sym-independent.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E02-integrity-diff.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E02-sym-tipbattery.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E02-sym-tipbattery-fleetwork.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/w1/Kb80E02Symlink.md; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E02-crosscheck-c1-stack.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E02-crosscheck-cand-counter.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E02-crosscheck-stack-counter.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E02-crosscheck-stack-integrity.json; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E02-crosscheck-stack-independent.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E02-crosscheck-cand-selftest-integrity.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E02-crosscheck-cand-selftest-independent.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E02-crosscheck-cand-integrity.json; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E02-crosscheck-stack6of6-counter-abs.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E02-crosscheck-stack6of6-counter-dot.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E02-crosscheck-ablation-counter.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E02-crosscheck-s08-integrity.json; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E02-crosscheck-entry-lands-green.txt
