# Agent-definition audit — round 6

Sourced 2026-09-28. An independent L2 reviewer lane applied the 9-item
agent-definition fidelity checklist (SKILL.md, added this round) verbatim to
all 18 non-bak files under `~/.config/opencode/agents/`; L1 re-verified every
cited defect by hand. Second end-to-end domain task after the round-5
SKILL.md fleet audit.

## Verdict matrix (18 files × AD-1…AD-9)

15/18 files clean. 4 fail cells total:

| File | AD-1 | AD-2 | AD-3 | AD-4 | AD-5 | AD-6 | AD-7 | AD-8 | AD-9 |
|------|------|------|------|------|------|------|------|------|------|
| bootstrapper | ✓ | ✓ | ✓ | n/a | ✓ | ✓ | ✓ | ✓ | ✓* |
| connector | ✓ | ✓ | ✓ | n/a | ✓ | ✓ | ✓ | ✓ | ✓ |
| critic | ✓ | ✓ | ✓ | n/a | ✓ | ✓ | ✓ | ✓ | ✓ |
| distiller | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| executor | ✓ | ✓ | ✓ | n/a | ✓ | ✓ | ✓ | ✓ | ✓ |
| janitor | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| labrat | ✓ | ✓ | ✓ | n/a | ✓ | ✓ | ✓ | ✓ | ✓ |
| mutation-tester | ✓ | ✓ | ✓ | n/a | ✓ | ✓ | **✗** | ✓ | ✓ |
| musketeer | ✓ | ✓ | ✓ | n/a | ✓ | ✓ | ✓ | ✓ | ✓ |
| orch | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| planner | ✓ | ✓ | ✓ | n/a | ✓ | ✓ | ✓ | ✓ | ✓ |
| revenger | ✓ | ✓ | ✓ | n/a | ✓ | ✓ | ✓ | ✓ | ✓ |
| reviewer | ✓ | ✓ | ✓ | n/a | ✓ | ✓ | ✓ | ✓ | ✓ |
| scout | ✓ | ✓ | ✓ | n/a | ✓ | ✓ | ✓ | ✓ | **✗** |
| sentinel | ✓ | ✓ | ✓ | n/a | ✓ | ✓ | ✓ | ✓ | ✓* |
| scribe | ✓ | ✓ | ✓ | n/a | ✓ | ✓ | ✓ | ✓ | ✓ |
| simplifier | ✓ | ✓ | ✓ | n/a | ✓ | ✓ | ✓ | ✓ | ✓ |
| ufo | **✗** | ✓ | ✓ | ✓ | **✗** | ✓ | ✓ | ✓ | ✓ |

## Verified failures (L1 re-checked)

1. **ufo.md AD-1** — no `name:` key in frontmatter (lines 1–9 open with
   `description`/`mode`/`model`/`cascade_class`/`cascade`/`cascade_note`/
   `variant`). Every other file has `name: <stem>` at line 2. opencode falls
   back to the file stem, so the failure is latent not behavioral — still a
   consistency defect (only file missing the key).
2. **ufo.md AD-5** — stale dated `cascade_note` at line 7: "…parked … until
   2026-08-29 23:48 UTC" — 30 days stale at audit time, plus a live seat
   assignment ("OpenCode Go depleted and parked"). Prior round-4 finding
   confirmed unfixed.
3. **mutation-tester.md AD-7** — the 9-line godspeed preamble appears twice
   verbatim (lines 8–14 and 34–40). Prior round-4 finding confirmed unfixed.
4. **scout.md AD-9** — body declares `aaron` "on PATH" (line 38) as the
   unconditional primary runner; `command -v aaron` returns nothing; install
   instructions at line 53 but no runtime absence fallback. `the-` prefixed
   names in bodies (the-scout, the-reviewer, …) match no enrollment key —
   only `the-janitor` is a real binary.

## Reachability (AD-2 detail)

- `opencode.json` `agent` map enrolls 15 of 18 files; `ufo` is
  `default_agent`. distiller/janitor/musketeer are reachable only via
  `orch.md` `subagents:` (16 entries, all resolve). Config also holds
  fileless keys devin/kimi/raw (+ disabled general/explore) — outside the
  file audit's scope but a real roster asymmetry: *config-only agents have no
  auditable body file*.

## Corrections to round-4 claims (filed by audit, L1-verified)

- Gods­peed preamble count is **14/18**, not 13 (orch.md:23 carries it too).
- Negative-routing tagline count is **11/18**, not 7 (connector, critic,
  distiller, executor, labrat, mutation-tester, reviewer, scout, scribe,
  sentinel, simplifier all carry `NOT …` cues).

## Checklist meta-findings → resolutions (all landed in SKILL.md this round)

| # | Finding | Resolution |
|---|---------|-----------|
| 1 | AD-1 absent-name vs file-stem fallback | Keep FAIL but record as *latent*: fallbacks don't excuse inconsistency; note added to item |
| 2 | No item governs `description` itself; round-indexed ops text at connector.md:3, planner.md:3 | AD-5 widened to "frontmatter including description" |
| 3 | AD-4's recognized-key list can't enumerate real keys (mode/variant/cascade_class/permission maps/steps) | AD-4 reworded: keys must resolve against the target harness's agent schema, not a fixed list |
| 4 | AD-5 frontmatter-only; musketeer.md:22 dated body anecdote ungoverned | AD-6 already covers body staleness; noted the body-vs-frontmatter split explicitly |
| 5 | Body file references (`../godspeed-core/directive.md`) unresolvable from file location though content hash-verified | AD-9 extended: file paths must resolve from the file's own dir or a named base (same rule as SKILL.md citations) |
| 6 | AD-9 "command" undefined for harness tool names (SendMessage/TaskCreate/…) | AD-9 scoped to external binaries + file paths; harness tool/role literals governed by host tool surface — new clause |
| 7 | `the-`-prefixed role literals match no enrollment key | Folded into AD-4: delegated names in body tables must match enrollment keys |
| 8 | Count corrections (13→14, 7→11) | Fixed in SKILL.md Sources + this file |
| 9 | Near-duplicate blocks pass strict AD-7 (labrat.md two different DESPAWN templates; orch.md `## Handoff` reused with different semantics) | AD-7 extended: same-name/anchor blocks with *differing* content are a conflict defect, not just duplication |
| 10 | bootstrapper.md "vendored in this repo" — repo base unnamed | Covered by resolved AD-9 file-path clause; PASS* kept (stated STOP-check mitigates) |

## Read

The agent-definition fleet is far healthier than the sibling SKILL.md fleet
(15/18 clean vs 0/5 on trigger items) — the difference is these files were
hand-maintained, not template-minted. All 4 fails are drift defects (stale
notes, duplicated preamble, missing name, missing binary), zero are design
defects. Fixes are cross-domain: reported, not landed.
