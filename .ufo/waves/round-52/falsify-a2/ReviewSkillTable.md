Result: HOLDS — every cell of the SKILL.md `instructions` table (SKILL.md:86-94) is supported by the entry and rows S032–S037, no universal clause exceeds the sources, and `verify_skill_checklist.py` is fully green (11 pass / 0 fail) at the judged revision.

Seat: KotobaR52a2.ReviewSkillTable. Target: the MCP `instructions` table added to
`/home/vgpnk/Projects/shokunin/kotoba-shokunin/SKILL.md` § Instruction surfaces,
lines 86-94, judged at `c8407a453788df964df5a7b835dd0ce1360de882`. Lane
`git diff -- SKILL.md` is empty, so the working tree equals the judged revision
(exit 0, no output).

## Cell-by-cell audit (SKILL.md:86-94 vs corpus/knowledge/mcp-server-instructions-round52.md)

Lead line (:86-87): "server-wide text the server returns at `initialize`; the spec
makes it optional and leaves placement to the client." Supported: entry row S032
(mcp-server-instructions-round52.md:23) and SOURCES S032 ("the schema leaves its
placement to the client"). Live check: fetched schema.md
2026-10-22T17:54:48Z, 130,800 B, sha256 5ab7cfcd5ea05c74… — byte-identical to the
S032 pin; `instructions?: string` optional and the description only gives a MAY
example ("this information MAY be added to the system prompt"), never a placement
mandate. Holds.

Row 1 (:91) "about the whole server: cross-tool order, constraints, rate limits →
the server's `instructions`, first 512 characters self-contained": Supported.
Codex mcp.md:197-199 live-verbatim: "uses it as server-wide guidance alongside the
server's tools" and "use `instructions` for cross-tool workflows, constraints, and
rate limits… Keep the first 512 characters self-contained" (S035 fetched
26,995 B, sha256 c78df8c70b7f31f7… — identical to pin). Claude Code 4,096-char
default cut confirmed on live bytes (line 1506). Choosing the smallest documented
budget as the row's rule is the entry's own craft point 2. One nit: the table's
"cross-tool order" narrows the documented "cross-tool workflows" — cosmetic, LOW.

Row 2 (:92) "about when to reach for the server at all → `instructions`": Supported,
and correctly scoped. The why cell says "with tool search" — the conditional fact
is not overclaimed. Live S033 (see drift note below): "Only tool names and server
instructions load at session start" and "Server instructions help Claude
understand when to search for your tools, similar to how skills work."

Row 3 (:93) "about one tool's inputs → that tool's `description`": The why cell
("not repeated per tool; Claude Code, VS Code (S034), Codex and Gemini CLI (S036)
put `instructions` in front of the model already") is fully backed: all four
placements are documented (S034 release notes byte-identical, sha256
19d9259e93ab3109…, "will include them in its base prompt"; S036
43,656 B, sha256 4aefc4dc30c329cb…, "appended to the system instructions").
The placement advice "that tool's `description`" is the only cell not backed by a
literal source sentence — it follows from the server-wide reading (entry craft
point 1) since `description` is the per-tool text field. Reasonable inference, but
it is an inference: LOW.

Row 4 (:94) "needed on every client → a skill or always-on file too": Supported and
carefully bounded — "the opencode and Copilot CLI pages opened on 2026-10-22 say
nothing about server instructions (entry § sweep)"; the entry itself disclaims
"does not use server instructions" (:37). No universal clause.

Universal-clause check: the only universal-sounding clauses are "the spec makes it
optional and leaves placement to the client" (S032, verbatim-backed) and row 2's
unconditional "put it in `instructions`" — but the latter's evidence is conditional
and the cell says so. No universal clause lacks source support.

## Verifier run (sandbox clone at c8407a4)

Setup: `git clone -q <lane> /fast/scratch/hyaku/kotoba-r52a2/fleet/kotoba-shokunin`,
`checkout -q c8407a45…`, plus parent symlinks `.ufo PROTOCOL.md AXES.md MISSION.md
SCORECARD.md shared kasegi-shokunin -> /home/vgpnk/Projects/shokunin/*` so
`../`-rooted citations and `name == directory` resolve as in the lane. (A first
run without this layout failed artifactually — dir-name and `..` resolution — not
a revision defect.)

`cd /fast/scratch/hyaku/kotoba-r52a2/fleet/kotoba-shokunin && python3 -B verifiers/verify_skill_checklist.py --json` → exit 0:

    pass 11, fail 0, na 0 — all 11 checks PASS, including
    checklist.box_map_complete  (41 boxes mapped; 8 executed, 2 delegated, 31 unexecuted)
    trigger.line_budget         "587 lines within budget 600 (from box at line 271)"
    trigger.citation_resolves   "53 repo-rooted citation token(s) resolve"
    governance.citation_resolves "984 governance citation token(s) resolve across 2 files"
    trigger.frontmatter_parses  "description 1019 chars"

Budgets: file budget 587/600 — 13 lines of headroom, no break. The box at
SKILL.md:271 is the operative budget; no per-section budget exists in the
checklist. The MCP table added ~9 lines and left the section's prose intact.
Frontmatter description is 1019 chars (no check enforces a cap; informational).

## Findings

- LOW — SKILL.md:93 row 3 "put it in: that tool's `description`" is an inference,
  not a documented sentence; the why cell's evidence supports only the
  "not repeated per tool" half. Parenthetical "Codex and Gemini CLI (S036)"
  also under-cites Codex (S035), though S035 is cited in row 1.
- LOW — SKILL.md:91 "cross-tool order" narrows the documented "cross-tool
  workflows" (S035 live text).
- Info — Claude Code page (S033) drifted since the 17:04Z pin: 128,298 B vs
  127,022 B, sha256 9ec4942d… vs 9a42e98f…; the cited quote moved :1468→:1488 and
  the 4,096 cut :1484-1486→:1506 (new "MCP Apps UI resources" content). All cited
  facts remain verbatim on live bytes; the pinned locations are now ~20 lines
  stale. Counter and entry quotes unaffected.
- Info — S037 (tier B blog) is cited in the lead range but not in any table cell;
  appropriate, since it documents implementer transparency, not placement.

No MEDIUM+ findings. The table HOLDS as documentation-faithful.

## Residual risk / verification gaps

- Whether Claude Code exposes `instructions` to the model when tool search is OFF
  is not stated on the live page (implicit only); row 3's "in front of the model
  already" for Claude Code is a documented-default reading, not a measured one.
  Entry already scopes to documentation statements.
- opencode/Copilot CLI silence is bounded to the two pages opened 2026-10-22;
  source code unread — correctly disclaimed at entry :36-37.
- Entry line-number pins for S033 are stale vs live (drift above); a future
  `--fetch` re-pin may want refreshed line cites.
