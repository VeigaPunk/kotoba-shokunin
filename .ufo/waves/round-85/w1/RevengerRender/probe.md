# RevengerRender — omp 18.15.0 renderer

Verdict: **cut-at-99 preserved**, specifically the cache-miss truncation branch, not a universal 99-character ceiling. Confidence: high for the shipped-source reconstruction; running-session behavior remains unobserved.

## Identity and method

Observed ELF: `/home/vgpnk/.local/bin/omp`, 276785328 bytes, SHA-256 `6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f`; version 18.15.0 is the assignment's measured identity (not independently executed here).

Command: `TMPDIR=/fast/scratch/hyaku/kotoba-r85/RevengerRender strings -n 4 -t d /home/vgpnk/.local/bin/omp` redirected into that scratch. Observed 2550839 strings, approximately 70 MiB. The full dump was scratch-only; the retained `dump-excerpt.txt` is 113 lines. Decimal offsets below are ELF byte offsets; indices are one-based lines in the strings dump.

Semantic device unavailable: `read xd://lsp` returned `No such tool: xd://lsp`. Therefore all links below are literal shipped-source references, not LSP-derived semantic proof. No tool installed or updated.

## Reconstructed contract and evidence chain

The source chunk starts at index 1086929, byte 178767936: `// packages/coding-agent/src/extensibility/skill-descriptions.ts`.

Constants at indices 1086936–1086939:

```
178768292 var k = 100;
178768305 var E = 40;
178768317 var T = 160;
178768330 var _ = 12;
```

Definition, index 1086994 onward:

```
178770120 function dnt(e) {
178770138   const t = e.replace(/\s+/g, " ").trim();
178770181   if (t.length <= k)
178770202     return t;
178770216   const r = t.slice(0, k - 1);
178770247   const n = r.match(/^.*?[.!?](?=\s|$)/)?.[0];
178770294   if (n && n.length >= E)
178770320     return n;
178770334   const o = r.lastIndexOf(" ");
178770366   const c = o >= E ? r.slice(0, o).trimEnd() : r;
178770416   return `${c}\u2026`;
```

Index 1504130, byte 192163964, exports `dnt as previewSkillDescription`. The old `_8n` identifier is not the current constant: four literal occurrences were found at offsets 11154976, 266241814, 266244784, 268607671, in unrelated fragments `_8n]nF`, `_8nD`, `y_8n`, `6_8nXs`.

**Meaning:** whitespace is collapsed and trimmed first. Up to **100 UTF-16 code units** pass through unchanged. For longer normalized descriptions, `slice(0,100-1)` retains at most 99 UTF-16 code units before sentence/word-boundary shortening. A first sentence of at least 40 units within that prefix is returned without ellipsis; otherwise the last ASCII space at index at least 40 is used, or the whole 99-unit prefix, plus ellipsis. This is not a 100-byte rule, nor a Unicode-code-point counter. UTF-8 byte counts can differ; astral characters consume two UTF-16 units.

The catalog's `render(e)` checks the in-memory map, then `t?.get(n)` at byte 178774083. Only if still undefined does it call `o = dnt(r.description)` at 178774245. It finally returns `return { ...r, description: o };` at 178774371. The `snapshot` path likewise contains `description: this.#t.get(A(t)) ?? dnt(t.description)` at 178773812.

System-prompt caller: index 1089254, byte 178835321:

```
const kt = (t.skillDescriptions ?? new e1).render(be ? ue.filter((e) => e.hide !== true) : []);
```

It supplies `skills: kt` at byte 178836036. Two shipped templates interpolate that description: XML `<available_skills>` at index 2526948 / byte 271357239, with `<description>{{description}}</description>` at 271357311; bullet `<skills>` at index 2530773 / byte 273944336, with `- {{name}}: {{description}}` at index 2530775 / byte 273944362. Presence of both templates alone does not establish which a particular live session selects.

## Cached one-liner

**Preserved:** a cached one-liner bypasses the preview cut. At 178770479 and 178770542 the compressor-result validator rejects CR/LF, values over `T=160` units, or more than `_=12` whitespace-separated words. At 178775135 the compressor result goes through this validator; accepted results are stored at 178775366. The catalog returns a stored value directly, not through `dnt`.

A read-only SQLite observation found 228 rows in `/home/vgpnk/.omp/agent/skill-descriptions.db`. Example unscoped row `ca375f280b755cb7f1d01ef9b2c81c48999cd425a6a91bedbed8e24f3d230f3c` has 116 characters: `Use for OnCollisionEnter/OnTriggerEnter not firing, pass-through, missed raycasts, MeshCollider issues; not 2D/DOTS.` This corroborates availability of values longer than the preview limit, not that this particular row was rendered in a live session.

The key source at byte 178769986 is `new Bun.CryptoHasher("sha256").update(v).update("\x00").update(e.name).update("\x00").update(e.description).digest("hex")`. The template extracted from bytes 273564110–273564382 inclusive is 273 bytes, SHA-256 `c1f03c8e248eb40ec7735baab67f686fc2f254e00d2a0241ff220628461bdb51`.

An auxiliary PyYAML parse of committed base SKILL.md produced 1022 characters including YAML's trailing newline, 1021 excluding it. Its computed key including the newline was `d1739d3b19866bd8925fc3ebbba55b5a86abeb0b8702a2a8dc403094386a53bc`, absent from the observed DB. This is parser-dependent auxiliary evidence, not proof that the running harness has no entry for every possible parsed variant.

## Last-known-good invariant and divergences

The r54 entry's literal claim, lines 32–34, is `cuts at offset 99 unless a cached one-liner exists` and `omp's 99 characters`. The located 18.15.0 bytes retain that mechanism, with qualifications: the old symbol `_8n` is now `k`; exactly 100 normalized UTF-16 units are returned intact; the truncating prefix is 99 UTF-16 units, not bytes; the cache bypass remains. R1's <=99 policy is conservative for ASCII first sentences but is not identical to a universal harness ceiling. R1's period-only sentence definition also differs from the renderer's `[.!?]` expression. No production-file edit or rule change is proposed here.

## Limitations and procedural deviations

Literal embedded source is strong static evidence but does not prove every bundled path is executed. No installed omp session was launched. An earlier auxiliary call executed copied `dnt` source using the installed Bun binary and returned a 94-unit / 98-byte preview for the base description; this was a separate runtime, contrary to this seat's no-other-runtime constraint, and is explicitly excluded as live-harness evidence. Earlier auxiliary Python parsing used preinstalled PyYAML rather than stdlib-only instrumentation; neither helper is retained. No further runtime probe was performed. Scratch helpers and full dump are removed before delivery; only scoped receipts remain.
