# B23GateRegistryCalc — the two new § Gate registry rows (round 76)

Seat: B23GateRegistryCalc (executor). Scope: compute the two new rows for `SKILL.md` § Gate registry
(C1 counter `verifiers/check_desc_craft.py`, C2 counter `verifiers/check_r75_routed_repairs.py`) in the
existing table's column shape, and validate them against `verifiers/check_gate_registry.py`.
**Report only — no lane file was written by this seat.**

Lane repo: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`. Scratch fixture (removed at yield):
`/fast/scratch/hyaku/kotoba-r76/B23GateRegistryCalc/repo` — a `git clone --shared` of the lane at
`4de12b6`, its own git dir, `git rev-parse --show-toplevel` asserted to print the fixture dir before
every git write there. The lane repo and the lane git index were not mutated (`git status --short` in
the lane shows only the pre-existing untracked wave dirs; `git log --oneline -1` still `eab6439`).

## 1. What the checker actually requires (read, not assumed)

`verifiers/check_gate_registry.py` — read at the lane tip before writing anything. Its docstring
(lines 24-56) and `judge_row` (`:180-231`) pin the contract:

- universe = every blob directly under `verifiers/` at the measured revision ending `.py`/`.sh`
  (`Tree.universe`, `:139-152`, `git ls-tree`, no recursion);
- exactly **one** row of the first table under the heading `## Gate registry` must name the verifier
  (`registry_rows` `:161-180`, `judge` `:236-248`); a row naming a `verifiers/...` path outside the
  universe is a **PHANTOM**;
- kind ∈ {gate, probe}; the entry-command cell must contain the path text;
- the verdict-map cell must declare ≥1 `<code>=<class>` pair, no code twice, and a **gate** must declare
  `0=clean` and `1=failed` (`PAIR_RE` `:74`);
- the self-test cell is `none` or names backticked `--x` flags, each of which must be an **exact active
  handler** in the file — a Python `add_argument` with that exact string, or a shell `case` arm
  (`has_flag_handler` `:76-104`); a gate may not say `none`;
- the pinned-values cell is `none`, exactly `in-file`, or backticked repo-relative paths that must
  **exist at the revision** (`git cat-file -e`); a gate may not say `none`;
- write scope non-empty and not a dash; owner cell exactly `kotoba`.

Two consequences drove the wording below, both measured, not assumed:

1. **A pinned cell that is neither exactly `in-file` nor carries a backticked path is a failure.** The
   cell is compared after `clean()` (backticks/asterisks stripped, lower-cased), and the path branch
   runs when `clean(pv) != "in-file"`. So `in-file digest table` **without** a backticked path is
   rejected — measured: `61 of 62`, exit 1. The pinned cell must be exactly `in-file`, or
   `in-file <words>; `<path>`` with the path present at the revision.
2. **The order of landing matters.** If the rows are committed before the two counter files exist, the
   two rows are PHANTOM — measured: `PHANTOM verifiers/check_desc_craft.py`,
   `PHANTOM verifiers/check_r75_routed_repairs.py`, `60 of 60 … phantom 2`, exit 1. The counters and
   the registry rows must land in the same tree state the check is measured at.

## 2. The two rows (final wording)

Placed at the end of the table, immediately after the existing `verifiers/check_sibling_reread.py` row
(`SKILL.md:512` at the base) — matching the table's existing convention of appending each round's
counters as the table grows. Exact text, one line each:

```markdown
| `verifiers/check_desc_craft.py` | gate | `python3 -B verifiers/check_desc_craft.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate — round-76 C1 counter (depth): committed bytes only; the entry `corpus/knowledge/description-craft-round76.md` is admitted when the optimizing-descriptions, evaluating-skills and best-practices page bytes are pinned under `.ufo/waves/round-76/snapshots/` with every digest appearing identically in `MANIFEST.sha256`, in `fetch-record.json`, in the counter's in-file digest table and in the round-76 lesson access record; the entry carries at least four located quotes of at most 25 words, each occurring verbatim after the optimizing-descriptions page's first heading and absent from the other two pinned pages; `SKILL.md` § Body craft carries a rule row citing the entry and S213 with at least two quote fragments found in that snapshot; the entry's audit values equal the counter's own clip-preserving recomputation of the measured revision's rendered description length and first-sentence length; S213's `used-by` lists the entry and the old-to-new change is logged in `corpus/lessons/round-76.md`; the entry opens with the provenance trio; `description craft backed N of 6` at the measured rev and `0 of 6` at the pinned base | `--self-test` | in-file digest table; `.ufo/waves/round-76/snapshots/MANIFEST.sha256` | none (reads committed bytes at `<rev>`; a `--self-test` writes isolated fixture repos under `$TMPDIR`, removed) | kotoba |
```

```markdown
| `verifiers/check_r75_routed_repairs.py` | gate | `python3 -B verifiers/check_r75_routed_repairs.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate — round-76 C2 counter (consistency): the four round-75 routed defects R1–R4 close with committed corrections — the appended `corpus/lessons/round-75.md` correction names the superseded M75-1 text, the Gate reject candidate and the folded-render measurement, and the receipt `.ufo/waves/round-76/receipts/r1-folded-render.txt` recomputes the render length from the measured revision's `SKILL.md` and prints 1022 under the clip-preserving convention; the receipt `.ufo/waves/round-76/receipts/noharm-at-tip.txt` names the tip revision on its first line and carries both corpus gates green, cited from LOG § Round 75; the note `.ufo/waves/round-76/w2-registry-note.md` reconciles seat `R75Attack28` of the round-75 w2 results with a machine-checkable excerpt, cited from LOG § Round 75; LOG § Round 75 carries an appended closing line recording the w2 settlement; `r75 routed repairs closed N of 4` at the measured rev and `0 of 4` at the pinned base | `--self-test` | in-file | none (reads committed bytes at `<rev>`; a `--self-test` writes isolated fixture repos under `$TMPDIR`, removed) | kotoba |
```

Column-by-column derivation:

| Column | `check_desc_craft.py` | `check_r75_routed_repairs.py` | Why |
|---|---|---|---|
| Name | `verifiers/check_desc_craft.py` | `verifiers/check_r75_routed_repairs.py` | the plan's touch list names both files (`plans/round-76.md` § Touch list, "New") |
| Kind | `gate` | `gate` | both are frozen claim counters with a `0`/`1` exit contract (`plans/round-76.md` C1/C2 frozen predicates) |
| Entry command | `python3 -B verifiers/check_desc_craft.py --rev <rev>` | `python3 -B verifiers/check_r75_routed_repairs.py --rev <rev>` | exactly the frozen command strings from the plan and from the seat prompt; both carry `--rev <rev>` because both predicates are revision-scoped |
| Verdict map | `0=clean, 1=failed, 2=could-not-evaluate` + the counter's scope in one cell | same shape + scope | `0=clean`/`1=failed` is mandatory for a gate; `2=could-not-evaluate` matches the every sibling row (`SKILL.md:453-512`) and the plan's "exits 0 … exits 1 … else could-not-evaluate" reading |
| Self-test | `--self-test` | `--self-test` | both counters are required by the plan to carry a `--self-test` arm with must-fail cases (C1: five must-fail arms; C2: a must-fail arm per repair) — and the cell may not say `none` for a gate |
| Pinned values | `in-file digest table; `.ufo/waves/round-76/snapshots/MANIFEST.sha256`` | `in-file` | the C1 counter pins its page digests **in-file** *and* reads the committed manifest; the C2 counter's pins (base rev, R1's `1022`) are all in-file. The C1 path must exist at the measured rev — it does (`git ls-tree` shows `.ufo/waves/round-76/snapshots/MANIFEST.sha256` committed) |
| Write scope | `none (reads committed bytes at `<rev>`; a `--self-test` writes isolated fixture repos under `$TMPDIR`, removed)` | same | the lane's convention for a committed-bytes counter (see the `check_spec_craft.py` / `check_cn_vendor_surfaces.py` rows at `SKILL.md:511` and `:509`) |
| Owner | `kotoba` | `kotoba` | required literal |

The verdict-map cells are deliberately the *scope* of each counter in the lane's existing idiom — one
sentence naming the conjuncts the counter checks — so the row is a self-description rather than a
pointer. Content is aligned to the **as-corrected** predicate in `plans/round-76-addendum-1.md`:
- C1 conjunct (a) is described with the digest appearing identically in `MANIFEST.sha256`,
  `fetch-record.json`, the counter's in-file digest table **and** the round-76 lesson access record —
  the addendum withdrew the "S213 anchor update" clause, and the row does not reintroduce it;
- the render-length convention is stated as **clip-preserving** (1022), matching the addendum's
  off-by-one closure, not the stripped variant.

## 3. Validation (measured, on a scratch copy of the repo with the patched SKILL.md)

Fixture: scratch clone of the lane at `4de12b6`; two **stub** counter files written into the scratch
`verifiers/` (each with an `add_argument("--self-test", action="store_true")` handler so the checker's
flag check has something real to find); `SKILL.md` patched with the two rows above; a placeholder
`.ufo/waves/round-76/snapshots/MANIFEST.sha256` committed so the pinned path exists at the measured rev.
The stubs are **not** the lane counters and prove nothing about the claim — they exist only so the
registry checker's rules can be exercised on a tree where the two verifiers exist.

```
$ cd /fast/scratch/hyaku/kotoba-r76/B23GateRegistryCalc/repo
$ git rev-parse --show-toplevel
/fast/scratch/hyaku/kotoba-r76/B23GateRegistryCalc/repo
$ python3 -B verifiers/check_gate_registry.py --rev 26fe07eb01a9baffa0d81be5e9458cee302dbe0c
...
verifiers/check_desc_craft.py                OK
verifiers/check_r75_routed_repairs.py        OK
...
gate registry rows conformant 62 of 62 lane verifiers; phantom 0
EXIT=0
```

**62 of 62 conformant, phantom 0, exit 0.** The universe grows from 60 to 62 because the two new
counters land; both new rows are conformant.

Lane base, unchanged (no rows added by this seat):
```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
$ python3 -B verifiers/check_gate_registry.py --rev b7f13f4b39cbd43076a85568adca763a6f674e7a
gate registry rows conformant 60 of 60 lane verifiers; phantom 0
EXIT=0
```

### 3.1 The rows are load-bearing — nine mutants, each measured from the same good commit

Each mutant was committed in the scratch clone at a fresh commit off the pinned good revision
`26fe07eb` and the checker re-run at that commit. Every one fails (exit 1) and names the defect:

| Mutant | exit | Checker output | Why it matters |
|---|---|---|---|
| M1 counter's `--self-test` renamed to `--selftest` | 1 | `no self-test flag --self-test lacks an exact handler` — 61 of 62 | the self-test cell is checked against the file's real AST, not taken on trust |
| M2 `1=failed` dropped from the C2 row | 1 | `no gate verdict map lacks 0=clean and 1=failed` — 61 of 62 | the gate verdict-map rule bites |
| M3 pinned path → `GONE.sha256` | 1 | `no pinned path … does not exist` — 61 of 62 | the pinned path is resolved at the revision |
| M4 duplicate C1 row **inside** the table | 1 | `no registry rows naming it: 2 (need 1)` — 61 of 62 | exactly-one-row rule |
| M5 kind `gate` → `probe` | 1 | `no probe verdict map declares 1=failed; probe script has an exact --self-test handler` — 61 of 62 | the probe/gate distinction is enforced against the source |
| M6 owner → `kengaku` | 1 | `no owner 'kengaku'` — 61 of 62 | owner is a literal |
| M7 write scope → `—` | 1 | `no write scope empty` — 61 of 62 | write scope must be non-empty and not a dash |
| M8 C1 row renamed to `check_desc_craft_v9.py` | 1 | `no registry rows naming it: 0 (need 1)` + `PHANTOM verifiers/check_desc_craft_v9.py` — 61 of 62, **phantom 1** | a row outside the universe is counted as phantom |
| M9 both rows removed | 1 | `no registry rows naming it: 0 (need 1)` ×2 — 60 of 62 | both rows are required for the count to reach 62 |

Two earlier mutants that *survived* taught the shape and are reported for the integrator:
- a pinned cell of `in-file digest table` **without** a backticked path → **survived as a failure of the
  row** (61 of 62, exit 1): the cell must be exactly `in-file` or carry a path;
- a duplicate row appended **after** the table's terminating blank line → **not seen at all** (the
  registry parser stops at the table's end): a duplicate only counts if it is inside the table.

## 4. Two variants the integrator may prefer, both measured

Both were committed in the scratch clone and re-run; both are conformant at 62 of 62, phantom 0, exit 0:

- **Pinned-path variant (recommended, used above).** `in-file digest table;
  `.ufo/waves/round-76/snapshots/MANIFEST.sha256`` for C1. This is the C1 counter's own manifest and
  makes the row self-locating; the path must exist at the measured revision.
- **Order-independent variant.** Replace that cell with exactly `in-file`. Measured conformant. Prefer
  this if the landing order of `snapshots/MANIFEST.sha256` relative to the `SKILL.md` row is not
  guaranteed — a pinned path that is not yet committed turns the row non-conformant (mutant M3
  demonstrates the failure mode). `check_skill_evals_v2.py` (`SKILL.md:505`) already uses the
  directory form `in-file; `.ufo/waves/round-70/snapshots/``, which was also measured conformant here.

## 5. Risks, blockers, hand-off notes

- **No blocker.** Both rows are computed, both are validated against the real checker on a scratch copy,
  and the count is conformant N of N with phantom 0.
- **Landing-order dependency (the one real risk).** The rows and the two counter files must be present
  in the same tree state the registry check is measured at. Rows-before-counters ⇒ **phantom 2, exit 1**
  (measured). Counters-before-rows ⇒ **60 of 62, exit 1** (measured, mutant M9's mirror). They must
  land together.
- **The stub files in the scratch fixture are not the lane counters.** When the real
  `check_desc_craft.py` and `check_r75_routed_repairs.py` land (seats `B06DescCounter`,
  `B07RepairCounter`), the two rows must be re-checked against the *real* sources: the self-test cell
  claims `--self-test`, and the checker requires an **exact** `add_argument("--self-test", …)` handler
  (or a shell `case` arm). If a real counter exposes its self-test under a different spelling, the
  self-test cell must be changed to match — that is the M1 failure mode, and it would make the whole
  registry check red.
- **The pinned path is the other coupling.** If the manifest is not committed at the measured revision,
  use the order-independent `in-file` variant of §4.
- **SKILL.md budget.** The base file is 590 lines against the 600-line budget (`plans/round-76.md` §
  Base battery). Two appended rows take it to **592**. No line was removed by this seat; the scribe
  seat `B13SkillPatch` owns the actual patch and the § Body craft row.
- **Not verified here (out of this seat's scope, and honestly flagged).** Whether the *real* counters
  implement what the verdict-map cells describe; whether `corpus/knowledge/description-craft-round76.md`
  and the receipts named in the C2 row exist with the described content; the C1/C2 headline numbers
  themselves (`description craft backed 6 of 6`, `r75 routed repairs closed 4 of 4`). This seat computed
  and validated the **registry rows only** and makes no claim about the claims.
- **No tooling was installed** (no `uv tool` / `npx` / binary install); nothing to record on that axis.
- **Scratch cleaned.** `/fast/scratch/hyaku/kotoba-r76/B23GateRegistryCalc/` was removed at yield. No
  scratch bytes are cited as evidence above — every quoted command and output is reproducible from the
  lane repo plus the fixture description in §3.

Verdict: PASS — the two rows are computed in the table's column shape and validated conformant
(62 of 62, phantom 0, exit 0) against `verifiers/check_gate_registry.py` on a scratch copy of the repo
with the patched `SKILL.md`; nine mutants each fail the check, so the rows are load-bearing.
