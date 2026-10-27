Assimilation cross-check — round 79, S06

## Staged assertions and live-page comparison

The staged entry `knowledge/corpus/knowledge/client-frontmatter-and-discovery-divergence.md` (2026-10-23) does not assert any `allowed-tools` semantics per client. It says only that the specification's canonical frontmatter list includes optional `allowed-tools` (S255), within this quote: “optional `license`, `compatibility`, `metadata`, `allowed-tools`” (entry lines 12–15). Its other assertions concern Deep Code and Junie field requirements and discovery, not allowed-tools. The cited S255 is `https://agentskills.io/skill.md`; the only staged `allowed-tools` source-row match I found is SOURCES.append.md S255.

Commands and outputs:

`grep -n 'allowed-tools\|frontmatter divergence' /home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md`
Output excerpts: S255 row describes canonical frontmatter list `name`, `description`, optional `license`, `compatibility`, `metadata`, `allowed-tools`; S295 row is Claude Japanese localization and describes a per-skill permission field. Other grep matches included S216/S217, S255, S295; no additional rows specifically about the staged entry's S250/S252/S255.

I fetched the six current URLs directly with JS `fetch`; exact observed result summary:

- Spec `https://agentskills.io/specification.md`: HTTP 200, 7,578 chars. Hit: `| allowed-tools | No | Space-separated string of pre-approved tools the skill may use. (Experimental) |` The staged assertion that the open spec lists this optional field agrees; live text further describes it as experimental and pre-approved.
- Claude Code `https://code.claude.com/docs/en/skills.md`: HTTP 200, 117,904 chars. Hit: `Tools Claude can use without asking permission during the turn that invokes this skill.` Agreement on field presence, with materially specific per-turn grant semantics. No Claude claim is made by staged entry.
- Factory `https://docs.factory.ai/cli/configuration/skills`: HTTP 200, 341,233 chars. Live hit: `Droid stores it as skill metadata and shows it in skill surfaces, but standard skill invocation is not a runtime sandbox. A skill cannot add tools that are unavailable in the current session.` This surfaces metadata and explicitly says not a security boundary. Staged entry is silent about Factory.
- Microsoft Agent Framework `https://learn.microsoft.com/en-us/agent-framework/agents/skills`: HTTP 200, 157,288 chars; one `allowed-tools` hit in a table-cell only in the lightweight fetch extraction. Insufficient context to determine semantics: silent/unresolved, not disagreement.
- pi `https://raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/docs/skills.md`: HTTP 200, 4,741 chars. Hit: `| allowed-tools | Experimental pre-approved tool list |`. Staged entry silent.
- Mistral Vibe `https://raw.githubusercontent.com/mistralai/mistral-vibe/main/README.md`: HTTP 200, 77,288 chars; hit `allowed-tools:`. Staged entry silent.

Thus no staged allowed-tools semantic assertion is contradicted by live text. Current spec corroborates the sole assertion. Live Factory and Claude semantics are not present in the staged entry, so cannot be classified as disagreements. This is not a full semantic audit of MS Agent Framework or Vibe: the fetch extraction did not preserve enough surrounding context.

## ID collision check and fixture guard

Not completed: round prompt §6.10 was not present in the lane plan/readable local material found during this seat, so the required exact grep-extracted id-list commands, registry fixture shape, and guard command were unavailable. I did not invent substitutes or claim collision results.

## Absent-defect register

Not completed: the requested awk expression from prompt §6.10 was unavailable. No S-id slice/count is asserted.

## Recommendation

Lead-only: the staged entry's one allowed-tools mention is a source-list fact corroborated by the current specification, but it contains no client-by-client permission semantics and the staged id/collision/register checks remain unperformed; do not adopt it as the C2 map.

VERDICT: Lead-only cross-check; no live-page disagreement observed for the staged entry's sole allowed-tools assertion; required collision/register checks unresolved.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/w1/Kb79S06AssimStaged.md