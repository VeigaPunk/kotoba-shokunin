# Kb80E14C1Worlds — C1 control worlds W0–W7 on the round-80 (E5-amended) counter

Seat: `Kb80E14C1Worlds` (C1 control worlds). Date: 2026-10-27.
Lane: `kotoba-shokunin`. Lane base: `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93` (r79 closure spot-check tip).
Deliverable: `.ufo/waves/round-80/build/Kb80E14C1Worlds.txt` (every battery output, own exit status, world diff `--stat`, and the corpus-gate class readings).

## 1. The counter I scored against (not derived by me)

The round-80 counter bytes are E06's published file, used verbatim:

| item | value |
|---|---|
| file | `.ufo/waves/round-80/build/check_tip_battery.amended.py` |
| sha256 | `15cc17614e61bdc47122bf501da951de3dbde6444b1ed4a98ca8192c2329ddba` |
| owner | `Kb80E06CounterErratum` (published; `Kb80E06CounterErratum.patch` + `.sha256` beside it) |
| E5 | `LINE_CAP` 40 → 60; `INSTRUMENT_PINS` gains `cc182613a4d089c41e44f11b50e03b45ce582dd8` (`verifiers/verify_corpus_integrity.py`, E04∘grammar) and `89f392daab3e4181db3ded7676ca0879871ef7ff` (`verifiers/verify_corpus_independent.py`); the self-test fixture constants re-anchored to `LINE_CAP` |
| self-test of these bytes | `self-test: 0 failure(s) over 69 assertions`, exit 0 (measured: `python3 -B check_tip_battery.amended.py --self-test`) |

Invocation, one command per world, the counter copied into the world clone's `verifiers/` and **not** committed (it is not one of the six instruments the guards measure, so committing it would be laundered into the world's diff):

```
cp <counter> <world-clone>/verifiers/check_tip_battery.py
cd <world-clone> && python3 -B verifiers/check_tip_battery.py --rev <world-rev> \
    --repo <world-clone> --fleet /home/vgpnk/Projects/shokunin
```

Every verdict below is the command's **own** exit status (`cmd > file 2>&1; rc=$?`), never a pipeline's. Each world is one scratch commit on the lane base in its own per-world clone (`git clone --shared`); each battery runs inside the counter's own fleet-shaped sandbox.

## 2. The world scoreboard

| world | construction | expected (plan) | MEASURED | verdict |
|---|---|---|---|---|
| W0 | base tree + empty commit | `guards 5 of 5; tip battery exit 0: 1 of 6` | `guards 5 of 5; tip battery exit 0: 1 of 6`, exit 1 | matches |
| W1 | registry rows only (r79 reviewed draft, 2 withdrawn rows) | ≤ 3 of 6 | `guards 5 of 5; tip battery exit 0: 2 of 6`, exit 1 | matches |
| W2 | the relative symlink only | ≤ 3 of 6 (r79 receipt parity: 3 of 6) | `guards 5 of 5; tip battery exit 0: 3 of 6`, exit 1 | matches (equals the r79 receipt) |
| W3 | coverage row + refreshed baseline only, no instrument repair | integrity still red on `report_dead` **and** `commit_unresolvable` | `guards 5 of 5; tip battery exit 0: 1 of 6`, exit 1; integrity exit 1 with `report_dead=1` **and** `commit_unresolvable=2` | matches |
| W4 | E04 report-pointer repair only | ≤ 3 of 6 | `guards 4 of 5` (instrument-pin FAIL, the E04-only blob `051b8c5f…` unpinned); `tip battery exit 0: 1 of 6`, exit 1 | matches |
| W5 | grammar class only, published candidate (`Kb80S07Quality-world.patch`) | ≤ 3 of 6 | `guards 3 of 5` (instrument-size FAIL 193 > 60 **and** instrument-pin FAIL on both gates); `tip battery exit 0: 1 of 6`, exit 1 | matches (the size FAIL is the candidate's size, not the class's effect) |
| W5b | grammar class only, **lean** variant (Y01's class minus the E04 hunk; 42 added lines) | ≤ 3 of 6, class effect visible | `guards 4 of 5` (instrument-pin FAIL on the grammar-only blob `67a668ce…`); `tip battery exit 0: 1 of 6`, exit 1 | matches; class effect visible |
| W6 | a battery instrument gutted (`verify_corpus_integrity.py` → two-line `sys.exit(0)` stub) | `instrument-pin` and/or `instrument-size` guard failure; **never** 6 of 6 | `guards 3 of 5` (instrument-size FAIL: loses 1473 lines > 60; instrument-pin FAIL); `tip battery exit 0: 2 of 6`, exit 1 | matches |
| W7 | a **base** spot-check file edited (`corpus/lessons/round-62-verifier-spotcheck.md`, its HEAD reference removed) | `spotcheck-identity` guard failure | `guards 4 of 5` (`FAIL guard spotcheck-identity: corpus/lessons/round-62-verifier-spotcheck.md differs from the base blob 2a247d6fe56b`); `tip battery exit 0: 1 of 6`, exit 1 | matches |
| W7b | the plan's **literal** W7 file edited (`corpus/lessons/round-77-verifier-spotcheck.md`: `git show HEAD:…` → `git show …`) | `spotcheck-identity` failure | `guards 5 of 5`; `tip battery exit 0: 1 of 6`, exit 1 — **no guard fires** | the plan's literal W7 is unreachable (see F5) |

**No world reached 6 of 6.** All ten worlds read ≤ 3 of 6 and every one exits 1. The C1 kill rule ("any world reaching 6 of 6 is a counter or guard defect and stops C1") is not triggered.

## 3. Corpus-gate class readings (the load-bearing evidence)

Run inside each world clone, own exit status appended (`verify_corpus_integrity.py --repo . --json`, `verify_corpus_independent.py --repo .`):

| world | `report_dead` | `commit_unresolvable` | `commit_external` | `unindexed` | exit |
|---|---|---|---|---|---|
| W3 (rows + baseline only) | **1** | **2** | 0 | 0 | 1 |
| W4 (E04 only) | **0** | **2** | 0 | 1 | 1 |
| W5 (grammar candidate) | 1 | **0** | **2** | 1 | 1 |
| W5b (grammar, lean) | 1 | **0** | **2** | 1 | 1 |

- **W3 — repairs 4+5 are load-bearing.** With the coverage row and a refreshed baseline but no instrument repair, integrity still reads `report_dead=1` (`corpus/lessons/round-77-verifier-spotcheck.md:15` `HEAD:.ufo/reports/round-77/kotoba.md`) and `commit_unresolvable=2` (`corpus/SOURCES.md:171` and `:172`, the *same* hash `7bb48f213ac677f943d5c791199ed3dddf302f00`). The refresh script itself refuses while a zero-mode class is nonzero; my W3 run carried the two known residuals (`--carry corpus.pointers.report_dead --carry corpus.pointers.commit_unresolvable`, exit 0), and the zero-mode expectations stay 0, so the drift stays red and named.
- **W4 vs W5b — the two repairs move different classes and neither alone suffices.** E04 moves `report_dead` 1 → 0 and leaves `commit_unresolvable` at 2; the grammar class moves `commit_unresolvable` 2 → 0 (the two tokens land in the new `commit_external` INFO class, naming `badlogic/pi-mono` and `mistralai/mistral-vibe`) and leaves `report_dead` at 1. Only E04 **and** the grammar class together clear both classes.

## 4. Findings for the L1

Numbering matches the deliverable `.ufo/waves/round-80/build/Kb80E14C1Worlds.txt` (F1–F11), so the two can be cross-referenced.

**F1 — no control world reaches the claim.** Ten worlds, ten readings ≤ 3 of 6, ten exits 1. C1's kill rule is not triggered.

**F2 — repairs 4+5 are load-bearing (W3).** Measured above; the baseline refresh cannot even complete without carrying the two residuals, and the residuals are exactly the two classes the instrument repairs own.

**F3 — the two repairs move different classes and neither alone is enough.** E04 (W4) moves `report_dead` 1 → 0 and leaves `commit_unresolvable` at 2; the grammar class (W5/W5b) moves `commit_unresolvable` 2 → 0 (the two tokens land in the new `commit_external` INFO class, naming `badlogic/pi-mono` and `mistralai/mistral-vibe`) and leaves `report_dead` at 1. Only E04 **and** the grammar class together clear both classes.

**F4 — the plan's named blocker tokens are not the counted ones.** The plan's Trigger names `google-gemini/gemini-cli@451a02ff` and `zed-industries/zed@cfb894a5`; both corpus gates classify those as `commit_quoted` context (already excluded) — I see them in the independent gate's quoted list in every world. The two counted blockers are `corpus/SOURCES.md:171` and `:172`, the same hash cited twice (rows S230/S231). A grammar class keyed only on the in-token `owner/repo@<hex>` grammar clears nothing; the class must fire at line scope. (Plan Addendum 2 records this correction; my measurements agree.)

**F5 — W7b: the plan's literal W7 is unreachable.** The only corpus file carrying a `HEAD:` pointer is `corpus/lessons/round-77-verifier-spotcheck.md`, and that file is **not** a base file at the counter's pinned base `072048fa` — it is reported as `INFO spotcheck added at …`, so editing it moves no guard (W7b reads `guards 5 of 5`). The reachable form of W7 is to edit a file that *is* a base spot-check file; W7 edits `corpus/lessons/round-62-verifier-spotcheck.md` and trips `spotcheck-identity` as the plan intends. The L1 should either amend the plan's W7 wording or keep W7's construction. **This is not a new finding**: the r79 seat recorded exactly this in `.ufo/waves/round-79/w1/Kb79E04DeadPointer.md` § 7 B3 ("the declared control world W7 is not blocked by the guard my item names") and then built the reachable form on round-62 and read the same failure. My W7b is r79's B3, independently re-measured on the round-80 counter.

**F6 — the size cap is tighter than the plan's sentence, and the pin guard carries the load.** The instrument-size guard diffs the six battery scripts against the **pinned r72 base `072048fa`**, not against the r80 base: 22 added lines are already spent at `398cbe1` (all in `check_assertion_floors.py`), E04 adds 17 → 39, leaving `60 − 39 = 21` added lines for a grammar class across **both** corpus gates. Measured consequences:
- the published grammar candidate spends 171 added lines → W5 trips `instrument-size` (193 > 60). Its *class* effect is still visible in the class readings (`commit_unresolvable` 2 → 0, `commit_external` = 2);
- the lean variant (W5b, Y01's class minus the E04 hunk, 42 added lines) stays inside the cap (`instrument-size` PASS) and shows the same class effect;
- every world that changes an instrument *without* being the reviewed composition trips `instrument-pin` **by name** (W4 `051b8c5f…`; W5/W5b the candidate's and lean blobs). That is the anti-laundering load the plan's kill rule names, working as designed.

  **Correction I owe the reader (measured, after a peer's challenge): a class-only patch IS pinnable.** I derived the class-only diff (E04-applied → composed: `+10/-4`) from primary bytes and applied it to the E04-applied file:

  | tree | integrity blob |
  |---|---|
  | base + E04 | `051b8c5f8676cba5c8d6047c8c9f7fcb56cd8f9f` |
  | base + E04 + that class-only diff | `cc182613a4d089c41e44f11b50e03b45ce582dd8` ← **the pinned blob** |

  So W5b's pin failure is **not** evidence that a class-only path is unpinnable: W5b reverted the E04 hunk *out* of the integrity file, so that file necessarily lacks E04 and its blob differs from the pinned one. W5b's *independent* blob is `89f392daab3e4181db3ded7676ca0879871ef7ff`, which **is** the pinned independent blob — W5b trips the pin on the integrity path only.

**F7 — the invocation forms agree.** W0 was run in both forms — `--repo <abs clone>` (used for all ten worlds) and `--repo .` from the lane root (`W0-dotform.txt`): same frozen line `guards 5 of 5; tip battery exit 0: 1 of 6`, same exit 1.

**F8 — the two pinned blobs are reproducible from primary bytes, and they belong to the Y01/E10 composed stack.** The amended counter pins `cc182613a4d089c41e44f11b50e03b45ce582dd8` (integrity) and `89f392daab3e4181db3ded7676ca0879871ef7ff` (independent). E16PinAudit and E04 independently recomputed both from primary bytes (base + `Kb80Y01-simplified.patch`, `git apply` rc 0) and they match; E04's own composed-stack receipts publish the same pair. I re-derived the integrity one myself (F6's table). **Consequence for the L1:** when E05's landed patch arrives, its two blob ids must equal these two, or the amended counter's pin table must be re-derived from E05's bytes — otherwise `instrument-pin` goes red at the tip.

**F9 — the S230 anchor carries a false attribution that a line-scope class would assert in a green line.** `corpus/SOURCES.md:171` is the S230 (pi-mono) row and cites `7bb48f21…`, which `S231.fetch.json` records as **mistral-vibe**'s head; `S230.fetch.json` records pi-mono's `main` at fetch time as `bb65e3e4…` (E12Census: the commit is absent from pi-mono and present in mistral-vibe; pi-mono at `7bb48f21` serves HTTP 404, mistral-vibe at `7bb48f21` serves 200). So the two counted tokens are one digest recorded twice, and one of the two rows is wrong about which repository it belongs to. The line-scope class prints `corpus/SOURCES.md:171: 7bb48f21… (repo badlogic/pi-mono)` — a green line asserting the wrong attribution. The round-80 lesson erratum is therefore load-bearing, not tidy: it is the only place the row's true provenance survives. (Measured by E08C2Entry and E12Census from the committed fetch records; my W5/W5b `commit_external_detail` readings are the shape of the green line in question.)

**F10 — two integration consequences for the L1** (from `Kb80V01C1`, consistent with my worlds):
- **The tip can never be the E04-only intermediate state.** My W4 shows why: the E04-only blob `051b8c5f…` is not a pinned blob, so an E04-only tree reads `instrument-pin` FAIL. E04 and the grammar class must land in **one** tree state before the tip is measured.
- **A registry row naming a verifier absent from the tree is a phantom red**, so E01's `check_allowed_tools` row and the C2 counter file must land in the same commit — the row must never precede the counter file. (V01C1's parser runs.)
- A third, from my own worlds: `check_gate_registry.py` has no `--repo` flag and reads `SKILL.md` from the **commit** — a worktree-only patch is invisible to it. My worlds committed everything, which is the right shape; a world that patched `SKILL.md` only in the worktree would have measured the base tree's registry and read 60 of 62.

**F11 — my worlds are C1-only, and the symlink is load-bearing for exactly two gates.** My trees carry no `verifiers/check_allowed_tools.py`, so every reading above is C1-only (`Kb80S15FreezeShas` makes the same point). And for W2's own item: `Kb80E02Symlink` measured the full stack **with** the symlink at 6 of 6 and **without** it at 4 of 6 (`verify_skill_checklist.py` and `check_assertion_floors.py` both red) — so the symlink is load-bearing for exactly two of the six gates. My W2 (symlink alone) reads 3 of 6, the expected partial: the symlink greens those two gates, the other four stay red.

## 5. What is provisional, and what I did not do

- **I did not derive the E5 counter.** E06's published bytes were used verbatim; I measured their self-test (0 failures over 69 assertions, exit 0) and recorded their sha256.
- **The grammar class is not E05's landed patch** — E05 published nothing under its own name at my run time. W5 uses the published candidate `Kb80S07Quality-world.patch` (S07's world, which S07 itself labels a candidate that must not be stacked with E05's patch). W5b is a variant **I derived** from Y01's published stack with the E04 hunk reverted out of `verifiers/verify_corpus_integrity.py` (42 added lines; `git apply -R` of `Kb80E04DeadPointer.patch` on the integrity file only, rc 0). Both are labelled in place in the deliverable.
- Because neither grammar variant produces the two pinned blobs, W5 and W5b trip `instrument-pin`. That is the pin guard working, not a defect in the worlds: a world that edits an instrument without being the reviewed composition *must* fail the pin.
- The world commits live in a scratch clone under `/fast/scratch/hyaku/kotoba-r80/Kb80E14C1Worlds/` and are **not** lane commits; the L1 integrates the real repair stack. My scratch dir was removed after the receipts were copied into the build dir.
- I ran no build, lint, or test suite of the lane; the only commands I ran are the counter, the two corpus gates, and the baseline-refresh script, each with its own captured exit status.

## 6. Files

- deliverable: `.ufo/waves/round-80/build/Kb80E14C1Worlds.txt` (515 lines: per-world battery output + exit + diff `--stat`, the corpus-gate class readings, and the findings above).
- per-world receipts (kept in the scratch tree during the run; summarised into the deliverable): `receipts/amended/W*.txt` (battery + `exit=`), `receipts/amended/W*.diffstat`, `receipts/gate-classes/W*-integrity.json`, `receipts/gate-classes/W*-independent.txt`, `receipts/W3-refresh.txt`.

VERDICT: All ten C1 control worlds score ≤ 3 of 6 and exit 1 on E06's published round-80 counter — no world reaches 6 of 6, the C1 kill rule is not triggered; W3 proves repairs 4+5 load-bearing (integrity still red on report_dead=1 AND commit_unresolvable=2), W7's spotcheck-identity fires while the plan's literal W7 file (W7b) cannot fire the guard, and the 21-line grammar budget left after E04 means only a lean class fits the cap.

DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E14C1Worlds.txt ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/w1/Kb80E14C1Worlds.md
