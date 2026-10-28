# Kb80V03Instruments — pin/blob exactness audit

Base: `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`. I recomputed blobs from committed bytes in scratch clones; no lane files were changed.

## Findings by severity

### High — initial E06 pin mismatch was corrected before the final E06 bytes

The first published E06 counter (`15cc1761…`) pinned Y01 candidate blobs `cc182613…` / `89f392da…`, not the canonical E04+E05 outputs. Applying the published E04 patch and then the published E05 patch to base gave integrity `68ccce1c152c915e16893a5157c9d5878df779fb` and independent `e887de71892ecfc6be5b3f47e362ce8a766c5c89`; both equal E05's `Kb80E05GrammarFix.blobs` and `combined-blob.txt`. I notified the owners and L1. L1 selected standalone E04 + canonical E05; E06 then replaced the two stale Y01 additions with those E05 composition blobs.

I independently applied the final `Kb80E06CounterErratum.patch` to a fresh base clone: apply-check exit 0, apply exit 0, `cmp` against `check_tip_battery.amended.py` exit 0. Final counter SHA-256 is `20e4960126961fe1892cf8647406a4619313db25deb3550a02c0bd41e6445276`; final patch SHA-256 is `fcd886870d3689468c8fa2a5f9aad27b4e0b25e9a4ca06dcf89d7fe297b80382`. `python3 -B verifiers/check_tip_battery.py --self-test` prints `self-test: 0 failure(s) over 69 assertions`, exit 0. The final pin rows now agree with the canonical E05 blobs below; the Y01 values are absent from the final counter. This resolution is also recorded in Kb80E16PinAudit.txt §12; its earlier §6.3 values describe the superseded counter.

### Medium — a source-row provenance error remains outside this pin repair

Both base corpus gates reported `commit_unresolvable=2` at `corpus/SOURCES.md:171-172`, token `7bb48f213ac677f943d5c791199ed3dddf302f00`; `451a02ff` and `cfb894a5` are quoted context, not those blockers. The line-scope E05 class moves the two blockers into `commit_external` INFO; it does not verify the claimed repository identity. S230 (`:171`) attributes that hash to `badlogic/pi-mono`, while S230.fetch.json records pi-mono's fetch-time main as `bb65e3e49710fbd14f10c7792d0eaa6e2b2c5923`; S231 (`:172`) records the `7bb48f…` Mistral Vibe revision. Thus S230's source row remains factually wrong after the classification-only repair. No SOURCES row was rewritten (M45); the round-80 lesson records this residual.

## INSTRUMENT_PINS table

“Recomputed” is the current committed blob at base for legacy pins, and the E04∘E05 composed stack blob for the two new E5 pins. `n` on a legacy row means that particular historical alternative is not today's blob; the instrument's current blob is covered by another pin in its tuple.

| Instrument | Scope | Pin value | Recomputed | Agrees? |
|---|---|---|---|---|
| `check_gate_registry.py` | base | `95ffed389f483c3d6f93db3c08dcfdb9a2240576` | `95ffed389f483c3d6f93db3c08dcfdb9a2240576` | y |
| `check_assertion_floors.py` | base | `780f6fe5184ecb94e70f0f79446ae4339d1aec27` | `9cb860bda21ef8d24fcb0603aa85372b96f3ac41` | n |
| `check_assertion_floors.py` | base | `50348420260ab41a916ef1ab19d27966565de5af` | `9cb860bda21ef8d24fcb0603aa85372b96f3ac41` | n |
| `check_assertion_floors.py` | base | `9cb860bda21ef8d24fcb0603aa85372b96f3ac41` | `9cb860bda21ef8d24fcb0603aa85372b96f3ac41` | y |
| `verify_skill_checklist.py` | base | `8d44c063e3d4b57c7c421c3107879e61983249bf` | `6aab16849bd6d71ded8f3bcb3f95668f14f6a78f` | n |
| `verify_skill_checklist.py` | base | `6aab16849bd6d71ded8f3bcb3f95668f14f6a78f` | `6aab16849bd6d71ded8f3bcb3f95668f14f6a78f` | y |
| `verify_corpus_integrity.py` | base | `71cb2730bfe89064567ad429bfd7c2da62aceb45` | `e470eaaea5ef11c582b8353c9344ddf730c1a57a` | n |
| `verify_corpus_integrity.py` | base | `e470eaaea5ef11c582b8353c9344ddf730c1a57a` | `e470eaaea5ef11c582b8353c9344ddf730c1a57a` | y |
| `verify_corpus_integrity.py` | E04∘E05 | `68ccce1c152c915e16893a5157c9d5878df779fb` | `68ccce1c152c915e16893a5157c9d5878df779fb` | y |
| `verify_corpus_independent.py` | base | `176abae3b66930d644482f95e1363932e4d143b4` | `edac0df79324ba62ee25ff10a6a4d422ef59da61` | n |
| `verify_corpus_independent.py` | base | `edac0df79324ba62ee25ff10a6a4d422ef59da61` | `edac0df79324ba62ee25ff10a6a4d422ef59da61` | y |
| `verify_corpus_independent.py` | E05 | `e887de71892ecfc6be5b3f47e362ce8a766c5c89` | `e887de71892ecfc6be5b3f47e362ce8a766c5c89` | y |
| `check_correction_sweep.py` | base | `c94b771fa7d798ef45fc3bb640422ee7910f81a6` | `c94b771fa7d798ef45fc3bb640422ee7910f81a6` | y |

The two methods `git rev-parse <base>:<path>` and `git show <base>:<path>` piped through `git hash-object --stdin` agreed for all six base instruments (each command exit 0); receipt: `build/Kb80V03Instruments/base-pin-computation.txt`. All six current base blobs are members of their respective final pin tuples (6/6 coverage). The E04-only blob `051b8c5f8676cba5c8d6047c8c9f7fcb56cd8f9f` is intentionally not the final integrity pin: the chosen stack is E04∘E05.

## Published-value recomputations and self-tests

- **E04:** r79 patch is at `.ufo/waves/round-79/build/Kb79E04DeadPointer/Kb79E04DeadPointer.patch` (directory form; the flat path in the prompt does not exist). Its SHA-256 is `d7169dd8f9db17a908f00c1e62a668d73c7ca96cca75626807fb81889f4a5d78`; the r80 patch is byte-identical. Scratch `git apply --check` and apply both exited 0. Resulting integrity blob `051b8c5f8676cba5c8d6047c8c9f7fcb56cd8f9f`, file SHA-256 `4b388798ec669ce2746bb98a1137e73176ea55d5ad1ee2ed8121b22a629771db`, agrees with `Kb80E04DeadPointer.blob` and E16 §3.
- **E05:** patch SHA-256 `a4345d34d3a8e35d7697b5abc05d077c2bb43e49e636edd6937590b1b223a2d3` agrees with its `.patch.sha256`. E04 then E05 apply-check/apply all exited 0. The final blobs above agree with E05's `.blobs`, `.combined-blob.txt`, and the final E06 pin rows. Reverse order is also reported by E05/E16 as producing identical composed blobs.
- **E06:** final counter SHA-256 `20e496…` agrees with `.sha256` and `check_tip_battery.amended.py`; scratch patch application and byte comparison exited 0; `--self-test` passed 69/69 assertions. Final E06 numstat is 30 added / 12 deleted lines in the counter (not one of the six pinned instruments). E16 §12 rechecked the final counter and canonical pins; its older §6.3 snapshot is superseded. E06's own landing-recipe receipt (`build/Kb80E06CounterErratum/landing-recipe-output.txt`) independently reproduces rev `fc91d8d2…`, counter `20e49601…`, instrument blobs `68ccce1c…` / `e887de71…`, six-instrument numstat 22/3 + 10/3 + 28/2 = 60 added / 8 deleted, and registry 63 of 63 — all consistent with my recomputation.
- **Gate self-tests at E04∘E05:** `python3 -B verifiers/verify_corpus_integrity.py --self-test` → 166 assertions, 0 failures, exit 0; `python3 -B verifiers/verify_corpus_independent.py --self-test` → 106 assertions, 0 failures, exit 0.
- **Floors:** in a fleet-shaped scratch tree with E04+E05 applied, `python3 -B verifiers/check_assertion_floors.py` exited 0. `corpus_integrity observed=166 floor=164` and `corpus_independent observed=106 floor=105` both PASS. Full receipt: `build/Kb80V03Instruments/canonical-floors-fleet-shaped.txt`.

## Residual risk and verification gap

The line-scope external class is intentionally classification-only: it counts a non-lane/non-fleet citation as INFO and does not establish that a row's cited repository/revision is factually correct. S230's mismatch therefore remains an append-only source-correction issue, not something this gate change resolves.

I did not run the final full-stack tip battery or score C1's after-value. E10 later measured the L1-selected option-B stack (standalone E04 + canonical E05 + final E06 counter) at both invocation forms: `guards 5 of 5; tip battery exit 0: 6 of 6`, exit 0, 60 added / 8 deleted (receipts: `build/battery-stack-optionB/`). E06's own final landing-recipe receipt independently reproduces the same composition. That after-value remains provisional: `.ufo/waves/round-80/receipts/freeze-shas.txt` is still absent, so no frozen-counter receipt is available to verify. Because the option-B stack sits at exactly 60 added / 8 deleted, any further added line in a battery script trips `instrument-size` — the plan's honest-stop channel, which no one has narrowed.

VERDICT: Base and final E04∘E05 pins match; both edited gates pass self-tests/floors. E10 reports 6/6 at the full stack, pending freeze receipt. S230 provenance remains wrong.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/w1/Kb80V03Instruments.md; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80V03Instruments/base-pin-computation.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80V03Instruments/e06-counter-audit.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80V03Instruments/canonical-floors-fleet-shaped.txt