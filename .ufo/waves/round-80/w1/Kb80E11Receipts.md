# Seat report — Kb80E11Receipts (independent receipt re-derivation, round 80 w1)

Seat: `Kb80E11Receipts` (leaf; receipts only — no patch, no counter edit, no corpus edit).
Base re-derived: `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`.
Scratch (all under `/fast/scratch/hyaku/kotoba-r80/Kb80E11Receipts/`, removed before this report was written): a `--shared` clone at base, a fleet-shaped sandbox (`fleet-shape/kotoba-shokunin` beside symlinks to every fleet-root entry, hidden entries included), a W2 symlink world, and scratch-only grammar-class probes C–G (none landed; each in its own throwaway clone).
Published receipt (one block per command: the command, its full output, its own exit status): `.ufo/waves/round-80/build/Kb80E11Receipts.txt` (1093 lines, 31 blocks).

**Every exit status below is the command's own**, captured as `cmd > f 2>&1; rc=$?; echo "exit=$rc" >> f`. No pipeline was used to read a verdict (M80-1). The M80-1 lesson is itself reproduced below, in both capture forms.

---

## 1. What I re-derived, and the verdict on each

### 1.1 The two object-presence probes (assigned explicitly)

`git cat-file -t 451a02ff` and `git cat-file -t cfb894a5`, in **three** repositories — the scratch lane clone at base, the lane itself (`/home/vgpnk/Projects/shokunin/kotoba-shokunin`), and the fleet root (`/home/vgpnk/Projects/shokunin`) — plus `git -C /home/vgpnk/Projects/shokunin cat-file -t` for both, as the brief asks.

**All six probes: `fatal: Not a valid object name <tok>`, exit 128.** Both objects are absent from the lane clone, the lane and the fleet root. Receipt blocks `catfile.txt` (lines 12–40 of the published file).

I also probed a third object, `7bb48f213ac677f943d5c791199ed3dddf302f00`, for the reason in §2: **`fatal: git cat-file: could not get object info`, exit 128, in the lane clone and the fleet root** — absent from both resolution sets.

### 1.2 The No-harm battery gates at base

| Command (cwd / args) | Own exit | Headline output |
|---|---|---|
| `check_gate_registry.py --rev 398cbe1…` | **1** | `gate registry rows conformant 60 of 62 lane verifiers; phantom 0`; the two reds are `check_desc_craft.py` and `check_r75_routed_repairs.py` ("no registry rows naming it: 0 (need 1)") |
| `check_assertion_floors.py` (fleet-shaped) | **1** | `FAIL checklist observed=1863 floor=1863 self_test_failures=1`; the other 15 rows PASS |
| `verify_skill_checklist.py` (fleet-shaped) | **1** | one FAIL: `governance.citation_resolves — LOG.md:2818: '.ufo/reports/round-76/kotoba.md' does not resolve`; the other 10 checks PASS |
| `verify_corpus_integrity.py` | **1** | 6 DRIFTs: `tracked_files` 152≠144, `unindexed` 1, `report_total` 109≠99, `report_dead` 1, `commit_total` 46≠43, `commit_unresolvable` 2; `3/9 checks pass` |
| `verify_corpus_independent.py` | **1** | `unindexed=1`, `commit_unresolvable=2`; `report_dead=0` (its extractor resolves `HEAD:`-prefixed bare `.ufo/reports/…` against the fleet root) |
| `check_correction_sweep.py --root .` | **0** | `correction sweep: 0 stale block(s)` |

Also run because the plan's No-harm battery names them: `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` → 23 W04 duplicate-URL warnings, `kotoba ok`, **exit 0**; `check_sibling_census.py` → **exit 1** with 16 province-row commit mismatches (a pre-existing fleet-drift red, identical in the lane root and in the scratch clone; it is not a round-80 regression and no round-80 file touches PROVINCE.md's `## Adjacent` table).

### 1.3 The tip battery at base, in all three argument forms

| Form | Own exit | Frozen line |
|---|---|---|
| `--repo .` from the lane root | **1** | `fleet root /home/vgpnk/Projects/shokunin; guards 5 of 5; tip battery exit 0: 1 of 6` |
| `--repo <absolute lane>` | **1** | identical line |
| `--repo <absolute scratch clone> --fleet <fleet root>` | **1** | identical line |

Per-gate exits inside the battery are identical in all three: registry 1, floors 1, checklist 1, integrity 1, independent 1, correction-sweep 0 → exactly **1 of 6** (only the correction sweep is green). Guards: no-deletions PASS, floors PASS, instrument-size PASS (22 added / 3 deleted vs cap 40), instrument-pin PASS, spotcheck-identity PASS → **5 of 5**.

**The plan's base clause is confirmed on its own terms.** `guards 5 of 5` and `tip battery exit 0: 1 of 6`, exit 1, in the `--repo .` form and in the absolute form, at the landed tip's base.

### 1.4 A measurement-shape caveat that changes two numbers

The plan's floors figure is `self_test_failures=1`. That is the **fleet-shaped** figure. In a plain scratch clone (directory named `clone`, no fleet siblings) the *same gate bytes* print `self_test_failures=2`, and `verify_skill_checklist.py` prints **three** FAILs instead of one (the extra two — `trigger.name_directory` and `trigger.citation_resolves` — are pure sandbox-shape artifacts: the lane directory is not named `kotoba-shokunin`, and `../.ufo/…` does not resolve).

**Consequence for the wave:** any world or repair scored outside a fleet-shaped sandbox (clone dir named `kotoba-shokunin` + fleet-root entries symlinked, hidden entries included) will read `2` where the plan reads `1`, and will read one extra checklist FAIL. The floor/ceiling arithmetic of the C1 stack must be scored in the fleet shape, or it will not match the plan's numbers. I hit this myself: my first fleet-shaped sandbox used `"$FLEET"/*` and silently skipped the hidden `.ufo`, which produced the same spurious extra FAILs; the receipt shows the corrected run.

### 1.5 M80-1 reproduced (pipe-read vs direct-read)

Same gate, two capture forms, at base:

* `python3 -B verifiers/verify_corpus_integrity.py | tail -1 ; echo $?` → the pipeline's last-element status: **0** for both corpus gates.
* `python3 -B verifiers/verify_corpus_integrity.py > f 2>&1; rc=$?` → the gate's own status: **1** for both.

Identical stdout in both forms, opposite verdicts. The lesson stands and is directly re-measurable.

---

## 2. Where my reading disagrees with the plan and with other seats

### 2.1 DISAGREEMENT (load-bearing): the two `commit_unresolvable` tokens are not `451a02ff`/`cfb894a5`

The plan's Trigger section says: *"The two `commit_unresolvable` tokens are `owner/repo@<hex>` citations of THIRD repositories (`google-gemini/gemini-cli@451a02ff`, `zed-industries/zed@cfb894a5`)"*, and the C1 repair-5 text keys the new grammar class on `owner/repo@<hex>`.

**Measured at base, by both corpus gates, identically:** the two counted unresolvable tokens are **the same object cited twice** —

```
commit_unresolvable: corpus/SOURCES.md:171: 7bb48f213ac677f943d5c791199ed3dddf302f00
commit_unresolvable: corpus/SOURCES.md:172: 7bb48f213ac677f943d5c791199ed3dddf302f00
```

(S230 pi-mono: *"page revision `main` resolved to `badlogic/pi-mono` commit `7bb48f21…`"*; S231 Mistral Vibe: *"served commit `7bb48f21…`"*.)

`451a02ff` and `cfb894a5` are classified **quoted** by both gates (they sit in double quotes or in a code span — the round-53/54 lesson context), and appear only in `commit_quoted_detail`. They are never counted as unresolvable. I confirmed this three ways: the gates' own `--json` site lists; the gates' own `commit_quoted_detail`; and my own enumeration of all 55 commit-shaped tokens through the gates' imported tokenizers (55 = 44 resolved, 6 quoted, 3 nonhash, **2 unresolvable** — receipt block `18-commit-token-enumeration.txt`).

`Kb80R02TipRecon` and `Kb80L01Grammar` report the same finding from their own runs; I reach it independently and add the token enumeration and the two probes below.

**Why it matters (not a naming quibble):** the plan's stated target shape for repair 5 does not exist in the corpus. I grepped for the `owner/repo@<hex>` shape *inside* a `commit \`…\`` token: **zero occurrences**. The 25 `owner/repo@hex` strings in the corpus all sit outside a `commit` token, so `COMMIT_RE` never fires on them and they are already invisible to the red count. The two tokens that actually carry the red are bare-hex `commit \`<hex>\`` citations whose third-party owner/repo is named in the *sentence* (S230) or only in the *row title/URL* (S231).

**Two scratch-only probes (never landed; probes C and D in the receipt):**

* **Probe C, narrow reading** — classify a token as external iff the token itself has the shape `owner/repo@<hex>`: `commit_unresolvable` stays **2**. The repair does not move the red.
* **Probe C, wide reading** — classify any bare-hex `commit` citation whose *line* names any owner/repo as external: `commit_unresolvable` → 0, but the external class swallows **24** tokens, including **resolvable lane commits** such as `corpus/README.md:23: 3b029b8`. That reading destroys the lane/fleet resolution the plan explicitly requires to be preserved ("Lane and fleet hex tokens keep the exact current resolution behavior").
* **Probe D, conjunctive reading** — external iff (i) the token does **not** resolve in lane or fleet **and** (ii) the citation sits in a sentence naming an owner/repo: `commit_unresolvable` → **0**, external = **exactly the 2** SOURCES.md sites, `commit_total` still 46, `commit_nonhash` still 0, and every resolvable lane/fleet token keeps its class. This is the shape that satisfies the plan's own constraints. It is the load-bearing finding for E05: **the conjunctive form is required; the narrow form is a no-op and the wide form over-captures.**

Caveat I must state plainly: the conjunctive form cannot distinguish S231 (which names its repo only in the row title/URL, not in the anchor cell) from a genuine lane break, by line-scoped context alone. Any E05 implementation needs that decision stated in its own spec; I am not repairing it (out of my scope).

### 2.1b The class needs TWO arms, and neither arm alone works (measured in both gates)

I built the class in four worlds and measured each. Two failures are worth stating because they are the shapes an implementer reaches for first:

* **Arm A (the plan's named shape, `owner/repo@<hex>`) must intercept BEFORE the hex/non-hex test.** If a citation is merely re-shaped to `owner/repo@<hex>` and the tokenizer still routes it through the "not a hex object" branch, the token lands in **`commit_nonhash` — observed 1** — and `commit_nonhash` is *also* a zero-mode class. The corpus gates then stay red on a different arm than the one the repair targeted. Measured (probe F, world "with-c2-entry-marked").
* **Arm B's resolution check must be a precondition.** The line-scope rule alone (no resolution test) over-captures **24** tokens into the external class, including **resolvable lane commits** — `corpus/README.md:23 3b029b8`, `:24 4002b9f`, `:25 a614927`, `:26 1d93182`, `:27 229b687`, `:28 397b29b8`, `:48 3b029b8`, `:49 8c300ad`, plus 16 more. That breaks the plan's own standing constraint that *"Lane and fleet hex tokens keep the exact current resolution behavior"*.

With both arms (external iff the token has the `owner/repo@<hex>` shape, **or** it is a bare hex that does not resolve in lane or fleet **and** its citation is at line scope in a third-repo context), the measured result is: `commit_total=46`, `commit_unresolvable=0`, `commit_nonhash=0`, external = **exactly** the 2 SOURCES.md sites, and every resolvable lane/fleet token keeps its class. That is the only form I measured that satisfies all of the plan's constraints at once. Receipt blocks `22`, `23`, `25`, `26`, `27`.

**A scope detail E05 must not inherit silently:** the anchor cell of `SOURCES.md:172` (S231) has **zero** owner/repo matches — its repo appears only in the row title/URL cell (`raw.githubusercontent.com/mistralai/mistral-vibe/…`). S230's anchor cell *does* contain `badlogic/pi-mono` in-line. A line-scoped rule catches both; an anchor-cell-scoped rule escapes S231 and leaves the red standing.

**The C2 entry is not a hazard in its current bytes.** `corpus/knowledge/allowed-tools-surfaces-round80.md` (build draft, sha256 `b89f0637ac66b60d6096d9a784e7f35c8fda4c6dbbb7b81d1409af4391bdba23`) carries **no** `commit \`<hex>\`` citation; its only 40-hex tokens are the lane base `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`, which resolves. With the class applied and the entry present: `commit_total=46`, `unresolvable=0`, `nonhash=0`, external=2 (only the SOURCES.md sites). An earlier draft of that entry *did* carry a bare `commit \`7bb48f21…\`` at line 125 and *did* add a third unresolvable — I measured that too — but the entry was rewritten mid-wave, so the hazard is discharged by the current bytes. It is recorded here because the entry was rewritten once and may be rewritten again.

### 2.1c The plan was amended mid-wave, and the amendment's wording needs one qualifier

The L1 amended `plans/round-80.md` line 11 in the lane working tree (credited to `Kb80V03Instruments`' audit) to: *"classify an explicit third-repository citation at line scope, and keep absent lane/fleet hashes unresolvable."* The locator is now correct and matches my measurement. The wording's second clause is the load-bearing qualifier and I have measured why it is needed: with the resolution precondition **as a precondition** (external iff unresolved **and** third-repo in scope), the external class is exactly the 2 SOURCES.md sites; **without** it, the line-scope rule alone over-captures 24 tokens including resolvable lane commits (block `25`). I flagged this to `Kb80E05GrammarFix` and `Kb80E10Battery`.

### 2.1d Peer claims I verified independently (no disagreement)

Three claims from `Kb80E08C2Entry` re-derived from primary bytes; all three confirmed (receipt block `28-peer-claim-verification.txt`):

* **The C2 entry carries zero commit-shaped citations.** Measured with the corpus gates' own tokenizer (`verify_corpus_integrity.COMMIT_RE`): 0 commit-shaped tokens; the only 40-hex token in the file is the lane base `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`, which resolves. The entry adds nothing to `commit_total` / `commit_unresolvable` / `commit_truncated` / `commit_nonhash`.
* **The S230 anchor cites the wrong repository's commit.** `S230.fetch.json` (pi-mono) names `main at fetch time = bb65e3e49710fbd14f10c7792d0eaa6e2b2c5923`; `S231.fetch.json` (mistral-vibe) names `7bb48f213ac677f943d5c791199ed3dddf302f00`; `corpus/SOURCES.md:171` (S230, pi-mono) carries the **mistral-vibe** hash. All three shas are absent from lane and fleet (`cat-file -t` exit 128); the pi-mono blob id `19d2bf28…` is a blob present in the lane (it is the committed snapshot's own git blob id) and absent from the fleet.
  **One consequence worth stating:** correcting that anchor cell to `bb65e3e4…` would **not** clear the corpus-gate red — that sha is also absent from lane and fleet, so it is also a third-repo citation. Only repair 5's grammar class clears the red. The erratum and the repair are independent and neither substitutes for the other. (The anchor cell is a protected SOURCES cell under rule 2, so the lesson-erratum route is the only in-scope one this round.)
* **The msaf surface is structurally unreachable under the r79 draft counter's Q70 rule — a counter defect, not a quote choice.** Running the draft counter's own `text_view` and `quote_location` on the committed `S229-msaf.html`: raw `allowed-tools` occurrences 1 (raw line 818); `text_view` yields 1550 lines; the draft's `first_head` = the first line starting with `#` = **index 168**, and that line is `# Auto-approve load_skill and read_skill_resource, but not run_skill_script.` — a **Python comment inside a code sample**, not a heading; the `allowed-tools` text-view index is **95**; `quote_location` returns `(False, "quote lies in the first-heading block (Q70)")` because 95 ≤ 168+1. The page's real `<h1 id="agent-skills">` is at **raw line 676**, i.e. text-view index ≈ **38** — *earlier* than the quote, so a heading-correct rule would **accept** it (95 > 38+1). The misfire is the `#`-prefix heuristic on an HTML text view. Reported to the counter owner (`Kb80E07C2Counter`); not repaired by me.

### 2.2 DISAGREEMENT (minor): the plan cites a base receipt that does not exist

The plan's Trigger line ends: *"(`receipts/tipbattery-base-dot.txt`, `tipbattery-base-abs.txt`)"*. `tipbattery-base-abs.txt` is **absent** from `.ufo/waves/round-80/receipts/` (only `census-before.txt`, `m80-1-pipe-vs-direct.txt`, `tipbattery-base-dot.txt` are committed, at `c2f69d4`). The absolute-form measurement exists nowhere in the tree. My receipt supplies it (blocks `19-tipbattery-base-abs-lane.txt`, `07-tipbattery-base-absclone.txt`).

### 2.3 AGREEMENT (and one clarification) with peer seats

* `Kb80R02TipRecon` and `Kb80L01Grammar`: same base battery figure, same `60 of 62`, same six DRIFTs, same token-mis-attribution finding. **No disagreement.** My addition: the fleet-shape caveat (§1.4) and the two grammar-class probes (§2.1).
* `Kb80E02Symlink` (build files `Kb80E02-base-*` / `Kb80E02-sym-*`): their base floors read `self_test_failures=1` and their symlink floors read PASS/exit 0 — **consistent with my fleet-shaped runs**, and their base checklist has exactly the one governance FAIL. Their floors delta confirms my own W2 measurement below.
* `Kb80E04DeadPointer`: their `integrity-repair.txt` shows `report_dead` 1 → 0 and their `tipbattery-repair.txt` shows `FAIL guard instrument-pin: verifiers/verify_corpus_integrity.py blob 051b8c5f… is not a pinned blob` and `guards 4 of 5` — **consistent with the plan's E5 erratum requirement** (the amended counter must pin that blob). Their measured `commit_unresolvable` is still 2 at `SOURCES.md:171/172`, matching my finding.
* `Kb80K02Patterns`: their `integrity-head.json` / `independent-head.json` carry `commit_unresolvable: 2` with the same site list I measured; their `sweep.txt` lists the `owner/repo@hex` occurrences at the same 25 sites.

---

## 3. One world I scored myself (W2), because it changes the stack arithmetic

I derived the W2 world **myself** from the r79 draft (the four-hop relative symlink `.ufo/reports/round-76/kotoba.md → ../../../../.ufo/reports/round-76/kotoba.md`), creating it by hand in my own fleet-shaped sandbox — not from any peer's receipt.

**W2 result: `guards 5 of 5; tip battery exit 0: 3 of 6`, exit 1.** Per-gate: registry 1, **floors 0**, **checklist 0**, integrity 1, independent 1, correction-sweep 0.

Two things follow, and the second is the important one:

1. The plan's W2 expectation ("expect ≤3 of 6, per the r79 receipt") is **satisfied exactly** — the symlink alone reaches 3 of 6.
2. **The symlink alone turns TWO gates green, not one.** The checklist goes green directly, *and* the floors gate goes green because the floors gate's `checklist` instrument measures the checklist's **live governance arm** — the same dead `LOG.md:2818` pointer that the symlink repairs. The plan's repair list treats the symlink as one repair among five; its arithmetic is right that W2 alone is short of 6, but any per-repair contribution table must credit the symlink with **two** gates (checklist + floors), because the floors red and the checklist red are the same defect seen by two gates. The plan's own note — *"the floors gate is red at base (checklist self-test live arm on LOG.md:2818)"* — names the same coupling; my measurement confirms it end-to-end.

---

## 4. Deliverables and evidence honesty

* Receipt file: `.ufo/waves/round-80/build/Kb80E11Receipts.txt` — 31 blocks; each block carries the exact command, its full stdout/stderr and its own `exit=` line. Where a command produced no output the block says so rather than being omitted; where a run was not performed the block is marked `[NOT PRESENT]` rather than being filled in.
* Every count above carries its command and its exit status.
* Nothing here is a gate verdict of record: the non-author closure and the L1 own verdicts. These are independent re-derivations for cross-checking.
* No tool was installed or upgraded (none needed). No host mutation, no pacman, no service restart. No lane mutation: the lane was read-only throughout (`git -C` reads and one `check_tip_battery.py` run that only writes inside `$TMPDIR`).
* Scratch directory `/fast/scratch/hyaku/kotoba-r80/Kb80E11Receipts/` removed after the receipts were copied into the build directory.
* Files written by this seat: the receipt file above and this report. No patch, no counter, no corpus edit, no edit outside `.ufo/waves/round-80/`.

VERDICT: Base re-derivation confirms the plan's frozen base clause in all three argument forms (`guards 5 of 5; tip battery exit 0: 1 of 6`, exit 1) and every per-gate exit, but disagrees with the plan on the load-bearing token identity — the red pair is `7bb48f21…` at `corpus/SOURCES.md:171/172`, not `451a02ff`/`cfb894a5` (which are quoted) — and my scratch probes C–G show repair 5's grammar class needs TWO arms with resolution as a PRECONDITION, or it is a no-op (in-token-only), over-captures 24 resolvable lane commits (line-scope alone), or trades one zero-mode red for another (the `owner/repo@<hex>` shape falling into `commit_nonhash`); I also measure W2 = 3 of 6 and show the symlink alone turns two gates green (checklist + floors, one defect seen twice), that the floors/checklist base figures are fleet-shape-dependent (`self_test_failures` 1 vs 2), and — verifying three peer claims from primary bytes — that the C2 entry adds no commit-shaped citation, that the S230 anchor cites the mistral-vibe commit (whose correction would NOT clear the red, since that sha too is absent from lane and fleet), and that the msaf surface is structurally unreachable under the r79 draft counter's Q70 rule (its `first_head` heuristic picks a Python code comment at text-view index 168 over the page's real heading at ~38, rejecting the one admissible quote at index 95) — a counter defect reported to its owner, not narrowed.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E11Receipts.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/w1/Kb80E11Receipts.md
