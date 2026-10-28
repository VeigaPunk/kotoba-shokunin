# Kb80E01Registry — round 80 w1, C1 repair 1: the `SKILL.md` § Gate registry rows

## What I changed

One file, three inserted lines, zero deletions: `SKILL.md`, appended at the end of the
`## Gate registry` table — after the `verifiers/check_sibling_reread.py` row, which is the
table's last row at the round-80 base `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`
(`SKILL.md:512`; the table ends at 512 and `## Sources` starts at 514).

The anchor was re-derived from the CURRENT bytes, not copied from the r79 patch: `SKILL.md`'s
blob is `26ce572ed8dad7625083b09236e3a7943bdbbe47` at the base **and** at the lane HEAD
`a481913bafeb1ec5c231fd581f13da6ae5a306dc`, so the table's row set and the anchor line are
identical to the r79 seat's; the r79 patch `Kb79E01Registry.patch` still applies to the base
cleanly (`git apply --check` → rc 0).

The three rows, verbatim as landed:

```
| `verifiers/check_desc_craft.py` | gate | `python3 -B verifiers/check_desc_craft.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate — claim withdrawn r79 before data (declared r76, never landed; still withdrawn at r80); not a claim gate until redesigned and re-controlled | `--self-test` | in-file | none when measuring (reads committed bytes); a `--self-test` writes isolated fixture repos under `$TMPDIR` (removed) | kotoba |
| `verifiers/check_r75_routed_repairs.py` | gate | `python3 -B verifiers/check_r75_routed_repairs.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate — claim withdrawn r79 before data (declared r76, never landed; still withdrawn at r80); not a claim gate until redesigned and re-controlled | `--self-test` | in-file | temp shared clones under `$TMPDIR` (removed): a measurement re-runs the corpus gates in one and a `--self-test` builds fixture repos there | kotoba |
| `verifiers/check_allowed_tools.py` | gate | `python3 -B verifiers/check_allowed_tools.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate — round-80 C2 counter (depth): form-level documentation of the allowed-tools frontmatter field per client; the grant-semantics rider is exploratory; prints `allowed-tools surfaces documented N of 6` and `generator world: M of 6` | `--self-test` | in-file | temp git fixture trees under `$TMPDIR` (removed); the measured tree is read-only | kotoba |
```

## Why each cell is what it is (no cell guessed)

The row requirements are `check_gate_registry.py`'s own `judge_row` (`verifiers/check_gate_registry.py:180-231`),
read from the source, and Q35/Q46 (`corpus/QUALITY.md:46,57`).

**Rows 1 and 2 — the two withdrawn claims.** Q46 requires an in-cell `claim withdrawn`
annotation saying the row is not a claim gate until redesigned and re-controlled. The r79
draft's wording was `claim withdrawn r79 before data (declared r76, never landed); not a
claim gate until redesigned and re-controlled`; I kept it and added `; still withdrawn at r80`,
because at r80 the two claims are still withdrawn (no r80 plan section admits either; the
round-80 plan's § C1 repair 1 lists them only as *"Q46 withdrawal cells"*). The house
convention for a withdrawn row is the same string plus a round reason — `SKILL.md` already
carries `claim withdrawn r56 before data`, `claim withdrawn r57 before data`, and
`claim withdrawn r58 (plan erratum 1)` with the same trailing clause; no verifier greps for
the string, so it is a reviewer-read obligation (Q46), and this row honours it.

- **kind `gate`** — `judge_row` rejects a `probe` whose source has an exact `--self-test`
  handler, and both scripts have one: `check_desc_craft.py:1002` and
  `check_r75_routed_repairs.py:1007`, each `ap.add_argument("--self-test", action="store_true")`
  at the base blob. A `probe` would be rejected, so `gate` is the only conformant kind.
- **entry command** — the path text `verifiers/check_desc_craft.py` /
  `verifiers/check_r75_routed_repairs.py` appears in the cell (`judge_row`: `if path not in r[2]`),
  and both scripts take `--rev` (`check_desc_craft.py:996`, `check_r75_routed_repairs.py:1003`).
- **verdict map** — both `main()`s return 2 on environment errors (`check_desc_craft.py:1025,1031,1037,1042`;
  `check_r75_routed_repairs.py:1035`), 1 on an unmet target (`check_desc_craft.py:1049`
  `return 0 if held == TOTAL else 1`; `check_r75_routed_repairs.py:1042`), 0 otherwise, so
  `0=clean, 1=failed, 2=could-not-evaluate` is the declared map and no code repeats.
- **self-test** — `--self-test`, an exact active handler in each file (above).
- **pinned values `in-file`** — the frozen pins live in each script's own bytes:
  `check_desc_craft.py:149` `SELF_SHA` plus its page-digest table; `check_r75_routed_repairs.py:74,89`
  `BASE` / `RENDER_CLIP` plus its token tables. I deliberately did **not** backtick a path
  here: `check_r75_routed_repairs.py:83` names `.ufo/waves/round-76/receipts/noharm-at-tip.txt`,
  which `git cat-file -e` shows is **not committed at any revision in this lane** (a sweep of
  `git rev-list --all` for that path returned nothing), so `judge_row`'s `exists(p)` would
  fail the row. `in-file` is the conformant and truthful cell.
- **write scope** — measured, not assumed. I instrumented `tempfile.mkdtemp` around each
  counter's `main()` on the base tree: `check_desc_craft.py` makes **0** `mkdtemp` calls during
  a measurement (its `check()` reads committed bytes only; its temp repos are built by
  `_world()` at `:1255-1281`, reached only from the `--self-test` path, and removed at `:1437`),
  so the cell says `none when measuring (reads committed bytes); a --self-test writes isolated
  fixture repos under $TMPDIR (removed)`. `check_r75_routed_repairs.py` makes **1** call
  during a measurement — `gates_at()` at `:131-165` clones `--shared` and runs both corpus
  gates in a temp sandbox (mkdtemp at `:135`, `shutil.rmtree` at `:165`); I reproduced this
  on a fixture rev that carries the r76 no-harm receipt (the receipt's presence is what
  `r2_receipt` at `:427` gates the re-run on): `created: …/k76-c2-gates-1q5z4wjm`,
  `exists after: False`. The cell names that.

**Row 3 — the new C2 counter.** Its pinned values are `in-file` and the row text quotes the
counter's own printed strings. Verified against the **published E07 bytes** at
`.ufo/waves/round-80/build/check_allowed_tools.py` (sha256 `b4ca1561a9cc6989ad9497ae0eab6f7e2b2e2077ac9ac6658e4e6eb7b2d55367`):

- `--self-test` is an exact handler there (`check_allowed_tools.py:2242`
  `ap.add_argument("--self-test", action="store_true")`), so the `--self-test` cell verifies.
- The counter's own `registry_home_ok()` (`:1133-1141`) requires a line starting
  `| \`verifiers/check_allowed_tools.py\`` with **8 non-empty cells** and `cells[1] == "gate"`.
  I ran that function against my own landed `SKILL.md`: `registry_home_ok(tip SKILL.md) → True`,
  with `cells: 8` and `kind cell = 'gate'`. Against the base `SKILL.md` it returns `False`
  (no row), so the row is what makes the counter's conjunct (g) second half hold.
- `skill_rule_ok()` still returns `False` on my `SKILL.md` (`surfaces_named` on my row = 0),
  so **the SKILL rule line stays the S09 seat's job** — my row neither satisfies nor
  pre-empts it.
- The pinned values are `in-file` (not a backticked path): the counter's `SELF_SHA` is in its
  own bytes (`:273`), and the reviewer `Kb80V01C1` flagged the same point about
  `.ufo/waves/round-79/snapshots/MANIFEST.sha256` — that file is **not** tracked at the base
  (`git ls-tree` of the base snapshot dir lists 18 files, no `MANIFEST.sha256`), so naming it
  would fail `judge_row`'s `exists(p)` and re-red the gate. `in-file` is the safe cell.
- The verdict-map cell names the two printed lines the counter's own docstring freezes
  (`check_allowed_tools.py:8-13`: `allowed-tools surfaces documented N of 6` and
  `generator world: M of 6`). Note for the L1: the published counter's **`print` statements
  still say the r79 wording** (`allowed-tools surfaces backed {n} of {TOTAL}` at `:2281` and
  `script-only world: {m} of {TOTAL}` at `:2282`) while its docstring says the r80 wording.
  That is E07's counter to reconcile, not mine — but the row text I wrote follows the **docstring
  and the plan** (`plans/round-80.md` § C2 freezes `allowed-tools surfaces documented N of 6` and
  `generator world: M of 6`), so if E07 changes the prints, this row's wording must be re-read.

## Evidence (commands and their own exit statuses)

All measurements ran in scratch clones under `/fast/scratch/hyaku/kotoba-r80/Kb80E01Registry/`;
the lane was never written to. Receipts are copied into
`.ufo/waves/round-80/build/Kb80E01Registry-*`.

1. **Base figure.** `python3 -B verifiers/check_gate_registry.py --rev 398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`
   → `gate registry rows conformant 60 of 62 lane verifiers; phantom 0`, **rc=1**
   (`Kb80E01Registry-registry-base.txt`). The two non-conformant rows are
   `verifiers/check_desc_craft.py` and `verifiers/check_r75_routed_repairs.py`
   (`no registry rows naming it: 0 (need 1)`), exactly the r79 base finding.
2. **Rows alone, counter file absent.** Scratch commit `e1bed9666e93ca3d7e3ee218be0807383f6861ae`
   (base + my three rows, no `verifiers/check_allowed_tools.py`): →
   `PHANTOM verifiers/check_allowed_tools.py` / `gate registry rows conformant 62 of 62 lane verifiers; phantom 1`,
   **rc=1** (`Kb80E01Registry-registry-A-skillmd-only.txt`).
   **This is the load-bearing finding of my seat: the third row and the counter file must
   land in the same tree, or the row is a PHANTOM row and the registry gate stays red.**
   `judge()` computes the universe from `git ls-tree` of `verifiers/` at the measured rev
   (`check_gate_registry.py:136-150`), so a row naming a file absent from that tree is a
   phantom, and `main()` returns 1 whenever `phantom` is non-empty.
3. **Rows + the counter file.** Scratch commit `547b9e4828e95e53ad3482b4fc7514420de5d4d0`
   (rows + E07's published `check_allowed_tools.py`, sha256 `b4ca1561…`) →
   `gate registry rows conformant 63 of 63 lane verifiers; phantom 0`, **rc=0**
   (`Kb80E01Registry-registry-B-rows-plus-counter.txt`). The universe grows 62 → 63 because the
   counter file is now a `verifiers/` blob, and all 63 have exactly one conformant row.
   63 of 63 with phantom 0 is the plan's C1 registry target.
4. **Line budget.** `wc -l SKILL.md`: base **590** → tip **593** (`+3`), against the box at
   `SKILL.md:285` `File ≤ 600 lines` (`Kb80E01Registry-linebudget.txt`).
5. **Checklist, base vs tip, identically shaped clones** (directory named `kotoba-shokunin` with
   `../.ufo` symlinked to the real fleet `.ufo`, so the clone-shape citation noise is identical
   on both sides): base `10 pass / 1 fail / exit 1`, tip `10 pass / 1 fail / exit 1`, and a
   **per-check status diff over all 11 checks shows no difference**; the single FAIL in both is
   the pre-existing `governance.citation_resolves` on `LOG.md`'s `../<sibling lane>/…` tokens
   (clone-shape artifact, the same one the r79 seat measured). `trigger.line_budget` is
   `PASS — 590 lines within budget 600` at base and `PASS — 593 lines within budget 600` at the
   tip (`Kb80E01Registry-checklist-base.json`, `…-checklist-tip.json`).
6. **Checklist with the rows but no counter file** (`Kb80E01Registry-checklist-tip-nocounter.json`):
   `9 pass / 2 fail`, with a **new** FAIL `trigger.citation_resolves | line 515:
   'verifiers/check_allowed_tools.py' does not resolve`. The checklist's `trigger.citation_resolves`
   reads backticked repo-rooted tokens out of `SKILL.md` itself, so my row's name cell is a
   second, independent reason the row and the counter file must land together.
7. **Cross-check against the counter's own conjunct.** `registry_home_ok(tip SKILL.md) → True`
   (8 cells, `cells[1] == "gate"`); `skill_rule_ok(tip SKILL.md) → False` (the rule line stays
   S09's); `province_state(PROVINCE.md) → (0, 0)` (the PROVINCE bullet stays S10's).
8. **Patch portability.** `git apply --check -v` of `Kb80E01Registry.patch` against a fresh clone
   at `398cbe1` → `Checking patch SKILL.md...`, **rc=0**; applied → `593 SKILL.md`,
   `git diff --stat` → `SKILL.md | 3 +++`, `1 file changed, 3 insertions(+)`.
9. **Patch bytes.** `Kb80E01Registry.patch`, 4294 bytes, sha256
   `dde6d91e888d4d6f41073bf985615927d16fdf67f547303127233cccc90a0b94`; `a/`–`b/` prefixes present
   (`diff --git a/SKILL.md b/SKILL.md`), hunk header `index 26ce572..2d4bff3 100644`, no rename,
   no binary. **Self-defect found and fixed:** my first cut was generated under the host's global
   `diff.mnemonicprefix=true` (`/home/vgpnk/.config/git/config`) and came out
   `diff --git c/SKILL.md w/SKILL.md`; I re-cut it with `git -c diff.mnemonicprefix=false diff`,
   verified the two cuts are **content-identical** after prefix normalisation
   (`CONTENT-IDENTICAL-to-published`), and re-ran every measurement above on the re-cut patch
   (A `e1bed966…` → `62 of 62; phantom 1`, exit 1; B `547b9e48…` → `63 of 63; phantom 0`, exit 0;
   base → `60 of 62`, exit 1). The superseded `c/`–`w/` cut was sha256 `263054b5…` and is not
   published.

10. **Independent corroboration (another seat, different scratch tree).** `Kb80E10Battery`
    substituted my canonical rows into its own fleet-shaped stack world and measured
    `gate registry rows conformant 63 of 63 lane verifiers; phantom 0` (exit 0),
    `verify_skill_checklist.py --json` **exit 0 with no failing check**, and `SKILL.md` at
    **593 lines**. It separately reproduced my A/B coupling: rows without the counter file read
    `PHANTOM … 62 of 62; phantom 1` and the checklist's `trigger.citation_resolves` FAILs on the
    same absent file. That is an outside reproduction of this seat's two load-bearing findings,
    in a tree built by a different seat from the published patch.

## What this does and does not do for C1

- It clears the gate-registry arm of the C1 battery: 60 of 62 → **63 of 63, phantom 0, exit 0**
  once `verifiers/check_allowed_tools.py` is present at the measured rev (the base universe is
  62; the C2 counter adds the 63rd).
- It does **not** claim C1. The battery's other red gates (`check_assertion_floors`,
  `verify_skill_checklist`'s governance arm, `verify_corpus_integrity`, `verify_corpus_independent`)
  are other repair seats' items, and the frozen counter `check_tip_battery.py` was neither
  edited nor re-run here.
- Nothing was scored on a frozen C2 counter; no control world was run or re-interpreted by
  this seat.

## Risks and integration notes (for the L1)

- **Landing-order coupling (high).** The third row is a PHANTOM row without the counter file
  (receipt 2, rc=1) and adds a `trigger.citation_resolves` FAIL without it (receipt 6). My
  patch must be applied in the same integration commit as E07's `verifiers/check_allowed_tools.py`.
  I did not ship the counter file in my patch: it is E07's deliverable, and the E10 battery
  stack already carries it, so bundling it here would double-apply.
- **Line budget is nearly spent.** `SKILL.md` goes 590 → 593 with my three rows, against the
  600-line box. The S09 SKILL rule line (≥1 line) and any other r80 SKILL.md edits land on top;
  at 593 there are 7 lines of headroom, and S09's rule line is ≤4 lines per its seat prompt.
  The box itself is at `SKILL.md:285` and I did not touch it.
- **Row wording vs the counter's prints (medium, E07's to reconcile).** The published counter's
  docstring freezes `allowed-tools surfaces documented N of 6` / `generator world: M of 6` while
  its `print` statements still emit the r79 wording (`:2281-2282`). My verdict-map cell follows
  the docstring and the plan; if E07 aligns the prints to the docstring the cell is exact, and
  if E07 changes the strings the cell must be re-read. A reviewer should re-read that cell
  against E07's final bytes before the tip is frozen.
- **Withdrawal wording (low).** `still withdrawn at r80` is my reading of the round-80 plan
  (§ C1 lists the two counters only as Q46 withdrawal cells, and no r80 plan section admits
  either claim). If the L1 intends a different round attribution, it is a text-only change in
  one cell of each row; the counter does not read the text.
- **Integration collision (medium).** My patch appends three rows at the same anchor the r79
  patch used. If the L1 applies the r79 patch first and mine second, both apply cleanly to the
  base (I verified `git apply --check` of mine against the base), but the r79 patch's two rows
  and my three overlap — mine already contains both withdrawn rows. **Apply mine, not the r79
  patch**: mine supersedes it. The L1 should stack SKILL.md edits from one source.
- **No other lane file was touched.** `git diff --stat` of my patch is `SKILL.md | 3 +++` only.

## Blockers

None. Scratch (`/fast/scratch/hyaku/kotoba-r80/Kb80E01Registry`) is removed before yield; no
tool was installed, no pacman run, no network fetch, no lane or fleet mutation, no lane
build/lint/test.

VERDICT: gate registry repaired in draft — with the counter file present, `conformant 63 of 63; phantom 0`, exit 0 at scratch `547b9e4` (60 of 62, exit 1 at the base); SKILL.md 590 → 593 (budget 600, `trigger.line_budget` PASS at both ends, no per-check checklist diff); the third row is PHANTOM without `verifiers/check_allowed_tools.py`, so the row and the counter file must land together.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E01Registry.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E01Registry-registry-base.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E01Registry-registry-A-skillmd-only.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E01Registry-registry-B-rows-plus-counter.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E01Registry-linebudget.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E01Registry-checklist-base.json, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E01Registry-checklist-tip.json, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E01Registry-checklist-tip-nocounter.json, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/w1/Kb80E01Registry.md
