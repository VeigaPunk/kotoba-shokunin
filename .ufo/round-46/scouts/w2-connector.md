# W2 Connector Report: Cross-Lane Adjacency & Synthesis (Round 46)

## 1. Sibling Scan & Missing Surfaces
- `audio-shokunin`: has `PROVINCE.md:3-6`; NO `SKILL.md`, NO `corpus/README.md`, NO `corpus/QUALITY.md`, NO `corpus/SOURCES.md` (`test -e audio-shokunin/SKILL.md` exit 1).
- `revenger-shokunin`: has `PROVINCE.md:3-7`, `corpus/README.md`, `corpus/QUALITY.md:1-37`; NO `SKILL.md`, NO `corpus/SOURCES.md` (`test -e revenger-shokunin/SKILL.md` exit 1).
- `game-dev-2d-shokunin`: has `PROVINCE.md:3-5`, `corpus/README.md`, `corpus/QUALITY.md:1-25`; NO `SKILL.md`, NO `corpus/SOURCES.md` (`test -e game-dev-2d-shokunin/SKILL.md` exit 1).
- `game-dev-3d-shokunin`: has `PROVINCE.md:3-10`, `SKILL.md:1-4`, `corpus/README.md`; NO `corpus/QUALITY.md`, NO `corpus/SOURCES.md` (`test -e game-dev-3d-shokunin/corpus/QUALITY.md` exit 1).
- `kumitate-shokunin`: has `PROVINCE.md:3-6`, `SKILL.md:1-4`, `corpus/README.md`; NO `corpus/QUALITY.md`, NO `corpus/SOURCES.md` (`test -e kumitate-shokunin/corpus/QUALITY.md` exit 1).
- `souji-shokunin`: has `PROVINCE.md:3-5`, `SKILL.md:1-4`, `corpus/README.md`; NO `corpus/QUALITY.md`, NO `corpus/SOURCES.md` (`test -e souji-shokunin/corpus/QUALITY.md` exit 1).
- All siblings except `chousa` lack `corpus/SOURCES.md` (`test -e chousa-shokunin/corpus/SOURCES.md` exit 0; all others exit 1).

## 2. Adjacent List for kotoba PROVINCE.md
- `chousa` — deep-research method (question framing, source hierarchy, citation chaining, claim verification) — `../chousa-shokunin/PROVINCE.md:3-8`
- `kumitate` — orchestration mechanism, tooling, dispatch runtime, and swarm/native task lifecycle — `../kumitate-shokunin/PROVINCE.md:3-5`
- `kengaku` — general LLM/model evaluation, benchmark arena, and route telemetry — `../kengaku-shokunin/PROVINCE.md:3-8`
- `tameshi` — reusable verification-fixture craft, mutation testing, and fail-closed audit methods — `../tameshi-shokunin/PROVINCE.md:3-8`
- `kotodama` — linguistic-cultural worldbuilding, conlangs, mythic-symbolic systems, and naming — `../kotodama-shokunin/PROVINCE.md:3-8,18`
- `mado` — desktop & compositor configuration (Hyprland, waybar, walker); reads omarchy skill — `../mado-shokunin/PROVINCE.md:3-12`
- `revenger` — reverse engineering of shipped binary/managed/APK/Electron artifacts via REA — `../revenger-shokunin/PROVINCE.md:3-7,22`
- `mori` — fleet & host observability, liveness, wave settlement, and OOM/resource monitoring — `../mori-shokunin/PROVINCE.md:3-10`
- `kama` — local model endpoints, baseURL drift, and serving health — `../kama-shokunin/PROVINCE.md:3-4`
- `kasegi` — bounty and security research, prompt injection exploits, and claim packages — `../kasegi-shokunin/PROVINCE.md:3-4`

## 3. Contested-Scope Items
- **Dispatch Prompts vs Tooling**: `kumitate` owns dispatch execution/runtime (`kumitate-shokunin/PROVINCE.md:3`, `scripts/ufo-swarm-wave.mjs:50-51`); `kotoba` owns dispatch prompt craft, wording, and trigger fidelity (`corpus/knowledge/dispatch-prompt-audit-round7.md:1`).
- **Harness Extraction vs Binary RE**: `revenger` explicitly refuses harness auditing (`revenger-shokunin/PROVINCE.md:22`); `kotoba` reverse-engineers harness system prompts and router offer mechanics (`corpus/knowledge/instruction-surface-census-round13.md:1`, `opencode-extraction-round14.md:1`).
- **Trigger Fidelity vs Model Eval**: `kengaku` owns general model evaluation (`kengaku-shokunin/PROVINCE.md:3-8`); `kotoba` evaluates skill trigger fidelity and router offer matching (`corpus/knowledge/skill-activation-telemetry.md:1`, `corpus/knowledge/trigger-miss-proxy-round6.md:1`).

## 4. Curated Sources to Cite Rather Than Re-derive
- **Deep-Research Method**: `chousa-shokunin/SKILL.md:17-31` & `chousa-shokunin/corpus/SOURCES.md:12-28` (S002 IFCN, S003 SIFT, S005–S007 citation fidelity). Mandated by `SOURCES-CONTRACT-v1.md:52-55` rule 3: research method stays chousa's.
- **JSON Lines Format**: `chousa-shokunin/corpus/SOURCES.md:23` (S013, `jsonlines.org`); kotoba parses JSONL in harness comparator (`verifiers/compare_harness_independent.py:1-40`).
- **Model Evaluation Literature**: `kengaku-shokunin/corpus/knowledge/eval-prior-art-calibration.md:1-50` & `PROVINCE.md:22-26` (arXiv/ICLR/ACL eval papers).

## 5. Reusable Cross-Lane Patterns
- `chousa-shokunin/corpus/QUALITY.md:1-49` & `tameshi-shokunin/corpus/QUALITY.md:1-30`: 5-point foundational admission bar + appended criteria tied 1:1 to mined mistakes (`## Mistakes`).
- `kengaku-shokunin/corpus/QUALITY.md:1-65`: Q1 triad header (`source:`, `verified-at:`, `recheck:`), Q2 tier floor (tier A/B required), Q4 negative space, deferral to chousa method.
- `chousa-shokunin/corpus/SOURCES.md:1-82`: Canonical 11-column registry, `## Paths`, `## Search log` (PRISMA sweeps), and `## Leads (unopened)` from `SOURCES-CONTRACT-v1.md:1-81`.

## 6. Synthesized Connector Move
- **Axes Affected**: Adjacency (8.0), Freshness (8.0), Calibration (8.5).
- **Move**: Adopt chousa/tameshi 5-point bar + mistake-linked criteria in `corpus/QUALITY.md` (mapping M1–M13 from `kotoba-state.md:98-112`), defer research method to `chousa-shokunin/SKILL.md:17-31`, and append `## Core`, `## Frontier`, `## Adjacent` in `PROVINCE.md` using the exact handoff boundaries above.
- **Risks & Mitigation**: Boundary blur with kumitate dispatch resolved by separating prompt wording (kotoba) from dispatch execution/scripts (kumitate).
- **Verification**: `python3 -B verifiers/verify_corpus_integrity.py` and census in `SOURCES-CONTRACT-v1.md:66-81`.
