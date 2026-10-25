# Round-1 aggregator corpus audit — kotoba

Auditor: aggregator L1 (m_qwen) + one independent L2 `reviewer` lane
(m_composer), 2026-09-28. Method: re-greped every quoted trigger string and
re-counted every line-count claim across `~/.agents/skills/*/SKILL.md` and
`~/.config/opencode/skills/ufo/SKILL.md`. Scope: `corpus/` only.

Round evidence: `LOG.md` round-1 entry; commit `1d93182`; lane report
`~/Projects/shokunin/.ufo/reports/round-1/kotoba.md`.

This audit is held to a stricter standard on purpose: kotoba's province *is*
citation and trigger fidelity in skill files, so a misattributed quote here is a
domain defect, not a typo.

## Verdict: NOT conformant — L2 reviewer verdict `fail`; 2 citation defects + 1 unfalsifiable sweep

Layout conforms (`README.md` with coverage map + gaps, `knowledge/` ×3,
`lessons/round-1.md` citing round/commit/LOG/report); no dangling index paths.
Most citations verify exactly — including every line count. The failures are
attribution and over-generalization.

## Independently re-verified

Line counts (`wc -l`, 2026-09-28) — the survey base is real and complete:

| File | Lines | File | Lines |
|---|---|---|---|
| `wwkd/SKILL.md` | 233 | `bailian-model-recommend` | 111 |
| `godspeed/SKILL.md` | **18** ✓ (claimed minimum) | `bailian-web-search` | 120 |
| `sekhmet-l3` | 94 | `bailian-gen` | 121 |
| `xbrd-ask` | 68 | `bailian-finetune` | 75 |
| `omarchy` | **392** ✓ (claimed maximum) | `bailian-sandbox` | 75 |
| `bailian-cli` | 132 | `bailian-managed-agent` | 196 |
| `bailian-protocol` | 152 | `bailian-docs-llm-wiki` | 180 |
| `bailian-train-deploy` | 200 | `opencode/skills/ufo/SKILL.md` | 161 |

16 files = the claimed survey size ✓.

| Claim | Command | Observed |
|---|---|---|
| wwkd "~600 lines per module" principle | `sed -n '64,66p' wwkd/SKILL.md` | principle 8, L64–65 ✓ |
| godspeed always-on description | `grep 'Use on every prompt' godspeed/SKILL.md` | L3 ✓ |
| omarchy anti-trigger in frontmatter | `head -12 omarchy/SKILL.md` | L10–11 "Excludes Omarchy…" inside `description` ✓ |
| bailian-gen 反触发 quote | `grep -n 反触发 bailian-gen/SKILL.md` | L16 verbatim ✓ |
| bailian-cli fail-closed gate | `sed -n '23p' bailian-cli/SKILL.md` | "stop and run `bl skill init`; do not guess auth/consent." ✓ |
| ufo fail-closed | `grep -n 'fail closed' ufo/SKILL.md` | L26–27 ✓ |
| sekhmet-l3 quoted triggers | `grep -n 'Triggers:' sekhmet-l3/SKILL.md` | L7–8 "sekhmet","swarm","L3","fan out","parallel probes","spark" ✓ |
| sekhmet symlink warning | `grep -n 'symlink titanium' sekhmet-l3/SKILL.md` | L31–32 ✓ |
| internal counts of the lane's own SKILL.md | count rows/items | 7-organ anatomy table (rows 0–6), 7 frontmatter rules, 13-item checklist, 8 anti-pattern rows ✓ |

## Defects filed

1. **Fabricated-location quote (hard failure).**
   `knowledge/frontmatter-trigger-surface.md` Fact 2 attributes a
   火山方舟/ark anti-trigger to `bailian-train-deploy`'s **frontmatter**.
   `grep -E '火山方舟|ark' bailian-train-deploy/SKILL.md` → **no match**; the
   file's anti-routing lives in the body under `## 反触发表` (L42+). The
   underlying craft point (anti-triggers belong in the description) is supported
   by omarchy and bailian-gen — the train-deploy citation must be dropped or
   re-pointed at a file that actually does it.
2. **Over-generalized family claim.** Fact 5 states
   `metadata.requires.bins: ["bl"]` "across the bailian family".
   `grep -L 'requires:' bailian-*/SKILL.md` → 3 of 10 lack `metadata.requires`
   entirely (`bailian-docs-llm-wiki`, `bailian-model-recommend`,
   `bailian-train-deploy`); 7 carry `bins: ["bl"]`. Correct form: "7 of 10".
3. **Unfalsifiable negative.** `knowledge/anatomy-and-compression.md` asserts
   "counterexample none found" for in-body trigger restatement with no search
   command attached. A negative claim needs its sweep (`grep -c` over the 16
   files, printed) or it is an unverifiable claim under `CORPUS.md`.
4. **Location nuance.** Fact 1's implicit-intent example
   (`bailian-model-recommend` "我想做一个XX") sits in the **body** (L23–24,
   适用场景), not the `description`. The rule survives; the exemplar must be
   labelled body-sourced, otherwise the file teaches the opposite of its own
   "anti-triggers belong in frontmatter" point.

## Gaps for the next round

- `AGENTS.md` craft (README already files it) — the six child `AGENTS.md` files
  in this fleet are a 5-line template identical modulo the repo name in line 1
  (`diff kasegi-shokunin/AGENTS.md kagi-shokunin/AGENTS.md` → only the
  `# <repo> operating rules` heading differs): a real comparison set, unused.
- Full in-body read of `bailian-docs-llm-wiki`, `bailian-managed-agent`,
  `bailian-sandbox` (lane reported them as line-count/frontmatter-only).
- Trigger-fidelity telemetry: no router/activation log has been inspected, so
  every claim about false activation is inference from file shape. One real
  activation trace would upgrade the whole province.
- **Fleet-internal customer (cross-lane learning, not scope creep):** the six
  shokunin `SKILL.md` files written this round are kotoba's own domain artifacts
  sitting one directory up. Auditing them against the 13-item checklist is the
  cheapest available end-to-end domain task for `SHONEN.md` box 2 — and this
  audit already found the round's two worst citation defects (kumitate's
  128-lane pointer, kake's row count) using kotoba's own rules.
