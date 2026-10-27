# Round 77 w2 — F02CheckRunC2: C2 frozen-counter falsification

## Verdict and scope

Attacked C2 (consistency, calibration sub-axis): repairs R1–R4 from `plans/round-76.md` § C2, as frozen by `plans/round-77.md`. The latest lane HEAD checked was `6523aced1ee0ebe07dca996213bdc645a6acbd1e` (`round-77: freeze plan, base receipts`). The C2 counter SHA-256 is `989203c40e1aab55fc14ee1d444dd4fa8b49fe01144b2dcdeaa6a27fa39f4a63`, exactly the plan pin; C1's counter also matched its pin, but C1 was not run by this seat. The last commit touching the C2 counter is `ec7f853` (r76 freeze), so the frozen counter is unchanged in r77.

**C2 is not verified at lane HEAD.** At the landed freeze tip all four repairs are open and the required counter is red. No claim-data commit follows the freeze; the tip's committed bytes do not contain the R1 lesson append/receipt, R2 no-harm receipt and citation, R3 note and citation, or R4 closing. Per the assignment this is a blocker, not an inferred after-value. The only lane files written by this seat are the scoped report(s) and evidence receipts under `.ufo/waves/round-77/`; all repair constructions below were scratch-only.

## Exact counter runs

Run from `/home/vgpnk/Projects/shokunin/kotoba-shokunin` with the frozen counter and its own work directory; outputs, including the counter's terminal exit line, are in the named receipts.

- `python3 -B verifiers/check_r75_routed_repairs.py --rev 6523aced1ee0ebe07dca996213bdc645a6acbd1e --work /fast/scratch/hyaku/kotoba-r77/F02Re-RunC2/work` → `measured-rev: 6523aced1ee0ebe07dca996213bdc645a6acbd1e`; `R1: open`, `R2: open`, `R3: open`, `R4: open`; `r75 routed repairs closed 0 of 4`; **exit 1**.
- `python3 -B verifiers/check_r75_routed_repairs.py --rev 2f675548eaad2a037a899d39247c1fd7a88aaf48 --work /fast/scratch/hyaku/kotoba-r77/F02Re-RunC2/work` → `r75 routed repairs closed 0 of 4`; **exit 1**. The findings body matches the committed r77 base receipt after its three header lines are excluded (`base-body-diff-exit=0`).
- `python3 -B verifiers/check_r75_routed_repairs.py --self-test --work /fast/scratch/hyaku/kotoba-r77/F02Re-RunC2/work` → `self-test: 0 failure(s) over 27 assertions`; **exit 0**.

## Repair-by-repair status at lane HEAD

- **R1 open:** `corpus/lessons/round-75.md` is unchanged from the pinned r76 base; no appended correction or committed `.ufo/waves/round-76/receipts/r1-folded-render.txt` exists at the measured tip.
- **R2 open:** `.ufo/waves/round-76/receipts/noharm-at-tip.txt` is absent at the measured tip, and LOG § Round 75 does not cite it. As an independent R2 precondition check, I re-ran both corpus gates on the required historical r75 final tip `ac9f29510d3914a6edb97c8dbdb3445cab9141de` in a scratch sandbox: `python3 -B verifiers/verify_corpus_integrity.py --repo /fast/scratch/hyaku/kotoba-r77/F02Re-RunC2/r75chk --json` → exit 0; `python3 -B verifiers/verify_corpus_independent.py --repo /fast/scratch/hyaku/kotoba-r77/F02Re-RunC2/r75chk --json` → exit 0. Both normalized outputs had no `DRIFT`; integrity reported 144 tracked corpus files. These are genuine greens at the pinned r75 tip, not evidence that R2 data is landed at r77 HEAD.
- **R3 open:** `.ufo/waves/round-76/w2-registry-note.md` is absent at the measured tip; LOG § Round 75 does not cite it. Recomputed from committed r75 results/tree: 64 results, 0 empty outputs, 63 matching report files; `R75Attack28` exists in results output but its report file is absent.
- **R4 open:** the committed Round 75 LOG section has no appended settlement after “w2 falsify results pending”.

The counter's own `render_length_at` recomputation returned `(1022, 1021, 4, 18)` at both `ac9f29510d3914a6edb97c8dbdb3445cab9141de` and `b7f13f4b39cbd43076a85568adca763a6f674e7a` (exit 0), consistent with the frozen clip-preserving convention.

## Scratch falsification and mutation results

These are scratch-only committed worlds, **not lane results or claims**. They demonstrate that the frozen predicate is satisfiable and each repair arm responds to a focused mutation.

- Independently applying the exact E05 R3/R4 note and LOG patch at scratch commit `37b279c6a4e3f20689fbf36084ddc1aa7f94c2eb` → R1/R2 open, R3/R4 closed, `r75 routed repairs closed 2 of 4`, **exit 1**. This reproduces the E05 receipt's result. The note and patch SHA-256s match E05's digest receipt: `07d72021e0369e6247525a4f6551f496e922467346bcef821ab9b9e7b0f19503` and `b309250214f0771fec813238d0c856eda2141ba1cf396b846a291c0932e5ad21` respectively.
- An honest R1–R4 scratch world using the B08 lesson patch, the r76 registry-note draft, a recomputed R1 receipt, the actual normalized gate outputs/exits from `ac9f295`, and a closing LOG line → scratch `fe1e089a98291e13bba7fb5648da83b35396922b`, `r75 routed repairs closed 4 of 4`, **exit 0**. R2 closed only after the counter re-ran both gates and matched the receipt transcript.
- The r76 B08 lesson patch + `log-draft.md` R2/R4 wording (with `<tip-rev>` filled by the pinned `ac9f295…`), r76 registry-note draft, and the same honest receipts → scratch `43548770cc644abe1d4179b2047de23a4fc121d1`, `r75 routed repairs closed 4 of 4`, **exit 0**. The drafts are sufficient when combined with the independently generated receipts.
- **M1 nuance:** my first incomplete mutation replaced `63 of 64` but left the valid `63/64` pair elsewhere in the note; it correctly remained 4/4. Replacing both pair notations at scratch `dd09197aca0b85f66d6ac670b90d9a59fde3d395` reopened only R3 (`3 of 4`, **exit 1**). This is a correction to my mutation, not a counter defect.
- M2 forged the R4 dead count at `3ee26343446e4d41a3b8d6a267417d7f929102ac`: only R4 open, `3 of 4`, **exit 1**.
- M3 changed the R1 receipt's 1,022 to 1,023 at `0d14a8e27ab2ae03713ec685abf885bfb429d42d`: only R1 open, `3 of 4`, **exit 1**.
- M4 changed the R2 first-line revision to the stale `b7f13f4…` at `c86a344a0d0181df0f876e128d738e52224e237e`: only R2 open, `3 of 4`, **exit 1**. The counter independently reran both gates there; both were red with DRIFT and their transcripts did not match.
- A junk/token-dump world at scratch `649f7dbd8635fa64448c7ba8f41bcf4df98ddca7` returned `1 of 4`, **exit 1**: R1–R3 remained open. R4's settlement fact arm accepted the true recomputed 63/64 and 0-dead values, as the counter's documented trust boundary allows; the overall predicate still rejected the junk world.

## Required next step / residual risk

The minimum step before claiming C2 is to integrate and commit the R1–R4 data and receipts without editing either frozen counter, then run the full no-harm battery at the final landed tip. The disclosed D4 work also requires the corpus index/baseline to travel with any new tracked corpus file and the baseline refresh to follow the order in E10's notes; do not infer that this battery is green from the historical r75-tip run above. This step does not require a counter change; landing index/baseline with the corpus changes is necessary to avoid unrelated coverage/operability regressions. No tool was installed.

Evidence files: `.ufo/waves/round-77/receipts/F02CheckRunC2.*` (tip/base/self-test, E05 reproduction, both scratch green worlds, gate transcripts, render recomputation, mutation log, hashes/scope, and base-receipt comparison). Scratch directory was removed before handoff.

VERDICT: BLOCKED — C2 claim data is absent from landed HEAD 6523aced; frozen counter correctly reports 0 of 4 (exit 1), so no C2 closure is verified.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w2/F02CheckRunC2.md; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w2/F02Re-RunC2.md; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/receipts/F02CheckRunC2.c2-tip-6523aced.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/receipts/F02CheckRunC2.c2-base-recheck.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/receipts/F02CheckRunC2.selftest-frozen.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/receipts/F02CheckRunC2.gates-at-r75tip.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/receipts/F02CheckRunC2.render-recompute.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/receipts/F02CheckRunC2.e05-exact-repro.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/receipts/F02CheckRunC2.greenworld-4of4.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/receipts/F02CheckRunC2.mutations.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/receipts/F02CheckRunC2.scope-and-hashes.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/receipts/F02CheckRunC2.base-receipt-body-diff.txt