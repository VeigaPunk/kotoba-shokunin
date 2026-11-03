# kotoba: curated sources to consider after hyaku

Date: 2026-11-03

**Status: unassimilated future reading.** These are candidate references, not trained knowledge, verified local capabilities, adopted dependencies, or changes to current training. Reserved for possible post-hyaku assimilation under the lane’s normal admission review. Earlier dated reflections remain unchanged.

Selection checked against the supplied PROVINCE, source registry and considerthese context, including exact URLs and source-entity mentions. No candidate code was executed.

## 1. Anthropic: Effective context engineering for AI agents

- Type: Practitioner methodology.
- Primary source: <https://www.anthropic.com/research/effective-context-engineering-for-ai-agents>
- Why this is worth considering: Extends prompt craft to the selection and organization of instructions, tool descriptions and retained context. Useful for examining whether a skill’s compact wording preserves the decisions and constraints needed at invocation time.
- Possible later exercise: After hyaku, review one skill in two paper variants: a concise entry point with references and an all-in-one body. Specify positive triggers, near-miss negatives and the constraints that must survive compression before any experiment.
- Boundaries and caveats: Vendor practice is a hypothesis source, not a universal model guarantee or proof of client loading behavior. Keep runtime orchestration with kumitate and measured capability comparisons with kengaku.
- License/reuse: No open reuse license established from article; link and original summary only.
- Currency/maintenance: Official article dated 2025-09-29; fetched 2026-11-03. The engineering URL redirects to this research URL.
- Duplicate check: no exact primary URL or source-entity match in the supplied lane context.

## 2. Promptfoo: declarative prompt regression cases

- Type: Repository.
- Primary source: <https://github.com/promptfoo/promptfoo>
- Why this is worth considering: A practical reference for expressing prompt variants, input cases and assertions separately. It can inform regression design for trigger fidelity and output contracts without replacing the lane’s existing client-specific rule authorities.
- Possible later exercise: After hyaku, design a small held-out table of must-trigger, must-not-trigger and ambiguous skill requests. Specify exact assertions where possible and record each client/model/context pin; do not turn this into an unqualified model ranking.
- Boundaries and caveats: Provider calls can incur cost or transmit prompt data; execution is not authorized here. Red-team scanning and deployment are outside this reading proposal. Synthetic tests do not prove an installed client actually loads or selects a skill.
- License/reuse: MIT for repository code. Evidence: <https://raw.githubusercontent.com/promptfoo/promptfoo/main/LICENSE>.
- Currency/maintenance: Official release page lists 0.125.1 dated 2026-10-25, verified 2026-11-03.
- Duplicate check: no exact primary URL or source-entity match in the supplied lane context.
- Supporting evidence: <https://www.promptfoo.dev/docs/configuration/test-cases/>, <https://github.com/promptfoo/promptfoo/releases>.

Selection note: DSPy was considered but excluded because the existing reading context already queues dspy.GEPA, ACE and GEPA. Promptfoo adds a different regression-specification angle rather than re-listing that queued optimizer family.
