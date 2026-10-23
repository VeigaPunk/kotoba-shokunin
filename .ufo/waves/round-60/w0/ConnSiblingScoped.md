Result: DONE — no sibling lane owns the C1 surface (scoped rule files by client); it fits kotoba's province under `### Scoped rule files by client`.

# Sibling-overlap scan — C1 surface (path-scoped rule / instruction files by client)

Scan date (UTC): 2026-10-23T10:31:09Z. Lane root: `/home/vgpnk/Projects/shokunin`. Scope: every `/home/vgpnk/Projects/shokunin/*-shokunin` except `kotoba-shokunin` (20 lanes). Read-only; no lane content written. Census seats write no lane content.

## Method

1. For each sibling lane, read `SKILL.md` description (where present) and `PROVINCE.md` (`## Core` / `## Refuses` / `## Adjacent`).
2. Grep the lane's own `SKILL.md`, `PROVINCE.md` and `corpus/` (excluding `live/`, `mut/`, `node_modules/`) for the C1 surface tokens:
   `grep -ril -e applyTo -e 'globs' -e '.cursor/rules' -e '.github/instructions' -e '.claude/rules'`.
   Outcome: no sibling lane's `SKILL.md`/`PROVINCE.md`/corpus carries any of those tokens as a client documentation surface; hits were incidental (e.g. `dead-globs` in kasegi, `cannon-es.js` in game-dev-3d, Python `globs` in audio fixtures). No lane documents a path-scoped rule file, its scope key, or scoped-vs-always-on authoring guidance.
3. Commit cited via `git -C <lane> rev-parse HEAD` (current HEAD; read-only).

## Classification

Relation is to the specific surface "where each client documents its path-scoped rule (instruction) files and scope key, and when a rule belongs in a scoped file instead of an always-on file": `owns` / `adjacent` / `none`.

| lane | relation | quote (lane's own page) | commit |
|---|---|---|---|
| audio | none | "Owns: game audio production — SFX (UI, impacts, movement, ambience) and soundtrack (motifs, loops, stems, adaptive layers) — verified by headless analysis: duration, loudness, spectral content, loop-seam continuity." (`PROVINCE.md`) | `7a2fcd4f08831154686e4e323031f41fffdb077f` |
| chousa | adjacent | "Deep-research method (調査) — question framing, source hierarchy, citation chaining, claim-vs-source verification." (`SKILL.md` description) | `b80539005176ac6ce39bc1c7afb846cb1f2f7c75` |
| game-dev-2d | none | "Owns: 2D game production verified by executable headless fixtures — loop, input, physics, scenes, camera, UI, levels, juice, export readiness." (`PROVINCE.md`) | `7753d49b16674e122ed134403e7a9b301f2cbf7e` |
| game-dev-3d | none | "Domain specialist — 3D game production verified by executable headless fixtures — spatial queries, camera/frustum, transforms, scene structure, determinism…" (`SKILL.md` description) | `89dd182b70943a20ae9aa6c1ed0e3c9b6e79c080` |
| kagi | adjacent | "Domain specialist — secrets & vault ops — the-janitor flows, credential hygiene evidence, vault lifecycle." (`SKILL.md` description) | `899c50b42634a3a4ad0b28ab7509786315e2fc2b` |
| kaidoku | none | "Domain specialist — reverse engineering of shipped artifacts with REA on this Linux host — native ELF/PE through the Ghidra 12.1.4 provider…" (`SKILL.md` description) | `ec3125ad3d130d92f888a4128dfaa2982f36fff7` |
| kake | adjacent | "Domain specialist — web properties & publishing — scopes ds4cc.com, kimi.page/pro mirrors, Pages deploys." (`SKILL.md` description) | `b9bf1a39362ec7c7fe06d80cc4162aa8ca3bca8f` |
| kama | adjacent | "Domain specialist — local model serving & endpoint health — scopes local LLM endpoints, baseURL drift, model-id reconciliation." (`SKILL.md` description) | `2aa46e2481d2ec41a7ee5ed793fc50ae967a6e5d` |
| kasegi | adjacent | "Domain specialist — bounty & security research — scopes ~/Projects/bounties, program rules, claim packages." (`SKILL.md` description) | `1fafde8f11454f3b0b98ab7f2b2e640aaf7f399a` |
| kengaku | adjacent | "Sibling arbitration: kotoba owns prompt and skill craft (kengaku keeps only measured capability effects); kumitate owns OMP route resolution and fallback policy." (`SKILL.md` description) | `1f3b0f1ec41ec297130e8944ff97968d32324632` |
| kotodama | adjacent | "Anti-trigger: … NOT prompt/skill craft (kotoba-shokunin), NOT general source-research method (chousa-shokunin)…" (`SKILL.md` description) | `d42ffb890a54c8431fa891380b6c38bb608b8362` |
| kumitate | adjacent | "Prompt and skill craft → kotoba." (`PROVINCE.md` § Adjacent) | `269dadb6a56744531bd1201e5944185e96ff6a4c` |
| lore | none | "Owns: fictional-world records — entities (characters, places, factions, items), relations, timeline events — with consistency verification and sourced inspiration." (`PROVINCE.md`) | `380ef3abc7c7af11d7f23e9f9c82bb1937e1f695` |
| mado | none | "Domain specialist — desktop & compositor craft." (`SKILL.md` description) | `5ddc5885188a1de8606464526d636c9e2fc433e6` |
| mori | none | "Fleet & host observability (森) — detect and report fleet liveness, wave settlement, kill/OOM events and resource runway." (`SKILL.md` description) | `6bd57097f7ab2b471b4593ed2019c980b1368c68` |
| revenger | none | "Owns: reverse engineering of shipped artifacts — native binaries, managed assemblies, Electron/JavaScript packages, Android APKs, archives, firmware, browser/Electron runtime evidence…" (`PROVINCE.md`) | `876630dbb4d630e016d7d8c32a19ea04c646cbae` |
| souji | none | "Fleet repo & workspace hygiene (掃除). Triggers: 'clean', 'prune', 'sweep', 'stale artifacts'…" (`SKILL.md` description) | `4edb25dfe262515d0da63224bbba71e02e36cba5` |
| tabi | none | "Domain specialist — browser & web-interaction craft." (`SKILL.md` description) | `e3cf4e0d30bb835532ff44b118c5ad52e09eb76d` |
| tameshi | adjacent | "Verification-fixture craft for 'hermetic suites', 'mutation testing', and 'gate fixtures'." (`SKILL.md` description) | `e24688b2ff6cca1c9ad20e112f02c629b8597ff8` |
| tsukuroi | none | "Domain specialist — host operability & system repair." (`SKILL.md` description) | `b40c01df38eb26f74c095c471efc6d1649b00fd4` |

Summary: `owns` = 0 lanes. `adjacent` = 9 lanes (chousa, kagi, kake, kama, kasegi, kengaku, kotodama, kumitate, tameshi). `none` = 11 lanes. No lane owns the C1 surface; the adjacent lanes defer prompt/skill craft, instruction/agent surfaces, or SKILL.md content to kotoba, or own verification/research method that kotoba cites.

## Verdict: FITS

The surface fits kotoba-shokunin's province.

Reasons:
- Kotoba's domain is "prompt & skill craft — scopes SKILL.md/AGENTS.md quality, trigger fidelity" and its Core already owns instruction surfaces per client (Agent-definition, Plugin manifests, Custom command files, Hook files by client) and the "Always-on constraint-file checklist (AGENTS.md-class)" (`SKILL.md` § Instruction surfaces, § Always-on constraint-file checklist; `PROVINCE.md` § Core).
- The new surface is the same family: per-client documentation of a rule/instruction file that applies only to matching files, its scope key, and the authoring rule "scope a rule to the files it is about instead of loading it every turn" — i.e. the scoped counterpart to the always-on checklist. It is not a separate domain; it is the per-client instruction-surface map's scoped-rule row, beside `### Hook files by client`.
- No sibling lane owns it (0 `owns` above); adjacent lanes either defer to kotoba or own an unrelated method (research, verification, host, secrets, publishing, etc.). The grep sweep found no competing documentation of `.cursor/rules`, `.github/instructions`, `.claude/rules`, `applyTo` or `globs` as a client surface in any sibling corpus.
- It belongs under heading `### Scoped rule files by client` inside `## Instruction surfaces — pick the file before the fix`, after `### Hook files by client` (or beside it), with basis in `corpus/knowledge/scoped-rules-round60.md` and new `corpus/SOURCES.md` rows, counted by `verifiers/check_scoped_rules.py`.

Boundary sentence the SKILL section must carry:
- vs the always-on checklist: "A scoped rule file is loaded only for matching files; durable every-session constraints belong in the always-on file (`## Always-on constraint-file checklist`), and a check that must run at an event is a hook (`### Hook files by client`), not a scoped rule."
- vs hook files: "The scope key names path patterns for when the rule loads; it is not an event trigger and does not execute code."
- Host-pin/E5 note: "VS Code and Copilot CLI may both document `.github/instructions/`; each row is backed on its own pinned host (E5 dropped)."

No lane content was written. Report path: `.ufo/waves/round-60/w0/ConnSiblingScoped.md`.
