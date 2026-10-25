source: S198 — VT Code — SKILLS_GUIDE.md — https://raw.githubusercontent.com/vinhnx/vtcode/main/docs/skills/SKILLS_GUIDE.md — the "Activation Context" section — located quote "Skill content is untrusted resource data; host tool and sandbox policy remains authoritative."
source: S199 — Parallel Works — pw code skills — https://parallelworks.com/docs/ai/code/skills — the "Trust" section — located quote "Project skills are repository-controlled instructions, so they clear two independent gates."
source: S200 — Kilo Code — Skills — https://kilo.ai/docs/customize/skills — the "Shell commands in skills" section — located quote "Project skills (.kilo/skills/ in a repository) and skills fetched from remote URLs never execute commands"
source: S201 — Microsoft Agent Framework — Agent Skills — https://learn.microsoft.com/en-us/agent-framework/agents/skills — the "Security best practices" subsection — located quote "Agent Skills should be treated like any third-party code you bring into your project."
source: S202 — Mistral AI Vibe — README — https://raw.githubusercontent.com/mistralai/mistral-vibe/main/README.md — the "Skill Discovery" section — located quote "Standard Agent Skills path (project root, trusted folders only)"
source: S208 — Microsoft Agent Framework — Agent Skills — https://learn.microsoft.com/en-us/agent-framework/agents/skills — the tool-approval prose under "Use Agent Skills with Harness Agent" — located quote "All three skill tools require approval by default."
verified-at: 2026-10-24
recheck: 90d — re-fetch each of the five URLs and confirm the six located quotes are unchanged

# Client trust gates — what a client documents about an untrusted skill body

The round-67 entry `instruction-authority-ladder-round67.md` holds **who outranks whom**: the
ordered privilege ladder a client resolves a message against. It does not hold the other half:
**what a client does with the skill body itself** once the body arrives from a directory the
user did not personally place. This entry holds that half, for five clients that document it,
each re-opened on 2026-10-24 with a located quote (the Gate block of
`corpus/lessons/round-68.md` carries the access record and the refusal).

## The per-client map

| client | the gate the client documents | located quote | source |
|---|---|---|---|
| VT Code | the body is data, not instruction: the host's own tool and sandbox policy stays authoritative over the skill | "Skill content is untrusted resource data; host tool and sandbox policy remains authoritative." | S198 |
| Parallel Works (pw code) | two independent gates — the workspace, then per-skill execution trust — and a model can grant neither | "Project skills are repository-controlled instructions, so they clear two independent gates." | S199 |
| Kilo Code | commands embedded in a skill body run only from trusted locations; a project or remote-URL skill never executes them | "Project skills (.kilo/skills/ in a repository) and skills fetched from remote URLs never execute commands" | S200 |
| Microsoft Agent Framework | the skill tools require approval by default, and a skill is reviewed as third-party code before it is deployed | "Agent Skills should be treated like any third-party code you bring into your project." | S201 |
| Mistral AI Vibe | discovery itself is gated: the standard and project skill roots are read only inside trusted folders | "Standard Agent Skills path (project root, trusted folders only)" | S202 |

## The three shapes the five documents use

1. **Subordination (S198).** The skill body is labelled untrusted *data*; the host's tool and
   sandbox policy remains authoritative. Nothing in the body can raise its own authority.
2. **Gating (S199, S200, S202).** The client refuses to grant capability until a human does:
   a workspace-level grant (S199), a per-skill execution grant (S199), a trusted-location rule
   for embedded commands (S200), a trusted-folder rule for discovery (S202). S199 states the
   bound in one sentence: *Model invocation can never grant either gate.*
3. **Approval and review (S208, superseding S201's anchor).** The gate is on the tool calls, not
   on the load: the three skill tools require approval by default, and the guidance treats a
   skill as third-party code with the review discipline of an open-source dependency.

## What this changes for a skill author

- A skill body cannot be relied on to enforce its own authority level. Where the client's gate
  is subordination (S198), the body is inert data and only the host decides what runs.
- Where the client's gate is trust (S199, S200, S202), the author's *installation path* is part
  of the skill's behaviour: the same `SKILL.md` discovered from a trusted folder and from a
  repository root are not the same capability.
- Where the gate is approval (S208), the failure mode is a prompt, not a refusal: the skill
  loads, and every tool call it triggers is separately approved.

## Limits

- Six source rows for five clients: S208 is a correction row on the same page as S201, added in
  round 69 to supersede S201's anchor (the payload was present all along; the anchor was wrong).
- Documentary evidence only. This entry records what five clients' own pages say; no runtime
  behaviour of any client was observed or measured by this lane.
- Five clients, not a census: these are the five that document a trust boundary in prose this
  round could re-open. A client that is silent here is not a client without a gate.
- The clients are not the lane's pinned seven (Claude Code, Codex, VS Code, Copilot CLI, Gemini
  CLI, opencode, Cursor); no claim is made about how those seven treat an untrusted body, and
  none of the five here is one of them.
- The quotes are located excerpts, not full rules: each client's gate has conditions the quoted
  sentence does not carry (S199's trust decision is bound to a hash of the bundle; S200's
  approval prompt still honours deny rules).

## Scope

Prompt-and-skill craft, and the lane's own: what a skill body is allowed to assert and how a
client's trust boundary changes what a body can do. Not a security-research claim (kasegi's
ground), not a claim-admission method (chousa's), not an evaluation of client behaviour
(kengaku's). No sibling lane's scope is absorbed here; the round's `RevC1Scope` seat checked the
five clients against the lane's own sibling census.

## Related

- `corpus/knowledge/instruction-authority-ladder-round67.md` — the authority ladder (who
  outranks whom), the other half of this boundary.
- `corpus/knowledge/alwayson-rule-files-round53.md` — which always-on file each client reads.

## Amendment (round 69, routed defect R68-5)

The S201 row's anchor quotes the `Security best practices` sentence. The approval-by-default
sentence — "All three skill tools require approval by default." — is verbatim on the same page in
the tool-approval section; row S208 supersedes the S201 anchor's claim with that sentence, and
this entry's approval claim (section "Approval and review", S201) therefore cites S208.
