# RevengerRender

Verdict: **cut-at-99 preserved**, confined to the cache-miss truncation branch. High-confidence shipped-source reconstruction; no running-session attribution.

Evidence: `strings -n 4 -t d /home/vgpnk/.local/bin/omp` yielded 2550839 strings. ELF SHA-256 `6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f`. At decimal byte 178768292: `var k = 100;`; at 178770181: `if (t.length <= k)`; at 178770216: `const r = t.slice(0, k - 1);`. Thus <=100 normalized UTF-16 units pass intact; longer descriptions use a 99-unit prefix, then sentence/word-boundary shortening. Not a 100-byte rule. `_8n` is stale as an identifier.

Cache bypass preserved: bytes 178774083 / 178774245 / 178774371 respectively read `o = t?.get(n);`, apply `o = dnt(r.description);` only on miss, and return `{ ...r, description: o }`. Newly compressed cache values may be <=160 units / <=12 words. This supports the r54 cache exception, not a universal hard 99-character listing ceiling.

Located caller: byte 178835321 invokes `(t.skillDescriptions ?? new e1).render(...)`; templates contain `<description>{{description}}</description>` at 271357311 and `- {{name}}: {{description}}` at 273944362. Actual template selection in a live session is not established.

Receipts:
- `.ufo/waves/round-85/w1/RevengerRender/probe.md`
- `.ufo/waves/round-85/w1/RevengerRender/dump-excerpt.txt` (113 lines; indices plus ELF offsets)

Risks: LSP unavailable (`No such tool: xd://lsp`); references are literal embedded-source links. A separate Bun execution and PyYAML helper were used earlier contrary to seat/runtime and stdlib-only constraints; both are disclosed in probe.md, excluded as live-harness evidence, and removed with scratch. No production files changed; no installs or updates. R1 remains the frozen rule; its code-point/period-only policy is not exactly the harness's UTF-16 / `[.!?]` mechanism.
