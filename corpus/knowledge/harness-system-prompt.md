# Harness-injected system prompts — observed class, not owned

Sourced 2026-09-28 (round 5). The sixth instruction surface on this host:
injected into every session by the runtime; no writable file owns it. This
lane observes it directly — the notes below are drawn from this session's own
preamble. Marked observed-not-owned: no file path to cite, so every claim
here is `[INFERENCE]`-grade evidence unless re-observed.

## Observed anatomy

- **RFC 2119 keyword contract up front.** The preamble declares the MUST/
  SHOULD/MAY vocabulary before any rule uses it — the normative-force legend
  precedes the rules that depend on it. Craft rule: declare the force
  vocabulary before first use, not inline.
- **Sectioned, not ordered.** Unlike SKILL.md's load-order anatomy, the
  preamble is a flat set of named sections (role → engineering → personality/
  tone → reasoning format → escalation → runtime/skills → tool policy →
  exploration → delegation → workflow → delivery contract → critical). The
  reader enters at any section; there is no gate→decide→act spine.
- **Constraint density ≈ AGENTS.md, scope ≈ SKILL.md.** Per-byte it reads like
  an always-on constraint file (`NEVER`, `MUST`, `AVOID`), but its content is
  full behavioral policy — tone, verification gates, delegation rules. It is
  the only surface that pays both costs: always-loaded *and* comprehensive.
- **Machine-level criticality markers.** `<critical>` blocks mark
  non-negotiable rules (no fabrication, no yield-before-done) separately from
  SHOULD-grade guidance — an explicit severity tier system missing from the
  other five surfaces, which rely on MUST/NEVER wording alone.
- **Anti-injection hygiene.** A declaration that XML tags may inject system
  content and user content is sanitized — the only surface that carries its
  own threat model.

## Craft implication (opinion)

- For writable surfaces, borrow the severity tiering: an explicit "this is
  inviolable" marker beats relying on MUST alone in a long file. SKILL.md's
  `## Refusals` + checklist are the closest writable analogue.
- Because this surface is always-loaded *and* comprehensive, its compression
  pressure is the strictest of any surface — every byte is paid every session
  by every agent. The observed fix: extreme fragment density, no prose
  transitions, tables and imperative fragments only.

## Why this file is thin

Deliberately: the surface is not writable, so no checklist or procedure can
act on it. Corpus value is negative knowledge — knowing the sixth class
exists prevents misclassifying its properties as SKILL.md craft problems.
