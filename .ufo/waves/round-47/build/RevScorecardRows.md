verdict: Round-47 SCORECARD edits are specifiable and safe only if all three claims are recorded as HELD (freshness 8, operability 8.5, calibration 8.5), no capability row enters, the stale round-47 "Before" values and the stale capability-shaped C3 are annotated append-only rather than rewritten, and every new backticked path in SCORECARD.md is checked against the governance citation gate (SCORECARD.md is itself a scanned governance file) — otherwise the round's own C3 target ("0 FAIL") breaks.

# RevScorecardRows — round-47 SCORECARD change specification (reviewer lane)

BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd` (`master`, tree clean except untracked `.ufo/waves/` and `plans/round-47.md`).
Contract source: `/home/vgpnk/Projects/shokunin/AXES.md` § Working the axes, § Capabilities, § The stagnation nudge, § SCORECARD.md contract.
Round plan: `plans/round-47.md:1-45` (claims C1 freshness / C2 operability / C3 calibration — note the plan **replaces** the capability-shaped C3 recorded at `SCORECARD.md:103`).
Before-measurements: `.ufo/waves/round-47/before/SUMMARY.md`.

This is advice to the L1 integrator. It is not an admission, it does not integrate anything, and it changes no production file.

---

## 0. Anchors at BASE (all `path:line` refer to BASE `c61a973`)

| Anchor | Location |
|---|---|
| axes table header | `SCORECARD.md:26` |
| depth row (owned) | `SCORECARD.md:28` |
| consistency sub-axis row (owned) | `SCORECARD.md:29` |
| coverage row (advisory) | `SCORECARD.md:30` |
| operability row (advisory) | `SCORECARD.md:31` |
| freshness row (advisory) | `SCORECARD.md:32` |
| calibration row (advisory) | `SCORECARD.md:33` |
| adjacency row (advisory) | `SCORECARD.md:34` |
| `## planned` | `SCORECARD.md:36` |
| stale round-47 planned block | `SCORECARD.md:100-104` (C1 `:101`, C2 `:102`, C3-capability `:103`, standing debt `:104`) |
| `## retired` | `SCORECARD.md:121` |
| `## Move log` | `SCORECARD.md:125` (round-46 table header `:225`, rows `:227-229`) |
| `## Capabilities` | `SCORECARD.md:231` (two rows `:235-236`) |
| `## Saturation` | `SCORECARD.md:242`; running-window refresh `SCORECARD.md:283` |
| governance citation gate | `verifiers/verify_skill_checklist.py:348` (`GOVERNANCE_FILES = ("LOG.md", "SCORECARD.md")`), `:347` (`CITATION_ROOTS`), `:304` (`INLINE_SPAN_RE`), `:1454` (`check_governance_citations`), `:1295` (`citation_resolve`) |
| floors registry / in-file tables | `verifiers/floors-registry.json`, `verifiers/check_assertion_floors.py:116-145` |
| corpus baseline | `verifiers/corpus-baseline.json` (`measured_against.observed.tracked_files = 58`) |
| corpus index | `corpus/README.md` (index rows; `corpus/lessons/round-46-verifier-spotcheck.md` currently unindexed) |
| S003 (XML-tag rule source) | `corpus/SOURCES.md:16` |
| the recorded absence the gate fails on | `LOG.md:2111` (token `.ufo/round-45/drafts/v10/post-r44-hunt.py`) |

---

## 1. Before-values measured by me (not copied from the summary)

Canonical layout = `/home/vgpnk/Projects/shokunin/kotoba-shokunin`. Scratch clone = `/fast/scratch/kotoba-r47/RevScorecardRows/lane` (detached at BASE).

| Command | Layout | Exit | Key output |
|---|---|---:|---|
| `PYTHONDONTWRITEBYTECODE=1 python3 -B verifiers/verify_surfaces.py --json` | scratch clone | **2** | `{"checks": [], "error": "opencode binary not found: /home/vgpnk/.opencode/bin/opencode", "exit_code": 2, "pass": 0, "fail": 0}` |
| `PYTHONDONTWRITEBYTECODE=1 python3 -B verifiers/check_substrate_pins.py` | scratch clone | **2** | `ERROR UNREADABLE opencode_binary_sha256 … /home/vgpnk/.opencode/bin/opencode`; `FAIL omp_binary_sha256: sha256 drift: expect=9513ef9f… got=fdbc8136…`; `FAIL omp_binary_mtime: … delta_ns=140082506863270`; `DRIFT 3/3 pins failed` |
| `PYTHONDONTWRITEBYTECODE=1 python3 -B verifiers/verify_skill_checklist.py --json` | **canonical** | **1** | `pass 9 fail 1 na 0`; sole FAIL `governance.citation_resolves :: LOG.md:2111: '.ufo/round-45/drafts/v10/post-r44-hunt.py' does not resolve from /home/vgpnk/Projects/shokunin/kotoba-shokunin` |
| same command | scratch clone (`…/lane`) | **1** | `pass 7 fail 3` — `trigger.name_directory` (dir renamed), `trigger.citation_resolves` (41 unresolvable), `governance.citation_resolves` (25 unresolvable) ⇒ **the checklist gate is layout-sensitive** |
| `PYTHONDONTWRITEBYTECODE=1 python3 -B verifiers/verify_corpus_integrity.py --json` | scratch clone | **1** | DRIFT `corpus.index.tracked_files` observed 59 vs expected 58; DRIFT `corpus.index.unindexed` observed 1 → `["corpus/lessons/round-46-verifier-spotcheck.md"]` |
| `PYTHONDONTWRITEBYTECODE=1 python3 -B verifiers/verify_corpus_independent.py --json` | scratch clone | **1** | DRIFT `corpus.index.unindexed` observed 1 (same file); `tracked_files`/`report_total`/`commit_total` are **observe-mode INFO**, not DRIFT |
| `grep -c '<skills>' SKILL.md` | canonical | — | `8` (whole file). Frontmatter-scoped count = **1** (the single `<` in the frontmatter is `SKILL.md:14`, `never reach the \`<skills>\` router`) |
| `awk` frontmatter scan | canonical | — | exactly one `<` in the frontmatter block (line 14) ⇒ the C2 after-value "0" is reachable by a one-token edit |

Baseline pin state at BASE (`verifiers/baseline.json`): `omp_binary_sha256 = 9513ef9f…` (18.12.2), `omp_binary_mtime = 2026-10-19T12:35:55.628…`, `opencode_binary_sha256 = d9123b9b…`; observed omp is `fdbc8136…` (18.12.5). The opencode default path in **both** `verifiers/check_substrate_pins.py:63` and `verifiers/verify_surfaces.py:130` is `/home/vgpnk/.opencode/bin/opencode`, which no longer exists on this host — so "3/3 pins at the **default** resolution" (the plan's after-target) requires moving that default to the 1.19.3 npx-cache ELF path, not only re-pinning the sha.

---

## 2. The axes rows — per-claim score delta, evidence pointer, counting command, measured-commit placeholder

### 2.1 C1 → `freshness` row (`SCORECARD.md:32`)

**Score delta: HELD at 8.0 (default). Conditional 9.0 only if BOTH conditions below are met and recorded.**
- (a) the opencode half of the loader surface is machine-covered and **non-vacuous** by re-derived rules (OC-1/OC-4/OC-6 actually match in the 1.19.3 binary), and the omp half's `no_uncovered_class` check is non-vacuous (the BASE failure mode: "omp vacuity 0/8 loader classes" per ``.ufo/waves/round-47/before/SUMMARY.md:4``);
- (b) a **named non-author lane** in wave 2 independently re-measures the re-derivation (rubric band 9 = "machine-checked or externally audited"; band 10 would additionally need repeated non-author verification in the opposite direction).

**Why held by default (counterexample CE1).** "The gates go green ⇒ freshness 9" is refuted by this lane's own recorded reasoning on the sibling row: `SCORECARD.md:30` ("`surfaces.no_uncovered_class` is vacuous by construction for opencode … so the machine check covers the omp `.md` set, not the coverage claim" — band 9 withheld, 8.0 landed). The same asymmetry applies to freshness: a green `verify_surfaces.py` proves the omp loader set only, and the opencode half stays prose-covered. Additionally, the freshness row has been **held at 8** across rounds 38–46 (`SCORECARD.md:32`, "Score held: round rejected on C1" ×5) while its cited evidence was already machine-checked; a green gate is a restoration of a red, not a band move. Precedent for "improved-bounded, score held" is `SCORECARD.md:33` and `:219` (round 46, all three axes held).

**Required row text elements**
- Score cell: `8` (unchanged) — if condition (a)+(b) are met: `8.5` is *not* supportable without a named non-author lane; the fractional step needs one of the two criteria of band 9 met, so a machine-covered-both-halves + non-author re-measure supports **9**, and the row must then name the reviewer seat. Default text: `**round 47 (C1 — improved-bounded; freshness holds 8):** …`.
- Counting commands (unchanged across rounds, they must stay literally re-runnable):
  - `python3 -B verifiers/verify_surfaces.py --json` → **7/7 PASS, exit 0** — at the **default** resolution.
  - `python3 -B verifiers/check_substrate_pins.py` → `OK 3/3 pins hold`, exit 0 — at the **default** resolution.
  - The row must name the **new default opencode path** (the 1.19.3 npx-cache ELF), because the current default (`/home/vgpnk/.opencode/bin/opencode`) is dead; a row that cites the commands without the new default is not reproducible by a reader.
- Evidence pointers (each must exist at the landing commit — see §6 F1): the r47 re-derivation record (extraction rules + omp 18.12.5 version/sha256/mtime + opencode 1.19.3 sha256), the wave-2 falsify matrix, and the post-landing floors vector.
- Measured commit placeholder: `<measured-commit>` → the row must carry the 8-hex landing prefix (e.g. `abc1234…`) for the commit that carries the re-pin; `…` inside a token is the schematic form the governance pass excludes (`verifiers/verify_skill_checklist.py:349`, `:1422-1426`), so `abc1234…` is safe in a backticked token.
- Mandatory **append-only correction**: the round-47 planned block's before-values (`SCORECARD.md:101`, "Before: surfaces 5/7, pins 1/3") are **stale** (CE2 below). The round-47 entry must state the measured before-values (surfaces exit 2 `opencode binary not found`; pins exit 2 `DRIFT 3/3 pins failed`) and annotate the stale line; it must not be edited in place.
- `Last change` cell → `47` (status field; see §6 F5).

### 2.2 C2 → `operability` row (`SCORECARD.md:31`)

**Score delta: HELD at 8.5.**
Reason: the claim adds one machine check with a discriminating fixture and a self-test floor — but 8.5 already carries band 9's half-criterion ("machine-checked"), and the row's own cited evidence still records 33 of 41 boxes unexecuted and the r46 residuals (mirror opt-out, missing verdict, `NaN`/case-variant shadow keys) surviving (`SCORECARD.md:31`). The lane has held 8.5 through rounds 38–46 with machine-checked evidence each time. A move to 9 needs the checklist surface machine-covered (or the band-9 criterion fully met + a named non-author re-measure).

**Required row text elements**
- Score cell: `8.5 — was 8.0` → `8.5` (unchanged), evidence prefixed `**round 47 (C2 — improved-bounded; operability holds 8.5):**`.
- Counting commands:
  - `python3 -B verifiers/verify_skill_checklist.py --json` → **0 FAIL, exit 0**, with the measured PASS count (BASE 9 + the governance fix + the new description check ⇒ the plan's "10/10 (11/11 with C2)" at `plans/round-47.md:38` is a **plan estimate, not a measurement**; the row must carry the measured number, whatever it is).
  - `python3 -B verifiers/verify_skill_checklist.py --self-test` → `0 failure(s) over N assertions` with N ≥ 1597 (BASE floor) and the planted-tag fixture **FAILing** while every tag-free control stays green.
  - `python3 -B verifiers/check_assertion_floors.py` → all rows PASS at observed = floor (the in-step floor bump; see §6 F3).
  - Frontmatter before/after counter: `grep -c '<skills>' <(sed -n '/^---$/,/^---$/p' SKILL.md)` → 1 at BASE, **0** after (frontmatter-scoped; the whole-file count is 8 and must not be used as the counting command).
- New check id: the row should name it explicitly (suggested `trigger.description_no_xml_tag`, consistent with `trigger.frontmatter_parses` / `trigger.literal_trigger_string` at `verifiers/verify_skill_checklist.py:67-87`); the row's count must match the implementation's check list.
- Evidence pointers: the check id + fixture path + the S003 source row (`corpus/SOURCES.md:16`) + the wave-2 matrix + the post-landing floor vector.
- Measured commit placeholder: `<measured-commit>` (8-hex prefix of the landing commit that carries both the verifier change and the `SKILL.md` description edit — they must land together, since the check would otherwise FAIL the lane's own file).
- **Mandatory scope-honesty note** (CE6, §6 F8): the rule is adopted from S003's XML-tag clause only. The same S003 row also states "body under 500 lines"; this lane's `SKILL.md` is **525 lines** (BASE checklist detail: `525 lines within budget 600`). The row must name the body-length clause as **not adopted** (named residual) or it overclaims S003 conformance.
- **Mandatory cross-claim note**: the `<skills>` removal changes this lane's own router-visible description (BASE: `description 814 chars`) and, per `SKILL.md:22-33`'s own mechanics, the omp description-cache key is `(name, description-as-loaded)` — the description edit therefore changes that key. The freshness row (C1) and the depth row's loader claims must cross-reference this; the row may state that the effect is inert here because the file is not in an omp skill discovery root (`SKILL.md:12-15`), but it may not stay silent.
- `Last change` cell → `47`.

### 2.3 C3 → `calibration` row (`SCORECARD.md:33`)

**Score delta: HELD at 8.5.**
Reason: the claim makes the records match repo state (checklist 0 FAIL; both corpus gates 0 DRIFT) and installs a new fail-closed mechanism (the governance erratum registry) — a genuine improvement in the class, but 8.5 already carries band 9's half-criterion and **no non-author lane has yet verified the new registry in the opposite direction** (the registry's own calibration is unmeasured). Same shape as round 46: "calibration improved as registered, class improved-bounded; score held 8.5" (`SCORECARD.md:33`, `:219`).

**Required row text elements**
- Score cell: `8.5 — was 8.0` → `8.5` (unchanged), evidence prefixed `**round 47 (C3 — improved as registered; calibration holds 8.5):**`.
- Counting commands:
  - `python3 -B verifiers/verify_skill_checklist.py --json` → 0 FAIL, exit 0 (governance.citation_resolves now PASS through the registry, **not** by editing `LOG.md:2111`).
  - `python3 -B verifiers/verify_corpus_integrity.py --json` → 0 DRIFT, exit 0.
  - `python3 -B verifiers/verify_corpus_independent.py --json` → 0 DRIFT, exit 0.
- Evidence pointers: the erratum registry path (new file under `verifiers/`), the `corpus/README.md` index row that covers `corpus/lessons/round-46-verifier-spotcheck.md`, the corpus baseline re-record note (`verifiers/corpus-baseline.json` `measured_against.note` — the lane's idiom appends the move to the note), the registry's self-test result, and the post-landing floors vector.
- Measured commit placeholder: `<measured-commit>`.
- **Mandatory honesty note** (CE3 / F10): the corpus DRIFT has **two distinct causes** that must be named separately — (i) `corpus.index.unindexed = 1` (the unindexed file — fixed by the index row), and (ii) `corpus.index.tracked_files 59 ≠ 58` (the baseline count — fixed by the baseline re-record). Conflating them into one "index fix" would misstate what changed. The row must state the baseline move `58 → <r47 count>` and that the index row is what removes `unindexed=1`.
- **Mandatory mechanism note** (F2): the registry must be described as **pinned and fail-closed**, and the row must state what happens when a recorded absence ends (the registry entry must then FAIL, not silently pass) and when the cited line changes (stale entry FAILs). A permissive allowlist would be a laundering channel of the same shape the depth row closed in rounds 39–44 (`SCORECARD.md:28`).
- `Last change` cell → `47`.

### 2.4 Rows that must NOT move

`depth` (`SCORECARD.md:28`), `consistency` (`:29`), `coverage` (`:30`), `adjacency` (`:34`): round 47 changes no verifier, corpus entry, owned surface, or sibling route for these. Per `AXES.md` § Working the axes ("no axis is harmed" + a score moves only when its band is met), they keep their scores, and their `Last change` cells stay as they are except for the correction discussed in F5 (status field, not history).

---

## 3. Move log (`SCORECARD.md:125`) — three new rows, one per claim

The round-46 table is at `SCORECARD.md:225-229`; the round-47 table is appended after it (append-only — never edit round-46 rows). Column shape is fixed: `| Round | Axis | Before | After | Evidence |`.

```
| 47 | freshness | 8 — surfaces exit 2 `opencode binary not found`; pins exit 2 `DRIFT 3/3 pins failed` (omp 18.12.2→18.12.5 rebuild; opencode default path dead) | 8 (held) — surfaces 7/7 exit 0 and pins 3/3 exit 0 at the default resolution after the re-derivation + re-pin; opencode half non-vacuous only if OC-1/OC-4/OC-6 match; <no score move: band 9 needs a named non-author re-measure> | `<measured-commit>`; `.ufo/round-47/evidence/c1/…`; floors vector |
| 47 | operability | 8.5 — no check on the frontmatter `description` XML-tag rule; the lane's own description carries `<skills>` (frontmatter count 1); checklist 9 PASS / 1 FAIL | 8.5 (held) — new machine check + discriminating fixture (planted tag FAILs, tag-free controls green); the lane's own description reaches 0 tags; checklist 0 FAIL exit 0, self-test 0/N (N ≥ 1597) with the floor bumped in step | `<measured-commit>`; new check id + fixture; `corpus/SOURCES.md` S003 |
| 47 | calibration | 8.5 — checklist `governance.citation_resolves` FAIL at `LOG.md:2111` (a recorded absence with no erratum mechanism); corpus integrity DRIFT `tracked_files 59≠58` + `unindexed 1`; corpus independent DRIFT `unindexed 1` | 8.5 (held) — pinned fail-closed erratum registry covers the recorded absence (the LOG line itself is not edited); index row covers `corpus/lessons/round-46-verifier-spotcheck.md`; corpus baseline re-recorded 58→<r47 count>; both corpus gates 0 DRIFT, checklist 0 FAIL | `<measured-commit>`; erratum registry + self-test; `corpus/README.md` index row; `verifiers/corpus-baseline.json` note |
```

Rules for these cells:
- **Before** = the measured before-value at BASE (not the stale plan text — CE2).
- **After** = the measured after-value at the landing commit, or the word `held` with the reason; never a plan target.
- **Evidence** = a pointer that exists at the landing commit (F1) and, for anything under `.ufo/waves/`, a note that wave artifacts are untracked (`.ufo/waves` has 0 tracked files at BASE) — the LOG.md:2111 class (M4, `corpus/lessons/round-46.md:42`) is exactly this failure.
- A `held` cell must carry the reason inline; the lane's own idiom is `9 (held) — …` (`SCORECARD.md:228`).

---

## 4. Capabilities (`SCORECARD.md:231`) — **no row may enter**

- The plan replaces the capability-shaped C3 (`SCORECARD.md:103`, "C3 — capability (sources curation with outside re-open)") with a **calibration** claim (`plans/round-47.md:33-40`). Per `AXES.md` § Capabilities, "Rows enter only through a round that demonstrates the capability running … a capability without a passing demonstration in the round report is pre-claiming and does not enter the table." Round 47 demonstrates no capability, so **the table keeps exactly two rows**: substrate-pin guard (first-working round 23) and assertion-floor guard (round 29), both unchanged.
- **Flagged temptation (must be refused):** the governance erratum registry is capability-shaped (a reusable fail-closed mechanism). If any round-47 artifact describes it as a capability, that description must not reach the table. It may be named in the round-48 planned row as a *candidate* (with the demonstration still owed), which is what `AXES.md` permits.
- **Flagged second temptation:** the substrate-pin guard row (`SCORECARD.md:233`) is the mechanism C1 re-pins. Its row text says the guard "hashes the live omp and opencode binaries" — after the r47 re-pin the opencode default path changes, so the row's evidence pointer must still be re-runnable. The guard's *capability* does not change (same name, same first-working round 23); only its pinned inputs move. If the integrator edits that row's prose, it must be an append-only annotation, not a rewrite of the first-working-round snapshot (the file already carries that precedent at `SCORECARD.md:238`, the round-41 annotation).

---

## 5. `## planned` (`SCORECARD.md:36`) — the round-47 block and the round-48 block

### 5.1 Disposition of the existing round-47 block (`SCORECARD.md:100-104`)

That block is the **pre-registered** claim set. It is now stale in three ways and must be handled **append-only**:
1. its before-values ("Before: surfaces 5/7, pins 1/3", `SCORECARD.md:101`) are false at BASE (CE2) — the round-47 entry records the measured before-values and annotates the stale line;
2. its C3 is capability-shaped and was re-planned as a calibration claim (`plans/round-47.md:33`) — the round-47 entry must say so and must not record a capability;
3. it says "scores move only if the rubric band is met" (`SCORECARD.md:100`) — the round-47 entry answers that per claim (§2).

Do **not** delete or edit `SCORECARD.md:100-104`. Append a `**Round 47 completed …**` block after it (the file's own idiom: every past round keeps its "Round N completed" paragraph, e.g. `SCORECARD.md:98`), and append the new `**Next: round 48 …**` block after that.

### 5.2 `**Next: round 48**` — proposed planned row (3 claims, distinct axes, causally separable)

Requirement recap (`AXES.md` § Working the axes): 1–3 claims, distinct axes, causally separable, each with its own falsifiable before→after, **and at least one claim on the lane's lowest-scoring non-retired axis**.

Proposed (the L1 may re-cut it, but the axis coverage below is what the SCORECARD must carry):

- **C1 — depth 9 (the lane's **owned**-axis obligation; see F6):** close the r46 spot-check residuals that round 47 carries — the comparator's mirror opt-out, the missing-verdict door, and the `NaN`/case-variant shadow keys — at the landing bytes, with a named non-author re-verification. This is depth's band-10 path ("repeated non-author verification in the opposite direction", `SCORECARD.md:17-19`). Count: the residual arms exit 2 class-named at `<measured-commit>`, plus the comparator's own self-test floor (BASE 330) and the corpus census doc updated. Evidence: wave-2 matrix + census doc pointer.
- **C2 — freshness 8.0 (the lowest non-retired axis under the all-axes reading; tie with adjacency 8.0):** make the r47 re-derivation a **committed, re-runnable artifact** (extraction rules + substrate provenance for both halves) so the next omp/opencode rebuild is caught by two commands instead of by a fresh census, and extend the machine gate so the opencode half is non-vacuous. Count: `python3 -B verifiers/verify_surfaces.py --json` → 7/7 exit 0 with the opencode classes matched; `python3 -B verifiers/check_substrate_pins.py` → `OK 3/3 pins hold` exit 0. Evidence: the committed derivation artifact + the census doc + the floors vector.
- **C3 — calibration 8.5:** a non-author re-measure of the **erratum registry's own fail-closed behaviour** (an entry whose recorded absence has ended must FAIL; a stale entry must FAIL; a permissive entry must be rejected) + the corpus baseline/index reconciliation carried to the r47 file set. Count: `python3 -B verifiers/verify_skill_checklist.py --json` → 0 FAIL; `python3 -B verifiers/verify_corpus_integrity.py --json` → 0 DRIFT; `python3 -B verifiers/verify_corpus_independent.py --json` → 0 DRIFT; registry self-test 0/N. Evidence: the registry + its self-test + the corpus baseline note.

Standing debt to carry in the round-48 block (from `SCORECARD.md:104` and the r46 rows): snapshot-pinned carrier for the scoped-out probe (HIGH-3); mirror opt-out + missing-verdict door; record-level `kind` drift; payload-selectable committed scope-outs; the divergence merge (operator, never rebase); the SHONEN form; IND self-test hang under wave load; resolver-vs-brace tokenizers.

### 5.3 Saturation refresh (`SCORECARD.md:242`, running window `:283`)

Append a new running-window paragraph after `:283` (do not edit `:283`):

> **Running window (round-47 refresh):** no capability row has entered since round 29 (rounds 30–47 dispatched, none added a row) — the window remains long past 3/3; the nudge stays **dormant** because depth (9) sits below the 10.0 owned-axis line. Round 47 added no capability row: the plan's C3 was re-cut as a calibration claim (`plans/round-47.md`), so the capability table is unchanged (two rows, `:235-236`, first-working rounds 23 and 29), and the governance erratum registry is a **candidate** only — AXES.md § Capabilities admits a row solely through a round that demonstrates the capability running. `PROVINCE.md` carries a Frontier inventory (round 46), so a nudge-fired round would have frontier ground to move.

Consistency requirement: the Saturation section's present-tense advisory list ("coverage 8.5, operability 8.5, calibration 8.5, freshness 8.0, adjacency 8.0", `SCORECARD.md:274`) stays true **only because §2 holds all three scores**; if any score moves, that list and the "Current state: consistency 10 … depth 9" line (`SCORECARD.md:254`) must move with it in the same edit.

---

## 6. Findings (severity-ordered) — every one is actionable for the L1

**F1 (HIGH) — the SCORECARD edit can break the very gate the round is closing.**
`SCORECARD.md` is itself a scanned governance file (`verifiers/verify_skill_checklist.py:348`), and the extractor scans **backticked** spans only (`INLINE_SPAN_RE` `:304`) whose token starts with `corpus/ verifiers/ opencode/ .ufo/ ../` and contains `/` (`CITATION_ROOTS` `:347`). Every such token is resolved at run time (`:1295`). Consequence: if the round-47 rows cite a path that does not exist at the landing commit — e.g. the round report path before it lands, or any `.ufo/waves/round-47/…` artifact after the wave directory is pruned — the checklist gate FAILs on the *new* text and C3's "0 FAIL" target is broken by the record itself. This is not hypothetical: the BASE failure is exactly this class (`LOG.md:2111`, token `.ufo/round-45/drafts/v10/post-r44-hunt.py`, absent because the drafts were pruned; recorded as M4 at `corpus/lessons/round-46.md:42`).
Mitigations, all available: (i) backtick **only** paths that exist at the landing commit; (ii) write not-yet-existing paths **unbackticked** (the extractor cannot see them — verified from the code path, `:1392`); (iii) use the schematic `…` form, which the governance pass excludes (`:1422-1426`).
**CE3 (counterexample):** "citing the round report path is harmless because the report will exist" is false at the moment the gate runs; the report is produced after the SCORECARD lands.

**F2 (HIGH) — the erratum registry can become a laundering channel unless it is pinned and fail-closed.**
The plan's C3 asks for "a pinned, fail-closed erratum registry for recorded absences" (`plans/round-47.md:35`). If the registry is merely a list of paths that the governance check skips, then adding a path turns the gate green without the recorded absence being fixed — the same laundering shape the depth row closed for scope-outs across rounds 39–44 (`SCORECARD.md:28`) and the same shape the pins guard closed in round 23 (`PIN_ABSENT`/`VACUOUS`, `SCORECARD.md:233`).
Required properties, which the C3 row must state: each entry carries (file, line, token, the recorded fact that justifies the absence, and that fact's evidence pointer); the registry is digest-pinned outside the file it guards (the lane's existing anchor pattern: `verifiers/floors-registry.json` as the external anchor for `verifiers/check_assertion_floors.py:116-145`); an entry whose cited line no longer matches FAILS; an entry whose path has since appeared FAILS (the absence ended); a missing/empty registry FAILS closed, not vacuous.
**CE4 (counterexample):** "the registry makes the governance gate green" is not evidence of calibration — a permissive allowlist produces exactly that green while the recorded absence stays unfixed.

**F3 (MED) — the floors bump-in-step coupling is a hard precondition of three of the rows.**
BASE floors vector: `10 / 150 / 91 / 87 / 1597 / 62 / 104 / 330 / 150` (harness, corpus_integrity, corpus_independent, surfaces, checklist, pins, harness_independent, compare_harness_independent, floors_guard) — `verifiers/floors-registry.json` + the two in-file tables at `verifiers/check_assertion_floors.py:116-145`. C1 changes the surfaces and pins self-test counts, C2 changes the checklist's, C3 changes the corpus gates'. The bump must land in the **same change** as the instrument edit (registry + both tables + guard docstring), or the floors guard fails — and if the SCORECARD row cites a floor vector, it must be the **post-landing** vector. Count: `python3 -B verifiers/check_assertion_floors.py` → all rows PASS at observed = floor.

**F4 (MED) — the pre-registered before-values are false at BASE and must be corrected in the round-47 entry, not in place.**
`SCORECARD.md:101` says "Before: surfaces 5/7, pins 1/3". Measured: `verify_surfaces.py --json` → exit **2** (`opencode binary not found`), `check_substrate_pins.py` → exit **2** (`DRIFT 3/3 pins failed`). **CE2 (counterexample):** "the planned before-state (5/7, 1/3) is the before-state" is refuted by the measurement; a round-47 entry that repeats 5/7 misstates its own before-value — exactly the class of defect this lane's calibration row exists to catch (`SCORECARD.md:33`, round 46's "uncommitted can…" correction).

**F5 (MED) — the `Last change` column is stale for every row, and the round-47 edit touches three of them.**
Values at BASE: depth 15, consistency 15, coverage 15, operability 16, freshness 21, calibration 17, adjacency 21 (`SCORECARD.md:28-34`) — while the same rows cite evidence from rounds 43–46. `AXES.md` § SCORECARD.md contract requires "last-change round" per row, so the column is currently a false present-tense claim.
Recommendation: re-stamp the three rows round 47 touches to `47` (a status field, not history — this is not a rewrite), and either re-stamp the other four from their own evidence text (depth → 46, operability → 46, freshness → 43, calibration → 46, adjacency → 26, coverage → 15) **or** record the staleness as named calibration debt. Do not use this column to re-attribute a score.

**F6 (MED) — the "both readings" assertion is unsupported under the owned-axis reading.**
`SCORECARD.md:283` closes with "round 47's C1 satisfies both readings". The all-axes reading is satisfied (freshness 8.0 is the lowest non-retired axis). The **owned** reading is not: the lane owns depth (9) and the consistency sub-axis (10) (`SCORECARD.md:3-4`, `:28-29`), so the lowest-scoring owned non-retired axis is depth (9), and round 47 carries no depth claim (`plans/round-47.md:25-42`). `AXES.md` § Working the axes: "At least one claim works the lane's lowest-scoring non-retired axis" — under the owned reading that obligation points at depth. Two honest resolutions: (i) the round-47 entry states explicitly under which reading the round is admitted (all-axes), and the owned-reading obligation is discharged in round 48 (the proposed C1 is a depth claim); or (ii) the assertion at `:283` is annotated with its limit. Silence is the one option that is not available — the assertion is currently a claim the round does not support.

**F7 (LOW) — the checklist gate is layout-sensitive; every quoted check count must name its layout.**
Measured: canonical → 9 PASS / 1 FAIL; scratch clone at `…/lane` → 7 PASS / 3 FAIL (`trigger.name_directory`, `trigger.citation_resolves`, `governance.citation_resolves`). **CE5 (counterexample):** "the checklist count is a property of the tree" is false — the same bytes read 7/3 in a clone and 9/1 in canonical layout. Round-47 evidence that quotes a PASS/FAIL count must state the layout, and the before/after counts must be taken in the same layout.

**F8 (LOW) — S003 adoption scope: the XML-tag clause only.**
`corpus/SOURCES.md:16` (S003) states "The description cannot contain XML tags, must be third person … body under 500 lines". Round 47 adopts the XML-tag clause. The body-length clause is **not** satisfied by this lane (525 lines). The C2 row must name the clause it does not adopt; otherwise the row reads as an S003 conformance claim it does not make.

**F9 (INFO) — no capability row (see §4).**

**F10 (INFO) — the corpus DRIFT has two causes; name them separately.**
Observed at BASE: integrity DRIFTs = `tracked_files 59≠58` **and** `unindexed 1`; independent DRIFT = `unindexed 1` only (its tracked/report/commit rows are observe-mode INFO). The index row removes `unindexed=1`; the baseline re-record removes the count drift. They are different fixes against different mechanisms; a single "index fix" sentence would misstate the change (a calibration defect by the lane's own definition).

**F11 (INFO) — the re-pin's blast radius reaches the pins guard's capability row.** `verifiers/check_substrate_pins.py:63` and `verifiers/verify_surfaces.py:130` both carry the dead opencode default; "3/3 pins at the **default** resolution" (the plan's after-target) therefore requires changing a **default path** in two instruments, not only re-pinning shas in `verifiers/baseline.json`. The SCORECARD freshness row must name the new default path (otherwise the counting command is not reproducible by a reader) and the pins-guard capability row (`SCORECARD.md:233`) must remain accurate about what it hashes.

---

## 7. Explicitly forbidden — history-rewriting risks in this edit

1. **Do not edit `LOG.md:2111`** (or any LOG line) to make the governance gate green. LOG.md is append-only; the fix is the registry. A silent edit there would also destroy the evidence the registry cites.
2. **Do not edit the round-46 Move-log rows** (`SCORECARD.md:225-229`) or the round-46 evidence text in the axes rows (`:28`, `:31`, `:33`) — append-only.
3. **Do not edit the stale round-47 planned block in place** (`SCORECARD.md:100-104`); annotate it from the round-47 entry (the file's own idiom: "Round 41 calibration annotation (append-only; round-40 seat denominator)", `SCORECARD.md:80`).
4. **Do not let the round-47 entry record a capability** (§4) — the plan's C3 was re-cut to calibration; recording the plan's capability wording would be a false record.
5. **Do not touch `corpus/lessons/round-46-verifier-spotcheck.md`**; the corpus index row is **additive** to `corpus/README.md`, and existing index rows are untouched.
6. **Corpus baseline re-record** (`verifiers/corpus-baseline.json`): update the observed counts and **append** the move to the `measured_against.note` (the lane's idiom, cf. LOG's round-46 re-record "tracked_files 55→58, report_total 38→40, commit_total 27→29") — do not delete the prior values from the note.
7. **Floors bump-in-step**: registry + both in-file tables + guard docstring together; do not delete the old floor values from the registry's `$comment`.
8. **The `Last change` column is a status field** — updating it for the three touched rows is not a rewrite; using it to restate a score's attribution would be.
9. **Do not rewrite `AXES.md`/`MISSION.md` or the fleet-root files** — out of this lane's scope (and the AXES↔MISSION naming mismatch stays routed to the protocol lane per `SCORECARD.md:8-13`).

---

## 8. What I did NOT check

- I did **not** measure any "after" value: no round-47 implementation existed at BASE. Every after-number in §2–§3 is a **target** for the L1 to fill from the landing tree, not a measurement.
- I did **not** run the comparator, `verify_harness_claims.py` (BASE 21/28 per the plan), `check_assertion_floors.py`, the corpus gates' `--self-test`s, or the wave-2 falsify batteries — none are named in my item; the floors vector I quote is the BASE registry value, not a re-run.
- I did **not** re-derive the loader-surface extraction myself (that is C1's executors' lane); I only confirmed the two gates' red state, the pin baseline vs observed omp sha, and the dead opencode default path.
- I did **not** execute `~/.local/bin/opencode` (contract forbids the npx wrapper) and did **not** launch an omp session; `omp --version` was not run — the omp facts come from the frozen snapshot values quoted in the plan and the pins-gate output (`got=fdbc8136…`).
- I did **not** verify the content correctness of `corpus/lessons/round-46-verifier-spotcheck.md`, only its index status (`unindexed=1`).
- I did **not** check the fleet-root `PROTOCOL.md`/`SCORECARD.md` conventions beyond `AXES.md` and kotoba's own file; nor did I check the aggregator's expectations for the r47 scorecard shape.
- I did **not** review the 200+ peer lanes' artifacts; my statements about wave-2 outputs are conditional ("if a named non-author lane shows X"), never assertions.
- I did **not** verify that the round-47 wave artifact paths the rows will cite will exist — that depends on the executors' chosen paths and is the L1's to confirm at landing (F1).

---

## 9. One-paragraph summary for the integrator

Land the round-47 SCORECARD edit as: three axes rows that **hold** (freshness 8, operability 8.5, calibration 8.5) with the measured before-values (surfaces exit 2 / pins exit 2 `DRIFT 3/3`, checklist 9 PASS/1 FAIL, corpus 2 and 1 DRIFTs), the new default opencode path named, `<measured-commit>` placeholders, the S003 clause-scope note, the two-cause corpus note, and the registry's fail-closed properties; three append-only Move-log rows in the same shape; **no** Capabilities row; an append-only `**Round 47 completed …**` + `**Next: round 48 …**` block (depth / freshness / calibration, one claim per axis, a depth claim so the owned-axis obligation is discharged — F6); and a round-47 running-window paragraph saying no capability row has entered since round 29. Backtick only paths that exist at the landing commit, or the governance gate will fail on the record itself (F1). Do not touch `LOG.md:2111`, the round-46 rows, the stale round-47 planned block, or the corpus lesson file.
