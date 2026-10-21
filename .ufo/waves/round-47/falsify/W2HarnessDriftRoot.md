verdict: PARTIAL — harness-drift patch is a substantive but incomplete re-derivation, not merely copied values; leaving it unlanded is honest, while its claim that suffixed cache values are served is refuted.

## Axes and recommendation

- **Freshness:** distinguish the shipped renderer's bare-key lookup from the model-specific compression-retry guard.
- **Operability:** distinguish computed preview, compressed cache hit, and retry-suppression record; a shared byte string is not proof of its provenance.
- **Calibration:** retain explicit 21/28 debt, not an implied 28/28 closure. Do not characterize the entire proposed patch as baseline laundering either: it includes a real source investigation and mechanism-level code changes.

Recommendation only: **do not land the proposed patch unchanged.** Not landing it is honest under `corpus/QUALITY.md:20` (Q09) and the explicit exclusion at `LOG.md:2326`, both at `7ad7fadfc09354b74fb66605dfb0c1182c115a2f`. The strongest local counterexample supports retaining the debt, rather than treating the patch's reported 28/28 as closure. This review makes no admission or scoring decision.

## F1 — Writer evidence was promoted to false renderer provenance

**Evidence at the landing:** `verifiers/verify_harness_claims.py:310-315` looks up only `omp_key(template, name, desc)` and otherwise counts a miss; `:331-336` supplies only those bare-key hits to catalogue matching. These describe compressed-cache lookup, not every possible preview-render path.

**Proposal evidence:** `.ufo/waves/round-47/build/C1HarnessDriftRoot.patch:105-120` adds `cache_lookup`, selecting any key beginning `bare + ':'`; `:151-164` then uses that value as the rendered/cached description and removes it from misses; `:179-188` promotes it into catalogue-match evidence. The report `build/C1HarnessDriftRoot.md` explicitly acknowledged that the render lookup order had NOT been checked. Its recommendation nevertheless calls the misses reader defects and the suffix rows served fallbacks.

**Strongest counterexample, frozen source:** `/fast/scratch/kotoba-r47/shared/omp-18.12.5.strings`, SHA-256 `33df0aeffc4565967bc1a3b42621f8eade0e6e4c2ae8733319fcd484902fb301`, character offset **26181578**, contains `class fM`. Its `render` computes `n = D(r)`, reads its in-memory map at `n`, then `t?.get(n)`. On absence it computes `o = xze(r.description)` and schedules `this.#r(t, n, r)`. `snapshot` similarly uses the bare-key memory map or computes `xze`.

The suffix appears in the asynchronous compression path at character offset **26182745**: `p = n.modelKey(); d = ... \`${t}:${p}\`; if (d !== undefined && e.get(d) !== undefined) return;`. Successful compression writes `e.put(t, u)`; unusable compression writes `e.put(d, xze(r.description))`. Thus the suffix record suppresses retry **for the selected model**. The renderer does not retrieve its value. Preview bytes equalling that record are insufficient to establish that the renderer consumed the record.

**Repro:** execute the supplied `W2HarnessDriftRoot.probe.txt` with Python (it extracts the actual proposed helper, not a rewritten helper). For `bare = 'b' * 64` and `{bare + ':other/model': 'not the computed preview'}`, proposed lookup returns `('preview-fallback', 'not the computed preview')`. The shipped render path, starting with an empty memory map and no bare row, instead computes `xze(r.description)` regardless of that suffix value. The latter is a static source prediction, not an executed omp observation. Additional actual helper results: an empty model suffix is accepted; with `a/model -> old` and `z/model -> current`, the first value wins. SQL sorting makes that deterministic, not semantically correct.

**Impacted axes:** freshness (wrong runtime model), operability (wrong attribution of served data), calibration (28/28 can be obtained by redefining the miss without matching renderer behavior).

**Smallest safe correction:** keep bare compressed-cache misses as a separately named observation. Derive and compare the computed preview for bare misses; independently inventory model-specific retry-suppression records, checking their values against the computed preview if asserting that property. Only assert retry suppression for an identified selected model, otherwise explicitly mark it unknown. Do not count arbitrary suffix values as rendered cache hits. Add a held-out fixture with absent bare key and deliberately different suffixed value; the renderer prediction must remain the computed preview. Re-derive expected pins only after those meanings are explicit.

This is a fixable proposal defect. It is not evidence that the actual three source-report suffix records contain wrong values, nor that their reported host-event decomposition is fabricated.

## F2 — Nonlanding disclosure is honest, but one sentence is too broad

At `7ad7fad`, `LOG.md:2326` records harness 21/28 **before and after**, same seven drift ids, explicitly **not claimed**. `SCORECARD.md:108` carries the re-derivation forward. These are not a harness-green claim and do not hide the unfinished gate behind C1 surfaces/pins success.

However `plans/round-47.md:43-45` says `cache rows absent for them`. The build report itself documents suffixed rows, and the shipped writer supports that namespace. The defensible wording is **bare compressed-description rows absent; model-specific preview/retry records reported present**. Do not simply replace this with the proposal's `cache_misses=0`: F1 shows why that also overstates provenance.

**Smallest safe correction:** clarify the plan's current wording; append any correction to historical logs/receipts rather than rewriting them. Name the unlanded patch and its unresolved renderer-model defect when carrying Q09. No production files were changed in this review.

## F3 — Patch is not directly applicable at the landing

`git apply --check .../C1HarnessDriftRoot.patch` in the canonical-layout scratch clone at `7ad7fad` exits **1**, failing both `verifiers/baseline.json:1` and `verifiers/verify_harness_claims.py:53`. The patch was explicitly offered against BASE, so this is an integration prerequisite, not dishonesty. A rebased version must preserve the landed substrate-pin provenance/default binary path rather than restoring an older authority or selecting whichever npx installation has newest mtime.

## Commands actually run in this review

Working directory: `/fast/scratch/kotoba-r47/w2/W2HarnessDriftRoot/kotoba-shokunin`.

| Command | Exit | Key result |
| --- | --- | --- |
| `git rev-parse HEAD` | 0 | `7ad7fadfc09354b74fb66605dfb0c1182c115a2f` |
| `python3 -B verifiers/verify_harness_claims.py --self-test` | 0 | `0 failure(s) over 10 assertions` |
| `git apply --check /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-47/build/C1HarnessDriftRoot.patch` | 1 | Both target files reject the BASE patch at the landing |
| `python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-47/falsify/W2HarnessDriftRoot.probe.py` | 0 | Actual proposed helper accepts wrong-model/empty-suffix rows; prints exact renderer/writer excerpts and digests |

The probe was subsequently renamed to **`W2HarnessDriftRoot.probe.txt`** to conform to artifact bounds; replay uses the same command with `.txt` instead of `.py`. Patch SHA-256 observed by the probe: `8e6bec3d246b3aaf19d8c4227a6a4f4ec1e14e3714cbc618d4aefedd675c595d`. The source offsets above are Python Unicode-character offsets in the supplied strings dump, not ELF addresses. Exact probe output is also retained by the tool at `artifact://16033`.

## Limits / not checked

- No fresh live harness run or private host DB/session/log reads in this review. The supplied earlier results report exit 1, 21/28 and the seven drift ids; those are prior evidence, not newly exercised passes. I did not rerun a user-reported failure merely to confirm it.
- No new proof of the three skills' installation times, per-row insertion times, actual selected compression model, or live catalogue lineage. Those remain the build report's evidence/limitations.
- No target runtime, omp session, opencode wrapper, network fetch, canonical judge, or another agent was invoked. The frozen dump was inspected as data; target code was not executed.
- No complete patched 28/28 run, no patch application, no commits, no production edits, and no review of unrelated C1/C2/C3 gates. The self-test does not validate the proposed helper; that helper was separately falsified by the minimal extraction probe.
- No tools installed or upgraded. Only this report and its uniquely named small probe artifact were written in the allowed falsify directory.
