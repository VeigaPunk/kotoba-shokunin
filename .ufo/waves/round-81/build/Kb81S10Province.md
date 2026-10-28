# Kb81S10Province — PROVINCE.md `## Core` extension for C2 (round 81, w1)

Status: DRAFT + PATCH, not applied. The lane tree was not edited by this seat (write scope:
patches only). Scratch source: `/fast/scratch/hyaku/kotoba-r81/Kb81S10Province/clone`,
base `b284223105f4d106f7e8f56ed4fd296c643cda0e`, seat commit
`82346dc2d6bf25205ee4e49088c3b299097cc2a7` (scratch-only, deleted on yield).

- Patch (authoritative change): `Kb81S10Province.patch` — 3587 B,
  sha256 `304fd286a864739908277ffa165ecdc341d60c5ed2c5d14e65b8c6d29a0d44d3`;
  `git apply --check` OK on a fresh base clone, and applying it reproduces
  `PROVINCE.md` sha256 `933e1233bf184fe551dfe9a6b0b4b5e8811a62b6b92c90e8c93d510ad7e10abf`
  (base file sha256 `83f1ea44bddac1cc05aedb72f5d2c875f71429b669ee3e4010a00db058d9ff43`).
- Receipts (every command + stdout + exit code below): `Kb81S10Province-receipts.txt`,
  sha256 `fa5f754e87325e7f6d60e3008119952eadc76f910cd639232129e2dc74f3db95`.

## 1. The extension

Target: `PROVINCE.md:34`, the round-80 `## Core` bullet
(`- Allowed-tools surfaces by client (round 80, depth): …`). It is one physical line, 667 B at base.
The edit is a single insertion **inside the bullet's existing parenthetical**, immediately after
`the six pages re-opened live 2026-10-27` and before that parenthetical's closing `)`:

```
; round 81 adds a seventh surface — the Claude Agent SDK — which documents a second grant channel, query-config `allowedTools`/`allowed_tools` beside frontmatter, with a managed-settings override, sourced to S249 in `corpus/knowledge/allowed-tools-sdk-round81.md` and counted by `verifiers/check_sdk_allowed_tools.py --rev <rev>`
```

Inserted span: 329 B. New line 34 is 996 B. Nothing else in the file changes (see § 2).

Resulting bullet, verbatim (only the parenthetical grew):

```
- Allowed-tools surfaces by client (round 80, depth): where the Open specification, Claude Code, Factory, Microsoft Agent Framework, pi and Mistral Vibe document the `allowed-tools` frontmatter field — the value form each page prints and the grant each states (`pre-approves`, `metadata-only`, `experimental`, `unstated`), each read from a snapshot-pinned located quote, form-level documentation only; the grant-semantics matrix is exploratory, reviewed by the round-80 non-author closure spot-check (S226–S231; the six pages re-opened live 2026-10-27; round 81 adds a seventh surface — the Claude Agent SDK — which documents a second grant channel, query-config `allowedTools`/`allowed_tools` beside frontmatter, with a managed-settings override, sourced to S249 in `corpus/knowledge/allowed-tools-sdk-round81.md` and counted by `verifiers/check_sdk_allowed_tools.py --rev <rev>`) — `corpus/knowledge/allowed-tools-surfaces-round80.md`, counted by `verifiers/check_allowed_tools.py --rev <rev>`.
```

Why appended rather than a 22nd bullet: the r80 counter's tree conjunct (h) reads *the bullet naming
the r80 entry* and prints `province surfaces named P of 6`; the r81 counter's (g) is expected to read
*the bullet naming the C2 entry* (that is the shape the r80 counter froze, `verifiers/check_allowed_tools.py:62`
and `:1308-1340`). Both stay satisfied either way, but the seat directive is to append, and C2 deepens
the same held area rather than opening a new one. The alternative (a separate bullet) is a one-line
move if the r81 counter demands it — see § 5.

## 2. Verbatim-preservation proof

From the receipt (computed on committed bytes at base and at the seat commit):

- `new_line.replace(inserted_span, '', 1) == old_line` → **True** (the edit is a pure insertion)
- `new_line.count(inserted_span) == 1` → **True**
- whole file: `old_lines[:33] + old_lines[34:] == new_lines[:33] + new_lines[34:]` → **True** (only line 34 differs)
- line count 76 → 76; § Core bullet count 21 → 21; no trailing whitespace added
- § section sha256, base → tip:
  - `Core`      `3c9721c0e0864786…` → `5f6bf80a31d0f57f…` **CHANGED** (the intended edit)
  - `Frontier`  `fa763651cc9166bc…` → `fa763651cc9166bc…` **IDENTICAL**
  - `Adjacent`  `c41f7b54a97ea298…` → `c41f7b54a97ea298…` **IDENTICAL** (7561 B both sides; this sha is
    exactly the `ADJACENT_ERRATA` ledger value in `verifiers/check_province_core.py:24`, i.e. the round-74
    re-pin the base counter already accepts)
- token counts in `PROVINCE.md` at tip: `corpus/knowledge/allowed-tools-sdk-round81.md` 1,
  `verifiers/check_sdk_allowed_tools.py` 1, `corpus/knowledge/allowed-tools-surfaces-round80.md` 1,
  `verifiers/check_allowed_tools.py` 1.

## 3. Derived tree conjunct and its control worlds

E09's C2 counter was **not published** when this seat ran (`.ufo/waves/round-81/build/` was empty at
23:18, and only `receipts/{census-before.txt,tipbattery-base-dot.txt}` existed under the wave root), so
the (g)-shaped arm was first derived from the r80 counter's frozen code path
(`province_bullets()` / `province_state()`, `verifiers/check_allowed_tools.py:1308-1340`) and measured
here. The counter's own author then confirmed the shipped shape by IRC (2026-10-27), quoted verbatim:

> Your draft passes (g): my counter requires exactly one `## Core` bullet containing the entry path
> `corpus/knowledge/allowed-tools-sdk-round81.md`, and that SAME bullet to name the SDK channel — I test
> `SDK` plus (`allowedTools` or `allowed_tools`) on the bullet's text. Yours has both. Keep the entry
> path out of every other § Core bullet (two bullets naming it is a finding, as in r80). No exact-phrase
> requirement beyond that.

Measured against exactly that test on committed bytes (`Kb81S10Province-receipts.txt`, last section):
base — 0 bullets name the entry; seat tip — **1** bullet names it, and that same bullet carries `SDK`,
`allowedTools` **and** `allowed_tools`, the counter path and `round 81`.

Replicated arm (bullets of `## Core` naming a token), on committed bytes:

| world | bullets naming `corpus/knowledge/allowed-tools-sdk-round81.md` |
|---|---|
| base `b2842231` | 0 |
| seat tip `82346dc2` | **1** |
| tip + a second bullet naming the entry | 2 (arm discriminates; not constant-1) |
| duplicate removed again | 1 |
| entry named only in `## Frontier` | 1 (§ Core is the only section read) |

Also 1 each for `verifiers/check_sdk_allowed_tools.py` and `round 81`, and the naming bullet is the
round-80 bullet, on one physical line.

## 4. Gates run (exact commands, exit codes)

Lane tree untouched; all counter runs used `--repo <scratch clone>` (or the clone as cwd) and read the
measured rev's committed bytes. Full stdout is in `Kb81S10Province-receipts.txt`.

| command | base `b2842231` | tip `82346dc2` | reading |
|---|---|---|---|
| `python3 -B verifiers/check_province_core.py --repo <clone> --rev <rev>` | exit 0, `province core rows 2 of 2` | exit 0, `province core rows 2 of 2` | § Adjacent pin + both held areas unaffected |
| `python3 -B verifiers/check_province_core.py --self-test` | exit 0, `0 failure(s) over 12 assertions` | — | counter trustworthiness |
| `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round74.md --fleet /home/vgpnk/Projects/shokunin --province PROVINCE.md --skill SKILL.md` (cwd = clone) | exit 0, `rows 20 verified 20`, `province rows 20 matched 20`, `skill description names 10 of 10 non-none lanes` | exit 0, same lines | **census stays green with the edit** |
| `python3 -B verifiers/check_sibling_census.py --self-test` | exit 0, `0 failure(s) over 68 assertions` | — | — |
| `python3 -B verifiers/check_allowed_tools.py --repo <clone> --rev <rev>` | exit 0, `6 of 6`, `province surfaces named 6 of 6`, `skill rule line ok`, `registry home ok` | exit 0, identical | r80 (h) still sees one bullet, six surfaces |
| `python3 -B verifiers/check_cn_vendor_surfaces.py --repo <clone> --rev <rev>` | exit 0, `4 of 4`, `province surfaces named 4 of 4` | exit 0, identical | — |
| `python3 -B verifiers/check_spec_craft.py --repo <clone> --rev <rev>` | exit 1, `province core names the entry: yes`, three `corpus/SOURCES.md is not census-conformant … (conjunct (b))` | exit 1, identical | base-red on SOURCES, not on PROVINCE; unchanged by the edit |
| `python3 -B verifiers/check_correction_sweep.py --root <clone>` | — | exit 0, `correction sweep: 0 stale block(s)` | the bullet carries neither stale pattern (`overlap levers backed 7 of 7 clients`, `specification and five pinned clients`) |
| `python3 -B verifiers/check_sibling_reread.py --repo <clone> --rev <rev>` | exit 0, `20 of 20` | exit 0, `20 of 20` | round-74 re-pin unaffected |

The census file for the `--province` cross-check is `corpus/knowledge/sibling-overlap-census-round74.md`:
run against `…-round49.md` the same command is **exit 1 at base already** (8 commit/classification
mismatches, `province rows 20 matched 4`), because round 74 re-pinned § Adjacent; that is a pre-existing
base state, not an effect of this edit, and the round-74 census is the one the § Adjacent block names.

Other counters that read `PROVINCE.md`: `check_sibling_reread.py`, `check_spec_craft.py`,
`check_cn_vendor_surfaces.py`, `check_allowed_tools.py`, `check_sibling_census.py`,
`check_correction_sweep.py`, `check_province_core.py` (`grep -ln PROVINCE verifiers/*.py`). All seven are
in the table above. None of the six tip-battery gates or the five battery guards reads `PROVINCE.md`
(`grep -n PROVINCE` on `verify_skill_checklist.py`, `check_gate_registry.py`, `check_correction_sweep.py`,
`verify_corpus_integrity.py`, `verify_corpus_independent.py`, `check_assertion_floors.py`: only
`check_correction_sweep.py`'s two stale-pattern rows, exercised above).

## 5. Risks and limits

1. **(g) is confirmed by the counter's author, not yet measured on frozen counter bytes.** The shipped
   test is the one quoted in § 3 and the drafted text passes it; if the frozen counter later narrows
   (e.g. requires the span as its own bullet), the fix is mechanical: move the 329-B span out of the
   parenthetical into a separate § Core bullet and repeat § 4. No wording in the r80 bullet may be
   reworded either way — both counters read the bullet naming each entry, and `check_allowed_tools.py`
   matches by substring only.
2. **This edit alone does not make C2 exit 0.** The C2 tree conjuncts also need
   `corpus/knowledge/allowed-tools-sdk-round81.md`, the 11-cell S249 row, the S249 snapshot pin, the
   S248 `used-by` update, the SKILL.md SDK-channel line and the registry row — all other seats' files.
   Scored here: the PROVINCE half only.
3. **`check_spec_craft.py` exit 1 is base state** (`corpus/SOURCES.md` not census-conformant at
   `b2842231`), identical before and after; it is not caused or fixed by this seat.
4. No claim after-value was measured. No file outside
   `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/` was written by this seat, and the
   lane's `PROVINCE.md` is untouched.

## 6. For L1 integration

```
git apply .ufo/waves/round-81/build/Kb81S10Province.patch        # from the lane root
python3 -B verifiers/check_province_core.py --rev <tip>
python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round74.md \
  --fleet /home/vgpnk/Projects/shokunin --province PROVINCE.md --skill SKILL.md
python3 -B verifiers/check_correction_sweep.py --root .
python3 -B verifiers/check_allowed_tools.py --rev <tip>          # must stay exit 0, 6 of 6
```
