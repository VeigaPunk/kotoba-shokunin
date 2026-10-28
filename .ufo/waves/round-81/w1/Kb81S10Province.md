# Kb81S10Province — PROVINCE.md `## Core` draft for round 81 C2 (w1, v2)

Seat item: draft the PROVINCE.md edit that (1) extends the round-80 `## Core` bullet
(`PROVINCE.md:34`) with the Agent SDK `allowedTools` channel and the new C2 entry, and (2) verifies
`check_sibling_census.py --province PROVINCE.md` stays green and that `check_province_core.py`
(§ Adjacent pinned byte-identical) is unaffected.

Deliverables are a **draft + patch**; the lane tree was not edited (write scope: patches only).
Scratch clone `/fast/scratch/hyaku/kotoba-r81/Kb81S10Province/clone` at base
`b284223105f4d106f7e8f56ed4fd296c643cda0e`, seat commit `82346dc2d6bf25205ee4e49088c3b299097cc2a7`,
removed before yield.

## 1. The edit (one insertion, nothing reworded)

Inserted inside the round-80 bullet's existing parenthetical, after `the six pages re-opened live
2026-10-27` and before that parenthetical's closing `)` (329 B):

```
; round 81 adds a seventh surface — the Claude Agent SDK — which documents a second grant channel, query-config `allowedTools`/`allowed_tools` beside frontmatter, with a managed-settings override, sourced to S249 in `corpus/knowledge/allowed-tools-sdk-round81.md` and counted by `verifiers/check_sdk_allowed_tools.py --rev <rev>`
```

- `PROVINCE.md` sha256: base `83f1ea44bddac1cc05aedb72f5d2c875f71429b669ee3e4010a00db058d9ff43` →
  tip `933e1233bf184fe551dfe9a6b0b4b5e8811a62b6b92c90e8c93d510ad7e10abf`; line 34 667 B → 996 B.
- Pure insertion proven on committed bytes: `new_line.replace(inserted_span,'',1) == old_line` **True**;
  `insert occurs exactly once` **True**; `old_lines[:33]+old_lines[34:] == new_lines[:33]+new_lines[34:]`
  **True**; line count 76 → 76; § Core bullets 21 → 21; no trailing whitespace.
- § section sha256: `Frontier` `fa763651cc9166bc…` **IDENTICAL**, `Adjacent` `c41f7b54a97ea298…`
  **IDENTICAL** (7561 B both sides; that digest is exactly the `ADJACENT_ERRATA` ledger value in
  `verifiers/check_province_core.py:24`), `Core` changed as intended.
- Token counts at tip: entry path 1, `verifiers/check_sdk_allowed_tools.py` 1, r80 entry path 1,
  `verifiers/check_allowed_tools.py` 1.

## 2. The r81 counter's (g) conjunct — what was required, and how it was settled

E09's counter was **not published** while this seat ran (`.ufo/waves/round-81/build/` empty; the wave
root held only `receipts/{census-before.txt,tipbattery-base-dot.txt}`), so the arm was derived from the
r80 counter's frozen code path (`verifiers/check_allowed_tools.py:62`, `:1308-1340`) and the exact draft
text was sent to `Kb81E09C2Counter`. Its author confirmed the shipped shape by IRC (2026-10-27):

> Your draft passes (g): my counter requires exactly one `## Core` bullet containing the entry path
> `corpus/knowledge/allowed-tools-sdk-round81.md`, and that SAME bullet to name the SDK channel — I test
> `SDK` plus (`allowedTools` or `allowed_tools`) on the bullet's text. Yours has both. Keep the entry
> path out of every other § Core bullet (two bullets naming it is a finding, as in r80). No exact-phrase
> requirement beyond that.

Measured against that test: base → 0 bullets name the entry; tip → **1**, and the same bullet carries
`SDK`, `allowedTools`, `allowed_tools`, the counter path and `round 81`. Discriminating control worlds
(receipts): tip + a second bullet naming the entry reads 2; the entry named only in `## Frontier` reads 1
(§ Core only). No after-value of the C2 claim was scored.

## 3. Verification — exact commands and exit codes

All on committed bytes with `--repo <scratch clone>` (or the clone as cwd); full stdout in
`build/Kb81S10Province-receipts.txt`. Lane tree untouched.

| command | base `b2842231` | tip `82346dc2` |
|---|---|---|
| `check_province_core.py --repo <clone> --rev <rev>` | exit 0, `province core rows 2 of 2` | exit 0, `province core rows 2 of 2` |
| `check_province_core.py --self-test` | exit 0, `0 failure(s) over 12 assertions` | — |
| `check_sibling_census.py corpus/knowledge/sibling-overlap-census-round74.md --fleet /home/vgpnk/Projects/shokunin --province PROVINCE.md --skill SKILL.md` | exit 0, `rows 20 verified 20`, `province rows 20 matched 20`, `skill description names 10 of 10 non-none lanes` | exit 0, identical |
| `check_sibling_census.py --self-test` | exit 0, `0 failure(s) over 68 assertions` | — |
| `check_allowed_tools.py --repo <clone> --rev <rev>` | exit 0, `6 of 6`, `province surfaces named 6 of 6`, `skill rule line ok`, `registry home ok` | exit 0, identical |
| `check_cn_vendor_surfaces.py --repo <clone> --rev <rev>` | exit 0, `4 of 4`, `province surfaces named 4 of 4` | exit 0, identical |
| `check_spec_craft.py --repo <clone> --rev <rev>` | exit 1, `province core names the entry: yes`, 3× SOURCES `(conjunct (b))` | exit 1, identical |
| `check_correction_sweep.py --root <clone>` | — | exit 0, `correction sweep: 0 stale block(s)` |
| `check_sibling_reread.py --repo <clone> --rev <rev>` | exit 0, `20 of 20` | exit 0, `20 of 20` |

- **`check_province_core.py` does pin `## Adjacent` byte-identical** to BASE `a5f7459f…`, but admits a
  rewrite whose whole-section sha256 is in `ADJACENT_ERRATA` (the round-74 re-pin). Our edit leaves
  `## Adjacent` untouched and its digest equals the ledgered round-74 value, so the counter reads
  `2 of 2` exit 0 both sides. It also re-checks the round-67/68 § Core bullets; the extension names
  neither of those entries/counters, so both areas stay held.
- **`check_sibling_census.py --province` reads only `## Adjacent`** (`_check_province`, `:789-867`), so a
  § Core edit cannot reach it — confirmed empirically, not just by reading: green on both sides.
- Census invocation note: `--province` against `…-round49.md` is **already exit 1 at base**
  (`province rows 20 matched 4`, 8 commit/classification mismatches) because round 74 re-pinned the
  block; `…-round74.md` is the census § Adjacent names and is exit 0 on both sides. That is pre-existing
  base state, not an effect of the edit.
- `check_spec_craft.py` exit 1 is **base state** (`corpus/SOURCES.md` not census-conformant at
  `b2842231`), byte-identical before and after, and its PROVINCE arm (`province core names the entry:
  yes`) stays green.
- Every other `PROVINCE.md` reader is covered above: `grep -ln PROVINCE verifiers/*.py` →
  `check_allowed_tools.py`, `check_cn_vendor_surfaces.py`, `check_correction_sweep.py`,
  `check_province_core.py`, `check_sibling_census.py`, `check_sibling_reread.py`,
  `check_spec_craft.py`. No tip-battery gate or guard reads `PROVINCE.md`.

## 4. Scope, limits, provenance

- **Not applied, not scored.** This is the PROVINCE half of C2; C2's exit 0 additionally needs the entry
  file, the S249 row + snapshot pin, the S248 `used-by` update, the SKILL.md SDK line and the registry
  row (other seats). Nothing here claims a C2 after-value.
- **No r80 artifact ported** in this seat — the remit was the `## Core` bullet; `Kb80E04DeadPointer.patch`,
  `Kb80E05GrammarFix.patch`, `run-battery.sh`, `refresh-corpus-baseline.py` belong to the C1 seats and
  were not consumed here.
- **Residual risk:** (g) is confirmed by the counter's author but not yet measured on the frozen counter
  bytes; if the frozen counter moves the span into its own bullet the change is a one-line move, and no
  wording of the r80 bullet may change either way (r80 (h) and r81 (g) both match by substring).
- **Write scope:** only `…/.ufo/waves/round-81/build/` (patch, receipts, this draft's build artifact) and
  `…/.ufo/waves/round-81/w1/` were written; the lane's `PROVINCE.md`, `verifiers/`, `SKILL.md`,
  `corpus/`, `plans/` and `.ufo/state/` are untouched, and the lane git index was never staged.
- **Tools:** none installed or upgraded (pacman paused host-wide; nothing needed).

VERDICT: PROVINCE.md `## Core` extension drafted as a pure 329-B insertion inside the round-80 bullet's parenthetical (patch applies clean at base, reproduces sha256 933e1233…); `check_sibling_census.py --province` and `check_province_core.py` both stay exit 0 with § Adjacent byte-identical, and the derived-then-confirmed r81 (g) arm reads base 0 → tip 1; not applied, no claim after-value measured.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S10Province.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S10Province.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S10Province-receipts.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81S10Province.md
