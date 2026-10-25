source: S255 — Agent Skills — skill.md (the format one-pager) — https://agentskills.io/skill.md — the "Product summary" and "Key files and paths" sections — located quote "at startup they load only the name and description of each skill (~50-100 tokens per skill)"
source: S262 — Factory Documentation — Skills — https://docs.factory.ai/cli/configuration/skills — the "Skills" page under the Droid harness — located quote "Use skills when instructions are too specific for always-on `AGENTS.md`"
source: S263 — pi-mono — coding agent — Skills — https://raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/docs/skills.md — the "# Skills" heading — located quote "Pi advertises each available skill by name and description, then loads its full instructions only when the task calls for them."
verified-at: 2026-10-25
recheck: 90d — re-fetch all three pages and confirm each located quote and the rung boundary it carries are unchanged

# The middle rung and the resident index — what belongs in a skill, an always-on file, or a one-off prompt

The lane had inferred the three-rung instruction ladder from how each client implements loading:
a one-off prompt below, a skill in the middle, an always-on context file above. Two of the three
vendors in the round-72 assimilation package state that middle rung in their own words, and the
specification's own one-pager states the cost side that makes the top rung an index rather than a
payload.

## What the three rows state

| rung | the sentence it rests on | what it decides for an author | source |
|---|---|---|---|
| one-off `prompt` | "too structured for a one-off prompt" (the same sentence that names the skill rung) | a use that happens once is a prompt, not a file | S262 |
| `skill` | "Use skills when instructions are too specific for always-on `AGENTS.md`, too structured for a one-off prompt, and useful enough to reuse." | reusable, specific, too shaped to be a prompt: this is the skill's ground | S262 |
| `skill` (second vendor) | "Pi advertises each available skill by name and description, then loads its full instructions only when the task calls for them." | the middle rung is on-demand by construction, and its resident part is name + description | S263 |
| `always-on` file | "at startup they load only the name and description of each skill (~50-100 tokens per skill)" | the resident surface is an index; the payload is what must stay retrievable | S255 |

## The rule this entry carries

A skill is for instructions that are too specific for an always-on file and too shaped for a
one-off prompt, and that are reused. When the choice is between the skill rung and the always-on
rung, the always-on file stays an index — names and descriptions resident, the payload
retrievable — because the resident surface is the one every turn pays for.

## What the rows do not settle

S262 and S263 name the boundary between the prompt rung and the skill rung, not the boundary
between the skill rung and the always-on rung: neither states when a rule must be resident
rather than retrievable. S255 states the resident cost of a skill catalogue, not the size at
which an always-on block stops paying. The invocation failure the lane measured (a skill that
is offered and never invoked) is the failure of the middle rung, and none of these three rows
measures it.

## Provenance (this draft)

Fetched and pinned by seat ExecAuthorControls on 2026-10-25; every located quote above was
re-found in the pinned bytes by a literal word-bounded search before the world was committed.
`docs.factory.ai/cli/configuration/skills` answers 308 to `docs.factory.com/harness/skills`; the
snapshot is the page's own `.md` sibling at the same path, so the bytes are the served text and
not a rendered HTML page. Sha256 of each snapshot is in `.ufo/waves/round-72/snapshots/<id>.sha256` (and `pins.json`).
